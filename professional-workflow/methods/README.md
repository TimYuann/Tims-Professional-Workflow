# Selected methods · current package selection

Profiles remain the owners of reusable responsibility mental models. This entry only routes: it owns the current method selection, not the method bodies. Since the 2026-10-11 extraction the bodies live byte-identical in the skill batch at the repository root (`skills/<entry>/SKILL.md`); the historical fixed objects remain retrievable at their pins (see §Status and source trace). Load one when the task Charter binds it; this list does not add applicability triggers, authority, or a fixed phase chain.

**Path convention.** `skills/…` resolves from the repository root; `profiles/…`, `charters/…`, `authority/…` and this entry's own `methods/…` resolve from the `professional-workflow/` package root.

| Task need | Method file | Judgment focus |
| --- | --- | --- |
| Reproduce and repair a known local defect | `skills/tpw-debug/SKILL.md` | E, with evidence supplied to F |
| Plan a change with cross-module dependencies | `skills/tpw-cross-module-design/SKILL.md` | D, preserving B/C ownership |
| Evaluate a specific baseline/treatment behavior claim | `skills/tpw-behavior-claim-evaluation/SKILL.md` | F (comparison scope) |

## On-demand guides

| Support need (on demand) | Guide file | Boundary |
| --- | --- | --- |
| Record or hand off evidence that may contain sensitive artifacts | `skills/tpw-on-demand-guides/guide-redacted-evidence.md` | evidence custody and HITL split; no verdict/authority change |
| Choose a test double/adapter across a dependency boundary | `skills/tpw-on-demand-guides/guide-mock-adapter-choice.md` | design/test-surface choice; no mandatory gate |

These guides are on-demand references at demonstrated knowledge gaps; they add no applicability triggers, authority, or fixed phase chain. When the support is needed, add the relevant guide to this task's existing bound/read set; no mandatory loading for tasks without that need. The task Charter still binds applicability, independence, and action permission.

## Absorption batch (2026-10-02) · integrated reviewed-object slice

Gate-reviewed, byte-passed files integrated by Driver; load only what the task needs, applicability and authority stay in the Charter.

| Need (on demand) | Method | Boundary |
| --- | --- | --- |
| Add a behavior change with test-first evidence | `skills/tpw-test-first-behavior-slice/SKILL.md` | loop and slice; no universal TDD gate |
| Judge whether produced evidence can support the claim | `skills/tpw-on-demand-guides/guide-test-evidence-quality.md` | evidence quality; not a product-verdict owner |
| Split a change into independently demonstrable slices | `skills/tpw-change-slicing/SKILL.md` | planning; wide-refactor exception preserved |
| Compare materially different designs | `skills/tpw-design-alternatives/SKILL.md` | design comparison; no mandatory option count |
| Record a decision or a rejection | `skills/tpw-decision-record/SKILL.md` | minimal decision/rejection memory and execution trail |
| Keep domain terms and local mappings consistent | `skills/tpw-domain-language/SKILL.md` | semantics; local mapping stays separate from definition |
| Define acceptance conditions with examples and counterexamples | `skills/tpw-behavior-contract-examples/SKILL.md` | behavior contracts, including consumer/acceptance questions |
| Write agent-facing text with pointer and pruning discipline | `skills/tpw-on-demand-guides/guide-agent-text.md` | authoring support; no per-sentence evaluation requirement |
| Bound shared write surfaces and composition | `skills/tpw-bounded-composition/SKILL.md` | logical write surfaces and shared canonical objects; runtime mechanics stay with D/E |
| Plan under uncertainty | `skills/tpw-uncertainty-planning/SKILL.md` | bounded destination; fog vs statable question; owner record index |
| Resolve a merge conflict | `skills/tpw-merge-conflict-resolution/SKILL.md` | needs existing action authorization and restore point; stage own files only |
| Decide what to check before writing | `skills/tpw-on-demand-guides/guide-check-design.md` | scope/real-entry/negative-control; no repo validator; write-time is not atomicity |
| Promote a lesson into a carrier | `skills/tpw-on-demand-guides/guide-lesson-promotion.md` | one-off vs pattern and carrier choice; no CI/metadata mechanism |
| Review a change on its two axes | `skills/tpw-change-review/SKILL.md` | axes stay separate and do not cancel; author contribution stated |
| Prototype to answer one question | `skills/tpw-bounded-prototype/SKILL.md` | question-first, isolated, observed evidence; not production delivery |
| Shape a change for its readers | `skills/tpw-on-demand-guides/guide-change-shape.md` | reader-load axes; authority decides the tradeoff |
| Survey architecture against friction | `skills/tpw-architecture-survey/SKILL.md` | grounded friction to candidate strength; may report no candidate |
| Run a scripted human procedure | `skills/tpw-human-procedure/SKILL.md` | per-value source/destination/sensitivity; helper is not proof of safety |
| Explain a premise or rationale | `skills/tpw-rationale-and-premise-review/SKILL.md` | evidence tiers per claim; history is not a current constraint |
| Define an agent-facing CLI contract | `skills/tpw-agent-facing-cli-contract/SKILL.md` | repeat/partial-failure semantics; headless checks; no universal validator |
| Keep domain state and invariants visible | `skills/tpw-domain-state-and-invariants/SKILL.md` | state model and invariants at a module boundary; no schema framework |
| Design the verification harness for a claim | `skills/tpw-verification-harness-design/SKILL.md` | harness maintenance scoped to affected features/claims/recipes; source-only checks do not claim live |
| Resume work from a handoff | `skills/tpw-handoff-and-resume/SKILL.md` | reconstruct from artifacts; verify necessary claims against the fixed object; no contract-like non-recheck |
| Explain a mechanism or rationale | `skills/tpw-on-demand-guides/guide-professional-explanation.md` | audience/mechanism/report scope; plain restatement without fake certainty |
| Learn a professional skill explicitly | `skills/tpw-professional-learning/SKILL.md` | only explicit learning tasks; coverage is not mastery; no default curriculum |
| Set a quality policy or gate | `skills/tpw-quality-policy-enforcement/SKILL.md` | four questions per threshold row; examples and exceptions carry owners; no universal checker |
| Design observability for a service | `skills/tpw-observability-design/SKILL.md` | on-call questions first; symptom alerts; trial-fire within valid permission; allowed fields follow the redacted guide |
| Define an interface contract and its retry semantics | `skills/tpw-interface-contract-and-retry/SKILL.md` | input/output/error/partial semantics and idempotency by intent; trust follows the writer |
| Release and roll a change back | `skills/tpw-release-and-recovery/SKILL.md` | deployed/enabled/accepted are separate; recovery plans are exercised or reported; thresholds are source examples |
| Set trust boundaries and gated actions | `skills/tpw-trust-boundary-and-actions/SKILL.md` | follow written values not channels; Ask-First list is pre-delegatable; derived-path and SSRF limits |
| Judge performance change and neutrality | `skills/tpw-performance-and-neutrality/SKILL.md` | same-condition re-measure and noise; neutrality is not a product FAIL; numbers are not SLOs |
| Operate an external tool within authorization | `skills/tpw-external-tool-operation/SKILL.md` | cost/permission/availability/retry in one short sequence; pagination/bulk follow valid authorization, cost scope and real host policy |
| Change positioned artifacts (docs/sheets/slides) | `skills/tpw-external-tool-operation/guide-positioned-artifacts.md` | position/revision semantics; lint is not visual proof; real-host claims need real observation |
| Deprecate or migrate a capability | `skills/tpw-deprecation-and-migration/SKILL.md` | design the removal; expand/contract needs all writers dual-writing and real copy coordination; no unconditional deploy safety |
| Observe accessibility behaviour on demand | `skills/tpw-on-demand-guides/guide-accessibility-observation.md` | keyboard/focus, modal exit and return, semantics/non-colour, live-region announcements; framework green is not real experience |
| Keep a change behaviour-preserving | `skills/tpw-behavior-preserving-change/SKILL.md` | structure change and visual parity as separately selectable sections; readability targets stay in guide-change-shape |
| Ask clarifying questions by dependency | `skills/tpw-decision-elicitation/SKILL.md` | facts first, then dependency-ordered questions; an unaccepted recommendation does not settle a decision |

Also integrated: tightened `skills/tpw-debug/SKILL.md` (root-cause/observation-surface clarification), `skills/tpw-cross-module-design/SKILL.md` (observation surface/module judgment references), `skills/tpw-behavior-claim-evaluation/SKILL.md` (comparison scope) and the matching Profile pointers. `skills/tpw-architecture-survey/SKILL.md` uses the B2 canonical version; the B1 duplicate is not installed.

All gate-reviewed absorption deltas are integrated; no held items remain. The candidate identity and the per-file index are recorded in the tables above and in `docs/absorption/2026-10-02/LEDGER.md`; source tails listed in the reviews remain service-specific references, and runtime effectiveness is not claimed.

## Status and source trace

Historical source trace: the original three method bodies were accepted at M4 commit `013659331c8c5f9f54b866b393972a03d7938773`, tree `2fc8db5e9bbd0a2c37888282c89c2328505fddee`. Per-file M4/M5 digests, the historical M5 snapshot and the corrected/final integration identities are recorded in `docs/overnight/2026-10-01/ABSORB-CORRECTED-CORE-MANIFEST.md` and `docs/overnight/2026-10-01/ABSORB-FINAL-INTEGRATION.md`; the absorption batch identity is in `docs/absorption/2026-10-02/LEDGER.md`. Those records describe their own snapshots; the current package state is the selection tables above. Acceptance of any historical object does not establish actual task binding, final M3 coverage, runtime dependency closure, or whole-package qualification.


The M4 selection entry's own historical digest and per-file snapshot values are preserved in the manifest pointer above; this README no longer duplicates them. Acceptance of either historical object does not establish actual task binding, final M3 coverage, runtime dependency closure, or whole-package qualification.

| Source repository | Fixed locator and pin | Used by |
| --- | --- | --- |
| Matt Pocock skills | `https://github.com/mattpocock/skills.git` · `c55ee46073ed923f86ce59a5eb3b6d895095d1b7` | local defect; cross-module design |
| Addy Osmani skills | `https://github.com/addyosmani/agent-skills.git` · `2686b620fc1fed2e8f60c704839c766b8594c6b6` | limited debugging and interface additions |
| Cursor plugins (verify-this) | `https://github.com/cursor/plugins.git` · `ecc249f1e306fc64ddf83c7bed16cacf7c2239db` | behavior-claim evidence |

These locators preserve source identity; pins and in-file anchors identify the reviewed bodies. The fixed Backbone projection is bundled under `../authority/` with its source commit and digest.

Deferred alternatives: the S2 bug-fix playbook's control/loop/model/PR defaults, `DESIGN-IT-TWICE` and its parallel-agent count, idempotency/retention rules, and the `interrogate`/`code-review` lenses. They were outside the two active M3 method needs; no alternative became a mandatory gate. No S4/S5 article-derived method is included. The X original remains `UNVERIFIED`; cached article notes are locator evidence only.

Nothing here grants authority, permissions, risk acceptance, or permission for consequential actions.

## Current state

Current shipped selection: the three original method bodies (`local-defect-feedback-loop`, `cross-module-design`, `behavior-claim-evaluation`, extended at demonstrated gaps), the two on-demand guides above, and the gate-passed absorption slice. The bodies themselves were extracted to the skill batch at the repository root on 2026-10-11 and stay byte-identical to pin `f5d6d0547459eb15c40aec25617418d5ea4710e6`; this entry routes to them. The package does not contain `path-trace`, `blast-radius`, `design-compare` or `drive-preview`; those four retired names have no equivalent body here or in the batch, and are not revived. All gate-reviewed absorption deltas are integrated; no held items remain. Package acceptance status: Oracle final acceptance 2026-10-03 (`docs/absorption/2026-10-02/FINAL-ACCEPTANCE.md`) accepts the 2026-10-02 absorption product (`8ba69427105d09b3efa1d3a5f28182d4243b5fea` / core `d0cbbfc8b56f588c183efdf8b6d503d9131b5f58`); the earlier 2026-10-01 baseline acceptance remains historical. Status-sync bytes carry a new Git identity. This index records consumption only; it grants no applicability trigger and no authority.
