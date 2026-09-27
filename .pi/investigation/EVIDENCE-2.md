# EVIDENCE-2 · feature map 维护 / 非一次性文档 / A 归类 / skill 数量

**来源**：TPW-driver 2026-09-27 的 Owner 新增四项。**只读**：三仓 pin（`ecc249f` / `c55ee46` / `2686b62`，工作区干净）+ 本仓只读。
**边界**：本文件**不修改** `SET-A.md`（Owner 已修正：A 的建立属设计工作，不由 investigator 承担；`SET-A.md` 仅作为清点保留）。本文件只给证据与归类，不提方案。
**编号**：本批新增项用 `F-*`。

---

## ① pstack 的 feature map：怎么维护、被谁维护

### F-1.1 谁产 / 什么触发

| 问题 | 答案 | 原文锚点 |
|---|---|---|
| 谁产 | 一个**生成器技能** `/create-verification-skill`（技能目录里还有要求它"生成给下一个 agent 读的产物"的约束） | `skills/create-verification-skill/SKILL.md:9`「You write the generator's output for the next agent, not for a human: it will be read cold, mid-task, by an agent that has never seen the app.」；`docs/guide/06-verify-and-ship.md:35-37` |
| 产出物 | `.cursor/skills/verify-<app>/SKILL.md`（六段）+ `features/README.md`（索引）+ `features/<feature>.md`（一功能一文件） | `create-verification-skill/SKILL.md:25`、`:36` |
| 触发（人工） | 项目**没有脚本化驱动面**、而 agent 需要证明行为时；`/setup-pstack` 也会提议生成一次 | `docs/guide/06-verify-and-ship.md:35`「If your project has one, great. If not, run: /create-verification-skill」；`docs/guide/01-setup.md:33` |
| 触发（并行/重复验证） | 有 verify 技能后，`/swarm` 可"按 feature-map 条目"拆分整轮验证 | `docs/guide/06-verify-and-ship.md:41`；`docs/guide/06-verify-and-ship.md:39`「a step any agent can execute, in this repo, with no setup conversation」 |
| 触发（自动化） | benny 的"复现并修复"自动化把 feature map 当**配置前置**，缺失即 fail-closed | `automations/benny/skills/reproduce-and-fix-issues/SKILL.md:11`；`references/control-adapter.md:9`；`templates/reproduce-automation-prompt.md:23` |

### F-1.2 谁维护 / 怎么发现腐烂 / 粒度 / 产出什么 / 多久跑

| 问题 | 答案 | 原文锚点 |
|---|---|---|
| 谁维护 | 一个**独立的维护技能** `/maintain-verification-skill`（人/agent 显式调用；技能声明"Use for /maintain-verification-skill or 'audit the verify skill'"） | `skills/maintain-verification-skill/SKILL.md:3` |
| 怎么发现腐烂 | ① 索引卫生（README 与兄弟文件的缺项/多项/重复/死项）；② **源波**：每个 feature 文件一个**只读**子代理，说明"这个用户可见功能怎么工作"并标出疑似 doc drift（带引用）；③ **活波**：即使源码看起来干净也必须跑，逐个功能真机驱动；④ 对不上的两类分法——doc drift 修 map，产品回归则报告 | `SKILL.md:27`、`:29`、`:33`、`:21`（"a behavior the map describes that the app no longer does is either doc drift (fix the map) or a product regression (report it, don't paper over it in docs)"） |
| 维护粒度 | **按 feature**："The unit of rigor is the feature, not every sentence: cover every feature file from source and exercise every feature live, without terminalising every bullet." | `SKILL.md:9` |
| 维护完产出什么 | **恰好三态之一**：`clean`（全覆盖，无东西要发，无分支无 PR）／`changed`（**一个 PR**，只包含已证明的文档/harness/map 修正，且**只限验证技能自己的目录**）／`blocked`（写明被什么阻断） | `SKILL.md:13-17`、`:21`、`:37` |
| 多久跑一次 / 触发 | **没有固定周期**；由人/agent 按需触发（"Suggest a cadence only if they ask"）；触发信号=发现漂移、应用变更、想把整轮验证做扎实时 | `create-verification-skill/SKILL.md:44`；`maintain-verification-skill/SKILL.md:9`（"A feature map rots the moment the app changes"） |
| 维护的边界 | 只改验证技能自己的目录（`SKILL.md`、`features/`、它拥有的 harness 脚本）；**跑维护时永不改产品代码**；无目标时"stop and point at /create-verification-skill instead of inventing a target" | `SKILL.md:19`、`:21`、`:23` |
| 交付门（生成侧） | 交付前必须**自己跑一遍**：launch → doctor → 驱动**一个**已映射功能 → 取证 → cleanup，并确认证据仍在原位；"A generated skill that was never executed is a draft, not a deliverable." | `create-verification-skill/SKILL.md:38-40`；`docs/guide/06-verify-and-ship.md:37`（"If that proof fails, don't use the output"） |

### F-1.3 四个固定 H2 的确切名字（两处原文）

- `skills/create-verification-skill/SKILL.md:36`：「**The four H2s are `Sub-features`, `How to get to it (user POV)`, `Driving it with <harness>`, and `Gotchas`.**」
- 示例索引 `skills/create-verification-skill/references/feature-map-example/README.md:33-42`：「Feature entry contract / Each feature file starts with an H1 title and one paragraph describing the user-visible behavior. **It then uses exactly four H2 sections in this order.** / 1. `Sub-features` … / 2. `How to get to it (user POV)` … / 3. `Driving it with <harness>` starts with `Preconditions:` … / 4. `Gotchas` …」
- 同文件 `:42`：「Keep implementation details out of the map. Name only user paths, stable handles, required state, commands, and observable proof.」
- benny 变体另有"每人可见功能一节"的要求与"不要冻结实现细节/当前代码路径"：`automations/benny/skills/setup-benny/SKILL.md:86`。

### F-1.4 举一反三：pstack 里所有"大型且需要被更新"的文档

判据：**会被反复修改、且修改有明确触发或明确无触发**。pstack 的更新机制全部是**技能/流程驱动**，仓内**没有 CI**（`find cursor-plugins/pstack -name ".github"` 无结果）。

| 文档 | 谁维护 | 什么触发更新 | 机械校验 |
|---|---|---|---|
| `skills/*/SKILL.md`（47 份） | 仓维护者 | ① 新技能/改技能走 authoring playbook；② `/reflect` 从会话挖经验→路由到技能编辑；③ `/automate-me` update 模式；④ 技能行为变更需过 eval playbook 盲测 | authoring playbook 校验 "frontmatter has name and description, referenced files exist, cross-skill links resolve"（`skills/poteto-mode/playbooks/authoring-a-skill.md:6`）；盲测（`docs/guide/09-make-it-yours.md:53-61`） |
| `skills/*/references/*`（9 个技能带） | 同上 | 与所属技能同改 | 无独立检查（含在技能校验里） |
| `skills/poteto-mode/playbooks/*.md`（23 个） | 仓维护者 | 无明文（新 playbook 由 authoring 流程产生；执行中发现问题回改） | 无 |
| `docs/guide/*.md`（11 页导读） | 仓维护者 | **无明文** | 无 |
| `README.md`（安装/技能表/原则/automations） | 仓维护者 | **无明文**（技能增删时应同步，但仓里没有这条规则） | 无 |
| `agents/*.md`（2 个：`poteto-agent`、`comment-sicko`） | 仓维护者 | 无明文 | 无 |
| `.cursor-plugin/plugin.json`（skills/agents 入口） | 仓维护者 | 无明文 | 无 |
| `automations/benny/**`（含 `FOR_AGENTS.md`、`templates/*.example.*`、`feature-map.example.md`、`routing.example.md`、`control-adapter.md`） | ① pack 维护者；② **用户自己的副本（pack 外）由用户维护** | pack 刷新/配置变化；用户改自己的配置 | setup-benny 的配置校验（必需值必须显式，"Fail setup if any required value stays ambiguous"`setup-benny/SKILL.md:114`）+ 新 agent 验证 + 编辑器检查清单（`:186`、`:220`）；**合并规则**：保留目标仓独有文件、绝不覆盖用户自有配置/feature map/routing map、歧义时停下问（`FOR_AGENTS.md:62-64`） |
| 项目 feature map（生成物） | `/maintain-verification-skill` | 漂移/按需 | 维护循环自身（见 F-1.2） |
| `decisions.tsv`（决策台账） | 跑该轮/该 lane 的 agent | **每决策点/每轮循环/每 tick**（append-only，错行追写覆盖） | 无（靠回核与跨模型复审） |
| `orchestrate/<slug>/`（编排 store：`preferences.md`/`overview.md`/`units.tsv`/`frontier.json`/`ledger.tsv`/`gates.md`/`status.md`…） | 每文件一个写者（coordinator/verifier/脚本各管各的） | 每次 drain / 每个 unit 状态变化 / 每个 verdict；`status.md` 由脚本重算 | 部分由 `scripts/orch/orch.ts` 保证（重算/锁） |
| 计划文件（多阶段程序） | 规划 agent | 程序启动前写、执行中按检查点更新 | `scripts/check-plan.mjs` 会被跑（`multi-phase-plan.md:10`） |

**一句话**：pstack 对"文档维护"的答案不是一条统一规则，而是**四个专用机制**：技能编辑流程（authoring/reflect/eval/automate-me）、feature map 维护循环（maintain）、程序状态库（orchestrate store 的每文件单写者）、用户自有配置（benny 的 pack 外交付 + 不覆盖）。**README 与 guide 属于"没有明文维护规则"的一类。**

### F-1.5 ①的"三仓无此法"

- matt 与 addy **没有**"专为一个**按用户可见功能拆分、可驱动、可证明**的索引"设置的维护循环；它们最接近的分别是 spec/ticket 生命周期（matt）与 eval cases/checklists（addy），对象都不是"已存在功能面如何被再次证明还活着"（详见 `EVIDENCE.md` G2.2）。
- 三仓中**只有 pstack** 把"腐烂"当独立问题处理（maintain 循环 + 三态产出 + 只改自己目录）。

---

## ② 三仓里"非一次性"的文档

**Owner 的判断**：过程记录层几乎都是一次性的；有少数文档必须长期维护。**下面的分离就是证据**：左列=需要反复更新，右列=写一次就归档/可丢。三仓都没有把两者**在同一个文件里**做分类，分离是从各仓的规则里读出来的。

判据：**"非一次性"= 会被同一主体反复更新，或必须随外部变化而更新**（不是"保留得久"——一次性的东西也可以被永久保留）。

### F-2.1 pstack

| 非一次性（会反复更新） | 维护者 | 触发 | 机械校验 |
|---|---|---|---|
| `skills/**`（SKILL.md、references、playbooks） | 仓维护者 | 技能改动/reflect/automate-me/eval | authoring 校验 + 盲测 |
| `docs/guide/**`（11 页） | 仓维护者 | 无明文 | 无 |
| `README.md`、`agents/*.md`、`plugin.json` | 仓维护者 | 无明文 | 无 |
| `automations/benny` pack 与用户副本 | pack 维护者 / 用户 | 刷新、配置变化 | setup-benny 校验 + FOR_AGENTS 合并规则 |
| 项目 feature map（`.cursor/skills/verify-<app>/features/`） | `/maintain-verification-skill` | 漂移/按需 | 维护循环 |
| 编排 store（程序期间） | 每文件单写者 | 每 drain/每事件 | 部分脚本保证 |
| 计划文件 | 规划 agent | 每检查点 | `check-plan.mjs` |
| 决策台账 | 执行者 | 每决策（append） | 无 |

| 一次性（写一次、之后只读或可丢） | 原文锚点 |
|---|---|
| resume note（`/tmp/<slug>-resume.md`） | `poteto-mode/playbooks/pause-safely.md:8` |
| swarm 截图与媒体（`/tmp/...`、`<media path>/...`） | `playbooks/multi-phase-plan.md:77`、`:123` |
| PR 正文与提交信息（每 PR 一次） | `playbooks/opening-a-pr.md:3`「Invoked at the end of every other playbook.」 |
| worker/verifier 的单次 handoff（写入后不再更新） | `orchestrate/references/handoffs.md:3-5`（"final message … saved verbatim"） |
| 单轮 brief（内嵌 prompt，不入库） | `poteto-mode/playbooks/orchestrate.md:38-49` |

### F-2.2 matt

| 非一次性 | 维护者 | 触发 | 机械校验 |
|---|---|---|---|
| 25 个技能人读页 `docs/<bucket>/<skill>.md` | 技能作者 | **技能新增/重命名/行为变化**（`AGENTS.md:17`） | **无自动**（`.agents/writing-docs.md:83` 的 done-when 是人工清单） |
| 顶层 `README.md`、5 个 bucket `README.md` | 维护者 | 技能增删改（`AGENTS.md:9/15`） | 无 |
| `ask-matt`（路由器） | 维护者 | 技能增删改（`AGENTS.md:21`，"a router that lies"） | 无 |
| `CHANGELOG.md` + `.changeset/*` | 贡献者 / 机器人 | 每个影响技能的改动带 changeset；release workflow 在 main 开版本 PR | **CI 只有 release workflow**（`.github/workflows/release.yml`）——它管版本，不查文档 |
| `.claude-plugin/plugin.json`、`marketplace.json` | 维护者 | 技能集变化 | `claude plugin validate . --strict`（人跑，`AGENTS.md:11`） |
| `.agents/{install-block,invocation,writing-docs}.md`（库级规范） | 维护者 | 对应约定变化 | 无 |
| `CONTEXT.md`（仓自身词汇） | 维护者 | 语言变化 | 无 |
| `.agents/adr/NNNN-slug.md`（本仓 2 份） | 维护者 | 难回退决定 | 无（同源规则见 addy `documentation-and-adrs/SKILL.md:99`「Don't delete old ADRs」——改主意写新 ADR 取代旧的） |
| `.out-of-scope/<concept>.md` | 维护者/triage | 同类增强请求再次被拒时**追加 prior requests**；改主意则删文件（`OUT-OF-SCOPE.md:86`、`:99-103`） | 无 |
| 项目侧：`CONTEXT.md`、`docs/adr/`、`.scratch/<feature>/{spec.md,issues/NN-*.md,map.md}` | 项目使用者 | 领域语言变化 / 工作推进（`Status:` 行、map 的 Decisions-so-far 追加） | 无 |

| 一次性 | 原文锚点 |
|---|---|
| handoff 文档（OS 临时目录） | `skills/productivity/handoff/SKILL.md:8` |
| 架构评审 HTML（OS 临时目录） | `skills/engineering/improve-codebase-architecture/SKILL.md:39` |
| wizard 脚本（默认 scratch，用完删） | `skills/engineering/wizard/SKILL.md:12` |
| 每条 changeset（发布时被消费） | `.changeset/*.md` + `release.yml` |
| triage 单条评论 / agent brief（贴到 tracker 后即定稿） | `skills/engineering/triage/SKILL.md:79`、`README` |

### F-2.3 addy

| 非一次性 | 维护者 | 触发 | 机械校验（CI：`.github/workflows/test-plugin-install.yml`） |
|---|---|---|---|
| `skills/*/SKILL.md`（25） | 技能作者 | 技能改动（CONTRIBUTING 流程） | `validate-skills.js`（`:23`）+ `skill-lint-test.js` + Tier2 evals（`:38`） |
| `evals/cases/<skill>.json`（25） | 技能作者 | 新技能必带；行为变化时更新 | CI 运行 eval runner + 单测（`:38`、`:41`）；CONTRIBUTING 要求至少 3 正例/2 负例/1 行为例 |
| `commands/` ×3 宿主面（各 9） | 维护者 | 命令增删改 | `validate-commands.js`（`:64`）——集合与 description 一致 |
| `references/*.md`（6 份共享清单） | 维护者 | 标准变化 | `validate-reference-links.js`（`:41`）——链接可解析 |
| spec/plan/todo 产物路径（跨文件约定） | 维护者 | 改约定（需同时改白名单与所有管线文件） | `validate-artifact-paths.js`（`:70`）+ 单测 |
| `docs/skill-anatomy.md`（技能结构单一真源） | 维护者 | 结构规则变化 | 被 `validate-skills.js` 使用（以它为规则源）；自身无校验 |
| `docs/*.md`（16 页，含 onboarding/各宿主接入） | 维护者 | 新宿主/流程变化 | 无直接校验（`developer-onboarding.md` 有 pre-PR 清单） |
| `README.md`（25 技能分阶段表） | 维护者 | 技能增删改 | 无直接校验 |
| `evals/skill-impact.md`（被拒变更账本，append-only） | 贡献者 | 提案被 eval 拒时 | 无自动（CONTRIBUTING 要求单独提交到默认分支，`CONTRIBUTING.md:73`） |
| `hooks/*.md` + 脚本 | 维护者 | 钩子变化 | `sdd-cache-test.sh`、`simplify-ignore-test.sh`、`session-start-test.sh`（`:50`、`:128`、`:131`） |
| `.claude/rules/skills-contributing.md`（路径作用域规则） | 维护者 | 技能贡献流程变化 | 无 |
| 插件清单 | 维护者 | 技能/版本变化 | `validate-versions.js`（`:29`）+ `claude plugin validate .`（`:144`）+ 安装测试（`:166`） |
| 项目侧：`SPEC.md`、`tasks/plan.md`、`tasks/todo.md` | 项目使用者 | 范围/决定变化、任务边界 | `validate-artifact-paths.js` **只约束仓内文档里写的路径一致性**，不检查项目文件是否存在 |
| 项目侧：`CONSTRAINTS.md` | 项目使用者 | 门禁变化；检测被悄悄放宽 | 无（技能自带检测表） |
| 项目侧：`docs/adr/`、`CHANGELOG.md`、规则文件 | 项目使用者 | 决定/发布/约定变化 | 无 |

| 一次性（gitignore 明列或规则明说） | 原文锚点 |
|---|---|
| `evals/results/`、`evals/plugin/results/<ts>/` | `evals/README.md:38/49`；`.gitignore`（`evals/results/`、`evals/plugin/results/`） |
| `.claude/sdd-cache/`、`.claude/simplify-ignore-cache/` | `.gitignore`；SDD-CACHE.md / SIMPLIFY-IGNORE.md |
| `SPEC.md`/`tasks/*`（开发期活文档，merge 前可删或 ignore） | `docs/getting-started.md:173-177` |
| 单次浏览器验证截图、eval trace | `browser-testing-with-devtools`（无落点规定，见 E-G5.1） |

### F-2.4 结论（供设计输入）

1. **"非一次性"集合在三仓都不大**：pstack ≈ 4 类机制管着 8 类文档；matt ≈ 9 类（其中 6 类无任何机械校验）；addy ≈ 13 类（其中 6 类进 CI，其余靠流程）。
2. **分界线在"是否随外部变化重写"**：技能正文/人读页/检查表/路由表/清单会随技能集变化重写；spec/ticket/ADR/账本只**追加**；handoff/评审报告/缓存/产物运行结果**写完即弃或只读**。
3. **机械校验只出现在"会随外部变化重写、且有多处副本"的那一类**（addy 的 commands 三镜像、artifact 路径、reference 链接、skills 结构、版本；matt 只有 release）。→ 这正是"长期维护 ≠ 机械校验"的证据：**长期维护的多数靠触发式协议，只有多副本/跨文件引用才上机器**。
4. **修正上一批的一句话**：我此前说 addy 是"CI 四类校验"。按 workflow 全文，实际是 **6 个校验器 + 5 组单测 + eval runner + hook 回归 + 插件 validate + 安装测试**（`:23/29/38/41/50/64/70/128/131/144/166`）。这一批以 workflow 为准。

---

## ③ `SET-A.md` 的 24 项按"类"重排

**Owner 问**："24 项是 24 类吗？"。**答**：不是。24 是**实例数**（逐份收据/记录），按"用途 + 载体形态"归并是 **9 类**；其中 **5 项根本不是独立文档**（伴随件或字段），1 项是**本库专有**，1 项（candidate）**以身份 token 表达、没有文件形态**。若把"项目长期文档更新"并入"授权与裁定"类，则得 **8 类**（与 Owner 直觉一致）；本表按 9 类列全，合并规则写在末尾。

| 类 | 实例（`SET-A.md` 编号） | 是否独立文档 | 产出方 | 产出环节 |
|---|---|---|---|---|
| **K1 授权与目标** | #1 `owner-brief`；#18 授权记录本体 | #1 独立（外部）；#18 **形态未规定**（内容被 `pipeline.md:123` 要求，task-card 只带快照） | Owner（外部）/ Driver 记录 | 步 0（入站）；#18 无环节 |
| **K2 批次契约** | #2 `task-card`；#6 `design-proposal`；#7 `slice-plan` | 三份都是**独立收据**（提案/计划属"会随本轮冻结而定稿"的一次性契约） | Driver / Architect / Planner（#7 Driver 可代产） | 步 0 / 2 / 3 |
| **K3 诊断报告** | #5 `investigation-report` | 独立收据 | Investigator（Driver 可代产） | 步 1 |
| **K4 对象身份** | #8 `candidate`；#16 `ws:v1` 清单；#17 范围声明 | #8 **不是文件**（`object := base=…;tree=…`，`identity.md:20`）；#16/#17 是 **#8/`object` 的伴随件**（Oracle 已判；`identity.md:60` 要求一起交） | Implementer；#16 由任何计算身份的角色产；#17 由 Driver 发写窗时分列 | 步 4（#8）；#16/#17 **无环节** |
| **K5 放行判断与证明** | #9 `review-verdict`；#10 `verification-evidence`；#11 `integrated-baseline`；#4 `oracle-ruling`；#13 `equivalence-proof`；#19 证据材料 | 前四份**独立收据**；#13 是"审查被等价证明替代"的证明收据；#19 是**伴随资产**（指针指向的夹具/读数/截图） | Reviewer / Verifier / Integrator / Oracle / Driver（#13）/ 各执行者（#19） | 步 5 / 6 / 7；A1；步 5 跳过路径；#19 隐含在 1/5/6 内 |
| **K6 争议提问** | #3 `pending-question` | 独立收据 | Architect / Reviewer / Driver | A0 |
| **K7 记录与对账** | #20 决策台账（+ `driver.md:292` 的"该批决策记录"）；#14 `ledger-input`；#15 `ledger-report`；#24 `SOURCES.md` 生成区 | #20/#14/#15 **独立台账或报告**；#24 **独立但库专有**（下游无对象，E1-7） | 执行者 / Driver / Ledger-custodian / `render-ledger.py` | #20 **无环节**；#14/#15/#24 = A3 |
| **K8 收口与未决** | #12 `roundup`；#21 现场包；#23 装配说明 | #12 **独立**；#21 **不是文档**（"打包现场、已排除解释与证据指针"= 指针束，且无产方 `pipeline.md:108`）；#23 **是字段**（写在 task-card，`closure.md:42`） | Driver；#21 无产出方 | 步 8；A2；（#21 无环节） |
| **K9 项目长期文档更新** | #22 词汇表 / ADR 更新 | **独立项目文档**（`architect.md:210` 指定 Architect 为默认写者） | Architect（无 Architect 时 Driver 指派唯一写者） | **无环节** |

**独立性总判定（24 项）**：
- **不是独立文档（5 项）**：#16 清单（`object` 伴随件）、#17 范围声明（task-card 伴随件）、#19 证据材料（指针所指资产的集合名）、#21 现场包（指针束）、#23 装配说明（字段）。
- **独立但形态未定（1 项）**：#18 授权记录本体。
- **独立但非文件**（1 项）：#8 candidate（以对象身份表达）。
- **独立文档（17 项）**：#1、#2、#3、#4、#5、#6、#7、#9、#10、#11、#12、#13、#14、#15、#20、#22、#24。
- **合并规则（给 Owner 的 8 类版本）**：把 K9 并入 K1（项目词汇/ADR 更新是"已授权裁定"的落点）⇒ 8 类；把 K8 的 #21/#23 视为"无独立物的字段/指针"、K4 的 #16/#17 同理 ⇒ **真正的文档类 ≈ 6 类（K1–K3、K5–K7）+ 2 个字段类（K4、K8 的非独立部分）**。

---

## ④ skill 数量 / 结构 / 角色-skill 绑定

### F-4.1 数量与结构（命令可复现）

| 仓 | skill 数（`find <repo>/skills -name SKILL.md \| wc -l`） | 分布 | SKILL.md 总行 | 中位 | 最大 | 带 `references/` | 带 `scripts/` | 其他附属文件 |
|---|---|---|---|---|---|---|---|---|
| pstack | **47** | 平铺在 `skills/<name>/`（23 个是 `principle-*`） | 2157 | 31 | 158（`why`） | 9 | 2 | 0（无技能内附属 md） |
| matt | **38** | `engineering` 18 / `productivity` 7 / `in-progress` 9 / `misc` 4 | 2633 | 74.5 | 168（`in-progress/pr`） | **0** | 2 | 13 个技能带同名支持文档（如 `ADR-FORMAT.md`、`DESIGN-IT-TWICE.md`）；**38 个技能各带 `agents/openai.yaml`** |
| addy | **25** | 平铺在 `skills/<name>/` | 7494 | 300 | 496（`performance-optimization`） | 2 | 1 | 1（`idea-refine` 带 3 份附属 md） |
| **本仓** | **0**（无 `skills/` 目录） | 旧载体归档在 `docs/archive/skills/`（8 个） | roles 10 份合计 **2365** 行（中位 227）+ `pipeline.md` 154 + `closure.md` 47 + `identity.md` 95 | — | — | — | — | 6 个 `scripts/` |

**结构结论**：越"角色化/流程化"的仓，单个 skill 越长（addy 中位 300 行）；越"词汇化/组合化"的仓，单个 skill 越短（pstack 中位 31 行，靠 47 个短技能 + playbooks 组合）。我们的角色文件（中位 ≈226 行）在"长度"上接近 addy 的技能，而不是 pstack 的短技能。**我们没有 skill 目录**——注入单元是角色文件。

### F-4.2 角色 ↔ skill 绑定的三种模型（含例子）

| 仓 | 绑定模型 | 证据 |
|---|---|---|
| pstack | **没有 persona-skill 绑定**；绑定的是 **"角色 → 模型"**：`setup-pstack` 写一份 `~/.cursor/rules/pstack-models.mdc`，**一行一个 role**；每个技能在自己的 spawn 处声明用哪条 role line（`how explorer`、`swarm workers`、`arena runners`、`interrogate reviewers`、`reflect judgment…` 等）。另有 **2 个 agent 定义**（`agents/poteto-agent.md`、`agents/comment-sicko.md`）作为被 spawn 的 subagent 场景。 | `skills/setup-pstack/SKILL.md:8`（"an always-applied rule that sets pstack's model per role"）、`:18`（退休 role 要删）、`:39`（one line per role，整文件重写以保持幂等）；`skills/how/SKILL.md:11`、`skills/swarm/SKILL.md:25`、`skills/arena/SKILL.md:28/41`、`skills/interrogate/SKILL.md:36`、`skills/reflect/SKILL.md:33`、`skills/architect/SKILL.md:33`、`skills/poteto-mode/SKILL.md:93`；`agents/` 下 2 个文件 |
| matt | **没有 persona**；绑定 = **调用模式**（user-invoked / model-invoked）+ 一个路由器。每个 `SKILL.md` 由 frontmatter `disable-model-invocation` 与 `agents/openai.yaml` 的 `policy` 决定"只能人调还是模型可自动触发"；`ask-matt` 是"路由到所有用户可达技能"的入口。 | `.agents/invocation.md:5-6`（两种调用模式的定义）、`:12`（README/桶页按两种模式分组）；`skills/engineering/ask-matt/SKILL.md:3`（"A router over the skills in this repo"） |
| addy | **三层显式绑定**：Skills = how / Personas = who / Slash commands = when；**用户或斜杠命令是编排者，persona 不调 persona，persona 可以调 skill**；唯一的多 persona 模式是 `/ship` 的三 persona 并行 + 汇总。 | `AGENTS.md:70-80`（三层定义、组合规则、`/ship` 是唯一多 persona 模式）；`commands/ship.toml:6-16`（并行派发 `code-reviewer` / `security-auditor` / `test-engineer`）；`references/orchestration-patterns.md:130-140`（subagents 只回报 vs teams 互相挑战）、`:156`（内置 `Explore`/`Plan` 只读） |
| **本仓** | **角色 = 注入单元 = 一层**（10 份角色文件）；没有 skill 层，也没有"角色→模型"绑定（第 4 层工具安排由 Driver 附加）。 | `README.md:29-37`（注入三步）、`:52`（roles/ 10 个角色文件）；`AGENTS.md:18`（四层注入契约） |

### F-4.3 给"判断题"的弹药（事实对比，不含结论）

- **单元数量**：pstack 47 个 skill（含 23 个 principle）；matt 38；addy 25；**我们 10 个角色 + 1 份流程 + 1 份闭环矩阵 + 1 份身份规范**。
- **单元体量**：pstack 中位 31 行、总计 2157；matt 中位 74.5、总计 2633；addy 中位 300、总计 7494；我们角色中位 ≈227、总计（roles+pipeline+closure+identity）2661。
- **结构习惯**：pstack 用 `references/`（9/47）与 `playbooks/`（1 组 23 份）；matt 用**技能内同名支持文档**（13/38）而**不用 references/**；addy 用根级共享 `references/`（6 份，技能链接过去，有 CI 查链接）。**三仓没有一种共同的目录约定**。
- **维护强度**：addy 对"会随外部变化重写的文档"上了 6 个校验器 + 5 组单测 + hook 回归；matt 只有 release workflow；pstack 没有 CI。

---

## 本批"三仓无此法"汇总

1. **feature map 型的"按用户可见功能建立、可驱动、可证明、可维护"的索引**：只有 pstack 有，且有专用维护循环与三态产出；**matt/addy 无此法**（最接近的是 eval cases 与 checklist，对象不同）。
2. **"非一次性文档 vs 一次性记录"的显式分类**：三仓都没有把这条分界线写在同一个地方；本文件 §② 是从各自规则里读出来的。
3. **"角色 → skill"的绑定表**：matt 无角色概念；pstack 绑的是"角色→模型"；addy 绑的是"命令→persona/skill"；**三仓都没有"一个角色持有一组能力/技能"的显式清单**（这正是我们角色文件干的活）。
4. **README/guide 的维护规则**：pstack **无明文**；matt 有明文（技能变更三处同步）；addy 靠 CONTRIBUTING 流程与 CI 的间接约束。**"文档索引自身的维护"只有 matt 写成了硬规则。**
