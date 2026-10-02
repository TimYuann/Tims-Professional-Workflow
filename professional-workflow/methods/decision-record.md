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
- **Common "expensive to change later" situations** worth recording: a framework/library or major dependency choice; a data model or schema; an authentication/authorization strategy; an API architecture; a build/hosting/infrastructure choice; or any decision where reversal would be costly. These are examples that make the three conditions concrete, not a separate mandatory checklist. *(Source: addy `2686b620…`, `skills/documentation-and-adrs/SKILL.md` §When to Use — its example list, compressed; its SQLite-specific dismissal is not imported.)*
- **A proposal, candidate, or deprecated item is not recorded as accepted.** The record's status must state what it actually is (proposed/candidate/deprecated/superseded); do not write `Accepted` for something that has not been accepted by its owner. *(Source: same file, lifecycle; the status-honesty boundary is the C2 gate ruling.)*

## Minimal record

- Default form: **a short title plus one to three sentences** — what the context was, what was decided, and why. An ADR can be a single paragraph. *(Source: `ADR-FORMAT.md` §Template L7–15.)*
- The point is to record *that* the decision was made and *why*, not to fill sections.
- **When the fuller form is used, it must be able to answer four questions:** the context at the time (constraints, data shape, external limits); the decision itself in one quotable sentence; **the alternatives considered and why each was rejected**; and the consequences (what this now enables, what it requires, what a later change would disturb). The rejected-alternatives question is the record's core value — a record with only the conclusion records nothing worth keeping. These are judgment questions, not a required section layout or Markdown template. *(Source: addy `2686b620…`, `skills/documentation-and-adrs/SKILL.md` §Architecture Decision Records; retained compressed, without its template.)*
- Heavier sections (Status, Considered Options, Consequences) are optional; include them only when they add genuine value — e.g. Status when the decision will be revisited, Considered Options when the rejected alternatives are worth remembering, Consequences when downstream effects are non-obvious. *(Source: same file, §Optional sections L17–33.)*
- The record is sufficient when it conveys the condition, the reason, and the effective owner/status (accepted, proposed, superseded, deprecated). Length is not the criterion, so do not hard-cap or pad it; a longer record that carries those facts is fine.
- Placement and numbering follow the repo's existing convention if one exists (location, filename pattern, heading set, numbering sequence, markdown flavour). **Match the existing convention before considering this method's defaults**, and do not restart numbering or introduce a second parallel scheme. If the existing evidence conflicts (two conventions, an ambiguous directory), **surface the conflict** and have its owner resolve it rather than silently adding a third scheme. Only when no convention can be established does a plain default (a decisions directory with sequential numbering) apply. *(Source: same file, §Match the existing convention first; `domain-modeling/SKILL.md` §File structure L40; the conflict-exposure rule is the C2 gate ruling.)*

## Lifecycle

- The status path is `proposed → accepted → (superseded | deprecated)`; the statuses used must be the ones the project already defines if it defines them. *(Source: addy `2686b620…`, `skills/documentation-and-adrs/SKILL.md` §Lifecycle.)*
- **Do not delete an old record; supersede it.** When a decision changes, write the new record and reference the one it replaces. The old record keeps the context of why the earlier choice was made; deleting it means the next reader re-proposes it. *(Source: same file; `triage/OUT-OF-SCOPE.md` L99–105 for the concept-level record.)*
- **The record carries the why and the rejected alternatives; the rule's own text remains the single source for the rule.** A record that restates the rule as a second definition is drift, not documentation. *(Source: same section; consistent with `authority/README.md`'s source-then-regenerate discipline.)*

## Around the decision

- **Comments state why, not what.** A comment that restates the code becomes false as soon as the code changes; a comment explaining a non-obvious reason (why the window resets at the boundary, why this order is required) stays true. Do not leave commented-out code (version history has it) and do not park do-it-now work as a TODO. *(Source: addy `2686b620…`, `skills/documentation-and-adrs/SKILL.md` §Inline Documentation.)*
- **Record known operational traps in place, pointing at the decision.** A pitfall the next reader will hit ("must run before first render, see ADR-003") belongs where the code is touched, with a pointer to the record that explains the commitment. *(Source: same section.)*
- **Documentation describes the current state, not the change history.** A rule/standard/README states what is true now in timeless terms; the history of how it got there belongs in the decision records, not in the rule text. *(Source: same file; `references/definition-of-done.md` §Documentation.)*

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
- **Export sinks: encode for the reader that will interpret the record.** When a trail is exported as TSV/CSV (or otherwise opened by a reader that interprets formulas or markup), handle that reader's real semantics: cells beginning with `=`, `+`, `-`, `@`, or carrying control/leading characters can be interpreted rather than displayed, so neutralize them for the destination reader (for example a leading quote) while keeping the original evidence recoverable in its source form. Quoting alone covers only the input shape the exporter was written for and does not certify every spreadsheet or reader as safe. *(Source: cursor `ecc249f1…`, `pstack/skills/show-me-your-work/scripts/log.sh` — formula-injection guard and `>>` write; gate2 MG5 ruling.)*
- **Append semantics are not concurrency semantics.** `>>` avoids truncating or replacing an existing file (useful where a network mount makes an `-s` test fail), but it does not prove that concurrent writers are atomic or that the whole filesystem view is consistent. Concurrent writers coordinate through the existing bounded-composition/shared-write rules; this trail adds no lock and claims none. The source's exact TSV header, shell script and UTC timestamp format are examples, not a required substrate. *(Same source; gate2 MG5 ruling.)*
- **Completion is a scoped triage event, not inherent success.** A finished unit is triaged against the scope it was asked to cover; completion does not by itself authorize interrupting a critical mutation, and a critical section keeps its integrity according to the real dependency and invariant. No fixed drain points or batch mandate applies. *(Source: cursor `ecc249f1…`, `pstack/skills/poteto-mode/playbooks/orchestrate.md`; gate2 MG4 ruling.)*
- **Preserve arrived, failed, unaccounted and abandoned work with their scope.** A later run must not silently erase contributions or gaps: reallocating a scope is explicit, and the record shows what reached its result, what failed, what is unaccounted for and what was abandoned. *(Same source; gate2 MG4 ruling.)*
- **No store or format registry.** No JSON+TSV store, registry, fixed counts or one-coordinator-per-plan is required; the trail remains the existing project record with its owner. *(Same source; the MG4 rejected-defaults list.)*
- **A hook marker, completion promise or state file is a message pattern, not a predicate or permission.** Its presence or exact match does not prove completion, grant a go, or authorize a continuation; a marker only triggers a re-read, and a damaged state file keeps its evidence rather than being auto-cleaned. *(Source: cursor `ecc249f1…`, `ralph-loop/hooks/{capture-response,stop-hook}.sh`; gate2 G07.)*

Boundaries that keep the trail a record rather than an authority:

- The trail records; it does not accept a decision, close a task, define an exit condition, or replace an independent evaluation. "The work stream owns its exit condition", "any side bug may be fixed", and "a plateau never stops" are **not** general permissions: conditions come from the delegation and stay bounded by its budget, stop and risk rules; a done marker only proves the marker exists. *(Boundary from the review of the source's autonomous-run framing.)*
- A **self-check is labelled as a self-check**; auditing the trail does not turn an author's self-report into independent evidence, and a needed independent evaluation cannot be substituted by a trail audit.
- Revert or discard only your own authorized changes, and keep a rollback object; do not delete another author's work.
- No mandatory different-model review of the trail and no fixed output format (for example an "Attention" section); decide with the task's own Charter whether a second reviewer is needed.
- Generalizable lessons are a **different mechanism** (lesson promotion/encode-lessons); this trail records what happened in this run. Decisions already recorded elsewhere are referenced by pointer, not restated, so the trail does not become a second source of truth.

## Limits

- Recording creates no C/D/B authority, no implementation or delete permission, and no acceptance.
- Not every decision needs a record; no mandatory file, template repository, sequential numbering, or registry is required. The four questions above are a quality test for the records that are written, not a mandate to write every decision up in full, and this method does not turn Matt's title-plus-one-to-three-sentences default into a mandatory long template. *(The C2 gate ruling.)*
- This method does not replace the acceptance/verification/action/closure separation: a recorded decision is not an accepted one, and an accepted one is not an authorized action.
- The execution trail is subject to the same limit: it is not an authority, an exit condition, or a substitute for independent evaluation (see §Execution trail).

## Source anchors

| Source | Retained contribution |
| --- | --- |
| Matt Pocock, `mattpocock-skills` at `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`, `skills/engineering/domain-modeling/SKILL.md` (§Offer ADRs sparingly L66–74; §File structure L40) | The three conditions; skip the ADR when one is missing; lazy creation of the decision directory. |
| Same pin, `skills/engineering/domain-modeling/ADR-FORMAT.md` (§Template L7–15; §Optional sections L17–23; §When to offer L29–37; §What qualifies L39–47) | Title plus one-to-three sentences as the default; optional heavier sections; qualifying decision types; the three conditions. |
| Same pin, `skills/engineering/triage/OUT-OF-SCOPE.md` (§Writing the reason L60–68; §When to check L70–82; §When to write L84–88; §Updating or removing L99–105) | Concept-level rejection records; durable reasons vs deferrals; the confirm/reconsider/disagree three-way; not recording already-implemented work; withdrawal semantics. |
| cursor-plugins `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`, `pstack/skills/show-me-your-work/SKILL.md` (§The format L11–32; §Logging a row L34–42; §Where it lives L44–48; §Rules L50–53; §Audit L55–63) | The decision row (decision / why / evidence pointer / result), what to log and what to skip, append-only supersession, and the run-scoped audit against real actions and artifacts. |
| cursor-plugins `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`, `pstack/skills/show-me-your-work/scripts/log.sh` | Export sink fidelity: neutralise formula-leading cells (`= + - @`) and control/leading characters for the reader that will open the record, keeping the source evidence recoverable; `>>` avoids truncation but is not a concurrency guarantee. The exact TSV header, script and UTC format are not imported. *(Gate2 MG5.)* |
| cursor-plugins `ecc249f1…`, `pstack/skills/poteto-mode/playbooks/orchestrate.md` | Scoped completion triage (completion is not inherent success and does not authorize interrupting a critical mutation, which keeps its integrity per dependency/invariant); arrived/failed/unaccounted/abandoned work preserved with its scope. No store/registry/JSON+TSV/fixed counts/one-coordinator-per-plan. *(Gate2 MG4.)* |
| addy `2686b620fc1fed2e8f60c704839c766b8594c6b6`, `skills/documentation-and-adrs/SKILL.md` (§Overview; §When to Use; §Architecture Decision Records incl. Match the existing convention first, template and lifecycle; §Inline Documentation; §Verification) and `references/definition-of-done.md` §Documentation | The expensive-to-change examples; the four questions (context/decision/rejected alternatives/consequences); match the existing convention before defaults with conflicts surfaced; proposed → accepted → superseded/deprecated with supersede-not-delete; comments only why, no commented-out code, no do-now TODOs; operational traps documented in place with a pointer; documentation describes the current state, not the change history. Its README/OpenAPI/changelog samples and SQLite dismissal are not imported. |
| cursor-plugins `ecc249f1…`, `pstack/skills/poteto-mode/playbooks/autonomous-run.md` (L1–12) | Keeping the acceptance predicate fixed and reporting the final predicate state honestly — read for the trail/checkpoint discipline only; its exit-condition ownership and side-fix permissions are not imported. |

Authored additions: the delegated-instruction exception for reversible decisions, the permanent-rejection vs resource-deferral distinction, the history-preservation and status/supersession rule, and the Limits.
