#!/usr/bin/env bash
# identity-selftest.sh · ws:v1 身份实现的正负夹具
#
# 这批夹具是**可失败的**：任何一个夹具的行为与 identity.md 规定不符，本脚本就以非零退出。
# 它们不检查"实现是否写着 ws:v1"，而是检查"实现是否会漏掉一类真实差异"。
#
# 用法：
#   identity-selftest.sh                     # 测 scripts/ws-identity.sh
#   identity-selftest.sh --tool <实现路径>    # 测指定实现（用来证明夹具本身会红）
#
# 夹具（每条对应一类真实缺陷）：
#   P1  规范化：同样内容，一次带 ./ 前缀 → digest 必须相等
#   P1b 规范化：同样内容，输入顺序不同   → digest 必须相等
#   N1  内容差异：**路径不变**、文件内容改一个字节 → digest 必须不等
#   N2  路径差异：**内容不变**、文件改名或搬目录   → digest 必须不等
#   N3  删除入单：删掉文件并留 `-` 行             → digest 必须不等
#   N4  排除规则：`.git/**`、`__pycache__/**` 的存在与状态不影响 digest
#
# 退出码：0 = 全部夹具行为符合规范；1 = 有夹具行为不符（即有缺陷漏检）。
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WS="$SCRIPT_DIR/ws-identity.sh"
if [[ "${1:-}" == "--tool" ]]; then
	WS="${2:?--tool needs a path}"
fi
[[ -f "$WS" ]] || { printf 'tool not found: %s\n' "$WS" >&2; exit 66; }

WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

pass=0
fail=0
report() { # <夹具> <期望> <实际> <说明>
	if [[ "$2" == "$3" ]]; then
		printf '[PASS] %-3s %s\n' "$1" "$4"
		pass=$((pass + 1))
	else
		printf '[FAIL] %-3s 期望 %s，实际 %s —— %s\n' "$1" "$2" "$3" "$4"
		fail=$((fail + 1))
	fi
}
cmp_pair() { # <清单A> <清单B> → EQUAL | DIFFERENT
	set +e
	"$WS" compare "$WORK/$1" "$WORK/$2" >/dev/null 2>&1
	local rc=$?
	set -e
	[[ $rc -eq 0 ]] && echo EQUAL || echo DIFFERENT
}
mk_manifest() { # <清单名> <输出名>
	"$WS" manifest "$WORK/$1" > "$WORK/$2"
}
mk_list() { # <输出文件> <路径...>
	local out="$1"; shift
	: > "$WORK/$out"
	local p
	for p in "$@"; do printf '%s\n' "$p" >> "$WORK/$out"; done
}

# ── 造工作区 ──────────────────────────────────────────────────────────────────
mkdir -p "$WORK/src" "$WORK/.git" "$WORK/__pycache__"
printf 'def authorized():\n    return True\n' > "$WORK/src/auth.py"
printf 'alpha\n' > "$WORK/src/a.txt"
printf 'beta\n' > "$WORK/src/b.txt"
printf 'git-internal-garbage\n' > "$WORK/.git/HEAD"
printf 'cached-bytecode\n' > "$WORK/__pycache__/auth.pyc"

LIST="list-normal"
mk_list "$LIST" "src/a.txt" "src/b.txt" "src/auth.py" ".git/HEAD" "__pycache__/auth.pyc"
mk_list "list-dotprefixed" "./src/b.txt" "src/auth.py" "src/a.txt" "__pycache__/auth.pyc" ".git/HEAD"
mk_list "list-shuffled" "src/auth.py" "src/a.txt" "__pycache__/auth.pyc" "src/b.txt" ".git/HEAD"
mk_list "list-excluded-as-deleted" "src/a.txt" "src/b.txt" "src/auth.py" \
	"-.git/HEAD=deadbeef" "-__pycache__/auth.pyc=deadbeef"

cd "$WORK"

# ── P1 / P1b 规范化 ───────────────────────────────────────────────────────────
mk_manifest "$LIST" m-normal
mk_manifest "list-dotprefixed" m-dotprefixed
mk_manifest "list-shuffled" m-shuffled
report P1 EQUAL "$(cmp_pair m-normal m-dotprefixed)" "带 ./ 前缀 vs 规范形态（不规范化 → 假 DIFFERENT）"
report P1b EQUAL "$(cmp_pair m-normal m-shuffled)" "乱序输入 vs 规范形态（不排序 → 假 DIFFERENT）"

# ── N1 内容差异（路径不变）────────────────────────────────────────────────────
printf 'def authorized():\n    return False\n' > "$WORK/src/auth.py"
mk_manifest "$LIST" m-content-changed
report N1 DIFFERENT "$(cmp_pair m-normal m-content-changed)" "路径不变、内容改一字节（只哈希路径 → 漏检）"
printf 'def authorized():\n    return True\n' > "$WORK/src/auth.py"

# ── N2 路径差异（内容不变）────────────────────────────────────────────────────
mv "$WORK/src/b.txt" "$WORK/src/b_renamed.txt"
mk_list "list-path-changed" "src/a.txt" "src/b_renamed.txt" "src/auth.py" ".git/HEAD" "__pycache__/auth.pyc"
mk_manifest "list-path-changed" m-path-changed
report N2 DIFFERENT "$(cmp_pair m-normal m-path-changed)" "内容不变、路径改名（只哈希内容 → 漏检）"
mv "$WORK/src/b_renamed.txt" "$WORK/src/b.txt"

# ── N3 删除入单 ───────────────────────────────────────────────────────────────
b_sha=$(shasum -a 256 < "$WORK/src/b.txt" | awk '{print $1}')
mk_list "list-deleted" "src/a.txt" "-src/b.txt=$b_sha" "src/auth.py" ".git/HEAD" "__pycache__/auth.pyc"
mk_manifest "list-deleted" m-deleted
report N3 DIFFERENT "$(cmp_pair m-normal m-deleted)" "删除文件并留 - 行（只看现存文件 → 漏检）"

# ── N5 清单漏掉写入范围内的一个文件 → 必须不等 ────────────────────────────────
mk_list "list-missing-one" "src/a.txt" "src/auth.py" ".git/HEAD" "__pycache__/auth.pyc"
mk_manifest "list-missing-one" m-missing-one
report N5 DIFFERENT "$(cmp_pair m-normal m-missing-one)" "漏写 → 与完整清单不等（只证明清单被改过；覆盖度由 identity.md §5 的范围声明负责）"

# ── N6 清单引用不存在的文件 → 必须报错（不得静默跳过）─────────────────────────
set +e
"$WS" manifest "$WORK/list-ghost" >/dev/null 2>&1
rc_ghost=$?
set -e
mk_list "list-ghost" "src/a.txt" "src/does-not-exist.txt"
set +e
"$WS" manifest "$WORK/list-ghost" >/dev/null 2>&1
rc_ghost=$?
set -e
report N6 NONZERO "$([[ $rc_ghost -ne 0 ]] && echo NONZERO || echo ZERO)" "清单里有不存在的文件（静默跳过 → 漏检）"

# ── V0–V5 verify 模式：五类异常必须报错，正常必须通过 ──────────────────────────
mk_list "scope" "src/a.txt" "src/b.txt" "src/auth.py"
"$WS" manifest "$LIST" > "$WORK/m-delivered" || true
# 交付清单只含写入范围里的三份文件（.git/__pycache__ 会被排除，不影响）
mk_list "list-delivered" "src/a.txt" "src/b.txt" "src/auth.py"
"$WS" manifest "$WORK/list-delivered" > "$WORK/m-delivered"

vrun() { # <夹具号> <预期 OK|ERR> <说明> <清单> <范围声明>
	local id="$1" expect="$2" desc="$3" man="$4" sc="$5"
	local out
	set +e
	out="$("$WS" verify "$man" "$sc" 2>&1)"
	local rc=$?
	set -e
	local got; got=$([[ $rc -eq 0 ]] && echo OK || echo ERR)
	local first; first="$(printf '%s\n' "$out" | head -n 1)"
	report "$id" "$expect" "$got" "$desc${first:+｜$first}"
}
vrun V0 OK "正常交付：范围与清单一致" "$WORK/m-delivered" "$WORK/scope"

# V1 缺文件：清单里有、磁盘上删掉
cp "$WORK/src/b.txt" "$WORK/src/b.keep"
rm "$WORK/src/b.txt"
vrun V1 ERR "缺文件（清单有、磁盘没有）" "$WORK/m-delivered" "$WORK/scope"
mv "$WORK/src/b.keep" "$WORK/src/b.txt"

# V2 范围里有、清单没记
mk_list "scope-extra" "src/a.txt" "src/b.txt" "src/auth.py" "src/c.txt"
printf 'gamma\n' > "$WORK/src/c.txt"
vrun V2 ERR "范围声明里有、清单没记" "$WORK/m-delivered" "$WORK/scope-extra"
rm -f "$WORK/src/c.txt"

# V3 越根
mk_list "list-escape" "src/a.txt" "../external.txt"
printf 'outside\n' > "$(dirname "$WORK")/external.txt"
set +e; "$WS" manifest "$WORK/list-escape" > "$WORK/m-escape" 2>/dev/null; rc_esc=$?; set -e
if [[ $rc_esc -eq 0 ]]; then
	vrun V3 ERR "越出仓根" "$WORK/m-escape" "$WORK/scope"
else
	report V3 ERR ERR "越根路径在生成清单阶段就被拒（退出码 $rc_esc）"
fi
rm -f "$(dirname "$WORK")/external.txt"

# V4 重复路径
{ "$WS" manifest "$WORK/list-delivered"; "$WS" manifest "$WORK/list-delivered"; } > "$WORK/m-dup"
vrun V4 ERR "同一路径重复出现" "$WORK/m-dup" "$WORK/scope"

# V5 伪删除：标了删除，文件其实还在
mk_list "list-fake-delete" "src/a.txt" "-src/b.txt=deadbeef" "src/auth.py"
"$WS" manifest "$WORK/list-fake-delete" > "$WORK/m-fake-delete"
vrun V5 ERR "伪删除（标了删除、文件还在）" "$WORK/m-fake-delete" "$WORK/scope"

# V6 内容改了、但用旧清单来复核 → 必须报错（这正是 compare 测不出来的那类）
"$WS" manifest "$WORK/list-delivered" > "$WORK/m-old"
printf 'def authorized():\n    return False\n' > "$WORK/src/auth.py"
vrun V6 ERR "源文件改了、拿旧清单复核（compare 测不出来）" "$WORK/m-old" "$WORK/scope"
printf 'def authorized():\n    return True\n' > "$WORK/src/auth.py"

# ── N4 排除规则 ───────────────────────────────────────────────────────────────
mk_manifest "list-excluded-as-deleted" m-excluded-as-deleted
report N4 EQUAL "$(cmp_pair m-normal m-excluded-as-deleted)" "排除目录的存在与状态不影响身份"

printf -- '----\n合计：%d 通过 / %d 失败（被测实现：%s）\n' "$pass" "$fail" "$WS"
[[ "$fail" -eq 0 ]] || exit 1
