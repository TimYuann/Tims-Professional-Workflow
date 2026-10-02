# A2R-CURSOR-ABC7 · cursor-plugins 审核包 7（Agent 载体质量门 / 同题候选仲裁 / 评审呈现 / 覆盖台账与残余）

- 发现者：tpw-absorb-a2r（A2r）
- 源仓：`cursor-plugins`，pin `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`（只读 locator：`.worktrees/legacy-pre-night-2026-10-01/upstreams/cursor-plugins`）
- 产品基线：night worktree；core `professional-workflow/`（21 文件）；冻结 Backbone 未触碰
- 供 `tpw-absorb-gate` 实质裁定；本包不自行裁定采纳；处置均为“拟/候选/待裁定”
- 与包 1–6 的关系：本包补 A/B/C 与工程裁决的最后三块（载体质量、候选仲裁、评审呈现），并以 MG-4 给出本 A2R 线对 863 路径的覆盖台账与 a4 交接清单，供 Driver 记账与门控核对。
- 已接受 gate 对包 1 的路径纠错（`thermos/skills/thermo-nuclear-review/SKILL.md`）。

## 1. 包内机制组总览

| MG | 机制组 | 主要源文件（pin 内） | 建议判断位点 | 类型 |
| --- | --- | --- | --- | --- |
| MG-1 | Agent 载体的创建与质量门 | `pstack/skills/poteto-mode/playbooks/authoring-a-skill.md`、`pstack/agents/poteto-agent.md`、`create-plugin/{README.md,skills/create-plugin-scaffold,skills/review-plugin-submission,rules/plugin-quality-gates.mdc,agents/plugin-architect.md}` | meta（方法/Profile 等载体的落点纪律） | 方法+门控候选 |
| MG-2 | 同题候选仲裁 | `pstack/skills/arena/SKILL.md` | D/工程裁决（限缩） | 方法候选 |
| MG-3 | 评审走查的组织与呈现 | `pr-review-canvas/skills/pr-review-canvas/SKILL.md`、`cursor-team-kit/skills/pr-review-canvas/SKILL.md`、`docs-canvas/skills/docs-canvas/SKILL.md` | F/B（评审 UX） | 合并候选 + 不吸收判定 |
| MG-4 | 覆盖台账与残余 | 旧索引 `ABSORB-A2-CURSOR-INDEX.tsv` + 本包 §2 | Driver 记账 | 台账（非机制） |

---

## MG-1 Agent 载体的创建与质量门（meta）

### 1) 机制与触发情境；源锚点与已读/尚缺

| 源锚点 | 已读 | 尚缺 |
| --- | --- | --- |
| `pstack/skills/poteto-mode/playbooks/authoring-a-skill.md`（全文，831B） | 全文 | 无 |
| `pstack/agents/poteto-agent.md`（全文，641B） | 全文 | 无 |
| `pstack/agents/comment-sicko.md`（全文，包 4 已读） | 全文 | 无 |
| `create-plugin/README.md`（全文） | 全文 | 无 |
| `create-plugin/skills/create-plugin-scaffold/SKILL.md`（全文） | 全文 | 无 |
| `create-plugin/skills/review-plugin-submission/SKILL.md`（全文） | 全文 | 无 |
| `create-plugin/rules/plugin-quality-gates.mdc`（全文） | 全文 | 无 |
| `create-plugin/agents/plugin-architect.md`（全文） | 全文 | 无 |
| `create-plugin/CHANGELOG.md`、`.cursor-plugin/plugin.json` | **未读** | 元数据 |
| 真实 plugin 校验器 | **未运行** | 未执行 |

触发情境：写或改一个 SKILL.md（authoring-a-skill）；从零创建/重构一个插件，或提交前做质量门（create-plugin 的三件套 + rule + architect agent）。

### 2) 操作、成立条件、失败模式、反例/例子

**authoring-a-skill（8 条，逐条）**：“You own the skill's voice.” ① 用作者平台的 skill-authoring 流程；② 校验：frontmatter 有 `name` 与 `description`、被引用文件存在、跨 skill 链接可解析；③ 结构性（structural）才写 test cases，主观的跳过；④ 走开 PR 流程。**“When in doubt, delete. Keep only prose that changes a decision.”** 告诉它去做那件事、跳过理由；只有规则没理由会令人困惑时才解释；语气匹配范围；**指向结构性来源**（types、READMEs、config，按 encode-lessons-in-structure）；**按路径委派其他 skill，不要重述**；反复遇到但未被捕获的工作流 → 提议新 skill。Reply：skill 摘要、关键设计决定、校验备注。

**poteto-agent（agent 定义纪律）**：是 `/poteto-mode` 与“用 poteto 风格”请求的路由目标；**恢复既有 `poteto-agent` 而不是 spawn 兄弟**；任何工作前**完整读 poteto-mode 的 SKILL.md（含 inline Principles index）**；**用 `generalPurpose` 替代会跳过该读并 drift**；`is_background: true`。

**comment-sicko（读过的评审 agent 定义，包 4）**：read-only 评审者；首条输出固定角色文本；**keep list 是唯一 leash**；只报告、`MUST KILL` 标符号、绝不写应用代码。与 MG-1 的关系：agent 定义是“载体”的一部分，其 description/触发与行为边界同样受质量门约束。

**create-plugin-scaffold（9 步要点）**：Required inputs：插件名（小写 kebab-case，起止为字母数字）、purpose 与 target users、组件集（rules/skills/agents/commands/hooks/mcpServers）、仓库风格（single-plugin vs multi-plugin marketplace）。默认输出 `~/.cursor/plugins/local/<plugin-name>/`（用户指定则遵从）。Workflow：① 校验名称格式；② 确定目录并创建；③ 建 base files（`.cursor-plugin/plugin.json`、`README.md`、`LICENSE`、可选 `CHANGELOG.md`）；④ 填 manifest（必需 `name`；推荐 `version/description/author/license/keywords`；**只在非默认发现需要时显式组件路径**）；⑤ 组件文件带有效 frontmatter（rules `.mdc` 含 `description/alwaysApply/可选 globs`；skills `skills/<name>/SKILL.md` 含 `name/description`；agents `agents/*.md` 含 `name/description`；commands `commands/*.(md|txt)` 含 `name/description`）；⑥ marketplace 仓库补 entry（name/source/可选 metadata）；⑦ **所有 manifest 路径相对、有效、不用绝对路径或父级穿越**。Guardrails：聚焦一个用例；偏好简明可执行的 skill/rule 文本而非长散文；**不引用不存在的文件**；用文件夹发现默认；默认位置除非用户另给。

**review-plugin-submission（提交前门）**：五类核验——manifest 有效性（存在、name kebab-case、metadata 一致）；组件可发现性（skills/rules/agents/commands/hooks/mcp.json 在约定位置）；组件元数据（skill 含 name+description；rule frontmatter 有效且指引清楚；agent/command 含 name+description）；仓库集成（marketplace entry 存在、source 解析到插件目录、名字唯一）；文档质量（README 说明 purpose/installation/组件覆盖；可选 logo 路径有效且 repo-hosted）。Checklist：manifest 存在且 JSON 合法；所有声明路径存在且相对；无 broken file reference；无缺失 frontmatter；插件范围清晰聚焦；marketplace 注册完整。输出：按 section 的 pass/fail、优先级修复列表、最终提交建议。

**plugin-quality-gates（always-applied rule，6 条）**：manifest 存在且 name 有效；路径相对且在插件目录内（无绝对、无 `..`）；声明的组件路径匹配真实文件/文件夹；rules/skills/agents/commands 都有必需元数据 frontmatter；插件范围聚焦且在 README 记录安装与用法；默认保存到本地插件目录，只有用户明确要求才换。

**plugin-architect（readonly agent）**：设计聚焦、可维护的插件，**最小可行组件集**；澄清 goal/users/expected outcomes；按需要推荐组件组合；提出目录布局与 manifest 形状；**早期 flag 可发现性/元数据问题**；返回具体实现清单。

**成立条件**：有可写的载体位置与命名空间；组件类型与 discoverability 规则已知；提交前有校验。

**失败模式/反例**：引用不存在的文件/跨 skill 断链；manifest 路径绝对或 `..` 穿越；缺 frontmatter 导致不注册；把多个用例塞进一个插件/方法；README 缺 purpose/安装/覆盖；marketplace name 重复或 source 不解析；agent description 用泛词导致误触发；用 `generalPurpose` 替代专用 agent 导致 drift；新建兄弟 agent 而不恢复既有；把 skill 写成散文而非可执行指令；重述其他 skill 内容。

### 3) 判断位点与 Profile 调用

| 位点 | 专业 concern | 何时调用 | 由哪个 Profile 提议 |
| --- | --- | --- | --- |
| meta：方法/Profile/Charter 等载体的落点 | 可维护性/可发现性 | 新增或修改任何吸收载体时 | `driver`（bounded composition）+ 方法作者 |
| A/Voice：面向 agent 的说明是否改变决定 | 沟通 | 写 description/触发条件 | `intent-voice` |
| F：提交前机械核验 | 证据 | 载体发布前 | `evidence-evaluation`（机械项不可替代专业测试） |

### 4) 当前产品锚点、覆盖、缺口、为何值得吸收

- `professional-workflow/methods/README.md` `## Scope and current state`：方法入口、按需加载、不接受对象替代。
- `professional-workflow/profiles/README.md`：“预设是**可缓存的判断配置**，不是职位表，不产生任务决定权，也不自带方法正文。”
- `docs/absorption/2026-10-02/EXECUTION-PLAN.md`：“可新增或深化方法/按需支持文件、修正 Profile 方法入口与 Charter 例子；不要把所有经验内联进 Profile。”“不建 registry/框架。”
- 项目 `AGENTS.md` Engineering Discipline：“Solve the smallest real problem…Do not add features, abstractions, configurability, or broad refactors that were not requested.”

已覆盖：最小问题、不建框架、Profile 不含方法正文、按需加载。

具体缺口：

1. **载体的“提交前质量门”缺失**：产品有 Charter/方法/Profile 三类载体，但没有“frontmatter/触发描述/引用存在/链接可解析/范围聚焦/README 覆盖”的检查清单；本仓吸收的每个新方法都要落到载体，门缺失会造成断链与重复。
2. **没有“为 agent 写的说明”的纪律**：`authoring-a-skill` 的“只保留改变决定的文字、告诉它做那件事、指向结构来源、按路径委派而不重述、反复遇到就提议新 skill”正是 `methods/` 与 `profiles/` 需要的写作文体（与包 4 的 human-facing 写作互补）。
3. **没有“最小可行组件集”判断**：插件 architect 的“聚焦一个用例、最小组件集、早期 flag 可发现性/元数据”可直接用于吸收落点选择，避免方法库膨胀。
4. **没有 agent 定义的路由纪律**（恢复既有专用 agent、完整读被引 skill、替代 `generalPurpose` 会 drift）——产品不定义 agent runtime，但“引用必须完整读取、专用配置不可被泛化替代”与产品“方法必须按需绑定、不能被泛化替代”同构。
5. **“不引用不存在的文件”“路径不得穿越”** 是机械可核规则，正好补 Gate 侧“check 只做机械核验”的分工。

为何值得吸收：吸收的每个机制最终都要落到载体；这组给出“载体形态 + 质量门 + 最小化”的纪律，且与执行计划的“不建 registry/框架”“不内联 Profile”完全一致。**限缩**：宿主插件字段（plugin.json、*.mdc、marketplace）不进入产品；只保留“载体清单、引用完整、触发描述具体、范围聚焦、最小化”等判断。

### 5) 拟处置与载体

- 拟保留：authoring-a-skill 的“只保留改变决定的文字/说做什么/指向结构来源/按路径委派不重述/反复遇到提新 skill/结构性才测”；poteto-agent 的“恢复而非新建、完整读被引、专用不可替代”原则；create-plugin 的“最小可行组件集、聚焦一个用例、引用存在、路径相对、frontmatter 必需、README 覆盖、提交前按 section 检查、优先级修复”。
- 拟改变：去 `.cursor-plugin`、`plugin.json`、`.mdc`、`~/.cursor/plugins/local/`、marketplace.json、commands 扩展名等宿主细节（改为“载体清单/元数据/路径/引用”等通用词）；去 `generalPurpose` 等具体 agent 名。
- 拟删除：市场发布/logo/keywords 等与吸收无关项。
- 载体：方案 1（推荐）新增 `methods/guide-method-carrier-hygiene.md`（载体落点与提交前检查），在 `methods/README.md` 的维护说明与 `profiles/README.md` 交叉引用；方案 2 并入包 2 MG-3 的 lesson-promotion（代价：那是“何时编码”，本组是“编码成什么形态并如何核”，触发不同）。本包倾向方案 1。
- **与 gate/check 的分工**：本组给 check 提供一组机械可核项（引用存在、路径相对、frontmatter、README 覆盖），但**不把专业覆盖判断交给 checker**。

**平台耦合/依赖**：宿主插件系统是载体；纪律骨架零耦合。

### 6) 正文草稿与验证方案

```
方法载体检查（草稿）
1. 范围：一个载体一个用例；最小可行集合（能不加就不加）。
2. 文字：只保留改变决定的句子；说做什么，跳过理由（理由只在否则困惑时给）；指向结构来源而不是复述；按路径引用其他方法，不重述。
3. 元数据与引用：名称与描述（触发条件具体）；被引用文件存在；链接可解析；路径相对、无穿越。
4. 入口与文档：README/入口表说明用途与组件覆盖；新增方法必须能从选择入口到达。
5. 提交前：按 section 核验并给优先级修复；机械项可交 check，覆盖与触发质量仍由专业判断。
6. 反复遇到但未捕获的工作流 → 提议新载体；不因假设未来而建框架。
```

验证方案（未执行）：对一个拟新增方法文件跑检查 (a) 是否最小且单一用例；(b) 引用/链接是否全部解析；(c) 是否可从入口到达；(d) 是否重述了其他方法内容。边界：不引入插件系统；不要求市场元数据。

---

## MG-2 同题候选仲裁（D/工程裁决，限缩）

### 1) 机制与触发情境；源锚点与已读/尚缺

| 源锚点 | 已读 | 尚缺 |
| --- | --- | --- |
| `pstack/skills/arena/SKILL.md`（全文） | 全文 | 无（其 Phase B/C 的模型调度细节属宿主，未执行） |
| `pstack/skills/architect/SKILL.md`（包 1 已读） | 全文 | `references/design-red-flags.md`、`rationale-template.md` 未读（a4） |
| `methods/cross-module-design.md`（产品） | 已读 | 无 |

触发情境：一次尝试会锁死错误形状的非平凡产物；需要多个候选同题比较并合成（`/arena`：naming、formats、algorithm、设计方向）。

### 2) 操作、成立条件、失败模式、反例/例子

**六阶段（要点）**：A **Frame**：N 个候选收到同一 prompt，**prompt 就是契约**；说明每个候选产出的 artifact；推导 rubric——“先说明*这个任务*的成功是什么，再转成 3–6 条可评分标准”；**rubric 是 Phase D 选择者的工具，候选只看到任务**；选 runners（不同模型；生成绑定可同模型 N 次；判断敏感才多模型）；给每个候选独立输出路径（worktree 或隔离目录）。B **Fan out**：一条消息并行 spawn 所有候选，各自带任务、共享 grounding 路径、自己的输出路径，并产出 artifact + 短 rationale（说明考虑过的替代与被拒原因）；候选失败则 N-1 继续并记录 dropout。C **Cross-judge**：候选完成后选一个**尽量与 parent 不同家族**的 readonly judge（按路径标签与 rubric 逐标准打分并推荐 base），**与 parent 的阅读并行**，不在候选还在写时 spawn。D **Pick a base**：**逐份端到端读完**每个候选再选；**逐标准打分而不是整体感觉**；与 cross-judge 比较——base 一致则确认，**分歧说明一方有偏或 rubric 含混**；选 base 的标准是**未来维护者最容易在不破坏不变量下扩展**的那个，平手时偏好更干净的边界或更小的 API（Laziness Protocol）；在 base 旁写短 synthesis note（含 cross-judge verdict）。E **Graft**：再走一遍每个败者，找出值得移植的一两点（信号通常是每个候选一到两点，不是大部分）；**手工折入**（不与机械粘贴），结果必须在**同一个心智模型下保持连贯**；记录 graft 来源与拒绝理由。**N 个候选收敛到同一形状是强一致信号**：记录收敛并 ship 共识形状，不需要 graft；**N 个候选大幅分歧说明 Phase A 欠规格**：reframe 后重跑，**不要把分歧平均掉**。F **Verify**：合成产物要与任何输出一样经得起同样审查；若验证暴露出 arena 没抓到的问题，要么 Phase A 错了（reframe 重跑），要么某个候选抓到了而你漏了 graft（回 Phase E），**不要粉饰**。Outputs：一个合成 artifact + 一个短 synthesis note（base、grafts 及来源、rejections、dropouts、verification 结果）。

**成立条件**：产物非平凡且一次尝试会锁形状；rubric 可评分；候选能独立产出。

**失败模式/反例**：prompt 作为契约却欠规格导致分歧后仍平均；rubric 给候选看（污染）；把候选的 rationale 当装饰不看替代/拒绝原因；不读完就按整体感觉选；与 judge 分歧不查偏见/rubric；平手时选更炫而非更易维护；机械粘贴 graft 导致不连贯；把收敛当“没有价值”而硬 graft；验证发现问题却粉饰。

### 3) 判断位点与 Profile 调用

| 位点 | 专业 concern | 何时调用 | 由哪个 Profile 提议 |
| --- | --- | --- | --- |
| D：候选方案比较与合成 | 技术/架构 | 存在多个实质不同方案且决定难逆 | `technical-planning` |
| F：合成产物的独立验证 | 证据 | 合成后 | `evidence-evaluation` |
| A/Voice：是否值得多个候选 | 成本/价值 | 决定探索宽度时 | `intent-voice`（成本） |

### 4) 当前产品锚点、覆盖、缺口、为何值得吸收

- `profiles/technical-planning.md` `## 关键问题`：“有没有多个实质不同的方案？取舍依据是什么，谁拥有该取舍的接受权？”
- `profiles/technical-planning.md` `## 常见误区`：“把 Plan 写到每个 helper/算法”。
- `methods/cross-module-design.md` `## Limits`：“Do not require a fixed number of design alternatives or parallel agents.”（M4 已明确 deferred `DESIGN-IT-TWICE`）
- `methods/README.md` “Deferred alternatives: … `DESIGN-IT-TWICE` and its parallel-agent count …”。

具体缺口：

1. **产品明确 defer 了并行候选与固定数量**，因此不能吸收 arena 的“默认多候选”；但**当任务自愿产生多个候选时**，产品没有“rubric 先行、逐标准、维护者可扩展性、graft 连贯、收敛/分歧处置、合成后验证”的仲裁程序。
2. **没有“分歧视为偏见或 rubric 含混”的判定**，也没有“大幅分歧 = 输入欠规格，重跑而不是平均”的反例。
3. **没有“收敛即共识、价值在合成不在数量”的表述**（避免为了流程而硬保持候选）。

为何值得吸收/限缩：它补 D 的方案仲裁面且不复活 fixed-parallelism；**限缩**：不要求 N>1、不要求并行、不要求固定模型数、不做常设 gate。

### 5) 拟处置与载体

- 拟保留：rubric 3–6 条且对候选保密；prompt 即契约；候选 rationale 记替代/拒绝；逐份读完、逐标准打分；与交叉判者比较且分歧查因；维护者可扩展性为 base 选择标准、平手偏好更小 API/更干净边界；手工 graft 且保持单一心智模型；收敛 ship 共识、分歧重跑不平均；合成后按正常标准验证。
- 拟改变：去 `arena`/模型 slug/`subagent_type`/`/tmp` 路径（改为“候选/评审者/隔离输出位置”）；去“默认 N 个模型”的固化数量。
- 拟删除：模型调度与配置细节。
- 载体：方案 1（推荐）并入 `methods/cross-module-design.md` 作为“多候选时的仲裁”一节（该文件已声明显式 deferred，正好承接）；方案 2 独立 `guide-candidate-arbitration.md`（代价：与 D 方法触发重叠且易被读成强制探索）。本包倾向方案 1，并保留其 Limits 中“不要求固定候选数/并行 agent”。

**平台耦合/依赖**：多模型调度是宿主；仲裁程序零耦合。

### 6) 正文草稿与验证方案

```
多候选仲裁（草稿，仅当任务自愿产生多个候选时）
1. rubric 先行（3–6 条可评分标准，候选不可见）；候选只拿任务。
2. 逐份读完、逐标准打分，不凭整体感觉；独立评审者的推荐与自己的判断比较，分歧先查偏见或 rubric 含混。
3. 选“未来维护者最易扩展而不破坏不变量”的 base；平手偏好更小 API/更干净边界。
4. 从败者手工折入一到两点，保持单一心智模型；收敛即共识，不硬 graft；大幅分歧说明输入欠规格，重跑不平均。
5. 合成产物照常独立验证；发现漏抓回查输入或 graft，不粉饰。
```

验证方案（未执行）：给一个自愿双候选的小设计，检查 rubric 是否候选不可见、选择是否逐标准且以维护者可扩展性为准、graft 是否连贯、合成是否被独立验证。边界：不要求候选数、不要求并行、不成为强制流程。

---

## MG-3 评审走查的组织与呈现（F/B，评审 UX）

### 1) 机制与触发情境；源锚点与已读/尚缺

| 源锚点 | 已读 | 尚缺 |
| --- | --- | --- |
| `pr-review-canvas/skills/pr-review-canvas/SKILL.md`（全文前 70 行与其结构段） | 全文主体 | 其余“Be creative”尾段（模式重复）未逐字；canvas SDK 细节（`~/.cursor/skills-cursor/canvas/`）不在源仓，未读 |
| `cursor-team-kit/skills/pr-review-canvas/SKILL.md`（全文前 120 行，包 3 MG-2 已读） | 相关主体 | `template.html`/`renderer.js`/`styles.css` 未读（资产，归 a4） |
| `docs-canvas/skills/docs-canvas/SKILL.md`（全文，3125B） | 全文 | 无 |
| 两个 pr-review-canvas 副本的 md5 | 实测：plugin 版 `89066b5b…` vs team-kit 版 `a6dde531…`，**字节不同**（一个用 canvas SDK，一个用自包含 HTML/gh API） | 两份的详细差异未逐字比较 |

触发情境：把 PR diff 组织成 reviewer 可读的走查（评审前的输入组织）；把文档/架构说明渲染成可导航 surface。

### 2) 操作、成立条件、失败模式、反例/例子

**pr-review-canvas（plugin 版，核心组织纪律）**：gather 期望 GitHub PR 链接（或 `gh` 可解析引用），用 `gh pr diff` 收集每个文件的 path/additions/deletions/hunks；**若用户没给 PR 链接，停下并问——不要猜当前 branch、不要从 recent history 推断、不要退回本地 `git diff`**。**不要按字母或树序呈现文件**；按 reviewer 价值重排：① Core logic（新行为、算法变化、状态转换、API 表面变化；全 diff + 上下文）；② Wiring & integration（route/dependency injection/config plumbing；压缩到足以确认正确）；③ Boilerplate & mechanical（import 重排、rename、生成代码、格式化、类型 re-export；只列文件名与统计，除非特别相关不给 inline diff）；**core logic 在最前，因为 reviewer 注意力在顶部最锐**。**Dense logic 蒸馏成 pseudocode**（深嵌套、状态机、retry/backoff、多步转换；剥离语法/错误处理/boilerplate，暴露本质算法/控制流）；**只在真实 diff 难以扫读时做，简单改动不需要 pseudocode mirror**。**Trace tricky logic on a concrete example**：当 hunk 以难以预测的方式改行为（效果重排、新 short-circuit、边界变化）时，选一个小而真实的输入，**old/new 路径并排走查**，高亮分歧点与可观察结果；只用于真正令人意外的行为变化，不是每个 core hunk。**Call attention to tricky things**：对 surprise/risky/easy-to-miss 的 hunk 视觉分离并配短标签（“Subtle”“Breaking”“Race condition”“Perf”）+ 一句话解释；**过度使用会毁掉信号**。Tone and content：写 reviewer-facing commentary 不是 changelog；说 **why** 不只 what；写文件间交互（如“core.ts 的新 validator 被 routes.ts 的新 route 调用”）；写 diff 本身不明显的东西；每条 1–2 句。Be creative：上述是地板不是天花板；按改动类型（refactor/bugfix/feature）选表示（状态图、before/after call graph、input→output 表、commit 时间线、逐文件置信标注、大 callout + 其余折叠）。

**team-kit 版差异（包 3 已读）**：同一机制的自包含 HTML 实现——`gh api` 并行取 PR/文件/评论，core vs mechanical 分类、pseudocode 摘要折叠（“Show full implementation”）、`renderDiff` 自动过滤 import/折叠空白改动/检测移动代码、`.verdict` 检查框；**安全注入**：patch 可能含 `</script>`，先用 `jq` 存 JSON、再用 Python 注模板，绝不手工嵌入 JS/JSON。

**docs-canvas（判定用）**：文件开头自标 **“Status: placeholder. The skill structure is in place so the canvas welcome page can surface this plugin via the marketplace query, but the full skill body still needs to be written. Treat the steps below as a starting outline and refine as the docs canvas pattern matures.”** 内容为通用大纲（Overview/TOC/Body/References、优先内置组件、reader-facing prose、lead with answer、be creative），并依赖源仓外部的 `~/.cursor/skills-cursor/canvas/SKILL.md` 与 SDK 类型。

**成立条件**：有 diff 与 PR 引用；有可渲染的 canvas/HTML 载体；reviewer 是消费者。

**失败模式/反例**：没有 PR 链接就猜 branch/本地 diff；按树序呈现；把 mechanical 与 core 混在一起；对所有改动都做 pseudocode/trace/callout（信号淹没）；把 changelog 当 commentary；core 不放最前；把 canvas SDK 细节当产品依赖；吸收 placeholder（docs-canvas）当成熟方法。

### 3) 判断位点与 Profile 调用

| 位点 | 专业 concern | 何时调用 | 由哪个 Profile 提议 |
| --- | --- | --- | --- |
| F：评审输入的组织 | 证据可读性 | 评审前准备 diff 走查 | `evidence-evaluation` |
| B：对外呈现的 reviewer 消费者 | 沟通 | 写走查说明/评论 | `behavior-domain` + `intent-voice` |
| D：呈现载体选择 | 技术 | 选 canvas/HTML/纯文本 | `technical-planning`（a4 侧） |

### 4) 当前产品锚点、覆盖、缺口、为何值得吸收

- 包 1 MG-6（评审裁决）与包 3 MG-2（评论输入）、包 6 MG-1（交付形态）已覆盖评审的判断与 PR 形态。
- `profiles/evidence-evaluation.md` `## 关键问题`：“结果能否被另一个会话按材料复现？”
- `docs/WORKFLOW-INTENT.md` §2：“控制注意力负担、传递失真与流程成本。”

具体缺口：

1. **没有“评审输入的组织”规则**：按 reviewer 价值排序、core/wiring/boilerplate 分层、dense logic 的 pseudocode、tricky hunk 的 old/new trace 与标签、overuse 警告——产品有证据纪律但没有“把证据摆给 reviewer”的注意力分配。
2. **没有“没有明确 diff 引用就不猜”的纪律**：与产品“不把推断当事实”同源，可复用。
3. **没有载体选择的适用性判断**：canvas/HTML 是可选呈现，不是产品依赖。

为何值得吸收：评审成本主要由输入组织决定；这组与包 6 MG-1 的 PR body 形态互补（一个管文本 briefing，一个管 diff 走查）。**判重**：两个 pr-review-canvas 副本是同一机制的两个载体（字节不同、渲染方式不同），吸收时只取组织纪律一份，渲染实现归 a4。

### 5) 拟处置与载体

- 拟保留：core → wiring → boilerplate 的 reviewer 价值排序；core 最前；pseudocode 条件性；concrete trace old/new；tricky 标签与 overuse 警告；说 why 与文件间交互、1–2 句；没有明确引用就停下问；机械噪声折叠/逐文件置信标注等可选表示。
- 拟改变：去 canvas SDK/HTML/渲染器/`gh` 命令（改为“可用呈现载体”）。
- 拟删除：docs-canvas（**placeholder，不吸收**；若未来成熟再评估）。
- 载体：方案 1（推荐）并入包 1 MG-6 的 `methods/review-verdict.md`（评审方法）作为“输入组织”一节，或与包 6 MG-1 的交付形态合并为“评审友好呈现”；方案 2 独立 `guide-review-walkthrough.md`（代价：与评审方法触发重叠）。本包倾向合并，并在溯源表注明两副本只算一份。
- **给 gate 的判重结论（事实）**：`pr-review-canvas` 在 pin 内有两个字节不同的载体（plugin 版 canvas SDK / team-kit 版自包含 HTML），机制同源；`docs-canvas` 自标 placeholder，不构成可吸收方法。

**平台耦合/依赖**：canvas SDK、浏览器渲染、`gh` 是宿主；组织纪律零耦合。

### 6) 正文草稿与验证方案

```
评审走查组织（草稿）
1. 先拿明确 diff 引用；没有就停下问，不猜 branch、不退回本地 diff。
2. 按 reviewer 价值排序：Core logic（全上下文）→ Wiring/integration（压缩）→ Boilerplate/mechanical（只列文件与统计）。core 在最前。
3. Dense logic 才加 pseudocode（剥离语法暴露算法）；tricky 行为变化才做 old/new 具体 trace；surprise/risk 才加短标签。过度使用毁信号。
4. 评论说 why、说文件间交互、说 diff 不明显的东西，每条 1–2 句；不写 changelog。
5. 呈现载体（canvas/HTML/文本）按可用性选择，不是产品依赖；机械噪声自动折叠。
```

验证方案（未执行）：对一个真实混合 diff 生成走查，检查 (a) core 是否在最前且 mechanical 被折叠；(b) pseudocode/trace/callout 是否只在需要时出现；(c) 没有引用时是否停下问。边界：不要求 canvas；纯文本同样适用组织规则。

---

## MG-4 覆盖台账与残余（供 Driver 记账与门控核对，非机制裁定）

### 1) 本 A2R 线（包 1–7）对 863 路径的覆盖

本 A2R 线按 A/B/C 主干 + 工程裁决产出包 1–7；下表按顶层目录给出覆盖归属与残差。**路径数来自旧索引 `ABSORB-A2-CURSOR-INDEX.tsv`（863 行含表头）；“已读/已评”指本线实际读到机制的路径，不等于全部路径都被逐字读完；“a4”指按委托应转交 tpw-absorb-a4 的 D/E/F、资产/支持脚本与尾部。**

| 顶层目录 | 路径数 | 本线覆盖 | a4 / 残余 |
| --- | --- | --- | --- |
| `third_party/` | 482 | **本包 §2 完成处置判定**（见下） | 6 个 MCP 用法指南 + shopify rule 的逐字机制归 a4 |
| `pstack/` | 158 | 包 1–7 覆盖 playbooks（bug-fix/feature/investigation/prototype/autonomous-run/pause/pickup/refactoring/visual-parity/eval/opening-a-pr/shipping/babysit/autopilot-full/stack/worktree-cleanup/multi-phase-plan）、skills（poteto-mode/how/why/teach/recall/reflect/interrogate/arena/tdd/blast-radius/create+maintain-verification-skill/show-me-your-work/no-comments/automate-me/unslop/technical-writing/bro/cli-for-agent?（cli-for-agent 是独立目录）/23 principles）、agents（poteto-agent/comment-sicko）、docs/guide 01–10（01/07/09 部分未逐字）、README | 未读：orchestrate.md、hillclimb、perf-issue、runtime-forensics、trace-forensics、typescript-best-practices、make-bot-ui、setup-pstack 余部、automations/benny、scripts、references/* |
| `orchestrate/` | 84 | 包 1 MG-7 + 包 5 MG-1 覆盖 SKILL/dispatcher/spawning/planner/handoffs/prompts（root/subplanner/worker/verifier/loop-hygiene/failure/finished/empty-error/andon-block/slack-block） | scripts/*、schemas/*、`__tests__/*`、adapters/*、cli/* 全归 a4 |
| `cursor-team-kit/` | 29 | 包 1–6 覆盖 thermo-nuclear code-quality、make-pr-easy-to-review、review-and-ship、verify-this、get-pr-comments、fix-ci、loop-on-ci、check-compiler-errors、run-smoke-tests、fix-merge-conflicts、new-branch-and-pr、control-cli、control-ui、deslop、pr-review-canvas、weekly-review、what-did-i-get-done、workflow-from-chats、agents/thermo 旧 agent（未逐字比较） | rules/no-inline-imports、rules/typescript-exhaustive-switch、agents/* 细节归 a4 |
| `advisor/` | 14 | 包 1 MG-6 + 包 3 MG-5 覆盖 README、SKILL、briefing-template、agent、stop-hook；包 8 未做 | 其余 hooks（record-consult/mark-pending/capture-response/lib）、CHANGELOG 归 a4 |
| `cursor-sdk/` | 11 | **未读** | 全归 a4（SDK 机制） |
| `thermos/` | 10 | 包 1 MG-6 + 包 5 MG-2 覆盖 README、thermos SKILL、thermo-nuclear-review SKILL、两个 subagent，实测 code-quality SKILL 与 team-kit 字节相同 | CHANGELOG/LICENSE、两个插件的重复判重结论已给出 |
| `ralph-loop/` | 10 | 包 1 MG-8 覆盖 stop-hook 判断面 + skills/ralph-loop 开头/抓取说明 | ralph-loop-help/cancel-ralph 余部、capture-response、hooks.json 细节归 a4 |
| `agent-compatibility/` | 10 | 包 3 MG-1 覆盖 README、SKILL、四个 agents | CHANGELOG、plugin.json 元数据 |
| `grok-voice/` | 9 | **未读** | 全归 a4 |
| `create-plugin/` | 9 | 包 7 MG-1 覆盖 README、两个 skills、rule、agent | CHANGELOG、plugin.json |
| `continual-learning/` | 8 | 包 5 MG-5 覆盖 README、skill、agent、hook 前段 | hook 余部、plugin.json 归 a4 |
| `teaching/` | 6 | 包 4 MG-4 覆盖 README、两个 skills（判定：不吸收） | plugin.json 元数据 |
| `pr-review-canvas/` | 6 | 包 3 MG-2 + 包 7 MG-3 覆盖 SKILL；与 team-kit 副本判重 | 渲染资产归 a4 |
| `docs-canvas/` | 6 | 包 7 MG-3 覆盖 SKILL（判定：placeholder 不吸收） | 渲染资产归 a4 |
| `cli-for-agent/` | 4 | 包 1 MG-3 覆盖 SKILL；README 未读 | README 归 a4/后续 |
| `schemas/` | 2 | **未读** | 归 a4 |
| `scripts/` | 1 | **未读** | 归 a4 |
| 根 `README.md`、`.gitignore`、`.github`、`.cursor-plugin` | 4 | 根 README 未逐字读（旧索引有 row） | 归 a4/台账 |

### 2) `third_party/` 482 路径的处置判定（供 a4 直接复用，不是机制裁定）

- **470 路径为纯资产/重复载体**（79 个插件 × {`.cursor-plugin/plugin.json`、`README.md`、`CHANGELOG.md`、`LICENSE`、`mcp.json`、`assets/logo.{png,svg}`}），无工程机制；旧索引 nature 为“市场展示资产/许可声明/版本记录”。建议 Driver/a4 按“纯资产/重复载体”一组处置，不逐文件精读。
- **8 路径含实际内容**，带工具使用与安全纪律，归 a4：
  - `third_party/google-docs/skills/google-docs/SKILL.md`（6.1KB）：Docs 编辑用零基 UTF-16 index range，每次写都会 shift 后续 index；**不要计算/猜 index，先定位文本**（“#1 source of bugs”）。
  - `third_party/google-sheets/skills/google-sheets/SKILL.md`（4.5KB）：两套坐标系统（VALUE 工具用 tab 标题 + A1；STRUCTURE/FORMAT 工具用另一套），故意分离。
  - `third_party/google-slides/skills/google-slides/SKILL.md`（6.9KB）：坐标是 slide 左上角的 POINTS（标准 720x405）；对象用 `read_presentation` 的 objectId 寻址；**每次读或写后带 `requiredRevisionId`，让并发编辑失败而不是静默损坏**。
  - `third_party/x/skills/x-api-mcp-guide/SKILL.md`（21.6KB）+ `references/pricing.md`（6.8KB）：连接 X 后必须在任何用户可见文本前取 `get_usage_credits`；tools=0 是 setup failure 而非 paywall；成本参考。
  - `third_party/x/skills/x-chat/SKILL.md`（9.7KB）：加密 X Chat 读取/发送，依赖本地 `chatxdk`/`xchat_lite.py`；缺工具时让用户重连而非自建 app/要 token。
  - `third_party/x-money/skills/x-money-guide/SKILL.md`（9.8KB）：**任何移钱动作每次都要问、无例外**；连接（connection code + passkey）、重连/撤销路径、失败消息含义。
  - `third_party/shopify-store/rules/shopify.mdc`（1.8KB）：在“已连接店铺的 MCP 工具”与“Shopify AI Toolkit skills”之间按用户问的是店铺数据还是建站来路由。
- 与 A/B/C 的关系：这些是第三方工具的行为契约与安全边界（B/F 邻近），但其机制归属在 D/E 工具使用面，且与产品已接受的责任骨架无冲突性新增；本包不另行吸收，仅给 a4 一份可复用清单。

### 3) 本线未读残余（诚实登记，不假装已评估）

- pstack：`playbooks/orchestrate.md`（16.8KB）、`hillclimb.md`、`perf-issue.md`、`runtime-forensics.md`、`trace-forensics.md`、`eval.md` 已读（本包）、`authoring-a-skill.md` 已读；`skills/typescript-best-practices`、`make-bot-ui`、`setup-pstack` 余部、`automations/benny/*`、`skills/poteto-mode/references/*`、`scripts/*`、`docs/guide/00、01、09` 部分。
- `why/references/sources/*`（7 类 investigator playbook + incident-postmortem）、`why/references/investigator-prompt.md`；`interrogate/references/code-quality-review.md`；`architect/references/design-red-flags.md`、`rationale-template.md`、`runner-prompt.md`。
- cursor-team-kit rules、agents 细节；cursor-sdk、grok-voice、schemas、scripts、docs-canvas/pr-review-canvas 渲染资产；orchestrate scripts/schemas/tests/adapters/cli。
- 上述残余按委托归 a4（D/E/F、支持脚本、资产、尾部）或后续 A2R 轮次；本包不据其下任何结论。

### 4) 与 gate 已知裁定的对齐

- 包 1 的 8 组已判（吸收 1/合并 1/限缩 6），并纠错源路径；本包 MG-3 的 `pr-review-canvas` 判重与包 5 MG-2 的 thermos 判重是同类“重复载体只算一份”的事实补充。
- gate 对包 1 MG-7 的边界（拒绝“worker words 直接当事实/唯一消息通道/机械映射”）与对 MG-8 的限缩（不吸收“任意 side bug/永不停/自定 exit condition”）在本线后续包（包 5 MG-1、包 6 MG-3/4）继续保持，未越界主张。

## 8. 包级综合观察（供 gate，不是裁定）

1. MG-1 是吸收流水线自身的载体纪律，建议在 B 落地任何新方法前先有该检查，避免断链与 Profile 内联。
2. MG-2 与产品已 deferred 的 `DESIGN-IT-TWICE` 不冲突：它只规定“已有多个候选时如何仲裁”，不要求产生候选。
3. MG-3 的判重结论（两个 pr-review-canvas 副本、docs-canvas placeholder）直接服务“多源一个机制不能重复算知识增量”。
4. MG-4 是本线的覆盖台账，供 Driver 记账；`third_party` 的 470 纯资产可整组处置，8 个实用文件清单可交 a4。

## 9. 包内自检（机械项，非专业裁定）

- 源 pin 与路径：均为 `ecc249f1e306fc64ddf83c7bed16cacf7c2239db` 下实际存在的路径；两副本 md5 实测；
- 未修改产品/他人文档/registry；未 commit；
- 每组含 6 项要求（MG-4 为台账组）；所有验证方案标注未执行。
