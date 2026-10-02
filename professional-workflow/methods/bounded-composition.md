# Bounded composition · candidate method body

- **Status:** candidate distilled under `REVIEW-A2R-CURSOR-ABC2` (MG-5), extended under `REVIEW-GATE2-A2R-CURSOR-ABC5` (MG-1), `REVIEW-GATE2-A2R-CURSOR-ABC6` (MG-2/MG-3), `REVIEW-GATE2-A2R-CURSOR-ABC8` (MG-4) and `REVIEW-GATE2-A4-CURSOR-DEF` (G04, 2026-10-02); not yet an accepted reference; creates no authority, trigger, or gate. A fixed-diff review still applies.
- **Method owner when bound:** Driver/routing arranges the logical write surfaces and dependencies; D owns the design when the sharing is a real invariant. This method does not define runtime concurrency mechanics (processes, locks, queues, compare-and-swap, retries) and does not replace Driver's routing.

## Use

Use when concurrent actors — agents, instances, or processes — might write to the same file, branch, key, or state object, or when several bounded workstreams must be composed into one deliverable. It keeps the composition bounded: eliminate avoidable sharing first, name the single writer for what remains, and keep the integration point explicit.

## Write targets

1. Identify the shared mutable state: files both read and write, branches both push to, keys both update, APIs both define and consume, state objects both mutate.
2. Default to eliminating the shared write target. Ask whether the actors need one canonical object or are publishing independent facts. Give each actor its own owned file, key, branch, or state directory, and merge only at the read/reporting boundary.
3. Independent owned outputs plus one integration writer is a bounded composition. Several actors appending their own fields to one shared file is still shared mutation, not separation — two workers each writing their own `lastX` field into one `state.json` is shared state; separate `indexer-state.json` and `metrics-state.json` are not.
4. Only when one shared write target is a real invariant, serialize access structurally: lockfile, sequential phase, single-writer actor, or atomic compare-and-swap. Treat "we need a lock" as a design smell to check, not as the default answer.
5. Name the single writer for every genuinely shared surface, and the merge point where owned outputs combine. Record the arrangement in the task's existing channels (Charter binding, dispatch note); do not create a registry, a coordinator role, or a new runtime.
6. Keep each actor's write set explicit and bounded: one writer per file, and the integrator knows which object it may change. An isolated worktree isolates its own files, not an external database, queue, key store, or credential store.
7. A written convention ("only X edits this") is a boundary statement, not proof that a runtime lock or transaction is actually in effect. Runtime effects need their own evidence; a convention neither grants nor substitutes for concurrency control.
8. Runtime mechanics (processes, queues, lock implementation, compare-and-swap, retries) are outside this method and outside Driver's routing role; they belong to the implementing design and its own authorization.
9. Adopting, cleaning up, or respawning another actor's state needs existing authorization; a shared-write arrangement is not that authorization, and unknown resources are left alone.

## Task inputs and starting point

10. A composed task's description should be self-sufficient for the instance it binds: the goal and non-goals, the accepted inputs, the write surface and what must be preserved, the conclusion or deliverable, and how the work will be observed plus what remains unknown and when to return. This is the same six-item basis as `charters/README.md` §Shortest startup path; keep the pointers instead of copying the checklist here. An execution environment that cannot ask a question mid-run needs the task text to carry this basis, but do not assume every instance is unable to ask or that an ambiguity will always drift silently.
11. Separate the logical starting point from the dependencies. The starting point names the fixed object actually read (path, commit, artifact version); a dependency names the conclusion, interface, or artifact that is still pending. A mutable locator — a branch or tag label — is not the fixed object: the snapshot is the commit or artifact version actually resolved and recorded at handoff time, with the time and the consumption scope, and the same label can resolve to a different object later. Verify the resolved object against the consumption scope rather than treating the label as fixed; this needs no resolver platform or new gate.
12. On receiving a handoff or a task, verify the actual branch/commit and the consumption range before relying on it; a preset placeholder or a name match is not identity, and a hand-written override still has to match the accepted inputs and purpose rather than being trusted because it is explicit. Artifact identity and failure records stay with `handoff-and-resume.md` (another batch); this section states only the composition-side checks.
13. Non-sensitive shared artifacts that the clone can see may travel by path and version, and the repository's existing convention is enough; credentials never go into task text or synced history, and environment passing follows the real tool boundary — do not generalize one VM's redaction into a universal env ban.
14. A task body or a handoff is an input, not authority: it does not by itself grant permission to change an object, merge, or publish, and a composed workstream does not silently become a durable permission.

## Dependency chain and integration

15. Consume a dependency chain as its currently advanceable frontier: a step can proceed when the conclusions, interfaces, or artifacts it depends on are actually satisfied, and a contiguous verified segment can be consumed without waiting for the whole chain. An upstream PASS does not erase a load-bearing downstream unknown, and independent work is not locked by an unrelated chain. The slicing of work into advanceable units belongs to `change-slicing` (another batch); this section states the composition-side rules and points there rather than duplicating its steps.
16. At each integration, verify the actual landed ref and its real consumers, and re-confirm the base, identity, and coverage of what the next dependent task will consume. A READY or armed state is not merged, and a merged label does not by itself prove the target ref contains the expected bytes. A blocked state whose rollup is not failing is not an allow, and unknown mergeability or a pending review requirement is not clearance; a structured field is not proof that the required policy was satisfied.
17. Reuse evidence only while the claim stays inside its original coverage. A prior green on an old revision, or an unchanged commit message, is not evidence for a new object; a rebase or retarget can invalidate a verdict without touching a check. A matching patch-id is a change-detection clue, not proof of behavioral equivalence: the same edit on a base with changed callers, invariants, or dependencies can behave differently. Documentation, tests, and configuration can be load-bearing, so do not exempt them by suffix or matching hash.
18. Keep writer roles and observers separate: a shared canonical object keeps a single writer while several pure observers are fine; a fix on an owned branch and a change to the base or topology are different actions, each needing its own valid permission. A real reserved approval is a wait-and-return condition, not a technical bug to fix, and an unknown state stays unknown rather than being filled from an unrelated field.

## Brief, completion, and rolling limits

19. Keep the brief proportionate to the unit: the goal and valid scope, accepted inputs, dependencies and recoverable artifacts, the observation and limits, and the permission/stop/report rules. A missing template field does not by itself reject the whole spawn; a missing load-bearing input is surfaced, and only the work that depends on it stops.
20. A dependency is both an order and a content relay: where the consumer can reach the fixed original object, pass a pointer to it; only where it cannot, transmit the minimal necessary content faithfully. Sending all standing context verbatim on every resume, or forbidding a resume chain outright, is not a requirement.
21. Treat completion as an event to triage by scope: it is not automatic success and not authority to interrupt a critical mutation. Keep a critical section intact according to its real dependency or invariant; do not impose a fixed number of drain points, mandatory batching, or a ban on inline professional review.
22. Roll or batch only by what can actually bear review and integration and by the shared write surface. Over-fanout is reined back — prefer fewer, broader units, keep fan-in small, aggregate many-upstream handoffs, and minimize path overlap — and a coordinator holding a valid E delegation is not forbidden from implementing part of the work itself.
23. Keep the current record of what arrived, what failed, what is unreturned, and what was abandoned with its scope, so a silent redo does not erase contributions or gaps; where no platform-wide child directory exists, state the observation range instead of implying completeness. Instance replacement or resume keeps the rounds, closed items, contributions, and pending work, and re-checks that the transmitted constraints are still valid rather than substituting an old order or a mutable trunk for the accepted basis.

## Persistence and lock claims

24. A same-directory temporary exclusive-create plus rename describes a single-file publish strategy, not durability: it does not equal fsync crash durability, a multi-file transaction, or a no-lost-update guarantee. An exists-check-then-write helper needs a real concurrency premise, and "the init step is idempotent by name" is not proof of it.
25. A PID lock's local namespace, file permissions, liveness check, and PID reuse — plus the check/unlink race — must be declared. A release that only verifies the PID is not a full epoch or fencing guarantee; `--force` is a technical option, not authority to steal a lock; a convention cannot replace a lock, and a new lock is not created by default.
26. Keep one canonical writer for shared state and independent owned outputs elsewhere; a derived view names its original owner. Existing records are enough — not every file needs a new TSV or JSON, and not all status must come from a new generator.
27. A ledger's missing record is unverified, not a claim of none: a new head does not clear old claims, and modes are not mapped mechanically. Record keys need a real repo or store namespace plus the object, claim, and coverage.
28. No "nobody answered, so the risk is accepted" default: a gate resolution needs a real answer, and a fallback comes only from a previous valid, non-reserved delegation. A strict format for the check plan (lane count, punctuation) is not professional sufficiency; do not port the gate/checker or force a one-off tool.

## Examples and counterexamples

- **Separated.** Each worker writes its own owned output; one integrator reads them and writes the combined artifact.
- **Still shared.** Two writers put their own fields into one `state.json`, even when the fields are disjoint.
- **Real invariant.** A lockfile or a single-writer phase is justified only when one canonical object is genuinely required; otherwise it is indirection or a smell.
- **False comfort.** Worktree isolation plus a convention does not protect a shared external database or key.

## Conditions and exceptions

- Not every composition needs a merge step or a recorded single writer; keep the arrangement as light as the actual sharing requires.
- An institutional write-surface agreement documents intent, not runtime concurrency; do not present it as proof that locks work. Denying that a lock exists is likewise a claim with its own evidence condition.
- Designing a genuinely shared surface is a D decision inside its delegation; this method supplies the arrangement questions, not the design authority.
- An environment scrub (an allowlisted env, a scratch HOME, a shell wrapper) reduces ambient pollution; it does not isolate the same-UID filesystem, network, or tool credentials and is not a security sandbox.

## Limits

- No fixed number of writers, workstreams, or merge points; no required lock, coordinator, registry, validator, or framework.
- The source control plane's defaults (a planner that never writes product code, one clone per task, no sibling cross-talk, default push or PR, fixed retry counts) are that runtime's arrangement, not requirements here.
- Shipping, publishing, and merge permissions follow the adopting project's own authority; the dependency and write-surface rules here do not create a shipping, approval, or integration platform.
- No write permission, branch or migration authority, or external-resource access is created here.
- Rolling and batching follow what can bear review and integration and the shared write surface; no fixed number of tiers, queued units, or budget percentage is set here, and a source's concrete numbers are that runtime's, not limits. No store, ledger, runner, or coordination framework is ported; the arrangement lives in the task's existing channels, and concrete lock implementations, store schemas, and release/check rules from a source are not ported either.
- Later cross-source work may merge this body with another shared-state source; keep the eliminate-first default, the canonical-versus-independent test, the single-writer/merge-point, the convention-is-not-concurrency-control boundary, and the runtime-ownership split.

## Source anchors

| Source | Pin / path | Section |
| --- | --- | --- |
| Cursor plugins | `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`, `pstack/skills/principle-separate-before-serializing-shared-state/SKILL.md` | Pattern 1–3 (L13–16): identify shared mutable state; eliminate by default; serialize structurally only when one shared write target is a real invariant |
| Product core | `authority/RESPONSIBILITY-BACKBONE.md` §4 | Driver stays at the logical routing layer and does not define processes, concurrency, queues, locks, or retries |
| Cursor plugins | `ecc249f1…`, `orchestrate/skills/orchestrate/SKILL.md` | Core principles: planners own scopes and publish tasks; workers are isolated with one handoff each |
| Cursor plugins | same pin, `orchestrate/skills/orchestrate/scripts/core/prompts.ts` §buildWorkerPrompt (L108–141) | A worker task carries goal/scoped goal, allowed and forbidden paths, acceptance criteria, a verification plan, upstream handoffs, and the starting ref/branch |
| Product core | `charters/README.md` §Shortest startup path | Mutual pointer for the six-item startup basis; no checklist copy |
| Product core | `methods/handoff-and-resume.md` (another batch) | Artifact identity and failure records; pointer only |
| Cursor plugins | `ecc249f1…`, `pstack/skills/poteto-mode/playbooks/shipping.md` | Land only the contiguous verified run; re-check that each verdict still describes the patch (head/base/patch-id; a rebase can invalidate a verdict); a host may retarget a child — do not assume it did |
| Cursor plugins | same pin, `pstack/skills/poteto-mode/playbooks/autopilot-stack.md` | Verified or operator-specified order; single writer on topology with parallel writers on builds; absorb drift then re-verify what moved; STACK-READY is not merge-ready |
| Cursor plugins | same pin, `orchestrate/skills/orchestrate/references/planner.md` | Planning rules: prefer fewer broader workers, keep fan-in small, aggregate many-upstream handoffs, minimize path overlap, and put shared artifacts in git referenced by path; failure recovery and planned checkpoint restarts |
| Cursor plugins | same pin, `pstack/skills/poteto-mode/scripts/orch/store.ts` | `atomicWrite`/`writeIfMissing` (L324–445): same-directory temp exclusive create plus rename; exists-check-then-write; PID lock acquire/takeover and PID-only release; `--force` takeover |
