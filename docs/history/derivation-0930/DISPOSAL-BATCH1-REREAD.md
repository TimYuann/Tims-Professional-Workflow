# DISPOSAL-BATCH1-REREAD-0930 · 来源第一批返工 · 十一份来源全文重读

- **角色**：`scout`（`tpw-0930-scout-b`）· 补事实与候选处置，**正式裁定由独立方做**
- **返工依据**：`docs/history/handoff/0930-oracle-BATCH1-CLARIFICATION.md`（24 行全文已读）
- **上一版**：`DISPOSAL-BATCH1-INPROGRESS.md` —— **不改，本轮是历史记录**。本文件取代其处置结论。
- **本轮动作**：只读 + 新建本文件一个。未 `git add` / `commit` / `tag`。`upstreams/` 只读
- **证据标记**：`[读到的]` / `[跑出来的]` / `[推断的]`

## 0. 本轮做了什么（对照裁定的返工理由）

裁定 `:21` 逐字：
> `验证摘录确实存在不等于确认摘录足以覆盖正式处置理由，不能仅凭短语命中率宣称整份来源已读/全部机制已审。可复用既有实际阅读证据，缺上下文的部分补读，不新增一种"转读即视为全面读过"的规则。`

`[读到的]` **本轮读了 11 份来源全文**（9 份 `SKILL.md` + 2 份 hooks `.md`），
**不是**台账 `UPSTREAM-INVENTORY-0930.md` §5.1-5.9 的引用。
台账**只在本轮读完全文后作对照**，且下述 §4 记录了**台账引用漏掉的内容**——
**这直接证明裁定那句「摘录不足以覆盖处置理由」是对的**。

`[读到的]` 上一版的实质错误，**不是措辞问题**：
`claude-handoff` 的「suggested skills 段」我上一版记成**本库净增**。
`[跑出来的]` 实测本库 `skills/handoff.md:24` 逐字已经有：
> `5. **点名下一轮该调用的技能。** 接手的人不该自己从头猜该用哪套方法；把这一步省掉，等于让新会话重复一遍选型的活。`

**我上一版那条候选是错的。** 详见 §4 第 1 项。

---

## 1. 版本上下文与阅读面

`[跑出来的]` **11 份全部不在 `upstreams.lock.yaml` 的 `skills:` 枚举内**（逐条实测）。
因此**没有文件级 pin**。按派工要求记 mtime + 行数 + md5，并标 UNVERIFIED。

| # | 来源 | 仓 pin（`upstreams.lock.yaml:repos`） | 文件 mtime | 行数 | md5 | 阅读面 |
|---|---|---|---|---|---|---|
| 1 | `mattpocock-skills/skills/in-progress/claude-handoff/SKILL.md` | `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`（2026-09-18） | 2026-09-26T15:56:44 | 18 | `b88da18f908930430d7b43acb90cbdf6` | **全文 1-18** |
| 2 | `…/implement-spec/SKILL.md` | 同上 | 2026-09-26T15:56:44 | 35 | `782bf02612a498cb3387e3a9ee83c70b` | **全文 1-35** |
| 3 | `…/loop-me/SKILL.md` | 同上 | 2026-09-26T15:56:44 | 32 | `a9f68eb8404593d84bbd2c77c68686d4` | **全文 1-32** |
| 4 | `…/pr/SKILL.md` | 同上 | 2026-09-26T15:56:44 | 168 | `6894ff148f67e127b13362724e1fb7d9` | **全文 1-168** |
| 5 | `…/retro/SKILL.md` | 同上 | 2026-09-26T15:56:44 | 44 | `b0b71961bb25ff49036193c53b126cb1` | **全文 1-44** |
| 6 | `…/setup-ts-deep-modules/SKILL.md` | 同上 | 2026-09-26T15:56:44 | 102 | `821d886372466c66bb46af2aa47eb00a` | **全文 1-102** |
| 7 | `…/writing-beats/SKILL.md` | 同上 | 2026-09-26T15:56:44 | 67 | `741e7809ed6a8357c2fc265ef2c731b7` | **全文 1-67** |
| 8 | `…/writing-fragments/SKILL.md` | 同上 | 2026-09-26T15:56:44 | 79 | `9ec2fec437eb0dce865e0e7bddb54e34` | **全文 1-79** |
| 9 | `…/writing-shape/SKILL.md` | 同上 | 2026-09-26T15:56:44 | 79 | `febe9192f89e476f6809e3c6ee640747` | **全文 1-79** |
| 10 | `addyosmani-agent-skills/hooks/SDD-CACHE.md` | `2686b620fc1fed2e8f60c704839c766b8594c6b6`（2026-09-25） | 2026-09-26T15:56:47 | 167 | `9751ce274869ce0b9632b497a42045b6` | **全文 1-167** |
| 11 | `addyosmani-agent-skills/hooks/SIMPLIFY-IGNORE.md` | 同上 | 2026-09-26T15:56:47 | 91 | `bb4172f6c0c62edb5b3a25b60d281c5c` | **全文 1-91** |

`[推断的]` **版本语义的限定（必须随处置一起传下去）**：
仓 pin 是 `upstreams.lock.yaml` 里**该仓最后一次同步的 commit**，
但这 11 个文件**都不在锁的枚举里**，所以**pin 只保证「我读的文件来自这次同步的仓状态」**，
**不保证「这个路径在那个 commit 上有内容」**——
`in-progress` 被 `scripts/_render-lock.py:27-28` 的 `SKIP_DIRS` 排除，hooks `.md` 不在 `skills/` 目录下。
**因此这 11 条的版本身份是 UNVERIFIED 的**：mtime 全部相同（`2026-09-26T15:56:44` / `15:56:47`），
说明是同一次批量落盘，**我无法据此证明它们对应上游某个可寻址版本**。

---

## 2. 逐项处置（**工具实现** 与 **可迁移方法** 分开）

> `[读到的]` 裁定 `:14` 逐字：`不等于这整项方法因工具名而范围外。`
> `[读到的]` 裁定 `:15` 逐字：`独立worktree／branch／merger subagent、最大并发、创建PR和清理动作是具体实现或授权动作，不能作为工具无关库的硬编码要求。`

### 2.1 `claude-handoff`（18 行全文）

**工具实现（不搬）**：`SKILL.md:8` 的 `claude --bg --name "<descriptive name>" "<handoff summary>"` 与 `the user manages it with \`claude agents\``；
`:10` 的 `Always pass \`-n\`/\`--name\``。
`[推断的]` 这些是 Claude Code 的命令行形态，吸收即违反本库 `README.md`「工具解耦」。

**可迁移方法**：
- `:12` `Include a "suggested skills" section in the summary, naming which skills the next agent should call the Skill tool for.`
- `:14` `Do not duplicate content already captured in other artifacts (specs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.`
- `:16` `Redact any sensitive information, such as API keys, passwords, or personally identifiable information, since the summary becomes the agent's prompt.`
- `:18` `If the user passed arguments, treat them as a description of what the next session will focus on and tailor the summary accordingly.`

**与本库重叠（逐条对 owner 文件）**：

| 上游 | 本库 owner | 逐字 |
|---|---|---|
| `:12` suggested skills | `skills/handoff.md:24` | `5. **点名下一轮该调用的技能。** 接手的人不该自己从头猜该用哪套方法；把这一步省掉，等于让新会话重复一遍选型的活。` **已存在** |
| `:14` 不重复 | `skills/handoff.md:22` | `3. **凡已在别处存在的，正文一律不复制，改成指路**。规格、计划、决策记录、变更记录、差异都各有其所在；简报里粘一份，等于造出第二个会漂移的副本，而它们迟早会不一致。` **已存在且更完整**（多列了具体载体） |
| `:16` 脱敏 | `skills/handoff.md:25` | `6. **脱敏**。密钥、口令、可识别的个人信息不落进简报。` **已存在** |
| `:18` 按参数定制 | `skills/handoff.md:20` | `1. **先定这份简报给谁、给下一轮做什么用**。用途决定详略…` **已存在（更一般）** |

`[跑出来的]` **全文级结论：四项可迁移方法全部已在本库 `skills/handoff.md` 存在。**

**候选处置：拒绝**（整条）。
**依据原文句子**：`:8` 的 `claude --bg --name` + `claude agents` 是**底座特定**；
而 `:12`/`:14`/`:16`/`:18` 四项**没有一条是净增**。
`[推断的]` 上一版把 `:12` 记成净增是**实测错误**，已在 §4 更正。

---

### 2.2 `implement-spec`（35 行全文）

**工具实现 / 授权动作（不搬）**：
`:23` `Create a branch, and a draft PR. The PR should be marked as 'closing' the spec issue and tickets.`；
`:25` `Each implementer subagent should work in its own worktree, on its own branch.`；
`:27` `merge its work to the PR branch with a **merger subagent**`；
`:15` 与 `:29` 的 `for **maximum concurrency**`；
`:33` `Mark the PR as ready for review.`；`:35` `Clean up all **implementer subagent** worktrees.`
`[读到的]` 裁定 `:15` 把这些列为「具体实现或授权动作」，**不能成为工具无关库的硬编码要求**。

**可迁移方法（裁定点名可评的两条）**：
- **A · 事实调查与实施的输入分离**：`:21` 逐字
  `2. (optional) Use an **exploration subagent** to conduct any exploration required by the tickets - relevant codebase files or external documentation. Ensure the exploration subagent can save files - it should save its markdown notes in a directory outside the repo, accessible by all future subagents. This lets **implementer subagents** focus on implementation rather than exploration.`
  `[推断的]` 可迁移的是**输入分离**（调查与实施读不同的东西）与**「笔记落仓外、所有后续子代理可读」**这一条；
  **不可迁移的是**「用 exploration subagent 这个角色名」与「目录在 repo 外」这个具体位置约定（那是实现）。
- **B · 固定候选与集中集成**：`:9` 逐字
  `The goal is a PR which implements the entire spec on a single branch.`
  `[推断的]` 可迁移的是**「这一轮只有一个集成目标，所有并行工作最终汇到它」**这个约束；
  不可迁移的是「PR」这个具体载体与 `:25`/`:27` 的分支合并动作。

**另两条可迁移方法**：
- `:11` `The tickets are not a list of steps. They are a **task graph** with blocking relationships between them. This means there is always a **frontier** of tickets which are ready to be grabbed.`
- `:13` `Communication to and from subagents should be sparse. Communicate primarily through **context pointers**: to the spec, tickets, research notes, and previous commits. Don't duplicate information already available via pointers.`

**沿用已有 —— 必须指出 owner 文件**（裁定 `:15` 硬要求）：

| 机制 | **现有 owner 文件与行** | 逐字 |
|---|---|---|
| frontier | **`skills/wayfinder.md:27`** | `5. **第二遍再连边。** 票先建、拿到标识之后再连依赖边。连完边，前沿（开放、无阻塞、无人认领的票）自然排出来。被阻塞的票照样写在地图上，只是不在前沿。` |
| 依赖边 | **`skills/task-breakdown.md:41`** | `- \`edges\`：依赖边按拓扑序排好，并标明哪些是必须串行（迁移、共享状态）、哪些可并行、哪些需要先冻结共享契约。` |
| context pointers 不重复 | `AGENTS.md` 全局「跨 Harness 委托」 | （本库已有同向纪律） |

`[跑出来的]` 本库 `wayfinder.md:27` 的前沿定义比上游 `:11` **多两个限定**：「无人认领」、以及 `:25` 的「雾不等于票」。

**候选处置**：
- `:11` frontier → **沿用已有，owner = `skills/wayfinder.md:27`**。**不另设一份。**
- `:13` context pointers → **沿用已有，owner = `AGENTS.md` 跨 Harness 委托节**。
- `:21` 调查/实施输入分离 → **吸收（候选）**。
- `:9` 固定候选与集中集成 → **吸收（候选）**。
- `:15`/`:23`/`:25`/`:27`/`:29`/`:33`/`:35` → **不搬**（实现或授权动作）。

**依据原文句子**：吸收 A 依 `:21` 末句 `This lets **implementer subagents** focus on implementation rather than exploration.`；
吸收 B 依 `:9` `The goal is a PR which implements the entire spec on a single branch.`

---

### 2.3 `loop-me`（32 行全文）

`[读到的]` 裁定 §1 已直接处理本项的误读，`:7-9` 逐字：
> `\`loop-me\` 的 \`## Vocabulary\` 里，"Mandate nothing structural"的紧接限定是：被设计的 workflow 不预设必须有 AI、checkpoint、schedule，除非访谈证明需要。`
> `这一节的对象是用户要设计的具体工作流，前一句还说词汇按工作流需要取用、不当检查清单。**不是"TIM 不得定义工程纪律"**，不能脱离后半句改写为 Owner 必须重新选择本库取向。`
> `TIM 可以采借其按真实需求设置人类检查点／触发方式的思路；AI、运行排程等执行细节仍由现场判断。`

`[读到的]` **我把上下文补齐了**——`:18` 完整逐字：
> `A shared language, reached for only when a workflow calls for it: never a checklist. **Mandate nothing structural**: a workflow needs no AI, no checkpoint, and no schedule unless the grilling shows it does.`

`[推断的]` **裁定 §1 成立**：`never a checklist` + `unless the grilling shows it does` 两句一起，
对象确实是**被设计的那个具体 workflow 的规格**，不是 TIM 自己的取向。
**我上一版把它列为「与本库取向可能有张力、需独立方判」，是把后半句丢了 —— 那是错的**（见 §4 第 2 项）。

**工具/位置特定（不搬）**：`:14` `Workflows live in \`workflows/*.md\` and are the source of truth.`；`:31`；`:32` 的 `NOTES.md` 约定。
`:8` 的 `/grilling` 指向另一条上游 skill，本库对应物是 `skills/grilling.md`。

**可迁移方法 —— 四词表**（`:20-23` 逐字）：
> `- **Trigger**: what fires each run, an **event** (a new email, a new issue) or a **schedule** (every morning). Event-triggering is usually the more efficient.`
> `- **Checkpoint**: a human-in-the-loop point where the user is asked to verify or decide. Some workflows have none and run autonomously; some use no AI at all.`
> `- **Push right**: defer the checkpoint as far as it will go. Do maximal work before involving the human, so they are asked once, late, with everything prepared.`
> `- **Brief**: what a checkpoint presents, a tight, decision-ready summary (what was produced, why, and a link down to the asset itself), never the raw output. The user reads a brief, not a draft. Speed of review is imperative.`

**完成判据**（`:27` 逐字）：
> `A workflow spec is done when an implementer agent could build it without asking a single question. Grill until then; nothing is done while a question remains.`

**与本库重叠**：`[跑出来的]` grep `Trigger` / `Checkpoint` / `Push right` / `Brief` 在 `skills/`、`roles/`、`AGENTS.md`、`docs/artifacts.md`、`workflow/registry.yaml` 中**四项全 0 命中**。
`[读到的]` 完成判据与 `roles/driver.md`「缺则退回」节同形（`缺一项就退回整件，不「先收下再说」`）。

**候选处置**：**吸收（候选）** —— 四词表 + 完成判据。
**不拆 `:18` 为独立候选**（上一版拆错了，裁定 §1 已裁定它不构成本库取向悬案）。
**依据原文句子**：`:20` 末句 `Event-triggering is usually the more efficient.` 是四词表里唯一一条**带优先级的建议**；
`:22` `**Push right**: defer the checkpoint as far as it will go. Do maximal work before involving the human, so they are asked once, late, with everything prepared.`
`[推断的]` `:22` 与本库 `AGENTS.md` 硬边界第 2 条形态相近（都是「把人工介入推到尽量靠后、只问一次、准备好」），
**但对象不同**：一个是循环里反复出现的 checkpoint，一个是单次 gate。**这个区分要在吸收时写清，否则会被读成重复。**

---

### 2.4 `pr`（168 行全文）

**工具特定（不搬）**：`:37` `Use the user's domain language from \`CONTEXT.md\`.`（引用上游自己的文件）。

**可迁移方法 —— 模板本体**（`:12-33` 逐字）：
> `Use this template for writing the PR body:` … `## Summary` / `## Evidence` `- **Before:** … **After:** …` / `## Merge Danger` `**Door:** <one-way or two-way>` `**Blast Radius:** <one-word description>`

**可迁移方法 —— 三段判据**：
- `:41` `Pick the smallest view that makes the key point clear.`（Summary 段判据）
- `:152-154` `Place each visual next to the short text it supports. Keep only the calls, files, props, states, and boundaries needed to answer the user's current question or the options to resolve the current discussion point.` / `You may use one of these, you may use several, it is unlikely you will use all of them. Use your judgement and don't overwhelm the user.`
- `:158` `Screenshots are S-tier - when the environment is set up for it and the change is visual.`
- `:162` `Execution-based evidence is A-tier. Test results, console output. Show the exact test that now fails and passes, using pseudocode.`
- `:166` `You can walk back through two-way doors, but not one-way doors. A PR that is cheap to roll back is lower risk.`
- `:168` `The blast radius is the potential impact or scope of the changes introduced by this PR. Consider all possibilities.`

**与本库重叠**：`[跑出来的]` grep `Blast` / `one-way` / `两向门` = **0 命中**；`单向门` = 2 命中，owner 是 `skills/tier-sizing.md:62`：
> `**风险与不确定都要往高处设**。单向门（做错了退不回来）与大面积影响面升档；可逆、低风险、判据现成的步骤降档。`

`[推断的]` **本库有「单向门」这个判断概念（tier-sizing），但没有「在 PR 里把它说出来」这个表达动作。**
`:166` 正是把 tier-sizing 的判断**翻译成 PR 正文一个词**（`Door: <one-way or two-way>`）——这是表达方法，不是重复概念。

**候选处置**：**吸收（候选）**，范围 = 模板三段 + `:41` + `:166` 的 Door/Blast Radius + `:158`/`:162` 的证据分级。
**不搬** `:37`。
**依据原文句子**：`:166` 的 `A PR that is cheap to roll back is lower risk.`

---

### 2.5 `retro`（44 行全文）

**可迁移方法 —— 七类候选**（`:17-23` 逐字，每条都带 `_Use when_` 条件）：

| 行 | 类 | `_Use when_` 条件（本轮全文才读到） |
|---|---|---|
| `:17` | Navigation | `_Use when_ the session took a long time to find a piece of information.` |
| `:18` | Automated checks | `_Use when_ the agent made a mistake an automated check could have caught, or the repo has no guardrail at all.` |
| `:19` | Coding standards | `_Use when_ the reviewer agent failed to catch a mistake.` |
| `:20` | Global AGENTS.md | `_Use when_ the AGENTS.md file is particularly large - in the repo OR the user's global scope.` |
| `:21` | Tool economy | `_Use when_ the agent made an expensive tool call.` |
| `:22` | No-ops | `_Use when_ the steering files are large and unwieldy.` |
| `:23` | Information access | `_Use when_ a crucial piece of information was not available to the agent.` |

**可迁移方法 —— `## Reference` 节**（`:27-44`，**台账引用完全没记这一节**）：
- `:31` `The implementation agent has the most **context pressure**. They are responsible for exploration, writing code, and debugging failures.`
- `:33` `The review agent has the least context pressure - it receives a diff, so no exploration needed.`
- `:35` `This means that the review agent should be responsible for imposing coding standards, not the implementation agent.`
- `:41` `\`CLAUDE.md\`/\`AGENTS.md\`: these files are pushed to the context window of any agent working in this repo. They should be used incredibly sparingly, usually only for **navigation pointers** to other files.`
- `:42` `\`CODING_STANDARDS.md\`: this file is read during review, not implementation.`

**可迁移方法 —— 最硬的一条**（`:19`）：
> `Classify the violation first: a **mechanical** one (a fixed syntactic pattern, a banned API, an import shape, a file-location rule) gets a deterministic check, full stop… Default to building the check over writing the rule. Reserve \`CODING_STANDARDS.md\` for genuine **judgement calls** (cross-file consistency, "matches the surrounding style," anything no guardrail could ever substitute for).`

**与本库重叠**：`[跑出来的]` grep `上下文压力` / `context pressure` = **0 命中**；
grep `CODING_STANDARDS` = 0；grep `guardrail` = 0。
`[读到的]` 本库有同向但不同的机制：`roles/verifier.md:22-23`
> `**新建或实质修改的验证机制，在首次被用来支持 PASS 之前，必须证明它具有判别能力。** 可接受的证明包括 negative control、mutation、已知坏 baseline、明确反实现，或其他能观察到「错误对象会红」的方法`

`[推断的]` **本库 `verifier.md:23` 的「negative control / mutation / 已知坏 baseline」与 retro `:19` 的
「mechanical 就建确定性检查、judgement 才写规则文本」是同族但不同层的两件事**：
前者管**一次验证机制自己的资格**，后者管**发现该写进代码还是写进规则文本**。**不重复。**

**候选处置**：**吸收（候选）**，范围 = 七类候选（含各自 `_Use when_`）+ `## Reference` 节的 context pressure 归属 + `:19` 的 mechanical/judgement 切分。
**依据原文句子**：`:19` 的 `Default to building the check over writing the rule.`

---

### 2.6 `setup-ts-deep-modules`（102 行全文）

**工具实现（不搬）** —— 裁定 `:14` 逐字点名不搬的三样：
- dependency-cruiser 的**安装**：`:47-51`（`### 2. Install dependency-cruiser` / `Install \`dependency-cruiser\` as a devDependency with the detected package manager.`）
- **具体配置**：`:55` `Copy [\`dependency-cruiser.config.cjs\`](./dependency-cruiser.config.cjs) to the repo root as \`.dependency-cruiser.cjs\`. Set \`PACKAGES_ROOT\` to the root detected in step 1.`
- **TS 目录形状**：`:15-22` 的 `src/packages/<name>/index.ts|client.ts|lib/|tests/` 与 `:24` 的 `By convention implementation lives in \`lib/\` and tests in \`tests/\``
  （但注意 `:24` 末句 `The rule itself is general, though: *anything* in *any* subfolder is private, so you never extend the config to add a folder.` —— **这句是方法，不依赖固定目录名**）
- 另：`:41` 包管理器探测、`:61-65` `lint:boundaries` 接线、`:99-102` 的 `$1` back-reference 与 `.cjs` 技巧。

**可迁移方法（裁定 `:14` 逐字点名「是方法」的三样）**：
1. **公共入口 / 隐藏实现**：`:24` 逐字
   `The public surface is the package's **root files**, not one designated \`index.ts\`. By convention implementation lives in \`lib/\` and tests in \`tests/\`, giving every package the same two-folder shape. The rule itself is general, though: *anything* in *any* subfolder is private, so you never extend the config to add a folder.`
   与 `:28` `**Entry-point boundary**: code outside a package (app code or another package) may import only that package's entry points (its root files), never anything in its subfolders.`
2. **测试只经公共接口**：`:30` 逐字
   `3. **Tests through the entry points**: files under \`<pkg>/tests/\` may import any package's entry points and their own \`tests/\` fixtures, but never any package's subfolder internals (not even their own). Integration tests across packages are fine; deep imports are not.`
3. **边界检查 pass → 故意违规 fail → 恢复 pass** —— `:79-87` 逐字
   `### 6. Prove the rules bite` / `This is the completion criterion for the whole skill: a config that doesn't fail on a violation is worthless.` /
   `1. Run \`lint:boundaries\`. It must **pass** on the clean example.` /
   `2. Temporarily add a deep import to \`tests/example.test.ts\`… Run \`lint:boundaries\` again; it must **fail** with \`tests-through-entrypoints\`.` /
   `3. Revert the deep import. Run once more, and it must **pass**.` /
   `**Done when:** you have observed a pass, then a fail on the deep import, then a pass again.`

**另两条方法**：
- `:33` `**Entry points, not a barrel.** Because the public surface is *every* root file, a package can expose several small entry points (\`index.ts\`, \`client.ts\`, \`server.ts\`) instead of funnelling everything through one giant \`index.ts\`.`
- `:35` `Layering (which packages may depend on which) is a *different* concern and is left as a commented stub in the config for this repo to fill in.`
- `:93` `add a **context pointer** to it from the repo's agent-instructions file… This is what makes an agent discover the boundary rule instead of tripping over it.`

**与本库重叠（owner 文件）**：
`[读到的]` `skills/codebase-design.md:57-58` 逐字
> `3. **接口就是测试面。** 调用方和测试走同一个接缝。想越过接口去测内部，多半是模块形状不对。`

`[推断的]` **本库 `codebase-design.md:57` 已经就是「测试只经公共接口」这条方法**（原则形态）。
上游 `:30` 是它的**工具规则形态**。**这是同一方法两种形态，不应两处设义** ——
但**第 3 样（pass→fail→pass）本库没有对等物**：
`[跑出来的]` grep `故意违规` / `让检查变红` / `负例` = **0 命中`；
`roles/verifier.md:23` 有 `negative control、mutation、已知坏 baseline`
—— `[推断的]` **那是「验证机制自己的资格证明」，本项是「一条架构门禁自己必须被证明会红」**。
**两者是不同对象**：前者验「我这次跑的验证可不可信」，后者验「仓库里那道长期门禁是不是摆设」。
**本库 `AGENTS.md`「新增检查的保留判据」要求给一个会红的反例，但那是**提出检查时的设计要求**，
不是**检查建好后的验收动作**。**这处是本项最值得独立方看的净增。**

**候选处置**：
- 公共入口/隐藏实现 → **沿用已有**，owner = `skills/codebase-design.md`（`:46-59` 四条判据）。
- 测试只经公共接口 → **沿用已有**，owner = `skills/codebase-design.md:57`。
- **pass → 故意违规 fail → 恢复 pass → 吸收（候选）**。
- Entry points not a barrel（`:33`）→ **吸收（候选）**，本库 `codebase-design.md` 无对应。
- dependency-cruiser 安装/配置/TS 目录形状/接线技巧 → **不搬**。
`[读到的]` **裁定 `:13` 纠正了我上一版的误读**：
> `AGENTS 硬边界第6条没有"构建期依赖"的逐字排除，禁止的是本库 Driver 定义进程、并发上限、WIP、队列、锁、重试、资源治理等下游 runtime mechanics。`
`[推断的]` 即：我上一版用「硬边界第 6 条」当拒整项的理由是**引用错了条款范围**。已按裁定更正。

**依据原文句子**：`:81` `a config that doesn't fail on a violation is worthless.`

---

### 2.7 `writing-fragments`（79 行全文）

**工具/位置特定（不搬）**：`:13` `If the user did not pass a path, ask once where to save the document, then remember it for the rest of the session.`；
`:44-67` 的文件格式样例；`:69` `Fragments are separated by a horizontal rule (\`\n---\n\`). No headings inside the body. No tags.`

**可迁移方法 ——**（**其中 `:36-38` 台账引用完全没有**）：
1. **素材期禁结构**（`:9`）：
   `This is pure **explore**: widen the space of what could be written without committing to structure. Committing is _exploit_, a separate skill's job. Run a grilling session that produces fragments, interviewing the user relentlessly about whatever they want to write about. Imposing phases, outlines, or article structure is out of scope here.`
2. **fragment 的准入判据**（`:25`）：
   `A fragment is any piece of text that might survive into the final article. It must be _readable by the author_ (the author can tell what it means), but it does not need to define its terms or be comprehensible to a cold reader. The bar is "is this a piece of good writing?", not "is this a self-contained argument?"`
3. **leading word 机制**（`:36-38`，**本轮全文才发现**）：
   `- A **leading word**: a compact metaphor or coinage the whole piece can hang on (one term that names the idea, the way _tracer bullets_ or _fog of war_ names a whole pattern).`
   `Of these, the leading word is the most valuable fragment to land. It is load-bearing: name the right one in explore and it shapes the structure, the transitions, and the title later, paying dividends through the entire exploit phase. When the conversation circles a recurring idea, push to coin a word for it.`
4. **先捕获不筛选**（`:15`）：`Capture fragments from the very first thing the user says, including the initial prompt.`
5. **写前重读、只追加**（`:75`）：`Before every write: re-read the file from disk. The user may have edited, reordered, or deleted fragments between turns, so preserve their changes. Never overwrite the file; only append`
6. **用户的编辑指令是一等指令**（`:77`）：`The user can say "cut the last one", "rewrite that one sharper", "merge those two" at any time. Treat those as first-class instructions.`

**与本库重叠**：`[跑出来的]` grep `leading word` = **0 命中**；grep `grounding` = 0；
`[读到的]` `skills/technical-writing.md:9-11` 覆盖「要写或改任何一份给人读的文档」，但**假定文档已存在**，不处理素材期。

**候选处置**：**吸收（候选）**，范围 = 上述 6 条。
**依据原文句子**：`:38` 的 `It is load-bearing: name the right one in explore and it shapes the structure, the transitions, and the title later`
——**这一整条机制在台账引用里不存在，是本轮全文重读的净收获。**

---

### 2.8 `writing-beats`（67 行全文）

**工具特定（不搬）**：`:11` 存档路径询问；`:13` 的 `choose-your-own-adventure style` 交互形态。

**可迁移方法**：
1. **grounding**（`:27`、`:34`）：
   `:27` `Every **concept** has to be **grounded** before a beat can lean on it: the audience either walked in knowing it or met it in an earlier beat. A beat that reaches for an ungrounded concept loses the reader; that is the one move the journey can't make. The unit is the concept, not the word for it: a beat can lean on an idea the reader lacks even with no jargon in sight.`
   `:34` `So each beat does two jobs: it **requires** concepts that are already grounded, and it **grounds** new ones. Keep a running list of what's grounded so far, and update it each time a beat lands.`
2. **grounding 决定可达性**（`:36`，**本轮全文才读到**）：
   `This is what shapes the choose-your-own-adventure. A candidate beat is only reachable if everything it requires is already grounded; picking a beat that grounds concept X unlocks every beat that was waiting on X. When you offer next beats, they must all be reachable from the current grounded set, and say what each one grounds, so the user can see which paths it opens.`
3. **beat 的粒度判据**（`:50`，**本轮全文才读到**）：
   `If a "beat" needs five paragraphs and three subheadings, it's not a beat; it's two beats glued together. Split it.`
4. **前置/内埋的杠杆**（`:38`）：
   `The big lever is what you make a prerequisite versus what you ground inside the piece. Demand too much up front and you shut out readers who don't have it; ground too much inside and the early beats drown in definitions.`
5. **结束不由素材堆决定**（`:58`）：
   `The article ends when the journey is complete, not when the pile is empty. Most piles will have leftover fragments that don't make it in. That is fine; that is the point of having more raw material than you need.`

**候选处置**：**与 §2.9 合并为一个候选**（grounding 同文，见下），本项独有 3 条。
**依据原文句子**：`:50` 的 `it's two beats glued together. Split it.`（粒度判据，本项独有）

---

### 2.9 `writing-shape`（79 行全文）

**工具/位置特定（不搬）**：`:13` 存档路径；`:15`、`:75-77` 的 `<what-to-do>` / `<supporting-info>` / `## Out of scope` 标签结构。

**可迁移方法**：
1. **先读完整堆**（`:9`）：`Read it end-to-end before doing anything else.`
2. **grounding**（`:30`、`:37`）：
   `:30` 与 `writing-beats:27` **同文**（`The unit is the concept, not the word for it…`）。
   `:37` 独有：`When you ask "what does the reader need to hear next?", an ungrounded concept the next move needs is itself the answer: ground it first (here or in an earlier block) or you can't make the move. This is the gap-naming of [Pulling from the pile](#pulling-from-the-pile) one level up: there the pile is missing material; here the article is missing a foundation.`
3. **素材缺口要显式命名**（`:57`）：
   `If the pile lacks something the article needs, name the gap explicitly: "We need an example here and the pile doesn't have one. Give me one now or we cut this section."`
4. **块的形式权衡要出声**（`:61`、`:63-67` 五组 tradeoffs）：
   `When choosing how to render a block, weigh these tradeoffs out loud with the user, not silently:`
5. **不写回素材堆**（`:11`）：`Do not edit the raw material file: it is read-only to this skill.`
6. **弱过渡要砍**（`:43`、`:47-51` 五个具体追问）：
   `Push back. Refuse to let weak transitions slide. If a paragraph doesn't earn its place, cut it.`

**与本库重叠**：`[跑出来的]` grep `grounding` / `grounded` = **0 命中**；
`[读到的]` `skills/technical-writing.md` 覆盖四层写法，**不覆盖逐块生长**。

**候选处置**：**与 §2.8 合并为一个 grounding 候选**；本项独有 `:37`（缺口命名）、`:57`、`:61-67`、`:43`、`:47-51` 各自可评。
**依据原文句子**：`:37` 的 `ground it first (here or in an earlier block) or you can't make the move.`
`[推断的]` **合并理由**：`writing-beats:27` 与 `writing-shape:30` 逐字相同（grounding 定义），
拆成两条会造成同一机制两处设义 —— 违反本库 `AGENTS.md`「原则正文只有一处」。

---

### 2.10 `hooks/SDD-CACHE.md`（167 行全文）

**下游实现（不搬）** —— 裁定 `:14` 逐字：`隐藏代码、临时改写文件、hook 事件与缓存路径属于下游实现，不随方法一起硬编码到 TIM`：
- hook 事件与配置（`:13-47` 的 `PreToolUse` / `PostToolUse` JSON）
- `HEAD` + `If-None-Match` / `If-Modified-Since` 机制（`:9`、`:65-66`）
- 缓存键 `sha256(url)` 与存储路径 `.claude/sdd-cache/<sha>.json`（`:61`、`:72`）
- 脚本与依赖（`:162-167` `jq` / `curl` / `shasum`）
- 调试开关（`:139-152`）

**可迁移方法 —— 证据新鲜性纪律**：
1. `:9` 逐字
   `This hook caches fetched content on disk, but **revalidates with the origin server on every reuse** via HTTP \`If-None-Match\` / \`If-Modified-Since\`. Content is only served from cache when the server responds \`304 Not Modified\`, which is a fresh verification — not a memory read.`
2. `:71` 逐字 —— **本条最硬的一句**
   `Entries without an \`ETag\` or \`Last-Modified\` header are never cached — without a validator, the hook cannot verify freshness later, and caching would mean trusting memory.`
3. `:57` 逐字 —— **缓存体是「一次解读」不是「原文」**
   `The stored body is not raw HTML — \`WebFetch\` post-processes each response through a model using the caller's prompt, so what we cache is one agent's reading of the page. The key stays URL-only so reads reuse across sessions; the original prompt is kept as metadata and surfaced in the hit message so the next agent can tell whether the earlier reading fits.`
4. `:7` 逐字 —— **为什么本地记忆会与 skill 矛盾**
   `Caching the content as local memory would contradict the skill — docs change, and a stale cache hides that.`
5. `:156` 逐字（Known limitations）
   `**Body is prompt-shaped.** A hit returns the earlier agent's reading of the page, with the original prompt surfaced so the current agent can decide whether it applies.`
6. `:159` 逐字
   `**A misbehaving server can serve a wrong \`304\`.** That's a server bug to diagnose, not a cache invariant to defend against; we don't paper over it with a TTL.`

`[读到的]` 裁定 `:20` 已确认：M34 §3 **只批准单独处置粒度，不是吸收裁决**，本轮形成机制候选即可。

**候选处置**：**吸收（候选）** —— 上面 6 条，**全部是无工具依赖的判据**。
`[推断的]` **与本库的关系**：`skills/source-driven-development.md` 是本库对应的技能（`[读到的]` `SDD-CACHE.md:3` 自己指向 `../skills/source-driven-development/SKILL.md`）。
**本库没有对应的「证据新鲜性」判据** —— `[跑出来的]` grep `304` = 0。
**但要小心**：`:57` 与 `:156` 揭示的「304 不能证明旧解读满足当前问题」这一点，
是**对裁定 `:46` 那句的加强**，不是推翻 —— 裁定已经说了「源站 304 也不能证明旧解读满足当前问题」。
**候选应按这个加强版写，不是按原文的「304 = fresh verification」写。**

**依据原文句子**：`:71` `without a validator, the hook cannot verify freshness later, and caching would mean trusting memory.`

---

### 2.11 `hooks/SIMPLIFY-IGNORE.md`（91 行全文）

**下游实现（不搬）**：`:7-17` 的注释标注样例；`:19-43` 的 hook JSON；
`:55-57` 的三事件表（`PreToolUse Read` / `PostToolUse Edit|Write` / `Stop`）；`:59` 的内容哈希与项目级缓存；
`:71-79` 的崩溃恢复脚本；`:83-87` 的五条 Known limitations；`:91` 的依赖。

**可迁移方法 —— 约束与恢复路径的显式记录**：
1. **保护块带理由**（`:64-66` 逐字）
   `\`/* simplify-ignore-start */\`           // basic — hides the block` /
   `\`/* simplify-ignore-start: reason */\`   // with reason — appears in placeholder` /
   `\`/* simplify-ignore-end */\``
2. **占位符必须可判定地还原**（`:59` 逐字）
   `Each block is content-hashed (8 hex chars via \`shasum\`/\`sha1sum\`) so the round-trip is unambiguous even if the model duplicates or reorders placeholders.`
3. **崩溃恢复路径是规格的一部分**（`:73-79` 逐字）
   `If Claude Code crashes without triggering the Stop hook, files on disk may still have \`BLOCK_<hash>\` placeholders. To restore manually:` / `echo '{}' | bash hooks/simplify-ignore.sh` / `Backups are stored in \`.claude/.simplify-ignore-cache/\` within your project directory.`
4. **失败模式要逐条写、含降级**（`:86` 逐字）
   `**A wholesale rewrite falls back to the backup.** … the hook can no longer tell where the protected block belongs. At \`Stop\` it restores the backup and prints a warning; the rewrite is not lost but is kept in the cache as \`.claude/.simplify-ignore-cache/<id>.recovered\`, whose path the warning prints, and you merge it back by hand.`
5. **失败要可见、不静默**（`:85` 逐字）
   `A warning is printed to stderr when this happens.`

**与本库重叠**：`[跑出来的]` grep `保护块` = **0 命中**。
`[推断的]` 本库有「恢复路径」但语境不同 —— `roles/driver.md:73`、`:120` 的「通道恢复后随正常交接一并送达」讲的是**送达通道**，
不是**文件级改写的还原**。`workflow/phases/P6.md:26` 有 `verify: A9.result 记下了发布动作与回滚路径，且回滚路径已被确认可执行`
—— **本库有「回滚路径必须被确认可执行」这条判据**，但**没有「保护块/占位符/降级合并」这一层**。

**候选处置**：**吸收（候选）** —— 上面 5 条。
**依据原文句子**：`:86` 的 `the rewrite is not lost but is kept in the cache as … whose path the warning prints, and you merge it back by hand.`
`[推断的]` 这句的**方法内核是「失败时数据不丢、路径可见、由人合并」**，
而不是任何 hook 机制。**吸收时应写成这条，不写成「加一个 simplify-ignore hook」。**

---

## 3. 处置汇总（索引，不替代上面各节）

| # | 来源 | 工具实现（不搬） | 可迁移方法 | 候选处置 | owner 文件（如沿用） |
|---|---|---|---|---|---|
| 1 | `claude-handoff` | `claude --bg` / `claude agents` | 四项 | **拒绝** | 全部已在 `skills/handoff.md:22-25` |
| 2 | `implement-spec` | worktree/branch/merger/max-concurrency/PR/清理 | 调查-实施分离、集中集成、frontier、pointers | **沿用 2 + 吸收 2** | frontier → `skills/wayfinder.md:27`；edges → `skills/task-breakdown.md:41` |
| 3 | `loop-me` | `workflows/*.md` / `NOTES.md` | 四词表 + 完成判据 | **吸收** | — |
| 4 | `pr` | `CONTEXT.md` | 三段模板、Summary 判据、证据分级、Door/Blast | **吸收** | `单向门` 判断在 `skills/tier-sizing.md:62`（表达面无 owner） |
| 5 | `retro` | — | 七类含 `_Use when_`、context pressure、mechanical/judgement | **吸收** | — |
| 6 | `setup-ts-deep-modules` | 安装/配置/TS 目录形状/接线 | 入口-隐藏（沿用）、测试经接口（沿用）、**pass→fail→pass**、not-a-barrel | **沿用 2 + 吸收 2** | `skills/codebase-design.md:57` |
| 7 | `writing-fragments` | 路径/格式 | 禁结构、准入判据、**leading word**、先捕获、只追加 | **吸收** | — |
| 8 | `writing-beats` | 路径/交互 | grounding、**可达性**、**beat 粒度**、杠杆、结束判据 | **与 9 合并 + 独有 3 条** | — |
| 9 | `writing-shape` | 路径/标签结构 | grounding、**缺口命名**、形式权衡、弱过渡 | **与 8 合并 + 独有 5 条** | — |
| 10 | `hooks/SDD-CACHE.md` | hook 事件/304/缓存路径/依赖 | 证据新鲜性 6 条 | **吸收** | `skills/source-driven-development.md`（对应技能） |
| 11 | `hooks/SIMPLIFY-IGNORE.md` | 标注/hook/哈希/恢复脚本/限制 | 保护块带理由、可判定还原、恢复路径、失败可见 | **吸收** | — |

`[推断的]` **没有一项判「范围外」**。唯一的「拒绝」是 `claude-handoff`，理由是**四项方法全部已存在 + 机制体底座特定**。

---

## 4. 上一版被本轮推翻的结论（返工记录）

> `[读到的]` 裁定 `:21` 逐字：`不新增一种"转读即视为全面读过"的规则。`
> 本节记录**上一版（`DISPOSAL-BATCH1-INPROGRESS.md`）因读台账引用而非原文而产生的错误**。

| # | 上一版写的 | 本轮实测 | 性质 |
|---|---|---|---|
| 1 | `claude-handoff:12` 的「suggested skills」是**本库净增** | **错**。`skills/handoff.md:24` 逐字已有 `5. **点名下一轮该调用的技能。**` | **把已有当净增** |
| 2 | `loop-me:18`「Mandate nothing structural」与本库取向**可能有张力，需独立方判** | **错**。裁定 §1 已裁定它不是本库取向问题；我丢了 `:18` 前半句 `A shared language, reached for only when a workflow calls for it: never a checklist.` | **缺上下文导致过度设问** |
| 3 | `setup-ts-deep-modules` 用「AGENTS 硬边界第 6 条」当拒整项的理由 | **错**。裁定 `:13` 逐字：该条**没有**「构建期依赖」的排除，禁的是 runtime mechanics | **引用错条款范围** |
| 4 | `writing-fragments` 净增只有「禁结构」与「准入判据」 | **漏**。全文 `:36-38` 的 **leading word 机制**（`It is load-bearing…`）台账引用完全没有 | **漏读导致漏报** |
| 5 | `writing-beats` 净增只记 `:33`「单位是概念」 | **漏**。全文 `:36`（grounding 决定可达性）、`:50`（beat 粒度判据）、`:58`（结束不由素材堆决定） | **漏读导致漏报** |
| 6 | `writing-shape` 净增只记 grounding | **漏**。全文 `:37`（缺口命名）、`:57`、`:61-67`、`:43`、`:47-51` | **漏读导致漏报** |
| 7 | `retro` 净增只记七类清单 + mechanical/judgement | **漏**。全文 `## Reference` 节 `:27-44`（**context pressure 归属** `:31-35`、**AGENTS.md 稀用原则** `:41`） | **漏读导致漏报** |
| 8 | `implement-spec` 的 worktree/merger/并发「本库没有，可拆候选」 | **半错**。裁定 `:15` 逐字把这些定为「具体实现或授权动作，不能作为工具无关库的硬编码要求」——**不是待评候选** | **把实现当方法候选** |
| 9 | `pr` 与 `loop-me` 判为「已回读原文」 | 属实（上一轮确实读了这两份全文） | 不算错 |

`[推断的]` **第 4–7 项合计漏掉 4 处机制**，全部只在全文里。
**这是「摘录不足以覆盖处置理由」的直接证据**，支持裁定要求返工。

---

## 5. UNVERIFIED / 空结果

| 项 | 结果 |
|---|---|
| 11 份的文件级 pin | **UNVERIFIED** —— 全部不在 `upstreams.lock.yaml:skills` 枚举内，只有仓级 pin + mtime/行数/md5（见 §1） |
| 本轮读完全文的份数 | **11 / 11**（逐条行数已列） |
| 判「范围外」的项 | **0 项** |
| 判「拒绝」的项 | **1 项**（`claude-handoff`） |
| 沿用已有的项 | **3 处机制**（frontier、edges、测试经接口），**均已指出 owner 文件与行号** |
| 独立评价 | **本轮没做**。裁定 `:21` / `:20` 要求独立评价 —— 本文件是**候选** |
| 11 份在 `upstream_dispositions` 的登记 | 本轮**未复核**（上轮实测为 0，不在本轮范围） |
| `SDD-CACHE.md` 指向的 `../skills/source-driven-development/SKILL.md` | `[读到的]` 文件自身声明该路径存在；**本轮未读该文件**，故「本库已有对应技能」这一条**只依据上游自述**，标 **UNVERIFIED** |

## 6. 纪律自证

- 只读 + 新建 `docs/history/derivation-0930/DISPOSAL-BATCH1-REREAD.md` 一个。
- **未改任何既有文件**，包括上一版 `DISPOSAL-BATCH1-INPROGRESS.md`（历史记录保留）。
- `upstreams/` **只读**：本轮读了 11 个文件全文，未写、未移动、未删除。
- 未 `git add` / `commit` / `tag`。
- 每条事实给来源 `文件:行号` + 逐字片段。
- 全文区分 `[读到的]` / `[跑出来的]` / `[推断的]`。
- **工具实现与可迁移方法逐项分开**（§2 每项都有独立的两栏）。
- **沿用已有均指出 owner 文件**（`wayfinder.md:27`、`task-breakdown.md:41`、`codebase-design.md:57`、`handoff.md:22-25`、`tier-sizing.md:62`）。
