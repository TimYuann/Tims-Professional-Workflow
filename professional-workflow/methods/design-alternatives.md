# Design alternatives · on-demand method (MG-10)

- **Method owner:** D technical/system design. B/C keep behavior and domain decisions; this method recommends, it does not accept.
- **Status:** on-demand reference at a demonstrated gap (comparing genuinely different technical options); a task Charter decides applicability and who owns the choice. It is not a mandatory design review and does not require parallel agents.

## Use

Use when a design decision has real, non-obvious alternatives — an interface shape, a module boundary, a dependency strategy, a seam placement — and the difference matters. Do not run it where the path is settled by an existing pattern, a constraint, or a mechanical change; comparing variants of the same first idea is not comparison.

## Frame

Before comparing options, write down:

- **Constraints** any acceptable option must satisfy: accepted B/C commitments, shared interfaces, error behavior, performance or compatibility boundaries, conventions in the area.
- **The dependencies** the design would rely on and their category (in-process, locally replaceable, remotely owned, true external — `cross-module-design.md` §Method 3 and `guide-mock-adapter-choice.md`).
- **A small illustrative sketch** to make the constraints concrete. It is a way to make the constraint visible, not a proposal; it may be wrong and be dropped.
- **The decision to be made** and what would change it.

## Compare

Develop genuinely different options (two or more; the source's parallel-subagent pattern is one way to get them, not a requirement). For each, state:

- an interface sketch — types, methods, parameters, plus invariants, ordering and error modes as far as they are known;
- a caller usage example, so the option is judged by what using it looks like;
- what the implementation hides behind the interface, and where callers still have to know the implementation;
- dependency strategy and adapters (production + test) — which seam moves, and whether one adapter or two is justified;
- where depth (leverage for callers), locality (where change concentrates) and seam placement land.

Then contrast the options on those axes, using two lenses from the design vocabulary:

- **The deletion thought experiment.** Imagine deleting the module: does complexity vanish (it was a pass-through) or reappear across callers (it was earning its keep)? *(Source: `codebase-design/SKILL.md` §Principles L63.)* Authored caution: this is a heuristic, not an automatic delete rule for thin wrappers. A small adapter may carry authentication, compatibility, audit, or mapping commitments that are not visible in its line count; look at the function and the commitments before concluding from shape.
- **Testability and surface trade-off.** Prefer interfaces that accept dependencies rather than create them and that return results rather than mutating through side channels; fewer methods and simpler parameters mean less test setup. *(Source: same file, §Designing for testability L67–95: accept dependencies L71–81, return results L83–93, small surface L95.)* Authored caveats: side effects are often the accepted behavior, so separate the pure computation from the effect instead of demanding a side-effect-free design; and "fewer methods/parameters" is not by itself correct design — do not trade a needed capability for a smaller count. The interface is the test surface; if you want to test past it, suspect the module shape. *(Same file, §Principles L64.)*

## Recommendation

After comparing, give your own read: which option is strongest and why, in terms of the constraints and the axes above. Be opinionated rather than presenting a menu; proposing a hybrid is fine when elements genuinely combine. If only one option survives the constraints, say that too and name the constraint that settled it.

Do not require the user to confirm every technical option, and do not present the comparison as a decision that has already been accepted: the authority that owns the choice is fixed by the Charter and the accepted commitments (`technical-planning.md` §心智模型).

## Limits

- No fixed number of options, no mandatory parallel agents, no global-optimality proof, and no fixed template for the comparison.
- No new gate, no mandatory design review, no "second opinion" step; the method runs when a real decision exists and its output can be used or discarded.
- Not the place for module-value judgments beyond the comparison above; adapter/mock choice stays in `guide-mock-adapter-choice.md`.
- Recommending does not authorize implementation, acceptance, or deletion.

## Source anchors

| Source | Retained contribution |
| --- | --- |
| Matt Pocock, `mattpocock-skills` at `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`, `skills/engineering/codebase-design/DESIGN-IT-TWICE.md` (§Process 1 Frame L9–17; §2 per-option outputs L32–38; §3 Present and compare L40–44) | Frame constraints and dependency categories; per-option interface, usage example, hidden implementation, dependency strategy/adapters, leverage trade-offs; compare by depth/locality/seam and give an opinionated recommendation or hybrid. |
| Same pin, `skills/engineering/codebase-design/SKILL.md` (§Principles L60–65; §Designing for testability L67–95) | Deletion thought experiment (heuristic); interface-as-test-surface; one adapter vs two; accept dependencies, return results, small surface. |
| Same pin, `skills/engineering/codebase-design/DEEPENING.md` (§Dependency categories L5–25; §Seam discipline L27–31) | The dependency categories used in Frame and in per-option adapter strategy. |

Authored additions: the deletion-test and side-effect caveats, the "fewer methods is not correctness" caution, the settled-path exclusion in Use, and the Limits (no fixed option count, no mandatory review).
