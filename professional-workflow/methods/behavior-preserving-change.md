# Behavior-preserving change · on-demand method (ABC5 MG-4)

- **Method owner:** B/C own the accepted behavior being preserved; F owns the pin/equivalence evidence; D/E own the structural execution. This method grants no refactor, migration or deletion authority.
- **Status:** on-demand reference at a demonstrated gap (recoverable baseline/pin evidence for structural changes and visual parity); a task Charter decides applicability. It is not a mandatory refactor ceremony and not a review gate.

## Use

Use when a structural change (rename, extract, inline, dedupe, move, reshape) must preserve accepted behavior, or when an accepted claim is visual/pixel equivalence during a UI migration. The two halves below are **independently selectable**: a structural change with no visual claim uses only the first; a UI migration whose behavior contract is settled uses only the second. Readability and reader-load goals stay in `guide-change-shape.md`; interface/seam/depth decisions stay in `cross-module-design.md` — this method does not restate those standards. *(Source: cursor `ecc249f1…`, `pstack/skills/poteto-mode/playbooks/refactoring.md` and `visual-parity.md`; the independent-section boundary is the gate2 MG4 ruling.)*

## Structural change (behavior-preserving)

1. **Pin the accepted behavior first, and state what the current object actually does where that differs from the contract.** Write a characterization test, a snapshot, an old/new output diff, a replay, or a matching-surface observation before touching the structure. If the area has no coverage, obtain that pin before the structural change; where no usable pin can be obtained and the behavior risk is substantive, say so and either get the necessary observation or mark the claim unverified. **A type-check or lint pass is not a behavior pin.** A stable, local rename may use targeted evidence instead of a full harness — not every refactor needs one. *(Source: same playbook, steps 1 and 6; the no-harness-for-small-renames boundary is the MG4 ruling.)*
2. **Name the target shape before moving toward it**, and reshape only toward something this task's goal justifies; keep a clear, boring local branch. Prefer subtracting (dead code, a single-caller wrapper, a redundant validator, an orphan reference) over adding a new layer. *(Same playbook, steps 2 and 4.)*
3. **Move in small, behavior-preserving steps and check the affected commitments at each step.** Prove behavior on the real artifact, not "it compiles": re-run the pin, diff outputs, replay a baseline, or run a matching-surface smoke. *(Same playbook, steps 5 and 6; `local-defect-feedback-loop.md` §Method.)*
4. **Renames are not only symbol edits.** Search strings, config, prose, back-references and public consumers for the old name; a search that finds nothing is not proof that no external usage exists. *(Same playbook, step 5.)*
5. **New behavior found mid-refactor is separate work.** A real bug or a missing feature is distinguished and may pause the dependent structural work or be split out legitimately; do not hide a known risk behind "the structure must ship first". *(Same playbook, the Feature/Bug-fix split; the no-hiding boundary is the MG4 ruling.)*
6. **Evaluate the refactor against this task's goal, not against a taste for a shape.** An accepted safety, correctness or compatibility goal is not vetoed merely because reader load did not decrease, and legitimate thin wrappers (authentication, audit, compatibility shims) are kept when their commitment is real. Speculative cleanup without a justified purpose can be reverted. Deleting legacy after caller migration requires checking for real live consumers and retained commitments, and a public rename or data migration returns to its B/C owner — a structural change does not change meaning. *(Source: guide-change-shape and cross-module-design for the standards; the no-veto boundary and the migrate/delete conditions are the MG4 ruling.)*

## Visual parity

Applies only to an accepted visual-preservation/pixel-equivalence claim; a change that is allowed to change the visuals is not filed under parity. *(Source: `visual-parity.md`; the claim-binding is the MG4 ruling.)*

1. **Baseline before the migration, with its conditions fixed.** Capture the current component across its real states, with the state/viewport/theme/fonts/engine/data and capture conditions recorded, and say what the baseline covers. No baseline means no parity claim — an absent or unusable baseline is UNVERIFIED, not a follow-up. *(Same playbook, step 1; the UNVERIFIED reading is the MG4 ruling.)*
2. **Check the comparison before interpreting a delta.** Separate dynamic/anti-aliasing/non-deterministic rendering noise from real differences; the accepted threshold, masks or allowed differences come from the real contract. A non-zero delta is a FAIL only when exact-zero was accepted and the comparison itself is valid. *(Same playbook, step 4; the contract-decides-threshold boundary is the MG4 ruling.)*
3. **Do not edit the baseline or the harness to make a diff pass.** If the baseline looks wrong, stop and check with its owner; a genuinely erroneous baseline/harness may be corrected with that owner's acceptance, preserving the original evidence and reason and re-checking the affected results — never by a silent change to force zero. *(Same playbook, step 2; the owner-accepted correction path is the MG4 ruling.)*
4. **Move one component at a time** (or one safe batch), with shared primitives handled as their own blocking step where they are genuinely shared. *(Same playbook, steps 3 and 5; the fixed one-component/PR cadence is not imported.)*
5. **Pixel green is only a visual result.** It does not prove interaction, accessibility or data behavior; those claims need their own observation. Eyes can explain the layout semantics of a diff but cannot by themselves establish exact equality. *(Same playbook; the independent-behavior boundary is the MG4 ruling.)*

## Limits

- No precondition that a refactor must delete a branch or an illegal state before it is allowed; no per-function architect requirement; no "no coverage therefore no change" ban, and no requirement that every refactor first build a complete harness.
- No per-slice subtraction/reshape/rebase/PR sequence, no all-callers-same-wave rule, no blanket ban on compatibility shims or parallel old/new paths, and no fixed one-component/per-component-PR/loop-until-zero cadence. Parallel work and layering are judged by the real graph, cost and authorization.
- No prohibition on restructuring a component for a legitimate migration, and no requirement to ship a structural change before fixing a known bug or feature — they are distinguished and may pause or split.
- The method creates no refactor/migration/deletion authority, no acceptance, and no visual-threshold policy; an unsupported parity claim is UNVERIFIED rather than passed.
- This method does not restate the reader-load/change-shape standard, the interface/design standard, or the general comparison-validity rules.

## Source anchors

| Source | Retained contribution |
| --- | --- |
| cursor-plugins `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`, `pstack/skills/poteto-mode/playbooks/refactoring.md` | Behavior pin before structure (characterization/snapshot/equivalence; type-check/lint are not pins); no coverage → pin first; name the target shape; subtract before adding; small behavior-preserving steps proven on real artifacts; rename spot-checks beyond code; new bug/feature is separate; evaluate against the task goal; migrate callers and delete legacy with real-consumer checks. The always-delete-step, per-function architect, all-callers-same-wave, no-shim and per-slice-cadence rules are not imported. |
| cursor-plugins `ecc249f1…`, `pstack/skills/poteto-mode/playbooks/visual-parity.md` | Baseline-first as a blocking prerequisite with fixed capture conditions; anti-shortcut (do not edit baseline/harness to pass); one component at a time with shared primitives as their own step; image diff interpreted only in a valid comparison; non-zero fails only under an accepted exact-zero claim; pixel green does not prove interaction/a11y/data. The fixed per-component PR/loop-to-zero cadence is not imported. |
| cursor-plugins `ecc249f1…`, `pstack/skills/poteto-mode/playbooks/{feature,bug-fix}.md` | The Feature (adds behavior) / Bug-fix (changes behavior) separation that makes "found something while refactoring" a distinct unit of work rather than an excuse to widen the structural change. |

Authored additions: the independent-section selection, the no-veto rule for accepted safety/correctness/compatibility goals, the owner-accepted baseline-correction path, and the Limits.
