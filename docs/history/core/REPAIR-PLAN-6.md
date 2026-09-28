# 从想法到可实施契约：初始阶段的独立裁决

**状态：方案，未实施。** 已读 `.pi/investigation/TASK-3.md`、现行角色/`pipeline.md`/`SOURCES.md`，及本地上游 `matt/wayfinder`、`grilling`、`to-spec`、`domain-modeling`，`addy/interview-me`、`idea-refine`、`spec-driven-development`，`pstack/figure-it-out`、`create-verification-skill` 原文。`.pi/investigation/FOUR-PARADIGMS.md §4` 与当前 `EVIDENCE.md G10–G11` 已可回核，T3 其它取证仍在进行；不能把尚未取到的“是谁在何提交引入意图文档”猜成事实。本轮只写本文件。Owner 已定：**BDD 本版不引入**；`SOURCES.md` 仅为本库溯源台账、不是下游 B 文档体系；feature map **完整能力要有，但项目可选，Driver/Verifier/Implementer 均不承接其制作维护**；不写 `/tmp`，历史文档只改入口指针、不删不重编。以下直接作判断，不把 Owner 已定项再列成选项。

## 一、初始阶段到底怎么走：是一条有条件分叉的线，不是六份必备文件

**最终判断**：Owner 说的“**获准的规格在计划之前，计划在实施之前**”是正确的依赖顺序，**如果 spec 指本批最小的、已由 Owner 确认的目标/边界/判据，而不强迫每个小改动另造一份 `SPEC.md`**。`addy/spec-driven-development/SKILL.md:24-32,150-153` 明示先 specify 再 plan/tasks/implement，已有规格体系优先；现行 `roles/driver.md §3 task-card`、`architect.md §3 design-proposal`、`planner.md §3 slice-plan` 已有对应接缝。**不能由此推出“feature map 必须在 spec 后、plan 前”**：pstack `create-verification-skill/SKILL.md:11-19,34-40` 是**读已有代码与可运行界面**生成项目内用户路径验证资产，不是从 spec 推导新功能的应然需求。现有产品的 map 可以先于新 spec 帮人看清“今天实际怎样”；新功能在实现前只能在 spec 写**预期入口/验收用例**，不能假装已经 `launch→doctor→drive` 并发布可信 feature map。新行为做出后更新 map 并由独立 Verifier 检查。**两者有用户行为这一交集，但权威方向不同：spec 规定应然；map 给既有/已实现行为的可复验路径。既不冗余，也无普遍的 spec→map 单向依赖。** 另须防同名误导：`addy/spec-driven-development/SKILL.md:34-65` 的 **capability map** 是“多项独立能力的模块/依赖/构建顺序”，在那类项目中反而**先于各模块 spec**；它不是 pstack 的“用户功能如何实际驱动与证明”的 feature map，不能拿它来论证后者必须排在 spec 前或后。

**一条可执行的主线**（`[]` 是按需、不是固定新门）：

```text
Owner 模糊想法
  → [人类沟通面：澄清谁/为什么/成功/边界；跨会话复杂问题才建决策索引]
  → Owner 确认的意图/owner-brief（现有 B 意图文档若有则复用，不并列造第二真源）
  → [领域词或业务关系冲突 → Architect 对照既有词汇表/案例，Owner 裁词义]
  → 本批可判否的获准目标契约：B 的既有 spec 或 task-card 的完整适用字段
  → [改变形状/状态/权限/跨边界 → Architect 的 design-proposal；硬取舍才 ADR]
  → Planner 的 slice-plan（单片无依赖时 Driver 可依法代产完整五字段）
  → Implementer code/测试候选 → 独立 Reviewer/Verifier → Integrator → roundup
                    ↘ 已实际可驱动的功能更新/核验 feature map；发现合同冲突回 Owner
```

**已有产品的条件旁路**：从现有代码/入口可先形成**现状 map**，用它给澄清/规格/测试接缝提供事实，但 Owner 未接受的现状**不是规格或授权**；已存在 map 可供 Planner/Verifier 定位受影响入口。**新项目无可运行产品**：spec→plan→code 后才有“可驱动、已自证”map；若实施前需规划覆盖，在 spec/`slice-plan.verification` 列出预期用户路径即可，不把该列表冒充 feature map。Feature map 不建立仍可按本批判据开发/验证，符合 Owner 先前裁决。

**几个易错环节的确切落点**：
- `grill` 的产出不是一个天生存在的“决策卡”新收据。短访谈由**同一份获准 `owner-brief`** 的 `goal/scope/success_signal/authorization` 承接；多会话、多个相依问题，才在 B 的现有 tracker 建 **wayfinder 式决策索引（索引指向各决定，不复制内容）**，最后把被接受的结论链接进该 brief。`matt/wayfinder/SKILL.md:9-13,21-23` 要**先有 destination**；“完全不知道想要什么”先谈用户/结果，不会因雾大就先开票据工厂。
- 项目若长期需要“意图文档”，由下节的人类沟通角色**起草于 B 已有位置**，Owner 确认后作为项目层目标源；Driver 仍收**Owner 出具/确认的 `owner-brief`**，不把草稿当授权。仅本批任务可直接写已有 brief/卡，**不强制意图文档、规格、词汇表三份同义副本**。当前 `roles/driver.md §4.1` 确有 frontier 提问并产 task-card；旧 `docs/archive/skills/decision-grilling/SKILL.md:34` 的“决策卡”是历史做法，不能算当前 A 缺漏的主链收据。`addy/interview-me/SKILL.md:142-146` 的 `docs/intent/` 是**经用户同意才保存**的外部例子，本库当前没有此默认路径。
- 词汇表/上下文只在共享领域语义有歧义时，由 `Architect §4.9` 提供对照和备选、**Owner/授权业务人裁定**后落 B 已有权威文档；没词可定就不造 glossary。ADR 是 Architect 对**难回退+无上下文难懂+确有真实取舍**才建议的决策记录，通常伴设计比较，不能插成每批必经的“spec 前文件”；新证据出现后可经授权修订词义/规格并触发受影响片重判。**这些也可能在实施后再出现**，故“全部方法只能在 implement 之前发生一次”过于绝对。

## 二、一条有机的 ideation 方法：从用户结果与真实约束一起收敛，而非拼三份模板

**名字：`事实—意图—区分—确认`，按一个未定的问题循环，最终只固定一份 Owner 接受的意图/契约。** 推荐由下节人类沟通面承担长/难 ideation；Driver 现有 `§4.1` 仍负责每批必要的授权/目标核对，不因此塞进所有项目的访谈上下文。

1. **先定要走向什么（粗目的）并查现场**：用用户/受益者/为什么现在/成功读数/不做什么写一句可反驳的意图假设；先读 B 现有需求与代码现状、历史约束，证据和想象分栏。目的还说不出时与 Owner 对话，**不建立 wayfinder 决策地图**。这是把 addy `interview-me:40-52,94-111` 的“带猜测问、复述用户话”与 pstack `figure-it-out:19-23` 的“可判完成、范围、代价”放在**同一个目标句**，不是先按 95% 数字问完再另开规划工作流。
2. **辨别是事实空白、价值分叉还是结构分叉**：事实由角色自行取证；价值/业务正确答案才向 Owner 问；多个互斥方向时给**能改变结论的对照**（保留现状/一个最小可行方向/必要时第二个结构不同方案），用一条用户场景或便宜实验区分。**不按 addy `idea-refine` 固定造 5–8 个方案，也不按 pstack 将每个想法都膨胀成多阶段程序。** 事实查不清可注明未知与风险，不能写“已决定”。
3. **仅让可回答的依赖决策进入当前轮**：一轮一个前沿问题或一小组**互不依赖**的问题，每问附工作假设与证据/后果，Owner 回答后重算；尚不能准确表述的记“待细化”，不让受阻分支挡住无依赖调查。这取 matt `grilling/SKILL.md:6-28` 的 frontier；**只有跨多会话、多个依赖决定**才借 wayfinder 的 destination/index/票据，不把每次聊天都票据化。
4. **在原位固化与停止**：把已确认的结果、可观察成功/判否、边界、排除项、未决/前提、批准原文与生效对象写入 B 的**同一权威意图/brief**；复杂项目可让决策索引只指向此处。人类明确确认后交 Driver→spec/卡；没有确认，保持草稿，继续只读澄清/不依赖的调查，**不得让 Implementer 拿草稿开写窗**。能否用具体反例区分“符合意图”和“看起来像但不是”、能否指出谁批准，是停止发问的读数；不是“问满四题/置信度 95%”的仪式。

**为何是有机改写而非三仓拼接**：三种手段分别只在一个**共同的未定意图**上工作：pstack 贡献“值不值得开始的可证伪结果/代价”，addy 贡献“用户真实要什么、反驳猜想与排除项”，matt 贡献“决定的依赖顺序”；其共同**权威输出仅是 Owner 接受的目标+边界+成功判据**。删掉上游各自独占的包装：pstack 的长跑待办/多会话默认、addy 固定变体数与默认 `docs/ideas/`、matt 每个疑问都进 tracker。冲突处单选本库既有门：Owner 负责业务/授权，Driver 负责批次交接；不能拿 pstack“可逆先做”跨越当前授权门。**上游这三种原文不曾合成过 TIM 这条线，这是本库拟新增的方法，应在实现时于 `SOURCES.md` 登记“改写了什么”，不能标为三仓已有。**

## 三、feature map：明确要装；消费者与归属要与它的事实性质一致

**结论：作为完整的**项目验证资产能力**装入库，项目上仍按 Driver 建议/Owner 授权决定是否建；它不属于 spec/意图层，属于 B 的**可维护的用户路径验证资产层**（靠近项目已有 test/harness，不复制成产品规格）。** pstack `create-verification-skill/SKILL.md:9,11-19,25-44` 原文“写给下一位从未见过 app 的 agent”、“访谈代码库、不是用户”、“`features/README.md`＋每功能文件”，典型消费者是下一位冷启动的验证 agent、维护该验证资产的 agent，以及按功能分配验证的协调者；人可读索引但不以它作为业务决定者。它的收益是让“验证这个功能”有明确入口、前提、动作、可观察状态/副作用、覆盖和清理，减少同一好走入口冒充全功能验证；**不能用它证明产品未来应该实现什么，也不因跑通 map 就证明与 Owner spec 一致**。完整能力包括生成（先现场访谈→map→至少一个功能实跑、cleanup 后证据仍在）和维护（入口/代码变化→核索引、读真实源→真实驱动→区分文档漂移/产品回归→`clean/changed/blocked`），遵守 `maintain-verification-skill/SKILL.md:9-37`。无现存 app 时只能标草稿/待实跑；不设 map 缺失的通用开工停机门。

**承接角色的正面裁决：新增一个按需 `Discovery/Mapping`（拟名 `roles/discovery.md`）会话/角色，只有这一种扩角色是有必要的。** Owner 已明确否决 Driver、Verifier、Implementer 作为 map **制作维护者**。现有其余角色也无合适的常驻写权与使命：`Planner` 只把规格分切片；`Architect` 设计边界与领域模型（可给场景，非既有产品用户路径资产维护）；`Investigator` 对已发生症状构造复现；`Integrator` 只写目标基线；`Oracle` §2 必须收到**已冻结 `pending-question`**、独立裁一争议，**不是**帮 Owner 发现尚未定义的业务答案或维护长期验证地图；`Ledger Custodian` 只维护本库 `SOURCES`。把 map 强塞其一会扩错权限且破坏角色自包含。新增 role/session 经 Driver 按需启用，**不自动计入 `solo/trio/full`**，不变成所有任务前置。

**它只做两类相邻工作**：① 与人澄清模糊意图、起草已有 B 意图/`owner-brief` 内容；**Owner 确认才是 owner-brief 原产者**，新角色不得代签、不得凭谈话给项目业务含义定案；复杂依赖决策可维护 B 的单写者索引。② 在有可观察产品且项目经授权建立 map 时，**读项目现状、写/维护 B 的项目自有 map/harness 说明**，明确现状/期望分栏；如果期望语义不明，请 Owner/Architect/Planner 解，不用源码当业务授权。它不能写产品实现、不能对自己写的 map 出独立 PASS；Reviewer/Verifier 仍可用已有反实现挑战/真实入口对 map 做独立资格检查，再用于放行。若 Owner 指定同一人既写 map 又作其唯一合格性判定，该结论 `UNVERIFIED`。

**最小接线**（既有主链收据不替换）：Owner 模糊 idea→Driver 可启动 Discovery/Mapping 会话，向它只给允许调研/写意图草稿的 scope；会话将**草稿和未决项**在 B 已授权位置给 Owner，Owner 亲自确认并出 `owner-brief`→现行 `Driver` 入口。map 是**项目验证资产**，建立/维护有单独授权的 B 写窗；其结果指针由现有 `task-card.verification`、`slice-plan.verification`、`verification-evidence.commands/uncovered` 消费，不新设“没 map 就停”的主链门。这个角色必然需要一份自包含 `roles/discovery.md` 与一个**可选前奏/反馈边**在 `pipeline.md/closure.md` 中声明（否则 checker 收件/产出形状会不一致），但**不新造能替 Owner 授权的 `owner-brief`**；起草与正式批文身份必须分开。项目 B 已有特定地图/意图位置就复用，没位置由 Owner 授权最小位置；不照搬 `.cursor/` 路径。

## 四、SDD 的现状与应负责的人：不是零，但缺“被接受的意图→规格”的显式归口

**判 Driver 的“现在没有任何角色负责它，所以是空位”——整体上不对；若特指项目长期意图/完整规格的单一维护者，则有真缺口。** 当前不是已吸纳 addy SDD：`SOURCES.md:253` 明记当轮**未读全文/NOT ABSORBED**，不能回填成早已采纳。但 TIM **自己已实质实施 spec-first 链的一部分**：`Driver §3` 产带目标/授权/判据的 `task-card`，`Architect §3` 的 `design-proposal.bound_contract` 固定设计契约（**它不是完整产品规格**），`Planner §3` 的 `slice-plan` 给实施顺序与判据，`pipeline.md §6/§9` 对对象冻结与汇合，`closure.md` 守适用收据。此相似不证明 Addy 方法被吸收；也不能把“没有叫 SPEC.md 的文件”当“没有前置契约”。

**建议最终责任**：Owner/明确授权业务人 **唯一决定**该做什么；新 Discovery/Mapping 角色**访谈并起草/维护项目 B 的意图与重大特性规格草稿**（如果本项目需要长期规格），不得自批；**Driver 是本批规格适用性/授权与从 Owner 确认规格→task-card 的交接责任人**，不当产品规格作者；Architect 负责适用的 how/边界设计与词义核查；Planner 负责规格→可验证片；Implementer 在冻结片内实施，独立 Reviewer/Verifier/Integrator 核对象与合同。这是**分段责任而非一个角色包办 SDD**。单个简单任务不强制独立长期 spec 文件，但不能缺 Owner 确认的目标、范围与可判否验收；大型多功能工作，草稿 spec → Owner 同意 → B 的唯一权威规格位置 → 设计/plan，具体 SDD 活文档程度由该项目 Owner 确认。

**账本另外修，不混入文档体系**：`SOURCES.md:253` 同时表达“当时未读正文”与“当时不登记为已吸收”；它是**来源处置的历史事实**，不能因看到本库有相似载体就把旧行改成“当时已吸收”。Driver 所说“账本只登记阅读行为、不登记生效方法”**只说对一半**：既有 §1–3 的 `保留/改写/落点` 本来就在登记生效方法，`render-ledger.py` 又能把 key 锚到角色实际原文；但仅结构命中不证明语义真正一致，也没有给“**本库自主形成的 spec-first 方法与尚未读取的上游 SDD 恰巧相似**”一条清楚的 provenance 类别。发现账实错位就即时列 repair：由 Ledger Custodian 对照源码与原意做 §4.9 的语义回读，Owner/维护者决定新增当前有效机制记录及来源，读过上游正文后才能决定是“后续新吸收/改写/仍不吸收”；**保留原 NOT ABSORBED 历史事实，不把阅读状态粉饰成旧版已吸收**。这件事属于本库维护，不要求下游 B 也建 `SOURCES.md`。

## 五、模拟推演：应进库，但只针对流程改造的前置设计检查

**正面判断：应该成为 Driver 在**新增/改变角色、交接边、判据或前置阶段**时的检查方法；不是每个普通任务新增一次全角色演练。** Owner 指出“改造流程前先模拟，再用真实任务验证”是实际根因防线：纸面角色链还没跑通时启动全会话实测，遇到缺件会产生假成功或沉没成本。反过来模拟推演只是**预测**，不能替代真正的角色冷启动/独立行为检验。

**落点**：`roles/driver.md §4.3`（风险/装配之后加本方法的**条件触发**；Driver 负责组织，不给本人作品出独立 PASS），如是具体工作流改造，场景轨迹写在**现有 `task-card.verification/dependencies/escalation` 或 `design-proposal` 的依据段**，随当前任务长期可取回；`pipeline.md` 至多在“发首卡前”注明先核适用的模拟轨迹，**不添加新主收据或常驻总控层**。库维护者修改核心拓扑时应将轨迹指向本批修订对象，并请独立 Reviewer 质疑其假设。

**可用方法正文**：
> 只在**新增/重排实际交接、角色写权、某方法的启动条件/退出判据**时，先用一个具体用户想法在纸上走通：“输入从谁来→谁确认目标/授权→每个被触发的角色收到哪些现有字段与路径→本轮会写什么→谁接收/谁独立判断→实现后怎么收口”。至少再走一个**会否造成越权或假绿**的反例（Owner 尚未确认 spec、map 不存在但任务可行、候选/证据缺失或 B 映射读不到），并对停机后重入写清下一接手人与旧结论效力；对两轮审查/同前提重复失败等已有上限，只按**各自的事件类型**模拟，不造统一轮次表。每一步写“依据现有哪份角色 §2/§3 或 B 位置”；走不通的边标未设计，不先用现实团队给它打补丁。模拟能在现有批准下闭环后，才以**最小独立冷启动**挑战其关键未知，失败回修规则再复试；不要求真的先开九角色长跑。纯局部代码变动、既有链未变时直接按正常任务验证，不重复推演。

**判否**：拿模糊 idea 推至 `slice-plan`，若 `owner-brief.success_signal` 未获 Owner 确认却能开 Implementer → 模拟红；新功能尚未运行却图谱被写成已验证 → 模拟红；map 缺失导致全部代码修改停机 → 模拟红；审查者产自己判据又给自己发 PASS → 模拟红。修正轨迹后可做一次**独立**小型冷启动验证，但 checker 结构绿与模拟自述均不能算实际流程已可靠。

## 六、后续真正要改的地方（方案不是实施）

| 文件/位置 | 拟改 | 实际验收与影响 |
|---|---|---|
| `roles/driver.md §4.1/§4.3`、`README.md` 注入/目录简介 | 把长模糊项目的专门 human session 触发交给 Driver，Driver 仍保留必要 Owner 授权/派卡核对；发新工作流第一张卡前按上节桌面推演；README 用一句话区分目标澄清和项目现状 map，**不把全量 ideation 又复制进 Driver**。 | 没触发时小任务正常发卡；触发时 Driver 不把未经 Owner 确认的草稿当授权。影响 Driver/Owner；库内方法出处要登记为本库对三仓机制的主动改写。 |
| **新增 `roles/discovery.md`**（需 Owner 同意新增角色及项目 B 写权后实施），`pipeline.md §1/§11` 可选前奏、`closure.md` 按需接线与 `check-library.py` 角色/闭环登记 | 角色全文自包含：接受 Owner idea+Driver 的范围限制、按**事实—意图—区分—确认**访谈，写项目 B 意图/规格草稿与经授权的**现状** feature map、给 Owner/Driver 的指针，明确草稿非批文、地图非 spec、无产品实现/自证通过权；项目行为变化后受授权可维护地图，留变更依据。项目里若已有相同文档先映射，不新建第二真源。**Owner 正式出 `owner-brief`** 后原主链才启动，避免新角色变成影子 Owner。 | 单文件注入角色在没有额外 skill 情况下能解释自己何时停/怎么做；有 Owner 确认能冷启动发卡、只有草稿则不开写窗；map 审查者与地图作者不同；缺 map 不挡普通开发。新角色若正式进入库要重新盘 README 的角色数与档位口径（当前 `full(9)` 数量矛盾已见 `REPAIR-PLAN-4.md`），不能偷偷记成既有九角色。 |
| `roles/architect.md §4.9`、`roles/planner.md §4.4–4.6`、`roles/verifier.md §4.2` 与 B 映射记录 | 只补衔接句：“先消费已接受的目标与已裁词义，设计提案/切片的判据不能拿现状 map 替代规格；map 提供既有入口/验证驱动线索，Verifier 独立检查实际加载对象、覆盖与漂移”。Owner 未裁领域意义继续挂起。 | 做两道反例：旧代码现状与 Owner 新 spec 冲突，不允许拿 map 改写业务目标；实现后地图新增入口未验证不得写 clean。只影响适用角色，不增加每次任务统一环节。 |
| `SOURCES.md`（**仅本库维护记账，与项目 B 文档体系分开**） | 把新阅读的上游出处与“新融合方法”分开登记；对历史 NOT ABSORBED 不追认旧版；发现已失效的 key/过宽处置按 Ledger Custodian §4.9 查清再修当前记录。BDD 本版不进任何角色/流程（研究文件可存档）。 | `render-ledger.py --check` 只证生成区、独立人核“出处原文支持当前方法”才得语义结论；下游普通任务无需 SOURCES。影响库维护者而非产品 Owner 的 B 文档体系。 |

**仍需 Owner 唯一明确的授权**：① 新 `Discovery/Mapping` 角色及其与人对谈/项目写入范围、能否在某既有 B 文档长期保存意图和 map；② 项目何时把草稿 spec 固化为长期产品真源（只对长期产品有必要，当前批已可用 Owner-approved brief）；③ 新角色是否占用既有 `solo/trio/full` 数字档位（**建议按需另列，既有 `full(9)` 先校准，不擅改数**）。Owner 已决定的“不用 BDD”“feature map 要有完整能力但项目可选”“Driver/Verifier/Implementer 不写 map”“历史不改写”不再重问。
