# Deprecation and migration · candidate method body

- **Status:** candidate distilled under `docs/absorption/2026-10-02/reviews/ORACLE-REVIEW-A1-ADDY-CD.md` (C3, 2026-10-02, source `addy@2686b620`); not yet an accepted reference; creates no authority, trigger, or gate. A fixed-diff review still applies.
- **Method owner when bound:** D/E/F use the migration operations; B/C keep the accepted behavior, identity and compatibility commitments. Technical strategy does not rewrite those commitments.

## Use

Use when something already in use is to be removed or replaced — a system, interface, library, feature, or data shape — and when designing the lifecycle of something new. A purely local, discardable change with no consumers and no persistent data does not need this method.

Two premises, both load-bearing:

- **Code is a liability.** Its value is the functionality it provides, not the lines. When the same functionality can be provided with less code, less complexity or fewer maintained surfaces, the old code should go. Most teams are good at building and weak at removing; this method covers the removal side.
- **Observable behaviour becomes depended on.** Bugs, timing, ordering and undocumented quirks included. Removal therefore needs active migration, not an announcement.

Ask the design-time question when building something new: "how would we remove this in three years?" Clean interfaces, flags kept minimal, and a small exposed surface make that possible later.

## The decision before the migration

Answer these five questions before committing to a deprecation:

1. Does it still provide unique value? If yes, maintain it and stop here.
2. How many consumers depend on it, including undocumented ones? Quantify the actual usage, not the documented usage.
3. Is a replacement available, **or has a valid owner decided to end the capability?** If neither, the replacement comes first — a valid owner can choose termination over migration, but that decision must be recorded as an accepted capability loss, not dressed up as a migration plan.
4. What is the migration cost per consumer, and what is the retention cost over a real horizon? Compare the two; the source's 2–3 year horizon is an example, the actual comparison uses the task's own cost evidence.
5. What does *not* deprecating cost — security exposure, engineer time, complexity, onboarding?

The answers decide whether this is a deprecation at all. They are a decision aid, not a checklist whose completion authorizes removal.

## Advisory versus compulsory

| Type | Meaning | Mechanism |
| --- | --- | --- |
| Advisory (default) | migration is optional; old surface is stable | warnings, documentation, nudges; consumers migrate on their own timeline |
| Compulsory | the old surface has security exposure, blocks progress, or its maintenance cost is unsustainable | a real deadline, **plus** migration tooling, documentation and support |

Compulsory deprecation without tooling and support is an announcement that shifts the work to consumers, not a deprecation. The decision to make a deprecation compulsory belongs to whoever owns the compatibility commitment (B/C in this library's vocabulary), not to the engineer doing the removal.

## Migration

Investigate the actual consumers and their undocumented dependencies first — the documented usage is a lower bound. Then migrate one consumer at a time, per path:

1. find every touchpoint with the deprecated surface (code, config, data, scheduled jobs, external callers)
2. switch the consumer to the replacement
3. verify the behaviour matches on the paths that consumer actually uses
4. remove the old references
5. confirm no regression

**Churn rule.** If you own the infrastructure being deprecated, you are responsible for migrating your consumers or for providing a backward-compatible update that requires no migration. Announcing a removal and leaving consumers to work it out transfers the cost rather than removing it.

### Choosing a migration form

- **Adapter** — keep the old interface, delegate to the new implementation. Use when consumers cannot be touched first.
- **Strangler** — run old and new in parallel and move traffic incrementally. Use when the old and new paths can coexist and the routing can be observed.
- **Flag** — switch consumers one at a time. Use when per-consumer cutover or fast rollback is the risk being managed.
- **Expand/contract** — the data-shape form below.

These are choices, not required stages. A migration with no live consumers needs none of them.

## Persistent data: expand → migrate → contract

Data is the one thing a code re-deploy cannot restore. The dangerous failure is coupling the schema change to the code change: rename a column in the same release that starts using the new name, and during the rollout window old and new code run at once — one of them queries a column that no longer exists.

```
EXPAND              MIGRATE                     CONTRACT
add the new shape,  backfill existing rows,     once no code reads the old
alongside the old   dual-write from the app     shape, drop it in a later,
                                                separate deploy
```

Worked shape — renaming `name` to `full_name`:

1. **Expand.** Add `full_name` as nullable. Deploy. Old code ignores it, so the old read/write path still works; the add is still not free on the engine (see the Rules below).
2. **Dual-write.** Deploy a version that writes both on every insert/update. This only helps once every writer that can touch the row runs it: an old instance, a background job or a batch process still writing only `name` can overwrite or invalidate the backfilled value afterwards. List the active writers before relying on the new column.
3. **Backfill.** Copy `name → full_name` in batches, off the hot path, and measure lock impact on the actual engine. A one-time copy is **not** automatically consistent under concurrent writes, and the two conditions below are additive, not alternatives:
   - **Writer compatibility, or a coordination plan covering the gap.** Every writer that can touch the row writes both columns — or a stated coordination/catch-up plan covers the case where an old writer would write only `name`. This removes the missing-old-writer write. It does **not** make the copy safe by itself.
   - **Backfill concurrency coordination.** The copy must not overwrite a newer value from its own snapshot. Use a mechanism whose actual guarantee can be stated and verified for the engine in use — a transactional read-modify-write, a conditional update on the expected value, a row version check, a re-read/catch-up pass over rows changed during the copy, or freezing the affected rows for its duration. "Only fill rows whose new column is still unset, plus a final pass" is an example of this class, not a universal guarantee; its correctness has to be declared and checked against the engine's actual concurrency behaviour.
   A final whole-table comparison before switching reads is a check, not the coordination design: it detects the disagreement but does not remove the race that produced it.

4. **Switch reads.** Only after the new column is verified to agree with the old one, point the app at `full_name` while still writing both. Deploy, let it bake, and keep a way back to `name`.
5. **Contract.** Before dropping `name`, confirm that no read or write path still depends on it — including old app versions that may still run and background jobs — and that the rollback version is compatible with the post-contract schema. Then stop writing `name`; in a separate, later deploy, drop the old column.

Rules:

- **Additive first, destructive last and alone.** Adding is *compatible with the old shape*, not free: a new nullable column, table or index can still lock rows, rewrite data or change the query plan and resource cost on a real engine. Add relative to a stated compatibility strategy and measure the actual engine impact; drops and renames get their own deploy after no code references the old shape.
- **Each step is independently deployable and individually reversible as code.** Where a data step is genuinely irreversible, declare the backup/restore or forward-fix path, the accepted data loss, and who accepts that risk. Do not write a *down* migration that only pretends to reverse the change — **code rollback does not imply data rollback**, and a false down-path guarantee is worse than an honest irreversible declaration.
- **Backfill in batches, off the hot path.** A single update over many rows can lock the table. The batch size, throttle and lock behaviour are engine-specific and must be measured, not assumed.
- **Build large indexes without blocking writes** where the engine supports it; verify the engine's actual semantics.
- **Decouple the code cutover with a flag when the risk justifies it.** This is a choice, not a requirement, and the flag adds its own cleanup obligation.

## Zombie code

Code that nobody owns but everybody depends on — no recent commits with active consumers, no maintainer, failing tests nobody fixes, dependencies with known vulnerabilities nobody updates, docs pointing at systems that no longer exist. It cannot stay in limbo: either assign an owner and maintain it properly, or deprecate it with a concrete migration (or termination) plan.

Examples, because they differ:

- **Cross-version mixed run (the failure this method exists to prevent).** Two failure shapes with the same cause. (i) A column is renamed in place in the same deploy as the code change: during rollout old instances query `name`, new instances query `full_name`, and one of them fails. (ii) The columns coexist and the app dual-writes, but an old instance, background job or batch writer still updates only `name` after the backfill copied it; `full_name` is now stale and switching reads serves the wrong value. Correct shape: expand → dual-write from **all** active writers → backfill with its own concurrency coordination (step 3) → verify the two shapes agree → switch reads with a fallback → contract only after no read or write path depends on the old shape. Each step separately deployable; the writer-side condition is that every writer that can touch the row is compatible, or a stated coordination/catch-up plan covers the gap — and, on top of that, the backfill still needs the concurrency coordination from step 3.
- **Backfill snapshot race with fully compatible writers.** All active writers already dual-write, so the missing-old-writer failure cannot occur. The backfill reads `name = A`; the app then atomically commits `name = B, full_name = B`; the backfill writes `full_name = A` from its older snapshot. The two columns now disagree, and no stale writer exists. Writer compatibility solves the missing write and nothing about ordering: the copy needs its own coordination as in step 3, and a final comparison before switching reads detects the damage without preventing it.
- **Pure retirement with no live consumers.** An internal module has zero references in code, config, scheduled jobs and external callers. No replacement or migration is needed; the removal still needs the usage evidence (metrics/logs/dependency analysis, not only a text search) and no regression on the accepted surface. This case is legitimate — the method must not invent a replacement requirement for it.

## Provenance is not a reference

"Zero references" retires code; it does not erase history that still has readers. Migration records, schema history, changelogs, incident records, or an external report/report generator may still need the old decision trail or the old name. Check for a reader whose contract is the history, not the live code, before deleting it. Do not use a reference count as the sole criterion for removing provenance.

## Limits

- This method does not require every retirement to build a replacement first or to be production-proven; a valid owner may end a capability. It does not require flags, parallel old/new stacks, in-place renaming bans, or a reversible *down* for every migration. A genuinely irreversible data change is declared as such, with its loss and risk acceptance.
- It does not set deadlines, does not grant release or removal authority, and does not decide compatibility commitments. "Zero active usage" must be supported by evidence, not by a claim.
- Specific engines, lock behaviour, and index-build semantics are version- and product-specific; verify against the actual system rather than treating a source example as universal.

## Source anchors

| Source | Retained contribution |
| --- | --- |
| Addy Osmani, `addyosmani-agent-skills` at `2686b620fc1fed2e8f60c704839c766b8594c6b6`, `skills/deprecation-and-migration/SKILL.md` (`Code Is a Liability`, `The Deprecation Decision`, `Compulsory vs Advisory Deprecation`, `The Migration Process`, `Migration Patterns`, `Zombie Code`, `Red Flags`) | Consumers and undocumented dependencies; migration vs retention cost; advisory/compulsory semantics and their decision source; per-consumer migration and reference cleanup; adapter/strangler/flag tradeoffs; expand → dual-write/backfill → switch reads → contract, batch backfill, index-lock impact, read consistency; zombie code's two options. |
| Same pin, same file (`Rules`, `Common Rationalizations`) | Additive-first, destructive-last. The universal "every migration has a tested down path" claim is narrowed to the irreversibility rule above rather than copied as a blanket requirement. |

Narrowed or excluded from the source: "replacement must be production-proven" as a universal precondition, mandatory flags/dual stacks, and the blanket claim that a migration without a reverse is a deploy that cannot be rolled back.
