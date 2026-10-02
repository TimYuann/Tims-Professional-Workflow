# A4-CURSOR-DEF · cursor-plugins 审核包（族 D/E/F＋playbook 支持文件/脚本/资产＋尾部未评估区）

- 实例/角色：`tpw-absorb-a4`（A 类发现者；只产出审核包，不裁定采纳）。
- 源仓与 pin：`cursor-plugins` @ `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`（863 paths）。
- 只读 locator：`.worktrees/legacy-pre-night-2026-10-01/upstreams/cursor-plugins`（本 session 全部 `git show <pin>:<path>` 读取，未 checkout、未执行、未写源）。
- 导航索引：`docs/overnight/2026-10-01/ABSORB-A2-CURSOR-INDEX.tsv` + `ABSORB-A2-CURSOR-HEADER.md`（仅作导航，旧 read_depth/标签不作资格）。
- 产品基线：night worktree（tip `3c00457`；Driver 记录基线 `800414d`）；core 21 文件在 `professional-workflow/`；Backbone 冻结不改。
- 边界：**本包不产生任何采纳裁定**，不修改产品/他人文档，不建 registry/框架，不 commit，不执行任何源脚本；所有"可执行观察"一律标注为未执行。
- 分工：A/B/C 主干归 `tpw-absorb-a2r`（其 `A2R-CURSOR-ABC1..4` 已交）；本包只做 D/E/F 与 playbook 支持材料、脚本、资产、尾部。为避免重复，§1 先列 a2r 已覆盖项，本包不再复述。

---

## 0 · 本 session 读深声明（诚实账）

**pin 内逐字全读**（`git show` 原文）：

- orchestrate：`README.md`、`skills/orchestrate/SKILL.md`、`references/{spawning,handoffs,planner,dispatcher}.md`、`prompts/{worker,verifier,root,subplanner,loop-hygiene,andon-block,slack-block,failure-handoff,empty-error-handoff,finished-no-handoff}.md`、`scripts/core/{loop,handoff,failure-handoff,redact-body,andon,comment-retry-queue}.ts`、`scripts/measurements.ts`。
- pstack 脚本：`skills/poteto-mode/scripts/check-plan.mjs`、`scripts/worktree-audit.sh`；`scripts/orch/store.ts` 选读（1–110、324–445、1200–1380、1432–1480 行）+ 函数面 grep；`scripts/watch-pr/types.ts` 全文；`scripts/watch-pr/policy.ts` 1–520 行（约 2/3）；`scripts/watch-pr/github.ts` 选段。
- pstack playbooks：`multi-phase-plan.md`（主体）、`eval.md`、`perf-issue.md`、`hillclimb.md`、`runtime-forensics.md`、`trace-forensics.md`、`shipping.md`、`babysit.md`、`autopilot-full.md`、`autonomous-run.md`、`pause-safely.md`、`worktree-cleanup.md`、`session-pickup.md`、`orchestrate.md`（前 90 行）。
- pstack skills：`create-verification-skill/SKILL.md` + `references/feature-map-example/{README,create-note}.md`、`maintain-verification-skill/SKILL.md`、`blast-radius/SKILL.md`、`show-me-your-work/SKILL.md` + `scripts/log.sh`、`interrogate/references/{rubric,lead-judgment}.md`、`why/references/{epistemics.md,sources/incident-postmortem.md,sources/datadog.md}`、`docs/guide/{04-design,06-verify-and-ship,07-overnight}.md`。
- hooks：`advisor/hooks/{hooks.json,lib.sh,capture-response.sh,mark-pending.sh,record-consult.sh,stop-hook.sh}`、`ralph-loop/hooks/{hooks.json,capture-response.sh,stop-hook.sh}` + `ralph-loop/skills/{ralph-loop,cancel-ralph}/SKILL.md` + `ralph-loop/README.md`、`continual-learning/hooks/{hooks.json,continual-learning-stop.ts}`。
- first-party：`cursor-team-kit/skills/{control-cli,control-ui,thermo-nuclear-code-quality-review}/SKILL.md`、`thermos/skills/thermos/SKILL.md`、`cli-for-agent/skills/cli-for-agents/SKILL.md`、`agent-compatibility/README.md`（前 80 行）、`docs-canvas/skills/docs-canvas/SKILL.md`（前 40 行）、`teaching/skills/run-learning-retrospective/SKILL.md`（前 30 行）、`pr-review-canvas/{README.md,skills/pr-review-canvas/SKILL.md}`、`cursor-team-kit/skills/pr-review-canvas/SKILL.md`（前 40 行）。
- 工程原则（D/E/F 侧 12 条）：`principle-{type-system-discipline,make-operations-idempotent,migrate-callers-then-delete-legacy-apis,separate-before-serializing-shared-state,boundary-discipline,prove-it-works,fix-root-causes,sequence-verifiable-units,test-behavior-not-implementation,encode-lessons-in-structure,build-the-lever,guard-the-context-window}/SKILL.md`。
- cursor-sdk：`skills/cursor-sdk/SKILL.md` 全文；`references/error-handling.md` 1–120 行；`references/runtime-choice.md` 前 60 行。
- benny：`pstack/automations/benny/{FOR_AGENTS.md,README.md(前80行),templates/configuration.example.yaml,skills/reproduce-and-fix-issues/references/{control-adapter.md,verify-existing-fix.md}}`。
- 装配面：`scripts/validate-plugins.mjs`、`.github/workflows/validate-plugins.yml`、`create-plugin/rules/plugin-quality-gates.mdc`、`schemas/{plugin,marketplace}.schema.json`（字段面）、`.cursor-plugin/marketplace.json`（头部）；`third_party/*/mcp.json` + `.cursor-plugin/plugin.json` 79 组用 jq/脚本做字段解析（机器提取，非逐字散文通读）；`third_party/github/README.md` 前 60 行 + `CHANGELOG.md` 头、`third_party/shopify-store/rules/shopify.mdc` 全文、`third_party/x-money/skills/x-money-guide/SKILL.md` 前 90 行、`third_party/x/skills/x-chat/SKILL.md` 前 50 行、`third_party/x/skills/x-api-mcp-guide/references/pricing.md` 前 50 行 + `SKILL.md` 标题面。

**只读标题级/结构级**（不作机制断言）：orchestrate `scripts/__tests__/` 28 个测试文件的 `describe/test` 名称与计数；`pstack/skills/poteto-mode/scripts/orch/orch.ts`、`orch.test.ts`（grep 签名/标题）；`watch-pr/{render,cli}.ts`（结构面）。

**本包明确未读**（列入 G-14/T-* 尾部，不假装已评估）：orchestrate `schemas/*.json` 全文、`cli/util.ts`、多数测试正文、`adapters/slack/index.ts` 正文；pstack 未读 playbook（`bug-fix,feature,refactoring,prototype,visual-parity,authoring-a-skill,opening-a-pr,investigation`）、`skills/{arena,swarm,architect,how,reflect,recall,tdd,unslop,automate-me,figure-it-out,setup-pstack,make-bot-ui,typescript-best-practices}/` 正文、`why` 其余 reference 与 sources、`interrogate/{SKILL.md,references/code-quality-review.md,reviewer-prompt.md}`；cursor-sdk 五个 reference（auth/streaming/mcp/advanced/patterns）；benny 三个 SKILL 正文与 `templates/{triage,reproduce}-automation-prompt.md`；third_party 79 份 README/CHANGELOG 散文、94 个 LICENSE、91 个品牌资产；cursor-team-kit 其余 skills、grok-voice 四技能、advisor/ralph-loop/continual-learning 的 skills+agents 正文（a2r 已读 advisor SKILL）。

---

## 1 · 与 a2r 的分工声明（本包不复述的部分）

`A2R-CURSOR-ABC1/2/3/4` 已完成下列 D/E/F 邻接面的**散文级**阅读；本包默认其转述可用，只在需要**实现层核对**时引用并补脚本证据：

| a2r 位置 | a2r 已覆盖 | 本包处理 |
| --- | --- | --- |
| ABC1 MG-4 | 领域结构先行（C）与边界纪律（D/E，"交 a4 参考"） | 本包 G-12 用 `principle-type-system-discipline`/`principle-boundary-discipline` 原文补齐操作；不复述 C 侧 |
| ABC1 MG-5 | `create-verification-skill`/`maintain-verification-skill` SKILL 全文、guide 06 | 本包 G-08 只做 SKILL 未读面的支持文件与脚本：feature-map `search.md`、`control-adapter.md`、`verify-existing-fix.md`、`control-ui/cli`、benny 运行契约 |
| ABC1 MG-6 | thermo-nuclear/interrogate SKILL、advisor SKILL、thermos/SKILL | 本包 G-10 只补 `interrogate/references/code-quality-review.md`、thermos 重复载体、agent-compatibility 评分面 |
| ABC1 MG-7 | `references/handoffs.md`、worker/verifier prompts 全文、prompts 摘录 | 本包 G-02 做实现层核对：`core/handoff.ts`/`failure-handoff.ts`/`measurements.ts` 的实际解析与判定，并补 prompts 未读件（root/subplanner/loop-hygiene/andon-block/slack-block/failure-handoff/empty-error/finished-no-handoff） |
| ABC1 MG-8 | show-me-your-work SKILL、autonomous-run/pause-safely/session-pickup、ralph stop-hook、advisor stop-hook、log 模板+`log.sh`（补读） | 本包 G-07/G-11 补其余 hooks 实现与 playbook 支撑；log.sh 的公式注入防护已被 a2r 记录，本包不再重复 |
| ABC2 MG-5 | `principle-separate-before-serializing-shared-state`、`principle-make-operations-idempotent` 全文 | 本包 G-12 只给**实现证据**（`orch/store.ts` 的锁/原子写）与 type-system/lever 面；不重提幂等三问本身 |
| ABC3 MG-5 | interrogate rubric/lead-judgment/reviewer-prompt、why synthesizer-prompt、decision-log 模板、log.sh、advisor-subagent、feature-map README+create-note、orchestrate worker/verifier prompts | 本包不重复；其残余清单（code-quality-review、why sources、orchestrate 其余 prompts、pr-review-canvas 资产）即本包 G-09/G-10/G-14 的主要输入 |

---

## 2 · 本包机制组总览

| 组 | 名称 | 主责任位点 | B 台账旧行（仅导航） |
| --- | --- | --- | --- |
| G-01 | 长任务编排循环：状态重建、检查点、退出码、看门狗 | D/E/F | PEND-02、ORC-05 |
| G-02 | 交接解析、合成失败分类与测量复核（实现层） | F/D | DES-10 部分、EVID-07/09/10、PEND-02 |
| G-03 | Andon、操作者边界、Slack 边界与脱敏 | D/F（安全） | ORC-05/06、PKG-06 |
| G-04 | 文件库编排：单写者状态、锁、原子写、frontier/ledger | D/E/F | DES-10/11/12、ORC-05/12 |
| G-05 | PR/CI 判定状态机与查询失败分类 | D/F | EVID-22、CONC-02 邻接 |
| G-06 | worktree 审计与安全回收 | D/E（安全） | DLV-05、ORC-13 |
| G-07 | 回合钩子与自主循环实现 | E/F（持久化） | ORC-06/07/10 |
| G-08 | 验证面支持文件与 benny 运行契约 | F/E | ORC-12、PKG-* 邻接 |
| G-09 | 历史动机调查与置信度分层 | F/D | DLV-11/12、AUTH-08 邻接 |
| G-10 | 评审镜头、过滤与重复载体 | F/D | EVID-13/14、PKG-11 |
| G-11 | 计划即交付物：核验单元、车道、patch-id | F/D/Driver | EVID-14、DLV-03/06、ORC-02/13 |
| G-12 | 类型/边界/原子写/工具化与 SDK 生命周期 | D/E | DES-09/11/12/24、PEND-03 |
| G-13 | 连接器装配、凭据形态、清单校验缺口 | D/F（安全） | PKG-01..10/12、PEND-01/07 |
| G-14 | 尾部与未评估区（含纯资产、重复载体） | 归组 | PKG-09/11、PEND-01/03 |

---

## G-01 · 长任务编排循环：状态重建、检查点、退出码、看门狗

### 1) 机制与触发情境；源锚点与已读/尚缺

触发情境：把一个目标交给**没有长时内存**的脚本+云代理树执行（小时级、崩溃/重启/断流正常）；需要回答"循环还活着吗、能不能重入、何时停、停了是错误还是计划内"。

源锚点（pin 内）：

- `orchestrate/skills/orchestrate/scripts/core/loop.ts`（全文）：`runOrchestrateLoop`、`SPAWN_SWEEP_INTERVAL_MS=10s`、`PLANNED_CHECKPOINT_EXIT_CODE=100`、`EXIT_ON_ERROR_EXIT_CODE=1`、`DEFAULT_MAX_RUNTIME_SEC=3600`、`preExistingErrors`、`plannedCheckpointRestart`、`flagUnreachablePending`、`computeLoopExitCode`、`pendingCouldStillSpawn`（含环检测）。
- `orchestrate/skills/orchestrate/scripts/core/agent-manager.ts`（选段）：`recoverRunning`（750–800）、`recordRecoverFailure`、`waitAndHandoff`（830–900 起）、`syncStateToGit`+`mirrorTaskToSlack`（1317–1380）、`waitRunWithWatchdog`（1839–1935）、`inspectRunStream`/`redactToolCallPayload` 签名面。
- `orchestrate/skills/orchestrate/prompts/loop-hygiene.md`（全文）：前台运行、100 不是错误、1 是 planner 的回合、失败 handoff 处置、`After run returns, call tree`、`Don't end your turn while this workspace has non-terminal tasks`。
- `orchestrate/skills/orchestrate/prompts/root.md`、`references/planner.md §Phase 2/Failure recovery`。
- 测试（标题级）：`__tests__/{checkpoint-restart,exit-on-error,wait-handoff-failure,watchdog-inspect}.test.ts`。

已读：上述全部；尚缺：`scripts/schemas.ts`/`cli/task.ts` 的 spawn 细节、`agent-manager.ts` 未读区间、`cli/util.ts`。

### 2) 操作、成立条件、失败模式、反例/例子

操作（实现层）：

1. **脚本是心跳，不是可分离的 worker**：`run` 前台跑；退出码契约：`0` 干净完成、`100` **计划内检查点重启**（已 `syncStateToGit` 提交 state/handoffs，重跑同命令即续）、`1` 本轮有新 error 或收尾时仍有 pending/cancelled。`--exit-on-all-done` 才回到"排空到静止"旧行为。
2. **重入先重建**：启动时对每个 `running` 调 `recoverRunning`（需同时有 `agentId` 与 `runId`；缺一即 `recordRecoverFailure` 标 error 并写 `<task>-failure.md`），用 `Agent.getRun` 重新挂上后 `waitAndHandoff`；`preExistingErrors` 集合保证**上次遗留的 error 不会让首次 sweep 短路**，只有本次新转入 error 才 `exit-on-error`。
3. **可真进展判定**：`canMakeProgress` = 有 running，或有 pending 且依赖链上没有 failed-terminal / 缺失 / 环。上游失败时下游保持 `pending`（**不自动 prune**）；循环退出后 `flagUnreachablePending` 给每条被阻塞的 pending 写 attention，恢复路径是"修上游再跑"或显式 `kill`。
4. **看门狗**：`waitRunWithWatchdog` 把 `run.wait()` 与周期性 `Agent.getRun` 轮询 `Promise.race`；SSE 静默但服务端已终态时轮询赢；分级日志（内部 idle 阈值 → 用户可见 `; stuck`，tool_call 另有阈值与环境变量覆盖）。失败侧记录从 `lastSseActivityAt` 取，避免 `touch` 覆盖 `lastUpdate` 后尸检显示终止时间。
5. **单行心跳**：每次 sweep 打 `[ISO] sweep <rootSlug>: pending=… running=… handed-off=… [ANDON]`，让 tail/轮询能区分"仍在 reconcile"与"死了"。

成立条件：状态文件 + git 是权威；每轮只做可重入的 reconciliation；runtime 支持按 id 重挂。

失败模式/反例：

- 把 `100` 当错误停止 → 树永远不续；把 `1` 当基础设施错误重启 → planner 失去回合。
- 用上一次遗留的 error 直接 exit-on-error → 永远无法恢复。
- 把 pending 当"已完成/可丢"自动 prune → 恢复路径消失。
- 会话结束时仍有非终态任务就结束回合 → 心跳停但任务在跑，树失去 reconcile。
- 只信 `run.stream()`：SSE 卡死时循环永久悬挂；`run.wait()` 无 `Agent.getRun` 兜底即单点。
- 部分身份（只有 agentId 或只有 runId）当 running 继续等 → 僵尸行。

### 3) A–F 判断位点与专业 concern

| 位点 | concern | 何时调用 | 拟供 Profile |
| --- | --- | --- | --- |
| D：恢复面与收敛性（状态是权威、重入幂等） | 持久化/可恢复性/长任务 | 任何跨进程、跨会话、可崩溃的长任务 | `technical-planning`（Commitments/Recall 与恢复条件） |
| E：实现循环、退出码、心跳 | 实现/运维 | 写跑批/编排脚本 | `implementation` |
| F：如何观察"还活着/已完成" | 证据/可观察性 | 需要判断长任务状态时 | `evidence-evaluation` 的验证设计 |
| Driver：何时重跑、何时 kill、何时停 | 程序性路由 | 上游失败、检查点、关闭 | `driver` |

### 4) 当前产品锚点、覆盖与缺口

- `profiles/technical-planning.md` 有 Commitments / Delegated Decisions / Recall Conditions；`profiles/driver.md` 有依赖/关闭/召回。
- `methods/local-defect-feedback-loop.md` `## Limits` 已写"不要求特定 control skill、loop 命令…"；`methods/README.md` 声明按需绑定。
- 缺口：**没有任何"长任务循环的收敛与恢复纪律"**——重入、检查点退出码、上游失败时下游不 prune、heartbeat、watchdog/断流兜底、部分身份当错误。这些不依赖 Cursor，可抽象为：状态文件权威、启动时重建、计划内检查点、只对新增错误提前退出、被阻塞项显式记账。

为何值得吸收：这是 D/E 在"无人值守/多小时任务"上最实操的失败面；产品目前只有单会话缺陷环，没有跨进程收敛面。

### 5) 拟处置与载体

- **拟保留（可独立于 Cursor）**：状态权威 + 重入重建 + 计划检查点（同步后退出、可重跑）+ "只在新增错误时提前退出" + 阻塞项显式记账（不自动 prune）+ 单行心跳 + 断流看门狗。
- **拟改变**：`Agent.getRun`/`Run.wait`/SSE 换成"runtime 提供按 id 重挂与终态查询（若没有，就不得声称可重入）"；`bun cli.ts run` 换成任务自身入口；10s/3600s 默认值标为来源参数而非规范。
- **拟删除**：Cursor 云代理、Slack、`state.json` 具体 schema、`exit 100` 字面值（保留"计划内重启码"语义）。
- **载体落点（建议，待 gate 裁定）**：`methods/` 增一份按需方法（如 `long-run-recovery.md`），或在 `local-defect-feedback-loop.md` 后新增一节；`profiles/implementation.md` 的"按需方法入口"加一行；`technical-planning.md` 的 Recall Conditions 处交叉引用。
- **仍依赖真实 runtime**：重挂、取消、运行中查询、断流检测；没有这些能力时只能降级为"前台阻塞式运行 + 落盘检查点"。

### 6) 可讨论正文草稿/操作例子 + 验证方案

```markdown
## 长任务重入检查（操作）
1. 启动时扫描既有状态：对每个"运行中"重新挂载；挂不上（无 id/查询失败）立即标错并写尸检，不要静默等待。
2. 记录启动前的错误集合；只有本次新转入的错误才让循环提前退出。
3. 每轮结束打印一行计数心跳（pending/running/done/error）。
4. 到达时间预算：提交状态与产物、以"计划内检查点"退出；重跑同命令必须从提交点续，不得从头重做。
5. 上游失败：下游保持 pending 并在日志记账；不要自动删除，恢复 = 修上游重跑，或显式取消。
6. 断流兜底：终态等待与"运行中查询"竞争；查询到终态就采用，不要等死流。
```

验证方案（**未执行**）：对一个可崩溃的本地 tasks-runner（如 `bun` 脚本 + JSON state）做三组观察：① 第一轮 kill -9 后重跑，任务从断点续且不重复副作用；② 注入上游 error，确认下游 pending + 一条 attention，修上游后重跑收敛；③ 人为让终态回调静默，确认轮询路径能收尾。边界：不要求所有任务都持久化；单会话、可重跑成本极低的脚本可只用前台阻塞式。

---

## G-02 · 交接解析、合成失败分类与测量复核（实现层，对 a2r MG-7 的核对）

### 1) 机制与触发情境；源锚点与已读/尚缺

触发情境：多实例并行时，唯一信息通道是"每任务一份最终消息"；实例会死不写交接，会自报数字，会把构建通过说成验证通过。

源锚点（pin 内）：

- `orchestrate/skills/orchestrate/scripts/core/handoff.ts`（全文）：`parseHandoffBranch`（`(no branch)`、反引号、CRLF、`##` 视为空）、`resolveRunBranch`（正文 > SDK branches > placeholder）、`parseHandoffVerification`（canonical `## Verification` 优先；legacy `## Verdict` 保守映射）、`parseHandoffFailureMode`、`parseHandoffPrNumber`、`writeHandoff`（header + 非 finished 加 banner，tmp+rename）、`emptyErrorHandoffBody`。
- `orchestrate/skills/orchestrate/scripts/core/failure-handoff.ts`（全文）：`classifyFailureMode`（OOM 优先于 cap-hit；70–80 分钟窗口；network/tool 正则）、`writeFailureHandoff`、`writeFinishedNoHandoff`、`hasStructuredHandoff`（`/^##\s+(Status|Verification)\s*$/m`）、各模式建议、`atomicWrite`。
- `orchestrate/skills/orchestrate/scripts/measurements.ts`（全文）：`parseHandoffMeasurements`（区分 `(none)` 与缺失）、`parseMeasurementLine`（算子需两侧空白）、`compareMeasurement`（10% 默认容差；单位必须一致，MB vs KB 直接 mismatch；否则退化为字符串相等）、`checkoutBranchForMeasurement`（`--depth 1 --branch` 临时 clone）、`buildMeasurementEnv`（**白名单** + 全新 scratch HOME）、`runMeasurementCommand`（`bash -c` 而非 `-lc`，防 rc 重新导出凭证）、parser `wc-l`/`regex`。
- `orchestrate/skills/orchestrate/core/redact-body.ts`（全文，见 G-03）。
- prompts（全文）：`worker.md`（Status/Branch/What I did/Measurements/Verification 四值/Notes/Suggested follow-ups；质量底线；崩溃时不要写临终防御）、`verifier.md`（`Run the code. Reading the diff is not verification.`；环境失败必须 `verifier-blocked`；不改目标源文件、不 merge/rebase/PR）、`failure-handoff.md`、`empty-error-handoff.md`、`finished-no-handoff.md`、`loop-hygiene.md`、`subplanner.md`、`root.md`、`slack-block.md`、`andon-block.md`。
- 测试（标题级）：`handoff-branch-parser`、`handoff-verification-parser`（14 例）、`handoff-verification-record`（5）、`failure-handoff`（14）、`wait-handoff-failure`（4）、`measurements-{parser,compare,mismatch}`（6+16+3）、`redact-body`（5）、`slack-prompt-shape`（11）、`worker-branch-discipline`（4）、`prompt-plan-validation`（3）。

已读：上述全部；尚缺：测试正文、`agent-manager.checkWorkerMeasurements` 全路径（选段已读）。

### 2) 操作、成立条件、失败模式、反例/例子

**与 a2r MG-7 的核对结果**：a2r 对 `handoffs.md` 的转述在实现层成立，并可由脚本补出三处**更硬的判据**：

1. **早退出条件基于"新错误"**：`failure-handoff.ts` 的分类只决定建议，是否 exit-on-error 由 `loop.ts` 的 `preExistingErrors` 决定——a2r 记录了两层，但未写"新错误"这个精确门。
2. **测量复核是不可自证的**：`checkWorkerMeasurements` 在 worker 的**真实 branch** 上浅 clone 重跑任务声明的 `measurements[]`；差值 >10% 或单位不一致写 attention；worker 未推真实分支就跳过并记 attention；worker 仍照常 handoff、由 planner 决定 respawn。命令环境是白名单 + 空 HOME + **非登录 shell**——这是"自报数字不可信"的具体可执行形态（对应 EVID-07/10）。
3. **`(none)` ≠ 缺失**：`parseHandoffMeasurements` 区分显式 `(none)` 与整节缺失；缺失会在 `checkWorkerMeasurements` 中被记为 attention。a2r 只写了"无量化写 (none)"。

其它实现级操作：

- 交接文件的**写入顺序**：先写 handoff 文件再改 state，避免下游看到 `handed-off` 却没有文件；非 `finished` 的运行在正文前加"⚠️ 无结构化交接，以下为原始输出"banner，防下游误解析。
- **结构化交接的判据**：`hasStructuredHandoff` 只认 `^## Status$` 或 `^## Verification$`；普通散文即使有内容也判 `finished-no-handoff` 并生成 sidecar + raw snippet（截断 2000 字符）。
- **合成失败分类**：`cap-hit`（70–80 分钟且 terminal error）、`oom`（OOMKilled/137）、`network-drop`、`tool-error`、`unknown`；OOM 优先于 cap-hit。建议的 retry 策略绑定模式；同一任务 2 次重试后倾向 abandon，而不是第三次。
- **env 传播反例（原文）**：`Cloud-agent VMs may redact environment variable values as a prompt-injection defense... Never paste credentials into scopedGoal; it is sent to the model provider and may end up in git history when state sync is on`。跨 agent 共享数据必须走"planner 写文件到 base 分支 + 下游按路径读"。

失败模式/反例：

- 用文件 mtime/`status=finished` 代替结构化交接 → sidecar 路径（反例：finished 但无 `## Status`）。
- 让 verifier 不跑只读 diff 就出 verdict → 源文明确这不是验证；环境失败伪装成 `type-check-only` 是允许的最坏欺骗。
- 自报测量被当作已验证（本组给了重跑机制，但产品侧此前没有）。
- 将 planner-authored 数字直接当证据（`hadPreviousPassingCi`、`measurements` 都在实现里被独立重查）。

### 3) A–F 判断位点与专业 concern

| 位点 | concern | 何时调用 | 拟供 Profile |
| --- | --- | --- | --- |
| F：交接证据等级与"实际执行了什么" | 验证/证据/独立性 | 跨实例声称验证结果时 | `evidence-evaluation` |
| D：交接面/解析契约（不可自证） | 接口/持久化 | 设计多实例协议时 | `technical-planning` |
| E：写入顺序、原子写、分类实现 | 实现/运维 | 实现交接/尸检 | `implementation` |
| Driver：重试/放弃/关闭 | 程序性 | 失败分诊时 | `driver` |

### 4) 当前产品锚点、覆盖与缺口

- 已覆盖：`behavior-claim-evaluation.md`（claim/对象/版本/baseline/treatment/三态）、`guide-redacted-evidence.md`（脱敏/custody）、`local-defect-feedback-loop.md`（复现/假设/回归）。
- 缺口：**"跨实例交接的不可自证面"**——结构化交接判据、非 finished 的 banner、测量重跑与容差/单位、环境白名单、失败模式分类与"2 次后 abandon"、下游 relay 逐字粘贴的污染问题。a2r MG-7 覆盖了格式；本组给出**实现判据**。

为何值得吸收：所有"子代理/并行实例自报完成"的场景都会遇到；产品已有证据哲学（"自测不等于独立评价"），但缺"怎么把自报变成可复核输入"的操作。

### 5) 拟处置与载体

- 拟保留：交接"唯一通道 + 逐字保存 + 不加料"；结构化判据（必含 status/verification 头）；非正常结束的 banner；测量重跑（容差+单位）；命令环境白名单 + 空 HOME + 非登录 shell；失败模式分类与重试建议；"2 次后 abandon"；"不要写临终防御"。
- 拟改变：`handoffs/*.md` 路径与 CLI 名去掉；`cap-hit 70–80 分钟` 标为对某 runtime 的观察而非通用值；把"planner 决定 respawn"改成"接到结果的人决定（责任位点依 Charter）"。
- 拟删除：Cursor/Slack 专属、PR 号解析、`kill`/`andon` 命令表面。
- 载体落点：并入 `methods/behavior-claim-evaluation.md` 的操作扩展或新增按需方法 `handoff-evidence.md`；`profiles/evidence-evaluation.md` 关键问题补一条"这是我跑的还是别人自报的"。
- 仍依赖 runtime 的能力：真实重跑命令、临时 checkout、进程环境隔离；没有隔离能力时至少记录"未复核自报"。

### 6) 可讨论正文草稿/操作例子 + 验证方案

```markdown
## 交接复核（操作）
- 只接受结构化交接：必须能解析出 Status 与 Verification/verdict；散文结尾按"无交接"处理，保留原文但标注。
- 交接口径：逐字保存，不重排不美化；下游依赖的上下文必须粘贴上游原文，worker 之间不共享 branch。
- 声明了量化指标的任务：在交付分支上重跑同一命令，比对数值（默认 10% 容差）与单位；单位不一致直接记不一致，不折算。
- 重跑命令的环境只带白名单变量，HOME 指向空目录，shell 不用登录模式；不携带任何用户凭证与 dotfile。
- 运行以失败结束：先分类（资源上限/内存/网络/工具/未知），按模式决定缩小范围或换模型；同一单元两次重试后倾向放弃并重规划。
- 验证结论：只有真正运行过才算；环境阻断写"未验证"，不得用更弱的检查伪装。
```

验证方案（**未执行**）：构造一个假 worker 输出：① 自报 `bundle size: 2.41 MB → 2.39 MB` 但分支实际 2.90 MB → 应记 mismatch；② 声明 MB、实测 KB → 必须单位不一致而非折算；③ 只有散文无标题 → 应生成"无交接" sidecar；④ 命令里尝试读取 `$HOME/.aws/credentials` → 空 HOME 使它失败且日志不含敏感值。边界：不要求每个任务都有量化指标；没有可重跑命令时，如实标"未复核"而不是假装复核。

---

## G-03 · Andon、操作者边界、Slack 边界与脱敏

### 1) 机制与触发情境；源锚点与已读/尚缺

触发情境：并行树继续产出会浪费/污染；需要一条人类可触发的全局暂停；机器侧无人值守时要区分"任务自己卡住"与"整棵树都会产出垃圾"；要把输出写到外部通道但不能越权或带秘密。

源锚点（pin 内）：

- `orchestrate/skills/orchestrate/scripts/core/andon.ts`（全文）：`AndonPoller.drainEvents`（从 Slack `:rotating_light:` 或缓存的 git state 读取；只在新状态/原因变化时 `saveState`；失败写 attention 不中断）、`SlackReactionAndonSource`（扫最近 20 条回复，解析 `🚨 ANDON RAISED: <reason>`，截断 500 字符）、`isAndonActive`、`isValidAndon`（用 zod schema 校验 git-fetched JSON）。
- `orchestrate/skills/orchestrate/prompts/andon-block.md`（全文）+ `references/planner.md §Andon`：raise 必须带 reason；只在"继续 spawn 会产生垃圾"时用；单任务卡住写 `Status: blocked` handoff。
- `orchestrate/skills/orchestrate/scripts/core/redact-body.ts`（全文）：2048 字符上限、敏感赋值 `token|secret|password|api_key|authorization` → `[redacted]`、`/workspace`、`/Users`、`.pnpm` 路径、反引号外的 40 位 SHA、连续 5 行日志前缀判为 log dump。
- `orchestrate/skills/orchestrate/scripts/core/comment-retry-queue.ts`（全文）：`allowedSlackThread` 守卫（只允许 run thread，禁 DM/频道根/兄弟线程；`drainCommentRetryQueue` 再查一次，防直接写队列绕过）、backoff `[1s,5s,30s,5m,30m]`、`required` 才入队、幂等入队（同 destination/body/sender）。
- `orchestrate/skills/orchestrate/scripts/adapters/slack/index.ts`（结构/签名面）+ `adapters/types.ts`。
- 测试（标题级）：`operator-boundary.test.ts`（4 例：忽略 `ORCHESTRATE_OPERATOR` 无 home flag；要求 current-user 0600；不信 HOME 覆盖/符号链接；工作区内加载 run thread）、`slack-channel-boundary`（4）、`andon-root-cache`（14）、`redact-body`（5）、`comment-retry-queue`（10）。

已读：上述；尚缺：`adapters/slack/index.ts` 正文、`cli/{andon,comments,inspect,forensics}.ts` 正文、`references/planner.md §Comments`（部分经索引）。

### 2) 操作、成立条件、失败模式、反例/例子

- **Andon 语义**：暂停**新 spawn**（不是杀在跑任务）；root 捕获原因并写入 `state.andon`，子代理通过 `plan.andonStateRef/Path` 从 git FETCH_HEAD 读缓存，子代理不直接调 Slack；reason 上限 500 字符；raise 需理由；`clearedAt/clearedBy` 记录恢复。
- **操作者模式**：外部操作需要 `~/.orchestrate/operator-mode`，且必须是**当前用户所有、0600**；不信任环境变量 `ORCHESTRATE_OPERATOR`、不信任 `HOME` 覆盖、不信任符号链接；worker 被假定无法写用户的 home。
- **Slack 边界（三层）**：① plannner 写入必须在 run thread（`allowedSlackThread` 同时校验 channel 与 `thread_ts`）；② `DM:` 前缀直接拒绝；③ 队列在 drain 时**重新校验**（防手工写 `comment-retry-queue.json`）。best-effort 直接发；`required` 入队 + 退避 + 耗尽记录；重复入队按 (destination, body, sender) 去重。
- **脱敏（发往 Slack 的正文）**：>2048 字符、含路径、log dump、裸 40 位 SHA、敏感赋值 → 标 reason 并替换；reason 只作提示，不替代"不要贴原始敏感证据"的判断。

失败模式/反例：

- 用 Andon 表达单任务卡住 → 整棵树停摆；应走 `Status: blocked` handoff。
- raise 不带 reason → 子树不知道为何停。
- 子代理直连 Slack 而不是读 root 缓存 → 权限/噪音/状态分裂。
- 靠环境变量或 HOME 覆盖进入操作者模式 → 越权（测试明确覆盖这两种伪造）。
- 只校验写入路径不校验 drain → 队列文件被改写后绕过线程约束。
- 把 `redactBody` 当敏感证据总闸 → 它是"避免把病态正文发到外部通道"的启发式，不等于 custody 策略（与产品 `guide-redacted-evidence.md` 是两层）。

### 3) A–F 判断位点与专业 concern

| 位点 | concern | 何时调用 | 拟供 Profile |
| --- | --- | --- | --- |
| F/D：全局暂停的触发条件与范围 | 安全/程序性 | 继续产出会污染整条链时 | `evidence-evaluation`+`driver` |
| D：操作者模式的身份与最小授权 | 安全/凭据/边界 | 任何"以操作者身份"写外部系统 | `technical-planning` |
| E：脱敏/队列/幂等发送 | 实现/安全 | 写外发通道 | `implementation` |
| F：外发通道的验证 | 安全验证 | 检查泄漏/越权 | `evidence-evaluation` |

### 4) 当前产品锚点、覆盖与缺口

- 已覆盖：`guide-redacted-evidence.md` 的脱敏/custody/HITL、Developer/Driver 路由。
- 缺口：**"全局暂停 vs 单任务卡住"的判定与操作纪律**、**"操作者身份必须来自不可伪造的本地 ownership/权限"**、**外发通道的线程/收件人白名单**、**发外前的最小化/文本启发式**。这些都属 D/E 安全面，产品目前无正文。

为何值得吸收：并行 agent 树最容易出的事故是"只停一个任务却污染全局"或"越权发消息/泄漏"。它可独立于 Cursor/Slack 表述为：单一暂停谓词 + 不可伪造的操作者凭据 + 收件人白名单 + 外发前最小化。

### 5) 拟处置与载体

- 拟保留：Andon 与 blocked-handoff 的边界；reason 必填与长度上限；子节点读缓存不直连外部；操作者身份用本地所有权/权限文件而非环境变量；外发目标白名单 + 二次校验；脱敏启发式。
- 拟改变：Slack→"外部可见通道"；`:rotating_light:`/`🚨` 协议换成"通道级暂停信号"；600 秒/20 条等参数标为来源参数。
- 拟删除：Slack 专属 API、`ORCHESTRATE_*` 命名、Cursor 代理链接。
- 载体落点：可在 `guide-redacted-evidence.md` 增"外发前最小化与目标白名单"一节，或独立 on-demand guide `external-write-boundary.md`；Driver 侧加"全局暂停 vs 局部 blocked"的判定一行。
- 仍依赖 runtime：真实外部通道（Slack/邮件/工单）与 OS 权限模型；没有真实权限模型时，方法只能要求"不要用一个可被伪造的标志宣称操作者身份"。

### 6) 可讨论正文草稿/操作例子 + 验证方案

```markdown
## 全局暂停判定
- 单任务死路 → 交接里写 blocked，树继续。
- 只有"继续分发会批量产出垃圾"（上游结论错、验收标准被证伪、基础设施不可恢复）才触发全局暂停；暂停必须带来原因。
- 暂停只冻结新分发；在跑的任务照常回收。

## 外发边界
- 外发目标必须在本次运行允许的白名单内（线程/收件人/仓库）；写入与重试两侧各校验一次。
- 操作者身份来自不可伪造的本地凭据（文件所有权/权限）；环境变量与可覆盖的 HOME 不作为身份。
- 外发正文先最小化：超长、日志片段、路径、裸哈希、键值凭据先替换/裁剪；替换不等于可以发送原始敏感物。
```

验证方案（**未执行**）：本地 mock 外部通道，分别尝试：环境变量伪造操作者、符号链接标志、把目标改成 DM/别的线程、队列文件手写绕过、正文含 `token=...`/`/Users/...`/裸 SHA。期望：全部拒绝或脱敏，且在运行日志可见原因。边界：不要求真实 Slack；无本地权限模型时本方法只产出"无法保证身份"的告警。

---

## G-04 · 文件库编排：单写者状态、锁、原子写、frontier/ledger

### 1) 机制与触发情境；源锚点与已读/尚缺

触发情境：多个 worker/verifier 经子代理运行，协调者需要可读、可审计、可重入的共享状态（谁在做什么、哪个 PR 验过、哪个人类闸门在等），但不能引入数据库服务或嵌套大框架。

源锚点（pin 内）：

- `pstack/skills/poteto-mode/scripts/orch/store.ts`：类型面（`UNIT_HEADER`/`LEDGER_HEADER`/`LOCK_FILE`；`Verdict` 五值；`Unit`/`LedgerEntry`/`InboxPointer`/`OpenGate|ResolvedGate`/`Frontier`/`StatusSummary`）；`atomicWrite`（同目录 `.name.pid.uuid.tmp`，`wx` 独占创建 + rename + finally rm）；`writeIfMissing`；`acquireLock`（`wx` 创建锁写 PID；EEXIST 时读 holder，`holderIsDead` 数字+PID 存活探测后接管；`force` 显式抢锁；释放前校验锁内 PID == 自己）；`readTsv/writeTsv`；`recordLedger`（按 `pr+sha` upsert）；`checkLedger`（无行抛 NotFound("NOT-VERIFIED")）；`readGates/renderGates`；inbox push/drain（a2r 未读面）；`resolveFrontier`（gt 分支/SHA 解析与 pin 校验）。
- `pstack/skills/poteto-mode/scripts/orch/orch.ts`（签名面）：`--store/ORCH_STORE`、`--repo/ORCH_REPO`、`--json`、`--force`；`frontierLine`、`statusLines`、`leaf` 子命令。
- `pstack/skills/poteto-mode/scripts/check-plan.mjs`（全文）：plan 文档的机器校验（固定 H2/H3 顺序、十个 sub-block 与顺序、`Ten lanes on ... at the PR head`、lane 1–10 且每 lane 必须有截图与 `Pass when`、perf 四项顺序、Review gate 的三种词、长破折号/弯引号/句中冒号、尾部只能 Appendix 且必须有 Prototype evidence）。
- `pstack/skills/poteto-mode/playbooks/orchestrate.md`（前 90 行）：store 布局与"每个文件恰好一个写者"、`units.tsv`/`ledger.tsv`/`inbox/`/`gates.md`/`frontier.json`/`decisions.tsv`/`status.md`（派生）、brief 模板（GOAL/SCOPE/CONTEXT/ACCEPTANCE/VERIFY/TIMEBOX/FORBIDDEN/REPORT/STANDING）、"补不上字段就是还没界定清楚的单元"、"Never resume-chain a brief"、rolling window（约十个 in-flight）、pilot 先跑通一个单元再 fan-out。
- `pstack/skills/poteto-mode/scripts/orch/orch.test.ts`（标题级，现已核实含：`initializes an idempotent plain-file store and releases its lock`；`replaces a stale lock whose holder pid is dead`；`blocks a writer and steals the pid lock only with force`；`rejects malformed TSV, verdict, frontier, and inbox data`）。

已读：上述；尚缺：`store.ts` 的 inbox/gates/frontier 全实现与测试正文、`orch.ts` 全文、`check-plan.mjs` 之外的多阶段计划正文其余段。

### 2) 操作、成立条件、失败模式、反例/例子

- **单写者 + 派生文件**：每个文件恰好一个写者；`status.md` 由 `units.tsv`+`ledger.tsv` 派生，不手工维护；`decisions.tsv` 只 append。`frontier.json` 是计算对象，不是叙述。
- **原子写**：临时文件与被写文件同目录、`wx` 独占创建、`rename` 替换、finally 清理；写缺失语义（`writeIfMissing`）用于幂等初始化。TSV 有显式表头常量；cell 清洗（去 tab/换行）与必填校验。
- **锁**：锁文件写 PID；`EEXIST` 时探活；死 PID 自动接管；活 PID 必须 `--force` 才抢；释放前核对 PID 归属（防误删他人的锁）。测试标题级证据：`replaces a stale lock whose holder pid is dead`、`blocks a writer and steals the pid lock only with force`；另有 `rejects malformed TSV, verdict, frontier, and inbox data` 与 `initializes an idempotent plain-file store and releases its lock`。
- **ledger 语义**：`pr+sha` 唯一键 upsert；查不到抛"NOT-VERIFIED"（显式非通过态）；五值 verdict。与 orchestrate playbook 的规则一致：**新 head SHA 作废该行**，CI 绿是输入不是 verdict。
- **gates**：`OpenGate{question,options,defaultAnswer}` → `ResolvedGate{answer}`；默认答案使"无人回答"也可推进；gates.md 有严格解析（重复 id/非法 status 报错）。
- **check-plan 是"把评审规则编码成脚本"的样例**：源文 `multi-phase-plan.md` 第 6 步要求跑 `check-plan.mjs` 并修掉每行；脚本把"测试不够、必须有 unit/live/perf 三格"、"live 必须十条车道且每条有截图与通过谓词"、"perf 四项"等从口诀变成可执行失败。这同时是 `principle-encode-lessons-in-structure` 与 `principle-build-the-lever` 的实证。

失败模式/反例：

- 两个 worker 各自写同一个 `state.json` 的字段（原则文明确说这仍是共享突变）；应按文件/键/分支拆分。
- 用锁当默认答案而不先判断共享是否必要（原则文的 smell）。
- 先写"当前状态"叙述、再让表格追平 → 派生文件腐化。
- 锁释放不校验归属：旧进程被接管后仍可能删掉新锁。
- ledger 只有"验过"没有"未验证"行 → 无法区分"没验"与"验失败"。
- plan 检查只做人工 review → 规则会漂；但脚本只检格式，不证明内容正确。

### 3) A–F 判断位点与专业 concern

| 位点 | concern | 何时调用 | 拟供 Profile |
| --- | --- | --- | --- |
| D：单写者状态设计与派生规则 | 接口/持久化/并发 | 多实例共享状态 | `technical-planning` |
| E：原子写/锁/TSV 边界校验 | 实现/崩溃安全 | 实现落盘与协调工具 | `implementation` |
| F：ledger 的"未验证"区分与作废规则 | 证据/版本 | 判断"这个版本验过吗" | `evidence-evaluation` |
| Driver：写集与集成 | 程序性 | 多写者集成 | `driver` |

### 4) 当前产品锚点、覆盖与缺口

- 已覆盖：ABC2 MG-5 已提出"先分离再串行/幂等三问/指令不是并发控制"的**判断**；`profiles/driver.md` 有"共享文件是否单写者串行集成"。
- 缺口：**实现面完全未落**——原子写手法、锁的归属与陈旧接管、`pr+sha` ledger 与"NOT-VERIFIED"、派生状态不可手改、把规则编码成脚本的样例。产品还明确说"runtime 机制不属本包职责"，因此本组建议只吸收**判断 + 最小操作纪律**，不引入锁实现。

为何值得吸收：这是"并行工作不互相覆盖"从口号变成可检查行为的唯一路径；`check-plan.mjs` 是一个可复制的"把质量规则变成可执行失败"的最小样例（非框架）。

### 5) 拟处置与载体

- 拟保留（判断层）：单写者 per file、派生文件不手改、ledger 必须有"未验证"态、新版本作废旧 verdict、把重复规则编码成可执行检查。
- 拟改变：TSV/JSON/锁文件/`wx` 等作为**实现例子**并标注"由 D/E 决定"；`NOT-VERIFIED` 的出口形式可换成任务自身记账。
- 拟删除：`orch` CLI 名、gt 依赖、Cursor store 路径。
- 载体落点：ABC2 MG-5 若落地为窄规则，本组实现细节并入其附例；`principle-encode-lessons-in-structure` 已提出（ABC2 MG-3 邻接），本包只补"可执行检查样例"。
- 仍依赖 runtime：真实文件系统语义（rename 原子性）、进程探活、git/forge 的 frontier 来源；没有这些时不得声称 provenance。

### 6) 可讨论正文草稿/操作例子 + 验证方案

```markdown
## 共享协调文件的最小纪律
- 每个协调文件恰有一个写者；汇总页由源表派生，禁止手改。
- 写入用"同目录临时文件 + 原子替换"；不允许直接覆盖。
- 需要互斥时：锁记录持有者；持有者失活才可接管；活持有者必须显式批准才抢；释放前核对归属。
- 验证台账键 = 对象 + 版本（如 PR + head SHA）；没有行 = 未验证，不是通过；新版本使旧结论失效。
- 每次重复写同一句人工指令，就问它能不能变成脚本/检查；能则编码并删除指令。
```

验证方案（**未执行**）：对本地实现做四组：① 并发两个写者 → 单写者约束被观察到（后写者失败或等待）；② kill -9 持锁进程 → 下一次运行自动接管且释放归属正确；③ 台账缺行 → 查询应得"未验证"而非空/通过；④ 故意写坏 plan 文档（缺 lane 截图/缺 perf 项/长破折号）→ checker 退出非零并逐行给出位置。边界：checker 只证明结构，不证明内容；不要求所有项目使用 TSV。

---

## G-05 · PR/CI 判定状态机与查询失败分类

### 1) 机制与触发情境；源锚点与已读/尚缺

触发情境：无人值守或半自动地把 PR 带到 merge-ready；需要"到底能不能合"的单一判定，而不是把 CI 绿、评论已回、GitHub mergeState 混成一锅；查询会间歇失败/限流。

源锚点（pin 内）：

- `pstack/skills/poteto-mode/scripts/watch-pr/types.ts`（全文）：`PrNumber` brand 与 `parsePrNumber`；`PullRequestFacts`/`ReviewThread`/`Check`（五 kind，含 `code-review-gate`）；`GitHubMergeAllowed|Refused`（`BLOCKED`+`ERROR|FAILURE` → refused；`BLOCKED`+其他 → allowed basis=rollup；非 BLOCKED → allowed basis=merge-state）；`CiState` 四态；`ReadyPr.proof`（mergeability clear、threads 空、ci-clean、gate open）；`MergeBlocker` 四类；`QueryFailure` 五类（json-parse/missing-key/command-exit/checks-unavailable/invalid-context-url，前四可重试）；`WaitingDecision`（frontier 与 pending 只属 frontier）；`WatcherVerdict` 的 progress/terminal 划分与 **exit code 0/2/3/4/5/6/7**；`QueueState`/`QueueWork`。
- `pstack/skills/poteto-mode/scripts/watch-pr/policy.ts`（1–520 行）：`assessGitHubMerge`、`readSnapshot`（check 分类、`AUTOMATION_TOKENS` 识别 review automation、`pendingHistory omit` 快路径）、阻断优先级 `conflict → thread → ci → gate`；`classifyPr`；`selectTierMajorStackDecision`；`queryBackoffSeconds = min(max(interval,60)*2^(failures-1),300)`；`pollUntilTerminal`（可重试失败→RETRY+退避，达到 `maxQueryErrors`→exit 7；deadline→TIMEOUT exit 5）；`runSimple`/`runQueued` 的 verdict 覆盖。
- `pstack/skills/poteto-mode/scripts/watch-pr/github.ts`（选段）：`REVIEW_THREADS_QUERY`/`PR_COMMIT_STATUS_QUERY`/`PR_CHECK_ROLLUP_QUERY`、`WatcherQueryError`/`ChecksUnavailable`、`mapRollupNode`（CheckRun/StatusContext 归一；`Code Review Gate` 永不计 pending——"把人工批准门当 pending 会让 watcher 等一个人"）、`resolveChecks`（先 `gh pr checks` fast path，接受退出码 0/1/8 的 JSON；失败再 GraphQL 分页 rollup；都空才抛 `ChecksUnavailable`）、`resolveContext`、`orderStack`/`discoverStack`（按 base/head 链与 PR 号排序）。
- `pstack/skills/poteto-mode/playbooks/{babysit,shipping}.md`：watcher 的消费方式（`check/--status-only`；GitHub 模式 stop 条件）、"CI green is not a verdict"、"approving bot review is not a verdict"、patch-id 规则（G-11）。
- 测试（标题级）：`policy.test.ts`、`github.test.ts`、`cli.test.ts`、`types.compile.ts`。

已读：上述；尚缺：`render.ts`/`cli.ts` 正文、`policy.ts` 520 行以后（队列实现）、测试正文。

### 2) 操作、成立条件、失败模式、反例/例子

- **单一 verdict + 退出码契约**：progress（STATUS/WAITING/ADVANCE/RETRY/QUEUE，exit 不定义）与 terminal（READY/COMPLETE=0；BLOCKER=2/3/4/6/7 按类；TIMEOUT=5）。调用方用退出码分类，不用文本猜。
- **阻断优先级是分层而非集合**：先 conflicts（2），再 review threads（3），再 failing checks（4），再 merge gate（6）；stack 模式为"tier-major"（同一层扫全 stack，再进下一层）。`ReadyPr.proof` 是四条同时满足的证据结构，而不是一个布尔。
- **merge 判定双源**：`mergeStateStatus==BLOCKED` 但 head rollup 非 ERROR/FAILURE → allowed(basis=rollup)；`BLOCKED`+`ERROR|FAILURE` → refused；这解决"GitHub 因 required check 未报而 BLOCKED、但该 PR 的 rollup 其实已过"的误判。`hadPreviousPassingCi` 提供历史通过信息。
- **人工批准门不计 pending（单点规则）**：`Code Review Gate` 无论两读路径都归 `code-review-gate` kind，不阻塞等待人类。
- **查询鲁棒性**：fast path → GraphQL 分页；`gh pr checks` 退出码 1/8 仍可能带有效 JSON；解析器对缺键/类型错/命令失败给出**可重试分类**；指数退避（60s 起、300s 封顶）；超限 → exit 7 而不是永远 RETRY。
- **pending 归因**：`WaitingDecision.frontier` 指向最低未合且实际在等的 PR，pending 仅该 PR 的 checks；upstack pending 不算 frontier 的阻断（queued 模式另有契约）。`reviewAutomationRunning` 单独标注，防止把机器人评审当人类阻塞。

失败模式/反例：

- 把"CI 绿 + 评论已回"直接当可合并（本组给出四条件证据结构）。
- 把人工批准门当 pending → watcher 永远等一个人（源代码注释记录了该缺陷的历史）。
- 查询失败即判 BLOCKER → 噪声；应区分可重试失败与真正阻断，并给 TIMEOUT 单独语义。
- 混合数据源（部分 fast path、部分 rollup）会得到不一致的 check 视图；`source` 字段显式标注。
- `BLOCKED` 一律当失败 → 大量假阻断。
- 只看单个 PR 的 pending 而把 upstack 等待记到 frontier 上 → 归因错误。

### 3) A–F 判断位点与专业 concern

| 位点 | concern | 何时调用 | 拟供 Profile |
| --- | --- | --- | --- |
| D：判定状态机与退出码契约 | 接口/可运维性 | 设计自动判定器 | `technical-planning` |
| F：证据条件（四条件 proof）与失败分类 | 验证/证据 | 判断"可合并/可交付" | `evidence-evaluation` |
| E：查询鲁棒/退避/分页 | 实现/可靠性 | 实现 watcher | `implementation` |

### 4) 当前产品锚点、覆盖与缺口

- 已覆盖：`behavior-claim-evaluation.md` 的 claim/对象/版本/比较；`evidence-evaluation.md` 的"三态与负控制"。
- 缺口：**多信号条件的判定结构**（何时算 ready，作为条件组合而非印象）、**退出码/失败分类契约**、**查询失败与产品失败分离**、**人工门不能被当 pending**。产品目前没有 CI/PR/队列类方法。

为何值得吸收：产品的方法面向"某个 claim 是否成立"，但真实交付里常见"多项检查 + 人类门 + 间歇查询失败"的组合判定；本组提供可复制的**判定代数**（阻塞分级 + 证据结构 + 可重试分类）。

### 5) 拟处置与载体

- 拟保留：terminal/progress 分离与退出码分类；阻断分级；`ReadyPr.proof` 式条件组合；人工门不计 pending；查询失败的可重试分类 + 退避 + 超限退出；数据源标注。
- 拟改变：GitHub/gh/GraphQL 字段名 → "宿主 forge 的等价事实"；exit code 具体值标来源参数。
- 拟删除：Slack/PR/gt 机制、Cursor 特定。
- 载体落点：可作为 `behavior-claim-evaluation.md` 的"组合判定的证据结构"扩展，或 on-demand `gate-verdict.md`；`profiles/evidence-evaluation.md` 关键问题补"这是一个判定还是多个条件的组合，未满足的到底是哪一条"。
- 仍依赖 runtime：真实 forge/CI 查询与限流语义；没有真实访问时只能定义判定结构，不能给 PASS。

### 6) 可讨论正文草稿/操作例子 + 验证方案

```markdown
## 组合判定（以"可合并"为例）
判定 = 冲突无 ∧ 无未解决评审线程 ∧ 检查无失败 ∧ 门是开的。
每一条单独取数并保留来源；"门是开" = 非草案/未要求变更（人工批准另行标注，不折算成检查）。
阻塞按优先级报一个主因（冲突 > 线程 > 检查 > 门），不要把所有问题混成一句"未就绪"。
查询失败是观察失败：可重试→退避重试；超过上限→"无法判定"，不是"不通过"。
```

验证方案（**未执行**）：用 mock reader 构造 8 个快照：仅全绿；BLOCKED+FAILURE；BLOCKED+SUCCESS；CONFLICTING；有线程；changes-requested；人工门 pending；查询连续失败。期望：前两类 refuse/allow 语义正确，第三类 allowed(rollup)，四/五/六给对应 blocker 与退出码，七不阻塞，八走 RETRY→上限后"无法判定"。边界：不要求真实 GitHub；无 forge 时只能做判定结构演练。

---

## G-06 · worktree 审计与安全回收

### 1) 机制与触发情境；源锚点与已读/尚缺

触发情境：并行写者为隔离各自 worktree，长期积累后磁盘告急；需要清理但不能删在用的、不能删未提交的。

源锚点（pin 内）：

- `pstack/skills/poteto-mode/scripts/worktree-audit.sh`（全文）：`git worktree list --porcelain` 取路径；`du -sh`；逐 worktree 取 HEAD 与提交时间；`git merge-base --is-ancestor origin/main` 判 merged；`git status --porcelain` 区分 `wip:N`（tracked 改动）与 `scratch:N`（仅 untracked）；remote 状态（pushed/ahead/no-remote/detached）；`gh pr list --author @me --state all --json number,state,headRefName` 一次取 PR，用 `jq` 匹配 branch；transcripts 目录按 repo 路径 slug 映射，按 "路径后跟 `/` 或引号" 精确匹配（防 `glint-482` 命中 `glint-482-r37`），取最近 mtime 的聊天日期；bucket 规则：`hold-wip` > `hold-open-pr` > `verify-recent-chat`（4 天内聊过）> `safe`（merged 或有 PR）> `review`；输出按 size 降序；只读、绝不删除。
- `pstack/skills/poteto-mode/playbooks/worktree-cleanup.md`（全文）：`df -h` 前后；bucket 只是建议不是许可；**pinned/active chats 是真凭据**，以用户/侧边栏集合为准；对 `verify-recent-chat` 或可疑项 fan 子代理读 transcript 判是否 pinned/进行中；`wip:N` 必须展示 diff 并取得决定（clean worktree 可从 branch 恢复，uncommitted 不能）；`scratch:N` 可丢但要列出文件；`git worktree remove --force` 后若目录因 ignored 构建产物残留再 `rm -rf` + `git worktree prune`；branch ref 存活所以不丢 commit；最后再 `df -h` 与重新 list；模拟器与缓存清理选项。

已读：两份全文；尚缺：无（脚本未执行）。

### 2) 操作、成立条件、失败模式、反例/例子

- **读-only 分类先行，删除是独立的人工/授权步**；脚本从不删。
- **squash-merge 不是 ancestor**：`merge-base --is-ancestor` 只能证明 fast-forward/rebase 合并；squash 合并必须靠 PR 状态；两者合判。
- **WIP vs scratch 区分**：tracked 改动 = 真实未保存工作；仅 `??` = 可丢弃草稿。这是删除安全门的核心反例来源。
- **bucket 是建议**：源文给了一句实测反例——lever 把用户 pinned 的 worktree 标成 `safe`；因此 pinned 集合覆盖 bucket。
- **transcript 边界**：按路径+分隔符匹配，避免前缀误命中；且 transcript 只作辅助证据，不替代用户可见的 pinned/active 集合。
- **删除后确认**：`--force` 删目录、`prune` 清元数据、`df -h` 对比；branch ref 保留是"可恢复"的依据。

失败模式/反例：

- 按进程名 kill 或按目录名猜 → 删掉在用 worktree。
- 只看 merged 一列 → squash 合并全被当未合并（保留垃圾）或反之（如果误判）。
- 把 untracked 文件当可删但其中含未保存产物（应列给用户）。
- bucket=`safe` 直接执行删除 → 源文实测会删掉 pinned 环境。
- 删除前不显示 `wip` diff → 丢失无法从 git 恢复的工作。

### 3) A–F 判断位点与专业 concern

| 位点 | concern | 何时调用 | 拟供 Profile |
| --- | --- | --- | --- |
| D/E：隔离与回收生命周期 | 资源/安全/可恢复 | 并行写者积累/磁盘压力 | `technical-planning`+`implementation` |
| F：删除前的使用证据与恢复依据 | 证据/不可逆 | 任何删除动作前 | `evidence-evaluation` |
| Driver：授权门 | 程序性 | 不可逆动作 | `driver` |

### 4) 当前产品锚点、覆盖与缺口

- 已覆盖：`profiles/driver.md` 的写集/单写者；ABC2 MG-5 的共享状态拆分。
- 缺口：**不可逆回收的判定程序**——只读审计、squash 合并的特殊性、WIP/scratch 区分、pinned 覆盖 bucket、"branch ref 存活"作为恢复依据。产品完全没有回收/清理面。

为何值得吸收：这是"并行隔离"的下游成本与安全边界；方法可独立于 git/Cursor 表述为"先分类证据、再独立授权删除、保留 ref 作为回退"。

### 5) 拟处置与载体

- 拟保留：读-only 审计 + 分类 + 人工/授权门；squash 反例；WIP/scratch 区分；真实使用证据优先于启发式打分；删除后复核。
- 拟改变：`git worktree`/`gh`/`du` 作为实现例子；"4 天/最近聊天"标为来源参数。
- 拟删除：模拟器/缓存清理等 host 专属（可留作环境例子）。
- 载体落点：on-demand guide（如 `workspace-reclaim.md`）或并入 `implementation.md` 的按需入口；不宜进 Backbone。
- 仍依赖 runtime：真实 git、磁盘、外部 PR 状态；无这些时只能做"列出候选 + 请人类判断"。

### 6) 可讨论正文草稿/操作例子 + 验证方案

```markdown
## 回收判定（操作）
1. 先记录空间基线；只读枚举候选（隔离目录 + 大小 + 年龄 + 合并状态 + 未提交状态 + 外部关联）。
2. 合并状态不能只看 ancestor：squash/rebase 合并要以外部 PR 状态为准，两法合判。
3. 未提交分两类：tracked 改动（需展示 diff 并取得决定）与 untracked 草稿（可丢但逐一列名）。
4. 自动分类只是建议；用户 pin/活跃集合是权威，任何冲突以用户集合为准。
5. 删除后复核空间与列表；保留分支引用作为恢复依据；删除动作本身需独立授权。
```

验证方案（**未执行**）：构造一个含 6 个 worktree 的本地 repo：干净且已合并、squash 合并、untracked 草稿、tracked WIP、pinned 活跃、detached。期望：脚本给出正确 bucket；人为把 pinned 标 safe 时人工流程仍以用户集合拦住；删除 tracked WIP 前必须出现 diff。边界：脚本只读；删除授权不在方法层。

---

## G-07 · 回合钩子与自主循环实现

### 1) 机制与触发情境；源锚点与已读/尚缺

触发情境：宿主支持"回合结束/文件编辑/子代理结束"事件；需要在回合边界加低价提醒、把同一提示循环喂回直到完成条件、或按轮次/时长节奏触发记忆更新。

源锚点（pin 内）：

- advisor：`hooks/hooks.json`（afterFileEdit/afterAgentResponse/subagentStop(matcher)/stop(`loop_limit:3`)）、`hooks/lib.sh`（`advisor_require_enabled` 先 jq 与 state 检查；`advisor_state_update` 用 jq 写临时文件再 `mv`；`advisor_bind_conversation` 首个会话绑定、换会话拒绝、重绑清 marker）、`capture-response.sh`（tail 400 字符）、`mark-pending.sh`（排除自身状态目录）、`record-consult.sh`（只认 `advisor-subagent`+completed；计数 + 清 pending + 追加 log）、`stop-hook.sh`（只 completed；`nudge` 开关；pending 存在；末字符 `?` 则静默保留 marker；输出 `followup_message`）。
- ralph-loop：`hooks/hooks.json`（`loop_limit: null`）、`capture-response.sh`（从 state 文件 frontmatter 读 completion promise；perl 提取 `<promise>…</promise>`；精确匹配才 `touch done`）、`stop-hook.sh`（无 state→放行；非数字 iteration/max → 报错并清 state；done→报完成并清；上限→报上限并清；取第二 `---` 后文本；原子改 iteration；构造 followup 头含"ONLY when genuinely true"）、`skills/{ralph-loop,cancel-ralph}/SKILL.md`、`README.md`（适用/不适用、写 prompt 的建议、始终设上限）。
- continual-learning：`hooks/hooks.json`、`hooks/continual-learning-stop.ts`（state JSON 版本+类型校验；`generation_id` 去重；`countedTurn = status==="completed" && loop_count===0`；turns+minutes+transcript mtime 三重条件；trial 模式阈值；每文件增量索引；触发时返回固定 `followup_message`，只在 `shouldTrigger` 时更新 lastRun/turns/mtime；异常时打印错误并返回 `{}`，**不阻断回合**）。

已读：上述全部（a2r 只读了 advisor stop-hook 与 ralph stop-hook）；尚缺：三个插件的 skills/agents 正文（advisor SKILL 由 a2r 读过）、`ralph-loop/skills/ralph-loop-help`（不存在？README 提及但索引仅两 skill）。

### 2) 操作、成立条件、失败模式、反例/例子

- **标记-提醒-清标记**是回环的基本形状：文件编辑记 pending；回合结束时若有 pending 且（可选的）最后一次回复不是问句，就发一次提醒并把 pending 清掉；loop_limit 限制重复次数；提醒文本直接给出下一步动作与模型名，不让读者自己推断。
- **问题检测**：末字符 `?` 作为"在等人类回答"的廉价启发式（并保留 marker 以便人类回答后再提醒）；这是启发式而非语义判断，误判代价是少提醒/多提醒一次。
- **完成承诺不可被模型轻易伪造**：仅在输出中出现与配置完全一致的 `<promise>TEXT</promise>` 才置 done；停止钩子同时受 max_iterations 保护；prompt 明确"只在真正完成时输出"。
- **损坏状态保护**：iteration/max 非数字 → 报错、清理、停止（不把坏状态当无限循环）；状态写入用临时文件 + mv。
- **节奏触发**：轮次 + 时长 + transcript 前进三重条件，避免"同一内容反复触发"；generation 去重防同回合重放；触发信息里给固定的 follow-up 指令（含增量索引路径），不靠模型记忆；**出错时 fail-open**（返回 `{}`）而不是让主流程中断。
- **会话绑定**：第一个接触状态的会话成为属主，其他会话直接退出；重绑清空 marker，避免继承上次的 pending。

失败模式/反例：

- stop hook 输出 followup 但宿主 `loop_limit=null` → 无上限自转（ralph 的 README 明确"始终设 max_iterations"）。
- 用"回复里有 question mark"当语义判断 → 代码块/URL 里的 `?` 会误判。
- 提醒钩子无 pending 清理 → 每回合重复提醒；无 loop_limit → 无限提醒。
- 状态损坏（非数字）继续解析 → 循环失控或崩在 hook 里；正确行为是清理并停止。
- 记忆更新钩子同步写 state 且异常上抛 → 阻断回合；实现选择 fail-open。
- 在 summary/self-report 上判断完成 → 与 G-02 同源反例；这里用显式 promise 且仍受上限约束。

### 3) A–F 判断位点与专业 concern

| 位点 | concern | 何时调用 | 拟供 Profile |
| --- | --- | --- | --- |
| E：hook 状态与幂等写 | 实现/持久化 | 实现回环/提醒 | `implementation` |
| F：完成条件的可观察形式 | 验证 | 定义"何时算完" | `evidence-evaluation` |
| Driver：循环边界与取消 | 程序性 | 设上限/取消/节奏 | `driver` |

### 4) 当前产品锚点、覆盖与缺口

- 已覆盖：`autonomous-run` 的"先写 predicate"（a2r MG-8 已转述）；`pause-safely`；产品 Backbone §4 Driver 的关闭判断。
- 缺口（实现层）：**标记/提醒/清标记的回环协议**、**完成 promise 的伪造防护与上限**、**状态损坏时 fail-stop**、**节奏触发去重与 fail-open**、**会话绑定**。产品没有 hook/回环方法，且不应把 host hook API 当规范。

为何值得吸收：任何"回合边界自动提醒/自动继续"的能力都需要这组安全阀；它决定无人值守是"可控回环"还是"token 失控"。

### 5) 拟处置与载体

- 拟保留：pending 标记 + 至多一次提醒 + 清理 marker；问题检测作为启发式标注；完成 promise 精确匹配；上限与取消；坏状态清理停止；节奏三重条件 + generation 去重；钩子 fail-open。
- 拟改变：hook JSON 字段名/命令路径 → "宿主提供的回合事件"；`loop_limit` 数字标为来源参数。
- 拟删除：Cursor/`.cursor/ralph|advisor` 路径、具体模型名。
- 载体落点：on-demand guide `turn-loop-guardrails.md`，或作为 G-11 无人值守方法的一节；`profiles/implementation.md` 按需入口一行。
- 仍依赖 runtime：真实 hook 事件与状态目录；没有 hook 支持时本方法只剩"上限 + predicate"，不能自动继续。

### 6) 可讨论正文草稿/操作例子 + 验证方案

```markdown
## 回合回环安全阀（操作）
- 需要继续时，状态必须外置（轮次、上限、完成谓词、原始提示）；不靠会话记忆。
- 完成信号必须是显式可匹配的标记，且仍受硬上限约束；提醒文本写明"只在真正完成时"。
- 状态解析失败 = 停止并清理，不是继续。
- 提醒唯一：有未处理标记才提醒；提醒后清标记；重复提醒有自己的上限。
- 结束时若在等人类（启发式：末字符问号），保留标记但不提醒。
- 节奏类钩子：按轮次+时长+输入确实前进三重判断，并记录最后处理点防重放；钩子自身异常不得阻断主流程。
```

验证方案（**未执行**）：mock hook 输入序列：① 无状态 → 放行；② 数字状态 + 未完成 → 递增并回喂；③ 损坏状态 → 清理并退出非阻塞；④ promise 精确匹配 → 清 state 停止；⑤ 上限到达 → 停止；⑥ 带 `?` 结尾 → 不提醒且 marker 保留；⑦ 经济钩子抛异常 → 回合正常结束。边界：不要求宿主支持全部事件；无状态持久化时不得声称可续。

---

## G-08 · 验证面支持文件与 benny 运行契约

### 1) 机制与触发情境；源锚点与已读/尚缺

触发情境：SKILL 级验证方法（a2r MG-5）已有，但把它落地成"可运行、可维护、可失败关闭"的自动化仍缺支持文件：feature map 的逐特性条目、受控适配器契约、既有修复的验证模式，以及外部自动化（Slack 触发）如何失败关闭。

源锚点（pin 内，a2r 未读或未细读）：

- `pstack/skills/create-verification-skill/references/feature-map-example/README.md`（a2r 已读）→ 本包只补 `search.md`（未读）。
- `pstack/automations/benny/skills/reproduce-and-fix-issues/references/control-adapter.md`（全文）：Bring up（返回 session、app 标记、run 细节、缺失能力；必须区分目标 app 与相似窗口/生产实例）、Drive UI（偏好 role/label；坐标须基于新截图；**不得设内部状态/调隐藏方法/直写存储/注入 DOM 制造症状**）、Drive mapped features（状态枚举、reset、双重复现、截图/录像/只读交叉核对；稳定 handle：role、accessible name、ARIA、purpose-named data-attr；禁用生成的 CSS/StyleX/hash/子索引）、Inspect（只读；会改状态的查询归 Drive）、Screenshot（须含 app chrome 证明正确对象）、Recording（须含判别性终态）、Cleanup（不删用户工作；保留策略）、adapter 行为（先报能力；同环境输入用于 baseline/patched；启动失败即失败；有界重试；秘密不进日志/产物；捕获物在仓库外）、环境翻译（把带平台名词的缺陷重述为行为，可翻译时标 translated evidence，不得当 exact repro）、Setup check 九步才启用。
- `.../verify-existing-fix.md`（全文）：只接受具体工件（PR/merged commit）；工作树隔离；baseline（PR 的 base / 合并前版本）跑两遍必须复现，否则"没有 baseline，不得声称修复有效"；patched 同环境同 UI 路径跑两遍；三种结局 Confirmed/Insufficient/Inconclusive 的操作与"no competing PR"。
- `pstack/automations/benny/FOR_AGENTS.md`（全文）：人类写给安装代理的意图文件；merge 进目标 repo 且**保留 destination-only 文件、不覆盖用户配置**；用户配置/feature map/routing/secret 放在 pack 外；两自动化的输入/输出/边界（"exactly one reply in source thread"、"never post a root message"、"draft PR only"、"utility/debug bots are evidence not delegation"）；commit 后才启用；先 draft review 再交 automation editor。
- `pstack/automations/benny/templates/configuration.example.yaml`（全文）：schema_version、slack/repository/tracker/routing/control/budgets/models 分节；`allowed: false` 类边界（`allow_source_root_posts: false`、`allow_worker_slack_writes: false`、`draft_only: true`）；预算（poll 45s、verdict wait 45m、repro 60m、fix 90m…）；artifact retention 24h。
- `cursor-team-kit/skills/{control-ui,control-cli}/SKILL.md`（全文）：真实浏览器/CDP 与 tmux/PTY harness；优先 repo 既有 harness；确定性等待优于 sleep；不按进程名 kill、不留 credential/破坏性命令；页面选择用正向标记。
- `pstack/docs/guide/06-verify-and-ship.md`（a2r 已读，本包只用其 finish-condition 表述）。

已读：上述；尚缺：`feature-map-example/search.md`、benny `setup-benny`/`triage-issue-reports`/`reproduce-and-fix-issues` 三个 SKILL 正文、`templates/{triage,reproduce}-automation-prompt.md`、routing example、benny feature-map example。

### 2) 操作、成立条件、失败模式、反例/例子

- **适配器能力先声明再驱动**：Bring up 返回"如何确认是正确 app/环境"与"缺失能力"；Setup check 九步全过才允许启用；后续任何步骤失败 → fail closed（不降级为"看起来像成功"）。
- **证据含动作与状态**：截图必须有 app chrome；录像必须含判别性终态；mutation 证明要有只读第二视图；UI 用 ARIA snapshot + 带标识截图；CLI 用 command/stdout/stderr/exit code。
- **禁止制造症状**：不能用内部 setter/直写存储/注入 DOM 来"产生报告的症状"；precondition 可以布置，症状必须来自真实用户动作。
- **既有修复的验证模式**：baseline 两遍复现 + patched 两遍消除；只认具体工件；"baseline 不复现就没有 baseline"；不编辑/不竞争 PR；三种结局各自的输出与"source thread 何时说话"。
- **配置边界默认 false/only**：不许可的根消息、worker 写 Slack、非 draft PR 都显式关；预算与保留期显式；秘密不进 pack、不进日志。
- **安装/合并纪律**：保留目标侧文件、冲突时停止询问、验证共享依赖在"目标仓库根的 fresh agent"里解析（不数当前会话的加载）、commit 后才启用。

失败模式/反例：

- 用 test-only endpoint 或内部写库证明用户路径（源文明确禁止）。
- 把 dry-run 的名字当证据（a2r MG-5 已转述；本包提供"观察跳过什么"的清单：文件、网络、git refs）。
- cleanup 删掉证据或按进程名杀；证据得活过 cleanup 且被检查。
- 只有一次复现就宣称修复有效；或 patched 只看编译/测试。
- 环境翻译后当 exact repro（必须标 translated，且缺失环境本身是缺陷时不得替代）。
- 未执行过的生成 skill 当交付（a2r 已记）；本包补 adapter 侧的同类门槛（Setup check 九步）。

### 3) A–F 判断位点与专业 concern

| 位点 | concern | 何时调用 | 拟供 Profile |
| --- | --- | --- | --- |
| F：证据结构（动作+状态、第二视图、双复现） | 验证/证据/环境 | 任何"证明行为"的任务 | `evidence-evaluation` |
| D：适配器接口与失败关闭 | 接口/边界 | 跑真实 app/UI/CLI | `technical-planning` |
| E：harness 实现与清理 | 实现 | 写驱动脚本 | `implementation` |
| B：用户路径/入口定义 | 行为/交互 | 定义 feature map/用户 POV | `behavior-domain` |

### 4) 当前产品锚点、覆盖与缺口

- 已覆盖：a2r 已把 SKILL 层五段与三不变量拟入方法；产品现有 `behavior-claim-evaluation.md`/`guide-mock-adapter-choice.md`/`guide-redacted-evidence.md`。
- 缺口（本包独有）：**适配器契约**（能力声明、正确 app 识别、fail closed、环境翻译）、**证据双复现模式**、**配置默认关闭的边界**、**安装/合并纪律**。这些让"验证面"从文档变成外接自动化可用的契约。

为何值得吸收：把"验证"从一次性人工变成可交给自动化的运行面时，真正的风险在适配器边界与失败关闭，而不是在 SKILL 步骤。

### 5) 拟处置与载体

- 拟保留：adapter 能力声明 + 九步 setup check；禁止内部状态制造症状；证据要求（chrome、终态、只读交叉、双复现）；baseline 双复现；环境翻译与标注；配置默认关边界；安装保留目标文件。
- 拟改变：Slack/PR/LINEAR 等具体系统 → "外部触发器/工单/代码宿主"；`/automate`、Cursor editor 步骤删除。
- 拟删除：benny 命名与目录、具体预算数字（保留"预算必须显式"）。
- 载体落点：可作为 a2r 拟建验证方法的**支持章节**（若 gate 采纳），或 on-demand guide；`methods/README.md` 按需表加一行；不要新建框架。
- 仍依赖 runtime：真实浏览器/CDP/PTY/HTTP、截图/录像、外部 tracker/Slack、凭证管理；方法层只能定义契约与证据标准。

### 6) 可讨论正文草稿/操作例子 + 验证方案

```markdown
## 适配器契约（摘要）
- 开跑前报告能力与不可驱动部分；缺能力 → 失败关闭。
- bring-up 必须给出"如何确认这是目标版本与环境"的稳定标记。
- 驱动只做真实用户动作；安排前置状态可以，注入症状不行。
- 每次驱动返回动作与观察到的状态变化；检视只读。
- 证据：真实用户路径 + 动作/结果状态 + 副作用（文件/行/消息）+ 只读交叉视图；截图带应用标识；录像含判别终态。
- 失败/中断也要清理；清理不得删证据，也不得按进程名乱杀。
```

验证方案（**未执行**）：做一个最小 app 与两个 adapter（一个合规、一个故意返回"成功"但没驱动真实路径），检查流程能否在证据层发现差异；再注入一个"dry-run 其实仍开浏览器"的假安全路径，确认观察清单能抓到。边界：不要求所有项目写 adapter；无法隔离环境时方法只给"不可信/需人工"结论。

---

## G-09 · 历史动机调查与置信度分层

### 1) 机制与触发情境；源锚点与已读/尚缺

触发情境：要回答"这段代码/决定为什么是这样"；证据在提交、PR、工单、聊天、遥测里，且常常缺失或互相矛盾。处理不当会产出"听起来很有道理"的假结论。

源锚点（pin 内）：

- `pstack/skills/why/references/epistemics.md`（全文）：五层置信（Direct/Supported/Inferred/Speculative/Unknown）与各自措辞；"代码不能自证意图"；词表（because/the reason is/was designed to 等须紧邻引用；appears/likely/suggests 用于推断）；避免"obviously/clearly/just/I think"；反理性化（不要为脏历史倒推合理动机；不要用"没人提安全问题"当反证）；谄媚陷阱（用户问题里嵌入的假设只是候选）；矛盾并置；缺失证据作为输出（具体写搜了什么、没找到什么）；定稿前校准四问（引用？措辞配层？拿代码当意图证据？有没有 What We Don't Know？）。
- `pstack/skills/why/references/sources/{incident-postmortem,datadog}.md`（全文）：把"防御性代码"当作跨源事故视角的触发器；多源交叉（Datadog incident ID → Linear → Notion postmortem → Slack → 目标 PR）；Datadog 的"监控阈值常是代码 clamp 的答案"；相关不等于因果；"instrumented != caused"；优先时间窗查询；返回结构（类型/标题/链接/作者/日期/引用/相关性强度）。
- `pstack/skills/why/references/synthesizer-prompt.md`（a2r 已读）→ 本包不重复。
- `pstack/skills/blast-radius/SKILL.md`（全文）："不要相信自己的书面分析"；每项安全假设沿证据阶梯（1 自述 → 2 指到行 → 3 论证不可能 → 4 写脚本跑真实代码 → 5 在运行 app 复现）尽量下走并说明停在哪；找"整个变更只因一个事实而安全"；grep 停之处（第三方库源码、钉住版本与本地补丁、微任务/卸载时序、API 返回、DB 列、wire format、另一语言读同一 bytes、flag、下游三跳）；风险要写可能性与代价，cleared 单列；证明那个事实（脚本/测试）并把输出贴回。

已读：上述；尚缺：`why/SKILL.md`、`investigator-prompt.md`、`sources/{code-archaeology,linear,notion,slack,sentry,databricks}.md`、`how/SKILL.md`。

### 2) 操作、成立条件、失败模式、反例/例子

- **置信分层 + 措辞绑定**是可用于任何"历史/动机"结论的 F 方法：Direct 可写 because，Inferred 只能写 likely/appears；Unknown 要写搜索面。
- **代码不是意图证据**：`why` 的 Direct 只认作者写过的话（PR 描述、工单、注释、设计文档、聊天）。
- **反谄媚**：用户嵌入的假设只当候选，独立验证后再表态。
- **事故视角**：遇到防御性代码（空检查、重试、超时、限流、开关）要专门查事故史；多源交叉形成高置信。
- **遥测的定位**：监控/看板"阈值常是答案"；但 instrumented != caused；时间窗与相邻 PR 必须一起看。
- **影响分析（blast radius）**：不要把"列出调用者"当产物；找那个安全事实并用可运行证据证明；证据阶梯要注明停在哪一级；grep 停住的地方才是高风险区。

失败模式/反例：

- 用"代码看起来是为性能"回答意图问题（层级错用）。
- 把没问题当没问题（absence of evidence）。
- 用"obviously/clearly/I think"包装推断。
- 遇到矛盾只取更顺的一个。
- blast radius 交出一篇"听起来对"的分析，没有运行证据；或只列 callers 就结束。
- 把 Datadog 图当因果；或搜不到就说"没发生过"。

### 3) A–F 判断位点与专业 concern

| 位点 | concern | 何时调用 | 拟供 Profile |
| --- | --- | --- | --- |
| F：历史结论的证据等级与缺口 | 研究/证据 | 回答"为什么/会不会破坏" | `evidence-evaluation` |
| A/B/C：动机归属（目标/承诺/语义） | 目标/行为/领域 | 结论涉及谁的决定时 | 按结论回 `intent-voice`/`behavior-domain` |
| D：影响面与安全事实 | 架构/回归 | 变更前判断爆炸半径 | `technical-planning` |

### 4) 当前产品锚点、覆盖与缺口

- 已覆盖：`local-defect-feedback-loop.md` 的假设纪律、`guide-redacted-evidence.md` 的"状态码不是原因"、`behavior-claim-evaluation.md` 的三态。
- 缺口：**历史证据的置信分层与措辞纪律**、**"代码不是意图证据"**、**缺失证据作为正式输出**、**影响分析的"一个事实 + 证据阶梯"**。产品目前没有研究/影响分析方法正文。

为何值得吸收：这是跨 D/E/F 的高频判断（"为什么这样设计""改动会不会炸"），且可在无外部工具时独立使用；有工具时再补遥测/事故源。

### 5) 拟处置与载体

- 拟保留：五层置信与措辞绑定；代码不自证意图；反谄媚；矛盾并置；未知要写明搜索面；blast-radius 的一段安全事实与证据阶梯；grep 停住处清单。
- 拟改变：Datadog/Linear/Notion/Slack 等具体源 → "可用的一手来源类别"；阈值/时间窗标为例子。
- 拟删除：工具调用命令、MCP 名。
- 载体落点：on-demand `rationale-research.md` + `impact-analysis.md`（或合一）；`profiles/evidence-evaluation.md`/`technical-planning.md` 各加按需入口；`methods/README.md` 对应行。
- 仍依赖 runtime：真实仓库历史、工单/聊天/遥测访问；无外部源时置信上限自动降级并在输出注明。

### 6) 可讨论正文草稿/操作例子 + 验证方案

```markdown
## 历史结论的置信分层（摘要）
- 直接：作者写下的原话（PR/工单/注释/文档/聊天），可写"因为"。
- 有支持：多份间接证据收敛，写"证据指向"并列出。
- 推断：合理读法但无直接支持，写"看起来/可能/与…一致"。
- 猜测：证据薄，写"一种可能是…没有直接证据"。
- 未知：写明搜过什么、找到什么；这是合法输出，不得用自信猜测填补。
- 代码只证明"做了什么"，不证明"为什么"。

## 影响分析（摘要）
- 变更的安全往往依赖一两个事实；先把它们写出来，再沿"自述 < 指到行 < 论证不可能 < 写脚本运行 < 在真实运行中复现"尽量下走，并注明停在哪一级。
- 特别检查 grep 停住处：依赖源码与钉住版本、执行时机/生命周期、数据与线格式、配置开关、下游三跳。
- 已确认风险与已排除项分列；缺运行证据时写 unproven。
```

验证方案（**未执行**）：给一个真实小仓库，选一段防御性代码，按五层各写一条结论并检查措辞是否匹配、是否给出了 Unknown 的搜索面；对一个小 diff 找"安全事实"，写一个能失败的脚本证明它（例如"该调用只丢已死缓存项"），并故意在另一分支注入反例看脚本变红。边界：无外部来源时只做仓库内证据；结论不授权动作。

---

## G-10 · 评审镜头、过滤与重复载体

### 1) 机制与触发情境；源锚点与已读/尚缺

触发情境：拿到一批对抗式评审意见，需要专业过滤（不是聚合）；需要一份攻击性质量评审的镜头的细则；同一评审载体存在多份实现，需要判去重。

源锚点（pin 内）：

- `pstack/skills/interrogate/references/rubric.md` + `lead-judgment.md`（a2r 已读并转述）→ 本包不重复，只在 G-10 的"重复载体"与 a2r 未读件上补充。
- `cursor-team-kit/skills/thermo-nuclear-code-quality-review/SKILL.md`（全文，a2r 已读）→ 本包补"结构判断的三条 presumptive blocker 与 code judo"作为 G-11 的来源，不重复。
- thermos 重复载体：`thermos/skills/thermo-nuclear-code-quality-review/SKILL.md`（12.4KB）与 `cursor-team-kit/skills/thermo-nuclear-code-quality-review/SKILL.md` 同内容；`thermos/skills/{thermo-nuclear-review,thermos}/SKILL.md`、`thermos/agents/*`。本包核对：两份质量 rubric **逐字节一致**——`git hash-object` 均为 `ac76a2bc88bb2d895e83ab1788aa584a82346cfc`。
- `agent-compatibility/README.md`（前 80 行）：评分模型 `round(deterministic*0.7 + workflow*0.3)`、四个 review agents、"scanner 不打包，npx 运行"、启发式声明（"not a full quality verdict"）。
- `pstack/skills/interrogate/references/code-quality-review.md`（a2r 残余；本包**未读**，列尾部）。

已读/尚缺：见上；本组主要是"载体核对 + 归属建议"，不在机制操作上展开（避免与 a2r MG-6 重复）。

### 2) 操作、成立条件、失败模式、反例/例子

- **同一 rubric 两份载体**是明确的漂移面：thermos 与 cursor-team-kit 各带一份质量 rubric；任一被修而不修另一份，评审标准会分叉。核对应做：逐字节比对（例如 `shasum`），并在吸收时选择单一 canonical 载体，或明确"一份是分发副本、只在发布时同步"。
- **评审 agent 声明的可信度**：agent-compatibility 明确"scanner 是启发式、不是质量判决"；它用四路 review 补 workflow 检查，且"accelerator layer 不抬高 deterministic 分"。这与 G-05 的"组合判定"同源：分数是输入之一，不是判决。
- **重复实现不同语义**：`pr-review-canvas` 在两处（cursor-team-kit 的 HTML renderer vs 独立插件的 Canvas）是"同名不同实现"，不是副本；吸收时须按机制分别判，不得按名字合并。

失败模式/反例：按名字判重（误把同名不同实现合并）；只更新一份 rubric；把启发式评分当 verdict；用单一模型评审当独立评价（a2r MG-6 已记）。

### 3) A–F 判断位点与专业 concern

| 位点 | concern | 何时调用 | 拟供 Profile |
| --- | --- | --- | --- |
| F：评审标准与去重 | 质量/独立性 | 采纳评审 rubric 时 | `evidence-evaluation` |
| D/PKG：载体唯一来源 | 维护性 | 多插件分发 | `technical-planning`（辅） |

### 4) 当前产品锚点、覆盖与缺口

- 已覆盖：a2r MG-6 拟议的评审裁决方法；产品 `profiles/evidence-evaluation.md` 的独立性纪律。
- 缺口：**载体唯一性/漂移核对**（工程维护面），以及 `code-quality-review.md` 的未读面。

为何值得吸收：吸收评审标准时必须同时处理"标准有几份、谁是源"，否则落地后必然分叉。

### 5) 拟处置与载体

- 拟保留：同一 rubric 单源；启发式评分单独声明且不与 verdict 混同；同名不同实现分开判。
- 拟删除：双份 rubric 的并行维护。
- 载体落点：随 a2r 的评审方法落地时在 `methods/` 的 source anchors 里声明"单一来源 + 删除重复载体"；本包不另建文件。
- 仍依赖 runtime：无（纯文档维护纪律）。

### 6) 可讨论操作例子 + 验证方案

例子：`shasum` 两份 thermo-nuclear rubric；若一致则标"分发副本"，落地时保留一份；若不一致则逐节 diff 并请作者裁定。验证方案（**未执行**）：对三组同名文件做 sha256/逐节对比，产出"副本 / 同名异构 / 内容分叉"三分类。边界：只处理有发布关系的载体，不清理 host 范围文件。

---

## G-11 · 计划即交付物：核验单元、车道、patch-id

### 1) 机制与触发情境；源锚点与已读/尚缺

触发情境：多阶段/多 PR 的交付需要一个"所有者逐格执行、操作者按证据审计"的计划；或需要把"绿"与"安全落地"分开；无人值守队列需要判"哪个 commit 已经验过"。

源锚点（pin 内）：

- `pstack/skills/poteto-mode/playbooks/multi-phase-plan.md`（主体）：计划是交付物、不是实现；一格一证据；固定 H2/H3 与 PR sub-block 顺序；十条 live 车道（含 lane 1 为 regression lane against trunk，若 trunk 无特性则记录并 gate 新行为与用户终态）；perf 门双边（trunk 与 head 都要出指标；场景不同不得比值，改绝对预算）；review gate（改交互的 PR 必须人工看截图/视频）；`Arm the program / Spawn owners / PR mechanics / Verdict and merge / Boot recipe`；30 分钟审计 tick 的 verbatim 提示（只报"无更早状态报告过的受跟踪变化"）；`/goal` 文本含计划路径/PR 顺序/验证规则/谁合并/完成条件；每个 PR 的 box 只有证据存在才勾。
- `pstack/skills/poteto-mode/scripts/check-plan.mjs`（全文，见 G-04）：把上述结构变成可执行失败。
- `pstack/skills/poteto-mode/playbooks/shipping.md`（全文）：每 PR 独立验证（fresh agent，未写代码者出 verdict；`PASS/PASS+NOTES/FAIL`）；只落地"从底部起的连续已验证段"；**patch-id 规则**：记录 verdict head/base SHA + `git patch-id`；rebase/base retarget 会作废结论；只在 tests/docs/lint 差异且"build twice at verdict SHA + once at current head"判定为噪声时才保留 lane 结果；其他差异重验；不得用匹配 commit message 或旧 SHA 的绿检查替代。
- `pstack/skills/poteto-mode/playbooks/{autopilot-full,autopilot-stack,babysit}.md`（全文）：owner 闭环（每 PR 一个 owner；self-proof/CI/babysit 与 swarm 并行；merge 需 root 的 clean verdict；有 operator item 时"state then wait"）；babysit 的受限模式（只碰 frontier；不 mutate topology；冲突报告不解决）；"CI green is not a verdict, approving bot review is not a verdict"。
- `pstack/skills/poteto-mode/playbooks/orchestrate.md`（前 90 行）：standing orders、brief 模板、rolling window、pilot、drain、frontier/ledger。
- `pstack/docs/guide/07-overnight.md`（全文）：过夜契约五要素（session override、done predicate、worktree、权限预答、escape hatch）；"duration is not a finish condition"；autopilot 分级与 shipping 的"verified run"。

已读：上述主体；尚缺：`autopilot-stack.md` 全文（仅经 guide 与索引）、`routing.example.md`、benny 自动化提示词模板。

### 2) 操作、成立条件、失败模式、反例/例子

- **验证规则句**："Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked." 每个验证块以它开头；live 块必须有；perf 块四项（Metric/Probe/Baseline/Rule）；每 lane 有名字、截图路径、`Pass when`。
- **回归车道对 trunk**：同一承载场景在 trunk 与 head 都跑；trunk 没有特性时，记录该事实并 gate"diff 增加的行为 + 用户等待的终态"，不得假造 trunk 结果。
- **perf 双边**：trunk 与 head 都必须产出指标；不要对不可比场景做比值。
- **人工门**：改交互的 PR 需操作者看截图 + 30–60 秒视频后再合；无交互写 `Review gate. None. <id> is not review-gated.` 且不放 box。
- **patch-id**：谁写的代码不给出 verdict；verdict 绑 head/base SHA + patch-id；rebase 后只有在 tests/docs/lint 变化且经"以 verdict SHA 构建两次"证明是噪声时保留；否则重验。**新 head 作废旧 verdict**。
- **落地只走连续已验证段**：底部未验证 => 上面的已验证 PR 也必须等；每次合并后重算 frontier 与 patch-id。
- **无人值守契约**：先写 predicate、隔离 worktree、预答权限、留 escape hatch；plateau 不是停；不以时长当完成条件；tick 周期只报"受跟踪变化"，避免噪音。
- **operator gate 的 state-then-wait**：操作者点名的 item 停在 merge-ready，任何 owner 不得替其合并。

失败模式/反例：

- 只勾 unit box 就宣称验证（规则句明确 unit+live+perf）。
- 十条车道只有 lane 名没有截图或 `Pass when`（check-plan 会失败）。
- trunk 无特性时直接跳过 regression lane 或编造 trunk 值。
- CI 绿/机器人批准当 verdict。
- rebase 后沿用旧 verdict（patch-id 规则反例）。
- 为了让队列流动，把未验证 PR 合进连续段。
- 用"4 小时"当完成条件；tick 重复报同一表格。
- owner 自审自合并（无独立 verdict）。

### 3) A–F 判断位点与专业 concern

| 位点 | concern | 何时调用 | 拟供 Profile |
| --- | --- | --- | --- |
| F：验证规则、车道、独立 verdict、patch-id | 验证/版本/独立性 | 多阶段交付/队列 | `evidence-evaluation` |
| D：计划结构、frontier、依赖与 rebase 纪律 | 架构/接口 | 规划多 PR | `technical-planning` |
| Driver：队列、暂停、operator gate、落地顺序 | 程序性 | 无人值守/队列 | `driver` |

### 4) 当前产品锚点、覆盖与缺口

- 已覆盖：`behavior-claim-evaluation.md`（单 claim 比较）；a2r MG-1（执行单元与证明纪律）、MG-6（评审裁决）、MG-7（交接证据）。
- 缺口：**"计划即交付物"的结构与机器检查**、**车道式 live 验证（含回归车道）**、**perf 双边门**、**patch-id 的版本-验证绑定**、**连续已验证段的落地规则**、**operator gate**。这些是 D/E/F 在"多 PR/长时间交付"上的操作面，产品目前没有。

为何值得吸收：产品已有"证据"与"接受"语义，但缺少"多个交付单元如何各自带证据、版本变化如何使证据失效、何时才允许落地"的可执行纪律。

### 5) 拟处置与载体

- 拟保留：验证规则句与三类 box；十车道（可缩为"覆盖矩阵：单元 + 真实面 + 回归 + 指标"）；perf 双边与不可比禁比值；人工门；patch-id + 新 head 作废；连续已验证段；predicate 而非时长；tick 只报受跟踪变化；operator gate。
- 拟改变：`/goal`、`/loop`、云 sleeper、具体 lane 数（10）与模型名 → "宿主唤醒机制与预算"；`gh/origin` 抽象为 forge。
- 拟删除：Cursor 云、Slack 表、swarm/arena 命令名。
- 载体落点：on-demand `multi-unit-delivery.md`（计划结构 + patch-id + 落地规则），`profiles/evidence-evaluation.md`/`driver.md` 各一行入口；`charters/examples/` 可加一个多 PR 例子。
- 仍依赖 runtime：真实 CI、forge、运行中的 app（车道）；无真实环境时只能产出计划与缺证报告。

### 6) 可讨论正文草稿/操作例子 + 验证方案

```markdown
## 单元计划模板（最小结构）
- 每个交付单元（PR）绑定：依赖、文件边界、构建动作、可观察结果、验证（单元/真实面/指标三格，每格一条可失败检查与证据位置）、评审门、落地条件。
- 真实面验证：一条回归检查（对基线）+ 若干覆盖用户路径的条目；每条给证据位置与通过谓词。
- 指标验证：基线、探针、规则（不可比时改绝对预算）。
- 版本绑定：verdict 记录对象与 patch-id；rebase 后按差异类型决定重验，新 head 默认作废。
- 落地顺序：只走从底部起的连续已验证段；底部未验证则上面的已验证段也等待。
```

验证方案（**未执行**）：写一个三单元计划，跑 checker 三遍：合法、缺 lane 截图、perf 项乱序；再模拟 rebase 后 patch-id 变化，检查重验判定；最后模拟底部未验证，检查落地被阻断。边界：不要求十车道；小型单单元任务不需要本方法。

---

## G-12 · 类型/边界/原子写/工具化与 SDK 生命周期

### 1) 机制与触发情境；源锚点与已读/尚缺

触发情境：实现期最常见的"承诺之内"的专业选择：类型能否消灭非法状态、外部数据在哪里解析、崩溃/重试下写盘是否安全、是否该造工具、面向 agent 的 CLI 怎么设计、SDK/Provider 的生命周期与错误分类。

源锚点（pin 内）：

- 原则文（本包新读、a2r 未覆盖的 12 条中 D/E 侧）：`principle-type-system-discipline`（非法状态不可表示；类型是构造不是限制；brand；外部数据未解析前未类型化；不骗编译器；穷尽匹配；从权威 schema 派生；只在出现 partial 时加强类型）、`principle-boundary-discipline`（边界验证、内部信任、业务逻辑纯函数）、`principle-build-the-lever`（非平凡工作先造工具；先手工单元学配方再工具化重跑 diff；确定性杠杆优于扇出；扇出时配方写成子代理可读技能并置于其写范围外；引用原则必须产出文件）、`principle-guard-the-context-window`、`principle-sequence-verifiable-units`、`principle-test-behavior-not-implementation`、`principle-prove-it-works`、`principle-fix-root-causes`、`principle-encode-lessons-in-structure`（ABCa2r 已覆盖其中一部分的判断，本包只用其与脚本的对应）。
- `cli-for-agent/skills/cli-for-agents/SKILL.md`（全文）：非交互优先；分层 help + 例子；stdin/pipeline；缺参立即失败并给正确调用；幂等；破坏性动作 dry-run + `--force`；命令结构一致；成功输出机器可用数据（ID/URL/duration）。
- `cursor-sdk/skills/cursor-sdk/SKILL.md`（全文）+ `references/error-handling.md`（1–120）+ `references/runtime-choice.md`（前 60）：三种调用形状（prompt / create+send / resume）；五个陷阱（省略 `cloud` 静默本地；两类失败；不 dispose 泄漏；不 wait 漏终态；`run.supports` 守卫）；错误分类（Authentication/RateLimit/Configuration/Network/Unknown + `isRetryable` + `UnsupportedRunOperationError`）；重试规则（≤3、仅 retryable、退避≥30s、非幂等风险）；运行形态矩阵（local/cloud 的 PR、uncommitted、outlive、artifact、MCP、settingSources 等）；`Agent.resume` 不持久化 inline mcpServers；cloud `bc-` id ≠ run id；生产守则（exit code 1/2/0、log ids、settingSources 默认空、skipReviewerRequest、显式 apiKey）。
- `pstack/skills/poteto-mode/scripts/orch/store.ts` 的原子写/锁（G-04）。

已读：上述；尚缺：`typescript-best-practices` 与 `patterns.md`、SDK 其余 references、`principle-*` 其余 D/E 侧（laziness/subtract/reader-load/foundational/outcome/redesign/attack-premise）。

### 2) 操作、成立条件、失败模式、反例/例子

- **类型纪律**：sum type 消灭非法组合（反例 `{completed:boolean; completedAt?:Date}`）；brand 语义原语；边界 parse（bytes→typed state 纯函数）；禁止 cast/`any` 掩盖边界；穷尽匹配必须让编译器在新增变体时失败；从权威 schema 派生；只在 partial 出现处加强类型，不过度精确化。
- **原子写/锁（实现证据）**：同目录临时文件 + `wx` + rename + finally 清理；锁记录 PID，死 PID 才自动接管，活持有者要显式 force，释放前核对归属。这是"幂等/崩溃安全"从判断到实现的落点（a2r MG-5 已给判断）。
- **造杠杆**：先手工一个单元学配方，再写脚本并对同一单元重跑 diff；能一次处理的不要在 fan-out 中手工做；扇出时把配方写成子代理可读技能并放在其写范围之外；引用本原则必须真的产出工具文件。
- **面向 agent 的 CLI**：非交互优先、分层 help（子命令自己拥有文档）、`--help` 必带 Examples、stdin/pipeline、缺参立即报错并给正确调用、幂等、dry-run + force、成功输出机器可用的 ID/URL/duration。
- **SDK 生命周期**：每个 create/prompt/resume 用 try/finally dispose；启动失败（抛 `CursorAgentError`）与运行失败（`status==="error"`）分开处理、不同退出码；`run.supports` 守卫四种操作；rehydrate 的 detached run 可能不支持 stream；不盲目重试非 retryable；resume 必须重传 inline MCP；本地默认不加载 ambient settings（除非显式 `settingSources`）；本地运行等同"可删文件"权限，需限制 cwd/凭证。

失败模式/反例：

- 用 cast/`any` 绕过边界校验，运行时才炸；状态用布尔+可选字段承担互斥语义。
- 原子写用"直接覆盖 + 崩溃"（可读到半文件）；锁用"约定不并发"而不是结构（a2r 已给判断，本包给实现反例）。
- 一次性脚本不造 lever：无法被审查者重跑，且规模上手工不可控。
- CLI 默认交互/缺参挂起；help 无例子；成功输出不可解析。
- 把"启动失败"和"运行失败"混一个 catch；不 dispose；不 wait；对 `isRetryable=false` 做重试（可能重复云运行）；resume 忘带 MCP 配置；省略 `cloud` 得到本地 agent。

### 3) A–F 判断位点与专业 concern

| 位点 | concern | 何时调用 | 拟供 Profile |
| --- | --- | --- | --- |
| D：类型/边界/模块契约 | 架构/类型/安全 | 设计接口与数据模型 | `technical-planning` |
| E：原子写、锁、CLI、SDK 生命周期 | 实现/可靠性 | 实现与集成 | `implementation` |
| F：可重跑检查（lever）与负控制 | 验证/证据 | 需要可复核产物 | `evidence-evaluation` |

### 4) 当前产品锚点、覆盖与缺口

- 已覆盖：`cross-module-design.md` 的接口/seam/depth；`guide-mock-adapter-choice.md` 的依赖分类；ABC2 MG-5 的幂等三问/共享状态判断；`profiles/implementation.md` 的"自测不等于独立评价"。
- 缺口：**类型系统纪律**（DES-09 未覆盖）、**原子写/锁的实现反例**（DES-11/12 未覆盖）、**build-the-lever**（DES-24 未覆盖）、**面向 agent 的 CLI 契约**、**SDK/Provider 生命周期与错误分类**（仍依赖真实 runtime）。

为何值得吸收：这些是 E 的主要专业技法，且都能以"判断 + 例子"吸收而不引入平台框架。

### 5) 拟处置与载体

- 拟保留：类型纪律七条与三个测试问句；边界 parse/纯函数；原子写与锁的判据（不强制实现）；lever 操作（先手工再工具化、可重跑、扇出时配方外置）；agent-CLI 九条；SDK 生命周期与两类失败、`supports` 守卫、resume 不持久 MCP、retry 边界。
- 拟改变：TypeScript/Rust/Swift 等语法示例改为"静态类型语言通用"，TS 细节留 `typescript-best-practices`（未读，尾部）；Cursor SDK 段落明确标为"平台/Provider 示例"，把可迁移部分（两类失败、生命周期、能力守卫、重试边界）与专属 API 分开。
- 拟删除：`@cursor/sdk`、`Agent.create` 等 API 名从通用方法正文删除，只留 source anchor 与"真实 SDK 证据"。
- 载体落点：`methods/` 可能新增 `type-and-boundary-discipline.md`、`crash-safe-writes.md`（若 gate 采纳）；或并入 `cross-module-design.md` 的按需扩展；`profiles/implementation.md` 入口补 2–3 行。
- 仍依赖 runtime：真实 SDK/Provider 调用、浏览器/网络/文件系统；无真实访问时必须标"未在真实 Provider 验证"。

### 6) 可讨论正文草稿/操作例子 + 验证方案

```markdown
## 类型与边界（操作摘要）
- 互斥状态用判别联合；不要用布尔+可选项表达。
- 语义原语（ID/金额/时间）在构造处校验后按类型信任。
- 外部数据（RPC/JSON/CLI 参数/配置/DB 行）在边界 parse 成领域类型；内部不再重复校验。
- 不骗编译器：出现 as/any/非空断言就追到边界改成 parse/narrow。
- 穷尽匹配让编译器在新增变体时报错。
- 只在出现 partial 的地方加强类型，其他保持普通形状。

## 崩溃安全写（操作摘要）
- 同目录临时文件独占创建 → 原子替换 → finally 清理；禁止直接覆盖。
- 互斥锁记录持有者；持有者失活才接管；活持有者需显式批准；释放前核对归属。
```

验证方案（**未执行**）：① 用判别联合改造一个"布尔+可选项"的状态，确认非法组合不可构造；② 在边界注入坏 JSON，确认 parse 报错且内部类型不再防御；③ 故意在写盘中途 kill，确认读端只见旧文件或完整新文件；④ 用一个 0.5 秒脚本替代手工批量编辑并重跑 diff；⑤ 对 SDK 做 mock 的启动失败/运行失败/不支持操作三路，确认退出码与处置不同。边界：不要求静态类型；动态语言用解析+断言替代；SDK 结论只在 pin 版本内有效。

---

## G-13 · 连接器装配、凭据形态、清单校验缺口

### 1) 机制与触发情境；源锚点与已读/尚缺

触发情境：把外部服务以 MCP 连接器接进 agent 宿主；需要判断传播形态、凭据注入面、宿主能力门（版本/客户端）、副作用与审批、以及"清单声明了什么"与"实际存在什么"的校验缺口。

源锚点（pin 内，机器核对）：

- 79 个 `third_party/*/.cursor-plugin/plugin.json` + `mcp.json`（jq 提取）：传输 **77 http / 2 stdio**（`playwright` 用 `npx -y @playwright/mcp@latest`；`xero` 用 `npx -y @xeroapi/xero-mcp-server@latest` 且 `env` 注入 client id/secret）。注意：`type` 字段可缺省，缺省按 http 处理（`gong` 即 `url`+`auth` 无 `type`；用"是否有 command"判断更稳）。
- 凭据形态四类：**headers 注入用户键 7 个**（`brevo, excalidraw, github, hunter, similarweb, smartsheet, wrike`，值走 `${VAR}`）；**`auth` OAuth 7 个**（`docusign, gong, hubspot, salesforce, x, x-ads, zoom`；其中 **x 与 x-ads 在仓库内硬编码同一个 `CLIENT_ID`**，其余走 `${VAR}`）；**env 注入本地进程 1 个**（xero）；**none 64 个**（依赖宿主浏览器/OAuth 流程）。12 个 `plugin.json` 声明 `variables`（JSON Schema：type/properties/required）用于让用户填值；其余靠 OAuth。
- 宿主门：`marketplace.json` 94 条目 = 15 first-party + 79 third_party；`minClientVersions` 分布（third_party，本 session 逐文件核对）——`3.13.0` 62 个；`3.19.0` 5 个（`onedrive, outlook, outlook-calendar, sharepoint, teams`）；`3.22.0` 4 个（`google-docs, google-sheets, google-slides, webull`）；**字段缺省 5 个**（`docusign, gong, hubspot, salesforce, zoom`，即无宿主门声明，不等于不兼容）；`cursor: "never"` 3 个（`finance`、`x-money`、`shopify-store`，对 Cursor 不可见，面向 Grok Bot/sand）。15 个 first-party 清单均无 `minClientVersions`。`schemas/marketplace.schema.json` 定义 `clientVersionRequirement` 为 semver 或字面量 `never`，并声明 `grokbot` 与 deprecated `sand`。
- 校验面：`scripts/validate-plugins.mjs`（全文）只做 marketplace schema + 每个 plugin schema + marketplace↔plugin `name` 相等 + source 目录/`plugin.json` 存在；**不校验声明的 skills/agents/rules/hooks/mcpServers 路径是否存在，不校验 frontmatter**；`schemas/plugin.schema.json` 的组件字段为 `stringOrStringArray`（skills/agents/rules/commands）与 `hooks: string|object`、`mcpServers: path|inline|array`、`variables` JSON Schema。CI workflow 仅在 `marketplace.json`、`**/plugin.json`、`schemas/**` 变化时触发，`npm install --no-save ajv ajv-formats` 后运行同一脚本。
- 前端质量门是**散文**：`create-plugin/rules/plugin-quality-gates.mdc` 六条（manifest name、相对路径无上溯、声明路径对应真实文件、frontmatter 必备、范围聚焦、默认装到 `~/.cursor/plugins/local/<name>/`）。
- 示例 README/CHANGELOG：`third_party/github/README.md` 的 PAT 最小权限与轮换说明；`CHANGELOG.md` 记录 logo/服务器/变量声明。
- 货币与审批：`third_party/x-money/skills/x-money-guide/SKILL.md`（前 90 行）"每次动钱都要重新批准、一次只批一个、变了重批、不得伪造 approval"；`x-api-mcp-guide/references/pricing.md`（前 50 行）：读按对象计费、写按成功请求、失败不计费、MCP 按 1:1 代理计价、owned-data 折扣。
- 规则路由：`third_party/shopify-store/rules/shopify.mdc`（全文）：同一服务两能力（连接商店的 MCP vs 构建用 toolkit）按问题类型路由；写前先读、写前确认并说明改什么；工具缺失不得改用 web 搜索商店数据。
- 副作用自述（索引级，未逐句核）：coinbase/robinhood/buffer/posthog-mcp/tinyfish/trello 等在 README 里明确 live 效果与责任。

已读：上述；尚缺：79 份 README 全文（本包抽查 4 份 + 索引摘要）、CHANGELOG 全文、`third_party/x/skills/x-api-mcp-guide/SKILL.md` 正文（只读标题面）、`create-plugin` 其余两 SKILL、`plugin.schema.json` 全文（只读字段面）。

### 2) 操作、成立条件、失败模式、反例/例子

- **传输形态决定风险面**：远程 http 潜在暴露面是 URL + 凭据注入；本地 stdio 会在调用者机器上执行 `npx -y ...@latest`（供应链与"最新版不可复现"问题），必须单独列风险。
- **凭据形态分类**是安全判断的起点：用户键 headers（可轮换、最小 scope）、内联 OAuth client id/secret（仓库内值 = 公开客户端 id，但 secret 不应入仓）、env 注入本地进程（进程可见、日志风险）、宿主托管 OAuth（用户可撤销、无本地 secret）。`variables` 的 JSON Schema 是"用户要填什么"的声明面。
- **宿主能力门**：`minClientVersions` + `never` 控制插件对特定客户端的可见性；被隐藏不等于不存在；`grokbot/sand` 表明同一清单服务多客户端。
- **声明 ≠ 存在**：校验只盖 schema 与名字相等；路径存在性与 frontmatter 由散文 checklist 兜底。这是明确的"诚实边界"：要么补机器检查，要么把不可检项显式登记为风险。
- **副作用与审批必须写进连接器自身材料**：动钱/发帖/写他人数据的连接器在文首声明 live 效果与责任；按动作逐次审批、一次一个、变更重批、拒绝后不得重试；`dry-run` 名称不可信（G-08）同样适用于此类工具。
- **能力以服务器为真源**：README 只描述；工具面/账户差异由服务端决定；结果消息按用户语言转述。

失败模式/反例：

- 把 `mcp.json` 的 `type` 缺失当异常；或把 `npx -y @latest` 当等价远程 MCP。
- 仓库内硬编码 client id 当 secret（x/x-ads 的共享 CLIENT_ID 是公开客户端标识，但任何 secret 入仓都是缺陷）。
- 只校验 schema 就宣布"插件有效"（路径/frontmatter 未核）。
- 在文档里假设某能力存在（真源在服务端）。
- 对 `never` 的插件在错误客户端做可用性判断。
- 动钱/发帖类工具无逐动作审批、或复用上一次批准。

### 3) A–F 判断位点与专业 concern

| 位点 | concern | 何时调用 | 拟供 Profile |
| --- | --- | --- | --- |
| D：连接器装配与传输选择 | 接口/依赖 | 引入外部服务 | `technical-planning` |
| F：副作用/审批/scope 的可验证声明 | 安全/合规/证据 | 有写副作用的工具 | `evidence-evaluation` |
| E：凭据注入与日志卫生 | 实现/安全 | 落地连接 | `implementation` |
| D：校验的诚实边界 | 维护性 | 声明式清单的可靠性 | `technical-planning`（辅） |

### 4) 当前产品锚点、覆盖与缺口

- 已覆盖：产品无连接器/MCP 面；`guide-redacted-evidence.md` 处理证据脱敏，不处理凭据注入与工具审批。
- 缺口：传输/凭据/宿主门/声明校验/副作用审批五类机制全缺。它们属 D/E 安全与工程装配，可在不引入 Cursor 专有字段的情况下表述为"外部服务接入的五个判断面"。

为何值得吸收：任何真实工作都会接外部系统；"工具权限 ≠ 动作许可"（Backbone/Charter 已有）在这里需要一个操作层对应物：**连接器声明、凭据最小面、宿主门、副作用逐次批准、校验边界**。

### 5) 拟处置与载体

- 拟保留：传输形态两分与本地执行风险；凭据形态四类；`variables` 声明；`minClientVersions`/`never` 的可见性语义；"声明 ≠ 存在"的诚实边界；副作用自述 + 逐动作审批；服务端为工具面真源。
- 拟改变：`plugin.json/mcp.json/minClientVersions` 字段 → "宿主清单的等价物"；`npx -y @latest` 作为例子并标注可复现性风险。
- 拟删除：Cursor/Grok Bot/sand 客户端名与具体插件名（source anchor 保留）。
- 载体落点：on-demand `external-service-onboarding.md`；`methods/README.md` 按需表加一行；`profiles/technical-planning.md`/`implementation.md` 各一行入口。
- 仍依赖 runtime：真实宿主清单/校验器/服务端工具面与审批机制；无外部系统时只能定义检查面。

### 6) 可讨论正文草稿/操作例子 + 验证方案

```markdown
## 外部服务接入检查面
1. 传输：远程连接 vs 本机执行；本机执行要标注供应链与版本钉住问题。
2. 凭据：用户自带键 / OAuth 客户端 / 本机环境注入 / 宿主托管；secret 不得入仓、入日志、入对话；说明撤销路径。
3. 宿主门：哪些客户端在什么版本可见；被隐藏不是不存在。
4. 声明 vs 存在：清单校验只证明 schema 与名字；声明的组件路径与 frontmatter 是否另检，未检的显式登记。
5. 副作用：动钱/发文/写他人数据的动作在材料里明示；逐动作批准、一次一个、变更重批、拒绝不重试。
6. 能力真源：以服务端当前工具面为准，不按文档假设能力；账户/版本差异要说明。
```

验证方案（**未执行**）：对一个本地 mock 连接器做四项：缺 `type` 字段；声明的 skill 路径不存在；凭据从环境变量进入日志；写动作无审批。期望检查面分别给出"按 http 处理"、"声明存在性未核/失败"、"脱敏或失败"、"必须逐次批准"。边界：不要求接入真实第三方；审批机制由宿主决定，方法只判定"是否必需"。

---

## G-14 · 尾部与未评估区（纯资产/重复载体/未读面的归组处置）

本节只做**归组与判定依据**，不作机制断言；凡未读即标未读。旧 B 台账（ABSORB-B-MECHANISM-COVERAGE.tsv）中 cursor 行 `not-covered/partial/pending` 已在 §2 导航，本包不因旧标签自动采纳。

| # | 面 | 路径/规模 | 本包读深 | 建议处置 |
| --- | --- | --- | --- | --- |
| T-01 | 纯资产：LICENSE（94，约 1063B/份）、logo PNG/SVG（91）、`assets/avatar.png`、`docs/guide/images`、`grok-voice/assets` | 第三方面板重复载体 | metadata（字段面） | 归组：无工程行为，随插件装配面处置；**例外**：`grok-voice/assets/logo.svg` 未被 manifest 引用（漂移面，PKG-09/11） |
| T-02 | CHANGELOG（79+） | 79 份 third_party + first-party | 抽查 1 份头 | 归组：版本叙事，非机制；只在需要版本历史时按行读 |
| T-03 | third_party README 全文（79） | 每份含 install/MCP/setup/gate/capabilities | 抽查 github/xero/playwright/x-money/x-chat + 索引 section 级 | 归组：能力/scope 清单按连接器；PEND-01 仍是未完成面，本包只给分类框架 |
| T-04 | 未读 first-party skills：cursor-team-kit 13 个（fix-ci/loop-on-ci/fix-merge-conflicts/get-pr-comments/make-pr-easy-to-review/new-branch-and-pr/run-smoke-tests/review-and-ship/verify-this/weekly-review/what-did-i-get-done/workflow-from-chats/check-compiler-errors/deslop/typescript-exhaustive-switch）、grok-voice 4、teaching 其余、agent-compatibility agents、create-plugin agents、docs-canvas 其余、ralph-loop 其余 | — | 部分标题/head | 其中多数属 A/B/C 或与 a2r 包重叠；DEF 相关候选：`fix-ci`/`loop-on-ci`/`fix-merge-conflicts`/`run-smoke-tests`（EVID-21/22、DBG-06/12）→ 建议下一波或并入 G-05/G-11 |
| T-05 | pstack 未读 skills：arena/swarm/architect/how/reflect/recall/tdd/unslop/automate-me/figure-it-out/setup-pstack/make-bot-ui/typescript-best-practices；`why` investigator/sources 其余；`interrogate/code-quality-review.md` | — | 索引 + 少量 head | 与 a2r 重叠较多；DEF 明确残余：`code-quality-review.md`（评审镜头）、`arena/swarm`（扇出规则）、`typescript-best-practices`+patterns（类型细节）、`why sources`（历史源） |
| T-06 | orchestrate 未读：`schemas/{plan,state}.schema.json`、`cli/{task,util,comments,inspect,forensics,andon,index}.ts` 正文、`adapters/slack/index.ts`、28 测试正文、`tools/{probe-models,nudge-root,generate-json-schemas}`、`models.ts`/`schemas.ts`/`errors.ts`/`branches.ts` | 最大机器面 | 标题/选段 | 本包已覆盖其**行为契约**（G-01/02/03）；schema 细节与测试正文按需回读；`probe-models`/`models-catalog` 的证据若需成本/模型主张再读 |
| T-07 | pstack 未读 playbooks：bug-fix/feature/refactoring/prototype/visual-parity/authoring-a-skill/opening-a-pr/investigation | — | 索引 | `bug-fix` 的"control/loop/model/PR 默认"在 M4 被显式 defer；本包 G-11 提供其验证与落地纪律，若 gate 要重估需回读全文 |
| T-08 | cursor-sdk 未读 references：auth(6.2KB)/streaming(8.4KB)/mcp(8.1KB)/advanced(9KB)/patterns(10.7KB) | PEND-03 | SKILL + 2 份部分 | 平台耦合面；仅在需要真实 SDK 集成方法时回读；可迁移结论（两类失败、dispose、supports、resume 不持久 MCP）已入 G-12 |
| T-09 | benny 未读：setup-benny/triage-issue-reports/reproduce-and-fix-issues SKILL 正文、automation prompt 模板、routing example、feature-map example | — | FOR_AGENTS/config/两个 reference | 三个 SKILL 是 B/E 操作文件；已由 FOR_AGENTS 与 adapter 契约覆盖运行边界；若 gate 采纳 G-08 再回读 |
| T-10 | pr-review-canvas 资产：`cursor-team-kit/skills/pr-review-canvas/{renderer.js,styles.css,template.html}`、`pr-review-canvas` 独立插件 | 6+6 paths | README + SKILL 前 80 行 | 同名不同实现（G-10）；渲染资产无独立机制价值，归组；如需吸收"评审信息重排"可回读 renderer |
| T-11 | x-api pricing.md（PEND-07） | 约 5KB | 前 50 行 | 成本主张已可回答：读按对象、写按成功、失败免费、MCP 1:1；完整表按需回读 |
| T-12 | marketplace 94 条目/plugin 清单字段 | 94 | 字段面 | 与 G-13 同组；`minClientVersions` 的 `never` 三例已核 |
| T-13 | 两文章与 UCBIP | 不在分母 | — | 不在本包范围 |

**尾部结论**：本包不把任何未读面写成"已评估"。按 Driver 的"所有 pin 内路径能解析到现有记账及机制组"口径，T-01/T-02/T-12 可归组处置；T-04/T-05/T-07/T-09 需下一波或明确暂缓理由；T-06/T-08 已有行为级覆盖但精确接口/schema 未逐字核对。

---

## 3 · 与旧 B 台账的对应（仅导航，不作资格）

- 本包直接回应的 B 旧行：`DES-09`（类型）、`DES-11/12`（原子写/锁）、`DES-13/16`（共享状态/减法，ABC2 已判）、`DES-24`（lever）、`DBG-10/12/14/15/18`、`EVID-07/08/09/10/13/14/21/22/23`、`DLV-01/03/04/05/06/11/12`、`ORC-02/03/05/06/07/10/12/13`、`HIT-05/06`（邻接）、`CONC-02/06`、`FMT-09`、`PKG-01..12`、`PEND-01/02/03/07`。
- 其中 `PEND-02`（agent-manager/watch-pr/orch 并发语义）与 `PEND-03`（cursor-sdk/why references）是本包的主要补读目标；`PEND-02` 已由 G-01/02/03/04/05 的行为级阅读覆盖，`PEND-03` 部分覆盖（SKILL + 2 份 reference 部分），其余列 T-08。
- 旧 adopt/narrow/defer 标签（含 B 台账 `verdict_candidate` 列）在本包中**未被继承为任何结论**；`narrow`/`pending-check` 仅用于定位未覆盖面。

---

## 4 · 机械自检（非专业裁定）

- 本包只写 `docs/absorption/2026-10-02/packages/A4-CURSOR-DEF.md` 一个文件；未改产品、未改他人文档、未 commit、未执行源内任何脚本或测试。
- 所有源引用均给 `cursor-plugins` + pin `ecc249f1…` + repo-relative path + section/函数/行段；行号来自本 session `git show` 输出。
- 未执行观察一律标注"未执行"；未读面集中在 §0 与 G-14（T-*），未把未读写成已评估。
- 与 a2r 的重复面已在 §1 声明并逐项指向其包；本包不重述其已拟入方法的正文。
- 本包产生的候选类型：机制组 14 个（G-01..G-14），其中 G-14 为归组/尾部，不含新机制主张。
