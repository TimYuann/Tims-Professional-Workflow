#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""B1 回归确认（零产物修改）：Driver 代产完整 slice-plan 的交接仍然成立。

不修任何文件；只做规则提取与两个场景读数，并核对 closure.md / ws-identity.sh
与上一轮（repair 1）结束时的 sha256 逐字一致。
"""
from __future__ import annotations

import hashlib
import pathlib
import re
import sys

ROOT = pathlib.Path("/Users/yuantian/Developer/tim-professional-workflow")


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def lines(rel: str, pat: str) -> list[str]:
    rx = re.compile(pat)
    return [ln.strip() for ln in read(rel).splitlines() if rx.search(ln)]


FAILED = []


def p(label: str, ok: bool, detail: str = "") -> bool:
    print(("  [PASS] " if ok else "  [FAIL] ") + label + (" :: " + detail if detail else ""))
    if not ok:
        FAILED.append(label)
    return ok


def main() -> int:
    ok = True
    print("B1 回归确认（零改；ROOT=%s）" % ROOT)

    print("\n[现行落点核对] 计划称这些已经是 Driver 代产完整 slice-plan，不重复修")
    closure_row = lines("closure.md", r"^\| 3 \| 切片")
    ok &= p("closure.md 主链第 3 行存在", bool(closure_row), "1 行" if closure_row else "0 行")
    if closure_row:
        row = closure_row[0]
        ok &= p("第 3 行跳过时由 Driver 代产完整 slice-plan", "roles/driver.md" in row and "slice-plan" in row and "五字段全填" in row)
        print("      行文: " + row[:300])
    driver_s3 = lines("roles/driver.md", r"^\*\*产出 `slice-plan`")
    ok &= p("driver §3 声明 slice-plan 产出", bool(driver_s3))
    driver_only = lines("roles/driver.md", r"只在「单片、无依赖」时由 Driver 代产")
    ok &= p("driver §3 限定「单片、无依赖」才代产", bool(driver_only), driver_only[0] if driver_only else "")
    pipe11 = lines("pipeline.md", r"^driver -> slice-plan -> implementer$")
    ok &= p("pipeline §11 有 Driver→slice-plan→Implementer 边", bool(pipe11))
    impl40 = lines("roles/implementer.md", r"唯一合法动作是停止")
    ok &= p("implementer §4.0 缺件先停", bool(impl40))

    print("\n[场景 1] 只有 task-card、没有 slice-plan")
    zero = lines("roles/implementer.md", r"拿到完整 `slice-plan` 之前\*\*零写入\*\*")
    stop = lines("roles/implementer.md", r"\*\*停止开工\*\*")
    route = lines("roles/implementer.md", r"请它合法代产（或转 `roles/planner.md`）")
    ok &= p("实现者零写入", bool(zero))
    ok &= p("实现者停止开工", bool(stop), "%d 行" % len(stop))
    ok &= p("点名要 Driver/Planner 补", bool(route))
    print("      读数: 缺 slice-plan → 停止开工 + 零写入 + 向 Driver（或 Planner）点名缺件")

    print("\n[场景 2] Driver 合法代产全字段 slice-plan")
    fields = lines("roles/driver.md", r"^\| `slices` \| 只有一片")
    verif = lines("roles/driver.md", r"^\| `verification` \| 该片的验证命令")
    scope = lines("roles/driver.md", r"^\| `scope` \|")
    auth = lines("roles/implementer.md", r"auth_record")
    ok &= p("代产切片含五字段（slices/verification/scope 可见）", bool(fields and verif and scope))
    ok &= p("实现者仍核 auth_record", bool(auth))
    print("      读数: 收据齐 + 授权有效 → 开工（不因代产者身份改变而降低核对）")

    print("\n[零改证据] 与上一轮结束时逐字一致")
    prev = {}
    prev_file = ROOT / ".pi/repair/evidence/post-hashes.txt"
    for ln in prev_file.read_text(encoding="utf-8").splitlines():
        if not ln.strip():
            continue
        h, path = ln.split("  ", 1)
        prev[path.strip()] = h
    for rel in ("closure.md", "scripts/ws-identity.sh"):
        now = hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()
        ok &= p("%s 未被本项改动" % rel, prev.get(rel) == now, "%s" % now[:16])

    print("\nB1 结论: " + ("回归成立、零产物修改" if ok else "存在 FAIL: " + "; ".join(FAILED)))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
