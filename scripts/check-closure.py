#!/usr/bin/env python3
"""
check-closure.py · 闭包检查器（只读，可重复运行）

它回答一个问题：**这套工作流是通的吗？**

「通」被拆成逐条可机械判定的断言。任何一条不成立即非零退出。

  C1 结构        registry 可解析，VERSION 单一来源
  C2 产物闭合    每个产物类型有且仅有一个产出角色；每个产物至少被一个阶段消费
  C3 阶段无孤儿   每个阶段至少一条依赖边（进或出）；所需产物在其之前已产出
  C4 判据可判定   判据里每个 `<X>.<y>` 引用都能解析；A* 字段真实存在
  C5 角色装配件   角色声明的产物/技能/原则都存在；技能与原则反向指认一致
  C6 引用完整     每个技能/原则被至少一个角色或阶段引用（无孤儿）
  C7 上游处置完备 锁文件里每个上游 SKILL.md 在处置表里恰好出现一次
  C9 来源存在     registry.sources 每条都在上游锁文件里；有克隆时另比 sha256/pin
  C10 处置咬合     处置→来源，正向与反向都成立
  C11 消费咬合     消费者→装配，正向与反向都成立
  C12 原创标注     无来源的技能必须显式标 origin: library
  C13 越权写       判据显式声明 write/verify，没有越权
  C14 头部一致     技能头部声明的产物与注册表 outputs 一致
  C15 字段有人填   被判据校验的字段，产出方正文里点名列出了
  C16 台账不断     每阶段都有一道记 A9 的判据
  C18 无前置成环   开工前要跑的技能不依赖开工后才有的产物
  C19 横切带无孤儿 每条横切带被至少一个角色挂载
  C20 来源段一致   技能正文「## 来源」段与 registry.sources 形态与内容一致
  C21 原则来源相等 原则正文「来源：」行反查出的上游 id 与 registry.sources 完全相等
  C22 绑定真实载体 provenance_policy 里的 enforced_by 指向本次运行中注册、且覆盖同一类目的检查
  D1 底座解耦     按**已知名**黑名单扫库内容（黑名单有限枚举，不是穷尽）

它判不了：判据本身是否合理、方法是否有效、下游是否真的照做、黑名单外的别名。
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
#
# 边界为什么不用 `\b`：Python 的 `\b` 只认「词字符 vs 非词字符」，而
#   - 汉字是词字符，所以中文与底座名紧邻时，左边根本没有边界；
#   - `_` 也是词字符，所以下划线连写的 SCREAMING_SNAKE 变量名右边根本没有边界；
#   - 驼峰的右边界同理（`xxxPane` 里的 `xxx` 后面紧跟大写字母，也不是边界）。
# 三者都是真绕过（旧版全漏）。改用显式字符类。**14 条统一两种形状**：
#
#   形状 A（13 条，唯一名称用）：
#       (?<![A-Za-z0-9-])名字(?![-])
#     左边界挡「字母 / 数字 / 连字符」；**右边界只挡连字符**。
#     为什么右边只挡连字符：`cursor-plugins` 是**另一个名字**（上游仓库目录名），
#     全库 50 多个技能的「## 来源」段都写着它，放过去是必须的；
#     而驼峰与下划线写法是**同一个名字**（SCREAMING_SNAKE 环境变量、
#     驼峰面板名），必须抓住，所以右边界不能挡字母和 `_`。
#
#   形状 B（品牌名用，名字只有两个字母，单独处理）：
#       (?<![A-Za-z0-9-])[Pp][Ii](?:[ _-][A-Za-z]|(?![A-Za-z]))
#     分隔符可选会把 `pip` / `pin` / `pip3` 全打进来（`pip` 是包管理器、
#     `pin` 是普通英文词，都不是品牌）。所以要么「分隔符 + 一个字母」，
#     要么「后面根本不是字母、也不是路径分隔符」——中文里「用 某品牌名 写」
#     这种不带分隔符的写法属于后者，仍然抓住；而本库自己的目录名
#     `.pi/injection/` 属于路径分隔符，放过去（否则它会被自己的品牌名规则打中）。
#
# 本文件自己也在扫描范围内，所以这段说明故意不写真实底座名。
#
# 维护者：本库维护者（新增一条 = 你要能说清它保护了哪条真实说法）。
DECOUPLING_PATTERNS = [
    (r"(?<![A-Za-z0-9-])herdr(?![-])", "终端工作区管理器"),
    (r"(?<![A-Za-z0-9-])pi[-_ ]?intercom(?![-])", "会话总线"),
    (r"(?<![A-Za-z0-9-])claude(?![-])", "某编码 agent"),
    (r"(?<![A-Za-z0-9-])codex(?![-])", "某编码 agent"),
    (r"(?<![A-Za-z0-9-])cursor(?![-])", "某编辑器"),
    (r"(?<![A-Za-z0-9-])antigravity(?![-])", "某编辑器"),
    (r"(?<![A-Za-z0-9-])gemini(?![-])", "某模型"),
    (r"(?<![A-Za-z0-9-])openai(?![-])", "某厂商"),
    (r"(?<![A-Za-z0-9-])anthropic(?![-])", "某厂商"),
    (r"(?<![A-Za-z0-9-])opencode(?![-])", "某编码 agent"),
    (r"(?<![A-Za-z0-9-])windsurf(?![-])", "某编辑器"),
    (r"(?<![A-Za-z0-9-])glasp(?![-])", "某应用容器"),
    (r"(?<![A-Za-z0-9-])tmux(?![-])", "某终端复用器"),
    (r"(?<![A-Za-z0-9-])[Pp][Ii](?:[ _-][A-Za-z]|(?![A-Za-z0-9/._-]))", "某品牌名"),
]

# 只扫「库内容」。docs/ 下的 history/ 与 archive/ 记的是「曾经发生过什么」——
# 它们是历史材料与被替换掉的旧载体，不构成对下游的指令，因此**只**豁免这两棵子树。
# docs/ 其余部分（coldstart / artifacts / ledger / downstream-mapping / closure-report）
# 是**当前**契约的下游说明，与 roles/ skills/ 同级，纳入扫描。
# D1 走 rglob，所以这两棵子树里的文件靠 decoupling_exempt() 逐个排除。
SCAN_DIRS = ("workflow", "roles", "skills", "principles", "scripts", "docs")
SCAN_FILES = ("README.md", "AGENTS.md", "VERSION")

# D1 豁免的子树（相对 ROOT）。只豁免这两棵，其余 docs 一律进扫描。
SCAN_EXEMPT_SUBTREES = ("docs/history", "docs/archive")


def decoupling_exempt(rel) -> bool:
    """rel 是相对 ROOT 的路径或纯相对 Path。True = 该文件在 D1 豁免范围内。"""
    parts = tuple(rel.parts) if hasattr(rel, "parts") else tuple(rel.split("/"))
    for x in SCAN_EXEMPT_SUBTREES:
        head = tuple(x.split("/"))
        if parts[:len(head)] == head:
            return True
    return False


def decoupling_pattern_lines():
    """DECOUPLING_PATTERNS 字面量在**本文件**里占的行号集合（1-based）。

    D1 扫库内容时会把本文件也扫进去，所以黑名单自己那几行必须排除。
    排除范围精确到这几行——不是整个文件。v2.0.5 之前是
    `if f.name == "check-closure.py": continue`，把整个检查器从 D1 里摘了出去，
    于是往本文件里写一个真实底座名也不会红。
    """
    try:
        lines = Path(__file__).read_text(encoding="utf-8").splitlines()
    except OSError:
        return set()
    start = next((i for i, l in enumerate(lines)
                  if l.startswith("DECOUPLING_PATTERNS")), None)
    if start is None:
        return set()
    out = set()
    for i in range(start, len(lines)):
        out.add(i + 1)
        if lines[i].rstrip() == "]":
            break
    return out

# 上游仓库目录名 -> 处置表里的前缀
UPSTREAM_PREFIX = {
    "cursor-plugins": "pstack",
    "mattpocock-skills": "matt",
    "addyosmani-agent-skills": "addy",
}
SKIP_DIRS = {"node_modules", "deprecated", "in-progress", "templates", "assets",
             "references", ".git", "automations", "third_party", "docs", "agents",
             "commands", "evals", "hooks", "schemas", "scripts"}


# 每个检查项声明的**实际受检载体**（类目, 锚点）。这是给 C22 用的：
# provenance_policy 里写 `enforced_by: C20` 不能只证明「有个叫 C20 的检查
# 存在」——「指向存在」不等于「覆盖」。检查项自己在这里声明它核的是哪一类
# 文件的哪一段，C22 再核这份声明与 policy 的类目对不对得上。
# 维护者：新增 enforced_by 绑定前先在这里登记；登记意味着你确认这条检查真的
# 读那类文件的那个锚点。变更检查实现时同步改这里，并重跑 C22 的反例。
CHECK_COVERS = {
    "C20": ("skills", "## 来源"),
    "C21": ("principles", "来源："),
}


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
    # 无本库自己的 git 元数据时 tag 核对无从进行。三种真实形状：
    #   - `git archive` 导出（整棵树没有 .git）
    #   - 装进下游仓库的副本（**外层**有 .git，但那是下游仓库的 HEAD 与 tag，
    #     与本库的 VERSION 无关）
    #   - 裸目录
    # 都是环境故障，按本库硬边界 3 判 UNVERIFIED（渲染为 SKIP）：既不冒充
    # PASS，也不判成产品缺陷。旧版只看 `rev-parse --git-dir` 是否成功，于是把
    # 「副本装在下游仓库里」判成「当前 commit 上没有 tag」——用一句假话把
    # 「没查」说成「查出来是坏的」。判据改为「git 顶层必须是 ROOT 自己」：
    # 只有本库的仓库才有权回答「这个 commit 上有没有 release tag」。
    probe = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                           capture_output=True, text=True, cwd=str(ROOT))
    top = probe.stdout.strip()
    git_meta = bool(probe.returncode == 0 and top
                    and Path(top).resolve() == ROOT.resolve())
    tag_checked = git_meta
    if git_meta:
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
    c1_detail = (f"版本 {vfile}，产物 {len(artifacts)}／阶段 {len(phases)}／角色 {len(roles)}"
                 f"／原则 {len(principles)}／技能 {len(skills)}")
    if not tag_checked:
        c1_detail += ("；无本库自己的 git 元数据（如 `git archive` 导出，"
                      "或副本装在下游仓库里），未核对 VERSION 与 release tag 的对齐"
                      "——按三态判 UNVERIFIED，不判 FAIL。"
                      "本库的 release 身份只能由本库自己的仓库或外层发布流程保证；"
                      "本树内不可判")
    r.add("C1", "结构与版本单一来源", not miss, c1_detail, miss,
          skip=(not tag_checked and not miss))

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

    # 孤儿阶段：一个阶段必须有**至少一条**依赖边——要么它要东西（进边），
    # 要么它产的东西被别人要（出边）。两头都没有的阶段，谁也不等它、它也不等谁，
    # 它可以被整条流程绕过去还不动任何东西。这是 C3 一直缺的断言：
    # 「按序可达」只查了「所需产物在上游已产出」，一个 required_inputs 为空、
    # produces 也为空的阶段完美地通过了那条断言。
    # 入口阶段（P0）天生没有进边，豁免；它必须有出边。
    consumers_of_artifact = {}
    for a in artifacts:
        for c in a.get("consumers", []):
            consumers_of_artifact.setdefault(c, set()).add(a["id"])
    orphan = []
    for i, ph in enumerate(phases):
        pid = ph["id"]
        inbound = bool(ph.get("required_inputs"))
        outbound = set()
        for out in ph.get("produces", []):
            for q in a_by_id.get(out, {}).get("consumers", []) or []:
                if q != pid:
                    outbound.add(q)
        if not inbound and not outbound:
            orphan.append(f"{pid}（required_inputs 为空，也没有下游阶段消费它产的东西）")
        elif i == 0 and not outbound:
            orphan.append(f"{pid} 是入口阶段，却没有任何下游阶段消费它产的东西")
    miss += [f"孤儿阶段：{x}——没有人等它，它也不产出任何人等的东西，"
             f"可以绕开整条流程而不动任何东西" for x in orphan]
    r.add("C3", "阶段可达、依赖闭合且无孤儿", not miss,
          f"{len(phases)} 个阶段按序可达、所需产物在上游已产出，"
          f"{len(phases) - len(orphan)}/{len(phases)} 个阶段至少有一条依赖边（无孤儿）", miss)

    # ── C4 退出判据引用的东西全部可解析 ────────────────────────
    # 字段名允许大写：旧正则 `[a-z_]+` 让 `A6.GHOST` 整条不匹配，
    # 同句里只要另有一个真字段（`A6.runnable`）就能滑过去。大写字段名同样是
    # 字段名，「小写」不是任何一条纪律的一部分。
    field_re = re.compile(r"\b(A\d+)\.([A-Za-z_][A-Za-z0-9_]*)")
    # 判据里任何 `<X>.<y>` 形状的引用，X 必须在已知 id 集合里。
    # 旧版只认 `A\d+.小写`，于是 `A6.GHOST` 这种大写伪字段根本不进正则，
    # 同句里只要另有一个真字段（`A6.runnable`）就能整句滑过去。
    # 判据不可判定 = 判据说了假话，必须报。
    ref_re = re.compile(r"\b([A-Za-z][A-Za-z0-9_-]{0,40})\.([A-Za-z_][A-Za-z0-9_]{0,40})\b")
    known_ids = (set(a_by_id) | set(p_by_id) | set(r_by_id) | set(pr_by_id)
                 | set(s_by_id) | {x["id"] for x in ribbons}
                 | {x["zh"] for x in roles if x.get("zh")})
    unresolvable = 0
    miss = []
    for ph in phases:
        for crit in ph.get("exit_criteria", []):
            for x, y in ref_re.findall(crit):
                if x not in known_ids:
                    unresolvable += 1
                    miss.append(f"{ph['id']} 判据里的 `{x}.{y}` 无法解析："
                                f"{x} 不是任何已定义的产物/阶段/角色/技能/原则/横切带 id"
                                f"——判据指向了一个不存在的东西，不可判定")
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
            # 用正则抽取字段名，不用 x.split(".")[0]——判据现在带 write:/verify: 前缀，
            # 整句首段是 "verify: A1" 而不是 "A1"，那种写法会永远比不上
            if not any(a["id"] in [m[0] for m in field_re.findall(x)]
                       for x in ph.get("exit_criteria", [])):
                miss.append(f"{a['id']} 由 {ph['id']} 产出，但 {ph['id']} 的退出判据里"
                            f"没有校验它——下游会拿到一份没被验证过的产物")
    r.add("C4", "判据可判定（引用全部可解析）", not miss,
          f"{sum(len(p.get('exit_criteria', [])) for p in phases)} 条退出判据，"
          f"{unresolvable} 处无法解析的引用，全部 A*.field 都指向真实字段", miss)

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
            # `into` 是**列表**。旧 schema 里它是标量，于是「一个上游同时被
            # 吸收进两处」这件事根本无处记录——而真实情况就是这样（7 条）。
            # 列表化之后，“一个上游一条处置”不变（C7 仍要求恰好一次），
            # 变的是一条处置可以指向多个目标。
            into = d.get("into")
            if d.get("outcome") == "absorbed":
                if not isinstance(into, list):
                    miss.append(f"{d['upstream']} 判为 absorbed，但 into 不是列表："
                                f"{into!r}（schema 要求 into: [目标, ...]）")
                elif not into:
                    miss.append(f"{d['upstream']} 判为 absorbed 但 into 是空列表"
                                f"——它到底被吸收进了哪里")
                else:
                    for t in into:
                        if t not in known:
                            miss.append(f"{d['upstream']} 指向 {t}，"
                                        f"但注册表里没有这个技能或原则")
            elif into:
                miss.append(f"{d['upstream']} 判为 {d.get('outcome')}，"
                            f"却仍指向 {into}——只有 absorbed 才能有目标")
    r.add("C7", "上游处置完备（对锁文件）", not miss,
          f"锁文件 {len(lock_skills)} 个上游 skill，处置表 {len(listed)} 条，一一对应", miss)

    # ── C9 来源声明与锁文件一致（有实物时校验内容）────────────
    # 名字必须说清能力边界：无 upstreams/ 时只核锁文件，**不做实物对照**，
    # 输出要自曝这一点，不把它说成「已核」。旧版在缺 .git 时跳过 pin 比对，
    # 却照样写「并已逐条比对 sha256 与 pin」——把「没核」说成「核过了」。
    miss = []
    for coll, kind in ((skills, "skill"), (principles, "principle")):
        for item in coll:
            for src in item.get("sources") or []:
                if src not in lock_skills:
                    miss.append(f"{kind} {item['id']} 的来源 {src} 不在上游锁文件里")
    has_upstreams = (ROOT / "upstreams").is_dir()
    pin_unchecked = []          # pin 没核的原因（缺 .git 元数据等）
    repos_n = 0
    if lock_skills and has_upstreams:
        # 锁与实物对照：逐条比 sha256；有 git 元数据的仓另比 pin
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
        repos = lock.get("repos") or {}
        repos_n = len(repos)
        if not repos:
            pin_unchecked.append("锁文件未登记 repos")
        for pre, meta in repos.items():
            d = ROOT / meta["path"]
            # 不能只看 `d/.git` 存在与否：pstack 是 cursor-plugins 仓库的子目录，
            # 它自己没有 .git，但 git 元数据经父仓可达。也不能只信 rev-parse：
            # 把 pstack 单独拷进另一个 git 检出时，rev-parse 会找到**外层**仓库，
            # 把外层 HEAD 当上游 pin（B4 控制台实测过这个假 FAIL）。
            # 判据：解析出的仓库顶层必须落在 upstreams/ 内，才是上游自己的元数据。
            probe = subprocess.run(["git", "-C", str(d), "rev-parse", "--show-toplevel"],
                                   capture_output=True, text=True)
            top = probe.stdout.strip()
            up_root = (ROOT / "upstreams").resolve()
            top_s, up_s = str(Path(top).resolve()) if top else "", str(up_root)
            if probe.returncode != 0 or not (
                    top_s == up_s or top_s.startswith(up_s + os.sep)):
                pin_unchecked.append(f"上游 {pre} 没有可信的 git 元数据"
                                     f"（该路径上没有属于 upstreams/ 的仓库）")
                continue
            head = subprocess.run(["git", "-C", str(d), "rev-parse", "HEAD"],
                                  capture_output=True, text=True).stdout.strip()
            if head != meta["commit"]:
                miss.append(f"上游 {pre} 的 pin 漂移：锁文件记 {meta['commit'][:7]}，"
                            f"克隆在 {head[:7]}")
    if miss:
        # 有真实不一致时 FAIL 优先，SKIP 不得替它掩盖
        detail = (f"{len(lock_skills)} 个上游 skill 索引（锁文件）；"
                  f"发现 {len(miss)} 条不一致（明细见下）")
        r.add("C9", "来源声明与锁文件一致（有实物时校验内容）", False, detail, miss)
    elif not has_upstreams:
        detail = (f"{len(lock_skills)} 个上游 skill 索引（锁文件），0 条失效来源。"
                  f"PASS（锁文件核对）：registry.sources 均在随包 upstreams.lock.yaml；"
                  f"未发现 upstreams/，未做上游实物 sha256/pin 对照；"
                  f"不证明锁文件与真实上游一致。")
        r.add("C9", "来源声明与锁文件一致（有实物时校验内容）", True, detail)
    elif pin_unchecked:
        detail = (f"{len(lock_skills)} 个上游 skill 索引（锁文件），0 条失效来源；"
                  f"upstreams/ 存在，sha256 已比对；未核 pin：{'；'.join(pin_unchecked)}"
                  f"——实物核对不完整，按三态判 UNVERIFIED（SKIP），不判成产品缺陷。")
        r.add("C9", "来源声明与锁文件一致（有实物时校验内容）", True, detail, None,
              skip=True)
    else:
        detail = (f"{len(lock_skills)} 个上游 skill 索引（锁文件），0 条失效来源。"
                  f"PASS（锁文件＋实物核对）：来源在锁文件中；上游文件 sha256 与 "
                  f"{repos_n} 仓 pin 均与锁文件一致。")
        r.add("C9", "来源声明与锁文件一致（有实物时校验内容）", True, detail)

    # ── C10 处置表声称吸收，目标就必须真的列了它（双向）────────
    # 这一条曾经缺失：6 条 absorbed 处置在 upstreams/ 里对得上，
    # 但目标技能的 sources 里根本没有它——台账在追一个没发生的事。
    miss = []
    claim = {}          # upstream -> set(into)
    for d in disp:
        if d.get("outcome") == "absorbed":
            for into in d.get("into") or []:
                claim.setdefault(d["upstream"], set()).add(into)
    for d in disp:
        if d.get("outcome") != "absorbed":
            if d.get("into"):
                miss.append(f"{d['upstream']} 判为 {d['outcome']}，却仍指向 {d['into']}")
            continue
        if not d.get("into"):
            miss.append(f"{d['upstream']} 判为 absorbed 却没有指向任何技能或原则")
            continue
        # 正向：into 里的**每一个**目标，sources 里都必须有它
        for into in d["into"]:
            tgt = s_by_id.get(into) or pr_by_id.get(into)
            if not tgt:
                miss.append(f"{d['upstream']} 指向不存在的 {into}")
            elif d["upstream"] not in (tgt.get("sources") or []):
                miss.append(f"假链接：{d['upstream']} 声称吸收进 {into}，"
                            f"但 {into} 的 sources 里没有它")
    # 反向：某目标的 sources 里出现过的上游，必须有一条 absorbed 处置的
    # into 列表**包含该目标**。旧版只查正向，反向不查的后果是：同一个上游
    # 可以被第二个技能白认领——它确实来自那里，但「读没读正文」「处置理由」
    # 这些只写了一份，另一份白拿。
    for coll, kind in ((skills, "技能"), (principles, "原则")):
        for item in coll:
            for src in item.get("sources") or []:
                if item["id"] not in claim.get(src, set()):
                    owner = sorted(claim.get(src, set())) or ["无"]
                    miss.append(f"反向假链接：{kind} {item['id']} 的 sources 里有 {src}，"
                                f"但处置表里 {src} 的 absorbed 指向 {owner}"
                                f"——认领了来源却没在台账里登记")
    r.add("C10", "处置与来源双向咬合", not miss,
          f"{len(disp)} 条处置与目标 sources 双向一致"
          f"（正向：into 里的每个目标都得列它；反向：sources 里的每个上游"
          f"都得有指向该目标的 absorbed 处置）", miss)

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
    # ── 反向：阶段要的东西，产物必须声明这个阶段在消费 ──
    # 旧版只查 consumers→装配。反向不查的后果：阶段照样把 A6 列进 required_inputs，
    # 但 A6.consumers 里没有它——台账与装配各说各话，而正向检查一条都不报。
    # 「自己产自己又要」（同阶段自产自消）在本库不存在，保留对称豁免以免把
    # 「产出方当场自验」这种合法形态判红；真出现时 C4 仍会要求它校验该字段。
    for ph in phases:
        for need in ph.get("required_inputs", []) or []:
            a = a_by_id.get(need)
            if not a:
                continue                       # C3 负责报未定义产物
            if need in (ph.get("produces") or []):
                continue
            if ph["id"] not in (a.get("consumers") or []):
                miss.append(f"{ph['id']} 开工需要 {need}，但 {need}.consumers "
                            f"{a.get('consumers')} 里没有 {ph['id']}"
                            f"——阶段要它，产物却没登记谁消费它")
    r.add("C11", "消费声明与装配双向咬合", not miss,
          f"{sum(len(a.get('consumers', [])) for a in artifacts)} 条消费声明全部被阶段接住，"
          f"且每个阶段的 required_inputs 都在对应产物的 consumers 里", miss)

    # ── C12 sources 为空的必须显式标 origin: library ───────────
    miss = []
    for s_ in skills:
        if not s_.get("sources") and s_.get("origin") != "library":
            miss.append(f"技能 {s_['id']} 没有来源也没标 origin: library"
                        f"——读者无法分辨它是「上游没有对应物」还是「忘了写来源」")
    r.add("C12", "无吸收来源技能显式标注", not miss,
          f"{sum(1 for x in skills if x.get('origin') == 'library')} 个技能没有吸收来源"
          f"（registry.sources 为空）并标了 origin: library；该计数与 C20 的非吸收"
          f"形态数（借鉴＋纯原创）对账，两者由交叉断言保证相等", miss)

    # ── C13 越权写：判据逐条声明 write / verify，不靠猜中文动词 ──
    # 上一版这里有一个受控动词表（已更新/已刷新/已保鲜/…）。二审给了两个反例：
    #   绕过：把措辞换成「已修订」「重建完成」就不报了；
    #   误报：「A8.frame_alignment 已写入，且 A3.freshness 与该记录一致」只是在
    #        **验证** A3，却因为同句出现「已写入」被判成越权写。
    # 靠措辞猜权限，永远既能绕又会误报。改成**显式声明**：每条判据以
    # `write:` 或 `verify:` 开头，声明它到底要什么。措辞不再参与判定。
    miss = []
    for ph in phases:
        own = set(ph.get("produces", []))
        equipped = set(ph.get("default_roles", []))
        for crit in ph.get("exit_criteria", []):
            if not isinstance(crit, str) or not (crit.startswith("write: ") or
                                                 crit.startswith("verify: ")):
                miss.append(f"{ph['id']} 有一条判据没声明动作：{str(crit)[:50]}"
                            f"——必须以 `write: ` 或 `verify: ` 开头，措辞不参与判定")
                continue
            if not crit.startswith("write: "):
                continue
            for aid in re.findall(r"\b(A\d+)\.", crit):
                if aid in own:
                    continue
                prod = a_by_id.get(aid, {}).get("producer")
                miss.append(f"{ph['id']} 声明要写 {aid}，但它不由本阶段产出"
                            f"（主产出方 `{prod}`，本阶段产出 {sorted(own)}）"
                            f"——越权写。验证偏差请写进本阶段自己产出的证据字段")
            for rid in r_by_id:
                if rid in equipped:
                    continue
                if re.search(rf"由\s*`?{re.escape(rid)}`?\s*(填|更新|写|记|产出|建|追加|维护)", crit):
                    miss.append(f"{ph['id']} 的判据要求 `{rid}` 做某事，"
                                f"但 `{rid}` 不在它的装配 {sorted(equipped)} 里")
    r.add("C13", "越权写由显式声明判定", not miss,
          f"{sum(len(p.get('exit_criteria', [])) for p in phases)} 条判据全部显式声明了 "
          f"write/verify，没有越权。"
          f"边界：仅核阶段退出判据的 write:/verify: 显式声明；不读取角色正文，"
          f"正文与 registry 的写权冲突须人审。", miss)

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
        declared = set(re.findall(r"\bA\d+\b", raw)) if raw != "无" else set()  # \b：否则 A404 会被读成 A4，报错信息会骗下一个人
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
    field_re2 = re.compile(r"\b(A\d+)\.([A-Za-z_][A-Za-z0-9_]*)")
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
        producer = a.get("producer")
        taught = f"`{fld}`" in producer_text(producer)
        # 「声明的责任人」与「实际的产出合同」**两者都必须成立**。
        # 旧版在这里有个短路：notes 写了「由 `X` 填」就 continue，正文到底教没教
        # 没人管。于是在 notes 里写一句「由 `builder` 填」就是一张免死金牌——
        # 角色正文与技能正文一个字不提这个字段，判据照样永远无法满足。
        # 声明只是声明；只有产出方的合同里真的教了填法，链才接得上。
        who = re.search(r"由\s*`([a-z-]+)`\s*填", note)
        if who and who.group(1) != producer:
            miss.append(f"{aid}.{fld} 声明由 `{who.group(1)}` 填，"
                        f"但它的主产出方是 `{producer}`")
        if not taught:
            miss.append(f"{aid}.{fld} 出现在阶段退出判据里，但产出方 `{producer}` "
                        f"的角色文件与它拥有的技能正文里都没出现这一栏"
                        + ("（notes 已经声明了填人，但光声明不算教过）"
                           if who else "")
                        + "——没人被要求填它，判据永远无法满足，链会断")
    # 「哪些字段没被任何判据门控」必须自动推导并展示（oracle 裁决 Q2）。
    # 推导源只有两处：registry 的 artifacts[].fields 全集，与上面从
    # exit_criteria 反查出来的 gated；差集就是未门控清单。
    # **不判成缺陷、不影响退出码**：字段可以有价值而不是退出门槛。
    # **不许手维护第二份名单**——手写的必然漂移，那本身就是「声明了但没人
    # 产出」的变体，所以这里每次运行时现算，随注册表增删自动变长变短。
    # 消费者与时刻：维护者改 registry 的 fields 或某阶段判据时，对照同一行
    # 输出看增减（尤其确认「刚拆掉的门」确实出现在这里）；审查者审计哪些
    # 声明字段目前只是装饰。放在 C15 的 detail 里，不另立检查项——一条
    # 永远不可能失败的检查就是一条假检查。
    all_fields = {(a["id"], fld) for a in artifacts for fld in (a.get("fields") or [])}
    ungated = sorted(f"{aid}.{fld}" for aid, fld in all_fields - gated)
    r.add("C15", "被判据校验的字段：声明的人与产出合同都成立", not miss,
          f"{len(gated)} 个被阶段判据校验的字段，"
          f"声明的责任人与产出方正文里的填法两两对齐。"
          f"边界：taught 只验字段名在产出方（角色文件 + 它拥有的技能正文）里出现，"
          f"不验是否在教——把真实教学删掉、只留一句语义无关提及的情形抓不到，"
          f"属语义、由人审。"
          f"边界：不保证字段名在角色文件与技能文件之间逐字一致——某一份改名、"
          f"另一份仍列着（role-contract-drift）不算缺陷。"
          f"未门控字段 {len(ungated)} 个（不是缺陷：字段可以有价值而不是退出门槛）："
          + (", ".join(ungated) if ungated else "无"), miss)

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

    # ── C19 横切带无孤儿 ───────────────────────────────────────
    # C6 查孤儿技能与孤儿原则，漏了横切带。v2.0.5 的反例：一条 always:false
    # 的横切带挂在一个不参与任何阶段的角色身上，于是它既不常驻、适用范围
    # 也无人经过，而 S7 只看“携带它的角色参与了哪些阶段”，一条都不报。
    # 编号用 C19：它属于 C6 的孤儿家族，但不开在 C6 里——两条断言的
    # 保护对象不同（一个说技能/原则，一个说横切带），合在一起会让失败原因
    # 看不出是哪一类对象出的问题。C17 在 v2.0.2 收敛时退役，编号空洞有历史
    # 原因，不复用。
    miss = []
    worn = {rb_id for role in roles for rb_id in role.get("ribbons", [])}
    rb_ids = {x["id"] for x in ribbons}
    for rb in ribbons:
        rid = rb["id"]
        if rid not in worn:
            miss.append(f"横切带 {rid} 没有任何角色挂载——孤儿。"
                        f"没人装配它，它宣称的纪律就不会生效")
        bad = [s for s in rb.get("skills", []) if s not in s_by_id]
        if bad:
            miss.append(f"横切带 {rid} 引用不存在的技能 {bad}")
    for role in roles:
        for rb_id in role.get("ribbons", []):
            if rb_id not in rb_ids:
                miss.append(f"角色 {role['id']} 挂载了未定义的横切带 {rb_id}")
    r.add("C19", "横切带无孤儿", not miss,
          f"{len(ribbons)} 条横切带全部被至少一个角色挂载，携带的技能与挂载引用全部可解析", miss)

    # ── C20 技能正文的「## 来源」段与注册表一致 ─────────────────
    # C9 只核 registry.sources 里的每条 id 都在锁文件里，**不核技能文件自己
    # 写了什么**。v2.0.5 的已知漏洞：50 个技能正文的来源段是散文，纯人读；
    # 在那里多列一个 registry 没有的上游，全库全绿。
    #
    # 来源段只有三种形态，**互斥**，混用即 FAIL：
    #   (a) 吸收  逐行列出 `upstreams/<repo>/<path>/SKILL.md`。
    #           → registry.sources 非空，且逐条双向相等（不多不少）。
    #   (b) 借鉴  散文写「本库原创。参考了 `upstreams/...` 的……思路」，未复制其实现。
    #           → registry.sources 为空且 origin: library。提到了路径的，
    #             每条路径仍必须在锁文件里（不许引用不存在的上游）。
    #   (c) 原创  只写「本库原创。」，不提到任何上游路径。
    #           → registry.sources 为空且 origin: library。
    # 写 (a) 又写「本库原创」= 混用；写了 (a) 却没登记 sources = 假链接。
    # 维护者：本库维护者。改来源时同改两处，并重新确认形态。
    UP_PATH_RE = re.compile(r"upstreams/[A-Za-z0-9_./-]+/SKILL\.md")
    BARE_PATH_RE = re.compile(r"^upstreams/[A-Za-z0-9_./-]+/SKILL\.md$")
    path2id = {v.get("path"): k for k, v in lock_skills.items() if v.get("path")}
    shapes = {"absorbed": 0, "borrowed": 0, "original": 0}
    miss = []
    for sk in skills:
        sid = sk["id"]
        f = ROOT / "skills" / f"{sid}.md"
        if not f.is_file():
            continue                              # S1 负责报缺文件
        m = re.search(r"^##\s+来源\s*$", f.read_text(encoding="utf-8"), re.M)
        if not m:
            miss.append(f"技能 {sid} 正文没有「## 来源」段——三类形态都判不了，"
                        f"读者无法分辨它是吸收、借鉴还是原创")
            continue
        rest = f.read_text(encoding="utf-8")[m.end():]
        nxt = re.search(r"^##\s+", rest, re.M)
        sec = rest[:nxt.start()] if nxt else rest
        claimed_original = "本库原创" in sec
        listed = [l.strip().lstrip("-*").strip().strip("`").strip()
                  for l in sec.splitlines() if l.strip()]
        bare = [x for x in listed if BARE_PATH_RE.match(x)]
        shape = ("borrowed" if claimed_original and UP_PATH_RE.search(sec)
                 else "original" if claimed_original
                 else "absorbed" if bare else None)
        if shape is None:
            miss.append(f"技能 {sid} 的来源段既没逐条列路径，也没声明「本库原创」"
                        f"——不属于三类形态中的任何一类")
            continue
        if shape == "absorbed" and claimed_original:
            miss.append(f"技能 {sid} 的来源段混用形态：既逐条列了 {len(bare)} 条上游路径，"
                        f"又声称「本库原创」——两者互斥，只能选一个")
            continue
        shapes[shape] += 1
        # 交叉断言：正文形态与 registry.origin 必须说的是同一件事。
        # C12 只管「sources 为空 → origin: library」；这一条补上反向——
        # 吸收形态的技能不得标 origin: library。缺了它，round-3 §6.5 那类
        # 「C12 说 3 个原创、C20 说 0 个原创／3 个借鉴」的对不上账会全绿。
        if shape == "absorbed" and sk.get("origin") == "library":
            miss.append(f"技能 {sid} 的来源段是吸收形态（逐条列了 {len(bare)} 条上游路径），"
                        f"但 registry 标了 origin: library——正文说吸收、注册表说库内，"
                        f"两个标签必须指向同一件事（与 C12 对账）")
        for p in set(UP_PATH_RE.findall(sec)):
            if p not in path2id:
                miss.append(f"技能 {sid} 的来源段提到 {p}，但它不在上游锁文件里"
                            f"——引用了一个不存在（或未登记）的上游")
        srcs = set(sk.get("sources") or [])
        if shape == "absorbed":
            got = {path2id.get(x) for x in bare}
            unknown = sorted(x for x in got if x is None)
            if unknown:
                miss.append(f"技能 {sid} 的来源段列了 {len(unknown)} 条锁文件里没有的路径")
            if got != srcs:
                only_file = sorted(x for x in got - srcs if x)
                only_reg = sorted(srcs - got)
                miss.append(f"技能 {sid} 的来源段与注册表不一致："
                            f"只在正文里 {only_file or '无'}，只在注册表里 {only_reg or '无'}")
        else:
            if srcs:
                miss.append(f"技能 {sid} 正文声明「本库原创」"
                            f"（{shape} 形态），但 registry.sources 非空 {sorted(srcs)}"
                            f"——一边说原创一边挂着上游")
            if sk.get("origin") != "library":
                miss.append(f"技能 {sid} 是{shape}形态（无吸收来源），"
                            f"但 registry 没标 origin: library（C12 的要求）")
    r.add("C20", "技能来源段与注册表形态一致", not miss,
          f"{shapes['absorbed']} 个吸收／{shapes['borrowed']} 个借鉴／"
          f"{shapes['original']} 个纯原创（形态 original）；其中 "
          f"{shapes['borrowed'] + shapes['original']} 个标 origin: library，"
          f"与 C12 的计数对账（交叉断言：吸收形态不得标 origin: library）", miss)

    # ── C21 原则来源与注册表完全相等 ───────────────────────────
    # provenance_policy 承诺 principles 的覆盖载体是「每条 `## p-*` 段内的
    # `来源：` 行」，但此前没有任何检查器读它（round-3 的 C1/C2 注入双绿）。
    # C21 把承诺变成断言：正文里反查出来的上游 id 集合必须与 registry.sources
    # **完全相等**——拒幽灵路径、拒缺失、拒串线、拒重复。
    # 形态分三支：有路径 + 「本库原创」= 借鉴；有路径不声明原创 = 吸收；
    # 无路径 + 声明原创 = original，必须给内部锚点。未来合法的多来源按集合比。
    miss = []
    pr_sections = {}          # pid -> (file, 该段落正文)
    for f in sorted((ROOT / "principles").glob("*.md")):
        text = f.read_text(encoding="utf-8")
        heads = list(re.finditer(r"^##\s+(p-[a-z0-9-]+)\s*$", text, re.M))
        for i, m in enumerate(heads):
            end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
            pr_sections[m.group(1)] = (f, text[m.end():end])
    for pid in sorted(set(pr_by_id) - set(pr_sections)):
        miss.append(f"原则 {pid} 在 registry 里，但 principles/ 里没有对应的 `## {pid}` 段落")
    for pid in sorted(set(pr_sections) - set(pr_by_id)):
        miss.append(f"principles/ 里的 `## {pid}` 不在 registry 里——孤段")
    path2id_pr = {v.get("path"): k for k, v in lock_skills.items() if v.get("path")}
    PR_PATH_RE = re.compile(r"upstreams/[A-Za-z0-9_./-]+/SKILL\.md")
    for pid in sorted(set(pr_sections) & set(pr_by_id)):
        f, sec = pr_sections[pid]
        rel = f.relative_to(ROOT)
        src_lines = re.findall(r"^来源：(.+)$", sec, re.M)
        paths = [p for line in src_lines for p in PR_PATH_RE.findall(line)]
        claimed_original = "本库原创" in sec
        declared = set(pr_by_id[pid].get("sources") or [])
        if not src_lines:
            miss.append(f"{rel} 的 {pid} 没有「来源：」行——来源无处可核")
            continue
        if len(paths) != len(set(paths)):
            miss.append(f"{rel} 的 {pid} 的来源有重复路径——同一个上游列了两遍")
        got = set()
        for p in paths:
            uid = path2id_pr.get(p)
            if uid is None:
                miss.append(f"{rel} 的 {pid} 的来源 {p} 不在上游锁文件里——幽灵路径")
            else:
                got.add(uid)
        if not paths and claimed_original:
            # 完全原创分支：显式声明 original，且必须给内部锚点
            if declared:
                miss.append(f"{rel} 的 {pid} 声明「本库原创」，但 registry.sources 非空 "
                            f"{sorted(declared)}——一边说原创一边挂着上游")
            if not re.search(r"A\d+|`@[a-zA-Z0-9-]+`|\]\([^)]+\)|p-[a-z0-9-]+", sec):
                miss.append(f"{rel} 的 {pid} 声明「本库原创」但正文里找不到内部锚点"
                            f"（契约 A*、技能 @id、相对链接或原则 p-*）——原创必须有内部出处")
        elif not paths:
            miss.append(f"{rel} 的 {pid} 的来源行里没有任何上游路径，也没声明「本库原创」"
                        f"——不属于三类形态中的任何一类")
        elif got != declared:
            only_file = sorted(got - declared)
            only_reg = sorted(declared - got)
            miss.append(f"{rel} 的 {pid} 的来源与 registry.sources 不一致："
                        f"只在正文里 {only_file or '无'}，只在注册表里 {only_reg or '无'}"
                        f"——串线、缺失或多列都算")
    r.add("C21", "原则来源与注册表完全相等", not miss,
          f"{len(pr_sections)} 条原则的「来源：」行反查出的上游 id 与 registry.sources "
          f"逐条相等（拒幽灵路径、缺失、串线、重复）。"
          f"边界：只证锚点存在且与注册表一致，不证段落语义忠实——"
          f"「这条原则的正文真的来自那段上游」不可机械核验，由人审。", miss)

    # ── 解耦检查 D1 ──────────────────────────────────────────
    # 名字里的「已知底座名黑名单」是承诺的一部分：这张表是**人工枚举**的，
    # 不是穷尽清单。详情见 DECOUPLING_PATTERNS 上面的边界说明。
    miss = []
    targets = [f for f in (ROOT / n for n in SCAN_FILES) if f.is_file()]
    for d in SCAN_DIRS:
        p = ROOT / d
        if p.is_dir() and not decoupling_exempt(d):
            targets += [f for f in sorted(p.rglob("*"))
                        if f.suffix in (".md", ".yaml", ".yml", ".py", ".sh")
                        and f.is_file()
                        and not decoupling_exempt(f.relative_to(ROOT))]
    self_lines = decoupling_pattern_lines()
    for f in targets:
        try:
            text = f.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        lines = text.splitlines()
        for pat, label in DECOUPLING_PATTERNS:
            # 大小写不敏感：把底座名写成全大写说的是同一件事，
            # 靠大小写差异绕过一条底座禁令没有任何语义价值。
            # 本行故意不点名任何具体底座——本文件也在 D1 的扫描范围内，
            # 写进来就会把自己判红（v2.0.5 之前整个文件被 skip，那种做法
            # 恰好让「往检查器里写底座名」永远不会红）。
            for m in re.finditer(pat, text, re.I):
                line = text[:m.start()].count("\n") + 1
                # 只排除黑名单字面量那几行（精确到行号），不是整个文件
                if f == Path(__file__).resolve() and line in self_lines:
                    continue
                ctx = lines[line - 1].strip()[:90]
                miss.append(f"{f.relative_to(ROOT)}:{line} 出现具体底座（{label}）→ {ctx}")
    r.add("D1", "底座解耦（已知名黑名单·大小写不敏感）", not miss,
          f"扫描 {len(targets)} 个库内容文件（含 docs/，只豁免 history/ 与 archive/），"
          f"0 处命中已知底座名。边界：黑名单是人工枚举的 {len(DECOUPLING_PATTERNS)} 条"
          f"已知名称，不是穷尽清单——别名、缩写、厂商代号抓不到", miss)

    # ── C22 来源政策的 enforced_by 绑定真实载体 ───────────────
    # 这是「检查检查器」的元检查。`provenance_policy.current[*].enforced_by`
    # 如果只证明「检查项存在」，那它就只是一张字符串指派表——「指向存在」
    # 不等于「覆盖」。所以每个检查项在 CHECK_COVERS 里声明它实际核的载体
    # 类目，C22 核四件事：
    #   1. enforced_by 指到的检查项真的在本次运行中注册；
    #   2. 该检查声明的载体类目与 policy 里那一条的类目一致；
    #   3. 状态本身合规：enforced 必须有可核粒度；UNVERIFIED 必须带 owner 与 due；
    #   4. level 不得超过该类别实际可核的上限（known_limits 的机械影子）。
    policy = reg.get("provenance_policy") or {}
    current = policy.get("current") or {}
    registered = {c[0] for c in r.checks}
    LEVEL_RANK = {"none": 0, "file": 1, "clause": 2, "paragraph": 3}
    LEVEL_CAP = {"skills": "file", "principles": "clause"}
    miss = []
    if not current:
        miss.append("provenance_policy.current 缺失——来源政策的实际覆盖级别无处可核")
    for cat, ent in sorted(current.items()):
        ent = ent or {}
        status = ent.get("status")
        level = ent.get("level")
        if status == "enforced":
            cid = ent.get("enforced_by")
            if not cid:
                miss.append(f"provenance_policy.current.{cat} 标 enforced 却没写 enforced_by"
                            f"——没有承载体，enforced 就是一句空话")
            elif cid not in registered:
                miss.append(f"provenance_policy.current.{cat} 的 enforced_by={cid} "
                            f"不是本次运行中注册的检查项——指向不存在的检查")
            elif cid not in CHECK_COVERS:
                miss.append(f"检查项 {cid} 没有在 CHECK_COVERS 里声明它核的载体类目"
                            f"——「指向存在」不等于「覆盖」，无法证明它的断言落在 "
                            f"provenance_policy.current.{cat} 上")
            elif CHECK_COVERS[cid][0] != cat:
                miss.append(f"provenance_policy.current.{cat} 声称由 {cid} 覆盖，"
                            f"但 {cid} 的 CHECK_COVERS 声明它核的是 "
                            f"{CHECK_COVERS[cid][0]}——绑定的不是同一个对象")
            if level in (None, "none"):
                miss.append(f"provenance_policy.current.{cat} 标 enforced 但 level={level}"
                            f"——没到任何可核粒度就不能声称执行")
        elif status == "UNVERIFIED":
            for k in ("owner", "due"):
                if not ent.get(k):
                    miss.append(f"provenance_policy.current.{cat} 标 UNVERIFIED 却没写 {k}"
                                f"——无限期的静态标签不是待办，必须有责任人与到期条件")
        else:
            miss.append(f"provenance_policy.current.{cat} 的 status={status!r} 非法"
                        f"——只承认 enforced / UNVERIFIED")
        if level not in LEVEL_RANK:
            miss.append(f"provenance_policy.current.{cat} 的 level={level!r} 非法"
                        f"——只承认 none / file / clause / paragraph")
        else:
            cap = LEVEL_CAP.get(cat)
            if cap and LEVEL_RANK[level] > LEVEL_RANK[cap]:
                miss.append(f"provenance_policy.current.{cat} 的 level={level} 高于实际可核的 "
                            f"{cap}——known_limits 明写条款级不能当段落级，写高了就是假声明")
    covers = "；".join(f"{k}→{v[0]}/{v[1]}" for k, v in sorted(CHECK_COVERS.items()))
    r.add("C22", "来源政策的 enforced_by 绑定真实载体", not miss,
          f"provenance_policy.current 共 {len(current)} 条；enforced 的绑定经 CHECK_COVERS "
          f"核对（{covers}）；UNVERIFIED 条目均带 owner 与 due。"
          f"边界：CHECK_COVERS 是维护者的声明——C22 证明「声明的类目」与 policy 一致，"
          f"不证明检查实现真的读了那些文件；后者靠 C20/C21 的故障注入反例。", miss)

    return r.report(args.quiet)


if __name__ == "__main__":
    sys.exit(main())
