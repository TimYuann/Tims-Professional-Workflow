# TPW Pro2 fixed affected-claim packet
Product 8ba69427105d09b3efa1d3a5f28182d4243b5fea
Root tree 2e69f1759960ac6a5832012dba602b10f2dd2b61
Core d0cbbfc8b56f588c183efdf8b6d503d9131b5f58
Meta 7357f0b178d0b314c4276e7a213afb81a46f1d79

# Exact diff from Pro1
```diff
diff --git a/professional-workflow/methods/external-tool-operation.md b/professional-workflow/methods/external-tool-operation.md
index 38ccf03..2204e3e 100644
--- a/professional-workflow/methods/external-tool-operation.md
+++ b/professional-workflow/methods/external-tool-operation.md
@@ -1,6 +1,6 @@
 # External tool operation · candidate method body
 
-- **Status:** candidate distilled under `ORACLE-REVIEW-A4-THIRD-PARTY` and extended under `REVIEW-GATE2-A4-CURSOR-DEF2` (H08/H09, 2026-10-02); not yet an accepted reference; creates no authority, trigger, or gate. A fixed-diff review still applies.
+- **Status:** candidate distilled under `ORACLE-REVIEW-A4-THIRD-PARTY`, extended under `REVIEW-GATE2-A4-CURSOR-DEF2` (H08/H09) and revised under `docs/absorption/2026-10-02/PRO1-DISPOSITION.md` (TPW-PRO1-002, 2026-10-03); not yet an accepted reference; creates no authority, trigger, or gate. A fixed-diff review still applies.
 - **Method owner when bound:** A/B/D/E/F bind this entry by the judgment the task is missing — A for why the work exists, B for the visible contract, D for the shared design, E for execution, F for evidence. The method supplies the operation sequence; it creates no action authority, does not replace a provider's own policy, and does not restate the pointer methods below.
 
 ## Use
@@ -31,8 +31,8 @@ This file states only the external-operation sequence and repeats none of their
 
 9. Execute in bounded units: small pages unless more was asked, only the fields and expansions actually used, and an explicit stop condition for pagination.
 10. Preserve partial success: a response may carry usable data together with per-item errors; keep both instead of collapsing the call into pass/fail, and do not discard successful items because one item failed.
-11. Distinguish outcomes: completed, pending/still-in-review, refused/blocked, unconfirmed/unknown, and transient failure. An unknown outcome is neither failure nor success; do not blindly resend. A legitimate retry reuses the same operation identity so the provider does not duplicate the effect.
-12. After a transient failure or outage, back off and retry within the task's authorization; do not retry a refusal, an unconfirmed result, or a missing-capability condition unchanged.
+11. Distinguish outcomes: completed, pending/still-in-review, refused/blocked, unconfirmed/unknown, and transient failure. An unknown outcome is neither failure nor success: a blind repetition without a confirmed stage semantic or an idempotency guarantee is not recovery.
+12. A legal recovery is narrower and has to be explicit, and its conditions differ by whether the step can re-apply the effect. A same-request replay, or any recovery that could re-apply the effect, needs the existing authorization, the same intent with the same key and payload, a retention window that still covers the re-delivery path, and a service guarantee that the repeated effect cannot apply twice; when only the response was lost after the effect applied, that replay returns the earlier result instead of acting again. A read-only status query by the original operation identity does not re-apply the effect: it proceeds under its own actual capability, object identity, and permission, cost, and data boundaries, and an expired write key or a write that cannot be safely replayed does not by itself forbid the query — with an unknown outcome, the query may be the evidence that distinguishes the states. Any side-effectful reconciliation or compensation still needs its own real stage semantics, guarantee, and valid authorization, and never uses a query's name to resend or to change the key, amount, or target. The replay still does not happen when a service explicitly says not to resend, when the guarantee is unknown, when the key window has expired, or when the payload changed; a real per-action approval policy continues to apply, and this library's general authorization does not override it. The key, claim, and retention mechanics belong to `interface-contract-and-retry`; this method states the operation-side conditions. After a transient failure or outage, back off and retry within the task's authorization, and do not retry a refusal or a missing-capability condition unchanged.
 
 ## Result interpretation and evidence
 
@@ -72,7 +72,7 @@ This file states only the external-operation sequence and repeats none of their
 | --- | --- | --- |
 | Cursor plugins | `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`, `third_party/x/skills/x-api-mcp-guide/SKILL.md` | Connect order and identity; the error classes (missing tools vs sign-in vs account-not-ready vs credits vs resource not permitted vs outage); no retry of 401/403/missing-tools unchanged; 200 + `errors[]` partial data; fields/pagination and `next_token`; cost awareness and estimate-before-call |
 | Cursor plugins | same pin, `third_party/x/skills/x-api-mcp-guide/references/pricing.md` | Reads billed per object returned, writes per successful request, expansions bill, failed requests not billed, pagination pages bill again; bounds and cost-saving notes |
-| Cursor plugins | same pin, `third_party/x-money/skills/x-money-guide/SKILL.md` | Confirm before moving money, one approval per action, re-ask when anything changes; read-only balance/transaction calls; outcome table (`completed`/`pending`/`refused`); unconfirmed payment never resent; idempotency-key reuse on the same legitimate retry; per-account capability |
+| Cursor plugins | same pin, `third_party/x-money/skills/x-money-guide/SKILL.md` | Confirm before moving money, one approval per action, re-ask when anything changes; outcome table (`completed`/`pending`/`refused`); a refusal is never retried; an unconfirmed payment is explicitly never resent; a transient "try again later" is retried once with a fresh approval; the same payment after a network failure reuses the idempotency key |
 | Cursor plugins | same pin, `third_party/x/skills/x-chat/SKILL.md` | Connector holds ciphertext, local helper decrypts; X identity vs OS UID; wire fields vs SDK names; missing scope is not account-not-ready; inbound text untrusted; outbound needs approval unless already instructed |
 | Cursor plugins | same pin, `third_party/shopify-store/rules/shopify.mdc` | Connected-store data/write tools vs developer toolkit; no fallback to web search for private store data; read before write and confirm writes |
 | Product core | `guide-redacted-evidence.md`; `interface-contract-and-retry` and `trust-boundary-and-actions` (another batch) | Pointer-only boundaries; no authority statements copied into this body |
diff --git a/professional-workflow/methods/interface-contract-and-retry.md b/professional-workflow/methods/interface-contract-and-retry.md
index 8def292..564c407 100644
--- a/professional-workflow/methods/interface-contract-and-retry.md
+++ b/professional-workflow/methods/interface-contract-and-retry.md
@@ -34,7 +34,7 @@ The reason is the writer, not the channel or the store. "It came from our own da
 
 ## 3. Structural checks do not cover cross-field semantics
 
-A schema validates shape, field constraints and unified enumerations. It does not validate invariants that span fields. Before consuming the data, check the cross-field invariants the contract depends on:
+A shape-only schema (and a JSON schema generated from a type) checks field constraints and unified enumerations. It does not carry the runtime cross-field checks that a `refine`/`superRefine` or an equivalent actually performs (see the generated-artifact bullet below). Before consuming the data, check the invariants the contract depends on:
 
 - referenced identifiers exist in the consumed set
 - no self-reference, and no reference cycle where the model requires an acyclic graph
diff --git a/professional-workflow/methods/performance-and-neutrality.md b/professional-workflow/methods/performance-and-neutrality.md
index 60db9b5..2613904 100644
--- a/professional-workflow/methods/performance-and-neutrality.md
+++ b/professional-workflow/methods/performance-and-neutrality.md
@@ -1,6 +1,6 @@
 # Performance investigation and neutrality · candidate method body
 
-- **Status:** candidate distilled under `docs/absorption/2026-10-02/reviews/ORACLE-REVIEW-A1-ADDY-CD.md` (C9, 2026-10-02, source `addy@2686b620`), extended under `docs/absorption/2026-10-02/reviews/REVIEW-GATE2-A2R-CURSOR-ABC8.md` (MG1/MG2, 2026-10-02, source Cursor `ecc249f1`), and further extended under `docs/absorption/2026-10-02/reviews/REVIEW-GATE2-A1-ADDY-EF-ADDENDUM.md` (P1–P9 performance/cache/query/pool branches, 2026-10-02, source `addy@2686b620`); not yet an accepted reference; creates no authority, trigger, or gate. A fixed-diff review still applies. This file is the single carrier for performance evidence; no second perf-evidence file or registry is created.
+- **Status:** candidate distilled under `docs/absorption/2026-10-02/reviews/ORACLE-REVIEW-A1-ADDY-CD.md` (C9, 2026-10-02, source `addy@2686b620`), extended under `docs/absorption/2026-10-02/reviews/REVIEW-GATE2-A2R-CURSOR-ABC8.md` (MG1/MG2, 2026-10-02, source Cursor `ecc249f1`), and further extended under `docs/absorption/2026-10-02/reviews/REVIEW-GATE2-A1-ADDY-EF-ADDENDUM.md` (P1–P9 performance/cache/query/pool branches, 2026-10-02, source `addy@2686b620`); revised under `docs/absorption/2026-10-02/PRO1-DISPOSITION.md` (TPW-PRO1-003: effect estimate, sample spread and actual value separated); not yet an accepted reference; creates no authority, trigger, or gate. A fixed-diff review still applies. This file is the single carrier for performance evidence; no second perf-evidence file or registry is created.
 - **Method owner when bound:** D/E run the investigation and the change; F evaluates a performance claim against its baseline with the actual measurement conditions. This method does not set a target the task does not have.
 
 ## Use
@@ -92,18 +92,23 @@ Route by what the change actually affects or would change: domain meaning, a sha
 - **Re-measure the way the baseline was measured** — same command, same data, same environment, same budget. A cold-cache baseline compared with a warm-cache result measures the cache, not the change.
 - **One attempt, one explainable hypothesis.** Say what the change is expected to move and by what mechanism before running it. A speculative probe is allowed when the mechanism is not yet known, but label it a probe and do not credit it as an explained win.
 - **Change one thing at a time.** Several optimizations landed together produce one number and no attribution. If they must ship together, measure each in isolation first; if they genuinely cannot be separated, state that attribution limit instead of crediting the combined number to each change. Do not stack untested tweaks and attribute the total to every item.
-- **Beat run-to-run variance, not just the mean.** Repeat the measurement and compare the delta to the observed spread. A 3% gain inside a ±5% spread is a different sample, not a gain.
+- **Separate the effect estimate from raw sample spread.** How much repetition and what design are needed follows the claim, the known noise and variation, and the coverage: a deterministic narrow count under a fixed input can be supported by a single run, while a claim that estimates noise or a stable benefit needs appropriate repetition. The uncertainty of the *effect* estimate depends on sample size, pairing and correlation, comparability and confounding — not on the raw overlap of two distributions. Heavily overlapping distributions can still support a precise enough estimate of the mean difference, and a mean that looks improved can come from too little sampling, incomparable conditions or a material confounder. A "3% gain inside a ±5% band" is therefore not by itself a verdict in either direction: two bare numbers cannot decide whether the improvement is established, unestablished or absent. That depends on the effect estimate and its uncertainty under the measurement design and on what the claim needs. Design the measurement for the claim; this method fixes no t-test, bootstrap, interval or N.
+
+Conditional shapes, to make the distinction concrete:
+- **Raw distributions overlap, estimate usable.** Two independent, comparable groups of 1000 runs with means 100 ms and 97 ms and standard deviation 5 ms give a standard error of the difference of about 0.224 ms (5 × √(2/1000)); the distributions overlap heavily and the 3 ms mean effect is still estimated precisely enough to support that claim under those conditions. This is a worked hypothetical for the arithmetic — not a benchmark, and not a required sample size.
+- **Mean moved, estimate not established.** Fewer or unmatched samples, an incomparable environment, or a material confounder (another change in the same window, a warmed cache, a different workload) can move the mean while leaving the effect unestablished. That calls for more or better evidence, not for claiming the win.
 
 Decision table:
 
 | Result versus baseline | Action |
 | --- | --- |
-| past the stated threshold and correctness checks green | **keep**, with the before/after numbers recorded |
-| within run-to-run noise (no measurable change) | **revert** — "neutral" is a revert, not a keep |
-| worse | **revert** |
+| a usable effect estimate past the stated benefit threshold and correctness checks green | **keep**, with the before/after numbers recorded |
+| no usable effect estimate for the claim (too imprecise, incomparable, or materially confounded) | the improvement is **not established**: continue, defer or revert per the existing budget and purpose — not a product FAIL |
+| a usable estimate shows no benefit worth keeping (below the accepted benefit threshold, or not worth the maintenance cost) | **revert or defer** — a supported neutral result is a revert, not a keep |
+| a usable estimate shows the change is worse | **revert** |
 | improved but a correctness check went red | **revert** — a regression wearing a win's clothing |
 
-A result inside the noise band is **not a product FAIL**. It is an unproven performance improvement, and (absent another accepted purpose) the change reverts rather than accumulating maintenance cost for nothing.
+An imprecise or inconclusive result is **not a product FAIL**: the improvement is simply not established, and what to do next — continue with a better measurement design, defer, or revert — follows the existing budget and purpose. A supported no-benefit result reverts rather than accumulating maintenance cost for nothing. A change that also serves an accepted reliability or correctness purpose is evaluated by that purpose; a performance-neutral result does not veto it.
 
 A comparison that measures the **wrong surface**, or comes out **inconclusive**, is not a PASS either. An inconclusive run does not confirm the fix, and a green result on a surface other than the claimed one does not establish the claim. A previously valid observation may be reused while its conditions still hold; an untested ceiling cannot be claimed as the limit.
 
@@ -115,7 +120,7 @@ Reverted work leaves no trace in version history, which is exactly why the same
 
 | Idea | Baseline → result | Verdict | Why |
 | --- | --- | --- | --- |
-| memoize the row component | INP 240 ms → 235 ms | reverted | inside noise (±15 ms); rows were not the bottleneck |
+| memoize the row component | INP 240 ms → 235 ms | reverted | the 5 ms difference is below the accepted benefit threshold for this claim; the trace pointed at the list rows, not the memoized component |
 | virtualize the list | INP 240 ms → 90 ms | kept | long tasks gone from the trace |
 | preconnect to the API origin | LCP 2.8 s → 2.8 s | reverted | already same-origin |
 
@@ -123,7 +128,7 @@ A section in the change description or a trail the repository already keeps both
 
 ## Complexity must pay for itself — without vetoing other purposes
 
-Code that is kept is maintained forever. When a change adds complexity solely for performance and produces no significant measured benefit, **revert or defer it**. But if the same change also serves an already-accepted reliability or correctness purpose, evaluate it by that purpose: a neutral performance measurement does not by itself veto it. State which purpose is being claimed, and remember that a green test result certifies the checks that ran, not every commitment the change retained.
+Code that is kept is maintained forever. When a change adds complexity solely for performance and produces no established benefit worth keeping, **revert or defer it**. But if the same change also serves an already-accepted reliability or correctness purpose, evaluate it by that purpose: a neutral performance measurement does not by itself veto it. State which purpose is being claimed, and remember that a green test result certifies the checks that ran, not every commitment the change retained.
 
 ## When to stop
 
@@ -154,9 +159,9 @@ The engineering conclusion is the boundary, not the trick: **do not remove `Cach
 
 | Source | Retained contribution |
 | --- | --- |
-| Addy Osmani, `addyosmani-agent-skills` at `2686b620fc1fed2e8f60c704839c766b8594c6b6`, `skills/performance-optimization/SKILL.md` (`Overview`, `The Optimization Workflow` steps 1–5, `Where to Start Measuring`, `Step 2: Identify the Bottleneck`, `Step 3` anti-patterns, `Step 4: Verify`, `Log every attempt`, `Step 5: Guard Against Regression`, `Common Rationalizations`, `Red Flags`) | Measure before optimizing; symptom decomposition; synthetic vs field evidence; the common bottlenecks with their deciding measurements; same-condition re-measurement, one change at a time, beat the noise; the four-way keep/revert decision including "neutral is a revert"; correctness gating the metric; the attempt ledger; guarding the user-facing metric. |
+| Addy Osmani, `addyosmani-agent-skills` at `2686b620fc1fed2e8f60c704839c766b8594c6b6`, `skills/performance-optimization/SKILL.md` (`Overview`, `The Optimization Workflow` steps 1–5, `Where to Start Measuring`, `Step 2: Identify the Bottleneck`, `Step 3` anti-patterns, `Step 4: Verify`, `Log every attempt`, `Step 5: Guard Against Regression`, `Common Rationalizations`, `Red Flags`) | Measure before optimizing; symptom decomposition; synthetic vs field evidence; the common bottlenecks with their deciding measurements; same-condition re-measurement, one change at a time, separating the effect estimate from raw sample spread; the decision table including the not-established case; correctness gating the metric; the attempt ledger; guarding the user-facing metric. |
 | Same pin, `references/performance-checklist.md` (`Connection pooling`, `Query plans`, `Index strategy`, `Caching Strategies` incl. read/write patterns, negative caching, request coalescing and the cache checklist, `Frontend Checklist`) | Pool capacity across all competing consumers and headroom, diagnosis before resizing, bounded wait/timeouts, unbounded autoscaling and proxy caveat; index-change plan reading with baseline plan, estimate/sort signals, composite-order and write-cost conditions, and non-automatic revert; cache selection evidence, key equivalence classes, invalidation/staleness ownership, negative results versus origin errors, in-flight coalescing with lock/stale-while-revalidate caveats, memory ceiling and hit-rate nuance; layout reservation via dimensions and fallback font metrics verified at the real viewport. The `no-store`/bfcache item remains a version-limited example corrected against the vendor documentation above. |
 | Chrome for Developers, `https://developer.chrome.com/docs/web-platform/bfcache-ccns` (published 2024-10-21, updated 2025-09-09) | The actual Chrome bfcache/no-store behavior, its conditions, the enterprise opt-out, and the explicit note that other browsers may still block these pages and that minimizing `no-store` remains best practice. |
 | Cursor plugins, `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`, `pstack/skills/poteto-mode/playbooks/hillclimb.md` and `pstack/skills/poteto-mode/playbooks/perf-issue.md` | Harness sensitivity proven before it is trusted; workload/architecture grounding and a reproducing case; falsifiable target and stop condition from the real authority; repeat under controlled conditions with warmup/cache/order/sample/noise and a negative control; one explainable hypothesis per change; kept/reverted/deferred records that reuse the existing trail; the eight strategy families as mechanism-grounded optional hypotheses with per-family win conditions; a trace shows what is slow, never what is safe to delete. |
 
-Narrowed from the sources: the fixed metric/budget values, "always use both synthetic and RUM", "the plan not changing means the index is worthless", and the unconditional list of things that must never be cached; the hillclimb attempt/improvement floors, fixed N-median requirement, per-fix commit and freeze-never-change rules; and any requirement to run a profiler or capture before proposing a labelled hypothesis. The Cursor playbooks are not ported as scripts or runtime; only the measurement discipline above is retained.
+Narrowed from the sources: the fixed metric/budget values, "always use both synthetic and RUM", "the plan not changing means the index is worthless", and the unconditional list of things that must never be cached; the hillclimb attempt/improvement floors, fixed N-median requirement, per-fix commit and freeze-never-change rules; and any requirement to run a profiler or capture before proposing a labelled hypothesis. Treating a raw ± spread as a verdict of no benefit is likewise not adopted (TPW-PRO1-003): an unusable estimate leaves the improvement unestablished instead of failing the product, and a usable estimate is weighed against the accepted benefit threshold, maintenance cost and other purposes. The Cursor playbooks are not ported as scripts or runtime; only the measurement discipline above is retained.
diff --git a/professional-workflow/methods/release-and-recovery.md b/professional-workflow/methods/release-and-recovery.md
index 22b60b6..73902e5 100644
--- a/professional-workflow/methods/release-and-recovery.md
+++ b/professional-workflow/methods/release-and-recovery.md
@@ -1,6 +1,6 @@
 # Release and recovery · candidate method body
 
-- **Status:** candidate distilled under `docs/absorption/2026-10-02/reviews/ORACLE-REVIEW-A1-ADDY-CD.md` (C4, 2026-10-02, source `addy@2686b620`) and further extended under `docs/absorption/2026-10-02/reviews/REVIEW-GATE2-A4-CURSOR-DEF.md` (G05 gate-status counterexample, G04 gate-answer semantics, 2026-10-02, source Cursor `ecc249f1`); not yet an accepted reference; creates no authority, trigger, or gate. A fixed-diff review still applies.
+- **Status:** candidate distilled under `docs/absorption/2026-10-02/reviews/ORACLE-REVIEW-A1-ADDY-CD.md` (C4, 2026-10-02, source `addy@2686b620`) and further extended under `docs/absorption/2026-10-02/reviews/REVIEW-GATE2-A4-CURSOR-DEF.md` (G05 gate-status counterexample, G04 gate-answer semantics, 2026-10-02, source Cursor `ecc249f1`); revised under `docs/absorption/2026-10-02/PRO1-DISPOSITION.md` (TPW-PRO1-001: observed usability separated from the acceptance act); not yet an accepted reference; creates no authority, trigger, or gate. A fixed-diff review still applies.
 - **Method owner when bound:** D/E plan the change, its rollout and its recovery path; the go/no-go decision, risk acceptance and any external communication stay with the authority that actually owns them.
 
 ## Use
@@ -11,10 +11,16 @@ Four different things are often called "release". Keep them separate, because cl
 
 - **deployed** — the artifact is present in the target environment
 - **enabled** — the feature is active for someone (flag on, route serving, job scheduled)
-- **accepted** — the intended user path actually works and is observed to work
+- **observed / verified usable** — the intended user path has been observed (or otherwise verified) to work for a definite object and version within a stated boundary: which path, when, under what conditions, and with what evidence — or the honest gap
 - **shut down** — the old path is removed and the temporary machinery (flag, dual path, migration task) is gone
 
-**Deployed is not enabled, and enabled is not usable.** A deployment that reports success while the user path fails is a deployment, not a release.
+**Deployed is not enabled, and enabled is not observed usable.** A deployment that reports success while the user path fails is a deployment, not a usable release.
+
+**Acceptance is an act, not an observation.** The responsible party — a role, or an existing valid rule that already covers the object — accepts a definite object and version, and the record names who or which rule accepted it, when, and under what scope or conditions. An observed or verified usable path is evidence for that decision; it is not the decision, and an F PASS does not produce acceptance. Do not route every acceptance to a human by default: an existing valid delegation can accept within its own boundary, and the record then names that rule.
+
+Record the two separately — `observed` (object/version, path, time and conditions, evidence or gap) and `accepted` (object/version, acceptor or rule, time, scope) — because they have different truth conditions and different owners. Collapsing them either blocks a working release on an unrecorded decision or treats authority as proof that the implementation works. Two cases show why:
+- the observed path passes (the canary is stable and the critical flow was exercised) but the authorized acceptance for this object has not happened: observed, not yet accepted;
+- the behaviour contract is accepted (for example by B/C) but the implementation was never observed: accepted contract, unobserved implementation — acceptance of the design is not evidence that the built version works.
 
 ## Preconditions
 
@@ -62,7 +68,7 @@ The error budget is a policy signal, not a negotiation: what action follows when
 
 ## Observation after enablement
 
-The first hour after enabling is when "deployed" is tested against "usable". The source's checks are a usable starting set: the health check returns successfully, error monitoring shows no new error class, latency shows no regression, the **critical user flow is exercised by hand**, logs are flowing and readable, and the rollback mechanism is confirmed ready (a dry run where possible). These are observation steps, not a universal gate; the actual set follows the change's critical path.
+The first hour after enabling is when "deployed" is tested against "observed usable". The source's checks are a usable starting set: the health check returns successfully, error monitoring shows no new error class, latency shows no regression, the **critical user flow is exercised by hand**, logs are flowing and readable, and the rollback mechanism is confirmed ready (a dry run where possible). These are observation steps, not a universal gate; the actual set follows the change's critical path.
 
 ## Recovery and data
 
@@ -81,7 +87,7 @@ The first hour after enabling is when "deployed" is tested against "usable". The
 
 | Source | Retained contribution |
 | --- | --- |
-| Addy Osmani, `addyosmani-agent-skills` at `2686b620fc1fed2e8f60c704839c766b8594c6b6`, `skills/shipping-and-launch/SKILL.md` (`Feature Flag Strategy`, `Staged Rollout`, `Rollout Decision Thresholds`, `When to Roll Back`, `Monitoring and Observability`, `Post-Launch Verification`, `Error Budget Release Gate`, `Rollback Strategy`, `Red Flags`) | Deployment/enablement/acceptance/shutdown distinction; flag owner, expiry, no nesting, both states tested; advance/hold/rollback relative to a baseline; burn rate as a hold signal even when individual thresholds pass; the four-part rollback plan with a time magnitude; data reversibility; first-hour verification including the critical user flow; error-budget policy as an owner decision. |
+| Addy Osmani, `addyosmani-agent-skills` at `2686b620fc1fed2e8f60c704839c766b8594c6b6`, `skills/shipping-and-launch/SKILL.md` (`Feature Flag Strategy`, `Staged Rollout`, `Rollout Decision Thresholds`, `When to Roll Back`, `Monitoring and Observability`, `Post-Launch Verification`, `Error Budget Release Gate`, `Rollback Strategy`, `Red Flags`) | Deployment/enablement/observed-usability/shutdown distinction, with acceptance as a separate act by an authorized party or existing rule; flag owner, expiry, no nesting, both states tested; advance/hold/rollback relative to a baseline; burn rate as a hold signal even when individual thresholds pass; the four-part rollback plan with a time magnitude; data reversibility; first-hour verification including the critical user flow; error-budget policy as an owner decision. |
 | Same pin, same file (`The Pre-Launch Checklist`, `Common Rationalizations`) | The deployed-is-not-usable mechanism. The full pre-launch checklist (code quality, security, performance, accessibility, infrastructure, documentation) is not adopted as a universal gate; its applicable parts follow the actual change and the accepted quality policy. |
 | Cursor plugins, `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`, `pstack/skills/poteto-mode/scripts/watch-pr/policy.ts` (`resolveChecks` / gate status rollup) | A gate or status field is not release permission: null/pending/`UNKNOWN` is not clear, review-required is not an allow, "not FAILURE" is not a pass, structural fields do not satisfy the required policy, prior CI green or automated approval is not risk acceptance, `READY` is neither merged nor released, and a default "(no answer) = accepted risk" field is not a decision. The watcher/rules are not ported. |
 
diff --git a/professional-workflow/methods/trust-boundary-and-actions.md b/professional-workflow/methods/trust-boundary-and-actions.md
index 6c5d88a..38cd829 100644
--- a/professional-workflow/methods/trust-boundary-and-actions.md
+++ b/professional-workflow/methods/trust-boundary-and-actions.md
@@ -157,7 +157,7 @@ The legal basis and the specific obligations come from the applicable policy and
 ## Limits
 
 - No universal control list, no mandatory header set, no fixed numeric threshold, no security gate. Controls follow the boundaries and assets of the actual feature.
-- The dependency-upgrade review path (upgrade choice, coverage, lockfile handling) is a separate on-demand guide in the integrated method set; this method states the security-side gate and does not duplicate that procedure.
+- Dependency-upgrade choices, coverage and lockfile handling are review concerns: apply `change-review.md` (dependencies and critical assumptions, findings and disposition) together with this file's dependency-install boundary above. This method does not duplicate that procedure.
 - Action permission comes from the task's valid authority and Charter. Naming a boundary or writing a checklist is not approval to act. This method does not grant creating operator flag files, adding credentials, sending to external channels, or lifting an existing restriction; those are actions for the authority that owns them.
 - An operator-identity mechanism is host-specific. If a real deployment adopts one, verify the host isolation and the trusted-configuration maintenance rights rather than copying the source's file convention.
 - The examples distinguish real observed behaviour (for example, a browser/manager documented behaviour), locally reproduced evidence, and code illustration. A code snippet in a source is not evidence that the same control works in the reader's stack.
@@ -168,7 +168,7 @@ The legal basis and the specific obligations come from the applicable policy and
 | --- | --- |
 | Addy Osmani, `addyosmani-agent-skills` at `2686b620fc1fed2e8f60c704839c766b8594c6b6`, `skills/security-and-hardening/SKILL.md` (`Process: Threat Model First`, `The Three-Tier Boundary System`, `Hardening Controls`, `Dependencies and supply chain`, `Personal data and privacy`, `AI / LLM features`, `Red Flags`) | Trust follows the writer (including local process values); STRIDE as a lens plus abuse cases; the Always / Ask First / Never classes; dependency boundary, install-script gate, audit-vs-trust and reachability triage; privacy as minimization/purpose/retention/deletion; model output untrusted and the system prompt not a security boundary. |
 | Same pin, `skills/security-and-hardening/references/hardening-patterns.md` (`Server-Side Request Forgery (SSRF)`, `Destructive Operations on Derived Paths`, `Dependency Audit Triage`) | SSRF allowlist + all-records + no-redirect with the DNS-rebinding TOCTOU stated honestly; destructive-path three conjunctive conditions and the self-attestation / check-use limits; the audit triage tree. |
-| Cursor plugins, `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`, `orchestrate/skills/orchestrate/scripts/cli/util.ts` (operator/target boundary), `scripts/cli/task.ts` (run/cancel entry points), `models.ts` (probe path), `scripts/__tests__/operator-boundary.test.ts` | Worker-controlled argv/env/cwd and non-trusted workspace; the operator-flag convention with its honest weakness (OS userInfo home, non-symlink uid/`0600`; same-UID home writes break it); target resolution from trusted configuration and fail-early half-configuration; per-structure encoding; probe-accepted ≠ model-completed, cancel-error-swallowed ≠ cancelled; green boundary tests ≠ complete identity security. Runtime scripts are not ported. |
+| Cursor plugins, `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`, `orchestrate/skills/orchestrate/scripts/cli/util.ts` (operator/target boundary), `scripts/cli/task.ts` (run/cancel entry points), `scripts/tools/probe-models.ts` (probe path), `scripts/__tests__/operator-boundary.test.ts` | Worker-controlled argv/env/cwd and non-trusted workspace; the operator-flag convention with its honest weakness (OS userInfo home, non-symlink uid/`0600`; same-UID home writes break it); target resolution from trusted configuration and fail-early half-configuration; per-structure encoding; probe-accepted ≠ model-completed, cancel-error-swallowed ≠ cancelled; green boundary tests ≠ complete identity security. Runtime scripts are not ported. |
 | Same pin, `orchestrate/skills/orchestrate/scripts/core/andon.ts` (pause scope, cached ref read-back, state clear), `scripts/core/redact-body.ts` (clue-based detection, length reason), `scripts/cli/comments.ts` (optional allowed thread), `pstack/skills/poteto-mode/scripts/worktree-audit.sh` and `playbooks/worktree-cleanup.md` (inventory buckets, human-gated deletion, read-only claim versus effects, non-exhaustive filters), `cursor-sdk/skills/cursor-sdk/references/error-handling.md` (two failure axes, retryable claim, unknown outcome) | Stop/pause state shape ≠ authority, stop surface scoped to new work, cached read-back needs identity/version/authorized writer, wrong/unknown state not cleared for convenience; channel authorization at enqueue and delivery, optional thread allowlist is that helper's boundary, dedup ≠ exactly-once, unknown delivery not resent; redaction patterns are clues, length is not truncation, custody allowlist required; cleanup inventory versus suggestion, PR/ancestor/scratch heuristics are not proof, declared effects over a read-only name; SDK failure axes separated, retryable is a claim, disposal ≠ remote termination. No Slack message, cleanup run, SDK call or runtime operation is authorized or ported. |
 | Same pin, `cursor-sdk/skills/cursor-sdk/references/streaming.md`, `auth.md`, `mcp.md` (config/transport/resume/events), `pstack/automations/benny/skills/triage-issue-reports/SKILL.md` and `pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md` | Agent vs run, event vs terminal state, configuration source vs effective configuration, observation vs execution failure; resume persist/reload boundary and a later send not changing an in-flight run; stream display is not the terminal result and a finished status is not artifact qualification; backpressure per client; disposal/cancel-accepted limits; key form is not identity and each configuration source has its own boundary; command location, secret destination and readers for stdio/HTTP; MCP registration, `settingSources` and resume carrying no account permission or persistence promise; frozen trigger coordinates, write-time parent/recipient/permission re-check, no root or alternate fallback, marker qualifies trigger data only, before/after checks are not a transaction; least privilege via real isolation, prompt prohibition is not removed credentials, insufficient isolation shrinks to the existing single executor. No SDK client, bot, external-write boundary or external write is created or authorized. |
 

```

---
# Fixed revised file: 8ba69427105d09b3efa1d3a5f28182d4243b5fea:professional-workflow/methods/external-tool-operation.md
SHA256 a411a4ca165ec22a722a403ddd9d2a6f4a4187e216e2af0ecd19267c2febca12

# External tool operation · candidate method body

- **Status:** candidate distilled under `ORACLE-REVIEW-A4-THIRD-PARTY`, extended under `REVIEW-GATE2-A4-CURSOR-DEF2` (H08/H09) and revised under `docs/absorption/2026-10-02/PRO1-DISPOSITION.md` (TPW-PRO1-002, 2026-10-03); not yet an accepted reference; creates no authority, trigger, or gate. A fixed-diff review still applies.
- **Method owner when bound:** A/B/D/E/F bind this entry by the judgment the task is missing — A for why the work exists, B for the visible contract, D for the shared design, E for execution, F for evidence. The method supplies the operation sequence; it creates no action authority, does not replace a provider's own policy, and does not restate the pointer methods below.

## Use

Use on demand when a task operates a third party or external service through a connector, MCP server, CLI, or API — especially when capability, permission, cost, or outcome interpretation is uncertain. The sequence is the method: capability and routing, permission and cost, bounded execution, result interpretation, handoff.

Ownership is split by pointer, not copied:
- `interface-contract-and-retry` (another batch) owns the request/response contract and retry mechanics.
- `trust-boundary-and-actions` (another batch) owns outbound, secret, and high-impact action authority.
- `guide-redacted-evidence` owns custody for tool output and secrets in evidence.
This file states only the external-operation sequence and repeats none of their authority statements.

## Capability and routing

1. Discover the actual capability before promising work: which connector/tool/server is present, which identity it uses, and which scopes or account gates apply. A source's guide is not evidence that the tool exists in this environment.
2. Separate the failure classes: tool missing, not authenticated, account not ready, quota/credits blocked, resource not permitted, service outage. Each has a different next step; do not infer "the whole account is broken" from one missing endpoint or one 403.
3. Route by the real data boundary: a connected account's own business data and write actions belong to that connection. Developer documentation or an SDK's capability does not imply access to a user's account or store; when the connector is absent, do not substitute public search for private data.
4. Keep the provider's own terms: a per-action approval rule the provider enforces (money movement, for example) is not bypassed by an agent's earlier general instruction. Source-specific money thresholds or every-action human policies are provider/host policy, not universal library rules — apply them because they are in force, not because this method invented them.

## Permission and cost before acting

5. Confirm the action sits inside the task's existing delegation before calling a tool that writes, sends, spends, or changes shared state; a read is not automatically safe either when it exposes private data, where `guide-redacted-evidence` custody applies.
6. Estimate cost in the provider's own billing model before a bulk or paginated job: reads may bill per object returned (expansions included), writes per successful request, and each pagination page can bill again. Parameterized estimate: `estimate = Σ_pages (objects_returned × per_object_price) + per_request_fees`; stop when the provider omits the next token.
7. Treat every price, free tier, and threshold quoted in any source as a time-specific reference, not a guarantee; re-read the provider's current authoritative pricing before quoting a cost. A saved estimate does not become a billing promise.
8. When a pagination or bulk job is involved, estimate it in the provider's billing terms, keep the scope bounded with an explicit stop condition, and track consumption as it runs. Route to the corresponding authority only when the valid authorization does not cover the work, when it would exceed the existing cost or scope boundary, or when the real provider/host policy requires approval. Work already covered by a valid authorization — a bounded set of pages with a stated budget and field range, for example — does not need an extra acknowledgement just because it loops. The authorization's cost and scope boundary is a task decision; this method sets no universal number.

## Bounded execution and partial success

9. Execute in bounded units: small pages unless more was asked, only the fields and expansions actually used, and an explicit stop condition for pagination.
10. Preserve partial success: a response may carry usable data together with per-item errors; keep both instead of collapsing the call into pass/fail, and do not discard successful items because one item failed.
11. Distinguish outcomes: completed, pending/still-in-review, refused/blocked, unconfirmed/unknown, and transient failure. An unknown outcome is neither failure nor success: a blind repetition without a confirmed stage semantic or an idempotency guarantee is not recovery.
12. A legal recovery is narrower and has to be explicit, and its conditions differ by whether the step can re-apply the effect. A same-request replay, or any recovery that could re-apply the effect, needs the existing authorization, the same intent with the same key and payload, a retention window that still covers the re-delivery path, and a service guarantee that the repeated effect cannot apply twice; when only the response was lost after the effect applied, that replay returns the earlier result instead of acting again. A read-only status query by the original operation identity does not re-apply the effect: it proceeds under its own actual capability, object identity, and permission, cost, and data boundaries, and an expired write key or a write that cannot be safely replayed does not by itself forbid the query — with an unknown outcome, the query may be the evidence that distinguishes the states. Any side-effectful reconciliation or compensation still needs its own real stage semantics, guarantee, and valid authorization, and never uses a query's name to resend or to change the key, amount, or target. The replay still does not happen when a service explicitly says not to resend, when the guarantee is unknown, when the key window has expired, or when the payload changed; a real per-action approval policy continues to apply, and this library's general authorization does not override it. The key, claim, and retention mechanics belong to `interface-contract-and-retry`; this method states the operation-side conditions. After a transient failure or outage, back off and retry within the task's authorization, and do not retry a refusal or a missing-capability condition unchanged.

## Result interpretation and evidence

13. Relay the provider's user-facing result in plain language; do not lecture on internal billing, enrollment, or token mechanics.
14. A controlled simulation — a fixture, local stand-in, or recorded response — can prove position or shape semantics; it does not prove the real provider/API is available or behaves that way. A lint or schema check is not a visual or end-to-end observation.
15. A real-host claim needs observation on the actual authorized host: the named connector, the real account, the real document or service, under the task's existing authorization. Do not obtain accounts or credentials, or send messages, merely to strengthen this knowledge, and never present a substitute green as a real-host result.
16. Record what was observed versus simulated, the provider/tool identity and version or time, the unit and range of the data, and any capability the run did not exercise.
17. Hand off tool output and secrets through `guide-redacted-evidence`, and the request/response or action-authority questions through `interface-contract-and-retry` / `trust-boundary-and-actions`; this method does not restate those rules.

## Invocation and write closure

18. Distinguish the invocation objects: an agent is not a run, an event is not the terminal state, and a configuration source is not the effective configuration. An observation failure is a third case, separate from a submission failure and from a run that started and failed; record which one happened.
19. Wait for the terminal state before treating a job as done: a stream or log line shows what was observed, not that the run finished, and a finished status does not by itself qualify the artifact or the goal. Where the client reports backpressure or a detached handle, follow that client's actual guarantee instead of assuming the display keeps up.
20. Respect each client's persistence and reload boundary: configuration that is not persisted (inline MCP parameters, for example) must be re-passed on resume, and a later send does not change an in-flight run. A resume or re-assembly restores what the platform actually persists — check it rather than assuming the original setup still applies.
21. Keep key form and identity separate: a key's shape (prefix, length) does not prove which account or identity it belongs to, and an explicit parameter and an environment variable have different trust sources. A registration, a setting source, or a resume example carries no account permission and no persistence promise.
22. For a write driven by an external trigger, either it closes or it does not happen: resolve the source and target coordinates from the frozen trusted configuration, and re-check the parent, recipient and permission at write time. On failure or uncertainty, stop without falling back to a root or backup target; a trusted marker only qualifies the trigger data — schema or configuration validity is not target authentication and is not permission to send.
23. Keep the source data and the execution delegation separate: the trigger record, the marker, and the configuration are inputs; the authorization to act comes from the task's valid delegation. A standard event or a thinking-style event does not create a logging or reasoning-record requirement.
24. For stdio or HTTP transports, establish where the command runs, where the secret goes, and who can read it; a registration, a documentation example, or a proxy claim does not authenticate the current deployment. The authority and credential side of these checks stays with `trust-boundary-and-actions`; this section keeps the operation-facing distinctions.

## Conditions and exceptions

- When the provider has no usable capability under the current authorization, report the capability gap instead of fabricating a workaround through an unrelated channel.
- A read-only call that exposes secrets or private data still follows the redacted-evidence custody.
- The provider's own approval policy and the task's delegation can each be stricter than this method; the stricter one governs.

## Limits

- No universal cost threshold, retry count, backoff schedule, tool list, or approval frequency; those come from the provider's policy and the task's delegation.
- No permission, account, credential, spend, send, or write is created here.
- Source specifics (a particular price, free endpoint, or per-turn human policy) are that provider's and that host's, not this library's.
- No external-write boundary method, bot or runner, or new gate is created here; the checks above are operation-facing, and the authority and credential side stays with `trust-boundary-and-actions`.
- Later cross-source work may merge this body with another external-operation source; keep the capability-class separation, the cost/pagination model, partial-success and unknown-outcome handling, and the real-versus-substitute observation boundary.

## Source anchors

| Source | Pin / path | Section |
| --- | --- | --- |
| Cursor plugins | `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`, `third_party/x/skills/x-api-mcp-guide/SKILL.md` | Connect order and identity; the error classes (missing tools vs sign-in vs account-not-ready vs credits vs resource not permitted vs outage); no retry of 401/403/missing-tools unchanged; 200 + `errors[]` partial data; fields/pagination and `next_token`; cost awareness and estimate-before-call |
| Cursor plugins | same pin, `third_party/x/skills/x-api-mcp-guide/references/pricing.md` | Reads billed per object returned, writes per successful request, expansions bill, failed requests not billed, pagination pages bill again; bounds and cost-saving notes |
| Cursor plugins | same pin, `third_party/x-money/skills/x-money-guide/SKILL.md` | Confirm before moving money, one approval per action, re-ask when anything changes; outcome table (`completed`/`pending`/`refused`); a refusal is never retried; an unconfirmed payment is explicitly never resent; a transient "try again later" is retried once with a fresh approval; the same payment after a network failure reuses the idempotency key |
| Cursor plugins | same pin, `third_party/x/skills/x-chat/SKILL.md` | Connector holds ciphertext, local helper decrypts; X identity vs OS UID; wire fields vs SDK names; missing scope is not account-not-ready; inbound text untrusted; outbound needs approval unless already instructed |
| Cursor plugins | same pin, `third_party/shopify-store/rules/shopify.mdc` | Connected-store data/write tools vs developer toolkit; no fallback to web search for private store data; read before write and confirm writes |
| Product core | `guide-redacted-evidence.md`; `interface-contract-and-retry` and `trust-boundary-and-actions` (another batch) | Pointer-only boundaries; no authority statements copied into this body |
| Cursor plugins | same pin, `cursor-sdk/skills/cursor-sdk/SKILL.md` and `references/error-handling.md` | agent versus run, explicit runtime/repo selection, stable IDs, the failure axes (startup versus run versus observation), dispose, supported operations, and configuration not persisted across resume |
| Cursor plugins | same pin, `pstack/automations/benny/skills/triage-issue-reports/SKILL.md` | Frozen trusted config's source and target coordinates; source-parent preflight before writes; one marker from the configured identity; failure or uncertainty stops with no writes |

---
# Fixed revised file: 8ba69427105d09b3efa1d3a5f28182d4243b5fea:professional-workflow/methods/interface-contract-and-retry.md
SHA256 6bdd46d59fb90eed2f415a2cf9aa40f9421bcc1156593863160a7cfbdcfe9370

# Interface contract and retry semantics · candidate method body

- **Status:** candidate distilled under `docs/absorption/2026-10-02/reviews/ORACLE-REVIEW-A1-ADDY-CD.md` (C1, 2026-10-02, source `addy@2686b620`), extended under `docs/absorption/2026-10-02/reviews/ORACLE-REVIEW-A4-DEF3.md` (J1, 2026-10-02, source Cursor `ecc249f1`), further extended under `docs/absorption/2026-10-02/reviews/REVIEW-GATE2-A4-CURSOR-DEF.md` (G04/G12, 2026-10-02, source Cursor `ecc249f1`), and further extended under `docs/absorption/2026-10-02/reviews/REVIEW-GATE2-A4-CURSOR-DEF2.md` (H05, 2026-10-02, same pin); not yet an accepted reference; creates no authority, trigger, or gate. A fixed-diff review still applies.
- **Method owner when bound:** B/C own business identity and error meaning; D owns the technical coordination strategy; E implements the contract and the intent record inside its delegation; F evaluates it with concurrency / differing-payload / unknown-outcome counterexamples from the actual execution path.

## Use

This method has two independently selectable parts:

- **Caller-visible contract and input verification (§1–3).** Use when an interface has consumers whose work depends on its behaviour, or when untrusted input crosses a boundary before use. A read-only list endpoint still has pagination and error contracts; a one-off import still needs structural and cross-field validation. No retry path is required to select these sections.
- **Retry and idempotency semantics (§4–9).** Use when a state-changing operation crosses a boundary and can be retried — network retry, client retry, queue re-delivery, dead-letter replay, manual re-send. An operation with no retry or duplicate-delivery path does not select these sections.

Two questions must be answered separately: what the caller can see (the contract), and what happens the second time (retry semantics). "We accept an idempotency key" is the contract; honouring it is the implementation.

## 1. Inventory the caller-visible behavior

Before reading the implementation, write down what a caller must know:

- inputs: required / optional / defaulted; what values are rejected and why; which discriminator selects each input variant, so an unknown discriminator is not silently treated as a default
- outputs: which fields are generated, which are stable across replay
- errors: what can fail, what each failure means for the caller, and whether a retry is safe or pointless
- partial updates: which fields change, and what "absent" means (do nothing vs set to null)
- list reads: page-size bounds, offset vs cursor, ordering, and what a caller sees when the underlying data changes between pages
- operation identity: exactly which parameters define "the same operation"
- dependencies: every outbound effect the operation performs (a database write, a provider call, a message publish), the order they must happen in, which of them are idempotent, and which are compensatable. A retry replays the sequence; an early effect that is not protected can repeat even when the final one is.

The contract is the thing consumers depend on. An undocumented observable behaviour (ordering, timing, error text) is a de facto contract too; that is a reason to be intentional about what is exposed, not a reason to document everything.

## 2. Validate where trust actually changes

Validation belongs where a value's trust level changes: at the system boundary where an untrusted writer's data enters, when parsing a third-party response, when loading configuration. It need not be repeated between internal functions that share an already-checked invariant.

The reason is the writer, not the channel or the store. "It came from our own database" is not itself a validation exemption: the data is only as trustworthy as the writers that can put rows there and the invariants the schema actually enforces. A shape check proves well-formedness, not authorization.

## 3. Structural checks do not cover cross-field semantics

A shape-only schema (and a JSON schema generated from a type) checks field constraints and unified enumerations. It does not carry the runtime cross-field checks that a `refine`/`superRefine` or an equivalent actually performs (see the generated-artifact bullet below). Before consuming the data, check the invariants the contract depends on:

- referenced identifiers exist in the consumed set
- no self-reference, and no reference cycle where the model requires an acyclic graph
- no duplicate names where uniqueness is an invariant
- an old-field migration is applied and written down, rather than assuming the new shape arrived

Errors should name the field path and state the executable fix, not only "invalid input".

Three errors are easy to make here:

- **Structure green, graph wrong.** Every node passes the schema, yet an edge points at a missing task, or the references form a cycle. The structural check is green and the consumer is still wrong.
- **A runtime cross-field check is not the generated artifact.** A runtime `refine`/`superRefine` on the Plan type (duplicate names, references, cycles) is not carried into a generated JSON-schema artifact. Generating both from one source reduces maintenance drift, but the generated schema is not equivalent to all runtime semantics; a freshly generated artifact is not proof that the graph checks survived. State which layer protects which invariant.
- **A source tree with a graph is not a generated view with a graph.** A filter can drop rows so unrelated corruption does not hide other observations. That is an availability measure, not a safety proof: a partial view cannot support "all subtasks were terminated" or "the task graph is complete", and it does not approve a dangerous action.

Related conditions:

- Strict rejection of unknown fields fits a closed input protocol. An extensible protocol may explicitly retain unknown fields; `.strict()` is a choice, not a universal interface discipline.
- A regex constrains the shape of a name. It does not establish path containment or authorization.
- A `verifies`-style relation pointing at an existing, non-self task proves a graph relation only. It does not prove the evaluator is independent, the scope is correct, or the contract was accepted.
- A fault-tolerant traversal must disclose what it skipped or could not read. The skipped range is part of the result.

**Types are not permissions or runtime invariants.** Discriminated-union variants, semantic primitives and brands, total functions, a real parse at the boundary, exhaustive handling of a new variant and deriving a shape from the authoritative source all remove whole error classes. They do not establish permission, write trust or temporal validity: a branded identifier is still a string underneath, and shared state, the database, asynchronous ordering, mutable objects and expired permissions still need invariants checked at the point of use. Rejecting every runtime guard because the types are trusted, and rejecting every legal cast or interop that carries a real guarantee, are both failures; `any`, optional fields and guard-then-reject are not the only patterns.

**Language-level type features are on-demand examples, not a policy.** A `satisfies` check, narrowing `unknown` to a validated value, a total function or a semantic primitive can document and enforce a boundary where they fit; they are techniques to choose, not a mandate to adopt a schema system in every project. A non-null assertion on an environment variable (`process.env.KEY!`) is a compile-time claim, not runtime validation — a comment that it "fails loudly" does not perform the check. Legal casts and interop with a real guarantee remain usable: do not blanket-ban `as` or non-null, and do not reject every added `if` as unnecessary.

## 4. Derive the key from the intent, not the attempt

The operation identity must be stable across retries of one intent and different across distinct intents. The key comes from the client or from the initiating event — never from the layer doing the retrying.

- Wrong: a fresh key generated inside the retry loop — every retry is a new operation.
- Wrong: a value that can legitimately repeat (`${userId}:${amount}`) — two legitimate charges collapse into one.
- Wrong: a timestamp used as identity — it is a per-attempt random value wearing a hat.
- Valid: the initiator generates one plain UUID per intent and reuses it on retry; or the key is derived from an immutable identifier (`charge:v1:${orderId}`). The UUID is not the problem; regenerating it per attempt is.

Business deduplication and idempotent-attempt deduplication are different problems. "This customer must not be charged twice for this order" is a business identity decision (B/C); "the same request must not be applied twice" is the retry mechanism described here. Conflating them produces either double charges or collapsed legitimate repeats.

## 5. Claim atomically

Claiming the key and storing the initial state must be one indivisible operation. A read followed by a write is a race: two concurrent retries both read "not seen" and both act.

One mechanism is a unique constraint that picks the winner (the source's example). It is an example, not a requirement that the store be SQL — a conditional write / set-if-absent with a documented atomicity scope is equivalent only if it actually guarantees the claim. If the store cannot claim atomically, the key does not protect this operation, and that is a design fact to report rather than hide behind the key.

**Single writer, and what a publish pattern proves.** Prefer one canonical writer per output, with derived views naming their original owner; a new file format or generator is not required for every status. A single-file publish pattern — create an exclusive temporary file in the same directory and rename it into place — is a publish strategy, not a durability guarantee: it does not equal an fsync or crash durability, a multi-file transaction, or the absence of lost updates. A `write-if-missing` that checks and then writes needs a real concurrency precondition, and the name being idempotent is not proof.

**Locks are claims with named guarantees.** A PID-based lock must state its local namespace, permissions, liveness and PID-reuse rules plus the check/unlink race; `--force` is a technical option, not authorization to take another holder's lock; confirming that a PID is gone is not a full epoch or fencing guarantee. A lock cannot be replaced by convention, and this method does not create one. A missing ledger record means unverified: do not treat a new head as a reset for old claims, or map status modes mechanically. A key needs the real repository/store namespace, the object, the claim and its coverage.

## 6. Bind the payload to the key

Store a hash (or the operation-defining parameters) with the claim and compare on every replay. The same key with a different body is a caller bug and must fail loudly rather than returning the first response to a different request. Omitting this turns a typo into silent data loss.

## 7. Make the in-flight duplicate an explicit choice

The first request is still running when the second arrives — the normal case under a retry storm. Pick one and write down why:

| Strategy | Response | Use when |
| --- | --- | --- |
| Reject | conflict (e.g. 409) | the caller can retry later; simplest and safest |
| Wait | block for the result, bounded | the caller needs it synchronously |
| Return pending | acceptance (e.g. 202) + status location | the effect is long-running |

Never let the second caller through because the first "seems stuck". A stalled attempt whose fate is unknown is exactly when duplicating costs most.

## 8. Treat unknown as a third outcome

Every call has three outcomes: success, failure and unknown. A timeout says nothing about whether the effect applied.

Record the intent before the outbound call so a crash between the call and the response leaves evidence something must resolve later, instead of a silently retried side effect. When the intent record and the external effect are not in one transaction (usually they cannot be), reconciliation is still required: a database UNIQUE constraint does not create exactly-once across an external provider. State how an unknown outcome is resolved — query the provider by the operation identifier, retry the same key (which now hits the claim), or compensate.

Execution "unknown" is not the same thing as an evidence verdict of UNVERIFIED: the former needs an intent record plus reconciliation; the latter is a judgment that the available evidence does not support a conclusion. This method does not change the verdict mapping.

## 9. Set retention from the longest re-delivery path

Keys must outlive every path that can re-deliver the same intent, not the disk budget: the dead-letter replay window, the queue's retention, the provider's dispute window, the batch re-run interval. A key TTL shorter than the longest re-delivery path is a queued duplicate (source example: a 24-hour key TTL behind a 7-day DLQ). The actual numbers come from the actual queue, provider and job scheduling in the task.

## Examples and counterexamples

- **Concurrent check-then-act.** Two retries arrive together; both read "key absent"; both charge. Counterexample to "we check the key first". Correct: let the storage claim decide the winner.
- **Same key, different payload.** A caller reuses a key after editing the body; the server returns the first result. The caller believes the edited request was applied. Correct: fail loudly.
- **Timeout, fate unknown.** A provider call times out; the client retries with the same key; the provider had applied the first attempt. Without an intent record there is no way to reconcile. Correct: record before the call; reconcile after.
- **Short TTL behind a long replay path.** A DLQ is replayed a week after the incident; the key expired after 24 hours; the replayed charge applies a second time.
- **Over-broad key.** Two legitimate same-amount charges for one customer collapse into one because the key was derived from mutable business values rather than the operation's immutable identity.
- **Schema green, cycle present.** A plan validates field by field, but task A references task B and B references A. A structural check passes; a consumer that assumes an acyclic graph loops or drops work.
- **Runtime check, generated artifact unchecked.** The type rejects a reference to a non-existent task at runtime, while the generated JSON schema consumers use has no such constraint. The artifact looks authoritative and protects less than the runtime.
- **Illegal reference: runtime rejection vs partial read.** The runtime parser rejects the bad reference and names the field path; a tolerant traversal instead skips the bad row and reports success. The second says "processed", not "all inputs were sound".

## Conditions and exceptions

- No retry path and no duplicate-delivery path means the retry/idempotency sections (§4–9) do not apply; the contract and verification sections (§1–3) are selected independently by the interface's actual boundary problem.
- A read-only operation needs no idempotency key; a naturally idempotent write (set a value to X) may need only a declared repeat semantic.
- An operation whose effect cannot be made idempotent must still declare its duplicate protection, query/recovery path, or compensation instead of promising exactly-once.
- The interface may be REST, RPC, a queue message, or an internal call; the rules are about the operation, not the transport.
- For an agent-facing command-line surface, the CLI-visible contract (non-interactive modes, actionable errors, repeat semantics, preview effects) is a separate consumer contract; this method supplies the retry and idempotency semantics that contract references.

## Limits

- REST naming, HTTP status-code tables, `camelCase` conventions and the one-version rule are optional design conventions from the source, not requirements. An existing legitimate multi-version strategy can be used. A new internal stable function does not need an API document, a schema, or an idempotency key because of this method; only a boundary it actually has selects a section.
- This method does not require an idempotency key everywhere, does not choose the key's storage or format, and does not grant permission to run payment, data or provider operations. Code examples are illustrative; carrying one into a real system needs the task's own authorization.
- Provider-specific exactly-once claims are not established here. If the task depends on one, its actual guarantee must be verified with that provider.
- This method does not require a JSON Charter, a schema generator, or a validator platform; the structural/semantic boundary above is a design discipline. Strict rejection versus unknown-field retention follows the actual protocol, and fault-tolerant reads must disclose their skipped range.
- A check's strict format, lane count or tidy output is not evidence that the professional review behind it was adequate; its implementation language is not evidence of what it verifies, and two checks sharing a language pattern are only a clue that they are related.
- Automating a check is justified by real scale, reliability and cost, not by the principle's name. Learning the recipe on a hand-done unit, keeping the comparison rerunnable and leaving the contract/scope unchanged are the useful parts; a one-off CI job or an out-of-scope framework is not required. No helper is ported here — not because scripts are worth less, but because no current task consumes them.

## Source anchors

| Source | Retained contribution |
| --- | --- |
| Addy Osmani, `addyosmani-agent-skills` at `2686b620fc1fed2e8f60c704839c766b8594c6b6`, `skills/api-and-interface-design/SKILL.md` (`Contract First`, `Consistent Error Semantics`, `Validate at Boundaries`, `Prefer Addition Over Modification`, `Pagination`, `Partial Updates`, `Honouring an Idempotency Key`, `Red Flags`, `Verification`) | Caller-visible contract inventory; validation at the boundary with third-party responses always untrusted; intent-derived keys; atomic claim; payload binding; in-flight duplicate choice; three outcomes and intent recorded before the call; retention from the longest re-delivery path; the concurrency / differing-payload / timeout / short-TTL counterexamples. |
| Same pin, `skills/api-and-interface-design/SKILL.md` (`Hyrum's Law`, `The One-Version Rule`, `Predictable Naming`) | Weakly retained as context: observable behaviour becomes a de facto contract. Naming, status codes and single-version preference are optional conventions, not adopted rules. |
| Cursor plugins, `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`, `orchestrate/skills/orchestrate/scripts/schemas.ts` (`Plan` cross-field `refine`, state/migration/formatter, generated `plan.schema.json`) and `scripts/cli/util.ts` (parse/URI/dispatcher encoding boundary) | Input variants, field constraints and unified enums; cross-field invariants — reference existence, self-reference, cycles, duplicate names — checked before consumption; field-path errors with an executable fix; explicit old-field migration; diagnostic traversal that isolates a bad row and discloses the skipped range; the structural-green/graph-wrong, runtime-check/generated-artifact, and source-has-graph/generated-lacks-graph counterexamples. |
| Same pin, `pstack/skills/principle-type-system-discipline/SKILL.md` (sum types, brands, boundary parsing, exhaustive matching, authoritative schemas), `pstack/skills/poteto-mode/scripts/orch/store.ts` (`atomicWrite` temp+rename, `writeIfMissing`, PID lock/force), `pstack/skills/principle-build-the-lever/SKILL.md` (manual unit first, rerunnable lever) | Illegal states unrepresentable, branded semantic primitives, external data parsed once at the boundary, exhaustive variant handling and authoritative-shape derivation — while types remain not permissions and runtime invariants still apply at shared/async/mutable/expiring points; single-file temp+rename is a publish pattern, not durability/transactionality; check-by-missing needs a concurrency premise; PID-lock caveats; the lever's manual-recipe/rerunnable part, with the scripting decision governed by real scale/reliability/cost. No validator platform, store or script is ported. |
| Same pin, `pstack/skills/typescript-best-practices/SKILL.md` and `references/patterns.md` | `satisfies`, `unknown` narrowed to a validated value, total functions and semantic primitives as on-demand mapping examples; a non-null assertion on an environment variable is a compile-time claim, not runtime validation; casts/interop with a real guarantee stay usable; no language-wide or schema-adoption policy. Examples only — no TypeScript version, client behaviour or boundary test is certified. |

Deferred from the same Addy source: GraphQL/type-system extras, branded types, discriminated unions, and the case for never maintaining two versions. The Cursor `orchestrate` runtime scripts, schema generator, type/store/build-lever skills and tests are not ported: no current task consumption depends on them, and porting would bring their permissions and dependency boundary. That is a consumption decision, not a judgment that scripts are worth less — the boundary experience above is retained, and no validator platform or store is introduced. Also not adopted: the type system as a substitute for runtime invariants or authority, temp+rename as durability, "the lever must produce a file" as a universal rule, a blanket ban on `as`/non-null, forced schema adoption, and treating a non-null assertion or a "fails loudly" comment as completed runtime validation.

---
# Fixed revised file: 8ba69427105d09b3efa1d3a5f28182d4243b5fea:professional-workflow/methods/performance-and-neutrality.md
SHA256 a2b2add421d652abb12f663875c6c9ff27fa5e9a84c782cb947f869f4b7897dc

# Performance investigation and neutrality · candidate method body

- **Status:** candidate distilled under `docs/absorption/2026-10-02/reviews/ORACLE-REVIEW-A1-ADDY-CD.md` (C9, 2026-10-02, source `addy@2686b620`), extended under `docs/absorption/2026-10-02/reviews/REVIEW-GATE2-A2R-CURSOR-ABC8.md` (MG1/MG2, 2026-10-02, source Cursor `ecc249f1`), and further extended under `docs/absorption/2026-10-02/reviews/REVIEW-GATE2-A1-ADDY-EF-ADDENDUM.md` (P1–P9 performance/cache/query/pool branches, 2026-10-02, source `addy@2686b620`); revised under `docs/absorption/2026-10-02/PRO1-DISPOSITION.md` (TPW-PRO1-003: effect estimate, sample spread and actual value separated); not yet an accepted reference; creates no authority, trigger, or gate. A fixed-diff review still applies. This file is the single carrier for performance evidence; no second perf-evidence file or registry is created.
- **Method owner when bound:** D/E run the investigation and the change; F evaluates a performance claim against its baseline with the actual measurement conditions. This method does not set a target the task does not have.

## Use

Use when a performance requirement exists, when users or monitoring report slow behavior, when a suspected regression needs a baseline comparison, or when a measured bottleneck has been identified. **Do not optimize before there is evidence of a problem**: premature optimization adds complexity that costs more than it returns.

## Workflow

```
measure → identify → fix → verify → guard
```

1. **Measure** with the best available data. Synthetic runs (a controlled harness, a profiler, a repeatable benchmark) are reproducible and good for isolating a specific effect; field data (real-user telemetry, traces, production metrics) is what shows what users actually experience. Use both when both exist; use what the task actually has.
2. **Identify** the actual bottleneck by decomposing the symptom, not by assuming.
3. **Fix** the specific bottleneck.
4. **Verify** with the same conditions as the baseline; keep or revert.
5. **Guard** the metric the user feels, so the regression is detected next time.

## What each kind of evidence can prove

- A **synthetic comparison** establishes behavior in the environment it actually ran in (same command, same data, same conditions). It proves the effect under those conditions and nothing wider.
- A **user-facing benefit claim** needs evidence from the user surface — field telemetry, a real client, production-like traffic — or an explicit statement that the observed effect was local and the user-facing benefit is unproven.
- Not every local backend performance task needs RUM, Lighthouse or a browser. A backend latency fix can be established with its own measured conditions; it just cannot claim a user-facing improvement it did not measure.

## Ground the workload and prove the harness

- **Name the real workload dimensions first** — data size, history, state, concurrency and the actual call or interaction pattern — and pick a case that reproduces the reported symptom. If no case reproduces it, fixing the reproduction comes before optimizing.
- **Fix one metric, its direction, and a falsifiable target** that the task's real authority accepts. The target's conditions, direction, threshold and stop basis come from that authority (see "When to stop"). A non-performance metric uses the comparison method that fits its own owner and claim rather than this one.
- **Prove the harness can distinguish the expected signal.** Run the target case and a simpler case that should behave differently; if the harness cannot separate them, change the workload or the metric before trusting a result. Easy-versus-target separation helps, but it does not guarantee coverage of every condition.
- **Record a baseline and the regression gate** — the checks that must stay green — before any change.
- **Freeze one repeatable command that emits the metric.** Changing the instrument keeps the old baseline and the reason; do not swap to a flattering measure to win. If a genuine measurement defect must be fixed, rebuild the affected comparable data and say so.
- **Repeat the same object under the same conditions and say what was controlled:** warmup, cache state, ordering, sample size and run-to-run noise, plus a negative control where one is meaningful. A single run is still an observed measurement of the object under those conditions; whether it is *sufficient* depends on the claim, the known noise and the coverage — a targeted count under a fixed input can validly support that count claim, while a stable user-facing benefit claim usually needs repetition and representative conditions. N repeats with a median is a common starting point, not a sufficient guarantee by itself and not the best statistic for every distribution. The method fixes no N and no attempt floor.
- **Existing timing, logs or query output that can answer the claim are enough.** A profiler, trace or capture is one available instrument, not a requirement for every task. A captured baseline or post-fix artifact is interpreted under the conditions that produced it — version, load, environment and noise — and does not stand for conditions it never ran in.

## Decompose the symptom before touching code

Decide what to measure from the reported symptom; the real trace path is the route, not the guess:

```
What is slow?
├── first page load
│   ├── large bundle → measure bundle size, check splitting
│   ├── slow server response → measure TTFB in the waterfall
│   └── render-blocking resources → check the waterfall for blocking CSS/JS
├── interaction feels sluggish
│   ├── UI freezes on click → profile the main thread for long tasks
│   └── animation jank → check layout thrashing / forced reflows
├── page after navigation
│   ├── data loading → measure API times, look for request waterfalls
│   └── client rendering → profile render time, check for N+1 fetches
└── backend / API
    ├── one endpoint slow → profile its queries and plans
    ├── all endpoints slow → check the connection pool, memory, CPU
    └── intermittent slowness → look for lock contention, GC, an external dependency
```

"Slow" is not a diagnosis. The decomposition says which of the available measurements can discriminate. A slow **interaction** decomposes further into input delay (the main thread was busy before the handler ran), processing time (the handler and render work itself), and presentation delay (the frame could not be committed). The three point at different fixes; find which one dominates in a trace of the actual interaction rather than editing the handler. If the problem does not reproduce on the available high-end machine, choose a representative device or condition and say that CPU throttling is a proxy, not the user's device; a local capture can support a local claim, and a RUM-first rule is not required to start a local investigation.

## Candidate strategies are hypotheses, not a checklist

These families generate hypotheses; they are a useful set, not an exhaustive taxonomy. A family is admissible only when the evidence names a mechanism it addresses; working through every family because it exists is the failure to avoid. A trace tells you what is slow, never what is safe to delete or that no consumer exists — elimination needs accepted behaviour or a real usage path.

| Family | Admissible when | Win condition |
| --- | --- | --- |
| Elimination | a computation, feature path or legacy branch may not need to exist | accepted behaviour or a real usage path shows nothing consumes it |
| Divide and conquer | a dominant cost grows with input size | chunking, sharding, pruning or independent parallel blocks reduce the measured cost |
| Caching | the same input is computed or fetched repeatedly | the input, key, staleness window and invalidation are named before any win is claimed |
| Indirection | an expensive operation sits on a hot path that a cheaper intermediate layer absorbs (an index instead of a scan, a queue moving work off the interactive thread, a handle swapping in a cheaper implementation) | it removes more from the critical path than it adds; the new hop and its own costs are measured |
| Batching | many small operations each pay a fixed overhead | they are combined into one batch that pays the overhead once |
| Redundancy / hedging | waiting on a slow instance dominates the time | the trace shows wait dominance and the system has headroom; cancellation, side effects, retry identity and result ordering are defined, and no charge or write is duplicated to take the fastest answer |
| Lazy evaluation | the cost lands on a result never used or not yet needed | the work moves to first use and the deferred path's own cost is counted |
| Scheduling | the work must happen but not at the interaction moment | the win is perceived latency, so the interaction path is measured, not only total work; deferred total cost and any new tail risk are recorded — moving work to the background is not automatically a total saving |

Route by what the change actually affects or would change: domain meaning, a shared interface, compatibility, or an established technical commitment. A cross-module or internal implementation that stays inside an existing valid delegation and preserves those agreements — for example, a batching arrangement D already authorized, implemented inside two modules against the existing interface — continues inside the performance loop; an ordinary function call does not need a design review every time. The loop may not change an upstream contract or expand its own permission, and it does not create a new approval actor or gate.

## Common bottlenecks and the conditions that decide them

- **N+1 reads.** One query per row where a join/batch would do. Evidence: the query log or trace shows repeated statements. Fix: fetch in one round trip; verify the count dropped.
- **Unbounded reads.** A list endpoint returning everything. Fix: pagination or a limit; a bounded read is also what protects the database from the caller.
- **A query that ignores its index.** "Add an index" is the guess; the query plan is the measurement. Capture the plan **before** the change as the baseline, and read it for the plan shape: a sequential scan on a large table that needs to be understood (index missing, unusable, or genuinely not worth it), a sort node that a composite index could absorb, and estimates (`rows=`) far from actuals, which point at stale statistics to refresh before touching indexes. Index the shape of the query — equality columns before the range/sort column is the common composite order, while covering, partial, expression and full-text indexes are conditional answers to specific shapes, not universal primitives. Know when a plain B-tree cannot help and a different mechanism is needed: low selectivity on the dominant value (`status` at 95% one value), a leading-wildcard match, or a function applied to the column. Measure the write cost on write-heavy tables: every index taxes every insert and update. **An unchanged plan does not automatically revert the index, and it does not prove the index was worthless**: check what the plan was measured on (statistics freshness, parameter values, actual data, engine and its load) and the measured usage; the specific benefit depends on the actually tested load and write cost. If it stays unexplained, do not keep it as a neutral change. Dropping an index is its own operation — check constraints, consumers and permissions first. Note that an `EXPLAIN ANALYZE`-level plan can actually execute the query (writes, functions, resource use), so it belongs in a legitimately authorized environment; where that capability is missing, record the read benefit as unverified rather than forcing a production probe.
- **Connection-pool exhaustion.** The signature is every endpoint slowing at once, the slow time spent waiting for a connection, and a mostly idle database. Size against the real resource limit and **all** competing consumers — every instance, pool, job, admin connection and migration plus headroom shares the same ceiling, so `instances × pool max` is one input, not the whole budget. A pool per request burns connections; one shared pool per process is the common example for a single resource, and separate pools for genuinely different tenants, databases or isolation goals can be legitimate. Diagnose before resizing: find what holds connections (long transactions, a missing await, leaked clients). A pool larger than what the database can execute concurrently just relocates the queue somewhere less visible — bigger is not faster. Bounded wait and timeouts follow the service objective and its recovery behaviour; failing fast is not a universal goal. Unbounded autoscaling needs an admission or capacity guarantee: a multiplexing proxy is one option that must be checked for transaction and session compatibility, not automatically safe. Parameter names and limits are engine- and client-version-specific.
- **Frontend.** Images (format, responsive sizes, explicit dimensions, priority vs lazy loading), render-blocking work, unnecessary re-renders, and bundle growth. Each has its own measurement; a bundle-size reduction is not a user-experience result until the user-facing metric moves. Reserving layout — explicit dimensions and art-direction-safe sizing for images, plus fallback font metrics — reduces shift, but verify it at the real viewport and font load rather than applying one width/height or format policy everywhere; forcing `sideEffects: false` onto a package that has side effects is not a tree-shaking win.
- **Caching.** Cache what is expensive to produce and read far more often than it changes; the measured cost and read/write ratio are the selection evidence, not the availability of a cache library. A layer (in-process, shared, CDN/edge) has visibility, staleness and invalidation costs that differ. **The key must include every input the response varies on** — tenant, locale, viewer, permissions, feature flags — whether by a literal key or by a partition/namespace that preserves the same equivalence class; a key that omits the viewer serves one user's data to another, which is a correctness failure, not only a performance one. Choose one invalidation strategy (TTL, event/tag, or versioned keys), or a stated combination; an accidental mix is the failure. The acceptable staleness window is a B/C/policy decision, not a TTL typed in passing. Write-through synchronising two writes does not by itself make them atomic across stores or prevent staleness; write-behind needs durability, replay and unknown-result handling so the cache never becomes the only unprotected source of truth. **The rule about sensitive data is not a blanket ban**: when staleness would break this task's correctness and there is no provable coordination guarantee, do not honour the promise with a TTL. Otherwise state the window. Set an eviction policy and a memory ceiling; an "unbounded" cache is a capacity risk, not by that word alone a diagnosed leak. A low hit rate is not automatically worthless — a cache can still pay for a correctness or burst-cost purpose — so read actual total cost, tail and maintenance instead of deleting on a hit threshold. These correctness conditions belong to the actual contract and its owner; `interface-contract-and-retry.md` covers operation identity and repeat semantics, and `trust-boundary-and-actions.md` covers authorization boundaries.
  - **Negative results.** Caching the absence of a result can protect a path that would otherwise reach the origin on every miss (a nonexistent ID probed in a loop). But authoritative absence is not the same as a timeout, a 5xx, a permission-masked response or an unknown outcome: cache the first, and never let an origin failure become a persistent "not found", or one failing minute becomes many. The negative window follows creation-visibility, abuse and load goals and is not necessarily shorter than the positive one; a newly created record must become visible promptly, and the reader's authorization semantics must stay correct.
  - **Stampede protection.** One recompute, N waiters: share the in-flight result per key, clean up after failure, and bound the wait. A process-local in-flight map covers only that process; a shared layer needs coordination that fits its freshness contract — a lock, admission control, or stale-while-revalidate where serving stale is allowed. Stale-while-revalidate cannot be used where the staleness would violate the contract, and a lock needs a real owner, fencing and timeout guarantee rather than convention. Sharing an in-flight promise is not the same as cancelling the underlying fetch: a caller giving up does not necessarily stop the work. A short illustrative in-flight snippet does not by itself establish safety across synchronous throws, re-entrancy, processes or cancellation.

## Verify: same conditions, one change, beat the noise

- **Re-measure the way the baseline was measured** — same command, same data, same environment, same budget. A cold-cache baseline compared with a warm-cache result measures the cache, not the change.
- **One attempt, one explainable hypothesis.** Say what the change is expected to move and by what mechanism before running it. A speculative probe is allowed when the mechanism is not yet known, but label it a probe and do not credit it as an explained win.
- **Change one thing at a time.** Several optimizations landed together produce one number and no attribution. If they must ship together, measure each in isolation first; if they genuinely cannot be separated, state that attribution limit instead of crediting the combined number to each change. Do not stack untested tweaks and attribute the total to every item.
- **Separate the effect estimate from raw sample spread.** How much repetition and what design are needed follows the claim, the known noise and variation, and the coverage: a deterministic narrow count under a fixed input can be supported by a single run, while a claim that estimates noise or a stable benefit needs appropriate repetition. The uncertainty of the *effect* estimate depends on sample size, pairing and correlation, comparability and confounding — not on the raw overlap of two distributions. Heavily overlapping distributions can still support a precise enough estimate of the mean difference, and a mean that looks improved can come from too little sampling, incomparable conditions or a material confounder. A "3% gain inside a ±5% band" is therefore not by itself a verdict in either direction: two bare numbers cannot decide whether the improvement is established, unestablished or absent. That depends on the effect estimate and its uncertainty under the measurement design and on what the claim needs. Design the measurement for the claim; this method fixes no t-test, bootstrap, interval or N.

Conditional shapes, to make the distinction concrete:
- **Raw distributions overlap, estimate usable.** Two independent, comparable groups of 1000 runs with means 100 ms and 97 ms and standard deviation 5 ms give a standard error of the difference of about 0.224 ms (5 × √(2/1000)); the distributions overlap heavily and the 3 ms mean effect is still estimated precisely enough to support that claim under those conditions. This is a worked hypothetical for the arithmetic — not a benchmark, and not a required sample size.
- **Mean moved, estimate not established.** Fewer or unmatched samples, an incomparable environment, or a material confounder (another change in the same window, a warmed cache, a different workload) can move the mean while leaving the effect unestablished. That calls for more or better evidence, not for claiming the win.

Decision table:

| Result versus baseline | Action |
| --- | --- |
| a usable effect estimate past the stated benefit threshold and correctness checks green | **keep**, with the before/after numbers recorded |
| no usable effect estimate for the claim (too imprecise, incomparable, or materially confounded) | the improvement is **not established**: continue, defer or revert per the existing budget and purpose — not a product FAIL |
| a usable estimate shows no benefit worth keeping (below the accepted benefit threshold, or not worth the maintenance cost) | **revert or defer** — a supported neutral result is a revert, not a keep |
| a usable estimate shows the change is worse | **revert** |
| improved but a correctness check went red | **revert** — a regression wearing a win's clothing |

An imprecise or inconclusive result is **not a product FAIL**: the improvement is simply not established, and what to do next — continue with a better measurement design, defer, or revert — follows the existing budget and purpose. A supported no-benefit result reverts rather than accumulating maintenance cost for nothing. A change that also serves an accepted reliability or correctness purpose is evaluated by that purpose; a performance-neutral result does not veto it.

A comparison that measures the **wrong surface**, or comes out **inconclusive**, is not a PASS either. An inconclusive run does not confirm the fix, and a green result on a surface other than the claimed one does not establish the claim. A previously valid observation may be reused while its conditions still hold; an untested ceiling cannot be claimed as the limit.

**Correctness gates the metric.** An "optimization" that wins by dropping work the product needed — skipping a validation, caching something that must be fresh, removing a load-bearing wait — is a regression, not a win. Do not manufacture a performance number by removing a correctness check.

## Keep a ledger of attempts

Reverted work leaves no trace in version history, which is exactly why the same dead idea is tried again later. Record every attempt — kept and reverted — with the numbers and the reason:

| Idea | Baseline → result | Verdict | Why |
| --- | --- | --- | --- |
| memoize the row component | INP 240 ms → 235 ms | reverted | the 5 ms difference is below the accepted benefit threshold for this claim; the trace pointed at the list rows, not the memoized component |
| virtualize the list | INP 240 ms → 90 ms | kept | long tasks gone from the trace |
| preconnect to the API origin | LCP 2.8 s → 2.8 s | reverted | already same-origin |

A section in the change description or a trail the repository already keeps both work; reuse the existing trail rather than creating a second registry, and do not require a commit per attempt. Each record names the actual object, the command or harness that produced the numbers, the measure and threshold, the verdict and reason, and what the observation does not cover — kept, reverted or deferred.

## Complexity must pay for itself — without vetoing other purposes

Code that is kept is maintained forever. When a change adds complexity solely for performance and produces no established benefit worth keeping, **revert or defer it**. But if the same change also serves an already-accepted reliability or correctness purpose, evaluate it by that purpose: a neutral performance measurement does not by itself veto it. State which purpose is being claimed, and remember that a green test result certifies the checks that ran, not every commitment the change retained.

## When to stop

A continued optimization loop ends when a legitimate stop condition is met — the accepted target is reached, resource, cost or environment constraints intervene, or the remaining benefit no longer justifies the cost. Cheap untried ideas do not license unlimited runtime; pivoting the mechanism class, combining near misses or re-reading the source can be worth another round, but "push past the first plateau" is not a universal obligation. Relaxing the target is the target owner's decision and must be stated explicitly; silently swapping the criterion to declare the work done is not a stop condition.

## A performance claim does not overwrite a valid security or cache policy

Cache and performance optimization interacts with policies set for other reasons. One source checklist item says to avoid `Cache-Control: no-store` on HTML responses because it blocks back/forward-cache eligibility. That statement is **browser- and version-dependent**, and the source predates a relevant change:

- Chrome's official page records experiments for `Cache-Control: no-store` pages since Chrome 116 and an **expected** reach of 100% in March and April 2025 — a forward-looking statement on the page, not a completion record. Its stated conditions: the page is evicted from bfcache on cookie or other authorization changes; pages using WebSocket, WebTransport or WebRTC, or that fetch a `no-store` response, remain ineligible; the bfcache timeout for these pages is reduced (3 minutes); and an enterprise policy can opt out. Whether the rollout has since completed is not established here; claiming completion needs direct completion evidence.
- The same documentation states plainly that other browsers may still block bfcache for `no-store` pages, and that the best practice remains to **minimize** `no-store` rather than depend on the heuristics.

Source and date: Chrome for Developers, "Enabling bfcache for Cache-Control: no-store", published 2024-10-21, updated 2025-09-09. This is version- and vendor-specific evidence about Chrome's expected rollout, not a universal rule, and not this library's observation of an actual user benefit.

The engineering conclusion is the boundary, not the trick: **do not remove `Cache-Control: no-store` from a page that holds sensitive content to win a performance metric.** Changing a cache policy for performance needs the actual browser support matrix for the target audience and the decision of whoever owns the security/cache policy. A performance number never overrides a valid security policy.

## Limits

- The source's fixed targets — LCP/INP/CLS values, bundle/CSS/image/font budgets, p95 milliseconds — are examples. They are **not this library's authorized SLO**, and adopting one requires the actual user requirement and the authority that owns it.
- This method does not require every task to measure, and it does not require RUM/Lighthouse where the claim is local. It does not create a performance gate.
- An unmeasured "obvious win" is not evidence. An optimization with no bottleneck identification is a guess that happens to compile.
- This method does not grant permission to add load, change production configuration, alter caching policy, or expand debugging or instrumentation access. Live instrumentation and process-level changes are mutations that need their own authorization, a rollback or cleanup path, and preserved evidence; a static code clue can rule a hypothesis out and justify a probe, but it does not by itself certify a measured benefit. Reverting a change is also an action: only revert within your own authorization, and preserve the evidence and a recoverable object.
- The source's hillclimb defaults — pairing a target with at least 10 attempts or a 50% improvement, a fixed N with a median, a commit per fix, a frozen harness that may never change, and reverting every non-win — are rejected as rules. This method also does not create a second performance-evidence file or registry.
- The source checklists' numbers, manager/proxy names, commands and browser/platform support matrices are inputs to verify, not this library's policy or current runnable qualification; cache, pool and index parameters follow the actual engine and client version. The pool-plan-cache conditions above are source-derived and have not been exercised against a real engine or workload here — verify each against the actual system.
- A performance result is evidence for a decision, not the decision: trade-offs, release timing and risk acceptance stay with the valid delegation, and a measurement does not become an authorization.

## Source anchors

| Source | Retained contribution |
| --- | --- |
| Addy Osmani, `addyosmani-agent-skills` at `2686b620fc1fed2e8f60c704839c766b8594c6b6`, `skills/performance-optimization/SKILL.md` (`Overview`, `The Optimization Workflow` steps 1–5, `Where to Start Measuring`, `Step 2: Identify the Bottleneck`, `Step 3` anti-patterns, `Step 4: Verify`, `Log every attempt`, `Step 5: Guard Against Regression`, `Common Rationalizations`, `Red Flags`) | Measure before optimizing; symptom decomposition; synthetic vs field evidence; the common bottlenecks with their deciding measurements; same-condition re-measurement, one change at a time, separating the effect estimate from raw sample spread; the decision table including the not-established case; correctness gating the metric; the attempt ledger; guarding the user-facing metric. |
| Same pin, `references/performance-checklist.md` (`Connection pooling`, `Query plans`, `Index strategy`, `Caching Strategies` incl. read/write patterns, negative caching, request coalescing and the cache checklist, `Frontend Checklist`) | Pool capacity across all competing consumers and headroom, diagnosis before resizing, bounded wait/timeouts, unbounded autoscaling and proxy caveat; index-change plan reading with baseline plan, estimate/sort signals, composite-order and write-cost conditions, and non-automatic revert; cache selection evidence, key equivalence classes, invalidation/staleness ownership, negative results versus origin errors, in-flight coalescing with lock/stale-while-revalidate caveats, memory ceiling and hit-rate nuance; layout reservation via dimensions and fallback font metrics verified at the real viewport. The `no-store`/bfcache item remains a version-limited example corrected against the vendor documentation above. |
| Chrome for Developers, `https://developer.chrome.com/docs/web-platform/bfcache-ccns` (published 2024-10-21, updated 2025-09-09) | The actual Chrome bfcache/no-store behavior, its conditions, the enterprise opt-out, and the explicit note that other browsers may still block these pages and that minimizing `no-store` remains best practice. |
| Cursor plugins, `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`, `pstack/skills/poteto-mode/playbooks/hillclimb.md` and `pstack/skills/poteto-mode/playbooks/perf-issue.md` | Harness sensitivity proven before it is trusted; workload/architecture grounding and a reproducing case; falsifiable target and stop condition from the real authority; repeat under controlled conditions with warmup/cache/order/sample/noise and a negative control; one explainable hypothesis per change; kept/reverted/deferred records that reuse the existing trail; the eight strategy families as mechanism-grounded optional hypotheses with per-family win conditions; a trace shows what is slow, never what is safe to delete. |

Narrowed from the sources: the fixed metric/budget values, "always use both synthetic and RUM", "the plan not changing means the index is worthless", and the unconditional list of things that must never be cached; the hillclimb attempt/improvement floors, fixed N-median requirement, per-fix commit and freeze-never-change rules; and any requirement to run a profiler or capture before proposing a labelled hypothesis. Treating a raw ± spread as a verdict of no benefit is likewise not adopted (TPW-PRO1-003): an unusable estimate leaves the improvement unestablished instead of failing the product, and a usable estimate is weighed against the accepted benefit threshold, maintenance cost and other purposes. The Cursor playbooks are not ported as scripts or runtime; only the measurement discipline above is retained.

---
# Fixed revised file: 8ba69427105d09b3efa1d3a5f28182d4243b5fea:professional-workflow/methods/release-and-recovery.md
SHA256 70be6fb43343b8d926a013d540acb35d6d73548497f94193f3b48fc87c83b5a3

# Release and recovery · candidate method body

- **Status:** candidate distilled under `docs/absorption/2026-10-02/reviews/ORACLE-REVIEW-A1-ADDY-CD.md` (C4, 2026-10-02, source `addy@2686b620`) and further extended under `docs/absorption/2026-10-02/reviews/REVIEW-GATE2-A4-CURSOR-DEF.md` (G05 gate-status counterexample, G04 gate-answer semantics, 2026-10-02, source Cursor `ecc249f1`); revised under `docs/absorption/2026-10-02/PRO1-DISPOSITION.md` (TPW-PRO1-001: observed usability separated from the acceptance act); not yet an accepted reference; creates no authority, trigger, or gate. A fixed-diff review still applies.
- **Method owner when bound:** D/E plan the change, its rollout and its recovery path; the go/no-go decision, risk acceptance and any external communication stay with the authority that actually owns them.

## Use

Use when a change involves persistence, external behaviour, deployment, or a staged rollout. A fully local change that can be discarded at any time with no external observable effect does not need this method.

Four different things are often called "release". Keep them separate, because closing one does not close the others:

- **deployed** — the artifact is present in the target environment
- **enabled** — the feature is active for someone (flag on, route serving, job scheduled)
- **observed / verified usable** — the intended user path has been observed (or otherwise verified) to work for a definite object and version within a stated boundary: which path, when, under what conditions, and with what evidence — or the honest gap
- **shut down** — the old path is removed and the temporary machinery (flag, dual path, migration task) is gone

**Deployed is not enabled, and enabled is not observed usable.** A deployment that reports success while the user path fails is a deployment, not a usable release.

**Acceptance is an act, not an observation.** The responsible party — a role, or an existing valid rule that already covers the object — accepts a definite object and version, and the record names who or which rule accepted it, when, and under what scope or conditions. An observed or verified usable path is evidence for that decision; it is not the decision, and an F PASS does not produce acceptance. Do not route every acceptance to a human by default: an existing valid delegation can accept within its own boundary, and the record then names that rule.

Record the two separately — `observed` (object/version, path, time and conditions, evidence or gap) and `accepted` (object/version, acceptor or rule, time, scope) — because they have different truth conditions and different owners. Collapsing them either blocks a working release on an unrecorded decision or treats authority as proof that the implementation works. Two cases show why:
- the observed path passes (the canary is stable and the critical flow was exercised) but the authorized acceptance for this object has not happened: observed, not yet accepted;
- the behaviour contract is accepted (for example by B/C) but the implementation was never observed: accepted contract, unobserved implementation — acceptance of the design is not evidence that the built version works.

## Preconditions

1. **Deployment can be separated from enablement.** If it cannot, staged/flag-off rollout is not available; state that as a design gap rather than imitating a rollout. It does **not** follow that there is no recovery path: an atomic release with no flag is still recovered by redeploying a compatible previous artifact or rolling forward, and a small service that cannot stage still has whatever redeploy/restore capability it actually runs. Name separately which staged capability is missing and which recovery mechanism is actually available; exercise it under valid authorization, and if it has never been exercised, report it as a plan rather than a capability. Do not claim that rollout is available, or that recovery is impossible, without checking.
2. **A baseline exists.** Every threshold below is *relative to a baseline*. Without a baseline there is no "2×" to compare against.
3. **The recovery path is verified, not merely documented.** A written rollback that has never been exercised is a plan, not a capability.

## The rollback plan (four parts; a missing part means there is no plan)

- **Trigger conditions.** Which signals cause a rollback — error rate relative to baseline, latency, data integrity, security, a user-reported failure pattern.
- **Rollback steps.** Which action comes first (turn the flag off, or redeploy the previous version), how the rollback is verified, and who is told.
- **What happens to the data.** Data written by this change is preserved, cleaned up, or needs separate reconciliation. Code rollback does not roll data back.
- **Time to roll back, as a number.** Give the magnitude for each mechanism the task actually has — flag off, redeploy, database action. "Fast" is not a duration; the source's `< 1 min` / `< 5 min` / `< 15 min` figures are examples, and a real plan states the measured or estimated value for its own mechanisms.

## Staged rollout: three decisions relative to the baseline

Every stage of a rollout must be able to go three ways — not two:

| Decision | Signal |
| --- | --- |
| **Advance** | the metric is near the baseline; no new failure class |
| **Hold and investigate** | the metric is clearly worse than baseline but not at the rollback line |
| **Roll back** | the metric crosses the rollback line, or integrity/security is in doubt |

Also read the **burn rate**, not only the current value: consuming the allowed error budget faster than the baseline pace is a hold signal even while each individual threshold is still green. A green snapshot with a rising burn is not "fine".

Source example thresholds (error rate within 10% / 10–100% / >2×; P95 latency within 20% / 20–50% / >50%; error-budget bands >20% / 0–20% / exhausted / reset; percentages 5 → 25 → 50 → 100; monitoring windows 24–48 h; flag cleanup within two weeks). None of these is a library rule. Adopting a threshold requires the service's actual SLO, its actual budget, and the authority that owns that policy.

**When there is no real traffic or no staged-rollout capability**, use the deployment and recovery evidence that actually applies — deploy verification, a dry-run recovery, an authorized synthetic request through the real path — and state the missing user-facing evidence honestly. Do **not** fabricate a canary result or present a synthetic check as user-facing evidence.

## Flags

If a flag is used to stage the rollout:

- every flag has an **owner** and an **expiry**; an unowned, never-expiring flag is permanent complexity
- after full rollout, remove the flag and the dead path together (the source's two-week window is an example)
- **do not nest flags** — combinations multiply and the test matrix stops being real
- **test both states**; a flag whose off-branch is never exercised is an untested code path carrying production risk

## Rollout gates and the error budget

The error budget is a policy signal, not a negotiation: what action follows when the budget is low or exhausted comes from the service's error-budget policy and its owner. The source's four bands (>20% ship normally; 0–20% slow rollouts, no high-risk changes; exhausted freeze feature work; reset resume and bake in the fix) are one concrete policy example. The method does not invent the bands, and a plan or dashboard does not by itself authorize a release.

**A gate or status field is not release permission.** A null, pending, `UNKNOWN` or not-yet-decided value is not "clear"; a review-required flag is not an allow; a rollup that is merely "not FAILURE" is not a pass; and a structurally correct field does not mean the required policy was satisfied. A previously green CI run or an automated review approval is not risk acceptance for this object, and a `READY` state is neither merged nor released. A default "(no answer) = accepted risk" field is not a decision: resolving a gate needs a real answer, and a legitimate fallback can only come from a previously valid, non-reserved delegation.

## Observation after enablement

The first hour after enabling is when "deployed" is tested against "observed usable". The source's checks are a usable starting set: the health check returns successfully, error monitoring shows no new error class, latency shows no regression, the **critical user flow is exercised by hand**, logs are flowing and readable, and the rollback mechanism is confirmed ready (a dry run where possible). These are observation steps, not a universal gate; the actual set follows the change's critical path.

## Recovery and data

- State whether the change's data is reversible. If it is not, say what the backup/restore or forward-fix path is, what would be lost, and who accepted that risk.
- A recovery path that depends on a human action must name who acts and how they are reached — inside the existing valid delegation, not by assuming it.
- **Notification and actual deployment inherit the task's existing valid delegation.** This method does not grant reach, access, or permission to notify external parties; a communication plan that is not covered by the current authorization needs its own decision.

## Limits

- Not every release needs staging, a warning-free build, the full e2e suite, a feature flag, external services, or a notification action. Which of these are needed follows the change and the accepted quality policy.
- The rollout percentages, time windows, latency/error multipliers and budget bands above are source examples. They are not this library's thresholds, and using one requires the actual SLO, budget and authority.
- A plan, a checklist, or a dashboard is not release authority. Risk acceptance and the go/no-go decision remain where the project's authority places them.
- Continuous-integration gate wiring belongs to the quality-policy method; this method states rollout and recovery behaviour and does not duplicate the gate table.

## Source anchors

| Source | Retained contribution |
| --- | --- |
| Addy Osmani, `addyosmani-agent-skills` at `2686b620fc1fed2e8f60c704839c766b8594c6b6`, `skills/shipping-and-launch/SKILL.md` (`Feature Flag Strategy`, `Staged Rollout`, `Rollout Decision Thresholds`, `When to Roll Back`, `Monitoring and Observability`, `Post-Launch Verification`, `Error Budget Release Gate`, `Rollback Strategy`, `Red Flags`) | Deployment/enablement/observed-usability/shutdown distinction, with acceptance as a separate act by an authorized party or existing rule; flag owner, expiry, no nesting, both states tested; advance/hold/rollback relative to a baseline; burn rate as a hold signal even when individual thresholds pass; the four-part rollback plan with a time magnitude; data reversibility; first-hour verification including the critical user flow; error-budget policy as an owner decision. |
| Same pin, same file (`The Pre-Launch Checklist`, `Common Rationalizations`) | The deployed-is-not-usable mechanism. The full pre-launch checklist (code quality, security, performance, accessibility, infrastructure, documentation) is not adopted as a universal gate; its applicable parts follow the actual change and the accepted quality policy. |
| Cursor plugins, `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`, `pstack/skills/poteto-mode/scripts/watch-pr/policy.ts` (`resolveChecks` / gate status rollup) | A gate or status field is not release permission: null/pending/`UNKNOWN` is not clear, review-required is not an allow, "not FAILURE" is not a pass, structural fields do not satisfy the required policy, prior CI green or automated approval is not risk acceptance, `READY` is neither merged nor released, and a default "(no answer) = accepted risk" field is not a decision. The watcher/rules are not ported. |

Narrowed from the source: the specific thresholds, rollout percentages, time windows and budget bands are examples rather than rules; staging, no-warning builds, full e2e and flags are not required for every release. The source's "BLOCKED + rollup not FAILURE/ERROR → allowed" rule is rejected: unknown or review-required status is not an allow, and a gate's structural fields are not proof the required policy was met. The Cursor watcher and rules are not ported, and a READY state grants no merge or release authority.

---
# Fixed revised file: 8ba69427105d09b3efa1d3a5f28182d4243b5fea:professional-workflow/methods/trust-boundary-and-actions.md
SHA256 bb1877e2ac61c383ce9f67c0a3bb5841751346a40ca46a7eb92d29c5931d0ce3

# Trust boundaries and action classes · candidate method body

- **Status:** candidate distilled under `docs/absorption/2026-10-02/reviews/ORACLE-REVIEW-A1-ADDY-CD.md` (C6, 2026-10-02, source `addy@2686b620`), extended under `docs/absorption/2026-10-02/reviews/ORACLE-REVIEW-A4-DEF3.md` (J5, 2026-10-02, source Cursor `ecc249f1`), further extended under `docs/absorption/2026-10-02/reviews/REVIEW-GATE2-A4-CURSOR-DEF.md` (G03/G06/G12, 2026-10-02, source Cursor `ecc249f1`), and further extended under `docs/absorption/2026-10-02/reviews/REVIEW-GATE2-A4-CURSOR-DEF2.md` (H08/H09, 2026-10-02, same pin); not yet an accepted reference; creates no authority, trigger, or gate. A fixed-diff review still applies.
- **Method owner when bound:** D/B design the boundary and the contract; E implements inside its delegation; the "Ask First" decision belongs to the authority that actually owns that action class. This method never approves an action by itself.

## Use

Use when designing or reviewing something that accepts external input, deletes/moves/overwrites, adds an integration or permission, handles personal data, or routes model output into an execution surface. It is an on-demand design aid, not a stage gate; everyday code that touches none of these does not need it.

## Trust follows the writer, not the channel

Untrusted data does not only arrive as an HTTP request, form field, upload, webhook, third-party response, queue message or model output. It also arrives as **another process's command line or environment, a filename on a shared volume, or a path inside a job payload** — values that look internal because the OS handed them over. The test is: *who wrote this value, and what can they make it be?* A value read from the kernel proves where it arrived from, not who authored it.

If you cannot name the trust boundaries of a feature, you are not ready to secure it. Most breaches begin in design, not in a missing string check.

## Five minutes of threat modeling

Write down, before hardening:

1. **Boundaries** — every point where a value crosses from a writer you do not control into a decision you make.
2. **Assets** — what is worth stealing or breaking: credentials, personal data, payment data, admin actions, money movement.
3. **Lenses** — run the six STRIDE questions over each boundary and record the relevant ones: spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege. It is a lens, not a ceremony; two minutes each.
4. **Abuse cases** — next to the use cases, write "how would I misuse this?" and make the first answer a test.

## Three action classes

The classes below are about *which authorization an action needs*, not about how dangerous it feels.

### Always do (inside the task's own scope)

- Validate external input at the boundary where it enters; parameterize queries; encode output for its sink.
- Use the platform's encryption for external transport; hash passwords with a slow password hash.
- Set the security headers the response actually needs; session cookies `httpOnly`, `secure`, and a `sameSite` value that matches the contract.
- Run the ecosystem's native audit against the committed lockfile before release, where the project has dependencies.

### Ask First — the action class needs an authorization that covers it

- adding a new authentication flow or changing authentication logic
- storing a new category of sensitive data (personal, payment, health)
- adding a new external service integration
- changing cross-origin (CORS) configuration
- adding a file-upload handler
- modifying rate limiting or throttling
- granting elevated permissions or roles

"Ask first" means the action needs the authority that owns that class — the policy owner, role, or human the project's valid authority reserves it to. It does **not** mean the executor may self-approve, and it does **not** universally mean "return to a human": where an existing valid policy already delegates that class (a standing upload-review process, an already-approved integration pattern), the action proceeds under that delegation. What is forbidden is treating this method, or the executor's own confidence, as the approval. If you cannot identify who owns the class, that is a recall condition, not a licence.

### Never

- commit secrets to version control
- write secrets, tokens, passwords or full personal data into logs
- treat client-side validation as a security boundary
- disable a security header for convenience
- pass user data into dynamic evaluation or raw HTML injection
- keep a session token in client-readable storage as the auth mechanism
- expose stack traces or internal errors to users

## Operator identity and external channels

When a process acts as, or on behalf of, an operator, ask what actually establishes that identity and what the action's target actually is.

- **The worker can control its own argv, environment and working directory.** Values that look internal for that reason are not a trust source, and the workspace is not necessarily trusted either.
- **An operator flag file proves only its strongest property.** The source establishes the operator through the OS account's home directory (not the environment's `HOME`) plus a non-symlink file owned by the operator with mode `0600`. That is weaker than it reads: if the worker runs as the same UID and can write that home, `0600` does not distinguish the operator from the worker, and the source's own code notes that a stronger boundary is needed. Do not describe this as universally unforgeable, and do not treat a passing test suite (environment spoofing rejected, `HOME` override rejected, symlink rejected, half-configuration rejected) as complete identity security — those tests do not rule out same-user home writes or a forged plan.
- **A workspace pointer can point at a forged plan.** A `--workspace`/plan selection is an input, not an authentication. Schema validity does not authenticate the thread or object coordinates inside the file; the target must come from trusted configuration, not from "the plan exists and its fields are non-empty".
- **Resolve the external target from trusted configuration.** Which channel, thread or object an external write reaches comes from authorized configuration, together with the actor's identity and scope. Without a valid authorization and a trusted target, do not perform the external write (message, deployment, credential change, API call). A half-configured token or target should fail early rather than fall back to a default.
- **Encode a field for the structure it enters.** JSON, shell and templates each need their own encoding; quoting or `JSON.stringify` protects the surrounding syntax, not the meaning of natural-language content. An escaping layer does not prevent prompt injection: the injected text was never a syntax error.
- **Only real isolation constrains actions.** A convention, a marker file or an escaping helper is a convenience layer. The guarantee comes from permissions, credentials and process boundaries the actor genuinely cannot cross. Where a deployment wants this mechanism, the responsible party must verify the host isolation and who maintains the trusted configuration.
- **A stop or pause state is data whose authority comes from elsewhere.** A schema shape or a cached record does not authenticate who may stop, resume or clear it. The surface is often narrower than it reads: pausing new work does not mean every in-flight writer has stopped or been cancelled, and a failed source query or a logged attention line cannot claim the global state. Reading a cached reference back requires the real identity, version and an authorized writer; a wrong or unknown state must not be deleted because clearing is convenient.
- **Channel authorization is checked at both ends.** Enqueue and delivery each re-check the target and the caller's authorization, and a valid grant plus the real recipient, time and scope are still required. A helper whose thread allowlist is optional (undefined simply returns) describes its own configuration boundary, not a universal thread restriction. Client message ids, or dedup on destination + body + sender, do not by themselves provide exactly-once or distinguish two legitimate identical-message intents; an unknown delivery is not blindly resent, and a queue's backoff or "required" flag is not permission to send.
- **An external trigger writes closed or not at all.** Freeze the trusted configuration's source and target coordinates; before any write, re-check the parent, the recipient and the permission, and on failure or an unknown outcome do not fall back to the root or an alternate target. Source data and the execution delegation are separate concerns, and a trusted marker's identity, location and uniqueness qualify the trigger data only — they do not establish the triage fact or authorize a code change. Dedup, link-back and compensation need real semantics; a check before and after a parent operation is not an atomic transaction, and a schema- or config-valid request is neither target authentication nor send permission.
- **Redaction is a clue set plus custody, not a guarantee.** Detecting named assignments, paths or bare commit hashes is useful; an over-length reason is not automatic truncation; and no pattern set covers every personal-data or secret format (a secret inside backticks or JSON needs the real allowlist). Follow `guide-redacted-evidence.md` for the field allowlist and custody. Source limits such as a 2048-character body, a DM ban, a fixed thread or deleting history are not this library's policy.

## Destructive operations on derived paths

A delete, move or overwrite is only as safe as the value naming its target. A shape check ("absolute path, at least one directory deep") proves well-formedness and is routinely mistaken for authorization. Before the call, require **all three**:

1. the resolved target (symlinks resolved, on the resolved path — never the raw string) sits under an allowlisted root;
2. it is at least one level *below* that root, so the root itself is never the target;
3. it carries ownership evidence that was read **before** the operation — and before any teardown that would remove it — so "absent" and "not mine" stay distinguishable.

On refusal: **log the rejected target and stop.** Never fall back to a broader default path; a cleanup routine that falls back is the failure this guards against.

Two honest limits, because the check reads stronger than it is:

- **A marker inside the tree is self-attestation.** Anything that can write to the tree can write the `.owner` marker. The expected owner must come from authenticated state, and the marker needs integrity protection (restrictive ownership or a MAC) before it counts as authorization.
- **Resolving a path and then operating on the name is a check/use race** wherever an untrusted process can swap an ancestor. On a shared volume, hold the target by descriptor with no-follow, beneath-the-root operations, or ensure the hierarchy cannot change for the duration.

**Worktree and scratch cleanup.** Before calling anything disposable, inventory the real objects: refs, tracked work in progress, untracked and ignored files, in-flight use and indirect use. A tool's "safe" bucket is a suggestion, not a permission, and its filters are not exhaustive — a space-split path list, an author filter, a recent-N-days window and a branch match against a possibly stale default branch are heuristics. A merged or closed pull request does not prove the unique changes behind it are droppable (a closed-unmerged PR especially); scratch, untracked or ignored files are not automatically throwaway; an ancestor relationship does not cover every squash/rebase semantic, and neither proves the current consumer has finished. A script that describes itself as read-only can still fetch, update refs and write temporary files: declare its actual effects, because the name is not a permission. Adopt the inventory, recovery, authorization and post-hoc check steps; do not run or port the removal or cache-cleaning tools, and needing evidence beyond the transcript does not grant access to it. Unknown state is retained or investigated; a file suffix never makes something deletable, and a cleanup suggestion is not permission.

## Server-side fetches of user-influenced URLs

For webhooks, "import from URL", image proxies, link previews and similar:

- allowlist scheme and host;
- resolve **all** DNS records and reject any private or reserved address — loopback, link-local (`169.254.169.254`, the cloud metadata endpoint), private and unique-local ranges, IPv4 and IPv6;
- forbid redirects.

Honest gap: this still has a TOCTOU window because the fetch resolves DNS again after the check, so a short-TTL record can rebind to an internal address between validation and connection. For high-risk surfaces, resolve once and connect to the pinned IP, or put a filtering agent in front. Do not describe the allowlist check as eliminating SSRF.

## Dependencies and install scripts

- **Locate the real installation boundary and manager first.** Use the workspace root that owns the lockfile; treat an independent nested project as separate only when it is actually outside that workspace. Corroborate the declared package manager, the lockfile and CI; stop on disagreement or competing lockfiles.
- **Block dependency lifecycle scripts before their first execution.** Bootstrap with scripts disabled or a documented fail-closed policy, inspect the pending script source, approve the minimum, commit that policy, then verify with a clean frozen/immutable install. Never blanket-approve.
- **Audit known advisories; do not confuse that with trust.** An audit matches known advisories and does not catch a newly malicious or typosquatted package. Triage critical/high by **reachability** (runtime, build, test, deploy paths) and by whether a fix exists; preview and test each upgrade rather than applying forced remediation (`npm audit fix --force` and equivalents may cross declared dependency ranges). Document every deferral with a reason and a review date.
- **Tool-specific calls need their support file.** Manager flags, frozen-install semantics, signature checks, and script-approval mechanisms differ by version and product. Verify against the actual manager's documentation for the version in use before copying a command; the source's manager matrix is point-in-time.

## External tools and agent SDKs

- **Pin what the integration actually depends on**: the runtime, the target, the key source, a stable agent/run identifier, and the SDK's supported version. Re-assembling a client can silently drop persisted configuration such as MCP arguments, so check it.
- **Keep the failure axes separate.** A submission failure (nothing started) is not a run that started and ended badly (cancelled, errored, or unknown), and an observation failure is a third case. Record and report which one happened.
- **Check this stage's guarantee before retrying.** A retryable flag or a typed error class is a claim by that layer, not proof of no duplicate execution, and a network failure can leave the outcome unknown. Consult the existing intent record before repeating an effect.
- **Disposal is not proof of remote termination.** Closing or disposing a handle stops what the SDK owns locally; it does not establish that all remote work stopped, and it does not prove zero resource use.
- **Keep the object and the state distinct.** An agent is not a run; an event is not the terminal state; the configuration source is not the effective configuration; and an observation failure is not an execution failure. On resume, check the actual persist/reload boundary — a later send changing something does not mean it changed an in-flight run.
- **A stream or log display does not replace the terminal result.** A finished status does not prove the goal or the artifact qualifies, and an async consumer needs the client's own backpressure guarantee. Do not turn a progress or thinking-event example into a requirement to record internal reasoning or sensitive detail.
- **Least privilege needs real isolation.** A prompt prohibition does not replace removing credentials or write tools, and a read-only name does not waive real effects. When the isolation is insufficient, shrink the work to the existing legitimate single executor rather than expanding privileges by default.
- **Key form is not identity, and each source has its own boundary.** A key's shape cannot tell you whose it is; explicit parameters and environment variables each have a trusted-configuration boundary — do not ban environment configuration wholesale for shared services, and do not adopt a source's key-rotation, key or model defaults. For local/cloud stdio or HTTP, check where the command runs, where the secret goes and who can read it; a source's claim of proxy redaction or cloud safety does not certify the current deployment. Registering an MCP server, `settingSources`, or a resume example carries no account permission, persistence promise, or guarantee of current support.
- Do not adopt source claims that any error means nothing executed, that a retryable flag guarantees no duplicate, that the default cloud runtime isolates every credential, or that personal/team key and model defaults are universal policy. Source API examples do not certify current availability or this task's authorization.

## Personal data

Hardening asks "can an attacker read this?" Privacy asks "should we hold it at all, and for how long?" The cheapest data to protect is the data never collected.

- classify fields as they are added (non-personal / personal / sensitive) — you cannot protect or delete what you cannot find
- collect only against a stated purpose; "might be useful later" is breach scope, not a purpose
- set retention up front, and have a working deletion path for the copies that the applicable policy and legal basis require
- support the data-subject rights the jurisdiction requires (export, correction, deletion) by designing a schema where a person's data is findable and erasable
- where collection or third-party sharing depends on consent, keep that consent auditable; where it rests on another valid basis, state that basis — this method does not decide which basis applies
- make region a configurable policy, not a hardcoded assumption
- keep personal data out of telemetry

Which copies must be erased (including backups, caches, search indexes and analytics copies), whether an obligation is consent-based, and how long a lawful retention may run are decisions for the applicable policy and the responsible professional authority. The operations here are to know where the data is, not collect what the purpose does not need, and keep telemetry clean of it. A lawful retention obligation, or a backup cycle without a feasible per-record deletion, is not automatically a violation: it has to be declared, with its compensating control or its accepted risk.

The legal basis and the specific obligations come from the applicable policy and professional responsibility. This method does not produce a uniform legal conclusion and must not be cited as one.

## Model output and prompts

- **Model/output content is untrusted input**, not a command. Do not hand it to a sink as-is: not to `eval`, an unparameterized query, a shell, raw HTML, or a file path. Parse defensively, validate against a schema, then encode for the sink; where the sink is a query, a shell or a path, the validated value may legitimately be used as a parameter or argument under that sink's own rules, never as raw text.
- **Prompts can be hijacked.** Untrusted text in the context — a user message, a fetched page, a document — can carry instructions. **The system prompt is not a security boundary**; permissions are enforced in code. Keep secrets, other tenants' data and policy information that must not be exposed out of the context window. A legitimate system prompt may appear in a context that genuinely needs it; what must not enter a lower-privilege context is its sensitive content. Scope tool permissions, validate every tool argument, confirm destructive actions, and cap tokens, request rate and recursion depth.

## Examples with their limits

- A `.owner` marker in a directory proves only that something could write there. It is not authorization unless the expected owner comes from authenticated state and the marker has integrity protection.
- Checking DNS before a fetch does not eliminate SSRF; the second resolution can rebind. Pinning or filtering is the mitigation, and even then the claim is bounded by what the filter actually covers.
- A successful authentication proves identity, not permission on a specific resource. Every request needs an authorization check on that resource (the classic IDOR failure: authenticated, but reading someone else's record).
- A public API may legitimately allow cross-origin requests; whether credentials are allowed depends on the contract and must be explicit, not a default.
- **Accepted is not answered, and no error is not cancelled.** A probe that only creates/accepts a session and sends a request, then records success without observing a response, proves at most that the call was accepted — not that the model can complete the task. A cancel whose error is swallowed and which still records success proves nothing about whether the work stopped, whether resources remain, or whether consumption was zero. Claims like "the model completed" or "the task was cancelled" need the corresponding observation.
- **A claim and a "fixed" artifact are checked against the real task and scope.** An artifact can be verified directly; an old pull request is not proof of a current fix, and an existing delegation is not a reason to forbid implementation. An internal setter must not manufacture the symptom on the real user path — local logic or a mapping has its own legitimate observation surface.

## What is not adopted

- The seven "Ask First" classes are not a universal "return to a human" list, and they are not a fence against legitimate pre-approved paths.
- Fixed patterns for every cookie/CORS/header, fixed rate limits or password rounds, mandatory deletion from every backup regardless of the applicable retention or legal basis, mandated agreements as a universal requirement, and a blanket ban on any system prompt in a legitimate context are not adopted. What is protected is secrets, cross-tenant data, and policy information that should not be exposed.
- The source's "rotate a secret first, then purge history" is risk-disposition advice. The action still needs valid authority; do not self-change credentials, policies or history.
- This method does not certify any SDK, manager or platform as fully secure. A copied tool-specific call must be checked against its support file and version.
- Fixed "UI twice", full video/screenshot sets, seven capabilities for every task, draft-only, a unique source reply, silence windows and human-only ownership are that automation's contract, not library gates. A bad configuration closes the affected external writes; a no-UI capability is not a product FAIL and does not block legitimate local work.

## Limits

- No universal control list, no mandatory header set, no fixed numeric threshold, no security gate. Controls follow the boundaries and assets of the actual feature.
- Dependency-upgrade choices, coverage and lockfile handling are review concerns: apply `change-review.md` (dependencies and critical assumptions, findings and disposition) together with this file's dependency-install boundary above. This method does not duplicate that procedure.
- Action permission comes from the task's valid authority and Charter. Naming a boundary or writing a checklist is not approval to act. This method does not grant creating operator flag files, adding credentials, sending to external channels, or lifting an existing restriction; those are actions for the authority that owns them.
- An operator-identity mechanism is host-specific. If a real deployment adopts one, verify the host isolation and the trusted-configuration maintenance rights rather than copying the source's file convention.
- The examples distinguish real observed behaviour (for example, a browser/manager documented behaviour), locally reproduced evidence, and code illustration. A code snippet in a source is not evidence that the same control works in the reader's stack.

## Source anchors

| Source | Retained contribution |
| --- | --- |
| Addy Osmani, `addyosmani-agent-skills` at `2686b620fc1fed2e8f60c704839c766b8594c6b6`, `skills/security-and-hardening/SKILL.md` (`Process: Threat Model First`, `The Three-Tier Boundary System`, `Hardening Controls`, `Dependencies and supply chain`, `Personal data and privacy`, `AI / LLM features`, `Red Flags`) | Trust follows the writer (including local process values); STRIDE as a lens plus abuse cases; the Always / Ask First / Never classes; dependency boundary, install-script gate, audit-vs-trust and reachability triage; privacy as minimization/purpose/retention/deletion; model output untrusted and the system prompt not a security boundary. |
| Same pin, `skills/security-and-hardening/references/hardening-patterns.md` (`Server-Side Request Forgery (SSRF)`, `Destructive Operations on Derived Paths`, `Dependency Audit Triage`) | SSRF allowlist + all-records + no-redirect with the DNS-rebinding TOCTOU stated honestly; destructive-path three conjunctive conditions and the self-attestation / check-use limits; the audit triage tree. |
| Cursor plugins, `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`, `orchestrate/skills/orchestrate/scripts/cli/util.ts` (operator/target boundary), `scripts/cli/task.ts` (run/cancel entry points), `scripts/tools/probe-models.ts` (probe path), `scripts/__tests__/operator-boundary.test.ts` | Worker-controlled argv/env/cwd and non-trusted workspace; the operator-flag convention with its honest weakness (OS userInfo home, non-symlink uid/`0600`; same-UID home writes break it); target resolution from trusted configuration and fail-early half-configuration; per-structure encoding; probe-accepted ≠ model-completed, cancel-error-swallowed ≠ cancelled; green boundary tests ≠ complete identity security. Runtime scripts are not ported. |
| Same pin, `orchestrate/skills/orchestrate/scripts/core/andon.ts` (pause scope, cached ref read-back, state clear), `scripts/core/redact-body.ts` (clue-based detection, length reason), `scripts/cli/comments.ts` (optional allowed thread), `pstack/skills/poteto-mode/scripts/worktree-audit.sh` and `playbooks/worktree-cleanup.md` (inventory buckets, human-gated deletion, read-only claim versus effects, non-exhaustive filters), `cursor-sdk/skills/cursor-sdk/references/error-handling.md` (two failure axes, retryable claim, unknown outcome) | Stop/pause state shape ≠ authority, stop surface scoped to new work, cached read-back needs identity/version/authorized writer, wrong/unknown state not cleared for convenience; channel authorization at enqueue and delivery, optional thread allowlist is that helper's boundary, dedup ≠ exactly-once, unknown delivery not resent; redaction patterns are clues, length is not truncation, custody allowlist required; cleanup inventory versus suggestion, PR/ancestor/scratch heuristics are not proof, declared effects over a read-only name; SDK failure axes separated, retryable is a claim, disposal ≠ remote termination. No Slack message, cleanup run, SDK call or runtime operation is authorized or ported. |
| Same pin, `cursor-sdk/skills/cursor-sdk/references/streaming.md`, `auth.md`, `mcp.md` (config/transport/resume/events), `pstack/automations/benny/skills/triage-issue-reports/SKILL.md` and `pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md` | Agent vs run, event vs terminal state, configuration source vs effective configuration, observation vs execution failure; resume persist/reload boundary and a later send not changing an in-flight run; stream display is not the terminal result and a finished status is not artifact qualification; backpressure per client; disposal/cancel-accepted limits; key form is not identity and each configuration source has its own boundary; command location, secret destination and readers for stdio/HTTP; MCP registration, `settingSources` and resume carrying no account permission or persistence promise; frozen trigger coordinates, write-time parent/recipient/permission re-check, no root or alternate fallback, marker qualifies trigger data only, before/after checks are not a transaction; least privilege via real isolation, prompt prohibition is not removed credentials, insufficient isolation shrinks to the existing single executor. No SDK client, bot, external-write boundary or external write is created or authorized. |

Narrowed or excluded from the sources: the fixed header/CORS/cookie patterns, the fixed rate-limit and password-round numbers, mandatory backup deletion and agreement signing, a blanket ban on system prompts in legitimate contexts, and the universal "all Ask First operations return to a human" reading. The Cursor `orchestrate` runtime scripts, the worktree audit and the cleanup playbook are not ported because no current task consumes them and they would bring their own permissions and dependency boundary — a consumption decision, not a judgment that scripts are worth less. Also not adopted: the SDK's "any error means nothing executed" and "retryable guarantees no duplicate" claims, disposal as proof of stopped remote work, default key/model/cloud-isolation policy, and the benny automation's UI/screenshot/capability/draft/silence/human-owner contract. No `external-write-boundary` method is created and no bot is ported. The operator/action-boundary, cleanup-inventory and external-trigger experience above is retained.

---
# Fixed support: 7357f0b178d0b314c4276e7a213afb81a46f1d79:docs/absorption/2026-10-02/PRO1-DISPOSITION.md

# Oracle · Pro#1 RETURN 处置与有界修订

2026-10-03，Owner 已授权本轮正式吸收后的两次 Pro；第1次已完成，当前1/2。对话 `https://chatgpt.com/c/6abfe3b0-d004-83e8-b850-94bf84148db9`，Pro思考30m39s，结论RETURN。产品对象 `5d7d89d3f8fc295ed7c96e63a2af8952e75398ec` / core `0e7614cd4eec20b4b43b7b0caba43187d3ec10b4`；配套对象 `edce02a9d9341376a1197503bb20720e1fee6fa0`。原回答完整保存在 `ABSORB-PRO1-RESPONSE.txt` / `ABSORB-PRO1-RESPONSE-RAW.json`；问题/附件/record各自保全，不能修改原RETURN。

## 判断

Oracle 定向读回三个承重段落，接受 TPW-PRO1-001～003 为真实正文缺陷：同词accepted被赋予不同性质的含义、未知结果的可合法同键恢复被过宽否定、原始样本波动被错当效果估计不确定性。第三项确实继承了上游过强判断，忠实于源不能免责。

Pro确认本轮已经有操作、条件与反例，不要求再重建责任主轴、角色库、runtime、registry或第43方法；未验证Provider/生产与全源精读不是本版的新阻断。实际读范围以完整回答与附阅读清单为准：核心59全文并独立重建Git树，定向源锚与配套9文件；不称独立重建tar或认证平台/工具链。

## 作者任务与写面

Driver先从固定产品5d7d89d3建新的工作区内修复worktree/分支，保全w1/w2/w3旧对象，不reset/amend/rebase旧历史。复用B3修 release/performance/interface/trust，B2修 external-tool-operation；methods入口历史噪声由Driver按记录单写。避免从旧作者分支整文件覆盖掉后来集成内容。原专业gate2独立核实际固定delta，不代写，不重开已经关闭的原源族。

### TPW-PRO1-001 · 接受与观察分离

- 写面 `methods/release-and-recovery.md` §Use及直接依赖该定义的后文。
- 将当前“accepted=观察到路径工作”改为 observed/verified usable，带对象/版本/观察边界；接受仍是有权责任方或既有有效规则对明确对象作出的接受。F PASS不产生接受，契约接受不证明实现可用。
- 引既有四项分离，不新造发布状态机/表，不默认所有接受回Human。
- 两相反案例：已观察路径通过但保留接受未发生；契约已接受而实现未观察。给实际字段如何记和理由，不需要跑部署。

### TPW-PRO1-002 · 未知结果不是一律禁止原样恢复

- 写面 `methods/external-tool-operation.md` §Bounded execution/partial success，以及与现有interface-contract-and-retry互指的一致性。
- 禁未经确认阶段语义/幂等保证的盲目重复，不禁已获授权、同一意图/键/载荷、保留期有效且服务保证不重复效果的合法查询/重放/协调恢复。
- 服务明确不得重发仍不可绕过；不能换key/金额/目标冒充恢复。现有真实逐动作approval政策继续继承，不把本库一般授权覆盖其有效边界。
- 核允许的响应丢失与不允许的禁重发/保证未知/过期/载荷变化两类条件；回读X Money原文相关段。无需实际支付或Provider网络调用。不要复制完整幂等设计到两个正文。

### TPW-PRO1-003 · 效果估计、样本波动与实际价值分开

- 写面 `methods/performance-and-neutrality.md` §Verify、决策表、尝试例子及重复该结论的句子。
- 不以“3%收益落在±5%原始spread”直接判无收益；适当测量设计下，效果估计的不确定性依赖样本量、配对/相关性、可比性和混杂。能辨识的效果是否值得保留，另外看已接受的实际收益门槛/维护成本/其他目的。
- 证据不足说明改善尚未成立，不自动product FAIL；按现有预算与目的选择继续/暂缓/回退，不规定统一t-test/bootstrap/95%或N。保留正确性与可靠性独立目的，不能被性能neutral一票否决。
- 条件案例：原始分布重叠但均值效果估计足够精确；采样不足/不可比/实质混杂时均值看似改善。Pro构造例（两组各1000、均值100/97、标准差5、独立可比）只作假设说明，SE约0.224ms，不是实际跑分，不把此N当门槛。可用纸面推导/短自有计算核这个反例，无需统计平台或真实性能实验。

## 同批低影响精确化（建议不升must-fix）

- trust-boundary-and-actions：不存在dependency-upgrade独立guide的存在性句改指真实相关章节或删除；probe源锚指真实 `scripts/tools/probe-models.ts`，不为一处旧句新建方法。
- interface-contract-and-retry：把“schema不验证跨字段不变量”的全类别否定限缩为此处shape-only/生成检查不覆盖运行不变量，保留已知runtime refine能力。
- methods/README：已纳入的idempotency/interrogate/code-review不再写为当前deferred；标清历史选择，四旧方法名是否存在与相近机制能力分开，不复活旧接口或建立alias平台。
- 长正文内部导航/历史噪声压缩是非阻断建议；本批不大改组织，不删专业细节，不因字数开第四设计环。其他未列入最终报告的中途疑点不当新阻断。

## 验证、整合、Pro#2与停止

每作者交固定commit/base、实际diff、上述条件例子的判读和源回读，不自报最终PASS。gate2核3个稳定ID及直接受影响关系/上述低影响精确化，保留真实贡献关系；不全库/全源/全脚本重跑，不给每个案例造强制test gate。

Driver串行集成被接受delta，核实际消费/方法引用/状态及冻结Backbone ce82a700不变，保全新core/commit/archive身份和条件证据，给Oracle。Oracle读回并正常push night、ls-remote MATCH后，在同对话发唯一剩余第2笔，范围限定这3个ID、相反案例与直接一致性；非阻断建议不自动成为第二审新gate。

两次结束后记录真实接受/残余与停止；若仍真阻断不能报PASS，也不得自动第三次Pro。无remote-main推送、tag/release、UCBIP修改或外部副作用。当前处置授权来自Owner既有纠错/审核任务，不因Pro本身产生发布权限。

---
# Fixed support: 7357f0b178d0b314c4276e7a213afb81a46f1d79:docs/absorption/2026-10-02/reviews/REVIEW-GATE2-PRO1-002-65d9408.md

# Gate2 · TPW-PRO1-002 定向复核

2026-10-03，tpw-absorb-gate2，非作者。**需一处最小修；002暂不关闭。** 原源族/已关finding不重开，不调用Pro或执行支付/Provider操作。

固定对象 `65d9408b8caa2c9aa8de400214f48822cefe7fe5`，唯一父/base `5d7d89d3f8fc295ed7c96e63a2af8952e75398ec`；实际diff仅external-tool-operation四增四减（Status、§11/12、X Money源表）。diff --check无输出，未读mutable。读PRO1-DISPOSITION的002范围，并核此fixed对象interface-contract-and-retry §4–9/Conditions直接一致性；回读Cursor `ecc249f1e306fc64ddf83c7bed16cacf7c2239db` X Money §Reading payment results及Never，不复裁Oracle源族。该文本仅保存条件证据，不宣实际服务保证。

## 已符合的两类条件（保留通过部分）

- **允许的原样重放案例**：既有有效授权；同一意图、key与payload；有效retention覆盖重投；真实服务对完整副作用保证不重复；仅响应丢失。原请求已执行而回复丢失时，原样重放返回原结果而非再做一次，§12确实允许，不再把所有unknown一律禁止。其保证仍需实际服务证据，例子不是授权或执行事实。
- **禁止的重放反例**：服务明示“accepted but could not confirm ... do not send again”时，即使手上有key也不能绕禁令；防重复保证未知、键窗过期、改payload、换key/金额/目标不能冒充安全原样重放。真实逐动作approval继续生效，一般任务授权不能替它。transient retry亦仍受同段合法恢复条件与host政策，不可凭最后一句绕过。
- **X Money出处精确**：refused永不retry；明确unconfirmed payment不得重发；“could not process ... try again later”原文称nothing moved且fresh approval后retry once；网络失败后very same payment复用key。新源表按这些具名情境记录，没有把源的所有动作approval/一次retry变成全库政策。接口的intent/key/payload/retention实现只互指，无整套设计复制。

## 残余：查询与副作用重放的条件不能一并封锁

§12先定义所有“legal recovery”必须same key/payload、有效retention与service no-duplicate guarantee；随后仅“Under those conditions”允许query/replay/reconciliation，又称expired key/unknown guarantee“is not recovery”。这把**只读查询原操作状态**也置于副作用重放的全部前提之下，与同对象interface §8的query恢复路径及Conditions“read-only operation needs no idempotency key”直接冲突。

反例：原写结果unknown，key去重TTL已过，但服务仍有原operation ID并提供授权范围内的只读status查询。不能再重放原写，因为可能重复；仍可以按该ID读取已完成/拒绝/待处理状态。查询不会重新执行原写，不需要原写的去重TTL继续有效，也不需要先证明原写可安全重放。保证未知时，该查询还可能正是区分状态所需证据；禁查询会妨碍合法恢复。

**最小修只改§12范围**：把same intent/key/payload、有效retention与防重复效果条件明确用于**可能重新施加副作用的原样重放**；只读query/status reconciliation按其自身实际capability、对象身份、权限/成本/数据边界执行，原写键过期或不可重放不自动禁止该查询。任何有副作用的协调/补偿仍须自身真实阶段语义、保证和有效授权，不能借“查询/协调”名重发、换key/金额/目标。保服务禁重发与逐动作approval；无需复制接口设计、建恢复平台或实际支付测试。

## 下一合法动作

Driver保全上述允许/禁止反例与X Money回读证据，送该单段限缩后的新fixed对象；gate只核此残余与直接一致性，其他已符合部分不重做。当前整文件暂不集成作002关闭依据。文本修订通过后仍不代表实际provider exactly-once/当前policy/支付授权或全包接受。

---
# Fixed support: 7357f0b178d0b314c4276e7a213afb81a46f1d79:docs/absorption/2026-10-02/reviews/REVIEW-GATE2-PRO1-002-21bd9cd.md

# Gate2 · TPW-PRO1-002 残余关闭

2026-10-03，tpw-absorb-gate2，非作者。**external-tool-operation.md PASS；TPW-PRO1-002 CLOSED。** 沿65d9408 review保留原样重放/禁重发两类条件与X Money回读证据，不重开源族/其他已关finding、轮次或贡献。

固定对象 `21bd9cd938a7a2927886077b93e5299975fc50d5`，唯一父 `65d9408b8caa2c9aa8de400214f48822cefe7fe5`，基线仍 `5d7d89d3f8fc295ed7c96e63a2af8952e75398ec`。实际父delta仅§12一行替换，diff --check无输出。核该句及上一对象已读同基线interface §8/Conditions的直接一致性；本次未改接口/X Money，未读mutable或运行Provider/支付。

- **重放的条件**明确限定可重新施加副作用的same-request replay/recovery：已有授权、同intent/key/payload、retention覆盖、真实no-duplicate保证；响应丢失时可返回原结果，不再把unknown一概禁止。
- **查询的条件**独立：按原operation identity只读status，在自身actual capability/object/permission/cost/data边界内执行。原写key过期或写不可安全重放不自动禁止查询，unknown时可据此区分状态，符合interface §8 query与read-only无需key。
- **负例保**：服务明示不得重发、保证未知、key窗过期、payload变化不允许重放；不得换key/金额/target冒充恢复。真实逐动作approval继续生效，一般授权不覆盖provider政策。
- **协调/补偿不偷渡**：有副作用的reconciliation/compensation须自身阶段语义、保证与有效授权，不因称query而重发或自改意图；幂等实现仍只指interface，没有复制设计或创建平台。

条件证据：写响应丢失且原key/完整副作用保证有效时，原样replay可成立；写key过期但原ID的只读status仍可查时，只允许该授权查询而不能以此再次写；X Money明确unconfirmed不得重发仍阻断replay，保该源fresh approval与network同key具名情境。均为纸面判读，非实际服务保证/支付结果。

Driver可串行集成此fixed external整文件，并将本记录与上一review条件证据交Oracle。001已关与003当前未决分别保全，不能由002关闭代其通过。本gate未调用Pro、派工、写产品或stage/commit；全包接受、真实provider行为/授权仍不由本文产生。

---
# Fixed support: 7357f0b178d0b314c4276e7a213afb81a46f1d79:docs/absorption/2026-10-02/reviews/REVIEW-GATE2-PRO1-001-003-054b30c.md

# Gate2 · Pro#1 001/003与低影响精确化

2026-10-03，tpw-absorb-gate2，非作者。**release/interface/trust三文件PASS；TPW-PRO1-001 CLOSED。performance需两句局部限缩，TPW-PRO1-003未关闭。002仍依其独立固定审单未决，不在本对象替其关闭。** 旧源族、已关finding、轮次与贡献保持；本gate不调用Pro。

固定对象 `054b30ce3b91b1c31ba535d1bf3007dda21fbec6`，唯一父/base `5d7d89d3f8fc295ed7c96e63a2af8952e75398ec`；actual diff仅四methods，diff --check无输出。对照PRO1-DISPOSITION 001/003及其低影响建议，读fixed相关正文/直接依赖，不读mutable或重新全库审。回源资格沿已直接核Addy `2686b620…` performance/shipping与Cursor `ecc249f1…` schema/refine/probe，此次直接核源performance的“3%/±5%”原句与probe-models全文；低影响建议不升新must-fix。

## 文件级结论

| 文件 | 结果 | 理由与边界 |
| --- | --- | --- |
| release-and-recovery | PASS；001 CLOSED | deployed/enabled/observed-or-verified usable/shut down分开；观察带对象/version/path/time/conditions/evidence或gap。接受是有权责任方/有效规则对明确对象的动作，记录acceptor/rule/time/scope，不从F PASS或“看起来能用”推接受；有效委托可接受，不默认Human。观察与接受字段分别记，不建状态机；后文观察与风险/发布权限保持。 |
| trust-boundary-and-actions | PASS；低影响精确化通过 | 删除不存在独立dependency-upgrade guide的存在性承诺，指change-review的真实dependencies/assumptions/findings disposition与本文件install边界，不复制程序/权限。probe源定位到实际`scripts/tools/probe-models.ts`：create/send后记ok、cancel异常吞掉的承重代码存在，仍只支持accepted≠completed/吞error≠cancelled；未运行probe、未认证model资格。 |
| interface-contract-and-retry | PASS；低影响精确化通过 | §3以shape-only检查/生成视图与runtime refine/superRefine实际能力分开，后文明确Plan runtime图检查不自动进入generated artifact；不再用“schema全类别不能跨字段”否认已知runtime能力。按该段shape-only上下文消费，不将所有schema/generator都认证或否认。无新validator或schema adopter政策，Oracle旧源裁不重开。 |
| performance-and-neutrality | 大部修复通过；003仍有局部残余 | 样本量/配对相关/可比性/混杂、usable estimate与价值阈值分开、inconclusive非产品FAIL、按预算continue/defer/revert、可靠性/正确性独立目的、无统一统计工具/N均正确；但新增band句仍从原spread推出证据不足，且repeat必要一概化，见下。 |

## 001 条件证据（纸面判读，不宣部署）

- **已观察、未接受**：对象build H、路径P、时点T、条件C下canary/关键流观察通过，record可写observed H/P/T/C/evidence；保留接受未发生，accepted记录为未发生/待相应authority。不能以F PASS填acceptor或授发布权。
- **契约已接受、实现未观察**：接受的是契约K/version V，由实际B/C接受委托或既有效规则记录时间/scope；implementation build H尚无运行证据，其observed为未核/gap。K的接受不是H可用证据。正文已明确对象种类/范围，不把这两项折成“accepted实现可用”。

这与fixed Backbone的contract acceptance≠evidential verification≠action authorization≠task closure、title不产生接受权直接一致；字段只是已有记录内容，不新建接受actor/表。

## 003 算术与相反案例

按Pro hypothetical既定条件计算：两独立可比组各n=1000、均值100/97 ms、SD各5 ms，`SE_diff = sqrt(25/1000 + 25/1000) = 0.22360679775 ms`，`3/SE = 13.4164`。本gate只用短自有算术核值，未采样/跑分；结果不是普遍N门槛、固定检验法或因果资格。

- **原始分布重叠但估计可用**：在独立/可比/无实质混杂的明确条件下，3 ms mean difference的不确定性可远小于原始5 ms spread，能支持这个受限平均差claim。是否值得keep还看接受的收益阈值/维护成本与其他目的，不由13.4 SE自授决策。
- **均值看似改善但估计不成立**：样本过少、相关结构未处理、冷/热cache不一致、另一个变更/负载同时变化等，可产生均值移动而不能支持所称效果。报告improvement未成立，按已有预算与目的继续/暂缓/回退；不产品FAIL、不因貌似mean更好自动keep。

正文两个条件例及决策表大部能区分上述情况；source的过强原句不能因忠实于Addy而免责，此次修订应保其拒绝记录。

## 003 残余最小修（仅§Verify新增bullet）

1. **band仍被赋予证据不足的结论**：新句“3% inside ±5% ... not by itself verdict no benefit: **it says the evidence as collected cannot establish the improvement** ...”仍由两个裸数推出cannot establish，与后面的n=1000算例直接冲突。最小修：**仅凭这两个裸数不能判断改善已建立、未建立或无收益**；需要效果估计/不确定性与设计条件。不应把“不够信息判断”写成“已判断证据不足”。保usable estimate与实际价值两轴，不全文重写或新统计gate。
2. **Repeating is necessary过宽**：同一bullet新写“Repeating the measurement is necessary”，未限定有噪声/估计稳定收益claim，与同文件已过Ground条款“固定输入一次计数可以支持窄count claim”直接冲突。最小修：按claim、已知噪声/变异与coverage选择所需重复和设计；对需要估计噪声/稳定收益者取适当重复，确定性窄count观察不一律要求额外run。保无fixedN、统计效果不确定性/混杂、已有授权/预算stop，不重开旧单run finding或ABC8源族。

memoize例需沿此解释：其“this sample effect not established”是案例已知的估计/设计不足，不能仅由±15 spread推出；可把该案例假定的不足写明，或去掉spread作为理由的歧义，不另造实验。其他decision/complexity/other-purpose已改内容保留，不因这两句重做。

## 交付与下一合法动作

Driver可逐文件串行集成release/interface/trust三个PASS，保001上述条件例与算术证据给Oracle；performance待上述两句的fixed窄修后定向核，003暂不关。002的只读query残余依独立review处理，不能由本四文件PASS代关。当前文字资格不认证真实统计设计/Provider/production/部署或全包接受。只写自有reviews，未产品写入、派B、stage/commit或扩大审查。

---
# Fixed support: 7357f0b178d0b314c4276e7a213afb81a46f1d79:docs/absorption/2026-10-02/reviews/REVIEW-GATE2-PRO1-003-5353588.md

# Gate2 · TPW-PRO1-003 残余关闭

2026-10-03，tpw-absorb-gate2，非作者。**performance-and-neutrality.md PASS；TPW-PRO1-003 CLOSED。** 001/002既有CLOSED保持，旧源族/单run/性能召回/轮次与贡献不重开。

固定对象 `535358837b92f7c98d526cf3fc1f4d99996c62d7`，唯一父 `054b30ce3b91b1c31ba535d1bf3007dda21fbec6`，base `5d7d89d3f8fc295ed7c96e63a2af8952e75398ec`。实际父delta仅performance +2/-2（§Verify bullet及memoize表行）；diff --check无输出，其他三文件与已过决策/可靠性/条件例未变。只核三处语义与直接一致性，沿上一review实际来源回读/算术证据，不读mutable或实际跑分。

- **裸数不下判决**：3%与±5%两数不能单独决定改善已建立、未建立或无收益；按measurement design中的效果估计/不确定性及claim需要判断。与紧接的重叠分布但估计可用、采样/可比性/混杂不足两个条件案例一致，不再从原spread推证据不足。
- **重复按claim选择**：所需设计/重复按已知noise/variation/coverage；固定输入确定性窄count单run可支持，估噪/稳定收益取适当重复。保无fixedN/统计工具gate与已有单run专业结论，不将概率估计方法强加所有测量。
- **实际价值另轴**：memoize示例明确5 ms低于该claim已接受的收益阈值，而非±15 ms原spread推出未建立；这是台账示例的明确条件，不是源跑分、普遍阈值或当前产品事实。与usable estimate/accepted threshold/maintenance cost及其他可靠性/正确性目的分离一致，未偷改真实目标。

条件证据沿054b30c review保全：假定两独立可比组n=1000、mean100/97、SD5，SE_diff≈0.2236068 ms、3 ms≈13.416 SE，仅算术示例，非benchmark/N门槛/自动因果或keep决定；不可比或实质混杂的mean移动仍不能支持所称效果，按已有预算/目的continue/defer/revert，非产品FAIL。性能neutral不否决独立已接受的可靠性/正确性目的。

Driver可串行集成此fixed performance整文件，并把本记录与054b30c/002条件证据交Oracle读回。本gate送审的Pro#1三个稳定ID均已专业关闭；集成字节/引用闭合、后续Oracle/Pro#2及最终接受仍由其实际责任持有，不由本PASS产生。未调用Pro、派工、写产品、stage/commit或运行性能/Provider/生产实验。
