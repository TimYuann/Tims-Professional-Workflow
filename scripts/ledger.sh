#!/usr/bin/env bash
# ledger.sh · 决策台账（A9）追加工具
#
# 纪律：只追加。没有删除、没有编辑。写错了就再追加一行说明上一行为什么错。
# 就地编辑会让人追溯性地改写历史；只追加让内容层保持不变，只有追加层在增长。
#
# 用法:
#   scripts/ledger.sh <台账路径> "决定了什么" "为什么" "凭什么" "结果如何"
#
# 它不做的事:
#   - 不判断一条决策该不该记
#   - 不检查 evidence 是否真实存在（只能靠写的人自觉，所以复核时必须抽查）
#   - 不做汇总、统计、格式化
#   - 不写入临时目录（需要留档的东西落在临时目录等于没写）

set -euo pipefail

if [ "$#" -lt 4 ] || [ "$#" -gt 5 ]; then
  echo "用法: $0 <台账路径> \"决定了什么\" \"为什么\" \"凭什么\" [\"结果如何\"]" >&2
  echo "见 docs/ledger.md" >&2
  exit 2
fi

ledger="$1"
decision="$2"
why="$3"
evidence="$4"
result="${5:-}"

if [ -z "$decision" ] || [ -z "$why" ] || [ -z "$evidence" ]; then
  echo "决定、为什么、凭什么 三栏都不能为空" >&2
  exit 2
fi

case "$ledger" in
  */tmp/*|/tmp/*|/var/tmp/*|/private/tmp/*)
    echo "拒绝写入临时目录：需要留档的东西落在临时目录等于没写" >&2
    exit 3
    ;;
esac

mkdir -p "$(dirname "$ledger")"

if [ ! -f "$ledger" ]; then
  printf 'ts\tdecision\twhy\tevidence\tresult\n' > "$ledger"
fi

# 字段里的制表符会破坏列对齐，换成空格
clean() { printf '%s' "$1" | tr '\t\n' '  '; }

printf '%s\t%s\t%s\t%s\t%s\n' \
  "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  "$(clean "$decision")" \
  "$(clean "$why")" \
  "$(clean "$evidence")" \
  "$(clean "$result")" >> "$ledger"

echo "已追加：$ledger"
