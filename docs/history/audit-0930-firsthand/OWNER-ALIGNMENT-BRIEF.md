# Owner 对齐简报 · 转交 `tpw-0929-driver`

来源：Owner 与外部审计会话（`01a0e83c`，非本库任何角色）进行的产品级对齐。
本文件是转达件，**不是裁定件**；里面的"修改点"一律**必须等推演结果出来再定**。
审计会话不再 push 这条线，由 driver 接手。

---

## 一、Owner 的核心批评（要原样往下传）

> 这个项目的构建要拆成几部分：**消化、融合、构建、推演**。
> **推演这一步肯定没做**，消化融合那块也有欠缺。

判断依据（审计会话核过的事实，全部是"推演五分钟就能发现"的）：

1. **A2 的时序自相矛盾**：`registry` 的 skills 段里 `research` / `trace-paths` 的 `inputs = [A1]`，而 `P0.produces = [A1, A2]`、`P0.required_inputs = []`——把"以 A1 为输入"和"与 A1 并列产出"同时登记了。
2. **A3 在结构上查不到**：`A3.consumers = [P1, P2, P5, P6]`，**没有 P0**；而 A3 在 `P1.produces = [A3, A4]` 才出。⇒ scout 写 A2 时 feature map 必然不存在，也不在消费名单里。
3. **计划没有独立审查环**：`A7` 的返工边写死在 registry——「附条件通过时回到 **P3** 重做」，回不到 P2（改计划）。
4. **「通知」不是义务**：9 份角色文件里 20 余处「告诉/发给/回报」，**没有一处**定义拒绝路径上的通知动作。
5. **环境勘察太薄**：`docs/coldstart.md` 第 1 步只有 4 行（能起独立会话 / 读写文件 / 会话间收发消息 / 能并行），**每仓库一次**，且**没有决策规则**（原文只说"改造流程的某部分——告诉 Owner"）。
6. **"拉起时下游是否已在场"没有裁决**：库把物理并行完全交给 runtime，driver 侧只有「缺件即停」这个**事后**动作。
7. **只有一轴**：driver 的"谁上场"完全由 `@tier-sizing` 的六项矩阵（任务体量/风险）决定，**没有任何一项是"当前环境能提供什么"**。

---

## 二、Owner 定的推演前提与三种形态

**前提（Owner 明示）**：直接假设 driver 具备
- 新建并**命名**可见会话的能力；
- 高自由度控制（指定模型、思考强度）；
- 完善的 session 间通信能力。

**不需要**规定用的是不是 herdr + pi。

**三种形态**：

| 形态 | 特征 |
|---|---|
| **1. 有可见会话 + 完善基础设施** | 看得见、可命名、可控制、可互通 |
| **2. 只有 agent teams** | teams 之间可通话（**DAG 可行**），但 **user 完全不能和 teams 里任何成员沟通** |
| **3. 单会话** | 什么都没有。**所有产物、所有阶段都得由 driver 负责** |

**推演方式**：对 `A1`–`A9` **逐件**推，每种形态下每件回答六个问题——
**谁产 / 什么时候 / 靠什么能力 / 能力缺了谁顶上 / 谁读 / 返工回哪。**

三种形态 × 9 个产物 × 6 问 = 推演的最小覆盖面。推演产物**落点由 driver 定**，但必须 durable、可被下一轮读到。

---

## 三、Owner 提出的修改点（**必须基于推演结果再定**）

### 3.1 第 8 点最重：**plan 的形态吸收不足**

已查实的**上游真身**（三条线，之前漏掉了）：

| 仓 | 计划/任务书 | 谁写 | 谁执行 | 关键约束 |
|---|---|---|---|---|
| **matt** | `.scratch/<feature>/issues/<NN>-<slug>.md`（本地一票一文件，blockers-first 编号）；或真实 tracker | **人敲 `/to-tickets`**（"The agent won't reach for it on its own"）；发布前必须拿编号清单给 operator 过（"Nothing reaches the tracker until you approve"） | **"running it (one session at a time, or a fleet) is your job, not the skill's."** | 票 = **tracer bullet**（窄而完整穿过所有层）；尺寸约束 = **放进一个 fresh context window**（因为捡起它的是一个从没见过你 spec 的 session） |
| **addy** | **`tasks/plan.md`（计划文档）+ 任务清单落 `tasks/todo.md` 或外部 tracker** | 调用该技能的 agent（另有 `commands/planning.toml`） | 下游按计划里的 Task List 取 | **"task list target 在这里定义一次，别处一律引用它"**；用 tracker 时 **plan 里保留有序索引 + 条目 ID/链接，不复制清单** |
| **pstack** | agent store 的 `docs/` 下的 plan 文件（`skills/poteto-mode/playbooks/multi-phase-plan.md`） | poteto planner | **operator 明确 go 之后**，按 plan 里命名的 execution playbook | **"You own the plan, not the code. The plan is a checklist an owner runs box by box and the operator audits from the evidence. The plan is the deliverable. Do not implement."**；探索用 subagents **返回 file pointers，不许内联**；**"One box is one unit of work. Every box names the evidence that checks it. Check a box only when its evidence exists, a file, a log line, a screenshot, a test run, or a SHA."**；写完跑 `check-plan.mjs`；**"Post the plan path and the script's output, then stop. Execution starts on the operator's explicit go."** |

**本库丢掉的两样**：
1. **落点约定**——谁写在哪、索引怎么指（三家都有，本库的 `A5` 没有）；
2. **"每个 box 必须带 Evidence"的结构**（pstack 有，本库没有）。

**指针要分两层**（Owner 澄清）：
- **上游产物指针**：冻结契约在哪、事实集在哪——builder 要去查；
- **下游报告指针**：裁决报告、验证报告——修的人要能找到。
- 这与 `to-tickets.md:30`「票文本里不写**代码**路径和代码片段」（那条是对的）**不冲突**。

### 3.2 角色与环境是**两轴**，不是一轴

形态 2/3 下，driver 若无法把会话摆到人面前，**A1 只能由 driver 自己产**——否则 voice 只剩"转译"，丢掉"澄清"。库里最接近的是 `solo` 档「我自己转成特殊 driver……不发派」，但 **solo 由任务体量触发，不是由环境能力触发**。
（实证：UCBIP 试装里 voice 派成了子代理，它只能把 `OWNER-BRIEF` 翻译成 A1 四栏，**不可能**满足 role 文件里「念一遍给 Owner 听」那一步。）

### 3.3 A3 是**常驻资产**，不是某阶段的产出

有代码的仓库里，driver 认识到"这里没有 feature map"就应当**立刻拉 architect 去建**；feature map 建成后是一张**可以被查的表**（A2 的调研可以直接查它）。现行登记把它绑死在 P1，且不给 P0 消费权。

### 3.4 adversary 与 verifier 的重合没有被推演过

- adversary **必须自己跑一遍 `A6.runnable`**（`roles/adversary.md:69`）；verifier 也要在真实目标上跑 ⇒ **"跑一遍"重叠**。
- 库里给的区分轴只有三条：对象（这一片候选 vs A3 里该验的能力）、产出（A7 三栏 vs A8 七栏+三态）、顺序（P5 吃 A7.conditions）。
- **没有**任何一条说"什么只在 P4 跑、什么只在 P5 跑"，**也没有去重规则**；
- 更危险：库里写了"验证者不得是候选的实现者"，但**没写"验证者不得是裁决者"**——同一会话既当 adversary 又当 verifier 目前是合法的。
- 重合度取决于 **A3 的粒度**，而库里**没有规定 A3 的粒度**。

### 3.5 ACK / 执行留痕目前**没有承载体**

- `roles/scribe.md:64`：「**不把台账当进度看板。它记的是判断，不是「我在做第几件事」。**」
- `skills/decision-ledger.md`：只记「决策点与检查点」，明说"琐碎步骤不记——记满了就没人读"。
- ⇒ "每个环节完成发 ACK、台账由 ACK 生成"这条路，库里是**明确否掉**的；而**执行留痕**这件事**没有任何承载体**。scribe 现在只有三件职责：A9 维护与只追加、`@context-reconstruction`、`@handoff`。

### 3.6 grill 三件套被合成了一个

`registry` 的处置表里有三条：`matt:grill-me → grilling`、`matt:grill-with-docs → grilling`、`matt:grilling → grilling`。
上游现状：**还有 `grill-with-docs`**，`grill-me` 已不在上游 skills 目录里。
Owner 的提醒：**这三个原来是"一组有内部关系的东西"**（追问的方法本体 / 追问并顺带产出 ADR / 纯追问），合并后"什么时候用哪一个"那层区别消失了。→ 这条归 investigator 查。

---

## 四、要 driver 做的三件事

### 1. 新建**推演 session**
- 模型：**`minimax-cn/MiniMax-M3.1-Flash-Preview`**，思考强度 **high**
  （注意：本机 `settings.json` 的默认是 `MiniMax-M3`，**必须显式指定**，例如
  `herdr agent start <名字> --kind pi --pane <pane> -- --provider minimax-cn --model MiniMax-M3.1-Flash-Preview --thinking high`）
- 任务：按第二节的**前提 + 三种形态 + 每件六问**，对 `A1`–`A9` 做逐件推演。
- 推演产物必须落盘、durable、可被下一轮读到。

### 2. 新建 **investigator**
- 模型同上（`minimax-cn/MiniMax-M3.1-Flash-Preview`）。
- 任务：沿"**计划/任务书 + 指针 + 谁写谁执行 + 台账/留痕 + 环境能力**"这条轴，把**三个上游仓再过一遍**——尤其 pstack（这次才发现 `skills/poteto-mode/playbooks/` 这条线，之前整条漏掉）；一定有别的漏的。
- 产出必须带锚点（文件:行号），空结果也要写。

### 3. driver 自己 push 这两条线并收口
- **先推演、再改**：不许先改再说；推演的结论要能逐条对上"哪个产物、哪个形态、哪一处要改"。
- 改库仍然要按既有纪律（不改真源以外的东西、不为变绿削弱检查、改完交 Owner）。

---

## 五、边界（保持既有纪律）

- 推演是推演，不是改库；改动要基于推演结果并交 Owner 裁。
- 三态只有 `PASS` / `FAIL` / `UNVERIFIED`；环境故障既不算 PASS，也不判成产品缺陷。
- 不许把未决事项当已决写进文档。
- **之前挂在 Owner 那里的七条裁定（①②③④⑤⑦⑨）仍在等**，不受本轮影响；但推演结果**可能改变它们的答案**——所以顺序上是"**先推演、后裁定**"。
