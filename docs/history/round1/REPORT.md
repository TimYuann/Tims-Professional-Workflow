# Round 1 · REPORT（worker session）

- 执行者：worker session（唯一实现者）
- 运行环境：provider `opencode-go` / model `deepseek-v4.1-flash` / thinking `max`
- 任务卡：`.pi/round1/TASK.md`（含 Owner 中途追加的三次收紧：Oracle 定位、冲突裁决表 + 闭环矩阵 + 工具解耦判定线 + 注入契约）
- **未做任何 commit**；工作树保持 dirty 供 review

---

## 1. 做了什么

### D1 `roles/` × 9 个自包含角色文件

统一结构：frontmatter（`role` / `title`，**不再带 version**）+ 标题下**注入契约**块 + 8 个编号节。
§4 全部写成"触发条件 → 编号步骤 → 判断依据 → 反例/何时不适用（每个文件 ≥2 处）"；§8 每条自欺都配一个可执行动作。

| 文件 | 行数 | §4 小节数 |
|---|---|---|
| `roles/driver.md` | 216 | 7 |
| `roles/oracle.md` | 212 | 8 |
| `roles/investigator.md` | 197 | 7 |
| `roles/architect.md` | 210 | 8 |
| `roles/planner.md` | 188 | 7 |
| `roles/implementer.md` | 186 | 6 |
| `roles/reviewer.md` | 200 | 7 |
| `roles/verifier.md` | 221 | 8 |
| `roles/integrator.md` | 196 | 7 |

关键设计的落点：

- **Oracle 新口径**：触发条件四条写在 `§4.1`；只读产物与冻结契约（不读作者叙述）在 `§4.2`；三件套（裁决 + 依据 + 区分性实验）在 `§4.3`；判不开写"不可区分"在 `§4.4`；**反实现挑战**在 `§4.5`（不需要第二个模型的同源信号）；不留断档（fresh Reviewer 承接、不得由实现者承担）在 `§4.7`；四条禁令在 `§4.8`。
- **§1–2 层与 §3–4 层的接缝**：9 个角色文件的注入契约块逐字一致，写明"Driver 附加内容不得改变本角色的纪律与方法边界（例：不能因为这轮只开 3 个会话就让实现者给自己发 PASS）"。
- **工具解耦**：`roles/driver.md` §4.3 步骤 0 是**全库唯一**一处提到"检测当前工作环境提供哪些能力（能否开独立会话 / 能否会话间通信 / 能否隔离工作区 / 有哪些模型档位）"，零命令、零产品名。其余任何位置都不出现具体底座名称（机器校验，见 §2）。

### D1b `closure.md` 闭环矩阵（42 行）

- 主链 9 行（发卡 → 调查 → 设计 → 切片 → 实现 → 审查 → 验证 → 集成 → 收口），列为 `环节 / 承接角色 / 输入字段（=上一行输出，逐字） / 附加输入（来自更早环节） / 输出字段 / 可跳过条件 / 跳过时职责移交给谁`。
- 拆出"附加输入"列的原因：Verifier 同时要收 Reviewer 的 `object` 与 Implementer 的 `base`/`tree`，不拆列就无法满足"每个输入字段在**上一行**输出里逐字存在"。
- 按需与降级表 2 行：A1 独立复核、A2 装配降级。
- 四条指定路径都有明确承接人：跳过调查 → `roles/architect.md`（§4.1 接地阶段填 `first_divergence`）；跳过设计 → `roles/planner.md`（补 `caller_usage` + 对照形状，且跳设计不取消独立复核）；solo 档 → Driver 装配 + 判断侧必须另起会话；没有独立复核会话 → fresh Reviewer 承接，**不得由实现者本人承担**。

### D2 `pipeline.md`（149 行，≤150）

10 项必含内容齐备：交付链 + 机器可读拓扑块、装配档位（含 solo 的"1 指作者侧常驻数、判断侧仍须另起会话"）、5 条硬边界、四类依赖、四问分 A/B/C/D 类与"只有写窗与合并串行"、写窗、停止条件、证据复用四条件（**明确不写"基线一动全部作废"**）、波次汇合、授权检查。

### D3 `SOURCES.md`（436 行）

- 三个 clone 逐方法登记（pstack 6 个小节、matt、addy），每条给出 `上游文件:行号 / 机制 / 保留·改写·删除 / 理由 / 落点`；SHA 用 `git rev-parse HEAD` 实取；阅读深度用 `[全文]/[局部]/[仅目录]` 如实标注。
- 开头如实记了"本仓文档对上游数量说法不一致"（AGENTS.md 与提案 §6 写 3 个 clone、Owner 口径 6 个来源）。
- 提案 §10 的 4 位外部作者（Dex Horthy / Armin Ronacher / Jesse Vincent / Garry Tan）**全部标 NOT ABSORBED**，写清原因与下一轮计划；其中两条机制的**署名撤回、机制保留**（出处改引本地可核对的证据）。
- **新增 §4 冲突裁决表 9 条**（比任务卡要求的 6 条多 3 条）：注释与文档 / 是否阻塞等人 / 多模型盲审 / 量化门禁 / TDD 严格性 / 调查者边界 / 集成冲突能否退出 / 深度判据（重复，裁为分层）/ "四类依赖"同名不同义（重复，只留一组）。每条都是**单选**，没有一条写"综合两者"。
- §5 消费者契约（只读对齐）逐行登记，含任务卡把「下次改动成本估算」记错出处的一处偏差说明。

### D4 `scripts/`

- `scripts/log-decision.sh` + `scripts/decision-log-template.tsv`：由上游 logger 改写而来（去环境耦合，保留 `>>` 追加、单元格清洗、公式前缀防护）。
- `scripts/check-library.py`：只读、可重复运行的 13 项检查（结构与注入契约、§4/§8 计数、引用限制、**收据字段 ⊆ 产出方字段**、**交接拓扑双向一致**、**闭环矩阵相邻字段包含**、死链、版本单一来源、底座解耦 ×2）。
- 顺带最小修复 `scripts/check-team-version.sh`：原实现在**解析不到版本时返回 0**（读不懂就放行），改为 `exit 3` fail-closed，并在头部写明退出码含义与"不校验内容快照"这一未做项。

### D5 `README.md`（68 行，≤80）

这是什么 / 给谁 / **底座必须提供的 4 个原语**（角色注入、会话隔离、会话间消息、工作区隔离）/ 怎么把角色注入一个会话（只写三个效果，零命令）/ 三个档位怎么选 / 目录说明 / 自检命令。

### D6 清理

- `workflows/`（3 份）与 `skills/`（8 份）→ `docs/archive/workflows/`、`docs/archive/skills/`（用 `git mv` 保留历史；**只把改名放进索引，便于 `git status` 看清 rename 映射，未 commit**）。
- `AGENTS.md` 重写：删掉不存在的 `wave-execution.md` / `evals/` / `read-only-investigation.md` / `perf-optimization.md` 引用，目录树与新结构一致。
- 版本收敛到 `VERSION` 单一来源，值改为 `1.0.0`（理由见 §4 残余不确定性第 4 条）。

---

## 2. 脚本实跑输出（原样贴）

### 2.1 最终自检（返修后）

```
$ python3 scripts/check-library.py
TIM · check-library.py（只读自检）
扫描范围: roles , scripts , pipeline.md , closure.md , README.md , AGENTS.md , SOURCES.md , VERSION
显式排除: docs/**（历史材料与归档） ; .pi/**（工作区） ; upstreams/**（只读克隆，按路径豁免） ; 上游仓库名 cursor-plugins / mattpocock-skills / addyosmani-agent-skills / pi-review / superpowers / gstack / humanlayer（溯源标识，非本库依赖或悬停） ; scripts/check-library.py 自身（含 harness token 清单与判定字样，按定义自排除）
本检查能判: 结构与字段级闭环、引用与死链、版本单一来源、底座解耦的措辞、能力探测块的位置与集中度
本检查判不了: §4 方法的实质深度、语义正确性、字段值是否真实、某次跳过是否真的合规——这些交给独立审查与人审
仓库根:   /Users/yuantian/Developer/tim-professional-workflow
------------------------------------------------------------------------
[PASS] 角色文件集合                                 缺 无；多 无
[PASS] 角色 frontmatter + 8 节                   9/9
[PASS] 注入契约声明                                 9/9
[PASS] §4 反例/不适用 ≥2                           9/9
[PASS] §8 常见自欺 ≤4                             9/9
[PASS] 角色文件引用仅限 roles/                        通过
[PASS] 闭环：收据字段 ⊆ 产出方字段                        全部成立｜收据 25/25、产出 11/11 参与校验
[PASS] 闭环：交接拓扑双向一致                            全部一致
[PASS] 闭环矩阵 ↔ 角色文件交叉校验                        主链 9 行 + 按需 2 行，逐行与角色文件交叉校验 全部成立
[PASS] 死链检查                                   无死链
[PASS] 版本单一来源 VERSION                         VERSION=1.0.0，扫描范围内无第二处声明
[PASS] 工具解耦：无具体 harness 名称                    0 命中
[PASS] 工具解耦：能力探测块恰好一处且在 driver.md             命中 roles/driver.md:109（4/4 项）
[PASS] 工具解耦：其他角色文件无能力枚举                       0 命中
------------------------------------------------------------------------
合计: 14 项通过 / 0 项失败 / 14 项检查
EXIT=0
```

### 2.2 开发过程中它真抓到的（未修复前的原始输出，节选）

```
[FAIL] 闭环：交接拓扑双向一致    roles/architect.md §3 交 design-proposal 给 roles/oracle.md，但后者 §2 未收;
                               roles/driver.md §3 交 task-card 给 roles/planner.md，但后者 §2 未收;
                               roles/investigator.md §3 交 investigation-report 给 roles/implementer.md，但后者 §2 未收;
                               roles/oracle.md §3 交 oracle-ruling 给 roles/driver.md，但后者 §2 未收;
                               roles/reviewer.md §3 交 review-verdict 给 roles/implementer.md，但后者 §2 未收;
                               roles/integrator.md §3 交 integrated-baseline 给 roles/driver.md，但后者 §2 未收

[FAIL] 死链检查                  SOURCES.md → skills/why/references/epistemics.md 等 39 条
[FAIL] 工具解耦：无具体 harness 名称  AGENTS.md:68 'cursor'; README.md:13 'dsh'; SOURCES.md:40 'mcp'; SOURCES.md:244 'pi' 等 9 处
[FAIL] 工具解耦：能力探测句恰好一处且在 driver.md  命中 [('roles/driver.md', 106), ('scripts/check-library.py', 54)]
```

四个失败里，**第一和第四个是真缺陷**：

1. 拓扑双向检查发现 6 处"产出方声明交出去、接收方却没声明收"——其中 `investigator → implementer`、`reviewer → implementer`、`oracle → driver` 三处是真断档（实现者确实要用调查的最小复现场景与审查的 findings），补了收据；`driver → planner` 一处是我多写了消费者，删掉。
2. 能力探测句命中 2 处（driver.md + 脚本自身）——这条如果不查，就会变成"规则写了但没人守"。

另外两项的诚实说明：

- **死链检查的 39 条里，相当一部分是我自己的引用风格造成的**：`SOURCES.md` 的引用路径相对上游 clone 根写（如 `skills/why/SKILL.md:36-48`），第一版检查器只按仓库根解析，于是全判死链。改成"仓库根 → 三个 clone 根"的解析次序后才分出真死链（`skills/codebase-design/...` 少了 `engineering/` 段、`workflows/thin-bugfix.md` 已归档未改路径），这几条是真错，已修。
- **底座解耦的 9 处命中**是真问题，其中 `AGENTS.md` / `README.md` 由重写解决，`SOURCES.md` 三处改成中性表述解决。

### 2.3 负控制：人为植入 6 处缺陷，看它抓不抓得住

在 `/tmp` 的仓库副本上植入（不改本仓）：① 删掉 `architect §3` 的 `change_cost` 字段；② 在 `README.md` 追加一句含具体底座名称的话；③ 把能力探测句复制进 `oracle.md`；④ 把 `closure.md` 里一处引用改成不存在的文件；⑤ 把 `implementer §7` 的节标题改短；⑥ 把 `closure.md` 主链第 3 行的输入字段改成上游没有的字段。

```
════ 负控制运行（6 处人为破坏）════
[FAIL] 角色 frontmatter + 8 节    roles/implementer.md: 节不符（得到 [... '退出判据', '常见自欺']）
[FAIL] 闭环：收据字段 ⊆ 产出方字段   roles/planner.md §2 收 design-proposal 缺字段 ['change_cost']（roles/architect.md §3 未提供）
[FAIL] 闭环矩阵相邻字段包含          第 3 行输入 ['nonexistent_field'] 不在上一行输出里
[FAIL] 死链检查                  closure.md → roles/does-not-exist.md
[FAIL] 工具解耦：无具体 harness 名称  README.md:70 出现 'herdr'; README.md:70 出现 'intercom'
[FAIL] 工具解耦：能力探测句恰好一处且在 driver.md  命中 [('roles/driver.md', 109), ('roles/oracle.md', 182)]
------------------------------------------------------------------------
合计: 7 项通过 / 6 项失败 / 13 项检查
EXIT=1
```

**植入 6 处 → 抓出 6 处，每处都指到正确位置，退出码非零。** 这是"它能抓到问题"的可核证据。

### 2.4 决策台账 logger 实跑

```
$ scripts/log-decision.sh .pi/round1/decisions.tsv ...
$ column -s$'\t' -t .pi/round1/decisions.tsv
ts                    phase  decision                                   why                                    evidence                  result
2026-09-26T13:47:52Z  装配   按 Owner 决定取消 skills/ 载体，经验写进 roles/*.md  注入单元等于角色文件，单独注入即可开工       roles/*.md, pipeline.md   9/9 角色文件已建
2026-09-26T13:47:52Z  裁决   集成冲突改为允许安全退出                        上游同一句里取一侧/不许发明/永不退出三者互斥   SOURCES.md §4.7            已裁决并写入角色文件
2026-09-26T13:47:52Z  版本   VERSION 收敛为 1.0.0                          三处版本并存；单一来源是 VERSION           VERSION                   check-library.py 通过
2026-09-26T13:47:52Z  脚本   check-library.py 做负控制：人为植入 6 处缺陷       自检必须能抓到真问题                     6 处人为破坏 → 6 项 FAIL   抓出=6/6，退出码 1
```

---

### 2.5 负控制 2（针对 REVIEW-1 的 B1/B2/N1）

在仓库副本上植入 5 处：散文式收据字段改名（`roles/verifier.md` `object`→`objectZZZ`）、删掉一条散文式收据字段行（`roles/integrator.md` 的 `review-verdict` 那行）、矩阵内一致改名（`red_flag_screen`）、改角色 §3 字段名（`reviewer` 的 `coverage`→`coverageZZZ`）、把能力探测改成语义等价说法放进 `roles/planner.md`。

```
[FAIL] 闭环：收据字段 ⊆ 产出方字段   roles/integrator.md:30 收据 `review-verdict` 没有解析到任何字段（该项检查会空转）;
                                  roles/verifier.md §2 收 review-verdict 缺字段 ['coverage']（roles/reviewer.md §3 未提供）
                                  ｜收据 24/25、产出 11/11 参与校验
[FAIL] 闭环矩阵 ↔ 角色文件交叉校验    第 2 行输出 ['red_flag_screenXX'] 不在 roles/architect.md §3 声明里;
                                  第 5 行输出 ['coverage'] 不在 roles/reviewer.md §3 声明里;
                                  第 6 行输入 ['object'] 不在 roles/verifier.md §2 声明里;
                                  第 7 行输入 ['blocking'] 不在 roles/integrator.md §2 声明里
[FAIL] 工具解耦：能力探测块恰好一处且在 driver.md  命中 roles/driver.md:109（4/4 项）｜应恰一处、在 driver.md、且四项齐
[FAIL] 工具解耦：其他角色文件无能力枚举            roles/planner.md:159 3 项
------------------------------------------------------------------------
合计: 11 项通过 / 3 项失败 / 14 项检查
EXIT=1
```

**5 处全部被抓，且覆盖面从 25/25 如实掉到 24/25（不再把空转报成全绿）。**

### 2.6 返修记录：REVIEW-1 的 4 条阻断项 + 2 条非阻断

| 项 | 审查意见 | 改了什么 |
|---|---|---|
| **B1** | 闭环检查 2/3 空转，且报成全绿 | 解析器新增散文式 `字段：` 行识别；**解析不到任何字段的收据/产出本身就是一条 FAIL**（不再静默恒真）；输出打印真实覆盖面（现在 `收据 25/25、产出 11/11 参与校验`） |
| **B2** | 闭环矩阵与角色文件没有交叉校验（文档强于实现） | 矩阵每行的**输入字段与附加输入**必须在承接角色 §2 声明里找得到；**输出字段**必须在承接角色 §3 声明里找得到；否则报红。拆成两项独立检查（相邻包含 / 与角色文件交叉校验） |
| **B3** | `机械等价` 是没有判据的旁路 | `roles/reviewer.md §4.1` 给出定义：**等价证明 = 一条可重复执行的命令 + 它的输出**（重命名→符号集合不变的比对；剥注释/文档字符串→剥除后逐字相同），且必须覆盖被改动文件的全部符号；**写不出命令 = 不算证明 = 必须开独立审查**。同步到 `roles/driver.md §5`、`§8` 与 `closure.md` 行 5 |
| **B4** | 能力缺失时没有停机规则 | `pipeline.md §3` 新增硬规则 6；`closure.md` 四条路径表与 A2 行、`roles/oracle.md §4.7`、`roles/driver.md §4.3` 步骤 0 同步：**能力缺失只降结论等级，不降纪律要求**——开不出独立会话时，本轮判断类结论最高只能是 `UNVERIFIED` 或 Owner 明确书面接受风险，**不得记为 `PASS`** |
| **N1** | 能力探测项是字面匹配，语义等价的说法能漏过 | 改为**多词命中计数**：4 项能力词（独立会话 / 会话之间通信 / 隔离工作区 / 模型档位）。检测块 = 同一行命中 ≥3 项，必须恰好一处、在 `driver.md`、四项齐；**其他任何角色文件命中 ≥2 项即报红**（独立检查） |
| **N2** | 机械检查判不了方法深度，不能给假信心 | 输出头部新增边界声明：`本检查能判: …` / `本检查判不了: §4 方法的实质深度、语义正确性、字段值是否真实、某次跳过是否真的合规——这些交给独立审查与人审` |

补记：新检查一上线就抓到两处之前被空转掩盖的真实不一致——`roles/driver.md` 的 `integrated-baseline` 收据少声明了 `conflicts` / `post_merge` / `reused_evidence`；`owner-brief` 收据头写法不合格式导致整条不参与校验。两处均已修。

---

## 3. 没做什么与原因

| 没做 | 原因 |
|---|---|
| 没有 commit | 任务卡硬要求；工作树留 dirty，归档用 `git mv` 只进了索引便于看 rename |
| **没有搬进性能诊断的完整方法** | addy 的 `performance-optimization` 有 496 行（测量手段清单、按类别的瓶颈表、缓存/打包/查询三类反模式）。本轮只把**噪声门**（同码 ≥2 次、效应落在噪声带内只能报"未测出"、机制指标 vs 结果指标）与"回退也要记账"写进 `roles/verifier.md §4.5/§4.8`。**瓶颈定位表与测量手段清单没有进来**——这是本轮明确的欠账，不是遗漏的借口 |
| 没有把 R2 建议的四个方法做成独立文件 | 载体决定是"经验写进角色"；planning → `roles/planner.md §4`、real-path → `roles/verifier.md §4.2`、safe-integration → `roles/integrator.md §4`、performance →（见上，只做了一半） |
| pstack 的 17 个 `principle-*` 只读了 6 个 | 其余只看了目录；`SOURCES.md` 已按 `[仅目录]` 标注并列入"下一轮先读全文再登记" |
| 没有为 `check-team-version.sh` 加内容快照校验 | R2 审查指出过这个缺口，但修它需要先有下游绑定的格式约定；本轮只修了"读不懂就放行"这个方向性错误 |
| 没有改 `docs/` 下的提案与两份历史评审 | 它们是历史材料；`docs/archive/` 里保留的旧载体里必然还有具体底座名称，这是**故意保留的历史**，不参与"库内容"判定（`check-library.py` 的排除清单里已打印） |
| 没有动 ekunai 任何文件 | 只读参考 |

---

## 4. 残余不确定性（如实）

1. **“机械等价”的判据已定义（B3），但没有机器校验**。`roles/reviewer.md §4.1` 步骤 4–6 已把等价证明定义为“一条可重复执行的命令 + 它的输出”；但**一条命令到底能不能真的区分“等价”与“不等价”，机器判不了**——它只能保证“命令与输出存在”，不能保证“命令选得对”。
2. **Oracle 的触发条件与拓扑有摩擦**。触发条件③"角色之间对方案或判据有争议"通常发生在 Architect / Reviewer 侧，但机器可读拓扑里只有 `driver → pending-question → oracle`。也就是说争议必须经 Driver 转手；如果 Driver 不认为是争议，这条触发就丢了。**这是真的断档风险，我没有修**（修它要给角色之间加直连边，会影响已有拓扑与 §2/§3 契约）。
3. **“连判断会话都开不出来”已补停机规则（B4）**——`pipeline.md §3` 硬规则 6 写明“能力缺失只降结论等级”：此时判断类结论最高只能是 `UNVERIFIED` 或 Owner 书面接受风险，不得记 `PASS`。**仍未机器校验**：本轮究竟有没有真的开独立会话，靠 Driver 声明，机器验不了。
4. **`VERSION = 1.0.0` 是我的判断，不是 Owner 的指示**。任务卡只说"统一到一个来源"。我选 `1.0.0` 是因为角色 frontmatter 与提案都已在用 1.0.x，且本轮是载体级重构（SemVer 下应升 major）。**请在 review 时确认这个值；改它只需要动 `VERSION` 一个文件。**
5. **`docs/` 里仍有版本字符串**（提案的 `1.0-final`）。按本轮判定，`docs/` 下的历史文档带的是**文档版本**，不参与库版本判定；`check-library.py` 的排除清单里打印了这一点。如果 Owner 认为历史文档也必须改，需要先解除"不动历史评审"的约束。
6. **`check-team-version.sh` 的修改是我主动加的**（任务卡 D4 没点名）。理由是它属于"读不懂就放行"的失败方向反转，属"修掉断档"的范围。如认为超范围，可单独回退这一个文件。
7. **归档的 git 状态是 mixed**：rename 已进索引、内容改动未进索引。`git status` 看 rename 映射，`git diff` 看内容改动。

---

## 5. 下一轮接手要看什么

1. `python3 scripts/check-library.py` 必须是 0 ——它是"闭环没有断档"的机器判据，改任何角色文件后都要跑。
2. `closure.md` 的字段必须与角色文件 §2/§3 同步；改角色契约时要同时改三处（角色文件、`pipeline.md` 的 `pipeline` 块、`closure.md`）。
3. 本轮三处已知未闭合（§4 的 1、2、3 条）是下一轮的候选工作，优先级按 Owner 判断。
4. `SOURCES.md §4 冲突裁决表` 是本轮的新增纪律：**以后三仓立场不一致处必须单选并把理由写在这里**，不接受"综合两者"。
5. 大块欠账是性能诊断方法（§3 第 2 行）。

---

## 6. 任务卡要求回答的三个问题

### 6.1 每个角色文件被单独注入时，它需要的信息是否都在文件里？一个我自己发现的缺口

**结论：绝大多数在（返修后已补齐一处）。** 返修前发现的缺口是 **Reviewer 缺少“机械等价”的判据**；B3 已把判据写进 `roles/reviewer.md §4.1` 步骤 4–6（等价证明 = 一条可重复执行的命令 + 它的输出；写不出命令即必须开独立审查）。**剩下真正还不在文件里的**是“这条命令选得对不对”——角色文件只能要求“给出一条命令”，无法保证它真的能区分等价与不等价；这一层只能靠独立审查与人审。

其余信息缺口都在设计上被正确地推给了第 3–4 层（例如"本轮有效授权记录在哪"），角色文件的处理是**卡住而不是自行补全**，这是刻意的：`pipeline.md §10` 要求"未授权的交接停在交付点"。

### 6.2 `check-library.py` 实际抓到了什么？如果一条都没抓到，说明它没用

它抓到了 **4 类真实问题**（细节见 §2.2）：

1. **6 处交接拓扑断裂**（产出方声明交、接收方未声明收）——其中 3 处是真断档，已补收据；
2. **真死链**（`SOURCES.md` 里引用的 `skills/codebase-design/...` 少了一段路径、`workflows/thin-bugfix.md` 已归档但引用未改）；
3. **9 处具体底座名称**（`AGENTS.md` / `README.md` / `SOURCES.md`）；
4. **能力探测句出现 2 处**（规则写了但没人守）。

为证明它不是在"抓空气"，又做了一次负控制：在仓库副本上人为植入 6 处缺陷（少一个字段 / 多一处底座名 / 多一句能力探测 / 一条死链 / 改一个节标题 / 改一个矩阵字段），**6 处全部被抓，退出码 1**（§2.3）。

另外如实说明一点：它的**第一版有一类误报**——把 `SOURCES.md` 里"相对上游 clone 根"的 39 条引用全判成死链。这不是检查器抓错了问题，而是抓错了对象；改成三级解析次序后才分出真假。

### 6.3 还有哪一处"看起来闭环、实际没闭环"？

1. **`closure.md` 只机器校验字段，不校验“跳过条件是否真的满足”。** 字段是硬校验；“什么情况下允许跳过”仍是文字条款（机械等价那一条已在 B3 里给了判据，但仍是人要判断的）。一次真实的跳过是否合规，机器判不了——只有审查者能判。
2. **Oracle 触发条件③没有直连边**（§4 第 2 条）：争议要经 Driver 转手，转手环节一旦漏判，独立复核就静默不发生。
3. **“开不出判断会话”已补停手条款（B4）**：`pipeline.md §3` 硬规则 6 要求“能力缺失只降结论等级”——判断类结论最高只能是 `UNVERIFIED` 或 Owner 书面接受风险。**但仍无机器验证**：本轮到底有没有真的开独立会话，只有 Driver 的声明。
4. **设计 → 实现之间的信息传递没有"该看的看到了"这一层校验**：矩阵只保证字段存在（`caller_usage` / `data_shapes` / `invariants`），不保证 Implementer 真的读了；`red_flag_screen` / `change_cost` 这类只给 Planner/Oracle 的字段，谁该看谁不该看，矩阵表达不了。
