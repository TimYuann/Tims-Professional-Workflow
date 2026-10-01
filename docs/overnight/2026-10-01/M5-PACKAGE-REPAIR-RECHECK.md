# M5 · Targeted Recheck of Package-Review Findings F1–F4

- **Reviewer:** the same independent Flash instance that wrote `M5-PACKAGE-INDEPENDENT-REVIEW.md` (file SHA-256 `53ed90a006fe0e58db1344c571a49febd59acfb4b1ea918c78178285570a2ecc`, re-verified on the current worktree).
- **Recheck basis:** `docs/overnight/2026-10-01/M5-PACKAGE-REPAIR-PROMPT.md`, SHA-256 `33602146bd1899d833b0d3238ddc363b3ee6b93e2d08680b213dcd8f5d620a18` (recorded value re-verified; matches).
- **Fixed object:** commit `d672914ac80eeed0aa5f04a0c80f448acc9de6f3`, tree `c88b662421bc44270fdf38bf43267010fe0a1d38`, package root `professional-workflow/` (19 files).
- **Prior reviewed package:** commit `f11de8b4b35015b14dfc50dd94d19525e424cd07` (package-review object).
- **Method:** `git archive d672914… professional-workflow | tar -x` into a temporary directory; all digest recomputations were executed against Git objects of the fixed commit, the M4 acceptance commit (`0136593…`, tree `2fc8db5e…`) and the prior reviewed commit; no network, no legacy role/compose files, no UCBIP, no package writes. The only write is this report.
- **Scope:** F1–F4 only. This is a targeted recheck, not M5/M6 acceptance or Pro audit.

## Object state observed

| Check | Observed |
| --- | --- |
| `d672914…` is a commit; tree equals `c88b6624…` | exact match; message `docs: pin M5 method package bytes and paths` |
| Package inventory | 19 files under `professional-workflow/` |
| Delta vs prior reviewed commit `f11de8b` | 6 files: `README.md`, `authority/README.md`, 3 example Charters, `methods/README.md` (+16/−8); all three method bodies untouched (see F1) |
| Worktree package vs `d672914` | clean (empty diff) |
| HEAD during recheck | moved to `149b342` (concurrent process note; package untouched); the fixed object was reviewed as extracted from `d672914` |

## F1 · Method byte identities and Charter pins — PASS

Every digest cited in the repaired package was recomputed from the actual Git objects and matches. Verified programmatically (all assertions passed):

| Package method file | Accepted M4 SHA-256 (`0136593…`) | M5 candidate SHA-256 at `d672914` | Cited in package |
| --- | --- | --- | --- |
| `methods/local-defect-feedback-loop.md` | `3ca23a74a1a1890123bbab01a114aba813d7e20a7ffcb21b7b2289d5047cb32c` | `1ba8f8f2fb46a0094c22e7ac946e27f30a27b1ce25e201fd5ede819ddc2e4215` | `methods/README.md` table; `charters/examples/implementation-local-fix.md:13` |
| `methods/cross-module-design.md` | `30066c8b3ccee2b85e98c8bc36975f57161e2c93d0bd71c9c668b27bf79bae6f` | `ab0a0bc03448407479fe82b92b2355384e7f2acf49c2ff3026882670f955a0a5` | `methods/README.md` table; `charters/examples/technical-planning-cross-module.md:13` |
| `methods/behavior-claim-evaluation.md` | `06b0692290a9ce8cdc7048b33a89ec21f3636ee00138a613121ec4b72457af06` | `cfacc0f57cedadc6360ad0338645e43740dad4b1e15cc6876088eb89b4034f02` | `methods/README.md` table (previously unpinned) |
| `methods/README.md` selection entry | `72a6ffb46277e3974f27d41e078623ce5b46865074898dae24cbdb6de2205e73` | `24de9ce294c682afd7c9930a1000b2c5b37fb5a518edb34e3544b21ba6c87538` | `methods/README.md` §Status and source trace, line 21 |

- Both example Charters now cite the accepted M4 source commit and digest *and* the current M5 candidate file digest; `behavior-claim-evaluation.md` now has both identities in `methods/README.md`, closing the prior unpinned-F-method gap.
- The package claims no longer conflate the two identities: `methods/README.md` states the M5 package bytes are not claimed as accepted, and `README.md:23` says `M4 acceptance does not itself accept the M5 package bytes`. The prior "accepted from M4 commit …" wording that contradicted the shipped bytes is gone (scan for `accepted from M4` / `accepted M4 references` → none).
- **No normative method-body changes:** all three method files are byte-identical between `f11de8b` and `d672914` (verified by SHA-256 equality; `git diff --stat f11de8b d672914 -- professional-workflow/methods/*.md` shows only `methods/README.md` changed). The repair is metadata/pins only.
- **Remaining affected path:** none. Residual (not a package defect): whether the M5 candidate bytes are themselves formally accepted remains an external acceptance question; the package now explicitly does not assert it.

## F2 · Supersession note for frozen M1 method-status text — PASS (with one residual observation)

- `README.md:23` now carries the supersession sentence: *"The M1-era “待 M4” labels remain in the frozen Profiles; for the three currently selected method references, use `methods/README.md`."*
- `profiles/` is unchanged at `d672914` (frozen M1 bytes; empty diff vs `f11de8b`), consistent with the package's declared M1 provenance and with the prior review's suggested location options.
- **Residual observation:** the documented E assembly does not include `README.md`, so the assembled startup text still contains the frozen label `绑定状态：候选，待 M4 归位后绑定；本预设不含方法正文` (`profiles/implementation.md`, appears as assembled-text line 41). The adjacent Charter line (assembled-text line 54) now pins both the accepted M4 digest and the current M5 file digest, so the assembly is no longer ambiguous about version identity, but the frozen label itself is only superseded at package-README level.
- **Remaining affected path:** `profiles/*.md` (intentionally frozen; residual only, no required package change per the prior recommendation).

## F3 · Provenance disclaimer for all source-history references — PASS

- The bundled Backbone contains exactly four filename-like source references: `WORKFLOW-INTENT.md` (line 6), `workflow/registry.yaml` (line 6), `history/derivation-0930/RESPONSIBILITY-BACKBONE-ORACLE-CHALLENGE-3.md` (line 179), `history/derivation-0930/RESPONSIBILITY-BACKBONE-MERGED-CHALLENGE-2.md` (line 180).
- `authority/README.md:15` now enumerates all four and states they are provenance references the package does not load or rely on at runtime. The Backbone blob is unchanged (`6cb486e5…`), and its export digest still recomputes to `ce82a70016a4a3fc234ea287f39aac8d79a260ddf13747c4fb705bda580453ba`.
- **Remaining affected path:** none.

## F4 · Package-root-relative Profile paths — PASS

- All three example Charters now use `profiles/implementation.md` / `profiles/technical-planning.md` with the qualifier "(relative to the `professional-workflow/` package root)" (`charters/examples/*.md:4`).
- No `professional-workflow/profiles/` occurrences remain anywhere in the package; the remaining `professional-workflow/` mentions are descriptive text (`charters/README.md:16`, the three new qualifiers). `template.md` still uses the generic `<profile path>` placeholder, which is consistent. All 5 relative Markdown links in the package resolve.
- **Remaining affected path:** none.

## Summary

| Finding | Previous state | Recheck result |
| --- | --- | --- |
| F1 method byte identities / Charter pins | Conflicting pins; stale M4-only claim; F method unpinned | **PASS** — M4 and M5 digests both recorded, all seven cited hashes verified, method bodies unchanged |
| F2 supersession note | Frozen "待 M4" labels with no supersession | **PASS** — note added at `README.md:23`; residual: frozen label remains inside the assembled E text (adjacent Charter now carries the correct dual pin) |
| F3 provenance disclaimer | Two `history/` references uncovered | **PASS** — all four source-history references enumerated |
| F4 Profile path convention | Parent-relative `professional-workflow/profiles/…` in example Charters | **PASS** — package-root-relative with explicit qualifier |

Boundaries of this recheck: only F1–F4 were rechecked; unrelated M3/M6 claims, upstream semantics, held case rubrics, and any acceptance decision were not re-reviewed. No upstream/network check was needed or performed this round. This result is not an M5/M6 acceptance.

## Appendix · Verification commands (evidence)

```sh
# object identity
git cat-file -t d672914ac80eeed0aa5f04a0c80f448acc9de6f3
git rev-parse d672914ac80eeed0aa5f04a0c80f448acc9de6f3^{tree}   # c88b6624…
git ls-tree -r d672914… professional-workflow/ | wc -l            # 19

# F1: recompute every cited digest from git objects (assertion script)
#   M4  = git show 0136593…:professional-workflow/methods/<f>.md | shasum -a 256
#   M5  = git show d672914…:professional-workflow/methods/<f>.md | shasum -a 256
#   cited values parsed from charters/examples/*.md:13 and methods/README.md table
#   -> all 7 cited digests match; M4 selection entry 72a6ffb4… also matches

# F1: no normative method-body change since prior review
git diff --stat f11de8b4b35015b14dfc50dd94d19525e424cd07 d672914… -- 'professional-workflow/methods/*.md'
#   -> only professional-workflow/methods/README.md changed

# F2/F3/F4: grep-based checks
git show d672914…:professional-workflow/README.md | sed -n '23p'                 # supersession sentence
git show d672914…:professional-workflow/authority/RESPONSIBILITY-BACKBONE.md | grep -noE '[A-Za-z0-9_./-]+\.(md|yaml)'   # exactly 4 refs
git show d672914…:professional-workflow/authority/README.md | sed -n '15p'        # all 4 enumerated
git grep -n 'professional-workflow/profiles/' d672914… -- professional-workflow/  # none
```
