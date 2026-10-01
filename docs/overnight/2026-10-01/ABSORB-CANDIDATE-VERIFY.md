# Absorb candidate verification · A (mechanical) + B (cold-read evaluation)

State: **independent verification report** by `tpw-night-check` (Pi session `01a0f66d-0b7b-7701-8c51-8d262cb2f8d4`, `commandcode/deepseek/deepseek-v4.1-flash` / max), 2026-10-01. Read-only apart from this file; no service, no network, no commit. The expected reader answer was held separately and was **not** written into the reader inputs.

Objects:

| Object | Identity |
| --- | --- |
| Night candidate tip (driver-stated fixed commit) | `20640db3999e9a6514f2e7d0896a385bad05fb70`; night HEAD = this commit, working tree clean except untracked `scan.js` |
| Candidate code commit (per manifest) | `eb7930b42524096a7a286186ba4561df7b95a24e` |
| Package subtree (same at both commits) | `69226762d65a7ded108977df7e816fe7894e795e` (21 files) |
| Accepted core (unchanged) | `91875114e51855517f92ef099cbdf60c34e68243` |
| Manifest | `docs/overnight/2026-10-01/ABSORB-CORRECTED-CORE-MANIFEST.md` SHA-256 `119136ed5b9401094d1908bcc5d1aaac3a081041bf170ad1656b8741dea52cef` |
| Reader inputs | `TASK-FACTS.md` `ef1d2094…`, `INSTANCE-CHARTER.md` `c8efe9af…`, `ANSWER.md` `b5be7cde…` (under `.worktrees/verification/absorb-reader/`) |
| `scan.js` / legacy | `scan.js` `c033c967…`; legacy worktree HEAD `496b067…`, staged `8eb56e9e…`, unstaged `b6506ea2…` (untouched) |

## A · Mechanical verification

| # | Check | Observed | Result |
| --- | --- | --- | --- |
| A1 | Manifest 21 digests vs actual bytes | 21 manifest entries; file set exactly equals `git ls-tree -r 20640db professional-workflow`; **0 digest mismatches** | **PASS** |
| A2 | Core subtree | `20640db:professional-workflow` = `69226762d65a7ded108977df7e816fe7894e795e` (also at `eb7930b`) | **PASS** |
| A3 | Deterministic archive | `git archive --format=tar eb7930b42524096a7a286186ba4561df7b95a24e professional-workflow` SHA-256 `6fa0738773c38c30007da418c070698963b5ea205202b0ecd0553b866f902d57` — matches the manifest’s own pairing. **But** `git archive --format=tar 20640db3999e9a6514f2e7d0896a385bad05fb70 professional-workflow` = `055005fa2bffc709b992617f54e8b08fe1045d3f506db59f96b2793144d90fee`, not `6fa07387…` | **PASS for `eb7930b`; MISMATCH for `20640db`** — see residual R-A |
| A4 | Diff vs accepted core `91875114` | `git diff --name-status 91875114 20640db:professional-workflow` = exactly **7 M + 2 A**: M `README.md`, `charters/README.md`, `methods/README.md`, `methods/behavior-claim-evaluation.md`, `methods/cross-module-design.md`, `methods/local-defect-feedback-loop.md`, `profiles/README.md`; A `methods/guide-mock-adapter-choice.md`, `methods/guide-redacted-evidence.md` | **PASS** |
| A5 | Backbone bytes | `professional-workflow/authority/RESPONSIBILITY-BACKBONE.md` = `ce82a70016a4a3fc234ea287f39aac8d79a260ddf13747c4fb705bda580453ba` | **PASS** |
| A6 | Stored DSH prompt/feedback untouched | `COLDSTART-DSH-PROMPT.md` `6831d556…`, `COLDSTART-DSH-FEEDBACK.md` `6e3e6e0f…` at the candidate and in the working tree | **PASS** |
| A7 | Guide filenames resolve in the package | `guide-redacted-evidence.md` and `guide-mock-adapter-choice.md` are referenced from `methods/README.md` (on-demand guides table) and from the method files, and both exist under `professional-workflow/methods/`; no dangling `guide-` reference (package entry → `methods/README.md` → guides) | **PASS** |
| A8 | `methods/README.md` support table + scope statement | Has the “On-demand guides” table (two support needs) and the “Scope and current state (2026-10-01)” statement: three method bodies; `path-trace` / `blast-radius` / `design-compare` / `drive-preview` “have no equivalent body here and are not revived”; guides “add no applicability triggers, authority, or fixed phase chain” | **PASS** |
| A9 | No new Role / gate / validator / composer | Diff adds only the two guide files; package directories unchanged (`authority`, `charters`, `methods`, `profiles`); added lines explicitly state “no mandatory gate”, “no new gate, validator, mandatory mock/port/DI, or test framework”, “creates no authority, generator, or gate” | **PASS** |
| A10 | `scan.js` / legacy untouched | `scan.js` present (untracked, `c033c967…`); legacy HEAD `496b067…` with staged/unstaged patches still `8eb56e9e…` / `b6506ea2…` | **PASS** |

A residual (R-A): the task statement paired commit `20640db` with archive `6fa07387…`, but that digest belongs to `eb7930b`; `git archive` records the commit timestamp in tar entries, so the two commits produce different tars despite the identical package tree. The manifest itself is internally consistent (`eb7930b` → `6fa07387…`). No core/product bytes are affected. The fixed archive identity should name `eb7930b`, or `20640db` should carry `055005fa…`.

## B · Cold-read evaluation

Answers are the reader’s planning-level explanation (no execution, per its Charter). Evaluation points as delegated:

| # | Point | Evaluation | Result |
| --- | --- | --- | --- |
| B1 | Located method/guide from the entry | Reader used the package entry → `profiles/evidence-evaluation.md` (F) → `methods/behavior-claim-evaluation.md` + `methods/guide-mock-adapter-choice.md`; it quotes the guide’s dependency classification and coverage-boundary items and notes the package still awaits the directed recheck | **PASS** |
| B2 | Action = evaluate the claim at the production adapter contract surface | Answer explicitly reframes the claim as the production adapter’s request-construction/response-parsing path, calls the in-memory-replaced surface a “mislabeled surface”, and moves observation to the adapter against a local stub/recorded fixture (or names which real normalization a test actually executes) | **PASS** |
| B3 | Evidence = local stub/recorded fixture incl. nested/missing/null; record uncovered parts | Requires a fixture matrix (normal nested shape with `discount: null`, numeric/object discount, missing/empty `data`, wrong types), assertion of request construction + parsed output, a negative control, and explicit recording of what the port suite does not cover | **PASS** |
| B4 | Recall = in-process collaborator → real collaborator; unavailable evidence → insufficiency/UNVERIFIED | The insufficiency/UNVERIFIED branch is handled well (verdict section plus listed unknowns). The in-process-collaborator recall branch is **not** named, although the guide’s counterexample includes it and the guide was in the reader’s read set. The TASK-FACTS scenario is remote-owned, so this does not change the answer’s verdict; it is a partial use of the available recall knowledge | **PARTIAL** |
| B5 | Verdict discipline | States the three-state vocabulary; correctly says the current suite cannot support **PASS** (wrong surface, no negative control), cannot support **FAIL** either (missing evidence ≠ counterexample), and that the appropriate state is **UNVERIFIED** with the blocker and uncovered parts recorded; no verdict grants closure/publish | **PASS** |
| B6 | Explicit uncertainty | Eight listed unknowns, including the strongest one — the stated symptom (“discounted orders priced free”) is inconsistent with the described mechanism (flat-shape lookup would zero *all* prices) — plus missing object/version identity, the redaction guide not being in its read set, E-return applicability, independence, input trust, and candidate status | **PASS** |
| B7 | No invented authorization / gate | Answer explicitly limits itself to the Charter, says the guide is candidate text and its presence adds no authority, authorizes no new gate/framework/module shape, and treats applicability as Charter-bound only | **PASS** |

Overall B: **PASS with one PARTIAL (B4)** and no FAIL. The reader did not treat the green in-memory suite as coverage, did not invent authority, and kept the required verdict limits.

## Residuals

- R-A: archive↔commit pairing mismatch in the task statement (see above); the manifest pairing is correct. Recommend fixing the identity sentence rather than re-archiving — no bytes changed.
- B4: single reader, no control group; the in-process-collaborator recall branch was not exercised/named. A second reader is not required for this bounded observation.
- Reader did not load `guide-redacted-evidence.md` (outside its Charter read set) and recorded that as an unknown; it also flagged that the package candidate is not yet accepted. Neither is a defect.
- This report verifies identities and the single reader answer only; it does not accept the candidate, does not rerun any test/service, and does not change any other file.
