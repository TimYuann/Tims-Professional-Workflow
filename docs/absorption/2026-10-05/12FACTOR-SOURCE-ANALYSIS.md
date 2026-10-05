# humanlayer/12-factor-agents：TPW 下一轮吸收分析

日期：2026-10-05。状态：研究子报告，候选处置；没有修改或接受 TPW 方法，没有运行来源程序。

## 结论

12-factor 的价值在于**把 agent 的有效输入、控制边界和恢复状态变成应用可检查的工程对象**，而不是给 TPW 增加十二个阶段或一个运行框架。TPW 已有装配、按需正文、未知结果、独立评价、恢复和单真源纪律；结合 UCBIP，最适合优先吸收的是两三个操作例：有效启动输入如何到达实例、失败怎样形成下一步可区分的观察、工具选择与执行之间怎样保留真实委托边界。[F02]、[F03]、[F08]、[T-adoption]、[T-agenttext]、[U-start]

本次没有发现可直接搬入 TPW 的运行组件。来源的模板可以说明机制形状，但不能由源码存在推出 durable、生产可靠或改进效果已证明。尤其 Factor 12 主要由图表达；实码 `Thread` 原地修改 `events`，不是一个已验证的纯 reducer 实现。[F12]、[C-agent]

## 1. 对象、读取和缺证

- 源：`https://github.com/humanlayer/12-factor-agents`，固定 commit `d20c728368bf9c189d6d7aab704744decb6ec0cc`；本地 `.worktrees/source-intake-2026-10-05/12-factor-agents`。读取后 `git status --short` 为空。
- TPW：`1f95f0650638b6b6fbc892dcb697dbad4da86fa4`。下列参与比对的 12 个 TPW 文件已逐字节对固定对象核同：`ADOPTION.md`、`guide-agent-text`、`handoff-and-resume`、`external-tool-operation`、`trust-boundary-and-actions`、`local-defect-feedback-loop`、`interface-contract-and-retry`、`domain-state-and-invariants`、`decision-elicitation`、`bounded-composition`、Driver Profile，以及 UCBIP 实践报告。另定向读了 `observability-design` 与 `uncertainty-planning`，不把其内容当新的来源增量。
- 源读取：根 README、CLAUDE；根 LICENSE 的许可身份与再分发段；canonical Factor 01–12 全部 Markdown、Appendix 13 全文；旧 Factor 1–9 全部一行文件；`img/1c0-stateless-reducer.png`、`img/1c5-agent-foldl.png` 静态图；模板 `src/{agent,state,server,cli,a2h}.ts`、`baml_src/agent.baml`；模板 README 的机制相关章及文本检索；对 `workshops/2025-07-16/walkthrough` 做了 error/retry/idempotency 等定向搜索，未逐个审计 workshop 实现。
- README 指向补零的 `factor-01…09`，旧 `factor-1…9` 每个只有一行 `Moved to …`，不是第二份同义正文，不计两次来源或证据。[S-nav]、[S-old]
- 没有安装依赖、运行 BAML eval、编译、测试、服务、SDK、Provider 或 webhook；没有联网扩读视频、作者访谈、图片中的 X 原帖或 README 的外链。因而运行表现、模型收益、生产耐久性和外部经验主张均未验证。
- `CLAUDE.md` 的 persona 激活、至少读 1500 行、每 5–10 分钟 commit 等是被研究仓库的来源资料。本次未将其作为 TPW 或研究者的指令，也不建议复制。[S-claude]

## 2. 来源实际主张，与能由代码确认的机制

### 2.1 Own prompts/context：透明有效输入，比角色标签更重要

Factor 2 要求提示词由应用拥有、当作代码，可以测试、评价和迭代；其 BAML 只是一个模板例，不是 BAML 依赖要求。Factor 3 把 instructions、检索材料、历史、tool results、memory、output schema 都列为 context，并允许应用自行选择存储格式与给模型的投影。作者明确没有给出最优格式；XML、single-user-message、减少 token 和角色技巧均不能据此升级成 TPW 规范。[F02]、[F03]

模板能证实：`baml_src/agent.baml` 的 `DetermineNextStep(thread)` 有显式 prompt、schema 和若干声明的 eval；`Thread.serializeForLLM()` 把事件转换为 XML 风格片段后送入该函数。这是有效输入具有可见载体的实例，不证明此序列化在嵌套对象、敏感数据或注入文本上可靠，也不证明这些 eval 已通过。[C-prompt]、[C-agent]

对 TPW 的实际价值是接到现有 `ADOPTION` 装配步骤和 `guide-agent-text` assembly check：核本次承重正文是否真的被注入或读取，而不是 Profile 名、路径存在或 vendor 字节相同。UCBIP 报告已说明“已读”仍不等于“已应用”，所以不能仅以记录了 prompt 就声称专业判断改善。[T-adoption]、[T-agenttext]、[U-start]

### 2.2 Tool output 与执行分离：不是模型提出就自动执行

Factor 1/4 把自然语言到结构对象作为一个独立可采用的模式；模型产生 intent，应用选择怎样执行。Factor 6/8 特别要求可以在工具选择和实际 invocation 之间暂停；暂停可能因等待信息、长任务或真实保留决定，三者不能混为每动作必须人工批准。[F01]、[F04]、[F06]、[F08]

模板 `agentLoop` 的可证行为是：先把 `nextStep` 放入事件，再对 clarification、done、manager request、divide 返回；add/subtract/multiply 进入 deterministic handler。CLI 对 divide 呈现对象，得到 approval 后才执行，并把拒绝意见作为事件送回。这里 divide 被称作“scary”是教学政策，不是风险判据；按回车批准是这个 CLI 的 UX 选择，不应移植为 TPW 的同意规则。[C-agent]、[C-cli]

现 TPW 已区分工具权限、有效委托、保留决定与未知状态，并明确现有有效授权不需重新确认；Driver 也明确不拥有进程/队列/重试。适合借一个**选择已形成但动作尚未发生**的反例，说明有条件的 checkpoint，而不新造批准角色、通用人工 gate 或调度权。[T-driver]、[T-actions]、[T-elicitation]、[T-handoff]

### 2.3 人类联系是显式交互对象；durable 闭环需要下游保证

Factor 7 给出 `question/context/options`，保存 thread 后联系接收者，回复带 thread ID 恢复；同文明确“总是 JSON”可能没有性能收益。Factor 11 的 Slack/email/SMS/event/cron 是产品接入设想，不是接入权、发送权或人工介入即安全的证明。[F07]、[F11]

模板 `FileSystemThreadStore` 存 JSON 和 LLM 投影文本，并从 JSON 重建 Thread；server 描述 `conversation.created`、`human_contact.completed`、`function_call.completed` 三类入口。代码能说明持久对象/关联 ID/回复反馈的设计意图，不能支持 exactly-once、受信回复、并发安全和 crash durability 等运行保证。[C-state]、[C-server]

一个具体静态缺口是：`ThreadStore.get` 声明返回 `Promise<Thread | undefined>`，server L83 却未 `await`；`create/update` 同样声明异步，server L115–119 未等待，并把 `create` 的返回值赋给 `string | undefined` 变量。本次没有编译或运行，所以只报告**读到的异步合同不匹配**，不声称复现了服务故障。也因此不把该模板作为“暂停恢复已可用”证据。[C-state]、[C-server]

对 UCBIP 只读监督事故，值得借的是问题/对象/接收者/待回复状态明确，而实际通知、回复认证、重新进入和执行能力由已有 harness 担责。TPW 已有这些边界；来源没有解决“工具面禁止 shell 导致无法取证”的现场约束，也不能替监督者获得发送权限。[U-supervision]、[T-tool]、[T-elicitation]

### 2.4 State/reducer：减少重复状态，不改变事实与接受权

Factor 5 建议能从事件历史推导的 execution state 尽量不另建一套；它本身也说分开有时有价值。此处作者的“business state”指 tool/message/result 历史，并非 TPW 的已接受领域合同、事实来源或风险接受。把上下文 window 视作权威会误读该建议，特别是模型输入可以有选择、压缩或隐藏已解决错误。[F05]、[F03]

Factor 12 Markdown 只有标题、两张图和前后导航；图表达 `context → Determine Next Step → Handle Next Step → new context` 以及 foldL 比喻。它没有完整的重放语义或 durability 合同。模板的可变事件数组也没有证明 reducer purity。因此建议仅把“选择逻辑与副作用 handler 分开”当下游可比对的表示方案，不能要求 TPW 或 UCBIP 把状态迁入新 event store。[F12]、[C-agent]

TPW 已有 `domain-state-and-invariants` 的状态/转移/guard/并发与 failure questions，以及 reducer/command/event 的可选表示；`bounded-composition` 已区分 canonical object、派生视图、单 writer 与耐久性。这里主要是同义覆盖，真实增量需要一条已观察到的重复状态 drift 及为何现源不足；不能让报告或 agent context 替代项目当前真源。[T-domain]、[T-composition]、[U-state]

### 2.5 Errors/focused agents/prefetch：局部工程手段，不是固定配额

Factor 9 将错误格式化入 context，让模型尝试调整；连续错误可由 deterministic code 有界停止或升级，三次是源例，不是通用预算。本文所谓 compact errors 主要是**让失败成为下一轮输入**，并不展示已实现的稳定摘要算法。模板核心 loop 没有这套异常捕获/错误计数机制，不能据 Factor 9 文档宣称代码具备它。[F09]、[C-agent]

TPW 的 defect feedback loop 已要求观察、区分假设、原失败复跑，并把错误文本视作不受信数据；external tool method 已区分 transient、refused、missing capability 和 unknown outcome。适合补的是一条“有结果但未获确认，先查状态”的 agent feedback 例，避免每个 exception 都让 LLM再试，更不能把 unknown 的副作用重发当 self-healing。[T-defect]、[T-tool]、[T-interface]

Factor 10 的价值是按实际领域与可评价结果控制范围，源的 3–10 或 20 steps 是作者经验性建议，未给可复查基准。TPW 已要求真实独立性、注意力跨度及按单位配置实例，也明确减少过度 fanout；不能从小 focused agents 推出每任务要拆更多代理、固定角色编制或硬步数上限。[F10]、[T-driver]、[T-composition]

Appendix 13 对高概率必需工具输出建议确定性预取，以减少模型 roundtrip。它可以解释 UCBIP 启动正文到达问题的一个装配选择，但“可能需要全部上下文”的标题不应覆盖 TPW 按需正文：只预取当次确需、授权可读、版本已固定的输入，保留数据来源和缺失状态。对动态状态仍要在消费时检查 freshness，不能预取秘密或以缓存保证事实有效。[F13]、[T-adoption]、[T-agenttext]

## 3. 机制级候选处置

下表中的 merge/narrow/defer/skip 是**本次研究建议**：merge＝并入已有载体的同义支持/短例；narrow＝只保留适用子机制；defer＝待项目需要和验证后再考虑；skip＝不导入。不是 Git merge、已接受方法或执行安排。

| 候选 | 建议 | 既有落点与最小交付 | 可证伪验证 / 失败条件 |
| --- | --- | --- | --- |
| F2/F3：可见的有效启动输入 | **merge，P0** | `ADOPTION` §2/§5 与 `guide-agent-text` Assembly check；在现 cross-module startup 例增加实际注入/实际读取二选一，沿已有记录指出来源；不新建 prompt registry。[T-adoption]、[T-agenttext] | 给正文充分/缺承重方法/字面占位路径三个冷启动输入，首个专业判断前能正确读入或报依赖缺口；只报告路径或后补阅读算失败。仍单列“读到≠应用”。[U-start] |
| F13：必需输入的确定性预取 | **narrow，合入上述例** | 按当前任务已选 Profile/Charter/method/path 预取，仅展示一种 harness 装配方式；不全包常驻、不自动选择方法。[F13]、[T-adoption] | 同模型、任务、预算比较实际 roundtrip、承重信息保留和结果；更长输入、错误对象或 stale cache 抵消收益时取消这项建议。 |
| F4/F6/F8：选择与 invocation 的可暂停边界 | **narrow，P1 操作例** | `external-tool-operation`/`trust-boundary-and-actions` 的已有动作边界；checkpoint 操作留在 `handoff-and-resume`，只引用，不复制三遍。[T-tool]、[T-actions]、[T-handoff] | 已授权继续、缺保留决定、等待工具结果、未知副作用四个分支：只有依赖缺项的分支暂停；恢复不重复已发生的动作，也不为已覆盖授权再问人。 |
| F7：显式问题、接收者、关联对象、回复状态 | **merge/narrow，P1** | `decision-elicitation` 的问答/记录/恢复例；渠道形状放已有 adoption example。报告“已发/待回复/未知”按现证据，不造新状态台账。[F07]、[T-elicitation] | 以只读监督取不到证据/可取得证据对照：缺证时给 UNKNOWN 和具名去向；已有事实不问人；没有发送授权则交付待发对象而非声称通知成功。[U-supervision] |
| F9：错误进入下一次判断，并由真实操作语义限制恢复 | **narrow，P1** | `local-defect-feedback-loop` 的反馈例，retry/unknown 指针继续归 `interface-contract-and-retry`；不采用源的固定三次。[T-defect]、[T-interface] | transient 调整、权限拒绝、missing tool、unknown-after-write 四类输入；同请求盲重发或不断重试拒绝算失败。原始信号必须能从处理后表示追回。 |
| F10：围绕可完成/可评价单位控制 scope | **merge，低增量** | `bounded-composition`/Driver 已有范围与注意力规则。最多加来源锚点，不加 Profile、slot 或步数规定。[F10]、[T-driver]、[T-composition] | 一个边界清楚的小任务无需拆分仍完成；一个真实跨度不足/独立性冲突的任务才拆。若 agent 数增多但质量/成本无益，停止增加规则。 |
| F5/F12：单事件历史、恢复 reducer | **defer 给下游；TPW 正文以 skip 新方法为先** | 现 `domain-state-and-invariants` 已有状态/reducer选型；只有具体 drift 需消除时，由项目设计比较 canonical state/derived views。[T-domain]、[T-composition] | 在项目已有授权环境验证重复/乱序/中途崩溃/恢复及 accepted state 与 projection一致；源码存在或 JSON可存取不算通过。此轮未跑。 |
| F11：Slack/email/SMS/cron 接入；模板 runtime/SDK/BAML | **defer/skip** | 渠道有产品需要再由下游处理；不在 TPW 引入部署、service、凭据、事件 store、webhook 或通知平台。[F11]、[T-driver] | 只有真实项目委托、渠道能力、接收方/动作权限及具体恢复合同齐备才有验证对象；本轮无该委托，不用安装测试“增强证据”。 |
| 源的 always JSON/XML、role hacking、scary divide、固定步数/重试数、CLAUDE persona纪律 | **skip** | 非通用专业判断增量，或源码/文字未提供有效性证据；保留作为来源观察，不成为 TPW指令。[F02]、[F03]、[F07]、[F09]、[F10]、[S-claude] | 若未来有人主张性能收益，需独立模型/任务/输入版本、控制组、真实输出/总成本；本次没有这类证据。 |

优先级应沿 UCBIP 已有建议推进：先确认启动输入消费；再选一两个有实际反例的方法操作例；盲案例验证有效后才决定项目辅助脚本。12-factor 支持“取小机制进入现产品”的思路，不能替代这项效果验证，也没有证据支持 TPW 恢复退役 registry/render、统一流程平台或新 authority。[S-intent]、[U-development]

## 4. 许可对象与吸收边界

根 README L4–7 标出 **Code Apache 2.0 / Content CC BY-SA 4.0**，L254–258 再明确“all content and images”属 CC BY-SA 4.0、“code”属 Apache 2.0；根唯一 `LICENSE` 文本是 Apache 2.0。应据 README 的对象区分记录来源，不能因为根 LICENSE 是 Apache 就把 factor 正文、翻译或图统一登记为 Apache。[S-license]、[S-apache]

本报告仅作事实核对：没有扩读 CC 官方法律文本，没有对“某一具体改写是否构成 adaptation”、代码嵌在文章中的许可适用、或与 TPW 许可的兼容性作完整法律判断。正式复制、翻译、改编正文/图片时，需要把署名、来源、修改及适用许可落实到对应载体；具体处置应由集成者按实际拟导入对象核定。本轮分析不复制图、不 vendor源码、不宣称已完成许可吸收。

建议尽量以可验证机制与 TPW 现有正文的短例消化，并保留固定来源锚点；但“只用自己的话改写”本身不是解除 CC 义务的结论。许可记录与专业语义接受、运行效果、下游动作授权各自不同。[S-license]、[T-adoption]

## 5. 固定来源索引

上游 GitHub 链接全部固定 source commit；TPW/UCBIP实践报告使用仓内相对路径，其固定依据为上述 TPW commit，亦可用 `git show <pin>:<path>` 恢复。相对路径当前可点击，不代表未来工作树始终维持该历史版本。

[S-nav]: https://github.com/humanlayer/12-factor-agents/blob/d20c728368bf9c189d6d7aab704744decb6ec0cc/README.md#L55-L71
[S-old]: https://github.com/humanlayer/12-factor-agents/blob/d20c728368bf9c189d6d7aab704744decb6ec0cc/content/factor-3-own-your-context-window.md#L1
[S-intent]: https://github.com/humanlayer/12-factor-agents/blob/d20c728368bf9c189d6d7aab704744decb6ec0cc/README.md#L181-L191
[S-claude]: https://github.com/humanlayer/12-factor-agents/blob/d20c728368bf9c189d6d7aab704744decb6ec0cc/CLAUDE.md#L3-L43
[S-license]: https://github.com/humanlayer/12-factor-agents/blob/d20c728368bf9c189d6d7aab704744decb6ec0cc/README.md#L254-L258
[S-apache]: https://github.com/humanlayer/12-factor-agents/blob/d20c728368bf9c189d6d7aab704744decb6ec0cc/LICENSE#L90-L129
[F01]: https://github.com/humanlayer/12-factor-agents/blob/d20c728368bf9c189d6d7aab704744decb6ec0cc/content/factor-01-natural-language-to-tool-calls.md#L3-L60
[F02]: https://github.com/humanlayer/12-factor-agents/blob/d20c728368bf9c189d6d7aab704744decb6ec0cc/content/factor-02-own-your-prompts.md#L13-L89
[F03]: https://github.com/humanlayer/12-factor-agents/blob/d20c728368bf9c189d6d7aab704744decb6ec0cc/content/factor-03-own-your-context-window.md#L12-L233
[F04]: https://github.com/humanlayer/12-factor-agents/blob/d20c728368bf9c189d6d7aab704744decb6ec0cc/content/factor-04-tools-are-structured-outputs.md#L29-L50
[F05]: https://github.com/humanlayer/12-factor-agents/blob/d20c728368bf9c189d6d7aab704744decb6ec0cc/content/factor-05-unify-execution-state.md#L3-L38
[F06]: https://github.com/humanlayer/12-factor-agents/blob/d20c728368bf9c189d6d7aab704744decb6ec0cc/content/factor-06-launch-pause-resume.md#L17-L27
[F07]: https://github.com/humanlayer/12-factor-agents/blob/d20c728368bf9c189d6d7aab704744decb6ec0cc/content/factor-07-contact-humans-with-tools.md#L17-L66
[F08]: https://github.com/humanlayer/12-factor-agents/blob/d20c728368bf9c189d6d7aab704744decb6ec0cc/content/factor-08-own-your-control-flow.md#L10-L84
[F09]: https://github.com/humanlayer/12-factor-agents/blob/d20c728368bf9c189d6d7aab704744decb6ec0cc/content/factor-09-compact-errors.md#L5-L83
[F10]: https://github.com/humanlayer/12-factor-agents/blob/d20c728368bf9c189d6d7aab704744decb6ec0cc/content/factor-10-small-focused-agents.md#L5-L39
[F11]: https://github.com/humanlayer/12-factor-agents/blob/d20c728368bf9c189d6d7aab704744decb6ec0cc/content/factor-11-trigger-from-anywhere.md#L3-L15
[F12]: https://github.com/humanlayer/12-factor-agents/blob/d20c728368bf9c189d6d7aab704744decb6ec0cc/content/factor-12-stateless-reducer.md#L3-L10
[F13]: https://github.com/humanlayer/12-factor-agents/blob/d20c728368bf9c189d6d7aab704744decb6ec0cc/content/appendix-13-pre-fetch.md#L3-L147
[C-agent]: https://github.com/humanlayer/12-factor-agents/blob/d20c728368bf9c189d6d7aab704744decb6ec0cc/packages/create-12-factor-agent/template/src/agent.ts#L8-L114
[C-prompt]: https://github.com/humanlayer/12-factor-agents/blob/d20c728368bf9c189d6d7aab704744decb6ec0cc/packages/create-12-factor-agent/template/baml_src/agent.baml#L30-L167
[C-state]: https://github.com/humanlayer/12-factor-agents/blob/d20c728368bf9c189d6d7aab704744decb6ec0cc/packages/create-12-factor-agent/template/src/state.ts#L7-L48
[C-server]: https://github.com/humanlayer/12-factor-agents/blob/d20c728368bf9c189d6d7aab704744decb6ec0cc/packages/create-12-factor-agent/template/src/server.ts#L59-L153
[C-cli]: https://github.com/humanlayer/12-factor-agents/blob/d20c728368bf9c189d6d7aab704744decb6ec0cc/packages/create-12-factor-agent/template/src/cli.ts#L67-L133
[T-adoption]: ../../../professional-workflow/ADOPTION.md
[T-agenttext]: ../../../professional-workflow/methods/guide-agent-text.md
[T-driver]: ../../../professional-workflow/profiles/driver.md
[T-actions]: ../../../professional-workflow/methods/trust-boundary-and-actions.md
[T-tool]: ../../../professional-workflow/methods/external-tool-operation.md
[T-handoff]: ../../../professional-workflow/methods/handoff-and-resume.md
[T-domain]: ../../../professional-workflow/methods/domain-state-and-invariants.md
[T-composition]: ../../../professional-workflow/methods/bounded-composition.md
[T-defect]: ../../../professional-workflow/methods/local-defect-feedback-loop.md
[T-interface]: ../../../professional-workflow/methods/interface-contract-and-retry.md
[T-elicitation]: ../../../professional-workflow/methods/decision-elicitation.md
[U-start]: ../../../docs/research/2026-10-05-ucbip-practice.md
[U-supervision]: ../../../docs/research/2026-10-05-ucbip-practice.md
[U-state]: ../../../docs/research/2026-10-05-ucbip-practice.md
[U-development]: ../../../docs/research/2026-10-05-ucbip-practice.md
