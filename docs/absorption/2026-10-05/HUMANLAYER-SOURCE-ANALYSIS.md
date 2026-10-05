# HumanLayer 仓库吸收研究（分项材料）

日期：2026-10-05（Asia/Shanghai）。状态：**研究建议，未实施、未接受为 TPW 方法或运行合同**。

## 1. 结论

`humanlayer/humanlayer` 最值得 TPW 吸收的部分，是**研究结果怎样变成下一阶段真正能消费的固定输入，以及恢复时怎样把旧记录和真实对象逐项对照**。它有具体 `.claude/commands/` 和 `.claude/agents/` 载体，能补 UCBIP 暴露的输入未进入上下文、旧卡替代原件、方法原则缺操作形状等问题。建议向已有方法和接入例合并少量步骤、产物例与反例，不另建固定 Research → Plan → Implement 流水线。[H03]、[H04]、[H05]、[H06]

必须先纠正来源身份：固定 tip `99abe673498cf8bdcd5f989aebe9406a27185b3b`（2026-06-18，提交题为 `Update README.md`）的根 README 直接将本仓称作 public issues repo，并声明代码大多弃用。这里包含旧 HumanLayer SDK 文档、CodeLayer 本地 Go daemon / CLI / WUI、较新的 Bun / oRPC / Electric / Yjs 草稿等不同历史层。**本仓不是当前受支持 HumanLayer 产品实现的认证来源。** 不应把 README 的 rebuild 链接反推为本仓仍受维护，也不应以旧 SDK 印象统摄全部源码。[H01]、[H02]、[H18]

TPW 当前基线为 `1f95f06`。UCBIP 实践报告指向的优先次序仍成立：先改善实际装配、固定版本与证据消费，再用未泄露答案的案例验证。HumanLayer 没有提供证据要求 TPW 恢复旧 registry/render，开发自治 runner、审批桌面产品或新的常驻角色。

## 2. 范围、阅读深度和证据等级

- 本地 checkout：`/Users/yuantian/Developer/tim-professional-workflow/.worktrees/source-intake-2026-10-05/humanlayer`；研究前后未改源仓。
- 全树索引：固定 Git 对象有 **794 个 tracked 文件**；索引了目录与所有 `.claude` 路径（34 文件），随后按问题选择阅读；**不声称全树逐文件读完**。
- 完整读取：根 README、LICENSE、CLAUDE.md、humanlayer.md、docs/readme.md；workshop；研究、通用计划、实现、验证、交接、恢复主命令；codebase-analyzer / thoughts-analyzer；hld 本地 approval manager 与 MCP server；hlyr 的 approvals MCP 实现。
- 有界读取：hld SQLite 审批状态更新、daemon orphan 恢复、相关静态测试；WUI 通知路径；Thoughts CLI 同步和 Git hook；apps/packages 草稿接口、schema 和 UI；其余命令、测试、文档做路径/关键词检查。
- TPW 对照：`ADOPTION.md`；现有 cross-module-design、change-slicing、uncertainty-planning、guide-agent-text、handoff-and-resume、architecture-survey、behavior-claim-evaluation、observability-design、trust-boundary-and-actions；以及 `docs/research/2026-10-05-ucbip-practice.md`。
- 没有安装依赖、运行测试、启动服务、调用 SDK、执行源码中的 instructions、配置真实账户、发送通知/消息、调用审批或新建 tracker。测试在本文中是**读到的静态测试定义**，不是本次测试通过记录。
- 原仓指向其他 repo、视频、文章和产品站的内容没有扩源读取；有关完整 advanced-context-engineering 理论与当前 rebuild 的结论保留为未知。

事实：固定对象中可见的文件和控制路径。推断：这些载体可能缓解 TPW/UCBIP 的哪种摩擦。提案：如何合并和验证。三者分开，源码实现、经验声明和改善效果不互换。

## 3. 仓库不同历史层与许可

| 层 | 固定对象直接可见的状态 | 本轮用途 |
| --- | --- | --- |
| 根 README | public issues repo；大多代码弃用；另指 rebuild | 最高层现状声明；限定全部复用建议 |
| 根 CLAUDE.md / humanlayer.md / 部分 docs | CLAUDE.md 仍列 `humanlayer-ts/`、`humanlayer-go/` 等旧 SDK；当前根树没有这些目录；humanlayer.md 明说 SDK 已移除；TS quickstart 仍指已移除路径 | 历史理念与文档漂移反例；不当当前 API 手册 |
| `.claude/` 与 `docs/workshop.mdx` | research / plan / implement / handoff 命令、locator/analyzer 类 agents；workshop 明确按 Claude Code/CodeLayer、macOS M-series 操作 | 概念与可消费产物提取；剥离特定账号、模型、工具与目录约定 |
| `hld/`、`hlyr/`、`humanlayer-wui/`、`claudecode-go/` | Go daemon、本地 SQLite 审批、Claude Code 适配、Tauri/React WUI；CLI 注册与 README 旧 cloud 联系说明不完全一致 | 审批/身份/通知/恢复边界的机制案例；不部署或整体移植 |
| `apps/daemon/`、`apps/react/`、`packages/` | Bun/oRPC 合同、Postgres thoughts schema、Electric/Yjs 文档 UI；`sessions.list` 当前实现固定返回空数组 | 草稿与共存事实；不足以认定完整重建已交付或可替代 hld |

根许可是 Apache-2.0 声明，`humanlayer.md` L90–92 明说 repo 中 SDK / CodeLayer sources 采用 Apache 2，`hlyr/package.json` 也标 Apache-2.0。tracked 树仅找到根 `LICENSE`，没有发现各分区单独 LICENSE；因此**没有证据把某个新目录自行认定为另一许可，也没有证据认定商业 rebuild 服务被这份许可覆盖**。本轮只分析概念与源码，不 vendor 文件；若后续复制，需要保留适用署名/许可并逐项核第三方衍生代码、依赖和素材的许可。此次没有完成依赖/图片/视频/商标的完整权利链审计，不把“根 Apache”外推为任意素材可直接复制。[H02]、[H19]

## 4. 机制矩阵：merge / narrow / defer / skip

这里的分类是建议，**不是方法接受记录**。`merge` 表示原则已有，以操作例或来源锚点合并；`narrow` 表示只取条件化子集；`defer` 表示下一轮出现真实需求时再研究/实现；`skip` 表示这次不吸收该形态。

| ID | 来源机制与证据 | TPW 已有接缝 / UCBIP 对应 | 建议 | 最小吸收与条件 |
| --- | --- | --- | --- | --- |
| HL-01 | 先记录当前实现、调用路径、文件/行与来源版本，再将建议另立；当前代码优先于历史 thoughts；研究命令限制做实现方案 [H03] | `architecture-survey.md` L17–22、`cross-module-design.md` L12；UCBIP §4.4 当前机制与预防包装混用 | merge / narrow | 在既有调查/设计输入加“事实路径 → 未知 → 候选”短例；当用户就是来求改进时保留改进，不采用一律禁止评价的角色定义 |
| HL-02 | 研究前自己读承重输入；子任务聚焦具体目录/问题，返回可恢复行引用；主者核异常结果而非仅拼接 [H03]、[H04] | `ADOPTION.md` L25–31、`handoff-and-resume.md` L32–35；UCBIP §3.1 读取不等于应用 | merge / narrow | 给一次并行研究输入/输出例：来源 pin、问题、范围、可用读工具、需要的证据；只在独立子问题值得分工时用，不变成固定多 agent 门 |
| HL-03 | 研究文档保存 date / commit / repo / question / findings / limitations，并生成 GitHub permalink [H03] | `ADOPTION.md` L9–23、`handoff-and-resume.md` L34、L41；UCBIP §4.7 固定对象易丢 | merge | 展示最短可消费研究原件，来源/对象/覆盖要够；不固定 YAML schema、ticket 名、thoughts 目录或必须全字段 |
| HL-04 | plan 把当前状态、目标终态、限制、非目标、阶段改动、验收面写清；自动与手工观察分开 [H04] | `cross-module-design.md` L20–22、`change-slicing.md` L12–16、L52；UCBIP §4.1 未先裁定产品单位 | merge / narrow | 用 Plan 例说明每个承诺对应对象、完成单位、观察；“自动/手工”可表示执行方式，不能取代 claim / coverage / real-surface 判断，也不能等于 agent/human 固定能力分界 |
| HL-05 | 计划命令多次要求用户互动，终版不得有任何未决问题；每个阶段默认停等手测 [H04]、[H05] | `uncertainty-planning.md` L17–28、`change-slicing.md` L31、L73–77；UCBIP §4.9 成本未验证 | narrow / skip | 只让会改变承诺/authority 的承重未知阻断依赖项；可带条件的后续未知继续记录。真实人类保留决定才召回；不导入必问、多轮确认或每阶段等人工 |
| HL-06 | implement 在现实偏离时报告 expected/found/why；validate 冷启动查 Git、比计划与实际代码、列手测未证 [H05]、[H07] | `cross-module-design.md` L22、`behavior-claim-evaluation.md` L16–27、`handoff-and-resume.md` L49–54；UCBIP §3.2、§4.2 | merge / narrow | 用一个承诺内适配与承诺变化的分叉例，差分绑定对象；validate 是评价操作参考，不证明独立 F，仍需核实际贡献。不能把“实现符合 Plan”当“Plan 正确” |
| HL-07 | 实现恢复默认信任旧 checkmarks，从首个未勾项继续 [H05] | `handoff-and-resume.md` L26、L28、L49–54；UCBIP §4.7 stale 卡 | skip；作反例 | checkbox 表示记录，不单独支持已完成；有效的既有证据可按 claim/object/coverage 复用，不一律重跑，也不盲信 |
| HL-08 | create_handoff 给 task/status、少量 critical references、recent changes、learnings、artifacts、next steps；resume 逐项旧状态→当前验证 [H06] | `handoff-and-resume.md` L12–15、L64–78；UCBIP §4.7 旧卡/最终 diff 缺失 | merge / narrow | 加“旧记录 → 当前对象/覆盖 → 仍有效/变化/未知”的接收例；已有 spec/plan 用指针，实际缺失状态才补内容。持续原地工作无需强制另建 handoff；不复制所有原件或默认确认两次 |
| HL-09 | thoughts-analyzer 过滤旧研究，分 decisions / proposals / implemented；源码 researcher 与 thoughts curator 分工 [H08] | `guide-agent-text.md` L8–12、L22–27，`handoff-and-resume.md` L68–69；UCBIP §4.7 入口巨量历史 | merge / narrow | 当前启动短片段指向固定原件，旧历史按需要读；保留会影响下一步的理由、例外和未知。不采用“删掉所有 rejected options”，因为承重理由可能需要保留 |
| HL-10 | Thoughts 独立 Git repo、symlink/hardlink searchable、hooks 与自动 sync；sync 会 `git add -A`、commit、pull --rebase、push [H09] | `ADOPTION.md` L42–50、L76–80；`guide-agent-text.md` L22–23 | skip 形态；defer 限定便利 | 项目记录继续放既有 owner 位置。若真实检索摩擦复发，只研究现有文档索引/可恢复路径，不安装 hooks/另一真源/自动 push；“sync”不是只读也不是仅保存本地 |
| HL-11 | 本地 approval 记录 session/run/tool/input；通过 tool_use_id 关联实际 tool call；拒绝带原因；SQLite 决定只从 pending 更新 [H10]、[H12]、[H15] | `trust-boundary-and-actions.md` L109–117、L137–138；`external-tool-operation`；UCBIP §4.6、§4.8 | merge / narrow，runtime defer | 如下游需要审批适配，先写清哪种具体动作在何处阻断、谁有权判断、批准绑定哪个实际输入、拒绝怎么回工作。审批记录/工具允许不创造 TPW 授权，也不是 OS 隔离 |
| HL-12 | manager 有 auto-accept edits 与 dangerous skip，超时只是禁用该模式；ralph/oneshot 把 skip-permissions、launch、PR、ticket comment 固定串起来 [H10]、[H17] | TPW Charter / Backbone authority；UCBIP §4.6 工具与授权错配 | skip | 不复制扩大工具权、全自动外部写、时间窗即安全的默认。历史 automation 给出的动作链不授予本任务或下游同等权 |
| HL-13 | SQLite 为记录；eventBus 仅内存，慢 subscriber 会丢事件；Go MCP 等待通道注册在创建审批之后，只由事件释放或 ctx cancel，无内置审批 timeout；旧 TS 路径则每秒查 persisted status [H11]、[H13] | `observability-design.md` L93–100、`handoff-and-resume.md` L36、L73–74；UCBIP §4.6 缺证沉默 | merge 失败例；runtime defer | 说明“状态持久化 ≠ 等待端/事件持久恢复”。对假想适配验证 fast decision、lost event、disconnect、restart、late reply 的消费与状态回读；不能把 UUID/事件/通知等价 exactly-once |
| HL-14 | daemon restart 将 running / waiting_input / starting 标 failed，保留 interrupted 等；静态测试核三类孤儿状态 [H14] | `handoff-and-resume.md` L64–78；UCBIP §4.6 真实状态/最后 commit 混用 | merge 反例；runtime defer | 加一例区分过程退出、checkpoint、业务效果未知、任务可恢复；从状态对账继续，不能把旧实现宣称 durable workflow 自动续跑 |
| HL-15 | WUI 按焦点与当前 session 选择 OS/in-app 通知；无权限/异常转 in-app；正在看同 session 时跳过 toast；notify 返回 ID 或 null [H16] | `observability-design.md` L82–100；UCBIP §4.6 sent=0 / 无告警证据 | merge 失败例；runtime defer | 分开 pending work 状态、通知发起、通道实际送达、接收者读到与已回应；一个 ID 或 send API resolved 不能证明人已知情。渠道实现由项目/harness 负责 |
| HL-16 | apps daemon 空 sessions.list、文档协作草稿、local CodeLayer 产品壳 [H18] | `ADOPTION.md` 无 runtime；UCBIP 报告§5.4 机械辅助条件 | defer / skip 整体产品 | 没有证据支持 TPW 现在开发 desktop approval manager、collaborative thoughts DB、Claude runner；若下游提出具体需求，先核维护/兼容/许可、现有工具与真正差异 |
| HL-17 | healthcare case study 声称 <7 天、1 人替代 3–4 人、生产无大问题 [H20] | `professional-learning` / `guide-test-evidence-quality`；UCBIP §4.9/§6 方法效果 | skip 作为效果证明 | 可记为原作者案例声明；没有本次可见原始运行/对照/验收证据，不能作为 TPW 或 HumanLayer 提效的已验证倍率 |

## 5. 两个最值得先做的候选交付

### 5.1 可消费研究输入例，合并现有 carrier

建议在现有 adoption example 或 method 的适用位置给一个短例，展示：

1. 研究问题和本次有效任务范围；固定代码对象、治理/方法对象分别写。
2. 当前实现的真实入口、数据/控制路径与会改变判断的事实 owner。
3. 已读原件与覆盖；亲读、他人具名报告、推断、建议分开。
4. 下一判断需要的最少固定输入，以及会阻断它的承重未知。
5. 可恢复报告位置、commit/path/section；已有原件用指针。

这不是新增通用 Research Profile、registry 或文档模板 gate。TPW 已经拥有这些原则，增量是让下一实例拿到之后知道如何使用。首轮验证直接沿 UCBIP §6.2 的离线未泄露答案任务做：能否先发现产品单位/生命周期/既有机制不足等承重未知，能否引用真实 owner，能否避免只复述历史结论。

### 5.2 接收者恢复对账例，补到 handoff-and-resume

推荐展示三个具体分叉：旧记录仍被当前对象的有效证据覆盖 → 复用；代码或承重输入已变 → 仅重核受影响 claim；旧卡只有 completion checkbox/自报 → 记未证并定位最便宜的观察。再展示 daemon 重启后 running 被标 failed 的案例：标记证明 runtime 认为过程已孤儿，不证明业务效果不存在，也不证明重复执行安全。这里的真实模型是**记录、实际进程、业务效果分别对账**。

首轮验证可以给一个已有候选 PASS、一个已改变的 caller、一个不带覆盖的 done 卡。正确结果应复用仍有效部分、找出受影响部分、不给 done 卡补造证据；保留本来已授权的下一步，不机械重新问所有批准。

## 6. 源码机制支持什么，不能支持什么

### 6.1 审批

`hld/approval/manager.go` 的本地控制路径，将 tool/action 输入记录到 SQLite 并关联 session 和实际 tool-use；SQLite 使用 `WHERE id = ? AND status = pending` 约束一次决定，静态测试也覆盖已批准/已拒绝后不再改决定。[H10]、[H15] 这些支持“该记录的决定只能从 pending 转出”这一窄结论，不支持 tool 绝无旁路、approve actor 有权、OS 隔离、端到端 exactly-once 或业务效果已发生。

若下游真的消费这类批准，仍须在执行点核准当前动作、实际参数/对象、有效授权与当前状态是否仍在原决定覆盖内；批准记录不能自动覆盖改参、换对象、旧工作恢复或原委托之后的状态变化。这个执行点核对是吸收提案，不声称本次已对历史实现完成端到端认证。此前有效授权和证据可以在适用范围内延续，不能由“重新核对”推导出每步都要再问人类。

Go MCP 读 `X-Session-ID` / `Mcp-Session-Id` 到 context，pending 等待表仅驻内存，并通过 eventBus 释放；此部分没有证明 header 所指身份经过完整权限校验。[H11] 本轮没有做整个 HTTP/socket 信任面审计，因此结论是**没有可据此认证的权限隔离证据**，不是断言整个系统无任何校验。

### 6.2 持久与恢复

SQLite 的记录持久，与 Go MCP handler 的 channel、eventBus subscribers 和 Claude subprocess 生存期是不同对象；源码实际在 restart 标失败而非透明恢复 active process。[H11]、[H13]、[H14] 可以为 TPW 的 fixed-object / event-vs-terminal / runtime-liveness 条文增加一个清楚反例。不能借 HumanLayer 的“durable outer loop”愿景将此历史实现认定为可等待几天并可靠续跑的引擎。

CreateApproval 发生后才注册 Go waiter，listener 未找到 waiter 的事件不重放；eventBus 满队列会 drop。[H11]、[H13] **由代码顺序推断** fast approval / lost event 存在值得验证的竞态窗口，但本次未复现，不报告已证实的线上事故。旧 TypeScript MCP 是按 ID 每秒回读状态，说明同树不同路径的恢复/等待语义不能互换。[H12]

### 6.3 通知与上下文

NotificationService 返回的是发起操作生成的 ID，焦点/权限/异常会改变实际输出渠道；不含人类已读回执。[H16] 对 UCBIP 事故最有用的不是复制通知 UI，而是明确需要哪个状态、哪个实际渠道、取不到/送不到时的 UNKNOWN 与升级路径。

Context engineering 在这份固定 repo 可直接观察到的是短命令、聚焦 agents、研究/计划/交接 artifacts 和恢复读取路径。workshop 把完整理论内容链接到其他文章/视频，尚未扩源。本文不会把“context 压缩到 X%”“每阶段清空窗口”“subagent 必定省 tokens”当已读事实或效果结论。[H21]

## 7. 重点未知与后续验证

| 未知 | 为什么会改变吸收决定 | 最小后续证据 |
| --- | --- | --- |
| 当前 HumanLayer rebuild 的接口、license 和维护模型 | 这份已弃用 code 不能决定 runtime 接入 | 若确要选运行工具，再对当前官方文档/发布对象做单独有界研究 |
| RPI 对 TPW/UCBIP 实际质量与成本的净影响 | 文档可执行不等于发现方向问题或提效 | 固定模型/工具/预算、任务未知、盲化输入，比较质量、总成本、返工 |
| 初始输入是否真的被消费且影响判断 | 文件在仓库/日志显示返回不能证明应用 | 冷启动实际输入记录＋未给答案的判断输出；缺项只阻断依赖部分 |
| runtime 审批持久/重连、决策身份与输入绑定 | 批准行、事件和 tool effect 是不同对象 | 只在下游明确需求后，在隔离 fixture 验 fast decision、重复决定、丢事件、crash、late reply 与 actual execution |
| 通知是否到达有权接收者并被处理 | notify ID 与 sent API resolved 不是读到/回应 | 有权测试渠道的实际发送/接收/处理证据；无该权限就记录未证 |
| 来源第三方代码/素材和依赖的许可链 | 根 Apache 不自动替所有第三方作许可声明 | 只在真正复制的文件/资产上核来源、声明、依赖及保留项，不做全树笼统认证 |

可先做 5.1/5.2 两个轻量交付并验效果，之后才判断是否做辅助脚本。当前有证据支持 carrier 的改进研究，没有证据支持新增编排/权限产品。接受语义变更仍交方法和责任 owner；本研究没有改变有效合同。

## 8. 固定一手来源

以下全部固定为 `humanlayer/humanlayer@99abe673498cf8bdcd5f989aebe9406a27185b3b`；行号来自该本地 Git 对象，链接未另做远端 UI 打开检验。

- [H01：根 README 的弃用与 issues repo 声明](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/README.md#L1-L3)。
- [H02：humanlayer.md 的 SDK removal / CodeLayer 历史与许可声明](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/humanlayer.md#L1-L5)；[许可部分 L90–92](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/humanlayer.md#L90-L92)。
- [H03：research_codebase，当前代码/历史记录、承重输入、产物身份与 permalinks](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/.claude/commands/research_codebase.md#L28-L84)；[产物段 L85–162](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/.claude/commands/research_codebase.md#L85-L162)。
- [H04：create_plan_generic，计划形状与承诺观察](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/.claude/commands/create_plan_generic.md#L179-L276)；[全决定/自动人工分界 L303–355](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/.claude/commands/create_plan_generic.md#L303-L355)；[聚焦分工/核证 L396–415](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/.claude/commands/create_plan_generic.md#L396-L415)。
- [H05：implement_plan，mismatch、phase manual stop、信任 checkmarks](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/.claude/commands/implement_plan.md#L21-L84)。
- [H06：create_handoff 的紧凑 critical references 与状态产物](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/.claude/commands/create_handoff.md#L43-L64)；[resume_handoff 的旧状态/当前核证对照 L80–115](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/.claude/commands/resume_handoff.md#L80-L115)。
- [H07：validate_plan 的实际代码/声明完成/观察面](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/.claude/commands/validate_plan.md#L30-L80)。
- [H08：thoughts-analyzer 的历史 relevance/decision-vs-proposal/implemented 区分](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/.claude/agents/thoughts-analyzer.md#L8-L54)。
- [H09：Thoughts sync 的实际 Git 外部副作用](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/hlyr/src/commands/thoughts/sync.ts#L32-L99)；[hardlink 索引 L169–195](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/hlyr/src/commands/thoughts/sync.ts#L169-L195)；[Git hooks L218–259](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/hlyr/src/commands/thoughts/init.ts#L218-L259)。
- [H10：本地 approval create / auto modes / persisted action](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/hld/approval/manager.go#L29-L115)；[明确 tool_use_id L289–375](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/hld/approval/manager.go#L289-L375)。
- [H11：Go MCP 的创建→注册→事件等待 / 无 timeout / header / 内存 listener](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/hld/mcp/server.go#L138-L260)。
- [H12：旧 TS MCP local daemon 与 persisted status polling](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/hlyr/src/mcp.ts#L13-L177)。
- [H13：eventBus 内存订阅与满队列 drop](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/hld/bus/events.go#L12-L24)；[Publish L81–125](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/hld/bus/events.go#L81-L125)。
- [H14：daemon restart 孤儿状态处理](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/hld/daemon/daemon.go#L341-L387)；[相应静态测试](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/hld/daemon/daemon_orphan_test.go#L11-L88)。
- [H15：SQLite pending-only 审批更新](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/hld/store/sqlite.go#L2865-L2905)；[静态重复决定测试](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/hld/store/sqlite_approval_test.go#L53-L88)。
- [H16：WUI 通知输出路径与 returned ID](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/humanlayer-wui/src/services/NotificationService.tsx#L198-L246)；[OS 权限/失败 fallback L330–366](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/humanlayer-wui/src/services/NotificationService.tsx#L330-L366)。
- [H17：ralph_impl 的危险 permission mode 与外部动作链](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/.claude/commands/ralph_impl.md#L19-L33)；[oneshot L5–6](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/.claude/commands/oneshot.md#L5-L6)。
- [H18：apps daemon 空实现](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/apps/daemon/src/router/sessions.ts#L1-L6)；[packages thoughts schema](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/packages/database/schema/thoughts.ts#L11-L47)；[apps react 文档 UI](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/apps/react/src/App.tsx#L16-L65)。
- [H19：根 LICENSE](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/LICENSE#L1-L15)；[hlyr package 许可 L60–61](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/hlyr/package.json#L60-L61)。
- [H20：case study 作者的结果声明](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/docs/case-studies/healthcare-case-study.md#L7-L15)。
- [H21：workshop 自述、外链理论与特定平台假设](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/docs/workshop.mdx#L1-L28)；[RPI 操作例 L54–127](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/docs/workshop.mdx#L54-L127)。
- [H22：根 CLAUDE 的旧 SDK 分区声明](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/CLAUDE.md#L7-L40)；[仍指旧 SDK 的 TS quickstart](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/docs/quickstart-typescript.mdx#L7-L19)；[当前 CLI 注册（未注册 README 中的 contact_human / mcp serve）](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/hlyr/src/index.ts#L31-L96)。

TPW 引用均以基线 `1f95f06` 的真实路径/上述行号为固定来源；UCBIP 事件的原件/证据强度沿用 TPW 已落盘的 `docs/research/2026-10-05-ucbip-practice.md`，本轮没有重读 UCBIP 现场，因此没有产生新的 UCBIP 运行证据。

[H01]: https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/README.md#L1-L3
[H02]: https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/humanlayer.md#L1-L5
[H03]: https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/.claude/commands/research_codebase.md#L28-L84
[H04]: https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/.claude/commands/create_plan_generic.md#L179-L276
[H05]: https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/.claude/commands/implement_plan.md#L21-L84
[H06]: https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/.claude/commands/create_handoff.md#L43-L64
[H07]: https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/.claude/commands/validate_plan.md#L30-L80
[H08]: https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/.claude/agents/thoughts-analyzer.md#L8-L54
[H09]: https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/hlyr/src/commands/thoughts/sync.ts#L32-L99
[H10]: https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/hld/approval/manager.go#L29-L115
[H11]: https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/hld/mcp/server.go#L138-L260
[H12]: https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/hlyr/src/mcp.ts#L13-L177
[H13]: https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/hld/bus/events.go#L12-L24
[H14]: https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/hld/daemon/daemon.go#L341-L387
[H15]: https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/hld/store/sqlite.go#L2865-L2905
[H16]: https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/humanlayer-wui/src/services/NotificationService.tsx#L198-L246
[H17]: https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/.claude/commands/ralph_impl.md#L19-L33
[H18]: https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/apps/daemon/src/router/sessions.ts#L1-L6
[H19]: https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/LICENSE#L1-L15
[H20]: https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/docs/case-studies/healthcare-case-study.md#L7-L15
[H21]: https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/docs/workshop.mdx#L1-L28
[H22]: https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/CLAUDE.md#L7-L40
