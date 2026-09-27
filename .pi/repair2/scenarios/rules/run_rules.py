#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A1/B2/B3 规则层验收（含"两种自洽读法→问 Owner"与"不新增层"两项）。"""
from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path("/Users/yuantian/Developer/tim-professional-workflow")
FAILED = []


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def p(label: str, ok: bool, detail: str = "") -> bool:
    print(("  [PASS] " if ok else "  [FAIL] ") + label + (" :: " + detail if detail else ""))
    if not ok:
        FAILED.append(label)
    return ok


def has(rel: str, needle: str) -> bool:
    return needle in read(rel)


def main() -> int:
    print("A1/B2/B3 规则层验收（ROOT=%s）" % ROOT)

    print("\n[A1] 判据质量由上游持有；错实现对照在开写窗前给出")
    for label, rel, needle in [
        ("planner §4.6 提出一个合理错实现", "roles/planner.md", "写判据时先从 Owner 的结果句提出至少一个合理但错误的实现或边界读法"),
        ("planner §4.6 make check 只说明入口", "roles/planner.md", "`make check` 只说明运行入口"),
        ("planner §4.6 语义未定才问 Owner", "roles/planner.md", "语义本身未定才问 Owner"),
        ("driver task-card.verification 正/反对照", "roles/driver.md", "一组可判否的正/反对照"),
        ("driver 不得只填 make check 并据它放行", "roles/driver.md", "不得只填 `make check` 并据它放行"),
        ("driver §4.2 第 6 步发卡前核对", "roles/driver.md", "发卡前核对 `verification`"),
        ("driver 补判据由 Implementer 改测试", "roles/driver.md", "Driver 与 Reviewer 都不顺手改产品"),
        ("driver 代产 slice-plan.verification 含正/反对照", "roles/driver.md", "该片的验证命令与判否条件，以及能把"),
        ("reviewer §4.5 独立挑战保留", "roles/reviewer.md", "### 4.5 反实现挑战"),
        ("verifier §4.6 独立挑战保留", "roles/verifier.md", "### 4.6 判据必须能失败"),
    ]:
        p(label, has(rel, needle))

    print("\n[B2] 范围声明：运行时产物不自动全局豁免")
    for label, rel, needle in [
        ("identity §2 不自动全局豁免", "identity.md", "编排/工具运行时产物不自动全局豁免"),
        ("identity §2 每项必答", "identity.md", "如果这里放了产品代码，它会被排掉吗？"),
        ("identity §2 事后扩大无效", "identity.md", "不能事后扩大为 `.pi/**`"),
        ("driver task-card.scope 分列", "roles/driver.md", "仅作全树比对例外的运行时路径"),
        ("driver §4.4 第 5 步首个写入前声明", "roles/driver.md", "首个写入前**声明并指名具体路径"),
        ("integrator §4.1 第 5 步两套范围声明", "roles/integrator.md", "各自正确的范围声明"),
        ("integrator 事后扩大不得换取无越界", "roles/integrator.md", "事后扩大排除清单不得换取"),
    ]:
        p(label, has(rel, needle))

    print("\n[B3] 证据寿命：临时不当长期锚；承重证据写明保留点")
    for label, rel, needle in [
        ("pipeline §8 位置未失效", "pipeline.md", "位置未失效"),
        ("reviewer §3 coverage 承重证据要素", "roles/reviewer.md", "需保留到哪个交付/复核点、原产者"),
        ("reviewer §4.1 第 8 步 /tmp 只算临时证据", "roles/reviewer.md", "只算**临时证据**"),
        ("reviewer §4.1 禁止静默搬迁", "roles/reviewer.md", "不得静默搬到范围外目录"),
        ("verifier §3 commands 保留点/原产者", "roles/verifier.md", "需保留到哪个交付点、原产者"),
        ("verifier §3 falsification 临时读数", "roles/verifier.md", "变异读数只存在于临时位置时"),
        ("verifier §3 uncovered 不可复用推断", "roles/verifier.md", "因临时证据失效或未获准稳定保管而**不可复用**"),
        ("driver §4.4 第 6 步三问", "roles/driver.md", "现在可取回 + 保管到所需时间 + 搬迁有授权"),
        ("driver §4.8 第 7 步 roundup 写保留结论", "roles/driver.md", "不得把未获保管授权的临时证据写成将来可复用"),
    ]:
        p(label, has(rel, needle))

    print("\n[硬约束] 不新增角色 / 收据 / 总控层；ws-identity.sh 不加全局排除")
    roles = sorted(x.name for x in (ROOT / "roles").glob("*.md"))
    p("角色数仍为 10", len(roles) == 10, str(len(roles)))
    for banned in ("evidence-store", "harness-receipt", "evidence-budget"):
        p("未引入新 artifact %s" % banned, banned not in "".join(read("roles/" + r) for r in roles))
    ws = read("scripts/ws-identity.sh")
    p("ws-identity.sh 仍无 .pi 排除项", ".pi" not in ws.replace("__pycache__", ""))
    p("ws-identity.sh 排除表未变（.git/缓存/构建产物/pycache）", ".pytest_cache" in ws and "*.pyc" in ws)

    print("\nA1/B2/B3 结论: " + ("全部通过" if not FAILED else "存在 FAIL: " + "; ".join(FAILED)))
    return 0 if not FAILED else 1


if __name__ == "__main__":
    sys.exit(main())
