#!/usr/bin/env bash
# mount-point-bypass.sh · 「挂载点」边界能不能真的构造出绕过
#
# docs/ledger.md 把这条写成「把临时目录 bind mount 到别的路径下，抓不到」。
# macOS 没有 bind mount；这里的等价构造是：把**易失存储（RAM 盘）挂到一个
# 看起来完全稳定的路径下**，闸只解析软链、不读挂载表，于是放行。
#
# 本机实测：uid=501（非 root）也能建 RAM 盘、newfs、mount。
# 只写 .pi/review-v4/probe3/ 下的临时工作区；结束前卸载并 eject。
set -uo pipefail

SELF_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO="$(cd "$SELF_DIR/../../.." && pwd)"
LEDGER="$REPO/scripts/ledger.sh"
RUNID="$(date -u +%Y%m%dT%H%M%S)-$$"
WORK="$SELF_DIR/work-mnt-$RUNID"
MNT="$WORK/stable/mnt"
mkdir -p "$MNT"

DEV=""
cleanup() {
  [ -n "$DEV" ] && { umount -f "$MNT" 2>/dev/null; hdiutil detach "$DEV" >/dev/null 2>&1; }
  rm -rf "$WORK"
}
trap cleanup EXIT

echo "uid=$(id -u)  （非 root）"
echo "工作区: $WORK"
echo

echo "1) 建 RAM 盘（不需要 root）"
DEV="$(hdiutil attach -nomount ram://4096 2>/dev/null | awk '{print $1}')"
[ -n "$DEV" ] || { echo "UNVERIFIED: 建不出 RAM 盘设备"; exit 2; }
echo "   RAM 盘设备: $DEV"
newfs_hfs -v TPWPROBE "$DEV" >/dev/null 2>&1 && echo "   newfs_hfs: OK" || echo "   newfs_hfs: 失败"

echo "2) 挂到稳定路径（不需要 root）"
mount -t hfs "$DEV" "$MNT" 2>&1 | head -2
mount | grep -F "$MNT" || { echo "UNVERIFIED: 挂不上去，本机不构成这条绕过"; exit 2; }
echo "   挂点 df: $(df -h "$MNT" | tail -1 | awk '{print $1, $9}')"
echo "   台账父目录所在卷 df: $(df -h "$WORK" | tail -1 | awk '{print $1, $9}')"

echo "3) 用 ledger.sh 往这个「稳定路径」写（TMPDIR 不设，排除第三条规定）"
target="$MNT/ledger.tsv"
out="$(cd "$WORK" && env -u TMPDIR TPW_ACTOR=probe TPW_RUN="$RUNID" bash "$LEDGER" "$target" P3 mnt "挂载点" "路径稳定、存储易失" "probe" "观察" 2>&1)"
rc=$?
echo "   退出码: ${rc}"
echo "   首行输出: $(printf '%s' "$out" | head -1)"
echo "   台账行数: $(wc -l < "$target" 2>/dev/null | tr -d ' ')"

echo "4) 卸载 + eject（RAM 盘释放，字节随之消失）"
umount "$MNT" 2>&1 | head -1
hdiutil detach "$DEV" >/dev/null 2>&1 && echo "   ejected $DEV"
DEV=""

if [ "$rc" -eq 0 ] && [ ! -e "$target" ]; then
  echo
  echo "结论: 绕过成立——闸放行（退出码 0），记录只存在于易失存储上，eject 后不复存在"
else
  echo
  echo "结论: 未构造出绕过（rc=${rc}，目标仍存在=$([ -e "$target" ] && echo yes || echo no)）"
fi
