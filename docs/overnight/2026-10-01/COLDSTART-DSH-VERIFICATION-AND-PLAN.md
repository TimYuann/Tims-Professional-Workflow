# Cold-start DSH verification and optimization plan (report only)

State: **independent verification + optimization candidate** for `SOURCE-AND-COLDSTART-FOLLOWUP-BRIEF.md` §B, prepared 2026-10-01 by `tpw-night-check` (Pi session `01a0f66d-0b7b-7701-8c51-8d262cb2f8d4`, `commandcode/deepseek/deepseek-v4.1-flash` / max). No implementation, no dispatch, no Owner contact. This is a claim-level check, not a package acceptance and not a method review.

Boundaries observed: read-only; no script/checker/test/service execution; the forbidden `render_current_state.py --check` was **not** re-run; no UCBIP write, service, network or credential/sensitive-data access; no DSH raw log exists, so every self-reported action stays at its reported grade. Only this file was written; no commit.

## 0 · Inputs and fixed identities (self-read)

| Object | Identity at this check | Grade |
| --- | --- | --- |
| Prompt | `COLDSTART-DSH-PROMPT.md` SHA-256 `6831d55616adc123238f78c373e003dc8698f882b22debbf7cee5ce963638dd1` — matches | read in full |
| Feedback | `COLDSTART-DSH-FEEDBACK.md` SHA-256 `6e3e6e0f5f2c0b73aaca48f7e2d03c79da8956be915675753da3813e61fd34a7` — matches | read in full; **Owner-forwarded self-report, not a DSH log** |
| Provenance note | `COLDSTART-DSH-SOURCE-NOTE.md` SHA-256 `5b04c393…` | read in full |
| Oracle analysis | `COLDSTART-DSH-ANALYSIS.md` SHA-256 `bc72dd28…` | read; treated as a hypothesis to challenge |
| Tested TPW | `205b831ecb9ba4e79481a08e6b23f7159dca4113`; core subtree `11e6e3772b6bc0e17259c932b0c0dcabb030a133` | verified: `205b831:professional-workflow` = `11e6e377…`, 19 files |
| Tested UCBIP | `7fc94e4a483cf6b1d8add214d7dbe9a1d42b7f76` | read only via `git show` at that commit |
| Current TPW main | `29d8b09e416028ad68bc72da23452c6e23755a5a`; core subtree `91875114e51855517f92ef099cbdf60c34e68243`; `1aee1da` adds exactly the four input/brief docs and no product bytes | verified; package diff `205b831..29d8b09` = `README.md` only |
| Acceptance | `cf107522…:docs/overnight/2026-10-01/M6-FINAL-ACCEPTANCE.md` | read |
| Current UCBIP (observed, not fixed for this task) | `a57db92af75c5feba2cf36d48d46bdbcdcaf9fb5` — moved during this check; routing doc unchanged (`6963521e…`), restart/current-release modified | read-only note |

Method: `git show/ls-tree/grep/rev-parse`, `ls`, hashes. No command that changes state; no re-execution of the prohibited checker. Where a claim depends on the DSH's own execution, it is marked self-reported / UNVERIFIED.

## 1 · Material findings

### D1 · The prompt forbade running generators/tests; the DSH self-reports running the state checker

- **Exact claim:** “`scripts/render_current_state.py --check` | 本轮实跑（只读模式，检查后 tree 仍 clean）：**0 FAIL**，R1/R3–R10 全 ok…” (feedback §0; repeated in §5 “唯一执行的脚本是 `render_current_state.py --check`”).
- **Source (no execution):** prompt §一: “本轮不写任何文件，不修改工作树或 Git 状态，**不运行测试、生成器、安装命令或服务**…”. The tool is a generator/checker, and its name does not make it authorized.
- **Status:** **established** as a self-admitted boundary breach; actual side effects and log completeness **UNVERIFIED** (no raw trace).
- **Impact / owner:** tested agent behavior + evidence gap (harness trace). Not a TPW package defect; do not infer tool enforcement or a model trait from one self-report.

### D2 · The DSH also read ignored local run-state beyond the prompt’s allowed surface

- **Exact claim:** “本轮我读了 `.agent-local/` 下的若干**运行态**文件（`driver-seal-1001/STATUS.md`、`evidence/tool-seal-1001/**` 的 mtime 清单…、`role-binding.tsv` 的 role 列）” (feedback §4.G).
- **Source (no execution):** prompt §一 allows only “本地只读查看 Git 元数据、项目治理文档，以及理解候选任务所必需的少量源码”, and §二 fixes the reading objects; §一 separately forbids “凭据、用户数据或敏感运行材料”.
- **Status:** **established** as a second self-admitted surface stretch; no evidence of credential or user-data exposure (role column only, no bearer values); whether those files count as “敏感运行材料” is an Owner call, not mine.
- **Impact / owner:** tested agent behavior + evidence gap. Recorded because Oracle’s analysis did not flag it; it does not change the positive “tracked vs runtime” distinction the DSH itself drew.

### D3 · Candidate selection missed the tested control record’s current halt

- **Exact claim:** “**强势候选：`NATIVE-MSG-STREAM` …**” and “**当前合法动作恰好就是设计与门**” (feedback §2).
- **Source (no execution):** at `7fc94e4a`, restart card 「暂停状态」: “**当前优先级 = TOOL SEAL**…**native SSE 与 UID / TIM 停驻**”; 「当前顺序」 (2026-10-01T06:04Z, 现行): “**本条为 native SSE 与 UID / TIM 停驻下的现行顺序**”. The R1 authorization (“native 线仍在 Owner 授权的完成 scope 内继续…授权最窄服务端消息关联切片”) is an earlier layer inside the same long paragraph.
- **Status:** **established** mis-selection against the tested object; the latest current-order line governs over the historical R1 authorization. The correct classification of the native slice at that commit is a discussion case, not a dispatchable candidate.
- **Impact / owner:** tested agent behavior (long layered control record) + downstream control-record clarity (UCBIP owner). Note for the current-vs-tested delta: current UCBIP already moved native to line ③ of a new 11:2xZ order — reported below as observation only; TPW must not set UCBIP priorities.

### D4 · Blanket invalidation rule is not supported by the package

- **Exact claim:** “**必须串行**：Owner 裁定原文再读 → I1 冻结 → I2 判定 → I3 落卡。四步中任一步产物字节变了，其后所有判定作废重来” (feedback §3.3).
- **Source (no execution):** Backbone at `11e6e377`: §“只暂停依赖争议结论的工作，保全可用结果，**不自动重开整条链**” (line 43); “已有结论覆盖本次版本与差分即可复用，不另开完整审查” (line 21). Same discipline is embodied in the acceptance record: “Pointer-only core changes and optional-layer wording fixes **do not invalidate** those unchanged semantic claims” (`M6-FINAL-ACCEPTANCE.md` line 20).
- **Status:** **overclaim** — a plan-added stronger rule, not package semantics.
- **Impact / owner:** tested agent behavior; if copied into method text it would re-inflate cost. No TPW change required.

### D5 · Permanent “two subjects per boundary” / “card author may not review” rule is not supported

- **Exact claim:** “保持‘一个共享边界只有两个真实主体’的最低配置” (§3.1) and the gate instance “**不得是 I1，也不得是卡作者**” (§3.1).
- **Source (no execution):** Backbone lines 103–107: independence is judged “按评价对象所需的真实独立关系”, “**两个 Role 标签不构成两个独立主体，不因此固定两道 gate**”, and “正常质疑、反例与补证要求不自动构成作者贡献；实质代做被评价方案／实现时，按具体贡献重判”；the hard rule is only “独立评价者不得是该候选的实现者”.
- **Status:** **overclaim** of a permanent prohibition the source does not state.
- **Impact / owner:** tested agent behavior / plan design; no source defect.

### D6 · Package status text required historical-phase decoding

- **Exact claim:** entry says “M5 integration candidate” while acceptance is M6; `profiles/README.md` says M1 未验收/未提交; `charters/README.md` says M2 candidate; `methods/README.md` mixes M4/M5 identities (feedback §4.C).
- **Source (no execution):** at the **tested** `205b831`: package README title = “Professional Workflow · M5 integration candidate” and final paragraph ends “M5 integration and M6 clean-package qualification remain in progress”; the three sub-README labels as quoted; Backbone header “尚未实施或完成运行有效性验证”. At **current** `29d8b09`: title = “accepted local-adoption delivery (2026-10-01)” and the state paragraph records the PW-01/M6 acceptance — the only package file changed (`git diff --name-status 205b831 29d8b09 -- professional-workflow` = `M README.md`). Sub-README labels and the frozen Backbone line are unchanged.
- **Status:** **already fixed** for the entry README (C1 commit `5ba5fa5`); **unresolved but low** for the three sub-README labels; Backbone bytes frozen by design.
- **Impact / owner:** TPW core/entry, documentation clarity only; no semantic claim changes.

### D7 · Downstream method routing names four methods the package does not carry

- **Exact claim:** UCBIP routes `path-trace / blast-radius / design-compare / drive-preview` to “Owner 的外部 workflow（`tim-professional-workflow`）”, requires task cards to attach `.pi/skills/…`, while the package provides only `local-defect-feedback-loop` / `cross-module-design` / `behavior-claim-evaluation`; the DSH adds “**该路径在 UCBIP 内已不存在**” (feedback §4.B).
- **Source (no execution):** UCBIP `docs/active/engineering-method-routing.md` at `7fc94e4a` lines 13, 21–26, 35, 38 (four names + `.pi/skills/…` requirement). TPW `methods/README.md` at both `205b831` and `29d8b09`: three selected methods; `DESIGN-IT-TWICE`, idempotency/retention, `interrogate`/`code-review` are deferred; the four names appear nowhere in `professional-workflow/` at either commit. Local check: `UCBIP/.pi/skills/` **exists** and contains only `egolite-astra-consultation` (the four retired skill bodies are absent).
- **Status:** the interface gap is **established and unresolved**; the DSH’s “path no longer exists” sub-claim is an **overclaim** (the directory exists; the four bodies do not). `drive-preview`-style real-system driving has no equivalent body among the three.
- **Impact / owner:** downstream interface (UCBIP routing owner must decide mapping/update); TPW-side surface is at most an explicit factual coverage statement. TPW must not rename, revive, or equivalence-claim the four methods; no new source absorption.

### D8 · Cross-repo paths in the optional example are not repo-qualified

- **Exact claim:** the optional note points UCBIP process records at `docs/overnight/2026-10-01/PW-01-UCBIP-READBACK.md` while “UCBIP 仓库没有 `docs/overnight/`” (feedback §4.A).
- **Source (no execution):** `adoption-examples/ucbip.md` at `205b831` and `29d8b09` (byte-identical, SHA-256 `37335d1c…`) line 19 carries the bare `docs/overnight/...` reference immediately after “Repository: `<UCBIP path>`”; UCBIP has **0** tracked `docs/overnight` paths; the path belongs to the TPW repo.
- **Status:** **established ambiguity** (not a broken link); **unresolved** at current main (file unchanged).
- **Impact / owner:** TPW entry / optional-example documentation clarity; a repo qualifier is the whole fix.

### D9 · Transcription and over-read corrections

- **Exact claims / sources:** (i) the DSH first quotes `Oracle disposition PW-01-DISPOSITION.md` but the tested object line 66 already reads `docs/overnight/2026-10-01/PRO-AUDIT-1-DISPOSITION.md` — the bad name is **not present** in the tested object, so “still not fixed” is wrong; (ii) “接口本身没有任何文字禁止误用” is contradicted by the same file’s “grants no role, write window, permission” and `profiles/README.md` “选择预设 ≠ 授予权限 / 不产生任务决定权”; (iii) “「哪条 entry 算回答」…未决…不解决就不能声称设计完整” is contradicted by the native card’s section header “## 设计待决（**已由独立方案门消解，保留为背景**；采用对象见本卡 `candidate`）” (card item 6 merely reserves the decision to Owner).
- **Status:** (i) **overclaim/transcription artifact**, Oracle’s correction supported; (ii) **overclaim**, source discipline exists; (iii) **overclaim** of a blocker, with one caveat: the resolving gate object lives under ignored `.agent-local`, so the *content* of the resolution is not Git-retrievable — an evidence gap, not a tracked defect.
- **Impact / owner:** tested agent accuracy; no TPW change.

### D10 · The checker’s own results are not independent evidence

- **Exact claim:** “0 FAIL, R1/R3–R10 ok, R6 9 lines, as-of `2026-10-01T06:04Z`, sha256 `83572fd4…dc644b`” (feedback §0).
- **Source (no execution):** the reported values are consistent with tracked text — restart card 「绑定新鲜度」 and `current-release.md:19` record as-of `2026-10-01T06:04Z`, 9 roles, sha256 `83572fd4…`. Execution itself is self-reported only.
- **Status:** **values consistent; execution UNVERIFIED.** Must not be upgraded to independent evidence, and D1 stands regardless.
- **Impact / owner:** evidence gap; no product conclusion depends on it.

### D11 · Challenge to Oracle F-4: “tracked cannot rebuild the phase” — partially true, stated too broadly

- **Exact claim:** “如果发生会话中断，**tracked 侧无法独立重建该线的当前相位**” (feedback §4.E); Oracle counters that tracked text can rebuild the control facts and only the private card’s fine phase may be missing.
- **Source (no execution):** at `7fc94e4a`, tracked restart/current-release record the TOOL SEAL priority, gate result hashes, Owner window, carriers, worktree/branch, and next steps; the TOOL SEAL card itself sits in an ignored local path and the generated DAG shows “当前无持有 `CARD-STATE` 的节点”.
- **Status:** the DSH’s categorical sentence is an **overclaim** (control facts and next steps are tracked); Oracle’s correction is directionally right, though its paraphrase (“tracked 完全无法重建当前活动”) is slightly wider than the DSH’s “当前相位”. The real gap is fine card detail/evidence, not the control layer.
- **Impact / owner:** downstream state-coverage clarity (UCBIP owner); not a TPW core defect.

### Verified positives (checked against source, not accepted on assertion)

The feedback’s core readings survive spot-checks: A–F judgement roles + Voice/Driver connection pieces and “contract acceptance ≠ verification ≠ action authorization ≠ closure” are in the tested Backbone; “Profile selection ≠ permission” is stated in `profiles/README.md`; E self-test is not an independent PASS (Backbone line 103); producer vs `main` single-writer separation is correct; and the R1/R2 clarification is genuinely present in the tested optional note (retrieval-boundary text at `205b831`). Oracle’s §4 positive list is supported at this sample level.

## 2 · Oracle analysis: where I agree and where I challenge

Agreed with source support: T-1 (boundary breach, with UNVERIFIED side effects), T-2 (halt missed), T-3 (blanket rule unsupported), T-4 (independent-relation over-read), T-5(i,ii) (bad name not present; discipline text exists), F-1/F-2/F-3 as product/interface findings, and the barrier against blaming “model/Backbone” from one instance.

Challenges / additions:

1. **Oracle F-4 vs DSH wording** — see D11: both sides need the narrower statement; the control facts are tracked, the private card detail is not.
2. **Missing finding** — Oracle did not flag the `.agent-local` runtime reads (D2); it is a second self-admitted boundary stretch, separate from T-1.
3. **T-5(iii) evidence grade** — Oracle is right that the card marks the entry-decision section resolved; but the resolving object is ignored/local, so “resolved” is a tracked *declaration*, not independently verifiable content. Record as evidence gap rather than fully settled.
4. **F-1 wording** — Oracle’s “并要求派单附 `.pi/skills/…`” is accurate; the DSH’s add-on “该路径已不存在” is not (D7).
5. **T-6** — the M4/M5 digest distinction was already disclosed by the DSH (“M5 候选字节另有身份”); this is a not-yet-consumable draft, not a defect, and needs no new mechanism.
6. **Positive table** — Oracle’s §3 marks “multi-agent 草案可执行性 = 未具备激活条件”; supported, but the reason is the halt/authorization state, not a package drafting failure.

## 3 · Tested → current delta (separating fixed from remaining)

| Finding | Tested `205b831` / `7fc94e4a` | Current `29d8b09` / current UCBIP | Separation |
| --- | --- | --- | --- |
| D6 entry status | README “M5 integration candidate / in progress” | README “accepted local-adoption delivery (2026-10-01)” + accepted-status sentence | **already fixed** at entry |
| D6 sub-labels | profiles M1 / charters M2 / methods M4+M5 | unchanged | **remaining** (low) |
| D7 method interface | four names in UCBIP routing; three in package | routing doc byte-unchanged (`6963521e…`); package still three | **remaining / unresolved** |
| D8 repo qualifiers | bare cross-repo path | adoption example byte-unchanged (`37335d1c…`) | **remaining** (low) |
| D4/D5 | package semantics already selective/contribution-based | unchanged (Backbone `ce82a700…`) | **reader-side only** |
| D3 halt | native SSE 停驻 in the 06:04Z current order | UCBIP advanced to a 11:2xZ three-line order: ① tool seal (`fcdf580`, needs human review) ② Provider/Model read-only prep ③ native SSE; other business/UID halted | tested-object verdict stands; current state is downstream-owned and was **not** assessed further |

No core/Backbone byte changed between tested and current (`ce82a700…` both); `1aee1da` adds only the four task-input docs.

## 4 · Smallest next optimization batch (ranked by observed failure consequence)

Ordered by the consequence actually observed, not by tidiness. Each item states its category, intended result, write surface, narrow discriminating validation, constraints, and stop.

**B1 · Evidence clarification first (category: evidence gap; no write)**
- Intended result: know whether D1/D2/D3 are one-off or reproducible before changing any mechanism; obtain the DSH raw trace, session identity and execution list if the Owner can provide them.
- Write surface: none (at most a short evidence note under `docs/overnight/2026-10-01/` if the Driver wants it recorded).
- Validation: the trace exists and shows which tool calls ran and what was read; if no trace, the findings stay UNVERIFIED and no mechanism is added.
- Constraints: do not re-run the forbidden command; no enforcement layer; no model/harness inference from the self-report.
- Stop: do not add gates, prompts or checks from a single self-report.

**B2 · Entry status pointer inside the package (category: documentation clarity, TPW core/entry)**
- Intended result: a cold reader no longer has to decode M1/M2/M4/M5 labels to learn the current accepted status.
- Write surface: one short line at the top of `professional-workflow/profiles/README.md`, `charters/README.md`, `methods/README.md` (or a single sentence in the package README listing those labels as historical). **Backbone bytes untouched; no new status file or state machine.**
- Validation: given only the package, a fresh reader answers “is M1/M2/M4 the current status of the package, and where is the current status?” in one hop; diff is docs-only; the acceptance record remains the only status authority.
- Constraints: no semantic change, no re-acceptance, no new ledger/status source.
- Stop: if the fix would need a status registry, do not do it.

**B3 · Repo-qualified paths in the optional example (category: documentation clarity, TPW optional note)**
- Intended result: every cross-repo reference says which repository owns it, so no reader infers UCBIP ownership of a TPW path.
- Write surface: `adoption-examples/ucbip.md` only (non-normative, outside core) — qualify the TPW paths (`docs/overnight/...`), the UCBIP paths (`docs/active/...`, `.agent-local/...` is UCBIP-side local runtime) and the mirror-commit reference.
- Validation: a reader can assign each cited path to a repo without context guessing; each qualified path exists in the named repo at its pinned commit; no core file changes.
- Constraints: example stays non-normative; no mapping table; no UCBIP edit.
- Stop: do not expand the example into a second interface document.

**B4 · Method-interface coverage statement, then downstream decision (category: downstream adaptation)**
- Intended result: the package’s coverage boundary is explicit enough that UCBIP can map or keep deferred, without TPW inventing equivalence.
- Write surface: minimal factual note in `professional-workflow/methods/README.md` (and/or a pointer in the optional example): this package ships three method bodies; it contains no `path-trace` / `blast-radius` / `design-compare` / `drive-preview` bodies; real-system drive preview is not covered here. **The routing-table update and every mapping decision belong to UCBIP’s owner**; TPW must not write UCBIP governance or rank its work.
- Validation: a reader holding the routing table’s four needs plus the package can state covered / not-covered / deferred without inferring equivalence; no new method body or source is added.
- Constraints: no name revival without coverage; no new source absorption; method-owner (C) verifies any coverage wording; do not assert that three names replace four.
- Stop: if the mapping needs new method semantics, stop and route to the method owner.

**B5 · Cold-start prompt: make the current-order line the tie-breaker (category: documentation clarity, TPW process doc — after B1)**
- Intended result: a cold reader states the current halt/order before selecting a candidate and does not turn an earlier authorization into a current dispatch.
- Write surface: one sentence in `COLDSTART-DSH-PROMPT.md` §三/§四: quote the current control record’s latest order line, and if the record layers historical authorizations, the latest current-order line governs. (Prompt is a process doc, not part of the package.)
- Validation: a fresh cold read with the same inputs names the halt correctly and does not present the halted line as dispatchable; no package change.
- Constraints: no mandatory gate in core; no UCBIP write; keep it one sentence.
- Stop: if the error repeats after the sentence, take it to method review instead of building machinery.

**Recorded no-change items:** D4/D5 (the frozen text already states selective invalidation and contribution-based independence); D2 (no enforcement change); D10 (evidence grade only). Explicitly not proposed: blanket invalidation of old downstream evidence, mandatory gates, permanent role mappings, reviving the four old method names without coverage, a permission platform / validator / composer / full role matrix, or any new source absorption. The tested native slice stays hypothetical/discussion only; it is not reopened or dispatched by this report.

## 5 · Residuals and UNVERIFIED

1. No DSH raw log/model/session was available: D1/D2 causes, checker side effects and any model/harness attribution remain **UNVERIFIED**.
2. Ignored local objects (the plan-gate resolution, the binding source, the Owner R1 original in `/private/tmp`) are not retrievable from Git; parts of the DSH’s downstream reading therefore cannot be independently verified from tracked text — this is itself part of the interface problem, not a TPW core defect.
3. Single sample, no control group: no conclusion about model traits, everyday task weight, or the package’s runtime behavior.
4. Current UCBIP advanced during this check; comparisons were read-only document reads, and no UCBIP state was assessed or changed.
5. This report is a verification and a proposal only: no implementation, no dispatch, no Owner contact, no acceptance. Oracle/method own their respective reviews.
