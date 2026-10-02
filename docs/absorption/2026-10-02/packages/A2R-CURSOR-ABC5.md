# A2R-CURSOR-ABC5 · cursor-plugins 审核包 5（编排控制面 / 双透镜评审代理 / 表面驱动取证 / 行为保持重构 / 记忆与偏好）

- 发现者：tpw-absorb-a2r（A2r）
- 源仓：`cursor-plugins`，pin `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`（只读 locator：`.worktrees/legacy-pre-night-2026-10-01/upstreams/cursor-plugins`）
- 产品基线：night worktree；core `professional-workflow/`（21 文件）；冻结 Backbone 未触碰
- 供 `tpw-absorb-gate` 实质裁定；本包不自行裁定采纳；处置均为“拟/候选/待裁定”
- 与包 1–4 的关系：包 1 MG-7 已读 `orchestrate/references/handoffs.md` 与 `planner.md` 的关键段；本包补 orchestrate 的 SKILL/dispatcher/spawning/其余 prompts、thermos 代理层与重复载体、control-cli/control-ui、refactoring/visual-parity、continual-learning。不重复包 1 的 handoff 模板细节。

## 1. 包内机制组总览

| MG | 机制组 | 主要源文件（pin 内） | 建议判断位点 | 类型 |
| --- | --- | --- | --- | --- |
| MG-1 | 编排的控制面与任务契约 | `orchestrate/skills/orchestrate/SKILL.md`、`references/dispatcher.md`、`references/spawning.md`、`prompts/{root,subplanner,loop-hygiene,failure-handoff,finished-no-handoff,empty-error-handoff}.md` | Driver / 工程裁决 | 规则候选（runtime 转 a4） |
| MG-2 | 双透镜评审代理与重复载体 | `thermos/README.md`、`thermos/agents/*.md`、`thermos/skills/thermo-nuclear-review/SKILL.md`（与 `cursor-team-kit/skills/thermo-nuclear-code-quality-review/SKILL.md` 字节相同） | F / 裁决 | 载体去重 + 代理契约候选 |
| MG-3 | 表面驱动与证据操作纪律 | `cursor-team-kit/skills/control-cli/SKILL.md`、`cursor-team-kit/skills/control-ui/SKILL.md` | F（验证面） | 方法候选 |
| MG-4 | 行为保持重构与视觉等价 | `pstack/skills/poteto-mode/playbooks/refactoring.md`、`visual-parity.md` | B/F | 方法候选 |
| MG-5 | 记忆与偏好整理 | `continual-learning/{README.md,skills/continual-learning/SKILL.md,agents/agents-memory-updater.md,hooks/continual-learning-stop.ts}` | A / meta | 整理纪律候选（hook runtime 不吸收） |

---

## MG-1 编排的控制面与任务契约（Driver / 工程裁决）

### 1) 机制与触发情境；源锚点与已读/尚缺

| 源锚点 | 已读 | 尚缺 |
| --- | --- | --- |
| `orchestrate/skills/orchestrate/SKILL.md`（全文） | 全文 | 无 |
| `orchestrate/skills/orchestrate/references/dispatcher.md`（全文） | 全文 | 无 |
| `orchestrate/skills/orchestrate/references/spawning.md`（全文） | 全文 | 无 |
| `orchestrate/skills/orchestrate/references/planner.md` | 包 1 已读关键段（Planning rules、Failure recovery、Andon、Comments） | 无新增 |
| `orchestrate/skills/orchestrate/references/handoffs.md` | 包 1 已读全文 | 无 |
| `prompts/root.md`、`subplanner.md`、`loop-hygiene.md`、`failure-handoff.md`、`finished-no-handoff.md`、`empty-error-handoff.md`（全文） | 全文 | `andon-block.md`、`slack-block.md` 已读（包 3 MG-5 未含，本轮读了 but 未逐字引用；见残余说明） |
| `orchestrate/skills/orchestrate/scripts/*`、`schemas/*`、`__tests__/*` | **未读** | 归 a4（runtime/脚本） |
| `cursor-sdk` 插件 | **未读** | 归 a4（SDK 机制） |

触发情境：用户显式 `/orchestrate <goal>` 把一个大型任务分解为并行 cloud agents 树（显式调用才加载，`disable-model-invocation: true`）。

### 2) 操作、成立条件、失败模式、反例/例子

**Core principles（原文 1–6）**：① **Planners own scopes and publish tasks. They do no coding.**（写 plan.json、读 handoffs、决定下一步；编辑文件/git merge/修冲突 inline 都不是 planner 工作；想写代码就发布 worker 任务）② **Planners don't know who picks up their tasks.**（脚本路由，planner 心智停留在 task 级）③ **Workers are isolated.**（一任务一 clone，无渠道与其他 agent 通话，一个 handoff）④ **Subplanners are recursive planners.**（“subplan this slice”任务；subplanner 完全拥有该 slice 并交回 aggregated handoff）⑤ **Continuous motion via handoffs.**（自认为完成的 planner 可能收到 late handoff 并重规划；直到 planner 决定停止发布才“finished”）⑥ **Propagation, not synchronization.**（兄弟间无串话、层间无共享状态；每层只见 children 的 handoffs）。

**Node types（原文表）**：Planner（跑 loop，全 goal，user-facing message + 可选 PR）；Subplanner（跑 loop，父 scope 的一个 slice，handoff 给父）；Worker（不跑 loop，一个具体任务，handoff 给 spawn 它的 planner）；Verifier（不跑 loop，一个目标的验收标准，verdict handoff）；Git（共享媒介：branches + handoffs/ 承载意义）。

**Dispatcher（一次性的）**：取用户 goal → kickoff CLI 启 cloud root planner → 返回 URL → 停；只有 goal 缺失/含糊才问澄清；**push back 只在任务真的 trivial 时**。**Minimal-goal discipline**：把用户 goal 原样传过，不加 planning 启发、subplanner 数量或结构处方；“Over-prescribing leaks dispatcher context into the planner's window and invalidates the skill as a realistic test of the planner's judgment.” 身份解析顺序（`--dispatcher-name` → Slack `users.lookupByEmail` 对 git email），`plan.summary` 是给人类的单行定位（kickoff 贴 `<rootSlug>: <summary> <agent-link>`；无 summary 则截断 goal ~200 字符）；`goal` 是 agent-facing 全文。同步默认开（`syncStateToGit`），可在 root plan 设 false。

**Spawning 契约（关键条目）**：branch naming 用确定性占位符（`orch/<rootSlug>/<task-name>`），任务名强制 kebab-case；**不要要求 worker 创建/改名到占位符**；下游需要上游代码就 dependsOn，脚本在 handoff 后记录实际 branch；**无自动集成分支**（“An auto-managed integration branch would smuggle planner-level coding decisions into infrastructure, violating Core Principle #1.”）。agent naming 仅可读性（server 上限 100 字符，空/纯空白拒绝）。`startingRef` 控制从哪个 branch clone（默认 `plan.baseBranch`），`dependsOn` 控制何时可 spawn；**`startingRef` 不带 `dependsOn` 是时点快照**（spawn 时该 branch 上有什么就是什么，可能什么都没有），除非真想要“从当前 tip 起，哪怕空”，否则配对使用；verifier 默认从 target branch 起并自动包含 target 于 dependsOn。`verify` 是 Markdown 计划（setup/automated/manual/gotchas）；worker 当目标规格读，verifier 继承。**PR 是 per-task opt-in**（`autoCreatePR` 镜像 `openPR`，默认 false；server gate 使其 no-op，真正机制是 worker prompt 指示 draft PR）；**PR base 与 worker starting ref 分离**（`plan.baseBranch` vs `plan.prBase`），经典模式不设 prBase 时 worker PR stack 在 planner branch。**Task prompt contract**：脚本从 scopedGoal/pathsAllowed/pathsForbidden/acceptance/startingRef/type/openPR 渲染；**不要 patch prompt 模板，改 plan entry**；每个 prompt 声明隔离、提交并 push 当前 branch、不改名/merge/rebase、只有 openPR worker 开 draft PR、final message 即 handoff。**“Workers cannot ask clarifying questions mid-run. Under-specified `scopedGoal` produces silent drift. Write each task as if you'll never get another chance to steer it.”** 环境变量可能被 cloud VM 出于 prompt-injection 防御 redact → 需要多 agent 共享的数据用 **planner-authored artifact pattern**（committed file on base branch + 在 scopedGoal 里按路径引用）；**绝不把凭证放进 scopedGoal**（会送模型提供方，state sync 开启时可能进 git 历史）。

**Tracking & recovery（关键条目）**：spawn 后持久化 `agentId`/`runId`/`parentAgentId`；重启时半身份行（恰好其一）标 `error` 并说明；**每次 handoff 后对账 dependent verifier 的 startingRef**——实际 worker branch 取自 handoff body 的 `## Branch` 行（SDK 的 `Run.git.branches[].branch` 对 worker run 为空，**body 是权威**）；planner 手写的 startingRef 覆盖优先；每次传播 log 到 attention.log；load 时扫已 handoff 行使 disk 恢复状态收敛。Lineage 走 `parentAgentId`，`kill-tree --agent-id` 向下走；planner 未设 `selfAgentId` 则 children `parentAgentId: null`，子树 scoped kill 跳过（不传 `--agent-id` 则整树取消）。

**Subplanner prompt（关键条目）**：“**You fully own this slice.**”父只给 goal/path bounds/acceptance，不给 sub-plan；`scopedGoal` 里的拆分提示至多是 weak hint，subplanner 对子树结构权威；递归规则：叶级用 worker，仍需内部结构或 merge/verify 时加 subplanner，无深度上限；默认更少更宽的 worker；子任务写入自己的 plan.json；`plan.rootSlug`、`plan.repoUrl` 继承、andon state 复制、`plan.selfAgentId` 写入；model selection per task by capability；**最终 handoff 的 Verification 值必须原样透传最弱真实 claim**：“Pass `verifier-blocked` through unchanged rather than rounding up to a thinner verified value. Use `not-verified` only when no verifier ran and your workers didn't self-report a stronger claim.” 且“Do not open a PR.”

**Root/loop hygiene（关键条目）**：`bun cli.ts run` **必须前台跑**（“The Shell default backgrounds the loop and breaks the heartbeat when your turn ends.”）；exit 100 = planned checkpoint restart，不是错误，立即重跑同一命令（从 committed state.json 恢复）；exit 1（非空错误集）是你的回合——脚本已为每个死 worker 写 synthetic failure handoff 与 finished-no-handoff；在飞 worker 继续跑，下次 run 经 `recoverRunning` 重挂；run 返回后 call `tree`，还有 pending/running 就再 loop；**有非终态任务时不要结束回合**。失败恢复决策表（同包 1 MG-7 的分类器）：cap-hit/oom→缩小 scope 重试；network-drop→原样重试（transient）；tool-error→换 model 重试；unknown→读 Last activity/SDK error，无信号按 transient 原样重试，再失败则 abandon；每次重试等于又一次 cloud-agent run，要预算决策；同任务 2 次重试后倾向 abandon（从 plan.json drop 并 replan around）而不是第 3 次，除非有具体证据下次会成功；finished-no-handoff 读 raw snippet 判断 intent 是否可恢复；更新 plan.json 后重跑 run。

**成立条件**：任务真的大到值得并行云树；planner 能只做规划与阅读；worker 能独立推进（无中途提问）；handoff 是唯一通道；Andon 只在“继续 spawn 会产生垃圾”时用（包 1 MG-7）。

**失败模式/反例**：planner 自己写代码/merge（违反 #1）；要求 worker 改名到占位符；把 startingRef 与 dependsOn 脱钩导致快照为空；把 PR 当成默认；prompt 模板被 patch 而不是改 plan entry；under-specified scopedGoal（silent drift）；把凭证/环境变量当共享数据；verifier startingRef 不对账（用占位符）；把 `verifier-blocked` 向上取整成更薄的 verified；有非终态任务就结束回合；第三次盲目重试；用 Andon 表达单任务阻塞。

### 3) 判断位点与 Profile 调用

| 位点 | 专业 concern | 何时调用 | 由哪个 Profile 提议 |
| --- | --- | --- | --- |
| Driver：任务分解、依赖、隔离、重试/放弃、终止 | 程序性 | 多实例编排 | `driver`（Backbone §4/§6） |
| F：verifier 值与证据对账 | 验证 | 跨实例验证结果聚合 | `evidence-evaluation` |
| D：任务间代码依赖的落点 | 技术 | 分支/接口/共享工件 | `technical-planning`（a4 侧） |
| A：goal 的传递与不扩写 | 目标 | dispatcher → planner | `intent-voice`（goal 保真） |

### 4) 当前产品锚点、覆盖、缺口、为何值得吸收

- `profiles/driver.md` `## 心智模型`：“Driver 连接内部责任：把‘谁该上场、哪个结论够不够格、退给谁、什么时候停’理顺。”
- `profiles/driver.md` `## 关键问题`：“并行写者的写集是否明确？共享文件是否单写者串行集成？”
- `profiles/driver.md` `## 常见误区`：“管到进程、并发、锁等 execution mechanics。”
- `authority/RESPONSIBILITY-BACKBONE.md` §4：“Driver 留在逻辑编排层，不定义进程、并发、队列、锁、重试等 runtime 机制。”
- 包 1 MG-7 已覆盖 handoff/verifier 五值/measurements/Andon 边界。

具体缺口：

1. **没有“任务发布契约”**：产品有 Driver 路由与 handoff 指针，但没有“worker 不能中途提问 → scopedGoal 必须写成像你再也没有机会 steer 它”“prompt 模板不 patch、改任务定义”“共享数据用 committed artifact 而非环境变量、凭证绝不入任务文本”这些具体契约。
2. **没有 startingRef/dependsOn 配对的语义**（时点快照 vs 依赖上游）；没有“planner 手写 startingRef 覆盖优先”的对账规则。
3. **没有“planner 不写代码”的硬边界**与“无自动集成分支”的理由（避免把 planner 级编码决定偷渡进基础设施）。
4. **没有 loop hygiene 的三条判定**（前台跑以保持心跳；exit 100 不是错误；有非终态任务不得结束回合）。
5. **没有“verifier 的最弱真实 claim 原样透传”** 的聚合纪律（包 1 有 verifier 五值，但未写聚合者不得向上取整）。
6. **没有 dispatcher 的 minimal-goal 纪律**（不把上游上下文/结构处方泄进 planner 窗口）。
7. 产品明确 runtime 不进本包，因此**状态机/脚本/队列/重试机制不吸收**；只吸收上述逻辑编排层契约。

为何值得吸收：这些是 Driver 在“多实例 + 多轮”场景下最容易失守的点，全部属逻辑编排层，不违反“runtime 不进本包”的边界。

### 5) 拟处置与载体

- 拟保留：planner 不写代码；worker 隔离与无串话；subplanner 递归/完全拥有 slice；continuous motion；propagation not synchronization；node types；dispatcher 一次性与 minimal-goal；任务契约（under-specified → silent drift；prompt 模板不 patch；共享数据用 committed artifact；凭证不入任务文本）；startingRef/dependsOn 配对与 verifier 自动依赖；PR per-task opt-in 与 prBase/base 分离；无自动集成分支；tracking 半身份→error；verifier startingRef 从 handoff body 对账（body 权威）；最弱真实 claim 原样透传；loop hygiene 三条；失败重试/放弃阶梯（已在包 1 记录，本组交叉引用）。
- 拟改变：去 Cursor SDK/cloud agent/`bun cli.ts`/Slack/state.json/attention.log/`plan.json` 具体字段与命令（改为“状态记录/循环入口/任务定义”等通用词）；去 `autoCreatePR`/ManagePullRequest 工具名；把 Andon 保持为包 1 的边界描述。
- 拟删除：auth、keychain、node_modules 安装、`probe-models`、agent naming 上限等 runtime 细节（归 a4 或排除）。
- 载体：方案 1（推荐）扩写包 1 MG-7 的交接与证据等级方法为 `methods/handoff-and-evidence-grading.md` + 新增 `methods/guide-orchestration-contract.md`（逻辑编排契约：任务发布/依赖/隔离/终止/最弱 claim），在 `profiles/driver.md` 按需入口加一行；方案 2 全部并入 driver Profile（代价：Profile 不承载方法正文，且会把 runtime 与逻辑层混写）。本包倾向方案 1。
- **风险提示**：本组源自一个 runtime 产品；吸收时必须只保留“谁在什么条件下可以发布什么、依赖如何传递、终止与放弃如何判定”，不把状态机/脚本语言带进产品（与执行计划“不复活旧 runtime/registry”一致）。

**仍依赖真实 runtime 的能力**：并行 spawn、状态持久化、handoff 自动转发、measurements 重跑；产品方法层只定义契约与判定。

### 6) 正文草稿与验证方案

```
编排契约（草稿，逻辑层）
1. 规划者只规划：发布任务、读 handoff、决定下一步；不写代码、不 merge、不 inline 修冲突。
2. 任务发布即最后机会：worker 不能中途提问；任务文本要含目标、允许/禁止路径、验收、起点引用、验证 recipe；不明确就必然 silent drift。
3. 依赖显式：需要上游产出就声明依赖；只给起点引用不给依赖 = 时点快照（可能为空）。
4. 共享数据用 committed artifact 按路径引用，不用环境变量；凭证绝不入任务文本。
5. 隔离：一任务一 clone、无兄弟串话；PR per-task opt-in；不设自动集成分支（避免把规划者级编码决定偷渡进基础设施）。
6. verifier 从目标 branch 起；聚合时最弱真实 claim 原样透传，不向上取整。
7. 终止/恢复：循环必须前台保持心跳；计划内 checkpoint 不是错误；有非终态任务不结束回合；同任务两次重试后倾向放弃并重规划，除非有具体证据。
```

验证方案（未执行）：用一个真实多实例小场景检查 (a) 任务文本是否自足到无需中途澄清；(b) 依赖/起点是否配对、verifier 是否对账；(c) 失败后是否按阶梯重试/放弃而非无限重试。边界：不引入 runtime 机制；无并行需求的任务不适用。

---

## MG-2 双透镜评审代理与重复载体（F / 裁决）

### 1) 机制与触发情境；源锚点与已读/尚缺

| 源锚点 | 已读 | 尚缺 |
| --- | --- | --- |
| `thermos/README.md`（全文） | 全文 | 无 |
| `thermos/agents/thermo-nuclear-review-subagent.md`（全文） | 全文 | 无 |
| `thermos/agents/thermo-nuclear-code-quality-review-subagent.md`（全文） | 全文 | 无 |
| `thermos/skills/thermo-nuclear-review/SKILL.md`（全文，包 1 已读） | 全文 | 无 |
| `cursor-team-kit/skills/thermo-nuclear-code-quality-review/SKILL.md`（全文，包 1 已读） | 全文 | 无 |
| `thermos/skills/thermo-nuclear-code-quality-review/SKILL.md` | **未逐字读**，已用 md5 确认与 team-kit 版本**字节相同**（md5 `4da293a79288af26c8e685b547c10455`） | 无内容差异 |
| `cursor-team-kit/agents/thermo-nuclear-code-quality-review.md`（1874B） | **未读** | 与 thermos 子代理（1870B）的关系未逐字比较；MD5 不同，待 gate 判重 |
| `thermos/skills/thermos/SKILL.md`（全文，包 1 已读） | 全文 | 无 |

触发情境：分支/PR 需要双透镜（安全与正确性 + 可维护性）深度审计；用子代理并行执行后再合成。

### 2) 操作、成立条件、失败模式、反例/例子

**架构（README mermaid 文字化）**：L2 编排器 `thermos` → L1 两个子代理（deep review + code quality）→ L0 两个 skill + diff 输入。

**双透镜代理契约（两个子代理文件，逐条）**

- thermo-nuclear-review-subagent：**Task 子代理**，父代理已收集 git 输出与变更文件内容，prompt 是带 `### Git / diff output` 与 `### Changed file contents` 段的 user message。工作：① 加载 `thermo-nuclear-review` skill 并**完全遵循其 SKILL.md**（scope 只报新增/修改代码、breaking functionality/devex、feature leaks、intended breakage、over-reporting、最终响应/PR 讨论规则、critical rules）；skill 不可用时仍以同样的严谨做 security/correctness-focused 的 diff-scoped reviewer（**“no issues with unfinished research when you can verify in-repo”**）；② 只对 diff 里变动的代码审计，追跨包副作用，**不报未改动代码中的既有问题**；③ **先完成独立审计（fresh eyes）**；④ 审计之后，**若**该分支存在 PR **且**已有 medium 或更高 finding，才用 `gh`/`glab` 读 PR/MR 讨论，纳入 BugBot 或人类线程——验证、去重、标注来源；⑤ 绝不呈现研究未完成的 issue（有 repo 内访问就追 client/server 或相关代码）。诚实校准严重度；最终响应按优先级与 file:line 证据组织；**除非用户/父明确要求，不 spawn 嵌套子代理**。
- thermo-nuclear-code-quality-review-subagent：同上父编排形态；① 加载 code-quality skill 并把其 SKILL.md 当**完整 rubric**（语气、审批门槛、输出排序、code-judo/1k 行/spaghetti 规则）；不可用时回落到一致的严格 maintainability 审计（ambitious simplification、无正当理由不得越过 ~1k 行、无 ad-hoc 分支增长、显式类型与边界、canonical layer）；只对 diff 与内容所示应用 rubric，跨文件影响要在改动触及 module 边界时追；按 rubric 指定优先级输出、直接且高信念、有结构问题就跳过 cosmetic nits；不 spawn 嵌套子代理。
- 父编排典型流程（两文件末尾相同）：**一条消息**里并行跑两个 Task——一个收集 `git diff <base>...HEAD`、一个 explore 收集变更文件全文（默认 base `main`）——然后以 `subagent_type: "thermo-nuclear-…-subagent"` 调用并把两段内容放进 user prompt。

**重复载体（实测）**：`cursor-team-kit/skills/thermo-nuclear-code-quality-review/SKILL.md` 与 `thermos/skills/thermo-nuclear-code-quality-review/SKILL.md` **md5 相同**（`4da293a79288af26c8e685b547c10455`）；thermos README `## Migration from cursor-team-kit` 明确：“cursor-team-kit previously included only thermo-nuclear-code-quality-review. That skill and agent now live in **Thermos** alongside deep review and thermos. Remove the old thermo entries from team-kit when you install this plugin **to avoid duplicates**.” 两个插件各自还有 agent（team-kit 1874B vs thermos subagent 1870B，md5 不同，未逐字比对）。`thermos` 编排 skill（包 1 已读）：一条消息并行跑两个后台子代理，合成时 findings 优先、跨 reviewer 去重、overlap 加重、分歧用自己判断、summary 简短。

**成立条件**：有 scoped diff 与变更文件全文；两个 rubric skill 可用或可回落；父代理在一条消息里并行收集与调用（避免串行丢失新鲜度）。

**失败模式/反例**：报未改动代码的既有问题；审计前先读 PR 讨论（破坏 fresh eyes）；未完成研究的 finding；把 code-quality rubric 的 1k 行当机械 gate；子代理自行嵌套 spawn；重复插件同时安装导致同一机制被计两次或审两遍。

### 3) 判断位点与 Profile 调用

| 位点 | 专业 concern | 何时调用 | 由哪个 Profile 提议 |
| --- | --- | --- | --- |
| F：评审裁决（各自独立、再合成） | 安全/正确性/可维护性 | 分支/PR 深度审计 | `evidence-evaluation` |
| C/D：结构质量透镜 | 可维护性/架构 | 结构回退或简化机会 | `technical-planning`（a4 侧） |
| Driver：并行评审的编排与去重 | 程序性 | 两个透镜并行时 | `driver` |

### 4) 当前产品锚点、覆盖、缺口、为何值得吸收

- `profiles/evidence-evaluation.md` `## 心智模型`：“独立是真实属性：评价者不得是被评价候选的实现者。”
- `methods/behavior-claim-evaluation.md` `## Limits`：“Independent authorship is not part of the measurement method”。
- 包 1 MG-6 已覆盖 thermo-nuclear 两 rubric 的内容面与 interrogate/advisor 的裁决面。
- `methods/README.md` 的溯源纪律（同一来源只应有一份接受对象）。

具体缺口：

1. **没有“评审代理的输入契约”**：父代理收集什么、以什么段名传入、子代理只对 diff 负责、独立审计在 PR 讨论之前——产品没有代理层交接面。
2. **没有 rubric 缺失时的回落定义**（“仍以同样严谨执行，但不得呈现未完成研究”）。
3. **没有重复载体的处理纪律**：同一机制在两个插件出现（字节相同的 skill），吸收时必须判重、只算一次知识增量；这正是 `methods/README.md` 溯源纪律在源侧的例子。
4. **没有“不嵌套 spawn”与“不同代理各持 rubric”的边界**。

为何值得吸收：这是把包 1 MG-6 的评审 rubric 变成可并行执行实例的接口；同时重复载体的发现直接服务执行计划的“多源一个机制不能重复算知识增量”。

### 5) 拟处置与载体

- 拟保留：两透镜输入契约（diff + 变更文件全文，标注段名）；只审 diff、追跨包副作用、不报既有问题；独立审计先于 PR 讨论；medium+ 才读讨论并入并标注来源；rubric 缺失时的回落与“不得未完成研究”；不嵌套 spawn；父代理一条消息并行收集与调用；合成规则（findings 优先、去重、overlap 加重、分歧自判、summary 简短）。
- 拟改变：去 `Task`/`subagent_type`/`gh`/`glab`/`run_in_background` 具体工具名（改为“可用代理/forge 工具”）；把 `subagent_type` 标签改为“两个独立评审实例”。
- 拟删除：`thermos` 插件的重复 code-quality skill 条目（吸收时只保留一份机制来源；team-kit 与 thermos 的字节相同 skill 不重复计数）；team-kit 旧 agent 与 thermos subagent 的差异由 gate 判重后择一。
- 载体：并入包 1 MG-6 的 `methods/review-verdict.md`（评审裁决方法）的一节“代理化执行契约”，不新建文件；在 `methods/README.md` 的溯源表注明 cursor-plugins 内两个同名载体字节相同、只取一份。
- **给 gate 的判重结论（事实，不是采纳建议）**：`thermo-nuclear-code-quality-review` 在 pin 内出现两次且 **SKILL 字节完全相同**；不是两个来源，不能算两次知识增量。

**平台耦合/依赖**：代理调用与 forge 工具是宿主；输入契约与独立审计次序零耦合。

### 6) 正文草稿与验证方案

```
双透镜评审代理契约（草稿）
- 父代理收集：diff（base...HEAD）+ 变更文件全文；以标注段传入。
- 子代理只审本次新增/修改；跨包副作用要追；不报未改动处的既有问题。
- 先独立审计（fresh eyes）；有 medium+ finding 且存在评审请求时，才读外部讨论，验证/去重/注明来源。
- rubric 不可用时以同等严谨执行，但绝不呈现未完成研究。
- 不嵌套 spawn；两个透镜各持自己的 rubric；合成 findings-first、去重、重叠加重、分歧自判、摘要简短。
判重：同名 skill 在两个插件中字节相同 → 只取一份机制来源。
```

验证方案（未执行）：用同一 diff 跑两个透镜，检查 (a) 独立审计是否先于讨论读取；(b) 是否误报未改动代码；(c) 合成是否去重并标注分歧。边界：1k 行等规则是 rubric 判据不是机械 gate；不要求同模型。

---

## MG-3 表面驱动与证据操作纪律（F）

### 1) 机制与触发情境；源锚点与已读/尚缺

| 源锚点 | 已读 | 尚缺 |
| --- | --- | --- |
| `cursor-team-kit/skills/control-cli/SKILL.md`（全文） | 全文 | 无 |
| `cursor-team-kit/skills/control-ui/SKILL.md`（全文） | 全文 | 无 |
| `pstack/skills/create-verification-skill/SKILL.md` | 包 1 MG-5 已读 | 无（本组是其 Drive/Launch 段的操作细化） |
| `pstack/skills/poteto-mode/playbooks/visual-parity.md` | 本包 MG-4 已读 | 无 |
| 真实浏览器/终端 | **未运行** | 所有 harness 命令未执行 |

触发情境（两个 description）：需要可重复地驱动/检查/剖析交互式 CLI 或 TUI（键盘流、提示、中断、resize、终端布局、启动回归、内存泄漏、hang、demo）；用本地 browser/CDP harness 驱动 web/IDE/Electron UI（截图、可访问性快照、性能 profile、视觉 diff、复现 UI bug）。

### 2) 操作、成立条件、失败模式、反例/例子

**control-cli（操作）**：**先复用 repo 自己的 test/demo harness**；没有才用标准本地工具组装临时 harness。用途：确定性输入复现 CLI/TUI bug；验证键盘流、提示、中断、resize、终端布局；缺陷修复的 before/after transcript；剖析启动时间、慢操作、hang、内存增长；录制短终端 demo。Harness loop 八步：确认被测命令与最小可复现 workspace → 发现既有本地 harness（package scripts、e2e、demo recorder、expect、PTY helper）→ 没有就隔离终端会话 + 确定性环境变量启动 → 交互前先 capture 当前屏 → **一次一个动作**（text、Enter、箭头、Escape、Ctrl-C、resize）→ **等具体屏幕模式或 prompt 再下一个动作** → 保存 transcript 与 profile artifact → 干净 kill session。Harness 选项：repo-native 优先（知道 app 启动/env/prompts）；tmux（managed session、capture-pane、send-keys、attach/detach）；PTY probe（无 tmux 时用短 Python/Node/Expect）；runtime inspector（Node/Bun inspector 做 CPU profile、heap snapshot、live eval）；terminal recorder（repo-local demo 工具或 asciinema 兼容工具，当用户要 demo）。Profiling recipes：启动回归（同机同 env 同命令的 baseline/treatment 计时）；慢操作（start CPU profile → 操作 → stop → 比较 top self-time）；内存泄漏（force GC → heap snapshot → 重复操作 → force GC → 再 snapshot）；hang（capture 屏幕、active handles/resources、stack/CPU sample 再中断）。Guardrails：**偏好确定性等待而非 sleep**（必须 sleep 要说明理由）；不把凭证或破坏性命令发进受控会话；harness 留在 `/tmp` 除非 repo 已有 test/demo harness；不硬编码其他 repo 路径；清 tmux session、temp dir、inspector 进程与 demo artifact 除非用户要求保留。

**control-ui（操作）**：**先复用 repo 自己的 Playwright/browser/Electron harness**；没有才围绕 dev server 或 Chromium debug port 组装临时 harness。用途：复现依赖真实浏览器 focus/键盘/滚动/resize/渲染的 UI bug；用截图与快照验证视觉/可访问性变更；检查本地 web/IDE/Electron 行为；抓 console/network/CPU profile/trace/heap snapshot；为 inspect 生成 before/after 证据。Setup 六步：用 repo 文档化 dev 命令本地起 app → 发现既有 harness（Playwright、Cypress、Storybook、browser scripts、Electron launch scripts、snapshot 工具）→ web app 用既有浏览器工具连本地 URL → Electron/Chromium 启用 remote debugging port → **按稳定 app marker 选正确 page，不靠 tab 顺序** → 偏好 a11y roles/labels/稳定 data-* 而非坐标。Interaction loop：先 capture snapshot/screenshot → 从最新页面结构选 target → **只做一个结构动作**（click/type/keypress/drag/scroll/navigate/resize）→ 重新 capture → 验证预期状态变化 → 需要时保存 before/after artifact。CDP 能力（高层 API 不够时）：Performance（CPU profile/trace/paint flashing/FPS/layout shift）、Memory（heap snapshot + forced GC）、Network（request blocking/throttling/cache disable/日志）、Rendering（viewport/color scheme/reduced motion/a11y）、Debugging（console streaming/exception capture/DOM snapshot）。Page selection：多窗口共享 debug port 时，用 surface 的正 marker（如 app root selector），必要时负 marker，不能用就列 titles/URLs 而不是猜。Guardrails：导航/结构变化后不依赖 stale element reference；**坐标点击前必须刚 capture 过截图**；测试数据本地可丢弃；隐私敏感 workspace 的截图/heap snapshot 未经用户明确同意不存；不硬编码其他 repo 的 selector/port/脚本路径，发现当前 repo marker；结束时清理 dev server、debug session、temp profile。不要为 probe 给项目加 Playwright 依赖，除非用户要求（源文明确）。

**成立条件**：repo 有可启动的 app 与至少一种驱动工具；最小可复现 workspace；能捕获证据。

**失败模式/反例**：手工乱戳代替确定性 harness；一次发多个动作/不等屏幕模式；用 sleep 代替等待且不说明；把凭证或破坏性命令发进受控会话；harness 留在 repo 里（除非已有约定）；硬编码他仓路径/selector/port；坐标点击前无新截图；导航后复用 stale element；泄漏 heap snapshot 侵犯隐私；不清进程/端口/临时 profile。

### 3) 判断位点与 Profile 调用

| 位点 | 专业 concern | 何时调用 | 由哪个 Profile 提议 |
| --- | --- | --- | --- |
| F：真实 surface 取证 | 验证/证据 | 需要 CLI/UI 行为证据时 | `evidence-evaluation` |
| E：harness 组装与实现 | 实现 | 驱动脚本编写 | `implementation`（a4 侧） |
| D：harness 复用的设计选择 | 技术 | harness 与 app 接缝 | `technical-planning`（a4 侧） |

### 4) 当前产品锚点、覆盖、缺口、为何值得吸收

- 包 1 MG-5 已记录 `create-verification-skill` 的 Launch/Doctor/Drive/Evidence/Cleanup 与证据标准。
- `methods/guide-mock-adapter-choice.md`（按需支持文件）：测试替身/适配器选择。
- `profiles/evidence-evaluation.md` `## 关键问题`：“什么观察能把‘成立’与‘不成立’分开？关键负控制是什么？”
- `profiles/evidence-evaluation.md` `## 常见误区`：“把环境/工具故障判成产品 FAIL”。

具体缺口：

1. **没有“复用优先”的 harness 选择顺序**（repo-native → tmux/PTY → generic），产品只有“测试替身”指南，没有“驱动真实 surface”。
2. **没有一次一动作、等屏幕模式、确定性等待**的操作纪律（`create-verification-skill` 的 Drive 段只说“真实 selector/命令、优先稳定 handle”，没有交互节奏与 stale element 规则）。
3. **没有 profiling recipes**（启动 baseline/treatment、CPU profile 比较 top self-time、heap snapshot + forced GC 循环、hang 前先抓资源与 stack）——这正是“性能/内存/hang”类 claim 的证据面（与 a4 的 perf 方法相邻）。
4. **没有 cleanup 与隐私边界**（清 session/temp/inspector；隐私 workspace 的截图/heap 需明确同意；不擅自加依赖）。

为何值得吸收：F 的证据最终要落到真实 surface；`create-verification-skill` 生成的是项目本地验证面，本组是其执行时的操作纪律，两者互补。

### 5) 拟处置与载体

- 拟保留：复用优先；八步/六步交互循环；一次一动作 + 等具体模式 + 确定性等待；tmux/PTY/CDP 作为可选项；profiling four recipes；page selection 正/负 marker 与列 titles 不猜；stale element/坐标点击规则；cleanup 与隐私/依赖边界。
- 拟改变：去 tmux/pty/playwright/Chromium 具体命令与代码片段（作例子）；去路径 `/tmp` 强制（改为“repo 约定之外的临时位置”）；把 debug port 具体开关改为“可用时”。
- 拟删除：与产品无关的 demo recorder 细节。
- 载体：方案 1（推荐）并入包 1 MG-5 的 `methods/verification-harness-design.md` 作为“执行期纪律”一节；方案 2 独立 `methods/guide-surface-driving.md`（代价：与 harness 设计方法触发重叠）。本包倾向方案 1，并在 `methods/guide-mock-adapter-choice.md` 交叉引用。
- 与 a4 的分工：具体 harness 实现、profiler 命令、Playwright/CDP 代码归 a4；本组保留操作纪律与证据标准。

**平台耦合/依赖**：终端浏览器工具是宿主；纪律骨架零耦合。仍依赖真实可启动 app 与驱动工具。

### 6) 正文草稿与验证方案

```
表面驱动纪律（草稿）
1. 复用优先：repo 自己的 harness → 受控终端会话/PTY → 通用浏览器/CDP。
2. 一次一个动作；等具体屏幕模式/prompt；用确定性等待，不 sleep（必须 sleep 要说明）。
3. 交互前先 capture；变化后重新 capture；不依赖 stale element；坐标点击前必须有新截图。
4. 证据：transcript、截图、ARIA 快照、profile、heap snapshot、网络日志；标注 feature 与入口。
5. Profiling：启动 baseline/treatment 同机同 env 同命令；慢操作 CPU profile 比 top self-time；泄漏 forced GC + 两次 heap snapshot；hang 先抓屏幕/handles/stack 再中断。
6. 清理：session、临时目录、inspector、dev server、temp profile；隐私 workspace 的截图/heap 未经明确同意不保存；不为 probe 擅自加依赖。
```

验证方案（未执行）：用真实 CLI 与真实 web UI 各跑一次交互序列，检查 (a) 是否复用了既有 harness；(b) 一次一动作并等待模式；(c) 证据与清理完整。边界：不要求所有场景都到 profile；无可用驱动工具时记录为阻断而非产品缺陷。

---

## MG-4 行为保持重构与视觉等价（B/F）

### 1) 机制与触发情境；源锚点与已读/尚缺

| 源锚点 | 已读 | 尚缺 |
| --- | --- | --- |
| `pstack/skills/poteto-mode/playbooks/refactoring.md`（全文） | 全文 | 无 |
| `pstack/skills/poteto-mode/playbooks/visual-parity.md`（全文） | 全文 | 无 |
| `pstack/skills/principle-model-the-domain/SKILL.md`、`principle-subtract-before-you-add/SKILL.md`、`principle-migrate-callers-then-delete-legacy-apis/SKILL.md`、`principle-minimize-reader-load/SKILL.md`、`principle-prove-it-works/SKILL.md`、`principle-separate-before-serializing-shared-state/SKILL.md` | 包 1/2 已读 | 无（本组引用其操作化） |
| `pstack/skills/create-verification-skill/SKILL.md` | 包 1 MG-5 已读 | 无 |
| `methods/cross-module-design.md` | 已读 | 无 |

触发情境：行为保持的结构改动（rename/extract/inline/dedupe/move）；像素级 UI 等价（两实现匹配或样式系统迁移）。

### 2) 操作、成立条件、失败模式、反例/例子

**refactoring（8 步，逐条）**：“You own the contract. The structure changes. The behavior does not.” 与 Feature（加行为）、Bug fix（修行为）区分。若清理时发现缺 feature 或真 bug：拆出去，先发结构改动（对着 pinned contract）；redesign 允许但要命名并转 Feature；大或横切结构工作归 figure-it-out；本 playbook 是聚焦到中等改动。① **先钉行为契约**：跑 how 学契约，然后写 characterization test、snapshot 或 equivalence harness 捕获当前行为，再动结构；**该区域无覆盖就在碰结构前写 pin**；**type check 与 lint 不是 pin**。② 按 model-the-domain 命名缺失结构；形状已清晰且局部时 boring code 留；reshape 必须删分支或非法状态，不加间接性。③ 命名目标形状（module layout、types、call graph 按今天从零建会是什么样：foundational-thinking、redesign-from-first-principles）；目标跨函数边界就先 architect 做并行设计探索。④ subtract before you add（删死代码、塌陷单 caller wrapper、去冗余 validator、去 orphan reference，再引新形状）；最小改动到达目标形状就发；“might help”的投机清理 revert。⑤ 小步行为保持地移动，每步让 pin 绿；API reshape 时同一波迁移每个 caller 并删除旧 API（no compatibility shims、no parallel old/new）；每个 rename 对实际文件 spot-check——**rename 会静默漏掉字符串、prose 与 back-reference 里的用法**；机械编辑可按范围委派。⑥ 在真实 artifact 上证明行为未变，不是“能编译”；更大 reshape 跑 equivalence check（diff 老/新输出、录 baseline 重放到新代码、匹配 surface 的 smoke run）。⑦ 确认改动值得保留：成功度量是 reduced reader load；如果 diff 没在某处降低 reader load 就 revert。⑧ rebase 成小而有序列的提交（一个 subtraction commit、再 reshape、再 follow-on cleanup），每片行为保持且绿。Reply：变了的结构、对着哪个 pin、equivalence 证明、reader-load delta、发了什么/revert 了什么、无新行为。

**visual-parity（5 步）**：“You own pixel-exact equivalence. The baseline is the spec. You do not touch it.” Equivalence 由 image diff 验证，不靠眼睛。① **先建 baseline**（在任何迁移之前）：一个 visual regression harness，对当前组件跨其各状态截图；两实现匹配时还要目标侧截图；**无 baseline 就没有 parity claim**——这是阻塞性前置而不是 follow-up。② 反捷径条款，明说并守住：不改 harness、不篡改 baseline、不为让 diff 通过而重构组件；**若 baseline 看起来不对，停下并问，不要编辑它**。③ 一次迁移一个组件；跨 worktree 并行、一 owner 一组件；共享 primitive 作为阻塞 phase 先迁。④ 每个组件对着 baseline 在匹配 surface 上 image diff；**非零 diff 即 fail**；调查像素差；每组件循环到 diff 为零。⑤ 每组件或每个安全批次跑 opening-a-PR。Reply：迁了哪些组件、各自 diff 结果、baseline harness 位置、还剩什么。

**成立条件**：refactoring 需要可运行的行为 pin 或可建 pin；visual-parity 需要可在开始前建立的截图 harness 与稳定的目标 surface。

**失败模式/反例**：把 type check/lint 当行为 pin；无覆盖就动结构；reshape 只加间接性不删分支/非法状态；将“might help”的清理搭车；留 compatibility shim 或新旧并行路径；rename 只改代码不改字符串/prose 引用；verification 只看“能编译”；reader load 未降却留下 diff；visual parity 先迁移后补 baseline；篡改 baseline 或改 harness 让 diff 通过；目测代替 image diff；多个组件同时改导致无法定位差异。

### 3) 判断位点与 Profile 调用

| 位点 | 专业 concern | 何时调用 | 由哪个 Profile 提议 |
| --- | --- | --- | --- |
| B：行为契约保持不变 | 行为/兼容 | 结构改动、UI 迁移 | `behavior-domain`（契约）+ `implementation`（执行） |
| F：equivalence/pin/图像 diff 的证据 | 验证 | 结构改动与视觉迁移 | `evidence-evaluation` |
| D：目标形状与跨边界 | 技术 | reshape 跨函数边界 | `technical-planning`（a4 侧） |
| Driver：pin 绿才前进的序列 | 程序性 | 多步 reshape | `driver` |

### 4) 当前产品锚点、覆盖、缺口、为何值得吸收

- `profiles/behavior-domain.md` `## 心智模型`：“B 的产物是**可观察行为约定**……交付后，外部应该看到什么？什么能把正确与错误区分开？”
- `profiles/implementation.md` `## 常见误区`：“‘能改就改’：顺手重构、扩大改动面”；`## 边界事实`：“实现中若需改变共享语义、接口或验证依据，先停依赖该结论的工作”。
- `methods/cross-module-design.md` step 4：“Replace or remove old coverage only when the replacement demonstrably covers its accepted claim”。
- `methods/local-defect-feedback-loop.md` step 5：“Rerun the original scenario and relevant regression checks.”

具体缺口：

1. **没有“结构改动前先钉行为”的方法**：产品有“可观察行为约定”与“不改承诺”，但没有“characterization test/snapshot/equivalence harness，**type check/lint 不是 pin**”的操作；这条最容易在重命名/提取时被忽略。
2. **没有“reshape 必须删分支/非法状态，否则只是加间接”的判据**（包 1 MG-4 的 model-the-domain 覆盖结构清单，但未覆盖重构的成功度量）。
3. **没有 rename 的 spot-check 纪律**（字符串/prose/back-reference 会漏），这是多 agent 代码库的高频静默缺陷。
4. **没有 reader-load delta 作为保留标准**（包 2 MG-2 覆盖了读者负担概念，但没有“diff 不降 reader load 就 revert”的收口）。
5. **没有视觉等价方法**：baseline-first、反捷径条款、非零 diff 即 fail、共享 primitive 阻塞 phase——产品完全没有 UI 迁移的证据面。

为何值得吸收：这组直接补 B/F 的“行为保持”证据面，且全是判据级操作，零平台耦合。

### 5) 拟处置与载体

- 拟保留：pin-first（type check/lint 不是 pin）；无覆盖先写 pin；reshape 必须删分支/非法状态；目标形状命名与跨边界才 architect；subtract-first；“might help”投机清理 revert；小步行为保持 + 每步 pin 绿；migrate-callers/delete 同波；rename spot-check 字符串/prose/back-reference；真实 artifact 上证明；equivalence check 三形态；reader-load delta 作为保留标准；commit 序列；视觉 baseline-first、反捷径、一次一组件、共享 primitive 阻塞、image diff 非零即 fail。
- 拟改变：去 pstack 命令名/模型；去 image diff 工具与截图存储细节（可作例子）；把 PR/loop 机制改为“交付单元/迭代”一般词。
- 拟删除：与产品无关的 `/loop` 使用细节。
- 载体：方案 1（推荐）新增 `methods/refactor-and-visual-parity.md`（B/F 侧），在 `methods/README.md` 按需表加一行，`profiles/behavior-domain.md` 与 `profiles/evidence-evaluation.md` 各加一行入口；方案 2 拆成两份（结构重构 / 视觉等价），本包不推荐——两者共享“baseline/pin 先行、反捷径、真实 surface 验证”的同一判据。
- 与 a4 的分工：目标形状设计、跨边界架构、image-diff 工具实现归 a4；本组保留契约 pin 与证据纪律。

**平台耦合/依赖**：零平台耦合；视觉等价依赖真实渲染与截图工具（runtime）。

### 6) 正文草稿与验证方案

```
行为保持与视觉等价（草稿）
1. 先钉契约：characterization test / snapshot / equivalence harness；type check 与 lint 不算 pin；无覆盖先写 pin。
2. 命名目标形状；reshape 必须删分支或非法状态，否则不加间接。
3. 先减后加；小步移动、每步 pin 绿；API reshape 同波迁 caller 并删旧 API，不留兼容 shim。
4. rename 后核对字符串、prose、back-reference 的用法。
5. 在真实 artifact 上证明行为未变（输出 diff、baseline 重放、匹配 surface 的 smoke）；reader load 未降就 revert。
6. UI 迁移：baseline harness 先行（阻塞前置）；不改 harness、不篡改 baseline、不为通过而改结构；一次一组件；共享 primitive 先迁；image diff 非零即失败。
```

验证方案（未执行）：对一个真实重命名/提取，检查 (a) 是否先有行为 pin 且非 type-check；(b) rename 后字符串/prose 引用是否被核对；(c) reader-load 是否下降。对一次 UI 迁移，检查 baseline 是否先于迁移、是否有反捷径记录、每组件 diff 是否为 0。边界：无视觉 surface 不适用视觉方法；不要求所有重构都先写完整 harness（局部可恢复的小改动按产品 envelope 判断）。

---

## MG-5 记忆与偏好整理（A / meta）

### 1) 机制与触发情境；源锚点与已读/尚缺

| 源锚点 | 已读 | 尚缺 |
| --- | --- | --- |
| `continual-learning/README.md`（全文） | 全文 | 无 |
| `continual-learning/skills/continual-learning/SKILL.md`（全文，634B） | 全文 | 无 |
| `continual-learning/agents/agents-memory-updater.md`（全文，1811B） | 全文 | 无 |
| `continual-learning/hooks/continual-learning-stop.ts`（前 130 行 + README 的状态/环境变量说明） | 节奏与状态骨架 | 文件余部（索引刷新细节）归 a4 |
| `pstack/skills/automate-me/SKILL.md`、`workflow-from-chats/SKILL.md`、`reflect/SKILL.md` | 包 2/4 已读 | 无（本组与之判重） |
| `.cursor/hooks/*` 真实运行 | **未运行** | 所有 hook 行为仅从源码/README 读取 |

触发情境（README）：自动、增量地从 transcript 变化保持 `AGENTS.md` 最新；用户在会话中反复纠正/出现持久工作区事实时。

### 2) 操作、成立条件、失败模式、反例/例子

**三件套（README）**：stop hook 决定何时触发学习 → `continual-learning` skill 编排学习流 → `agents-memory-updater` 子代理挖新增/变更 transcript 并更新 `AGENTS.md`。防噪改写三条：**先读既有 `AGENTS.md` 并就地更新匹配 bullet**；**只处理新或有变更的 transcript**；**只写纯 bullet（无 evidence/confidence metadata）**。skill 标 `disable-model-invocation: true`（正常模型调用不会自动选中），运行时把全部记忆更新流委托给 updater。状态：`.cursor/hooks/state/continual-learning.json`（cadence）+ `continual-learning-index.json`（增量索引）。

**触发节奏（README）**：默认至少 10 个 completed turns、距上次至少 120 分钟、transcript mtime 必须自上次运行前进；trial 模式默认（hook 配置启用）至少 3 turns、至少 15 分钟、24 小时后自动过期回落默认。七个环境变量可覆盖（主名与 legacy 双名）：MIN_TURNS、MIN_MINUTES、TRIAL_MODE、TRIAL_MIN_TURNS、TRIAL_MIN_MINUTES、TRIAL_DURATION_MINUTES。

**updater workflow（逐条）**：① 先读既有 `AGENTS.md`；不存在则创建且只含 `## Learned User Preferences` 与 `## Learned Workspace Facts`；② 载入增量索引（若有）；③ **只检查** workspace 内 `agent-transcripts/` 下相对索引新增或 mtime 更新的 transcript；④ 只抽取 durable、reusable 的项：反复出现的用户偏好/纠正、稳定的 workspace 事实；⑤ 小心更新 `AGENTS.md`：**匹配 bullet 就地更新、只加净新 bullet、语义去重、每个 learned section 至多 12 条 bullet**；⑥ 刷新增量索引（处理过的 transcript；移除已不存在的文件条目）；⑦ 若合并未产生变化，**不改 `AGENTS.md` 但仍刷新索引**；⑧ 若无有意义的更新，**精确回复 `No high-signal memory updates.`**。Guardrails：只用纯 bullet；只保留两个 section；不写 evidence/confidence tag；不写过程指令、rationale、metadata block；**排除 secrets、private data、one-off instructions、transient details**。

**成立条件/失败模式**：有可读 transcript 与可写 `AGENTS.md`；有索引状态。失败模式：把一次性指令/临时细节写成记忆；把 secrets/私有数据写入；写下过程指令/rationale/metadata；无变化也改文件；在已有 section 之外新增结构；跨 workspace 读取。

### 3) 判断位点与 Profile 调用

| 位点 | 专业 concern | 何时调用 | 由哪个 Profile 提议 |
| --- | --- | --- | --- |
| A/Voice：接受记录与偏好固化 | 偏好/沟通 | 反复纠正、持久工作区事实 | `intent-voice`（A） |
| meta：经验编码 | 可维护性 | 同包 2 MG-3 / 包 4 MG-4 | `driver` |

### 4) 当前产品锚点、覆盖、缺口、为何值得吸收

- `profiles/intent-voice.md` `## 交接与召回`：“人类接受记录（决定、范围、条件）”。
- `docs/absorption/2026-10-02/EXECUTION-PLAN.md`：“记录从 source lead 到正式落地文件/固定对象；多源一个机制不能重复算知识增量。”（本组与 automate-me/workflow-from-chats 是同一机制族）。
- 项目 `AGENTS.md`：全局行为规则文件的存在。

具体缺口：

1. **没有记忆整理的“最小输出”纪律**：产品有接受记录，但没有“只两个 section、纯 bullet、无 evidence/confidence tag、无过程指令/rationale、每 section 至多 12 条、语义去重、无变化不变更、无更新时精确回复”——这些正是防止记忆文件腐烂的操作。
2. **没有增量处理与索引纪律**（只处理新/变更；刷新索引；移除死条目）——对应产品“不重做已有结论”的注意力纪律。
3. **没有“排除 secrets/private/one-off/transient”的边界**：与 `guide-redacted-evidence.md` 的敏感数据纪律相邻但对象不同（记忆文件）。
4. **与包 2 MG-3（lesson promotion）和包 4 MG-4（automate-me）重叠**：三者都是“从历史提取持久规则”；建议 gate 合并为一份“记忆/偏好整理”支持文件，避免三套标准。

为何值得吸收：A/Voice 的偏好固化需要“最小、可维护、无噪声”的产出纪律；与 automate-me 的入口纪律互补（一个管怎么采、一个管怎么存）。

### 5) 拟处置与载体

- 拟保留：先读后就地更新；只处理新增/变更；只写净新与去重；每 section 至多 12 条；无变化不变更但刷新索引；无更新时精确回复；只两个 section、纯 bullet、无 metadata/rationale/过程指令；排除 secrets/private/one-off/transient；节奏门槛（turns/minutes/mtime 前进）作为条件示例。
- 拟改变：去 hooks、状态/索引文件路径、环境变量名与 trial 机制（改为“按已接受节奏触发；可配置但不默认频繁”）；transcript 路径改为“本工作区可读会话记录”。
- 拟删除：hook 实现与 cron 语义（不复活 runtime）。
- 载体：方案 1（推荐）并入包 2 MG-3 / 包 4 MG-4 合并后的 `methods/guide-lesson-promotion.md`，作为“记忆文件整理”一节；方案 2 独立 `methods/guide-memory-curation.md`（代价：与 lesson promotion 触发重叠，三份标准漂移）。本包倾向方案 1，并建议 gate 把 continual-learning、workflow-from-chats、reflect、automate-me 视为**一个机制族**只算一份知识增量。
- **给 gate 的判重结论（事实）**：这四个来源共享“从会话/历史提取持久规则并编码”的机制；`continual-learning` 的独特增量是**存储侧整理纪律**（两个 section、纯 bullet、≤12、去重、无变化处理、无更新响应、隐私排除）。

**平台耦合/依赖**：hook/cron/状态文件是宿主；整理纪律零耦合。

### 6) 正文草稿与验证方案

```
记忆/偏好整理（草稿）
- 先读现有记忆文件；匹配条目就地更新，只加净新，语义去重。
- 只处理新/变更的会话记录；不重复处理已消化内容。
- 每个 section 至多 12 条；只保留固定 section；纯 bullet，无 evidence/confidence、无过程指令/rationale/metadata。
- 排除 secrets、私有数据、一次性指令、临时细节。
- 无变化：不改文件，但仍更新处理索引；无高信号更新时输出固定短句，不硬塞内容。
- 触发按已接受节奏（例如完成回合数 + 时间间隔 + 记录有变化），不默认频繁运行。
```

验证方案（未执行）：给一段含一次性指令、真实复现偏好、secret、临时细节的会话记录，检查 (a) 只有 durable 项进入且去重；(b) secret/一次性被排除；(c) 无变化时不改文件；(d) section 数与 bullet 上限守住。边界：不引入 hook/cron；记忆文件不等于责任定义或权限。

---

## 8. 包级综合观察（供 gate，不是裁定）

1. **判重结论（源侧事实）**：`thermo-nuclear-code-quality-review` 在两个插件字节相同；`continual-learning`/`workflow-from-chats`/`reflect`/`automate-me` 属同一“从历史提取持久规则”机制族；`create-verification-skill` 与本包 MG-3 属同一“驱动真实 surface”机制族。吸收时应按机制合并计数，避免重复知识增量。
2. **package 1 MG-7 与本包 MG-1 的接口**：MG-1 是“任务如何发布与终止”，MG-7 是“结果如何交接与分级”；建议在 `methods/README.md` 中相邻列出，或合并为一份交接/编排支持文件。
3. **runtime 边界**：orchestrate 与 continual-learning 都是 runtime 产品；本包只提取逻辑层契约与整理纪律，未吸收状态机、脚本、hook、索引实现。请 gate 在采纳时确认没有把 runtime 机制带入产品。
4. **A/F 交界**：MG-5 的隐私/一次性排除与 `guide-redacted-evidence.md` 相邻但对象不同（记忆文件 vs 证据移交）；建议相互引用而非合并。
5. **风险提示**：MG-4 的 visual-parity “baseline 先行”若被写成所有 UI 改动的强制前置会过度流程化；正文应限定在“像素级等价/样式系统迁移”的适用条件。

## 9. 未读残余（本包未覆盖；不假装已评估）

- `orchestrate/skills/orchestrate/prompts/andon-block.md`、`slack-block.md`（本轮已读但未在正文逐字引用；内容属 runtime 通知面）。
- `orchestrate/scripts/*`、`schemas/*`、`__tests__/*`、`cursor-sdk`（a4）。
- `continual-learning/hooks/continual-learning-stop.ts` 余部、plugin.json。
- `cursor-team-kit/agents/thermo-nuclear-code-quality-review.md`（与 thermos 子代理的差异未逐字比较）。
- 其余同仓目录与包 1–4 的未读残余相同（pstack 其余 playbooks、arena/swarm/no-comments 等 SKILL 正文、docs-canvas、pr-review-canvas 资产、create-plugin、grok-voice、third_party 等）。

## 10. 包内自检（机械项，非专业裁定）

- 源 pin 与路径：均为 `ecc249f1e306fc64ddf83c7bed16cacf7c2239db` 下实际存在的路径；
- 未修改产品/他人文档/registry；未 commit；
- 每组含 6 项要求；所有验证方案标注未执行；重复载体的 md5 事实已给出；runtime 内容标注为不吸收。
