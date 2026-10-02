# Trust boundaries and action classes · candidate method body

- **Status:** candidate distilled under `docs/absorption/2026-10-02/reviews/ORACLE-REVIEW-A1-ADDY-CD.md` (C6, 2026-10-02, source `addy@2686b620`) and extended under `docs/absorption/2026-10-02/reviews/ORACLE-REVIEW-A4-DEF3.md` (J5, 2026-10-02, source Cursor `ecc249f1`); not yet an accepted reference; creates no authority, trigger, or gate. A fixed-diff review still applies.
- **Method owner when bound:** D/B design the boundary and the contract; E implements inside its delegation; the "Ask First" decision belongs to the authority that actually owns that action class. This method never approves an action by itself.

## Use

Use when designing or reviewing something that accepts external input, deletes/moves/overwrites, adds an integration or permission, handles personal data, or routes model output into an execution surface. It is an on-demand design aid, not a stage gate; everyday code that touches none of these does not need it.

## Trust follows the writer, not the channel

Untrusted data does not only arrive as an HTTP request, form field, upload, webhook, third-party response, queue message or model output. It also arrives as **another process's command line or environment, a filename on a shared volume, or a path inside a job payload** — values that look internal because the OS handed them over. The test is: *who wrote this value, and what can they make it be?* A value read from the kernel proves where it arrived from, not who authored it.

If you cannot name the trust boundaries of a feature, you are not ready to secure it. Most breaches begin in design, not in a missing string check.

## Five minutes of threat modeling

Write down, before hardening:

1. **Boundaries** — every point where a value crosses from a writer you do not control into a decision you make.
2. **Assets** — what is worth stealing or breaking: credentials, personal data, payment data, admin actions, money movement.
3. **Lenses** — run the six STRIDE questions over each boundary and record the relevant ones: spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege. It is a lens, not a ceremony; two minutes each.
4. **Abuse cases** — next to the use cases, write "how would I misuse this?" and make the first answer a test.

## Three action classes

The classes below are about *which authorization an action needs*, not about how dangerous it feels.

### Always do (inside the task's own scope)

- Validate external input at the boundary where it enters; parameterize queries; encode output for its sink.
- Use the platform's encryption for external transport; hash passwords with a slow password hash.
- Set the security headers the response actually needs; session cookies `httpOnly`, `secure`, and a `sameSite` value that matches the contract.
- Run the ecosystem's native audit against the committed lockfile before release, where the project has dependencies.

### Ask First — the action class needs an authorization that covers it

- adding a new authentication flow or changing authentication logic
- storing a new category of sensitive data (personal, payment, health)
- adding a new external service integration
- changing cross-origin (CORS) configuration
- adding a file-upload handler
- modifying rate limiting or throttling
- granting elevated permissions or roles

"Ask first" means the action needs the authority that owns that class — the policy owner, role, or human the project's valid authority reserves it to. It does **not** mean the executor may self-approve, and it does **not** universally mean "return to a human": where an existing valid policy already delegates that class (a standing upload-review process, an already-approved integration pattern), the action proceeds under that delegation. What is forbidden is treating this method, or the executor's own confidence, as the approval. If you cannot identify who owns the class, that is a recall condition, not a licence.

### Never

- commit secrets to version control
- write secrets, tokens, passwords or full personal data into logs
- treat client-side validation as a security boundary
- disable a security header for convenience
- pass user data into dynamic evaluation or raw HTML injection
- keep a session token in client-readable storage as the auth mechanism
- expose stack traces or internal errors to users

## Operator identity and external channels

When a process acts as, or on behalf of, an operator, ask what actually establishes that identity and what the action's target actually is.

- **The worker can control its own argv, environment and working directory.** Values that look internal for that reason are not a trust source, and the workspace is not necessarily trusted either.
- **An operator flag file proves only its strongest property.** The source establishes the operator through the OS account's home directory (not the environment's `HOME`) plus a non-symlink file owned by the operator with mode `0600`. That is weaker than it reads: if the worker runs as the same UID and can write that home, `0600` does not distinguish the operator from the worker, and the source's own code notes that a stronger boundary is needed. Do not describe this as universally unforgeable, and do not treat a passing test suite (environment spoofing rejected, `HOME` override rejected, symlink rejected, half-configuration rejected) as complete identity security — those tests do not rule out same-user home writes or a forged plan.
- **A workspace pointer can point at a forged plan.** A `--workspace`/plan selection is an input, not an authentication. Schema validity does not authenticate the thread or object coordinates inside the file; the target must come from trusted configuration, not from "the plan exists and its fields are non-empty".
- **Resolve the external target from trusted configuration.** Which channel, thread or object an external write reaches comes from authorized configuration, together with the actor's identity and scope. Without a valid authorization and a trusted target, do not perform the external write (message, deployment, credential change, API call). A half-configured token or target should fail early rather than fall back to a default.
- **Encode a field for the structure it enters.** JSON, shell and templates each need their own encoding; quoting or `JSON.stringify` protects the surrounding syntax, not the meaning of natural-language content. An escaping layer does not prevent prompt injection: the injected text was never a syntax error.
- **Only real isolation constrains actions.** A convention, a marker file or an escaping helper is a convenience layer. The guarantee comes from permissions, credentials and process boundaries the actor genuinely cannot cross. Where a deployment wants this mechanism, the responsible party must verify the host isolation and who maintains the trusted configuration.

## Destructive operations on derived paths

A delete, move or overwrite is only as safe as the value naming its target. A shape check ("absolute path, at least one directory deep") proves well-formedness and is routinely mistaken for authorization. Before the call, require **all three**:

1. the resolved target (symlinks resolved, on the resolved path — never the raw string) sits under an allowlisted root;
2. it is at least one level *below* that root, so the root itself is never the target;
3. it carries ownership evidence that was read **before** the operation — and before any teardown that would remove it — so "absent" and "not mine" stay distinguishable.

On refusal: **log the rejected target and stop.** Never fall back to a broader default path; a cleanup routine that falls back is the failure this guards against.

Two honest limits, because the check reads stronger than it is:

- **A marker inside the tree is self-attestation.** Anything that can write to the tree can write the `.owner` marker. The expected owner must come from authenticated state, and the marker needs integrity protection (restrictive ownership or a MAC) before it counts as authorization.
- **Resolving a path and then operating on the name is a check/use race** wherever an untrusted process can swap an ancestor. On a shared volume, hold the target by descriptor with no-follow, beneath-the-root operations, or ensure the hierarchy cannot change for the duration.

## Server-side fetches of user-influenced URLs

For webhooks, "import from URL", image proxies, link previews and similar:

- allowlist scheme and host;
- resolve **all** DNS records and reject any private or reserved address — loopback, link-local (`169.254.169.254`, the cloud metadata endpoint), private and unique-local ranges, IPv4 and IPv6;
- forbid redirects.

Honest gap: this still has a TOCTOU window because the fetch resolves DNS again after the check, so a short-TTL record can rebind to an internal address between validation and connection. For high-risk surfaces, resolve once and connect to the pinned IP, or put a filtering agent in front. Do not describe the allowlist check as eliminating SSRF.

## Dependencies and install scripts

- **Locate the real installation boundary and manager first.** Use the workspace root that owns the lockfile; treat an independent nested project as separate only when it is actually outside that workspace. Corroborate the declared package manager, the lockfile and CI; stop on disagreement or competing lockfiles.
- **Block dependency lifecycle scripts before their first execution.** Bootstrap with scripts disabled or a documented fail-closed policy, inspect the pending script source, approve the minimum, commit that policy, then verify with a clean frozen/immutable install. Never blanket-approve.
- **Audit known advisories; do not confuse that with trust.** An audit matches known advisories and does not catch a newly malicious or typosquatted package. Triage critical/high by **reachability** (runtime, build, test, deploy paths) and by whether a fix exists; preview and test each upgrade rather than applying forced remediation (`npm audit fix --force` and equivalents may cross declared dependency ranges). Document every deferral with a reason and a review date.
- **Tool-specific calls need their support file.** Manager flags, frozen-install semantics, signature checks, and script-approval mechanisms differ by version and product. Verify against the actual manager's documentation for the version in use before copying a command; the source's manager matrix is point-in-time.

## Personal data

Hardening asks "can an attacker read this?" Privacy asks "should we hold it at all, and for how long?" The cheapest data to protect is the data never collected.

- classify fields as they are added (non-personal / personal / sensitive) — you cannot protect or delete what you cannot find
- collect only against a stated purpose; "might be useful later" is breach scope, not a purpose
- set retention up front, and have a working deletion path for the copies that the applicable policy and legal basis require
- support the data-subject rights the jurisdiction requires (export, correction, deletion) by designing a schema where a person's data is findable and erasable
- where collection or third-party sharing depends on consent, keep that consent auditable; where it rests on another valid basis, state that basis — this method does not decide which basis applies
- make region a configurable policy, not a hardcoded assumption
- keep personal data out of telemetry

Which copies must be erased (including backups, caches, search indexes and analytics copies), whether an obligation is consent-based, and how long a lawful retention may run are decisions for the applicable policy and the responsible professional authority. The operations here are to know where the data is, not collect what the purpose does not need, and keep telemetry clean of it. A lawful retention obligation, or a backup cycle without a feasible per-record deletion, is not automatically a violation: it has to be declared, with its compensating control or its accepted risk.

The legal basis and the specific obligations come from the applicable policy and professional responsibility. This method does not produce a uniform legal conclusion and must not be cited as one.

## Model output and prompts

- **Model/output content is untrusted input**, not a command. Do not hand it to a sink as-is: not to `eval`, an unparameterized query, a shell, raw HTML, or a file path. Parse defensively, validate against a schema, then encode for the sink; where the sink is a query, a shell or a path, the validated value may legitimately be used as a parameter or argument under that sink's own rules, never as raw text.
- **Prompts can be hijacked.** Untrusted text in the context — a user message, a fetched page, a document — can carry instructions. **The system prompt is not a security boundary**; permissions are enforced in code. Keep secrets, other tenants' data and policy information that must not be exposed out of the context window. A legitimate system prompt may appear in a context that genuinely needs it; what must not enter a lower-privilege context is its sensitive content. Scope tool permissions, validate every tool argument, confirm destructive actions, and cap tokens, request rate and recursion depth.

## Examples with their limits

- A `.owner` marker in a directory proves only that something could write there. It is not authorization unless the expected owner comes from authenticated state and the marker has integrity protection.
- Checking DNS before a fetch does not eliminate SSRF; the second resolution can rebind. Pinning or filtering is the mitigation, and even then the claim is bounded by what the filter actually covers.
- A successful authentication proves identity, not permission on a specific resource. Every request needs an authorization check on that resource (the classic IDOR failure: authenticated, but reading someone else's record).
- A public API may legitimately allow cross-origin requests; whether credentials are allowed depends on the contract and must be explicit, not a default.
- **Accepted is not answered, and no error is not cancelled.** A probe that only creates/accepts a session and sends a request, then records success without observing a response, proves at most that the call was accepted — not that the model can complete the task. A cancel whose error is swallowed and which still records success proves nothing about whether the work stopped, whether resources remain, or whether consumption was zero. Claims like "the model completed" or "the task was cancelled" need the corresponding observation.

## What is not adopted

- The seven "Ask First" classes are not a universal "return to a human" list, and they are not a fence against legitimate pre-approved paths.
- Fixed patterns for every cookie/CORS/header, fixed rate limits or password rounds, mandatory deletion from every backup regardless of the applicable retention or legal basis, mandated agreements as a universal requirement, and a blanket ban on any system prompt in a legitimate context are not adopted. What is protected is secrets, cross-tenant data, and policy information that should not be exposed.
- The source's "rotate a secret first, then purge history" is risk-disposition advice. The action still needs valid authority; do not self-change credentials, policies or history.
- This method does not certify any SDK, manager or platform as fully secure. A copied tool-specific call must be checked against its support file and version.

## Limits

- No universal control list, no mandatory header set, no fixed numeric threshold, no security gate. Controls follow the boundaries and assets of the actual feature.
- The dependency-upgrade review path (upgrade choice, coverage, lockfile handling) is a separate on-demand guide in the integrated method set; this method states the security-side gate and does not duplicate that procedure.
- Action permission comes from the task's valid authority and Charter. Naming a boundary or writing a checklist is not approval to act. This method does not grant creating operator flag files, adding credentials, sending to external channels, or lifting an existing restriction; those are actions for the authority that owns them.
- An operator-identity mechanism is host-specific. If a real deployment adopts one, verify the host isolation and the trusted-configuration maintenance rights rather than copying the source's file convention.
- The examples distinguish real observed behaviour (for example, a browser/manager documented behaviour), locally reproduced evidence, and code illustration. A code snippet in a source is not evidence that the same control works in the reader's stack.

## Source anchors

| Source | Retained contribution |
| --- | --- |
| Addy Osmani, `addyosmani-agent-skills` at `2686b620fc1fed2e8f60c704839c766b8594c6b6`, `skills/security-and-hardening/SKILL.md` (`Process: Threat Model First`, `The Three-Tier Boundary System`, `Hardening Controls`, `Dependencies and supply chain`, `Personal data and privacy`, `AI / LLM features`, `Red Flags`) | Trust follows the writer (including local process values); STRIDE as a lens plus abuse cases; the Always / Ask First / Never classes; dependency boundary, install-script gate, audit-vs-trust and reachability triage; privacy as minimization/purpose/retention/deletion; model output untrusted and the system prompt not a security boundary. |
| Same pin, `skills/security-and-hardening/references/hardening-patterns.md` (`Server-Side Request Forgery (SSRF)`, `Destructive Operations on Derived Paths`, `Dependency Audit Triage`) | SSRF allowlist + all-records + no-redirect with the DNS-rebinding TOCTOU stated honestly; destructive-path three conjunctive conditions and the self-attestation / check-use limits; the audit triage tree. |
| Cursor plugins, `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`, `orchestrate/skills/orchestrate/scripts/cli/util.ts` (operator/target boundary), `scripts/cli/task.ts` (run/cancel entry points), `models.ts` (probe path), `scripts/__tests__/operator-boundary.test.ts` | Worker-controlled argv/env/cwd and non-trusted workspace; the operator-flag convention with its honest weakness (OS userInfo home, non-symlink uid/`0600`; same-UID home writes break it); target resolution from trusted configuration and fail-early half-configuration; per-structure encoding; probe-accepted ≠ model-completed, cancel-error-swallowed ≠ cancelled; green boundary tests ≠ complete identity security. Runtime scripts are not ported. |

Narrowed or excluded from the sources: the fixed header/CORS/cookie patterns, the fixed rate-limit and password-round numbers, mandatory backup deletion and agreement signing, a blanket ban on system prompts in legitimate contexts, and the universal "all Ask First operations return to a human" reading. The Cursor `orchestrate` runtime scripts are not ported because no current task consumes them and they would bring their own permissions and dependency boundary — a consumption decision, not a judgment that scripts are worth less. The operator/action-boundary experience above is retained.
