# Round 1 · TIM Professional Workflow 重构任务卡

- 任务：把本仓从"流程库"改造成"工程经验库"，并修掉全部断档。
- 交付者：worker session（独立上下文）
- 计划者/审查者：planner session（本卡作者，不写实现）
- 授权：本仓内任意改动；**不得**改动 `/Users/yuantian/Developer/ekunai/...`（只读参考）
- 提交要求：**不要 commit**。把工作树留成可 `git diff` 的状态供 review。

---

## 0. 一句话目标

> 一个 session 被注入**一个角色文件**之后，就知道自己该收什么、该交出什么、怎么判断、什么时候不算做完。
> 工程经验装在**角色**里，流程薄到只有 Driver 读一份，不依赖任何具体 harness，不依赖任何本机全局技能。

---

## 1. 必须先读（不要跳过）

| 顺序 | 路径 | 读它是为了 |
|---|---|---|
| 1 | `docs/TIM-PROFESSIONAL-WORKFLOW-PROPOSAL.md` | 背景与原始意图。**不是权威**，与本卡冲突时以本卡为准 |
| 2 | `docs/TIM-PROFESSIONAL-WORKFLOW-PROPOSAL_REVIEW_R2.md` | 内容层意见，多数成立。**但它主张"改成 12 个 skill"，与本卡的载体决定相反**——采纳它的内容批评，不采纳它的载体 |
| 3 | `upstreams/cursor-plugins/pstack/skills/` | 主要方法来源。**重点读带 `references/` 的那几个**（`how` / `why` / `architect` / `show-me-your-work` / `blast-radius`），它们的方法骨架和脚本都在 references 里 |
| 4 | `upstreams/mattpocock-skills/` | 方法来源 |
| 5 | `upstreams/addyosmani-agent-skills/skills/` | 方法来源。**注意：本仓 7 处死链里，有 4 个名字在这里真实存在**（`planning-and-task-breakdown` / `constraint-driven-development` / `incremental-implementation` / `git-workflow-and-versioning`） |
| 6 | `/Users/yuantian/Developer/ekunai/Unified-Customs-Bonded-Intelligence-Platform/docs/active/multi-agent-development-principles.md` + `docs/active/engineering-method-routing.md` | **真实消费方的契约**。只读参考，用来对齐产物形状与依赖分类；**不要**把它整段搬进本仓 |

---

## 2. Owner 的目标（判定标准，逐条必须满足）

1. **方法 > 流程**。流程只要薄到能让 Driver 干活即可；主体是工程经验。
2. **经验装进角色，不放在 skill 里**。角色的注入单元就是角色文件本身。
3. **Driver 是独立 session**，只做编排/交接/组织，不被执行、审查、验证的上下文污染。它只读一份流程文件。
4. **完全解耦**：不依赖任何具体 harness，不依赖本机全局技能，不搞厚 host 层。允许并鼓励脚本。
5. **厚薄可缩放**：同一套角色既能 9 个会话跑，也能 3 个会话跑，也能 1 个会话顺序跑。**但"实现者"与"判断者"永远不能合并在同一个 agent**。
6. **自洽无断档**：角色 ↔ 方法 ↔ 流水线阶段，一处都不能缺；没有死引用；单一版本源。
7. **充足且闭环**：证据不是"箭头画完了"，而是**上一环交出的东西就是下一环声明需要的输入**。
8. **深度吸收三仓，但必须裁决重复与冲突**：三仓互相重复或直接矛盾的地方，逐条给出采纳哪个、为什么，**不许默默挑一个**。
9. **工具解耦的判定线**：只有 `roles/driver.md` 提"检测当前工作环境的能力"；其余文件零工具字样。

### 2.1 注入契约：每个 agent 最终收到的是四层

```
第 1 层  工作纪律   ┐
第 2 层  工作方法   ┘ ← 来自 roles/<role>.md（本库提供，工具无关，稳定不变）
第 3 层  本轮工作流切片  ← 由 Driver 附加（本次任务图、依赖、写窗、验收口径）
第 4 层  工具安排        ← 由 Driver 附加（用哪个 harness、怎么开会话、怎么通信、怎么隔离）
```

由此产生两条对角色文件的硬要求：

- 角色文件必须**显式声明这个接缝**：本文件只提供第 1–2 层；第 3–4 层由 Driver 附加；并写明**Driver 附加的内容不得改变本角色的纪律与方法边界**（例如不能因为"这轮只开 3 个 agent"就让实现者给自己发 PASS）。
- 角色文件必须**单独注入即可开工**：不能假设第 3–4 层还会补充任何属于第 1–2 层的信息。

---

## 3. 已经定好的决定（不要重新讨论）

- **载体**：`skills/` 目录整体取消；经验写进 `roles/*.md`。
- **Oracle**：保留为第 9 个角色，定位为**触发条件下的独立复核者**。
  - **触发条件**（满足任一即启用）：改变接口形态 / 状态归属 / 权限 / 数据语义；存在 ≥2 个自洽方案；角色之间对方案或判据有争议；宣布"已闭合"之前的关键分叉。
  - **输出固定三件套**：`裁决 + 依据 + 一个能区分选项的实验`。判不开就明说"在当前证据下不可区分"，不要含糊表态。
  - **净收益来自独立性与可核对性，不来自模型更强**：同一个模型也可以有净收益，前提是它不读作者的叙述、只读产物与冻结契约，并且必须给出可核对的东西（区分性实验），而不是偏好。
  - **必须不留断档**：solo 档位或没有独立复核会话时，这份职责不消失——由 **fresh Reviewer**（不同 session、不读作者叙述）承担同一职责；但**不得由实现者本人承担**。
  - 角色文件里同时写一条更便宜的同源信号：**反实现挑战**——故意构造一个"能过现有检查但行为是错的"实现，看判据会不会红；红了说明判据有效，没红说明判据无效（这一步不需要第二个模型）。
  - Oracle **不得**当唯一闸门、不得替 Owner 授权、不得豁免验证、不得给 Owner 未授权的结论背书。
- **并行**：被串行化的只有**写窗**和**合并**，不是流水线。
- **Wave 协议**：属于个人作息，不是库的规范；移出核心。
- **薄/厚两条固定配方**：取消，改成"项目成熟度 × 本次变更风险"两条轴 + 装配档位。

---

## 4. 交付物与完成判据（DoD）

### D1 `roles/` × 9 个角色文件，每个自包含

固定结构（后面有机械检查，字段名不要改）：

```
---
role: <id>
title: <中文名>
---

# <角色名>

## 1. 使命
## 2. 我收到什么（输入契约）   ← 上一位交付的 artifact 名称 + 必需字段 + 前置条件；缺哪一条我不开工
## 3. 我必须交出什么（输出契约）← artifact 名称 + 字段 + 下一步是谁、凭什么开工
## 4. 我的工程方法              ← 主体
## 5. 权限边界（我可以 / 我不可以）
## 6. 升级条件（什么情况交给谁）
## 7. 退出判据（什么算做完，什么不算）
## 8. 常见自欺（≤4 条，每条必须指向一个具体动作，不是口号）
```

**第 4 节是这次交付的主体**，门槛：

- 写成**可执行程序**：触发条件 → 编号步骤 → 每步的判断依据 → 至少 2 个「反例 / 何时不适用」。
- **每条主张必须能追到出处**：要么指到 `upstreams/.../file:line`，要么是你这一步实测出来的（附命令与输出）。
  **写不出出处的句子，删掉。** 这是本次最重要的一条纪律——防止把"感觉是好实践"写成正文。
- 上游方法骨架**被丢掉的部分补回来**，至少：`why` 的置信度分级 / 证据覆盖（含空结果也要记）；`architect` 的 `references/design-red-flags.md` 四类红旗与「下次改动成本估算」；`blast-radius` 的「在真实运行的 app 里复现」这一档；`show-me-your-work` 的 append-only 决策台账。
- 禁止把上游的 harness 字段（`disable-model-invocation` 等）抄进来。
- 允许的唯一跨文件引用形式：指向 `roles/<name>.md`。**禁止**引用本机全局技能、`upstreams/`、`skills/`。

**角色 → 方法归属参考表**（可调整，但必须无断档）：

| 角色 | 承接的工程经验 | 主要上游 |
|---|---|---|
| Driver | 意图对齐与提问、任务分级与依赖分类、写窗与放行、批处理与并行、收口 | matt `grilling`；addy `interview-me` |
| Investigator | 真实路径追踪（第一次失真）、历史意图考古、因果归因、确定性反馈回路 | pstack `how`、`why`（+references）、`principle-attack-the-premise`；matt `diagnosing-bugs` |
| Architect | 接口与边界设计、深模块、非法状态不可表示、方案对照（含"不重构"）、红旗筛查 | pstack `architect`（+references）、matt `codebase-design` |
| Planner | 垂直切片、四类依赖、最小验证位置、任务卡字段 | addy `planning-and-task-breakdown`、`constraint-driven-development`；pstack `principle-sequence-verifiable-units` |
| Implementer | 行为 TDD、垂直增量、范围自律、交付固定候选 | addy `test-driven-development`、`incremental-implementation`；pstack `principle-test-behavior-not-implementation` |
| Reviewer | 对抗审查、双轴、阻断与建议分离、反实现挑战 | addy `doubt-driven-development`、`api-and-interface-design`；pstack `principle-prove-it-works` |
| Verifier | 真实路径驱动、判据可证伪性、三态结论、证据保管 | pstack `blast-radius`、`show-me-your-work`；addy `browser-testing-with-devtools`、`performance-optimization` |
| Integrator | 单写者合并、冲突语义判断、组合检查、证据复用判据 | addy `git-workflow-and-versioning`、`deprecation-and-migration`；pstack `principle-migrate-callers-then-delete-legacy-apis` |
| Oracle | 独立复核、区分性实验 | — |

### D1b 闭环矩阵（写进 `pipeline.md`，或单独一个 `closure.md`）

闭环不能只是箭头。必须有一张表，一行一个环节：

| 环节 | 承接角色 | 输入 = 上一环输出字段（逐字一致） | 输出字段 | 可跳过条件 | 跳过时职责移交给谁 |

硬要求：**每一条可跳过路径都必须有明确的职责移交，不能默认消失**。至少覆盖：

- 跳过调查（根因已明）→ 谁承担"第一次失真"的定位？
- 跳过设计（局部改动）→ 谁承担"调用者用法 + 方案对照"？
- solo 档位（一个 session 顺序跑）→ 谁保证"实现者 ≠ 判断者"？
- 没有第二模型 / 没有独立复核会话 → 独立复核由谁承接？

`check-library.py` 要能机械验证：矩阵里每个"输入字段"都能在上一行的"输出字段"里逐字找到。

### D2 `pipeline.md`（目标 ≤ 150 行）—— Driver 唯一读的流程

必须包含：

1. 拓扑：调查 → 设计 → 切片 → 实现 → 审查 → 验证 → 集成（含每步的交接物名称，与角色文件 §2/§3 逐字一致）。
2. **装配档位**：`solo(1)` / `trio(3)` / `full(9)` 的**角色归并表**。trio 参考：A=调查+设计+切片，B=实现，C=审查+验证+集成。
3. **不可合并的边界**（硬规则）：实现者 ≠ 判断者；Driver 不实现；集成只有一个写者；Oracle 不产生 Owner 权限。
4. **四类依赖**：接口冻结 / 写权释放 / 资源可用 / 证据资格（下游只等它真需要的那一类）。
5. **并行批处理**：逐项问四个问题（同一字段状态权限接口？同一文件或符号？共享可写资源？等同一未冻结接口？）→ 分 A/B/C/D 类 → A 类实现/审查/验证三路并发、只在合并排队；串行的只有写窗与合并。
6. **写窗**：冻结候选 + 接收确认才交权；定向返修 = 新候选 + 新冻结。
7. **停止条件**：同一故障两轮无新证据 → 停手，重新归因或挂起（不要第三个补丁）。
8. **证据复用判据**（**不要写"基线一动前序 PASS 全部作废"**）：覆盖目标断言 ∧ 相关实现未变（或变化已证实在依赖范围外）∧ 运行条件等价 ∧ 决定未改变该断言的正确答案；执行者换人不在判据里。
9. **波次汇合**：一个批次要有一次在**合并后候选**上的旅程级验收；各项 PASS 的集合不等于交付。
10. **授权检查**：每一步推进前看当前有效授权；未授权就停在交付点。

### D3 `SOURCES.md` —— 六仓映射（诚实第一）

每行：`来源 repo / pinned SHA / 具体文件 / 保留了哪些机制 / 改写了什么与理由 / 删了什么与理由 / 落在哪个角色哪一节`。

- 3 个已有 clone（`cursor-plugins` / `mattpocock-skills` / `addyosmani-agent-skills`）**逐方法填满**，SHA 用 `git rev-parse HEAD` 实取。
- 另外几个来源（提案 §10 列的：Dex Horthy、Armin Ronacher、Jesse Vincent、Garry Tan）**显式标 `NOT ABSORBED`**，写清原因与下一轮计划。
- **不许把没做的事写成做了。** 顺便在文件开头如实记一句：本仓文档自身对上游数量的说法不一致（AGENTS.md/提案 §6 写 3 个 clone，Owner 的口径是 6 个来源），本表是唯一清单。

**冲突裁决表（独立一节，必须逐条给出，不许默默挑一个）**

三仓在若干主题上互相重复或直接冲突。逐条给：`争议主题 / 各方主张（附 file:line）/ TIM 采纳哪个 / 理由 / 影响了哪个角色哪一节`。至少覆盖下面这些（读料时发现的其他重复/冲突也要补进去）：

| 主题 | 冲突双方 |
|---|---|
| 注释与文档 | pstack `no-comments` / `principle-minimize-reader-load` vs addy `documentation-and-adrs` |
| 是否阻塞等人 | pstack `principle-never-block-on-the-human` vs matt / addy 的 spec 门禁 |
| 多模型盲审 | pstack `arena` + `principle-exhaust-the-design-space` vs 上下文与成本节制 |
| 量化门禁 | addy `constraint-driven-development` vs "指标必须来自用户要求或既有契约，不能由执行者发明" |
| TDD 严格性 | matt `tdd` 的 red-green vs pstack `principle-prove-it-works` 的证伪型交付（零生产 diff 也可以是有效交付） |
| 调查者的边界 | pstack `why` 要求出 Preserve/Change/Avoid/Risk vs "只交事实、不夹带方案" |

**裁决要给理由；写"综合两者"等于没裁。**

### D4 `scripts/` —— 两类脚本，都必须真跑一次并把输出写进报告

1. **吸收来的可移植脚本**：至少一份 append-only 决策台账 logger + 表头模板（参考 `upstreams/cursor-plugins/pstack/skills/show-me-your-work/scripts/log.sh` 与 `references/decision-log-template.tsv`）。去 Cursor 耦合，改成本仓可用。
2. **自写 `scripts/check-library.py`**（只读，可重复运行），至少检查：
   - 每个角色文件 8 个必需节齐全、frontmatter 有 `role`/`title`；
   - 角色间的交叉引用只指向真实存在的 `roles/*.md`；
   - 角色 `§2 输入契约` 的字段名能在流水中前一位的 `§3 输出契约` 找到对应（**闭环检查**）；
   - 全仓无死链（README.md / AGENTS.md / pipeline.md 提到的路径都真实存在）；
   - 版本号单一来源。
   - 输出必须是可读的三态/计数形式，退出码有意义（0 全通过 / 非 0 有失败）。

### D5 `README.md`（≤ 80 行）

这是什么 / 给谁 / **harness 必须提供的 4 个原语**（角色注入进 session、session 隔离、会话间消息、工作区隔离）/ 怎么把角色注入 session（只写"需要什么效果"，**不写任何具体 harness 命令**）/ 三个档位怎么选 / 目录说明。

### D6 清理

- `workflows/wave-protocol.md`、`workflows/thin-bugfix.md`、`workflows/thick-cross-boundary.md`、整个 `skills/` → 移到 `docs/archive/`（**保留历史，不删除**）。
- 修 `AGENTS.md` 的漂移（`wave-execution.md`、`evals/`、`read-only-investigation.md`、`perf-optimization.md` 都不存在），并让它与新的目录结构一致。
- 版本号统一到一个来源（`VERSION`）。当前有三处不一致：`VERSION=0.1.0-draft` / frontmatter `1.0.0` / 提案 `1.0-final`。

### D7 `.pi/round1/REPORT.md`

做了什么 / 脚本实跑输出（原样贴）/ 没做什么与原因 / 残余不确定性 / 下一轮接手要看什么。

---

## 5. 硬约束

- 不 commit；工作树留 dirty 供 review。
- 不动 `docs/TIM-PROFESSIONAL-WORKFLOW-PROPOSAL_REVIEW_R2.md`（Owner 的未跟踪文件）和 `.pi/` 里原有的 loops 文件。
- 不为没有消费者角色的需求新增抽象；能删的机制优先删，不要让它更可配置。
- **工具解耦的判定线**：`roles/driver.md` **以外**的任何文件，不得出现任何具体 harness 名称或命令；`roles/driver.md` 里**恰好一处**提"检测当前工作环境的能力（能否开独立会话 / 能否会话间通信 / 能否隔离工作区 / 有哪些模型档位），据此决定本轮怎么装配"——**只写需要什么能力，不写任何具体命令**。`check-library.py` 必须能机械抓到违反。
  - **扫描范围（Owner 已批准的裁决）**：只扫本库自有、可注入/可发布的文件 —— `roles/**`、`pipeline.md`、`closure.md`、`README.md`、`AGENTS.md`、`SOURCES.md`、`scripts/**`、`VERSION`。
  - **显式排除**：`docs/**`（历史与归档）与 `.pi/**`（工作区）—— 这两处必然含历史 harness 名称，且部分文件已被冻结不可改。`upstreams/**` 是只读溯源路径，按路径豁免（路径名不是指令）。
  - **排除范围必须打印在 `check-library.py` 的输出里**，不得隐含。
- 不得把"猜 Owner 偏好"写成一种授权。
- 中文为主；代码、路径、命令、上游原文引用保持原样。

---

## 6. 完成后必须回答的三个问题（写进 REPORT）

1. 每个角色文件被单独注入时，**它需要的信息是否都在文件里**？举一个你自己发现的信息缺口。
2. `check-library.py` 实际抓到了什么？**如果它一条都没抓到**，说明它没用——那就改写它直到它能抓到至少一条真实问题。
3. 还有哪一处"看起来闭环、实际没闭环"？如实列出来，不要修饰。
