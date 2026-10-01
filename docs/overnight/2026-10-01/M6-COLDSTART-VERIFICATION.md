# M6 · Independent Cold-Start Verification · case 1

- **Verifier:** the independent reviewer instance designated in the prompt (`tpw-night-m5-review`); it did not author `COLDSTART-REPORT.md`, the case1 changes, or the cold-start session output.
- **Verification basis:** `docs/overnight/2026-10-01/M6-COLDSTART-VERIFY-PROMPT.md`, SHA-256 `8524cdc4d3c60f4615b4b4ce8b7364869457878f4ec02ff40579e358c6978ef7` (recorded value re-verified; matches).
- **Package object:** commit `d672914ac80eeed0aa5f04a0c80f448acc9de6f3`, tree `c88b662421bc44270fdf38bf43267010fe0a1d38`; read-only copy at `/Users/yuantian/Developer/tim-professional-workflow/.worktrees/verification/tpw-m6-coldstart-d672914/professional-workflow/`. The copy was verified byte-identical to the d672914 package (19/19 files, SHA-256).
- **Candidate exercise object:** `case1/` in the same read-only copy.
- **Conduct:** read-only verification; no package or case1 byte was changed, no commit was made in the verification copy, and no legacy role/compose/history record, held F criterion, or UCBIP material was inspected. A full before/after SHA-256 snapshot of all 30 package+case1+manifest files was identical after the verification runs. The only write is this report in the main night worktree.

## 1. Fixed hashes — PASS

**Package manifest** (`shasum -a 256 -c SHA256SUMS` in the verification copy): all 19 `professional-workflow/` entries `OK`. Independently, the 19-file copy equals the d672914 package tree file-for-file (same SHA-256 set, 19/19). The manifest's method/Profile digests match the pins established by the M5 repair, including `methods/local-defect-feedback-loop.md` `1ba8f8f2…`, `methods/README.md` `24de9ce2…`, and the frozen Backbone `ce82a700…`.

**Prompt-listed candidate hashes** — all match the actual case1 bytes:

| Object | Prompt value | Observed |
| --- | --- | --- |
| `case1/COLDSTART-REPORT.md` | `ffc254f3e69ba0b6213efa584abdbdfeecc23d056ed81db39a493fe167a93a73` | match |
| `case1/src/labels.py` (post-fix) | `f767787ba2ac8cf52e7b4f62e74b146b858fad91031bed139c849c9e23a92f87` | match |
| `case1/tests/test_labels.py` (supplied) | `8dbf28589f9e4ce34cc36aa87df88a8aeed63cb260214d3bf1997f0fe396bb06` | match |
| `case1/tests/test_labels_regression.py` (added) | `a60868486e9652bf8c83fe4ff661654ed80df34d78227fde26f1d8e9280ece5f` | match |

**Report §3 input and pin hashes** — recomputed against the actual bytes:

- Case1 inputs: Charter `2da085ba…`; Invitation `100b3926…`; CONTRACT `ecfc6195…`; TASK-INPUT `90b7e06d…`; BASELINE `6e8262b6…`; seed `src/__init__.py` `01668323…` (all match the report).
- Seed commit `04521323d0afdb44da99e839bb3a21535dd551c6`: seed `src/labels.py` (pre-fix) `0507c9e7…`, `tests/test_labels.py` `8dbf2858…`, CONTRACT/TASK-INPUT/BASELINE identical to the case1 copies — confirming the report's statement that the supplied test file was carried over unchanged (not weakened) and the candidate derives from the recorded seed.
- M4 acceptance pins: `3ca23a74…` (local-defect method) and `72a6ffb4…` (M4 selection entry) recomputed from commit `0136593…`, matching the report's citations. `authority/RESPONSIBILITY-BACKBONE.md` still recomputes to `ce82a700…`.
- Diff of seed `src/labels.py` against the shipped candidate: exactly one line, `value.strip().upper()` → `" ".join(value.split()).upper()`.

## 2. Sample behavior — PASS

All runs from `case1/` with `PYTHONDONTWRITEBYTECODE=1` and `python3` = Python 3.14.4 (matches BASELINE.md):

1. **Documented command:** `python3 -m unittest discover -s tests -v` → exit `0`, **7 tests ran, all OK** (the 4 supplied tests plus 3 regression tests), matching report §4 item 4.
2. **Retained negative control (pre-change behavior substituted in memory before test discovery):** exit `1`, 2 failures — the retained original `test_collapses_internal_whitespace` and the new `test_collapses_mixed_internal_whitespace_to_single_ascii_space`, with `'NORTHERN   STAR' != 'NORTHERN STAR'`. This reproduces BASELINE.md's recorded failure exactly and shows the green suite is not vacuous; no file bytes were altered (substitution was `src.labels.normalize_label` in memory before discovery).
3. **Supplementary remove-all-variant check:** exit `1`, 4 failures including `test_single_internal_space_is_preserved_not_removed` — the regression test described as the negative control does distinguish collapse-to-one from remove-all.
4. **Direct original failing scenario:** `normalize_label(' \tNorthern   Star\n')` → `'NORTHERN STAR'` (exit `0`), matching report §4 item 5.
5. **Report §4 item 2 spot-check (contract cases):** independently re-ran the four contract cases — C2 `" ".join(value.split()).upper()` and C4 `re.sub(r"\s+", " ", value).strip().upper()` pass all four; C3 remove-all fails the reported case and `"north star"`; C1 pre-change fails the reported case. Consistent with the report.

## 3. Report claims against actual package objects — PASS

- **Profile/method/Charter selection:** all digests cited in report §1/§3 match the package manifest and the M4 source commit; the mapping "known local defect → `local-defect-feedback-loop.md`" matches `methods/README.md`, and not binding `evidence-evaluation.md` (F) is consistent with Backbone §3 F (the evaluator must not be the candidate's implementer) and §6 combination boundaries, and with `profiles/implementation.md` ("self-check is evidence input, not the independent conclusion").
- **Authority/recall/closure statements:** the delegation line matches the actual `M6-COLDSTART-CHARTER.md`; the recall description matches Backbone §3 E and §4; the closure separation ("acceptance ≠ verification ≠ action ≠ closure") matches Backbone §2/§4 and the Charter's "Independence / closure" clause. No contradictory claim found.
- **Changed paths:** only `case1/src/labels.py` and `case1/tests/test_labels_regression.py` are new relative to the seed; the copy contains no stray artifact (19 package + 10 case1 + manifest). Supplied `tests/test_labels.py` is byte-identical to the seed.
- **Recorded path deviation:** the Charter does cite `/private/tmp/tpw-m6-export-d672914/case1/`, while the report's workspace `/private/tmp/tpw-m6-coldstart-d672914/` exists — the deviation is accurately recorded, not silently resolved.

**Observation O1 (minor, disclosed by the report):** the report describes the whitespace class as inherited from the pre-existing `strip()` (`str.isspace()`), which is accurate, but internal NBSP behavior does observably change with the fix: `normalize_label("a\u00a0b")` is now `'A B'` whereas pre-change it returned `'A\u00a0B'`. This is consistent with the contract's "collapse each internal run of whitespace to one ASCII space" under that class and the report explicitly flags NBSP as uncovered by accepted evidence, so it remains a disclosed remaining fact rather than a contradiction.

## 4. Verdict

**PASS for this cold-start sample** — the fixed package/case1/report hashes all match the recorded values, the documented command reproduces the reported green result on the frozen bytes, and the in-memory negative controls show the retained tests detect the pre-fix and remove-all behaviors. This verdict covers hash identity and sampled behavior only.

**Not claimed:** independent F evaluation, M6 acceptance, M3 whole-chain completion, or any product/UCBIP conclusion.

## Coverage limits

- The cold-start session's internal isolation claims (e.g. "no prior conversation or evaluator criteria were read") are self-reported and cannot be verified from the artifacts; this verification can only confirm that no contradicting material appears in the fixed objects.
- The original cold-start run's transcripts were not replayed; the same commands were re-run on the frozen bytes, which is equivalent for deterministic behavior but not proof of the original process.
- `.pi/` loop state in the verification copy (untouched, mtime before this verification) was not part of the package/case1 verification and was not modified.
- This verification is bound to the d672914 package copy and the case1 bytes listed above; later commits or edits are outside its scope.

## Appendix · Key commands

```sh
V=/Users/yuantian/Developer/tim-professional-workflow/.worktrees/verification/tpw-m6-coldstart-d672914

# package manifest and copy identity
(cd "$V" && shasum -a 256 -c SHA256SUMS)
# compare /tmp/m6-d672914-pkg (git archive of d672914) with the copy's SHA256SUMS -> 19/19 identical

# case1 candidate hashes
shasum -a 256 "$V"/case1/{src/labels.py,tests/test_labels.py,tests/test_labels_regression.py,COLDSTART-REPORT.md}

# documented test command
(cd "$V/case1" && PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v)   # exit 0, 7 tests OK

# retained negative control (in-memory pre-change strip().upper(), before discovery)
(cd "$V/case1" && PYTHONDONTWRITEBYTECODE=1 python3 -c '
import src.labels as L
def pre_change(v):
    if not isinstance(v, str): raise TypeError("value must be a string")
    return v.strip().upper()
L.normalize_label = pre_change
import unittest
r = unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().discover("tests"))
raise SystemExit(0 if r.wasSuccessful() else 1)')                                     # exit 1, 2 expected failures

# immutability: before/after SHA-256 snapshot of package+case1+manifest identical
```

*Outputs quoted in sections 1–2 are the observed console results; the negative-control substitution existed only in the process memory and left no bytes on disk.*
