# Professional explanation · on-demand guide (MG-4)

Status: on-demand guide at a demonstrated gap; creates no authority, generator, or gate. Source anchors and authored additions are marked. It explains professional state and decisions to a person; it does not change the object and it is not a teaching workspace.

## Use

On demand, when a person needs to understand something — a change, a subsystem, a decision, a current state — rather than to receive a status report. The goal is that they understand it, not that anything changes. Pair it with `handoff-and-resume.md` §Reconstruct and status when the question is "where does this stand"; this guide is for the "help me understand" case.

## Audience

- **Choose the few things this person should walk away understanding**, from why they are asking (about to change it, reviewing it, debugging it, new to it) and what they already know, read from the conversation rather than quizzed out of them. Skip what they plainly know; put the depth where their question is. *(Source: cursor `ecc249f1…`, `pstack/skills/teach/SKILL.md` step 1 L13.)*
- **Keep it a conversation, not a lecture.** Offer to go deeper or move on and follow their lead. Do not print framing labels ("the one idea to hold onto", "TL;DR", "at its core") and do not announce that a part is important or hard. *(Source: same file, steps 3–4 L15–16.)*
- **No quiz.** Understanding does not need to be tested back; capability training is a different task with its own goals, and this guide is not that task. *(Source: same file L16; the review's boundary.)*

## Mechanism and evidence

- Explain **what the thing is** (a plain definition, with its common name if it has one), then tie it to the case at hand, then how it works, then the deeper reasons and edge cases. *(Source: same file, step 3 L15.)*
- **Keep the confidence language of the reasons intact.** A hedge in a rationale is a finding, not style; flattening it fabricates certainty. *(Source: same file L11.)*
- **State the concrete mechanism, not a metaphor or a framing.** Explain the problem each part solves and how it actually works; listing functions and constants is reference, not explanation. *(Source: same file, steps 3 and 5 L15–19.)*
- **Smallest complete answer first** — a sentence or two — then add layers when asked, rather than opening with a dense wall. *(Source: same file, step 3 L15.)*
- **Show, don't only tell.** When a picture lands faster than words, build it up diagram by diagram: for three or more moving parts, draw a short series where each redraw adds a single part, so the reader watches the system assemble. One all-at-once diagram is a reference, not an explanation. *(Source: same file, step 5 L17.)* Authored boundary: this is a technique, not a rule — no fixed number of diagrams and no requirement to generate an image when words suffice.
- **Run the needed investigation rather than redoing it by hand**: read the code to orient yourself, then use the available how/why (or source) work for mechanism and rationale; match the depth to the question and keep the rationale search deliberately narrow unless the reasons are the point. *(Source: same file, step 2 L14.)* Authored boundary: no mandatory how+why invocation for every explanation.
- Write it plainly: prefer the concrete mechanism over a metaphor or a preview of what is coming, keep one name per concept, and cut filler. Carrier expression follows the agent-text guide when that guide is bound; this guide owns the professional content, not the writing craft. *(Source: same file L19; the division of labor from the review.)*

## Expression rules

These rules decide whether the explanation can be followed at all; they are on-demand and apply to the shape of the explanation, not to every engineering artifact. *(Source: matt `c55ee460…`, `skills/in-progress/writing-beats/SKILL.md` and `writing-shape/SKILL.md`; the source's literary workflow is not imported as a default.)*

- **Ground a concept before a block leans on it.** Settle up front what the audience already knows (the prerequisites); everything else must be grounded by an earlier block before a later one can lean on it. The unit is the concept, not the word for it: a block can lean on an idea the reader lacks even with no jargon in sight, and where the concept has a name, the idea and the term land together. Keep a running list of what is grounded; when the next move needs an ungrounded concept, that is itself the answer — ground it first (here or earlier) or promote it to a prerequisite. *(Same source, §Grounding.)*
- **Choose the form deliberately and say why.** Prose carries an argument; a list carries parallel items (if they are not truly parallel, prose is better). A callout only when the aside would genuinely derail the main line. A table when the same shape repeats with the same fields; otherwise prose with bold leads. Quote when the original wording is the point; paraphrase when only the idea matters. A code block for anything multi-line or runnable; inline code for a single identifier. *(Same source, `writing-shape/SKILL.md` §Format arguments.)*
- **The raw material is a quarry, not a script.** A fragment may be split, merged, reworked or paraphrased to fit the surrounding explanation; the explanation must read as one voice. If the material lacks something the explanation needs (an example, a step), name the gap rather than inventing the missing material. *(Same source, `writing-beats/SKILL.md` §Pulling from the pile, `writing-shape/SKILL.md` §Pulling from the pile.)*
- **Preserve in-flight edits.** Re-read the document from disk before every write — the human may have edited it between turns — and preserve their changes; append or edit only the section in scope rather than overwriting the whole document. *(Same source, §Writing rhythm.)*
- **Make a long explanation navigable, without a fixed layout.** When the explanation is long or spans several kinds of material, collect its headings, code blocks, diagrams and cross-references first, then organize it with a short overview of purpose/scope/audience, a section structure (a table of contents or equivalent) the reader can jump around in, and references that let a reader go deeper into the related docs or source. The source for this is self-labelled a placeholder: its unfinished host implementation is not imported, and the format follows the library/project convention — no mandatory card set, sentence count or alphabetical order. *(Source: cursor `ecc249f1…`, `docs-canvas/skills/docs-canvas/SKILL.md` — organization only, host implementation deferred; gate2 MG3 ruling.)*

## Report scope

- **The explanation is the deliverable, not a report about what you did or delivered.** A reply that narrates the work instead of producing the explanation has missed the object. *(Source: `teach/SKILL.md` §Reply L21.)*
- **Keep the epistemic classes visible.** State which parts are observed facts, which are inference, and which are unknown; say what would settle an open question. (This mirrors the Voice/A profile's fact/assumption/unknown split.) *(Authored, consistent with `profiles/intent-voice.md`.)*
- **When the explanation includes history or status, bound it by the record.** Use the actual evidence range and say which range was used; base claims on the commits/diffs or records examined; exclude merge commits and uncommitted work unless the scope includes them; omit cosmetic-only changes; do not infer intent or motivation from a commit — describe changes functionally. *(Source: cursor `ecc249f1…`, `cursor-team-kit/skills/weekly-review/SKILL.md` §Guardrails L23–27; `what-did-i-get-done/SKILL.md` §Guardrails L20–25 and §Workflow L12–18.)*
- **"Committed", "merged", "deployed" each need their own evidence.** An authored commit does not prove something shipped, and a merge commit may carry real integration; state the level the evidence actually supports. *(Authored; the review's status-honesty boundary.)*
- **If the identity or record needed is unclear**, use an explicit verifiable range and state the limitation rather than inventing a narrative or demanding an environment change. *(Authored; `handoff-and-resume.md` §Reconstruct and status has the same rule.)*
- **Sanitize before any public output**; redact private context and secrets. *(Source: `recall/SKILL.md` L33; `guide-redacted-evidence.md` for custody.)*

## Limits

- No mandatory how+why run, no fixed diagram count, no image-generation requirement, no enforced language or tone, no "three nodes need three pictures" or "three repeats must be a table" rule, and no docs-canvas host implementation or fixed layout (card set/heading count/ordering).
- The expression rules do not make a literary workflow the default: no forced candidate openings or beat-by-beat approval by the owner, no requirement that every paragraph be chosen by a human, no command to expand the whole raw pile, no requirement to coin a term, and no rule that source material is always immutable when the author has explicitly asked for it to be edited. The concept/grounding list is a working device, not published structure, and accepted material stays distinguishable from candidate material.
- Understanding-level explanation does not need a quiz; it also does not replace acceptance, review, verification, or a capability-training task.
- The guide changes no object and grants no action permission; it explains an object's state and rationale without altering it.
- Explanations that would expose private transcripts, credentials, customer data, or unrelated work are out of scope; read only what the authorized scope allows and sanitize.
- This guide does not create a persistent teaching/learning workspace (that is a different mechanism and is not part of this package).

## Source anchors

| Source | Pin / path | Section |
| --- | --- | --- |
| cursor-plugins | `ecc249f1…`, `pstack/skills/teach/SKILL.md` | What/why and confidence language L9–11; steps 1–5 L13–19; reply L21 |
| cursor-plugins | `ecc249f1…`, `pstack/skills/recall/SKILL.md` | Output contract L24–33 (cite by source; sanitize before public output) |
| cursor-plugins | `ecc249f1…`, `cursor-team-kit/skills/weekly-review/SKILL.md` | §Workflow L12–21; §Guardrails L23–27 |
| cursor-plugins | `ecc249f1…`, `cursor-team-kit/skills/what-did-i-get-done/SKILL.md` | §Workflow L12–18; §Guardrails L20–25 |
| cursor-plugins | `ecc249f1…`, `pstack/skills/bro/SKILL.md` (L1–7) and `pstack/skills/unslop/SKILL.md` (rules 3–33); usage notes in `pstack/docs/guide/10-recipes-and-pitfalls.md` | Plain-spoken restatement and AI-tell removal for the explanation's surface; carrier expression stays with the agent-text guide. |
| cursor-plugins | `ecc249f1…`, `docs-canvas/skills/docs-canvas/SKILL.md` | Navigable long-form organization (overview/scope/audience, section structure/table of contents, references to related material); the source is a placeholder, so its host implementation is deferred and the format follows the project convention. *(Gate2 MG3.)* |
| matt `c55ee46073ed923f86ce59a5eb3b6d895095d1b7` | `skills/in-progress/writing-beats/SKILL.md` L9–67; `writing-shape/SKILL.md` L21–77; `writing-fragments/SKILL.md` L23–41 | Ground concepts before leaning on them; prerequisites vs introduced; deliberate form choice; raw material as a quarry with gaps named; preserve in-flight edits. The literary session workflow, forced openings and owner-approval rhythm are not imported. |

Authored additions: the explanation-vs-report scope, the epistemic-class rule, the committed/merged/deployed evidence separation, the no-quiz/no-mandatory-how+why/no-fixed-diagram boundaries, the navigable long-form organization, and the sanitize/scope boundary.
