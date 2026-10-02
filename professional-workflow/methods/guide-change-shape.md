# Change shape and reader load · on-demand guide (MG-2)

Status: on-demand guide at a demonstrated gap; creates no authority, generator, or gate. Source anchors and authored additions are marked.

## Use

On demand, when a change's *shape* is being decided or questioned: which consumers it serves, what it makes a reader carry, what should be deleted before building, and whether the current design should be treated as an alternative to redesign. It complements `cross-module-design.md` (interface facts, seams, depth) and `design-alternatives.md` (comparing genuinely different options); it does not replace either, and it is not a style checklist to apply to every diff.

## Consumers and cost

The user is whoever consumes the work: for a UI the end user, for a library or internal API the colleague who imports it, and the engineer who maintains the code next. Weigh their experience and explain impact from their perspective. *(Source: cursor `ecc249f1…`, `pstack/skills/principle-experience-first/SKILL.md` L9–17.)*

The target rules that follow: every feature, control and option must be justified; ship fewer polished things over more rough ones; prototype before committing when a design decision is at stake (`bounded-prototype.md`); get the details right (transitions, alignment, spacing, feedback, error states); tighten the core loop so each feature serves the central workflow or gets out of the way. *(Source: same file, L11–15.)*

Authored boundaries:

- These rules are a **trade-off stance, not an authority**: delight does not override safety, cost, accepted behavior, or a value policy, and the consumers are not equal in decision power. The effective A/B or resource authority decides the trade-off; this guide supplies the consumer perspective, not the decision.
- A maintenance cost can be paid deliberately (a compatibility layer, a generated file) when the accepted commitment requires it; "the maintainer would prefer it simpler" is an argument, not an acceptance.

## Reader load: the two axes

Maintainability is the work a reader must do to understand the code. Track two independent axes: *(Source: cursor `ecc249f1…`, `pstack/skills/principle-minimize-reader-load/SKILL.md` L9–13.)*

1. **Layers to trace** — how many indirections sit between the question and the answer.
2. **State to hold** — how much hidden or mutable context the reader must keep in mind.

LOC, cyclomatic complexity and "clean architecture" are proxies for these, not the thing itself. The axes are independent: a flat file with fifty globals can be as hard to reason about as a six-layer adapter stack, so "flatten everything" is not the goal. *(Source: same file, L13.)*

The pattern *(Source: same file, L15–21)*:

- **Collapse layers that cost more than they save:** wrappers with one caller, adapters with no second implementation, speculative indirection that was never needed.
- **Make adjacent layers change the abstraction.** A layer that repeats the same methods and arguments adds reader load without compressing anything.
- **Demand interface compression.** A broad interface that hides little complexity makes readers learn both the surface and the implementation; prefer boundaries that hide meaningful decisions.
- **Shrink state scope:** pure functions over mutation, locals over fields, fields over module state, module state over globals; derive instead of sync.
- **Name the invariant at the boundary,** not in every consumer, so a reader learns it once.
- Before adding a layer or a piece of state, ask whether it reduces reader load somewhere else by at least as much.

The test is a question, not a metric: can a new reader answer "where does X come from?" and "what can change X?" without tracing the whole system? Treat the common "under 30 seconds" phrasing as a heuristic, not a threshold to enforce. *(Source: same file, L23.)*

Counterexamples to keep: a legitimate thin wrapper that carries authentication, compatibility, audit, or mapping commitments is not removable just because it is thin (`cross-module-design.md` §Method 2 has the same caveat); a clear, local, stable branch needs no abstraction; a deliberate compatibility layer with real external consumers may be the right cost.

## Subtraction before construction

Default to removing complexity before adding: look for what can be deleted before what can be built; keep the call hierarchy flat; consolidate a repeated decision behind one source of truth; make the smallest change that solves the problem; question a task that asks to thread a new signal through types, schemas, or pipelines; remove small pass-throughs and representation leaks before they spread. *(Source: cursor `ecc249f1…`, `pstack/skills/principle-laziness-protocol/SKILL.md` L9–16.)*

Sequence removal before construction — cut before polishing, design for observed usage rather than speculative edge cases, add no validator/parser/guard beyond what the accepted work demands, and delete a reference with no novel content rather than leaving a stub. *(Source: cursor `ecc249f1…`, `pstack/skills/principle-subtract-before-you-add/SKILL.md` L9–21.)*

The test for the shape: if a human developer would find the code exhausting to maintain, it is a bad solution — but that is a judgment made with the axes above, not a line count. *(Source: laziness-protocol L18.)*

## Ordering the work: data shape, sharing, scaffold

- **Data shape before logic.** Define the core types early, trace every access pattern, and choose structures that match the dominant paths; structural decisions protect option value while code-level decisions protect simplicity. *(Source: cursor `ecc249f1…`, `pstack/skills/principle-foundational-thinking/SKILL.md` L9–13.)*
- **Before sharing state between actors, ask what happens if another actor modifies it concurrently.** If the answer is not "nothing", isolate. *(Source: same file, L15.)* The write-set/serialization arrangement is the Driver/D–E side; this guide only raises the question.
- **Scaffold first where it helps every later phase** (setup before features, tests before fixes), and subtraction comes before scaffolding: remove dead code first, then lay foundations. Each increment should land a coherent abstraction or deepen an existing one rather than spreading a new capability across callers as special-case coordination. *(Source: same file, L17–21.)*
- Authored boundary: scaffold is sized to the task's accepted reliability level, not to a hypothetical future — do not build infrastructure because a later phase might want it, and do not treat "scaffold first" as a mandate in a clear, small, local change. *(Source tension noted in the review of `foundational-thinking`; the robustness-proportionality rule applies.)*

## Integrating a change: redesign as an alternative

When a new requirement is being integrated, consider the alternative of treating it as if it had been a foundational assumption from the start: read all affected files and understand the current design; ask "if we were writing this with this requirement from the outset, what would we build?"; propagate the change through every reference (types, docs, examples, rationale); think the whole redesign and deliver it incrementally. *(Source: cursor `ecc249f1…`, `pstack/skills/principle-redesign-from-first-principles/SKILL.md` L9–16; `design-alternatives.md` §Compare for the option comparison itself.)*

Authored boundaries: this is an **alternative to weigh, not an obligation**; it does not authorize a big-bang rewrite, and it does not by itself permit intermediate breakage or migration of external commitments — those are D decisions inside accepted constraints, and the outcome/migration operational face is handled elsewhere. Preserve the current design's accepted behavior while the alternative is only a proposal.

## Limits

- No fixed number of design options (2–3 is not a quota), no fixed layer count, no enforced 30-second threshold, and no requirement to build a scaffold.
- Not "always delete" and not "always flatten": the two reader-load axes are independent, and deletion/flattening that raises hidden state is a regression. Single-caller wrappers and adapters are heuristics, not automatic deletions.
- Not every guard is speculative: an authorized input-validation contract can require one.
- Shape choices inside the coordination surface stay with D/E; consumer trade-offs are decided by the effective authority; this guide changes no accepted behavior, grants no implementation or deletion permission, and does not replace the Charter.
- A written shape decision that matters is recorded per `decision-record.md`; it does not become an accepted commitment from this guide.

## Source anchors

| Source | Pin / path | Section |
| --- | --- | --- |
| cursor-plugins | `ecc249f1…`, `pstack/skills/principle-experience-first/SKILL.md` | Target rules L9–17 |
| cursor-plugins | `ecc249f1…`, `pstack/skills/principle-minimize-reader-load/SKILL.md` | Two axes L9–13; pattern L15–21; the test L23 |
| cursor-plugins | `ecc249f1…`, `pstack/skills/principle-laziness-protocol/SKILL.md` | L9–18 |
| cursor-plugins | `ecc249f1…`, `pstack/skills/principle-subtract-before-you-add/SKILL.md` | L9–21 |
| cursor-plugins | `ecc249f1…`, `pstack/skills/principle-foundational-thinking/SKILL.md` | L9–21 |
| cursor-plugins | `ecc249f1…`, `pstack/skills/principle-redesign-from-first-principles/SKILL.md` | L9–16 |
| cursor-plugins | `ecc249f1…`, `pstack/skills/principle-guard-the-context-window/SKILL.md` | L9–16 (the reader-load analogue: isolate large payloads, keep frequent content inline, size phases) |

Authored additions: the consumer-authority boundary, the maintainer-cost-as-argument rule, the counterexamples (auth/compat wrapper, clear local branch, deliberate compatibility layer), the scaffold-proportionality boundary, the redesign-is-an-alternative boundary, and the Limits.
