看一下该agent的反馈，信息量很大，你来分析和落盘，然后向我汇报测试结果，先不向下推进：
已完成本轮只读冷读。以下是结论。

---

## 0. 现场事实（本轮实际读数）

| 项 | 读数 |
| --- | --- |
| UCBIP cwd | `/Users/yuantian/Developer/ekunai/Unified-Customs-Bonded-Intelligence-Platform`（即本 session 工作目录） |
| UCBIP HEAD | `7fc94e4a483cf6b1d8add214d7dbe9a1d42b7f76`（`main`，2026-10-01 14:06:23 +0800，`docs(governance): sync current control to the tool-seal implementation window`）；tracked tree clean，仅 2 个未跟踪根 HTML 导出 |
| PW worktree | `/Users/yuantian/Developer/tim-professional-workflow/.worktrees/night-2026-10-01`，HEAD=`cf107522…`（验收 commit），status 仅 `?? scan.js`；**未 checkout、工作树当前文件未被当作交付版本** |
| 固定交付 commit | `205b831ecb9ba4e79481a08e6b23f7159dca4113`（2026-10-01 16:15:25 +0800） |
| 核心 subtree | `11e6e3772b6bc0e17259c932b0c0dcabb030a133` —— 实测**就是** `205b831:professional-workflow` 这棵树的 oid，19 文件 |
| 验收记录 | `cf107522…:docs/overnight/2026-10-01/M6-FINAL-ACCEPTANCE.md`，存在且可读 |
| `scripts/render_current_state.py --check` | 本轮实跑（只读模式，检查后 tree 仍 clean）：**0 FAIL**，R1/R3–R10 全 ok，R6 读到 9 行绑定、as-of `2026-10-01T06:04Z`、sha256 `83572fd4…dc644b` |

所有 PW 侧内容均以 `git show <fixed-commit>:<path>` 读取，未 checkout、未写文件、未跑生成器写模式。

---

## 1. 这套 workflow 实际提供了什么

**它提供的是"判断配置 + 绑定表单 + 装配顺序"，不是流程引擎。**

核心是《RESPONSIBILITY-BACKBONE》冻结下来的六类判断责任 A–F（Intent/Outcome、Behavioral Contract、Domain Semantics、Technical/System Design、Implementation、Verification）加两个连接件：**Voice**（人机接口，负责把取舍翻译给 Owner 并记录接受）和 **Driver**（内部逻辑路由，负责识别触发、找有委托的责任方、检查程序足够性、管理版本与召回、按已接受规则执行关闭）。六者共享的唯一交接纪律是：下游能找到**本次相关、适用且足够的**结论、条件、依据、决定责任与接受状态；并且明确写着 **契约接受 ≠ 证据验证 ≠ 动作授权 ≠ 任务关闭**，四件事各有来源，互不推出。

`profiles/` 是这六类判断的可复用"心智模型"包（常见误区 + 关键问题），`charters/template.md` 是把它绑到一次真实任务上的表单（委托来源、对象范围、已接受输入、绑定方法、可决/不可决、交付、独立性、召回、验收/验证/行动/关闭分开写），`methods/` 是**被显式绑定才会生效**的方法正文，`authority/RESPONSIBILITY-BACKBONE.md` 是责任边界投影。装配方式字面就是 `cat`：Profile → 需要的 authority 上下文 → 填好的 Charter → 绑定的方法文件 → 任务输入，产出**启动提示文本**（`README.md` §Use、`charters/README.md` §Assembly）。

**一个团队怎么用它**：不把它当编排器，而是当"每次开一个实例前的判断配置与授权表单"。先按"这次要下哪类判断"选 Profile（`profiles/README.md` 的选择表），再把这次**真实存在的**委托、输入、对象、写集、评价者、召回路径填进 Charter 对应字段，只绑定本次用到的方法，拼成该实例的启动文本；实例之间靠短消息 + 持久产物指针交接，冲突按"返回真正拥有该边界的 authority"路由。

**必须由项目自身提供的东西**（package 明确不拥有）：

- **一切授权**：任务图、优先级、写窗口、派工、`main` 单写者、角色↔承载绑定；
- **接受权与关闭规则**：谁评价、谁接受、谁关门、finding 是否阻断；
- **状态与证据的权威载体**：每节点的权威状态块、证据索引、收据、生成投影；
- **独立性资源**：真实独立的挑战者/评价者是谁；
- **方法正文与任务适用的绑定判断**：Profile **不激活**方法，Charter 名字本身不构成授权。

三条最容易误用的边界：① `profiles/README.md` 反复写着"选择预设 ≠ 授予权限"、"不产生任务决定权"；② A–F 是**判断函数索引，不是执行序号**，不要求六种固定岗位，也不用凑齐六份文件（可只调 E/F，可多次返回 B/C）；③ Backbone 自述"**尚未实施或完成运行有效性验证**"，所以它是责任语言与召回语言，不是可执行流程。

**UCBIP 已经自己写下了这个 seam**：`docs/active/engineering-method-routing.md` 记着外部 `tim-professional-workflow` 只承载方法正文、"**上游只提供方法正文**"、"**方法不产生权限**"，角色/任务图/审查循环/验收仍由 `multi-agent-development-principles.md` 定义。所以正确接法是"包提供判断与表单，UCBIP 提供权限与状态"，**不是**在 UCBIP 里再立一套角色名册或第二状态源。

---

## 2. 候选下一任务与选择依据

我把 UCBIP 当前所有开放节点过了一遍（控制记录「暂停状态」「当前顺序」「本波节点表」+ 生成区的开放节点表 + `## Now` + `## Decisions still needed`）。

**强势候选：`NATIVE-MSG-STREAM` 的"最窄服务端消息关联切片"（设计 → 独立方案门这一段）。**

选择依据，逐条可核：

1. **它是卡的显式开放状态**：`docs/tasks/2026-09-30-native-message-stream.md` 的 `CARD-STATE`（r6）phase=`候选冻结/修复中`，`next_or_blocker` 写明 R1 裁定 = 候选 `80618e55…` 不得合并，转最窄切片；生成区的开放节点表里它是唯一"**等谁=—**、有明确下一步"的开放节点。
2. **授权来路可追**：Owner 2026-09-30T12:5xZ R1 裁定授权了这条最窄切片（卡上有 checkpoint 与裁定 locator）。
3. **下一步具体到可开工**：Designer 定 owning seam / 字段生命周期 → 独立方案门 → 实施/审查/验证。
4. **四类依赖准入是"当前可得"而不是"已关闭"**：卡的四类依赖表写"接口冻结=无（设计未冻结）·写权释放=无（本阶段零产品源码写权/零写集）·资源可用=Designer 隔离 scratch + 离线 mapping/cursor proof（不启平台栈、不新增 Provider 调用）·证据资格=call2 探针已托管"。也就是说**当前合法动作恰好就是设计与门，而不是实现**。
5. **即时性**：Owner 的 R1 判词自身给出了"不做/不做/不做/必须 fail-closed"的硬边（不给全局生成序、不建通用排序、不按文本/计数/freshness 猜归属、不重定义 durable 回答选择），且独立门必核清单七条已经写成可核条目。
6. **相关源码/证据锚真实存在**（我按引用回源核到）：`tools/pi-server/pi-service-rpc.js`、`tools/pi-server/pi-rpc-runtime-manager.js`、`api/platform/execution.py`、`frontend/unified/src/api/contracts.ts`、`frontend/unified/src/components/UnifiedShell.tsx`（`replyBaselineRef` 邻近）；分支 `feat/native-msg-0930` 仍在（worktree 卡片称 clean at `eadd2c77`）。

**否掉的其它方向与原因（不是"没发现"，是逐个否掉）**：

- **TOOL SEAL 候选的 review/verify/merge**——**正在飞**。证据目录 `.agent-local/evidence/tool-seal-1001/` 的 verify/review 文件最新 mtime 为今天 **17:51**（我读表时 17:50 左右），且存在 `fix/toolseal-1001-classification-harness`、`verify/toolseal-combo-B-H`、`verify/toolseal-combo-B-H2` 等分支；`M6` 只读插进来只会撞车。
- **`ARCH-03`**（需要 plan-writer-03 交最小接口冻结计划）与 **`FINAL-PREVIEW`**（需要 Owner 定 Console 可用角色/字段/层级 + Driver 核写窗与产品字节冻结）——前置分别是"Driver 核新计划基线"与"Owner 决定"，**tracked 材料里看不到这两个前提的取值**，本轮无权补。FINAL-PREVIEW 还额外要求起栈前按 `docs/active/2026-09-19-v12-binding-switch-checklist.md` §4 前置执行。
- **三份固定候选 B8-2 `f77b0fc` / B8-2b `e265ba1` / B-1 `9e48356`**——已审 PASS、未合并，`## Decisions still needed` 明写要"仍按 Owner 既有停点"，**不得由对账自动放行**。没有可执行的下一个动作，只能等 Owner。
- **TODO 里的 D 类项（B6 / B8 / B14 / R13 等）**——`TODO.md` 自述是 backlog，个别条目自带"**实现中**"字样而 `current-release` 生成区当前**没有持有 `CARD-STATE` 的对应节点**。两者不一致时我按"卡状态块才是权威"处理 ⇒ 无法把其中任何一条当已授权任务来读（这本身记为第 4 节的一条歧义）。

**因此：如果要把这个候选变成真正可派的工，当前缺的输入是**（我不用猜测补上）——

- 该切片的**写权窗口记录**（卡当前写的是"零产品源码写权/零写集"，现行顺序里只列了 TOOL SEAL 实施窗）；
- 具名 **Designer 承载**（绑定源里 `governance-designer`、`plan-writer-03`、`plan-writer-cards` 三槽当前**无承载者**）；
- Owner **R1 裁定原文**的可取回副本——tracked 侧只有摘要与 locator（`.agent-local/driver-native-0930/r1-identity-ruling-0930.md`，Owner 原文在 `/private/tmp/…`）；**"/private/tmp" 不在 Git 里，路径被记录不等于字节可从 Git 恢复**；
- 一个**必须承认的固有歧义**：卡自己写着"「哪条 entry 算回答」是产品/owner 决定"，Designer/Driver 均不代决。

---

## 3. 针对该任务的最精简 multi-agent 计划（**本轮不执行**）

### 3.1 需要哪些实际实例，为什么

保持"一个共享边界只有两个真实主体"的最低配置：

| # | 实例（角色） | 为什么必须有 | 拟用 PW 判断映射 |
| --- | --- | --- | --- |
| I1 | **Designer**（新建，独立 scratch/worktree） | 产出一个 ≤半页的方案门材料 + owning seam 判定；这是 Owner 裁定里点名的第一道 | D（`profiles/technical-planning.md`，按需绑定 `methods/cross-module-design.md`） |
| I2 | **独立方案门实例**（fresh reviewer，**不得是 I1，也不得是卡作者**） | 门要判"最短路径 / 是否命中 §7.1 四类触发 / 证据锚是否足够继续"，这属于独立判断 | 设计挑战 + F 的证据取向（`profiles/evidence-evaluation.md`）；不要把它写成 Driver 的活 |
| I3 | **现行 Driver**（`driver-seal-1001` 槽位） | 只有它有写窗/派工/依赖与召回的路由权，并负责把结果落成卡状态 delta | PW 的 `driver` 是"逻辑路由入口"，**正好不占专业裁定权** |
| I4 | **Oracle（`w26:p1H`）** | 若结论需要改 adopted product contract 或无法确定身份，必须带最窄反例回它 | 保留 authority 的再解释者 |
| — | **Implementer / Verifier / Integrator** | **本阶段显式不需要**：无写集、无产品 diff、无 merge | 后续在门 PASS 后才出现 |

**不新建**：第二套名册、第二个 Driver、常驻安全/成本节点、以及任何新的状态载体。

### 3.2 每个实例的判断、委托依据、读什么、交什么、谁依赖它

**I1 Designer**
- *判断*：在**不改动 durable 语义**的前提下，determine 唯一 owning seam（哪一层是"哪个 raw Pi event 属于哪条消息"这一事实的 owner）、字段生命周期、调用者最小知识集合、回归面；**不**给全局生成序、**不**建通用排序、**不**按文本/计数/freshness 猜归属、**不**重定义 durable 回答选择。
- *委托依据*：**待确认**——Owner R1 裁定原文 + 一条 Driver 写窗记录。当前只有卡上的摘要与 locator。
- *读*：卡 `CARD-STATE` 与四类依赖表；`tools/pi-server/pi-service-rpc.js`（`mapAgentEventToSse` 现状只转 `text_delta`）、`pi-rpc-runtime-manager.js`（`parentId` 链、presentation readback 被截断 ⇒ 不可作 binding 输入）、`api/platform/execution.py`（canonical `(session_ref, entry_id)` 身份与 adoption cursor）、`frontend/unified/src/api/contracts.ts`、`UnifiedShell.tsx` 可见性与接管条件；已托管探针 `probe-call2.json` / `probe.mjs`；设计输入 `.agent-local/designer-native-0930/{plan-gate,design-report}.md`。**代码锚一律按实际 HEAD 重核，不按旧行号猜。**
- *交*：有界产物（seam 判定 + 字段生命周期 + 候选对照含"不重做"对照组 + 锚点 + 未决点 + 最小证伪实验），落 Designer 自有目录，**登记进卡**。
- *谁依赖*：I2 直接依赖；I3 依赖它以决定是否放行下一阶段；未来 Implementer 依赖门 PASS 后的 Plan。

**I2 独立方案门实例**
- *判断*：对**同一冻结对象**独立判 PASS/blocking，覆盖"最短路径、触发条件、证据是否真的够、召回条件是否可判"；**不**替 Owner 决定"哪条 entry 算回答"，**不**改方案。
- *委托依据*：Driver 按 `agent-delivery-contract.md` §1「plan gate 归属」配门资源（Designer 标条件 → Driver 派发前确认 → Reviewer 发现漏门可阻断）。
- *读*：只读 I1 冻结产物 + 卡 + 必要源码锚；**不读 I1 的推理过程当结论**。
- *交*：门结论 + 实际复核范围 + 残余；非阻断建议不自动重开轮次（两轮上限，超限按原则分流）。

**I3 现行 Driver**：先核委托来源与写窗、确认是否需门与配独立资源；把结果落成**该卡的 `CARD-STATE` delta**（唯一手写处），再经 Integrator 刷新生成投影。**Driver 不自任技术裁判**，也不得自报"风险不变/架构合理"。

**I4 Oracle**：仅在两条触发时进入——需要改 adopted product contract，或**身份无法确定**（按卡：带最窄反例回 Oracle）。

### 3.3 并行 / 串行

- 可并行：I1 内部的多条只读路径（三处源码 + 探针 + 卡）互不写；I2 的"门"可**同批**建立（材料与门对象并行准备），但**评审必须在 I1 冻结之后**，否则门评的是移动靶。
- **必须串行**：Owner 裁定原文再读 → I1 冻结 → I2 判定 → I3 落卡。四步中任一步产物字节变了，其后所有判定作废重来。
- **不得与其他线并行占位**：TOOL SEAL 的 review/verify 仍在跑（证据目录 17:5x 还在增长），串行位（重测试/资源）不得抢占；本阶段恰好也不需要起栈或跑重测。

### 3.4 什么发现会让计划改变 / 返回其他责任方（召回）

| 发现 | 去哪 |
| --- | --- |
| owning seam 需要改 adopted product contract，或身份无法确定 | **带最窄反例回 Oracle**（卡已写明） |
| "哪条 entry 算回答"必须被决定 | **Owner**（卡明写是产品/owner 决定，Designer/Driver 不代决） |
| 关联必须依赖**别的模块**变更，或 seam 落在私有 RPC/runtime 且与产品契约冲突 | 触发 §7.1 重新判定 → 重开 plan gate，Driver 重排写窗 |
| 需要新增测试基础设施/端口/Provider 调用 | 资源前提不成立 ⇒ **报未运行**，不扩权限（本阶段被禁：不启平台栈、不新增 Provider 调用） |
| 门 verdict BLOCK | **回原 Implementer/Designer**（修复回原作者），两轮上限后按原则分流给技术判断角色 |
| 上游裁定对象与 R1 裁定范围不一致（例如换了 base 或换了候选） | 停依赖工作，报 **Driver**，由它找该边界的 authority |

### 3.5 谁评价、谁接受、谁能关闭

- **评价**：I2（独立方案门）对该设计对象出结论；它**不得**是该对象的作者。
- **接受**：门的 PASS 是"可继续"的判据，不是接受权；**接受权来自实际委托**——本卡的上游再解释权在 **Oracle**，产品/范围接受在 **Owner**。
- **关闭**：本卡**自我声明"尚无可声明资格（未 merge、未收口）⇒ 不声明 settled"**。所以关闭必须由**有效委托指明的关闭规则 + 持有该权者**执行；当前可见的是 Driver 按已接受规则记录、Oracle 保留再解释、Owner 才是 product-level 关闭者。**缺关闭授权时 Driver 返回委托来源，不自创规则。**

### 3.6 输出如何落进 UCBIP 已有治理（避免新增竞争真源）

- 阶段 delta → **该卡的 `CARD-STATE` 块**（唯一手写状态处）；
- 生成可见性 → `current-release ## Now` / 重启图的 `role-binding`+`dag-table`，**只能由 Integrator 跑 `--write` 刷新，不手改**（本轮实跑 `--check` 0 FAIL，说明这条链目前是通的）；
- 证据 → raw 进 `.agent-local/evidence/<flow>/`，**至多一份 **sanitized receipt 落 `docs/receipts/2026/`，并加**一行** `docs/evidence-ledger.md`；
- 被接受的事实 → 其 owner 文档（产品行为→产品契约；架构→ADR；支持行为/资格→domain current-truth），由 Integrator 在**同一集成批**写入；
- **不建**：第二活 roster、第二 ledger、第二份回执式记账；`main` 保持单写者。

### 3.7 一个关键实例的 Charter 草案（仅 I1；未取得项留空）

```text
Instance Charter · 原生消息身份·最窄服务端消息关联切片 · 设计整备

- State:              candidate（未取得委托前不激活）
- Profile:            profiles/technical-planning.md（D）
- Instance:           <待 Driver 具名；绑定源 governance-designer 槽当前无承载者>
- 装配行:             cat profiles/technical-planning.md \
                          authority/RESPONSIBILITY-BACKBONE.md \
                          charters/examples/technical-planning-cross-module.md \
                          methods/cross-module-design.md \
                          <本次任务输入>

Task and delegation
- Task / outcome:     产出 ≤半页方案门材料 + owning seam 判定 + 字段生命周期 + 回归面；
                      使"同一真实 assistant message 最多一份可见正文、一条消息一个身份"在
                      不改 durable 语义的前提下可继续设计。Non-goals：实现、改产品契约、定义
                      "哪条 entry 算回答"、建通用排序/全局生成序、按文本或计数猜归属。
- Delegation source:  <待确认> = Owner 2026-09-30T12:5xZ R1 裁定原文 locator + Driver 写窗记录；
                      卡：docs/tasks/2026-09-30-native-message-stream.md（CARD-STATE r6）。
                      **记录既有授权，不新增授权。**
- Object scope:       read = 卡与四类依赖表；tools/pi-server/pi-service-rpc.js、
                      pi-rpc-runtime-manager.js；api/platform/execution.py；
                      frontend/unified/src/api/contracts.ts、components/UnifiedShell.tsx；
                      已托管探针 probe-call2.json / probe.mjs；设计输入
                      .agent-local/designer-native-0930/*。
                      write = 仅本实例自有 evidence 目录下新文件（父目录 <待确认>）。
                      **不写产品源码；产品源码只在独立 tree 的授权窗口内改动。**
- Accepted inputs:    <待确认>：Owner R1 裁定可取回副本；设计输入现稿 sha256；
                      探针托管件 sha256；卡 r6 的当前 base。
- Applicable methods: methods/cross-module-design.md（M4 接受正文
                      013659331c8c5f9f54b866b393972a03d7938773 / 30066c8b…bae6f；
                      M5 候选字节另有身份）。绑定方法不产生权限、触发条件或范围。

Work and limits
- Responsibility:     判断"哪个 raw Pi event 属于哪条消息"这一事实的 owner 在哪一层、
                      其字段生命周期与调用者最小知识；给出候选 seam 对照（含"不重做"对照组）。
- Delegated decisions: 候选 seam 的组织与呈现、证据锚的选择、最小证伪实验的设计。
- Preserve / do not:  保留 canonical `(session_ref, entry_id)` 身份与 adoption cursor 语义；
                      私有 binding cursor **不回写** durable adoption cursor；缺关联时
                      **fail-closed** 且诚实标注边界；保留 B1/B2/B3 回归锁。
                      不做：产品契约修改、身份语义发明、"哪条 entry 算回答"的决定。
- Tools and actions:  只读本地源码与已托管探针；离线 mapping/cursor proof。
                      **不启平台栈、不新增 Provider 调用、不跑重测试、不 push、不 merge。**

Handoff and return
- Deliver:            冻结的设计产物（seam 判定 / 字段生命周期 / 候选对照 / 锚点 / 未决点 /
                      最小证伪实验 / 自测读数）+ 偏离项；登记进卡。
- Independence:       作者 = 本实例；独立挑战与门判定 = 另一实例（不得是作者，也不得是卡作者）；
                      结果评价在实现后由另一实例承担（本阶段不发生）。
- Recall:             ① 需要改 adopted product contract 或身份无法确定 → 带最窄反例回 Oracle；
                      ② "哪条 entry 算回答" → Owner（经 Voice），Designer/Driver 不代决；
                      ③ 关联需跨模块变更或 seam 落在私有 runtime → 触发 §7.1 重判，回 Driver 重排；
                      ④ 需要新资源/端口/Provider → 报未运行，不扩权限。
- Acceptance:         本卡自述"尚无可声明资格（未 merge、未收口）⇒ 不声明 settled"。
                      接受权按有效委托：上游再解释 = Oracle；产品/范围 = Owner；
                      阶段落地由 Driver 记录、Integrator 串行写 main。
                      门的 PASS ≠ 接受 ≠ 动作授权 ≠ 关闭。
```

---

## 4. 冷读中真正遇到的歧义、断链、过重之处

**这些都是实测到的，不是我为了凑 review 造的。** 按"具体文件/小节依据"给。

### A. 跨仓引用链断（影响：任何"按引用回源"的动作）

- `adoption-examples/ucbip.md`（`205b831`）把 UCBIP 侧的**流程记录**指向 `docs/overnight/2026-10-01/PW-01-UCBIP-READBACK.md`，同一段又写 "The core package deliberately ships no downstream mapping"。实测：**UCBIP 仓库没有 `docs/overnight/`**（其 `docs/` 下是 `active/ adr/ contracts/ history/ receipts/ reference/ reviews/ tasks/ templates/`）。`docs/overnight/2026-10-01/**` 是 **PW 仓库自己的**目录（验收记录也在这里）。⇒ 两个仓库用了**各自独立、互不存在的日期目录约定**；带仓库标识的引用能解析，裸路径不能。
- 同文件 Charter 的 `Delegation source` 写 `Oracle disposition PW-01-DISPOSITION.md`，实际对象是 `docs/overnight/2026-10-01/PRO-AUDIT-1-DISPOSITION.md`（`PW-01-MAPPING-REVIEW.md` Check 1 缺陷 1 记的是同一处）。该 review 的 **post-fix** 表说这一处已 PASS 关闭（"now reads … full path on one line"），但我实际读到的 `205b831` 版本写的是 `docs/overnight/2026-10-01/PRO-AUDIT-1-DISPOSITION.md` —— **仍是不含仓库标识的相对路径**。这处（读者可能以为它指 UCBIP）值得记一笔；我只报事实，不自行改写。

### B. 方法名接口对不上（影响：**最可能被误用的一处**）

- UCBIP `docs/active/engineering-method-routing.md` §3 与 §2 触发路由表指名 `tim-professional-workflow` 承载 **`path-trace` / `blast-radius` / `design-compare` / `drive-preview`** 四个方法，并要求任务卡"**附 `.pi/skills/…` 路径**"。
- 固定版本的专业包实际正文只有三个：`local-defect-feedback-loop.md`、`cross-module-design.md`、`behavior-claim-evaluation.md`；`methods/README.md` 明确把 **`DESIGN-IT-TWICE` 与 parallel-agent 数量、idempotency/retention、`interrogate`/`code-review` 列为 deferred（"did not use"/"deferred"）**，全文**没有出现那四个名字**。`§5` 的补记说的也是"四个 skill 已于 2026-09-26 退役、改由外部 workflow 承载"。
- 同时 `§3` 要求附 `.pi/skills/…` 路径，而该路径在 UCBIP 内**已不存在**（同一文件自述已退役、改由外部承载）。
- ⇒ **冷读者按 UCBIP 路由表去外部包找 `path-trace`/`blast-radius` 会找不到；按包选方法又对不上 UCBIP 的触发词。** 这是真实的适配缝，落在 `engineering-method-routing.md` §2/§3 与 `methods/README.md` 之间，需要一次显式的名称映射（或由 Driver 在任务卡里按性质指名实际绑定的方法文件），而不是靠读者猜。

### C. 包内保留的早期候选状态文字（影响：冷读者可能读成当前状态）

- 包入口 `professional-workflow/README.md` 标题仍是 **"M5 integration candidate"**，而验收对象是 M6；正文自己补了一句 "M5 integration and M6 clean-package qualification remain in progress"，`M6-FINAL-ACCEPTANCE.md` 又说 "M5/core assembly and M6 controlled-copy coldstart/rollback retain their original scopes"。⇒ **标题与验收状态不同步**，读者必须读到段尾才不会当成 stale 标签。
- `charters/README.md` 标题 "M2 candidate"、`profiles/README.md` 标题 "M1 候选，未经独立验收，未提交"，并写着"方法入口为候选，待 M4 按来源归位后绑定"；而 `methods/README.md` 标题是 "M4 accepted references" 并给出 M4/M5 双 digests。⇒ **"待 M4" 标签残留在冻结 Profiles 里**，只有 `methods/README.md` 做了更正 —— 多一跳。
- `authority/RESPONSIBILITY-BACKBONE.md` 首行自述 "**尚未实施或完成运行有效性验证**"，与其被当作已接受冻结基线的地位并存。这三种"候选/接受/in-progress"文字同时在一个 19 文件包里，**没有单一的状态行**；`M6-FINAL-ACCEPTANCE.md` 才是唯一能定位交付状态的地方（含"Residuals retained"与 "Stop / next boundary"）。

### D. 装配"过重"与轻量并存

- `README.md` §Use 第 4 步与 `charters/README.md` §Assembly 给了**同一个 `cat`**，但示例里直接写 `path/to/current-task-input.md` 占位（`PW-01-MAPPING-REVIEW.md` Check 4 歧义 2 已记），且**没有 schema 校验器或权限引擎**（`charters/README.md` 自述 "the package intentionally has no schema validator or general permission engine"）。⇒ 装配是"文本顺序约定"，任何顺序错误不会被机械发现。反过来看这是刻意的（不新增机制），但冷读者要意识到**没有东西会替你把关**。
- Charter 有两种书写形态：`charters/template.md` 的 bullet 表单，与 `adoption-examples/ucbip.md` 里的 fenced `text` 块（字段名略有出入，如 `Acceptance` vs `Acceptance / verification / action / closure`）。**同义不同形**，如果将来要机械检查会很麻烦。

### E. UCBIP 侧的两条不一致

- `current-release.md` 生成区有一条 "**当前无持有 `CARD-STATE` 的节点**"，而同文件上方正文与重启卡都写着 TOOL SEAL **已过 card gate、Owner 已开实施窗**，且 `.worktrees/toolseal-1001` 实际存在、`feat/toolseal-1001` 上已有 5 个提交、证据目录 17:5x 仍在增长。两者可以并存解释（TOOL SEAL 的卡在**已忽略的本地路径** `.agent-local/oracle-0930b/tool-seal-1001/TASK-CARD-r2.md`，不是 tracked 载体、不进 `dag-table`），但**对一个只读生成区的冷读者，正出现的活动是不可见的**；这也意味着 TOOL SEAL 的状态每步只能靠 Driver 手写正文承载。⇒ 如果发生会话中断，**tracked 侧无法独立重建该线的当前相位**。
- `docs/TODO.md` 与卡状态存在**新鲜度差**：TODO 里 B6 写着"实现中（2026-09-24 夜，作者 `fe-0923-01`）"、B14 是"冻结未执行/下一优先"，但 `current-release` 的生成区里**没有任何 B6/B14 的 `CARD-STATE` 节点**。TODO 自述是 backlog，这不算错，但读者**不能**从 TODO 推断这些项在飞或在停。

### F. 角色模型双轨（**最容易误用的接口**）

- 专业包的角色词汇是 **A–F + Voice + Driver**；UCBIP 的角色词汇是**槽位制**：`driver / writer / reviewer / governance-designer / gov-implementer / plan-writer-03 / plan-writer-cards / project-partner / monitor`（`.agent-local/driver-0922/role-binding.tsv`，我**只读了 role 列与 as-of，未读 bearer 列**）＋ `Owner / Oracle / Verifier / Integrator / Designer / Implementer`。
- 两套词汇**没有映射表**（PW 的 driver profile 也不认 UCBIP 的 Integrator 槽）。既然 UCBIP 已经自述包"只提供方法正文、不产生权限"，那么正确用法是**把 A–F 当判断函数映射到既有槽位**；但如果有人照包里的 Profile 名去 UCBIP 立新角色，就会撞上 UCBIP 的"**不另建竞争活跃名册**"红线。这一条我在计划里按"映射不新建"处理，但**接口本身没有任何文字禁止误用**。
- 顺带：`.agent-local/driver-seal-1001/STATUS.md` 写着"`render_current_state.py --check`: R1 remains FAIL because the tracked role-binding projection is stale"（当时 05:25Z 阶段），而**当前** `--check` 是 **0 FAIL**（as-of `2026-10-01T06:04Z`，9 行）。⇒ 那是**已收敛的历史读数**，不是当前缺陷；但它说明"过期读数"在这个仓里是常态，读者必须自己核对 as-of。我把它记为**已收敛**，不当问题报。

### G. 关于"不可从 Git 恢复"的一条我要说清楚

本轮我读了 `.agent-local/` 下的若干**运行态**文件（`driver-seal-1001/STATUS.md`、`evidence/tool-seal-1001/**` 的 mtime 清单与命名、`role-binding.tsv` 的 role 列）。它们是**本地时间点观察**：路径与内容不在 `7fc94e4a` 里，被记录≠可从 Git 恢复。**我没有把它们的内容当作 tracked 权威**，只在"当前是否在飞"这一件事上作为运行态证据使用。同理，PW 侧 Owner R1 裁定原文在 `/private/tmp/…`，tracked 侧只有摘要与 locator —— 计划里这一条已标为**待确认输入**，我**没有**假定可取回。

**没有发现问题的部分如实说**：`AGENTS.md` 的五个冷启动问题（谁调度／谁可写 `main`／是否暂停／哪些节点开放／各等谁与下一步法律动作）在 `restart「当前控制权」` + `current-release ## Now` + 绑定源三处**可以一致回答**；`agent-delivery-contract.md` §7 的"运行时绑定三条件"（来源唯一 / 指针+as-of / 有存在性与新鲜度检查）**实测成立**（`--check` R6 ok，结论有 receipt 落点）；`docs/evidence-ledger.md` 与 `docs/receipts/2026/` 的索引关系明确，未发现第二 ledger。

---

## 5. 实际读过的关键文件与固定版本

**Professional Workflow 仓库**（全部经 `git show <commit>:<path>`，未 checkout）
- 固定交付 commit `205b831ecb9ba4e79481a08e6b23f7159dca4113`；核心 subtree `11e6e3772b6bc0e17259c932b0c0dcabb030a133`（实测 = `205b831:professional-workflow`）
- `professional-workflow/README.md`、`authority/README.md`、`authority/RESPONSIBILITY-BACKBONE.md`、`profiles/README.md`、`profiles/driver.md`、`profiles/technical-planning.md`、`profiles/evidence-evaluation.md`、`charters/README.md`、`charters/template.md`、`charters/examples/implementation-local-fix.md`、`charters/examples/technical-planning-cross-module.md`、`methods/README.md`、`methods/local-defect-feedback-loop.md`、`methods/cross-module-design.md`
- `adoption-examples/ucbip.md`（`205b831`，SHA-256 `37335d1c…62fce`，与验收记录一致）
- 验收与证据边界：`cf107522f9b13a778fa381ba600b4ecfb95fdc7e:docs/overnight/2026-10-01/M6-FINAL-ACCEPTANCE.md`、`PW-01-FINAL-REPORT.md`、`PW-01-MAPPING-REVIEW.md`
- 未读（按其自述或本轮范围）：PW 的 `roles/`、`skills/`、`workflow/registry.yaml`、旧检查器、`principles/`、`sources/`、`upstreams.lock.yaml`

**UCBIP 仓库**（HEAD `7fc94e4a483cf6b1d8add214d7dbe9a1d42b7f76`，tracked clean）
- `AGENTS.md`、`docs/active/agent-delivery-contract.md`（含 §3.1 伪绿必答项、§7 冷启动检查）、`docs/active/multi-agent-development-principles.md`（§5 与 §5.1 角色合同、§11 标题级）
- `docs/tasks/2026-09-19-multi-agent-restart.md`（「当前控制权」「本波节点表」「当前任务图索引」及其两个生成区）、`docs/active/current-release.md`（`## Now` 与其 `current-entry` 生成区、`## Decisions still needed`）、`docs/tasks/2026-09-30-native-message-stream.md`（`CARD-STATE` r6、目标、已核事实表、设计待决、四类依赖、验收）、`docs/TODO.md`（头部与 2026-09-23 全流程测试节）、`docs/active/engineering-method-routing.md`（§1–§5）
- 运行态（**非 tracked 权威**，仅用于判断"是否在飞"）：`.agent-local/driver-0922/role-binding.tsv`（**仅 role 列与 as-of**）、`.agent-local/driver-seal-1001/STATUS.md`、`.agent-local/evidence/tool-seal-1001/**` 的目录与 mtime、`.agent-local/oracle-0930b/tool-seal-1001/` 文件清单
- 只读命令：`git rev-parse/log/status/ls-tree/cat-file/worktree list/branch`、`sed`、`grep`、`awk`、`shasum`、`python3 scripts/render_current_state.py --check`

**本轮未做**：不写文件、不改工作树或 Git 状态、不 checkout、不跑测试/生成器写模式/安装/服务、不访问网络、不启动或联系任何 agent。唯一执行的脚本是 `render_current_state.py --check`（只读模式，前后 `git status` 均 clean）。所有"计划"仅为本轮规划，未执行、未验证通过；UCBIP 那条 native 切片**未被授权派工**，本 session 的有效委托只有这次只读测试。

---

## 6. 影响计划的未核事项

1. **Owner R1 裁定的可取回副本**——原文在 `/private/tmp/ucbip-native-r1-identity-ruling-0930.md`，tracked 侧只有摘要 + locator；**未确认能否取回**。取不回则 Designer 的委托文本只能引用摘要，需要 Driver 显式说明证据等级。
2. **native 切片的写权窗口**——卡写"本阶段零产品源码写权/零写集"，现行顺序只列 TOOL SEAL；**该窗口是否已开、开到哪个目录，我未在 tracked 材料里找到取值**。
3. **Designer 承载**——绑定源 `governance-designer` / `plan-writer-03` / `plan-writer-cards` 三槽**当前无承载者**；I1 到底复用什么，属 Driver 决定，我不预设。
4. **"哪条 entry 算回答"**——卡自述为产品/owner 决定，**未决**；它直接决定验收判据，不解决就不能声称设计完整。
5. **TOOL SEAL 线的实时相位**——我只能从 `.agent-local` 的运行态与分支名看出仍在 review/fix/verify；**tracked 侧无法独立重建**。若我要与它并行，必须先请 Driver 给出当前相位与串行位归属。
6. **TODO 与卡状态的新鲜度差**（B6/B14 等）——我没有能力在本轮判定它们是"在飞"、"已并入"还是"已放弃"；已按"卡状态块权威"处理，未据此选择任务。
7. **UCBIP 与包的"方法名"映射**（第 4 节 B）——是否已由 Driver 在任务卡里用别的名字落地，我未核；这会影响未来任何"按路由表选方法"的动作。
8. 三份固定候选（B8-2 / B8-2b / B-1）与 FINAL-PREVIEW 的 Owner 决定——**纯 Owner 事项，未核、不推定**。

我在此待命，不执行、不派工、不为 UCBIP 决定开工。