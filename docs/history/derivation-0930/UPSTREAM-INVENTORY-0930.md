# UPSTREAM-INVENTORY-0930 · 完整上游机制来源清点

- **角色**：`scout`（`tpw-0930-scout-b`）· 找事实，不给结论，不裁决处置
- **driver**：`tpw-0930-driver`
- **任务书**：`docs/history/handoff/0930-scout-b-TASK.md`（115 行，`wc -l` 实测 115）
- **落点**：本文件，唯一可写
- **方法**：全部只读实测（`os.walk` / `re` 解析 / 逐文件读正文）。摘录一律逐字，解释写在引用之外。

## 0. 三态汇总

| 项 | 状态 | 依据 |
|---|---|---|
| driver 基线数字（1344 / 159 / 101 / 58）独立复核 | **PASS** | §1 四个数字逐个复现，分布表逐行吻合 |
| 根因推断（`REPOS` 只 3 条 + `SKIP_DIRS` 排 7 项）复核 | **PASS** | §2 逐字锚点，driver 说的 `:23-27` 实为 `:22-26`，`:28-29` 实为 `:27-28`（差一行，见 §2.3） |
| Q-A 非 `SKILL.md` 载体完整枚举 | **PASS** | §3，1239 文件全集（不含 `.git`），1080 个非 SKILL.md，19 类 |
| Q-B 58 个不在锁里的 `SKILL.md` 逐条描述 | **PASS** | §4，58 条全部读 frontmatter 正文 |
| Q-C `in-progress` 9 个逐个读正文 | **PASS** | §5，9/9 读完，含行号锚点与逐字摘录 |
| Q-D `rejected` 但找不到正文的条目 | **PASS（空集）** | §6，20 条 rejected 全部能定位到磁盘实体；UPRESCAN N12 的锚点复核见 §6.2 |
| 本库 `check-closure.py` / `check-consistency.py` 运行态 | **UNVERIFIED** | 本轮**没有运行**任何检查器。缺的是执行授权与运行时验证；不是缺陷 |
| 58 个里「本库用得上」的程度判定 | **UNVERIFIED（故意留空）** | 见 §4.3。scout 不裁决吸收；「用得上」需要与 `registry.yaml` 逐条比对，是 `adversary` 的判据 |

## 1. 基线独立复核（driver 实测 → scout 复现）

| 数字 | driver | scout 实测 | 状态 |
|---|---|---|---|
| `upstreams/` 文件总数 | 1344 | **1344**（含 `.git` 内部）／**1239**（不含任何 `.git` 目录） | PASS（口径差异已记） |
| `SKILL.md` 个数 | 159 | **159** | PASS |
| `upstreams.lock.yaml` 枚举 | 101 | **101**（`skills:` 段 `path:` 条目；另有 `repos:` 段 3 条 `path:`，driver 的 104 是 101+3 混计） | PASS |
| 不在锁里的 `SKILL.md` | 58 | **58** | PASS |

`159 - 101 = 58`，口径闭合。

**锁文件 101 条的分布**（scout 解析 `upstreams.lock.yaml`）：

| 仓前缀 | 锁内条数 | `upstreams.lock.yaml` `repos:` 段行锚点 |
|---|---|---|
| `pstack:` | 39 | `upstreams.lock.yaml:3` `path: upstreams/cursor-plugins/pstack` |
| `matt:` | 29 | `upstreams.lock.yaml:4` `path: upstreams/mattpocock-skills` |
| `addy:` | 33 | `upstreams.lock.yaml:5` `path: upstreams/addyosmani-agent-skills` |

**58 个的分布**（scout 实测，与 driver 表格逐行吻合）：

| 位置 | 数量 | 排除原因 |
|---|---|---|
| `cursor-plugins/cursor-team-kit/skills/*` | 18 | `REPOS` 无此路径 |
| `mattpocock-skills/skills/in-progress/*` | 9 | `SKIP_DIRS` 含 `in-progress` |
| `cursor-plugins/third_party/*` | 6 | `SKIP_DIRS` 含 `third_party` |
| `cursor-plugins/grok-voice/*` | 4 | `REPOS` 无此路径 |
| `cursor-plugins/{ralph-loop,thermos}` | 3 + 3 | 同上 |
| `cursor-plugins/pstack/automations/benny/skills/*` | 3 | `SKIP_DIRS` 含 `automations` |
| `cursor-plugins/{create-plugin,teaching}` | 2 + 2 | 同 cursor-team-kit |
| `cursor-plugins/{advisor,agent-compatibility,cli-for-agent,continual-learning,cursor-sdk,docs-canvas,orchestrate,pr-review-canvas}` | 1 × 8 | 同上 |

合计 18+9+6+4+3+3+3+2+2+8 = **58**。PASS。

## 2. 根因复核

### 2.1 枚举源逐字

`scripts/_render-lock.py:22-26`：

```
REPOS = {
    "pstack": "cursor-plugins/pstack",
    "matt": "mattpocock-skills",
    "addy": "addyosmani-agent-skills",
}
```

`scripts/_render-lock.py:27-28`：

```
SKIP_DIRS = {"deprecated", "in-progress", "templates", "assets", "references",
             ".git", "automations", "third_party", "node_modules"}
```

`scripts/_render-lock.py:52-53`：

```
        for root, dirs, files in __import__("os").walk(base / "skills"):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
```

**这一行是全部结构性不可见的唯一机制**：只 walk `base/"skills"`，且 `dirs[:]` 在原地裁剪 `SKIP_DIRS`。因此
(a) `base/"skills"` 之外的任何文件永不入枚举；(b) `SKIP_DIRS` 里任何一个目录名，在任何深度、任何仓下都被裁掉。

### 2.2 driver 补的 `references` 一条 —— 复核结果：成立，且比 driver 说的更宽

`references` 在 `SKIP_DIRS` 第 27 行第 6 位。因为 `dirs[:]` 的裁剪对**每一层 walk 都生效**，所以它命中的不只是仓根的 `references/`：

| 实测 | 数量 |
|---|---|
| `upstreams/**/references/` 下文件总数（含 `third_party`） | **57** |
| 其中 `SKILL.md` | **0** |
| 排除 `third_party` 后 | **56** |
| 其中 `SKILL.md` | **0** |

`references/` 下 0 个 `SKILL.md` 意味着：这一条**没有额外藏 skill**，它藏的是 **56 份非 skill 载体的参考正文**（rubric、checklist、prompt 模板等）。driver 的判断方向正确，scout 补一个限定：这 57 个文件不进锁，但它们是 Q-A 的主要内容，不是 skill。

**逐字摘录**（`upstreams/cursor-plugins/pstack/skills/interrogate/references/rubric.md` 存在于磁盘，见 §3 清单）。

### 2.3 一处锚点修正（事实，不是不判）

driver 任务书与 ACK 里写 `scripts/_render-lock.py:23-27` = `REPOS`、`:28-29` = `SKIP_DIRS`。
scout 实测（`cat -n`）：`REPOS` 是 **22-26**，`SKIP_DIRS` 是 **27-28**。整体上移一行。
结论不变（`REPOS` 3 条、`SKIP_DIRS` 9 个目录名），只是行号。**记为事实差异，不记为缺陷。**

### 2.4 `cursor-plugins/` 插件目录数

`upstreams/cursor-plugins/` 下实有 **16 个插件目录** + `README.md` + `schemas/` + `scripts/` + `third_party/`：
`advisor`、`agent-compatibility`、`cli-for-agent`、`continual-learning`、`create-plugin`、`cursor-sdk`、
`cursor-team-kit`、`docs-canvas`、`grok-voice`、`orchestrate`、`pr-review-canvas`、`pstack`、`ralph-loop`、
`teaching`、`thermos`、`third_party`。
**只有 `pstack` 在 `REPOS` 里。** 其余 15 个从未被 walk —— 与 §1 的分布表完全闭合。PASS。

## 3. Q-A · `SKILL.md` 之外的载体完整枚举

**口径**：`upstreams/` 下 1239 个文件（排除任何 `.git` 目录内部的记账文件），其中 159 个 `SKILL.md`，
**1080 个非 `SKILL.md`**，分 **19 类**：

| # | 载体类 | 数量 |
|---|---|---|
| 1 | `third_party/`（外仓整包） | 476 |
| 2 | `scripts/` | 104 |
| 3 | `evals/` | 84 |
| 4 | 根级 `.md`（README / CHANGELOG / AGENTS.md / CLAUDE.md / CONTEXT.md / CONTRIBUTING.md 等） | 71 |
| 5 | `docs/` | 58 |
| 6 | `references/` | 56 |
| 7 | `agents/` | 55 |
| 8 | 其它 `json` | 29 |
| 9 | `commands/` | 27 |
| 10 | `playbooks/` | 23 |
| 11 | `hooks/` | 20 |
| 12 | 无扩展名（LICENSE 等） | 17 |
| 13 | 图片（png / jpg / svg） | 14 |
| 14 | `.changeset/` | 13 |
| 15 | `prompts/` | 10 |
| 16 | `.gitignore` | 5 |
| 17 | `automations/`（非 `SKILL.md` 部分） | 5 |
| 18 | `yaml` / `yml`（散在根与插件层） | 4 |
| 19 | 零散代码与配置（`mdc` 3 / `cjs` 1 / `sh` 1 / `js` 1 / `css` 1 / `html` 1） | 8 |

合计 1080。

**其中 `.md` 正文载体 447 个，排除 `third_party` 后 288 个**，按类：

| 类 | `.md` 数 |
|---|---|
| 根级 `.md` | 71 |
| `references/` | 55 |
| `docs/` | 52 |
| `evals/` | 32 |
| `playbooks/` | 23 |
| `agents/` | 17 |
| `.changeset/` | 12 |
| `prompts/` | 10 |
| `commands/` | 9 |
| `automations/` | 4 |
| `hooks/` | 2 |
| `scripts/` | 1 |
| **合计** | **288** |

### 3.1 分仓明细（排除 `third_party`）

| 仓/目录 | 非 SKILL.md 文件数 | SKILL.md 数 |
|---|---|---|
| `cursor-plugins/third_party` | 476 | 6 |
| `cursor-plugins/orchestrate` | 83 | 1 |
| `cursor-plugins/pstack` | 108 | 44 |
| `addyosmani-agent-skills/evals` | 84 | 0 |
| `addyosmani-agent-skills/docs` | 16 | 0 |
| `addyosmani-agent-skills/scripts` | 14 | 0 |
| `addyosmani-agent-skills/hooks` | 9 | 0 |
| `addyosmani-agent-skills/commands` | 9 | 0 |
| `addyosmani-agent-skills/references` | 7 | 0 |
| `addyosmani-agent-skills/skills` | 6 | 25 |
| `mattpocock-skills/skills` | 70 | 55 |
| `mattpocock-skills/docs` | 25 | 0 |
| `mattpocock-skills/.changeset` | 13 | 0 |
| `mattpocock-skills/.out-of-scope` | 3 | 0 |
| `mattpocock-skills/.agents` | 5 | 0 |
| `cursor-plugins/{advisor,cursor-team-kit,cursor-sdk,agent-compatibility,create-plugin,continual-learning,thermos,ralph-loop,grok-voice,docs-canvas,pr-review-canvas,teaching,cli-for-agent}` | 88 | 27 |
| 各仓根级散文件（`AGENTS.md` / `CLAUDE.md` / `README.md` / `CONTEXT.md` / `CHANGELOG.md` / `CONTRIBUTING.md` / `plugin.json` / `package.json` / `LICENSE` / `.github` / `.claude` / `.gemini` / `.agents` / `.claude-plugin` / `.codex-plugin` / `.gitattributes` / `.gitignore`） | 约 100 | 0 |

**结论（事实）**：锁文件**只登记 `SKILL.md`**（`upstreams.lock.yaml` 全部 104 条 `path:` 里，101 条 skills + 3 条 repo 根）。
其余 1080 个文件在结构上**没有任何登记位置** —— 不在锁、不在 `registry.yaml`、不在 `check-closure.py` 的 C7 断言范围。
本轮可见性只能靠这份清单。

### 3.2 「沉默桶」实测（UPRESCAN 线索，scout 独立核）

| 线索 | 实测 | 状态 |
|---|---|---|
| `in-progress/` 9 个 skill | **9**，见 §5 | PASS |
| `.changeset/` | **13 个文件**（UPRESCAN 说 2 份；实测 13，含 `README.md` 与 11 份具名 changeset，具名的有 `retro-deterministic-checks.md`、`add-implement-spec-skill.md`、`add-pr-skill.md`、`wait-what-context-map.md`、`remove-em-dashes-repo-wide.md` 等） | **PASS（数字修正）** |
| `evals/` 三个沉默桶 | `addyosmani-agent-skills/evals/` 共 **84 个文件**，下辖 `fixtures/`（按 skill 名分 20 个子目录）、`plugin/`（4 个场景，每个含 `prompt.md` + `graders/*.md`）、`README.md`、`skill-impact.md` | PASS |
| `references` 使任何 skill 自带 references 不被枚举 | **成立**，见 §2.2，56 个非 third_party 文件、0 个 SKILL.md | PASS |

`evals/plugin/` 的 4 个场景值得单列（**已发现，未读正文**）：
`code-review-fires`、`code-review-stays-quiet`、`code-review-stays-quiet-on-commit-message`，各带
`graders/not-fired.md` / `severity-labels.md` / `off-by-one.md` / `tdd-fired.md` / `skill-fired.md`。
**读法：这是一套「skill 该不该在此时开火」的负例评测集**，与本库「何时不上场」类判据方向重合。
**只记录，不裁决。**

## 4. Q-B · 58 个不在锁里的 `SKILL.md`

**全部 58 条已读 frontmatter 正文**（`已读` 档）。下面逐条给「讲什么」。
格式：`路径 | 行数 | 它讲什么`。**只描述，不裁决吸收。**

### 4.1 `mattpocock-skills/skills/in-progress/*`（9）— 见 §5 详节

| 路径 | 行 | 讲什么 |
|---|---|---|
| `in-progress/claude-handoff` | 19 | 把当前会话交接给一个后台 agent，**不落盘**，直接 `claude --bg --name` 起进程 |
| `in-progress/implement-spec` | 36 | 按 spec+tickets 开工单分支 PR，tickets 是**任务图**不是步骤清单，靠 frontier 抢单 |
| `in-progress/loop-me` | 33 | 用 grilling 逼出「loop / workflow」规格，落 `workflows/*.md` |
| `in-progress/pr` | 169 | PR 正文模板：Summary / Evidence（Before-After）/ Merge Danger（Door + Blast Radius） |
| `in-progress/retro` | 45 | 编码会话复盘，产出**环境改进候选**（导航 / 自动检查 / 编码标准 / 全局 AGENTS.md / 工具经济 / no-ops / 信息可达） |
| `in-progress/setup-ts-deep-modules` | 103 | 装 dependency-cruiser，把每个 package 变成 deep module，四条 error 级规则 |
| `in-progress/writing-beats` | 68 | 文章成文：逐 beat 推进，每个 beat 都要**grounding（落地）**它依赖的每个概念 |
| `in-progress/writing-fragments` | 80 | 素材期：只挖 fragment，不定结构，明确「imposing phases, outlines, or article structure is out of scope」 |
| `in-progress/writing-shape` | 80 | 成长期：定结构后逐段生长，段落格式本身要可辩护 |

### 4.2 `cursor-plugins/*` 不在 `REPOS` 的 15 个插件（43）

| 路径 | 行 | 讲什么 |
|---|---|---|
| `cursor-team-kit/skills/control-cli` | 110 | 建/改一个本地 harness 驱动、检视、profile 交互式 CLI 或 TUI（启动回归、内存泄漏、挂起、prompt 流） |
| `cursor-team-kit/skills/control-ui` | 110 | 建/改一个本地 browser/CDP harness 驱动检视 Web/IDE/Electron UI（截图、无障碍快照、perf profile、视觉 diff） |
| `cursor-team-kit/skills/thermo-nuclear-code-quality-review` | 193 | 极严可维护性审查：抽象质量、巨型文件、意大利面式条件膨胀 |
| `cursor-team-kit/skills/pr-review-canvas` | 177 | 把 PR 变成交互式 HTML 走读页：拉 PR 数据、核心改动 vs 机械改动分类、标注、moved-code 检测 |
| `cursor-team-kit/skills/verify-this` | 75 | 用新证据验一条断言：可证伪地重述、采基线与处置、比对产物，返回 VERIFIED / NOT VERIFIED / INCONCLUSIVE |
| `cursor-team-kit/skills/make-pr-easy-to-review` | 60 | 清理噪声历史、改进 PR 描述、加评审指引，**不改代码行为** |
| `cursor-team-kit/skills/review-and-ship` | 42 | 审当前分支的 bug / 意图契合 / 测试覆盖，跑或写测试，提交，开 PR |
| `cursor-team-kit/skills/loop-on-ci` | 51 | 盯 PR checks 并修到绿，以 `gh pr checks` 为真源 |
| `cursor-team-kit/skills/workflow-from-chats` | 51 | 从近期 Cursor 聊天里抽持久工作偏好，转成 skills / rules / workflow 文档 |
| `cursor-team-kit/skills/weekly-review` | 33 | 按 bugfix / tech debt / 净新增给一周提交做综述 |
| `cursor-team-kit/skills/what-did-i-get-done` | 32 | 按用户指定时间段汇总自己写的提交 |
| `cursor-team-kit/skills/run-smoke-tests` | 43 | 跑 Playwright smoke、修失败、验修复 |
| `cursor-team-kit/skills/fix-merge-conflicts` | 33 | 非交互解冲突，验 build 与测试，收尾 |
| `cursor-team-kit/skills/fix-ci` | 30 | 找失败的 PR check，看日志或外链，做聚焦修复 |
| `cursor-team-kit/skills/get-pr-comments` | 23 | 抓当前 PR 的评审意见并摘要 |
| `cursor-team-kit/skills/check-compiler-errors` | 24 | 跑编译与类型检查，报失败 |
| `cursor-team-kit/skills/deslop` | 23 | 移除 AI 生成代码 slop |
| `cursor-team-kit/skills/new-branch-and-pr` | 30 | 开新分支、做完、开 PR |
| `thermos/skills/thermo-nuclear-code-quality-review` | 193 | 与 cursor-team-kit 同名同体（193 行，两处重复） |
| `thermos/skills/thermo-nuclear-review` | 52 | 分支改动的安全+正确性全面审计 |
| `thermos/skills/thermos` | 22 | 两个 thermo review 子代理**并行**起，再综合 |
| `advisor/skills/advisor` | 124 | Advisor 模式：在关键检查点（重大决策前、卡住时、宣布完成前）咨询更强/不同模型；`Never enable it on your own.` |
| `agent-compatibility/skills/check-agent-compatibility` | 47 | 跑整套仓兼容 pass：scanner 打分、启动路径、验证环、文档可靠性 |
| `cli-for-agent/skills/cli-for-agents` | 88 | 为 agent 装/改 CLI（frontmatter `description: >-` 多行） |
| `continual-learning/skills/continual-learning` | 25 | 把 transcript 挖掘与 AGENTS.md 更新委派给 `agents-memory-updater` |
| `create-plugin/skills/create-plugin-scaffold` | 71 | 生成合法 Cursor 插件脚手架：manifest、组件目录、marketplace 接线 |
| `create-plugin/skills/review-plugin-submission` | 50 | 审插件能否上 marketplace：manifest、组件元数据、发现路径 |
| `cursor-sdk/skills/cursor-sdk` | 240 | 在 Cursor TypeScript SDK 上建 app/脚本/CI/自动化；**同目录另带 7 份 `references/`（advanced / auth / error-handling / mcp / patterns / runtime-choice / streaming）** |
| `docs-canvas/skills/docs-canvas` | 55 | 文档 canvas（frontmatter `description: >-`） |
| `grok-voice/skills/add-voice` | 124 | 加语音 |
| `grok-voice/skills/add-dictation` | 172 | 加听写 |
| `grok-voice/skills/add-read-aloud` | 184 | 加朗读 |
| `grok-voice/skills/debug-voice` | 199 | 调语音 |
| `orchestrate/skills/orchestrate` | 48 | 显式 `/orchestrate <goal>` 才触发：拆大任务、经 Cursor SDK 拉一树并行云 agent、收结构化 handoff；`do not invoke autonomously.` |
| `pr-review-canvas/skills/pr-review-canvas` | 67 | PR 评审 canvas（frontmatter `description: >-`） |
| `ralph-loop/skills/ralph-loop` | 55 | 起一个自指迭代开发 loop |
| `ralph-loop/skills/cancel-ralph` | 29 | 取消跑着的 ralph loop |
| `ralph-loop/skills/ralph-loop-help` | 82 | 解释 ralph loop 怎么用 |
| `teaching/skills/create-learning-path` | 35 | 建带里程碑与练习检查点的学习路线 |
| `teaching/skills/run-learning-retrospective` | 29 | 评学习进度、找阻塞、调计划 |

### 4.3 `cursor-plugins/pstack/automations/benny/skills/*`（3）+ `third_party`（6）

| 路径 | 行 | 讲什么 |
|---|---|---|
| `pstack/automations/benny/skills/triage-issue-reports` | 241 | 分类 Slack 问题报告：单 verdict、证据审阅、cause-aware 路由、tracker 去重、**fail-closed 建单**；`Use only from the configured Benny triage automation.` |
| `pstack/automations/benny/skills/setup-benny` | 267 | 配置 Benny 及其 triage/repro 自动化（Slack、tracker、仓库、路由、control、模型、预算） |
| `pstack/automations/benny/skills/reproduce-and-fix-issues` | 311 | 经 app-control adapter 复现已分类的 Slack bug，验已有修复，**只在有前后证据后才开有界 draft PR** |
| `third_party/google-docs` | 120 | 用 google-docs 工具写/编 Google Docs |
| `third_party/google-sheets` | 87 | 建/编 Google Sheets（值、格式、图表、条件格式、校验、命名/保护区域） |
| `third_party/google-slides` | 125 | 建/编 Google Slides（幻灯片网格、文本框、形状、图片、表格、逐页 PNG 渲染） |
| `third_party/x/skills/x-api-mcp-guide` | 357 | X API MCP 指南 |
| `third_party/x/skills/x-chat` | 185 | X 聊天 |
| `third_party/x/skills/x-money-guide` | 173 | X 财经指南 |
| `third_party/zoom`、`third_party/xero` | — | **无 `SKILL.md`**；各自有 `LICENSE`，scout 未读正文 |

### 4.4 Q-B 小结（描述，不裁决）

- **58 条中，`third_party` 6 条与 `grok-voice` 4 条明显是产品/平台 API 绑定**（Google 办公套件、X API、语音），
  与本库「工程工作流」不同域。**这是描述，不是拒绝建议。**
- **`orchestrate`、`thermos`、`advisor`、`continual-learning`、`workflow-from-chats`、`verify-this`、
  `review-and-ship`、`retro`（在 in-progress）这 8 条的 frontmatter 描述里出现了与本库判据同形的措辞**
  （显式触发不自启、并行子代理后综合、验证三态、环境改进候选）。**这只说明「值得读正文」，不构成吸收。**
- **`thermo-nuclear-code-quality-review` 在 `cursor-team-kit` 与 `thermos` 两处各有一份，均 193 行。**
  重复事实，见 §7。

### 4.5 「本库用得上吗」—— 故意留空 UNVERIFIED

**判定需要的东西我没有**：要判「用得上」必须逐条比对 `registry.yaml:upstream_dispositions`（101 条）与本库
`skills/`（49 个文件）、`roles/`（9 个文件）的现有覆盖，并判断**重复/互补/冲突**。
这是 58 次独立比对，超出本轮只读清点的范围，且**结论就是裁决**——scout 不做。
**记 UNVERIFIED。缺的是：与 adversary 共享的判定判据（Owner 尚未给）。**

## 5. Q-C · `in-progress` 九个逐个读正文

**9/9 读完正文。** 每条给：讲什么 + 与本库 `skills/` 的重叠 + 重叠在哪一条。
**重叠是描述性的事实对比，不是「该不该吸收」的判断。**

### 5.1 `claude-handoff`（19 行）
- **正文要点**（`upstreams/mattpocock-skills/skills/in-progress/claude-handoff/SKILL.md:7` 逐字）：
  > `Instead of saving it, launch a background agent seeded with the summary as its prompt: \`claude --bg --name "<descriptive name>" "<handoff summary>"\`.`
- 它要求交接摘要含「suggested skills」段（`:12` 逐字）：
  > `Include a "suggested skills" section in the summary, naming which skills the next agent should call the Skill tool for.`
- 还要求不重复已在别处捕获的内容（`:14`）、脱敏（`:16`）。
- **与本库重叠**：`skills/handoff.md` 存在。**重叠在「交接摘要该装什么」这一层**——
  本库 handoff 是落盘产物，in-progress 这条是**不落盘、直接起后台进程**，且多一条「点名下一个 agent 该用哪些 skill」。
  本库 `AGENTS.md`「跨 harness 交接」一节讲的是「只放接手方需要的东西」，与 `:14` 的不重复指令同向。

### 5.2 `implement-spec`（36 行）
- **正文要点**（`:11` 逐字）：
  > `The tickets are not a list of steps. They are a **task graph** with blocking relationships between them. This means there is always a **frontier** of tickets which are ready to be grabbed.`
- `:13` 逐字：
  > `Communication to and from subagents should be sparse. Communicate primarily through **context pointers**: to the spec, tickets, research notes, and previous commits. Don't duplicate information already available via pointers.`
- `:10-12` 要求 exploration subagent 的笔记存**仓外**目录，理由是让 implementer 专注实现。
- **与本库重叠**：`skills/to-tickets.md`、`skills/implement.md`、`skills/task-breakdown.md` 都在。
  **重叠在「ticket 之间是不是有依赖图」这一条**——本库 `to-tickets` 的产物契约里写了 dependencies，
  但「frontier / 抢单 / 按依赖解锁下一批」这套**调度语义**在上游是显式的，在本库 `driver.md` 侧有相近位置。
  **描述到此为止，是否重复由 adversary 判。**

### 5.3 `loop-me`（33 行）
- **正文要点**（`:7` 逐字）：
  > `Run a stateful \`/grilling\` session whose only output is **workflow** specs.`
- 词表（`:17-24` 逐字摘）：`Trigger` / `Checkpoint` / `Push right` / `Brief`。
  - `:21` 逐字：`> **Push right**: defer the checkpoint as far as it will go. Do maximal work before involving the human, so they are asked once, late, with everything prepared.`
  - `:23` 逐字：`> **Brief**: what a checkpoint presents, a tight, decision-ready summary (what was produced, why, and a link down to the asset itself), never the raw output. The user reads a brief, not a draft. Speed of review is imperative.`
- 明确的反结构约束（`:15` 逐字）：
  > `> **Mandate nothing structural**: a workflow needs no AI, no checkpoint, and no schedule unless the grilling shows it does.`
- **完成判据**（`:27` 逐字）：
  > `A workflow spec is done when an implementer agent could build it without asking a single question. Grill until then; nothing is done while a question remains.`
- **与本库重叠**：`skills/grilling.md`、`skills/wayfinder.md` 都在。
  **重叠在两条**：(a)「完成判据 = 下一个 agent 不用问问题就能做完」——与本库 driver 的 artifact 够格判据同形；
  (b) `Brief ≠ raw output`——与本库 driver 收 packet 的判据同形。
  **本库无对应文件承载「Push right」与「Trigger 优先于 Schedule」**（描述，不裁决）。

### 5.4 `pr`（169 行）
- **正文要点**：`description: "Use when writing a PR body."`（`:3` 逐字）。frontmatter 带 credits，
  来源是 Humanlayer 的 `show-me` skill（`:5-9` 逐字 `author: Dex Horthy` / `organisation: Humanlayer`）。
- 正文给一个三段模板：`## Summary` / `## Evidence`（Before-After）/ `## Merge Danger`（`Door` + `Blast Radius`）。
- 同目录另有 `upstreams/mattpocock-skills/skills/in-progress/pr/CREDITS.md`。
- **与本库重叠**：本库 `skills/git-workflow-and-versioning.md` 覆盖提交面；`skills/shipping-and-launch.md` 覆盖发布面。
  **重叠在「PR 正文模板」这一条**——本库**没有**独立 PR 正文模板文件。
  **注意**：本库硬边界第 5 条禁止输出未经上游提炼的流程清单；这份模板是上游自带的，
  是否构成「吸收一份模板」是裁决，scout 不判。

### 5.5 `retro`（45 行）
- **正文要点**（`:7` 逐字）：
  > `The user has asked for a **retrospective**. You are suggesting improvements to the coding agent's **environment** to improve future runs.`
- 七类候选（`:17-23`）：Navigation / Automated checks / Coding standards / Global AGENTS.md / Tool economy / No-ops / Information access。
- 两条最硬的子判据，逐字：
  - `:19` 逐字：`> Classify the violation first: a **mechanical** one (a fixed syntactic pattern, a banned API, an import shape, a file-location rule) gets a deterministic check, full stop... Default to building the check over writing the rule. Reserve \`CODING_STANDARDS.md\` for genuine **judgement calls** (cross-file consistency, "matches the surrounding style," anything no guardrail could ever substitute for).`
  - `:18` 逐字：`> A repo with no **guardrail** (no pre-commit hook and no CI job running its lint/typecheck/test command) is itself a finding: an un-linted repo is a standing missed opportunity, not a neutral default.`
- **与本库重叠**：本库有 `scripts/` 三检查器 + `AGENTS.md`「新增检查的保留判据」。
  **重叠在两条**：(a)「mechanical 违规默认建确定性检查，不写进规则文本」——
  与本库硬边界第 2 条「不得为让检查变绿而削弱检查」及「新增检查的保留判据」**方向同构**；
  (b)「本库自己的仓有没有 guardrail」——本库有 `AGENTS.md` 的四条命令段，**有**。
  **本库无对应文件承载「retro 七类候选」清单本身。**

### 5.6 `setup-ts-deep-modules`（103 行）
- **正文要点**（`:9` 逐字）：
  > `Make every package in this repo a **deep module**: a lot of behaviour behind a small interface. A package's public surface is its **entry points** (the files at the package root), and everything in its subfolders is hidden.`
- 明确要求复用 `codebase-design` 的词表（`:11` 逐字）：
  > `For the vocabulary (deep module, interface, seam, depth), call the Skill tool with "codebase-design" and use its language throughout.`
- 四条规则全为 `error` 级（`:20-27`）：entry-point boundary / intra-package freedom / tests through the entry points / no cycles。
- `:29` 逐字：
  > `**Entry points, not a barrel.** Because the public surface is *every* root file, a package can expose several small entry points (\`index.ts\`, \`client.ts\`, \`server.ts\`) instead of funnelling everything through one giant \`index.ts\`.`
- **与本库重叠**：`skills/codebase-design.md` 在，且本库 `upstream_dispositions` 已收 `matt:codebase-design`（absorbed）。
  **重叠点是词表本身，不是新东西。** 真正**不在**上游正文里的、只在**这条**里的是：
  **可执行的 dependency-cruiser 配置 + 四条 error 级规则**。
  本库硬边界第 5 条明说本库 Driver **不定义 execution mechanics**；dependency-cruiser 规则属不属于「方法」而非「机制」，
  **scout 不判**。

### 5.7 `writing-beats`（68 行）
- **正文要点**（`:9` 逐字）：
  > `The user has passed (or will pass) a markdown file of raw material. This is **exploit**: the exploring is done, the pile is fixed.`
- 每个 beat 做两件事（`:39-40` 逐字）：
  > `So each beat does two jobs: it **requires** concepts that are already grounded, and it **grounds** new ones. Keep a running list of what's grounded so far, and update it each time a beat lands.`
- 关键机制（`:33` 逐字）：
  > `The unit is the concept, not the word for it: a beat can lean on an idea the reader lacks even with no jargon in sight.`
- **与本库重叠**：本库 `skills/technical-writing.md` 存在。**重叠在「每个块必须先落地它依赖的概念」这一条**。
  本库无对应文件承载 explore/exploit 二分（in-progress 三条共用这个二分，见 §5.9）。

### 5.8 `writing-fragments`（80 行）
- **正文要点**（`:7` 逐字）：
  > `This is pure **explore**: widen the space of what could be written without committing to structure. Committing is _exploit_, a separate skill's job. Run a grilling session that produces fragments, interviewing the user relentlessly about whatever they want to write about. Imposing phases, outlines, or article structure is out of scope here.`
- fragment 的判据（`:26-28` 逐字）：
  > `It must be _readable by the author_ (the author can tell what it means), but it does not need to define its terms or be comprehensible to a cold reader. The bar is "is this a piece of good writing?", not "is this a self-contained argument?"`
- 首写格式约束（`:15` 逐字）：
  > `On first write, put a single H1 at the top with a working title (it can change later) and nothing else: no metadata, no TOC, no date.`
- **与本库重叠**：`skills/technical-writing.md` 在。**重叠在「素材期禁止提前定结构」这一条**——
  与本库 `hard boundary` 精神同向，但本库**无**承载「explore / exploit 是两个 skill 的职责」这一分的文件。
  **本库无**与本条对应的文件（描述）。

### 5.9 `writing-shape`（80 行）
- **正文要点**（`:7` 逐字）：
  > `This is **exploit**: the exploring is done, the pile is fixed: commit to a structure and mine the pile to fill it. Do not edit the raw material file: it is read-only to this skill.`
- 循环六步（`:19-27`），关键两条：
  - `:24` 逐字：`> Pull material from the pile to answer. The next block may only lean on grounded concepts, and grounds new ones as it lands.`
  - `:25` 逐字：`> Argue about the form the next block takes: a paragraph, a list, a table, a callout, a quote, a code block. Each format choice should be deliberate and defensible.`
- 「先读完整堆再动手」（`:15` 逐字）：`Read it end-to-end before doing anything else.`
- **与本库重叠**：`skills/technical-writing.md`。**重叠在 grounding 机制**（与 5.7 同一机制，正文措辞几乎一致）。
  **本库无**承载「块的形式本身要可辩护」这一条的文件。

### 5.10 Q-C 小结（描述）

- **9 条中 3 条是写作三件套**（fragments / beats / shape），共用 explore-exploit 二分 + grounding 机制，
  正文措辞高度重复（`writing-beats:33` 与 `writing-shape` 的 Grounding 段落几乎同文）。
- **9 条中 2 条（`retro`、`loop-me`）的完成判据与本库 driver 判据同形**——这是本轮最值得 driver 注意的重叠面。
- **9 条全部不在 `upstreams.lock.yaml`**，因此**全部不在 `registry.yaml:upstream_dispositions`**（§6 实测：101 条全在锁内）。
  即：**处置表对这一批 9 条连「已拒绝」这一格都没有**。

## 6. Q-D · 判 `rejected` 但找不到正文的条目

### 6.1 实测结果：**空集。0 条。**

`workflow/registry.yaml:1131-1236` 共 **101 条**处置条目，scout 逐条解析：

| outcome | 条数 |
|---|---|
| `absorbed` | 81 |
| `rejected` | 20 |
| 其它 | 0（处置表**只有这两格**，与任务书背景描述一致） |

**20 条 `rejected` 逐条核实体，全部命中磁盘 `SKILL.md`**：

| registry 行 | upstream key | 磁盘实体 |
|---|---|---|
| 1133 | `pstack:figure-it-out` | `upstreams/cursor-plugins/pstack/skills/figure-it-out/SKILL.md` |
| 1134 | `pstack:bro` | `upstreams/cursor-plugins/pstack/skills/bro/SKILL.md` |
| 1136 | `pstack:setup-pstack` | `upstreams/cursor-plugins/pstack/skills/setup-pstack/SKILL.md` |
| 1146 | `pstack:automate-me` | `upstreams/cursor-plugins/pstack/skills/automate-me/SKILL.md` |
| 1151 | `pstack:no-comments` | `upstreams/cursor-plugins/pstack/skills/no-comments/SKILL.md` |
| 1152 | `pstack:unslop` | `upstreams/cursor-plugins/pstack/skills/unslop/SKILL.md` |
| 1154 | `pstack:typescript-best-practices` | `upstreams/cursor-plugins/pstack/skills/typescript-best-practices/SKILL.md` |
| 1155 | `pstack:poteto-mode` | `upstreams/cursor-plugins/pstack/skills/poteto-mode/SKILL.md` |
| 1156 | `pstack:make-bot-ui` | `upstreams/cursor-plugins/pstack/skills/make-bot-ui/SKILL.md` |
| 1184 | `matt:setup-matt-pocock-skills` | `upstreams/mattpocock-skills/skills/engineering/setup-matt-pocock-skills/SKILL.md` |
| 1188 | `matt:ask-matt` | `upstreams/mattpocock-skills/skills/engineering/ask-matt/SKILL.md` |
| 1189 | `matt:wizard` | `upstreams/mattpocock-skills/skills/engineering/wizard/SKILL.md` |
| 1190 | `matt:improve-codebase-architecture` | `upstreams/mattpocock-skills/skills/engineering/improve-codebase-architecture/SKILL.md` |
| 1195 | `matt:resolving-merge-conflicts` | `upstreams/mattpocock-skills/skills/engineering/resolving-merge-conflicts/SKILL.md` |
| 1200 | `matt:wait-what` | `upstreams/mattpocock-skills/skills/productivity/wait-what/SKILL.md` |
| 1206 | `matt:setup-pre-commit` | `upstreams/mattpocock-skills/skills/misc/setup-pre-commit/SKILL.md` |
| 1207 | `matt:git-guardrails-claude-code` | `upstreams/mattpocock-skills/skills/misc/git-guardrails-claude-code/SKILL.md` |
| 1208 | `matt:migrate-to-shoehorn` | `upstreams/mattpocock-skills/skills/misc/migrate-to-shoehorn/SKILL.md` |
| 1209 | `matt:scaffold-exercises` | `upstreams/mattpocock-skills/skills/misc/scaffold-exercises/SKILL.md` |
| 1213 | `addy:using-agent-skills` | `upstreams/addyosmani-agent-skills/skills/using-agent-skills/SKILL.md` |

**同时核了正向：101 条全部能解析到磁盘实体，0 条悬空。**

### 6.2 UPRESCAN N12 的锚点复核

任务书要独立复核 N12（「`registry.yaml:1180` 判 rejected 但没读正文」）。**实测：`registry.yaml:1180` 不是处置条目。**

逐字（`workflow/registry.yaml:1180`）：

```
  # ── matt (29)
```

它是一行**分节注释**。相邻的处置条目是 `1181`（`matt:research`，`outcome: absorbed`）与 `1183`（`matt:wayfinder`，`absorbed`）。

**结论（事实）**：N12 指向的行号不对。`1180` 上没有任何 `rejected` 判定，因此**「1180 判 rejected 但没读正文」这条不成立**。
**Q-D 的真实答案是空集：20 条 rejected 全部有正文。**
**N12 是否指另一条条目，scout 不知道 —— UNVERIFIED，缺的是 N12 的原文上下文。**

### 6.3 Q-D 真正的盲区（不是「悬空条目」，是另一件事）

`registry.yaml:upstream_dispositions` 的 101 条**全部对应锁内 skill**（§6.1 正向核 0 悬空）。
所以处置表对 §1 那 **58 个 + §3 那 1080 个非 SKILL.md 文件**，
**连「已拒绝」这一格都没有** —— 它们不是「判了但没读」，是**根本没被枚举到，因此无法被判**。

这正是 Owner 要的「至少可见」的缺口本体：**不可见 ≠ 不存在**。

## 7. 顺带查到的事实（只记录，不修）

| # | 事实 | 锚点 | 状态 |
|---|---|---|---|
| F1 | `thermo-nuclear-code-quality-review` 在两处各存一份，均 193 行 | `upstreams/cursor-plugins/thermos/skills/thermo-nuclear-code-quality-review/SKILL.md` 与 `upstreams/cursor-plugins/cursor-team-kit/skills/thermo-nuclear-code-quality-review/SKILL.md` | 两条都在 58 个清单里，**scout 未逐字 diff，内容是否完全相同 UNVERIFIED** |
| F2 | `thermo-nuclear-code-quality-review` 另有 `agents/` 形态两份 | `upstreams/cursor-plugins/thermos/agents/thermo-nuclear-code-quality-review-subagent.md`、`.../thermo-nuclear-review-subagent.md` | 已发现，未读正文 |
| F3 | `pstack` 有 10 篇 guide 文档（`01-setup` … `10-recipes-and-pitfalls`） | `upstreams/cursor-plugins/pstack/docs/guide/` | 已发现，未读正文。**不在 1080 之外也不在 101 内**——在 1080 内 |
| F4 | `pstack/skills/poteto-mode/playbooks/` 有 **23 个 playbook** | 见 §3 `.md` 分类表 | 已发现，未读正文 |
| F5 | `pstack/skills/why/references/sources/` 有 9 份来源手册（sentry / datadog / linear / notion / slack / incident-postmortem / code-archaeology / databricks） | `upstreams/cursor-plugins/pstack/skills/why/references/sources/` | 已发现，未读正文 |
| F6 | 锁文件时间戳早于 `check-closure.py` | `upstreams.lock.yaml` mtime `Sep 28 06:15`；`scripts/check-closure.py` mtime `Sep 30 01:36` | **事实，不是缺陷。** 本轮**未运行** `_render-lock.py`，**未验证**锁文件是否已与上游实物脱节 → **UNVERIFIED** |
| F7 | 处置表只有 `absorbed` / `rejected` 两格 | `workflow/registry.yaml:1131-1236`，101 条，outcome 值集合 = {absorbed, rejected} | PASS |

## 8. 空结果清单（照实写，不补）

| 项 | 结果 |
|---|---|
| Q-D：判 `rejected` 但找不到正文的条目 | **0 条（空集）** |
| `references/` 下的 `SKILL.md` | **0 个**（57 个文件全是非 skill 载体） |
| `upstreams/**/references/` 之外被 `SKIP_DIRS` 隐藏的 skill | **0 个**（`references` 这条规则只藏非 skill 文件） |
| 处置表中悬空的 upstream key（101 条里） | **0 条** |
| `registry.yaml` 中第三种 outcome | **不存在** |
| `third_party/zoom`、`third_party/xero` 的 `SKILL.md` | **不存在**（各只有 `LICENSE`；正文未读） |
| `in-progress/` 下无 `SKILL.md` 的子目录 | **0 个**（9 个目录全有 `SKILL.md`；另有 1 个 `README.md`） |
| 58 个里 `description` 字段缺失的 | **0 个**（多行 `>-` 的 9 个按首行取，其余完整） |
| F1 两份 thermo-nuclear 文件是否逐字相同 | **UNVERIFIED**（未 diff） |
| 本轮是否运行过 `render.py` / `check-closure.py` / `check-consistency.py` / `compose-role.py` | **没有**（scout 只读，不执行写派生视图的脚本） |
| 锁文件是否已与上游实物脱节 | **UNVERIFIED**（未重跑 `_render-lock.py` 比对 sha256） |

## 9. 纪律自证

- 只读 `upstreams/` 与本库。**唯一写入 = 本文件。**
- 未执行 `git add` / `commit` / `tag`。`git status` 在开工前后一致（已有 staged 改动为 driver 与 scribe-b 的，非本轮）。
- 未修改 `registry.yaml` / `roles/` / `skills/` / `scripts/` / 任何 `upstreams/` 文件。
- **未裁决任何处置。** §4.4 与 §4.5 明确把「用得上吗」留为 UNVERIFIED 并写清缺什么。
- 每条事实带 `仓/路径:行号`；摘录逐字。
- 三态只用 PASS / FAIL / UNVERIFIED，**无 FAIL**（无失败断言），环境类缺口一律记 UNVERIFIED。


---

## 10. 追加（Oracle M3 派工 · 任务二结果）· 锁文件只读 sha256 核对

> 本节是 scout 上轮 F6「UNVERIFIED」的收口。完整版见姊妹文件
> `docs/history/derivation-0930/UPSTREAM-CARRIER-LEDGER-0930.md` §7。

### 10.1 三态结论

| 项 | 状态 | 实测 |
|---|---|---|
| 逐仓 commit pin vs 实际 git HEAD | **PASS** | 3/3 一致，0 漂移 |
| 逐 skill sha256（101 条） | **PASS** | 101/101 一致，0 漂移，0 缺失 |
| 只读重跑 `_render-lock.py` 枚举逻辑 | **PASS** | 101 条，与锁双向零差集 |
| `upstreams.lock.yaml` 是否被改动 | **PASS（零改动）** | 未运行 `_render-lock.py`；sha256 与 mtime 见 §10.4 |
| **F6 原状态** | **UNVERIFIED → 已排除** | 「可能已脱节」经核对**不成立** |

### 10.2 关键事实：`pstack` 没有自己的 `.git`

`upstreams/cursor-plugins/pstack/` **不是独立 git 克隆**，它是父仓 `upstreams/cursor-plugins/` 的子目录
（`pstack/` 下只有 `.cursor-plugin/` 与 `.gitignore` 两个隐藏项，无 `.git`）。
scout 沿目录向上找到父仓，其 HEAD = `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`，
**与 `upstreams.lock.yaml:18` 的 pin 逐字相同**；`git cat-file -t` 确认该 commit 对象真实存在。

`matt` 与 `addy` 各有独立 `.git`，HEAD 与 pin 均逐字相同，工作区干净（`git status --porcelain` 空）。

### 10.3 只读保证

`scripts/_render-lock.py` docstring 第 5 行逐字：
> `只读 upstreams/，只写 upstreams.lock.yaml。不碰任何其他文件。`

**它会写 `upstreams.lock.yaml`，因此本轮没有运行它。**
按派工要求改写为只读等价代码（复用其 `REPOS`、`SKIP_DIRS`、`os.walk` 裁剪、`sha256[:16]`），输出只到 `/tmp`。

### 10.4 `upstreams.lock.yaml` 零改动自证

| 项 | 值 |
|---|---|
| sha256[:16] | `a056b2ced80d3a6e` |
| 大小 | 15451 字节 |
| mtime | 2026-09-28T06:15:40 |

注：`upstreams/` 被 `.gitignore` 挡着，`git status --porcelain upstreams/` 返回空 ——
**「git 干净」在此不足以单独作为证据**，故另给独立 sha256 与 mtime。

### 10.5 一条要留给 driver 的事实

**sha256 全绿 ≠ 枚举完整。** 101 条逐字节一致，但它们**只覆盖 `SKILL.md`**。
那 58 个不在锁里的 `SKILL.md` 与 1080 个非 `SKILL.md` 载体，**根本不在比对范围内**。
锁文件没有失效，是**它的覆盖面**不含它们。
`upstreams.lock.yaml:5-6` 逐字自述的用途是「处置表与上游实物之间那本可随包分发的账」——
**它没声称覆盖非 skill 载体。** 这不是缺陷，是设计边界。

### 10.6 F6 原陈述的处理

上轮 F6 写的是「锁文件 mtime `Sep 28 06:15` 早于 `check-closure.py` mtime `Sep 30 01:36`」+「可能已脱节」。

- **观察仍是事实**：mtime 先后关系未变。
- **推论不成立**：`check-closure.py` 后来被改过，不等于 `upstreams.lock.yaml` 变旧。
  **一个文件比另一个文件旧，不构成它失效的证据。**

按三态记：这不是 FAIL，是**上轮的怀疑被本轮证据排除**。
