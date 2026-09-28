# REPORT · 0929 轮取证（investigator）

任务：只找证据，不下结论，不给建议。四件取证 A/B/C/D。
产出路径：`.pi/investigation/REPORT-0929-investigator.md`。
三态口径：`PASS` / `FAIL` / `UNVERIFIED`。环境故障既不算 `PASS`，也不判成产品缺陷。

**边界声明**：本报告在仓库工作树上零改动。所有实验都在 `/tmp` 的独立副本里做，逐条列出见 §F。
报告里每一句断言都带 file:line；没有 file:line 的句子是本报告的测量口径说明，不是对产品的判断。

> **0929 续（Round 2，pane 重建后的新会话）**：本文件末尾新增 `R · Round 2` 节。
> Round 1 的被测对象是 tag v2.0.6（`29a50e4`）；Round 2 的被测对象是 commit `12aecf1`。
> 取证期间代码前进了一次（`e7f6de1` → `12aecf1`，2026-09-28 20:36:19 +0800），
> 导致 Round 1 的两处结论过时；取代关系在 `R0` 逐条列出，Round 1 正文保留作 v2.0.6 的测量记录。

---

## 0. 被测对象与基线（先测基线）

### 0.1 被测对象

- 基线句柄：`tag v2.0.6`（附注 tag）→ `commit 29a50e4`。`git rev-parse v2.0.6` = `29a50e40f2ed0bf5d5bff85b7fbfa6b78059df3c`。
- 工作树 `HEAD` 在取证时为 `8825b0e`；`git diff --stat v2.0.6 HEAD` = 只改 `.decisions/ledger.tsv`（+12 行），不触产品面（与 round-3 verify §0.1 记录一致）。
- 取证期间工作树上有**未提交**改动：`scripts/check-closure.py`、`scripts/check-consistency.py`、`scripts/ledger.sh`（`git status --porcelain` 三个 ` M`）。这是另外两个 worker 正在改检查器脚本，属于任务书预告的情况。本报告**没有**使用这三个未提交版本做任何行为判定；所有检查器行为证据取自 tag `29a50e4` 的干净检出。

### 0.2 基线结果（在 `/tmp/inv0929-final`，`git clone` + `git checkout 29a50e4`）

| 检查 | 结果 | 退出码 |
|---|---|---|
| `python3 scripts/render.py --check` | `OK（12 个派生文件逐字一致）` | 0 |
| `python3 scripts/check-closure.py` | `合计: 19 项通过 / 0 项失败 / 0 项跳过 / 19 项检查` | 0 |
| `python3 scripts/check-consistency.py` | `合计: 7 项通过 / 0 项失败 / 7 项检查` | 0 |

**基线判定：`PASS`。**

- 同一副本挂上 `upstreams/`（软链接到工作树的只读克隆）后重跑：仍 `19/19 + 7/7`；`C9` 的 detail 追加了 `；并已逐条比对 sha256 与 pin`。即：`upstreams/` 在不在只影响 `C9` 的对照深度与 detail 措辞，不影响基线颜色。
- 工作树 `HEAD=8825b0e` 上跑检查器会出现 `C1 FAIL`（`当前 commit 上没有 tag——打了 tag 之前不能算一个 release`）。原因是 `HEAD` 比 tag 多一个 commit（`.decisions/ledger.tsv`），是本库 `C1` 自身语义，不是产品面破坏；且工作树上的脚本正在被别人编辑，不作为证据。

### 0.3 基线中途是否变红

取证过程中没有观察到基线因他人编辑而中途变红。本报告的全部 checker 行为数据在 `/tmp` 的 tag 检出上采集。仓库工作树上的三处 ` M` 我全程未触碰、未 staged。

---

## A · 21 个「不被任何判据门控」的产物字段

### A.0 口径与复现方式

- 「被门控」的口径与 `C15` 完全一致：字段对 `(A\d+, field)` 出现在**任意阶段** `exit_criteria` 的文本里即算门控。实现见 `scripts/check-closure.py:721-725`（`gated.update(field_re2.findall(crit))`）。
- 全库阶段退出判据共 25 条（`C4` detail：`25 条退出判据`）。
- 独立复算结果与 verify 报告一致：**产物字段 40 个，门控 19 个，未门控 21 个**。
- 另查「判据之外的东西会不会挡」：把 21 个字段名拿去扫所有阶段的 `purpose` / `driver_seat_note` / `hard_rules`，命中 **0** 处（脚本口径：字段名加词边界，扫 `workflow/registry.yaml`）。也扫了两个 checker 的源码，命中的都是英语变量名/注释（如 `consumers` 是 `a.get("consumers")`、`claim` 是 `C10` 的局部变量），**没有一处把 21 个字段里的任何一个当契约字段来校验**。

**本报告对「三堆」的操作性定义（先把口径写死，避免分类不可复核）：**

- **真空**：既没有判据挡，也没有产出方正文要求（角色文件或它拥有的技能里没有要求填），也没有工具层载体。
- **有软约束**：没有判据挡，但产出方角色文件 / 技能正文 / 字段 notes 里**明确要求填**；空着不会被任何机制拦下。
- **实际被别的东西约束着**：没有阶段判据挡，但有一个**非散文**的载体在拒绝或自动生成该值。

三堆互斥、合起来是 21。

### A.1 逐字段证据（21 个）

#### A1 · 诉求陈述（producer: `voice`；registry.yaml:77）
- **A1.done_meaning**
  - notes（registry.yaml:96）：「做完之后世界什么样——不是「做完了」，是可观察的差别」
  - 产出方正文：roles/voice.md:39「`A1` 诉求陈述，四个字段全部非空」；roles/voice.md:44；skills/grilling.md:46；skills/interview-me.md:55；skills/idea-refine.md:53
  - 判据挡？**否**（P0 只点名 `A1.ask`、`A1.non_goals`，registry.yaml:314-315）
  - 其他载体：无
  - **堆：有软约束**
- **A1.unknowns**
  - notes（registry.yaml:98）：「现在还不知道的，以及它挡住了哪一步」
  - 产出方正文：roles/voice.md:39、:46；skills/grilling.md:49；skills/interview-me.md:57；skills/idea-refine.md:55；skills/to-questionnaire.md:17
  - 判据挡？**否**
  - 其他载体：无（消费者侧另有技能要求它非空：skills/research.md:17、skills/tier-sizing.md:16-17；后者与 registry 冲突，见 §D.4）
  - **堆：有软约束**

#### A2 · 事实集（producer: `scout`；registry.yaml:99）
- **A2.claims**
  - notes（registry.yaml:116）：「每条结论 + 置信档位：直接（有人明确写了为什么）／推断／未验」
  - 产出方正文：roles/scout.md:38「`A2` 事实集，三个字段全部非空」、:42；skills/research.md:42；skills/trace-paths.md:97-99
  - 判据挡？**否**（P0 只点名 `A2.gaps`，registry.yaml:316）
  - 其他载体：无
  - **堆：有软约束**
- **A2.evidence**
  - notes（registry.yaml:117）：「对应锚点：文件行号、命令输出、或一次真实运行」
  - 产出方正文：roles/scout.md:38、:43；skills/research.md:45；skills/trace-paths.md:97-102；skills/recall-context.md:59
  - 判据挡？**否**
  - 其他载体：无（消费者侧：skills/domain-modeling.md:18、skills/spec-driven-development.md:19、skills/feature-map.md:17、skills/codebase-design.md:17、skills/teach.md:16 都要求它非空）
  - **堆：有软约束**

#### A3 · 能力地图（producer: `architect`；registry.yaml:120）
- **A3.consumers**
  - notes（registry.yaml:139）：「每条能力谁在用；没有消费者的能力是候选删除项」
  - 产出方正文：roles/architect.md:48「`A3` 能力地图」+ :51 合格线表；skills/feature-map.md:72
  - 判据挡？**否**（P1 只点名 `A3.capabilities`，registry.yaml:333）
  - 其他载体：无
  - **堆：有软约束**
- **A3.freshness**
  - notes（registry.yaml:140）：「上次与代码核对的时间。过期不更新的地图比没有地图更坏。**建立与保鲜的分工是死的：feature-map（P1·architect）负责建，verification-suite（P5·verifier）只跑不改，偏差写进 A8.frame_alignment 交回 architect。verifier 不得自己重建能力清单。**」
  - 产出方正文：roles/architect.md:52；skills/feature-map.md:74、:86
  - 判据挡？**否**（0 条判据提到 `freshness`；P1 判据 registry.yaml:329-333 无它，P5 判据 :381-384 无它，P6 判据 :396-398 无它）
  - 其他载体：无（详见 §C）
  - **堆：有软约束**

#### A4 · 冻结契约（producer: `architect`；registry.yaml:142）
- **A4.why**
  - notes（registry.yaml:164）：「为什么——业务理由，不是技术偏好」
  - 产出方正文：roles/architect.md:58-59；skills/spec-driven-development.md:69、:115、:136、:145；skills/domain-modeling.md:66；skills/documentation-and-adrs.md:72；skills/constraint-driven-development.md:93；skills/api-and-interface-design.md:82；skills/codebase-design.md:146
  - 判据挡？**否**（P1 只点名 `A4.what` / `done_definition` / `scope` / `boundaries`，registry.yaml:329-332）
  - 其他载体：无
  - **堆：有软约束**

#### A5 · 任务图（producer: `cartographer`；registry.yaml:175）
- **A5.edges**
  - notes（registry.yaml:192）：「依赖边。**图里没有路径依赖的那些节点才是可并行的**；有边的按拓扑序串行。没有验收口径的并行结果无法汇合，所以 edges 与 acceptance 缺一不可」
  - 产出方正文：roles/cartographer.md:39「`A5` 任务图，三个字段全部非空」、:44；skills/to-tickets.md:39；skills/triage.md:40；skills/task-breakdown.md:39；skills/wayfinder.md:39
  - 判据挡？**否**（P2 只点名 `A5.slices` / `A5.acceptance`，registry.yaml:344-345）
  - 其他载体：无
  - **堆：有软约束**

#### A6 · 实现候选（producer: `builder`；registry.yaml:195）
- **A6.change**
  - notes（registry.yaml:214）：「改了什么。**这一栏要点名列全工作过程建出的每一样东西**——杠杆工具、改造脚本、生成器、闸门检查、流水线配置、测试、注释、一次性原型、会红的反馈回路。它们不是独立产物，但漏列就等于这一轮没人对它们负责」
  - 产出方正文：roles/builder.md:46「`A6` 实现候选，**四栏**全部非空」、:51；skills/implement.md:37；skills/incremental-implementation.md:40；skills/code-simplification.md:38；skills/arena.md:33；skills/prototype.md:39；skills/deprecation-and-migration.md:40；skills/tdd.md:39；skills/user-interface-engineering.md:70；skills/debugging.md:37；skills/source-driven-development.md:39
  - 判据挡？**否**（P3 只点名 `A6.runnable` / `A6.known_gaps`，registry.yaml:356-357）
  - 其他载体：无（README.md:93、registry.yaml:230 的 A6 embodiment 是要求语句，不是载体）
  - **堆：有软约束**

#### A7 · 裁决（producer: `adversary`；registry.yaml:218）
- **A7.stance**
  - notes（registry.yaml:234）：「采纳／挑战／附条件通过」
  - 产出方正文：roles/adversary.md:40「`A7` 裁决，三个字段全部非空」、:44；skills/swarm.md:32；skills/code-review.md:35；skills/doubt-driven-development.md:35；skills/interrogate.md:33
  - 判据挡？**否**（P4 只点名 `A7.reason`，registry.yaml:368）
  - 其他载体：无
  - **堆：有软约束**
- **A7.conditions**
  - notes（registry.yaml:236）：「附条件通过时，条件是什么、由谁验收」
  - 产出方正文：roles/adversary.md:40、:46；skills/swarm.md:34；skills/code-review.md:37；skills/doubt-driven-development.md:37；skills/interrogate.md:35
  - 判据挡？**否**
  - 其他载体：无
  - **堆：有软约束**

#### A8 · 验证凭据（producer: `verifier`；registry.yaml:239）
- **A8.claim**
  - notes（registry.yaml:258）：「证明了哪一条 A4.done_definition」
  - 产出方正文：roles/verifier.md:52「`A8` 验证凭据，**七栏**全部非空」、:56；skills/verification-suite.md:41；skills/security-and-hardening.md:36；skills/browser-testing.md:39；skills/performance-optimization.md:39；skills/observability-and-instrumentation.md:39
  - 判据挡？**否**（P5/P6 判据只点名 `A8.verdict` / `A8.subject` / `A8.frame_alignment`，registry.yaml:381-383、:396-398）
  - 其他载体：无
  - **堆：有软约束**
- **A8.scope**
  - notes（registry.yaml:260）：「这次验证覆盖了 A3 的哪些能力条目。**由 `verifier` 填**，逐条列出能力 id」（21 个未门控字段里，**唯一**在 notes 中带显式「由 X 填」声明的）
  - 产出方正文：roles/verifier.md:52、:58、:64（「`subject` 与 `scope` 是这一轮最硬的两个字段」）；skills/verification-suite.md:53；skills/security-and-hardening.md:44；skills/browser-testing.md:45；skills/performance-optimization.md:47；skills/observability-and-instrumentation.md:47
  - 判据挡？**否**
  - 其他载体：无
  - **堆：有软约束**
- **A8.observation**
  - notes（registry.yaml:261）：「实际观察到什么——跑出来的，不是推理出来的」
  - 产出方正文：roles/verifier.md:52、:59；skills/verification-suite.md:42；skills/security-and-hardening.md:37；skills/browser-testing.md:40；skills/performance-optimization.md:40；skills/observability-and-instrumentation.md:40；roles/driver.md:71（「A8 的 `observation` 必须是外部观察」）
  - 判据挡？**否**
  - 其他载体：无
  - **堆：有软约束**
- **A8.environment**
  - notes（registry.yaml:263）：「在什么环境、什么对象上跑的」
  - 产出方正文：roles/verifier.md:52、:61；skills/verification-suite.md:43；skills/security-and-hardening.md:38；skills/browser-testing.md:41；skills/performance-optimization.md:41；skills/observability-and-instrumentation.md:41
  - 判据挡？**否**
  - 其他载体：无
  - **堆：有软约束**

#### A9 · 决策台账（producer: `scribe`；registry.yaml:266）
- **A9.run**
  - notes（registry.yaml:287）：「本次运行的标识。并发追加靠它区分谁写的哪一行」
  - 产出方正文：roles/scribe.md:39「`A9` 决策台账，**八个字段**」、:44
  - 判据挡？**否**（各阶段只点名 `A9.actor`；P6 只点名 `A9.result`，registry.yaml:317、:397）
  - 其他载体：**有**。scripts/ledger.sh:126 用 `TPW_RUN` 或时间戳+pid 自动生成，不经过人的手
  - **堆：实际被别的东西约束着（工具自动生成）**
- **A9.subject**
  - notes（registry.yaml:288）：「这条决策关于哪个对象：commit、文件路径或契约条目」
  - 产出方正文：roles/scribe.md:45
  - 判据挡？**否**
  - 其他载体：**有**。scripts/ledger.sh:50-55 对空值 `exit 2`
  - **堆：实际被别的东西约束着（工具拒空）**
- **A9.phase**
  - notes（registry.yaml:289）：「在哪个阶段做出」
  - 产出方正文：roles/scribe.md:46
  - 判据挡？**否**
  - 其他载体：**有**。scripts/ledger.sh:50-55 对空值 `exit 2`
  - **堆：实际被别的东西约束着（工具拒空）**
- **A9.decision**
  - notes（registry.yaml:290）：「决定做什么」
  - 产出方正文：roles/scribe.md:47；skills/decision-ledger.md:24、:38
  - 判据挡？**否**
  - 其他载体：**有**。scripts/ledger.sh:50-55 对空值 `exit 2`
  - **堆：实际被别的东西约束着（工具拒空）**
- **A9.why**
  - notes（registry.yaml:291）：「为什么」
  - 产出方正文：roles/scribe.md:39、:48；skills/decision-ledger.md:24、:39
  - 判据挡？**否**
  - 其他载体：**有**。scripts/ledger.sh:50-55 对空值 `exit 2`
  - **堆：实际被别的东西约束着（工具拒空）**
- **A9.evidence**
  - notes（registry.yaml:292）：「凭什么」
  - 产出方正文：roles/scribe.md:49；skills/decision-ledger.md:24、:40
  - 判据挡？**否**
  - 其他载体：**有**。scripts/ledger.sh:50-55 对空值 `exit 2`
  - **堆：实际被别的东西约束着（工具拒空）**

### A.2 三堆小结与计数

| 堆 | 数量 | 字段 |
|---|---:|---|
| 真空 | **0** | — |
| 有软约束 | 15 | A1.done_meaning、A1.unknowns、A2.claims、A2.evidence、A3.consumers、A3.freshness、A4.why、A5.edges、A6.change、A7.stance、A7.conditions、A8.claim、A8.scope、A8.observation、A8.environment |
| 实际被别的东西约束着 | 6 | A9.run、A9.subject、A9.phase、A9.decision、A9.why、A9.evidence |

两处必须说清的口径：

1. **「没有判据挡」对 21 个字段全部成立**，这一条是纯机械的：25 条 `exit_criteria` 的文本里，这 21 个字段名一次都没出现。21 个字段里没有一个是「哪怕空着也会被某条判据拦下」。
2. A9 那 6 个字段的「工具层约束」有一个前提：**得用 `scripts/ledger.sh` 写**。roles/scribe.md:55 用散文要求「用 `scripts/ledger.sh` 追加，不要手写」，但没有任何 checker 检查台账行是不是由该工具产生、也没有 checker 读台账行内容。用 `Exit 2` 之外的方式（例如手写 TSV）写出的空栏，不会被任何机制发现。

### A.3 受控实验：把 `C15` 的覆盖面从 19 扩到 40

实验副本：`/tmp/expA`（tag 检出副本，只改 `scripts/check-closure.py`：把 `gated` 集合从「判据里的字段对」替换为「全部产物字段对」）。

| 实验 | 操作 | 结果 |
|---|---|---|
| A-E1 | 未注入，直接扩到 40 | `C15 PASS`，detail 变成 `40 个被阶段判据校验的字段，声明的责任人与产出方正文里的填法两两对齐`；全套仍 `19/19`（`合计: 19 项通过 / 0 项失败`） |
| A-E2 | 在 A-E1 基础上，抹掉 `why` 在产出方正文里的教学（把 `roles/scribe.md` 与 `skills/decision-ledger.md` 里的 `` `why` `` 改成 `~~why~~`） | `C15 FAIL`：`↳ A9.why 出现在阶段退出判据里，但产出方 scribe 的角色文件与它拥有的技能正文里都没出现这一栏——没人被要求填它，判据永远无法满足，链会断`；`合计: 18 项通过 / 1 项失败` |
| A-E3（对照） | 同样的注入，**不扩**，用原版 19 门控 | `C15 PASS`，全套 `19/19`（`A9.why` 不在门控集合里，注入不进 C15 的扫描范围） |

补充测量（脚本口径，直接对 registry 文本）：按 `C15` 的 `taught` 判定（`` `field` `` 出现在「产出方角色文件 + 它拥有的全部技能正文」），**40/40 个字段当前都判定为 taught**。也就是说：今天扩到 40，不会新增任何红；A-E2 说明扩了以后，未门控字段的「教学被抹掉」才会被抓住。

另记一条实验里看到的文本行为：`C15` 的失败消息模板固定写「出现在阶段退出判据里」；在 A-E2 里 `A9.why` 并不在任何判据里，消息仍这么写。这是消息模板与扫描集合解耦后的现状，原文见 `scripts/check-closure.py:757-762`。

---

## B · 三条产物形态仍然没有箭头

口径：round-2 verify 报告 §5.2 的 18 行；「有箭头」= 该技能的 `@技能id` 出现在某一个产物 `embodiment` 字符串里（9 个产物的 `embodiment` 在 registry.yaml:90、:112、:134、:159、:187、:209、:230、:254、:282）。
独立复算：**15 行有箭头，3 行没有**，与 verify 报告 §3 第 9 条一致。没有箭头的三行：`arena`、`git-workflow-and-versioning`、`teach`。

搜索口径（全库 tracked 文件）：`@arena` / `@git-workflow-and-versioning` / `@teach` 在 `embodiment` 字符串中的命中数均为 0。

### B.1 `arena`（skills/arena.md；registry.yaml:894-901，`outputs: [A6]`）

**正文产出了什么：**
- skills/arena.md:31：「产出 **A6（实现候选）**：一份合成后的制品，外加一份放在它旁边的简短合成记录。」
- skills/arena.md:37：「合成记录要含：基底与选择理由、交叉评判的推荐、嫁接清单（标明来源候选）、驳回清单、收敛或发散的判读、验证结果。」
- 产生过程另有「评分表」（skills/arena.md:21：「评分表是后面选优者的工具，候选本人看不到它」）与「交叉评判」的推荐（skills/arena.md:23：「它只拿到评分表和候选的位置标签，逐条打分并给出推荐基底加理由」）。

**现在被谁接住：**
- 全库搜 `合成记录` / `交叉评判` / `评分表` / `嫁接清单` / `驳回清单` / `收敛或发散`：**除 skills/arena.md 自身外零命中**。
- `A6` 的 `embodiment`（registry.yaml:230-231）逐项点名了 `@incremental-implementation`、`@deprecation-and-migration`、`@ci-cd-and-automation`、`@prototype`、`@tdd`、`@build-the-lever`，**没有 `@arena`**；`A6` 四栏 notes（registry.yaml:212-215）里，`change` 说「点名列全每一样东西」，`known_gaps` 说「知道自己没做什么」——都不是「合成记录」的承载体。
- **结论证据：合成记录/评分表/交叉评判推荐没有对应字段或 embodiment；没有任何一处声明它在哪一栏落。**

### B.2 `git-workflow-and-versioning`（skills/git-workflow-and-versioning.md；registry.yaml:960-967，`outputs: []`）

**正文产出了什么**（skills/git-workflow-and-versioning.md:32-40，原文）：
- :34「本技能不产出 A8 类的凭据；它交付的是版本控制层的结构，随决策台账留存：」
- :36「提交序列：每个提交一行——它对应 A5 的哪一片、做了哪一件逻辑事、验证到哪一步。」
- :37「分支与合并：分支名、开出点、合并点、存续时长。」
- :38「忽略清单的覆盖范围，以及本轮是否发生凭据形态内容的误入（若有，写明处置）。」
- :39「发布时：版本号及其依据（破坏性／新增／修复）、标签名、变更日志条目、以及「故意没做的」那一段。」
- :40「未提交残留的清单：有就写明为什么留着。」
- 头部 skills/git-workflow-and-versioning.md:5 写「产物：无」；registry `outputs: []`（registry.yaml:960-967）。

**现在被谁接住：**
- 全库搜 `提交序列` / `分支与合并` / `残留的清单`：**除本技能正文外零命中**；`变更日志` 的其它命中（skills/documentation-and-adrs.md:62、:86；skills/source-driven-development.md:27）都讲的是别的事（下游既有物、调研来源）。
- `A9` 的 `embodiment`（registry.yaml:282-283）点名了 `@document-mapping`、`@shipping-and-launch`、`@documentation-and-adrs`，**没有 `@git-workflow-and-versioning`**；它只说「原始 git 历史仍属 `A6`」。
- `A9.result` 的 P6 判据（registry.yaml:397）确实覆盖了这套输出的**一段**：「记下了发布动作与回滚路径，且回滚路径已被确认可执行」。
- **结论证据：发布动作与回滚路径被 `A9.result` 的 P6 判据接住；提交序列、分支与合并、忽略清单覆盖、版本号依据、标签名、变更日志条目、「故意没做的」、未提交残留清单，没有对应字段或 embodiment 声明。**

### B.3 `teach`（skills/teach.md；registry.yaml:1017-1024，`outputs: []`）

**正文产出了什么**（skills/teach.md:64-71，原文）：
- :66「无产物——它不产出文件。但**没有交付物就不算讲完**，交付物都在对方那边，是两样：」
- :68「**对方脑子里的模型**：讲完之后他能不能用自己的话把要点说出来；每一个「因为」都能指回 A2 的一条 claim 或一条锚点；「还没查清」的部分被明说，而不是被含糊过去。」
- :69「**对方手上的东西**（目标是学会时）：他**做出了一个东西**——一道题收到的正确反馈、一段在自己环境里跑通的步骤、一次真实场合的练习。讲解稿、笔记、参考件都是**给他用的材料**，不是交付物；把材料当成交付物，等于把「我讲完了」冒充成「他学会了」。」
- :71「考古途中的新决策与新理由，追加进 A9（只追加，见 `decision-ledger`）。」

**registry 里 `outputs` 是不是真空的：**
- `outputs: []`（registry.yaml:1024 行附近；skills/teach.md:5 亦写「产物：无」）。正文自己给的理由是「它不产出文件」——即「无文件产物」；但同一节又说「没有交付物就不算讲完」，并把两项交付物明确放在**对方那边**（:66、:68、:69）。
- **交付物现在落在哪：** 全库搜 `@teach` 的命中只有四处——roles/driver.md:126（技能表）、workflow/ribbons/expression.md:12（横切带技能清单）、registry.yaml:426 与 :439（角色的 `skills` 列表）。**没有任何产物 `embodiment` 或字段提到 teach 的这两项交付物或它的材料（讲解稿/笔记/术语表/速查/图解）。** 唯一被指到落点的是「考古途中新产生的决策与理由 → A9」（skills/teach.md:71）。
- **结论证据：`outputs: []` 与正文「不产出文件」一致；正文同时声明的两项「交付物」（对方脑子里的模型、对方手上的东西）与参考件材料，在 registry 的产物/字段模型里没有承载体。**

---

## C · `A3.freshness` 到底有没有被任何东西保鲜

### C.1 谁写、谁读（file:line 全量）

**写（正文要求填它的地方）：**
- roles/architect.md:52：「`freshness` | 上次与代码核对的时间。**过期不更新的地图比没有地图更坏**，因为人会信它。」（architect 是 A3 的 `producer`，registry.yaml:123）
- skills/feature-map.md:74：「`freshness`：上次与代码逐条核对的时间，以及这一轮覆盖了几条能力、……」
- skills/feature-map.md:86：「建完就再也不管：应用一变，地图当场过期。地图的保鲜循环和建它一样重要。」
- roles/architect.md:95（技能表）：「`@feature-map` 能力地图 | 建 / 保鲜 `A3`。」

**声称「分工是死的」的地方（派生/说明）：**
- workflow/registry.yaml:140（notes，原文见 §A）
- docs/artifacts.md:40（registry notes 的派生视图）
- workflow/phases/P1.md:37（同上，派生视图）

**读（把它当输入/条件用）：**
- 全库 raw grep `freshness` 命中仅：roles/architect.md:52、skills/feature-map.md:74、skills/document-mapping.md:26、docs/artifacts.md:40、workflow/registry.yaml:132/140、workflow/phases/P1.md:37。**没有任何技能把 `A3.freshness` 的值当输入读。**
- 语义上「看地图过没过期」的地方（都没有点名该字段）：skills/verification-suite.md:16「地图不存在或已过期就先对齐地图再验证」；roles/verifier.md:45；roles/cartographer.md:34；roles/adversary.md:56「看到 `A3` 过期，回报，不在这里展开」；roles/architect.md:81「不在 `A3` 与代码不一致时宣布 `P1` 完成」。
- skills/document-mapping.md:26 把它当「下游映射必须保留的纪律」之一列出（「例如 A9 台账必须只追加、A4 判据必须可判定、A3 必须有 freshness」）——要求语句，不是读取方。

**判据侧：** `A3.freshness` 出现在 **0** 条阶段 `exit_criteria` 里（§A.0 的机械复算）。

### C.2 README 阶段表 vs registry / 派生视图

| 处 | 原文 | 对照 |
|---|---|---|
| README.md:70 | 表头：`| | 阶段 | 产出 | 退出判据（摘要） |` | — |
| README.md:77 | P5 行：`三态判定；能力地图已保鲜` | registry P5 的 4 条 `exit_criteria`（registry.yaml:381-384）是 `A8.verdict` / `A8.subject` / `A8.frame_alignment` / `A9.actor`；**没有保鲜** |
| workflow/registry.yaml:378 | P5 `purpose`：「在真实目标上跑出凭据，并把能力地图与代码重新对齐。」 | 派生视图 workflow/phases/P5.md:3 与它一致；但 `purpose` 不是判据 |
| workflow/phases/P5.md:22-25 | 退出判据 4 条，同 registry | 派生视图与 registry 一致，**没有 freshness** |
| workflow/phases/P6.md:27（= registry.yaml:398） | 「……地图的更新是**下一次 P1** 的活，不在 P6 的判据里（P6 没装 architect，要求它更新是越权）」 | P6 明确把地图更新推到下一次 P1 |

证据表明：README 把「能力地图已保鲜」写在**退出判据（摘要）**一列，而 registry 与 `workflow/phases/P5.md`、`P6.md` 的退出判据里都没有这条。

### C.3 保鲜循环还产不产出「地图已过期」信号、产出了有没有人接

- 信号的生产端：skills/verification-suite.md:33「8. **保鲜循环。** 地图在系统改动的那一刻就开始烂。定期过一遍：按能力分派并行读源码的人……标出疑似文档漂移并附引用、给出一条现场验证配方；然后由协调方亲自把**每个**能力真跑一遍。」
- 信号的落点：skills/verification-suite.md:48-50「**`frame_alignment`**：**未覆盖的能力清单**逐条列出……以及**清单与现实不符的条目**。这张清单是本字段的一部分，不是另出一份文档。它是 verifier 唯一能对 `A3` 做的事——**不得直接改地图**。」以及 skills/verification-suite.md:53（`scope` 列覆盖了哪些能力 id）与 :54（「只记录，不改地图——`A3` 归 `architect`」）。
- 信号被谁接住：`A8` 的消费者是 `P6`（registry.yaml:243-244）；`A8.frame_alignment` 被两条判据门控——P5 `verify: A8.frame_alignment 已显式记录（写「无」也要写出来）`（registry.yaml:383）、P6 `verify: A8.frame_alignment 非空……`（registry.yaml:398）。P6 判据同时写明「地图的更新是**下一次 P1** 的活」。
- 下一次 P1 是否接：P1 的 `required_inputs` 是 `[A1, A2]`（registry.yaml:327），P1 的 6 条判据（registry.yaml:329-333 + :317 的 A9.actor）里没有任何一条点名 `A8` / `frame_alignment` / `A3.freshness`。roles/architect.md:7 写了 architect「也服务于 `P2`（切片时的落点）、`P5`（地图保鲜）」，但 P5 的 `default_roles` 是 `[verifier]`（registry.yaml:385），P5 判据里没有涉及 architect 的动作。
- **证据结论：保鲜循环产出的信号是 `A8.frame_alignment`；该信号在 P5/P6 被要求记录/非空；「把偏差变回地图（更新 `A3`）」这一步在判据层没有接收方。**

### C.4 「把 architect 装进 P6」在图上的实测

P6 现状：`required_inputs: [A3, A4, A5, A6, A7, A8, A9]`（registry.yaml:394）、`default_roles: [verifier, scribe]`（registry.yaml:399）、`produces: []`（registry.yaml:404）。A3 的 `consumers` 已包含 P6（registry.yaml:124-128），`A3.producer` = architect（registry.yaml:123）。

四个受控实验（都在 `/tmp/expC*`，每次先跑 `scripts/render.py` 再跑两个 checker）：

| 实验 | 改动 | 结果 |
|---|---|---|
| C1 | P6 `default_roles: [architect, verifier, scribe]`（只加人） | `render.py` OK；closure `19/19`、consistency `7/7`，**零新增红、零新增覆盖** |
| C2 | C1 + P6 增一条判据 `write: A3.freshness 由 architect 在本阶段更新` | `C13 FAIL`：`↳ P6 声明要写 A3，但它不由本阶段产出（主产出方 architect，本阶段产出 []）——越权写。验证偏差请写进本阶段自己产出的证据字段`；`C15` 门控字段 19→20 且 PASS |
| C3 | C1 + P6 增一条判据 `verify: A3.freshness 已保鲜`（不加 produces） | closure `19/19`、consistency `7/7` 全绿；`C15` 门控字段 19→20（`A3.freshness` 成为被门控字段，产出方 architect 正文里教了它，C15 PASS）；派生 `workflow/phases/P6.md:29` 出现该判据 |
| C4 | C1 + P6 `produces: ["A3"]` + 同 C2 的 `write:` 判据 | render OK；closure `19/19`、consistency `7/7` 全绿（C13 的「本阶段产出」条件被满足后不再报越权写） |

写权相撞的机制证据（`C13` 实现，scripts/check-closure.py:644-676）：`C13` 判定「`write:` 不得指向本阶段不产出的产物」，以**阶段级 `produces`** 为准，不以「本阶段装了什么角色」为准；`verify:` 前缀的判据不参与该检查。所以：
- 只把 architect 装进 P6（C1）：不改任何检查结果。
- 要让 P6 出现一条「写 `A3.freshness`」的合法判据：需要把 `A3` 加进 P6 的 `produces`（C4），而 `A3` 同时也是 P1 的产出物——`C3`/`C4` 在该配置下未报阶段图问题（实测 C4 全绿）。`C2` 与 C4 的差别只有 `produces` 这一项。
- `S7`（横切带覆盖）不参与：architect 的 `ribbons` 是 `[]`（registry roles 段），加它进 P6 不产生 S7 义务；实测 C1 的 `S7 PASS`。
- registry.yaml 里 P6 现有 `produces: []` 位于块尾（:404），与 `hard_rules` 之后；实验 C4 第一次插入的 `produces: ["A3"]`（插在 `exit_criteria` 前）被这个块尾键**按 YAML 重复键覆盖**（`yaml.safe_load` 取最后一个），修正后才生效。同类重复键在 registry 里另有一处：`tier-sizing` 的 `note:`（见 §D.4）。

---

## D · 冷启动 / README 的说法，一共几个版本

搜索范围：全部 tracked 文件（`git ls-files`，含 `docs/`、`workflow/`、`README.md`、`roles/`、`skills/`、`scripts/`）。`.pi/` 不进。

### D.1 「C7/C9 在下游会怎样」

| # | 处 | 原文（节选） | check-closure.py 实际行为 | 与代码一致？ |
|---|---|---|---|---|
| 1 | README.md:263-268 | 「`SKIP` 是第三种状态……现在有两项会 SKIP：`C7`……与 `C9`……**不随安装分发**，所以在下游仓库里判不了。……**在下游仓库里它们必须 SKIP。**」 | `skip=True` 全库 **0 处使用**（grep `skip=True`：无命中）；`SKIP` 只有渲染分支（check-closure.py:165），没有检查项会走进去。干净 clone（无 `upstreams/`）实测：`C7 PASS`、`C9 PASS`（见基线 §0.2） | **不一致（FAIL）** |
| 2 | README.md:139 | 「C7 \| 101 条上游处置与 `upstreams/` 文件系统一一对应」 | `C7` 的实际对照是「处置表 ↔ `upstreams.lock.yaml` 的 skill 索引」（check-closure.py C7 段：`listed` vs `lock_skills`）；`upstreams/` 只在 `C9` 的 `if (ROOT/"upstreams").is_dir()` 分支里被读（check-closure.py C9 段） | **不一致**（对象是锁文件；文件系统对照在 C9 且需克隆在场） |
| 3 | README.md:141 | 「**C9** \| **每条 sources 指向真实存在的上游文件**」 | 下游（无 `upstreams/`）：逐个 `sources` 判 `src in lock_skills`（索引成员资格），不检查文件存在；本库（`upstreams/` 在场）：检查文件存在 + `sha256` + 各仓 pin | **部分一致**：有克隆时一致；下游只核索引，不核「真实存在」 |
| 4 | README.md:274 | 「由 `check-closure.py` 直接对 `upstreams/` 的文件系统核对」 | 同 #2/#3：路径是「处置表 → 锁文件 →（有克隆时）上游文件」的链，不是直接 | **不一致**（「直接」） |
| 5 | docs/coldstart.md:57-63 | 「在下游，`C7`……与 `C9`……照样是 `PASS`，不是 `SKIP`。……**所以：漏拷 `upstreams.lock.yaml` 的下游，`C7` 会直接红并告诉你「锁文件过期」**」 | 结论方向一致（无 SKIP；缺锁会红）。实测缺锁时 `C7` 的消息是：`缺少 upstreams.lock.yaml——没有它，处置表在干净 clone 里无处核对`；`锁文件过期` 这句话只在「锁在、但索引与处置表对不上」的分支里出现（check-closure.py C7 段）。另：缺锁时 `C9` 与 `C20` 也会红，不止 `C7` | **部分一致**：PASS/红 的方向一致；消息文本、以及「只有 C7 红」两点不一致 |
| 6 | docs/coldstart.md:60 | 「有克隆的本库里，这两项会**额外**逐条比 sha256 与 pin」 | `sha256`/pin 的比较只在 `C9` 里（C9 段源码）；`C7` 在有克隆时行为不变。实测：挂上 `upstreams/` 后只有 `C9` 的 detail 追加 `；并已逐条比对 sha256 与 pin` | **部分一致**（「这两项」→ 实际只有 `C9`） |
| 7 | docs/coldstart.md:65-67 | 「v2.0.5 之前这两项是 `SKIP`。锁文件随包分发之后 `SKIP` 分支已经不可达……**要么 `PASS`，要么红。**」 | 一致 | **一致** |
| 8 | skills/coldstart.md:42 | 「**`upstreams.lock.yaml` 跟注册表一起拷**——它是 `C7` / `C9` 在下游能跑的唯一依据，漏拷这两项直接红。」 | 方向一致；缺锁时 `C7`/`C9`/`C20` 都红（「这两项」未含 C20） | **部分一致** |
| 9 | skills/coldstart.md:48-52 | 「在下游是 `PASS`，不是 `SKIP`。……漏拷锁文件的后果是**红**（并提示「锁文件过期」），不是 `SKIP`。**没有「因为下游没有上游所以跳过」这种状态**」 | 方向一致；消息文本同 #5 | **部分一致** |
| 10 | skills/coldstart.md:63-65、:77-79 | 「包括 `C7` 与 `C9`——它们对随包分发的 `upstreams.lock.yaml` 判……见到 `SKIP` 说明装法或检查器有问题」 | 一致 | **一致** |
| 11 | scripts/sync-upstreams.sh:9-13；upstreams.lock.yaml:1、:13 | 「锁文件是随 release 分发的」「干净 clone 出来的下游要能跑检查，靠的就是这份锁文件」 | `upstreams.lock.yaml` 被 git 跟踪（`git ls-files upstreams.lock.yaml` 命中），不在 `.gitignore`；干净 clone 里它在 | **一致** |

**「C7/C9 在下游会怎样」的不同版本计数：**
- 下游**结果**的说法有 **2 个互不相同的版本**：(a) 「必须 SKIP」（README.md:263-268，与代码矛盾）；(b) 「是 PASS，SKIP 不可达」（docs/coldstart.md:57-67、skills/coldstart.md:48-52/63-65/77-79，与代码一致）。
- 在 (b) 内部，**机制描述**还分岔出 3 个互不相同的说法，没有一个完整等于代码：README.md:139 的「与 `upstreams/` 文件系统一一对应」、README.md:141 的「指向真实存在的上游文件」、docs/coldstart.md:60 的「这两项额外比 sha256 与 pin」。
- 另有 1 个共同的细节错误出现在两个 coldstart 里：「漏拷锁文件」时提示的是「锁文件过期」（docs/coldstart.md:61、skills/coldstart.md:50），而代码在缺锁时输出的是「缺少 upstreams.lock.yaml……」。

### D.2 「`render.py` 要不要」

| 处 | 原文（节选） | 与代码/彼此一致？ |
|---|---|---|
| docs/coldstart.md:49 | 「`render.py` \| **要**。派生视图（阶段契约、横切带、产物表、闭包报告）全部由它从注册表生成，下游改了注册表就得重跑它」 | 一致（`render.py --check` 在 tag 上 `OK（12 个派生文件逐字一致）`；12 = 7 阶段 + 3 横切带 + `docs/artifacts.md` + `docs/closure-report.md`） |
| docs/coldstart.md:52 / skills/coldstart.md:43 | 「`sync-upstreams.sh` / `_render-lock.py` \| **不拷**。它们是本库维护上游用的」 | 一致（`sync-upstreams.sh:16-17` 只维护锁；`_render-lock.py:33` 没有 `upstreams/` 就 `sys.exit`） |
| skills/coldstart.md:43 | 「**生成脚本也要拷**——派生视图全部由它从注册表算出来」 | 一致 |
| skills/coldstart.md:44 | 「**派生文件由脚本重新生成，不手工编辑**」 | 一致（与 `AGENTS.md:22-25`、`render.py --check` 的用途一致） |
| README.md:58、:124、:288；AGENTS.md:22-25、:49 | 脚本清单 / 自检命令 / 维护命令 / 本库纪律 | 一致（README:288 与 AGENTS:49 是本库维护口径，不是下游口径） |

**结论：没有发现互不相同的版本；全部说法与实测一致。**（grep 全库 `render.py` 未发现「下游不需要 render.py」这类相反说法。）

### D.3 「`upstreams.lock.yaml` 要不要」

| 处 | 原文（节选） | 与代码一致？ |
|---|---|---|
| docs/coldstart.md:51 | 「随注册表一起拷。下游没有三仓克隆，靠这份锁文件核对处置表」 | 一致（干净 clone 有它，`C7`/`C9` PASS） |
| docs/coldstart.md:58-59 | 「它核对的 `upstreams/` 不随包分发，但 `upstreams.lock.yaml` 随包分发——所以这两项在干净 clone 里直接对锁文件判，**实测全绿**」 | 一致 |
| skills/coldstart.md:42、:49-50、:63、:78 | 同义（跟注册表一起拷；下游判得了） | 一致 |
| scripts/sync-upstreams.sh:11-13；upstreams.lock.yaml:1、:13 | 锁文件随 release 分发 | 一致（且文件被 git 跟踪，未被 `.gitignore` 挡） |
| （无人提及） | — | 实测**缺锁时 `C20` 也红**（`技能 grilling 的来源段提到 upstreams/...，但它不在上游锁文件里`）；`docs/coldstart.md` 与 `skills/coldstart.md` 只提 `C7`/`C9` |

**结论：就「要不要」本身没有互不相同的版本，全部一致；缺锁时的连带红（`C20`）没有文档。**

### D.4 「判档判据」

| 处 | 原文（节选） | 与 check-closure.py 实际行为 | 判定 |
|---|---|---|---|
| docs/coldstart.md:82-95 | 「## 第 4 步：判档……小→`solo`，中→少量几个角色，大→全链条。**不写数字。**……判据是**这次变更的风险与仓库成熟度**……**「闭环完整」不是判据，是结果**……」（第 :93-94 与 :95 是同一句话的两次出现） | `check-closure.py` 只在 `C18` 里判「开工前技能不依赖阶段产物」；`C18` 的 `pre_phase_skills` 是**硬编码集合** `{"tier-sizing","coldstart"}`（check-closure.py:790-792），detail：`2 个开工前技能不依赖任何阶段产物` | 计数/范围见下 |
| skills/coldstart.md:26、:38、:53 | 「这次任务会经过哪几个阶段」「跑一遍 `tier-sizing`，按这次变更的风险与仓库成熟度定……档位只决定装几个、怎么排」「档位判据……记进 A9」 | 与 docs 同向 | 一致 |
| roles/driver.md:17、:46-57、:121 | 「判档——这次任务有多大」「档位用 `@tier-sizing` 的**六项触发矩阵**判」「前 3 项是硬闸门……判断的全部内容在 `skills/tier-sizing.md`」；表里含 `新增文件上限` 列：2 / 5 / 12 | 没有 checker 读角色文件这一段 | 与 skills/tier-sizing 一致；与 docs/coldstart:91「不写数字」的关系见下 |
| skills/tier-sizing.md:9、:16-17、:21 | 「每个新任务开工前，先判这一轮装多少」「**A1 诉求陈述**（`inputs` 里唯一的产物）：四个字段都用得上……**A1 拿不到就退回**」「从 `A1.done_meaning` 出发」 | registry `tier-sizing.inputs: []`（registry.yaml:1046）；`C18` 把 tier-sizing 当开工前技能、要求它的 inputs 不被任何阶段产出——inputs 为空所以 **PASS**。**没有任何 checker 读技能正文的「开工前要拿到」段**（`C14` 只解析技能头部的「产物：」声明，check-closure.py C14 段） | **不一致**（正文要求 A1；registry/C18 注释把 A1 依赖当循环） |
| workflow/registry.yaml:1046、:1049-1052 | `inputs: []`；`note: >-`「inputs 为空是刻意的——判档发生在 A1 之前，依赖 A1 就成了循环。判据用的是「Owner 说的那一句话」加上仓库现状，不是 A1 的四个字段。」 | 该 `note` 在同一技能块里**被第二个 `note:` 键覆盖**（registry.yaml:1055「本库原创——上游三仓没有对应物……」）；`yaml.safe_load` 解析结果里 `tier-sizing.note` = 后者，:1050-1052 只作为文件文本存在，不出现在解析后的数据里。无 checker 读技能 note | 记录事实 |
| skills/tier-sizing.md:24-42、:45-49、:59 | 六项触发矩阵、三档表（含 `新增文件上限` 2/5/12）、「**闭环完整是结果，不是判据**」「编号一律不写：编号会诱导凑数」「档位能被人从 **`A1` 的两个字段**复算出来」 | 无 checker 对应 | 与 docs/coldstart:91「不写数字」的关系：两处并存；「数字」在 docs 里指编号/凑数，在技能表里是文件上限；本报告**无法只凭文本判定是否实质冲突 → `UNVERIFIED`** |
| README.md:149 | 「**C18** \| **开工前要跑的技能不依赖开工后才有的产物**（防判档循环）」 | 实现只覆盖 2 个硬编码 id；`C18` 自己的 detail 报 `2 个开工前技能`。全库 `phase: null` 的 driver 技能有 5 个（`teach`、`context-management`、`tier-sizing`、`document-mapping`、`coldstart`） | 描述比实现对宽；是否算不一致取决于「开工前技能」的定义 → 记录事实 |
| check-closure.py:779-787（注释） | 「判档循环：tier-sizing.inputs 曾经是 [A1]，而 A1 由 P0 产出，但 P0 开工前就得先判档决定装谁——用结果定前提」「teach / document-mapping 这类在 P0 之后跑的 driver 技能依赖 A1/A2 是对的」 | 与 registry 的 note（:1050-1052）同向；与 skills/tier-sizing.md:16/21 反向 | **不一致**（同一件事在三处有不同说法：技能正文、registry 注释、C18 注释） |

**邻近记录（不属于四件事字面范围，但同类）：** registry.yaml:1056-1060 `document-mapping` 是 `phase: null` + `inputs: [A1]`；skills/coldstart.md:37 说冷启动里「跑一遍 `document-mapping`」，docs/coldstart.md:73-78 把「把产物映射到下游」放在**第 3 步**、而「起 P0」在**第 5 步**；`C18` 按注释把 document-mapping 排除在检查之外（check-closure.py:786）。这是与判档循环同形的「开工前依赖 A1」，未被 `C18` 覆盖。

### D.5 明确未发现相关说法的文件

对下面这些文件做 `C7` / `C9` / `render` / `lock` / `锁文件` / `判档` / `SKIP` / `upstreams` 的逐文件 grep，命中如下：

- `docs/artifacts.md`：只有 `workflow/registry.yaml` 派生的 render 生成标记（:137）与 `置信档位`（:32，语义不同）。
- `docs/downstream-mapping.md`：**0 命中**。
- `docs/closure-report.md`：只有 render 生成标记（:45）与两处 `solo 档` 硬规则文本（:34、:35）。
- `workflow/ribbons/context.md`、`decision.md`、`expression.md`：只有 render 生成标记。
- `workflow/phases/P0.md`…`P6.md`：只有 render 生成标记；没有任何一处提到 `C7`/`C9`/锁文件/判档。

### D.6 相邻发现（不在四件事之内，仅记录）

README 同一批「自检」文字里的检查计数，与当前检查器实际输出不一致：

| 处 | 原文 | 实际 |
|---|---|---|
| README.md:25 | 「24 项检查（`check-closure.py` 17 项 + `check-consistency.py` 7 项）」 | 当前输出：closure **19** 项 + consistency **7** 项 = **26** |
| README.md:122 | 「`check-closure.py` # 17 项」 | 19 项 |
| README.md:129 | 「### 24 项检查各管什么」 + 表内 25 行（含 `C8`，无 `C19`/`C20`） | 当前输出没有 `C8`（`C8` 已退役，check-closure.py:812 注释只留编号历史），有 `C19`/`C20` |
| README.md:159 | 「**加粗的十二项**是……新增的」 | 表内加粗行 10 行 |
| README.md:232 | 「22 项检查全绿」 | 该段是 v2.0.1 历史叙述（`v2.0.1` 字样在上下文），非当前主张 |

---

## E. `UNVERIFIED` 项与补证条件

| 项 | 状态 | 补证条件 |
|---|---|---|
| A9 台账「工具层拒空」在非 `ledger.sh` 写法下的效果 | 未测（本报告只测了 `ledger.sh`） | 手写 TSV 空栏 + 跑任一 checker，观察是否有红 |
| `C9` 的 sha256 篡改检测（有 `upstreams/` 时） | 本轮未重新注入；只验证了该分支执行（detail 出现 `；并已逐条比对 sha256 与 pin`） | 在带 `upstreams/` 的副本上改一个被锁文件覆盖的文件内容，看 `C9` 是否红（round-3 verify 的 A2 注入做过） |
| docs/coldstart.md:91「不写数字」与 skills/tier-sizing.md 表内 2/5/12 是否实质冲突 | `UNVERIFIED`（文本无法判定所指） | 由人裁定「数字」指编号还是文件上限 |
| README:139/141/274、「锁文件过期」消息文本、docs/coldstart:60「这两项」是否为「需修」而非「口径差异」 | 证据齐（见 §D.1），判定为「与代码不符」；是否修属人审 | — |
| 另外两个 worker 未提交的检查器改动会带来的行为变化 | 不在本报告范围 | 他们提交后重跑 §F |

## F. 复现本报告

```bash
# 基线（tag 检出）
rm -rf /tmp/inv0929-final && git clone -q <repo> /tmp/inv0929-final
cd /tmp/inv0929-final && git checkout 29a50e4
python3 scripts/render.py --check
python3 scripts/check-closure.py        # 19/19
python3 scripts/check-consistency.py    # 7/7

# 基线 B：挂上只读克隆（只影响 C9 的对照深度）
ln -sfn <repo>/upstreams /tmp/inv0929-final/upstreams
python3 scripts/check-closure.py | grep C9   # 追加「并已逐条比对 sha256 与 pin」

# A：门控集合复算与「扩到 40」实验
#   见 /tmp/expA（把 check-closure.py 的 gated 集合换成全部字段）
python3 scripts/check-closure.py | grep C15  # 40 字段版 PASS

# C：P6+architect 四个实验（各自副本）
#   /tmp/expC  C1：default_roles 加 architect            → 全绿
#   /tmp/expC2 C2：再加 write: A3.freshness              → C13 FAIL
#   /tmp/expC3 C3：再加 verify: A3.freshness             → 全绿，C15 门控 20
#   /tmp/expC4 C4：P6 produces 加 A3 + write 判据        → 全绿

# D：下游两态
cp -R /tmp/inv0929 /tmp/inv0929-nolock && rm -f /tmp/inv0929-nolock/upstreams.lock.yaml
cd /tmp/inv0929-nolock && python3 scripts/check-closure.py | grep -E "C7|C9|C20"   # 三项红
mkdir -p /tmp/inv0929-archive && cd /tmp/inv0929 && git archive 29a50e4 | tar -x -C /tmp/inv0929-archive
cd /tmp/inv0929-archive && python3 scripts/check-closure.py | grep -E "C1|C7|C9"   # C1 红（无 .git），C7/C9 PASS
```

---

*取证范围（Round 1）：`git ls-files` 的 tracked 文件；`.pi/` 不计入库内容。工作树零改动；三条未提交的检查器改动未触碰。*

---

# R · Round 2（0929 续 · pane 重建后的新会话）

任务：①「偏差交回下一次 P1」有没有承载体；②21 个未门控字段的三堆划分（决定 C15 覆盖面）；③最高优先——全库 SKIP 口径与当前代码是否一致。
本节的被测对象钉死在 **commit `12aecf1`**（`fix(0929-b)`，2026-09-28 20:36:19 +0800，Round 2 期间为 HEAD；无 tag）。Round 1 的 v2.0.6 测量记录原样保留。

## R0. 基线变化、时间线与取代关系

### R0.1 取证期间仓库的时间线（+0800）

| 时刻 | 观察到的状态 | 对取证的影响 |
|---|---|---|
| 20:33 | 启动。HEAD=`e7f6de1`；工作树 ` M`：`check-closure.py`/`check-consistency.py`/`ledger.sh`（impl-checkers 在改） | 检查器行为不取工作树；文件证据可用 |
| 20:36:12 | 工作树新增 `workflow/registry.yaml`、`roles/architect.md`、`workflow/phases/P1.md`、`docs/closure-report.md` 改动（未提交）——即「偏差交回 P1」的承载体 | 我在此前对 `e7f6de1` 的核对结论是「无承载体」；此后承载体出现（R1） |
| 20:36:19 | 上述四处改动连同三个脚本改动一起提交为 **`12aecf1`** | Round 2 基线确定 |
| 20:40:56 起 | 工作树又出现 `scripts/check-closure.py` 未提交改动（+18/−2：C15 detail 自动列出未门控字段，oracle 裁决 Q2）；其后 `docs/ledger.md` 也出现改动 | 这两处**未提交、未采用为产品证据**；只作为 R2.1 的巧合性交叉核对 |

### R0.2 Round 1 结论的取代关系

| Round 1 结论 | 现状 | 处理 |
|---|---|---|
| §C.3「P1 不读 `A8.frame_alignment`，『交回下一次 P1』在判据层没有接收方」 | `12aecf1` 补上了承载体 | **已被取代**，见 R1 |
| §D.1 #10「『SKIP 分支不可达』与代码一致」 | `12aecf1` 已提交 C1/C9 的可达 SKIP 分支 | **已不成立**，见 R3 |
| §D.1 表格里 README 的行号（139/141/274） | `e7f6de1` 改过 README，行号整体下移 | 当前行号 144/146/285，见 R3.3 |

Round 1 中未被本轮代码改动触及、且 Round 2 已复算的结论：40/19/21 字段划分（R2）、A9 工具层拒空/自动生成（R2.2）、缺锁文件时 C7 的实际消息文本（R3.1）。

Round 2 基线（`12aecf1` 干净检出 + 当前工作树脚本之外的提交内容）实跑：`render.py --check` → `OK（12 个派生文件逐字一致）`；`check-closure.py` → `20 通过 / 0 失败 / 1 跳过 / 21`（唯一 SKIP 是无 `.git` 副本里的 C1，见 R3.1 场景 A；在本库里因 HEAD 未打 tag，C1 为 FAIL，打 tag 即消）；`check-consistency.py` → 7/7。

> 口径说明：Round 2 的所有行为证据取自 `/tmp` 的 `git archive 12aecf1` 检出（无 `.git`，脚本由该 commit 解出），以及一个带 `.git` 的 `git clone`。工作树上的未提交改动不参与任何行为判定。

## R1. 优先项 1：「偏差交回下一次 P1」有没有承载体

### R1.1 承载体已在 `12aecf1` 落地（file:line）

- **判据**：`workflow/registry.yaml:367`（P1 第 6 条退出判据，原文）
  > `verify: 上一轮的 A8.frame_alignment 里的每条地图偏差都已逐条处置——修订了 A3，或在 A9 写下不修的理由与裁决；没有逐条处置不得宣称本次 P1 完成。首次 P1（不存在上一轮 A8）时本条不触发`
  派生视图 `workflow/phases/P1.md:25` 逐字同句。
- **角色**：`roles/architect.md:103-109`（「怎么开工」新增第 2 步）：「**先看上一轮的 `A8.frame_alignment`。** 这是我作为地图主人的**唯一收件箱**……逐条处置，每条两种结果：确实过期 → 修订 `A3` 对应条目，**并更新 `A3.freshness`**；不改 → 在 `A9` 写下不修的理由（或 Owner 的裁决），**不许无声跳过**。」
  以及 `roles/architect.md:82-83`（「我不做的事」新增）：「**收到上一轮 `A8.frame_alignment` 却不当场处理。** 那是我的收件箱，不是别人的垃圾。」
- **派生报告**：`docs/closure-report.md:17`，A8 一行「在哪一步被校验」由 `P5、P6` 变为 `P1、P5、P6`。
- **落地机械核对**（`12aecf1` 检出实跑）：C4 = `26 条退出判据，0 处无法解析的引用`（含新增那条）；C13 = `26 条判据全部显式声明了 write/verify`；`render.py --check` OK。

### R1.2 `12aecf1` 之前确实没有承载体（复验，非推测）

- `git show e7f6de1:workflow/registry.yaml | grep -c '上一轮的 A8.frame_alignment'` → `0`；`git show e7f6de1:roles/architect.md | grep -c '收到上一轮'` → `0`。
- `git log -S '上一轮的 A8.frame_alignment' -- workflow/registry.yaml` → 只有一处添加：`12aecf1`。
- `e7f6de1` 的 P1 仍是 `required_inputs: [A1, A2]`（行号 360），判据里没有 A8。

即：驱动报文里问的「承载体」，在 `e7f6de1` 上答案确实是「没有」；在 `12aecf1` 上是「判据 + 角色都有了」。

### R1.3 承载体在数据流图上仍缺一格（事实，不是判定）

- `12aecf1` 上：A8 `consumers` 仍为 `[P6]`（`workflow/registry.yaml:276-277`）；P1 `required_inputs` 仍为 `[A1, A2]`（:360）。
- 受控实验（`12aecf1` 检出副本，只改 registry）：
  | 实验 | 改动 | 结果 |
  |---|---|---|
  | E1a | P1 `required_inputs` 加 `A8` | `C3 FAIL`（A8 不在 P1 的上游）+ `C11 FAIL`（A8.consumers 里没有 P1） |
  | E1b | A8 `consumers` 加 `P1`（不其余） | `C11 FAIL`（P1 既不 required 它也不产出它）；C3 PASS |
  | E1c | 两处同时加 | `C11 PASS`，但 `C3 FAIL`（A8 由 P5 产出，在 P1 下游） |
  结论：这条「上一轮 A8 → 本轮 P1」是**回边**，把它建进线性装配图会让 C3 红——与库内已有惯例一致：A7 的回边（`workflow/registry.yaml:271`）与 A9 里 `A8.verdict→P3` 的回边（:329）都写明「**刻意不建成消费关系**」。
- 与惯例的差别：已有两条回边各有一条 `rework:` 注记解释为什么不在 consumers 里；新增的 P1←上一轮 A8 这条**没有任何 registry 注记**，只存在于判据文本与角色正文。这是事实记录；是否要补注记由人审。
- 另一处细节：判据要求「在 `A9` 写下不修的理由与裁决」，A9 的主产出方是 `scribe`（`workflow/registry.yaml:302`），P1 `default_roles` 是 `[architect, scout]`（:369）。但 P1 本来就有 A9 判据（:368），architect 也已承担「冻结 `A4` 写进 `A9`」（`roles/architect.md:113`），所以这不是新缺口；C13 只核 `write:` 前缀，不核这类语义。

### R1.4 `A3.freshness` 的写方 / 读方现状（`12aecf1`）

- **写方**：`architect`（A3 的 producer）。正文：`roles/architect.md:52`（字段表）、`roles/architect.md:106`（新增：修订时「并更新 `A3.freshness`」）、`skills/feature-map.md:74`、`:86`；registry 注记 `workflow/registry.yaml:173`。
- **读方**：仍是**没有**。机械复算：`freshness` 出现在 0 条 `exit_criteria` 里（与 Round 1 相同）。新增的 P1 判据消费的是 `A8.frame_alignment`（偏差信号），**不是** `A3.freshness` 的值；没有任何判据要求 freshness 被更新或达到某个新鲜度。
- 所以：「偏差交回下一次 P1」现在有了消费端（R1.1）；但 `A3.freshness` 这个**时间戳本身**仍然只有生产端、没有读取端——它仍属 R2 的「软约束」堆。

## R2. 优先项 2：21 个未门控字段的三堆

### R2.1 机械复算（`12aecf1`，与 Round 1 完全一致）

口径与 C15 相同：字段对 `(A\d+, field)` 出现在任意阶段 `exit_criteria` 文本里即算门控。

- 产物字段 **40** 个；门控 **19** 个；未门控 **21** 个；退出判据 **26** 条（v2.0.6 时为 25，新增的正是 R1 的 P1 判据；它不改变门控集合——`A8.frame_alignment` 本来就被 P5/P6 门控）。
- 21 个未门控字段（逐字）：`A1.done_meaning, A1.unknowns, A2.claims, A2.evidence, A3.consumers, A3.freshness, A4.why, A5.edges, A6.change, A7.conditions, A7.stance, A8.claim, A8.environment, A8.observation, A8.scope, A9.decision, A9.evidence, A9.phase, A9.run, A9.subject, A9.why`。
- 交叉核对：工作树上有一份**未提交**的 C15 改动会在 detail 里自动列出未门控字段（20:40:56 观察到）；它列出的 21 个与上面逐字一致。该改动未采用为证据，只记为一处巧合性一致。

### R2.2 三堆（与 Round 1 相同，逐条证据见 Round 1 §A.1）

| 堆 | 数量 | 字段 id |
|---|---:|---|
| 真空 | **0** | — |
| 有软约束（产出方正文/notes 明确要求填；空着没有机制拦） | 15 | `A1.done_meaning`、`A1.unknowns`、`A2.claims`、`A2.evidence`、`A3.consumers`、`A3.freshness`、`A4.why`、`A5.edges`、`A6.change`、`A7.stance`、`A7.conditions`、`A8.claim`、`A8.scope`、`A8.observation`、`A8.environment` |
| 实际被别的东西约束着（仅当用 `scripts/ledger.sh` 写） | 6 | `A9.run`、`A9.subject`、`A9.phase`、`A9.decision`、`A9.why`、`A9.evidence` |

工具层约束在 `12aecf1` 上的复核：
- `scripts/ledger.sh:51-56`：`阶段 / 对象 / 决定 / 为什么 / 凭什么` 任一为空 → `exit 2`。实测：空 `why` → 退出码 2、消息「为什么 不能为空」。
- `scripts/ledger.sh:233`：`run` 用 `TPW_RUN` 或时间戳+pid 自动生成。实测写入行 `run=20260928T124138Z-pid:23952`。
- 前提不变：这两个约束只在走 `ledger.sh` 时生效；手写 TSV 空栏不会被任何机制发现（两个检查器都不读 `.decisions/`，`grep` 复核仍为 0 处）。

相对 Round 1 的变化只有一处：`roles/architect.md:103-109` 为 `A3.freshness` 增加了一条产出方要求语句（不改变分堆）。

### R2.3 C15 扩面实验在 `12aecf1` 上复跑

- 把 C15 的 `gated` 集合换成全部 40 个字段对后实跑：`C15 PASS`（`40 个被阶段判据校验的字段……两两对齐`），全套 `20 通过 / 0 失败 / 1 跳过`——**今天扩到 40 不会新增任何红**。
- 扩面能抓到的：把某个未门控字段的产出方教学抹掉（Round 1 §A.3 已用 `A9.why` 做过受控注入）。扩面**抓不到**的：字段值是否真的被填、是否非空（C15 只核「名字教过」，其 detail 自己也写了这个边界）。
- 结论层的事实：21 个字段今天**没有任何一条判据对它们持非空/质量约束**；15 个软约束字段的「要被填」只靠散文，6 个 A9 字段靠工具脚本且只在用该工具时生效。C15 覆盖面扩不扩，这个事实不变。

## R3. 优先项 3（最高）：全库 SKIP 口径与当前代码

### R3.1 `12aecf1` 上的行为矩阵（全部实测）

| 场景 | 构造 | C1 | C7 | C9 | 其他 | 合计 |
|---|---|---|---|---|---|---|
| A 无 `.git`、无 `upstreams/`、锁文件在 | `git archive 12aecf1` 解出 | **SKIP** | PASS | PASS（detail 自曝：未做实物 sha256/pin 对照） | — | 20/0/1 |
| B 同 A，删掉 `upstreams.lock.yaml` | — | **SKIP** | **FAIL** | **FAIL** | **C20、C21 也 FAIL** | 16/4/1 |
| C 无 `.git`、`upstreams/` 在但无 git 元数据 | 拷入 `upstreams/` 后删掉各仓 `.git` | **SKIP** | PASS | **SKIP**（pin 未核，逐仓列出原因） | — | 19/0/2 |
| D 有 `.git` 有完整上游克隆 | `git clone` + 软链接 `upstreams/` | FAIL（HEAD 未打 tag；打 tag 即消） | PASS | PASS（sha256 + 3 仓 pin） | — | 20/1/0 |

代码路径（`scripts/check-closure.py`，`12aecf1`）：C1 的唯一 skip 点是 `:290` 的 `skip=(not tag_checked and not miss)`；C9 的 skip 点是 `:628`，且 `:613` 明确 FAIL 优先（有真实不一致时 SKIP 不得掩盖）。C7 没有 skip 分支。

### R3.2 逐条说法与代码的一致性（`12aecf1`）

| # | file:line | 原文要点 | 与当前代码 |
|---|---|---|---|
| 1 | `docs/coldstart.md:57` | 「在下游，`C7` 与 `C9` 照样是 `PASS`，不是 `SKIP`」 | **一致**（场景 A 即下游代理；C7/C9 只依赖锁文件） |
| 2 | `docs/coldstart.md:59-60` | 「有克隆的本库里，这两项会**额外**逐条比 sha256 与 pin」 | **部分不一致**：实测只有 C9 做；且 pin 不可信时 C9 判 SKIP，不再是额外比对的 PASS（场景 C/D） |
| 3 | `docs/coldstart.md:61-62` | 「漏拷 `upstreams.lock.yaml` → `C7` 直接红并提示「锁文件过期」」 | **不一致**：实测 C7/C9/C20/C21 四项红；C7 的消息是「缺少 upstreams.lock.yaml——没有它，处置表在干净 clone 里无处核对」（`scripts/check-closure.py:523`）；「锁文件过期」（:528）是另一个分支（锁在但索引对不上） |
| 4 | `docs/coldstart.md:63-64` | 「任何一种情况下这两项都必须是 `PASS`，不能是「没查就当过了」」 | **不一致**：C9 有设计内的 SKIP（场景 C）。精神（不得冒充 PASS）被三态满足，字面「必须 PASS」已过时 |
| 5 | `docs/coldstart.md:65` | 「锁文件随包分发之后 `SKIP` 分支已经不可达」 | **不一致**：C9 SKIP 实测可达（场景 C）；C1 SKIP 也可达（场景 A/B） |
| 6 | `docs/coldstart.md:67` | 「现已改成实况：**要么 `PASS`，要么红。**」 | **不一致**：SKIP 是第三态，README:269 也这么写 |
| 7 | `skills/coldstart.md:48` | 「`C7` 与 `C9` 在下游是 `PASS`，不是 `SKIP`」 | **一致**（同 #1） |
| 8 | `skills/coldstart.md:50-52` | 「漏拷锁文件的后果是**红**（并提示「锁文件过期」），不是 `SKIP`……没有「因为下游没有上游所以跳过」这种状态」 | **方向一致、文本不一致**：红是真的、不是 SKIP 也是真的；但消息文本同 #3，且「没有跳过这种状态」只对「因为下游没上游」这一种理由成立 |
| 9 | `skills/coldstart.md:63-65` | 「**全部检查项 PASS。**……见到 `SKIP` 说明装法或检查器有问题，不说明「下游判不了」」 | **不一致**：「全部 PASS」与三态冲突（无 `.git` 的下游/导出目录里 C1 合法 SKIP，场景 A）；「见到 SKIP 说明装法或检查器有问题」把设计内 SKIP 一律当故障 |
| 10 | `skills/coldstart.md:77-79` | 「见到 `SKIP` 说明漏拷了锁文件或者检查器退化了，**两种都要当故障查**」 | **不一致**：漏拷锁文件实测是 **FAIL** 不是 SKIP（场景 B）；设计内 SKIP（C1 无 git、C9 pin 不完整）会被这句话误判成故障 |
| 11 | `README.md:269-270` | 「`SKIP` 是 `UNVERIFIED` 的一种……而不是「判定为通过」」 | **一致**（`skip=True` 渲染路径，`scripts/check-closure.py:173-187`） |
| 12 | `README.md:271-275` | 「早先版本把 C7/C9 在下游判成 SKIP……现在是 PASS，通过范围更小；C9 输出自曝范围」 | **一致**（场景 A 的 C9 detail 逐字自曝） |
| 13 | `README.md:276-278` | 「`C1` 在没有 git 元数据时判 `UNVERIFIED` 而不是 `FAIL`」 | **一致**（`12aecf1` 落地；在 `e7f6de1` 提交的当时实现还没落盘——`..decisions/ledger.tsv:24` 自己记了这个时间差） |
| 14 | `AGENTS.md:70` | 「某一次跳过是否真的合规」检查器判不了 | **一致**（且这条比以往更贴切：现在确实存在合规的 SKIP） |

全库穷举：`git grep -n 'SKIP'` 除去 `scripts/`、`.pi/`、`upstreams/`、`docs/history/`、`docs/archive/` 后，只有上表出现过的文件；「不可达」「即故障」「当故障查」三种说法只出现在 `docs/coldstart.md:65` 与 `skills/coldstart.md:65/:79`。`.decisions/ledger.tsv:21/:24/:25/:32` 是历史决策行（记的是当时的状态与待办），不是面向读者的规范主张，不计入不一致。

### R3.3 相邻发现（非 SKIP，但同属「coldstart/README 与代码不一致」）

- README 检查表在 `e7f6de1` 之后仍未修的三处旧口径：`README.md:144`（C7 说成「与 `upstreams/` 文件系统一一对应」——实际对锁文件）、`README.md:146`（C9 说成「每条 sources 指向真实存在的上游文件」——无 `upstreams/` 时只核锁文件索引成员资格）、`README.md:285`（「由 `check-closure.py` 直接对 `upstreams/` 的文件系统核对」——实际是「处置表→锁文件→有克隆时上游文件」的链）。
- `check-consistency.py` 的 SKIP 只是 schema 对齐，脚本自身没有依赖环境的 SKIP 分支（其 docstring 写明「本脚本当前没有依赖环境的 SKIP 分支」）。上表涉及的 SKIP 主张全部只与 `check-closure.py` 有关。
- 相邻风险（未验）：coldstart 拷文件清单里从未出现 `VERSION`（`grep VERSION` 在 `docs/coldstart.md`、`skills/coldstart.md`、README 中 0 命中），而 `check-closure.py:249` 在 C1 一开头就无条件读它。实测删掉 `VERSION` 后：两个版本的脚本都在打印任何 `[PASS]/[FAIL]` 之前抛 `FileNotFoundError` 退出。若下游没拷 `VERSION`，「跑一次自检」会得到一个崩溃而不是报告。
- 相邻未验（UNVERIFIED）：C1 的 tag 语义默认脚本跑在本库的 git 仓库里；下游是自带 tag 的另一个仓库时 C1 会比出什么，本轮未构造下游全量安装场景，留待补证。

## R4. Round 2 的未决与未验

| 项 | 状态 | 补证条件 |
|---|---|---|
| 新增 P1 判据的「逐条处置」是否真被执行 | 只验到判据存在、引用可解析（C4） | 语义，人审；检查器判不了 |
| 「上一轮 `A8`」在磁盘上如何定位 | 判据/角色只说「上一轮」，未规定路径 | 下游/多任务场景实测 |
| `A3.freshness` 的读取端 | 仍为空（R1.4） | 人审是否需要在 P1 判据里读它 |
| `docs/coldstart.md:91`「不写数字」与 `skills/tier-sizing.md` 2/5/12 的关系 | 沿用 Round 1 的 `UNVERIFIED` | 由人裁定 |
| 下游带 tag 时 C1 的行为 | 本轮未测 | 全量下游安装 + `git tag` 复现 |
| 20:40:56 起工作树上的 C15 未提交改动 | 未采用为证据 | 提交后按 Round 1 §F 流程重跑 |

## R5. Round 2 复现命令

```bash
# 基线（12aecf1，无 .git）
rm -rf /tmp/inv0929-h && mkdir -p /tmp/inv0929-h
cd <repo> && git archive 12aecf1 | tar -x -C /tmp/inv0929-h
cd /tmp/inv0929-h && python3 scripts/render.py --check && python3 scripts/check-closure.py

# 场景 A：C1 SKIP / C7 PASS / C9 PASS（自曝）——见上文命令输出
# 场景 B：删锁文件 → C1 SKIP、C7/C9/C20/C21 FAIL
rm -f /tmp/inv0929-h/upstreams.lock.yaml && cd /tmp/inv0929-h && python3 scripts/check-closure.py | grep -E '^\[FAIL\]'

# 场景 C：无 .git 的 upstreams/ → C9 SKIP（pin 未核）
rm -rf /tmp/inv0929-hc && mkdir -p /tmp/inv0929-hc
cd <repo> && git archive 12aecf1 | tar -x -C /tmp/inv0929-hc
cp -R upstreams/. /tmp/inv0929-hc/upstreams/ && find /tmp/inv0929-hc/upstreams -maxdepth 3 -name .git -exec rm -rf {} +
cd /tmp/inv0929-hc && python3 scripts/check-closure.py | grep -E 'C1 |C9 '

# 场景 D：有 .git 有克隆 → C1 FAIL（未打 tag）、C9 PASS（sha256+pin）
rm -rf /tmp/inv0929-hd && git clone -q <repo> /tmp/inv0929-hd
ln -sfn <repo>/upstreams /tmp/inv0929-hd/upstreams
cd /tmp/inv0929-hd && python3 scripts/check-closure.py | grep -E 'C1 |C9 '

# E1 回边受控实验（b 例：只把 P1 加进 A8.consumers → C11 FAIL；两处都加 → C11 PASS、C3 FAIL）
# E2 C15 扩到 40 字段：把 gated 换成 {(a['id'], f) for a in artifacts for f in a['fields']} → 40/40 PASS

# A9 工具层（无 .git 无关）
cd ~ && mkdir -p ledgertest-inv && cd ledgertest-inv
bash <repo>/scripts/ledger.sh ./L.tsv P1 x "d" "w" "e"   # run 自动生成
bash <repo>/scripts/ledger.sh ./L.tsv P1 x "d" ""  "e"   # exit 2，为什么不能为空
```

---

*取证范围（Round 2）：被测对象钉死 `12aecf1`；行为证据取自该 commit 的 `/tmp` 独立检出。仓库工作树上 20:40:56 起的未提交改动未触碰、未采用；报告只写 `.pi/investigation/REPORT-0929-investigator.md` 这一个文件并按指示提交。*
