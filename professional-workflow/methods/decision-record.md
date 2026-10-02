# Decision record · on-demand method (MG-6)

- **Method owner:** the responsibility that owns the decision being recorded (B, C or D); recording itself creates no authority. Voice records human acceptance where that is the accepted path.
- **Status:** on-demand reference at a demonstrated gap (recording decisions and rejected concepts); a task Charter decides applicability. It is not a documentation gate and does not require a new registry or file layout.

## When to record

Offer a standalone ADR-quality record when **all three** are true:

1. **Hard to reverse** — the cost of changing your mind later is meaningful.
2. **Surprising without context** — a future reader will look at the code and wonder why it is this way.
3. **The result of a real trade-off** — genuine alternatives existed and one was chosen for specific reasons.

*(Source: matt `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`, `skills/engineering/domain-modeling/SKILL.md` §Offer ADRs sparingly L66–74.)*

Authored clarifications:

- The three conditions decide whether the decision deserves an **independent, durable record**; they do not cancel what an existing authorization, acceptance step, or audit requirement obliges you to write down. A delegated instruction can require a record of an easily reversible choice — record it, and keep the heavier form for the decisions that meet all three.
- Qualifying material includes: architectural shape; integration patterns between contexts; technology choices that carry lock-in; boundary and scope decisions (the explicit no-s as much as the yes-s); deliberate deviations from the obvious path; constraints not visible in the code; and rejected alternatives whose rejection is non-obvious. *(Source: same pin, `ADR-FORMAT.md` §What qualifies L39–47.)*

## Minimal record

- Default form: **a short title plus one to three sentences** — what the context was, what was decided, and why. An ADR can be a single paragraph. *(Source: `ADR-FORMAT.md` §Template L7–15.)*
- The point is to record *that* the decision was made and *why*, not to fill sections.
- Heavier sections (Status, Considered Options, Consequences) are optional; include them only when they add genuine value — e.g. Status when the decision will be revisited, Considered Options when the rejected alternatives are worth remembering, Consequences when downstream effects are non-obvious. *(Source: same file, §Optional sections L17–33.)*
- The record is sufficient when it conveys the condition, the reason, and the effective owner/status (accepted, proposed, superseded, deprecated). Length is not the criterion, so do not hard-cap or pad it; a longer record that carries those facts is fine.
- Placement and numbering follow the repo's existing convention if one exists (location, filename pattern, heading set). Do not introduce a second scheme; create the directory lazily when the first record is needed. *(Source: same file, §Numbering and §When to offer; `domain-modeling/SKILL.md` §File structure L40.)*

## Rejected and deferred concepts

Keep a concept-level record of rejected work so the reasoning is not lost and the same request is not re-litigated:

- One record per **concept**, not per request; group later requests under the same concept. *(Source: `skills/engineering/triage/OUT-OF-SCOPE.md` §Directory structure L17.)*
- The reason must be durable and substantive — project scope or philosophy, technical constraints, strategic choices — not temporary circumstances ("we are too busy"), which are deferrals rather than rejections. *(Source: same file, §Writing the reason L60–68.)*
- Distinguish **permanent rejection** from **resource deferral**: a deferral is not a rejection and should not be recorded as one.
- Do **not** record something that is already implemented as a rejection; point to where it lives instead. *(Source: same file, §When to write L88.)*
- When a matching request arrives, surface the prior decision to the maintainer and let them **confirm / reconsider / judge it a different concept** — never auto-reject from the record. *(Source: same file, §When to check L70–82.)*

## Examples

- A reversible decision the task explicitly asked to record: write it down in the minimal form; the three ADR conditions decide whether it deserves a standalone durable record, not whether the delegated instruction is honoured.
- A request that matches something already implemented: do not create a rejection record (that would poison later dedup checks); point to where the feature lives. *(Source: `triage/OUT-OF-SCOPE.md` L88.)*
- A rejected concept whose premises no longer hold: withdraw or update the record and let the work proceed normally; the history stays visible in the record's status/supersession, not deleted. *(Source: same file L99–105.)*

## Revisit

- When the owner reconsiders, update or withdraw the record and let the new work proceed through the normal path. *(Source: same file, §Updating or removing L99–105.)*
- Withdrawing a rejection does not erase history: previously accepted decisions and their records keep their status; a change is expressed by an explicit status/supersession relation, not by deleting the old record.
- A revisit that changes an accepted behavior or domain meaning returns to B/C; a record does not decide that on its own.

## Execution trail

Keep a reviewable trail when work is long-running, unattended, or must be trusted/resumed by a later reader — not for every task, and not for every action.

- **A row records a decision or checkpoint**, not a narration: what was chosen or done, why (plain words, not a jargon tag), an evidence pointer that resolves (commit, `file:line`, artifact path — never a paragraph), and the result/predicate state. Log the forks that shaped the work: a choice taken, a unit completed with its verification result, a pivot or revert with its trigger, a blocker surfaced, a gate fixed. Skip the trivial and self-evident. *(Source: cursor `ecc249f1…`, `pstack/skills/show-me-your-work/SKILL.md` §The format L11–32, §Logging a row L34–42.)*
- **Append-only.** A wrong call gets a new row that supersedes it; never edit or delete history. Prefer evidence produced by a repeatable script over hand-made one-offs. *(Source: same file, §Rules L50–53.)*
- **Audit the trail against this run's actual work** before handing over: every row maps to a real decision or action, and every evidence pointer resolves and shows what the row claims. A fork, pivot or abandoned approach that shaped the work but is missing is a gap — add it. Correct by superseding, not by rewriting. Read only this run's own record/artifacts; do not sweep unrelated private transcripts or other runs' history. *(Source: same file, §Audit the log against the transcript L55–63.)*
- **Placement and substrate follow the project's convention.** This package does not mandate a file, a TSV, a column set, or a per-iteration entry: the trail is a working artifact unless a reviewer needs it, and it may be the record the project already keeps. *(Source: same file, §Where it lives L44–48; the review's "no per-iteration commit/TSV" boundary.)*

Boundaries that keep the trail a record rather than an authority:

- The trail records; it does not accept a decision, close a task, define an exit condition, or replace an independent evaluation. "The work stream owns its exit condition", "any side bug may be fixed", and "a plateau never stops" are **not** general permissions: conditions come from the delegation and stay bounded by its budget, stop and risk rules; a done marker only proves the marker exists. *(Boundary from the review of the source's autonomous-run framing.)*
- A **self-check is labelled as a self-check**; auditing the trail does not turn an author's self-report into independent evidence, and a needed independent evaluation cannot be substituted by a trail audit.
- Revert or discard only your own authorized changes, and keep a rollback object; do not delete another author's work.
- No mandatory different-model review of the trail and no fixed output format (for example an "Attention" section); decide with the task's own Charter whether a second reviewer is needed.
- Generalizable lessons are a **different mechanism** (lesson promotion/encode-lessons); this trail records what happened in this run. Decisions already recorded elsewhere are referenced by pointer, not restated, so the trail does not become a second source of truth.

## Limits

- Recording creates no C/D/B authority, no implementation or delete permission, and no acceptance.
- Not every decision needs a record; no mandatory file, template repository, sequential numbering, or registry is required.
- This method does not replace the acceptance/verification/action/closure separation: a recorded decision is not an accepted one, and an accepted one is not an authorized action.
- The execution trail is subject to the same limit: it is not an authority, an exit condition, or a substitute for independent evaluation (see §Execution trail).

## Source anchors

| Source | Retained contribution |
| --- | --- |
| Matt Pocock, `mattpocock-skills` at `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`, `skills/engineering/domain-modeling/SKILL.md` (§Offer ADRs sparingly L66–74; §File structure L40) | The three conditions; skip the ADR when one is missing; lazy creation of the decision directory. |
| Same pin, `skills/engineering/domain-modeling/ADR-FORMAT.md` (§Template L7–15; §Optional sections L17–23; §When to offer L29–37; §What qualifies L39–47) | Title plus one-to-three sentences as the default; optional heavier sections; qualifying decision types; the three conditions. |
| Same pin, `skills/engineering/triage/OUT-OF-SCOPE.md` (§Writing the reason L60–68; §When to check L70–82; §When to write L84–88; §Updating or removing L99–105) | Concept-level rejection records; durable reasons vs deferrals; the confirm/reconsider/disagree three-way; not recording already-implemented work; withdrawal semantics. |
| cursor-plugins `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`, `pstack/skills/show-me-your-work/SKILL.md` (§The format L11–32; §Logging a row L34–42; §Where it lives L44–48; §Rules L50–53; §Audit L55–63) | The decision row (decision / why / evidence pointer / result), what to log and what to skip, append-only supersession, and the run-scoped audit against real actions and artifacts. |
| cursor-plugins `ecc249f1…`, `pstack/skills/poteto-mode/playbooks/autonomous-run.md` (L1–12) | Keeping the acceptance predicate fixed and reporting the final predicate state honestly — read for the trail/checkpoint discipline only; its exit-condition ownership and side-fix permissions are not imported. |

Authored additions: the delegated-instruction exception for reversible decisions, the permanent-rejection vs resource-deferral distinction, the history-preservation and status/supersession rule, and the Limits.
