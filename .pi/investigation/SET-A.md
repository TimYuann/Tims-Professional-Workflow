# SET-A · 本库文档类型全集（A 侧）

**任务**：`TASK-2.md`。**方法**：只读 `roles/*.md`（10 份）+ `pipeline.md` + `closure.md`（+ `identity.md`，因为它被六份角色文件内联引用），逐条提取"角色拿到的那一份 / 交出的那一份"。
**限定**：本文件只立事实，不设计体系、不提方案。**"无"是结论，不是省略**——找不到产出环节写"无产出环节"，找不到落点规定写"无"。

## 0. 口径

| 项 | 取值 | 出处 |
|---|---|---|
| **产出环节** | `pipeline.md` 主链 0–8（`:19-27`）与按需 A0–A3（`closure.md:39-42`）；无则写"无产出环节" | `pipeline.md:6-27`、`closure.md:37-42` |
| **类别** | **承重证据** = 该文档被后续判断/放行/身份/授权/冻结契约直接引用；**过程记录** = 记录来龙去脉但不直接充当放行依据（报告/提案/切片/问题单/汇总/裁决） | 按 `TASK-2.md` 的定义；逐行备注依据 |
| **寿命档** | D 长期权威与审计骨架 / W 活跃批次/周期记录 / E 可复用证明材料（按引用） / S 可丢工作现场；**拿不准写"待定"** | `.pi/core/REPAIR-PLAN-3.md:36-39`（**该文件是一份修复计划，不是已采纳规范**，此处只借用其四档口径） |
| **落点** | 指"这份东西存在哪里、以什么文件名/形态落地"的规定；只写字段规则不算落点 | `TASK-2.md` |

**不做的事**：不判"应该放哪"；不评寿命是否合理；承重证据的保全/失效规则已有（`roles/driver.md:207/276`、`pipeline.md §8`），本文不重复。

---

## 1. 集合 A（24 项）

### 1.1 角色 §3 明确产出的交接物（15 项）

| # | 名称 | 产出方（file:line） | 产出环节（file:line） | 消费者（file:line） | 类别 | 现有落点规定 | 建议寿命档 |
|---|---|---|---|---|---|---|---|
| 1 | `owner-brief` | Owner（外部，非本库角色）；接收方 `roles/driver.md:18` | 步 0 发卡（输入侧）`pipeline.md:19`、拓扑 `pipeline.md:134` | `roles/driver.md:18` | 承重（授权/目标） | **无** | W（其中授权原文随 #18 升 D） |
| 2 | `task-card` | `roles/driver.md:58` | 步 0 `pipeline.md:19`、拓扑 `pipeline.md:135` | `roles/investigator.md:18`、`roles/architect.md:30`、`roles/implementer.md:32` | 承重（授权/判据/依赖） | **无**（装配说明写入卡内：`closure.md:42`） | W |
| 3 | `pending-question` | `roles/architect.md:51`、`roles/reviewer.md:55`、`roles/driver.md:71` | 按需 A0 `closure.md:39`；拓扑 `pipeline.md:136/143/144` | `roles/driver.md:32/36`、`roles/oracle.md:18`（经 Driver） | 过程记录 | **无** | W |
| 4 | `oracle-ruling` | `roles/oracle.md:31`；降级时 `roles/reviewer.md:67` | 按需 A1 `closure.md:40`；拓扑 `pipeline.md:150/151` | `roles/driver.md:40/44` | 过程记录（裁决） | **无** | D |
| 5 | `investigation-report` | `roles/investigator.md:30`；跳过调查时 Driver 代产 `roles/driver.md:89` | 步 1 `pipeline.md:20`、拓扑 `pipeline.md:141/137` | `roles/architect.md:18`、`roles/planner.md:31`、`roles/implementer.md:37`、`roles/verifier.md:33`（部分字段）、`roles/driver.md:28` | 过程记录 | **无**；内含路径字段 `repro_fixture`（`roles/investigator.md:43`），且受 `pipeline.md:108`"记录可取回"约束 | W（夹具/命令升 E） |
| 6 | `design-proposal` | `roles/architect.md:36` | 步 2 `pipeline.md:21`、拓扑 `pipeline.md:142` | `roles/planner.md:18`、`roles/implementer.md:28`、`roles/reviewer.md:33` | 过程记录（含冻结契约 `bound_contract`） | **无** | W |
| 7 | `slice-plan` | `roles/planner.md:37`；跳过切片时 Driver 代产 `roles/driver.md:96` | 步 3 `pipeline.md:22`、拓扑 `pipeline.md:145/138` | `roles/implementer.md:18`、`roles/reviewer.md:29` | 过程记录 | **无** | W |
| 8 | `candidate` | `roles/implementer.md:49` | 步 4 `pipeline.md:23`、拓扑 `pipeline.md:146` | `roles/reviewer.md:18`、`roles/verifier.md:20`、`roles/integrator.md:30` | 承重（对象身份） | **无文件落点**；身份序列化 `identity.md:20`，跨会话移交要求 `identity.md:58-60` | W（对象身份升 D） |
| 9 | `review-verdict` | `roles/reviewer.md:43` | 步 5 `pipeline.md:24`、拓扑 `pipeline.md:147` | `roles/verifier.md:29`、`roles/implementer.md:43`、`roles/integrator.md:34` | 承重（放行结论＋对象绑定） | 仅"承重证据路径"字段规则：`roles/reviewer.md:50`、`roles/reviewer.md:108` | D（结论+证明指针）＋W（明细） |
| 10 | `verification-evidence` | `roles/verifier.md:41` | 步 6 `pipeline.md:25`、拓扑 `pipeline.md:148` | `roles/integrator.md:18` | 承重（证明） | 仅路径规则：`roles/verifier.md:47`、自建装置 `roles/verifier.md:86`、`pipeline.md:108` | D＋E |
| 11 | `integrated-baseline` | `roles/integrator.md:40` | 步 7 `pipeline.md:26`、拓扑 `pipeline.md:149` | `roles/driver.md:48` | 承重（交付对象身份） | **无** | D（对象身份）＋W |
| 12 | `roundup` | `roles/driver.md:81` | 步 0 交 / 步 8 收口 `pipeline.md:19`、`closure.md:33`、拓扑 `pipeline.md:140` | Owner（外部） | 过程记录（收口汇总） | 仅内容规则：`roles/driver.md:276` | D（最终 roundup） |
| 13 | `equivalence-proof` | `roles/driver.md:108` | 步 5 跳过路径 `closure.md:30`；拓扑 `pipeline.md:139` | `roles/reviewer.md:37`（及拓扑所列 verifier/implementer） | 承重（替代审查的证明） | **无**（受 `pipeline.md:108` 可取回约束） | E |
| 14 | `ledger-input` | `roles/driver.md:133` | 按需 A3 `closure.md:41`；拓扑 `pipeline.md:152` | `roles/ledger-custodian.md:26` | 过程记录 | **无** | W |
| 15 | `ledger-report` | `roles/ledger-custodian.md:36` | 按需 A3 `closure.md:41`；拓扑 `pipeline.md:153` | `roles/driver.md:52` | 过程记录（对账结论） | **无**（其对象在库内：`roles/ledger-custodian.md:14/20`） | W |

### 1.2 被规则要求存在、但无角色 §3 产物的记录（8 项）

| # | 名称 | 产出方（file:line） | 产出环节（file:line） | 消费者（file:line） | 类别 | 现有落点规定 | 建议寿命档 |
|---|---|---|---|---|---|---|---|
| 16 | `ws:v1` 清单文件（对象身份 manifest） | 计算对象的角色（`identity.md:4-11` 声明"内联规则"，driver/implementer/reviewer/verifier/integrator/oracle 各 §3 内联）；无单一 `产出` 行 | **无产出环节** | 所有接收 `object` 的角色（如 `roles/reviewer.md:18`、`roles/verifier.md:20`、`roles/integrator.md:18`） | 承重（身份） | `identity.md:60`：**必须连同清单文件本身或其保存路径 + 范围声明一起交** | E（被引用的对象身份升 D） |
| 17 | 范围声明（写入范围清单） | `roles/driver.md:64`（`scope` 字段）、`roles/driver.md:206`（发写窗前分列范围与例外） | **无独立产出环节**（内容属 task-card；但在移交时被要求为独立交付物） | `identity.md:60`、`roles/integrator.md:72` | 承重（身份/范围） | `roles/driver.md:206`、`identity.md:36`、`identity.md:60` | E |
| 18 | 授权记录（authorization record 本体） | **无角色 §3 产物**（`task-card.auth_record` 只是"标识+内容快照"：`roles/driver.md:65`） | **无产出环节** | `roles/driver.md:65`、`roles/implementer.md:34` | 承重（授权） | **无**；仅内容要求 `pipeline.md:122` | D |
| 19 | 证据材料（`evidence_pointer` 指向的夹具/读数/截图/命令输出） | 运行检查的角色（`roles/investigator.md:49` 起的回路、`roles/verifier.md:41` 的 commands、`roles/reviewer.md:108`） | **无独立产出环节**（隐含在步 1/5/6 内） | `roles/driver.md:87`（roundup.evidence_pointer）、`pipeline.md:108`（复用判定）、`roles/reviewer.md:50`、`roles/verifier.md:47` | 承重 | 保管决定 `roles/driver.md:207`；路径资格 `roles/reviewer.md:50/108`、`roles/verifier.md:47`、`pipeline.md:108` | E |
| 20 | 决策台账（append-only TSV） | `roles/verifier.md:212`（表格形态）；Driver 由 Owner 承载时写"该批决策记录"`roles/driver.md:292` | **无产出环节** | 收口前的回核者 `roles/verifier.md:215`、后续会话 | 过程记录（行内含承重指针） | 形态规定 `roles/verifier.md:212-217`；**无路径**；脚本可任意路径 `scripts/log-decision.sh:4`；`README.md:58` | W（关键项升 D） |
| 21 | 停下时的"现场包"（已排除的解释＋证据指针） | **无产出方**（`pipeline.md:102` 只写"停下后打包现场…"） | **无产出环节** | 接手人（`pipeline.md:96-102` 两行的接手列） | 过程记录 | **无** | 待定 |
| 22 | 项目词汇表 / ADR 的更新 | `roles/architect.md:210`（"Architect 是默认**写者**"；无 Architect 时 Driver 指派唯一写者） | **无产出环节** | 项目侧后续设计与实现（`roles/architect.md:206` 要求先映射现有事实源） | 承重（业务裁定/词义冻结） | `roles/architect.md:210`（落入项目既有词汇表/契约；新建需 Owner 同意且先映射既有权威文档）；`roles/architect.md:217` | D（项目层） |
| 23 | 装配说明 | `roles/driver.md`（`closure.md:42` 明确"装配说明写在任务卡里"） | 按需 A2 `closure.md:42` | 被装配的角色 | 过程记录 | `closure.md:42`（无新 artifact，字段化） | W |

### 1.3 库自身产物（1 项，标注：本库专有，非下游通用）

| # | 名称 | 产出方（file:line） | 产出环节（file:line） | 消费者（file:line） | 类别 | 现有落点规定 | 建议寿命档 |
|---|---|---|---|---|---|---|---|
| 24 | `SOURCES.md` 生成区（台账） | 只能由 `scripts/render-ledger.py` 写出：`roles/ledger-custodian.md:14` | 按需 A3 `closure.md:41` | `roles/driver.md:52`、本库维护者 | 承重（本库来源审计） | `roles/ledger-custodian.md:14`（生成区禁手工编辑）、`AGENTS.md:22/34` | D（本库） |

**计数**：**24 项**＝承重证据 **13**（#1、2、8、9、10、11、13、16、17、18、19、22、24）＋过程记录 **11**（#3、4、5、6、7、12、14、15、20、21、23）。

---

## 2. 收件对照（每个角色收到什么 → 谁产）

用于交叉验证"收到的每一份都有人产出、产出的每一份都有人收"。

| 角色 | 主收据 | 副收据 | 接不到任何文档的？ |
|---|---|---|---|
| `roles/driver.md:18-54` | `owner-brief`（Owner） | `investigation-report`、`pending-question`×2、`oracle-ruling`×2、`integrated-baseline`、`ledger-report` | 否 |
| `roles/investigator.md:18` | `task-card`（driver） | — | 否 |
| `roles/architect.md:18-30` | `investigation-report` | `task-card` | 否 |
| `roles/planner.md:18-31` | `design-proposal` | `investigation-report` | 否 |
| `roles/implementer.md:18-43` | `slice-plan` | `design-proposal`、`task-card`、`investigation-report`、`review-verdict` | 否 |
| `roles/reviewer.md:18-37` | `candidate` | `slice-plan`、`design-proposal`、`equivalence-proof` | 否 |
| `roles/verifier.md:20-33` | `candidate` | `review-verdict`、`investigation-report`（仅 bugfix） | 否 |
| `roles/integrator.md:18-34` | `verification-evidence` | `candidate`、`review-verdict` | 否 |
| `roles/oracle.md:18` | `pending-question`（只由 driver 转手） | — | 否 |
| `roles/ledger-custodian.md:26` | `ledger-input`（driver） | — | 否 |

**反向检查**：§1.1 的 15 项，除 #1（Owner，外部）外全部有本库产出方；§1.2 的 8 项中有 6 项无产出方/无环节（见 §3）。

---

## 3. 异常表 1 · **有文档、但找不到产出环节**（7 条）

| # | 文档 | 要求它存在的原文 | 缺什么 | 后果（原文可推） |
|---|---|---|---|---|
| E1-1 | `ws:v1` 清单文件（#16） | `identity.md:60`「交 `object` 时必须**连同清单文件本身或其保存路径**、以及范围声明一起交；**只交 digest 不算交付**」 | 无角色 §3 产出行、无环节、无命名/路径规则 | 交接时"必须交"却没有谁在何时产它：跨会话交接可核性依赖一个未入环的产物 |
| E1-2 | 范围声明（#17） | `identity.md:60`（同上）；`roles/driver.md:206` | 内容在 task-card 字段里，但**作为交付物无独立形态** | digest 不能证明覆盖范围（`identity.md:60`），而范围声明的形态无人负责 |
| E1-3 | 授权记录本体（#18） | `pipeline.md:123`「授权记录必须包含：谁授权、批的是什么对象、条件、有效期、以及执行方的接收确认」 | 无产出方、无环节、无形态/落点（task-card 只有快照字段 `roles/driver.md:65`） | "未被授权的交接停在交付点"（`pipeline.md:124`）靠的是一份没有被规定由谁产出的记录 |
| E1-4 | 决策台账 / 该批决策记录（#20） | `roles/verifier.md:212-217`（形态与 append-only）；`roles/driver.md:292`（Driver=Owner 时写"该批决策记录"） | 无环节、无路径、无保管人 | 回退掉的工作不在版本历史（`roles/verifier.md:217`），台账是唯一防线，但它在流程里没有位置 |
| E1-5 | 停下时的现场包（#21） | `pipeline.md:102`「停下后**打包现场、已排除的解释与证据指针**」 | 无产出方、无产物名、无落点 | 停手后接手人（`pipeline.md:96-102`）要接的东西没有名字与去处 |
| E1-6 | 项目词汇表/ADR 的更新（#22） | `roles/architect.md:210`「被授权的裁定落到项目既有词汇表 / 契约……Architect 是默认**写者**」 | 产出动作被指定了写者，但**不在任何环节、不在 §3 产物**（§3 只有 design-proposal 与 pending-question） | 业务裁定落不到"谁在什么时候交"的链上，只能靠方法节自觉 |
| E1-7 | `SOURCES.md` 生成区（#24） | `roles/ledger-custodian.md:14`（生成区只能由脚本写出）；`pipeline.md:15`（每批落盘后走记录侧边） | 环存在（A3），但**对象是本库专有文件**：下游项目没有对应物 | 下游使用该角色时，A3 要对账什么没有定义（本库内成立） |

---

## 4. 异常表 2 · **有环节、但不产任何文档**（0 条 + 1 条声明例外）

| 环节 | 产出文档 | 判定 |
|---|---|---|
| 步 0 发卡（`pipeline.md:19`） | `task-card`、`pending-question`、`roundup`（#2/#3/#12） | 有 |
| 步 1 调查（`pipeline.md:20`） | `investigation-report`（#5） | 有 |
| 步 2 设计（`pipeline.md:21`） | `design-proposal`（#6） | 有 |
| 步 3 切片（`pipeline.md:22`） | `slice-plan`（#7） | 有 |
| 步 4 实现（`pipeline.md:23`） | `candidate`（#8） | 有 |
| 步 5 审查（`pipeline.md:24`） | `review-verdict`（#9）；跳过路径另有 `equivalence-proof`（#13） | 有 |
| 步 6 验证（`pipeline.md:25`） | `verification-evidence`（#10） | 有 |
| 步 7 集成（`pipeline.md:26`） | `integrated-baseline`（#11） | 有 |
| 步 8 收口（`pipeline.md:27` / `closure.md:33`） | `roundup`（#12） | 有 |
| 按需 A0（`closure.md:39`） | `pending-question` | 有 |
| 按需 A1（`closure.md:40`） | `oracle-ruling` | 有 |
| 按需 A3（`closure.md:41`） | `ledger-report`（+ 对 `SOURCES.md` 生成区的对账） | 有（对象问题见 E1-7） |
| **按需 A2 装配降级（`closure.md:42`）** | **（无新 artifact；装配说明写在任务卡里）** | **0 文档，且是原文声明**——不是漏洞，但它是唯一"无独立交付物"的单元 |

**结论**：**主链 0–8 每环都有产出物**；唯一无独立产物的是 A2，其原文已声明降级为 task-card 内字段（`closure.md:42`）。若把"某角色在环内的隐含产物"（如 #19 证据材料、#21 现场包）也算作环节交付物，则问题从异常表 2 转到异常表 1——即**产物存在但没被命名/没被安排环节与落点**，而不是"环节空转"。

---

## 5. 统计（供交审）

- **A 总数 24 项**：主链/按需角色产出 15 项 + 派生记录 8 项 + 库自身 1 项。
- **类别**：承重证据 13 项、过程记录 11 项。
- **异常表 1（有文档、无产出环节）7 条**：E1-1 manifest、E1-2 范围声明、E1-3 授权记录本体、E1-4 决策台账/该批决策记录、E1-5 现场包、E1-6 项目词汇表/ADR 更新、E1-7 `SOURCES.md` 生成区（下游对象缺失）。
- **异常表 2（有环节、无文档）0 条**；唯一例外 A2（`closure.md:42` 声明）。
- **落点规定现状**：24 项中 **13 项"无"**（#1、2、3、4、5、6、7、11、13、14、15、18、21）；有落点/部分落点的 11 项全部是**规则片段**（"承重证据路径要写清""生成区不得手工编辑""范围声明要一起交"），**没有任何一项规定"存在哪个目录、以什么文件名、由谁保管"**。
- **合计 18 项至少缺一类**：无落点 13 项 ＋ 无产出环节 7 条，其中 #18（授权记录）与 #21（现场包）同时缺两类（13＋7−2＝18）。
