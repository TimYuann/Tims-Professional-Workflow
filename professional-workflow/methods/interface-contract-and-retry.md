# Interface contract and retry semantics · candidate method body

- **Status:** candidate distilled under `docs/absorption/2026-10-02/reviews/ORACLE-REVIEW-A1-ADDY-CD.md` (C1, 2026-10-02, source `addy@2686b620`), extended under `docs/absorption/2026-10-02/reviews/ORACLE-REVIEW-A4-DEF3.md` (J1, 2026-10-02, source Cursor `ecc249f1`), and further extended under `docs/absorption/2026-10-02/reviews/REVIEW-GATE2-A4-CURSOR-DEF.md` (G04/G12, 2026-10-02, source Cursor `ecc249f1`); not yet an accepted reference; creates no authority, trigger, or gate. A fixed-diff review still applies.
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

A schema validates shape, field constraints and unified enumerations. It does not validate invariants that span fields. Before consuming the data, check the cross-field invariants the contract depends on:

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

Deferred from the same Addy source: GraphQL/type-system extras, branded types, discriminated unions, and the case for never maintaining two versions. The Cursor `orchestrate` runtime scripts, schema generator, type/store/build-lever skills and tests are not ported: no current task consumption depends on them, and porting would bring their permissions and dependency boundary. That is a consumption decision, not a judgment that scripts are worth less — the boundary experience above is retained, and no validator platform or store is introduced. Also not adopted: the type system as a substitute for runtime invariants or authority, temp+rename as durability, and "the lever must produce a file" as a universal rule.
