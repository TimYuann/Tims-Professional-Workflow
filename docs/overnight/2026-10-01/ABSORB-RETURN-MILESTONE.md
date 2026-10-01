# Deep-absorption RETURN · fixed-object milestone

**State:** the Pro pre-merge review returned **RETURN**; the bounded correction batch and the two draft candidates are complete; method's affected-claim follow-up is recorded with three unresolved quality questions (FM-1…FM-3). **No core landing, no new Pro, no UCBIP action.** Core remains `91875114e51855517f92ef099cbdf60c34e68243`.

## Fixed objects

- Pro response/disposition: `ABSORB-PRO-REVIEW-RESPONSE.txt` `9aa4af3777b2063fe0fca8a5d2e62fd28d0a9794252ac00de7aa1ea514858569`, `ABSORB-PRO-REVIEW-DISPOSITION.md` `fa9d8b073a29909edac86409e16e0a670796378377ca628ddc558c9776d3b9f0` (RETURN; conversation `https://chatgpt.com/c/6abe6b24-fac8-83e8-8bab-dc3fa3208435`, phase budget 1/1).
- Corrected evidence at commit `5cd2b8e39b5e25f6aa4ffe1107a01d54a45a0235`: B calibration `aa07e947…e439`, B coverage `78351a35…c082`, B adjudication `a456b032…bc59`; A2 index `1ee86954…00c71` / header `c1ae2a73…d961`; drafts `ABSORB-DRAFT-DBG-05-EVIDENCE.md` `e162d967…b867`, `ABSORB-DRAFT-DBG-16-MOCK-ADAPTER.md` `81cebd63…e43f`.
- Method follow-up: `ABSORB-METHOD-FOLLOWUP-REVIEW.md` `db8b2225e3b7280f61ba330ef9e6da3724e985a80d21850656ed1d056640c351` (RETURN at `5cd2b8e`; FM items below).

## Corrected source claims (closed)

- A2 orchestrate: `cursor-sdk/skills/cursor-sdk/SKILL.md` exists at the pinned repo (blob `bb070b33…`); repo presence is separated from target-host install/load, which stays UNVERIFIED. Eight further same-class rows were fixed in the same bounded pass.
- AUTH-27: Matt ADR default is title + one-to-three sentences, heavier sections optional, ADR-applicability conditions stated; Addy's ADR form is recorded separately.
- BHV-10: CONTEXT.md is glossary-only by design (must not carry specs/drafts/implementation decisions); modeling activities may use context challenges/code comparison but not dump their products into CONTEXT.
- DES-23, ORC-07, AUTH-07, BHV-08, AUTH-04: incremental-compilation default is no longer claimed as adopted; adviser invocation is separated from independence proof; AUTH-07 is no longer attributed to Matt ADR 0001; Voice/Charter record material is acknowledged; the security-axis rule stays covered while CONC-01's operational gap remains its own item.
- Completion downgrade: the 175 rows are **filled coverage comparison opinions with uneven source verification**, not completed substantive assessment; pending (8) and not-assessed faces stay separate; covered+narrow coexist is acknowledged.
- R grading: tags are reading self-reports, not qualification; all 39 adopt candidates still lack the §5 full original+support read; rows give recoverable pre-read pointers (DES-24/DBG-06).
- Adoption discipline: substantive narrow/replace requires the same §5 grounding as adopt; scope exclusions are worded as "not introduced this round"; unread-source edits are exploratory.
- DES-20/encode-lessons: the "authorize future checks" phrase is removed; the non-structural branch (strengthen explanation + failure examples; feedback closure may produce concrete TODOs) is restored.
- Statistics/locators: source-combination buckets total 183; `third_party` is 73×6 + 5×7 + 1×9 = 474 plus 8 extra paths = 482; requery anchors now point to existing files/sections/IDs.
- C1–C6 and MCAL-1…4 consumption limits applied (loci unordered; depth non-rankable but not an exemption; joint reading without forced single rules; byte reuse ≠ context equivalence; relation clues are leads, not proof; text coverage / static source basis / runtime enforcement separated; calibration generalization withdrawn).

## Provisional status (label counts only)

- Coverage rows: **covered 49 / partial 55 / not-covered 71 / pending-check 8** (183 mechanisms).
- Verdict candidates: **none 37 / adopt 39 / narrow 60 / defer 43 / reject 4** (183).
- Path accounting: A1–A3 = 1,240/1,240 with columns and path sets verified; the read-depth labels remain authors' self-reported actions, not a cross-repo quality metric.
- Actual read set / remaining work: the 19 product files were read in full; B's per-family source reads are recorded in the adjudication §1; the 39 adopt candidates still require the §5 original+support read, and the 8 pending plus the not-assessed faces list what remains. No claim that all 1,240 paths or 183 mechanisms received substantive source assessment.

## Draft candidates (non-active, docs only)

- `ABSORB-DRAFT-DBG-05-EVIDENCE.md`: redact-first evidence — preserve diagnostic signal, remove credentials, sensitive-artifact custody, HITL step vs capture distinction; proposed landing point only (`local-defect-feedback-loop.md` §Method 5, `behavior-claim-evaluation.md` §Method 2).
- `ABSORB-DRAFT-DBG-16-MOCK-ADAPTER.md`: mock/adapter choice across true external, owned remote, local substitute and internal seams; counterexample included; proposed landing point only (`cross-module-design.md` §Method 3).
- Both carry the "draft candidate — no adoption, no authority/generator/gate" disclaimer; neither modifies active methods.

## Method disposition and unresolved quality (milestone questions)

- Method at `5cd2b8e`: **RETURN/FAIL**; most corrections closed; three items remain, recorded as milestone quality rather than a new repair loop:
  - **FM-1**: R first-tag recount is **24/8/7** while the report still shows 25/7/7; and DES-14's `current_text_basis` retains one contradictory "additive-only default" clause.
  - **FM-2**: DBG-05's "correct" example writes full response headers/body to disk before redaction, conflicting with its own save rule and verify-this L51; the minimal fix direction is a conditions-branch example (approved minimal redacted evidence by default; raw only with existing consent, restricted location, custody/cleanup boundaries).
  - **FM-3**: DBG-16's counterexample puts the defect in the production HTTP adapter while the proposed fix swaps in an in-memory adapter, so the claimed defect is not executed by the proposed test; deep-module logic testing must be separated from transport/boundary contract checking, or the second variant (mocking internal collaborators) used.
- These are draft/record quality questions, not observed runtime damage; no FM was repaired in this batch per the disposition.

## Stop / next

- No more Pro, no full rescan, no upstream mutation, no tests/services, no UCBIP or remote-main action.
- Owner/Oracle decide whether to authorize a landing envelope and/or a small future batch for FM-1…FM-3; until then the round stays a preserved discovery/candidate record with the core unchanged and runtime effectiveness UNVERIFIED.
- Remote: night branch pushed to the milestone tip; `origin/main` stays `448c3d67…` (legacy).
