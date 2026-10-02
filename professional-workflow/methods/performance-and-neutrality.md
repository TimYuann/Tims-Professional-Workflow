# Performance investigation and neutrality · candidate method body

- **Status:** candidate distilled under `docs/absorption/2026-10-02/reviews/ORACLE-REVIEW-A1-ADDY-CD.md` (C9, 2026-10-02, source `addy@2686b620`), extended under `docs/absorption/2026-10-02/reviews/REVIEW-GATE2-A2R-CURSOR-ABC8.md` (MG1/MG2, 2026-10-02, source Cursor `ecc249f1`), and further extended under `docs/absorption/2026-10-02/reviews/REVIEW-GATE2-A1-ADDY-EF-ADDENDUM.md` (P1–P9 performance/cache/query/pool branches, 2026-10-02, source `addy@2686b620`); not yet an accepted reference; creates no authority, trigger, or gate. A fixed-diff review still applies. This file is the single carrier for performance evidence; no second perf-evidence file or registry is created.
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
- **Beat run-to-run variance, not just the mean.** Repeat the measurement and compare the delta to the observed spread. A 3% gain inside a ±5% spread is a different sample, not a gain.

Decision table:

| Result versus baseline | Action |
| --- | --- |
| past the stated threshold and correctness checks green | **keep**, with the before/after numbers recorded |
| within run-to-run noise (no measurable change) | **revert** — "neutral" is a revert, not a keep |
| worse | **revert** |
| improved but a correctness check went red | **revert** — a regression wearing a win's clothing |

A result inside the noise band is **not a product FAIL**. It is an unproven performance improvement, and (absent another accepted purpose) the change reverts rather than accumulating maintenance cost for nothing.

A comparison that measures the **wrong surface**, or comes out **inconclusive**, is not a PASS either. An inconclusive run does not confirm the fix, and a green result on a surface other than the claimed one does not establish the claim. A previously valid observation may be reused while its conditions still hold; an untested ceiling cannot be claimed as the limit.

**Correctness gates the metric.** An "optimization" that wins by dropping work the product needed — skipping a validation, caching something that must be fresh, removing a load-bearing wait — is a regression, not a win. Do not manufacture a performance number by removing a correctness check.

## Keep a ledger of attempts

Reverted work leaves no trace in version history, which is exactly why the same dead idea is tried again later. Record every attempt — kept and reverted — with the numbers and the reason:

| Idea | Baseline → result | Verdict | Why |
| --- | --- | --- | --- |
| memoize the row component | INP 240 ms → 235 ms | reverted | inside noise (±15 ms); rows were not the bottleneck |
| virtualize the list | INP 240 ms → 90 ms | kept | long tasks gone from the trace |
| preconnect to the API origin | LCP 2.8 s → 2.8 s | reverted | already same-origin |

A section in the change description or a trail the repository already keeps both work; reuse the existing trail rather than creating a second registry, and do not require a commit per attempt. Each record names the actual object, the command or harness that produced the numbers, the measure and threshold, the verdict and reason, and what the observation does not cover — kept, reverted or deferred.

## Complexity must pay for itself — without vetoing other purposes

Code that is kept is maintained forever. When a change adds complexity solely for performance and produces no significant measured benefit, **revert or defer it**. But if the same change also serves an already-accepted reliability or correctness purpose, evaluate it by that purpose: a neutral performance measurement does not by itself veto it. State which purpose is being claimed, and remember that a green test result certifies the checks that ran, not every commitment the change retained.

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
| Addy Osmani, `addyosmani-agent-skills` at `2686b620fc1fed2e8f60c704839c766b8594c6b6`, `skills/performance-optimization/SKILL.md` (`Overview`, `The Optimization Workflow` steps 1–5, `Where to Start Measuring`, `Step 2: Identify the Bottleneck`, `Step 3` anti-patterns, `Step 4: Verify`, `Log every attempt`, `Step 5: Guard Against Regression`, `Common Rationalizations`, `Red Flags`) | Measure before optimizing; symptom decomposition; synthetic vs field evidence; the common bottlenecks with their deciding measurements; same-condition re-measurement, one change at a time, beat the noise; the four-way keep/revert decision including "neutral is a revert"; correctness gating the metric; the attempt ledger; guarding the user-facing metric. |
| Same pin, `references/performance-checklist.md` (`Connection pooling`, `Query plans`, `Index strategy`, `Caching Strategies` incl. read/write patterns, negative caching, request coalescing and the cache checklist, `Frontend Checklist`) | Pool capacity across all competing consumers and headroom, diagnosis before resizing, bounded wait/timeouts, unbounded autoscaling and proxy caveat; index-change plan reading with baseline plan, estimate/sort signals, composite-order and write-cost conditions, and non-automatic revert; cache selection evidence, key equivalence classes, invalidation/staleness ownership, negative results versus origin errors, in-flight coalescing with lock/stale-while-revalidate caveats, memory ceiling and hit-rate nuance; layout reservation via dimensions and fallback font metrics verified at the real viewport. The `no-store`/bfcache item remains a version-limited example corrected against the vendor documentation above. |
| Chrome for Developers, `https://developer.chrome.com/docs/web-platform/bfcache-ccns` (published 2024-10-21, updated 2025-09-09) | The actual Chrome bfcache/no-store behavior, its conditions, the enterprise opt-out, and the explicit note that other browsers may still block these pages and that minimizing `no-store` remains best practice. |
| Cursor plugins, `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`, `pstack/skills/poteto-mode/playbooks/hillclimb.md` and `pstack/skills/poteto-mode/playbooks/perf-issue.md` | Harness sensitivity proven before it is trusted; workload/architecture grounding and a reproducing case; falsifiable target and stop condition from the real authority; repeat under controlled conditions with warmup/cache/order/sample/noise and a negative control; one explainable hypothesis per change; kept/reverted/deferred records that reuse the existing trail; the eight strategy families as mechanism-grounded optional hypotheses with per-family win conditions; a trace shows what is slow, never what is safe to delete. |

Narrowed from the sources: the fixed metric/budget values, "always use both synthetic and RUM", "the plan not changing means the index is worthless", and the unconditional list of things that must never be cached; the hillclimb attempt/improvement floors, fixed N-median requirement, per-fix commit and freeze-never-change rules; and any requirement to run a profiler or capture before proposing a labelled hypothesis. The Cursor playbooks are not ported as scripts or runtime; only the measurement discipline above is retained.
