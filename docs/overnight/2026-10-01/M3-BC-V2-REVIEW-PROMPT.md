# M3 case 2 · bounded B/C v2 independent review

- **Reviewer:** `tpw-night-method`, independent of the B/C author and Driver.
- **Fixed candidate B:** `fixtures/m3-snapshot/BEHAVIOR-CONTRACT.md`, SHA-256 `6cf43d3fb647cf2c250f275179762917c0763a669e84f1718d85968a8e66c738`.
- **Fixed candidate C:** `fixtures/m3-snapshot/DOMAIN-SEMANTICS.md`, SHA-256 `d35766b45085db2b7e5b3315cca5ce4183f722186a850ef317fd571ebba6d45b`.
- **Prior accepted inputs:** B v1 / C v1 are recoverable at commit `893eaf8`; the independent challenge is `M3-SNAPSHOT-PLAN-CHALLENGE.md`, SHA-256 `bf3e15de71f4bf82adaa5547b9c412b4384a90d9d919420d5023fd9f593ab126`.

## Review question

Give one three-state result (`PASS`, `FAIL`, or `UNVERIFIED`) for whether these exact B/C v2 objects resolve the challenge's bounded PC-1 and PC-2 points while preserving the previously accepted B/C claims.

1. **PC-1:** Check that the recorded source hashes now identify the accepted investigation baseline, rather than impose a standing no-change condition; that in-scope `src/**` and `tests/**` changes can inherit acceptance only while preserving the stated behavior/terms/invariants; and that re-opening conditions identify changes that exceed that scope without silently authorizing changed semantics.
2. **PC-2:** Check that the aggregate recipe unambiguously sorts by relative path, states the line encoding/final newline/hash operation, and correctly distinguishes the digest-line-sorted alternative.
3. Compare B-1…B-6, P-1…P-3, B-O1…B-O2, the C term definitions, DS-I1…I7, and DS-U1…U4 against the accepted v1 objects at `893eaf8`. Confirm the claimed v2 semantic preservation, not merely its change-log statement.
4. Report any newly introduced scope, authority, or dependency ambiguity that would affect the B/C acceptance boundary. Keep findings limited to these fixed B/C objects and the cited challenge.

## Isolation and write set

- Do **not** read `fixtures/m3-snapshot/src/**`, `fixtures/m3-snapshot/tests/**`, implementation outputs, private evaluation criteria, or the D Plan. The implementation and its expected results are outside this review input.
- Do not edit B/C, the D Plan, implementation, tests, or other artifacts.
- Write only `docs/overnight/2026-10-01/M3-BC-V2-REVIEW.md`, with exact input hashes, commands/anchors used, result, findings, and limits.
- This is bounded input/claim review only. It does not accept the D Plan, authorize E, evaluate implementation, or accept M3.
