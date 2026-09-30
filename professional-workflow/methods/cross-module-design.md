# Cross-module design method · M4 candidate

- **Method owner:** D technical/system design. B/C keep their accepted behavior and domain decisions.
- **Status:** candidate for the isolated M3 path; not a universal gate.

## Use

Use when the proposed change affects facts, behavior or constraints that another module, responsibility or verifier must rely on. Backbone terms such as coordination surface and implementation interior remain the responsibility vocabulary; the technical terms below do not replace them.

## Method

1. Read the accepted B/C inputs and inspect the relevant system paths. Separate established commitments from observations and assumptions.
2. Identify the interface in its full technical sense: the facts a caller must know, including inputs, outputs, ordering, error behavior, invariants and relevant performance characteristics.
3. Locate the seam where behavior can be substituted or tested. Use the actual dependency shape to choose a useful test path: in-process, locally replaceable, remotely owned behind an adapter, or a true external dependency.
4. Decide which existing checks cover the new behavior. Replace or remove old coverage only when the replacement demonstrably covers its accepted claim; this method does not grant deletion authority.
5. Write a compact Plan with Commitments, Delegated Decisions and Recall Conditions. Keep B/C meanings with their owners; state only the technical coordination others must rely on.
6. Where consumers must remain compatible, prefer an additive change. Keep error behavior predictable for the interface this task actually uses. A valid authority may accept a breaking change; this method does not override that authority.

The terms `module`, `interface`, `seam` and `depth` describe technical design. Depth describes how much useful behavior callers obtain without needing to know the implementation; it is leverage from a compact interface, not a required size ratio. These terms do not assign B/C ownership, determine freshness semantics, create task permission or enlarge the accepted objective.

## Limits

Do not force modules to merge for depth, prescribe each helper, or choose a design solely from file count. Do not import REST, pagination, naming, GraphQL or idempotency rules without a task need. Do not require a fixed number of design alternatives or parallel agents. A local implementation may proceed without this method when it preserves the accepted coordination surface.

## Source anchors

| Source | Retained contribution |
| --- | --- |
| Matt Pocock, `mattpocock-skills` at `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`, `skills/engineering/codebase-design/SKILL.md` (`Glossary`, `Principles`) | Interface facts, seam placement, depth as leverage, and checking whether the abstraction hides the complexity consumers need to know. |
| Same pin, `skills/engineering/codebase-design/DEEPENING.md` (`Dependency categories`, `Testing strategy: replace, don't layer`) | Distinguish dependency shapes to choose tests; replace tests only when the new surface covers the old claim. |
| Addy Osmani, `addyosmani-agent-skills` at `2686b620fc1fed2e8f60c704839c766b8594c6b6`, `skills/api-and-interface-design/SKILL.md` (`Contract First`, `Consistent Error Semantics`, `Prefer Addition Over Modification`) | Define the relevant contract before implementation, keep used error behavior predictable, and prefer compatibility when existing consumers must be preserved. |

`DESIGN-IT-TWICE`, its 3+ parallel-agent count, and idempotency/retention rules are deferred. The independently reviewed candidate dossier at `docs/overnight/2026-10-01/METHOD-CANDIDATES.md` records their status and reasons; that dossier is not an acceptance authority.
