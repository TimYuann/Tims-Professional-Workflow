# M6 · Read-Only Verification of the Controlled-Copy Rollback

- **Verifier:** the independent M6 verifier instance (`tpw-night-m5-review`), separate from the Driver who ran the rehearsal.
- **Basis:** `docs/overnight/2026-10-01/M6-ROLLBACK-VERIFY-PROMPT.md`, SHA-256 `d05ee75a0b954f9bc8d64f0f434500098d57d32efbc16f38fb799859ccfcb94b` (re-verified; matches).
- **Fixed package object:** commit `d672914ac80eeed0aa5f04a0c80f448acc9de6f3`, tree `c88b662421bc44270fdf38bf43267010fe0a1d38`.
- **Evidence report:** `docs/overnight/2026-10-01/M6-ROLLBACK-REPORT.md`, SHA-256 `611a41aa1dcfdb4e80f85953a55b0240a43f7b842688bf9adb39540618a6bcd5` (re-verified; matches).
- **Read-only scratch:** `/private/var/folders/vq/dk3gntzd7dz529mp_57ybgyh0000gn/T/tpw-m6-rollback-exercise-d672914/`.
- **Conduct:** read-only inspection and re-execution of the documented assembly command; nothing was written, renamed, deleted, or committed in the scratch directory or in `.worktrees/verification`; scratch mtimes showed zero files modified within this verification window. The only write is this report in the main night worktree.

## 1. Preserved evidence inventory — PASS

| Location | Contents |
| --- | --- |
| `broken/` | `professional-workflow/` with 18 files (method file absent), `broken/withheld/local-defect-feedback-loop.md`, `broken-assembly.txt`, `broken-assembly.stderr`, 19-entry `SHA256SUMS`, `smoke-task-input.md` |
| `recovered/` | `professional-workflow/` with 19 files, 19-entry `SHA256SUMS`, `smoke-task-input.md` |
| scratch root | `SHA256SUMS` (same 19-entry manifest), `smoke-task-input.md` |
| additional | `restored/` — a complete 19-file copy, byte-identical to `recovered/` (Observation O1) |

`broken/withheld/local-defect-feedback-loop.md` hashes to `1ba8f8f2fb46a0094c22e7ac946e27f30a27b1ce25e201fd5ede819ddc2e4215`, which is the fixed d672914 method bytes pinned in `methods/README.md`. The scratch-wide file inventory totals 67 files with no symlinks.

## 2. Injected missing-method failure — PASS

- `shasum -a 256 -c SHA256SUMS` in `broken/`: exit `1`, 18 `OK`, exactly one `FAILED open or read` — `professional-workflow/methods/local-defect-feedback-loop.md`.
- Re-ran the documented E assembly from `broken/professional-workflow/` (`cat profiles/implementation.md charters/examples/implementation-local-fix.md methods/local-defect-feedback-loop.md ../smoke-task-input.md`): exit `1`; stderr exactly `cat: methods/local-defect-feedback-loop.md: No such file or directory`; stdout and stderr were byte-identical to the preserved `broken-assembly.txt` (`0043581c1dbf9731a0faa8a3d8d02798c6b554deff46e6da242a15f0014c4e37`) and `broken-assembly.stderr` (`98e1ed41015c0091c1e28cc5cfa9ca29d2c0d28c415aec632e5a56f0eced8d63`).

## 3. Withheld method digest — PASS

The withheld file digest `1ba8f8f2…e4215` matches (a) the recovered copy's method file, (b) the manifest entry, and (c) the d672914 candidate digest recorded in `methods/README.md`. The bytes were preserved, not altered, while the file was absent from `broken/professional-workflow/methods/`.

## 4. Recovered manifest — PASS

- `shasum -a 256 -c SHA256SUMS` in `recovered/`: exit `0`, **19 `OK`, 0 failed**.
- The manifest is byte-identical to a fresh recomputation from the fixed object: `git archive d672914 professional-workflow | tar -x` then `find … | shasum -a 256` produced the same file set and hashes (manifest file hash `c40b31e87bdad8374af0bf7b393bec5583dd45deee38601e4fed324c669f1ad0` in root, `broken/`, `recovered/`, and `restored/`).
- The `broken/` manifest is the same valid 19-entry manifest; its only failure is the one missing file, so the report's "before injection 19/19 passed" is consistent with the preserved evidence (the pre-injection run itself is not replayable).

## 5. Recovered E-assembly against the fixed d672914 candidate — PASS

- `recovered/professional-workflow/` assembly digest: `713925256a7eb3157697edd60baaf9a3762d16cddf373d0bef8347c0e6f7b181`.
- Independently recomputed from a fresh extraction of commit `d672914` with the same `smoke-task-input.md`: **same digest**, byte-identical assembled text.
- The digest is the one recorded as "Extracted-package local assembly hash" in `docs/overnight/2026-10-01/M6-PACKAGE-CANDIDATE-d672914.md:47`, i.e. the report's "earlier M6 package-candidate assembly output".
- The report's source-archive hash `e2571ca9cca6148378d1b6ec1a580c0432252727e135fa0bb29f59ec23c5a39d` also reproduces exactly with `git archive d672914 professional-workflow | shasum -a 256` (and is referenced in the same candidate note and `DECISIONS.md`).

## 6. Verdict

**PASS for the controlled-copy rollback evidence** — the injected absence of the method file produces exactly one manifest failure and the exact recorded `cat` error/exit; the withheld file's bytes are intact; all 19 recovered hashes verify; and the recovered E-assembly is byte-identical to the fixed d672914 candidate assembly. This is evidence about the package object and the controlled copy only.

**Not claimed:** application database/runtime/deployment recovery, M3 case-2/PC-1, M6 acceptance, or any change to the no-Pro/no-publish status.

## Observation

- **O1 (minor):** the scratch contains an additional `restored/` copy (timestamp `12:27:29`, complete 19-file package, byte-identical to `recovered/`) that the rollback report does not mention. It does not contradict any claim — every byte matches the fixed object — but the report's narrative account of the scratch would be complete if it named this copy.

## Coverage limits

- The report's claim that the fixed `.worktrees/verification/tpw-m6-*` package copies were untouched was **not verified**: the prompt prohibits inspecting or altering those copies, so it remains an unverified statement (no contradicting evidence was seen).
- The pre-injection `broken/` 19/19 manifest pass is a past state; only its consistent end state (valid manifest plus all 19 digests present across copy and withheld file) could be checked.
- Recovery provenance (fresh Git extraction versus any other byte-identical source) is not observable; what is verified is exact byte identity of `recovered/` with the fixed `d672914` package object.
- The scratch directory was not re-hashed before this verification began (only mtime-based non-modification within the window); all inspected evidence is internally consistent with the recorded hashes.
- The negative/positive checks were re-executed as read-only commands; no mutating restore was attempted, so the recovery action itself is not independently reproduced.

## Appendix · Key commands and results

```sh
S=/private/var/folders/vq/dk3gntzd7dz529mp_57ybgyh0000gn/T/tpw-m6-rollback-exercise-d672914

shasum -a 256 docs/overnight/2026-10-01/M6-ROLLBACK-REPORT.md     # 611a41aa… (matches)
shasum -a 256 "$S/broken/withheld/local-defect-feedback-loop.md" # 1ba8f8f2… (matches fixed candidate)

(cd "$S/broken"    && shasum -a 256 -c SHA256SUMS)  # exit 1, 18 OK / 1 FAILED (missing local-defect method)
(cd "$S/recovered" && shasum -a 256 -c SHA256SUMS)  # exit 0, 19 OK / 0 failed

# documented E assembly, broken copy (exit 1; stderr and stdout byte-identical to preserved evidence)
(cd "$S/broken/professional-workflow" && cat profiles/implementation.md \
    charters/examples/implementation-local-fix.md methods/local-defect-feedback-loop.md \
    ../smoke-task-input.md > /tmp/broken-repro.out 2> /tmp/broken-repro.err); echo $?   # 1

# recovered assembly digest
(cd "$S/recovered/professional-workflow" && cat profiles/implementation.md \
    charters/examples/implementation-local-fix.md methods/local-defect-feedback-loop.md \
    ../smoke-task-input.md | shasum -a 256)     # 71392525…

# same digest from a fresh extraction of the fixed commit
git archive d672914ac80eeed0aa5f04a0c80f448acc9de6f3 professional-workflow | tar -x -C /tmp/m6-rb-check
(cd /tmp/m6-rb-check/professional-workflow && cat profiles/implementation.md \
    charters/examples/implementation-local-fix.md methods/local-defect-feedback-loop.md \
    "$S/smoke-task-input.md" | shasum -a 256)   # 71392525… (identical)

git archive d672914ac80eeed0aa5f04a0c80f448acc9de6f3 professional-workflow | shasum -a 256
                                                    # e2571ca9… (matches report)
```
