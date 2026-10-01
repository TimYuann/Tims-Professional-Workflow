# Source & cold-start follow-up · milestone (report/plan only)

**State:** Parts A/B/C complete within `SOURCE-AND-COLDSTART-FOLLOWUP-BRIEF.md`; **no implementation, no new source absorption, no product/core change, no push**. Local report commits only; core subtree stays `91875114e51855517f92ef099cbdf60c34e68243`. `scan.js` and the legacy worktree are untouched.

## A · Five-source absorption report

`docs/overnight/2026-10-01/SOURCE-ABSORPTION-REPORT.md` (commit `5fda796`; driver-authored, physical integrator).

- **Counts (defensible, re-checked at pins):** 159 SKILL.md units = S1 addy 25 + S2 cursor-plugins 96 (pstack 47 + benny 3 + other 46) + S3 matt 38. Surveyed at ≥index level: 159/159. Full-body-read SKILL.md: **21/159 ≈ 13.2 %** (S1 4, pstack 8, cursor-other 3, matt 6); separately pstack playbooks 4/23 full, matt support docs 2 full.
- **Adopted units:** **5/159 ≈ 3.1 %** — three main-owner units (matt `diagnosing-bugs` → `methods/local-defect-feedback-loop.md`; matt `codebase-design` (+DEEPENING) → `methods/cross-module-design.md`; cursor-team-kit `verify-this` → `methods/behavior-claim-evaluation.md`) plus two limited increments (addy `debugging-and-error-recovery`, addy `api-and-interface-design`). All three shipped methods are **partial mechanism absorption**, not whole-skill adoption; acceptance evidence M4 `0136593` + `ORACLE-ACCEPTANCE.md` + MR-01/02/06/07/08; consumption evidence M3 Charter bindings (local-fix / D / F) and the M6 cold-start binding.
- **Articles:** 2/2 carriers read (old-library method notes, not original text; mirror partial), **0 adopted**, X originals UNVERIFIED, `capture_sha256` not recomputable.
- **Limits:** reading-state counts are the survey’s process record (only pins, counts, article hashes, adopted digests and bindings were re-verified here); pstack aggregate “14 full” vs explicit per-file anchors (8 SKILL + 4 playbooks) has a 2-unit difference recorded as unresolved; old 101/1080/absorbed labels deliberately not inherited.
- **Conclusion:** three bounded mechanisms are genuinely in use with binding evidence; the overwhelming majority of the five sources is only surveyed; gaps are the UCBIP routing-name interface, the two articles’ unverified originals, and partial-mechanism boundaries.

## B · Independent DSH verification + optimization candidate

`docs/overnight/2026-10-01/COLDSTART-DSH-VERIFICATION-AND-PLAN.md` — corrected identity commit `19df06c`, SHA-256 `cfe82d2d370148fe0961ab981f70f0b7c4b0d935255ffcdf46680a26087e2ccf` (original `c8fed3e` preserved in history; author `tpw-night-check`, independent of the DSH feedback and Oracle analysis; both originals self-read).

Verified material findings: **D1** DSH self-reports running the prompt-forbidden `render_current_state.py --check` — self-admitted breach, side effects UNVERIFIED without raw trace; **D2** self-admitted `.agent-local` runtime reads — scope/sensitivity question UNVERIFIED (after MC-1), no credential/user data shown; **D3** candidate selection missed the tested 06:04Z halt/current order (established; later ordering changes are downstream-owned observations only); **D4/D5** the DSH’s blanket byte-invalidation and permanent two-subject/card-author bans are unsupported overclaims; **D6** entry README status already fixed at `29d8b09`, sub-README labels remaining (low); **D7** UCBIP routing names four methods (`path-trace`/`blast-radius`/`design-compare`/`drive-preview`) versus three shipped bodies — interface gap unresolved, owner is UCBIP, and the DSH’s “`.pi/skills` no longer exists” sub-claim is corrected (directory exists; four bodies absent); **D8** bare cross-repo paths in the optional note remain (low); **D9** transcription overclaims corrected; **D10** checker values consistent with tracked text but execution still self-reported; **D11** “tracked cannot rebuild the phase” narrowed to fine card detail. Oracle’s T-1…T-3, T-4, T-5(i,ii), F-1…F-3 were supported; Oracle missed D2 and its F-4 wording was wider than the DSH’s.

Minimal next batch (ranked, proposal only, needs separate authorization): **B1** per-run trace clarification when available (no mechanism, no gate); **B2** one short status pointer in the sub-READMEs (low); **B3** repo-qualified paths in the optional example, with validation split by tracked vs ignored references; **B4** factual coverage note (three bodies, four routing names not carried; real-system drive-preview uncovered) + the mapping decision stays with the UCBIP owner (deferred); **B5** one-sentence cold-start prompt clarification to read the effective downstream control before selecting a candidate (not gated on B1). Explicitly excluded: blanket evidence invalidation, mandatory gates, permanent role mappings, reviving old method names without coverage, permission platform/validator/composer/full role matrix, new source absorption.

Residuals: no DSH raw log/model/session; ignored local objects not Git-retrievable; single sample, no control group; current UCBIP advanced during the check (read-only observation, not assessed).

## C · Method review outcome

`docs/overnight/2026-10-01/COLDSTART-OPTIMIZATION-METHOD-REVIEW.md` (commit `743c0c9`; reviewer `tpw-night-method`, Sol/medium; authored none of A/B).

Disposition trail: **RETURN_FOR_BOUNDED_CORRECTION (one round)** on MC-1 (D2 softened to self-report + UNVERIFIED scope), MC-2 (core tree `11e6e377→91875114` correctly separated; routing content SHA-256 `fc0b3942…` vs git blob `6963521e…`), MC-3 (B1 limited to per-run clarification, decoupled from B2/B3/B5; B5 points to the effective downstream authority, not timestamp precedence), plus conditions (B3 validation split; B4 Part-C method-judgment ≠ Domain Semantics C; downstream adoption deferred; D5 contribution-based independence) → corrected candidate `19df06c` **delta confirmation PASS, no further design loop**. Method notes it cannot certify an actual reliability improvement (no comparative run) and that the original conditions/residuals continue to apply. No implementation, dispatch, Owner contact, Pro-3, core or UCBIP change.

## Integration / status

- Report commits: A `5fda796`; B `c8fed3e` → `19df06c`; C `743c0c9`; this milestone. Local `main` fast-forwarded to the milestone tip; **no push**, no tag/release.
- Remote unchanged; core subtree unchanged at `91875114…`; no method/Profile/Charter semantics changed by this batch.
- Stop / next: wait for Owner/Oracle alignment before any B1–B5 implementation; no automatic continuation, no new absorption, no third Pro.
