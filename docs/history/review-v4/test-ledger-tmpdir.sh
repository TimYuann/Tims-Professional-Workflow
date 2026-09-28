#!/usr/bin/env bash
# test-ledger-tmpdir.sh · A9 台账「拒写临时目录」回归测试
#
# 用法:
#   bash .pi/review-v4/test-ledger-tmpdir.sh [被测 ledger.sh 路径]
# 默认被测对象: <仓库>/scripts/ledger.sh
#
# 三态: 全部通过 = PASS（退出码 0）；有 FAIL = FAIL（退出码 1）；
#       工作区本身落在临时目录等环境不可用情形 = UNVERIFIED（退出码 2）。
#
# 判据形状：每一类都给一个「会红的反例」和一个「不误报的合法变体」。
#   红方：目标会落在临时目录 → 必须拒写（退出码 3），且文件不落盘
#   绿方：目标落在稳定位置（含名为 tmp 的目录、指向稳定处的软链）→ 必须写入成功
#
# 注意：`.pi/` 被 .gitignore，这套测试不随 release 分发，是给本库自己用的。
# 这不是缺陷——它依赖本机路径形状（/tmp 的真实路径等）。

set -uo pipefail

SELF_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO="$(cd "$SELF_DIR/../.." && pwd)"
LEDGER_SH="${1:-$REPO/scripts/ledger.sh}"

[ -f "$LEDGER_SH" ] || { echo "被测脚本不存在: $LEDGER_SH" >&2; exit 2; }
# 用绝对路径：run_ledger 会先 cd 到用例目录，相对路径会失效
LEDGER_SH="$(cd "$(dirname "$LEDGER_SH")" && pwd -P)/$(basename "$LEDGER_SH")"

RUNID="$(date -u +%Y%m%dT%H%M%S)-$$"
WORK="$SELF_DIR/work-$RUNID"
TEST_TMP="/tmp/tpw-ledger-test-$RUNID"
TEST_VARTMP="/var/tmp/tpw-ledger-test-$RUNID"

PASS=0; FAIL=0; SKIP=0

ok()   { PASS=$((PASS + 1)); printf 'PASS  %s\n' "$1"; }
bad()  { FAIL=$((FAIL + 1)); printf 'FAIL  %s\n        %s\n' "$1" "$2"; }
skip() { SKIP=$((SKIP + 1)); printf 'SKIP  %s\n        %s\n' "$1" "$2"; }

cleanup() { rm -rf "$WORK" "$TEST_TMP" "$TEST_VARTMP"; }
trap cleanup EXIT

mkdir -p "$WORK"
WORK_REAL="$(cd "$WORK" && pwd -P)"
# 稳定路径用例的前提是「稳定路径真的稳定」。仓库若被放在临时目录里，
# 绿方用例本身就会（正确地）被拒写，此时整套判据无意义 → UNVERIFIED。
for root in /tmp /var/tmp "${TMPDIR:-}"; do
  [ -n "$root" ] || continue
  root_real="$(cd "$root" 2>/dev/null && pwd -P || printf '%s' "$root")"
  case "$WORK_REAL" in
    "$root_real"|"$root_real"/*)
      echo "UNVERIFIED: 工作区 $WORK_REAL 落在临时目录 $root_real 之下，稳定路径用例无法判定" >&2
      exit 2
      ;;
  esac
done

# ── 运行与断言 ────────────────────────────────────────────────

# 运行被测工具。读取 CASE_CWD / CASE_TMPDIR（__UNSET__ = 不传 TMPDIR）
LAST_RC=0; LAST_OUT=""
run_ledger() {
  local out rc
  if [ "$CASE_TMPDIR" = "__UNSET__" ]; then
    out="$(cd "$CASE_CWD" && env -u TMPDIR TPW_ACTOR=test-ledger TPW_RUN="$RUNID" bash "$LEDGER_SH" "$@" 2>&1)"
  else
    out="$(cd "$CASE_CWD" && TMPDIR="$CASE_TMPDIR" TPW_ACTOR=test-ledger TPW_RUN="$RUNID" bash "$LEDGER_SH" "$@" 2>&1)"
  fi
  rc=$?
  LAST_RC=$rc; LAST_OUT="$out"
}

# 拒写断言：退出码必须是 3；列出的路径必须不存在
check_rejected() { # NAME MUST_NOT_EXIST...
  local name="$1"; shift
  local probs="" p
  [ "$LAST_RC" -eq 3 ] || probs="退出码 $LAST_RC != 3；首行输出: $(printf '%s' "$LAST_OUT" | head -1)"
  for p in "$@"; do
    [ -e "$p" ] && probs="$probs 不该存在的路径存在: $p;"
  done
  if [ -z "$probs" ]; then ok "$name"; else bad "$name" "$probs"; fi
}

# 写入断言：退出码 0；文件存在；表头恰 1 行；数据恰 want 行；每行 8 栏
check_ledger_ok() { # NAME FILE WANT_DATA_ROWS
  local name="$1" f="$2" want="$3" probs=""
  if [ ! -f "$f" ]; then bad "$name" "文件不存在: $f"; return; fi
  local h r b
  h="$(awk -F'\t' '$1 == "actor" {c++} END {print c+0}' "$f")"
  r="$(awk -F'\t' 'NR > 1 {c++} END {print c+0}' "$f")"
  b="$(awk -F'\t' 'NF != 8 {c++} END {print c+0}' "$f")"
  [ "$h" = "1" ] || probs="$probs 表头 $h 行 != 1;"
  [ "$r" = "$want" ] || probs="$probs 数据 $r 行 != $want;"
  [ "$b" = "0" ] || probs="$probs 非 8 栏 $b 行;"
  if [ -z "$probs" ]; then ok "$name"; else bad "$name" "$probs"; fi
}

echo "被测对象: $LEDGER_SH"
echo "工作区:   $WORK"
echo "运行 ID:  $RUNID"
echo

# ── 红方：拒写 ────────────────────────────────────────────────

# C01 绝对 /tmp
CASE_CWD="$WORK"; CASE_TMPDIR="__UNSET__"
run_ledger "/tmp/tpw-$RUNID/c01/new.tsv" P3 c01 "绝对 /tmp" "定义之一" "测试" "应拒绝"
check_rejected "C01 绝对 /tmp 路径 → 拒写" "/tmp/tpw-$RUNID/c01/new.tsv"

# C02 /tmp 在 macOS 上的真实路径 /private/tmp
if [ -d /private/tmp ]; then
  CASE_CWD="$WORK"; CASE_TMPDIR="__UNSET__"
  run_ledger "/private/tmp/tpw-$RUNID/c02/new.tsv" P3 c02 "真实路径" "macOS /tmp 的真实路径" "测试" "应拒绝"
  check_rejected "C02 /private/tmp 绝对路径 → 拒写" "/private/tmp/tpw-$RUNID/c02/new.tsv"
else
  skip "C02 /private/tmp 绝对路径 → 拒写" "本机没有 /private/tmp"
fi

# C03 绝对 /var/tmp
CASE_CWD="$WORK"; CASE_TMPDIR="__UNSET__"
run_ledger "/var/tmp/tpw-$RUNID/c03/new.tsv" P3 c03 "绝对 /var/tmp" "定义之一" "测试" "应拒绝"
check_rejected "C03 绝对 /var/tmp 路径 → 拒写" "/var/tmp/tpw-$RUNID/c03/new.tsv"

# C04 相对路径经单级软链指向 /tmp（原始缺陷形状）
ln -s /tmp "$WORK/c04-link"
CASE_CWD="$WORK"; CASE_TMPDIR="__UNSET__"
run_ledger "c04-link/tpw-$RUNID/c04/new.tsv" P3 c04 "单级软链" "原始缺陷形状" "测试" "应拒绝"
check_rejected "C04 相对路径经单级软链指向 /tmp → 拒写" "/tmp/tpw-$RUNID/c04/new.tsv"

# C05 相对路径经多级软链指向 /tmp
ln -s "$WORK/c05-mid" "$WORK/c05-first"
ln -s /tmp "$WORK/c05-mid"
CASE_CWD="$WORK"; CASE_TMPDIR="__UNSET__"
run_ledger "c05-first/tpw-$RUNID/c05/new.tsv" P3 c05 "多级软链" "两跳后到 /tmp" "测试" "应拒绝"
check_rejected "C05 相对路径经多级软链指向 /tmp → 拒写" "/tmp/tpw-$RUNID/c05/new.tsv"

# C06 目标文件尚不存在、父目录是软链（中间层也不存在）
ln -s /tmp "$WORK/c06-parent"
CASE_CWD="$WORK"; CASE_TMPDIR="__UNSET__"
run_ledger "c06-parent/tpw-$RUNID/c06/a/b/new.tsv" P3 c06 "父目录软链" "末级与中间层都不存在" "测试" "应拒绝"
check_rejected "C06 父目录是软链、目标尚不存在 → 拒写" "/tmp/tpw-$RUNID/c06/a/b/new.tsv"

# C07 含 . 与 .. 的路径，真实落点仍在临时目录
ln -s /tmp "$WORK/c07"
CASE_CWD="$WORK"; CASE_TMPDIR="__UNSET__"
run_ledger "c07/./tpw-$RUNID/../tpw-$RUNID/c07/new.tsv" P3 c07 ". 与 .." "真实落点仍在 /tmp" "测试" "应拒绝"
check_rejected "C07 含 . / .. 的相对路径 → 拒写" "/tmp/tpw-$RUNID/c07/new.tsv"

# C08 TMPDIR 指到别处：该处即临时目录
mkdir -p "$WORK/custom-tmp"
CASE_CWD="$WORK"; CASE_TMPDIR="$WORK/custom-tmp"
run_ledger "$WORK/custom-tmp/tpw-$RUNID/c08/new.tsv" P3 c08 "TMPDIR" "TMPDIR 指向处" "测试" "应拒绝"
check_rejected "C08 TMPDIR 指向别处 → 按该处拒写" "$WORK/custom-tmp/tpw-$RUNID/c08/new.tsv"

# C09 TMPDIR 带尾斜杠（macOS 默认 TMPDIR 就带）
mkdir -p "$WORK/custom-tmp"
CASE_CWD="$WORK"; CASE_TMPDIR="$WORK/custom-tmp/"
run_ledger "$WORK/custom-tmp/tpw-$RUNID/c09/new.tsv" P3 c09 "TMPDIR 尾斜杠" "TMPDIR 指向处" "测试" "应拒绝"
check_rejected "C09 TMPDIR 带尾斜杠 → 拒写" "$WORK/custom-tmp/tpw-$RUNID/c09/new.tsv"

# C10 TMPDIR 本身是软链：按真实路径判
ln -s "$WORK/custom-tmp" "$WORK/tmpdir-link"
CASE_CWD="$WORK"; CASE_TMPDIR="$WORK/tmpdir-link"
run_ledger "$WORK/tmpdir-link/tpw-$RUNID/c10/new.tsv" P3 c10 "TMPDIR 软链" "TMPDIR 经软链" "测试" "应拒绝"
check_rejected "C10 TMPDIR 经软链 → 按真实位置拒写" "$WORK/custom-tmp/tpw-$RUNID/c10/new.tsv"

# C12 目标路径本身是指向 /tmp 的软链（目标文件存在）→ 拒写，且不改动原文件
# 判断理由：追加打开跟随软链，字节落在 /tmp；判「字节落在哪」而不是「路径名长什么样」。
mkdir -p "/tmp/tpw-$RUNID/c12"
printf 'SENTINEL-12' > "/tmp/tpw-$RUNID/c12/target.tsv"
ln -s "/tmp/tpw-$RUNID/c12/target.tsv" "$WORK/c12-leaf.tsv"
CASE_CWD="$WORK"; CASE_TMPDIR="__UNSET__"
run_ledger "$WORK/c12-leaf.tsv" P3 c12 "末级软链" "指向 /tmp 下的已存在文件" "测试" "应拒绝"
if [ "$LAST_RC" -eq 3 ] && [ "$(cat "/tmp/tpw-$RUNID/c12/target.tsv")" = "SENTINEL-12" ]; then
  ok "C12 末级软链指向 /tmp（文件已存在）→ 拒写且原文件未被追加"
else
  bad "C12 末级软链指向 /tmp（文件已存在）→ 拒写且原文件未被追加" \
      "rc=$LAST_RC 内容=[$(cat "/tmp/tpw-$RUNID/c12/target.tsv" 2>/dev/null)]"
fi

# C13 目标路径本身是悬空软链，指向 /tmp 下尚不存在的位置 → 拒写，且不创建
ln -s "/tmp/tpw-$RUNID/c13-never.tsv" "$WORK/c13-leaf.tsv"
CASE_CWD="$WORK"; CASE_TMPDIR="__UNSET__"
run_ledger "$WORK/c13-leaf.tsv" P3 c13 "悬空软链" "指向 /tmp 下不存在的位置" "测试" "应拒绝"
check_rejected "C13 末级悬空软链指向 /tmp → 拒写且不创建" "/tmp/tpw-$RUNID/c13-never.tsv"

# C20 软链成环：无法解析 → 拒写（退出码 4），不猜
ln -s "$WORK/loop-b" "$WORK/loop-a"
ln -s "$WORK/loop-a" "$WORK/loop-b"
CASE_CWD="$WORK"; CASE_TMPDIR="__UNSET__"
run_ledger "$WORK/loop-a" P3 c20 "软链成环" "真实路径不可解析" "测试" "应拒写"
if [ "$LAST_RC" -eq 4 ] && [ ! -e "$WORK/loop-a" ]; then
  ok "C20 软链成环 → 拒写（退出码 4，区别于临时目录的 3）"
else
  bad "C20 软链成环 → 拒写（退出码 4，区别于临时目录的 3）" "rc=$LAST_RC 首行: $(printf '%s' "$LAST_OUT" | head -1)"
fi

# C19 大小写不敏感文件系统上的 /TMP：真实路径是 /private/tmp
if [ -d /TMP ] && [ "$(cd /TMP && pwd -P)" = "$(cd /tmp && pwd -P)" ]; then
  CASE_CWD="$WORK"; CASE_TMPDIR="__UNSET__"
  run_ledger "/TMP/tpw-$RUNID/c19/new.tsv" P3 c19 "大小写" "大小写不敏感文件系统" "测试" "应拒绝"
  check_rejected "C19 /TMP（大小写不敏感文件系统）→ 拒写" "/tmp/tpw-$RUNID/c19/new.tsv"
else
  skip "C19 /TMP（大小写不敏感文件系统）→ 拒写" "本机文件系统区分大小写或 /TMP 不可达"
fi

# C24 祖先目录不可穿过（无 +x）→ 解析不到真实路径 → 拒写（退出码 4）
# 这条盖的是 docs/ledger.md「路径无法解析时（软链成环、无权限进入祖先目录）不猜」
# 里的后半句——以前只有成环那条有夹具。
mkdir -p "$WORK/noperm24/inner"
chmod 000 "$WORK/noperm24"
CASE_CWD="$WORK"; CASE_TMPDIR="__UNSET__"
run_ledger "$WORK/noperm24/inner/x.tsv" P3 c24 "无权限祖先" "解析不到真实路径" "测试" "应拒写"
chmod 755 "$WORK/noperm24"
if [ "$LAST_RC" -eq 4 ] && [ ! -e "$WORK/noperm24/inner/x.tsv" ]; then
  ok "C24 祖先目录无权限穿过 → 拒写（退出码 4）"
else
  bad "C24 祖先目录无权限穿过 → 拒写（退出码 4）" "rc=$LAST_RC 首行: $(printf '%s' "$LAST_OUT" | head -1)"
fi

# ── 绿方：不许误报 ────────────────────────────────────────────

# C11 TMPDIR 指到别处，不影响其他路径
CASE_CWD="$WORK"; CASE_TMPDIR="$WORK/custom-tmp"
run_ledger "$WORK/outside/c11.tsv" P3 c11 "TMPDIR 旁路" "不在 TMPDIR 之下" "测试" "应写入"
if [ "$LAST_RC" -eq 0 ]; then check_ledger_ok "C11 TMPDIR 之外 → 正常写入" "$WORK/outside/c11.tsv" 1
else bad "C11 TMPDIR 之外 → 正常写入" "rc=$LAST_RC 首行: $(printf '%s' "$LAST_OUT" | head -1)"; fi

# C14 目标路径本身是指向稳定位置的软链 → 正常写入
ln -s "$WORK/c14-real.tsv" "$WORK/c14-leaf.tsv"
CASE_CWD="$WORK"; CASE_TMPDIR="__UNSET__"
run_ledger "$WORK/c14-leaf.tsv" P3 c14 "末级软链" "指向稳定位置" "测试" "应写入"
if [ "$LAST_RC" -eq 0 ]; then check_ledger_ok "C14 末级软链指向稳定位置 → 正常写入" "$WORK/c14-real.tsv" 1
else bad "C14 末级软链指向稳定位置 → 正常写入" "rc=$LAST_RC 首行: $(printf '%s' "$LAST_OUT" | head -1)"; fi

# C15 正常绝对路径
CASE_CWD="$WORK"; CASE_TMPDIR="__UNSET__"
run_ledger "$WORK/normal/abs.tsv" P3 c15 "正常绝对路径" "不在临时目录" "测试" "应写入"
check_ledger_ok "C15 正常绝对路径 → 写入成功" "$WORK/normal/abs.tsv" 1

# C16 正常相对路径
CASE_CWD="$WORK"; CASE_TMPDIR="__UNSET__"
run_ledger "normal/rel.tsv" P3 c16 "正常相对路径" "不在临时目录" "测试" "应写入"
check_ledger_ok "C16 正常相对路径 → 写入成功" "$WORK/normal/rel.tsv" 1

# C17 目录名叫 tmp，但不在任何临时目录下 → 这是合法变体，必须允许
CASE_CWD="$WORK"; CASE_TMPDIR="__UNSET__"
run_ledger "$WORK/proj/tmp/ledger.tsv" P3 c17 "名叫 tmp 的目录" "不是临时目录" "测试" "应写入"
check_ledger_ok "C17 目录名叫 tmp 但位置稳定 → 正常写入（修掉旧的词面误报）" "$WORK/proj/tmp/ledger.tsv" 1

# C18 多级软链指向稳定位置 → 正常写入
mkdir -p "$WORK/stable-real"
ln -s "$WORK/stable-real" "$WORK/c18a"
ln -s "$WORK/c18a" "$WORK/c18b"
CASE_CWD="$WORK"; CASE_TMPDIR="__UNSET__"
run_ledger "$WORK/c18b/x.tsv" P3 c18 "多级软链" "指向稳定位置" "测试" "应写入"
if [ "$LAST_RC" -eq 0 ]; then check_ledger_ok "C18 多级软链指向稳定位置 → 正常写入" "$WORK/stable-real/x.tsv" 1
else bad "C18 多级软链指向稳定位置 → 正常写入" "rc=$LAST_RC 首行: $(printf '%s' "$LAST_OUT" | head -1)"; fi

# C21 末级软链指向稳定位置、目标文件尚不存在 → 正常写入（不把「指向不存在」一律当危险）
mkdir -p "$WORK/stable-never"
ln -s "$WORK/stable-never/x.tsv" "$WORK/c21-leaf.tsv"
CASE_CWD="$WORK"; CASE_TMPDIR="__UNSET__"
run_ledger "$WORK/c21-leaf.tsv" P3 c21 "末级软链" "指向稳定位置的不存在文件" "测试" "应写入"
if [ "$LAST_RC" -eq 0 ]; then check_ledger_ok "C21 末级软链指向稳定位置（文件尚不存在）→ 正常写入" "$WORK/stable-never/x.tsv" 1
else bad "C21 末级软链指向稳定位置（文件尚不存在）→ 正常写入" "rc=$LAST_RC 首行: $(printf '%s' "$LAST_OUT" | head -1)"; fi

# C23 末级悬空软链指向稳定位置、但目标的父目录不存在 → 闸不拦（不是临时目录），
# 失败来自打开本身（ENOENT）。旧实现同样如此：mkdir 只建「给定路径」的父目录。
ln -s "$WORK/never-parent/x.tsv" "$WORK/c23-leaf.tsv"
CASE_CWD="$WORK"; CASE_TMPDIR="__UNSET__"
run_ledger "$WORK/c23-leaf.tsv" P3 c23 "悬空软链+缺父目录" "落点稳定，闸不应判临时目录" "测试" "不是闸拒写"
if [ "$LAST_RC" -ne 0 ] && [ "$LAST_RC" -ne 3 ] && [ ! -e "$WORK/never-parent/x.tsv" ]; then
  ok "C23 悬空软链到稳定位置但目标的父目录不存在 → 闸放行，打开失败（rc=${LAST_RC}，非 3）"
else
  bad "C23 悬空软链到稳定位置但目标的父目录不存在 → 闸放行，打开失败（rc 非 0 非 3）" \
      "rc=$LAST_RC 首行: $(printf '%s' "$LAST_OUT" | head -1)"
fi

# C22 上级目录不存在、路径里带 .. 回到稳定位置 → 正常写入（mkdir -p 会补齐）
CASE_CWD="$WORK"; CASE_TMPDIR="__UNSET__"
run_ledger "$WORK/ghost/../stable-dir/x.tsv" P3 c22 "不存在 + .." "落点稳定" "测试" "应写入"
if [ "$LAST_RC" -eq 0 ]; then check_ledger_ok "C22 不存在组件 + .. 回到稳定位置 → 正常写入" "$WORK/stable-dir/x.tsv" 1
else bad "C22 不存在组件 + .. 回到稳定位置 → 正常写入" "rc=$LAST_RC 首行: $(printf '%s' "$LAST_OUT" | head -1)"; fi

# ── 汇总 ──────────────────────────────────────────────────────

echo
printf '合计: %d 通过 / %d 失败 / %d 跳过\n' "$PASS" "$FAIL" "$SKIP"
if [ "$FAIL" -gt 0 ]; then
  echo "判定: FAIL"
  exit 1
fi
if [ "$SKIP" -gt 0 ]; then
  echo "判定: PASS（有跳过；跳过项未验证）"
else
  echo "判定: PASS"
fi
