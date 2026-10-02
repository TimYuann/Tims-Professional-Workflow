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
