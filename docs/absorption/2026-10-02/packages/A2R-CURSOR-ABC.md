# A2R-CURSOR-ABC · cursor-plugins 审核包（族 A/B/C 主干 + 工程裁决）

- 发现者：tpw-absorb-a2r（A2r）
- 源仓：`cursor-plugins`，pin `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`（只读 locator：`.worktrees/legacy-pre-night-2026-10-01/upstreams/cursor-plugins`）
- 产品基线：night worktree tip `800414d`；core `professional-workflow/`（21 文件）；冻结 Backbone 未触碰
- 本包定位：供 `tpw-absorb-gate` 作实质裁定。**本包不自行裁定采纳**，处置均为“拟/候选/待裁定”。
- 旧索引：`docs/overnight/2026-10-01/ABSORB-A2-CURSOR-INDEX.tsv` 仅作导航；旧 adopt/R/narrow 标签在本包中不作资格。
- 同仓分工：a4 负责 D/E/F 技术面、资产/支持脚本与尾部；本包负责 A/B/C 主干与工程裁决类机制（评审/验证/交接/无人值守收束中的判断部分）。两侧都未覆盖的尾部列在 §9。
- 读取方式说明：本包所有“源说法”均为**读到的原文描述**，不是我在本仓执行观察到的效果；未执行/未验证的部分已标明。

## 1. 包内机制组总览（编号供 gate 逐组裁定）

| MG | 机制组 | 主要源文件（pin 内） | 建议判断位点 | 类型 |
| --- | --- | --- | --- | --- |
| MG-1 | 前提审问与设计理由调查 | `pstack/skills/principle-attack-the-premise/SKILL.md`；`pstack/skills/why/SKILL.md` + `references/epistemics.md`；`pstack/skills/how/SKILL.md` | A / B / C 的事实与前提层 | 方法候选 |
| MG-2 | 可观察事实 vs 人类偏好；原型决策 | `pstack/skills/poteto-mode/playbooks/prototype.md`；`pstack/skills/principle-never-block-on-the-human/SKILL.md`；`playbooks/multi-phase-plan.md` step 2 | A / B / Voice 的暂停判定 | 判定规则候选 |
| MG-3 | 面向 agent 消费者的行为契约（CLI） | `cli-for-agent/skills/cli-for-agents/SKILL.md` | B（外部可观察行为） | 方法候选 |
| MG-4 | 领域结构先行与边界纪律 | `pstack/skills/principle-model-the-domain/SKILL.md`；`pstack/skills/principle-boundary-discipline/SKILL.md` | C（横向约束 B/D）；边界部分归 a4 | 方法候选（C 部分） |
| MG-5 | 验证工具链的设计与维护 | `pstack/skills/create-verification-skill/SKILL.md`；`pstack/skills/maintain-verification-skill/SKILL.md`；`pstack/docs/guide/06-verify-and-ship.md` | F（验证设计） | 方法候选 |
| MG-6 | 独立评审裁决与完成前复核 | `cursor-team-kit/skills/thermo-nuclear-review/SKILL.md`；`cursor-team-kit/skills/thermo-nuclear-code-quality-review/SKILL.md`；`thermos/skills/thermos/SKILL.md`；`pstack/skills/interrogate/SKILL.md`；`advisor/skills/advisor/SKILL.md` | F（裁决与独立性） | 方法+规则候选 |
| MG-7 | 交接格式与证据等级 | `orchestrate/skills/orchestrate/references/handoffs.md`；`references/planner.md`（`## Failure recovery`、`### Andon`） | F→Driver 交接面 | 载体/格式候选 |
| MG-8 | 无人值守收束与决定轨迹 | `pstack/skills/show-me-your-work/SKILL.md`；`pstack/skills/poteto-mode/playbooks/autonomous-run.md`；`pause-safely.md`；`session-pickup.md`；`ralph-loop/hooks/stop-hook.sh` | Driver 关闭面（含 F 证据） | 方法候选 |

多层优先级说明：本包优先选取 A/B/C 薄弱操作经验（MG-1/2/3/4 为 A/B/C 主干），同时覆盖工程裁决（MG-5/6/7/8）。同一文件的多机制拆分（如 `why` 拆出 epistemics、`prototype` 拆出自 `never-block`）与跨文件共同机制合并（MG-6 合并 thermos/cursor-team-kit/interrogate/advisor）已在本包内处理，例外保留在各组“成立条件/失败模式”里。

---

## MG-1 前提审问与设计理由调查（A/B/C）

### 1) 机制与触发情境；源锚点与已读/尚缺

| 源锚点（repo pin 内路径 · section） | 已读 | 尚缺 |
| --- | --- | --- |
| `pstack/skills/principle-attack-the-premise/SKILL.md`（全文） | 全文 | 无（该文件短小、机制自含） |
| `pstack/skills/why/SKILL.md`（`## Operating Posture`、Step 1–5、`## Output Format`、`## Common Failure Modes to Avoid`、`## Reference Files`） | 正文 | `references/investigator-prompt.md`、`references/sources/*.md` 7 类 playbook 正文未逐份读；本包只按 SKILL.md 的描述记录 |
| `pstack/skills/why/references/epistemics.md`（`## Confidence Tiers`、`## Phrasing Guide` 前半） | 五档分层与措辞规则 | 文件后半与 `synthesizer-prompt.md` 未读 |
| `pstack/skills/how/SKILL.md`（全文） | 全文 | `references/explorer-prompt.md`、`explainer-prompt.md` 未读 |
| `pstack/docs/guide/03-understand.md`（全文） | 全文 | 无 |
| `pstack/skills/poteto-mode/playbooks/investigation.md`（全文） | 全文 | 无 |

触发情境（源文所述）：

- 两次以上修复共享同一前提且都在同一 gate 失败（attack-the-premise 的 description 与 `Stop` 段）。
- 需要知道“某段代码为什么长这样/这个阈值哪来的/回归原因”时（`why`：design rationale、regressions、postmortems、data-backed thresholds）。
- 需要为改动建立 traced model（`how`：变更前理解子系统、placement/ownership/layering 问题；`how` 的 `description` 与两步复杂度分流）。

### 2) 操作、成立条件、失败模式、反例/例子

**attack-the-premise 的操作（原文 Pattern 四条 + Stop 两条）**

1. 把前提写成一句话（每个失败修复所假设的那一句）。
2. 下一次修复前做 census：按 actor 数不平衡，写成可重跑脚本（链接 `principle-build-the-lever`）。
3. 读 skew：若同一批 actor 每次运行都承担大部分不平衡，找“是什么在分配这个角色”，那才是下一个 why。
4. 移除不对称而不是补偿（轮换/随机化/移动角色；返回路径、共享池、批处理交接、周期再平衡会保留分配并增加常设工作）。
5. Stop：前提未写下且 census 未存在时不得开始下一次修复；census 在各 actor 均衡时说明前提不是原因，保留 census 作为证据。

**why 的操作（原文 Step 1–5）**

- Step 2 代码锚点：file:line、关键符号、初始 commit 列表、merge commit 里的 PR 号（pattern `(#1234)`）；用 `git blame -L`、`git log --follow -p`、`gh pr view` 取种子上下文。
- Step 3 先列可用 MCP，映射七类证据：源码控制、issue/ticket、长文档、实时聊天、基础设施可观测、错误跟踪、产品分析仓库；源码控制永远生成；目标代码有防御性特征（null/retry/timeout/feature flag）时追加 incident-postmortem playbook。
- 覆盖目标是 complete coverage map：**记录 null**，不跳过检索；“无可用 MCP”或“可证无关”才可跳过，且必须在 Sources Consulted 写明理由。
- Step 4 合成者按 `epistemics.md` 输出：The Question / Code in Question / What We Found / What We Can Reasonably Infer / Competing Hypotheses / What We Don't Know / Sources Consulted / Confidence Summary。
- epistemics 五档：Direct（作者明文写下的理由）→ Supported（多份间接证据收敛）→ Inferred（解释链清楚的推断）→ Speculative（多个解释同样成立的薄证据假设）→ Unknown（查过哪些地方、没找到，也是有效结果）。措辞规则：because/the reason is/was designed to 只能用于 Direct/Supported；Inferred 用 appears to/likely/suggests。
- Step 5 之后，若 why 是改代码的前置，把谱系发现转成 Preserve / Change / Avoid / Risk 约束集供计划使用。

**how 的操作（原文）**：简单问题一条路径直读直讲；复杂问题拆 2–4 个探索角度并行 explorer，再交单一 explainer 合成；输出 Overview / Key Concepts / How It Works / Where Things Live / Gotchas（explainer-prompt 定义，本包未读该文件）。`03-understand.md` 给出组合用法（“do why first then how”）、`/teach` 的 “convince me it fixes the cause and not the symptom” 反转式提问、`/recall` 与 Session pickup 的分工，以及陷阱：不做 traced model 就开始编辑的 agent 会在第一个像样的地方修症状。

**成立条件**

- attack-the-premise：失败必须共享单一可写下的前提，且 census 可运行；否则（census 均衡）原文明确说不是前提问题，要另找原因。
- why：证据源可访问；结论必须保持 confidence 分层。缺任一来源时结论不是被阻止，而是要明写 gap。
- how：目标子系统可被静态读取；read-only 探索为主。

**失败模式与反例**

- 把 `maybe cleaner` 当作审问结果：attack-the-premise 明确要求前提+数字 census，否则不得开始下一修复。
- census 均衡仍继续质疑前提：原文显式反例，要求转向别处并保留 census。
- why 的常见失败模式原文只写了一项：**recency bias**（把最近一次提交当成权威；当前形态常是多轮早期决定堆积的结果，要往回追）。
- epistemics 失败：用 because/the reason is 讲 Inferred/Speculative 的内容，把推断说成事实。
- 影子证据源：因“大概无关”跳过一类证据且不记录 → 输出把未搜索误报为没有理由。

**例证**：多轮修复都在同一 gate 失败时，先写前提、再按 actor 数不平衡并跑脚本；`why` 输出中 “Appears to’ 而非 ‘because’，并把 “searched ticket tracker with keywords A and B, scanned 6 PRs since 2023, grep’d string literals; none surfaced a rationale” 作为 Unknown 的具体写法（`epistemics.md` Unknown 段）。

### 3) A–F 判断位点与专业 concern；拟供哪些 Profile 何时调用

| 位点 | 专业 concern | 何时调用 | 由哪个 Profile 提议 |
| --- | --- | --- | --- |
| A：问题定义中的前提与未知 | 目标/范围/价值（A 自身） | 同一方向反复失败、或未知项会改变方向 | `intent-voice`；Driver 在“适用性有歧义”时召回 |
| B：行为约定所依赖的既有理由是推断还是事实 | 行为/兼容/UX | 要改变现有可观察行为、怀疑“现状就是要求” | `behavior-domain` |
| C：同名概念/阈值/不变量为何存在 | 领域规则/持久化/合规 | revision/snapshot/阈值等语义冲突且无文档 | `behavior-domain`（C 部分） |
| D/F 的上游输入 | 技术/证据 | why 结果是改代码前置时转约束集 | `technical-planning` / `evidence-evaluation` 接收 |

位置说明：以上是判断位点，不是固定阶段或岗位；同一任务可只调用其中一项，已适用结论可复用（Backbone §1 已对齐）。

### 4) 当前产品锚点、已覆盖、具体缺口、为何值得吸收

当前产品段落（逐条）:

- `professional-workflow/profiles/intent-voice.md` `## 心智模型`：“人类原始诉求是证据入口，不是已证实的事实。‘查找成本高’的报告不等于‘经常找不到’。” `## 关键问题`：“哪些是观察事实、哪些是推断、哪些还是未知？哪个未知会改变方向？”
- `professional-workflow/profiles/behavior-domain.md` `## 心智模型`：“冲突要在约定正文显露，不能在正文里悄悄解决。” `## 常见误区`：“把技术偏好写成业务规则”。
- `professional-workflow/profiles/evidence-evaluation.md` `## 关键问题`：“依据本身有没有冲突或缺失？该退回 B、C、D 还是 A？”
- `professional-workflow/methods/behavior-claim-evaluation.md`：可证伪 claim、baseline/treatment；`## Verdict mapping`。
- `professional-workflow/authority/RESPONSIBILITY-BACKBONE.md` §1：“任务命中已接受的 applicability trigger … 已有适用结论可直接复用”。

已覆盖：事实/推断/未知的**区分原则**；依据冲突的上交路线；可证伪 claim 的测量结构。

具体缺口：

1. 没有任何“前提审问”操作：现有文本能提示“这和事实不一样”，但没有“两次失败共享同一前提 → 写前提 + actor census + 找分配者”的判定程序与停止规则。
2. 没有理由调查（rationale investigation）方法：产品有“事实/推断/未知”的标签，但没有“去哪里找、覆盖哪些证据类别、null 怎么记、confidence 怎么分层与措辞”的操作。
3. 缺“已搜索但未找到”作为有效交付的写法；这与 Backbone §2 “缺少无关材料不阻断继续”互补，但产品正文没有具体形态。
4. 缺变更前的 traced model 输出形状（how 的 Overview/Key Concepts/…），而 `implementation.md` `## 心智模型` 只写“实现是发现事实的地方…发现要记录”，没有“先建模型再编辑”的操作面。

为何值得吸收：这三项直接服务 A/B/C 的责任判断，且都能在不引入 runtime/多 agent 平台的前提下独立使用；现有产品已有接受“事实/推断/未知”的上位原则，吸收是补操作而非加职责。

### 5) 拟保留/改变/删除与原因；载体落点；耦合拆除；SDK/runtime 依赖

**拟保留（原样机制）**：attack-the-premise 的“写前提 + census + 移除不对称/均衡即另找原因”；epistemics 五档与措辞规则；Unknown 的“已搜哪些地方”写法；how 的简单/复杂分流与 traced model 输出。

**拟改变（去宿主化）**：

- why 的“七类 MCP/证据源”不能作为固定清单，改为“可用证据源可归类到这些典型类别、以本次环境实际可用为准；不可用的类别记录为 gap 而非失败”。源文本身的 coverage-map 语义允许这样处理。
- why 的多 subagent 并行探索与 synthesizer 拆分：改为“在需要时按证据类别分头搜索，主线程合成”，不要求固定 agent 数。
- “MCP 缺失则类别不可查”的假设要改为“该类证据可经其他受权渠道获取时照常尝试，否则记 gap”。

**拟删除/不吸收**：`interrogate` 式的“一模型一 reviewer”并行（除非 gate 判定 MG-6 需要，见该组）；`why` 的 `readonly:false` 具体权限设定（属于宿主工具语义，不进入产品正文）。

**载体落点（提案，待 gate）**：

- 方案 1（推荐）：`professional-workflow/methods/rationale-and-premise-review.md` 作为一个按需方法（含 attack-the-premise 操作 + 证据覆盖/confidence 分层 + traced-model 需求），并在 `methods/README.md` 的按需表新增一行，`profiles/intent-voice.md`/`behavior-domain.md` 的 `## 按需方法入口（候选）` 各加一条指向它。
- 方案 2（更小）：只扩写 `methods/behavior-claim-evaluation.md` 的前置段（前提审问）并把 epistemics 作为 `guide-*` 支持文件。代价：A/C 场景会硬塞进 F 方法，责任错位。

**平台耦合拆除**：MCP 枚举/`mcps/` 目录扫描、Task `readonly`、slug 回退、`~/.cursor/rules/pstack-models.mdc` 全部去除；只保留“证据类别 → 结论置信分层 → 输出段落”的判断骨架。

**仍依赖真实 SDK/runtime 的能力**：多 MCP 实际并发查询、`gh`/`glab` 读取 PR 讨论、真实 commit blame（依赖真实 repo/SDK）；产品若只写方法正文，下游任务仍须有带这些能力的 runtime 才能执行。

### 6) 可讨论正文草稿与验证方案、边界

草稿（拟入新方法文件，约 20 行）：

```markdown
# 前提与理由审问（A/B/C 按需支持）

## Use
- 两次以上修复共享同一前提且在同一 gate 失败时。
- 需要解释“现状为何如此”、阈值/不变量来源、回归原因，再决定改动时。

## Method
1. 写前提：用一句话写出这些失败共同假设了什么。
2. 前提 census：按 actor/路径统计不平衡，写成可重跑检查；不要只凭印象。
3. 读 skew 并移除不对称（轮换/随机化/移动角色），不要用补偿性重试、缓冲或周期性再平衡掩盖分配本身。
4. 若 census 均衡，前提不是原因：保留 census 作为证据并另找原因。
5. 理由调查：先建代码锚点（path、symbol、初始 commit/PR），再从可用证据类别分别取证：源码历史、ticket、长文档、团队沟通、运行可观测、错误跟踪、产品分析。每类（含 null）都要写进 Sources；不可用类别记为 gap。
6. 结论分层：Direct / Supported / Inferred / Speculative / Unknown。限定词与分层匹配（because 只用于 Direct/Supported）。Unknown 写明搜索范围与关键词。
7. 若后续要改代码：把发现转为 Preserve / Change / Avoid / Risk 约束集，附证据指针。

## Limits
- 不要求为每个任务做完整证据覆盖；只在需要解释“为什么”或前提可疑时使用。
- 不要求多模型/多 agent；不使用真实 repo 之外的工具时，结论降级并说明。
- 不把 census 均衡的结论继续当前提；不把 Inferred 写成事实。
```

**验证方案（未执行，供 gate/B 设计）**：

- 小场景 A：构造“同一 gate 两次失败、共享前提”的案件材料，检查方法是否产出前提句 + census 设计 + 停止判定；反例材料用“census 会在均衡处停下”。
- 小场景 B：给一个只有部分证据源可用的 rationale 问题，检查输出是否在不同源缺失时给出分层与 gap，且 Unknown 的搜索范围具体。
- 边界：本方法不能替代真实业务 authority 的规则裁定；C 语义冲突仍需按 Backbone 返回业务 owner。

### 待 gate 明确的问题（不是退包条件）

- 是否值得独立成方法文件，还是应作为 `intent-voice`/`behavior-domain` 的短操作段？本包推荐独立成按需方法，理由：它同时被 A/B/C 三类判断引用，内联会导致重复与漂移。
- `interrogate` 的多模型对抗评审是否并入 MG-6 或本组？本包建议归 MG-6（评审裁决），见下。

---

## MG-2 可观察事实 vs 人类偏好；原型决策（A/B/Voice）

### 1) 机制与触发情境；源锚点与已读/尚缺

| 源锚点 | 已读 | 尚缺 |
| --- | --- | --- |
| `pstack/skills/poteto-mode/playbooks/prototype.md`（全文） | 全文 | 无 |
| `pstack/skills/principle-never-block-on-the-human/SKILL.md`（全文） | 全文 | 无 |
| `pstack/skills/poteto-mode/SKILL.md` `## Non-negotiables` 第二 bullet（AskQuestion 分类规则） | 全文（相关段） | 无 |
| `pstack/skills/poteto-mode/playbooks/multi-phase-plan.md` step 2（“Settle open questions by prototype before you write”） | 该步 | 其余步骤只与本组交接有关 |
| `pstack/docs/guide/09-make-it-yours.md` / `10-recipes-and-pitfalls.md` | **未读** | 可能含同机制的使用经验，本包未据此下结论 |

触发情境（源文所述）：即将向人类提问 “which approach / how should I / what should this do”；或一个设计/行为分叉没有先例可参照；或多阶段计划里存在开放问题。

### 2) 操作、成立条件、失败模式、反例/例子

**核心判定规则（`poteto-mode` Non-negotiables 第二 bullet，逐字要点）**：在 AskQuestion 之前先分类。**如果答案是一个你可以通过运行某样东西观察到的事实（behavior、timing、layout、output、perf，甚至 eval 能否区分），那它就不是人类该回答的**。用 Prototype playbook 画出草图，让结果决定。只有当任务是 read-only Investigation 且交付物是有引用的答案时直接回答。把问题留给“genuine product or preference call that no experiment can settle”。全自治授权下：授权覆盖的决定自己做了并报告；只有 operator 能做的决定取默认值并给出完整解释与可撤销的一句话。

**prototype 的操作（1–6）**：先锁定“原型要做的那个决定”（没有决定就没有原型，回 Feature）；设计空间开放时先收集 references/moodboard 让用户挑方向；在隔离 scratch dir 里用最轻栈做 throwaway；多方案用一个 switcher 并列（`exhaust-the-design-space` 的便宜版）；在匹配 surface 上观察（截图/日志/计时），原型里“观察就是测试，不是断言”；输出是决定 + throwaway artifact，交回 Feature/architect。

**never-block 的操作与边界**：reversible work 直接做并展示结果；irreversible（force-push、删生产数据、发外部消息）仍要确认；**产品方向来自人类，执行不阻塞**。

**成立条件**

- 分叉确实可被运行/观察判定（不是产品价值取舍）。
- 原型是 throwaway、隔离、不进生产源；比较至少两个结构上不同的候选才够（prototype 与 architect 都要求 2+ 整形状候选）。
- 人类在场与否不改变 reversible 结论：程序性自治与产品决定权分开。

**失败模式/反例**

- 把产品/偏好决定伪装成“可观察事实”去跑原型 → 原型无法settle，浪费一轮；源文用 “no experiment can settle” 作反例定义。
- 对 reversible 工作停下等许可 → 违反 never-block；源文 Why：“Every permission pause stalls the pipeline and makes the human the bottleneck.”
- 把 prototype 代码当可交付 → 源文明说 throwaway、不进生产（与 product-quality 门槛刻意反转，但仅限原型）。
- 拿单实例观察当设计定论：prototype 只做“决定”的输入，最终 shape 仍要走 design 路径。

### 3) 判断位点与 Profile 调用

| 位点 | 专业 concern | 何时调用 | 由哪个 Profile 提议 |
| --- | --- | --- | --- |
| A/Voice：向人类提问之前的分类 | 产品/价值/偏好 vs 事实 | 准备 AskQuestion/暂停前 | `intent-voice`（A 的未知项筛选） |
| B：用哪个具体行为/交互 | 行为/交互/密度 | 有 2+ 个可观察候选 | `behavior-domain` |
| Driver：bounded composition 与自治边界 | 程序足够性 | 授权边界内可自行决定时 | `driver` |

### 4) 当前产品锚点、已覆盖、具体缺口、为何值得吸收

- `profiles/intent-voice.md` `## 关键问题`：“需要人类决定的是哪一个选择，用行为/成本/风险/承诺怎么表达才可理解？”已覆盖“人类决定面”的存在。
- `profiles/intent-voice.md` `## 常见误区`：“要求 Owner 对未经解释的实现细节背书；或反过来，替 Owner 接受风险与取舍。”
- `profiles/driver.md` `## 心智模型`：“在 envelope 内可更新 Plan 绑定与 Charter，不反复申请文件清单许可。”已覆盖“不要反复要许可”的程序层。
- `authority/RESPONSIBILITY-BACKBONE.md` §1：“任务命中已接受的 applicability trigger … 应在第一个依赖该判断的下游结论、承诺或动作形成前调用”。

具体缺口：

1. 没有“提问前的分类程序”：什么答案属于可观察事实、什么属于产品/偏好/人类保留决定。产品有“需要人类决定的是哪一个选择”，但没有筛选规则。
2. 没有“用原型让结果决定”的操作以及其与生产 code 门槛的刻意反转（throwaway、isolated、无测试、决定就是交付物）。
3. 没有 reversible/irreversible 的程序性分界（never-block 的边界）与它同“人类保留决定”的关系写法。
4. `intent-voice.md` 的“事实/推断/未知”讲的是记录状态，不是“未知该由谁解决”。

为何值得吸收：它直接减少 A/Voice 的不必要人类暂停，同时不扩大执行授权；与现有“不反复申请许可”原则同向，但给出了可操作的分类与原型路径。

### 5) 拟处置与载体

- 拟保留：提问前分类规则；可观察事实→原型→由结果决定；多候选并列；throwaway 边界；reversible/irreversible 分界（用产品现有“不可逆/需人类保留”词汇重写）。
- 拟改变：把 “AskQuestion” 这种宿主工具名改为“向人类提问/暂停”；把 “use any MCP / Just do it” 的平台自治段落删除，只保留与产品 envelope 一致的“授权覆盖内自行决定、授权外返回”。
- 拟删除：原型的具体栈建议（vanilla HTML/CDN/hot reload）不进入方法正文，只作可选例子。
- 载体：两个落点可选。方案 1：`methods/guide-decision-request-vs-observation.md`（一个支持 guide）；方案 2：并入 `profiles/intent-voice.md` 的 `## 关键问题` 与 `## 常见误区` 各一条。本包倾向方案 1 + Profile 加一行入口，避免把操作细节内联进 Profile（符合执行计划“不要把经验内联进 Profile”）。

**平台耦合拆除/依赖**：只要去掉 AskQuestion/Task/`/poteto-mode` 名称即可独立；原型观察仍依赖真实 surface（浏览器/CLI/计时工具），属 F/E 的 runtime 能力。

### 6) 操作例子与验证方案

```
判定例：准备问“这个表用虚拟滚动还是分页？”
- 若答案取决于“三种数据量下首屏时间与滚动手感”→ 属可观察事实：按 prototype 做两个 variant 在同一页面切换，用计时/录制决定。
- 若答案取决于“目标用户更习惯哪种浏览方式”→ 属产品/偏好：由 Voice 提成人类可决定的选择（行为/成本影响），不替其决定。
- 若两者都重要：先原型测事实，再把参考与事实交给人类做偏好选择。
```

验证方案（未执行）：给一个真实小分叉，分别按“事实型”“偏好型”跑分类，检查是否正确路由到原型或 Voice；反例是“事实型被问回人类”或“偏好型被原型悄悄决定”。边界：原型不产生行动授权，也不改变接受承诺。

---

## MG-3 面向 agent 消费者的行为契约（B）

### 1) 机制与触发情境；源锚点与已读/尚缺

| 源锚点 | 已读 | 尚缺 |
| --- | --- | --- |
| `cli-for-agent/skills/cli-for-agents/SKILL.md`（全文） | 全文 | 无 |
| `cli-for-agent/README.md` | **未读** | 可能含使用场景，本包结论不依赖 |
| `cursor-team-kit/skills/control-cli/SKILL.md`、`control-ui/SKILL.md` | **未读** | 归 a4（E 支持），但本组第 7 条要引其存在 |

触发情境：构建/评审一个会被 coding agent 或自动化调用的 CLI；写 `--help`；或任何“人类界面的 CLI 在无头环境会卡住 agent”的场景（源文开头即此问题陈述）。

### 2) 操作、成立条件、失败模式、反例/例子

源文条目（逐项）：

1. **Non-interactive first**：每个输入都应可用 flag/flag value 表达；交互模式只能作为 flag 缺失时的 fallback，而不是反过来。Bad: `mycli deploy` → 方向键菜单；Good: `mycli deploy --env staging`。
2. **Discoverability without dumping context**：subcommand 文档各自拥有，避免每次运行打印全手册（agent 逐层发现：`mycli` → `mycli deploy --help`）。
3. **`--help` 可用**：每个 subcommand 有 `--help`，含真实 invocation 的 Examples（示例比说明文字更利于 pattern matching）。
4. **stdin/flags/pipelines**：支持 stdin（`cat config.json | mycli config import --stdin`）；避免奇怪的位置参数顺序；不要缺值就回退交互；支持链式（`mycli deploy --tag $(mycli build --output tag-only)`）。
5. **Fail fast with actionable errors**：缺 required flag 时立刻退出，给清楚消息**和正确示例 invocation**，不是挂起；示例还给出“可用值在哪查”（`Available tags: mycli build list --output tags`）。
6. **Idempotency**：agent 会重试，同一成功命令跑两次必须安全（no-op 或明确 “already done”），不能重复副作用。
7. **Destructive actions**：提供 `--dry-run` 预览；`--yes/--force` 跳确认同时为人类保留安全默认。
8. **Predictable structure**：统一 `resource` + `verb`（`mycli service list` → `mycli deploy list` → `mycli config list`）。
9. **Success output**：成功后返回机器可用数据（IDs、URLs、durations），不只有装饰性输出。

Review 清单（源文末段）：non-interactive path、layered help、examples、stdin/pipeline、error messages with invocations、idempotency、dry-run、confirmation bypass flags、consistent structure、structured success output。

**成立条件**：消费者中包含自动化/agent；命令可能被重试或缺上下文；人类仍可能直接使用（安全默认要保留）。

**失败模式/反例**：把真正的人类便利（方向键、彩色菜单）当作唯一路径，导致 agent 卡死；缺 flag 报 “missing --env” 但不给示例；错误信息只给 “invalid input”；成功输出只有装饰文本导致无法串联；把 dry-run 当成一定不触网——本组第 7 条只要求提供 dry-run，真正的“dry-run 是否真的安全”属于 MG-5 的证据要求（create-verification-skill 明确要求观察它跳过了什么，而不是相信名字）。

### 3) 判断位点与 Profile 调用

| 位点 | 专业 concern | 何时调用 | 由哪个 Profile 提议 |
| --- | --- | --- | --- |
| B：外部可观察行为与接受条件 | DevEx/自动化/安全（dry-run/幂等） | 新增/修改 CLI 行为契约时 | `behavior-domain` |
| E：flag/帮助文本/退出码实现 | 实现 | 实现阶段按契约落地 | `implementation` |
| F：无头路径与错误消息的验证 | 证据 | 验收时用真实调用取证 | `evidence-evaluation` |

### 4) 当前产品锚点、覆盖、缺口、为何值得吸收

- `profiles/behavior-domain.md` `## 心智模型`：“B 的产物是**可观察行为约定**：场景、交互、输出、异常与接受条件；例子用来暴露漏项与冲突。”
- `profiles/behavior-domain.md` `## 常见误区`：“用方便实现的行为悄悄替代接受承诺。”
- `authority/RESPONSIBILITY-BACKBONE.md` §3 B：“明确行为契约范围，把目标表达成场景、交互、输出、异常与可观察接受条件”。
- `charters/template.md` `## Work and limits` 有 “Tools and actions”。

具体缺口：

1. B 没有任何“消费者是自动化/agent”这一类的行为面：无头可运行、错误可恢复、重试安全、成功输出机器可用。
2. “异常与接受条件”在 Profile 里没有 CLI/进程行为的实例（退出码、stdout 形状、幂等语义、dry-run 的承诺）。
3. `charters/template.md` 的 tools 字段讲的是本次实例权限，不是**被交付物面向 agent 的行为契约**；两者不同，产品目前无后者。
4. 与 MG-5 的接口缺口：F 需要可观察面；CLI 无 flag 化/结构化输出会让 F 只能靠人肉 session。

为何值得吸收：这是 B 的直接扩展，且可在纯文本方法层独立使用；不需要引入任何 runtime 或特定 CLI 框架。

### 5) 拟处置与载体

- 拟保留：9 条契约条目 + review 清单；把它们作为 B 的“agent/自动化消费者”方法。
- 拟改变：`--yes/--force` 与 `--dry-run` 的措辞按产品安全词汇重写（“不可逆动作需确认/人类保留”而非“skip confirmations”）；把 Cursor/agent 特定词改为“自动化消费者”。
- 拟删除：具体 CLI 库/框架暗示（源文没有点名，保持中立）。
- 载体：方案 1（推荐）`methods/agent-facing-cli-contract.md`，`profiles/behavior-domain.md` 按需入口加一行，`methods/README.md` 按需表加一行；方案 2 作为 `charters/examples/` 的 B 例子（只能示范，不能作为方法）。B 类的其他资产（`control-cli`/`control-ui` 的驱动能力）明确留给 a4，避免与 E 的支持脚本重复。

**平台耦合/依赖**：方法正文零平台耦合；实际验证无头行为仍依赖真实可执行 CLI runtime。

### 6) 正文草稿片段与验证方案

草稿可直接由源 9 条压缩成产品语言（示例略，见 §2）。验证方案（未执行）：取一个真实 CLI，按契约跑三件事——(a) `--help` 示例可直接复制运行；(b) 缺 flag 时退出码非 0 且 stderr 含正确 invocation；(c) 同一成功命令连续两次，第二次无新增副作用；dry-run 观察实际跳过项（结合 MG-5 证据要求）。边界：本组只定义契约，不要求所有命令都实现 dry-run；由 B 的适用条件决定。

---

## MG-4 领域结构先行（C）与边界纪律（D/E，交 a4 参考）

### 1) 机制与触发情境；源锚点与已读/尚缺

| 源锚点 | 已读 | 尚缺 |
| --- | --- | --- |
| `pstack/skills/principle-model-the-domain/SKILL.md`（全文） | 全文 | 无 |
| `pstack/skills/principle-boundary-discipline/SKILL.md`（全文） | 全文 | 无（本组只做 C 归属，边界部分交 a4） |
| `pstack/skills/architect/SKILL.md`（全文，含 design-red-flags 引用） | 全文 | `references/design-red-flags.md`、`rationale-template.md`、`runner-prompt.md` 未读（设计探索主体属 D，交 a4） |
| `pstack/skills/principle-type-system-discipline/SKILL.md` | **未读** | 属 D/E 技术面，交 a4 |
| `pstack/skills/principle-outcome-oriented-execution/SKILL.md`、`principle-subtract-before-you-add/SKILL.md` | **未读** | 属设计与瘦身，交 a4 |

触发情境（model-the-domain description）：写有状态逻辑；代码大量分支或在多个文件重复同一形状假设。`architect` description：非平凡改动直接写代码会锁死错误形状。

### 2) 操作、成立条件、失败模式、反例/例子

**model-the-domain 操作（原文）**：把领域编码成结构而不是散落条件。可选结构清单：state machine（替代散落 boolean/phase/lifecycle check）；typed model（替代 loose params/重复形状假设）；map/registry/lookup table/discriminated union（替代跨文件分支）；reducer 或 command/event model（替代 ad hoc 状态突变）；**围绕一整块领域知识组织的 module**，而不是 load/validate/transform/save 这种执行顺序（原文：“Execution order is not ownership”）；围绕重复行为/所有权/不变量的 module boundary；queue/cache/index/graph/tree/normalized collection。没有现成结构时，先做两件事：这个代码**绝不能允许什么**，数据如何被读取，再找正好编码这两者的结构。

**边界纪律（供 a4 的 D/E 参考，保留在本包只是为 C/D 交界说明）**：验证/类型收窄/错误处理集中在系统边界（CLI args、config、network、外部 API）；内部信任类型、不重复校验；业务逻辑在纯函数；测试两个问题——“现在这数据是否在跨边界？”“这能不能是 shell 只是调用的纯函数？”

**成立条件**：当前形状已明显在增长（新 feature 只是给 if/else 再加一个分支、第二个必须与第一个保持同步的 boolean）才引入结构；源文明确“Do not force an abstraction. Prefer boring code if the current shape is already clear, local, and unlikely to grow.” 对“只增加间接性而不删除分支/重复规则/非法状态/生命周期风险”的抽象持怀疑。

**失败模式/反例（原文点名的三个信号）**：`新功能让既有 if/else 链又长一节`；`第二个必须与第一个同步的 boolean`；`temporal decomposition`（按阶段命名的 module 把同一领域规则重复到各步骤）。以及强制抽象（无收益的 wrapper）。

### 3) 判断位点与 Profile 调用

| 位点 | 专业 concern | 何时调用 | 由哪个 Profile 提议 |
| --- | --- | --- | --- |
| C：概念/关系/状态/不变量的表达方式 | 领域语义/持久化/业务规则 | 有状态逻辑、分支扩散、跨文件重复形状 | `behavior-domain`（C 部分） |
| D：结构选择与边界位置 | 技术设计/边界 | 形状会影响调用者依赖时 | `technical-planning`（a4 侧） |
| E：局部结构替换 | 实现 | 在承诺内的局部形状选择 | `implementation`（a4 侧） |

### 4) 当前产品锚点、覆盖、缺口、为何值得吸收

- `profiles/behavior-domain.md` `## 心智模型`：“C 的产物是**领域语义**：概念、关系、状态、不变量、规则与上下文边界；同一规则只应有一个 owner。”
- `profiles/behavior-domain.md` `## 关键问题`：“这条规则由谁拥有？状态与不变量在哪些转换下必须保持？”
- `methods/cross-module-design.md` step 3：“Locate the seam where behavior can be substituted or tested”，step 4 “decide which existing checks cover”。
- `profiles/technical-planning.md` `## 常见误区`：“把 Plan 写到每个 helper/算法，或用最少文件数代替边界判断。”

具体缺口：

1. C 有“语义必须准确、owner 唯一”的目标，但**没有“用什么结构表达领域”的可选清单**：state machine/registry/reducer/discriminated union/围绕知识组织的 module 等都不在正文。
2. 没有 temporal decomposition 的显式反模式（按阶段命名的 module 重复领域规则），这正是 C 的横向约束最常漏的。
3. “结构选择”和“抽象是否值得”的判断门槛（不做只加间接性的抽象；boring code 优先）在产品中缺席。
4. `cross-module-design.md` 的 “do not force modules to merge for depth” 与 model-the-domain 的“不强制抽象”同向，但前者只谈 module/seam，不谈领域结构。

为何值得吸收：C 的产品正文目前只有“语义准确”的抽象要求，缺“如何把语义编码进结构”的可操作面；这是 C 约束 B/D 的主要手段之一，而且完全可在纯方法层使用。

### 5) 拟处置与载体

- 拟保留：结构清单（压缩为 6–8 项）、三个反模式信号、不强制抽象的门槛、`execution order is not ownership`。
- 拟改变：把 pstack 的 principle 名称引用改为自包含方法正文（产品不做跨 skill 引用）；“先做两件事（不能允许什么/数据如何读）”保留为选型程序。
- 拟删除：无（本组不需要删除产品内容）。
- 载体：方案 1（推荐）作为 `methods/domain-structure-choice.md`（C 方法，挂 `behavior-domain` 按需入口）；方案 2 并入 `methods/cross-module-design.md` 的一个前置小节（代价：C/D 责任混在一份 D 方法里，且该文件已声明 “Method owner: D”）。本包倾向方案 1，并把 boundary-discipline 作为 a4 的 D/E 候选转交（本包不重复吸收）。

**耦合拆除**：无平台耦合；不需要改 Backbone。

### 6) 正文草稿片段与验证方案

草稿要点（可直接用的短例）：

```
选择程序：
1. 这个模块绝不能允许什么？（非法状态）
2. 数据如何被读取？（访问模式）
3. 从清单里找正好编码这两者的最小结构；找不到再讨论新结构。
4. 若引入结构只增加间接性而没删掉分支/重复规则/非法状态/生命周期风险 → 不做。
反例：给已有 if/else 加一个分支；再添一个与旧 boolean 必须同步的 boolean；把同一条规则在 load/validate/save 三个阶段各写一遍。
```

验证方案（未执行）：对一个真实的有状态小模块，先按方法选结构再实现，记录所选结构与删除的 branch/boolean 数量；反例对照是“直接加分支”的版本。边界：方法不产生重构授权，也不要求一次性重写领域模型。

---

## MG-5 验证工具链的设计与维护（F）

### 1) 机制与触发情境；源锚点与已读/尚缺

| 源锚点 | 已读 | 尚缺 |
| --- | --- | --- |
| `pstack/skills/create-verification-skill/SKILL.md`（全文） | 全文 | `references/feature-map-example/`（README+单特性范例）只从索引摘要与本文件第 3 步得知结构，未逐字读 |
| `pstack/skills/maintain-verification-skill/SKILL.md`（全文） | 全文 | 无 |
| `pstack/docs/guide/06-verify-and-ship.md`（全文） | 全文 | 无 |
| `cursor-team-kit/skills/verify-this/SKILL.md`（全文） | 全文 | 产品 M4 已吸收；本组只做对比防重复 |
| `pstack/skills/principle-prove-it-works/SKILL.md` | **未读** | 后续包/ a4 补；本组只用 guide 06 的转述 |
| `pstack/skills/blast-radius/SKILL.md` | **未读** | 与水印-5 相邻（“one fact the change is safe because of proves it by running code”），可作后续包 |

触发情境：项目没有脚本化方式证明 UI/CLI/service 行为；或已有验证 skill 需要定期审查（app 变了，feature map 会腐烂）。源文 `description` 与 `## Outcomes`。

### 2) 操作、成立条件、失败模式、反例/例子

**create-verification-skill（5 步）**

1. **Interview the repo, not the user**：从 codebase 回答，只问观察不到的。五类问题：Surface（用户实际碰什么）；Run（本地如何起：优先 repo 自己文档化的 dev command，记 ports/env/seed/auth）；Drive（已有 harness 优先：Playwright/Cypress、expect、PTY、curl-able endpoint、debug port；然后才是 generic recipe: browser/CDP、tmux/PTY、plain HTTP）；Observe（能捕获什么证据：截图、终端 transcript、response body、日志、exit code、DB state）；Isolate（两个实例能否并行；不能就必须在 skill 里写明拒绝双开共享实例，而不是冒损坏用户 session 的险）。
   若 checkout 本身不能 build/start：先修或精确报告；对“无关缺失资产阻塞启动”的情况，允许生成的一次性 scaffolding 但必须标注并在 cleanup 删除。
2. **Generate** `.cursor/skills/verify-<app>/SKILL.md`：frontmatter `name`+`description`（不写 frontmatter 就永不注册）；段：Launch（精确启动命令 + 如何判定 ready + teardown；短命 CLI/TUI 的 launch 是先 build 一次再每个 drive 用独立 PTY/tmux）；Doctor（read-only 单检查：“这个实例值得驱动吗”——进程、版本/build、port 归属、auth）；Drive（本 repo 真实 selector/命令；优先稳定 handle：ARIA label、data attribute、prompt string、route path）；**Evidence（证据标准：走真实用户路径而不是内部 setter/test-only endpoint；捕获动作与结果状态，不只最终屏幕；同时验证 side effects（写文件、插行、发消息）与可见结果；mock 只放在生产边界已隔离外部系统处；当安全路径是 dry-run/test mode 时，观察它实际跳过了什么（文件、网络、git refs），不要相信名字——有些 dry-run 仍会触网或开浏览器）**；Cleanup（拆自己起的实例，不许按进程名 kill；cleanup 移除实例与 scratch state，**绝不删除证据**；证据留在 skill 命名位置）；Helpers（脚本可执行且调用方式写在 skill body 里）。
3. **Seed feature map**：`features/README.md` + 每用户可见 feature 一文件（先做 3–5 个，来自 routes/commands/menus/docs）；四个 H2：`Sub-features`、`How to get to it (user POV)`、`Driving it with <harness>`、`Gotchas`；map 是 repo 维护的验证来源，“a proof that drives one convenient entry point is incomplete when the map lists others”。
4. **Prove the generated skill**：launch → doctor → drive 一个 feature → 捕获 evidence → cleanup；cleanup 后确认证据仍在命名位置（“a cleanup that eats the proof fails this step”）；失败迭代也要跑 cleanup 以免残留进程/端口。**未执行过的 generated skill 是 draft 不是 deliverable。**
5. 指向 `maintain-verification-skill` 维护。

**maintain-verification-skill（Outcomes/Edit scope/Pass 0–6）**

- 结局三选一并声明：clean（全 feature 有 source+live 覆盖，无 PR）/ changed（一个 PR，只含已证明的 doc、harness 或 map 修正）/ blocked（说明精确阻塞）。
- Edit scope 只允许 verification skill 自己目录；**绝不在一次 run 里改产品代码**——map 描述的行为不符时，要么是 doc drift（修 map），要么是产品回归（报告，不用文档粉饰）。
- Pass：0 定位目标（多个候选就问；没有就停在 `/create-verification-skill`，不自造目标）；1 index hygiene；2 source wave（每 feature 一个 read-only subagent，只解释、标 drift、给一条 live recipe；children 不 drive 不编辑）；3 reconcile（合并重叠 recipes；spot-check drift，不重证 clean claim）；4 **live pass**（即使 source 看起来 clean 也必须做；coordinator 拥有全部 driving；三条不变量：① 对自上次“做过意外之事”以来未 health-check 的实例不再 drive——首 drive 前 doctor、每个新 session doctor、任何失败 drive 后 doctor，doctor 看不到的失败就 reset/relaunch；② 已捕获证据必须活过每次 cleanup，且在命名位置被检查；③ 任何 drive 启动的东西不得比该 drive 的用途活得更久，失败迭代残留要清理）；5 triage（doc drift/harness gap/product gap 三类）；6 ship or stop（changed 才出一个 PR；re-read 每个 changed file）。

**guide 06 的可复用点**：finish condition 先写进首个 prompt（“text output stays byte-identical, the json parses, both run against the sample project. show me the evidence.”）；check 与 change 类型匹配表（CLI 跑真命令、UI 走 changed flow、parser/migration 重放保存输入、perf 比较前后 profile、storage 读回写入值）；“It compiles is not evidence”；confident reply without evidence 是红标。

**成立条件/失败模式**

- 生成 skill 前 checkout 必须能 build/start；否则先修或精确报告。
- dry-run/test mode 的信任前提是**被观察验证过**，不是名字。
- cleanup 与 evidence 的边界是硬条件：清理过程不得吞掉证据。
- live pass 不可因 source clean 跳过；doctor 不可省；共享实例不可双开。
- 失败模式的直接反例：未跑过的 generated skill 当成交付（第 4 步明文禁止）；“verified-unreachable” 必须带具体前提（auth、entitlement、OS、外部状态）与尝试过的路线，map 漏了前提算 drift 不算 unreachable。

### 3) 判断位点与 Profile 调用

| 位点 | 专业 concern | 何时调用 | 由哪个 Profile 提议 |
| --- | --- | --- | --- |
| F：把“协议成立吗”变成可观察验证设计与真实证据 | 验证/证据/独立性 | 项目缺脚本化验证方式；或验证 skill 需要维护 | `evidence-evaluation` |
| B：feature map 的“用户可见行为”定义 | 行为/交互 | 生成 feature map 时界定 user POV | `behavior-domain` 提供输入 |
| D/E：harness 选择（已有优先）与 cleanup | 技术/实现 | 实现阶段选 harness | `technical-planning`/`implementation` |

### 4) 当前产品锚点、覆盖、缺口、为何值得吸收

- `methods/behavior-claim-evaluation.md`：`## Use`（baseline/treatment 比较）、`## Method` 1–4、`## Verdict mapping`、`## Limits`（不评 user value、不授权 release）。
- `profiles/evidence-evaluation.md` `## 心智模型`：“F 工作面：验证设计、获取实际证据、评价证据与反例”；“三态只有 PASS / FAIL / UNVERIFIED；环境故障记 UNVERIFIED”。
- `profiles/evidence-evaluation.md` `## 常见误区`：“只验证‘能跑通’，不设计能揭示错误的负控制。”
- `methods/guide-mock-adapter-choice.md`（按需支持文件，存在）。
- `methods/guide-redacted-evidence.md`（敏感证据 custody，存在）。

已覆盖：单一 claim 的 baseline/treatment 比较与三态；mock/adapter 选择；敏感证据记录。

具体缺口：

1. **没有“如何构造可重复的驱动面”**：产品有 claim 和 baseline，但没写 launch/doctor/drive/evidence/cleanup 五段，也没有“优先已有 harness”的选择顺序。
2. **没有能力把验证面本身作为可维护对象**：feature map 的映射、drift vs regression 的分类、clean/changed/blocked 三结局，产品都没有。
3. **没有证据完整性不变量**：evidence 必须活过 cleanup、doctor-before-drive、失败迭代残留清理，这些是“复现/取证”方法正文缺失的操作面（`evidence-evaluation.md` 只写“命令、环境、输入与输出如实记录，可被他人重放”）。
4. **dry-run/test-mode 的名字不可信**这条反例在产品中完全没有，而它直接防“假安全路径”误报 PASS。
5. **cleanup 不得销毁证据**与现有 `guide-redacted-evidence.md` 的 custody 是不同问题：后者管敏感数据，前者管“证据存续”。

为何值得吸收：验证设计是 F 的主体工作之一；产品目前只覆盖“评”，不覆盖“怎么把环境做成可评”。本组内容可在纯方法层独立（不依赖 Cursor skill 目录或特定框架）。

### 5) 拟处置与载体

- 拟保留：五段结构（Launch/Doctor/Drive/Evidence/Cleanup）与“已有 harness 优先”顺序；Evidence 六条标准（真实用户路径、动作+结果状态、side effects、mock 边界、dry-run 观察、证据位置）；三条 live-pass 不变量；clean/changed/blocked 三结局；drift vs regression 分类；“未执行=草稿”门槛。
- 拟改变：
  - `.cursor/skills/verify-<app>/` 路径 → “任务本地验证 skill/脚本的所在位置”通用说法；
  - 多 subagent source wave → “按 feature 分头只读取证，主线程 reconcile”，不要求 agent 数；
  - Cursor/CDP/tmux 作为 recipe **例子**而不是规范；维持“先已有 harness”。
- 拟删除：frontmatter 注册语义、`/maintain-verification-skill` 命令名、PR 机制（产品不内置 forge 流程；只保留“修正属于验证面自身 vs 产品回归”的分类）。
- 载体：方案 1（推荐）`methods/verification-harness-design.md` + `methods/README.md` 按需表 + `profiles/evidence-evaluation.md` 入口一行；方案 2 拆成两份（生成/维护），本包不推荐——维护是生成物的一项属性，拆开会重复标准。
- 与 M4 已吸收的 `behavior-claim-evaluation.md` 的关系：后者评 claim（对象/版本/比较/三态）；本方法产出可评的环境与证据面。两者在 `methods/README.md` 应保持一条交叉引用，避免 gate 把它判为重复。

**仍依赖 runtime 的能力**：真实 browser/CDP/PTY/HTTP 驱动、截图/trace/DB 读取、隔离端口与凭证；方法层只能定义要求与证据标准。

### 6) 正文草稿（关键段）与验证方案

```markdown
## Evidence 标准（摘要）
- 走真实用户路径；不得用内部 setter 或 test-only endpoint。
- 同时记录动作与结果状态；同时验证可见结果与副作用（文件/行/消息）。
- mock 只能放在生产边界本已隔离外部系统之处。
- 安全路径（dry-run/test mode）要先观察它实际跳过了什么（文件/网络/git ref），再按名字信任。
- 证据保存在命名位置；cleanup 只清实例与 scratch，绝不动证据。

## 维护三结局
clean（全覆盖、无修正）/ changed（一个出证过的修正）/ blocked（精确阻塞）。
map 与实现不符时先分类：doc drift（修验证面）还是 product regression（报告，不粉饰）。
```

验证方案（未执行）：选一个真实小 app，按五段生成验证面并跑一次 end-to-end proof（launch→doctor→drive 一 feature→evidence→cleanup→证据仍在）；然后人为引入一个 doc drift 与一个 product regression，检查维护流程是否分别归类。边界：不要求所有项目都生成 skill；无可用驱动面时本方法只产出“缺口报告”。

---

## MG-6 独立评审裁决与完成前复核（F）

### 1) 机制与触发情境；源锚点与已读/尚缺

| 源锚点 | 已读 | 尚缺 |
| --- | --- | --- |
| `cursor-team-kit/skills/thermo-nuclear-review/SKILL.md`（全文） | 全文 | 无 |
| `cursor-team-kit/skills/thermo-nuclear-code-quality-review/SKILL.md`（全文） | 全文 | 无 |
| `thermos/skills/thermos/SKILL.md`（全文） | 全文 | 无 |
| `thermos/skills/thermo-nuclear-code-quality-review/SKILL.md`、`thermo-nuclear-review/SKILL.md`、`agents/*.md` | **未读** | thermos/README.md 中提到重复载体迁移说明；本包按 cursor-team-kit 版本为准，thermos 目录重复体留给 a4 判重 |
| `pstack/skills/interrogate/SKILL.md`（全文） | 全文 | `references/reviewer-prompt.md`、`rubric.md`、`code-quality-review.md`、`lead-judgment.md` 未读 |
| `advisor/skills/advisor/SKILL.md` + `references/briefing-template.md`（全文） | 全文 | `advisor/hooks/*.sh` 只读 stop-hook（见 MG-8 注） |
| `cursor-team-kit/skills/make-pr-easy-to-review/SKILL.md` | 全文 | 无（行为保持 + reviewability，属交付组织；本组只取其“不隐藏行为变化”纪律） |
| `cursor-team-kit/skills/review-and-ship/SKILL.md` | 全文 | 无 |
| `pstack/skills/poteto-mode/playbooks/babysit.md` | **未读** | comment triage（skeptical posture）只从 README/guide 摘要得知 |

触发情境：分支/PR 需要深度审计；准备宣称完成；卡在同一错误或失败测试；或面对“要不要加 workaround/retry/sleep/skip test”。

### 2) 操作、成立条件、失败模式、反例/例子

**thermo-nuclear-review（安全与正确性）核心**：只报 diff 中新增/修改的代码（`# Scope`）；跨 package/module 依赖的微妙交互必须追副作用；Breaking Devex 清单（改密读取方式/位置、改环境变量名或新增、改端口/网络、新增必须执行的脚本；不算破坏：新增替代运行方式、包管理器加依赖除非要求用户手工装软件）；Feature Leak（flag/internal 门后特性不得泄漏，往往微妙）；Intended Breakage（分支有意引入且范围受限 → 不浪费作者时间；但若怀疑作者未意识到完整影响或低估负面影响（例：“Delete the database” 标题）→ 仍报）；Over-reporting（误报 High 会失去信任，绝不错误标优先级，充分追到端到端再报）；Final Response（有中高优先级发现且存在 PR 时，**审计之后**再用 gh/glab 读 PR/MR 讨论核对 BugBot 与他人评论，验证后纳入并标注来源）；Critical Rules（绝不呈现研究未完成的发现；必须审计后才看 PR 讨论以保持 fresh eyes；极度彻底；不得遗漏）。

**thermo-nuclear-code-quality-review 核心**：默认 strict maintainability；code judo（行为不变、结构显著更简）；三个 presumptive blockers：PR 让文件从 <1k 变 >1k 行、引入随机 spaghetti 分支、用局部 special case 把 feature check 散到共享路径；approval bar 八条（无结构回归、无可见的大简化机会被错过、无文件尺寸爆炸、无 spaghetti 增长、无 hacky/magic 抽象、无 wrapper/cast/optional churn、无边界泄漏/canonical helper 重复、无明显可做的分解）；output 优先级（结构回归 > 大简化机会 > 分支复杂度 > 边界/类型 > 文件尺寸 > 模块化 > 可读性）；“Do not flood the review with low-value nits if there are larger structural issues.”；tone 直接但不无礼。

**thermos 编排**：并行跑两个 review 子代理（一个 bug/安全/devex/feature leak，一个 maintainability/structure），同一 scoped diff；两者回来后合成 findings：去重、重叠的更重、分歧用自己判断解决。

**interrogate 操作**：先确定 scope（diff/文件）→ **先写 intent 段落**（不确定就问人类）→ 同一 prompt+rubric 发给每个 reviewer（每模型一个，`readonly:true`）→ 合成：2+ 模型独立提出的为最高信号；lone-model 折权；去重并标注提出者；记录显式分歧 → lead judgment（不是中性聚合者）：每个发现分 act on / consider / noted / dismissed，每组给模型来源与一句理由 → 输出 Intent/Reviewers/Act On/Consider/Noted/Dismissed/Agreement Map。多模型多样性是信号来源，**不是 persona 分工**。

**advisor 检查点规则（判断部分）**：

- Checkpoints 四处：① 重大决定（架构/方法选择；难逆或大 blast radius：schema/data migration、删除或重写模块、公开 API/config 格式变化、依赖替换、auth/payments/安全敏感代码；或歧义到会实质改变工作）；② 卡住（同一错误/失败测试在**两次真正修复尝试**之后；无法从代码解释的行为；或即将伸手去抓 workaround：retry loop、sleep、宽 try/except、skip test、disable check）；③ 宣布完成前（改了逻辑或碰了不止两三个文件；先在最终总结前 consult 一次，含验证了什么与怎么验的；trivial 编辑跳过并一句话说明）；④ 应要求。
- 不得咨询的场合：routine steps、自己可验证的事、每个 checkpoint 超过一次；“如果一个任务里要 consult 超过约四次，任务应拆分或问用户”。
- Briefing（`briefing-template.md` 七段）：Checkpoint、User's request verbatim、What has happened so far（按序：查了什么/决定了/改了/试过/排除了，各带理由）、Evidence（verbatim 工具输出：错误、stack、测试输出、相关 diff hunk；可裁无关噪声并用 `[...]` 标记，**不得改写证据**）、Current state（git status --short、git diff --stat、碰过的文件、半成品）、Questions for the advisor（含选项与当前倾向及理由）、What I need back、Full transcript（路径或 not available）。保密要求：不得含 secrets；token/key/.env 值要 redact。
- 输出 verdict 三值：proceed / proceed with changes / stop；主模型是 accountable，advisor 是强第二意见不是 authority；若 advisor 对代码判断错，展示证据一次或推翻并告知用户；不 ping-pong（每个 checkpoint 至多一次 follow-up）。
- 结束前 nudge：文件自上次 consult 后有变化且回合无 consult → stop hook 发一行 `[Advisor]`；若 agent 以问号结尾（在等用户）则保持安静并保留 marker。原文还规定 never enable unasked、read-only、不与 executors 混淆。

**成立条件**

- thermo-nuclear：有明确 diff/分支；审计在 PR 讨论之前；优先级必须追到端到端才报。
- interrogate：intent 必须先显式写清；模型多元但 rubric 相同；lead judgment 必须给最终分类。
- advisor：只在四个 checkpoint；卡住判定用“两次真正尝试”与“即将 workaround”划线；这是“咨询”而非“评审通过”——不构成独立性结论，也不改变三态。

**失败模式/反例**

- 报未改动代码中的既有漏洞（Scope 违反）；把讨论里的评论当成自己的原始审计（次序违反）；误标高优先级（Over-reporting）；忽略作者有意且有范围的破坏（Intended Breakage 误报）；把“文件超 1k 行”当唯一质量指标（源文把它列为 presumptive blocker 但非全部）。
- interrogate：把“多模型共识”当真理而不作 lead judgment；把 persona 多样性当模型多样性。
- advisor：把 advisor 的 proceed 当作发布许可；把无法解释的行为用 workaround 绕过（checkpoint ② 的 carve-out）；多次 follow-up ping-pong。

### 3) 判断位点与 Profile 调用

| 位点 | 专业 concern | 何时调用 | 由哪个 Profile 提议 |
| --- | --- | --- | --- |
| F：评审裁决与完成前复核 | 安全/正确性/可维护性/DevEx | diff 审计、宣完成前、卡住时 | `evidence-evaluation`；完成前复核可由 Driver 触发但由 F 判断 |
| C/D：结构/边界质量（code judo、1k、spaghetti） | 可维护性/架构 | 结构性回退或大简化机会 | `technical-planning` 接收 |
| B：feature leak 与 devex 破坏 | 行为泄漏/兼容 | 有 flag、配置、环境变量的改动 | `behavior-domain` 的泄漏面 |
| A/Voice：intent 段落 | 目标/意图 | 评审前必须能写清 intent | `intent-voice` 提供输入 |

### 4) 当前产品锚点、覆盖、缺口、为何值得吸收

- `profiles/evidence-evaluation.md` `## 心智模型`：“独立是真实属性：评价者不得是被评价候选的实现者；正常质疑与反例不自动构成作者贡献，实质代做要重新判断该部分的独立性。”
- 同文件 `## 常见误区`：“评价者顺手改成作者，再声称独立；或‘戴不同帽子’充当独立性”；“只看实现，不回源核对 B/C 的接受状态与适用范围”。
- `methods/behavior-claim-evaluation.md` `## Verdict mapping`：PASS/FAIL/UNVERIFIED 与“Independent authorship is not part of the measurement method”。
- `authority/RESPONSIBILITY-BACKBONE.md` §3 F：“独立挑战约束作者／评价者关系，不另添顺序节点…同一外部实例可在不同时间评价两者，分别说明对象、作者关系、证据时点与覆盖”。
- `profiles/evidence-evaluation.md` `## 按需方法入口（候选）`：“验证设计方法 / 证据评价方法 / 复现/取证方法”。

具体缺口：

1. **没有评审 rubric 与被裁决质量门槛**：产品只讲独立性关系，不讲“这是一条什么级别的 finding、是否阻断、如何避免误报/漏报”，尤其缺三条实际校准规则：只评本次变更、有意破坏的例外、over-reporting 的信任代价。
2. **没有完成前独立复核的检查点纪律**：产品写“复用评价前确认本次版本/差分仍在其覆盖内”，但没有“改了逻辑/碰了多文件 → 完成前复核一次”“同一错误两次真实尝试后升级”“即将加 workaround 时升级”的操作触发。
3. **缺 workaround 的早期信号清单**（retry loop、sleep、宽 try/except、skip test、disable check）：这些是 F/E 交界处最常被静默吸收的坏证据面。
4. **缺 intent 先行的评审前置**（interrogate Step 2）：产品 `behavior-claim-evaluation` 有 claim，但评审整个 diff 时没有“先写一段 intent”的要求。
5. **缺多来源评审的合成规则**（重叠加权、显式分歧记录、lead judgment 四桶）；现有产品没有“评审意见如何合成裁决”的任何正文。

为何值得吸收：这些是 F 的裁决面操作经验，且与已冻结的“独立是真实属性”完全兼容；不引入固定 gate，只是方法内容。

### 5) 拟处置与载体

- 拟保留：
  - thermo-nuclear-review 的 Scope / Intended Breakage / Over-reporting / PR 讨论次序 / 未完成研究禁止 五条；
  - code-quality 的 approval bar 与 output 优先级（压缩成“评审发现的分级与阻断倾向”），three presumptive blockers（尤其 1k 行仅作为**强 smell** 而非机械 gate）；
  - interrogate 的 intent 先行 + 2+ 共识加权 + 显式分歧 + lead judgment 四桶 + Agreement Map；
  - advisor 的四处 checkpoint（含“两次真正尝试”“即将 workaround”）与 briefing 不得改写证据、redact secrets、“advisor 不是 authority”。
- 拟改变：
  - 去掉模型 slug、Task/`readonly`、`gh/glab` 选型（改为“可用的 forge 工具”）；
  - “thermos 双评审并行子代理”改为“按两个透镜独立评审再合成”的选项，不强制子代理；
  - 1k 行规则改为“文件尺寸突增作为强 smell，需结构理由”，避免机械阈值变成新 gate。
- 拟删除：persona 化 reviewer 分工（源文本身反对）、把 multi-model 当独立性的替代（与 Backbone 冲突的部分必须删）。
- 载体：方案 1（推荐）`methods/review-verdict.md`（评审 rubric/合成/完成前复核），`profiles/evidence-evaluation.md` 按需入口加一行；方案 2 把 rubric 部分作为 `guide-*` 支持文件、checkpoint 部分并入 `profiles/evidence-evaluation.md`。本包推荐方案 1；理由：rubric 与 checkpoint 是同一“裁决纪律”，拆开会造成两处标准。
- 与 Backbone 的冲突检查：本组**不得**引入“第二方常驻 gate”或“每任务必审”；所有触发均为条件式，且明确“咨询/评审意见不授予关闭或发布许可”。

**平台耦合拆除**：模型名、slug 回退、hooks、`/advisor` 命令全部剥离；保留的判断骨架与宿主无关。仍依赖真实 SDK/runtime 的是：多模型并行调用、forge 讨论读取、真实 diff。

### 6) 正文草稿要点与验证方案

```
评审裁决最小结构（草稿）：
1. 先写 intent 一段；写不出 → 先向来源确认，不开始评审。
2. 范围=本次新增/修改；跨模块副作用要追，但不报未改动处既有问题。
3. 发现分级：act on（真实影响正确性/安全/可维护性，会阻断真实 PR）/ consider / noted / dismissed，各给理由与证据。
4. 优先级校准：误报 High 会失去信任；追到端到端再报；有意且有范围的破坏不报，除非怀疑作者未意识到完整影响。
5. 完成前复核：改了逻辑或碰了多文件 → 独立视角复核一次；同一错误两次真实修复失败或即将加 workaround → 升级。
6. 复核者不是 authority：proceed 不构成关闭/发布许可。
```

验证方案（未执行）：准备三份材料——(a) 含一个真 High 与两个 nits 的 diff；(b) 一个“有意删除的保护”、作者已在 PR 说明的 diff；(c) 一个 reviewer 误报 High 的 diff——检查分级与阻断判断是否分别到达正确桶，且有意破坏不产生报怨；再用同一材料检查“先审计后看 PR 讨论”的次序纪律是否可操作。边界：不规定 finding 数、不要求多模型。

---

## MG-7 交接格式与证据等级（F→Driver）

### 1) 机制与触发情境；源锚点与已读/尚缺

| 源锚点 | 已读 | 尚缺 |
| --- | --- | --- |
| `orchestrate/skills/orchestrate/references/handoffs.md`（全文） | 全文 | 无 |
| `orchestrate/skills/orchestrate/references/planner.md`（`Planning rules`、`## Failure recovery`、`### Andon`、`## Comments` 摘要） | 相关段 | 脚本实现（`scripts/core/handoff.ts` 等）归 a4 |
| `orchestrate/skills/orchestrate/references/dispatcher.md`、`spawning.md` | **未读** | 归 a4（编排 runtime） |
| `orchestrate/skills/orchestrate/SKILL.md` | **未读** | 归 a4 |
| `orchestrate/skills/orchestrate/prompts/*.md` | **未读** | 本组已从 handoffs.md 获得格式要点；prompts 逐字签名/格式留待补齐或 a4 |

触发情境：多节点/多 session 工作需要在没有共享 branch、没有 status API、没有跨兄弟聊天的情况下移动信息（源文第一段）。

### 2) 操作、成立条件、失败模式、反例/例子

**主要机制（handoffs.md）**

- **Handoff 是唯一信息通道**；worker 产出一份，planner 读取并决定。统一性让树在无全局协调下保持运动。
- 结构化最终消息五段：status、branch、summary（What I did）、notes/follow-ups；脚本把最终消息逐字保存为 `<workspace>/handoffs/<task-name>.md` 并加 traceability header；**不得 enrich/sanitize**——“the planner needs the worker's words unfiltered”。
- Planner 读法五条：Status 非 success → 决定 retry/repair/clarify；Branch 注意并可被下游引用；What I did 当事实但留意与预期不符处；Notes/concerns/deviations/findings/feedback 最富信息（每条可能变成新任务；对 scoping/task clarity 的反馈尤其宝贵）；Suggested follow-ups 是候选任务（accept/reject/consolidate）。
- `Status: blocked` 是单任务死路，planner 重试/修复/澄清，树继续；只有**继续 spawn 会在整棵树产生垃圾**时才用 Andon。
- Synthetic failure handoffs：worker 无 handoff 死亡（cap-hit/OOM/tool-error/network-drop/uncaught SDK error）时脚本写 `<task>-failure.md`（含 failureMode、started/terminated/duration、last activity、last tool call、branch、SDK error 截断、Suggested next steps）。分类经验规则：cap-hit（时长 70–80 分钟且 terminal-error）、oom（OOMKilled/137）、network-drop（fetch failed/ETIMEDOUT/ECONN/socket/dns/disconnect）、tool-error（tool_use_failed）、unknown。默认重试：cap-hit/oom 缩小范围重试；network-drop 原样重试；tool-error 换模型；unknown 原样一次后放弃；同一任务两次重试后倾向 abandon 而非第三次。
- Finished-without-handoff sidecar：status=finished 但正文无 `## Status` 时写 `<task>-finished-no-handoff.md`，raw body 当 intent；可恢复则重试，否则放弃。
- **Upstream relay**：worker 在兄弟 branch 上，运行时读不到彼此；`dependsOn` 里已交接的任务，脚本把上游 handoff body 粘进下游 prompt。后果：`dependsOn` 是语义性的（不只调度门）；未声明的 dependsOn + 需要上游上下文 = worker 猜；fan-in 太长就压缩上游 handoff 而不是膨胀下游 prompt；**handoffs 逐字渲染，草率的 What I did 会污染每个下游任务**——格式是 shared-context commons。
- Verifier handoffs：`## Verification` 五值被脚本解析**持久化到目标任务的 state row**（`tasks[].verification`），让事后分类按质量桶而不是“非失败即等价”：
  - `live-ui-verified`：复现并确认修复；planner 视为已交付（除非其他发现）。
  - `unit-test-verified`：目标测试覆盖 changed path 且通过；非 UI bug 可接受；UI bug 在环境允许后追加 live 复核。
  - `type-check-only`：只有类型检查/构建通过；弱，只对纯类型改动足够；任何行为改动都要更强 verifier。
  - `verifier-blocked`：环境失败（Docker 限流、端口、缺凭证）；修复可能正确但未证；环境健康后重 spawn，或升级；**不得计入 verified**。
  - `verifier-failed`：verifier 跑了而修复没解决；出 follow-up fix 任务，不 auto-respawn。
  - 旧 `## Verdict pass | fail | inconclusive` 迁移到**最保守值**：pass→type-check-only、fail→verifier-failed、inconclusive→verifier-blocked。
  - `## Execution` 段列出每件真正跑过的事——“this section is what distinguishes a real verification from pattern-matching”。
- Merges are tasks：planner 不写代码；merge 由 worker 任务完成（scopedGoal 指明两个 branch 与冲突策略、dependsOn 门控两个兄弟、acceptance 含 typecheck）。
- Continuous motion：planner 在 children 可能仍有 handoff 时不算 done；新 handoff 到达后读它、改结论、发 follow-up、产出新 handoff；只有停止发布且所有 in-flight 任务终态才硬停。
- **Measurements**：worker 自报 `## Measurements`；task 声明 `measurements[]` 时脚本在 worker branch 上重跑每条命令，numeric drift >10% 或单位不符写 `attention.log`；worker 仍照常 handoff，由 planner 决定是否 respawn。
- Planner 的 planning rules 相关条：默认出 verifier；`verify` 是具体检查 recipe（workers 当目标行为读，verifier 从 target 继承）；`measurements[]` 用于定量声明；fan-in 保持小（很多上游则先发一个 aggregation worker）；path overlap 最小化，必要时列 forbidden paths；任务 spec 放 plan.tasks，共享工件放 git 按路径引用。
- Andon 边界（planner.md）：只在“继续 spawn 会产生垃圾时”raise：bad upstream output、broken acceptance、不可恢复 auth/infra；**任务自己的 snag 属于它的 handoff，不是 Andon**。Andon reason 由 operator 输入、上限 500 字符。

**成立条件**：节点间确实不能共享 branch/状态；planner 有决定权；verifier 与 worker 是不同实例；measurements 是可重跑命令。

**失败模式/反例**：把 handoff 当日志或摘要而不是唯一通道；planner enrich/sanitize（去掉 worker 原话）；用聚合状态替代逐任务 handoff；把 `type-check-only` 当“已验证”；`verifier-blocked` 被算作通过；在兄弟节点间直接共享 branch 或让 worker 互相 chat；用 Andon 表达单任务卡住（阻塞整棵树）；两次重试后仍盲目第三次；把 merge 交给 planner 自己写。

### 3) 判断位点与 Profile 调用

| 位点 | 专业 concern | 何时调用 | 由哪个 Profile 提议 |
| --- | --- | --- | --- |
| F：证据等级与“实际执行了什么” | 验证/证据 | 任何跨实例交接验证结果 | `evidence-evaluation` 产出、`driver` 接收与路由 |
| Driver：依赖排序、重试/放弃、Andon、关闭 | 程序性 | 上游失败、上下文传递、终止判断 | `driver`（Backbone §4） |
| E：worker 自测如何写进证据 | 实现 | 交出自测时 | `implementation` |

### 4) 当前产品锚点、覆盖、缺口、为何值得吸收

- `profiles/driver.md` `## 交接与召回`：“交出：可执行的安排与路由、必要的对象指针；短消息承载路由与状态，事实与结论落持久产物。”
- `profiles/driver.md` `## 关键问题`：“并行写者的写集是否明确？共享文件是否单写者串行集成？”
- `profiles/evidence-evaluation.md` `## 交接与召回`：“交出：对象/版本、依据、观察、覆盖限制与 PASS/FAIL/UNVERIFIED；单列实际独立性。”
- `authority/RESPONSIBILITY-BACKBONE.md` §2：“下游能找到本次相关、适用且足够的结论、条件、依据、决定责任与接受状态”。
- `charters/template.md` `## Handoff and return`：Deliver / Independence / Recall / Acceptance。

具体缺口：

1. **没有手交的具体字段形状**：产品说“短消息承载路由、产物承载事实”，但没有 handoff 的必备段（status/branch/summary/notes/follow-ups）与“逐字保存不得改写”的纪律。
2. **证据等级只有三态，缺操作态**：`verifier-blocked`（环境失败）在产品中只能笼统进 UNVERIFIED；源把 UNVERIFIED 拆得更可操作（blocked vs failed vs type-check-only vs unit vs live），并规定旧标签向最保守值迁移。
3. **缺“Execution 段区分真验证与模式匹配”** 这一显式要求。
4. **缺定量声明的独立复跑**：`measurements[]` + >10% drift 检查在产品无对应面；`behavior-claim-evaluation.md` 有“同一命令/数据/环境”的要求，但没有“声明的数字可被重跑并自动 flag 偏差”。
5. **缺失败恢复的默认策略与 Andon 边界**（单任务 snag vs 整树垃圾）；Driver 现有正文只说“缺关闭授权时返回委托来源”，没有重试/降级/放弃的默认阶梯。
6. **缺上游上下文经 dependsOn 显式传递的要求**（未声明依赖 + 需要上游 = 猜）。

为何值得吸收：Driver 的跨实例工作质量几乎全由交接面决定；现有产品只有原则（“产物指针 + 短消息”）而无形状。此组不与任何 runtime 绑定：字段与判断可独立使用。

### 5) 拟处置与载体

- 拟保留：handoff 五段与“唯一通道/不改写”纪律；planner 读法五条；阻塞 vs Andon 边界；失败 handoff 的分类与重试阶梯（去掉脚本触发，保留判断）；verifier 五值及其 planner 响应；Execution 段；measurements 的“可重跑 + 阈值 flag”；dependsOn 的语义性；merges are tasks；continuous motion。
- 拟改变：
  - 去 `state.json`、`attention.log`、Slack、脚本、cloud agent 术语：改为“状态记录/失败日志（若存在）”“可用的通知渠道”；
  - 五值改为产品词汇：live-verified / test-verified / type-check-only / blocked / failed，并在 `evidence-evaluation.md` 的三态映射表中写清（blocked→UNVERIFIED+记录阻断，failed→FAIL）；**不新增第四态**，只增加可操作的子类别与交接字段。
  - Modern 版旧 `## Verdict` 迁移规则保留为“缺字段时取最保守解释”。
- 拟删除：Slack 权限清单、`operator-mode`、comment retry queue、agent-manager 等 runtime 细节（归 a4 或直接排除）。
- 载体：方案 1（推荐）`methods/handoff-and-evidence-grading.md`（支持文件，可在 `methods/README.md` 按需表出现），并在 `profiles/driver.md` 的 `## 交接与召回` 与 `profiles/evidence-evaluation.md` 的 `## 交接与召回` 各加一行指针；方案 2 作为 `charters/template.md` 的 filling guide（代价：非任务绑定也需手交时无所依附）。本包推荐方案 1。

**仍依赖真实 runtime 的能力**：把 handoff 真正持久化并让下游按 dependsOn 读取、measurements 自动重跑（源是脚本能力）；产品方法层只能规定字段与判断。

### 6) 正文草稿（verifier 段）与验证方案

```markdown
## Verification（五值，向产品三态映射）
- live-verified: 在目标 surface 上复现并确认行为；planner 可视为已交付。
- test-verified: 目标测试覆盖 changed path 并通过；非 UI 改动可接受；UI 需补 live。
- type-check-only: 只有类型/构建通过；仅对纯类型改动足够，行为改动不算。
- blocked: 环境失败（端口/凭证限流等）；修复可能正确但未证，不得计入通过；记 UNVERIFIED + 阻断原因。
- failed: 跑了而未解决；记 FAIL，出修复任务。
以上是证据等级的子类，不改变 PASS/FAIL/UNVERIFIED 的判定语义。

## Execution
列出每件真正执行过的命令与结果。本段是区分“已验证”与“模式匹配”的依据。
```

验证方案（未执行）：用一次真实跨实例交接检查 (a) 下游是否能在不询问上游的情况下继续；(b) `type-check-only` 是否被正确判弱；(c) 定量声明被重跑时 >10% 偏差是否被标出。边界：不要求每次交接都带 measurements；只有定量声明才需要。

---

## MG-8 无人值守收束与决定轨迹（Driver + F）

### 1) 机制与触发情境；源锚点与已读/尚缺

| 源锚点 | 已读 | 尚缺 |
| --- | --- | --- |
| `pstack/skills/show-me-your-work/SKILL.md`（全文） | 全文 | `references/decision-log-template.tsv`、`scripts/log.sh` 未读（模板/脚本归 a4） |
| `pstack/skills/poteto-mode/playbooks/autonomous-run.md`（全文） | 全文 | 无 |
| `pstack/skills/poteto-mode/playbooks/pause-safely.md`（全文） | 全文 | 无 |
| `pstack/skills/poteto-mode/playbooks/session-pickup.md`（全文） | 全文 | 无 |
| `ralph-loop/hooks/stop-hook.sh`（全文）、`ralph-loop/skills/ralph-loop/SKILL.md`（开头） | 全文/开头 | `ralph-loop/README.md`、`skills/ralph-loop/SKILL.md` 其余、`skills/cancel-ralph/SKILL.md`、`hooks/capture-response.sh` 未读 |
| `advisor/hooks/stop-hook.sh`（全文） | 全文 | 其余 advisor hooks（归 a4） |
| `pstack/docs/guide/07-overnight.md` | **未读** | 可能含无人值守使用经验，后续包/ a4 补 |

触发情境：长时间/自主/多阶段运行；人类走开后再审（“going to bed / trust it when i'm back / /loop until X”）；会话需要安全暂停或从上一代理接续；或循环任务的终止条件。

### 2) 操作、成立条件、失败模式、反例/例子

**show-me-your-work（决定轨迹）**

- 唯一 canonical log：一个 TSV，一行一个决定。列：`ts`（ISO8601）、`phase`、`decision`（一行）、`why`（plain words；用原则时“说人话而非术语 tag”）、`evidence`（指针：commit SHA、PR 号、`file:line`、artifact/trace/screenshot 路径，**绝不是段落**）、`result`（`tests green`、`reverted`、`pixel-diff 0`、`INCONCLUSIVE`、`open`）。
- 记录“决定点与检查点”，不记每个动作：选择了的分叉、完成的单元及其验证结果、pivot/revert 及其触发、浮出的 blocker、修好的 gate；循环 run 每次迭代一行；跳过 trivial。
- Append-only：错的行用新行 supersede，**绝不编辑或删除历史**。
- Run 定义：一个 agent 对话（含后续回合与它的 summary）；pickup/替换 agent/新 chat = 新 run。向已有 log 追加时，本 run 第一行 phase 用 `start`（唯一用途），并命名它未写入的既有行 ts 范围与自身的 agent id。
- 位置：默认 working artifact，不提交；`decisions.tsv` 或 `.audit/<task-slug>.tsv`；**只有当工作足够重要、reviewer 需要轨迹才能信任结果时才提交**。
- **审计轨迹 vs transcript**：run 结束前，读本 run 的 transcript（本 workspace 的 `agent-transcripts/`；**不要 glob `~/.cursor/projects/*/`**，会读到无关私有聊天），逐段（从本 run 的 start 行到下一个 start 行）核对每行是否对应真实决定/动作、evidence 是否可解析并支持其声明；有未被记录的 fork/pivot/abandoned approach 是 gap，要补。**修正 log 而不是故事**：即使 invented row 也不编辑/删除，而是加 supersede 行。
- **跨模型复核轨迹**：交回前，用**不同模型家族**的 subagent 读审计轨迹与 transcript，标出用户该注意的东西（弱/缺证据的决定、被跳过或声称验证但 transcript 无据的步骤、事后看有风险的 choices、用户随手扫会漏的 gap）；回复末尾“Attention”段以 `reviewed by <model>` 开头，逐条指向具体行；`No flags` 是合法值，模型名不是。
- 复核读法：top to bottom、跟 evidence 指针、spot-check；GitHub 会把 committed TSV 渲染成表，终端用 `column -s$'\t' -t`。

**autonomous-run（exit predicate）**：先写可检查 predicate（tests green、repro fixed、N PRs merged、pixel-diff zero）；选 wake 机制（事件 watcher + 长时心跳 fallback，无事件用固定间隔）；每次迭代做证据支持的最小改动、对 predicate 验证、advance 则 commit、没帮助则 discard（“Belt-and-suspenders that might help gets reverted, not left to ride”）；mid-run 发现自己处理（broken skill 单独 PR、不 park reversible work、不 AskQuestion）；每迭代 checkpoint 一行；predicate 满足才停，**plateau 不是 stop**（继续并 pivot），**绝不 relax predicate 宣布胜利**，真 dead end 要浮出。

**pause-safely**：显式暂停才做（“keep going/going to bed”不 pause）；停在安全边界、不启新、取消嵌套 subagent；不做不可逆动作（不 push/PR）；把未提交编辑做成一个清晰 `wip:` commit（树坏就在 commit body 一句话说明）；写 off-context 的 resume note（intent、在做什么、进度与已验证、当前状态、下一步、关键文件、gotchas）；有 show-me-your-work 轨迹就指过去而不是重复。

**session-pickup**：定位 prior trail（本 workspace transcript / cloud-agent URL / pushed branch；不跨 workspace glob）；先读 metadata overview 与最后消息，再回扫 decision points，长 transcript 用 subagent 解析、主线程保留 reduced timeline；重构建操作状态（branch、已落地、open todos、决定）；**prior trail 是权威输入**，不要重derive；diff done vs pending 并命名 resume point，不重跑 prior repro；路线到匹配 playbook；**intended claims 要在真实 artifact 上验证**——prior self-report 通过不是证明。

**ralph-loop（判断部分）**：同一 prompt 反复喂回，agent 通过文件与 git 历史看见自己前一轮的工作；stop hook 逐轮：无 state → 结束；解析 frontmatter `iteration`/`max_iterations`/`completion_promise`；非数字 → 报错并清理 state（损坏保护）；done 标记存在 → 报“completion promise fulfilled at iteration N”并清理退出；`max_iterations>0 且 iteration>=上限` → 报上限并清理退出；从第二个 `---` 之后取 prompt，空则报错清理；迭代+1 原子写回（sed 到临时文件再 mv）；构造 followup（promise 非 null 时头部含 “To complete: output <promise>...</promise> ONLY when genuinely true.”）。cancel 时删 state 并报迭代数。

**advisor 的完成前 nudge（机制向，判断部分见 MG-6）**：afterFileEdit 记 pending；stop hook 仅在 status=completed、nudge 开、pending 存在时触发一次；若 last-response 去掉空白后末字符是 `?` 则安静退出并保留 marker（等待用户回答后再提醒）。

**成立条件**：长/自主/人类走开的任务；有可持久化的 workspace；transcript 可读（否则审计降级为自查并说明）。

**失败模式/反例**：

- 把“完成了”当 predicate：源文要求可检查谓词，且 plateau 与 dead end 要区分。
- 用自己的 summary 代替轨迹：源文要求审计 transcript、修正 log 不改故事。
- 单模型自查取代跨模型扫描（源文明确“Self-review is not a substitute”）。
- 编辑/删除历史行；把 working log 提交进产品（默认不提交）。
- pause 时做 push/PR 等不可逆动作；或未显式要求就自行 pause。
- pickup 时“从头验证”重做已完成工作（源文明确这是把权威 trail 当不可信）。
- 循环无完成谓词且无上限 → 源文提醒会无限运行；state 损坏时要清理而不是继续。

### 3) 判断位点与 Profile 调用

| 位点 | 专业 concern | 何时调用 | 由哪个 Profile 提议 |
| --- | --- | --- | --- |
| Driver：关闭/暂停/接续/依赖管理 | 程序性 | 无人值守、跨会话接续、显式暂停 | `driver` |
| F：轨迹审计与跨模型扫描 | 验证/证据 | 交回人类前 | `evidence-evaluation`（可作无独立评价者时的替代，但须声明不构成独立结论） |
| A/Voice：人类接受记录的交出面 | 目标/接受 | 人类走开后回来审 | `intent-voice` 接收轨迹 |

### 4) 当前产品锚点、覆盖、缺口、为何值得吸收

- `profiles/driver.md` `## 主要误区`：“独立性不可得或能力降级时，说成‘独立复核’或‘Owner 同意’；或据此伪造三态结论——如实记录真实关系。”
- `profiles/driver.md` `## 交接与召回`：“短消息承载路由与状态，事实与结论落持久产物。”
- `profiles/evidence-evaluation.md` `## 关键问题`：“结果能否被另一个会话按材料复现？”
- `authority/RESPONSIBILITY-BACKBONE.md` §4：完成/关闭权是 envelope 属性；未满足规则时 Driver 路由剩余问题。
- `profiles/intent-voice.md` `## 交接与召回`：“人类接受记录（决定、范围、条件）”。

具体缺口：

1. **没有决定轨迹的形状**：产品要求“事实与结论落持久产物”，但没有“一行一决定、evidence 是指针、append-only、supersede”的结构，也没有“何时才需要提交轨迹”。
2. **没有轨迹自身的审计**（对照 transcript、修正 log 而非故事）和跨模型扫描；这直接补 Driver 的“如实记录”原则的检查办法。
3. **没有 exit predicate / plateau / dead-end 的区分**，也没有“绝不 relax predicate”；这是无人值守最容易自欺的地方。
4. **没有 pause/pickup 的检查点纪律**：产品有 Driver 的召回/关闭，但没有“显式暂停才停、wip commit、resume note、prior trail 权威、继承 claim 要在真 artifact 复证”。
5. **没有循环终止的损坏保护与最保守解释**：ralph-loop 的“state 损坏→报错清理、done 标记→报 fulfilled、上限→报上限、promise 头部要求 ONLY genuinely true”是可以独立作为方法存在的判断纪律。

为何值得吸收：Driver 在无人值守场景的判断质量取决于轨迹与收束条件；产品已有正确原则（不伪造独立性、关闭权属 envelope），但缺操作面。

### 5) 拟处置与载体

- 拟保留：TSV 六列与 evidence 指针；记录决定点/检查点而非动作；append-only supersede；run/start 语义；审计对照 transcript（含“不跨 workspace”边界）；跨模型扫描与 Attention 段；exit predicate/plateau/不 relax；pause 检查点；pickup 权威性与复证；循环的 done/上限/损坏最保守处理。
- 拟改变：
  - `agent-transcripts/` 路径与 `column -s$'\t' -t` 保留为例子；
  - 跨模型扫描改为“用不同来源的复核者”；若产品环境无此能力，必须声明“这是自审，不构成独立结论”（不得伪装）；
  - hooks 机制（afterFileEdit/stop、followup_message）不进入产品正文，只保留“当有此类 runtime 时，nudge 应一次一批、等用户的问题不要催”的交互条件（作为边界说明）。
- 拟删除：`.audit/` 具体目录名、`scripts/log.sh`、`column` 命令依赖可留作例子但不作规范。
- 载体：方案 1（推荐）`methods/decision-trail-and-unattended-run.md`（把轨迹 + 收束 + pause/pickup 合为一份按需方法；它们共享“人类走开后的可审计性”这个目的），`profiles/driver.md` 按需入口加一行；方案 2 拆成 `guide-decision-trail.md` + 两个 playbook 摘要（本包不推荐，重复）。**明确排除**：ralph-loop 的 hook 脚本与 state-file runtime 不吸收；`never relax predicate` 与 `plateau is not a stop` 作为方法判断保留。

**仍依赖真实 runtime 的能力**：transcript 读取、决定行自动化（log.sh）、hook nudge；方法层只定义要求与判定。

### 6) 正文草稿要点与验证方案

```
轨迹（TSV）：
ts / phase / decision / why / evidence(指针) / result
- 只记决定点与检查点；append-only；错行用新行 supersede。
- 一个重要事实：轨迹不是 summary；交回前要对照原始 transcript 审计，有 fork/pivot 未记就补。

无人值守收束：
1. 开始前写可检查 predicate。
2. 每轮最小改动 + 对 predicate 验证；没推进就 revert，不“留着也许有用”。
3. 每次迭代记一行。
4. plateau 不停（换路径），dead end 浮出；绝不改 predicate 宣布胜利。
```

验证方案（未执行）：模拟一段 6 轮无人值守工作（含一次 pivot、一次 revert、一次假成功），要求轨迹能对照 transcript 还原全部决定且被跨来源复核者标出弱证据行；反例是轨迹与 transcript 不一致时审计必须发现。边界：轨迹默认不入库；不要求逐动作记录；无 transcript 或复核者时降级并声明。

---

## 8. 包级综合观察（供 gate 做覆盖/采纳判断，不是裁定）

1. **A/B/C 主干的最大空白**是“操作程序”而非“原则”。产品已有 A–F 责任与 Backbone，但缺少：提问前的事实/偏好分类（MG-2）、理由调查与前提审问（MG-1）、面向自动化消费者的行为契约（MG-3）、领域结构选择（MG-4）。
2. **工程裁决的最大空白**是“证据/评审/交接的等级与校准”：产品只有三态与独立性原则，缺评审 rubric（MG-6）、交接字段与证据子类（MG-7）、验证面建构（MG-5）、无人值守谓词与轨迹（MG-8）。
3. **风险模式（供 gate 注意）**：源仓大量内容与 Cursor runtime（Task 工具、hooks、模型 slug、cloud agent、state.json、Slack）强耦合。本包已逐组给出“拆除后的判断骨架”；凡无法拆除的能力（真实驱动、多模型、forge 讨论、自动重跑）都保留为“仍依赖真实 SDK/runtime”的说明，不作为已有效。
4. **与已吸收 M4 的重复风险**：`verify-this` 已在 `behavior-claim-evaluation.md` 吸收；本包 MG-5 是验证面建构（源 `create/maintain-verification-skill`），不是同一 claim 的 baseline/treatment 方法；MG-6 的 advisor 与 Backbone 的“独立性”不同（advisor 是第二意见，不构成独立结论，源文自己写明不是 authority）。请 gate 按机制而非文件判定。
5. **与 a4 的边界清单**：D/E/F 技术方法（architect/arena/type-system-discipline/boundary-discipline/tdd/blast-radius/design red flags）、支持脚本与 hooks 实现细节、thermos 目录的重复载体、orchestrate scripts/schemas/prompts 逐字、cursor-sdk、agent-compatibility、teaching、docs-canvas/pr-review-canvas、grok-voice、third_party 清单、create-plugin、rules（no-inline-imports、typescript-exhaustive-switch）。

## 9. 未读残余（本包未覆盖；不假装已评估）

- pstack：`playbooks/` 其余（autopilot-full/stack、babysit、hillclimb、opening-a-pr、shipping、worktree-cleanup、eval、authoring-a-skill、refactoring、perf-issue、runtime-forensics、trace-forensics、visual-parity、multi-phase-plan 余部）；`skills/` 其余（arena、swarm、tdd、teach、recall、reflect、no-comments、unslop、technical-writing、typescript-best-practices、make-bot-ui、automate-me、bro、principle-* 14 项、setup-pstack）；`automations/benny/*`；`skills/poteto-mode/references/*`、`scripts/*`；`docs/guide/00、01、02、04、05、07、08、09、10`。
- cursor-team-kit：`agents/*`、`rules/*`、`skills/check-compiler-errors、control-cli、control-ui、deslop、fix-ci、fix-merge-conflicts、get-pr-comments、loop-on-ci、new-branch-and-pr、pr-review-canvas、run-smoke-tests、weekly-review、what-did-i-get-done、workflow-from-chats`。
- thermos：`agents/*`、`skills/thermo-nuclear-*/SKILL.md`（重复体）、`README.md`、`CHANGELOG.md`。
- orchestrate：`SKILL.md`、`references/dispatcher.md`、`spawning.md`、`prompts/*`、`scripts/*`、`schemas/*`、`__tests__/*`。
- advisor：`agents/advisor-subagent.md`、其余 hooks、`CHANGELOG.md`。
- ralph-loop：`README.md`、`skills/ralph-loop/SKILL.md` 余部、`skills/cancel-ralph/SKILL.md`、`capture-response.sh`。
- continual-learning 全部、cli-for-agent README、create-plugin、cursor-sdk、agent-compatibility、teaching、docs-canvas、pr-review-canvas、grok-voice、third_party 全量、schemas/、scripts/、根 README。

上述残余不代表无机制；按计划由 a4（D/E/F、资产/支持脚本与尾部）与后续 A2R 包继续覆盖。本包只声明：已读部分足以支撑 §1 八组的判断，未读部分不作任何结论。

## 10. 包内自检（机械项，非专业裁定）

- 源 pin 与路径：均为 `ecc249f1e306fc64ddf83c7bed16cacf7c2239db` 下实际存在的路径（可在 `upstreams/cursor-plugins` 复核）。
- 未修改任何产品文件、他人文档、registry；未 commit（Driver 统一提交）。
- 每个 MG 均含 6 项要求（机制/源锚点+已读尚缺、操作与条件/失败模式/例证、判断位点与 Profile、产品段落/覆盖/缺口、处置与载体/耦合/依赖、草稿与验证方案与边界）。
- 所有“验证方案”均标注未执行；所有源说法均标注为原文描述而非本仓观察。
