# Architecture survey · candidate method body

- **Status:** candidate distilled under `REVIEW-A3-MATT-DEF` (DEF-3, 2026-10-02); not yet an accepted reference; creates no authority, trigger, or gate. A fixed-diff review still applies.
- **Method owner when bound:** D technical/system design. The survey produces candidates and evidence; it does not change code and does not decide the refactor. The responsible B/C/D authorities keep their decisions.

## Use

Use on demand when a task asks for an architecture or system survey — finding structural friction worth a candidate change — not as a default step of every change or every session. A survey may legitimately end with "no well-founded candidate"; that is a result, not a failure.

## Scope

1. Fix the pain point or direction first. If the requester named a module, subsystem, or pain point, take it and skip the inference below. Otherwise walk back a good stretch of commit history (`git log --oneline`) to find the hot spots — the files and areas that keep coming up — and let those paths pull attention first; if the changes are scattered with no clear hot spot, widen the net.
2. Read the project's domain glossary and the decision records in the area first; a candidate that contradicts an accepted decision is surfaced only when the friction is real enough to warrant revisiting it.
3. Change history is a clue, not a ranking law: frequently changed code is not automatically bad architecture, and rarely changed code may still carry critical risk. Use the history to choose where to look, then examine the actual structure.
4. Keep the survey bounded to the stated direction or pain point; it does not expand its own scope.

## Evidence

5. Walk the codebase and note where understanding is hard: concepts that require bouncing between many small modules; shallow modules whose interface is nearly as complex as the implementation; extracted pure functions whose real bugs live in how they are called; modules that leak across their seams; areas untested or hard to test through their current interface.
6. Apply the deletion test to a suspected shallow module: would deleting it concentrate complexity, or just move it? A "concentrates" signal supports the candidate. A thin wrapper that genuinely delivers authentication, compatibility, audit, or another accepted commitment is not shallow just because it looks small — inspect the function it performs.
7. Separate observed friction from the proposed fix. Each candidate names the affected object and the friction, and its benefit and cost statements are tied to that evidence.
8. Grade evidence strength per candidate, not once for the survey. The source uses `Strong` / `Worth exploring` / `Speculative`; a weak candidate is marked weak rather than presented as a conclusion.

## Candidates

9. For each candidate record: the files or objects involved; the problem — why the current shape causes friction; the plain-language change; benefits expressed as locality and leverage and how tests would improve; and a before/after picture where it helps. Keep the project's domain vocabulary for the domain and the codebase-design vocabulary for the architecture.
10. If a candidate contradicts an accepted decision record, mark that clearly and only when the friction justifies reopening the decision; do not list every theoretically forbidden refactor.
11. End with a top recommendation, or state that no candidate has enough evidence. The presentation channel is the task's own (the source's HTML report is one example, not a requirement).
12. The survey does not implement and does not create a rejection ledger. A rejection whose reason a future survey would need goes through the decision-record method; ephemeral reasons ("not worth it right now") do not need a record.

## Conditions and exceptions

- The survey is evidence gathering for a possible change; accepting a candidate, designing the new shape, and implementing it remain separate decisions with their own authorities.
- A survey that finds nothing actionable should say what it examined and why no candidate met the bar, rather than inventing a finding.
- An accepted decision record is not automatically final, but the survey cannot override it; it can only present the friction that argues for revisiting it.

## Limits

- No default deepening, no mandatory HTML report, no candidate per session, no fixed candidate count, and no mandatory finding.
- The survey does not create implementation authority, change accepted behavior or domain meaning, or grant migration or deletion permission.
- Later cross-source work may merge this body with another architecture-survey source; keep the pain-point-first scope, the history-is-a-clue and deletion-test operations, the per-candidate benefit/cost/evidence-strength record, the "no well-founded candidate" outcome, and the rejection-to-decision-record path.

## Source anchors

| Source | Pin / path | Section |
| --- | --- | --- |
| Matt Pocock, `mattpocock-skills` | `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`, `skills/engineering/improve-codebase-architecture/SKILL.md` | §1 Explore (L18–35): scope before scan, hot spots from history, friction list, deletion test; §2 Present candidates (L37–56): candidate card, recommendation strength, top recommendation, ADR conflicts; §3 Grilling loop (L62–70): rejection with a load-bearing reason goes to an ADR offer |
| Product core | `methods/cross-module-design.md` §Source anchors | codebase-design vocabulary and the seam/depth terms the survey reports against |
