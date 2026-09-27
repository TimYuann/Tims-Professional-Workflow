#!/usr/bin/env bash
# log-decision.sh · 往 append-only 决策台账（TSV）追加一行
#
# 用法：scripts/log-decision.sh <台账文件> <阶段> <决定> <理由> <证据> <结果>
#
# 例：
#   scripts/log-decision.sh decisions.tsv 验证 "在合并后候选上跑了旅程验收" \
#     "各项 PASS 的集合不等于交付" "commit 4f2a1c9, 输出见 /tmp/run.log" "全绿"
#
# 约定
#   - 只追加。判断错了写一条新行覆盖它，永不编辑或删除历史行。
#   - 证据列填指针（提交、文件:行、产物路径），不要写段落。
#   - 单元格内的制表符/换行会被替换为空格；以 = + - @ 开头的单元格会加前导单引号，
#     以免台账被电子表格打开时把内容当成公式执行。
set -euo pipefail

if [ "$#" -ne 6 ]; then
	printf 'usage: log-decision.sh <logfile> <phase> <decision> <why> <evidence> <result>\n' >&2
	exit 1
fi

logfile="$1"
shift

logdir="$(dirname "$logfile")"
if [ -n "$logdir" ] && [ "$logdir" != "." ] && [ ! -d "$logdir" ]; then
	mkdir -p "$logdir"
fi

# 用 >> 而不是 >：网络盘上 -s 判断可能失败，代价是多一行表头，而不是丢掉已有行。
if [ ! -s "$logfile" ]; then
	printf 'ts\tphase\tdecision\twhy\tevidence\tresult\n' >> "$logfile"
fi

clean() {
	local v
	v=$(printf '%s' "$1" | tr '\t\n\r' '   ')
	case "$v" in
		=*|+*|-*|@*) printf "'%s" "$v" ;;
		*) printf '%s' "$v" ;;
	esac
}

ts="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
printf '%s\t%s\t%s\t%s\t%s\t%s\n' \
	"$ts" "$(clean "$1")" "$(clean "$2")" "$(clean "$3")" "$(clean "$4")" "$(clean "$5")" \
	>> "$logfile"
