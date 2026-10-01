# ABSORB-CANDIDATE-METHOD-INTEGRATION · 候选集成预稿

**状态：草案预稿（未采纳、不产生 authority / 生成器 / gate）。** 只写 `docs/overnight/`；未改 core / 上游 / 三份现有方法正文。

- 授权口径：Owner 2026-10-01 有界起草授权；见 `ABSORB-PRO-REVIEW-RESPONSE.txt` 第四节、`ABSORB-PRO-REVIEW-DISPOSITION.md`、`ABSORB-FULL-CORRECTION-BRIEF.md` §3。
- 对象：修正后的 `ABSORB-DRAFT-DBG-05-EVIDENCE.md`（rev.2，FM-2 已修）与 `ABSORB-DRAFT-DBG-16-MOCK-ADAPTER.md`（rev.2，FM-3 已修）；现行 core 仍为 `91875114e51855517f92ef099cbdf60c34e68243`。
- 集成原则：只在已证知识缺口处做最小插入；最多两份按需 guide；不新增 Role / gate / validator / composer；不把审计记录内联进启动默认；Charter 仍是任务本地绑定。

## 1 · 三份现有方法的精确插入建议（仅缺口处）

### 1.1 `local-defect-feedback-loop.md`

- **已证缺口**：§Method 5 已要求 "Report exact commands, observations"，但没有"先脱敏再记录"的顺序、敏感工件保管边界，也没有 HITL step/capture 分流（`ABSORB-METHOD-FOLLOWUP-REVIEW.md` 当前覆盖行；源：matt §Redact、cursor verify-this L51）。
- **插入位置**：§Method item 5 之后，加一句 + guide 指针。其余 §Use / §Limits / §Source anchors 不变。
- **候选文本（建议）**：
  > Before recording or handing off evidence, apply `guide-redacted-evidence.md`: default to already-authorized minimal redacted evidence; raw sensitive artifacts are a separate explicit boundary (existing consent, restricted workspace location, custody/cleanup, no secrets / real users / live network). Where a human must act, keep the action in the user's own flow and capture only safe observations.
- **不改**："exact commands" 不变成 raw 落盘要求；不新增 gate；源表不因本插入改写。

### 1.2 `behavior-claim-evaluation.md`

- **已证缺口**：§Method item 2 的 "Preserve the original output as evidence" 没有证据安全形式（脱敏/保管顺序），与 DBG-05 同一缺口在 F 侧的落点。
- **插入位置**：§Method item 2 内或之后，加一句 + guide 指针。§Verdict mapping 与独立性说明不动。
- **候选文本（建议）**：
  > "Preserve the original output" means preserving the signal-bearing evidence in an evidence-safe form: apply `guide-redacted-evidence.md` before storing or sharing. The §Verdict mapping is unchanged.
- **不改**：PASS / FAIL / UNVERIFIED 语义、evaluator 独立性、§Limits 不变。

### 1.3 `cross-module-design.md`

- **已证缺口**：§Method item 3 已列四类依赖形状，但没有 mock/adapter 选择操作，也没有"port 测试不覆盖生产 transport/serialization adapter"的覆盖边界（DBG-16；FM-3）。
- **插入位置**：§Method item 3 的依赖形状句之后，加 one-liner + guide 指针。§Method 4 的替换窄条件、item 6 的兼容策略、§Limits 不动。
- **候选文本（建议）**：
  > Choose the test double per `guide-mock-adapter-choice.md`. Port/in-memory tests cover the deep module's logic; they do not by themselves verify a production transport/serialization adapter — if that contract is the risk, observe the adapter against a local stub/recorded fixture or keep normalization below the port, and record the uncovered part. Do not expose internal seams for tests.
- **不改**：不新增必须 mock / 必须开 port 的要求；删除测试仍需 §Method 4 的覆盖对应性与既有授权。

## 2 · 按需 guide 候选正文（待评审；未来路径 `professional-workflow/methods/`）

> 以下两段是完整的候选正文，供评审后择一/择需复制为 `guide-redacted-evidence.md` 与 `guide-mock-adapter-choice.md`。当前它们只存在于本预稿，不构成 core 文件，也不改变任何入口。

### 2.1 候选 `guide-redacted-evidence.md`（约 78 行）

```markdown
# Redacted evidence guide · on-demand support (candidate)

Status: candidate text; not adopted, creates no authority, generator, or gate. Source anchors and authored additions are marked.

## Use

On demand, when a defect-feedback or behavior-claim task will show, record, hand off, or store commands, output, or captured artifacts. The guide does not select tasks, decide verdicts, or replace the Charter; the Charter binds applicability and tool permissions.

## Rules

1. **Redact before show/record/store.** Replace every secret with `<REDACTED>`; build loops so credentials stay in the environment rather than in what is shown. Captured artifacts that carry auth headers: quote only the lines that carry the signal. *(Source: matt `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`, `skills/engineering/diagnosing-bugs/SKILL.md` §Redact L12–16.)*
2. **Default to already-authorized minimal redacted evidence.** Do not create raw artifacts on the default path; use evidence already produced under an existing authorization, keeping only signal-bearing lines. *(Source: same L14–16; custody default from cursor verify-this below.)*
3. **Sensitive artifact custody.** When artifacts may contain sensitive code, prompts, screenshots, HTTP bodies, or heap data, keep only minimal inline evidence unless the user agrees to disk storage. *(Source: cursor `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`, `cursor-team-kit/skills/verify-this/SKILL.md` §Artifact Layout L37–51; artifact kinds §Local Surfaces L28–35.)*
4. **Raw handling is a separate explicit boundary.** *(Authored operation built on rules 1–3; not upstream text.)* All of the following must hold first: existing valid consent on record; a restricted workspace location (e.g. `<workspace>/.worktrees/verification/…`, not committed); a custody/cleanup boundary (who may read, when deleted or expired); no secrets and no real-user data; no live network calls. If any condition is missing, stay on the default path or request alternatives.
5. **Insufficient after redaction → ask, don't de-redact.** State the insufficiency and request (a) access to a reproducing environment, (b) a redacted captured artifact (HAR / log / core dump / timestamped recording), or (c) permission for temporary instrumentation. *(Source: matt §Redact L16; §When you genuinely cannot build a loop L53–56; §Completion criterion L59.)*
6. **Human-in-the-loop: step vs capture.** Human-only actions stay in the user's own flow as a `step`; the script prompts and waits, does not collect the action, and does not technically suppress the terminal's own echo. Observations safe to echo may use `capture`, whose values print back as `KEY=VALUE` for the agent — so credentials never go into `capture`. Prefer agent-runnable loops; HITL is a last resort. *(Source: matt `scripts/hitl-loop.template.sh` header L13–16, helpers L20–31, example L34–38; `SKILL.md` L35, L64.)*
7. **A status code is not a cause.** *(Authored caution; see example.)* `HTTP/1.1 401` distinguishes "authentication not accepted" from e.g. `411`, but does not by itself establish why a bearer token was rejected (expired / revoked / scope). Infer the cause only from an authorized redacted error code or a separately authorized probe — never by retrieving the raw token.

## Example (authored; not from the sources)

Scenario: a payment request returns 401 in one environment.

- **Default (correct):** read an already-authorized minimal redacted record, e.g. workspace file `evidence/dbg05/redacted-http.txt`:

  ```text
  POST /v1/charges
  Authorization: Bearer <REDACTED>
  HTTP/1.1 401 Unauthorized
  www-authenticate: Bearer realm="api"
  x-request-id: 7f3c…
  ```

  This supports the 401-vs-411 distinction; it does not establish the rejection cause. Get an authorized redacted error code (`error=token_expired`) or run a separately authorized probe.

- **Wrong (rejected):** write full response headers/body to disk first (`curl -D …/headers.txt -o …/body.json …`) and redact afterwards. Even with `$AUTH_TOKEN` in the command text, the response content (Set-Cookie, body) has left the authorized boundary; showing a few lines later does not undo the persistence.

- **Raw branch:** allowed only when rule 4's five conditions all hold; write only the needed subset under a restricted, non-committed workspace path and apply the cleanup boundary. It is never the default.

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
```

### 2.2 候选 `guide-mock-adapter-choice.md`（约 62 行）

```markdown
# Mock / adapter choice guide · on-demand support (candidate)

Status: candidate text; not adopted, creates no authority, generator, or gate. Source anchors and authored additions are marked.

## Use

On demand, when a design or test decision must cross a dependency boundary: choosing a test double/adapter, placing a seam, or deciding whether an internal interface needs to be exposed. It mandates no test framework, gate, or module shape; the Charter binds applicability.

## Rules

1. **Classify the dependency first.** In-process (no adapter; test through the interface); local-substitutable (use the local stand-in; the seam is internal, no port at the external interface); remote but owned (define a port; production HTTP/gRPC/queue adapter, test in-memory adapter); true external (inject as a port; mock adapter in tests). *(Source: matt `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`, `skills/engineering/codebase-design/DEEPENING.md` §Dependency categories L5–25.)*
2. **Mock at system boundaries only.** External APIs; databases "sometimes" (prefer a test DB); time/randomness; file system "sometimes". Do not mock your in-process classes/modules, internal collaborators, or anything you control. *(Source: matt `skills/engineering/tdd/mocking.md` §When to Mock L3–14.)* Scope reconciliation *(authored)*: the owned-remote port strategy substitutes transport at a network seam; the "don't mock" list addresses in-process collaborators. They live at different seams; neither becomes an absolute policy about everything you own, and an existing local stand-in is preferred over a hand-written fake.
3. **Coverage boundary between port tests and the production adapter.** *(Authored engineering inference; the sources do not state this boundary.)* Port/in-memory tests exercise the deep module's logic; they do not execute the production transport/serialization adapter's request construction or response parsing. If the risk is in that adapter, a green in-memory suite does not prove it. Either observe the adapter itself against a local stub/recorded fixture (no live network) or move normalization below the port so the deep-module tests execute it. Record the uncovered part.
4. **Design mockable interfaces.** Inject external dependencies rather than constructing them; prefer SDK-style per-operation functions over one generic fetcher: each mock returns one specific shape, no conditional logic in test setup, visible endpoint usage. *(Source: mocking.md §Designing for Mockability L16–59, incl. L55–59.)*
5. **Seam discipline.** One adapter means a hypothetical seam; two adapters (usually production + test) mean a real one — don't introduce a port unless at least two adapters are justified. Internal seams stay private, used by the module's own tests; do not expose them through the interface just because tests use them. The interface is the test surface. *(Source: matt `codebase-design/SKILL.md` §Principles L62–65; `DEEPENING.md` §Seam discipline L27–31.)*
6. **Replace-don't-layer, narrowly.** Source background: old tests on shallow modules become waste once tests at the deepened interface exist. *(Source: DEEPENING.md §Testing strategy: replace, don't layer L32–37.)* Adoption keeps the current method's narrow condition: replace or remove old coverage only when the replacement demonstrably covers its accepted claim and deletion is already authorized. This is not an "always delete old unit tests" policy.

## Counterexample (authored; true failing case)

Scenario: an order module depends on an owned pricing service (remote but owned). Contract fixture: `GET /price?sku=X → 200 {"data":{"unit_price_cents":1200,"discount":null}}`.

The production adapter assumes a flat body (`body.unit_price_cents`); the real field is nested under `data`, so it reads `undefined`, prices the order at 0, and production gives the order away.

- Port-level tests are green: the in-memory adapter returns the correct domain object `{unitPriceCents: 1200, discount: null}`; the production parsing path never runs. This is the mislabeled surface.
- Correct test surface (task-local; no global integration gate): observe the production adapter against a local stub/recorded fixture covering nested/missing/null shapes and assert request + parsed output; or move normalization below the port and keep the adapter thin.
- Second variant, correctly attributed: the defect is in an in-process collaborator (order × inventory) that the test mocked as "as intended". Fix: use the real collaborator directly — not the same operation as substituting transport at a cross-network port.

## Conditions and exceptions

- Applies to design/test decisions at a dependency boundary; not to every unit test.
- `sometimes` for DB/file system: prefer a real substitute (test DB, temp dir) when available; state the choice and its coverage.
- Do not expose internal seams for tests; if a test must reach past the interface, suspect the module shape rather than exporting internals.

## Limits

- No new gate, validator, mandatory mock/port/DI, or test framework; no runtime claim.
- Does not change responsibility ownership or task authority; the Charter remains binding.

## Source anchors

| Source | Pin / path | Section |
| --- | --- | --- |
| mattpocock-skills | `c55ee460…`, `skills/engineering/tdd/mocking.md` | §When to Mock L3–14; §Designing for Mockability L16–59 |
| mattpocock-skills | `c55ee460…`, `skills/engineering/codebase-design/SKILL.md` | §Principles L62–65; §Designing for testability L69–80 |
| mattpocock-skills | `c55ee460…`, `skills/engineering/codebase-design/DEEPENING.md` | §Dependency categories L5–25; §Seam discipline L27–31; §Testing strategy L32–37 |
```

## 3 · `methods/README.md` 入口指向建议

在现有 "Task need | Method file | Judgment focus" 表之后，加一个 on-demand 小表（措辞建议）：

| Support need (on demand) | Guide file | Boundary |
| --- | --- | --- |
| Record or hand off evidence that may contain sensitive artifacts | `guide-redacted-evidence.md` | evidence custody and HITL split; no verdict/authority change |
| Choose a test double/adapter across a dependency boundary | `guide-mock-adapter-choice.md` | design/test-surface choice; no mandatory gate |

并加一句（建议）：

> These guides are on-demand references at demonstrated knowledge gaps; they add no applicability triggers, authority, or fixed phase chain. The task Charter still binds applicability, independence, and action permission.

现有 pin 表已含 matt / cursor 两个 pin，可复用；不新增来源仓库、不新增 Role。

## 4 · 边界与不主张

- 本预稿不修改 core、不产生 generator / validator / composer / gate，不新增或复活角色名。
- 不把审计记录（146 候选、183 行、R 标签、统计等）内联进方法入口或启动默认；预稿与 guide 都是按需材料。
- 实际 Charter 绑定仍为任务本地；方法/guide 不产生动作许可、风险接受或发布权限。
- 源与自拟区分：guide 内以 *(Source: …)* 与 *(Authored …)* 标注；示例整体为自拟，不因源表正确而自动正确。
- 运行时效果（脱敏是否被宿主执行、adapter 契约观察是否运行）未验证；本预稿不据此声称已可采纳。

## 5 · 残余

- 两份 guide 的行号为约数，最终以 future 复制后的文件为准；插入建议中的英文句子为目的语候选，可在编辑时本地化。
- 未读除三份固定源外的其他 TDD/测试材料；其覆盖不由本预稿声称。
- 采纳需独立编辑决定与接受记录；`methods/README.md` 变更属于集成动作，不在本轮执行。
