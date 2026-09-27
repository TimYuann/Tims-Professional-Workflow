# Round 1 · §4 来源忠诚度审查（冻结工作树）

对象：冻结摘要 `86dc6d75872f63d9ae97f17db86b9f40a4bfab697f949b0ae39618b35682189e`；本表先于交付方自述/Arbiter 审查制作。

**计数规则**：对 `investigator` / `reviewer` / `oracle` 的每个 `### 4.x`，按一条触发条件、每条编号步骤、一条判断依据、每条反例/不适用各计一个“主张单元”；编号步骤内的小分句作为同一单元核（任一承重分句找不到依据，整单元不忠实）。`oracle §4.1` 的 4 条触发列表也作为编号步骤计。此规则共 **N=208；可与上游原文或 Owner 在 `.pi/round1/TASK.md` 的直接要求对应 M=191；不忠实/缺合规来源 K=17**。M 包含任务卡直接规定的 Oracle 边界，并不暗称这些边界来自某一个上游；K 中包含既有引用不支持其说法的单元，以及唯一可找到的来源是下游只读消费方、却被当作“三仓吸收”的单元。一个单元由多个句子组成，统计不能冒充逐句机械证明。

| 角色/单元范围 | N | K | 主要比对依据及不忠实处 |
|---|---:|---:|---|
| Investigator 4.1 | 10 | 0 | matt `skills/engineering/diagnosing-bugs/SKILL.md:18-67`；能判红、已跑、不能跑即停；适用条件保留。 |
| Investigator 4.2 | 8 | 0 | 同上 `:68-85`；复现原始症状与最小化。 |
| Investigator 4.3 | 11 | 0 | pstack `skills/how/references/explorer-prompt.md:21-55`；入口/流/抽象/边界/反常与未知。 |
| Investigator 4.4 | 11 | **1** | pstack `skills/why/SKILL.md:36-48,65-125,140-146`、`references/epistemics.md:7-75,98-144`；见 I-1。 |
| Investigator 4.5 | 11 | **1** | matt `diagnosing-bugs/SKILL.md:88-112`；见 I-2。 |
| Investigator 4.6 | 9 | 0 | pstack `skills/principle-attack-the-premise/SKILL.md:9-23`，同前提同判据后按 actor 清点。 |
| Investigator 4.7 | 9 | 0 | matt `diagnosing-bugs/SKILL.md:114-138`、pstack `why/SKILL.md:146`、任务卡的仅交事实边界。**但**来源台账另称已吸收约束集、产物漏了它，见 L-1。 |
| Reviewer 4.1 | 10 | **3** | 固定对象及真实检查来自 pstack `principle-prove-it-works/SKILL.md:9-23`；第 4–6 步额外发明的符号集合/剥注释等价法既无三仓来源也无实测，见 R-1。 |
| Reviewer 4.2 | 9 | 0 | addy `doubt-driven-development/SKILL.md:75-107,168-180`，保留 artifact + contract、去掉作者论证。 |
| Reviewer 4.3 | 13 | 0 | addy `doubt-driven-development/SKILL.md:85-107`、pstack `interrogate/references/rubric.md:3-68`，步骤允许逐条排除不适用镜头。 |
| Reviewer 4.4 | 8 | 0 | 任务卡按因返工/阻断分栏；addy `doubt-driven-development/SKILL.md:168-180` 的契约误读/可改/取舍/噪声归类。 |
| Reviewer 4.5 | 9 | 0 | Owner `.pi/round1/TASK.md §3 Oracle` 的反实现挑战以及 pstack `principle-test-behavior-not-implementation/SKILL.md:9-25`；严格适用高风险。 |
| Reviewer 4.6 | 11 | **11** | 七形态、触发、判断和两条反例的**唯一明确出处**是下游只读 `docs/active/multi-agent-development-principles.md:288-298`，由 `SOURCES.md:400-401`（§6 消费者契约）承认；三仓台账未给 `roles/reviewer.md §4.6` 任何上游锚点，也未附本人实测命令输出。见 R-2。 |
| Reviewer 4.7 | 10 | **1** | `SOURCES.md:217` 把 addy `doubt-driven-development/SKILL.md:181-192` 映到此处；上游写 **3 cycles**，角色在 `roles/reviewer.md:165` 写 **两轮**，又在 `:169` 写 **三轮**。见 R-3。 |
| Oracle 4.1 | 11 | 0 | 四条触发由 `.pi/round1/TASK.md §3` 逐项规定；不是借上游伪造触发。 |
| Oracle 4.2 | 9 | 0 | addy `doubt-driven-development/SKILL.md:75-107` 的产物+契约、不传 CLAIM；任务卡对同模型输入隔离的要求。 |
| Oracle 4.3 | 10 | 0 | 任务卡固定三件套、区分性实验；matt `diagnosing-bugs/SKILL.md:88-98` 支持因果预测句（仅对因果类争议）。 |
| Oracle 4.4 | 7 | 0 | pstack `why/references/epistemics.md:46-59,112-135` 的未知/互斥证据；任务卡明确不可区分。 |
| Oracle 4.5 | 8 | 0 | Owner `.pi/round1/TASK.md §3` 直接规定反实现挑战。 |
| Oracle 4.6 | 7 | 0 | Owner 定的独立职责与实现/判断隔离。 |
| Oracle 4.7 | 9 | 0 | Owner 明定 fresh Reviewer 替代及无独立会话不能 PASS。 |
| Oracle 4.8 | 8 | 0 | Owner 明定不得当唯一闸、不得替授权、不得豁免验证、不得背书。 |
| **合计** | **208** | **17** | **M=191**（包含直接来自 Owner 的要求）；下面给出每个 K 的精确位置与证伪点。 |

### 不忠实 / 无合规来源的单元

- **I-1：`roles/investigator.md:103`**：“只有‘直接’才可以用‘因为’”；pstack `why/references/epistemics.md:63-69` 的原文是 **Direct or Supported** 可用这一类有证据的因果词。比上游收窄了一个档位，`SOURCES.md:36` 却称“保留规则”；应标为 TIM 的主动收紧，而不是引用忠实复述。
- **I-2：`roles/investigator.md:122`**：把假设排序交给下游 Planner/Implementer “看一次”，但 matt `diagnosing-bugs/SKILL.md:88-98` 要的是 **show ranked list to the user before testing**（人可凭领域知识重排），虽允许不阻塞；`SOURCES.md:160` 声称保留原规则，却改变接收者且没说理由。Owner 用户决策与同伴接手不等价。
- **R-1：`roles/reviewer.md:54-59`**：第 4–6 步以符号集合相同作为重命名/搬文件等价证明，把注释/空行剥除后逐字相同作为注释删除证明；`SOURCES.md` 未列任何三仓对应来源，也未附实测。**最小反例已运行**：`def authorized(): return True` → `False` 的两个字符串，函数符号集合均为 `{'authorized'}`、差集 `[]`，行为却从 `True` 变 `False`。因此第 4–6 步不只是未引出处，其放行证明本身不充分（即使卡上先声称“纯重命名”，该证明无法排除顺带的行为变更）。
- **R-2：`roles/reviewer.md:140-155`**：11 个单元全部只能在只读消费方找来源。任务卡 D1 要求角色 §4 每一实质主张给 `upstreams/.../file:line` 或本轮实测命令输出；`SOURCES.md §6` 明说消费方“不是吸收来源”。使用该方法可以有价值，但当前说法不是合规的三仓吸收出处；应先说明 Owner 直接采纳该下游清单、或补可验证的三仓依据/本轮实测，而非暗渡。
- **R-3：`roles/reviewer.md:165,169`**：同节“两轮后停”与“三轮仍无法收敛”相互冲突；上游 addy 是 3 cycles。任务卡对**同一故障无新证据**规定两轮即停，与“审查对象两轮仍有阻断”的含义不同，必须明确选择。单写 `SOURCES.md:217` 映射为“保留三轮”不忠实。

### 台账本身另两处不实（与 N/M/K 分开，不重复计数）

- **L-1 `SOURCES.md:42,312-315`** 反复声称把 pstack `why/SKILL.md:146` 的 Preserve/Change/Avoid/Risk 转成调查交付的“约束集”；但 `roles/investigator.md:28-38` 八个输出字段没有此约束，`roles/investigator.md:154-165` 只说“下一步要验证什么”，也不提供安全承重约束的明确位置。来源存在、落点不在。
- **L-2 `SOURCES.md:300-304`** 把 matt `tdd/SKILL.md:36-38` 读成“交付必须包含生产代码”作为与 pstack `principle-prove-it-works/SKILL.md:9-20` 的冲突；两份原文都**没有**生产 diff 必需的断言。真正存在、但此表没裁的冲突是 matt `tdd/SKILL.md:36-38` **refactoring is not part of the loop** 与 addy `test-driven-development/SKILL.md:38-95` **red-green-refactor**；本库 `roles/implementer.md:72-78` 采了后者，`SOURCES.md:168` 却称采了前者。结果来源、裁决、角色三者不一致。
