# SUMMARY · 熔炼后的答案 + 开放问题

> 证据逐条在 `EVIDENCE.md`（引用格式：`E-章节-序号`，如 E-G1.1-04）。本文只作答与判，不给实施方案。
> 三仓锁定：`ecc249f`（cursor-plugins）/ `c55ee46`（matt）/ `2686b62`（addy），均干净。

## 一、三条主问题的答案

### Q1 · "文档体系该长什么样"（三仓能支持的部分）

三仓给出的可复用骨架，可以归成**六个必须被点名的东西**。三仓在这六条上分布不均，下表同时标出"谁有、谁没有"。

| # | 必须被点名 | 三仓证据 | 缺了会怎样（有原文支撑） |
|---|---|---|---|
| 1 | **每个记录的落地位置**（写在仓里、写在工作区、写临时区） | pstack 台账「`decisions.tsv` in the work dir，or `.audit/<task-slug>.tsv`；默认不进 git」（E-G1.1-01）；addy `SPEC.md`/`tasks/plan.md`/`tasks/todo.md` 固定路径（E-G1.3-01）；matt `.scratch/<feature>/spec.md` + `issues/NN-slug.md`（E-G1.2-02） | 记录散在会话里，恢复靠回忆（pstack `session-pickup` 明说"prior trail is authoritative"，E-G1.1-05） |
| 2 | **每个记录的唯一写者** | pstack「Every file has exactly one writer」、「One writer per worktree or branch」（E-G1.1-04/E-G3.1-01）；orchestrate 三角色写权矩阵（E-G3.2-02/03） | 并发写同一条记录 → 谁的版本是真无法判；pstack 用 `orch` 锁处理持有者消失（E-G1.1-04） |
| 3 | **三类写法不能混**：事实表**就地更新**、事件记录**只追加**、派生视图**由工具重算** | pstack store 布局（E-G1.1-04）；台账 append-only（E-G1.1-03）；`status.md` 由脚本从 TSV 重算（E-G1.1-04） | 手工维护的派生视图会与事实表分叉；台账被编辑就失去历史（E-G1.1-03 反例） |
| 4 | **寿命分级与保留判据**（临时/工作/耐久） | pstack：台账默认本地，只在"reviewer 需要 trail"时提交；store 保留作 postmortem；resume note 在 `/tmp`（E-G1.1-01/05）。addy：活文档可 merge 前删或 gitignore；ADR/changelog 耐久；eval 结果 gitignore（E-G1.3-01/05）。matt：handoff 与架构评审 HTML 进 OS temp，ADR/`.out-of-scope/` 耐久（E-G1.2-07） | 要么全进版本库（噪声与腐烂），要么全丢（不可追溯）；三仓都选了显式分级 |
| 5 | **防腐烂的写法判据** | matt：规格/工单**禁写文件路径与行号**（"they go stale"，E-G1.2-03）；pstack：feature map 只留用户路径与可观察证明，不留实现细节（E-G2.1-02）；addy：ADR 只记 why 与替代方案、不许改旧 ADR（E-G1.3-05） | 文档指向的路径/行号过期后，读者无法判断文档是否还有效 |
| 6 | **更新触发 + 维护者** | pstack：每决策/每轮循环/每 drain/每 30 分钟 tick（E-G1.1-02）；matt：triage 状态机 + 认领先于干活（E-G1.2-02/04）；addy：每个任务边界 + 每任务一 commit（E-G1.3-06）；matt 的文档与技能**同一次改动里同步**（E-G1.2-06） | 没有触发的记录只会在会话结束时补写，等于事后追述 |

**三仓明确没有的一层（本仓要补的就是这一层）**：
- 三仓都**没有**"某个角色的所有交接物统一落某目录 / 由某角色保管 / 有统一保留期"的中央文档制度（E-G1.5-1）。
- 三仓都**没有**把"过程记录 vs 工作现场"做统一分类（E-G1.5-2）。
- 三仓都**没有**"会话产物归档层"这个概念；pstack 的 store 是唯一最接近的（E-G1.1-04/05），matt/addy 完全依赖项目仓/外部 tracker 的既有约定。

**因此，"文档体系该长什么样"的可靠答案是**：
1. 本库需要补的是 **"产物分类 + 落地位置 + 唯一写者 + 三类写法 + 寿命分级"** 这五件事——这五件在三仓都有可引原文，属于**吸收**，不是发明；
2. 本库历史里已有一版"项目文档双模适配"草案（复用项目已有真源，或经 Owner 同意后引入轻量规范），现在被丢在 `docs/` 与 `docs/archive/`（E-G5.6-A1）——它回答的是"下游项目里这套记录往哪里接"，与本库自身的记录体系是两件事，需要分开裁；
3. 本库**不能**照搬 pstack 的部分：它的 `decisions.tsv` 会把"Reverted/未测出"也记进永久历史的假设依赖 append-only 文件，而本库对"临时证据不得升格为可复用"有更硬的规则（`pipeline.md §8`），两者的**寿命判据不同**（E-G1.1-01 vs E-G5.5-2）。

### Q2 · "角色写权限该按什么粒度限制"

**结论：三仓一致地把"能不能写"拆成四问，从不使用"某角色禁止写"这种整体禁令。**

四问（三仓证据在 E-G3.5 的交叉表）：
1. **写不写产品实现代码**——pstack 的 coordinator「never authors or edits code」、verifier「Do NOT modify target source files」、维护者「Never edit product code」（E-G3.1-03/04/E-G3.2-02）；matt/addy 靠技能定位而非权限字段（E-G3.3-01/E-G3.4-01）。
2. **能不能写自己的交付物**——三仓都**要求**判断侧写自己的证据/报告：pstack verifier 必须写 verdict handoff 与 ledger 行、可把 repro 脚本提交到自己分支（E-G3.2-02）；matt 各技能写自己的 tracker 件（E-G3.3-03）；addy 各阶段写各自件（E-G3.4-04/05）。→ **"禁止写"必须排除"写自己的报告"**，这是三仓共同的隐含前提。
3. **临时探针与实验写在哪里**——pstack/addy 都规定临时件进"工作目录/OS temp/被屏蔽块"，且 cleanup 只清 scratch **不清 evidence**（E-G3.1-05，E-G3.4-04）；matt 的 handoff/HTML 也进 OS temp（E-G3.3-02）。
4. **共享状态与配置谁能改**——pstack 每文件一个写者、`status.md` 只由脚本写、operator-mode 文件 `0600` 门（E-G3.2-03）；matt 对 tracker 的写有显式条件（不许关父 issue、不许写已实现的 `.out-of-scope/`）（E-G3.3-03）；addy 用唯一人门 + 每任务一 commit（E-G1.3-06）。
   （第五类——日志只准追加——pstack 有明文，matt/addy 无对应物；E-G3.6-3。）

**三仓都没有的东西**：按角色名的 ACL / capability 表；"reviewer 一律不许写"这类禁令；日志的删除权限分级。（E-G3.6）

**对本库问题的直接回答**：我们派活时说的"reviewer 禁止写"**粒度错了**——把四问压成了一条。正确粒度是"**按产物类别授权**"：产品实现代码禁写、自己的 `review-verdict` 必写、临时探针限临时空间且收尾清理、共享状态与配置只在被授予单写者身份时写。本库角色文件的 §5「我可以/我不可以」其实已经是这个粒度（`roles/reviewer.md:225-229`、`roles/verifier.md:226`、`roles/implementer.md:199-203`、`roles/integrator.md:183-187`、`roles/ledger-custodian.md:149-158`），**问题出在派活语言没有引用 §5，而另说了一句更粗的话**。

### Q3 · "四套方法论各归哪个角色"

| 方法论 | 主角色 | 副角色 | 归位理由（一句话） | 本库现有落点 |
|---|---|---|---|---|
| **BDD**（行为驱动） | Driver（Discovery/验收）、Planner（可判否判据）、Implementer（行为先行） | Reviewer（挑战前提）、Verifier（对着行为给三态） | BDD 的三种实践 Discovery/Formulation/Automation 正好是三段分工；"Should it? Really?" 是审查动作 | `driver.md:68`、`planner.md:136-153`、`implementer.md:107-140`、`reviewer.md:170-176` |
| **TDD**（测试驱动） | Implementer（红—绿—重构）、Investigator（缺陷先复现） | Planner（接缝与判据）、Verifier（变异/反例证明检查有效） | 谁改行为谁先写会红的检查；缺陷路径的回路属于调查 | `implementer.md:107-140/161-179`、`investigator.md:49-67/76`、`verifier.md:49` |
| **DDD**（领域建模；标准术语是 Domain-Driven **Design**） | Architect（模型与边界、术语冲突的查证与备选） | **Owner/授权业务角色=裁定者（不属十角色）**、Investigator（一手用词）、Reviewer（词义冲突阻断） | DDD 的模型是设计产物；但本库硬边界是"工程侧不得裁业务含义" | `architect.md:201-217`、`investigator.md:95`、`planner.md:107`、`reviewer.md:142`；`SOURCES.md:180` |
| **SDD**（规格驱动） | Architect（spec 层=`design-proposal`）、Planner（spec→tasks）、Driver（每批 task-card=批次契约） | Reviewer/Verifier/Integrator（守约：对象身份绑定与字段闭环） | SDD 的"先 what/why 后 how"与"任务带验收"正是这三段 | `architect.md:82/170-185`、`planner.md §3`、`closure.md`、`identity.md`、`pipeline.md §3.2/§6` |

**四套的层级关系（不是并列）**：BDD ⊃ TDD（BDD 是 TDD 的验收层扩展，Dan North 原文）；SDD 与 DDD 是**输入层**（先定要什么/词指什么），TDD/BDD 是**证明层**（怎么证明行为成立）；本库把它们拆进不同角色的理由也正是"输入层由 Architect/Planner/Owner 负责，证明层由 Implementer/Verifier 负责"——**判断与实现分离这条硬边界同时解决了四套的方法归属**。

**必须指出的一处真实冲突（需人裁，见开放问题 3）**：BDD 原文允许"前提变了就删测试"，本库禁止"为了让检查变绿而削弱检查"。

---

## 二、我方复核的缺口清单（对 Owner 初判的判定）

| # | Owner 初判 | 我的判定 | 依据 |
|---|---|---|---|
| 1 | 交接物有名字，没规定落在哪、谁保管、活多久 | **成立**（更强的说法：本库把"记录留不留"当成每批一次的商业决定，而非体系默认） | E-G5.1 |
| 2 | 没有跨角色的文档层级 | **成立**（注意本库有"契约层级"，但那不是"文档层级"） | E-G5.2 |
| 3 | 没有 feature map 类的东西 | **成立**，且是 `SOURCES.md:142` 明写的**有意未采纳**；本库只有"库自身检查项"，没有"产品行为索引" | E-G5.3 |
| 4 | 没有 to-do / 进度管理 | **成立**；本库还明确拒绝百分比进度（`driver.md:331`），进度只以事件和收口快照表达 | E-G5.4 |
| 5 | 没有"哪些算过程性记录必须保全、哪些算工作现场可以丢"的规定（Owner 认定的根因） | **半成立，措辞需改**：本库对**承重证据**已有相当严格的保全/禁用规则（`driver.md:207/276`、`pipeline.md §8`、`verifier.md:47`、`reviewer.md:50`、`identity.md:36`），缺的是**过程记录层**（报告/结论/提案/切片/决策）的分类与归属 | E-G5.5 |

**我追加的缺口（Owner 清单之外）**：A1 旧载体的"文档双模适配"现被丢失；A2 决策台账只挂在 `verifier.md §4.8`、未接全库；A3 没有项目级门禁载体（`CONSTRAINTS.md` 位置）；A4 没有产物索引/路由器；A5 没有"记录活多久"的判据；A6 没有人类可读说明层（onboarding）；A7 没有 DDD 的上下文边界层（Bounded Context/上下文映射）；A8 没有"文档被悄悄放宽/腐烂"的检测面。详表 E-G5.6。

---

## 三、我判断不了、必须交人裁的开放问题

**O1 · 这套记录体系的"权威真源"放在哪，谁是维护者？**
三仓可类比：matt 用外部 tracker 当唯一真源并让技能配置指向它；pstack 用 agent store + 每文件一个写者；addy 用仓内固定路径。三者互斥（外部工具 / 运行底座 / 项目仓），本库"与运行底座解耦"的定位决定不能选 pstack 式 store，但选"项目仓内固定路径"还是"下游已有 tracker/文档体系"需要 Owner 定，且要与 `AGENTS.md` 纪律 2（下游按固定 commit 引用）兼容。**关键取舍：本库只规定记录的类别与判据（形态无关），还是同时规定默认落点（形态相关）。** 证据：E-G1.4、E-G5.6-A1。

**O2 · "过程记录"要不要有保留期与清理责任？**
pstack 的"本地默认、需要才提交"与 addy 的"可 merge 前删"是两种相反默认；本库现有对证据的规则（"可从临时位置消失的不得复用"）会与"记录默认不落盘"直接互相作用。需要 Owner 裁：默认保留、默认丢弃、还是按类别分档（谁判档、多久复核一次）。证据：E-G1.1-01、E-G1.3-01、E-G5.5。

**O3 · BDD 的"前提变了就删测试"与本库"不许削弱检查"如何排他裁决？**
BDD 原文允许删除过时测试；本库的防线是"改判据必须回 Planner/Architect，不由实现者自行删"。两者的差别是**"谁有权宣布前提变了"**：BDD 假设业务/开发者可以，本库只允许授权侧。需要确认本库是否已有足够的例外通道（例如 `design-proposal.open_questions`/`pending-question`）覆盖"合法删测试"的场景。证据：E-G4.1、E-G4.5-1、`roles/implementer.md:203`。

**O4 · SDD 要引入到哪一级？**
Böckeler 明说 SDD 术语未定，且分 spec-first / spec-anchored / spec-as-source。本库现状是 spec-first + 局部 spec-anchored（每批冻结、批次结束无长期 spec 载体）。引入 SDD 可能等于引入"长期活文档"（新载体 + 新维护责任），也可能只需要把现有 `design-proposal` 上升到"项目级 spec"（会与"每批一卡"的授权模型冲突）。这是**范围决定**，不是技术细节。证据：E-G4.4、`SOURCES.md:253`、`pipeline.md §10`。

**O5 · feature map 这一层要不要、以什么形态引入？**
上游形态是"项目内验证技能目录 + 每功能一文件"，本库已明确不吸收该载体（`SOURCES.md:142`）。若引入，必须先答：它的分割单位（用户可见功能）、驱动面（谁来驱动）、维护循环（谁跑 maintain、靠什么触发）、缺失时是否 fail-closed——四项都有上游原文可引（E-G2），但"谁来承担维护"在本库没有人选（现有十角色无"验证资产管理"角色）。**这是新增角色/职责的问题，交 Owner。**

**O6 · DDD 的"上下文边界"要不要补？**
本库吸收了术语冲突与 ADR 三条件，但没有 Bounded Context / 上下文映射层（E-G5.6-A7）。补它意味着 Architect 的产出新增一个层级（模块/上下文表），并要处理"同一词在不同上下文有不同模型"与现有"唯一词汇表"假设的冲突。需要 Owner 裁是否在范围内。证据：E-G4.3、`SOURCES.md:180`。

**O7 · 本库自身（作为一个仓库）要不要纳入自己定义的文档体系？** → **Owner 已在 `AB-SPEC.md` §4 定为"要"**（"搭建文档体系的过程中，要把本库自己的文档也按同一套标准优化；本库自己就是最好的实验场"）。本条因此不再是开放问题，而是 **O8/O10 的适用对象**（同一套标准先在本库试点）。

---

## 四、给 reviewer 的三条使用说明

1. 本文所有"三仓有/无"的判断都以 `EVIDENCE.md` 的 `file:line` 为准；两个外部关键判断（SDD 未定型、BDD 允许删测试）是**外部来源**，已在 G4 标注 URL 与原文，不属于三仓吸收。
2. 本库"已有影子"清单（G4 各表最后一列、G5.5 的既有规则）说明：**四套方法论不是新造，只是归属与命名没有显式化**；任何改造应先在现有角色 §4 里找落点，而不是新增章节。
3. 我未做的判断：不给方案、不选载体、不评"哪种更好"。上述 O1–O7 全部需要人裁或更高阶 reviewer 综合。

---

## 五、追加任务（Owner 第二批：① 清点 / ② 拼接已有体系 / ③ feature map 定位 / ④ 过程记录层）

### Q4 · 三仓文档全清点的结论（支撑我们自己设计）

**全量清单在 `EVIDENCE.md` G6**（pstack L 表 + A 表、matt L 表 + A 表、addy L 表 + A 表，各自带路径·命名/写者/触发/频率/VCS）。可直接搬的部件：

1. **路径与命名（三仓都有可引规则）**：pstack `orchestrate/<project-slug>/` + 固定文件名（`units.tsv`、`ledger.tsv`、`decisions.tsv`、`handoffs/<task-name>.md`）；matt `.scratch/<feature-slug>/{spec.md,issues/NN-<slug>.md}`（编号从 01、一单一文件、编号即依赖顺序）；addy `SPEC.md`/`tasks/plan.md`/`tasks/todo.md` 白名单。
2. **三类写法必须分开**：事实表就地更新 / 事件记录只追加 / 派生视图由工具重算（pstack，G6.1-L）。
3. **寿命三档**：临时（OS temp，不进仓）→ 工作（本地不上版本库，"reviewer 需要 trail"才提交）→ 耐久（tracker/ADR/spec）。三仓都各有实例（G6 表最后一列）。
4. **层级**：**只有 addy 有正式的产物分层**（rules→spec/arch→source→output→conversation + 信任级别，G6.3-H）；matt 给的是"加载预算/受众分离"（agent 文件极简→标准只在审查读→docs 被指到才读→技能自带文档）；pstack 给的是受众分离（人 README/guide vs agent SKILL.md vs 下一个 agent 的生成物）。
5. **防腐触发**：addy 把"文档/产物路径一致性"做成了 CI 门（`validate-artifact-paths.js`，单一白名单：`SPEC.md`/`docs/SPEC.md`/`tasks/plan.md`/`tasks/todo.md`；历史事故 PR #93），另有 skill 结构/命令三面一致/引用链接三个校验；matt 用"技能变动→同步五处"的硬规则 + changeset/release；pstack 用 maintain/reflect/收口写回。**三仓都没有常驻文档维护职责，也没有固定刷新周期**。

**最值得注意的一条**：addy 的两个历史事故（producer 改产物路径、SKILL 引用链接断）都是"**只在文档之间保持一致，没有任何自动化在盯**"造成的；它的修法不是写更多文档，而是**把唯一约定写成常量并用 CI 盯住**（G6.3-R / G7-08）。

### Q5 · ② 已有治理系统时，Driver 怎么裁定产物去向

**本轮 Owner 已给定框架（`.pi/investigation/AB-SPEC.md`，设计输入，高于本节建议）**：A = workflow 可产出的全部文档类型（带产出方 + 产出环节）；B = 目标仓已有文档体系（带何时写 + 谁写 + 什么时候发生）。情况 1（B 空/薄）：问 Owner 后把 A 搬进 B 并按 A 的标准移植 B；情况 2（B 厚实）：做 A↔B 逐项**映射**，Driver 形成 **adaptive 版本**（举例 `a→3, b→2`），要发挥主观能动性；情况 3：Owner 同意时可按 A 改造 B。

**三仓做法对 AB-SPEC 的用处（四件可搬的零件）**：
1. **探测先于发问**：不猜，先读现有物（matt `setup-matt-pocock-skills/SKILL.md:21-30` 的探测清单；addy `documentation-and-adrs/SKILL.md:36-44`）。
2. **既有约定覆盖技能默认**：addy 原文「An established convention overrides the defaults below」「Only when no convention can be established do you apply the default below」（`documentation-and-adrs:36-44`）；外部 spec 工具就沿用它、不另建 `SPEC.md`（`spec-driven-development:150-153`）；任务跟踪走外部 tracker 时 plan 只留索引不复制（`planning-and-task-breakdown:162-164`）。
3. **冲突显式摊开，不静默造第二来源**：「surface the conflict rather than silently introducing another scheme」（同上）；matt 的 ADR 矛盾要拿出来问（`domain.md:47-51`）。
4. **映射结果必须落成单一真源 + 机械检查**：否则 producer/consumer 会分叉（addy 真实事故：`scripts/validate-artifact-paths.js:1-17`）；另外用户自有配置/地图不得被覆盖（pstack `setup-benny:28`）。

**三仓无此法（对 AB-SPEC 情况 2 的直接回答）**：① 没有任何逐项 A↔B 映射的成例，也没有 adaptive 文档体系的产物形态；② 没有任何一仓处理"项目已有体系承载不了我们的必需字段时怎么办"；③ 三仓都没有"项目已有系统会改动我们的状态（例如勾完成/关工单），谁说了算"的规则。→ Owner 对三仓的判断成立。以上①②③均属交人裁（见 O8/O9）。

### Q6 · ③ feature map：可选能力、持有者、触发

**定位（Owner 口径 + 上游证据一致）**：**可选，不得作为开工门**；但**建立能力必须完整存在**（= 生成 + 维护 + 防腐烂，上游六步见 `EVIDENCE.md` G8-01）。上游通用路径下它由"项目没有脚本化驱动面且需要验证"触发（`06-verify-and-ship.md:35`）；维护循环无目标时拒绝开工而非强行造目标（`maintain:25`）；**唯一把它当必需的场景是 benny 自动化**（先有 `control.feature_map_path` 配置，`benny/SKILL.md:11`、`control-adapter.md:9`）——那是项目自选的前置，不是通用要求。

**触发权（按 AB-SPEC）**：**Driver 根据当前项目尺寸/预期尺寸判断并建议 User 建立**；可用的判定信号在上游有对应物：项目没有可复用驱动面 + 确实存在反复驱动同一批入口的需求（`06-verify-and-ship.md:35,39,41`）。**不触发**：一次性验证、已有可靠驱动面、无人需要重复跑。

**建立过程（按 AB-SPEC）应像 grill（对话式、按 frontier 一轮轮推进，不是填模板）**：本库**已有现成方法**——`roles/driver.md:143-155` §4.1「对齐目标：按 frontier 分轮提问」（画决策树 → 算 frontier → 每问自带推荐答案 → 一轮问完再下一轮 → frontier 清空才开工）。→ **不需要新方法**；把上游 `create-verification-skill` 的"访谈代码库五问"接到 Driver 的 frontier 会话里即可（事实自己查、决定问人）。

**能力执行者（我的证据建议，需 reviewer/Driver 核）**：**Verifier 持有完整能力**——它的四节方法（对象/环境断言 `verifier.md:69`、真实入口驱动 `:88`、判据必须能失败 `:169`、证据复用四条件 `:188`）与权限（临时空间写夹具/探针/变异 `:226`）已是该能力的内容；**Investigator 提供构造回路手艺**（`investigator.md:49,76`，其回路是对症状的，不是对功能面）；**Driver 管触发判定、授权与写窗**（`pipeline.md §2`、`driver.md:206`）；**map 落仓须走"独立可审候选"**（本库已有此规则：`verifier.md:86`；先例：台账能力挂 `ledger-custodian` 且按需参与，`closure.md` A3）。**不需新角色。**

**必须一并写进能力的一条约束**：map 缺失/未建立时，验证照常按当次判据进行，Driver 在装配说明里声明"本轮无复用验证面"——不让它变成事实上的开工门（与 AB-SPEC §3 一致）。

### Q7 · ④ 过程记录层：定义与我方缺口

- **定义（按 Owner 澄清）**：每个角色"拿到的那一份"与"产出的那一份"（交接输入/输出）。三仓对这批东西的处理逐类对照见 `EVIDENCE.md` G9-02（任务卡/规格/审查结论/决策记录/恢复笔记/进度状态）；**三仓都没有"按角色列输入/输出记录"的表**，pstack 最接近的只是"每文件一个写者"的**存储层**规则（G9-04）。
- **本库现状**：交接物有**字段契约**（`closure.md:21-33`）但无落地位置/写者/寿命（G5.1）；已有规则只覆盖"承重证据"（`driver.md:207/276`、`pipeline.md §8`），不能当过程记录层的答案（G5.5）。
- **结论**：这一层是真空白；三仓只有零件（唯一写者、三类写法、寿命三档、派生视图重算、单一白名单+CI），没有成品。

### 新增开放问题（接 O1–O7）

- **O8 · 要不要把"单一真源 + 机械检查"引入本库的文档体系？** addy 的四类校验器证明了它有效（并留下了事故理由），但本库 `README.md:70-72` 与 `AGENTS.md` 已给新检查设了保留判据（能声明真实断言、有会红的反例、误报可控、维护成本与负责人）。需要 Owner 裁：先建"单一约定表"，还是先建检查。
- **O9 · 项目已有体系与我们的"状态权"冲突时谁说了算？**（谁有权勾完成/改状态/关工单；项目自己的 todo 可能让实现者自勾完成，而我们的硬边界是"判断与实现分离"）。三仓无成例，只能人裁。
- **O10 · 过程记录的默认寿命档与复核人**：进版本库 / 工作区 / 临时，三选一作为默认（或按类别分档）；以及"谁来定期清理"（本库无文档维护者角色；现有十角色的职责均不含"文档维护"）。
- **O11 · feature map 的持有者与独立性**：若由 Verifier 持有，是否接受"验证者既定义接受面又验证"（本库已有 `verifier.md:86` 的隔离机制，但未点名适用于 map）；还是要求落仓时由第二个角色独立审一次。
- **O12 · 下游已有文档体系的接入方式要不要回收到本库？** 旧载体的"双模适配"（复用或裸引导规范，`docs/TIM-PROFESSIONAL-WORKFLOW-PROPOSAL.md:145-165` + `docs/archive/skills/professional-workflow/SKILL.md:35-40`）已被丢失；是恢复它，还是按三仓做法只要求"探测→既有优先→冲突摊开"三个可核对动作。
