# pipeline.md · Driver 唯一读的流程

本文件只回答三件事：**谁在什么时候把什么交给谁**、**什么时候必须停**、**什么时候可以复用旧结论**。主链是：调查 → 设计 → 切片 → 实现 → 审查 → 验证 → 集成。
工程方法不在这里——每个角色的方法在自己那份角色文件里。角色文件的 `§2 我收到什么` / `§3 我必须交出什么` 与本文件的交接物名称必须逐字一致。

## 1. 交付链

```
task-card ─→ investigation-report ─→ design-proposal ─→ slice-plan ─→ candidate
                                   └─→ planner 也可直接收 design-proposal 产出 slice-plan
candidate ─→ review-verdict ─→ verification-evidence ─→ integrated-baseline ─→ roundup（交 Owner）
architect / reviewer ─→ pending-question ─→ Driver ─→ oracle-ruling
```

单张卡也可直送下游（Driver → 任意角色），上图只是主链。**记录侧另有一条边，不参与实现与判断链**：每批改动落盘后 `Driver → ledger-input → 台账管理员 → ledger-report → Driver`（见 §11 与 `closure.md` A3 行）。它只对齐台账的派生视图，不产生、不放宽、不否决任何判断结论。

| 步 | 角色 | 收 | 交 |
|---|---|---|---|
| 0 | Driver | `owner-brief` | `task-card`、`pending-question`、`roundup` |
| 1 | `roles/investigator.md` | `task-card` | `investigation-report` |
| 2 | `roles/architect.md` | `investigation-report`、`task-card` | `design-proposal` |
| 3 | `roles/planner.md` | `design-proposal`、`investigation-report` | `slice-plan` |
| 4 | `roles/implementer.md` | `slice-plan`、`design-proposal`、`task-card` | `candidate` |
| 5 | `roles/reviewer.md` | `candidate`、`slice-plan`、`design-proposal` | `review-verdict` |
| 6 | `roles/verifier.md` | `candidate`、`review-verdict` | `verification-evidence` |
| 7 | `roles/integrator.md` | `verification-evidence`、`candidate`、`review-verdict` | `integrated-baseline` |
| 按需 | `roles/oracle.md` | `pending-question`、`candidate` | `oracle-ruling` |

角色文件 §2/§3 里每份交接物都列了**必需字段**；字段缺哪一条，接收方不得开工。

## 2. 装配档位

按"项目成熟度 × 本次变更风险"选档；不按文件数选。**档位口径 = 工作会话数**（作者侧 + 判断侧）；**Driver 的承载单列、不计入档位**。承载三选一，必须在装配说明里显式声明：① Owner 亲自；② 独立轻量编排会话；③ **仅限 `trio`/`full`**：作者侧之一兼任——**且仅当它不是实现该候选的人**。

| 档位 | 工作会话 | 归并 | 「Driver 是独立会话」 |
|---|---|---|---|
| `solo(1)` | 1 | 一个作者会话顺序兼任调查 / 设计 / 切片 / 实现 | **不满足**（只能走承载 ①：Owner 亲自）。**本档位可用，但必须由 Owner 明确接受这一条降级**；不接受就改用 `trio(3)` |
| `trio(3)` | 3 | A = 调查 + 设计 + 切片；B = 实现；C = 审查 + 验证 + 集成 | **满足**（承载 ② 或 ③；走 ③ 时兼任者不得是实现该候选的人） |
| `full(9)` | 9 | 每角色一个会话 | **满足**（三者皆可） |

判断侧不计在作者侧档位里：`solo(1)` 也仍需**另起**审查/验证会话；Oracle 按触发条件启用，且不得落在产出争议对象的会话里。

高风险触发条件（命中任一即上独立复核，不因档位低而取消）：改变接口含义 / 状态归属 / 权限 / 数据语义；存在两个以上自洽方案；角色之间对方案或判据有争议；宣布"已闭合"前的关键分叉。

## 3. 不可合并的边界（硬规则）

1. **实现者 ≠ 判断者。** 同一个人不得既产出某个候选，又对那个候选给出审查或验证结论。任何档位都不放宽。
2. **Driver 不实现。** 它可以划范围、排序、发卡、交接，不写产线实现。
3. **集成只有一个写者。** 同一时刻只有 Integrator 写目标基线。
4. **Oracle 不产生 Owner 权限。** 它只在已冻结契约范围内裁决；范围内没有答案就写"需要 Owner"。
5. **判断者不得由本人放宽判据。** 判据不足由 `roles/planner.md` 补，不由审查/验证方临时放宽。
6. **不可兼任的组合（任何档位不放宽）**：`Driver × Implementer`（`solo(1)` 成立的前提就是 Driver 由 Owner 承担）｜`Driver × 任一判断角色`｜`Implementer × 任一判断角色`（产出该候选的会话不得审查/验证/复核它）｜`Oracle × 争议对象的产出方`。违反任一条：该轮结论**无效**，记 `UNVERIFIED`。
7. **能力缺失只降结论等级，不降纪律要求。** 环境开不出独立会话时（由 Driver 检测并声明）：本轮所有判断类结论最高只能是 `UNVERIFIED`，或由 Owner 明确书面接受风险；**不得记为 `PASS`**，也不得由实现该候选的人自己判断。

## 4. 四类依赖

每条前置边必须标明它在等哪一类；四类解除条件不同，**不能用"等上游完成"代替**：

| 类型 | 解除条件 |
|---|---|
| `接口冻结` | 上游交出确定的接口/契约，消费者可据此开发 |
| `写权释放` | 上游停止写这些文件/符号，并把写权交出去 |
| `资源可用` | 数据库、端口、进程、依赖目录、外部配额可用 |
| `证据资格` | 上游结论的对象/环境/覆盖范围足以支持下游要引用的那条断言 |

下游只等它**实际依赖的最小前提**。上游拿了 PASS 不等于四类都满足。

## 5. 并行批处理

对批内每一项，逐项问四个问题：

1. 是否与别项共同决定**同一字段、状态、权限、接口**？
2. 是否落在**同一文件或同一公共符号**上？
3. 是否共享**可写资源**（数据库、端口、进程、目录、配额）？
4. 是否**等同一未冻结接口**？

按答案分类：

| 类 | 特征 | 推进方式 |
|---|---|---|
| **A 互不相干** | 四问全否 | 实现 / 审查 / 验证三路并发，只在**合并处**排队 |
| **B 共享字段/状态/权限** | 问 1 是 | 先定唯一 owner 与最小接口；消费者在接口冻结后开工 |
| **C 共享文件/符号** | 问 2 是 | 一个写者，或明确交权的串行窗口 |
| **D 共享资源** | 问 3 或 4 是 | 分离资源；不能分离则排队 |

**被串行化的只有写窗与合并，不是流水线。** 审查方与验证方在候选固定后可以并行工作，在合并处汇合；任一侧阻断即停止晋升。

## 6. 写窗

1. 候选**冻结**后，发出交付通知，等**接收确认**。
2. 收到确认才交权；交出后原写者停止写这些文件。
3. **定向返修 = 新候选 + 新冻结**：新候选生成时显式通知审查方与集成方——旧候选退出队列、旧结论不自动延续、轮次不因换候选或换人重置。
4. 审查期间候选保持冻结；不在这期间"顺手改一下"。

## 7. 停止与归因（两种不同事件，不是通用轮次表）

| 事件 | 判据与上限由谁守 | 接手人 |
|---|---|---|
| 同一**前提、同一道判据、无新证据**的重复失败（诊断 / 修复链） | `roles/investigator.md §4.6` 的停手条件；共享前提的写下与按 actor 清点由它执行 | `roles/investigator.md` 重新归因；判据不足 → `roles/planner.md`；范围 / 授权 → `roles/driver.md` |
| 同一候选审查两轮仍有 blocker（审查链） | `roles/reviewer.md §4.7`；**两轮硬规定**，不因候选版本或人员变化重置，**也不得被装配参数覆盖或放宽** | 升级给独立复核或设计方（`roles/driver.md` 按 §4.7 判触发条件） |

两种事件的读数不同，不共用"轮次"默认值；停下后打包现场、已排除的解释与证据指针，**不许发第三个同前提补丁**；停止不影响已交付部分。

## 8. 证据复用判据

复用旧结论来支持新交付，四条必须同时成立：

1. 记录可取回，且那次运行有效；**"可取回"包含其承重夹具/原始读数仍可取回、位置未失效**——只剩摘要或已不存在的 `/tmp` 路径，不得复用为 `PASS`；2. 它实际覆盖了本次的目标断言与边界；3. 相关实现 / 检查 / 运行设施未变，或变化已证实在依赖范围之外；4. 当前判定没有改变该断言的正确答案。

**执行者是否换人不在判据里。** 换人复跑同一条确定性检查不会自动增加覆盖，也不自动升级证据等级。

基线移动时，按第 2、3 条**只补受影响项**——不写"基线一动前序结论全部作废"。

## 9. 波次汇合

一个批次交付前，必须在**合并后的候选**上走一次**旅程级验收**：完整用户旅程、关键路径、真实入口。

- 各项各自 PASS 的集合 **不等于** 交付；服务健康检查、固定字节相同、任务全绿，都不能替代这一步。汇合失败：原节点记为"集成后验证失败"，新增下游修复任务；**不画回边、不重置原对象**。

## 10. 授权检查

**每一步推进前，先看当前有效授权。**
- 授权记录必须包含：谁授权、批的是什么对象（计划摘要 / 具体候选身份是两类对象）、条件、有效期、以及执行方的接收确认。
- 未被授权的交接，**停在交付点**：不推进、不代签、不默认延续。
- 授权或范围被改：通知所有受影响的任务并取得确认；旧任务继续持有旧决定比新增一个文件更危险。
- 超出授权范围的问题：保留问题，继续推进无依赖的已授权部分；需要越权时交 Owner，不自行扩权。
- **推进前说明不产生授权**：一批任务首次派出、写窗开放、目标 / 范围 / 风险实质变化之前应当说明；**唯一硬线：跨过「开始实现」这条线之前必须已用自然语言对齐**。**送达 ≠ 批准**；细节在 `roles/driver.md §4.9`。

## 11. 机器可读的交接拓扑

下面这段是本节唯一的交接拓扑来源；角色文件 §2 的收据必须与它一致。每一步的字段级对应、以及“某一环被跳过时谁承接”见 `closure.md`。

```pipeline
owner -> owner-brief -> driver
driver -> task-card -> investigator, architect, implementer
driver -> pending-question -> oracle
driver -> investigation-report -> architect, planner, implementer
driver -> slice-plan -> implementer
driver -> equivalence-proof -> reviewer, verifier, implementer
driver -> roundup -> owner
investigator -> investigation-report -> architect, planner, implementer
architect -> design-proposal -> planner
architect -> pending-question -> driver
reviewer -> pending-question -> driver
planner -> slice-plan -> implementer
implementer -> candidate -> reviewer, verifier, integrator
reviewer -> review-verdict -> verifier, implementer
verifier -> verification-evidence -> integrator
integrator -> integrated-baseline -> driver
oracle -> oracle-ruling -> driver
reviewer -> oracle-ruling -> driver
driver -> ledger-input -> ledger-custodian
ledger-custodian -> ledger-report -> driver
```
