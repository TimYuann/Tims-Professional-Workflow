# Quality policy and its enforcement · candidate method body

- **Status:** candidate distilled under `docs/absorption/2026-10-02/reviews/ORACLE-REVIEW-A1-ADDY-CD.md` (C5, 2026-10-02, source `addy@2686b620`), merged with the G5 adjudication in `docs/absorption/2026-10-02/reviews/REVIEW-A1-ADDY-AB.md`; not yet an accepted reference; creates no authority, trigger, or gate. A fixed-diff review still applies.
- **Method owner when bound:** the policy's valid owner (a project authority, not this method) decides the bar and its revisions; B/C keep the accepted commitments it protects; E applies it to the change; F checks the claimed evidence.

## Use

Use when a project's quality bar must be written down, when an existing policy must be applied to a task, or when a change may be quietly lowering the bar. This is an on-demand method, not a stage every task must pass through. It creates no library-wide mandatory baseline and does not make anyone the owner of a policy they do not own.

## Standing policy versus task acceptance criteria

These answer different questions and are not substitutes:

| | Acceptance criteria | Standing quality policy |
| --- | --- | --- |
| Scope | one task or spec | every increment under that policy |
| Changes | per item | fixed and reused |
| Answers | "did we build *this thing*?" | "is it *ready* to our standard?" |
| Owner | set when the task is planned | set once by the policy's valid owner |

A task is finished only when its own acceptance criteria and the applicable standing policy are both satisfied. A single green test is not closure: closure comes from the valid closure rule, not from this checklist. Conversely, a checklist cannot create closure where the accepted criteria are unmet.

Applying a policy means covering the concerns the change actually touches — correctness, quality, integration, documentation, recovery — in proportion to the change, not running every row uniformly. A typing or documentation change produces its evidence per its claim; there is no universal obligation that every task run at runtime, be test-first, require human review, or be deploy-ready. Those are decisions for the policy's owner, not consequences of this method.

## Applying an existing policy

- **Detect before asking.** Read the project's actual rules, tools and current values before proposing anything. `CONSTRAINTS.md`, existing lint/test config, CI configuration and current coverage output are evidence; asking for what can be read wastes the owner's time.
- **Cite, don't renegotiate.** Apply the policy as written. A task does not acquire the freedom to relax a standing rule because the rule is inconvenient for this change.
- **State the metric and the reason together.** A threshold without a rationale gets deleted by the next person who hits it. A number with no observation command behind it is an aspiration, not a constraint.
- **Separate enforced from measured-only.** "Measured, not yet enforced" is a legitimate state: record today's value and the direction it must not move.
- **Policies can be revised.** They are not never-renotiable or monotonic. A revision is a policy change by its owner, not a silent edit inside a feature diff.

## Writing a threshold line

Every line that claims to constrain a change must be able to answer four questions:

1. **What is the rule?**
2. **What decides it?** — the command, tool, or observation that produces the verdict.
3. **Where does it run?** — edit loop, task end, review, CI.
4. **Who may break it, under what condition, until when?**

A line with a number and no deciding command is a wish. An exception without an owner or an expiry is a permanent exemption; exceptions carry a reason, an owner and an end date.

## Placement by cost, not by enthusiasm

The biggest failure is running everything everywhere. A check that stalls the change loop gets switched off, and **a gate people switched off is worse than no gate at all** — the bar still looks like it exists.

- seconds → edit loop
- tens of seconds → when the task believes it is done
- minutes → review
- directional/regression checks → the final gate

Two rules keep the placement tolerable: **scope expensive checks to the changed surface** (the coverage of the changed lines is something the change's author can move; the whole-repo number is inherited), and **reuse output that already exists** rather than running a suite twice to produce the same number.

## Guarding the bar itself

When the same agent writes the implementation and the checks, the checks prove less than they look like they prove. The realistic failure is not a clever loophole: a red check appears and the cheapest road to green is taken. Watch for five moves in the diff at review time:

1. **The threshold moved.** A budget lowered, a severity downgraded, a check removed from the fast stage, a rule deleted from the policy file.
2. **A test got easier.** A skip added, a test file deleted, assertions removed from a test that remains.
3. **A checker got silenced.** New suppression comments. Four deserve particular attention because they disable a check the change depends on: dropping code from coverage, hiding a surviving mutation, and suppressing a security finding (two of the four are the same class in different tools).
4. **Work is unfinished.** A stub that throws, an empty catch turning a failure into silence, a placeholder standing where the implementation belongs.
5. **An exception appeared.** A new exception row nobody discussed, with no owner or expiry.

**Tightening the bar should be silent; loosening it should be loud.** Comparing the policy file against its state at the branch point is normally enough; a dedicated runner is one option, not a requirement.

## Where the check's evidence comes from

Rank checks by one question: *can the change make this pass by writing code that does not work?*

- **External** — encodes an outside standard or database (a browser-based accessibility/market check, a vulnerability/advisory database). The change cannot argue with it.
- **Project** — the project's own rules and boundaries. A human owns the configuration.
- **Own suite** — the project's tests. The most useful, and the only genuinely circular one.

A bar made entirely of the third kind is weaker than one with an outside opinion in it. At least one external constraint is the source's target, not a fixed quota; and an external tool's result is not automatically correct — it can have no coverage of the change, be misconfigured, run the wrong version, or be falsely green. Treat its result as evidence to read, not as an unquestionable verdict.

## Ratchets (an optional accepted policy)

When no one has a number, record where the project is today and refuse to get worse. The comparison is against the **recorded value**, not an aspiration: improvement updates the record; a drop is a finding.

A ratchet is an optional policy a project may accept — not a library rule. A real professional objective may legitimately accept a metric change (for example, a bundle grows for a feature that pays for it), decided by the policy's owner. What is not allowed is relaxing the rule because the current value changed.

## Mechanical guards: clues, not judges

If a project uses a diff-scoped guard for the five moves above, it should follow the source's contract: exit `0` clean, `1` at least one violation, `2` the guard could not run — and **a `2` must never read as a `0`**. A check that could not execute is not a clean check. The guard reports the rule and the location, never the matched value; redaction is a hard requirement for anything that may match a secret.

Two boundaries keep the guard honest:

- **A pattern match is a clue, not a semantic verdict.** Legal deletion or replacement of a test, a reasonable suppression, an unfinished stub in an independent candidate, or a legitimate rename can all trip a regex. A mechanical hit starts an inspection; it does not establish a violation.
- **Do not port the source's floor-guard script into this library as a product tool.** The five-move review and the `0/1/2` distinction can be absorbed. A mechanical runner is selected later only when real usage demands one, through the project's existing admission, not to fill a template.

## Limits

- No hard gate, validator, or standing obligation is created here. The source's numbers and heuristics — 80% changed-line coverage, 90-day exception lifetime, 0.5% ratchet tolerance, a ~90-second task budget, "more than ~30 lines of guarding shell means escalate", an external checker per project, two-week enforcement — are source examples and defaults. Adopting one requires the project's actual value and its policy owner.
- There is no universal duty list: runtime verification, test-first development, human review and deploy-readiness are policy choices the project's owner may or may not require for a given class of change.
- Enforcement level is a project choice: written-only, scripted via the project's own command, or a dedicated runner. Most projects should stop at the simplest level that works; the escalation threshold is a heuristic, not a rule.
- This method does not grant release permission, does not close a task, and does not change anyone's ownership of the quality policy.

## Source anchors

| Source | Retained contribution |
| --- | --- |
| Addy Osmani, `addyosmani-agent-skills` at `2686b620fc1fed2e8f60c704839c766b8594c6b6`, `skills/constraint-driven-development/SKILL.md` (`The Process` steps 1–7, `Sane Defaults`, `Escalation Path`, `Red Flags`) | Detect before asking; metric + reason; enforced vs measured-only; the four questions a threshold line must answer; placement by cost and diff-scoping; exception owner/expiry; the five loosening moves; tightening silent / loosening loud; the external / project / own-suite ranking; ratchets against a recorded value; the guard's `0/1/2` contract and "report rule+location, never the value"; snapshots as the guard's evidence. |
| Same pin, `references/floor-guard.md` (`Contract`, `Adapting it`) | Exit-code semantics and the refusals: a `2` must not read as clean; regexes are deliberately shallow; the reference is a starting point, not a finished tool. Not adopted: porting the script as a library product tool. |
| `docs/absorption/2026-10-02/reviews/REVIEW-A1-ADDY-AB.md` (G5), source `references/definition-of-done.md` | Standing policy vs task acceptance criteria; a task needs both; a single green test is not closure; the checklist is a reference for creating/applying an accepted policy, not a new mandatory baseline or a policy owner; policy revision belongs to the valid authority. |

Narrowed from the sources: all numeric defaults and the external-checker quota; the floor-guard script is not shipped as a product tool. Legitimate test deletion, reasonable suppression and incomplete independent candidates are not automatic violations.
