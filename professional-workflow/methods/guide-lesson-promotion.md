# Lesson promotion · on-demand guide (MG-3)

Status: on-demand guide at a demonstrated gap; creates no authority, platform, or gate. Source anchors and authored additions are marked. This guide is the shared carrier for the repeating-correction mechanism (with the preference-extraction and mechanical-vs-judgement work from the other source families); it does not create a second one.

## Use

On demand, when the same instruction is being written a second time, when a correction repeats, or when a working preference looks durable enough to outlive the task. It turns a repeating signal into the right carrier — or explicitly decides not to. It is not a session-retro ritual and not a mandate to encode everything.

## Scope and evidence

- **Read only what you are authorized to read.** Pin the window (make "recent" a real range), the topic if named, and the workspace (the active one by default; never read another project's records unless asked). State the scope back. Sanitize before anything leaves the context. *(Source: cursor `ecc249f1…`, `cursor-team-kit/skills/workflow-from-chats/SKILL.md` §Scope L10–15; `pstack/skills/recall/SKILL.md` L18.)*
- **Classify the evidence before extracting anything:** explicit corrections and stated preferences; accepted workflows; repeated patterns across records; conflicts between records. *(Source: `workflow-from-chats/SKILL.md` §Workflow L16–26.)*
- **Label confidence, and do not mistake it for authority.** Strong: an explicit user preference, a correction that changed the workflow, a repeated parent-record pattern, or a direct request to encode the behavior. Medium: an accepted workflow, a repeated tool/verification preference, a consistent subagent finding that the parent then used successfully. Weak: agent-chosen behavior with no user feedback, a single ambiguous record, a possibly task-specific correction. Contradicted: the evidence conflicts — ask before writing. *(Source: same file, §Confidence L27–32.)* Authored boundary: none of these levels grants acceptance or the right to change organization-level behavior; "an agent did it and it was used" is not automatically a human preference.
- **Separate the signal from the noise.** Extract the trigger, the decision rule, the quality bar, the stop condition and the evidence — not a transcript summary. Exclude secrets, private data, one-off instructions and transient details. *(Source: same file, §Workflow L16–26; cursor `ecc249f1…`, `continual-learning/agents/agents-memory-updater.md` guardrails.)*

## One-off or pattern

- A **one-off correction** — the situation was specific, the response was situational, no rule is implied — is recorded (or simply corrected) and not promoted. Do not turn a single correction into a principle.
- A **pattern** — the second occurrence of the same instruction, or a recurring failure/correction — is a candidate for promotion. *(Source: cursor `ecc249f1…`, `pstack/skills/principle-encode-lessons-in-structure/SKILL.md` L13–27.)*
- Genuinely system-level issues can deserve a principle/method-level carrier rather than a local rule; keep that judgment separate from the local fix. *(Source: same file, §Feedback loop L23–26.)*
- Anti-patterns to avoid: acknowledging without recording ("I'll keep that in mind" does not persist); recording without routing (a note that never reaches a carrier); fixing one instance while leaving the pattern intact. *(Source: same file, L28–31.)*

## Classify the violation

Before writing a rule, classify what went wrong — the carrier follows from the class. *(Source: matt `c55ee460…`, `skills/in-progress/retro/SKILL.md` §Steps L18–22, §Implementation vs Review L29–36.)*

- **Look for the existing executable carrier first.** Read the repo's own check command (its `lint`/`check`/test scripts, its CI workflow) and its existing config before proposing anything: a check that already exists but is unwired or silently broken is the finding, and wiring it is the fix — not a new tool. *(Same source, §Steps L18.)*
- **A mechanical violation** — a fixed syntactic pattern, a banned API, an import shape, a file-location rule, a boundary that can be expressed as a path/matcher — is a candidate for the cheapest deterministic check the repo's language and toolchain actually support (its own linter, a pre-commit hook, a CI job). Prefer the check over a new prose rule when the check is feasible within the task's reliability level and cost. *(Same source, §Steps L19.)* Authored boundary: "mechanical" makes a check *feasible*, not mandatory — building one needs its own authorization and must cost less than the risk it covers, so a mechanical issue may still be carried by text when the check is expensive, brittle, or outside the delegated scope. *(Source: same file; the review's cost/authority boundary.)*
- **A judgement call** — cross-file consistency, "matches the surrounding style", anything no guardrail could substitute for — is carried by prose (an existing standards document or review instruction), not by a fabricated check. Never dress a judgment call as a lint rule just to make the lesson feel enforced. *(Same source, §Steps L19.)*

## Choose carrier

When a pattern qualifies, choose the **strongest mechanism the situation allows within the task's accepted reliability level**: an unrepresentable state that cannot compile > a lint rule or banned API that fails CI > a canonical helper/entry point > a runtime check > a more prominent instruction with a failure-mode example. *(Source: `encode-lessons-in-structure/SKILL.md` L13–19.)*

- Choose by detectability, false-positive rate, maintenance cost and the task's reliability requirement — not by a fixed ranking applied blindly.
- **When the rule needs judgment, the legitimate branch is the text carrier**: make the instruction more prominent and add an example of the failure mode. Not everything can or should become a check. *(Source: same file, L17.)*
- Prefer **existing carriers** — a Profile paragraph, a Charter field, a method section, an existing config convention. Do not create a tool, registry, tracker, or new platform for a lesson; the mechanism strength is bounded by what the task actually accepted. *(Source: the review's MG-3 boundary; the execution plan's no-registry rule.)*
- A tool that performs or proves one-off work for the task in front of you is a different mechanism (`build-the-lever`); this guide is for a repeating rule that should outlive the task.
- Carrier *expression* — how the text reads, what it points at, what to leave out — is the agent-text guide's job (when that guide is bound). This guide decides *whether and where* the lesson is promoted.
- If the carrier is a memory/standing-context file, keep it minimal and truthful: update an existing matching entry in place, add only net-new entries, keep entries plain, and do not write procedure/rationale/metadata into it. *(Source: `continual-learning/agents/agents-memory-updater.md`; `guide-agent-text.md` for expression when present.)*

## Accept and apply

- **Do not auto-apply durable changes.** A change that affects future work (a rule, a Profile/method edit, an organization-level behavior) needs the acceptance its scope requires; where the change is already inside an explicit, valid authorization, apply it and record it — do not rebuild a full approval ceremony for an edit that is already authorized. *(Source: cursor `ecc249f1…`, `pstack/skills/reflect/SKILL.md` §4–5 L47–65.)*
- **Close the loop:** apply now or create a concrete todo; a recorded lesson that changes nothing is the anti-pattern. *(Source: `encode-lessons-in-structure/SKILL.md` L26.)*
- **Record the accepted change and the rejected/deferred ones** per `decision-record.md` (its §Execution trail records what happened in the run; the decision record carries the accepted rule and its status). A rejection on record is just as useful: it prevents the same request from being re-litigated.
- **When citing a principle or method name, name the decision it changed.** A citation with no decision behind it is a name-drop, not an application. *(Source: cursor `ecc249f1…`, `pstack/docs/guide/08-principles.md`.)*
- Contradictory evidence goes to the actual owner of the rule; unresolved conflicts are not silently filed as a preference.

## Limits

- No "second time, therefore must encode": the second occurrence makes it a candidate, not an obligation.
- No "mechanical violation therefore a check must be built": the classification selects the cheapest *adequate* carrier, and a check that is expensive, brittle, or outside the delegated scope can be declined in favour of a text rule. No rule that a repo without CI is automatically defective in this package, and no assumption that every standard can be compiled or that a reviewer role automatically owns all standards.
- No fixed mechanism-strength ranking, no requirement that an encoded lesson delete every explanation, and no requirement that every lesson become a check.
- No automatic backlog/public-tracker entry, no new registry or configuration platform, no host/read-only/MCP assumption; if the records needed are not accessible, say so and stop rather than inventing evidence.
- Confidence labels (strong/medium/weak/contradicted) do not grant acceptance, and repetition by an agent does not convert a behavior into a human preference.
- This guide does not duplicate the execution trail (`decision-record.md` §Execution trail), the professional explanation guide, or the memory-file hygiene rules; those are separate carriers for separate objects.

## Source anchors

| Source | Pin / path | Section |
| --- | --- | --- |
| cursor-plugins | `ecc249f1…`, `pstack/skills/principle-encode-lessons-in-structure/SKILL.md` | Pattern L13–19; strongest-mechanism L19; corollary L21; feedback loop L23–26; anti-patterns L28–31 |
| cursor-plugins | `ecc249f1…`, `pstack/skills/reflect/SKILL.md` | §Locate L17–27; §Synthesize L43–45; §Structural enforcement L47–49; §Apply L51–64 |
| cursor-plugins | `ecc249f1…`, `cursor-team-kit/skills/workflow-from-chats/SKILL.md` | §Scope L10–15; §Workflow L16–26; §Confidence L27–32; §Artifact Choice L34–39 |
| cursor-plugins | `ecc249f1…`, `pstack/docs/guide/08-principles.md` | Principle names as interfaces; the citation-without-a-decision tell |
| cursor-plugins | `ecc249f1…`, `continual-learning/agents/agents-memory-updater.md` | In-place bullet update, net-new only, no metadata, exclude secrets/private/one-off/transient |
| mattpocock-skills / addy (dedupe) | `c55ee460…`, `skills/in-progress/retro/SKILL.md` (§Steps L18–22; §Implementation vs Review L29–36) and `.changeset/retro-deterministic-checks.md`; `2686b620…`, `evals/README.md` and `evals/skill-impact.md` | The mechanical-vs-judgement classifier (mechanical violation → cheapest deterministic check; judgement → prose), the "existing check unwired/broken is the finding" rule, and the method-evaluation discipline share this promotion mechanism; the review merges them here rather than creating parallel carriers. The no-CI-universal and mechanical-must-build-check boundaries are authored. |

Authored additions: the confidence-is-not-authority boundary, the existing-authorization apply rule, the decision-record/agent-text division of labor, the memory-file carrier note, and the Limits.
