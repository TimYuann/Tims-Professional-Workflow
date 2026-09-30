# M3 case 1 · evidence-evaluation Charter

- **State:** active for post-implementation evaluation of this fixture
- **Profile:** `professional-workflow/profiles/evidence-evaluation.md` (M1 accepted; SHA-256 `d72b3a5097f142f5ea397ab423b146a3b853913c5c1de096d93b95133199f900`)
- **Instance:** `tpw-night-method`
- **Independence:** This instance did not author the fixture, contract, baseline or implementation candidate. It did review method documents; it has not contributed to this implementation.

## Evaluation object and claim

- **Object:** the fixed implementation commit and diff for `fixtures/m3-local-fix/`.
- **Claim:** the implementation restores the exercise contract in `CONTRACT.md` while preserving the function interface, error behavior and test evidence.
- **Accepted inputs:** `CONTRACT.md`, `TASK-INPUT.md`, `BASELINE.md`, and the implementation Charter, each fixed by the M3 seed commit.

## Evaluation work and limits

- Reproduce the baseline and compare it with the candidate using the same local command, data and Python environment where possible.
- Observe the original failing input, existing passing behaviors, and any added focused coverage. Report object/version, exact command/output, coverage and environment limits.
- Treat a valid counterexample as evidence against the claim. Invalid or unavailable observations are `UNVERIFIED`, not a product failure. Use only `PASS`, `FAIL`, or `UNVERIFIED`.
- Do not modify the implementation, contract, baseline, or tests. Do not accept residual risk or authorize release, deployment or any external action.
- Write the evaluation only after the implementation candidate is fixed, to `docs/overnight/2026-10-01/M3-LOCAL-EVALUATION.md`.
