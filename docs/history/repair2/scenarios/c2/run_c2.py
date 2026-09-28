#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C2 情景 · 范围对照（真跑：全树比对 + 库自带 ws-identity.sh）。

断言：
 1. 事前声明的运行时例外（具名 loops 路径）可在全树比对中排除；
 2. 未声明的 .pi/ 源码文件（.pi/evil.py）必须被发现为范围外变更；
 3. 事后扩大排除（改成 .pi/**）不得换取"无越界"结论（声明哈希门）；
 4. 候选 manifest 只覆盖两个白名单文件，loops 自动写入不使其漂移；
 5. scripts/ws-identity.sh 无"全局排除 .pi/**"。
"""
from __future__ import annotations

import fnmatch
import hashlib
import os
import pathlib
import shutil
import subprocess
import sys

ROOT = pathlib.Path("/Users/yuantian/Developer/tim-professional-workflow")
SC = ROOT / ".pi/repair2/scenarios/c2"
TREE = SC / "tree"
DECL = SC / "range-declaration.json"
WSID = ROOT / "scripts/ws-identity.sh"

EXPECT_EXCEPTIONS = [".pi/loops/loops-*.json", ".pi/loops/loops-*.json.prev"]
WRITE_SCOPE = ["src/price.ts", "src/fee.ts"]


def sha(p: pathlib.Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def all_files() -> list[str]:
    out = []
    for dirpath, _d, files in os.walk(TREE):
        for f in files:
            out.append(os.path.relpath(os.path.join(dirpath, f), TREE))
    return sorted(out)


def snapshot() -> dict[str, str]:
    return {rel: sha(TREE / rel) for rel in all_files()}


def changed_since(base: dict[str, str]) -> list[str]:
    now = snapshot()
    out = []
    for rel, dig in now.items():
        if rel not in base or base[rel] != dig:
            out.append(rel)
    for rel in base:
        if rel not in now:
            out.append(rel + " (deleted)")
    return sorted(out)


def excluded_by(rel: str, patterns: list[str]) -> bool:
    return any(fnmatch.fnmatch(rel, pat) for pat in patterns)


def p(label: str, ok: bool, detail: str = "") -> bool:
    print(("  [PASS] " if ok else "  [FAIL] ") + label + (" :: " + detail if detail else ""))
    return ok


def ws(*args: str) -> subprocess.CompletedProcess:
    # 路径按调用方 cwd 解析：在 fixture tree 里跑，路径才对应候选仓根
    return subprocess.run(["bash", str(WSID), *args], capture_output=True, text=True, cwd=str(TREE))


def main() -> int:
    ok = True
    print("C2 范围对照（tree=%s）" % TREE)
    # 重置现场为基线
    (TREE / "src/price.ts").write_text("export const FEE = 1500;\n", encoding="utf-8")
    (TREE / "src/fee.ts").write_text("export function price(total: number) { return total - 1500; }\n", encoding="utf-8")
    (TREE / ".pi/loops/loops-1.json").write_text('{"fire":1}\n', encoding="utf-8")
    (TREE / ".pi/loops/loops-1.json.prev").write_text('{"fire":0}\n', encoding="utf-8")
    evil = TREE / ".pi/evil.py"
    if evil.exists():
        evil.unlink()
    if (SC / "range-declaration-widened.json").exists():
        (SC / "range-declaration-widened.json").unlink()

    base = snapshot()
    decl_hash_pre = sha(DECL)
    print("  基线文件数=%d；事前声明 sha256=%s" % (len(base), decl_hash_pre[:16]))

    # 候选 manifest（只有两个白名单文件）
    pathlist = SC / "candidate-paths.txt"
    pathlist.write_text("\n".join(WRITE_SCOPE) + "\n", encoding="utf-8")
    m1 = ws("manifest", str(pathlist))
    man1 = SC / "candidate-manifest-1.txt"
    man1.write_text(m1.stdout, encoding="utf-8")
    d1 = ws("digest", str(man1)).stdout.strip()
    print("  候选 manifest(两文件) digest=%s" % d1)

    # (a) 运行时写入：仅具名 loops 文件变化
    (TREE / ".pi/loops/loops-1.json").write_text('{"fire":2}\n', encoding="utf-8")
    (TREE / ".pi/loops/loops-1.json.prev").write_text('{"fire":1}\n', encoding="utf-8")
    changed_a = changed_since(base)
    loops_changed = sorted(c for c in changed_a if c.startswith(".pi/loops/"))
    conf_a = [c for c in changed_a if c not in loops_changed]
    out_a = [c for c in loops_changed if not excluded_by(c, EXPECT_EXCEPTIONS)] + conf_a
    print("  (a) 变化=%s" % changed_a)
    ok &= p("具名 loops 变化可被事前声明排除", all(excluded_by(c, EXPECT_EXCEPTIONS) for c in loops_changed), str(loops_changed))
    ok &= p("(a) 范围外变更集为空", not out_a, str(out_a))
    m2 = ws("manifest", str(pathlist))
    man2 = SC / "candidate-manifest-2.txt"
    man2.write_text(m2.stdout, encoding="utf-8")
    d2 = ws("digest", str(man2)).stdout.strip()
    ok &= p("loops 自动写入不使两文件候选 manifest 漂移", d1 == d2, "%s vs %s" % (d1[:14], d2[:14]))
    v = ws("verify", str(man2), str(pathlist))
    ok &= p("身份复核走 verify：运行时写入后按范围声明复核仍通过", v.returncode == 0,
            "exit=%d %s" % (v.returncode, (v.stdout or v.stderr).strip().splitlines()[:1]))

    # (b) 契约内改动：两个白名单源码文件变化
    (TREE / "src/price.ts").write_text("export const FEE = 1500; // contract v2\n", encoding="utf-8")
    (TREE / "src/fee.ts").write_text("export function price(total: number) { return total - FEE; }\n", encoding="utf-8")
    changed_b = changed_since(base)
    in_scope = [c for c in changed_b if c in WRITE_SCOPE]
    print("  (b) 白名单内变化=%s" % in_scope)
    ok &= p("白名单内改动被记入写入范围", sorted(in_scope) == sorted([c for c in changed_b if c in WRITE_SCOPE]), str(in_scope))
    m3 = ws("manifest", str(pathlist))
    man3 = SC / "candidate-manifest-3.txt"
    man3.write_text(m3.stdout, encoding="utf-8")
    d3 = ws("digest", str(man3)).stdout.strip()
    ok &= p("契约内源码改动使候选身份变化（需新冻结）", d3 != d1, "%s -> %s" % (d1[:14], d3[:14]))

    # (c) 未声明的 .pi/ 源码文件
    evil.write_text("FEE = 1500\n", encoding="utf-8")
    changed_c = changed_since(base)
    undeclared = [c for c in changed_c if c not in WRITE_SCOPE and not excluded_by(c, EXPECT_EXCEPTIONS)]
    print("  (c) 未声明新增后的范围外变更=%s" % undeclared)
    ok &= p("未声明的 .pi/ 源码文件必须被发现", ".pi/evil.py" in undeclared, str(undeclared))

    # (d) 事后扩大排除：以"先声明后写入"的哈希门判定无效
    widened = SC / "range-declaration-widened.json"
    widened.write_text('{"write_scope": ["src/price.ts", "src/fee.ts"], "runtime_exceptions": [".pi/**"], "declared_by": "driver", "declared_before_first_write": true}\n', encoding="utf-8")
    hash_now = sha(DECL)
    gate_ok = hash_now == decl_hash_pre
    ok &= p("事前声明未被事后改写（哈希门）", gate_ok, "pre=%s now=%s" % (decl_hash_pre[:12], hash_now[:12]))
    guarded_out = [c for c in changed_c if c not in WRITE_SCOPE and not excluded_by(c, EXPECT_EXCEPTIONS)]
    print("  (d) 即使另写一份 .pi/** 排除声明，判定仍用事前声明 → 范围外=%s；不得据此得出\"无越界\"" % guarded_out)
    ok &= p("事后扩大排除不得获得\"无越界\"结论", ".pi/evil.py" in guarded_out, str(guarded_out))

    # (e) 库工具不含全局 .pi 排除
    text = WSID.read_text(encoding="utf-8")
    bad = [ln for ln in text.splitlines() if ".pi" in ln and ("return 0" in ln or "case" in ln or "exclude" in ln.lower())]
    ok &= p("scripts/ws-identity.sh 无\"全局排除 .pi/**\"", not bad and ".pi" not in text.replace("__pycache__", ""), "命中 %d 行" % len(bad))
    print("  ws-identity.sh sha256=%s" % sha(WSID)[:16])

    print("\nC2 结论: " + ("全部通过" if ok else "存在 FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
