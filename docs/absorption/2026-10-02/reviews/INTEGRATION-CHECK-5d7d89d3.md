# Integration check · commit `5d7d89d3`

State: **mechanical identity/reference/hash check** by `tpw-night-check` (Pi session `01a0f66d-0b7b-7701-8c51-8d262cb2f8d4`, `commandcode/deepseek/deepseek-v4.1-flash` / max), 2026-10-02. No professional review, no product edit, no commit; this file is the only write.

Objects:

| Object | Value |
| --- | --- |
| Checked commit | `5d7d89d3f8fc295ed7c96e63a2af8952e75398ec` (“docs(workflow): metadata-only status correction — prior baseline accepted, current candidate pending Pro/Oracle; remove stale pending sentence”, parent `5c7a2bd`) |
| Previous object | `c7215694` (core `a1a27613…`) |
| Core subtree | `0e7614cd4eec20b4b43b7b0caba43187d3ec10b4` — matches |
| Archive at candidate | `git archive --format=tar 5d7d89d3 professional-workflow` SHA-256 `2758099eabcaeb8c4c19deab22a4341e48323ea8313ab42f49f2110d439e3395` — matches `2758099e…` |
| Backbone | `ce82a70016a4a3fc234ea287f39aac8d79a260ddf13747c4fb705bda580453ba` — unchanged |
| Night HEAD at check | `a5f9622` (later docs commits); working tree clean except untracked `scan.js` |

## Checks

| # | Check | Observed | Result |
| --- | --- | --- | --- |
| 1 | Relative to `c7215694`, product change is only the 4 metadata files; no method/Backbone/authorization semantics | `git diff --name-status c7215694 5d7d89d3 -- professional-workflow` = exactly `README.md`, `charters/README.md`, `methods/README.md`, `profiles/README.md` (4 files, +8/−6). Per-file diffs are status/pointer wording only: package README title + “Package state” status text (prior baseline accepted; current absorption candidate’s Oracle/Pro overall acceptance not yet complete); `charters/README.md` status note adds the LEDGER pointer and the pending-acceptance caveat; `methods/README.md` “Current state” replaces the stale pending sentence with “All gate-reviewed absorption deltas are integrated; no held items remain”; `profiles/README.md` adds a “Current:” note and the same LEDGER pointer. No method body, Profile semantics, Backbone or authority text changed. Full commit also carries process records (`docs/absorption/…/LEDGER.md` M, previous `INTEGRATION-CHECK-c7215694.md` A) — not product. | **PASS** |
| 2 | New core subtree / archive identity | subtree `0e7614cd…`; archive `2758099eabcaeb8c4c19deab22a4341e48323ea8313ab42f49f2110d439e3395`; both match the supplied objects | **PASS** |
| 3 | Relative links still resolve, no dangling | 7 relative Markdown links, 0 dangling; backticked outside-package refs also resolve: `../adoption-examples/ucbip.md` (ADOPTION.md, package README), `../adoption-examples/cross-module-start.md`, `../authority/` | **PASS** |
| 4 | Backbone unchanged | `ce82a700…` | **PASS** |
| 5 | `methods/*.md` 42/42 still indexed; stale pending sentence gone | `methods/README.md` contains all 42 method filenames; pattern counts: “Pending gate-confirmed” = 0, “not yet integrated” = 0, “shared Profile merge” = 0, “no held items remain” present | **PASS** |
| 6 | Absorption identity files present; `STOPPAGE-2026-10-03.md` byte-identical to root | At the candidate: `LEDGER.md`, `STOPPAGE-2026-10-03.md`, `reader/` (3 `READER-*.md`), `reviews/` with `GATE-HANDOFF.md`, `REVIEW-QUEUE.md`, `INTEGRATION-CHECK-6b64b59.md`, `INTEGRATION-CHECK-c7215694.md` and the review/oracle records. `STOPPAGE-2026-10-03.md` is tracked at the candidate and both the night worktree and the root checkout hash to `12c4c2782e85b9a535fbf759f1583c83615fd39d57ca3e8d372baca690bf2397` — byte-identical, matching the stated `12c4c278…`. | **PASS** |

## Residual

- No anomaly found. (The previous stale pending sentence identified in `INTEGRATION-CHECK-c7215694.md` is removed by this commit; the remaining status text is consistent with “prior baseline accepted / current candidate pending Pro-Oracle”.)
- Scope: identity, paths, links and declared state only; the absorbed content was not evaluated, and this check accepts nothing.
