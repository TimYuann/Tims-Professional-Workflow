# Uncertainty planning · on-demand method (DEF-4)

- **Method owner:** A/Voice owns the destination and scope; D owns dependency ordering; the owner of a resolved question carries its answer into its own record. Planning a question never transfers the authority to decide or execute it.
- **Status:** on-demand reference at a demonstrated gap (a goal too large for one working session whose route is not yet visible); a task Charter decides applicability. It is a planning aid, not a tracker, not a ticket system, and not an execution authorization.

## Use

Use when the destination is clear enough to name but the way to it is wrapped in fog: the goal is bigger than one session can hold, and the next steps cannot simply be listed. The method separates what can already be asked from what cannot yet be phrased, works the answerable questions, and stops when the way is clear. Skip it when the route is already visible or the goal fits one session — an ordinary plan covers that case and a map adds ceremony.

## Destination

- **Name the destination first.** What reaching the end looks like — a spec to hand off, a decision to lock, a change made in place. It fixes scope: every later question is judged by whether it moves toward it, and work beyond it is not fog. *(Source: matt `c55ee460…`, `skills/engineering/wayfinder/SKILL.md` L7–9, L32–34, L97.)*
- **The destination is a scoping act, not a plan.** Naming it does not authorize the work to reach it; it bounds what this planning effort is about. *(Authored boundary.)*

## Known questions and unknowns

- **A question that can be stated precisely now is a question**, even if it is blocked and cannot be worked yet: record it with what it waits on, and it becomes available when its blocker resolves. *(Source: same file, §Fog of war L88–91.)*
- **What cannot yet be stated precisely is in-scope uncertainty.** Record it loosely, in the destination's direction, without pre-slicing it into question-sized pieces: one patch may graduate into several questions, or none, once the frontier reaches it. *(Same source, §Fog of war L82–93.)*
- **Out-of-goal work is recorded separately.** Work past the destination is out of scope, not fog: it never graduates, and returning to it means redrawing the destination as a new effort rather than quietly resuming a parked item. *(Same source, §Out of scope L95–101.)*
- The discriminator is *can this be stated precisely*, not *can this be answered*: do not promote fog to a question because it feels important, and do not park a precisely statable question because it is blocked.

## Dependencies and update

- **Satisfy dependencies before expanding.** A question whose blocker is unresolved stays on hold; resolving the blocker is what makes the rest of the route statable. Recorded dependencies are relationships between questions, not a schedule: the useful output of a resolution is the answer plus what newly became precise. *(Source: same file, L69, L125–126.)*
- **Keep results where they belong.** The answer to each question lives in its own owner record (the decision record, spec, issue, or task); the planning view stays an index that points at them. A plan that restates the answers creates a second source of truth that drifts. *(Source: same file, §The Map L21–23.)*
- **Update on every resolution:** record the answer where it belongs, close the question, append the new pointer, graduate the fog that became statable, and delete or redirect entries the answer invalidated. An index that stops tracking reality is worse than none. *(Source: same file, §Work through the map L125–126.)*
- **One question at a time** (beyond work already authorized in parallel): each resolution changes which next question is even askable. *(Same source, L105, L122–126.)*
- **A claim or an assignment is a coordination marker, not a lock.** Marking a question claimed is not permission to work it; an editable planning note is a note, not execution authority. The accepted delegation remains the source of authority for any action. *(Authored boundary; the source's tracker assignment is a collision-avoidance convention.)*

## Handoff

- **When the way is clear, hand off.** The planning ends when no question remains before someone can go and do the thing: hand over what was decided (pointing at where each answer lives), what remains, and the next concrete action. *(Source: same file, §Plan, don't do L11–13.)*
- **A decision is not the deliverable.** This method produces the route, not the destination artifact; the actual spec/decision/change is produced by the ordinary work that follows, with its own authority. *(Source: same file, §Plan, don't do L11–13.)*
- **If the goal turns out to be larger or different, return to the actual authority.** Do not silently widen the destination, keep planning an unbounded goal, or treat the existing notes as authorization for a new one. *(Authored boundary.)*

## Limits

- **Not a tracker.** The method does not record task status, own work items, replace the decision record, or require an external issue tracker; it is a planning view over questions.
- **No fixed budgets or rhythms.** No required session/context size per question, no mandatory per-person or per-agent review, no requirement that every question be assigned, no one-map-per-goal ceremony, and no mandatory sweep to collect all uncertainty before starting. The method scales to the goal; a small goal may need no written view at all.
- **Planning grants nothing.** Naming a destination, recording a question or claiming it does not authorize code changes, spending budget, or bypassing a needed approval; tool and action limits stay with the task.
- No fixed vocabulary beyond owner records and pointers is required; a compact in-task note is a valid form.

## Source anchors

| Source | Retained contribution |
| --- | --- |
| matt `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`, `skills/engineering/wayfinder/SKILL.md` (L7–13; §The Map L19–53; §Tickets L55–71; §Fog of war L82–93; §Out of scope L95–101; §Invocation L103–128) | Destination named first; the view as an index pointing at where each answer lives; question = statable-now vs in-scope fog; out-of-goal work listed separately and never graduating; resolve one at a time and update the view; planning hands off to execution. The tracker schema, ticket types, labels, claim mechanism, and map body format are not imported. |

Authored additions: the destination-is-scoping-not-authorization rule, the claim-is-not-a-lock/notes-are-not-permission boundary, the return-to-authority rule when the goal changes, and the Limits.
