# Decisions · 2026-10-01 Overnight

Append-only. Each entry distinguishes accepted direction from observed facts and names its evidence.

## D-001 · Fix the overnight candidate identity and output boundary

- **Recorded:** 2026-10-01 by `tpw-night-driver`.
- **Accepted basis:** Owner's overnight authorization and the accepted plan in `docs/OVERNIGHT-WORKFLOW-PLAN-2026-10-01.md`, with the frozen input `docs/RESPONSIBILITY-BACKBONE.md` at `a77c3974128cee6059b1662579e3803fc1bdfcb9`.
- **Decision:** Build the greenfield candidate only under `professional-workflow/`; keep this night's status, decisions, candidates and evidence under `docs/overnight/2026-10-01/`. Keep `upstreams/` and the original worktree read-only. Do not change the Backbone or UCBIP, and do not push, merge, tag or publish.
- **Observed baseline:** Candidate branch `night/2026-10-01-workflow` starts from plan commit `496b0676e302e2d0eafba129ff61de4c203d258a`; its current bootstrap child is `fc746d81db43b58515e7ecba078884a05a472c12`. Candidate worktree was clean before this entry. The original worktree's 8 staged paths and other dirty/untracked paths have a read-only preservation snapshot at `/private/tmp/tpw-legacy-preservation-20261001/`.
- **Scope:** This fixes the local candidate and evidence locations for M0–M6; it does not accept any Profile, Charter, method or implementation candidate.

## D-002 · Serial package integration with isolated candidate write sets

- **Recorded:** 2026-10-01 by `tpw-night-driver`.
- **Accepted basis:** The overnight plan's shared-write rule and the Owner's handoff identifying `tpw-night-profile` (`w27:pE`) and `tpw-night-source` (`w27:pF`) with bounded first assignments.
- **Decision:** Preserve those separate authoring sessions and their stated write sets. The Driver alone writes shared package configuration and performs serial integration. A candidate's authorship or completed report is not acceptance; each new relied-on claim requires an independent evaluation before integration/closure.
- **Runtime evidence:** Herdr shows two live Pi sessions with separate session paths; their session records identify provider `commandcode`, model `deepseek/deepseek-v4.1-flash`, and `thinkingLevel: max` on runtime events and assistant message metadata. Driver runtime is `gpt-6-luna / xhigh`; Oracle is `gpt-6.1-sol / medium`.
- **Scope:** No new authority is created by Profile names, Charters, messages, model settings or package configuration.

## D-003 · Reserve Owner's two Pro audit allowances for fixed milestones

- **Recorded:** 2026-10-01 by `tpw-night-driver` after reading `docs/overnight/2026-10-01/PRO-AUDIT-ALLOWANCE.md` in full.
- **Accepted basis:** Owner's explicit two-review authorization and its preserved scope in that file; it supplements the accepted plan only for the described review branch push.
- **Decision:** Keep the count at 0/2 until a review is actually sent. Oracle chooses whether and when to use the allowances; preferred candidates are the full M5 integration and fixed M6 delivery. The allowance is not a per-stage gate. Oracle operates ego-browser/ChatGPT Pro and the GitHub connector; Driver prepares the exact commit/tree, branch and concise read list.
- **Push boundary:** Once Oracle selects a fixed review object, only the night branch may be pushed to `origin` for that review. `main`, tags, force-push and the original worktree's dirty/index state remain excluded. The authorization does not permit UCBIP, production, migration or publication actions.
- **Preservation:** `PRO-AUDIT-ALLOWANCE.md` is a supplied process artifact and remains unchanged; include its exact content in the next process checkpoint.

## D-004 · Keep article summaries outside the adopted method evidence

- **Recorded:** 2026-10-01 by `tpw-night-driver` after the bounded M4 survey and Owner's source-evidence instruction.
- **Evidence:** `SOURCE-SURVEY.md` §8 records that the two cached article files are derived notes, not original text; X remains `UNVERIFIED`, and the fixed mirror was not read in full for an active method.
- **Decision:** The cached notes may locate a method candidate only. Before any S4/S5 method enters the active path, independently reread its complete original page or a pinned full-text mirror and record which source was actually read. Keep the X source `UNVERIFIED` unless the original is actually verified. No article method is active now.
- **Scope:** This bounds M4 to methods that support the two planned M3 tasks; it does not reopen broad source research or convert a source index into adoption.
