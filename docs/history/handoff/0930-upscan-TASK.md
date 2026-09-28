# 0930 轮 · 三仓重扫任务书（investigator）

仓库：`/Users/yuantian/Developer/tim-professional-workflow`
你的名字：`tpw-0930-upscan`
driver：`tpw-0929-driver`

## 硬边界

- **只读。** 你**一个字节都不许改**本库任何文件，也不许改 `upstreams/`（上游只读是本仓硬边界）。
- 产出只写 `.pi/derivation-0930/UPSTREAM-RESCAN.md`。
- **不许 `git commit`、不许 `git tag`。**
- **每个结论必须带 `仓/路径:行号` 锚点。**
- **空结果也要写。** 「这条线上什么都没有」是有效结论，**比编一个更有价值**。
  上一轮就是「没写正文就算吸收」栽的（`AGENTS.md` 改动纪律第 1 条：
  吸收的机制要**先读正文**；没读正文不算吸收）。

---

## 背景：为什么重扫

Owner 的判断：

> 这个项目的构建要拆成**消化、融合、构建、推演**。**推演肯定没做**，消化融合也有欠缺。

具体到「融合」这一环，就是**上游机制有没有被真正吸收**。审计会话已经查实一处漏得很彻底：

> **pstack** 的真身在 `skills/poteto-mode/playbooks/multi-phase-plan.md`——
> **之前整条 `playbooks/` 线漏掉了。**

**一条线漏掉，说明扫法有系统性缺陷，不是孤立疏漏。** 你要做的是**用更好的扫法重扫一遍三条线**，
找出还有哪些漏的。

---

## 一、五个扫描轴（Owner 指定）

沿这五条轴，把**三个上游仓**各过一遍：

1. **计划 / 任务书**（plan / ticket / task list）
2. **指针**（pointer / 引用 / 索引 / evidence 引用）
3. **谁写、谁执行**（谁产出、谁跑、谁批准才能跑）
4. **台账 / 留痕**（ledger / trace / ack / progress）
5. **环境能力**（capability / 运行时需要什么 / 缺了怎么办）

三个仓：`upstreams/` 下的实际目录（先自己 `ls` 确认真实路径，不要照抄我这里的说法）。

---

## 二、已查实的三仓真身（**基线，不是结论**）

下面这些是审计会话**已经查到的**。**它们的用途是让你校准扫法**——
**不是让你复述，也不是说只有这些**。Owner 明确说了「一定有别的漏的」。

### matt
- 计划/票：`.scratch/<feature>/issues/<NN>-<slug>.md`（一票一文件、blockers-first 编号）；或真实 tracker
- **谁写：人敲 `/to-tickets`**——上游原话大意是「agent 不会自己去够它」
- **发布门**：拿编号清单给 operator 过，上游原话大意是「Nothing reaches the tracker until you approve」
- **谁执行**：上游原话「running it (one session at a time, or a fleet) is your job, not the skill's」
- **票 = tracer bullet**（窄而完整穿过所有层）
- **尺寸约束 =「放进一个 fresh context window」**——理由是捡起它的是一个从没见过你 spec 的 session
- 票文本里**不写代码路径和代码片段**

### addy
- 计划文档 `tasks/plan.md` + 任务清单落 `tasks/todo.md` 或外部 tracker
- **「task list target 在这里定义一次，别处一律引用它」**
- 用 tracker 时 **plan 里保留有序索引 + 条目 ID/链接，不复制清单**

### pstack
- 计划：agent store 的 `docs/` 下（`skills/poteto-mode/playbooks/multi-phase-plan.md`，**这条线之前整条漏了**）
- **「You own the plan, not the code. The plan is a checklist an owner runs box by box
  and the operator audits from the evidence. The plan is the deliverable. Do not implement.」**
- 探索用 subagents **返回 file pointers，不许内联**
- **「One box is one unit of work. Every box names the evidence that checks it.
  Check a box only when its evidence exists: a file, a log line, a screenshot,
  a test run, or a SHA.」**
- 写完跑 `check-plan.mjs`
- **「Post the plan path and the script's output, then stop.
  Execution starts on the operator's explicit go.」**

---

## 三、你要重点回答的三个具体问题

### Q1. pstack 的 `playbooks/` 还有哪些？漏的不止 `multi-phase-plan.md` 吧？
`ls` 那个目录，**逐个打开读**。`multi-phase-plan.md` 说明了什么模式？
**是不是还有同模式的兄弟文件被漏了？** 把 `playbooks/` 整个目录的清单列出来，
标出每个「已被吸收 / 未吸收 / 不适用」。

### Q2. 「每个 box 必须带 evidence」这个结构，本库丢了吗？
本库的 `A5`（`cartographer` 产）现在**没有**「每个 box 带 evidence」的结构——这一点已查实。
**你要做的是**：在上游三家 + 你新扫到的地方里，**还有谁有类似结构**，
以及它们的 evidence 种类清单（文件/日志行/截图/测试/SHA 还有别的吗？）。
**同时查一件事**：本库的 `A6.runnable` 或别的字段，能不能承接这个结构而不新增字段。

### Q3. `grill` 三件套到底怎么合并的？
本库 `registry` 的处置表里有三条：`matt:grill-me → grilling`、
`matt:grill-with-docs → grilling`、`matt:grilling → grilling`。
**上游现状待你核实**：
- `grill-me` 现在还在上游 skills 目录里吗？
- `grill-with-docs` 还在吗？
- 三者原本的关系是什么（追问的方法本体 / 追问并顺带产出 ADR / 纯追问）？
- 合并成一条之后，**「什么时候用哪一个」那层关系去哪了**？

Owner 的判断是「这三个原来是一组有内部关系的东西，合并后那层区别消失了」。
**你要给出的是：这个区别能不能恢复，以及恢复它需要什么形态**（新增技能？判据？处置表加字段？）。

---

## 四、产出要求

`.pi/derivation-0930/UPSTREAM-RESCAN.md`：

1. **三个仓的真实目录结构**（先 `ls`，不照抄）
2. **五轴 × 三仓的扫描表**——每格：有什么 / 在哪（`仓/路径:行号`）/ 本库吸收了没有 / 判定依据
3. **Q1 / Q2 / Q3 逐条回答**
4. **新发现的漏**（不在上面基线里的）——这是本轮最有价值的部分
5. **扫不到 / 不存在 / 不适用**——**空结果单列一节，不要混进「已吸收」**
6. **一句话结论**：三条线上一共漏了几处，最严重的是哪一处

**判定「已吸收」的标准**（本仓 `AGENTS.md` 改动纪律第 1 条）：
**要能指出本库哪个文件哪一行承接了它。** 指不出来就是**没吸收**，
不要因为「意思差不多」就算吸收。
