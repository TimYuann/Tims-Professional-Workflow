#!/usr/bin/env python3
"""
check-consistency.py · 一致性与互斥检查（只读，可重复运行）

check-closure.py 证明「图是通的」。本脚本证明「文件之间不打架」。

上一版把同一段工程方法复制进 9 个角色正文，于是同一件事在 9 个地方被写成互相
矛盾的说法。本脚本把这类失败变成非零退出。

  S1 无游离文件   roles/ skills/ workflow/phases/ workflow/ribbons/ 与注册表一一对应，
                 含子目录（子目录里的文件同样算游离）
  S2 引用可解析   文件里出现的 @id 与相对链接（含 #fragment）必须能解析
  S3 权限互斥     同一文件里对同一对象既「不得」又「必须」（按子句判极性）
  S4 硬规则一致   阶段硬规则只引用已定义的阶段/角色；实现—裁决—验证三者不同场
  S5 技能三角一致 技能的 phase / owner_role / outputs / 该阶段默认角色四者相容
  S6 持久性一致   声明为 session 级的产物不得出现在交付阶段的判据里
  S7 横切带一致   横切带的适用范围必须是已定义阶段，且覆盖携带角色参与的阶段

用法:
  python3 scripts/check-consistency.py
  python3 scripts/check-consistency.py --quiet
"""

import sys, re, argparse
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("需要 pyyaml：python3 -m pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "workflow" / "registry.yaml"

DIRS = {
    "roles": ROOT / "roles",
    "skills": ROOT / "skills",
    "principles": ROOT / "principles",
    "phases": ROOT / "workflow" / "phases",
    "ribbons": ROOT / "workflow" / "ribbons",
}

# 本库只承认这四个脚本。出现别的就是上一版残留或临时产物——
# 不在 S1 的比对范围内，但必须被发现，否则它们会像 v2.0.0 里那样躺着。
KNOWN_SCRIPTS = {
    "check-closure.py",       # 闭包检查
    "check-consistency.py",   # 一致性与互斥检查
    "render.py",              # 派生视图生成 / 核对
    "ledger.sh",              # A9 台账追加工具
    "sync-upstreams.sh",      # 上游同步 + 重生成锁文件
    "_render-lock.py",        # 被 sync-upstreams.sh 调用的锁文件生成器
}

# 「不得 / 必须」识别。只在受控动词 + 重叠宾语上配对才算互斥。
NEG = re.compile(r"(不得|禁止|不可以|不许|不能|不应)")
REQ = re.compile(r"(必须|应当|应该|要|需要|每次|一定)")

# 受控动作词表：只比对这些动作之间的冲突，避开“禁止 A” vs “必须 B”的假阳性。
VERBS = [
    "写", "改", "删", "建", "问", "停", "合并", "跳过", "读", "跑", "跑一遍",
    "声称", "复制", "粘贴", "同步", "落盘", "记录", "判断", "裁决", "验证",
    "宣称", "输出", "产出", "引用", "内联", "带过", "打包", "执行", "重跑",
]
STOPWORDS = set("""的了和与或在是有为对把被从到并且则就都也还很更最一个这那它他她我你
我们你们他们这个那个一个如果因为所以但是而且""".split())


def objects_of(sentence):
    """抽取 (动词, 宾语短语, 动词位置) 列表。宾语为动词后到句读/标点为止，去掉序号与停用词。

    位置随行返回，因为 S3 要按**子句**定极性：只知道 (动词, 宾语) 无法回答
    「这个「写」属于前半句的「不得」还是后半句的「必须」」。
    """
    out = []
    for v in sorted(VERBS, key=len, reverse=True):
        for m in re.finditer(re.escape(v), sentence):
            tail = sentence[m.end():]
            tail = re.split(r"[，,。；;：:\n（(]", tail)[0]
            tail = re.sub(r"^[的地得\s]+", "", tail).strip()
            tail = re.sub(r"^\d+[.、)]\s*", "", tail)
            key = re.sub(r"[\s`*]", "", tail)
            if len(key) < 2 or key in STOPWORDS:
                continue
            out.append((v, key, m.start()))
    return out


# 子句切分。极性词可能在句首也可能在句尾：「不得写审查报告，但必须写审查报告」
# 整句只取一个极性（旧版只取第一个）时，第二半句的「必须」根本看不见。
CLAUSE_SPLIT = re.compile(r"[，,。；;]")


def clause_spans(sentence):
    """子句的 (start, end) 列表，按出现顺序。"""
    out, last = [], 0
    for m in CLAUSE_SPLIT.finditer(sentence):
        out.append((last, m.start()))
        last = m.end()
    out.append((last, len(sentence)))
    return out


class Result:
    """三态结果集。schema 与 check-closure.py 一致：
    通过 / 失败 / 跳过 / 检查。本脚本当前没有依赖环境的 SKIP 分支
    （不读 git、不要求网络），skip 参数为保持两个检查器同 schema 而保留——
    「合计」行少一栏会让下游 harness 的解析对不上账（round-3 §6.8）。
    """

    def __init__(self):
        self.checks = []

    def add(self, cid, name, ok, detail="", misses=None, skip=False):
        self.checks.append((cid, name, ok, detail, misses or [], skip))

    @property
    def failed(self):
        return [c for c in self.checks if not c[2] and not c[5]]

    def report(self, quiet=False):
        if not quiet:
            print("TIM · check-consistency.py（只读一致性与互斥检查）")
            print(f"真源: {REGISTRY.relative_to(ROOT)}")
            print("-" * 76)
            for cid, name, ok, detail, misses, skip in self.checks:
                tag = "SKIP" if skip else ("PASS" if ok else "FAIL")
                print(f"[{tag}] {cid} {name:<20} {detail}")
                for m in misses[:10]:
                    print(f"         ↳ {m}")
                if len(misses) > 10:
                    print(f"         ↳ …另 {len(misses) - 10} 条")
        npass = sum(1 for c in self.checks if c[2] and not c[5])
        nskip = sum(1 for c in self.checks if c[5])
        nfail = len(self.failed)
        print("-" * 76)
        print(f"合计: {npass} 项通过 / {nfail} 项失败 / {nskip} 项跳过 / {len(self.checks)} 项检查")
        return 0 if nfail == 0 else 1


def read(p):
    return p.read_text(encoding="utf-8")


# S2/S3 的扫描集 = 库内容文件 + 面向读者的入口文档。
# docs/ 下的 history/ 与 archive/ 只记「曾经发生过什么」，不构成对下游的指令，
# 与 D1 一样只豁免这两棵子树；docs/ 其余部分是当前契约的下游说明，必须可解析。
DOC_EXEMPT_SUBTREES = ("docs/history", "docs/archive")
IGNORE_NAMES = {".DS_Store"}
IGNORE_DIRS = {"__pycache__"}


def exempt(rel) -> bool:
    parts = tuple(rel.parts) if hasattr(rel, "parts") else tuple(str(rel).split("/"))
    for x in DOC_EXEMPT_SUBTREES:
        head = tuple(x.split("/"))
        if parts[:len(head)] == head:
            return True
    return False


def walk_md(root: Path):
    """root 下全部 .md，按路径排序，豁免 DOC_EXEMPT_SUBTREES 与噪声。"""
    if not root.is_dir():
        return
    for f in sorted(root.rglob("*.md")):
        if exempt(f.relative_to(ROOT)) or f.name in IGNORE_NAMES:
            continue
        if any(p in IGNORE_DIRS for p in f.relative_to(root).parts[:-1]):
            continue
        yield f


def library_md_files():
    """S2/S3 扫描的全部 .md：库内容目录 + 入口文档。"""
    out = [f for d in DIRS.values() for f in walk_md(d)]
    for n in ("README.md", "AGENTS.md"):
        if (ROOT / n).is_file():
            out.append(ROOT / n)
    out += list(walk_md(ROOT / "docs"))
    seen, uniq = set(), []
    for f in out:
        if f not in seen:
            seen.add(f)
            uniq.append(f)
    return uniq


def polarity_of(text):
    """一句话/子句的极性：先看否定，再看要求。都没有则 None。"""
    if NEG.search(text):
        return "neg"
    if REQ.search(text):
        return "req"
    return None


def sentences(text):
    """按行 + 按中文句读切句，避免整段匹配造成误判。"""
    out = []
    for i, line in enumerate(text.splitlines(), 1):
        if line.strip().startswith("#") or line.strip().startswith(">"):
            continue
        for s in re.split(r"[。；;]", line):
            if s.strip():
                out.append((i, s.strip()))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    r = Result()
    if not REGISTRY.is_file():
        print(f"找不到 {REGISTRY}")
        return 2
    reg = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))

    a_by_id = {a["id"]: a for a in reg.get("artifacts", [])}
    p_by_id = {p["id"]: p for p in reg.get("phases", [])}
    r_by_id = {x["id"]: x for x in reg.get("roles", [])}
    pr_by_id = {p["id"]: p for p in reg.get("principles", [])}
    s_by_id = {s["id"]: s for s in reg.get("skills", [])}
    ribbons = reg.get("ribbons", [])

    # ── S1 无游离文件 ───────────────────────────────────────────
    miss = []
    expect = {
        "roles": set(r_by_id),
        "skills": set(s_by_id),
        "phases": set(p_by_id),
        "ribbons": {rb["id"] for rb in ribbons},
    }
    for key, ids in expect.items():
        d = DIRS[key]
        if not d.is_dir():
            miss.append(f"{key}/ 目录不存在")
            continue
        # rglob 而不是 glob：旧版只看一层，skills/rogue/SKILL.md 这种
        # 嵌套目录整棵漏掉——它既不在注册表里，也没人扫得到。
        # 一个目录下的文件只有「<id>.md」这一种合法名字，其余（含子目录里
        # 的任何文件、任何非 .md 旁路文件）都是游离。
        for f in sorted(p for p in d.rglob("*") if p.is_file()):
            if f.name in IGNORE_NAMES or any(
                    part in IGNORE_DIRS for part in f.relative_to(d).parts):
                continue
            rel = f.relative_to(d).as_posix()
            if rel != f"{f.stem}.md" or f.stem not in ids:
                miss.append(f"{key}/{rel} 不在注册表里——游离文件"
                            f"（子目录里的文件同样算），删掉或登记")
        for absent in sorted(ids):
            if not (d / f"{absent}.md").is_file():
                miss.append(f"注册表里的 {key}:{absent} 没有对应文件")
    # 原则一个文件放多条（按主题分组），不强制一文件一条；
    # 但不允许在 principles/ 下开子目录。
    if DIRS["principles"].is_dir():
        declared = set()
        for f in DIRS["principles"].glob("*.md"):
            declared |= set(re.findall(r"^##\s+(p-[a-z\-]+)\s*$", read(f), re.M))
        for missing in sorted(set(pr_by_id) - declared):
            miss.append(f"原则 {missing} 在 principles/ 里没有对应的 ## 段落")
        for orphan in sorted(declared - set(pr_by_id)):
            miss.append(f"principles/ 里的 {orphan} 不在注册表中")
        for sub in sorted(p for p in DIRS["principles"].rglob("*") if p.is_dir()):
            miss.append(f"principles/{sub.relative_to(DIRS['principles']).as_posix()}/ "
                        f"是子目录——原则按主题分文件，不按子目录分组")
    sd = ROOT / "scripts"
    if sd.is_dir():
        for f in sorted(sd.iterdir()):
            if f.is_file() and f.name not in KNOWN_SCRIPTS and f.name != ".DS_Store":
                miss.append(f"scripts/{f.name} 不在本库承认的四个脚本内——"
                            f"上一版残留或临时产物，删掉或登记")
    r.add("S1", "无游离文件（rglob 含子目录）", not miss,
          f"角色 {len(expect['roles'])}／技能 {len(expect['skills'])}／"
          f"阶段 {len(expect['phases'])}／横切带 {len(expect['ribbons'])} 与注册表对齐"
          f"（含子目录逐个文件比对），scripts/ 无残留", miss)

    # ── S2 引用可解析 ───────────────────────────────────────────
    known = (set(r_by_id) | set(s_by_id) | set(pr_by_id) | set(p_by_id) | set(a_by_id)
             | {rb["id"] for rb in ribbons} | {str(v) for v in a_by_id.values() for v in []})
    miss = []
    md_files = library_md_files()
    # 链接先剥 fragment 再判存在：旧正则 `\]\((?!https?:)([^)#]+)\)` 遇到
    # `#` 就整条不匹配，于是 `../missing.md#section` 这种死链连报都不报。
    LINK = re.compile(r"\]\((?![a-zA-Z][a-zA-Z0-9+.-]*:)([^)\s]+)\)")
    for f in md_files:
        text = read(f)
        for lineno, line in enumerate(text.splitlines(), 1):
            for ref in re.findall(r"`@([a-zA-Z0-9\-]+)`", line):
                if ref not in known and ref not in {k for k, v in s_by_id.items()}:
                    miss.append(f"{f.relative_to(ROOT)}:{lineno} 引用未知 id `{ref}`")
            for link in LINK.findall(line):
                path = link.split("#", 1)[0].strip().strip("<>")
                if not path:
                    continue
                target = (f.parent / path).resolve()
                if not target.exists():
                    miss.append(f"{f.relative_to(ROOT)}:{lineno} 死链 → {link}")
    r.add("S2", "引用可解析（含 fragment 死链）", not miss,
          f"扫描 {len(md_files)} 个库文件与入口文档（含 README/AGENTS/docs，"
          f"只豁免 history/ 与 archive/），0 处未知 id、0 处死链", miss)

    # ── S3 权限互斥 ─────────────────────────────────────────────
    # 极性按**子句**判，(动词,宾语) 仍在整句范围抽。
    # 旧版整句只取一个极性（谁先出现算谁），于是
    # 「不得写审查报告，但必须写审查报告」整句被判成纯 neg，第二半句的
    # 「必须」根本没人看——同一句话里既禁又令，恰恰是最该报的那种互斥。
    #
    # 归属规则：每个 (动词, 宾语) 落到它**所在子句**的极性上；子句本身
    # 没有极性词时回退到整句极性（保守，行为与旧版一致）。
    # 不能把整句所有宾语同时挂到 neg 和 req 上——那会让每一句“不得X，
    # 必须Y”里的 X 和 Y 都变成互斥，误报满天飞。
    miss = []
    for f in md_files:
        text = read(f)
        by_pair = {}
        for lineno, s in sentences(text):
            objs = objects_of(s)
            if not objs:
                continue
            spans = clause_spans(s)
            sent_pol = polarity_of(s)
            for v, obj, pos in objs:
                pol = sent_pol
                for a, b in spans:
                    if a <= pos < b:
                        pol = polarity_of(s[a:b]) or sent_pol
                        break
                if not pol:
                    continue
                by_pair.setdefault((v, obj), {"neg": set(), "req": set()})[pol].add(lineno)
        for (v, obj), where in by_pair.items():
            if where["neg"] and where["req"]:
                miss.append(f"{f.relative_to(ROOT)} 互斥：「{v}{obj}」在第 "
                            f"{sorted(where['neg'])[0]} 行被禁止、第 {sorted(where['req'])[0]} 行又被要求")
        ids = re.findall(r"^##\s+([A-Za-z0-9\-]+)\s*$", text, re.M)
        for i in set(ids):
            if ids.count(i) > 1:
                miss.append(f"{f.relative_to(ROOT)} 重复定义 {i}（出现 {ids.count(i)} 次）")
    r.add("S3", "文件内权限互斥（子句级）", not miss,
          f"扫描 {len(md_files)} 个文件的「动作+宾语」否定/要求配对（极性按子句判），"
          f"0 处互斥。边界：只抓同一文件内同动词同宾语；同义改写与跨文件冲突"
          f"抓不到，那部分靠独立审查与人审", miss)

    # ── S4 阶段硬规则 ──────────────────────────────────────────
    #
    # 旧实现：「硬规则点名了某个角色，而该角色正在该阶段默认角色里 → FAIL」。
    # 它在本库当前数据上**一条都抓不到**，也没人能说它保护了什么：
    #   1. 角色名匹配是「按注册表顺序取第一个命中的」，结果取决于字典顺序，
    #      不取决于任何语义。roles 换个顺序，同一条硬规则的判定就变。
    #   2. 三条硬规则里没有一条能被匹配上（它们写的是「实现者」「验证者」，
    #      而角色的 zh 是「实现」「独立验证」），所以 who 恒为 None。
    #      反过来也证明了「把它反过来」不行：反过来的读法是「硬规则点名的角色
    #      必须在该阶段 default_roles 里」，而 P4 的规则是
    #      「实现者不得对本候选给出裁决」——builder 本来就不该在 P4，这个读法
    #      会把一条正确的硬规则判成错。
    # 两个方向都会在干净数据上出错，所以它不是一条能靠改写挽救的断言。
    # 下面换成两条**结构性**的（不猜中文语义）：
    miss = []
    hard_rule_ids = set(r_by_id)
    for ph in reg.get("phases", []):
        for rule in ph.get("hard_rules", []):
            # 硬规则里引用的阶段/角色 id 必须存在（改阶段名、改角色名时跟上）
            for tok in set(re.findall(r"\bP\d+\b", rule)):
                if tok not in p_by_id:
                    miss.append(f"阶段 {ph['id']} 的硬规则引用未定义的阶段 {tok}：{rule}")
            for tok in set(re.findall(r"\b[a-z][a-z-]{2,}\b", rule)):
                if tok in {"solo", "driver", "roles", "md"} or "_" in tok:
                    continue
                if re.fullmatch(r"[a-z][a-z-]{2,}", tok) and tok not in p_by_id \
                        and tok not in hard_rule_ids and "-" in tok:
                    miss.append(f"阶段 {ph['id']} 的硬规则提到 `{tok}`，"
                                f"但它既不是已定义的角色 id，也不是已定义的阶段 id：{rule}")
    # 实现—裁决—验证不共场。
    # 本库的两条职责分离硬规则（「实现者不得对本候选给出裁决」「验证者不得是
    # 候选的实现者」）说的是同一件事：产出 A6 的角色不得与产出 A7/A8 的角色
    # 同时在岗。把它从散文降为可判定约束——旧版没有任何检查覆盖这一条：
    # 往 P4.default_roles 里加 builder，C3/C4/C6/C11/C13/S5 都不会红。
    sep = []
    if "A6" in a_by_id and "A7" in a_by_id:
        sep.append((a_by_id["A6"]["producer"], a_by_id["A7"]["producer"], "裁决"))
    if "A6" in a_by_id and "A8" in a_by_id:
        sep.append((a_by_id["A6"]["producer"], a_by_id["A8"]["producer"], "验证"))
    for ph in reg.get("phases", []):
        equipped = set(ph.get("default_roles", []))
        for r1, r2, what in sep:
            if r1 in equipped and r2 in equipped:
                miss.append(f"阶段 {ph['id']} 同时装配了 `{r1}`（实现候选的产出方）"
                            f"与 `{r2}`（{what}的产出方）——实现与{what}不得同场，"
                            f"这正是本库硬规则要守的职责分离")
    # 同一角色在注册表里被两个阶段同时赋予互斥职责
    for rid, role in r_by_id.items():
        raw = role.get("forbidden", [])
        dup = {x for x in raw if raw.count(x) > 1}
        if dup:
            miss.append(f"{rid} 的 forbidden 列表里有重复项：{sorted(dup)}")
    r.add("S4", "硬规则引用可解析 + 实现裁决验证不同场", not miss,
          f"{sum(len(p.get('hard_rules', [])) for p in reg.get('phases', []))} 条阶段硬规则"
          f"只引用已定义的阶段/角色；{len(sep)} 组职责分离不共场；"
          f"{sum(len(x.get('forbidden', [])) for x in reg.get('roles', []))} 条角色硬边界无重复。"
          f"边界：硬规则的中文语义（如「solo 档除外」的豁免）抓不到——"
          f"本检查只看它引用的 id 与它维护的分离约束。"
          f"边界：S4 不读角色正文；「实现者」↔`builder`、「下结论」↔「给出裁决」"
          f"是中文语义映射，没有确定性规则能把它变成断言——角色正文里写反硬边界"
          f"的散文抓不到（s4-role-body）。", miss)

    # ── S5 技能三角一致 ─────────────────────────────────────────
    miss = []
    for sid, sk in s_by_id.items():
        ph = sk.get("phase")
        owner = sk.get("owner_role")
        # outputs 必须指向已定义产物。
        # 旧版不查这条，而 C14 的 `A\d` 正则会把 A404 读成 A4，于是「技能
        # outputs 引用不存在的产物」这件事全库无人负责（C14 兼底是偶然，
        # 报错信息还把 A404 说成 A4，误导下一个来查的人）。C14 已改用
        # `\bA\d+\b`，这条是它的必要配套。
        for out in sk.get("outputs", []):
            if out not in a_by_id:
                miss.append(f"技能 {sid} 的 outputs 引用未定义的产物 {out}"
                            f"——它不是任何一类已定义产物")
        if ph and ph not in p_by_id:
            miss.append(f"技能 {sid} 声明属于阶段 {ph}，该阶段不存在")
            continue
        if owner not in r_by_id:
            miss.append(f"技能 {sid} 的 owner_role {owner} 未定义")
            continue
        if ph:
            equipped = set(p_by_id[ph].get("default_roles", []))
            rb_carriers = {rb["id"] for rb in ribbons if sid in rb.get("skills", [])}
            if owner not in equipped and not rb_carriers:
                miss.append(f"技能 {sid} 归 {owner} 且标在 {ph}，但 {ph} 的默认角色里"
                            f"没有 {owner}，也没有横切带携带它——不知道谁在什么时候用它")
        if ph:
            # 一个技能只能产出「该阶段的默认角色里有人产出」的产物。
            # 这一条会拦住：adversary 在 P4 产出 builder 独占的 A6。
            equipped = set(p_by_id[ph].get("default_roles", []))
            for out in sk.get("outputs", []):
                prod = (a_by_id.get(out) or {}).get("producer")
                if prod and prod not in equipped and prod != owner:
                    miss.append(f"技能 {sid} 在 {ph} 产出 {out}，但它的主产出方 {prod} "
                                f"不在 {ph} 的默认角色里，而 {sid} 属于 {owner}——"
                                f"这个产物在那个阶段没人负责")
        if sk.get("outputs") and not sk.get("inputs") and sid not in (
                "decision-ledger", "grilling", "interview-me", "idea-refine"):
            miss.append(f"技能 {sid} 有产出但没有输入，链路起点不成立")
    r.add("S5", "技能三角一致（含 outputs 可解析）", not miss,
          f"{len(s_by_id)} 个技能的阶段／归属角色／outputs 可解析／装配四者相容", miss)

    # ── S6 持久性一致 ───────────────────────────────────────────
    miss = []
    LIVE_ACROSS = ("durable",)
    for ph in reg.get("phases", []):
        for need in ph.get("required_inputs", []):
            a = a_by_id.get(need)
            if a and a.get("persistence") not in LIVE_ACROSS:
                miss.append(f"{ph['id']} 依赖 {need}，但它的 persistence 是 "
                            f"{a.get('persistence')}——活不过当前会话的东西不能作为阶段输入")
    for sid, sk in s_by_id.items():
        for out in sk.get("outputs", []):
            a = a_by_id.get(out)
            if a and a.get("persistence") not in LIVE_ACROSS and sk.get("phase") == "P6":
                miss.append(f"技能 {sid} 在交付阶段产出 {out}，但它的 persistence 是 "
                            f"{a.get('persistence')}")
    # 声明为 session 级的产物，不得被任何角色说成「长期留档」
    for rid, role in r_by_id.items():
        for a in role.get("owns_artifacts", []):
            art = a_by_id.get(a)
            if art and art.get("persistence") == "session" and rid != art.get("producer"):
                miss.append(f"{rid} 声称拥有 session 级的 {a}，但它的主产出方是 "
                            f"{art.get('producer')}")
    r.add("S6", "产物持久性一致", not miss,
          f"{len(a_by_id)} 类产物的 persistence 与各阶段依赖、各角色归属相容", miss)

    # ── S7 横切带一致 ───────────────────────────────────────────
    miss = []
    phase_of_role = {}
    for ph in reg.get("phases", []):
        for rid in ph.get("default_roles", []):
            phase_of_role.setdefault(rid, set()).add(ph["id"])
    for rid, role in r_by_id.items():
        for rb_id in role.get("ribbons", []):
            rb = next((x for x in ribbons if x["id"] == rb_id), None)
            if rb is None:
                miss.append(f"{rid} 挂载了未定义的横切带 {rb_id}")
                continue
            if rb.get("always"):
                continue
            applies = set(rb.get("applies_to", []))
            # applies_to 里的每个 id 都必须是已定义阶段。
            # 旧版不查：写一个不存在的 P404 进去，适用范围看起来只是「多了一项」，
            # 于是「只适用于 P0/P4/P6」这句话在实际上没人能对照核——适用范围
            # 是这个检查的**全部依据**，依据本身错了它就跟着错。
            for bad in sorted(applies - set(p_by_id)):
                miss.append(f"横切带 {rb_id} 的 applies_to 里有未定义的阶段 {bad}")
            outside = phase_of_role.get(rid, set()) - applies
            if outside:
                miss.append(f"横切带 {rb_id} 只适用于 {sorted(applies)}，"
                            f"但 {rid} 还参与 {sorted(outside)}")
            if not applies:
                miss.append(f"横切带 {rb_id} 既非常驻又没写适用范围")
    r.add("S7", "横切带适用范围一致且可解析", not miss,
          f"{len(ribbons)} 条横切带的适用范围全部是已定义阶段，且覆盖其携带角色参与的阶段", miss)

    return r.report(args.quiet)


if __name__ == "__main__":
    sys.exit(main())
