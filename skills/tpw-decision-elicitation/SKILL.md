---
name: tpw-decision-elicitation
description: "Ask clarifying questions by dependency: facts first, then dependency-ordered questions. Use when a decision is missing inputs; an unaccepted recommendation does not settle a decision."
license: Local self-use packaging only; no public distribution license granted; upstream MIT notices in THIRD-PARTY-NOTICES.md
metadata:
  package: tpw-skills-packaging-f5d6d054
  status: local-use package
  method-location: this package (skills/tpw-decision-elicitation/SKILL.md)
  source-method-historical: professional-workflow/methods/decision-elicitation.md @ f5d6d0547459eb15c40aec25617418d5ea4710e6
  source-pin: f5d6d0547459eb15c40aec25617418d5ea4710e6
  source-tree: 9d7c057417da73895cda3b85ec34d49db58669b6
  source-sha256: 5ce9b2939b4b2211a69ba6bee4042ec39211a01ec729d2ffaeb02183560a956d
---

## 包装与资源边界（本机自用固定成品包）

正文逐字节等于**历史固定对象** `professional-workflow/methods/decision-elicitation.md` @ `f5d6d0547459eb15c40aec25617418d5ea4710e6`（tree `9d7c057417da73895cda3b85ec34d49db58669b6`）；**现行位置即本包**（该路径 2026-10-11 起已从工作流包摘出，仍可按 pin 取回）。包装只增加本 frontmatter 与本节，不改正文。

- **读取型资源 / 实际条件依赖**（随包提供，路径相对本技能目录）：`behavior-claim-evaluation.md`（正文按条件指向该方法；随包取回，另见对应入口）。
- **读取型资源 / 实际条件依赖**（随包提供，路径相对本技能目录）：`guide-redacted-evidence.md`（输出／交接可能含敏感工件时；证据保管）。
- **读取型资源 / 实际条件依赖**（随包提供，路径相对本技能目录）：`guide-test-evidence-quality.md`（判断所产证据能否支撑声明时）。
- **边界指针**：正文未把职责外派给其他方法文件的指针。
- **来源锚**（正文 Source anchors 段中的上游路径）：是出处记录，不是加载或执行本包的要求；需要这些能力时显式绑定其固定原件。

`SOURCE.md` 记录固定 pin、逐项校验值与本地包装差异；`THIRD-PARTY-NOTICES.md` 保留上游 MIT 原文。本包许可边界：本机自用，公开发行条款未定。

# Decision elicitation · candidate method body

- **Status:** candidate distilled under `REVIEW-A3-MATT-ABC` (MG-9) and extended under `REVIEW-A2R-CURSOR-ABC` (MG-2, 2026-10-02); not yet an accepted reference; creates no authority, trigger, or gate. A fixed-diff review still applies.
- **Method owner when bound:** A/Voice (problem framing and human read-back), with B/C routing their unresolved behavioral or semantic items through it. Decisions stay with the authority that holds them; the method allocates questions, it does not answer them.

## Use

Use on demand when a task has unresolved items whose answers change the work and those answers belong to a decision owner (a human, or an authority inside the delegation). It is a question-allocation method, not a questionnaire and not a fixed interview phase. It does not replace the problem definition, the behavior contract, the acceptance record, or the task's recall path.

## Prepare

1. List the unresolved items that actually affect this task. Separate facts (an observation the environment, files, tools, or existing records can settle) from decisions (an answer only an owner can give).
2. Look up accessible facts before asking. Do not put a lookup question to a person. If a lookup is still running, only questions downstream of it wait; ask the rest.
3. Name each decision's owner from the actual delegation or policy. Decisions inside an accepted delegation may already be settled for the team or the instance — do not re-ask them. Decisions that change objectives, accepted commitments, risk, or retained boundaries go to the authority that owns them; human-reserved decisions go through Voice.

## Facts and choices

4. Keep an observable measure and a value choice separate. Speed, timing, rendering, and layout behavior can be measured; whether speed matters more than cost, or which design is preferred, is a value decision for the authority that owns it. A measurement does not settle a preference.
5. Reversibility does not create authorization. "It is easy to undo" is not a substitute for an operator-retained decision; a default plus an undo note is not acceptance.
6. Advance only choices the existing delegation already covers; work that depends on a missing decision waits rather than proceeding on a chosen default. When the delegation is silent, route the decision to its owner.
7. Reuse evidence that already answers the question; a new measurement or artifact is not required merely to follow the method.

## Ask by dependencies

8. Order the unresolved items by dependency: if one answer can change another question, its options, or its relevance, the later question is downstream.
9. Ask the current frontier — the questions whose prerequisite answers are settled — and nothing downstream of an open item. Number each question and attach a recommended answer with its reason, so an owner can answer by number and accept, adjust, or override the recommendation.
10. Size the batch to the owner's cognitive burden: the whole current frontier in one round, or one question at a time when the owner reads slowly, works in a second language, or uses the sequential form deliberately. Both are supported; neither is a defect.
11. Put only genuine decisions to the owner. A question is already settled only when an accepted commitment, or a choice actually made within a clear delegation by the authority that owns it, determines the answer. An unaccepted recommendation does not settle anything: if the choice is retained by the Owner (for example, "we recommend vendor A, but the vendor choice is the Owner's"), still ask, and do not record it as decided. Do not file an item whose authority is insufficient as a mere explanation.

## Recompute

12. After answers arrive, record the accepted decisions in their existing carrier (task input, owner document, acceptance record); settle the answered items and re-scope the tree. Do not pre-write questions that depended on answers not yet given.
13. Recompute the frontier and ask the next round: a downstream item may now be answerable, changed, or moot.
14. If an answer contradicts an earlier one, reopen only the affected branch and fix its dependents; do not silently patch the contradiction in the record.

## Unanswerable by conversation

15. When an item needs seeing, trying, or feeling rather than describing, first scope the decision the artifact exists to make (which layout, interaction, density, or which behavior, timing, or approach). No decision means no artifact — route back to the ordinary work.
16. Build the disposable artifact in an isolated scratch location separate from production source, using the lightest stack that renders or exercises the question (for example vanilla HTML/CSS/JS with hot reload for a visual decision; the smallest script for a behavioral or timing one). A production framework, abstractions, and a test suite are not required for this artifact.
17. When comparing alternatives, put them behind one switcher (buttons or a keypress) with labeled variants, and observe on the matching surface: screenshots and interaction for a visual decision; logged timing, output, or render for a behavioral one. The observation is the evidence. Present alternatives, tradeoffs, a recommendation, and the artifact path; say plainly that the artifact is throwaway.
18. Describe the prototype evidence by what it actually used: the inputs, the runtime environment, whether the dependencies were real or substitutes, and the observation scope. A narrow claim about a specific reaction or mapping can be supported by a representative surface, a scratch database, or an existing page. Where a claim's real leg was actually executed under the task's authorization (a fixed SDK call reading one provider record, a real page interacted with in that environment), it supports that narrow provider path or experience observation for the version, inputs, and scope observed — but not production-wide behavior, all deployment environments, all inputs, or scale. Where the real leg was not executed, a controlled green result cannot replace it; use the claim-appropriate evidence legs in `behavior-claim-evaluation.md` §Use for those parts. The artifact stays throwaway and separate from the production delivery, and building it still needs its own valid action authorization. The same measurement can support different product choices: the measurement answers the fact, not the value.

## Close / return

19. Close when the frontier for this task is empty: the unresolved items that actually affect this work are settled to the level this task needs, and what remains unknown is stated explicitly. Do not traverse an unbounded design tree, and do not cap questions by count.
20. Pause only work that depends on an unresolved item; preserve settled results. Route an item owned by another authority through the task's return path — Driver for routing, Voice for human-reserved decisions or human acceptance.
21. Human-reserved decisions and acceptances need read-back and an explicit record. Existing valid delegations and action authorizations continue; do not add a new final acknowledgement gate to every task.
22. Decisions and acceptances are not evidence that the resulting behavior works: a recorded decision is accepted intent, and prototype evidence covers only the inputs, environment, dependencies, and observation scope it actually used. It is not the production delivery or release, and it does not authorize one; behavior observed inside that scope is evidence for that scope only, not for the unobserved production-wide remainder.

## Examples

- **Dependent questions.** "Which identity provider?" gates "what token lifetime applies?" Ask the provider question now; the lifetime question belongs to a later round because the answer can change its options.
- **Settled inside the delegation.** An accepted Plan delegates local retry parameters. Treat that as settled and record the choice where the delegation says; do not wake the Owner to re-approve what the delegation already granted.
- **Recommendation vs retained decision.** The team recommends vendor A, but the vendor choice is retained by the Owner. The recommendation does not settle it: still ask, and do not record the item as decided.
- **Fact not accessible.** A required production metric is not reachable under the current authorization. State it as unknown, name the dependent work that pauses, and use the task's recall path. Do not turn it into an interview question or infer the value.
- **Prototype before decision.** "How should this interaction feel?" cannot be settled by talking. Build a throwaway variant set, react on the matching surface, then bring back one focused question. The artifact is evidence of the reaction, not the production implementation.

## Conditions and exceptions

- Decisions belong to the actual authority, not automatically to the user; "ask the user" is wrong when policy or an accepted delegation already settles the item.
- The frontier is a judgment, not a computed graph: a round can accidentally couple two questions. When that is discovered, reopen the affected branch in the next round.
- A weak or fast run can collapse the interview, answer its own questions, or stop early; record that as a run failure rather than normalizing it.
- The method does not require questions for every branch, and it does not prevent existing clarifications from being recorded in their owner documents.
- A prototype's build still needs valid action authorization, and it does not authorize the production implementation it informs.

## Limits

- No fixed question count, no mandatory round count, no long questionnaire dump, and no substitute "decision memo" for a decision the owner has not actually given.
- No mandatory 2+ prototype variants, no ban on test or production stacks, no "no planning" rule carried over, and no "the prototype result decides everything": use the lightest sufficient tool, and reuse existing evidence.
- Question quality is not guaranteed by a model choice or by running the method; an improvement claim needs its own real observation, not the method's name.
- Human-reserved decisions still require read-back and acceptance; this method does not create approval, acceptance, or implementation authority.
- Later cross-source work may merge this body with another elicitation source; keep the facts/decisions split, fact-vs-value separation, dependency frontier, recommendation format, prototype branch, and close/return operations above.

## Source anchors

| Source | Pin / path | Section |
| --- | --- | --- |
| Matt Pocock, `mattpocock-skills` | `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`, `skills/productivity/grilling/SKILL.md` | Design tree, rounds, frontier (L6–9); round format and recommendations (L10–23); recompute (L24); facts vs decisions and non-blocking lookup (L26); close (L28) |
| Matt Pocock, `mattpocock-skills` | same pin, `docs/productivity/grilling.md` | §The round, the frontier, and who decides (L21–35); §Common questions (L43–63): one-at-a-time opt-out, confirmation gate, honest frontier limit |
| Matt Pocock, `mattpocock-skills` | same pin, `docs/productivity/grill-me.md` | §It's a conversation, not an interview (L21–29); §Grillable and ungrillable (L31–35); "I don't know" / prototype (L62) |
| Cursor plugins | `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`, `pstack/skills/poteto-mode/playbooks/prototype.md` | Items 1, 3–6: scope the decision and no-decision route; throwaway isolation and lightest stack; one-switcher labeled variants; matching-surface observation as the evidence; present alternatives/tradeoffs/recommendation and hand the chosen direction to the real build |
| Product core | `methods/behavior-claim-evaluation.md` §Use (L9–10) | Claim-appropriate evidence legs: synthetic or fixture-based evidence for logic isolation or mapping under controlled input; a real leg for a real Provider, SDK, wire behavior, deployment or end-user claim |

Consumption pointers added (by the first batch) at `profiles/intent-voice.md` and `profiles/behavior-domain.md` §按需方法入口. `methods/README.md` indexing is Driver's integration step.
