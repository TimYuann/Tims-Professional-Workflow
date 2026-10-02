# REVIEW-A2R-CURSOR-ABC2

tpw-absorb-gate，2026-10-02。5/5实质裁定：合并MG-1/3/4，限缩吸收MG-2/5；全组含可蒸馏部分，不计五个独立增量。非正文、集成或运行接受。

固定包：`docs/absorption/2026-10-02/packages/A2R-CURSOR-ABC2.md`，读取blob `80c1e6c8ed9b945bdd511a697fe96697a48a25a5`。固定产品仍为`800414dd9eb517f7132223866fe484d28a8bbf0b:professional-workflow`/tree `7c814e54c5e775045bc1c5155e3c181ceb1345fb`；按基线三方法、两guide、相关Profiles及Charter直接核覆盖。源本地cursor-plugins pin `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`，本轮已核HEAD/status；以下路径相对pin。

直接回读：`pstack/skills/principle-{sequence-verifiable-units,prove-it-works,fix-root-causes,build-the-lever,test-behavior-not-implementation,experience-first,exhaust-the-design-space,foundational-thinking,laziness-protocol,minimize-reader-load,subtract-before-you-add,redesign-from-first-principles,encode-lessons-in-structure,guard-the-context-window,separate-before-serializing-shared-state,make-operations-idempotent}/SKILL.md`；`pstack/skills/{tdd,blast-radius,recall,teach,reflect}/SKILL.md`；`cursor-team-kit/skills/{workflow-from-chats,weekly-review,what-did-i-get-done}/SKILL.md`。未执行其中指令；未根据文件内部委派条款派agent或写产品。包的转述、未读docs/运行playbook和支持prompts不当独立观察。

## MG-1 · executable units / proof

**覆盖：基线部分，已裁候选覆盖大部。** local-defect的复现/假说/回归、F claim/版本与mock guide已有；A3 test-first/test-quality/change-slicing及Cursor ABC harness已补主要操作。

**裁定：合并。** sequence §Execution/Delivery取已知状态→有界改动→针对claim检查、交付可恢复证据顺序；tdd §Workflow/If impractical取正确红因、已有便宜路径、合理替代观察；test-behavior取subject真正执行、oracle来源、弱断言具体遗漏；blast-radius §Steps取语义/数据/wire/版本/时间性依赖超出grep、承重安全假设及其反例，confirmed/cleared/unproven分开。lever取有明确收益时先学一个单元再脚本化，验证重跑和恢复条件；与Matt DEF工具验证合并，不新建默认工具框架。

**边界：**无每单元必须独立绿/rebase/commit（宽迁移例外已接受）、凡非trivial必须建工具、每任务最高证明阶梯、所有检查必须脚本。编译可证明类型claim，缓存也可正是被测契约；观测失败调查工具和系统竞争解释，不先验认定谁错。undefined替换是启发而非标准：`toBeDefined()`在subject返回undefined时会失败，源将它列为“仍pass”不成立；禁止搬成机械质量判据。合法absence/调用次数/类型证据按claim判断，防漏错不必全是literal assertion。nil guard可以兑现有效非法输入约定；comment长不证明代码错；clear state仅是因果线索，不授权清数据或证明根因；兄弟缺陷调查不自动扩修改权限。不要伪造概率/毫秒成本。

**可蒸馏落点：**test-first与guide-test-evidence-quality补具体信号/合法例外；change-slicing补单位证据顺序；change-review §Dependencies/critical assumptions补blast-radius；local-defect只补仍缺且有依据的根因/观察面，lever验证放未来`guide-check-design.md`，不重复造“证明”方法。**补读：无所取机制缺口。**perf/hillclimb/a4工具实现不在此关闭。

## MG-2 · experience / structure / reader load

**覆盖：B目标不能被便利替换、D/E自由与约束已有；体验取舍、读者两轴操作不足；design-alternatives/domain-state候选已覆盖部分。**

**裁定：限缩吸收。** experience-first识别终端消费者、API调用者、维护者及具体体验代价；reader-load两轴（追的层/隐藏可变状态）、追“X从哪来、谁能改”实例；foundational的数据形状/访问模式/共享状态先问；redesign用“新要求若从最初存在”作备选方案思考、核受影响依赖并增量交付。exhaust的实质差异方案合A3 design-alternatives及bounded-prototype。

**边界：**不能把各类用户等权或delight压过安全/成本/接受行为写作价值政策；由有效A/B/资源authority取舍。没有固定2–3案、3层/30秒阈值、总是删除/flatten/scaffold先、单caller就删、无第二adapter全无价值、每increment必须新抽象、把新增guard一律当投机或重设计等于全库改权。保留合法鉴权薄wrapper、清楚局部分支和无需scaffold的反例。迁移外部承诺/中间破坏属于受委托D与接受约束，不为其“终态优先”补权限；outcome/migrate具体面留a4。

**可蒸馏落点：**B的消费者/接受行为问题并behavior-contract-examples或decision-elicitation；D/E的读者负担取舍放按需`methods/guide-change-shape.md`（关联cross-module、design-alternatives）。不把所有形态选择误归C，C只给领域不变量。**补读：无；**a4实现面未裁。

## MG-3 · lesson promotion

**覆盖：源身份/决定记录/按需文本部分已有，反馈归纳操作新增。**

**裁定：合并。** reflect §Locate/Apply、workflow-from-chats §Workflow/Confidence/Artifact Choice 与encode §Feedback loop支持：限定有权读取的会话/时间/主题，识别显式纠正、一次性情境/反复模式、证据冲突，给trigger/decision/quality/stop/evidence及置信依据；选择既有规则/方法改进、具体工具或不保存；复用拒绝与轨迹carrier。承重结果不靠原则name-drop；解释方法实际改变哪一选择而非每回复打印标签。

**边界：**强/中/弱不授接受权，“agent自己做且被用”不自动人类偏好；contradiction找实际owner，既有明确授权允许编辑则不再新建全部Accepted最终ACK gate，未授权组织级行为变更不能自行推广。无第二次必编码、固定强度排序、只能结构修复、编码后必须删所有解释、自动建backlog/公开tracker。结构强度按可检测性/误报/维护成本/任务可靠性选择，本轮只吸收方法，不实现工具平台。source“no readonly才MCP可用”的宿主假设不移植。

**可蒸馏落点：**共同`methods/guide-lesson-promotion.md` §Scope/evidence、One-off/pattern、Choose carrier、Accept/apply、Limits；Cursor ABC4/5偏好、Matt DEF-12和Addy方法评估同处去重。decision-record记已接受改变与拒绝，guide-agent-text管载体表达。**补读：无所取机制缺口；**reflect四reviewer支持文件未核，不声称delegated执行可靠性。

## MG-4 · recall / explain / report

**覆盖：handoff与A/Voice原则已有，解释/历史当前事实区分可改善。**

**裁定：合并。** recall §1/2/5与Output取已给足state capsule就用、不跨任务历史盲挖、固定window/topic/workspace、对分支/产物核live状态、区分继承与新增；teach取从读者目的/已知出发，what/how/why分清且保留why置信语言、渐进例子/图按需要；weekly/what-did取明确时间和证据范围、按实质变化归纳，不从commit猜动机。

**边界：**无默认全共享记录search/子agent/map格式、每次resume必须所有步骤。worktree/未提交工作可在用户要求范围报告，merge commit可能承载真实集成；源“shipped”不能由authored commit推出，标committed/merged/deployed需相应证据。身份不明可先用明确可查范围并写限制，不强制用户改git email。理解型解释不需要测验，能力训练另有任务目标不禁quiz；无必须how+why、三个节点要三图、imagegen强制或固定英语。这里只吸收专业交接/解释操作，不开持续教学工作区。

**可蒸馏落点：**handoff-and-resume §Reconstruct/status；按需`guide-professional-explanation.md` §Audience、Mechanism/evidence、Report scope（与ABC4写作整合）；guide-agent-text仅保context load，不重复写历史挖掘。**补读：无；**未执行recall/真实教学，不声称性能收益。

## MG-5 · shared writes / idempotency

**覆盖：Driver已有写集/单写者和runtime排除；前置共享需求及半成品重跑操作新增。**

**裁定：限缩吸收。** separate §Pattern取辨别canonical共享对象还是各自事实、能独立就各自owned输出再单写整合；真正共享则明确有效排他安排。idempotent §Test取连续两次/部分失败后恢复/相同操作末态问题，在D/E侧揭示reconciliation需求。

**边界：**Driver只安排逻辑写面/依赖，不裁定lock/CAS/transaction实现。机构写面约定不证明运行时并发锁已有效；隔离worktree仍不隔离外部DB/key。幂等并非任意起始状态都相同，需有效state与operation identity；无法自然幂等的动作说明防重复/查询恢复/补偿，不假承诺exactly-once。PID可能复用，不直接接受PID-only stale lock安全或content-equivalence足以清理；清理/采用session/respawn均需已有授权，不动未知资源。

**可蒸馏落点：**bounded-composition §Write targets；CLI/API契约 §Repeat/partial failure；技术幂等guide由a4回源整合，与Addy C1共一机制，不在Driver Profile写runtime流程。**补读：**实现算法/脚本正确性留a4，无当前判断缺口。

## 批次与限制

可蒸馏：测试/切片/评审合并；consumer与reader-load限缩；lesson-promotion与后续偏好族合并；恢复/专业解释合并；共享写面与技术幂等分归正确owner。Driver划互斥写面、统一入口，不因机制同源就强合成大文件。未执行、无效果PASS。没有“无法变红就不是证据”的通用归约：否定性搜索/历史引用/类型证明有各自证据条件，不能用oracle/置信五档取代全部验证。A3 overlap图只是去重信号，实际正文与源条件决定归并。
