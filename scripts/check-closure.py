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

import sys, os, re, argparse, subprocess
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

    def add(self, cid, name, ok, detail="", misses=None, skip=False):
        self.checks.append((cid, name, ok, detail, misses or [], skip))

    @property
    def failed(self):
        return [c for c in self.checks if not c[2] and not c[5]]

    def report(self, quiet=False):
        if not quiet:
            print("TIM · check-closure.py（只读闭包检查）")
            print(f"真源: {REGISTRY.relative_to(ROOT)}")
            print("-" * 76)
            for cid, name, ok, detail, misses, skip in self.checks:
                tag = "SKIP" if skip else ("PASS" if ok else "FAIL")
                print(f"[{tag}] {cid} {name:<22} {detail}")
                for m in misses[:12]:
                    print(f"         ↳ {m}")
                if len(misses) > 12:
                    print(f"         ↳ …另 {len(misses) - 12} 条")
        npass = sum(1 for c in self.checks if c[2] and not c[5])
        nskip = sum(1 for c in self.checks if c[5])
        nfail = len(self.failed)
        print("-" * 76)
        print(f"合计: {npass} 项通过 / {nfail} 项失败 / {nskip} 项跳过 / {len(self.checks)} 项检查")
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
    # VERSION 必须与当前 commit 上的 tag 对齐。v2.0.1–v2.0.3 三次打了 tag 却没改
    # VERSION，而 C1 只比前两个，所以一直 PASS——下游按 tag 锁定会锁到一个自称
    # 2.0.0 的东西。「版本单一来源」必须包含 release tag，否则不是单一来源。
    tag = subprocess.run(["git", "tag", "--points-at", "HEAD"],
                         capture_output=True, text=True,
                         cwd=str(ROOT)).stdout.split()
    if not tag:
        miss.append("当前 commit 上没有 tag——打了 tag 之前不能算一个 release")
    else:
        vtags = [x for x in tag if re.fullmatch(r"v?\d+\.\d+\.\d+", x)]
        if not vtags:
            miss.append(f"当前 commit 的 tag {tag} 里没有语义化版本号 tag")
        elif f"v{vfile}" not in tag:
            miss.append(f"VERSION={vfile}，但当前 commit 的 tag 是 {tag}——"
                        f"两者对不上。发版前先改 VERSION 再打 tag，或打 tag 后改 VERSION 再补打")
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

    # ── C7 上游处置完备（以随包分发的锁文件为准）──────────────
    # v2.0.1–v2.0.3 这里的反例：干净 clone 出来 C7/C9 直接红，
    # 因为核对依赖 upstreams/ 目录，而那三个只读克隆被 .gitignore 挡着。
    # 现在真源是随 release 分发的 upstreams.lock.yaml：
    #   - 没有 upstreams/ 时，用锁文件核对处置表与 sources（干净 clone 成立）
    #   - 有 upstreams/ 时，逐条比 sha256 并核 pin，把上游漂移抓出来
    listed = [d["upstream"] for d in disp]
    dup = sorted({u for u in listed if listed.count(u) > 1})
    known = set(s_by_id) | set(pr_by_id)

    lock = {}
    lock_path = ROOT / "upstreams.lock.yaml"
    have_lock = lock_path.is_file()
    if have_lock:
        lock = yaml.safe_load(lock_path.read_text(encoding="utf-8")) or {}
    lock_skills = lock.get("skills", {}) if lock else {}

    miss = []
    if not have_lock:
        miss.append("缺少 upstreams.lock.yaml——没有它，处置表在干净 clone 里无处核对")
    else:
        listed_set = set(listed)
        lock_set = set(lock_skills)
        for u in sorted(listed_set - lock_set):
            miss.append(f"{u} 在处置表里但锁文件里没有——锁文件过期，用 scripts/sync-upstreams.sh 重生成")
        for u in sorted(lock_set - listed_set):
            miss.append(f"{u} 在锁文件里但处置表里没有——要么补处置，要么说明为什么跳过")
        for x in dup:
            miss.append(f"处置表里 {x} 出现了 {listed.count(x)} 次（必须恰好一次）")
        for d in disp:
            if d.get("outcome") not in ("absorbed", "merged", "rejected"):
                miss.append(f"{d['upstream']} 的 outcome 非法：{d.get('outcome')}")
            if not d.get("reason"):
                miss.append(f"{d['upstream']} 没有写处置理由")
            if d.get("into") and d["into"] not in known:
                miss.append(f"{d['upstream']} 指向 {d['into']}，但注册表里没有这个技能或原则")
    r.add("C7", "上游处置完备（对锁文件）", not miss,
          f"锁文件 {len(lock_skills)} 个上游 skill，处置表 {len(listed)} 条，一一对应", miss)

    # ── C9 来源路径真实存在（对锁文件；有克隆时另比内容）──────
    miss = []
    for coll, kind in ((skills, "skill"), (principles, "principle")):
        for item in coll:
            for src in item.get("sources") or []:
                if src not in lock_skills:
                    miss.append(f"{kind} {item['id']} 的来源 {src} 不在上游锁文件里")
    detail = f"{len(lock_skills)} 个上游 skill 索引（锁文件），0 条失效来源"
    if lock_skills and (ROOT / "upstreams").is_dir():
        # 锁与实物对照：sha256 与 pin 都核
        import hashlib
        for key, ent in lock_skills.items():
            fp = ROOT / ent["path"]
            if not fp.is_file():
                miss.append(f"锁文件里的 {key} 在 upstreams/ 中不存在：{ent['path']}")
                continue
            h = hashlib.sha256(fp.read_bytes()).hexdigest()[:16]
            if h != ent["sha256"]:
                miss.append(f"{key} 的内容漂移：锁文件记 {ent['sha256']}，磁盘是 {h}"
                            f"（上游更新了，重跑 scripts/sync-upstreams.sh 并复核处置）")
        for pre, meta in (lock.get("repos") or {}).items():
            d = ROOT / meta["path"]
            if not (d / ".git").exists():
                continue
            head = subprocess.run(["git", "-C", str(d), "rev-parse", "HEAD"],
                                  capture_output=True, text=True).stdout.strip()
            if head != meta["commit"]:
                miss.append(f"上游 {pre} 的 pin 漂移：锁文件记 {meta['commit'][:7]}，"
                            f"克隆在 {head[:7]}")
        detail += "；并已逐条比对 sha256 与 pin"
    r.add("C9", "来源真实存在（锁 + 实物对照）", not miss, detail, miss)

    # ── C10 处置表声称吸收，目标就必须真的列了它 ────────────────
    # 这一条曾经缺失：6 条 absorbed 处置在 upstreams/ 里对得上，
    # 但目标技能的 sources 里根本没有它——台账在追一个没发生的事。
    miss = []
    for d in disp:
        into = d.get("into")
        if d.get("outcome") != "absorbed":
            if into:
                miss.append(f"{d['upstream']} 判为 {d['outcome']}，却仍指向 {into}")
            continue
        if not into:
            miss.append(f"{d['upstream']} 判为 absorbed 却没有指向任何技能或原则")
            continue
        tgt = s_by_id.get(into) or pr_by_id.get(into)
        if not tgt:
            miss.append(f"{d['upstream']} 指向不存在的 {into}")
        elif d["upstream"] not in (tgt.get("sources") or []):
            miss.append(f"假链接：{d['upstream']} 声称吸收进 {into}，"
                        f"但 {into} 的 sources 里没有它")
    r.add("C10", "处置与来源双向咬合", not miss,
          f"{len(disp)} 条处置与目标 sources 双向一致", miss)

    # ── C11 consumers 必须真的被 required_inputs 接住 ───────────
    # 允许「同阶段自产自消」（P1 消费自己产出的 A3），那是自我校验。
    miss = []
    for a in artifacts:
        for c in a.get("consumers", []):
            ph = p_by_id.get(c)
            if not ph:
                continue
            if a["id"] in ph.get("required_inputs", []):
                continue
            if a["id"] in ph.get("produces", []):
                continue      # 同阶段产出并校验，合法
            miss.append(f"{a['id']} 声明被 {c} 消费，但 {c} 既不 required 它、也不自己产出它"
                        f"——消费声明与实际装配对不上")
    r.add("C11", "消费声明与装配咬合", not miss,
          f"{sum(len(a.get('consumers', [])) for a in artifacts)} 条消费声明全部被阶段接住", miss)

    # ── C12 sources 为空的必须显式标 origin: library ───────────
    miss = []
    for s_ in skills:
        if not s_.get("sources") and s_.get("origin") != "library":
            miss.append(f"技能 {s_['id']} 没有来源也没标 origin: library"
                        f"——读者无法分辨它是「上游没有对应物」还是「忘了写来源」")
    r.add("C12", "原创技能显式标注", not miss,
          f"{sum(1 for x in skills if x.get('origin') == 'library')} 个原创技能已标注", miss)

    # ── C13 越权写：阶段判据不得要求更新别阶段产出的产物 ───────
    # 判据里说「已更新/已刷新/已保鲜」的是**写**，「可判定/非空/一致」的是**验**。
    # 写一个自己没有产出权的产物 = 角色越权，A3.freshness 被 verifier 更新就是这么来的。
    UPDATE_VERBS = ("已更新", "已刷新", "已保鲜", "已写入", "已补上", "已对齐", "已同步")
    miss = []
    for ph in phases:
        own = set(ph.get("produces", []))
        for crit in ph.get("exit_criteria", []):
            if not any(v in crit for v in UPDATE_VERBS):
                continue
            for aid in re.findall(r"\b(A\d+)\.", crit):
                if aid not in own:
                    prod = a_by_id.get(aid, {}).get("producer")
                    equipped = set(ph.get("default_roles", []))
                    miss.append(f"{ph['id']} 的判据要求更新 {aid}，但它的主产出方是 "
                                f"{prod}，不在 {ph['id']} 的默认角色 {sorted(equipped)} 里"
                                f"——越权写。验证偏差请写进本阶段自己产出的证据字段")
    r.add("C13", "判据不越权写他人产物", not miss,
          f"{len(phases)} 个阶段的 {sum(len(p.get('exit_criteria', [])) for p in phases)} 条判据"
          f"没有越权写", miss)

    # ── C14 技能头部的产物声明必须与注册表一致 ─────────────────
    # 抓的是这一类：头部写「产物：无」，产出节却写「A9 决策台账」。
    # 它们回答的是同一个问题，答案必须一样。
    miss = []
    for sk in skills:
        f = ROOT / "skills" / f"{sk['id']}.md"
        if not f.is_file():
            continue
        m = re.search(r"^- 阶段：.*?　产物：(.+)$", f.read_text(encoding="utf-8"), re.M)
        if not m:
            miss.append(f"技能文件 {sk['id']}.md 的头部没有「产物：」声明行")
            continue
        # 只取第一个括号之前的部分：头部允许带解释，解释不是产物声明
        raw = re.split(r"[（(]", m.group(1).strip())[0].strip()
        declared = set(re.findall(r"A\d", raw)) if raw != "无" else set()
        registered = set(sk.get("outputs") or [])
        if declared != registered:
            miss.append(f"技能 {sk['id']} 头部声明产物 {sorted(declared) or '无'}，"
                        f"注册表登记 {sorted(registered) or '无'}")
    r.add("C14", "技能头部产物声明与注册表一致", not miss,
          f"{len(skills)} 个技能的头部声明与注册表 outputs 一致", miss)

    # ── C15 每个产物字段都必须有产出方 ─────────────────────────
    # 这一条是这一版最贵的教训。v2.0.1 给 A6/A8 加了 subject/scope/frame_alignment
    # 三个字段来解决「P6 无法证明验证对象就是上线对象」，
    # 但没有任何一个技能或角色说「谁填这三个字段」——
    # 于是 P5 的退出判据永远无法满足，只能判 UNVERIFIED，
    # 而 P6 第一道闸门要求 PASS，**链在 P5→P6 之间断掉**。
    # 声明字段 ≠ 有人产出字段。
    # 只管「出现在某阶段退出判据里的字段」：判据要判它，就一定得有人产出它。
    # 不要求每栏都写「由 X 填」（那只是套话）——改为**真交叉核对**：
    # 这一栏必须在产出方的角色文件、或它拥有的某个技能正文里被明确要求填。
    # v2.0.1 就是在这里断的：subject / scope / frame_alignment 三个字段
    # 出现在 P5 的退出判据里，但全库没有一个文件说谁填它们。
    field_re2 = re.compile(r"\b(A\d+)\.([a-z_]+)")
    gated = set()
    for ph in phases:
        for crit in ph.get("exit_criteria", []):
            gated.update(field_re2.findall(crit))

    def producer_text(producer):
        """产出方「自己说的话」：它的角色文件 + 它拥有的技能的正文。"""
        buf = []
        f = ROOT / "roles" / f"{producer}.md"
        if f.is_file():
            buf.append(f.read_text(encoding="utf-8"))
        for s_ in skills:
            if s_.get("owner_role") == producer:
                sf = ROOT / "skills" / f"{s_['id']}.md"
                if sf.is_file():
                    buf.append(sf.read_text(encoding="utf-8"))
        return "\n".join(buf)

    miss = []
    for aid, fld in sorted(gated):
        a = a_by_id.get(aid)
        if not a or fld not in a.get("fields", []):
            continue                        # C4 负责报未定义字段
        note = (a.get("notes") or {}).get(fld, "")
        who = re.search(r"由\s*`([a-z-]+)`\s*填", note)
        if who:
            if who.group(1) != a.get("producer"):
                miss.append(f"{aid}.{fld} 声明由 `{who.group(1)}` 填，"
                            f"但它的主产出方是 `{a.get('producer')}`")
            continue
        producer = a.get("producer")
        if f"`{fld}`" not in producer_text(producer):
            miss.append(f"{aid}.{fld} 出现在阶段退出判据里，但产出方 `{producer}` "
                        f"的角色文件与它拥有的技能正文里都没出现这一栏——"
                        f"没人被要求填它，判据永远无法满足，链会断")
    r.add("C15", "被判据校验的字段产出方真的会说填", not miss,
          f"{len(gated)} 个被阶段判据校验的字段，产出方正文里都点名列出了", miss)

    # ── C16 每个阶段都必须有「记台账」的判据 ────────────────────
    # A9 是常驻产物，但 v2.0.1 的 P0–P5 没有任何一条判据提到它，
    # 于是台账可以一路空着走到 P6，「全程记录不丢」就是句空话。
    miss = []
    for ph in phases:
        if not any("A9." in c for c in ph.get("exit_criteria", [])):
            miss.append(f"{ph['id']} 的退出判据里没有一道要求记 A9——"
                        f"这一阶段可能悄悄什么都不记就过去了")
    r.add("C16", "每阶段都要求记台账", not miss,
          f"{len(phases)} 个阶段都有 A9 判据", miss)

    # ── C17 阶段判据不得要求一个不在本阶段装配里的角色去做某事 ──
    # P6 曾要求「architect 更新 A3.freshness」，而 architect 不在 P6 的装配里。
    # C13 只认「已更新/已刷新」这几个动词，「已由 architect 指向」它没抓住。
    miss = []
    for ph in phases:
        equipped = set(ph.get("default_roles", []))
        for crit in ph.get("exit_criteria", []):
            for rid, role in r_by_id.items():
                if rid in equipped:
                    continue
                # 「由 X 做的」这种委托式措辞：X 不在装配里就落不了地
                for m in re.finditer(rf"由\s*`?{re.escape(rid)}`?\s*(填|更新|写|记|产出|建|追加|维护)", crit):
                    miss.append(f"{ph['id']} 的判据要求 `{rid}` 做某事，"
                                f"但 `{rid}` 不在它的装配 {sorted(equipped)} 里")
    r.add("C17", "判据里的委托落在装配内", not miss,
          f"{sum(len(p.get('exit_criteria', [])) for p in phases)} 条判据里的角色委托都能落地", miss)

    # ── C18 技能不得依赖它自己产不出、且由更早阶段才产出的产物 ──
    # 判档循环：tier-sizing.inputs 曾经是 [A1]，而 A1 由 P0 产出，
    # 但 P0 开工前就得先判档决定装谁——用结果定前提。
    miss = []
    produces_at = {}
    for ph in phases:
        for aid in ph.get("produces", []):
            produces_at.setdefault(aid, []).append(ph["id"])
    # 只有「第一阶段开工之前就要跑」的技能受这条约束——
    # 判档与冷启动。teach / document-mapping 这类在 P0 之后跑的 driver 技能
    # 依赖 A1/A2 是对的：那时候产物已经在了。
    first_phase = phases[0]["id"] if phases else None
    pre_phase_skills = {s["id"] for s in skills
                        if s.get("owner_role") == "driver"
                        and s.get("phase") is None
                        and s["id"] in ("tier-sizing", "coldstart")}
    for s in skills:
        if s["id"] not in pre_phase_skills:
            continue
        for need in s.get("inputs", []):
            src = produces_at.get(need, [])
            if src:
                miss.append(f"技能 {s['id']} 在 {first_phase} 开工之前就要跑，"
                            f"却依赖 {need}——而 {need} 由 {'/'.join(src)} 产出。"
                            f"用结果定前提，成环")
    r.add("C18", "开工前的技能不依赖开工后才有的产物", not miss,
          f"{len(pre_phase_skills)} 个开工前技能不依赖任何阶段产物", miss)

    # ── 解耦检查 ───────────────────────────────────────────────
    miss = []
    targets = [f for f in (ROOT / n for n in SCAN_FILES) if f.is_file()]
    for d in SCAN_DIRS:
        p = ROOT / d
        if p.is_dir():
            targets += [f for f in sorted(p.rglob("*")) if f.suffix in (".md", ".yaml", ".yml", ".py", ".sh")]
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
