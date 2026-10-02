# REVIEW-A1-ADDY-AB

tpw-absorb-gate，2026-10-02；源机制裁定，非正文/集成接受。7/7 已裁：限缩吸收 G1/G2/G5/G7；合并 G3/G4/G6。七组均含可蒸馏部分，组内拒绝移植的规则见下。

## 固定对象及回源

包 `03dfb8ab865dab2ab62a23e32bdaee6f48c53877:docs/absorption/2026-10-02/packages/A1-ADDY-AB.md`，blob `9eaa40eba7d3c2e28529de8d9c64aaedc0a61bea`；产品 `800414dd9eb517f7132223866fe484d28a8bbf0b:professional-workflow`，tree `7c814e54c5e775045bc1c5155e3c181ceb1345fb`（本次核当前子树仍相同）。源 `../legacy-pre-night-2026-10-01/upstreams/addyosmani-agent-skills` HEAD `2686b620fc1fed2e8f60c704839c766b8594c6b6`，status无差分。

直接回读源：`skills/code-review-and-quality/SKILL.md`、`agents/code-reviewer.md`、`references/definition-of-done.md`、`docs/adoption-guide.md`、`CONTRIBUTING.md`全文；`references/orchestration-patterns.md` 的 Endorsed patterns、Compatibility及Anti-patterns/Decision flow/准入相关段；`AGENTS.md` Intent/Execution/Anti-Rationalization；`skills/using-agent-skills/SKILL.md` Skill Discovery/Core Operating Behaviors；`docs/getting-started.md` Working across sessions；`skills/context-engineering/SKILL.md` Restartable Session Boundaries及Context Budget Management；`docs/skill-anatomy.md` Shared References、Context Efficiency、Procedure not Workaround等；`scripts/lib/skill-lint.js`限制定义、`validate-artifact-paths.js`范围及检查、`validate-commands.js`输入/名称映射/解析、`validate-reference-links.js`范围及链接解析；`.claude/commands/ship.md`。脚本未全量执行或认证，截断段未记全文。产品相关Profile、Charter、三方法和两guide已在本轮直接回核，沿用其责任/覆盖，不只读A转述。

我未代写包或产品，本记录独立给出处理要求；B的实际固定差分另审。下文源路径相对上述pin，产品路径相对professional-workflow。

## G1 · composition

**覆盖：部分且责任已充分。** Driver/Profile选择/Backbone已有组合失效、独立性、按需与程序/实质区别；缺成本与转述失真操作例子。

**裁定：限缩吸收。** 取 orchestration-patterns §1/3/5 的直接完成基线、真实独立子工作、写面/次序/合成成本核对，保留重复转述与无判断价值中间层的失败机制。新增组合先说明真实需要、既有做法缺口、示例产物与容易误用处，不把次数当资格。

**边界：**拒绝源的“用户唯一编排者、persona绝不调用persona、深度≤1、所有合成归主实例、≤2文件且<50行才可跳fanout、不同kind发现才可并行”。这些是其宿主/运行政策，不能重写本仓已接受Driver和有效委托；两个真实独立reviewer可审同一claim。共享状态可用任务已有互斥安排，非任何共享都禁止并行。无两次真实使用硬准入或常驻方法catalog框架；只是设计判断参考。约2×tokens等是源解释，非本轮测量。

**可蒸馏落点：**新 `methods/bounded-composition.md` §Use、Direct baseline、Dependencies/write ownership、Context handoff、Costs/anti-patterns；Driver方法入口。与Cursor ABC2共享写面机制合并。**补读：无承重缺口；**无需平台Teams操作验证。不自动获得当前会话派工权限。

## G2 · intent routing

**覆盖：选择入口与歧义路由充分覆盖，用户语句/排除条件例子不足。** `methods/README.md`任务需要表，Profile和Charter绑定，Driver对歧义召回专业责任已成立。

**裁定：限缩吸收。** 从 `using-agent-skills` §Skill Discovery取以任务问题/常见用户表达索引能力、正/负适用例子、只加载相关正文、避免双路由与多处重复维护映射。

**边界：**不采“even 1%必用”、按固定生命周期加载、不得部分适用、三件套最低集或反理性化全套。方法自己不产生applicability obligation；适用性存疑回核任务事实或召回相应判断，不能靠偏向加载制造mandatory gate。例外与方法子段按真实需求选择，简短低风险任务可直接沿已有契约；合理调查不算借口。无新增router/registry。

**可蒸馏落点：**现有 `methods/README.md` §Selected methods/On-demand guides 按任务needs更新必要正负例；文本规则并入 A3 `guide-agent-text.md` §Pointers。与G1不同触发，不必强合成一种driver流程。**补读：无。**描述匹配有效性留Addy EF评估裁定，不声称1%阈值有用。

## G3 · change review

**覆盖：部分。** F有独立性/版本/接受依据，缺五轴具体探针、发现的作者动作与依赖升级操作。已与Cursor MG-6候选同主落点。

**裁定：合并。** `code-review-and-quality` §Five-Axis、Structural Remedies、Review Process、Change Descriptions、Handling Disagreements、Honesty、Dependency Discipline 与 reviewer正文提供：核任务/spec→核测试是否能揭错→按相关关切追可达路径→核作者验证故事；每finding标实际影响、需要动作、依据、建议和未定；讨论事实/接受约束而非个人偏好；变更说明what/why/不足/证据；升级读真实changelog/迁移、相关小组隔离、lockfile传递变化与回归覆盖，安装成功不足证实。

**边界：**无每变更强制审/每轴全跑、100/300/1000行门槛、三次使用才抽象、一个工作日SLA、必须人作最终裁定、作者有上下文即可推翻安全/行为规则、总是先测试、无前缀自动required或无条件“以后从不可以”。blocking由有效规则/authority判断，不由标签创造。保留Critical/Required/Optional/Nit/FYI的行动区分即可，词表按本库一致定义，不为上游漂移grader复制标签；review建议与F三态/接受/发布许可分开。合理已授权死代码处理不重复问；不确定ownership/行为才召回。依赖升级可成有依据的关联组；lockfile是否记录沿仓库惯例，勿泛化npm规则。安全/性能细化另见CD，不假称此处已完整专业审核。

**跨源张力裁定：**共同 `methods/change-review.md` 应保留Spec与Standards/专业关切各自来源、观察、未解决项；可去重同一缺陷并作有委托的处置摘要，不能把一轴通过抵消另一轴失配。既有Matt源“不跨轴排序”是呈现/独立阅读纪律，可在该需要时应用，不禁止实际有权者依据严重性安排工作；Cursor合成不得创造源authority之外的决定权。后续DEF-2对此定向补裁，而非另造第四种形态。

**可蒸馏落点：**共同 `change-review.md` §Preparation、Lenses、Finding/disposition、Reviewability；依赖升级独立按需 `guide-dependency-change.md` §Choose/upgrade/coverage（与CD安全供链内容互指）。F方法入口。**补读：**此组可直接蒸馏；安全/perf细节由已到CD/EF回源后裁，不退AB。

## G4 · handoff / restart

**覆盖：部分。** Backbone/Charter已有可恢复结论、版本、接受和召回；缺五事实与重放观察具体操作。context-engineering缺读已由我直接补到 §Restartable Session Boundaries L123–137。

**裁定：合并。** `getting-started` §Working across sessions 与 context条款支持：既有产物承载现行决定/范围/未决/下一步/验证对象命令结果；切换后先读真实对象和Git状态；进程退出不证明完成，重启不绕授权；基线或覆盖条件改变只重核受影响证据，记录未提交状态，不推断不可见批准。

**边界与取向：**持久产物是工作真源，handoff只携指针和尚无owner文档的操作状态；可移植brief有价值，但不另写第二份契约。拒绝A的“交接总结必为第二真源”绝对说法：brief明确引用owner/version、区分候选与接受且不替代源，可安全传送。无每phase新session、每taskcommit、各切换全suite、默认临时doc可删、digest替代承重完整语义。授权可继承但需可恢复依据，不因摘要就自动失效。process supervisor/model/runtime不纳本方法。

**可蒸馏落点：**共同 `methods/handoff-and-resume.md` §Existing artifact first、Minimal transfer、Restart state、Evidence reuse；与Cursor MG-7/8、Matt DEF-9合并。**補读：无承重缺口。**验证需能恢复working state及未核claims，不只检字段非空。

## G5 · standing quality / task acceptance

**覆盖：区分原则已充分，操作参考可改善。** Backbone/Charter已分accepted policies、B/C承诺、F证据与closure；并不是缺一常备完成authority。

**裁定：限缩吸收。** `definition-of-done.md` §DoD vs Acceptance Criteria/Standing Checklist提供区别、按改动关切核正确性/质量/集成/文档/恢复面，并说明单一测试绿不能等同完整委托关闭。

**边界：**清单是制定/应用已接受质量政策的参考，不能以方法之名新增全库mandatory baseline或自行设policy owner。无所有任务runtime/test-first/human-review/deploy-ready义务；typing/documentation任务证据按claim。政策可由有效authority修订，非永不重新谈判/单调增gate。适用政策和本任务条件均需满足各自授权范围内要求，完成由有效closure rule而非本清单授予。

**可蒸馏落点：**与CD C5合并成 `methods/quality-policy-and-checks.md` §Standing vs task criteria、Apply/cite、Coverage/exception/change、Closure boundary；B/F指针。**补读：无。**至少保留已满足兼容条件和不需runtime的文本交付反例。

## G6 · library changes

**覆盖：部分。** 产品已有source pins、按需和唯一owner，缺变更前查重、负结果留存、生产/消费引用同步与载体可移植性说明。

**裁定：合并。** `CONTRIBUTING` §Before proposing/Modifying、`skill-anatomy` §Shared References/Procedure not Workaround、检查器具体范围支持：先核既有/在飞/拒绝证据，改善优先、记录未成功原因；原义一处维护，用固定可解析引用；改约定时同步真正消费者；支持文件分发也要能解析。机制检查不能由被约束对象自授豁免，其豁免来自有效规则owner。

**边界：**不引入本仓registry/schema/脚本/默认分支发布/固定500行或一层link/三positive两negative门槛。具名工具/版本在实际SDK能力方法可能是关键成立条件，不能因“无法不点名说明”全排；去掉的是无依据且针对一模型的普遍workaround。源的跨模型研究仅引述、未回读论文，不作为已验证收益。source linter自己有机械范围限制，字节一致不证明语义正确，文件在磁盘存在不证明单skill安装可用。源码对500行仅warning；不以文档说法硬化gate。

**可蒸馏落点：**并入A3 `guide-agent-text.md` §Change/traceability/portability，以及Addy EF F7的 `guide-method-evaluation.md` §Prior attempts/evidence；负结果概念并入 `decision-record.md`。methods README只选择/状态索引，不塞贡献治理house rules。**补读：**无需退包；未读全部脚本单测不接受checker运行可靠性；无脚本实施委托。

## G7 · brownfield adoption

**覆盖：该专业操作未覆盖。** 已有约束/授权保护，不等于引入方法到存量体系的经验。

**裁定：限缩吸收。** `adoption-guide.md` §Which path/Path B/Anti-patterns 的识别现状覆盖与未记录承诺、先理解/查真实约定与已有观察、对将改路径用characterization保护、区分存量与新增承诺、交界contract-first、按真实事件/风险补观测并有依据退役。现状表征只说明当前行为，不把已知缺陷接受为正确。

**边界：**这是采用者受其自身有效授权调用的按需经验，不授权TPW或Driver到下游实施。无四phase固定顺序、绿地always-on全生命周期、审查零风险承诺、全存量security audit、无测试绝不改、必须增加而永不撤gate/季度达到稳态。风险/证据足够的既有结论可复用；characterization不能替代B/C接受，也不为“原型可能产品化”要求全部原型写spec。不按年龄机械判断。

**可蒸馏落点：**新 `methods/guide-brownfield-adoption.md` §Assess baseline、Protect affected behavior、New/legacy boundary、Observe/retire、Limits；与change-slicing、rationale、测试质量互指，不强合G5：采用策略与当前policy应用触发不同。**补读：无当前操作承重缺口；**TDD细节由EF裁并去重。

## 可蒸馏批次与7问答复

组合G1→bounded-composition；路由G2→现有选择入口/agent文本；评审G3→共同change-review及dependency guide；恢复G4→共同handoff；政策G5→与CD C5合并；库维护G6→agent文本/方法评估/决定记录；采纳G7→brownfield guide。共享methods README/Profile/cross-module由Driver分互斥写面、串行集成。本表不派工、不授B写面权限。

1. G1/G2不用强合；选择入口承载路由，组合方法只在组合问题出现时调用。2. G3独立change-review，不扩F的baseline/treatment方法。3. 分级统一行动语义、不追随外部grader，三态独立。4. G5与C5合并，G7独立按需采纳指南。5. 不把G6house rules塞methods README，归支持正文。6. 源数值可附来源作例子、非本库阈值；缺依据的数值不当硬边界。7. G4只说artifact/restart契约，排process/model调度，不触runtime实现权。

未执行脚本或真实下游采纳；未关闭全源路径分母。AB源读深缺口已能补则自行补，不退形式循环；CD/EF及addendum继续实质回核。效果、security/perf全部专业资格及全库一致性尚未由本review认证。
