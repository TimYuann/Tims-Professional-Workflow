# DISPOSAL-BATCH1-INPROGRESS-0930 · 来源第一批处置 · Matt in-progress 九项

- **角色**：`scout`（`tpw-0930-scout-b`）· 补事实与候选处置，**正式裁定由独立方做**
- **裁定依据**：`docs/history/handoff/0930-oracle-SCOPE-DECISION.md` 第 2 节（`:18-25`，全文 54 行已读）
- **九项正文**：前一轮已读，引用在姊妹台账 `UPSTREAM-INVENTORY-0930.md:305-407`（§5.1–5.9）。
  **本轮先读那 9 节**；其中 `pr` 与 `loop-me` 的台账引用较薄，**已回读原文**补足。
- **本库侧重叠**：本轮实读 `skills/wayfinder.md`、`skills/technical-writing.md`、`skills/codebase-design.md`、
  `skills/task-breakdown.md`、`skills/handoff.md`、`AGENTS.md`、`workflow/registry.yaml`、`workflow/phases/P6.md`
- **本轮动作**：只读 + 新建本文件一个。**未改任何既有文件**，未 `git add` / `commit` / `tag`。`upstreams/` 只读
- **证据标记**：`[读到的]` / `[跑出来的]` / `[推断的]`

> **裁定第 2 节的程序要求**（`:23` 逐字）：
> `正式吸收或拒绝方法必须先读对应正文并由独立方评价`
> `[推断的]` **因此本文件的第 4 栏一律是「候选处置」，不是裁定。**
> 裁定同节 `:24` 另有一句直接约束本批：
> `实际方法内容未读而仅凭初判低直接拒绝，不允许` —— **本批九项全部已读正文，所以这一条不构成本批的阻拦理由。**

---

## 1. `retro`

**① 机制是什么**
对一次编码会话做复盘，产出的是**对 agent 环境的改进候选**，不是对代码的评价。原文 `SKILL.md:7` 逐字：
> `The user has asked for a **retrospective**. You are suggesting improvements to the coding agent's **environment** to improve future runs.`

最强的一条子判据在 `:19` 逐字：
> `Classify the violation first: a **mechanical** one (a fixed syntactic pattern, a banned API, an import shape, a file-location rule) gets a deterministic check, full stop... Default to building the check over writing the rule. Reserve \`CODING_STANDARDS.md\` for genuine **judgement calls** (cross-file consistency, "matches the surrounding style," anything no guardrail could ever substitute for).`

**② 与本库重叠在哪里**
- `[读到的]` **重叠（强）**：`AGENTS.md`「新增检查的保留判据」四条 —— 要能说清保护哪条**真实断言**、给会红的反例、说清合法变体为什么不误报、谁维护。`:19` 的「mechanical → 建确定性检查，judgement → 才写规则文本」与它是**同一分工的两面**。
- `[读到的]` **重叠（中）**：`AGENTS.md:91` 硬边界第 3 条 `不得为让检查变绿而削弱检查`。
- `[读到的]` **不重叠**：`retro:18` 的「本库有没有 guardrail」—— 本库有 `AGENTS.md` 的四条命令段（`AGENTS.md`「改动之后」节），**有**。
- `[跑出来的]` 本库全文 grep `CODING_STANDARDS` = **0 命中**；grep `guardrail` = **0 命中**。

**③ 它缺什么 —— 若吸收，本库会多出什么**
1. **七类候选清单本身**（`SKILL.md:17-23`：Navigation / Automated checks / Coding standards / Global AGENTS.md / Tool economy / No-ops / Information access）。本库**没有任何文件**承载这个分类。
2. **「mechanical vs judgement」这个切分动作**。本库有「新增检查的保留判据」，但**没有**回答「这次发现该写成检查还是写成规则文本」的前置分类。
3. **Global AGENTS.md 那一类**（`:23`）——本库的 `AGENTS.md` 有硬边界但**没有**「哪些指令该从 steering 文件搬进检查」这个动作。

**④ 候选处置**
**吸收（候选）**。理由：本批九项里它是**唯一一条直接对本库既有判据体系做元层改进**的机制，
且它要补的三样东西本库确认没有（`[跑出来的]` 两条 grep 全 0）。
不因为它在 `in-progress`（beta）就拒——`:19` 是一条完整、可判定、与本库同域的判据。

**⑤ 依据正文哪一句**
`:19`（`Default to building the check over writing the rule`）作为**为什么值得吸收**；
`:7`（`improvements to the coding agent's **environment**`）作为**为什么范围对得上**——
它改的是环境不是代码，与本库「纪律由本库定义、落点由下游裁定」同层。

---

## 2. `implement-spec`

**① 机制是什么**
按 spec + tickets 开工，出**一个分支一个 PR**；tickets 被当作**带阻塞关系的任务图**而不是步骤清单，
因此永远存在一个可抢的 frontier。原文 `SKILL.md:11` 逐字：
> `The tickets are not a list of steps. They are a **task graph** with blocking relationships between them. This means there is always a **frontier** of tickets which are ready to be grabbed.`

`:13` 逐字（子代理通信）：
> `Communication to and from subagents should be sparse. Communicate primarily through **context pointers**: to the spec, tickets, research notes, and previous commits. Don't duplicate information already available via pointers.`

**② 与本库重叠在哪里**
- `[跑出来的]` **重叠（强，且是本批最实的一条）**：本库 `skills/wayfinder.md:27` 逐字已经写着
  `**第二遍再连边。** 票先建、拿到标识之后再连依赖边。连完边，**前沿**（开放、无阻塞、无人认领的票）自然排出来。被阻塞的票照样写在地图上，只是不在前沿。`
  —— **frontier 这个机制本库已经有了，中文叫「前沿」，而且说得比上游更细**（多了「无人认领」与「雾不等于票」两层）。
- `[读到的]` 重叠：`skills/task-breakdown.md:41` 逐字 `\`edges\`：依赖边按拓扑序排好，并标明哪些是必须串行…哪些可并行`；`skills/swarm.md:16` `切片的边界与依赖边`。
- `[读到的]` 重叠：`AGENTS.md` 全局「跨 Harness 委托」一节讲「只放接手方需要的东西」，与 `:13` 的 context pointers 同向。

**③ 它缺什么 —— 若吸收，本库会多出什么**
1. **实现侧的 frontier 消费**：本库 `wayfinder:27` 的「前沿」是**规划时**的概念（哪些票可开）；`implement-spec:11` 是**执行时**的（哪些票现在抢）。本库 `skills/implement.md` 讲「知道自己取的是哪一片」，但**没有**「按依赖解锁下一批、并发拉满」这一步。
2. **每个 implementer 独立 worktree + 独立分支 + merger 子代理合并**（`:17-18`、`:23`）。`[跑出来的]` 本库 `roles/builder.md:82` 只提 `branch/worktree` 作为**写前核对项**，`skills/arena.md:21` 提「各自的工作副本／工作树」用于**多候选选优**——**都不是「一票一 worktree 并行推进」**。
3. **探索子代理与实现子代理分离，且探索笔记存仓外**（`:17-18` 理由是「让 implementer 专注实现」）。`[跑出来的]` 本库 grep `探索子` = 0、`exploration subagent` = 0。

**④ 候选处置**
**沿用已有（候选）——只对 frontier 一半；执行侧那一半另作候选**。
理由：frontier 机制本库 `wayfinder.md:27` **已经存在且更完整**，
吸收上游 `:11` 会造成同一概念两处设义——正是 `AGENTS.md`「原则正文只有一处」明令禁止的。
但 `:17-18` 的 **worktree 隔离 + merger 子代理 + 探索/实现分离**本库确实没有，**不该被「沿用已有」一并带走**。
`[推断的]` 建议 Driver 把这一项**拆成两个候选**再送独立评价，不要整条吸收或整条拒。

**⑤ 依据正文哪一句**
沿用已有的依据是 `wayfinder.md:27`（本库侧逐字，非上游）；
拆分的依据是 `SKILL.md:11` 的 `frontier of tickets which are ready to be grabbed`
与 `:23` 的 `Each implementer subagent should work in its own worktree, on its own branch`——
**这两句管的是不同的事，前者已有、后者没有。**

---

## 3. `claude-handoff`

**① 机制是什么**
把当前会话交接给一个**后台 agent**：不落盘，直接用交接摘要当 prompt 起进程。原文 `SKILL.md:7` 逐字：
> `Instead of saving it, launch a background agent seeded with the summary as its prompt: \`claude --bg --name "<descriptive name>" "<handoff summary>"\`.`

`:12` 逐字（摘要里必须有一段点名技能）：
> `Include a "suggested skills" section in the summary, naming which skills the next agent should call the Skill tool for.`

**② 与本库重叠在哪里**
- `[读到的]` 重叠（强）：`skills/handoff.md`（`[读到的]` 标题「移交简报」）**就是本库的交接技能**，
  触发条件逐字为「换会话／换人／中途转手」。
- `[读到的]` 重叠：`AGENTS.md` 全局「跨 Harness 委托」一节讲交接只放接手方需要的东西，与 `:14` 的不重复指令同向。

**③ 它缺什么 —— 若吸收，本库会多出一个什么**
**只有一个可迁移的增量**：`:12` 的 **「suggested skills」段** ——
交接摘要里**点名下一个 agent 该调哪几个 skill**。
`[跑出来的]` 本库 grep `suggested skills` = 0 命中；`skills/handoff.md` 没有这一项。
其余全是**工具特定**：`claude --bg --name` 是 Claude Code 的命令行形态，`claude agents` 是它的管理界面。
`AGENTS.md`「工具解耦」明写本库不出现具体底座名字。

**④ 候选处置**
**拒绝（候选）——但理由是工具特定，不是「beta」**。
`:7` 的机制本体（`claude --bg` + `claude agents`）是**某一底座的命令形态**，
吸收它会把底座名字写进本库技能正文，与本库「工具解耦」直接冲突。
`[推断的]` **但 `:12` 的「suggested skills」段是可迁移的**，
它不依赖任何底座。**建议 Driver 把 `:12` 单独作为一条方法候选**，
不要因为拒绝 `:7` 就把 `:12` 一起带走——这正是「不因为名字像就整条同处置」。

**⑤ 依据正文哪一句**
拒绝依据 = `SKILL.md:7` 的 `claude --bg --name ...` 与 `claude agents`（底座特定）。
`:12` 独立成候选的依据 = 同句 `naming which skills the next agent should call the Skill tool for`
——**这句里没有底座名**。

---

## 4. `writing-shape`

**① 机制是什么**
把一堆原始素材**定结构、逐段填**，产出独立成文文件。原文 `SKILL.md:7` 逐字：
> `This is **exploit**: the exploring is done, the pile is fixed: commit to a structure and mine the pile to fill it. Do not edit the raw material file: it is read-only to this skill.`

`:24` 与 `:25` 逐字（两块关键动作）：
> `> Pull material from the pile to answer. The next block may only lean on grounded concepts, and grounds new ones as it lands.`
> `> Argue about the form the next block takes: a paragraph, a list, a table, a callout, a quote, a code block. Each format choice should be deliberate and defensible.`

**② 与本库重叠在哪里**
- `[跑出来的]` **重叠（中）**：`skills/technical-writing.md`（`[读到的]` 标题「技术写作分层」）覆盖技术文档的四层写法。
  但**它管的是「文档属于哪一层」**（`technical-writing.md:17` 逐字 `这份文档属于哪一层`），**不管「一段一段生长时每个块依赖什么」**。
- `[跑出来的]` **不重叠（本库无）**：grep `grounding` = **0 命中**、`grounded` = **0 命中**。
  **本库没有「概念先落地才能被靠」这个机制。**
- `[跑出来的]` 不重叠：`块`/`段落形式可辩护` 这个动作，本库无。

**③ 它缺什么 —— 若吸收，本库会多出什么**
1. **grounding 机制**：每个块只能依赖已落地的概念，落地一个就更新一次清单（`:24`）。
   这是**可判定的**（能数出「本块引入了几个新概念」），本库完全没有。
2. **「先读完整个素材堆再动手」**（`:15` 逐字 `Read it end-to-end before doing anything else.`）——
   本库 `technical-writing.md` **没有**开工前的阅读面要求。
3. **块的形式要可辩护**（`:25`）——本库 `technical-writing.md:22` 有「先选层」，
   但那是**整篇选一层**，不是**每块选一种形式并论证**。

**④ 候选处置**
**吸收（候选）**。理由：grounding 是本批九条里**唯一一条完全新增的判据机制**（grep 双 0 命中），
而且它可判定、与本库「判据要可判定」的取向一致。
它与 `technical-writing` 是**互补不是重复**：前者管层，后者管块。

**⑤ 依据正文哪一句**
`:24` 的 `The next block may only lean on grounded concepts, and grounds new ones as it lands.`
——**这一句是机制本体，且在本库全文 0 命中**（`[跑出来的]`）。
`:15` 的 `Read it end-to-end before doing anything else.` 作为第二增量。

---

## 5. `loop-me`

**① 机制是什么**
用 grilling 逼出「循环／工作流」的规格，落成文件。原文 `SKILL.md:8` 逐字：
> `Run a stateful \`/grilling\` session whose only output is **workflow** specs.`

词表 `:20-23` 逐字：
> `- **Trigger**: what fires each run, an **event** (a new email, a new issue) or a **schedule** (every morning). Event-triggering is usually the more efficient.`
> `- **Checkpoint**: a human-in-the-loop point where the user is asked to verify or decide. Some workflows have none and run autonomously; some use no AI at all.`
> `- **Push right**: defer the checkpoint as far as it will go. Do maximal work before involving the human, so they are asked once, late, with everything prepared.`
> `- **Brief**: what a checkpoint presents, a tight, decision-ready summary (what was produced, why, and a link down to the asset itself), never the raw output.`

反结构约束 `:18` 逐字：
> `**Mandate nothing structural**: a workflow needs no AI, no checkpoint, and no schedule unless the grilling shows it does.`

完成判据 `:27` 逐字：
> `A workflow spec is done when an implementer agent could build it without asking a single question. Grill until then; nothing is done while a question remains.`

**② 与本库重叠在哪里**
- `[读到的]` 重叠：驱动方式是 `/grilling`，本库有 `skills/grilling.md`（`[读到的]` 标题「追问式对话」）。
- `[读到的]` **重叠（强）**：「完成判据 = 下一个 agent 不用问问题就能做完」
  与本库 driver 的 artifact 够格判据同形（`roles/driver.md`「缺则退回」节：
  `缺一项就退回整件，不「先收下再说」`）。
- `[跑出来的]` **不重叠**：grep `Checkpoint` = 0、`checkpoint` = 0、`Push right` = 0、`Brief` = 0、`brief` = 0 —— **四个词表项本库全部没有**。
- `[推断的]` 重叠但**方向不同**：`AGENTS.md` 硬边界第 2 条要求「可送达时 driver **有义务**提供一次可复制粘贴的独立复核启动 prompt，尽量降低 Owner 转发成本」——
  这与 `:22` 的 `Push right`（把人工介入点尽量往后推、让人只被问一次、且准备好）**形态相近但对象不同**：
  一个是**单次 gate**，一个是**循环里反复出现的 checkpoint**。**不是同一条。**

**③ 它缺什么 —— 若吸收，本库会多出什么**
1. **四词表**（Trigger / Checkpoint / Push right / Brief）——本库 0 命中，是一整套可复用的规格词汇。
2. **「事件优先于定时」**（`:20` 末句 `Event-triggering is usually the more efficient.`）——本库无。
3. **「不强加结构」这条反约束**（`:18`）——本库 `AGENTS.md` 有硬边界但没有「先证明这个 workflow 需要 AI/需要 checkpoint/需要 schedule」的门槛。
4. **「Brief ≠ 原始输出」**（`:23`）——`[推断的]` 本库 `roles/driver.md` 收 packet 时讲过「结构化 handoff」，
   但**没有**一条说「给人看的那份必须是 decision-ready 摘要而不是原始产物」。

**④ 候选处置**
**吸收（候选），但按词表逐项送评，不整条吸收**。理由：四词表是本批**词表型增量**，
grep 四项全 0 说明本库确实没有；但 `:18` 的「不强加结构」是**方法论主张**，
它与本库「纪律由本库定义」的取向**可能冲突**（本库倾向于规定而非不强加）。
`[推断的]` 建议 Driver 把 `:20-23` 词表与 `:18` 反约束**分成两个候选**——
前者是中性词汇，后者是需要独立评价的方法论主张。

**⑤ 依据正文哪一句**
吸收词表的依据 = `:20-23` 四句逐字（本库 grep 四项全 0）。
`:18` 单列候选的依据 = `**Mandate nothing structural**` 这一句本身，
以及它与本库取向的**张力**——`[推断的]` 这个张力必须由独立方判，**我不判**。

---

## 6. `setup-ts-deep-modules`

**① 机制是什么**
把 TypeScript 仓的每个 package 变成**深模块**，并装上能把规则变成红线的工具。原文 `SKILL.md:9` 逐字：
> `Make every package in this repo a **deep module**: a lot of behaviour behind a small interface. A package's public surface is its **entry points** (the files at the package root), and everything in its subfolders is hidden.`

`:11` 逐字（明确要求复用另一条 skill 的词表）：
> `For the vocabulary (deep module, interface, seam, depth), call the Skill tool with "codebase-design" and use its language throughout.`

`:29` 逐字：
> `**Entry points, not a barrel.** Because the public surface is *every* root file, a package can expose several small entry points (\`index.ts\`, \`client.ts\`, \`server.ts\`) instead of funnelling everything through one giant \`index.ts\`.`

**② 与本库重叠在哪里**
- `[读到的]` **重叠（强）**：本库 `skills/codebase-design.md` 已有完整深模块词表，
  `:46-47` 逐字 `**深与浅**` / `深模块：小接口 + 厚实现。浅模块：大接口 + 薄实现——通常是层层转发。`
- `[读到的]` 更强的重叠：上游 `:11` **自己就说**「词表请用 codebase-design」——
  `[推断的]` **也就是说这一条自己承认词表部分不是它的增量**。
- `[跑出来的]` **不重叠**：`skills/codebase-design.md:52-59` 的四条判据里
  有一条是 `**接口就是测试面。** 调用方和测试走同一个接缝。想越过接口去测内部，多半是模块形状不对。`
  ——**这条与上游 `:25` 的「tests through the entry points」同源**，但本库是**原则表述**、上游是**工具规则**。
- `[跑出来的]` 不重叠：`entry point` = 0、`deep module`（英文）= 0（本库用中文「深模块」，11 命中）。

**③ 它缺什么 —— 若吸收，本库会多出什么**
**唯一增量是「可执行形态」**：dependency-cruiser 的配置 + 四条 `error` 级规则
（entry-point boundary / intra-package freedom / tests through the entry points / no cycles）。
`[推断的]` 即：上游把本库 `codebase-design.md:52-59` 的四条**原则判据**落成了**会红的规则**。

`[推断的]` **但这里有一个必须由独立方判的边界问题**：
本库 `AGENTS.md:95-98` 硬边界第 6 条逐字
`6. **本库的 Driver 停在「逻辑编排层」。** … 它**不定义 execution mechanics**——进程、并发上限、WIP、队列、锁、重试、资源治理都属下游 runtime。`
dependency-cruiser 是**下游仓的构建期依赖**，不是本库 runtime。
**所以「这是方法还是机制」我不能替独立方答。**

**④ 候选处置**
**沿用已有（候选）——指词表与四条判据**；**同时把「可执行形态」单列为一个新候选，不并入沿用**。
理由：词表本库已有且更完整（上游自己都这么说）；
但「原则 → 会红的规则」这个转化动作本库**没有**，`[跑出来的]` `codebase-design.md` 通篇是判据、没有门禁。
`[推断的]` 收进本库时它会落成**给下游的参考材料**而不是本库自身的检查器——
这与本库「闸门是代码与配置，所以它是 `A6` 的一部分」一致，但**落点由 driver 按集合 B 裁定，不是我**。

**⑤ 依据正文哪一句**
沿用已有的依据 = `SKILL.md:11` 逐字 `call the Skill tool with "codebase-design" and use its language throughout`
（**上游自己指认了重叠**）。
单列候选的依据 = `SKILL.md:9` 的 `This skill installs dependency-cruiser and the rules that make the entry points the only way in, then proves the rules bite.`
——注意末句 `proves the rules bite`，这与本库 `verifier.md` 的「判别能力」要求同源，
是**这条最值得单独看的一句**。

---

## 7. `writing-fragments`

**① 机制是什么**
纯素材期：只挖碎片、**不定结构**。原文 `SKILL.md:7` 逐字：
> `This is pure **explore**: widen the space of what could be written without committing to structure. Committing is _exploit_, a separate skill's job. Run a grilling session that produces fragments, interviewing the user relentlessly about whatever they want to write about. Imposing phases, outlines, or article structure is out of scope here.`

fragment 的判据 `:26-28` 逐字：
> `It must be _readable by the author_ (the author can tell what it means), but it does not need to define its terms or be comprehensible to a cold reader. The bar is "is this a piece of good writing?", not "is this a self-contained argument?"`

**② 与本库重叠在哪里**
- `[跑出来的]` **重叠（中）**：`skills/grilling.md` 存在（`[读到的]` 标题「追问式对话」）——
  `:7` 说的 `Run a grilling session` 就是调它。
- `[跑出来的]` **不重叠**：`technical-writing.md` 全文是**四层分类**（教程/参考/说明/决策，`[读到的]` `:24-27`），
  **它假定文档已存在**，不处理「还没写、从哪挖」。
- `[跑出来的]` 不重叠：grep `fragments` = 0、grep `片段` = 4 但**全部是「代码片段」**（`skills/to-tickets.md:30`、`:47`、`skills/spec-driven-development.md:57`），
  **与写作素材无关**。

**③ 它缺什么 —— 若吸收，本库会多出什么**
1. **「素材期禁止提前定结构」这条纪律**。`[推断的]` 本库有近似纪律但对象不同：
   `AGENTS.md`「唯一真源」与 `to-tickets.md:47`（`票文本里不写具体文件路径和代码片段：它们很快过期`）
   都是**防止过早具体化**；`:7` 是**防止过早结构化**。**方向相反，本库没有后者。**
2. **fragment 的准入判据**（`:26-28`「作者读得懂即可，不需冷读者读得懂」）——这是一条**明确降低门槛**的判据，本库无同类。
3. **首次落盘格式约束**（`:15` 逐字 `On first write, put a single H1 at the top with a working title (it can change later) and nothing else: no metadata, no TOC, no date.`）——微小但可判定。

**④ 候选处置**
**吸收（候选）**。理由：它与 `writing-shape` **不重叠**（一个禁结构一个定结构），
且它补的「禁止过早结构化」在本库 grep 无同类。
但**必须与 `writing-beats` 一起看**——见下一项，两者共用 explore/exploit 二分。

**⑤ 依据正文哪一句**
`:7` 的 `Imposing phases, outlines, or article structure is out of scope here.`
——**这一句是本条的机制本体，且本库全文 0 命中**。
`:26-28` 的 `readable by the author` 作为第二增量。

---

## 8. `writing-beats`

**① 机制是什么**
同上素材，但**逐 beat 推进**成文。原文 `SKILL.md:9` 逐字：
> `The user has passed (or will pass) a markdown file of raw material. This is **exploit**: the exploring is done, the pile is fixed.`

`:33` 逐字（本条的判别性一句）：
> `The unit is the concept, not the word for it: a beat can lean on an idea the reader lacks even with no jargon in sight.`

`:39-40` 逐字：
> `So each beat does two jobs: it **requires** concepts that are already grounded, and it **grounds** new ones. Keep a running list of what's grounded so far, and update it each time a beat lands.`

**② 与本库重叠在哪里**
- `[跑出来的]` **重叠（强）**：`skills/technical-writing.md` 存在，覆盖技术文档四层。
- `[跑出来的]` **与 `writing-shape` 高度重复**：姊妹台账 `UPSTREAM-INVENTORY-0930.md:412` 已记
  `共用 explore-exploit 二分 + grounding 机制，正文措辞高度重复（\`writing-beats:33\` 与 \`writing-shape\` 的 Grounding 段落几乎同文）`。
  `[推断的]` 即 **grounding 机制在三条写作 skill 里出现两次以上**。
- `[跑出来的]` **不重叠**：grep `grounding` / `grounded` = **0 命中**（本库无）。

**③ 它缺什么 —— 若吸收，本库会多出什么**
**与第 4 项 `writing-shape` 是同一批增量**（grounding 机制 + 概念单元判据），
**本项独有的只有一处**：`:33` 的「**单位是概念，不是词**」——
`a beat can lean on an idea the reader lacks even with no jargon in sight`。
`[推断的]` 这一句比 `writing-shape` 的对应段落**更锋利**：它明确了 grounding 的**判别单位**，
避免了「术语都解释过了就算落地」这种伪落地。

**④ 候选处置**
**吸收（候选），但与第 4 项合并为一个候选送评，不拆成两条**。
理由：grounding 机制在两者中同文，拆开会出现同一机制两处设义
（本库 `AGENTS.md`「原则正文只有一处」明令禁止）。
**若吸收，本库多出来的应该是 grounding 机制本身（一次），加上 `:33` 的「概念为判别单位」这句强化。**

**⑤ 依据正文哪一句**
合并的依据 = `SKILL.md:39-40` 的 `requires concepts that are already grounded, and grounds new ones`
与 `writing-shape/SKILL.md:24` 的同义句**同文**。
本项独有的依据 = `SKILL.md:33` 的 `The unit is the concept, not the word for it`
——**这一句是本项相对 `writing-shape` 唯一的净增**。

---

## 9. `pr`

**① 机制是什么**
写 PR 正文的三段模板 + 每段的写法。原文 `SKILL.md:12-33` 逐字（模板本体）：

```markdown
## Summary

<diagram, diff-sketch, or tree>

## Evidence

- **Before:** <screenshot/output/failing test run>
  **After:** <screenshot/output/passing test run>

## Merge Danger

**Door:** <one-way or two-way>

<optional: description>

**Blast Radius:** <one-word description>

<optional: potential ramifications of merge>
```

`:37` 逐字：
> `Skip all preambles and keep prose brief. Use the user's domain language from \`CONTEXT.md\`.`

`:41` 逐字（Summary 的判据）：
> `Pick the smallest view that makes the key point clear.`

`:156-162` 逐字（Evidence 段的证据分级，本轮回读补入）：
> `Concrete evidence that the change works. Show a before and after.`
> `Screenshots are S-tier - when the environment is set up for it and the change is visual.`
> `Execution-based evidence is A-tier. Test results, console output. Show the exact test that now fails and passes, using pseudocode.`

`:164-168` 逐字（Merge Danger 段的两句解释，本轮回读补入）：
> `Describe whether it's a one-way or two-way door. You can walk back through two-way doors, but not one-way doors. A PR that is cheap to roll back is lower risk. Changes that involve destructive actions or hard-to-reverse decisions are one-way doors.`
> `The blast radius is the potential impact or scope of the changes introduced by this PR. Consider all possibilities. Examples are layout shift, breakages for consumers, mobile responsiveness, etc.`

**② 与本库重叠在哪里**
- `[跑出来的]` **重叠（中）**：`skills/git-workflow-and-versioning.md` 覆盖提交面；
  `skills/shipping-and-launch.md` 覆盖发布面。`[读到的]` `workflow/phases/P6.md:26` 有
  `verify: A9.result 记下了发布动作与回滚路径，且回滚路径已被确认可执行`——
  **「回滚路径」与上游模板的 `Merge Danger` 段是同一件事的两种说法**。
- `[跑出来的]` **不重叠**：`Blast Radius` = **0 命中**、`blast radius` = 0、`PR 正文` = 0、`pull request` = 0。
  **本库没有 PR 正文模板。**
- `[读到的]` 来源可追：frontmatter `:5-9` 逐字
  `skill: show-me` / `author: Dex Horthy` / `organisation: Humanlayer` / `url: "https://github.com/humanlayer/skills/blob/main/plugins/show-me/skills/show-me/SKILL.md"`。
  同目录另有 `upstreams/mattpocock-skills/skills/in-progress/pr/CREDITS.md`。

**③ 它缺什么 —— 若吸收，本库会多出什么**
1. **一份 PR 正文模板**（本库 0 命中）。`[推断的]` 具体增量是三段结构：
   `Summary`（用**最小视图**，可以是伪代码或调用树，见 `:43-51`）+
   `Evidence`（Before/After 成对）+ `Merge Danger`（`Door` 单向/双向 + `Blast Radius` 一词）。
   `[读到的]` `Summary` 段还给了六种视觉形态（伪代码 `:45-51`、调用树 `:55-60`、组件树 `:66`、
   文件树 `:72-78`、Mermaid 时序图 `:82-89`、diff `:91-131`、整块代码 `:135-137`），
   并在 `:152-154` 逐字 `Use your judgement and don't overwhelm the user.`。
2. **「Evidence 必须成对」的写法**——本库 `A8` 要求 `observation` 是外部观察，
   但**没有**要求它以 Before/After 对的形式出现在 PR 正文里。
3. **「Door：单向还是双向」这个提问**——本库 `skills/tier-sizing.md:53` 有
   `单向门（做错了退不回来）与大面积影响面升档`，**是同一概念的判断侧**；
   `:26` 的 `Door: <one-way or two-way>` 是**表达侧**。**本库有判断、无表达。**
4. **证据分级 S/A tier**（`:158`、`:162`）——截图 S 级、执行类证据（测试结果、控制台输出）A 级。
   `[推断的]` 本库 `A8.observation` 要求「跑出来的，不是推理出来的」，**要求真实性但不要求分级**。
   这是本条一个此前未记的净增。

**④ 候选处置**
**吸收（候选）——但只吸收「表达模板」，不吸收工具链**。
理由：模板本体无工具依赖（三段 Markdown），本库确认没有（grep 双 0）；
而 `[读到的]` `:37` 的 `Use the user's domain language from \`CONTEXT.md\``
引用的是**上游自己的 `CONTEXT.md`**，本库对应物不同，**这句不能直接搬**。
`[推断的]` **注意一个既有风险**（不是本条的否决理由）：
本库 `AGENTS.md` 硬边界第 5 条是 `\`A9\` 台账只追加。不修改、不删除既有行。`
——`:26` 的 `## Evidence` 与本库 A9 的 evidence 栏**不是同一栏**（一个是 PR 正文段落、一个是台账字段），
但两者都叫 evidence，**吸收时需要避免读者混读**。这一点值得独立方看一眼。

**⑤ 依据正文哪一句**
吸收依据 = `SKILL.md:24-32` 的 `## Merge Danger` / `**Door:** <one-way or two-way>` / `**Blast Radius:** <one-word description>`
——**`Blast Radius` 在本库全文 0 命中**（`[跑出来的]`），是本批最干净的一处净空位。
`[推断的]` 补充依据 = `:166` 的 `You can walk back through two-way doors, but not one-way doors. A PR that is cheap to roll back is lower risk.`
——**这句把「可回滚性 = 风险大小」写成了可陈述的规则**，本库有对应的判据（`tier-sizing.md:53`）但没有要求在 PR 里说出来。
不搬 `:37` 的依据 = 同句引用了上游自己的 `CONTEXT.md`。

---

## 10. 汇总（**仅索引，不替代上面九节**）

| # | 候选处置 | 净增的一句话 |
|---|---|---|
| 1 | **吸收** | mechanical vs judgement 的切分 + 七类候选清单 |
| 2 | **沿用已有（frontier）+ 拆出执行侧候选** | 一票一 worktree 并行、merger 子代理、探索/实现分离 |
| 3 | **拒绝（工具特定）+ `:12` 单列候选** | 交接摘要点名下一个 agent 该用哪些 skill |
| 4 | **吸收** | grounding 机制（块只能靠已落地概念） |
| 5 | **吸收词表 + `:18` 单列候选** | Trigger/Checkpoint/Push right/Brief 四词表 |
| 6 | **沿用已有（词表）+ 可执行形态单列候选** | 深模块四判据落成会红的门禁 |
| 7 | **吸收** | 素材期禁止提前定结构 |
| 8 | **吸收（与 4 合并为一个候选）** | grounding + 「单位是概念不是词」 |
| 9 | **吸收（只吸表达模板）** | PR 三段模板 + Door/Blast Radius |

`[推断的]` **九项里没有一项判「范围外」**。
`[推断的]` 九项分五类：**吸收 5**（1、4/8、5、7、9）、**沿用已有 + 拆分 2**（2、6）、
**拒绝 + 拆分 1**（3）、**单列候选 4 处**（2 的执行侧、3 的 `:12`、5 的 `:18`、6 的可执行形态）。
**没有任何一项因「同属 in-progress／是 beta」被整桶同处置。**

---

## 11. 纪律自证与空结果

- 只读 + 新建本文件一个。**未改任何既有文件**；`git status` 复核见汇报。
- `upstreams/` **只读**：本轮读了 9 份 `SKILL.md`（其中 `pr`、`loop-me` 因台账引用薄而回读全文）。
  **未写、未移动、未删除。**
- 未 `git add` / `commit` / `tag`。
- 每条事实给 `文件:行号` + 原文片段。
- 全文区分 `[读到的]` / `[跑出来的]` / `[推断的]`。

### 空结果 / UNVERIFIED

| 项 | 结果 |
|---|---|
| 判「范围外」的条目 | **0 项**（九项都落在本库工程工作流域内） |
| 「因为是 beta 所以拒」的条目 | **0 项**。第 3 项 `claude-handoff` 的拒绝理由是 `claude --bg` 底座特定，**不是 beta** |
| 「因为名字像就吸」的条目 | **0 项**。第 6 项 `setup-ts-deep-modules` 名字像新东西，判的是**沿用已有** |
| `pr/SKILL.md` 全文长度 | 169 行；`[读到的]` 本轮**读完 `:1-169` 全文**（`### Evidence` 起于 `:156`、`### Merge Danger` 起于 `:164`，文件以 `:168` 的 blast radius 句结束）。**无未读段** |
| 独立评价 | **本轮没有做**。`[读到的]` 裁定 `:23` `由独立方评价` —— 本文件是**候选**，不是裁定 |
| 九项在 `upstream_dispositions` 的登记 | `[推断的]` 上轮实测 9 项全部不在；**本轮未复核该数字**（不在本任务范围） |
