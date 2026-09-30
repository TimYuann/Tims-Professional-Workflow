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
