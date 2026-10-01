# M3 case 2 · E implementation Charter

- **State:** active for the isolated case-2 fixture task only; this Charter records existing Owner authorization and adds none.
- **Profile:** `professional-workflow/profiles/implementation.md`, SHA-256 `c96162668a1b80096c872a79321e07111a7eecc346f037f7060834f272b0aa5f` (M1-accepted Profile).
- **Instance:** `tpw-night-m3-local-impl` (Pi session `01a0f3ac-a22b-75ef-9946-984ec8f6603b`), reused from the earlier case-1 implementation task; workspace relocation and reuse do not create a new independent identity.

## Task and delegation

- **Task / outcome:** Implement the accepted case-2 snapshot behavior in this synthetic fixture, following the D-accepted Plan. Return the code/test changes, self-check observations and remaining deviations for separate F evaluation.
- **Delegation source:** Owner-authorized M3–M6 overnight work plan at baseline `496b0676e302e2d0eafba129ff61de4c203d258a`, plus the Owner's explicit direction to continue case-2 E/F after B/C v2 confirmation and the D Plan's affected-claim PASS and D acceptance. This Charter records that existing authority; it does not create or enlarge it.
- **Object scope:** May edit only `docs/overnight/2026-10-01/fixtures/m3-snapshot/src/**`, `tests/**`, and the single handoff report `M3-CASE2-E-REPORT.md`. The initial file list is an expected touch set, not an additional permission. Do not edit B/C, the D Plan, this Charter, task inputs, `professional-workflow/`, other package files, or evaluation artifacts.
- **Accepted inputs:**
  - `CASE-INPUT.md` — SHA-256 `50063486b149fc599464cb5cb25872cc9b4c4b971d1fcbc2eab0efdabeffd772`.
  - `BASELINE.md` — SHA-256 `00494d48e01f2af932e401d7e8edccbfb10d0af95e541c416b054090f0dc19da`.
  - `BEHAVIOR-CONTRACT.md` v2 — SHA-256 `6cf43d3fb647cf2c250f275179762917c0763a669e84f1718d85968a8e66c738`; accepted by the B/C owner and independently reviewed PASS for PC-1/PC-2 and v1 claim preservation (`M3-BC-V2-REVIEW.md`, SHA-256 `675f32ded97ed90013db7eb4d0e6e6ea56fdce702f28ad1ba9e94124a303d091`).
  - `DOMAIN-SEMANTICS.md` v2 — SHA-256 `d35766b45085db2b7e5b3315cca5ce4183f722186a850ef317fd571ebba6d45b`; accepted with B as a pair by the B/C owner and covered by the same independent review.
  - `TECHNICAL-PLAN.md` — SHA-256 `a306205729a002fdf1bc4eac6a623849cb2198985f8a6fbae4ec4c00ec47e5b9`; accepted by D within the D Charter. Its affected-claim recheck is PASS on predecessor `bb8afeb1…` (`M3-SNAPSHOT-PLAN-V2-RECHECK.md`, SHA-256 `e93ac8869c2f0c94eb6b9ea8ec91a265920406656d31eacf12cee5b9a25ce278`); the corrected accepted Plan records the §8 wording fix and D acceptance.
  - `RESPONSIBILITY-BACKBONE.md` — SHA-256 `ce82a70016a4a3fc234ea287f39aac8d79a260ddf13747c4fb705bda580453ba`, for the applicable responsibility and coordination boundaries.
- **Applicable methods:** None for this E instance. D used the accepted M4 `cross-module-design` method to produce the Plan; that method does not select B/C meanings or add E instructions. No unaccepted method is bound here.

## Work and limits

- **Responsibility:** Implement within the accepted B/C v2 behavior/domain claims and D Plan. Local algorithms, helpers, decomposition and test seams are E's choices while they preserve those inputs.
- **Preserve / recall:** Do not change B/C meanings, D commitments, the observable surface or the exercise scope. If an accepted claim cannot be preserved, stop dependent edits, preserve current bytes and report the affected owner, fact and impact to Driver. Driver routes to that authority; Voice is used only for a human-reserved decision.
- **Tools and actions:** Work offline in this fixture only. The seed command is `python3 -m unittest discover -s tests -v` from the fixture directory. No network, production service, persistent migration, UCBIP access, deployment, release, push or merge.
- **Evaluation isolation:** The E startup input contains the public B/C contract, accepted Plan and implementation task only. It omits the separate F evaluator's private criteria and reports. Do not search for, request or read those criteria. E self-check evidence is not an independent verdict.

## Handoff and return

- **Deliver:** Write those facts only to `M3-CASE2-E-REPORT.md`: changed file paths and SHA-256s, commands and exit/output summary, coverage added or preserved, chosen entry point/episode boundary/carrier/pin representation, deviations and unresolved issues. Do not claim PASS/FAIL for the behavior; F owns that evaluation.
- **Independence:** This is the existing E author session previously used for case 1, not a fresh identity. The case-2 F evaluator is `tpw-night-method`, a different session that did not author this implementation. Record actual contributions; do not infer independence from the workspace move.
- **Acceptance / verification / closure:** E owns its implementation and self-check report only. F independently evaluates a fixed code/test object. Neither E's self-check nor F's local verdict alone accepts overall M3 or authorizes a consequential action.
