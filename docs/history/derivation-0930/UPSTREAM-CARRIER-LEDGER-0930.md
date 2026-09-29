# UPSTREAM-CARRIER-LEDGER-0930 · 1080 载体完整路径清单 + 锁文件只读 sha256 核对

- **角色**：`scout`（`tpw-0930-scout-b`）· 找事实，不给结论，不裁决处置
- **driver**：`tpw-0930-driver` · **授权**：Oracle M3 派工
- **本文件**：`docs/history/derivation-0930/UPSTREAM-CARRIER-LEDGER-0930.md`（任务一落点）
- **姊妹文件**：`docs/history/derivation-0930/UPSTREAM-INVENTORY-0930.md`（任务二结果追加在 §6）
- **口径**（Oracle 认可）：按载体类给聚合计数 + **全部路径**，不逐条读正文。

## 0. 三态汇总

| 项 | 状态 | 依据 |
|---|---|---|
| 任务一 · 1080 载体完整路径清单 | **PASS** | §1-§4，25 类，全部路径列出，无省略、无「等」、无「若干」 |
| 任务一 · 三个沉默桶单独成节 | **PASS** | §2 in-progress 9 / §3 .changeset 13 / §4 evals 84 |
| 任务一 · third_party 476 单独成节 | **PASS** | §5，含建议（不裁） |
| 任务二 · 逐 skill sha256 核对 | **PASS** | §6.2，101/101 一致，0 漂移，0 缺失 |
| 任务二 · 逐仓 commit pin vs HEAD | **PASS** | §6.1，3/3 一致，含 pstack 的父仓解析 |
| 任务二 · 只读重跑 `_render-lock.py` 枚举逻辑 | **PASS** | §6.3，101 条与锁完全同集，0 差异 |
| 任务二 · `upstreams.lock.yaml` 是否被改动 | **PASS（零改动）** | §6.0，未运行 `_render-lock.py`（它会写 lock），改写只读等价代码；mtime 与 sha256 前后一致 |
| 载体类「本库是否有方法价值」三档初判 | **PASS（初判，非裁决）** | 每类一行理由，见各节 |
| 各类「是否已被本库吸收」 | **UNVERIFIED（故意留空）** | 需 adversary 判据，Owner 尚未给 |
| 任务一 · 1080 载体完整路径清单（M5 更正后重验） | **PASS** | `missing = 0`，与 1080 逐条闭合 |
| hooks 两份 `.md` 处置粒度 | **PASS（粒度已分开）** | §1.hooks 例外节；**吸收与否未裁定**，留给 driver 按裁定 §3 流程走 |
| FAIL | **无** | — |

### 0.1 M5 更正记录（2026-09-30 · 依 `0930-oracle-M34-DECISION.md` 第 2、3 节）

**作者更正，不改历史裁定**；更正后由作者以外的人复核（adversary）。**scout 不自评。**

| # | 位置 | 原值 | 新值 | 来源 |
|---|---|---|---|---|
| 1 | §5.3 理由一 | 会高估 **4.5 倍** | **已删除，不另造推导** | 裁定 §2 |
| 2 | §5.1b | 「真实待判规模」类推论 | 改为**两种筛选口径各自余量**（604 / 642），显式声明非裁定 | 裁定 §2 |
| 3 | §5.1 / §8 | 「零正文」/「有方法正文」 | 「**未识别到方法正文**」（证据限定表述） | 裁定 §2 |
| 4 | §5.1 | 73 份 README 事实 | **保留**，改写为「信息各不相同」≠「是否含可迁移方法」 | 裁定 §2 |
| 5 | §2 | in-progress **20**（9+11） | **21**（9+12），补 `dependency-cruiser.config.cjs` | 裁定 §2 |
| 6 | §5.2 | `x` 包 **8** | **9** | 裁定 §2 |
| 7 | §1.agents | **39 / 16** | **38 / 17** | 裁定 §2 |
| 8 | §1.commands | 「9 条同一套」 | **8 同名 + 1 不一致**（`.claude`=`plan`，另两处=`planning`） | 裁定 §2 |
| 9 | §1.evals | 27 case + 4 组 grader | **cases 25 + plugin 3 组场景（6 grader + 3 prompt）**，**补列 fixtures 48** | 裁定 §2 |
| 10 | §1.hooks | 「20 份（sh/ts/json）」 | **14 sh + 3 json + 1 ts + 2 md**，点名 2 份 `.md` | 裁定 §2 |
| 11 | §1.hooks | 2 份 `.md` 被连带排除 | **改单独处置**，裁定只批准粒度、**未裁定吸收** | 裁定 §3 |
| 12 | §1.docs | 25 / 11 / 22 | **9 setup + 7 其他 / 11 md + 6 图 / 25** | **scout 自查**（裁定未列） |
| 13 | §1 根级 md | 19 / 43 | **10 + 23 / 29** | **scout 自查**（裁定未列） |

**scout 自查中又撤回一处自己的错**：中间稿曾把 `third_party` 总量写成 483，实测 **482**（73×6+38+7），
已改回 482；见 §5.1 表下注记。

---

## 1. 载体类完整清单（方法价值初判：高/中/低）

**初判不是裁决。** 三档只回答「本库**可能**从中拿到方法」这一层直觉，处置由 adversary / Owner 定。

### 1.references · `references/（skill 自带 + 仓根）` — 56 个 · 初判 **高**

**理由**：56 份全是判据/清单/模板类正文，且被 `SKIP_DIRS` 结构性隐藏；本库判据体系缺的正是这类可读判据文本。

```
addyosmani-agent-skills/references/accessibility-checklist.md
addyosmani-agent-skills/references/definition-of-done.md
addyosmani-agent-skills/references/observability-checklist.md
addyosmani-agent-skills/references/orchestration-patterns.md
addyosmani-agent-skills/references/performance-checklist.md
addyosmani-agent-skills/references/security-checklist.md
addyosmani-agent-skills/references/testing-patterns.md
addyosmani-agent-skills/skills/constraint-driven-development/references/floor-guard.md
addyosmani-agent-skills/skills/security-and-hardening/references/hardening-patterns.md
cursor-plugins/advisor/skills/advisor/references/briefing-template.md
cursor-plugins/cursor-sdk/skills/cursor-sdk/references/advanced.md
cursor-plugins/cursor-sdk/skills/cursor-sdk/references/auth.md
cursor-plugins/cursor-sdk/skills/cursor-sdk/references/error-handling.md
cursor-plugins/cursor-sdk/skills/cursor-sdk/references/mcp.md
cursor-plugins/cursor-sdk/skills/cursor-sdk/references/patterns.md
cursor-plugins/cursor-sdk/skills/cursor-sdk/references/runtime-choice.md
cursor-plugins/cursor-sdk/skills/cursor-sdk/references/streaming.md
cursor-plugins/orchestrate/skills/orchestrate/references/dispatcher.md
cursor-plugins/orchestrate/skills/orchestrate/references/handoffs.md
cursor-plugins/orchestrate/skills/orchestrate/references/planner.md
cursor-plugins/orchestrate/skills/orchestrate/references/spawning.md
cursor-plugins/pstack/automations/benny/skills/reproduce-and-fix-issues/references/control-adapter.md
cursor-plugins/pstack/automations/benny/skills/reproduce-and-fix-issues/references/feature-map.example.md
cursor-plugins/pstack/automations/benny/skills/reproduce-and-fix-issues/references/verify-existing-fix.md
cursor-plugins/pstack/automations/benny/skills/triage-issue-reports/references/routing.example.md
cursor-plugins/pstack/skills/architect/references/design-red-flags.md
cursor-plugins/pstack/skills/architect/references/rationale-template.md
cursor-plugins/pstack/skills/architect/references/runner-prompt.md
cursor-plugins/pstack/skills/create-verification-skill/references/feature-map-example/README.md
cursor-plugins/pstack/skills/create-verification-skill/references/feature-map-example/create-note.md
cursor-plugins/pstack/skills/create-verification-skill/references/feature-map-example/search.md
cursor-plugins/pstack/skills/how/references/explainer-prompt.md
cursor-plugins/pstack/skills/how/references/explorer-prompt.md
cursor-plugins/pstack/skills/interrogate/references/code-quality-review.md
cursor-plugins/pstack/skills/interrogate/references/lead-judgment.md
cursor-plugins/pstack/skills/interrogate/references/reviewer-prompt.md
cursor-plugins/pstack/skills/interrogate/references/rubric.md
cursor-plugins/pstack/skills/poteto-mode/references/bugbot-triage.md
cursor-plugins/pstack/skills/reflect/references/divergent-reviewer.md
cursor-plugins/pstack/skills/reflect/references/judgment-reviewer.md
cursor-plugins/pstack/skills/reflect/references/synthesizer.md
cursor-plugins/pstack/skills/reflect/references/tooling-reviewer.md
cursor-plugins/pstack/skills/show-me-your-work/references/decision-log-template.tsv
cursor-plugins/pstack/skills/typescript-best-practices/references/patterns.md
cursor-plugins/pstack/skills/why/references/epistemics.md
cursor-plugins/pstack/skills/why/references/investigator-prompt.md
cursor-plugins/pstack/skills/why/references/source-playbook.md
cursor-plugins/pstack/skills/why/references/sources/code-archaeology.md
cursor-plugins/pstack/skills/why/references/sources/databricks.md
cursor-plugins/pstack/skills/why/references/sources/datadog.md
cursor-plugins/pstack/skills/why/references/sources/incident-postmortem.md
cursor-plugins/pstack/skills/why/references/sources/linear.md
cursor-plugins/pstack/skills/why/references/sources/notion.md
cursor-plugins/pstack/skills/why/references/sources/sentry.md
cursor-plugins/pstack/skills/why/references/sources/slack.md
cursor-plugins/pstack/skills/why/references/synthesizer-prompt.md
```

### 1.playbooks · `playbooks/` — 23 个 · 初判 **高**

**理由**：23 个是可直接对照本库 phase 的成文流程剧本，本库 `phases/` 无对应物。

```
cursor-plugins/pstack/skills/poteto-mode/playbooks/authoring-a-skill.md
cursor-plugins/pstack/skills/poteto-mode/playbooks/autonomous-run.md
cursor-plugins/pstack/skills/poteto-mode/playbooks/autopilot-full.md
cursor-plugins/pstack/skills/poteto-mode/playbooks/autopilot-stack.md
cursor-plugins/pstack/skills/poteto-mode/playbooks/babysit.md
cursor-plugins/pstack/skills/poteto-mode/playbooks/bug-fix.md
cursor-plugins/pstack/skills/poteto-mode/playbooks/eval.md
cursor-plugins/pstack/skills/poteto-mode/playbooks/feature.md
cursor-plugins/pstack/skills/poteto-mode/playbooks/hillclimb.md
cursor-plugins/pstack/skills/poteto-mode/playbooks/investigation.md
cursor-plugins/pstack/skills/poteto-mode/playbooks/multi-phase-plan.md
cursor-plugins/pstack/skills/poteto-mode/playbooks/opening-a-pr.md
cursor-plugins/pstack/skills/poteto-mode/playbooks/orchestrate.md
cursor-plugins/pstack/skills/poteto-mode/playbooks/pause-safely.md
cursor-plugins/pstack/skills/poteto-mode/playbooks/perf-issue.md
cursor-plugins/pstack/skills/poteto-mode/playbooks/prototype.md
cursor-plugins/pstack/skills/poteto-mode/playbooks/refactoring.md
cursor-plugins/pstack/skills/poteto-mode/playbooks/runtime-forensics.md
cursor-plugins/pstack/skills/poteto-mode/playbooks/session-pickup.md
cursor-plugins/pstack/skills/poteto-mode/playbooks/shipping.md
cursor-plugins/pstack/skills/poteto-mode/playbooks/trace-forensics.md
cursor-plugins/pstack/skills/poteto-mode/playbooks/visual-parity.md
cursor-plugins/pstack/skills/poteto-mode/playbooks/worktree-cleanup.md
```

### 1.prompts · `prompts/` — 10 个 · 初判 **高**

**理由**：10 份是 orchestrate 的角色 prompt 全文（root/worker/verifier/subplanner/handoff），与本库 `roles/` 正是一一对应的关系。

```
cursor-plugins/orchestrate/skills/orchestrate/prompts/andon-block.md
cursor-plugins/orchestrate/skills/orchestrate/prompts/empty-error-handoff.md
cursor-plugins/orchestrate/skills/orchestrate/prompts/failure-handoff.md
cursor-plugins/orchestrate/skills/orchestrate/prompts/finished-no-handoff.md
cursor-plugins/orchestrate/skills/orchestrate/prompts/loop-hygiene.md
cursor-plugins/orchestrate/skills/orchestrate/prompts/root.md
cursor-plugins/orchestrate/skills/orchestrate/prompts/slack-block.md
cursor-plugins/orchestrate/skills/orchestrate/prompts/subplanner.md
cursor-plugins/orchestrate/skills/orchestrate/prompts/verifier.md
cursor-plugins/orchestrate/skills/orchestrate/prompts/worker.md
```

### 1.agents · `agents/` — 55 个 · 初判 **中**

**理由**：55 份里 **38** 份是 `agents/openai.yaml` 模型映射配置（低价值），**17** 份是真 agent 人格定义 `.md`（与本库 `roles/` 同形）。

> **M5 更正（2026-09-30）**：原写「39 份 / 16 份」→ **新值 38 份 / 17 份**。
> 原值源于把 `cursor-plugins/pstack/skills/interrogate/…` 之外的一份记错。复核方法：对 `agents/` 类 55 条路径按「后缀是否 `.md`」二分，实测 `.md` = 17、`openai.yaml` = 38。清单本身未变。

```
addyosmani-agent-skills/agents/code-reviewer.md
addyosmani-agent-skills/agents/security-auditor.md
addyosmani-agent-skills/agents/test-engineer.md
addyosmani-agent-skills/agents/web-performance-auditor.md
cursor-plugins/advisor/agents/advisor-subagent.md
cursor-plugins/agent-compatibility/agents/compatibility-scan-review.md
cursor-plugins/agent-compatibility/agents/docs-reliability-review.md
cursor-plugins/agent-compatibility/agents/startup-review.md
cursor-plugins/agent-compatibility/agents/validation-review.md
cursor-plugins/continual-learning/agents/agents-memory-updater.md
cursor-plugins/create-plugin/agents/plugin-architect.md
cursor-plugins/cursor-team-kit/agents/ci-watcher.md
cursor-plugins/cursor-team-kit/agents/thermo-nuclear-code-quality-review.md
cursor-plugins/pstack/agents/comment-sicko.md
cursor-plugins/pstack/agents/poteto-agent.md
cursor-plugins/thermos/agents/thermo-nuclear-code-quality-review-subagent.md
cursor-plugins/thermos/agents/thermo-nuclear-review-subagent.md
mattpocock-skills/skills/engineering/ask-matt/agents/openai.yaml
mattpocock-skills/skills/engineering/code-review/agents/openai.yaml
mattpocock-skills/skills/engineering/codebase-design/agents/openai.yaml
mattpocock-skills/skills/engineering/diagnosing-bugs/agents/openai.yaml
mattpocock-skills/skills/engineering/domain-modeling/agents/openai.yaml
mattpocock-skills/skills/engineering/grill-with-docs/agents/openai.yaml
mattpocock-skills/skills/engineering/implement/agents/openai.yaml
mattpocock-skills/skills/engineering/improve-codebase-architecture/agents/openai.yaml
mattpocock-skills/skills/engineering/prototype/agents/openai.yaml
mattpocock-skills/skills/engineering/research/agents/openai.yaml
mattpocock-skills/skills/engineering/resolving-merge-conflicts/agents/openai.yaml
mattpocock-skills/skills/engineering/setup-matt-pocock-skills/agents/openai.yaml
mattpocock-skills/skills/engineering/tdd/agents/openai.yaml
mattpocock-skills/skills/engineering/to-spec/agents/openai.yaml
mattpocock-skills/skills/engineering/to-tickets/agents/openai.yaml
mattpocock-skills/skills/engineering/triage/agents/openai.yaml
mattpocock-skills/skills/engineering/wayfinder/agents/openai.yaml
mattpocock-skills/skills/engineering/wizard/agents/openai.yaml
mattpocock-skills/skills/in-progress/claude-handoff/agents/openai.yaml
mattpocock-skills/skills/in-progress/implement-spec/agents/openai.yaml
mattpocock-skills/skills/in-progress/loop-me/agents/openai.yaml
mattpocock-skills/skills/in-progress/pr/agents/openai.yaml
mattpocock-skills/skills/in-progress/retro/agents/openai.yaml
mattpocock-skills/skills/in-progress/setup-ts-deep-modules/agents/openai.yaml
mattpocock-skills/skills/in-progress/writing-beats/agents/openai.yaml
mattpocock-skills/skills/in-progress/writing-fragments/agents/openai.yaml
mattpocock-skills/skills/in-progress/writing-shape/agents/openai.yaml
mattpocock-skills/skills/misc/git-guardrails-claude-code/agents/openai.yaml
mattpocock-skills/skills/misc/migrate-to-shoehorn/agents/openai.yaml
mattpocock-skills/skills/misc/scaffold-exercises/agents/openai.yaml
mattpocock-skills/skills/misc/setup-pre-commit/agents/openai.yaml
mattpocock-skills/skills/productivity/grill-me/agents/openai.yaml
mattpocock-skills/skills/productivity/grilling/agents/openai.yaml
mattpocock-skills/skills/productivity/handoff/agents/openai.yaml
mattpocock-skills/skills/productivity/teach/agents/openai.yaml
mattpocock-skills/skills/productivity/to-questionnaire/agents/openai.yaml
mattpocock-skills/skills/productivity/wait-what/agents/openai.yaml
mattpocock-skills/skills/productivity/writing-for-agents/agents/openai.yaml
```

### 1.commands · `commands/` — 27 个 · 初判 **中**

**理由**：27 份是 9 条命令 × 3 处落地（`.claude/commands` 9 个 `.md`、`.gemini/commands` 9 个 `.toml`、仓根 `commands` 9 个 `.toml`）。**8 条命令在三处同名**（`build` / `code-simplify` / `constraints` / `review` / `ship` / `spec` / `test` / `webperf`），**1 条不一致**：`.claude` 用 `plan`，`.gemini` 与仓根用 `planning`。方法价值在 `.claude` 那 9 份。

> **M5 更正（2026-09-30）**：原写「9 条命令 × 3 种 harness 的同一套命令的重复落地」→ **新值 8 条三处同名 + 1 条不一致**。
> 原值把 `plan` / `planning` 当成同一命令。复核方法：三处文件名 stem 求集合，三处交集 8 个，`plan` 仅 `.claude` 有、`planning` 仅另两处有。清单本身未变。

```
addyosmani-agent-skills/.claude/commands/build.md
addyosmani-agent-skills/.claude/commands/code-simplify.md
addyosmani-agent-skills/.claude/commands/constraints.md
addyosmani-agent-skills/.claude/commands/plan.md
addyosmani-agent-skills/.claude/commands/review.md
addyosmani-agent-skills/.claude/commands/ship.md
addyosmani-agent-skills/.claude/commands/spec.md
addyosmani-agent-skills/.claude/commands/test.md
addyosmani-agent-skills/.claude/commands/webperf.md
addyosmani-agent-skills/.gemini/commands/build.toml
addyosmani-agent-skills/.gemini/commands/code-simplify.toml
addyosmani-agent-skills/.gemini/commands/constraints.toml
addyosmani-agent-skills/.gemini/commands/planning.toml
addyosmani-agent-skills/.gemini/commands/review.toml
addyosmani-agent-skills/.gemini/commands/ship.toml
addyosmani-agent-skills/.gemini/commands/spec.toml
addyosmani-agent-skills/.gemini/commands/test.toml
addyosmani-agent-skills/.gemini/commands/webperf.toml
addyosmani-agent-skills/commands/build.toml
addyosmani-agent-skills/commands/code-simplify.toml
addyosmani-agent-skills/commands/constraints.toml
addyosmani-agent-skills/commands/planning.toml
addyosmani-agent-skills/commands/review.toml
addyosmani-agent-skills/commands/ship.toml
addyosmani-agent-skills/commands/spec.toml
addyosmani-agent-skills/commands/test.toml
addyosmani-agent-skills/commands/webperf.toml
```

### 1.hooks · `hooks/` — 20 个 · 初判 **中**

**理由**：20 份 = **14 个 `.sh` + 3 个 `.json` + 1 个 `.ts` + 2 个 `.md`**。前 18 份是运行时钩子实现；本库明确不定义 execution mechanics，故其方法价值中等、机制价值高。**后 2 份 `.md` 不是实现，是文档 —— 已按 M5 裁定改为单独处置，见 §1.hooks 附节。**

> **M5 更正（2026-09-30）**：原写「20 份是运行时钩子实现（sh/ts/json）」→ **新值 18 份实现 + 2 份 `.md` 文档**。
> 原值漏点名两份 `.md`：`hooks/SDD-CACHE.md` 与 `hooks/SIMPLIFY-IGNORE.md`，并把它们连带归入「不吸收」。清单本身未变。

```
addyosmani-agent-skills/hooks/SDD-CACHE.md
addyosmani-agent-skills/hooks/SIMPLIFY-IGNORE.md
addyosmani-agent-skills/hooks/sdd-cache-post.sh
addyosmani-agent-skills/hooks/sdd-cache-pre.sh
addyosmani-agent-skills/hooks/sdd-cache-test.sh
addyosmani-agent-skills/hooks/session-start-test.sh
addyosmani-agent-skills/hooks/session-start.sh
addyosmani-agent-skills/hooks/simplify-ignore-test.sh
addyosmani-agent-skills/hooks/simplify-ignore.sh
cursor-plugins/advisor/hooks/capture-response.sh
cursor-plugins/advisor/hooks/hooks.json
cursor-plugins/advisor/hooks/lib.sh
cursor-plugins/advisor/hooks/mark-pending.sh
cursor-plugins/advisor/hooks/record-consult.sh
cursor-plugins/advisor/hooks/stop-hook.sh
cursor-plugins/continual-learning/hooks/continual-learning-stop.ts
cursor-plugins/continual-learning/hooks/hooks.json
cursor-plugins/ralph-loop/hooks/capture-response.sh
cursor-plugins/ralph-loop/hooks/hooks.json
cursor-plugins/ralph-loop/hooks/stop-hook.sh
```

#### 1.hooks 例外 · `SDD-CACHE.md` 与 `SIMPLIFY-IGNORE.md` 单独处置

> **M5 裁定（2026-09-30 · `docs/history/handoff/0930-oracle-M34-DECISION.md` 第 3 节）**：
> 「同意两份 `.md` 分别阅读与处置，不能因目录名 `hooks/` 或 runtime 实现而整类排除。」
> 「本裁定只批准独立处置粒度，**未裁定吸收两份全文**。」

**变更**：这两份从「被本类理由连带排除」改为**单独处置**。
**本节的可迁移点转述自裁定人自己的阅读，不是 scout 的阅读，也不构成吸收裁定。**

| 文件 | 裁定给出的可迁移点（出处：裁定 §3） | 裁定明确的限制 |
|---|---|---|
| `addyosmani-agent-skills/hooks/SDD-CACHE.md` | **证据新鲜性纪律**。该 hook 缓存的是**经 prompt 处理的页面解读**；源站返回 304 **不能证明旧解读满足当前问题** | 「不得把该 hook 的实现或自述直接当已验证机制」 |
| `addyosmani-agent-skills/hooks/SIMPLIFY-IGNORE.md` | **约束与恢复路径的显式记录**。含保护块的范围、理由及恢复限制 | 「隐藏代码、临时改写文件、hook 事件与缓存路径属于下游实现，**不随方法一起硬编码到 TIM**」 |

**scout 不提候选方法。** 裁定 §3 定的流程是「Driver 按已有来源流程比较现有契约，能引用既有原则就引用；
有新方法再提候选并独立评价」。本轮这两份的处置留给 driver 按该流程走，
**不得写成已吸收**。

**scout 未读这两份正文**，因此除上表转述外不对其内容作任何断言。
**三态：UNVERIFIED**（scout 侧未读；阅读结论属裁定人）。

### 1.evals · `evals/` — 84 个 · 初判 **高**

**理由**：84 份 = **fixtures 48（占本类 57.1%，主体）+ cases 25 + plugin 9 + 根级 2**。
`plugin/` 是 **3 组场景**（6 份 grader + 3 份 prompt），构成「该不该开火」的负例评测。
本库没有任何 skill 触发判据的可执行评测。

> **M5 更正（2026-09-30）**：原写「27 个 case 定义 + 4 组 grader」→ **新值 cases 25 + plugin 3 组场景（6 grader + 3 prompt）**，并**补列 fixtures 48（本类主体）**。
> 原值两处错：`cases/` 实为 25 个文件（不是 27）；`plugin/` 实为 3 个场景目录（不是 4），其 grader 共 6 份。
> 另：原理由**完全未提 fixtures**，而 fixtures 占本类 57.1% —— 遗漏的是本类主体。
> 复核方法：`os.walk` 逐目录计数 `cases` / `fixtures` / `plugin` / 根级，四项相加 = 84，与总数闭合。清单本身未变。

```
addyosmani-agent-skills/evals/README.md
addyosmani-agent-skills/evals/cases/api-and-interface-design.json
addyosmani-agent-skills/evals/cases/browser-testing-with-devtools.json
addyosmani-agent-skills/evals/cases/ci-cd-and-automation.json
addyosmani-agent-skills/evals/cases/code-review-and-quality.json
addyosmani-agent-skills/evals/cases/code-simplification.json
addyosmani-agent-skills/evals/cases/constraint-driven-development.json
addyosmani-agent-skills/evals/cases/context-engineering.json
addyosmani-agent-skills/evals/cases/debugging-and-error-recovery.json
addyosmani-agent-skills/evals/cases/deprecation-and-migration.json
addyosmani-agent-skills/evals/cases/documentation-and-adrs.json
addyosmani-agent-skills/evals/cases/doubt-driven-development.json
addyosmani-agent-skills/evals/cases/frontend-ui-engineering.json
addyosmani-agent-skills/evals/cases/git-workflow-and-versioning.json
addyosmani-agent-skills/evals/cases/idea-refine.json
addyosmani-agent-skills/evals/cases/incremental-implementation.json
addyosmani-agent-skills/evals/cases/interview-me.json
addyosmani-agent-skills/evals/cases/observability-and-instrumentation.json
addyosmani-agent-skills/evals/cases/performance-optimization.json
addyosmani-agent-skills/evals/cases/planning-and-task-breakdown.json
addyosmani-agent-skills/evals/cases/security-and-hardening.json
addyosmani-agent-skills/evals/cases/shipping-and-launch.json
addyosmani-agent-skills/evals/cases/source-driven-development.json
addyosmani-agent-skills/evals/cases/spec-driven-development.json
addyosmani-agent-skills/evals/cases/test-driven-development.json
addyosmani-agent-skills/evals/cases/using-agent-skills.json
addyosmani-agent-skills/evals/fixtures/api-and-interface-design/service-brief.md
addyosmani-agent-skills/evals/fixtures/browser-testing-with-devtools/README.md
addyosmani-agent-skills/evals/fixtures/browser-testing-with-devtools/index.html
addyosmani-agent-skills/evals/fixtures/browser-testing-with-devtools/server.js
addyosmani-agent-skills/evals/fixtures/ci-cd-and-automation/package.json
addyosmani-agent-skills/evals/fixtures/ci-cd-and-automation/src/slug.js
addyosmani-agent-skills/evals/fixtures/ci-cd-and-automation/test/slug.test.js
addyosmani-agent-skills/evals/fixtures/code-review-and-quality/user-search.diff
addyosmani-agent-skills/evals/fixtures/code-simplification/config-parser.js
addyosmani-agent-skills/evals/fixtures/code-simplification/config-parser.test.js
addyosmani-agent-skills/evals/fixtures/context-engineering/context-audit.md
addyosmani-agent-skills/evals/fixtures/debugging-and-error-recovery/pagination.js
addyosmani-agent-skills/evals/fixtures/debugging-and-error-recovery/pagination.test.js
addyosmani-agent-skills/evals/fixtures/debugging-and-error-recovery/time-pressure.md
addyosmani-agent-skills/evals/fixtures/deprecation-and-migration/api-inventory.md
addyosmani-agent-skills/evals/fixtures/documentation-and-adrs/decision-context.md
addyosmani-agent-skills/evals/fixtures/doubt-driven-development/migration-plan.md
addyosmani-agent-skills/evals/fixtures/frontend-ui-engineering/Button.tsx
addyosmani-agent-skills/evals/fixtures/frontend-ui-engineering/design-system.md
addyosmani-agent-skills/evals/fixtures/git-workflow-and-versioning/.eval/working-tree.patch
addyosmani-agent-skills/evals/fixtures/git-workflow-and-versioning/app.js
addyosmani-agent-skills/evals/fixtures/git-workflow-and-versioning/app.test.js
addyosmani-agent-skills/evals/fixtures/incremental-implementation-pressure/draft-export.js
addyosmani-agent-skills/evals/fixtures/incremental-implementation-pressure/scenario.md
addyosmani-agent-skills/evals/fixtures/incremental-implementation/reports.js
addyosmani-agent-skills/evals/fixtures/incremental-implementation/reports.test.js
addyosmani-agent-skills/evals/fixtures/incremental-implementation/tasks/plan.md
addyosmani-agent-skills/evals/fixtures/observability-and-instrumentation/operations.md
addyosmani-agent-skills/evals/fixtures/observability-and-instrumentation/payment-retry.js
addyosmani-agent-skills/evals/fixtures/performance-optimization/benchmark.js
addyosmani-agent-skills/evals/fixtures/performance-optimization/products.js
addyosmani-agent-skills/evals/fixtures/planning-and-task-breakdown/notifications-spec.md
addyosmani-agent-skills/evals/fixtures/security-and-hardening/webhook.js
addyosmani-agent-skills/evals/fixtures/security-and-hardening/webhook.test.js
addyosmani-agent-skills/evals/fixtures/shipping-and-launch/authority-pressure.md
addyosmani-agent-skills/evals/fixtures/shipping-and-launch/launch-status.md
addyosmani-agent-skills/evals/fixtures/source-driven-development/framework-task.md
addyosmani-agent-skills/evals/fixtures/spec-driven-development-decomposition/portal-brief.md
addyosmani-agent-skills/evals/fixtures/spec-driven-development/billing-brief.md
addyosmani-agent-skills/evals/fixtures/test-driven-development-ecosystem/README.md
addyosmani-agent-skills/evals/fixtures/test-driven-development-ecosystem/ledger.py
addyosmani-agent-skills/evals/fixtures/test-driven-development-ecosystem/test_ledger.py
addyosmani-agent-skills/evals/fixtures/test-driven-development/BUG.md
addyosmani-agent-skills/evals/fixtures/test-driven-development/README.md
addyosmani-agent-skills/evals/fixtures/test-driven-development/package.json
addyosmani-agent-skills/evals/fixtures/test-driven-development/src/split.js
addyosmani-agent-skills/evals/fixtures/test-driven-development/test/split.test.js
addyosmani-agent-skills/evals/fixtures/using-agent-skills/incident.md
addyosmani-agent-skills/evals/plugin/code-review-fires/graders/off-by-one.md
addyosmani-agent-skills/evals/plugin/code-review-fires/graders/severity-labels.md
addyosmani-agent-skills/evals/plugin/code-review-fires/graders/skill-fired.md
addyosmani-agent-skills/evals/plugin/code-review-fires/prompt.md
addyosmani-agent-skills/evals/plugin/code-review-stays-quiet-on-commit-message/graders/not-fired.md
addyosmani-agent-skills/evals/plugin/code-review-stays-quiet-on-commit-message/prompt.md
addyosmani-agent-skills/evals/plugin/code-review-stays-quiet/graders/not-fired.md
addyosmani-agent-skills/evals/plugin/code-review-stays-quiet/graders/tdd-fired.md
addyosmani-agent-skills/evals/plugin/code-review-stays-quiet/prompt.md
addyosmani-agent-skills/evals/skill-impact.md
```

### 1.docs · `docs/` — 58 个 · 初判 **中**

**理由**：58 份 = **addy 16（9 份 `*-setup.md` harness 安装指南，低 + 7 份其他）+ pstack 17（11 篇 guide `.md` + 6 张配图）+ matt 25（engineering 18 + productivity 7，逐 skill 说明，与本库 `skills/` 重复度未知）**。

> **M5 更正（2026-09-30，自查发现，非裁定列举）**：原写「25 份是 harness 安装指南 / 11 篇 pstack guide / 22 份 matt」→ **新值 9 / 11 / 25**。
> 原值把 addy 全部 16 份都算成安装指南（实为 9 setup + 7 其他），且把 matt 的 25 份写成 22。三项均按 `os.walk` 逐目录重数。清单本身未变。

```
addyosmani-agent-skills/docs/adoption-guide.md
addyosmani-agent-skills/docs/advanced-per-agent-configuration.md
addyosmani-agent-skills/docs/agents.md
addyosmani-agent-skills/docs/antigravity-setup.md
addyosmani-agent-skills/docs/codex-setup.md
addyosmani-agent-skills/docs/commandcode-setup.md
addyosmani-agent-skills/docs/comparison.md
addyosmani-agent-skills/docs/copilot-cli-setup.md
addyosmani-agent-skills/docs/copilot-setup.md
addyosmani-agent-skills/docs/cursor-setup.md
addyosmani-agent-skills/docs/developer-onboarding.md
addyosmani-agent-skills/docs/gemini-cli-setup.md
addyosmani-agent-skills/docs/getting-started.md
addyosmani-agent-skills/docs/opencode-setup.md
addyosmani-agent-skills/docs/skill-anatomy.md
addyosmani-agent-skills/docs/windsurf-setup.md
cursor-plugins/pstack/docs/guide/01-setup.md
cursor-plugins/pstack/docs/guide/02-poteto-mode.md
cursor-plugins/pstack/docs/guide/03-understand.md
cursor-plugins/pstack/docs/guide/04-design.md
cursor-plugins/pstack/docs/guide/05-build-and-clean.md
cursor-plugins/pstack/docs/guide/06-verify-and-ship.md
cursor-plugins/pstack/docs/guide/07-overnight.md
cursor-plugins/pstack/docs/guide/08-principles.md
cursor-plugins/pstack/docs/guide/09-make-it-yours.md
cursor-plugins/pstack/docs/guide/10-recipes-and-pitfalls.md
cursor-plugins/pstack/docs/guide/README.md
cursor-plugins/pstack/docs/guide/images/design.jpg
cursor-plugins/pstack/docs/guide/images/overnight.jpg
cursor-plugins/pstack/docs/guide/images/recipes.jpg
cursor-plugins/pstack/docs/guide/images/router.jpg
cursor-plugins/pstack/docs/guide/images/understanding.jpg
cursor-plugins/pstack/docs/guide/images/verification.jpg
mattpocock-skills/docs/engineering/ask-matt.md
mattpocock-skills/docs/engineering/code-review.md
mattpocock-skills/docs/engineering/codebase-design.md
mattpocock-skills/docs/engineering/diagnosing-bugs.md
mattpocock-skills/docs/engineering/domain-modeling.md
mattpocock-skills/docs/engineering/grill-with-docs.md
mattpocock-skills/docs/engineering/implement.md
mattpocock-skills/docs/engineering/improve-codebase-architecture.md
mattpocock-skills/docs/engineering/prototype.md
mattpocock-skills/docs/engineering/research.md
mattpocock-skills/docs/engineering/resolving-merge-conflicts.md
mattpocock-skills/docs/engineering/setup-matt-pocock-skills.md
mattpocock-skills/docs/engineering/tdd.md
mattpocock-skills/docs/engineering/to-spec.md
mattpocock-skills/docs/engineering/to-tickets.md
mattpocock-skills/docs/engineering/triage.md
mattpocock-skills/docs/engineering/wayfinder.md
mattpocock-skills/docs/engineering/wizard.md
mattpocock-skills/docs/productivity/grill-me.md
mattpocock-skills/docs/productivity/grilling.md
mattpocock-skills/docs/productivity/handoff.md
mattpocock-skills/docs/productivity/teach.md
mattpocock-skills/docs/productivity/to-questionnaire.md
mattpocock-skills/docs/productivity/wait-what.md
mattpocock-skills/docs/productivity/writing-for-agents.md
```

### 1.automations · `automations/` — 5 个 · 初判 **中**

**理由**：5 份是 Benny 自动化的配置样例与 prompt 模板；含 fail-closed 建单等语义。

```
cursor-plugins/pstack/automations/benny/FOR_AGENTS.md
cursor-plugins/pstack/automations/benny/README.md
cursor-plugins/pstack/automations/benny/templates/configuration.example.yaml
cursor-plugins/pstack/automations/benny/templates/reproduce-automation-prompt.md
cursor-plugins/pstack/automations/benny/templates/triage-automation-prompt.md
```

### 1..changeset · `.changeset/` — 13 个 · 初判 **中**

**理由**：13 份是上游变更说明，其中 5 份直接记录了 skill 判据的改动历史（retro-deterministic-checks 等），是「上游改了什么」的一手证据。

```
mattpocock-skills/.changeset/README.md
mattpocock-skills/.changeset/add-implement-spec-skill.md
mattpocock-skills/.changeset/add-pr-skill.md
mattpocock-skills/.changeset/config.json
mattpocock-skills/.changeset/domain-modeling-trigger-context-adr.md
mattpocock-skills/.changeset/fix-yaml-frontmatter-colons.md
mattpocock-skills/.changeset/grilling-add-hr-between-questions.md
mattpocock-skills/.changeset/grilling-remove-em-dashes.md
mattpocock-skills/.changeset/remove-em-dashes-repo-wide.md
mattpocock-skills/.changeset/retro-deterministic-checks.md
mattpocock-skills/.changeset/skill-tool-invocation-terminology.md
mattpocock-skills/.changeset/user-invoked-skill-invocation.md
mattpocock-skills/.changeset/wait-what-context-map.md
```

### 1..agents · `.agents/` — 6 个 · 初判 **中**

**理由**：6 份含 2 份 ADR（架构决策记录），本库有 `documentation-and-adrs` skill 但 ADR 载体格式未见于本库。

```
addyosmani-agent-skills/.agents/plugins/marketplace.json
mattpocock-skills/.agents/adr/0001-explicit-setup-pointer-only-for-hard-dependencies.md
mattpocock-skills/.agents/adr/0002-ship-as-a-claude-code-plugin.md
mattpocock-skills/.agents/install-block.md
mattpocock-skills/.agents/invocation.md
mattpocock-skills/.agents/writing-docs.md
```

### 1..out-of-scope · `.out-of-scope/` — 3 个 · 初判 **中**

**理由**：3 份是上游自己划的「不做什么」，与本库硬边界同形——上游用独立目录表达边界，本库用 `AGENTS.md` 硬边界段。

```
mattpocock-skills/.out-of-scope/mainstream-issue-trackers-only.md
mattpocock-skills/.out-of-scope/question-limits.md
mattpocock-skills/.out-of-scope/setup-skill-verify-mode.md
```

### 1..claude · `.claude/` — 1 个 · 初判 **中**

**理由**：1 份 skills-contributing 规则，是上游对「怎么写 skill」的方法论约束。

```
addyosmani-agent-skills/.claude/rules/skills-contributing.md
```

### 1.根级与配置类（合计 139 个）· 初判见各组

#### `_root:md` — 根级 .md（README/CHANGELOG/AGENTS/CLAUDE/skill 附带参考 .md） · 62 个 · 初判 **中**

**理由**：62 份 = **仓根 `.md` 10（`AGENTS.md` / `CLAUDE.md` / `CONTEXT.md` / `README.md` / `CONTRIBUTING.md` / `CHANGELOG.md` 等，低）+ plugin README/CHANGELOG 23（低）+ skill 目录附带 29（`PHASE-BOUNDARIES` / `DEEPENING` / `ADR-FORMAT` / `GLOSSARY-FORMAT` / `OUT-OF-SCOPE` 等，方法价值高但已在 101 条处置表覆盖范围内）**。

> **M5 更正（2026-09-30，自查发现，非裁定列举）**：原写「19 份 README+CHANGELOG / 43 份 skill 附带」→ **新值 10 + 23 / 29**。
> 原值把 15 份 plugin 目录级 `README.md` 混入了「skill 附带」一类。复核方法：按路径层级分三档（仓根 / plugin 目录 / skill 目录内），三档相加 = 62 闭合。清单本身未变。

```
addyosmani-agent-skills/AGENTS.md
addyosmani-agent-skills/CLAUDE.md
addyosmani-agent-skills/CONTRIBUTING.md
addyosmani-agent-skills/README.md
addyosmani-agent-skills/skills/idea-refine/examples.md
addyosmani-agent-skills/skills/idea-refine/frameworks.md
addyosmani-agent-skills/skills/idea-refine/refinement-criteria.md
cursor-plugins/README.md
cursor-plugins/advisor/CHANGELOG.md
cursor-plugins/advisor/README.md
cursor-plugins/agent-compatibility/CHANGELOG.md
cursor-plugins/agent-compatibility/README.md
cursor-plugins/cli-for-agent/README.md
cursor-plugins/continual-learning/README.md
cursor-plugins/create-plugin/CHANGELOG.md
cursor-plugins/create-plugin/README.md
cursor-plugins/cursor-sdk/README.md
cursor-plugins/cursor-team-kit/README.md
cursor-plugins/docs-canvas/CHANGELOG.md
cursor-plugins/docs-canvas/README.md
cursor-plugins/grok-voice/README.md
cursor-plugins/orchestrate/README.md
cursor-plugins/pr-review-canvas/CHANGELOG.md
cursor-plugins/pr-review-canvas/README.md
cursor-plugins/pstack/README.md
cursor-plugins/ralph-loop/README.md
cursor-plugins/teaching/README.md
cursor-plugins/thermos/CHANGELOG.md
cursor-plugins/thermos/README.md
mattpocock-skills/AGENTS.md
mattpocock-skills/CHANGELOG.md
mattpocock-skills/CLAUDE.md
mattpocock-skills/CONTEXT.md
mattpocock-skills/README.md
mattpocock-skills/skills/deprecated/README.md
mattpocock-skills/skills/engineering/README.md
mattpocock-skills/skills/engineering/ask-matt/PHASE-BOUNDARIES.md
mattpocock-skills/skills/engineering/codebase-design/DEEPENING.md
mattpocock-skills/skills/engineering/codebase-design/DESIGN-IT-TWICE.md
mattpocock-skills/skills/engineering/domain-modeling/ADR-FORMAT.md
mattpocock-skills/skills/engineering/domain-modeling/CONTEXT-FORMAT.md
mattpocock-skills/skills/engineering/improve-codebase-architecture/HTML-REPORT.md
mattpocock-skills/skills/engineering/prototype/LOGIC.md
mattpocock-skills/skills/engineering/prototype/UI.md
mattpocock-skills/skills/engineering/setup-matt-pocock-skills/domain.md
mattpocock-skills/skills/engineering/setup-matt-pocock-skills/issue-tracker-github.md
mattpocock-skills/skills/engineering/setup-matt-pocock-skills/issue-tracker-gitlab.md
mattpocock-skills/skills/engineering/setup-matt-pocock-skills/issue-tracker-local.md
mattpocock-skills/skills/engineering/setup-matt-pocock-skills/triage-labels.md
mattpocock-skills/skills/engineering/tdd/mocking.md
mattpocock-skills/skills/engineering/tdd/tests.md
mattpocock-skills/skills/engineering/triage/AGENT-BRIEF.md
mattpocock-skills/skills/engineering/triage/OUT-OF-SCOPE.md
mattpocock-skills/skills/in-progress/README.md
mattpocock-skills/skills/in-progress/pr/CREDITS.md
mattpocock-skills/skills/misc/README.md
mattpocock-skills/skills/productivity/README.md
mattpocock-skills/skills/productivity/teach/GLOSSARY-FORMAT.md
mattpocock-skills/skills/productivity/teach/LEARNING-RECORD-FORMAT.md
mattpocock-skills/skills/productivity/teach/MISSION-FORMAT.md
mattpocock-skills/skills/productivity/teach/RESOURCES-FORMAT.md
mattpocock-skills/skills/productivity/writing-for-agents/SKILL-MECHANICS.md
```

#### `_root:json` — 根级 json（配置与依赖） · 28 个 · 初判 **低**

**理由**：package.json / plugin.json / marketplace.json 等机械配置。

```
addyosmani-agent-skills/.claude-plugin/marketplace.json
addyosmani-agent-skills/.claude-plugin/plugin.json
addyosmani-agent-skills/.codex-plugin/plugin.json
addyosmani-agent-skills/plugin.json
cursor-plugins/.cursor-plugin/marketplace.json
cursor-plugins/advisor/.cursor-plugin/plugin.json
cursor-plugins/agent-compatibility/.cursor-plugin/plugin.json
cursor-plugins/cli-for-agent/.cursor-plugin/plugin.json
cursor-plugins/continual-learning/.cursor-plugin/plugin.json
cursor-plugins/create-plugin/.cursor-plugin/plugin.json
cursor-plugins/cursor-sdk/.cursor-plugin/plugin.json
cursor-plugins/cursor-team-kit/.cursor-plugin/plugin.json
cursor-plugins/docs-canvas/.cursor-plugin/plugin.json
cursor-plugins/grok-voice/.cursor-plugin/plugin.json
cursor-plugins/orchestrate/.cursor-plugin/plugin.json
cursor-plugins/orchestrate/skills/orchestrate/schemas/plan.schema.json
cursor-plugins/orchestrate/skills/orchestrate/schemas/state.schema.json
cursor-plugins/pr-review-canvas/.cursor-plugin/plugin.json
cursor-plugins/pstack/.cursor-plugin/plugin.json
cursor-plugins/ralph-loop/.cursor-plugin/plugin.json
cursor-plugins/schemas/marketplace.schema.json
cursor-plugins/schemas/plugin.schema.json
cursor-plugins/teaching/.cursor-plugin/plugin.json
cursor-plugins/thermos/.cursor-plugin/plugin.json
mattpocock-skills/.claude-plugin/marketplace.json
mattpocock-skills/.claude-plugin/plugin.json
mattpocock-skills/package-lock.json
mattpocock-skills/package.json
```

#### `_root:yaml` — 根级 yaml/yml · 4 个 · 初判 **低**

**理由**：CI workflow 与 hook 配置。

```
addyosmani-agent-skills/.github/ISSUE_TEMPLATE/skill-gap.yml
addyosmani-agent-skills/.github/workflows/test-plugin-install.yml
cursor-plugins/.github/workflows/validate-plugins.yml
mattpocock-skills/.github/workflows/release.yml
```

#### `_root:noext` — 无扩展名（LICENSE 等） · 17 个 · 初判 **低**

**理由**：法律文本。

```
addyosmani-agent-skills/LICENSE
cursor-plugins/advisor/LICENSE
cursor-plugins/agent-compatibility/LICENSE
cursor-plugins/cli-for-agent/LICENSE
cursor-plugins/continual-learning/LICENSE
cursor-plugins/create-plugin/LICENSE
cursor-plugins/cursor-sdk/LICENSE
cursor-plugins/cursor-team-kit/LICENSE
cursor-plugins/docs-canvas/LICENSE
cursor-plugins/grok-voice/LICENSE
cursor-plugins/orchestrate/LICENSE
cursor-plugins/pr-review-canvas/LICENSE
cursor-plugins/pstack/LICENSE
cursor-plugins/ralph-loop/LICENSE
cursor-plugins/teaching/LICENSE
cursor-plugins/thermos/LICENSE
mattpocock-skills/LICENSE
```

#### `_root:image` — 图片 png/jpg/svg · 14 个 · 初判 **低**

**理由**：文档配图。

```
cursor-plugins/advisor/assets/avatar.png
cursor-plugins/agent-compatibility/assets/avatar.png
cursor-plugins/continual-learning/assets/avatar.png
cursor-plugins/create-plugin/assets/avatar.png
cursor-plugins/cursor-team-kit/assets/avatar.png
cursor-plugins/docs-canvas/assets/avatar.png
cursor-plugins/grok-voice/assets/logo.png
cursor-plugins/grok-voice/assets/logo.svg
cursor-plugins/orchestrate/assets/avatar.png
cursor-plugins/pr-review-canvas/assets/avatar.png
cursor-plugins/pstack/assets/logo.png
cursor-plugins/ralph-loop/assets/avatar.png
cursor-plugins/teaching/assets/avatar.png
cursor-plugins/thermos/assets/logo.png
```

#### `_root:mdc` — mdc 规则文件 · 3 个 · 初判 **中**

**理由**：3 份是 harness 规则片段，形态上与本库原则正文同形。

```
cursor-plugins/create-plugin/rules/plugin-quality-gates.mdc
cursor-plugins/cursor-team-kit/rules/no-inline-imports.mdc
cursor-plugins/cursor-team-kit/rules/typescript-exhaustive-switch.mdc
```

#### `_root:dotfile` — .gitignore/.gitattributes · 6 个 · 初判 **低**

**理由**：仓库记账。

```
addyosmani-agent-skills/.gitattributes
addyosmani-agent-skills/.gitignore
cursor-plugins/.gitignore
cursor-plugins/orchestrate/.gitignore
cursor-plugins/pstack/.gitignore
mattpocock-skills/.gitignore
```

#### `_root:js` — 根级 js · 1 个 · 初判 **低**

**理由**：单文件工具。

```
cursor-plugins/cursor-team-kit/skills/pr-review-canvas/renderer.js
```

#### `_root:cjs` — 根级 cjs · 1 个 · 初判 **低**

**理由**：单文件工具。

```
mattpocock-skills/skills/in-progress/setup-ts-deep-modules/dependency-cruiser.config.cjs
```

#### `_root:css` — 根级 css · 1 个 · 初判 **低**

**理由**：样式。

```
cursor-plugins/cursor-team-kit/skills/pr-review-canvas/styles.css
```

#### `_root:html` — 根级 html · 1 个 · 初判 **低**

**理由**：页面。

```
cursor-plugins/cursor-team-kit/skills/pr-review-canvas/template.html
```

#### `_root:sh` — 根级 sh · 1 个 · 初判 **低**

**理由**：单文件脚本。

```
mattpocock-skills/skills/engineering/wizard/template.sh
```

## 2. 沉默桶之一 · `mattpocock-skills/skills/in-progress/`（Owner 点名）

**为什么它是沉默桶**：`upstreams.lock.yaml` 不含其中任何一个 skill，
因此 `workflow/registry.yaml:upstream_dispositions`（101 条）**连「已拒绝」这一格都没有**。
逐条读正文的「讲什么 + 与本库重叠」见姊妹文件 `UPSTREAM-INVENTORY-0930.md` §5（9/9 已读）。

**该目录下全部 21 个文件**（9 个 `SKILL.md` + 12 个载体）：

> **M5 更正（2026-09-30）**：原写「20 个文件（9 SKILL + 11 载体）」→ **新值 21 个（9 SKILL + 12 载体）**。
> 漏的是 `setup-ts-deep-modules/dependency-cruiser.config.cjs`。
> 复核方法：对 `in-progress/` 递归 `os.walk` 逐文件重数。清单已补齐该文件。

```
mattpocock-skills/skills/in-progress/README.md
mattpocock-skills/skills/in-progress/claude-handoff/SKILL.md
mattpocock-skills/skills/in-progress/claude-handoff/agents/openai.yaml
mattpocock-skills/skills/in-progress/implement-spec/SKILL.md
mattpocock-skills/skills/in-progress/implement-spec/agents/openai.yaml
mattpocock-skills/skills/in-progress/loop-me/SKILL.md
mattpocock-skills/skills/in-progress/loop-me/agents/openai.yaml
mattpocock-skills/skills/in-progress/pr/SKILL.md
mattpocock-skills/skills/in-progress/pr/agents/openai.yaml
mattpocock-skills/skills/in-progress/pr/CREDITS.md
mattpocock-skills/skills/in-progress/retro/SKILL.md
mattpocock-skills/skills/in-progress/retro/agents/openai.yaml
mattpocock-skills/skills/in-progress/setup-ts-deep-modules/SKILL.md
mattpocock-skills/skills/in-progress/setup-ts-deep-modules/agents/openai.yaml
mattpocock-skills/skills/in-progress/setup-ts-deep-modules/dependency-cruiser.config.cjs
mattpocock-skills/skills/in-progress/writing-beats/SKILL.md
mattpocock-skills/skills/in-progress/writing-beats/agents/openai.yaml
mattpocock-skills/skills/in-progress/writing-fragments/SKILL.md
mattpocock-skills/skills/in-progress/writing-fragments/agents/openai.yaml
mattpocock-skills/skills/in-progress/writing-shape/SKILL.md
mattpocock-skills/skills/in-progress/writing-shape/agents/openai.yaml
```

**载体构成**：9 份 `agents/openai.yaml`（模型映射配置）+ `README.md` + `pr/CREDITS.md` + `setup-ts-deep-modules/dependency-cruiser.config.cjs` = 12。
**注意**：这 9 份 `openai.yaml` 同时出现在 §1 的 `agents/` 类里（scout 分类按唯一归属，**每个文件只计一次**）；
本节列出是为说明 in-progress 桶的完整构成，**不是重复计数**。

**初判（整桶）**：**高** —— 9 个 skill 全是工程工作流方法，且 9 个全部不在任何登记结构里。

## 3. 沉默桶之二 · `mattpocock-skills/.changeset/`（Owner 点名）

**为什么它是沉默桶**：`_render-lock.py:52` 只 walk `base/"skills"`，此目录在 `mattpocock-skills/` 根下，从不入枚举。

**全部 13 个文件** · 初判 **中**

**理由**：上游变更说明是「上游改了什么判据」的一手证据。其中 6 份直接记录 skill 判据改动
（`retro-deterministic-checks`、`grilling-add-hr-between-questions`、`grilling-remove-em-dashes`、
`remove-em-dashes-repo-wide`、`user-invoked-skill-invocation`、`skill-tool-invocation-terminology`），
能解释本库**已收** skill 的判据在时间上如何演变 —— 这是只有变更记录才有的信息。

```
mattpocock-skills/.changeset/README.md
mattpocock-skills/.changeset/add-implement-spec-skill.md
mattpocock-skills/.changeset/add-pr-skill.md
mattpocock-skills/.changeset/config.json
mattpocock-skills/.changeset/domain-modeling-trigger-context-adr.md
mattpocock-skills/.changeset/fix-yaml-frontmatter-colons.md
mattpocock-skills/.changeset/grilling-add-hr-between-questions.md
mattpocock-skills/.changeset/grilling-remove-em-dashes.md
mattpocock-skills/.changeset/remove-em-dashes-repo-wide.md
mattpocock-skills/.changeset/retro-deterministic-checks.md
mattpocock-skills/.changeset/skill-tool-invocation-terminology.md
mattpocock-skills/.changeset/user-invoked-skill-invocation.md
mattpocock-skills/.changeset/wait-what-context-map.md
```

**修正 UPRESCAN**：UPRESCAN 记「`.changeset` 2 份」，实测 **13 个文件**
（`README.md` + `config.json` + 11 份具名 changeset）。

## 4. 沉默桶之三 · `addyosmani-agent-skills/evals/`（Owner 点名）

**全部 84 个文件** · 初判 **高**

**理由**：本库没有任何「skill 该不该开火」的可执行评测。
这 84 份里 25 个 case 定义 + 6 份 grader 是这类判据的现成形态，与本库「触发/不触发」类判据直接同形。

**结构分解（scout 实测）**：

| 子目录 | 目录数 | 文件数 |
|---|---|---|
| `cases/` | 25 个 case | 25 |
| `fixtures/` | 25 个 skill 素材目录 | 48 |
| `plugin/` | **3** 个场景 | 9 |
| 根级 | — | 2（`README.md`、`skill-impact.md`）|
| **合计** | | **84** |

**修正姊妹文件 §3.2**：那里写「`plugin/` 4 个场景」与「`fixtures/` 20 个子目录」，
**实测为 3 个场景与 25 个子目录**。此处为准。

**3 个 plugin 场景**（grader 文件名自述期望行为，scout 未读 grader 正文）：

| 场景 | prompt | graders | 场景名自述的期望 |
|---|---|---|---|
| `code-review-fires` | `prompt.md` | `off-by-one.md`、`severity-labels.md`、`skill-fired.md` | 该开火时开火 |
| `code-review-stays-quiet` | `prompt.md` | `not-fired.md`、`tdd-fired.md` | 不该开火时不开火 |
| `code-review-stays-quiet-on-commit-message` | `prompt.md` | `not-fired.md` | 特定输入下不开火 |

```
addyosmani-agent-skills/evals/README.md
addyosmani-agent-skills/evals/cases/api-and-interface-design.json
addyosmani-agent-skills/evals/cases/browser-testing-with-devtools.json
addyosmani-agent-skills/evals/cases/ci-cd-and-automation.json
addyosmani-agent-skills/evals/cases/code-review-and-quality.json
addyosmani-agent-skills/evals/cases/code-simplification.json
addyosmani-agent-skills/evals/cases/constraint-driven-development.json
addyosmani-agent-skills/evals/cases/context-engineering.json
addyosmani-agent-skills/evals/cases/debugging-and-error-recovery.json
addyosmani-agent-skills/evals/cases/deprecation-and-migration.json
addyosmani-agent-skills/evals/cases/documentation-and-adrs.json
addyosmani-agent-skills/evals/cases/doubt-driven-development.json
addyosmani-agent-skills/evals/cases/frontend-ui-engineering.json
addyosmani-agent-skills/evals/cases/git-workflow-and-versioning.json
addyosmani-agent-skills/evals/cases/idea-refine.json
addyosmani-agent-skills/evals/cases/incremental-implementation.json
addyosmani-agent-skills/evals/cases/interview-me.json
addyosmani-agent-skills/evals/cases/observability-and-instrumentation.json
addyosmani-agent-skills/evals/cases/performance-optimization.json
addyosmani-agent-skills/evals/cases/planning-and-task-breakdown.json
addyosmani-agent-skills/evals/cases/security-and-hardening.json
addyosmani-agent-skills/evals/cases/shipping-and-launch.json
addyosmani-agent-skills/evals/cases/source-driven-development.json
addyosmani-agent-skills/evals/cases/spec-driven-development.json
addyosmani-agent-skills/evals/cases/test-driven-development.json
addyosmani-agent-skills/evals/cases/using-agent-skills.json
addyosmani-agent-skills/evals/fixtures/api-and-interface-design/service-brief.md
addyosmani-agent-skills/evals/fixtures/browser-testing-with-devtools/README.md
addyosmani-agent-skills/evals/fixtures/browser-testing-with-devtools/index.html
addyosmani-agent-skills/evals/fixtures/browser-testing-with-devtools/server.js
addyosmani-agent-skills/evals/fixtures/ci-cd-and-automation/package.json
addyosmani-agent-skills/evals/fixtures/ci-cd-and-automation/src/slug.js
addyosmani-agent-skills/evals/fixtures/ci-cd-and-automation/test/slug.test.js
addyosmani-agent-skills/evals/fixtures/code-review-and-quality/user-search.diff
addyosmani-agent-skills/evals/fixtures/code-simplification/config-parser.js
addyosmani-agent-skills/evals/fixtures/code-simplification/config-parser.test.js
addyosmani-agent-skills/evals/fixtures/context-engineering/context-audit.md
addyosmani-agent-skills/evals/fixtures/debugging-and-error-recovery/pagination.js
addyosmani-agent-skills/evals/fixtures/debugging-and-error-recovery/pagination.test.js
addyosmani-agent-skills/evals/fixtures/debugging-and-error-recovery/time-pressure.md
addyosmani-agent-skills/evals/fixtures/deprecation-and-migration/api-inventory.md
addyosmani-agent-skills/evals/fixtures/documentation-and-adrs/decision-context.md
addyosmani-agent-skills/evals/fixtures/doubt-driven-development/migration-plan.md
addyosmani-agent-skills/evals/fixtures/frontend-ui-engineering/Button.tsx
addyosmani-agent-skills/evals/fixtures/frontend-ui-engineering/design-system.md
addyosmani-agent-skills/evals/fixtures/git-workflow-and-versioning/.eval/working-tree.patch
addyosmani-agent-skills/evals/fixtures/git-workflow-and-versioning/app.js
addyosmani-agent-skills/evals/fixtures/git-workflow-and-versioning/app.test.js
addyosmani-agent-skills/evals/fixtures/incremental-implementation-pressure/draft-export.js
addyosmani-agent-skills/evals/fixtures/incremental-implementation-pressure/scenario.md
addyosmani-agent-skills/evals/fixtures/incremental-implementation/reports.js
addyosmani-agent-skills/evals/fixtures/incremental-implementation/reports.test.js
addyosmani-agent-skills/evals/fixtures/incremental-implementation/tasks/plan.md
addyosmani-agent-skills/evals/fixtures/observability-and-instrumentation/operations.md
addyosmani-agent-skills/evals/fixtures/observability-and-instrumentation/payment-retry.js
addyosmani-agent-skills/evals/fixtures/performance-optimization/benchmark.js
addyosmani-agent-skills/evals/fixtures/performance-optimization/products.js
addyosmani-agent-skills/evals/fixtures/planning-and-task-breakdown/notifications-spec.md
addyosmani-agent-skills/evals/fixtures/security-and-hardening/webhook.js
addyosmani-agent-skills/evals/fixtures/security-and-hardening/webhook.test.js
addyosmani-agent-skills/evals/fixtures/shipping-and-launch/authority-pressure.md
addyosmani-agent-skills/evals/fixtures/shipping-and-launch/launch-status.md
addyosmani-agent-skills/evals/fixtures/source-driven-development/framework-task.md
addyosmani-agent-skills/evals/fixtures/spec-driven-development-decomposition/portal-brief.md
addyosmani-agent-skills/evals/fixtures/spec-driven-development/billing-brief.md
addyosmani-agent-skills/evals/fixtures/test-driven-development-ecosystem/README.md
addyosmani-agent-skills/evals/fixtures/test-driven-development-ecosystem/ledger.py
addyosmani-agent-skills/evals/fixtures/test-driven-development-ecosystem/test_ledger.py
addyosmani-agent-skills/evals/fixtures/test-driven-development/BUG.md
addyosmani-agent-skills/evals/fixtures/test-driven-development/README.md
addyosmani-agent-skills/evals/fixtures/test-driven-development/package.json
addyosmani-agent-skills/evals/fixtures/test-driven-development/src/split.js
addyosmani-agent-skills/evals/fixtures/test-driven-development/test/split.test.js
addyosmani-agent-skills/evals/fixtures/using-agent-skills/incident.md
addyosmani-agent-skills/evals/plugin/code-review-fires/graders/off-by-one.md
addyosmani-agent-skills/evals/plugin/code-review-fires/graders/severity-labels.md
addyosmani-agent-skills/evals/plugin/code-review-fires/graders/skill-fired.md
addyosmani-agent-skills/evals/plugin/code-review-fires/prompt.md
addyosmani-agent-skills/evals/plugin/code-review-stays-quiet-on-commit-message/graders/not-fired.md
addyosmani-agent-skills/evals/plugin/code-review-stays-quiet-on-commit-message/prompt.md
addyosmani-agent-skills/evals/plugin/code-review-stays-quiet/graders/not-fired.md
addyosmani-agent-skills/evals/plugin/code-review-stays-quiet/graders/tdd-fired.md
addyosmani-agent-skills/evals/plugin/code-review-stays-quiet/prompt.md
addyosmani-agent-skills/evals/skill-impact.md
```

## 5. `cursor-plugins/third_party/` · 476 个 · 初判 **低**

scout 实测：该目录下实有 **79 个包，482 个文件**。

**口径说明**：482 与本文件标题的 476 差 6，原因是那 6 个是 `SKILL.md` —— 
它们已计入姊妹文件 §4 的「58 个不在锁里的 `SKILL.md`」，不进「非 SKILL.md 载体」这 476。

### 5.1 三种形态（实测，79 包全覆盖）

| 形态 | 包数 | 文件数 | 构成 |
|---|---|---|---|
| **纯骨架** | 73 | **438** | `.cursor-plugin/plugin.json` + `CHANGELOG.md` + `LICENSE` + `README.md` + `assets/logo.png`(或 `.svg`) + `mcp.json` |
| **带 SKILL.md** | 5 | **38** | 骨架 + `skills/*/SKILL.md`（其中 1 份带 `references/pricing.md`） |
| **带 rules** | 1 | 7 | 骨架 + `rules/shopify.mdc` |
| **合计** | **79** | **482** | 其中 `SKILL.md` **6** 个、`references/` **1** 个 |

> **M5 更正（2026-09-30）**：本表原写「带 SKILL.md = 37」→ **新值 38**。
> 原因是 `x` 包实际 9 个文件而非 8 个。复核：73×6 + 38 + 7 = 482，与逐包重数一致；总量 **482 不变**。

### 5.1b 两种筛选口径与各自余量

> **M5 裁定第 2 节**：「**604 和 642 是两种筛选策略的剩余文件数，不是已裁定的真实待判规模。**」
> 「不得写『44% 的注意力放在 2 个正文文件上』：文件数不能证明注意力分配，『2 个』也依赖方法价值判据；
> 即使存在两份特定正文，也不能以数量替代逐项方法判断。」

| 口径 | 算式 | 余量 | 性质 |
|---|---|---|---|
| 全量非 `SKILL.md` 载体 | 1239 − 159 | **1080** | 完整清单，本文件已逐条列出 |
| 口径 A：排除 `third_party` 全部非 SKILL 文件 | 1080 − 476 | **604** | 筛选后的剩余文件数 |
| 口径 B：仅排除 73 个纯骨架包的 438 个文件 | 1080 − 438 | **642** | 筛选后的剩余文件数 |
| 参照：`third_party` 在 1080 中的文件数占比 | 476 / 1080 | **≈ 44.1%** | **文件数占比**，不是注意力分配 |

**604 与 642 是两种筛选策略各自的结果，本台账不裁定该用哪一种，也不把其中任何一个称为「真实待判规模」。**
全量清单 1080 条全部保留；阅读／处置队列可以由 driver / adversary 另排优先级。

**s-evals 84 的构成**（见 §4）：fixtures 48 + cases 25 + plugin 9 + 根级 2 = 84。

**「本节所列 604 / 642 不裁定」**——它们是上表的算式结果，不是待判规模的裁定。

### 5.2 5 个带 SKILL.md 的包

| 包 | 文件数 | `SKILL.md` | 额外 |
|---|---|---|---|
| `google-docs` | 7 | 1（120 行） | — |
| `google-sheets` | 7 | 1（87 行） | — |
| `google-slides` | 7 | 1（125 行） | — |
| `x-money` | 7 | 1（`x-money-guide` 173 行） | — |
| `x` | **9** | 2（`x-api-mcp-guide` 357 行、`x-chat` 185 行） | `x-api-mcp-guide/references/pricing.md` |

> **M5 更正（2026-09-30）**：原写 `x` 包「8」个文件 → **新值 9**。
> 复核方法：`os.walk` 逐文件重数。5 个带 `SKILL.md` 的包合计 37 → **38**，与 §5.1 表格的「带 SKILL.md = 37」同步更正为 38。

唯一带 rules 的包：`shopify-store`（7 个文件，**0** 个 `SKILL.md`，含 `rules/shopify.mdc`）—— 
这是 79 个包里**唯一**的 harness 规则文件。

**这 73 个纯骨架包里**未识别到方法正文**。**scout 未逐包读正文，这是证据限定表述，
**不等于「已证明其中不含可迁移方法」**。

**它们的 73 份 `README.md` 内容两两不同**（scout 实测：73 份 README 的 sha256 前 12 位互不相同，72 种不同字节长度）。
**信息各不相同 ≠ 含可迁移方法**：「是否有可迁移方法」与「信息是否相同」是两个不同问题，
前者需要方法价值判据，scout 本轮不判。

### 5.3 建议：整体排除，作为一个决策单元另议（建议，不是裁决）

> **M5 更正（2026-09-30）**：原「理由一：分母虚高。476 里有 438 个（92%）……会高估 **4.5 倍**」——
> 按裁定第 2 节「**不要求为 4.5 倍补事后理由**」，**该数字已删除，不另造推导**。
> 原「真正有方法正文的只有 5 个包、6 个 skill」中的「有方法正文」改为「**未识别到**方法正文」（证据限定表述）。

**理由一（中性陈述，不再推论）：** 476 个 `third_party` 非 `SKILL.md` 文件中，438 个来自 73 个纯骨架包；
本轮对这 438 个**未识别到方法正文**。两种筛选口径与各自余量见 §5.1b。
**本台账不就这 476 个应否进入处置队列表态。**

**理由二：这是上游作者的显式选择，不是枚举缺陷。**
`scripts/_render-lock.py:27-28` 的 `SKIP_DIRS` 第 8 位是 `"third_party"`。
这与 `in-progress` / `references` **性质不同**：那两个是**漏了**，这个是**有意排除**。
处置一个「有意排除」的东西要先推翻上游作者的判断，代价应高于收益。

**理由三：域不同。** 79 个包全部绑定具体外部 SaaS / 平台 API。
本库 `AGENTS.md` 开篇定义本库是「**一套与工具无关的工程工作流**」。
`mcp.json` 与 API 端点清单的寿命受制于该 SaaS 的 API 稳定性，不受本库控制。

**反方事实（供 Owner 权衡，scout 不作推荐）**：

- 6 个 `SKILL.md` 确实有正文体量：`third_party/x/skills/x-api-mcp-guide/SKILL.md` 达 **357 行**，
  超过本库任一 skill 正文。若将来本库扩到「非工程工作流」域，这 476 个是唯一已到手的素材。
  **scout 不预判这个域会不会扩。**
- `shopify-store/rules/shopify.mdc` 是唯一 `.mdc` 规则文件，形态上与本库原则正文同类。
  **单点，不构成整体保留的理由。**

### 5.4 逐包实测计数（79 包全覆盖，无省略）

| # | 包 | 文件数 | 形态 | `SKILL.md` |
|---|---|---|---|---|
| 1 | `ahrefs` | 6 | 纯骨架 | 0 |
| 2 | `amplemarket` | 6 | 纯骨架 | 0 |
| 3 | `ashby` | 6 | 纯骨架 | 0 |
| 4 | `attio` | 6 | 纯骨架 | 0 |
| 5 | `beehiiv` | 6 | 纯骨架 | 0 |
| 6 | `brevo` | 6 | 纯骨架 | 0 |
| 7 | `brex` | 6 | 纯骨架 | 0 |
| 8 | `buffer` | 6 | 纯骨架 | 0 |
| 9 | `calendly` | 6 | 纯骨架 | 0 |
| 10 | `circleback` | 6 | 纯骨架 | 0 |
| 11 | `clay` | 6 | 纯骨架 | 0 |
| 12 | `coda` | 6 | 纯骨架 | 0 |
| 13 | `coinbase` | 6 | 纯骨架 | 0 |
| 14 | `craft` | 6 | 纯骨架 | 0 |
| 15 | `customer-io` | 6 | 纯骨架 | 0 |
| 16 | `daloopa` | 6 | 纯骨架 | 0 |
| 17 | `docusign` | 6 | 纯骨架 | 0 |
| 18 | `etoro-trading` | 6 | 纯骨架 | 0 |
| 19 | `excalidraw` | 6 | 纯骨架 | 0 |
| 20 | `fathom` | 6 | 纯骨架 | 0 |
| 21 | `finance` | 6 | 纯骨架 | 0 |
| 22 | `fireflies` | 6 | 纯骨架 | 0 |
| 23 | `gamma` | 6 | 纯骨架 | 0 |
| 24 | `github` | 6 | 纯骨架 | 0 |
| 25 | `gmail` | 6 | 纯骨架 | 0 |
| 26 | `godaddy` | 6 | 纯骨架 | 0 |
| 27 | `gong` | 6 | 纯骨架 | 0 |
| 28 | `google-calendar` | 6 | 纯骨架 | 0 |
| 29 | `google-cloud-bigquery` | 6 | 纯骨架 | 0 |
| 30 | `google-docs` | 7 | 带 SKILL.md | 1 |
| 31 | `google-drive` | 6 | 纯骨架 | 0 |
| 32 | `google-sheets` | 7 | 带 SKILL.md | 1 |
| 33 | `google-slides` | 7 | 带 SKILL.md | 1 |
| 34 | `guru` | 6 | 纯骨架 | 0 |
| 35 | `hubspot` | 6 | 纯骨架 | 0 |
| 36 | `hunter` | 6 | 纯骨架 | 0 |
| 37 | `interactive-brokers` | 6 | 纯骨架 | 0 |
| 38 | `intercom` | 6 | 纯骨架 | 0 |
| 39 | `jotform` | 6 | 纯骨架 | 0 |
| 40 | `juicebox` | 6 | 纯骨架 | 0 |
| 41 | `klaviyo` | 6 | 纯骨架 | 0 |
| 42 | `mailerlite` | 6 | 纯骨架 | 0 |
| 43 | `meltwater` | 6 | 纯骨架 | 0 |
| 44 | `mem` | 6 | 纯骨架 | 0 |
| 45 | `mercury` | 6 | 纯骨架 | 0 |
| 46 | `navan` | 6 | 纯骨架 | 0 |
| 47 | `onedrive` | 6 | 纯骨架 | 0 |
| 48 | `otter` | 6 | 纯骨架 | 0 |
| 49 | `outlook` | 6 | 纯骨架 | 0 |
| 50 | `outlook-calendar` | 6 | 纯骨架 | 0 |
| 51 | `outreach` | 6 | 纯骨架 | 0 |
| 52 | `plaud` | 6 | 纯骨架 | 0 |
| 53 | `playwright` | 6 | 纯骨架 | 0 |
| 54 | `posthog-mcp` | 6 | 纯骨架 | 0 |
| 55 | `profound` | 6 | 纯骨架 | 0 |
| 56 | `readwise` | 6 | 纯骨架 | 0 |
| 57 | `robinhood` | 6 | 纯骨架 | 0 |
| 58 | `salesforce` | 6 | 纯骨架 | 0 |
| 59 | `semrush` | 6 | 纯骨架 | 0 |
| 60 | `sharepoint` | 6 | 纯骨架 | 0 |
| 61 | `shopify-store` | 7 | 带 rules | 0 |
| 62 | `similarweb` | 6 | 纯骨架 | 0 |
| 63 | `smartsheet` | 6 | 纯骨架 | 0 |
| 64 | `sp-global` | 6 | 纯骨架 | 0 |
| 65 | `statsig` | 6 | 纯骨架 | 0 |
| 66 | `teams` | 6 | 纯骨架 | 0 |
| 67 | `tinyfish` | 6 | 纯骨架 | 0 |
| 68 | `todoist` | 6 | 纯骨架 | 0 |
| 69 | `trello` | 6 | 纯骨架 | 0 |
| 70 | `typeform` | 6 | 纯骨架 | 0 |
| 71 | `upwork` | 6 | 纯骨架 | 0 |
| 72 | `webull` | 6 | 纯骨架 | 0 |
| 73 | `workable` | 6 | 纯骨架 | 0 |
| 74 | `wrike` | 6 | 纯骨架 | 0 |
| 75 | `x` | 9 | 带 SKILL.md | 2 |
| 76 | `x-ads` | 6 | 纯骨架 | 0 |
| 77 | `x-money` | 7 | 带 SKILL.md | 1 |
| 78 | `xero` | 6 | 纯骨架 | 0 |
| 79 | `zoom` | 6 | 纯骨架 | 0 |
| | **合计 79 包** | **482** | | **6** |

### 5.5 全部 476 个非 SKILL.md 路径

```
cursor-plugins/third_party/ahrefs/.cursor-plugin/plugin.json
cursor-plugins/third_party/ahrefs/CHANGELOG.md
cursor-plugins/third_party/ahrefs/LICENSE
cursor-plugins/third_party/ahrefs/README.md
cursor-plugins/third_party/ahrefs/assets/logo.png
cursor-plugins/third_party/ahrefs/mcp.json
cursor-plugins/third_party/amplemarket/.cursor-plugin/plugin.json
cursor-plugins/third_party/amplemarket/CHANGELOG.md
cursor-plugins/third_party/amplemarket/LICENSE
cursor-plugins/third_party/amplemarket/README.md
cursor-plugins/third_party/amplemarket/assets/logo.png
cursor-plugins/third_party/amplemarket/mcp.json
cursor-plugins/third_party/ashby/.cursor-plugin/plugin.json
cursor-plugins/third_party/ashby/CHANGELOG.md
cursor-plugins/third_party/ashby/LICENSE
cursor-plugins/third_party/ashby/README.md
cursor-plugins/third_party/ashby/assets/logo.png
cursor-plugins/third_party/ashby/mcp.json
cursor-plugins/third_party/attio/.cursor-plugin/plugin.json
cursor-plugins/third_party/attio/CHANGELOG.md
cursor-plugins/third_party/attio/LICENSE
cursor-plugins/third_party/attio/README.md
cursor-plugins/third_party/attio/assets/logo.png
cursor-plugins/third_party/attio/mcp.json
cursor-plugins/third_party/beehiiv/.cursor-plugin/plugin.json
cursor-plugins/third_party/beehiiv/CHANGELOG.md
cursor-plugins/third_party/beehiiv/LICENSE
cursor-plugins/third_party/beehiiv/README.md
cursor-plugins/third_party/beehiiv/assets/logo.png
cursor-plugins/third_party/beehiiv/mcp.json
cursor-plugins/third_party/brevo/.cursor-plugin/plugin.json
cursor-plugins/third_party/brevo/CHANGELOG.md
cursor-plugins/third_party/brevo/LICENSE
cursor-plugins/third_party/brevo/README.md
cursor-plugins/third_party/brevo/assets/logo.png
cursor-plugins/third_party/brevo/mcp.json
cursor-plugins/third_party/brex/.cursor-plugin/plugin.json
cursor-plugins/third_party/brex/CHANGELOG.md
cursor-plugins/third_party/brex/LICENSE
cursor-plugins/third_party/brex/README.md
cursor-plugins/third_party/brex/assets/logo.png
cursor-plugins/third_party/brex/mcp.json
cursor-plugins/third_party/buffer/.cursor-plugin/plugin.json
cursor-plugins/third_party/buffer/CHANGELOG.md
cursor-plugins/third_party/buffer/LICENSE
cursor-plugins/third_party/buffer/README.md
cursor-plugins/third_party/buffer/assets/logo.png
cursor-plugins/third_party/buffer/mcp.json
cursor-plugins/third_party/calendly/.cursor-plugin/plugin.json
cursor-plugins/third_party/calendly/CHANGELOG.md
cursor-plugins/third_party/calendly/LICENSE
cursor-plugins/third_party/calendly/README.md
cursor-plugins/third_party/calendly/assets/logo.png
cursor-plugins/third_party/calendly/mcp.json
cursor-plugins/third_party/circleback/.cursor-plugin/plugin.json
cursor-plugins/third_party/circleback/CHANGELOG.md
cursor-plugins/third_party/circleback/LICENSE
cursor-plugins/third_party/circleback/README.md
cursor-plugins/third_party/circleback/assets/logo.png
cursor-plugins/third_party/circleback/mcp.json
cursor-plugins/third_party/clay/.cursor-plugin/plugin.json
cursor-plugins/third_party/clay/CHANGELOG.md
cursor-plugins/third_party/clay/LICENSE
cursor-plugins/third_party/clay/README.md
cursor-plugins/third_party/clay/assets/logo.png
cursor-plugins/third_party/clay/mcp.json
cursor-plugins/third_party/coda/.cursor-plugin/plugin.json
cursor-plugins/third_party/coda/CHANGELOG.md
cursor-plugins/third_party/coda/LICENSE
cursor-plugins/third_party/coda/README.md
cursor-plugins/third_party/coda/assets/logo.png
cursor-plugins/third_party/coda/mcp.json
cursor-plugins/third_party/coinbase/.cursor-plugin/plugin.json
cursor-plugins/third_party/coinbase/CHANGELOG.md
cursor-plugins/third_party/coinbase/LICENSE
cursor-plugins/third_party/coinbase/README.md
cursor-plugins/third_party/coinbase/assets/logo.png
cursor-plugins/third_party/coinbase/mcp.json
cursor-plugins/third_party/craft/.cursor-plugin/plugin.json
cursor-plugins/third_party/craft/CHANGELOG.md
cursor-plugins/third_party/craft/LICENSE
cursor-plugins/third_party/craft/README.md
cursor-plugins/third_party/craft/assets/logo.png
cursor-plugins/third_party/craft/mcp.json
cursor-plugins/third_party/customer-io/.cursor-plugin/plugin.json
cursor-plugins/third_party/customer-io/CHANGELOG.md
cursor-plugins/third_party/customer-io/LICENSE
cursor-plugins/third_party/customer-io/README.md
cursor-plugins/third_party/customer-io/assets/logo.png
cursor-plugins/third_party/customer-io/mcp.json
cursor-plugins/third_party/daloopa/.cursor-plugin/plugin.json
cursor-plugins/third_party/daloopa/CHANGELOG.md
cursor-plugins/third_party/daloopa/LICENSE
cursor-plugins/third_party/daloopa/README.md
cursor-plugins/third_party/daloopa/assets/logo.png
cursor-plugins/third_party/daloopa/mcp.json
cursor-plugins/third_party/docusign/.cursor-plugin/plugin.json
cursor-plugins/third_party/docusign/CHANGELOG.md
cursor-plugins/third_party/docusign/LICENSE
cursor-plugins/third_party/docusign/README.md
cursor-plugins/third_party/docusign/assets/logo.png
cursor-plugins/third_party/docusign/mcp.json
cursor-plugins/third_party/etoro-trading/.cursor-plugin/plugin.json
cursor-plugins/third_party/etoro-trading/CHANGELOG.md
cursor-plugins/third_party/etoro-trading/LICENSE
cursor-plugins/third_party/etoro-trading/README.md
cursor-plugins/third_party/etoro-trading/assets/logo.png
cursor-plugins/third_party/etoro-trading/mcp.json
cursor-plugins/third_party/excalidraw/.cursor-plugin/plugin.json
cursor-plugins/third_party/excalidraw/CHANGELOG.md
cursor-plugins/third_party/excalidraw/LICENSE
cursor-plugins/third_party/excalidraw/README.md
cursor-plugins/third_party/excalidraw/assets/logo.png
cursor-plugins/third_party/excalidraw/mcp.json
cursor-plugins/third_party/fathom/.cursor-plugin/plugin.json
cursor-plugins/third_party/fathom/CHANGELOG.md
cursor-plugins/third_party/fathom/LICENSE
cursor-plugins/third_party/fathom/README.md
cursor-plugins/third_party/fathom/assets/logo.png
cursor-plugins/third_party/fathom/mcp.json
cursor-plugins/third_party/finance/.cursor-plugin/plugin.json
cursor-plugins/third_party/finance/CHANGELOG.md
cursor-plugins/third_party/finance/LICENSE
cursor-plugins/third_party/finance/README.md
cursor-plugins/third_party/finance/assets/logo.svg
cursor-plugins/third_party/finance/mcp.json
cursor-plugins/third_party/fireflies/.cursor-plugin/plugin.json
cursor-plugins/third_party/fireflies/CHANGELOG.md
cursor-plugins/third_party/fireflies/LICENSE
cursor-plugins/third_party/fireflies/README.md
cursor-plugins/third_party/fireflies/assets/logo.png
cursor-plugins/third_party/fireflies/mcp.json
cursor-plugins/third_party/gamma/.cursor-plugin/plugin.json
cursor-plugins/third_party/gamma/CHANGELOG.md
cursor-plugins/third_party/gamma/LICENSE
cursor-plugins/third_party/gamma/README.md
cursor-plugins/third_party/gamma/assets/logo.png
cursor-plugins/third_party/gamma/mcp.json
cursor-plugins/third_party/github/.cursor-plugin/plugin.json
cursor-plugins/third_party/github/CHANGELOG.md
cursor-plugins/third_party/github/LICENSE
cursor-plugins/third_party/github/README.md
cursor-plugins/third_party/github/assets/logo.svg
cursor-plugins/third_party/github/mcp.json
cursor-plugins/third_party/gmail/.cursor-plugin/plugin.json
cursor-plugins/third_party/gmail/CHANGELOG.md
cursor-plugins/third_party/gmail/LICENSE
cursor-plugins/third_party/gmail/README.md
cursor-plugins/third_party/gmail/assets/logo.svg
cursor-plugins/third_party/gmail/mcp.json
cursor-plugins/third_party/godaddy/.cursor-plugin/plugin.json
cursor-plugins/third_party/godaddy/CHANGELOG.md
cursor-plugins/third_party/godaddy/LICENSE
cursor-plugins/third_party/godaddy/README.md
cursor-plugins/third_party/godaddy/assets/logo.png
cursor-plugins/third_party/godaddy/mcp.json
cursor-plugins/third_party/gong/.cursor-plugin/plugin.json
cursor-plugins/third_party/gong/CHANGELOG.md
cursor-plugins/third_party/gong/LICENSE
cursor-plugins/third_party/gong/README.md
cursor-plugins/third_party/gong/assets/logo.png
cursor-plugins/third_party/gong/mcp.json
cursor-plugins/third_party/google-calendar/.cursor-plugin/plugin.json
cursor-plugins/third_party/google-calendar/CHANGELOG.md
cursor-plugins/third_party/google-calendar/LICENSE
cursor-plugins/third_party/google-calendar/README.md
cursor-plugins/third_party/google-calendar/assets/logo.svg
cursor-plugins/third_party/google-calendar/mcp.json
cursor-plugins/third_party/google-cloud-bigquery/.cursor-plugin/plugin.json
cursor-plugins/third_party/google-cloud-bigquery/CHANGELOG.md
cursor-plugins/third_party/google-cloud-bigquery/LICENSE
cursor-plugins/third_party/google-cloud-bigquery/README.md
cursor-plugins/third_party/google-cloud-bigquery/assets/logo.png
cursor-plugins/third_party/google-cloud-bigquery/mcp.json
cursor-plugins/third_party/google-docs/.cursor-plugin/plugin.json
cursor-plugins/third_party/google-docs/CHANGELOG.md
cursor-plugins/third_party/google-docs/LICENSE
cursor-plugins/third_party/google-docs/README.md
cursor-plugins/third_party/google-docs/assets/logo.svg
cursor-plugins/third_party/google-docs/mcp.json
cursor-plugins/third_party/google-drive/.cursor-plugin/plugin.json
cursor-plugins/third_party/google-drive/CHANGELOG.md
cursor-plugins/third_party/google-drive/LICENSE
cursor-plugins/third_party/google-drive/README.md
cursor-plugins/third_party/google-drive/assets/logo.svg
cursor-plugins/third_party/google-drive/mcp.json
cursor-plugins/third_party/google-sheets/.cursor-plugin/plugin.json
cursor-plugins/third_party/google-sheets/CHANGELOG.md
cursor-plugins/third_party/google-sheets/LICENSE
cursor-plugins/third_party/google-sheets/README.md
cursor-plugins/third_party/google-sheets/assets/logo.svg
cursor-plugins/third_party/google-sheets/mcp.json
cursor-plugins/third_party/google-slides/.cursor-plugin/plugin.json
cursor-plugins/third_party/google-slides/CHANGELOG.md
cursor-plugins/third_party/google-slides/LICENSE
cursor-plugins/third_party/google-slides/README.md
cursor-plugins/third_party/google-slides/assets/logo.svg
cursor-plugins/third_party/google-slides/mcp.json
cursor-plugins/third_party/guru/.cursor-plugin/plugin.json
cursor-plugins/third_party/guru/CHANGELOG.md
cursor-plugins/third_party/guru/LICENSE
cursor-plugins/third_party/guru/README.md
cursor-plugins/third_party/guru/assets/logo.png
cursor-plugins/third_party/guru/mcp.json
cursor-plugins/third_party/hubspot/.cursor-plugin/plugin.json
cursor-plugins/third_party/hubspot/CHANGELOG.md
cursor-plugins/third_party/hubspot/LICENSE
cursor-plugins/third_party/hubspot/README.md
cursor-plugins/third_party/hubspot/assets/logo.png
cursor-plugins/third_party/hubspot/mcp.json
cursor-plugins/third_party/hunter/.cursor-plugin/plugin.json
cursor-plugins/third_party/hunter/CHANGELOG.md
cursor-plugins/third_party/hunter/LICENSE
cursor-plugins/third_party/hunter/README.md
cursor-plugins/third_party/hunter/assets/logo.png
cursor-plugins/third_party/hunter/mcp.json
cursor-plugins/third_party/interactive-brokers/.cursor-plugin/plugin.json
cursor-plugins/third_party/interactive-brokers/CHANGELOG.md
cursor-plugins/third_party/interactive-brokers/LICENSE
cursor-plugins/third_party/interactive-brokers/README.md
cursor-plugins/third_party/interactive-brokers/assets/logo.png
cursor-plugins/third_party/interactive-brokers/mcp.json
cursor-plugins/third_party/intercom/.cursor-plugin/plugin.json
cursor-plugins/third_party/intercom/CHANGELOG.md
cursor-plugins/third_party/intercom/LICENSE
cursor-plugins/third_party/intercom/README.md
cursor-plugins/third_party/intercom/assets/logo.svg
cursor-plugins/third_party/intercom/mcp.json
cursor-plugins/third_party/jotform/.cursor-plugin/plugin.json
cursor-plugins/third_party/jotform/CHANGELOG.md
cursor-plugins/third_party/jotform/LICENSE
cursor-plugins/third_party/jotform/README.md
cursor-plugins/third_party/jotform/assets/logo.png
cursor-plugins/third_party/jotform/mcp.json
cursor-plugins/third_party/juicebox/.cursor-plugin/plugin.json
cursor-plugins/third_party/juicebox/CHANGELOG.md
cursor-plugins/third_party/juicebox/LICENSE
cursor-plugins/third_party/juicebox/README.md
cursor-plugins/third_party/juicebox/assets/logo.png
cursor-plugins/third_party/juicebox/mcp.json
cursor-plugins/third_party/klaviyo/.cursor-plugin/plugin.json
cursor-plugins/third_party/klaviyo/CHANGELOG.md
cursor-plugins/third_party/klaviyo/LICENSE
cursor-plugins/third_party/klaviyo/README.md
cursor-plugins/third_party/klaviyo/assets/logo.png
cursor-plugins/third_party/klaviyo/mcp.json
cursor-plugins/third_party/mailerlite/.cursor-plugin/plugin.json
cursor-plugins/third_party/mailerlite/CHANGELOG.md
cursor-plugins/third_party/mailerlite/LICENSE
cursor-plugins/third_party/mailerlite/README.md
cursor-plugins/third_party/mailerlite/assets/logo.png
cursor-plugins/third_party/mailerlite/mcp.json
cursor-plugins/third_party/meltwater/.cursor-plugin/plugin.json
cursor-plugins/third_party/meltwater/CHANGELOG.md
cursor-plugins/third_party/meltwater/LICENSE
cursor-plugins/third_party/meltwater/README.md
cursor-plugins/third_party/meltwater/assets/logo.png
cursor-plugins/third_party/meltwater/mcp.json
cursor-plugins/third_party/mem/.cursor-plugin/plugin.json
cursor-plugins/third_party/mem/CHANGELOG.md
cursor-plugins/third_party/mem/LICENSE
cursor-plugins/third_party/mem/README.md
cursor-plugins/third_party/mem/assets/logo.png
cursor-plugins/third_party/mem/mcp.json
cursor-plugins/third_party/mercury/.cursor-plugin/plugin.json
cursor-plugins/third_party/mercury/CHANGELOG.md
cursor-plugins/third_party/mercury/LICENSE
cursor-plugins/third_party/mercury/README.md
cursor-plugins/third_party/mercury/assets/logo.png
cursor-plugins/third_party/mercury/mcp.json
cursor-plugins/third_party/navan/.cursor-plugin/plugin.json
cursor-plugins/third_party/navan/CHANGELOG.md
cursor-plugins/third_party/navan/LICENSE
cursor-plugins/third_party/navan/README.md
cursor-plugins/third_party/navan/assets/logo.png
cursor-plugins/third_party/navan/mcp.json
cursor-plugins/third_party/onedrive/.cursor-plugin/plugin.json
cursor-plugins/third_party/onedrive/CHANGELOG.md
cursor-plugins/third_party/onedrive/LICENSE
cursor-plugins/third_party/onedrive/README.md
cursor-plugins/third_party/onedrive/assets/logo.svg
cursor-plugins/third_party/onedrive/mcp.json
cursor-plugins/third_party/otter/.cursor-plugin/plugin.json
cursor-plugins/third_party/otter/CHANGELOG.md
cursor-plugins/third_party/otter/LICENSE
cursor-plugins/third_party/otter/README.md
cursor-plugins/third_party/otter/assets/logo.png
cursor-plugins/third_party/otter/mcp.json
cursor-plugins/third_party/outlook-calendar/.cursor-plugin/plugin.json
cursor-plugins/third_party/outlook-calendar/CHANGELOG.md
cursor-plugins/third_party/outlook-calendar/LICENSE
cursor-plugins/third_party/outlook-calendar/README.md
cursor-plugins/third_party/outlook-calendar/assets/logo.svg
cursor-plugins/third_party/outlook-calendar/mcp.json
cursor-plugins/third_party/outlook/.cursor-plugin/plugin.json
cursor-plugins/third_party/outlook/CHANGELOG.md
cursor-plugins/third_party/outlook/LICENSE
cursor-plugins/third_party/outlook/README.md
cursor-plugins/third_party/outlook/assets/logo.svg
cursor-plugins/third_party/outlook/mcp.json
cursor-plugins/third_party/outreach/.cursor-plugin/plugin.json
cursor-plugins/third_party/outreach/CHANGELOG.md
cursor-plugins/third_party/outreach/LICENSE
cursor-plugins/third_party/outreach/README.md
cursor-plugins/third_party/outreach/assets/logo.png
cursor-plugins/third_party/outreach/mcp.json
cursor-plugins/third_party/plaud/.cursor-plugin/plugin.json
cursor-plugins/third_party/plaud/CHANGELOG.md
cursor-plugins/third_party/plaud/LICENSE
cursor-plugins/third_party/plaud/README.md
cursor-plugins/third_party/plaud/assets/logo.png
cursor-plugins/third_party/plaud/mcp.json
cursor-plugins/third_party/playwright/.cursor-plugin/plugin.json
cursor-plugins/third_party/playwright/CHANGELOG.md
cursor-plugins/third_party/playwright/LICENSE
cursor-plugins/third_party/playwright/README.md
cursor-plugins/third_party/playwright/assets/logo.svg
cursor-plugins/third_party/playwright/mcp.json
cursor-plugins/third_party/posthog-mcp/.cursor-plugin/plugin.json
cursor-plugins/third_party/posthog-mcp/CHANGELOG.md
cursor-plugins/third_party/posthog-mcp/LICENSE
cursor-plugins/third_party/posthog-mcp/README.md
cursor-plugins/third_party/posthog-mcp/assets/logo.png
cursor-plugins/third_party/posthog-mcp/mcp.json
cursor-plugins/third_party/profound/.cursor-plugin/plugin.json
cursor-plugins/third_party/profound/CHANGELOG.md
cursor-plugins/third_party/profound/LICENSE
cursor-plugins/third_party/profound/README.md
cursor-plugins/third_party/profound/assets/logo.png
cursor-plugins/third_party/profound/mcp.json
cursor-plugins/third_party/readwise/.cursor-plugin/plugin.json
cursor-plugins/third_party/readwise/CHANGELOG.md
cursor-plugins/third_party/readwise/LICENSE
cursor-plugins/third_party/readwise/README.md
cursor-plugins/third_party/readwise/assets/logo.png
cursor-plugins/third_party/readwise/mcp.json
cursor-plugins/third_party/robinhood/.cursor-plugin/plugin.json
cursor-plugins/third_party/robinhood/CHANGELOG.md
cursor-plugins/third_party/robinhood/LICENSE
cursor-plugins/third_party/robinhood/README.md
cursor-plugins/third_party/robinhood/assets/logo.png
cursor-plugins/third_party/robinhood/mcp.json
cursor-plugins/third_party/salesforce/.cursor-plugin/plugin.json
cursor-plugins/third_party/salesforce/CHANGELOG.md
cursor-plugins/third_party/salesforce/LICENSE
cursor-plugins/third_party/salesforce/README.md
cursor-plugins/third_party/salesforce/assets/logo.svg
cursor-plugins/third_party/salesforce/mcp.json
cursor-plugins/third_party/semrush/.cursor-plugin/plugin.json
cursor-plugins/third_party/semrush/CHANGELOG.md
cursor-plugins/third_party/semrush/LICENSE
cursor-plugins/third_party/semrush/README.md
cursor-plugins/third_party/semrush/assets/logo.png
cursor-plugins/third_party/semrush/mcp.json
cursor-plugins/third_party/sharepoint/.cursor-plugin/plugin.json
cursor-plugins/third_party/sharepoint/CHANGELOG.md
cursor-plugins/third_party/sharepoint/LICENSE
cursor-plugins/third_party/sharepoint/README.md
cursor-plugins/third_party/sharepoint/assets/logo.svg
cursor-plugins/third_party/sharepoint/mcp.json
cursor-plugins/third_party/shopify-store/.cursor-plugin/plugin.json
cursor-plugins/third_party/shopify-store/CHANGELOG.md
cursor-plugins/third_party/shopify-store/LICENSE
cursor-plugins/third_party/shopify-store/README.md
cursor-plugins/third_party/shopify-store/assets/logo.png
cursor-plugins/third_party/shopify-store/mcp.json
cursor-plugins/third_party/shopify-store/rules/shopify.mdc
cursor-plugins/third_party/similarweb/.cursor-plugin/plugin.json
cursor-plugins/third_party/similarweb/CHANGELOG.md
cursor-plugins/third_party/similarweb/LICENSE
cursor-plugins/third_party/similarweb/README.md
cursor-plugins/third_party/similarweb/assets/logo.png
cursor-plugins/third_party/similarweb/mcp.json
cursor-plugins/third_party/smartsheet/.cursor-plugin/plugin.json
cursor-plugins/third_party/smartsheet/CHANGELOG.md
cursor-plugins/third_party/smartsheet/LICENSE
cursor-plugins/third_party/smartsheet/README.md
cursor-plugins/third_party/smartsheet/assets/logo.png
cursor-plugins/third_party/smartsheet/mcp.json
cursor-plugins/third_party/sp-global/.cursor-plugin/plugin.json
cursor-plugins/third_party/sp-global/CHANGELOG.md
cursor-plugins/third_party/sp-global/LICENSE
cursor-plugins/third_party/sp-global/README.md
cursor-plugins/third_party/sp-global/assets/logo.png
cursor-plugins/third_party/sp-global/mcp.json
cursor-plugins/third_party/statsig/.cursor-plugin/plugin.json
cursor-plugins/third_party/statsig/CHANGELOG.md
cursor-plugins/third_party/statsig/LICENSE
cursor-plugins/third_party/statsig/README.md
cursor-plugins/third_party/statsig/assets/logo.png
cursor-plugins/third_party/statsig/mcp.json
cursor-plugins/third_party/teams/.cursor-plugin/plugin.json
cursor-plugins/third_party/teams/CHANGELOG.md
cursor-plugins/third_party/teams/LICENSE
cursor-plugins/third_party/teams/README.md
cursor-plugins/third_party/teams/assets/logo.svg
cursor-plugins/third_party/teams/mcp.json
cursor-plugins/third_party/tinyfish/.cursor-plugin/plugin.json
cursor-plugins/third_party/tinyfish/CHANGELOG.md
cursor-plugins/third_party/tinyfish/LICENSE
cursor-plugins/third_party/tinyfish/README.md
cursor-plugins/third_party/tinyfish/assets/logo.png
cursor-plugins/third_party/tinyfish/mcp.json
cursor-plugins/third_party/todoist/.cursor-plugin/plugin.json
cursor-plugins/third_party/todoist/CHANGELOG.md
cursor-plugins/third_party/todoist/LICENSE
cursor-plugins/third_party/todoist/README.md
cursor-plugins/third_party/todoist/assets/logo.png
cursor-plugins/third_party/todoist/mcp.json
cursor-plugins/third_party/trello/.cursor-plugin/plugin.json
cursor-plugins/third_party/trello/CHANGELOG.md
cursor-plugins/third_party/trello/LICENSE
cursor-plugins/third_party/trello/README.md
cursor-plugins/third_party/trello/assets/logo.png
cursor-plugins/third_party/trello/mcp.json
cursor-plugins/third_party/typeform/.cursor-plugin/plugin.json
cursor-plugins/third_party/typeform/CHANGELOG.md
cursor-plugins/third_party/typeform/LICENSE
cursor-plugins/third_party/typeform/README.md
cursor-plugins/third_party/typeform/assets/logo.png
cursor-plugins/third_party/typeform/mcp.json
cursor-plugins/third_party/upwork/.cursor-plugin/plugin.json
cursor-plugins/third_party/upwork/CHANGELOG.md
cursor-plugins/third_party/upwork/LICENSE
cursor-plugins/third_party/upwork/README.md
cursor-plugins/third_party/upwork/assets/logo.png
cursor-plugins/third_party/upwork/mcp.json
cursor-plugins/third_party/webull/.cursor-plugin/plugin.json
cursor-plugins/third_party/webull/CHANGELOG.md
cursor-plugins/third_party/webull/LICENSE
cursor-plugins/third_party/webull/README.md
cursor-plugins/third_party/webull/assets/logo.png
cursor-plugins/third_party/webull/mcp.json
cursor-plugins/third_party/workable/.cursor-plugin/plugin.json
cursor-plugins/third_party/workable/CHANGELOG.md
cursor-plugins/third_party/workable/LICENSE
cursor-plugins/third_party/workable/README.md
cursor-plugins/third_party/workable/assets/logo.png
cursor-plugins/third_party/workable/mcp.json
cursor-plugins/third_party/wrike/.cursor-plugin/plugin.json
cursor-plugins/third_party/wrike/CHANGELOG.md
cursor-plugins/third_party/wrike/LICENSE
cursor-plugins/third_party/wrike/README.md
cursor-plugins/third_party/wrike/assets/logo.png
cursor-plugins/third_party/wrike/mcp.json
cursor-plugins/third_party/x-ads/.cursor-plugin/plugin.json
cursor-plugins/third_party/x-ads/CHANGELOG.md
cursor-plugins/third_party/x-ads/LICENSE
cursor-plugins/third_party/x-ads/README.md
cursor-plugins/third_party/x-ads/assets/logo.png
cursor-plugins/third_party/x-ads/mcp.json
cursor-plugins/third_party/x-money/.cursor-plugin/plugin.json
cursor-plugins/third_party/x-money/CHANGELOG.md
cursor-plugins/third_party/x-money/LICENSE
cursor-plugins/third_party/x-money/README.md
cursor-plugins/third_party/x-money/assets/logo.png
cursor-plugins/third_party/x-money/mcp.json
cursor-plugins/third_party/x/.cursor-plugin/plugin.json
cursor-plugins/third_party/x/CHANGELOG.md
cursor-plugins/third_party/x/LICENSE
cursor-plugins/third_party/x/README.md
cursor-plugins/third_party/x/assets/logo.svg
cursor-plugins/third_party/x/mcp.json
cursor-plugins/third_party/x/skills/x-api-mcp-guide/references/pricing.md
cursor-plugins/third_party/xero/.cursor-plugin/plugin.json
cursor-plugins/third_party/xero/CHANGELOG.md
cursor-plugins/third_party/xero/LICENSE
cursor-plugins/third_party/xero/README.md
cursor-plugins/third_party/xero/assets/logo.png
cursor-plugins/third_party/xero/mcp.json
cursor-plugins/third_party/zoom/.cursor-plugin/plugin.json
cursor-plugins/third_party/zoom/CHANGELOG.md
cursor-plugins/third_party/zoom/LICENSE
cursor-plugins/third_party/zoom/README.md
cursor-plugins/third_party/zoom/assets/logo.png
cursor-plugins/third_party/zoom/mcp.json
```
## 6. `scripts/` · 104 个 · 初判 **低**（作为方法）/ **高**（作为机制参照）

**理由**：104 个里 62 个是 `orchestrate` 与 `pstack/poteto-mode` 的 TypeScript 实现与测试，
17 个是 `addyosmani-agent-skills/scripts/` 的校验脚本。**前者是 execution mechanics** —— 
本库 `AGENTS.md` 硬边界第 5 条明说本库 Driver **停在逻辑编排层，不定义进程/并发/WIP/队列/锁/重试**。
按这条边界，本库不吸收这些实现本身。

**但**：那 17 个是**校验器**（`skill-lint.js`、`validate-commands.js`、`validate-artifact-paths.js`、
`validate-reference-links.js`、`validate-versions.js`、`run-evals.js`），
**形态与本库 `scripts/` 的三个检查器同类**。这是「别人怎么做检查器」的方法参照。**不裁。**

**逐仓分布**（scout 实测）：

| 位置 | 文件数 |
|---|---|
| `addyosmani-agent-skills/scripts` | 15 |
| `cursor-plugins/orchestrate/…/scripts` | 62 |
| `cursor-plugins/pstack/skills/show-me-your-work/scripts` | 1 |
| `cursor-plugins/pstack/…/poteto-mode/scripts` | 20 |
| `cursor-plugins/scripts` | 1 |
| `mattpocock-skills/scripts` | 3 |
| `mattpocock-skills/skills/engineering/diagnosing-bugs/scripts` | 1 |
| `mattpocock-skills/skills/misc/git-guardrails-claude-code/scripts` | 1 |
| **合计** | **104** |

```
addyosmani-agent-skills/scripts/floor-guard-reference-test.js
addyosmani-agent-skills/scripts/lib/skill-lint-test.js
addyosmani-agent-skills/scripts/lib/skill-lint.js
addyosmani-agent-skills/scripts/run-evals-test.js
addyosmani-agent-skills/scripts/run-evals.js
addyosmani-agent-skills/scripts/validate-artifact-paths-test.js
addyosmani-agent-skills/scripts/validate-artifact-paths.js
addyosmani-agent-skills/scripts/validate-commands-test.js
addyosmani-agent-skills/scripts/validate-commands.js
addyosmani-agent-skills/scripts/validate-reference-links-test.js
addyosmani-agent-skills/scripts/validate-reference-links.js
addyosmani-agent-skills/scripts/validate-skills.js
addyosmani-agent-skills/scripts/validate-versions-test.js
addyosmani-agent-skills/scripts/validate-versions.js
addyosmani-agent-skills/skills/idea-refine/scripts/idea-refine.sh
cursor-plugins/orchestrate/skills/orchestrate/scripts/__tests__/agent-manager-slack-mirror.test.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/__tests__/andon-root-cache.test.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/__tests__/checkpoint-restart.test.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/__tests__/comment-cli.test.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/__tests__/comment-retry-queue.test.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/__tests__/exit-on-error.test.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/__tests__/failure-handoff.test.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/__tests__/handoff-branch-parser.test.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/__tests__/handoff-verification-parser.test.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/__tests__/handoff-verification-record.test.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/__tests__/kickoff-dedupe.test.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/__tests__/measurements-compare.test.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/__tests__/measurements-mismatch.test.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/__tests__/measurements-parser.test.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/__tests__/models-catalog.test.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/__tests__/operator-boundary.test.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/__tests__/probe-models.test.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/__tests__/prompt-plan-validation.test.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/__tests__/redact-body.test.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/__tests__/schemas.test.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/__tests__/slack-adapter.test.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/__tests__/slack-channel-boundary.test.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/__tests__/slack-message-format.test.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/__tests__/slack-prompt-shape.test.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/__tests__/support/slack-web-api-mock.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/__tests__/verifier-startingref-reconcile.test.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/__tests__/wait-handoff-failure.test.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/__tests__/watchdog-inspect.test.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/__tests__/worker-branch-discipline.test.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/adapters/README.md
cursor-plugins/orchestrate/skills/orchestrate/scripts/adapters/index.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/adapters/slack/client.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/adapters/slack/index.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/adapters/types.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/biome.json
cursor-plugins/orchestrate/skills/orchestrate/scripts/bun.lock
cursor-plugins/orchestrate/skills/orchestrate/scripts/cli.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/cli/andon.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/cli/comments.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/cli/forensics.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/cli/index.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/cli/inspect.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/cli/task.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/cli/util.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/core/agent-manager.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/core/andon.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/core/branches.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/core/comment-retry-queue.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/core/failure-handoff.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/core/handoff.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/core/loop.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/core/prompts.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/core/redact-body.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/errors.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/measurements.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/models.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/package.json
cursor-plugins/orchestrate/skills/orchestrate/scripts/schemas.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/tools/generate-json-schemas.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/tools/nudge-root.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/tools/probe-models.ts
cursor-plugins/orchestrate/skills/orchestrate/scripts/tsconfig.json
cursor-plugins/pstack/skills/poteto-mode/scripts/bootstrap.ts
cursor-plugins/pstack/skills/poteto-mode/scripts/bun.lock
cursor-plugins/pstack/skills/poteto-mode/scripts/check-plan.mjs
cursor-plugins/pstack/skills/poteto-mode/scripts/orch/orch.test.ts
cursor-plugins/pstack/skills/poteto-mode/scripts/orch/orch.ts
cursor-plugins/pstack/skills/poteto-mode/scripts/orch/store.ts
cursor-plugins/pstack/skills/poteto-mode/scripts/package.json
cursor-plugins/pstack/skills/poteto-mode/scripts/watch-pr/cli.test.ts
cursor-plugins/pstack/skills/poteto-mode/scripts/watch-pr/cli.ts
cursor-plugins/pstack/skills/poteto-mode/scripts/watch-pr/fakes.test-helper.ts
cursor-plugins/pstack/skills/poteto-mode/scripts/watch-pr/github.test.ts
cursor-plugins/pstack/skills/poteto-mode/scripts/watch-pr/github.ts
cursor-plugins/pstack/skills/poteto-mode/scripts/watch-pr/policy.test.ts
cursor-plugins/pstack/skills/poteto-mode/scripts/watch-pr/policy.ts
cursor-plugins/pstack/skills/poteto-mode/scripts/watch-pr/render.ts
cursor-plugins/pstack/skills/poteto-mode/scripts/watch-pr/tsconfig.json
cursor-plugins/pstack/skills/poteto-mode/scripts/watch-pr/types.compile.ts
cursor-plugins/pstack/skills/poteto-mode/scripts/watch-pr/types.ts
cursor-plugins/pstack/skills/poteto-mode/scripts/watch-pr/watch-pr
cursor-plugins/pstack/skills/poteto-mode/scripts/worktree-audit.sh
cursor-plugins/pstack/skills/show-me-your-work/scripts/log.sh
cursor-plugins/scripts/validate-plugins.mjs
mattpocock-skills/scripts/link-skills.sh
mattpocock-skills/scripts/list-skills.sh
mattpocock-skills/scripts/sync-plugin-version.mjs
mattpocock-skills/skills/engineering/diagnosing-bugs/scripts/hitl-loop.template.sh
mattpocock-skills/skills/misc/git-guardrails-claude-code/scripts/block-dangerous-git.sh
```

## 7. 任务二 · 锁文件只读 sha256 核对（scout 的 F6）

### 7.0 只读保证

`scripts/_render-lock.py` 的 docstring 第 5 行逐字：
> `只读 upstreams/，只写 upstreams.lock.yaml。不碰任何其他文件。`

**它会写 `upstreams.lock.yaml`。因此本轮没有运行它。** 按派工要求，scout 改写了一段**只读等价代码**：
复用它的 `REPOS`、`SKIP_DIRS`、`os.walk` 裁剪与 `sha256[:16]` 逻辑，**不执行写入**，输出只到 `/tmp`。

| 保护对象 | 手段 | 实测 |
|---|---|---|
| `upstreams.lock.yaml` | 全程只读打开；比对逻辑在内存 | **零改动**（sha256 与 mtime 见 §7.5） |
| `upstreams/**` | 只用 `os.walk` 读、`hashlib` 读字节 | **零改动**（`git status upstreams/` 空） |
| 本库其它文件 | 无写入 | **零改动** |

### 7.1 逐仓 commit pin vs 实际 git HEAD

| 仓 | 锁内 pin | 锁内 date | 实测 HEAD | 实测 HEAD date | 一致 | 工作区 |
|---|---|---|---|---|---|---|
| `pstack` | `ecc249f1e306…` | 2026-09-25 | `ecc249f1e306…` | 2026-09-25 | **是** | 干净 |
| `matt` | `c55ee46073ed…` | 2026-09-18 | `c55ee46073ed…` | 2026-09-18 | **是** | 干净 |
| `addy` | `2686b620fc1f…` | 2026-09-25 | `2686b620fc1f…` | 2026-09-25 | **是** | 干净 |

**`pstack` 的特殊处理（这条值得 driver 注意）**：

`upstreams/cursor-plugins/pstack/` **自己没有 `.git` 目录** —— 它是父仓 `upstreams/cursor-plugins/` 
的一个子目录。scout 沿目录向上找到最近的 git 仓 `upstreams/cursor-plugins/`，
其 HEAD = `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`，**与锁内 pin 逐字相同**。
`git cat-file -t ecc249f1e306…` 返回 `commit`，确认该对象在父仓中真实存在。

**因此三仓全部一致，0 漂移。**

### 7.2 逐 skill sha256 核对（101 条）

| 项 | 数 |
|---|---|
| 锁内条目 | 101 |
| **sha256 一致** | **101** |
| sha256 漂移 | 0 |
| 文件缺失 | 0 |

**101 / 101 完全一致，0 漂移，0 缺失。**

### 7.3 只读重跑枚举（复现 `_render-lock.py:52-60` 的逻辑）

| 比对维度 | 结果 |
|---|---|
| 只读重跑枚举出的条数 | **101** |
| 锁内条数 | **101** |
| 锁有 / 枚举无 | **0**（空集） |
| 枚举有 / 锁无 | **0**（空集） |
| 同键 sha256 不一致 | **0** |

**锁文件与上游实物当前完全同步。若此刻运行 `_render-lock.py`，产出会与现有 `upstreams.lock.yaml` 逐字相同。**

### 7.4 反向差集：磁盘上不在锁里的 `SKILL.md`

磁盘 `SKILL.md` 总数 **159**，锁内 101，**不在锁里 58** —— 与姊妹文件 §1 的 58 吻合。

**这条同时说明：sha256 全绿 ≠ 枚举完整。** 101 条逐字节一致，
但它们只覆盖 `SKILL.md`；那 58 个与本文件列的 1080 个载体**根本不在比对范围内**。
锁文件没有失效，是**它的覆盖面**不含它们。

### 7.5 `upstreams.lock.yaml` 零改动自证

| 项 | 值 |
|---|---|
| 当前 sha256[:16] | `a056b2ced80d3a6e` |
| 当前大小 | 15451 字节 |
| 当前 mtime | 2026-09-28T06:15:40 |

**本轮未执行 `_render-lock.py`**（它第 61 行之后会 `LOCK.write_text(...)`），**未对 `upstreams.lock.yaml` 调用任何写 API**。
`git status --porcelain upstreams/` 返回空 —— 该路径整体不在本仓 git 追踪内，
**「git 干净」在此不足以单独作为证据**，故以上表给出独立的 sha256 与 mtime。

### 7.6 F6 结论

| 原 F6 陈述 | 现状 |
|---|---|
| 「锁文件 mtime 早于 check-closure.py，可能已脱节」 | **UNVERIFIED → PASS（已排除脱节）** |
| 缺什么 | 不缺了。已跑完 pin 比对、sha256 比对、只读重跑枚举三项，全部一致 |

**但**：F6 当初的**观察**（mtime `Sep 28 06:15` 早于 `check-closure.py` 的 `Sep 30 01:36`）
**本身仍是事实**。只是它的推论（「可能已脱节」）经核对**不成立** —— 
`check-closure.py` 后来被改过，不等于 `upstreams.lock.yaml` 变旧。
**一个文件比另一个文件旧，不构成它失效的证据。**

---

## 8. 空结果清单（照实写，不补）

| 项 | 结果 |
|---|---|
| 载体类中未列出的文件 | **0 个**。§1-§6 共列 1080 条；M5 更正后机器重验 `missing = 0`，与 1080 逐条闭合 |
| 使用「等」「若干」「部分」省略的路径 | **0 处** |
| 「4.5 倍」作为结论出现在正文 | **0 处**。仅存于 §5.3 的 M5 更正注记（记录原值→新值，供复核对账） |
| 「零信息」/「零方法」表述 | **0 处**。已全部改为「未识别到方法正文」 |
| sha256 漂移的 skill | **0 个** |
| 锁内条目但文件缺失 | **0 个** |
| commit pin 与 HEAD 不一致的仓 | **0 个** |
| 只读重跑枚举与锁的差集 | **空集**（双向） |
| `third_party/` 里 scout **未识别到方法正文**的包 | **74 个**（79 − 5 带 `SKILL.md`）；其中 73 个是纯骨架包，1 个是带 `rules` 的 `shopify-store`。**证据限定表述，不等于「已证明没有」** |
| 各类「是否已被本库吸收」 | **UNVERIFIED（故意留空）** —— 需 adversary 判据，Owner 尚未给 |
| 载体类「本库是否有方法价值」的最终判定 | **UNVERIFIED** —— 本文件只给初判，处置不是 scout 的活 |
| 姊妹文件 §3.2 的 `evals/plugin` 场景数 | **原写 4，实测 3**，本文件 §4 为准 |
| 姊妹文件 §3.2 的 `evals/fixtures` 子目录数 | **原写 20，实测 25**，本文件 §4 为准 |

## 9. 纪律自证

- `upstreams/` 只读。`upstreams.lock.yaml` 只读，**未运行 `_render-lock.py`**（它会写 lock），改用只读等价代码。
- 本库写入仅两个落点：本文件 + 姊妹文件 §7 追加节。`registry.yaml` / `roles/` / `skills/` / `scripts/` / `upstreams.lock.yaml` **零改动**。
- 未执行 `git add` / `commit` / `tag`。
- 每个结论带 `仓/路径` 锚点。
- 三态只用 PASS / FAIL / UNVERIFIED。**本文件无 FAIL。**
- **未裁决任何处置。** §5.3 的「建议整体排除」明确标注为建议；§1 各档初判标注为初判；
  §1.hooks 例外节的两份 `.md` 标注为**单独处置、未裁定吸收**；三处都把最终判定留给 adversary / Owner。
- **M5 更正不改历史裁定。** 本轮只改本台账（作者交付物），未动 `0930-oracle-M34-DECISION.md`，
  未动 adversary 的复核文件。**scout 不自评**，等 adversary 独立复核。
