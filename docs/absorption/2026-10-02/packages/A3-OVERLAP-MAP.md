# A3 联动观察（非裁定，供 gate 归并）

**性质：** 只读联动观察。**本文件不作任何采纳/限缩/拒绝结论**，不改变产品、不改变他人文档。
它把 `A3-MATT-ABC.md`（11 组）与 `A3-MATT-DEF.md`（14 组）共 **25 个机制组**与另外三包已落包的
机制组做一次对位，供 gate 判断"同一机制是否应合并到已有的家、知识增量是否只计一次"。
是否归并、如何归并，属计划中"碰撞由 gate 判断知识整合"，本文件不代裁。

**读深声明（重要，直接限定本文件若干条目的可信度）**

| 我读了什么 | 深 度 |
| --- | --- |
| A2R-CURSOR-ABC2 MG-1 全文（含 `principle-test-behavior-not-implementation`、`skills/tdd`、`principle-fix-root-causes`、`prove-it-works`、`blast-radius` 的机制段） | 逐字 |
| A2R-CURSOR-ABC2 MG-5 全文（共享写面与幂等，含三问测试） | 逐字 |
| A2R-CURSOR-ABC MG-5 全文（验证工具链的设计与维护） | 逐字 |
| A2R-CURSOR-ABC MG-2 全文（可观察事实 vs 人类偏好 + 原型决策） | 逐字 |
| 三包的「机制组一览 / 总览」表与全部组标题 | 逐字（表格与标题级） |
| A1 G1–G7、A2R-CURSOR-ABC MG-1/3/4/6/7/8、A2R-CURSOR-ABC2 MG-2/3/4 的**正文** | **未读** |
| mattpocock-skills 源仓原文 | 本文件**未重读**；一律引用 `A3-MATT-ABC.md` / `A3-MATT-DEF.md` 已固定的锚点 |

凡某一对位只依据"组标题 + 源文件清单 + 判断位点列"得出，我在该条标注 **[标题级]**。标题级不等于
已确认——组标题可以覆盖与我不同的机制，也可能我据标题推断的机制其实不在其中。**标 [标题级] 的条目，
归并前需要 gate 或我补读其正文。**

---

## (1) 他仓机制组全景与来源包名

**A1-ADDY-AB.md**（913 行，7 组，族 A/B）

| # | 机制组 | 主源锚 | 我方可辨对位 |
| --- | --- | --- | --- |
| G1 | 编排与组合纪律（含反模式目录与准入条件） | `references/orchestration-patterns.md`、`docs/agents.md`、`agents/*.md#Composition` | — |
| G2 | 意图路由与"适用性存疑"的默认 | `AGENTS.md#Intent → Skill Mapping`、`skills/using-agent-skills/SKILL.md#Skill Discovery` | — |
| G3 | 变更评审纪律（五轴/分级/规模/描述/分歧/诚实/依赖） | `skills/code-review-and-quality/SKILL.md`、`agents/code-reviewer.md` | 对位 A3 DEF-2 |
| G4 | 交接与恢复纪律（跨会话/跨实例） | `docs/getting-started.md#Working across sessions`、`skills/context-engineering/SKILL.md#Restartable Session Boundaries` | 对位 A3 DEF-9 |
| G5 | 常备门槛与本次验收条件的分离 | `references/definition-of-done.md`、`docs/adoption-guide.md` | 与 A3 ABC MG-5 同域但问题不同 |
| G6 | 方法库自身的变更纪律（反重复/负结果/同步面/耦合拆除判据） | `CONTRIBUTING.md`、`docs/skill-anatomy.md#Write the Procedure, Not the Workaround` | 对位 A3 DEF-12、DEF-14 |
| G7 | 在存量工作里引入门槛的顺序（两速 + 棘轮） | `docs/adoption-guide.md`、`skills/code-simplification/SKILL.md#Step 1` | 对位 A3 DEF-3 |

**A2R-CURSOR-ABC.md**（846 行，8 组，族 A/B/C 主干 + 工程裁决）

| # | 机制组 | 主源锚 | 我方可辨对位 |
| --- | --- | --- | --- |
| MG-1 | 前提审问与设计理由调查 | `principle-attack-the-premise`、`why` + `references/epistemics.md`、`how` | 对位 A3 DEF-6 |
| MG-2 | 可观察事实 vs 人类偏好；原型决策 | `playbooks/prototype.md`、`principle-never-block-on-the-human`、`playbooks/multi-phase-plan.md` step 2 | 对位 A3 ABC MG-9、DEF-5 |
| MG-3 | 面向 agent 消费者的行为契约（CLI） | `cli-for-agent/skills/cli-for-agents/SKILL.md` | 与我 ABC MG-8 相邻（契约 vs 文本排布） |
| MG-4 | 领域结构先行与边界纪律 | `principle-model-the-domain`、`principle-boundary-discipline` | 对位 A3 ABC MG-6、MG-7、MG-10 |
| MG-5 | 验证工具链的设计与维护 | `create-verification-skill`、`maintain-verification-skill`、`docs/guide/06-verify-and-ship.md` | 对位 A3 DEF-13、DEF-14 |
| MG-6 | 独立评审裁决与完成前复核 | `thermo-nuclear-review`、`thermo-nuclear-code-quality-review`、`thermos`、`interrogate`、`advisor` | 对位 A3 DEF-2 |
| MG-7 | 交接格式与证据等级 | `orchestrate/references/handoffs.md`、`references/planner.md` | 对位 A3 DEF-9 |
| MG-8 | 无人值守收束与决定轨迹 | `show-me-your-work`、`playbooks/autonomous-run.md`、`pause-safely.md`、`session-pickup.md` | 与 A3 DEF-9 相邻（决定轨迹） |

**A2R-CURSOR-ABC2.md**（511 行，5 组，原则族）

| # | 机制组 | 主源锚 | 我方可辨对位 |
| --- | --- | --- | --- |
| MG-1 | 执行单元与证明纪律 | `sequence-verifiable-units`、`prove-it-works`、`fix-root-causes`、`build-the-lever`、`test-behavior-not-implementation`、`tdd`、`blast-radius` | 对位 A3 ABC MG-1、MG-3、DEF-1、DEF-13 |
| MG-2 | 变更形态与读者负担 | `experience-first`、`exhaust-the-design-space`、`foundational-thinking`、`laziness-protocol`、`minimize-reader-load`、`subtract-before-you-add` 等 9 支 | 对位 A3 ABC MG-2、MG-8、DEF-11 |
| MG-3 | 原则语言与学习编码 | `docs/guide/08-principles.md`、`principle-encode-lessons-in-structure`、`skills/reflect`、`workflow-from-chats` | 对位 A3 ABC MG-8、DEF-12 |
| MG-4 | 上下文重建、解释与状态报告 | `principle-guard-the-context-window`、`skills/recall`、`skills/teach`、`weekly-review`、`what-did-i-get-done` | 对位 A3 DEF-9、DEF-10 |
| MG-5 | 共享写面与幂等（Driver/D/E 交界） | `principle-separate-before-serializing-shared-state`、`principle-make-operations-idempotent` | 对位 A3 DEF-13、DEF-14 |

**A3 组在 25 组中的对位分布（供 gate 核账）**

```
(2) 的 12 条对位覆盖 A3 的 11 个组（DEF-13 / DEF-14 各被两条命中）
(3) 判断仍具独立性            7 组
(2b) 对位存在但依据较弱         7 组
合计                    11 + 7 + 7 = 25 ✓
```

---

## (2) 确认高重叠 12 条

每条格式：**我的组 → 他仓更强的家 → 对位依据 → 我的可辨增量**。

### 1. ABC MG-3（测试反模式 tell）→ A2R-ABC2 MG-1 `principle-test-behavior-not-implementation`

**依据（逐字读过）：** 对方给出决定性二分判据——"如果它 import 的每个函数都返回 `undefined` 测试仍会过，
那它没有观察行为、不可能因缺陷失败"，并列出**五种仍然会过的形状**（弱/无断言：无 `expect`、只有
`toBeDefined`/`toBeTruthy`/`not.toThrow`/`toBeInstanceOf`/`toBeGreaterThan(0)`；只测 mock 或缺失：
`toHaveBeenCalled`/`toBeUndefined`/`toEqual([])`/`toHaveLength(0)`；自指：expected 来自被测代码；常量 pin；
fixture 断言 fixture），每形状附修复，并保留例外（跨表关系测试、`*.test.d.ts` 编译期检查）。

**我的可辨增量：** "expected value 必须来自独立真值来源"的框架；以及与 ABC MG-4 接缝链的连接（F 按约定面
核对，故坏测试的判定要落在约定面上）。**我的实现-coupled / tautological 两条命名与对方五种形状高度同域，
归并时不应各计一次。**

### 2. ABC MG-1（red before green）→ A2R-ABC2 MG-1 `skills/tdd`

**依据（逐字读过）：** 同一 red→green 循环；对方另含 "**Prefer no new test over a bad test**"、
坏测试定义（主要测 mock / 编码实现细节 / 依赖时序或无关全局状态 / 小修复需要昂贵基础设施 / 证完就删）、
以及**不可行时的替代**（定向脚本、手工复现命令、浏览器自动化、快照比较、日志断言、聚焦集成）。

**我的可辨增量：** 垂直切片与 tracer bullet；"refactoring 不在循环内、归 code-review"这一决定及其理由；
以及 MG-4 的接缝约定前置。**我缺对方"无可行测试路径时怎么办"的替代清单，属补读候选。**

### 3. DEF-13（prove the check bites）→ A2R-ABC MG-5

**依据（逐字读过）：** 对方以"**未执行过的 generated skill 是 draft 不是 deliverable**"表达同一规则，
并多出三条我没有的硬条件：**cleanup 不得吞掉证据**（"a cleanup that eats the proof fails this step"）；
**doctor-before-drive**（自上次"做过意外之事"以来未 health-check 的实例不再 drive，任何失败 drive 后先 doctor）；
**dry-run/test mode 必须观察它实际跳过了什么**（文件、网络、git refs），"不要相信名字——有些 dry-run 仍会触网或开浏览器"。

**我的可辨增量：** 把该规则落在**机械检查（linter 规则 / pre-commit / CI job）**这一载体类别上，而非验证
skill；以及"写明检查抓不到什么"的诚实边界条款。**对方在"证据不得被清理吞掉"与"不信名字只信观察"两点上更强，
建议以对方为该机制的家。**

### 4. DEF-14（非篡改式漂移检查）→ A2R-ABC MG-5 `maintain-verification-skill`

**依据（逐字读过）：** 对方有 clean / changed / blocked 三结局并强制声明、edit scope 只允许验证 skill 自身目录、
**"绝不在一次 run 里改产品代码"**（map 与行为不符时：要么 doc drift 修 map，要么产品回归报告，不用文档粉饰）、
以及 Pass 0–6 的定位/索引卫生/源波次/对账/live pass/triage/ship 流程。

**我的可辨增量：** 非篡改的 **`--check` 模式**（报告偏离、不改任何东西、非零退出）与写后断言、以及
"只改值、保持周围格式"的最小写入。**这是窄贡献，不宜自成一 груп。**

### 5. DEF-14（目标不对即拒绝）+ DEF-13（合并不覆盖）→ A2R-ABC2 MG-5

**依据（逐字读过）：** 对方是该领域的正经所有者——"**指令与约定不是并发控制**"；消除共享优先于加锁、
并把"我们需要一把锁"当作**要被检查的设计 smell 而非默认答案**；给出共享可变状态的判别细则
（两个 worker 各自写 `lastX` 进同一个 `state.json` **仍是共享突变**；`indexer-state.json` +
`metrics-state.json` **不是**）；以及**幂等三问测试**（连续跑两次会怎样？上次在每个可能点崩掉会怎样？
重执行是否收敛到同一末端状态？任一答案是"取决于留下什么状态" → 需要 reconciliation 步骤）。

**跨源合并信号（重要）：** 对方 MG-5 §4 引用的产品锚点与我 DEF-8 第 3 条相同——`profiles/driver.md`
"并行写者的写集是否明确？共享文件是否单写者串行集成？"，且**命中了同一处缺口**：现有文本只到"单写者
串行集成"，缺"共享写目标是否必要"的前置判断程序。**两源同缺口，正是计划预期的跨源合并，知识增量应计一次。**

**我的可辨增量：** "目的地不是我以为的那样就停下报错、而不是写下去看"这一条守卫（对方无此条）。

### 6. DEF-9（上下文转移）→ **三家都碰**

**依据 [标题级]：** A1 **G4 交接与恢复纪律**（源 `docs/getting-started.md#Working across sessions`、
`skills/context-engineering/SKILL.md#Restartable Session Boundaries`）；A2R-CURSOR-ABC **MG-7
交接格式与证据等级**（源 `orchestrate/references/handoffs.md`、`references/planner.md#Failure recovery`）；
A2R-CURSOR-ABC2 **MG-4 上下文重建、解释与状态报告**（源 `principle-guard-the-context-window`、`skills/recall`、
`weekly-review`、`what-did-i-get-done`）。三条正文我均未读。

**我的可辨增量：** "**可移植性而非压缩**"的定位与四情境触发（换工具/换目录/换人/中途分叉），以及
**已落盘者只引用不复写**（避免第二份要维护的真相）。若三家已覆盖同一机制，我 DEF-9 应视为第四次重复，
其贡献收敛为上述两条。

### 7. DEF-2（双轴评审）→ A1 G3 + A2R-CURSOR-ABC MG-6

**依据 [标题级]：** A1 **G3 变更评审纪律**自述为"五轴/分级/规模/描述/分歧/诚实/依赖"（源
`skills/code-review-and-quality/SKILL.md`、`agents/code-reviewer.md`、`.claude/commands/review.md`）；
A2R-CURSOR-ABC **MG-6 独立评审裁决与完成前复核**（源 `thermo-nuclear-review`、
`thermo-nuclear-code-quality-review`、`thermos`、`interrogate`、`advisor`）。两条正文我均未读。

**我的可辨增量：** **反混淆那一条**——两轴产出后禁止合并、禁止跨轴排序，理由是"混合裁决会让通过的那一轴
遮住失败的那一轴"，并附两种不对称例子（合规但做错事 / 做对事但破坏约定）。轴数本身（我 2、A1 5）
不构成增量。**gate 需读 A1 G3 正文判断其是否已含"禁止跨轴排序"。**

### 8. ABC MG-9（facts vs decisions）→ A2R-CURSOR-ABC MG-2 的 AskQuestion 分类规则

**依据（逐字读过）：** 对方规则为——提问前先分类：**"如果答案是一个你可以通过运行某样东西观察到的事实
（behavior、timing、layout、output、perf，甚至 eval 能否区分），那它就不是人类该回答的"**；只有
"genuine product or preference call that no experiment can settle"才留给人类；read-only 调查类任务直接回答；
全自治授权下可自决已授权的决定、operator-only 的决定取默认值并给完整解释与可撤销的一句话。

**我的可辨增量：** **排程**——设计树、frontier、逐轮问整个 frontier、同轮内不得互相依赖、重算而非预写、
以及"frontier 空 + 人类确认理解一致"才结束。对方只有分类没有排程；**两者互补，不应互替。**

### 9. DEF-5（原型作为有界证据）→ A2R-CURSOR-ABC MG-2 的 prototype playbook

**依据（逐字读过）：** 对方有"先锁定原型要做的那个决定（没有决定就没有原型）"、设计空间开放时先收集
references 让用户挑方向、在隔离 scratch dir 用最轻栈、多方案用一个 switcher 并列、
**"在匹配 surface 上观察"**、以及 **"原型里观察就是测试，不是断言"**；成立条件明写"**比较至少两个
结构上不同的候选才够**"。

**我的可辨增量：** **证据保全**——原型作为一手来源留在 main 之外的 throwaway 分支，并从实现记录用 context
pointer 指回（理由是"下一会话的人要从什么出发；原型的文字摘要会丢掉让它有说服力的东西"）；
以及**非作者可驱动**这一载体要求（终端程序会排除掉最需要征询其意见的人）。这两条对方均未表述。

### 10. DEF-10（持久学习工作区）→ A2R-ABC2 MG-4 + MG-3

**依据 [标题级]：** A2R-ABC2 **MG-4** 的源文件清单**含 `skills/teach`**，同组还有
`principle-guard-the-context-window`、`skills/recall`；**MG-3** 含 `principle-encode-lessons-in-structure`
与 `skills/reflect`。两条正文我均未读。

**我的可辨增量：** 可迁移的三条**规则**（而非教学工作区本身）——difficulty 的符号随阶段反转
（理解期是敌人、能力期是工具）；coverage 不是 learning 的记录门与 supersede-by-marking；
**复用预测决定载体**（会被反复回看的压缩成 reference，只读一次的留给产出它的工作）。
**我包内已声明不提议引入教学工作区本体**；若 MG-3/MG-4 已覆盖"学习编码"，我 DEF-10 应窄化为上述三条。

### 11. ABC MG-8（指针措辞 / no-op / leading words）→ A2R-ABC2 MG-2 + MG-3

**依据 [标题级]：** MG-2 含 **`principle-minimize-reader-load`**、`principle-subtract-before-you-add`、
`principle-experience-first`；MG-3 为"原则语言与学习编码"。两条正文我均未读。

**我的可辨增量：** 指针**措辞**工程（措辞而非目标决定可达性；一分支一触发、同义词即同一分支写两遍；
前导词前置；cached 身份要删）与 **no-op 检验的模型相对性**（是否改变行为相对于默认，只能靠跑文档定，
不能靠辩论；句子不过关就整句删而非修词）。若 MG-2 的 `minimize-reader-load` 已含这些，则我该组窄化。

### 12. DEF-1（诊断的 gate 与复现率）→ A2R-ABC2 MG-1 `principle-fix-root-causes`

**依据（逐字读过）：** 对方含先复现、问到根因、**不加 guard**（"加 nil check 压 crash 是症状修复"）、
需要长注释辩护的 workaround 说明代码错了（**改代码不改注释**）、**修 pattern 不只修 instance**
（grep 同模式、修全部）、卡住就仪器化不猜；以及一条我没有的经验：**重启类 bug 先怀疑状态**
（config 文件、cache、lock 文件、序列化状态；**若清掉一个 state 文件就恢复，优先把 state 校验作为修复**）。

**我的可辨增量：** phase **gate 表**（各阶段开门的具体可检条件，尤其"无红能力命令则不得进入假设"）；
tightness 四性质与校准句；**非确定性缺陷以"提高复现率"为目标**及其手段；**最小化的完成条件**
（逐个移除、每个剩余元素都是承重的）；预测试的假设排序检查点。

**附：他仓有而我缺的具名机制（属本条与第 1、3 条，供补读而非新组）**

| 机制 | 他仓家 | 我处状态 |
| --- | --- | --- |
| 启动/重启类故障先怀疑状态（config/cache/lock/序列化），清掉即恢复时把状态校验当修复 | A2R-ABC2 MG-1 `fix-root-causes` | 我 DEF-1 **缺** |
| 五级置信阶梯 + "找到这个改动之所以安全的那一两个事实并运行代码证明它"（含"看 grep 停下的地方"、confirmed 与 cleared 分开） | A2R-ABC2 MG-1 `blast-radius` | 我 ABC/DEF **均无**；注意与我 matt 侧 `to-tickets` 的"wide refactor blast radius"是**不同机制**（机械改动的影响面 vs 安全性所依赖的那个事实），勿混 |
| 无可行测试路径时的替代检查清单 | A2R-ABC2 MG-1 `tdd` | 我 DEF-1 部分有（十阶阶梯），但无"不可行时"的收口 |
| dry-run 必须观察实际跳过了什么 | A2R-ABC MG-5 | 我 DEF-7 缺该反例 |
| 证据不得被 cleanup 吞掉 | A2R-ABC MG-5 | 我 DEF-13 缺 |
| 幂等的三问测试与 reconciliation | A2R-ABC2 MG-5 | 我 DEF-14 缺（我 matt 侧本就无幂等材料） |
| "指令与约定不是并发控制" | A2R-ABC2 MG-5 | 我 DEF-8 部分有（作者自合并），未成规则 |

---

## (2b) 对位存在但依据较弱的 7 组

这 7 组我也认为可能与别仓同域，但**依据只到组标题或源文件清单级**，或我尚未确认对方是否真的含该机制。
列在此处是为了让 25 组的核账完整（11 + 7 + 7），**不是为了把它们当作已确认重叠**；均需补读后由 gate 判。

| 组 | 疑似同域的家 | 弱的理由 / 我的可能增量 |
| --- | --- | --- |
| **ABC MG-2** 垂直切片与 demo-path 问句 | A2R-ABC2 MG-1 `sequence-verifiable-units`（“每单元以可检查状态结束，绿了才前进”、先 rebase 到干净 trunk） | [标题级 + 同组已逐字读] 对方是执行单元的**可验证性**，非“切分方式”；我的增量是 demo-path 一问句与 wide-refactor 的 expanded–migrate–contract 例外 |
| **ABC MG-6** 决定记忆（ADR 三闸 + 拒绝记录） | A2R-ABC MG-4 `principle-model-the-domain`；A1 G6（反重复/负结果） | [标题级] 对方是领域结构层与库自身变更纪律；我的增量是“三闸全中才记”与**拒绝记录的持久性判别**（延期 ≠ 拒绝） |
| **ABC MG-10** 模块边界词汇 | A2R-ABC MG-4 的边界纪律部分 | [标题级] 对方拥有边界纪律；我的增量是 deletion test、depth-as-leverage 与**被拒框架及其理由**（含 boundary 与 C 撞词） |
| **DEF-3** 周期性结构普查 | A2R-ABC MG-5 `maintain-verification-skill`（周期性复审、三结局）；A1 G7 | [标题级 + 同组已逐字读] 对方是**验证** skill 的维护；我的增量是强度徽章作为“什么都没找到”的表达装置，与拒绝记录的可持久化提议 |
| **DEF-6** 委派调查 | A2R-ABC MG-1（why/how + epistemics） | [标题级] 对方是前提审问与理由调查；我的增量是 fact vs decision 的**保质期**判别与 delegation-depth 守卫 |
| **DEF-11** 长文草稿 | A2R-ABC2 MG-2（`experience-first`/`minimize-reader-load`）；MG-3 | [标题级] 可能已含读者负担；我的增量是 grounding 规则的双向失效与**共享文档写入节奏**（每次写前重读、只追加不覆盖） |
| **DEF-12** 机械违例→确定性检查 | A1 G6（方法库自身变更纪律）；A2R-ABC2 MG-3（学习编码） | [标题级] 对方含反重复判据；我的增量是机械/判断力分类器、**默认建检查而非写规则**、以及无 guardrail 本身是 finding |

## (3) 我判断仍具独立性的组（7）

判据：在他仓的组标题与源文件清单中**未见**对应机制，且不是同一规则的不同措辞。仍是待 gate 复核的
观察，不是结论。**均未重读 matt 原文**，机制描述引自已固定的 `A3-MATT-ABC.md` / `A3-MATT-DEF.md`。

| 组 | 机制 | 未见对应家的理由 |
| --- | --- | --- |
| **ABC MG-4** | 接缝约定作为**已接受契约项**：既有接缝优先于新接缝、取最高可及接缝、数量趋向一条、且由下游按约定面核对；绑定是间接的（经由契约文件），所以要在有全貌时定而非推到实现期 | 三包无"接缝"组；A2R-ABC MG-5 是验证工具链、MG-6 是评审裁决，非"约定测试面" |
| **ABC MG-5** | **可失败的接受判据**：对每条判据点名"什么观察会证伪它"，并确认该观察在**基点版本**上为红；三种形状（基点已真、只能由本变更之外的工作满足、只是重述请求） | A1 G5 是"常备门槛 vs 本次验收条件的分离"，**问题不同**（分离 ≠ 能否失败） |
| **ABC MG-7** | 术语纪律的 `_Avoid_`：决议一个词时**同时记录被放弃的词**；定义 what it IS 而非 what it does；项目特有概念过滤；以及"陈述与代码对质并在改变任一方之前先暴露矛盾"及其**范围限制**（够不到已关闭的历史决议） | A2R-ABC MG-4 是"领域结构先行"（结构层），未含 `_Avoid_` 这一存留机制 |
| **ABC MG-11** | **每仓配置运行时读取**而非硬编码：canonical 词汇 + 可编辑的本地映射；"tracker 是 setup 答案不是方法属性"；以及再同步触发（方法体变更后旧证据覆盖失效） | 三包均无配置面/再同步面分组 |
| **DEF-4** | **迷雾下多会话规划**：destination 先行定范围；map 是索引不是仓库（一处一处存、按需 zoom）；**模糊度与范围是两轴**（可精确表述=条目 / 不可表述=fog / 越界=out of scope，fog 永不毕业）；先认领后开工；plan-don't-do 及其**可自编辑约束不是约束**的结构教训 | 三包无对应；A1 G7 是"引入门槛的顺序"，非迷雾规划 |
| **DEF-7** | **人工程序**：固定库 / 作者只写阶段（字面 marker 为界）；从环境推导输入而非冷问；每值三问（哪来/写到哪/是否机密）；**先开 URL 再取值**；以及**不可端到端执行产物的静态校验 + 逐值落点 trace**，并如实交付"首次运行才是测试" | A2R-ABC MG-5 有"未执行即 draft"（对验证 skill），但无"人工程序"这一载体与静态 trace 法 |
| **DEF-8** | **合并先追意图后看 diff**：把两侧追到 primary source 使选择发生在两种意图之间；兼容则保双方、不兼容按本次操作的目标取舍并**说出让掉了什么**；不发明新行为；以及"**合并是最容易产出两边都满足、两边测试都不过的代码的地方**，故提交前先跑本项目检查" | A2R-ABC2 MG-1 只有"先 rebase 到干净 trunk 使检查对真实 baseline"这一基点规则，非意图解析 |

---

## (附) 归并前建议补读的最小集

只影响归并判断、不改变我已交的两包正文。按性价比排序：

1. **A1 G3 正文** —— 决定我 DEF-2 是否为重复（五轴是否已含"禁止跨轴排序"）。**[标题级]**
2. **A2R-ABC2 MG-2、MG-3 正文** —— 决定我 ABC MG-8、DEF-10、DEF-11 是否需窄化。**[标题级]**
3. **A2R-ABC MG-4 正文** —— 决定我 ABC MG-6、MG-7 是否需窄化。**[标题级]**
4. **A1 G4、A2R-ABC MG-7、A2R-ABC2 MG-4 正文** —— 决定我 DEF-9 的最终增量收敛到哪两条。**[标题级]**
5. **A2R-ABC2 MG-1 `blast-radius`** —— 决定"五级置信阶梯 + 安全性所依赖的那个事实"是否作为独立机制补入（我目前无）。已读同组其他支，仅此支未逐字读。

（我这边可随时执行上述补读，但按计划应等 gate 裁定或 Driver 派工，不自行扩范围。）

## 边界

- 本文件**不含**任何采纳/限缩/拒绝/暂缓结论，也不建议优先级；`确认高重叠` / `需归并但低置信` /
  `仍具独立性` 三个标签是**对位状态描述**，不是裁定。
- 未改产品、未改他人文档、未建 registry/框架、未 commit。
- 未执行任何验证；未重读 matt 源仓原文；标 **[标题级]** 的 6 条依据未读正文，归并前需补读或其正文被 gate 直接核对。
