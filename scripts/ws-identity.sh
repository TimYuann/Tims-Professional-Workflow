#!/usr/bin/env bash
# ws-identity.sh · 无版本历史时的对象身份（ws:v1）
#
# 规范见仓库根 identity.md（维护者规范）。本脚本是它的参考实现，同时也是
# scripts/identity-selftest.sh 的被测对象。
#
# 用法：
#   ws-identity.sh manifest <路径清单文件>   # 生成规范化清单 → stdout
#   ws-identity.sh digest   <清单文件>       # 输出 ws:v1:<sha256>
#   ws-identity.sh compare  <清单A> <清单B>  # EQUAL / DIFFERENT；退出码 0 / 1
#   ws-identity.sh verify   <交付清单> <范围声明>   # 用当前源文件逐条复核交付身份；异常一律报错
#
# verify 与 compare 的区别（identity.md §5）：
#   compare 只比两份清单文件本身；源文件改了、旧清单与旧清单比仍然 EQUAL。
#   **身份复核必须走 verify**：它按范围声明重新枚举当前源文件逐条比对。
# verify 报的五类异常：MISSING（清单里有、磁盘上没有）/ CHANGED（内容变了）/
#   SCOPE_NOT_IN_MANIFEST（范围里有、清单没记）/ PSEUDO_DELETE（标了删除、文件其实还在）/
#   BAD_PATH（越出仓根或重复路径）。任一异常 → 非零退出。
#
# 路径清单文件每行一条：相对仓根、一律 / 分隔、无前导 ./。
#   现存文件：   <相对路径>
#   被删文件：   -<相对路径>         （取删除前字节的 sha256，须由调用方提供 -<路径>=<sha256>）
#
# 规范化规则（identity.md §2）：
#   每行 = 相对路径 + NUL + 文件字节 sha256
#   按路径字节序升序；排除 .git/**、缓存、构建产物、__pycache__、.pytest_cache
#   digest = sha256(清单字节) 的小写十六进制
set -euo pipefail

LC_ALL=C
export LC_ALL

usage() {
	printf 'usage: ws-identity.sh manifest <listfile> | digest <manifest> | compare <A> <B>\n' >&2
	exit 64
}

is_excluded() {
	case "$1" in
		.git/*|*/.git/*|*/__pycache__/*|__pycache__/*|*/.pytest_cache/*|.pytest_cache/*) return 0 ;;
		*.pyc|*/build/*|*/dist/*|*/.cache/*|*.log) return 0 ;;
		*) return 1 ;;
	esac
}

norm_path() {
	# 去掉前导 ./，统一分隔符，压掉重复斜杠
	local p="$1"
	p="${p#./}"
	p="$(printf '%s' "$p" | tr '\\' '/')"
	while [[ "$p" == *//* ]]; do p="${p//\/\//\/}"; done
	printf '%s' "$p"
}

sha256_file() {
	if command -v shasum >/dev/null 2>&1; then
		shasum -a 256 -- "$1" | awk '{print $1}'
	elif command -v sha256sum >/dev/null 2>&1; then
		sha256sum -- "$1" | awk '{print $1}'
	else
		printf 'no sha256 tool available\n' >&2
		exit 69
	fi
}

sha256_stdin() {
	if command -v shasum >/dev/null 2>&1; then
		shasum -a 256 | awk '{print $1}'
	else
		sha256sum | awk '{print $1}'
	fi
}

cmd_manifest() {
	local list="$1"
	[[ -f "$list" ]] || { printf 'list file not found: %s\n' "$list" >&2; exit 66; }
	local out
	out="$(mktemp)"

	while IFS= read -r raw || [[ -n "$raw" ]]; do
		[[ -z "$raw" ]] && continue
		local deleted=0
		local line="$raw"
		if [[ "$line" == -* ]]; then deleted=1; line="${line#-}"; fi
		local path; path="$(norm_path "$line")"
		if is_excluded "$path"; then continue; fi
		local digest=""
		if [[ "$deleted" == "1" ]]; then
			# 形式：-path=sha256（调用方必须提供删除前的内容摘要，不能只给路径）
			if [[ "$path" == *=* ]]; then
				digest="${path##*=}"
				path="${path%%=*}"
			else
				printf 'deleted entry needs -<path>=<sha256>: %s\n' "$raw" >&2
				rm -f "$out"
				exit 65
			fi
			printf '%s\t-%s\n' "$path" "$digest" >> "$out"
		else
			if [[ ! -f "$path" ]]; then
				printf 'file not found: %s\n' "$path" >&2
				rm -f "$out"
				exit 66
			fi
			digest="$(sha256_file "$path")"
			printf '%s\t%s\n' "$path" "$digest" >> "$out"
		fi
	done < "$list"

	# 按路径字节序升序（LC_ALL=C 下 sort 即字节序），再把分隔符换成 NUL。
	# 用 bash 的 printf 生成 NUL（macOS 自带 awk 的 "\0" 不是 NUL，会把分隔符吃掉）：
	sort -t$'\t' -k1,1 "$out" | while IFS=$'\t' read -r p d; do
		[[ -n "${p:-}" ]] || continue
		printf '%s\0%s\n' "$p" "$d"
	done
	rm -f "$out"
}

cmd_digest() {
	local manifest="$1"
	[[ -f "$manifest" ]] || { printf 'manifest not found: %s\n' "$manifest" >&2; exit 66; }
	printf 'ws:v1:%s\n' "$(cmd_digest_raw "$manifest")"
}

cmd_digest_raw() {
	sha256_stdin < "$1"
}

cmd_compare() {
	local a="$1" b="$2"
	[[ -f "$a" && -f "$b" ]] || { printf 'manifest not found\n' >&2; exit 66; }
	local da db
	da="$(cmd_digest_raw "$a")"
	db="$(cmd_digest_raw "$b")"
	if [[ "$da" == "$db" ]]; then
		printf 'EQUAL ws:v1:%s\n' "$da"
		return 0
	fi
	printf 'DIFFERENT %s vs %s\n' "ws:v1:$da" "ws:v1:$db"
	return 1
}

cmd_verify() {
	local manifest="$1" scope="$2"
	[[ -f "$manifest" ]] || { printf 'manifest not found: %s\n' "$manifest" >&2; exit 66; }
	[[ -f "$scope" ]] || { printf 'scope declaration not found: %s\n' "$scope" >&2; exit 66; }

	local tmp; tmp="$(mktemp)"
	tr '\0' '\t' < "$manifest" > "$tmp"

	local rc=0
	local p d

	# 1) 越根（绝对路径、或任何 ../ 段）
	while IFS=$'\t' read -r p d; do
		[[ -n "$p" ]] || continue
		case "$p" in
			/*|../*|*/../*|*/..) printf 'BAD_PATH %s\n' "$p"; rc=1 ;;
		esac
	done < "$tmp"

	# 2) 重复路径（同一路径出现两次会让同一文件集产生两个身份）
	local dups
	dups="$(cut -f1 "$tmp" | LC_ALL=C sort | LC_ALL=C uniq -d)"
	if [[ -n "$dups" ]]; then
		while IFS= read -r x; do printf 'BAD_PATH duplicate %s\n' "$x"; done <<< "$dups"
		rc=1
	fi

	# 3) 逐条比对当前源文件
	while IFS=$'\t' read -r p d; do
		[[ -n "$p" ]] || continue
		if [[ "$d" == -* ]]; then
			if [[ -e "$p" || -L "$p" ]]; then
				printf 'PSEUDO_DELETE %s（标了删除，文件其实还在）\n' "$p"; rc=1
			fi
			continue
		fi
		if [[ ! -f "$p" ]]; then
			printf 'MISSING %s\n' "$p"; rc=1
			continue
		fi
		local cur; cur="$(sha256_file "$p")"
		if [[ "$cur" != "$d" ]]; then
			printf 'CHANGED %s\n' "$p"; rc=1
		fi
	done < "$tmp"

	# 4) 范围声明里的每条都必须出现在交付清单里
	while IFS= read -r raw || [[ -n "$raw" ]]; do
		[[ -z "$raw" ]] && continue
		local want; want="$(norm_path "${raw#-}")"
		if ! awk -F'\t' -v want="$want" '$1==want{found=1} END{exit !found}' "$tmp"; then
			printf 'SCOPE_NOT_IN_MANIFEST %s\n' "$want"; rc=1
		fi
	done < "$scope"

	rm -f "$tmp"
	if [[ "$rc" -eq 0 ]]; then
		printf 'VERIFIED %s\n' "$(cmd_digest "$manifest")"
	fi
	return "$rc"
}

case "${1:-}" in
	manifest) shift; [[ $# -eq 1 ]] || usage; cmd_manifest "$1" ;;
	digest) shift; [[ $# -eq 1 ]] || usage; cmd_digest "$1" ;;
	compare) shift; [[ $# -eq 2 ]] || usage; cmd_compare "$1" "$2" ;;
	verify) shift; [[ $# -eq 2 ]] || usage; cmd_verify "$1" "$2" ;;
	*) usage ;;
esac
