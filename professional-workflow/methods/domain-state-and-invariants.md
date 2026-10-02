# Domain state and invariants · on-demand method (MG-4)

- **Method owner:** C domain semantics for what the states mean and which transitions are legal; D/E own the code representation. This method sits next to `domain-language.md` and does not replace it.
- **Status:** on-demand reference at a demonstrated gap (state/invariant operations); a task Charter decides applicability. It creates no registry, schema, or mandatory structure.

## Use

Use when stateful logic is being written or changed, when code branches a lot or repeats a shape assumption across files, or when a review needs to judge whether the state model is the source of the branching. Do not use it for clear, local, stable shapes that are unlikely to grow: boring code is the right answer there. *(Source: cursor `ecc249f1…`, `pstack/skills/principle-model-the-domain/SKILL.md` L24.)*

## State questions (C's judgment)

Before choosing a representation, answer:

- **States:** which states actually exist in the domain, and which of the current booleans/flags/phases each one corresponds to?
- **Transitions:** which transitions are legal, and who may trigger them? A transition that is legal only under an unstated condition is an invariant waiting to be violated.
- **Invariants:** what must hold in every state and across every transition (including concurrent access and failure paths)?
- **Reads:** how is the data actually read? The access pattern decides whether a map, index, queue or normalized collection fits — not the number of branches.
- **Never-allow:** what must the code make impossible? Work that out first, then pick the structure that encodes exactly that. *(Source: same file, L11–22.)*

The **ownership split** matters here: C owns the domain meaning, transitions and invariants. **D** decides and revises the shared technical approach inside the valid envelope — the Plan's commitments and delegated decisions — and **E** chooses the local representation inside its delegated scope and the commitments it must preserve. A representation choice inside those bounds is D's or E's to make without a return; what goes back through the corresponding route is a change to the meaning, a shared interface, or a compatibility commitment (B/C, or the recall judgment in `cross-module-design.md` §Method 2) — never a silent local edit. *(Source: same file, L19; the D/E split boundary is from the R2 gate ruling.)* An execution order is not ownership: a module organized around "load, validate, transform, save" repeats the same domain rules across the steps, whereas a module organized around one body of domain knowledge states them once. *(Source: same file, L19.)* Execution order being mistaken for rule ownership is a *symptom* to diagnose; it does not mean every load/validate/save module is wrong.

## Transition examples

- **Illegal combination to remove.** A record typed as `{ completed: boolean; completedAt?: Date }` admits `completed: false` with `completedAt` set, and invites two fields that must be kept in sync. If completion is the state, model the state (a discriminated union/state machine, `completed` carrying its timestamp) so the impossible combination has no representation; the downstream branches that would have checked the fields then disappear. *(Authored example in the shape of the source's list: state machine instead of scattered booleans; typed model instead of repeated shape assumptions; map/registry/discriminated union instead of branches spread across files; reducer/command model instead of ad-hoc mutation. Source: same file, L15–18.)*
- **Legal simple branch to keep.** A single local `if (retriesLeft > 0)` around a small, stable, clearly named path needs no abstraction; forcing a structure here adds indirection without removing a branch, an invalid state, or a duplicated rule. *(Source: same file, L24: "Do not force an abstraction. Prefer boring code if the current shape is already clear, local, and unlikely to grow.")*
- **Signs the model is missing** (diagnose, don't count): a new feature grows an existing if/else chain by one more branch; a second boolean must stay in sync with the first; phase-named modules repeat the same rules across steps. *(Source: same file, L26.)*

## Representations and handoff (D/E)

Where a representation is warranted, the source's candidate shapes are: a state machine; a typed object/model; a map/registry/lookup table/discriminated union; a reducer or command/event model; a module gathered around one body of domain knowledge; a small module boundary that gathers repeated behavior/ownership/invariants; a queue, cache, index, graph/tree or normalized collection where the access pattern calls for it. *(Source: same file, L15–22.)*

When handing the decision to another module or verifier, carry what the representation must convey and to whom:

- the state names and which real-world conditions they stand for;
- the legal transitions and their guards;
- the invariants that must hold (including at boundaries and under concurrency);
- which access patterns the shape was chosen for, so a later change can tell whether the shape still fits.

Do not hand over only the code shape: the state meaning is C's object, and a verifier cannot check an invariant that was never stated.

## Limits

- **No branch-count KPI.** Fewer `if`s or booleans is not the success measure; preserving meaning, lifecycle constraints and invariants is. Do not substitute a smaller method/parameter count for a correct model.
- **No forced abstraction.** Where the current shape is clear, local and stable, keep it; an abstraction that adds indirection without removing branches, duplicated rules or invalid states is a cost.
- **C's method does not authorize technical refactors.** Replacing a representation is a D/E change; it follows the coordination-surface judgment and the task's authority, not this method.
- **No blanket "trust internal types".** The verification-boundary details of dependency/type discipline are not imported here (a separate source batch handles them): authorization, state, external bypasses and temporal constraints can still require guards. This method says nothing about removing checks.
- **No new state/registry/schema platform.** The method produces a model or a statement of invariants, not a tool.

## Source anchors

| Source | Retained contribution |
| --- | --- |
| cursor-plugins `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`, `pstack/skills/principle-model-the-domain/SKILL.md` (full, L9–26) | Encode the domain in a structure instead of scattered conditionals; the candidate structures (state machine, typed model, map/union, reducer/command, knowledge-owned module, queue/cache/index, normalized collection); the never-allow/read-pattern question; do-not-force-an-abstraction; the skip signs (one more branch, a second synced boolean, temporal decomposition). |
| cursor-plugins `ecc249f1…`, `pstack/skills/principle-boundary-discipline/SKILL.md` | **Not imported in this batch** — listed in the review as deferred to a later batch; this method does not adopt its "trust internal types" position. |

Authored additions: the C/D/E ownership split restated for the product, the illegal-boolean and legal-simple-branch examples, the handoff fields (states/transitions/invariants/access patterns), and the Limits (no branch-count KPI, no refactor authority, no verification-boundary import).
