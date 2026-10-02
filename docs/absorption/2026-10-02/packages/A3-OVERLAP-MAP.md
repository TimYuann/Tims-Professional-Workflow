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
| **本轮补读（有界升级）**：A1 **G3 / G4 / G6 / G7** 正文（机制段 + 覆盖段） | 逐字 |
| **本轮补读**：A2R-CURSOR-ABC **MG-1 / MG-4 / MG-6 / MG-7** 正文（机制段 + 覆盖段） | 逐字 |
| **本轮补读**：A2R-CURSOR-ABC2 **MG-2 / MG-3 / MG-4** 正文（机制段 + 覆盖段） | 逐字 |
| 仍未读：A1 G1/G2/G5 正文；A2R-ABC MG-3/MG-5/MG-8 正文（MG-5 已在上一轮逐字读过机制段）；A2R-ABC2 MG-1/MG-5 正文（均已逐字读过）；A2R-ABC MG-2 正文（已逐字读过） | 见各行标注 |
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

**证据级别：** 正文级（本轮之前已逐字读该组正文）。**补读后结论：** 重叠**确认**，且对方更操作化——它把“坏测试”变成可判定的二分（import 的函数全返回 `undefined` 仍会过 ⇒ 未观察行为），并给出五种仍然会过的形状与逐形状修复；另声明保留例外（跨表关系测试、`*.test.d.ts` 编译期检查）。我方两条命名（implementation-coupled / tautological）与之同域，**归并时不应各计一次**。

**依据（逐字读过）：** 对方给出决定性二分判据——"如果它 import 的每个函数都返回 `undefined` 测试仍会过，
那它没有观察行为、不可能因缺陷失败"，并列出**五种仍然会过的形状**（弱/无断言：无 `expect`、只有
`toBeDefined`/`toBeTruthy`/`not.toThrow`/`toBeInstanceOf`/`toBeGreaterThan(0)`；只测 mock 或缺失：
`toHaveBeenCalled`/`toBeUndefined`/`toEqual([])`/`toHaveLength(0)`；自指：expected 来自被测代码；常量 pin；
fixture 断言 fixture），每形状附修复，并保留例外（跨表关系测试、`*.test.d.ts` 编译期检查）。

**我的可辨增量：** "expected value 必须来自独立真值来源"的框架；以及与 ABC MG-4 接缝链的连接（F 按约定面
核对，故坏测试的判定要落在约定面上）。**我的实现-coupled / tautological 两条命名与对方五种形状高度同域，
归并时不应各计一次。**

### 2. ABC MG-1（red before green）→ A2R-ABC2 MG-1 `skills/tdd`

**证据级别：** 正文级（本轮之前已逐字读该组正文）。**补读后结论：** 重叠**确认**。对方多出“Prefer no new test over a bad test”、坏测试的五条定义、以及**不可行时的替代检查清单**（定向脚本/手工复现/浏览器自动化/快照/日志断言/聚焦集成）。我方增量（垂直切片、refactoring 移出循环及其理由、接缝约定前置）**成立**。

**依据（逐字读过）：** 同一 red→green 循环；对方另含 "**Prefer no new test over a bad test**"、
坏测试定义（主要测 mock / 编码实现细节 / 依赖时序或无关全局状态 / 小修复需要昂贵基础设施 / 证完就删）、
以及**不可行时的替代**（定向脚本、手工复现命令、浏览器自动化、快照比较、日志断言、聚焦集成）。

**我的可辨增量：** 垂直切片与 tracer bullet；"refactoring 不在循环内、归 code-review"这一决定及其理由；
以及 MG-4 的接缝约定前置。**我缺对方"无可行测试路径时怎么办"的替代清单，属补读候选。**

### 3. DEF-13（prove the check bites）→ A2R-ABC MG-5

**证据级别：** 正文级（本轮之前已逐字读该组正文）。**补读后结论：** 重叠**确认且对方更强**。对方以“未执行过的 generated skill 是 draft 不是 deliverable”表达同一规则，并多出三条硬条件：cleanup 不得吞掉证据（“a cleanup that eats the proof fails this step”）、doctor-before-drive（自上次“做过意外之事”以来未 health-check 的实例不再 drive）、以及 dry-run 必须观察实际跳过了什么（“不要相信名字”）。我方增量收敛为：把规则落在**机械检查（linter/hook/CI）**这一载体类别，与“写明检查抓不到什么”。

**依据（逐字读过）：** 对方以"**未执行过的 generated skill 是 draft 不是 deliverable**"表达同一规则，
并多出三条我没有的硬条件：**cleanup 不得吞掉证据**（"a cleanup that eats the proof fails this step"）；
**doctor-before-drive**（自上次"做过意外之事"以来未 health-check 的实例不再 drive，任何失败 drive 后先 doctor）；
**dry-run/test mode 必须观察它实际跳过了什么**（文件、网络、git refs），"不要相信名字——有些 dry-run 仍会触网或开浏览器"。

**我的可辨增量：** 把该规则落在**机械检查（linter 规则 / pre-commit / CI job）**这一载体类别上，而非验证
skill；以及"写明检查抓不到什么"的诚实边界条款。**对方在"证据不得被清理吞掉"与"不信名字只信观察"两点上更强，
建议以对方为该机制的家。**

### 4. DEF-14（非篡改式漂移检查）→ A2R-ABC MG-5 `maintain-verification-skill`

**证据级别：** 正文级。**补读后结论：** 重叠**确认**。对方有三结局（clean/changed/blocked）强制声明、edit scope 只允许验证 skill 自身目录、“绝不在一次 run 里改产品代码”（doc drift 修 map vs 产品回归报告，不用文档粉饰）、以及 **live pass 即使在 source 看起来 clean 时也必须做**。我方增量（非篡改 `--check` 模式 + 写后断言 + 最小写入保持格式）为窄贡献，**不宜自成一组**。

**依据（逐字读过）：** 对方有 clean / changed / blocked 三结局并强制声明、edit scope 只允许验证 skill 自身目录、
**"绝不在一次 run 里改产品代码"**（map 与行为不符时：要么 doc drift 修 map，要么产品回归报告，不用文档粉饰）、
以及 Pass 0–6 的定位/索引卫生/源波次/对账/live pass/triage/ship 流程。

**我的可辨增量：** 非篡改的 **`--check` 模式**（报告偏离、不改任何东西、非零退出）与写后断言、以及
"只改值、保持周围格式"的最小写入。**这是窄贡献，不宜自成一 груп。**

### 5. DEF-14（目标不对即拒绝）+ DEF-13（合并不覆盖）→ A2R-ABC2 MG-5

**证据级别：** 正文级（本轮之前已逐字读该组正文）。**补读后结论：** 重叠**确认**，对方是幂等的正经所有者（“指令与约定不是并发控制”、消除共享优先于加锁、把“我们需要一把锁”当作待检查的设计 smell、三问测试、reconciliation 步骤）。**跨源合并信号确认**：对方 §4 与我 DEF-8 第 3 条引用同一产品锚点（`profiles/driver.md` “并行写者的写集是否明确？”）并命中**同一处缺口**（缺“共享写目标是否必要”的前置判断），知识增量应计一次。我方增量仅“目的地不是我以为的那样就停下报错”。

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

**证据级别：** 正文级（本轮补读 A1 G4、A2R-ABC MG-7、A2R-ABC2 MG-4 正文）。**补读后结论：重叠确认，且发现一处与我方前提的实质冲突，需 gate 裁定。**

- **A1 G4** 的机制是“**产物即交接**”：把工作带向前的是获批文件而非对话；并明确把“**交接产物写成第二份真源**（与 spec/plan 不一致的交接总结）”列为失败模式。另含：切换前必须落盘的**五类事实**；“**已记录的通过 = 对特定基线的 claim**”及其三个重跑触发条件与“按比例检查不必全量”；恢复边界构成（状态更新 + 验证结果 + 提交）；**“进程退出不是任务通过的证据”**；**“重启不得绕过批准闸门”**；隔离读（读多回小）。
- **A2R-ABC MG-7** 的机制是交接作为**唯一信息通道**：五段结构化最终消息、脚本逐字保存且**不得 enrich/sanitize**（“the planner needs the worker's words unfiltered”）、planner 读法五条、合成失败交接与失败模式分类及默认重试阶梯、`dependsOn` 上游 relay（**逐字渲染，草率的 What I did 会污染每个下游任务**）、以及 **`## Verification` 五值证据等级**（`live-ui-verified` / `unit-test-verified` / `type-check-only` / `verifier-blocked` / `verifier-failed`）持久化到任务 state，旧标签**向最保守值迁移**，并要求 `## Execution` 段区分真验证与模式匹配。

**冲突点（需 gate 裁定，非我裁定）：** 我方 DEF-9 以“写一份转移文档”为前提，并以“已落盘者只引用不复写”为规则；A1 G4 更进一步——**不该另写文档，工作产物本身就是交接**，另写即为第二份真源。我方那条规则是 A1 G4 的弱化版。**故 DEF-9 的剩余增量仅为：**（a）“可移植性而非压缩”的定位与四情境触发（含“不旅行就别写”的原地选项 continue/clear/compress）；（b）分叉案例（出去—拿答案—回来并从未结束的线程指回）。其“引用不复写”应**让位于** A1 G4 的“产物即交接”，或改为对它的补充条款（“若产物不足，补产物而非另写摘要”）。

**依据：** 正文级（本轮补读）。 A1 **G4 交接与恢复纪律**（源 `docs/getting-started.md#Working across sessions`、
`skills/context-engineering/SKILL.md#Restartable Session Boundaries`）；A2R-CURSOR-ABC **MG-7
交接格式与证据等级**（源 `orchestrate/references/handoffs.md`、`references/planner.md#Failure recovery`）；
A2R-CURSOR-ABC2 **MG-4 上下文重建、解释与状态报告**（源 `principle-guard-the-context-window`、`skills/recall`、
`weekly-review`、`what-did-i-get-done`）。三条正文我均未读。

**我的可辨增量：** "**可移植性而非压缩**"的定位与四情境触发（换工具/换目录/换人/中途分叉），以及
**已落盘者只引用不复写**（避免第二份要维护的真相）。若三家已覆盖同一机制，我 DEF-9 应视为第四次重复，
其贡献收敛为上述两条。

### 7. DEF-2（双轴评审）→ A1 G3 + A2R-CURSOR-ABC MG-6

**证据级别：** 正文级（本轮补读两处正文）。**补读后结论：重叠确认，但出现**三方向张力**，需 gate 统一取舍（非我裁定）。**

- **A1 G3** 的五轴是**变更质量的五个维度**（正确性 / 可读性简洁 / 架构 / 安全 / 性能），配每轴具体探针、5 步评审顺序（先要意图 → **先看测试** → 逐文件过五轴 → 分级 → **核作者的验证故事**）、**分级 + 作者动作语义**（无前缀=必改 / Critical=阻断 / Nit=可忽略 / Optional / FYI）与**按杠杆排序**（“若你有一个结构性问题与十个 nit，那个结构性问题就是这次评审”）、**分歧判决序**（技术事实与数据 > 风格指南 > 工程原理 > 代码库一致性）、**“不接受以后清理”**（要么现在清，要么开单自派）、依赖纪律（新增五问；升级五条：读 changelog、一次一个、让测试裁决、看传递依赖、lockfile 诚实）、以及**假定阻断项**（显露 + 提出更简单设计，只有确实使结构变差才升级为必改）。**它没有跨轴禁止合并/禁止排序的规则；结论是单一二值（Approve / Request changes）。**
- **A2R-ABC MG-6** 的机制是**多透镜独立评审 + lead judgment 合成**：thermos 并行两个透镜（bug/安全/devex/feature-leak 与 maintainability/structure）再合成（去重、重叠加权、分歧自裁）；interrogate 同 rubric 发多模型、2+ 独立提出为最高信号、lone-model 折权、**显式记录分歧**、lead judgment 分四桶（act on / consider / noted / dismissed）并给理由；另有 Scope（只报本次 diff 新增改动）、**Intended Breakage**（有意且范围受限的破坏不浪费时间）、**Over-reporting 的信任代价**、**先审计后读 PR 讨论以保持 fresh eyes**、briefing **不得改写证据**、以及 advisor 四处 checkpoint（含“同一失败**两次真正修复尝试**后”“即将伸手去抓 workaround 时”：retry loop / sleep / 宽 try/except / skip test / disable check）。

**三方向张力：** A1 G3 = 单一二值裁决 + 轴内杠杆排序；A2R-ABC MG-6 = 多透镜合成 + lead judgment 四桶（**它确实合并**）；我方 DEF-2 = 两轴产出后**禁止合并、禁止跨轴排序**。三者对“评审结论能否合并”给出三种不同答案。
**我方增量经补读后仍然成立且收窄为：**（i）**反混淆规则本身**（禁止把通过轴与失败轴合成一个裁决，理由是“混合裁决让通过的那一轴遮住失败的那一轴”）；（ii）**每条发现必须携带引用**（标准规则/命名 smell + 片段/契约行）；（iii）**fail-fast 校验基点**（先确认被比较的版本能解析、范围非空，再开始评价）与三点 diff 排除未提交工作。注意（iii）与 A1 G3 的“拿不到意图只能审风格，把这点当缺口说出来”同源，属于互相印证。

**依据：** 正文级（本轮补读）。 A1 **G3 变更评审纪律**自述为"五轴/分级/规模/描述/分歧/诚实/依赖"（源
`skills/code-review-and-quality/SKILL.md`、`agents/code-reviewer.md`、`.claude/commands/review.md`）；
A2R-CURSOR-ABC **MG-6 独立评审裁决与完成前复核**（源 `thermo-nuclear-review`、
`thermo-nuclear-code-quality-review`、`thermos`、`interrogate`、`advisor`）。两条正文我均未读。

**我的可辨增量：** **反混淆那一条**——两轴产出后禁止合并、禁止跨轴排序，理由是"混合裁决会让通过的那一轴
遮住失败的那一轴"，并附两种不对称例子（合规但做错事 / 做对事但破坏约定）。轴数本身（我 2、A1 5）
不构成增量。**gate 需读 A1 G3 正文判断其是否已含"禁止跨轴排序"。**

### 8. ABC MG-9（facts vs decisions）→ A2R-CURSOR-ABC MG-2 的 AskQuestion 分类规则

**证据级别：** 正文级（本轮之前已逐字读该组正文）。**补读后结论：** 重叠**确认**（同一分类规则：“能通过运行某样东西观察到的事实不是人类该回答的”；只有 “genuine product or preference call that no experiment can settle” 才留给人类；另有 never-block 的可逆/不可逆分界）。我方增量（**排程**：设计树/frontier/逐轮问整个 frontier/同轮不得互相依赖/重算而非预写/以“frontier 空 + 人类确认理解一致”收束）**成立**——对方只有分类没有排程，两者互补不应互替。**另需并入**对方 `workflow-from-chats` 的**四档置信（strong/medium/weak/contradicted）**与“contradicted → 写文件前先问用户”，这是我缺的。

**依据（逐字读过）：** 对方规则为——提问前先分类：**"如果答案是一个你可以通过运行某样东西观察到的事实
（behavior、timing、layout、output、perf，甚至 eval 能否区分），那它就不是人类该回答的"**；只有
"genuine product or preference call that no experiment can settle"才留给人类；read-only 调查类任务直接回答；
全自治授权下可自决已授权的决定、operator-only 的决定取默认值并给完整解释与可撤销的一句话。

**我的可辨增量：** **排程**——设计树、frontier、逐轮问整个 frontier、同轮内不得互相依赖、重算而非预写、
以及"frontier 空 + 人类确认理解一致"才结束。对方只有分类没有排程；**两者互补，不应互替。**

### 9. DEF-5（原型作为有界证据）→ A2R-CURSOR-ABC MG-2 的 prototype playbook

**证据级别：** 正文级（本轮之前已逐字读该组正文）。**补读后结论：** 重叠**确认**，对方含“先锁定原型要做的那个决定（没有决定就没有原型）”、设计空间开放时先收集 references 让用户挑方向、隔离 scratch dir + 最轻栈、多方案 switcher 并列、**“在匹配 surface 上观察”**、**“原型里观察就是测试，不是断言”**，成立条件明写“**比较至少两个结构上不同的候选才够**”。我方增量（**证据保全**：原型作为一手来源留 main 之外分支 + 从实现记录指针指回；**非作者可驱动**这一载体要求）**成立**，对方均未表述。

**依据（逐字读过）：** 对方有"先锁定原型要做的那个决定（没有决定就没有原型）"、设计空间开放时先收集
references 让用户挑方向、在隔离 scratch dir 用最轻栈、多方案用一个 switcher 并列、
**"在匹配 surface 上观察"**、以及 **"原型里观察就是测试，不是断言"**；成立条件明写"**比较至少两个
结构上不同的候选才够**"。

**我的可辨增量：** **证据保全**——原型作为一手来源留在 main 之外的 throwaway 分支，并从实现记录用 context
pointer 指回（理由是"下一会话的人要从什么出发；原型的文字摘要会丢掉让它有说服力的东西"）；
以及**非作者可驱动**这一载体要求（终端程序会排除掉最需要征询其意见的人）。这两条对方均未表述。

### 10. DEF-10（持久学习工作区）→ A2R-ABC2 MG-4 + MG-3

**证据级别：** 正文级（本轮补读两处正文）。**补读后结论：重叠度比标题级判断时更低——DEF-10 的核心增量成立，且获得一处跨源印证。**

- **A2R-ABC2 MG-4 的 `teach` 是“向人类做一次性说明”，不是多会话工作区**：决定对方应带走几件事、跳过显然已知的、把深度放在问题处、先给朴素定义再绑定当前案例、先给最小完整答案再停、对话而非演讲、**无 quiz、无 pacing theater**、**图示逐张搭建**（“一张全量图、尤其放最后，是 reference 不是 teaching”）、**保持 why 层的 confidence language**（“它的 hedge 是 finding，不是文风”）、**“回复就是说明本身，绝不是关于你做了什么/交付了什么”**。
- **MG-3** 的 `encode-lessons-in-structure` / `reflect` / `workflow-from-chats` 是偏好沉淀与机制化，非学习工作区。

**结论：** 对方**没有** mission 门、learning records、zone of proximal development，也**明确反对 quiz/演练**——即对方只覆盖“理解期”（difficulty 是敌人）这一半，**未覆盖“能力期”（difficulty 是工具）**。故我方 DEF-10 的“difficulty 符号随阶段反转”**成立**，并因此获得**跨源印证**：一个源主张理解期不设难度、另一个源主张能力期以难度为工具，两者在同一不对称性上相容。coverage-不是-learning 的**记录门**与 reuse-预测决定载体亦**未见对方**，增量成立。**建议并入**对方的“hedge 是 finding，不是文风”（对 DEF-9/DEF-6 的证据状态保全同样适用）与“最小完整答案先行再停”。

**依据：** 正文级（本轮补读）。 A2R-ABC2 **MG-4** 的源文件清单**含 `skills/teach`**，同组还有
`principle-guard-the-context-window`、`skills/recall`；**MG-3** 含 `principle-encode-lessons-in-structure`
与 `skills/reflect`。两条正文我均未读。

**我的可辨增量：** 可迁移的三条**规则**（而非教学工作区本身）——difficulty 的符号随阶段反转
（理解期是敌人、能力期是工具）；coverage 不是 learning 的记录门与 supersede-by-marking；
**复用预测决定载体**（会被反复回看的压缩成 reference，只读一次的留给产出它的工作）。
**我包内已声明不提议引入教学工作区本体**；若 MG-3/MG-4 已覆盖"学习编码"，我 DEF-10 应窄化为上述三条。

### 11. ABC MG-8（指针措辞 / no-op / leading words）→ A2R-ABC2 MG-2 + MG-3

**证据级别：** 正文级（本轮补读两处正文）。**补读后结论：重叠确认，且我方的 leading-words 一条被对方覆盖并改进；指针措辞/no-op/否定失效三条增量成立。**

- **MG-3 的 `principle names as interface` 覆盖并改进我方 leading words**：名字指向一条完整规则、一个短语比一段话更精确地改向；并附一条我缺的**可检查伴随要求**——“**agent 必须在回复中说明该规则改变了哪个决定**；A principle citation with no decision behind it is the tell that it name-dropped instead of applying.” 我方 leading-word 机制应**让位于**此（或改为其补充）。
- **MG-2 的 `minimize-reader-load`** 给出**两轴测量**（到答案要追的层数；读者要放脑中的隐藏/可变状态）与 **30 秒测试**，并含接口压缩、state 范围收缩（纯函数 > 返回而非突变 > 局部 > 字段 > module > global；derive 而非 sync）、加层前问“它在别处减少的读者负担是否至少等量”。这属**代码读者负担**，与我方**文档指针**不同域，但共用“读者负担”概念。
- **MG-2 的 `laziness-protocol` / `subtract-before-you-add`**（优先删除、3 层以上穿层就压平、合并决定到单一真源、最小 diff、question the threading、不做投机 validator）与 **`exhaust-the-design-space`**（无先例 → 2–3 个整形状竞争原型，“同一形状的第二版不算”，并给出**不适用条件**）——后者正是被旧轮 defer 的 `DESIGN-IT-TWICE`，且**条件比我方 ABC MG-10 缺口 4 更完整**。
- **MG-4 的 `guard-the-context-window`** 补我方 MG-8 缺的一条：**频繁使用的内容保持内联**（模板与每次调用的引用放文件里，不拆成每次都要读的文件）+ **phase 大小与回合预算**的机制成本意识。

**我方仍未被覆盖的增量：**（i）**指针措辞工程**（措辞而非目标决定可达性；一分支一触发、同义词即同一分支写两遍；前导词前置；删掉 body 已携带的身份信息）；（ii）**no-op 检验的模型相对性**（是否改变行为相对于默认，只能靠跑文档定，不能靠辩论；句子不过关就整句删）；（iii）**否定指令的失效模式**（“Don't think of an elephant”；只能作为无法正面表述的硬护栏并配正面目标）；（iv）**面向 agent 文档**这一框架本身。

**依据：** 正文级（本轮补读）。 MG-2 含 **`principle-minimize-reader-load`**、`principle-subtract-before-you-add`、
`principle-experience-first`；MG-3 为"原则语言与学习编码"。两条正文我均未读。

**我的可辨增量：** 指针**措辞**工程（措辞而非目标决定可达性；一分支一触发、同义词即同一分支写两遍；
前导词前置；cached 身份要删）与 **no-op 检验的模型相对性**（是否改变行为相对于默认，只能靠跑文档定，
不能靠辩论；句子不过关就整句删而非修词）。若 MG-2 的 `minimize-reader-load` 已含这些，则我该组窄化。

### 12. DEF-1（诊断的 gate 与复现率）→ A2R-ABC2 MG-1 `principle-fix-root-causes`

**证据级别：** 正文级（本轮之前已逐字读该组正文）。**补读后结论：** 重叠**确认**（先复现、问到根因、**不加 guard**、需要长注释辩护的 workaround 说明代码错了、**修 pattern 不只修 instance**、卡住就仪器化不猜），并含一条我缺的经验：**重启类 bug 先怀疑状态**（config/cache/lock/序列化状态；**清掉一个 state 文件即恢复时，优先把状态校验作为修复**）。我方增量（phase **gate 表**、tightness 四性质与校准、**以“提高复现率”为目标的非确定性缺陷**、最小化完成条件、预测试的假设排序检查点）**成立**。

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

## (2b) 原「依据较弱 7 组」· 补读后定论

这 7 组上一版只依据组标题与源文件清单标注 [标题级]。**本轮已补读相关正文，逐条结论如下。**
（本节原样保留上一版的三类合计口径：主体让位 9 + 存在张力 2 + 具独立性 14 = 25。）

| 组 | 补读的家 | 补读后结论 |
| --- | --- | --- |
| **ABC MG-2** 垂直切片与 demo-path 问句 | A2R-ABC2 MG-1 `sequence-verifiable-units` | **主体不重叠。** 对方机制是“把工作排成小单元、每单元以**可检查状态**结束、绿了才前进”，执行上是 before/after 括号（known-good → 一处改动 → 跑检查 → 继续）、先 rebase 到干净 trunk 使每次检查对**真实 baseline**、以及“提交序列读起来是一个论证”。它是**执行单元的可验证性**，不是**切分方式**。我方增量（demo-path 一问句、垂直-完整路径、expand→migrate→contract 的 wide-refactor 例外及其 green-only-there 兜底）**成立**。与 DEF-8 的关系：对方的“先 rebase 到干净 trunk”是基点规则，不是意图解析，两者不重复。 |
| **ABC MG-6** 决定记忆（ADR 三闸 + 拒绝记录） | A2R-ABC MG-4 `principle-model-the-domain`；**A1 G6**（负结果留存） | **该组须拆开：part B（拒绝记录）主体让位，part A（ADR 三闸）具独立性。** A2R-ABC MG-4 是**领域结构选型**（state machine / typed model / registry / reducer 等清单 + 三个反模式信号 + “不强制抽象”门槛），**与 ADR 和拒绝记录无关**，故不构成重叠。但 **A1 G6 的“负结果留存（被拒台账）”正是我 ABC MG-6 part B 的同一机制，且更操作化**：只增行、只记被拒、**必带“用什么证据被拒”与结果**、并**必须单独落在默认分支**——理由是“若只留在被拒提案的分支上，关闭或强推该分支会把记录一起丢掉”。我方增量收敛为：**三闸全中才记**的 ADR 门槛 + 最小记录（标题 + 1–3 句）+ 七类合格范畴，以及拒绝记录的**持久性判别**（“延期 ≠ 拒绝”，且“已实现”不得写入拒绝台账以免污染去重）。**建议：拒绝记录以 A1 G6 为家，我方只补持久性判别两条。** |
| **ABC MG-10** 模块边界词汇 | A2R-ABC MG-4 边界纪律；A2R-ABC2 MG-2 `minimize-reader-load` | **删除测试一条已被覆盖，该组大幅让位。** A2R-ABC MG-4 的“不强制抽象”门槛即同一操作，且**列举了必须被删掉的东西**——“对只增加间接性而不删除**分支 / 重复规则 / 非法状态 / 生命周期风险**的抽象持怀疑”，并给出三个具名失败信号（新功能让既有 if/else 链又长一节；**第二个必须与第一个同步的 boolean**；**temporal decomposition**——按阶段命名的 module 把同一领域规则在各步骤重复，附判据句 “**Execution order is not ownership**”）。A2R-ABC2 MG-2 的 `minimize-reader-load` 进一步给出**两轴测量**与 **30 秒测试**，`laziness-protocol` 给出“优先删除 / 3 层以上穿层就压平”。**我方残余仅为：** 被拒框架及其理由（`interface` ≠ TS 关键字或公开方法；`boundary` 与 C 的 bounded context 撞词，须改用 seam/interface）+ 接口即“调用者必须知道的全部事实”这一定义（后者**已在产品** `methods/cross-module-design.md` §Method 2）。另注：我方 ABC MG-10 缺口 4（`DESIGN-IT-TWICE` 窄化复入）也应**让位于** A2R-ABC2 MG-2 `exhaust-the-design-space`——对方条件更完整（无先例 → 2–3 个**整形状**竞争原型；“**同一形状的第二版不算**”；并给出**明确不适用条件**：既定模式的机械实现、目标明确的 bug fix/refactor）。 |
| **DEF-3** 周期性结构普查 | A2R-ABC MG-5；A1 G7 | **族已覆盖，机制本身具独立性。** A2R-ABC MG-5 拥有**周期性**复审（三结局 clean/changed/blocked、edit scope 限制、doc-drift 与产品回归三分、live pass 必做），A1 G7 拥有**引入顺序**（六信号判路径、四阶段、表征测试、棘轮自检）。**但两者都没有**：（i）**强度徽章作为“什么都没找到”的表达装置**（源文自陈“the framing pushes it toward producing candidates rather than concluding that nothing is wrong”，故徽章是唯一的诚实出口）；（ii）**普查产生的拒绝要落成可持久记录**（与 ABC MG-6 part B / A1 G6 交汇，应并入同一处）。我方增量**成立但收窄**为这两条。 |
| **DEF-6** 委派调查 | A2R-ABC MG-1 | **主体让位，且对方明显更强。** 对方 MG-1 含三支：`why` 的**完整覆盖图**（七类证据源、**记录 null 而不跳过检索**、只有“无可用 MCP”或“可证无关”才可跳过且必须写明理由）、**五档置信**（Direct → Supported → Inferred → Speculative → Unknown，其中 Unknown 也是有效结果）与**措辞规则**（because / the reason is / was designed to **只能**用于 Direct/Supported；Inferred 必须用 appears to / likely / suggests），以及输出契约与“转成 Preserve / Change / Avoid / Risk 约束集”；`how` 的 traced model；`attack-the-premise` 的前提审问（两次失败共享同一前提 → 写前提 + actor census + **移除不对称而非补偿** + 停止规则）。**这直接覆盖并超过我 DEF-6 的“只读一手来源 / 逐 claim 引用 / 降级未验证断言”。** 我方残余：**fact vs decision 的保质期判别**（研究产出短命资产、决定持久；把 fact 当 decision 归档会让陈旧前提变成承重假设）与 **delegation-depth 守卫**（已是 delegate 者自己做，不再转派）。**并注：** 我上一版提的“证据不能变红就不是证据”整合机会，其最操作化的形式很可能就是对方的**措辞规则**——建议以它为家，而不是新建第五处。 |
| **DEF-11** 长文草稿 | A2R-ABC2 MG-2 / MG-3；**MG-4 的 `teach`** | **不重叠，增量成立；且应并入 MG-4 的说明规范。** MG-2 是**代码/设计形态**（experience-first、design-space、laziness、reader-load），MG-3 是**原则语言与偏好沉淀**，均非文稿写作。**MG-4 的 `teach` 是“向人类做一次性说明”**，与长文写作不同域，但含四条可直接复用的规范：**不给 framing labels**（“one idea to hold onto”“TL;DR”等）、**回复就是说明本身、绝不是关于你做了什么/交付了什么**、**最小完整答案先行再停**、**图示逐张搭建**（≥3 个活动部件不要一张画全）。**我方增量成立：** grounding 规则（前置概念 vs 文中引入；**双向失效**——前置要求太多会挡住读者，文中铺垫太多会让开头淹死在定义里；单位是**概念**不是词）与**共享文档写入节奏**（每次写前从磁盘重读、只追加不覆盖、把“改这段/删上一条/合并这两条”当一等指令）。 |
| **DEF-12** 机械违例→确定性检查 | A2R-ABC2 MG-3 `encode-lessons-in-structure`；A1 G6 | **主体让位，对方更操作化。** MG-3 给出**触发**（“抓到自己在**第二次**写同一指令时”）、**机制强度阶梯**（**不可表示的状态**（编译不过）> lint 或 banned API（CI 失败）> canonical helper > runtime check）及理由（“agents copy whatever the surrounding code already does and **a weaker guard becomes the next template**”）、**capture → route → close** 的闭环（一次性→脑记；重复→skill/lint；系统性问题→principle）与三个反模式（只承认不记录 / 只记录不落地 / 修实例不推模式）。A1 G6 另补：**豁免必须写在检查器内并附理由，不得写在被检查对象里**（理由原句：“这样贡献者就不能通过编辑自己的技能文件来绕过校验器”）。**我方残余仅三条：** 无 guardrail **本身**是 finding（“an un-linted repo is a standing missed opportunity, not a neutral default”）、**先读项目已有的检查命令**（“已在但未接线或静默失效”本身才是 finding）、以及**按上下文压力分配标准所有权**（实现者上下文压力最大 → 标准由评审方持有而非实现方）。**并注：** 对方自己也标出本族与“不建 registry/框架”的张力，与我在 DEF-12/DEF-13 处置里的风险提示同源——两包应给出一致的措辞。 |
## (3) 补读后分类（25 组完整核账）

上一版按“确认重叠 12 / 弱依据 7 / 独立 7”分区。**补读后的分类如下，仍是观察而非裁定。**

```
A. 主体让位、仅留具名残余        9 组
B. 与对方结论存在张力、需 gate 裁定  2 组
C. 判断仍具独立性               14 组
合计                        25 组 ✓
```

### A · 主体让位、仅留具名残余（9）

| 组 | 让位于 | 我方保留的具名残余 |
| --- | --- | --- |
| ABC MG-1 | A2R-ABC2 MG-1 `skills/tdd` | 垂直切片/tracer bullet；refactoring 移出循环及其理由；接缝约定前置 |
| ABC MG-3 | A2R-ABC2 MG-1 `test-behavior-not-implementation` | 与接缝链的连接（F 按约定面核对 ⇒ 坏测试判定须落在约定面上） |
| ABC MG-6 | A1 G6（负结果留存） | 三闸全中才记 + 最小记录 + 七类合格范畴；拒绝记录的**持久性判别**（延期 ≠ 拒绝；“已实现”不得入拒绝台账） |
| ABC MG-8 | A2R-ABC2 MG-3（principle names） | 指针**措辞**工程；no-op 检验的模型相对性；否定指令失效模式；面向 agent 文档的框架 |
| ABC MG-10 | A2R-ABC MG-4（不强制抽象门槛）+ A2R-ABC2 MG-2（reader-load） | 被拒框架及其理由（interface ≠ TS 关键字；boundary 撞词） |
| DEF-6 | A2R-ABC MG-1（`why` 覆盖图 + 五档置信 + 措辞规则） | fact vs decision 的保质期判别；delegation-depth 守卫 |
| DEF-12 | A2R-ABC2 MG-3（encode-lessons-in-structure） | 无 guardrail 本身是 finding；先读既有检查命令；按上下文压力分配标准所有权 |
| DEF-13 | A2R-ABC MG-5 | 把规则落在**机械检查**这一载体类别；写明检查抓不到什么 |
| DEF-14 | A2R-ABC MG-5 + A2R-ABC2 MG-5 | 非篡改 `--check` 模式 + 写后断言 + 最小写入；目标不对即拒绝 |

### B · 存在张力，需 gate 裁定（2）

| 组 | 张力 |
| --- | --- |
| **DEF-9** | 我方前提是“写一份转移文档、已落盘者只引用不复写”；**A1 G4 主张“产物即交接”，并把“另写交接总结”列为第二份真源的失败模式**。二者不是措辞差异而是取向差异。另 A2R-ABC MG-7 以五值证据等级把“未证”细分到可操作，超过我方“降级未验证断言”。**建议**：DEF-9 收敛为“可移植性触发 + 分叉案例”，其余让位于 A1 G4/MG-7。 |
| **DEF-2** | 三方向张力：A1 G3 = 单一二值裁决 + 轴内杠杆排序；A2R-ABC MG-6 = 多透镜合成 + lead judgment 四桶（**它确实合并**）；我方 = 两轴产出后**禁止合并、禁止跨轴排序**。对“评审结论能否合并”三种答案。**建议**：以我方反混淆规则作为对 MG-6 合成步的**约束条款**（允许 four-bucket 分类，但禁止把一条轴上的失败并入另一条轴的成功），而非独立第四种评审形态。 |

### C · 判断仍具独立性（14）

判据：补读后仍**未见**更强的家；或族有对应家但机制本身未见对应。仍是观察，非裁定。

| 组 | 机制 | 未见对应家的补读依据 |
| --- | --- | --- |
| ABC MG-2 | demo-path 一问句（“这个做完能演示什么”）；expand→migrate→contract 及其 green-only-there 兜底 | A2R-ABC2 MG-1 `sequence-verifiable-units` 是执行单元的可验证性，非切分方式；无 wide-refactor 例外 |
| ABC MG-4 | **接缝约定作为已接受契约项**（既有 > 新、取最高、趋向一条；由下游按约定面核对；绑定经由契约文件故须在有全貌时定） | 三包无接缝组；A2R-ABC MG-5 是验证工具链、MG-6 是评审裁决，均非“约定测试面” |
| ABC MG-5 | **可失败的接受判据**（点名证伪观察 + 确认基点版本为红；三形状） | A1 G5 是“常备门槛 vs 本次验收条件的分离”，**问题不同**（分离 ≠ 能否失败） |
| ABC MG-7 | 术语纪律 `_Avoid_`（决议一词时同时记录被放弃的词）；定义 what it IS；项目特有概念过滤；陈述↔代码对质及其范围限制 | A2R-ABC MG-4 是领域**结构**选型，非术语存留机制 |
| ABC MG-9 | **排程**：设计树 / frontier / 逐轮问整 frontier / 同轮不得互相依赖 / 重算而非预写 / “frontier 空 + 人类确认”收束 | A2R-ABC MG-2 只有**分类**（哪些问题不该问人类）没有排程；另建议并入其四档置信（含 contradicted → 先问） |
| ABC MG-11 | 每仓配置**运行时读取**而非硬编码；canonical 词汇 + 可编辑本地映射；“tracker 是 setup 答案不是方法属性”；再同步触发 | 三包无配置面/再同步面分组 |
| DEF-1 | phase **gate 表**；tightness 四性质与校准；**以“提高复现率”为目标**的非确定性缺陷；最小化完成条件；预测试假设排序检查点 | A2R-ABC2 MG-1 `fix-root-causes` 是同族但无 gate 结构、无 tightness 校准、无复现率目标。**应补入**对方的“重启类先怀疑状态” |
| DEF-3 | **强度徽章作为“什么都没找到”的表达装置**；普查产生的拒绝落成可持久记录 | A2R-ABC MG-5 是验证 skill 的维护、A1 G7 是引入顺序，两者均无诚实出口装置与拒绝落点 |
| DEF-4 | 迷雾下多会话规划：destination 先行定范围；map 是索引不是仓库；**模糊度与范围两轴分离**（条目 / fog / out of scope，fog 永不毕业）；先认领后开工；plan-don't-do 及“可自编辑约束不是约束”的结构教训 | 三包无对应；A1 G7 是引入门槛的顺序，非迷雾规划 |
| DEF-5 | 原型的**证据保全**（留 main 之外分支 + 从实现记录指针指回）与**非作者可驱动**这一载体要求 | A2R-ABC MG-2 prototype playbook 有“决定先行/多候选/在匹配 surface 观察”，但明说输出是“决定 + throwaway artifact”，未表述保全与可驱动性 |
| DEF-7 | 人工程序：固定库/作者只写阶段（字面 marker）；从环境推导输入；每值三问；先开 URL 再取值；**不可端到端执行产物的静态校验 + 逐值落点 trace** | A2R-ABC MG-5 的“未执行即 draft”针对验证 skill；“人工程序”这一载体与静态 trace 法未见 |
| DEF-8 | 合并先追意图后看 diff；兼容则保双方、不兼容按目标取舍并说出让掉了什么；**“合并是最容易产出两边都满足、两边测试都不过的代码的地方”**故提交前先跑本项目检查 | A2R-ABC2 MG-1 只有“先 rebase 到干净 trunk”的基点规则 |
| DEF-10 | **difficulty 符号随阶段反转**（理解期是敌人 / 能力期是工具）；coverage 不是 learning 的记录门与 supersede-by-marking；**复用预测决定载体** | A2R-ABC2 MG-4 的 `teach` 只覆盖理解期并**明确反对 quiz/演练**，故未覆盖能力期；MG-3 是偏好沉淀非学习工作区。**本组获跨源印证**（两源在同一不对称性上相容）。建议并入其“hedge 是 finding，不是文风”与“最小完整答案先行再停” |
| DEF-11 | grounding 规则（前置/引入；双向失效；单位是概念）；共享文档写入节奏（每次写前重读、只追加不覆盖、编辑指令为一等指令） | MG-2 是代码/设计形态、MG-3 是原则语言；MG-4 的 `teach` 是一次性说明，非长文写作。建议并入其四条说明规范 |

### 附 · 由他仓拥有、我方未覆盖但与本包主体现状高度相关的一条

**A1 G7「在存量工作里引入门槛的顺序」**：六信号判路径（代码龄/覆盖/约定/团队习惯/爆炸半径/采纳策略）、增量四阶段（只读与保护 → 先测后改：**表征测试只钉现状不夹带修正**、“Beyonce 规则：若已依赖某行为就该给它测试” → 两速并存 + 交界处契约先行 → 回收与观测）、**Chesterton's Fence**（那个古怪的重试循环可能是承重的）、**棘轮**（“过一段时间后你能说出**现在被强制而过去没有**的是什么吗？说不出来就是推广停滞”）、以及五条采纳期反模式（大爆炸式采纳 / 放任重构无测试代码 / 以代码即文档为由跳过上下文 / 默认把遗留行为当错 / 不棘轮）。A1 自评“我方未覆盖”，与我补读所见一致。**这与本包当前处境直接相关**（把一套方法库引入一个已在运行的工作体系）；作为 A3 的观察列出，采纳与否属 gate。
## (附) 补读执行记录

**本轮已完成的补读**（只读他仓包正文的相关段落，未读全仓、未改他人文档）：

| 优先级（上一版所列） | 是否完成 | 读了什么 |
| --- | --- | --- |
| 1. A1 G3 正文 | ✅ | `G3.1`–`G3.4`（机制、源锚、五轴探针、分级与判决序、覆盖与十个缺口） |
| 2. A2R-ABC2 MG-2、MG-3 正文 | ✅ | 两组 `1)`–`4)`（机制段 + 覆盖段） |
| 3. A2R-ABC MG-4 正文 | ✅ | 整组（`1)`–`6)`） |
| 4. A1 G4、A2R-ABC MG-7、A2R-ABC2 MG-4 正文 | ✅ | 三组 `1)`–`4)` |
| 5. A2R-ABC2 MG-1 `blast-radius` | ✅（上一轮即已逐字读到） | 该支机制段（五级置信阶梯、安全性所依赖的那个事实、看 grep 停下的地方、confirmed 与 cleared 分开） |

**为完整性额外补读**（不在上一版最小集内，但为归并判断所需）：A1 **G6**、A1 **G7**、A2R-ABC **MG-1**、A2R-ABC **MG-6** 的 `1)`–`4)`。

**仍未读**：A1 G1/G2/G5 正文；A2R-ABC MG-3/MG-5/MG-8 正文（MG-5 上一轮已逐字读机制段）；A2R-ABC2 MG-1/MG-5 正文（均已逐字读过）。**这些不构成本文件任何条目的依据**，故不影响上文结论；若日后 gate 需要，按同一有界方式补读即可。

**补读带来的三处新发现**（上一版不可见）：
1. **DEF-9 与 A1 G4 存在取向冲突**（“产物即交接”vs“另写转移文档”），非单纯重叠——已升级为 B 类待裁定。
2. **DEF-2 处于三方向张力**（单一二值裁决 / 多透镜合成四桶 / 禁止跨轴合并）——已升级为 B 类待裁定。
3. **A2R-ABC MG-1 的五档置信与措辞规则**很可能是我上一版所提“证据不能变红就不是证据”整合机会的**最操作化既有形式**——建议以它为家，避免新建第五处。
## 边界

- 本文件**不含**任何采纳/限缩/拒绝/暂缓结论，也不建议优先级；`确认高重叠` / `需归并但低置信` /
  `仍具独立性` 三个标签是**对位状态描述**，不是裁定。
- 未改产品、未改他人文档、未建 registry/框架、未 commit。
- 未执行任何验证；未重读 matt 源仓原文。
- **证据级别现已全部升级为正文级**：上一版的 12 条比对与 7 组弱依据对位，其相关他仓正文（A1 G3/G4/G6/G7、A2R-ABC MG-1/MG-4/MG-6/MG-7、A2R-ABC2 MG-2/MG-3/MG-4）已于本轮逐字补读，逐条结论见 §2 各条目与 §(2b)。**仍未读的段落已在 §(附) 列明**，且不构成本文件任何条目的依据。
