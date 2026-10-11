---
name: tpw-professional-learning
description: "Learn a professional skill explicitly. Use only for explicit learning tasks; coverage is not mastery and there is no default curriculum."
license: Local self-use packaging only; no public distribution license granted; upstream MIT notices in THIRD-PARTY-NOTICES.md
metadata:
  package: tpw-skills-packaging-f5d6d054
  status: local-use package
  method-location: this package (skills/tpw-professional-learning/SKILL.md)
  source-method-historical: professional-workflow/methods/professional-learning.md @ f5d6d0547459eb15c40aec25617418d5ea4710e6
  source-pin: f5d6d0547459eb15c40aec25617418d5ea4710e6
  source-tree: 9d7c057417da73895cda3b85ec34d49db58669b6
  source-sha256: 925dc0aed5e903d459677d74377b1db64f498993e34bdf2da7e60e311a1413c2
---

## 包装与资源边界（本机自用固定成品包）

正文逐字节等于**历史固定对象** `professional-workflow/methods/professional-learning.md` @ `f5d6d0547459eb15c40aec25617418d5ea4710e6`（tree `9d7c057417da73895cda3b85ec34d49db58669b6`）；**现行位置即本包**（该路径 2026-10-11 起已从工作流包摘出，仍可按 pin 取回）。包装只增加本 frontmatter 与本节，不改正文。

- **读取型资源 / 实际条件依赖**（随包提供，路径相对本技能目录）：`guide-professional-explanation.md`（需要帮助一个人理解某物（变化／子系统／决定／当前状态）而非接收状态报告时；普通工程回报／状态汇报有理由不自动触发）。
- **读取型资源 / 实际条件依赖**（随包提供，路径相对本技能目录）：`guide-redacted-evidence.md`（输出／交接可能含敏感工件时；证据保管）。
- **边界指针**：正文未把职责外派给其他方法文件的指针。
- **来源锚**（正文 Source anchors 段中的上游路径）：是出处记录，不是加载或执行本包的要求；需要这些能力时显式绑定其固定原件。

**关于正文内的 Status／评审标注（时间身份）**：正文中 `candidate`、`not yet an accepted reference`、`fixed-diff review still applies` 一类标注，说明该正文在**吸收批次**中的评审阶段。对该批次已 gate-reviewed 并通过的对象，当前接受依据是 `docs/absorption/2026-10-02/FINAL-ACCEPTANCE.md`（Oracle 2026-10-03；product `8ba69427…` / core `d0cbbfc8…`）。该接受**只覆盖原接受对象本身**，不代表本包装、简介、资源可达性、安装状态或任何实际使用已经验证。

**仍然现行有效、不因上述时间身份改写**：正文的适用条件与边界；权力限制（如“不产生 authority／trigger／gate”）；明确标为未经验证的实验性判断；以及明确 deferred／未采纳的分支（不晋升、也不复活）。本包装不重开方法语义，也不把“已安装”推成“已接受”。

`SOURCE.md` 记录固定 pin、逐项校验值与本地包装差异；`THIRD-PARTY-NOTICES.md` 保留上游 MIT 原文。本包许可边界：本机自用，公开发行条款未定。

# Professional learning · candidate method body

- **Status:** candidate distilled under `REVIEW-A3-MATT-DEF` (DEF-10, 2026-10-02); not yet an accepted reference; creates no authority, trigger, or gate. A fixed-diff review still applies.
- **Method owner when bound:** the instance responsible for the explicit learning or teaching task. This method applies only when the task explicitly includes professional skill learning or teaching; it does not add a teaching prerequisite to ordinary engineering work.

## Goal

1. Start from the mission: the concrete real-world goal the learner is chasing, what success observably looks like, constraints, and what is out of scope. If the learner cannot articulate why, interview them before writing material — a vague mission steers every later decision wrong.
2. Separate knowledge (from high-trust resources), skills (through relevant practice with feedback), and wisdom (from real-world interaction or a community). Topics weigh these differently; do not force the same split.
3. The mission may change. Update the mission record and keep the change visible instead of leaving a stale mission steering future sessions.

## Knowledge

4. Gather knowledge from primary, high-trust resources and cite each claim back to its source; do not trust parametric recollection as a citation or an unverified memory as a resource.
5. Teach only the knowledge the target skill needs. Difficulty while acquiring knowledge consumes working memory that understanding needs, so keep non-essential load out.

## Practice

6. For skill acquisition, difficulty is the tool: use effortful retrieval, spacing, and (for skills) interleaving. Keep lessons short, tied to the mission, and inside the learner's zone of proximal development.
7. The difficulty inversion — make practice effortful so retention grows — is a source teaching heuristic; its learning benefit is not validated in this package. Treat it as an experiment to observe, not an established law.
8. Keep the feedback loop as tight as possible. An interactive lesson, a quiz, or a guided real-world task can each serve; the choice follows the goal, and a lesson does not require a quiz.

## Evidence

9. Record demonstrated ability separately from material merely covered. Coverage is not learning; a single correct answer does not prove retention; self-reported prior knowledge is recorded as a claim (with its claimed depth), not as demonstrated ability.
10. Keep reference material and lessons as separate roles: reference is the compressed, revisit-able essence; a lesson is the scoped teaching unit. Reuse shared components instead of duplicating them across lessons.
11. When recording, distinguish what was demonstrated, what was claimed, corrections, and mission changes; mark a superseded record rather than deleting the history.

## Limits

- Use only when the task explicitly includes professional learning or teaching. No fixed workspace layout, file set, course structure, assessment gate, community-join requirement, per-quiz constraint, or equal-length answer formatting requirement.
- Explanation without a quiz and training with a quiz can coexist by goal; neither is mandated, and this method does not forbid one in favor of the other.
- This method does not issue credentials, certification, or proof of long-term mastery. Retention needs longer-term observation than a session can provide.
- Later cross-source work may merge this body with another learning or explanation source; keep the mission-first goal, the knowledge/skills/wisdom split, the demonstrated-versus-claimed record, and the unvalidated-difficulty caution.

## Source anchors

| Source | Pin / path | Section |
| --- | --- | --- |
| Matt Pocock, `mattpocock-skills` | `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`, `skills/productivity/teach/SKILL.md` | Teaching workspace (L10–20); Philosophy: knowledge, skills, wisdom, never trust parametric knowledge (L22–32); Fluency vs Storage Strength (L34–45); Lessons (L47–61); Assets reuse (L63–69); The Mission (L71–79); Zone of Proximal Development (L81–89); Knowledge (L91–97); Skills (L99–110); Reference Documents (L122–136) |
| Matt Pocock, `mattpocock-skills` | same pin, `skills/productivity/teach/MISSION-FORMAT.md` | Template (L5–23); Rules: concrete over abstract, push back on vagueness, revise when reality shifts, keep it short (L25–31) |
| Matt Pocock, `mattpocock-skills` | same pin, `skills/productivity/teach/LEARNING-RECORD-FORMAT.md` | Template (L7–15); Evidence field (L22); When to write: demonstrated understanding vs disclosed prior knowledge (L29–38); What does not qualify: coverage is not learning (L40–42); Supersession (L44–48) |
| Product core | `methods/guide-professional-explanation.md` (another batch) | Cross-reference: audience, mechanism/evidence, and report scope belong to the professional-explanation guide; this method owns the learning/teaching cycle |
