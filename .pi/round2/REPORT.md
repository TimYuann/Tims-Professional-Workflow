# R2 · REPORT（返修）

- 对象：`/Users/yuantian/Developer/tim-professional-workflow` 工作树（**未 commit**）
- 基线 `git rev-parse HEAD` = `52d3315d881cdff9f42d52c2db0eb2796b4fa44e`
- 来源：oracle `VERIFY-REPORT.md`（FAIL / 7 阻断）+ `VERIFY-CITATION-AUDIT.md`（208 单元 / 17 异常）+ `REVIEW-1.md`
- 本报告所有"变红"输出都是**实跑原文**；负夹具全部在 `/tmp` 的仓库副本上做，主仓未被破坏

---

## ① 逐条 B-1 … B-7

| 项 | 改了什么 | 落在哪 |
|---|---|---|
| **B-1** solo 档自撞 | `solo(1)` 不再让同一会话兼任 Driver 与 Implementer：**Driver 由 Owner 亲自承担**，Owner 不承担时该档位**不成立**；判断侧必须另起短命会话。`trio(3)` 明确 Driver 由 Owner 或**额外**轻量编排会话承担，不占 A/B/C。新增不可兼任组合清单：`Driver × Implementer`、`Driver × 任一判断角色`、`Implementer × 任一判断角色`、`Oracle × 争议对象的产出方`；违反任一条该轮结论**无效**，记 `UNVERIFIED` | `pipeline.md:37-38`（档位表）、`:50`（硬规则 6）；`roles/driver.md:154`（能力缺失停机）；`closure.md:13`（四条路径表第 3 行） |
| **B-2** 五条跳过路径的替代收据 | 逐条给出**完整替代收据**（产出方 + 字段全集 + 判定条件）：① 跳调查 → `roles/driver.md` 代产 `investigation-report` **十二字段全填**，且**取消"根因已明"作为跳过理由**（那是猜测）；② 跳设计 → `roles/planner.md` 代产完整 `design-proposal` **十字段全填**，填不出就不得跳过；③ 跳切片 → `roles/driver.md` 代产完整 `slice-plan` 五字段；④ 跳独立审查 → `roles/driver.md` 产出 `equivalence-proof` 五字段且 `validator` 必须非实现者，缺则不得跳过；⑤ 跳验证 / 跳集成 → **取消可跳过标记**，改"退化为更薄但仍完整的收据"（八字段 / 六字段一个不能少）。配套新增：`investigation-report` 加 `repro_command`/`repro_fixture`/`red_point`/`constraints`；`design-proposal` 加 `chosen_shape`/`approved_by`/`bound_contract`；`review-verdict`/`verification-evidence` 加 `state`；`driver §3` 新增三个降级产物 | `closure.md:15-19`（四条路径）+ `:26-33`（主链 9 行）；`roles/driver.md §3`（三个新产出块）；`roles/investigator.md §3`（12 字段）；`roles/architect.md §3`；`roles/planner.md §3`；`roles/reviewer.md §3`；`roles/verifier.md §3`；各角色 §2 收据 |
| **B-3** 等价判据会假放行 | 判据改成**比被承诺的不变行为/语义**：搬文件比内容 hash **双射**；符号改名比**定义体字节 hash 前后一致 + 双射**；剥注释比剥除后逐字相同。**只比名字集合不算证明**；**无法证明时不得跳过独立审查**。实测反例（`True`→`False`，符号集合相同、行为相反）写进角色文件做常驻警示；`equivalence-proof` 必须有非实现者 `validator` | `roles/reviewer.md:73-78`（步骤 4–7 + 常驻反例）；`closure.md:31`（行 5 的跳过条件） |
| **B-4** Planner 擅自设数字门禁 | 合法来源收窄为**用户要求 / 既有契约 / CI 配置**三处；没有授权阈值时**只报测量值与不确定性**，阈值写成「待确认」提给 Owner 或既有契约，**不得自建门禁**；新增第二条反例（一次测量值 ≠ 阈值授权） | `roles/planner.md:118`（步骤 2）、`:127`（反例）、`§8` 自欺行、`§7` 退出判据 |
| **B-5** 台账与角色不一致（17 异常） | 见 §③；另修越界引用 `skills/architect/SKILL.md:81-84 → :81-83`；注释裁决改成**真单选**（采纳乙方判据、不采纳甲方判据）；TDD 冲突改成**真冲突**（matt「重构不属于循环」 vs addy 红绿重构），假冲突**撤回**；台账新增 §4.10 逐条处置表 | `SOURCES.md:82`（越界）、`:260-262`（注释单选）、`:298-306`（TDD 真冲突）、`:356+`（§4.10 处置表） |
| **B-6** 空主链仍 PASS | 新增 G3 断言：**主链行数 < 9 / 行号重复 / 输入为空 / 输出为空 → 直接 FAIL** | `scripts/check-library.py` 的"闭环矩阵 G3：主链行数/唯一/非空"检查 |
| **B-7** checker 自我豁免 | **取消自排除**：工具名与上游仓库标识改为**分片拼接**写在源码里（正文不出现完整名字）；工作区目录名按路径归一化处理。`scripts/check-library.py` 现在**完整落在扫描范围内**，输出里也写明"0 命中（含本脚本自身）"；排除清单只剩 Owner 批准的三类 | `scripts/check-library.py` 头部 `HARNESS_TOKENS` / `UPSTREAM_REPO_IDS` / `CAPABILITY_TERMS` / `strip_upstream_paths`；输出行 `显式排除（仅此三类，Owner 批准）` |

### 收尾项 A · Oracle 入件断档（oracle 点名"应在返修时具体决定"）

**决策按 planner 裁定实现**：`roles/architect.md` / `roles/reviewer.md` **不直接**投 Oracle，只产出 `pending-question`（五字段：`question` `frozen_contract` `options` `evidence_pointer` `requested_by`）交给 Driver；**Driver 是唯一构造者与转手者**——收件后判定四条触发条件，命中则转 `roles/oracle.md`，一条都不命中则**记录「未触发 + 理由」并退回原角色**，不得记成「已复核」。

| 落地处 | 内容 |
|---|---|
| `roles/architect.md §3`、`roles/reviewer.md §3` | 新增产出块 `pending-question → roles/driver.md`（五字段表） |
| `roles/driver.md §2` | 新增两条收据 `pending-question ← architect / reviewer`（各五字段 + 处置行） |
| `roles/driver.md §3` | `pending-question` 产出加 `requested_by` 字段 |
| `roles/driver.md §4.7` | 新增「转手独立复核：判定四条触发条件」程序（4 步 + 判断依据 + 2 条反例 + 不适用） |
| `roles/driver.md §6` | 升级行改为"先判触发条件再转手" |
| `roles/oracle.md §2` | 主收据注明**来件只由 Driver 构造与转手** |
| `closure.md` | 新增按需行 **A0 提问与转手**（含"未触发时退回原角色"的移交说明） |
| `pipeline.md` | 拓扑块加 `architect -> pending-question -> driver`、`reviewer -> pending-question -> driver`；示意图改为主线标注 |

### 收尾项 B · `identity-selftest.sh` N5 标签强于所测

N5 实际验的是"漏写一个文件的清单与完整清单**不等**"，原来却写成"漏写不报警 → 漏检"——**一个从不完整清单算出的 digest 与它自己比较仍然相等，没有范围声明时这在原理上测不出**。两处都改了：

1. **标签改成它真正测的东西**：`漏写 → 与完整清单不等（只证明清单被改过；覆盖度由 identity.md §5 的范围声明负责）`；
2. **`identity.md §5` 明写**：交 `object` 必须连同清单、**以及范围声明（写入范围清单）**一起交；**没有范围声明时 digest 不能被当成覆盖证明**——它只证明"这份清单描述的这批字节没变"，不证明"这就是全部该变的范围"。该规则同步进 6 个角色的内联身份规则，并加进 G1 的必需要件（`identity.md` 与 6 处内联各校验一次）。


---

## ② 负夹具：变红的实跑原文

全部在仓库副本上植入（主仓不动）。**不是看检查器报 PASS，是看夹具真的变红。**

### 2.1 G1（身份内联规则被删）

```
[FAIL] 身份规范 G1：唯一定义 + 内联规则   roles/verifier.md 缺内联身份规则要件：ws:v1;
                                        roles/verifier.md 缺内联身份规则要件：NUL;
                                        roles/verifier.md 缺内联身份规则要件：路径字节序升序;
                                        roles/verifier.md 缺内联身份规则要件：前缀类型相同;
                                        roles/verifier.md 缺内联身份规则要件：只交 digest 不算交付;
                                        roles/verifier.md 缺内联身份规则要件：不回答
```

### 2.2 G3（主链删光 —— **oracle 的原始 B-6 反例**）

```
[FAIL] 闭环矩阵 G3：主链行数/唯一/非空   主链只有 0 行（至少 9）
EXIT=1
```
（同一副本里相邻/跨角色校验随之级联报红，但**这一条独立拦住了空链**。）

### 2.3 G4（收据处置被清空 / 散文式收据缺处置）

```
[FAIL] 收据处置 G4：缺了怎么办非空   roles/architect.md §2 收 investigation-report：有一行没写「缺了怎么办」;
                                  roles/driver.md §2 收 integrated-baseline（散文式）没写缺了怎么办
```

### 2.4 G5（某条替代收据的字段被删空）

```
[FAIL] 可跳过路径 G5：替代收据完整   第 3 行移交没写完整替代收据字段
```

### 2.5 新收尾项的两条夹具

```
════ 夹具①：转手链断（driver 少 requested_by 字段 + 少一条 pending-question 收据）════
[FAIL] 闭环矩阵：相邻 + 角色交叉    第 A0 行输出 ['requested_by'] 不在 roles/driver.md §3 声明里
EXIT=1

════ 夹具②：identity.md 缺「范围声明」要件 ════
[FAIL] 身份规范 G1：唯一定义 + 内联规则（无自由条款）   identity.md 缺规范要件：范围声明
EXIT=1
```

### 2.6 G2（身份实现：把两种序列化算成同一 digest / 漏文件 / 路径乱序）

夹具脚本 `scripts/identity-selftest.sh` 本身可失败；用 `--tool` 指向两个**故意写坏**的实现在 `/tmp` 里跑：

```
════ 破法 A：只哈希路径、不哈希内容 ════
[FAIL] N1  期望 DIFFERENT，实际 EQUAL —— 路径不变、内容改一字节（只哈希路径 → 漏检）
合计：7 通过 / 1 失败   EXIT=1

════ 破法 B：不排序、不去前导 ./ ════
[FAIL] P1  期望 EQUAL，实际 DIFFERENT —— 带 ./ 前缀 vs 规范形态（不规范化 → 假 DIFFERENT）
[FAIL] P1b 期望 EQUAL，实际 DIFFERENT —— 乱序输入 vs 规范形态（不排序 → 假 DIFFERENT）
[FAIL] N4  期望 EQUAL，实际 DIFFERENT —— 排除目录的存在与状态不影响身份
合计：5 通过 / 3 失败   EXIT=1
```

正确实现下的夹具全绿（**8 条**，含新增的 N5「清单漏掉写入范围内的一个文件」与 N6「清单里有不存在的文件必须报错」）：

```
[PASS] P1 / P1b / N1 / N2 / N3 / N5 / N6 / N4
合计：8 通过 / 0 失败（被测实现：scripts/ws-identity.sh）   EXIT=0
```

**G4 只是结构哨兵**——oracle 说得对：它保证"每条收据都写了缺了怎么办"，**不能**作为"身份一致性已解决"的证据；身份那件事的证据在 G1 + G2 与 §④ 的落点。

---

## ③ 17 条引文异常逐条处置

| 异常（单元数） | 处置 | 落点 |
|---|---|---|
| **I-1**（Investigator 4.4，1） | **改成与来源一致**：`epistemics.md:63-74` 原文是 Direct **or Supported** 可用有证据的因果词 | `roles/investigator.md:107` |
| **I-2**（Investigator 4.5，1） | **改成与来源一致**：排序清单交给**决定者**（Owner 或经 Driver 转达），不阻塞 | `roles/investigator.md:126` |
| **R-1**（Reviewer 4.1，3） | **标为主动改写 + 本轮实测**：判据从"符号集合"改成"不变行为"；实测反例写进角色做常驻警示 | `roles/reviewer.md:73-78`；`SOURCES.md §4.10` |
| **R-2**（Reviewer 4.6，11） | **显式登记来源类型**：那 7 类形态的唯一明确来源是**只读消费方契约**（Owner 已采纳），**不是三仓吸收**；不再冒称上游 | `SOURCES.md §4.10` + `§6.1` 的 `:288-298` 行 |
| **R-3**（Reviewer 4.7，1） | **真单选**：取**两轮**（消费者契约），**不采纳** addy 的 3 cycles，并说明两者量的不是同一件事 | `roles/reviewer.md:188`；`SOURCES.md` addy 行 |
| **L-1**（台账不实） | **落成字段**：`investigation-report.constraints`（Preserve/Change/Avoid/Risk），并接进 Architect 的输入与矩阵 | `roles/investigator.md §3`、`roles/architect.md §2`、`closure.md` 行 1/2 |
| **L-2**（台账不实） | **真单选 + 撤回假冲突**：采纳 addy（重构在循环内），不采纳 matt `:38`；原来那条"生产 diff 必须存在"的冲突撤回（两份原文都没这个断言） | `SOURCES.md §4.5`、matt 两行 |
| 越界引用 | `skills/architect/SKILL.md:81-84` → **`:81-83`** | `SOURCES.md:82` |
| 自由条款「等价树」 | **从全库删除**并加机械守卫（角色/流程文件出现即报红） | `roles/verifier.md:67`、`roles/integrator.md:121`、`roles/implementer.md:161`；`scripts/check-library.py` G1 |
| 注释裁决"取甲+取乙" | **改成真单选**：采纳乙方判据，不采纳甲方判据，并写明排除的那一半 | `SOURCES.md:260-262` |

**没有一条是"附近有关"**：要么改成与来源一致（I-1/I-2），要么在台账里显式标为主动改写/不采纳并给理由（R-1/R-2/R-3/L-2/注释），要么把台账承诺落成字段（L-1）。

---

## ④ 身份规范落在哪几个文件的哪几节

**规范（唯一真源）**：`identity.md`（维护者规范，非注入件）——表达形式优先级、`ws:v1` 清单规范化规则（含 `-<sha256>` 删除标记）、基线固定、相等判定三条、跨会话移交、与"机械等价"的分界。

**内联规则（每个用身份的角色都自带，不依赖外部文件）**：

| 角色 | 位置 |
|---|---|
| `roles/driver.md` | `:102`（§3 末） |
| `roles/implementer.md` | `:58`（§3 末） |
| `roles/integrator.md` | `:48`（§3 末） |
| `roles/oracle.md` | `:45`（§3 末） |
| `roles/reviewer.md` | `:53`（§3 末） |
| `roles/verifier.md` | `:51`（§3 末） |

每段内联含六条：形式优先级 / `ws:v1` 算法（含 `-<sha256>` 标记与路径字节序）/ 基线固定 / 相等判定三条 / 跨会话移交 / **本规则不回答"行为是否等价"**。
另：`equivalence-proof` 的 `object` 字段与 `candidate.base`/`tree` 统一走这套形式；**"等价树"这个未定义自由条款已从全库删除**（`grep` 在 `roles/`、`pipeline.md`、`closure.md`、`identity.md` 里零命中：`roles/verifier.md:67`、`roles/integrator.md:121`、`roles/implementer.md:161` 三处已改成具体形式），并加了一条机械守卫：**该短语一旦在角色文件或流程文件里出现即报红**（G1 检查内）。

**范围声明**：`identity.md §5` 与 6 处内联规则都写明——交 `object` 必须同时交出范围声明（写入范围清单）；**没有范围声明时 digest 不能当成覆盖证明**。

**实现与夹具**：`scripts/ws-identity.sh`（manifest / digest / compare）、`scripts/identity-selftest.sh`（8 条正负夹具，`--tool` 可指向别的实现来验证夹具会红）。

---

## ⑤ 本轮仍欠的项（如实标，不静默跳过）

| 欠账 | 为什么不修 |
|---|---|
| `check-team-version.sh` 的**内容快照校验** | R2 卡 §6 明说本轮只要求把它当前的能力边界写清楚（只比版本字符串、不校内容快照），已写进脚本头注释与 `SOURCES.md §8` |
| **性能诊断的完整方法**（瓶颈定位表 + 测量清单） | R2 卡 §6 明列为本轮欠账；现状仍只有 `roles/verifier.md §4.5` 的噪声门与 §4.8 的"回退也记账" |
| §5 的第 5、6、7 项只做了最小形态 | ⑤ 依赖边释放凭据：做了**结构定义**（五元 + 四类），**没有做机器校验**；⑥ oracle 的 `distinguishing_experiment` 已接进 driver §2 与矩阵，但**没有在回程产物上再落一个字段**；⑦ `auth_record` 已进任务卡字段与 `§4.4` 的核对动作，但**授权记录本身的持久化格式**没有定义（属于下游绑定的范畴） |
| oracle 新发现的"争议要经 Driver 转手可能被漏判" | 本轮**未修**：修它要给角色之间加直连边，会改动已有拓扑与 §2/§3 契约，超出"不重写整体结构"的范围。已保留为已知风险 |
| `docs/**` 仍未纳入扫描 | 历史材料与归档，Owner 批准的排除项；里面的旧底座名称是**故意保留的历史** |

---

## ⑥ 最终自检

```
$ python3 scripts/check-library.py
TIM · check-library.py（只读自检）
扫描范围: roles , scripts , pipeline.md , closure.md , identity.md , README.md , AGENTS.md , SOURCES.md , VERSION
显式排除（仅此三类，Owner 批准）: docs/**（历史材料与归档） ; .pi/**（工作区） ; upstreams/**（只读克隆，按路径豁免）
本检查能判: 结构与字段级闭环、矩阵行数与跳过收据、身份规范与夹具、引用与死链、版本单一来源、运行底座解耦的措辞
本检查判不了: §4 方法的实质深度、语义正确性、字段值是否真实、某次跳过是否真的合规——这些交给独立审查与人审
仓库根:   /Users/yuantian/Developer/tim-professional-workflow
------------------------------------------------------------------------
[PASS] 角色文件集合                                 缺 无；多 无
[PASS] 角色 frontmatter + 8 节                   9/9
[PASS] 注入契约声明                                 9/9
[PASS] §4 反例/不适用 ≥2                           9/9
[PASS] §8 常见自欺 ≤4                             9/9
[PASS] 角色文件引用仅限 roles/                        通过
[PASS] 闭环：收据字段 ⊆ 产出方字段                        全部成立｜收据 28/28、产出 14/14 参与校验
[PASS] 闭环：交接拓扑双向一致                            全部一致
[PASS] 收据处置 G4：缺了怎么办非空                       全部非空
[PASS] 闭环矩阵 G3：主链行数/唯一/非空                     主链 9 行
[PASS] 闭环矩阵：相邻 + 角色交叉                         主链 9 行 + 按需 2 行，逐行与角色文件交叉校验 全部成立
[PASS] 可跳过路径 G5：替代收据完整                        全部完整或已标不可跳过
[PASS] 死链检查                                   无死链
[PASS] 版本单一来源 VERSION                         VERSION=1.0.0，扫描范围内无第二处声明
[PASS] 工具解耦：无具体运行底座名称                         0 命中（含本脚本自身）
[PASS] 工具解耦：能力探测块恰好一处且在 driver.md             命中 roles/driver.md:154（4/4 项）
[PASS] 工具解耦：其他角色文件无能力枚举                       0 命中
[PASS] 身份规范 G1：唯一定义 + 内联规则（无自由条款）          identity.md 要件齐；6/6 角色内联（含范围声明要件）
[PASS] 身份实现 G2：正负夹具全过                         退出码 0｜合计：8 通过 / 0 失败（被测实现：…/scripts/ws-identity.sh）
------------------------------------------------------------------------
合计: 19 项通过 / 0 项失败 / 19 项检查
EXIT=0
```

（收尾项改完后的复跑：仍是 **19 项通过 / 0 失败，EXIT=0**；`pipeline.md` 现 148 行，仍在 ≤150 内。）

其他约束未破：`README.md` 70 行（≤80）、`pipeline.md` 146 行（≤150）、`closure.md` 45 行；9 个角色的 8 节结构未重写；未新增角色；未引入第二套状态机；**未 commit**。
