# Performance investigation and neutrality · candidate method body

- **Status:** candidate distilled under `docs/absorption/2026-10-02/reviews/ORACLE-REVIEW-A1-ADDY-CD.md` (C9, 2026-10-02, source `addy@2686b620`); not yet an accepted reference; creates no authority, trigger, or gate. A fixed-diff review still applies. The source's cache/query/pool detail branches are handled by the separate EF-addendum ruling and are not merged here.
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

"Slow" is not a diagnosis. The decomposition says which of the available measurements can discriminate.

## Common bottlenecks and the conditions that decide them

- **N+1 reads.** One query per row where a join/batch would do. Evidence: the query log or trace shows repeated statements. Fix: fetch in one round trip; verify the count dropped.
- **Unbounded reads.** A list endpoint returning everything. Fix: pagination or a limit; a bounded read is also what protects the database from the caller.
- **A query that ignores its index.** "Add an index" is the guess; the query plan is the measurement. Read `EXPLAIN`-equivalent output for the plan shape (sequential scan where an index was expected, estimates far from actuals indicating stale statistics, a sort above the scan). Index the shape of the query — equality columns before the range/sort column. Know when an index will not help: low selectivity on the dominant value, a leading-wildcard match, a function applied to the column, and write-heavy tables where every index taxes every write. **An unchanged plan does not by itself prove the index is worthless**: check what the plan was measured on (statistics freshness, parameter values, actual load, the tested query shape) and measure the write cost. The specific benefit depends on the actually tested load and write cost; if it stays unexplained, do not keep it as a neutral change.
- **Connection-pool exhaustion.** The signature is every endpoint slowing at once, the slow time spent waiting for a connection, and a mostly idle database. A pool larger than what the database can execute concurrently just relocates the queue somewhere less visible — bigger is not faster. Find what holds connections; where instance count is unbounded, a multiplexing proxy is the usual fix, not a higher maximum.
- **Frontend.** Images (format, responsive sizes, explicit dimensions, priority vs lazy loading), render-blocking work, unnecessary re-renders, and bundle growth. Each has its own measurement; a bundle-size reduction is not a user-experience result until the user-facing metric moves.
- **Caching.** Cache what is expensive to produce and read far more often than it changes. A layer (in-process, shared, CDN/edge) has visibility, staleness and invalidation costs that differ. **The key must include every input the response depends on** — tenant, locale, viewer, permissions, feature flags — and the acceptable staleness window and one invalidation strategy must be stated. **The rule about sensitive data is not a blanket ban**: when staleness would break this task's correctness and there is no provable coordination guarantee, do not honour the promise with a TTL. Otherwise state the window. (Cache design detail is merged from the EF-addendum branch, not repeated here.)

## Verify: same conditions, one change, beat the noise

- **Re-measure the way the baseline was measured** — same command, same data, same environment, same budget. A cold-cache baseline compared with a warm-cache result measures the cache, not the change.
- **Change one thing at a time.** Several optimizations landed together produce one number and no attribution. If they must ship together, measure each in isolation first.
- **Beat run-to-run variance, not just the mean.** Repeat the measurement and compare the delta to the observed spread. A 3% gain inside a ±5% spread is a different sample, not a gain.

Decision table:

| Result versus baseline | Action |
| --- | --- |
| past the stated threshold and correctness checks green | **keep**, with the before/after numbers recorded |
| within run-to-run noise (no measurable change) | **revert** — "neutral" is a revert, not a keep |
| worse | **revert** |
| improved but a correctness check went red | **revert** — a regression wearing a win's clothing |

A result inside the noise band is **not a product FAIL**. It is an unproven performance improvement, and (absent another accepted purpose) the change reverts rather than accumulating maintenance cost for nothing.

**Correctness gates the metric.** An "optimization" that wins by dropping work the product needed — skipping a validation, caching something that must be fresh, removing a load-bearing wait — is a regression, not a win. Do not manufacture a performance number by removing a correctness check.

## Keep a ledger of attempts

Reverted work leaves no trace in version history, which is exactly why the same dead idea is tried again later. Record every attempt — kept and reverted — with the numbers and the reason:

| Idea | Baseline → result | Verdict | Why |
| --- | --- | --- | --- |
| memoize the row component | INP 240 ms → 235 ms | reverted | inside noise (±15 ms); rows were not the bottleneck |
| virtualize the list | INP 240 ms → 90 ms | kept | long tasks gone from the trace |
| preconnect to the API origin | LCP 2.8 s → 2.8 s | reverted | already same-origin |

A section in the change description or a file in the repo both work; what matters is that the next person reads it before proposing the experiment again.

## Complexity must pay for itself — without vetoing other purposes

Code that is kept is maintained forever. When a change adds complexity solely for performance and produces no significant measured benefit, **revert or defer it**. But if the same change also serves an already-accepted reliability or correctness purpose, evaluate it by that purpose: a neutral performance measurement does not by itself veto it. State which purpose is being claimed.

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
- This method does not grant permission to add load, change production configuration, or alter caching policy; those actions follow the task's authorization.

## Source anchors

| Source | Retained contribution |
| --- | --- |
| Addy Osmani, `addyosmani-agent-skills` at `2686b620fc1fed2e8f60c704839c766b8594c6b6`, `skills/performance-optimization/SKILL.md` (`Overview`, `The Optimization Workflow` steps 1–5, `Where to Start Measuring`, `Step 2: Identify the Bottleneck`, `Step 3` anti-patterns, `Step 4: Verify`, `Log every attempt`, `Step 5: Guard Against Regression`, `Common Rationalizations`, `Red Flags`) | Measure before optimizing; symptom decomposition; synthetic vs field evidence; the common bottlenecks with their deciding measurements; same-condition re-measurement, one change at a time, beat the noise; the four-way keep/revert decision including "neutral is a revert"; correctness gating the metric; the attempt ledger; guarding the user-facing metric. |
| Same pin, `references/performance-checklist.md` (`Frontend Checklist`) | The `no-store`/bfcache item, kept as a version-limited example and corrected against the browser vendor documentation above. |
| Chrome for Developers, `https://developer.chrome.com/docs/web-platform/bfcache-ccns` (published 2024-10-21, updated 2025-09-09) | The actual Chrome bfcache/no-store behavior, its conditions, the enterprise opt-out, and the explicit note that other browsers may still block these pages and that minimizing `no-store` remains best practice. |

Narrowed from the source: the fixed metric/budget values, "always use both synthetic and RUM", "the plan not changing means the index is worthless", and the unconditional list of things that must never be cached.
