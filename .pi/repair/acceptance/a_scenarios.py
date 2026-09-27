#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A 批验收情景 · 提取角色文件里真实存在的规则行，按情景断言它会要求什么。

这不是"再写一个校验器"，是验收夹具：所有被断言的句子都从 roles/*.md 现场读出，
脚本里不硬编码规则文本。缺任何一条 → 非零退出。
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def text(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def lines(rel: str, pattern: str) -> list[str]:
    pat = re.compile(pattern)
    return [ln.strip() for ln in text(rel).splitlines() if pat.search(ln)]


def check(name: str, cond: bool, detail: str) -> bool:
    print(("  [PASS] " if cond else "  [FAIL] ") + name + " :: " + detail)
    return cond


def show(title: str, rows: list[str]) -> None:
    print("  - " + title)
    for r in rows:
        print("      命中规则: " + r)


def a1_missing_slice_plan() -> bool:
    print("[情景 A-1] 任务声称有 slice-plan 却没交 → 实现者必须停止开工、零写入并点名缺件")
    impl = "roles/implementer.md"
    t = text(impl)
    ok = True
    stop_rows = lines(impl, r"停止开工|零写入")
    name_rows = lines(impl, r"点名缺什么、谁应补")
    route_rows = lines(impl, r"唯一合法动作是停止")
    contradiction = "要不到就按最小范围处理" in t
    ok &= check("存在「停止开工/零写入」规则", bool(stop_rows), "%d 行" % len(stop_rows))
    ok &= check("存在「点名缺什么、谁应补」规则", bool(name_rows), "%d 行" % len(name_rows))
    ok &= check("存在「唯一合法动作是停止」规则", bool(route_rows), "%d 行" % len(route_rows))
    ok &= check("已无「要不到就按最小范围处理」矛盾处置", not contradiction,
                "残留" if contradiction else "0 残留")
    show("slice-plan 与收件四步", (stop_rows + name_rows + route_rows)[:6])
    return ok


def a2_env_not_ready() -> bool:
    print("[情景 A-2] 任务写「服务已就绪」但现场找不到正确实例 → 验证者必须给 UNVERIFIED + 缺什么 + 交 Driver，不得借旧材料发 PASS")
    vf = "roles/verifier.md"
    t = text(vf)
    ok = True
    need_target = lines(vf, r"本轮任务必须说明运行目标及期望环境")
    not_ready = lines(vf, r"未声明就绪")
    ask_driver = lines(vf, r"缺目标或授权向 `roles/driver.md` 要")
    unverified = lines(vf, r"记 `UNVERIFIED`")
    no_verdict = lines(vf, r"不给产品代码判 `FAIL`/`PASS`")
    no_rewrite = lines(vf, r"不要改写成通过")
    no_borrow = lines(vf, r"不把\"发件人说有\"当作\"现场确有\"")
    ok &= check("任务须声明运行目标与期望环境", bool(need_target), "%d 行" % len(need_target))
    ok &= check("「未声明就绪」≠「就绪」", bool(not_ready), "%d 行" % len(not_ready))
    ok &= check("缺目标/授权向 Driver 要", bool(ask_driver), "%d 行" % len(ask_driver))
    ok &= check("建不起来记 UNVERIFIED", bool(unverified), "%d 行" % len(unverified))
    ok &= check("不给产品代码判 FAIL/PASS", bool(no_verdict), "%d 行" % len(no_verdict))
    ok &= check("环境不满足不得改写成通过（§4.2 第 5 步）", bool(no_rewrite), "%d 行" % len(no_rewrite))
    ok &= check("不把发件人说法当现场事实（收件四步）", bool(no_borrow), "%d 行" % len(no_borrow))
    show("验证者收件与三态", (need_target + not_ready + ask_driver + unverified + no_verdict + no_rewrite)[:8])
    return ok


def main() -> int:
    print("A 批验收（规则提取自角色文件现场文本；ROOT=%s）" % ROOT)
    ok = a1_missing_slice_plan()
    print()
    ok &= a2_env_not_ready()
    print()
    print("A 批验收结论: " + ("全部通过" if ok else "存在 FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
