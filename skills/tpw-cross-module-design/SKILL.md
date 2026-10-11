---
name: tpw-cross-module-design
description: "Design shared technical commitments and observation surfaces when other modules or verifiers depend on the change. Use for module boundaries, interface depth, seams, adapters, and testability of a cross-module change; not a broad architecture survey and not ordinary feature implementation."
license: Local self-use packaging only; no public distribution license granted; upstream MIT notices in THIRD-PARTY-NOTICES.md
metadata:
  package: tpw-skills-packaging-f5d6d054
  status: local-use package
  method-location: this package (skills/tpw-cross-module-design/SKILL.md)
  source-method-historical: professional-workflow/methods/cross-module-design.md @ f5d6d0547459eb15c40aec25617418d5ea4710e6
  source-pin: f5d6d0547459eb15c40aec25617418d5ea4710e6
  source-tree: 9d7c057417da73895cda3b85ec34d49db58669b6
  source-sha256: 373ff499c9b56a8b5426046c017e7b9ab01770f75e670953489858438665a204
---

## 包装与资源边界（本机自用固定成品包）

正文逐字节等于**历史固定对象** `professional-workflow/methods/cross-module-design.md` @ `f5d6d0547459eb15c40aec25617418d5ea4710e6`（tree `9d7c057417da73895cda3b85ec34d49db58669b6`）；**现行位置即本包**（该路径 2026-10-11 起已从工作流包摘出，仍可按 pin 取回）。包装只增加本 frontmatter 与本节，不改正文。

- **读取型资源**（按需读，随包提供，路径相对本技能目录）：`guide-mock-adapter-choice.md`（依赖／观察面分支）；`design-alternatives.md`（真实方案分歧才读）。二者均为 TPW 方法正文的同字节副本。
- **条件读取的上游原件**：`references/DEEPENING.md`（上游 Matt 原件，逐字节保留）——只在需要原始依赖分类参考时读；其冲突以已接受适配为准，不自动采其删除建议。
- **来源锚**（正文 Source anchors 段中的 testing-patterns、mocking 与上游 SKILL 路径）：是出处记录，不是加载或执行本包的要求；另需其独特能力时显式绑定实际固定版本。

`SOURCE.md` 记录固定 pin、逐项校验值与本地包装差异；`THIRD-PARTY-NOTICES.md` 保留上游 MIT 原文。本包许可边界：本机自用，公开发行条款未定。

# Cross-module design method · M4 accepted reference

- **Method owner:** D technical/system design. B/C keep their accepted behavior and domain decisions.
- **Status:** accepted as a bounded reference for this method need; a task Charter decides applicability and delegated scope. It is not a universal gate.

## Use

Use when the proposed change affects facts, behavior or constraints that another module, responsibility or verifier must rely on. Backbone terms such as coordination surface and implementation interior remain the responsibility vocabulary; the technical terms below do not replace them.

## Method

1. Read the accepted B/C inputs and inspect the relevant system paths. Separate established commitments from observations and assumptions.
2. Identify the interface in its full technical sense: the facts a caller must know, including inputs, outputs, ordering, error behavior, invariants and relevant performance characteristics.

When shaping that interface, use two design lenses. The **deletion thought experiment**: imagine deleting the module — if the complexity vanishes it was a pass-through, if it reappears across callers it was earning its keep. This is a heuristic, not an automatic delete rule for thin adapters: a small wrapper may carry authentication, compatibility, auditing or mapping commitments that its line count does not show, so check the function and the commitments before judging from shape. The **testability trade-off**: accept dependencies instead of creating them, return results instead of mutating through a side channel, and keep the surface small (fewer methods, simpler parameters). Side effects are often the accepted behavior — separate the pure computation from the effect rather than demanding a side-effect-free design — and never trade a needed capability for a smaller method count.
3. Locate the seam where behavior can be substituted or tested. Use the actual dependency shape to choose a useful test path: in-process, locally replaceable, remotely owned behind an adapter, or a true external dependency.

Choose the test double per `guide-mock-adapter-choice.md`. Port/in-memory tests cover the deep module's logic; they do not by themselves verify a production transport/serialization adapter — if that contract is the risk, observe the adapter against a local stub/recorded fixture, or name which real normalization is called by which test (moving logic into an adapter that the test double still replaces does not change coverage), and record the uncovered part. Do not expose internal seams for tests.

Decide the **observation surface while planning**, not after: state how the key behavior will be observed, prefer an existing surface and the surface a caller would use, and say what the chosen surface catches and what it misses, plus what the slower or costlier alternative would catch. One external behavior plus one production adapter can honestly need two surfaces (the adapter's request construction and mapping is a different claim from the port's logic); do not reduce the surface count at the cost of the claim, and do not keep surfaces that contribute nothing to a claim. B owns the observable commitments, D the shared technical surface, F the coverage judgment; local test seams stay with E inside the delegated scope. Changing a shared technical surface follows the recall judgment — does it change a dependency commitment or the validation basis? — not an automatic human ACK.
4. Decide which existing checks cover the new behavior. Replace or remove old coverage only when the replacement demonstrably covers its accepted claim; this method does not grant deletion authority.
5. Write a compact Plan with Commitments, Delegated Decisions and Recall Conditions. Keep B/C meanings with their owners; state only the technical coordination others must rely on. Carry the chosen observation surface, the seams it relies on, and the claims it does not cover, so the next session does not re-derive them.
6. Where consumers must remain compatible, prefer an additive change. Keep error behavior predictable for the interface this task actually uses. A valid authority may accept a breaking change; this method does not override that authority.

The terms `module`, `interface`, `seam` and `depth` describe technical design. Depth describes how much useful behavior callers obtain without needing to know the implementation; it is leverage from a compact interface, not a required size ratio. The interface is the test surface; if a check must reach past it, suspect the module's shape. One adapter means a hypothetical seam, two adapters a real one — do not introduce a seam unless something varies across it. These terms do not assign B/C ownership, determine freshness semantics, create task permission or enlarge the accepted objective.

## Limits

Do not force modules to merge for depth, prescribe each helper, or choose a design solely from file count. Do not import REST, pagination, naming, GraphQL or idempotency rules without a task need. Do not require a fixed number of design alternatives or parallel agents. A local implementation may proceed without this method when it preserves the accepted coordination surface.

## Source anchors

| Source | Retained contribution |
| --- | --- |
| Matt Pocock, `mattpocock-skills` at `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`, `skills/engineering/codebase-design/SKILL.md` (`Glossary` L10–28; `Principles` L60–65, esp. the deletion test L63, interface-as-test-surface L64, one/two adapters L65; `Designing for testability` L67–95, esp. accept dependencies L71–81, return results L83–93, small surface L95) | Interface facts, seam placement, depth as leverage, the deletion thought experiment (as a heuristic), the interface as the test surface, the adapter rule, and the dependency-injection/return-results/small-surface trade-off. |
| Same pin, `skills/engineering/codebase-design/DEEPENING.md` (`Dependency categories` L5–25; `Seam discipline` L27–31; `Testing strategy: replace, don't layer` L32–37) | Distinguish dependency shapes to choose tests; internal vs external seams; replace tests only when the new surface covers the old claim. |
| Same pin, `skills/engineering/to-spec/SKILL.md` (`Process` 2, L15) | Existing seams preferred to new ones; the highest seam as a heuristic, not a hard rule. |
| Same pin, `skills/engineering/tdd/SKILL.md` (`Seams: where tests go` L18–26) | A seam is the public boundary behavior is observed at; tests live at seams, never against internals. |
| Addy Osmani, `addyosmani-agent-skills` at `2686b620fc1fed2e8f60c704839c766b8594c6b6`, `skills/api-and-interface-design/SKILL.md` (`Contract First`, `Consistent Error Semantics`, `Prefer Addition Over Modification`) | Define the relevant contract before implementation, keep used error behavior predictable, and prefer compatibility when existing consumers must be preserved. |

`DESIGN-IT-TWICE`, its 3+ parallel-agent count, and idempotency/retention rules are deferred. The comparison frame without the parallel-agent pattern is available on demand as `design-alternatives.md`.
