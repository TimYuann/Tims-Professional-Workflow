# EVIDENCE · 文档体系 / feature map / 角色写权限粒度 / 四套方法论

**角色**：调查者（只读取证，不改任何产物）。**产出**：本文件 + `SUMMARY.md`。

## 0. 取证范围与方法

| 取证对象 | 锁定值 | 工作区状态 |
|---|---|---|
| `upstreams/cursor-plugins`（含 pstack 0.15.5） | `ecc249f1e306fc64ddf83c7bed16cacf7c2239db` | 干净（`git status --porcelain` 空） |
| `upstreams/mattpocock-skills` | `c55ee46073ed923f86ce59a5eb3b6d895095d1b7` | 干净 |
| `upstreams/addyosmani-agent-skills` | `2686b620fc1fed2e8f60c704839c766b8594c6b6` | 干净 |
| 本仓（`tim-professional-workflow`） | 只读；不写任何受保护路径 | — |

- 方法：每个仓先读 README / 目录结构再检索（pstack `docs/guide/README.md`、matt `CLAUDE.md`+`CONTEXT.md`、addy `docs/getting-started.md`）；每条结论给 `file:line` + 原文摘录。
- 三仓没有的，写「三仓无此法」；需要外部权威时给 URL + 引文，并注明「外部来源，非三仓」。
- **未覆盖**：三仓的 `third_party/**`、`index.html`、`node_modules`、git 历史；不想象未读内容。
- 外部来源为 **2026-09-27 抓取**，引文以抓取时的页面文本为准。

---

## G1 · 三仓怎么管理"文档与进度记录"

### G1.1 pstack（cursor-plugins）

**G1.1-01 · 决策台账：形态 / 谁写 / 存哪 / 活多久**
`skills/show-me-your-work/SKILL.md:13-22`：「一份 TSV 台账，一行一个决定：时间 / 阶段 / 决定 / 理由（白话）/ 证据（指针不是段落）/ 结果」；`:9`「Keep one canonical log.」
`SKILL.md:44-48`：「## Where it lives / By default the log is a working artifact, not committed. Keep it at `decisions.tsv` in the work dir, or `.audit/<task-slug>.tsv` when several efforts run at once, and leave it out of git. / Commit it only when the work is ambitious enough that a reviewer needs the trail to trust the result.」
→ 形态=单文件 append-only TSV；写者=执行该轮工作的 agent；位置=工作目录/`.audit/`；寿命=默认本地不提交，按"reviewer 需不需要这条 trail"决定是否进版本库。**这是三仓里唯一明写"记录活多久/进不进版本库"判据的地方。**

**G1.1-02 · 更新频率与触发**
`SKILL.md:40`：「Log decision points and checkpoints, not every action: a fork chosen, a unit completed with its verification result, a pivot or revert with its trigger, a blocker surfaced, a gate fixed. For loop runs, one row per iteration.」
`skills/poteto-mode/playbooks/autonomous-run.md:10`：「5. Checkpoint every iteration via the **show-me-your-work** skill, a row for what changed and whether the predicate moved.」
`skills/poteto-mode/playbooks/multi-phase-plan.md:43`（30 分钟审计 tick 的 prompt）：「…Either way, log this tick's row in your decision trail.」
→ 触发=每个决策点 / 每轮循环 / 每次审计 tick；**不允许只留会话不留文件**。

**G1.1-03 · 防腐烂（append-only + 回核）**
`show-me-your-work/SKILL.md:52`：「Append-only. A wrong call gets a new row that supersedes it. Never edit or delete history.」
`:63`：「Correct the log, not the story. The audit never edits or removes a row, even an invented one. When a row records neither a real decision nor a real action, or its claim or evidence is wrong, add a row that supersedes it…」
`:67`：「Before handing back, spawn a subagent on a different model family from the one that did the work. Self-review is not a substitute.」
→ 台账不靠"删错行"保真，靠**追写覆盖 + 独立会话回核 + 跨模型复审**。

**G1.1-04 · 长程序的状态库：每文件一个写者，派生视图可重算**
`skills/poteto-mode/playbooks/orchestrate.md:23`：「Create `orchestrate/<project-slug>/` … Every file has exactly one writer. Owners publish facts, readers aggregate at read time.」
`:25` `preferences.md`（standing orders，逐条，append）；`:26` `overview.md`「durable PR and issue DB. Append. Never rewrite wholesale per event.」；`:27` `units.tsv`「one row per unit: id, track, state, branch, PR, head SHA, brief path. Update rows in place.」；`:28` `frontier.json`（computed）；`:29` `ledger.tsv`（one row per verdict，keyed by PR + head SHA）；`:30` `inbox/`+`gates.md`；`:31` `decisions.tsv`；`:32`「`status.md` is derived from `units.tsv` and `ledger.tsv` at each drain, never hand-maintained. Regenerate it from the tables instead of narrating events into it.」
→ **文件级写权矩阵 + "事实表就地更新 / 事件记录追加 / 视图重算"三类写法的明确分工**。这是本组最强的可搬迁机制。

**G1.1-05 · 寿命与死后利用**
`orchestrate.md:66`：「Close. … Leave the store intact. It is the postmortem.」
`:91`：「A unit is not done until its output is externalized the moment it lands, never batched to the end of the run. … Work that exists only on one VM when that VM dies was never done.」
`:101`（重启恢复）：「local agents are dead, cloud work is not. Re-read the standing orders and `units.tsv`, recompute the frontier, reattach cloud work by PR and branch rather than agent id…」
`skills/poteto-mode/playbooks/pause-safely.md:8`：「Write the resume note off-context… For the compaction trigger write it to a file like `/tmp/<slug>-resume.md`. If a show-me-your-work trail exists, point at it instead of duplicating it.」
`skills/poteto-mode/playbooks/session-pickup.md:6`：「The prior trail is authoritative input. Resist the bias to re-derive it.」
→ 寿命判据=「store 留作 postmortem」；**中间态一律落盘**；恢复靠读文件而不是回忆；暂停笔记是 `/tmp` 级临时件（可丢）。

**G1.1-06 · 计划文档（checklist + 证据）**
`multi-phase-plan.md:3`：「You own the plan, not the code. The plan is a checklist an owner runs box by box and the operator audits from the evidence. The plan is the deliverable.」
`:8`：「Unless the operator names a path, write the file under the agent store's `docs/`.」
`:24`：「Check a box only when its evidence exists, a file, a log line, a screenshot, a test run, or a SHA.」
→ 进度=**勾选框 + 每框必须指到证据**；无证据不得勾。附录固化 prototype 证据 / 被否方案 / 风险 / 阅读清单（`:139` 起）。

**G1.1-07 · 验证源（feature map）与验证账**
见 G2；另 `orchestrate.md:89`：「`ledger.tsv`, one row per verdict, keyed by PR number plus head SHA… CI green is an input to a verdict, not a verdict… A new head SHA voids the row… The ledger answers 'was this verified', not memory and not the transcript.」

**G1.1-08 · 项目文档仓库里的位置（pstack 自己的仓）**
`docs/guide/README.md:5-16` 是 10 页导读（`01-setup` … `10-recipes`）的索引；`README.md:131-132` 在技能总表里登记两个验证技能。→ pstack 自己的文档=「导读 + 技能总表」双层，属于**上游插件仓的文档**，不是它替用户项目规定的文档层级。

### G1.2 mattpocock-skills

**G1.2-01 · 工作追踪的真源是外部 issue tracker，不在仓里**
`CONTEXT.md:7-9`：「**Issue tracker**: The tool that hosts a repo's issues: GitHub Issues, Linear, a local `.scratch/` markdown convention, or similar. Skills like `to-tickets`, `to-spec`, and `triage` read from and write to it.」
`skills/engineering/setup-matt-pocock-skills/SKILL.md:40`：「The "issue tracker" is where issues live for this repo… They need to know whether to call `gh issue create`, write a markdown file under `.scratch/`, or follow some other workflow you describe.」
`:46`：「**Local markdown**: issues live as files under `.scratch/<feature>/` in this repo (good for solo projects or repos without a remote)」
`:49`：「Record the choice in `docs/agents/issue-tracker.md`.」
→ 形态=**可换后端的工作追踪器**（GitHub/Linear/本地 `.scratch/` markdown）；选择本身落成仓内配置 `docs/agents/issue-tracker.md`。

**G1.2-02 · 本地 markdown 后端的目录/状态约定**
`skills/engineering/setup-matt-pocock-skills/issue-tracker-local.md:8-10`：「The spec is `.scratch/<feature-slug>/spec.md` / Implementation issues are one file per ticket at `.scratch/<feature-slug>/issues/<NN>-<slug>.md`, numbered from `01`, never a single combined tickets file / Triage state is recorded as a `Status:` line near the top of each issue file」
`:25-30`（wayfinder 操作）：「**Map**: `.scratch/<effort>/map.md` … **Child ticket**: … `Status:` line records `claimed`/`resolved` / **Frontier**: scan `.scratch/<effort>/issues/` for files that are open, unblocked, and unclaimed; first by number wins / **Claim**: set `Status: claimed` and save before any work / **Resolve**: append the answer under an `## Answer` heading, set `Status: resolved`, then append a context pointer … to the map's Decisions-so-far」
→ 进度=**文件里的状态字段 + frontier 扫描**；认领先写后干（防并发重复）。

**G1.2-03 · 规格与工单的"防腐"写法**
`skills/engineering/to-spec/SKILL.md:19`：「Write the spec using the template below, then publish it to the project issue tracker. Apply the `ready-for-agent` triage label」
`:55`：「Do NOT include specific file paths or code snippets. They may end up being outdated very quickly.」（Testing Decisions 一节另见 `:59`）
`skills/engineering/to-tickets/SKILL.md:62`（本地）：「write one file per ticket … numbered from `01` in dependency order (blockers first)」；`:105`：「In either form, avoid specific file paths or code snippets: they go stale fast.」
`triage/AGENT-BRIEF.md:11`：「The issue may sit in `ready-for-agent` for days or weeks. The codebase will change in the meantime. Write the brief so it stays useful even as files are renamed, moved, or refactored.」；`:15`：「**Don't** reference file paths: they go stale」；`:28`「Complete acceptance criteria」
→ **防腐烂判据：写行为/接口/验收，不写路径与行号**。这是三仓里最明确的一条"文档为什么会烂、怎么不烂"。

**G1.2-04 · 状态机（进度就是 label）**
`skills/engineering/triage/SKILL.md:31-45`：五个 state 角色 `needs-triage` / `needs-info` / `ready-for-agent` / `ready-for-human` / `wontfix`，五个之间的转移由 triage 执行；`:41`：「Every triaged issue should carry exactly one category role and one state role.」
`:13-16`：「Every comment or issue posted to the issue tracker during triage **must** start with this disclaimer: `> *This was generated by AI during triage.*`」
→ 进度不记百分比，记**状态 + 谁在推进**；AI 产生的评论必须自报来源。

**G1.2-05 · 被拒请求的知识库（消灭"重复讨论"）**
`skills/engineering/triage/OUT-OF-SCOPE.md:5`：「**Institutional memory**: why a feature was rejected…」；`:17`：「One file per **concept**, not per issue.」；`:68`：「The reason should be durable. Avoid referencing temporary circumstances」；`:86`：「Only when an **enhancement** (not a bug) is *rejected* as `wontfix`.」
`triage/SKILL.md:83`：「**Already implemented**: … Point to where it lives; do **not** write to `.out-of-scope/` (that KB is for *rejected* requests, not built ones).」
→ 一个**长期存活的决策知识库**，有明确写入条件（只在"被拒的增强"）、命名规则（按概念）、失效规则（改主意就删文件）。

**G1.2-06 · 人类可读文档与路由器**
`CLAUDE.md:9`：promoted bucket 的每个技能必须在顶层 `README.md` 有引用、在 plugin manifest 有条目；`:15`：每个 bucket `README.md` 列全技能；`:17`：`docs/<bucket>/<skill-name>.md` 人工页，四段 `What it does` / `When to reach for it` / `Common questions` / `It's working if`，「When you add, rename, or change the behaviour of a skill … create or re-sync its docs page」；`:21`：「[`ask-matt`] is the router … a new skill it never mentions, or a stale one it still routes to, is a router that lies.」
`.agents/writing-docs.md:83`：「no stale page survives a rename or bucket move」。
→ **文档与代码同改**是硬规则（加/删/改名必须同步），并有一个 router 文件承担索引。

**G1.2-07 · 寿命分级（谁进仓、谁只活一会）**
`skills/productivity/handoff/SKILL.md:8`：「Save to the temporary directory of the user's OS - not the current workspace.」
`skills/engineering/improve-codebase-architecture/SKILL.md:39`：「Write a self-contained HTML file to the OS temp directory so nothing lands in the repo.」
`skills/engineering/wizard/SKILL.md:12`：「A wizard is ephemeral by default: built for one run, saved to a scratch or `scripts/` path, deleted when the job's done. Commit it only when the user wants a repeatable setup path that should live in the repo.」
`skills/engineering/domain-modeling/ADR-FORMAT.md:3-5`：「ADRs live in `docs/adr/` and use sequential numbering… Create the `docs/adr/` directory lazily: only when the first ADR is needed.」
→ 存在**三类寿命**：临时件（OS temp，明确不进仓）/ 工作件（scratch，做完删）/ 耐久件（ADR/规格/工单/tracker）。判据是"以后还有没有消费者"。

**G1.2-08 · wayfinder 地图：索引不是仓库**
`skills/engineering/wayfinder/SKILL.md:21`：「The map is a single issue on this repo's issue tracker, labelled `wayfinder:map`, the canonical artifact.」；`:23`：「The map is an **index**, not a store. It lists the decisions made and points at the tickets that hold their detail; a decision lives in exactly one place…」；`:40-52`：map body 固定四段 `## Decisions so far` / `## Not yet specified` / `## Out of scope`（+ Destination/Notes）；`:123-125`：认领 → 解决 → `post the answer as a **resolution comment**`, close, append context pointer。
→ 一个"唯一权威位置 + 索引 + 未定域 + 排除域"的**层级化文档模板**，是三仓最接近"跨角色文档层级"的东西。

### G1.3 addyosmani-agent-skills

**G1.3-01 · 三个工作件的固定路径与寿命**
`docs/getting-started.md:173-177`：「The `/spec` and `/plan` commands create working artifacts (`SPEC.md`, `tasks/plan.md`, `tasks/todo.md`). Treat them as **living documents** while the work is in progress / Keep them in version control during development so the human and the agent have a shared source of truth / Update them when scope or decisions change / If your repo doesn't want these files long-term, delete them before merge or add the folder to `.gitignore` — the workflow doesn't require them to be permanent.」
`skills/planning-and-task-breakdown/SKILL.md:33`：「The output is a plan document saved to `tasks/plan.md` and a task list recorded in the task list target … default `tasks/todo.md`」
`:145`：「**Plan document:** Save the implementation plan to `tasks/plan.md`.」
`:150`：「**Never overwrite an incomplete plan.**… Unchecked tasks may be mid-build in another session.」
`:161-164`：默认 `tasks/todo.md` 勾选式清单；项目可指定外部 tracker，此时 plan 里只留 tool ID/链接索引。
`skills/spec-driven-development/SKILL.md:210-217`：「Keeping the Spec Alive / Update when decisions change … Commit the spec … Reference the spec in PRs」
→ **形态**：spec + plan + todo 三件，路径固定、版本库内、活文档；**寿命由项目决定（可 merge 前删/ignore）**；**防冲突**：不许覆盖别人未完成的计划。

**G1.3-02 · 跨会话交接靠文件，不靠对话**
`docs/getting-started.md:181`：「a fresh session per phase (spec → plan → build → review) keeps context focused — what carries the work forward is the approved files, not the conversation」
`:183-186`：交接前确保文件里有「still-apply 的决定、批准的范围、仍开放的问题、下一个任务、当前验证状态（跑了什么、对什么）」；新会话先读文件与 `git status`；「Don't assume approvals you can't see in the artifacts.」
`skills/context-engineering/SKILL.md:123-135`：「Restartable Session Boundaries … persist: 1. the accepted scope and decisions in the spec or plan; 2. the current task status and the next pending task; 3. the files changed and the working-tree state; 4. the exact verification commands and outcomes; 5. unresolved questions, risks, and required approvals.」`… Do not infer approval from a previous conversation unless the durable artifact records it.`
`docs/getting-started.md:192-194`：每个完成的任务是一个 restartable boundary；`A process exit is not evidence that a task passed, and a restart must not bypass an approval gate.`
→ **"会话里丢、文件里活"被写成清单**：五类必须落盘的信息 + 重入先读文件 + 不得从对话推断批准。

**G1.3-03 · 上下文分层（文档层级的直接答案）**
`skills/context-engineering/SKILL.md:19-27`：五层，从最持久到最临时——1 Rules Files（`CLAUDE.md` 等，项目级常驻）→ 2 Spec / Architecture Docs（按 feature/session 载入）→ 3 相关源码 → 4 错误/测试输出 → 5 对话历史；`:57-60`：「Load the relevant spec section when starting a feature. Don't load the entire spec if only one section applies.」；`:92`「Pre-task context loading:」（读要改的文件、相关测试、仓内相似样例、类型定义）；`:98`「Trust levels for loaded files:」（可信源码/测试/类型；需核实的配置与外部文档；不可信的用户与第三方内容）。
→ 这是**唯一的显式文档分层模型**：规则 > 规格/架构 > 源码 > 运行输出 > 对话；并给每层的信任级别。

**G1.3-04 · 质量门禁文件（防腐的数值部分）**
`skills/constraint-driven-development/SKILL.md:12`：「This skill produces something different: a written record of **this project's** bar, with numbers, that outlives the conversation and can be checked mechanically.」；`:16`「Spec-driven development says what to build. Test-driven development proves it works. Constraint-driven development defines what 'good enough to ship' means…」；description（`:3`）：「records everything in `CONSTRAINTS.md`, and watches the diff for a weakened bar — new `@ts-ignore` or eslint-disable suppressions, skipped or deleted tests, assertions stripped out, unimplemented stubs, thresholds edited down」
→ 项目级**长期存活的约束文件**，且有"被悄悄放宽"的检测面。

**G1.3-05 · 评审知识库与账本**
`skills/documentation-and-adrs/SKILL.md:25`：「ADRs capture the reasoning behind significant technical decisions. They're the highest-value documentation you can write.」；`:36`「Match the existing convention first」；`:99`「**Don't delete old ADRs.** They capture historical context.」（生命周期 `PROPOSED → ACCEPTED → SUPERSEDED/DEPRECATED`）
`skills/documentation-and-adrs/SKILL.md:231`（Changelog）/ `:250`（Documentation for Agents：rules files、spec files、ADRs、inline gotchas）。
`evals/skill-impact.md:3`：「This append-only ledger records skill and description changes rejected on eval evidence so contributors can review prior attempts before proposing overlapping work.」
`evals/README.md:38,49`：eval 结果写 `evals/results/`、plugin eval 报告写 `evals/plugin/results/<timestamp>/`，「already gitignored」。
→ ADR/changelog=耐久；eval 结果=重跑可重得，故 gitignore；被否提案=append-only 账本防重复尝试。

**G1.3-06 · 进度=勾选框 + 每个任务一个 commit 边界**
`commands/build.toml:4`：「`/build auto` — … implement every task without stopping between them.」；`:33`「Single checkpoint. Present the full plan and wait for an unambiguous affirmative (e.g. "approve", "go", "yes"). Treat hedged responses ("looks reasonable", "I guess") as NOT approved. This is the only human gate — after approval, run autonomously.」；`:35`「Execute every task in dependency order… make one commit per task so any point is a clean rollback.」
→ 自主执行版的进度纪律：**唯一人门 + 每任务一提交（可回滚边界）+ 状态勾选**。

**G1.3-07 · 仓库自身的 docs 与 onboarding**
`docs/developer-onboarding.md:9-30`（mental model）、`:50-68`（三层验证循环：结构 / 触发与路由 / 行为三层 eval）、`:98`（Pre-PR checklist）；`docs/getting-started.md:61-92`（推荐配置）。→ addy 仓自己维护了 onboarding 文档（**三仓中唯一有 onboarding 页的**）。

### G1.4 三仓对照（顺序：形态 / 谁写 / 存在哪 / 活多久 / 更新触发 / 防腐烂）

| 维度 | pstack | matt | addy |
|---|---|---|---|
| 主形态 | 决策台账 TSV + 计划勾选清单 + 编排 store（TSV/JSON/MD） + feature map | 外部 issue tracker（或 `.scratch/` markdown）+ CONTEXT.md + ADR + `.out-of-scope/` + map | SPEC.md + tasks/plan.md + tasks/todo.md + ADR + CONSTRAINTS.md + eval 账本 |
| 谁写 | 执行该轮/该 lane 的 agent；store 内每文件**一个**写者 | 跑该技能的人/agent；triage 写 label 与评论（强制 AI 声明） | 各阶段技能写各自件；plan 归属"当前会话" |
| 存在哪 | 工作目录或 agent store（`orchestrate/<slug>/`、`docs/`） | 项目仓（`.scratch/`、`docs/adr/`、`docs/agents/`）或外部 tracker | 项目仓固定路径（`tasks/` 等），或外部 tracker |
| 活多久 | 台账默认本地、需要 trail 才提交；编排 store 保留作 postmortem；resume note 在 `/tmp` | tracker/ADR/`CONTEXT.md`/`.out-of-scope/`=长期；handoff 与架构评审 HTML=OS temp；wizard=ephemeral | spec/plan/todo=活文档，可 merge 前删或 gitignore；ADR/changelog=长期；eval 结果=gitignore |
| 更新触发 | 每决策/每轮循环/每 drain/30 分钟 tick | triage 与实现时即时改状态；决定落定即写 ADR/词汇表 | scope 或决定变化；每个任务边界；任务勾选 |
| 防腐烂 | append-only + 追写覆盖 + 独立会话回核 + 跨模型复审；`status.md` 派生重算 | 规格/工单**禁写路径与行号**；文档与技能同改；router 同步；ADL "不许覆盖未完成计划" | plan/spec 活文档化 + "不许覆盖未完成计划" + 门禁带命令与豁免到期日 + 被否提案 append-only |

### G1.5 G1 的"三仓无此法"

1. **三仓都没有**"某个角色的所有交接物统一落在某目录 / 由某角色保管 / 有统一保留期"的**中央文档制度**；每份记录各自由产出它的技能定义位置与寿命（pstack 是唯一明写"local vs commit"判据的）。
2. **三仓都没有**把"过程记录"和"工作现场"做**统一分类**并规定哪类必须保全的文件——最接近的是 pstack 的「evidence 与 cleanup 分离」（`create-verification-skill/SKILL.md:31`）与 addy 的「restartable boundary 五类必落盘」（`context-engineering:123-135`）。
3. matt 的 `docs/` 是**发布给人看的技能说明页**（`CLAUDE.md:17`），不是"会话产物归档层"；三仓都没有"会话产物归档层"这一概念。

---

## G2 · `feature map`（pstack 专项）

### G2.1 它是什么

- **G2.1-01 · 定义与结构**：`skills/create-verification-skill/SKILL.md:36`：「Create `.cursor/skills/verify-<app>/features/README.md` plus one file per user-facing feature you can identify (aim for the top 3-5 to start, from routes, commands, menus, or docs)… with a README index and one file per feature. Each file answers, from the user's point of view: what the feature is, how to reach it, how to drive it with the harness, and what observable end state proves it works. The four H2s are `Sub-features`, `How to get to it (user POV)`, `Driving it with <harness>`, and `Gotchas`. **The map is the repo's maintained verification source; a proof that drives one convenient entry point is incomplete when the map lists others.**」
- **G2.1-02 · 每个 feature 文件的契约**：`skills/create-verification-skill/references/feature-map-example/README.md:33-42`：「Feature entry contract… starts with an H1 title and one paragraph describing the user-visible behavior. It then uses exactly four H2 sections in this order. 1 `Sub-features`… 2 `How to get to it (user POV)`… 3 `Driving it with <harness>` starts with `Preconditions:`… 4 `Gotchas`…」「Keep implementation details out of the map. Name only user paths, stable handles, required state, commands, and observable proof.」
- **G2.1-03 · README 索引的固定段**：同文件 `:5-44`：Baseline preconditions（`:5`）/ Driving conventions（`:14`）/ Proof and skip reporting（`:23`，含「Record the feature ID and entry point used with every artifact」「Do not report a skipped entry point as verified through a different path」）/ Feature entry contract（`:33`）/ Features 列表（`:44`）。
- **G2.1-04 · 谁产**：`docs/guide/06-verify-and-ship.md:35-37`：「`/create-verification-skill` interviews the repository, not you… It writes `.cursor/skills/verify-<app>/`… plus a feature map under `features/` that indexes what the app does and what result proves each feature works.」——产者=生成验证技能的 agent，做法是**访谈代码库而不是人**。
- **G2.1-05 · 何时冻结 / 交付门**：`create-verification-skill/SKILL.md:38-40`：「Prove the generated skill before handing it over … Run its own instructions end to end once: launch, doctor, drive ONE mapped feature …, capture evidence, clean up. After cleanup, confirm the evidence still exists at the named location… **A generated skill that was never executed is a draft, not a deliverable.**」；`docs/guide/06-verify-and-ship.md:37`：「If that proof fails, don't use the output.」
- **G2.1-06 · 谁维护 / 何时维护**：`docs/guide/06-verify-and-ship.md:45-51`：「Apps change and feature maps rot. When yours drifts, run `/maintain-verification-skill`… It ends in exactly one of three outcomes. `clean`… `changed`… `blocked`… It never edits product code.」；`create-verification-skill/SKILL.md:44`：「Point the user at `/maintain-verification-skill`… **Suggest a cadence only if they ask.**」→ 无固定周期，由人触发。
- **G2.1-07 · 腐烂的处置**：`skills/maintain-verification-skill/SKILL.md:9`：「A feature map rots the moment the app changes. This skill is the upkeep loop… The unit of rigor is the feature, not every sentence」；`:21`「Only edit the verification skill's own directory (its SKILL.md, features/, and any harness scripts it owns). **Never edit product code during a run**: a behavior the map describes that the app no longer does is either doc drift (fix the map) or a product regression (report it, don't paper over it in docs).」；`:29`「One read-only subagent per feature file … Children never drive the app and never edit files.」；`:33`「Live pass. Required even when source looks clean.」
- **G2.1-08 · 缺了会怎样（fail-closed）**：`automations/benny/skills/reproduce-and-fix-issues/SKILL.md:11`：「If the config, required actions, control adapter, or completed feature map is missing, fail closed.」；`references/control-adapter.md:9`：「If the skill, feature map, or a required capability is absent, ambiguous, or incomplete, repro and fix work must fail closed.」；`SKILL.md:130`：「If no section covers the feature, **mark the run blocked instead of inventing a path or selector**.」
- **G2.1-09 · 它在文档层级里的位置**：载体是 `.cursor/skills/verify-<app>/features/`（`create-verification-skill/SKILL.md:36`）——即**项目内、面向 agent 的验证技能目录**，不是产品文档、不是 spec。benny 版本进一步要求把它放到 **pack 之外的用户自有位置**：`automations/benny/skills/setup-benny/SKILL.md:28`「Keep user-owned configuration, feature maps, and routing maps outside the destination. Never overwrite them.」；`references/feature-map.example.md:5`「Copy this file outside `.cursor/automations/benny/`, for example to `.cursor/benny/feature-map.md`, and set `control.feature_map_path` to the copy. **Pack refreshes must not overwrite it.**」；`setup-benny/SKILL.md:86`「Fill one feature-map section for every user-facing feature the automation may reproduce. Keep it at the user point of view. Do not freeze implementation details or current code paths in the map.」
- **G2.1-10 · 与验证账/分工的接法**：`docs/guide/06-verify-and-ship.md:41`：「Once the verify skill works, a `/swarm` can split a full pass by feature-map entry and aggregate the results.」

### G2.2 matt / addy 的对应物

| 仓 | 有无 feature map | 最接近的对应物（file:line + 说明） |
|---|---|---|
| pstack | **有** | 上述 `.cursor/skills/verify-<app>/features/`（G2.1） |
| matt | **无同一物** | ① spec（`to-spec`，用户故事 + `Testing Decisions`，`to-spec/SKILL.md:59`）；② ticket 的验收清单（`to-tickets/SKILL.md:38`「blocking edges」+ 模板里的 `- [ ] Acceptance criterion`）；③ `wayfinder:map`（决策索引，非行为清单，`wayfinder/SKILL.md:21-23`）；④ `code-review` 的 Spec 轴在 `docs/`、`specs/`、`.scratch/` 找 spec 文件（`code-review/SKILL.md:31`）。**没有"按用户可见功能一份文件 + 可驱动 + 可证明"的清单。** |
| addy | **无同一物** | ① **capability map**：模块表 + 构建顺序，稳定 kebab-case id（`spec-driven-development/SKILL.md:44-60`）——是"能力/模块索引"，但不含用户入口/驱动方法/证明；② `evals/cases/<skill>.json` 的 `expectations[]`：**每个技能一份行为期望清单 + trigger 正负例 + 可运行 runner**（`evals/README.md:29-38`）——是"行为清单+验证器"的最近亲，但对象是技能而不是产品功能；③ 六份 `references/*-checklist.md`（DoD/无障碍/性能/安全/可观测性）是**横切检查表**，不是功能索引；④ evals 的 `skill-impact.md` 记录被否变更。 |

**结论（G2）**：feature map 的不可替代点有三个，三仓其余做法都没有同时具备：**(a) 以"用户可见功能"为分割单位；(b) 每项自带"怎么到、怎么驱动、什么读数算证明"；(c) 有配套的 maintain 循环 + 缺失 fail-closed。** matt 的 spec/ticket 是"要交付什么"，addy 的 capability map 是"模块怎么分"，两者都不回答"这个已经存在的功能怎么被再次证明还活着"。

---

## G3 · 三仓怎么限制"某个角色能写什么"

### G3.1 pstack（最成体系）

- **G3.1-01 · 任务卡按路径白/黑名单**：`skills/poteto-mode/playbooks/orchestrate.md:40`：「SCOPE　　paths this unit may write; paths it may not; its exclusive worktree or branch」；`:46`「FORBIDDEN　no gt, no rebase, no force-push, no fixes outside scope, plus unit-specific bans」；`:17`「One writer per worktree or branch」。
- **G3.1-02 · 每 worker 独立可写产物**：`skills/swarm/SKILL.md:26`：「Give each worker its own writable output when it writes.」
- **G3.1-03 · 角色级不写产品代码（身份不同、粒度不同）**：
  - 协调者：`orchestrate.md:13`「Coordinator (this chat) … **It never authors or edits code.**」；`:66`（close）保留 store。
  - 只读探源：`maintain-verification-skill/SKILL.md:29`「One read-only subagent per feature file … Children never drive the app and never edit files.」
  - 验证者：`orchestrate.md:89`「A verifier overrides it on the same key.」+ G1.1-04 `ledger.tsv` 由其写行。
  - 评审 agent：`agents/comment-sicko.md:30`「I touch comments and identify refactor targets. **I never write application code.**」
- **G3.1-04 · 维护者的写范围被限定在"自己那套东西"**：`maintain-verification-skill/SKILL.md:21`：「Only edit the verification skill's own directory (its SKILL.md, features/, and any harness scripts it owns). **Never edit product code** during a run」；`:11`三态产出之一 `changed`「one PR of proven corrections, confined to the verification skill's own directory」。
- **G3.1-05 · 临时空间与证据空间分开，且清理不碰证据**：`create-verification-skill/SKILL.md:31`：「Cleanup removes instances and scratch state, **never the evidence**: proof artifacts survive the teardown, in a location the skill names.」；`:28` doctor 是「one read-only check」；`:36` 生成物可创建"clearly marked as verification scaffolding"的缺失资源并在 cleanup 移除。
- **G3.1-06 · 共享状态：一个写者 + 派生视图只由工具写**：`orchestrate.md:23`「Every file has exactly one writer.」；`:32` `status.md` 由脚本从 TSV 重算、`never hand-maintained`。
- **G3.1-07 · 日志/台账：只准追加**：`show-me-your-work/SKILL.md:52`「Append-only… Never edit or delete history.」；`:63`「The audit never edits or removes a row, even an invented one.」；`swarm/SKILL.md` 报告用固定三态 `PASS`/`ISSUES`/`BLOCKED`（`scripts` 之外的 Phase B）。
- **G3.1-08 · 没有权限就没有动作（fail-closed 姿态）**：`figure-it-out`（经 SOURCES 引：不可逆动作需确认）之外，最直接的是 `orchestrate.md:111` 的 gate 机制与 `maintain` 的 `blocked` 产出。

### G3.2 cursor-plugins 其他插件（同 clone）

- **G3.2-01 · orchestrate：角色=写权的边界**：`orchestrate/skills/orchestrate/SKILL.md:22`：「**Planners own scopes and publish tasks. They do no coding.** Writing `plan.json`, reading handoffs, and deciding what's next are planner work. Editing files, running `git merge`, and fixing conflicts inline are not.」；`:24`「**Workers are isolated.** One task, one clone of the repo, no channel to any other agent. One handoff when done.」；`:27`「**Propagation, not synchronization.** No cross-talk between siblings. No shared state between levels.」
- **G3.2-02 · 提示词模板把写权写成三段**：`prompts/worker.md:11-14`：「Paths you may MODIFY (read any file in the repo): {{allow}} / Do NOT modify: {{forbid}}」；`:21`「Push exactly `{{branch}}` and report it in your handoff.」；`prompts/verifier.md:34-36`：「Do NOT modify target source files. / Do NOT merge, rebase, or open a PR. The planner owns integration. / **Your branch is never merged back**; the planner reads your handoff and decides follow-ups.」；`:32`「Commit verifier artifacts (repro scripts, audit notes, log captures if useful) to the branch already checked out」。→ 验证者**可以写自己的证据**，但只能写在自己的分支上，且该分支永不合并。
- **G3.2-03 · 共享状态与配置的写者与门**：`references/planner.md:37-42`：`plan.json`（planner）/`state.json`（脚本）/`handoffs/*.md`（worker 与 verifier 的最终消息，脚本落盘）/`attention.log`（失败与决策）；「Slack is human visibility, not task state.」；`:113`：「Operators outside a run enable operator mode with a current-user-owned `~/.orchestrate/operator-mode` file set to `0600`. Workers are assumed unable to write the operator's OS home directory.」；`:84`「Minimize path overlap. List forbidden paths when sibling ownership matters.」
- **G3.2-04 · 信息流动只有一条管道**：`references/handoffs.md:3`：「Handoffs are the only way information moves between nodes… No shared branch, no status API, no cross-sibling chatter.」；`:5`「The script saves the final message verbatim to `<workspace>/handoffs/<task-name>.md` with a traceability header. Don't enrich or sanitize; the planner needs the worker's words unfiltered.」
- **G3.2-05 · thermos：审查者以 Task subagent 身份只回报告**：`thermos/agents/thermo-nuclear-review-subagent.md:10`「You are a **Task subagent**. The parent agent already collected git output and changed-file contents」；`:24`「Do **not** spawn nested subagents unless the user or parent explicitly asks.」；`thermos/skills/thermo-nuclear-review/SKILL.md:15-16`「# Scope / ONLY report issues related to code that is being ADDED or MODIFIED in this PR.」
- **G3.2-06 · cursor-team-kit：控制面（control-ui/control-cli）与验证技能是分开的技能**（README 技能表），验证/复现通过 harness 驱动，不在产品代码里写探针——细化证据在 SOURCES.md:143 已登记（本仓已吸收其中"先复用仓内驱动面"这一条）。

### G3.3 mattpocock-skills（**没有** role 写权限模型，但有"哪个技能能写哪里"）

- **G3.3-01 · 没有 per-role 写权限声明**：`skills/engineering/code-review/SKILL.md` 全文只规定输出两轴报告（`:43-49`「Present the two reports under `## Standards` and `## Spec` headings… Do not merge or rerank findings」），**没有** tools/写权限字段；`skills/engineering/implement/SKILL.md`（15 行）也没有写权限声明；仓内**不存在** `permissionMode` / `allowed-tools` / `disallowedTools` 这类**角色**权限配置。唯一一处"写限制"是**技能级**的：`skills/in-progress/writing-shape/SKILL.md:11`「Do not edit the raw material file: it is read-only to this skill.」——限制的对象是产物，不是角色。
- **G3.3-02 · 替代机制一：技能作用域本身就是权限**——`handoff` 写 OS temp（`handoff/SKILL.md:8`）、`improve-codebase-architecture` 写 OS temp（`:39`）、`wizard` 默认 scratch 且做完删（`:12`）、`research` 写"仓库已有放笔记的地方"（`research/SKILL.md:3`）。**能力即权限**：技能规定的产物位置就是它的写范围。
- **G3.3-03 · 替代机制二：对共享状态（tracker）有显式写条件**：`triage/SKILL.md:13-16`（写评论必须带 AI 声明）；`:83`（已实现者**不许**写 `.out-of-scope/`）；`OUT-OF-SCOPE.md:86`（仅"被拒的增强"才写；`Update or removing` 一节规定改主意要删文件）；`to-tickets/SKILL.md:67`：「Do NOT close or modify any parent issue.」
- **G3.3-04 · 替代机制三：并发写者靠 worktree/branch 隔离 + 单一 merge 者**：`skills/in-progress/implement-spec/SKILL.md:25`「Each implementer subagent should work in its own worktree, on its own branch.」；`:27`「merge its work to the PR branch with a **merger subagent**」；`:21`「Ensure the exploration subagent can save files - it should save its markdown notes in a directory outside the repo, accessible by all future subagents.」
- **G3.3-05 · 替代机制四：判断与实现分离写进文档而不是权限**：`skills/in-progress/retro/SKILL.md:33`「The review agent has the least context pressure - it receives a diff, so no exploration needed.」；`:35`「the review agent should be responsible for imposing coding standards, not the implementation agent.」
- **结论**：matt **不按角色限制写权限**；它把"谁能写什么"降为**技能的产物约定 + 外部 tracker 的写条件 + worktree 隔离**，并用「不读作者叙述、独立判断」的流程约束代替权限约束。

### G3.4 addyosmani-agent-skills（**没有** role 写权限模型；有"工具/作用域"粒度）

- **G3.4-01 · personas 没有写权限字段**：`agents/code-reviewer.md`、`security-auditor.md`、`test-engineer.md`、`web-performance-auditor.md` 的 frontmatter 只有 `name`/`description`（`agents/code-reviewer.md:1-3` 等），无 `tools`/`disallowedTools`；`references/orchestration-patterns.md:164`：「Plugin subagents do **not** support the `hooks`, `mcpServers`, or `permissionMode` frontmatter fields — these are silently ignored.」→ 插件形态下**权限字段根本不可用**。
- **G3.4-02 · 替代机制一：只读/写入由平台内置 subagent 类型区分**：`references/orchestration-patterns.md:156`：「`Explore` | Read-only codebase search and analysis. Use this for Pattern 5 (research isolation).」「`Plan` | Read-only research during plan mode.」「`general-purpose` | Multi-step tasks needing both exploration and modification.」；`:130-140`（subagents vs teammates 表）：「Sub-agents see | The same diff, different lenses」「Main agent fans out, sub-agents only report back」。
- **G3.4-03 · 替代机制二：执行 eval 用显式 permission mode**：`evals/README.md:38`：「The executor runs with an explicit permission mode (`--permission-mode acceptEdits` plus a pre-approved tool list) so execution evals can genuinely edit files…」
- **G3.4-04 · 替代机制三：把"写范围"写成技能规则/钩子**：
  - `skills/incremental-implementation/SKILL.md:115-130`：「Rule 0.5: Scope Discipline … NOTICED BUT NOT TOUCHING: - src/utils/format.ts has an unused import (unrelated to this task)」；
  - `skills/code-simplification/SKILL.md:103`：「Default to simplifying recently modified code. Avoid drive-by refactors of unrelated code unless explicitly asked to broaden scope.」；`:317`「Refactoring code outside the scope of the current task without being asked」列为红旗；
  - `hooks/SIMPLIFY-IGNORE.md:3-19`：`simplify-ignore-start/end` 标记的块**模型根本看不到**（PreToolUse 备份 + 替换为占位符），是"物理屏蔽写范围"的最强形式；
  - `commands/build.toml:31`：「Stage only the files that task touched plus its task-status update — never `git add -A` blindly」。
- **G3.4-05 · 替代机制四：不许削弱检查（对"负向写"的限制）**：`skills/constraint-driven-development/SKILL.md:3`：检测「new `@ts-ignore` or eslint-disable suppressions, skipped or deleted tests, assertions stripped out, unimplemented stubs, thresholds edited down」。
- **结论**：addy **不按角色限制写权限**；替代机制是**平台内置只读 subagent 类型 + 显式 permission mode + 技能内的范围纪律 + 钩子级物理屏蔽**。

### G3.5 五类写权 × 三仓对照

| 类别 | pstack | matt | addy |
|---|---|---|---|
| 产品实现代码 | 只有 implementer/worker 在 SCOPE 白名单内可写；coordinator/verifier/reviewer 一律不写 | implementer 可写；reviewer 只出报告；无权限字段，靠技能定位 | 实现技能可写；reviewer personas 只出报告；Explore/Plan 只读内置类型 |
| 自己的交付物/报告 | 明写：worker 写 handoff、verifier 写 verdict handoff/ledger 行、维护者写自己目录内文件 | 明写：triage 写 label/评论（带 AI 声明）、to-spec/to-tickets 写 tracker、research 写笔记文件 | 明写：各技能写各自件；eval 写 results（gitignore） |
| 临时探针/实验 | 临时空间可写，**新依赖不许加**；cleanup 只清 scratch **不清 evidence** | handoff/HTML 写 OS temp；wizard scratch 后删；调研笔记仓外 | `NOTICED BUT NOT TOUCHING`；eval 显式 perm mode；`simplify-ignore` 物理屏蔽 |
| 共享状态/配置 | 每文件一个写者；`status.md` 由脚本重算；standing orders append；operator-mode 文件 0600 门 | tracker 写条件受限（不许关父 issue、不许写已实现的 `.out-of-scope/`）；单一 merger | 单一 checkpoint 批准、唯一人门；tasks/todo 归属"当前 plan" |
| 日志/记录 | append-only 台账；错误动作**只许追写覆盖**；verdict 账按 PR+SHA keyed，新 head 作废旧行 | `.out-of-scope/` 追加 prior requests；triage 评论自报 AI | eval 结果可再生成故 gitignore；skill-impact 账 append-only |

### G3.6 G3 的"三仓无此法"

1. **三仓都没有**"按**角色名**授予/禁用写权"的机制（没有 ACL、没有 capability 表）。pstack 与 cursor orchestrate 用的是**任务卡里的路径白/黑名单 + 单一写者 + 只读子代理**；matt/addy 完全没有权限层。
2. **三仓都没有**"reviewer 绝对不许写"这种笼统禁令的等价物；相反，pstack/orchestrate 明确**要求** verifier 写它自己的证据与 verdict，只禁止它改目标源码、合并、开 PR（`prompts/verifier.md:34-36`）。**"禁止写"必须按类别拆分，这一点上三仓一致。**
3. **三仓都没有**"日志只能追加"这一条之外的日志权限分级（例如"谁能删旧日志"）；pstack 的 append-only 是唯一的日志写纪律，且它以"追写覆盖"解决错误。

---

## G4 · 四套开发模式：权威解释、工程 practice、归哪个角色

> 说明：**BDD/TDD/DDD 的权威解释不在三仓**（三仓只提供工程实践切片）；SDD 在三仓有实践（pstack `/architect`、matt `to-spec`、addy `spec-driven-development`），但权威定义在外部。以下每条区分「外部权威」与「三仓原文」。

### G4.1 BDD · Behavioral Driven Development

**权威解释（外部来源）**
- Dan North《Introducing BDD》（2006-09-20, https://dannorth.net/blog/introducing-bdd/）：起源是 TDD 教学问题；「My response is behaviour-driven development (BDD)… designed to make them [agile practices] more accessible and effective for teams new to agile software delivery. Over time, BDD has grown to encompass the wider picture of agile analysis and automated acceptance testing.」；命名模板「The class _should_ do something」；「“Behaviour” is a more useful word than “test”」；「A more subtle aspect of the word _should_ … _Should_ implicitly allows you to challenge the premise of the test: “Should it? Really?”」；失败的三种处置含「The behaviour was no longer correct; the premise of the system had changed. Solution: _Delete the test._」；「BDD provides a “ubiquitous language” for analysis」；「Acceptance criteria should be executable」。
- Dan North《There's more to BDD than evolving TDD》（2006-06-04, 同站）：「BDD is fundamentally about identifying behaviour. At the analysis level, the behaviour of a story is its acceptance criteria」。
- Cucumber 官方文档《Behaviour-Driven Development》（https://cucumber.io/docs/bdd/）：「BDD is a way for software teams to work that closes the gap between business people and technical people by: Encouraging collaboration across roles to build shared understanding of the problem to be solved / Working in rapid, small iterations… / Producing system documentation that is automatically checked against the system's behaviour」；三实践「Discovery, Formulation, Automation」：先谈具体例子、再写成可自动化并求一致、最后「implement the behaviour described by each documented example, starting with an automated test to guide the development of the code.」
- org 级 practice：Given-When-Then / Gherkin 场景（Cucumber 参考文档 https://cucumber.io/docs/gherkin/reference/）。

**归本库哪个角色（含理由）**
1. **Driver（主）**：BDD 的 Discovery 是"与业务方谈出可验收的行为"；本库对应 Driver 的 `task-card.verification` 与 §4.9 的"推进前说明/说完才跨线"。理由：BDD 要求行为来自 stakeholder，而本库唯一能代表 Owner 定"行为该是什么"的角色是 Driver（`roles/driver.md:8-12`、`:44` `verification` 字段；`pipeline.md:120-128` 授权检查）。证据：`roles/driver.md:68`「判据必须能判否…一组可判否的正/反对照」=「Acceptance criteria should be executable」的本库写法。
2. **Planner（主）**：把行为切成可验证的片，每条判据必须能判否（`roles/planner.md:136-153` §4.6）。理由：BDD 的"自动化验收"在角色分工里就是 Planner 的 `verification` 字段；BDD 说"一个句子只能描述一段行为"⇒切片粒度纪律。
3. **Implementer（主）**：行为先行（`roles/implementer.md:107-110` §4.2「行为先行：红—绿—重构」）与 §4.3「反同义反复」（`:124`）。理由：BDD 的 Automation 就是"先写能表达该行为的自动检查"。
4. **Reviewer（副）**：BDD 的 `should` 用于**挑战前提**；本库对应 §4.5「反实现挑战：判据真的能抓住错误实现吗」（`roles/reviewer.md:170-176`）。理由："Should it? Really?" 是审查动作，不是实现动作——判定"行为本身是否仍成立"必须由没写代码的人做。
5. **Verifier（副）**：BDD 的"documentation automatically checked against behaviour"对应"真实入口 + 三态结论"（`roles/verifier.md:41-50`）。

### G4.2 TDD · Test Driven Development

**权威解释（外部来源）**
- Martin Fowler《Test Driven Development》bliki（2023-12-11 更新, https://martinfowler.com/bliki/TestDrivenDevelopment.html）：「Write a test for the next bit of functionality you want to add. / Write the functional code until the test passes. / Refactor both new and old code to make it well structured.」；「there's also a vital initial step where we write out a list of test cases first」；「thinking about the test first forces us to think about the interface to the code first」；「The most common way that I hear to screw up TDD is neglecting the third step.」
- Kent Beck《Canon TDD》（https://newsletter.kentbeck.com/p/canon-tdd）：5 步含「Optionally refactor to improve the implementation design」。
**三仓工程 practice**（本库已吸收的部分）
- `pstack/skills/tdd/SKILL.md:9-30`：只在有「clear, cheap test path」时做；「Do not force a test when it would be impractical.」「Prefer no new test over a bad test.」；`:28-31` Guardrails：「Do not change tests merely to match a wrong implementation.」「Do not weaken existing assertions unless the expected behavior has genuinely changed and the reason is clear.」
- `addy/skills/test-driven-development/SKILL.md:10`「Write a failing test before writing the code that makes it pass. For bug fixes, reproduce the bug with a test before attempting a fix. Tests are proof — 'seems right' is not done.」；`:51`「Write the test first. It must fail. A test that passes immediately proves nothing.」；`:96` Prove-It 模式；`:24-37`「Discover the Stack First… Never assume a default like `npm test`」。
- `matt/skills/engineering/tdd/SKILL.md:36-38`：红在绿前、一次一片；**「Refactoring is not part of the loop… belongs to the review stage」**（本库在 `SOURCES.md:306-313` §4.5 明确不采纳这一条，采纳 addy 的"重构在循环内"）。
- 本库已吸收：`implementer.md:107-140`（行为先行 + 反同义反复）、`:161-179`（先复现再修）、`investigator.md:49`（先建反馈回路）、`planner.md:136-153`（验证位置）、`reviewer.md:170`（反实现挑战）、`verifier.md:49`（变异/反例）。
- **本仓历史载体（已归档）**：`docs/archive/skills/behavioral-tdd/SKILL.md:3-16`（description「行为驱动垂直切片测试先行技能，在接缝处断言可观测行为，坚决消灭同义反复测试与假绿」；正文「融合了 Matt Pocock 的垂直切片与接缝测试理论，以及 `pstack` 的"测试行为而非实现细节"硬指标」）。→ BDD/TDD 的合并簇在本仓**曾以技能形式存在**，现以 `implementer.md §4.2/§4.3` 的形式存活，属于"认出来归位"而非新造。

**归本库哪个角色**
1. **Implementer（主）**：`roles/implementer.md:107` 就是 TDD 的红—绿—重构，且 `:217` 算做完要求「`self_verification` 里包含'预期会红的那一次'」。
2. **Investigator（主，缺陷路径）**：`roles/investigator.md:49-67` §4.1「先建反馈回路，再谈原因」；`:76`「把最小场景保存下来，它就是后面要交给实现方的回归测试本体」。理由：Beck/Fowler 的 bug loop 与 Investiggator 的 repro_command 是同一件事，只是本库把它从"测试文件"泛化为"能判红的命令"。
3. **Planner（副）**：定接缝与判据（`roles/planner.md:136-153`；Fowler「thinking about the test first forces us to think about the interface first」的接缝面）。
4. **Verifier（副）**：TDD 的绿色只证明"实现能满足写下的测试"；要做到"测试本身能抓住错误实现"需要 verifier 的变异/反例（`roles/verifier.md:49` `falsification`）与 reviewer 的反实现挑战（`reviewer.md:170`）。**这条分工是本库相对三仓的加强项。**

### G4.3 DDD · Domain Driven Design（注意：标准术语是 Design，不是 Development）

**权威解释（外部来源）**
- Eric Evans《Domain-Driven Design》（2003），经 Martin Fowler 概述（https://martinfowler.com/bliki/DomainDrivenDesign.html）：「Domain-Driven Design is an approach to software development that centers the development on programming a domain model that has a rich understanding of the processes and rules of a domain… to develop software for a complex domain, we need to build Ubiquitous Language that embeds domain terminology into the software systems that we build… DDD stresses doing them in software, and evolving them during the life of the software product.」「A particularly important part of DDD is the notion of Strategic Design - how to organize large domains into a network of Bounded Contexts.」
- Fowler《Ubiquitous Language》（https://martinfowler.com/bliki/UbiquitousLanguage.html）：「the practice of building up a common, rigorous language between developers and users. This language should be based on the Domain Model used in the software - hence the need for it to be rigorous, since software doesn't cope well with ambiguity. / Evans makes clear that using the ubiquitous language in conversations with domain experts is an important part of testing it… the language (and model) should evolve as the team's understanding of the domain grows.」
- Fowler《Bounded Context》（https://martinfowler.com/bliki/BoundedContext.html）：同一词在不同上下文有不同模型，边界要显式。
**三仓工程 practice**
- matt `skills/engineering/domain-modeling/SKILL.md:40`「Create files lazily: only when you have something to write…」；`:66`「Offer ADRs sparingly」+ 三条件；`ADR-FORMAT.md:3`（`docs/adr/` 顺序编号）；`setup-matt-pocock-skills/SKILL.md:59`（默认 single-context：`CONTEXT.md` + `docs/adr/`，多上下文才用 `CONTEXT-MAP.md`）。
- pstack `skills/principle-model-the-domain/SKILL.md`（本轮按 `SOURCES.md:138` 标为"删除（本轮），未读全文"——**本轮无可用原文引用**）。
- 本库已吸收（`SOURCES.md:180` 登记为"局部吸收（改写）"）：术语冲突摊开、canonical 化、ADR 三条件；**改写点**：裁定权与写权分开（Owner 裁业务含义，Architect 只查证/备选/记录）。
- 本库落点：`roles/architect.md:201-217` §4.9（`:209`「业务含义的**裁定权 = 项目 Owner 本人**，或 Owner 书面指定/明确授权的业务角色…工程侧…不得擅自决定」）；`architect.md:210`（新建词汇表需 Owner 同意且先映射既有权威文档）；`investigator.md:95`（保留原症状用词、冲突并列不替它选义）；`planner.md:107`（未决词义不得由切片定名）；`reviewer.md:142`（领域词义冲突报为阻断并指向有权裁定者）。

**归本库哪个角色**
1. **Architect（主）**：DDD 的 Ubiquitous Language/模型 ↔ `architect.md §4.9` 与 §4.3「数据形状先行，不变量尽量编码进类型」（`:99`）。理由：DDD 的模型是**设计产物**，本库唯一产出设计契约的角色是 Architect；但裁决权在 Owner（本库硬边界，见下）。
2. **Owner / Owner 授权的业务角色（决定性角色，不属于十个工程角色）**：`roles/architect.md:209` 明确业务含义不得由工程角色裁定。DDD 的"domain expert should object"在本库的实现是"Owner 裁"——**这是本库对 DDD 的一处主动改写**（`SOURCES.md:180` 已登记）。
3. **Investigator（供料）**：`investigator.md:84-103` 真实路径追踪 + `:104`（历史意图考古）+ `:95`（原话保留），为模型边界提供一手用词。
4. **Reviewer（守门）**：`reviewer.md:142` 把词义冲突判为阻断。
5. **Bounded Context 在本库没有对应角色/产物**：本库没有"限界上下文/上下文映射"这一层（`SOURCES.md:180` 只吸收了 CONTEXT/ADR 的写法，没有吸收上下文映射）；`docs/archive/skills/interface-and-boundary-design`（旧载体）也不含 Bounded Context。→ 见 G5 缺口。

### G4.4 SDD · Spec Driven Development

**权威解释（外部来源）**
- GitHub Spec Kit README（https://github.com/github/spec-kit）：「## Spec-Driven Development / Define **what and why** before deciding **how** to build it. SDD turns your requirements into a specification, a technical plan, and actionable tasks, then guides implementation against those artifacts. / **Constitution once per project; specify → plan → tasks → implement → converge per feature.**」
- Kiro（AWS）文档《Specs》（https://kiro.dev/docs/specs/）：每个 spec 三步 `Requirements → Design → Tasks`，一个 markdown/步；requirements 用 "As a…" 用户故事 + `GIVEN… WHEN… THEN…` 验收（转述自 Fowler 文章，见下）。
- Birgitta Böckeler / martinfowler.com《Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl》（https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html）：三级分类「**Spec-first**: A well thought-out spec is written first… / **Spec-anchored**: The spec is kept even after the task is complete, to continue using it for evolution and maintenance… / **Spec-as-source**: The spec is the main source file over time…」；「A spec is a structured, behavior-oriented artifact - or a set of related artifacts - written in natural language that expresses software functionality and serves as guidance to AI coding agents.」；并给出关键警告「the term 'spec-driven development' isn't very well defined yet」、导入既有代码库更难、文件冗长难审。
**三仓工程 practice**
- addy `skills/spec-driven-development/SKILL.md:22-33`（四阶段 gated workflow + 每阶段人工 review）、`:44-60`（Phase 0 capability map：module id 表 + 依赖方向 + build order；「Stable module ids… chosen once, never renamed mid-initiative」）、`:110-138`（spec 六核心区：Objective / Commands / Project Structure / Code Style / Testing Strategy / Boundaries〔Always·Ask first·Never〕）、`:150-153`（已有 OpenSpec 就用它的格式，不造第二份 `SPEC.md`）、`:210-217`（活文档）、`:239-250`（Red flags / Verification checklist）。
- addy `commands/build.toml:30`：`/build auto` 只认已知路径的 spec（`SPEC.md`、`docs/SPEC.md`、`spec/*`）——「A README or arbitrary doc does NOT count. If none exists, stop and tell the user to run /spec first — do not invent requirements.」（**fail-closed 的 SDD**）
- matt `skills/engineering/to-spec/SKILL.md:3`（只综合、不重新访谈）、`:19`（发布到 tracker）、`:55`（禁写路径与代码片段）；`code-review/SKILL.md:29-31`（Spec 轴：从 commit 引用/tracker/`docs/`·`specs/`·`.scratch/` 找 spec）；`wayfinder`（先定 destination，再问 frontier）。
- pstack `skills/poteto-mode/playbooks/multi-phase-plan.md:3`（plan 是交付物、operator 按证据审计）、`docs/guide/06-verify-and-ship.md:7-20`（先把 finish condition 写进第一条 prompt）。
**本库已有的影子**：`architect.md §3 design-proposal`（含 `alternatives` 与 `bound_contract`，即"冻结契约"）、`planner.md §3 slice-plan`、`pipeline.md §3.2`「接口冻结」、`closure.md` 字段闭环、`identity.md`（对象身份的固定序列化）、`driver.md §3 task-card`（`goal` `scope` `verification` `authorization`）。

**本仓历史里已裁过一次同一个问题**：`docs/TIM-PROFESSIONAL-WORKFLOW-PROPOSAL.md:203-205` 把“规格驱动 vs 代码即规格”列为五大冲突之一，当时的裁决是「动态厚薄路由：小修局部走薄配方，跨边界大改走厚规格；支持运行中自动升级厚度并隔离试验」——即**按风险决定要不要写厚规格**。现载体的对应物是 `pipeline.md §2 装配档位`（按项目成熟度 × 变更风险选档，不按文件数）与 `closure.md` 的“可跳过条件”。→ SDD 的规模门槛问题在本仓**已有一次裁决记录**，新裁决必须与它对齐或显式推翻。

**归本库哪个角色**
1. **Architect（主）**：`design-proposal` 就是本库的 spec 层；其 `caller_usage` 先于 type 草案（`architect.md:82`）对应 SDD 的"先 what/why 后 how"。
2. **Planner（主）**：spec → tasks 的分解（`planner.md §3`）与 SDD 的 Phase 2/3 同构；本库把 SDD 的"每个 task 有验收与验证步骤"落成 `slice-plan.verification`。
3. **Driver（主）**：本库的"每批一份 task-card"= SDD 的 constitution/批次契约；授权检查（`pipeline.md §10`）是 SDD 没有的层。
4. **Verifier/Reviewer/Integrator（守约者）**：`closure.md` 的字段闭环 + `identity.md` 的 base/tree 绑定，使"实现是否按 spec 走"可核对（这一层比三仓的 SDD 更硬：三仓没有对象身份绑定）。
5. **本库当前处在 SDD 的哪一级**：证据上属于 **spec-first + 局部 spec-anchored**——`design-proposal` 与 `slice-plan` 是每批冻结的契约（`pipeline.md §6 写窗`），但本库**没有**"spec 作为长期活文档"的载体（无 `docs/specs/`、无 spec 生命周期字段），所以不是 Böckeler 定义的 spec-anchored/spec-as-source。`SOURCES.md:253` 也登记过 addy 的 `spec-driven-development` 为 NOT ABSORBED。

### G4.5 四套之间的重叠与冲突（含与本库纪律的冲突）

1. **BDD ⊃ TDD 的立场冲突：删测试 vs 不许削弱检查**。Dan North（外部）明说前提变了就 **Delete the test**；本库 `roles/implementer.md:203`「我不可以：…为了让检查变绿而削弱检查」。→ 冲突真实存在；本库的消解路径是**改判据必须回 Planner/Architect（`planner.md:136`、`reviewer.md:186`），不由实现者自行删**。**这一条需要 reviewer 显式确认本库的做法是否覆盖了 BDD 的合法删测试场景。**
2. **TDD（matt 版：重构在循环外）vs TDD（addy/Fowler：重构在循环内）**：本库已单选（`SOURCES.md:306-313`，采纳 addy，理由是"审查者不改实现"的角色边界）。→ 已有裁决，无需重裁。
3. **TDD vs SDD 的顺序冲突**：TDD 主张"测试驱动接口设计"（Fowler 引文），SDD 主张"先写规格再定任务"。本库把两者拆到不同角色（Architect/Planner 出契约，Implementer 在契约内做测试驱动），**冲突在本库已被角色边界吸收**；但存在一处未裁决点：**当 Implementer 的测试暴露出契约本身有问题时，谁有权改 `slice-plan.verification`**（现规则：回 Planner，见上文）。
4. **SDD 内部（spec-first vs spec-anchored/spec-as-source）本身未定义**：Böckeler 原文即指出术语"isn't very well defined yet"，且观察到"spec 冗长难审""对 brownfield 更贵""SDD≠TDD/BDD"。→ 本库若引入 SDD，必须显式选择级别与规模门槛，不能照搬工具形态。
5. **DDD 的模型演化 vs 本库的冻结契约**：DDD 要求语言随理解演化（Fowler 引 Evans）；本库 `pipeline.md §6` 要求候选冻结、定向返修=新候选+新冻结。→ 不矛盾（"演化"在本库表现为形成新冻结），但**本库没有"模型/词汇表的演化轨迹"载体**（ADR 只覆盖"难回退决定"，不覆盖词义演化）；属 G5 缺口。
6. **BDD 的"文档自动对着系统行为检查" vs 本库"证据绑定对象"**：三仓的 BDD 实践（Cucumber）靠可执行规格；本库没有可执行规格载体，只有"判据 + 命令"（`planner.md:145`「每一行门禁必须写下'由什么命令判定'」）。→ 本库的机制更重对象身份，更轻"规格即测试"；这是差异性，不是缺陷，但**购买 BDD 的收益需要另一条路径**（feature map 或等价的"行为→驱动→证明"索引，见 G2/G5）。
7. **DDD 的"工程侧不得裁业务含义" vs DDD 的"developer 与 domain expert 共同磨语言"**：本库 `architect.md:209-210` 把裁定权收归 Owner/授权业务角色，工程侧只查证与记录。→ 这是**对 DDD 的收紧**，三仓（matt）默认让 agent 直接写 `CONTEXT.md`；本库明确改写（`SOURCES.md:180`）。谁对需要人裁。

---

## G5 · 对本仓"缺口清单"的独立复核

复核对象：`README.md`、`AGENTS.md`、`pipeline.md`、`closure.md`、`identity.md`、10 份角色文件、`scripts/**`、`docs/**`、`.pi/**`（仅列目录与样例，不当作规范）。

### G5.1 「交接物有一批名字，但没规定落在哪、谁保管、活多久」→ **成立，但需按维度细化**

- 名字与字段确实齐：`pipeline.md:19-27`（0–7 步与按需 Oracle 的收/交表）、`:9-11`（主链）、`:129-152`（机器可读拓扑）；`closure.md:21-33`（字段级相邻校验）。角色 §3 共 21 处 `**产出 …**` 声明（`grep -n "产出 \`" roles/*.md | wc -l` = 21）。
- **没有**任何一条规则规定这些交接物"写到哪里/以什么文件名落地"。全库检索 `存放/落盘/保存位置/目录约定/文件命名`：
  - 只有 `roles/driver.md:207`「接收冻结判据时核**'现在可取回 + 保管到所需时间 + 搬迁有授权'**；不满足则先向 Owner 要**保存位置或仅本轮一次性使用**的决定」；
  - `roles/driver.md:276`「收口时把证据保留结论写进 `roundup`：`not_delivered` 写明未获稳定保管的部分，`open_decisions` 列出保存位置/一次性使用的选择」；
  - `roles/verifier.md:47` 与 `roles/reviewer.md:50`：承重证据要另写「具体对象、路径或可重建输入、hash、需保留到哪个交付/复核点、原产者」；
  - `identity.md:60`：跨会话移交必须连同清单文件本身或其保存路径；
  - `roles/investigator.md:167`「一次性原型删除或移入明确的临时目录」。
- → **精确结论**：本库对"**承重证据**"有"每批核一次保管"的判据与两个字段（`evidence_pointer`、`not_delivered`/`open_decisions`），但**没有**对"交接物本体（report/verdict/proposal/slice-plan…）"规定存哪、谁保管、活多久；也没有任何默认目录或命名规则。**Owner 初判成立**，且我给出更强的说法：**本库把"记录该不该留"当成每批一次的商业决定（`driver.md:207` 的三种选项），而不是体系性默认**。

### G5.2 「没有跨角色的文档层级」→ **成立**（但本库有两种"层级"，别混淆）

- **成立的部分**：全库检索 `权威文档/派生视图/文档层级/文档体系` 只命中：`pipeline.md:15` 与 `roles/ledger-custodian.md:14` 的"**派生视图**"（指 `SOURCES.md` 生成区，不是项目文档）、`roles/architect.md:210` 的"项目已有的权威文档"（指被设计对象所在项目，不是本库自身）。
- **不要混淆的两种层级**：
  1. **契约层级（本库有）**：`README.md:50-58` + `pipeline.md` + `closure.md` + `identity.md`（"维护者规范，单一真源"）+ 各角色文件中的"内联副本"（`AGENTS.md:23` 核心原则 8；`identity.md:3`）。这是**规则之间的层级**，用于防止同一含义多处设值。
  2. **文档层级（本库没有）**：没有"规则/规格/计划/任务/记录/现场"这类**产物层级**，没有"哪一层是权威、哪一层是派生、哪一层可丢"的分类。
- 对照：addy 的 `context-engineering:19-27` 五层（rules > spec/architecture > source > output > conversation）是**产物层级**，本库没有对应物。

### G5.3 「没有 feature map 类的东西」→ **成立**，且是**有意识的未采纳**

- 本库唯一相关登记：`SOURCES.md:142`「`skills/create-verification-skill/SKILL.md:15-44`… 上游'生成项目内验证技能目录'的**载体形态不吸收**；只吸收 doctor 四问与'证据清理后仍在'」→ feature map 随载体一起未被采纳。
- 本库的"行为清单"最近亲是**自查夹具**：`scripts/identity-selftest.sh`（正负夹具，`AGENTS.md:41`）与 `scripts/check-library.py` 的检查项（`README.md:70-72`）；这是**对库自身**的行为清单，不是对下游项目产品的。`roles/verifier.md:46` 的 `falsification` 是"一次性的反例"，不构成索引。
- → 「没有 feature map 类的东西」成立；更准确的说法是：**本库没有"产品/行为级索引"，只有"库自身检查项"**。缺它的后果可引上游原文：`create-verification-skill/SKILL.md:36`「a proof that drives one convenient entry point is incomplete when the map lists others」+ benny `SKILL.md:130`「If no section covers the feature, mark the run blocked」。

### G5.4 「没有 to-do / 进度管理」→ **成立**（且本库明确拒绝百分比进度）

- 无 tracker/backlog/todo 载体：`SOURCES.md:181`「只吸收'机械宽范围改动可用 expand–contract'这一句，**不引入工单系统与 tracker 形态**」；`:183` 把 `triage` 列为 NOT ABSORBED（未读）。
- 进度只能以**事件**表达：`roles/driver.md:331`「报个百分比表示进度 | 只报事件：哪一步完成、证据在哪、卡在哪一步；百分比不落进 `roundup`」；`roles/planner.md:190`「只有一份'待办清单'没有判据」列为不算做完；`pipeline.md §7` 只定义两类停止事件（同前提重复失败 / 同一候选两轮阻断），没有"进度表"。
- 存在的**替代**：`closure.md` 的每环"可跳过/谁承接"、`roundup` 的 `delivered`/`not_delivered`/`evidence_pointer`/`open_decisions`（`roles/driver.md:85-88`）、以及本仓自己的 `.pi/round1..4/` 目录惯例。这些是**收口快照**，不是**进行中的进度台账**。
- → 成立；与本组旁证一致：本库连"谁现在在哪一步"的唯一权威位置都没有（`orchestrate.md:23` 的"每文件一个写者"式 store 本库没有对应物）。

### G5.5 「没有'哪些算过程性记录必须保全、哪些算工作现场可以丢'的规定」→ **部分成立（我不同意 Owner 的强表述）**

- **成立的一半**：没有统一的分类规则/清单；没有"必须保全"的默认集合；没有"现场可丢"的默认集合；`SOURCES.md` 的 `NOT ABSORBED` 与 `docs/archive/` 是唯一两处"刻意保留/刻意不保留"的实践（`README.md:61`「docs/archive/ 是被替换掉的旧载体，保留供追溯」）。
- **不成立的一半（本库已有零散但真实的规则）**：
  1. 承重证据的保管必须每批裁定：`roles/driver.md:207` + `:276`；
  2. 临时证据不得升格为可复用证据：`pipeline.md §8` 第 1 条「'可取回'包含其承重夹具/原始读数仍可取回、位置未失效——只剩摘要或已不存在的 `/tmp` 路径，不得复用为 `PASS`」；`verifier.md:49`「变异读数只存在于临时位置时，标为**临时证据**，不得当作将来可复用的锚」；`reviewer.md:51`「`/tmp` 只算**临时证据**，不能单凭'此刻存在'写成将来可复用的唯一锚」；
  3. 临时插桩必须清理：`implementer.md:217`「临时插桩已清理」；`investigator.md:167`「临时插桩按前缀全部删掉；一次性原型删除或移入明确的临时目录」；
  4. 运行时产物不自动豁免：`identity.md:36`。
- → **修正后的结论**：本库已经有"**证据层**"的保全/丢弃判据（且相当严格），**没有的是"**过程记录层**（报告、审查结论、设计提案、切片计划、决策记录）的保全/丢弃判据**"。所以 Owner 的根因表述应改成：**"哪些过程性记录必须保全、哪些工作现场可以丢"没有体系性规定，只有"承重证据"这一类的逐批裁定**。这个差别会影响修法：要补的不是"证据保管流程"，而是"过程记录的分类与归属"。

### G5.6 我追加的缺口（Owner 清单之外，独立复核发现）

| # | 缺口 | 证据（现状） | 对照（三仓有/无） |
|---|---|---|---|
| A1 | **本库自身的策略曾包含"文档体系双模适配"，在现载体中被丢掉** | `docs/TIM-PROFESSIONAL-WORKFLOW-PROPOSAL.md:145-165`（模式1：语义与路径映射，完全复用项目已有真源「绝不强行制造第二来源」；模式2：自然语言征求 Owner 意愿后引入轻量规范模板）；旧载体 `docs/archive/skills/professional-workflow/SKILL.md:35-40`（步骤 3：自适应项目文档体系）；现 10 角色文件与 `pipeline.md` **无一处**承接 | matt/addy 的同类机制是"外部 tracker 配置 + `docs/agents/*.md`"（matt `setup-matt-pocock-skills/SKILL.md:40-49`）与"活文档+可为 nil"（addy `getting-started.md:173-177`） |
| A2 | **决策台账机制存在但只挂在一个角色身上，且不覆盖其他角色** | `roles/verifier.md:207-217` 是**唯一**出现"决策台账"的角色章节；`README.md:58`/`AGENTS.md:42` 只把它列为脚本；`.pi/round1/decisions.tsv` 证明实际用过 | pstack 把它做成**跨角色共用**的 `show-me-your-work` 技能（`SKILL.md:9`「Keep one canonical log」）并规定"其他技能引用它、不要各自发明"（`SKILL.md:82`「Other skills route their audit trail here instead of inventing one. Reference it by name and let it own the format.」） |
| A3 | **没有项目级"门禁/约束"载体**（数字只能落在每张卡或外部契约） | `roles/planner.md:115-134` §4.5：门禁写进"项目自己的约束文件"，但本库没有规定该文件的形态/位置/生命周期；`SOURCES.md:300` 与 §4.4 裁决只保留"必须带命令、来源三选一" | addy 有 `CONSTRAINTS.md` + 四问 + 豁免到期日（`constraint-driven-development`，本库登记为 NOT ABSORBED，`SOURCES.md:253` 不含它，但 `:198`/`:300` 只吸收了"探测再提问"与"带命令"） |
| A4 | **没有"产物索引/路由器"** | 本库的索引只有 `README.md:50-58`（目录职责）与 `closure.md`（字段矩阵）；没有"哪个交接物在谁手里、哪条链现在活到哪一环"的索引 | matt 有 `ask-matt`（`CLAUDE.md:21`「a router that lies」）；pstack 有 `README.md:131+` 技能表与 `docs/guide/README.md`；addy 有 `using-agent-skills/SKILL.md:15-33` 的发现流程图 |
| A5 | **没有"记录活多久"的判据**（进版本库 vs 本地 vs 临时） | 本库对 `candidate`/`evidence` 有身份与可重取判据，但对"报告本身要不要进版本库、要不要在合并后删除"没有规则 | pstack `show-me-your-work/SKILL.md:44-48`（local by default, commit when reviewer needs it）；addy `getting-started.md:177`（可 merge 前删或 gitignore）；matt `handoff/SKILL.md:8`（OS temp） |
| A6 | **没有 onboarding/人类可读说明层** | 本库 `README.md` 是概览；`docs/` 是"设计背景、历史评审与归档"（`README.md:61`），明确非权威；没有"每个角色/机制给人看的一页说明" | matt `docs/<bucket>/<skill>.md` 四段模板（`CLAUDE.md:17`、`.agents/writing-docs.md`）；addy `docs/developer-onboarding.md`、`docs/getting-started.md` |
| A7 | **DDD 的上下文边界层缺失** | 10 角色无 Bounded Context/上下文映射位置；`SOURCES.md:180` 只吸收术语冲突与 ADR 三条件 | matt 有 single/multi-context 布局与 `CONTEXT-MAP.md`（`setup-matt-pocock-skills/SKILL.md:59-61`）；addy 有 capability map（模块边界，`spec-driven-development/SKILL.md:44-60`） |
| A8 | **没有"文档/记录被悄悄放宽或腐烂"的检测面** | 本库检查器 `check-library.py` 只兜结构与确定性回归（`README.md:70-72`「它判不了：§4 方法的实质深度…」），对下游项目文档无检测 | addy `constraint-driven-development`（检测被削弱的门禁）+ `evals` 三层（`evals/README.md:20-27`）；pstack `maintain-verification-skill`（feature map 漂移检测）；matt `triage` 的重复请求检测 |

### G5.7 复核结论（供 reviewer 直接使用）

- Owner 的 5 条初判：**4 条成立**（G5.1/G5.2/G5.3/G5.4），**1 条需要修正措辞**（G5.5：证据层已有规则，缺的是过程记录层的分类）。
- 我追加 8 条缺口（A1–A8），其中 **A1（旧载体有文档双模适配、现载体丢了）** 与 **A2（决策台账只挂 verifier）** 是本轮吸收任务最可能直接利用的两条：前者说明"该长什么样"在本库自己的历史里已有草案，后者说明"记录系统"已有可复用的落点与脚本，只是没接到全库。

---

# 追加任务（Owner 2026-09-27 第二批）

## G6 · 三仓文档全清点（硬要求）

**清点口径**：每个仓分两层——**(L) 库自身的文档** 与 **(A) 技能为下游项目规定的产物流文档**。因为三仓都是"技能库"，真正能支撑我们设计文档体系的是 (A) 的路径/命名/写者/寿命规则；
(L) 只提供"技能库自己的文档怎么组织"的样例。
**表格栏含义**：路径·命名 / 谁写 / 触发 / 频率 / 进版本库。无明文规则处一律写「无明文」。

### G6.1 pstack

**G6.1-L · 库自身文档（158 个文件）**

| 产物 | 路径 · 命名 | 谁写 | 触发 / 频率 | VCS |
|---|---|---|---|---|
| 技能库总览 + 技能总表 + 安装/使用 | `README.md`（`## install` `:15`、`## get started` `:21`、`## usage` `:32`、`## skills` `:95`、`## principles` `:194`、`## automations` `:253` 等） | 维护者 | 无明文；随技能增删改 | 是 |
| 人类导读 | `docs/guide/README.md` + `01-setup.md` … `10-recipes-and-pitfalls.md`（编号+主题） | 维护者 | 无明文 | 是 |
| 技能正文 | `skills/<name>/SKILL.md`；frontmatter 必写 `name`/`description`（`authoring-a-skill.md:2`） | 技能作者 | 技能新增或被改；**"misbehaving 时不要在任务中改，另开 PR"**（`docs/guide/09-make-it-yours.md:65`） | 是 |
| 技能参考/模板 | `skills/<name>/references/*.md`（如 `architect/references/{design-red-flags,rationale-template,runner-prompt}.md`、`interrogate/references/rubric.md`）、`poteto-mode/playbooks/<task-type>.md`、`show-me-your-work/references/decision-log-template.tsv` | 技能作者 | 与所属技能同改 | 是 |
| 技能脚本 | `skills/<name>/scripts/**`（`check-plan.mjs`、`orch/orch.ts`、`watch-pr/cli.ts`、`worktree-audit.sh`） | 技能作者 | 同上 | 是 |
| 子代理定义 | `agents/comment-sicko.md`、`agents/poteto-agent.md` | 维护者 | 无明文 | 是 |
| 自动化包与示例 | `automations/benny/{FOR_AGENTS.md,README.md,skills/**,templates/*.example.*,skills/*/references/*.example.md}` | 维护者 | 无明文；**示例要求被复制到 pack 之外使用**（`feature-map.example.md:5`、`setup-benny/SKILL.md:28`） | 是（示例本体） |
| 清单 | `.cursor-plugin/plugin.json`（`skills`/`agents` 入口）、`LICENSE`、`.gitignore` | 维护者 | 随结构变化 | 是 |

**G6.1-A · 技能为下游项目规定的产物**

| 产物 | 路径 · 命名 | 谁写 | 触发 / 频率 | VCS |
|---|---|---|---|---|
| 项目验证技能 + feature map | `.cursor/skills/verify-<app>/SKILL.md` + `features/README.md` + `features/<feature>.md`（一功能一文件） | 生成器 agent（`create-verification-skill/SKILL.md:25,36`） | 项目没有脚本化驱动面且需要验证时（`docs/guide/06-verify-and-ship.md:35-37`） | 无明文；benny 版本要求放到 pack 外、用户自有（`setup-benny/SKILL.md:28`） |
| 决策台账 | `decisions.tsv` 或 `.audit/<task-slug>.tsv`（`show-me-your-work/SKILL.md:46`） | 执行该轮/该 lane 的 agent | 每决策点；循环任务每轮一行（`:40`） | **默认不进**；"reviewer 需要 trail"才提交（`:48`） |
| 计划文件 | 默认 agent store 的 `docs/`；**操作者指名则用指名路径**（`multi-phase-plan.md:8`） | 规划 agent（plan 即交付物，`:3`） | 程序启动前 | 无明文（agent store 通常不在仓内） |
| 编排状态库 | `orchestrate/<project-slug>/{preferences.md, overview.md, units.tsv, frontier.json, ledger.tsv, inbox/, gates.md, decisions.tsv, status.md}`（`orchestrate.md:23-32`） | 逐文件单写者：coordinator 写 preferences/overview/gates、`units.tsv` 就地更新、verifier 写 `ledger.tsv` 行、脚本写 `state.json`/`attention.log`/inbox 与 handoffs、`status.md` 由脚本重算 | 每次 drain / 每个 unit 状态变化 / 每个 verdict | 无明文；store 保留作 postmortem（`:66`） |
| Handoff（worker/verifier 最终消息） | `<workspace>/handoffs/<task-name>.md`，脚本原样落盘（`references/handoffs.md:3,5`） | **脚本**（内容=agent 的最后一条消息） | 每个任务完成/失败（含合成失败 handoff） | 无明文 |
| 任务卡（brief） | 并入 spawn 提示词，不入库；字段模板见 `orchestrate.md:38-49`（GOAL/SCOPE/CONTEXT/ACCEPTANCE/VERIFY/TIMEBOX/FORBIDDEN/REPORT/STANDING） | coordinator/planner | 每次 spawn 与每次 resume 逐字携带 | 否（cloud spawn 必须内联） |
| 心跳与门 | `children.tsv`（owner 维护，记录子代理 id/预期时长/状态）、`gates.md`（等待人的问题+选项+默认） | owner / coordinator | 子代理启动时；门出现时 | 无明文 |
| 恢复笔记 | `/tmp/<slug>-resume.md`（`pause-safely.md:8`） | 暂停的 agent | 明确暂停时 | **否**（`/tmp`） |
| 验证证据截图 | `/tmp/swarm-<pr-id>/worker-<n>/<slug>.png`、`<media path>/<pr-id>-review-<slug>.png|.mp4`（`multi-phase-plan.md:77,123`） | 各 lane / owner | 每次 live lane / 每个 review gate | 无明文 |
| 修订轮记录 | 单条 decision 行 / lane 报告（`autopilot-full.md:6` 要求 owner 在 15 分钟内起 `decisions.tsv` trail 与 `children.tsv`；`:10` 每次 tick "collect the decision trails"；`:13` Reply 要求报"trail 在哪"） | owner | 每轮 / 每 tick | 无明文（`decisions.tsv` 保持未提交，随报告交回） |
| benny 配置与 feature map | `.cursor/benny/feature-map.md`、`~/.config/benny/feature-map.md`、`configuration.example.yaml` 的副本（`control-adapter.md:7`、`setup-benny/SKILL.md:81-84`） | 用户 | 自动化建立时；**pack 刷新不得覆盖**（`setup-benny/SKILL.md:28`） | 是（用户仓） |

**G6.1-H · 层级**：README（人的入口：安装/技能表）→ `docs/guide/`（人的教程，编号成序列）→ `SKILL.md`（agent 的操作面）→`references/*`（按需载入的判据/模板）；跨层原则两条：生成物**写给下一个 agent 而不是人**（`create-verification-skill/SKILL.md:9`）、**共享产物进 git 并按路径引用**（`orchestrate/references/planner.md:85`）。**没有**项目级文档层级（spec/plan/ticket 的层级）——因为 pstack 不把"项目文档"当自己的产物。

**G6.1-R · 防腐烂**：① 技能编辑时校验 frontmatter/被引用文件存在/跨技能链接可解析（`playbooks/authoring-a-skill.md:6`）；② 技能改动单独开 PR（`09-make-it-yours.md:65`）；③ `reflect` 从会话挖经验→落到技能编辑，并做"可否改成 lint/脚本/元数据"的检查（`reflect/SKILL.md:47-49`）；④ `maintain-verification-skill` 的漂移维护循环（三态：clean/changed/blocked，`SKILL.md:15-17`）；⑤ `show-me-your-work` 的台账回核 + 跨模型复审（`:63,67`）；⑥ 编排收口把反复出现的纠正写进 `preferences.md` 或 brief 模板（`orchestrate.md:66`）。**触发**：技能改动、漂移被发现、程序收口。**pstack 仓没有 CI**（无 `.github/`）。

### G6.2 mattpocock-skills

**G6.2-L · 库自身文档（168 个文件）**

| 产物 | 路径 · 命名 | 谁写 | 触发 / 频率 | VCS |
|---|---|---|---|---|
| 顶层入口（安装两种哲学+技能表+bucket 列表） | `README.md` | 维护者 | 技能增删改时同步（`AGENTS.md:9,15`） | 是 |
| agent 工作区根文件 | `AGENTS.md` 与 `CLAUDE.md`——**两文件内容逐字节相同**（`diff` 为空） | 维护者 | 同上 | 是 |
| 仓自身领域词汇 | `CONTEXT.md`（issue tracker / issue / decision ticket / triage role 及其关系，`:7-29`） | 维护者 | 语言变化时 | 是 |
| 发布记录 | `CHANGELOG.md` + `.changeset/*.md` + `.changeset/config.json`；版本 PR 由 `changesets/action` 在 main 上开（`.github/workflows/release.yml`） | 贡献者（changeset）/ 机器人（版本 PR） | 每个影响技能的改动带一条 changeset | 是 |
| 仓级决策 | `.agents/adr/NNNN-slug.md`（`0001-explicit-setup-pointer-only-for-hard-dependencies.md`、`0002-ship-as-a-claude-code-plugin.md`） | 维护者 | 难回退决定 | 是 |
| 库级规范子文档 | `.agents/install-block.md`（安装措辞单一来源）、`.agents/invocation.md`（user/model-invoked 约定）、`.agents/writing-docs.md`（docs 页模板#写作判据） | 维护者 | 相关约定变化时 | 是 |
| 人读技能页 | `docs/<bucket>/<skill-name>.md`（18 工程 + 7 生产力 = 25 页；四段固定：What it does / When to reach for it / Common questions / It's working if） | 技能作者 | **技能新增/重命名/行为变化**（`AGENTS.md:17`） | 是 |
| 技能正文与附属 | `skills/<bucket>/<skill>/SKILL.md` + 同名支持文档（`DEEPENING.md`、`DESIGN-IT-TWICE.md`、`ADR-FORMAT.md`、`CONTEXT-FORMAT.md`、`mocking.md`、`tests.md`、`PHASE-BOUNDARIES.md`、`SKILL-MECHANICS.md`、`HTML-REPORT.md`、`LOGIC.md`、`UI.md`、`template.sh`）+ `agents/openai.yaml`（Codex 元数据） | 技能作者 | 技能改动时 | 是 |
| bucket 索引 | `skills/<bucket>/README.md`（列全技能，一行一条） | 维护者 | bucket 内容变化时 | 是 |
| 路由器 | `skills/engineering/ask-matt/SKILL.md` | 维护者 | **技能增删改时必须同步**；"a router that lies"（`AGENTS.md:21`） | 是 |
| 被拒请求 KB | `.out-of-scope/<concept>.md`（3 个：`mainstream-issue-trackers-only`、`question-limits`、`setup-skill-verify-mode`） | 维护者/ triage | 增强类请求被拒时 | 是 |
| 仓库脚本与清单 | `scripts/{link-skills.sh,list-skills.sh,sync-plugin-version.mjs}`、`.claude-plugin/{plugin.json,marketplace.json}`、`LICENSE`、`package.json` | 维护者 | 结构/版本变化时 | 是 |

**G6.2-A · 技能为下游项目规定的产物**

| 产物 | 路径 · 命名 | 谁写 | 触发 / 频率 | VCS |
|---|---|---|---|---|
| 跟踪器配置 | `docs/agents/issue-tracker.md`（另 `docs/agents/domain.md`、`docs/agents/triage-labels.md`） | `setup-matt-pocock-skills`（一次性）；**用户此后可直接编辑**（`SKILL.md:116`） | 首次接入仓库时；只在"换跟踪器或从头重来"时重跑（`:116`） | 是 |
| agent 文件里的指针块 | `AGENTS.md`/`CLAUDE.md` 的 `## Agent skills` 块（三条单行摘要 + 指向 `docs/agents/*.md`，`SKILL.md:91-99`） | 同上 | 同上 | 是 |
| 规格 | `.scratch/<feature-slug>/spec.md`（本地 tracker）或 tracker issue | `to-spec` | 对话转规格时；立即打 `ready-for-agent`（`to-spec/SKILL.md:19`） | 是（本地 tracker 情形） |
| 工单 | `.scratch/<feature-slug>/issues/<NN>-<slug>.md`（编号从 `01` 起按依赖序；一单一文件） | `to-tickets` | 用户批准分解后（`to-tickets/SKILL.md:62`） | 是 |
| 工单/规格状态 | 本地文件里的 `Status:` 行（triage 态）；tracker 上用 label（五态状态机）与指派 | triage / 执行者 | 每次状态变化；认领先于开工（`issue-tracker-local.md:29`） | 是 |
| agent brief | tracker 评论（issue/PR 上），格式固定六段（Current/Desired/Key interfaces/Acceptance/Out of scope） | triage | 转 `ready-for-agent` 时（`triage/SKILL.md:79`） | 是（tracker） |
| triage 评论 | tracker 评论，**首行必须是 AI 生成声明**（`triage/SKILL.md:13-16`） | triage | 每次 triage | 是 |
| wayfinder 地图 | `.scratch/<effort>/map.md` 或 tracker 上的 `wayfinder:map` issue；子单 `issues/NN-<slug>.md` | 会话首个 affordance 者（chart） | 大工作开工前（`wayfinder/SKILL.md:21,113-114`） | 是 |
| 领域词汇表 | `CONTEXT.md`（单上下文）或 `CONTEXT-MAP.md`+每上下文 `CONTEXT.md` | `domain-modeling` | **懒创建**：第一个词定下时（`domain-modeling/SKILL.md:40`） | 是 |
| ADR | `docs/adr/NNNN-slug.md`（顺序编号，扫描最大号+1）；多上下文另有 `<context>/docs/adr/` | `domain-modeling` 建议、作者写 | **三条件齐**（难回退/无上下文难懂/真实取舍）才提（`:66-74`） | 是 |
| 研究笔记 | "repo already keeps such notes 的位置；match the existing convention；没有就放一个合理位置并说明"（`research/SKILL.md:12`） | 后台 research subagent | 需要外部知识时 | 无明文 |
| handoff | **OS 临时目录**，不进工作区（`handoff/SKILL.md:8`） | 当前会话 | 交接给新会话时 | **否** |
| 架构评审报告 | OS 临时目录的 HTML（`improve-codebase-architecture/SKILL.md:39`） | 评审会话 | 每次评审 | **否** |
| wizard 脚本 | scratch 或 `scripts/`，做完删；用户要求才提交（`wizard/SKILL.md:12`） | 当前会话 | 一次性 | 默认否 |

**G6.2-H · 层级**：`CLAUDE.md`/`AGENTS.md`（极简，主要当**导航指针**；`retro:41`）→ `CODING_STANDARDS.md`（**审查时读，非实现时**；`retro:42`）→ `docs/`（**被别的文件指到的引用文件**，写前先找既有文档；`retro:43`）→ skills（既是文档又是可调用单元：description 进上下文窗口；`retro:44`）→ 项目层：tracker/spec/tickets、`CONTEXT.md`、ADR、`.out-of-scope/`。此外 `.agents/invocation.md:16` 规定**共享参考文档放在拥有它的技能内，其他技能靠 Skill 调用取用，不做跨目录链接**。

**G6.2-R · 防腐烂**：① 技能增删改的三处同步（README、bucket README、plugin manifest）+ docs 页重写 + ask-matt 重读，全在 `AGENTS.md:9-21`；② changeset→CHANGELOG→release PR（`.github/workflows/release.yml`）；③ `.out-of-scope/` 的去重与改主意即删（`OUT-OF-SCOPE.md:86,108-118`）；④ `writing-for-agents` 的 pruning/no-ops/sediment 判据；⑤ `retro` 把会话问题转成环境改进（`retro/SKILL.md:18-19`：先读仓库自己的检查命令；机械性违规一律"Default to building the check over writing the rule"，`CODING_STANDARDS.md` 只留判断类）；⑥ `domain.md:47-51` 遇到与 ADR 矛盾要显式摊开。**触发**：技能改动、发布、被拒请求、复盘。**仓内 CI 只有 release，没有任何文档检查**。
**格式与实际的一致度**：`OUT-OF-SCOPE.md:19-40` 规定 `# 概念` + `## Why this is out of scope` + `## Prior requests`，本仓三个 `.out-of-scope/*.md` 逐一核过，三个文件都符合该格式（无漂移）。→ 说明"格式声明"可以被遵守，但三仓里**只有它没有机械校验**（靠人/agent 自觉）。

### G6.3 addyosmani-agent-skills

**G6.3-L · 库自身文档（文件清单：见 `find` 结果；16 个 `docs/*.md`）**

| 产物 | 路径 · 命名 | 谁写 | 触发 / 频率 | VCS |
|---|---|---|---|---|
| 顶层入口 | `README.md`（`## Commands` `:22`、`## Quick Start` `:44`、`## All 25 Skills` `:222` 按阶段分组、`## Agent Personas` `:288`、`## Reference Checklists` `:303`、`## Project Structure` `:350`） | 维护者 | 技能/命令增删时 | 是 |
| 仓库 agent 规则 | `AGENTS.md`（三层：Skills=how / Personas=who / Commands=when）+ `CLAUDE.md` + `.claude/rules/skills-contributing.md`（**路径作用域规则**：只对 `skills/**` 生效） | 维护者 | 约定变化时 | 是 |
| 规则书与地图 | `CONTRIBUTING.md`（自称 authoritative rulebook）、`docs/developer-onboarding.md`（自称 the map，与前者分工明写） | 维护者 | 流程变化时 | 是 |
| 技能结构规范 | `docs/skill-anatomy.md`：目录约定（`SKILL.md` 必需；`scripts/`、`references/`、supporting-file 可选，按需要加）+ frontmatter 规则 + 命名（小写连字符、必须=目录名）+ section anatomy | 维护者 | 结构规则变化时 | 是 |
| 工具接入指南 | `docs/{getting-started,adoption-guide,comparison}.md` + 每宿主一页（`claude?`/`codex-setup`、`copilot-setup`、`copilot-cli-setup`、`cursor-setup`、`gemini-cli-setup`、`opencode-setup`、`windsurf-setup`、`antigravity-setup`、`commandcode-setup`）+ `agents.md`、`advanced-per-agent-configuration.md` | 维护者 | 新宿主/新功能时 | 是 |
| 命令面（三份镜像） | `commands/<name>.toml`（Antigravity）、`.claude/commands/<name>.md`、`.gemini/commands/<name>.toml`——每个命令三处齐备且 description 相同（`scripts/validate-commands.js`） | 维护者 | 命令增删改时 | 是 |
| 人格 | `agents/<role>.md` ×4（code-reviewer / security-auditor / test-engineer / web-performance-auditor） | 维护者 | 角色变化时 | 是 |
| 共享检查表 | `references/*.md` ×6（definition-of-done / testing-patterns / security / performance / accessibility / observability） | 维护者 | 标准变化时 | 是 |
| 技能正文 | `skills/<kebab-name>/SKILL.md` ×25 + 可选的 `references/`、supporting 文件（`docs/skill-anatomy.md:9-15`） | 技能作者 | 技能改动时（走 CONTRIBUTING） | 是 |
| 评测体系 | `evals/README.md`（三档框架）、`evals/cases/<skill-name>.json` ×25（正/负触发例 + `expectations[]`）、`evals/fixtures/**`（真实输入基线）、`evals/plugin/**`（整插件评测）、`evals/skill-impact.md`（被拒变更 append-only 账本） | 技能作者/维护者 | 新增技能必带 case；改动按需重跑 | 是（`results/` 除外，见 gitignore） |
| 钩子文档 | `hooks/SDD-CACHE.md`、`hooks/SIMPLIFY-IGNORE.md`（+ 脚本与测试） | 维护者 | 钩子变化时 | 是 |
| CI | `.github/workflows/test-plugin-install.yml`（`validate-skills` → skill-lint 测试 → `validate-versions`）；另有 `.github/ISSUE_TEMPLATE/skill-gap.yml` | 维护者 | push/PR 每次 | 是 |
| 校验脚本 | `scripts/{validate-skills,validate-commands,validate-versions,validate-artifact-paths,validate-reference-links}.js` + `scripts/lib/skill-lint.js`（+ 各自单测） | 维护者 | 规则变化时（单源真源+s测试） | 是 |

**G6.3-A · 技能为下游项目规定的产物**

| 产物 | 路径 · 命名 | 谁写 | 触发 / 频率 | VCS |
|---|---|---|---|---|
| 规格 | `SPEC.md`（根）、`docs/SPEC.md` 或 `spec/` 下——**只有这三个位置被 `/build` 承认**（`commands/build.toml:30`） | `/spec`（spec-driven-development） | 新项目/特性/重大改动且无规格时（`:3` description） | **开发期进版本库；merge 前可删或 gitignore**（`docs/getting-started.md:175-177`） |
| 计划 | `tasks/plan.md`（永远是 markdown） | `/plan` | 有规格后 | 同上 |
| 任务清单 | `tasks/todo.md`（默认；或项目指定的外部 tracker——使用外部 tracker 时 plan 里只留 ID/链接索引） | `/plan` / `/build` | 每任务状态变化；**每 2–3 任务一个 checkpoint**（`planning-and-task-breakdown/SKILL.md:115`） | 同上 |
| 项目约束 | `CONSTRAINTS.md`（维度+数字+判定命令+豁免到期日） | constraint-driven-development | 无书面质量门时；`/build auto` 前 | 是（项目仓） |
| ADR | 默认 `docs/decisions/ADR-NNN-*.md`，**已有约定时沿用**（`docs/adr/`、MADR、`adr-tools`、`.adr-dir` 等）（`documentation-and-adrs/SKILL.md:36-40`） | 做决定的人（经 skill） | 难回退决定；**生命周期 PROPOSED→ACCEPTED→SUPERSEDED**，旧 ADR 不删 | 是 |
| 变更摘要 | 每任务一次 commit + 三段式摘要（What changed / **THINGS I DIDN'T TOUCH** / concerns，`git-workflow-and-versioning/SKILL.md:200`） | 实现会话 | 每个任务边界 | 是（commit/PR） |
| 规则文件 | `CLAUDE.md`/`AGENTS.md`/`.cursorrules` 等（context-engineering Level 1） | 项目 | 项目建立时 | 是（项目仓） |
| API 文档 | 类型内联注释（首选）/ OpenAPI；README 结构固定（Quick Start/Commands/Architecture/Contributing） | 实现会话 | 公共接口变化时 | 是 |
| Changelog | 项目 `CHANGELOG.md`（Keep-a-Changelog 式 Added/Fixed/Changed） | 实现会话 | 发布时 | 是 |
| 评估与外溢缓存 | `evals/results/`、`evals/plugin/results/<timestamp>/`、`.claude/sdd-cache/`、`.claude/simplify-ignore-cache/` | 工具/钩子 | 每次运行 | **否**（`.gitignore` 明列） |
| 浏览器证据 | before/after 截图与运行记录（`browser-testing-with-devtools`） | 验证会话 | UI 改动验证时 | 无明文 |

**G6.3-H · 层级**：**addy 是唯一给出正式分层的仓**——`context-engineering/SKILL.md:19-27` 五层：1 Rules Files（项目级常驻）→ 2 Spec / Architecture Docs（按 feature/session）→ 3 相关源码（按任务）→ 4 错误/测试输出（按迭代）→ 5 对话历史（可压缩）；`:98` 还给每层配了**信任级别**（源码/测试/类型=可信；配置/外部文档=需核实；用户内容/第三方响应=不可信）。
**G6.3-R · 防腐烂**（触发=CI 每次 push/PR + 按需 eval）：
- `validate-skills.js`：**以 `docs/skill-anatomy.md` 的规则为单一真源**（`scripts/lib/skill-lint.js`），逐技能校验；
- `validate-commands.js`：三个宿主命令目录的**命令集与 description 一致性**；
- `validate-versions.js`：清单版本一致；
- `validate-artifact-paths.js`：**spec/plan/todo 产物路径只能来自 `ARTIFACT_ALLOWLIST`（`SPEC.md`、`docs/SPEC.md`、`tasks/plan.md`、`tasks/todo.md`）**，任何文件里的相它路径与白名单不一致就红；**文件头注释逐字记了历史事故**：`scripts/validate-artifact-paths.js:8-12`——"Guards the spec -> plan -> build pipeline against silent artifact-path drift. … When a producer moves an artifact without updating the consumers — as in PR #93, which pointed `/spec` and `/plan` at docs/features/[name]/ while `/build` still required SPEC.md and tasks/plan.md — the pipeline breaks, **and nothing else in CI catches it** (command parity only compares descriptions)."；
- `validate-reference-links.js`：SKILL.md 与其 `references/` 内指向共享 checklists 的链接必须能解析；**同样有逐字事故说明**：`scripts/validate-reference-links.js:9-13`——"All 18 links across 11 skills resolved to files that do not exist, in the repo and in every plugin-install layout … Agents that followed the guidance — for example using-agent-skills pointing at the Definition of Done — **hit a file-not-found and stalled**. / Nothing else in CI catches this"；
- **每个校验器都带自己的单测**：`scripts/validate-artifact-paths-test.js`、`scripts/validate-reference-links-test.js`、`scripts/validate-commands-test.js`、`scripts/validate-versions-test.js`、`scripts/validate-skills` 对应的 `scripts/lib/skill-lint-test.js`（均在 `scripts/` 目录）；
- `evals` 三档：Tier1/2 进 CI，Tier3/plugin 按需（`evals/README.md:49`「this runs on demand and never in CI, like Tier 3」）；`skill-impact.md` 要求被拒变更**单独提交到默认分支**（`CONTRIBUTING.md:73`）；
- `references/definition-of-done.md:45`：「Documentation describes the current state in timeless language, not the change history」；
- `constraint-driven-development` 检测门禁被削弱。

### G6.4 三仓对照：项目级文档 vs 技能自带文档

| 维度 | pstack | matt | addy |
|---|---|---|---|
| 技能自带文档的结构 | `SKILL.md` + `references/` + `playbooks/` + `scripts/` + `agents/`（按职责分文件，无跨技能链接） | `SKILL.md` + 同名支持文档 + `agents/openai.yaml`；共享参考文档**内嵌在拥有它的技能里**（`invocation.md:16`） | `SKILL.md` 必需，`scripts/`/`references/` 可选；**参考材料不进技能目录**（`CONTRIBUTING.md:63`） |
| 技能↔人文档的关系 | README/guide（人） 与 SKILL.md（agent）分开，且要求生成物"给下个 agent 看" | 每个技能一个人读页 `docs/<bucket>/<name>.md`，四段固定 | 无逐技能人读页；人读文档在顶层 `docs/`（结构/onboarding/接入） || 项目级文档的载体 | 基本没有（除 `docs/guide` 是插件自己的）；项目文档交给 `orchestrate/<slug>/` store | 外部 tracker 或 `.scratch/` + `CONTEXT.md`/ADR | 仓内固定路径（`SPEC.md`/`tasks/*`）+ ADR + CONSTRAINTS |
| 分层声明 | 无正式分层；只有受众分离（人 vs agent vs 下一个 agent） | 无正式分层；只有"加载预算/受众"分工（agent 文件→标准→docs→skills） | **有正式 5 层**（rules→spec/arch→source→output→conversation）+ 信任级别 |
| 路径/命名一致性检查 | 无（无 CI） | 无（无 CI；只有 release workflow） | **有**（artifact-path 白名单 / reference-link / command 三面一致 / skill 结构 / 版本） |
| 维护循环与触发 | maintain-verification-skill（漂移）、reflect（会话复盘）、收口写回 standing orders | 技能变更同步（README/桶页/plugin/ask-matt/docs页）、changeset→release、retro | CI 每次 push/PR、evals 按需、skill-impact 账本、CONTRIBUTING pre-flight |
| 无明文的部分 | 文档更新频率、验证技能的 VCS | 研究笔记位置（由仓库约定决定）、handoff/评审报告不进仓的判据只有"临时件" | 证据截图的保存位置与期限 |

### G6.5 ① 的「三仓无此法」

1. **三仓都没有**一个**统一的"过程记录"目录**或"所有交接物归档"制度；记录散布在 tracker、agent store、仓内 `tasks/`、OS temp 四处。
2. **三仓都没有**规定"谁负责在什么时候复核文档是否过期"的**常驻职责**；防腐都是"触发式"（改动时同步 / 发现漂移时跑循环 / CI 时校验）。
3. **三仓都没有**固定刷新周期（cadence）：pstack 明说"用户问了才建议节奏"（`create-verification-skill/SKILL.md:44`）；addy 的行为层 eval 明说"按需求跑、不进 CI"（`evals/README.md:49`）。
4. **只有 addy**把"文档路径一致性"做成了 CI 门（也是唯一有历史事故记录作为动机的）。

---

## G7 · ②「已有文档体系时，往哪里放」三仓做法

**G7-01 · 通用优先级规则（addy，最强的写法）**：`skills/documentation-and-adrs/SKILL.md:36-44`：「### Match the existing convention first / Before creating an ADR, inspect the available repository context for an established convention … An established convention overrides the defaults below. / **Location and format** — e.g. `docs/adr/*.md`, `Documentation/Decisions/*.rst`, a MADR layout, or an `adr-tools` setup. Match the existing directory, file extension, and markup … / If the available evidence conflicts, surface the conflict rather than silently introducing another scheme. **Only when no convention can be established do you apply the default below.**」
→ 三仓里最接近"优先级裁定"的原句：**既有约定覆盖技能默认值；冲突要显式摊开，不得静默引入第二套；只有完全找不到约定时才用默认。**

**G7-02 · 规格工具层**：`skills/spec-driven-development/SKILL.md:150-153`：「**External spec tools:** This workflow is format-agnostic. If the project already uses OpenSpec or another specification system, keep that system's artifact format and storage conventions instead of creating a duplicate `SPEC.md`. This skill owns the clarification, content, and approval gates; the external tool owns how the approved spec is represented.」

**G7-03 · 任务跟踪层**：`skills/planning-and-task-breakdown/SKILL.md:162-164`：「**External tracker:** if the project's agent rules (`CLAUDE.md`, `AGENTS.md`, etc.) or the user designate an issue tracker …, create one tracker item per task instead of writing `tasks/todo.md`… When using an external tracker, note it in `tasks/plan.md` … and keep the plan document's Task List section as an ordered index of tracker item IDs or links rather than a duplicate checklist.」→ **外部 tracker 与 plan 并存，但 plan 不复制内容，只做索引**（"rather than a duplicate checklist"）。

**G7-04 · 探测先于发问（matt）**：`setup-matt-pocock-skills/SKILL.md:21-30`：「Look at the current repo to understand its starting state. Read whatever exists; don't assume: … `AGENTS.md` and `CLAUDE.md` … is there already an `## Agent skills` section? / `CONTEXT.md` 与 `CONTEXT-MAP.md` / `docs/adr/` 与 `src/*/docs/adr/` / `docs/agents/`：**does this skill's prior output already exist?** / `.scratch/`：a sign that a local-markdown issue tracker convention is already in use …」；`:59` 默认 single-context；`:61` 有 monorepo 信号才提 multi-context；`:116` 配置写完后「they can edit `docs/agents/*.md` directly later; re-running this skill is only necessary if they want to switch issue trackers or restart from scratch.」
→ **探测既有物 → 复用/只补缺 → 把决定写进仓内配置文件 → 之后由项目自己拥有。**

**G7-05 · 矛盾要摊开（matt）**：`setup-matt-pocock-skills/domain.md:47-51`：「## Flag ADR conflicts / If your output contradicts an existing ADR, surface it explicitly rather than silently overriding: > _Contradicts ADR-0007 (event-sourced orders), but worth reopening because…_」；`improve-codebase-architecture/SKILL.md:70`：被有分量理由拒绝的提案，**问**是否记成 ADR 以免后人重复建议。

**G7-06 · 默认不往项目里加文档（pstack）**：`multi-phase-plan.md:8`：「Unless the operator names a path, write the file under the agent store's `docs/`.」；`handoff/SKILL.md`（matt）与 `improve-codebase-architecture:39` 与之同向：**默认不在项目里落第二个位置**。

**G7-07 · 用户自有配置不得被包刷新覆盖（pstack benny）**：`setup-benny/SKILL.md:28`：「Keep user-owned configuration, feature maps, and routing maps outside the destination. Never overwrite them.」；`feature-map.example.md:5`「Pack refreshes must not overwrite it.」

**G7-08 · 路径移动会把下游打断（addy 的真实事故，逐字有据）**：`scripts/validate-artifact-paths.js:8-12`（文件头注释）：一次 producer 改了产物路径而 consumer 没跟上（PR #93，`docs/features/[name]/` vs `SPEC.md`+`tasks/plan.md`），"the pipeline breaks, and nothing else in CI catches it"；`scripts/validate-reference-links.js:9-13` 另记一起引用链接事故（18 links 全断，agent "hit a file-not-found and stalled"）；现在用 `ARTIFACT_ALLOWLIST` 一个规范集合把管线文件绑死，且每个校验器都有单测（`scripts/*-test.js`）。

**G7-09 · 与本轮 Owner 口述的 AB-SPEC 对齐**（`.pi/investigation/AB-SPEC.md`，19:04 加入）：Owner 把问题定为 **A（workflow 可产出的全部文档类型）↔ B（目标仓已有文档体系）的映射**，并要求 Driver 在情况 2 下做 "adaptive 版本"（举例 `a→3, b→2`），同时判断"不要指望三个上游仓库能有这个问题的答案"。**本轮证据支持该判断**：三仓有"探测 + 既有优先 + 冲突摊开 + 自己只占一个接缝"（G7-01…07），但**没有任何一处做 A↔B 的逐项映射，也没有"映射表/适配层"的产物形态**。可搬进映射机制的三件零件是：① 探测清单（matt `SKILL.md:21-30`）；② 优先级句"既有约定覆盖默认、冲突摊开"（addy `documentation-and-adrs:36-44`）；③ 单一真源+机械检查（addy `validate-artifact-paths.js`）——**它们能保证映射结果不被两套写法弄分叉，但它们不提供映射本身**。

**结论（②）**：
- **三仓都有**"引入/拼接已有文档体系"的做法，可归纳为四步：**探测既有物 → 既有约定优先（覆盖技能默认）→ 冲突摊开、不造第二来源 → 自己只占一个明确定义的接缝（配置指针 / 索引 / 白名单路径）**。
- **三仓都没有**"两套完整文档体系并存并规定优先级"的成例；最接近的是 addy 的"外部 tracker 与 plan 索引并存"（G7-03）与 matt 的"配置写在项目里、技能只当读写者"（G7-04）。
- **对 AB-SPEC 的直接回答（情况 2 的映射）**：**三仓无此法**——没有逐项 A↔B 映射、没有 adaptive 文档体系的产物形态、也没有"映射结果由谁裁定"的规则。三仓只提供探测、优先级句、唯一路径集合三件零件（G7-09）。
- **三仓都没有**"项目已有体系承载不了我们的必需字段时怎么办"的规则。addy 的 CI 白名单说明了一类答案（约定必须唯一且被工具盯住），但它管的是**同一个系统内部**，不是两系统之间。

---

## G8 · ③ feature map 的定位：完整能力、归属、触发

**G8-01 · 能力的完整步骤（只在 pstack 这一个地方有原文）**

| # | 步骤 | 原文锚点 | 产出/判据 |
|---|---|---|---|
| 1 | 访谈代码库（面/启动/驱动/观察/隔离） | `create-verification-skill/SKILL.md:11-19` | 能填满后续段落的真实事实；能观察到的绝不问人 |
| 2 | 生成验证技能（Launch/Doctor/Drive/Evidence/Cleanup/Helpers 六段） | 同上 `:23-32` | `.cursor/skills/verify-<app>/SKILL.md`；`Doctor` 是一个只读检查；`Cleanup` 不碰证据 |
| 3 | 播种 feature map（README 索引 + 每功能一文件 + 四个固定 H2） | 同上 `:34-36`；示例 `references/feature-map-example/README.md:33-42` | 项目内"维护中的验证真源"；缺一个入口就不算完整证明 |
| 4 | 交付前自证（launch→doctor→驱一功能→取证→cleanup，且确认证据仍在） | 同上 `:38-40` | 没跑过的生成物是草稿，不是交付物 |
| 5 | 交给维护循环 | 同上 `:42-44` | 指向 `/maintain-verification-skill`；**用户不问就不设周期** |
| 6 | 维护（漂移循环） | `maintain-verification-skill/SKILL.md:9-37` | 三态 clean/changed/blocked；只改验证技能自己目录；**不碰产品代码**；源波只读；活波必跑 |

**G8-02 · 触发条件（上游原文）**
- 无脚本化驱动面 + 需要验证：`docs/guide/06-verify-and-ship.md:35`「The UI bullet above hides a real requirement. The agent needs a scripted way to drive your app. **If your project has one, great. If not, run:** `/create-verification-skill`」；技能 description「Use for … when a project has no scripted way to prove UI/CLI/service behavior」。
- 有重复/并行驱动的真实需求：`06-verify-and-ship.md:41`「Once the verify skill works, a `/swarm` can split a full pass by **feature-map entry** and aggregate the results.」；同页："From then on, 'verify it in the app' is a step **any agent can execute, in this repo, with no setup conversation.**"
- 自动化把它当必需（仅限那一类设计）：benny `SKILL.md:11`、`control-adapter.md:9`、`FOR_AGENTS.md:35`（fail-closed）。
- 维护触发：漂移被发现 / 人或 agent 决定跑；**无固定周期**（`create-verification-skill/SKILL.md:44`）。
- 反证（它不是开工门）：上游唯一把 feature map 当"缺了不能干"的场景是 benny 自动化（先有 `control.feature_map_path` 配置才成立）；通用路径下 `/maintain-verification-skill` 在没有目标时的动作是"**stop and point at /create-verification-skill instead of inventing a target**"（`maintain:25`）——**那是维护循环的拒绝，不是工作流的拒绝**。

**G8-03 · 归属本库角色的候选与判据（对照现有角色文件）**

| 候选 | 支持证据 | 反对/缺口 |
|---|---|---|
| **Verifier（首选）** | 方法即"从真实入口驱动"（`roles/verifier.md:88` §4.2）、"对象与环境绑定断言"（`:69`）、"判据必须能失败"（`:169`）、"证据复用四条件"（`:188`）——四节都在做 feature map 要做的事；权限已含"在临时空间写夹具、探针与变异实现"（`:226`）；已有"自建前提"的处置规则：进仓/触共享数据或成为唯一放行闸时**由 Driver 发卡给有写权者，形成独立可审候选**（`:86`） | 该能力目前只以"临时装置"形式存在，**没有任何角色被指定为"长期验证资产"的持有人**；若让 Verifier 自己创建设计并自己验证，需靠 `:86` 的独立候选规则拉开距离 |
| Investigator（次选/协作） | 方法即"先建反馈回路"（`roles/investigator.md:49`）、"最小场景保存下来就是回归测试本体"（`:76`）——**构造驱动面的手艺在它手里** | 它的回路是**对症状**的（同一节触发条件：症状明确、原因不明），不是对"整套用户可见功能面"；它的 §5 只允许临时空间（`:195`） |
| Driver（必参与） | 写窗/授权/范围归 Driver（`pipeline.md:88-93`、`roles/driver.md:206`）；"自建前提要进仓"的分流也在 Driver（`driver.md:171/315`）；"是否真的存在反复驱动需求"是装配决定（`pipeline.md §2`） | 它不产内容 |
| Planner（接口） | map 里"什么读数算证明"属于判据层；Planner 已有"验证位置与最小验证"（`roles/planner.md:136`） | 不应把 map 变成逐片判据的替代品 |

**G8-04 · 本库现有"可选但要有能力持有者"的同类先例**：台账能力由 `ledger-custodian` 持有（`roles/ledger-custodian.md:16-20`，"按需"参与，`closure.md` A3 行明确"按需"）；决策台账能力已在 `verifier.md §4.8` 落过点；→ 本库已有"能力挂在某个角色、按条件参与"的写法，无需新角色。

**G8-05 · 与我们纪律的接法（供 reviewer 核）**：
- 不成为开工门 ⇒ 与 Owner 口径一致；
- 生成/维护者不得是唯一放行闸 ⇒ 本库已有 `verifier.md:86`；
- 进仓的 map 是"共享产物" ⇒ 需写明写入范围与保留决定（本库 `driver.md:207/276` 现有规则可套用）；
- 上游的"证据不因 cleanup 消失"与本库 `pipeline.md §8` 同向。

---

## G9 · ④「过程记录层」的定义性证据

**G9-01 · 口径**（按 Owner 澄清）：过程记录层 = **每个角色做事时"拿到的那一份"与"产出的那一份"**（即交接的输入与输出）。**不是**承重证据的保全规则（那部分本库已有且严格，本轮不查）。

**G9-02 · 三仓对这批"交接物"的处理方式**（逐类对照，锚点见 G6 各表）：

| 交接物类别 | pstack | matt | addy |
|---|---|---|---|
| 任务卡/工单（输入） | brief 内嵌于 prompt，不入库（`orchestrate.md:38-49`） | tracker issue / `.scratch/.../issues/NN-*.md`（`to-tickets:62`） | tracker item 或 `tasks/todo.md`（`planning:161-162`） |
| 规格/提案（输出） | plan 文件：默认 agent store `docs/`（`multi-phase-plan:8`） | `.scratch/<feature>/spec.md` 或 tracker（`to-spec:19`） | `SPEC.md`/`docs/SPEC.md`/`spec/*`（`build.toml:30`） |
| 审查/验证结论（输出） | `handoffs/<task-name>.md` + `ledger.tsv` 行（`planner.md:37-41`、`orchestrate.md:89`） | 报告在两轴下并列；只在对话里（`code-review/SKILL.md:43-49`） | 报告在对话里；agent brief 之外无落盘规则 |
| 决策记录 | `decisions.tsv`（append-only，本地默认） | ADR（`docs/adr/`） + 决定写进 `CONTEXT.md`/`.out-of-scope/` | ADR + `CONSTRAINTS.md` |
| 恢复/交接笔记 | `/tmp/<slug>-resume.md`（`pause-safely:8`） | OS temp handoff（`handoff:8`） | restartable boundary 五类信息写进 spec/plan（`context-engineering:123-135`） |
| 进度状态 | `units.tsv` 就地更新 + `status.md` 派生（`orchestrate.md:27,32`） | issue 状态机（label/`Status:` 行） | `tasks/todo.md` 勾选 + 每任务一 commit（`build.toml:35`） |

**G9-03 · 本库现状（与 G5.1/G5.5 一致，此处只给定义性结论）**：本库的交接物有**字段契约**（`closure.md:21-33`）但没有**落地位置/写者/寿命**；且已有两处只覆盖"证据"的规则（`driver.md:207/276`），不能拿它们当过程记录层的答案。**因此"过程记录层"在本库是明确的空白，不是半个句子。**

**G9-04 · 三仓无此法（对④）**：三仓都没有"按角色声明其输入/输出记录分别放哪、谁写、活多久"的**表**；pstack 最接近，但它写的是**每文件一个写者**（存储层）而不是**每角色一对输入/输出**（角色层）。→ 本库若要做，三仓只有零件，没有成品。

---

# 追加任务（Owner 2026-09-27 第三批 · 调查者 B）

**范围**：⑦ `grill` 现在归哪个角色｜⑧ 「人类沟通面」这个角色/会话除 feature map 外还能承担什么。三仓 pin 同 §0；本仓只读。任务一的产物另见 `.pi/investigation/FOUR-PARADIGMS.md`。

## G10 · ⑦ `grill` 这套东西现在归哪个角色

**G10-01 · 本库有没有 grill 类方法 → 有，而且已经归了角色（不是"无归属"）**

归属写在 `roles/driver.md:143-160` §4.1，标题就是「**对齐目标：按 frontier 分轮提问，不按清单一次性问完**」：

| 行 | 原文 |
|---|---|
| `driver.md:145` | **触发条件**：`scope`、`success_signal`、`authorization` 任一缺失，或目标有两种自洽读法 |
| `driver.md:148` | 1. 把待定事项画成**决策树**：每个决定下面挂依赖它的决定 |
| `driver.md:149` | 2. 算出 **frontier**——所有前置已定、现在就能问的决定。**只问 frontier**，一次一轮 |
| `driver.md:150` | 3. 每个问题附上我的推荐答案；下一轮再问依赖本轮结果的问题 |
| `driver.md:151` | 4. **事实我自己查，不向 Owner 要**；只有决定交给 Owner |
| `driver.md:152` | 5. frontier 清空后再开工；**Owner 确认之前不动手** |
| `driver.md:155` | **判断依据**：一轮结束时，如果我对 Owner 接下来三个问题的回答仍无法预测，说明 frontier 没走完 |
| `driver.md:159` | 反例：把"可扩展""规范"这类听起来正确的词当成目标接受下来。遇到这类回答，追问一句：如果不向任何人交代，你实际想要的是什么 |
| `driver.md:160` | 反例：把"你自己看着办"当作决定。这是**授权外包**，不是决定 |

**出处（已登记，可核）**：`SOURCES.md:152`（matt `skills/productivity/grilling/SKILL.md:6,8` 决策树 + frontier）；`:153`（同 `:24` 每轮重塑树）；`:154`（同 `:26` **"Finding facts is your job, never the user's."**）；`:155`（同 `:28` frontier 清空才算完成、用户确认前不许动手）；另有 `SOURCES.md:199`（addy `constraint-driven-development:57-90` 改写：只落地「每问自带推荐答案」与「按 frontier 分轮」）、`:229`（addy `interview-me:53-78` 一次一个 → 与 frontier 合并成"一轮问一个 frontier"）、`:231`（addy `:94-112` 用对方的话复述六项）、`:279`（乙方阻塞：授权门优先）、`:1245-1263`（引文审计逐条落点）。

**G10-02 · 逐条对照（上游原文 → 本库落点）**

| matt `grilling` 原文 | 本库 `driver.md §4.1` | 判定 |
|---|---|---|
| `grilling/SKILL.md:6`「Map this as a **design tree**: every decision branches into the decisions that hang off it.」 | `driver.md:148` | 逐字对译 |
| `:8`「The **frontier** is every decision whose prerequisites are already settled … Ask the whole frontier in one round: number each question and give your recommended answer.」 | `driver.md:149-150` | 逐字对译（"一次一轮"取代"一轮编号"格式，格式未吸收） |
| `:8`「Then wait for the user's answers before the next round.」 | `driver.md:150`、`:152` | 对译，并**加强**为"Owner 确认之前不动手" |
| `:24`「Each round the user answers reshapes the tree … Recompute the frontier and ask the next round.」 | `driver.md:150`「下一轮再问依赖本轮结果的问题」 | 对译 |
| `:26`「**Finding _facts_ is your job, never the user's.** … The _decisions_ are the user's: put each to them and wait.」 | `driver.md:151` | 逐字对译 |
| `:28`「**Do not act on it until the user confirms you have reached a shared understanding.**」 | `driver.md:152` | 对译 |
| （上游无此句） | `driver.md:155` 判断依据"能否预测接下来三个问题" | **本库自造的停手判据**（来源是 addy `interview-me:132-140` 的 95% confidence stop，`SOURCES.md:229` 登记为改写） |
| （上游无此句） | `driver.md:159-160` 两条反例 | `:159` 来源 addy `interview-me:90`「If you didn't have to justify this to anyone, what would you actually want?」；`:160` 来源 addy `interview-me:117`「"Whatever you think is best." → The user is delegating … Re-ask with two concrete options」 |

**G10-03 · 三仓里 grill 怎么用、由谁执行**

| 问题 | 答案 | 原文锚点 |
|---|---|---|
| 谁执行 | 由 **agent 访谈人**；一轮问整个 frontier，每问附推荐答案；等答复再进下一轮 | matt `skills/productivity/grilling/SKILL.md:6,8`；`:26`「The _decisions_ are the user's: put each to them and wait.」 |
| 谁触发 | `grilling` 是**唯一可被模型自发调用的**（`grill-me`/`grill-with-docs` 都 `disable-model-invocation: true`） | `docs/productivity/grilling.md:9`「**It is the only skill in the grilling family that is model-invoked**」；`grill-me/SKILL.md:4`、`grill-with-docs/SKILL.md:4`（均 `disable-model-invocation: true`） |
| 它的地位 | **primitive，不是被排进流程的一步**；由任意需要访谈的技能调用 | `docs/productivity/grilling.md:87`「`grilling` is a **primitive**, not a step you schedule: the single source of truth for the interview technique, kept in one place so **every skill that needs an interview reaches for it instead of inventing one**.」同页列出调用者：`grill-me` / `grill-with-docs`（两个 user-invoked 门）、`to-spec` 之前的主链起点、`wayfinder`、`triage`、`improve-codebase-architecture` |
| 会话的硬约束 | 必须有活的、可回应的人；**禁止在非交互环境跑** | addy `skills/interview-me/SKILL.md:36`（Loading Constraints）「This skill needs a live, responsive user. **Do not invoke in non-interactive contexts** like CI pipelines, scheduled runs, `/loop`, or autonomous-loop.」 |
| 什么不算确认 | 明确的"是"才算 | addy `interview-me/SKILL.md:113-122`；matt `grilling:28` |
| 问题数量 | matt：**不设上限**（`docs/productivity/grilling.md:67`「Can I cap the number of questions? **No, and a cap is deliberately out of scope.**」）；addy intake：**上限四问**（`constraint-driven-development/SKILL.md:91`「**Stop at four.** A twelve-question intake produces a config nobody understands and a user who regrets starting.」） | 两边**相反**，本库选了 frontier 而非数量设界（`SOURCES.md:199`） |
| pstack 有没有对应的 | **没有**。三处最近的都是别的东西 | `skills/interrogate/SKILL.md:9`「Spawn one reviewer per configured model to **adversarially review code changes**」（多模型互审，不是访谈人）；`skills/automate-me/SKILL.md:42`「### 2. Ask the user directly」（自动化配置访谈）；`principle-never-block-on-the-human`（`SOURCES.md:276-279` 登记为"默认不阻塞"，方向相反） |

**G10-04 · 本仓历史载体（已归档，可核）**：`docs/archive/skills/decision-grilling/SKILL.md:3`（description「通过按轮次推进决策树 frontier，结合附带假设的高效提问与显式确认门…输出结构化决策卡」）；`:11`「融合了 Matt Pocock 的决策树 frontier 分轮推进法与 Addy Osmani 的附带假设提问法」；`:34`「输出结构化《决策卡（Decision Record）》，记录已确认事实、人类拍板选项、排除路径」；`:44`「**没有白纸黑字就不算对齐！**必须沉淀出包含 Settled Decisions 的决策卡」。→ 现行 `roles/driver.md §4.1` 是它的存活形态，但**"决策卡"这个产物没有再出现**（对外只落 `task-card`）。

**G10-05 · 结论（事实层）**

1. **grill 有归属：Driver**。不是"无归属"。落点 `roles/driver.md:143-160`，来源 matt `grilling`，且已按 Owner 裁决改写过一次（授权门优先，`SOURCES.md:279`）。
2. **没有归属的是 grill 的"第二种用法"**：三仓把它当 primitive 供任意技能调用（`grilling.md:87`），本库只有 Driver 一处 —— `grep -rn "frontier" roles/` 的全部命中都在 `roles/driver.md`（`:143` `:149` `:152` `:155`），**没有任何其他角色文件引用 frontier 或 §4.1**。addy `interview-me` 那种"在任何 plan/spec/code 之前、面向 underspecified ask"的独立位置（`interview-me:12,14`）在本库没有对应者。
3. **本库把 grill 与"授权"绑在一起**（`driver.md:152`、`driver.md:145` 触发条件含 `authorization`），上游 `grilling` 本身不管授权（只管共识，`grilling:28`）；这条绑定是 `SOURCES.md:279` 登记的本库改写。
4. **`grill-me` 是三仓里唯一"无仓、无文件、纯对话"的 grill 形态**：`docs/productivity/grill-me.md:5`「It is **stateless**. It writes no files and leaves no workspace behind. The only thing it leaves is a sharper version of the idea, in your own head.」；`:15`「**Anything, anywhere** … It needs no repo and writes no files」；`:72`「no repo, no workspace, no setup, and **no assumption that the idea is even about software**」。→ 这条直接关系到 G11：**"人类沟通面"可以是一个不落盘的会话，上游有先例**。

**G10-06 · 三仓无此法（对⑦）**：三仓都**没有**"grill 归某个角色"这个概念 —— matt 把它定位在**技能层**（`primitive`，`grilling.md:87`），addy 的 **persona 层**里没有任何访谈/沟通面 persona（`docs/agents.md:5-10` 仅四个技术 persona）。→ **"grill 归哪个角色"这个问题三仓无此法；本库的答案（Driver）是自定的。**

---

## G11 · ⑧ 「人类沟通面」这个角色／会话，除 feature map 外还能承担什么

> Owner 前提（写在 `.pi/core/OPEN-ITEMS.md`）：`C2`「**不由 Driver 承接**：Driver 上下文只放 TIM 给它的 guideline/playbook，不能塞大块项目开发类内容」；`C3`「可以新开一个 session（"人类沟通面"）」；`A4`「除 feature map 外还能承担什么职责，要研究」。本节只给证据。

**G11-01 · 三仓里有没有"定位就是 human interface / 与人对谈并产出结构化共识"的角色或技能 → 有技能，没有角色**

**(1) addy `interview-me`：三仓里最接近"人类沟通面"的一个，且它把自己定位在**"所有其它技能之前"**

| 行 | 原文 |
|---|---|
| `skills/interview-me/SKILL.md:3` | description：「**Extracts what the user actually wants** instead of what they think they should want. Achieves this through **one-question-at-a-time interview** until ~95% confidence about the underlying intent. Use when an ask is underspecified ("build me X" without "for whom" or "why now") … or when you catch yourself silently filling in ambiguous requirements **before any plan, spec, or code exists**.」 |
| `:12` | 「The cheapest moment to find this gap is **before any plan, spec, or code exists**. Once you've started building, switching costs are real, and the user will rationalize the wrong thing into a "good enough" thing. **The misfit gets locked in.**」 |
| `:14` | 「The other Define-phase skills assume you already know roughly what you want: `idea-refine` generates variations, `spec-driven-development` writes the requirements down, `doubt-driven-development` stress-tests a plan. **Interview-me is the part before all of those.**」 |
| `:20-24` | 触发条件四条（缺 who/why/success/constraint 之一；请求是惯例式的而非具体的；你正准备用未说出的假设开工；两个合理价值取向相冲突时用户没说选哪个） |
| `:36` | （Loading Constraints）「This skill needs a live, responsive user. **Do not invoke in non-interactive contexts like CI pipelines, scheduled runs, `/loop`, or autonomous-loop.** If you're in one of those and the ask is underspecified, **flag that as a blocker for the user instead of guessing**.」 |
| `:40-49` | Step 1 **Hypothesize, with a confidence number**：先写下**一句话假设 + 0–100 的置信度**；「The number forces honesty.」 |
| `:53-60` | Step 2 格式：`Q: <one focused question>` / `GUESS: <your hypothesis, with the reasoning>`；「**Wait for the user to react before asking the next question.**」 |
| `:79-92` | Step 3 **Listen for "want vs. should want"**；对 sophistication-signaling 回答的固定追问：「*If you didn't have to justify this to anyone, what would you actually want?*」 |
| `:94-111` | Step 4 **Restate intent in the user's own words**：六字段 `Outcome / User / Why now / Success / Constraint / Out of scope` + `Yes / no / refine?`；「**Including "Out of scope" is non-negotiable.** Half of misalignment is silent disagreement about what is *not* being built.」 |
| `:113-122` | Step 5 **Confirm — explicit yes, not "whatever you think"**；列出**四种不算 yes**（"Whatever you think is best." / "Sounds good." / "Sure, let's go." / 沉默后的 "okay let's start."） |
| `:124-130` | Step 6 **Terminal Turn & Stop Rule (CRITICAL)**：拿到明确 yes 后 → 交付 Statement of Intent → 给出下游路径 → **STOP YOUR TURN IMMEDIATELY.**「Do NOT invoke tools or start downstream work in this turn.」 |
| `:132-138` | **The 95% Confidence Stop**：「Can I predict the user's reaction to the next three questions I would ask?」 |
| `:142-144` | **Output**：「The output of this skill is a **confirmed statement of intent** … **That's the deliverable.** Specs, plans, and task lists are downstream; **they consume the intent this skill produces.**」 |

定位旁证：`addy/skills/using-agent-skills/SKILL.md:19`（技能发现树的第一行）「Don't know what you want yet? ──────→ **interview-me**」→ 它是**第一个入口**，在 `idea-refine`（`:20`）与 `spec-driven-development`（`:21`）之前。

**(2) matt `grilling` 家族：一个 primitive + 三个前台**

| 前台 | 定位 | 原文 |
|---|---|---|
| `grilling` | **primitive**，可被任意技能调用 | `skills/productivity/grilling/SKILL.md:6`「Interview the user relentlessly until you reach a shared understanding.」；`docs/productivity/grilling.md:87` |
| `grill-me` | **无仓、无文件、纯对话**，可跑在任何主题上 | `docs/productivity/grill-me.md:5`、`:15`、`:72` |
| `grill-with-docs` | 同一场访谈 + **边谈边写** `CONTEXT.md` 与 ADR | `skills/engineering/grill-with-docs/SKILL.md:3`「A relentless interview to sharpen a plan or design, **which also creates docs (ADR's and glossary) as we go**.」；`:7`「Call the Skill tool twice, for "grilling" and "domain-modeling".」 |
| `wayfinder` | 一次装不下的工程 → **决策票据地图** | `skills/engineering/wayfinder/SKILL.md:3`「Plan a huge chunk of work (more than one agent session can hold) as a **shared map of decision tickets** on your issue tracker」；`:11-13`「Wayfinder is **planning** by default … absent that, **produce decisions, not deliverables**.」 |
| `to-questionnaire` | **面向另一个人**的沟通面 | `skills/productivity/to-questionnaire/SKILL.md:7`「Turn something the user can't answer alone into a **questionnaire**: a Markdown document they hand to one person to fill in async, or fill out together over a meeting.」；`:9`「**Grill the send, not the subject.**」 |

**(3) addy 的角色层：明确**没有**人类沟通面 persona**

- `docs/agents.md:5-10` persona 表只有四个，**全部是技术审查视角**：`code-reviewer`（Senior Staff Engineer）/ `security-auditor` / `test-engineer` / `web-performance-auditor`。
- `docs/agents.md:16-19` 三层定义：`Skill` = The *how*；`Persona` = **"A role with a perspective and an output format"** = The *who*；`Command` = The *when*。
- `docs/agents.md:22`「The user (or a slash command) is the orchestrator. **Personas do not call other personas.** Skills are mandatory hops inside a persona's workflow.」→ **人不在 persona 体系里被建模，人是编排者。**

**(4) pstack：没有 human interface 型技能**（`interrogate` 是多模型互审 `:9`；`automate-me:42` 是配置访谈；`principle-never-block-on-the-human` 方向相反）。

**G11-02 · grill / interview 类方法产出的东西通常冻结成什么形态**

| 冻结形态 | 技能 | 原文锚点 |
|---|---|---|
| **不冻结（纯对话）** | matt `grill-me` | `docs/productivity/grill-me.md:5`「It is **stateless**. It writes no files and leaves no workspace behind. The only thing it leaves is a sharper version of the idea, in your own head.」 |
| **词汇表 + ADR（边谈边写）** | matt `grill-with-docs` | `grill-with-docs/SKILL.md:3,7`；产物形态与门槛见 `domain-modeling/SKILL.md:64`（glossary and nothing else）与 `:66-72`（ADR 三条件） |
| **一份"意图"文档（六字段）** | addy `interview-me` | `interview-me/SKILL.md:99-108`（`Outcome / User / Why now / Success / Constraint / Out of scope` + `Yes / no / refine?`）；`:146`「If the user wants the intent to persist (a multi-session project, a handoff to another collaborator), offer to save it to **`docs/intent/[topic].md`**. **Only save if they confirm.**」 |
| **一页纸（五固定段）** | addy `idea-refine` | `idea-refine/SKILL.md:30-37`「The final output is a **markdown one-pager** saved to **`docs/ideas/[idea-name].md`** (after user confirmation), containing: Problem Statement / Recommended Direction / Key Assumptions / MVP Scope / Not Doing list」；`:140`「Only save if they confirm.」 |
| **配置表（仓库根一个文件）** | addy `constraint-driven-development` | `SKILL.md:95`「**One file at the repo root.** Any agent on any harness can read it, and a change to it shows up in review where it belongs.」；结构 `:102-137`（`## Floor` / `## Enforced with numbers` / `## Measured, not yet enforced` / `## Exceptions` 列含 **`Owner`** 与 **`Expires`**）；`:140` 往 `AGENTS.md`/`CLAUDE.md` 加一行指针 |
| **索引 + 决策票据（在 issue tracker 上）** | matt `wayfinder` | `wayfinder/SKILL.md:21`「The map is a single issue on this repo's issue tracker, labelled `wayfinder:map`, the canonical artifact. Its tickets are child issues of the map.」；`:23`「**The map is an index, not a store.** … a decision lives in exactly one place, its ticket, so the map never restates it, only gists it and links.」 |
| **给别人填的问卷** | matt `to-questionnaire` | `to-questionnaire/SKILL.md:16`「Write it to **`to-questionnaire-<slug>.md`** in the current directory (slug from the topic) and report the path.」；`:18-22` 文档结构（Purpose / From·To·How your answers will be used / Context / How to answer / 按主题分节） |
| **决策卡（本仓历史）** | `docs/archive/skills/decision-grilling/SKILL.md:34` | 「输出结构化《决策卡（Decision Record）》，记录已确认事实、人类拍板选项、排除路径」 |

**结论（事实层）**
1. **冻结形态不统一，共六档，且"不冻结"是合法的一种**（`grill-me`）。**没有任何一处把"清单式 checklist"当作访谈的最终形态。**
2. **任何落盘都带"用户确认"这一步**：`interview-me:146`、`idea-refine:140` 都写「Only save if they confirm.」→ 上游**不默认落盘**。
3. **"谈出来"与"落成什么"在上游是两个技能**：`grilling` 只负责谈（primitive），落盘由 `domain-modeling`（glossary/ADR）或 `to-spec`（spec）或 `wayfinder`（票据）承接。`grilling.md:87` 把这条写成规则：「every skill that needs an interview reaches for it **instead of inventing one**」。

**G11-03 · 三仓无此法**
1. 三仓都**没有**"human interface"作为一个**角色/persona**：addy 的四 persona 全是技术审查（`docs/agents.md:5-10`），pstack 没有角色层，matt 没有角色层。→ **"人类沟通面"作为一等角色，三仓无此法。**
2. 三仓都**没有**"某个会话专门承担人类沟通、其余会话不承担"的分工规则；matt 的做法相反 —— 把访谈做成 primitive 让**任意**技能调用（`grilling.md:87`）。→ **"人类沟通面由哪个会话承接"三仓无此法。**
3. 与 Owner 约束（Driver 上下文不放项目文档）同向的原文只有一条，且它是**技能属性而非角色职责**：`grill-me` 的无仓/无文件/可跑任何主题（`grill-me.md:5,15,72`）。

**G11-04 · 本库现状（事实，不含建议）**
- 10 份角色文件的 §1 使命里，**没有一份**包含"与人对谈并产出结构化共识"：`driver.md:12` 是"把 Owner 的目标与授权变成可执行的任务卡…不做实现、审查、验证"；其余 9 份是调查/设计/切片/实现/审查/验证/集成/复核/台账。
- 唯一现存的访谈方法在 `roles/driver.md §4.1`，而 Owner 已把 Driver 排除在 feature map 承接者之外（`.pi/core/OPEN-ITEMS.md` C2）。
- 全库 `grep -rn "frontier"` → **只有 `roles/driver.md` 四处**（`:143` `:149` `:152` `:155`）。
- 全库 `grep -rniE "追问|质询|拷问|访谈" roles/ pipeline.md closure.md` → **命中 1 处**：`roles/driver.md:159`（§4.1 的反例「遇到这类回答，追问一句：…」）。pipeline.md 与 closure.md **0 命中**。
- → **"人类沟通面"在本库的状态是：方法有一份（driver §4.1），位置没有**。是否新增位置、由谁承担、承接哪些产物，属设计决定。
