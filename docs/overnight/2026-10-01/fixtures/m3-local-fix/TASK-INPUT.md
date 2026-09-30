# M3 case 1 · task input

The isolated fixture has an existing, versioned behavior contract at `CONTRACT.md` and a deterministic failing observation recorded in `BASELINE.md`.

Repair the local defect in `src/labels.py` while preserving the contract. Return the patch, the exact verification command and output, and any remaining facts or deviations. The contract, tests, and task input are read-only exercise inputs.

Only this offline fixture is in scope. Existing tests and contract are evidence inputs: do not weaken their expectations to make the patch pass. You may add local tests under `tests/` if useful. Do not access external services, production data, UCBIP, or other repository paths. No D redesign is requested; if the existing function boundary cannot preserve the contract, report the affected object and reason to Driver before crossing it.
