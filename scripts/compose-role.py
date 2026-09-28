#!/usr/bin/env python3
"""
compose-role.py · 把一个角色装配成一段可直接注入的 system prompt（只读）

为什么需要它：原则正文只允许存在于 `principles/`。角色文件里只留
`@p-xxx` 引用与 role-specific 的 trigger，不复述原则的意思——否则同一条
语义就有两份副本，必然漂。

而冷启动文档教的是「把角色文件正文发进空会话」。在装配器存在之前，
`@p-type-system-discipline` 对模型只是一个没有定义的符号。
本脚本把这件事变成机械的：装配角色时���定把被引用的原则正文一起带上。

用法:
  python3 scripts/compose-role.py architect            # 装配一个角色
  python3 scripts/compose-role.py --all                # 装配全部角色
  python3 scripts/compose-role.py --check              # 只校验结构，不输出正文

`--check` 断言的是**结构事实**，不是语义相似度：
  1. 角色引用的每一个 `@p-xxx` 在注册表里真实存在；
  2. 每条原则的正文只有 `principles/` 这一个 canonical location；
  3. 角色文件里的原则条目只出现 id 与 trigger，不带第二份释义。

非零退出即失败。任何一条不成立都不许靠改措辞糊过去。
"""

import re
import sys
import argparse
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("需要 pyyaml：python3 -m pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "workflow" / "registry.yaml"
ROLES_DIR = ROOT / "roles"
PRINCIPLES_DIR = ROOT / "principles"

# 角色文件里引用原则的写法。同一行里 id 之后还有散文，就是第二份释义。
REF = re.compile(r"@([a-z0-9-]+)")
HEADING = re.compile(r"^## (p-[a-z0-9-]+)\s*$")
# `## 我的心智模型` 这类角色内的章节标题，用来圈定「本角色挂了哪些原则」
SECTION = re.compile(r"^##\s")


def load_registry():
    with REGISTRY.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def principle_bodies():
    """从 principles/ 取每条原则的正文。来源行不属于正文。"""
    bodies = {}
    for f in sorted(PRINCIPLES_DIR.glob("*.md")):
        cur, buf = None, []
        for line in read(f).splitlines():
            m = HEADING.match(line)
            if m:
                if cur:
                    bodies[cur] = "\n".join(buf).strip()
                cur, buf = m.group(1), []
                continue
            if cur is not None:
                if line.startswith("来源："):
                    bodies[cur] = "\n".join(buf).strip()
                    cur, buf = None, []
                    continue
                buf.append(line)
        if cur:
            bodies[cur] = "\n".join(buf).strip()
    return bodies


def role_refs(path: Path):
    """返回 (该角色引用的 id 集合, 结构性违规列表)。"""
    refs, bad = set(), []
    for i, line in enumerate(read(path).splitlines(), 1):
        ids = REF.findall(line)
        if not ids:
            continue
        for pid in ids:
            if not pid.startswith("p-"):
                continue
            refs.add(pid)
            # id 之后允许的只有列表符号、反引号、连字符。
            # 有 `——`、`：`、`，` 之类就是同一行带了释义。
            tail = line.split("@" + pid, 1)[1]
            body = tail.strip(" `*-\t")
            if body and not re.match(r"^`?\s*$", tail.strip()):
                bad.append((i, pid, body[:40]))
    return refs, bad


def check(registry):
    bodies = principle_bodies()
    known = {p["id"] for p in registry["principles"]}
    miss = []

    for role in registry["roles"]:
        path = ROLES_DIR / f"{role['id']}.md"
        if not path.is_file():
            miss.append(f"角色 {role['id']} 没有角色文件")
            continue
        refs, bad = role_refs(path)
        for pid in sorted(refs):
            if pid not in known:
                miss.append(
                    f"{path.name}:{pid} —— 引用了注册表里不存在的原则")
            elif pid not in bodies:
                miss.append(
                    f"{path.name}:{pid} —— 注册表里有，但 principles/ 里找不到正文")
        for line_no, pid, tail in bad:
            miss.append(
                f"{path.name}:{line_no}: @{pid} 后面带了第二份释义"
                f"（{tail}…）——原则正文只允许存在于 principles/，"
                f"角色里只留 id 与 trigger")
        # 角色声明引用、但正文里没提的，反向也算漂
        for pid in role.get("principles", []):
            if pid not in refs:
                miss.append(
                    f"{path.name}: 注册表声明挂载 {pid}，正文里却没有 @ 引用")

    # 原则正文只能有一处：roles/ 与 skills/ 里都不许再出现 `## p-` 章节
    for d in (ROLES_DIR, ROOT / "skills"):
        if not d.is_dir():
            continue
        for f in d.rglob("*.md"):
            for i, line in enumerate(read(f).splitlines(), 1):
                if HEADING.match(line):
                    miss.append(
                        f"{f.relative_to(ROOT)}:{i}: 出现了原则正文标题"
                        f"——canonical location 只有 principles/")

    return miss


def compose(registry, role_id):
    bodies = principle_bodies()
    path = ROLES_DIR / f"{role_id}.md"
    refs, _ = role_refs(path)
    order = [p["id"] for p in registry["principles"] if p["id"] in refs]
    out = [read(path).rstrip(), "",
           "---", "",
           "# 以下为该角色引用的原则正文（唯一 canonical location：principles/）", ""]
    for pid in order:
        zh = next((p.get("zh", "") for p in registry["principles"]
                   if p["id"] == pid), "")
        out += [f"## {pid}" + (f" · {zh}" if zh else ""), "", bodies.get(pid, "（缺失）"), ""]
    return "\n".join(out).rstrip() + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description="角色装配器 / 原则结构检查")
    ap.add_argument("role", nargs="?", help="要装配的角色 id")
    ap.add_argument("--all", action="store_true", help="装配全部角色")
    ap.add_argument("--check", action="store_true", help="只校验结构")
    a = ap.parse_args(argv)

    registry = load_registry()
    ids = [r["id"] for r in registry["roles"]]

    if a.check:
        miss = check(registry)
        if miss:
            print("角色装配：结构不成立")
            for m in miss:
                print(f"  ↳ {m}")
            print(f"\n合计: {len(miss)} 处结构问题")
            return 1
        n = sum(len(role_refs(ROLES_DIR / f"{i}.md")[0]) for i in ids)
        print(f"角色装配：结构成立（{len(ids)} 个角色，{n} 条原则引用，"
              f"正文均在 principles/，角色内无第二份释义）")
        return 0

    if a.all:
        for i in ids:
            print(compose(registry, i))
        return 0

    if not a.role:
        ap.error("给一个角色 id，或者 --all / --check")
    if a.role not in ids:
        print(f"没有角色 {a.role}。可选：{' '.join(ids)}")
        return 1
    print(compose(registry, a.role), end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
