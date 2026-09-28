#!/usr/bin/env bash
# C1 情景 · 比例错实现对照（真跑 pytest，原样输出）
set -uo pipefail
cd "$(dirname "$0")"
export PYTHONDONTWRITEBYTECODE=1
rm -rf .pytest_cache __pycache__ impl_fixed/__pycache__ impl_ratio/__pycache__

run() {
  local impl="$1"; shift
  echo "----- PYTHONPATH=impl_${impl} pytest -q $* -----"
  PYTHONPATH="impl_${impl}" python3 -m pytest -q -p no:cacheprovider "$@" 2>&1
  echo "[pytest 退出码] $?"
}

echo "### 1) 旧 7 条 vs 比例错实现（旧测试全绿，必须被读成\"不能区分\"，不得据此晋升）"
run ratio test_pricing_old.py
echo
echo "### 2) 新判据（旧 7 条 + 非边界 witness）vs 比例错实现（应红）"
run ratio test_pricing_new.py
echo
echo "### 3) 新判据 vs 定额实现（应全绿）"
run fixed test_pricing_new.py
echo
echo "### 4) 上游判据规则是否已在角色文件里（开写窗前要求非边界正/反对照）"
ROOT=/Users/yuantian/Developer/tim-professional-workflow
grep -n "先从 Owner 的结果句提出至少一个合理但错误的实现" "$ROOT/roles/planner.md"
grep -n "make check\` 只说明运行入口" "$ROOT/roles/planner.md"
grep -n "一组可判否的正/反对照" "$ROOT/roles/driver.md"
echo
 echo "### 5) Reviewer 的独立挑战仍在（上游判据不是终审）"
grep -n "### 4.5 反实现挑战" "$ROOT/roles/reviewer.md"
grep -n "什么样明显错误的实现，仍能通过当前这套判据" "$ROOT/roles/reviewer.md"
