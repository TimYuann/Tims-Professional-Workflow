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

## D-009 · Bind only the selected M4 methods in the M3 exercise Charters

- **Recorded:** 2026-10-01 by `tpw-night-driver` as an M5 integration candidate, using the fixed M4 selection entry accepted under D-008.
- **Candidate binding:** Case 1 E selects `local-defect-feedback-loop.md`; case 1 F selects `behavior-claim-evaluation.md`; case 2 D selects `cross-module-design.md`. Each Charter cites the M4 accepted commit and per-file digest. Only the named method body is inserted after the Charter in the prompt, before task inputs.
- **Reason:** The M4 selection entry maps these three method needs to the two bounded M3 paths. A reusable Profile alone does not activate a method. This explicit field lets each task bind only what it needs.
- **Coverage effect:** Case 1 E's existing candidate and self-check predate method binding. Preserve them as author evidence, but mark final M3 method coverage invalid until a targeted method-bound E pass and independent F evaluation. Case 2 has no prior D output; its updated fixed prompt binds the D method, while independent challenge remains required before E starts.
- **Fixed-input record:** The original case 1 prompt actually sent to E is preserved byte-for-byte at `docs/history/2026-10-01/M3/STARTUP-PROMPT-PRE-M4.md` (SHA-256 `f1e9afe77856f1bf3e4f6e694a9f78f59363dedf7d00156ef00b311b4cf4105f`). The new targeted revalidation prompt is `fixtures/m3-local-fix/STARTUP-PROMPT.md` (SHA-256 `d6e2768326fede1856cae430f07f566ca562e41ca827976560f84adf36b6444b`). The earlier case 2 prompt hash `d0580554198ae016471d55ea11c64641a4862dbc298154ced8971d25111e1393` was never sent; its replacement is fixed at `0f6d0e4e028543676273b33c1d0c74e5d933da2ed033be3f9669ca83ac748c90`.
- **Limits:** This is not a new method acceptance, a universal trigger, an authority grant, or M3 milestone acceptance. New method claims remain subject to independent method evaluation; semantics-preserving package metadata edits do not.

## D-010 · Preserve the results of the repository-prescribed structural checks

- **Recorded:** 2026-10-01 by `tpw-night-driver` after integrating the M5 candidate and archiving the original pre-M4 E prompt.
- **Observed:** `python3 scripts/render.py` exited 0 without changing generated files. `python3 scripts/check-consistency.py` passed all 7 checks after the consumed pre-M4 prompt was moved to `docs/history/`; `python3 scripts/compose-role.py --check` passed. `python3 scripts/check-closure.py` returned 19 PASS / 2 FAIL across 135 scanned library files: C1 requires a Git tag, and D1 detects tool/model names in the accepted overnight plan and bootstrap/process records.
- **Disposition:** Do not create a tag, weaken or modify a checker, hide process evidence, or treat these legacy-registry checks as proof of the new package. C1 remains blocked by the explicit no-tag boundary. D1 is a scope mismatch between the checker’s whole-library scan and the required tool-specific execution evidence; the `professional-workflow/` product documents themselves remain tool-independent. The M6 verifier must check the clean package directly and report the legacy results as residuals.
- **Scope:** These checks do not establish method effectiveness, live binding, cold-start, or M3/M5/M6 acceptance.

## D-011 · Record final structural-check rerun after the M6 export manifest

- **Recorded:** 2026-10-01 by `tpw-night-driver` after adding `M6-PACKAGE-CANDIDATE-f11de8b.md`.
- **Observed:** `python3 scripts/render.py` exited 0; `python3 scripts/check-consistency.py` passed 7/7 (including S2, 116 files); `python3 scripts/compose-role.py --check` passed. `python3 scripts/check-closure.py` remained 19 PASS / 2 FAIL across 136 files (C1 no tag, D1 scans tool-specific execution records). The export manifest independently checked all 19 package files; see the M6 candidate report.
- **Disposition:** D-010 remains the original result. No checker or source assertion changed. No tag, push, merge or UCBIP action occurred.

## D-012 · Correct the earlier Herdr environment attribution

- **Recorded:** 2026-10-01 by `tpw-night-driver` after Owner supplied Oracle's foreground-process observation.
- **Separate check:** `test "${HERDR_ENV:-}" = 1` exited 0. Per-field `printenv` showed `HERDR_ENV=1`, `HERDR_WORKSPACE_ID=w27`, `HERDR_TAB_ID=w27:t1`, `HERDR_PANE_ID=w27:pD`; the exec shell parent PID was `86526`.
- **Foreground process check:** `ps eww -p 86526 -o command= | tr ' ' '\n' | rg '^HERDR_(ENV|WORKSPACE_ID|TAB_ID|PANE_ID)='` exited 0 under authorized read-only escalation and showed the same four values, with no other environment values emitted.
- **Prior result / correction:** The earlier combined command was `test "${HERDR_ENV:-}" = 1 && herdr agent list`. Its tool result was `Error: Os { code: 1, kind: PermissionDenied, message: "Operation not permitted" }`; it provided no isolated `test` result. It did not establish a missing `HERDR_ENV`. The prior attribution in `STATUS.md` was incorrect. Current shell and foreground process both show the same Herdr context, so there is no evidence of session detachment; the previous error was a sandbox/tool-operation denial, inferred from its permission error.
- **Scope:** This appended correction preserves all earlier decision entries and does not alter UCBIP, tags, or publish permissions.

## D-013 · Resume and confirm M3 D/E/F dispatch through Herdr

- **Recorded:** 2026-10-01 by `tpw-night-driver` after separate guard and roster calls succeeded.
- **Runtime:** `herdr agent list` exited 0. Newly started D and E Pi sessions displayed live footers `DeepSeek V4.1 Flash (CommandCode) · think:max`; this verifies runtime configuration beyond argv.
- **D:** `tpw-night-m3-design`, pane `w27:pJ`; fixed input `fixtures/m3-snapshot/D-STARTUP-PROMPT.md`, SHA-256 `0f6d0e4e028543676273b33c1d0c74e5d933da2ed033be3f9669ca83ac748c90`; write set `TECHNICAL-PLAN.md`. After one prompt, `herdr agent get` reported `working` (state change seq 12191).
- **E:** `tpw-night-m3-local-bound-e`, pane `w27:pM`; fixed input `fixtures/m3-local-fix/STARTUP-PROMPT.md`, SHA-256 `d6e2768326fede1856cae430f07f566ca562e41ca827976560f84adf36b6444b`; write set `src/labels.py` and `tests/`. After one prompt, `herdr agent get` reported `working` (state change seq 12190).
- **F:** Existing independent evaluator `tpw-night-method`, pane `w27:pG`; fixed prompt `fixtures/m3-local-fix/F-STARTUP-PROMPT.md`, SHA-256 `75ef8c4305b7f4255a75b379d5ae6b7c44feeb002c30c1d4aa6b1226dace4bbd`; target code/test object is commit `9699276ab1d413379ace91afa0cf683a83b69aa3`. After one prompt, `herdr agent get` reported `working` (state change seq 12193). Held criteria were not copied into shared inputs.
- **Limits:** These are confirmed starts, not completed results. If E changes code/test bytes, F's present conclusion is limited to commit `9699276` and only the changed object needs reevaluation. D's Plan still requires its independent challenge before case-2 E may start.

## D-014 · Preserve the coordination incident and retain the unmet morning target

- **Recorded:** 2026-10-01 by `tpw-night-driver` after reading Oracle's [DRIVER-COORDINATION-INCIDENT.md](DRIVER-COORDINATION-INCIDENT.md) in full. The incident artifact is preserved unmodified.
- **Incident evidence:** The prior pause at 03:52 occurred with M3/M6 incomplete and Pro 0/2. The first combined Herdr command did not capture per-call exit status; later evidence disproved the claim that `HERDR_ENV` was absent. The report retains the incident's evidence boundary and identifies the permission/tool failure as the supported explanation, without asserting an unobserved low-level cause.
- **Outcome record:** At the 03:52 pause, the planned 08:00 closure objective remained unmet. Resuming D/E/F work is recovery activity and does not rewrite that checkpoint as success. M3, M5, and M6 remain open until their actual criteria and final report are satisfied.
- **Continuity:** Keep all earlier decision rows intact. Continue only within the existing night authorization; actual D/E/F starts are recorded in D-013. The incident and recovery do not change the no-push/no-tag/UCBIP boundaries or consume a Pro review.

## D-015 · Record completed case-1 method-bound E evidence and independent F verdict

- **Recorded:** 2026-10-01 by `tpw-night-driver` from `tpw-night-m3-local-bound-e`'s retrieved response and `tpw-night-method`'s fixed evaluation report.
- **E revalidation:** The method-bound input was prompt SHA `d6e2768326fede1856cae430f07f566ca562e41ca827976560f84adf36b6444b`. E reports two repetitions of `python3 -m unittest discover -s tests -v` exiting 0, the original discriminating input passing, the bounded edge observations, and a seed-implementation negative control with 3/7 failures. E changed no files. Its full response is preserved verbatim in `M3-LOCAL-E-REVALIDATION.md` (SHA-256 `82b755517c703aed8f9a71951458aa6ee937b7db62577424088479a0ccd350ff`).
- **Independent F:** `M3-LOCAL-EVALUATION.md` reports PASS for code/test object `9699276ab1d413379ace91afa0cf683a83b69aa3` only (report SHA-256 `0cfb21cc9aab60be142af48c45673bc489acb32c17b57f4ee7635e50c6c6ebc1`). F independently reproduced the baseline failure, ran candidate old/full suites, and ran a negative control. It kept private case criteria out of the repository. The E and F reports name identical source/test hashes; Driver's targeted `git diff` against `9699276` confirmed those bytes remain unchanged.
- **Residual:** The contract says “whitespace” without enumerating the Unicode set; E used Python `str.split()` semantics and recorded the edge as unresolved. This did not change the fixed code/contract or the scope of F's claim. Preserve the limitation; do not silently expand the contract.
- **Limits:** This closes only case-1 E revalidation plus F evaluation for the fixed code/tests. It does not complete case 2, accept the D Plan, or accept M3/M5/M6. Any later change to code/test bytes requires a new fixed object and targeted evaluation.

## D-016 · Hold case-2 E pending independent challenge of D's fixed Plan

- **Recorded:** 2026-10-01 by `tpw-night-driver` after D returned a candidate and Herdr state settled.
- **Fixed candidate:** `fixtures/m3-snapshot/TECHNICAL-PLAN.md`, SHA-256 `bcc10e4829918532f695b2d8be838d1aa2a2b9b8556c7654b5b14f1ce44adc1a` (188 lines). D reports all B/C/startup bindings match and the fixture source/tests/B/C objects remain untouched. The candidate is not yet committed or accepted.
- **Finding requiring review:** Plan §0.2/R-9 flags that D's Charter cites the M4 accepted cross-module method hash `30066c8b…`, while the startup prompt embeds a different method-file revision and the current M5 package file is SHA-256 `ab0a0bc03448407479fe82b92b2355384e7f2acf49c2ff3026882670f955a0a5`. D reports that the normative Use/Method/Limits sections match across these revisions but identifies a different deferral sentence and status metadata. Driver verified the accepted-source and current-file hashes; Driver has not adjudicated semantic equivalence or the binding.
- **Action:** Send this exact candidate to `tpw-night-method` for the already-preheld independent D challenge, including R-9. Do not start case-2 E until the fixed Plan has been challenged and D has decided any returned finding.
- **Limits:** This is a source-binding/configuration issue for method review, not a new method acceptance or an Owner decision. No case-2 implementation, M3 closure, or package acceptance follows from this record.

## D-017 · Fix the D Plan candidate and start its independent challenge

- **Recorded:** 2026-10-01 by `tpw-night-driver` after D's session settled and delivered its response.
- **Fixed candidate:** Commit `e3b2d3cbb8664466fc9fd6d7e461dab82752ec19`, tree `4024c85c47840ddcd5df3ca7a073813892263988`; `TECHNICAL-PLAN.md` SHA-256 `bcc10e4829918532f695b2d8be838d1aa2a2b9b8556c7654b5b14f1ce44adc1a` (188 lines). The candidate keeps case-2 E held.
- **Independent challenge:** `tpw-night-method` received fixed prompt `fixtures/m3-snapshot/METHOD-CHALLENGE-PROMPT.md` (SHA-256 `cf1eb0ea0ec500b18adc71d3f9a44f42fe94c07390e4f7d65162f272a2346bf3`) against the fixed commit. Herdr reports the method reviewer `working` (state change seq 12204).
- **Question under review:** Plan §0.2/R-9 reports that the accepted M4 method hash, embedded method text in the D prompt, and current M5 method file refer to three revisions; D says normative sections match and identifies metadata/deferral-text differences. Driver has verified the accepted and current hashes but makes no semantic-equivalence ruling. The challenge must decide whether the Plan's method binding is sufficient, needs a bounded revision, or returns to an authority.
- **Limits:** Challenge is not Plan acceptance. D retains delegated Plan acceptance after receiving findings. Do not start case-2 E until D decides/revises the challenged object. No M3/M5/M6 acceptance follows from fixing this candidate.

## D-018 · Start an independent package-use/isolation review for M5 candidate f11de8b

- **Recorded:** 2026-10-01 by `tpw-night-driver`; one fresh Flash reviewer is assigned.
- **Fixed object:** M5 package commit `f11de8b4b35015b14dfc50dd94d19525e424cd07`, tree `252093659181f0fd73e8ef6f9316e0778f524961`. Prompt `M5-PACKAGE-REVIEW-PROMPT.md`, SHA-256 `f35989cf7a730ceb73fd49074262fe702e11066bcabb2623ef5f29a9ddb9a5e3`.
- **Scope:** Independent review of package-root startup usability, ownership boundaries, Backbone export identity, method source path/anchor traceability, and legacy-library isolation. Reviewer must read the fixed commit, may run only a synthetic text assembly, and may write only `M5-PACKAGE-INDEPENDENT-REVIEW.md`; it cannot accept method effectiveness or the M5/M6 milestones.
- **Runtime/dispatch:** `tpw-night-m5-review` in `w27:pP`; live footer verified `DeepSeek V4.1 Flash (CommandCode) · think:max`; Herdr state changed to `working` after dispatch.
- **Limits:** This partial review does not include final M3 evidence or Pro review. It does not consume a Pro allowance, alter the fixed package, or authorize UCBIP/publish actions.

## D-019 · Record the independent case-2 Plan challenge and route PC-1 to B/C

- **Recorded:** 2026-10-01 by `tpw-night-driver` from `M3-SNAPSHOT-PLAN-CHALLENGE.md` (SHA-256 `bf3e15de71f4bf82adaa5547b9c412b4384a90d9d919420d5023fd9f593ab126`) against Plan commit `e3b2d3cbb8664466fc9fd6d7e461dab82752ec19`, tree `4024c85c47840ddcd5df3ca7a073813892263988`.
- **Verdict:** FAIL for the Plan as an implementation dependency, with one blocker PC-1. The current B/C Conditions/R-2 say any change to recorded `src/**`/`tests/**` invalidates B/C acceptance, while the authorized E task must change that same structure. Until the B/C owner clarifies baseline identity versus permitted implementation/test diffs, E cannot rely on the present B/C acceptance under this Plan.
- **Bounded findings:** PC-2 corrects an aggregate recipe fact: byte-order sorting by path yields the recorded `dbd6a306…` aggregate; sorting complete digest lines yields `9074f27d…`. The B/C source record's sort key is ambiguous and has been routed to its owner for a bounded correction. R-9 is not a separate blocker: the challenger independently verified that the normative method body is identical across the cited revisions and that M4 accepted the fixed 0136593 object; the provenance note still needs alignment. No new method gate was added.
- **Routing:** `tpw-night-m3-bc` was prompted to resolve PC-1 within its authorized B/C write set and clarify the aggregate recipe; it is working. `tpw-night-m3-design` owns response or revision of the Plan after B/C reply. No case-2 E work starts while PC-1 is unresolved.
- **Limits:** This does not reject B/C meanings, the core coherence design, or M3 as a whole; it does not accept the Plan. Any B/C new version or D Plan revision requires exact new hashes and only affected challenge coverage to be rerun. M5/M6 independent work continues separately.

## D-020 · Preserve the independent M5 package-use/isolation findings

- **Recorded:** 2026-10-01 by `tpw-night-driver` from `M5-PACKAGE-INDEPENDENT-REVIEW.md` (SHA-256 `53ed90a006fe0e58db1344c571a49febd59acfb4b1ea918c78178285570a2ecc`) on fixed package commit `f11de8b4b35015b14dfc50dd94d19525e424cd07`, tree `252093659181f0fd73e8ef6f9316e0778f524961`.
- **Passed checks:** package identity, in-package links, both documented text assemblies with synthetic input, Backbone byte identity, upstream pin/path/anchor existence, and the absence of legacy runtime dependencies in the package.
- **Findings:** F1 (high traceability): shipped M5 method files and two Charter digest pins do not match the exact M4 accepted method object digests; the F method file has no shipped digest. F2 (low status): frozen M1 Profile files still say “待 M4” without a package-level supersession note. F3 (low provenance): the Backbone export disclaimer omits two source-history references. F4 (info): example Profile paths use repo-root form while assembly runs from package root.
- **Disposition:** M5 package candidate is not accepted. Update only package identity/status/path/provenance metadata to make shipped bytes verifiable, then send the exact diff and hashes for targeted independent recheck. Do not rewrite the frozen Backbone or M1 Profile content. M3/M6 scope remains independent.

## D-021 · Fix package traceability/status/path findings in M5 candidate d672914

- **Recorded:** 2026-10-01 by `tpw-night-driver` after applying the bounded F1–F4 fixes to the fixed M5 package.
- **Fixed candidate:** commit `d672914ac80eeed0aa5f04a0c80f448acc9de6f3`, tree `c88b662421bc44270fdf38bf43267010fe0a1d38`.
- **Disposition:** Methods README now distinguishes exact M4 accepted source hashes from current M5 packaged method hashes; Charter examples cite both. Root README clarifies M1-era candidate-status wording; Backbone provenance note includes the two cited history paths; example Profile paths are relative to the package root. No normative method body, Profile bytes, or Backbone export bytes changed.
- **Recheck:** The same independent Flash reviewer has fixed prompt `M5-PACKAGE-REPAIR-PROMPT.md` (SHA-256 `33602146bd1899d833b0d3238ddc363b3ee6b93e2d08680b213dcd8f5d620a18`) and is working only on F1–F4 against this commit. Until its result and the M3 dependency are closed, M5 is not accepted and no Pro audit is sent.
- **Scope:** This is a metadata/source-trace/path repair candidate, not method-body reassessment, M3 acceptance, M6 qualification, or publication authority.
