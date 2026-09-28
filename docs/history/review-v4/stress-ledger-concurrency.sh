#!/usr/bin/env bash
# stress-ledger-concurrency.sh · A9 台账并发压测夹具
#
# 用法:
#   bash .pi/review-v4/stress-ledger-concurrency.sh [轮数] [并发数]
# 默认: 10 轮 × 100 并发
# 被测对象: $LEDGER_SH（默认 <仓库>/scripts/ledger.sh）
#
# 每轮一个全新台账文件，N 个进程同时首次追加，互不相同的 decision。
# 判据（全部满足才算这一轮 OK）:
#   - 所有进程退出码 0
#   - 数据行恰 N 行（0 丢行）
#   - 表头恰 1 行（0 重复表头）
#   - 非 8 栏行 0（0 列错乱）
#   - decision 全部唯一（0 重复）
#   - 出现 3 种 actor（归因可区分）
#
# 台账落在仓库 .pi/ 下（稳定位置）；新闸会拒写临时目录，所以不能放 /tmp。

set -uo pipefail

ROUNDS="${1:-10}"
N="${2:-100}"

SELF_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO="$(cd "$SELF_DIR/../.." && pwd)"
LEDGER_SH="${LEDGER_SH:-$REPO/scripts/ledger.sh}"
[ -f "$LEDGER_SH" ] || { echo "被测脚本不存在: $LEDGER_SH" >&2; exit 2; }
LEDGER_SH="$(cd "$(dirname "$LEDGER_SH")" && pwd -P)/$(basename "$LEDGER_SH")"

RUNID="$(date -u +%Y%m%dT%H%M%S)-$$"
WORK="$SELF_DIR/stress-$RUNID"
mkdir -p "$WORK"
trap 'rm -rf "$WORK"' EXIT

echo "被测对象: $LEDGER_SH"
echo "夹具:     $ROUNDS 轮 × $N 并发（每轮全新台账，首次追加）"
echo

overall_fail=0
for round in $(seq 1 "$ROUNDS"); do
  f="$WORK/round-$round/ledger.tsv"
  mkdir -p "$(dirname "$f")"

  pids=""
  for i in $(seq 1 "$N"); do
    TPW_ACTOR="actor-$((i % 3))" TPW_RUN="round$round-i$i" \
      bash "$LEDGER_SH" "$f" P3 "s-$round-$i" "d-$round-$i" "w" "e" "r" \
      >/dev/null 2>&1 &
    pids="$pids $!"
  done

  failed_proc=0
  for pid in $pids; do
    wait "$pid" || failed_proc=$((failed_proc + 1))
  done

  rows="$(awk -F'\t' 'NR > 1 {c++} END {print c+0}' "$f")"
  headers="$(awk -F'\t' '$1 == "actor" && NF == 8 {c++} END {print c+0}' "$f")"
  badcols="$(awk -F'\t' 'NF != 8 {c++} END {print c+0}' "$f")"
  uniq="$(awk -F'\t' 'NR > 1 {print $5}' "$f" | sort -u | wc -l | tr -d ' ')"
  actors="$(awk -F'\t' 'NR > 1 {print $1}' "$f" | sort -u | wc -l | tr -d ' ')"

  if [ "$failed_proc" = "0" ] && [ "$rows" = "$N" ] && [ "$headers" = "1" ] && \
     [ "$badcols" = "0" ] && [ "$uniq" = "$N" ] && [ "$actors" = "3" ]; then
    printf 'round %2d: OK    rows=%-4s headers=%-2s badcols=%-2s unique=%-4s actors=%-2s failed_proc=%s\n' \
      "$round" "$rows" "$headers" "$badcols" "$uniq" "$actors" "$failed_proc"
  else
    printf 'round %2d: FAIL  rows=%-4s headers=%-2s badcols=%-2s unique=%-4s actors=%-2s failed_proc=%s\n' \
      "$round" "$rows" "$headers" "$badcols" "$uniq" "$actors" "$failed_proc"
    overall_fail=1
  fi
done

echo
if [ "$overall_fail" = "0" ]; then
  echo "STRESS PASS: $ROUNDS 轮 × $N 并发，0 丢行 / 0 重复表头 / 0 列错乱 / 0 重复 decision"
  exit 0
fi
echo "STRESS FAIL"
exit 1
