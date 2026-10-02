# Bounded composition · candidate method body

- **Status:** candidate distilled under `REVIEW-A2R-CURSOR-ABC2` (MG-5, 2026-10-02); not yet an accepted reference; creates no authority, trigger, or gate. A fixed-diff review still applies.
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

## Examples and counterexamples

- **Separated.** Each worker writes its own owned output; one integrator reads them and writes the combined artifact.
- **Still shared.** Two writers put their own fields into one `state.json`, even when the fields are disjoint.
- **Real invariant.** A lockfile or a single-writer phase is justified only when one canonical object is genuinely required; otherwise it is indirection or a smell.
- **False comfort.** Worktree isolation plus a convention does not protect a shared external database or key.

## Conditions and exceptions

- Not every composition needs a merge step or a recorded single writer; keep the arrangement as light as the actual sharing requires.
- An institutional write-surface agreement documents intent, not runtime concurrency; do not present it as proof that locks work. Denying that a lock exists is likewise a claim with its own evidence condition.
- Designing a genuinely shared surface is a D decision inside its delegation; this method supplies the arrangement questions, not the design authority.

## Limits

- No fixed number of writers, workstreams, or merge points; no required lock, coordinator, registry, validator, or framework.
- No write permission, branch or migration authority, or external-resource access is created here.
- Later cross-source work may merge this body with another shared-state source; keep the eliminate-first default, the canonical-versus-independent test, the single-writer/merge-point, the convention-is-not-concurrency-control boundary, and the runtime-ownership split.

## Source anchors

| Source | Pin / path | Section |
| --- | --- | --- |
| Cursor plugins | `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`, `pstack/skills/principle-separate-before-serializing-shared-state/SKILL.md` | Pattern 1–3 (L13–16): identify shared mutable state; eliminate by default; serialize structurally only when one shared write target is a real invariant |
| Product core | `authority/RESPONSIBILITY-BACKBONE.md` §4 | Driver stays at the logical routing layer and does not define processes, concurrency, queues, locks, or retries |
