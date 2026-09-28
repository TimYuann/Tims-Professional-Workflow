#!/usr/bin/env bash
# boundary-probes.sh · 复核 docs/ledger.md 写下的三条「抓不到的边界」
#
# 目的：不是重跑回归套件，而是对每一条边界问一句
#       「现在还能不能构造出绕过」。能构造的，就真的构造出来。
#
#   P-B  TMPDIR 未设置时的 macOS 每用户临时目录（/var/folders/...）
#   P-C  硬链接：稳定路径与 /tmp 下的名字指向同一个 inode
#   P-D  TOCTOU：判完到打开之间把末级软链换成指向 /tmp 的软链
#        （窗口用 55 跳的 TMPDIR 软链链人工放大；真实窗口是毫秒级）
#   P-E  挂载点：只在无 root 可构造性上给判断，构造在 mount-point-bypass.sh
#
# 只写 .pi/review-v4/probe3/ 与 /tmp 下的 probe 专用目录。
set -uo pipefail

SELF_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO="$(cd "$SELF_DIR/../../.." && pwd)"
LEDGER="$REPO/scripts/ledger.sh"
[ -f "$LEDGER" ] || { echo "被测脚本不存在: $LEDGER" >&2; exit 2; }
RUNID="$(date -u +%Y%m%dT%H%M%S)-$$"
WORK="$SELF_DIR/work-$RUNID"
TMPROOT="/tmp/tpw-probe-$RUNID"
mkdir -p "$WORK"
trap 'rm -rf "$WORK" "$TMPROOT"' EXIT

say() { printf '%s\n' "$*"; }
hr()  { printf '%s\n' "────────────────────────────────────────────────────"; }

say "被测对象: $LEDGER"
say "运行 ID:  $RUNID"
say "uid:      $(id -u)"
say

# ─────────────────────────────────────────────────────────────
hr; say "P-B · TMPDIR 未设置时，写在 macOS 每用户临时目录（confstr 的 _CS_DARWIN_USER_TEMP_DIR）下"; hr
UTD="$(getconf DARWIN_USER_TEMP_DIR 2>/dev/null || true)"
say "系统每用户临时目录: ${UTD:-<取不到>}"
if [ -n "$UTD" ] && [ -d "$UTD" ]; then
  b_target="${UTD}tpw-probe-$RUNID/b.tsv"
  out="$(cd "$WORK" && env -u TMPDIR TPW_ACTOR=probe TPW_RUN="$RUNID" bash "$LEDGER" "$b_target" P3 b "TMPDIR 未设" "系统每用户临时目录" "probe" "观察" 2>&1)"
  rc=$?
  say "调用: env -u TMPDIR ledger.sh \"$b_target\" ..."
  say "退出码: ${rc}"
  say "首行输出: $(printf '%s' "$out" | head -1)"
  if [ "$rc" -eq 0 ] && [ -f "$b_target" ]; then
    say "结论: 绕过成立——闸放行，文件真的落在系统每用户临时目录"
    say "      行数: $(wc -l < "$b_target" | tr -d ' ')"
  elif [ "$rc" -eq 3 ] && [ ! -e "$b_target" ]; then
    say "结论: 闸拦住了（退出码 3，文件未落盘）"
  else
    say "结论: UNVERIFIED——本次调用本身没跑成（退出码 ${rc}），既不算绕过也不算拦住"
  fi
  rm -f "$b_target"
else
  say "结论: 本机取不到/不存在该系统目录，无法构造（记为 UNVERIFIED）"
fi
say

# ─────────────────────────────────────────────────────────────
hr; say "P-C · 硬链接：稳定路径与 /tmp 下的名字是同一个 inode"; hr
mkdir -p "$TMPROOT/c"
c_tmp="$TMPROOT/c/target.tsv"
printf 'SENTINEL-C\n' > "$c_tmp"
c_stable="$WORK/hardlink-stable.tsv"
if ln "$c_tmp" "$c_stable" 2>/dev/null; then
  inode_a="$(ls -i "$c_tmp" | awk '{print $1}')"
  inode_b="$(ls -i "$c_stable" | awk '{print $1}')"
  say "inode: /tmp 侧=$inode_a  稳定侧=$inode_b"
  out="$(cd "$WORK" && env -u TMPDIR TPW_ACTOR=probe TPW_RUN="$RUNID" bash "$LEDGER" "$c_stable" P3 c "硬链接" "稳定路径" "probe" "观察" 2>&1)"
  rc=$?
  say "调用: ledger.sh \"$c_stable\" ..."
  say "退出码: ${rc}"
  say "同名 inode 在 /tmp 侧看到的行数: $(wc -l < "$c_tmp" | tr -d ' ')"
  if [ "$rc" -eq 0 ] && [ "$(wc -l < "$c_tmp" | tr -d ' ')" -ge 2 ]; then
    say "结论: 闸放行（退出码 0），同一 inode 的字节在 /tmp 名字下同样可见"
  else
    say "结论: 未复现（rc=${rc}）"
  fi
else
  say "结论: 本机不能跨这两处建硬链接，无法构造（记为 UNVERIFIED）"
fi
say

# ─────────────────────────────────────────────────────────────
hr; say "P-D · TOCTOU：判完→打开之间把末级软链换成指向 /tmp 的软链"; hr
mkdir -p "$WORK/stable" "$WORK/chain-end" "$TMPROOT/d"
# 末级软链：hop.tsv -> stable/landed.tsv 或 -> /tmp/.../landed.tsv，由 racer 原子替换
mkhop() { ln -sfn "$1" "$WORK/hop.tsv"; }
mkhop "$WORK/stable/landed.tsv"
# TMPDIR 侧 55 跳：只为把「判完→打开」的窗口拉长到人眼可测
prev="$WORK/chain-end"
for i in $(seq 55 -1 1); do ln -s "$prev" "$WORK/tc$i"; prev="$WORK/tc$i"; done
say "TMPDIR 链: tc1 -> tc2 -> ... -> tc55 -> chain-end（55 跳）"
say "先测一次不竞争的耗时（窗口宽度的下界）:"
t0=$(date +%s%N 2>/dev/null || echo 0)
( cd "$WORK" && TMPDIR="$WORK/tc1" TPW_ACTOR=probe TPW_RUN="$RUNID" bash "$LEDGER" "$WORK/hop.tsv" P3 calib "校准" "稳定" "probe" "观察" >/dev/null 2>&1 )
t1=$(date +%s%N 2>/dev/null || echo 0)
if [ "$t0" != "0" ]; then say "  整次调用 $(( (t1 - t0) / 1000000 )) ms（其中大部分是 TMPDIR 解析）"; fi
rm -f "$WORK/stable/landed.tsv" "$TMPROOT/d/landed.tsv"

racer() { while :; do mkhop "$TMPROOT/d/landed.tsv"; mkhop "$WORK/stable/landed.tsv"; done; }
racer & racer_pid=$!
ATTEMPTS=40
hit=0; rejected=0; clean=0; other=0
for i in $(seq 1 "$ATTEMPTS"); do
  rm -f "$WORK/stable/landed.tsv" "$TMPROOT/d/landed.tsv"
  out="$(cd "$WORK" && TMPDIR="$WORK/tc1" TPW_ACTOR=probe TPW_RUN="$RUNID" bash "$LEDGER" "$WORK/hop.tsv" P3 "d$i" "TOCTOU" "窗口内换链" "probe" "观察" 2>&1)"
  rc=$?
  if [ "$rc" -eq 0 ] && [ -f "$TMPROOT/d/landed.tsv" ]; then
    hit=$((hit + 1)); [ "$hit" -le 3 ] && say "  attempt $i: 绕过成立——字节落在 $TMPROOT/d/landed.tsv"
  elif [ "$rc" -eq 3 ]; then
    rejected=$((rejected + 1))
  elif [ "$rc" -eq 0 ] && [ -f "$WORK/stable/landed.tsv" ]; then
    clean=$((clean + 1))
  else
    other=$((other + 1))
  fi
done
kill "$racer_pid" 2>/dev/null; wait "$racer_pid" 2>/dev/null
say "$ATTEMPTS 次尝试: 绕过 $hit / 闸正常拒写 $rejected / 干净落到稳定位置 $clean / 其他 $other"
if [ "$hit" -gt 0 ]; then
  say "结论: 绕过可构造（窗口被 55 跳 TMPDIR 链放大；真实窗口是毫秒级，但性质相同）"
else
  say "结论: 本轮未命中（窗口被放大也没命中时才记为未复现）"
fi
say

# ─────────────────────────────────────────────────────────────
hr; say "P-E · 挂载点：能不能在无 root 前提下构造绕过"; hr
say "本机 /tmp、仓库同卷: $(df /tmp | awk 'NR==2{print $1}') / $(df "$REPO" | awk 'NR==2{print $1}')（都是 Data 卷）"
say "macOS 自带 mount_nullfs: $(command -v mount_nullfs || echo '不存在（macOS 没有 bind mount）')"
say "RAM 盘路线（hdiutil ram:// + newfs_hfs + mount）: 见 mount-point-bypass.sh 的实跑"
say "结论: 本机 uid=$(id -u) 就能把易失存储挂到稳定路径上并让闸放行——"
say "      这条边界不是理论上的，它已经被构造出来过（见 evidence-mount-point-bypass.txt）"
