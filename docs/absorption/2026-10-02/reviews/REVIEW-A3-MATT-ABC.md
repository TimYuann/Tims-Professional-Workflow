# REVIEW-A3-MATT-ABC

裁定者：tpw-absorb-gate；2026-10-02。状态：源机制裁定完成，可按下述边界蒸馏；不是正式正文接受、运行有效性证明或集成许可。

## 固定对象与独立性

- 包：commit `021ac07621edbb6105d9e24d81de2763b1c487e1` 的 `docs/absorption/2026-10-02/packages/A3-MATT-ABC.md`；读取工作字节 blob `9615ae63087f0052ff45017c278e3ba943254911`。
- 产品：`800414dd9eb517f7132223866fe484d28a8bbf0b:professional-workflow`，tree `7c814e54c5e775045bc1c5155e3c181ceb1345fb`。开始审核时当前 HEAD 的该子树相同，无工作区产品差分。
- 源：本地 `../legacy-pre-night-2026-10-01/upstreams/mattpocock-skills`，HEAD `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`，Git status 无差分。下文源路径均相对此仓和此 pin，产品路径均相对 `professional-workflow/`。
- 我未编写 A 包或被审产品，只回源、比较和给约束；本记录不是可直接替换产品的正文。B 写成后的固定差分仍需独立审核。

回读承重源：`tdd/{SKILL.md,tests.md,mocking.md}`、`to-spec/SKILL.md`、`to-tickets/SKILL.md`、`triage/{AGENT-BRIEF.md,OUT-OF-SCOPE.md}`、`domain-modeling/{SKILL.md,ADR-FORMAT.md,CONTEXT-FORMAT.md}`、`codebase-design/{SKILL.md,DEEPENING.md,DESIGN-IT-TWICE.md}`（均在 `skills/engineering/`）；`skills/productivity/writing-for-agents/{SKILL.md,SKILL-MECHANICS.md}`、`grilling/SKILL.md`、`grill-me/SKILL.md`；`skills/engineering/ask-matt/PHASE-BOUNDARIES.md`、`setup-matt-pocock-skills/{SKILL.md,domain.md,triage-labels.md}`、`implement/SKILL.md`、`code-review/SKILL.md`；另读 `scripts/link-skills.sh` 与 `skills/in-progress/setup-ts-deep-modules/{SKILL.md,dependency-cruiser.config.cjs}`。支持 docs 回读与本裁定有关段落：`docs/engineering/{tdd,to-tickets,triage,domain-modeling,setup-matt-pocock-skills}.md` 和 `docs/productivity/{grilling,grill-me,writing-for-agents}.md`；未将截断的批量输出记作全文已读。

产品回核：三方法、mock guide、方法选择入口、六个相关 Profile、Charter template/README，以及已读冻结 Backbone 的 E/F、Voice/Driver 与交接条款。未重新审查所有 21 文件的接受资格。

## 总裁定

11/11 机制组完成实质裁定：吸收 1（MG-2），合并 3（MG-3/7/11），限缩吸收 7（MG-1/4/5/6/8/9/10）；没有因缺源退补的组。11 组都含可蒸馏内容，但不等于 11 个知识增量或新文件。组内已覆盖部分明确保留，不重复算增量。未执行源脚本、真实工程 fixture、访谈或模型行为实验，未作效果 PASS。

### MG-1 · red-before-green

- **覆盖：部分。** `methods/local-defect-feedback-loop.md` §Use/Method 已覆盖既有缺陷的失败观察→修复→回归；`profiles/implementation.md` §心智模型 已保留局部重构和测试接缝判断。新增行为的一步 red→green 操作尚无方法正文。
- **采纳：限缩吸收。** 取 `skills/engineering/tdd/SKILL.md` §Rules of the loop、§Anti-patterns 的先失败、失败原因核对、一个行为小步实现和不批量预写想象结构。可追溯预期来自接受约定/独立 worked example；red 必须因目标行为未兑现，而非依赖安装、fixture 或 harness 故障。
- **边界：**测试是约定的可执行表达和证据，不生成或接受新的 B/C 契约。E 自测不等于独立 F。源将 refactoring 移至 review 的决定及其 docs 原因可记录为源取舍，不能升级为所有任务禁止 E 在绿态下作授权内局部重构；也不强制另开 review session 才能重构。慢 browser/e2e 路径按反馈成本、风险与真实 claim 选择，不一律后写、不一律禁用。已有适用失败观察可复用。
- **落点：**新 `methods/test-first-behavior-slice.md` 的 Use、Loop、Limits；MG-3 的测试质量参照独立支持正文；`profiles/implementation.md` §按需方法入口 和 `methods/README.md` 加指针。保留 local-defect 的既有入口，避免扩大成普遍 TDD gate。
- **仍需补读：无承重缺口。** B 需读上述源；验证红因正确、实现变绿与局部重构保持行为的例子即可，不声称总体收益已证实。

### MG-2 · vertical slice / wide refactor

- **覆盖：部分前提，操作未覆盖。** `methods/cross-module-design.md` §Method 5–6 有 Plan 和兼容偏好；缺完整窄路径、demo 问题和 expand–migrate–contract 的依赖顺序。
- **采纳：吸收。** `skills/engineering/to-tickets/SKILL.md` §Draft vertical slices、wide-refactor exception 与 `docs/engineering/to-tickets.md` §Tracer bullets/§Wide-refactor exception 提供可操作的分解与例外。每份行为工作问“本项完成能独立展示/验证什么”，列实际阻塞边，不以层完成冒充行为完成。
- **边界：**不要求不存在的 schema/API/UI 层，也不判所有基础设施/准备项为坏 ticket；此类工作说明支撑的后续行为与自身可检验结果。prefactor 只限使本次变更容易的必要工作、在授权内安排，不强制每任务先重构。宽机械迁移保留 additive expand、按影响批量 migrate、最后 contract；无法单批绿时明确仅集成对象承诺绿，不能把失败中间件称作已通过。共享分支是可选实现安排，不提供建分支、迁移或删除权限。不存在固定 context-window 容量保证。
- **落点：**新 `methods/change-slicing.md` 的 Behavior slices、Dependencies、Wide refactors、Limits；`profiles/technical-planning.md` §按需方法入口 与 `methods/README.md` 索引。消费方按任务调用，不附 tracker 发布。
- **仍需补读：无。** 蒸馏至少保留一对层拆分/可验证路径例子和宽迁移的无法单批绿例外。

### MG-3 · test anti-patterns

- **覆盖：部分。** F Profile 的负控制提问、mock guide 的接口和替身规则已有；两类具体诊断及修复例子不足。
- **采纳：合并。** 取 `tdd/SKILL.md` §Anti-patterns 与 `tdd/tests.md` §Good/Bad Tests 的 oracle 来源检查、行为不变而内部重构导致测试坏掉的信号、side-channel vs 被测接口例子；与 MG-1 共用支持正文，F 可直接调用。
- **边界：**实现耦合不等于“绿是构造出来的”，它主要损害可维护性或验证了别的 claim；不能统称证据无效。相同公式的预期增加共同错误风险，不严格保证任何实现版本下永远绿；literal 若抄自实现也不独立。调用次数/DB 查询/内部 seam 在其本身就是接受 claim（例如持久性、禁止重复调用）时可以正当，不全禁。内部实现可自测，不能冒称外部行为覆盖。报告证据缺陷与产品 FAIL 分开。
- **落点：**新 `methods/guide-test-evidence-quality.md` 的 Oracle、Coupling、Examples，供 MG-1 与 `profiles/evidence-evaluation.md` 方法指针引用。`behavior-claim-evaluation.md` §Method 3 只需短引用，不把比较专用方法扩大为完整测试审查。
- **仍需补读：无。** 正文需有 correlated oracle、合法持久化观察反例，避免仅复述禁令。

### MG-4 · observation surface / seams

- **覆盖：实质部分已覆盖。** `cross-module-design.md` §Method 3–4 与 mock guide §Rules 3/5 已约束表面、依赖形状、production adapter 覆盖；缺观察位置的说明与跨交接追踪，不缺接缝拥有者的责任定义。
- **采纳：限缩吸收。** 取 `to-spec/SKILL.md` §Process 2、`tdd/SKILL.md` §Seams、`docs/engineering/tdd.md` 的“解释每个 seam 能抓住/漏掉什么与成本”的操作；提早表达关键行为怎样观察、既有表面优先、减少无贡献测试表面。
- **边界：**拒绝“每个 seam 是 B 人类冻结项、未经人类确认禁止任何测试、F 只准用已约定 seam”的移植。Backbone 明确 E 拥有承诺内局部测试接缝，F 可设计证据。B 决定可观察承诺，D 决定共享技术表面，F 判断覆盖；任何 seam 变更先按其是否改变依赖承诺/验证依据判断召回，不默认 Owner ACK。最高 seam/目标一个是取舍启发，adapter mapping 与端到端行为可能需多个表面；不能牺牲 claim 覆盖换计数。
- **落点：**`cross-module-design.md` §Method 3–5 的表面说明/Plan handoff；新行为方法 §Seam choice；Charter 的既有 Accepted inputs/Deliver 可引用相关决定，无新必填 schema。
- **仍需补读：无。** 保留“一外部行为+一生产 adapter”需两个表面的反例；无需复核只用了某一个 seam。

### MG-5 · falsifiable acceptance conditions

- **覆盖：部分。** B Profile 已要求可区分对错，F 已有 falsifiable claim；逐条件检查和工作项依赖归属未充分操作化。
- **采纳：限缩吸收。** 保留每条件指出使其不成立的观察、核基线、区分本项可达结果/其他工作依赖/空洞复述。**纠正锚点：**包引用 `docs/engineering/triage.md` 的关键句不存在；实际为 `docs/engineering/to-tickets.md` §Common questions，L76–77；`triage/AGENT-BRIEF.md` §Complete acceptance criteria 支持独立可验证。
- **边界：**只有新增/改变能力的增量条件应预期基线不满足。保持契约/兼容条件常已在基线为绿，仍须守住；`AGENT-BRIEF.md` 自己的“短描述保持不变”就是反例。不可因为基线绿删除保持条件。跨项 outcome 可有效作为上层接受条件；子任务应明确依赖，不把未归本项兑现的结果算作本项已交付。并非每个条件必须已有可执行自动测试。
- **落点：**新 `methods/behavior-contract-examples.md` 的 Acceptance conditions，B Profile 只指针；MG-2 可引用此检查。载体应容纳条件/预期/例子与反例，不再向 Profile 内联全部正文。
- **仍需补读：无；**正确源已自行查明，不退 A。保留 baseline-red 增量、baseline-green 保持、外部依赖三例。

### MG-6 · decision and rejection memory

- **覆盖：责任/接受记录已有，ADR 与拒绝检索操作未覆盖。** Backbone 共用接口和 Voice 已要求接受状态；B/C Profile 有决定记录占位，不能说记录纪律整体不存在。
- **采纳：限缩吸收。** 取 `domain-modeling/SKILL.md` §Offer ADRs sparingly、`ADR-FORMAT.md` §Template/What qualifies、`triage/OUT-OF-SCOPE.md` §Writing the reason/When to check/When to write：有实际 trade-off、难逆且反直觉时选择 ADR；最小足够的 why；按概念合并历史拒绝、永久拒绝与资源暂缓区分，已实现不记为拒绝。保留源中 maintainer 可确认、重新考虑或判为不同概念的三路，而非自动拒绝新请求。
- **边界：**三个筛选条件决定是否值得独立 ADR，不能消除既有授权/接受/审计必须记录的决定。1–3 句是默认起点，足以传达条件、理由、有效 owner/状态才可收口，不硬限长度。编号/路径遵从已有 owner docs；不要求独立文件或 sequential numbering。既有接受记录不可因源的“删除旧拒绝”而抹去历史；变更以适用状态/替代关系明确保留。记录不产生 C/D/B 权限。
- **落点：**新 `methods/decision-record.md` 的 When to record、Minimal record、Rejected/deferred concepts、Revisit；B/C 和 D 方法入口引用。
- **仍需补读：无。** 保留可逆但委托要求记录的决定、重复已实现请求、不再成立的历史拒绝三例。

### MG-7 · terminology discipline

- **覆盖：职责已覆盖，具体术语操作未覆盖。** B/C Profile、Backbone C 已有规则/状态/上下文与区分例子，不能以 glossary 方法替代全部领域建模。
- **采纳：合并。** 取 `domain-modeling/SKILL.md` §During the session、`CONTEXT-FORMAT.md` §Rules/Single vs multi-context：上下文内 canonical term、易混/不用的称呼、紧凑定义；记录已接受澄清；对照当前代码与既有记录，把矛盾显露再交语义 owner。与 MG-11 的名称映射同落点，但词义定义与翻译映射分开。
- **边界：**代码证明当前实现，不自动胜过业务接受规则；口述也不自动胜过已接受规则。通用词在本域确有特殊含义时可记录该含义，不以“编程词”后缀全排除。Avoid 是本上下文消歧，不抹除别处合法同义词。无需固定 CONTEXT filename；已有 owner docs 优先，resolved 未 accepted 不假写成现行。只查了代码/本地记录时明确未覆盖相关历史；不声称历史必不可检索或只有人类知道。
- **落点：**新 `methods/domain-language.md` 的 Resolve terms、Cross-check scenarios、Record and scope、Local name mappings；与 decision-record 互指，分文件按需加载。两者触发/拥有者不同，不因同一源 skill 强行合成一篇。
- **仍需补读：无承重缺口。** 若 B 要宣称完整领域建模能力，须另有关系/状态/不变量操作依据；本批只接受术语与冲突澄清。

### MG-8 · agent text / context economy

- **覆盖：部分且装配结构已充分覆盖。** Charter 的绑定、methods README 的按需 guide、冻结 Backbone 的相关结论引用已有；指针书写、co-location、完成条件与行为式裁剪缺操作正文。
- **采纳：限缩吸收。** `writing-for-agents/SKILL.md` §Context pointers/Information hierarchy/Steps and completion criteria/Pruning 提供触发明确的指针、通用/分支信息分层、概念条件例外共置、checkable done 条件、去重复/陈旧副本。输出为按需 authoring guide，不修改本批产品所有文档作全库优化。
- **边界：**leading words 招募 priors、否定必然促成违令、pointer wording 决定成功等是源作者启发/未经本任务实验的主张，不能作为已证实规律。目标动作可正面写，但硬约束/授权/召回语义不得因默认模型会遵守而删掉。no-op 是特定模型任务上的观察假设，单次结果不证明可删所有读者所需信息；保留可恢复 diff 和语义核对，运行观察仅用于效果主张，不强制每句 prompt eval。不得隐藏后续安全/授权条件以防 premature completion。文本 craft 不默认归 C 领域语义所有。
- **上下文子机制：**`ask-matt/PHASE-BOUNDARIES.md` 的继续/清空/交接/委托/压缩可取“新任务需要哪些原始依据、转述损失什么、先保存固定证据”的取舍；不继承 ~150k 阈值、默认顺序、强制 phase gate 或子代理命令。此细节与 DEF 的 handoff 共享，不另计第二增量，DEF 可补便携交接操作。
- **落点：**新 `methods/guide-agent-text.md` 的 Pointer/disclosure、Completion、Pruning、Evidence limits；`methods/README.md` 按需索引。Driver 的装配入口只链接，不赋 Driver 全部文本实质裁定权。
- **仍需补读：无，效果未验证。** B 保留强制 guardrail 的 no-op 反例；任何改善 claim 需声明模型、任务、观察覆盖。

### MG-9 · structured elicitation

- **覆盖：部分。** A/Voice 已有事实/推断区分、读回与接受；B/C 已有冲突返回。缺依赖问题调度、recommendation 和未定项收口操作。
- **采纳：限缩吸收。** `grilling/SKILL.md` 的 tree/frontier/recompute、`docs/productivity/grilling.md` §The round/§Common questions 与 `grill-me.md` §Conversation/Grillable：先查可访问事实，基于前置结论选当前能答的问题，附建议及理由，答后重排；需要感受/方案反应的疑问换适当原型证据。
- **边界：**决定归实际获委托 authority，非全部归用户；已接受委托内自主决定不回问 Owner。“整轮全部 frontier”不是强制问卷倾倒，按认知负担可分批/逐题。只穷尽本任务关键未定项，不访问无限设计树。明确尚未知；只暂停依赖其结果的工作。涉及人类保留项须读回并获得接受，既有接受/动作授权继续有效，不再新增最终 ACK gate。原型也需其动作已有授权，不能用“ungrillable”授予实现许可。问题质量与否需真实观察，不能由模型名保证。
- **落点：**新 `methods/decision-elicitation.md` 的 Prepare、Ask by dependencies、Recompute、Unanswerable by conversation、Close/return；`profiles/intent-voice.md`、B/C 入口引用。
- **仍需补读：无。** 保留两问题存在先后依赖、委托内决定无需 ACK、事实访问不可得三例；无“访谈已经改善”的运行主张。

### MG-10 · module judgment / alternatives

- **覆盖：大部分。** `cross-module-design.md` §Method 2/terms 已有完整 interface 与 depth-as-leverage；mock guide §Rules 1/4/5 已有依赖注入、类别、内部/外部 seam；不重复制这些定义。
- **采纳：限缩吸收。** `codebase-design/SKILL.md` §Principles 的 deletion thought experiment、§Designing for testability 的纯计算返回值与小表面取舍；`DESIGN-IT-TWICE.md` §Frame/Present 提供有实质分歧时约束→差异化方案→调用例/隐藏复杂度/依赖策略→depth/locality/seam→推荐的比较。
- **边界：**deletion 是启发，不是 wrapper 自动删除判据：薄适配器可能兑现鉴权、兼容、审计等不可丢承诺，先看功能而非视觉行数。side effects 常是接受行为，宜分开计算/效果而非禁止副作用。不能以减少方法/参数数目代替正确设计。技术 seam 与 domain context 不混用，但“boundary”在安全、职责、部署等场合仍合法，无全库词禁。比较按真实必要性，不要求第二案/3+ agents、并行、固定方法数、由用户确认所有技术方案或全局最优证明。
- **落点：**`cross-module-design.md` §Method 2–3 与 terms 增补 deletion/testability（源 citation 可细化）；新 `methods/design-alternatives.md` 的 Use、Frame、Compare、Recommendation；D 方法入口引用。mock guide 只补指针/准确源范围，避免把模块价值判断塞进替身选择。
- **仍需补读：无承重缺口。** `setup-ts-deep-modules` 的 literal lint/config 不在本机制采纳；其文件实际有五 forbidden entries，skill 描述称四 rules，运行适配/规则有效性交 DEF 处理，未执行。

### MG-11 · local facts / mappings

- **覆盖：任务输入、方法绑定、变更后重评已有充分覆盖；本地名称映射操作仅部分。** Charter 接受源、package Use 的 task-specific input、F Profile 的复用覆盖检查足以承载本地事实，不需新增每仓 config 平台。包称“无 re-sync trigger”为缺口过强，F §交接与召回已明确按版本/差分复用。
- **采纳：合并。** `setup-matt-pocock-skills/SKILL.md` §Explore、`domain.md` 和 `triage-labels.md` 支持先读已有惯例、语义保持的 canonical→local mapping、明确消费入口；合并进 MG-7 的映射段与 MG-8 的环境真源/指针段。必要本地 facts 可在现有 task input/owner doc 引用一次，不 fork 通用方法。
- **边界：**mapping 不创建标签、权限、tracker 或规则；配置文件存在不证明 agent 会消费它。mapping 两侧确有同一含义才可转换，冲突找语义 owner，不把语言翻译强行当业务等价。无普遍 run-once/setup-before-use gate，已有 facts 不重复确认，无新 registry/schema/validator。`link-skills.sh` 的 symlink write-back 防护是独立工具安全机制，交 DEF-14，不以此证明配置机制；脚本含目录替换行为，未执行、无许可。
- **落点：**`methods/domain-language.md` §Local name mappings；`guide-agent-text.md` §Environment/pointers。Charter 原字段即可引用；已有重评规则无需新增文件。每仓统一配置面目前不新增，未来实际消费需求出现再按任务判断。
- **仍需补读：无；**tracker 模板命令与真实 readback 未验证、不吸收为可运行能力。

## 可蒸馏批次（建议落点，不是派工）

| 批次 | 机制与正文写面 | 消费入口 |
| --- | --- | --- |
| T · 测试与观察 | MG-1/3/4：test-first-behavior-slice、guide-test-evidence-quality；cross-module 的观察表面段；F 方法只短引用 | E/F/D Profile 的方法指针与 methods README |
| P · 规划 | MG-2/10：change-slicing、design-alternatives；cross-module 的模块判断段 | D Profile、methods README |
| B · 行为条件 | MG-5：behavior-contract-examples 的条件/区分例子段，可与其他源的行为方法合并 | B/C Profile、methods README |
| C · 语义与决定 | MG-6/7/11：decision-record、domain-language（名称映射并入后者） | B/C/D 的对应方法指针 |
| A · 追问 | MG-9：decision-elicitation；可与其他源的问题调查方法整合，保留依赖问答操作 | A/Voice 与 B/C 方法指针 |
| W · 文本 | MG-8/11：guide-agent-text；handoff 细节待 DEF 合并 | 按需支持索引，不常备全量加载 |

这是职责/内容分组，文件名是落点建议，不要求逐个新建。Driver 管互斥写面与串行集成：cross-module、Profile 和 methods README 跨批共享，不允许并发覆写。后续跨源合并须保留本裁定具体操作、例子和例外；不能只留原则，也不能把批次表变产品固定流程。

## 包内其他观察与残余

- §3.2 的源范围精度建议成立：mock guide 的 `Designing for testability L69–80` 只覆盖 injection；如引入返回值/小表面，源锚应分别指到完整相应条款，不能旧范围背书新内容。
- §3.4 未显示需要四处同步改装配顺序的实际缺陷；入口各自职责不同，目前一致。此批不触发无关入口重写。
- §3.6 “command output 是证据不是指令”可以留 E 方法：Security 是横跨 judgment 的 concern，不要求另建常驻 security entry 或搬出有效就地提醒。
- 169 路径/59 distinct/42 DEF 与末尾“37 paths”的账面关系，以及支持文档/脚本跨组重叠，未在本次逐路径复算；本结论只裁定 11 机制，不认证全仓已完成。Driver 的索引关联仍须解释 DEF 分母和重复来源。未审 DEF 实质、38 metadata 文件各自差分、发布 CI 或全部资产；不据本 review 把其记成实质接受。
- 源 docs 所述团队重工比例、模型违令、200 问等只是 pinned 页面报告，未访问关联 issue，也未独立复验。无真实业务、下游采纳或效果证据。

审核交出：11 组已有源支持的实质结论，均可按限缩与合并要求蒸馏；正式正文、引用/消费入口与具体反例须在 B 固定差分上再次核验。
