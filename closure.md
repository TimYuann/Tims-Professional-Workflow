# closure.md · 闭环矩阵

`pipeline.md` 画的是箭头；本文件回答"**上一环交出的字段，是不是下一环声明需要的字段**"，以及**每一环被跳过时谁交出什么**。

读法：**主链**表逐行相邻（第 N 行的输入字段必须逐字出现在第 N−1 行的输出字段里）；**按需与降级**表不参与相邻校验，它的输入字段只需出现在主链任一行的输出字段或任一角色文件 §2 声明的字段里。
字段名来自各角色文件的 `§2 我收到什么` / `§3 我必须交出什么`，逐字一致。

**跳过的规则**：每一环被跳过时，**下一环要收的收据必须完整地被交出来**——由谁产出、字段全集、判定条件三样都要写清。
**只移交"职责"不算通过**：字段缺一条，接收方按自己 §2 就有权拒收。填不出完整收据的路径**不得标"可跳过"**。

## 四条必答的可跳过路径

| 路径 | 完整替代收据（产出方 + 字段全集 + 判定条件） |
|---|---|
| 跳过调查（**只允许"本次没有待解释的现象"**） | `roles/driver.md` 代产 `investigation-report`，**十二个字段一个不能少**（`symptom` `entry_point` `first_divergence` `root_cause` `hypotheses` `confidence` `coverage` `not_proven` `repro_command` `repro_fixture` `red_point` `constraints`）；`repro_*` 三列写「不适用（无现象）」。**「根因已明」不再是跳过理由**——那是猜测，不是事实 |
| 跳过设计（局部改动） | **只能由 `roles/architect.md` 产出最小形式的 `design-proposal`**（十字段全填；`alternatives` 至少要给「维持现状」对照 + 一个候选）——它本来就是该产物的生产者。**`roles/planner.md` 不得代产**（它只切分、不重新设计）。任一字段填不出 → 该路径**不可跳过**，走完整设计。**跳设计不取消独立复核** |
| solo 档（作者侧只开一个会话） | `roles/driver.md` 装配 + `roles/reviewer.md` 承接判断：**Driver 由 Owner 亲自承担**，判断侧另起短命会话；**不得由实现该候选的人承接任何判断**。Owner 不承担 Driver 时该档位不成立 |
| 没有第二模型 / 没有独立复核会话 | `roles/reviewer.md`（另一会话、不读作者叙述、只读产物与冻结契约）交出完整 `oracle-ruling`：`question` `frozen_contract` `ruling` `basis` `distinguishing_experiment` `undecided`。**不得由实现者本人承担** |
| 连一个能做独立复核的会话都开不出来 | **能力缺失只降结论等级**：`state` 记 `incomplete`，判断类结论最高 `UNVERIFIED`，或由 Owner 明确书面接受风险；**不得记 `PASS`**（`pipeline.md §3` 第 7 条） |

## 主链（相邻校验）

| # | 环节 | 承接角色 | 输入字段（= 上一行输出，逐字一致） | 附加输入（来自更早环节） | 输出字段 | 可跳过条件 | 跳过时职责移交给谁 |
|---|---|---|---|---|---|---|---|
| 0 | 发卡 | `roles/driver.md` | （来自 Owner，无上一行） | — | `goal` `symptom` `scope` `authorization` `auth_record` `dependencies` `verification` `escalation` | 不可跳过（每批必做） | — |
| 1 | 调查 | `roles/investigator.md` | `goal` `symptom` `scope` `authorization` `dependencies` | — | `symptom` `entry_point` `first_divergence` `root_cause` `hypotheses` `confidence` `coverage` `not_proven` `repro_command` `repro_fixture` `red_point` `constraints` | 只有「本次没有待解释的现象」（主动改造） | `roles/driver.md` 代产与 `investigation-report` **完全同字段**的收据（`symptom` `entry_point` `first_divergence` `root_cause` `hypotheses` `confidence` `coverage` `not_proven` `repro_command` `repro_fixture` `red_point` `constraints`）；`repro_*` 三列写「不适用（无现象）」；**填不出实质性内容就不得跳过**（「根因已明」不是理由） |
| 2 | 设计 | `roles/architect.md` | `symptom` `entry_point` `first_divergence` `root_cause` `confidence` `coverage` `constraints` | 0→`goal` `scope` `authorization` | `caller_usage` `data_shapes` `alternatives` `red_flag_screen` `invariants` `change_cost` `open_questions` `chosen_shape` `approved_by` `bound_contract` | 不改变接口形态 / 状态归属 / 权限 / 数据语义的局部改动 | `roles/architect.md` 产出**最小形式**的 `design-proposal`（`caller_usage` `data_shapes` `alternatives` `red_flag_screen` `invariants` `change_cost` `open_questions` `chosen_shape` `approved_by` `bound_contract` 十字段全填；`alternatives` 至少含「维持现状」对照）；填不出 → 该路径不可跳过。**`roles/planner.md` 不得代产**。跳设计不取消独立复核 |
| 3 | 切片 | `roles/planner.md` | `caller_usage` `data_shapes` `alternatives` `invariants` `change_cost` `chosen_shape` `approved_by` `bound_contract` | 1→`symptom` `root_cause` `confidence` `coverage` | `slices` `dependencies` `verification` `scope` `stop_condition` | 单片、无依赖、判据显然 | `roles/driver.md` 代产完整 `slice-plan`（`slices` `dependencies` `verification` `scope` `stop_condition` 五字段全填）；填不出 → 不得跳过，转 `roles/planner.md` |
| 4 | 实现 | `roles/implementer.md` | `slices` `verification` `scope` `dependencies` `stop_condition` | 2→`caller_usage` `data_shapes` `invariants`；0→`authorization` `auth_record` `verification`；1→`repro_command` `repro_fixture` `red_point` | `base` `tree` `diff` `self_verification` `not_touched` `residuals` | 不可跳过 | — |
| 5 | 审查 | `roles/reviewer.md` | `base` `tree` `diff` `self_verification` `not_touched` `residuals` | 3→`slices` `verification` `scope`；2→`caller_usage` `invariants` `change_cost` | `object` `state` `findings` `blocking` `coverage` `residuals` | **不可跳过**（可走**快速等价审**：复用 `equivalence-proof` 缩短工作量，但必须交出字段齐全的 `review-verdict`；`equivalence-proof` 不得单独充当 `review-verdict`） | `roles/driver.md` 提供 `equivalence-proof`（`object` `proof_command` `proof_output` `covered_set` `validator`，`validator` 必须是非实现者）作为快速审的输入；`roles/reviewer.md` 仍须交出完整 `review-verdict`（`object` `state` `findings` `blocking` `coverage` `residuals`）。**`roles/implementer.md` 永不承接本行** |
| 6 | 验证 | `roles/verifier.md` | `object` `state` `blocking` `coverage` | 4→`base` `tree` `self_verification` `residuals` | `object` `state` `environment` `commands` `result` `falsification` `noise` `uncovered` | 不可跳过；无运行时行为的改动**退化为静态形态**，但八字段仍要完整交 | — |
| 7 | 集成 | `roles/integrator.md` | `object` `state` `environment` `commands` `result` `falsification` `uncovered` | 4→`base` `tree` `diff`；5→`object` `blocking` | `base` `tree` `conflicts` `combination_check` `post_merge` `reused_evidence` | 不可跳过；基线未移动时组合检查可记录为「已就地验证 + 命令与输出指针」，但六字段仍要完整交 | — |
| 8 | 收口 | `roles/driver.md` | `base` `tree` `conflicts` `combination_check` `post_merge` `reused_evidence` | 1→`symptom` `root_cause` `confidence` `not_proven`；按需→`ruling` `basis` `distinguishing_experiment` `undecided` | `delivered` `not_delivered` `evidence_pointer` `open_decisions` | 不可跳过（每批必做） | — |

## 按需与降级（不参与相邻校验）

| # | 环节 | 承接角色 | 输入字段 | 附加输入（来自哪一行） | 输出字段 | 可跳过条件 | 跳过时职责移交给谁 |
|---|---|---|---|---|---|---|---|
| A0 | 提问与转手 | `roles/driver.md` | `question` `frozen_contract` `options` `evidence_pointer` `requested_by` | 2→`caller_usage` `alternatives` `invariants` `change_cost`；5→`object` `blocking` `coverage` | `question` `frozen_contract` `options` `evidence_pointer` `requested_by` | **不可跳过**（每轮提问必经此处；但可能被判为「未触发」而不进入 A1） | 命中触发条件 → 转 `roles/oracle.md`（A1）；**一条都不命中 → `roles/driver.md` 记录「未触发 + 理由」并把问题退回原角色**，不得记成「已复核」 |
| A1 | 独立复核 | `roles/oracle.md` | `question` `frozen_contract` `options` `evidence_pointer` | 4→`tree` `diff` `self_verification`；2→`caller_usage` `alternatives` `invariants` `change_cost` | `ruling` `basis` `distinguishing_experiment` `undecided` | 四条触发条件一条都不命中 | `roles/reviewer.md`（另一会话、不读作者叙述、只读产物与冻结契约）承接同一职责，仍要交出 `question` `frozen_contract` `ruling` `basis` `distinguishing_experiment` `undecided` 六字段；**不得由实现者本人承担** |
| A3 | 台账对账 | `roles/ledger-custodian.md` | `changed_files` `key_set` `batch_id` | 4→`diff`；2→`design-proposal` | `region_diff` `broken_keys` `moved_steps` `regenerated_at` | 不可跳过（每批改动落盘后重跑生成器） | — |
| A2 | 装配降级 | `roles/driver.md` | `goal` `scope` `authorization` | — | （无新 artifact；装配说明写在任务卡里） | 工作会话数不足以支撑 `trio(3)`，且 Owner 愿意亲自承担 Driver | `roles/driver.md` 写装配说明 + `roles/reviewer.md` 承接判断：solo 只压缩**作者侧**（调查 / 设计 / 切片 / 实现可同会话顺序执行），**判断侧必须另起会话**；实现该候选的人不得承接审查、验证或复核。若连一个能做独立复核的会话都开不出来：`state` 记 `incomplete`，判断类结论最高 `UNVERIFIED` 或由 Owner 明确书面接受风险，**不得记 `PASS`** |

## 维护规则

- 本表字段与角色文件不一致时，**以角色文件为准**，并同步修正本表；`scripts/check-library.py` 会同时检查两处（矩阵内部相邻关系、矩阵 ↔ 角色 §2/§3 的字段归属）。
- 新增角色或新增交接物时，必须补一行并写明"可跳过条件 / 跳过时谁交出什么"；**没有完整替代收据的路径不得标"可跳过"**。
