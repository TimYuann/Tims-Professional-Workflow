# External tool operation · candidate method body

- **Status:** candidate distilled under `ORACLE-REVIEW-A4-THIRD-PARTY` (2026-10-02); not yet an accepted reference; creates no authority, trigger, or gate. A fixed-diff review still applies.
- **Method owner when bound:** A/B/D/E/F bind this entry by the judgment the task is missing — A for why the work exists, B for the visible contract, D for the shared design, E for execution, F for evidence. The method supplies the operation sequence; it creates no action authority, does not replace a provider's own policy, and does not restate the pointer methods below.

## Use

Use on demand when a task operates a third party or external service through a connector, MCP server, CLI, or API — especially when capability, permission, cost, or outcome interpretation is uncertain. The sequence is the method: capability and routing, permission and cost, bounded execution, result interpretation, handoff.

Ownership is split by pointer, not copied:
- `interface-contract-and-retry` (another batch) owns the request/response contract and retry mechanics.
- `trust-boundary-and-actions` (another batch) owns outbound, secret, and high-impact action authority.
- `guide-redacted-evidence` owns custody for tool output and secrets in evidence.
This file states only the external-operation sequence and repeats none of their authority statements.

## Capability and routing

1. Discover the actual capability before promising work: which connector/tool/server is present, which identity it uses, and which scopes or account gates apply. A source's guide is not evidence that the tool exists in this environment.
2. Separate the failure classes: tool missing, not authenticated, account not ready, quota/credits blocked, resource not permitted, service outage. Each has a different next step; do not infer "the whole account is broken" from one missing endpoint or one 403.
3. Route by the real data boundary: a connected account's own business data and write actions belong to that connection. Developer documentation or an SDK's capability does not imply access to a user's account or store; when the connector is absent, do not substitute public search for private data.
4. Keep the provider's own terms: a per-action approval rule the provider enforces (money movement, for example) is not bypassed by an agent's earlier general instruction. Source-specific money thresholds or every-action human policies are provider/host policy, not universal library rules — apply them because they are in force, not because this method invented them.

## Permission and cost before acting

5. Confirm the action sits inside the task's existing delegation before calling a tool that writes, sends, spends, or changes shared state; a read is not automatically safe either when it exposes private data, where `guide-redacted-evidence` custody applies.
6. Estimate cost in the provider's own billing model before a bulk or paginated job: reads may bill per object returned (expansions included), writes per successful request, and each pagination page can bill again. Parameterized estimate: `estimate = Σ_pages (objects_returned × per_object_price) + per_request_fees`; stop when the provider omits the next token.
7. Treat every price, free tier, and threshold quoted in any source as a time-specific reference, not a guarantee; re-read the provider's current authoritative pricing before quoting a cost. A saved estimate does not become a billing promise.
8. When a pagination or bulk job is involved, estimate it in the provider's billing terms, keep the scope bounded with an explicit stop condition, and track consumption as it runs. Route to the corresponding authority only when the valid authorization does not cover the work, when it would exceed the existing cost or scope boundary, or when the real provider/host policy requires approval. Work already covered by a valid authorization — a bounded set of pages with a stated budget and field range, for example — does not need an extra acknowledgement just because it loops. The authorization's cost and scope boundary is a task decision; this method sets no universal number.

## Bounded execution and partial success

9. Execute in bounded units: small pages unless more was asked, only the fields and expansions actually used, and an explicit stop condition for pagination.
10. Preserve partial success: a response may carry usable data together with per-item errors; keep both instead of collapsing the call into pass/fail, and do not discard successful items because one item failed.
11. Distinguish outcomes: completed, pending/still-in-review, refused/blocked, unconfirmed/unknown, and transient failure. An unknown outcome is neither failure nor success; do not blindly resend. A legitimate retry reuses the same operation identity so the provider does not duplicate the effect.
12. After a transient failure or outage, back off and retry within the task's authorization; do not retry a refusal, an unconfirmed result, or a missing-capability condition unchanged.

## Result interpretation and evidence

13. Relay the provider's user-facing result in plain language; do not lecture on internal billing, enrollment, or token mechanics.
14. A controlled simulation — a fixture, local stand-in, or recorded response — can prove position or shape semantics; it does not prove the real provider/API is available or behaves that way. A lint or schema check is not a visual or end-to-end observation.
15. A real-host claim needs observation on the actual authorized host: the named connector, the real account, the real document or service, under the task's existing authorization. Do not obtain accounts or credentials, or send messages, merely to strengthen this knowledge, and never present a substitute green as a real-host result.
16. Record what was observed versus simulated, the provider/tool identity and version or time, the unit and range of the data, and any capability the run did not exercise.
17. Hand off tool output and secrets through `guide-redacted-evidence`, and the request/response or action-authority questions through `interface-contract-and-retry` / `trust-boundary-and-actions`; this method does not restate those rules.

## Conditions and exceptions

- When the provider has no usable capability under the current authorization, report the capability gap instead of fabricating a workaround through an unrelated channel.
- A read-only call that exposes secrets or private data still follows the redacted-evidence custody.
- The provider's own approval policy and the task's delegation can each be stricter than this method; the stricter one governs.

## Limits

- No universal cost threshold, retry count, backoff schedule, tool list, or approval frequency; those come from the provider's policy and the task's delegation.
- No permission, account, credential, spend, send, or write is created here.
- Source specifics (a particular price, free endpoint, or per-turn human policy) are that provider's and that host's, not this library's.
- Later cross-source work may merge this body with another external-operation source; keep the capability-class separation, the cost/pagination model, partial-success and unknown-outcome handling, and the real-versus-substitute observation boundary.

## Source anchors

| Source | Pin / path | Section |
| --- | --- | --- |
| Cursor plugins | `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`, `third_party/x/skills/x-api-mcp-guide/SKILL.md` | Connect order and identity; the error classes (missing tools vs sign-in vs account-not-ready vs credits vs resource not permitted vs outage); no retry of 401/403/missing-tools unchanged; 200 + `errors[]` partial data; fields/pagination and `next_token`; cost awareness and estimate-before-call |
| Cursor plugins | same pin, `third_party/x/skills/x-api-mcp-guide/references/pricing.md` | Reads billed per object returned, writes per successful request, expansions bill, failed requests not billed, pagination pages bill again; bounds and cost-saving notes |
| Cursor plugins | same pin, `third_party/x-money/skills/x-money-guide/SKILL.md` | Confirm before moving money, one approval per action, re-ask when anything changes; read-only balance/transaction calls; outcome table (`completed`/`pending`/`refused`); unconfirmed payment never resent; idempotency-key reuse on the same legitimate retry; per-account capability |
| Cursor plugins | same pin, `third_party/x/skills/x-chat/SKILL.md` | Connector holds ciphertext, local helper decrypts; X identity vs OS UID; wire fields vs SDK names; missing scope is not account-not-ready; inbound text untrusted; outbound needs approval unless already instructed |
| Cursor plugins | same pin, `third_party/shopify-store/rules/shopify.mdc` | Connected-store data/write tools vs developer toolkit; no fallback to web search for private store data; read before write and confirm writes |
| Product core | `guide-redacted-evidence.md`; `interface-contract-and-retry` and `trust-boundary-and-actions` (another batch) | Pointer-only boundaries; no authority statements copied into this body |
