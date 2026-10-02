# Human procedure · candidate method body

- **Status:** candidate distilled under `REVIEW-A3-MATT-DEF` (DEF-7, 2026-10-02); not yet an accepted reference; creates no authority, trigger, or gate. A fixed-diff review still applies.
- **Method owner when bound:** the authority that owns the procedure's action permission. This method scopes a human-driven procedure and its value flow; it does not grant action authorization and does not replace the redacted-evidence custody boundary.

## When manual

1. Use only for steps a human must perform: provisioning, an unfamiliar third-party dashboard walkthrough, credentials or CI secrets, a one-off migration or cutover. Ordinary executable steps stay with the agent; do not push them to a person.
2. Scope the procedure from the environment first: read the repo (`.env`, `.env.example`, `.env.*`, README, `docker-compose*`, framework config, and `.github/workflows/*` `secrets.*` / `vars.*` references) instead of asking cold. For a migration or transition, identify the current state, the target state, and the irreversible actions between them.
3. Present the ordered stages and the values each produces; let the owner add, drop, or reorder. Done when every stage is named in order. A stage that is a pure action (no captured value) is still a stage.

## Value / action trace

4. For every captured value answer three questions: where the human gets it (which URL, page, or command), where it is written (env file, CI secret, both, nowhere), and whether it is secret (hidden entry) or public.
5. Map each stage to the precise path a human follows: which URL to open, what to do there, where the value is shown, which variable it fills. Where the current UI or exact command is unknown, say so and check the docs or ask; never invent a step that may not exist.
6. Open the URL before asking for its value; use hidden input for anything secret; confirm before an irreversible action; keep one focused task per stage so nothing the human needs scrolls away.
7. Derive the required values from the environment's declarations, not from a wish list. The wizard template's authoring discipline — library helpers fixed, the stages section authored per procedure — is a design example, not a required library.

## Artifact verification

8. Static validation first: `bash -n <script>`, `shellcheck` if available, executable bit. Do not run the procedure end to end yourself when it opens browsers and blocks on human input.
9. Trace the artifact statically instead: every value from the scope step is captured and lands where the scope step said; every CI secret or variable name exactly matches a real `secrets.*` / `vars.*` reference; no example URL or endpoint is inserted as a live outbound target.
10. A first run is unverified: static syntax and value tracing do not prove the procedure works end to end. State that, and name who will run it.
11. Protect human in-flight edits: re-read the target file before writing and write only the authorized sections.

## Partial / limits

12. A helper library does not prove safety. For example, a `write_env`-style helper that appends `KEY=VALUE` directly has to be checked for quoting, encoding, and newlines; a `read`/`confirm` helper that swallows EOF keeps going with an empty or default value; and a `gh` helper may be missing or unauthenticated while the flow still reaches a closing "Setup complete" with the skipped writes listed separately.
13. If such a helper is used, verify: key/value encoding, the destination file's permissions, partial-write behavior, EOF behavior, and the actual target (which file, repository, or secret store). Do not assume the library is never edited or 100% correct; a hidden-input helper prevents terminal echo, not the value entering the process. Secrets follow `guide-redacted-evidence.md` custody.
14. Do not read all `.env` values or secrets automatically; read only the specific keys this procedure needs. Do not add a fixed TTL/delete step or require committing a repeatable setup path; those are task decisions.
15. The procedure's action authorization comes from the task delegation; this method does not create permission for provisioning, migrations, secret writes, or CI changes.

## Limits

- No fixed stage count, no mandated helper library, no run-once gate, and no automatic secret discovery.
- Static checks and a value-placement trace are not end-to-end evidence; a procedure's real effect stays unverified until someone actually runs it under its authorization.
- Later cross-source work may merge this body with another manual-procedure source; keep the environment-derived scope, the three value questions, the open-before-ask and hidden-secret operations, the static trace, and the helper-does-not-prove-safety boundary.

## Source anchors

| Source | Pin / path | Section |
| --- | --- | --- |
| Matt Pocock, `mattpocock-skills` | `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`, `skills/engineering/wizard/SKILL.md` | §1 Scope the procedure (L16–25): environment-derived values, three questions, ordered stages; §2 Map each stage's journey (L27–31): exact path, never invent steps; §3 Author the wizard (L33–37): open URL before asking, hidden secrets, confirm irreversible, one task per stage; §4 Verify and hand off (L39–43): static checks and value tracing, no end-to-end run |
| Matt Pocock, `mattpocock-skills` | same pin, `skills/engineering/wizard/template.sh` | Library vs stages marker; `ask`/`ask_secret` (L100–128); `write_env` direct `KEY=VALUE` upsert (L130–141); `read` with `|| true` (L80, L87, L108, L122); `set_secret`/`set_var` fallback to a skipped list (L143–168); `finish` prints "Setup complete" while skipped items remain (L170–182) |
| Product core | `methods/guide-redacted-evidence.md` | Sensitive-value custody and the raw-artifact boundary reused by this method |
