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
- **Materialize each edge to what it truly blocks on** — a conclusion, an interface/contract, a write surface, or a resource — rather than to a vague phase name. That is what makes the order checkable against real system facts. *(Source: addy `2686b620…`, `skills/planning-and-task-breakdown/SKILL.md` §Step 2; the materialization phrasing is the C8 gate ruling.)*
- Dependencies are work items, not layers or phases; only include edges that genuinely gate the item.
- **Record the actual dependency chain, not only this item's edges.** Alongside the blocking edges, note the chain the unit sits in — what it needs, what needs it, and which upstream conclusions, interfaces or artifacts must exist — so a consumer can see which segment is genuinely available and which is still waiting. The shared-write, topology and interference rules belong to the composition method (`bounded-composition.md`, once integrated); this method adds no shipping or integration authorization platform. *(Source: cursor `ecc249f1…`, `pstack/skills/poteto-mode/playbooks/shipping.md` and `cursor-team-kit/skills/make-pr-easy-to-review/SKILL.md`; the cross-reference boundary is the gate2 MG2 ruling.)*
- An item does not get credit for an outcome another item owns: if this item's result can only be observed after a different item lands, say so and keep the acceptance criterion with the owning item, or state explicitly that this item is a supporting step.
- Prefactoring ("make the change easy, then make the easy change") is limited to what actually makes this change easier, arranged inside the current authorization. It is not a mandate to refactor first, and refactoring may be sliced as ordinary work with its own verifiable result.

## Ordering and checkpoints

- **Map the dependencies first, then order bottom-up.** Establish what depends on what from real system facts (for example data shape → types/validation → endpoints → callers → UI/consumers, adapted to the system), and sequence the work along the graph so foundations land before the things that need them. The storage-before-API-before-UI direction is an illustration, not a fixed order — the graph decides. This is an ordering basis, distinct from the Plan's commitments, delegated decisions and recall conditions. *(Source: addy `2686b620…`, `skills/planning-and-task-breakdown/SKILL.md` §Step 2; illustration-not-rule boundary is the C8 gate ruling.)*
- **Slice vertically, not by layer.** The failure shape is horizontal — build all the schema, then all the API, then all the UI, and only then connect them — which hides integration risk until the end. A vertical slice is one complete usable path ("a user can create an account", "a user can log in", "a user can view the list"); each slice ends with something usable and testable, which is also what makes its checkpoint able to verify anything. *(Same source, §Step 3 and its good/bad contrast.)*
- **Ordering signals:** satisfy dependencies first; leave the system usable after each item; place high-risk or high-uncertainty items early (failing fast is cheaper than failing late); set a verification checkpoint at a practical cadence — the source's every-2–3-items is an example, not a gate — and check that the relevant checks pass and the core flow still works. Where a human decision is genuinely needed before the next step, that checkpoint is a real stop; it is not a mandatory human confirmation for every item. *(Same source, §Step 5; the checkpoint-as-signal and human-stop boundaries are the C8 gate ruling.)*
- **Re-split signals** (the semantic ones need no time estimate): the item needs more than one focused session; its acceptance criteria cannot be written clearly and briefly; it touches two or more independent subsystems; **its title contains "and"** (that is usually two items). File counts or a size table may illustrate scale, but they are examples, not thresholds. *(Same source, §Task Sizing Guidelines; all four retained as signals, not gates.)*
- **Skip this section when it is unnecessary:** a single-file change with obvious scope, or a task list that the accepted material already defines well. *(Same source, §When NOT to use.)*

## Unit evidence order

For work made of many similar edits (a sweep, migration, or batch of edits), give each unit a **before/after bracket** and a recoverable piece of evidence: *(Source: cursor `ecc249f1…`, `pstack/skills/principle-sequence-verifiable-units/SKILL.md` §Execution L13.)*

1. **Known state** — start from a state whose check you trust (align to a clean baseline where practical for the run; a break caught at a later unit is harder to localize).
2. **One bounded change** — one unit of work, not a batch.
3. **A check aimed at the claim** — run the check that would expose a failure of *this* unit before starting the next one; where no per-unit check exists, use the nearest executable observation and say what it covers.
4. **Recoverable evidence** — keep the observable result (or the rerunnable check) so the sequence can be replayed by someone else.

Rationale: a break caught at the unit that caused it is cheap to localize; a break caught after a batch is buried and you have already built further on a broken base. *(Source: same file §Why L11.)*

**Delivery order is part of the evidence.** Order the units so the sequence reads as an argument: the canonical shape is the failing check first, then the fix on top; other honest orders are a subtraction before the reshape, a baseline capture before the treatment, the scaffold before the feature. Each unit should land on its own so a reviewer can replay the sequence. *(Source: same file §Delivery L15.)*

Boundaries: this does **not** require a green check, a rebase, or a commit per unit — wide refactors legitimately cannot stay green per unit (see the exception below), and where the per-unit check is expensive, batch sizing and the claim decide. The order is a discipline for finding failures where they happen, not a ritual that produces evidence for its own sake.

## Delivery units and landing

When several units make up one delivery, record per unit what the unit actually needs: its dependencies, what it must preserve, its write surface, the deliverable, the evidence that applies to its claims, and its unknowns. A plan is a delivery object, not evidence: a checkbox, a passing checker or a plan document generates no acceptance by itself. Unit/real-surface/metric boxes, a build step, a review gate and a landing condition are referenced only where the actual task and its accepted policy have them — they are not a fixed three-box shape or a new gate. *(Source: cursor `ecc249f1…`, `pstack/skills/poteto-mode/playbooks/multi-phase-plan.md` and `shipping.md`; scripts are not ported. Gate2 G11 / N-DELIVERY.)*

- **A baseline that lacks the feature is recorded, not fabricated.** When the trunk does not contain the behavior, gate the diff-added behavior and the user-facing terminal state instead of inventing a trunk result. A real-surface check that needs the feature cannot be claimed on trunk by substitution.
- **Incomparable scenarios are not ratio'd.** When a metric gate is used, both sides produce the metric; if the scenarios differ, an absolute budget is one substitute only when the goal's owner has accepted it — it is not self-set without a target. *(Same source.)*
- **Patch-id and rebase discipline.** A verdict binds the object and a change-detection identity (patch-id is a clue, not equivalence). After a rebase/retarget, check the actual object, diff and load-bearing inputs/paths: claims that changed or are unclear are re-checked, while unaffected claims with still-valid coverage may be reused with the basis stated; the noise comparison is one available method, not the only one. A matching commit message or an old SHA's green never substitutes. *(Same source; `change-review.md` §Verdict object and applicability; gate2 N-REUSE.)*
- **Contiguous landing applies inside a real dependency stack.** Where units genuinely depend on each other, land only a contiguous bottom-up verified segment (an unverified lower unit makes the verified upper ones wait) and recompute the frontier and the change identity after each merge; independent work and other legitimate delivery arrangements follow their own graph. *(Same source.)*

Boundaries: no fixed lane count, audit-tick interval, duration threshold, interaction-video mandate, PR header or punctuation rule is imported; duration is not a completion condition, and writing the plan grants no F/acceptance/merge authority. *(Gate2 G11 rejected list.)*

## Wide refactors (the exception)

A **wide refactor** is one mechanical change (rename a column, retype a shared symbol) whose blast radius fans across the codebase, so a single edit breaks many call sites at once and no vertical slice can land green. Do not force it into a tracer bullet; sequence it as **expand–migrate–contract**:

1. **Expand:** add the new form beside the old so nothing breaks.
2. **Migrate:** move call sites over in batches sized by the blast radius (per package, per directory), each batch a work item blocked by the expand; CI stays green batch to batch because the old form still exists.
3. **Contract:** delete the old form once no caller remains, in an item blocked by every migrate batch.

When even the batches cannot stay green alone, keep the sequence but let them share an integration branch and all block a final integrate-and-verify item — green is promised **only there**, and failing intermediate items are not reported as passing. The shared-branch arrangement is optional; it grants no branch, migration or deletion permission (deletion follows `cross-module-design.md` §Method 4).

## Limits

- No mandatory plan mode, no fixed file-count, time or acceptance-criteria thresholds, and no "every item must be completable in under a fixed budget". The four re-split signals guide a judgment; they do not become numeric gates. Size items by what one working session can actually finish and verify in this repo, and say when the basis for the size is an assumption. *(The C8 gate ruling.)*
- No mandatory checkpoint cadence, no per-item human confirmation, and no requirement that every checkpoint run the full suite: the checkpoint verifies what the affected claims need.
- A plan's item list is not the owner's default approval boundary: cross-module changes and deletions follow the existing delegation and the authority rules in `cross-module-design.md`; where the project already has a tracker or cards, keep them as the carrier and leave unfinished work visible rather than opening a second list. *(Same gate ruling.)*
- No fixed layer order (for example storage → API → UI) and no blanket concurrency ban ("shared state or migrations may never run in parallel"): real shared commitments only need coordination, and a small local change does not need this method's ceremony at all.
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
| addy `2686b620fc1fed2e8f60c704839c766b8594c6b6`, `skills/planning-and-task-breakdown/SKILL.md` (§Step 2 Dependency Graph; §Step 3 Slice Vertically with its good/bad contrast; §Step 5 Order and Checkpoint; §Task Sizing Guidelines; §When NOT to use) | Dependency graph first and bottom-up ordering; vertical vs horizontal slice contrast; ordering signals (dependencies first, usable system, high-risk early, a checkpoint cadence); the four re-split signals; skip when the change is trivial. The size table, `Task [N]` template, output files and plan-document template are not imported. |
| cursor `ecc249f1…`, `pstack/skills/poteto-mode/playbooks/shipping.md` and `cursor-team-kit/skills/make-pr-easy-to-review/SKILL.md` | The actual dependency chain a unit sits in (needs/needed-by and the upstream objects that must exist) for the current frontier, with shared-write/topology rules kept in the composition method and no shipping-authorization platform. *(Gate2 MG2.)* |
| cursor `ecc249f1…`, `pstack/skills/poteto-mode/playbooks/{multi-phase-plan,shipping}.md` | Delivery units record what each unit actually needs (dependencies, preservation, write surface, deliverable, applicable evidence, unknowns); the unit/real-surface/metric boxes, build step, review gate and landing condition apply only where the task/accepted policy has them; trunk-without-feature is recorded not fabricated; incomparable scenarios are not ratio'd and an absolute budget needs the goal owner's acceptance; rebase/retarget re-checks affected claims with reuse allowed for unaffected coverage (noise comparison one method among others); contiguous landing applies inside a real dependency stack. No fixed lane count/tick/duration/video/PR-header rules; scripts are not ported. *(Gate2 G11 / N-DELIVERY / N-REUSE.)* |

Authored additions: the "what can this item independently demonstrate" question as the slice test, the support-work rule (enabled behavior plus own checkable result), the dependency-credit rule, and the limits (no context-window guarantee, no tracker mandate, no hardened C8 defaults).
