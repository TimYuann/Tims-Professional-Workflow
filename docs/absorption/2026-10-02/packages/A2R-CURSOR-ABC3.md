# A2R-CURSOR-ABC3 · cursor-plugins 审核包 3（仓库现实契约 / 评审输入 / 绿色闭环 / 装配 / 承重材料补读）

- 发现者：tpw-absorb-a2r（A2r）
- 源仓：`cursor-plugins`，pin `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`（只读 locator：`.worktrees/legacy-pre-night-2026-10-01/upstreams/cursor-plugins`）
- 产品基线：night worktree；core `professional-workflow/`（21 文件）；冻结 Backbone 未触碰
- 供 `tpw-absorb-gate` 实质裁定；本包不自行裁定采纳；处置均为“拟/候选/待裁定”
- 与包 1/包 2 的关系：包 1 覆盖 A/B/C 主干与评审/交接/轨迹；包 2 覆盖原则族。本包覆盖（a）评审的输入面与评论分诊、（b）仓库现实/文档可靠性核对、（c）CI/冲突/冒烟闭环、（d）装配与 prompting 纪律、（e）包 1 标为“尚缺”的承重支持材料补读与校正。
- 边界：本包不覆盖 D/E/F 实现技术（a4）、资产与第三方 MCP、hook/脚本 runtime。本包 MG-5 只补证据、不改机制结论。

## 1. 包内机制组总览

| MG | 机制组 | 主要源文件（pin 内） | 建议判断位点 | 类型 |
| --- | --- | --- | --- | --- |
| MG-1 | 仓库现实契约与文档可靠性（冷启动/验证环/文档漂移） | `agent-compatibility/README.md`、`skills/check-agent-compatibility/SKILL.md`、`agents/startup-review.md`、`agents/validation-review.md`、`agents/docs-reliability-review.md`、`agents/compatibility-scan-review.md` | B（交付契约）+ F（现实核对） | 方法候选 |
| MG-2 | 评审输入与评论分诊 | `cursor-team-kit/skills/get-pr-comments/SKILL.md`、`cursor-team-kit/skills/pr-review-canvas/SKILL.md`、`pstack/skills/poteto-mode/references/bugbot-triage.md` | F/工程裁决 | 方法候选 |
| MG-3 | 绿色闭环：编译/CI/冒烟/合并冲突 | `cursor-team-kit/skills/{check-compiler-errors,fix-ci,loop-on-ci,run-smoke-tests,fix-merge-conflicts}/SKILL.md` | F/E 交付纪律（实现面转 a4） | 规则候选 |
| MG-4 | 装配纪律与 prompting 选择入口 | `pstack/README.md`（usage/get started/not shipped here/why no planning skills）/ `pstack/docs/guide/02-poteto-mode.md`、`04-design.md`、`05-build-and-clean.md`、`skills/setup-pstack/SKILL.md` | A/Driver（选择与装配） | 规则候选 |
| MG-5 | 承重支持材料补读与包 1/2 校正 | `interrogate/references/*`、`why/references/synthesizer-prompt.md`、`orchestrate/prompts/{worker,verifier}.md`、`show-me-your-work/{references,scripts}`、`advisor/agents/advisor-subagent.md`、`create-verification-skill/references/feature-map-example/*` | 证据核实 | 补读记录 |

---

## MG-1 仓库现实契约与文档可靠性（B + F）

### 1) 机制与触发情境；源锚点与已读/尚缺

| 源锚点 | 已读 | 尚缺 |
| --- | --- | --- |
| `agent-compatibility/README.md`（全文） | 全文 | 无 |
| `agent-compatibility/skills/check-agent-compatibility/SKILL.md`（全文） | 全文 | 无 |
| `agent-compatibility/agents/startup-review.md`（全文） | 全文 | 无 |
| `agent-compatibility/agents/validation-review.md`（全文） | 全文 | 无 |
| `agent-compatibility/agents/docs-reliability-review.md`（全文） | 全文 | 无 |
| `agent-compatibility/agents/compatibility-scan-review.md`（全文） | 全文 | 无 |
| `agent-compatibility/CHANGELOG.md` | **未读** | 版本历史（旧索引有 Unreleased 五条），对机制判断非必要 |
| `agent-compatibility/.cursor-plugin/plugin.json`、`LICENSE` | **未读** | 元数据 |
| 外部 npm 包 `agent-compatibility` | **未运行** | 评分模型只在源文描述层读取；未执行 CLI |

触发情境（README）：想知道“repo 在 agent 工作流下有多好用”；具体触发：repo 冷启动成本、能否在不必全仓循环的情况下验证小改动、文档与实际路径的漂移程度。

### 2) 操作、成立条件、失败模式、反例/例子

**四个 review 单元 + 一个 scan（`## What it includes`）**：`check-agent-compatibility`（full pass）→ `compatibility-scan-review`（raw CLI-backed scan）、`startup-review`（cold-start/bootstrap）、`validation-review`（small-change verification loop）、`docs-reliability-review`（docs reliability）。

**评分模型（README `## Score model`，原文）**：

- `Agent Compatibility Score`：最终混合分（展示给用户）。
- `Deterministic Compatibility Score`：published CLI 的原始分。
- `Startup Compatibility Score`：启动 repo 要多少猜测。
- `Validation Loop Score`：验证一个小改动有多实际。
- `Docs Reliability Score`：文档与实际 setup 路径多接近。
- 公式：`Agent Compatibility Score = round((deterministic * 0.7) + (workflow * 0.3))`。
- CLI 另报 accelerator layer（已提交的 agent 工具）；它影响建议，**不抬高** deterministic score 本身。
- 完整工作流：deterministic scan + workflow 三检查；workflow 分是三者的四舍五入平均（`check-agent-compatibility` step 6–7）。
- README 明说：**scanner 是启发式的**；“scores repo signals and surfaces likely friction, but it is not a full quality verdict on the codebase.”

**check-agent-compatibility 输出纪律（原文）**：markdown，**最小化，不用 fenced code block**；只显示一个二级标题分 `## Agent Compatibility Score: N/100`；**不展示计算过程（权重、公式、deterministic/workflow/各检查分、算术），除非用户明确要求 breakdown**；`Top fixes` 平铺优先级列表，一行一 issue，以 `- ` 开头；若 deterministic scanner 因工具环境无法运行，单独说明且**不当成 repo 缺陷、不惩罚 repo**；deterministic 与行为 findings 合进同一列表而非分节；不要额外 summary。内部计分：用具体的非整十 workflow 分而非粗桶；“如果 startup/validation/docs 大体能工作，就当作 good-with-friction，不要默认给它 60 几分”；**不因日志噪声或错误文本粗糙就给低分**。

**四个 reviewer 的评分锚点与反例纪律（逐文件）**

- startup-review：读 README/scripts/toolchain/env/工作流文档，选最可能 bootstrap 路径，在固定时间预算内尝试首次成功；首路径失败只允许少量 recovery 并记录推断；**不得仅凭 lockfile、被占用端口或既有 repo 进程推断启动失败**；只有自己的启动尝试失败或文档路径在预算内无法完成才叫 blocked/failed。锚点：≈93（主路径在预算内工作，即使需要普通本地前置如 Docker/DB）；≈84（要挖掘/recovery/比文档更重才能起）；≈68（路径可能存在但太手工/含糊/昂贵）；≈27（拿不出可信启动路径）；≈12（被 secrets/账号/基础设施挡死，无法合理访问）。偏好具体分（82/85/91）而非整十。输出纯文本（无 markdown 栅栏、无 `#`、无强调），首行 `Startup Compatibility Score: <score>/100`，随后 summary 段落与 `Problems` 列表。**Docker/本地服务等标准前置算 friction 不算 failure；若成功启动是强结果，记录摩擦但不按接近失败打分；错误消息质量次要，除非它实际阻止启动或恢复。**
- validation-review：检查声明的 test/lint/check/typecheck 路径，判断小改动是否有实用 scoped loop，试最相关路径，判断结果是否 targeted/actionable/noisy/too expensive。锚点同为 93/84/68/27/12。**不要仅因 loop 重就给 60 几分；只要 agent 仍能可靠验证，就留在好区并注明成本；噪声日志与额外 warning 只在掩盖验证结果时重要。** “偏好具体可操作问题（如 only full-repo test path exists）而非泛泛质量建议。”
- docs-reliability-review：读 README/setup/env/贡献或 agent 指南，**尽可能字面地跟随文档 setup/run 路径**，记录准确/过时/不完整/误导处。锚点同。**“Score the damage from the drift, not the mere existence of drift.”** 小漂移或过时引用不应把好 repo 拖到 60 几分，只要真实路径仍容易恢复。
- compatibility-scan-review：先试 `npx -y agent-compatibility@latest --json "<path>"`；明确在 scanner 源仓内且 published 包因环境原因失败时才回退本地入口；**只有真的试过 published 包（以及在明显可用时的本地回退）才能说 scanner 不可用**；保留 scanner 真实分、summary 方向与问题排序；**不得把 startup/validation/docs 判断混进来**；accelerator context 与 deterministic score 分开；没有问题就写 `- None.`；**scanner 可用性不是目标 repo 的缺陷**。

**成立条件**：repo 可被读与（在预算内）尝试启动/验证；或至少可做文档路径核对；scanner 可运行（否则降级为行为检查并说明）。

**失败模式/反例（源文点名）**：把 lockfile/端口占用/既有进程当作启动失败证据；把 Docker/标准前置当失败；把成功启动按接近失败打分；把噪声日志/粗糙错误文本当缺陷；把 drifted docs 的一处小漂移拖到低分；把 scanner 环境问题当 repo 缺陷；在输出里泄露权重/公式（除非被要求）；把四类检查塞进一个 agent prompt（`check-agent-compatibility` step 5：“Use one subagent per task. Do not collapse these checks into one agent prompt.”）。

### 3) 判断位点与 Profile 调用

| 位点 | 专业 concern | 何时调用 | 由哪个 Profile 提议 |
| --- | --- | --- | --- |
| B：对 agent/自动化消费者的交付契约 | DevEx/可运行性 | 新增或修改 repo 的启动/验证/文档面 | `behavior-domain` |
| F：文档/启动/验证环的现实核对 | 证据 | 宣称“可运行/可验证/文档可用”之前 | `evidence-evaluation` |
| D：把核对结果转成修复安排 | 技术/成本 | 修复漂移或验证环 | `technical-planning`（a4 侧） |

### 4) 当前产品锚点、覆盖、缺口、为何值得吸收

- `profiles/behavior-domain.md` `## 心智模型`：“B 的产物是**可观察行为约定**：场景、交互、输出、异常与接受条件。”
- `profiles/evidence-evaluation.md` `## 心智模型`：“F 工作面：验证设计、获取实际证据、评价证据与反例”；三态。
- `methods/create-verification-skill` 相关机制已在包 1 MG-5 记录（验证 skill 的 Doctor/Drive/Evidence/Cleanup）；本组是它的**前置面**：先判断 repo 是否值得/可能被驱动。
- `AGENTS.md`（项目）Diagnosis Discipline：“Establish the observed failure from actual evidence … Do not modify behavior merely because one explanation sounds plausible.”

具体缺口：

1. **没有“仓库可运行性/可验证性”的 B 面**：产品 B 讲外部行为约定，但没有“交付物给自动化消费者时的启动路径、验证环、文档与现实的差距”这一验收面。
2. **没有分数纪律与反过罚规则**：agent-compatibility 的“摩擦 vs 失败”“不以噪声/环境/单点漂移重罚”“scanner 不可用不是 repo 缺陷”是 F 评分的直接校准经验，产品 `evidence-evaluation.md` 只有“环境故障记 UNVERIFIED”的笼统规则。
3. **没有“文档漂移的伤害评分”**：docs-reliability 的“评漂移造成的伤害，不是漂移的存在”与 `guide-*` 系列的证据纪律互补，产品无。
4. **没有冷启动时间预算与“不得从间接信号推断失败”**：这两条直接可复用到任何“repo/环境能否用”的 F 判断。
5. **混合分的展示纪律与管理**：产品不一定要引入分数（分数是启发式），但“不展示计算过程除非被要求”“不做质量定论”的态度值得作为 F 的边界声明。

为何值得吸收：产品里“验证”面向 claim，缺少“验证环境/仓库本身是否可用”这一前置判断；C 类经验（启动预算、摩擦 vs 失败、漂移伤害）能减少误判 repo 为缺陷。注意评分模型本身有启发式局限，源文已自认；建议吸收**判断纪律**而非分数公式。

### 5) 拟处置与载体

- 拟保留：四检查分工（scan/startup/validation/docs）；“摩擦 vs 失败”的判定；固定时间预算；不得从间接信号推断失败；文档漂移按伤害评分；scanner 不可用不是 repo 缺陷；输出不泄露内部权重；“scanner 是启发式、不是质量定论”。
- 拟改变：**去掉分数量化**（0.7/0.3、93/84/68/27/12 锚点），改为“通过/有摩擦/不可用 + 具体阻断与前置”的定性判定；去掉 npm CLI 依赖与 Cursor agent frontmatter（`model: fast`、`readonly: true`），改为“可用时用既有扫描/静态检查，不可用则仅用行为检查并说明覆盖”。
- 拟删除：accelerator layer、JSON/Markdown/text 输出模式、本地 symlink 安装等宿主细节。
- 载体：方案 1（推荐）新增支持文件 `methods/guide-repo-reality-check.md`（B/F 前置检查：可启动、可验证、文档可信三项），并在 `profiles/evidence-evaluation.md` 与 `profiles/behavior-domain.md` 的按需入口各加一行；方案 2 并入包 1 MG-5 的验证面方法（代价：把“环境是否可用”与“claim 如何证”混在一份里，触发条件不同）。
- 与 a4 的分工：scanner 实现、CI/工具链修复归 a4；本组只保留判断纪律。

**平台耦合/依赖**：npm scanner 与四 agent 的全套调用是宿主；判断骨架零耦合。仍依赖真实 runtime 的是实际启动/验证尝试。

### 6) 正文草稿与验证方案

```
repo 现实检查（三问）
1. 冷启动：按文档路径在时间预算内能否首次成功？失败只按自己尝试的结果判定；lockfile/端口/既有进程不算证据；Docker/DB 等标准前置算 friction。
2. 验证环：小改动是否有 scoped、可行动、不太贵的检查路径？loop 重不等于差；噪声只在掩盖结果时算问题。
3. 文档可靠性：字面跟随文档，按漂移造成的伤害评分（能否恢复真实路径），不是漂移存在本身。
判定：可用 / 有摩擦（+具体前置与代价） / 不可用（+具体阻断）。
边界：扫描/评分工具不可用不判为 repo 缺陷；启发式分不是质量定论；不展示内部权重。
```

验证方案（未执行）：对一个真实 repo 做三项检查，分别记录 (a) 启动尝试结果与时间；(b) 小改动的验证路径与耗时/噪声；(c) 文档漂移点与恢复成本；反例材料为“lockfile 存在但启动成功”与“文档有小漂移但路径好走”。边界：本组不产出分数，不要求四 agent 并行。

---

## MG-2 评审输入与评论分诊（F / 工程裁决）

### 1) 机制与触发情境；源锚点与已读/尚缺

| 源锚点 | 已读 | 尚缺 |
| --- | --- | --- |
| `cursor-team-kit/skills/get-pr-comments/SKILL.md`（全文） | 全文 | 无 |
| `cursor-team-kit/skills/pr-review-canvas/SKILL.md`（全文前 120 行 + 结构与安全注入段） | 相关部分 | `template.html`、`renderer.js`、`styles.css` 未读（资产，归 a4）；文件后半未读 |
| `pr-review-canvas/skills/pr-review-canvas/SKILL.md`（4.8KB） | **未读** | 与 team-kit 版本可能重复/不同；待判重 |
| `pstack/skills/poteto-mode/references/bugbot-triage.md`（全文） | 全文 | 无 |
| `pstack/skills/poteto-mode/playbooks/babysit.md` | **未读** | 本组从 bugbot-triage 与前文摘要取得分诊机制；babysit 主流程属交付，归 a4/后续 |

触发情境：取得当前 PR 的评审意见并要可行动列表（get-pr-comments）；把 PR diff 变成可读评审走查（pr-review-canvas）；PR 上有 Bugbot/agentic security review 评论且要决定 fix/dismiss/ask（bugbot-triage）。

### 2) 操作、成立条件、失败模式、反例/例子

**get-pr-comments（原文四步）**：resolve 当前分支的 active PR → 取 review comments 与 discussion comments → **按严重度与可行动性分组** → 返回简明 action list。输出：grouped feedback summary、按优先级排序的 action list、仍需澄清的 open questions。

**pr-review-canvas（评审输入的组织）**：用 `gh api` 并行取 PR 元数据、文件 patch、评审 comments；然后**把 diff 写成给人读的走查 HTML**：header+stats、plain-English summary box、core file sections with annotations、mechanical/boilerplate 默认折叠、review checklist；可选 pseudocode summaries（冗长代码用 plain English/短伪代码展示算法，真实 diff 折叠在 “Show full implementation” 下）、内联 SVG/mermaid/ASCII 图、before/after 控制流、老新行为对比表、warning/question/gotcha callout、交互 widget。**核心评审输入纪律**：categorize files into core vs mechanical changes；`renderDiff` 自动过滤 import、折叠纯空白改动、检测移动代码（3+ 连续删除且别处相同出现 → 蓝/紫 tint）与近似移动（移动+小改）另一个紫色；评审就不必再手动跳过机械噪声。安全注入纪律（原文）：patch 字符串可能含 `</script>`，**绝不手工把 patch 字符串嵌进 JS/JSON**；先用 `jq` 存 JSON（正确转义），再用 Python 注进 template，避免 HTML 提前结束 tag。附带 review checklist 框（`.verdict`）。

**bugbot-triage（评论分诊，核心）**：目标**不是默认忽略 Bugbot，而是不再把每条评论当成必须的代码改动**。决策 rubric 三类：`fix`（评论指出 plausible 的 correctness/security/privacy/data loss/auth/billing/migration/idempotency/race/shipped-behavior 问题 → 在最低 owning PR 修，回 commit SHA 并 resolve thread）；`dismiss`（评论匹配已记录的 noisy pattern 且当前代码/上下文证明不需改 → 短理由回复并 resolve）；`ask`（novel/high-severity/security/privacy/data 相关或含糊 → 问用户而不是猜）。“When in doubt, ask. Skipping a noisy code-quality comment is cheap; skipping a real data or security bug is not.”

Learned pattern 格式（供累积）：`Confidence: candidate | recurring | strong`；`Skip when`（必须为真的条件）；`Do not skip when`（风险边界）；`Example signal`；`Source`。候选/recurring 判定：一次或两次例 → candidate；多次真实 dismissal → recurring；**只有 pattern 窄、反复验证且低风险才 strong**。

六个 recurring skip candidates（原文全部）：intentional UI/design-system visual changes（若评论只重述共享视觉默认变了，且 PR 描述/截图/设计评审/邻近代码使其显式；**不跳过**当指向 a11y、focus visibility、键盘导航、对比度或 PR 未有意改的组件 API 契约）；upstack/stack-local usage（当 Bugbot 说 export/component/helper/file unused，而 forge 的 PR 列表/diff、上层 stack diff 或 PR context 显示后面的 PR 会用；**不跳过**当当前 PR 不在 stack、符号是 public API、或所谓上层使用无法核实）；temporary duplication during parallel implementation（PR 有意小量重复以保持新路径与将被删除/替换/验证的旧路径并行；**不跳过**当重复改到 security/billing/data access/API 行为，或长期共享抽象明显降风险）；existing framework/component invariant covers the warning（共享组件、框架契约、类型不变量或单一真源已保证；**不跳过**当不变量只是假设未强制、依赖时序、或跨 async/state 边界会发散）；owner-declared follow-up or deferred cleanup（owner 明说已知 follow-up、行为未变差、非高风险区；**不跳过**当 agent 无 owner 输入、medium/high severity 产品行为、或延迟会合入新回归）；self-withdrawn/explicit false-positive rule comments（评论或后续 Bugbot 回复明确撤回/compliant/false positive 且可本地核实；**不跳过**当唯一证据是人在高风险 issue 上说“false positive”而无解释）。

**Ask by default（不得自动跳过，即使以前类似项被 dismiss 过）**：security、privacy、auth、billing、data retention、training-data、permission-boundary findings；high-severity；migration、schema、idempotency、concurrency、cross-system behavior；建议修复小且明显降风险且不改产品意图的评论。“Historical data showed humans sometimes dismiss security/data-flow comments. Treat those as owner judgment calls, not team-wide skip rules.”

两个高价值 candidate learnings（原文摘要）：**manual reimplementations of native browser behavior**（用 JS 克隆替代原生 sticky、转发 wheel/touch、mask/clip 遮挡时，Bugbot 的 logic-bug findings 被证明一贯有效——“practically never”跳过；一个 sticky-occlusion PR 六轮 pass 约十八条 finding 全部修复未 dismiss）；**contract-test drift claims are cheaply verifiable — run the test first**（当 PR 含 pin 协议/文档用语的 contract test，Bugbot 说“test 与 doc 不符”时，先在 PR tip 跑该测试再分类；红跑经验证实，绿跑是具体 disproof；注意 prose-pinning test 会因为早先 fix 轮改 prose 而漂移，重复 pass 的 lean-dismiss 启发会误判）。

**成立条件**：能解析 active PR 与评论列表；评论可分类；`ask` 的出口真实存在（用户可被问）。分诊的前提是**先用代码/测试核实，不靠倾向**（contract-test drift 的反例说明“重复 pass 就倾向 dismiss”会错）。

**失败模式/反例**：把每条评论当必改（churn）；把 noisy code-quality 评论当数据/安全问题；对 security/data 项用历史 dismiss 作团队级 skip 规则；不跑可一条命令验证的 contract test 就下结论；把 stack-local 使用当 unused 直接删；对 UI 视觉评论误跳过 a11y/键盘/对比度子项；在没有 owner 输入时判定 medium/high 产品行为为 deferred cleanup。

### 3) 判断位点与 Profile 调用

| 位点 | 专业 concern | 何时调用 | 由哪个 Profile 提议 |
| --- | --- | --- | --- |
| F：外部评论进入评审裁决前的证据核实 | 证据 | PR 有 bot/human 评论时 | `evidence-evaluation` |
| 评审裁决：fix/dismiss/ask 分桶 | 安全/数据/行为风险 | 决定是否改代码前 | `evidence-evaluation`（MG-6 的 review 方法） |
| B/C：评论涉及行为/契约/语义时 | 行为/领域 | 判断“是否真是问题” | `behavior-domain` |
| Driver：把 ask 项路由给人类 | 程序性 | 需要 owner 判断 | `driver`（Voice 承接） |

### 4) 当前产品锚点、覆盖、缺口、为何值得吸收

- `profiles/evidence-evaluation.md` `## 关键问题`：“什么观察能把‘成立’与‘不成立’分开？关键负控制是什么？”“依据本身有没有冲突或缺失？”
- `profiles/evidence-evaluation.md` `## 常见误区`：“只验证‘能跑通’”“把环境/工具故障判成产品 FAIL”。
- `profiles/behavior-domain.md` `## 常见误区`：“把技术偏好写成业务规则”。
- `pstack` 侧已在包 1 MG-6 记录了 interrogate/thermo-nuclear 的评审裁决；本组补的是**输入面**（评论→证据）与**canvas 组织**。

具体缺口：

1. **没有评论分诊规则**：产品没有“外部评审评论是证据还是必须改动”的判定；尤其没有“dismiss 必须给理由 + resolve”“ask 出口”“security/data 类永不自动 skip”。
2. **没有 learned-pattern 的置信与边界格式**：candidate/recurring/strong + skip-when/do-not-skip-when + example signal + source，可直接用于把反复 dismiss 变成受控经验（与包 2 MG-3 的 lesson promotion 衔接）。
3. **没有“先跑可验证的 claim 再分类”规则**：contract-test drift 的“一条命令就能证实/证伪”是 F 证据优先的直接体现，且明确警告重复 pass 的 lean-dismiss 启发会误判。
4. **没有评审输入的组织面**：core vs mechanical 文件分类、pseudocode 摘要、before/after 表、checklist、机械噪声自动折叠——这些让 F/评审者把注意力放在行为面。
5. **没有 diff/输入的安全注入纪律**：patch 含 `</script>` 等可能导致 HTML 提前结束；虽然属实现细节，但“评审证据的保真与安全”是可用经验。

为何值得吸收：评论分诊是团队最常发生的“工程裁决”场景之一，现有产品只有独立性原则，无分诊；canvas 的组织经验可提升 F 的证据可读性。

### 5) 拟处置与载体

- 拟保留：fix/dismiss/ask 三分类与“When in doubt, ask”；learned pattern 格式与三档 confidence；ask-by-default 清单；contract-test 先跑；native-behavior reimplementation 的默认不跳过；canvas 的 core/mechanical 分类、pseudocode 摘要、折叠机械噪声、checklist；patch 注入安全纪律。
- 拟改变：去掉 gh API 命令、HTML/CSS/JS 类名与 template 细节（可作例子）；去掉 `renderer.js` 具体函数（归 a4）；把“PR/MR”平台词改为“评审请求/变更集”；`gh`/Bugbot 品牌词一般化（“自动化评审评论”）。
- 拟删除：具体 forge 命令与页面结构模板作为规范；`build-the-lever` 实现的 HTML 组件细节。
- 载体：方案 1（推荐）新增 `methods/review-intake-and-triage.md`（评论分诊 + 评审输入组织），`profiles/evidence-evaluation.md` 按需入口加一行；方案 2 并入包 1 MG-6 的评审裁决方法（代价：分诊发生在评审之前，与裁决 rubric 的触发条件不同）。本包倾向方案 1。
- 与 a4 的分工：pr-review-canvas 的 renderer/模板实现、babysit 的观察循环转 a4；本组只保留判断与组织纪律。

**平台耦合/依赖**：forge API、HTML 渲染器、Bugbot 全去；仍依赖真实评审评论与 diff 获取能力。

### 6) 正文草稿与验证方案

```
评论分诊（草稿）
每线程先分类：
- fix：plausible 的正确性/安全/隐私/数据/认证/计费/迁移/幂等/竞态/已发布行为问题 → 在最低 owning 单元修复，回复修复证据并 resolve。
- dismiss：匹配已记录 noisy pattern 且当前代码/上下文证明无需改 → 短理由 + resolve。
- ask：novel/高严重度/安全隐私数据相关/含糊 → 问人类，不猜。
ask-by-default（不得自动 skip）：安全、隐私、认证、计费、数据保留、训练数据、权限边界、高严重度、迁移/schema/幂等/并发/跨系统行为。
先跑可验证 claim：能一条命令证实/证伪的（如 contract test）先跑再分类；重复 pass 不构成 dismiss 依据。
pattern 记录：confidence(candidate/recurring/strong) + skip when + do not skip when + example signal + source；只有窄、反复验证、低风险才 strong。
```

验证方案（未执行）：用一份含 (a) 真数据/安全评论、(b) 已知 noisy UI 评论、(c) stack-local unused 评论、(d) contract-test drift 评论 的评审列表，检查分诊是否分别落到 fix/dismiss/dismiss + 先跑测试；反例是“重复 pass 就 dismiss”导致漏掉后轮引入的 drift。边界：dismiss 必须给出理由与解除条件；ask 不得由 agent 自答。

---

## MG-3 绿色闭环：编译 / CI / 冒烟 / 合并冲突（F/E 交付纪律）

### 1) 机制与触发情境；源锚点与已读/尚缺

| 源锚点 | 已读 | 尚缺 |
| --- | --- | --- |
| `cursor-team-kit/skills/check-compiler-errors/SKILL.md` | 全文 | 无 |
| `cursor-team-kit/skills/fix-ci/SKILL.md` | 全文 | 无 |
| `cursor-team-kit/skills/loop-on-ci/SKILL.md` | 全文 | 无 |
| `cursor-team-kit/skills/run-smoke-tests/SKILL.md` | 全文 | 无 |
| `cursor-team-kit/skills/fix-merge-conflicts/SKILL.md` | 全文 | 无 |
| `cursor-team-kit/skills/new-branch-and-pr/SKILL.md` | 全文 | 无（交付打包，归包 1/MG-3 背景） |
| `pstack/skills/poteto-mode/playbooks/babysit.md` | **未读** | 完整观察循环在 a4/后续；本组仅取分诊与循环纪律 |
| 真实 CI 系统 | **未运行** | 所有命令均未执行；仅读源文 |

触发情境：编译/类型检查失败阻塞本地或 CI；PR checks 失败要看日志并迭代到绿；需要监视 PR 并修 CI；提交前/后要跑端到端冒烟；分支有冲突要非交互解决到可构建状态。

### 2) 操作、成立条件、失败模式、反例/例子

**check-compiler-errors**：跑 repo 的 compile/type-check；按文件与类型汇总错误；先修最高置信问题；重跑至干净或被阻。输出：当前状态、按文件/类别的错误摘要、已修与剩余阻断。

**fix-ci**：resolve active PR 并看 `gh pr checks --json name,bucket,state,workflow,link`；检查失败 job 并**提取第一个可行动错误**（有 GitHub Actions 日志用日志，否则用 check link 定位失败命令/服务）；应用最小安全修复；push、重查整个 check set，重复至绿。Guardrails：一次一个可行动失败；偏好最小低风险改动先于大重构；`gh pr checks` 是 PR CI 状态的 source of truth。输出：主失败 job 与根错误、按迭代顺序的修复、当前 CI 状态与下一步。

**loop-on-ci**：`gh pr checks` 是 source of truth（含所有 PR-attached checks；`gh run list` 只覆盖 GitHub Actions）。流程：resolve PR → 等之前先看当前 checks → 已失败先诊断 → pending 用 `gh pr checks --watch --fail-fast` 观察 → 每次 push 后重查完整 check set 并重复至绿。Guardrails：每次修复尽量限定单一失败原因；**不得用 `--no-verify` 绕过 hook 求推进**；若失败明显与 PR 无关且 main 已修，merge 最新 main 而不是把无关修复塞进 PR；flaky 只 retry 一次并报告 flake 证据；**每次 push 后重跑 `gh pr checks --json ...`，因为 check set 会变**。输出：当前 CI 状态、失败摘要与修复、绿后的 PR URL。

**run-smoke-tests**：为目标 app 构建前置；跑相关 smoke suite 或聚焦测试文件；失败则看 traces/logs 隔离根因；最小修复并重跑至稳定。Guardrails：**偏好确定性等待与断言而非脆弱 timeout**；重跑已通过的修复以减少 flaky 假阳性；**只有明确要求且记录时才 quarantine 测试**。输出：测试结果摘要、根因与修复、剩余 flake 风险。

**fix-merge-conflicts**：从 git status 与冲突标记检测全部冲突文件；用最小、正确性优先的编辑解决；**安全时优先保留双方，否则选能编译且保持公开行为稳定的变体**；lockfile 用包管理器重新生成而非手改；跑 compile/lint/相关测试；stage 已解决文件并总结关键决定。Guardrails：改动最小可读；不留冲突标记；冲突解决期间不做大 refactor；**不得 push 或 tag**。

**成立条件**：CI/编译/冒烟命令可运行；check set 可解析；冲突可用 git 工具解决；lockfile 有包管理器。

**失败模式/反例**：一次修多个失败原因（难定位）；用 `--no-verify`；把 flaky 当通过或无限 retry；手改 lockfile；用 timeout 等 brittle 断言；quarantine 未记录；冲突解决时顺手大改；把无关 main 修复塞进 PR；冲突解决期间 push/tag。

### 3) 判断位点与 Profile 调用

| 位点 | 专业 concern | 何时调用 | 由哪个 Profile 提议 |
| --- | --- | --- | --- |
| F/E：交付前绿色状态与失败归因 | 证据/实现 | CI 失败、编译失败、冒烟失败 | `evidence-evaluation` + `implementation` |
| F：flake 与 timeout 的证据纪律 | 验证可靠性 | 重跑与断言设计 | `evidence-evaluation` |
| Driver：迭代顺序与单因修复 | 程序性 | 多失败迭代修复 | `driver` |
| D：冲突解决后的行为稳定性判断 | 兼容 | 冲突涉及公共行为时 | `technical-planning`（a4 侧） |

### 4) 当前产品锚点、覆盖、缺口、为何值得吸收

- `profiles/implementation.md` `## 关键问题`：“自测能观察到什么？哪些关键负控制必须变红？”
- `profiles/evidence-evaluation.md` `## 常见误区`：“只验证‘能跑通’，不设计能揭示错误的负控制。”
- `methods/local-defect-feedback-loop.md` `## Method` 5：“Rerun the original scenario and relevant regression checks on the candidate version. Report exact commands, observations, deviations and remaining uncertainty.”
- `authority/RESPONSIBILITY-BACKBONE.md` §1：“约束的 mandatory/reserved 或 negotiable within X 来自其有效 authority”。

具体缺口：

1. **没有“一次一个失败原因”的迭代纪律**：产品讲复现与修复，但没有“CI 失败提取第一个可行动错误、单因修复、每次 push 后重查 check set”的操作。
2. **没有“不得绕过 hook 求推进”的明确反例**：这对证据诚实性直接相关（绕过 hook 等于自造无效证据）。
3. **没有 flake 的决定规则**：retry 一次并报告 flake 证据；`prefer deterministic waits over brittle timeouts`；quarantine 需显式要求与记录。
4. **没有冲突解决的“双方保留/公开行为稳定/lockfile 重生成/期间不 push 不 tag”纪律**。
5. **没有“无关 main 修复 merge 而不塞进 PR”的范围纪律**。
6. **冒烟测试的“构建前置 + 聚焦文件 + 根因隔离 + 最小修复”** 与包 1 MG-5 的验证面互补。

为何值得吸收：这些是 F/E 交界高频循环；产品有原则但缺单因迭代、flake 证据、hook 诚实性、冲突范围四条具体纪律。注意大部分属于交付/实现面，a4 可能也想吸收；本包提出建议落点并标注分工。

### 5) 拟处置与载体

- 拟保留：单因迭代；check set 为 source of truth 且每次 push 后重查；不得 `--no-verify`；flake retry 一次 + 证据；确定性等待优先；quarantine 需记录；冲突双方保留/公开行为稳定/lockfile 重生成/期间不 push/tag；无关 main 修复不塞 PR。
- 拟改变：去 `gh`/GitHub Actions 具体命令（改为“可用 forge/CI 工具”）与 check 名；去具体 npm 脚本名。
- 拟删除：`--watch --fail-fast` 等工具细节（可作例子）。
- 载体：方案 1（推荐）作为短支持文件 `methods/guide-green-loop.md`，在 `methods/README.md` 按需表加一行并在 `profiles/evidence-evaluation.md` 按需入口指向；方案 2 并入 `local-defect-feedback-loop.md`（代价：该文件面向局部缺陷，CI/冲突/冒烟会把范围撑宽）。本包倾向方案 1，并建议 Driver 在 golden 规则中引用。
- 与 a4 的分工：具体 CI/工具链修复、lockfile 操作归 a4；本组保留判定与纪律。

**平台耦合/依赖**：forge CLI 与 CI 系统是宿主；纪律骨架零耦合。仍依赖真实 CI/测试 runtime。

### 6) 正文草稿与验证方案

```
绿色闭环纪律（草稿）
- 编译/类型错误：按文件与类别汇总，先修最高置信项，重跑至干净或被阻。
- CI：以“变更集关联的 check set”为真源；先看当前状态；失败提取第一个可行动错误；一次修一个原因；每次 push 后重查完整集合（check set 会变）。
- 禁止：--no-verify 之类绕过 hook 求推进。
- flake：只重试一次并报告 flake 证据；用确定性等待/断言，不用脆弱 timeout；quarantine 仅在明确要求且记录时。
- 冲突：检测全部冲突文件；安全时保留双方，否则选能编译且公开行为稳定者；lockfile 用包管理器重生成；期间不 push/tag、不做大 refactor。
```

验证方案（未执行）：构造一次含两个独立失败原因的 CI 场景，检查是否按单因迭代并在每次 push 后重查；构造 flaky 测试与一次 lockfile 冲突，检查 flake 证据与重生成纪律。边界：不要求所有 repo 用同一 CI 工具；不产生 git 操作授权。

---

## MG-4 装配纪律与 prompting 选择入口（A / Driver）

### 1) 机制与触发情境；源锚点与已读/尚缺

| 源锚点 | 已读 | 尚缺 |
| --- | --- | --- |
| `pstack/README.md`（`get started`、`usage`、`just use /poteto-mode`、23 playbook 表、`skills`、`principles`、`not shipped here`、`why are there no planning skills?`、`make it yours`、`automations`） | 相关段 | 个别小节目录（`license`） |
| `pstack/docs/guide/02-poteto-mode.md`（全文） | 全文 | 无 |
| `pstack/docs/guide/04-design.md`（全文） | 全文 | 无 |
| `pstack/docs/guide/05-build-and-clean.md`（全文） | 全文 | 无 |
| `pstack/skills/setup-pstack/SKILL.md`（全文） | 全文 | 无 |
| `pstack/docs/guide/01-setup.md`、`09-make-it-yours.md` | **未读** | 安装/个性化配置细节；本组已知 setup-pstack 的机制骨架 |
| `pstack/skills/automate-me/SKILL.md` | **未读** | 从 transcript 产出个人 mode（与包 2 MG-3 的 workflow-from-chats 相邻），后续包 |

触发情境：任务开始时决定用什么 rigor/流程（“just use poteto-mode”）；prompt 怎么写才能获得证据而不是仪式；任务切换与并行隔离；设计深度要多少；何时该直接调 skill 而非走编排；模型/角色如何配置（setup-pstack）。

### 2) 操作、成立条件、失败模式、反例/例子

**选择入口（README `## get started`/`### just use`）**：两步——先 `/setup-pstack` 选推理预算与模型，再用 `/poteto-mode` 做任何需要 rigor 的事；“other skills are situational; the mode skill uses them for you as needed.” mode 是 sticky：进入后跨回合保持，playbook 匹配或任务需要 rigor 时应用，其余时候让开；说“off”可退出。mode 干三件事：把任务匹配到 playbook 并把其步骤逐字复制进 todo list；在步骤触发时路由其他 skill；写 unslopped 回复（framed for consumer and maintainer）。**23 playbook 表**（README 内）按用途分：investigation（read-only 问题）、bug fix、perf、hillclimb、runtime/trace forensics、feature、refactoring、prototype、visual parity、authoring-a-skill、eval、babysit、shipping、autonomous run、orchestrate、autopilot-full/stack、session pickup、pause safely、multi-phase plan、worktree cleanup、opening a PR（每个其他 playbook 结尾都会调用）。

**prompt 纪律（guide 02）**：“You don't write a spec. You say what's wrong or what you want, plus anything you already know that saves the agent time.” 例：`/poteto-mode users get two notifications after a retry. repro first, then fix and verify.` ——“repro first”是真实约束不是礼貌；选中的 playbook 步骤进 todo，**跳过的步骤留在列表里并写 `skip: <reason>`**。上下文足够时 prompt 可以极短（`do it`、`continue`、`keep going until done`）；mode sticky + playbook 持有结构。**切换任务说 “new task”**：长 chat 会累积上个任务上下文；说 “new task” 让 mode 重新匹配而不是继续先前 playbook；凡只想 Investigation 就写 “don't change any code yet”，否则 mid-Feature 的 mode 会把问题当下一步 feature。**并行工作给自己的工作树**：多 agent 同 repo 会抢工作树，要 upfront 隔离；开 PR playbook 本身从 worktree 工作，只在特定 base/位置时才需要说。**Pitfall：不要在 prompt 里枚举 skills**（“use /how, then /architect, then /arena…”）——playbook 已排好序，手写序列通常重排或丢掉 playbook 会保留的步骤；只在要覆盖某个具体选择时才命名 skill。

**设计深度阶梯（guide 04）**：不需要每次都有设计。粗阶梯：小而完成但不确定的改动 → 只需 `/interrogate`；跨函数边界或移动 ownership → `/architect`（自带 `/arena`）；独立决策（命名、格式、算法）→ 直接 `/arena`；覆盖矩阵/并行检查/声明 arms 的 race → `/swarm`；昂贵且难逆的 contested design → `/architect` 然后 `/interrogate`。`/poteto-mode` 已应用此阶梯（cross-boundary 自动触发 architect）。工具分工：architect 先 ground（跑 how，必要时 why），再 arena 出竞争 sketch（caller 用法先写、后类型/签名/module map）；arena 是 N 候选同题 + read-only cross-judge（不同模型家族时）+ coordinator 读完全部、选 base、graft、verify；interrogate 同 diff+intent+rubric 给不同模型家族；swarm 分片/race。默认 checkpoint：architect 默认直接进实现；要停就显式 `/architect with checkpoint`。

**构建任务 prompt 纪律（guide 05）**：bug prompt 说症状并要求先复现；feature prompt 说行为与不能变的东西（“text output stays byte-identical”）；refactor prompt 先钉行为再动结构（“record the current output first and prove it's unchanged after”）；perf prompt 说测量不是感觉；每个 prompt 路由到 playbook，playbook 补上你没打的步骤。**failing test first 只在有 cheap local test path 时**；“Don't force a test where a real command is stronger evidence.” 清理：`/deslop` 在每次 commit 前清代码 slop；`/unslop` 清 prose（PR 描述、commit body）；`/no-comments` 把注释交给非作者的新鲜眼睛（Comment Sicko；keep list：license header、public API doc comment、解释代码无法表达之物的链接、外部依赖强制的行为），它在接受后从根因修 flag；注释声称约束（“do not remove”）时，skill 提供把该 claim 编码为 type/test/lint。**Pitfall：cleanup 不是可选抛光**——带叙述注释与防御性死重的 diff 会被 reviewer 读成未完成，且多余代码是下一个 bug 藏身处；“If the diff feels padded, say `deslop it` before you commit, not after review calls it out.”

**not shipped here（README）**：pstack 引用的 `/deslop`、`control-cli`、`control-ui` 在 cursor-team-kit；`/create-skill` 与内置 babysit 是宿主；pstack 的 babysit playbook 在同词请求下取代内置。“install cursor-team-kit alongside pstack if you want the full set.”——**装配边界声明**。

**why no planning skills（README）**：作者不信 planning——“the best spec is code”；“if you do want to make a plan, /poteto-mode covers it, but it's not a default.”（这是源仓风格选择，不是普适规则；产品应保留自己的 planning 判断。）

**make it yours / setup-pstack**：`/automate-me` 从 transcript 挖出你的实际工作方式，起草 `<your-name>-mode`（保留 pstack 作底，叠加自己的 routing skill）。`/setup-pstack` 检测可用模型并写 always-applied rule `~/.cursor/rules/pstack-models.mdc`，把 role（code/judgment/review panels）映射到模型；每个 skill 读它、缺失时回落默认值；重跑保持与默认不同的 role 值、丢弃退役 role 行；预算四档（unlimited/large/medium/small → 改每个真实 slug 的 effort token，末 token 或 trailing fast 前的 token，阶梯 max>xhigh>high>medium>low；alias inherit-parent/auto 不变）；写前校验每个真实 slug 在 detected set；`arena runners`/`interrogate reviewers` 是 list（list 长度决定 fan-out 数）；`arena cross-judge pool` 也是 list 但 arena 选一个与 parent 家族不同的值。可选提一次 verification skill（项目无 `verify-*`/harness 时问一次，不反复推销）。

**成立条件**：mode/playbook 装配存在；prompt 携带目标而非 ceremony；模型角色可解析；用户愿意让流程 sticky。反例：把 playbook 已排的步骤手写进 prompt；把“new task”省掉导致串任务；多 agent 共用一个 worktree；把 cleanup 放到 review 之后；把 `/setup-pstack` 的默认模型当作自己的实际可用模型（源文要求检测/确认）；按源仓风格取消产品应有的 planning。

### 3) 判断位点与 Profile 调用

| 位点 | 专业 concern | 何时调用 | 由哪个 Profile 提议 |
| --- | --- | --- | --- |
| A：目标优先、prompt 写目标不写仪式 | 目标/约束 | 任务启动 | `intent-voice` |
| Driver：路由与装配、隔离、跳过留痕 | 程序性 | playbook/深度阶梯选择、并行隔离 | `driver`（bounded composition） |
| B：prompt 中“不能变的东西”的约束 | 行为 | feature/refactor prompt | `behavior-domain` |
| D：设计深度阶梯（何时 architect/arena/interrogate） | 技术 | 跨边界或难逆设计 | `technical-planning`（a4 侧） |

### 4) 当前产品锚点、覆盖、缺口、为何值得吸收

- `profiles/driver.md` `## 按需方法入口（候选）`：“bounded composition 方法：在接受预设与约束内组装实例，区分‘选配置’与‘授权限’。”
- `authority/RESPONSIBILITY-BACKBONE.md` §6：“Driver 在已有预设与约束内装配；缺能力时找相应专业责任…不建固定 Role matrix 或资格审批平台。”
- `profiles/intent-voice.md` `## 心智模型`：“目标与非目标同权；‘顺手优化’不是目标的一部分。”
- `profiles/behavior-domain.md` `## 常见误区`：“用方便实现的行为悄悄替代接受承诺。”
- `profiles/evidence-evaluation.md` `## 常见误区`：“把文档、字段非空、自测输出当作已验证结论。”

已覆盖：Driver 的 bounded composition 与不建 Role matrix；目标/非目标；行为约束；文档不是证据。

具体缺口：

1. **没有“任务启动 prompt 的目标化”纪律**：说目标不说 ceremony（不说“先 how 再 architect 再 arena”）；跳过步骤要留 `skip: <reason>`；极简 prompt 依赖结构而不是省略约束。
2. **没有任务切换与隔离纪律**：“new task” 重匹配；“don't change any code yet” 钉 read-only；并行工作 upfront 各自 worktree。
3. **没有设计深度阶梯**：产品有 A–F 位点与独立性，但没有“这个小改动只需独立评审 / 跨边界才要先行设计 / 独立决策直接探索 / 覆盖或 race 用分片”的按任务深度选择。
4. **没有装配边界声明**：哪些能力不在本包（“not shipped here” 的态度）——产品是 skill/method 库，同样需要说明“不包含 runtime/forge/CI 工具”，避免下游把它当全集。
5. **没有清理与注释新鲜眼睛的纪律**：产品没有“注释交非作者评审”“cleanup 是交付的一部分而非事后抛光”“注释声称的约束编码为 type/test/lint”。
6. **没有模型/角色的配置与回落纪律**：产品不预设模型，但“检测可用能力 + 缺失回落 + 只覆盖想覆盖的 role + 不在装配层创造权限”是可复用的组合纪律（与 Backbone §6 一致）。
7. **planning 的立场冲突**：源仓“不信 planning、best spec is code”与产品把 planning（D）作为独立判断责任直接冲突；吸收时必须**保留产品立场**，只吸收“按任务选择 rigor/深度”的部分。

为何值得吸收：这组是 A/Driver 的装配与选择入口，直接决定新扩展（Profiles/methods）如何被正确消费；尤其“目标化 prompt、深度阶梯、装配边界声明”是产品当前没有的操作面。

### 5) 拟处置与载体

- 拟保留：目标化 prompt 与 `skip: <reason>`；new task/read-only pin/并行 worktree 三纪律；设计深度阶梯（改写成“判断位点 + 什么时候只需要独立评审/什么时候需要上游设计判断/什么时候做覆盖分片”）；装配边界声明；cleanup 与注释新鲜眼睛；配置检测/回落/只覆盖想覆盖的 role。
- 拟改变：把 `/poteto-mode`、`/arena`、`/architect`、`/interrogate`、`/swarm`、`/deslop`、`/unslop`、`setup-pstack` 等命令名改为“可选的装配/工具形态”；模型与 effort token 机制全部去掉，只保留“能力按实际可用检测、缺失回落、不写未确认能力”；不吸收“不信 planning”（保留产品 D 责任）。
- 拟删除：pstack 模型表/slug、role line 语法、宿主规则文件路径。
- 载体：方案 1（推荐）把“目标化 prompt + 深度阶梯 + 装配边界”作为两处小改动：`profiles/driver.md` 的按需入口加“任务装配与深度选择”一行（指向新的短支持文件 `methods/guide-task-framing-and-depth.md`），清理/注释纪律并入包 2 MG-2 或 a4 的清理面；方案 2 只写进 Charter 例子（代价：无法影响非任务绑定时的选择）。
- **与 a4 的分工**：design 深度阶梯的 D 侧（architect/arena）转 a4；cleanup 的 deslop/no-comments 实现归 a4；本包保留 A/Driver 的选择入口与 prompt 纪律。

**平台耦合/依赖**：全部命令名与配置路径去耦；仍依赖真实可用的工具/模型才谈得上装配。

### 6) 正文草稿与验证方案

```
任务装配纪律（草稿）
1. prompt 写目标与已知约束（症状、不可变行为、测量、finish condition），不写 ceremony；用共享结构承载步骤。
2. 跳过的步骤在清单里留 skip: <reason>，不静默消失。
3. 切换任务显式声明（重匹配）；只想只读就钉住“不改代码”。
4. 并行写者 upfront 隔离；不共用工作树。
5. 深度选择：小而不确定的改动 → 独立评审；跨边界/移动 ownership → 先做上游设计判断；独立决策 → 候选比较；覆盖/race → 分片；难逆 → 先设计再评审。按任务，不建固定阶段。
6. 装配边界声明：哪些能力不在本包；缺能力找对应责任，不建 Role matrix。
```

验证方案（未执行）：给一个真实任务，检查 prompt 是否只含目标/约束且步骤跳过留痕；再给一个跨边界设计，检查是否按深度阶梯触发上游判断而非直接实现。边界：不要求固定工具链；不因源仓风格取消产品的 planning 判断。

---

## MG-5 承重支持材料补读与包 1/2 校正（证据核实）

### 1) 已读支持材料与它们补了什么

| 补读文件（pin 内） | 补到的内容 | 对包 1/2 的影响 |
| --- | --- | --- |
| `pstack/skills/interrogate/references/rubric.md` | 六透镜 rubric：Correctness（含幂等/并发检查）、Root Causes vs Symptoms（guard 掩盖不变量违反、retry 隐藏破损契约、type cast 静默建模错误、“指令 vs 结构”）、Structural Integrity（boundary、抽象层、耦合、数据模型匹配、bolted-on vs integrated、legacy dual-paths）、Verification（行为 vs 实现、bug 修复有测试、集成边界全路径、real vs proxy、委派/async 是否verify实际输出）、Complexity Budget、Security（追输入路径、TOCTOU） | 确认并细化包 1 MG-6 的“评审 rubric 缺口”；补充具体透镜条目与反例 |
| 同目录 `lead-judgment.md` | 过滤原则：nitpick gravity（全是 nit 就说代码大概率没问题）、hypothetical vs actual（追调用点）、premature abstraction warnings、**“I would have done it differently” 是最常见 false positive**、missing context signals（建议改作者未改的代码、把与 codebase 一致的风格当 finding、与已知约束冲突的建议）、何时该重视（多模型独立共识、具体执行路径而非假设、暴露你自己心智模型缺口、你读完想“yeah, actually”）；安全与 correctness 单模型也要更谨慎；**verdict calibration：Act On >5 条说明没过滤够；“Dismissed” 段是信任机制，不是 busywork** | 包 1 MG-6 的 lead judgment 四桶得到完整判据 |
| 同目录 `reviewer-prompt.md` | reviewer 模板：先给 intent 并“Do NOT question the intent itself”；finding 四要素（Severity critical/warning/nit、Finding、Evidence、可选 Suggestion）；好 finding 标准（引用具体代码、解释 why、区分 broken vs 不同做法、考虑 intent）；不写赞美；“An empty review is a valid outcome.” | 补充包 1 未记录的 severity 三档与 reviewer 输出模板 |
| `pstack/skills/why/references/synthesizer-prompt.md` | 合成规则：Direct/Supported 必须引用（PR#、ticket、doc URL、chat permalink、commit hash、file:line）；**“Never cite code as evidence for its own intent.”**；用户问题里嵌入的 hypothesis 只当 candidate；矛盾要并置不取一；citation 抽查核实（可读代码/MCP，不写文件）；输出八段与 Sources Consulted 的“Not searched. No matching MCP available…”写法；“better to leave an open question open than fill with a confident-sounding guess” | 确认并细化包 1 MG-1 的 why/epistemics；补充“代码不能自证意图”与 citation 抽查 |
| `orchestrate/skills/orchestrate/prompts/worker.md` | worker 最终消息七段模板（Status/Branch/What I did/**Measurements**/Verification 四值/Notes/Suggested follow-ups）；Measurements 算子 `→,<=,<,>,>=,==` 与三例；无量化写 `(none)`；质量底线（无 placeholder TODO、每个 public function 真实实现、除断言 helper 外不得 `throw new Error("not implemented")`、无叙述注释只写非显然 why、UI 交互 bug 录屏并给产物路径）；崩溃时脚本代写尸检，不要浪费回合写临终防御；branch discipline 占位符 | 包 1 MG-7 的“worker 侧”模板得到逐字结构；补充质量底线与录屏要求 |
| `orchestrate/skills/orchestrate/prompts/verifier.md` | verifier 五值定义与 planner 响应；**“Run the code. Reading the diff is not verification.”**；每验收标准用可观察行为复现（跑测试贴输出、真输入调 CLI、起服务打端点、起 UI 点查 DOM/localStorage/network、build/typecheck）；**环境失败必须 `verifier-blocked`，不得用 `type-check-only` 伪装**；想不跑就写 verdict 时置 `verifier-blocked` 并说明；UI bug 录屏；分支纪律（从 startingRef 起、把验证产物提交并 push 当前检出分支、不改名、不改目标源文件、不 merge/rebase/开 PR、分支永不合并回） | 包 1 MG-7 的 verifier 结构确认；补充“不得伪装”与“分支永不合并回” |
| `pstack/skills/show-me-your-work/references/decision-log-template.tsv` | 表头逐字：`ts	phase	decision	why	evidence	result` | 确认包 1 MG-8 |
| `pstack/skills/show-me-your-work/scripts/log.sh` | 运维/安全细节：`>>` 而非 `>`（网络挂载会让 `-s` 测试失败，代价只是一行多余表头而非丢行）；strip tab/newline/CR 保持单行；**表单公式注入防护：任何以 `=`,`+`,`-`,`@` 开头的单元格加单引号前缀**（因为 log 会用电子表格打开，攻击者可控证据如 PR 标题/文件名/生成文本不能变成公式执行）；UTC ISO8601 时间戳 | 包 1 MG-8 未记录的安全细节；建议补进吸收正文（轨迹记录的注入防护） |
| `advisor/agents/advisor-subagent.md` | 顾问方法：读完整 briefing 再形成看法；分离证据与 parent 的解释；**读 repo 与实际 diff 而非描述**（可用只读 git/grep/读文件）；大 transcript 先看文件大小、读最近部分、搜索用户消息；找 parent 最可能漏的（未测试假设、更简路径、隐藏耦合、生产失败模式、悄悄掉出范围的请求、声称验证但未运行）；**prefer one clear recommendation；若两个选项确实接近就说接近并给 tie-breaker**；回复 <约 400 词，结构 Verdict/Why/Recommendations/Risks/Answers/Confidence；规则：不编辑、不 state-changing、不自己干活、直说不谄媚、**说清核实了什么与推断了什么、绝不把猜测当事实**、缺信息时一次编号清单并要求仍给 provisional read、不 spawn subagent、resume 视为同一任务下一 checkpoint 不重验未变部分 | 包 1 MG-6 的 advisor 机制确认；补充“读实际 diff 而非描述”“<400 词”“一次 follow-up”“provisional read” |
| `create-verification-skill/references/feature-map-example/README.md` + `create-note.md` | 完整维护示例：Baseline preconditions（`http://127.0.0.1:4173`、disposable data dir、seed 数据、PATH、`control-notes doctor` 要求 URL/data dir/build revision、**Never drive an instance that was not started by this verification run**）；Driving conventions（ARIA 优先、literal 命令、restore seeded data、cleanup 不删证据）；Proof and skip reporting（捕获动作与结果状态不只最终屏、UI proof 含 ARIA snapshot + 带 app identity 的截图、CLI proof 含 command/stdout/stderr/exit code、mutation proof 含只读第二视图、记录 feature ID 与入口、不可达路径要报尝试命令与未满足前置、**不得把跳过的入口点用另一条路当已验证**）；feature entry contract 恰四 H2（Sub-features / How to get to it (user POV) / Driving it with <harness> / Gotchas）；create-note 示例的七步驱动与四条 gotchas（焦点在输入框时 `n` 会打字；title trim 要断言渲染值；save status 不是充分证据要 reopen；cleanup 删 fixture 但保留 artifact） | 包 1 MG-5 的五段结构与证据标准得到 worked example；补充“doctor 要求 build revision”“不得用另一路径替代跳过入口”“清理保留 artifact”三条 |

### 2) 是否需要对包 1/包 2 的结论做实质修正

- **无机制级推翻**。已补读文件均与包 1/2 的描述一致，且增加操作细节。
- **需要补记的三点**（建议吸收时写入，不改变结论）：
  1. show-me-your-work 的 log 写入有**公式注入防护**与网络挂载写入策略；包 1 MG-8 未提，吸收轨迹格式时应带上（证据可能含攻击者可控文本）。
  2. why 的合成禁止“用代码自证意图”，并要求 Direct/Supported 引用、citation 抽查；包 1 MG-1 只写到 confidence 分层，应把这两条补入。
  3. verifier 的“环境失败不得用 type-check-only 伪装、想不写 verdict 就 blocked”与 worker 的“崩溃时不要写临终防御”是两条强反例，包 1 MG-7 未逐字覆盖。

### 3) A–F 判断位点与 Profile 调用

| 补读项 | 位点 | 何时调用 |
| --- | --- | --- |
| interrogate rubric/lead-judgment | F 评审裁决 | 有候选评审意见需过滤时 |
| why synthesizer 规则 | A/B/C 理由调查 | 输出 rationale 结论时 |
| worker/verifier 模板 | F→Driver 交接 | 跨实例验证与自报时 |
| log.sh 防护 | Driver 轨迹 | 记录/共享决定轨迹时 |
| advisor agent | F 第二意见 | 完成前/卡住/重大决定（包 1 MG-6） |
| feature-map-example | F 验证面 | 生成/维护验证 skill 时 |

### 4) 载体与处置

- 上述补读内容不单独成方法，作为包 1/包 2 对应方法的细节并入：
  - `methods/guide-lesson-promotion.md`（包 2 MG-3）不含本组；
  - 补读 1 → 包 1 MG-8 的轨迹方法正文；
  - 补读 2 → 包 1 MG-1 的理由调查方法正文；
  - 补读 3 → 包 1 MG-7 的交接证据等级正文；
  - interrogate/advisor/feature-map 细节 → 包 1 MG-5/MG-6 的正文。
- 若 gate 决定包 1 某些机制不吸收，本组补读按其联动范围一并处理，不单独留存。

### 5) 残余

- `interrogate/references/code-quality-review.md`（5.2KB）未读；`why/references/investigator-prompt.md`、`sources/*.md` 未读；`orchestrate/prompts` 的 root/subplanner/loop-hygiene/failure-handoff/slack-block/andon-block/empty-error/finished-no-handoff 未读；`pr-review-canvas/skills/...` 第二份 SKILL 与 `template.html`/`renderer.js`/`styles.css` 未读；这些属于更深支持材料或 a4 资产面。

## 8. 包级综合观察（供 gate，不是裁定）

1. MG-1 是 B/F 的一个真实空白：产品既有 `behavior-domain`（外部行为）也有 `evidence-evaluation`（证据），但没有“交付物给自动化消费者时的可启动/可验证/文档可信”这一组验收面；建议只吸收判断纪律，不引入启发式分数。
2. MG-2 的评论分诊与包 1 MG-6 的评审裁决是上下游：分诊决定哪些评论进入证据裁决；请 gate 注意两组的接口（分诊的 `ask` 出口对应 Driver/Voice 升级）。
3. MG-3 与 a4 的实现面有重叠；本包只提交纪律层（单因迭代、hook 诚实、flake 证据、冲突范围），实现/工具链交 a4。
4. MG-4 的“目标化 prompt + 深度阶梯 + 装配边界”是 Driver bounded composition 的操作化；planning 立场冲突已标注，不吸收源仓的反 planning 主张。
5. MG-5 未发现对包 1/2 的机制级修正，仅三条补记；建议 gate 在裁定包 1/2 时把这三条并入相应结论。

## 9. 未读残余（本包未覆盖；不假装已评估）

- `agent-compatibility/CHANGELOG.md`、plugin.json、LICENSE。
- `pr-review-canvas/skills/pr-review-canvas/SKILL.md` 后半、`cursor-team-kit/skills/pr-review-canvas` 的 template/renderer/styles、`pr-review-canvas` 插件 SKILL 全文与资产。
- `pstack/skills/poteto-mode/playbooks/babysit.md`、`opening-a-pr.md`、`shipping.md`、`autopilot-*.md`、`worktree-cleanup.md`、`authoring-a-skill.md`、`eval.md`、`refactoring.md`、`perf-issue.md`、`runtime-forensics.md`、`trace-forensics.md`、`visual-parity.md`（部分在包 1/2 已列）。
- `pstack/skills/setup-pstack` 已读；`automate-me`、`no-comments`、`unslop`、`technical-writing`、`typescript-best-practices`、`make-bot-ui`、`bro`、`arena`、`swarm` SKILL 正文未读（部分属 a4）。
- 其余同仓目录与包 1 §9 相同（thermos、orchestrate scripts、advisor hooks、ralph-loop 余部、continual-learning、create-plugin、cursor-sdk、teaching、docs-canvas、grok-voice、third_party、schemas、scripts）以及 `interrogate/code-quality-review.md`、`why/references/investigator-prompt.md`/`sources/*`、`orchestrate/prompts` 其余模板。

## 10. 包内自检（机械项，非专业裁定）

- 源 pin 与路径：均为 `ecc249f1e306fc64ddf83c7bed16cacf7c2239db` 下实际存在的路径；
- 未修改产品/他人文档/registry；未 commit；
- 每组含 6 项要求（MG-5 为补读核实组，按“读什么/补什么/是否修正/位点/载体/残余”组织）；
- 所有验证方案标注未执行；源说法标注为原文描述。
