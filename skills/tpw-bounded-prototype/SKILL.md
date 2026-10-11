---
name: tpw-bounded-prototype
description: "Prototype to answer one question. Use for isolated, question-first experiments with observed evidence; not production delivery."
license: Local self-use packaging only; no public distribution license granted; upstream MIT notices in THIRD-PARTY-NOTICES.md
metadata:
  package: tpw-skills-packaging-f5d6d054
  status: local-use package
  method-location: this package (skills/tpw-bounded-prototype/SKILL.md)
  source-method-historical: professional-workflow/methods/bounded-prototype.md @ f5d6d0547459eb15c40aec25617418d5ea4710e6
  source-pin: f5d6d0547459eb15c40aec25617418d5ea4710e6
  source-tree: 9d7c057417da73895cda3b85ec34d49db58669b6
  source-sha256: aa65d1ac4a7fdf7c28be9ee4f42cba6929a349377709d0950276b2828916a92d
---

## 包装与资源边界（本机自用固定成品包）

正文逐字节等于**历史固定对象** `professional-workflow/methods/bounded-prototype.md` @ `f5d6d0547459eb15c40aec25617418d5ea4710e6`（tree `9d7c057417da73895cda3b85ec34d49db58669b6`）；**现行位置即本包**（该路径 2026-10-11 起已从工作流包摘出，仍可按 pin 取回）。包装只增加本 frontmatter 与本节，不改正文。

- **读取型资源 / 实际条件依赖**：本入口不随包携带额外资源。
- **边界指针**：正文未把职责外派给其他方法文件的指针。
- **来源锚**（正文 Source anchors 段中的上游路径）：是出处记录，不是加载或执行本包的要求；需要这些能力时显式绑定其固定原件。

**正文内的 Status／评审语义**（如 “candidate”“not yet an accepted reference”“fixed-diff review”“尚未”“待审”）描述该正文在吸收批次中的**历史阶段**；**当前的适用与接受依据**是包接受记录 `docs/absorption/2026-10-02/FINAL-ACCEPTANCE.md`（Oracle 2026-10-03 接受，product `8ba69427…` / core `d0cbbfc8…`），全部 gate-reviewed 吸收增量已整合、无 held items。旧评审要求不对已接受对象重复；本包装不重开方法语义，也不由“已安装”推成“已接受”。

`SOURCE.md` 记录固定 pin、逐项校验值与本地包装差异；`THIRD-PARTY-NOTICES.md` 保留上游 MIT 原文。本包许可边界：本机自用，公开发行条款未定。

# Bounded prototype · on-demand method (MG-2 prototype)

- **Method owner:** the responsibility that owns the decision being explored (A/Voice for product-preference questions, D for technical shape); the prototype is an instrument, not the decision and not the build.
- **Status:** on-demand reference at a demonstrated gap (settling a fork with a throwaway instrument); a task Charter decides applicability and the actions it permits. The prototype grants nothing by being reversible.

## Use

Use when a real question can be settled cheaply by building something throwaway — a layout/interaction/density choice, or an empirical fork about behavior, timing or approach. No decision means no prototype: if the question is already settled by an accepted commitment or an existing answer, reuse the existing evidence and continue with the normal build. *(Source: cursor `ecc249f1…`, `pstack/skills/poteto-mode/playbooks/prototype.md` §1 L7.)*

## Question

- **Scope the decision the prototype exists to make.** Write it down before building: which layout, which interaction, which density — or for an empirical fork, which behavior, timing or approach. The prototype's output is that decision plus its evidence, not shippable code. *(Source: same section.)*
- **Separate the observable quantity from the value standard.** Speed, layout render, or a timing curve are measurable; whether speed matters more than cost, or which layout a human prefers, is a value judgment owned by the effective authority. A prototype can settle the former, not the latter. *(Authored boundary; source: §5–§6 observe and present.)*
- **Reversible does not create authorization.** A throwaway does not make an unauthorized action safe; a default-plus-undo cannot stand in for the operator's reserved decision; only choices inside an existing delegation proceed autonomously, and work that depends on a missing decision waits. *(Authored boundary; the prototype remains subject to the Charter.)*
- **Reuse before rebuilding.** If an accepted measurement, prior prototype or existing artifact already answers the question, use it; a second prototype of the same question adds no evidence. *(Source: §2 L8 — skip references when the direction is set; the review's reuse boundary.)* There is no required number of prototypes or variants.

## Isolation

- Build the prototype **throwaway and isolated** from production source (a scratch location), so it cannot be mistaken for a deliverable or leak into the real build. *(Source: §3 L9.)*
- Use the **lightest instrument that answers the question**: for a visual decision, plain HTML/CSS/JS or the lightest stack that renders it (CDN deps, hot reload); for a behavioral/timing decision, the smallest script that exercises it. *(Source: same section.)* Authored clarification: this is a default, not a prohibition — when the question genuinely needs the project's stack or an existing test tool to be representative, use it, and keep the prototype marked and disposable.
- When comparing alternatives, build them behind one switcher, each labelled, so the comparison is cheap and direct. *(Source: §4 L10.)*
- Propose variations the user did not ask for when they sharpen the decision; that is the point of the instrument, and it is not scope creep as long as the decision stays the object. *(Source: §5 L5; §2 L8.)*

## Instrument shape

Shape the instrument around the decision maker, not around the code. When the question is genuinely ambiguous between a behavior question and an appearance question, say which branch you assumed and why — the wrong instrument wastes the whole prototype. *(Source: matt `c55ee460…`, `skills/engineering/prototype/SKILL.md` §Pick a branch, L10–17.)*

- **Write the question into the artifact.** Put the question where the decision maker will see it (an intro, a top note), not only in a comment, so the artifact can be re-read later and checked against what it was meant to settle. *(Same source, `LOGIC.md` §1 L18–20.)*
- **State, actions, scenarios.** For a behavior/state question: render the full relevant state after every action in readable domain terms (not a raw dump), provide one action per control so anyone can free-play the model in any order, and add guided scenarios that reset to a known initial state so each runs the same way every time. Scenarios should include the awkward cases — the happy path, a tricky edge, an attempt that should be illegal. *(Same source, `LOGIC.md` §3 L41–50.)*
- **Same conditions, structurally different variants.** For an appearance question: run the variants under the same surrounding conditions (same route, real data, real density) so the comparison is about the design rather than an isolated vacuum; the variants must disagree about structure — layout, information hierarchy, primary affordance — not merely colour or copy. Choose them deliberately, not by a required count. *(Same source, `UI.md` §2–§3 and Anti-patterns L48–54, L108–111; the source's default of three variants is not imported as a rule.)*
- **The switch is real and shareable.** A single visible switcher, each variant reachable by a stable address (a URL parameter or equivalent), so the decision maker can move between them without asking you to rebuild. Hide prototype-only controls from production builds. *(Same source, `UI.md` §4 L85–90.)*
- **Keep it easy for the decision maker to open.** One obvious command or, for a self-contained file, double-click; no setup reasoning required from the person whose decision it is. *(Same source, `SKILL.md` §Rules L22; the double-click form is an example, not a required artifact type.)*

## Observe

- **Verify on the matching surface.** For a visual decision, screenshot each variant and drive the interaction; for a behavioral or timing decision, observe the thing being decided (log the timing, print the output, watch the render). The observation *is* the evidence; there is no assertion substitute. *(Source: §5 L11.)*
- Record what was observed, on which variant, under which conditions, so the evidence can be re-read later without the prototype running.

## Evidence limits

- The deliverable is: the variants explored, the evidence (screenshots or observed output), the trade-offs, a recommendation, and the scratch path — with the throwaway status stated plainly. Hand the chosen direction to the real build; the prototype itself is not shipped. *(Source: §6 L12, §Reply L14.)*
- **Capture the answer and keep the artifact recoverable.** Record the choice and the observations that settled it in the decision's own record (issue, task, decision record), and keep the prototype itself as a primary source where the next reader can find it (for example a clearly marked throwaway branch with a pointer from the decision) rather than deleting it by default. Whether the pointer lives in the repo at all follows the task's custody and cleanliness rules — the point is that the why stays recoverable, not that the scratch path survives everywhere. *(Source: matt `c55ee460…`, `skills/engineering/prototype/SKILL.md` §Rules L26, `LOGIC.md` §5 L56–58, `UI.md` §6 L98–105; the custody boundary is authored.)*
- **Re-earn the product contract before the real implementation.** A prototype is written under prototype constraints (no tests, minimal error handling, no generalisation); its logic or winning variant may be lifted, but only as a starting point that then satisfies the real contract, error handling, verification and review. “It was validated in the prototype” is not a production qualification. *(Source: `SKILL.md` §Rules L20–25, `UI.md` Anti-patterns L112.)*
- **Describe the evidence by its actual input, environment, dependencies and observation scope — not by the "prototype" label.** The label says the artifact is throwaway and not production-qualified; it does not say the inputs were synthetic or that only synthetic claims were testable. State what the prototype actually touched: which inputs and data, the running environment, which dependencies were real and which were substitutes, and what was observed. The sources permit real elements where the question needs them — a scratch database for a persistence question, the existing page's real data fetching and auth when mounting variants inside it, a minimal script driven against real dependencies for a behavior/timing question — provided the access stays inside the task's authorization. *(Source: matt `c55ee460…`, `skills/engineering/prototype/SKILL.md` §Rules 3 L23 and `UI.md` §Sub-shape A L18–22; cursor `ecc249f1…`, `pstack/skills/poteto-mode/playbooks/prototype.md` §1/3/5–6.)*
- **Scope the claim to what was observed.** A prototype green under controlled or isolated conditions is evidence for those conditions only; it does not upgrade to production-wide behavior, all inputs, or scale. Conversely, an authorized isolated prototype that actually reads a real record through a pinned SDK version does support a read/mapping observation on that version and input — do not downgrade it to synthetic just because the artifact is a prototype, and do not inflate it into proof of deployment or scale. If everything was fixtures, the claim is fixture-condition only. *(Authored; the pinned-SDK real-record counterexample is from the R5 gate ruling.)*
- **Prototype ≠ production delivery or release.** Whatever the prototype touched, it remains a throwaway instrument: it is not production implementation, it is not the shipped artifact, and validating it does not release anything. Real dependencies used inside it do not open extra network/data permissions, and re-earning the product contract before real implementation still applies. *(Source: package source set; the no-extra-permissions boundary is the R5 gate ruling.)*
- The same measurement can support different decisions: one timing result does not choose between "optimize the path" and "change the product so the path does not matter"; present the observation and the choice separately. *(Authored counterexample; required by the review.)*
- A prototype whose questions cannot be answered this way (needs real users, real scale, or an irreversible change) is not settled by building one.

## Limits

- No hard minimum of 2+ variants (and no fixed count of 3 or 5), no ban on tests or on the production stack, no required one-file or shareable-HTML form, and no "the prototype result decides everything".
- The prototype does not create implementation authority, acceptance, or a change to accepted commitments; its results enter the normal decision path (and, when accepted, the decision record). Committing the prototype to a throwaway branch is a capture convention, not an authorization to merge or to keep it in the main line.
- No production artifact, no hidden persistence: keep it isolated, mark it throwaway, and do not let it become an undeclared dependency of the real build.
- This method does not absorb the wider design-space or reader-load principles; `design-alternatives.md` handles deliberate option comparison where a real architectural decision exists.

## Source anchors

| Source | Retained contribution |
| --- | --- |
| cursor-plugins `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`, `pstack/skills/poteto-mode/playbooks/prototype.md` (§1 Scope L7; §2 References L8; §3 Build throwaway L9; §4 Switcher L10; §5 Verify on the matching surface L11; §6 Present L12; §Reply L14) | Decision-first scope; throwaway isolation in the lightest sufficient stack; one switcher for comparison; observation as the evidence; the deliverable and recommendation; hand the direction to the real build. |
| matt `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`, `skills/engineering/prototype/SKILL.md` L8–26, `LOGIC.md` L7–58, `UI.md` L7–105 | Explicit question in the artifact; state/actions/scenarios shape for the decision maker; same-conditions structurally different variants; easy to open; capture the answer and keep the artifact recoverable; re-earn the product contract before real implementation. The variant count, stack and no-test rules are not imported. |

Authored additions: the observable-vs-value separation, the reversibility-is-not-authorization boundary, the reuse-before-rebuilding rule, the evidence-by-actual-input/environment/dependency/scope framing (with the prototype-≠-production and no-extra-permissions boundaries), and the different-decisions-from-one-measurement counterexample.
