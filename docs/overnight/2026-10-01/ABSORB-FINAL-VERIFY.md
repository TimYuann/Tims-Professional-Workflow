# Absorb candidate · final short verification (references/state + manifest)

State: **short final check** by `tpw-night-check` (Pi session `01a0f66d-0b7b-7701-8c51-8d262cb2f8d4`, `commandcode/deepseek/deepseek-v4.1-flash` / max), 2026-10-01. Bounded: only the affected references/state and the whole-package manifest identity; no full audit reopened, no service/network, no other file changed, no commit.

Fixed pin: `a41f6962f8fe061c8ef8cc4466bb43180db5d35c` (night HEAD; working tree clean except untracked `scan.js`). Package subtree at the pin: `e5e5338ed8abc717bdda48e0f4ae751dea30dbb1` (also at `31929b3`). Package-changing commits after the base `eb7930b`: `bc1c3fc` (Rev.2), `dca01b4` (Rev.3), `08d9907` (Rev.4), `1184fcc`, `8a7db4a`, `31929b3` (Rev.5).

## 1 · Short references/state check

| # | Item | Evidence at the pin | Result |
| --- | --- | --- | --- |
| S1 | Two Charter examples keep only the M4 historical source and point current bytes to `methods/README.md` §Status + the night manifest; no stale current digest | `implementation-local-fix.md` L13 and `technical-planning-cross-module.md` L13 both: “Accepted M4 source: commit `013659331c8c5f9f54b866b393972a03d7938773`, SHA-256 `3ca23a74…` / `30066c8b…`; current package bytes are recorded in `methods/README.md` §Status and source trace and the night candidate manifest — a real task rebinds the current fixed object rather than copying a digest here.” No M5/current digest value is copied in the examples. (`technical-planning-cross-module.md` L3 still says “illustrative M5 binding” as a historical state label, not a digest.) | **PASS** |
| S2 | Six Profiles + `profiles/README.md` binding lines point to `methods/README.md` | Each of `behavior-domain`, `driver`, `evidence-evaluation`, `implementation`, `intent-voice`, `technical-planning`, `profiles/README.md` contains exactly one `methods/README` pointer. | **PASS** |
| S3 | Package README Package state compressed to historical source pointers + current candidate/manifest | `professional-workflow/README.md` L23: M1 checkpoint and M4 commit/tree as historical sources; “M1–M5 labels … are not current acceptance”; then the current status: accepted PW-01/M6 delivery (`M6-FINAL-ACCEPTANCE.md`) plus the 2026-10-01 corrected candidate recorded in `ABSORB-CORRECTED-CORE-MANIFEST.md`, awaiting the directed recheck. | **PASS** |
| S4 | `docs/WORKFLOW-INTENT.md` §10 registry-retired marker | §10 (L282) contains: “本文件当前迭代不改 registry（该对象已于 **2026-10-01** 从默认根退役，此处为历史迭代记录）…” and the earlier 2026-10-01 switch note at L16. | **PASS** |
| S5 | `guide-mock-adapter-choice.md` Rule 3 / example limited to the paths the test actually invokes, referencing `behavior-claim-evaluation` §Use | Rule 3 (L13): “A double exercises only what the test actually calls… the replaced adapter’s request construction, transport and response mapping are not executed”, marked as “applying `behavior-claim-evaluation.md` §Use to adapter seams”; example L25: “with the mapping path actually invoked”. Real-Provider/SDK/wire claims are left to an appropriate real leg under existing authorization. | **PASS** |
| S6 | `guide-redacted-evidence.md` Rule 2 allows collection or reuse inside valid authorization | Rule 2 (L12): “Within the task’s valid delegation you may either collect new observations or reuse existing records; keep only the minimum signal-bearing evidence, and redact before you show, record, share or store it… requires no re-asking each time, and it does not authorize capture outside the valid authorization.” Rule 4 remains the separate raw boundary. | **PASS** |

## 2 · Whole-package manifest check

| # | Item | Observed | Result |
| --- | --- | --- | --- |
| M1 | 21-file path set at the pin | exactly the 21 documented paths (same set as the manifest) | **PASS** |
| M2 | Core subtree | `a41f696:professional-workflow` = `e5e5338ed8abc717bdda48e0f4ae751dea30dbb1` = the Rev.5 subtree (identical at `31929b3`) | **PASS** |
| M3 | Archive | `git archive --format=tar 31929b34f4eada9e7a3653b1804f409785d9b7c7 professional-workflow` = `a45e8cba3be1f3f23de144dddbaccd87a356854017a5837f970e8018362d469f` — matches Rev.5. For the pinned commit itself: `git archive --format=tar a41f6962f8fe061c8ef8cc4466bb43180db5d35c professional-workflow` = `be49dd45b834a68f89a8ab8d04234861000b135df22671c552aec54474d7d92e` (commit-specific tar metadata; package bytes identical) | **PASS** (Rev.5 pairing), pinned-commit digest recorded here for completeness |
| M4 | Backbone bytes | `authority/RESPONSIBILITY-BACKBONE.md` = `ce82a70016a4a3fc234ea287f39aac8d79a260ddf13747c4fb705bda580453ba` | **PASS** |
| M5 | 21-file digest table vs actual bytes | **9/21 match the last-recorded value; 12/21 differ.** The base table (and Rev.2–4 deltas) does not record the final digests of the files changed by `1184fcc`, `8a7db4a` and `31929b3` | **LIMIT** — see below |

M5 mismatch list (recorded ≠ actual at the pin; recorded = base or latest revision override):

```
README.md                            ee5a284328b8 -> 0d80d3c2b0d3
charters/examples/implementation-local-fix.md      038e6a31d699 -> b0dff7041e7e
charters/examples/technical-planning-cross-module.md 62050af72fdf -> 8d1168ae783e
methods/behavior-claim-evaluation.md 0531835f77a8 -> 25086584eb4a
methods/guide-mock-adapter-choice.md 5ad055b39a7a -> 3e047e1f5ef5
profiles/README.md                   e2a37dbaecd3 -> 047a76dc6245
profiles/behavior-domain.md          d8b75a5734c0 -> 43b02f332286
profiles/driver.md                   8a2f42c874ca -> 0703cf617940
profiles/evidence-evaluation.md      d72b3a5097f1 -> 76cd77f888bb
profiles/implementation.md           c96162668a1b -> 5c4186d4efa8
profiles/intent-voice.md             0f3206ae22fa -> f54e283e8a83
profiles/technical-planning.md       d53da06edc99 -> 15c751670b24
```

Cause: the manifest is base + revision notes; Rev.2/3/4 record their changed-file digests, but the audit-disposition commits `1184fcc` (profiles, README, charter examples, `behavior-claim-evaluation`, `guide-mock`), `8a7db4a` (`guide-mock`) and `31929b3` (README, charter examples) are covered only by the new subtree/archive, not by a file-digest list. The base 21-file table therefore describes `eb7930b`, not the pin.

## 3 · Conclusion and residuals

- **Short references/state check: PASS** on all six items; the affected pointers/state now resolve as intended, with no stale current digest duplicated in the Charter examples and no new authority/gate introduced.
- **Manifest: subtree, archive (Rev.5 pairing) and Backbone PASS**; the 21-file path set is intact. **Limit:** the manifest's per-file digest table is not current for the pin — 12/21 files differ from their last-recorded values, because the last three package-changing commits were recorded only as a new subtree/archive. If a reader needs per-file verification at the pin, the `e5e5338e…` subtree (or the `be49dd45…` archive of the pin) is the binding identity; the file table should be refreshed or explicitly labelled as the `eb7930b` snapshot.
- Archive digests stay commit-specific (`31929b3` → `a45e8cba…` per Rev.5; `a41f696` → `be49dd45…`; identical package bytes). No re-archive or semantic change is needed for this note.
- No other file was changed and nothing was committed; this report is the only write.

- **Final identity re-check (2026-10-02): PASS** — tip `bb58b003ae6fe71005f9e7ef0a3f27ac52ca9a5b`; product-bytes `9085d758848de8836a3e6e6083962480b1af42ca` (root tree `27bbdfb85299d751fe0bc48e09c1dc8b545f5dcf`, subtree `7c814e54c5e775045bc1c5155e3c181ceb1345fb` at both tip and product commit, 21 files with Rev.7 digests 21/21 match); archive@9085d758 `63ac073fcdb976cb5a11bc2556036a914e82b62a7e8447e467ff8d18491d260e`; Backbone `ce82a700…` unchanged; status sync labels confirmed (both guides title/Status = accepted bounded reference (2026-10-02); package README = accepted as a bounded usable reference; `methods/README.md` and root `README.md` → `docs/overnight/2026-10-01/ABSORB-FINAL-ACCEPTANCE.md`); Pro/Oracle records present (`ABSORB-PRO-RECHECK-{RECORD.tsv,REQUEST.txt,RESPONSE.json,RESPONSE.txt}`, `ABSORB-FINAL-ACCEPTANCE.md`, appended entries in `ORACLE-ACCEPTANCE.md` L55 and `PRO-AUDIT-ALLOWANCE.md` L43); diff vs the reviewed identity `e5e5338e` is exactly 4 package files (`README.md`, `methods/README.md`, `guide-mock-adapter-choice.md`, `guide-redacted-evidence.md`) and all changes are status text/pointers; `scan.js` unchanged (`c033c967…`).
