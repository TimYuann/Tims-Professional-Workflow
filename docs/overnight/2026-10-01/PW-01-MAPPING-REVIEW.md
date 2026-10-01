# PW-01 · independent mapping check + cold read

State: **independent check report** produced by `tpw-night-check` for `PW-01-DISPATCH.md` §C, after
§A/§B delivered. Reviewer identity: Pi session `01a0f66d-0b7b-7701-8c51-8d262cb2f8d4`, provider
`commandcode`, model `deepseek/deepseek-v4.1-flash`, thinking `max`. This reviewer authored none of
the §A/§B outputs. No self-PASS beyond that statement; nothing here accepts M6 or the package —
Oracle owns acceptance.

Objects reviewed:

| Object | Role in this check |
| --- | --- |
| `adoption-examples/ucbip.md` | the optional adoption mapping under review |
| `docs/overnight/2026-10-01/PW-01-UCBIP-READBACK.md` | the §A raw readback the mapping must stay faithful to |
| `professional-workflow/` (19 tracked files) | core package for the no-dependency check |
| `docs/overnight/2026-10-01/PW-01-DISPATCH.md` | fixed refs + §C scope; cold-read input |
| `/Users/yuantian/Developer/ekunai/Unified-Customs-Bonded-Intelligence-Platform` | read-only spot-check target |

Method: read-only. UCBIP commands were `git cat-file/ls-tree/show/grep/status/rev-parse`, `sed`,
`shasum`; the ignored binding source was re-read for digest/columns/role names only (bearer values
not printed). No UCBIP write, no service, no test, no network, no `render_current_state.py --check`
execution, no package qualification re-run, no tracked-file write other than this file, no commit.

## Check 1 · mapping fidelity and cited-object location — PASS with 2 defects

The period is pinned and still current: UCBIP HEAD at re-read is the same commit
`7fc94e4a483cf6b1d8add214d7dbe9a1d42b7f76` (`main`, 2026-10-01 14:06:23 +08:00, tracked tree clean;
the two untracked root HTML exports are present and were not opened). No drift between dispatch,
readback and this re-read.

Spot-checked citations (sample level, at `7fc94e4a`):

| Mapping claim | Evidence | Result |
| --- | --- | --- |
| `docs/active/current-release.md` `## Now`, `current-entry` region (10–35) | line 6 `## Now`; markers at 10/35 | exact |
| Readback: three generated regions, two files | current-release has 1 (`current-entry`); restart card has `role-binding` (19–31) and `dag-table` (78–102) | exact |
| `role-binding.tsv` ignored, Driver-owned, 4 cols, pointer + as-of | 10 lines, 4 cols, 9 roles, `sha256 83572fd4…dc644b` = current-release:19 and `.gitignore:191` `/.agent-local/` | exact |
| Integrator = `writer` in the binding source | `writer` is present in the role column | exact |
| `CARD-STATE` per-card state block | `docs/tasks/2026-09-30-l5-live-sse.md` markers at 4/13 | exact |
| `docs/receipts/2026/*.md` count | 129 tracked files | exact |
| Ledger header/classes/rows | header line 23, `Classes:` line 13, 186 data rows (precise row count) | exact |
| `engineering-method-routing.md` quotes | line 11 `方法**不产生权限**`; `tim-professional-workflow` at 12/13/35/50 | substantively exact (quote has inline bold, not byte-identical) |
| `72ac591` not on main / no branch contains it / added `docs/decision-ledger.md` | `cat-file` commit exists; no branch contains it; tree contains `docs/decision-ledger.md`; ledger row `L6-GOVERNANCE-0929/drift-audit` (line 283) records the same finding | exact |
| `docs/TODO.md` rule that this package's repo is another project | line 706 `属**他人项目**，本仓不得改` | exact |

Defects found in `adoption-examples/ucbip.md` (not patched by this reviewer; §C recall applies):

1. **Line 60 — non-resolving object name.** The Charter block writes `Oracle disposition
   PW-01-DISPOSITION.md`. The actual object is
   `docs/overnight/2026-10-01/PRO-AUDIT-1-DISPOSITION.md` (SHA-256 `afc63730…0712f`, verified in
   this repo and matching the dispatch). The hash pins the identity, but the cited name alone does
   not resolve.
2. **Line 32 — generated-region count/location.** The row reads `docs/active/current-release.md`
   `` `## Now` `` and "the two generated regions". Spot-check shows **three** generated regions
   across two files: `current-entry` in current-release; `role-binding` and `dag-table` in the
   restart card. Under either reading the cell is wrong: current-release holds one generated region,
   and the "two" (if meant as role-binding/dag-table) are not in current-release. The readback
   (line 32) states the correct three-region/two-file split, so the mapping deviates from its own
   source.

Limits (verified only at the stated level):

- Line 35 `Product behavior → docs/active/stable-v1-product-contract.md`: the path exists and the
  file self-declares target-behavior authority, but the readback never named this object; the row is
  an addition verified at path-existence level only (semantic attribution not sampled further).
- Line 21's read-basis summary omits "no network" from the readback's not-done list. Not a false
  claim ("documentation-only"), but not a complete restatement.
- Readback residual limits stand: receipt bodies, ledger bodies, `docs/TODO.md` and most of
  `current-release.md` were sampled, not read through. This check did the same.

## Check 2 · positioning — PASS

- **Optional / non-normative / outside core.** The file lives at `adoption-examples/ucbip.md`,
  outside `professional-workflow/`; its header says preparation-only, non-normative, no role/window/
  permission/acceptance granted. The package README (lines 27–29) states the same and that the
  example does not affect assembly or package state.
- **No invented binding or authorization.** "Delegation source … Records existing authorization;
  adds none"; "Not an authorization, role binding or write window"; the future-embodiment block is
  explicitly `not authorized` with four mandatory activation conditions. The one role fact it cites
  (`writer`) was spot-checked and exists in the binding source.
- **No competing state/evidence system.** The mapping declares itself "not a status source", keeps
  UCBIP's control record / `## Now` / ledger as the only ones, and cites `72ac591` as the
  counter-example; the readback likewise declares it is not a ledger or roster. The `72ac591` /
  `L6-GOVERNANCE-0929/drift-audit` facts check out.
- Observation (not a defect): the Driver row points at the restart card's 「当前控制权」, while
  readback family 4 treats `role-binding.tsv` as the binding source and the card as its projection.
  `current-release.md:11` itself equates the control record with that card section, so the pointer is
  correct; only the source-vs-projection layering is slightly compressed in the cell.

## Check 3 · core starts without the optional note — PASS

- **Single reference.** Inside `professional-workflow/`, the only occurrence of
  `ucbip`/`adoption` is the README pointer section (lines 27–29). No other package file references
  the note; the package contains no executable or script that could load it.
- **Documented assembly still yields ordered startup text.** Running the README §Use step 4 form
  (`cat profiles/implementation.md charters/examples/implementation-local-fix.md
  methods/local-defect-feedback-loop.md`, task-input placeholder omitted because none exists)
  produced 99 lines in the fixed order Profile → Charter → method, with no mention of the optional
  note. All three fixed objects exist and are non-empty.
- **Core file set is still 19 files.** `git ls-files professional-workflow | wc -l` = 19;
  `62e3792..HEAD` shows only `M professional-workflow/README.md` and
  `professional-workflow/authority/README.md` (the §B appends), no add/delete; the package working
  tree is clean. The pre-revision path list and the current path list are identical.
- Limit: the assembly run omitted the task-input object (placeholder), so this verifies ordering and
  fixed objects, not an end-to-end filled-Charter startup. No runtime exists in the package beyond
  the documented read/cat assembly.

## Check 4 · cold read observation — PASS (bounded observation, not re-qualification)

Inputs: `PW-01-DISPATCH.md` (especially §C) + `professional-workflow/README.md`, with at most one
additional hop per pointer.

- Profile: locatable in 1 hop to `profiles/README.md` (selection table); §C itself fixes this task's
  Profile as not activated.
- Methods: locatable in 1 hop to `methods/README.md`; §C fixes this task's methods as none bound.
- Objects: README §Use names the assembly objects (Profile, Charter, bound method files, task input)
  and §C fixes this task's write set.
- Constraints: §C Preserve/do-not-do plus README §Package state and the "Nothing in this directory
  alone grants…" line are sufficient.
- Return points: from §C alone (Deleverable file, Recall → Driver, Acceptance → Oracle). The package
  README defines no deliver/return semantics of its own — expected for a generic package, but worth
  knowing: return points are dispatch-local, not package-local.

Observed ambiguities (non-blocking, recorded as asked):

1. README title reads "M5 integration candidate" while the active process is PW-01 under M6; the
   package-state paragraph ends by saying M5/M6 remain in progress. A cold reader must read the
   paragraph's end to avoid a stale revision label.
2. README §Use uses the literal placeholder `path/to/current-task-input.md`; clearly illustrative
   but an unmarked reader could try to resolve it.
3. The M1-era "待 M4" labels remain in frozen Profiles; only `methods/README.md` corrects their
   binding status — one extra hop for a cold reader (already signposted by the README).
4. The optional-note pointer sits after §Package state; a fast reader could take it as part of the
   assembly, though heading and text mark it non-normative.

## Unresolved items (for the Driver / §C recall)

1. Two fidelity defects in `adoption-examples/ucbip.md` (**line 60** disposition object name;
   **line 32** generated-region count/location) remain in place by design of this write set. §C
   recall: report the affected object and fact to the Driver; do not silently patch. The mapping's
   substance is otherwise faithful and the note's non-binding status is unaffected.
2. Product-behavior owner row (line 35) verified only at path existence.
3. Readback's "no network" clause is not restated in the example's read-basis summary.
4. No UCBIP-side owner has reviewed the readback (unchanged from §A); a downstream mismatch stops
   the affected item and returns to the Driver.
5. Not done here: renderer `--check`, package re-qualification, M3 case reruns, acceptance of any
   object, M6 closure, commits. Oracle owns acceptance; this check accepts nothing.

## Post-fix re-verify (2026-10-01, tpw-night-check)

Bounded re-verify of exactly the three author fixes in `adoption-examples/ucbip.md`, requested after
the original check. Scope was limited to those three locations; nothing else in the file or package
was re-inspected. Read-only; same reviewer identity and method as above; no commit.

| # | Fixed location | Observed after fix | Against | Result |
| --- | --- | --- | --- | --- |
| 1 | Read-basis sentence (lines 21–22) | now reads “no UCBIP write, service, test run, **network**, product data or credential access, and the downstream state checker was not executed” | readback “Not done: … **no network** …”; dispatch §A read scope | **PASS — closed** (matches the omitted clause verbatim in substance) |
| 2 | Entry / generated projection row (line 32) | now reads “three generated regions across two files — `current-entry` in `docs/active/current-release.md` `## Now`, and `role-binding` + `dag-table` in `docs/tasks/2026-09-19-multi-agent-restart.md`; refreshed by `scripts/render_current_state.py`, never hand-edited” | readback family 5 (three regions, two files); re-sampled at `7fc94e4a`: current-release has 1 `BEGIN GENERATED` (`current-entry`, line 10, inside `## Now`), restart card has 2 (`role-binding` line 19, `dag-table` line 78) | **PASS — closed** (count, names and both locations exact) |
| 3 | Delegation source (lines 60–62) | now reads “Oracle disposition `docs/overnight/2026-10-01/PRO-AUDIT-1-DISPOSITION.md` (SHA-256 `afc63730…0712f`)”, full path on one line | this repo: the file exists at that path and its `shasum -a 256` is exactly `afc63730d8f886230dc4e6b43056a2425b1536d2e6a4632d4081437ad005712f` | **PASS — closed** (name resolves; digest unchanged) |

Effect on the original report: the two Check 1 defects and the one fidelity-omission limit are closed
at their cited locations. The other Check 1 limits (product-behavior row verified at path level
only; sampled-not-read bounds) and all §C unresolved items other than these three are unchanged and
were intentionally not re-checked. This re-verify adds no new acceptance claim; Oracle still owns
acceptance.

## Differential re-check · R1/R2 (2026-10-01, tpw-night-check)

Bounded differential re-check of exactly the four working-tree modifications requested after Pro 2
(`PRO-AUDIT-2-DISPOSITION.md`, R1/R2). No whole-package re-qualification, no M3 rerun, no renderer
`--check`, no commit. At check time all four were uncommitted changes against `05f4bbb`; the SHA-256
values below are the exact bytes this verdict covers (the three earlier fixes remain intact at
`adoption-examples/ucbip.md` lines 21 / 37 / 66).

Fixed-object identity:

| File | SHA-256 (working tree) | Diff vs `05f4bbb` |
| --- | --- | --- |
| `adoption-examples/ucbip.md` | `37335d1c7245e30a10d7c74b8c33a0a74b5c4f7fd3d1c64e7e65f93894a62fce` | 28+/13−, confined to the four authorized zones (R1 Acceptance, R2 retrieval boundary, R2 sanitized/retrieval paragraph, state/projection clarification) |
| `docs/overnight/2026-10-01/PW-01-DISPATCH.md` | `37aa265903aec355dc3cb83ad52affc021f74d437767a8e30ab7adc9f1212654` | 11+/0− append-only (Errata · R1) |
| `docs/overnight/2026-10-01/PW-01-UCBIP-READBACK.md` | `83a54d0b2cf0f713ad12b74c2d22a426808d4da2bcbc586bbb65674488735ce5` | 10+/0− append-only (Errata · R2) |
| `docs/overnight/2026-10-01/M6-PACKAGE-CANDIDATE-05f4bbb.md` | `9845bfbe896c73b0d0a90489afb263f8a6a7d7916766523a18eff7e483e6eb06` | 4+/0− append-only (manifest correction) |

Per-item verdicts:

| # | Check | Evidence | Result |
| --- | --- | --- | --- |
| R1-a | The optional note no longer assigns downstream acceptance/authorization to TIM Oracle or this run | Acceptance field now reads exactly the disposition's R1 text: TIM Oracle accepts only the TIM-side adaptation-preparation artifact and the local-adoption delivery; UCBIP adoption, task acceptance, action authorization and closure stay with the effective downstream delegation; no downstream acceptance occurred in this run. Grep shows no residual “Oracle owns package/downstream acceptance” in the note (remaining `Oracle` mentions are the delegation source and the recorded acceptance-file hash) | **PASS** |
| R1-b | Historical dispatch corrected by errata, not rewritten | Append-only +11/−0; the errata quotes the original §A sentence, substitutes the TIM-only acceptance scope, names the downstream owner, states no downstream acceptance, and explicitly says it does not rewrite the dispatch as if the original had been correct | **PASS** |
| R2-a | Ignored binding/runtime raw no longer promised as commit-retrievable; future re-read required | New “Retrieval boundary (R2)” bullet, amended ownership row, and rewritten “Sanitized result and retrievable raw index (R2)” paragraph split tracked documents/projections (retrievable at `7fc94e4a…`) from the ignored binding source and other runtime raw (local point-in-time observation; path/digest/`as-of` kept, recovery **not** promised; future adoption must re-read the then-effective binding); still declares no copy, no archive, no second ledger | **PASS** |
| R2-b | Readback check-3 blanket claim narrowed, original assertions preserved | Append-only +10/−0; Errata · R2 quotes check 3's “every path in the table above is in `git ls-files` at HEAD”, limits it to tracked document/source paths, excludes the ignored runtime source, keeps check 2's byte match as a local observation, and states the correction creates no archive, ledger row or tracked copy | **PASS** |
| H | Historical files not rewritten | `git diff --numstat` gives pure appends for the three errata files (4/0, 11/0, 10/0); each correction header says the original text is preserved unchanged; the note's body diff touches only the four authorized zones | **PASS** |
| S | Status source vs generated projection distinguished correctly | New bullet: hand-written state sources are each card's `CARD-STATE` and the Driver-owned binding source; generated entry/projections (`current-entry` in current-release; `role-binding` + `dag-table` in the restart card) hold no state of their own and are refreshed by `scripts/render_current_state.py`. Matches readback families 3/4/5 and current-release:61 (“one hand-written place, three generated regions”) | **PASS** |
| N | No new archive or ledger | `git status --short` shows only the four modified files plus pre-existing untracked `scan.js`; `adoption-examples/` still contains only `ucbip.md`; both errata and the note disclaim archive/ledger creation | **PASS** |
| M | M6 manifest correction accurate | Original sentence at line 63 preserved; correction appended at line 74; the quoted stale claim exists verbatim; the fixture README did receive exactly +4/−0 lines in `e9c0c99` and sits outside `professional-workflow/`, so the core 19-file manifest and the package-only archive (`git archive … professional-workflow`, lines 11–12) are unaffected | **PASS** |

Reference spot-checks supporting R2: `role-binding.tsv` digest is still `83572fd4…dc644b`, matching readback check 2's recorded value — cited here only as the local observation the note now describes, not as commit retrievability. `PRO-AUDIT-2-DISPOSITION.md` exists (the errata's reference resolves).

Limits:

- `PW-01-DISPATCH.md` line 26 still carries the original mis-attribution by design; a reader who stops at §A without the appended errata still sees the superseded sentence.
- The M6 candidate's optional/outside digest table remains pinned to `05f4bbb`, so it is stale for the current working tree — including this review file — until the Driver records the corrected identity at commit time (disposition §31 assigns that to the Driver's final report).
- Differential scope only: no whole-package or M3 re-check, renderer `--check` not executed, no acceptance given. Oracle owns acceptance.
