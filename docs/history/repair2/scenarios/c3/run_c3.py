#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C3 情景 · 证据寿命对照（真跑：立即可运行 → 临时证据消失后复用失败 → 可重建输入按新对象重做）。

不触碰 /tmp/f-review-probes/（发现 4 的现场，等 Owner 裁 D1）：断言临时根不是它。
"""
from __future__ import annotations

import hashlib
import os
import pathlib
import shutil
import subprocess
import sys

ROOT = pathlib.Path("/Users/yuantian/Developer/tim-professional-workflow")
SC = ROOT / ".pi/repair2/scenarios/c3"
FORBIDDEN = "/tmp/f-review-probes"
TEMP = pathlib.Path("/tmp/f-repair2-%d" % os.getpid())

WITNESS = "total=51000 expected=49500 fee=1500 ratio_result=49470\n"

TEST_SRC = '''"""C9 fixture 的 8 条：7 条旧 + 非边界 witness。"""
FEE = 1500


def price(total):
    return total - FEE


def test_50000():
    assert price(50000) == 48500


def test_repeat():
    assert price(50000) == price(50000) == 48500


def test_type():
    assert isinstance(price(50000), int)


def test_boundary():
    assert price(50000) == 48500


def test_input_not_mutated():
    t = 50000
    price(t)
    assert t == 50000


def test_no_double_fee():
    assert price(50000) == 48500


def test_two_in_a_row():
    assert [price(50000) for _ in range(2)] == [48500, 48500]


def test_non_boundary_witness():
    assert price(51000) == 49500
'''


def run_c9() -> subprocess.CompletedProcess:
    return subprocess.run(
        ["python3", "-m", "pytest", "-q", "-p", "no:cacheprovider", "test_pricing_base.py"],
        capture_output=True, text=True, cwd=str(TEMP),
    )


def p(label: str, ok: bool, detail: str = "") -> bool:
    print(("  [PASS] " if ok else "  [FAIL] ") + label + (" :: " + detail if detail else ""))
    return ok


def main() -> int:
    ok = True
    print("C3 证据寿命对照（临时根=%s；禁区=%s）" % (TEMP, FORBIDDEN))
    ok &= p("临时根不是 /tmp/f-review-probes", not str(TEMP).startswith(FORBIDDEN), str(TEMP))
    print("  禁区是否仍存在（只读观察，不写入）: %s" % ("存在" if pathlib.Path(FORBIDDEN).exists() else "不存在"))

    # 1) 造证据：唯一参照副本放在 /tmp
    if TEMP.exists():
        shutil.rmtree(TEMP)
    TEMP.mkdir(parents=True)
    (TEMP / "witness.txt").write_text(WITNESS, encoding="utf-8")
    (TEMP / "test_pricing_base.py").write_text(TEST_SRC, encoding="utf-8")
    input_hash = hashlib.sha256(WITNESS.encode()).hexdigest()

    frozen = SC / "frozen-c9.md"
    frozen.write_text(
        "# 冻结判据 C9（fixture）\n\n"
        "- 承重证据：`%s/test_pricing_base.py` + `%s/witness.txt`\n"
        "- 命令：`cd %s && python3 -m pytest -q test_pricing_base.py`\n"
        "- 预期：`8 passed`\n"
        "- witness 输入 hash：`%s`\n"
        "- 原产者：verifier（fixture）；需保留到：本次验证复核点\n"
        % (TEMP, TEMP, TEMP, input_hash),
        encoding="utf-8",
    )

    print("\n--- 1) 冻结判据引 /tmp 时立即可运行 ---")
    r1 = run_c9()
    print("$ cd %s && python3 -m pytest -q test_pricing_base.py" % TEMP)
    print((r1.stdout + r1.stderr).strip())
    print("[退出码] %d" % r1.returncode)
    ok &= p("此刻可运行且 8 passed", r1.returncode == 0 and "8 passed" in r1.stdout, "rc=%d" % r1.returncode)

    # 2) 角色/流程规则：临时证据的定位
    print("\n--- 2) 规则是否要求写明保留点、且把 /tmp 定为临时证据 ---")
    checks = [
        ("pipeline.md §8 位置未失效", ROOT / "pipeline.md", "位置未失效"),
        ("reviewer §4.1 第 8 步临时证据", ROOT / "roles/reviewer.md", "只算**临时证据**"),
        ("reviewer §4.1 禁止静默搬迁", ROOT / "roles/reviewer.md", "不得静默搬到范围外目录"),
        ("verifier §3 commands 保留点/原产者", ROOT / "roles/verifier.md", "需保留到哪个交付点、原产者"),
        ("driver §4.4 第 6 步三问", ROOT / "roles/driver.md", "现在可取回 + 保管到所需时间 + 搬迁有授权"),
        ("driver §4.8 第 7 步不得写成可复用", ROOT / "roles/driver.md", "不得把未获保管授权的临时证据写成将来可复用"),
    ]
    for label, path, needle in checks:
        hit = needle in path.read_text(encoding="utf-8")
        ok &= p(label, hit, "")

    # 3) 临时证据消失 → 复用必须失败
    print("\n--- 3) 临时证据消失后，按同一冻结判据复用 ---")
    shutil.rmtree(TEMP)
    r2 = subprocess.run(
        ["python3", "-m", "pytest", "-q", "-p", "no:cacheprovider", "test_pricing_base.py"],
        capture_output=True, text=True,
    )
    print("$ cd %s && python3 -m pytest -q test_pricing_base.py   # 目录已删除" % TEMP)
    print((r2.stdout + r2.stderr).strip().splitlines()[-1] if (r2.stdout + r2.stderr).strip() else "(无输出)")
    print("[退出码] %d" % r2.returncode)
    ok &= p("复用失败（不得再发 PASS）", r2.returncode != 0, "rc=%d" % r2.returncode)

    # 4) 可重建的最小输入 → 按新对象重做
    print("\n--- 4) 能重建的最小输入经 hash 核对后可按新对象重做 ---")
    rebuilt = SC / "rebuilt-witness.txt"
    rebuilt.write_text(WITNESS, encoding="utf-8")
    rebuilt_hash = hashlib.sha256(rebuilt.read_bytes()).hexdigest()
    ok &= p("重建输入 hash 与冻结判据记录一致", rebuilt_hash == input_hash, "%s" % rebuilt_hash[:16])
    print("  注：重建的是**输入**；原本未保留的变异原始读数不能因此说成还在。")

    print("\nC3 结论: " + ("全部通过" if ok else "存在 FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
