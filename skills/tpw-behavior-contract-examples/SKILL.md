---
name: tpw-behavior-contract-examples
description: "Define acceptance conditions with examples and counterexamples, including consumer and acceptance questions. Use when a behavior contract needs observable acceptance; it grants no authority."
license: Local self-use packaging only; no public distribution license granted; upstream MIT notices in THIRD-PARTY-NOTICES.md
metadata:
  package: tpw-skills-packaging-f5d6d054
  status: local-use package
  method-location: this package (skills/tpw-behavior-contract-examples/SKILL.md)
  source-method-historical: professional-workflow/methods/behavior-contract-examples.md @ f5d6d0547459eb15c40aec25617418d5ea4710e6
  source-pin: f5d6d0547459eb15c40aec25617418d5ea4710e6
  source-tree: 9d7c057417da73895cda3b85ec34d49db58669b6
  source-sha256: 6c9ae6ba219f9d4c6eee9739c6fdfb1edb760a50163bfdfeb2ffb47e3a13663e
---

## 包装与资源边界（本机自用固定成品包）

正文逐字节等于**历史固定对象** `professional-workflow/methods/behavior-contract-examples.md` @ `f5d6d0547459eb15c40aec25617418d5ea4710e6`（tree `9d7c057417da73895cda3b85ec34d49db58669b6`）；**现行位置即本包**（该路径 2026-10-11 起已从工作流包摘出，仍可按 pin 取回）。包装只增加本 frontmatter 与本节，不改正文。

- **读取型资源 / 实际条件依赖**：本入口不随包携带额外资源。
- **边界指针**：正文未把职责外派给其他方法文件的指针。
- **来源锚**（正文 Source anchors 段中的上游路径）：是出处记录，不是加载或执行本包的要求；需要这些能力时显式绑定其固定原件。

**正文内的 Status／评审语义**（如 “candidate”“not yet an accepted reference”“fixed-diff review”“尚未”“待审”）描述该正文在吸收批次中的**历史阶段**；**当前的适用与接受依据**是包接受记录 `docs/absorption/2026-10-02/FINAL-ACCEPTANCE.md`（Oracle 2026-10-03 接受，product `8ba69427…` / core `d0cbbfc8…`），全部 gate-reviewed 吸收增量已整合、无 held items。旧评审要求不对已接受对象重复；本包装不重开方法语义，也不由“已安装”推成“已接受”。

`SOURCE.md` 记录固定 pin、逐项校验值与本地包装差异；`THIRD-PARTY-NOTICES.md` 保留上游 MIT 原文。本包许可边界：本机自用，公开发行条款未定。

# Behavior contract examples · candidate method body

- **Status:** candidate distilled under `REVIEW-A3-MATT-ABC` (MG-5) and extended under `REVIEW-A2R-CURSOR-ABC2` (MG-2, 2026-10-02); not yet an accepted reference; creates no authority, trigger, or gate. A fixed-diff review still applies.
- **Method owner when bound:** B behavioral contract. F consumes the conditions when evaluating a claim. Writing conditions, examples, or their observations does not accept the contract, grant implementation authority, or establish evaluation independence.

## Use

Use on demand when a behavior contract or a set of acceptance conditions is written or reviewed, and the question is whether each condition can actually be shown false. This supplements the contract work in `profiles/behavior-domain.md`; it does not replace the contract, the technical Plan, or independent evaluation. A change-slicing or ticket-decomposition method may reference this check for each slice's demoable result.

Carry conditions with their expected outcome, at least one example, and one counterexample, so a fresh reader can tell passing from failing without reconstructing the author's intent.

## Acceptance conditions

For every condition:

1. **Derive it from the artifact, not the request.** State an observable outcome of the changed object. Restating the request ("fix the bug", "improve triage") grades nothing.
2. **Name the falsifying observation.** Say which observation would show the condition false — a command, query, inspection, or fixed manual observation and its failing result — not only the happy path.
3. **Confirm the baseline state** against the commit/work state the implementer starts from:
   - a new-capability condition is expected to fail there;
   - a preservation or compatibility condition may already be true and must stay true — do not drop it for being green;
   - a condition satisfiable only by another work item is a dependency, not this item's delivery: make the blocker explicit instead of counting that item's result as this item's outcome.
4. **Make it independently verifiable.** Concrete and testable for a reader who did not write it. "Triage should work correctly" is not a condition. Not every condition needs an executable automated test; each needs a named observation.
5. **Keep the project's vocabulary.** Use accepted glossary terms where they exist so a condition does not silently rename an accepted concept.

## Consumers and acceptance

Name the consumer class the visible behavior serves before deriving conditions: the end user, the API or library caller, the maintainer who will change this next — possibly several at once. State the specific experience cost or benefit from that class's perspective rather than a generic quality word.

- Acceptance behavior is decided by the authority that owns it (B's accepted contract, with Voice for a human-retained acceptance and the resource/risk authority for trade-offs), not by which consumer class is most convenient to satisfy. Do not equal-weight all classes by default, and do not let "delight" override safety, cost, or an accepted behavior or value policy.
- Reversibility does not create authorization: an easy-to-undo behavior choice is still a contract choice. Make it explicit and route it to the owner instead of settling it by implementation convenience or a default.
- When consumer classes conflict, surface the trade-off in the contract and route the choice; do not silently pick the one that is easiest to implement.

## Examples

- **Increment (expected red at baseline).** "`gh issue list --label needs-triage` returns issues that have been through initial classification"; the baseline observation is that the label is not yet applied.
- **Preservation (may be green at baseline, still required).** "Descriptions under 1024 characters are unchanged" sits beside the new truncation behavior in the source list; passing before the change is not a reason to remove it.
- **External dependency (blocked, not delivered).** "The new export follows the pagination contract from ticket 03": record ticket 03 as a blocker. Until it lands, this condition does not demonstrate this item's result. A cross-item outcome can be a valid upper-level acceptance condition; the sub-item still states the dependency.

## Counterexamples

- A criterion already true at the base commit that is not restating a preservation requirement: it passes before any work and proves nothing about the change.
- A criterion that can only be satisfied by another ticket's work: passing it measures that other work.
- A criterion that restates the request rather than deriving from the artifact: it cannot distinguish done from not-done.
- "Triage should work correctly": vague; nothing can fail it.

## Conditions and exceptions

- Only new or changed capability conditions are expected to be red at baseline; contract and compatibility conditions may be green and must still be held.
- The falsifying observation need not be an automated test; an inspection, query, or fixed manual observation is acceptable when it names the result that shows the condition false.
- If the observation needs access, data, or a real provider beyond the current authorization, use the task's recall path. This method neither self-grants access nor requires every condition to be evaluated end to end.
- What counts as the artifact's observable outcome belongs to B; how it is measured and whether evidence supports it belong to F. A green check is evidence input, not acceptance.

## Limits

- No universal test gate, tracker template, or fixed number or count of conditions.
- This method does not decide implementation structure, does not replace F's evaluation, and does not turn a passed condition into an accepted commitment.
- Later cross-source work may merge this body with another acceptance-criteria source; keep the falsifying-observation, baseline, dependency and preservation operations and the counterexamples above.

## Source anchors

| Source | Pin / path | Section |
| --- | --- | --- |
| Matt Pocock, `mattpocock-skills` | `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`, `skills/engineering/to-tickets/SKILL.md` | §Draft vertical slices (`<vertical-slice-rules>`, L29–36); §4 Quiz the user (L42–55) |
| Matt Pocock, `mattpocock-skills` | same pin, `docs/engineering/to-tickets.md` | §Common questions, "The acceptance criteria graded nothing" (L76–77): three shapes and the falsifying-observation/baseline check |
| Matt Pocock, `mattpocock-skills` | same pin, `skills/engineering/triage/AGENT-BRIEF.md` | §Complete acceptance criteria (L28–30); preservation criterion example (L96) |
| Cursor plugins | `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`, `pstack/skills/principle-experience-first/SKILL.md` | L17: the consumer is whoever consumes the work (end user, importing colleague, next maintainer); explain impact from their perspective |

Consumption pointer added (by this batch) at `profiles/behavior-domain.md` §按需方法入口; F-side pointer at `profiles/evidence-evaluation.md`. `methods/README.md` indexing is Driver's integration step.
