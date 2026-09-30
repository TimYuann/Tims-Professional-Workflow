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
