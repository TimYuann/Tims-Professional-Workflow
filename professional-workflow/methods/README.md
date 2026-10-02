# Selected methods · current package selection

Profiles remain the owners of reusable responsibility mental models; this directory owns the selected method bodies. The tables below are the current selection: the three original method bodies (extended at demonstrated gaps), the two on-demand guides, and the 2026-10-02 absorption slice. Load one when the task Charter binds it; this list does not add applicability triggers, authority, or a fixed phase chain.

| Task need | Method file | Judgment focus |
| --- | --- | --- |
| Reproduce and repair a known local defect | `local-defect-feedback-loop.md` | E, with evidence supplied to F |
| Plan a change with cross-module dependencies | `cross-module-design.md` | D, preserving B/C ownership |
| Evaluate a specific baseline/treatment behavior claim | `behavior-claim-evaluation.md` | F (comparison scope) |

## On-demand guides

| Support need (on demand) | Guide file | Boundary |
| --- | --- | --- |
| Record or hand off evidence that may contain sensitive artifacts | `guide-redacted-evidence.md` | evidence custody and HITL split; no verdict/authority change |
| Choose a test double/adapter across a dependency boundary | `guide-mock-adapter-choice.md` | design/test-surface choice; no mandatory gate |

These guides are on-demand references at demonstrated knowledge gaps; they add no applicability triggers, authority, or fixed phase chain. When the support is needed, add the relevant guide to this task's existing bound/read set; no mandatory loading for tasks without that need. The task Charter still binds applicability, independence, and action permission.

## Absorption batch (2026-10-02) · integrated reviewed-object slice

Gate-reviewed, byte-passed files integrated by Driver; load only what the task needs, applicability and authority stay in the Charter.

| Need (on demand) | Method | Boundary |
| --- | --- | --- |
| Add a behavior change with test-first evidence | `test-first-behavior-slice.md` | loop and slice; no universal TDD gate |
| Judge whether produced evidence can support the claim | `guide-test-evidence-quality.md` | evidence quality; not a product-verdict owner |
| Split a change into independently demonstrable slices | `change-slicing.md` | planning; wide-refactor exception preserved |
| Compare materially different designs | `design-alternatives.md` | design comparison; no mandatory option count |
| Record a decision or a rejection | `decision-record.md` | minimal decision/rejection memory and execution trail |
| Keep domain terms and local mappings consistent | `domain-language.md` | semantics; local mapping stays separate from definition |
| Define acceptance conditions with examples and counterexamples | `behavior-contract-examples.md` | behavior contracts, including consumer/acceptance questions |
| Write agent-facing text with pointer and pruning discipline | `guide-agent-text.md` | authoring support; no per-sentence evaluation requirement |
| Bound shared write surfaces and composition | `bounded-composition.md` | logical write surfaces and shared canonical objects; runtime mechanics stay with D/E |
| Plan under uncertainty | `uncertainty-planning.md` | bounded destination; fog vs statable question; owner record index |
| Resolve a merge conflict | `merge-conflict-resolution.md` | needs existing action authorization and restore point; stage own files only |
| Decide what to check before writing | `guide-check-design.md` | scope/real-entry/negative-control; no repo validator; write-time is not atomicity |
| Promote a lesson into a carrier | `guide-lesson-promotion.md` | one-off vs pattern and carrier choice; no CI/metadata mechanism |
| Review a change on its two axes | `change-review.md` | axes stay separate and do not cancel; author contribution stated |
| Prototype to answer one question | `bounded-prototype.md` | question-first, isolated, observed evidence; not production delivery |
| Shape a change for its readers | `guide-change-shape.md` | reader-load axes; authority decides the tradeoff |
| Survey architecture against friction | `architecture-survey.md` | grounded friction to candidate strength; may report no candidate |
| Run a scripted human procedure | `human-procedure.md` | per-value source/destination/sensitivity; helper is not proof of safety |
| Explain a premise or rationale | `rationale-and-premise-review.md` | evidence tiers per claim; history is not a current constraint |
| Define an agent-facing CLI contract | `agent-facing-cli-contract.md` | repeat/partial-failure semantics; headless checks; no universal validator |
| Keep domain state and invariants visible | `domain-state-and-invariants.md` | state model and invariants at a module boundary; no schema framework |
| Design the verification harness for a claim | `verification-harness-design.md` | harness maintenance scoped to affected features/claims/recipes; source-only checks do not claim live |

Also integrated: tightened `local-defect-feedback-loop.md` (root-cause/observation-surface clarification), `cross-module-design.md` (observation surface/module judgment references), `behavior-claim-evaluation.md` (comparison scope) and the matching Profile pointers. `architecture-survey.md` uses the B2 canonical version; the B1 duplicate is not installed.

Held for pending fixes or dependencies (do not treat as consumed): `handoff-and-resume` (belief sentence fix), `local-defect-feedback-loop` diagnosis update (fix pending; the earlier integrated version stays), `guide-professional-explanation` (waits for handoff), `decision-elicitation` (prototype-claim scope fix), `professional-learning` (waits for professional-explanation), the `decision-record`/`change-slicing` C2/C8 merges, the seven C1/C3/C4/C5/C6/C7/C9 methods in `absorb/w3` (awaiting gate), the A4 third-party pair `external-tool-operation`/`guide-positioned-artifacts` (in distillation), and the second-side Profile pointers (shared `profiles/evidence-evaluation.md` merges serially when those targets pass).

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

Current shipped selection: the three original method bodies (`local-defect-feedback-loop`, `cross-module-design`, `behavior-claim-evaluation`, extended at demonstrated gaps), the two on-demand guides above, and the gate-passed absorption slice. The package does not contain `path-trace`, `blast-radius`, `design-compare` or `drive-preview`; those four retired names have no equivalent body here and are not revived. Pending gate-confirmed fixes and the shared Profile merge are listed in the absorption batch section and `docs/absorption/2026-10-02/LEDGER.md`. Package acceptance status: `docs/overnight/2026-10-01/ABSORB-FINAL-ACCEPTANCE.md` accepts the 2026-10-01 prior baseline package; it does not cover the 2026-10-02 absorption slice, whose reviewed integration and residuals are recorded in the absorption batch section and `docs/absorption/2026-10-02/LEDGER.md`. This index records consumption only; it grants no applicability trigger and no authority.
