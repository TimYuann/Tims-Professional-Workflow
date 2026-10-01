# M6 · read-only verification of the controlled-copy rollback

- **Verifier:** the independent M6 verifier session `tpw-night-m5-review`; verifier is separate from the Driver who ran the rehearsal.
- **Fixed package object:** `d672914ac80eeed0aa5f04a0c80f448acc9de6f3`, tree `c88b662421bc44270fdf38bf43267010fe0a1d38`; 19-file manifest in the verification export.
- **Evidence report:** `docs/overnight/2026-10-01/M6-ROLLBACK-REPORT.md`, SHA-256 `611a41aa1dcfdb4e80f85953a55b0240a43f7b842688bf9adb39540618a6bcd5`.
- **Read-only scratch:** `/private/var/folders/vq/dk3gntzd7dz529mp_57ybgyh0000gn/T/tpw-m6-rollback-exercise-d672914/`. Inspect the preserved `broken/`, `withheld/`, and `recovered/` evidence. Do not write, rename, delete, commit, or run a mutating restore. Do not inspect or alter `.worktrees/verification` package copies.
- **Verify:** the injected missing-method assembly failure and its exact stderr/exit; the withheld method file digest; all 19 hashes in `recovered/SHA256SUMS`; and the recovered E-assembly digest against the fixed d672914 candidate.
- **Write set:** only `docs/overnight/2026-10-01/M6-ROLLBACK-VERIFICATION.md` in the main worktree.
- **Output:** PASS/FAIL/UNVERIFIED with the exact object, paths, commands/results, and coverage limits. This does not accept M6, prove application data recovery, or change the no-Pro/no-publish status.
