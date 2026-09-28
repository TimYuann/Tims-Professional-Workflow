# EVIDENCE · 核心闭环 8 条的证据

- 对象：本仓工作树（未改动），HEAD `52d3315` + 未提交重写
- 本轮角色：闭环设计者（只读产物，只写 `.pi/core/**`）
- 交付：本文件 + `.pi/core/PLAN.md`
- 方法约束（遵守）：**一条一条读**；`grep -n` 只用于定位行号，结论一律来自逐行读到的原文。**没有**用脚本或正则批量核对语义。

## 阅读深度（如实标注）

`[全文]` 逐行读过 ｜ `[局部]` 只读用到的行 ｜ `[仅目录]` 只看了标题结构

**本库**：`roles/*.md` 10 份 `[全文]`；`pipeline.md` `[全文]`；`closure.md` `[全文]`；`identity.md` `[全文]`；`README.md` `[全文]`；`AGENTS.md` `[全文]`；`scripts/*` 8 份 `[全文]`（含 `check-library.py` 879 行）；`SOURCES.md` `[局部]`（第 1–14、17、18、76–130、195–255、340–470 行）；`.pi/round3/REPORT.md` `[全文]`；`.pi/round4/TASK.md` `[全文]`。

**三仓**（`[全文]` 或 `[局部]` 逐条列在 §1–§8）：

- `upstreams/mattpocock-skills`：`skills/engineering/domain-modeling/SKILL.md` `[全文]`、`skills/productivity/writing-for-agents/SKILL.md` `[全文]`、`skills/engineering/diagnosing-bugs/SKILL.md` `[全文]`、`scripts/list-skills.sh` `[全文]`、`scripts/link-skills.sh` `[全文]`
- `upstreams/cursor-plugins`：pstack 的 `show-me-your-work`、`figure-it-out`、`create-verification-skill`、`maintain-verification-skill`、`architect`、`blast-radius`、`swarm`、`interrogate`、`poteto-mode`、principle（`prove-it-works` / `sequence-verifiable-units` / `never-block-on-the-human` / `boundary-discipline` / `model-the-domain` / `encode-lessons-in-structure`）、playbooks（`bug-fix` / `perf-issue` / `runtime-forensics` / `trace-forensics` / `investigation` / `autonomous-run` / `pause-safely` / `session-pickup` / `eval` / `hillclimb` / `feature` / `multi-phase-plan` / `orchestrate`）、`automations/benny/skills/reproduce-and-fix-issues/SKILL.md` 与 `references/verify-existing-fix.md`、`docs/guide/06-verify-and-ship.md`、`skills/show-me-your-work/scripts/log.sh` `[全部全文]`；`cursor-team-kit` 的 `control-ui`、`control-cli`（目录）、`verify-this`、`run-smoke-tests` `[全文]`
- `upstreams/addyosmani-agent-skills`：`skills/performance-optimization/SKILL.md`、`skills/doubt-driven-development/SKILL.md`、`skills/interview-me/SKILL.md`、`skills/planning-and-task-breakdown/SKILL.md`、`skills/debugging-and-error-recovery/SKILL.md`、`references/definition-of-done.md` `[全部全文]`；其余 skills `[仅目录]`

**四号来源（只读消费方契约，非三仓吸收）**：`/Users/yuantian/Developer/ekunai/Unified-Customs-Bonded-Intelligence-Platform/docs/active/engineering-method-routing.md` `[局部：18–32 行]`、`multi-agent-development-principles.md` `[局部：125–145 行]`。本文件凡引用它，一律标注 `消费方契约（非三仓）`。

---

## 1. C1 · 环境/运行条件不就绪时无人负责修

### 1.1 本库现状（原文定位）

| 位置 | 原文 | 问题 |
|---|---|---|
| `roles/investigator.md §6` | 「造不出回路、需要能复现的环境或现场材料 → 向 `roles/driver.md` 要资源，由 Driver 决定」 | 只要资源，没有"资源不存在时怎么办"的下一步 |
| `roles/investigator.md §4.1` 步骤 5 | 「造不出回路：停手，明确说出来，列出试过的方法，然后要么要到能复现的环境……没有回路之前不许给结论」 | 方法正确，但停手之后的归属是空的 |
| `roles/verifier.md §6` | 「环境/资源不满足、无法构造真实路径 → `roles/driver.md`（要资源或改验收范围）」 | 同上 |
| `roles/verifier.md §4.1` 步骤 2 | 「这些条件不成立就**先报协调方，不开始验证**」 | 只定义了"报"，没定义"报什么、谁接手" |
| `roles/verifier.md §8` 尾行 | 「……或**先修条件再跑**」 | 全库唯一一句"修条件"，§4 没有对应方法，也没有权限 |
| `roles/driver.md §5` | 「我可以：拆分与排序任务；决定并行与写窗；划定禁止改动的范围；发任务卡与交接；指定复核与审查资源」 | 没有"修环境"，也没有"把环境阻塞变成一张卡"的规则 |
| `pipeline.md §4` | 「`资源可用`：数据库、端口、进程、依赖目录、外部配额可用」 | 已有依赖类型，但没有"这类依赖被阻塞时谁去解除" |

结论：**这是一个真实的断档**。`资源可用` 是四类依赖之一，但解除动作没有主人；Investigator/Verifier 只能"要"，Driver 只能"排"。

### 1.2 三仓证据（同等机制在三仓的对应物）

**A. pstack `create-verification-skill` — 把"可驱动面"定义成一份可执行的自证物**

- `upstreams/cursor-plugins/pstack/skills/create-verification-skill/SKILL.md:28`
  > 「**Doctor:** one read-only check that answers "is this instance worth driving?" — process up, right version/build, port owned by us, auth valid. An agent runs this first whenever anything looks off.」
- 同文件 `:21`
  > 「If the checkout doesn't build or start as-is, **fix that first (or report it precisely)** before generating; a skill written against a broken base teaches wrong steps.」
- 同文件 `:38-40`（这一条是"交什么收据"的核心判据）
  > 「Run its own instructions end to end once: launch, doctor, drive ONE mapped feature … capture evidence, clean up. … **A generated skill that was never executed is a draft, not a deliverable.**」
- 同文件 `:19`
  > 「**Isolate:** can two instances run side by side (ports, data dirs, profiles)? If not, say so in the generated skill: refusing to double-drive a shared instance beats corrupting the user's session.」

五段结构（Launch / Doctor / Drive / Evidence / Cleanup）+ "必须自证一次"= 我所说的"可驱动面"上游原型。

**B. pstack `figure-it-out` — 把建 harness 排进流程，并且是**改动前**的动作**

- `upstreams/cursor-plugins/pstack/skills/figure-it-out/SKILL.md:29`
  > 「**Build the verification harness before the work, with the baseline captured from the pre-change state**, so the check reads as "old value vs new value".」

**C. pstack benny `reproduce-and-fix-issues` — 缺能力时的合法收据是 `Blocked` + 缺了哪一项**

- `upstreams/cursor-plugins/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md:132` 列表要求七项能力：① 拉起目标 app 与测试环境 ② 导航到被映射的功能与状态 ③ 用真实 UI 驱动 ④ 只读检查状态 ⑤ 截图 ⑥ 录制/停止录屏 ⑦ 清理进程、会话、profile、临时数据
- 同文件 `:142`
  > 「**If the adapter is absent or any required capability is missing, mark the operations status as blocked and stop. Do not pretend a screenshot, unit test, state mutation, or source reading is a UI repro.**」
- 同文件 `:183`
  > 「Use the configured repro budget. … If the environment cannot provide a required capability, **report `Blocked` and state what was missing**.」

**D. cursor-team-kit `control-ui` — 复用优先；不许跨仓硬编码；跑完清理**

- `upstreams/cursor-plugins/cursor-team-kit/skills/control-ui/SKILL.md:8`
  > 「**First reuse the repo's own** Playwright, browser, or Electron harness if it exists; otherwise assemble a temporary local harness around the app's dev server or Chromium debug port.」
- 同文件 `:20`「Start the app locally using **the repo's documented dev command**」
- 同文件 `:108-109`「Do not hard-code selectors, ports, or script paths from another repository. Discover the current repo's local app markers.」「Clean up dev servers, debug sessions, and temp profiles when done.」

**E. cursor-team-kit `verify-this` — 环境差异直接判 `INCONCLUSIVE`，不许硬判**

- `upstreams/cursor-plugins/cursor-team-kit/skills/verify-this/SKILL.md:24`
  > 「Capture treatment from the changed state **with the same command, data, warmup, and environment**.」
- 同文件 `:57`
  > 「`INCONCLUSIVE`: no valid baseline, noisy signal, failed measurement, or **an environment difference invalidates the comparison**.」

**F. matt `diagnosing-bugs` — 造不出回路时：停手、列出试过的、要点名要哪一种环境/材料**

- `upstreams/mattpocock-skills/skills/engineering/diagnosing-bugs/SKILL.md:53-64`
  > 「### When you genuinely cannot build a loop / Stop and say so explicitly. List what you tried. Ask the user for: (a) access to whatever environment reproduces it, (b) a redacted captured artifact …, or (c) permission to add temporary production instrumentation. **Do not proceed to hypothesise without a loop.**」
- 同文件 `:31` 提供"退而求其次的回路"：**Throwaway harness**（单服务 + 假依赖，单次函数调用走通故障路径）

**G. pstack `principle-prove-it-works` — 检查要脚本化，产物留给人重跑**

- `upstreams/cursor-plugins/pstack/skills/principle-prove-it-works/SKILL.md:18-20`
  > 「**Script the check when you can** / The strongest proof is a deterministic script that re-runs the same comparison, not a one-time eyeball. Write the script, run it, and keep its output as an artifact a reviewer can re-run instead of trusting your word.」

### 1.3 三仓的归属结论（回答"补角色还是补方法"）

三仓**都没有**"环境检修角色"。三仓一致的做法是：

1. **要驱动的人自己建** harness（pstack `figure-it-out`、`create-verification-skill`、`control-ui` 都是同一执行者）；
2. **先复用仓库已有的 harness**，没有再临时组装（`control-ui:8`）；
3. **建不出来就交一个 `Blocked` 结论，并点名缺哪一项能力**（benny `:142`、`:183`；`verify-this:57` 判 `INCONCLUSIVE`）；
4. **改动前就建好并采好基线**（`figure-it-out:29`）；
5. **harness 必须自己先被跑通一次**，否则只是草稿（`create-verification-skill:38-40`）。

**"谁修"的答案三仓也没有独立角色**：pstack 把"仓库跑不起来"当成生成器要处理的前置问题（`create-verification-skill:21` "fix that first (or report it precisely)"），matt 把它变成"点名要哪一种环境/材料"（`diagnosing-bugs:53`）。**没有"环境管家"这个角色。**

### 1.4 只读消费方契约（非三仓）的对应

`消费方契约（非三仓）`：`engineering-method-routing.md:18-32` 的路由表里已经有一行：

> | agent 不会正确驱动真实系统 | `tim-professional-workflow` 的 `drive-preview` | **Launch/Doctor/Drive/Evidence/Cleanup 记录 + 证据** | 验证角色 |

三仓证据与这条契约同向、同结构（五段 + 证据 + 验证角色）。**SOURCES.md 只把整张路由表登记成一句 `@产出 des`（`SOURCES.md:437`），这一行从未真正落地**——这与 C2 里 `domain-modeling` 变成死链是同一类失误。

### 1.5 结论

- 本库**已有**两个天然落点：`verifier.md §4.1/§4.2`（真实入口驱动 + 环境断言）与 `investigator.md §4.1`（判红的回路）。
- 缺的是三件东西：①**五段方法**（launch/doctor/drive/evidence/cleanup）；②**一份有 `state` 的收据**（ready / blocked / not-attempted + 缺哪一项）；③**阻塞后的路由规则**（谁在什么授权下把它变成可开工的卡）。
- **不建议新增角色**：三仓无此角色；且本库自己的纪律是"不为没有消费者角色的需求新增抽象"（`SOURCES.md §4.9` 用同一理由删过一组依赖类型）。环境是**状态**不是**纪律**，状态的解除是"谁写权归谁"的问题，不是"谁常驻"的问题。

---

## 2. C2 · 术语/领域事实归属零 owner

### 2.1 本库现状

`grep -rn "domain-modeling|术语|词汇表|命名裁定" roles/ pipeline.md`（任务卡已核）= **只命中 1 处**，且是 `driver.md §4.8` 步骤 6「不用术语替代事实」——那是**汇报语言**规则，不是领域事实归属规则。角色文件里没有任何"读项目的术语表 / 术语冲突要二选一 / 术语解析出来写回哪里"的动作。

R1 历史（已核）：`git show HEAD:roles/architect.md` 第 44 行确实写着
> `- skills/domain-modeling/SKILL.md`（领域建模与不变量收敛）

——那是把**上游技能目录**当引用，属于"引用一个本库不该引用的外部路径"；重写改成角色文件载体后，它被登记为 `NOT ABSORBED`（`SOURCES.md:176`，`[仅目录]` 未读全文），于是这条能力整体消失。

### 2.2 三仓证据

**A. matt `domain-modeling`（主来源，全文读过）**

- `upstreams/mattpocock-skills/skills/engineering/domain-modeling/SKILL.md:3`（description）
  > 「Build and sharpen a project's domain model. Use when discussing codebase terminology, writing or editing a CONTEXT.md, or recording or editing an ADR.」
- 同文件 `:44`「### Challenge against the glossary / When the user uses a term that conflicts with the existing language in `CONTEXT.md`, call it out immediately.」
- 同文件 `:60`「### Update CONTEXT.md inline / When a term is resolved, update `CONTEXT.md` right there. **Don't batch these up: capture them as they happen.**」
- 同文件 `:64`「`CONTEXT.md` should be totally devoid of implementation details. **It is a glossary and nothing else.**」
- 同文件 `:68-70` ADR 三条件：**Hard to reverse**（晚改代价大）＋ **Surprising without context**（未来读者会问为什么）＋ **The result of a real trade-off**（有真实备选）。三条缺一就不记 ADR。
- 同文件还有两条未在任务卡点名的动作：**Sharpen fuzzy language**（把"account"逼成 Customer 还是 User）与 **Cross-reference with code**（用户说的和代码不一致时把矛盾摊开，而不是选一个）。
- 同文件 `:11` 说明边界：**只是读 CONTEXT.md 取词汇不算这个技能**；这个技能是**改变**模型时的主动纪律。

**B. pstack `principle-model-the-domain`（互为补充，但目标不同）**

- `upstreams/cursor-plugins/pstack/skills/principle-model-the-domain/SKILL.md:3`
  > 「Encode the domain in a structure instead of scattered conditionals.」
  这一条讲的是**代码结构**（状态机 > 散落布尔、错误状态不可表示），与 matt 的**词汇表/ADR**是两件事。本库 `architect.md §4.3`（数据形状先行、不变量编码进类型）已经吸收了它的结构侧；**词汇表侧完全没有**。

**C. 其他**

- `matt diagnosing-bugs:5` 也点名了消费方式：「When exploring the codebase, read `CONTEXT.md` (if it exists) to get a clear mental model of the relevant modules, and check ADRs in the area you're touching.」——即"读术语表"是**任何开工前**的动作。
- pstack、addy **没有**对应的术语/领域词汇机制（addy 的 `documentation-and-adrs` 讲 ADR 写法，但不在本库已读范围，且它不含"术语冲突即二选一"的动作）。

### 2.3 只读消费方契约（非三仓）的对应

`消费方契约（非三仓）`：`engineering-method-routing.md:21-27` 的路由表：

> | **术语/事实归属冲突** | `domain-modeling` | **术语裁定 + 落点（`CONTEXT.md`/ADR/契约）** | Driver 指定角色 |

即下游已经把"谁读方法"写死成 **Driver 指定角色**，"最小产物"写死成 **术语裁定 + 落点**。这条契约与 matt 的机制一致，且比 matt 多说了两点：**裁定要落到三选一的位置**（CONTEXT.md / ADR / 契约），**由 Driver 指定承担角色**。

### 2.4 结论

- 机制是**有主**的（Architect 是数据形状与命名的 owner），缺的是：①**读**的动作（开工前读项目词汇表）；②**冲突即二选一**的动作；③**写回**的落点与写权；④**边界**（glossary 只放词汇，ADR 三条件）。
- 落点文档（项目侧）= `CONTEXT.md`（多上下文用 `CONTEXT-MAP.md`）+ `docs/adr/`；**本库不 vendor 上游技能目录**，机制必须写进角色文件并在 `SOURCES.md` 登记 `file:line`。
- **本库自身不需要 CONTEXT.md**（它是方法库，没有业务词汇）；本库自己的"术语单一来源"是 `identity.md`（对象身份）与 `SOURCES.md`（机制出处），与 C6 同族。

---

## 3. C3 · 性能诊断方法缺正文

### 3.1 本库现状

`roles/verifier.md §4.5` 只有"噪声门"：先量噪声带（≥2 次），效应落在噪声带内只报"未测出"，机制型指标可直接采信，任何"这轮变差了"先跑同码复现。`roles/verifier.md §4.8` 有"回退也记账"的台账。
`roles/investigator.md §4.5` 反例一行：「不适用：性能类问题不要用日志探针；先建立可比较的基线测量，再二分。」

`SOURCES.md` 自己承认（第 236 行附近）：

> | `skills/performance-optimization/SKILL.md:30-39` | 五步：测量 → 定位 → 修 → 验证（留或回退）→ 设防 | **不采纳（未落地）** | 五步循环……未落成角色动作；本库只落地噪声带与「先量后说」 |

`.pi/round3/REPORT.md` §④ 也把它列为未修项：「性能诊断的完整方法（瓶颈定位表 + 测量清单）| 卡 §4 明说仍为欠账」。

### 3.2 三仓证据（addy `performance-optimization`，全文读过）

- `upstreams/addyosmani-agent-skills/skills/performance-optimization/SKILL.md:10`
  > 「Measure before optimizing. … Profile first, identify the actual bottleneck, fix it, measure again. Optimize only what measurements prove matters.」
- 同文件 `:30-39` 五步工作流：`1. MEASURE → 2. IDENTIFY → 3. FIX → 4. VERIFY（keep or revert）→ 5. GUARD`
- 同文件 `:73`「### Where to Start Measuring」——**症状 → 先测什么**的决策树：
  - 首屏慢 → 大 bundle？→ 量 bundle size / 代码分割；服务端响应慢？→ 量 TTFB（DNS / TCP+TLS / 等待）；渲染阻塞资源 → network waterfall
  - 交互卡 → 主线程长任务 >50ms；表单输入延迟 → 重渲染；动画 jank → layout thrashing
  - 导航后慢 → 数据加载 / 客户端渲染
  - 后端 / API → 单接口慢（查查询计划与索引）/ 全部接口慢（连接池、内存、CPU）/ **间歇性慢（锁竞争、GC、外部依赖）**
- 同文件 `:99`「### Step 2: Identify the Bottleneck」——前端/后端两张"症状 → 可能原因 → 怎么查"的表（慢 LCP / 高 CLS / 差 INP；慢 API / 内存增长 / CPU 尖峰 / 高延迟）。
- 同文件 `:157`：索引不是猜出来的——「"Add an index" is the guess. **The query plan is the measurement**」，用 `EXPLAIN ANALYZE` 三个读数决定修法（Seq Scan / 行数估值偏差 / Sort 节点）；`:185`「An index that did not change the plan is a revert」。
- 同文件 `:387`
  > 「**"Neutral" is a revert, not a keep.** … the change is already written, throwing it away feels wasteful, so it lands unmeasured, and the codebase accretes complexity that never bought anything.」
- 同文件 `:391`「#### Log every attempt, including the reverted ones」——回退掉的尝试也要记账（"the same dead idea gets tried again next quarter"）。
- 同文件 `:403`「### Step 5: Guard Against Regression」——只守用户真正感受到的那个指标；合成 CI 门 + 现场监控两层；任一触发就回第一步重建基线。

### 3.3 三仓的边界判断

- **addy 的方案是"语言/框架无关的方法骨架 + 工具专有示例"混排**。后半（`EXPLAIN ANALYZE`、`React.memo`、连接池大小、`web-vitals` 代码）是具体协议与语言形态。
- 本库已有先例：`SOURCES.md` 第 195–215 行附近因"全是具体语言与协议形态；本库不绑定语言与协议栈"删掉了 `api-and-interface-design` 的幂等键/品牌类型等条目。同一标准要一贯执行。
- **pstack 另有一份"策略族"（不是表）**：`playbooks/perf-issue.md:8-16` 的八个假设生成器（elimination / divide and conquer / caching / indirection / batching / redundancy / lazy evaluation / scheduling），并明确「Use them as hypothesis generators, not a checklist. A family earns an attempt only when the trace shows the signal it names.」这是**方法级**内容，不是工具级。

### 3.4 结论

本库**应当含此环节**（它是"测量类主张"的定位方法，与 `verifier §4.5` 的噪声门是同一条链的上下游），但只搬**方法骨架**：

- `Verifier §4.5` 补测量清单：同命令/同条件复测（existing）、中性=回退、一次只改一个、尝试台账（`§4.8` 已有，引用不重复）、守用户可感的那个指标；
- `Investigator` 补定位动作：先建**可比基线**（改动前采），再按**症状→要测什么**的通用映射选对象，再二分/差分；显式写"性能类不用日志探针"。
- **不搬**工具专有表（Lighthouse、EXPLAIN、React.memo、连接池数值、web-vitals 调用），理由与 `SOURCES.md` 已登记的删减标准一致，代价是：具体工具怎么做查不到了——这是有意的底座解耦，记在 SOURCES 的"未吸收"栏。

---

## 4. C4 · 停止条件/轮次被三处各自定义，默认值来源错位

### 4.1 本库现状（三处定义 + 一处来源）

| 位置 | 原文（关键句） | 量的东西 | 数字 |
|---|---|---|---|
| `pipeline.md §7` | 「同一故障或同一判据**连续两轮失败且没有新证据**：停手。」+「不许发第三个补丁」 | 失败修复轮次 | 2 |
| `roles/driver.md §4.5` | 「同一**前提**连续失败就停下来」；步骤 2–5 是清点与归因 | 失败修复轮次（另一套措辞） | 无数字 |
| `roles/planner.md §4.7` | 「同一判据连续**两轮**失败且没有新证据」 | 失败修复轮次（第三套措辞） | 2 |
| `roles/reviewer.md §4.7` | 「**两轮**之后仍有阻断：停止在这个候选上循环」 | **审查轮次**（同一候选被审几轮） | 2 |
| `roles/reviewer.md:215` | 「本库取**两轮**（来源：消费者契约「默认最多两轮审查」），不采纳上游 addy … 3 cycles」 | 来源标注 | — |

另外三处重复的还有「不许发第三个补丁」：`investigator.md §4.6` 步骤 5、`driver.md §4.5` 反例、`planner.md §4.7` 步骤 3、`pipeline.md §7`。

### 4.2 三仓证据

**A. addy `doubt-driven-development`（全文读过）— 它量的确实是另一个东西**

- `upstreams/addyosmani-agent-skills/skills/doubt-driven-development/SKILL.md:186-191`
  > 「Stop when: … **3 cycles completed** (escalate to user, don't grind a fourth alone), or User explicitly says "ship it" … **Do not lift the bound.**」
- 同文件 `:215` 红旗：「**Doubt theater (checkable signal)**: across 2 or more cycles where the reviewer surfaced substantive findings, zero findings were classified as actionable.」
- 关键：它的 cycle 是**同一产物被反复怀疑/复核的循环**（每一轮都用 fresh-context reviewer 重看同一 artifact），不是"同一候选的审查-返修轮次"。本库 reviewer 的"两轮"是**第一轮 blocker → 定向返修 → 新候选再审一轮**。`reviewer.md:215` 对这一区别的判断**正确**；错的是它把**下游契约**当成了本库默认值的来源。

**B. pstack — 用一个**谓词**而不是轮数来停**

- `playbooks/autonomous-run.md:1`:「**You own the exit condition. Define done, then drive to it without stopping.**」Step 1: 「State the exit condition as a checkable predicate before the first iteration (tests green, repro fixed, all N PRs merged, pixel-diff zero).」
- `playbooks/hillclimb.md:1`:「a checkable stop predicate that pairs a target with a floor on attempts so a lucky early win can't end the run」——**目标 + 尝试下限**的组合，而不是"最多几轮"。
- `playbooks/orchestrate.md:97`:「**Retry by mode**: cap-hit or oom, respawn with smaller scope. Network-drop, retry as-is. Tool-error, retry on a different model. Unknown, retry once. **Two retries, then abandon the unit and replan around it.**」——按**失败模式**分类的重试预算（也不是按"轮"）。同一个 playbook 的停止线是「write a stop line at the top of the standing orders, let in-flight work finish, fix the cause, clear it.」
- `playbooks/perf-issue.md:4`:「When evidence refutes a hypothesis, revert what it motivated.」

**C. matt**

- `diagnosing-bugs` 无轮次上限；它用「一段时间后仍造不出回路 → 停手、列出试过的、点名要什么」替代。没有"最多几轮"的默认值。

**D. 三仓一致点**：**没有第二个来源把"两轮"当通用默认**。addy 的 3 cycles 属于另一个量；pstack 用谓词与失败模式分类；matt 用具名阻塞替代。**"来源：消费者契约"是本库独有的、且与本库自身定位冲突的写法**。

### 4.3 只读消费方契约（非三仓）的对应

`消费方契约（非三仓）`：`multi-agent-development-principles.md:131-140` 原文（本文件 §6 部位读到）

> 「默认最多**两轮审查**：第一轮 → 原 Implementer 一次定向返修 → 同一 Reviewer 第二轮。第二轮仍有 blocker，停止该候选继续循环，升级给技术判断角色…… **不靠换 SHA／换人重置**。」

所以"两轮"在下游**是存在的**，但它是**那个项目的约定**。本库若把它当默认，就等于把一个下游的具体约定写成本库的抽象默认——这违反本库自己的 `SOURCES.md §4.10`（来源类型分级表：消费方契约"即使被 Owner 采纳过"也不构成抽象默认值）。

### 4.4 结论

1. 三处定义的是**两个不同的量**（失败修复轮次 / 审查轮次）。它们可以各自有 owner，但**不能各自定义数字**。
2. 数字默认值必须有唯一 owner，且来源必须是**本库自定（附理由）**或**显式标注的下游覆盖值**。
3. 三仓支持"用谓词 + 失败模式分类"而不是"用一个通用轮数"；本库可以把"同一判据连续失败"保留为**事件**，把"几轮"降级为**本轮装配参数**（本库默认值只写在 `pipeline.md §7`）。
4. `orchestrate.md:97` 提供了第三种可选形态：**按失败模式分类的重试预算**（不同失败不同次数），代价是复杂度上升、且需要失败模式分类器；本计划把它列为"可选、不默认采纳"。

---

## 5. C5 · 数字的合法性规则与 Architect 的成本估算相撞

### 5.1 本库现状

| 位置 | 原文 | 性质 |
|---|---|---|
| `roles/planner.md §4.5` 触发条件 | 「需要在卡里写量化门槛（覆盖率、体积、耗时、延迟）」 | 只管**门禁**数字 |
| 同节步骤 2 | 「三个合法来源：**用户要求 / 既有契约 / CI 配置**。**没有授权阈值时不得自建门禁**：只报告**测量值与不确定性**……把阈值写成「待确认」」 | 三来源规则 |
| 同节步骤 3 | 「有数字没有命令的那一行是愿望，不是约束」 | 可判否要求 |
| `roles/planner.md §5` | 「我不可以：……发明没有来源的量化指标」 | 与 §4.5 同义 |
| `roles/planner.md §2` | `change_cost`「下次改动成本估算…缺：无法判断切片边界是否合理」 | **估算被当成判断输入** |
| `roles/architect.md §4.6` | 「假设下一次同类需求出现，问：要改哪几个文件？…把答案写成"**波及面清单 + 一句理由**"，**不写成分数**」 | 估算形态（非数字） |
| `roles/planner.md §4.3` | 体量按 `1 个文件=极小 / 1–2=小 / 3–5=中 / 5–8=大 / 8+=过大` | 切片启发式 |
| `roles/reviewer.md §2` | 收 `design-proposal.change_cost` | 审查也用它 |

**全库没有任何一句说"估算不是门禁"**——`grep` 零命中。而 planner §5 的措辞（"发明没有来源的量化指标"）在字面上会把它自己在 §2 里接收的 `change_cost` 一起判为非法。

### 5.2 三仓证据

**A. 估算在 addy 那里是**分解启发式**，不是门禁**

- `upstreams/addyosmani-agent-skills/skills/planning-and-task-breakdown/SKILL.md`「### Task Sizing Guidelines」：`XS/S/M/L/XL` 的**用途**是"如果任务是 L 或更大，就继续拆"；「Estimated scope」只是卡片字段。
- 它的**门禁**另有其物：`references/definition-of-done.md:63`「"It's done, I just haven't run it yet": **unverified work is not done**」——门禁是可判否的**状态**（跑没跑），不是数字。
- 同文件 `:23`（Task List Target）与 Verification 段：门禁写成"能跑的命令 + 能判否的条件"，例如 `Tests pass: [the repository's focused-test command]`。

**B. pstack 的成本比较也是定性/结构性**

- `pstack/skills/architect/SKILL.md:26`（Phase B 比较）「Compare viable candidates on **interface depth**. Prefer the design that hides more complexity behind a smaller, simpler public surface.」——没有分数。
- `pstack/skills/blast-radius/SKILL.md:2` 的"风险"要求「Give it a **real chance of happening and a real cost if it does**」——要求真实，但不要求数字化。
- `pstack/skills/poteto-mode/playbooks/orchestrate.md:60`「**Quantify scope**: units, rough effort, expected stacks, and the wall-clock budget」——**rough**（粗估），且它管的是"值不值得按这个规模跑"，不是"过不过门"。

**C. 三仓的共同点**：**阈值/门禁必须有可判否的命令或可观察状态；估算只需要"依据 + 用途"，允许粗、允许区间。**

### 5.3 只读消费方契约（非三仓）的对应

- `engineering-method-routing.md:23`：`design-compare` 最小产物含**"下次改动成本估算"**（`change_cost` 的提法出处，`SOURCES.md:438-442` 已如实登记为消费方契约）。
- `multi-agent-development-principles.md:73`（`SOURCES.md:293` 同一行的乙方来源）：「**约束来自事实和产品目标，不强行指定行数、触点数或实现细节**」；`engineering-method-routing.md:28-30`（`SOURCES.md:293` 的甲方）：「**填了必须有产物支撑，不得写成仪式**」。
- pstack 的同族句（`SOURCES.md:293` 的乙方）：**"Most teams don't have a number, and an invented one gets ignored."** → 默认动作是"测量并保持"。

### 5.4 结论

碰撞的根因是**没有把数字分成类**。三仓与外部的共识是三类：

1. **门禁数字**（能判否、能拦交付）：只允许三个授权来源 + 必须配一条判定命令；
2. **估算 / 判断输入**（`change_cost`、体量、波及面）：用于比较与切片，**不构成门禁**，写"用途 + 依据"即可，允许区间与相对量；
3. **测量值**（一次或几次读数）：只作报告，**不自动升级为门禁**（噪声门在 verifier §4.5，已落地）。

落点：`planner.md §4.5`（加定义与三分类）、`planner.md §5`（改措辞：禁止的是"把无授权来源的数字写成门禁"）、`architect.md §4.6`（写明 `change_cost` 是判断输入、不是门禁）、`planner.md §2` 的 `change_cost` 行（标注"估算，非门禁"）。

---

## 6. C6 · 本库缺"同一条规范只由一处拥有"

### 6.1 本库现状

`grep -rn "只由一处拥有|单一所有者|一处拥有" roles/*.md pipeline.md AGENTS.md` → **零命中**。
最接近的两句都不在这条原则上：

- `roles/architect.md §4.3` 步骤 4：「每条不变量**只有一个来源**：能派生的就派生，不要双向同步」——这是**代码设计**规则，不是库自身的规范所有权规则。
- `closure.md` 维护规则：「本表字段与角色文件不一致时，以角色文件为准」——这是一处**特例**，不是一般原则。

**症状（C4 之外还查到两处同类残留）**：

| 重复内容 | 出现处 | 数量 |
|---|---|---|
| 停止条件/轮次 | `pipeline §7`、`driver §4.5`、`planner §4.7`、`reviewer §4.7` | 4 |
| 「不许发第三个补丁」 | `investigator §4.6`、`driver §4.5`、`planner §4.7`、`pipeline §7` | 4 |
| **证据复用四条件** | `pipeline §8`、`verifier §4.7`、`integrator §4.5`（逐字） | 3 |
| `ws:v1` 身份算法 | `identity.md` + 6 个角色内联 | 7（**这一处是有意为之**，见 6.2） |

### 6.2 三仓证据

**A. matt `writing-for-agents`（全文读过）— 直给原则与反例**

- `upstreams/mattpocock-skills/skills/productivity/writing-for-agents/SKILL.md:78`
  > 「**Keep each meaning in a single source of truth**: one authoritative place, so changing the behaviour is a one-place edit. **Duplication** (the same meaning in more than one place) costs maintenance and tokens, and inflates a meaning's prominence on the ladder past its real rank. (The accidental inverse of a leading word, which repeats a token on purpose, never the meaning.)」
- 同文件同段还区分了三个不同现象（这是本库现在混在一起的）：**duplication**（一个含义两处）／**scattering**（一个含义碎成很多处）／**cache**（把环境里查得到的东西抄进文档）。
- 同文件末尾给出"什么时候抄是合理的"判据：**只有当查一次很贵时**才把它抄成 cache（"Cache what the agent cannot find by looking"）。

**B. pstack `orchestrate`— 一写者 + 派生视图，两条可操作规则**

- `pstack/skills/poteto-mode/playbooks/orchestrate.md:23`
  > 「Every file has exactly **one writer**. **Owners publish facts, readers aggregate at read time.**」
- 同文件 `:32`
  > 「`status.md` is derived from `units.tsv` and `ledger.tsv` at each drain, **never hand-maintained. Regenerate it from the tables instead of narrating events into it.**」
- 同文件 `:25`
  > 「`preferences.md` is the standing-orders register: … When you **catch yourself restating an instruction, append the line before you act** (principle-encode-lessons-in-structure).」

**C. pstack `principle-encode-lessons-in-structure`**

- `upstreams/cursor-plugins/pstack/skills/principle-encode-lessons-in-structure/SKILL.md:3`
  > 「Apply when you **catch yourself writing the same instruction a second time**, or notice a recurring correction. **Encode the rule as a lint, metadata flag, runtime check, or script instead of more text.**」
  （同文件 `:14` 重复"second time"这一触发条件。）

**D. 三仓的边界（重要）**：三仓都不追求"零重复"，它们区分**有意的重复**与**事故性重复**：
- 有意的：`show-me-your-work` 把格式定为唯一来源后说「Other skills route their audit trail here instead of inventing one. **Reference it by name and let it own the format. Don't restate the columns.**」（`show-me-your-work/SKILL.md:79`）——**引用而不复述**；
- 事故性的：同一规范在两个地方各自定义、各自可漂移（`writing-for-agents:78` 的 duplication）。

### 6.3 结论（并回答"能不能机械检查"）

这条原则必须**同时**容纳本库的核心约束"注入单元就是角色文件"（AGENTS.md 核心原则 2），所以它不是"禁止一切重复"，而是**三层结构**：

1. **事实源（唯一）**：一条规范/一个默认值只有一个权威位置。
2. **登记的内联副本（允许）**：为了单独注入而必须内联的副本，必须在 `SOURCES.md` 登记其事实源，且**内容必须一致**。`identity.md` + 6 份内联算法是现成的正面范例（有 G1 机械门守一致性）。
3. **禁止的竞争性定义（不允许）**：同一规范在多个位置各自定义（数字可以各自漂移、没人负责统一）——`C4` 的三处就是这一类。

**机械可检查性（如实回答）**：
- **可查**：① 内联副本与事实源的**结构性**一致（identity 的 G1 已经这样做）；② 生成物由脚本派生（`render-ledger.py --check` 已这样做）；③ 同一文件里同一句话逐字出现两次。
- **不可查**：**语义重复**（同一条规范换一种措辞写两遍）。上一轮已经用 `P5″`（中文二元组 + Jaccard）试过并按 R3 §7.4 删除，理由是"大量语义正确的落点重叠率也是 0.000……一个大量误报的门最终会被绕过或忽略，比没有更坏"。**结论：这条原则只能部分机械化，语义层必须交独立审查与人审，并且要把这条边界写在 checker 的输出里**（`check-library.py` 结尾已有"本检查判不了"段，可加一条）。

---

## 7. C7 · Driver 缺"推进前用自然语言讲清楚"的硬规则

### 7.1 本库现状

`roles/driver.md §4` 现有 8 个小节：4.1 对齐目标（frontier 提问）/ 4.2 分级与依赖 / 4.3 选档 / 4.4 写窗 / 4.5 停止条件 / 4.6 并行批处理 / 4.7 转手复核 / 4.8 收口与汇报。**§4.8 只管收口，不管推进前**。
唯一接近的一句是 `§4.1` 步骤 5：「frontier 清空后再开工；**Owner 确认之前不动手**」——那是**关于问题的确认**（缺 scope/success_signal/authorization 时），不是"动手前把要做的事讲清楚"。

任务卡自陈：「**我自己就是反例**——我把 SOURCES 台账这类 infra 问题推进了好几轮，从没在推进前用自然语言向 Owner 讲清楚'我要做什么、为什么、代价是什么'。」

### 7.2 三仓证据

**A. addy `interview-me`（全文读过）— 六要素复述 + 明确 yes + 停手**

- `upstreams/addyosmani-agent-skills/skills/interview-me/SKILL.md:94`「### Step 4: Restate intent in the user's own words」，结构为：

  > `Outcome: <one line>` / `User: <one line — who benefits>` / `Why now: <one line>` / `Success: <one line — how we know it worked>` / `Constraint: <one line — the binding limit>` / **`Out of scope: <one line — what we're explicitly not doing>`**

- 同文件 `:106`（原文）：「Including **"Out of scope"** is non-negotiable. Half of misalignment is silent disagreement about what is *not* being built.」
- 同文件 `:115`「**The gate is an explicit "yes."**」并列出不算 yes 的回答（"whatever you think is best" / "sounds good" / "sure, let's go" / silence）。
- 同文件 `:130`「**STOP YOUR TURN IMMEDIATELY.** Do NOT invoke tools or start downstream work in this turn.」
- 同文件 `:132`「### The 95% Confidence Stop / Can I predict the user's reaction to the next three questions I would ask?」

**B. pstack `figure-it-out` / `orchestrate` — 长跑前"呈现框架"，把代价与不做什么一起说**

- `upstreams/cursor-plugins/pstack/skills/figure-it-out/SKILL.md:19-23`
  > 「The definition of done as a falsifiable predicate. **Scope, quantified**: rough units and effort, plus the blockers grounding surfaced. The rigor level, biased high. … **Present the framing and tradeoffs before committing to a long run.** Reversible work proceeds (the **never-block-on-the-human** principle skill), but a multi-hour run earns one checkpoint.」
- `orchestrate.md:60`「**Present the framing once. Reversible prep proceeds without waiting.**」；`:39` 的 brief 模板是 `GOAL / SCOPE / CONTEXT / ACCEPTANCE / VERIFY / TIMEBOX / FORBIDDEN / REPORT / STANDING`，并说「**A field you cannot fill is a unit you have not scoped yet.**」
- `playbooks/multi-phase-plan.md:11` / `:34`：多 PR 计划「**State the protocol and this plan to the operator, then stop. Start execution only on the operator's explicit go.**」

**C. 反向约束（必须同时遵守）**

- `pstack/skills/principle-never-block-on-the-human/SKILL.md:1-3`
  > 「The human supervises asynchronously. Agents must stay unblocked. Make reasonable decisions, proceed, and let the human course-correct after the fact. … **Irreversible actions** … still require confirmation. **Reversible actions** … should proceed without blocking.」
- `pstack/skills/architect/SKILL.md:43-45`：`Phase C: Agree (opt-in)` —「**Default: proceed directly to implementation** with the synthesized design. **No human checkpoint.** Opt in to a checkpoint when the invoker explicitly asks」。
- `orchestrate.md:60`「Reversible work proceeds without waiting」（与 figure-it-out 同一句）。

**D. 三仓的一致形态**：**讲清楚（陈述）+ 只在长跑/不可逆/被点名时停**。不是"每次动作都要批准"。

### 7.3 只读消费方契约（非三仓）的对应

`消费方契约（非三仓）`：`multi-agent-development-principles.md:145`（`SOURCES.md:293` 上方那条）：方案审查门「**不满足不给小事加仪式**」；`:73`「小卡不填不扣分」。即下游同样反对把"讲清楚"变成"每件小事都走审批"。

### 7.4 结论

- 规则本身要硬（**任何推进前都要讲**），**形式可以轻**（一句话到六要素三档）。
- 判据要可检查：借 `interview-me` 的"**能不能用他自己的话复述**"与六要素清单（做什么 / 为什么 / 动哪些文件与范围 / 代价与风险 / 不做什么 / 怎么算成功）。
- 必须写清**边界**：这是**陈述**不是审批门；只有三类真的停下来等（授权缺失或变更、不可逆动作、Owner 明确要求确认），其余"讲完即推进"（与 `never-block`、`§4.1`、`architect Phase C` 一致）。
- 与 `§4.1` 的分工要在文本里互相指认：`§4.1` 管"要问的决定"（frontier），新小节管"动手前讲清的事"；不重述。
- `solo(1)` 档（Driver 由 Owner 亲自承担）时"向 Owner 解释"退化为"**写下**这段解释"——仍有价值（暴露假设），不是免做。

---

## 8. C8 · 脚本审计（8 个文件 / 1685 行 / 7 个无角色引用）

### 8.1 逐个读到的实现（按文件）

**① `scripts/check-library.py`（879 行）`[全文]`**
- 是什么：库自身的**只读文档一致性检查**。实测清单（脚本头部与 `main()` 内的 `record(...)`）：角色结构与 8 节顺序、注入契约声明、§4 反例数 ≥2、§8 行数 ≤4、角色内引用白名单、收据字段 ⊆ 产出方字段、拓扑双向、收据"缺了怎么办"非空、闭环矩阵 G3/相邻/角色交叉、可跳过路径 G5、死链、VERSION 单一来源、运行底座名称解耦（分片拼 token 以免自伤）、能力探测块恰一处、身份规范 G1 + 夹具 G2、开工门 B-6、替代收据 G5′、跳过可兑现 G7、唯一转手 G6、同名同形 G8、台账 P5 + P5′（调 `render-ledger.py --check`）、P5″ 已在 R3 删除。
- 它是**自证**（验文档规整度），不是"工作流能不能干活"的检查。它结尾自己打印：「本检查判不了: §4 方法的实质深度、语义正确性、字段值是否真实、某次跳过是否真的合规、以及「某条落点声称的动作是否真的写在那一步里」——这些交给独立审查与人审」。
- 消费者：`roles/**` 里 **0 命中**；`README.md:67`、`AGENTS.md:38/63`、`closure.md:46`、`identity.md:5` 引用它。`AGENTS.md` 纪律 6 把它写成"改动先自检"的**强制门**。
- 历史教训（`.pi/round3/REPORT.md` §7.3–7.5，我读了全文）：上一轮的抽样方法"把抽样单元选在了'正确答案'上而不是台账的实际声明上"，导致"21 条逐字回读"证明力为零；随后新增的 P5″ 因误报太多被删。R3 §7.5 的表格自陈：可机械化的只剩"锚点存在 / 字段集 / 产物名 / 形状"。

**② `scripts/render-ledger.py`（223 行）`[全文]`**
- 人写 key（`@短语`）→ 脚本从 `roles/*.md` 抽规则行（编号步骤 / 判断依据 / 契约块 / 条目 / 整段 / 表行），把「文件 · 节 · 小节 · 行类型与编号 · 原文」写进标记包裹的生成区；key 找不到或歧义 → 非零退出（fail closed）；`--check` 逐字比较。
- 消费者：`roles/ledger-custodian.md:14/51/52/150/173`（**明写**）+ `check-library.py` 的 P5′。判：**工作**。

**③ `scripts/ws-identity.sh`（211 行）`[全文]`**
- `ws:v1` 的参考实现：`manifest`（规范化清单，NUL 分隔、排除规则、字节序排序、删除行带 `-`）、`digest`、`compare`（只比两份清单）、`verify`（按范围声明重新枚举当前源文件，五类异常 MISSING / CHANGED / SCOPE_NOT_IN_MANIFEST / PSEUDO_DELETE / BAD_PATH，一律非零退出）。
- 消费者：`identity.md:90-93`（明写）；6 个身份角色内联了算法（**刻意不依赖脚本**，为了单独开工）。判：**工作**（身份计算的可执行实现）。

**④ `scripts/identity-selftest.sh`（183 行）`[全文]`**
- 正负夹具：P1/P1b 规范化、N1 内容差异、N2 路径差异、N3 删除入单、N5 漏写、N6 引用不存在文件、N4 排除规则，V0–V6 的 `verify` 五类异常 + "源文件改了拿旧清单复核"（`compare` 测不出来的那类）。
- 消费者：`check-library.py` G2 自动跑；`SOURCES.md` 把它登记为"本库自定 + 实测"主张的证据载体；`identity.md:94`。判：**自证**（但它是"主动改写"类主张唯一的可重跑证据）。

**⑤ `scripts/sync-upstreams.sh`（76 行）`[全文]`**
- 三个上游 clone 的只读 state 检查 + `--pull` 时才 `git pull --ff-only`；打印 behind 计数与最近 5 条提交。
- 消费者：`AGENTS.md` 纪律 2（Layer 1）、`SOURCES.md §8`（"保留：它是 Layer 1 的入口"）；`roles/**` 0 命中。判：**维护工作**（不是角色工作流）。

**⑥ `scripts/check-team-version.sh`（65 行）`[全文]`**
- 读下游绑定文件的 `version:` 与 `VERSION` 比较；0 一致 / 1 绑定文件不存在 / 2 漂移 / 3 解析不出（fail closed，R2 的修复）。头注释自陈：「**本脚本只比对版本字符串，不校验内容快照**」。
- 消费者：`AGENTS.md` 纪律 2（Layer 2）；`roles/**` 0 命中；**下游项目尚无任何绑定格式**（`SOURCES.md §8` 承认"需要先有下游绑定的格式约定"）。判：**未接线的工作**。

**⑦ `scripts/log-decision.sh`（47 行）`[全文]`** + **⑧ `scripts/decision-log-template.tsv`（1 行）`[全文]`**
- logger：6 参数、按需建目录、首次写表头、用 `>>` 不用 `>`、剥离制表符/换行/回车、给 `= + - @` 开头的单元格加前导单引号（防电子表格公式执行）。
- 上游原文对照（已逐行比对）：`upstreams/cursor-plugins/pstack/skills/show-me-your-work/scripts/log.sh` 几乎逐行相同；`SOURCES.md:108/113` 登记为"保留（改写成 `scripts/log-decision.sh`）"。
- 消费者：`roles/verifier.md §4.8`「决策台账：只追加，不改历史」把**方法**写全了（时间/阶段/决定/理由/证据指针/结果、只在决策点记、只追加、收口前对账），但**没有点名脚本**；`roles/**` 对这个脚本 0 命中。判：**工作**，但缺一根"方法 ↔ 工具"的连线。

### 8.2 上游同类物的定性（用于判断"该不该有"）

| 上游 | 同类物 | 上游怎么定性它 |
|---|---|---|
| matt | `scripts/link-skills.sh`、`list-skills.sh`、`sync-plugin-version.mjs` | `link-skills.sh` 头部写死：「**This is a dev-only script, intended for use by maintainers of this repo. It is not a supported installer.**」 |
| addy | `scripts/validate-*.js` + `scripts/lib/skill-lint*.js`（合计 3802 行，含自测） | 库自身的校验套件（用于它自己的 skills） |
| pstack | `skills/poteto-mode/scripts/check-plan.mjs`（186 行，检查计划文档格式）、`worktree-audit.sh` | 前者被 `multi-phase-plan` 步骤 6 **明确接线**：「Run `node pstack/skills/poteto-mode/scripts/check-plan.mjs <plan.md>` and fix every line it prints」 |

**结论：上游普遍有"库自身维护/自检"脚本，且都明确标注 dev-only 或被某一步骤点名消费。** 本库的问题不是"有自检脚本"，而是：**① 没有一个角色步骤消费 `check-library.py`，却被 `AGENTS.md` 写成强制门；② 没有任何一处说明这些脚本里哪些是维护工具、哪些是角色工作流的一部分。**

### 8.3 结论（判据：① 消费者步骤；② 工作 / 自证；③ 留改删 + 谁接手）

| 脚本 | ① 消费者步骤 | ② 性质 | ③ 判 |
|---|---|---|---|
| `render-ledger.py` | `ledger-custodian §4.1` 步骤 1–2（明写）+ `check-library` P5′ | 工作 | **留**，不动 |
| `log-decision.sh` + 模板 | 方法在 `verifier §4.8`，**脚本没被点名** | 工作 | **留 + 在 `verifier §4.8` 点名脚本与用法**（方法↔工具连线；不点名就是一件没人用的工具） |
| `ws-identity.sh` | `identity.md §7` 明写；6 角色内联算法（刻意不依赖） | 工作 | **留**；在 `identity.md` 里标明它是"参考实现"，角色仍以内联规则为准（现状已如此） |
| `identity-selftest.sh` | `check-library` G2 自动跑；SOURCES 的实测证据 | 自证 | **留**（否则身份规范是纸面的；它是"主动改写"类主张唯一的可重跑证据） |
| `sync-upstreams.sh` | 维护者（`AGENTS.md` 纪律 2）；角色 0 命中 | 维护工作 | **留**，但**明标 dev-only/维护工具**（照 matt `link-skills.sh` 的做法），并从"角色工作流"的叙述中摘出去 |
| `check-team-version.sh` | 无（下游绑定格式不存在） | 未接线的工作 | **删**；职责交回下游（本库只在 `AGENTS.md`/`README` 声明"下游绑定必须能核验版本**与内容快照**"这个能力要求）。留着就是一个没有消费者的接口，违反 Owner 的"必须被证明有用" |
| `check-library.py` | 维护者；被 `AGENTS.md` 纪律 6 写成强制门；角色 0 命中 | 自证 | **留，但降级定性 + 加预算规则**：从"改动先自检的机器判据"降为"库自身的回归检查（dev-only），不产生任何判断结论、不构成交付门禁"；输出照旧贴进收口报告；并加一条**门预算**：新增检查必须附一次"它拦下过真实错误"的证据，否则删。**不重写、不删**——R3 证明它抓到过真错（G5′/G8/G3′ 的负夹具），删掉是净损失；但它不能继续当"工作流能不能干活"的替代品 |

**删掉 `check-team-version.sh` 的影响面（必须同批处理）**：`AGENTS.md` 纪律 2 与目录清单、`README.md` 目录段、`SOURCES.md §8` 的那句"保留"、以及 `check-library.py` 的死链检查（它会因为引用一个不存在的路径而报红）——四处要一起改。

---

## 9. 未证实 / 存疑项（如实列出）

1. **C1 的"谁写 harness"在真实底座里是否可行**：本库与底座解耦，我无法验证下游是否允许验证角色在临时空间装配浏览器/CDP/PTY harness。PLAN 里按"临时空间可写、落进仓库须走卡"设计，代价是某些项目里 harness 会被反复重造。
2. **C4 的"阈值属于第 3 层装配参数"是否会被 Driver 漏写**：我给了兜底（缺省→不开工/要说明），但没有下游真实装配说明可验证。
3. **C6 的"登记内联副本"机制**：`SOURCES.md` 是一份 145KB 的手写台账，新增"事实源 ↔ 内联副本"登记会不会让它更难维护，我没有实测。
4. **C8 对 `check-library.py` 的"留+降级"是判断不是实测**：我没有下游项目用它当门的证据，只有本仓 R3 历史。
5. **三仓未覆盖的部分**：C7 的"纯自然语言"要求（"不用术语替代事实"）在三仓里没有直接对应物——`interview-me` 要求"用对方的话复述"，但没说"不许用术语"。这一条本库已有 `AGENTS.md` 原则 6 作依据，属**本库自定**。
6. **C2 的写权设计**（Architect 落盘、其余角色提议）是三仓没有的问题（三仓是单会话），属**本库自定**，代价是可能增加一次交接。
