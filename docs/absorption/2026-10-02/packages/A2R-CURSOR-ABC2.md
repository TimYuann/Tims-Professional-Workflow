# A2R-CURSOR-ABC2 · cursor-plugins 审核包 2（原则族：执行证明 / 变更形态 / 学习编码 / 上下文与报告 / 共享写面）

- 发现者：tpw-absorb-a2r（A2r）
- 源仓：`cursor-plugins`，pin `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`（只读 locator：`.worktrees/legacy-pre-night-2026-10-01/upstreams/cursor-plugins`）
- 产品基线：night worktree；core `professional-workflow/`（21 文件）；冻结 Backbone 未触碰
- 供 `tpw-absorb-gate` 实质裁定；本包不自行裁定采纳；所有处置为“拟/候选/待裁定”
- 与包 1（`A2R-CURSOR-ABC.md`）的关系：包 1 覆盖 A/B/C 主干机制与评审/交接/轨迹；本包覆盖 pstack 原则族的可用部分与上下文/报告/学习机制。不重复包 1 已读文件（`never-block`、`model-the-domain`、`boundary-discipline`、`attack-the-premise` 已在包 1 记录）。
- 与 a4 的边界：本包 MG-2 明确把 `outcome-oriented-execution`、`migrate-callers-then-delete-legacy-apis`、`boundary-discipline/type-system-discipline`、实现工具类（codemod 具体形态）列为 a4 候选；本包只保留 A/B/C 与工程裁决相关判断面。
- 读取方式说明：以下均为**读到原文的描述**；未执行任何源脚本或 hook；“验证方案”均未执行。

## 1. 包内机制组总览

| MG | 机制组 | 主要源文件（pin 内） | 建议判断位点 | 类型 |
| --- | --- | --- | --- | --- |
| MG-1 | 执行单元与证明纪律 | `principle-sequence-verifiable-units`、`principle-prove-it-works`、`principle-fix-root-causes`、`principle-build-the-lever`、`principle-test-behavior-not-implementation`、`skills/tdd`、`skills/blast-radius` | F（证据与执行） | 方法候选 |
| MG-2 | 变更形态与读者负担 | `principle-experience-first`、`principle-exhaust-the-design-space`、`principle-foundational-thinking`、`principle-laziness-protocol`、`principle-minimize-reader-load`、`principle-subtract-before-you-add`、`principle-redesign-from-first-principles`、`principle-outcome-oriented-execution`、`principle-migrate-callers-then-delete-legacy-apis` | B/C 为主，D 交界 | 方法候选 |
| MG-3 | 原则语言与学习编码 | `docs/guide/08-principles.md`、`principle-encode-lessons-in-structure`、`skills/reflect`、`cursor-team-kit/skills/workflow-from-chats` | A / meta / Driver | 规则+方法候选 |
| MG-4 | 上下文重建、解释与状态报告 | `principle-guard-the-context-window`、`skills/recall`、`skills/teach`、`cursor-team-kit/skills/weekly-review`、`what-did-i-get-done` | A / Voice / Driver | 方法候选 |
| MG-5 | 共享写面与幂等（Driver/D/E 交界） | `principle-separate-before-serializing-shared-state`、`principle-make-operations-idempotent` | Driver 组合 + D/E | 规则候选（部分交 a4） |

---

## MG-1 执行单元与证明纪律（F）

### 1) 机制与触发情境；源锚点与已读/尚缺

| 源锚点 | 已读 | 尚缺 |
| --- | --- | --- |
| `pstack/skills/principle-sequence-verifiable-units/SKILL.md`（全文） | 全文 | 无 |
| `pstack/skills/principle-prove-it-works/SKILL.md`（全文） | 全文 | 无 |
| `pstack/skills/principle-fix-root-causes/SKILL.md`（全文） | 全文 | 无 |
| `pstack/skills/principle-build-the-lever/SKILL.md`（全文） | 全文 | 无 |
| `pstack/skills/principle-test-behavior-not-implementation/SKILL.md`（全文） | 全文 | 无 |
| `pstack/skills/tdd/SKILL.md`（全文） | 全文 | 无 |
| `pstack/skills/blast-radius/SKILL.md`（全文） | 全文 | 无 |
| `pstack/skills/poteto-mode/playbooks/bug-fix.md` steps 1–6 | 包 1 已读，本包引用 | 无 |
| `pstack/skills/poteto-mode/playbooks/perf-issue.md`、`hillclimb.md` | **未读** | 属 a4（性能/实验方法） |

触发情境（源文 description）：多步工作（sweep、迁移、成批相似编辑）与提交/PR 堆叠（sequence-verifiable-units）；完成任务后、宣布完成前（prove-it-works）；调试（fix-root-causes）；任何非平凡工作（build-the-lever）；写/改/保留测试（test-behavior）；有便宜本地测试路径的 bug（tdd）；小 diff 不信任、想知道改动能破坏什么（blast-radius）。

### 2) 操作、成立条件、失败模式、反例/例子

**sequence-verifiable-units（操作）**：把工作排成小单元，每单元以可检查状态结束，绿了才前进。执行上：每个单元是 before/after 括号（known-good 状态 → 一处改动 → 跑检查 → 继续）；先把分支 rebase 到干净 trunk，使每次检查都对真实 baseline；即使 tool 化编辑让逐单元检查近乎免费也要跑。交付上：按“能证明工作”的顺序堆提交/PR；典型形状是 failing test 先、fix 在上；其他合法故事顺序：先减法再重塑、先捕获 baseline 再 treatment、先 scaffold 再 feature；每个提交独立站得住、序列读起来是一个论证。

**prove-it-works（操作）**：直接检查真东西，不从代理/自述/“能编译”推断。检查清单：进程活性直接查，不查派生状态；读实际值，不读缓存/派生表示；验证失败时先怀疑观察方法、后怀疑系统。强调“脚本化检查”：最强的证明是可重复同一比较的确定性脚本，跑它、保留输出作为 reviewer 可复跑的 artifact；artifact 保持人类可见；只有大型/复杂工作（大端口、迁移）才提交它。

**fix-root-causes（操作）**：先复现；问 why 到根因；不加 guard（加 nil check 压 crash 是症状修复）；需要一段长注释辩护的 workaround 说明代码错了（改代码不改注释）；修 pattern 不只修 instance（grep 同模式、修全部）；卡住就仪器化，不猜。**重启类 bug 先怀疑状态**：config 文件、cache、lock 文件、序列化状态；若清掉一个 state 文件就恢复，优先把 state 校验作为修复。

**build-the-lever（操作）**：非平凡工作建工具（codemod/生成器/脚本/子代理遵循的 skill），不要手工做。两个收益：吞吐（同法每次、免费重跑）与信心（一个 reviewer 可读可重跑的 artifact；“手做的改动只能靠重做来重验”）。模式：默认建 lever，仅在 trivial（一两处一眼可见的编辑）跳过；先手工做第一个单元学 recipe，再建工具，并用“重跑工具 vs 手工版 diff”证明它；让 lever 可安全重跑；确定性 lever 优于 fan-out（能一遍处理全部就自己跑，不派代理手工应用）；fan-out 时把 lever 写成所有子代理读的 skill（recipe、验证契约、do-not-touch 围栏一个 artifact），并放在代理写集之外；**引用了本原则却 diff 里没有 codemod/script/generator/delegate skill 就是没应用**；工作比 session 活得久就提交 lever。平衡：门槛是 triviality 不是 repetition；一次性工作若 lever 让它可检查也值得；最小的脚本，绝不框架。

**test-behavior-not-implementation（操作）**：测试按用户方式调用代码、断言观察到的字面期望值。检查：**如果它 import 的每个函数都返回 `undefined` 测试仍会过，那它没有观察行为、不可能因缺陷失败** → 重写断言或删除。五种仍会过的形状：弱/无断言（无 expect、只有 toBeDefined/toBeTruthy/not.toThrow/toBeInstanceOf/toBeGreaterThan(0)）；只测 mock 或缺失（toHaveBeenCalled/not.toHaveBeenCalled/toBeUndefined/toEqual([])/toHaveLength(0)/not.toBe(wrongValue)）；自指（expected 来自被测代码）；常量 pin（重述手工常量/config 默认/表行/prompt 字符串）；fixture 断言 fixture（断言测试自建数据或 beforeEach 计算值，subject 从未在 body 中运行）。修复：在 body 内用具体输入调用 subject 并断言字面输出或可观察效果；缺失类断言在另一输入上断言存在；常量类改为测读它的机制；mock 类断言收到的 payload 或调用后状态。保留例外：跨表行的关系测试（键在两表都存在、父存在）、`*.test-d.ts` 编译期检查。

**tdd（操作）**：只在用户明示要 TDD/失败测试/回归测试，或 bug 有明显便宜本地测试目标时。流程：理解 bug（期望行为、当前行为、受影响路径、最小可观察复现）→ 选最窄可执行检查（优先该 codepath 已有的最接近测试；无明显可行路径就不要为流程而新造）→ 先写最小失败测试（编码期望行为，不镜像实现）→ 修复前运行确认它因预期原因失败（过了或因无关原因失败就先纠正测试/复现）→ 做最小生产改动 → 重跑通过。不可行时用最接近的可执行回归检查（定向脚本、手工复现命令、浏览器自动化、快照比较、日志断言、聚焦集成）。**“Prefer no new test over a bad test”**；坏测试定义：主要测 mock、编码当前实现细节、依赖时序或无关全局状态、小修复需要昂贵基础设施、证完就删。Guardrails：不为匹配错误实现改测试；不削弱既有断言（除期望行为真的变了且理由清楚）；聚焦 bug、避免 fixture churn；flaky 就尽量确定化并记录锁定信号；暴露更大类失败时先落聚焦回归再考虑 sibling 覆盖。最终响应报证据：失败在前测试/检查与其产出失败、通过在后运行、若未能演示 failing-before 要说明原因与所用替代检查。

**blast-radius（操作）**：不要交一份“听起来对”的写稿——找到整件事所依赖的**一到两个安全事实**，用运行代码证明。置信阶梯五级（尽量往下爬并说明停在哪一级）：1) 你说如此（单独无价值）；2) 指向行（真实 file:line 或库源码）；3) 展示坏情况不可能发生（逐步走通失败路径到不了）；4) 运行它（脚本/测试调真实代码，错了大声失败）；5) 在运行 app 中复现。步骤：读改动（diff、增删符号、实际不同之处，含 diff 没写明的部分）；找“它之所以安全的那一个事实”（如“这个调用只删已死的 cache 条目、不做别的”），时间花这里而非长串 maybe；看 grep 停下的地方（读所调库源码与 pinned 版本/本地 patch；理清 microtask、unmount/teardown、框架 timing；追符号搜索漏掉的：API 返回 JSON、DB 列、wire format、另一语言读同一字节、feature flag、下游三跳）；诚实标每条风险的概率与代价，confirmed vs cleared 分开；证明那一个事实（写脚本/测试跑真实代码并贴出结果）；大范围改动可用 arena 多模型同题合并。回头交付段：What it does / The one fact it's safe because of（含证明步骤与证据，未证明就写 unproven）/ Risks（file:line、概率、代价、怎么查）/ Cleared / Before you merge（最便宜能抓到真 bug 的测试或复现脚本）。

**成立条件**

- sequence：每个单元存在可执行检查；能先对齐干净 baseline。
- prove-it-works：存在可观察的真实 artifact（值、进程、diff、运行中 app）；观察方法本身可靠（失败时先怀疑它）。
- fix-root-causes：能复现；有仪器化手段；重启类 bug 存在可清理的持久状态。
- build-the-lever：工作非 trivial；lever 可安全重跑；fan-out 时写集隔离。
- test-behavior：测试能调用真实 subject 并断言字面期望；例外关系测试/编译期检查。
- tdd：存在便宜、稳定、贴近已有测试路径的检查；否则明确跳过而不是硬造。
- blast-radius：能定位“一个安全事实”，且该事实可被脚本运行验证；库版本/运行时序可查。

**失败模式/反例（源文点名或直接反例）**

- 批量检查放最后：break 被埋在批次里，且已在不稳的 base 上继续建。
- “能编译”当证据；读缓存/派生状态；验证失败先怪系统。
- nil-check 压 crash；一段长注释辩护的 workaround；只修当前 instance。
- 手工重做代替 lever；引用原则但 diff 里没有工具（源文明确判定为“没应用”）；把 lever 做成框架。
- 测试在 import 全返回 undefined 时仍通过（五形状）；为流程硬造坏测试；改测试去匹配错误实现。
- blast-radius：交写稿而不证明；只列 caller（“agent 一秒就能 grep 到”）；风险不标概率/代价；把“符号搜索无结果”当无风险。
- tdd 反例：把“便宜测试路径不存在”也硬塞 TDD；快照/mock 测试证明力不如跑真命令。

### 3) 判断位点与 Profile 调用

| 位点 | 专业 concern | 何时调用 | 由哪个 Profile 提议 |
| --- | --- | --- | --- |
| F：证明与验证设计 | 证据/测试/回归 | 完成前、回归、bug 修复、怀疑小 diff | `evidence-evaluation` |
| E：最小改动与复现 | 实现/调试 | 修复过程中 | `implementation`（自测为可核对输入） |
| Driver：单元排序与交付顺序 | 程序性 | 多单元/多 PR 顺序 | `driver` |

### 4) 当前产品锚点、覆盖、缺口、为何值得吸收

- `methods/local-defect-feedback-loop.md`：`## Method` 1–5（精确契约与原失败场景、可复现、竞争解释、修复、重跑）+ `## Limits`（不要求固定假设数、每红测试一提交、控制技能/loop/模型/PR）。其 `## Source anchors` 已注明：“The S2 pstack bug-fix playbook was considered but is not part of this method body. Its same-surface and mechanism-evidence advice remains optional; its control/loop/model/PR defaults are excluded.”
- `methods/behavior-claim-evaluation.md`：claim/条件/度量/阈值；baseline/treatment 同命令同环境；verdict mapping；`## Limits`（独立作者不是测量方法的一部分）。
- `profiles/evidence-evaluation.md` `## 常见误区`：“只验证‘能跑通’，不设计能揭示错误的负控制。”`## 关键问题`：“什么观察能把‘成立’与‘不成立’分开？关键负控制是什么？”
- `profiles/implementation.md` `## 心智模型`：“实现是发现事实的地方”；`## 交接与召回` 交出“自测证据”。

已覆盖：复现→假设→最小修复→重跑主场景；可证伪 claim 与 baseline/treatment；负控制意识。

具体缺口：

1. **没有单元/交付排序方法**：产品写“小步验证”在 `implementation.md` 按需入口只作为候选名，没有 before/after 括号、rebase 干净 trunk、failing test 先行的交付故事。
2. **没有“证明强度阶梯”**：`prove-it-works` 的 real-vs-proxy 检查（进程直接查/读实际值/失败先怀疑观察方法）与“脚本化可重跑 artifact”在产品缺席；现有三态只规定 verdict，不规定证据形式。
3. **没有测试有效性判据**：五形状 + “import 全 undefined 仍通过”这一击穿式检查是可直接采用的操作；产品只有“负控制”原则。
4. **tdd 的适用/跳过条件是正交补充**：产品无 TDD 方法正文（M4 曾延后；执行计划明确不得以“避免过度流程化”排除 TDD 本身），源文给了明确的 cheap-path 门槛与“prefer no test over bad test”。
5. **没有 blast-radius 方法**：小 diff 不信任时，产品无“一个安全事实 + 证明 + 置信阶梯 + grep 停下的地方”的操作；`cross-module-design.md` 管的是改动规划时的 D 判断，不是事后风险审计。
6. **没有 build-the-lever**：产品缺“把工作变成 reviewer 可重跑 artifact”的交付形态；这与 `guide-redacted-evidence.md` 的证据保管互补，但不同（lever 是可重跑性）。

为何值得吸收：这组是 F 的证据纪律主体，全部可在纯方法层使用，且与已接受的 M4 方法（claim/treatment、复现循环）互补而非替换。

### 5) 拟处置与载体

- 拟保留：before/after 括号与交付顺序；脚本化可重跑证据；real-vs-proxy 检查；restart-bug 状态优先；pattern-not-instance；五形状与击穿检查；tdd 的 cheap-path 门槛与“no test over bad test”；blast-radius 的五级阶梯与“一个安全事实”。
- 拟改变：把 `principle-*` 交叉引用改为自包含正文；把“commit/PR/CI”措辞改为产品中性（提交/交付单元），不捆绑 forge 流程；`build-the-lever` 的 codemod/generator 例保留但说明“lever 形态由任务决定，不要求框架”。
- 拟删除：模型 slug、subagent 调用、Cursor 工具名、`show-me-your-work` 标签引用（轨迹已由包 1 MG-8 覆盖，改为交叉引用）。
- 载体：方案 1（推荐）把执行证明纪律扩进现有 `methods/local-defect-feedback-loop.md`（它已拥有“局部缺陷 + 证据”责任）与新支持文件 `methods/guide-proof-strength.md`（prove-it-works/blast-radius/test-behavior 合并为“证据强度与测试有效性”指南），`methods/README.md` 按需表加一行；`tdd` 作为 `guide-*` 或扩进局部缺陷方法的一节。方案 2 全部塞进 `behavior-claim-evaluation.md`（代价：该文件已声明只评特定 claim，会撑破边界）。
- 与 a4 的分工：`perf-issue`/`hillclimb` 的实验设计、`build-the-lever` 的具体工具形态归 a4；本包只保留“可重跑证明”的产品面。

**仍依赖真实 runtime 的能力**：脚本真正执行、真实 app 复现、库源码与 pinned version 读取；产品只能定义要求与证据形状。

### 6) 正文草稿与验证方案

```
证据强度阶梯（用于任何“它安全/它能用”的声明）：
1. 声称 → 无价值
2. 指到 file:line（或库源码/pinned 版本）
3. 展示坏情况不可能发生（逐步走通）
4. 运行脚本/测试，调真实代码，错了大声失败
5. 在运行 app 中复现
停在哪一级要明说；未证明的写 unproven。

测试有效性击穿检查：
如果测试 import 的每个函数都返回 undefined 而测试仍通过 → 它没观察行为，重写或删除。

单元交付故事：
known-good → 一处改动 → 跑检查 → 下一单元；failing test 先、fix 在上；先减法/先 baseline/先 scaffold 也成立。
```

验证方案（未执行）：选一个真实小修复，(a) 按 before/after 单元序列做并记录每步检查；(b) 对一段现存测试跑“undefined 击穿”检查，统计应删/应修的测试；(c) 对一个不信任的小 diff 做 blast-radius，检查是否找到并运行验证“一个安全事实”。边界：不要求所有任务都到阶梯 5；不要求每个修复都有失败测试（cheap-path 门槛）；不创建框架。

---

## MG-2 变更形态与读者负担（B/C 为主，D 交界）

### 1) 机制与触发情境；源锚点与已读/尚缺

| 源锚点 | 已读 | 尚缺 |
| --- | --- | --- |
| `pstack/skills/principle-experience-first/SKILL.md` | 全文 | 无 |
| `pstack/skills/principle-exhaust-the-design-space/SKILL.md` | 全文 | 无 |
| `pstack/skills/principle-foundational-thinking/SKILL.md` | 全文 | 无 |
| `pstack/skills/principle-laziness-protocol/SKILL.md` | 全文 | 无 |
| `pstack/skills/principle-minimize-reader-load/SKILL.md` | 全文 | 无 |
| `pstack/skills/principle-subtract-before-you-add/SKILL.md` | 全文 | 无 |
| `pstack/skills/principle-redesign-from-first-principles/SKILL.md` | 全文 | 无 |
| `pstack/skills/principle-outcome-oriented-execution/SKILL.md` | 全文 | 无（拟交 a4，见处置） |
| `pstack/skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md` | 全文 | 无（拟交 a4，见处置） |
| `pstack/skills/principle-type-system-discipline/SKILL.md` | **未读** | 已由 a4 认领；本包不评估 |
| `pstack/skills/architect/SKILL.md`（design-twice、scrap tells） | 包 1 已读相关段 | `references/design-red-flags.md` 未读（a4） |
| `pstack/docs/guide/08-principles.md` 相关条目 | 全文 | 无 |

触发情境：产品/UX/功能范围取舍（experience-first）；没有先例的新交互或架构选择（exhaust-design-space）；写逻辑前选核心类型/数据结构、排 scaffold-vs-feature、问并发 actor 共享什么（foundational-thinking）；重构、评估 diff 大小、想加抽象/层/信号穿线（laziness）；代码难追、要数层数与隐藏状态（minimize-reader-load）；排序新增/重构/重写（subtract-before-you-add）；把新需求整合进既有设计（redesign-from-first-principles）；有明确 phase 边界的规划重写/迁移（outcome-oriented）；引入新内部 API 而旧 caller 仍在（migrate-callers）。

### 2) 操作、成立条件、失败模式、反例/例子

**experience-first**：实现方便与用户愉悦冲突时选愉悦。五条：每个 feature/control/option 必须被证明合理；ship less, ship better（三个打磨好的 feature 胜过十个粗糙的）；先原型再承诺；细节做对（转场、对齐、间距、反馈、错误态）；收紧核心循环（每个 feature 服务中央工作流或让开）。**“用户”是消费工作的人**：UI 是终端用户；library/internal API 是 import 它的同事；**接下来维护代码的工程师也是用户**，同权重、从其视角解释影响。Foundations 服务体验；foundational thinking 管*顺序*，本原则管*目标*。

**exhaust-the-design-space**：没有既定先例时，先建 2–3 个具体竞争原型/sketch 并列比较再承诺；“design it twice” 是同一规则的别名；**同一形状的第二版不算**。适用：无先例的新 UI 交互、有多个可行方案的架构选择、依赖“手感而非逻辑”的产品设计决定。不适用：既定模式的机械实现、目标状态明确的 bug fix/refactor、约束决定唯一可行方案。

**foundational-thinking**：structural decisions 保护 option value；code-level decisions 保护 simple。**数据形状先于逻辑**：早定核心类型、追每个访问模式、选匹配主路径的结构。code 级：DRY 结构而非每行；类型/数据模型应收敛；三条相似语句胜过过早抽象；偏好 explicit 胜过 clever；测行为与边界，不测行数。并发推论：actor 共享状态前问“另一 actor 并发修改会怎样？”，答案不是“无事”就隔离。scaffold first：若某物让之后每个 phase 受益就先做（CI、lint、测试基础设施、共享类型是 scaffold）；按 option value 排序：setup 先于 feature，tests 先于 fix；提交小而单一目的；每个增量应落地一个连贯抽象或深化既有抽象；不要把新能力作为 special-case 协调散到各 caller。**减法先于 scaffold**：先删死代码再铺地基。

**laziness-protocol**：以最少代码/复杂度换最大结果。Prefer deletion（要重构/改进时先找可删）；维护平坦调用层级（若回答一个问题要穿 3 个以上文件/层，就压平；富接口隐藏实质工作不算深调用链）；合并决定（同一选择不在多处重复，放一个真源并传简单 flag）；最小 diff；**question the threading**（要求把新信号穿过类型/schema/pipeline 时停下来找更直接路径）；sweat the small leaks（删小 pass-through、表示泄漏、重复选择）；**测试**：人类开发者会不会觉得难维护——会，就是坏方案。

**minimize-reader-load**：可维护性 = 读者理解代码要做的工作。两个独立轴：到答案要追的层数；读者要放脑中的隐藏/可变状态。LOC、圈复杂度、“clean architecture”都只是代理。模式：删成本大于收益的层（单 caller wrapper、无第二实现的 adapter、从未需要的投机抽象）→ inline；相邻层必须改变抽象（重复相同方法与参数、无压缩 → 塌陷）；要求接口压缩（宽接口隐藏很少复杂度会让读者同时学表面与实现，偏好隐藏有意义决定的边界）；缩小 state 范围（纯函数 > 返回而非突变、局部 > 字段、字段 > module state、module state > globals；derive 而不是 sync）；**在边界命名不变量**，让读者只学一次；加层或加状态前问：它在别处减少的读者负担是否至少等量。测试：新读者能否在 30 秒内回答“X 从哪来”“什么能改 X”。

**subtract-before-you-add**：演化系统先删复杂度再建。默认减法；把简化当持续投资（同一或更小表面留下更简单且更有能力的设计）；顺序：删在构前；cut before polish（先到最小再投资质量）；按观察到的用法设计，不做投机边界；不做 spec 未要求的 validator/parser/guard；简化 prompt（删冗余指令、过多模板）；引用无新内容就删而不是留 stub。

**redesign-from-first-principles**：整合变更时不把需求 bolt-on，而是当作 day-one 假设重设计。读所有受影响文件并理解当前设计；问“如果今天用这个新需求从零写，会建什么”；把变更传播到每个引用（类型、文档、例子、rationale 段）；想完整重设计，但增量交付。这是整合变更时保护 option value 的方法。

**outcome-oriented-execution**（拟交 a4）：优化可验证的最终状态而非平滑中间态；**core rule**：末端完整性优先于过渡稳定；计划内、有界、可逆的中间破坏可接受；**guardrails**：只用于有明确 phase 边界的计划重写/迁移；声明哪里可接受临时破坏；迁移中对活跃触碰区域保留高信号检查；计划完成时要求完整静态+运行时验证。

**migrate-callers-then-delete-legacy-apis**（拟交 a4）：新 API 是正确设计时，同一波迁移 caller 并删除旧 API，不因内部 caller 仍在而保留旧路径；inventory caller → migrate → delete；临时 adapter 是例外且限时，不是默认架构；测试改断言新契约，删除只保护 refactor 前实现细节的测试。适用：无外部用户依赖向后兼容；项目能吸收协调式破坏；新 API 属简化/refactor 计划。

**成立条件/失败模式**

- experience-first：存在真实消费体验冲突；能识别“用户”是谁（含维护者）。反例：为方便实现把粗糙十条 feature 当交付；把维护者体验排除在“用户”之外。
- exhaust-design-space：无先例且答案不显然；**反例**：既定模式的机械实现也去建三个原型；或“第二个同形状变体”充数。
- foundational-thinking：结构性决定有 option value 可保护；反例：为 hypothetical future 铺地基（与产品“robustness proportionality”冲突面，见 §5）。
- laziness/reader-load/subtract：形状已清晰、局部、不太会增长时**不要**强推抽象或大改；反例：把 6 层 adapter 换成 500 行平铺全局状态（flat file with 50 globals 与 6 层堆栈同样难读——源文两轴独立）。
- redesign/outcome/migrate：只在有明确边界与可逆性时用；反例：把“中间可破坏”当成无限期兼容层或大爆炸重写的许可。

### 3) 判断位点与 Profile 调用

| 位点 | 专业 concern | 何时调用 | 由哪个 Profile 提议 |
| --- | --- | --- | --- |
| B：体验与范围取舍 | UX/产品/维护者体验 | 功能范围、交互、抛光取舍 | `behavior-domain`，Voice 冻结选择 |
| C：不变量与状态表达 | 领域/维护性 | 判断“结构是否在积累偶然复杂度” | `behavior-domain`（C 部分） |
| D：设计空间与兼容策略 | 架构/兼容/恢复 | 无先例设计、重写、API 替换 | `technical-planning`（a4 侧执行） |
| E：局部形状 | 实现 | 承诺内的删减/压平 | `implementation`（a4 侧） |

### 4) 当前产品锚点、覆盖、缺口、为何值得吸收

- `profiles/behavior-domain.md` `## 心智模型`：“冲突要在约定正文显露”；`## 常见误区`：“用方便实现的行为悄悄替代接受承诺。”
- `profiles/technical-planning.md` `## 心智模型`：“coordination surface 与 implementation interior”；“最低充分性：未参与讨论的合格实现者能开始且不猜共享承诺。过度规定检验：换一种局部实现，上游约定是否全都不变。”
- `methods/cross-module-design.md` `## Limits`：“Do not force modules to merge for depth, prescribe each helper, or choose a design solely from file count.”
- `profiles/implementation.md` `## 心智模型`：“implementation interior 自主：局部算法、数据结构、类型、重构、测试接缝在此范围内由 E 判断。”
- `profiles/intent-voice.md` `## 心智模型`：“目标与非目标同权；‘顺手优化’不是目标的一部分。”

已覆盖：行为不能悄然替换；coordination surface 判据；不过度规定的检验；E 有局部数据结构/重构空间；非目标同权。

具体缺口：

1. **没有“目标体验优先”的 B 判断**：产品没有“消费者是谁（含维护者）”的明确陈述与“ship less, ship better / 每个 option 必须被证明”的取舍规则；这与“范围/优先级”直接相关。
2. **没有设计空间探索门槛**：“无先例 → 2–3 个整形状竞争原型，同形状第二版不算；有既定模式就不做”是可直接用的 B/D 判据；产品的 `technical-planning.md` 只问“有没有多个实质不同的方案”，没有何时必须找、何时明确不找。
3. **没有“数据形状先于逻辑”的 C 操作**（模型部分包 1 MG-4 已覆盖结构清单；本组补“核心类型早期 + 并发推论 + scaffold 顺序 + 减法先于 scaffold”）。
4. **没有读者负担两轴与 30 秒测试**：这是 C 的“领域/结构是否可依赖”与可维护性的操作判据；产品 `cross-module-design.md` 有 depth 概念但没有读者负担的测量方式。
5. **没有 deletion-first 与 diff 最小化规则**：laziness 的“先删、压平、合并决定、最小 diff、question the threading、small leaks”与 `technical-planning.md` 的“过度规定检验”互补；产品缺“删除优先”的明确倾向。
6. **没有 outcome-oriented / migrate-callers 的兼容策略**（a4 候选；但 B/C 责任方需要在“行为承诺改变 vs 兼容层”上知道它，避免把“兼容”当成默认）。
7. **没有 redesign-from-first-principles**：产品要求“不静默改写承诺”，但缺“把新需求当 day-one 假设重设计并传播到所有引用”的操作。

为何值得吸收：这组决定“要做多少、先删什么、给谁做、什么算过度设计”，是 B/C 范围判断与 D 交接之间的薄弱层；全组可在无 runtime 依赖下使用。

### 5) 拟处置与载体

- 拟保留：experience-first 的目标条款（含维护者）；exhaust-design-space 的“2–3 整形状 + 不适用反例”；foundational 的“数据形状先于逻辑 + 并发推论 + scaffold 顺序 + 减法先于 scaffold”；laziness 六条与人类维护测试；reader-load 两轴、接口压缩、state 范围、30 秒测试；subtract 的“删在构前、按观察用法、不做投机 guard”；redesign 的“day-one 假设 + 传播到每个引用 + 增量交付”。
- 拟改变：将 `migrate-callers`/`outcome-oriented` 明确标为 a4 候选，本包只保留其**判断条件**（无外部兼容需求、计划内有界可逆）供 B/C 在“承诺变更 vs 兼容层”时引用；robustness 相关的“scaffold”措辞改为按任务可靠性要求配置，避免与产品 AGENTS 的 proportionality 冲突。
- 拟删除：把 pstack 原则名当引用；模型/工具；`arena` 具体调用（只保留“需要独立比较时可用并行探索”）。
- 载体：方案 1（推荐）新增 `methods/change-shape-and-reader-load.md`（B/C 侧：experience、design space、删减与读者负担、redesign；D 交接面引用 `cross-module-design.md`），`profiles/behavior-domain.md` 与 `profiles/technical-planning.md` 各加一行入口；`outcome-oriented`/`migrate-callers` 转 a4。方案 2 拆成两份（范围取舍 / 代码形态）——本包不推荐，两者共享“消费者与维护者体验”的同一判据。
- **风险提示（供 gate）**：`encode-lessons-in-structure`（MG-3）与 `foundational-thinking` 的 scaffold 倾向都可能被读成“建设平台/框架”，与执行计划“不复活旧 runtime/registry、不建 registry/框架”和产品 AGENTS 的 robustness proportionality 有张力。本包建议在正文里写明“机制强度按已接受可靠性级别配置，不因假设未来而建”。

**平台耦合拆除**：无强制平台耦合。仍依赖真实 runtime 的是原型/设计的真实比较与实现反馈。

### 6) 正文草稿与验证方案

```
范围与形态判据（草稿）：
1. 消费者是谁：终端用户 / import 的同事 / 维护者；三者体验同权。
2. 无先例且答案不显然 → 2–3 个整形状候选并排比较；同形状第二版不算；有既定模式就不做。
3. 数据形状先于逻辑；先问并发 actor 是否共享可变状态。
4. 默认减法：删死代码/投机 guard/单 caller wrapper/重复决定，再建。
5. 读者负担两轴（层数/隐藏状态）；30 秒回答“X 从哪来、什么能改 X”；边界命名不变量。
6. 新增量落一个连贯抽象；不把新能力散成 special-case 协调。
反例：给已清晰局部的小功能强加抽象；用 500 行平铺全局换取“扁平”而堆高隐藏状态；把兼容层当默认架构。
```

验证方案（未执行）：取一个真实小功能，先按“消费者三视角 + 2 候选 + 删减清单”走一遍，记录删掉的层/状态与读者负担变化（层数、隐藏状态项、30 秒问题是否可答）；反例材料为“直接加抽象/兼容层”的版本。边界：本组不产生重构授权；不要求每次变更都做多候选；`migrate-callers` 只在无外部兼容需求时适用。

---

## MG-3 原则语言与学习编码（A / meta / Driver）

### 1) 机制与触发情境；源锚点与已读/尚缺

| 源锚点 | 已读 | 尚缺 |
| --- | --- | --- |
| `pstack/docs/guide/08-principles.md`（全文） | 全文 | 无 |
| `pstack/skills/principle-encode-lessons-in-structure/SKILL.md`（全文） | 全文 | 无 |
| `pstack/skills/reflect/SKILL.md`（全文，含 5/6 步与路由表） | 全文 | `references/judgment-reviewer.md`、`tooling-reviewer.md`、`divergent-reviewer.md`、`synthesizer.md` 未读（属执行细节） |
| `cursor-team-kit/skills/workflow-from-chats/SKILL.md`（全文） | 全文 | 无 |
| `pstack/docs/guide/10-recipes-and-pitfalls.md`（全文） | 全文 | 无 |
| `pstack/README.md` 的原则分组、`/setup-pstack` 的 role lines | 部分（包 1 索引+摘要） | `skills/setup-pstack/SKILL.md` 未读（配置机制，归 a4 或后续） |

触发情境：想用一致词汇精确指挥工作（08-principles：“You don't invoke principles. You use their names to steer.”）；发现自己在第二次写同一条指令（encode-lessons）；用户说 reflect；要从最近 chat 提取持久偏好并转成 skill/rule/doc（workflow-from-chats）。

### 2) 操作、成立条件、失败模式、反例/例子

**principle names 作为接口（08-principles）**：每个名字指向一个完整规则（agent 已读过），一个短语比一段指令更精确地改向。示例：`use subtract before you add...`、`apply prove it works...`、`separate before serializing shared state...`。**配套要求**：agent 必须在其回复中说明该规则改变了哪个决定；“A principle citation with no decision behind it is the tell that it name-dropped instead of applying.” 23 条按五组（core 10 / architecture 6 / verification 4 / delegation 2 / meta 1）。**pitfall 列表**（10-recipes）：在 prompt 里枚举 skills 会重排 playbook 已定顺序（只给目标与约束，命名 skill 只在要覆盖默认时）；模糊 finish condition 让循环无事可查；并行 agent 共用一个 worktree 互相覆盖；用 arena 做 coverage（arena 是同题重复+选基+嫁接；swarm 是分片或声明 race）；接受所有 review 评论（bots/humans 都会混真 catch 与噪声；interrogate 分 act-on/dismissed 并给理由）；把 `auto` 当 model slug；绿构建即成功（build 只证明能编译，要真命令/流程/存储值/profile）；手写 SKILL.md 不走 authoring playbook。

**encode-lessons-in-structure**：把重复的修复编码进机制（工具、代码、metadata、automation）而不是文本指令。Why：文本指令要求读者注意、记住、遵守；结构机制（lint 规则、metadata flag、runtime check、脚本）无需配合即可执行。Pattern：抓到自己在第二次写同一指令时：① 能否变成 lint/metadata/runtime check/脚本；② 能就编码并删除指令；③ 不能（需要判断）就让指令更突出并加失败模式例子。**Pick the strongest mechanism**：不可表示的状态（编译不过）> lint 或 banned API（CI 失败）> canonical helper > runtime check；“agents copy whatever the surrounding code already does and a weaker guard becomes the next template”。Corollary：结构性修复就用结构修复，指令是症状。Feedback loop：capture every correction（区分一次性 vs pattern）→ route to right layer（一次性→脑记；重复→skill/lint；系统性问题→principle）→ close the loop（记录 + 现在应用或建具体 todo）。Anti-patterns：acknowledging without recording（“我会记着”不会持久）；recording without routing（笔记不落地）；fixing without generalizing（修一个实例留模式）。

**reflect（操作）**：用户说 reflect 时，从**本会话自己的 transcript** 挖掘 durable learnings 并路由到具体 skill 编辑。步骤：定位自己的 transcript（系统提示给出路径；**不要 glob 跨 `~/.cursor/projects/*/`**，会读无关私有聊天；三种布局：legacy flat、嵌套、subagent；用第一行 JSONL 的开场用户 prompt 匹配当前会话，找不到就写紧凑 digest）；三个并行 reviewer（judgment/tooling/divergent 三个 lens，各自 prompt template），合成器返回 Accepted/Rejected/Backlog；**结构强制检查**：Accepted 里任何用 lint/script/metadata/runtime check 更可靠执行的项移到 Backlog（encode-lessons）；**应用前把完整 Accepted/Rejected/Backlog 给用户并等明确批准**（skill 变更影响未来所有 agent，不自动应用）；路由：trivial 既有 skill 编辑父代理直做、substantive 既有 skill 编辑交给作者的 skill-authoring 流程、`tune description`（skill 未在应触发时触发）走 description 优化、`new skill` 走创建流程、Backlog 自动进团队 devex/backlog tracker；最后简短总结（已应用/新建/已入 backlog/丢弃+理由）。

**workflow-from-chats（操作）**：从最近 chat 推断 durable working preferences（不是总结 chat，而是提取可复用工作流指导）。Scope：默认最近 7 天；读 parent transcripts 与相关 subagent transcripts（subagent 内容可作证据，但只引用 parent）；不得暴露本地 transcript 路径、secrets、客户数据、私有 chat、凭证。流程：一句话说明目标工作流/偏好面 → 内部 transcript inventory（title/topic、parent conversation ID、日期、完成态、相关 subagent、为何可能含偏好证据）→ 扫描显式偏好、纠正、工作流标记词（“I prefer”“always”“never”“not what I asked”“stop”“review”“PR”“CI”“logs”“skill”）→ 提取 preference atoms（trigger、workflow step、decision rule、quality bar、stop condition、evidence、confidence）→ **confidence 四档**：strong（显式用户偏好、改变工作流的纠正、重复 parent-chat 模式、直接要求编码行为）；medium（被接受的工作流、重复的工具/模型/验证偏好、subagent 共识且 parent 成功使用）；weak（agent 自选行为无用户反馈、单一含糊 transcript、可能任务特定的纠正）；**contradicted（证据互相矛盾→写文件前问用户）** → 按 workflow shape 而非 transcript 聚类（shipping/review/simplification/debugging/capture/communication/delegation/validation）→ 选 artifact（new skill / skill edit / rule / workflow doc / no artifact；对应条件：可触发且反复多步→skill；广泛行为→rule；有用但不可靠触发→workflow doc；情境性/过时/低置信→无）→ 只起草可复用指导，过滤无助于未来任务的轶事。输出：目标工作流、仅 parent 引用的证据语料、偏好画像、Adopt/consider/dismissed、拟 artifact、仅阻挡时列 open questions。

**成立条件**：有可读且属于当前工作区的 transcript/chat 历史；用户授权该学习范围；有可落地的 skill/rule 载体；reflect 需要用户明确要求。

**失败模式/反例**：原则 drop-in（引用名字但没说出改变了哪个决定）；在 prompt 里枚举 skill 重排流程；把一次性纠正写成原则；只笔记不路由；reflect 自动应用（源文明确不自动）；workflow-from-chats 把 subagent 内容当引用来源、跨工作区读 transcript、暴露私有内容；对 contradicted 证据沉默写文件。

### 3) 判断位点与 Profile 调用

| 位点 | 专业 concern | 何时调用 | 由哪个 Profile 提议 |
| --- | --- | --- | --- |
| A/Voice：与人类用共同词汇对齐、纠正/偏好提取 | 目标/偏好/沟通 | 反复纠正、偏好成模式、退工/复盘 | `intent-voice` |
| Driver：把程序性重复升级为机制 | 程序性/组合 | 同一指令第二次出现、失败模式复发 | `driver`（bounded composition） |
| C/meta：把领域规则编码进结构 | 领域/维护 | 规则重复出现在多个消费者 | `behavior-domain` |

### 4) 当前产品锚点、覆盖、缺口、为何值得吸收

- `professional-workflow/methods/README.md` `## Status and source trace` + “Deferred alternatives”：记录接受对象、digest、来源 pin，并明确 defer 理由（“no alternative became a mandatory gate”）。
- `profiles/driver.md` `## 按需方法入口（候选）`：“bounded composition 方法：在接受预设与约束内组装实例，区分‘选配置’与‘授权限’。”
- `docs/absorption/2026-10-02/EXECUTION-PLAN.md`：“不按每文件填长表；一组一份完整包 …”；“不造 registry 平台”。
- `authority/RESPONSIBILITY-BACKBONE.md` §6：“Driver 在已有预设与约束内装配；缺能力时找相应专业责任…不建固定 Role matrix 或资格审批平台。”
- `AGENTS.md`（项目）：Robustness Proportionality 段（不因假设未来加状态机/注册表/框架）。

已覆盖：方法接受与溯源纪律；bounded composition；流程不进 runtime；不建平台。

具体缺口：

1. **没有“共同词汇”的操作面**：产品有 Profile/method 名称，但没有“引用必须伴随被改变的决定”这一防名不副实的检查；也没有“不要在 prompt 里枚举 skill 重排流程”的纪律。
2. **没有“重复纠正 → 机制”的升级阶梯**：产品是方法库，**它自身就是 encode-lessons 的产物**，但正文没有把“一次性 → skill/lint → 系统性问题”作为可用判断；执行计划明确“不建 registry/框架”，因此需要把阶梯限制在“本次任务可达的最强机制（在已接受可靠性级别内）”。
3. **没有 reflect/偏好提取方法**：从会话/纠正中提炼 durable guidance 是 A/Voice 的弱项；`intent-voice.md` 只记录“人类接受记录（决定、范围、条件）”，没有“反复纠正如何变成结构”的流程。
4. **没有偏好置信度与 contradicted 处理**：workflow-from-chats 的四档置信（strong/medium/weak/contradicted）可直接用于产品“事实/推断/未知”与接受记录，避免把单次纠正升格。
5. **没有隐私/边界纪律**（不跨工作区读 transcript、不暴露私有内容）：产品未涉及，但吸收时应写入边界。

为何值得吸收：A/Voice 与 Driver 都需要“从人类反馈到持久结构”的闭环，且产品本身已在用该纪律（吸收流水线）；补上操作面可减少同一纠正重复三次。风险是过度机制化，见本组处置。

### 5) 拟处置与载体

- 拟保留：原则名接口的“引用必须伴随被改变的决定”检查；不枚举 skill 重排流程；encode-lessons 的三步升级与 strongest-mechanism 排序（缩到“本次任务可达”）；reflect 的“不自动应用 + 用户批准 + 结构强制检查”；workflow-from-chats 的 preference atom 与四档置信（尤其 contradicted 必须先问）。
- 拟改变：
  - `reflect`/`workflow-from-chats` 的 transcript 路径与多模型/多 subagent 调用改为“可读的会话记录/证据源”通用说法；不要求固定 reviewer 数；
  - “Backlog 自动进 devex tracker”去掉（产品不内置 tracker）；
  - encode-lessons 加入 proportionality 条件：“只编码本任务内已确认重复且收益可指出的规则；不因假设未来建框架”；并把“最强机制”的边界限定为产品已接受的可靠性级别。
- 拟删除：pstack 模型 slug、`create-skill` 具体工具、`/reflect` 命令名（保留触发语义）。
- 载体：方案 1（推荐）新增支持文件 `methods/guide-lesson-promotion.md`（重复纠正→机制的升级与边界），`profiles/driver.md` 与 `profiles/intent-voice.md` 按需入口各加一行；方案 2 只改 `intent-voice.md` 的“人类接受记录”段（代价：无法覆盖 Driver 的程序性重复）。
- **与执行计划的张力（请 gate 特别注意）**：本组很容易被读成“建 registry/平台”。本包建议吸收时**不新增任何持久机制载体**，只写判断程序与边界；encode-lessons 的示例用产品已有对象（Profile 段落、Charter 字段、方法正文）而非新工具。若 gate 认为风险过高，可只吸收 workflow-from-chats 的置信度与 contradicted 规则（最小切片）。

**平台耦合/依赖**：transcript 格式与工具全去；仍依赖真实可读的会话记录（若 inaccessible 则降级为 digest 并说明）。

### 6) 正文草稿与验证方案

```
从纠正到结构（草稿，proportionality 版）：
1. 抓到自己第二次写同一指令、或同一失败模式第二次出现。
2. 判断一次性还是 pattern；一次性只记录，不建机制。
3. pattern 时选本任务可达的最强机制：不可表示的状态 > lint/banned API > 既有 canonical 入口 > runtime check > 更突出的文本+失败例子。
4. 编码后删除原指令；不能编码就在这里说明为何需要判断。
5. 引用原则/方法名时必须同时说明它改变了哪个决定；没有决定就不算应用。
6. 从会话/纠错提取偏好时给出置信（strong/medium/weak/contradicted）；contradicted 先问不写。
边界：不因假设未来建平台；不改冻结责任；偏好提取不暴露私有内容，不跨工作区取材。
```

验证方案（未执行）：用一次真实纠正场景，检查：(a) 是否区分一次性/pattern；(b) 编码机制是否落在本次任务可达的最强级别且删除了原指令；(c) 引用方法名时是否指出被改变的决定。反例：把一次性纠正写成新方法；或只记录不路由。边界：不要求每次纠正都编码；不与“不建 registry/框架”冲突。

---

## MG-4 上下文重建、解释与状态报告（A / Voice / Driver）

### 1) 机制与触发情境；源锚点与已读/尚缺

| 源锚点 | 已读 | 尚缺 |
| --- | --- | --- |
| `pstack/skills/principle-guard-the-context-window/SKILL.md`（全文） | 全文 | 无 |
| `pstack/skills/recall/SKILL.md`（全文） | 全文 | 无 |
| `pstack/skills/teach/SKILL.md`（全文） | 全文 | 无 |
| `pstack/skills/poteto-mode/playbooks/session-pickup.md` | 包 1 MG-8 已读 | 无 |
| `cursor-team-kit/skills/weekly-review/SKILL.md` | 全文 | 无 |
| `cursor-team-kit/skills/what-did-i-get-done/SKILL.md` | 全文 | 无 |
| `pstack/docs/guide/03-understand.md`（recall/teach/session-pickup 分工）、`07-overnight.md`（轨迹+审计） | 已读 | 无 |
| `continual-learning/hooks/*.ts`、`skills/*` | **未读** | 归 a4/后续（A 记忆机制，但强 hook 耦合） |

触发情境：上下文将满（大输出、长文件、重复读、fan-out 规划）；开始或恢复工作前要重建最近工作上下文（recall）；人类要真正理解某物（teach）；需要周/阶段回顾或状态更新（weekly/what-did-i-get-done）；夜间/长运行后人类审计。

### 2) 操作、成立条件、失败模式、反例/例子

**guard-the-context-window**：上下文窗口有限且 session 内不可再生；每个 token 都要值。模式：隔离大 payload（冗长输出、截图、大文档交给子代理；主上下文只留 summary）；频繁使用的内容保持内联（模板与每次调用用的引用放 skill 文件，不拆成每次都要读的文件）；给 phase 定大小与 scope（限制每 phase 文件数、设回合预算、计入机制成本）。

**recall（操作要点）**：开始/恢复工作前重建用户最近工作上下文，交回 tight capsule：现在在哪里、接下来做什么。两个记录：自己的 chat history（你做了什么、决定了什么）；共享记录（同一 code 在别的名字下发生的事：用户持续报告的症状、上线又回滚的修复、仍在 prod 触发的错误）。分类再路由：一个具体旧 chat 要恢复 → session-pickup；把习惯变 durable skill → automate-me；人类可读工作总结 → 另一任务；用户已给完整状态 capsule → 直接用、跳过挖掘。Lock scope：pin 时间窗（默认最近 7 天）、命名主题、工作区（默认当前；未经要求绝不读别的项目 transcript）；把 scope 说回去；绝不悄悄把 “all” 变 “recent N”。Fan out 到自己 chat history（跨片并行、按真实修改时间 `ls -t` 排序而非 UUID 名、先 grep 主题再只读匹配 chat 的相关区域、跳过当前 chat 与明显噪声如 subagent/eval/test chat；每块同 schema：topic、用户目标、决定、open threads、struggle 与纠正、artifact，各带 chat UUID；一两个 chat 就直接搜，不 fan-out；raw transcript 留在子代理，主线程只拿 findings）。**只要主题命名了 feature/file/subsystem/area/bug 就默认 sweep 共享记录**（不是判断选择；“my work on X” 不豁免）：交给 why 的 source investigators，但把问题从“为什么这样构建”转向“现状、试过什么没成立、用户还在报什么”；按源并行、沿用 why 的姿态（一源一 investigator、null 也是 finding、缺 MCP 就说）；并入 brief。只有纯活动回顾且无命名目标（“what did I do this week”）才跳过。对照 live state：mining/sweep 浮出的 PR/branch/ticket 用 git/gh 核对；答案取决于 agent 实际做了什么（跑过什么工具、读过什么文件、撞过什么错）时读完整 transcript 而非裁剪副本。**输出契约**：Capsule（≤5 条，这个工作是什么、总体在哪）；Threads（一行一条，前缀恰一个状态 tag：`[merged #N]`、`[open PR #N]`、`[in flight <branch>]`、`[verified, uncommitted]`、`[reverted #N]`、`[planned, not started]`；没 tag 就没完成，必须打）；Problems（≤5 条，反复出现的；含用户持续报告的症状与上线又回滚的修复，让下一次从上次失败处开始）；Next move（一条最有用、具体）。相邻 feature/ticket 除非阻塞否则不进；capsule 与 thread 超屏先砍细节不砍 thread；引用 chat UUID 与共享源；公开输出前 sanitize 私有上下文。

**teach（操作要点）**：目标是“人真正理解”，不是改变任何东西；跑 how + why 并把发现织成一篇朴素说明；**保持 why 的 confidence language**（它的 hedge 是 finding，不是文风）。步骤：决定对方应带走几件事（从其提问动机与已知读起，不问测验；跳过显然已知的，把深度放在问题处）；让 how/why 做功不重做（读代码定向后跑两者，按问题大小配比；why 默认窄，把收窄写进请求本身）；以朴素定义开头（用高级工程师的说法讲这是什么、有通用名就说），再绑定当前案例，然后 how/why/edge cases；每个部分讲清它解决的问题与实际工作方式；当“人怎么做这件事”能让理解落地时按人操作顺序走；列 function/constant 是 reference 不是 teaching；**不要打印 framing labels**（“one idea to hold onto”“TL;DR”等）；先给最小完整答案（一两句）再停，等对方要更多；保持对话而非演讲、无 quiz、无 pacing theater；show don't only tell，图示**逐张搭建**（三个以上活动部件不要一张图全画：先 A→B，重画加 C，再重画加返回边/下一块；一张全量图、尤其放最后，是 reference 不是 teaching；mermaid 适合流程/结构，空间类想法（布局、重叠、滚动位置、before/after）用图像生成，marker-on-whiteboard 风格、短标签）；每个回复走 unslop（plain spoken English、tight not terse、具体机制不是比喻/预告、同概念一名到底、避免镜像句与奉承收尾）；**回复就是说明本身，绝不是关于你做了什么/交付了什么**。

**weekly-review / what-did-i-get-done（回顾报告纪律）**：从 repo config 取 git user email（缺失就要求先设置）；收集最近 7–10 天（或用户指定窗口）在 primary branch context 的 authored commits；**排除 merge commits 与未提交改动**；把有意义变更归成 2–5 条简明 bullet；每周版另加分类段（likely bug fixes / tech debt / net-new）；**只基于 commit 历史与 diff 下claim**；省略 cosmetic-only（格式化、import、minor rename）；**不得推断意图或动机，只按功能描述**；输出含实际使用的 date range。

**成立条件/失败模式**

- guard-context：大 payload 真的可隔离；频繁引用有稳定所在。反例：把每次调用的模板拆成要读的文件（源文点名）。
- recall：有可读会话记录；scope 明确；共享记录有可访问源。反例：安静地把 “all” 变 “recent N”；主题命名 feature 却只挖自己 transcript（源文说那是默认，不是判断）。
- teach：对方确在学；how/why 可运行。反例：把说明变成工作汇报；一张全量图当 teaching；把 why 的 hedge 去掉（会伪造确定性）。
- weekly/what-did：有 authored commit 历史；无则先要 email/窗口。反例：把 merge commit 与 cosmetic 混入；从 commit 推断动机；不写实际日期范围。

### 3) 判断位点与 Profile 调用

| 位点 | 专业 concern | 何时调用 | 由哪个 Profile 提议 |
| --- | --- | --- | --- |
| A/Voice：重建上下文、解释取舍 | 目标/沟通 | 开始/恢复工作、人类要理解变更 | `intent-voice` |
| Driver：上下文预算与序列化 | 程序性 | 大 payload / fan-out / 多阶段 | `driver` |
| F：共享记录扫查与 live 核对 | 证据 | recall 的状态核对 | `evidence-evaluation` 支持 |

### 4) 当前产品锚点、覆盖、缺口、为何值得吸收

- `profiles/intent-voice.md` `## 心智模型`：“Voice 连接人与专业判断：对齐 Delegation Envelope，解释取舍的行为、成本、风险与承诺影响，读回理解，记录接受决定。”
- 同文件 `## 关键问题`：“哪些是观察事实、哪些是推断、哪些还是未知？哪个未知会改变方向？”；“需要人类决定的是哪一个选择，用行为/成本/风险/承诺怎么表达才可理解？”
- `profiles/driver.md` `## 心智模型`：“只留在逻辑编排层”。
- `profiles/evidence-evaluation.md` `## 关键问题`：“结果能否被另一个会话按材料复现？”
- `docs/WORKFLOW-INTENT.md` §4：“更深层判断需要人类决定时，必须翻译成可理解的行为、成本、风险或承诺”。

已覆盖：Voice 的解释职责与事实/推断/未知；人类可理解性要求；Driver 的逻辑编排边界。

具体缺口：

1. **没有上下文重建方法**：产品有“复用仍适用的结论”，但没有“开始/恢复工作前先重建用户视角的现状（capsule/threads/problems/next move + 状态 tag + 共享记录默认扫查）”。
2. **没有“解释给人听”的操作面**：Voice 要翻译，但无方法；teach 的“保留 confidence language（hedge 是 finding）”与“逐张搭建图示”“最小完整答案先行”“不打印 framing labels”是可直接复用的专业操作。
3. **没有上下文预算的机制成本意识**：guard-context 的“大 payload 隔离、常用内容内联、phase 大小与回合预算”是国内产品 Driver 组合的缺失面（注意与“进程/并发不属于本包”的边界：这里指注意力预算，不是 runtime）。
4. **没有历史报告纪律**：weekly/what-did 的“仅依据 commit/diff、排除 merge、不推断动机、省略 cosmetic、写明实际日期范围”可用于 A/Voice 的回到人类场景，防止把回顾写成叙事。
5. **没有“共享记录”概念**：产品提到“已有适用结论可直接复用”，但没有“同一 code 在别的名字下发生的事（症状、回滚、prod 错误）是默认证据源”。

为何值得吸收：A/Voice 的两个高频失败正是“恢复工作时靠记忆/最近一次对话”与“解释变成汇报”。这组全为纯方法层，且与已接受的“事实/推断/未知”和“可理解性”直接衔接。

### 5) 拟处置与载体

- 拟保留：recall 的输出契约与状态 tag、scope 纪律、共享记录默认扫查；teach 的 confidence-language 保留、图示逐张搭建、最小完整答案先行、无 framing labels；guard-context 的三条；weekly/what-did 的四条报告纪律。
- 拟改变：去 transcript 路径与工具名（改为“会话记录/共享记录”，不可读就降级并说明）；多 subagent fan-out 改为“按片分头读取，主线程只留 findings”；`/recall`、`/teach` 命令名去掉；不引入 `automate-me`/`session-pickup` 的产品依赖（session-pickup 已在包 1 MG-8）。
- 拟删除：模型 slug、`ls -t` 等具体实现（可作例子但不作规范）、任何把记录内容公开的默认行为（保留 sanitize 要求）。
- 载体：方案 1（推荐）新增 `methods/guide-context-and-briefing.md`（recall+teach+guard 合并为“上下文重建与人类解释”支持指南），`profiles/intent-voice.md` 按需入口加一行；weekly/what-did 作为 A/Voice 的一个小节（或在 Charter 例子里）。方案 2 把 recall 单独成方法、teach 单独成 guide（本包倾向合并，因两者共享“把专业状态翻译给当前人类”的目的）。
- 与 a4 的分工：continual-learning 的 hook/记忆机制（`hooks/*.ts`、三件套）在未读残余中，归 a4/后续；本包不评估其 runtime。

**平台耦合拆除**：transcript 路径、UUID 排序、`gh`/MCP 具体调用全去；仍依赖“有可读的会话记录与共享证据源”。

### 6) 正文草稿与验证方案

```
上下文重建 brief（草稿）：
Capsule（≤5 条：这是什么、在哪）→ Threads（一行一 tag：merged/open/in-flight/verified-uncommitted/reverted/planned）→ Problems（≤5，含反复症状与回滚过的修复）→ Next move（一条，具体）。
纪律：scope 先说回去；主题命名了对象就默认扫共享记录；对照 live state；不安静缩小 scope；公开前 sanitize。

人类解释（草稿）：
先给最小完整答案；保留 why 的确定性分层（hedge 是 finding）；三个以上部件用逐张搭建图；不打印 framing 标签；解释本身是交付，不是工作汇报。
```

验证方案（未执行）：(a) 给一个冷却两周的真实主题，跑一次 recall 并对输出台账检查：capsule ≤5、thread tag 完整、problems 含回滚、scope 未缩水；(b) 用一次真实变更做 teach，检查是否保留置信分层、是否给最小完整答案、图示是否逐张；(c) 用一次周回顾验证只从 commit/diff 取证、无动机推断。边界：无会话记录/共享源时降级并声明；不要求每次任务都做 brief；teach 不改变任何对象。

---

## MG-5 共享写面与幂等（Driver / D / E 交界）

### 1) 机制与触发情境；源锚点与已读/尚缺

| 源锚点 | 已读 | 尚缺 |
| --- | --- | --- |
| `pstack/skills/principle-separate-before-serializing-shared-state/SKILL.md`（全文） | 全文 | 无 |
| `pstack/skills/principle-make-operations-idempotent/SKILL.md`（全文） | 全文 | 无 |
| `orchestrate/skills/orchestrate/references/handoffs.md`（“handoffs 唯一通道/relay/continuous motion”） | 包 1 MG-7 已读 | 无 |
| `pstack/skills/poteto-mode/playbooks/feature.md` step 3（共享可变状态默认拆分） | 包 1 已读 | 无 |

触发情境：并发 actor 可能写同一文件/branch/key/state object；设计命令、生命周期步骤或处理循环，面对 crash、重启、重试；多 worker 在同一 repo 输出。

### 2) 操作、成立条件、失败模式、反例/例子

**separate-before-serializing-shared-state**：并发 actor 可能共享可变状态时，先问它们是否真的需要同一个可变对象；不需要就**消除共享**。共享为真时用结构强制串行（lockfile、顺序 phase、独占所有权）。**指令与约定不是并发控制。** 模式：① 识别共享可变状态（双方都读写的文件、都 push 的 branch、既定义又消费的 API）；② 默认消除共享写目标：“do these actors need one canonical object, or are they publishing independent facts?” 给每个 actor 自己拥有的 file/key/branch/state 目录，只在 read/reporting 边界合并；**两个 worker 把各自的 `lastX` 字段写进同一个 `state.json` 仍是共享突变；`indexer-state.json` + `metrics-state.json` 不是**；③ 只有当“一个共享写目标”是真实不变量时才结构化串行（lockfile、顺序 phase、单写者 actor、原子 compare-and-swap）；**把“我们需要一把锁”当作要被检查的设计 smell，而不是默认答案**。

**make-operations-idempotent**：让操作收敛到正确状态，不管跑几次、从哪开始；每个突变操作回答：“跑两次会怎样？上一次跑一半崩了会怎样？” Why：命令、生命周期操作与处理循环运行在 crash/restart/retry 常态环境中；部分状态改变下次结果 → 每次重启变成调试 session。模式：convergent startup（扫既有状态、清 stale artifact、adopt live session）；content-based cleanup（按内容等价比较，不按创建顺序）；self-healing lock（PID 基 stale lock 检测）；idempotent scheduling（失败工作干净 respawn、每周期后重新生成新输入）。**三问测试**：连续跑两次会怎样？上次在每个可能点崩掉会怎样？重执行是否收敛到同一末端状态？**任一答案是“取决于留下什么状态” → 需要 reconciliation 步骤。**

**成立条件**：存在并发写者或 crash/retry 环境；写目标可被拆分或被结构性串行。

**失败模式/反例**：给每个 actor 自己的文件但仍在 read/reporting 边界前互写；用“我们需要锁”直接开始加锁而不先问共享是否必要；两个 worker 各自 `lastX` 字段进同一 state；指令说“不要同时写”当作并发控制；操作“跑两次会重复副作用”；清理按创建顺序而非内容等价。

### 3) 判断位点与 Profile 调用

| 位点 | 专业 concern | 何时调用 | 由哪个 Profile 提议 |
| --- | --- | --- | --- |
| Driver：并行写集与单写者集成 | 程序性 | 多写者、共享文件、repo 级集成 | `driver`（`## 关键问题` 已有此问） |
| D：共享状态的结构性拆分/串行 | 架构/持久化 | 共享对象是真实不变量时 | `technical-planning`（a4 侧） |
| E：命令/循环的幂等设计 | 实现/运维可靠性 | 崩溃/重试常态 | `implementation`（a4 侧） |

### 4) 当前产品锚点、覆盖、缺口、为何值得吸收

- `profiles/driver.md` `## 关键问题`：“并行写者的写集是否明确？共享文件是否单写者串行集成？”
- `profiles/driver.md` `## 心智模型`：“只在逻辑编排层：进程、并发、队列、锁、重试等 runtime 机制不属于本包职责。”
- `authority/RESPONSIBILITY-BACKBONE.md` §2：“下游能找到本次相关、适用且足够的结论、条件、依据、决定责任与接受状态”。
- `profiles/technical-planning.md` `## 心智模型`：“私有代码也可能影响共享预算、安全或资源边界”。

已覆盖：Driver 要问写集与单写者；runtime 机制不进本包；共享边界属 D。

具体缺口：

1. **Driver 的“写集是否明确”没有“先消除共享、再考虑锁”的判断程序**；现有只到“单写者串行集成”，缺“共享写目标是否必要”的前置问题。
2. **没有幂等的三问测试与 reconciliation 判据**：产品在 D/E 交接里没有“跑两次/半崩/收敛”的检查；这对任何有重试或恢复面的承诺都相关（且与 Backbone 的“可恢复性”判断衔接）。
3. **缺“指令不是并发控制”的明确反例**：产品在委派中常出现“不要并行写同一文件”的措辞，但没有指出约定不足以保证。
4. **与 runtime 边界的张力**：产品明确 runtime 机制不属本包职责；本组若吸收，必须只保留“拆分共享 / 设计收敛”的判断，不引入锁实现、队列、重试机制。

为何值得吸收：这是 Driver/D 交界最高频的协作失败面；吸收后能减少“并排 worker 互相覆盖”的事故，且不要求新 runtime。但由于与 runtime 的张力，建议作为**窄规则**而非完整方法。

### 5) 拟处置与载体

- 拟保留：消除共享优先、锁作为 smell、写目标拆分的正反例（`state.json` vs 各自 state 文件）、三问幂等测试与 reconciliation 判据、“指令不是并发控制”。
- 拟改变：把 `lockfile/compare-and-swap` 等实现留作例子并标注“由 D/E 与 runtime 决定，本包只判定是否需要”；不把本组扩成并发方法。
- 拟删除：与 runtime 实现相关的任何具体机制。
- 载体：方案 1（推荐）在 `profiles/driver.md` 的 `## 关键问题` 增补一问（“共享写目标是真实的还是可以拆分？”）并在 `methods/` 上加一个**短**支持文件 `methods/guide-shared-write-and-idempotency.md`；方案 2 并入 `methods/cross-module-design.md`（代价：该文件属 D 且已声明 Method owner，吸收后会改变其责任面）。本包倾向方案 1。
- 与 a4 的边界：幂等的实现面（lifecycle/命令/循环的具体设计）转 a4；本包只保留判断条件与反例。

### 6) 正文草稿与验证方案

```
共享写目标检查：
1. 列出双方都读写的对象（文件/键/branch/state 目录）与“各自发布独立事实”的对象。
2. 默认消除共享：各自拥有写目标，只在读取/报告边界合并。
3. 只有“一个共享写目标”是真实不变量时才结构化串行；把“需要一把锁”当 smell 再检查一遍。
4. 指令/约定不是并发控制。
幂等测试：跑两次？每个可能点崩掉？重执行是否收敛同一末端？任一“取决于遗留状态”→ 需要 reconciliation。
```

验证方案（未执行）：(a) 对着一次真实多写者场景，按检查判定是否可拆分、拆分后是否仍在边界共享写；(b) 对一个可重跑操作做三问测试，记录发现。边界：本组不引入锁/队列实现；与 runtime 相关的方案由 D/E 负责。

---

## 8. 包级综合观察（供 gate，不是裁定）

1. **本包五组的共同价值**：把 pstack 的“原则词汇”转成产品可用的**判断程序**，而不是复制 23 条文本。它们补的是包 1 之外的 F（执行证明）、B/C（范围与读者负担）、A/Voice（上下文与解释）、Driver（共享写面）四个薄弱面。
2. **与包 1 的去重**：`attack-the-premise`、`never-block`、`model-the-domain`、`boundary-discipline`、`interrogate`、`thermo-nuclear`、`show-me-your-work`、`handoffs`、`advisor`、`ralph-loop` 均已在包 1 记录，本包不重复；仍有交叉的只有 `show-me-your-work`（包 1 轨迹/stdout 已覆盖）与 `session-pickup`（包 1 MG-8），本包只引用不重述。
3. **风险模式**：
   - MG-3 的 `encode-lessons-in-structure` 与 MG-2 的 `foundational-thinking` 都可能被读成“建平台/框架”，与执行计划“不建 registry/框架”和项目 AGENTS 的 robustness proportionality 有张力。本包的建议是把它们限定为“本次任务可达的机制 + 已接受可靠性级别”，不新增持久载体。
   - MG-2 的 `outcome-oriented-execution` 的“中间破坏可接受”若脱离 guardrails 会变成大爆炸重写的许可；本包建议只在 a4 落地时保留 guardrails 四条。
   - MG-1 的 `tdd` 若被写成 mandatory gate 会与执行计划“去掉无适用条件的强制 ceremony”冲突；本包保留其 cheap-path 门槛与“prefer no test over a bad test”。
4. **建议 gate 的优先顺序（供参考，不构成裁定）**：MG-1（F 证明纪律，缺口最实）≥ MG-2（B/C 范围与形态）> MG-4（A/Voice 上下文与解释）> MG-3（学习编码，风险高、可小片吸收）> MG-5（窄规则，注意 runtime 边界）。
5. **与 a4 的交接清单**：`outcome-oriented-execution`、`migrate-callers-then-delete-legacy-apis`、`type-system-discipline`（a4 已认领）、`boundary-discipline`（包 1 记录为 a4 候选）、`make-operations-idempotent`/`separate-before-serializing` 的实现面、`perf-issue`/`hillclimb`/`runtime-forensics`/`trace-forensics`/`visual-parity` 实验方法、`build-the-lever` 的具体工具形态、`continual-learning` 的 hook 与记忆机制、`setup-pstack` 配置。

## 9. 未读残余（本包未覆盖；不假装已评估）

- pstack：`skills/arena`、`skills/swarm`（本包只从 10-recipes 转述其分工，未读 SKILL 正文）、`skills/no-comments`、`unslop`、`technical-writing`、`typescript-best-practices`、`make-bot-ui`、`automate-me`、`bro`、`setup-pstack`、`skills/principle-type-system-discipline`；`docs/guide/00、01、02、04、05、09`；`skills/poteto-mode/references/*`、`scripts/*`；`playbooks/` 未读部分（包 1 已列）。
- cursor-team-kit：`agents/*`、`rules/*`、`check-compiler-errors`、`control-cli`、`control-ui`、`deslop`、`fix-ci`、`fix-merge-conflicts`、`get-pr-comments`、`loop-on-ci`、`new-branch-and-pr`、`pr-review-canvas`、`run-smoke-tests`。
- 其余同仓目录（thermos agents、orchestrate scripts/schemas/prompts/tests、advisor hooks/agent、ralph-loop 余部、continual-learning、create-plugin、cursor-sdk、agent-compatibility、teaching、docs-canvas、pr-review-canvas、grok-voice、third_party、schemas/、scripts/）与包 1 的 §9 相同，归 a4/后续。

## 10. 包内自检（机械项，非专业裁定）

- 源 pin 与路径：均为 `ecc249f1e306fc64ddf83c7bed16cacf7c2239db` 下实际存在的路径；
- 未修改产品/他人文档/registry；未 commit；
- 每组含 6 项要求；所有验证方案标注未执行；源说法标注为原文描述。
