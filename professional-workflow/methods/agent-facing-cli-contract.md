# Agent-facing CLI contract · candidate method body

- **Status:** candidate distilled under `REVIEW-A2R-CURSOR-ABC` (MG-3), extended under `REVIEW-A2R-CURSOR-ABC2` (MG-5), `ORACLE-REVIEW-A4-DEF3` (J4) and `REVIEW-GATE2-A4-CURSOR-DEF` (G12, 2026-10-02); not yet an accepted reference; creates no authority, trigger, or gate. A fixed-diff review still applies.
- **Method owner when bound:** B behavioral contract for the CLI's external behavior. Implementation and its authorization stay with E; this method supplies contract operations and failure modes for a specific consumer class.

## Use

Use on demand when designing or reviewing a command-line interface that an agent or automation will run — commands, flags, help, errors, exit behavior, output, retry, preview. It is a behavior contract for that consumer class, not a general CLI style guide. Cross-reference the API/idempotency sources when repeated-effect semantics need more than this contract states.

## Consumers and modes

1. Non-interactive first: every input is expressible as a flag or flag value; do not require arrow keys, menus, or timed prompts. An interactive fallback comes after flags are missing, never before.
2. Distinguish an explicit interactive/TTY mode from headless mode. Headless mode with missing required input exits immediately with a clear, actionable message; it does not open a menu or wait.
3. Positional arguments remain legitimate where the tool's shape calls for them; stdin is used only where the data flow fits (for example `cat config.json | mycli config import --stdin`).
4. Success output is machine-useful — IDs, URLs, durations, counts. Plain text is acceptable; decorative output alone is not. Whether output must be JSON, and which exit codes are fixed, are contract choices B accepts; the source claims machine usefulness, not a specific format.

## Discover / compose

5. Layered help: `mycli` lists commands, `mycli deploy --help` documents that command. Do not print the entire manual on every run; each subcommand owns its documentation so unused commands stay out of context.
6. Every subcommand has `--help` with real invocations in an Examples block; examples pattern-match better than prose.
7. Keep a consistent command shape (for example `resource` + `verb`) so an agent can infer unseen commands, and support pipelines/chaining where the data flow justifies it (for example `--tag $(mycli build --output tag-only)`).

## Error / retry behavior

8. Missing required input fails fast: exit immediately with a clear message, a correct example invocation, and how to discover the missing value. The counterexample is the hang: `mycli deploy` opening "Which environment?" with arrow keys in a headless run.
9. Agents retry, so a successful command should be safe to run twice — a no-op or an explicit "already done", not a duplicate side effect. Not every successful action is naturally idempotent (sending a notification, for example): declare the repeat semantics, the operation identity, and how to query or recover the outcome after an uncertain failure. Do not promise an unconditional no-op.
10. `--yes` / `--force` skips UI confirmation for actions that are already authorized; it does not bypass permission checks, reserved decisions, or policy. Keep the safe default for humans.

## Repeat / partial failure

11. Ask the two questions this contract must answer: what happens if the command runs twice in a row, and what happens if the previous run crashed partway? If either answer depends on whatever state was left behind, the operation needs a reconciliation step — the CLI exposes the state or the recovery path, and D/E own the reconciliation design.
12. Repeat safety needs a valid starting state and an operation identity (idempotency key, request id, or equivalent). An idempotency key is built from the fields that define the intent and scope — the operation, the target object, and the fixed inputs that change the outcome; a result-changing element missing from the key lets two different intents collide, and which fields are required is task- and provider-specific (no fixed field count or time window here). Finding an existing active object by name is a lookup heuristic, not a complete idempotency guarantee: the lookup may cover only a time window, a status subset, or a bounded list, and the name may not carry the goal, repository, or base. Reuse therefore needs the task's real intent identifier and scope, and "not found" means "not found in the searched window", not "none exists anywhere". It is not a claim that any starting state converges to the same result; an action that cannot be naturally idempotent declares its duplicate protection, query/recovery path, or compensation instead of promising exactly-once.
13. Partial failure is visible: report what succeeded, what is still in doubt, and the safe next command. Do not report a partial run as completed, and do not hide an uncertain outcome behind a success exit code.
14. Technical idempotency pattern details belong to the technical idempotency guide integrated with the API/idempotency sources; this contract states the CLI/API-visible behavior and does not repeat those rules.
15. Name the runtime and target explicitly and where the key comes from: when the client can silently default (for example to a local runtime), an omitted option is not a decision. Confirm before submission which runtime and target the call will use.
16. Keep the identity stable and observable: record the agent and run identifiers right after submission, before streaming, and capture the actual terminal state. Separate the failure stages — submission rejected, run refused, run errored, observation failed — because only some of them prove that anything ran. Cancel or dispose the resources the client actually holds, and re-pass configuration the platform does not persist across a resume (inline MCP parameters, for example).
17. Do not generalize a client library's promise: a client error does not always mean the work never executed, a "retryable" flag does not guarantee no duplicate effect, and a dispose or cancel call does not prove all remote work stopped. A network error may leave the outcome unknown; check the stage's actual guarantee and the existing operation identity before retrying.
18. Check the platform's supported operations before calling them — an operation may be unsupported on a detached handle — and treat a version or capability mismatch as a real gap rather than assuming parity with the documentation.

## Effects / preview

19. Destructive or irreversible actions offer `--dry-run` (or equivalent) so the caller can preview what would change before committing.
20. A dry run may still touch external systems (reads, permission or quota validation). Declare the actual effect and verify it; "dry" does not by itself mean "no effect".
21. A preview reports the plan; it is not authorization to execute, and it does not replace the accepted contract.

## Examples

- **Headless missing input.** `mycli deploy --env staging` (no `--tag`) in a non-TTY context exits non-zero with `Error: No image tag specified.` and the repair invocation `mycli deploy --env staging --tag <image-tag>` (plus how to list tags), instead of prompting. The check is observable: run it with stdin/stdout not a TTY and confirm a non-zero exit with no wait for input.
- **Existing active object.** Before starting a job, search for an existing active object and inspect its real state and parameters. If it matches the same intent and scope, reuse or report it; if an input or the base changed, that is a different intent. Report what was found, in which window, and what was not searched.
- **Repeated invocation.** `mycli deploy --env staging --tag v1.2.3` run twice reports "already deployed" or no-ops the second time; a notification command instead declares its operation identity and how to query whether it was sent.
- **Preview effect.** `mycli deploy --dry-run --env production` prints the plan; the run may still validate permissions against the environment, so the observed effect is recorded rather than assumed to be zero.

## Counterexamples

- A menu or timed prompt on a command that automation will call.
- Printing the full manual on every invocation (context dump).
- A missing-flag hang instead of a fast exit with a fix.
- Treating `--yes` as permission for the action, or `--dry-run` as proving no side effect.
- Claiming "run it twice and nothing happens" for an action whose repeat semantics were never declared.
- **Same name reused across repos or goals.** A launcher derives its job name from the goal text and looks up an active job by exact name within a recent window; two different repos (or a changed base) with the same name are treated as one job, so the second intent is never started or the first is adopted for the wrong work. Name plus a window is a heuristic; the key must carry the real scope elements.
- Treating a client error as proof that the work never ran, or a retryable flag as proof that a retry cannot duplicate the effect.

## Conditions and exceptions

- Not every CLI needs every flag or shape; apply what the actual consumer and claim need.
- Retry and idempotency detail beyond this contract belongs to the API/idempotency source; this method states the CLI-visible contract, not the service's full deduplication design.
- Fixed JSON schemas and exit-code tables are B choices, not source mandates; do not present a design suggestion as a source requirement.
- Running or validating a CLI needs its own authorization; reviewing the contract does not grant it.

## Limits

- No mandatory flag set, no validator, no fixed output format, and no universal idempotency promise.
- Detection and termination are bounded by the search: an incomplete directory or unknown state is reported as such, and "not found" does not prove no object exists service-wide. Cancel-running and prune-pending are different operations with different effects, and `--force` is a technical option, not permission to duplicate or to skip the existing-object check. Loops, queues, retry counts, and timeouts belong to the adopting runtime.
- This method does not replace the accepted behavior contract, the technical Plan, or independent evaluation.
- Later cross-source work may merge this body with the API/idempotency source; keep the modes, actionable-error, repeat-semantics, preview-effect, and confirmation-bypass boundaries above.

## Source anchors

| Source | Pin / path | Section |
| --- | --- | --- |
| Cursor plugins | `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`, `cli-for-agent/skills/cli-for-agents/SKILL.md` | Non-interactive first; Discoverability without dumping context; `--help` that works; stdin, flags, and pipelines; Fail fast with actionable errors; Idempotency; Destructive actions; Predictable structure; Success output; When reviewing an existing CLI |
| Cursor plugins | same pin, `pstack/skills/principle-make-operations-idempotent/SKILL.md` | §The test (L19–22): runs twice in a row, crashed partway, re-execution converges; the pattern body is deferred to the a4 technical idempotency integration (shared mechanism with the Addy API source) |
| Cursor plugins | same pin, `orchestrate/skills/orchestrate/scripts/cli/task.ts` §findActiveRootPlanner/inferKickoffRootSlug (L478–515); `scripts/__tests__/kickoff-dedupe.test.ts` | Exact-name lookup over a bounded list and a recency window heuristically adopts an active object; the slug derives from the goal text only, and `--force` skips the lookup |
| Cursor plugins | same pin, `cursor-sdk/skills/cursor-sdk/SKILL.md` | Three invocation patterns and Top Five Traps: explicit runtime/repo or local cwd selection, stable agent/run IDs, startup error versus run error, dispose in finally, supported-operations checks, and configuration not persisted across resume |
| Cursor plugins | same pin, `cursor-sdk/skills/cursor-sdk/references/error-handling.md` | Two failure axes (`CursorAgentError` versus `RunResult.status` error/cancelled), retryable versus configuration/auth errors, unsupported run operations, and run-ID lookups |
