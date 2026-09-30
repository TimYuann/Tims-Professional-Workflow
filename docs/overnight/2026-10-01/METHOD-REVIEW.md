# 关键方法评审 · MR-01

日期：2026-10-01。评价者：`tpw-night-method`。委托：Driver 本轮固定对象的 M1-B1 差分、M2 配置与 M4 §8 候选比较。

## 独立关系与范围

我不是 Profile、M2 Charter/入口或 SOURCE-SURVEY 的作者；此前给出 M1-B1 反例与补证要求，没有代写候选。本轮只读候选与必要源正文，只写本报告。该关系支持独立方法评价，不替 Oracle 接受实际交付或关闭夜间委托。

未重做外部计划评审，未读旧 roles/compose/history，未介入 M3 fixture，未修改产品或上游，未新起会话或新增 gate。原 `PROFILE-EVALUATION.md` 的 FAIL 原样保留；本节追加对后续对象的判断。

## 固定对象核对

以下 SHA-256 均实测与 Driver 指定值一致，包括更正后的原报告摘要。其余六份 Profile 实测仍等于原评价表；本轮不重评其未变 claim。

| 对象 | SHA-256 |
| --- | --- |
| PROFILE-EVALUATION.md | `2fef2e0751b4b267166daf8f96b57e658d710cd7a3a9382fae505543c7edad9c` |
| PROFILE-CANDIDATE.md | `38867970b803f86c8555b61cbc14e9a88f41a6a001f0db87a29379a370fc0dd1` |
| profiles/driver.md | `8a2f42c874ca08c94b06e20131623178f5a45bc6b7d419a3a8fb7ce1651be399` |
| professional-workflow/README.md | `5f2921fda1d01214e612410bce723216d416d626641ea31378f41ead4916ea9d` |
| charters/README.md | `7c86612a561b5d56f7efadb672dfb6b0c62f0f7a674b47b6d204956fa4137edb` |
| charters/template.md | `313a99f242fd4ef5164f8b233e61295998b17d0b7e4f757bb13a709018dbae7e` |
| charters/examples/implementation-cross-module.md | `203d5d64d1266b4833de6a87f2de9073f1ef9bca11ef4795229e6f6050e4977c` |
| charters/examples/implementation-local-fix.md | `98f8f373a7f2cdd6868b761f3777620297dfc4bd600486886fb24b470bf292f6` |
| SOURCE-SURVEY.md（仅评价 §8） | `31f638eb6d27a059aca813588ca7d77476b2c5fab318247bccb5b41135fb697e` |

基准仍为接受计划与冻结 Backbone，重点 §§2–4。正文和例子完整阅读；SOURCE-SURVEY 的其他节只用于定位原始文件，不接受其全库调查 claim。

## 结论与继续范围

| 新增 claim | 方法判断 | 范围 |
| --- | --- | --- |
| M1-B1 修订 | **PASS** | 新 driver.md:37 明确先返回实际判断/边界 authority，仅人类保留决定进入 Voice；原唯一阻断已解决。原报告的其他支持范围可继承。 |
| M2 委托记录与薄装配设计 | **PASS** | 模板、说明性例子与 cat 入口能表达所需绑定，不自授权；没有发现要求增设 schema/权限引擎的依据。 |
| M4 §8 活跃路径候选适配 | **PASS** | 主候选及有限补充有源正文支持，适合进入有界选择/蒸馏；不等于原文整包采纳、最终 Skill 接受或 M3 覆盖。 |

**本轮没有新增阻断 finding，也没有需要 Owner 新授权的裁定点。** Driver 可继续 M2 实际绑定与 M4 有界采用工作。实际实例委托、运行闭环、最终 Skill 及交付资格尚未在这些对象上验证；不能将这份方法 PASS 外推为它们的 PASS。

## M2：委托继承与装配

模板要求实际 delegation source、decision owner、granted authority；接受输入有版本、条件和接受责任。Object scope 区分预计触及对象与显式边界，Tools and actions 区分可用工具和允许动作，末项分别绑定 acceptance / verification / action / closure。缺授权不由 Charter 文本补上，符合 Backbone §2。

两份例子都选同一 E Profile，但局部修复依赖既有行为与失败观察，跨模块实现依赖 B/C 和 D 的 Plan；自主空间、对象与召回条件随任务变化。局部例子没有强制重做 A–D；跨模块例子要求另一实例挑战相关 Plan，结果评价者不得是实现者，且分别记录贡献与时点，符合 Backbone §3 的对象独立性要求。

README 明示例子不能直接激活，须替换为真实授权与输入；因此支持的是绑定设计，不是“这些示例已经继承了实际授权”。正式 Charter 仍要有可恢复的接受输入与实际委托，不能把占位描述当版本引用。风险/资源/整合权限若被本次工作依赖，可通过 delegation、accepted inputs、preserve 和末项引用其 owner/条件，无须新增全任务字段清单。

实际运行 `cat implementation.md implementation-local-fix.md`，观察 Profile 在前、Charter 在后且文本完整，无旧装配依赖；文档明确任务输入是第三项，由调用者提供。我没有提供或执行真实任务输入。这证明基本拼接方式可用，不证明未参与设计实例的冷启动或授权充分性。文件读取失败时仍应检查命令 exit，不能把部分输出当完整 prompt；当前没有观察到足以引入额外脚本的机械成本。

## M4：必要正文核对与采用建议

本轮直接完整读取下列源文件；只是评审输入，没有执行这些 Skill 的委派、发 PR 或其他操作指令。三个仓库 HEAD 实测与 SOURCE-SURVEY 的 pin 一致。

| 固定来源 | 完整读取的相对路径 |
| --- | --- |
| S3 `c55ee46073ed923f86ce59a5eb3b6d895095d1b7` | `skills/engineering/diagnosing-bugs/SKILL.md`；`codebase-design/SKILL.md`、`DEEPENING.md`、`DESIGN-IT-TWICE.md`；`code-review/SKILL.md` |
| S1 `2686b620fc1fed2e8f60c704839c766b8594c6b6` | `skills/debugging-and-error-recovery/SKILL.md`；`skills/api-and-interface-design/SKILL.md` |
| S2 `ecc249f1e306fc64ddf83c7bed16cacf7c2239db` | `pstack/skills/poteto-mode/playbooks/bug-fix.md`；`cursor-team-kit/skills/verify-this/SKILL.md`；`pstack/skills/interrogate/SKILL.md` 及其 `references/` 四份正文（reviewer-prompt、rubric、code-quality-review、lead-judgment） |

### 局部修复

支持以 diagnosing-bugs 的症状专属反馈回路为主：已实际跑过、能红、足够快、确定或有稳定复现率，再用证伪探针定位根因，修后重跑原场景。原文适用“hard bugs”，允许明确解释的跳步；对于已经有契约和失败观察的局部缺陷，应复用回路，不重复建平台、穷举十种构造法或强制三至五个无意义假设。

边缘增量可限于：S1 的非可复现分类与错误输出作为不可信数据；S2 的同表面复验、机制需运行证据。失败 repro 先入 Git 历史可作为适用时的交付纪律，不必为每次修复制造额外提交。S1 Stop-the-line 应限于依赖故障的工作，不变成全队停工。S2 “跨函数就 architect”、默认委派模型、/loop 和 Opening a PR 不继承为本包规则：函数边界本身不等于 Backbone 的共享承诺边界，来源操作指令也不产生本夜发布权限。

### 跨模块设计与词汇 owner

支持 codebase-design 的 interface 全义（调用者须知道的约束、顺序、错误与性能）、seam 位置、depth-as-leverage 和 DEEPENING 的依赖分类用于 D 的分析。它们不能自行决定 B/C 意义、freshness 责任或任务接受权；也不要求为了“深模块”合并所有模块。测试穿过真实 interface 很有用，replace-don't-layer 仅在新覆盖已经替代旧覆盖时适用，不自动授权删测试或扩大改造。

**建议词汇 owner：** 本包责任/授权词汇由冻结 Backbone 拥有，领域词汇由本次 C 接受对象拥有；D 方法可使用 module/interface/seam 的技术词汇，并显式记录 seam 是可替换行为的位置、interface 是依赖者所需知道的全部事实。不要把 Backbone 的“边界”全局改成 seam。matt 的禁用 boundary/API 是其内部词汇纪律，限缩移植时说明该调整，避免声称原文逐字采用。

S1 适合补 contract first、可预测错误语义及保持现有消费者约定；无需一起搬入 REST、分页、命名表。§8 建议保留的 idempotency 三态与 retention 只有在真实路径涉及重试/副作用时才加载，目前只列候选不足以证明需要采用。DESIGN-IT-TWICE 延后合理；有实质方案分歧时可保留比较纪律，不把 3+ 子代理数量变成产品要求。

### F：证据方法、挑战与独立性

verify-this 的 baseline/treatment 在同命令、数据与环境下比较，支持具体变化 claim；它并不覆盖一切 F 判断。对应有效反证可映射 NOT VERIFIED→FAIL，预测阈值满足可映射 VERIFIED→PASS；缺有效 baseline、噪声或测量失败是 INCONCLUSIVE→UNVERIFIED，不能仅按标签机械转换。观察对象和覆盖仍必须说明。

interrogate 提供同 rubric、去重、共识/独见/分歧与 lead judgment；code-review 提供 Standards/Spec 分轴，二者是不同候选用途，不必常驻同时执行。模型多样性、多个标签或 fresh 仪器均不证明作者独立性；关系由 Charter/实际贡献声明，Backbone 独立性标准仍是责任 owner。§8 将这个缺口留在 Charter 层是正确的。

必要补充观察：interrogate 的 code-quality-review 支持正文含 1000 行阈值、激进结构审查、presumptive blockers 等偏好。§8 的合成程序摘要不能被当作这份全部 lens 已与本包相容；若只采用合成/相关 rubric，就显式延后其硬阈值和机会性重构倾向。单模型发现不能因缺共识而丢弃已有的正确性/安全反证，lead-judgment 本身也提醒单模型安全/正确性问题需认真处理。这是采用范围说明，不阻断当前“候选地图”继续。

## 可选修订与开放处置

- 可在 M4 下一份处置索引中把 debugging/api/F 各自的“主正文 owner、补充锚点、延后项”记清；无需三套平行流程。上列建议不要求修改当前地图后才推进。
- SOURCE-SURVEY 称 diagnosing-bugs “无平台依赖”可理解为主回路不依赖指定平台，但原文 HITL 分支引用配套脚本；若实际采用该分支，须完整核读并携带 `scripts/hitl-loop.template.sh`，使该引用可恢复。当前未采用此分支，不形成 blocker。
- S4/S5 延后保持：本轮不将其旧摘要或镜像抽读当作新正文证据。只有选入活跃采用路径时，按委托要求固定原文/镜像并全文核读。
- 最终采用若改变活跃 Profile/Charter/Skill/routing 含义，按已有计划标受影响 M3 coverage 失效并定向重验；本报告不增加新的重验 gate。

Driver 最少待办是按上述有界建议作实际选择与记录，并填写真实 Charter；不需把每个开放候选送 Owner，也不需将本报告再作为 Oracle 的实际交付二次方法 gate。

## M4 adaptation · MR-02

日期：2026-10-01。固定对象：`METHOD-CANDIDATES.md`，SHA-256 `dfbf6349522dcda65d68c2120a2516591907f483a1999c621bc1925fc4b4dc13`，实测吻合。作者 `tpw-night-source`；我只提供过 MR-01 的判断与限缩建议，没有代写该 dossier 或产品。本轮独立关系仍成立。

只核该实际蒸馏对象，沿用 MR-01 已完整核读的必要正文；复核三仓 HEAD、源章节位置、冻结 Backbone 与 Charter template 摘要，均未变化。不重审 §8 全库地图、外部计划或实际交付；既有 MR-01 与原 M1 FAIL 记录保留。

**结论：PASS（有界蒸馏 dossier 的方法适配），无阻断 finding。** 三条方法的 retain/narrow/strip 与源正文及 MR-01 相容，可供 Driver 串行形成所声明范围的 Skill 候选。不等于最终 Skill 正文已接受、真实演练已覆盖或 Oracle 已接受交付。

| 方法 | 核评结果 |
| --- | --- |
| 局部缺陷 | 保留症状专属 red-capable 回路、证伪探针、正确 seam 与原场景复验，准确抓住 diagnosing-bugs 主体；明确允许复用已有观察与有解释的限缩，未把构造法数量/假设数量变成仪式。S1 仅补非可复现分类和不可信输出；S2 整体未采用，平台/模型/跨函数强制 architect/PR 指令剥离有据。HITL 未启用且依赖处置可见。 |
| 跨模块设计 | interface 全义、seam、depth、deletion test 与四类依赖来自所列源正文。测试替代以已有覆盖为条件，避免从方法推出删除许可。S1 契约/错误/兼容元素有限补充，REST/幂等/大规模比选延后，未扩大当前采用面。词汇 owner 保留 Backbone/C，不将源词汇纪律变成责任边界改名或 B/C 决定权转移。 |
| F 变化 claim | baseline/treatment 同命令/数据/环境及原 artifact 比较忠实于 verify-this；VERIFIED→PASS 保留方向、阈值与无明显混淆，NOT VERIFIED→FAIL 对应有效比较下的未变/反向/未达阈值，测量无效或不可比→UNVERIFIED。对象、版本、覆盖及“非一切 F 判断”限制齐备，未以仪器新鲜度代替真实独立性。 |

### 来源与 anchors

三仓 pin 与 MR-01 实测一致。dossier 主/补表中的 pin + 仓库相对文件路径足以定位当前有限正文，仓库身份可由它所固定引用的 SOURCE-SURVEY 取回；这是可恢复的来源链，不是“全部来源已吸收”。后续导出包若不携带过程地图，应把必要 locator/pin/路径一并保留，不能留下只有本机路径的断链。

关键正文锚点已直接核对：

- S3 diagnosing-bugs：`Phase 1: Build a feedback loop`、`Completion criterion: a tight loop that goes red`、`Phase 5: Fix + regression test`。
- S1 debugging：`When a bug is non-reproducible`、`Treating Error Output as Untrusted Data`；Stop-the-line 的缩小明确标为改动，不冒充原文原样含义。
- S3 codebase-design：`Glossary`、`Principles`；DEEPENING：`Dependency categories`、`Testing strategy: replace, don't layer`。
- S1 api：`Contract First`、`Consistent Error Semantics`、`Prefer Addition Over Modification`。
- S2 verify-this：`Workflow`、`Verdict Rules`、`Output`。

当前文件级 anchors 足够这三条短源的复核；加上述章节名能降低最终采用者回源成本，属于可选改进，不要求追加逐句映射表。

### 三态、独立关系与 gate

verify-this 的有效性判断先于三态结论：例如命令失败、无有效 baseline 时，即使输出数值未达阈值，也落 UNVERIFIED，不能套 NOT VERIFIED 判产品 FAIL。dossier 已将这些情形单列，严格映射成立。若有效观察已经证伪明确 claim，则保持 FAIL，不因环境另有无关故障软化反证。

Charter template 的 Independence 字段记录具体对象上的 author/challenger/evaluator 与时点；F 方法不定义作者独立性标准，标准仍来自 Backbone §3。该分工与 M1 Profile 的独立性边界相容，E 可使用回路自测但不能由此产出独立 F 结论。三态、动作许可和 closure 分别成立，没有新增接受/发布授权。

“无回路不进入假设”“先定契约”是所选方法适用时的工作纪律，不是任意任务的 mandatory applicability trigger。dossier 未将其放大为全项目审查义务；DESIGN-IT-TWICE、interrogate、code-review 都明确延后/候选、不设常驻并行 gate。S4/S5 仍未进入活跃路径，旧摘要没有获得新的正文证据资格。

### 可选精确化

1. S1 的“加字段不改删”可表述为“在须保持现有消费者约定时优先兼容扩展”；这忠实于 Prefer Addition 的意图，也避免未来读者误以为有权接受的破坏性变更永远被方法禁止。错误格式一致性同样针对本次被依赖的接口，不必强迫整个系统每层采用同一种返回形状。当前 dossier 的 B/C 权责限制已经兜住该边界，不构成 blocker。
2. 当前 S2 bug-fix 标为“不采用/仅可选”，应在最终 Skill 中保持这个状态；若下一版实际纳入其独有正文，再记录新增采用差分。已有主方法覆盖同表面复验不代表 S2 整体被采用。

最少继续动作：Driver 可按上述已界定范围串行集成，并保留来源/处置；只有新增实质语义差分才需按原计划复核受影响 claim。没有需 Owner 新裁定点，不要求对本 dossier 再造一轮 gate。

### MR-03 · M2 README 状态差分附记

2026-10-01；只核 `professional-workflow/README.md` 状态段，新 SHA-256 `89ade543391c7cf52770648902cf770850a8d38a778d46d99faed587192e84f5` 实测吻合。其余四份 M2 对象摘要仍与 MR-01 一致，未重新评价。

**PASS，无阻断。** `ORACLE-ACCEPTANCE.md`（实测 SHA-256 `630e564f1bff8acaed2a7547bf9df53b8174ee5c159b5233294e86ade2c49a4f`）明确接受 M1 Profile 固定内容作为后续输入，引用的 `M1-REPORT.md` 摘要 `d2184f964bf3422b60c80ab4598c45cfe606a5f77777f137dc84dceefaedf733` 也匹配，七份 Profile 摘要通过该报告可恢复。README 将 Profile 内容的接受与候选方法入口、M2 说明性绑定、真实授权及冷启动分开，准确继承这项 Oracle 接受，不冒充 Owner 新接受或扩大权限。与 MR-01 的 M2 设计 PASS 一致；该状态更新不改变装配或责任语义，不触发完整 M2 重审。

### MR-04 · M4 dossier 兼容性表述差分

2026-10-01；固定新对象 `METHOD-CANDIDATES.md`，SHA-256 `9e6518449869b02de7089da12ef0ad76bd48361eb9d5594397747cc794ff0ff5` 实测吻合。只核 §② S1 三原则的一句变更及文末修订行；将该句还原、去掉新增修订节后，内存中重建的旧文本 SHA-256 精确等于 MR-02 的 `dfbf6349522dcda65d68c2120a2516591907f483a1999c621bc1925fc4b4dc13`，确认其余内容未变，未写入候选文件。

**PASS，无新增阻断。** “本次必须保持既有消费者约定时优先兼容添加”准确限缩源方法的兼容性偏好；显式保留有效 authority 对破坏性变更的接受权，符合 Backbone §2–4，不让方法产生否决权或自行授予变更许可。修订行保留 candidate 状态，没有新 trigger/gate、独立性或三态差分。原 MR-02 PASS 及其适用限制继续有效；不扩为实际交付接受或完整 M4 重审。作者关系与 MR-02 相同，评价者未代写候选。

### MR-05 · M2 metadata 格式差分

2026-10-01；三个新 SHA-256 实测吻合：`charters/template.md` = `33d1f92edde1389f4c29db363ff69e0a4e59488a83e9e0593e5a302da591ad58`；`examples/implementation-local-fix.md` = `1785cbd1cab2d94a013aee33000855cc2d52da388962a71c6f3c374ed3479ff9`；`examples/implementation-cross-module.md` = `e55e52e002ff89b7cb08e6c52621beb4685b63480bbcd655f27d7770f9e0b304`。实际 diff 仅将 State/Profile/Instance 三行的 Markdown hard-break 改为 metadata bullets；在内存还原格式后，三个摘要分别精确匹配 MR-01 旧对象。**PASS：MR-01 M2 设计 PASS 及原限制继续适用于新摘要，无措辞、claim、授权或独立性变更，无需完整重审。** 只追加本注，未改候选/产品或既有评价。

## MR-06 · M4 product-method candidate 完整新增 claim 检查

2026-10-01；作者/物理集成者 `tpw-night-driver`，来源 dossier 作者 `tpw-night-source`。我此前仅评价 dossier 和差分，未编写或修改这批产品正文；本轮是独立方法检查，只 append 本报告。未介入 M3 fixture、不作 Oracle 的 M4 接受。

### 对象身份

以下固定 SHA-256 实测全部 MATCH，五份产品正文完整读取；对照 MR-02/MR-04、固定 dossier 与此前完整核读的原始正文。为了核对接受状态，仅补读当前 ORACLE-ACCEPTANCE 的接受范围；未扩大来源研究。

| professional-workflow/ 下对象 | SHA-256 |
| --- | --- |
| README.md | `13b376c6316e8d37b54dcc703a5bd3636b06dd7f5fdfaca74c79d490099d0a09` |
| methods/README.md | `c4b24e7c089265b98a44ad6c0c9d5f20fbd2c3b19ff97774c3ebf37f51ea7c35` |
| methods/behavior-claim-evaluation.md | `9d40273309c6407f869d00965f0a6a06200ddd52fdd10f522a7eabf0de8b9697` |
| methods/cross-module-design.md | `90d51699a632a88a01a1b27755ae9d89446469d95a66f71ce852fbfff8321dae` |
| methods/local-defect-feedback-loop.md | `9e7f1107274b9d9aeb008144a10858fe1222c2fb73c83cbd76ec68d903263e8a` |

依据 dossier 摘要仍为 `9e6518449869b02de7089da12ef0ad76bd48361eb9d5594397747cc794ff0ff5`，实测吻合。

### 结论与 claim 覆盖

**PASS：这批固定产品方法的有界蒸馏、责任分工及入口设计无实质方法 blocker。** 保持 candidate；该结论不接受实际任务结果、不代表最终 M4 里程碑接受，也不证明运行依赖闭合/冷启动。可继续串行收口，不增加双评审 gate。

| 新增 claim | 独立判断 |
| --- | --- |
| retain/narrow/strip 从 dossier 落入产品正文 | 支持。局部方法保持已运行的症状专属观察、可复现/最小化、必要时证伪探针、原场景复验与正确 seam；S1 只补分类/不可信输出，S2 未整包采用。没有十种构造法、固定假设数量、控制工具、模型、PR 或跨函数必审规则。未复现时继续取证/返回依赖，不凭日志宣布根因。 |
| 跨模块方法保持责任与局部自由 | 支持。完整 interface、依赖形态/测试接缝、接受 B/C、三部分 Plan 与有限兼容/错误原则相容；测试替代须覆盖既有 claim，且不产生删除授权。未强制深模块合并、helper 规定、REST/幂等或固定多方案/并行实例数量。方法不取得领域、行为或 freshness 决定权。 |
| F 严格三态与独立性相容 | 支持。明确先判比较有效性，再判方向/阈值；测量失败、不可比、缺 baseline 为 UNVERIFIED，有效反证为 FAIL，无明显混淆且满足预测为 PASS。对象/版本/覆盖随结论说明，不把设计观察性、用户价值或 closure 混入单变化 claim。Charter/实际贡献决定独立关系，fresh 仪器和模型标签不充当独立证明，E 自测不能冒充 F 独立结论。 |
| 来源 pins/anchors 可回核 | 支持当前评审范围。三份正文均列固定完整 pin 与仓库相对正文路径，跨模块/F 含章节锚点，内容与已全文核读的原文一致；局部方法的两个短文件按文件锚点可定位。没有 S4/S5 摘要被提升为新证据。 |
| 不新增 applicability obligation 或无用方法堆叠 | 支持。methods/README 是按任务 need 选择，不是固定阶段链；各 Use 是已选方法的适用说明，未宣称 Profile/方法可授予 mandatory trigger。只形成局部修复、跨模块设计、单 claim 评价三种有界正文，备选程序留在处置索引，不常驻叠加。README 不把方法集成当采用接受。 |

### 可选修订（不阻断本次方法 PASS）

1. `cross-module-design.md:33` 的 “accepted source dossier” 不准确：固定 dossier 自称未接受，当前 ORACLE-ACCEPTANCE 仅记 M1。建议改为 “reviewed candidate source dossier”，并给其明确 locator。这一短语不能作为任何接受依据；同文件标题/Status、methods/README 和总 README 都明确候选与待 Oracle 接受，未产生实际自授权或 downstream 采用，因此不把这处引用措辞放大为新 gate。
2. 跨模块 source 表称保留 depth-as-leverage，但工作正文只列 depth 名称，未给短定义；可补“调用者以少量 interface 知识取得的行为能力”，或把该贡献明确为只作来源背景。当前实际设计步骤不依赖未定义的 depth 指标，故不阻断。
3. 最终独立包应带来源 repo locator（不只短 repo 名）、必要处置身份及 Backbone 投影，避免依赖本库过程目录；这是现有 M5/M6 交付工作，不是要求当前候选再造脚本或新索引平台。局部文件也可沿用 MR-02 的章节名降低回源成本。

没有需 Owner 新裁定的方法点。若作者只修上述措辞/定位而不改活跃含义，定向确认差分即可；若改变语义，按既有计划处理对应覆盖，不重开未变 claim。

## MR-07 · M4 方法措辞与回源定位差分

2026-10-01；固定新对象 `methods/cross-module-design.md` SHA-256 `374582907e71b28fa14e4832f39ac89129fca9c69d0cd21d345bf6341bd88679`，`methods/README.md` SHA-256 `72a6ffb46277e3974f27d41e078623ce5b46865074898dae24cbdb6de2205e73`，实测均 MATCH。在内存去掉所申报的定义/状态/locator 增量后，两文件精确重建 MR-06 旧摘要，确认无其他差分；未修改产品。

**PASS，无新增 blocker；MR-06 方法 PASS 与限制继续适用。** depth 的短定义保留 leverage-from-compact-interface，明确不是大小比率；dossier 改称 independently reviewed candidate 并明确不是接受 authority，解决 MR-06 两项可选措辞问题，不声称 M4 已接受。新增三个完整 repo locator 与 pin 均与本地上游实际 origin/HEAD 相符：Matt Pocock `https://github.com/mattpocock/skills.git` / `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`；Addy Osmani `https://github.com/addyosmani/agent-skills.git` / `2686b620fc1fed2e8f60c704839c766b8594c6b6`；Cursor `https://github.com/cursor/plugins.git` / `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`。这是本地固定来源身份核对，未声称远程当前可取回已验证。

README 将 Backbone projection 与脱离过程文件的 source record 明确列为最终 export 待完成项，状态诚实，没有把定位补充当交付闭合证据。该差分不改变触发、授权、独立性或三态，不要求重审 MR-06 全文；候选仍待实际交付接受。独立关系与 MR-06 相同，我未代写候选或介入 fixture；本轮只追加本节。

## MR-08 · M4 metadata 格式差分

2026-10-01；三个新 SHA-256 实测 MATCH：`local-defect-feedback-loop.md` = `3ca23a74a1a1890123bbab01a114aba813d7e20a7ffcb21b7b2289d5047cb32c`；`cross-module-design.md` = `30066c8b3ccee2b85e98c8bc36975f57161e2c93d0bd71c9c668b27bf79bae6f`；`behavior-claim-evaluation.md` = `06b0692290a9ce8cdc7048b33a89ec21f3636ee00138a613121ec4b72457af06`。仅在内存将 Method owner/Status 的 bullets 还原为原 hard-break 格式，三份全文分别精确匹配 MR-06/MR-07 对应旧摘要，确认正文无差分。**PASS：MR-06/MR-07 的方法 PASS 与原限制继续适用，无新增 blocker；此注不构成 M4 接受或全文重审。** 只追加本注，未改产品或读取实现候选。
