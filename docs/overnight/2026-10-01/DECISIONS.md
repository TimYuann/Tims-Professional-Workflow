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

## D-005 · Accept the fixed M1 Profile content for downstream composition

- **Recorded:** 2026-10-01 by `tpw-night-driver` after verifying the ten object hashes listed in `M1-REPORT.md`.
- **Decision authority/evidence:** Oracle's acceptance in `docs/overnight/2026-10-01/ORACLE-ACCEPTANCE.md`; independent M1 review and differential are in `PROFILE-EVALUATION.md` and `METHOD-REVIEW.md`.
- **Accepted scope:** The seven fixed Profile files plus their candidate/evaluation reports are accepted as M1 inputs for M2/M3. The original M1 FAIL finding is retained unchanged as evidence; the single-file correction is independently PASS.
- **Not accepted by this decision:** Candidate method entries, actual task-specific delegation inheritance, Charter activation/cold-start, M3 behavior, and M5/M6 package qualification. This acceptance consumes no Pro audit allowance and adds no UCBIP or publication authority.

## D-006 · Select a bounded M4 method-integration candidate set

- **Recorded:** 2026-10-01 by `tpw-night-driver` after reading `METHOD-CANDIDATES.md` and MR-02/MR-04 in `METHOD-REVIEW.md`.
- **Candidate scope:** (1) local-defect feedback loop based on S3 `diagnosing-bugs` with two limited S1 additions; (2) cross-module design based on S3 `codebase-design` + `DEEPENING` with three limited S1 contract/error/compatibility elements; (3) S2 `verify-this` claim/baseline/treatment method with the strict three-state mapping. Exact retained, limited and deferred elements are in `METHOD-CANDIDATES.md`.
- **Decision status:** This is the Driver's bounded integration proposal under the accepted active-path envelope, not final method acceptance. `tpw-night-method` has independently rated the dossier PASS; Oracle acceptance of the integrated method package remains for the M4 milestone. Do not integrate S4/S5 article methods, S2 control/loop/PR mechanics, DESIGN-IT-TWICE parallel counts, or the deferred `interrogate`/`code-review` lenses as mandatory paths.
- **Vocabulary / authority boundary:** Responsibility and authorization terms remain owned by the frozen Backbone; domain terms remain owned by accepted C objects. Technical D methods may use `module`/`interface`/`seam` without renaming Backbone responsibility boundaries or gaining B/C authority. Methods grant neither permissions nor applicability triggers.
- **Revalidation:** No M3 execution has occurred yet. If later integration changes active Profile/Charter/Skill/routing semantics after M3 evidence exists, invalidate only affected coverage and retest per the accepted plan.

## D-007 · Accept B/C exercise inputs for the M3 snapshot fixture

- **Recorded:** 2026-10-01 by `tpw-night-driver` after checking the outputs against their fixed Charter inputs.
- **Decision owners:** `tpw-night-m3-bc` accepted behavior and domain meanings under `fixtures/m3-snapshot/BC-CHARTER.md`, using `CASE-INPUT.md` and the frozen fixture source structure.
- **Accepted objects:** `BEHAVIOR-CONTRACT.md` v1 (SHA-256 `86dd6664b73de07ceefdbc5f4d03e09f49b4b1f2ee11cb6a80e48c251176555c`) and `DOMAIN-SEMANTICS.md` v1 (SHA-256 `15537d71d100dde30075f724c1ef79bc0d4e6a76a179f7f82d7f6c6b286cda06`). Both explicitly restrict their meaning to this synthetic fixture; neither selects D/E module placement or implementation.
- **Scope:** D may depend on these versions when drafting the exercise Plan. They do not define UCBIP/other product behavior, accept a technical design or implementation, or close M3.

## D-008 · Accept the fixed M4 method package as downstream input

- **Recorded:** 2026-10-01 by `tpw-night-driver` after Owner's M4 milestone acceptance.
- **Accepted object:** Commit `013659331c8c5f9f54b866b393972a03d7938773`, tree `2fc8db5e9bbd0a2c37888282c89c2328505fddee`; Oracle verified the five committed summaries for three method bodies, `methods/README.md`, and `METHOD-REVIEW.md`. The independent MR-06/07/08 scope is recorded in `ORACLE-ACCEPTANCE.md`.
- **Decision:** The three bounded methods and their selection entry are accepted as reliable downstream inputs: local-defect feedback loop, cross-module design, and behavior-claim evaluation. S4/S5 and the listed alternatives remain deferred; article originals are not represented as verified or adopted.
- **Limits:** This does not accept actual Profile/Charter binding, final M3 evidence coverage, runtime dependency closure, cold-start, or M5/M6 package qualification. If a later binding or routing change alters active semantics, mark only affected M3 coverage invalid and rerun it. Pure formatting or semantics-preserving metadata changes need an integrator diff check, not another Sol method review; ask for method judgment only for a new or changed relied-on claim.
- **Scope:** This acceptance consumes no Pro review allowance and grants no UCBIP, deployment, publication, or release authority.
