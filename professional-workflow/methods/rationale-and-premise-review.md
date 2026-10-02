# Rationale and premise review · candidate method body

- **Status:** candidate distilled under `REVIEW-A2R-CURSOR-ABC` (MG-1) and extended under `REVIEW-A3-MATT-DEF` (DEF-6, 2026-10-02); not yet an accepted reference; creates no authority, trigger, or gate. A fixed-diff review still applies.
- **Method owner when bound:** supplies historical motivation and premise checks to the judgment the task needs (A/B/C/D, with F handling evidence evaluation). It does not accept a change, resolve a defect, or grant action authority.

## Use

Use on demand when a decision or change depends on why an object has its current shape — a design rationale, a threshold, a defensive pattern, dead code, a regression's history — or when repeated failures under one shared premise make the premise itself the question.

Do not duplicate `methods/local-defect-feedback-loop.md`: competing explanations for an observed defect belong to that method's hypothesis loop. This method investigates historical rationale and premise assumptions; it hands findings to the receiving judgment and does not become a census gate for every question.

Fix the target before searching: a code anchor (paths and line ranges, key symbols, the commits that last touched it, merge-commit PR numbers), a named design decision, or another concrete historical object. If the target is vague, state the interpretation briefly and proceed; the reader can redirect.

## Premise probes

1. Write the premise as one sentence: the assumption every failed or proposed approach shares. This probe applies when a shared-premise pattern actually exists, not as a default step on every task.
2. Before another fix under that premise, name the observation that could distinguish "the premise is wrong" from "the approach was wrong". If no such observation exists, that is the finding — do not keep acting on an unexaminable premise.
3. Actor skew is one case, not the census gate. Take an actor census only when there is a real unequal-allocation risk: the same actors repeatedly hold the failure. A census counts which actors hold the imbalance, not how large it is.
4. Read the result without over-claiming: an even census refutes only the tested skew explanation for the observed failures, not every premise; an uneven census alone does not prove causality.
5. Keep "remove the asymmetry" and "compensate for it" as two compared options. This method does not mandate randomization or rotation, and does not ban retries, buffering, shared pools, or batched hand-offs.
6. Record the premise, the observation, and (when taken) the census; do not start another fix under an unexamined premise.

## Trace and search

7. Trace the lineage through source control first: blame the target lines, follow the file through renames, read substantive commit messages and PR bodies/discussion. Recency is not authority — the current shape is often the accretion of earlier decisions.
8. Search the applicable evidence categories and say which were searched: source control; issue/ticket tracker; long-form design docs; real-time chat; infrastructure observability; error tracking; product/data analytics. One category returning nothing is a result, not a failure.
9. Choose which sources to search by the current question's needs, its load-bearing claims, and the task's valid scope. A source may be left out because the current need does not require it, because the search is already sufficient for the claim, or because the resource envelope stops here; an unavailable or deliberately unsearched source is recorded with its reason and a coverage limit. None of these requires proving the source absolutely irrelevant. Do not report an unsearched source as having returned nothing, and do not write an unsearched question into the Unknown tier as if it had been searched.
10. For a runtime-behavior question, explain the mechanics separately (entry → data → decision → side effects → gotchas) and scale exploration to complexity: one pass for a narrow module, a few angles for a cross-cutting subsystem. Mechanics explain what the code does; motivation lives in the historical record.
11. Code and history are evidence only. Do not cite the code itself as the reason it exists, and do not treat a historical rationale as a currently accepted constraint until a valid authority says so.

## Source evidence

12. Prefer a source that owns the claim — official documentation, source code, a spec, a first-party API — over a secondary write-up about it; follow each claim back to its origin instead of citing the summary.
13. A primary source is not automatically trustworthy or sufficient: record its version or access time, the scope it actually covers, and which claim it supports. A citation proves the source said something, not that the claim holds for this object.
14. Check only the claims the task actually needs; a larger sweep is a scope decision, not a virtue. The citations that need checking are the ones the conclusion actually rests on: read the cited item's load-bearing section and confirm it says what the conclusion claims. Checking every citation, requiring a background agent per claim, or sweeping all seven categories is not required. Delegation or parallel reading is allowed when the task provides the access and resources, but no method mandates a background agent. A citation that could not be checked is recorded as unchecked, never as empty content, and a citation already verified for a valid, appropriately scoped claim is reused rather than re-checked without reason.
15. Record where the finding lives and how the next consumer reaches it, following the repository's existing note convention rather than a hard one-file format or a new registry. Keep facts and decisions separate; a fact may need long-lived evidence, and a decision does not have to come from an interview.
16. When a source is secondary, or a needed source could not be reached, say so. An unavailable access or an empty search is a documented gap with its own evidence condition — not a negative verification result and not proof that the answer does not exist.
17. Source code is evidence about mechanics, never about author intent. When relying on a summary or citation, restore its load-bearing original text first. Example URLs or endpoints in source material are illustrations: do not install them into product code or fixtures as live outbound targets without the task's authorization and its own verification.

## Confidence and gaps

18. Put every claim in a tier and phrase it to match:
    - **Direct:** an explicit textual citation that answers the question ("this exists because X"; cite the source).
    - **Supported:** several indirect items converge; phrase as derived ("the evidence points strongly to X: …"), never as the author's stated reason.
    - **Inferred:** a reasonable reading with no explicit support; hedge and show the inference chain.
    - **Speculative:** a plausible hypothesis with thin evidence; mark it as a guess.
    - **Unknown:** searched with no result; state what was searched and for what.
    These tiers describe how a historical claim is supported; they are not the PASS / FAIL / UNVERIFIED evaluation states. "Unknown" here is an investigation result after a stated search, not a failed verification, and a Direct citation does not by itself verify that a behavior holds.
19. Treat the asker's embedded hypothesis as one candidate among others; do not confirm it because it was asked.
20. Surface contradictions instead of choosing the tidier story; both accounts may hold, or one may be wrong.
21. Do not turn absence of evidence into evidence of absence, and do not retrofit a clean rationale onto messy history. An honest, specific "we don't know" is a valuable result.
22. Name gaps concretely: the question, the sources searched, the queries, what each returned, and which sources were unavailable or unsearched.
23. Reuse existing evidence that already answers the question under a valid, appropriately scoped record; do not repeat a search merely to follow the method.

## Handoff

24. Deliver the question restated, the target/code anchor, findings by tier, competing hypotheses, explicit gaps, and a sources-consulted line per category (including empty and skipped with reasons).
25. Where the investigation feeds a change, convert lineage findings into a constraint set that separates accepted constraints from candidate suggestions: Preserve / Change / Avoid / Risk. A finding is evidence, not an accepted constraint or a decision.
26. The receiving judgment (B/C/D, or F for evidence) decides and, where needed, evaluates independently. This method supplies inputs; it does not accept the change or authorize it.

## Examples and counterexamples

- **Direct.** A PR description stating "this fixes pagination for users with more than 1000 items" is direct evidence for that rationale.
- **Supported, not stated.** A PR title "improve performance" plus a perf label plus commits on the hot path converge: state it as derived, not as "the author said it was for performance".
- **Contradiction.** A ticket says "customer compliance requirement" while the PR says "tech-debt cleanup": present both with citations instead of picking one.
- **Gap.** No chat tool is available in the environment: record "chat not searched — no access", not a guess about what was discussed.
- **Skew over-claim.** A balanced census refutes the tested skew explanation only; it does not prove that no other premise is involved.
- **Borrowed recency.** The most recent commit is not automatically the authoritative rationale.

## Limits

- No fixed failure count, category count, agent count, or mandatory seven-source sweep; the search scales with the task and its access envelope.
- "Supported" remains a derived inference, not an author statement; confidence language must not be upgraded to look more certain.
- This is not a universal reduction: a negative search, a historical citation, and a type-level proof each carry their own evidence conditions. Do not collapse all verification into the confidence tiers or into an expected-failure signal.
- Later cross-source work may merge this body with another rationale/premise source; keep the premise probe, actor-skew limits, lineage trace, tier separation, gap record, and constraint-set handoff operations above.

## Source anchors

| Source | Pin / path | Section |
| --- | --- | --- |
| Cursor plugins | `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`, `pstack/skills/why/SKILL.md` | Operating Posture; Step 1–2 target and code anchor; Step 3 evidence categories, skip rules, recency warning; Step 4–5 synthesize/present; Output Format |
| Cursor plugins | same pin, `pstack/skills/why/references/epistemics.md` | Confidence Tiers; Phrasing Guide; Avoid rationalization; The Sycophancy Trap; When Evidence Contradicts; When Evidence Is Missing; Calibration Check |
| Cursor plugins | same pin, `pstack/skills/why/references/synthesizer-prompt.md` | Output Format (tiers, competing hypotheses, what we don't know, sources consulted); Quality Check |
| Cursor plugins | same pin, `pstack/skills/how/SKILL.md` | Step 1 complexity assessment; Output Format (overview, key concepts, how it works, where things live, gotchas) |
| Cursor plugins | same pin, `pstack/skills/principle-attack-the-premise/SKILL.md` | Pattern (write the premise, actor census, read the skew, remove vs compensate) and Stop |
| Matt Pocock, `mattpocock-skills` | `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`, `skills/engineering/research/SKILL.md` | L10–12: primary sources that own the claim, per-claim citation, save where the repo already keeps such notes |
| Product core | `methods/local-defect-feedback-loop.md` §Method 3 | Mutual pointer: defect failure hypotheses stay with that method; this method does not duplicate them |
