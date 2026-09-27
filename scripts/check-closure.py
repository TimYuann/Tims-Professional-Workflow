#!/usr/bin/env python3
"""
check-closure.py · 闭包检查器（只读，可重复运行）

它回答一个问题：**这套工作流是通的吗？**

「通」被拆成可机械判定的七条断言。任何一条不成立即非零退出。

  C1 结构        registry 可解析，VERSION 单一来源
  C2 产物闭合    每个产物类型有且仅有一个产出角色；每个产物至少被一个阶段消费
  C3 阶段可达    从 P0 出发每个阶段可达；阶段开工所需产物在其之前已被产出
  C4 判据可判定   阶段退出判据引用的产物字段真实存在
  C5 角色装配件   角色声明的产物/技能/原则都存在；技能与原则反向指认一致
  C6 引用完整     每个技能/原则/横切带被至少一个角色或阶段引用（无孤儿）
  C7 上游处置完备 upstreams/ 下每个 SKILL.md 在处置表里恰好出现一次

它判不了：判据本身是否合理、方法是否有效、下游是否真的照做。
这些交给 check-consistency.py 与人审。

用法:
  python3 scripts/check-closure.py            # 全量
  python3 scripts/check-closure.py --quiet    # 只输出结论
"""

import sys, os, re, argparse
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("需要 pyyaml：python3 -m pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "workflow" / "registry.yaml"

# 运行底座名称黑名单：本库只声明"需要什么能力"，不写"用什么跑"。
DECOUPLING_PATTERNS = [
    (r"\bherdr\b", "终端工作区管理器"),
    (r"\bpi[- ]?intercom\b", "会话总线"),
    (r"\bclaude\b(?![\w-])", "某编码 agent"),
    (r"\bcodex\b(?![\w-])", "某编码 agent"),
    (r"\bcursor\b(?![\w-])", "某编辑器"),
    (r"\bantigravity\b", "某编辑器"),
    (r"\bgemini\b(?![\w-])", "某模型"),
    (r"\bopenai\b", "某厂商"),
    (r"\banthropic\b", "某厂商"),
    (r"\bopencode\b", "某编码 agent"),
    (r"\bwindsurf\b", "某编辑器"),
    (r"\bglasp\b", "某应用容器"),
    (r"\btmux\b", "某终端复用器"),
    (r"\b[Pp][Ii] [A-Za-z]", "某品牌名"),
]

# 只扫「库内容」。docs/ 是历史材料与外部评审，archive/ 是被替换掉的旧载体——
# 它们记录曾经发生过什么，不构成对下游的指令，因此豁免。
SCAN_DIRS = ("workflow", "roles", "skills", "principles", "scripts")
SCAN_FILES = ("README.md", "AGENTS.md", "VERSION")

# 上游仓库目录名 -> 处置表里的前缀
UPSTREAM_PREFIX = {
    "cursor-plugins": "pstack",
    "mattpocock-skills": "matt",
    "addyosmani-agent-skills": "addy",
}
SKIP_DIRS = {"node_modules", "deprecated", "in-progress", "templates", "assets",
             "references", ".git", "automations", "third_party", "docs", "agents",
             "commands", "evals", "hooks", "schemas", "scripts"}


class Result:
    def __init__(self):
        self.checks = []

    def add(self, cid, name, ok, detail="", misses=None):
        self.checks.append((cid, name, ok, detail, misses or []))

    @property
    def failed(self):
        return [c for c in self.checks if not c[2]]

    def report(self, quiet=False):
        if not quiet:
            print("TIM · check-closure.py（只读闭包检查）")
            print(f"真源: {REGISTRY.relative_to(ROOT)}")
            print("-" * 76)
            for cid, name, ok, detail, misses in self.checks:
                print(f"[{'PASS' if ok else 'FAIL'}] {cid} {name:<22} {detail}")
                for m in misses[:12]:
                    print(f"         ↳ {m}")
                if len(misses) > 12:
                    print(f"         ↳ …另 {len(misses) - 12} 条")
        npass = sum(1 for c in self.checks if c[2])
        nfail = len(self.failed)
        print("-" * 76)
        print(f"合计: {npass} 项通过 / {nfail} 项失败 / {len(self.checks)} 项检查")
        return 0 if nfail == 0 else 1


def find_upstream_skills():
    """扫出 upstreams/ 下每个 SKILL.md，返回 repo_prefix:skill_name 列表。"""
    up = ROOT / "upstreams"
    found = []

    def walk(d, prefix):
        try:
            entries = sorted(d.iterdir(), key=lambda p: p.name)
        except OSError:
            return
        for e in entries:
            if not e.is_dir() or e.name.startswith(".") or e.name in SKIP_DIRS:
                continue
            if (e / "SKILL.md").is_file():
                found.append(f"{prefix}:{e.name}")
            else:
                walk(e, prefix)

    for dirname, prefix in UPSTREAM_PREFIX.items():
        base = up / dirname
        if not base.is_dir():
            continue
        # pstack 藏在 cursor-plugins/pstack 下
        if prefix == "pstack" and (base / "pstack" / "skills").is_dir():
            walk(base / "pstack" / "skills", prefix)
        else:
            walk(base / "skills", prefix)
    return sorted(found)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    r = Result()
    if not REGISTRY.is_file():
        print(f"找不到 {REGISTRY}")
        return 2
    reg = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))

    artifacts = reg.get("artifacts", [])
    phases = reg.get("phases", [])
    ribbons = reg.get("ribbons", [])
    roles = reg.get("roles", [])
    principles = reg.get("principles", [])
    skills = reg.get("skills", [])
    disp = reg.get("upstream_dispositions", [])

    a_by_id = {a["id"]: a for a in artifacts}
    p_by_id = {p["id"]: p for p in phases}
    r_by_id = {x["id"]: x for x in roles}
    pr_by_id = {p["id"]: p for p in principles}
    s_by_id = {s["id"]: s for s in skills}

    # ── C1 结构 ────────────────────────────────────────────────
    vfile = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    miss = []
    if reg.get("version") != vfile:
        miss.append(f"VERSION 文件={vfile}，registry={reg.get('version')}")
    for label, coll, key in (("产物", artifacts, "id"), ("阶段", phases, "id"),
                             ("角色", roles, "id"), ("原则", principles, "id"),
                             ("技能", skills, "id")):
        ids = [x[key] for x in coll]
        dup = {i for i in ids if ids.count(i) > 1}
        if dup:
            miss.append(f"{label} id 重复: {sorted(dup)}")
    r.add("C1", "结构与版本单一来源", not miss,
          f"版本 {vfile}，产物 {len(artifacts)}／阶段 {len(phases)}／角色 {len(roles)}"
          f"／原则 {len(principles)}／技能 {len(skills)}", miss)

    # ── C2 产物闭合 ────────────────────────────────────────────
    miss = []
    producers = {}
    for a in artifacts:
        for c in a.get("consumers", []):
            if c not in p_by_id:
                miss.append(f"{a['id']}.consumers 引用不存在的阶段 {c}")
        if not a.get("fields"):
            miss.append(f"{a['id']} 没有字段定义（无法判定下游能不能用）")
        if not a.get("rationale"):
            miss.append(f"{a['id']} 没有写明为什么需要它")
        prod = a.get("producer")
        if prod not in r_by_id:
            miss.append(f"{a['id']} 的产出方 {prod} 不是已定义角色")
        producers.setdefault(a["id"], []).append(prod)
        if not a.get("consumers"):
            miss.append(f"{a['id']} 没有任何阶段消费——孤儿产物")
    r.add("C2", "产物有主且有人接", not miss,
          f"{len(artifacts)} 类产物全部有唯一产出方且被消费", miss)

    # ── C3 阶段可达 + 所需产物已被产出 ────────────────────────
    miss = []
    produced_by = {}          # artifact_id -> set(phase_id)
    for ph in phases:
        for a in ph.get("produces", []):
            if a not in a_by_id:
                miss.append(f"{ph['id']} 声称产出不存在的产物 {a}")
            produced_by.setdefault(a, set()).add(ph["id"])
    # 常驻横切带从第一个阶段起就在写它的产物，不绑定到某个阶段
    ribbon_produced = set()
    for rb in ribbons:
        if not rb.get("always"):
            continue
        for a in rb.get("produces", []):
            if a not in a_by_id:
                miss.append(f"横切带 {rb['id']} 声称产出不存在的产物 {a}")
            ribbon_produced.add(a)
    if phases and phases[0].get("required_inputs"):
        miss.append(f"{phases[0]['id']} 是入口阶段，不应有 required_inputs")
    for i, ph in enumerate(phases):
        earlier = {p for q in phases[:i] for p in q.get("produces", [])}
        if i == 0:
            earlier |= ribbon_produced
        for need in ph.get("required_inputs", []):
            if need not in a_by_id:
                miss.append(f"{ph['id']} 所需产物 {need} 未定义")
            elif need not in earlier and need not in ribbon_produced:
                miss.append(f"{ph['id']} 需要 {need}，但它在此阶段之前没有被任何阶段或"
                            f"常驻横切带产出（产它的阶段：{sorted(produced_by.get(need, [])) or '无'}）")
        if not ph.get("exit_criteria"):
            miss.append(f"{ph['id']} 没有退出判据")
        if not ph.get("default_roles"):
            miss.append(f"{ph['id']} 没有默认角色")
    seen = set()
    for ph in phases:
        for dr in ph.get("default_roles", []):
            if dr not in r_by_id:
                miss.append(f"{ph['id']} 默认角色 {dr} 未定义")
        if ph["id"] in seen:
            miss.append(f"阶段 id 重复 {ph['id']}")
        seen.add(ph["id"])
    r.add("C3", "阶段可达且依赖闭合", not miss,
          f"{len(phases)} 个阶段按序可达，每个阶段所需产物在上游已产出", miss)

    # ── C4 退出判据引用的字段真实存在 ──────────────────────────
    field_re = re.compile(r"\b(A\d+)\.([a-z_]+)")
    miss = []
    for ph in phases:
        for crit in ph.get("exit_criteria", []):
            for aid, fld in field_re.findall(crit):
                if aid not in a_by_id:
                    miss.append(f"{ph['id']} 判据引用未定义产物 {aid}")
                elif fld not in a_by_id[aid].get("fields", []):
                    miss.append(f"{ph['id']} 判据引用 {aid}.{fld}，但该字段未定义"
                                f"（现有：{a_by_id[aid].get('fields')}）")
            if not field_re.search(crit):
                miss.append(f"{ph['id']} 判据未指向任何产物字段，不可判定：{crit[:40]}")
    for a in artifacts:
        # 闭包的正确表述：产出该产物的阶段，必须在它的退出判据里校验它——
        # 否则下游拿到的是一份没人验证过的东西。
        owners = [p_by_id[q] for q in produced_by.get(a["id"], set()) if q in p_by_id]
        for ph in owners:
            if not any(x.split(".")[0] == a["id"] for x in ph.get("exit_criteria", [])
                       if field_re.search(x)):
                miss.append(f"{a['id']} 由 {ph['id']} 产出，但 {ph['id']} 的退出判据里"
                            f"没有校验它——下游会拿到一份没被验证过的产物")
    r.add("C4", "判据可判定", not miss,
          f"{sum(len(p.get('exit_criteria', [])) for p in phases)} 条退出判据全部指向真实字段", miss)

    # ── C5 角色装配件一致性 ────────────────────────────────────
    miss = []
    for role in roles:
        rid = role["id"]
        for a in role.get("owns_artifacts", []):
            if a not in a_by_id:
                miss.append(f"{rid} 声称拥有未定义产物 {a}")
            elif a_by_id[a].get("producer") != rid:
                miss.append(f"互斥：产物 {a} 的主产出方是 {a_by_id[a].get('producer')}，"
                            f"但 {rid} 也声称拥有它")
        for s in role.get("skills", []):
            if s not in s_by_id:
                miss.append(f"{rid} 引用不存在的技能 {s}")
            elif s_by_id[s].get("owner_role") != rid:
                miss.append(f"互斥：技能 {s} 声明属于 {s_by_id[s].get('owner_role')}，"
                            f"但 {rid} 的技能清单里有它")
        for p in role.get("principles", []):
            if p not in pr_by_id:
                miss.append(f"{rid} 引用不存在的原则 {p}")
        if not role.get("forbidden"):
            miss.append(f"{rid} 没有硬边界（forbidden 为空）")
    for a in artifacts:
        prod = a.get("producer")
        if prod in r_by_id and a["id"] not in r_by_id[prod].get("owns_artifacts", []):
            miss.append(f"产物 {a['id']} 的产出方 {prod} 未把它列入 owns_artifacts")
    # 原则正文只有一处：owner 唯一，且 owner 必须在引用它的人当中
    for pid, pr in pr_by_id.items():
        owner = pr.get("owner")
        referrers = {rid for role in roles for rid in [role["id"]]
                     if pid in role.get("principles", [])}
        if owner not in r_by_id:
            miss.append(f"原则 {pid} 的 owner {owner} 不是已定义角色")
        elif owner not in referrers:
            miss.append(f"原则 {pid} 的 owner 是 {owner}，但 {owner} 自己的心智模型里没有它")
        if not pr.get("text"):
            miss.append(f"原则 {pid} 没有正文")
    # 互斥：同一角色不得既是某技能的 owner 又在别的角色清单里重复挂载
    for sid, sk in s_by_id.items():
        hosts = [role["id"] for role in roles if sid in role.get("skills", [])]
        if len(hosts) > 1:
            miss.append(f"互斥：技能 {sid} 同时挂在 {hosts} 身上——技能归属唯一")
    r.add("C5", "角色装配件一致", not miss,
          f"{len(roles)} 个角色的产物／技能／原则指认双向一致", miss)

    # ── C6 无孤儿 ──────────────────────────────────────────────
    miss = []
    used_skills = {s for role in roles for s in role.get("skills", [])}
    used_skills |= {s for rb in ribbons for s in rb.get("skills", [])}
    for sid in s_by_id:
        if sid not in used_skills:
            miss.append(f"技能 {sid} 没有任何角色或横切带引用——孤儿")
    used_pr = {p for role in roles for p in role.get("principles", [])}
    for pid in pr_by_id:
        if pid not in used_pr:
            miss.append(f"原则 {pid} 没有任何角色引用——孤儿")
    for rb in ribbons:
        for s in rb.get("skills", []):
            if s not in s_by_id:
                miss.append(f"横切带 {rb['id']} 引用不存在的技能 {s}")
        if not rb.get("why"):
            miss.append(f"横切带 {rb['id']} 没写为什么它必须一直在")
    # 每个阶段至少能装出产出它所需产物的角色
    for ph in phases:
        prods = ph.get("produces", [])
        if not prods:
            continue
        equipped = set(ph.get("default_roles", []))
        for a in prods:
            if a in a_by_id and a_by_id[a].get("producer") not in equipped:
                miss.append(f"{ph['id']} 声称产出 {a}，但该阶段的默认角色里没有它的产出方 "
                            f"{a_by_id[a].get('producer')}")
    r.add("C6", "无孤儿且阶段装得出来", not miss,
          f"{len(skills)} 个技能／{len(principles)} 条原则全部被引用，"
          f"每个阶段的默认角色能产出它声称的产物", miss)

    # ── C7 上游处置完备（对文件系统核对）───────────────────────
    actual = find_upstream_skills()
    listed = [d["upstream"] for d in disp]
    miss = []
    dup = sorted({u for u in listed if listed.count(u) > 1})
    for u in dup:
        miss.append(f"处置表里 {u} 出现了 {listed.count(u)} 次（必须恰好一次）")
    for u in actual:
        if u not in listed:
            miss.append(f"{u} 在 upstreams/ 里存在，但处置表里没有它——要么补上要么说明为什么跳过")
    for u in listed:
        if u not in actual:
            miss.append(f"处置表里的 {u} 在 upstreams/ 里不存在——可能是拼错或上游已改名")
    known = set(s_by_id) | set(pr_by_id)
    for d in disp:
        if d.get("outcome") not in ("absorbed", "merged", "rejected"):
            miss.append(f"{d['upstream']} 的 outcome 非法：{d.get('outcome')}")
        if not d.get("reason"):
            miss.append(f"{d['upstream']} 没有写处置理由")
        into = d.get("into")
        if into and into not in known:
            miss.append(f"{d['upstream']} 指向 {into}，但注册表里没有这个技能或原则")
    r.add("C7", "上游处置完备", not miss,
          f"文件系统 {len(actual)} 个上游 skill，处置表 {len(listed)} 条，一一对应", miss)

    # ── 解耦检查 ───────────────────────────────────────────────
    miss = []
    targets = [f for f in (ROOT / n for n in SCAN_FILES) if f.is_file()]
    for d in SCAN_DIRS:
        p = ROOT / d
        if p.is_dir():
            targets += [f for f in sorted(p.rglob("*")) if f.suffix in (".md", ".yaml", ".yml", ".py")]
    for f in targets:
        try:
            text = f.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        for pat, label in DECOUPLING_PATTERNS:
            for m in re.finditer(pat, text):
                # 本检查器自身的黑名单不参与判定
                if f.name == "check-closure.py":
                    continue
                line = text[:m.start()].count("\n") + 1
                ctx = text.splitlines()[line - 1].strip()[:90]
                miss.append(f"{f.relative_to(ROOT)}:{line} 出现具体底座（{label}）→ {ctx}")
    r.add("D1", "底座解耦", not miss,
          f"扫描 {len(targets)} 个库内容文件，0 处具体运行底座名称", miss)

    return r.report(args.quiet)


if __name__ == "__main__":
    sys.exit(main())
