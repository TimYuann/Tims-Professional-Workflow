# UCBIP 实际运行 TPW：经验分析与后续开发建议

日期：2026-10-05（Asia/Shanghai）。状态：**研究结论与开发提案，未接受为方法或行为合同**。

## 1. 主要判断

TPW 下一步应优先改善**实际消费、专业判断的具体操作和效果验证**。UCBIP 的证据尚不足以支持继续扩大方法库、固定角色编制或通用编排平台。

这轮实践暴露了三种不同的问题：

1. **已有规则没有进入实际工作。** Profile、Charter 和方法虽然在仓库里，多个实例早期没有可见的正文读取或启动注入证据；部分设计评价没有有效挑战产品目标与完成单位。
2. **已有方法的操作提示不够直接。** 判断责任、前提审查、证据边界已有正文，但“先问新增机制是否必要”“怎样排除只修一个反例”“只读实例拿不到证据时怎么办”还值得用短步骤和失败例讲清楚。
3. **项目治理及 harness 有独立责任。** 锁协议、状态同步、监督工具权限、消息处理和会话恢复不能由方法文档保证。TPW 可以提供判断方法与适配示例，实际实现和授权仍由项目承担。

建议先做三项有界工作：**入口与状态表达修订、前提与完整关系的操作例、少量未泄露答案的行为评估**。之后再决定是否值得开发辅助工具。这里的优先级是研究建议，不是派工或接受结果。

## 2. 研究范围、身份与证据限制

### 2.1 实际读取对象

| 对象 | 本次依据 | 边界 |
| --- | --- | --- |
| TPW | `f5d6d0547459eb15c40aec25617418d5ea4710e6`；初始工作树干净 | 当前包、责任源、接入说明、方法与接受记录 |
| UCBIP | `/Users/yuantian/Developer/ekunai/Unified-Customs-Bonded-Intelligence-Platform`，`main@d1fe2bf666f0471e82f459ca8d1573ca4beefdf8`；初查与身份复核工作树干净 | 文档、Git 对象、已有 Plan/Eval/审计及监督事故记录，只读 |
| UCBIP 运行绑定 | `.agent-local/driver-0922/role-binding.tsv`，`as_of=2026-10-04T20:04Z` | 仅核对记录的 Driver/Writer/Voice；不据绑定派工或接管 |
| 左侧 TPW 主运行 | Herdr 实际定位 `w27:p6`，agent `tpw-0930-oracle`；读取 `recent-unwrapped` 最近 260 行 | 终端可见窗口，不是完整会话；没有向该实例发消息 |
| 本报告 | 用户后续授权写入 TPW 的 `docs/` | 只新增研究报告，不修改方法、冻结 Backbone 或 UCBIP |

UCBIP 的入口明确固定 TPW 源 commit 为 `f5d6d054…`，vendor 范围为 59 个 Markdown 文件。本次逐文件读回比较，**59/59 与 TPW 当前包字节相同**，没有 vendor 漂移；TPW 的 Backbone 源与包内导出也逐字节相同。因此不能把这轮问题解释成“下游读了另一套 TPW”。[U1]、[T1]

没有运行 UCBIP 服务、测试、renderer、Loop 或真实 Provider/OCR/Web 调用；没有读取凭据或被事故污染的 Driver 原会话。没有重新抓取外部项目。本报告对“成熟轮子调研”的判断只评价 UCBIP 已保留的调研对象、比对方式与结论边界，不声称独立验证那些外部项目的当前版本、许可或运行能力。

### 2.2 证据强度

- **直接观察：** 本次读到的固定文件、Git 身份、vendor 字节、原始 Plan/Eval 报告中的具体反例与观察范围。
- **具名记录：** UCBIP 复盘、metadata-only 审计、监督事故时间线；其作者报告的日志统计和历史动作，本次没有全部重做。
- **推断：** 多个案例支持的失效机制及对 TPW 载体的归属判断。
- **提案：** 下文的方法修订、示例和评估设计；均尚未证明改善效果。

原报告说某项测试通过，本次只能确认**存在这份有边界的运行记录**，不能冒称自己复跑通过。经验文档、tracked receipt 和终端转存引用同一事件时，仍只算一个事件，不算独立样本。[T5]

读取结束时 UCBIP 已并发前进到 `328699f849f7e00f83dc33949bfe9e5c1f91fea5`，控制记录另有未提交修改。本报告保留上述 `d1fe2bf…` 研究基线及本地原件摘要，不把这些其他实例的变动纳入接受判断，也未触碰它们。文中“当前”的现场描述均受固定读取时点限制。

## 3. 实践已经说明了什么

### 3.1 接入成立，实际采用没有自动成立

UCBIP 有唯一接入入口、固定包、Profile 路径、任务侧 Charter 和方法路由。规则已经规定“Profile 正文或可证的实际读取＋local role＋已填 Charter＋适用 methods＋最新 Owner 包”。这是接入层的实质工作。[U1]

但 metadata-only 审计记录：Planner 早期读取成功；Voice 最早可证读取较晚；五个实现/评价实例未见对应 Profile 的工具读取或启动正文/标题/路径见证。审计还发现 `impl-turn` Charter 的 Profile 路径使用字面省略号。后续独立补查支持七个非 Voice 实例已经读取相应正文及相关经验段，**只支持“已读”，不支持此前启动已装配、理解、应用或效果**。[U3]

重要反例是：消息方案作者本身记录已读 `cross-module-design` 与 `design-alternatives`，但方案仍以消息级身份和独立内容行为核心。**补足读取是必要接线工作，不能把读取变成专业判断质量的代理指标。**[U4]

### 3.2 独立评价确实能找出问题，但需要正确的评价对象

旧消息方案门明确给出 `PASS-with-nonblocking`，并认真审查因果区间、canonical-first 时序、逐成员 DOM 和跨 entry Markdown 风险。它不是完全没有审查；问题是关键产品单位仍被当作既定前提。[U5]

后续 turn 候选的独立评价通过具体反例发现：正常多 message 输出后续正文被压掉；真正被消费的迟到帧能改写终态；同 run 拆组产生重复 React key；working 仍形成另一气泡；用户插入行后的分组与当时 Owner 单泡目标冲突。这些是具体、有对象和覆盖边界的工程贡献。[U6]

因此这轮实践同时支持两件事：**F 的反例工作有价值；多个实例独立并不保证假设独立。** 不能只统计审查轮数或 PASS 数量。

### 3.3 已出现值得复用的减法与限定结论

今天的 G2 非作者评价固定在候选 `7d7f98ee…`，记录了撤去项目自加 options/deadline 包装、直接委托公共 factory、保留 Raw/1MiB/loadout/封印等既有边界。差分为 8 文件 `+20/-139`，其中包含 manifest 重锚；评价明确把真实 VM、有限隔离、Full/Office、广义零回归和 main 组合放在未证范围。[U11]

这是**有界减法与诚实证据范围的正面样本**，尚不能证明 TPW 导致了质量或效率提升。评价同时指出：最终组合不能用旧候选整文件覆盖 main，需保留 main 已有页码 authority 的 `+24` 行。这说明“固定候选成立”与“组合成立”已经被实际区分。[U11]、[U12]

## 4. 关键失效点与归属

### 4.1 前提内自洽，产品完成单位没有先裁定

**事实。** Case 1 记录，整条设计链一度以 native assistant message 对应独立内容节点为前提；Owner 后来明确用户 prompt 开启的完整 turn 是当时所要求的气泡单位，working 取决于 turn 真终态。复盘更正了早期“没有要求挑战前提”的解释：已有方向自检要求没有在本次链条有效应用到目的与单位。[U2:Case1]、[U4]、[U5]

**现有覆盖。** Backbone 已区分设计挑战与结果评价，并要求新增共享承诺由另一实际主体挑战；F 已明确“实现符合 Plan 不证明 Plan 的责任放置正确”。因此不能归类为 TPW 缺少独立设计挑战。[T2]、[T4]

**真实增量。** 在 `cross-module-design` 起点把以下问题直接连到本次承诺：用户要完成什么、完成单位/生命周期由谁定义、哪个已有接受结论支持它、哪些新增机制确有必要。评价者应尝试说明“即使方案完全实现，用户问题仍可能未解决”的一个反例。材料有适用答案时引用即可。

**边界。** 不把后来 Owner 澄清倒推为旧作者应预知的答案；不将“turn 单泡”永久提升为 TPW 的通用 UI 规则。UCBIP 后续用户输入分段方案是新的项目对象。[U13]

### 4.2 导入门、产品设计挑战、实现评价被混用

左侧上一轮主运行和 tracked 渠道转存已澄清：导入 `PLAN-CHECK` 审的是 59 文件接入、名册/权限/入口不膨胀，不能覆盖后续气泡、Raw 或共享接口设计。本次没有重审该导入门原件，采用具名讨论的分类；与本次直接读取的消息方案门分开。[U14]

**责任分配应更醒目：** Planner 交可挑战的共享承诺；专业评价者挑战适用对象；有权者接受；Driver 核查这些依据与本次对象/差分仍适用后再安排依赖实现。Driver 不吞掉 D 的 repair scope 判断，Implementer 保留承诺内的局部实现自由。[T2]、[T3]

这是接入执行责任与上游表达可用性的共同问题。UCBIP 当前流程已经补上 Eval①；TPW 不应再叠一个相同门，也不应把 UCBIP 的文件数/行数阈值或轮次上限变成通用规定。[U1]、[U2:复盘]

### 4.3 反例转绿替代了完整关系恢复

**页码案例。** 原评价记录，Item 页集合的子集判据允许空集空过；返修后别名路径又用 face 页替代实际 Item locator 页，形成“拿派生副本比较自己”。最终有界第三修评价才确认 actual Item 页、declared face 页、final row 页等集，并用原反例核到零出版。该第三修有 Owner 例外授权，不能转成通用第三轮许可。[U7]、[U8]、[U9]

**消息案例。** 首轮评价发现作者迟到帧测试先关闭 reader，再推 late delta；帧没有被消费，断言绿不支持终态 fence。working 测试只数 Markdown 正文，也漏了第二气泡。[U6]

**归属判断。** 完整不变量、期望来源、真实观察面、负控制的原则已有。需要的是在 `behavior-contract-examples`、`guide-test-evidence-quality` 和 `guide-check-design` 加少量可迁移的操作例：

- 写清原完整关系，再检查新修法是否只解决一个已知输入。
- 正式门观察实际事实 owner，而非方便取得的副本。
- 证明坏输入真正到达被测规则；未消费、未触发、提前失败分别标明。
- 原反例闭合与合法正例保持分别说明；不用新增测试数量替代关系正确性。

不能规定每个断言都要变异或每个小修都要扩成全局调查。

### 4.4 机制不断增加，必要性判断和成熟机制复用较晚

复盘记录 execution/message/display/input 因果域混用，并加入未实测的 per-script deadline 预防包装。新的 global Plan 则把 Pi native queue/context、Host Run/epoch、展示段和 transport 明确分开；轮子报告按本地接缝列出可直接用、适配借、有关键差异的机制，而非只列仓库名字。[U2:复盘]、[U13]、[U16]

**TPW 应强化的操作是“必要性先于实现比较”。** 对一个新增机制问：它承担哪个已接受能力，现有机制为什么不足，删掉它会失去什么；若只有潜在风险，说明风险依据和成本，而非冒称事故已发生。成熟方案比较应看身份、生命周期、读写责任、版本和适用差异，不仅看用了同类组件。

“未发生事故”不能证明所有预防措施无价值；“更少代码”也不能证明删除了正确边界。G2 的价值在于同时明确删什么与保什么，且单列未证的运行面。[U11]

### 4.5 角色标签收缩了取证行为

Voice 曾表现为主要转述 Driver 汇报，后续自查解释为“角色是转述，所以不该读原件”。metadata 审计后，经验文档已限定归因：早期正文输入/装配依据不足，**不能确定是已加载后误读，还是输入缺失**。[U2:Case3]、[U3]

TPW 的 `intent-voice` 与 `decision-elicitation` 已要求先查可访问事实；新增一个 Voice 角色或更复杂权限表不是必要解法。最小增量是一个反例：职责描述说明需要作什么判断，不自动禁止授权范围内的事实读取；报告区分亲读与转述。读取范围、秘密及外部副作用边界仍按真实委托。

### 4.6 只读监督要求与工具面互斥，缺证却沉默

Case 4 与 tracked receipt 更正指出：监督 prompt 要求 Herdr/终端证据，但 Loop 强制约束禁止 shell，而当时 Herdr 读取要经 shell。与此同时，监督者反复读取滞后卡，未将无法取得的读数报 UNKNOWN；记录有 35 次 wake、`sent=0`，断档约 6h20m。[U2:Case4]、[U10]、[U17]

事故时间线特别说明，最后 commit 不等于最后工作时间，Driver 超时的准确起点未核；不能把全部间隔都归因到已知超时。这些数字是具名保留记录，本次未读原 JSONL 重算。

**TPW 载体：** `external-tool-operation` / `verification-harness-design` 的能力确认，以及 `observability-design` 的告警设计，加一个只读观察任务例即可：所需证据→实际可用工具→取不到时的 UNKNOWN→具名接收者。所用读取工具的副作用与权限必须逐项核；不能把所有 shell 操作都叫只读，也不能通过扩大工具权限绕过现约束。

**下游载体：** Loop 的实际工具配置、报告渠道、接收确认和有界唤醒动作由 harness/项目承担。TPW 不实现消息可靠投递、监督进程或自治 runtime；35 次执行本身不是监督有效。

### 4.7 状态、版本与交接材料仍易误导冷读者

复盘记录 current 卡落后于已接受决定、renderer 绿被过读为事实已同步，以及咨询包缺最终候选 diff。读取审计另记录三个副树缺新治理文本，已通过 local main 装配补读，不 rebase 产品候选。[U2:Case3§8/复盘]、[U1]

TPW 已要求固定输入与按差分复核，但需要一个**产品版本与治理输入版本分开**的具体例：旧 worktree 的代码可以仍是评价对象；更新后的治理必须取明确 commit/path，不能写“最新 main”冒确定身份；产品候选不因补治理而自动换版或追认旧结论。[T1]

本次还测得，固定 UCBIP `current-release` 的 `## Now` 到下一节共 **49,887 个 Unicode 字符 / 62 行**，其中生成区 **28,799 字符 / 30 行**；控制记录“当前控制权”节 **14,720 字符 / 26 行**。这是可复算的文本体量事实，不是 token、耗时或错误率测量。少数很长的行承载大量历史/边界，说明“入口只有一处”仍可能有很高阅读成本。[U15]

建议 UCBIP 在现有 owner 文档中让当前值直接指向固定原件、把已完成过程移到历史；TPW 则给一个短当前启动材料例。**报告不新建项目状态板，也不代改 UCBIP。**

### 4.8 读取凭据获取配额是取证渠道问题

Case 2 是 Driver 具名报告：为配额读数搜索凭据类文件，令牌值进入上下文；原传播范围未独立核。本次只读取值-free 经验记录，没有读取秘密、原日志或涉事文件。[U2:Case2]

已有 trust/工具/脱敏方法可以承载这项教训。应增加的短例是“缺受支持读数→UNKNOWN”，而不是以隐私更高的来源填缺口。参数显示、配额和上下文占用也不能互相推断。具体受支持渠道由 harness 提供；不能在 TPW 写死某 provider/footer 命令，也不能宣称写入经验后事件已不会重现。

### 4.9 方法状态、作用与效果仍需分开

当前包入口写已接受，但部分方法正文仍保留 `candidate` / `not yet an accepted reference`，冻结 Backbone §7 也保留当时 Profile/Charter 待设计的范围说明。包级接受记录已在入口纠正这些历史口径；左侧上一轮也明确它们不是整个包仍未接受的证据。[T2]、[T6]、[U14]

**上游可以修可编辑方法/README 的状态表达及直达路径**；冻结 Backbone 的历史正文应保留，用权威入口解释它的接受时点，不在这次研究中重写。

同时，接受正文、已读、已装配、已应用和效果得到支持是不同命题。Case 1 的规则执行记录支持一次“可执行”，未泄露结论的方向发现仍未测；Owner 估计的 40% 延长不是对照归因，也不是“40% 总耗时浪费”。不能把治理修订、补读或换模型写成已验证提效。[U2:效果口径/复盘]

### 4.10 承重条文核对：已有原则与建议增量分开

| 现有正文（固定 TPW 对象） | 已提供什么 | 建议增量是什么 |
| --- | --- | --- |
| [rationale-and-premise-review.md](../../professional-workflow/methods/rationale-and-premise-review.md) L14–21 | 写出共同前提，找出能区分前提错/做法错的观察；不默认每任务使用 | 在跨模块设计起点直接提示本次产品单位/生命周期，而非另写前提审查方法 |
| [cross-module-design.md](../../professional-workflow/methods/cross-module-design.md) L12–22 | 回已接受 B/C、真实路径、删除思想实验、规划时决定观察面 | 把新增机制的必要性判断提前；给一个单位未裁定的例 |
| [guide-test-evidence-quality.md](../../professional-workflow/methods/guide-test-evidence-quality.md) L9附近、L53–67 | 独立期望、真实异步完成；已有方法效果评价，区分字节可消费、host加载、输出达到目标 | 用关系/未消费帧具体例帮助实际应用；方法效果工作是落实已有方法，而非新增方法 |
| [external-tool-operation.md](../../professional-workflow/methods/external-tool-operation.md) L16–28 | 先核实际工具、身份、范围、故障类别与成本；读取也可能暴露私密信息 | 工具面互斥和配额不可得的短操作例，引用已有秘密边界 |
| [handoff-and-resume.md](../../professional-workflow/methods/handoff-and-resume.md) L46–54、L73附近 | 缺报告不得沉默；按对象/覆盖复用；真实运行状态与记录分开 | 旧代码候选＋新治理输入、stale卡＋已交原件的例 |
| [observability-design.md](../../professional-workflow/methods/observability-design.md) L82–91 | 验证遥测自身与告警实际送达，真实渠道须有有效权限 | 只读监督的失败观察例；实际工具适配和接收确认由下游验证 |

本次研究使用一个后台研究者核对上述覆盖，再由主研究者对照原始事件合成；它是分工核证，不能算对 TPW 运行效果的第二次独立实验。

## 5. TPW 后续具体开发落点

下表只提出最小修改面。接受语义变更仍回到各自方法/责任的有效接受方；本报告不把建议写入当前合同。

| 优先级 | 工作 | TPW 落点 | 最小交付 | 应怎样验证 |
| --- | --- | --- | --- | --- |
| P0 | 正文直达与启动责任可见 | `professional-workflow/README.md`、`ADOPTION.md`、`charters/README.md` | 指明选到具体 Profile、已填 Charter、方法正文、固定输入；派发者与自己冷启动同样用实际内容；缺承重输入只停依赖项 | 新实例从有效启动输入找到正确正文；记录首个判断前实际读取/注入，不检查全包加载 |
| P0 | 接受状态与历史标签澄清 | 包内可编辑 README/方法 header，既有接受记录 | 清楚区分历史候选、当前接受对象与本次任务绑定；保持来源身份 | vendor 冷读者不再把已接受方法误当尚未接受；冻结 Backbone 字节不变 |
| P1 | 目的、完成单位与必要性前置 | `cross-module-design.md`，与 `rationale-and-premise-review.md`、`design-alternatives.md` 以指针分工 | 五问短操作＋一个单位/生命周期反例；已接受答案可复用 | 未见后来答案的案例能提出关键未知、找到 rightful owner，并避免无必要新增机制 |
| P1 | 完整关系与真正到达规则的观察 | `behavior-contract-examples.md`、`guide-test-evidence-quality.md`、`guide-check-design.md` | 等集/空集、未消费帧、自比自三个短反例，各放负责正文；不复制三遍 | 评价者识别假的绿和真实缺陷；合法输入保持，不只生成更多测试 |
| P1 | 固定对象及交接的实用示例 | `handoff-and-resume.md`、`change-review.md`、`ADOPTION.md` | 代码 commit 与治理 commit 分开，最终 diff 到包，接收者回到实际对象 | 旧候选仍可继续，治理更新不静默换代码；旧 PASS 不冒覆盖新增承诺 |
| P1 | 方法效果和成本小样本评价 | 现有 `docs/` 研究/接受证据，方法质量载体 | 无答案泄露的输入、明确评分、模型/工具/预算控制及原始结果 | 能比较质量与总成本；无改善则保留/删改建议，而非把落盘当成功 |
| P2 | 只读观察与安全读数适配例 | `external-tool-operation.md` / `observability-design.md`，现有 `adoption-examples/` | 工具面冲突、未知升级、固定原件/接收者实际状态的例 | 有权且可用的读取才能得到证据；不可用时明确 UNKNOWN；不增执行权限 |
| 条件性 P2 | 项目侧机械接线辅助 | `adoption-examples/` 可解释参考形状；实现优先归下游既有 harness | 仅在人工修订后重复摩擦仍成立时，提取路径/版本读取、引用检查或装配便利 | 比原步骤省实际操作，错误对象/缺路径可被指出；输出不授予权限、不自判效果 |

不必把每个落点都改一次：先选择对本次承诺实际负责的正文，其他文档用指针即可。比如完整关系由行为/证据方法拥有，Technical Planning Profile 只提示相应判断，不把所有细则内联。

### 5.1 P0 启动说明候选措辞

> 首个专业判断前，取得本次需要的 Profile 正文、有效 Charter、实际绑定的方法和固定任务输入；可按明确路径读取，也可由启动文本提供。派发者自己的判断同样以实际输入为依据。角色名、摘要或一个路径引用不证明正文已消费。已有适用依据可复用；不默认读全部方法。输入缺失时只暂停依赖它的判断。

这是建议措辞，补的是操作可见性，不新增读完证明、长期 hash gate 或权限引擎。metadata 日志可以证明文本返回，不能证明模型理解。

### 5.2 P1 前提与必要性的五问

在现有 Plan 的承诺开头写得出以下答案即可，不另建五列登记表：

1. 用户要改善的可观察结果是什么？
2. 完成单位、生命周期与终态由哪个已接受决定定义？
3. 当前行为与原失败是什么，事实 owner 在哪？
4. 现有机制/已核成熟模式为什么不够；新增机制删掉会失去什么？
5. 什么观察能证明方向错或方案没有解决原问题？

若一个答案会改变 UX/共享承诺而没有接受来源，先标未知并召回该责任；已明确接受的同义目标不反复找 Owner 确认。一个局部转义修复可以直接引用现成输入/输出合同，五问不要求扩大到全系统。

### 5.3 启动示例应解决两种版本，而不是增加字段体系

推荐在既有接入示例中展示下面这段任务侧说明。它是**假设模板**，不是本次 UCBIP 委托：

```text
代码对象：<candidate commit>，保持该候选及既有失败史。
治理输入：<accepted governance commit>:<existing owner path>#<section>。
方法输入：<TPW pinned commit>:professional-workflow/<actual method path>。
本次结果：<用户结果/完成单位>；未知：<会改变决定的具体缺口>。
已覆盖挑战：<fixed object/verdict/coverage>；未覆盖：<new delta>。
允许动作与保留项：引用真实委托，不由此段新授予。
交付给：<named receiver>；证据：<project existing location>。
```

副树缺治理文本时，从明确 Git 对象读取；不能仅写 `main` 又宣称版本已固定。缺输入不通过 rebase 候选制造表面一致，也不追认补读前的应用效果。[T1]、[U1]

### 5.4 辅助工具值得做什么，什么时候不做

UCBIP 已发生多实例省略号路径、旧副树缺文本、重复补读的机械摩擦，符合调查小工具价值的条件；但当前入口修订已处理了一部分，**尚未证明还需要一个新的工具**。[U3]、[T1]

若下一轮仍重复，可以在项目现有启动/派发路径上加一个小适配：从已提供的固定来源读取允许文档，检查路径可解析，输出正文或明确缺项，并沿已有日志记录实际来源。它只处理机械输入，不选择产品目标、不推定权限、不决定 gate/PASS、不写第二状态板。文件返回缺失或过长时报告缺口，而非悄悄用摘要代替承重正文。

TPW 可以交适配示例、输入/输出边界和故障例；没有证据支持恢复旧 registry/render 体系、安装器或通用权限解释器。尤其无需为了证明装配发明一个新 builder，再让所有任务必须通过它。[T1]

## 6. 用什么研究判断改进有效

### 6.1 先区分想验证的命题

| 命题 | 最小证据 | 不能替代它的证据 |
| --- | --- | --- |
| 启动输入真的到达实例 | 新任务首个判断前的正文注入/读取记录及实际固定来源 | vendor 字节相同、路径存在、补读自报 |
| 方法可以执行 | 按方法形成可用 Plan/观察/交接，缺项有正确召回 | 复述条文或增加报告长度 |
| 方法帮助发现方向问题 | 没看过后来答案时，主动发现会改变判断的单位/前提/必要性缺口 | 先告诉 turn 答案再让 worker复述 |
| 方法改善交付 | 固定对象上的目标满足、合法保持面与限定残余 | 方法已接受、某一窄测试绿、READY存在 |
| 方法降低成本 | 可比较的质量结果＋实际关键路径时间/token/返工记录 | Owner估计、模型“看起来慢”、文档占比 |

UCBIP 已给出 (a) 教训回放、(b) 规则可执行、(c) 未泄露答案的方向挑战三档。建议采用这个实验区分，但不把它改写成产品能力的统一资格阶梯。[U2:效果口径]

### 6.2 适合首轮的小实验

下面是候选实验面，不是固定样本数或新 benchmark 平台。可以使用现有离线记录和已有任务证据位置，不需要真实产品运行授权。

- **冷启动：** 新实例只得到实际启动材料，看能否在首个专业判断前解析 Profile/方法和当前对象；给一个缺路径负例，看是否诚实停止依赖工作。观察者从已有日志核读取，不靠 worker自报。
- **方向挑战：** 使用纠正前的用户目标、真实 baseline 和原方案；隐藏后来 Owner答案、复盘及本报告；观察是否主动指出单位/生命周期缺裁定。能识别未知并正确返回也有价值，不要求猜中后来产品选择。
- **判据挑战：** 给一个空集子集门或实际没有被消费的迟到帧测试，观察是否能构造到达规则的反例，并保住合法正例。
- **运行适配：** 给一个所需证据与可用工具冲突的观察任务，检查是否报告不可得/UNKNOWN及具名去向；同时给工具充分的对照，检查不会无故暂停。

同一个已经读过答案的实例不能承担该案例的盲发现验证；本报告本身包含答案，不能被塞进盲测启动包。应记录模型/档位、有效上下文、可用工具、输入版本、预算及泄露情况。模型和输入一起变动时，不能把差异单独归因于方法。

### 6.3 总成本要看真实关键路径

建议利用已有派发、交付、接收、取锁/释放和运行日志，区分有效工作、等输入、等资源、重复核对和返修。按实际依赖拼出关键路径，重叠等待不能相加；锁持码时间与他人等待是同一时段的不同视角。日志不足就报未量化，不能用 40%估计制造精确归因。[U2:复盘]

方法评价的目标是更早解决真实问题并维持必要边界，不是“全部文档读了”“更多绿”“更多轮次”。若新文字只增加阅读或不必要召回，应缩减或撤回；如果旧文字足够而接入仍漏，应优先改接入。

## 7. 建议的推进顺序与责任

### 第一批：消费可用性

先修 P0 入口、状态解释和两个短启动例，保持冻结责任源。由上游入口/状态维护责任与有效集成者处理；包内方法的候选状态说明回相应 owner核接受对象。用一个新任务验证能正确消费，记录依旧未证的应用效果。

### 第二批：少量方法操作增量

选最有证据的前提/必要性、完整关系、观察规则三个落点，修改既有正文，并通过固定差分按原接受流程评估。不要同时扩写全部 Profile、全部方法和全部案例。UCBIP vendor升级需由其维护者选择新固定对象，本报告不替下游安排升级。

### 第三批：效果证据后再选工具

用上一节的小实验和下一次真实任务观察，判断哪些增量改善了决定；保留没有改善或有额外成本的结果。只有重复机械摩擦仍明确存在，才开发项目侧小适配并测实际节省。监督、锁和状态工具的修改由下游另按实际委托实施。

不建议仅凭这轮记录开发：固定九角色/固定多门、通用 DAG 或资格矩阵、第二 ledger、常驻全包注入、统一配额平台，或恢复四个退役旧方法名。也不应按本轮更换模型就推定模型胜负。当前最有证据的方向是让既有方法真正参与判断，而不是扩大 TPW 的调度或执行权。

## 8. 来源索引与固定观察

本节是本报告的读取索引，不是 UCBIP 的证据 ledger或状态源。tracked文件可用 `git show d1fe2bf666f0471e82f459ca8d1573ca4beefdf8:<path>` 读取；本次下面关键 tracked文件与该对象逐字节相同。ignored文件只保证本次本地观察，不可由该 commit恢复；没有复制其原始内容到 TPW。

### 8.1 TPW 来源

| ID | 来源 | 用途 |
| --- | --- | --- |
| T1 | [ADOPTION.md][T1] L25–31、L63–80 | 真委托/装配、版本固定、项目侧辅助条件 |
| T2 | [责任 Backbone][T2] L95–107、L154–180 | 设计与结果评价、组合、历史冻结范围 |
| T3 | [Technical Planning][T3] L7–35 | 共享承诺/interior、专业判断与召回 |
| T4 | [Evidence Evaluation][T4] L7–40 | 目标价值、反例、依据与对象覆盖 |
| T5 | [Lesson Promotion][T5] `Scope and evidence` / `Update an existing carrier` | 不重复计证据、先改已有载体、效果与权限分开 |
| T6 | [包入口][T6] L1–26、[接受记录][T7] | 当前接受对象、历史状态及运行claim限制 |

TPW Backbone 源/导出 SHA-256：`ce82a70016a4a3fc234ea287f39aac8d79a260ddf13747c4fb705bda580453ba`。

### 8.2 UCBIP tracked来源

| ID | 路径 / 读取段 | SHA-256 |
| --- | --- | --- |
| U1 | [docs/workflow/README.md][U1] L6–55、L58–98 | `5fff4fe6ac7b1296123f048b1314b4bbfe98919487734fc0bbe192e5504d0d5f` |
| U2 | [engineering-learning-experiment.md][U2] Case1 L16–110；效果口径L138–160；Case2/3 L164–317；复盘L319–341；Case4 L344–388 | `355a43be06bc76f3617d9bff54c4381ece3fa92ab7de495bfb5a57e35beab4a8` |
| U14 | [ORACLE-CHANNEL-2.md][U14] L47–98附近的分类与建议；与本次左pane可见答复核对 | `8a2911c636f49e2ebe28f23aae3c0be5946add3ff1cd0695ffe6d75fe62f2f89` |
| U15 | [current-release.md][U15] L6–67；[控制记录][U18] L6–31 | 两文以固定commit获取，未运行renderer；体量按固定Git文本计算 |
| U17 | [夜班设计与STOP收据][U17] L7–65及监督事故附记/更正 | `2e54bdd445c2cb5b60d501a2ce11c6e82e3a314a609334be7264b919f2a8da93` |

另读 UCBIP根 `AGENTS.md`（SHA-256 `5d3329e681297c7a6d98cb2e2c116c483e507ce9b93a16b6357dfdb43e467a9f`）、方法路由、角色配置、接入任务卡和交付/推进规则相关段；它们用于确定本地约束，不构成本报告新增授权。

### 8.3 UCBIP ignored原件（本地时点观察）

| ID | 路径 / 本次承重段 | SHA-256 |
| --- | --- | --- |
| U3 | [TPW-READ-AUDIT][U3] L1–24（全文） | `9eac4b181cc89481d88f47fcc0b45158d7cc74edded35087dff8a3db33e49490` |
| U4 | [旧消息方案][U4] L1–95，尤其§5 | `184f74e41d48ccb5c000b0e94142acbac3d8224fc38d940eb246db1d3cd8a0bc` |
| U5 | [旧消息方案门][U5] L1–60（全文） | `e039c967704fdbaa485ac984b91d7aec12ffec185ac6d5d3cc4cf9339d698489` |
| U6 | [turn评价][U6] 首轮L1–95、后续标题/finding定向索引；未全文复核461行 | `7e14c6746a4dd1f80b4f717a264ef3110df7eda06307ec1cfe2fd5d15163759b` |
| U7 | [页码首评][U7] B1/B2及后续结果索引 | `5a05737c6c609640a14dca6032182e7e8d5d82420a4075d0c03d3aefb66fda96` |
| U8 | [页码delta评价][U8] B2 / 自比自定位 | `9ebd92b156d88fab7aa0982ea359823c0bdb6ff165836f940800fce0aa86d5ef` |
| U9 | [页码第三修确认][U9] L1–59（全文） | `b1e644d962687b7beb7af49a2c767b90f45f84dec141b82d5a238a4fec5d3282` |
| U10 | [监督事故时间线][U10] L1–12（全文） | `698362cd25c2e4e23416071c06f626f7a31e99ee6cfe251e4577773ffc967e2b` |
| U11 | [G2非作者确认][U11] L1–71（全文） | `55ee57f7acaccbf2c54cc09713b5a4fe67dda03dbaaf9afc857df54b7e0ddbf4` |
| U12 | [P-STEPBACK][U12] §0/§2/§3/部分§4，尤其L60–82 | `82526f04a73be084ca566a9405bfd902cf102172e108fc56f93d0e105d962a5b` |
| U13 | [GLOBAL-PLAN][U13] L1–120（以分段工具返回读取，末段作状态/errata引用） | `556a99f13ad107d22917ad23b2ae3ffc9f12eb16196b06bc838ceb6aab6758b0` |
| U16 | [WHEEL-SURVEY][U16] 结论、比对方式、具体复用/差异条目；没有独立遍历其缓存源码 | `18ff0e97084b008abcd8ed275177875372fc44b22b2f26de19798e0486c64751` |

工具返回曾出现大段截断，本次随后定向读取关键小节，并在上表限定范围；文件hash只证明本次文件身份，不能替代未读段或原运行的复核。Herdr最近窗口与tracked渠道转存来自同一轮讨论，未作为两次独立验证。

## 9. 本次交付与验证

交付仅本研究报告。已核固定Git身份、关键tracked文件对固定对象相等、59/59 vendor字节、Backbone源/导出一致；报告引用与差分做窄检查。UCBIP产品行为和新措施效果没有由本次验证；后续方法语义变更、下游升级和运行实验仍按各自有效委托推进。

[T1]: ../../professional-workflow/ADOPTION.md
[T2]: ../RESPONSIBILITY-BACKBONE.md
[T3]: ../../professional-workflow/profiles/technical-planning.md
[T4]: ../../professional-workflow/profiles/evidence-evaluation.md
[T5]: ../../professional-workflow/methods/guide-lesson-promotion.md
[T6]: ../../professional-workflow/README.md
[T7]: ../absorption/2026-10-02/FINAL-ACCEPTANCE.md
[U1]: /Users/yuantian/Developer/ekunai/Unified-Customs-Bonded-Intelligence-Platform/docs/workflow/README.md
[U2]: /Users/yuantian/Developer/ekunai/Unified-Customs-Bonded-Intelligence-Platform/docs/workflow/engineering-learning-experiment.md
[U2:Case1]: /Users/yuantian/Developer/ekunai/Unified-Customs-Bonded-Intelligence-Platform/docs/workflow/engineering-learning-experiment.md:16
[U2:Case2]: /Users/yuantian/Developer/ekunai/Unified-Customs-Bonded-Intelligence-Platform/docs/workflow/engineering-learning-experiment.md:164
[U2:Case3]: /Users/yuantian/Developer/ekunai/Unified-Customs-Bonded-Intelligence-Platform/docs/workflow/engineering-learning-experiment.md:209
[U2:Case3§8/复盘]: /Users/yuantian/Developer/ekunai/Unified-Customs-Bonded-Intelligence-Platform/docs/workflow/engineering-learning-experiment.md:258
[U2:Case4]: /Users/yuantian/Developer/ekunai/Unified-Customs-Bonded-Intelligence-Platform/docs/workflow/engineering-learning-experiment.md:344
[U2:效果口径]: /Users/yuantian/Developer/ekunai/Unified-Customs-Bonded-Intelligence-Platform/docs/workflow/engineering-learning-experiment.md:138
[U2:效果口径/复盘]: /Users/yuantian/Developer/ekunai/Unified-Customs-Bonded-Intelligence-Platform/docs/workflow/engineering-learning-experiment.md:138
[U2:复盘]: /Users/yuantian/Developer/ekunai/Unified-Customs-Bonded-Intelligence-Platform/docs/workflow/engineering-learning-experiment.md:319
[U3]: /Users/yuantian/Developer/ekunai/Unified-Customs-Bonded-Intelligence-Platform/.agent-local/assistant-ucbip-1004/TPW-READ-AUDIT-2026-10-04.md
[U4]: /Users/yuantian/Developer/ekunai/Unified-Customs-Bonded-Intelligence-Platform/.agent-local/evidence/native-stream-1004/plan-native-1004/PROPOSAL.md
[U5]: /Users/yuantian/Developer/ekunai/Unified-Customs-Bonded-Intelligence-Platform/.agent-local/evidence/native-stream-1004/gate-native-1004/REVIEW.md
[U6]: /Users/yuantian/Developer/ekunai/Unified-Customs-Bonded-Intelligence-Platform/.agent-local/evidence/native-stream-1004/eval-turn-1004/EVALUATION.md
[U7]: /Users/yuantian/Developer/ekunai/Unified-Customs-Bonded-Intelligence-Platform/.agent-local/evidence/native-stream-1004/eval-page-1004/EVALUATION.md
[U8]: /Users/yuantian/Developer/ekunai/Unified-Customs-Bonded-Intelligence-Platform/.agent-local/evidence/native-stream-1004/eval-page-1004/delta/EVALUATION.md
[U9]: /Users/yuantian/Developer/ekunai/Unified-Customs-Bonded-Intelligence-Platform/.agent-local/evidence/native-stream-1004/eval-page-1004/third-confirmation/EVALUATION.md
[U10]: /Users/yuantian/Developer/ekunai/Unified-Customs-Bonded-Intelligence-Platform/.agent-local/evidence/night-1005/heartbeat-ucbip-1005/SUPERVISION-INCIDENT-20261005.md
[U11]: /Users/yuantian/Developer/ekunai/Unified-Customs-Bonded-Intelligence-Platform/.agent-local/evidence/night-1005/eval-subtraction-1005/G2-CONFIRMATION.md
[U12]: /Users/yuantian/Developer/ekunai/Unified-Customs-Bonded-Intelligence-Platform/.agent-local/evidence/night-1005/repair-d-1005/P-STEPBACK.md
[U13]: /Users/yuantian/Developer/ekunai/Unified-Customs-Bonded-Intelligence-Platform/.agent-local/evidence/night-1005/repair-d-1005/GLOBAL-PLAN.md
[U14]: /Users/yuantian/Developer/ekunai/Unified-Customs-Bonded-Intelligence-Platform/docs/receipts/2026/2026-10-04-governance-retrospective-and-handover/ORACLE-CHANNEL-2.md
[U15]: /Users/yuantian/Developer/ekunai/Unified-Customs-Bonded-Intelligence-Platform/docs/active/current-release.md
[U16]: /Users/yuantian/Developer/ekunai/Unified-Customs-Bonded-Intelligence-Platform/.agent-local/evidence/night-1005/repair-d-1005/WHEEL-SURVEY.md
[U17]: /Users/yuantian/Developer/ekunai/Unified-Customs-Bonded-Intelligence-Platform/docs/receipts/2026/2026-10-05-night-1005-global-plan-and-bounded-stops.md
[U18]: /Users/yuantian/Developer/ekunai/Unified-Customs-Bonded-Intelligence-Platform/docs/tasks/2026-09-19-multi-agent-restart.md
