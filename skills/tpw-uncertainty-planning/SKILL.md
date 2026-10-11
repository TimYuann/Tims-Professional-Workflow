---
name: tpw-uncertainty-planning
description: "Plan under uncertainty: name the destination, separate statable questions from in-scope fog. Use when a goal is real but the map is incomplete; planning is not authorization."
license: Local self-use packaging only; no public distribution license granted; upstream MIT notices in THIRD-PARTY-NOTICES.md
metadata:
  package: tpw-skills-packaging-f5d6d054
  status: local-use package
  method-location: this package (skills/tpw-uncertainty-planning/SKILL.md)
  source-method-historical: professional-workflow/methods/uncertainty-planning.md @ f5d6d0547459eb15c40aec25617418d5ea4710e6
  source-pin: f5d6d0547459eb15c40aec25617418d5ea4710e6
  source-tree: 9d7c057417da73895cda3b85ec34d49db58669b6
  source-sha256: d37a4ef1cace6786f31db307d1808a57c7248fb16cb20a62fa387f4adedf5601
---

## 包装与资源边界（本机自用固定成品包）

正文逐字节等于**历史固定对象** `professional-workflow/methods/uncertainty-planning.md` @ `f5d6d0547459eb15c40aec25617418d5ea4710e6`（tree `9d7c057417da73895cda3b85ec34d49db58669b6`）；**现行位置即本包**（该路径 2026-10-11 起已从工作流包摘出，仍可按 pin 取回）。包装只增加本 frontmatter 与本节，不改正文。

- **读取型资源 / 实际条件依赖**：本入口不随包携带额外资源。
- **边界指针**：正文未把职责外派给其他方法文件的指针。
- **来源锚**（正文 Source anchors 段中的上游路径）：是出处记录，不是加载或执行本包的要求；需要这些能力时显式绑定其固定原件。

**关于正文内的 Status／评审标注（时间身份）**：正文中 `candidate`、`not yet an accepted reference`、`fixed-diff review still applies` 一类标注，说明该正文在**吸收批次**中的评审阶段。对该批次已 gate-reviewed 并通过的对象，当前接受依据是 `docs/absorption/2026-10-02/FINAL-ACCEPTANCE.md`（Oracle 2026-10-03；product `8ba69427…` / core `d0cbbfc8…`）。该接受**只覆盖原接受对象本身**，不代表本包装、简介、资源可达性、安装状态或任何实际使用已经验证。

**仍然现行有效、不因上述时间身份改写**：正文的适用条件与边界；权力限制（如“不产生 authority／trigger／gate”）；明确标为未经验证的实验性判断；以及明确 deferred／未采纳的分支（不晋升、也不复活）。本包装不重开方法语义，也不把“已安装”推成“已接受”。

`SOURCE.md` 记录固定 pin、逐项校验值与本地包装差异；`THIRD-PARTY-NOTICES.md` 保留上游 MIT 原文。本包许可边界：本机自用，公开发行条款未定。

# Uncertainty planning · on-demand method (DEF-4)

- **Method owner:** A/Voice owns the destination and scope; D owns dependency ordering; the owner of a resolved question carries its answer into its own record. Planning a question never transfers the authority to decide or execute it.
- **Status:** on-demand reference at a demonstrated gap (a goal too large for one working session whose route is not yet visible); a task Charter decides applicability. It is a planning aid, not a tracker, not a ticket system, and not an execution authorization.

## Use

Use when the destination is clear enough to name but the way to it is wrapped in fog: the goal is bigger than one session can hold, and the next steps cannot simply be listed. The method separates what can already be asked from what cannot yet be phrased, works the answerable questions, and stops when the way is clear. Skip it when the route is already visible or the goal fits one session — an ordinary plan covers that case and a map adds ceremony.

## Destination

- **Name the destination first.** What reaching the end looks like — a spec to hand off, a decision to lock, a change made in place. It fixes scope: every later question is judged by whether it moves toward it, and work beyond it is not fog. *(Source: matt `c55ee460…`, `skills/engineering/wayfinder/SKILL.md` L7–9, L32–34, L97.)*
- **The destination is a scoping act, not a plan.** Naming it does not authorize the work to reach it; it bounds what this planning effort is about. *(Authored boundary.)*

## Known questions and unknowns

- **A question that can be stated precisely now is a question**, even if it is blocked and cannot be worked yet: record it with what it waits on, and it becomes available when its blocker resolves. *(Source: same file, §Fog of war L88–91.)*
- **What cannot yet be stated precisely is in-scope uncertainty.** Record it loosely, in the destination's direction, without pre-slicing it into question-sized pieces: one patch may graduate into several questions, or none, once the frontier reaches it. *(Same source, §Fog of war L82–93.)*
- **Out-of-goal work is recorded separately.** Work past the destination is out of scope, not fog: it never graduates, and returning to it means redrawing the destination as a new effort rather than quietly resuming a parked item. *(Same source, §Out of scope L95–101.)*
- The discriminator is *can this be stated precisely*, not *can this be answered*: do not promote fog to a question because it feels important, and do not park a precisely statable question because it is blocked.

## Dependencies and update

- **Satisfy dependencies before expanding.** A question whose blocker is unresolved stays on hold; resolving the blocker is what makes the rest of the route statable. Recorded dependencies are relationships between questions, not a schedule: the useful output of a resolution is the answer plus what newly became precise. *(Source: same file, L69, L125–126.)*
- **Keep results where they belong.** The answer to each question lives in its own owner record (the decision record, spec, issue, or task); the planning view stays an index that points at them. A plan that restates the answers creates a second source of truth that drifts. *(Source: same file, §The Map L21–23.)*
- **Update on every resolution:** record the answer where it belongs, close the question, append the new pointer, graduate the fog that became statable, and delete or redirect entries the answer invalidated. An index that stops tracking reality is worse than none. *(Source: same file, §Work through the map L125–126.)*
- **One question at a time** (beyond work already authorized in parallel): each resolution changes which next question is even askable. *(Same source, L105, L122–126.)*
- **A claim or an assignment is a coordination marker, not a lock.** Marking a question claimed is not permission to work it; an editable planning note is a note, not execution authority. The accepted delegation remains the source of authority for any action. *(Authored boundary; the source's tracker assignment is a collision-avoidance convention.)*

## Handoff

- **When the way is clear, hand off.** The planning ends when no question remains before someone can go and do the thing: hand over what was decided (pointing at where each answer lives), what remains, and the next concrete action. *(Source: same file, §Plan, don't do L11–13.)*
- **A decision is not the deliverable.** This method produces the route, not the destination artifact; the actual spec/decision/change is produced by the ordinary work that follows, with its own authority. *(Source: same file, §Plan, don't do L11–13.)*
- **If the goal turns out to be larger or different, return to the actual authority.** Do not silently widen the destination, keep planning an unbounded goal, or treat the existing notes as authorization for a new one. *(Authored boundary.)*

## Limits

- **Not a tracker.** The method does not record task status, own work items, replace the decision record, or require an external issue tracker; it is a planning view over questions.
- **No fixed budgets or rhythms.** No required session/context size per question, no mandatory per-person or per-agent review, no requirement that every question be assigned, no one-map-per-goal ceremony, and no mandatory sweep to collect all uncertainty before starting. The method scales to the goal; a small goal may need no written view at all.
- **Planning grants nothing.** Naming a destination, recording a question or claiming it does not authorize code changes, spending budget, or bypassing a needed approval; tool and action limits stay with the task.
- No fixed vocabulary beyond owner records and pointers is required; a compact in-task note is a valid form.

## Source anchors

| Source | Retained contribution |
| --- | --- |
| matt `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`, `skills/engineering/wayfinder/SKILL.md` (L7–13; §The Map L19–53; §Tickets L55–71; §Fog of war L82–93; §Out of scope L95–101; §Invocation L103–128) | Destination named first; the view as an index pointing at where each answer lives; question = statable-now vs in-scope fog; out-of-goal work listed separately and never graduating; resolve one at a time and update the view; planning hands off to execution. The tracker schema, ticket types, labels, claim mechanism, and map body format are not imported. |

Authored additions: the destination-is-scoping-not-authorization rule, the claim-is-not-a-lock/notes-are-not-permission boundary, the return-to-authority rule when the goal changes, and the Limits.
