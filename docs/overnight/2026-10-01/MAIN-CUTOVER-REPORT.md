# Main cutover · final report (2026-10-01)

**State:** Owner-authorized local mainline cutover is complete. Root default `main` is the new Professional Workflow; the complete old working state is preserved at `.worktrees/legacy-pre-night-2026-10-01` (`legacy/pre-night-2026-10-01`, old `main@496b067`). Local only: `origin/main` is unchanged and no push/tag/release/UCBIP action occurred.

## Objects

- Old root: `main@496b0676e302e2d0eafba129ff61de4c203d258a` (ahead of unchanged `origin/main@448c3d67c23994c86f5b0e344b82488823624586`).
- Fixed cutover object: `81f1ceff33699ca407b2644cd6c8b53673e40ee7` (C1 entry/retire commit `5ba5fa5`, evidence commits `a046e48`/`81f1cef`); this report and its commit are tip-only process records.
- Legacy worktree: `.worktrees/legacy-pre-night-2026-10-01`, branch `legacy/pre-night-2026-10-01`, HEAD `496b067`.
- Custody capsule (local, not committed or pushed): `.worktrees/preservation/tpw-main-cutover-20261001-c0/`.
- Night worktree retained: `.worktrees/night-2026-10-01`; untracked `scan.js` (7816 B) untouched.

## Preservation result (independent check PASS)

| Item | Identity |
| --- | --- |
| Staged set (8 = 6 A + 2 M) | `git diff --cached --binary` SHA-256 `8eb56e9edf6603e468ec59187990bbeae8a25891cc02532bbcfb5db00b504a91` |
| Unstaged edits (3) | `git diff --binary` SHA-256 `b6506ea2df3f484f3450a42451cdc8d9aac776d1e649f6e63fa3e433a218a3a4` |
| Untracked (21 files) | per-file SHA-256 matched in legacy worktree and custody copies |
| Ignored raw assets | `upstreams/` 1344 regular files + 2 recorded symlinks, manifest match |
| Index state | 8/8 staged index entries equal the captured root index |

The independent reader `tpw-night-check` verified C0 preservation, C1 entry, C3 cold read and spot-checked C2 in `docs/overnight/2026-10-01/MAIN-CUTOVER-PRESERVATION-VERIFY.md` (all PASS with tracked limits). Limits: the upstreams manifest covers regular files plus recorded symlinks; legacy is local-only; no recovery rehearsal was performed (Owner final clarification).

## Entry / core diff

- New root entry: `AGENTS.md` + `README.md` (one current path; legacy pointer; no old registry/render/check requirement).
- Retired from the active root (326 tracked files): `.decisions/`, `VERSION`, `principles/`, `roles/`, `scripts/`, `skills/`, `workflow/`, `sources/`, `upstreams.lock.yaml`, `docs/archive/`, `docs/artifacts.md`, `docs/closure-report.md`, `docs/coldstart.md`, `docs/downstream-mapping.md`, `docs/history/`, `docs/ledger.md` — all preserved in the legacy worktree and Git history.
- Kept: `professional-workflow/`, `adoption-examples/`, `docs/WORKFLOW-INTENT.md`, `docs/RESPONSIBILITY-BACKBONE.md`, `docs/OVERNIGHT-WORKFLOW-PLAN-2026-10-01.md`, `docs/overnight/`.
- `.gitignore` now tracks `.worktrees/`; `docs/WORKFLOW-INTENT.md` carries a dated cutover note.
- Core: only `professional-workflow/README.md` changed (title + current-status sentence) from accepted `11e6e3772b6bc0e17259c932b0c0dcabb030a133` to `91875114e51855517f92ef099cbdf60c34e68243`. No method/Profile/Charter semantics changed; Backbone bytes `ce82a700…` unchanged.

## New core manifest (19 files at the fixed core tree)

```text
053239f0cc8b8c5755c480a31d87a85b42357d508e37a2b491eb38d541b0a9df  professional-workflow/README.md
01fe9a811a465786ffec8bfd931a5140663bf9f86e85fdd87e4ace9f7d351d12  professional-workflow/authority/README.md
ce82a70016a4a3fc234ea287f39aac8d79a260ddf13747c4fb705bda580453ba  professional-workflow/authority/RESPONSIBILITY-BACKBONE.md
035f2a1f58cc28373a5f90b6478061bcad51d02b0cc341b7fd2d0ffb49306439  professional-workflow/charters/README.md
b159bf96323a9b89a286a5d80fdd703a1375da02467a60645e989b4903336627  professional-workflow/charters/examples/implementation-cross-module.md
038e6a31d699fad0d607cc23aebd02c8f0d6947051863beed98c3901653d3cc1  professional-workflow/charters/examples/implementation-local-fix.md
62050af72fdf53784d757026eb2569bf989ef770b8b95c692584e49245feba5f  professional-workflow/charters/examples/technical-planning-cross-module.md
f03cc007ff6e3c9b7a62f7fbe23953dce9ce0cc080f12fd3326d5084075a0cdb  professional-workflow/charters/template.md
24de9ce294c682afd7c9930a1000b2c5b37fb5a518edb34e3544b21ba6c87538  professional-workflow/methods/README.md
cfacc0f57cedadc6360ad0338645e43740dad4b1e15cc6876088eb89b4034f02  professional-workflow/methods/behavior-claim-evaluation.md
ab0a0bc03448407479fe82b92b2355384e7f2acf49c2ff3026882670f955a0a5  professional-workflow/methods/cross-module-design.md
1ba8f8f2fb46a0094c22e7ac946e27f30a27b1ce25e201fd5ede819ddc2e4215  professional-workflow/methods/local-defect-feedback-loop.md
2e103f2f05c038e4d6064cf2caf4c5d4cb482a3aba3e8205764db6488db49711  professional-workflow/profiles/README.md
d8b75a5734c015f70d4c3f1479e094be11b92f2ee20d193dc22726fd599377fa  professional-workflow/profiles/behavior-domain.md
8a2f42c874ca08c94b06e20131623178f5a45bc6b7d419a3a8fb7ce1651be399  professional-workflow/profiles/driver.md
d72b3a5097f142f5ea397ab423b146a3b853913c5c1de096d93b95133199f900  professional-workflow/profiles/evidence-evaluation.md
c96162668a1b80096c872a79321e07111a7eecc346f037f7060834f272b0aa5f  professional-workflow/profiles/implementation.md
0f3206ae22fa478c40402d60e17d197f8909184fe6a29b6c89ec4c6fa059ddc8  professional-workflow/profiles/intent-voice.md
d53da06edc99af3bcfc93c744af5f2cc8d512430d318a8b13b1b7f42652d74aa  professional-workflow/profiles/technical-planning.md
```

- Core subtree: `91875114e51855517f92ef099cbdf60c34e68243`; archive: `git archive --format=tar 81f1cef professional-workflow` SHA-256 `51489f61bd0bc11f66494526171e175f0fa2e063f0b80452184d759f32f139ad` (commit-specific; the earlier accepted `05f4bbb` archive identity `5d551aca…` stays bound to its own object).

## Status

- Local root `main`: clean; top level is `AGENTS.md README.md adoption-examples/ docs/ professional-workflow/`.
- Remote: `origin/main` `448c3d67…` unchanged; `origin/night/2026-10-01-workflow` `cf107522…` unchanged (local branch ahead by the cutover commits). No push by Driver.
- Crew: the ten old overnight workers were retired by Oracle (record `.worktrees/state/2026-10-01-pane-retirement.json`); retained Driver/Oracle/method/check; unnamed user pane untouched.
- Exceptions / limits: `/tmp` scratch deviation from the earlier PW-01 batch is retained as non-blocking; cold read found no version number beyond the acceptance identity, the report link that only resolves at this final tip, historical M2/M4/M5 sub-README labels (resolved via the package README status paragraph), and legacy being local-only.
- Stop: no automatic continuation, no remote `main` push, no tag/release/archive move, no UCBIP change, no method absorption. Oracle reads this milestone; Driver waits.

## Tail item · legacy `.pi` runtime (Oracle read-back follow-up)

The new root still physically held the ignored legacy `.pi/` runtime (`handoff`, `loops`, `repair`, `repair2`, `review-v4`, `tasks`). Ownership check before moving: no open handles on `.pi` (`lsof +D` empty), every file mtime was pre-cutover (newest `2026-10-01 01:28`), no file newer than the cutover window, and no loop field or runtime configuration was touched. The six directories were moved unchanged into `.worktrees/legacy-pre-night-2026-10-01/.pi/`; an empty `.pi/` container remains in the new root as the runtime path.

- Preserved content: 36 regular files (32K `handoff` + 136K `loops`; three dirs empty of files), 11 symlinks (all under `review-v4/probe2`), 32 directories.
- Custody manifests: `pi-runtime.files.sha256` `20142524f9edfd21fc98a9547df3d86244f1f9f85948d96aabdd4d4a96531534`, `pi-runtime.files.stat` `ced588dc23a5a32f60c95a30a7da03d1207e7d6b828b6981d7fe466057c7341b`, `pi-runtime.symlinks.stat` `c7e5709758f9ce72c5630e5aa2e5d1954f422feb916e53630f25dea91c19518e`, `pi-runtime.dirs.stat` `e3550d0021c3a66d5c85c9a5f526175b7f21a901e26b927accc49ba9f83ec784`; all four re-verified against the moved content (files/symlinks/subdirs byte- and attribute-identical; the legacy `.pi` container mtime was aligned to the recorded original).
- Limits: symlink targets were preserved verbatim; absolute targets that pointed into the old root `.pi/review-v4/probe2/...` (and `/tmp` leaves) now dangle by design — they are historical probe fixtures, not live paths. No live dependency was found; no unknown session was closed and pane `pN` was untouched.
- Evidence: independent targeted check in `MAIN-CUTOVER-PRESERVATION-VERIFY.md` (“Tail item · legacy .pi runtime”).
