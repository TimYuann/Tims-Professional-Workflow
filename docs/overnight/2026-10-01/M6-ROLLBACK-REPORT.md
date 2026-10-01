# M6 · controlled-copy rollback rehearsal · d672914

**State:** Driver-run recovery rehearsal passed in a separate temporary controlled copy. This is not an independent verifier verdict or M6 acceptance.

## Fixed source object

- Commit: `d672914ac80eeed0aa5f04a0c80f448acc9de6f3`
- Tree: `c88b662421bc44270fdf38bf43267010fe0a1d38`
- Source archive SHA-256: `e2571ca9cca6148378d1b6ec1a580c0432252727e135fa0bb29f59ec23c5a39d`
- Recovery source: local Git object `d672914…`; no remote fetch, branch change, commit, or tag.
- Controlled scratch: `/private/var/folders/vq/dk3gntzd7dz529mp_57ybgyh0000gn/T/tpw-m6-rollback-exercise-d672914/`. The fixed `.worktrees/verification/tpw-m6-*` package copies were left untouched.

## Observed sequence

1. Extracted `professional-workflow/` from the fixed commit into `broken/` and `recovered/`. Before injection, `shasum -a 256 -c SHA256SUMS` in `broken/` passed all 19 files.
2. Simulated a recoverable package failure only in the controlled `broken/` copy by moving `methods/local-defect-feedback-loop.md` to `broken/withheld/`. The file bytes were preserved (SHA-256 `1ba8f8f2fb46a0094c22e7ac946e27f30a27b1ce25e201fd5ede819ddc2e4215`).
3. Ran the documented E assembly from `broken/professional-workflow/` with the synthetic caller input. It exited `1` and reported `cat: methods/local-defect-feedback-loop.md: No such file or directory`.
4. After that failure, re-extracted the exact `d672914…` object into `recovered/`, copied the external 19-file manifest and the same synthetic caller input, then ran `shasum -a 256 -c SHA256SUMS`: all 19 files passed.
5. Re-ran the same documented E assembly from `recovered/professional-workflow/`; it produced SHA-256 `713925256a7eb3157697edd60baaf9a3762d16cddf373d0bef8347c0e6f7b181`, matching the earlier M6 package-candidate assembly output.

Assembly command from the recovered package root:

```sh
cat profiles/implementation.md \
    charters/examples/implementation-local-fix.md \
    methods/local-defect-feedback-loop.md \
    ../smoke-task-input.md | shasum -a 256
```

## Limits

- This demonstrates recovery of the package object and a working assembly in a controlled copy. It does not prove recovery of an application database, runtime service, or deployment.
- The failure was injected in a separate scratch copy; no package bytes in the validation worktrees or main package were changed.
- A separate M6 verifier has not yet reviewed this rollback report. M3 case 2 remains blocked at PC-1, so overall M5/M6 closure is still open.
