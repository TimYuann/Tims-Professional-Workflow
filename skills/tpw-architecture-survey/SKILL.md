---
name: tpw-architecture-survey
description: "Survey a codebase for structural friction and grounded candidates. Use when a task asks for an architecture or system survey; it may legitimately report no candidate and does not implement the change."
license: Local self-use packaging only; no public distribution license granted; upstream MIT notices in THIRD-PARTY-NOTICES.md
metadata:
  package: tpw-skills-packaging-f5d6d054
  status: local-use package
  method-location: this package (skills/tpw-architecture-survey/SKILL.md)
  source-method-historical: professional-workflow/methods/architecture-survey.md @ f5d6d0547459eb15c40aec25617418d5ea4710e6
  source-pin: f5d6d0547459eb15c40aec25617418d5ea4710e6
  source-tree: 9d7c057417da73895cda3b85ec34d49db58669b6
  source-sha256: 682d7d36471806f4809cc627f17d298ac27487a294baa5807b1703e0557fef0e
---

## 包装与资源边界（本机自用固定成品包）

正文逐字节等于**历史固定对象** `professional-workflow/methods/architecture-survey.md` @ `f5d6d0547459eb15c40aec25617418d5ea4710e6`（tree `9d7c057417da73895cda3b85ec34d49db58669b6`）；**现行位置即本包**（该路径 2026-10-11 起已从工作流包摘出，仍可按 pin 取回）。包装只增加本 frontmatter 与本节，不改正文。

- **读取型资源 / 实际条件依赖**（随包提供，路径相对本技能目录）：`guide-agent-text.md`（写 agent-facing 文本时（经传递闭包））。
- **读取型资源 / 实际条件依赖**（随包提供，路径相对本技能目录）：`guide-check-design.md`（写前该查什么（范围／真实入口／负控制）；UCBIP routing 中与本入口组合消费）。
- **读取型资源 / 实际条件依赖**（随包提供，路径相对本技能目录）：`guide-lesson-promotion.md`（把经验提升为载具时（经 guide-check-design 传递））。
- **读取型资源 / 实际条件依赖**（随包提供，路径相对本技能目录）：`guide-professional-explanation.md`（解释机制／理由时）。
- **读取型资源 / 实际条件依赖**（随包提供，路径相对本技能目录）：`guide-redacted-evidence.md`（输出／交接可能含敏感工件时；证据保管）。
- **边界指针（不要求读）**：正文将 `cross-module-design.md` 的职责归属另一方法 → 本批入口 `tpw-cross-module-design`。
- **来源锚**（正文 Source anchors 段中的上游路径）：是出处记录，不是加载或执行本包的要求；需要这些能力时显式绑定其固定原件。

**关于正文内的 Status／评审标注（时间身份）**：正文中 `candidate`、`not yet an accepted reference`、`fixed-diff review still applies` 一类标注，说明该正文在**吸收批次**中的评审阶段。对该批次已 gate-reviewed 并通过的对象，当前接受依据是 `docs/absorption/2026-10-02/FINAL-ACCEPTANCE.md`（Oracle 2026-10-03；product `8ba69427…` / core `d0cbbfc8…`）。该接受**只覆盖原接受对象本身**，不代表本包装、简介、资源可达性、安装状态或任何实际使用已经验证。

**仍然现行有效、不因上述时间身份改写**：正文的适用条件与边界；权力限制（如“不产生 authority／trigger／gate”）；明确标为未经验证的实验性判断；以及明确 deferred／未采纳的分支（不晋升、也不复活）。本包装不重开方法语义，也不把“已安装”推成“已接受”。

`SOURCE.md` 记录固定 pin、逐项校验值与本地包装差异；`THIRD-PARTY-NOTICES.md` 保留上游 MIT 原文。本包许可边界：本机自用，公开发行条款未定。

# Architecture survey · candidate method body

- **Status:** candidate distilled under `REVIEW-A3-MATT-DEF` (DEF-3, 2026-10-02); not yet an accepted reference; creates no authority, trigger, or gate. A fixed-diff review still applies.
- **Method owner when bound:** D technical/system design. The survey produces candidates and evidence; it does not change code and does not decide the refactor. The responsible B/C/D authorities keep their decisions.

## Use

Use on demand when a task asks for an architecture or system survey — finding structural friction worth a candidate change — not as a default step of every change or every session. A survey may legitimately end with "no well-founded candidate"; that is a result, not a failure.

## Scope

1. Fix the pain point or direction first. If the requester named a module, subsystem, or pain point, take it and skip the inference below. Otherwise walk back a good stretch of commit history (`git log --oneline`) to find the hot spots — the files and areas that keep coming up — and let those paths pull attention first; if the changes are scattered with no clear hot spot, widen the net.
2. Read the project's domain glossary and the decision records in the area first; a candidate that contradicts an accepted decision is surfaced only when the friction is real enough to warrant revisiting it.
3. Change history is a clue, not a ranking law: frequently changed code is not automatically bad architecture, and rarely changed code may still carry critical risk. Use the history to choose where to look, then examine the actual structure.
4. Keep the survey bounded to the stated direction or pain point; it does not expand its own scope.

## Evidence

5. Walk the codebase and note where understanding is hard: concepts that require bouncing between many small modules; shallow modules whose interface is nearly as complex as the implementation; extracted pure functions whose real bugs live in how they are called; modules that leak across their seams; areas untested or hard to test through their current interface.
6. Apply the deletion test to a suspected shallow module: would deleting it concentrate complexity, or just move it? A "concentrates" signal supports the candidate. A thin wrapper that genuinely delivers authentication, compatibility, audit, or another accepted commitment is not shallow just because it looks small — inspect the function it performs.
7. Separate observed friction from the proposed fix. Each candidate names the affected object and the friction, and its benefit and cost statements are tied to that evidence.
8. Grade evidence strength per candidate, not once for the survey. The source uses `Strong` / `Worth exploring` / `Speculative`; a weak candidate is marked weak rather than presented as a conclusion.

## Candidates

9. For each candidate record: the files or objects involved; the problem — why the current shape causes friction; the plain-language change; benefits expressed as locality and leverage and how tests would improve; and a before/after picture where it helps. Keep the project's domain vocabulary for the domain and the codebase-design vocabulary for the architecture.
10. If a candidate contradicts an accepted decision record, mark that clearly and only when the friction justifies reopening the decision; do not list every theoretically forbidden refactor.
11. End with a top recommendation, or state that no candidate has enough evidence. The presentation channel is the task's own (the source's HTML report is one example, not a requirement).
12. The survey does not implement and does not create a rejection ledger. A rejection whose reason a future survey would need goes through the decision-record method; ephemeral reasons ("not worth it right now") do not need a record.

## Conditions and exceptions

- The survey is evidence gathering for a possible change; accepting a candidate, designing the new shape, and implementing it remain separate decisions with their own authorities.
- A survey that finds nothing actionable should say what it examined and why no candidate met the bar, rather than inventing a finding.
- An accepted decision record is not automatically final, but the survey cannot override it; it can only present the friction that argues for revisiting it.

## Limits

- No default deepening, no mandatory HTML report, no candidate per session, no fixed candidate count, and no mandatory finding.
- The survey does not create implementation authority, change accepted behavior or domain meaning, or grant migration or deletion permission.
- Later cross-source work may merge this body with another architecture-survey source; keep the pain-point-first scope, the history-is-a-clue and deletion-test operations, the per-candidate benefit/cost/evidence-strength record, the "no well-founded candidate" outcome, and the rejection-to-decision-record path.

## Source anchors

| Source | Pin / path | Section |
| --- | --- | --- |
| Matt Pocock, `mattpocock-skills` | `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`, `skills/engineering/improve-codebase-architecture/SKILL.md` | §1 Explore (L18–35): scope before scan, hot spots from history, friction list, deletion test; §2 Present candidates (L37–56): candidate card, recommendation strength, top recommendation, ADR conflicts; §3 Grilling loop (L62–70): rejection with a load-bearing reason goes to an ADR offer |
| Product core | `methods/cross-module-design.md` §Source anchors | codebase-design vocabulary and the seam/depth terms the survey reports against |
