# P0 取证报告 · 0928 investigator

- 仓库：`/Users/yuantian/Developer/tim-professional-workflow`
- 基线：工作树 `1ba2be1`（v2.0.5 + 一次未打 tag 的提交），`git status` 干净
- tag `v2.0.5` = `2a3522a`
- 本文只摆证据与计数，不下裁定结论。行号除注明外均为上述工作树行号。
- 未改动 `scripts/`、`workflow/`、`roles/`、`skills/` 任何文件。唯一写入是本文件（`.pi/` 已被 `.gitignore` 忽略）。

---

## A · definition-of-done 的概念拆分

### A-1 上游正文怎么切这两件事

文件：`upstreams/addyosmani-agent-skills/references/definition-of-done.md`（3798 字节，54 行）

| 位置 | 原文要点 |
|---|---|
| `:3` | "A standing, project-wide bar … Unlike acceptance criteria, which vary per task and answer *'did we build the right thing?'*, the Definition of Done is the same every time and answers *'is this finished to our standard?'*" |
| `:5` | 独立小节 `## Definition of Done vs. Acceptance Criteria` |
| `:7–13` | 对照表五行：Scope（one task vs **every increment**）／Changes（different each item vs **fixed and reused**）／Answers（"did we build *this thing*" vs "is it *ready*"）／Owner（**defined when planning the task** vs **defined once for the project**）／Example |
| `:15` | "A task is done only when **its** acceptance criteria are met **and** the standing Definition of Done is satisfied." —— 两者是互补的两条腿，不是同一条 |
| `:19`（Correctness 首条） | "- [ ] All acceptance criteria for the task are met" —— 每任务 AC 被**收进** standing DoD 当第一条 |
| `:59` | "Tailor the list to the project once, then reuse it unchanged. A Definition of Done that is renegotiated every sprint is not a Definition of Done." |
| `:66`（Red Flags） | "Acceptance criteria treated as the whole bar, with no standing quality floor." |

上游的三处硬区分：**粒度**（one task / every increment）、**变动性**（different each item / fixed and reused）、**归属**（planning the task / defined once for the project）。并明确：把 AC 当全部门槛是 Red Flag。

### A-2 这份 references 正文现在没有任何机器覆盖

| 证据 | 位置 |
|---|---|
| `references` 在 `check-closure.py` 的 `SKIP_DIRS` 里 | `scripts/check-closure.py:65–66` |
| 该 `SKIP_DIRS` 被 `find_upstream_skills()` 用来跳目录 | `scripts/check-closure.py:112` |
| `references` 也在 `scripts/_render-lock.py:27` 的 `SKIP_DIRS` 里 → 锁文件根本不索引 `references/` | `scripts/_render-lock.py:27` |
| 锁文件里 `references/` 出现次数 = 0（实测 `grep -c`） | `upstreams.lock.yaml` |
| `upstream_dispositions` 里没有任何 `references/*` 条目（实测 grep 只命中 `addy:constraint-driven-development`） | `workflow/registry.yaml:1105` |

`references/` 目录实测有 7 个文件：`accessibility-checklist.md`、`definition-of-done.md`、`observability-checklist.md`、`orchestration-patterns.md`、`performance-checklist.md`、`security-checklist.md`、`testing-patterns.md`。

上游 disposition 只登记 SKILL.md（实测 `check-closure.py` 输出「锁文件 101 个上游 skill」）。**这 7 份 references 正文没有任何一条 `sources:` 指向它们。**

### A-3 本库 `skills/constraint-driven-development.md` 产出的根目录质量契约文件，在注册表里叫什么

- 技能产出声明：`skills/constraint-driven-development.md:5`「- 阶段：P1　归属角色：`architect`　产物：A4」
- 产出段 `:76`「A4 冻结契约，**这个契约里的质量部分**」——即不产出独立产物类型，是 A4 的一个分面
- 落点写死：`:38`「**一个文件放仓库根目录**」
- 注册表对应：`workflow/registry.yaml:107`（A4.embodiment）「**门槛形态**：仓库根目录一份的质量契约，含底线、带数字的强制项、只量不强制项、例外四段（`@constraint-driven-development`）」
- 派生出的人读视图：`docs/artifacts.md:116`（与 registry 逐字一致，`render.py --check` 通过）
- 消费者：A4 的 `consumers` 是 P2/P3/P4/P5/P6（`workflow/registry.yaml:93–99`）
- disposition：`workflow/registry.yaml:1105` `- {upstream: addy:constraint-driven-development, outcome: absorbed, into: constraint-driven-development, reason: 质量契约}`

**答：在注册表里它叫 A4 的「门槛形态」，不是独立产物。**（对照 `artifact-arrows.md` R11 把它编号为 C11「质量契约文件」，处置 `并入 A4`——该表自己就归到 A4 门槛形态。）

### A-4 `A4.embodiment` 与 `A4.notes.done_definition` 是不是同一件事

原文（`workflow/registry.yaml:106–113`）：

```
    embodiment: >-
      **主形态**：task packet 里的契约段。**规格形态**：落进仓库的规格文件或问题跟踪系统（`@spec-driven-development`）。**门槛形态**：仓库根目录一份的质量契约，含底线、带数字的强制项、只量不强制项、例外四段（`@constraint-driven-development`）。**长期形态**：难回头且有取舍的决定写成决策记录，逐编号、只追加不删（`@documentation-and-adrs`）。
    persistence: durable
    notes:
      what: 建什么。动词开头，能被第三方复述
      why: 为什么——业务理由，不是技术偏好
      done_definition: 什么证据算完成。必须可判定：只凭它能给出 PASS/FAIL/UNVERIFIED
      boundaries: 什么不做、什么不许改——包括不许为了变绿而削弱检查
```

- `embodiment`（`:107`）写的是**形态**（文件/段落长什么样、落在哪）——四种形态：契约段、规格、门槛（根目录质量契约）、决策记录。
- `notes.done_definition`（`:112`）写的是**判据性质**（必须可判定、三态）——是 A4 这个**产物**自身的判据字段。

两段的**主语不同**：`embodiment` 的主语是「A4 的落盘形态」，`notes.done_definition` 的主语是「A4 里的一个字段」。二者是产物与其字段的关系，文本上没有互相定义。

### A-5 上下游口径落差的三个可核对点

| # | 上游 | 本库 | 证据 |
|---|---|---|---|
| 1 | standing DoD 是**独立的、每项目定一次**的固定门槛（`:12` Owner "defined once for the project"） | 本库把门槛塞进 A4 作为**一个 `embodiment` 形态**，A4 本身是**每次任务**由 P1·architect 产出的产物（`registry.yaml:91` `producer: architect`、`consumers: P2–P6`；`skills/constraint-driven-development.md:5` 阶段 P1） | 上游 `definition-of-done.md:12` vs `registry.yaml:91–99,107` |
| 2 | 每任务 AC 与 standing DoD 是**并列互补**（`:15`），且「把 AC 当全部门槛」是 Red Flag（`:66`） | `registry.yaml:133`（A5.notes.acceptance）「每片的验收口径，**必须能追溯到 A4.done_definition**」——方向是**每任务判据由 A4 派生**，与上游的「两条腿」是反向 | 上游 `:15,:66` vs `registry.yaml:133`；另 `registry.yaml:277`（P2 判据）「verify: A5.acceptance 每片都能追溯到 A4.done_definition」 |
| 3 | standing DoD **内含**一条「All acceptance criteria for the task are met」（`:19`） | 本库 A4 的 fields 是 `what / why / done_definition / boundaries`（`registry.yaml:102–106`），**没有**「本任务 AC 已满足」这一条 | 上游 `:19` vs `registry.yaml:102–106` |

另记一条同名的**第三种**用法：`skills/constraint-driven-development.md:84`（产出段）把 `done_definition` 定义为「**门槛本身**也要可判定。合格形态是『跑一遍现在这套检查，在当前代码上不新增失败』」。这是 DoD-of-the-DoD（门槛自身的判据），与 `registry.yaml:112` 的 A4.done_definition（本次契约的判据）是同一字段名、同一产物、不同时所指的对象——两处定义在正文层面对齐情况：

- `registry.yaml:112`：「什么证据算完成。必须可判定：只凭它能给出 PASS/FAIL/UNVERIFIED」
- `skills/constraint-driven-development.md:84`：「合格形态是『跑一遍现在这套检查，在当前代码上不新增失败』」

（未裁定：这两句是同一判据的抽象层与具体层，还是两件事。）

### A-6 机器能不能核到这一层

`check-closure.py` C4「判据可判定」只核「退出判据引用的字段在 registry 里真实存在」（`check-closure.py:9` 描述，输出行「23 条退出判据全部指向真实字段」）。**没有任何一条检查核 `embodiment` 段的内容**，也没有检查核 A4 的 `done_definition` 是否真的承担了 standing DoD 的角色。`embodiment` 段本身是 v2.0.5 新增的自由文本，机器只读 `id/key/zh/producer/consumers/fields/shape/persistence/notes` 这些结构字段。

---

## B · 角色与脚本的来源

### B-1 全库来源声明清点（实测命令，非估计）

| 目录 | 文件数 | 带来源声明 | 粒度 | 机器可核？ |
|---|---|---|---|---|
| `skills/` | 51 | **51**（`## 来源` 段，文件级） | **文件级** | ✅ C9 / C10 / C12 |
| `principles/` | 7 | **23 条原则**各有 `来源：` 行 | **段落级**（每条原则一节一来源） | ✅ C9 / C10 |
| `roles/` | 9 | **0** | — | ❌ |
| `scripts/` | 6 | **0** | — | ❌ |
| `docs/` | 5 | **0** | — | ❌ |
| `workflow/` | 1 | **0** | — | ❌ |

命令：`for f in skills/*.md; do grep -q "^## 来源" "$f" || echo $f; done`（skills 返回空 → 51/51 齐）
命令：`for f in principles/*.md; do echo "$(grep -c '^来源：' $f)"; done` → 1/9/8/2/1/1/1 = **23**

### B-2 `roles/` 头部现状

`roles/architect.md:1–40`、`roles/builder.md:1–30`、`roles/cartographer.md:1–25`、`roles/voice.md:1–25` 已读。头部结构一律是：

```
# <角色名>（`<id>`）
> <一句话使命>
- 主产物：`Ax` …
- 默认出场：`Px` …
- 横切带：`…`（部分角色有）
---
## 我是谁
## 我的心智模型
- `@p-xxx` —— <原则摘要>
```

`roles/` 里「来源」二字只出现 3 次，全是无关机散文，与来源声明无关：

- `roles/architect.md:21`「它是『该在哪验』和『改这里会破坏谁』的**唯一可靠来源**」
- `roles/architect.md:42`「这是 `A3` 的**唯一事实来源**」
- `roles/cartographer.md:51`「不能新增一条『顺手也检查一下 X』这种**没来源**的要求」

角色与来源的唯一机器联系是**间接**的：`roles/*.md` 的心智模型段 `@p-xxx` 指向 `principles/`，而 `principles/` 有来源；由 C5（角色装配件一致）+ S1（无游离文件）保证指向存在。**角色正文自身写下的每一句判断，零来源声明。**

### B-3 `scripts/` docstring 声称的来源

| 脚本 | docstring 声称的是什么 | 有无来源/依据声明 |
|---|---|---|
| `scripts/_render-lock.py:2–7` | 「`_render-lock.py` · 生成 upstreams.lock.yaml／只读 upstreams/，只写 upstreams.lock.yaml」 | ❌ 无。用途声明 |
| `scripts/check-closure.py:2–22` | 「闭包检查器（只读，可重复运行）／它回答一个问题：**这套工作流是通的吗？**」+ C1–C7 七条断言清单 | ❌ 无。「七条」已过期（实际 C1–C16+D1 共 17 项，见 D-4 实测输出） |
| `scripts/check-consistency.py:2–17` | 「一致性互斥检查／上一版把同一段工程方法复制进 9 个角色正文…」+ S1–S7 | ❌ 无。「上一版」的教训是唯一的历史溯源，但无出处 |
| `scripts/render.py:2–12` | 「从唯一真源生成派生视图」+ 「生成区不得手工编辑」 | ❌ 无 |
| `scripts/ledger.sh:2–4` | 「决策台账（A9）追加工具／纪律：只追加」 | ❌ 无。`registry.yaml:210`（A9 硬边界「台账只追加」）是**下游**引用，不是来源声明 |
| `scripts/sync-upstreams.sh:2–16` | 「更新只读上游克隆并重新生成锁文件／**这是本库唯一允许改动 upstreams/ 的脚本**」 | ❌ 无。这是**权限**声明，不是来源声明 |

**六个脚本的 docstring 没有一个声明「这段逻辑是从哪来的 / 依据什么」。** 唯一接近的是 `check-consistency.py:9–10` 提到「上一版把同一段工程方法复制进 9 个角色正文」——记了失败史，但没给出「这段检查该怎么来的」的出处。

### B-4 C9/C10/C12 实际覆盖到哪一级

| 检查 | 代码位置 | 覆盖对象 | 粒度 |
|---|---|---|---|
| C9 来源真实存在 | `check-closure.py:392–422` | `skills[].sources` 与 `principles[].sources` 对 `upstreams.lock.yaml` 的 key 集合（101 项） | 技能=文件级；原则=段落级 |
| C10 处置与来源双向咬合 | `check-closure.py:425–447` | `upstream_dispositions[].into` ↔ 目标 `sources` | 同上 |
| C12 原创技能显式标注 | `check-closure.py:449–456` | `sources` 为空必须 `origin: library` | 文件级 |
| （锁内实物对照） | `check-closure.py:402–421` | 有 `upstreams/` 时逐条比 sha256 + 三仓 pin | 只覆盖锁里索引的 101 个 `SKILL.md` |

registry 实测数据（`python3 -c "yaml.safe_load(...)"`）：

- `skills` 51 条，**51 条都有 `sources` 或 `origin`**
- `origin: library` 的 3 条：`tier-sizing`、`document-mapping`、`coldstart`
- `principles` 23 条，**23 条全有 `sources`**
- `roles` 9 条，字段是 `id/zh/mission/owns_artifacts/ribbons/skills/principles/forbidden`——**没有 `sources` 字段位**

### B-5 答：Owner 说的「每一段话有来源」，机器现在能核到哪一级

- **能核**：技能**文件**（51 个，100%）与原则**段落**（23 条，100%）的来源路径真实存在于锁文件、且与 disposition 表双向咬合。上游内容漂移也能核（有 `upstreams/` 时比 sha256）。
- **核不到**：
  1. **`roles/` 9 个文件**：registry 的 roles 段没有 `sources` 字段位，9 个文件正文没有来源段，9 个文件在检查器的覆盖范围之外。角色正文的每一句判断（`## 我是谁`、`## 我不做的事`、`## 硬边界`）零来源。
  2. **`scripts/` 6 个文件**：docstring 只声明用途与权限，无来源；检查器只把 `scripts/` 当**被扫描对象**（S1「scripts/ 无残留」），不检查其来源。
  3. **`docs/` 5 个文件**：`docs/artifacts.md`、`docs/closure-report.md` 是 render 生成物（无来源可言）；`docs/coldstart.md`、`docs/downstream-mapping.md`、`docs/ledger.md` 是手写正文，无来源段。
  4. **`upstreams/*/references/` 7 份正文**（含本报告 A-1 那份 DoD）：被 `SKIP_DIRS` 跳过，不进锁、不进处置表、无人核。
- **差的这一段具体差在哪**：来源声明目前是**「有 `sources` 字段的集合」的属性**，不是「全库每个文件的属性」。差距是**载体缺位**（roles/scripts/docs/references 四处没有可填来源的字段位），不是「有几份漏填」。

---

## C · 口径裁定取证

### C-1 96 条箭头的两堆归类（从 `artifact-arrows.md` 的表里直接数出）

`artifact-arrows.md` 共有 R01–R98 共 **98** 行；`:R97`/`:R98`（registry 本身与处置表本身）按该文件 `:§3` 的口径扣除 → **96 条运行期箭头**。

处置列计数（脚本从表里 regex 提取，98 行全中）：

| 堆 | 处置标记 | 条数（98 行口径） | 扣掉 R97/R98 后 |
|---|---|---|---|
| **第一堆：右端落到 A1–A9 之一** | 并入 A6 | 17 | 17 |
| | 并入 A9 | 13 | 13 |
| | 下游既有物 → 见右列 | — | — |
| | 并入 A4 | 8 | 8 |
| | 并入 A8 | 8 | 8 |
| | 并入 A3 | 7 | 7 |
| | 并入 A7 | 6 | 6 |
| | 并入 A2 | 5 | 5 |
| | 并入 A5 | 3 | 3 |
| | 并入 A1 | 1 | 1 |
| | **小计** | **68** | **68** |
| **第二堆：落不到 A1–A9 任何一类** | 下游既有物 | 14 | 14 |
| | 不产出 | 9 | 7（扣 R97/R98） |
| | 保留登记表外 | 7 | 7 |
| | **小计** | **30** | **28** |
| | **合计** | **98** | **96** ✓ |

**第一堆 68 条**，按 A 分类：A1=1、A2=5、A3=7、A4=8、A5=3、A6=17、A7=6、A8=8、A9=13。
代表例子：R01 问卷文件→A1、R06 调研文件→A2、R14 能力索引+每能力页→A3、R11 质量契约文件→A4、R24 决策票据→A5、R30 提交→A6、R45 两轴审查报告→A7、R55 前后截图→A8、R65 发布记录→A9。

**第二堆 28 条**，三类：
- `下游既有物` 14 条 —— R22 接口文档/快速开始、R28 外发评论、R38 弃用通告、R41 N 份候选工作副本、R62 告警规则、R63 runbook、R68 版本标签、R69 变更日志、R70 改动说明三段、R72 CI 流水线配置+合并保护（另 R22 计两次）
- `不产出` 7 条 —— R29 检查点结论、R36 调试插桩、R37 诊断脚手架、R79 轻量计划、R81 练习与反馈、R88 冷启动自检结论、R96 只读检查器输出
- `保留登记表外` 7 条 —— R34 一次性原型分支、R40 rubric、R49 扇出工单、R51 验证套件+helper、R57 性能尝试记录、R84/R90 A↔B 映射表、R94 12 个派生文件

**两处一行两处置**（脚本未单独捕获，需人工读）：
- R80（`teach.md:58` 教学参考件）= `并入 A3`（术语表）／`保留登记表外`（速查、图解）
- R84（`document-mapping.md:40` 映射表）= `保留登记表外`（映射表）／`并入 A9`（映射行）

### C-2 54 种 C 表：多少已被 embodiment 段接住

`artifact-arrows.md §3` 的 C 表 54 条（脚本 regex 提取，与该文件自报数字一致）：
`并入 A1`=1、`A2`=2、`A3`=2、`A4`=6、`A5`=2、`A6`=8、`A7`=1、`A8`=6、`A9`=2 = **30 条**；`保留登记表外`=8、`不产出`=6、`下游既有物`=10 = **24 条**。合计 54。

当前 registry 的 A1–A9 **每条都有 `embodiment` 段**（实测 9/9；`registry.yaml:38, 60, 82, 107, 127, ~A6, ~A7, ~A8, ~A9`）。把每条 C 按其归属产物的 `embodiment` 原文做关键词核对：

| 结果 | 条数 | 明细 |
|---|---|---|
| **被 embodiment 点名** | **22** | C01 问卷(A1)、C02 调研文件(A2)、C03 工作面快照/移交简报(A2)、C04 词汇表/术语形态(A3)、C05 索引(A3)、C06 决策记录·逐编号·只追加(A4)、C07 规格形态/规格文件(A4)、C11 质量契约/门槛形态(A4)、C12 票据(A5)、C13 triage(A5)、C14 闸门(A6)、C15 脚本·生成器(A6)、C16 commit(A6)、C19 测试·反馈回路(A6)、C20 杠杆(A6)、C21 代码本身(A6)、C22 对抗·质疑·interrogate·doubt-driven(A7)、C23 未覆盖能力清单(A8)、C30 台账·装配记录·映射结果·三栏(A9) |
| **未被点名** | **32** | C08 待建模块地图、C09 设计草图、C10 备选形状与落选理由、C17 功能开关、C18 回退脚本、C24 浏览器计划+截图、C25 性能基线、C26 依赖审计、C27 值班问题清单+信号对照、C28 流水线自证、C29 发布记录/回滚路径/可观测项（以上 11 条 tpw-map 判「并入 A*」）+ C31–C34、C37–C44、C45–C46、C48–C54（21 条 tpw-map 判登记表外/不产出/下游既有物） |

**注意两个不同层级的「接住」**——上表只测「embodiment 正文里出现该产物名」。若改测「embodiment 里 `@技能id`」：

| C | 目标 | 技能是否被 @ 引用 |
|---|---|---|
| C08 待建模块地图 | A4 | ✅ `@spec-driven-development` |
| C13 triage 整备记录 | A5 | ✅ `@triage` |
| C09 设计草图 / C10 备选形状 | A4 | ❌ `@codebase-design` 未出现在 A4.embodiment |
| C17 功能开关 | A6 | ❌ `@incremental-implementation` 未出现 |
| C18 回退脚本 | A6 | ❌ `@deprecation-and-migration` 未出现 |
| C24–C28 五个 A8 产物 | A8 | ❌ 五个技能全部未出现在 A8.embodiment |
| C29 发布记录/回滚路径 | A9 | ❌ `@shipping-and-launch` 未出现 |

A6/A8/A9 的 `embodiment` 段里**一个 `@技能id` 都没有**（A1–A5 有）。这是可直接核对的事实。

### C-3 口径差异 vs 真实漏项：三条处置在 v2.0.5 已被 embodiment **翻面**

| C | tpw-map 处置 | 当前 embodiment 实际写法 | 证据 |
|---|---|---|---|
| **C35 一次性原型分支** | `保留登记表外`（理由：原型代码被禁止当产品代码用） | A6.embodiment 明写「…**一次性原型**…全部是 A6 的组成部分——它们改的就是代码和配置。不要为它们另开编号，但每一样都要在 A6.change 里点名列出来」 | `registry.yaml` A6.embodiment |
| **C36 A↔B 映射表** | `保留登记表外`（v2.0.1 技能说进版本库） | A9.embodiment 明写「**装配记录**（集合 A↔B 映射结果、冷启动三栏报告）是 A9 在装配时写的几行，**不是独立文档**」 | A9.embodiment |
| **C47 CI 流水线配置+合并保护** | `下游既有物` | A6.embodiment 明写「…**流水线配置**…全部是 A6 的组成部分」 | A6.embodiment |

**答 Owner 问的那个问题：三条是「口径差异」（v2.0.1 之后 embodiment 主动收编了它们），不是 tpw-map 漏了。** 但另有一批不是口径差异：上表 11 条「并入 A* 却没被 embodiment 点名」的里，C09/C10/C17/C18/C24–C28 这 9 条，其**技能**在 registry 里确实声明 `outputs: [A6]` / `[A8]`（C14「技能头部产物声明与注册表一致」实测 PASS），只是 `embodiment` 段没写出这些形态名——**tpw-map 与 embodiment 之间是描述粒度差，不是归属判定冲突**。真正两处仍与 embodiment 判定相反的只有 C35、C36、C47 三条，且都是 v2.0.5 已改口的（tpw-map 在 §3 表尾与 §4-⑦ 已自行标注其中两条被后续提交改判）。

### C-4 `simulation.md` 的 P0→P6 走查：判为断链的条目，现在还在不在

`simulation.md:§3` 列 10 条。逐条对当前工作树核对：

| # | 断链（`simulation.md:§3` 原文摘要） | 现状 | 证据 |
|---|---|---|---|
| 1 | `A6.subject` 无产出方；P3 不校验、P5 依赖 | **已修** | `skills/implement.md:41`「**每个产出 `A6` 的技能都要在交付时填上它**」；`roles/builder.md:50` 有该字段行。新增检查 **C15**「被判据校验的字段产出方真的会说填：17 个被阶段判据校验的字段，产出方正文里都点名列出了」实测 PASS |
| 2 | `A8.subject`/`frame_alignment` 无产出方 | **已修** | `roles/verifier.md:52`「A8…**七栏**全部非空」，`:57` subject、`:60` frame_alignment；5 个 P5 技能全部补齐（`verification-suite.md:52,54`、`browser-testing.md:44,46`、`performance-optimization.md:46,48`、`security-and-hardening.md:43,45`、`observability-and-instrumentation.md:46,48`） |
| 3 | P5 判据② 对「没有可比的对手」无定义 | **仍在** | `registry.yaml:314`／`workflow/phases/P5.md:23` 仍只有「A8.subject 与 A6.subject 逐字一致——不一致…判 UNVERIFIED」一条；**没有**覆盖「A6.subject 为空」的分支。空栏一侧现在由 `skills/implement.md:41` 的强制填写约束，但**判据层无对应条目** |
| 4 | P6 判据③ 的更新者（architect）不在 P6 装配；且 `roles/verifier.md:92` 与 `registry.yaml:82` 矛盾 | **已修** | `roles/verifier.md:97–99` 已改为「**不更新 `A3`**…写进 `A8.frame_alignment` 交回去」；`registry.yaml:88` freshness note 写死分工；P6 判据改为 `registry.yaml:330`／`workflow/phases/P6.md:27`「A8.frame_alignment 非空…地图的更新是**下一次 P1** 的活，不在 P6 的判据里（**P6 没装 architect，要求它更新是越权**）」 |
| 5 | 判档依赖 A1 而 A1 装配依赖判档（循环）；`driver` 不在任何阶段 | **已解** | `registry.yaml:978` `tier-sizing.inputs: []` + `:982–984` note「inputs 为空是刻意的——判档发生在 A1 之前…A1 出来之后若与判档前提冲突，按 P0 的退出判据退回重判档」；`registry.yaml:252` `driver_seat_note`「driver 在 P0 之前判档。它不产出本阶段任何产物，所以不进 default_roles」；新增检查 **C18**「开工前的技能不依赖开工后才有的产物：2 个开工前技能不依赖任何阶段产物」PASS |
| 6 | 能力清单建立权四处打架 | **已修** | `roles/verifier.md:28`「**只做两件事**…写进 `A8.frame_alignment` 交回 architect」、`:30`「不要顺手自己补一页」；`registry.yaml:88` 写死「verifier 不得自己重建能力清单」 |
| 7 | `A8 = FAIL` 的回边没有定义 | **仍在** | `registry.yaml` A8 `consumers: [P6]`（实测只有 P6 一个）；`:177` `rework:` 只挂在 A7 上（「附条件通过时回到 P3 重做…刻意不建成消费关系」）；P6 判据 `:328`「A8.verdict 是 PASS——UNVERIFIED 与 FAIL 都不许上线」。**A8=FAIL 之后回哪一步，全库仍无条文** |
| 8 | P0–P5 没有任何判据要求台账被写 | **已修** | 7 个阶段全部有 `verify: A9.actor 有本阶段这一轮的决定行…`（`registry.yaml:251,266,278,290,301,316`，P6 为 `:329` 的 A9.result）；新增检查 **C16**「每阶段都要求记台账：7 个阶段都有 A9 判据」PASS |
| 9 | P0/P1 退出判据不检查产物落点；`docs/artifacts.md` 用 `persistent` 而 registry 取值是 `durable` | **部分修** | 词表已统一：`docs/artifacts.md:131` 现为「**`durable`** 的产物必须有可追溯的落点，并进版本库」；`docs/` 内 `persistent` 仅剩 `docs/downstream-mapping.md:90` 一处。「退出判据不检查落点」本身**仍无对应判据**（registry 落盘纪律仍在 notes/docs 层，不在 verify 层） |
| 10 | P6 判据②「回滚路径已被确认可执行」没有定义确认人 | **仍在** | `registry.yaml:329` 判据原文未变；`skills/shipping-and-launch.md:24` 有「谁执行」但那是**执行人**不是**确认人**；`:36`「未写下并被确认可执行就不算发布完成」仍未指明谁确认 |

**汇总：10 条里 6 条已修（#1 #2 #4 #5 #6 #8），3 条仍在（#3 #7 #10），1 条部分修（#9）。** 6 条已修项中有 3 条（#1 的 C15、#5 的 C18、#8 的 C16）是**新增的机器检查**——`simulation.md:§3` 当时给这 6 条的「是否被检查覆盖」栏填的是「否」。

---

## D · 冷启动与安装协议现状

### D-1 干净 clone 实测（`git clone --branch v2.0.5` 到 `/tmp`，`upstreams/` 未随包分发）

```
$ rm -rf /tmp/tpw-clonetest && mkdir -p /tmp/tpw-clonetest
$ git clone --quiet --branch v2.0.5 /Users/yuantian/Developer/tim-professional-workflow tpw
$ cd /tmp/tpw-clonetest/tpw && git log --oneline -1
2a3522a fix(v2.0.5): 二审阻断项 B1/B2/B3 + C13 改为显式声明

$ ls -d upstreams
ls: upstreams: No such file or directory      ← 确认未随包分发
$ ls
AGENTS.md  docs  principles  README.md  roles  scripts  skills
upstreams.lock.yaml  VERSION  workflow
```

**`python3 scripts/check-closure.py`（退出码 0）**

```
TIM · check-closure.py（只读闭包检查）
真源: workflow/registry.yaml
------------------------------------------------------------------------------
[PASS] C1 结构与版本单一来源              版本 2.0.5，产物 9／阶段 7／角色 9／原则 23／技能 50
[PASS] C2 产物有主且有人接               9 类产物全部有唯一产出方且被消费
[PASS] C3 阶段可达且依赖闭合              7 个阶段按序可达，每个阶段所需产物在上游已产出
[PASS] C4 判据可判定                  23 条退出判据全部指向真实字段
[PASS] C5 角色装配件一致                9 个角色的产物／技能／原则指认双向一致
[PASS] C6 无孤儿且阶段装得出来             50 个技能／23 条原则全部被引用，每个阶段的默认角色能产出它声称的产物
[PASS] C7 上游处置完备（对锁文件）           锁文件 101 个上游 skill，处置表 101 条，一一对应
[PASS] C9 来源真实存在（锁 + 实物对照）       101 个上游 skill 索引（锁文件），0 条失效来源
[PASS] C10 处置与来源双向咬合              101 条处置与目标 sources 双向一致
[PASS] C11 消费声明与装配咬合              22 条消费声明全部被阶段接住
[PASS] C12 原创技能显式标注               3 个原创技能已标注
[PASS] C13 越权写由显式声明判定             23 条判据全部显式声明了 write/verify，没有越权
[PASS] C14 技能头部产物声明与注册表一致         50 个技能的头部声明与注册表 outputs 一致
[PASS] C15 被判据校验的字段产出方真的会说填       17 个被阶段判据校验的字段，产出方正文里都点名列出了
[PASS] C16 每阶段都要求记台账              7 个阶段都有 A9 判据
[PASS] C18 开工前的技能不依赖开工后才有的产物      2 个开工前技能不依赖任何阶段产物
[PASS] D1 底座解耦                   扫描 86 个库内容文件，0 处具体运行底座名称
------------------------------------------------------------------------------
合计: 17 项通过 / 0 项失败 / 0 项跳过 / 17 项检查
EXIT=0
```

**`python3 scripts/check-consistency.py`（退出码 0）**

```
TIM · check-consistency.py（只读一致性与互斥检查）
真源: workflow/registry.yaml
------------------------------------------------------------------------------
[PASS] S1 无游离文件                角色 9／技能 50／阶段 7／横切带 3 与注册表对齐，scripts/ 无残留
[PASS] S2 引用可解析                扫描 76 个库文件，0 处未知 id、0 处死链
[PASS] S3 文件内权限互斥（词形级）         扫描 76 个文件的「动作+宾语」否定/要求配对，0 处互斥。边界：只抓同一文件内同动词同宾语；同义改写与跨文件冲突抓不到，那部分靠独立审查与人审
[PASS] S4 硬规则不互斥               3 条阶段硬规则与 19 条角色硬边界不打架
[PASS] S5 技能三角一致               50 个技能的阶段／归属角色／装配三者相容
[PASS] S6 产物持久性一致              9 类产物的 persistence 与各阶段依赖、各角色归属相容
[PASS] S7 横切带适用范围一致            3 个横切带的适用范围覆盖其携带角色参与的阶段
------------------------------------------------------------------------------
合计: 7 项通过 / 0 项失败 / 0 项跳过 / 7 项检查
EXIT=0
```

**`python3 scripts/render.py --check`（附加实测，退出码 0）**

```
render --check: OK（12 个派生文件逐字一致）
EXIT=0
```

**工作树 `1ba2be1` 对照实测**（tag 之后又加了一次提交）：

```
$ python3 scripts/check-closure.py --quiet
合计: 16 项通过 / 1 项失败 / 0 项跳过 / 17 项检查
EXIT=1
    ↳ [FAIL] C1 结构与版本单一来源：当前 commit 上没有 tag——打了 tag 之前不能算一个 release
$ python3 scripts/check-consistency.py --quiet   → 7 项通过 / 0 失败，EXIT=0
$ python3 scripts/render.py --check              → OK，EXIT=0
```

该 FAIL 的 `misses` 原文只有一句 tag 缺失，与内容无关；`1ba2be1` 技能数为 51（tag `v2.0.5` 为 50，新增 `skills/user-interface-engineering.md`）。**未把这条记为产品缺陷**——按本库硬边界 3，环境/流程状态既不算 PASS 也不判成产品缺陷。

### D-2 两份冷启动文档的说法不一致之处（逐条）

`skills/coldstart.md`（技能，横切带，`driver`）vs `docs/coldstart.md`（人读安装手册）：

| # | 项 | `skills/coldstart.md` | `docs/coldstart.md` | 现状 |
|---|---|---|---|---|
| **1** | **`render.py` 要不要** | 第 9 步只列「注册表、角色文件、原则、阶段契约、技能文件」；第 10 步只说「**检查脚本**接到下游的检查入口…**台账脚本**随 A9 的落点一起放」；第 11 步只说「派生文件由脚本重新生成」——**全文 `render` 出现 0 次** | 第 2 步表里 `render.py` 一行，结论写成加粗「**要**。派生视图…全部由它从注册表生成，下游改了注册表就得重跑它」 | **仍在**（二审点的第 1 处，未修） |
| **2** | `upstreams.lock.yaml` 要不要 | 全文 `upstreams.lock` 出现 **0 次** | 第 2 步表里明确列出「随注册表一起拷。下游没有三仓克隆，靠这份锁文件核对处置表」（出现 2 次） | **仍在**。且锁文件是 C7/C9 在干净 clone 里能跑的唯一依据（实测 PASS），漏拷 = 下游 C7/C9 直接红 |
| **3** | `sync-upstreams.sh` / `_render-lock.py` | 全文出现 **0 次**，**没说拷也没说不拷** | 第 2 步明确「**不拷**。它们是本库维护上游用的，下游不需要更新上游」 | **仍在**（技能侧缺失） |
| **4** | **`SKIP` 判档** | 第 12 步：「**会显示 `SKIP` 的两项是正常的**：`C7`…与 `C9`…依赖 `upstreams/`，那是本库自己的只读克隆，**不随安装分发**」；「看到 `SKIP` 不要当成装完了」；产出段判定标准第一条「**除 `C7`/`C9` 之外的全部检查项 PASS，且那两项是 SKIP**…报 PASS 才是假的」 | 第 2 步：「下游跑检查会看到两项 `SKIP`…它们核对的 `upstreams/` 不随包分发，所以**用随包分发的 `upstreams.lock.yaml` 顶替**」 | **两份都还说下游会 SKIP；干净 clone 实测两项都是 `PASS`**（见 D-1 输出） |
| **5** | `ledger.sh` / `check-closure` 的具体落点 | 只说「台账脚本随 A9 的落点一起放」「检查脚本接到下游的检查入口」 | 第 2 步表逐行给出「下游的检查目录（如果有 CI，接到 CI 里）」「随 `A9` 的落点一起放」 | 技能侧缺表格，粒度差 |
| **6** | **档位判据** | 第 8 步：「跑一遍 `tier-sizing`，按**这次变更的风险与仓库成熟度**定这一轮装哪些角色」——**没有「闭环完整」** | 第 4 步：「**不写数字。**编号会诱导凑数。**判据只有一条：闭环完整**——装配完之后，每一环需要的东西都有人产出」 | **仍在**（二审点的第 2 处，未修）。两处对判据的表述不同 |
| **7** | 档位三档的具体处置 | 只有「定这一轮装哪些角色」一句 | 第 4 步给了 小/`solo`／中／大 四行具体装配说明 | 技能侧细节缺失 |
| **8** | `A1.non_goals` 的强制点 | 无 | 第 5 步独立成节：「起 `P0` 之前，**强制 `voice` 拿到 `A1.non_goals`**」 | 技能侧无对应条目 |
| **9** | 自检清单 | 第 12 步只说「跑一次闭合检查」 | 文末独立「## 自检清单」7 条勾选项 | 粒度差 |
| **10** | 底座四项能力 | 第 6 步「实测四项能力（起独立会话、读写真实文件、会话之间互发、并行跑多个）」 | 第 1 步整节 + 四行表格 | 实质一致，仅粒度差 |

**二审点的两处（「`render.py` 需不需要」= 上表 #1；「闭环完整判档」= 上表 #6）：两处都仍在。**

### D-3 #4（SKIP 判档）的可核对根因

| 证据 | 位置 |
|---|---|
| `check-closure.py` 的 `Result.add(..., skip=False)` 形参存在 | `scripts/check-closure.py:74` |
| 报告逻辑 `tag = "SKIP" if skip else (...)` 存在 | `scripts/check-closure.py:87` |
| **全文件没有任何一处调用时传 `skip=True`** | `grep -c "skip=True\|skip=1" scripts/check-closure.py` → **0** |
| 唯一出现的 `SKIP` 字符串是 `SKIP_DIRS` 与第 112 行的目录跳过 | `scripts/check-closure.py:65, 112` |
| C7 的描述已改为「（**对锁文件**）」，走 `lock_skills` 而非 `upstreams/` 目录 | `check-closure.py:388`，实现 `scripts/check-closure.py:356–372` |
| C9 同理：「锁 + 实物对照」，无 `upstreams/` 时只走锁分支 | `check-closure.py:392–422`，条件 `if lock_skills and (ROOT / "upstreams").is_dir():` |
| 缺锁文件时报错信息就是为干净 clone 写的 | `check-closure.py:372`「缺少 upstreams.lock.yaml——没有它，处置表在干净 clone 里无处核对」 |
| 锁文件头部的自述 | `upstreams.lock.yaml:2–13`，`why` 字段明写「干净 clone 出来的下游要能跑检查，靠的就是这份锁文件」 |

即：C7/C9 现在是**按锁文件判的**（`upstreams/` 缺席时降级为纯锁核对，而不是 SKIP）。两份冷启动文档描述的 SKIP 行为在当前实现下不可达。

### D-4 附：`check-closure.py` docstring 自身过期

`scripts/check-closure.py:11` 自述「『通』被拆成可机械判定的**七条**断言」，但实测输出为 **17 项**（C1–C6, C7, C9–C16, C18, D1；注意编号跳过了 C8、C17）。docstring 未随 C9–C18 / D1 的加入更新。`check-consistency.py:11` 的 S1–S7 七条与实际一致（实测 7 项 PASS）。

---

## 附 · 计数复算方法

| 结论 | 复算命令 |
|---|---|
| 96 条箭头 68/28 两堆 | `python3` regex `^\| (R\d+) \|(.*?)\|\s*`([^`]+)`[^|]*\|` 提取 `artifact-arrows.md`，对第 3 列计数 |
| 54 条 C 表 30/24 | 同法提取 `^\| (C\d+) \|`，对第 5 列计数 |
| 22 条被 embodiment 点名 | 逐条把关键词喂进对应 artifact 的 `embodiment` 字段（`yaml.safe_load` 取出） |
| skills 51/51、principles 23、roles 0 | `grep -q "^## 来源"` / `grep -c '^来源：'` / `grep "来源"` |
| 干净 clone 两脚本退出码 | `/tmp/tpw-clonetest/tpw` 下直接运行，已贴原始输出 |
