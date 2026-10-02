# Integration check · commit `c7215694`

State: **mechanical identity/reference/hash check** by `tpw-night-check` (Pi session `01a0f66d-0b7b-7701-8c51-8d262cb2f8d4`, `commandcode/deepseek/deepseek-v4.1-flash` / max), 2026-10-02. No professional review, no demo, no product edit, no commit; this file is the only write.

Objects:

| Object | Value |
| --- | --- |
| Checked commit | `c721569460eeef7f4b312f1b7ab363520576a1bf` (“docs(workflow): current-state wording after all reviewed deltas integrated”, parent `89915e2`) |
| Core subtree | `a1a276138e1e28542541d6c10c8a6a8ad1df6230` — matches |
| Archive at candidate | `git archive --format=tar c7215694 professional-workflow` SHA-256 `6ad60594713bc00291fb4cab00439201701d3883165be3c1d01e3e0007ee076b` — matches |
| Backbone | `ce82a70016a4a3fc234ea287f39aac8d79a260ddf13747c4fb705bda580453ba` — unchanged |
| Night HEAD at check | `9616dac` (later docs commits); working tree clean except untracked `scan.js` |

## Checks

| # | Check | Observed | Result |
| --- | --- | --- | --- |
| 1 | Core path set / file count / subset identity | `c7215694:professional-workflow` = 59 files; vs the previous integration `6b64b59` (30 files) there are **0 deletions / 0 renames** — pure superset: 15 modified + 29 added. Methods tree = 43 md files (42 method files + `README.md`). Subtree and archive match the supplied objects. | **PASS** |
| 2 | Every `methods/*.md` indexed in `methods/README.md`; no stale held section | 42/42 method files appear by name in `methods/README.md` (selection table, on-demand guides, and the “Absorption batch (2026-10-02)” table). The old “Pending gate-confirmed fixes and therefore not yet integrated: …” section is **gone**; L66 states “All gate-reviewed absorption deltas are integrated; no held items remain,” and all 10 previously-pending method files (`handoff-and-resume`, `domain-state-and-invariants`, `verification-harness-design`, `change-review`, `bounded-prototype`, `guide-change-shape`, `guide-professional-explanation`, `rationale-and-premise-review`, `agent-facing-cli-contract`, `decision-elicitation`) now exist. L64 keeps the accurate B1/B2 resolution note (“`architecture-survey.md` uses the B2 canonical version; the B1 duplicate is not installed”). | **PASS** (one stale wording pointer noted below) |
| 3 | Markdown relative links resolve, no dangling | 7 relative Markdown links across the package, all resolve: `README.md` → `authority/RESPONSIBILITY-BACKBONE.md`, `authority/README.md`, `profiles/README.md`, `charters/README.md`, `methods/README.md`, `ADOPTION.md`; `charters/README.md` → `../methods/README.md`. The named outside-package references also resolve: `../adoption-examples/ucbip.md` and `../adoption-examples/cross-module-start.md` (both exist at the commit; ADOPTION.md L84 documents that a vendored copy of `professional-workflow/` alone may not include them, which is an explicit caveat) and `../authority/` (→ `professional-workflow/authority/`, exists). 0 dangling. | **PASS** |
| 4 | `profiles/evidence-evaluation.md` keeps both B1 and B2 pointer lines | Final pointer block retains the B1-era lines — `methods/behavior-claim-evaluation.md` (expanded wording), `methods/guide-redacted-evidence.md`, `methods/guide-test-evidence-quality.md` — and adds the B2 line `methods/behavior-contract-examples.md`; diff vs `6b64b59` shows no pointer line removed (only the behavior-claim line was reworded), plus the unchanged binding-status line pointing to `methods/README.md`. | **PASS** |
| 5 | Backbone unchanged | `c7215694:professional-workflow/authority/RESPONSIBILITY-BACKBONE.md` = `ce82a700…` | **PASS** |
| 6 | `git diff --check` clean; no `scan.js`/tmp mixed in | `git diff --check 6b64b59 c7215694` and `git show --check c7215694` both clean; the integration diff and the commit tree contain no `scan.js`, `*.tmp`, scratch or `/tmp/` paths (`scan.js` stays untracked in the worktree). | **PASS** |
| 7 | `docs/absorption/2026-10-02` review/reader/ledger identity files present | `LEDGER.md`; `reader/READER-EXISTING-GOV.md`, `READER-LIGHTWEIGHT.md`, `READER-PROFESSIONAL-USE.md`; `reviews/` 51 files including `GATE-HANDOFF.md`, `REVIEW-QUEUE.md`, `INTEGRATION-CHECK-6b64b59.md`, the `REVIEW-A*`/`REVIEW-B1-*`/`REVIEW-B2-*`/`REVIEW-GATE2-*`/`ORACLE-REVIEW-*` records. | **PASS** |

## Anomaly / residual (non-blocking)

- `methods/README.md` L89 (“Current state”) still says “Pending gate-confirmed fixes and the shared Profile merge are listed in the absorption batch section and `docs/absorption/2026-10-02/LEDGER.md`.” The referenced pending list no longer exists (the batch section now says no held items remain, all 10 previously-pending files are integrated, and `LEDGER.md` `CAND` records “全部已审 delta 集成、无 held”), and the shared `evidence-evaluation.md` B2 pointer has landed. This is a stale wording pointer in one sentence — path/hash/reference checks are unaffected; a wording pass can drop or re-scope the sentence.
- Scope: identity, paths, links and declared state only; the absorbed content was not evaluated, and this check accepts nothing.
