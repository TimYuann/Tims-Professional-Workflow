"""与检查器实现无关的语义后置条件（probe）与独立判据。

probe(d) 回答一个问题：**这条注入要制造的缺陷，现在真的在这棵树里吗？**

它只读文件、自己解析，**不复用 scripts/ 里的任何代码**——拿被审对象的实现
去证明被审对象上真有缺陷，等于自证。这里的函数是「缺陷的定义」，不是
「检查器的输出」。

约定（三态纪律的一部分）：
  probe 返回 True  = 缺陷确在其中 → 测量可以继续，等检查器的判定。
  probe 返回 False = 这条注入没引入缺陷 → 判 UNVERIFIED（注入无效），
                     **绝不允许**记成「检查器漏报」。
"""
from __future__ import annotations

import hashlib
import re
from pathlib import Path

import yaml

# 开发工作树根：probe 用它做「实物参照」（upstreams/ 被 gitignore，不在 commit 里）
DEV_REPO = Path(__file__).resolve().parents[2]


# ── registry 读取 ────────────────────────────────────────────
def reg(d: Path) -> dict:
    return yaml.safe_load((d / "workflow" / "registry.yaml").read_text(encoding="utf-8"))


def artifact(r: dict, aid: str):
    return next((a for a in r.get("artifacts", []) if a["id"] == aid), None)


def phase(r: dict, pid: str):
    return next((p for p in r.get("phases", []) if p["id"] == pid), None)


def skill(r: dict, sid: str):
    return next((s for s in r.get("skills", []) if s["id"] == sid), None)


def role(r: dict, rid: str):
    return next((x for x in r.get("roles", []) if x["id"] == rid), None)


def ribbon(r: dict, rid: str):
    return next((x for x in r.get("ribbons", []) if x["id"] == rid), None)


def all_ids(r: dict, kind: str) -> set:
    return {x["id"] for x in r.get(kind, [])}


# ── 锁文件 ───────────────────────────────────────────────────
def lock(d: Path) -> dict:
    p = d / "upstreams.lock.yaml"
    return (yaml.safe_load(p.read_text(encoding="utf-8")) or {}).get("skills", {})


def lock_paths(d: Path) -> set:
    return {v["path"] for v in lock(d).values() if v.get("path")}


def lock_record_false(d: Path, key: str) -> bool:
    """C9 的语义：锁文件里这条 sha256 与**实物**对不上。

    实物优先看副本里的 upstreams/（挂了就是副本自己的），没挂就用开发工作树里的
    实物——锁文件本来就是为了在缺 upstreams/ 时仍能核对，而「假的 sha256」
    这个缺陷与场景无关：它相对于真实上游内容永远是假的。
    """
    ent = lock(d).get(key)
    if not ent:
        return False
    p = d / ent["path"]
    if not p.is_file():
        p = DEV_REPO / ent["path"]
    if not p.is_file():
        return False                      # 环境缺实物 → 探针无法判定，不算缺陷
    h = hashlib.sha256(p.read_bytes()).hexdigest()[:16]
    return h != ent["sha256"]


# ── 技能正文的「## 来源」段 ──────────────────────────────────
def source_section(d: Path, sid: str) -> str:
    t = (d / "skills" / f"{sid}.md").read_text(encoding="utf-8")
    m = re.search(r"^##\s+来源\s*$", t, re.M)
    if not m:
        return ""
    rest = t[m.end():]
    nxt = re.search(r"^##\s+", rest, re.M)
    return rest[:nxt.start()] if nxt else rest


def section_bare_paths(sec: str) -> list[str]:
    """来源段里逐条列出的裸路径行（形态 a）。"""
    return [l.strip().lstrip("-*").strip().strip("`").strip()
            for l in sec.splitlines() if l.strip()]


def tdd_source_semantics_broken(d: Path) -> bool:
    """C20 形态(a) 的语义：tdd 正文来源段列出的路径 ⇄ registry.sources。

    正文与注册表说的必须是同一件事。数量多一条、少一条都算「不一致」。
    """
    r = reg(d)
    sk = skill(r, "tdd")
    sec = source_section(d, "tdd")
    p2i = {v["path"]: k for k, v in lock(d).items() if v.get("path")}
    got = {p2i[x] for x in section_bare_paths(sec) if x in p2i}
    return got != set(sk.get("sources") or [])


# ── C15 的语义：字段被门控，但产出方正文再也不教它 ──────────
def producer_taught_files(d: Path, r: dict, producer: str) -> list[Path]:
    files = [d / "roles" / f"{producer}.md"]
    files += [d / "skills" / f"{s['id']}.md" for s in r.get("skills", [])
              if s.get("owner_role") == producer]
    return files


def field_lost_from_producer(d: Path, aid: str, fld: str) -> bool:
    """缺陷定义：产出方的角色文件与它拥有的全部技能正文里，再也找不到 `` `fld` ``。"""
    r = reg(d)
    a = artifact(r, aid)
    if a is None:
        return False
    taught = any(f.is_file() and f"`{fld}`" in f.read_text(encoding="utf-8")
                 for f in producer_taught_files(d, r, a.get("producer")))
    return not taught


def field_untaught_everywhere(d: Path, aid: str, fld: str) -> bool:
    """缺陷定义：该字段出现在某阶段退出判据里（被门控），
    而产出方的**角色文件与它拥有的全部技能**正文里再也找不到 `` `fld` ``。"""
    r = reg(d)
    gated = any(f"{aid}.{fld}" in c
                for ph in r.get("phases", []) for c in ph.get("exit_criteria", []))
    return gated and field_lost_from_producer(d, aid, fld)


# ── 链接与文本 ───────────────────────────────────────────────
def markdown_dead_links(d: Path, rel: str) -> list[str]:
    """文件里解析不到目标的相对链接（含带 fragment 的）。"""
    t = (d / rel).read_text(encoding="utf-8")
    missing = []
    for link in re.findall(r"\]\(([^)\s]+)\)", t):
        p = link.split("#", 1)[0].strip().strip("<>")
        if not p or re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", p):
            continue
        if not (d / Path(rel).parent / p).resolve().exists():
            missing.append(link)
    return missing


BARE_PATH_RE = re.compile(r"^upstreams/[A-Za-z0-9_./-]+/SKILL\.md$")

BASE_NAME_RE = re.compile(r"(?<![A-Za-z0-9-])herdr(?![-])", re.I)


def contains_base_name(text: str) -> bool:
    """D1 的语义谓词：文本里出现具体底座名（大小写不敏感）。"""
    return bool(BASE_NAME_RE.search(text))


def file_contains_base_name(d: Path, rel: str) -> bool:
    return contains_base_name((d / rel).read_text(encoding="utf-8"))
