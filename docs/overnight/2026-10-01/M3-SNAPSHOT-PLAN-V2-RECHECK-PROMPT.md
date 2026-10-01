# M3 case 2 · affected-claim recheck of D Plan after B/C v2

- **Reviewer:** `tpw-night-method`, independent of D Plan author `tpw-night-m3-design`.
- **Fixed Plan candidate:** `fixtures/m3-snapshot/TECHNICAL-PLAN.md`, SHA-256 `bb8afeb1d7519cac8926e1553f30e83590b8fb0504f120120c09cd916e0823d3`.
- **Fixed B/C inputs:** B v2 SHA-256 `6cf43d3fb647cf2c250f275179762917c0763a669e84f1718d85968a8e66c738`; C v2 SHA-256 `d35766b45085db2b7e5b3315cca5ce4183f722186a850ef317fd571ebba6d45b`.
- **B/C independent review:** `M3-BC-V2-REVIEW.md`, SHA-256 `675f32ded97ed90013db7eb4d0e6e6ea56fdce702f28ad1ba9e94124a303d091`.
- **Prior Plan challenge:** `M3-SNAPSHOT-PLAN-CHALLENGE.md`, SHA-256 `bf3e15de71f4bf82adaa5547b9c412b4384a90d9d919420d5023fd9f593ab126`.
- **D reconciliation task:** `M3-D-PLAN-RECONCILIATION-PROMPT.md`, SHA-256 `8cfc6872e9ca266a488f4bb739de94cc42d438e6788332439735bb3fefe0f9df`.

## Review question

Give one three-state result (`PASS`, `FAIL`, or `UNVERIFIED`) for the affected D Plan claims in this exact candidate. This is a challenge/recheck, not Plan acceptance, execution authorization, implementation review, or M3 acceptance.

1. **PC-1 / R-2:** Does the Plan correctly apply B/C v2's accepted-baseline inheritance to authorized in-scope `src/**`/`tests/**` diffs, remove every active claim that such byte changes alone void B/C acceptance, and retain the exact semantic/scope re-open conditions? Confirm that the text lifts only the former dependency conflict and does not create implementation authority; identify whether E eligibility is correctly distinguished from D acceptance and the Driver's dispatch decision.
2. **PC-2 / R-10:** Does the Plan state path-order recipe and both digests accurately, withdraw the locale explanation, and close rather than preserve an active request/blocker against the B/C owner?
3. Reopen any PC-3/PC-4 finding from the prior challenge only if this reconciliation changed it or introduced a contradiction. Do not repeat review of unaffected Plan claims. Identify any other material claim newly introduced by this reconciliation that affects the same boundaries.
4. Read the entire current Plan and the fixed B/C/review/challenge inputs needed for those questions. Do not read implementation source/tests, private evaluation criteria, or unrelated package artifacts.

## Isolation and write set

- Do not modify `TECHNICAL-PLAN.md`, B/C, Charter, implementation, tests, or any other candidate.
- Write only `docs/overnight/2026-10-01/M3-SNAPSHOT-PLAN-V2-RECHECK.md` with exact input hashes, anchors, result, findings, and limits.
- The D author retains Plan acceptance responsibility. This recheck does not record that acceptance and does not authorize case-2 E/F.
