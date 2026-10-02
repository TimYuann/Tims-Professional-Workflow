# Agent text guide · on-demand authoring support (candidate)

- **Status:** candidate distilled under `REVIEW-A3-MATT-ABC` (MG-8/MG-11, 2026-10-02); not yet an accepted reference; creates no authority, trigger, or gate. A fixed-diff review still applies.
- **Use:** when writing or editing a document an agent consumes — a method, a Profile/Charter entry, an `AGENTS.md` / `CLAUDE.md` line, a spec, a ticket, a hand-off, or a runtime prompt. Apply it to the draft in hand: it governs how the text reads, not what it knows, and it is not a whole-repository optimization or a per-sentence evaluation program.

## Pointer / disclosure

1. A context pointer is a line held in context that names out-of-context material and encodes the condition for reaching it. The pointer's wording, not its target, decides how reliably the agent reaches the material; a must-have target behind a weak pointer is a variance bug — sharpen the wording first, and inline only if that fails.
2. Front-load the leading word; write one trigger per distinct branch; collapse synonyms that rename one branch; cut identity the body already carries. An always-loaded pointer earns harder pruning than the body it points at.
3. Two loads: context load (always-loaded lines, spent every turn) and cognitive load (which documents exist and when to reach for them — the human is the index). Material behind a pointer pays only the pointer's line; material with no pointer rides entirely on human memory.
4. Information hierarchy: in-file step → in-file reference → disclosed reference behind a pointer. Progressive disclosure moves branch-specific material down so the top stays legible; co-location keeps one concept's definition, rules, and caveats under one heading; sprawl is cured by the ladder, not by trimming words.
5. Branching is the disclosure test: inline what every branch needs; disclose what only some branches reach. A flat peer-set of rules is a legitimate in-file reference, not a smell.

## Completion

6. Every step ends on a completion criterion. Two properties matter: clarity (can the agent tell done from not-done?) and demand (how much work it forces). The strongest criteria are both checkable and exhaustive ("every modified model accounted for").
7. A vague bound invites premature completion: the visible later steps pull attention forward and a fuzzy criterion cannot hold it back. Defend in order: first sharpen the done condition (local and cheap). Split or hide later steps only when the criterion cannot be further clarified and premature completion or rush has actually been observed — and only across a real context boundary (a hand-off or a separate agent), because an inline call leaves them in context. A necessary split still carries the key authorization and recall semantics with it and needs run resources and delegation the task already has; a general worry is not a reason to add a hand-off, an agent, or a gate.
8. Keep hard guardrails, authorization boundaries, and recall semantics visible even when a default model would obey them. Do not hide safety or permission conditions to prevent premature completion.

## Pruning

9. Keep each meaning in a single source of truth. Duplication costs maintenance and tokens and inflates a meaning's rank; scattering fragments one meaning. Check every line for relevance; without a pruning discipline, stale layers settle (sediment).
10. The environment is a source of truth too (package scripts, config files, directory layout, `--help` output). A document that restates it is a cache: keep only what the agent cannot find by looking — an unwritten convention, the reason behind a choice, a gotcha no config confesses — and leave one-command lookups to the environment.
11. Hunt no-ops sentence by sentence: an instruction the model already obeys by default pays load to change nothing. The test is behavioral and model-relative: delete the sentence and ask whether behavior changed; settle disagreement by running the document, not by debate. When a sentence fails, delete the whole sentence rather than trimming words from it.
12. Prefer a positive target to a prohibition, which drags the forbidden behavior into context; a prohibition earns its place only as a hard guardrail that cannot be phrased positively, and even then pair it with the positive target.

## Environment / pointers (local facts)

13. Point to the environment's own sources of truth and their consumer rules instead of restating them — for example a configured issue-tracker file, a domain-doc consumer rule, a label mapping, or the repo's agent-instruction block. Explore what already exists before proposing structure; do not assume it or recreate it.
14. A semantics-preserving name mapping converts a canonical term to the local name only when both sides mean the same thing. Record the mapping with its meaning, use the glossary's vocabulary in outputs, and surface a conflict with an existing decision record (for example an ADR) explicitly instead of silently overriding it.
15. A mapping does not create labels, permissions, trackers, or rules; a config file existing does not prove an agent consumes it. Do not add a run-once setup gate, a new registry/schema/validator, or re-confirm facts that already exist. For a hand-off pointer, carry the trade-off — which original basis the receiving task needs, what paraphrase loses, which evidence to fix first — while the receiving-side hand-off operations belong to the hand-off method.

## Evidence limits

16. The levers above are authoring heuristics, not proven behavior laws. In particular, leading-word effects, negation backfiring, and "pointer wording decides success" are source-author claims not validated in this package's tasks; present them as hypotheses, not established rules.
17. The no-op test and any improvement claim need a declared model, task, and observation coverage. One run does not establish that all reader-needed information can be deleted. There is no automated eval requirement; use a manual run plus the failure vocabulary (duplication, sediment, no-op, sprawl, premature completion) as the diagnostic.
18. Keep a recoverable diff and a semantic check when pruning: behavior change is the goal, not length. Do not over-fit a document to one model revision; a new model usually calls for another no-op pass rather than a rewrite.
19. Improvement observations are evidence about a specific document, model, and task; they do not prove general effectiveness, do not grant action permission, and do not replace independent evaluation of the work the document describes.

## Examples / counterexamples

- **Weak pointer.** "See `docs/agents/domain.md`." Better: front-load the condition for reaching it, for example when a term or an accepted decision in this area is unresolved.
- **Co-location.** Keep a concept's definition, its rules, and its exceptions under one heading instead of scattering them across sections; a reader who finds one part should meet its neighbors.
- **Completion.** "Understanding reached" is vague; "the unresolved items affecting this task are settled and the remaining unknowns are stated" is checkable.
- **Environment mapping.** Map five canonical triage roles to the repository's actual label strings in one mapping file, with meanings; do not restate the labels in every document that mentions triage.
- **Pruning counterexample (hypothesis, not an observation).** "A line the default model already follows is a no-op to delete" is a model-relative hypothesis: deleting a sentence only shows a no-op if the deletion was actually run on a declared model and task and behavior did not change. Without that observation, treat the sentence as a candidate no-op, not as evidence — and note that removing a task-specific obligation such as "write tests" can change behavior. A hard safety constraint is not a no-op just because the default model usually complies — keep it explicit.

## Limits

- On-demand authoring support only: it does not rewrite the repository, create a framework, or require an evaluation for every sentence.
- It does not change ownership: text craft does not default to domain-semantics ownership, and local mappings do not grant authority or tracker permissions.
- Effectiveness is not claimed; an improvement claim needs its own model/task/observation coverage.

## Source anchors

| Source | Pin / path | Section |
| --- | --- | --- |
| Matt Pocock, `mattpocock-skills` | `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`, `skills/productivity/writing-for-agents/SKILL.md` | §Context pointers (L10–18); §The two loads (L20–27); §Information hierarchy (L29–43); §Steps and completion criteria (L45–52); §When to split (L54–59); §Leading words and negation (L61–74); §Pruning (L76–82) |
| Matt Pocock, `mattpocock-skills` | same pin, `docs/productivity/writing-for-agents.md` | §The levers (L24–30); §Common questions (L32–59): no-op behavioral test, manual run as the check, no per-model rewrite |
| Matt Pocock, `mattpocock-skills` | same pin, `skills/engineering/setup-matt-pocock-skills/SKILL.md` | §1 Explore (L19–30); §4 Write: pointer block to `docs/agents/*.md` (L72–102) |
| Matt Pocock, `mattpocock-skills` | same pin, `skills/engineering/setup-matt-pocock-skills/domain.md` | §Use the glossary's vocabulary (L41–45); §Flag ADR conflicts (L47–51) |
| Matt Pocock, `mattpocock-skills` | same pin, `skills/engineering/setup-matt-pocock-skills/triage-labels.md` | Canonical-role to local-label mapping (L3–15) |

Consumption: on-demand support index in `methods/README.md` (Driver's integration step); no Profile applicability trigger is added by this file.
