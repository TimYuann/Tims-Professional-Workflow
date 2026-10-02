# READER-PROFESSIONAL-USE · 轻量专业使用观察（同一 reader2 会话 · continuation）

读者序列状态：同一 reader2 读者，第 2 次观察（第 1 次为 `0e2bc4ba` 的接入案例）。本轮不是第二次 fresh；两轮观察一起构成同一读者的序列观察。
读取纪律：只读 fixed 对象（`git -C .worktrees/night-2026-10-01 show f76a5955…:professional-workflow/<path>`）；未读 mutable 工作区、未执行代码/网络/Provider 操作。本报告只写实际读到或找不到的内容，不含运行结果。

## 0. 消费定位

- commit：`f76a5955a89e4d703f66c120a90ab2b37901b7f2`（`cat-file -t` = commit）
- core 子树：`professional-workflow/`，tree `01514a3918dbf5a08d47b2f8e046c30e6ee0ee82`（与任务给定一致），共 57 个文件
- 序列观察（对第 1 轮消费对象 `0e2bc4ba` 的 diff）：core 从 51 文件 → 57 文件；增补集合包括 `methods/interface-contract-and-retry.md`、`methods/trust-boundary-and-actions.md`、`methods/release-and-recovery.md`、`methods/performance-and-neutrality.md`、`methods/deprecation-and-migration.md`、`methods/external-tool-operation.md`，以及 `domain-state-and-invariants.md` 修订；`charters/README.md` 新增「Shortest startup path」六项；`charters/template.md` 的 Accepted inputs 增加「the current facts/assumptions/unknowns this run relies on」；`README.md`、`ADOPTION.md`、`profiles/*` 两轮之间未变（`git diff --stat` 观察）。

## 1. 情境（按给定事实与约束复述，不补预期）

事实：一个服务仓的适配层重构后——

- 逻辑层用内存替身测试全绿；
- 生产 transport/序列化适配器的请求构造（request construction）与响应解析（response parsing）已改；
- 没有真实 Provider 可用；
- 任务授权只允许本地测试运行；
- 目标：判断这次变更能否算已验证、需要什么最小证据、交付什么、何时把问题召回给谁。

我的读法：这本质是 F 的 evidence evaluation，而不是 E 的实现任务；「全绿」发生在替身层，被改的却是生产适配器层，两者覆盖不同（文本依据见 §5 动作 2–3）。

## 2. 选定的 Profile

**`professional-workflow/profiles/evidence-evaluation.md`（F · 证据与验证）。**

依据（该文件原文）：

- 一句话：「对明确对象、版本与覆盖给出证据判断；不因 PASS 授予关闭或发布许可。」
- 心智模型：「三态只有 PASS / FAIL / UNVERIFIED；环境故障记 UNVERIFIED，不算 PASS，也不判为产品缺陷」；「证据针对明确的对象与版本；测试通过不证明目标价值已实现」。
- 关键问题：「被评价的确切对象、版本与 claim 是什么？覆盖到哪里，没覆盖什么？」「什么观察能把"成立"与"不成立"分开？关键负控制是什么？」
- 常见误区：「只验证"能跑通"，不设计能揭示错误的负控制」「把文档、字段非空、自测输出当作已验证结论」——正对本案的「替身全绿」风险。

不选 `implementation.md` 作为主 Profile 的原因（同读该文件）：E 的心智模型说「把自测变绿当作正确依据，或自己给出结论断言（结论由具独立性的 F 给）」；本次要的是对已发生变更做证据判断，不是把结果做出来。若后续需要在本地补最小证据（动作 4），其动作仍由 Charter 授权决定，而不是靠 E 的 Profile 名。

## 3. Charter 填写（遵照 `charters/template.md` 字段；未给定的写占位并标注）

- **State:** candidate（本次没有真实接受记录，按模板字面填候选）。
- **Profile:** `professional-workflow/profiles/evidence-evaluation.md`
- **Instance:** `<reader2-professional-use-2026-10-02>`（占位，非真实会话名）
- **Task / outcome:** 对「适配层重构后，本次变更是否已验证」给出 F 结论，并设计达成判断所需的最小证据；范围＝被改的 transport/序列化适配器 + 逻辑层 claim；非目标＝不改产品代码、不调真实 Provider、不做发布/部署判断。
- **Delegation source:** 「任务授权只允许本地测试运行」是给定约束；**谁委托、谁是决定人未给定**。按模板字面：「if absent, no authority is implied」。本报告只能把它作为占位；真实开工需要补真实委托对象。
- **Object scope:** 待固定的变更 diff/commit（未给定具体对象，占位）；允许 inspect：适配层代码、现有测试、契约/fixture（若有）；不得改变的对象：未授权前默认不改生产代码（「Do not turn the initial expected file set into a permission list unless an authority explicitly made it a boundary」——charters/README Rules）。
- **Accepted inputs:** 需要「被接受的接口/行为契约 + 版本 + 决定人 + 当前事实/假设/未知项」（模板字段原文要求 current facts/assumptions/unknowns）。**本案未给定契约来源**，因此此项只能留占位——这也直接决定 §5 动作 4 能否成立。
- **Applicable methods:** 见 §4 绑定清单（6 个 accepted/on-demand 文件路径；candidate 文件未绑定，理由见 §4）。
- **Responsibility:** F 对固定对象/版本评价 claim，并给出三态结论、覆盖与限制；不授予关闭或发布许可（profile 一句话）。
- **Delegated decisions:** 验证设计内的选择（用哪种本地 stub/fixture 形状、断言什么、捕捉什么证据）；不含：真实 Provider 访问、生产代码改动、发布/部署动作。
- **Preserve / do not do:** 不改生产代码（未授权）；不发起真实 Provider/SDK/wire 交互；不把 self-check 说成独立评价；不把 UNVERIFIED 说成 FAIL 或 PASS；证据先按 `guide-redacted-evidence.md` 处理。
- **Tools and actions:** 允许本地测试运行；网络/Provider/外部写入未授权（「tool access alone is not permission」）。
- **Deliver:** F 报告（对象/版本、claim、命令与输入、观察、覆盖与限制、三态、独立性声明）+ 最小证据工件（本地 contract-mapping 测试/脚本 + redacted 证据）。
- **Independence:** **未给定**。模板要求「State who authored, challenges, and evaluates」；若 F 就是本次变更作者，则不独立（`change-review.md`：「A review the author ran on their own change is labeled a self-check … does not become independent F evidence」）。
- **Recall:** 见 §7。
- **Acceptance / verification / action / closure:** 四者分开（模板要求「do not infer one from another」）；**接受人/关闭依据未给定**——F 的 PASS 本身不等于接受、更不等于发布许可。

## 4. 绑定的方法文件（真实路径 + 状态 + 依据）

本轮实际读过的相关方法全文及绑定决定：

| 路径 | 文件自标状态 | 是否绑定 | 绑定理由 |
| --- | --- | --- | --- |
| `professional-workflow/methods/behavior-claim-evaluation.md` | M4 accepted reference | **是** | 三态结论与 real-leg 边界的主方法 |
| `professional-workflow/methods/guide-mock-adapter-choice.md` | accepted bounded reference (2026-10-02) | **是** | Rule 3 直接覆盖「替身替换了哪些路径」 |
| `professional-workflow/methods/guide-test-evidence-quality.md` | on-demand guide（methods/README 标注 gate-reviewed、byte-passed integrated） | **是** | 检查「全绿」本身是否有意义 |
| `professional-workflow/methods/verification-harness-design.md` | on-demand method (MG-5)；Charter decides applicability | **是** | 定义需要 real leg 的 claim、以及 drive 不成立时的处理 |
| `professional-workflow/methods/change-review.md` | on-demand method (MG-6)；Charter decides applicability | **是** | 固定对象/意图、Verification lens、证据缺陷与产品缺陷分开 |
| `professional-workflow/methods/guide-redacted-evidence.md` | accepted bounded reference (2026-10-02) | **是** | 证据保管纪律（behavior-claim-evaluation §Method 2 指到它） |
| `professional-workflow/methods/interface-contract-and-retry.md` | **candidate**（「not yet an accepted reference; creates no authority, trigger, or gate. A fixed-diff review still applies.」） | 否 | 内容与请求构造/响应解析契约相关，但状态未接受；不作为判断依据 |
| `professional-workflow/methods/trust-boundary-and-actions.md` | **candidate**（同上） | 否 | 与「本地测试授权/Provider 集成 Action Class」相关，但未接受；授权判断改为直接写 Charter 字段 |
| `professional-workflow/methods/release-and-recovery.md`、`performance-and-neutrality.md`、`deprecation-and-migration.md`、`external-tool-operation.md`、`domain-state-and-invariants.md` | 本轮新增/修订，未逐一读全文 | 否 | 与本案 claim 不相关，未读不绑 |

**序列观察（如实记录，不下判断）：** `interface-contract-and-retry.md` 与 `trust-boundary-and-actions.md` 已被 `methods/README.md` 的 absorption batch 表列为 integrated 条目，但文件自身仍写 candidate 状态与固定的 review 要求。两份文本对同一文件的「已整合」与「未接受」表述并存；本次只作观察，未据此绑定。

## 5. 动作序列：依哪段方法 → 做什么 → 交什么

### 动作 1 · 固定对象与 claim 拆分

- 依据：`change-review.md` §Fixed object and intent——「Pin the object before reviewing. The fixed point (commit/branch/tag/merge-base) must be supplied; if it is not, ask rather than guessing.」；「State the intent from an applicable accepted basis … If no spec is available, record "no spec available" rather than inventing requirements.」`behavior-claim-evaluation.md` §Method 第 1 条：「State one falsifiable claim and its conditions, measure and threshold. Name the exact object and version.」
- 做什么：取得变更的固定 commit/diff 与被接受的适配层契约；把「这次变更算已验证」拆成可证伪 claim：
  - C1 逻辑层在受控输入下的行为（内存替身已观察到的部分）；
  - C2 生产适配器的请求构造（字段编码、参数形状）；
  - C3 生产适配器的响应解析（嵌套/missing/null/错误体等形状）；
  - C4 真实 Provider/SDK/wire/部署行为。
- 交什么：claim 清单 + 固定对象/版本 + 意图来源；无 spec 就写「no spec available」（change-review 原文）。

### 动作 2 · 检查现有「全绿」的证据质量

- 依据：`guide-test-evidence-quality.md` §Use——「It checks whether a green result is meaningful evidence. It does not decide the product verdict」；§Oracle——期望值须来自独立来源（known-good literal / worked example / accepted spec / prior art），「Recomputing the expectation with the same formula or logic as the implementation makes the check agree with the implementation's own mistake.」；§Signal 的五类省略；§Evidence defect vs product verdict——「an unusable green is an evidence problem — UNVERIFIED at best; it is not by itself a product FAIL.」`behavior-claim-evaluation.md` §Method 第 4 条后段：test/suite 的质量检查由该 guide 承担，comparison 方法不扩张成 suite review。
- 做什么：对现有替身测试检查 oracle 来源、耦合、弱断言；明确指出缺陷（哪个 check 验的是什么、漏的是什么），而不是只给「invalid」的结论。
- 交什么：C1 的证据质量说明（可支持/不可支持，及具体缺陷）。

### 动作 3 · 判断替换了哪一层（覆盖边界）

- 依据：`guide-mock-adapter-choice.md` Rule 3 全文——「A double exercises only what the test actually calls: if the test double directly returns a ready domain object, the replaced adapter's request construction, transport and response mapping are not executed. If the risk or claim is in that adapter or its mapping, observe the adapter at its own surface … Or state which real normalization function runs under which test: moving logic into an adapter that the test double still replaces does not change coverage. Record the uncovered part.」；§Counterexample（订单定价：port 级测试全绿，生产解析读 `undefined`，把订单价格算成 0——「This is the mislabeled surface.」）。
- 做什么：确认内存替身处于哪个 seam；若测试直接拿到现成领域对象，则 C2/C3 未被任何现有证据覆盖。
- 交什么：未覆盖部分记录（Rule 3 末句要求）；对 C2/C3 的现状判定（在补证据前 = UNVERIFIED）。

### 动作 4 · 设计最小证据

- 依据：
  - `guide-mock-adapter-choice.md` Rule 3 的替代路径——「observe the adapter at its own surface — a local stub or recorded fixture is one option for contract mapping … needs an appropriate real leg under the task's existing authorization (a green substitute does not establish it, and this guide does not require a real leg for every task).」
  - 同文件 §Counterexample 的 Correct test surface——「observe the production adapter against a local stub/recorded fixture covering nested/missing/null shapes and assert request + parsed output, with the mapping path actually invoked」。
  - `verification-harness-design.md` §Use——「A real leg is required only for the claims that need one, and the harness scope follows the delegation」；§Recipe 的 Evidence 标准——「exercise the real user path, not internal setters or test-only endpoints; capture the action and the resulting state … verify side effects … substitute/mock only where a production boundary already isolates the external system.」；§Prove and limits——「A harness that was never executed is a draft, not a deliverable.」；§Cleanup and evidence——「Fixing a broken base, generating scaffolding … requires existing action authorization; a broken environment is recorded UNVERIFIED rather than absorbed into the claim.」
  - `behavior-claim-evaluation.md` §Method 第 2–4 条——同命令/数据/环境保持 baseline 与 treatment，保留下原始输出（signal-bearing、redacted），报告 exact command and inputs、observed result、coverage and limitations。
- 做什么（本地授权内）：用 contract fixture/local stub 驱动生产适配器的 request construction + response parsing，覆盖嵌套/missing/null/错误形状，断言请求与解析输出，并确认 mapping 路径真的被执行；记录命令与观察。若需要真实 app/service 或真实 Provider 才能驱动 → 超出当前授权/环境，停（进入 §7 召回）。
- 交什么：最小证据工件 + 运行记录（redacted）；每条结论携带 claim 与对象版本、实际执行了什么、覆盖范围与限制。

### 动作 5 · 证据保管

- 依据：`guide-redacted-evidence.md` Rule 1——「Redact before show/record/store. Replace every secret with `<REDACTED>`」；Rule 2——在现存授权内 collect or reuse minimal necessary evidence；Rule 3——sensitive artifact 默认只保留 minimal inline evidence；`behavior-claim-evaluation.md` §Method 第 2 条——「apply `guide-redacted-evidence.md` before storing or sharing」。
- 做什么：捕获的请求/响应样例只保留信号行；凭据留在环境变量；需要落盘原件的走 Rule 4 单独边界。
- 交什么：可被另一会话重放的、已 redact 的证据材料。

### 动作 6 · F 结论

- 依据：`behavior-claim-evaluation.md` §Verdict mapping——PASS/FAIL/UNVERIFIED 的定义；`profiles/evidence-evaluation.md` 心智模型与常见误区；`change-review.md` §Finding evidence and impact 的「Evidence defect vs product defect」及 Limits——「a self-check by the author is recorded as a self-check rather than upgraded to independent review」。
- 做什么：逐 claim 给三态；证据缺陷与产品缺陷分开；列明独立性与覆盖限制。
- 交什么：F 报告。

### 动作 7 · 召回/升级

见 §7。

## 6. 证据是否足够（基于给定事实的文本推演，非运行结果）

- **C1（逻辑层，受控输入）**：够不够取决于动作 2 的结果；文本不允许仅凭「全绿」下结论（`guide-test-evidence-quality.md` §Oracle/§Signal）。若 oracle 独立、断言针对行为，则该范围内的绿色可作证据；具体结论需要真实测试内容的检查，本报告无从判断。
- **C2/C3（生产适配器请求构造/响应解析）**：**现有证据不足**。`guide-mock-adapter-choice.md` Rule 3 的覆盖边界意味着，若替身直接返回领域对象，这两条路径没有被执行过；在补齐本地 contract fixture 证据之前，这两条 claim 是 UNVERIFIED。
- **C4（真实 Provider/SDK/wire/部署）**：**在现有授权内无法建立**。`behavior-claim-evaluation.md` §Use：「when the claim is about a real Provider, an actual SDK, wire behavior, deployment or end-user experience, an appropriate real leg is required under the task's existing policy and Charter authorization — a cheaper substitute's green result does not establish such a claim」；「If the needed real evidence lies beyond the existing authorization or boundary, use the task's recall path instead of self-granting access.」保持 UNVERIFIED。
- **不是 FAIL**：FAIL 需要「a valid comparison provides a counterexample, shows no required change, or misses the stated threshold」（§Verdict mapping）或有效反例；「全绿但覆盖不到」是证据问题，不是产品故障（`guide-test-evidence-quality.md` §Evidence defect vs product verdict；`change-review.md` 同义段）。
- **独立性未给定**：F 若为作者，结论只能标注 self-check，不构成独立 F 证据（`change-review.md`；`profiles/evidence-evaluation.md` 心智模型「评价者不得是被评价候选的实现者」）。
- **最小证据可达范围**：本地 fixture 级证据可把 C2/C3 从 UNVERIFIED 推进到 PASS/FAIL；C4 在无真实 leg 前保持 UNVERIFIED。这个「最小」是 claim-scoped 的，不是全量回归或全面集成 gate（`verification-harness-design.md` §Limits；`guide-mock-adapter-choice.md` Limits）。

## 7. 召回/升级路径（触发条件 → 去向）

依据：`charters/template.md` Recall 字段——「send Driver the affected object, fact, and impact. Driver routes to the authority that owns the affected boundary; Voice is used only for a human-reserved decision or human acceptance.」；`charters/README.md` Rules——「A changed or missing dependency goes to the authority that owns the affected decision. Use Voice only when a human-reserved decision or human acceptance is involved.」；`profiles/evidence-evaluation.md` §交接与召回——「实现违反约定返回 E；依据冲突或缺失返回 B/C/D；目标解释失准返回 A；环境阻断记录 UNVERIFIED 并说明」。

- **需要真实 Provider/SDK/wire 观察，而授权只允许本地测试运行** → 不自授访问（`behavior-claim-evaluation.md` §Use 明文；`guide-mock-adapter-choice.md` Rule 3「needs an appropriate real leg under the task's existing authorization」）；记录受影响对象、事实、影响，经 Driver 路由到拥有该授权/测试环境的责任方；涉及 human-reserved 决定时经 Voice。
- **适配器契约（输入/输出形状、错误语义）缺失、矛盾或未接受** → 回 B/C（`profiles/evidence-evaluation.md` 召回节）；在缺契约时 fixture 本身没有接受的依据，验证无法开始（`change-review.md`「no spec available」同理：不发明要求）。
- **实现违反已接受约定** → 返回 E。
- **评测者不独立（F 即作者）** → 交真实委托决定：换独立 evaluator 或把结论降为 self-check（`change-review.md` Limits）。
- **升级**：若包版本升级，按 `ADOPTION.md` §4 的固定对象 diff 与重核纪律处理（本轮 commit 变更即一次序列示例，但本轮未执行升级动作）。

## 8. 文本未规定 / 只能推测 / 需真实运行或授权才能回答

- **真实对象与版本**：变更的 commit/diff、适配器代码、现有测试内容——情境未给。我未运行任何东西，无法核对 C1–C4 的真实状态。
- **委托与接受关系**：谁委托、谁验收、F 的独立性——未给。本报告按模板占位；模板明文「if absent, no authority is implied」。
- **「只允许本地测试运行」是否覆盖新增测试文件/证据脚本**：文本没有规定动作分类到这个粒度。我可以确定的是：真实 Provider 调用未授权；改生产代码未授权。写测试/夹具是否在授权内，需要真实授权澄清（`charters/README.md`：「Do not turn the initial expected file set into a permission list unless an authority explicitly made it a boundary」，反向亦然——没人明确授权时不应假定）。
- **替身的具体接缝**：内存替身是 port 级 substitute 还是直接返回现成领域对象——情境未说明，这直接改变 C2/C3 的覆盖判断（`guide-mock-adapter-choice.md` Rule 3 是有条件的）。我只能给出两种接缝下的判断路径，不能给出最终结论。
- **契约/fixture 的形状来源**：无真实 Provider 时，fixture 必须来自某份被接受的契约或录制产物；本案未给定契约。形状从哪来、谁接受它，是真实运行/授权才能回答的问题。
- **C4 是否必须**：取决于接受方对 claim 的定义——文本给出的是 claim-scoped 判定（真实 Provider/SDK/wire/部署的 claim 才需要 real leg），而非「一切任务都要真实 Provider」（`behavior-claim-evaluation.md` §Use；`verification-harness-design.md` §Use「A real leg is required only for the claims that need one」）。缩窄 claim 范围即可在本地授权内完成一部分验证，但这是任务方的选择，不是我能替之决定的。
- **两份 candidate 文件的可用性**：`interface-contract-and-retry.md` 与 `trust-boundary-and-actions.md` 已在整合表内、但文件自标 candidate 且标注固定的 review 要求——「已整合」与「未接受」并存（见 §4）。本案因此未把它们用作判断依据；若后续要依赖其内容，需要先解决这个状态问题（文本未规定由谁解决）。

## 9. 消费 commit

本报告消费 fixed 对象：commit `f76a5955a89e4d703f66c120a90ab2b37901b7f2`，core 子树 `professional-workflow/` = tree `01514a3918dbf5a08d47b2f8e046c30e6ee0ee82`；序列上一轮消费 `0e2bc4ba72ab8825b84e0e455de9ae5a2df26fe9`（同为 `professional-workflow/`）。报告内所有引用均来自上述对象内文件；未使用 mutable 工作区内容，未执行任何代码、网络或 Provider 操作。

**文本可消费观察，非运行效果。**

## Correction (one feedback round, original retained as history)

本节为 reader2 的一次 feedback 轮：纠正上文中两处实际误读。只追加本节，不改其他内容；原文保留作为历史，凡与本节冲突处，以本节为准。未重跑 cold read，未执行代码/网络/Provider 操作，消费对象不变（commit `f76a5955…`）。

### (a) 动作 4：把「真实 app/service 或 Provider」一并当作超出本地测试授权

**原文（动作 4）：**「若需要真实 app/service 或真实 Provider 才能驱动 → 超出当前授权/环境，停（进入 §7 召回）。」

**误读：** 把「真实」与「远端/授权外」画了等号，于是把可在本地实际执行的对象也一并推进了召回。

**正确语义：**

- **real leg 指实际执行被声明的对象/代码/交互，不等于远端联网。** 真实 SDK、production mapping、序列化/解析代码在被声明的对象上真正跑起来，就是 real leg 的一种形式；它不因「真实」二字自动越出「只允许本地测试运行」的授权。
- **local service 不因叫「真实」就自动越出 local 测试授权**；本地启动、本地驱动属于本地测试运行的范畴，是否在授权内取决于任务对象与工具边界，而不是取决于它是不是「真实服务」。
- **远端 Provider/部署行为另需其相应证据**（真实远端交互、部署环境观察），这部分才可能超出「本地测试运行」的授权，按 §7 召回。
- **修正后的动作 4 执行判定：** 先做本地可执行的部分——用本地合法 stub/fixture 实际执行 production adapter 的 mapping、实际执行真实 SDK/序列化代码并捕获观察；只有确实需要远端 Provider 或部署环境观察的 claim 才停下并召回。

**fixed 文本可核对句（f76a5955）：** `behavior-claim-evaluation.md` §Use：「The verification surface follows the claim's natural requirement. Synthetic or fixture-based evidence is appropriate when the claim is about logic isolation or mapping under controlled input」；「Test mode is a professional choice, not a whitelist.」（该 §Use 的 author addition 即「verification surface follows the claim's natural requirement」这一表述。）`guide-mock-adapter-choice.md` Rule 3：「observe the adapter at its own surface — a local stub or recorded fixture is one option for contract mapping」「this is not a universal no-network rule.」

### (b) §6 C4：把 SDK/wire/Provider/部署混成一桶判「全不能证」

**原文（§6 C4）：**「**C4（真实 Provider/SDK/wire/部署）**：**在现有授权内无法建立**……保持 UNVERIFIED。」

**误读：** 把四类观察合并成一个整体判定，连带把可在本地合法执行的 SDK/production mapping 部分也判为不可证。

**正确拆分：**

| 观察类别 | 修正后的判定 |
| --- | --- |
| production mapping / 真实 SDK 的本地执行 | 属于动作 4 可达范围：在本地合法 stub/fixture 下实际执行适配器/序列化代码即可证明该范围。在给定事实下其状态是「尚未执行」，不是「无权执行」；不因「无真实 Provider 可用」而判不可证。 |
| wire 行为 | 拆开看：本地可观察的序列化字节/字段形状/构造结果，可在本地执行中观察到；真实远端链路上的 wire 行为，随远端 Provider 一并另需证据。 |
| 远端 Provider 行为 | 另需其相应证据（真实 Provider 交互）；在现有授权下不可建立的部分保持 UNVERIFIED，并按 §7 召回。 |
| 部署行为 | 同理，另需相应证据；部署/发布动作不在本次任务授权内。 |

因此 §6 的 C4 条按上表拆分替换；§6 中 C2/C3「本地 fixture 驱动 production mapping 可达」的结论与本节一致，不受影响；C4 中「不依赖远端观察即可证明的部分」改判为「尚未执行（可达）」，只有「远端 Provider/部署」保持「现有授权内不可建立 + 召回」。不声称任何观察已被执行。

**fixed 文本可核对句（f76a5955）：** `verification-harness-design.md` §Use：「A real leg is required only for the claims that need one」；`guide-mock-adapter-choice.md` Rule 3 与 §Counterexample：「observe the production adapter against a local stub/recorded fixture covering nested/missing/null shapes and assert request + parsed output, with the mapping path actually invoked」。

**来源说明：** 本节接受的语义（real leg = 实际执行被声明的对象/代码/交互，不等于远端联网；真实 SDK/production mapping 可在本地合法 stub/fixture 下实际执行并证明该范围；local service 不因叫真实就自动越出 local 测试授权；远端 Provider/部署行为另需其相应证据）来自本次 tpw-night-driver feedback，与上列 fixed 文本句子一致。该定义在消费的 f76a5955 版本中无逐字原句，以本次反馈为准接受。

消费 commit 仍为 `f76a5955a89e4d703f66c120a90ab2b37901b7f2`（core tree `01514a3918dbf5a08d47b2f8e046c30e6ee0ee82`）；本节为**文本可消费观察，非运行效果**。
