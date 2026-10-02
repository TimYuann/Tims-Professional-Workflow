# Handoff and resume · on-demand method (MG-7 + MG-8 checkpoint)

- **Method owner:** Driver for the transfer and checkpoint; E/F keep their own judgment; Voice only when a human-reserved decision travels.
- **Status:** on-demand reference at a demonstrated gap (carrying work across a session/agent/repo boundary); a task Charter decides applicability. It is not a reporting ritual and it changes no authority.

## Use

Use when work has to **travel** — a different harness, a different directory or repo, another person/agent, or a side task forked off mid-work — or when an explicit stop must leave something a cold reader can resume from. When nothing is travelling, do not produce a transfer artifact: the record (spec, plan, task status, commits) is the handoff and the work continues in place. Producing a summary for a same-place continuation is the ceremony this method exists to prevent.

## Handoff: what travels and at what evidence grade

- **The artifacts are the handoff.** What carries work forward is the accepted, written record (spec, plan, task status, verification results, commits), not the conversation. If the task spans sessions, those files are the handoff. *(Source: addy `2686b620`, `docs/getting-started.md` §Working across sessions L179–190; `docs/adoption-guide.md` §Day 0 L34–46.)*
- **Reference, don't copy.** Anything already written down — spec, plan, decision record, issue, commit, diff — is referenced by path/URL, never restated; copying it creates a second source of truth that drifts. A pointer to something the receiver cannot reach (a scratch path, another context's file) is not a handoff: check that it resolves. *(Source: matt `c55ee460…`, `docs/productivity/handoff.md` §What travels L30–34; §Common questions L44–51; plus the second-source failure mode below.)*
- **What travels.** The live thread: what is in flight and why, what is next, and (when it helps the receiver) which method/section to reach for. Redact before writing; custody follows `guide-redacted-evidence.md`. *(Source: same file, L32; `handoff/SKILL.md` L12–14.)*
- **Grade by the claim; the source's labels are observation modes, not a mandatory taxonomy.** Record how the evidence was obtained and on which object; the modes below are examples, and none of them assigns a conclusion by itself — they are not a UI/non-UI classification, and a stronger mode on one claim says nothing about another:

  | Mode (source example) | What it can support |
  | --- | --- |
  | target behavior reproduced live on the changed object | that behavior, on that object/version and those conditions — not a blanket "shipped", and not coverage of claims the run did not exercise |
  | a targeted test exercises the changed path and passes | what the test actually covers; a correct logic fixture can support a UI change's logic claim without settling its real-experience claim, which needs its own real leg |
  | type-check/build passes only | a typing/compile claim; no behavior |
  | the verifier could not run (ports, creds, environment) | unproven; record it as unverified rather than as a pass, and do not fabricate the run type |
  | the verifier ran and the target did not hold | a contradicting observation; a fix item, not a re-verify |

  *(Source: cursor `ecc249f1…`, `orchestrate/skills/orchestrate/references/handoffs.md` §Reading handoffs L11–21, §Verifier handoffs L98–141 incl. the legacy-label migration L142 — retained as observation modes and a migration convention, not as a required five-grade vocabulary.)* The conclusion belongs to the claim: its object and version, whether the real path was actually executed, what the run covered, the run's limits, and how independent the producer was. A self-reported pass stays a report until a verifier or a reproducible observation confirms it (a later verification overrides a self-report on the same target). An old recovered pass with no evidence of what was run stays **unverified** — do not assign it a mode to fill the table, and do not claim a type-check (or any other check) was executed when the record does not show it. A claim that travelled unverified is recorded as unverified rather than presented as a run, so the record does not overstate what is known.
- **Failure mode — the summary as a second source of truth.** A handoff that restates the spec/plan/decisions rather than pointing at them becomes a competing record; the next reader then has two versions to reconcile. The fix is the reference rule above, not a better summary.
- **Failure mode — beliefs written as facts.** This is the risk of taking an unverified report as a fact: a statement like "X is done / Y isn't built" written as fact can be relied on as a premise. The reader checks a necessary claim against the fixed object/version and the coverage that actually applies, keeps any accepted basis that is already valid, and marks a claim whose evidence is missing as unverified rather than assuming it. Before handing over, read the record back and downgrade anything only assumed, stating its basis (or that it has none). *(Source: `docs/productivity/handoff.md` §Common questions L59–60; the receiver-as-contract absolute is not retained.)*

## Portability and fork

- **The common travel reasons are useful examples, not a closed taxonomy.** A different harness/tool, a different directory or repo, another person or agent, and a side task forked off mid-work; decide by whether the receiver can actually recover the work and its state, not by whether the reason matches one of these categories. *(Source: matt `c55ee460…`, `docs/productivity/handoff.md` §What travels L30–34; the open-list boundary is authored.)*
- **Where the brief lives is a real constraint.** A note only in the sender's OS temp directory is unreachable for most receivers. The durable home is the project's conventional place (the repo, the issue, the shared record); if a reachable location is genuinely unavailable, say where the note is and leave a pointer the receiver can resolve. *(Authored; source: same file §Where does it live L42–43 — its single per-directory convention is not imported as a required path.)*
- **Carry the why when it conditions the next step.** Brevity must not drop a condition or exception that changes whether the receiver should do the work (why this approach, what was ruled out, why the next action is next); state the reason with a reference that resolves. If the reason is unknown, say unknown rather than letting the receiver infer one. *(Source: `handoff/SKILL.md` L12–14; the review's needed-why rule.)*
- **A fork inherits context, not authorization or verification.** A side task forked off mid-work inherits the parent's written context exactly — but the inherited record is not re-verified by arriving, and the fork's own changes still need their own applicable authorization, evidence and acceptance. Carrying a decision forward does not extend the decision to work it never covered. *(Authored fork boundary; the inherited-vs-produced rule above.)*
- **No second contract.** The brief points at the accepted record and adds only what is missing (in-flight state, next action); it does not restate or reinterpret the accepted commitments, and a fork's separate record does not revise the origin's.

## Missing or failed evidence

- **Report the failure, never silence.** A task that cannot produce its handoff still reports the run state it has (what ran, what did not, what evidence is missing) so the receiver is not left guessing; a missing report is not a success signal. *(Source: `handoffs.md` §Synthetic failure handoffs L23–68 — read for the principle, not the runtime classifier/retry policy it also contains.)*
- **"Tests pass" is a claim about a baseline.** Re-run the checks it covers when the code has moved since, when the record does not say what ran against what, or when you are about to touch the area it covers. If the baseline still holds, continue with a check proportional to the change rather than a full suite at every boundary. *(Source: addy `docs/getting-started.md` L186–190; `skills/context-engineering/SKILL.md` §Restartable Session Boundaries L123–137.)*
- **A recorded pass without coverage is unverified.** Do not present it as though the check had been run; state which part of the claim the evidence does not cover.
- **Keep the execution record even when the environment blocked the rest.** A compile or type-check that actually ran can be recorded as compile/type evidence for the claims it covers, alongside the behavior claims the blocked environment left unverified — do not blanket-erase an existing valid execution record because part of the task could not run. What must not happen is presenting that partial run as full coverage. *(Source: cursor `ecc249f1…`, `orchestrate/skills/orchestrate/prompts/worker.md` and `verifier.md`; gate2 MG5 ruling.)*
- **Blocked vs failed.** An environment failure is UNVERIFIED; a failure verdict requires a valid observation that contradicts the expected behavior (a broken measuring instrument is still UNVERIFIED). This keeps the comparison verdict mapping in `behavior-claim-evaluation.md` unchanged.

## Dependencies

- Carry the **upstream object** a dependent step needs (the handoff/report itself, or a resolving pointer to it), so the receiver recovers the original meaning instead of guessing from a scheduling edge. Declaring a dependency without carrying its context makes the receiver invent one.
- When a step's work is a composite, its own handoff **summarizes** what its sub-steps delivered (status, what it did, deviations/concerns, candidate follow-ups); forwarding the raw sub-reports is not a handoff. Say which acceptance criteria are met, not just that work happened. *(Source: `handoffs.md` §Producing your own handoff L86–97; §Reading handoffs L11–21.)*
- Quantitative claims keep their unit, the command that produced them and the comparison conditions; a number without those is not transportable evidence. *(Source: same file, §Measurements L7–9.)*

## Reconstruct and status

Before starting or resuming work, rebuild the *current* state rather than trusting memory. *(Source: cursor `ecc249f1…`, `pstack/skills/recall/SKILL.md` L9–22 and §Output contract L24–33.)*

- **A complete state capsule the requester handed you is used as given**; skip the mining. A specific prior conversation to resume, or turning a habit into a durable rule, routes to its own carrier rather than this section.
- **Lock the scope before searching:** the time window (make "recent" a real range), the topic if named, and the workspace (the active one by default — never read another project's records unless asked). State the scope back; never quietly turn "all" into "recent N".
- **Get the sources the current scope actually needs.** When the scope or a necessary claim lacks its basis (a symptom with no diagnosis, a fix that may have been reverted, a state that only the shared record shows), fetch that evidence — the shared record holds what an agent's own history does not. When a complete state capsule was already supplied, reuse it as given and skip the mining. Record what was **not** checked rather than implying full coverage; do not self-authorize a default exhaustive sweep, and do not quietly widen "recent" or "this workspace" without saying so.
- **Verify against live state:** check branches, PRs, tickets and commits against the actual repository rather than the summary; when the answer depends on what an agent actually did, read the full record rather than a trimmed copy. Cite findings by their source and sanitize before any public output.
- **Report shape:** capsule (a few lines: what this work is, where it stands) → threads (one line each with exactly one status tag — merged, open PR, in flight, verified but uncommitted, reverted, planned) → problems (the recurring ones, including a fix that shipped and was reverted) → next move (one concrete action). A thread with no tag is not done; say so.

**Status honesty.** Distinguish decided/known from assumed, and inherited from newly produced. "Committed", "merged" and "deployed" each need the evidence for that state: an authored commit does not prove something shipped, and a merge commit may carry real integration. Uncommitted or worktree state may be reported when it is in the requested scope; if the identity or scope is unclear, use an explicit verifiable range and state the limitation rather than forcing an environment change. *(Source: cursor `ecc249f1…`, `cursor-team-kit/skills/weekly-review/SKILL.md` §Guardrails L23–27 and `what-did-i-get-done/SKILL.md` §Guardrails L20–25; the shipped/merged separation is authored.)*

Boundaries: no mandatory full-record search, subagent fan-out, or fixed brief format; do not re-run every step on every resume. *(Source: the review's MG-4 boundary.)*

## Checkpoint and pickup

- Stop at a **safe boundary**: finish or back out of the current atomic step, start nothing new, cancel nested work. Take no irreversible action merely to pause.
- Make the work durable — the current state, what is in flight, what is verified, the next action, key paths and gotchas — and leave it where the next reader can actually read it. Point at the existing decision trail (`decision-record.md` §Execution trail) instead of duplicating it.
- Separate **inherited accepted decisions** from **unverified claims**: a decision that travelled is not re-accepted by arriving; a claim that travelled is not re-verified by arriving.
- On pickup, read the artifacts and the repository state before acting; do not assume an approval that is not in the durable record, and do not use a restart to bypass an approval gate. *(Source: addy `docs/getting-started.md` L184–192; `skills/context-engineering/SKILL.md` L123–137.)*
- An explicit pause is explicit: a "keep going" instruction is not a pause trigger. *(Source: cursor `pause-safely.md` L3; read for the checkpoint content, not as a runtime pause protocol.)*

## Limits

- Not a document-writing mandate: the portability trigger (common examples: a different harness/tool, directory/repo, person/agent, or a side fork) decides whether anything travels; ordinary continuation uses the existing artifacts. The transfer-document orientation of the source is not adopted, and the example list is not treated as exhaustive.
- No fixed temp path, no per-iteration handoff, no mandatory summary format, and no new artifact when the record already covers it.
- Redaction and raw-artifact custody follow `guide-redacted-evidence.md`; the runtime retry/classifier policy of the source (cap-hit/OOM/network/tool-error handling, retry counts) is not part of this method — a delegation's own policy governs that.
- A handoff or checkpoint records state; it does not accept a claim, authorize an action, close a task, or replace the independent evaluation of the object.

## Source anchors

| Source | Retained contribution |
| --- | --- |
| addy `2686b620fc1fed2e8f60c704839c766b8594c6b6`, `docs/getting-started.md` §Working across sessions L179–200; `skills/context-engineering/SKILL.md` §Restartable Session Boundaries L123–137; `docs/adoption-guide.md` §Day 0 L34–46 | Artifacts are the handoff; the pre-switch fact list; baseline claims and the three re-run triggers; proportional checks; process exit is not a passed task; restart cannot bypass approval. |
| matt `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`, `docs/productivity/handoff.md` (L3–34, L38–60) and `skills/productivity/handoff/SKILL.md` L8–16 | Portability, not compression; the travel-reason examples as an open list; reference-don't-copy with the drift reason; what travels and the needed why; the fork case (context inherits, authorization/verification does not); pointer chasing; downgrade unverified claims; the durability question. |
| cursor `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`, `orchestrate/skills/orchestrate/references/handoffs.md` (§Measurements L7–9; §Reading handoffs L11–21; §Verifier handoffs L98–141; §Upstream handoffs L73–85; §Producing your own handoff L86–97; §Continuous motion L185–194) | Status/branch/what-did/concerns/follow-ups; observation modes as source examples (live/test/type-check/blocked/failed) judged per claim, not a required five-grade vocabulary; the legacy-to-conservative migration as a convention; verification execution evidence per criterion; upstream context must travel with the dependency; composite handoffs summarize. |
| cursor `pause-safely.md` (L3–9) | The checkpoint content (intent, in-flight work, verified state, next action, key files/gotchas) and the safe-stop boundary. |
| cursor `ecc249f1…`, `pstack/skills/recall/SKILL.md` (L9–22; §Output contract L24–33) | Rebuilding current state from the two records; scope locking; scope-driven source retrieval (not a default exhaustive sweep); live-state verification; capsule/threads/problems/next-move with one status tag per thread. |
| cursor `ecc249f1…`, `orchestrate/skills/orchestrate/prompts/worker.md` and `verifier.md` | Execution-record honesty: a run that happened is recorded for what it covered (compile evidence is still compile evidence while behavior blocked by the environment stays unverified); do not erase valid evidence or dress a partial run as full coverage. *(Gate2 MG5.)* |
| cursor `ecc249f1…`, `cursor-team-kit/skills/weekly-review/SKILL.md` (§Workflow L12–21; §Guardrails L23–27) and `what-did-i-get-done/SKILL.md` (§Workflow L12–18; §Guardrails L20–25) | Evidence-bound status reporting: explicit date range, authored commits only, exclude merges/uncommitted, omit cosmetic, no inferred intent. |

Authored additions: the report-vs-proven-fact scoping, the claim-bound evidence grade, the second-source-of-truth failure mode, the inherited-decision vs unverified-claim split on pickup, and the Limits (no document mandate, no runtime retry policy).
