# M3 case 2 - F independent evaluation startup packet

Fixed treatment: commit 17602f2b12822aba88785e27a733f75a3238214d, tree f9b4f90b9e5a0c7ae11dfe681b82a4a22dddef03.
Fixed baseline: commit 2ad72273c6aa7dd9cb9775d9146a6fd549db19b1, tree f7f3fb2524a8f6a7ad125c0f45a6564d29139744.
Confidentiality: this packet contains public accepted inputs and candidate evidence only. It contains no private F rubric or expected verdict. Apply the separate case-2 criteria already held by this F session and do not reproduce those criteria in the report.

## Evidence Evaluation Profile (M1 accepted)
Source: professional-workflow/profiles/evidence-evaluation.md
SHA-256: d72b3a5097f142f5ea397ab423b146a3b853913c5c1de096d93b95133199f900

# Evidence Evaluation · 证据与验证（F）

一句话：对明确对象、版本与覆盖给出证据判断；不因 PASS 授予关闭或发布许可。

> 选用本预设不获得任务授权。本次责任、范围、输入、输出、工具与独立性由 Instance Charter 绑定；本预设只提供专业心智模型、误区与方法入口。

## 心智模型

- F 工作面：验证设计、获取实际证据、评价证据与反例；必要时在实现前指出设计不可观察、依据矛盾或假设不可行。
- 三态只有 PASS / FAIL / UNVERIFIED；环境故障记 UNVERIFIED，不算 PASS，也不判为产品缺陷。
- 独立是真实属性：评价者不得是被评价候选的实现者；正常质疑与反例不自动构成作者贡献，实质代做要重新判断该部分的独立性。
- 证据针对明确的对象与版本；测试通过不证明目标价值已实现，实现符合 Plan 也不证明 Plan 的责任放置正确。
- 评价标准来自被接受的 B/C/D 与质量政策；不能改预期后宣布成功。

## 关键问题

- 被评价的确切对象、版本与 claim 是什么？覆盖到哪里，没覆盖什么？
- 什么观察能把"成立"与"不成立"分开？关键负控制是什么？
- 证据来源与作者关系是什么？我在本次对象上的独立性如何，需不需要分开？
- 依据本身有没有冲突或缺失？该退回 B、C、D 还是 A？
- 结果能否被另一个会话按材料复现？

## 常见误区

- 只验证"能跑通"，不设计能揭示错误的负控制。
- 把文档、字段非空、自测输出当作已验证结论。
- 把环境/工具故障判成产品 FAIL；或把观察不足笼统写成 UNVERIFIED 而不说明阻断原因与剩余。
- 评价者顺手改成作者，再声称独立；或"戴不同帽子"充当独立性。
- 把评价结论当发布或风险接受授权。
- 只看实现，不回源核对 B/C 的接受状态与适用范围。

## 交接与召回

- 交出：对象/版本、依据、观察、覆盖限制与 PASS/FAIL/UNVERIFIED；单列实际独立性。
- 召回：实现违反约定返回 E；依据冲突或缺失返回 B/C/D；目标解释失准返回 A；环境阻断记录 UNVERIFIED 并说明。
- 设计挑战与结果评价可以是不同时点；复用评价前确认本次版本/差分仍在其覆盖内。

## 按需方法入口（候选）

- 验证设计方法：从 claim 反推可观察证据与负控制。
- 证据评价方法：区分观察、推断与结论，核对来源与独立性。
- 复现/取证方法：命令、环境、输入与输出如实记录，可被他人重放。
- 绑定状态：候选，待 M4 归位后绑定；本预设不含方法正文。

## Frozen Responsibility Backbone
Source: professional-workflow/authority/RESPONSIBILITY-BACKBONE.md
SHA-256: ce82a70016a4a3fc234ea287f39aac8d79a260ddf13747c4fb705bda580453ba

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

## Case-2 F Charter
Source: docs/overnight/2026-10-01/fixtures/m3-snapshot/M3-CASE2-F-CHARTER.md
SHA-256: 98ab5c2bd4db2da434e5ed0d7346c354af08e9870a8f367a316a2512bb11e26b

# M3 case 2 · F independent evaluation Charter

- **State:** active for evaluating the fixed case-2 E candidate only; this Charter records Owner-authorized verification and adds no publication authority.
- **Profile:** `professional-workflow/profiles/evidence-evaluation.md`, SHA-256 `d72b3a5097f142f5ea397ab423b146a3b853913c5c1de096d93b95133199f900` (M1-accepted Profile).
- **Instance:** `tpw-night-method` (Codex / gpt-6.1-sol / medium), independent of E author session `tpw-night-m3-local-impl`.

## Task and delegation

- **Task / outcome:** Independently evaluate the fixed case-2 implementation candidate against the accepted B/C behavior/domain claims and D Plan, applying the case-2 evaluation criteria held for this F instance. Return a three-state result and an auditable evidence report.
- **Delegation source:** Owner-authorized M3–M6 overnight exercise and the accepted case-2 input chain: B/C v2 (owner-accepted and independently reviewed), D-accepted Plan, and fixed E candidate. The Charter records the existing F responsibility; writing it does not create acceptance authority.
- **Object scope:** Read only the fixed candidate commit/tree and the public evidence listed in the startup packet. Do not edit the implementation, tests, B/C, Plan, Profiles, Charters, or any package file. May write only `M3-CASE2-F-EVALUATION.md`.
- **Accepted inputs:** B/C v2 (`6cf43d3f…` / `d35766b4…`), D-accepted Plan (`a3062057…`), and E candidate commit `17602f2b12822aba88785e27a733f75a3238214d`, tree `f9b4f90b9e5a0c7ae11dfe681b82a4a22dddef03`. Candidate file hashes and E self-report are fixed in the startup packet.
- **Applicable method:** `behavior-claim-evaluation.md` from M4 accepted commit `013659331c8c5f9f54b866b393972a03d7938773`, SHA-256 `06b0692290a9ce8cdc7048b33a89ec21f3636ee00138a613121ec4b72457af06`. It is a bounded baseline/treatment method, not a complete F workflow; its exact accepted body is included in the startup packet.

## Work and limits

- **Responsibility:** Apply the held case-2 criteria to this exact E candidate; assess the specified claims, evidence validity and coverage. Independently reproduce observations needed for a verdict; treat E's report as input, not as an F conclusion.
- **Verdict:** Use only `PASS`, `FAIL`, or `UNVERIFIED` with the accepted method's mapping. An invalid comparison or environment limitation is `UNVERIFIED`, not product `FAIL`.
- **Confidentiality/isolation:** The case-2 rubric is held by this F session and is not included in the E Charter, E startup packet, source/test files, or shared repository. Do not reproduce, quote, or expose the private criteria in the report. If the held criteria are not available in this session's context, do not infer or request them from E; return `UNVERIFIED` and state the missing-input limit without revealing private content. Report evidence and rationale in terms of public B/C and Plan claims.
- **Tools and actions:** Offline fixture only. Local test execution and ephemeral read-only copies of fixed Git objects are allowed for baseline/treatment comparison. Do not change the main candidate or any package/verification copy. No network, UCBIP, deployment, migration, release, push, merge, or commit.

## Handoff and return

- **Deliver:** `M3-CASE2-F-EVALUATION.md` with exact candidate identity, inputs and hashes, commands/results, claim-level evidence, verdict, coverage and limitations. Do not claim overall M3 acceptance.
- **Independence:** E implementation was authored by a different session. This F instance previously reviewed B/C and challenged the D Plan but did not author the case-2 implementation. Workspace migration adds no independence.
- **Acceptance / closure:** F owns the independent case result only. Driver integrates the evidence; Oracle/Owner milestone acceptance remains separate. F does not accept the D Plan, residual risk, or overall M3.

## Accepted M4 behavior-claim-evaluation method
Source: 0136593:professional-workflow/methods/behavior-claim-evaluation.md
SHA-256: 06b0692290a9ce8cdc7048b33a89ec21f3636ee00138a613121ec4b72457af06

# Behavior claim evaluation · M4 candidate

- **Method owner:** F verification. Independence comes from the active Charter and actual contribution record.
- **Status:** candidate for specific behavior claims; not a complete F workflow.

## Use

Use when a contract can be evaluated by comparing a concrete baseline with a treatment. Other F judgments, including whether a design is observable, can need other evidence.

## Method

1. State one falsifiable claim and its conditions, measure and threshold. Name the exact object and version.
2. Compare baseline and treatment with the same command, data and environment. Preserve the original output as evidence.
3. Decide whether the comparison is valid before interpreting its result. A missing/invalid baseline, noisy or incomparable data, failed measurement, or material environment difference makes the observation inconclusive.
4. Report the verdict, exact command and inputs, observed result, coverage and limitations.

## Verdict mapping

- **PASS:** a valid comparison supports the predicted direction and threshold, without a material confound.
- **FAIL:** a valid comparison provides a counterexample, shows no required change, or misses the stated threshold.
- **UNVERIFIED:** the comparison is not valid or the environment prevents a conclusion. Do not turn an invalid observation into product failure; do not turn missing evidence into PASS.

This mapping is semantic, not label substitution. In the source method, `VERIFIED` maps to PASS only when its conditions hold; `NOT VERIFIED` maps to FAIL only after a valid comparison; `INCONCLUSIVE` maps to UNVERIFIED. Independent authorship is not part of the measurement method and is not proved by a fresh instrument, model diversity or multiple labels.

## Limits

This method evaluates a specific observable claim, not user value or overall task closure. It does not accept residual risk or authorize release, deployment or other actions. The Charter must identify the actual evaluator and its independence for the object.

## Source anchors

Cursor Team Kit `verify-this` in `cursor-plugins` at `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`, `cursor-team-kit/skills/verify-this/SKILL.md` (`Workflow`, `Verdict Rules`, `Output`): falsifiable claim, baseline/treatment comparison, single verdict and evidence output.

## Behavior Contract B v2
Source: docs/overnight/2026-10-01/fixtures/m3-snapshot/BEHAVIOR-CONTRACT.md
SHA-256: 6cf43d3fb647cf2c250f275179762917c0763a669e84f1718d85968a8e66c738

# M3 case 2 · Behavior contract (B) — read-episode coherence and later-episode freshness

Isolated exercise contract for this synthetic fixture directory. It defines the externally observable behavior of the viewer exercise only. It is not a UCBIP rule and not a general product freshness policy; it must not be cited or generalized outside this fixture.

- **Version:** v2 · 2026-10-01 — supersedes v1 (`sha256 86dd6664b73de07ceefdbc5f4d03e09f49b4b1f2ee11cb6a80e48c251176555c`), which remains recoverable at commit `893eaf8`. v2 changes only the Conditions, the aggregate recipe and version metadata; the acceptance below is unchanged from v1.
- **Owner:** `tpw-night-m3-bc` — B/C authoring instance for this exercise.
- **Scope:** observable behavior of a read episode, and of a later read episode, over one case-store lineage in this fixture. Meanings of the terms used here (case, status, view, revision, update, coherence) are owned by `DOMAIN-SEMANTICS.md` v2 and are not restated.
- **Conditions:** accepted against the baseline inputs below. Those hashes identify the fixture state the contract was authored against — the **accepted baseline** — not a continuing no-change condition on the fixture source tree.
  - **Inherits this acceptance (no new B/C version needed):** diffs under `src/**` and `tests/**` that preserve every acceptance item below and the observable quantities it uses (`revision`, `open_count`, `case_id`, `status`) — including new or amended tests, added coordination behaviour, internal decomposition and renames, and the interface shape D selects. The authorized D/E exercise is expected to produce such diffs; changing the recorded bytes is not by itself an invalidation.
  - **Requires a new B/C version:** a change that alters an acceptance item (B-1…B-6), the observable surface, the read-episode / presented-view model, the freshness anchor (updates completed before an episode begins), or the scope notes in B-O2; a change to `DOMAIN-SEMANTICS.md` terms or invariants (B-1…B-6 cite them); or a change to `CASE-INPUT.md` (exercise goal) or `BC-CHARTER.md` (delegation and scope). Until a new version is accepted, the changed part is not covered by this acceptance.
  - This document and `DOMAIN-SEMANTICS.md` are accepted as a pair (both at v2); a new version of either is re-issued together.
  - **Seed status:** the seed's current split-read behavior is evidence of the starting system, not this contract, and does not by itself satisfy the acceptance below.
  - This document defines behavior only: it does not assign module responsibility, select an interface, prescribe implementation, write a technical plan, or authorize implementation.
- **Acceptance status:** **ACCEPTED** for the isolated exercise only, by the owner under `BC-CHARTER.md` (instance `tpw-night-m3-bc-contract`), as `BEHAVIOR-CONTRACT.md` v2 paired with `DOMAIN-SEMANTICS.md` v2. Author acceptance, not independent evaluation. No product generalization is accepted or implied.
- **Produced by:** Pi session `01a0f39e-8658-7478-ad5e-b1870bb69bd6`; runtime verified from the process environment as `commandcode / deepseek/deepseek-v4.1-flash / max`.

## Inputs used (exact hashes)

**Accepted baseline** (recorded at v1 acceptance on 2026-10-01; the baseline identity this contract was authored against, not a continuing no-change condition — see Conditions):

- **`CASE-INPUT.md`** — `sha256 50063486b149fc599464cb5cb25872cc9b4c4b971d1fcbc2eab0efdabeffd772`
- **Fixture source structure** (`src/**`, `tests/**`) — aggregate `sha256 dbd6a306815bdc4cf3a33be14b38d4dd62b49d1535d7db41b9064eb07e51b474`
  - All seven per-file hashes below were independently re-verified on 2026-10-01 against both the worktree and commit `893eaf8`:
  - `src/__init__.py` — `sha256 a5f855a87138b8c9a515d76a2b7858da6bba6fb60eff9446197fafc774733cf4`
  - `src/case_reader.py` — `sha256 89f05180854b8cb38b58299f516e7298cd2d211b88bed38f35087e6b1fe350bc`
  - `src/page_summary.py` — `sha256 59bffca2096cdb3818a202e552fa5214dd3f263466fd4799b3d7ba4e4fac2fc4`
  - `src/service.py` — `sha256 ea3fff5faf10d3025b19a07cc709985467b9dc67e607282ff1c87c73ddd66a0d`
  - `src/state_store.py` — `sha256 90a1cb56549f5afdbae24d2b485f8a956e66081939159a435aa83e2f43029196`
  - `src/turn.py` — `sha256 5de7b6c681f8379e567d9be455a3176a48c429ca460b6810092ff7ae46504ac0`
  - `tests/test_existing_behavior.py` — `sha256 9ac7ea872b8c50f921128e7a8d734539b273551e7d6e9363e3d5116103c7876f`
  - aggregate recipe: order the files under `src/**` and `tests/**` by their relative path ascending (Python `sorted()` on the path string), then emit one line per file as `<per-file sha256><two spaces><relative path>`, join the lines with `\n`, append a final `\n`, and take the sha256 of that UTF-8 text. This path order yields the recorded aggregate. Sorting the digest-prefixed lines themselves instead yields `sha256 9074f27da8e0d76113bda8f774297c7c8fbceaedaf67d6ea75eec87d2421e88c`, which is not the recorded value.
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

## Change log

- **v1 · 2026-10-01** — initial accepted contract; baseline inputs and per-file hashes recorded.
- **v2 · 2026-10-01** — challenge PC-1 bounded clarification: the recorded hashes are the acceptance **baseline**, not a continuing no-change condition on `src/**`/`tests/**`; in-scope implementation/test diffs inherit this acceptance, and only contract-content changes require a new B/C version. Challenge PC-2 bounded correction: the aggregate recipe now states the sort key explicitly (path order), with the digest-line-sorted value `9074f27d…` recorded as the non-matching alternative. No acceptance item or semantic claim was changed.

## Domain Semantics C v2
Source: docs/overnight/2026-10-01/fixtures/m3-snapshot/DOMAIN-SEMANTICS.md
SHA-256: d35766b45085db2b7e5b3315cca5ce4183f722186a850ef317fd571ebba6d45b

# M3 case 2 · Domain semantics (C) — case, view, revision and invariants

Definitions and invariants for the same isolated synthetic fixture. Meaning only: observable acceptance is owned by `BEHAVIOR-CONTRACT.md` v2 and is not restated. Not a UCBIP or product domain model; it must not be cited or generalized outside this fixture.

- **Version:** v2 · 2026-10-01 — supersedes v1 (`sha256 15537d71d100dde30075f724c1ef79bc0d4e6a76a179f7f82d7f6c6b286cda06`), which remains recoverable at commit `893eaf8`. v2 changes only the Conditions, the aggregate recipe and version metadata; the terms and invariants below are unchanged from v1.
- **Owner:** `tpw-night-m3-bc` — B/C authoring instance for this exercise.
- **Scope:** meaning of the exercise's domain terms and the invariants B/D may rely on, for one case-store lineage in this fixture. No module responsibility, interface, technical plan or implementation is defined here.
- **Conditions:** accepted against the baseline inputs below. Those hashes identify the fixture state the terms and invariants were defined against — the **accepted baseline** — not a continuing no-change condition on the fixture source tree.
  - **Inherits this acceptance (no new B/C version needed):** diffs under `src/**` and `tests/**` that keep these terms and invariants true — including implementation changes, new or amended tests, internal decomposition and renames. The authorized D/E exercise is expected to produce such diffs; changing the recorded bytes is not by itself an invalidation.
  - **Requires a new B/C version:** a change to any term definition or to DS-I1…I7; a change to this document that resolves or narrows DS-U1…U4 into new requirements (a D/E choice made freely inside DS-U3 is not such a change); any change to the case/view/revision model itself; a change to `BEHAVIOR-CONTRACT.md` acceptance items (C's terms are cited there); or a change to `CASE-INPUT.md` (exercise goal) or `BC-CHARTER.md` (delegation and scope). Until a new version is accepted, the changed part is not covered by this acceptance.
  - This document and `BEHAVIOR-CONTRACT.md` are accepted as a pair (both at v2); a new version of either is re-issued together.
  - **Conflict rule:** if a fixture fact conflicts with a definition below, that is an open item to report, not a reason to silently redefine the term. D may rely on these meanings and may not silently change them.
- **Acceptance status:** **ACCEPTED** for the isolated exercise only, by the owner under `BC-CHARTER.md` (instance `tpw-night-m3-bc-contract`), as `DOMAIN-SEMANTICS.md` v2 paired with `BEHAVIOR-CONTRACT.md` v2. Author acceptance, not independent evaluation. No product generalization is accepted or implied.
- **Produced by:** Pi session `01a0f39e-8658-7478-ad5e-b1870bb69bd6`; runtime verified from the process environment as `commandcode / deepseek/deepseek-v4.1-flash / max`.

## Inputs used (exact hashes)

**Accepted baseline** (recorded at v1 acceptance on 2026-10-01; the baseline identity these terms and invariants were defined against, not a continuing no-change condition — see Conditions):

- **`CASE-INPUT.md`** — `sha256 50063486b149fc599464cb5cb25872cc9b4c4b971d1fcbc2eab0efdabeffd772`
- **Fixture source structure** (`src/**`, `tests/**`) — aggregate `sha256 dbd6a306815bdc4cf3a33be14b38d4dd62b49d1535d7db41b9064eb07e51b474`
  - All seven per-file hashes below were independently re-verified on 2026-10-01 against both the worktree and commit `893eaf8`:
  - `src/__init__.py` — `sha256 a5f855a87138b8c9a515d76a2b7858da6bba6fb60eff9446197fafc774733cf4`
  - `src/case_reader.py` — `sha256 89f05180854b8cb38b58299f516e7298cd2d211b88bed38f35087e6b1fe350bc`
  - `src/page_summary.py` — `sha256 59bffca2096cdb3818a202e552fa5214dd3f263466fd4799b3d7ba4e4fac2fc4`
  - `src/service.py` — `sha256 ea3fff5faf10d3025b19a07cc709985467b9dc67e607282ff1c87c73ddd66a0d`
  - `src/state_store.py` — `sha256 90a1cb56549f5afdbae24d2b485f8a956e66081939159a435aa83e2f43029196`
  - `src/turn.py` — `sha256 5de7b6c681f8379e567d9be455a3176a48c429ca460b6810092ff7ae46504ac0`
  - `tests/test_existing_behavior.py` — `sha256 9ac7ea872b8c50f921128e7a8d734539b273551e7d6e9363e3d5116103c7876f`
  - aggregate recipe: order the files under `src/**` and `tests/**` by their relative path ascending (Python `sorted()` on the path string), then emit one line per file as `<per-file sha256><two spaces><relative path>`, join the lines with `\n`, append a final `\n`, and take the sha256 of that UTF-8 text. This path order yields the recorded aggregate. Sorting the digest-prefixed lines themselves instead yields `sha256 9074f27da8e0d76113bda8f774297c7c8fbceaedaf67d6ea75eec87d2421e88c`, which is not the recorded value.
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

## Change log

- **v1 · 2026-10-01** — initial accepted semantics; baseline inputs and per-file hashes recorded.
- **v2 · 2026-10-01** — challenge PC-1 bounded clarification: the recorded hashes are the acceptance **baseline**, not a continuing no-change condition on `src/**`/`tests/**`; in-scope implementation/test diffs inherit this acceptance, and only semantic changes require a new B/C version. Challenge PC-2 bounded correction: the aggregate recipe now states the sort key explicitly (path order), with the digest-line-sorted value `9074f27d…` recorded as the non-matching alternative. No term definition or invariant was changed.

## D-accepted Technical Plan
Source: docs/overnight/2026-10-01/fixtures/m3-snapshot/TECHNICAL-PLAN.md
SHA-256: a306205729a002fdf1bc4eac6a623849cb2198985f8a6fbae4ec4c00ec47e5b9

# M3 case 2 · Technical Plan (D)

**Status:** **ACCEPTED by D** for this fixture's technical Plan, within the `D-CHARTER.md` delegated technical-planning scope — acceptance record at §8.1 (2026-10-01). Independent affected-claim recheck **PASS** on the reviewed predecessor `bb8afeb1d7519cac8926e1553f30e83590b8fb0504f120120c09cd916e0823d3` (`M3-SNAPSHOT-PLAN-V2-RECHECK.md`, `sha256 e93ac8869c2f0c94eb6b9ea8ec91a265920406656d31eacf12cee5b9a25ce278`), whose single non-blocking wording finding is the §8 correction applied in this revision. This acceptance is **not** acceptance of B/C, not evaluation or acceptance of any implementation, not M3 closure, and not authorization to deploy, migrate, release or change UCBIP; it does not authorize implementation, and starting E remains Driver's arrangement under existing authorization.
- **Reconciliation input:** `M3-D-PLAN-RECONCILIATION-PROMPT.md` (`sha256 8cfc6872e9ca266a488f4bb739de94cc42d438e6788332439735bb3fefe0f9df`).
- **Acceptance input:** `M3-D-PLAN-ACCEPTANCE-PROMPT.md` (`sha256 9154e1c7308e325ffd7afa750255975c1d52f3f516c71f13e8b820a1d9071773`).

> ### Dependency eligibility after B/C v2 — former PC-1 blocking callout withdrawn
> B/C v2 resolves the conflict this callout described: the recorded hashes are the **accepted baseline** — the fixture state the contract was authored against — and **not** a continuing no-change condition on `src/**`/`tests/**`. In-scope implementation and test diffs that preserve every acceptance item and observable quantity (`revision`, `open_count`, `case_id`, `status`) **inherit** the acceptance — including new or amended tests, added coordination behaviour, internal decomposition, renames, and the interface shape D selects. Changing the recorded bytes is not by itself an invalidation.
> The former "E must not start" bar and the §5/§6 gating are **withdrawn**. What this does **not** do: it is dependency eligibility only — it does not authorize implementation. D acceptance for the delegated technical-planning scope is now recorded (§8.1); that acceptance likewise does not authorize implementation.
- **Plan owner / decision responsibility:** `tpw-night-m3-design` (D instance for this exercise).
- **Delegation:** `D-CHARTER.md` (`sha256 6a0e6b7da8f8861e5d37c4d242b7df473e3ede1ffa531e5c73edd92e2730609f`) — Owner-authorized offline exercise in `docs/OVERNIGHT-WORKFLOW-PLAN-2026-10-01.md`, fixed M3 plan baseline `496b0676e302e2d0eafba129ff61de4c203d258a`. Task input: `D-PLAN-INPUT.md` (`sha256 89b131138ead556a3f6ac46ab758237c230c8cb6b615a9af57c92238fb4b7374`).
- **Date:** 2026-10-01 · **Object scope:** this fixture directory only.

## 0. Inputs and verified version binding

All bindings this Plan depends on were recomputed and **matched**, including the fixed B/C v2 pair. One method-provenance item stays bounded and recorded rather than resolved by D (§0.2). B/C v2 replaced the v1 Conditions; the v1 objects remain recoverable at commit `893eaf8` and are cited here only as superseded history.

### 0.1 Verified bindings

| Input | Role / decision owner | sha256 (recomputed) | Result |
| --- | --- | --- | --- |
| `BEHAVIOR-CONTRACT.md` **v2** | accepted behavior; owner `tpw-night-m3-bc` | `6cf43d3fb647cf2c250f275179762917c0763a669e84f1718d85968a8e66c738` | match (fixed B/C v2 input) |
| `DOMAIN-SEMANTICS.md` **v2** | accepted meaning/invariants; owner `tpw-night-m3-bc` | `d35766b45085db2b7e5b3315cca5ce4183f722186a850ef317fd571ebba6d45b` | match (fixed B/C v2 input) |
| `M3-BC-V2-REVIEW.md` | independent v2 review (`tpw-night-method`) | `675f32ded97ed90013db7eb4d0e6e6ea56fdce702f28ad1ba9e94124a303d091` | match — **PASS** on PC-1/PC-2 resolution and v1 claim preservation |
| `M3-SNAPSHOT-PLAN-CHALLENGE.md` | prior Plan challenge v1 | `bf3e15de71f4bf82adaa5547b9c412b4384a90d9d919420d5023fd9f593ab126` | match (dispositioned in §0.3) |
| `CASE-INPUT.md` | B/C authoring input (v2 re-open condition: exercise-goal change) | `50063486b149fc599464cb5cb25872cc9b4c4b971d1fcbc2eab0efdabeffd772` | match |
| `BC-CHARTER.md` | B/C delegation (v2 re-open condition: delegation/scope change) | `1395a01731f1ea4885b2e20c157ec47ba607e27fe8e2037006287562d3dd57ba` | match |
| fixture source (`src/**`, `tests/**`) aggregate | **accepted baseline** identity (B/C v2) | `dbd6a306815bdc4cf3a33be14b38d4dd62b49d1535d7db41b9064eb07e51b474` | match (all 7 per-file digests also match) |
| `RESPONSIBILITY-BACKBONE.md` | authority export cited by the Charter | `ce82a70016a4a3fc234ea287f39aac8d79a260ddf13747c4fb705bda580453ba` | match |
| `profiles/technical-planning.md` | Plan profile cited by the Charter | `d53da06edc99af3bcfc93c744af5f2cc8d512430d318a8b13b1b7f42652d74aa` | match |
| `D-STARTUP-PROMPT.md` | this task's startup input | `0f6d0e4e028543676273b33c1d0c74e5d933da2ed033be3f9669ca83ac748c90` | match |
| `D-CHARTER.md` / `D-PLAN-INPUT.md` | delegation / task input | `6a0e6b7da8f8861e5d37c4d242b7df473e3ede1ffa531e5c73edd92e2730609f` / `89b131138ead556a3f6ac46ab758237c230c8cb6b615a9af57c92238fb4b7374` | read, cited above |

**Superseded, cited only as history (recoverable at commit `893eaf8`, not active bindings):** `BEHAVIOR-CONTRACT.md` v1 `86dd6664b73de07ceefdbc5f4d03e09f49b4b1f2ee11cb6a80e48c251176555c`; `DOMAIN-SEMANTICS.md` v1 `15537d71d100dde30075f724c1ef79bc0d4e6a76a179f7f82d7f6c6b286cda06`. B and C are accepted **as a pair at v2**; a new version of either is re-issued together, so the Plan cites both at v2 throughout.

**Aggregate recipe — now normative in B/C v2 and aligned here (challenge PC-2, closed).** v2 states the sort key explicitly: order the files under `src/**` and `tests/**` by **relative path ascending** (Python `sorted()` on the path string), emit one line per file as `<per-file sha256><two spaces><relative path>`, join the lines with `\n`, append a final `\n`, and hash the UTF-8 text. That path order yields the recorded `dbd6a306…`. Sorting the digest-prefixed lines themselves yields `9074f27da8e0d76113bda8f774297c7c8fbceaedaf67d6ea75eec87d2421e88c`, which is **not** the recorded value; v2 records it as the non-matching alternative. Both orderings were recomputed here and agree with v2.
*Superseded in this Plan:* the pre-reconciliation draft explained the divergence as a **locale** effect and raised R-10 asking the B/C owner to correct the recipe wording. **Both are withdrawn** — locale was never involved, and v2 already states the key, so no correction request to the B/C owner survives. **R-10 is closed and is no longer an active recall.**

**Embedded copies vs. on-disk files.** `BASELINE.md` and `README.md` as embedded in `D-STARTUP-PROMPT.md` are byte-identical to the files on disk, as is the embedded Backbone export. The embedded **B and C** sections are byte-identical to the **v1** objects at commit `893eaf8`, **not** to the v2 files now on disk — v2 post-dates the startup prompt. This is the expected consequence of the v2 revision, not a discrepancy: the v1 body and the v2 body are byte-identical apart from the Conditions/recipe/metadata changes (§0.1, A-4), so none of the accepted behavior or domain content this Plan reasons over was altered by the revision.

### 0.2 Method provenance — bounded, independently re-checked (challenge PC-3)

The Charter cites the applicable method as `methods/cross-module-design.md` "from accepted M4 commit `013659331c8c5f9f54b866b393972a03d7938773` (SHA-256 `30066c8b…`)". Three blobs are in play:

| Object | sha256 |
| --- | --- |
| method blob at the cited M4 commit `0136593` | `30066c8b3ccee2b85e98c8bc36975f57161e2c93d0bd71c9c668b27bf79bae6f` |
| method text embedded in `D-STARTUP-PROMPT.md` — the copy this Plan actually applied | `59e686d0a7e488e9c7ae3eb85090da947ad7ac6a68d2feea1b007e4f6ba1456c` |
| method blob at this Plan's candidate commit `e3b2d3c` | `ab0a0bc03448407479fe82b92b2355384e7f2acf49c2ff3026882670f955a0a5` |

- **Semantic equivalence holds.** The normative range (`## Use` … before `## Source anchors`) is byte-identical across all three revisions: `sha256 e68e8d983ec675ce4fa4d6dea625987c94c7c14dc1e8521500203ae373ba42b9`. Differences are confined to the title, the `Status:` metadata line and the trailing deferral/provenance sentence — **no step, limit, trigger, independence rule or acceptance right differs**, and all three defer the same alternatives. The challenger re-derived this independently from Git objects rather than accepting my statement.
- **Acceptance is external to a blob's self-label.** `ORACLE-ACCEPTANCE.md` §M4 fixes `0136593` (tree `2fc8db5e…`) and accepts “该 commit 上三份有界方法正文与选择入口” as dependable content, and states that a change of *acceptance-status wording or typesetting alone* does not require re-running semantics. The earlier draft of this section inferred an unresolved acceptance problem from the blob calling itself "candidate"; **that inference was over-strong and is withdrawn.**
- **Residual, bounded and non-blocking:** the blob applied is not byte-identical to the blob cited. That is a **provenance/recording** matter for Driver and the integration writer — record the embedded copy's origin and the equivalence differential, and D cites one fixed version. It raises no new question for the method owner and does not gate E. It becomes a method-coverage matter only if the *substantive* body ever changes.

The method text applied constrains *how* this Plan is written; it does not select B/C meanings and does not enlarge delegated authority.

### 0.3 Disposition of challenge v1

Fixed object re-verified by me in this repository: candidate commit `e3b2d3cbb8664466fc9fd6d7e461dab82752ec19`, tree `4024c85c47840ddcd5df3ca7a073813892263988`, Plan `bcc10e4829918532f695b2d8be838d1aa2a2b9b8556c7654b5b14f1ce44adc1a` — all match the challenge's fixation.

| Finding | Disposition |
| --- | --- |
| **PC-1** · R-2 + B/C Conditions made any authorized implementation invalidate the acceptance it depends on | **Resolved upstream and verified closed.** B/C v2 Conditions redefine the recorded hashes as the **accepted baseline** — not a no-change condition — and state that in-scope `src/**`/`tests/**` diffs preserving the acceptance items and observable quantities inherit the acceptance. `M3-BC-V2-REVIEW.md` independently returned **PASS** on that resolution. The former blocking R-2 and the ⛔ callout are removed; §5/§6 gating is lifted. |
| **PC-2** · aggregate divergence is path-order vs digest-line-order, not locale | **Accepted; this Plan's factual error, now aligned.** The incorrect recipe explanation and the locale attribution are withdrawn in §0.1, the path-order key is stated to match the now-normative B/C v2 wording, and **R-10 is closed**. |
| **PC-3** · R-9 is bounded provenance, not a blocker; equivalence independently verified; M4 acceptance of `0136593` already recorded | **Accepted.** §0.2 rewritten; R-9 downgraded from "unresolved binding" to a recording action. |
| **PC-4(1)** · D-1/D-5 are not purely interior; name them bounded delegated coordination decisions, require the chosen entry point/episode boundary to be recorded | **Accepted.** §3 relabelled; recording obligation added. |
| **PC-4(2)** · the lazy-resolution sentence in D-5 must not imply any deferred first read is conformant | **Accepted.** D-5 tightened to the declared episode start of C-3. |
| **PC-4(3)** · C-2 is too absolute; re-read+validate is legitimate when both observations share one revision | **Accepted.** C-2 restated as *this Plan's* technical strategy, not a B-level prohibition. |
| **PC-4(4)** · R-7 "no shared state" is inaccurate; `StateStore` is a shared mutable reference | **Accepted; wording error.** R-7 corrected, and deliberately not turned into a safety conclusion. |

Not re-litigated (challenger-supported, unchanged): the core coherence direction, the X-2 falsifier as a discriminating observation, the pinned policy within B-O1/P-1, and the retained-versus-added coverage split.

## 1. Observed system facts (evidence, not prescription)

All of the following is from reading the actual fixture files and from a read-only in-process probe (`PYTHONDONTWRITEBYTECODE=1`; no file written, no test added).

**1.1 Structure.** `StateStore` holds `_current: StateView`; `StateView(revision, cases)` and `CaseRecord(case_id, status)` are frozen dataclasses with a `tuple[CaseRecord, ...]`. `page_summary.build_page_summary(store)` resolves `current_view()` once and returns a fresh `dict` carrying `revision` and `open_count`. `case_reader.read_cases(store)` resolves `current_view()` **again** and returns the case tuple. `turn.begin_turn` wraps the summary; `service.start` / `service.cases` are thin compositions.

**1.2 Enabling fact — the snapshot is a sound coherence unit.** `update_status` never mutates: it rebuilds the tuple and **rebinds** `self._current` to a new `StateView`. The old view therefore never changes. Observed:

```
captured view stable under later update?: True  [('C-1','CLOSED'),('C-2','OPEN')] -> [('C-1','CLOSED'),('C-2','OPEN')]
```

So a single captured `StateView` pins revision *and* statuses together, and holding it is sufficient to satisfy DS-I1/DS-I2 by construction.

**1.3 The defect — two independent resolutions of one presented view.** Each individual read is self-consistent; nothing binds them. Reproduced on the unmodified seed:

```
overview            : {'revision': 1, 'open_count': 2}
details             : [('C-1', 'CLOSED'), ('C-2', 'OPEN')]
store revision now  : 2
open count in details: 1
B-1/DS-I2 count-faithful?  False
B-6(a)/(b) violation?      True
```

This is exactly B's negative control X-2 illegal outcome. The cause is localized: `page_summary` and `case_reader` each call `store.current_view()` separately, so a completed update between the two calls yields a revision-1 overview with revision-2 details.

**1.4 Already-conformant behavior (do not "fix").** `open_count` counts exactly `status == "OPEN"` and is derived from the same view whose revision it reports, so DS-I2 holds *within* the overview. `update_status` preserves case order and, for an absent id, leaves every status unchanged (DS-I7). Revision always advances on update — legal under DS-I4 (revision may change with unchanged data) and DS-U2. Empty case set: `{'revision': 1, 'open_count': 0}` with empty details, per X-6. The existing suite passes 3/3, matching `BASELINE.md`.

**1.5 Coverage gap.** The three existing checks cover the module operations only. None asserts coherence spanning the overview/details pair — `BASELINE.md` says so and the test file confirms it.

## 2. Commitments — what others must rely on

Each commitment is a coordination surface: changing it forces a dependent to change semantics, interface, constraint or verification basis. Basis and owner are cited. **D does not acquire B/C's decision authority by writing these.**

- **C-1 · One resolution per presented view.** Every presented view is derived from **exactly one** resolution of `StateStore.current_view()`. The overview's `revision` is that view's revision; the details are that view's cases; `open_count` is computed from that same view's statuses. *Basis:* B-1, B-6(a)(b); DS-I1, DS-I2. *Owner of the requirement:* B/C (`tpw-night-m3-bc`). *Forbids:* pairing an overview and details produced by two separate reads.

- **C-2 · Coherence is structural under this Plan's chosen strategy (challenge PC-4(3) correction).** *This is D's technical strategy for this fixture, not a claim about what B forbids.* A re-read-and-validate scheme is legitimate when the observations it pairs carry the **same** revision, because coherence then follows from that revision's identity (DS-I4); it fails only when it leaves an already-obtained overview belonging to a different revision. This Plan deliberately chooses **single-resolution structural binding with no retry/reconcile path**, so the straddle cannot arise at all. *Basis:* B-1 with X-2; DS-I1/I4. *Consequence:* the binding unit is the **pair**. *Effect of deviating:* substituting a reconcile-on-mismatch design is a **Plan-conformance** question for E, not a B violation in itself.

- **C-3 · Episode policy is pinned (B-O1 resolved).** An episode resolves its view at its start and reuses it; no mid-episode refresh, no visible-refresh signal. Freshness at episode start is therefore automatic: the view current at start already includes every update completed before the episode began. *Basis:* B-O1 delegates this choice to D; P-1 permits pinning; DS-I3/I5. *Owner of the choice:* D (this Plan). *A weaker alternative is also legal* (switching to a newer revision mid-episode, P-1) — noted at U-4 as an open preference question, not offered as a second policy in this Plan.

- **C-4 · Published views are immutable.** `update_status` must continue to publish a **new** `StateView` and must not mutate a previously published one; `CaseRecord`/`StateView` statuses must remain value-immutable for the lifetime of any pinned view. This is what makes C-3 sound; breaking it fails silently. *Basis:* observed 1.2; DS-I4. *Basis for the constraint:* the pin depends on it, so it is a coordination surface, not an interior choice.

- **C-5 · Observations are values, not live aliases.** The overview and details a caller receives must be immutable or freshly copied, so a pinned presented view cannot change after an update. *Basis:* DS-I1/I2 must hold at presentation time, not merely at read time. *Current code already satisfies this* (fresh `dict`, tuple of frozen records) — preserve it.

- **C-6 · Count rule unchanged.** `open_count` counts exactly `status == "OPEN"`; a case is open iff its status is exactly `OPEN`. Do not add handling, validation, normalization or inference for other labels. *Basis:* C §Terms (open), DS-I2, DS-U1 (undefined; **no authority in this fixture to rule**). *Forbids:* resolving DS-U1 as a side effect of implementation.

- **C-7 · Case order and membership unchanged.** Preserve presented order; do not sort, dedupe or add cases. *Basis:* C §Terms (case set "in the presented order"; two views identical iff same ids in same order with same statuses), DS-I7. Duplicate ids remain outside the contract.

- **C-8 · Compatibility is additive.** Existing call forms `service.start(store) -> Turn` with `page_summary["revision"]`/`["open_count"]`, and `service.cases(store) -> tuple[CaseRecord, ...]`, remain callable with a bare `StateStore` and keep their current results when no update interleaves. The three existing checks stay passing and are **not** deleted or weakened. *Basis:* method step 6 (prefer additive when consumers must remain compatible); DS-U3 notwithstanding, `tests/test_existing_behavior.py` asserts a fresh store starts at revision 1 and one update makes it 2 — so keep start 1 / step 1. *Owner of the compatibility requirement:* D; the coverage itself belongs to the fixture's recorded structure.

- **C-9 · Deterministic, in-process, no new resources.** The coherence mechanism must be exercisable in-process against a bare `StateStore`: no clock, thread, sleep, I/O, retry loop, locking or persistence. *Basis:* method step 3 (seam for the actual dependency shape: in-process, locally replaceable, no true external dependency) and B-6's need for deterministic observation.

- **C-10 · No new observable behavior.** The change adds nothing beyond B-1…B-6. No new exceptions for in-contract inputs, no logging contract, no error semantics beyond what exists, no membership/persistence/concurrency features. *Basis:* B's scope; DS-U4 / B-O2 (outside the exercise); Charter "do not select new product behavior".

- **C-11 · No performance or ordering commitment is added.** No latency, throughput, buffering or ordering guarantee beyond the coherence relation itself; no performance characteristic of this interface becomes something a caller may rely on. *Basis:* method step 2 asks for "relevant performance characteristics" — here the honest answer is that none is relevant to the accepted claims, and inventing one would enlarge the objective.

## 3. Delegated Decisions — bounded coordination choices delegated to E

These are delegated, not prescribed (method step 5: planner preference alone is not a reason to fix them). Per challenge PC-4(1) they are **not** treated as invisible internals: because F and the next consumer must be able to locate the concrete entry point and episode boundary, **E must record the actual choice it makes** — entry point, episode boundary, carrier and pin representation — in its handoff, mapped to C-1…C-10. Nothing here licenses a change to semantics, interface, constraint or verification basis; that is R-4 territory, not delegation. B v2 Conditions explicitly list "the interface shape D selects" among the `src/**`/`tests/**` diffs that inherit the acceptance, so this delegation sits inside the inherited envelope — subject to the same re-open conditions (R-2).

- **D-1 · The carrier shape for a coherent pair (bounded delegated coordination decision).** Whether this is a single producer returning overview and details together, an episode/handle object created at open, an optional revision or pin argument with a store-only fallback, or a pin stored on `StateStore`. Naming and module placement are also E's. *Constraint:* C-1, C-2, C-8, C-9. *Must be recorded:* the concrete entry point a consumer or verifier calls and the episode boundary it establishes (D-5). *Explicitly not prescribed* — `D-PLAN-INPUT.md` states it intentionally does not prescribe module ownership or a token/argument shape, and I am not inventing one.
- **D-2 · Whether the pin is materialized or implicit**, i.e. a stored `StateView` reference versus producing the pair within one call so no separate pin exists. Same constraints.
- **D-3 · Reuse `Turn` as the carrier or add another**, provided `turn.Turn.page_summary` keeps its two keys and meaning (C-8) and the addition is additive.
- **D-4 · `DS-U2` — revision advance on a no-op update.** The seed advances the revision even when the named id is absent. Keeping or changing this is E's, since C leaves it unconstrained and B's X-5 permits either. *Constraint:* DS-I4 must hold, C-8 must hold, C-10 applies.
- **D-5 · Where the episode boundary is drawn in a fixture with no viewer/session object (bounded delegated coordination decision).** B defines the episode from opening the view to the next user action; the fixture has no such object. E may model it as exactly one pair-producing call, or as an explicit open step. *Constraint:* the resolution point must be well-defined and atomic with respect to updates — in this single-threaded fixture, inside one Python call. A lazy (first-use) resolution is conformant **only if it occurs at the episode start declared under C-3**, i.e. the moment the caller's episode opens; a deferred first read that happens *after* further updates have completed is a different episode boundary, not a lazy pin, and must not be presented as satisfying C-3. Either way a presented view never resolves twice (C-1). *Must be recorded:* which boundary was chosen, so F and the next consumer can find it.
- **D-6 · Local types, refactors, and the structure of new tests**, consistent with the existing `unittest` style and with C-9.

## 4. Recall Conditions — when to come back

Return through Driver to the cited authority. Do not silently resolve any of these.

- **R-1 · B/C change.** Any need to alter, reinterpret or extend an accepted B/C meaning, or any finding that a B/C input conflicts: name the affected accepted object, the observed fact and the impact → Driver → `tpw-night-m3-bc`. D does not decide it.
- **R-2 · B/C acceptance scope (was the PC-1 blocker — resolved by B/C v2, retained in narrowed form).** Per B/C v2 Conditions the recorded hashes are the **accepted baseline**, not a no-change condition: in-scope `src/**`/`tests/**` diffs that preserve every acceptance item and observable quantity **inherit** the acceptance, and changing the recorded bytes is not by itself an invalidation. **A new B/C version is still required** — and the changed part is not covered until one is accepted — for a change that alters any acceptance item (B-1…B-6), the observable surface, the read-episode / presented-view model, the freshness anchor (updates completed before an episode begins), or the B-O2 scope notes; any `DOMAIN-SEMANTICS.md` term or DS-I1…I7; the case/view/revision model; a DS-U item resolved or narrowed into a new requirement; or `CASE-INPUT.md` (exercise goal) or `BC-CHARTER.md` (delegation and scope). B and C are accepted **as a pair**, so a new version of either is re-issued together. *Basis:* `BEHAVIOR-CONTRACT.md` v2 and `DOMAIN-SEMANTICS.md` v2 §Conditions — the authority here is the B/C owner, and **D does not decide this and does not read it away**.
  *Citation guidance:* cite the v2 **Conditions**, not the v2 change-log summary, which is narrower than the Conditions list (noted as non-blocking in `M3-BC-V2-REVIEW.md`).
- **R-3 · Undefined semantics pressed into service.** DS-U1 (other status labels) → C owner, and must not be resolved as a side effect of implementation. By contrast, B/C v2 Conditions state that a **D/E choice made freely inside DS-U3** is *not* a re-open condition, and DS-U2 is likewise left unconstrained — so D-4's numbering/advance choice does not return here. The re-open trigger is instead **resolving or narrowing** a DS-U item into a new requirement.
- **R-4 · Coordination surface must change.** If coherence cannot be achieved without changing `StateView`/`CaseRecord` immutability, view publication semantics, or the revision's identity/ordering relations → back to D (this Plan). This is a surface change, not an interior one.
- **R-5 · Accepted coverage must be replaced.** If implementation cannot proceed without deleting or weakening one of the three existing checks → back to D; the method grants no deletion authority, and C-8 forbids it.
- **R-6 · Out-of-scope capabilities requested.** Persistence across restarts, concurrent viewers, case-set membership changes, multi-store comparison, deployment or migration → B-O2 / DS-U4: outside the exercise, **requires a new B version**; and any of these is in any case outside this Plan's and this fixture's action authorization. Do not implement.
- **R-7 · Safety/cost/professional concern appears.** Corrected per challenge PC-4(4): `StateStore` **is** a shared mutable reference across this fixture's reads and updates — "no shared state" was wrong. What the exercise genuinely lacks is *concurrency, cross-viewer sharing, persistence, and any external effect*; the in-process tests plus immutable view values are what cover the surface known today. That is a statement about present scope — **not** a risk assessment, and not a "no risk" claim. If concurrency, cross-viewer sharing, persistence or another external effect is proposed, D cannot rule on it: route via Driver to the relevant professional responsibility; human-reserved items only via Voice.
- **R-8 · Challenge and re-check findings.** `tpw-night-method`'s independent challenge v1 returned **FAIL** on the pre-reconciliation candidate; its findings are dispositioned in §0.3. Findings return to the D owner for decision or revision; the challenger is neither author nor acceptor of this Plan. This reconciliation has **not** itself been independently re-checked — Driver routes only the materially affected Plan claims for recheck, and a further finding re-opens the corresponding claim rather than the whole Plan.
- **R-9 · Method provenance recording (downgraded per challenge PC-3).** **Not a binding failure and not blocking.** The M4 acceptance of `0136593` is recorded in `ORACLE-ACCEPTANCE.md` §M4, and the normative body is byte-identical across the cited, embedded and current blobs (`e68e8d98…`). Action: Driver / the integration writer record the embedded copy's origin and the equivalence differential, and D cites one fixed version. No new acceptance question is raised for the method owner. Re-open only if the *substantive* body changes.

## 5. Validation basis

> **Eligibility (formerly "gated on R-2"; PC-1 resolved).** Under B/C v2 Conditions, in-scope implementation and test diffs — including new or amended tests — inherit the B/C acceptance. What follows is the coverage that must exist when E implements. **This is dependency eligibility, not authorization:** D acceptance is recorded at §8.1, and starting E is Driver's call under existing authorization, not this document's.

**Existing coverage:** the three checks in `tests/test_existing_behavior.py` cover the module-level operations and their accepted claim ("each current operation works"). They stay. **New coverage is required** because none of them asserts coherence across the pair (1.5). No existing check is replaced, so the method's replacement condition is not engaged.

**Falsifier for the core claim (design-time and implementation-time):** the X-2 straddle — produce a presented view's overview, complete a status update, then obtain the presented view's details. A design or implementation is invalid if it can present that pair as a revision-1 overview with revision-2 details. On the seed this falsifier fires today (§1.3), so it discriminates.

**Per-claim observables** (all reachable in-process with a bare `StateStore`; no mocks, no clock, no I/O):

| Claim | Observation that would falsify it |
| --- | --- |
| B-1 / DS-I1, DS-I2 | overview `revision` not the revision of its own details, or `open_count` ≠ number of `OPEN` among its own details, or a pair assembled from two resolutions |
| B-2 / DS-I5 | update completes, then episode opens, and the presented view's revision is older than that update |
| B-3 / DS-I3 | later episode reports a revision smaller than an earlier episode's |
| B-4 / DS-I4 | two episodes report an equal revision with different case data |
| B-5 | an update changed a status between episodes, and the later episode shows the old status or a non-greater revision |
| B-6 (a)–(d) | the four negative controls occur; (b) mixed pair and (d) pre-update status after a completed update are the two reachable on the seed |
| X-1, X-6 | no-change episode, and empty case set → count 0 with empty details |
| C-8 | any of the three existing checks fails or is weakened |

**Boundary for F — do not mislabel a legal variant as a B violation.** Pinning (C-3) is a **permitted** choice under P-1, not an accepted B requirement. An implementation that pins satisfies B; an implementation that instead switches to a newer revision mid-episode also satisfies B. F must verify B-1…B-6. Whether the implementation honors this Plan's pinned policy is a Plan-conformance question, not a B violation, and F owns neither acceptance of this Plan nor the policy choice. F also must not treat "no visible refresh" as a defect. `A8`-style verdicts here remain three-state; an environment block is `UNVERIFIED`, not a product defect.

**Expected scope of change (implementation assumption, not a file list):** the defect site is the second independent `current_view()` resolution in `src/case_reader.py` relative to `src/page_summary.py`, and the missing pair carrier across `src/turn.py` / `src/service.py`. `D-PLAN-INPUT.md` warns that the current structure is evidence, not a responsibility map; E owns placement (D-1).

## 6. Affected dependencies and regression surface

> **Eligibility (formerly "gated on R-2"; PC-1 resolved).** The change surface below describes where the coherence binding must land, and the in-scope diffs it implies inherit the B/C v2 acceptance. This is **not** authorization to modify these files: D acceptance is recorded at §8.1, and E start is Driver's call under existing authorization.

- `src/state_store.py` — `StateView`/`CaseRecord` immutability and rebind-not-mutate publication are **design dependencies** (C-4). `update_status` semantics for absent ids and for `"OPEN"`-only counting feed C-6/C-7.
- `src/page_summary.py` — already coherence-correct within the overview; may need to expose its view or be composed differently (E's choice).
- `src/case_reader.py` — the second resolution; the change site.
- `src/turn.py` — `Turn.page_summary` is a compatibility surface; the pair carrier currently does not exist.
- `src/service.py` — the entry points; compatibility surface (C-8).
- `tests/test_existing_behavior.py` — accepted coverage; retained verbatim (C-8, R-5).
- **Consumers outside the fixture:** none. No persistence, no schema, no migration, no external effect, so no compatibility or recovery obligation arises beyond C-8. No dependency on `UCBIP` or any product is created.

## 7. Assumptions

- A-1 · Single-threaded, in-process, one store lineage; no read/update interleaving *within* a single call (grounded in C's "in this single-threaded fixture, when the call returns").
- A-2 · `StateView`/`CaseRecord` value-immutability and rebind publication survive implementation (C-4). If not, R-4 governs.
- A-3 · E works within the Charter's object scope and does not modify B/C objects, `CASE-INPUT.md`, or the Charters.
- A-4 · B/C v2 acceptance is **author acceptance by `tpw-night-m3-bc`, not independent evaluation** — stated in both objects. The v2 clarification (PC-1/PC-2) and preservation of the v1 claims were separately reviewed **PASS** by `tpw-night-method` (`M3-BC-V2-REVIEW.md`), and I reproduced the same preservation directly: the v1 body (section heading → EOF) is byte-identical to the v2 body before `## Change log` — `eab01bf9…` for B, `f303d5c9…` for C, matching the review's digests. That review covers the B/C inputs only; it does not accept this Plan and does not authorize E. This Plan relies on the accepted *meanings* and does not extend them to any product.
- A-5 · "Presented view" is realized by composition of the fixture's entry points; the fixture has no viewer/session object, so the episode boundary is a technical proxy (D-5).
- A-6 · The runtime reported in `BASELINE.md` and observed here reproduces the recorded 3/3 pass; the seed's `revision == 2` assertion is live coverage.

## 8. Unresolved points, boundaries and independence

**Resolved by this Plan (within delegation):** B-O1 → pinned policy (C-3/D-1). Version binding → the active bindings are the fixed **B/C v2** pair, verified in §0.1. The startup prompt's **B/C copies are the v1 objects** (identical to commit `893eaf8`); only their behavior/domain body is byte-consistent with v2, since v2 changed only the Conditions, recipe and version metadata (§0.1, A-4). This Plan relies on the **v2 Conditions**, not on the embedded copies being v2. The embedded **Backbone** copy is the original fixed export and stays byte-identical to `RESPONSIBILITY-BACKBONE.md`. All challenge findings are dispositioned in §0.3, with PC-1 closed upstream and PC-2 closed here.

**Nothing is left blocking in this Plan.** The former PC-1 blocker is resolved by fixed B/C v2 and its independent PASS, and the PC-2 correction is applied. D acceptance for the delegated technical-planning scope is recorded below; E start remains Driver's arrangement under existing authorization and the §5/§6 eligibility, and neither this Plan nor its acceptance authorizes implementation.

### 8.1 D acceptance (recorded 2026-10-01)

- **Accepted object:** the corrected Plan in this file, within the technical-planning responsibility delegated by `D-CHARTER.md` (M3 plan baseline `496b0676e302e2d0eafba129ff61de4c203d258a`).
- **Reviewed predecessor and independent basis:** `bb8afeb1d7519cac8926e1553f30e83590b8fb0504f120120c09cd916e0823d3`, independently rechecked for the affected claims with verdict **PASS** — `M3-SNAPSHOT-PLAN-V2-RECHECK.md`, `sha256 e93ac8869c2f0c94eb6b9ea8ec91a265920406656d31eacf12cee5b9a25ce278`. Its single finding (the §8 embedded-copy wording) was classified **non-blocking** and is the correction applied in this revision.
- **Accepting party:** `tpw-night-m3-design`, as the D instance holding this delegation. This records the **existing** D responsibility for the technical Plan; it adds **no new gate**, approval step or authority beyond it.
- **Scope — what is accepted:** this fixture's technical Plan only, as written in this file.
- **Explicitly not accepted or granted here:** B/C themselves (the v2 pair was accepted by `tpw-night-m3-bc` and separately reviewed PASS — a different act, by different parties); any implementation or its correctness; M3 closure; and any deployment, migration, release or UCBIP change.
- **Not claimed:** that *this corrected hash* has itself been independently rechecked. The recheck covered `bb8afeb1…`; this revision differs from it only by the non-blocking §8 correction and this acceptance record — the narrow diff for Driver to verify.

**Left open, deliberately:**
- U-1 · The carrier shape and episode-boundary representation (D-1, D-2, D-5) — **bounded delegated coordination decisions**, not invisible internals: E must record the concrete choice, and any answer satisfying C-1…C-10 within the recorded boundary is acceptable.
- U-2 · `DS-U2` revision behavior on a no-op update (D-4).
- U-3 · `DS-U1` statuses other than `OPEN`/`CLOSED` remain undefined and must not be resolved here (C-6, R-3).
- U-4 · Whether the Owner or B owner would prefer a visible refresh instead of pinning. Pinning is inside D's delegation by B-O1, so no approval is sought; a later switch is a Plan-level change (R-4) and, if it must become an accepted observable, a B change (R-1).
- U-5 · Method provenance recording (§0.2, R-9): the blob applied differs from the blob cited, while the normative body is byte-identical and M4 acceptance of `0136593` is already recorded. This is a recording action for Driver / the integration writer, not a decision, and it stays **bounded** — it is not a method gate, not an acceptance gate, and not a blocker.

**Not granted here:** implementation beyond the cited Charter delegation, deployment, migration, release, product generalization, M3 closure, or acceptance of B/C. Design acceptance does not produce execution permission; `PASS` on future verification does not produce a release authorization.

**Independence.** This Plan is authored by the D instance `tpw-night-m3-design`. It was independently challenged once: `tpw-night-method` — neither author nor acceptor — returned **FAIL** (`bf3e15de…`) against candidate `e3b2d3c` / Plan `bcc10e48…`; that was revised (`f081c1c3…`) and then reconciled to `bb8afeb1…`, on which an independent **affected-claim recheck returned PASS** (`e93ac886…`) with one non-blocking wording finding. Author and acceptor here are the same responsible party, as the delegation provides: the recheck is independent *challenge*, whereas D acceptance (§8.1) is D's own act — two different facts, not a self-review. **This corrected revision has not itself been rechecked**; it differs from the rechecked hash only by the correction that recheck called non-blocking, plus the acceptance record. D owns acceptance of this fixture's technical Plan within the cited delegation; Driver checks input and version binding, not substantive design; F evaluates the implementation later. The B/C inputs were accepted by a different instance (`tpw-night-m3-bc`, session `01a0f39e-8658-7478-ad5e-b1870bb69bd6`) and independently reviewed PASS at v2 by `tpw-night-method`. D acceptance of this Plan is not acceptance of B/C, of any implementation, or of M3 closure.

**Unverified by me:** that the mechanism proposed to E will in fact satisfy B-1…B-6 — that is established only by the implementation and its evidence, or by a further counterexample. This Plan makes the target falsifiable and localizes the defect; it does not itself constitute verification. Also not established here: that any implementation actually placed inside the B/C v2 inherited envelope keeps every acceptance item true — that is what the §5 observables are for, and D's acceptance of this Plan does not substitute for it.

## M3 case input
Source: docs/overnight/2026-10-01/fixtures/m3-snapshot/CASE-INPUT.md
SHA-256: 50063486b149fc599464cb5cb25872cc9b4c4b971d1fcbc2eab0efdabeffd772

# M3 case 2 · B/C authoring input

This is an offline exercise about a viewer whose overview and case details are read at different moments. The underlying case store can change between those reads.

Define the externally observable behavior and the domain meaning needed for a coherent view during one user interaction, including what may be observed by a later interaction. Keep the contract small enough to test and state the important example/exception.

The fixture contains `state_store`, `page_summary`, `turn` and `case_reader` modules. Read them as evidence of the current system. This task does not ask you to place responsibilities in those modules, design an interface, name a recall route, or choose an implementation. Those are later judgments. Keep the result scoped to this synthetic fixture; do not imply business rules for UCBIP or another product.

No external service, persistent migration, production data, or network access is part of the exercise.

## Pre-contract baseline
Source: docs/overnight/2026-10-01/fixtures/m3-snapshot/BASELINE.md
SHA-256: 00494d48e01f2af932e401d7e8edccbfb10d0af95e541c416b054090f0dc19da

# M3 case 2 · pre-contract seed observation

This observation is from the fixture seed, before any cross-module B/C contract, D Plan, or implementation candidate was added.

- Runtime: Python 3.14.4.
- Command, run from this fixture directory: `python3 -m unittest discover -s tests -v`.
- Exit: `0`; 3 existing module-level checks passed.
- Current code exposes `StateStore.current_view()`, `page_summary.build_page_summary()`, `turn.begin_turn()`, and `case_reader.read_cases()` through separate modules. The tests cover each current operation but do not assert a coherent snapshot spanning a turn.
- No D Plan or implementation candidate exists at this baseline.

The new cross-module behavior is not part of this seed; its accepted B/C inputs will be recorded separately before D planning begins.

## E factual handoff
Source: 17602f2b12822aba88785e27a733f75a3238214d:docs/overnight/2026-10-01/fixtures/m3-snapshot/M3-CASE2-E-REPORT.md
SHA-256: 557c1ed51e5c9b8c951b1e68a01b318160126ac63924c960b6e1b0c9dd298aed

# M3 case 2 · E implementation handoff

- **Instance:** `tpw-night-m3-local-impl` (Pi session `01a0f3ac-a22b-75ef-9946-984ec8f6603b`) — the existing E author session previously used for case 1; reused, not a new independent identity.
- **Binding inputs (hashes as received and re-verified):** startup packet `M3-CASE2-E-STARTUP-PROMPT.md` `e0cf4f0e4beac2e777c460e74f3eee5142e1eb2b5ab30b0c1057ac49696ad346`; Charter `M3-CASE2-E-CHARTER.md` `75b5f5023c5682bd932069a6a783bc808e5b1c76b447a659f155abe0fee39661`; B/C v2 pair `6cf43d3fb647cf2c250f275179762917c0763a669e84f1718d85968a8e66c738` / `d35766b45085db2b7e5b3315cca5ce4183f722186a850ef317fd571ebba6d45b`; accepted D Plan `a306205729a002fdf1bc4eac6a623849cb2198985f8a6fbae4ec4c00ec47e5b9`.
- **Environment:** worktree `…/.worktrees/night-2026-10-01`, branch `night/2026-10-01-workflow`, base commit `2ad7227`; Python 3.14.4; offline, standard library only.
- **Scope of this report:** implementation facts and self-check observations only. It is **not** a verdict on the behavior; no PASS/FAIL is claimed, and no F criterion, rubric or report was read, searched for or inferred. E self-checks are evidence input for F, not an independent conclusion. No release, deployment, migration or closure is claimed.

## 1. Pre-edit baseline verification (seven per-file hashes and the aggregate)

Verified against the worktree files before any edit, with the B/C v2 recipe (files under `src/**` and `tests/**` ordered by relative path ascending; one line per file as `<sha256><two spaces><path>`; joined with `\n` + final `\n`; sha256 of the UTF-8 text):

| File | Recorded (B/C v2) | Recomputed | Result |
| --- | --- | --- | --- |
| `src/__init__.py` | `a5f855a8…33cf4` | `a5f855a87138b8c9a515d76a2b7858da6bba6fb60eff9446197fafc774733cf4` | match |
| `src/case_reader.py` | `89f05180…e350bc` | `89f05180854b8cb38b58299f516e7298cd2d211b88bed38f35087e6b1fe350bc` | match |
| `src/page_summary.py` | `59bffca2…ac2fc4` | `59bffca2096cdb3818a202e552fa5214dd3f263466fd4799b3d7ba4e4fac2fc4` | match |
| `src/service.py` | `ea3fff5f…d66a0d` | `ea3fff5faf10d3025b19a07cc709985467b9dc67e607282ff1c87c73ddd66a0d` | match |
| `src/state_store.py` | `90a1cb56…029196` | `90a1cb56549f5afdbae24d2b485f8a956e66081939159a435aa83e2f43029196` | match |
| `src/turn.py` | `5de7b6c6…504ac0` | `5de7b6c681f8379e567d9be455a3176a48c429ca460b6810092ff7ae46504ac0` | match |
| `tests/test_existing_behavior.py` | `9ac7ea87…c7876f` | `9ac7ea872b8c50f921128e7a8d734539b273551e7d6e9363e3d5116103c7876f` | match |
| **aggregate** | `dbd6a306…e51b474` | `dbd6a306815bdc4cf3a33be14b38d4dd62b49d1535d7db41b9064eb07e51b474` | match |

The digest-line-sorted alternative was also recomputed as `9074f27da8e0d76113bda8f774297c7c8fbceaedaf67d6ea75eec87d2421e88c`, matching the non-matching value recorded in B/C v2 — so the path-order recipe is the one in force and it reproduces the recorded aggregate.

After implementation, the five files the change did not touch (`src/__init__.py`, `src/case_reader.py`, `src/service.py`, `src/state_store.py`, `tests/test_existing_behavior.py`) were re-hashed and still match their baseline digests above.

## 2. Chosen design (D-1, D-2, D-3, D-5; C-1…C-3, C-9)

- **Carrier (D-1, D-3):** the existing `turn.Turn` is reused as the pair carrier. No new module, no new public function, no second carrier type.
- **Entry point (D-5):** `service.start(store)` (which calls `turn.begin_turn(store)`). This is the call a consumer or verifier makes to open the episode; it returns the pinned `Turn`.
- **Episode boundary (D-5):** one call, atomic with respect to updates. The episode is the `Turn` returned by `start`/`begin_turn`; it resolves `StateStore.current_view()` exactly once, at open. The two observations of that episode are `turn.page_summary` (overview: `revision`, `open_count`) and `turn.cases` (details: the case pairs), both serving the presented view. No mid-episode refresh, no retry/reconcile path.
- **Pin representation (D-2):** materialized — `Turn.view: StateView` holds the single resolution; `page_summary` and `cases` are derived properties over that one view. The overview count is computed by the same `page_summary.summarize_view(view)` used by the retained `build_page_summary(store)`, so the `OPEN`-only count rule has one implementation.
- **Observation values (C-5):** `page_summary` returns a fresh `dict` per access and `cases` returns the pinned view's immutable tuple, so nothing a caller receives can change under a later update.
- **`DS-U2` / D-4:** kept the seed behavior — an update that leaves every status unchanged (unknown case id) still advances the revision. Legal under DS-U2 and X-5; DS-I4 still holds because no case data changes.
- **Compatibility (C-8):** `service.start(store)` still returns a `Turn` whose `page_summary` carries exactly `revision` and `open_count`; `service.cases(store)` is unchanged; the three existing checks are byte-identical and were not deleted or weakened. `StateStore.update_status` still publishes a new `StateView` by rebinding (C-4), and `CaseRecord`/`StateView` remain frozen.

Boundary note for F and the next consumer: `service.cases(store)` and `page_summary.build_page_summary(store)` remain independent single-resolution callables. Two separate calls still resolve twice and can observe different revisions; that two-call pattern is **not** the presented view under this Plan's model — the modeled presented view is the pinned pair carried by the `Turn` opened by `service.start`. No hidden episode state was added to `StateStore` to bridge the two call forms.

## 3. Changed files and SHA-256

| Path | Change | SHA-256 (current bytes) |
| --- | --- | --- |
| `src/page_summary.py` | modified — added `summarize_view(view)`; `build_page_summary(store)` now delegates | `a3b81175423bd241a2c63c9d0b530fda2aad9698a3e96ba6bd9495764d7570f1` |
| `src/turn.py` | modified — `Turn` pins the resolved `StateView`; `page_summary`/`cases` are derived properties; `begin_turn` resolves once | `2be753eb357ad4c0eb150861c61a2b220c75af5423fc10a2ad9d304eede52354` |
| `tests/test_episode_coherence.py` | added — coherence coverage (see §5) | `4f0b000892b2e5f3808166ee305bc8ba492661262d1be27757c661dac317076e` |

No other file in the fixture was written. Nothing was committed; the candidate is the worktree state above (base commit `2ad7227`), so F/Driver can fix the object by these hashes.

## 4. Commands and observations

All commands run from `docs/overnight/2026-10-01/fixtures/m3-snapshot`.

**4.1 Seed baseline before any edit** — `python3 -m unittest discover -s tests -v`
Exit `0`; `Ran 3 tests … OK` (matches `BASELINE.md`).

**4.2 Pre-change falsifier probe (negative control on the unmodified seed bytes, in-process, `PYTHONDONTWRITEBYTECODE=1`)** — opens a "view", completes an update, then obtains the details through the then-available second resolution:

```
seed overview  : {'revision': 1, 'open_count': 2}
seed details   : [('C-1', 'CLOSED'), ('C-2', 'OPEN')]
count-faithful : False
same revision  : False
X-2 straddle (B-6(b)) present in seed split pattern: True
Exit 0
```

**4.3 New tests against the unmodified seed (red evidence)** — `python3 -m unittest discover -s tests -p 'test_episode_coherence.py' -v`
Exit `1`; `Ran 9 tests … FAILED (failures=1, errors=6)`. The carrier was absent (`AttributeError: 'Turn' object has no attribute 'cases'`) and the pinned-value check failed on the seed because a mutated returned summary was the stored object (`{'open_count': 99}`) — the live-alias defect behind C-5.

**4.4 Post-change full suite (Charter seed command)** — `python3 -m unittest discover -s tests -v`
Exit `0`; `Ran 12 tests … OK` (3 retained existing checks + 9 new).

**4.5 Post-change carrier probe** — same scenario as 4.2 through the pinned carrier:

```
carrier overview: {'revision': 1, 'open_count': 2}
carrier details : [('C-1', 'OPEN'), ('C-2', 'OPEN')]
count-faithful  : True
still revision 1: True
store revision  : 2
Exit 0
```

## 5. Coverage preserved and added

Preserved: the three checks in `tests/test_existing_behavior.py` are byte-identical (hash §1) and pass; nothing was deleted or weakened.

Added (`tests/test_episode_coherence.py`, 9 checks):

| Check | Claims exercised |
| --- | --- |
| `test_mid_episode_update_cannot_straddle_the_presented_pair` | X-2, B-1, B-6(a)(b), DS-I1, DS-I2, C-1…C-3 |
| `test_episode_observations_are_pinned_values` | C-3, C-5 (caller mutation cannot alter a pinned observation) |
| `test_update_completed_before_episode_is_visible` | X-3, B-2, B-5, DS-I5 |
| `test_later_episode_revision_never_decreases` | B-3, B-6(c), DS-I3; start-1/step-1 compatibility (C-8) |
| `test_equal_revision_presents_equal_case_data` | X-1, B-4, DS-I4 |
| `test_each_update_between_episodes_is_visible` | X-4, B-2, B-5 |
| `test_empty_case_set_presents_zero_open_and_no_details` | X-6, B-1 |
| `test_update_with_unknown_case_id_leaves_all_statuses_unchanged` | DS-I7 with DS-U2 (documents the kept D-4 choice) |
| `test_existing_entry_points_stay_callable_with_a_bare_store` | C-8 (keys and call shapes) |

## 6. Deviations, boundary facts and unresolved items

- **Deviations from the Plan: none identified.** No B/C meaning, D commitment, observable surface, scope or acceptance item was changed; no R-1…R-9 recall condition was triggered. `CASE-INPUT.md`, `BC-CHARTER.md`, the B/C v2 pair, the Plan, the Charters, the packet, `professional-workflow/` and all evaluation artifacts were not edited.
- **Placement fact (D-1 leaves placement to E):** the change lands in `src/page_summary.py` and `src/turn.py`; `src/case_reader.py` and `src/service.py` needed no edit — `service.start` already delegates to `begin_turn`, which now pins.
- **Boundary fact recorded for F:** the legacy two-call pattern (`start(...)` then `cases(store)`) still resolves twice by design; the modeled episode/presented view is the `Turn` (see §2). This is the recorded D-5 boundary, not a residual defect claim.
- **Unresolved / left to F and the next consumer:** whether the pinned-pair carrier and the recorded boundary are the ones to rely on; observable independence and coverage adequacy of these self-checks; behaviour under concurrency, persistence or cross-viewer sharing is outside the exercise (B-O2, DS-U4) and was not attempted.
- **Not claimed:** behavioral correctness, an F verdict, M3 closure, or any authorization beyond this fixture.

## 7. Independence

This implementation was authored by the case-1 E session above, which is the same identity for case 2. The case-2 F evaluator (`tpw-night-method`) is a different session and did not author these changes; E did not read or infer its criteria, and this report does not speak for it. E self-check observations above are inputs to that evaluation, not an independent result.

## Treatment src/page_summary.py
Source: 17602f2b12822aba88785e27a733f75a3238214d:docs/overnight/2026-10-01/fixtures/m3-snapshot/src/page_summary.py
SHA-256: a3b81175423bd241a2c63c9d0b530fda2aad9698a3e96ba6bd9495764d7570f1

from .state_store import StateStore, StateView


def summarize_view(view: StateView) -> dict[str, int]:
    return {
        "revision": view.revision,
        "open_count": sum(case.status == "OPEN" for case in view.cases),
    }


def build_page_summary(store: StateStore) -> dict[str, int]:
    return summarize_view(store.current_view())

## Treatment src/turn.py
Source: 17602f2b12822aba88785e27a733f75a3238214d:docs/overnight/2026-10-01/fixtures/m3-snapshot/src/turn.py
SHA-256: 2be753eb357ad4c0eb150861c61a2b220c75af5423fc10a2ad9d304eede52354

from dataclasses import dataclass

from .page_summary import summarize_view
from .state_store import CaseRecord, StateStore, StateView


@dataclass(frozen=True)
class Turn:
    """A read episode pinned to the StateView resolved when it opened."""

    view: StateView

    @property
    def page_summary(self) -> dict[str, int]:
        return summarize_view(self.view)

    @property
    def cases(self) -> tuple[CaseRecord, ...]:
        return self.view.cases


def begin_turn(store: StateStore) -> Turn:
    return Turn(view=store.current_view())

## Treatment tests/test_episode_coherence.py
Source: 17602f2b12822aba88785e27a733f75a3238214d:docs/overnight/2026-10-01/fixtures/m3-snapshot/tests/test_episode_coherence.py
SHA-256: 4f0b000892b2e5f3808166ee305bc8ba492661262d1be27757c661dac317076e

import unittest

from src.service import cases, start
from src.state_store import CaseRecord, StateStore


def store_with(*pairs: tuple[str, str]) -> StateStore:
    return StateStore(tuple(CaseRecord(case_id, status) for case_id, status in pairs))


def presented_pairs(turn) -> list[tuple[str, str]]:
    return [(case.case_id, case.status) for case in turn.cases]


def open_count_of(pairs: list[tuple[str, str]]) -> int:
    return sum(status == "OPEN" for _, status in pairs)


class EpisodeCoherenceTests(unittest.TestCase):
    """Coverage for B-1..B-6 and DS-I1..I7 through the pinned episode carrier."""

    def test_mid_episode_update_cannot_straddle_the_presented_pair(self):
        # X-2 / B-1 / B-6(b): one resolution per presented view.
        store = store_with(("C-1", "OPEN"), ("C-2", "OPEN"))
        turn = start(store)
        store.update_status("C-1", "CLOSED")
        self.assertEqual(turn.page_summary["revision"], 1)
        self.assertEqual(turn.page_summary["open_count"], 2)
        self.assertEqual(presented_pairs(turn), [("C-1", "OPEN"), ("C-2", "OPEN")])
        # B-6(a) / DS-I2: the count is faithful to the details of the same view.
        self.assertEqual(turn.page_summary["open_count"], open_count_of(presented_pairs(turn)))

    def test_episode_observations_are_pinned_values(self):
        # C-3 / C-5: observations are values, and the pin cannot change under later updates.
        store = store_with(("C-1", "OPEN"))
        turn = start(store)
        returned = turn.page_summary
        returned["open_count"] = 99
        del returned["revision"]
        store.update_status("C-1", "CLOSED")
        self.assertEqual(turn.page_summary, {"revision": 1, "open_count": 1})
        self.assertEqual(presented_pairs(turn), [("C-1", "OPEN")])
        self.assertIsInstance(turn.cases, tuple)

    def test_update_completed_before_episode_is_visible(self):
        # X-3 / B-2 / B-5 / DS-I5.
        store = store_with(("C-1", "OPEN"), ("C-2", "OPEN"))
        store.update_status("C-1", "CLOSED")
        turn = start(store)
        self.assertEqual(turn.page_summary["revision"], 2)
        self.assertEqual(turn.page_summary["open_count"], 1)
        self.assertEqual(presented_pairs(turn), [("C-1", "CLOSED"), ("C-2", "OPEN")])

    def test_later_episode_revision_never_decreases(self):
        # B-3 / B-6(c) / DS-I3; also fixes the fixture's start-1 / step-1 behaviour (C-8).
        store = store_with(("C-1", "OPEN"), ("C-2", "OPEN"))
        revisions = []
        for index in range(3):
            revisions.append(start(store).page_summary["revision"])
            store.update_status("C-1", "CLOSED" if index % 2 == 0 else "OPEN")
        self.assertEqual(revisions, sorted(revisions))
        self.assertEqual(revisions, [1, 2, 3])

    def test_equal_revision_presents_equal_case_data(self):
        # X-1 / B-4 / DS-I4: no update between episodes.
        store = store_with(("C-1", "OPEN"), ("C-2", "OPEN"))
        first = start(store)
        second = start(store)
        self.assertEqual(first.page_summary["revision"], second.page_summary["revision"])
        self.assertEqual(presented_pairs(first), presented_pairs(second))

    def test_each_update_between_episodes_is_visible(self):
        # X-4 / B-2 / B-5: two completed updates are reflected by the next episode.
        store = store_with(("C-1", "OPEN"), ("C-2", "OPEN"))
        first = start(store)
        store.update_status("C-1", "CLOSED")
        store.update_status("C-2", "CLOSED")
        second = start(store)
        self.assertGreater(second.page_summary["revision"], first.page_summary["revision"])
        self.assertEqual(second.page_summary["open_count"], 0)
        self.assertEqual(presented_pairs(second), [("C-1", "CLOSED"), ("C-2", "CLOSED")])

    def test_empty_case_set_presents_zero_open_and_no_details(self):
        # X-6 / B-1.
        turn = start(store_with())
        self.assertEqual(turn.page_summary, {"revision": 1, "open_count": 0})
        self.assertEqual(presented_pairs(turn), [])

    def test_update_with_unknown_case_id_leaves_all_statuses_unchanged(self):
        # DS-I7 with DS-U2: the statuses are unchanged; the fixture keeps advancing the revision (D-4).
        store = store_with(("C-1", "OPEN"), ("C-2", "OPEN"))
        before = start(store)
        store.update_status("C-9", "CLOSED")
        after = start(store)
        self.assertEqual(presented_pairs(after), presented_pairs(before))
        self.assertEqual(after.page_summary["revision"], before.page_summary["revision"] + 1)

    def test_existing_entry_points_stay_callable_with_a_bare_store(self):
        # C-8: the pre-existing call forms keep their shape and results.
        store = store_with(("C-1", "OPEN"))
        turn = start(store)
        self.assertEqual(set(turn.page_summary), {"revision", "open_count"})
        self.assertIsInstance(cases(store), tuple)
        self.assertTrue(all(isinstance(case, CaseRecord) for case in cases(store)))


if __name__ == "__main__":
    unittest.main()

## Evaluation task

Independently evaluate the exact treatment commit against the B/C v2 contract and the D-accepted Plan, using the accepted M4 method body and the held private case-2 F criteria. Treat E's report as a factual self-report to verify, not as a verdict.

Use a valid baseline/treatment comparison where the held criteria require it. The baseline object is the exact pre-E commit above; the treatment is the exact E commit above. Preserve exact commands, outputs, and environment facts in the report. Evaluate only the public B/C claims and Plan commitments plus the held F criteria; distinguish the Plan's pinned-pair choice from B's permitted variants and keep out-of-scope behavior UNVERIFIED where appropriate.

If the held criteria are not available in your session context, do not infer or request them from E; return UNVERIFIED and state the missing-input limit without revealing private content.

Return exactly one three-state verdict: PASS, FAIL, or UNVERIFIED. Do not disclose the private rubric or its precise expected outcomes. Identify the exact commit/tree and file hashes, evidence, claim coverage, negative controls if used, and limits.

Write only docs/overnight/2026-10-01/fixtures/m3-snapshot/M3-CASE2-F-EVALUATION.md. Do not edit, stage, or commit source/tests, Charters, Plans, package files, or verification copies. This evaluation does not accept M3 as a whole.
