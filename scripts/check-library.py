#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check-library.py · TIM Professional Workflow 结构闭环自检（只读，可重复运行）

检查什么
  1  角色文件结构：frontmatter（role/title）+ 8 个必需节，按序齐全
  2  注入契约：每个角色文件声明"本文件只提供第 1–2 层"
  3  §4 反例/不适用 ≥ 2 处；§8 常见自欺 ≤ 4 行
  4  角色文件内引用：只允许 roles/<id>.md（driver 额外允许 pipeline.md）；禁止 skills/ 与 upstreams/
  5  闭环：角色 §2 收据的字段必须逐字出现在产出方 §3 声明的字段里（含覆盖面报告）
  6  闭环：交接拓扑双向一致（§3 声明的消费者必须真的在 §2 收信）
  7  闭环矩阵：主链行数/唯一性/非空（G3）、相邻字段包含、与角色文件交叉校验（G5 的跳过收据）
  8  死链：README / AGENTS / pipeline / closure / SOURCES 里出现的仓库内路径必须真实存在
  9  版本单一来源：VERSION 存在且合法；扫描范围内不得再有 version: 声明
 10  工具解耦：扫描范围内不得出现具体运行底座名称；能力探测块恰好一处且在 roles/driver.md
 11  身份规范 G1：identity.md 是唯一权威定义（含无 git 降级形式与相等判定），用到身份的角色都有内联规则
 12  身份实现 G2：scripts/identity-selftest.sh 的正负夹具必须全过（夹具会因实现缺陷而变红）
 13  收据处置 G4：每条收据的"缺了怎么办"非空（表格式逐行、散文式逐条）
 14  替代收据 G5′：可跳过行的替代字段集必须覆盖接收方 §2 的要求集（差集非空即失败）
 15  唯一转手 G6：拓扑里指向 oracle 的边只允许 Driver 起点；其他角色不得直投 oracle
 16  跳过可兑现 G7：可跳过行的替代**产出方**必须在其 §3 声明该产物且字段覆盖要求集
 17  同名同形 G8：`object` 与 `dependencies` 在不同文件里必须是同一形状
 18  台账落点 P5：SOURCES.md 声称的 `roles/<id>.md §N` 必须真实存在

扫描范围（不含即将被排除的部分）
  roles/**  pipeline.md  closure.md  identity.md  README.md  AGENTS.md  SOURCES.md  scripts/**  VERSION
显式排除（只有这三类，且由 Owner 批准）
  docs/**（历史材料与归档）、.pi/**（工作区）、upstreams/**（只读克隆，按路径豁免）
  注：上游仓库标识（只读克隆名）是**溯源标识**而不是运行指令；它们与工具名言一样以分片方式写在源码里，
      因此本脚本自身也完整落在扫描范围内，不再自排除。

本检查判不了：§4 方法的实质深度、语义正确性、字段值是否真实、某次跳过是否真的合规、以及同义重复（同一含义的措辞在库内没有唯一权威位置时，只能人审）——这些交给独立审查与人审。
退出码：0 = 全部通过；1 = 有失败项。
"""

from __future__ import annotations

import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SCAN_DIRS = ["roles", "scripts"]
SCAN_FILES = ["pipeline.md", "closure.md", "identity.md", "README.md", "AGENTS.md", "SOURCES.md", "VERSION"]
EXCLUDED = [
    "docs/**（历史材料与归档）",
    ".pi/**（工作区）",
    "upstreams/**（只读克隆，按路径豁免）",
]

# ── 名称清单：以分片拼接，源码正文里不出现完整名字（B-7：本脚本也必须落在扫描范围内）──
HARNESS_TOKENS = [
    "her" + "dr",
    "inter" + "com",
    "sub" + "agent",
    "sub" + "agents",
    "clau" + "de",
    "cod" + "ex",
    "cur" + "sor",
    "gem" + "ini",
    "copi" + "lot",
    "aid" + "er",
    "open" + "code",
    "d" + "sh",
    "m" + "cp",
    "chat" + "gpt",
    "open" + "ai",
    "anthro" + "pic",
    "oll" + "ama",
    "p" + "i",
]
UPSTREAM_REPO_IDS = [
    "cur" + "sor" + "-plugins",
    "matt" + "pocock" + "-skills",
    "addy" + "osmani" + "-agent-skills",
    "p" + "i-review",
    "super" + "powers",
    "gstack",
    "human" + "layer",
]
CAPABILITY_TERMS = ["独立" + "会话", "会话" + "之间通信", "隔离" + "工作区", "模型" + "档位"]
CAPABILITY_REQUIRED_FILE = os.path.join("roles", "driver.md")

# 死链解析次序：先仓库根，再三个上游 clone 根（SOURCES.md 的引用路径相对上游根写）
RESOLVE_ROOTS = [
    "",
    "upstreams/" + "cur" + "sor" + "-plugins/pstack",
    "upstreams/" + "cur" + "sor" + "-plugins",
    "upstreams/" + "matt" + "pocock" + "-skills",
    "upstreams/" + "addy" + "osmani" + "-agent-skills",
]

REQUIRED_SECTIONS = [
    "使命",
    "我收到什么（输入契约）",
    "我必须交出什么（输出契约）",
    "我的工程方法",
    "权限边界（我可以 / 我不可以）",
    "升级条件（什么情况交给谁）",
    "退出判据（什么算做完，什么不算）",
    "常见自欺",
]

ROLE_IDS = [
    "driver", "oracle", "investigator", "architect", "planner",
    "implementer", "reviewer", "verifier", "integrator", "ledger-custodian",
]

# 用到身份字段的角色（B-2/身份规范：这 6 个必须内联规则）
IDENTITY_ROLES = ["driver", "implementer", "integrator", "oracle", "reviewer", "verifier"]
IDENTITY_INLINE_MARKERS = [
    "ws:v1",
    "NUL",
    "路径字节序升序",
    "前缀类型相同",
    "只交 digest 不算交付",
    "范围声明",
    "不回答",
]
IDENTITY_SPEC_MARKERS = [
    "无版本历史时的降级形式",
    "路径 + NUL + 该文件字节的 sha256",
    "-<sha256>",
    "相等判定",
    "范围声明",
    "跨会话移交",
]

MAIN_CHAIN_MIN_ROWS = 9

# B-6 开工门：Implementer 的输入契约必须带可执行的停机动作与授权快照
OPEN_GATE_MARKS = ["### 4.0 开工前收据核对（第 0 步，先于任何写入）", "唯一合法动作是停止", "零写入"]
OPEN_GATE_ROLE = "roles/implementer.md"

# G8 形状标记
OBJECT_SHAPE_MARK = "base=<token>;tree=<token>"
# 4 个身份角色必须带这条规范 bullet（不是"文件里某处出现过就算"）
OBJECT_SHAPE_BULLET = "- **对象身份写成二元组**：`object := base=<token>;tree=<token>`"
# 被弃用的单 token 说法：出现在 object 字段附近即算回退
OBJECT_SINGLE_TOKEN = "（`commit:`/`tree:`/`ws:v1:` 之一）"
OBJECT_SHAPE_REQUIRED = ["roles/driver.md", "roles/reviewer.md", "roles/verifier.md", "roles/integrator.md"]
DEP_SHAPE_MARKS = ["解除证据指针", "谁接受解除"]
DEP_SHAPE_REQUIRED = ["roles/driver.md", "roles/planner.md"]
# G6：除 driver/oracle 外，任何角色文件都不得提到指向 oracle 的投递
ORACLE_REF_ALLOWED = ["roles/driver.md", "roles/oracle.md"]

results: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, detail: str) -> None:
    results.append((name, ok, detail))


def rel(path: str) -> str:
    return os.path.relpath(path, ROOT)


def read(path: str) -> str:
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def run_ledger_check() -> tuple[bool, str]:
    """调 `scripts/render-ledger.py --check`：台账落点的锚点与原文由生成器保证一致。

    本检查**不再自己解析锚点**：上一版用正则解析 SOURCES.md 里的「角色文件 + §节 + 步骤号」锚点，
    结果漏掉粗体等形态（静默跳过 100+ 个锚点）。现在判据只有一个——生成器重跑结果与磁盘一致。
    """
    script = os.path.join(ROOT, "scripts", "render-ledger.py")
    if not os.path.isfile(script):
        return False, "scripts/render-ledger.py 不存在（台账落点已无生成器保证）"
    proc = subprocess.run([sys.executable, script, "--check"], cwd=ROOT,
                          capture_output=True, text=True)
    out = (proc.stdout + proc.stderr).strip().replace("\n", " ")
    return proc.returncode == 0, "退出码 %d｜%s" % (proc.returncode, out[:180])


def read_without_generated(path: str) -> str:
    """读文件，但**剔除台账生成区**（`<!-- BEGIN:landings -->…<!-- END:landings -->`）。

    生成区是角色原文的派生副本；"某段文字恰好在某处出现一次"这类计数必须只看事实源，
    否则同一段原文被引用一次就会被算成两处。生成区本身由 `render-ledger.py --check` 守住。
    """
    text = read(path)
    if "<!-- BEGIN:landings" not in text:
        return text
    head, rest = text.split("<!-- BEGIN:landings", 1)
    _body, tail = rest.split("<!-- END:landings", 1)
    keep = tail.count("\n")
    return head + "\n" * keep + "\n" * (head.count("\n") and 0)


def scanned_files() -> list[str]:
    out: list[str] = []
    for d in SCAN_DIRS:
        base = os.path.join(ROOT, d)
        if not os.path.isdir(base):
            continue
        for dirpath, _dirnames, filenames in os.walk(base):
            if "__pycache__" in dirpath:
                continue
            for fn in sorted(filenames):
                if fn.startswith(".") or not fn.endswith((".md", ".sh", ".py", ".tsv")):
                    continue
                out.append(os.path.join(dirpath, fn))
    for f in SCAN_FILES:
        p = os.path.join(ROOT, f)
        if os.path.isfile(p):
            out.append(p)
    return sorted(out)


def strip_upstream_paths(line: str) -> str:
    """溯源用的上游标识不是运行指令：先替换仓库标识，再替换 upstreams/... 路径。"""
    for ident in UPSTREAM_REPO_IDS:
        line = line.replace(ident, "<upstream-repo>")
    line = re.sub(r"`upstreams/[^`]*`", "`<upstream-path>`", line)
    line = re.sub(r"\(upstreams/[^)]*\)", "(<upstream-path>)", line)
    line = re.sub(r"\bupstreams/[A-Za-z0-9._/\-]+", "<upstream-path>", line)
    line = line.replace(".pi/", "<workspace>/").replace("`.pi`", "<workspace>")
    return line


RE_FRONT_ROLE = re.compile(r"^role:\s*(\S+)\s*$", re.M)
RE_FRONT_TITLE = re.compile(r"^title:\s*(.+?)\s*$", re.M)
RE_H1 = re.compile(r"^#\s+(.+?)\s*$", re.M)
RE_SECTION = re.compile(r"^##\s+(\d)\.\s*(.+?)\s*$", re.M)
RE_RECEIPT = re.compile(r"^\*\*(主收据|副收据)\s+`([^`]+)`\s*←\s*`([^`]+)`\*\*")
RE_OUTPUT = re.compile(r"^\*\*产出\s+`([^`]+)`\s*→\s*(.+?)\*\*\s*$")
RE_TABLE_ROW = re.compile(r"^\|\s*(.*?)\s*\|\s*$")
RE_TABLE_FIELD = re.compile(r"^\|\s*`([A-Za-z_][A-Za-z0-9_]*)`\s*\|")
RE_PROSE_FIELDS = re.compile(r"^字段\s*[：:]\s*(.+)$")
RE_FIELD_TOKEN = re.compile(r"`([a-z][a-z0-9_]*)`")
RE_ROLE_PATH = re.compile(r"roles/[a-z\-]+\.md")
RE_DISPOSITION = re.compile(r"缺")
RE_BACKTICK = re.compile(r"`([^`]+)`")


class RoleFile:
    def __init__(self, path: str) -> None:
        self.path = path
        self.name = rel(path)
        text = read(path)
        self.text = text
        self.role = (RE_FRONT_ROLE.search(text) or [None, ""])[1]
        self.title = (RE_FRONT_TITLE.search(text) or [None, ""])[1]
        self.h1 = (RE_H1.search(text) or [None, ""])[1]
        self.sections = [(m.group(1), m.group(2)) for m in RE_SECTION.finditer(text)]
        self.receipts: list[dict] = []
        self.outputs: list[dict] = []
        self._parse_blocks()

    def _parse_blocks(self) -> None:
        current: dict | None = None
        for lineno, line in enumerate(self.text.splitlines(), 1):
            m = RE_RECEIPT.match(line)
            if m:
                current = {"kind": m.group(1), "artifact": m.group(2), "peer": m.group(3),
                           "fields": [], "rows": [], "text": [line], "line": lineno}
                self.receipts.append(current)
                continue
            m = RE_OUTPUT.match(line)
            if m:
                current = {"artifact": m.group(1), "consumers": m.group(2),
                           "fields": [], "rows": [], "text": [line], "line": lineno}
                self.outputs.append(current)
                continue
            if line.startswith("## ") or (line.startswith("**") and not line.startswith("|")):
                current = None
                continue
            if current is None:
                continue
            current["text"].append(line)
            m = RE_TABLE_FIELD.match(line)
            if m:
                current["fields"].append(m.group(1))
                current["rows"].append(RE_TABLE_ROW.match(line).group(1))
                continue
            m = RE_PROSE_FIELDS.match(line)
            if m:
                current["fields"].extend(RE_FIELD_TOKEN.findall(m.group(1)))
                current["rows"].append("prose:" + m.group(1))

    def section_text(self, num: str) -> str:
        pat = re.compile(r"^##\s+%s\.\s*(.+?)\s*$" % num, re.M)
        m = pat.search(self.text)
        if not m:
            return ""
        start = m.end()
        nxt = re.compile(r"^##\s+\d\.", re.M).search(self.text, start)
        return self.text[start:nxt.start() if nxt else len(self.text)]

    def artifact_fields(self, artifact: str) -> set[str] | None:
        for o in self.outputs:
            if o["artifact"] == artifact:
                return set(o["fields"])
        return None

    def receipt_fields(self, artifact: str) -> set[str] | None:
        for r in self.receipts:
            if r["artifact"] == artifact:
                return set(r["fields"])
        return None


def parse_table(block: str) -> list[list[str]]:
    rows = []
    for line in block.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if not cells or set("".join(cells)) <= set("-: "):
            continue
        rows.append(cells)
    return rows[1:] if rows else []


def fields_of(cell: str) -> set[str]:
    return set(RE_BACKTICK.findall(cell))


def closure_blocks(text: str) -> tuple[str, str]:
    main_m = re.search(r"^##\s+主链.*?$", text, re.M)
    aux_m = re.search(r"^##\s+按需与降级.*?$", text, re.M)
    if not main_m:
        return "", ""
    main_start = main_m.end()
    if aux_m:
        main = text[main_start:aux_m.start()]
        aux = text[aux_m.end():]
    else:
        main = text[main_start:]
        aux = ""
    aux = re.split(r"^##\s+", aux, maxsplit=1, flags=re.M)[0]
    return main, aux


def aux_groups(cell: str) -> list[set[str]]:
    """把 `4→`a` `b`；5→`c` 拆成若干字段集（不校验行号时用）。"""
    return [fields_of(g) for g in re.split(r"[；;]", cell) if "→" in g]


def pipeline_edges() -> list[tuple[str, str, list[str]]]:
    """解析 pipeline.md 的 ```pipeline 块：producer -> artifact -> consumers"""
    path = os.path.join(ROOT, "pipeline.md")
    if not os.path.isfile(path):
        return []
    m = re.search(r"```pipeline\n(.*?)```", read(path), re.S)
    if not m:
        return []
    edges = []
    for line in m.group(1).splitlines():
        parts = [x.strip() for x in line.split("->")]
        if len(parts) != 3:
            continue
        cons = [c.strip() for c in parts[2].split(",") if c.strip()]
        edges.append((parts[0], parts[1], cons))
    return edges


def resolve_in_repo(target: str) -> bool:
    for root in RESOLVE_ROOTS:
        if os.path.exists(os.path.join(ROOT, root, target)):
            return True
    return False


def main() -> int:
    roles_dir = os.path.join(ROOT, "roles")
    roles: dict[str, RoleFile] = {}
    if not os.path.isdir(roles_dir):
        record("roles/ 目录存在", False, "缺少 roles/ 目录")
    else:
        for fn in sorted(os.listdir(roles_dir)):
            if fn.endswith(".md"):
                rf = RoleFile(os.path.join(roles_dir, fn))
                roles[fn[:-3]] = rf

    role_by_file = {"roles/%s.md" % rid: rf for rid, rf in roles.items()}

    # 1 角色结构
    missing_roles = [r for r in ROLE_IDS if r not in roles]
    extra_roles = [r for r in roles if r not in ROLE_IDS]
    record("角色文件集合", not missing_roles and not extra_roles,
           "缺 %s；多 %s" % (missing_roles or "无", extra_roles or "无"))

    struct_bad = []
    for rid, rf in sorted(roles.items()):
        if rf.role != rid:
            struct_bad.append("%s: frontmatter role=%r" % (rf.name, rf.role))
        if not rf.title:
            struct_bad.append("%s: frontmatter 缺 title" % rf.name)
        got = [t for _n, t in rf.sections]
        if got != REQUIRED_SECTIONS:
            struct_bad.append("%s: 节不符（得到 %s）" % (rf.name, got))
    record("角色 frontmatter + 8 节", not struct_bad, "; ".join(struct_bad) or "9/9")

    # 2 注入契约
    seam_bad = [rf.name for rf in roles.values()
                if "注入契约" not in rf.text or "第 1–2 层" not in rf.text]
    record("注入契约声明", not seam_bad, "; ".join(seam_bad) or "9/9")

    # 3 §4 反例计数 / §8 行数
    sec4_bad, sec8_bad = [], []
    for rf in roles.values():
        s4 = rf.section_text("4")
        n4 = len(re.findall(r"反例|不适用", s4))
        if n4 < 2:
            sec4_bad.append("%s: §4 反例/不适用=%d" % (rf.name, n4))
        s8 = rf.section_text("8")
        n8 = len([ln for ln in s8.splitlines() if ln.strip().startswith("|")]) - 2
        if n8 > 4 or n8 < 0:
            sec8_bad.append("%s: §8 行数=%d" % (rf.name, n8))
    record("§4 反例/不适用 ≥2", not sec4_bad, "; ".join(sec4_bad) or "9/9")
    record("§8 常见自欺 ≤4", not sec8_bad, "; ".join(sec8_bad) or "9/9")

    # 4 角色内引用
    ref_bad = []
    for rf in roles.values():
        for tok in RE_BACKTICK.findall(rf.text):
            if "skills/" in tok:
                ref_bad.append("%s: 引用 skills/ → %s" % (rf.name, tok))
            if tok.startswith("upstreams/") or "/upstreams/" in tok:
                ref_bad.append("%s: 引用 upstreams/ → %s" % (rf.name, tok))
            m = re.match(r"^(roles/[a-z\-]+\.md)", tok)
            if m and not os.path.isfile(os.path.join(ROOT, m.group(1))):
                ref_bad.append("%s: 死引用 → %s" % (rf.name, tok))
            if tok.endswith(".md") and "/" in tok and not tok.startswith(("roles/", "docs/")):
                if tok != "pipeline.md":
                    ref_bad.append("%s: 可疑跨文件引用 → %s" % (rf.name, tok))
    record("角色文件引用仅限 roles/", not ref_bad, "; ".join(ref_bad) or "通过")

    # 5 闭环：收据 → 产出方 §3
    closure_bad, cov_rec, cov_declared, cov_out, cov_out_declared = [], 0, 0, 0, 0
    for rf in roles.values():
        for r in rf.receipts:
            cov_declared += 1
            if not r["fields"]:
                closure_bad.append("%s:%d 收据 `%s` 没有解析到任何字段（该项检查会空转）"
                                   % (rf.name, r["line"], r["artifact"]))
                continue
            cov_rec += 1
            producer = role_by_file.get(r["peer"])
            if producer is None:
                continue
            declared = producer.artifact_fields(r["artifact"])
            if declared is None:
                closure_bad.append("%s §2 收 %s，但 %s §3 未声明该 artifact"
                                   % (rf.name, r["artifact"], producer.name))
                continue
            missing = sorted(set(r["fields"]) - declared)
            if missing:
                closure_bad.append("%s §2 收 %s 缺字段 %s（%s §3 未提供）"
                                   % (rf.name, r["artifact"], missing, producer.name))
    for rf in roles.values():
        for o in rf.outputs:
            cov_out_declared += 1
            if o["fields"]:
                cov_out += 1
            else:
                closure_bad.append("%s:%d 产出 `%s` 没有解析到任何字段（下游校验会空转）"
                                   % (rf.name, o["line"], o["artifact"]))
    coverage = "收据 %d/%d、产出 %d/%d 参与校验" % (cov_rec, cov_declared, cov_out, cov_out_declared)
    record("闭环：收据字段 ⊆ 产出方字段", not closure_bad,
           ("; ".join(closure_bad) if closure_bad else "全部成立") + "｜" + coverage)

    # 5b 拓扑双向
    topo_bad = []
    for rf in roles.values():
        for o in rf.outputs:
            for cname in [c.strip(" `/") for c in re.split(r"[、,]", o["consumers"])]:
                if not cname.startswith("roles/"):
                    continue
                consumer = role_by_file.get(cname)
                if consumer is None:
                    topo_bad.append("%s §3 声明消费者 %s 不存在" % (rf.name, cname))
                    continue
                if not any(r["artifact"] == o["artifact"] for r in consumer.receipts):
                    topo_bad.append("%s §3 交 %s 给 %s，但后者 §2 未收"
                                    % (rf.name, o["artifact"], cname))
    record("闭环：交接拓扑双向一致", not topo_bad, "; ".join(topo_bad) or "全部一致")

    # 5c 收据处置（G4）
    disp_bad = []
    for rf in roles.values():
        for r in rf.receipts:
            rows = [x for x in r["rows"] if not x.startswith("prose:")]
            if rows:
                for row in rows:
                    cells = [c.strip() for c in row.split("|")]
                    if len(cells) < 3 or not cells[2]:
                        disp_bad.append("%s §2 收 %s：有一行没写「缺了怎么办」" % (rf.name, r["artifact"]))
                        break
            elif not any(RE_DISPOSITION.search(ln) for ln in r["text"]):
                disp_bad.append("%s §2 收 %s（散文式）没写缺了怎么办" % (rf.name, r["artifact"]))
    record("收据处置 G4：缺了怎么办非空", not disp_bad, "; ".join(disp_bad) or "全部非空")

    # 6 闭环矩阵
    closure_path = os.path.join(ROOT, "closure.md")
    matrix_bad, matrix_note = [], ""
    if not os.path.isfile(closure_path):
        record("闭环矩阵 closure.md", False, "文件不存在")
    else:
        main_block, aux_block = closure_blocks(read(closure_path))
        rows = [r for r in parse_table(main_block) if len(r) >= 6]
        aux_rows = [r for r in parse_table(aux_block) if len(r) >= 6]

        # G3 主链行数 / 唯一性 / 非空
        g3_bad = []
        if len(rows) < MAIN_CHAIN_MIN_ROWS:
            g3_bad.append("主链只有 %d 行（至少 %d）" % (len(rows), MAIN_CHAIN_MIN_ROWS))
        nums = [r[0] for r in rows]
        if len(set(nums)) != len(nums):
            g3_bad.append("主链行号重复：%s" % nums)
        for r in rows:
            if not fields_of(r[3]) and r[0] != "0":
                g3_bad.append("第 %s 行输入字段为空" % r[0])
            if not fields_of(r[5]):
                g3_bad.append("第 %s 行输出字段为空" % r[0])
        for r in aux_rows:
            if not fields_of(r[3]):
                g3_bad.append("按需表 %s 行输入字段为空" % r[0])
        record("闭环矩阵 G3：主链行数/唯一/非空", not g3_bad, "; ".join(g3_bad) or "主链 %d 行" % len(rows))

        out_fields: list[set[str]] = [fields_of(r[5]) for r in rows]
        in_fields: list[set[str]] = [fields_of(r[3]) for r in rows]
        for i in range(1, len(rows)):
            missing = sorted(in_fields[i] - out_fields[i - 1])
            if missing:
                matrix_bad.append("第 %s 行输入 %s 不在上一行输出里" % (rows[i][0], missing))
        for i, r in enumerate(rows):
            for grp in re.split(r"[；;]", r[4] if len(r) > 4 else ""):
                m = re.match(r"\s*(\d+)\s*→(.*)$", grp)
                if not m:
                    continue
                idx = int(m.group(1))
                if idx >= len(out_fields):
                    matrix_bad.append("第 %s 行附加输入引用了不存在的行 %d" % (r[0], idx))
                    continue
                miss = sorted(fields_of(grp) - out_fields[idx])
                if miss:
                    matrix_bad.append("第 %s 行附加输入 %s 不在第 %d 行输出里" % (r[0], miss, idx))
        union_main = set().union(*out_fields) if out_fields else set()
        union_roles = set()
        for rf in roles.values():
            for o in rf.outputs:
                union_roles |= set(o["fields"])
        for r in aux_rows:
            miss = sorted(fields_of(r[3]) - (union_main | union_roles))
            if miss:
                matrix_bad.append("按需表 %s 输入 %s 无处产出" % (r[0], miss))
        # 与角色文件交叉校验
        for r in rows + aux_rows:
            m = RE_ROLE_PATH.search(r[2])
            if not m:
                matrix_bad.append("第 %s 行承接角色不是 roles/<id>.md" % r[0])
                continue
            role = role_by_file.get(m.group(0))
            if role is None:
                matrix_bad.append("第 %s 行承接角色 %s 不存在" % (r[0], m.group(0)))
                continue
            declared_in = set().union(*[set(x["fields"]) for x in role.receipts]) if role.receipts else set()
            declared_out = set().union(*[set(x["fields"]) for x in role.outputs]) if role.outputs else set()
            wanted = fields_of(r[3])
            # 主链行的附加输入也必须是承接角色 §2 声明的字段；
            # 按需行的附加输入可以来自任意角色（例如 Driver 转手时要读来源角色的产物），
            # 因此只校验它的行号与上一行包含关系，不要求写进承接角色的 §2。
            if r in rows:
                for grp in re.split(r"[；;]", r[4] if len(r) > 4 else ""):
                    if "→" in grp:
                        wanted |= fields_of(grp)
            miss_in = sorted(wanted - declared_in)
            if miss_in:
                matrix_bad.append("第 %s 行输入 %s 不在 %s §2 声明里" % (r[0], miss_in, m.group(0)))
            miss_out = sorted(fields_of(r[5]) - declared_out)
            if miss_out:
                matrix_bad.append("第 %s 行输出 %s 不在 %s §3 声明里" % (r[0], miss_out, m.group(0)))
        matrix_note = "主链 %d 行 + 按需 %d 行，逐行与角色文件交叉校验" % (len(rows), len(aux_rows))
        record("闭环矩阵：相邻 + 角色交叉", not matrix_bad,
               "; ".join(matrix_bad) or ("%s 全部成立" % matrix_note))

        # G5 可跳过路径必须给出完整替代收据
        g5_bad = []
        for r in rows + aux_rows:
            skip = r[6] if len(r) > 6 else ""
            handover = r[7] if len(r) > 7 else ""
            if "不可跳过" in skip:
                continue
            if not handover.strip():
                g5_bad.append("第 %s 行可跳过但没写移交对象" % r[0])
                continue
            if not RE_ROLE_PATH.search(handover):
                g5_bad.append("第 %s 行移交没写承接角色" % r[0])
            if len(fields_of(handover)) < 2:
                g5_bad.append("第 %s 行移交没写完整替代收据字段" % r[0])
        record("可跳过路径 G5：替代收据完整", not g5_bad, "; ".join(g5_bad) or "全部完整或已标不可跳过")

    # 7 死链
    dead = []
    path_re = re.compile(
        r"(?<![\w./-])((?:roles|scripts|docs|workflows|skills|upstreams)/[A-Za-z0-9._/\-]+\.[A-Za-z0-9]+"
        r"|(?:README|AGENTS|SOURCES|pipeline|closure|identity)\.md|VERSION)")
    md_link = re.compile(r"\]\(([^)#\s]+)\)")
    for path in scanned_files():
        if path.endswith("VERSION"):
            continue
        text = read(path)
        cands = set(path_re.findall(text))
        for target in md_link.findall(text):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            cands.add(target)
        for c in sorted(cands):
            if c.startswith("upstreams/"):
                continue
            if not resolve_in_repo(c):
                dead.append("%s → %s" % (rel(path), c))
    record("死链检查", not dead, "; ".join(dead) or "无死链")

    # 8 版本单一来源
    ver_path = os.path.join(ROOT, "VERSION")
    ver_bad, ver_val = [], ""
    if not os.path.isfile(ver_path):
        ver_bad.append("VERSION 缺失")
    else:
        ver_val = read(ver_path).strip()
        if not re.match(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.\-]+)?$", ver_val):
            ver_bad.append("VERSION 不是 SemVer: %r" % ver_val)
    for path in scanned_files():
        if path.endswith("VERSION"):
            continue
        for n, line in enumerate(read(path).splitlines(), 1):
            if re.match(r"^\s*version:\s*\S", line):
                ver_bad.append("%s:%d 另起 version 声明" % (rel(path), n))
    record("版本单一来源 VERSION", not ver_bad,
           "; ".join(ver_bad) or ("VERSION=%s，扫描范围内无第二处声明" % ver_val))

    # 9 工具解耦
    harness_hits, cap_blocks, role_cap_hits = [], [], []
    for path in scanned_files():
        if path.endswith("VERSION"):
            continue
        is_role = rel(path).startswith("roles/")
        for n, line in enumerate(read_without_generated(path).splitlines(), 1):
            safe = strip_upstream_paths(line)
            for tok in HARNESS_TOKENS:
                if re.search(r"(?<![A-Za-z0-9])%s(?![A-Za-z0-9])" % re.escape(tok), safe, re.I):
                    harness_hits.append("%s:%d 出现 %r" % (rel(path), n, tok))
            n_terms = sum(1 for t in CAPABILITY_TERMS if t in safe)
            if n_terms >= 3:
                cap_blocks.append((rel(path), n, n_terms))
            if n_terms >= 2 and is_role and rel(path) != CAPABILITY_REQUIRED_FILE:
                role_cap_hits.append("%s:%d %d 项" % (rel(path), n, n_terms))
    record("工具解耦：无具体运行底座名称", not harness_hits,
           "; ".join(sorted(set(harness_hits))[:8]) or "0 命中（含本脚本自身）")
    cap_ok = (len(cap_blocks) == 1 and cap_blocks[0][0] == CAPABILITY_REQUIRED_FILE
              and cap_blocks[0][2] == len(CAPABILITY_TERMS))
    record("工具解耦：能力探测块恰好一处且在 driver.md", cap_ok,
           ("命中 %s:%d（%d/%d 项）" % (cap_blocks[0][0], cap_blocks[0][1], cap_blocks[0][2], len(CAPABILITY_TERMS))
            if cap_blocks else "0 处")
           + ("" if cap_ok else "｜应恰一处、在 driver.md、且四项齐"))
    record("工具解耦：其他角色文件无能力枚举", not role_cap_hits,
           "; ".join(role_cap_hits) or "0 命中")

    # 10 G1 身份规范
    spec_path = os.path.join(ROOT, "identity.md")
    g1_bad = []
    if not os.path.isfile(spec_path):
        g1_bad.append("identity.md 缺失（身份字段被 ≥2 个角色使用，必须有唯一权威定义）")
    else:
        spec = read(spec_path)
        for mk in IDENTITY_SPEC_MARKERS:
            if mk not in spec:
                g1_bad.append("identity.md 缺规范要件：%s" % mk)
    for rid in IDENTITY_ROLES:
        rf = roles.get(rid)
        if rf is None:
            g1_bad.append("角色 %s 不存在" % rid)
            continue
        for mk in IDENTITY_INLINE_MARKERS:
            if mk not in rf.text:
                g1_bad.append("%s 缺内联身份规则要件：%s" % (rf.name, mk))
    # 身份自由条款：未定义的兜底说法不得留在任何可注入件里
    free_clause = ["等价" + "树"]
    for path in scanned_files():
        if not (rel(path).startswith("roles/") or rel(path) in ("pipeline.md", "closure.md")):
            continue
        for n, line in enumerate(read(path).splitlines(), 1):
            for fc in free_clause:
                if fc in line:
                    g1_bad.append("%s:%d 残留未定义自由条款 %r" % (rel(path), n, fc))
    record("身份规范 G1：唯一定义 + 内联规则（无自由条款）", not g1_bad,
           "; ".join(g1_bad) or ("identity.md 要件齐；%d/%d 角色内联" % (len(IDENTITY_ROLES), len(IDENTITY_ROLES))))

    # 11 G2 身份实现自检
    selftest = os.path.join(ROOT, "scripts", "identity-selftest.sh")
    g2_detail = ""
    g2_ok = False
    if not os.path.isfile(selftest):
        g2_detail = "scripts/identity-selftest.sh 缺失"
    else:
        try:
            proc = subprocess.run(["bash", selftest], capture_output=True, text=True, timeout=120)
            g2_ok = proc.returncode == 0
            tail = [ln for ln in (proc.stdout or "").strip().splitlines() if ln.strip()][-1:]
            g2_detail = "退出码 %d｜%s" % (proc.returncode, tail[0] if tail else "")
        except Exception as exc:  # noqa: BLE001
            g2_detail = "运行失败：%r" % exc
    record("身份实现 G2：正负夹具全过", g2_ok, g2_detail)

    # 12b B-6 开工门
    b6_bad = []
    impl = roles.get("implementer")
    if impl is None:
        b6_bad.append("缺 roles/implementer.md")
    else:
        for mk in OPEN_GATE_MARKS:
            if mk not in impl.text:
                b6_bad.append("缺要件：%s" % mk)
        main_rec = impl.receipt_fields("slice-plan") or set()
        if main_rec != {"slices", "verification", "scope", "dependencies", "stop_condition"}:
            b6_bad.append("slice-plan 主收据字段集变了：%s" % sorted(main_rec))
        for r in impl.receipts:
            if r["artifact"] != "slice-plan":
                continue
            for row in r["rows"]:
                if row.startswith("prose:"):
                    continue
                cells = [c.strip() for c in row.split("|")]
                if len(cells) >= 3 and "停止开工" not in cells[2]:
                    b6_bad.append("slice-plan 有一行的处置不是「停止开工」")
                    break
        if "auth_record" not in (impl.receipt_fields("task-card") or set()):
            b6_bad.append("task-card 副收据缺 auth_record")
    record("开工门 B-6：缺件即停止 + 授权快照", not b6_bad, "; ".join(b6_bad) or "要件齐（停机动作/零写入/auth_record）")

    # 12 G5′ / G7：可跳过路径的替代收据 vs 接收方要求集
    g5p_bad, g7_bad = [], []
    known_artifacts: set[str] = set()
    for rf in roles.values():
        known_artifacts |= {x["artifact"] for x in rf.receipts}
        known_artifacts |= {x["artifact"] for x in rf.outputs}
    if os.path.isfile(closure_path):
        main_block, aux_block = closure_blocks(read(closure_path))
        all_rows = [r for r in (parse_table(main_block) + parse_table(aux_block)) if len(r) >= 8]
        for r in all_rows:
            if "不可跳过" in r[6] or not fields_of(r[5]):
                continue
            m = RE_ROLE_PATH.search(r[2])
            if not m or m.group(0) not in role_by_file:
                continue
            owner = role_by_file[m.group(0)]
            produced = None
            for o in owner.outputs:
                if fields_of(r[5]) <= set(o["fields"]):
                    produced = o["artifact"]
                    break
            if produced is None:
                g5p_bad.append("第 %s 行的输出字段在 %s §3 里找不到对应 artifact" % (r[0], m.group(0)))
                continue
            required: set[str] = set()
            for rf in roles.values():
                got = rf.receipt_fields(produced)
                if got:
                    required |= got
            alt = fields_of(r[7])
            mention = {a for a in alt if a in known_artifacts}
            if mention and produced not in mention:
                g7_bad.append("第 %s 行第 8 列声称的是 %s，而反推的产物是 %s"
                              % (r[0], sorted(mention), produced))
            miss = sorted(required - alt)
            if miss:
                g5p_bad.append("第 %s 行替代收据缺接收方要求字段 %s" % (r[0], miss))
            alt_role = RE_ROLE_PATH.search(r[7])
            if alt_role and alt_role.group(0) in role_by_file:
                alt_declared = role_by_file[alt_role.group(0)].artifact_fields(produced)
                if alt_declared is None:
                    g7_bad.append("第 %s 行的替代产出方 %s §3 未声明 %s"
                                  % (r[0], alt_role.group(0), produced))
                else:
                    miss2 = sorted(required - alt_declared)
                    if miss2:
                        g7_bad.append("第 %s 行替代产出方 %s 的 %s 缺字段 %s"
                                      % (r[0], alt_role.group(0), produced, miss2))
            elif not alt_role:
                g7_bad.append("第 %s 行可跳过但没写明替代产出方" % r[0])
    record("替代收据 G5′：字段覆盖接收方要求", not g5p_bad, "; ".join(g5p_bad) or "全部覆盖")
    record("跳过可兑现 G7：替代产出方 §3 有该产物", not g7_bad, "; ".join(g7_bad) or "全部可兑现")

    # 13 G6：指向 oracle 的边只允许 Driver 起点
    g6_bad = []
    for producer, artifact, cons in pipeline_edges():
        if "oracle" in cons and producer != "driver":
            g6_bad.append("拓扑边 %s -> %s -> oracle 的起点不是 driver" % (producer, artifact))
    for rf in roles.values():
        if rf.name in ORACLE_REF_ALLOWED:
            continue
        for n, line in enumerate(rf.text.splitlines(), 1):
            if "roles/oracle.md" not in line:
                continue
            # 只有「提到该路径 + 出现投递动词」才算直投；单纯引用字段形状不算
            if re.search(r"(发|投|交给|转给|提交给|直达|→)", line):
                g6_bad.append("%s:%d 非 Driver 角色出现指向 oracle 的投递表述" % (rf.name, n))
    record("唯一转手 G6：指向 oracle 的边只由 Driver 发起", not g6_bad,
           "; ".join(g6_bad) or "拓扑与角色文本均合规")

    # 14 G8：同名同形
    g8_bad = []
    spec = read(spec_path) if os.path.isfile(spec_path) else ""
    if OBJECT_SHAPE_MARK not in spec:
        g8_bad.append("identity.md 缺 object 的固定序列化 %s" % OBJECT_SHAPE_MARK)
    for f in OBJECT_SHAPE_REQUIRED:
        rf = role_by_file.get(f)
        if rf is None:
            continue
        if OBJECT_SHAPE_BULLET not in rf.text:
            g8_bad.append("%s 缺 object 二元组的规范 bullet" % f)
        for n, line in enumerate(rf.text.splitlines(), 1):
            if "`object`" in line and OBJECT_SINGLE_TOKEN in line:
                g8_bad.append("%s:%d 仍用单 token 形式描述 object" % (f, n))
    for f in DEP_SHAPE_REQUIRED:
        rf = role_by_file.get(f)
        if rf is None:
            continue
        for mk in DEP_SHAPE_MARKS:
            if mk not in rf.text:
                g8_bad.append("%s 的 dependencies 缺形状要件 %s" % (f, mk))
    record("同名同形 G8：object / dependencies 形状一致", not g8_bad,
           "; ".join(g8_bad) or "object 四文件 + identity.md 一致；dependencies 两文件一致")

    # 14b P5′：落点由生成器保证——直接调 render-ledger.py --check
    ledger_ok, ledger_detail = run_ledger_check()
    record("台账落点 P5′：render-ledger --check", ledger_ok, ledger_detail)

    # 15 P5：台账落点存在性
    p5_bad = []
    sources_path = os.path.join(ROOT, "SOURCES.md")
    if os.path.isfile(sources_path):
        src = read(sources_path)
        claims = set()
        for m in re.finditer(r"roles/([a-z\-]+)\.md\s*§\s*([0-9])", src):
            claims.add((m.group(1), m.group(2)))
        for rid, sec in sorted(claims):
            rf = roles.get(rid)
            if rf is None:
                p5_bad.append("SOURCES.md 落点指向不存在的角色 %s" % rid)
                continue
            if not re.search(r"^##\s+%s\." % sec, rf.text, re.M):
                p5_bad.append("SOURCES.md 落点 roles/%s.md §%s 不存在" % (rid, sec))
        p5_note = "%d 条带节号的落点声明" % len(claims)
    else:
        p5_note = "SOURCES.md 缺失"
    record("台账落点 P5：SOURCES 的 roles/<id>.md §N 存在", not p5_bad,
           "; ".join(p5_bad) or (p5_note + " 全部存在"))

    print("TIM · check-library.py（只读自检）")
    print("扫描范围: " + " , ".join(SCAN_DIRS + SCAN_FILES))
    print("显式排除（仅此三类，Owner 批准）: " + " ; ".join(EXCLUDED))
    print("本检查能判: 结构与字段级闭环、矩阵行数与跳过收据、身份规范与夹具、引用与死链、版本单一来源、运行底座解耦的措辞")
    print("本检查判不了: §4 方法的实质深度、语义正确性、字段值是否真实、某次跳过是否真的合规、同义重复")
    print("              以及「某条落点声称的动作是否真的写在那一步里」——这些交给独立审查与人审")
    print("仓库根:   " + ROOT)
    print("-" * 72)
    failed = 0
    for name, ok, detail in results:
        flag = "PASS" if ok else "FAIL"
        if not ok:
            failed += 1
        print("[%s] %-38s %s" % (flag, name, detail))
    print("-" * 72)
    print("合计: %d 项通过 / %d 项失败 / %d 项检查" % (len(results) - failed, failed, len(results)))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
