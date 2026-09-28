#!/usr/bin/env python3
"""故障注入集 v2 · 0929 —— 每条注入自带 probe（语义后置条件）与 expect（期望归因）。

与 harness.py（v2）配套。相对上一轮（prev-r3/suite.py）的改动只有两类：

  1. 每条注入补 probe：证明**缺陷真的被引入了**，不是「文件变了」。
     probe 只读文件、自己解析，不复用 scripts/ 里的检查器代码。
  2. 收紧 expect：写清这条缺陷按语义该被哪几项抓住；宽泛的「兜底集合」不再算数。
     红在期望之外会单独打出来（期望外红），不让它冒充归因。

另加：两条负对照（无害注入必须被拒绝记成指控）、两条 C9 锁篡改（probe 的样例来源）。

三态纪律：probe 不成立 = 这条注入无效 = UNVERIFIED，**绝不是**「检查器漏报」。
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import harness as H          # noqa: E402
import probes as P           # noqa: E402

REG = "workflow/registry.yaml"
ROWS: list[dict] = []


def add(tag, expect, desc, mutate, probe, *, with_upstreams=True,
        boundary=None, control=False, witness=None, predicate=None):
    assert control or boundary is not None or expect, f"{tag}: 没有 expect 就必须给 boundary（或声明为负对照）"
    ROWS.append(dict(tag=tag, expect=set(expect or ()), desc=desc, mutate=mutate,
                     probe=probe, with_upstreams=with_upstreams, boundary=boundary,
                     control=control, witness=witness, predicate=predicate))


# ══════════════════════════════════════════════════════════════
# 28 条（沿用上一轮的注入动作，逐条补 probe / 收紧 expect）
# ══════════════════════════════════════════════════════════════

# ── C3 孤儿阶段 ──────────────────────────────────────────────
def c3_orphan_phase(d):
    H.sub(REG, "phases:\n  - id: P0", """phases:
  - id: P7
    name: ORPHAN
    zh: 孤儿阶段
    purpose: 没有上游依赖，谁也不依赖它。
    required_inputs: []
    exit_criteria:
      - "verify: A9.actor 有一行"
    default_roles: [driver]
    produces: []
  - id: P0""")(d)
    (d / "workflow" / "phases" / "P7.md").write_text(
        "# P7 孤儿阶段\n\n什么都不产出。\n", encoding="utf-8")


def c3_probe(d):
    """缺陷定义：存在一个阶段，既没有进边（required_inputs 空）也没有出边
    （produces 空 / 无人消费它的产出）。P7 两端都空到不能再空。"""
    r = P.reg(d)
    ph = P.phase(r, "P7")
    if ph is None or ph.get("required_inputs") or ph.get("produces"):
        return False
    return (d / "workflow" / "phases" / "P7.md").is_file()


add("c3-orphan-phase", {"C3"},
    "C3：塞一个无输入、无产出、无上游依赖的 P7 + 同名 md",
    c3_orphan_phase, c3_probe)


# ── C4 伪字段 ────────────────────────────────────────────────
def c4_ghost_field(d):
    H.sub(REG, '      - "verify: A6.runnable 是真的能跑的（不是「应该能跑」）"',
          '      - "verify: A6.GHOST 已刷新，同时 A6.runnable 是真的能跑的"')(d)


def c4_probe(d):
    """缺陷定义：某条判据引用了 A6.GHOST，而 A6 的字段表里没有 GHOST。"""
    r = P.reg(d)
    a6 = P.artifact(r, "A6")
    crit = [c for ph in r["phases"] for c in ph.get("exit_criteria", []) if "A6.GHOST" in c]
    return bool(crit) and "GHOST" not in (a6.get("fields") or [])


add("c4-ghost-field", {"C4"},
    "C4：判据写 A6.GHOST 伪字段 + 同句一个真字段", c4_ghost_field, c4_probe)


# ── C10 第二次认领 ───────────────────────────────────────────
def c10_second_target(d):
    H.sub(REG, "sources: [matt:tdd, pstack:tdd, addy:test-driven-development]",
          "sources: [matt:tdd, pstack:tdd, addy:test-driven-development, pstack:blast-radius]")(d)


def c10_second_target_probe(d):
    """缺陷定义：tdd 的 sources 多认领了 pstack:blast-radius，
    而该上游的处置记录里没有任何指向 tdd 的 into（白拿第二份）。"""
    r = P.reg(d)
    tdd = P.skill(r, "tdd")
    if "pstack:blast-radius" not in (tdd.get("sources") or []):
        return False
    dsp = next((x for x in r.get("upstream_dispositions", [])
                if x["upstream"] == "pstack:blast-radius"), None)
    return dsp is not None and "tdd" not in (dsp.get("into") or [])


add("c10-second-target", {"C10", "C20"},
    "C10：同一上游被第二个技能认领（tdd 多认一个没有处置指向它的来源）",
    c10_second_target, c10_second_target_probe)


# ── C11 反向消费 ─────────────────────────────────────────────
def c11_reverse(d):
    H.sub(REG, "    required_inputs: [A4, A5]", "    required_inputs: [A1, A4, A5]")(d)


def c11_reverse_probe(d):
    """缺陷定义：P3 装配里要 A1，而 A1 的 consumers 里没有 P3。"""
    r = P.reg(d)
    p3 = P.phase(r, "P3")
    a1 = P.artifact(r, "A1")
    return ("A1" in (p3.get("required_inputs") or [])
            and "A1" not in (p3.get("produces") or [])
            and "P3" not in (a1.get("consumers") or []))


add("c11-reverse", {"C11"},
    "C11：P3.required_inputs 加 A1，但 A1.consumers 不加 P3", c11_reverse, c11_reverse_probe)


# ── C13 判据不声明动作 ───────────────────────────────────────
def c13_no_prefix(d):
    H.sub(REG, '      - "verify: A6.known_gaps 非空或明确标注无"',
          '      - "A6.known_gaps 非空或明确标注无"')(d)


def c13_probe(d):
    """缺陷定义：某条判据没有 write:/verify: 前缀。"""
    r = P.reg(d)
    return any(c == "A6.known_gaps 非空或明确标注无"
               and not c.startswith(("write: ", "verify: "))
               for ph in r["phases"] for c in ph.get("exit_criteria", []))


add("c13-no-prefix", {"C13"},
    "C13：判据不声明 write/verify 前缀", c13_no_prefix, c13_probe)


# ── D1 底座名三处 ────────────────────────────────────────────
def d1_roles_probe(d):
    return P.file_contains_base_name(d, "roles/builder.md")


def d1_ledger_probe(d):
    return P.file_contains_base_name(d, "scripts/ledger.sh")


def d1_docs_probe(d):
    return P.file_contains_base_name(d, "docs/coldstart.md")


add("d1-uppercase", {"D1"}, "D1：角色文件写大写 Herdr",
    H.append("roles/builder.md", "\n运行在 Herdr 里。\n"), d1_roles_probe)

add("d1-ledger-env", {"D1"}, "D1：scripts/ledger.sh 写 HERDR_AGENT",
    H.append("scripts/ledger.sh", '\nAGENT_NAME="${HERDR_AGENT}"\n'), d1_ledger_probe)

add("d1-docs", {"D1"}, "D1：active docs 写具体底座名",
    H.append("docs/coldstart.md", "\n用 herdr 打开这个工作区。\n"), d1_docs_probe)


# ── S1 游离文件 ──────────────────────────────────────────────
def s1_nested(d):
    p = d / "skills" / "rogue"
    p.mkdir(parents=True, exist_ok=True)
    (p / "SKILL.md").write_text(
        "# rogue\n\n- 阶段：无　产物：无\n\n## 什么时候用\n\n## 开工前要拿到\n\n"
        "## 方法\n\n## 产出\n\n## 常见做错\n\n## 来源\n\n本库原创。\n", encoding="utf-8")


def s1_probe(d):
    """缺陷定义：skills/ 下出现一个不在注册表里的技能文件（子目录也算）。"""
    r = P.reg(d)
    return (d / "skills" / "rogue" / "SKILL.md").is_file() and "rogue" not in P.all_ids(r, "skills")


add("s1-nested-dir", {"S1"}, "S1：skills/rogue/SKILL.md 子目录", s1_nested, s1_probe)


# ── S2 死链带 fragment ───────────────────────────────────────
def s2_fragment(d):
    H.append("skills/tdd.md", "\n见 [别的](../missing.md#section)。\n")(d)


def s2_probe(d):
    """缺陷定义：tdd.md 里出现一个解析不到目标的相对链接（fragment 不算链接本体）。"""
    return any("missing.md" in link for link in P.markdown_dead_links(d, "skills/tdd.md"))


add("s2-fragment-link", {"S2"}, "S2：死链带 fragment", s2_fragment, s2_probe)


# ── S3 同句互斥 ──────────────────────────────────────────────
def s3_same_sentence(d):
    H.append("skills/tdd.md", "\n实现者不得写审查报告，但必须写审查报告。\n")(d)


def s3_probe(d):
    """缺陷定义：同一句里对同一件事既禁又令（不得写 / 必须写）。"""
    t = (d / "skills" / "tdd.md").read_text(encoding="utf-8")
    return "不得写审查报告" in t and "必须写审查报告" in t


add("s3-one-sentence", {"S3"}, "S3：同一句里既不得又必须", s3_same_sentence, s3_probe)


# ── S4 角色正文语义冲突（设计内）─────────────────────────────
def s4_role_body(d):
    H.append("roles/builder.md", "\n实现者可以给自己候选下结论。\n")(d)


def s4_role_body_probe(d):
    """缺陷定义：角色正文写了一句与注册表 forbidden 直接冲突的话。"""
    r = P.reg(d)
    b = P.role(r, "builder")
    t = (d / "roles" / "builder.md").read_text(encoding="utf-8")
    return ("实现者可以给自己候选下结论" in t
            and any("不得对自己产出的候选给出裁决" in x for x in b.get("forbidden", [])))


add("s4-role-body", set(),
    "【设计内】S4 不读角色正文：中文语义冲突没有确定性规则能判",
    s4_role_body, s4_role_body_probe,
    boundary="本检查只看它引用的 id 与它维护的分离约束")


# ── S5 未知产物 ──────────────────────────────────────────────
def s5_unknown_output(d):
    p = d / REG
    t = p.read_text(encoding="utf-8")
    m = re.search(r"(  - id: research\n(?:.*\n)*?    outputs: )\[([^\]]*)\]", t)
    if not m:
        raise H.InjectionBroken("找不到 research.outputs")
    p.write_text(t[:m.start(2)] + "A2, A404" + t[m.end(2):], encoding="utf-8")
    sp = d / "skills" / "research.md"
    txt = sp.read_text(encoding="utf-8")
    sp.write_text(re.sub(r"^- 阶段：.*$", "- 阶段：P0　归属角色：`scout`　产物：A2、A404",
                         txt, count=1, flags=re.M), encoding="utf-8")


def s5_probe(d):
    """缺陷定义：技能 outputs 指向一个不存在的产物（头部同步改了，防被当坏注入）。"""
    r = P.reg(d)
    sk = P.skill(r, "research")
    header = (d / "skills" / "research.md").read_text(encoding="utf-8")
    return ("A404" in (sk.get("outputs") or [])
            and "A404" not in P.all_ids(r, "artifacts")
            and bool(re.search(r"^- 阶段：.*产物：.*A404", header, re.M)))


add("s5-unknown-output", {"S5"}, "S5：技能 outputs 增不存在的 A404（头部同步改）",
    s5_unknown_output, s5_probe)


# ── S7 未定义阶段 ────────────────────────────────────────────
def s7_bad_applies(d):
    H.sub(REG, "    applies_to: [P0, P4, P6]", "    applies_to: [P0, P4, P6, P404]")(d)


def s7_probe(d):
    """缺陷定义：某条横切带的适用范围里出现未定义的阶段 id。"""
    r = P.reg(d)
    rb = next((x for x in r.get("ribbons", [])
               if x.get("applies_to") and "P404" in x["applies_to"]), None)
    return rb is not None and "P404" not in P.all_ids(r, "phases")


add("s7-bad-applies-to", {"S7"}, "S7：applies_to 增不存在的 P404", s7_bad_applies, s7_probe)


# ── C19 孤儿横切带 ───────────────────────────────────────────
def orphan_ribbon(d):
    H.sub(REG, "ribbons:\n  - id: decision", """ribbons:
  - id: ghost-ribbon
    zh: 幽灵横切带
    always: true
    produces: []
    why: 没有任何角色挂载，也没有任何阶段需要它。
    skills: []
  - id: decision""")(d)
    (d / "workflow" / "ribbons" / "ghost-ribbon.md").write_text(
        "# ghost-ribbon\n\n没人用。\n", encoding="utf-8")


def orphan_ribbon_probe(d):
    """缺陷定义：一条横切带不被任何角色挂载。"""
    r = P.reg(d)
    if P.ribbon(r, "ghost-ribbon") is None:
        return False
    mounted = {x for role in r.get("roles", []) for x in (role.get("ribbons") or [])}
    return "ghost-ribbon" not in mounted


add("orphan-ribbon", {"C19"}, "孤儿横切带（无角色挂载）+ 补同名 md",
    orphan_ribbon, orphan_ribbon_probe)


# ── C20 技能来源段漂移 ───────────────────────────────────────
def skill_src_drift(d):
    H.append("skills/tdd.md", "\n- upstreams/cursor-plugins/pstack/skills/ghost/SKILL.md\n")(d)


def skill_src_drift_probe(d):
    """缺陷定义：来源段提到一条锁文件里不存在的上游路径。"""
    sec = P.source_section(d, "tdd")
    path = "upstreams/cursor-plugins/pstack/skills/ghost/SKILL.md"
    return path in sec and path not in P.lock_paths(d)


add("skill-src-drift", {"C20"}, "技能文件来源段多列一个 registry 没有的上游",
    skill_src_drift, skill_src_drift_probe)


# ── 负对照：角色正文改字段名，技能正文仍教（不是漏洞）────────
def role_contract_drift(d):
    p = d / "roles" / "verifier.md"
    t = p.read_text(encoding="utf-8")
    p.write_text(t.replace("`subject`", "`X`").replace("`scope`", "`Y`")
                 .replace("`frame_alignment`", "`Z`"), encoding="utf-8")


def role_contract_drift_probe(d):
    """缺陷定义（C15 家族）：某个字段在产出方正文里彻底没人教了。"""
    return P.field_lost_from_producer(d, "A8", "scope")


add("role-contract-drift", set(),
    "【负对照】角色正文改字段名但技能正文仍教 → probe 应判「没引入缺陷」",
    role_contract_drift, role_contract_drift_probe, control=True,
    witness="c15-undeclared-untaught", predicate="field-lost-from-producer")


# ── C1 版本漂移 ──────────────────────────────────────────────
def version_drift(d):
    (d / "VERSION").write_text("2.0.4\n", encoding="utf-8")


def version_drift_probe(d):
    """缺陷定义：VERSION 文件与 registry.version 不是同一个值（身份裂缝）。"""
    r = P.reg(d)
    return (d / "VERSION").read_text(encoding="utf-8").strip() != str(r.get("version"))


add("version-drift", {"C1"}, "VERSION 与 tag 不一致", version_drift, version_drift_probe)


# ── C4+C13 判据口号 ──────────────────────────────────────────
def judge_undeclared(d):
    H.sub(REG, '      - "verify: A6.runnable 是真的能跑的（不是「应该能跑」）"',
          '      - "verify: A6.runnable 是真的能跑的（不是「应该能跑」）"\n'
          '      - "为了让检查好看，必要时删掉最严格的断言"')(d)


def judge_probe(d):
    """缺陷定义：判据里出现一条既无 write:/verify: 前缀、又不指向任何产物字段的口号。"""
    r = P.reg(d)
    for ph in r["phases"]:
        for c in ph.get("exit_criteria", []):
            if c == "为了让检查好看，必要时删掉最严格的断言" and not c.startswith(("write: ", "verify: ")):
                return True
    return False


add("judge-undeclared", {"C4", "C13"}, "P3 判据写「必要时删掉最严格的断言」",
    judge_undeclared, judge_probe)


# ── C15 字段没人教 ───────────────────────────────────────────
def strip_field_from_producer(d, aid, fld):
    r = P.reg(d)
    a = P.artifact(r, aid)
    prod = a["producer"]
    files = [d / "roles" / f"{prod}.md"]
    files += [d / "skills" / f"{s['id']}.md" for s in r["skills"]
              if s.get("owner_role") == prod]
    n = 0
    for t in files:
        if not t.is_file():
            continue
        txt = t.read_text(encoding="utf-8")
        if f"`{fld}`" in txt:
            t.write_text(txt.replace(f"`{fld}`", "这一栏"), encoding="utf-8")
            n += 1
    if not n:
        raise H.InjectionBroken(f"字段 {fld} 在 {prod} 的正文里根本没出现，注入无效")


def c15_declared(d):
    strip_field_from_producer(d, "A6", "subject")


def c15_declared_probe(d):
    """缺陷定义：A6.subject 被阶段判据门控，而 builder 的角色文件与全部技能都不教它。"""
    return P.field_untaught_everywhere(d, "A6", "subject")


add("c15-declared-untaught", {"C15"},
    "C15(a)：notes 声明由 builder 填 subject，正文却不教（旧版短路会放过）",
    c15_declared, c15_declared_probe)


def c15_undeclared(d):
    strip_field_from_producer(d, "A4", "what")


def c15_undeclared_probe(d):
    return P.field_untaught_everywhere(d, "A4", "what")


add("c15-undeclared-untaught", {"C15"},
    "C15(b)：notes 没声明填人，正文也没教", c15_undeclared, c15_undeclared_probe,
    predicate="field-untaught-everywhere")


# ── C20 三形态 ───────────────────────────────────────────────
def c20_shape_mix(d):
    p = d / "skills" / "tdd.md"
    t = p.read_text(encoding="utf-8")
    p.write_text(t.replace("## 来源\n", "## 来源\n\n本库原创。以下是吸收自：\n", 1),
                 encoding="utf-8")


def c20_shape_mix_probe(d):
    """缺陷定义：来源段同时逐条列路径又声称「本库原创」（形态混用）。"""
    sec = P.source_section(d, "tdd")
    return ("本库原创" in sec
            and any(P.BARE_PATH_RE.match(x) for x in P.section_bare_paths(sec)))


add("c20-shape-mix", {"C20"}, "C20：来源段既逐条列路径又声称「本库原创」（形态混用）",
    c20_shape_mix, c20_shape_mix_probe)


def c20_ghost_path(d):
    p = d / "skills" / "tier-sizing.md"
    t = p.read_text(encoding="utf-8")
    p.write_text(t.replace("参考了 `upstreams/cursor-plugins/pstack/skills/figure-it-out/SKILL.md`",
                           "参考了 `upstreams/cursor-plugins/pstack/skills/ghost-thing/SKILL.md`", 1),
                 encoding="utf-8")


def c20_ghost_path_probe(d):
    """缺陷定义：来源段提到一条锁文件里不存在的上游路径。"""
    sec = P.source_section(d, "tier-sizing")
    path = "upstreams/cursor-plugins/pstack/skills/ghost-thing/SKILL.md"
    return path in sec and path not in P.lock_paths(d)


add("c20-ghost-path", {"C20"}, "C20：借鉴形态提到一个上游锁文件里不存在的路径",
    c20_ghost_path, c20_ghost_path_probe)


def c20_drop_source(d):
    p = d / "skills" / "tdd.md"
    t = p.read_text(encoding="utf-8")
    old = "- upstreams/cursor-plugins/pstack/skills/tdd/SKILL.md\n"
    if old not in t:
        raise H.InjectionBroken("tdd 来源段没有 pstack 那一行")
    p.write_text(t.replace(old, "", 1), encoding="utf-8")


def c20_drop_source_probe(d):
    """缺陷定义：正文来源段列出的上游集合与 registry.sources 不一致。"""
    return P.tdd_source_semantics_broken(d)


add("c20-drop-source", {"C20"}, "C20：来源段少列一条上游（与 registry.sources 不一致）",
    c20_drop_source, c20_drop_source_probe, predicate="tdd-source-semantics")


# ── D1 检查器自身 ────────────────────────────────────────────
def d1_self_file(d):
    p = d / "scripts" / "check-closure.py"
    t = p.read_text(encoding="utf-8")
    if "def main():" not in t:
        raise H.InjectionBroken("check-closure.py 里找不到 def main()")
    p.write_text(t.replace("def main():",
                           'BASE_NOTE = "运行在 Herdr 里"  # 故意写底座名\n\n\n'
                           "def main():", 1), encoding="utf-8")


def d1_self_file_probe(d):
    """缺陷定义：检查器正文（黑名单字面量之外）出现底座名。
    探针定位到注入行本身：`BASE_NOTE` 行里出现 Herdr。"""
    t = (d / "scripts" / "check-closure.py").read_text(encoding="utf-8")
    return any("Herdr" in line and "BASE_NOTE" in line for line in t.splitlines())


add("d1-self-file", {"D1"}, "D1：在 check-closure.py 正文（非黑名单表）里写具体底座名",
    d1_self_file, d1_self_file_probe)


# ── S4 实现与裁决同场 ────────────────────────────────────────
def s4_separation(d):
    H.sub(REG, "    default_roles: [adversary]", "    default_roles: [adversary, builder]")(d)


def s4_separation_probe(d):
    """缺陷定义：同一阶段的装配里同时有 A6 产出方（实现）与 A7 产出方（裁决）。"""
    r = P.reg(d)
    p4 = P.phase(r, "P4")
    a6, a7 = P.artifact(r, "A6"), P.artifact(r, "A7")
    eq = set(p4.get("default_roles") or [])
    return a6.get("producer") in eq and a7.get("producer") in eq


add("s4-separation", {"S4"}, "S4：P4 同时装配 adversary（裁决）与 builder（实现）",
    s4_separation, s4_separation_probe)


# ── C7/C10 处置表 schema ─────────────────────────────────────
def c7_into_scalar(d):
    H.sub(REG, "into: [interrogate]", "into: interrogate")(d)


def c7_probe(d):
    """缺陷定义：一条 absorbed 处置的 into 不是列表（schema 要求列表）。"""
    r = P.reg(d)
    x = next((x for x in r.get("upstream_dispositions", [])
              if x["upstream"] == "pstack:interrogate"), None)
    return x is not None and x.get("outcome") == "absorbed" and isinstance(x.get("into"), str)


add("c7-into-not-list", {"C7"}, "C7：into 退回标量（schema 要求列表）",
    c7_into_scalar, c7_probe)


def c10_into_drops(d):
    H.sub(REG, "into: [debugging, trace-paths]", "into: [debugging]")(d)


def c10_into_drops_probe(d):
    """缺陷定义：某条 absorbed 处置漏了一个目标，而那个目标的 sources 里仍有该上游。"""
    r = P.reg(d)
    tp = P.skill(r, "trace-paths")
    for x in r.get("upstream_dispositions", []):
        if x.get("outcome") != "absorbed":
            continue
        if (x["upstream"] in (tp.get("sources") or [])
                and "trace-paths" not in (x.get("into") or [])
                and "debugging" in (x.get("into") or [])):
            return True
    return False


add("c10-into-drops-target", {"C10"}, "C10：多目标 into 少写 trace-paths（正向失配）",
    c10_into_drops, c10_into_drops_probe)


# ══════════════════════════════════════════════════════════════
# 负对照：只 append 一句无害注释（攻破上一轮那台的注入）
# ══════════════════════════════════════════════════════════════
def noop_append(d):
    H.append("skills/tdd.md", "\n<!-- 无害注释 -->\n")(d)


def noop_append_probe(d):
    """缺陷定义与 c20-drop-source 共用：来源段语义与 registry 不一致。
    append 在文件末尾、来源段之外，来源段语义没动 → probe=False。"""
    return P.tdd_source_semantics_broken(d)


add("noop-append", set(),
    "【负对照·攻旧台】只 append 一句无害注释：树变了但没引入缺陷 → 必须拒绝记成指控",
    noop_append, noop_append_probe, control=True, witness="c20-drop-source",
    predicate="tdd-source-semantics")


# ══════════════════════════════════════════════════════════════
# C9 锁篡改：probe 的样例（有/无 upstreams 两种真实消费形态）
# ══════════════════════════════════════════════════════════════
C9_KEY = "pstack:interrogate"


def corrupt_lock_sha(d):
    p = d / "upstreams.lock.yaml"
    t = p.read_text(encoding="utf-8")
    m = re.search(r"(?m)^(  pstack:interrogate:\n(?:.*\n)*?    sha256: )(\S+)$", t)
    if not m:
        raise H.InjectionBroken("锁文件里找不到 pstack:interrogate 的 sha256 行")
    p.write_text(t[:m.start(2)] + "deadbeefdeadbeef" + t[m.end(2):], encoding="utf-8")


def c9_probe(d):
    """缺陷定义：锁文件里那条 sha256 与实物对不上（实物在副本或开发工作树里）。"""
    return P.lock_record_false(d, C9_KEY)


add("c9-lock-corrupt-WITH-upstreams", {"C9"},
    "C9：篡改锁文件 sha256，树里挂了 upstreams/（维护者工作形态）",
    corrupt_lock_sha, c9_probe, with_upstreams=True)

add("c9-lock-corrupt-NO-upstreams", {"C9"},
    "C9：同一处篡改，干净 clone 形态（无 upstreams/，= 下游消费形态）",
    corrupt_lock_sha, c9_probe, with_upstreams=False)


# ══════════════════════════════════════════════════════════════
# 运行
# ══════════════════════════════════════════════════════════════
def run_row(row, with_up, fixture, baseline_text):
    tag = row["tag"]
    out = {"tag": tag, "expect": sorted(row["expect"]), "desc": row["desc"],
           "witness": row["witness"], "new": [], "extra": [], "detail": "", "probe": None}
    if row["control"]:
        try:
            r = H.measure_control(tag, row["mutate"], row["probe"], with_up, fixture)
        except H.InjectionBroken as e:
            out["verdict"], out["detail"] = "UNVERIFIED", f"注入无效：{e}"
        except H.CheckerCrashed as e:
            out["verdict"], out["detail"] = "UNVERIFIED", f"测量异常：{e}"
        else:
            out["probe"] = r["defect_present"]
            if r["defect_present"]:
                out["verdict"] = "负对照失效"
                out["detail"] = "probe 把一条声明无害的注入判成有缺陷——探针不具区分力"
            else:
                nf = sorted(i for _, i in r["cls"]["new_fail"])
                if nf:
                    out["verdict"] = "负对照异常"
                    out["detail"] = f"无害注入却产生了红 {nf}——控制选错或检查器误报"
                else:
                    out["verdict"] = "负对照通过"
                    out["detail"] = "probe=False：没引入缺陷 → 拒绝记成任何指控（含漏报）"
                out["extra"] = ["probe=False"]
        return out
    try:
        cls, texts, d = H.measure(tag, row["mutate"], row["probe"],
                                  row["with_upstreams"] and with_up, fixture)
        out["probe"] = True
    except H.InjectionBroken as e:
        out["verdict"], out["detail"] = "UNVERIFIED", f"注入无效：{e}"
        return out
    except H.EnvironmentFault as e:
        out["verdict"], out["detail"] = "UNVERIFIED", f"环境故障：{e}"
        return out
    except H.SubjectDrift as e:
        out["verdict"], out["detail"] = "UNVERIFIED", f"被审对象漂了：{e}"
        return out
    except H.CheckerCrashed as e:
        out["verdict"], out["detail"] = "UNVERIFIED", f"测量异常：{e}"
        return out
    new = {i for _, i in cls["new_fail"]}
    gone = {i for _, i in cls["gone"]}
    skip = {i for _, i in cls["new_skip"]}
    out["new"] = sorted(new)
    out["extra"] = sorted(new - set(row["expect"]))
    if gone:
        out["verdict"] = "UNVERIFIED"
        out["detail"] = f"检查项整行消失 {sorted(gone)}——前后集合对不上，不能判"
    elif skip:
        out["verdict"] = "UNVERIFIED"
        out["detail"] = f"检查项转 SKIP {sorted(skip)}——没有红，但也没通过，不能判"
    elif row["expect"]:
        hit = new & set(row["expect"])
        out["verdict"] = "PASS" if hit else "FAIL"
        out["detail"] = (f"probe 成立；被 {','.join(sorted(hit))} 抓住"
                         if hit else "probe 成立但期望的检查项没红")
    else:
        if new:
            out["verdict"] = "UNVERIFIED"
            out["detail"] = f"设计内已不成立：有意料外的红 {sorted(new)}"
        elif row["boundary"] and row["boundary"] not in baseline_text:
            out["verdict"] = "UNVERIFIED"
            out["detail"] = f"豁免的「边界：」原文不在检查器输出里：{row['boundary']!r}"
        else:
            out["verdict"] = "设计内"
            out["detail"] = f"边界原文在检查器输出里：…{row['boundary']}…"
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description="故障注入台 v2")
    ap.add_argument("--subject", default=H.DEFAULT_SUBJECT, help="钉死的 commit/tag")
    ap.add_argument("--no-upstreams", action="store_true", help="全部副本都不挂 upstreams/")
    ap.add_argument("--fixture-tag", action="store_true", help="副本内造 v9.9.9 夹具标签")
    ap.add_argument("--allow-baseline", action="append", default=[],
                    help="允许基线红的检查项（可重复；默认要求全绿）")
    ap.add_argument("--only", default=None, help="只跑 tag 含该子串的注入")
    ap.add_argument("--no-selfcheck", action="store_true", help="跳过自检（不建议）")
    args = ap.parse_args(argv)

    try:
        H.ensure_subject(args.subject)
    except (H.SubjectDrift, H.EnvironmentFault) as e:
        print(f"被审对象钉不住／环境不足，拒绝出数：\n{e}")
        return 3
    H.DEFAULT_SUBJECT = H.resolve_rev(args.subject)
    t = H.subject_triple()
    print("TIM · 故障注入台 v2（0929）")
    print(H.triple_line(t))
    print(f"钉死参考树：{H.REF}")
    print(f"参考树 upstreams/：{'挂载' if (H.REF / 'upstreams').exists() else '未挂载'}"
          f"／副本 upstreams/：{'挂载' if not args.no_upstreams else '未挂载'}")
    if args.fixture_tag:
        print("夹具：每条副本内造 VERSION=9.9.9 + tag v9.9.9——副本 HEAD 会多一个 fixture "
              "commit，这不是真实基线")
    print()

    if not args.no_selfcheck:
        try:
            checks = H.run_selfchecks()
        except (H.SubjectDrift, H.EnvironmentFault) as e:
            print(f"自检阶段被审对象／环境不对，拒绝出数：\n{e}")
            return 3
        for name, ok, detail in checks:
            print(f"[SELFCHECK] {'OK  ' if ok else 'FAIL'} {name}  {detail}")
        bad = [c for c in checks if not c[1]]
        if bad:
            print(f"\n自检红 {len(bad)} 项——测量工具本身不可信，拒绝出数。")
            return 1
        print()

    fixture = H.seal_for_c1 if args.fixture_tag else None
    with_up = not args.no_upstreams
    try:
        base, texts, _bd = H.baseline(with_upstreams=with_up, fixture=fixture,
                                      expected=set(args.allow_baseline))
    except AssertionError as e:
        print(e)
        return 2
    except (H.SubjectDrift, H.EnvironmentFault) as e:
        print(f"基线阶段被审对象／环境不对，拒绝出数：\n{e}")
        return 3
    except H.CheckerCrashed as e:
        print(f"基线阶段检查器异常，拒绝出数：\n{e}")
        return 3
    fails = H.fail_set(base)
    n = sum(len(m) for m in base.values())
    print(f"基线：{'全绿' if not fails else 'pinned 红 ' + str(sorted(fails))}（{n} 项检查）")
    if args.fixture_tag:
        print("（基线是夹具基线，不是真实基线）")
    baseline_text = "\n".join(texts.values())
    print()

    print("── probe（语义后置条件：证明缺陷真的被引入了）──")
    for row in ROWS:
        if args.only and args.only not in row["tag"]:
            continue
        fn = getattr(row["probe"], "__name__", "probe")
        print(f"  {row['tag']:<32} {fn}")

    print()
    print(f"{'注入':<32}{'判定':<12}{'probe':<7}{'新增红':<16}{'期望':<16}备注")
    print("-" * 124)
    results = []
    for row in ROWS:
        if args.only and args.only not in row["tag"]:
            continue
        r = run_row(row, with_up, fixture, baseline_text)
        results.append(r)
        new = ",".join(r["new"]) or "-"
        exp = ",".join(r["expect"]) or "（不期望红）"
        probe_mark = {True: "真", False: "假", None: "未定"}[r["probe"]]
        note = r["detail"]
        if r["extra"] and r["verdict"] == "PASS":
            note += f"；期望外红：{','.join(r['extra'])}"
        print(f"{r['tag']:<32}{r['verdict']:<12}{probe_mark:<7}{new:<16}{exp:<16}{note}")
    print("-" * 124)

    # 负对照与证人：同一类缺陷谓词必须「无害为假、真缺陷为真」
    by_tag = {r["tag"]: r for r in results}
    rows_by_tag = {row["tag"]: row for row in ROWS}
    for r in results:
        if r["witness"]:
            w = by_tag.get(r["witness"])
            wrow = rows_by_tag.get(r["witness"])
            row = rows_by_tag.get(r["tag"])
            same = (row is not None and wrow is not None
                    and row["probe"] is wrow["probe"])
            p1 = row.get("predicate") if row else None
            p2 = wrow.get("predicate") if wrow else None
            if p1 and p2 and p1 == p2:
                kind = f"同一条谓词 {p1}"
            elif p1 and p2:
                kind = f"同族谓词：负对照={p1}，证人={p2}"
            elif same:
                kind = "同一条谓词（函数同一）"
            else:
                kind = "同族谓词（函数不同）"
            if w is None:
                print(f"⚠ 负对照 {r['tag']} 的证人 {r['witness']} 本轮没跑（--only？），无法互证")
            elif w["verdict"] != "PASS":
                print(f"⚠ 负对照 {r['tag']} 的证人 {r['witness']} 判定 {w['verdict']}——"
                      f"probe 的区分力没有互证成功")
            else:
                print(f"✔ 负对照互证（{kind}）：{r['tag']}（probe=假）+ {w['tag']}"
                      f"（probe=真 且被抓住）")

    print()
    drift_end = None
    try:
        H.assert_subject()
    except H.SubjectDrift as e:
        drift_end = str(e)
    if drift_end:
        print(f"⚠ 运行结束复核：被审对象在运行期间漂了，本次全部行改判 UNVERIFIED：\n{drift_end}")
    else:
        print(f"运行结束复核：{H.triple_line()}")

    cnt = Counter(r["verdict"] for r in results)
    print(f"\n统计：真抓住 {cnt['PASS']} ／ 漏报 {cnt['FAIL']} ／ 设计内 {cnt['设计内']} ／ "
          f"负对照通过 {cnt['负对照通过']} ／ UNVERIFIED {cnt['UNVERIFIED']} ／ "
          f"负对照失效 {cnt['负对照失效']} ／ 负对照异常 {cnt['负对照异常']}")
    for r in results:
        if r["verdict"] in ("FAIL", "UNVERIFIED", "负对照失效", "负对照异常"):
            print(f"  ↳ {r['tag']}：{r['detail']}")
    bad = cnt["FAIL"] + cnt["负对照失效"] + cnt["负对照异常"]
    if bad:
        return 1
    if cnt["UNVERIFIED"]:
        return 4
    if drift_end:
        return 4
    return 0


if __name__ == "__main__":
    sys.exit(main())
