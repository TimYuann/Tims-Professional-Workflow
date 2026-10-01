# M3 case 1 · independent F evaluation

- **Evaluator:** `tpw-night-method` (the evaluator has already held the case criteria independently).
- **Fixed candidate:** commit `9699276ab1d413379ace91afa0cf683a83b69aa3`; evaluate only the code and tests under `fixtures/m3-local-fix/` from this commit.
- **Charter:** `fixtures/m3-local-fix/EVALUATOR-CHARTER.md` at that same commit. It binds the accepted M4 behavior-claim method and defines the evaluation claim, evidence, limits, and output path.
- **Inputs:** `CONTRACT.md`, `TASK-INPUT.md`, and pre-change `BASELINE.md` from the same fixed candidate commit. Compare baseline and treatment using the same command and environment; use the original baseline observation where it remains suitable.
- **Independence:** Use the case criteria already held in your session. Do not add their contents to this prompt, the repository, or the implementation input. Do not rely on E's self-check as the conclusion.
- **Write set:** Write only `docs/overnight/2026-10-01/M3-LOCAL-EVALUATION.md`. Do not modify code, tests, Charters, baseline, or contract.
- **Output:** State the exact candidate commit, command, exit/output, observed behavior, coverage, limitations, and one of PASS/FAIL/UNVERIFIED. Do not accept residual risk or authorize release/deployment.

This evaluation covers commit `9699276...` only. If the method-bound E pass creates a later code/test commit, evaluate that version only if those code/test bytes differ.
