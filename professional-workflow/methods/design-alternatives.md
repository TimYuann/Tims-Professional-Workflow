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

## Synthesis from candidates

When several candidates for the same object actually exist — the options above, or parallel attempts at one artifact — combining them is a synthesis with its own rules, not a copy of the winner: *(Source: cursor `ecc249f1…`, `pstack/skills/{arena,swarm}/SKILL.md`; gate2 MG2 and A4-DEF2 H02 / N-ANCHOR rulings.)*

- **Declare the run mode and the selection rule before fan-out (swarm Frame).** State whether the candidates are competing for **coverage**, **time-to-finish**, or a **mix**, what the done predicate is and how it will be judged, which artifact each candidate must return, and the object/measurement method the results will be compared on. For a race or mixed shape declare the selection rule before spawning — the source's `first pass`, `rank all` and `best-of` are examples, not the only legal rules; N is the total worker count, not the concurrency limit; each candidate writes to its own output; a measurement/verification brief names the exact SHAs and the method (sample count, what one sample is, order), and the result records both. *(Source: cursor `ecc249f1…`, `pstack/skills/swarm/SKILL.md` §Frame; A4-DEF2 H02 / N-H02-SOURCE.)*
- **Coverage and race have different meanings.** A candidate that missed a coverage slice is not "done"; the first to finish a race has not necessarily satisfied the predicate first. A result that does not record the required SHAs/method cannot support the claim it belongs to: keep the raw result and record the **gap** (a gap is not a pass). Adding the missing evidence or re-running is a choice under the existing authorization, cost and the real selection rule — the source's single re-run is an example, not a mandatory default; when the current authorization or cost only allows the existing evidence, hand in the gap rather than starting another worker, and the retry count is not coverage evidence. Coverage requires a result for every required slice, and the aggregate keeps a compact table with one-line evidenced issues and explicit gaps/dropouts rather than pasting raw worker dumps. *(Source: same, §Aggregate; gate2 A4-DEF2 H02 / N-ANCHOR / N-H02-RETRY.)*
- **Compare on the real object and conditions; keep the limits of losing or late results.** If a losing or late result would have changed the choice, preserve what it does and does not cover rather than discarding or over-trusting it. *(Source: cursor `ecc249f1…`, `pstack/skills/arena/SKILL.md`; gate2 A4-DEF2 H02.)*
- **State the rubric before the candidates.** Define what success and the real trade-offs mean for this task, turn them into gradeable criteria, and make the key constraints available to the candidates; the rubric is the picker's tool. If the experiment needs blind grading, that follows the effect-evaluation rules — keeping a success criterion secret is not a general design procedure. The prompt records the task intent; calling it a contract does not make it an accepted rule. *(Same source, Phase A.)*
- **Give the same brief and fixed inputs, and say what may vary.** Candidates work from the same accepted constraints, inputs and resources; the record states what was fixed, what was allowed to differ, and which artifact each produced. *(Same source; the same-brief boundary is the gate2 MG2 ruling.)*
- **Judge per criterion against the actual artifact, not holistically.** Record the base and enough rationale to carry the choice. A dropout or an unread candidate keeps its gap: do not claim to have beaten an object that was never read. *(Same source, Phases C–D.)*
- **Future maintainability is one legitimate concern among safety, correctness, cost and business goals** — it does not automatically override them. A smaller API or cleaner boundary can break a tie when the accepted capability is preserved; it is not a reason to drop capability. *(Same source, Phase D; the review's no-override boundary.)*
- **Graft by conditions, not by copy.** Before porting a part from a losing candidate, check whether its enabling conditions, dependencies, identity/error/state protocol can coexist with the base; keep the source and the reason for rejection; no graft without a demonstrated benefit. *(Same source, Phase E.)*
- **The synthesized object is new.** A candidate's original PASS does not transfer to the synthesis; a participant in the synthesis is one of its authors, so their own check is labeled a self-check and is not converted into independent F evidence by a different-family judge. The synthesis is verified like any other object. *(Same source, Phase F; the review's authorship boundary.)*
- **Disagreement and convergence are not automatic verdicts.** Disagreement may come from different facts, different context/risk trade-offs, a misused or under-covering rubric, or genuinely optional solutions — it is not automatically bias or underspecification, and not every disagreement requires a re-run. Convergence may be shared inertia or the same unstated assumption and does not prove correctness; check the shared load-bearing conditions, and do not average legitimate different solutions to reach agreement. Same-model and multi-model candidate sets are both not automatically independent, and a fixed candidate count, single message, cloud execution, fixed model family, judge-only rubric or one-time re-run is not a universal rule. When verification surfaces an error, fix along the actual symptom or re-frame the work — the response is not restricted to two fixed phases. *(Same source; the A4-DEF2 H02 rejected list.)*

## Recommendation

After comparing, give your own read: which option is strongest and why, in terms of the constraints and the axes above. Be opinionated rather than presenting a menu; proposing a hybrid is fine when elements genuinely combine. If only one option survives the constraints, say that too and name the constraint that settled it.

Do not require the user to confirm every technical option, and do not present the comparison as a decision that has already been accepted: the authority that owns the choice is fixed by the Charter and the accepted commitments (`technical-planning.md` §心智模型).

## Limits

- No fixed number of options, no mandatory parallel agents, no global-optimality proof, and no fixed template for the comparison.
- **No revived parallel-arena ceremony.** The deferred DESIGN-IT-TWICE parallel-agent pattern is not resurrected: no fixed criteria count, candidate count, same-message launch, forced multi-model set, default slugs, or mandatory read-only cross-judge; "the candidates agreed on the base" is not by itself confirmation, a different-family judge is not the only acceptable check, no per-loser quota of one or two points, and wild divergence does not automatically mean the brief was under-specified while convergence does not automatically ship. Loading every candidate's full text into standing context is not required, and a parent's synthesis self-check is not independent acceptance. *(Source: `arena/SKILL.md`; gate2 MG2 rejected-defaults list.)*
- No new gate, no mandatory design review, no "second opinion" step; the method runs when a real decision exists and its output can be used or discarded.
- Not the place for module-value judgments beyond the comparison above; adapter/mock choice stays in `guide-mock-adapter-choice.md`.
- Recommending does not authorize implementation, acceptance, or deletion.

## Source anchors

| Source | Retained contribution |
| --- | --- |
| Matt Pocock, `mattpocock-skills` at `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`, `skills/engineering/codebase-design/DESIGN-IT-TWICE.md` (§Process 1 Frame L9–17; §2 per-option outputs L32–38; §3 Present and compare L40–44) | Frame constraints and dependency categories; per-option interface, usage example, hidden implementation, dependency strategy/adapters, leverage trade-offs; compare by depth/locality/seam and give an opinionated recommendation or hybrid. Its deferred parallel-agent process is not revived. |
| Matt Pocock, same pin `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`, `skills/engineering/codebase-design/SKILL.md` (§Principles L60–65; §Designing for testability L67–95) | Deletion thought experiment (heuristic); interface-as-test-surface; one adapter vs two; accept dependencies, return results, small surface. |
| Matt Pocock, same pin `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`, `skills/engineering/codebase-design/DEEPENING.md` (§Dependency categories L5–25; §Seam discipline L27–31) | The dependency categories used in Frame and in per-option adapter strategy. |
| cursor-plugins `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`, `pstack/skills/arena/SKILL.md` | Candidate synthesis (arena): rubric before candidates with the same brief and fixed inputs; per-criterion judgment on actual artifacts with a recorded base/rationale; grafting by conditions with sources and rejection reasons; the synthesis is a new object verified like any other; disagreement/convergence are not verdicts; late/losing-result limits preserved. The fixed runner pool, model slugs, judge contract and phase cadence are not imported. *(Gate2 MG2 / A4-DEF2 H02 / N-H02-SOURCE.)* |
| cursor-plugins `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`, `pstack/skills/swarm/SKILL.md` | Swarm Frame/Aggregate: done predicate and returned artifact; shape (slices/race/mixed) and a pre-declared selection rule (the source's `first pass`/`rank all`/`best-of` are examples, not the only legal rules); N as total worker count; per-candidate writable output; exact SHAs and measurement method in the brief and result; a result missing the required SHA/method cannot support its claim (raw result and gap kept, gap ≠ pass); the source's single re-run is an example, not a mandatory default — extra evidence/re-run follows existing authorization/cost/selection rule or the gap is reported; per-slice coverage; compact table instead of raw dumps. The model/cloud/`run_in_background`/concurrency specifics are not imported. *(Gate2 A4-DEF2 H02 / N-ANCHOR / N-H02-RETRY.)* |

Authored additions: the deletion-test and side-effect caveats, the "fewer methods is not correctness" caution, the settled-path exclusion in Use, the synthesis rules (same brief/rubric, per-criterion judgment, new-object verification, disagreement/convergence boundaries), and the Limits (no fixed option count, no mandatory review, no revived parallel-arena ceremony).
