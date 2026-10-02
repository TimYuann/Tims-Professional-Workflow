# Change slicing · on-demand method (MG-2)

- **Method owner:** D technical/system design for the slicing, E for executing a slice. B/C keep behavior and domain ownership.
- **Status:** on-demand reference at a demonstrated gap (splitting a change into verifiable slices); a task Charter decides applicability and delegated scope. It publishes nothing and creates no tracker process.

## Use

Use when a plan, spec or conversation has to be broken into work items that can each be finished, demonstrated or verified on their own — typically when the change spans several sessions or more than one module. Skip it when the whole change fits in one working pass; over-decomposition is the common failure on the other side.

## Behavior slices

- Each slice cuts a **narrow but complete path** through the layers it actually needs (schema, API, UI, tests — whichever exist; do not require layers a change does not have). Vertical, not a layer taken alone.
- Ask of every item: **what can this item independently demonstrate or verify when it is done?** An item with no answer is a layer slice or a placeholder. The answer should be behavior, not "the schema is finished".
- Do not mistake layer completion for behavior completion. "All the parsing is done" is not a demo; "a user can paste X and see Y" is.
- The first slice should be the smallest complete path (a tracer bullet) that proves the shape end to end.
- Every slice needs its own verifiable result, including support work: when an item is infrastructure or preparation, state which later behavior it enables **and** what can be checked about the item itself.

## Dependencies

- List the **actual blocking edges**: the other items that must complete before this one can start. An item with no open blockers is on the frontier and can start now.
- Dependencies are work items, not layers or phases; only include edges that genuinely gate the item.
- An item does not get credit for an outcome another item owns: if this item's result can only be observed after a different item lands, say so and keep the acceptance criterion with the owning item, or state explicitly that this item is a supporting step.
- Prefactoring ("make the change easy, then make the easy change") is limited to what actually makes this change easier, arranged inside the current authorization. It is not a mandate to refactor first, and refactoring may be sliced as ordinary work with its own verifiable result.

## Unit evidence order

For work made of many similar edits (a sweep, migration, or batch of edits), give each unit a **before/after bracket** and a recoverable piece of evidence: *(Source: cursor `ecc249f1…`, `pstack/skills/principle-sequence-verifiable-units/SKILL.md` §Execution L13.)*

1. **Known state** — start from a state whose check you trust (align to a clean baseline where practical for the run; a break caught at a later unit is harder to localize).
2. **One bounded change** — one unit of work, not a batch.
3. **A check aimed at the claim** — run the check that would expose a failure of *this* unit before starting the next one; where no per-unit check exists, use the nearest executable observation and say what it covers.
4. **Recoverable evidence** — keep the observable result (or the rerunnable check) so the sequence can be replayed by someone else.

Rationale: a break caught at the unit that caused it is cheap to localize; a break caught after a batch is buried and you have already built further on a broken base. *(Source: same file §Why L11.)*

**Delivery order is part of the evidence.** Order the units so the sequence reads as an argument: the canonical shape is the failing check first, then the fix on top; other honest orders are a subtraction before the reshape, a baseline capture before the treatment, the scaffold before the feature. Each unit should land on its own so a reviewer can replay the sequence. *(Source: same file §Delivery L15.)*

Boundaries: this does **not** require a green check, a rebase, or a commit per unit — wide refactors legitimately cannot stay green per unit (see the exception below), and where the per-unit check is expensive, batch sizing and the claim decide. The order is a discipline for finding failures where they happen, not a ritual that produces evidence for its own sake.

## Wide refactors (the exception)

A **wide refactor** is one mechanical change (rename a column, retype a shared symbol) whose blast radius fans across the codebase, so a single edit breaks many call sites at once and no vertical slice can land green. Do not force it into a tracer bullet; sequence it as **expand–migrate–contract**:

1. **Expand:** add the new form beside the old so nothing breaks.
2. **Migrate:** move call sites over in batches sized by the blast radius (per package, per directory), each batch a work item blocked by the expand; CI stays green batch to batch because the old form still exists.
3. **Contract:** delete the old form once no caller remains, in an item blocked by every migrate batch.

When even the batches cannot stay green alone, keep the sequence but let them share an integration branch and all block a final integrate-and-verify item — green is promised **only there**, and failing intermediate items are not reported as passing. The shared-branch arrangement is optional; it grants no branch, migration or deletion permission (deletion follows `cross-module-design.md` §Method 4).

## Limits

- No fixed "one context window" capacity guarantee: size items by what one working session can actually finish and verify in this repo, and say when the basis for the size is an assumption.
- No tracker, template, label, or publication step is required; how items are recorded and dispatched is a task/Charter matter.
- Do not invent layers or work that the change does not need; do not brand all preparation or infrastructure work as bad.
- Deletion and legacy removal inside a wide refactor follow the coverage-replacement and authority rules; this method confers none.
- Slicing is a design judgment; it does not create acceptance, implementation authority, or closure.

## Source anchors

| Source | Retained contribution |
| --- | --- |
| Matt Pocock, `mattpocock-skills` at `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`, `skills/engineering/to-tickets/SKILL.md` (§3 Draft vertical slices L25–40; prefactor L23) | Tracer-bullet slices cut through the layers a change actually has; a completed slice is demoable/verifiable alone; blocking edges; prefactoring first; the expand–migrate–contract wide-refactor exception and the integration-branch variant. |
| Same pin, `docs/engineering/to-tickets.md` (§Tracer bullets, not layers L25–31; §Blocking edges L33–42; §The wide-refactor exception L44–54; §Common questions: acceptance criteria L76–77) | Vertical vs horizontal slicing and its cost; edges as the point of the artifact and the frontier; the wide-refactor sequence; the criterion check "name the observation that would show it false at the starting commit". |
| Same pin, `skills/engineering/to-spec/SKILL.md` (§Process 2, L15) | Seams are chosen before implementation and existing seams are preferred. |
| cursor-plugins `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`, `pstack/skills/principle-sequence-verifiable-units/SKILL.md` (§Why L11; §Execution L13; §Delivery L15) | The before/after bracket (known-good → one change → check → proceed), the localization rationale, aligning to a clean baseline, and the delivery order that makes the sequence prove itself (failing check first, subtraction/baseline/scaffold variants). |

Authored additions: the "what can this item independently demonstrate" question as the slice test, the support-work rule (enabled behavior plus own checkable result), the dependency-credit rule, and the limits (no context-window guarantee, no tracker mandate).
