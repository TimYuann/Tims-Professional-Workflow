# TASK-3-B · feature map 的性质 / ideation 与 wayfinder / implement 之前的全景清单

**角色**：调查者 B（只读取证，不改任何产物；本文件是唯一写入物）。
**范围**：`.pi/investigation/TASK-3.md` 第二部分（T3-3、T3-4、T3-5）。T3-1/T3-2 不在本文件内。

| 取证对象 | 锁定值 | 工作区 |
|---|---|---|
| `upstreams/cursor-plugins`（pstack 0.15.5） | `ecc249f1e306fc64ddf83c7bed16cacf7c2239db` | 干净 |
| `upstreams/mattpocock-skills` | `c55ee46073ed923f86ce59a5eb3b6d895095d1b7` | 干净 |
| `upstreams/addyosmani-agent-skills` | `2686b620fc1fed2e8f60c704839c766b8594c6b6` | 干净 |
| 本仓 | 只读 | — |

**方法**：T3-5 先做**全量检索**（对三仓 `**/SKILL.md` 逐份抽 `name` + `description` 头，去 `third_party/` 后 **153 份**；再按关键词全仓 grep 复核），再按"是否属于 implement 之前"筛。每条给 `file:line` + 原文。外部来源标 URL，抓取日 2026-09-27。
**记号**：`[事实]` = 有原文可核；`[推断]` = 由原文推出并附推导链；`[外部]` = 非三仓。
**未覆盖**：三仓 `third_party/**`、`node_modules`、git 历史；`cursor-plugins` 里与 pstack 无关的其他插件（ralph-loop / teaching / grok-voice / create-plugin 等）只在 T3-5 附录里点名，不逐条展开。

---

# T3-3 · feature map 的消费者与性质

**取证方法**：`grep -rniE 'feature[ _-]map' --include='*.md' --include='*.json' --include='*.ts' --include='*.js' --include='*.toml' upstreams/cursor-plugins/` → **42 处命中，全部在 pstack 一仓**（matt / addy 各 0，逐仓复现见 T3-5-0）。逐条读过。下表所有结论只来自这 42 处。

## T3-3-1 读者 / 消费者：**主要读者是 agent，不是人**

| 消费者 | 原文锚点 | 它拿 map 做什么 |
|---|---|---|
| **下一个 agent（冷启动、任务中途读）** | `skills/create-verification-skill/SKILL.md:9`「You write the generator's output **for the next agent, not for a human**: it will be read **cold, mid-task**, by an agent that has never seen the app.」 | 无需与人对话就能驱动 app |
| 要驱动 app 的 agent | `references/feature-map-example/README.md:3`「**Read the index before driving the app**, then use the matching feature file **as the recipe**.」 | 索引 → 配方 |
| benny 复现自动化 | `automations/benny/skills/reproduce-and-fix-issues/SKILL.md:130`「Find the feature-map section that matches the reported user path. **Read it before driving the app.** If no section covers the feature, **mark the run blocked instead of inventing a path or selector.**」 | 定位 → 驱动；找不到就**阻断**，不许自创选择器 |
| control adapter（写驱动面的人） | `.../references/control-adapter.md:55`「Read the relevant feature-map section before driving the app.」；`:132`「Report **which feature-map sections it can drive and which are blocked**.」 | 能力清单 + 缺口清单 |
| 维护循环的并行 source reader | `skills/maintain-verification-skill/SKILL.md:29`「**One read-only subagent per feature file**, launched concurrently.」 | 工作单位 |
| `/swarm` 的切片单位 | `docs/guide/06-verify-and-ship.md:41`「a `/swarm` can split a full pass **by feature-map entry** and aggregate the results.」 | 并行切片 |
| **人** | **原文没有一处说"人读它"作为目的。** 人只出现在两个位置：① 被要求**填**用户自有的 map（`automations/benny/skills/setup-benny/SKILL.md:86`「**Fill one feature-map section** for every user-facing feature the automation may reproduce.」）；② 被**建议**去跑维护（`skills/create-verification-skill/SKILL.md:44`「Point the user at `/maintain-verification-skill`」） | 填 / 触发维护 |

`[事实]` **结论**：feature map 是 **agent-facing** 资产。唯一面向人的读取是 benny 那条"用户自己维护一份给自动化用"的变体，而它的读者仍然是 agent（`SKILL.md:128`「Read `references/control-adapter.md` and **the completed map** at `control.feature_map_path`, then invoke the skill named by `control.skill_name`.」）。

## T3-3-2 存在动机（原文的动机句）

- `skills/create-verification-skill/SKILL.md:9`「**Every serious project needs a scripted way to drive the real app and prove behavior**: launch it, exercise a feature the way a user would, and capture evidence.」
- `docs/guide/06-verify-and-ship.md:39`「From then on, "verify it in the app" is a step **any agent can execute, in this repo, with no setup conversation.**」
- `docs/guide/06-verify-and-ship.md:35`「The UI bullet above hides a real requirement. **The agent needs a scripted way to drive your app.** If your project has one, great. If not, run: `/create-verification-skill`」
- `skills/create-verification-skill/SKILL.md:36`「The map is the repo's **maintained verification source**; a proof that drives one convenient entry point is **incomplete** when the map lists others.」

`[事实]` **动机 = 把"证明行为正确"这件事从"每次会话重新搭建"变成"项目内一次建好、任何 agent 冷启动可用"。** 不是为了让人类读懂系统，也不是为了排期。

## T3-3-3 它读什么：**生成与维护都读代码；维护额外要求真机驱动**

| 阶段 | 读代码还是读人 | 原文 |
|---|---|---|
| 生成 | **读代码，不读人** | `skills/create-verification-skill/SKILL.md:11`「**Interview the repo, not the user**」；`:13`「Answer these **from the codebase** and only ask the user what you cannot observe」 |
| 生成（驱动面五问） | 从仓库事实回答 | `:15-19`──`Surface` / `Run` / `Drive` / `Observe` / `Isolate`；`:16`「Prefer **the repo's own documented dev command** (package scripts, Makefile, README quickstart)」 |
| 生成（功能来源） | 从路由/命令/菜单/文档抽 | `:36`「one file per user-facing feature you can identify (aim for the top 3-5 to start, **from routes, commands, menus, or docs**)」 |
| 维护 · source wave | 读代码 + 标记漂移 | `skills/maintain-verification-skill/SKILL.md:29`「Each explains "how does this user-facing feature work?" **from source**, flags likely doc drift with citations」 |
| 维护 · live pass | **必须真机跑，源码干净也不例外** | `:33`「**Live pass. Required even when source looks clean.** … Exercise every feature at least once」 |
| 维护 · 索引卫生 | 读 map 自身 | `:27`「Read the feature map README and glob its sibling files. Fix missing, extra, duplicate, or dead entries.」 |

`[事实]` **对 Owner 那句"如果它直接去读了代码"的回答**：是的，生成与维护**都以代码为主要信息源**，人只在代码答不上来时被问（`:13`）。

## T3-3-4 性质：**描述现状，不是规定应然**（但对"怎么算证明"有规范权）

**描述性证据（四条）**
1. `skills/maintain-verification-skill/SKILL.md:21`「a behavior **the map describes** that **the app no longer does** is either **doc drift (fix the map)** or **a product regression (report it, don't paper over it in docs)**.」
   → 冲突时**地图让位于 app**：要么改地图（漂移），要么把产品问题另行上报；**地图不许改写对产品的判断**。
2. `skills/maintain-verification-skill/SKILL.md:21`「**Never edit product code** during a run」— 维护循环对产品没有写权。
3. `automations/benny/skills/setup-benny/SKILL.md:86`「Keep it at the **user point of view**. **Do not freeze implementation details or current code paths in the map.**」
4. `.../references/feature-map.example.md:3`「Keep this map at the user point of view. **Discover internals and current code paths at runtime instead of freezing them here.**」；`references/feature-map-example/README.md:42`「**Keep implementation details out of the map.** Name only user paths, stable handles, required state, commands, and observable proof.」

**规范性证据（两条，只针对"证明"）**
- `skills/create-verification-skill/SKILL.md:36`「The map is **the repo's maintained verification source**; **a proof that drives one convenient entry point is incomplete** when the map lists others.」→ 在**"什么算证明完了"**上有规范权。
- `references/feature-map-example/README.md:23-31`（`Proof and skip reporting` 七条，含 `:31`「**Do not report a skipped entry point as verified through a different path.**」）与 `skills/create-verification-skill/SKILL.md:31`「Cleanup removes instances and scratch state, **never the evidence**: proof artifacts survive the teardown」→ 证据标准是硬规定。

`[事实]` **一句话性质**：它是**"现状的验收地图"**——记录**已经存在的用户可见行为**与**证明它的方法**；它对"该做什么"**没有**规范权，对"怎么证明过了"**有**规范权。

`[推断]` 由此推出一条对下游开发的直接后果：**它不能当任务来源**。map 里出现的一项若 app 已能正确执行，就没有任何事可做；benny 把它当配置前置（`SKILL.md:11`「If the config, required actions, control adapter, or **completed feature map is missing, fail closed**.」）时，用途仍是"给复现定位入口"，不是"生成开发任务"。

## T3-3-5 它对后续开发的作用（原文怎么被下游用）

| 下游用法 | 原文 |
|---|---|
| 并行验证的切片单位 | `docs/guide/06-verify-and-ship.md:41`；`skills/swarm/SKILL.md:23`（swarm 的分片形状由调用方声明） |
| 自动化的**失败关闭**前置 | `automations/benny/skills/reproduce-and-fix-issues/SKILL.md:11`；`FOR_AGENTS.md:35`「i want both automations to **fail closed** when channel coordinates, tracker access, the control adapter, or the feature map are **missing or uncertain**.」 |
| 驱动前的定位依据（找不到就阻断） | `.../SKILL.md:130` |
| 适配器能力与缺口的对账表 | `.../references/control-adapter.md:132` |
| 交付前的 setup check 第 3 步 | `.../references/control-adapter.md:161`「3. Load **one completed feature-map section**.」 |
| 维护的工作单位与严格度单位 | `skills/maintain-verification-skill/SKILL.md:9`「**The unit of rigor is the feature, not every sentence**: cover every feature file from source and exercise every feature live」 |
| 索引失效的判据 | `:25`「none → **stop and point at `/create-verification-skill` instead of inventing a target**」 |

`[事实]` **原文从未把 feature map 用作"开发需求来源"或"任务清单"。** 它在下游只有一种角色：**驱动与证明的入口索引**。

## T3-3-6 与 spec 的关系：**反向互补（不同轴、不同时点、不同作者、不同权威），原文无任何互引**

**先给事实**
- `[事实]` 我按 `feature[ _-]map` 穷举了 pstack 全部 **42 处**命中：**没有一处提到 spec / SPEC.md / 规格**。反向亦然（pstack 全仓 `grep -rn "SPEC.md"` → **0 命中**）。
- `[事实]` 时序相反：spec 在**动手前**（`addy/skills/spec-driven-development/SKILL.md:10`「Write a structured specification **before writing any code**」）；feature map 在**app 已存在之后**（`create-verification-skill/SKILL.md:36` 从 routes/commands/menus 抽取；`maintain/SKILL.md:9`「A feature map **rots the moment the app changes**」）。
- `[事实]` "冻结什么"相反：spec 那侧要**冻结可用信息**（addy `:84-114` 六核心区含 `Commands` / `Project Structure` / `Code Style` / `Testing Strategy` —— 都是要被写定的东西，只是 `:55` 禁 `file paths or code snippets`）；feature map 那侧**明令禁止冻结实现细节与当前代码路径**（`setup-benny:86`、`feature-map.example.md:3`）。

**发现一处同名不同质（要单独交给 Oracle）**：**addy 也有一个 "map"**，但性质与 pstack 的 feature map **相反**：

| | pstack `feature map` | addy `capability map` |
|---|---|---|
| 时点 | **app 之后**（描述已存在的行为） | **spec 之前**（`spec-driven-development/SKILL.md:44`「**Propose a capability map before writing any spec.**」） |
| 内容 | 用户可见行为 + 驱动配方 + 证明标准 | 模块分解 + 依赖方向 + 构建顺序（`:47-57`：`Module id / Responsibility / Depends on` + `Build order:`） |
| 性质 | **描述性**（`maintain:21` 冲突时改地图） | **规范性**（`:63`「**The map is gated like every phase.**」；`:65`「the map, not filename guessing, is the index of what exists」） |
| 权威 | 无（不得改产品） | 有（`:250`「Every module spec traces to a module id in the **approved** map」） |
| 谁批 | 无人批准（自动生成 + 漂移修复） | **人**（`:63`「The human reviews module boundaries, dependency direction, and build order」） |

`[事实]` 第三个 "map" 在 matt：`wayfinder` 的 **decision map**（`skills/engineering/wayfinder/SKILL.md:21`「The map is a single issue on this repo's issue tracker, labelled `wayfinder:map`, the canonical artifact.」）——**决策地图**，规范性的，且不在代码仓里（见 T3-4）。

**判定（回答"重叠？冗余？依赖？"）**
`[推断，推导链见下]` **既不是重叠、也不是冗余、也不是依赖，而是"反向互补"。**
- 不是**依赖**：feature map 的生成不读 spec（`create-verification-skill/SKILL.md:11`「Interview the repo, not the user」，只读代码）；spec 的生成也不读 feature map（addy `spec-driven-development` 的输入是 vision + 人的回答；matt `to-spec` 的输入是会话上下文）。
- 不是**重叠**：spec 定"该有什么行为"（应然），map 记"已有什么行为、怎么驱动它"（实然）。同一功能会在两处各出现一次，但**回答的问题不同**。
- 不是**冗余**：删掉任一，另一个无法承担其功能——删 spec 则无"要造什么"的冻结物；删 map 则每次验证都要重新发现驱动面（`docs/guide/06-verify-and-ship.md:39`「with **no setup conversation**」正是它省掉的东西）。
- **唯一接口**：spec 的验收判据要能被"驱动真实入口"证明（本库对应 `roles/verifier.md:88-105`；pstack 对应 `create-verification-skill/SKILL.md:30`「exercise the **real user path**, not internal setters or test-only endpoints」）。**两者是"应然/实然"的对偶，不是同一物的两种写法。**

## T3-3-7 与 grill / wayfinder 的关系

| 轴 | grill 家族（matt） | feature map（pstack） |
|---|---|---|
| 读谁 | **读人**：`skills/productivity/grilling/SKILL.md:26`「Finding _facts_ is your job, never the user's. … **The _decisions_ are the user's: put each to them and wait.**」 | **读代码**：`create-verification-skill/SKILL.md:11`「**Interview the repo, not the user**」 |
| 产出 | **决定/共识**（`grilling:6`「until you reach a shared understanding」；`grill-me` 连文件都不写） | **现状索引 + 驱动配方** |
| 时点 | 动手**前**（`docs/productivity/grill-me.md:11`「Reach for it **as soon as you have an idea worth taking seriously**」） | app **之后**（`maintain:9`） |
| 谁读产物 | 人 + 后续 agent | **agent**（`create-verification-skill/SKILL.md:9`） |

`[事实]` **唯一交汇点，也是三仓的根本分歧**：pstack 明确把"可观察的事实"从人手里拿走 ——
- `skills/poteto-mode/SKILL.md:20`「If the answer is a fact you could observe by running something (behavior, timing, layout, output, perf, **even whether an eval separates**), **it is not the human's to answer**. Sketch it via the **Prototype** playbook (`playbooks/prototype.md`) and let the result decide. … **Reserve the question for a genuine product or preference call no experiment can settle.**」
- 而 addy `skills/interview-me/SKILL.md:36` 要求「a **live, responsive user**」，matt `grilling:8` 要求「**wait for the user's answers** before the next round」。
→ **这不是"两套工具"，是"要不要问人"的相反默认值。** 见 T3-5 冲突清单 C1。

**与 wayfinder 的关系**：wayfinder 的雾里**明确包含"现状是什么"这一类** —— `docs/engineering/wayfinder.md:21`「a lot of the fog is **"what is already true here"** rather than "what should we do"」。这一块与 feature map 的功能**目标重叠**（都在回答现状），但：
- wayfinder 用 `research`（AFK，读外部一手资料）与 `prototype` 回答（`wayfinder/SKILL.md:77-80`），**没有一处用 feature map**；
- feature map 也不引用 wayfinder；
- 二者的"现状"范围不同：wayfinder 要的是**阻塞某个决定的事实**，feature map 要的是**能驱动起来的用户可见行为**。
`[事实]` **原文中两者零交集。**

---

# T3-4 · ideation 阶段：三仓各自的方法论 + wayfinder 专项

## T3-4-1 matt `wayfinder`：是什么、何时用、产出什么、冻结成什么

| 问题 | 原文 |
|---|---|
| **是什么** | `skills/engineering/wayfinder/SKILL.md:7`「A loose idea has arrived, **too big for one agent session**, and wrapped in fog: the way from here to the **destination** isn't visible yet. Wayfinding is about **finding that way, not charging at the destination**. This skill charts the way as a **shared map** on the repo's issue tracker, then works its **decision tickets** (questions whose resolution is a decision, not slices of a build to execute) one at a time until the route is clear.」 |
| **解决什么问题** | `docs/engineering/wayfinder.md:3`「an idea whose **destination** you can name but whose **route** you cannot yet see」；`:5`「It plans, it does not do. … the map is finished when **nothing is left to decide before someone goes and builds the thing**.」 |
| **何时用（触发）** | `docs/engineering/wayfinder.md:11`「the trigger is narrow: the effort has to be **genuinely larger than one agent session can hold**, and **the route to the destination has to be foggy**.」；`:16`「A greenfield project, or a build spanning many sessions, **with the route still unclear**」；`:21`「**Greenfield is not a requirement.** … it is arguably sharper there, because a lot of the fog is "what is already true here"」 |
| **产出什么** | `SKILL.md:21`「The map is **a single issue** on this repo's issue tracker, labelled `wayfinder:map`, **the canonical artifact**. Its tickets are **child issues** of the map.」；`:23`「The map is **an index, not a store** … a decision lives in exactly one place, its ticket, so the map never restates it, only gists it and links.」；四个区块 `Destination` / `Notes` / `Decisions so far` / `Not yet specified`（`:31-53`）+ `Out of scope`（`:95-101`） |
| **解析一个票据的动作** | `SKILL.md:125`「post the answer as a **resolution comment**, **close** the issue, and **append a context pointer** to the map's Decisions-so-far」 |
| **票据的四种类型** | `SKILL.md:65,:73-80`：`research`（AFK）/ `prototype`（HITL）/ `grilling`（HITL，**默认**）/ `task`（HITL 或 AFK） |
| **冻结成什么** | **不是一份文档，是 tracker 上的 issue 集合（map + 子 issue + resolution comment + blocking 关系）；而且它不是终点** —— `docs/engineering/wayfinder.md:66`「**The map is cleared.** Didn't wayfinder already write the spec and make the tickets? … **No.** Wayfinder's tickets are decision tickets, and by the time the map closes they are all closed too. What is left is a map full of linked decisions, **which is not a build plan**. **`to-spec` collapses those linked decisions into one spec** (`/to-spec #<map_issue>`) and **`to-tickets` slices that into tracer-bullet implementation tickets**. **Looping the map straight into `implement` skips the collapse and throws the linked detail away.**」 |
| **票据本身的粒度** | `SKILL.md:57`「sized to **one 100K token agent session**」 |
| **一次会话做几个** | `SKILL.md:105`「**never resolve more than one ticket per session**, with the exception of research tickets」 |
| **上游自认的洞** | `docs/engineering/wayfinder.md:69`「My agent started writing production code in the middle of a wayfinder session. — The most-reported failure with this skill, and **there is a real hole behind it**. Wayfinder's "plan, don't do" default can be overridden in the map's **Notes**, but **the Notes are written by the agent**, so the constraint and its exemption live in the same file the constrained party owns.」 |

## T3-4-2 与 `grill-me` / `grill-with-docs` 的分工与边界 —— **核 Owner 的判断**

**Owner 的判断**：「grill me 我大概明白，就是不知道想什么的时候用，**但那个时候其实应该用 wayfinder**。」

**上游原文（四条，直接回应）**
1. `docs/engineering/wayfinder.md:11`「**The split is a clean one**: `/grill-with-docs` for **single-session planning**, `/wayfinder` for **multi-session planning**.」
2. `docs/engineering/wayfinder.md:60`（最常见问题）「**How is this different from `/grill-with-docs`? Which should I start with?** — **Session count, not project size.** … If you can hold the whole thing in one conversation, grilling is the cheaper and better tool, and wayfinder is **genuinely slower and denser** for that case. The community shorthand that has settled on it: **wayfinder only makes sense if the work doesn't fit into a single session.** … **You have to judge the session count yourself.**」
3. `skills/engineering/wayfinder/SKILL.md:112`（**建图过程中就可能退回 grill**）「**Map the frontier.** Grill again, breadth-first … **If this surfaces no fog** (the way to the destination is already clear, **the whole journey small enough for one session**), **you don't need a map. Stop and ask the user how they'd like to proceed.**」
4. `skills/engineering/wayfinder/SKILL.md:111`「**Name the destination.** Call the Skill tool twice, for **"grilling"** and "domain-modeling"」→ **wayfinder 内部就用 grilling 来定 destination。**
5. 反向（`grill-me` 侧）：`docs/productivity/grill-me.md:11`「Reach for it as soon as you have an idea worth taking seriously … **Vagueness is not a reason to wait; it is the thing the session eats.** If you can already specify the thing precisely, you don't need to grill it.」
6. `docs/productivity/grill-me.md:17`「**Too big for one session**: `wayfinder`. It charts the effort as a map and runs grilling sessions inside it.」

**判定**
- `[事实]` **Owner 判断里"不知道想什么"这一半判据与上游不符**：上游的判据是**会话数 + 有没有雾**（`:60`「Session count, not project size」），而且**"模糊"被明确划给 grill-me**（`grill-me.md:11`「Vagueness is not a reason to wait; it is the thing the session eats」）。
- `[事实]` **Owner 判断里"该用 wayfinder"这一半在一种情形下成立**：当"不知道想什么"的**根因是工程装不下一个会话、路线看不清**时——因为 wayfinder **自己也用 grilling** 去谈 destination（`:111`），所以它不是替代 grilling，而是**把 grilling 装进一个多会话的决策地图里**。
- `[事实]` 上游还给了**一条反向闸门**：`SKILL.md:112` 明确"没有雾就不要建图，停下问用户"——即**wayfinder 会拒绝被误用**。
- `[推断，推导链]` 因此正确的说法是：**"不知道想什么"本身不是选型依据；"这件事能不能装进一次会话"才是。** 装得下 → `grill-me`（无仓）/ `grill-with-docs`（有码库）；装不下 → `wayfinder`，而它内部照样要先 grill。

## T3-4-3 addy 的 ideation 侧

| 技能 | 何时用 | 产出 |
|---|---|---|
| `skills/interview-me/SKILL.md:3`（description）「Extracts **what the user actually wants** instead of what they think they should want … until ~95% confidence」 | `:20-24` 四条：缺 who/why/success/constraint；请求是惯例式而非具体；正准备用未说出的假设开工；两个合理价值取向冲突时用户没选 | **一份"已确认的意图陈述"**（六字段）：`:99-108` `Outcome / User / Why now / Success / Constraint / Out of scope` + `Yes / no / refine?`；**唯一落盘形态**`:146`「offer to save it to **`docs/intent/[topic].md`** … **Only save if they confirm.**」 |
| `skills/idea-refine/SKILL.md:3`（description）「Refines raw ideas into sharp, actionable concepts through structured **divergent and convergent** thinking」 | `:29` 触发语「refine this idea / ideate on / stress-test my plan」；`:18`「This skill is primarily an **interactive dialogue**」 | **一页纸**：`:30-37`「The final output is a **markdown one-pager** saved to **`docs/ideas/[idea-name].md`** (after user confirmation), containing: Problem Statement / Recommended Direction / Key Assumptions / MVP Scope / **Not Doing list**」；`:130`「**The "Not Doing" list is arguably the most valuable part.**」 |
| `skills/constraint-driven-development/SKILL.md:57-91` 的 intake（`:57`「### Step 2: Four questions, each with a default」，`Q1`–`Q4` 各带 `GUESS` 与 `DEFAULT if unsure`，`:91`「Stop at four.」） | 项目没有写下质量标准时 | **`CONSTRAINTS.md`**（仓库根）：`:95`「**One file at the repo root.** Any agent on any harness can read it」；`:306`「`interview-me` — **the one-question-at-a-time discipline this skill's intake borrows**」 |

`[事实]` **addy 没有 brainstorming 技能，它的 ideation 载体就是 `idea-refine`**：25 个 `skills/` 目录里没有 brainstorming；全仓 `grep -li brainstorm` 只命中 `docs/comparison.md`，而那里是在描述**别的技能套件**（`:23` 表格把 `brainstorming` 归给 Superpowers 那一列，不是 addy 自己）。反过来，`idea-refine` **自称** ideation：`SKILL.md:41`「You are an **ideation partner**.」、`:104`「This is where most **ideation** fails.」、`:156`「examples of what great **ideation sessions** look like」；附件 `examples.md:1`（`# Ideation Session Examples`）与 `frameworks.md:1`（`# Ideation Frameworks Reference`，含 `:64` `## Constraint-Based Ideation`）。
`[事实]` **addy 的 Define 分组就是这四个**：`addyosmani-agent-skills/README.md:232-239` 表内 `interview-me` / `idea-refine` / `spec-driven-development` / `constraint-driven-development`；且同文件 `:16-22` 的相位图把 `Idea Refine` 画成整条链的第一格（`DEFINE ─→ PLAN ─→ BUILD ─→ VERIFY ─→ REVIEW ─→ SHIP`）。
`[事实]` **addy 内部的排序**：`interview-me/SKILL.md:190-191`「**`idea-refine`**: **downstream.** … **`spec-driven-development`**: **downstream.**」→ interview-me 在 idea-refine 与 spec 之前。

## T3-4-4 pstack 的 ideation 侧：**没有"问人"的 ideation 技能**

`[事实]` pstack `skills/` 下 **47 个条目**（含 23 个 `principle-*`）里没有 ideation / discovery / brainstorm / interview 类技能。**pstack 全仓 `grep -rniE 'brainstorm|ideation'` → 0 命中**；`discovery` 只有两处，且都不是产品发现：`skills/why/SKILL.md:62` 的小标题 `### Discovery`（从证据源里发现事实）、`automations/benny/FOR_AGENTS.md:33` 的 "slash-skill discovery"（技能发现）。
`[事实]` pstack 的 ideation 由四个东西承担，**全部是"做出来再看"**：

| 名称 | 原文 |
|---|---|
| `poteto-mode/playbooks/prototype.md` | `:3`「**You own the design decision, not the code. The prototype is a throwaway instrument.** The real build follows Feature.」；`:7`「Scope the decision the prototype exists to make … **No decision means no prototype. Route to Feature.**」；`:12`「The output is **the decision plus the throwaway artifact**, not shippable code.」 |
| `principle-exhaust-the-design-space` | description「Apply when facing a **novel UI interaction or architectural decision with no precedent** in the codebase. Build **2-3 competing prototypes** and compare side by side before committing.」 |
| `figure-it-out` | `:9`「When the task matches no playbook, design one. **The deliverable before any code is the workflow itself**: a sequence of phases that scales rigor to the task, runs the scientific method, and leaves a decision trail a human can audit after stepping away.」；Phase A `:17-23`「Ground first, then commit. Don't start the run until you can state: The definition of done as a **falsifiable predicate** … Scope, quantified … The rigor level, biased high.」 |
| `architect` + `arena` | `architect/SKILL.md:35`「**Design it twice.** Require at least two structurally distinct candidates before synthesis」；`arena` description「Spawn N parallel candidates at the same task, pick a base, graft the strongest parts of the losers into it.」 |

`[事实]` **pstack 的默认值是"不问人"**：`poteto-mode/SKILL.md:20`（全文见 T3-3-7）；配套 `principle-never-block-on-the-human`（description「Apply when tempted to ask "should I do X?" on reversible work. **Proceed, present the result, let the human course-correct after the fact**; reserve confirmation for irreversible actions.」）。

## T3-4-5 外部权威：软件工程的 ideation / discovery 阶段

**四条公认方法论（外部，附来源与逐字引文）**

**① Double Diamond**（UK Design Council，2004 公开；[外部] `https://www.designcouncil.org.uk/resources/the-double-diamond/`）
- 四相位：`Discover → Define → Develop → Deliver`（Design Council 官方讲义《Design methods for developing services》「Divided into four distinct phases: Discover, Define, Develop and Deliver」）。
- 关键原话：「**The first diamond helps people understand, rather than simply assume, what the problem is. It involves speaking to and spending time with people who are affected by the issues.**」
- 结构原话：「The two diamonds represent a process of **exploring an issue more widely or deeply (divergent thinking)** and then **taking focused action (convergent thinking)**」（同站《Framework for Innovation》）。
- **这一阶段冻结在第一个菱形的收口（Define）：问题定义。**

**② Shape Up / shaping**（Basecamp, Ryan Singer；[外部] `https://basecamp.com/shapeup/1.1-chapter-02` 与 `https://basecamp.com/shapeup/1.5-chapter-06`）
- shaping 四步：「1. **Set boundaries.** … 2. **Rough out the elements.** … 3. **Address risks and rabbit holes.** … 4. **Write the pitch**. Once we think we've shaped it enough to potentially bet on, we package it with a formal write-up called a `pitch`.」
- **冻结物 = pitch，五个必需成分**：「1. **Problem** … 2. **Appetite** — How much time we want to spend and how that constrains the solution 3. **Solution** … 4. **Rabbit holes** … 5. **No-gos** — Anything specifically excluded from the concept」。
- 三条性质：「**Property 1: It's rough**」「**Property 2: It's solved**」「**Property 3: It's bounded**」；对"太细太早"的警告：「**Work that's too fine, too early commits everyone to the wrong details.**」
- 缺一则不可下注：「**A problem without a solution is unshaped work.** … It's only ready to bet on when **problem, appetite, and solution come together**.」

**③ Amazon Working Backwards / PR/FAQ**（[外部] `https://workingbackwards.com/concepts/working-backwards-pr-faq-process/`）
- 主张：「Its key tenet is to **start by defining the customer experience, then iteratively work backwards** from that point until the team achieves **clarity of thought around what to build**. Its principal tool is … the **PR/FAQ**, short for Press Release and Frequently Asked Questions.」
- 结构：`Press Release`（Heading / Subheading / Summary / Problem / Solution / Quotes & Getting Started）+ `FAQ`（External FAQ + Internal FAQ）；内部 FAQ 要「cover all the challenging problems that need to be solved to build the product, whether technical, financial, legal, or operational」。
- 与实现的关系：「**Works with Agile** — The PR/FAQ process is used appropriately **at the beginning of the new product development process**. Once the PR/FAQ is finalized and approved, the Agile process can be employed to build the product.」
- **这一阶段冻结物 = 一份 PR/FAQ 文档，产出一个 go / no-go 决定**（「a level of completion of the PR/FAQ document is reached, and a **go, no-go decision** can be made」）。

**④ Continuous Discovery / Opportunity Solution Tree**（Teresa Torres；[外部] `https://www.producttalk.org/opportunity-solution-trees/`）
- 「Opportunity solution trees are a simple way of **visually representing the paths you might take to reach a desired outcome** … **The root of the tree** is your desired outcome…」
- 价值：「**The opportunity solution tree makes implicit assumptions explicit.** It helps teams draw strong logical connections between the solutions they're exploring, the opportunities they've identified, and the impact both have on their desired outcome.」
- 前提（来自其书中定义）：把"该解决什么"当 **ill-structured problem**，**framing the problem itself** 占大头工作。

**这一阶段最终要冻结出什么 —— 四条来源的共识（`[事实]`逐条可核）**

| 冻结项 | Double Diamond | Shape Up | PR/FAQ | OST |
|---|---|---|---|---|
| **① 一个被写下来的问题**（不是"想要个功能"） | Define 相位 | `Problem` | Press Release 的 "Problem" 段 | 树根 = desired outcome |
| **② 一个已成形但故意粗的解法** | Develop 相位起 | `Solution` +「Property 1: It's rough」 | Internal FAQ 的解法 | solution 节点 |
| **③ 明确不做的东西** | Define 的边界 | **`No-gos`** | out-of-scope | 未选中的分支 |
| **④ 已知的坑 / 约束** | — | **`Rabbit holes`** + `Appetite`（时间预算） | FAQ 里的 risks / constraints | 假设与实验 |
| **⑤ 一个由有权者作出的决定** | — | `betting table` 下注 | **go / no-go** | — |
| **不冻结** | 实现细节 | 「too fine, too early commits everyone to the wrong details」 | — | 具体接口 |

**另有一条本库已有外部裁决可对接**：`docs/TIM-PROFESSIONAL-WORKFLOW-PROPOSAL.md:203-205` 曾就"规格驱动 vs 代码即规格"裁过「**动态厚薄路由**：小修局部走薄配方，跨边界大改走厚规格」。→ 与上表的"厚度由风险定"同向。

## T3-4-6 一句话对比：三家在"从模糊想法 → 可开工"各选了哪条

| 仓 | 一句话 | 关键原文 |
|---|---|---|
| **matt** | **靠"谈"**：把决定一个个问出来（`grilling`）；一次装不下就先画决策地图（`wayfinder`），谈不动的造原型（`prototype`），最后**坍缩**成 spec 与工单（`to-spec` → `to-tickets`） | `wayfinder.md:66`「**to-spec collapses those linked decisions into one spec**」；`grilling:26`「The _decisions_ are the user's: put each to them and wait.」 |
| **addy** | **靠"访谈 + 变异"**：先把"用户真要什么"问出来（`interview-me` 六字段，唯一落盘 `docs/intent/`），需要扩选项再发散收敛成一页纸（`idea-refine`，唯一落盘 `docs/ideas/`），再写 PRD（`spec-driven-development`，四阶段**每阶段人工 review**） | `spec-driven-development/SKILL.md:26-32`（`SPECIFY/PLAN/TASKS/IMPLEMENT` 下方各写 `Human reviews`）；`interview-me:142-144`「**That's the deliverable.** Specs, plans, and task lists are downstream」 |
| **pstack** | **靠"做出来再说"**：**不问人**（可观察的事实不属于人），用最便宜的 `prototype` / `arena` / `architect` 把问题变成可看的候选；`figure-it-out` 只在没有更窄 playbook 时把整件事框成一份 playbook | `poteto-mode/SKILL.md:20`「**it is not the human's to answer** … Reserve the question for a genuine product or preference call **no experiment can settle**」；`playbooks/prototype.md:12`「The output is **the decision plus the throwaway artifact**」 |
| **三者共同缺口** | **三家都没有"idea 阶段"的落盘产物之外的东西**：matt 的 `grill-me` 不落盘、pstack 的 prototype 是丢弃物、addy 的 intent/idea 落盘要用户确认。**"模糊想法 → 可开工"这条路上，唯一被三家共同接受的持久物是 spec/plan/tickets 三件套，而它们都已属于"决定已经谈完"之后。** | `grill-me.md:5`「It is **stateless**. It writes no files」；`playbooks/prototype.md:3`「throwaway instrument」；`interview-me:146`「**Only save if they confirm.**」 |

---

# T3-5 · "implement 之前"的全景清单

## T3-5-0 全量检索怎么做的（可复核）

1. 抽出三仓全部 `**/SKILL.md`（**153 份**，已去 `third_party/`；逐仓：cursor-plugins **90**（含 pstack 50 + 其它插件）、matt **38**、addy **25**），逐份解析 frontmatter 的 `name` 与 `description`。
   可复现：`cd upstreams && for r in cursor-plugins mattpocock-skills addyosmani-agent-skills; do find $r -name SKILL.md | grep -v third_party | wc -l; done` → `90 / 38 / 25`。
2. 再按关键词全仓 grep 复核：`feature[ _-]map`（cursor-plugins **42** / matt **0** / addy **0**）、`SPEC.md`（pstack **0** / addy **13**）、`task[ _-]list`、`docs/adr`、`CONTEXT.md`、`CONSTRAINTS.md`、`plan.md`、`todo.md`、`intent`、`ideation`（pstack **0** / addy **10**，全在 `idea-refine` / matt **1**，在写作技能里）、`brainstorm`、`discovery`。
3. 筛选口径：**"在写第一行产品代码之前就已经产出、或必须已经存在的东西"**。据此排除：TDD/审查/验证/集成/发布/清理类技能（它们发生在 implement 之时或之后），以及纯跨切面的写作规范（`unslop` / `technical-writing` / `writing-for-agents`），后者在表后单列。

## T3-5-1 主表（`名称 | 哪一仓 | 何时用 | 产出物 | 冻结成什么 | 谁读`）

**A 组 · 触发与路由（决定"该用哪一套"）**

| 名称 | 仓 | 何时用 | 产出物 | 冻结成什么 | 谁读 |
|---|---|---|---|---|---|
| `using-agent-skills` | addy | 开始会话 / 判断该用哪个技能（`SKILL.md:3`） | 会话内判定 + 一组跨技能核心行为（`:49-80` Surface Assumptions / Manage Confusion / Push Back） | 不落盘 | agent |
| `ask-matt` | matt | 不知道该用哪个技能（description「A router over the skills in this repo」） | 路由建议 | 不落盘 | 人 → agent |
| `poteto-mode` | pstack | 非轻量任务的标准模式（`SKILL.md:8` reminder） | **playbook 选择** + 强制原则引用（`:15`「name each principle that shaped a decision」） | 选择结果进 todo | agent |
| `setup-matt-pocock-skills` | matt | 首次接入仓库，**一次性**（`docs/engineering/setup-matt-pocock-skills.md`） | `docs/agents/issue-tracker.md`、`docs/agents/domain.md`、`docs/agents/triage-labels.md`，以及 `AGENTS.md`/`CLAUDE.md` 里的 `## Agent skills` 指针块 | **仓内配置文件**（此后项目自己拥有） | agent（所有后续技能） |
| `setup-pstack` | pstack | 配置模型/预算 | `~/.cursor/rules/pstack-models.mdc`（model + reasoning budget） | 用户级规则 | agent |
| `setup-benny` | pstack | 装/改 Benny | `configuration.example.yaml` 的副本 + **用户自有 feature map**（放在包外） | 用户自有配置（包刷新**不得覆盖**，`SKILL.md:28`） | automation |
| `context-engineering` | addy | 开新会话 / 输出质量下降 / 切任务（description） | rules files + 上下文打包；**restartable boundary 五类信息**（`:123-135`：scope+decisions 进 spec/plan、任务状态与下一个待办、改动文件与工作树状态、验证命令与结果、未决问题与所需批准） | 落进 spec/plan（不是新文件） | 下一个会话 |
| `recall` | pstack | 开新任务前、上下文丢失（description） | 一份 current-state brief | 不落盘（会话内） | agent 自己 |

**B 组 · 读现状（不改任何东西）**

| 名称 | 仓 | 何时用 | 产出物 | 冻结成什么 | 谁读 |
|---|---|---|---|---|---|
| `how` | pstack | 改东西之前理解子系统、归属/分层问题（description） | 真实路径追踪出的心智模型 | **不落盘**（会话内解释） | agent |
| `why` | pstack | 设计沿革 / 回归 / 事后分析（description） | 历史意图与证据；**可转成 `Preserve / Change / Avoid / Risk` 约束集** | 约束集（`SOURCES.md:4.6` 已登记本库只吸收"约束集"形态） | 设计与切片 |
| `research` | matt | 需要外部一手事实、要委派阅读（description） | **一个 Markdown 文件**，逐条引用来源 | 写进**仓库既有的笔记位置**；无既有约定则"放个合理的地方并说明"（`SKILL.md:12`） | 后续会话 |
| `source-driven-development` | addy | 用框架/库、要引官方文档（description） | 带引用的实现依据 | 落进代码注释/文档（非独立文件） | agent + 审查 |
| `create-verification-skill` | pstack | 项目**没有脚本化驱动面**而需要证明行为（`docs/guide/06:35`） | `.cursor/skills/verify-<app>/SKILL.md`（六段：Launch/Doctor/Drive/Evidence/Cleanup/Helpers）+ **`features/` feature map** | 项目内**长期维护的验证资产**（`SKILL.md:36`「the repo's maintained verification source」） | **agent**（见 T3-3-1） |
| `maintain-verification-skill` | pstack | feature map 漂移时（`docs/guide/06:45`） | 三态之一：`clean` / `changed`（**一个 PR，只含已证实的修正，只限验证技能自己目录**）/ `blocked` | 一个 PR 或"什么都不发" | 人（PR）+ agent |
| `blast-radius` | pstack | 小 diff 但不敢信（description） | 一个"这个改动为什么安全"的**可执行证明** | 命令 + 输出 | 审查 |
| `improve-codebase-architecture` | matt | 要找深化机会（description） | **自包含 HTML 报告** | **写到 OS temp，不落 repo**（`SKILL.md:39`「so nothing lands in the repo」） | **人**（`:60`「ask the user: "Which of these would you like to explore?"」） |
| `interrogate` | pstack | 设计/代码要对抗审（description） | 综合裁决（Act on / Consider / Noted / Dismissed）+ Agreement Map | 不落盘（裁决） | 人 + agent |
| `arena` | pstack | 一个非平凡产物怕锁死形状（description） | N 个候选 + 择优 + 嫁接结果 | 被选中的候选 | 下游实现 |
| `swarm` | pstack | 需要并行覆盖 / 赛马（description） | 一份合并报告（`PASS`/`ISSUES`/`BLOCKED` + gaps） | 报告 | 人 / agent |

**C 组 · 把模糊变成决定**

| 名称 | 仓 | 何时用 | 产出物 | 冻结成什么 | 谁读 |
|---|---|---|---|---|---|
| `grilling` | matt | 用户想压力测试计划/决定/想法（description） | **一棵被走完的决策树**（frontier 清空） | **不落盘**（primitive） | 会话内 |
| `grill-me` | matt | 有想法但还没成形；**无仓也可**（`grill-me.md:11,15`） | 一个更锋利的想法 | **完全不落盘**（`grill-me.md:5`「It is **stateless**. It writes no files and leaves no workspace behind. The only thing it leaves is a sharper version of the idea, **in your own head**.」） | 人自己 |
| `grill-with-docs` | matt | 有码库要对齐（`grill-me.md:16`） | 同一场访谈 + **边谈边写** | **`CONTEXT.md` 词汇表 + `docs/adr/` ADR**（`SKILL.md:3`） | 后续 agent |
| `wayfinder` | matt | **装不下一个会话且有雾**（`wayfinder.md:11`） | tracker 上的 map issue + 决策子 issue + resolution comment | **issue 集合**（不是文档），且**不是终点**：还要 `to-spec` 坍缩（`wayfinder.md:66`） | 会话之间（`SKILL.md:122` 每会话加载低分辨率 map） |
| `to-questionnaire` | matt | 决定卡在**别人**脑子里（`SKILL.md:7`） | `to-questionnaire-<slug>.md` | 一份**交给另一个人填**的 Markdown 问卷（`SKILL.md:16`） | 收件人（人） |
| `interview-me` | addy | 需求说不清、或在任何 plan/spec/code 之前（`:3,:12`） | **已确认的意图陈述**（六字段） | 可选 `docs/intent/[topic].md`（`:146`「**Only save if they confirm.**」） | 下游 spec/plan |
| `idea-refine` | addy | 概念还很粗糙、要扩选项（`:3,:29`） | **一页纸**（Problem Statement / Recommended Direction / Key Assumptions / MVP Scope / Not Doing） | `docs/ideas/[idea-name].md`（`:32`，用户确认后） | 下游 spec |
| `doubt-driven-development` | addy | 高风险/不熟的代码，要在决定生效前对抗审（description） | `CLAIM → EXTRACT → DOUBT → RECONCILE → STOP` 的复核结果 | 不落盘（决定被确认或推翻） | agent |
| `prototype`（playbook） | pstack | 有一个**决定**要靠看才知道（`:7`「No decision means no prototype」） | **决定 + 丢弃物**（`:12`） | **不冻结**（`:3`「throwaway instrument」） | 人（看图/看行为） |
| `prototype`（skill） | matt | 状态模型/逻辑手感，或 UI 长什么样（description） | 单个可分享 HTML（逻辑分支）或 UI 变体 | 临时物；答完即弃 | 人 |
| `principle-exhaust-the-design-space` | pstack | 无先例的交互/架构决定 | 2–3 个并列原型 | 比较结论 | agent |
| `figure-it-out` | pstack | **没有更窄 playbook 可用**的大工程（description） | **workflow 本身**（phase 序列 + rigor 等级 + falsifiable predicate） | 一份可审计的 playbook 写下来（`:32`「Write the designed phase list down. **That list is what the human reviews.**」） | 人（审）+ 执行者 |
| `principle-never-block-on-the-human` | pstack | 想为可逆工作问"要不要做 X"（description） | — | 默认：先做再给人看 | — |

**D 组 · 冻结"词 / 形状 / 契约"**

| 名称 | 仓 | 何时用 | 产出物 | 冻结成什么 | 谁读 |
|---|---|---|---|---|---|
| `domain-modeling` | matt | 讨论术语 / 写 `CONTEXT.md` / 记 ADR（description） | 就地改写的词汇表 + ADR | **`CONTEXT.md`（glossary and nothing else，`SKILL.md:64`）+ `docs/adr/NNNN-slug.md`（`:66-72` 三条件）**；多上下文用 `CONTEXT-MAP.md`（`CONTEXT-FORMAT.md:32-52`） | 所有后续技能（`tdd/SKILL.md:10` 明写先读 `CONTEXT.md`） |
| `documentation-and-adrs` | addy | 要记架构决定 / 改公开 API / 发特性（description） | ADR | **`docs/adr/*.md` 或项目既有约定（`:38-42`「An established convention overrides the defaults below」）** | 未来的工程师与 agent |
| `codebase-design` | matt | 设计模块接口 / 决定接缝位置（description） | 深模块词汇（模块/接口/实现/深度/接缝/适配器/杠杆/局部性） | **不落盘**（共享词汇，供其它技能引用） | 其它技能（`tdd/SKILL.md:26`） |
| `api-and-interface-design` | addy | 设计 API/模块边界/公开接口（description） | 契约先行的接口设计 | 落进代码与契约文档 | 实现方 + 消费者 |
| `architect` | pstack | 非平凡工作怕锁死形状（description） | 草稿式类型/签名/模块边界（`not implemented` 体） | **草稿即契约**：`SKILL.md:55`「The synthesized sketch **is the contract**.」；偏离要上报（`:57`） | 实现者 |
| `principle-type-system-discipline` / `principle-model-the-domain` / `principle-foundational-thinking` | pstack | 写逻辑**之前**定类型/结构（三条 description 分别写 `Designing types or a signature` / `Apply when writing stateful logic` / `Apply before writing logic`） | 形状决定 | 写进代码的结构 | 实现者 |

**E 组 · 冻结"怎么算对 / 底线"**

| 名称 | 仓 | 何时用 | 产出物 | 冻结成什么 | 谁读 |
|---|---|---|---|---|---|
| `constraint-driven-development` | addy | 没有写下质量标准，或 agent 在悄悄降标准（description） | 四问 intake → `CONSTRAINTS.md` | **仓库根 `CONSTRAINTS.md`**（`:95`）+ `AGENTS.md`/`CLAUDE.md` 一行指针（`:140`）+ `references/floor-guard.md`（diff 级底线守卫） | agent（每次改动）+ CI |
| `principle-prove-it-works` | pstack | 声明完成之前（description） | 对真实产物的验证 | 判据 | 人 |
| `verify-this` | cursor-team-kit | 要用新证据验证一个主张（description） | `VERIFIED` / `NOT VERIFIED` / `INCONCLUSIVE` | 结论 | 人 |
| `planning-and-task-breakdown` 的检查点 | addy | 计划里定检查点（`:106-124`） | 每 2–3 个任务的检查点（含"继续前与人类复核"） | 写进 `tasks/plan.md` | 人 + agent |

**F 组 · 冻结"要做什么"（spec 层）**

| 名称 | 仓 | 何时用 | 产出物 | 冻结成什么 | 谁读 |
|---|---|---|---|---|---|
| `spec-driven-development` | addy | 新项目/特性/重大改动且还没有 spec（description） | 四阶段（+Phase 0 能力地图）→ spec 六核心区（`:84-114`） | **`SPEC.md` / `docs/SPEC.md` / `spec/*`**；若项目已有 OpenSpec 等则**用它自己的形态**（`:150-154`「instead of creating a duplicate `SPEC.md`」）；Phase 0 的 `capability map` 存项目根、每模块 `SPEC-<module>.md`（`:65`） | 人（每阶段 review）+ 下游 plan/build |
| `to-spec` | matt | 会话里决定已经谈完了（`wayfinder.md:66`） | 一份 spec，**发到 tracker** 并打 `ready-for-agent`（`SKILL.md:19`） | **tracker issue**（`Problem Statement / Solution / User Stories / Implementation Decisions / Testing Decisions / Out of Scope / Further Notes`，`:21-73`） | triage 与后续实现 |
| `triage` | matt | issue / 外部 PR 进仓（description） | 分类 + 状态标签 + **agent brief** | 两类标签（`bug`/`enhancement`）+ 五态（`needs-triage`/`needs-info`/`ready-for-agent`/`ready-for-human`/`wontfix`，`SKILL.md:31-37`）；brief 形态见 `AGENT-BRIEF.md`；排除项进 **`.out-of-scope/` 知识库**（`:22`） | agent（取 `ready-for-agent` 的活） |
| pstack 的 "finish condition in the first prompt" | pstack | 派活的第一句话（`docs/guide/06:7-9`） | 可运行的三条检查 | **不落盘**（在 prompt 里） | 执行 agent |

**G 组 · 切片（implement 前的最后一步）**

| 名称 | 仓 | 何时用 | 产出物 | 冻结成什么 | 谁读 |
|---|---|---|---|---|---|
| `planning-and-task-breakdown` | addy | 有 spec 或清晰需求，要拆成可实现的任务（description） | 计划文档 + 任务清单 | **`tasks/plan.md`（总是 Markdown）+ `tasks/todo.md`（默认清单）或外部 tracker**（`:143-164`）；用外部 tracker 时 plan 的 Task List 区只作**索引**，不复制（`:164`） | 人 + `/build` |
| `to-tickets` | matt | 有了 plan/spec，要拆成 tracer-bullet 工单（description） | 一组垂直切片票据，每个声明 blocking edges | **本地：`.scratch/<feature-slug>/issues/<NN>-<slug>.md`（一票一文件）**；真实 tracker：一条 issue 一个票据，用原生 blocking（`:62-63`），打 `ready-for-agent` | agent（`.scratch/.../issues/NN-*.md` 由 /implement 消费） |
| `multi-phase-plan` | pstack | 要交给人审计的多阶段计划（playbook） | plan 文件 | **默认写进 agent store 的 `docs/`**（`multi-phase-plan.md:8`「Unless the operator names a path, write the file under **the agent store's `docs/`**」）；勾选框必须在证据存在后才勾（`:24`） | 人（按证据审计）+ agent |

**H 组 · 症状入口（也属于 implement 之前：没有回路就不许开工）**

| 名称 | 仓 | 何时用 | 产出物 | 冻结成什么 | 谁读 |
|---|---|---|---|---|---|
| `diagnosing-bugs` | matt | 硬 bug / 性能回归，用户说 diagnose / debug（description） | **一条对这个 bug 会变红的紧回路** | `SKILL.md:20`「**This is the skill.** Everything else is mechanical. If you have a **tight** pass/fail signal for the bug (one that goes red on _this_ bug), you will find the cause … **If you don't have one, no amount of staring at code will save you.**」；`:26-30` 给出便宜→贵的构造顺序（失败测试 → curl/HTTP 脚本 → CLI diff → 无头浏览器 → 重放捕获的 trace）；`:10`「read `CONTEXT.md` (if it exists)」 | 实现者（回路即回归测试本体） |
| `debugging-and-error-recovery` | addy | 测试挂 / 构建断 / 行为不符（description） | 五步分类结果 | Stop-the-Line Rule：停 → 保存证据 → 诊断 → 修根因 → 防复发 → 验证过才恢复 | 实现者 |
| `investigation`（playbook） | pstack | 只读调查类请求；`:5`「Investigation requests are **read-only**. They produce a cited explanation or a recommendation, **not a code change**.」 | `how` 形状的产出（Overview / Key Concepts / How It Works / Where Things Live / Gotchas），或带 tradeoffs 表的建议 | `:12`「No PR, no babysit, no `architect` **unless the investigation precedes a code change**. If it does, hand back to the user and re-route to Bug fix or Feature.」 | 人（拿结论决定下一步） |
| `runtime-forensics` / `trace-forensics`（playbooks） | pstack | 需要从运行时痕迹反推（playbook 名） | 痕迹分析结论 | 不落盘（可进决策台账） | 调查者 / 人 |

**T3-5-1b · 边界判定（我把哪些算进来、哪些判出去，以及为什么——便于 Oracle 重切）**

| 判定 | 条目 | 理由 |
|---|---|---|
| **判进来（虽然作用在动静之间）** | `blast-radius`、`interrogate`、`arena`、`swarm`、`verify-this`、`principle-prove-it-works`、`architect` | 它们读的是**已存在的 diff 或草图**，但它们产出的判断会**改变要不要开工 / 怎么开工**；且 pstack 把 `architect` 摆在 `Feature` playbook 的第 2 步（`playbooks/feature.md:6`），即**实现之前**。若 Oracle 认为它们属于判断层而非输入层，可整组移出，不影响其余七组。 |
| **判出去（发生在 implement 之时或之后）** | `tdd` / `test-driven-development` / `incremental-implementation`（写代码时）、`code-review` / `code-review-and-quality` / `code-simplification` / `thermos` / `thermo-nuclear-*`（写完之后）、`browser-testing-with-devtools` / `run-smoke-tests`（验证时）、`observability-and-instrumentation` / `security-and-hardening` / `performance-optimization` / `deprecation-and-migration` / `frontend-ui-engineering`（主用点在写与写之后）、`git-workflow-and-versioning` / `opening-a-pr` / `shipping-and-launch` / `ci-cd-and-automation`（交付与流水线） | 它们确实会产出**判断**，但作用对象是**已经存在的代码**；把它们列进表会注水（本库 `pipeline.md` 的分类也把审查/验证/集成放在 implement 之后）。**唯一边界擦模糊的是 `api-and-interface-design`**：它的"契约先行"发生在实现前，但它的技能主体是写接口；本表只在 D 组保留它的名字，不重复。 |

`[事实]` 这张表另一个可复现的口径（脚本数行，非估）：**上表八组共 53 行** —— A 8 · B 11 · C 13 · D 6 · E 4 · F 4 · G 3 · H 4。三仓 `**/SKILL.md` 共 153 份，故**约三分之一（±）属于 implement 之前**。Oracle 若要重切，重切对象是 53 而不是 153。


## T3-5-2 跨切面（不属"implement 之前"，但每一段都要用）

| 名称 | 仓 | 作用 | 落盘 |
|---|---|---|---|
| `show-me-your-work` | pstack | 决策台账（一行一决定：时间/阶段/决定/理由/证据/结果） | `decisions.tsv`（默认本地，不提交）或 `.audit/<task-slug>.tsv` |
| `handoff` / `claude-handoff` | matt | 压缩会话交给下一个 agent | **OS temp 级文档** |
| `session-pickup` / `pause-safely` | pstack | 暂停与接手 | `/tmp/<slug>-resume.md` 级 |
| `writing-for-agents` / `technical-writing` / `unslop` / `no-comments` | matt/pstack | 写 agent 读的文档 / 技术文风 / 去 AI 味 / 注释纪律 | 就地 |
| `reflect` / `retro` / `continual-learning` / `workflow-from-chats` | pstack/matt/cursor-plugins | 从会话里挖经验并改写技能或规则 | 技能文件 / `AGENTS.md` |

## T3-5-3 边界与冲突清单（**交给 Oracle，我不拼**）

> 格式：`编号 · 争点` → 甲方原文 / 乙方原文 → 冲突性质。

**C1 · 「可观察的事实该不该问人」——极性相反**
- 甲方（**必须问人**）：matt `skills/productivity/grilling/SKILL.md:26`「Finding _facts_ is your job, never the user's. … **The _decisions_ are the user's: put each to them and wait.**」；`grilling:28`「**Do not act on it until the user confirms**」；addy `skills/interview-me/SKILL.md:36`「This skill needs a **live, responsive user**. **Do not invoke in non-interactive contexts** like CI pipelines, scheduled runs, `/loop`, or autonomous-loop.」
- 乙方（**不许问人**）：pstack `skills/poteto-mode/SKILL.md:20`「If the answer is a fact you could observe by running something (behavior, timing, layout, output, perf, even whether an eval separates), **it is not the human's to answer**. Sketch it via the Prototype playbook and **let the result decide**.」（配套 `principle-never-block-on-the-human`）
- 性质：**不是措辞差异，是默认值相反**。本库已裁过一次（`SOURCES.md:276-281`：「执行不阻塞，**范围与授权必须阻塞到明确确认**」），但那次裁的是"执行"轴，**没有裁"事实"轴**。

**C2 · 三个都叫 "map" 的东西，性质互不相同**
- addy `capability map`：**规范性、spec 之前、人工批准**（`spec-driven-development/SKILL.md:44,63,250`）
- pstack `feature map`：**描述性、app 之后、agent 读**（`create-verification-skill/SKILL.md:36`；`maintain-verification-skill/SKILL.md:21`）
- matt `wayfinder map`：**决策性、在 tracker 上、人+agent 读**（`wayfinder/SKILL.md:21`）
- 性质：**同名不同物**。任何"把 map 融进来"的说法都必然歧义。

**C3 · 「谁写 spec / 写之前要不要访谈」——直接相反**
- 甲方（**禁止访谈，只综合**）：matt `skills/engineering/to-spec/SKILL.md:7`「This skill takes the current conversation context and codebase understanding and produces a spec. **Do NOT interview the user**; just synthesize what you already know.」
- 乙方（**必须访谈**）：addy `skills/spec-driven-development/SKILL.md:69`「Start with a high-level vision. **Ask the human clarifying questions until requirements are concrete.**」
- 性质：**直接冲突**。两边都有明确理由（matt 的访谈发生在 `grilling` 那一步、spec 只做坍缩；addy 把访谈放在 spec 内部）。

**C4 · 「人工门的密度」——直接相反**
- 甲方（**每阶段都有人门**）：addy `spec-driven-development/SKILL.md:24`「Do not advance to the next phase until the current one is **validated**」+ `:26-32` 四个阶段下方各写 `Human reviews`；`:246`「The human has **reviewed and approved** the spec」
- 乙方（**默认无人门**）：pstack `skills/architect/SKILL.md:43-45`「**Phase C: Agree (opt-in)** — **Default: proceed directly to implementation with the synthesized design. No human checkpoint.** Opt in … when the invoker explicitly asks」
- 丙方（**一次门**）：addy `commands/build.toml:33`「**Single checkpoint.** Present the full plan and wait for an unambiguous affirmative … This is the only human gate — after approval, run autonomously.」
- 性质：三种门密度都在同一批技能里。本库 `pipeline.md:120-128` §10 已选"授权检查 + 实现前硬线"，与三者都不同。

**C5 · 「一轮问一个问题 vs 一轮问完整个 frontier」——两边都自认有争议**
- 甲方（**一次一个**）：addy `interview-me/SKILL.md:53-60`「Ask one question at a time, each with a guess attached」；`:64-69` 给出三条理由（用户无法对埋在列表里的假设做反应；批量鼓励略读；第三问常依赖第一问）
- 乙方（**一轮问完**）：matt `grilling/SKILL.md:8`「Ask the whole frontier in one round」
- **两边都自述这条有争议**：matt `docs/productivity/grilling.md:45-52`「**Can I go back to one question at a time?** Yes, and a large part of the audience does. … **The round-based default is genuinely contested.**」
- 性质：**真实分歧，且未被任何一方解决**。本库 `roles/driver.md §4.1` 选了"一轮问一个 frontier"，来源是 matt（`SOURCES.md:152-155`）。

**C6 · 「idea 阶段要不要发散」——三家选了三种答案**
- addy：**要**，`idea-refine` 的 divergent→convergent，产出多个变体（`:132`「Don't generate 20+ ideas. Quality over quantity. **5-8 well-considered variations** beat 20 shallow ones.」）
- matt：**不要**，没有发散技能；用 `grilling` 收敛 + `prototype` 回答"谈不动的"（`grill-me.md:33-37`）
- pstack：**要，但发散的是"做出来的东西"而不是"想法"**（`principle-exhaust-the-design-space`：2–3 个并列原型；`arena`：N 个候选 + 择优嫁接）
- 性质：**同一目标（扩大选项空间）的三种载体**（描述 / 谈话 / 原型）。

**C7 · 「产物落在哪」——三仓三个默认位置，且有一仓明确反对另外一仓的做法**
- addy：**仓内固定路径**——`tasks/plan.md`、`tasks/todo.md`、`SPEC.md`、`docs/intent/`、`docs/ideas/`、`CONSTRAINTS.md`（都在仓库里）
- matt：**仓外 tracker 为主**——`.scratch/<feature>/issues/`（本地兜底：一票一文件）或真实 tracker；`SPEC.md` 不出现
- pstack：**agent store 的 `docs/`**，且明确"不往项目里加第二个位置"（`multi-phase-plan.md:8`「Unless the operator names a path, write the file under the agent store's `docs/`」）
- **matt 明确反对仓内落盘**：`docs/engineering/wayfinder.md:78`「**local markdown puts the artifacts in your repo, which is not recommended**: storing this material in the repo tends to lead to **accidental persistence**.」
- 性质：**三仓都同意"必须指定一个位置"，但对"在仓内还是仓外"结论相反。** 本库 `AGENTS.md` 与 `SOURCES.md` 已有相关裁决（G7 组），但**当时未涉及 feature map / intent / idea 这三类**。

**C8 · 「谁有权写"词"」——上游与已改写过的本库**
- 上游：matt `domain-modeling/SKILL.md:62`「When a term is resolved, **update `CONTEXT.md` right there. Don't batch these up**」→ agent 直接写。
- 本库已改写：`roles/architect.md:209-210`（业务含义裁定权归 Owner；Architect 只是写者），`SOURCES.md:180` 登记为「局部吸收（改写）」。
- 性质：**已裁过，不是新冲突**；但它是 DDD 那一段在融合时**不能照搬上游**的直接证据。

**C9 · 「spec 是活文档还是冻结物」**
- addy：**活**（`spec-driven-development/SKILL.md:212`「The spec is a **living document**, not a one-time artifact」；`:214`「Update when decisions change — If you discover the data model needs to change, **update the spec first, then implement**.」）
- matt：**进 tracker 后由 triage 状态机接管**（`to-spec:19` 打 `ready-for-agent`），没有"活文档"规则
- pstack：**无 spec 载体**（全仓 `SPEC.md` 0 命中）；最接近的是"调用方体验即 spec"（`skills/architect/references/rationale-template.md:11`「**The caller's experience is the spec.** The types serve it.」）与"基线即 spec"（`playbooks/visual-parity.md:3`「The baseline is the spec. You do not touch it.」）——**两者都不是文档**
- 性质：**同一词指三种东西。**

**C10 · 「pstack 缺 spec 这一层」——融合时的硬约束**
- `[事实]` pstack 全仓 **`SPEC.md` 0 命中**，也没有"规格"这个一等产物；它的对应物是 ① prompt 里的 finish condition（`docs/guide/06:7-9`）、② `multi-phase-plan` 的 plan 文件、③ `architect` 的 sketch-as-contract（`architect/SKILL.md:55`）。
- `[事实]` 而 matt 主链是 `grill-with-docs → to-spec → to-tickets → implement → code-review`（`docs/engineering/tdd.md:91`），addy 是 `SPECIFY → PLAN → TASKS → IMPLEMENT`（`spec-driven-development:27`）。
- 性质：**"三家融成一条"时，pstack 那一段必须被改写而不是搬运**——它没有可以对齐的 spec 载体。

## T3-5-4 五处本库已经裁过、可以直接复用的裁决（避免 Oracle 重裁）

| 争点 | 本库已有裁决 | 位置 |
|---|---|---|
| 重构在 TDD 循环内还是外 | 采纳 addy（**在循环内**），明确不采纳 matt | `SOURCES.md:306-313` |
| 何时阻塞在人身上 | **执行不阻塞，范围与授权必须阻塞到明确确认**；授权门优先 | `SOURCES.md:276-281` |
| 数字门禁从哪来 | 只允许三个来源（用户要求 / 既有契约 / CI）；**"当前实测基线"不是来源** | `SOURCES.md:295-305`（§4.4 量化门禁）；`roles/planner.md:115-133`（§4.5） |
| 业务词义的裁定权 | **Owner 或 Owner 授权的业务角色**；工程侧不得擅自决定 | `roles/architect.md:209`；`SOURCES.md:180` |
| 规格的厚薄 | **动态厚薄路由**（按风险，不按文件数） | `docs/TIM-PROFESSIONAL-WORKFLOW-PROPOSAL.md:203-205`；现载体 `pipeline.md §2` |

## T3-5-5 三仓无此法（对 T3-3/T3-4/T3-5）

1. **feature map 与 spec 的任何显式关系**：三仓无此法。pstack **42 处** feature map 命中里 **0 处提到 spec**；`SPEC.md` 在 pstack **0 命中**；matt 的 spec 链（`to-spec`/`to-tickets`）**完全不提 feature map**；addy 的 spec 链只提它自己的 `capability map`。
2. **feature map 的"人类读者"定位**：三仓无此法。`create-verification-skill/SKILL.md:9` 反向明写「**not for a human**」。
3. **"ideation 阶段"作为一个被独立命名的阶段**：三仓无此法 —— **pstack 全仓 `ideation` 0 命中**，matt 只在写作技能里用过一次（`skills/in-progress/writing-shape/SKILL.md:43`「In ideation, the question was "what are you actually noticing?"」，讲写文章不是做软件）；只有 addy 把它当成自己技能的定位（`idea-refine/SKILL.md:41`「You are an **ideation partner**」）。但**三家都没有把 ideation 排成流程里的一个阶段**：addy 的相位图第一格叫 `Idea Refine`（`README.md:16-22`），matt 用 `grilling` primitive，pstack 没有对应分组。
4. **"idea 阶段"的持久产物**：三仓都只有"可选、且需用户确认"的落盘（`interview-me:146`、`idea-refine:140`），或干脆不落盘（`grill-me:5`、prototype 丢弃物）。**没有一仓规定"进 implement 之前必须有一份 idea 文档"。**
5. **Double Diamond / Shape Up / PR/FAQ / OST 这四条外部方法论**：三仓**一条都没引用**（全仓 `grep -riE 'double diamond|shape up|pr.?faq|continuous discovery|opportunity solution'` → **0 命中**）。→ 若要把它们作为"公认方法论"引入，**必须标为外部来源，不能挂三仓的名义**。
6. **"谁维护 idea/意图文档"**：三仓无此法（`docs/intent/` 与 `docs/ideas/` 只规定"存哪"，不规定谁维护、活多久、何时可删）。

---

## 附：本次未取证 / 判不了的点（不猜）

| # | 点 | 为什么判不了 |
|---|---|---|
| U1 | feature map 是否**应该**在本库成为长期资产 | 本库 Owner 已定"可选、不是开工门"，但**没有回答"谁持有、谁维护、活多久"**（`.pi/core/OPEN-ITEMS.md` C1/C6 + A5 仍为未开始） |
| U2 | 「事实该不该问人」在本库的落点 | `SOURCES.md:276-281` 只裁了"执行"轴；"事实"轴**无裁决**，而两仓默认值相反（C1） |
| U3 | 三家 spec 载体选哪一个 | matt 的 tracker 形态在本库无底座（本库无 tracker 绑定）；addy 的 `SPEC.md` 与 pstack 的"无 spec"三种形态，取舍属设计 |
| U4 | GV Design Sprint 是否算公认 | 我**没有取到一手页面**，因此本文件不引用它（只在 T3-4-5 记名，不算证据） |
| U5 | `wayfinder` 的 `task` 票据类型在本库对应什么 | 上游自认这是最常被误用的一类（`wayfinder.md:53`「agents interpret it as an implementation step and start writing product code inside the map」）；本库没有"为了解锁一个决定而先做的杂活"这一类收据 |
