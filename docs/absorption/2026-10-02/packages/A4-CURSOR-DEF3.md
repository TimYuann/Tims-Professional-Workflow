# A4-CURSOR-DEF3 · cursor-plugins 审核包 3（orchestrate schemas/cli/tests 正文：机制级内容判定与抽取）

- 实例/角色：`tpw-absorb-a4`（A 类发现者；只产出审核包，不裁定采纳）。
- 源仓与 pin：`cursor-plugins` @ `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`。
- 只读 locator：`.worktrees/legacy-pre-night-2026-10-01/upstreams/cursor-plugins`；本 session 未 checkout、未执行、未写源、未 commit。
- 前置：`A4-CURSOR-DEF.md` G-01..G-03、G-14/T-06；`A4-CURSOR-DEF2.md`。
- 判定：**有机制级内容**，故按包格式出本文件；不是"无新增机制"分支。与 DEF1 的关系：G-01/G-02/G-03 已覆盖 runtime 行为契约（循环、交接、失败分类、Andon/操作者边界）；本包补 DEF1 明确留白的**精确接口层**——计划/状态的 schema 校验、分支与合并任务的命名不变量、提示词装配契约、CLI 操作面、模型目录与探测器、提示注入加固。不重述 G-01..G-03 已写的机制。

---

## 0 · 读深声明

**pin 内逐字全读（本包新增）**：

- `orchestrate/skills/orchestrate/scripts/schemas.ts`（选段全读：1–110、110–196、196–370、366–460、540–660、655–720）。
- `scripts/cli/util.ts`（全文）、`scripts/cli/task.ts`（全文）、`scripts/models.ts`（全文）、`scripts/tools/{probe-models,generate-json-schemas}.ts`（全文）、`scripts/tools/nudge-root.ts`（前 120 行 + 头注释）、`scripts/core/branches.ts`（全文）、`scripts/core/prompts.ts`（14–110、245–305）。
- 测试正文：`__tests__/operator-boundary.test.ts`（全文）、`__tests__/slack-channel-boundary.test.ts`（全文）、`__tests__/kickoff-dedupe.test.ts`（1–140）、`__tests__/worker-branch-discipline.test.ts`（1–80）、`__tests__/schemas.test.ts`（1–160）、`__tests__/checkpoint-restart.test.ts`（1–145）；其余测试仅标题级。

**本包未读（保留为残余，不评估）**：`scripts/cli/{index,inspect,forensics,comments,andon}.ts`、`scripts/cli.ts`、`scripts/adapters/{index.ts,types.ts,slack/{client.ts,index.ts}}`、`scripts/errors.ts`、`scripts/tools/nudge-root.ts` 的后半、`scripts/schemas/plan.schema.json` 与 `state.schema.json` 全文（只知其为 zod 生成物）、`biome.json`/`tsconfig.json`/`package.json`/`bun.lock`、`__tests__/` 其余测试正文。

---

## J-01 · 计划与状态的可执行契约（schema 层）

### 1) 机制与触发情境；源锚点与已读

触发情境：planner 手写 JSON、脚本机器写 JSON、崩溃后重读 JSON；需要在**分发任何工作前**拒绝结构性错误的计划，并让迁移/漂移的旧字段以可读错误退出，而不是中途崩。

源锚点（pin 内）：`scripts/schemas.ts` + `__tests__/schemas.test.ts`。

- 命名：`TASK_NAME_RE=/^[a-z0-9-]+$/`（kebab-case ascii；任务名进 branch 与 prompt，正则兼作路径穿越防线）。
- 类型判别：`TaskTypeSchema` worker/subplanner/verifier；`VerifierTaskSchema` 要求 `verifies`，worker/subplanner 的 `verifies` 为 `undefined`（`nonVerifierVerifiesSchema` 带 `invalid_type_error: "is only valid when type is verifier"`）；`PlanTaskSchema` 是 `discriminatedUnion("type")`。
- 严格性：`PlanObjectSchema`/各 task schema `.strict()`（未知字段直接失败）；`MeasurementSpecSchema`/parser `.strict()`。
- `PlanSchema.superRefine`：tasks 非空；**重名**；verifier **不能验证自己**、`verifies` 必须是已知任务；`dependsOn` 必须已知、不能自依赖；三色 DFS 检出 **依赖环** 并打印环路径；verifier 的 `dependsOn` 自动并入其 target（`normalizedDependsOn`）。
- 状态：`TaskStateSchema` 显式列全部字段（agentId/runId/parentAgentId/status/resultStatus/handoffPath/attempts/failureMode/verification 等），`.strict()`；`StateSchema` 含 `attention` 数组与可选 `andon`；可空字段有默认值；`verification` 枚举与 `FAILURE_MODE_VALUES` 从同一 schema 导出（与 `core/handoff.ts` 的解析共用常量）。
- 迁移：`deletedTrackerFields`（tracker/linearTeam/trackerRef/parentTrackerRef/controlRef/slack）在解析 plan 时**先于 zod** 拒绝并给出迁移指引（"删 plan.slack，用 plan.slackChannel；外部 tracker 让 agent 运行时直调 MCP"）；`normalizeLegacyStateValue` 在读 state 时静默剥离 `tasks[].trackerRef`。
- 容错遍历：`parseTreeStateJson` 对 root 与单个 task 用 safeParse，坏的丢掉而不是整棵树失败（kill-tree/crawl 仍能工作）；`formatZodIssues` 输出 `path: message` 列表。

测试级证据（正文级，非标题）：`PlanSchema rejects verifier that targets missing task`（断言错误文本含 `verifies unknown task`）；`PlanSchema rejects removed tracker fields`；`parsePlanJson rejects legacy plan.slack with a migration error`（断言抛错含 `plan.slackKickoffRef`）；`parsePlanJson preserves script-written task slackTs`。

### 2) 操作、成立条件、失败模式、反例

- **把不变量放进 schema，而不是放进运行期循环**：重名、未知依赖、环、verifier 目标、非法任务名都在"启动前"失败；错误文本是给人看的（迁移指引）。
- **状态与计划用同一常量源**：verdict/failure 枚举从 schema 导出，避免解析器与校验器分叉。
- **严格但可诊断**：`.strict()` 拒绝未知字段，同时 `formatZodIssues` 给出精确路径；迁移字段走专门错误而不是通用 "unrecognized key"。
- **容错读**：遍历类读取（tree/crawl）对坏根/坏行降级，而不是让一个坏行藏住整棵子树。
- 失败模式/反例：用宽松 schema 让 cyclic plan 通过 → 循环永远不 spawn 或死等；把 verifier 指向不存在任务 → 运行期才炸；把 tracker 字段静默丢弃 → 用户不知为何行为变化；traversal 因单行损坏而整树不可见。

### 3) A–F 判断位点与专业 concern

| 位点 | concern | 何时调用 | Profile |
| --- | --- | --- | --- |
| D：把跨边界不变量做成可执行契约 | 接口/可靠性 | 多实例共享的计划/状态 | `technical-planning` |
| F：校验器的诚实边界（schema 能否证明语义） | 证据/边界 | 依赖"校验通过"作判断 | `evidence-evaluation` |
| E：迁移/宽松读的实现 | 实现/运维 | 演进 schema | `implementation` |

### 4) 当前产品锚点、覆盖与缺口

- 已覆盖：`cross-module-design.md` 的接口事实与"错误行为可预测"；`methods/README.md` 的"机器可核项 vs 专业判断"；`profiles/evidence-evaluation.md` 的"字段非空不是验证"。
- 缺口：**"可执行契约"的具体形态**——判别联合 + 严格解析 + 跨字段 refine（重名/环/目标存在）+ 迁移错误 + 容错遍历。产品有原则，缺一个可抄的最小样例。

为何值得吸收：这是 D/E 把"边界校验"从口号变成代码的最短路径；且可用任何语言/库复现（不绑定 zod）。

### 5) 拟处置与载体

- 拟保留：不变量进 schema；错误文本含修复指引；枚举单一来源；严格 + 精确路径；容错遍历。
- 拟改变：zod/TypeScript 语法 → 通用"解析即校验"；`TASK_NAME_RE` 作为"命名同时影响路径安全"的例子。
- 拟删除：orchestrate 字段名（source anchor 保留）。
- 载体落点：并入 DEF1 G-12 的类型/边界方法作为"可执行契约"小节；`profiles/technical-planning.md` 按需入口一行。
- 仍依赖 runtime：真实解析库；无 schema 库时用等价的手写解析 + 测试。

### 6) 可讨论正文草稿/操作例子 + 验证方案

```markdown
## 可执行契约（最小形态）
- 判别联合表达变体；未知字段失败；错误给精确路径与修复指引。
- 跨字段不变量在解析层检查：重名、自依赖、未知名引用、依赖环；verifier 目标必须存在且不能是自己。
- 同一枚举由单一来源导出，解析器与校验器共用。
- 旧字段迁移：成功路径给出替代，失败文本说清怎么改；能安全降级的读路径（遍历）宽一点。
```

验证方案（**未执行**）：写 6 个负例（重名/自依赖/未知依赖/环/verifier 指向缺失/旧字段），确认每个在启动前失败且错误文本含修复指引；再写一个坏行状态的遍历读取，确认只丢坏行。边界：schema 通过 ≠ 语义正确（与 `profiles/evidence-evaluation.md` 一致）。

---

## J-02 · 分支与合并任务的命名不变量

### 1) 机制与触发情境；源锚点与已读

触发情境：多 worker 各自在独立分支上工作，下游任务要按上游**实际分支**取上下文；若 worker 自选分支名，`dependsOn` 的语义就不成立。

源锚点（pin 内）：`scripts/core/branches.ts`（全文）、`scripts/core/prompts.ts` 的 `renderMergeDiscipline`、`__tests__/worker-branch-discipline.test.ts`（正文 1–80）。

- `plannedBranchForTask` = `orch/<rootSlug>/<taskName>`；若任务名匹配 `^merge-(.+)$` 且类型 worker，则目标是 `orch/<rootSlug>/<slice>`（合并任务落在 slice 分支）。
- `mergeWorkerSourceBranches`：只从 `dependsOn` 中取非合并型 worker，按 `dependsOn` 顺序返回它们的 planned branch。
- `AgentManager.branchForTask` 对普通 worker 做**断言**：实际分支必须等于 planned branch，否则抛 `"<task>: branch must be orch/<root>/<task>, got <actual>"`（测试正文覆盖）。
- 提示词侧：普通 worker 的 prompt 含 `Push exactly \`orch/<root>/<task>\``；合并 worker 的 prompt 明确 `This is a merge worker for slice \`<slice>\``、按 `dependsOn` 顺序逐个合并、只推目标分支（测试正文断言顺序与文本）。

### 2) 操作、成立条件、失败模式、反例

- **命名不是风格问题，是依赖语义的锚点**：下游按名字解析上游分支；worker 改名 → 链路断裂。
- **合并任务也是任务**：`merge-<slice>` 命名约定同时决定目标分支与 source 列表，planner 只需要写 `dependsOn`。
- **断言优先于信任**：与其在 handoff 里"注意分支名"，不如在读取状态时直接拒绝不一致。
- 失败模式/反例：worker 自选分支名；把非 worker 命名为 `merge-*`；合并任务漏写 dependsOn 导致 source 为空；下游依赖一个尚未交接的分支（DEF1 G-02 已给 relay 规则）。

### 3) A–F 判断位点与专业 concern

| 位点 | concern | 何时调用 | Profile |
| --- | --- | --- | --- |
| D：依赖的物理锚点（分支/版本） | 接口/版本 | 多写者并行 | `technical-planning` |
| E：命名/断言的实现 | 实现/可靠性 | 实现编排器 | `implementation` |
| Driver：写集与合并顺序 | 程序性 | 合并与集成 | `driver` |

### 4) 当前产品锚点、覆盖与缺口

- 已覆盖：`profiles/driver.md` 的写集/单写者；DEF1 G-04 的单写者文件。
- 缺口：**"依赖锚在物理对象上并用断言维持"**——名字派生、合并约定、运行时校验、prompt 与实现一致。

为何值得吸收：任何并行写者/分支体系都需要"依赖可解析"的物理锚点；这是 D/E 交界的高频失败面。

### 5) 拟处置与载体

- 拟保留：名字派生分支；合并任务的命名约定与 source 顺序；实际分支必须等于计划分支的断言；prompt 明示唯一可推分支。
- 拟改变：`orch/` 前缀与 git 语义 → "每个写者一个可解析的隔离标识（分支/目录/命名空间）"。
- 拟删除：orchestrate CLI 名。
- 载体落点：并入 DEF1 G-04（共享写面）或 G-11（多单元交付）的"隔离锚点"小节；不新建方法。
- 仍依赖 runtime：真实 VCS/隔离机制；无 VCS 时用目录/命名空间等价。

### 6) 可讨论正文草稿/操作例子 + 验证方案

```markdown
## 依赖的物理锚点（操作）
- 每个写者的隔离对象名从"根 + 任务名"派生，不由写者自选；下游按名字解析上游产物。
- 合并/集成是普通任务，命名约定同时给出目标与来源顺序；来源来自声明的依赖，不手工列举。
- 读取时断言实际锚点等于计划锚点，不一致立即失败；提示词里写明"只能推这一个"。
```

验证方案（**未执行**）：mock 一个写者改名，确认被断言拒绝；mock 合并任务漏 dependsOn，确认 source 为空且被检查；确认 prompt 文本与派生规则一致。边界：非 VCS 环境用等价命名空间规则。

---

## J-03 · 提示词装配契约（模板与上游 relay）

### 1) 机制与触发情境；源锚点与已读

触发情境：spawn 的 prompt 是 worker 唯一输入；模板有占位符；下游需要上游 handoff；没有 Slack/Andon 时不应渲染相关块。

源锚点（pin 内）：`scripts/core/prompts.ts`（`renderPromptTemplate`、`buildUpstreamHandoffsSection`、`buildWorkerPrompt`/`buildVerifierPrompt`/`buildSubplannerPrompt` 签名面、`renderMergeDiscipline`、`buildSlackBlock`、`buildInlineBriefBlock`）+ `prompts/*.md`（DEF1 已读）。

- `renderPromptTemplate`：模板缓存；逐 key `replaceAll("{{key}}", value)`；**渲染后检查残留占位符**，有则抛 `template "<name>" has unrendered placeholders: ...`——模板漂移在装配时失败，而不是把 `{{...}}` 送进模型。
- `buildUpstreamHandoffsSection`：按 `dependsOn`（verifier 自动并入 target）取上游 handoff，**去掉 traceability 注释后逐字粘贴**；缺失时插入明确的"(no handoff on disk — planner spawned this task without waiting; treat as missing context)"，不静默省略。
- 装配顺序/条件：`buildPromptScopedGoal` 把 `brief` 作为 `Task brief:` 前缀；`renderMergeDiscipline` 只在 merge worker 时插入；`buildSlackBlock` 在无 `slackKickoffRef` 时返回空串（不渲染空块）；`agentIdFlag` 在无 agentId 时完全省略（避免 `--agent-id  --workspace` 这种畸形命令）。
- `renderPrompt` 的 CLI 预览路径：无 agentId 时仍渲染（slack 块不带 flag），保证 `prompt` 子命令可用。

### 2) 操作、成立条件、失败模式、反例

- **模板是契约**：残留占位符必须硬失败；否则模型会看到字面 `{{goal}}`。
- **payload 随依赖流动**：`dependsOn` 不只是调度门，装配时把上游产出粘进下游；缺失要有显式标记，让下游知道自己在猜。
- **条件装配**：可选块（Slack/Andon/merge）只在适用时插入，避免"空块"污染注意力；flag 缺失时不要输出空参数。
- 失败模式/反例：模板加新占位符但调用方没传 → 静默漏渲染；上游未交接仍 spawn → 下游无上下文（DEF1 G-02 的 relay 规则）；把上游 handoff 做摘要（污染来源）；无 Slack 仍渲染空的 Slack 段。

### 3) A–F 判断位点与专业 concern

| 位点 | concern | 何时调用 | Profile |
| --- | --- | --- | --- |
| D：装配契约与依赖 payload | 接口/行为传递 | 生成子实例提示词 | `technical-planning` |
| E：模板渲染/条件块实现 | 实现 | 实现 spawn 器 | `implementation` |
| F：缺失上下文要显式 | 证据/完整性 | 下游凭上游结论工作时 | `evidence-evaluation` |

### 4) 当前产品锚点、覆盖与缺口

- 已覆盖：`charters/template.md` 的交接字段、`profiles/*` 的"下游能找到结论/条件/依据"。
- 缺口：**模板装配的可失败检查**（残留占位符）、**上游 payload 的逐字 relay 与缺失标记**、**可选块/参数的条件装配**。产品讲责任交接的语义，缺生成器的操作纪律。

为何值得吸收：任何"生成子任务提示词"的编排都需要这三条，且与 DEF1 G-02（交接唯一通道）互补。

### 5) 拟处置与载体

- 拟保留：残留占位符失败；逐字 relay + 缺失标记；可选块条件渲染；空参数不输出。
- 拟改变：`{{var}}` 语法 → "模板占位符"；Slack/Andon 专属块 → 可选上下文章节。
- 拟删除：orchestrate 模板名。
- 载体落点：并入 DEF1 G-02/G-04 的装配小节；不单独成方法。
- 仍依赖 runtime：无（纯装配逻辑）。

### 6) 可讨论正文草稿 + 验证方案

```markdown
## 子任务提示词装配（操作）
- 模板渲染后检查残留占位符，有则失败；缺值不静默。
- 声明的依赖必须把上游产出（原文）粘进下游；缺产出写显式"缺失上下文"标记。
- 可选章节（外部通道/集成/合并）只在适用时出现；参数缺失不输出空 flag。
```

验证方案（**未执行**）：模板故意留占位符 → 确认失败；上游缺 handoff → 确认出现缺失标记；无外部通道配置 → 确认不渲染空块。边界：无。

---

## J-04 · CLI 操作面：kickoff 去重、ad-hoc spawn、respawn、kill、crawl/kill-tree

### 1) 机制与触发情境；源锚点与已读

触发情境：同一个 goal 被重复 kickoff（浪费云代理）；失败任务要重试；要整树停摆；要查看/批量终止跨 branch 的树。

源锚点（pin 内）：`scripts/cli/task.ts`（全文）、`scripts/cli/util.ts`（全文）、`__tests__/kickoff-dedupe.test.ts`（1–140）。

- **kickoff 去重**：`findActiveRootPlanner` 在 cloud agent 列表里找**名字完全等于** `<rootSlug>-root`、创建时间在 30 分钟（`MAX_BOOT_MS`）内、且最新 run 状态为 `pending|running` 的代理；命中则打印 `adopting <id>` 并返回同结构 JSON（`adopted:true`），不新建；`--force` 跳过；不同 slug 可并行；**前缀不匹配**（"refactor" 不会 adopt "refactor-ui-root"）；`list` 未带 latest run 时回退 `listRuns`。rootSlug 从 goal 首行 `` `slug`: `` 前缀推断，否则取首行前 100 字符。
- **ad-hoc spawn**：只允许 worker/subplanner（拒绝 verifier）；同名且状态非 pending 直接拒绝并提示改名或 prune；`adHoc=true` 写入 state；`--wait` 等待并打印 handoff，否则提示 `tail`。
- **respawn**：只把终态（error/pruned）放回 pending；`--source` 限 `local-cli|self-planner|script-auto-retry`（记录是谁发起的）；`--cascade` 把传递依赖上的 `pruned` 行一并重置（`transitivelyDependsOn` 走 dependsOn 图）。
- **kill**：无 task 参数 = 取消所有 running + prune 所有 pending；带 task = 默认 cascade-prune 依赖者，`--no-cascade` 只停自己；**未加 `-y` 时打印将停止的清单并退出 1**（需要显式确认）；返回 cancelled/pruned 计数。
- **crawl/kill-tree**：从 `origin/<branch>:.orchestrate/<slug>/state.json` 读树（不要求本地 checkout）；`crawlBranch` 递归 subplanner 分支并做 `branch:slug` **visited 环检测**（打印 cycle detected）；`collectRunningAgentsInTree` 只收 `running` 且带 agentId+runId 的行，坏行不影响更深层；`filterVictimsToSubtree` 按 `parentAgentId` 祖先链过滤（`kill-tree --agent-id` 用）。
- **tail**：流事件可 `--only-text` 只留文本/thinking。

### 2) 操作、成立条件、失败模式、反例

- **幂等入口**：同一 root slug 的重复 kickoff 应 adopt 而非重建；30 分钟窗口限制"最近"；精确名避免前缀误认。
- **状态外置即可远程巡检**：crawl 从 git 读 state，不依赖本地工作区；环检测防止递归分支无限展开。
- **破坏性动作显式确认**：kill 必须先展示受害者清单，`-y` 才执行；区分 cancel（running）与 prune（pending）。
- **重试要留痕**：respawn 记录 source，cascade 用依赖图而不是"全清"。
- 失败模式/反例：用 startsWith 匹配导致 adopt 别的 goal 的 root；重复 kickoff 造出并行同题树；kill 无确认批量停摆；respawn 全部重置；crawl 因一个坏状态文件看不到子树；用本地 checkout 当唯一真源导致远程观察不到。

### 3) A–F 判断位点与专业 concern

| 位点 | concern | 何时调用 | Profile |
| --- | --- | --- | --- |
| Driver：重复入口、重试、终止、巡检 | 程序性 | 编排运维 | `driver` |
| D/E：幂等入口与状态外置的实现 | 接口/实现 | 实现 CLI | `technical-planning`/`implementation` |
| F：破坏性动作的清单证据与确认 | 证据/不可逆 | kill/prune | `evidence-evaluation` |

### 4) 当前产品锚点、覆盖与缺口

- 已覆盖：DEF1 G-01 的循环/退出码；`profiles/driver.md` 的程序性检查。
- 缺口：**幂等 kickoff（精确命名 + 时间窗 + 活跃状态）**、**ad-hoc/重试/级联的语义**、**破坏性动作的确认清单**、**从外部状态巡检树并处理环/坏行**。

为何值得吸收：这是"编排器可运维"的最小纪律；不引入新岗位，只给 Driver/Implementation 的操作判据。

### 5) 拟处置与载体

- 拟保留：同题入口 adopt、时间窗、精确名；重试标 source、级联按依赖图；破坏性动作清单+确认；外部状态巡检 + 环检测 + 容错读。
- 拟改变：CLI 名与 JSON 字段 → 通用"入口/采纳/重试/终止/巡检"；30 分钟标为来源参数。
- 拟删除：Cursor 云 API 细节。
- 载体落点：并入 DEF1 G-01（循环运维）与 `profiles/driver.md` 的程序性检查；不新建方法。
- 仍依赖 runtime：真实代理/run 列表与 VCS 读取；无外部状态时退化为本地。

### 6) 可讨论正文草稿 + 验证方案

```markdown
## 编排器运维（操作）
- 同一目标重复启动：先按精确标识查是否已有活跃实例（时间窗内、状态活跃），有则采纳而非新建；允许不同目标并行。
- 重试：终态才可重置；记录发起者；级联只沿声明的依赖图。
- 终止：先列出将受影响的对象与当前状态，需显式确认；区分"取消运行中"与"剪除待启动"。
- 巡检：从外部化状态读取整棵树（不依赖本地检出），递归要有环检测，坏行不影响其他子树。
```

验证方案（**未执行**）：mock agent 列表验证精确匹配/前缀不匹配/时间窗/活跃状态；mock 树验证环检测与坏行跳过；验证 kill 无 `-y` 时退出非零且未执行。边界：不要求真实云 API。

---

## J-05 · 操作者/外部通道的不可伪造边界（CLI 侧）

### 1) 机制与触发情境；源锚点与已读

触发情境：worker 控制 argv/env/cwd，能把 `--workspace` 指向伪造的 plan.json；同时要允许真正的操作者在工作区外发消息。

源锚点（pin 内）：`scripts/cli/util.ts`（全文）、`__tests__/operator-boundary.test.ts`（全文）、`__tests__/slack-channel-boundary.test.ts`（全文）。DEF1 G-03 因当时只读了 `core/andon.ts` + 标题级测试，未含本节的 CLI 侧证据；本节补实现层。

- `operatorModeFlagPath(home=userInfo().homedir)` → `<OS home>/.orchestrate/operator-mode`；`isOperatorModeEnabled` 要求 `lstatSync` 是文件、`uid === process.getuid()`、`mode & 0o777 === 0600`；**忽略 `ORCHESTRATE_OPERATOR` 环境变量**；`operatorModeFlagPath` 不读 `process.env.HOME`（测试断言：设 `HOME=<temp>` 后路径**不等于** symlink 位置；symlink flag 一律拒绝）。代码注释写明威胁模型："workers control argv/env/cwd… If workers can write that home directory, use a stronger boundary."
- `loadAllowedSlackThreadOrBail`：非操作者模式下必须有 `--workspace` 且 plan.json 存在且含 `slackKickoffRef`，否则 fail closed（报错信息含创建 0600 flag 的提示）；返回 `{channel, threadTs}`。操作者模式返回 undefined（= 不受 run-thread 限制）。
- `resolveKickoffSlackChannelOrBail` / `resolveWorkspaceSlackChannelOrBail`：`SLACK_BOT_TOKEN` 已设但无 channel → **在 Slack 初始化前**抛 `set --slack-channel or SLACK_CHANNEL_ID, or unset SLACK_BOT_TOKEN to disable Slack`；无 token 无 channel → Slack 关闭；无 token 有 channel → 接受并留给 plan 持久化；工作区运行继承 `plan.slackChannel`。
- 提示注入加固：`dispatcherInstruction` 对 Slack 首名先 `replace(/[\r\n`{}]/g," ")` 再 `JSON.stringify`，防止引号/反引号/`{{...}}` 破坏提示词或模板残留检查（注释明说"Slack first_name is operator-controlled but not vetted"）。
- 其他：`normalizeKickoffRepoUrl` 把 `git@` scp 形式转 https、剥 credentials/query/hash/`.git`；`parsePositiveIntegerOrBail` 严格正整数；`parseRespawnSourceOrBail`/`parseCommentCriticalityOrBail` 枚举校验。

### 2) 操作、成立条件、失败模式、反例

- **不可伪造边界来自 OS 所有权与权限，不来自环境变量**；文档化残余风险（能写 home 的攻击者需要更强边界）。
- **外部写默认失败关闭**：拿不到受信线程坐标就不写；操作者模式是唯一逃生口且要本地凭据。
- **配置缺一半要早失败**：token 设了没 channel 不能"先跑起来再说"。
- **把外部输入当不可信文本**：首名进提示词前净化 + JSON 编码；slack 文本入口同理（DEF1 G-03 的 Slack 边界）。
- 失败模式/反例：用 env flag 当操作者身份；信任 `HOME` 覆盖；接受 symlink flag；无 workspace 也允许评论；token 有 channel 缺时静默关闭 Slack；把首名原样插进提示词。

### 3) A–F 判断位点与专业 concern

| 位点 | concern | 何时调用 | Profile |
| --- | --- | --- | --- |
| D/F：不可伪造的操作者身份与失败关闭 | 安全/权限 | 外部写动作 | `technical-planning`+`evidence-evaluation` |
| E：OS 权限检查、净化实现 | 实现/安全 | 实现 CLI/提示装配 | `implementation` |
| B：外部通道消息的授权面 | 行为边界 | 用户可见写动作 | `behavior-domain`（辅） |

### 4) 当前产品锚点、覆盖与缺口

- 已覆盖：Backbone "工具权限≠执行授权"；`guide-redacted-evidence.md`。
- 缺口：**"不可伪造凭据"的实现形态**（OS home + uid + 0600 + 拒绝 symlink/env，并说明残余风险）；**外部写缺坐标时 fail closed**；**配置半配早失败**；**外部文本进提示词前的净化**。DEF1 G-03 给了机器侧队列约束；本组给 CLI/身份侧。

为何值得吸收：这是"人机边界"的具体化，直接支撑产品已有的授权语义。

### 5) 拟处置与载体

- 拟保留：OS 所有权/权限作身份；忽略环境变量与 HOME 覆盖；symlink 拒绝；残余风险声明；fail closed；半配置早失败；外部文本净化。
- 拟改变：Slack/`ORCHESTRATE_*` → 通用外部通道与宿主环境。
- 拟删除：具体路径名（保留 `~/.<tool>/operator-mode` 形态作例子）。
- 载体落点：并入 DEF1 G-03 的同一 on-demand guide（`external-write-boundary.md`）；`profiles/driver.md` 的安全边界一行。
- 仍依赖 runtime：真实 OS 权限模型；无 OS 隔离时规则要求"不得声称能区分操作者"。

### 6) 可讨论正文草稿 + 验证方案

```markdown
## 操作者身份与外部写（操作）
- 操作者身份来自不可伪造的本地凭据（文件所有权 + 权限，且拒绝符号链接与环境变量伪造）；文档化残余风险。
- 外部写默认失败关闭：没有受信目标坐标就不写；操作者模式是唯一显式逃生口。
- 配置只配一半（有凭据无目标）时在初始化前失败。
- 任何外部文本进入提示词/命令前净化并编码。
```

验证方案（**未执行**）：复现三类伪造（env flag、HOME 覆盖、symlink）应全部拒绝；无 workspace 的评论应失败；token 有 channel 缺应早失败；首名含引号/花括号/换行时提示词不畸变。边界：不要求真实 Slack。

---

## J-06 · 模型目录/探测、生成 schema 与提示注入加固

### 1) 机制与触发情境；源锚点与已读

触发情境：模型 slug 与后端参数会漂移；planner 需要选模型；JSON schema 是生成物；外部输入会进入提示词。

源锚点（pin 内）：`scripts/models.ts`、`scripts/tools/probe-models.ts`、`scripts/tools/generate-json-schemas.ts`、`scripts/tools/nudge-root.ts`（头 + 参数解析段）。

- **目录**：`ModelProfile` 分 `slug`（作者用稳定名）与 `selection`（SDK 规范化形态，可带 params 如 thinking/context/effort/reasoning/fast）；`defaultFor` 给每类任务默认；`resolveModelSelection` 未知 slug 透传为 `{id: slug}`（允许服务端模型）；`renderModelCatalog` 生成给 planner 的清单文本；注释要求 "Run `bun cli.ts models --check` after SDK or backend model-schema drift"。
- **探测**：`probeModelCatalog` 对目录逐项 `Agent.create` + `send("probe, ignore")` + `getRun().cancel()`，把失败收集为 `{ok:false,error:截断200}`；输出 `[OK]/[FAIL]` 与失败计数，非零退出。这是"模型声明必须被真实探测"的可执行检查。
- **生成 schema**：`generate-json-schemas.ts` 以 `PlanSchema`/`StateSchema` 为源，`zodToJsonSchema({$refStrategy:"none"})` 生成 `schemas/*.json`（去掉生成的 `$schema` 再补 `$id/title/description`）。机制 = **单一来源 + 生成物**；漂移风险在 `references/planner.md` 明确要求形状变化后重生成。
- **nudge**：给运行中的 agent 发 follow-up；默认对 `agent_busy` 重试；`--wait-idle` 轮询直到最新 run 非 running；有 `--max-wait/--poll-ms` 上限；message 可 inline/文件/stdin。

### 2) 操作、成立条件、失败模式、反例

- **作者名与运行时选择分离**：planner 写稳定 slug，脚本翻译成 SDK 形态；后端参数变化只改目录，不改 plan。
- **目录要能自检**：提供 `--check`/probe 路径，把"slug 还能用吗"变成真实调用 + 退出码；失败给出"重探 /v1/models 并更新目录"的修复指引。
- **生成物单源**：schema 从代码生成，不手写两份；形状变化后必须重生成（否则编辑器校验与实际解析分叉）。
- **唤醒有界**：nudge 有 busy 重试与 wait-idle 上限，不无限等。
- 失败模式/反例：在 plan 里硬编码后端参数；目录漂移后静默解析失败；手改生成的 JSON schema；nudge 无限轮询；把探测 agent 留在运行。

### 3) A–F 判断位点与专业 concern

| 位点 | concern | 何时调用 | Profile |
| --- | --- | --- | --- |
| D/E：能力声明与实际可用性 | 接口/依赖 | 选择模型/生成 schema | `technical-planning`/`implementation` |
| F：声明的可执行验证（probe） | 证据/时效 | 依赖"模型可用" | `evidence-evaluation` |
| Driver：唤醒/重试边界 | 程序性 | 长任务唤醒 | `driver` |

### 4) 当前产品锚点、覆盖与缺口

- 已覆盖：`methods/behavior-claim-evaluation.md` 的"真实 Provider/SDK claim 需要真实 leg"。
- 缺口：**"能力目录 + 真实探测 + 退出码"的操作形态**；**生成物单源 + 重生成纪律**；**唤醒的重试/等待边界**。

为何值得吸收：这是把"环境能力假设"变成可执行检查的最小样例；与产品"真实 leg"一致。

### 5) 拟处置与载体

- 拟保留：slug/selection 分离；每类任务默认；未知透传；探测 + 退出码 + 修复指引；生成物单源 + 重生成；唤醒有界。
- 拟改变：SDK 参数与 `Agent.create` → "能力声明与真实探测"；具体模型名删除。
- 拟删除：Cursor 云。
- 载体落点：并入 DEF1 G-12/G-13（真实 runtime 能力）或 J-01 的"可执行契约"；不新建方法。
- 仍依赖 runtime：真实 Provider/SDK；无探测能力时只能声明"未验证"。

### 6) 可讨论正文草稿 + 验证方案

```markdown
## 能力目录（操作）
- 作者使用稳定标识；运行时选择集中在目录里；未知标识透传但需日志。
- 提供探测路径：对每条声明做一次真实最小调用并取消，失败即非零退出 + 修复指引。
- 生成物（schema/清单）由单一来源生成；源形状变化后重生成。
- 唤醒/重试有上限与等待策略，不无限轮询。
```

验证方案（**未执行**）：故意把一条目录项改成无效参数 → probe 非零；改动 schema 源后不重生成 → 生成物与源不一致可检出；nudge 在 busy 下超限退出。边界：探测需要真实凭据；无凭据时标未验证。

---

## 2 · 残余（本包未读，不评估）

| # | 面 | 路径 | 为什么留 |
| --- | --- | --- | --- |
| R-1 | 操作者子命令 | `scripts/cli/{inspect,forensics,comments,andon,index}.ts` | 与 DEF1 G-03 的运维面重叠；无新机制假设，按需回读 |
| R-2 | Slack 适配器实现 | `scripts/adapters/{types,index,slack/*}.ts` | DEF1 G-03/G-05 已覆盖行为契约（线程守卫、post/retry）；实现细节待需要时读 |
| R-3 | 生成的 JSON schema | `schemas/{plan,state}.schema.json` | 由 `schemas.ts` 生成（J-06）；除非要核对生成漂移，否则不逐字读 |
| R-4 | 其余测试正文 | `__tests__/` 剩余 ~20 份 | 已用标题级 + 6 份正文覆盖关键负例；其余按需 |
| R-5 | 工具/配置 | `biome.json`/`tsconfig.json`/`package.json`/`bun.lock` | 与机制无关；不需要 |
| R-6 | `nudge-root.ts` 后半 | 轮询/发送实现 | 机制已在 J-06 头段；按需 |

---

## 3 · 机械自检（非专业裁定）

- 本包只新增 `docs/absorption/2026-10-02/packages/A4-CURSOR-DEF3.md`；未改产品、未改他人文档、未 commit、未执行源内任何脚本/测试。
- 判定为"有机制级内容"，理由：schema 层跨字段不变量与迁移错误、分支/合并命名不变量、模板装配失败检查、CLI 幂等/级联/确认/巡检、操作者边界的不可伪造检查、模型目录探测与生成物单源——均满足"可操作 + 有失败模式 + 可迁移"。
- 与 DEF1 的分工：DEF1 覆盖 G-01/G-02/G-03 的 runtime 行为契约；本包只补精确接口层与 CLI/测试实现证据，未重述。
- 未读面集中在 §2，未把未读写成已评估；所有"可执行观察"均标未执行。
