# Integration check · commit `6b64b59`

State: **mechanical identity/reference/package check** by `tpw-night-check` (Pi session `01a0f66d-0b7b-7701-8c51-8d262cb2f8d4`, `commandcode/deepseek/deepseek-v4.1-flash` / max), 2026-10-02. No professional review, no demo, no product edit, no commit; this file is the only write.

Objects:

| Object | Value |
| --- | --- |
| Checked commit | `6b64b594916b679e0193a58dd35d032d25a00e79` (“feat(workflow): integrate gate-passed absorption slice (B1 13 files + B2 3 methods) with consumption index”) |
| Base | `d3aab6ad30f36789664287f304e4e91ffd61d96a` (“docs: authorize substantive three-source absorption pipeline”) |
| Core subtree at check | `7dcac80f35e56a08d613a42ac74bc3fa488db8f5` |
| Archive at check | `git archive --format=tar 6b64b59 professional-workflow` SHA-256 `7c30c4d5c00cf9d1ad25ae873f61458d4719df0c7d7f30b3eb9a0e725f53beb3` |
| Backbone | `ce82a70016a4a3fc234ea287f39aac8d79a260ddf13747c4fb705bda580453ba` (unchanged) |
| Night HEAD at check | `636c7cb` (one docs-ledger commit after the checked object); working tree clean except untracked `scan.js` |

## Checks

| # | Check | Observed | Result |
| --- | --- | --- | --- |
| 1 | Product files changed vs base = exactly 16, matching the integration list, no held/pending file mixed in | `git diff --name-status d3aab6a 6b64b59 -- professional-workflow` = **16 files**: 13 under `methods/` (M `README.md`, `behavior-claim-evaluation.md`, `cross-module-design.md`, `local-defect-feedback-loop.md`; A `behavior-contract-examples.md`, `bounded-composition.md`, `change-slicing.md`, `decision-record.md`, `design-alternatives.md`, `domain-language.md`, `guide-agent-text.md`, `guide-test-evidence-quality.md`, `test-first-behavior-slice.md`) + 3 under `profiles/` (M `evidence-evaluation.md`, `implementation.md`, `technical-planning.md`). Matches the commit subject “B1 13 files + B2 3 methods” and the ledger INT1 row (16 files, core `7dcac80f`). None of the 10 explicitly pending targets (`handoff-and-resume`, `domain-state-and-invariants`, `verification-harness-design`, `change-review`, `bounded-prototype`, `guide-change-shape`, `guide-professional-explanation`, `rationale-and-premise-review`, `agent-facing-cli-contract`, `decision-elicitation`) appears as an integrated file. | **PASS** |
| 2 | Every new method is indexed + has a status declaration in `methods/README.md`; filenames resolve | `methods/README.md` §“Absorption batch (2026-10-02)” indexes all 9 new files with a boundary note each; each new file carries its own `Status:` line (`candidate…` for `behavior-contract-examples`, `bounded-composition`, `guide-agent-text`; `on-demand reference/guide…` for `change-slicing`, `decision-record`, `design-alternatives`, `domain-language`, `guide-test-evidence-quality`, `test-first-behavior-slice`). All 9 backticked filenames resolve to existing files at the commit (9/9 OK). The 4 tightened methods are covered by the batch’s “Also integrated at this batch” paragraph. | **PASS** |
| 3 | Three changed Profiles exist and relative references resolve; pending-file pointers only in the un-integrated/hold note | `evidence-evaluation.md` → `behavior-claim-evaluation.md`, `guide-redacted-evidence.md`, `guide-test-evidence-quality.md` (all exist); `implementation.md` → `test-first-behavior-slice.md`, `change-slicing.md`, `guide-test-evidence-quality.md`, `local-defect-feedback-loop.md` (all exist); `technical-planning.md` → `cross-module-design.md`, `change-slicing.md`, `design-alternatives.md`, `decision-record.md`, `domain-language.md` (all exist). Pending-name hits in the three Profiles = **0**; the pending list appears only in `methods/README.md`’s explicit “Pending gate-confirmed fixes and therefore not yet integrated: …” sentence. | **PASS** |
| 4 | Backbone bytes unchanged | `6b64b59:professional-workflow/authority/RESPONSIBILITY-BACKBONE.md` = `ce82a700…` | **PASS** |
| 5 | No `scan.js` / temporary file mixed in | The full `d3aab6a..6b64b59` diff touches only `docs/absorption/2026-10-02/**` and `professional-workflow/**`; no `scan.js`, no `*.tmp`, no scratch path. `scan.js` remains untracked in the working tree. | **PASS** |

## Observations / residuals

- Minor, non-blocking: `methods/README.md` still carries the dated “Scope and current state (2026-10-01)” paragraph (“ships three method bodies … plus the two on-demand guides above”) alongside the new 2026-10-02 absorption table; the dates and the new table make the layering readable, but the older sentence is now narrower than the directory. Recorded as a state-text observation only — no path/hash impact.
- The checked object `6b64b59` is an ancestor of the current night HEAD `636c7cb` (docs ledger); the product bytes are those of `6b64b59` (`7dcac80f…`).
- Scope: this check covers identity, paths, references and declared status only; it does not evaluate the absorbed content, does not re-run any gate/demo, and does not accept the integration.
