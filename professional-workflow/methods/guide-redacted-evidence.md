# Redacted evidence guide · on-demand support (accepted bounded reference)

Status: accepted bounded reference (2026-10-02); creates no authority, generator, or gate. Source anchors and authored additions are marked.

## Use

On demand, when a defect-feedback or behavior-claim task will show, record, hand off, or store commands, output, or captured artifacts. When this support is needed, add the guide to the task's existing bound/read set; it is not mandatory loading. The guide does not select tasks, decide verdicts, or replace the Charter; the Charter binds applicability and tool permissions.

## Rules

1. **Redact before show/record/store.** Replace every secret with `<REDACTED>`; build loops so credentials stay in the environment rather than in what is shown. Captured artifacts that carry auth headers: quote only the lines that carry the signal. *(Source: matt `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`, `skills/engineering/diagnosing-bugs/SKILL.md` §Redact L12–16.)*
2. **Collect or reuse minimal necessary evidence inside the existing authorization.** Within the task's valid delegation you may either collect new observations or reuse existing records; keep only the minimum signal-bearing evidence, and redact before you show, record, share or store it. Creating raw artifacts follows Rule 4's separate custody boundary. This requires no re-asking each time, and it does not authorize capture outside the valid authorization. *(Retained from the Matt Redact passage L14–16; the collect-or-reuse framing is an authored adaptation; custody default from cursor verify-this below.)*
3. **Sensitive artifact custody.** When artifacts may contain sensitive code, prompts, screenshots, HTTP bodies, or heap data, keep only minimal inline evidence unless the user agrees to disk storage. *(Source: cursor `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`, `cursor-team-kit/skills/verify-this/SKILL.md` §Artifact Layout L37–51; artifact kinds §Local Surfaces L28–35.)*
4. **Raw handling is a separate explicit boundary.** *(Authored operation built on rules 1–3; not upstream text.)* General conditions: existing valid consent on record; a restricted location; a custody/cleanup boundary (who may read, when deleted or expired); no self-expansion of authorized access. Real-task access, data, and network limits are inherited from the task's valid policy and Charter — this guide neither grants nor unconditionally cancels existing allowances, and an existing valid authorization can be inherited without re-asking each step. If consent or the custody/cleanup boundary is missing, stay on the default path or request alternatives.
5. **Insufficient after redaction → ask, don't de-redact.** State the insufficiency and request (a) access to a reproducing environment, (b) a redacted captured artifact (HAR / log / core dump / timestamped recording), or (c) permission for temporary instrumentation. *(Source: matt §Redact L16; §When you genuinely cannot build a loop L53–56; §Completion criterion L59.)*
6. **Human-in-the-loop: step vs capture.** Human-only actions stay in the user's own flow as a `step`; the script prompts and waits, does not collect the action, and does not technically suppress the terminal's own echo. Observations safe to echo may use `capture`, whose values print back as `KEY=VALUE` for the agent — so credentials never go into `capture`. Prefer agent-runnable loops; HITL is a last resort. *(Source: matt `scripts/hitl-loop.template.sh` header L13–16, helpers L20–31, example L34–38; `SKILL.md` L35, L64.)*
7. **A status code is not a cause.** *(Authored caution; see example.)* `HTTP/1.1 401` distinguishes "authentication not accepted" from e.g. `411`, but does not by itself establish why a bearer token was rejected (expired / revoked / scope). Infer the cause only from an authorized redacted error code or a separately authorized probe — never by retrieving the raw token.

## Example (authored; not from the sources)

Scenario: a payment request returns 401 in one environment.

- **Default (correct) — one common case:** reuse an already-authorized minimal redacted record, e.g. workspace file `evidence/dbg05/redacted-http.txt`:

  ```text
  POST /v1/charges
  Authorization: Bearer <REDACTED>
  HTTP/1.1 401 Unauthorized
  www-authenticate: Bearer realm="api"
  x-request-id: 7f3c…
  ```

  This supports the 401-vs-411 distinction; it does not establish the rejection cause. Get an authorized redacted error code (`error=token_expired`) or run a separately authorized probe. If the loop needs a fresh observation, collect it inside the same valid authorization and keep the same redact-first discipline — reuse is the common case here, not a ban on new collection.

- **Wrong (rejected) on the default route:** without an explicit raw authorization, writing full response headers/body to disk first (`curl -D …/headers.txt -o …/body.json …`) and redacting afterwards. Even with `$AUTH_TOKEN` in the command text, the response content (Set-Cookie, body) has left the authorized boundary; showing a few lines later does not undo the persistence. Under an existing valid raw authorization, Rule 4's restricted location and custody/cleanup conditions apply instead — this sentence targets the un-authorized default route, not every raw capture.

- **Raw branch:** allowed only under rule 4's general conditions (existing valid consent, restricted location, custody/cleanup, no self-expansion; real-task limits inherit valid policy/Charter). Write only the needed subset and apply the cleanup boundary. It is never the default.

## Conditions and exceptions

- Applies whenever evidence leaves the current context (stored, committed, handed to another agent/reviewer, logged, or shown).
- "Report exact commands" remains valid: a command can be recorded verbatim when its credentials come from environment variables; this does not extend to raw response custody.
- If a required signal exists only in raw content and consent/custody cannot be met, the correct outcome is an explicit insufficiency report, not de-redaction.

## Limits

- No new gate, validator, checklist, or always-on tooling; no claim that any host actually enforces redaction.
- Does not change verdict mapping, ownership, independence, or task authority.

## Source anchors

| Source | Pin / path | Section |
| --- | --- | --- |
| mattpocock-skills | `c55ee460…`, `skills/engineering/diagnosing-bugs/SKILL.md` | §Redact L12–16; §Phase 1 item 10 L35; §When you genuinely cannot build a loop L53–56; §Completion criterion L57–66 |
| mattpocock-skills | `c55ee460…`, `skills/engineering/diagnosing-bugs/scripts/hitl-loop.template.sh` | header L13–16; helpers L20–31; example L34–38 |
| cursor-plugins | `ecc249f1…`, `cursor-team-kit/skills/verify-this/SKILL.md` | §Artifact Layout L37–51; §Local Surfaces L28–35 |
