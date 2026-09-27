# T3-1 / T3-2 · 追责链条 与 "implement 之前"角色承接

**范围**：只做 TASK-3 的第一部分（T3-1、T3-2）。T3-3/4/5 属 tim-investigator-b。
**方法**：`git` 取证 + 现行工作树 + 各轮 `.pi/**` 任务与报告三方对照。**不改任何产物**。

## 0. 取证前提（先说清，避免把"未提交"错记成"没发生"）

| 事实 | 值 | 影响 |
|---|---|---|
| `HEAD` | `52d3315 chore: sanitize absolute file paths to relative markdown links` | 只含 proposal 与**第一版 9 角色 + 8 skill** 的状态 |
| 已跟踪文件 | 28 个（`git ls-files \| wc -l`）：proposal、8 个归档 skill、3 个旧 workflow、`roles/{architect,driver,implementer,integrator,investigator,oracle,planner,reviewer,verifier}.md`、`scripts/{check-team-version,sync-upstreams}.sh` | **`pipeline.md` / `closure.md` / `identity.md` / `SOURCES.md` / `roles/ledger-custodian.md` 全部未跟踪**；`roles/*.md` 有未提交改动 |
| 关键结论 | **现行角色文本里没有对应的 commit**；"谁放进去的"必须用**轮次产物**（`.pi/round1`、`.pi/core`、`.pi/repair`）回答，SHA 只能追到**上一版** | 表格里"谁引入"一栏分三种写法：`SHA`（已提交）、`轮次+文件`（未提交）、`既有+轮次` |

**三源对照用到的文件**：
`.pi/round1/TASK.md`、`.pi/round1/decisions.tsv`、`.pi/round1/REPORT.md`；`.pi/core/TASK.md`、`.pi/core/PLAN.md`、`.pi/core/ORACLE-REVIEW.md`、`.pi/core/REPAIR-PLAN*.md`、`.pi/core/OPEN-ITEMS.md`；`.pi/repair/REPORT.md`；`SOURCES.md`；`docs/TIM-PROFESSIONAL-WORKFLOW-PROPOSAL.md`；`docs/archive/skills/decision-grilling/SKILL.md`。

---

## T3-1 · 追击表

> 读法：**"在不在"→"谁引入"→"有没有产出物"→"为什么没进 24 项"**。"无产出物规定"是明确结论，不是没查到。

| 词/概念 | 在哪个文件:行（现行/相关） | 谁引入（SHA / 轮次） | 有没有产出物规定 | 为什么没进 24 项 |
|---|---|---|---|---|
| **意图文档** | `docs/TIM-PROFESSIONAL-WORKFLOW-PROPOSAL.md:112`：「Oracle 的职责：阅读项目的**长期意图文档**（`CONTEXT.md`、产品定位、用户偏好）…」；**现行 `roles/`+`pipeline.md`+`closure.md` 零命中** | **`5b41cd4`**（proposal v1.0-final；`git log -S"意图文档"` 首次出现即此 commit）。引入时的意图：commit message「incorporating GPT-6 Pro review and **Owner operational directives**」——即"按 Owner 指令把 Oracle 定位写进提案" | **无产出物规定**：该句只规定 Oracle"**读**"这份文档，**没写谁产它、在哪、交给谁**；它被描述为项目既有物（CONTEXT.md/产品定位/用户偏好），不是本库产物 | **它从来不是 workflow 产物**：无产出方、无环节、无消费者交接；现行库连这个词都没有（Oracle 现行 §4.2 只读"产物与冻结契约"，`roles/oracle.md:74-84`）。→ 漏不在统计，在**从未有产出物** |
| **"需求与意图对齐"（能力名）** | `docs/…PROPOSAL.md:181`：「`matt/grilling` + `addy/interview-me` → **`decision-grilling`** … 输出决策卡」 | 同上 `5b41cd4` | 有：指定输出**决策卡** | 该能力名随 proposal 进入归档；其实体的产物（决策卡）另见下一行 |
| **决策卡 / Decision Record** | `a9a709d:docs/…PROPOSAL.md:158`「**产出物**：生成结构化决策卡（Decision Record），记录已确认事实、人类拍板结论与已排除选项」；`5b41cd4:…:183`；实现件 `docs/archive/skills/decision-grilling/SKILL.md:3`（description"输出结构化决策卡"）、`:32-34`（步骤 4：决策卡固化）、`:50`（退出判据："产出结构化决策卡，包含已冻结的硬契约与边界"） | **`a9a709d` 提出**（proposal 初版）；**`5b41cd4` 并入 v1.0-final**；**`e053963` 实现为 skill**（commit message"complete implementation of 9 core roles, **8 core skills**"） | **曾经有**：产出结构化决策卡，退出判据明确（archive `:50`） | **在折叠轮被丢**：`e053963` 时 `roles/driver.md` 只是**指针**（`git show HEAD:roles/driver.md:57`「`skills/decision-grilling/SKILL.md`（对齐与决策 frontier 推进）」）；`.pi/round1` 取消 skill 载体后，Driver 只保留了**提问方法**（现行 `roles/driver.md:143-155`），**决策卡这个产物没有任何角色 §3 承接** → 故 24 项里没有 |
| **grill / grilling** | 现行：`roles/driver.md:143-155`（§4.1）；登记：`SOURCES.md:152-155`（来源 matt `skills/productivity/grilling/SKILL.md:6,8…`；落点栏 `@把待定事项画成决策树…`） | **折叠轮 `.pi/round1`**（未提交）：`.pi/round1/TASK.md:112`「Driver \| **意图对齐与提问**、任务分级与依赖分类… \| matt `grilling`；addy `interview-me`」；决策行 `.pi/round1/decisions.tsv`「按 Owner 决定取消 skills/ 载体，经验写进 roles/*.md」 | **无产出物规定**：现行 §4.1 六步全是"怎么问"（画树→算 frontier→带推荐答案→事实自查→frontier 清空才开工→交叉提示），**没有一句说产出什么、交给谁** | **吸收样式的副作用**：把"技能（有退出判据+产物）"改写成"方法节（只有动作）"时，产物被抹掉；问出来的东西**隐式落进 task-card 的 `goal`/`scope`/`success_signal`/`authorization` 字段**（SET-A #2），所以统计上只看到 task-card。**这是"被吸收的写法让它不再产生东西"的实证** |
| **frontier** | 现行 `roles/driver.md:149`、`:152`、`:155`；`docs/archive/skills/decision-grilling/SKILL.md:3`、`:14` | 同折叠轮；概念源自 matt `grilling`（`SOURCES.md:152`「决策树 + frontier：只问前置已定的决定」） | 同上：**无产出物规定**（方法） | 方法不是产物；其最近产物是 task-card 字段与"该批决策记录"（后者是 SET-A #20/异常 E1-4，**无环节**） |
| **interview-me（addy）** | `SOURCES.md:228-231`（假设+置信度→`roles/driver.md:150` 第 3 步）、`:279`（"明确的'是'才算确认"→授权门裁决：`SOURCES.md` §4.2，"范围与授权必须阻塞到明确确认"） | 折叠轮 `.pi/round1`（TASK.md:112 列为 Driver 的第二上游） | **无产出物规定**（两个片段都并入提问/确认方法） | 同上；确认门的产出（授权）落在 task-card `authorization`/`auth_record`（SET-A #2/#18） |
| **词汇表 / glossary** | 现行 `roles/architect.md:203`（触发条件）、`:206`、`:209`（裁定权）、`:210`（"被授权的裁定落到项目既有词汇表/契约…Architect 是默认**写者**"）、`:211`（ADR 三条件）；另 4 处联动：`investigator.md:95`、`reviewer.md:141`、`planner.md:107`、`implementer.md:99` | **上游** matt `domain-modeling`（`SOURCES.md:180`，处置"局部吸收（改写）"）；**引入链**：`.pi/core/TASK.md:31-33`（C2 认定"术语/领域事实归属零 owner"，并自认"R1 时是挂在 architect 名下的**死链**，重写时没补回来"）→ `.pi/core/PLAN.md:222-230`（起草 §4.9 文本）→ `.pi/core/ORACLE-REVIEW.md:12`（裁定"术语写者≠术语决定者"）→ Owner D3（`SOURCES.md:180`"Owner D3，2026-09-26"）→ **`.pi/repair/REPORT.md:27`（R6 实施）**，全部**未提交** | **有产出物**（且是本批唯一明确有写者的）："记录裁定结果"`architect.md:209` + "落到项目既有词汇表/契约"`:210` + ADR `:211` | **进了 24 项但只以项目侧文档出现**：SET-A #22「项目词汇表/ADR 更新」被列为**无产出环节**（异常表 1 的 E1-6）。原因：§4.9 是方法节，**roles 的 §3 产物里没有它**，pipeline 也没有它的环节 → 它没有"被算进别项"，而是**被收成了一个没有环节的独立项** |
| **ADR** | 现行 `roles/architect.md:206`、`:211`；proposal `:162`（旧映射示意"TIM 决策卡 ──▶ CONTEXT.md / ADR"） | 同"词汇表"链（同一节 §4.9） | 有："难回退、无上下文难懂、存在真实取舍"三条齐才**建议**（`:211`），落在项目既有文档 | 同 #22；在 24 项里与词汇表合并计为一项 |
| **wayfinder** | 全库零命中（`roles/`+`pipeline.md`+`closure.md`+`docs/archive/**`）；SOURCES 里只有 **NOT ABSORBED** 登记：`SOURCES.md:183`（"`wayfinder`… [仅目录] \| 未读全文 \| **NOT ABSORBED**"） | 未引入 | 未引入（上游 matt `wayfinder` 有产出：map/decision tickets；本库无对应物） | **从未是产物**；`.pi/core/OPEN-ITEMS.md:42` 记着 Owner 点名的 C7"`grill` 现在归哪个角色 \| **未开始**" |
| **grill-me / grill-with-docs** | 三处零命中（现行角色、pipeline、closure）；`SOURCES.md:183` 的 NOT ABSORBED 名单含 `grill-with-docs`；**`grill-me` 连 SOURCES 都没登记**（`grep "grill-me" SOURCES.md` 无命中） | 未引入 | 未引入 | 从未是产物；属"未读全文、不登记"的一类（`SOURCES.md:183` 的纪律："没有读过正文就不登记为已吸收"） |
| **ideation / discovery** | 全库零命中（含 archive 8 个 skill） | 未引入 | 未引入 | — |
| **intent（英文）** | 零命中 | — | — | — |
| **"意图"（作为词，非文档）** | `roles/integrator.md:97`「冲突消解：按**意图**，不能同时满足就停」、`:104`、`:107`、`:210`；`roles/investigator.md:12`「历史**意图**」、`:104`（§4.4 历史意图考古）、`:113` | 现行文本；integrator 用法源自 `SOURCES.md:85+`（resolving-merge-conflicts 的吸收，§4.7 裁决）；investigator 用法源自 pstack `why`（`SOURCES.md:257` 段） | **无产出物规定**：integrator 的意图写进 `conflicts` 字段（SET-A #11）；investigator 的意图写进 `root_cause`/`not_proven`（SET-A #5） | 两者都是**字段/方法**，不是文档类型 → 不构成 A 项 |

### 补充事实（为什么"24 项里没有 grill 产物"

`.pi/core/OPEN-ITEMS.md:40-42` 把这条记成 **C5/C7**：
- `:40`「C5 \| 建立过程 \| 已定 \| **与 `grill` 很相似**（对话式、按 frontier 推进）」——即 Owner 已把"feature map 的建立过程"定为 grill 式；
- `:42`「C7 \| **`grill` 现在归哪个角色** \| **未开始** \| Owner 点名要查」——**本文件即对该条的第一份证据**。

---

## T3-2 · "implement 之前"的动作 × 10 角色

**动作清单的来源**：现行角色 §4 方法节 + `pipeline.md` 环节 + `.pi/core/TASK.md` 的 C1/C2 + `SOURCES.md` 的未吸收登记。**不照抄任何一张已给的表**。
状态定义：**有承接**（角色文件里有可执行的方法且写明产出/交接）｜**部分**（有方法但无产物/无环节/只在触发条件下动作）｜**无承接**（全库无人负责）。

| # | implement 之前的动作 | 承接者 | 状态 | 证据 | 空位说明 |
|---|---|---|---|---|---|
| P1 | **事实自查**（能从代码/配置/历史查到的事实，不问人） | Driver | **有** | `roles/driver.md:151` 第 4 步「**事实我自己查，不向 Owner 要**；只有决定交给 Owner」；`SOURCES.md:155`（来源 matt grilling `:26`） | — |
| P2 | **目标对齐与提问**（决策树 / frontier / 分轮 / 带推荐答案 / 明确 YES） | Driver | **有**（方法完备） | `roles/driver.md:143-155`（§4.1 六步）；`SOURCES.md:152-155`、`:228-231`、`:279` | 产出物缺：问出的结论只隐式进 `task-card` 字段，无独立记录（见 T3-1） |
| P3 | **授权、范围与"不做什么"** | Owner → Driver | **有** | `roles/driver.md:58-70`（task-card 的 `scope`/`authorization`/`auth_record`）；`pipeline.md:120-128`（§10 授权检查） | — |
| P4 | **把"要做什么/代价/不做"在动手前讲清**（implement 前硬线） | Driver | **有** | `roles/driver.md:285-294`（§4.9；`.pi/repair/REPORT.md:22` R1 实施；`pipeline.md:127`） | 记录：仅当"Driver 由 Owner 本人承载"才写入决策记录（`:292`） |
| P5 | **定"什么算对"（验收判据、可判否）** | Driver → Planner | **有** | `roles/driver.md:68`（`verification` 字段）；`roles/planner.md:136-153`（§4.6 验证位置与最小验证） | — |
| P6 | **定边界/接口/不变量（含"不改"对照）** | Architect | **有** | `roles/architect.md:82-98`（§4.2 调用者用法先于类型）、`:99-117`（§4.3 数据形状与不变量）、`:118-135`（§4.4 至少两个候选+不改对照）、§3 `bound_contract` | — |
| P7 | **切片、依赖排序、停止条件** | Planner | **有** | `roles/planner.md:49-65`（§4.1 垂直切片）、`:66-82`（§4.2 依赖图）、`:154-169`（§4.7 停止条件） | — |
| P8 | **冻结写窗与交权** | Driver | **有** | `pipeline.md:88-93`（§6 写窗）；`roles/driver.md:200-208`（§4.4） | — |
| P9 | **产品取舍/风险接受**（谁拍板） | Owner（外部）；Oracle 只在冻结契约内裁 | **有**（但不在 10 角色内） | `roles/driver.md:304`「我不可以：替 Owner 决定产品目标、范围取舍与风险接受」；`roles/oracle.md:196`（同义禁令）；`pipeline.md:120-127` | 工程角色**按设计不承接**；Oracle 也不产生 Owner 权限（`closure.md:18`） |
| P10 | **术语/领域词义裁定与落点** | Architect（查证/备选/记录）+ Owner/授权业务角色（裁定） | **部分**（本表最大 gap 之一） | `roles/architect.md:201-217`（§4.9）；触发条件是**冲突时**（`:203`「一个词在 Owner 说法、代码行为、词汇表/契约之间冲突」）——**没有"开工前读项目词汇表"的动作**；产物落点是**项目侧文档**，不是本库收据/环节（SET-A #22、异常 E1-6） | ① 无"开工前读"；② 产出物未进 §3/环节；③ 下游项目没有词汇表时，新建需 Owner 同意（`:210`） |
| P11 | **长期意图/意图文档（产品定位、用户偏好、"为什么做这个"）** | **无承接者** | **无** | 全库唯一出处 `docs/…PROPOSAL.md:112`（Oracle 阅读"长期意图文档"）；现行 `roles/oracle.md:74-84`（§4.2）把输入限定为"产物 + 冻结契约"，**不读长期意图**；10 角色 §3 无它的产物 | **Owner 说的巨大 gap 成立**：既无人读、也无人产、也无落点；proposal 默认"项目已有"，但本库没有"没有时怎么办" |
| P12 | **从模糊想法到可开工（ideation / discovery）** | **无承接者** | **无** | `SOURCES.md:183`（`wayfinder`、`prototype`、`research` 等 **NOT ABSORBED**）；`roles/*.md` 无对应节；`.pi/core/OPEN-ITEMS.md:42`（C7"grill 归哪个角色"**未开始**） | 三仓各有方法（matt wayfinder / addy interview-me+idea-refine / pstack figure-it-out），本库**只有 grill 的提问片段**，没有"idea → 可开工"的完整路径 |
| P13 | **领域上下文边界（同名异义、多上下文）** | 无（Architect 只在术语冲突时处理单词） | **部分/条件缺失** | `roles/architect.md:201-217`（只处理"一个词冲突"，无上下文/边界概念）；`.pi/core/REPAIR-PLAN-3.md:23`（A7："条件缺口，不是所有项目必备…多领域同名异义才需要显式边界"） | 单上下文项目不需要；多上下文时无承接 |
| P14 | **环境/运行条件就绪（能跑起来才能实现/验证）** | 无专职；Verifier/Investigator 只能"要资源"，Driver 分流 | **部分** | `.pi/core/TASK.md:27-33`（C1 标题在 `:27`、原文"**没有修环境**"在 `:28`；证据列 investigator §6 / verifier §6 / driver §5；C2 在 `:31-33`）；补丁：`.pi/repair/REPORT.md:24`（R3：Verifier §4.1 自建前提 + `roles/driver.md:171` 分流"仓库内可修→实现者；能力缺失→Owner"） | 仍是**分流**而非 owner；"仓库内可修"由 Implementer 做，但那是实现环，不在 implement 之前 |
| P15 | **过程记录/决策留痕（批次级）** | Driver（`该批决策记录`）+ 各执行者（决策台账） | **部分** | `roles/driver.md:292`（Driver=Owner 时写入）、`roles/verifier.md:207-217`（§4.8 决策台账：形态+只追加）；SET-A #20/#21（异常 E1-4/E1-5：**无环节、无路径**） | 有形态、无落点/无环节/无保管人 |
| P16 | **用户可见行为索引（feature map 类）** | **已定不在 10 角色内**：新开"人类沟通面" session | **无（十角色内）；Owner 已定向** | `.pi/core/OPEN-ITEMS.md:37`（C2"**不由 Driver 承接**"）、`:38`（C3"可以新开一个 session…**否掉 Implementer，也否掉 Verifier**"）、`:16`（A4"职责=人类沟通面"）、`:13`（A1"正确形态：约 8 类，不是 24 项"） | 十角色表里的空位；按 Owner 决定由表外角色承接 |
| P17 | **入口优先级/backlog triage（先做哪件）** | 无 | **无** | `SOURCES.md:183`（matt `triage` NOT ABSORBED）；`pipeline.md` 无对应环节 | 是否属本库范围未定（`.pi/core/OPEN-ITEMS.md` 无该条） |
| P18 | **规格层（spec：what/why 的独立产物与生命周期）** | 无独立产物；由 task-card + design-proposal 承载 | **部分** | `SOURCES.md:253`（addy `spec-driven-development` **NOT ABSORBED**）；`.pi/core/REPAIR-PLAN-3.md:109`（D3 推荐"默认保持按风险的 spec-first（不升格永久 SPEC）"）；`roles/architect.md` §3 `bound_contract` | 有"批次契约"，无"规格文档"及其寿命；属已裁的"不升格永久 SPEC" |

### 空位汇总（按证据，不按感觉）

| 空位 | 性质 | 依据 |
|---|---|---|
| **P11 长期意图/意图文档** | **完全无承接**（读/产/落点三缺） | 唯一出处 proposal:112；现行 Oracle §4.2 不读它；10 角色 §3 无产物 |
| **P10 词汇表/ADR** | **部分**：有写者、有项目侧落点，**无"开工前读"动作、无 workflow 产物/环节** | `architect.md:203`（只在冲突时触发）、`:209-211`；SET-A #22/E1-6 |
| **P12 ideation / discovery 全段** | **完全无承接**（只有 grill 的提问片段） | `SOURCES.md:183`（wayfinder 等 NOT ABSORBED）；`OPEN-ITEMS.md:42`（C7 未开始） |
| **P14 环境就绪** | **部分**（分流而非 owner；且修在实现环） | `.pi/core/TASK.md:27-28`（C1；"没有修环境"在 `:28`）；`.pi/repair/REPORT.md:24` |
| **P15 过程记录留痕** | **部分**（有形态无环节/落点） | SET-A #20/#21；异常表 1 的 E1-4/E1-5 |
| **P16 feature map** | 十角色内无；Owner 已定向到表外"人类沟通面" session | `OPEN-ITEMS.md:13/16/37/38` |
| P13 上下文边界 / P17 triage / P18 规格层 | 条件缺失或已裁不引入 | `REPAIR-PLAN-3.md:23`、`SOURCES.md:183/253`、`REPAIR-PLAN-3.md:109` |

---

## 归因（事实链条，不做道德评判）

**引入者**：`5b41cd4`（proposal v1.0-final）—「意图文档」被写成 Oracle 的**阅读物**（`docs/…PROPOSAL.md:112`）；同版 `:181` 把 grill+interview 合成 `decision-grilling` 并规定输出**决策卡**。`a9a709d` 更早已在 proposal 里写过"产出物：结构化决策卡"（`a9a709d:docs/…PROPOSAL.md:158`）。

**实现者**：`e053963` — 8 个 skill 落地，其中 `skills/decision-grilling/SKILL.md` 有完整退出判据与产物（现归档 `docs/archive/skills/decision-grilling/SKILL.md:32-34/50`）。**此时产物是存在的。**

**丢失者：折叠轮 `.pi/round1`（未提交）**：
- `.pi/round1/TASK.md:112` 把"**意图对齐与提问**"派给 Driver，上游 matt grilling + addy interview-me；
- `.pi/round1/decisions.tsv`「按 Owner 决定**取消 skills/ 载体**，经验写进 `roles/*.md`」；
- 结果：driver 得到**提问方法**（现行 `:143-155`），**决策卡没有迁移到任何角色 §3** → 产物消失。
- 同一轮还留下一次自认的缺口：`.pi/core/TASK.md:33`「上游有 `domain-modeling`… **R1 时是挂在 architect 名下的死链，重写时没补回来**」。
- 该轮的验收目标本身写着「**自洽无断档**：角色 ↔ 方法 ↔ 流水线阶段，一处都不能缺」（`.pi/round1/TASK.md:38`）——**目标有、检查手段没有针对"产物"**。

**补修者（未提交）**：`.pi/core` 计划（`TASK.md:31-35` C2、`PLAN.md:222-230`）→ Oracle 裁定写者≠裁定者（`.pi/core/ORACLE-REVIEW.md:12`）→ Owner D3（`SOURCES.md:180`）→ `.pi/repair/REPORT.md:27`（R6）落地为 `architect.md:201-217` 等 6 处。**补回了写者与裁定权，没有补回 §3 产物与 pipeline 环节** → 所以它在 SET-A 里只能算 #22 的"无环节"项。

**系统性原因（本批最值得注意的一条）**：
1. **吸收台账没有"产出物"栏**：`SOURCES.md` 的表格列是「来源 \| 机制 \| 处置 \| 改写/删除理由 \| **落点**」（表头见 `SOURCES.md:25/35/57`）。"落点"记录的是**规则句子落到哪个角色节的哪一步**，**不记录"这条规则吸收后要产出什么、交给谁"** → 折叠轮把"skill（有产物）"改成"方法节（只有动作）"时，台账全绿，产物消失无人发现。
2. **检查器只兜结构**：`README.md:70-72` 与 `scripts/check-library.py` 自述只查结构/闭环/死链，不查"某方法节是否还应产生产物"。
3. **折叠轮的自查项不含产物**：`round1/TASK.md:38-39`（"自洽无断档 / 充足且闭环"）在实现时被当成"箭头闭环"（`closure.md` 的字段闭环），**没有一条检查问"每个被吸收的方法，产物去哪了"**。

**一句话归责（按证据）**：**上游无责**——matt 的 grilling/domain-modeling 与 addy 的 interview-me 都自带产物或确认门规定，wayfinder 等未被吸收也如实登记为 NOT ABSORBED；**错在本库折叠轮的吸收方式**（取消 skill 载体时只迁方法、不迁产物，`round1`）+ **登记方式缺"产出物"检查栏**（`SOURCES.md` 表头）+ **自查项只查箭头不查产物**（`round1/TASK.md:38-39` 对 `closure.md`）。三处叠加，使"吸收后是否还产生东西"这个问题在本库里**没有任何一处会提出**——所以 24 项统计里看不到 grill 产物与意图文档，**不是漏数，是它们确实已经不存在了**。

*（唯一有产物却被计成"无环节"的是词汇表/ADR：它在 SET-A 里是 #22，异常 E1-6；它的写者与裁定权是 `.pi/repair` R6 补的，同样未提交。）*
