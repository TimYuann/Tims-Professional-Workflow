# M3 case 2 · reconcile D Plan after confirmed B/C v2

- **D owner:** `tpw-night-m3-design`; write only `fixtures/m3-snapshot/TECHNICAL-PLAN.md`.
- **Current working candidate before this task:** SHA-256 `f081c1c3e165a7ab192bb89d82957c482800feacd4cb6c1fbb114ef4719603c1`.
- **Fixed B input:** `fixtures/m3-snapshot/BEHAVIOR-CONTRACT.md`, SHA-256 `6cf43d3fb647cf2c250f275179762917c0763a669e84f1718d85968a8e66c738`.
- **Fixed C input:** `fixtures/m3-snapshot/DOMAIN-SEMANTICS.md`, SHA-256 `d35766b45085db2b7e5b3315cca5ce4183f722186a850ef317fd571ebba6d45b`.
- **Independent B/C v2 review:** `M3-BC-V2-REVIEW.md`, SHA-256 `675f32ded97ed90013db7eb4d0e6e6ea56fdce702f28ad1ba9e94124a303d091`, PASS for PC-1/PC-2 and preservation of the stated v1 claims.
- **Prior Plan challenge:** `M3-SNAPSHOT-PLAN-CHALLENGE.md`, SHA-256 `bf3e15de71f4bf82adaa5547b9c412b4384a90d9d919420d5023fd9f593ab126`.

## Task

Reconcile only the affected D Plan claims and dependency references against the fixed B/C v2 inputs and review result. Preserve D's accepted scope, strategy, and existing non-affected claims.

1. Replace stale B/C v1 identities/conditions with the exact v2 identities and the clarified accepted-baseline rule. Resolve the old PC-1/R-2/U-6 block and every duplicated statement that currently says E is barred solely because in-scope `src/**` or `tests/**` bytes change. Preserve all actual delegation, authority, scope, and semantic-change re-open conditions; this task does not itself authorize implementation.
2. Align the Plan's aggregate-recipe statements with the corrected relative-path ordering (PC-2). Mark the old recipe wording/factual explanation as superseded where needed; do not keep a contradictory active R-10 or locale explanation.
3. Keep PC-3/R-9 as the already bounded provenance-recording item. Do not turn it into a new method or acceptance gate.
4. Update the Plan's exact B/C references, challenge disposition, validation/implementation eligibility text, unresolved points, and independence/status wording wherever affected. Do not change the B/C documents, Charter, implementation, tests, or any other file.
5. Return the revised complete Plan as an unfixed working candidate with its exact SHA-256 and a short list of affected sections. Do not claim independent review or acceptance by this task. No case-2 E/F work starts here; after the fixed diff is inspected, Driver will route only the affected Plan claims for independent recheck.
