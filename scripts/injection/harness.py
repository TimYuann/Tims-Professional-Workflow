#!/usr/bin/env python3
"""故障注入台 v2 · 0929

它测的是「检查器在坏输入上会不会红」。它自己也是被上一轮审出来的被审对象之一。

纪律（1–3 沿用，4–8 为本轮新增）：

  1. 基线不绿就不许测。          BASE 里任何一项红都要么修好、要么写进 expected 逐条说明。
  2. 只认「新增的红」。          after 里本来就有的红是基线噪声，不算这条注入的战果。
  3. 归因到具体检查项。          每条注入声明期望被哪几项抓住；红在别人身上不算抓住，
                                并且要单独把「期望外的红」打出来。
  4. 注入必须自证缺陷落地。      每条注入自带 probe(d)：它证明**缺陷真的被引入了**，
                                不是「文件变了」。probe 不成立 = 这条注入无效，
                                判 UNVERIFIED，**绝不记成「检查器漏报」**。
                                上一轮的病：只 append 一句无害注释，指纹变了，
                                于是被记成「漏报」——坏注入伪装成了对检查器的指控。
  5. 被审对象钉死在 commit 上。  参考树是 detached clone，每轮测量前重新断言
                                HEAD == 钉死的 commit 且工作树干净；漂了拒绝出数。
                                上一轮那台量的是工作树，基线绿的时候连都不打印。
  6. 解析三态并比对检查项集合。  只收 [FAIL] 行会让「某个检查项整个消失」静默变成通过。
  7. 「合计」行与逐行明细对账。  摘要说全绿、明细其实没跑，必须当场抓住。
  8. 负对照证明 probe 不是摆设。 一条无害注入必须被判「没引入缺陷」并被拒绝记成指控。

三态口径：
  PASS        注入的缺陷被它声明期望的检查项抓住了。
  FAIL        漏报：缺陷真实存在（probe 成立），期望的检查项却没红。
  UNVERIFIED  无法判定：注入无效 / 检查器崩了 / 输出不可解析 / 检查项消失或变 SKIP /
              被审对象漂了。「注入没引入缺陷」属于这一类：它不是通过，是这条注入无效。

界内还有一条给「设计内不报」用的：expect 为空的行必须指向检查器输出里一句真实存在的
`边界：` 原文；那句原文不在输出里，这条豁免就不成立（UNVERIFIED），不是静默通过。
"""
from __future__ import annotations

import hashlib
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

# ─────────────────────────────────────────────────────────────
# 位置与常量
# ─────────────────────────────────────────────────────────────
DEV_REPO = Path(__file__).resolve().parents[2]   # 开发工作树（可能正被别的角色改）
WORK = Path(os.environ.get("TPW_INJ_WORK", "/tmp/tpw-inj4"))
REF = WORK / "subject"                            # 钉死的参考树（detached clone）
RUNS = WORK / "runs"
SCRIPTS = ("check-closure.py", "check-consistency.py")

# 本轮基线：tag v2.0.6 指向的 commit（委派里写明）。可用 --subject <rev> 换。
DEFAULT_SUBJECT = "29a50e40f2ed0bf5d5bff85b7fbfa6b78059df3c"

LINE_RE = re.compile(r"^\[(PASS|FAIL|SKIP)\]\s+(\S+)\s*(.*)$")
SUM_RE = re.compile(r"合计:\s*(\d+)\s*项通过\s*/\s*(\d+)\s*项失败"
                    r"(?:\s*/\s*(\d+)\s*项跳过)?\s*/\s*(\d+)\s*项检查")
IGNORE = shutil.ignore_patterns(".pi", "upstreams", "__pycache__", "*.pyc")
FP_SUFFIXES = (".md", ".yaml", ".yml", ".py", ".sh")


# ─────────────────────────────────────────────────────────────
# 异常：每一种都对应 UNVERIFIED 的一个具体原因（不是产品缺陷）
# ─────────────────────────────────────────────────────────────
class EnvironmentFault(RuntimeError):
    """本地环境缺东西（参考树、upstreams/）——不是产品缺陷。"""


class SubjectDrift(RuntimeError):
    """被审对象漂了：HEAD 不是钉死的 commit，或参考树有未提交改动。"""


class InjectionBroken(RuntimeError):
    """这条注入无效：锚点没中 / probe 不成立 / 指纹没变。判 UNVERIFIED。"""


class CheckerCrashed(RuntimeError):
    """检查器崩了。崩了的检查器不产 [FAIL] 行——不 raise 会被读成「全绿」。"""


class SummaryMismatch(CheckerCrashed):
    """「合计」行与逐行明细对不上——摘要可能掩盖了没跑到的检查。"""


# ─────────────────────────────────────────────────────────────
# 被审对象钉死
# ─────────────────────────────────────────────────────────────
_RESOLVED: dict[str, str] = {}


def _git(*args, cwd=DEV_REPO):
    return subprocess.run(["git", *args], cwd=str(cwd), capture_output=True, text=True)


def resolve_rev(rev: str) -> str:
    """把任意 rev（tag/短 sha/HEAD）解析成完整 commit sha。"""
    if rev in _RESOLVED:
        return _RESOLVED[rev]
    r = _git("rev-parse", f"{rev}^{{commit}}")
    if r.returncode != 0:
        raise EnvironmentFault(f"解析不了 rev {rev!r}：{r.stderr.strip()}")
    _RESOLVED[rev] = r.stdout.strip()
    return _RESOLVED[rev]


def ensure_subject(rev: str | None = None) -> str:
    """准备/更新钉死的参考树：detached clone，HEAD == rev，工作树干净。

    参考树里的 upstreams/ 是指向开发工作树的符号链接——该目录被 .gitignore
    挡着，不属于任何 commit。它只是 C9 的实物参照物，不属于被审对象；
    用 .git/info/exclude 排除掉，不让它把参考树记成「有未提交改动」。
    """
    pinned = resolve_rev(rev or DEFAULT_SUBJECT)
    if not (REF / ".git").exists():
        REF.parent.mkdir(parents=True, exist_ok=True)
        if REF.exists():
            shutil.rmtree(REF)
        r = _git("clone", "--quiet", "--local", str(DEV_REPO), str(REF))
        if r.returncode != 0:
            raise EnvironmentFault(f"克隆参考树失败：{r.stderr.strip()}")
    _git("fetch", "--quiet", "origin", cwd=REF)          # 新 commit 不致命，放任
    r = _git("checkout", "--quiet", "--detach", pinned, cwd=REF)
    if r.returncode != 0:                                # 重新克隆一次再试
        shutil.rmtree(REF)
        r = _git("clone", "--quiet", "--local", str(DEV_REPO), str(REF))
        if r.returncode == 0:
            r = _git("checkout", "--quiet", "--detach", pinned, cwd=REF)
        if r.returncode != 0:
            raise EnvironmentFault(f"检出 {pinned[:7]} 失败：{r.stderr.strip()}")
    _ensure_upstreams_link()
    assert_subject(pinned)
    return pinned


def _ensure_upstreams_link():
    up = REF / "upstreams"
    if not up.exists() and (DEV_REPO / "upstreams").is_dir():
        up.symlink_to(DEV_REPO / "upstreams")
    info = REF / ".git" / "info"
    info.mkdir(parents=True, exist_ok=True)
    excl = info / "exclude"
    txt = excl.read_text(encoding="utf-8") if excl.exists() else ""
    # 注意：`upstreams/`（带斜杠）只匹配目录，匹配不上指向目录的符号链接。
    if "upstreams" not in txt.splitlines():
        excl.write_text(txt + "upstreams\n", encoding="utf-8")


def assert_subject(expected: str | None = None) -> str:
    """每轮测量前重新断言：参考树 HEAD 仍是钉死的 commit，且工作树干净。

    这是本轮加固的第一条：上一轮那台测的是工作树，git_rev() 只出现在
    assert 的消息字符串里，基线绿的时候根本不会打印——「测于哪个 commit」
    只能靠人记得看报告。现在每次测量都重新钉一次。
    """
    if not (REF / ".git").exists():
        raise SubjectDrift(f"参考树不存在：{REF}（先跑 ensure_subject）")
    want = resolve_rev(expected or DEFAULT_SUBJECT)
    head = _git("rev-parse", "HEAD", cwd=REF).stdout.strip()
    if head != want:
        raise SubjectDrift(f"被测对象漂了：期望 {want}，参考树 HEAD 是 {head}——拒绝出数\n"
                           f"  {triple_line()}")
    dirty = _git("status", "--porcelain", cwd=REF).stdout.strip()
    if dirty:
        raise SubjectDrift(f"参考树有未提交改动，拒绝出数：\n{dirty}\n  {triple_line()}")
    return head


def subject_triple() -> dict:
    head = _git("rev-parse", "HEAD", cwd=REF).stdout.strip()
    tags = _git("tag", "--points-at", "HEAD", cwd=REF).stdout.split()
    dirty = _git("status", "--porcelain", cwd=REF).stdout.strip()
    return {"commit": head, "short": head[:7], "tags": tags,
            "clean": not dirty, "dirty": dirty}


def triple_line(t: dict | None = None) -> str:
    t = t or subject_triple()
    tag = "/".join(t["tags"]) if t["tags"] else "（无）"
    state = "干净" if t["clean"] else "有未提交改动"
    return f"被审对象：commit {t['short']}（{t['commit']}）／tag {tag}／参考树{state}"


# ─────────────────────────────────────────────────────────────
# 副本与夹具
# ─────────────────────────────────────────────────────────────
def fresh(tag: str, with_upstreams: bool = True) -> Path:
    """从钉死的参考树复制一份干净副本，施加注入用。"""
    assert_subject()
    d = RUNS / tag
    if d.exists():
        shutil.rmtree(d)
    d.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(REF, d, ignore=IGNORE)
    if with_upstreams:
        target = DEV_REPO / "upstreams"
        if not target.is_dir():
            raise EnvironmentFault("本条注入要求 upstreams/ 做实物对照，但开发工作树里没有它")
        (d / "upstreams").symlink_to(target)
    return d


def seal_for_c1(d: Path):
    """测量夹具：给副本造一个自洽的 VERSION + tag，让 C1 不因「HEAD 无 tag」而红。

    只在把基线钉在**没有 tag 的 commit**（例如收口前的 HEAD）时使用。
    用了它，副本 HEAD 会多出一个 fixture commit——报告里必须写明「这不是真实基线」。
    """
    FIX = "9.9.9"
    reg = d / "workflow" / "registry.yaml"
    t = reg.read_text(encoding="utf-8")
    t = re.sub(r"(?m)^version: .*$", f"version: {FIX}", t, count=1)
    reg.write_text(t, encoding="utf-8")
    (d / "VERSION").write_text(FIX + "\n", encoding="utf-8")
    _git("add", "-A", cwd=d)
    _git("-c", "user.email=t@t", "-c", "user.name=t", "commit", "-qm", "fixture", cwd=d)
    _git("tag", f"v{FIX}", cwd=d)


# ─────────────────────────────────────────────────────────────
# 检查器输出：三态解析 + 合计对账
# ─────────────────────────────────────────────────────────────
def parse_output(script: str, text: str, returncode: int) -> dict[str, str]:
    """把一次检查器输出解析成 {检查项: PASS|FAIL|SKIP}。

    三态全收，并做两件上一轮没做的事：
      - 检查项不得重复打两行状态；
      - 末尾「合计」行必须与逐行明细**逐数相等**（PASS/FAIL/SKIP/总数四项）。
        合并两个检查器的输出再搜一条「合计」是上一轮 verify 自己踩过的坑：
        聚合统计了 N 个脚本的明细，却只匹配到最后一条摘要。
    """
    if returncode not in (0, 1) or "Traceback (most recent call last)" in text:
        tail = "\n".join(text.strip().splitlines()[-8:])
        raise CheckerCrashed(f"{script} 崩了（exit={returncode}），判定中止：\n{tail}")
    status: dict[str, str] = {}
    counts = {"PASS": 0, "FAIL": 0, "SKIP": 0}
    for line in text.splitlines():
        m = LINE_RE.match(line.strip())
        if not m:
            continue
        tag, cid = m.group(1), m.group(2)
        if cid in status:
            raise CheckerCrashed(f"{script} 对 {cid} 打了两行状态——输出不可信")
        status[cid] = tag
        counts[tag] += 1
    sums = SUM_RE.findall(text)
    if len(sums) != 1:
        raise SummaryMismatch(
            f"{script} 的「合计」行出现 {len(sums)} 次（必须有且只有一次）——"
            f"多脚本输出被合并统计过？拒绝判定")
    sp, sf, ssk, stot = sums[0]
    summary = (int(sp), int(sf), int(ssk or 0), int(stot))
    detail = (counts["PASS"], counts["FAIL"], counts["SKIP"], len(status))
    if summary != detail:
        raise SummaryMismatch(
            f"{script} 合计行与逐行明细不一致：合计 {summary}，明细 {detail}"
            f"（PASS/FAIL/SKIP/总数）——摘要可能在掩盖没跑到的检查")
    return status


def _run_one(script_path: Path, cwd: Path) -> dict[str, str]:
    p = subprocess.run([sys.executable, str(script_path)],
                       capture_output=True, text=True, cwd=str(cwd))
    return parse_output(Path(script_path).name, p.stdout + p.stderr, p.returncode)


def run_checkers(d: Path) -> tuple[dict[str, dict[str, str]], dict[str, str]]:
    """跑两个检查器，返回 ({脚本: {检查项: 状态}}, {脚本: 原始输出})。"""
    status, texts = {}, {}
    for s in SCRIPTS:
        p = subprocess.run([sys.executable, str(d / "scripts" / s)],
                           capture_output=True, text=True, cwd=str(d))
        text = p.stdout + p.stderr
        status[s] = parse_output(s, text, p.returncode)
        texts[s] = text
    return status, texts


def classify(before: dict, after: dict) -> dict:
    """比对前后两次的完整检查项集合。消失和转 SKIP 都要浮出来，不许静默。"""
    ids = lambda st: {(s, i) for s, m in st.items() for i in m}
    b, a = ids(before), ids(after)
    new_fail = {(s, i) for s, m in after.items() for i, v in m.items()
                if v == "FAIL" and before.get(s, {}).get(i) != "FAIL"}
    new_skip = {(s, i) for s, m in after.items() for i, v in m.items()
                if v == "SKIP" and before.get(s, {}).get(i) != "SKIP"}
    gone = b - a
    recovered = {(s, i) for s, m in after.items() for i, v in m.items()
                 if v == "PASS" and before.get(s, {}).get(i) == "FAIL"}
    return {"new_fail": new_fail, "gone": gone, "new_skip": new_skip,
            "recovered": recovered}


def fail_set(status: dict) -> set[str]:
    return {i for m in status.values() for i, v in m.items() if v == "FAIL"}


def _fingerprint(d: Path) -> str:
    """整树内容指纹。只证明「树变了」，不证明「缺陷引入了」——后者靠 probe。"""
    h = hashlib.sha256()
    for f in sorted(d.rglob("*")):
        if f.is_file() and ".git" not in f.parts and (
                f.suffix in FP_SUFFIXES or f.name == "VERSION"):
            try:
                h.update(str(f.relative_to(d)).encode())
                h.update(f.read_bytes())
            except OSError:
                pass
    return h.hexdigest()


# ─────────────────────────────────────────────────────────────
# 测量
# ─────────────────────────────────────────────────────────────
def measure(tag: str, mutate, probe, with_upstreams: bool = True, fixture=None):
    """复制 → 基线态 → 施加故障 → **证明缺陷真的引入** → 再跑检查器。

    probe 是语义后置条件：它必须证明这条注入要制造的缺陷真的在树里
    （例如「锁文件里那个 id 的 sha256 与实物对不上」），而不是「树变了」。
    不成立就 raise InjectionBroken，由调用方判 UNVERIFIED——绝不记成漏报。
    """
    assert_subject()
    d = fresh(tag, with_upstreams)
    if fixture:
        fixture(d)
    before, _ = run_checkers(d)
    fp0 = _fingerprint(d)
    mutate(d)
    if not probe(d):
        raise InjectionBroken(
            f"probe 不成立：这段注入没有把声明的缺陷真正引入——判 UNVERIFIED"
            f"（这条注入无效），不记成「检查器漏报」")
    if _fingerprint(d) == fp0:
        raise InjectionBroken("probe 成立但整树指纹没变——两者矛盾，拒绝出数")
    after, texts = run_checkers(d)
    return classify(before, after), texts, d


def measure_control(tag: str, mutate, probe, with_upstreams: bool = True, fixture=None):
    """负对照：这条注入**声明为无害**，probe（缺陷谓词）必须判它没有引入缺陷。

    返回 defect_present=False 才算负对照成立；为 True 时调用方必须报
    「负对照失效」——那说明要么这条注入不无害，要么 probe 认不出无害变更。
    两种情况都不允许把行记成「漏报」。
    """
    assert_subject()
    d = fresh(tag, with_upstreams)
    if fixture:
        fixture(d)
    before, _ = run_checkers(d)
    fp0 = _fingerprint(d)
    mutate(d)
    changed = _fingerprint(d) != fp0
    defect = bool(probe(d))
    after, texts = run_checkers(d)
    cls = classify(before, after)
    if not changed:
        raise InjectionBroken(f"负对照 {tag} 没有改动任何文件（指纹没变）——注入无效")
    return {"defect_present": defect, "cls": cls, "texts": texts, "dir": d}


def baseline(with_upstreams: bool = True, fixture=None, expected=()):
    """基线必须在 expected（默认空集）上恰好红——多一项、少一项都断言炸。"""
    assert_subject()
    d = fresh("baseline", with_upstreams)
    if fixture:
        fixture(d)
    st, texts = run_checkers(d)
    fails = fail_set(st)
    exp = set(expected)
    if fails != exp:
        t = subject_triple()
        raise AssertionError(
            f"基线不绿/基线漂了：期望红 {sorted(exp) or '（无）'}，实际红 {sorted(fails) or '（无）'}\n"
            f"  {triple_line(t)}\n"
            f"  多出来的红需要逐条解释；少掉的红说明该项已修好。"
            f"两种都要人看过再改 expected——不要为了让基线对上而改断言。")
    return st, texts, d


# ─────────────────────────────────────────────────────────────
# 改写助手（锚点不中即注入无效）
# ─────────────────────────────────────────────────────────────
def sub(path: str, old: str, new: str, count: int = 1):
    def f(d: Path):
        p = d / path
        t = p.read_text(encoding="utf-8")
        if old not in t:
            raise InjectionBroken(f"锚点不匹配 {path}: {old[:70]!r}——注入无效，判 UNVERIFIED")
        p.write_text(t.replace(old, new, count), encoding="utf-8")
    return f


def append(path: str, text: str):
    def f(d: Path):
        p = d / path
        p.write_text(p.read_text(encoding="utf-8") + text, encoding="utf-8")
    return f


# ─────────────────────────────────────────────────────────────
# 自检：证明第 6、7 条（三态解析、合计对账）不是摆设
# ─────────────────────────────────────────────────────────────
SYN_OK = """TIM · synthetic
----------------------------------------------------------------------------
[PASS] C1 结构
[FAIL] C2 产物
[SKIP] C3 阶段
----------------------------------------------------------------------------
合计: 1 项通过 / 1 项失败 / 1 项跳过 / 3 项检查
"""


def _syn(script: str, text: str):
    return {script: parse_output(script, text, 0)}


def run_selfchecks() -> list[tuple[str, bool, str]]:
    """本台自己的自检。任何一项红，注入台拒绝出数（先修测量工具，再测产品）。"""
    ensure_subject()
    out: list[tuple[str, bool, str]] = []

    def case(name, fn):
        try:
            detail = fn() or ""
            out.append((name, True, detail))
        except Exception as e:                          # noqa: BLE001 —— 自检就是要抓一切
            out.append((name, False, f"{type(e).__name__}: {e}"))

    def sc_three_states():
        st = parse_output("synthetic", SYN_OK, 0)
        assert st == {"C1": "PASS", "C2": "FAIL", "C3": "SKIP"}, st
        assert st["C3"] == "SKIP" and st["C3"] != "FAIL", "SKIP 被读成了 FAIL"
        return "三态都解析出来：PASS/FAIL/SKIP 各就各位"

    def sc_summary_mismatch():
        bad = SYN_OK.replace("合计: 1 项通过", "合计: 2 项通过")
        try:
            parse_output("synthetic", bad, 0)
        except SummaryMismatch:
            return "改坏合计行 → SummaryMismatch（摘要骗不了明细）"
        raise AssertionError("合计行与明细不一致却没报错")

    def sc_disappearing_item():
        gone_text = """TIM · synthetic
----------------------------------------------------------------------------
[PASS] C1 结构
[FAIL] C2 产物
----------------------------------------------------------------------------
合计: 1 项通过 / 1 项失败 / 2 项检查
"""
        before, after = _syn("s", SYN_OK), _syn("s", gone_text)
        cls = classify(before, after)
        assert ("s", "C3") in cls["gone"], cls
        return "C3 整行消失 → gone 集合抓到（不会被静默当通过）"

    def sc_new_skip():
        skip_text = """TIM · synthetic
----------------------------------------------------------------------------
[SKIP] C1 结构
[FAIL] C2 产物
[SKIP] C3 阶段
----------------------------------------------------------------------------
合计: 0 项通过 / 1 项失败 / 2 项跳过 / 3 项检查
"""
        before, after = _syn("s", SYN_OK), _syn("s", skip_text)
        cls = classify(before, after)
        assert ("s", "C1") in cls["new_skip"], cls
        assert ("s", "C1") not in cls["new_fail"], "SKIP 被读成了 FAIL"
        return "某检查项转 SKIP → new_skip 抓到（不是 PASS，也不是 FAIL）"

    def sc_merged_summary_trap():
        co = ("TIM · synthetic\n" + "-" * 76 + "\n"
              + "".join(f"[PASS] S{i} 一致\n" for i in range(1, 8))
              + "-" * 76 + "\n合计: 7 项通过 / 0 项失败 / 7 项检查\n")
        merged = SYN_OK + co
        all_sums = SUM_RE.findall(merged)
        assert len(all_sums) == 2, "合成输出里该有两条合计行"
        naive = all_sums[-1]      # 天真做法：合并统计后只拿最后一条摘要对账
        agg = (1 + 7, 1 + 0, 1 + 0, 3 + 7)   # 两个脚本的明细聚合
        assert (int(naive[0]), int(naive[1]), int(naive[2] or 0), int(naive[3])) != agg, \
            "陷阱不成立：聚合明细与最后一条摘要恰好相等"
        # 逐脚本对账则两边都过；只有「聚合明细 + 只比最后一条摘要」才会炸
        parse_output("closure", SYN_OK, 0)
        parse_output("consistency", co, 0)
        return (f"聚合明细 {agg} vs 最后一条摘要 {tuple(naive)} 不等（=verify 踩过的坑）；"
                f"逐脚本对账两边都过")

    def sc_crash_detected():
        p = WORK / "selfcheck-crash.py"
        p.write_text("raise RuntimeError('boom')\n", encoding="utf-8")
        try:
            _run_one(p, WORK)
        except CheckerCrashed:
            return "exit 非 0/1 → CheckerCrashed（崩了不会被读成全绿）"
        raise AssertionError("崩溃脚本没被判成 CheckerCrashed")

    def sc_fingerprint_guard():
        def rewrite_same(d: Path):
            p = d / "VERSION"
            p.write_text(p.read_text(encoding="utf-8"), encoding="utf-8")
        try:
            measure("selfcheck-fingerprint", rewrite_same, lambda d: True)
        except InjectionBroken:
            return "probe 为真但内容指纹没变 → 拒绝出数"
        raise AssertionError("指纹没变却出了数")

    def sc_subject_pin():
        other = _git("rev-parse", "HEAD").stdout.strip()
        if other == subject_triple()["commit"]:
            other = _git("rev-parse", "HEAD~1").stdout.strip()
        try:
            assert_subject(other)
        except SubjectDrift:
            return (f"喂一个不同的 commit（{other[:7]}）→ SubjectDrift"
                    f"（参考树现在钉在 {subject_triple()['short']}）")
        raise AssertionError("被审对象漂了却没拒绝")

    def sc_baseline_gate():
        try:
            baseline(expected={"C99"})
        except AssertionError:
            return "基线 expected 写错 → AssertionError（基线护栏还在）"
        raise AssertionError("基线对不上却没有断言炸")

    def sc_dirty_reference_tree():
        """参考树有未提交改动必须拒绝出数——不是只拒绝「HEAD 不对」。"""
        p = REF / "SELFCHECK-DIRTY.md"
        p.write_text("dirty\n", encoding="utf-8")
        try:
            try:
                baseline()
            except SubjectDrift:
                verdict = "参考树被写脏 → 运行前重新断言拒绝出数（SubjectDrift）"
            else:
                raise AssertionError("参考树有未提交改动却照样出数")
        finally:
            p.unlink(missing_ok=True)
        leftover = _git("status", "--porcelain", cwd=REF).stdout.strip()
        assert not leftover, f"自检没把参考树擦干净：{leftover}"
        return verdict

    def sc_triple_unconditional():
        """报告表头的三元组能独立打印，不依赖任何 assert 触发。"""
        t = subject_triple()
        line = triple_line(t)
        assert t["commit"] in line, line
        assert (t["tags"][0] in line) if t["tags"] else ("（无）" in line), line
        return f"三元组可独立打印：{line}"

    case("SC1 三态解析", sc_three_states)
    case("SC2 合计对账", sc_summary_mismatch)
    case("SC3 检查项消失", sc_disappearing_item)
    case("SC4 转 SKIP", sc_new_skip)
    case("SC5 合并合计陷阱", sc_merged_summary_trap)
    case("SC6 崩溃检测", sc_crash_detected)
    case("SC7 指纹护栏", sc_fingerprint_guard)
    case("SC8 被审对象钉死", sc_subject_pin)
    case("SC9 基线护栏", sc_baseline_gate)
    case("SC10 参考树脏了拒绝", sc_dirty_reference_tree)
    case("SC11 三元组可独立打印", sc_triple_unconditional)
    return out
