# M6 · fixed export and qualification evidence report

**State:** fixed 19-file export with case-1 cold-start and controlled-copy rollback evidence; **M6 is not accepted**. The full Pro audit remains unused (`0/2`).

## Export identity

- Source commit: `d672914ac80eeed0aa5f04a0c80f448acc9de6f3`
- Source tree: `c88b662421bc44270fdf38bf43267010fe0a1d38`
- Root: `professional-workflow/`
- 19-file manifest SHA-256: `c40b31e87bdad8374af0bf7b393bec5583dd45deee38601e4fed324c669f1ad0`
- Deterministic archive SHA-256: `e2571ca9cca6148378d1b6ec1a580c0432252727e135fa0bb29f59ec23c5a39d`
- Candidate and manifest details: `M6-PACKAGE-CANDIDATE-d672914.md`, SHA-256 `af6a7653baaefcaffe3a8fdc0d8c5c6f1d86839822beb37e1acb6afcbec338c3`.

## Cold-start sample

- E self-report: `M6-COLDSTART-REPORT.md`, SHA-256 `ffc254f3e69ba0b6213efa584abdbdfeecc23d056ed81db39a493fe167a93a73`.
- Independent verifier: `M6-COLDSTART-VERIFICATION.md`, SHA-256 `2b80184e0f0b83eddf4dbb196fa60a15a613ac8077a8f8dd79c94566395b1576`; PASS for the fixed d672914 case-1 sample.
- The independent verifier matched the 19-file manifest and supplied hashes, reproduced 7/7 candidate tests, reproduced the baseline failure using an in-memory pre-change function, checked a remove-all negative control, and observed package/case1/manifest identity before and after.
- The author was a fresh case-1 cold-start session before workspace migration, then restored with the same session identity/CWD. Migration added no independence. This sample is not a package-wide startup acceptance.

## Controlled-copy rollback

- Driver rehearsal: `M6-ROLLBACK-REPORT.md`, SHA-256 `611a41aa1dcfdb4e80f85953a55b0240a43f7b842688bf9adb39540618a6bcd5`.
- Independent read-only verification: `M6-ROLLBACK-VERIFICATION.md`, SHA-256 `b7c1fb5ac97bb6b624136567446b135a95fc28214517dc2910c7569b782f8e64`; PASS for the controlled-copy evidence.
- The reviewer matched the missing-method manifest/assembly error, withheld method digest, all 19 recovered manifest entries, and recovered assembly digest against a fresh extraction of d672914. It observed no scratch/verification-copy writes during its review window.
- The report notes an extra `restored/` copy, byte-identical to `recovered/` (O1).

## Scope limits

- These reports do not prove application/database/runtime recovery, the recovery action itself from first principles, production deployment, or overall M6 acceptance.
- The rollback verifier did not re-establish the pre-injection 19/19 state, did not hash the scratch tree before its review, and did not independently verify the untouched state of `.worktrees/verification` copies; it used mtime evidence during its window. These limits remain explicit.
- The cold-start sample covers the specified case-1 startup task only. It does not establish all routes, all Profiles, or final M3/M5 acceptance.
- M3 has a self-contained report ready for Oracle/Owner acceptance at `M3-REPORT.md`, SHA-256 `c8cac65c835604b0d6f67059d88d90f9fc8d92d4a605b7d365260247baf60915`; no overall M3 acceptance is yet recorded.
- No Pro review or branch push has occurred; no tag, merge, UCBIP change, or release action occurred.

## Requested Oracle/Pro review

From the exact fixed night-branch commit, read the complete package, 19-file external manifest/archive identity, M6 candidate report, cold-start E/F reports, rollback rehearsal and independent review, plus final M3/M5 acceptance state. Assess whether the export is self-contained and whether the stated cold-start/rollback evidence supports only the claimed scope. Keep the review bound to the exact GitHub connector repo/branch/commit, and preserve the explicit gaps above.

The Owner-authorized M6 Pro slot remains unused. Oracle chooses whether and when to submit it.
