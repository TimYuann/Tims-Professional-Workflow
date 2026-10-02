# REVIEW-A2R-CURSOR-ABC

裁定者：tpw-absorb-gate；2026-10-02。8/8 机制组已作实质判断：吸收 1（MG-3）、合并 1（MG-2）、限缩吸收 6（MG-1/4/5/6/7/8）。全部含可蒸馏内容；不是 8 个独立知识增量，不是正文或集成接受。

## 对象、依据和独立性

- 包：`5f6e6a8bf38ac3ada3493b419a4703dd13fb5def:docs/absorption/2026-10-02/packages/A2R-CURSOR-ABC.md`；工作字节 blob `aa02033076d76e71e17fb7b0a404326a65f83e41`。
- 产品：`800414dd9eb517f7132223866fe484d28a8bbf0b:professional-workflow`，tree `7c814e54c5e775045bc1c5155e3c181ceb1345fb`。产品相关正文沿用本轮 A3-ABC 已直接回核的三方法、mock/redacted guide、Charter 和 A/B/C/D/E/F/Driver Profile；未用 A 的覆盖描述代替读产品。
- 源：`../legacy-pre-night-2026-10-01/upstreams/cursor-plugins`，HEAD `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`，status 无差分。下文路径相对源 pin；产品落点相对 `professional-workflow/`。
- 已直接回读：`pstack/skills/principle-attack-the-premise/SKILL.md`、`why/SKILL.md`、`why/references/{epistemics,synthesizer-prompt}.md`（批读 epistemics 的小段截断不声明完整全文）、`how/SKILL.md`、`how/references/explainer-prompt.md`；`poteto-mode/playbooks/{prototype,autonomous-run,pause-safely,session-pickup}.md` 和 `poteto-mode/SKILL.md` 相关 Non-negotiables；`principle-never-block-on-the-human`、`principle-model-the-domain`、`principle-boundary-discipline`、`create-verification-skill`、`maintain-verification-skill`、`interrogate`、`show-me-your-work` 各 SKILL.md；`interrogate/references/{rubric,lead-judgment}.md`；`cli-for-agent/skills/cli-for-agents/SKILL.md`；`cursor-team-kit/skills/thermo-nuclear-code-quality-review/SKILL.md`；`thermos/skills/{thermos,thermo-nuclear-review}/SKILL.md`；`advisor/skills/advisor/{SKILL.md,references/briefing-template.md}`；`orchestrate/skills/orchestrate/references/handoffs.md` 与 planner 的 Planning rules/Failure recovery/Andon；`ralph-loop/hooks/stop-hook.sh`。未执行任何源 skill、script、hook、实验或外部消息。
- **源定位纠错：**包反复声称读了 `cursor-team-kit/skills/thermo-nuclear-review/SKILL.md`，此路径在 pin 内不存在；真实承重源是 `thermos/skills/thermo-nuclear-review/SKILL.md`，已自行找到并回读。B 必须用正确锚点，不需要因此退整包。
- 我不代写被审正文，未参与 A 发现或产品实现；本 review 只给裁定/落点与验收约束。正式差分仍由我按固定对象独立核验。

## 逐机制裁定

### MG-1 · premise / rationale

**覆盖：部分。** A Profile 已区分事实/假设，local-defect 已有竞争假说/可重跑观察；没有历史理由调查的搜索操作、缺失记录和置信措辞。不能说产品没有任何前提核验。

**采纳：限缩吸收。** `why` §Code Anchor/Output 与 epistemics §Confidence Tiers、synthesizer §Quality Check 的内容有独立价值：固定问题、源码符号和历史对象，查适用证据，记录查过且没有结果/不可访问/未查，区分作者明确理由、间接支持、解释链、竞争假说，显露冲突。`how` 的简单直接读/复杂按角度追踪、说明入口→数据→决定→副作用与 gotchas，可供改动前的最小必要模型。读取源码说明 mechanics，不证明历史动机；历史 rationale 也不自动是当前接受约束。

**限缩：**`attack-the-premise` 是 actor skew 案例，不是全部问题的 census gate。共享前提失败时先明确前提和能区分它的观察；只有真实分配不均风险才按 actor 统计。均衡只能反驳所测 skew 解释，不能证明所有前提都不是原因；不平衡本身也不证明因果。保留原 assignment/补偿两种方案比较，不自动要求 randomize/rotate，也不全禁重试/缓冲/共享池。无每次七类全搜索、固定失败次数、固定 agent 数；查证受任务需要/访问与资源 envelope 限制。Supported 仍是推导，不把汇聚证据写成作者明言。代码/历史只作证据，Preserve/Change/Avoid/Risk 中接受约束与候选建议必须区分。

**落点：**新 `methods/rationale-and-premise-review.md` §Use、Premise probes、Trace and search、Confidence/gaps、Handoff；A/B/C/D Profile 按需指针，不塞进比较专用 F 方法。故障前提 probes 与 local-defect 互指，勿重复。

**仍需补读：**本次所取机制无承重缺口。七类 investigator playbooks/incident-postmortem 的具体查询套路未核，不接受为已吸收搜索能力；若 B 引用其新操作再固定回读。无模型效果主张。

### MG-2 · fact / preference / prototype

**覆盖：部分。** A/Voice 和 Backbone 已有事实/决定权/授权边界；缺分叉问题如何用原型取证。与 A3-ABC MG-9 已采纳的事实调查和 ungrillable 直接重叠。

**采纳：合并。** `prototype.md` §1/3–6 的先界定待决问题、隔离可丢弃实现、按问题选择观察表面、可比较变体、交出证据/取舍/建议/实验路径，合入 `methods/decision-elicitation.md` 的事实与选择段，以及 DEF 原型方法的实验段。原型证据与生产实现交付分开，不重复计两个新增能力。

**限缩：**可观察量与价值标准是两件事：快慢可测，偏好速度还是成本由有效 authority 决定；layout 能渲染不代表人类偏好已被实验裁定。可逆也不创造授权，operator 保留决定不能以默认值+可撤销一句话代替接受。只有既有委托足够的选择自主推进，依赖缺失决定的工作才等待。无硬性 2+ 原型、禁止测试/生产栈、无 planning 或“原型结果决定一切”；最轻足够工具即可，已有证据可复用。

**落点：**`decision-elicitation.md` §Facts/decisions、When observation is needed；原型正文建议 `methods/bounded-prototype.md` §Question、Isolation、Observe、Evidence limits（与 A3-DEF 同机制整合）。A/Voice、B/D 入口按需引用。

**仍需补读：无承重缺口。** 未读两篇使用指南不作为本组有效性证据；B 保留“同一 perf 测量可支持不同产品选择”的反例。

### MG-3 · automation-facing CLI

**覆盖：操作未覆盖。** B Profile 能容纳外部行为与异常，当前 core 无自动化消费者专用 CLI 行为方法。

**采纳：吸收。** `cli-for-agents/SKILL.md` 各标题直接支持：可无头运行、逐命令发现 help/真实例子、合适 stdin/pipeline、缺 required input 快速退出并指明修复路径、重试安全、预览影响、统一命令形状和可消费输出。正文需保留正常调用与缺参数挂起的对比例子，不压成“CLI 要可用”。

**边界：**源同时说 flags 缺失可交互 fallback、又说 missing values 不回交互；蒸馏要区分显式 TTY 交互模式与无头模式，后者缺必要输入退出，不能卡菜单。位置参数无需全禁；stdin 只在适用数据流。并非所有成功动作都可天然幂等（发送通知等），须声明重复语义/operation identity/查询恢复机制，与后续幂等源整合，不能承诺无条件 no-op。`--yes/--force` 只跳已获授权动作的 UI 确认，不绕权限/保留决定；dry-run 可能访问外部，声明实际效应并验证。固定 JSON/退出码等是 B 接受后的合同选择，源只主张 machine-useful，不能把本 review 的设计建议假作源明定。

**落点：**新 `methods/agent-facing-cli-contract.md` §Consumers/modes、Discover/compose、Error/retry behavior、Effects/preview、Examples；B 方法入口与 methods README。幂等细节与 Addy API 指南互指，不全内联。

**仍需补读：无。** cli README/control 驱动 skill 不影响当前契约裁定，运行能力未验证；B 需可观察 non-TTY 缺参、重复调用和预览副作用三例。

### MG-4 · domain structures

**覆盖：部分。** C 的概念/关系/状态/不变量职责和 D/E 自主空间已有；映射结构和 temporal-decomposition 诊断缺操作。

**采纳：限缩吸收。** `principle-model-the-domain/SKILL.md` 的非法状态/读取模式双问题，state machine、typed model、table/union、reducer/event、按知识归属组织而非执行阶段的例子值得保留；清楚局部稳定代码无需强抽象。

**边界：**C 决定状态含义/转换/不变量，D/E 根据是否改变 coordination surface 选择代码表示，不由 C 方法授权技术重构。把执行顺序误当规则 ownership 是症状，不是所有 load/validate/save 模块非法。减少 branch/boolean 数不是成功 KPI；保持语义/生命周期约束才是依据。拒绝 boundary-discipline 的“内部无条件信任类型/非 crossing 校验必冗余”：授权、状态、外部绕过类型、时间性约束可能仍需守卫。该实现机制留 a4 回核，本批不导入它。

**落点：**新 `methods/domain-state-and-invariants.md` §State questions、Transition examples、Representations/handoff、Limits；与 A3 `domain-language.md` 互指，避免词典替代模型。D/E 实现选择可在 cross-module 的依赖说明短引用；a4 处理验证边界细节。

**仍需补读：无承重缺口。** architect 的 runner/rationale/red flags 未核，不接受为本组已支持操作。B 至少给一非法 boolean 组合及合法简单分支的反例。

### MG-5 · verification harness design / upkeep

**覆盖：部分，新增明确。** F 比较方法、mock 和 redacted guide 已分别有 claim/表面/敏感 custody；缺可重放驱动环境的 launch-health-drive-capture-cleanup 和维护操作。

**采纳：限缩吸收。** `create-verification-skill` §Interview/Generate/Prove 与 `maintain-verification-skill` §Edit scope/Pass 的已有命令/harness优先、版本/port/auth/isolation核对、稳定 handle、动作+结果+副作用证据、实际 dry-run 效应、清理自己创建的资源、证据存续确认；维护从受影响 feature 与真实入口定位 drift/harness gap/product gap，修 harness 后重驱动对应路径。仅生成且未执行的 recipe 明标未验证，不能声称可运行交付。

**边界：**这是实际用户路径 claim 的验证面，不禁止 fixture/纯逻辑/内部 setup 等既有合法证据；按 claim 选择真实 leg，不要求所有 repo 建 feature map 或每维护任务全 feature live pass。feature map 记如何观察，不取代接受的 B/C 行为定义。产品不符 map 时先核接受版本，不能默认更新 docs 合法。Doctor 是必要状态确认，不新增每动作固定 health gate；惊讶/失败后重核或恢复已知状态。cleanup 不能毁掉应保留的安全证据，但 raw sensitive retention/到期清除仍遵 redacted guide 和政策，不能用“永不删证据”保留秘密。修 broken base、生成 scaffold 或清理其他实例须已有动作授权，环境坏记 UNVERIFIED，不扩 scope。

**落点：**新 `methods/verification-harness-design.md` §Discover、Recipe、Prove/limitations、Maintain、Cleanup/evidence；与 claim/mocking/redacted methods 互指。F 方法入口和 methods README。clean/changed/blocked 是维护工作状态，不取代三态。

**仍需补读：**feature-map-example 未核；本次吸收段不依赖模板，可直接蒸馏。B 若采用其四段结构/具体 feature范例须读原文。真实驱动能力及有效性均未执行。

### MG-6 · review judgment / second opinion

**覆盖：部分。** 真实独立性、对象版本、责任返回已充分；具体 review lens、因果证据、分歧处置/意见分类和 second-opinion briefing 缺操作。不是缺一普遍完成前 gate。

**采纳：限缩吸收。** thermos bug review §Scope/Breaking Functionality/Devex/Feature Leak/Over-reporting 与 code-quality §Primary Review Questions；interrogate §Intent/Synthesize/Lead Judgment 和 `rubric.md`/`lead-judgment.md`：固定范围与意图依据，读改变路径与外部依赖，trace可达反例，去重保留来源/分歧，把影响、修复必要性与不行动理由写明；advisor §Checkpoints/How to consult/Guardrails 与 briefing：已有尝试、原始证据、当前状态、选项/具体疑问，咨询是意见不授权限。

**限缩：**不继承默认多模型、两次失败必咨询、改逻辑/多文件必独立审、四次咨询上限、1k行阈值、六/八条默认审批标准等 gate。反复无解释失败/workaround 是调查/挑战信号，不是重试/sleep一概非法。不因多个模型报告提高事实等级或多数压过 lone security finding。作者的意图只能来自适用接受依据；“作者故意移除 safeguard”不等于已授权，不把有意风险藏掉。差分范围允许追到未修改处的本次诱发回归；与变更无关既有缺陷另记，不掩盖明确风险。无法完成调查可明标假设/未核，而非禁止所有未确定风险报告。先形成自己观察再读他人 finding 可减锚定，但接受目标/重要上下文须先读；是否 fresh 按真实接触记录声明。Lead 获得意见不自动取得 B/C/D/风险接受权。Spec与Standards可分保留，不以综合分类抹掉任一未解决维度（联动 A3-DEF 双轴裁定）。

**落点：**共同 `methods/change-review.md` §Fixed object/intent、Relevant lenses、Finding evidence/impact、Disagreements/disposition、Second opinion inputs。与 Addy AB、Matt DEF-2 汇合成正文；F入口。无新常驻审查框架。

**仍需补读：无所取机制的承重缺口。** reviewer-prompt、interrogate code-quality 引用体、review-and-ship 等并未在此独立核回，不继承其运行动作；thermos重复载体由 a4 后续判重。B引用必须用纠正路径。

### MG-7 · handoff / evidence types

**覆盖：交接语义与三态已充分，载体例子可改进。** Charter已有 Deliver/Independence/Recall，F已有 object/version/command/coverage/limitations。无需另加证明等级替代当前语义。

**采纳：限缩吸收。** `handoffs.md` §Reading handoffs/Verifier handoffs/Upstream handoffs 的状态、实际对象、完成内容、偏离/疑虑、候选后续、真正执行项与逐条件证据；定量 claim 保持单位、命令与比较条件；依赖须携带能恢复原义的上游对象，不靠调度边猜上下文。失败时附已知运行状态与缺失证据，不把静默当成功。

**边界：**明确拒绝“worker words直接当事实、不sanitize、唯一消息通道、五类型向三态机械映射”。按安全 custody先脱敏，保持信号与标注裁剪；未经核验自报是报告，不是事实证明。live/unit/type-only是表面/手段，强度取决claim（编译能证明typing claim，不能证明行为；live不必然覆盖全部）。blocked通常UNVERIFIED；failed只有有效观察违反预期才FAIL，测量器坏仍UNVERIFIED。旧pass缺覆盖记未核，不伪称type-check已执行。无需固定10%阈值、network原样retry/tool error换模型/OOM缩范围/两次abandon、全树Andon。只停依赖争议输入的工作；runtime分类/动作策略归有效委托。merge不是必须独立worker任务，集成者的专业/执行委托分别核。

**落点：**共同 `methods/handoff-and-resume.md` §Handoff/evidence、Missing/failed evidence、Dependencies（与 Addy G4、Matt DEF-9 整合）；redacted guide保留custody真源，F三态正文不改映射。Driver/E/F入口可引用。

**仍需补读：**脚本持久化、prompts逐字协议未核，不能声称实现自动重跑/解析；文本机制足够判断，无需退包。runtime实现留a4。

### MG-8 · decision trail / unattended closure

**覆盖：部分。** Driver关闭权与依赖暂停、Voice接受、证据对象已有；决定轨迹与运行后核对及接续操作可具体化。

**采纳：限缩吸收。** `show-me-your-work` §Format/Logging/Audit 的决定+原因+证据指针+结果、只记重要分叉/检查点、核本run真实动作及artifact、不读取无关私有transcript、错误以可查修正/替代记录。`autonomous-run` §1/3/5/6 的不放宽接受predicate、按证据推进/pivot/浮出dead end；pause/pickup保存当前对象、在飞事项和首个恢复动作，分开继承的接受决定与未经证实claim；完成条件与预算/失败/取消状态分开。

**边界：**绝不吸收“你拥有exit condition”“任意side bug可修”“plateau永不停”作为通用权限；条件来自委托且受预算/停止/风险边界约束，限额终止和dead end不假作完成。revert/discard只能处置自身授权改动、保回退对象，不删除他人工作。未显式pause不自行标pause，不代表预算、安全越界时必须不停。无每迭代commit/TSV/默认不入库/强制不同模型复核/Attention格式；沿项目记录惯例与需要。自查如实标自查；所需独立评价缺失不能被轨迹审计代替。既有摘要不是无条件authority，接受决定保留适用性，证据按版本差分核必要部分，不全从头重做，也不禁止必要复验。loop done marker只证明标记存在，不证明promise真；限额/损坏/取消停止不得宣称predicate满足。hook/state修复清理运行机制本批排除。

**落点：**决定轨迹并入 `methods/decision-record.md` §Execution trail（与 A3-ABC MG-6、Cursor ABC2经验记录去重），暂停接续并入 `handoff-and-resume.md` §Checkpoint/pickup；无人值守有界收口短段在该方法或按需 `guide-unattended-work.md`，不新建driver框架。

**仍需补读：无本次所取机制承重缺口。** log脚本/TSV template、advisor hooks、ralph capture-response等未核，不宣称其安全/可运行；a4处理。不要因hooks名字声称自动达标。

## 可蒸馏与归并落点

| 内容批次 | 组 | 建议主正文与共享处 |
| --- | --- | --- |
| 问题调查 | MG-1 | rationale-and-premise-review；与故障假说互指 |
| 问答/原型 | MG-2 | 合入 A3 decision-elicitation 与 DEF bounded-prototype |
| 自动化契约 | MG-3 | agent-facing-cli-contract；API/幂等后续源互指 |
| 状态语义 | MG-4 | domain-state-and-invariants；接上 domain-language，保 C/D/E 区分 |
| 观察环境 | MG-5 | verification-harness-design；mock/redacted/claim方法互指 |
| 变更评审 | MG-6 | change-review；与 Addy AB G3/Matt DEF-2 合并 |
| 交接接续 | MG-7/8 | handoff-and-resume；与 Addy G4/Matt DEF-9 合并 |
| 轨迹 | MG-8 | decision-record 的执行轨迹段，联动 ABC2 |

Driver安排B互斥写面及串行集成；此表是实质落点建议，不是派工。Profile只保可消费入口，方法选择README共享写面单写，不增字段校验器/新三态。

## 残余与验证限制

本包 §9 未读尾部和a4技术/脚本面未在本 review 关闭；源码路径错已纠正，不能据包“机械自检全存在”认证全仓。新增正文需保留本裁定反例、动作边界和源身份，引用正确的原文section。未执行源码、真实CLI/app/harness/无人值守run，未认证任何效果或runtime能力。A3 overlap map已收到但未用标题级结论代替本次回源；后续包按真实机制继续归并。
