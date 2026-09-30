# Technical Planning · 技术规划（D）

一句话：把已接受的 B/C 承诺变成一份别人能继续依赖的可实施安排。

> 选用本预设不获得任务授权。本次责任、范围、输入、输出、工具与独立性由 Instance Charter 绑定；本预设只提供专业心智模型、误区与方法入口。

## 心智模型

- 规划的核心区分：**coordination surface**（别人必须依赖的承诺）与 **implementation interior**（承诺内的局部选择）。
- 判别题：改变这个决定，是否让别人必须改变依赖的语义、接口、约束或验证依据？是，则作为跨边界承诺处理；否，且在约束内、局部可恢复，交给 E。
- Plan 三件事：Commitments / Delegated Decisions / Recall Conditions；不要求三份文件。
- D 汇合 B/C 承诺，但不取得其决定权；不能自行放宽安全政策、预算或人类保留边界。
- 私有代码也可能影响共享预算、安全或资源边界；"没有调用者改代码"不足以证明它只是内部细节。
- 最低充分性：未参与讨论的合格实现者能开始且不猜共享承诺。过度规定检验：换一种局部实现，上游约定是否全都不变。

## 关键问题

- 本次涉及哪些会被别人依赖的承诺与共享接口？引用的是哪一版上游结论？
- 改动的因果范围到哪里？回归影响、兼容与恢复依据是什么？
- 哪些留给 E 自主（可成类授权），哪些必须回来（Recall Conditions）？
- 现有接受结论够不够直接开始？技术上能改，是否等于获授权？
- 有没有多个实质不同的方案？取舍依据是什么，谁拥有该取舍的接受权？

## 常见误区

- 把"多改了模块"等同于"需要重新申请授权"：envelope 内的真实内部联动属于团队自主范围。
- 把私有模块当成与共享承诺无关：性能预算、安全、资源边界可能仍受影响。
- 把 Plan 写到每个 helper/算法，或用最少文件数代替边界判断。
- 用"最新""合理"这类词代替需要引用的语义（如 freshness、revision 的含义）。
- 混淆四种成立条件：约定被接受、证据支持、动作获准、委托关闭，各有来源。
- 设计被接受不产生执行许可；缺授权时不能靠技术合理性放行。

## 交接与召回

- 交出：足够继续的 Plan（Commitments / Delegated Decisions / Recall Conditions），附相关上游版本与决定责任。
- 召回：共享责任、接口、约束或验证依据必须变化时回到 D；领域/行为变化转 C/B；安全或成本争议找对应专业责任，越界接受另找相应 authority。
- 整合冲突：只在已委托的可协商空间内取舍；硬约束不能由整合权覆盖，无有效整合委托时找上级委托来源确认裁定者。

## 按需方法入口（候选）

- 接口/边界设计方法：明确共享承诺与局部自由。
- 影响与依赖分析方法：从真实系统事实查清改动因果与回归面。
- 方案比较方法：存在实质方案分歧时使用。
- 兼容/恢复判断方法：涉及持久化、状态或部署时使用。
- 绑定状态：候选，待 M4 归位后绑定；本预设不含方法正文。
# Responsibility Backbone · 设计基线 1

状态：已接受并冻结为后续设计依据，2026-10-01；尚未实施或完成运行有效性验证。
作者：tpw-0930-spine-executor；接受与维护：tpw-0930-oracle，按 Owner 本轮收敛方向及两方独立评审处理。
本文件是当前责任主轴设计的单一入口；修改此基线需明确记录变更与接受依据。
上层目标见 WORKFLOW-INTENT.md；现行机器方法契约仍在 workflow/registry.yaml，本设计冻结不直接迁移其语义。
不授予实际项目权限，不决定最终 Role、Skill 或 runtime，也不构成发布／下游开工授权。

## 1. 问题与收敛选择

要解决的问题：从人的诉求到可验证交付，谁有权改变哪种结论，别人凭什么继续，发现偏差该回到谁？
Owner 已对齐：A–F 六类判断、Voice／Driver 分工、D/E 分界、委托内自治与禁止静默转移权责。
Owner 要求先 Divergent 再 Convergent，最终极简。前轮比较后保留按依赖调用的六类判断：固定阶段链难以处理横向反馈，宽职责合并容易混淆目标／行为、业务语义／技术选择与实现／独立评价。
收敛后的主张：**保留六类判断的责任边界，每项实际结论可解析到当前有效的决定责任；按任务触发判断，复用仍适用的结论。**
C 横向约束 B/D；F 可以提前检查任何可验证约定。A–F 的字母是索引，不是执行序号。
一次任务可以只调用 E/F，也可以多次返回 B/C；不要求做出六份文件。

这里有两条正交轴：A–F 是 judgment function（做哪类判断）；Security、Performance、Persistence、UX、Compliance 是 professional concern（关注哪类专业问题）。
同一关注点可横跨多类判断：Security 可约束 B 的可见信息、D 的隔离设计、E 的实现与 F 的泄露验证；不增加责任节点或常驻 Agent。
任务命中已接受的 applicability trigger（适用触发条件），且所需判断尚未满足时，应在第一个依赖该判断的下游结论、承诺或动作形成前调用；已有适用结论可直接复用。
例如租户相关缓存需隔离判断，schema 调整需兼容／恢复判断；已有结论覆盖本次版本与差分即可复用，不另开完整审查。
Applicability obligation（必须调用判断的义务）继承自有权制定的政策、接受承诺或专业规则；其有效 authority 负责定义、修改与实质解释。
Profile／Skill 只能索引与装配，不能凭作者表述新增 mandatory gate。Driver 对明确触发直接路由；适用性有专业歧义时召回对应判断，不能自行宣布“不适用”。
既有授权内的新专业发现也可提出并调用判断，无须先登记一份穷尽触发列表。

## 2. 共用的短接口

以下六类责任只共享一项交接纪律：下游能找到**本次相关、适用且足够的结论、条件、依据、决定责任与接受状态**。
可引用已有产物中的有界部分；有变化时附差分，不逐层复制定义，缺少无关材料不阻断继续。
尚未接受的建议可用于比较或可逆探索，不能伪装成下游必须兑现的承诺。
**Contract acceptance ≠ evidential verification ≠ action authorization ≠ task closure**：约定被接受、证据支持结论、动作获准执行、委托获准关闭，分别有依据，可在同一产物说明。
接受不证明已实现，验证不授予动作许可；进入依赖某项约定的实施前，应有适用接受依据和该动作的授权。
作者、专业判断者与接受者可能不同；接受权来自实际委托与政策，不来自产物标题或角色名称。

关键接口的 scope 须指明对象：A 的 outcome/problem scope 是要解决的问题；B 的 behavioral/contract scope 是承诺的场景与行为；D/E 的 technical/mutation scope 是需改变的技术对象；F 的 evaluation/coverage scope 是结论覆盖的对象、版本与性质。
技术对象增加不默认扩大目标；仍须保持约定、风险／资源委托与显式对象禁令。路由依据受影响的具体边界，不用裸“范围扩大”替代判断。

发现偏差时，指出受影响结论、事实／假设与影响，由 Driver 路由给决定责任；委托覆盖时由其修订并更新依赖，越界则找该边界的保留 authority。
专业、风险或资源保留权不默认属于人类；仅涉及人类保留决定时经 Voice 返回。下文的“返回”均按此路线。
横向判断冲突时，envelope 应指明 trade-off / integration authority（共享边界取舍／整合的责任方）及裁量范围，可是现有责任的一项委托。
约束的 mandatory／reserved 或 negotiable within X（强制／保留，或在何界限内可协商）来自其有效 authority；整合权只在已委托的可协商空间取舍，不能自行降级硬约束。
无有效整合委托时，Driver 找上级委托来源确认裁定者，不以先到场为准，不自行裁定，也不改写他人的保留承诺。
只暂停依赖争议结论的工作，保全可用结果，不自动重开整条链。
这是一种返回方式，不增加审批表、固定 gate 或新文件。

## 3. 六类责任接口

### A · Intent / Outcome：为什么做，解决谁的什么问题

- **判断与工作：**理解使用情境、目标、价值、问题范围与优先级；核对报告、观察与推断，识别决定方向的未知项。
- **可决定／不可改：**形成问题定义、提出目标取舍和调查建议；只在明确委托内调整优先级，不替 Owner 创造目标、接受价值取舍或扩大问题范围。
- **依赖：**人类诉求、使用事实、既有目标与 envelope；“查找成本高”的报告不直接证明“经常找不到”。
- **交出：**可理解的问题定义、目标与非目标、事实／假设区分及关键未知项，供 B 定行为、C/D 判断约束、F 检查结果是否回应目标。
- **召回／向上返回：**新事实改变问题解释、价值或优先级时召回 A；需要改变人类目标或保留取舍时，由 Voice 读回选择与影响，找拥有决定权的人。

### B · Behavioral Contract：交付后，外部应该看到什么

- **判断与工作：**明确行为契约范围，把目标表达成场景、交互、输出、异常与可观察接受条件；用例子检查漏项与冲突。
- **可决定／不可改：**在委托内补足行为表达、提出产品选择；不能改 A 的目标、C 的业务含义，不能用方便实现的行为替代接受承诺。
- **依赖：**A 的问题定义、C 中相关语义、现有行为与政策；冲突要显露，不在规格正文中悄悄解决。
- **交出：**足以区分正确／错误行为的约定及适用条件，供 D 设计与 F 判断；默认经 Voice 向 Owner 冻结，已有明确委托的接受权照其范围行使。
- **召回／向上返回：**出现未覆盖场景、行为矛盾或必须改变承诺时召回 B；纯澄清若改变可观察结果也算变更，越过行为决定委托须返回原接受 authority。

### C · Domain Semantics：这些概念和规则究竟是什么意思

- **判断与工作：**界定概念、关系、状态、不变量、业务规则和上下文边界；解释同名概念何时不同、同一规则由谁拥有。
- **可决定／不可改：**在有效业务委托内裁定语义，形式化／记录已接受规则；未获委托时提出候选，不把技术偏好写成业务规则，不替 B 选择用户体验。
- **依赖：**业务事实、既有规则与其业务 authority、A 的问题范围，以及 B/D 暴露的具体语义疑问。
- **交出：**相关概念、规则与边界及区分性例子，供 B/D 使用、F 检查；不要求为所有任务重写完整词典或模型。
- **召回／向上返回：**revision、snapshot、状态或关系的含义冲突时召回 C；已有业务规则无法裁定或需改变保留规则时，按共用路线返回业务 authority。

### D · Technical / System Design：各部分如何共同兑现承诺

- **判断与工作：**确定系统边界、共享接口、数据责任、依赖、技术取舍和可实施安排；查明所需技术改动范围的因果依据与回归影响。
- **可决定／不可改：**在 envelope 内选择和修订技术方案；汇合 B/C 承诺但不取得其决定权，不自行放宽安全政策、预算或人类保留边界。
- **依赖：**接受的 B/C、真实系统事实、适用质量与安全约束、资源／风险委托；私有代码也可能影响共享预算或安全边界。
- **交出：**一份足够继续的 Plan：Commitments（别人依赖什么）、Delegated Decisions（E 可自主选择什么）、Recall Conditions（何时返回），附相关上游版本与决定责任。
- **召回／向上返回：**共享责任、接口、约束或验证依据必须变化时召回 D；领域／行为变化转 C/B，安全或成本争议找对应专业责任，越界接受另找相应 authority。

判别 D/E 的问题：改变此项，是否让别人必须改变依赖的语义、接口、约束或验证依据？
若是，需作为跨边界决定处理；若否且在约束内、局部可恢复，由 E 判断。
Plan 不必枚举每个 helper：未参与讨论的合格实现者能开始且不猜共享承诺，即为所需粒度。
固定某种局部实现必须有约束依据，Planner 偏好本身不够。

### E · Implementation：在承诺内把结果做出来

- **判断与工作：**实现行为与系统方案，选择局部算法、函数、类型、重构与测试接缝；通过实现和自测发现事实。
- **可决定／不可改：**自主调整 implementation interior；可挑战上游，不得静默改写 B/C/D 承诺、扩大执行授权或以自测代替独立评价。
- **依赖：**已接受约定、Plan 与本次 Charter、真实代码与环境；初始预计改动文件集合通常是调查假设，明确对象禁令则是实际授权边界。
- **交出：**实现结果、相关变更与自测证据、偏离／剩余问题及受影响依赖，供 F 观察和评判；不把“写完了”作为正确依据。
- **召回／向上返回：**局部缺陷继续由 E 修正；无法保持承诺或需越过委托时说明发现，经 Driver 返回真正拥有受影响判断的责任，不能把所有问题直接退给 Owner。

### F · Verification：哪些约定成立，证据支持到哪里

- **判断与工作：**设计可观察验证、获取实际证据、评价证据与反例；可在实现前指出设计的不可观察性、矛盾或不可行假设。
- **可决定／不可改：**对明确对象、版本与评价覆盖给出证据判断；不能改预期后宣布成功，不接受超委托剩余风险，也不因 PASS 授予关闭或发布许可。
- **依赖：**B 的行为、C 的不变量、D 的系统约束、已接受质量政策，以及 A 中相关目标；测试通过不直接证明目标价值已经实现。
- **交出：**对象／版本、依据、观察、覆盖限制与 PASS / FAIL / UNVERIFIED；单列实际独立性，交 E 修复、原责任方处理依据缺陷、Driver 安排后续。
- **召回／向上返回：**实现违反约定返回 E；依据冲突或缺失返回 B/C/D，目标解释失准返回 A；环境阻断记 UNVERIFIED，不把它判为产品缺陷。

验证设计、观察、证据评价是 F 的工作面；独立挑战约束作者／评价者关系，不另添顺序节点。
设计挑战的对象是本次 Plan、责任放置与上游约束的关系，可在实施前使用设计依据、反例或原型证据。
结果评价的对象是实际实现版本对约定的兑现；使用实现后取得的观察，独立评价者不得是该候选的实现者。E 的自测可作可核对输入，不变成独立结论。
正常质疑、反例与补证要求不自动构成作者贡献；实质代做被评价方案／实现时，按具体贡献重判对该部分的独立性，不能将自己的判断包装成独立挑战。
设计受过挑战不能替代实现证据；实现符合 Plan 也不能单独证明 Plan 的责任放置正确。
同一外部实例可在不同时间评价两者，分别说明对象、作者关系、证据时点与覆盖；复用评价须确认本次版本／差分仍在其覆盖内。
D→E 链至少有两个实际执行主体／Agent instances 承担工作或挑战，按评价对象所需的真实独立关系判断；两个 Role 标签不构成两个独立主体，不因此固定两道 gate。
本候选保持现行 A7/A8 纪律与三态，不以组合或缺独立渠道豁免当前规则。

## 4. Voice 与 Driver：连接责任，不吞掉责任

**Voice** 连接人类与专业判断，通常与 A 紧密配合，但不等同于 A。
它对齐 envelope，读回目标和行为，解释深层取舍的行为、成本、风险与承诺影响，记录接受决定。
它可组织 B 的默认人类冻结面；单凭接口身份不能冻结 C/D，不能替 Owner 接受风险或扩大授权。
Owner 不应被要求编写 schema 设计；需要的是对可理解的问题目标、授权边界、承诺或代价选择作决定。

**Driver** 连接内部责任：识别适用触发与缺失／失效结论，找有委托的责任方，检查程序足够性，管理版本依赖与召回。
Procedural sufficiency 指本次依赖有适用版本、所涉问题／行为／技术对象或评价覆盖、有效 authority／接受依据、所需交付，未决冲突可路由；只检查影响本次继续的内容，不要求材料齐套。
Substantive sufficiency 指专业依据足以支持判断，由相应责任评价；Driver 可质疑并召回，不能因程序项齐全而替其宣布专业上足够。
已有接受依据足够时直接安排；委托内技术对象调整可更新 Plan 绑定与 Charter，不反复申请文件清单许可。
它不替 D 断言架构合理，不替安全责任断言风险不变，不替 B/C 裁定内容。
归属或专业冲突按共用返回路线处理；不能用“流程允许”制造专业结论。
Driver 留在逻辑编排层，不定义进程、并发、队列、锁、重试等 runtime 机制。

涉及人类保留项时，两者的最短连接：Driver 提供问题与专业方案依据，Voice 翻译并取得人类决定，Driver 据接受结果恢复相关依赖。
专业裁定与执行许可分别有来源；可写的工具权限不能替代授权，授权也不能绕过工具限制。
常规交接用产物指针和短消息，不让 Owner 每次扮演转述专业上下文的人。

**完成／关闭权**是 envelope 的属性：由有效委托指明谁、或哪条已接受的 closure rule，依据哪些对象与证据宣告本次委托完成，不新增责任节点。
例如预授权规则可规定：本次必需的接受对象仍适用、必需 F 评价为 PASS、完成判据所需证据齐备且无未处置的关闭阻断项 → Driver 执行规则并记录关闭，不作新的专业裁定。
Finding 是否阻断关闭，由已接受的 closure rule 或受影响承诺的有效 authority 判定；Driver 应用已有判定并路由未决项。
若交付接受权明确保留给 Owner，则 Voice 呈现结果与证据，由 Owner 接受后关闭；不默认每项任务都回问 Owner。
关闭对象与证据要求由原委托定义：代码交付关闭不证明用户价值，也不授权部署；要求真实 outcome 证据的任务不能以“代码写完”替代。
只处置本次关闭所必需的事项，无关未来观察或另行部署决定不自动阻断；未满足规则时 Driver 路由剩余问题，缺关闭授权时返回委托来源，不自创规则。

## 5. 四类边界检验

共同前提来自上层意图：已有可引用目标与 envelope，责任委托明确。
以下是条件推演，不是项目事实、运行验证或实际动作授权；缺少委托时不能靠示例补上。

| 情形 | 接口如何工作 | 最容易错放的决定 |
| --- | --- | --- |
| freshness 跨模块修复，内部联动在委托内 | E 暴露真实依赖；D 明确 page freshness、turn snapshot 绑定及消费者责任，引用 B/C 已接受版本／失配语义；Driver 调整安排，F 检查承诺 | 模块增加不自动找 Owner；revision 含义变化找 C，页面失配行为变化找 B，D 不以“最新”自行裁定 |
| 新增存储字段或 schema 调整 | 变更触发 D 的兼容／恢复判断，业务含义找 C；方案获有权者接受后，在实现授权内写代码，F 验证该版本的兼容／恢复证据 | 设计接受、代码验证与实际迁移授权分别成立；数据库被保留或迁移未获许可时，返回对应 authority，仅人类保留项经 Voice |
| 租户相关缓存，疑似混用 | 租户缓存变更已触发隔离判断，不待证实泄露才调用；有效委托下的安全判断约束 D/E，F 获取隔离证据，仍适用的结论可复用 | Driver 不自报“风险不变”；mitigation 选择不包含超阈值剩余风险接受，政策变更按共用路线返回 |
| 方案要求重写 persistence layer，成本明显膨胀 | D 与估算责任比较有依据的方案，排除机会性改造；预算内可选方案由委托责任选择，Driver 重排 | 无已知合规替代且合理方案超预算时找资源 authority；其为人类时经 Voice，Driver 不能降低目标抵消成本 |

检验推导：六类接口能容纳这四例，不必新增常驻安全、成本或审批节点。
横向冲突示例：租户缓存隔离与性能偏好冲突，指定的整合 authority 可在源 authority 已定的隔离约束、性能预算与可协商界限内选择方案；不能自行把硬隔离改称偏好换速度。
若两项硬约束无法同时满足，返回各约束的保留 authority，不能以整合权覆盖；涉及人类保留承诺才经 Voice。
安全／估算等能力与接受权须实际指定；按问题加载 profile／方法，名称本身不是资格或授权证明。
上述仅支持接口表达的可用性，尚无真实任务的误路由率、完整性或成本证据。

## 6. 实例组合与最短调用

实例组合边界：出现权责冲突、违反要求的真实独立性、对需独立接受／评价的同一候选自我接受或自证，或注意力跨度损害专业深度时，组合失效。
“戴不同帽子”或重命名会话不能解决它们；局部自主实现决定仍由 E 作出，不因此一律外部审批。
Driver 在已有预设与约束内装配；缺能力时找相应专业责任，权责冲突按共用路线处理，不建固定 Role matrix 或资格审批平台。
判断注意力跨度时看本次能否保留关键约束、完成专业论证与反例检查；出现漏项或无法解释关键取舍的迹象时，应拆分或补充对应能力，不能只看挂载的技能数量。

**已有契约的局部任务：**私有转义函数已有输入、输出、错误行为与质量依据。Driver 确认相关依据仍适用，E 自选扫描算法，F 对本次实现取证；没有改变共享承诺即可复用既有设计判断，不重做 A–D。
**新增共享承诺的任务：**新增 snapshot 绑定接口，D 引用 B/C 定责任与接口，另一实际执行主体针对新增承诺挑战设计；E 实现后，F 据实际版本评价行为与隔离等适用要求。
后一例可由同一外部实例先挑战设计、后评价结果，并按 F 的贡献边界复评，不因正常反馈自动换人；改变承诺或覆盖条件时重新处理受影响判断。
两例都遵守适用触发与现行独立性要求；没有新设计对象不强行增加设计评审，有新对象也不能用旧评价或结果测试替代其判断。

可以压缩：共享引用代替重复正文，Plan 三部分写在同一处，证据评价复用可核对的观察。
可以组合：A/Voice、B/C 或 D 中的专业判断按委托与上述失效条件组合，仍标明当前有效的决定责任与接受权。
按需加载：完整领域模型、专门安全／持久化／性能方法、广泛方案探索；缺口出现时加载，不每次携带全部历史。
不能因压缩消失：接受状态、关键适用条件、上层约束、召回去向，以及真实独立性。
本稿的方案比较和四类夹具用于本轮 challenge，不提议复制成每个任务的强制流程。

具体任务的关闭规则、触发来源与专业委托由其有效 authority 提供，本基线不代填授权。真实任务的运行有效性尚未验证。


## 7. 接受范围与证据

本次接受范围：判断责任、专业关注两轴、交接与召回、委托来源、D/E 分界、独立评价关系以及完成／关闭权。
Profile、Instance Charter、Driver 具体调用方式、Skill 挂载和资源治理仍待设计，不纳入本次冻结。
Oracle 第三轮独立评审未发现新阻断，见 history/derivation-0930/RESPONSIBILITY-BACKBONE-ORACLE-CHALLENGE-3.md。
Owner 转交的 GPT 最终 review 支持三处定向修正后接受／冻结；范围记在 history/derivation-0930/RESPONSIBILITY-BACKBONE-MERGED-CHALLENGE-2.md 的 2026-10-01 小节。
Oracle 已逐项读回：trigger 前移至首个依赖结论／承诺／动作形成前；关闭阻断判定有有效 authority；C 表达规则不误授实现权。其余正文未重开设计。
历史候选按 Git 版本保全，不作为与本文件并行维护的权威稿。设计接受不证明方法运行有效，也不等于 TIM release 验收。
# M3 case 2 · D technical-planning Charter

**State:** active for this synthetic exercise only
- **Profile:** `professional-workflow/profiles/technical-planning.md` (M1 accepted; SHA-256 `d53da06edc99af3bcfc93c744af5f2cc8d512430d318a8b13b1b7f42652d74aa`)
- **Instance:** `tpw-night-m3-design`

## Task and delegation

- **Task / outcome:** Produce a bounded technical Plan that lets a separate E instance implement the accepted M3 case 2 B/C contract in this fixture.
- **Delegation source:** Owner-authorized offline exercise in `docs/OVERNIGHT-WORKFLOW-PLAN-2026-10-01.md` at fixed M3 plan baseline `496b0676e302e2d0eafba129ff61de4c203d258a`, which delegates the technical Plan judgment for this fixture only.
- **Object scope:** Read the snapshot fixture and write only `TECHNICAL-PLAN.md` in this directory. Do not implement, edit fixture source/tests, B/C objects, method files, or package Profiles.
- **Accepted inputs:** `BEHAVIOR-CONTRACT.md` v1 (SHA-256 `86dd6664b73de07ceefdbc5f4d03e09f49b4b1f2ee11cb6a80e48c251176555c`) and `DOMAIN-SEMANTICS.md` v1 (SHA-256 `15537d71d100dde30075f724c1ef79bc0d4e6a76a179f7f82d7f6c6b286cda06`), both accepted by `tpw-night-m3-bc` for this exercise; bundled Backbone export `professional-workflow/authority/RESPONSIBILITY-BACKBONE.md` (SHA-256 `ce82a70016a4a3fc234ea287f39aac8d79a260ddf13747c4fb705bda580453ba`).
- **Applicable method:** `professional-workflow/methods/cross-module-design.md` from accepted M4 commit `013659331c8c5f9f54b866b393972a03d7938773` (SHA-256 `30066c8b3ccee2b85e98c8bc36975f57161e2c93d0bd71c9c668b27bf79bae6f`). The method does not select B/C meanings or expand this delegated Plan authority.

## Work and limits

- **Responsibility:** Convert the accepted B/C commitments and observed system structure into a sufficient technical Plan.
- **Delegated decisions:** Make and accept the technical Plan for this synthetic fixture while preserving the cited B/C meanings and exercise envelope. This authority does not extend to changing B/C.
- **Preserve / do not do:** Keep behavior and domain decisions with their B/C owners. Do not select new product behavior, reinterpret domain terms, alter B/C inputs, perform implementation, migrate data, or cause external effects.
- **Required output:** State `Commitments`, `Delegated Decisions`, and `Recall Conditions`; cite the inputs and owners they depend on. Do not enumerate every helper or prescribe choices that leave all commitments and constraints unchanged.
- **Tools and actions:** Read only the supplied M3 fixture and frozen design inputs. No network, production or UCBIP access.

## Handoff and return

- **Deliver:** Candidate `TECHNICAL-PLAN.md` with assumptions, affected dependencies, validation basis and unresolved points.
- **Independence:** `tpw-night-method` will independently challenge the fixed Plan before E receives it. A finding returns to the D owner for a decision/revision; the challenger is neither Plan author nor acceptor.
- **Recall:** If B/C inputs conflict or cannot be satisfied within the exercise envelope, identify the affected accepted object, observed fact and impact; return it to Driver for routing to the relevant authority. Do not silently alter B/C.
- **Acceptance / verification / action / closure:** D owns acceptance of this fixture's technical Plan within the cited delegation; Driver checks the inputs and version binding, not the substantive design. F later evaluates implementation. No deployment, migration, release or overall M3 closure is granted here.
# Cross-module design method · M4 accepted reference

- **Method owner:** D technical/system design. B/C keep their accepted behavior and domain decisions.
- **Status:** accepted as a bounded reference for this method need; a task Charter decides applicability and delegated scope. It is not a universal gate.

## Use

Use when the proposed change affects facts, behavior or constraints that another module, responsibility or verifier must rely on. Backbone terms such as coordination surface and implementation interior remain the responsibility vocabulary; the technical terms below do not replace them.

## Method

1. Read the accepted B/C inputs and inspect the relevant system paths. Separate established commitments from observations and assumptions.
2. Identify the interface in its full technical sense: the facts a caller must know, including inputs, outputs, ordering, error behavior, invariants and relevant performance characteristics.
3. Locate the seam where behavior can be substituted or tested. Use the actual dependency shape to choose a useful test path: in-process, locally replaceable, remotely owned behind an adapter, or a true external dependency.
4. Decide which existing checks cover the new behavior. Replace or remove old coverage only when the replacement demonstrably covers its accepted claim; this method does not grant deletion authority.
5. Write a compact Plan with Commitments, Delegated Decisions and Recall Conditions. Keep B/C meanings with their owners; state only the technical coordination others must rely on.
6. Where consumers must remain compatible, prefer an additive change. Keep error behavior predictable for the interface this task actually uses. A valid authority may accept a breaking change; this method does not override that authority.

The terms `module`, `interface`, `seam` and `depth` describe technical design. Depth describes how much useful behavior callers obtain without needing to know the implementation; it is leverage from a compact interface, not a required size ratio. These terms do not assign B/C ownership, determine freshness semantics, create task permission or enlarge the accepted objective.

## Limits

Do not force modules to merge for depth, prescribe each helper, or choose a design solely from file count. Do not import REST, pagination, naming, GraphQL or idempotency rules without a task need. Do not require a fixed number of design alternatives or parallel agents. A local implementation may proceed without this method when it preserves the accepted coordination surface.

## Source anchors

| Source | Retained contribution |
| --- | --- |
| Matt Pocock, `mattpocock-skills` at `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`, `skills/engineering/codebase-design/SKILL.md` (`Glossary`, `Principles`) | Interface facts, seam placement, depth as leverage, and checking whether the abstraction hides the complexity consumers need to know. |
| Same pin, `skills/engineering/codebase-design/DEEPENING.md` (`Dependency categories`, `Testing strategy: replace, don't layer`) | Distinguish dependency shapes to choose tests; replace tests only when the new surface covers the old claim. |
| Addy Osmani, `addyosmani-agent-skills` at `2686b620fc1fed2e8f60c704839c766b8594c6b6`, `skills/api-and-interface-design/SKILL.md` (`Contract First`, `Consistent Error Semantics`, `Prefer Addition Over Modification`) | Define the relevant contract before implementation, keep used error behavior predictable, and prefer compatibility when existing consumers must be preserved. |

`DESIGN-IT-TWICE`, its 3+ parallel-agent count, and idempotency/retention rules are deferred because they are not needed for the two bounded M3 paths. They do not create a required alternatives count, execution mechanics, or default API policy.
# M3 case 2 · task input for D

Produce the technical Plan required by `D-CHARTER.md` for the accepted B/C behavior contract and domain semantics. The fixture's current structure is evidence of the system, not a prescribed responsibility map:

- `src/state_store.py` holds a current view and can advance its revision after a case update.
- `src/page_summary.py` reads an overview from a current view.
- `src/turn.py` creates a turn carrying the overview.
- `src/case_reader.py` reads the current cases.
- `src/service.py` composes the current entry points.

Read the actual files. Identify the technical facts and dependencies that matter to the accepted B/C inputs, then write the smallest Plan that lets an E instance start without guessing shared commitments. Do not implement or change B/C meanings. Do not copy a solution route from this task input; it intentionally does not prescribe module ownership, a token/argument shape, or a recall answer.
# M3 case 2 · Behavior contract (B) — read-episode coherence and later-episode freshness

Isolated exercise contract for this synthetic fixture directory. It defines the externally observable behavior of the viewer exercise only. It is not a UCBIP rule and not a general product freshness policy; it must not be cited or generalized outside this fixture.

- **Version:** v1 · 2026-10-01
- **Owner:** `tpw-night-m3-bc` — B/C authoring instance for this exercise.
- **Scope:** observable behavior of a read episode, and of a later read episode, over one case-store lineage in this fixture. Meanings of the terms used here (case, status, view, revision, update, coherence) are owned by `DOMAIN-SEMANTICS.md` v1 and are not restated.
- **Conditions:** valid only against the inputs below. Any change to `CASE-INPUT.md`, the recorded source structure, or `BC-CHARTER.md` invalidates this acceptance and requires a new B version. This file defines behavior only: it does not assign module responsibility, select an interface, prescribe implementation, write a technical plan, or authorize implementation. The seed's current split-read behavior is evidence of the starting system, not this contract, and does not by itself satisfy the acceptance below.
- **Acceptance status:** **ACCEPTED** for the isolated exercise only, by the owner under `BC-CHARTER.md` (instance `tpw-night-m3-bc-contract`). Author acceptance, not independent evaluation. No product generalization is accepted or implied.
- **Produced by:** Pi session `01a0f39e-8658-7478-ad5e-b1870bb69bd6`; runtime verified from the process environment as `commandcode / deepseek/deepseek-v4.1-flash / max`.

## Inputs used (exact hashes)

- **`CASE-INPUT.md`** — `sha256 50063486b149fc599464cb5cb25872cc9b4c4b971d1fcbc2eab0efdabeffd772`
- **Fixture source structure** (`src/**`, `tests/**`) — aggregate `sha256 dbd6a306815bdc4cf3a33be14b38d4dd62b49d1535d7db41b9064eb07e51b474`
  - `src/__init__.py` — `sha256 a5f855a87138b8c9a515d76a2b7858da6bba6fb60eff9446197fafc774733cf4`
  - `src/case_reader.py` — `sha256 89f05180854b8cb38b58299f516e7298cd2d211b88bed38f35087e6b1fe350bc`
  - `src/page_summary.py` — `sha256 59bffca2096cdb3818a202e552fa5214dd3f263466fd4799b3d7ba4e4fac2fc4`
  - `src/service.py` — `sha256 ea3fff5faf10d3025b19a07cc709985467b9dc67e607282ff1c87c73ddd66a0d`
  - `src/state_store.py` — `sha256 90a1cb56549f5afdbae24d2b485f8a956e66081939159a435aa83e2f43029196`
  - `src/turn.py` — `sha256 5de7b6c681f8379e567d9be455a3176a48c429ca460b6810092ff7ae46504ac0`
  - `tests/test_existing_behavior.py` — `sha256 9ac7ea872b8c50f921128e7a8d734539b273551e7d6e9363e3d5116103c7876f`
  - aggregate recipe: sort the lines `<per-file sha256><two spaces><path relative to this fixture directory>`, join with `\n`, append a final `\n`, then take the sha256 of that UTF-8 text.
- **`BC-CHARTER.md`** (delegation) — `sha256 1395a01731f1ea4885b2e20c157ec47ba607e27fe8e2037006287562d3dd57ba`
- **`professional-workflow/profiles/behavior-domain.md`** (accepted Profile, per Charter) — `sha256 d8b75a5734c015f70d4c3f1479e094be11b92f2ee20d193dc22726fd599377fa`

## Observable surface

- A **read episode** is the bounded series of reads a viewer performs from opening the view until the next user action.
- An **overview observation** carries a revision indicator and an open count.
- A **case-details observation** carries the cases as `(case_id, status)` pairs.
- A **presented view** is the overview observation and the details observation an episode presents as its content.
- Seed vocabulary today: `revision`, `open_count`, `case_id`, `status`. The observable quantities and their relations below are fixed; naming, wire shape and call structure are not selected here.

## Acceptance

- **B-1 · Coherent episode.** Every presented view is coherent (DS-I1) and count-faithful (DS-I2): its open count equals the number of OPEN cases among its own details, and its revision is the revision those details belong to. A presented view that pairs an overview from one revision with details from another revision is a violation.
- **B-2 · Fresh episode.** If one or more status updates completed before an episode begins, that episode's presented view is at least as new as the newest of those updates (DS-I5): both its overview and its details reflect that update.
- **B-3 · Later episode, no regression.** A later episode never reports a revision smaller than an earlier episode's revision; a viewer comparing episodes in time order may treat a decreased revision as a violation (DS-I3, DS-I5).
- **B-4 · Equality is trustworthy.** Two episodes reporting the same revision present the same case data (DS-I4), so a viewer may treat an unchanged revision as unchanged statuses.
- **B-5 · Change is visible.** If an update changed a case's status between two episodes, the later episode presents the new status and its revision is strictly greater (DS-I4).
- **B-6 · Negative controls.** These observable outcomes are violations and must be treated as failures: (a) open count inconsistent with the details of the same presented view; (b) a presented view mixing two revisions; (c) a later episode reporting a revision smaller than an earlier episode's; (d) a later episode that begins after an update completed but still presents the pre-update status.

## Examples

Numbers in the examples are illustrative (DS-U3).

- **X-1 · No change (legal).** At revision 1 the store holds `C-1 OPEN`, `C-2 OPEN`. Episode 1 presents revision 1, open count 2, details `C-1 OPEN`, `C-2 OPEN`. No update follows. Episode 2 presents the same. *Acceptance: B-1, B-4.*
- **X-2 · Change between an episode's two reads (the important exception).** Episode 1 has already read its overview (revision 1, open count 2). Before its details are presented, `C-1 → CLOSED` completes (revision 2, open count 1). Legal outcomes: the episode presents the revision-1 pair (open count 2 with `C-1 OPEN`) or the revision-2 pair (open count 1 with `C-1 CLOSED`) — but not a revision-1 overview combined with revision-2 details. *Acceptance: B-1.*
- **X-3 · Change before a later episode (legal).** Episode 1 presents revision 1 with 2 open. `C-1 → CLOSED` completes. Episode 2 begins; it must not present revision 1, and it presents 1 open with `C-1 CLOSED`. *Acceptance: B-2, B-3, B-5.*
- **X-4 · Two changes between episodes (legal).** After `C-1 → CLOSED` and then `C-2 → CLOSED` complete, the next episode presents 0 open with both cases CLOSED and a revision greater than the first episode's. *Acceptance: B-2, B-5.*
- **X-5 · Unknown case id (exception, not fixed here).** An update naming a case id not in the case set leaves every status unchanged (DS-I7); whether the revision advances is not constrained (DS-U2). If it advances, the episode still satisfies B-1, B-3 and B-4: a revision may change with unchanged case data, while changed case data under an equal revision is a violation.
- **X-6 · Empty case set (legal).** A store with no cases presents an overview with open count 0 and empty details (the seed numbers its initial revision 1; DS-U3 does not fix the starting number). *Acceptance: B-1.*

## Permitted variants (not gaps)

- **P-1.** An episode may stay pinned to the revision current at its start, or switch to a newer revision when an update lands mid-episode, provided its presented view is coherent (B-1). No particular way of signalling a mid-episode refresh is required.
- **P-2.** An episode may read its details before its overview, or interleave reads, provided B-1 holds for what is presented.
- **P-3.** Revision values need not be contiguous or start at any particular number (DS-U3); only the ordering, equality and freshness relations are fixed.

## Open items (not decided here)

- **B-O1.** If an update lands mid-episode, whether the viewer sees a visible refresh (and in what form) or silently keeps the pinned revision: either is legal under P-1; whether the exercise fixes one is left to the D design.
- **B-O2.** Persistence across process restarts, concurrent viewers, and case-set membership changes are outside this exercise (see DS-U4); introducing any of them would require a new B version.
# M3 case 2 · Domain semantics (C) — case, view, revision and invariants

Definitions and invariants for the same isolated synthetic fixture. Meaning only: observable acceptance is owned by `BEHAVIOR-CONTRACT.md` v1 and is not restated. Not a UCBIP or product domain model; it must not be cited or generalized outside this fixture.

- **Version:** v1 · 2026-10-01
- **Owner:** `tpw-night-m3-bc` — B/C authoring instance for this exercise.
- **Scope:** meaning of the exercise's domain terms and the invariants B/D may rely on, for one case-store lineage in this fixture. No module responsibility, interface, technical plan or implementation is defined here.
- **Conditions:** valid only against the inputs below; any change to `CASE-INPUT.md`, the recorded source structure, or `BC-CHARTER.md` invalidates this acceptance and requires a new C version. If a fixture fact conflicts with a definition below, that is an open item to report, not a reason to silently redefine the term. D may rely on these meanings and may not silently change them.
- **Acceptance status:** **ACCEPTED** for the isolated exercise only, by the owner under `BC-CHARTER.md` (instance `tpw-night-m3-bc-contract`). Author acceptance, not independent evaluation. No product generalization is accepted or implied.
- **Produced by:** Pi session `01a0f39e-8658-7478-ad5e-b1870bb69bd6`; runtime verified from the process environment as `commandcode / deepseek/deepseek-v4.1-flash / max`.

## Inputs used (exact hashes)

- **`CASE-INPUT.md`** — `sha256 50063486b149fc599464cb5cb25872cc9b4c4b971d1fcbc2eab0efdabeffd772`
- **Fixture source structure** (`src/**`, `tests/**`) — aggregate `sha256 dbd6a306815bdc4cf3a33be14b38d4dd62b49d1535d7db41b9064eb07e51b474`
  - `src/__init__.py` — `sha256 a5f855a87138b8c9a515d76a2b7858da6bba6fb60eff9446197fafc774733cf4`
  - `src/case_reader.py` — `sha256 89f05180854b8cb38b58299f516e7298cd2d211b88bed38f35087e6b1fe350bc`
  - `src/page_summary.py` — `sha256 59bffca2096cdb3818a202e552fa5214dd3f263466fd4799b3d7ba4e4fac2fc4`
  - `src/service.py` — `sha256 ea3fff5faf10d3025b19a07cc709985467b9dc67e607282ff1c87c73ddd66a0d`
  - `src/state_store.py` — `sha256 90a1cb56549f5afdbae24d2b485f8a956e66081939159a435aa83e2f43029196`
  - `src/turn.py` — `sha256 5de7b6c681f8379e567d9be455a3176a48c429ca460b6810092ff7ae46504ac0`
  - `tests/test_existing_behavior.py` — `sha256 9ac7ea872b8c50f921128e7a8d734539b273551e7d6e9363e3d5116103c7876f`
  - aggregate recipe: sort the lines `<per-file sha256><two spaces><path relative to this fixture directory>`, join with `\n`, append a final `\n`, then take the sha256 of that UTF-8 text.
- **`BC-CHARTER.md`** (delegation) — `sha256 1395a01731f1ea4885b2e20c157ec47ba607e27fe8e2037006287562d3dd57ba`
- **`professional-workflow/profiles/behavior-domain.md`** (accepted Profile, per Charter) — `sha256 d8b75a5734c015f70d4c3f1479e094be11b92f2ee20d193dc22726fd599377fa`

## Terms

- **Case.** A tracked item identified by `case_id`, carrying exactly one current status. Case ids are opaque strings; this exercise assumes a view's case set has unique ids, and treats duplicates as outside the contract.
- **Case status.** A label on a case. This exercise defines two labels: `OPEN` (still pending) and `CLOSED` (no longer pending). A case is **open** iff its status is exactly `OPEN`. The **open count** of a view is the number of its open cases. Meaning of any other label is undefined here (DS-U1).
- **Case set.** The cases a view contains, in the presented order. This exercise does not change membership (DS-U4).
- **View (state view).** A complete assignment of one status to every case of a case set at one point in the store's history. Two views are **identical** iff they contain the same case ids, in the same order, with the same statuses.
- **Revision.** An integer tag identifying a view within one store lineage; its ordering, equality and freshness semantics are the invariants below.
- **Update (status update).** An operation naming one case id and one new status; its effect is DS-I7. An update is **completed** once its result is part of the store's history — in this single-threaded fixture, when the call returns.
- **Read episode.** As defined in `BEHAVIOR-CONTRACT.md` §Observable surface; C uses the term and does not redefine it.
- **Coherent / coherence.** A set of observations is coherent when one revision explains every observation in the set.
- **Presented view.** As defined in `BEHAVIOR-CONTRACT.md` §Observable surface; the invariants below constrain it.

## Invariants

- **DS-I1 · Episode coherence.** For any presented view, its overview observation and its details observation belong to exactly one revision. No presented view mixes two revisions.
- **DS-I2 · Count fidelity.** For any presented view, the open count equals the number of cases whose status is `OPEN` among that view's own details, and the overview's revision is the revision those details belong to.
- **DS-I3 · Monotonicity.** Within one store lineage, revision never decreases as updates complete.
- **DS-I4 · Revision identity.** Two observations with the same revision describe identical case data. If two observations show different statuses for the same case, their revisions differ, and the observation made later in time has the greater revision. (A revision may change without case data changing; case data cannot change without the revision changing.)
- **DS-I5 · Freshness.** If one or more updates completed before a read episode begins, the episode's presented view has a revision greater than or equal to the resulting revision of every such update — equivalently, a new episode cannot render older than the newest completed update at its start.
- **DS-I6 · Scope.** Revisions are comparable only within one store lineage; revisions of different stores are unrelated numbers.
- **DS-I7 · Update locality.** An update names one case id. The view after the update differs from the view before it only in that case's status when the id is present; when the id is not present, every case status is unchanged.

## Distinguishing examples

- A view over `C-1 OPEN`, `C-2 CLOSED` has open count 1: the count is derived from the same view's statuses (DS-I2), not from a separately read list.
- Revision 4 in one store and revision 4 in another store are unrelated (DS-I6).
- An update naming `C-9` (not in the set) leaves all statuses unchanged (DS-I7); whether the revision advances is DS-U2.
- Two observations showing `C-1 OPEN` and `C-1 CLOSED` cannot have the same revision (DS-I4); a presented view showing both descriptions of `C-1` is incoherent (DS-I1).

## Unresolved semantic questions (not decided here)

- **DS-U1.** Meaning and count treatment of statuses other than `OPEN`/`CLOSED`: undefined in this exercise; the seed store accepts arbitrary strings and this fixture holds no business authority to rule on them.
- **DS-U2.** Whether an update that leaves every status unchanged (unknown case id) advances the revision: not constrained. If it does, DS-I4 still holds.
- **DS-U3.** The numbering scheme (start value, step): not fixed; only the DS-I3/DS-I4 ordering and equality relations are required. The seed starts at 1 and steps by 1; the examples' numbers are illustrative.
- **DS-U4.** Case-set membership changes (creation or removal of cases): outside this exercise; if ever introduced, revision identity (DS-I4) must be re-derived for the new view type before it can be relied on.
# M3 case 2 · pre-contract seed observation

This observation is from the fixture seed, before any cross-module B/C contract, D Plan, or implementation candidate was added.

- Runtime: Python 3.14.4.
- Command, run from this fixture directory: `python3 -m unittest discover -s tests -v`.
- Exit: `0`; 3 existing module-level checks passed.
- Current code exposes `StateStore.current_view()`, `page_summary.build_page_summary()`, `turn.begin_turn()`, and `case_reader.read_cases()` through separate modules. The tests cover each current operation but do not assert a coherent snapshot spanning a turn.
- No D Plan or implementation candidate exists at this baseline.

The new cross-module behavior is not part of this seed; its accepted B/C inputs will be recorded separately before D planning begins.
# M3 case 2 · offline snapshot fixture seed

This seed is an intentionally small, dependency-free Python system for a later exercise. It contains a page summary, a turn wrapper and a case reader. The seed predates the cross-read snapshot contract; the accepted exercise B/C objects are now `BEHAVIOR-CONTRACT.md` v1 and `DOMAIN-SEMANTICS.md` v1.

Run the existing smoke tests from this directory with:

```sh
python3 -m unittest discover -s tests -v
```

The B/C authoring input is `CASE-INPUT.md`; it states the goal without selecting a module, interface or implementation. B/C outputs are now fixed. D may prepare a Plan; E implementation begins only after an independent challenge and acceptance of that Plan.
from dataclasses import dataclass


@dataclass(frozen=True)
class CaseRecord:
    case_id: str
    status: str


@dataclass(frozen=True)
class StateView:
    revision: int
    cases: tuple[CaseRecord, ...]


class StateStore:
    def __init__(self, cases: tuple[CaseRecord, ...]):
        self._current = StateView(revision=1, cases=cases)

    def current_view(self) -> StateView:
        return self._current

    def update_status(self, case_id: str, status: str) -> None:
        cases = tuple(
            CaseRecord(case.case_id, status if case.case_id == case_id else case.status)
            for case in self._current.cases
        )
        self._current = StateView(revision=self._current.revision + 1, cases=cases)
from .state_store import StateStore


def build_page_summary(store: StateStore) -> dict[str, int]:
    view = store.current_view()
    return {
        "revision": view.revision,
        "open_count": sum(case.status == "OPEN" for case in view.cases),
    }
from dataclasses import dataclass

from .page_summary import build_page_summary
from .state_store import StateStore


@dataclass(frozen=True)
class Turn:
    page_summary: dict[str, int]


def begin_turn(store: StateStore) -> Turn:
    return Turn(page_summary=build_page_summary(store))
from .state_store import CaseRecord, StateStore


def read_cases(store: StateStore) -> tuple[CaseRecord, ...]:
    return store.current_view().cases
from .case_reader import read_cases
from .state_store import StateStore
from .turn import Turn, begin_turn


def start(store: StateStore) -> Turn:
    return begin_turn(store)


def cases(store: StateStore):
    return read_cases(store)
import unittest

from src.service import cases, start
from src.state_store import CaseRecord, StateStore


class ExistingSnapshotFixtureTests(unittest.TestCase):
    def setUp(self):
        self.store = StateStore((CaseRecord("C-1", "OPEN"), CaseRecord("C-2", "OPEN")))

    def test_summary_counts_current_open_cases(self):
        turn = start(self.store)
        self.assertEqual(turn.page_summary["open_count"], 2)

    def test_case_reader_returns_current_cases(self):
        self.assertEqual(len(cases(self.store)), 2)

    def test_update_changes_next_current_read(self):
        self.store.update_status("C-1", "CLOSED")
        self.assertEqual(self.store.current_view().revision, 2)
        self.assertEqual(cases(self.store)[0].status, "CLOSED")


if __name__ == "__main__":
    unittest.main()
