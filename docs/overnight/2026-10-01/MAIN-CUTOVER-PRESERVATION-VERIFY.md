# Main cutover C0 · independent preservation verification

State: **independent check report** for the C0 done conditions in
`docs/overnight/2026-10-01/MAIN-CUTOVER-PLAN.md` §4, produced 2026-10-01T19:10+08 by
`tpw-night-check` — Pi session `01a0f66d-0b7b-7701-8c51-8d262cb2f8d4`, provider `commandcode`,
model `deepseek/deepseek-v4.1-flash`, thinking `max`. Read-only apart from this file; no commit, no
mutation of root, legacy worktree or custody capsule.

Objects and fixed identities:

| Object | Path / ref | Identity at check |
| --- | --- | --- |
| Old root checkout | `/Users/yuantian/Developer/tim-professional-workflow` | `main` @ `496b0676e302e2d0eafba129ff61de4c203d258a`; `origin/main` unchanged @ `448c3d67c23994c86f5b0e344b82488823624586`; still dirty (capture state) |
| Legacy worktree | `.worktrees/legacy-pre-night-2026-10-01` | branch `legacy/pre-night-2026-10-01` @ `496b0676e302e2d0eafba129ff61de4c203d258a`; registered linked worktree |
| Custody capsule | `.worktrees/preservation/tpw-main-cutover-20261001-c0/` | `refs.txt` ROOT_HEAD `496b067…`, MAIN `496b067…`, NIGHT `2e7ee4d…`, ORIGIN_MAIN `448c3d67…` |
| Capsule key digests | `staged.patch` `8eb56e9e…`; `unstaged.patch` `b6506ea2…`; `status.NUL` `2f950981…` | `shasum -a 256 -c custody.sha256` → all three OK |
| Capsule inventories | `index.ls.NUL` 337 entries; `files.sha256` / `files.stat` 32 dirty paths; `untracked.NUL` 21 paths; `upstreams.sha256` 1344 files | self-records, cross-checked against live trees below |

## Checks

| # | Check | Result |
| --- | --- | --- |
| 1 | legacy HEAD == 496b067 == capsule ROOT_HEAD | **PASS** |
| 2 | legacy status set == custody `status.NUL` (8 staged / 3 unstaged / 21 untracked) | **PASS** |
| 3 | staged binary diff SHA-256 == `8eb56e9e…`; 8 index entries and worktree blobs == captured root index | **PASS** |
| 4 | unstaged binary diff SHA-256 == `b6506ea2…` | **PASS** |
| 5 | 21 untracked files byte-identical to `custody/untracked/**` | **PASS** |
| 6 | ignored `upstreams` copy: 1344-file sha256 manifest identical | **PASS** (format note below) |
| 7 | root drift since capture | **PASS — none observed** |

### 1 · identity

Root HEAD, root `main` ref, legacy HEAD, legacy branch ref and capsule `refs.txt` ROOT_HEAD are all
exactly `496b0676e302e2d0eafba129ff61de4c203d258a`; legacy HEAD's abbrev ref is
`legacy/pre-night-2026-10-01`; `git worktree list --porcelain` registers the legacy path on
`refs/heads/legacy/pre-night-2026-10-01`.

### 2 · status set

`git -C legacy status --porcelain=v1 -z` is **byte-identical** to `custody/status.NUL` (32 entries):
6 × `A `, 2 × `M ` (staged = 8), 3 × ` M` (unstaged = 3), 21 × `??`. The eight staged paths are
`docs/history/derivation-0930/{DERIVATION,SYNTHESIS,UPSTREAM-RESCAN}.md`,
`docs/history/handoff/{0930-derive-TASK,0930-upscan-TASK}.md` (staged modifications) and
`docs/history/handoff/{0930-herdr-pitfalls-TASK,0930-synth-TASK,HERDR-PI-PITFALLS}.md` (staged adds).

### 3 · staged state

`git -C legacy diff --cached --binary` = custody `staged.patch`, SHA-256
`8eb56e9edf6603e468ec59187990bbeae8a25891cc02532bbcfb5db00b504a91`, byte-equal. For all 8 staged
paths the legacy index entries (mode, blob SHA, stage) equal the captured root index entries in
`index.ls.NUL`, and `git hash-object` of each worktree file equals its index blob (8/8). Mode/size for
these (and all 32 dirty paths) also match `files.stat`.

### 4 · unstaged state

`git -C legacy diff --binary` = custody `unstaged.patch`, SHA-256
`b6506ea2df3f484f3450a42451cdc8d9aac776d1e649f6e63fa3e433a218a3a4`, byte-equal (worktree-vs-index
distinction preserved; the three ` M` paths are `.decisions/ledger.tsv` and
`docs/history/derivation-0930/{ADVERSARY-VERDICT-BATCH1-REREAD,DISPOSAL-BATCH1-REREAD}.md`).

### 5 · untracked state

All 21 paths in `untracked.NUL` exist in the legacy worktree and in `custody/untracked/`; per-file
SHA-256 matches 21/21, and mode/size match `files.stat`.

### 6 · ignored upstreams

Legacy `.worktrees/legacy-pre-night-2026-10-01/upstreams/` has 1344 regular files; the path→SHA-256
mapping is exactly equal to `custody/upstreams.sha256` (and to the identical `upstreams.legacy.sha256`),
0 missing paths, 0 hash mismatches. The root checkout's own `upstreams/` still holds the same 1344
files and matches the same manifest. **Format note:** a naive line-by-line `cmp` differs because the
custody manifest was sorted with the macOS default locale while this check re-sorted with
`LC_ALL=C`; the mapping comparison above is the correct equivalence and is exact.

### 7 · root drift

Root `status --porcelain=v1 -z` is byte-identical to the captured `status.NUL`; all 32 captured dirty
paths match `files.sha256` (SHA-256) and `files.stat` (mode/size) in the root checkout 32/32; root
HEAD is still `496b067…` and `origin/main` is still `448c3d67…`. No drift observed within the captured
scope (tracked dirty set + untracked + ignored upstreams).

## Limits

- The `upstreams.sha256` inventory is regular-file SHA-256 only. The legacy copy also contains 2
  symlinks (`addyosmani-agent-skills/.opencode/skills → ../skills/`;
  `mattpocock-skills/AGENTS.md → CLAUDE.md`) whose link metadata is not in the manifest; their target
  regular files are covered individually where applicable. No mode/uid/gid manifest exists for the
  upstreams tree.
- Drift check (7) can only cover the captured inventory: new files under ignored/untracked-ignored
  areas outside the 32-path + upstreams records would not be visible to these artifacts.
- `custody.sha256` self-hashes only `staged.patch`, `unstaged.patch`, `status.NUL`; the other capsule
  records are cross-checked against the live legacy/root trees in this report rather than by a
  capsule-internal hash.
- The capsule README records that `.pi/` runtime and OS junk were deliberately not copied; that is a
  documented exclusion, not a preservation failure.
- Point-in-time check: no further mutation occurred after these reads (this report is the only write).

## Verdict

C0 done conditions for items 1–7 are verified **PASS** at the exact identities above, with the limits
listed. The old root现场 is intact at capture state and recoverable from the verified legacy worktree
plus the custody capsule (reconstitution recipe in the capsule README); no root drift since capture was
observed. This report covers C0 preservation only — it does not perform or accept C1/C2, does not
touch `professional-workflow/`, UCBIP, M3, remotes, tags or releases, and is not a package acceptance.

## C1 entry check (2026-10-01, tpw-night-check)

Independent, read-only check of C1 commit `5ba5fa54e96b3a0f53fb62e3d585b8bffb48567f`
("chore(root): promote new default entry and retire legacy active surfaces", parent `2e7ee4d`). Night
HEAD at check time is `a046e48` (adds only this report). No C0 re-run, no other file changed, no
commit. Reference base: the accepted core tree `11e6e377` (the `professional-workflow` subtree of the
accepted delivery — a tree object, not a commit; the comparison below is tree-vs-tree:
`git diff 11e6e377 5ba5fa5:professional-workflow`).

| # | Check | Evidence | Result |
| --- | --- | --- | --- |
| 1 | Package diff vs accepted tree `11e6e377` | **`README.md` only, 2 insertions / 2 deletions**: title line → `Professional Workflow · accepted local-adoption delivery (2026-10-01)`; the Package-state final sentence → the PW-01/M6 accepted-status sentence (records `M6-FINAL-ACCEPTANCE.md` + `PW-01-FINAL-REPORT.md`). No other package path changed; no method/Profile/Charter/Backbone byte touched; package working tree clean (0 porcelain entries) | **PASS** |
| 2 | Retained set present; retired set absent at tip (listed 16 paths) | Retired 16: `roles`, `skills`, `principles`, `workflow`, `scripts`, `VERSION`, `.decisions`, `docs/artifacts.md`, `docs/coldstart.md`, `docs/ledger.md`, `docs/downstream-mapping.md`, `docs/closure-report.md`, `docs/archive`, `docs/history`, `sources`, `upstreams.lock.yaml` — each **ABSENT** at `5ba5fa5` and in the working tree, each **PRESENT** in `.worktrees/legacy-pre-night-2026-10-01`. Retained at tip: top-level `.gitignore, AGENTS.md, README.md, professional-workflow/, adoption-examples/, docs/` with `docs/{WORKFLOW-INTENT.md, RESPONSIBILITY-BACKBONE.md, OVERNIGHT-WORKFLOW-PLAN-2026-10-01.md, overnight/}`; C1 commit has **0 added paths**, so no new entry/archive directory was smuggled in | **PASS** |
| 3 | Root AGENTS/README only lead by reference to one current entry; no old registry/render/check chase; legacy pointer resolves | `AGENTS.md` names `README.md` as the entry and the package dirs as the assembly owners; `README.md` short path is `WORKFLOW-INTENT` + `RESPONSIBILITY-BACKBONE` → `professional-workflow/{profiles,charters,methods}` → `professional-workflow/README.md` assembly order. `AGENTS.md` explicitly marks `workflow/registry.yaml`, `scripts/render.py`, `docs/artifacts.md` etc. as retired, “不要求、不查找、不运行”. Legacy pointer `.worktrees/legacy-pre-night-2026-10-01` + branch `legacy/pre-night-2026-10-01` exists on disk at `496b0676e302e2d0eafba129ff61de4c203d258a` | **PASS**, one dangling forward ref (below) |
| 4 | `.gitignore` contains `.worktrees/` | Added at line 10 with its comment (`# 本地 worktree 与保全/验证目录；fresh clone 不需要`), +2 lines total | **PASS** |
| 5 | Backbone source and package export both `ce82a700…` | `docs/RESPONSIBILITY-BACKBONE.md` and `professional-workflow/authority/RESPONSIBILITY-BACKBONE.md` both hash `ce82a70016a4a3fc234ea287f39aac8d79a260ddf13747c4fb705bda580453ba` at tip and in the working tree | **PASS** |

Limits and ambiguities recorded:

- **Dangling forward reference (only unresolved pointer).** Root `README.md` “已接受身份与状态” lists
  `docs/overnight/2026-10-01/MAIN-CUTOVER-REPORT.md` as “本次主线切换与新旧对象”, but that file is
  **absent** at `5ba5fa5` and in the working tree; per `MAIN-CUTOVER-PLAN.md` §C3 it is a Driver
  handoff deliverable still to come. Until then the entry chain itself resolves, but this one status
  pointer 404s. Expected to close at C3; recorded, not patched.
- **Check level is commit/tip, not the physical root.** The C1 files live on the night branch; the root
  checkout is still old `main@496b067` with the old entry until the C2 promotion. C0 verified root is
  unchanged since capture, so this is a staging fact, not drift.
- **Retired set is directory-level for six entries** (`roles`, `principles`, `scripts`, `skills`,
  `docs/archive`, `docs/history`); file-level completeness rests on the C1 diff itself (233 `docs`
  deletions + the other groups), with the bytes C0-verified in the legacy worktree.
- `upstreams/` (the legacy-section token) is the ignored raw-asset copy, present on disk in the legacy
  worktree and root but intentionally not in the tip tree; `upstreams.lock.yaml` moved to legacy.
- Remote state untouched: `origin/main` remains `448c3d67c23994c86f5b0e344b82488823624586`.
- Scope note: C1 entry check only — no C2 promotion, no C3 cold read, no package semantic acceptance,
  no M3/UCBIP action.

## C3 cold read + C2 spot check (2026-10-01, tpw-night-check)

Read-only. Cold read used only the promoted root `AGENTS.md` + `README.md` plus normal one-hop file
references; C2 spot check used `rev-parse`/`status`/`ls-tree`/`worktree list`/`ls-remote`/`ls` only.
No state-affecting command, no file write except this append, no commit.

### C2 spot check

| # | Check | Evidence at check time | Result |
| --- | --- | --- | --- |
| 1 | Root branch `main`, HEAD `81f1cef`, clean, expected top level | `main` @ `81f1ceff33699ca407b2644cd6c8b53673e40ee7`; porcelain 0 lines; top level `.gitignore AGENTS.md README.md adoption-examples docs professional-workflow` (the hidden `.gitignore` is the only entry beyond the five named; no retired surface) | **PASS** |
| 2 | Legacy preserved | legacy HEAD `496b0676e302e2d0eafba129ff61de4c203d258a`; staged `8eb56e9edf6603e468ec59187990bbeae8a25891cc02532bbcfb5db00b504a91`; unstaged `b6506ea2df3f484f3450a42451cdc8d9aac776d1e649f6e63fa3e433a218a3a4`; 8 staged / 3 unstaged / 21 untracked | **PASS** |
| 3 | `scan.js` retained | `.worktrees/night-2026-10-01/scan.js` exists (7816 bytes) | **PASS** |
| 4 | Worktree registration | list shows root `81f1cef [main]`, legacy `496b067 [legacy/pre-night-2026-10-01]`, night `81f1cef [night/2026-10-01-workflow]` (plus two pre-existing /private/tmp detached worktrees, untouched) | **PASS** |
| 5 | Remote unchanged | `origin/main` = `448c3d67c23994c86f5b0e344b82488823624586`; `origin/night/2026-10-01-workflow` = `cf107522f9b13a778fa381ba600b4ecfb95fdc7e`; local `main` is ahead 95 of `origin/main` (no push) | **PASS** |

### C3 cold read (root AGENTS.md + README.md, one-hop references)

| # | Question | Locatable answer and path used | Result |
| --- | --- | --- | --- |
| a | Current version and default entry | Root README: default `main` is the 2026-10-01 new Professional Workflow, Oracle-accepted bounded local-adoption delivery (record `docs/overnight/2026-10-01/M6-FINAL-ACCEPTANCE.md`); AGENTS names `README.md` as the entry | **PASS** (no version string; see limits) |
| b | Owner of intent / responsibility boundary / methods / delivery status | Intent `docs/WORKFLOW-INTENT.md`; boundary `docs/RESPONSIBILITY-BACKBONE.md` (editable source) + frozen package export `professional-workflow/authority/RESPONSIBILITY-BACKBONE.md`; methods `professional-workflow/methods/README.md` (bodies under `methods/`); delivery status `docs/overnight/2026-10-01/` with `M6-FINAL-ACCEPTANCE.md` as current acceptance. All from root README step 1/2/4 + AGENTS 当前唯一入口与归属 | **PASS** |
| c | How a task binds a Profile and a method | Root README step 2–3 → `professional-workflow/charters/README.md` (Charter binds one use of a Profile to the actual task; choosing a Profile is composition, not authorization; `template.md` is the binding form) → `professional-workflow/methods/README.md` (method used only when the Charter binds it; no applicability triggers added by the list) → assembly order in `professional-workflow/README.md` | **PASS** (2-hop) |
| d | What legacy is and where | Old registry/roles/skills/principles/scripts world, retired from the default root; complete working state at `.worktrees/legacy-pre-night-2026-10-01`, local branch `legacy/pre-night-2026-10-01`, old `main@496b067` | **PASS** |
| e | How to retrieve an old script | Read-only from the legacy worktree (root README 旧版归档入口 + AGENTS 窄而有效的检查: old registry/render/etc. “不要求、不查找、不运行; 只读历史在 .worktrees/legacy-pre-night-2026-10-01”). Concrete subpath resolves in one hop: `.worktrees/legacy-pre-night-2026-10-01/scripts/` (verified: `render.py`, `check-closure.py`, `compose-role.py`, …) | **PASS** (path not spelled to subdir level; see limits) |

Cold-read limits and ambiguities recorded:

- **No version string.** Current identity is the dated accepted delivery (`M6-FINAL-ACCEPTANCE.md` /
  `PW-01-FINAL-REPORT.md`); the old `VERSION` file is retired. A reader looking for `x.y.z` will not
  find one via AGENTS/README.
- **`MAIN-CUTOVER-REPORT.md` still dangling.** Root README’s “已接受身份与状态” points to it, but the
  file does not exist yet (it is this C3 handoff’s deliverable). Same forward reference already noted
  in the C1 entry check.
- **Sub-README phase labels.** `professional-workflow/charters/README.md` says “M2 candidate” and
  `methods/README.md` says “M4 accepted references / M5 candidate”. The package README’s Package-state
  paragraph states these labels describe their own snapshots and are not current acceptance, so the
  chain resolves — but only after reading that paragraph; the sub-READMEs alone read stale.
- **Legacy is local-only.** The branch/worktree are not on the remote; the README marks them 本地, so a
  fresh clone would not carry them. Retrieval is read-only (no import/restore procedure given, by
  design: 不要把旧体系当默认治理或在默认根恢复).
- **`upstreams/` in the legacy paragraph** refers to the legacy copy only (raw ignored assets), not a
  path in the new root tree; the sentence’s context makes this clear.
- Scope note: this is a documentation/reference cold read on the promoted local root; it does not
  re-run package qualification, does not accept M6, and does not cover remote promotion.
