#!/usr/bin/env python3
"""
check-consistency.py · 一致性与互斥检查（只读，可重复运行）

check-closure.py 证明「图是通的」。本脚本证明「文件之间不打架」。

上一版把同一段工程方法复制进 9 个角色正文，于是同一件事在 9 个地方被写成互相
矛盾的说法。本脚本把这类失败变成非零退出。

  S1 无游离文件   roles/ skills/ principles/ workflow/phases/ 与注册表一一对应
  S2 引用可解析   文件里出现的 @id 与相对链接必须能解析
  S3 权限互斥     同一文件里对同一对象既「不得」又「必须」
  S4 硬规则一致   阶段硬规则与角色硬边界不得互相打架
  S5 三角一致     技能的 phase / owner_role / 该阶段默认角色三者相容
  S6 持久性一致   声明为 session 级的产物不得出现在交付阶段的判据里
  S7 横切带一致   横切带的适用范围必须覆盖实际装配它的角色所参与的阶段

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
KNOWN_SCRIPTS = {"check-closure.py", "check-consistency.py", "render.py", "ledger.sh"}

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
    """抽取 (动词, 宾语短语) 列表。宾语为动词后到句读/标点为止，去掉序号与停用词。"""
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
            out.append((v, key))
    return out


class Result:
    def __init__(self):
        self.checks = []

    def add(self, cid, name, ok, detail="", misses=None):
        self.checks.append((cid, name, ok, detail, misses or []))

    def report(self, quiet=False):
        if not quiet:
            print("TIM · check-consistency.py（只读一致性与互斥检查）")
            print(f"真源: {REGISTRY.relative_to(ROOT)}")
            print("-" * 76)
            for cid, name, ok, detail, misses in self.checks:
                print(f"[{'PASS' if ok else 'FAIL'}] {cid} {name:<20} {detail}")
                for m in misses[:10]:
                    print(f"         ↳ {m}")
                if len(misses) > 10:
                    print(f"         ↳ …另 {len(misses) - 10} 条")
        npass = sum(1 for c in self.checks if c[2])
        nfail = sum(1 in [0] for c in self.checks if not c[2])
        nfail = len(self.checks) - npass
        print("-" * 76)
        print(f"合计: {npass} 项通过 / {nfail} 项失败 / {len(self.checks)} 项检查")
        return 0 if nfail == 0 else 1


def read(p):
    return p.read_text(encoding="utf-8")


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
        on_disk = {f.stem for f in d.glob("*.md")}
        for extra in sorted(on_disk - ids):
            miss.append(f"{key}/{extra}.md 不在注册表里——游离文件，删掉或登记")
        for absent in sorted(ids - on_disk):
            miss.append(f"注册表里的 {key}:{absent} 没有对应文件")
    # 原则一个文件放多条（按主题分组），不强制一文件一条
    if DIRS["principles"].is_dir():
        declared = set()
        for f in DIRS["principles"].glob("*.md"):
            declared |= set(re.findall(r"^##\s+(p-[a-z\-]+)\s*$", read(f), re.M))
        for missing in sorted(set(pr_by_id) - declared):
            miss.append(f"原则 {missing} 在 principles/ 里没有对应的 ## 段落")
        for orphan in sorted(declared - set(pr_by_id)):
            miss.append(f"principles/ 里的 {orphan} 不在注册表中")
    sd = ROOT / "scripts"
    if sd.is_dir():
        for f in sorted(sd.iterdir()):
            if f.is_file() and f.name not in KNOWN_SCRIPTS and f.name != ".DS_Store":
                miss.append(f"scripts/{f.name} 不在本库承认的四个脚本内——"
                            f"上一版残留或临时产物，删掉或登记")
    r.add("S1", "无游离文件", not miss,
          f"角色 {len(expect['roles'])}／技能 {len(expect['skills'])}／"
          f"阶段 {len(expect['phases'])}／横切带 {len(expect['ribbons'])} 与注册表对齐，"
          f"scripts/ 无残留", miss)

    # ── S2 引用可解析 ───────────────────────────────────────────
    known = (set(r_by_id) | set(s_by_id) | set(pr_by_id) | set(p_by_id) | set(a_by_id)
             | {rb["id"] for rb in ribbons} | {str(v) for v in a_by_id.values() for v in []})
    miss = []
    md_files = [f for d in DIRS.values() if d.is_dir() for f in sorted(d.glob("*.md"))]
    for f in md_files:
        text = read(f)
        for lineno, line in enumerate(text.splitlines(), 1):
            for ref in re.findall(r"`@([a-zA-Z0-9\-]+)`", line):
                if ref not in known and ref not in {k for k, v in s_by_id.items()}:
                    miss.append(f"{f.relative_to(ROOT)}:{lineno} 引用未知 id `{ref}`")
            for link in re.findall(r"\]\((?!https?:)([^)#]+)\)", line):
                target = (f.parent / link).resolve()
                if not target.exists():
                    miss.append(f"{f.relative_to(ROOT)}:{lineno} 死链 → {link}")
    r.add("S2", "引用可解析", not miss,
          f"扫描 {len(md_files)} 个库文件，0 处未知 id、0 处死链", miss)

    # ── S3 权限互斥 ─────────────────────────────────────────────
    miss = []
    for f in md_files:
        text = read(f)
        by_pair = {}
        for lineno, s in sentences(text):
            polarity = "neg" if NEG.search(s) else ("req" if REQ.search(s) else None)
            if not polarity:
                continue
            for v, obj in objects_of(s):
                by_pair.setdefault((v, obj), {"neg": set(), "req": set()})[polarity].add(lineno)
        for (v, obj), where in by_pair.items():
            if where["neg"] and where["req"]:
                miss.append(f"{f.relative_to(ROOT)} 互斥：「{v}{obj}」在第 "
                            f"{sorted(where['neg'])[0]} 行被禁止、第 {sorted(where['req'])[0]} 行又被要求")
        ids = re.findall(r"^##\s+([A-Za-z0-9\-]+)\s*$", text, re.M)
        for i in set(ids):
            if ids.count(i) > 1:
                miss.append(f"{f.relative_to(ROOT)} 重复定义 {i}（出现 {ids.count(i)} 次）")
    r.add("S3", "文件内权限互斥（词形级）", not miss,
          f"扫描 {len(md_files)} 个文件的「动作+宾语」否定/要求配对，0 处互斥。"
          f"边界：只抓同一文件内同动词同宾语；同义改写与跨文件冲突抓不到，"
          f"那部分靠独立审查与人审", miss)

    # ── S4 硬规则一致 ───────────────────────────────────────────
    miss = []
    for ph in reg.get("phases", []):
        for rule in ph.get("hard_rules", []):
            # 角色可能以 id 或中文名出现在硬规则里，两种都要认
            who = None
            for rid, role in r_by_id.items():
                if rid in rule or (role.get("zh") and role["zh"] in rule):
                    who = rid
                    break
            if who and who in ph.get("default_roles", []):
                miss.append(f"互斥：阶段 {ph['id']} 的硬规则说「{rule}」，"
                            f"但 {who} 正在该阶段的默认角色里")
    # 同一角色在注册表里被两个阶段同时赋予互斥职责
    for rid, role in r_by_id.items():
        raw = role.get("forbidden", [])
        dup = {x for x in raw if raw.count(x) > 1}
        if dup:
            miss.append(f"{rid} 的 forbidden 列表里有重复项：{sorted(dup)}")
    r.add("S4", "硬规则不互斥", not miss,
          f"{sum(len(p.get('hard_rules', [])) for p in reg.get('phases', []))} 条阶段硬规则与 "
          f"{sum(len(x.get('forbidden', [])) for x in reg.get('roles', []))} 条角色硬边界不打架", miss)

    # ── S5 技能三角一致 ─────────────────────────────────────────
    miss = []
    for sid, sk in s_by_id.items():
        ph = sk.get("phase")
        owner = sk.get("owner_role")
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
    r.add("S5", "技能三角一致", not miss,
          f"{len(s_by_id)} 个技能的阶段／归属角色／装配三者相容", miss)

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
            outside = phase_of_role.get(rid, set()) - applies
            if outside:
                miss.append(f"横切带 {rb_id} 只适用于 {sorted(applies)}，"
                            f"但 {rid} 还参与 {sorted(outside)}")
            if not applies:
                miss.append(f"横切带 {rb_id} 既非常驻又没写适用范围")
    r.add("S7", "横切带适用范围一致", not miss,
          f"{len(ribbons)} 条横切带的适用范围覆盖其携带角色参与的阶段", miss)

    return r.report(args.quiet)


if __name__ == "__main__":
    sys.exit(main())
