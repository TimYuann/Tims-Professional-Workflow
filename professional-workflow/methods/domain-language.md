# Domain language · on-demand method (MG-7 + MG-11)

- **Method owner:** C domain semantics for term meaning and accepted rules; the consuming task keeps its own naming. This method is not a full domain-modeling method.
- **Status:** on-demand reference at a demonstrated gap (resolving terms and mapping local names); a task Charter decides applicability. It creates no label, registry, or schema.

## Use

Use when a term, concept, or local label has to be pinned, clarified, or mapped during real work: a conflict between names, a fuzzy or overloaded term, a local vocabulary that must stay consistent with the canonical one. Do not use it as a substitute for domain modeling itself: relationships, state machines, and invariants need their own basis (`profiles/behavior-domain.md` §心智模型 C).

## Resolve terms

- **Challenge against the glossary.** When usage conflicts with an existing domain term, call it out immediately and ask which meaning is intended. *(Source: matt `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`, `skills/engineering/domain-modeling/SKILL.md` §Challenge against the glossary L44–46.)*
- **Sharpen fuzzy language.** When a term is vague or overloaded, propose one precise canonical term and name the alternatives it replaces. *(Source: same file, §Sharpen fuzzy language L48–50.)*
- **Stress-test with concrete scenarios.** Invent edge-case scenarios that force the boundary between two concepts to be stated. *(Source: same file, §Discuss concrete scenarios L52–54.)*
- **Definition shape.** One or two sentences; define what the concept **is**, not what it does. Pick the best term and list the words to avoid for this context. *(Source: `CONTEXT-FORMAT.md` §Rules L25–30.)*
- Include a term only when it is specific to this context; general programming concepts (timeouts, error types, utility patterns) do not belong even if used heavily. *(Source: same file, L29.)* Authored clarification: a general-looking word that has a special meaning here may be recorded with that meaning — the rule excludes generic vocabulary, not domain-specific senses of common words.
- Group related terms under subheadings when a cluster emerges. *(Source: same file, L30.)*
- The avoid-list is context-local disambiguation; it does not make a synonym illegal in another context, and it is not a global word ban. *(Authored qualification of L27.)*

## Cross-check scenarios and code

- When a claim is made about how something works, check whether the code agrees; on a contradiction, surface it explicitly ("the code cancels entire Orders, but you said partial cancellation is possible — which is right?") rather than resolving it silently. *(Source: `domain-modeling/SKILL.md` §Cross-reference with code L56–58.)*
- Authored boundary: the code proves the current implementation, not automatically the accepted business rule; a spoken statement does not automatically beat an accepted rule either. Contradictions go to the semantics owner for a decision — this method records the conflict, it does not settle ownership.
- When only the code and local records were consulted, state that the relevant history was not covered; do not claim the history is unavailable or that only a person could know it. *(Authored.)*

## Record and scope

- Record an accepted clarification where the repo keeps its domain documentation, following the existing owner docs (no fixed filename is required). Create it lazily, when the first term or decision is actually resolved. *(Source: `domain-modeling/SKILL.md` §Update CONTEXT.md inline L60–62; §File structure L40; `CONTEXT-FORMAT.md` §Single vs multi-context L54–60.)*
- Update in place as terms resolve; do not batch clarifications into a later cleanup. *(Source: same file, L62.)*
- Keep status honest: "resolved" is not "accepted". Do not present a proposal, a scratch note, or an implementation decision as current domain language.
- The glossary-style document is a glossary and nothing else: it must not become a spec, a scratch pad, or a container for implementation decisions. Domain work may challenge terms, test scenarios and clarify conflicts, but those activities' other outputs belong in their own carriers. *(Source: `domain-modeling/SKILL.md` L64.)*
- With multiple contexts, the map points to each context's document; infer the relevant context from the topic and ask when it is unclear. *(Source: `CONTEXT-FORMAT.md` §Single vs multi-context L54–60.)*

## Local name mappings

Local environments keep their own names for shared concepts (tracker labels, label strings, tool/role names). Map them deliberately:

- Map **canonical term → local name** only where both sides mean the same thing; the mapping preserves semantics rather than translating words. *(Source: `skills/engineering/setup-matt-pocock-skills/triage-labels.md` L3–14.)*
- Read the existing local convention first — what is already recorded in this repo — and propose only what the current task needs; do not assume a fresh scaffold is wanted. *(Source: `setup-matt-pocock-skills/SKILL.md` §1 Explore L19–30; §2 Section C L59–61.)*
- The mapping creates no label, permission, tracker rule, or consumption guarantee: a config file existing does not prove an agent reads it. *(Authored.)*
- Where canonical and local names conflict, route the conflict to the semantics owner instead of forcing a translation; language mapping is not business equivalence. *(Authored.)*
- Record the mapping once where the local facts already live (task input or the repo's owner doc); do not fork a general method or build a per-repo configuration platform for it. How the consuming task reads that record stays with the task input and the Charter.
- Previously established local facts are not re-confirmed on every task.

## Limits

- No new registry, schema, validator, or per-repo configuration platform; no run-once "setup before use" gate.
- No claim of full domain-modeling coverage: this method covers term resolution, conflict surfacing, and local mapping only. If a task needs relationships, state, or invariants modeled, that needs its own basis.
- Does not create C/D/B authority, decide which meaning wins, or grant implementation permission.
- See `decision-record.md` for recording the decisions that come out of these clarifications; the two are separate carriers with different owners.

## Source anchors

| Source | Retained contribution |
| --- | --- |
| Matt Pocock, `mattpocock-skills` at `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`, `skills/engineering/domain-modeling/SKILL.md` (§During the session L42–64; §File structure L40) | Challenge against the glossary; sharpen fuzzy language; concrete edge-case scenarios; cross-reference with code and surface contradictions; update inline; glossary-only boundary; lazy creation. |
| Same pin, `skills/engineering/domain-modeling/CONTEXT-FORMAT.md` (§Rules L25–30; §Single vs multi-context L32–60) | Opinionated canonical term with avoid-list; tight definitions; context-specific terms; grouping; single vs multi-context layout. |
| Same pin, `skills/engineering/setup-matt-pocock-skills/SKILL.md` (§1 Explore L19–30; §2 Section C L59–61) | Read the existing convention before writing; single vs multi-context choice; one section at a time with a recommended answer. |
| Same pin, `skills/engineering/setup-matt-pocock-skills/domain.md` (L5–11, L41–45) | Read the existing domain docs before exploring; use the glossary's vocabulary in output. |
| Same pin, `skills/engineering/setup-matt-pocock-skills/triage-labels.md` (L3–14) | Canonical-to-local label mapping that preserves meaning and stays editable locally. |

Authored additions: the code-vs-accepted-rule boundary, the honest-history statement for local-only checks, the status honesty rule, the no-configuration-guarantee and conflict-routing rules for mappings, and the Limits.
