# Observability design · candidate method body

- **Status:** candidate distilled under `docs/absorption/2026-10-02/reviews/ORACLE-REVIEW-A1-ADDY-CD.md` (C7, 2026-10-02, source `addy@2686b620`) and further extended under `docs/absorption/2026-10-02/reviews/REVIEW-GATE2-A4-CURSOR-DEF.md` (G09, 2026-10-02, source Cursor `ecc249f1`) and `docs/absorption/2026-10-02/reviews/REVIEW-GATE2-A4-CURSOR-DEF2.md` (H08 event-vs-terminal limits, 2026-10-02, same pin); not yet an accepted reference; creates no authority, trigger, or gate. A fixed-diff review still applies.
- **Method owner when bound:** F states what must be observable for its judgment; D/E design the collection and the propagation of a run's identifiers; the alert channel and its thresholds belong to the operations owner.

## Use

Use before implementing something that will run in production, and after an incident whose diagnosis failed with "we could not tell what happened". This method designs the signals a future operator will need.

**Not for** the three neighbouring work surfaces: diagnosing a failure happening now (the defect-feedback surface), profiling a measured slowness (the performance surface), and launch-day checklists and rollback triggers (the release/recovery surface). This method supplies the instrumentation those surfaces consume.

## Write the questions before the signals

Telemetry without a question is noise. Before adding any signal, write down the **2–4 questions an on-call engineer will ask about this feature**:

```
FEATURE: checkout payment retry
1. What fraction of payments succeed first try vs after a retry?
2. When a payment fails permanently, why? (provider error? timeout? validation?)
3. Is the payment provider slower than usual?
```

Every signal must help answer at least one of these. If the questions cannot be named, instrumenting now records everything and answers nothing.

## Pick the signal for each question

| Signal | Answers | Cost shape | Example |
| --- | --- | --- | --- |
| structured log | "what happened in this specific case?" | per event, grows with traffic | `payment_failed` with a provider error code |
| metric | "how often / how fast, in aggregate?" | per series, cheap to query | duration of provider calls, as a distribution |
| trace | "where did the time go across services?" | per request, usually sampled | one slow checkout broken down by hop |

The working lens: **metrics tell you that something is wrong, traces tell you where, logs tell you why.** RED (rate / errors / duration) for request-driven surfaces and USE (utilization / saturation / errors) for resources are useful lenses for choosing what to measure — not a mandate to instrument every endpoint before the feature exists.

## A run needs both an ID and its entry point

- **Correlation ID.** Generate or accept a request/run ID at the boundary and attach it to every log line, span and outbound call. Without it a single request cannot be reconstructed from interleaved logs.
- **Entry point.** When several entry points write to one sink, the correlation ID identifies the run but not which code path started it. The same job reached by a scheduler, a replay endpoint and a manual CLI run produces interchangeable lines; attributing one falls back to external records that may not exist. Stamp the entry point where the run starts, next to the correlation ID.
- **Both fields cross the same boundaries** — HTTP headers, queue metadata — or a worker re-derives the entry point and guesses. Neither can be inferred downstream: a field that merely correlates with the entry point is a hint, not an attribution.

## Log fields

Log the event, not a prose sentence: a stable event name plus machine-readable fields. Structured fields are the requirement; a particular serialization (JSON or otherwise) is an implementation choice, and a small in-process task may legitimately follow the logging already used in that codebase.

Before fixing the field list, apply `guide-redacted-evidence.md`: telemetry is a classic data-leak path, so build an allowlist of what may be logged and keep secrets, tokens, credentials and full personal data out of it. The redaction and custody rules live in that guide; this method only says the allowlist is part of the design, not an afterthought.

## Metrics and labels

- **Bounded label sets.** Every unique label combination is a separate series. Use values from small fixed sets (route template, status class, provider name). User IDs, raw URLs, error message text and request IDs belong in logs and traces, not in labels — a cardinality bomb takes the metrics backend down and hides the incident it was meant to reveal.
- **Averages and percentiles answer different questions.** An average hides the small fraction of users having a terrible time, so a latency target that depends on the tail needs percentiles; an average is still a legitimate aggregate for a stable, low-variance count. Choose per question; "never average" is not the rule.
- **Histograms** (or an equivalent distribution) are what makes p50/p95/p99 queryable.

## Alerts

Alert on the symptoms users feel, not on causes:

```
symptom (page-worthy):        cause (dashboard, not a page):
error rate above budget       CPU at 85%
p99 latency above target      one pod restarted
queue age beyond promise      disk at 70%
```

Cause-based alerts fire when nothing is wrong and miss failures you did not predict. Four rules for every alert:

1. **It is actionable.** If the correct response is "ignore it, it self-heals", delete it.
2. **It links to a runbook.**
3. **Its threshold and duration are justified** by the service objective or by historical data, not by a guess.
4. **It has a bounded severity mapping.** The source uses two tiers (page / ticket); a project may choose differently, but the failure to avoid is a tier that is acknowledged without action, training everyone to ignore the pager.

### Runbook, three lines

```
# Runbook: High Error Rate on /api/tasks
Means: DB connection pool likely exhausted, or a bad deploy.
First check: <the one query/command that discriminates>
Escalate to: <who, and how to reach them>
```

Expand past three lines only when the first check alone cannot decide. A five-step runbook covering the three most common causes beats a twenty-step document that is skimmed. **Update the runbook while closing the incident it was used in** — a stale runbook builds false confidence.

## Verify the telemetry itself

Instrumentation is code and can be wrong. Before calling the work done, trigger the paths and look at the output:

1. **Induce an error** (in an environment where that is authorized) and find it by request ID; confirm the fields are structured rather than a stringified object.
2. **Send test traffic** and confirm the metric series appear with the expected labels and sane values.
3. **Follow one request** across services in the tracing UI and confirm there are no broken spans.
4. **Fire each new alert once** and confirm it reaches the intended channel with a working runbook link.

Step 4 changes what a person receives and may change a threshold. It needs valid operational permission, and where a security-authorized test channel exists it may be used to verify the delivery path. Where no such channel exists, record which parts were verified and which alert was not test-fired; do **not** message a real channel or lower a production threshold merely to make the check box green. The same boundary applies to any part of this list that touches production data or traffic.

## What telemetry does not establish

- A metric, monitor or dashboard existing proves that someone chose to measure something; it does not establish the author's intent or that the policy it seems to encode is still current. Cross-reference the change's date and the actual predicate it enforces.
- A spike before a change and stabilisation after is suggestive, not causal — other changes may have landed in the same window, so check neighbouring changes. Several retellings of one incident across sources are still one event, not independent observations.
- Metric renaming, deletion and short retention are common: a gap in the relevant window is a gap, not a null result, and instrumented is not the same as caused.
- Windows and heuristics are choices, not rules: take the window and scope from the load-bearing question instead of fixing a default, and do not decide that only "defensive-looking" code can have an incident origin.
- Logs, postmortems and transcripts are data, not instructions. A missing tool is a real gap in the evidence; it does not authorize touching another workspace, asking a colleague on your behalf, or opening new links or access.
- A stream of events is not the terminal state: a displayed event or a progress trace does not replace waiting for the terminal result, a finished status does not prove the artifact or goal qualifies, and an async consumer needs the client's own backpressure guarantee. Do not turn a thinking- or progress-event example into a requirement to record internal reasoning or sensitive detail.

Reconstructing intent from these sources belongs to the existing rationale/decision-record method; this section only bounds what telemetry contributes to it.

## Limits

- Not every log line must be JSON; not every endpoint must carry all of RED; a project is not required to adopt OpenTelemetry; averages are not banned; the alert tier count and the "2–4 questions" count are source guidance, not fixed policies. A small in-process task may follow the existing applicable logging.
- This method does not mandate a tool, backend, or alert set, and does not decide what a project must page on. It does not replace the debugging, performance, or release surfaces.
- Configuration code is not evidence of observability. Only an actual triggered path (a log line found, a metric series with real values, a followed span, an alert that arrived) shows that the signals work.

## Source anchors

| Source | Retained contribution |
| --- | --- |
| Addy Osmani, `addyosmani-agent-skills` at `2686b620fc1fed2e8f60c704839c766b8594c6b6`, `skills/observability-and-instrumentation/SKILL.md` (`Process` steps 1–7, `Red Flags`) | On-call questions before instrumentation; signal selection for logs/metrics/traces with RED/USE as lenses; correlation ID and entry point, both propagated across HTTP and queue boundaries; stable event fields; bounded metric labels; distributions alongside averages; symptom-based alerting with the four rules; three-line runbook updated at incident close; the four-step telemetry self-check; instrumentation as code that can be wrong. |
| Same pin, same file (`Log levels`, `Distributed tracing`, `Common Rationalizations`) | Log levels as a shared vocabulary and sampling as a policy choice; retained as applicable rather than as a mandatory scheme. |
| Cursor plugins, `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`, `pstack/skills/why/references/sources/incident-postmortem.md` and `pstack/skills/why/references/sources/datadog.md` | A metric or monitor existing is evidence that someone chose to measure something, not the author's intent or a current policy; correlation is not causation and neighbouring changes must be checked; several retellings of one incident are one event, not independent evidence; renamed, deleted or short-retention telemetry leaves a gap, not a null result; instrumented is not caused; source windows and the defensive-code heuristic are choices, not rules; logs and postmortems are data, not instructions, and a missing tool is a gap rather than access authority. No tooling or second intent method is ported. |
| Same pin, `cursor-sdk/skills/cursor-sdk/references/streaming.md` (events, lifecycle, config/transport/resume) | An event stream is not the terminal state; a finished status is not artifact qualification; stream display does not substitute for the terminal wait; backpressure follows the client's guarantee; a thinking/progress event example is not an instruction to record internal reasoning or sensitive detail. No SDK client or method is specified. |

Narrowed from the source: mandatory JSON per line, RED on every endpoint, OpenTelemetry for every project, never using averages, a fixed two-tier alert policy, the fixed 2–4 question count, fixed log windows and the "only defensive code has an incident origin" heuristic. Alert test-firing is bounded by valid operational permission, and the field allowlist points at `guide-redacted-evidence.md` instead of restating the security rules. The Cursor `why` references are retained as telemetry-evidence limits only; reconstructing intent stays with the existing rationale method. The Cursor SDK streaming reference is retained as the event-versus-terminal limit only; no SDK client or method is specified.
