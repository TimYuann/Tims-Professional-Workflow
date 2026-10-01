# ABSORB-B-CALIBRATION · B 类小样本校准与准入口径

2026-10-01 · 实例 `tpw-absorb-b`（B 类，机制级 coverage/裁定）· 工作树 `~/Developer/tim-professional-workflow/.worktrees/night-2026-10-01`
依据：`UPSTREAM-DEEP-ABSORPTION-PLAN.md` §3（B 机制级覆盖与采纳分离）、§4（记账/评估完成度分离、pending-check）、§5（校准与实际采纳）、§6（Owner 决定点）。
输入：`ABSORB-A1-ADDY-INDEX.tsv`（208 行）、`ABSORB-A2-CURSOR-INDEX.tsv`（863 行）、`ABSORB-A3-MATT-INDEX.tsv`（169 行）及各自 HEADER；三仓只读 locator 根 `.worktrees/legacy-pre-night-2026-10-01/upstreams/`；当前产品正文 `professional-workflow/`（19 文件、73,623 B）只读。

本文件只做三件事：**（1）校准**（B 独立回读原文 → 再对照 A 屏）；**（2）准入口径修正**；**（3）计数与未评估项的诚实报告**。不含采纳决定（见 `ABSORB-B-ADJUDICATION.md`），不给百分比，不写 core/product/legacy。

---

## 1 · 固定输入核对（本轮实测）

| 项 | A 表声明 | 本轮实测 | 结论 |
| --- | --- | --- | --- |
| `addyosmani-agent-skills` HEAD | `2686b620fc1fed2e8f60c704839c766b8594c6b6` | 同值；`git status --porcelain` 0 行 | 一致，未停 |
| `cursor-plugins` HEAD | `ecc249f1e306fc64ddf83c7bed16cacf7c2239db` | 同值；0 行 | 一致，未停 |
| `mattpocock-skills` HEAD | `c55ee46073ed923f86ce59a5eb3b6d895095d1b7` | 同值；0 行 | 一致，未停 |
| A 表数据行 | 208 / 863 / 169 = 1240 | 逐表实测 208 / 863 / 169 | 与计划 §1 分母相等 |
| A 表列形 | 10 列、tab 分隔、首行表头 | 实测每行恰 10 列、无空单元、无重复 path | 与 HEADER 声明一致 |

跨源复核（本轨新增，供 Driver 引用）：

- `commands/review.toml` 与 `.gemini/commands/review.toml` 逐字节相同（各 844 B，`diff` 返回 IDENTICAL）。
- `thermos/skills/thermo-nuclear-code-quality-review/SKILL.md` 与 `cursor-team-kit/skills/thermo-nuclear-code-quality-review/SKILL.md` 逐字节相同：两者 sha256 均为 `7faca08b51b643b2ddd0836f92af15574444024685dcc1e677dbbb39ae8c9e8f`（A2 行曾记为"逐字重复的可能性高，建议 shasum 比对"——本轨已执行并确认）。
- `docs/engineering/codebase-design.md` 确含 issue #458 与 dependency-cruiser 指向，且该页同时声称 `setup-ts-deep-modules` "has no lint rule shipped with it"——而已读的 `skills/in-progress/setup-ts-deep-modules/dependency-cruiser.config.cjs` 正是该规则（A3 §7.4 的 docs/SKILL 漂移观察成立）。

## 2 · 本次实际读过的原文（可复核）

- **产品正文（coverage 的判定面）**：`professional-workflow/` 全部 19 份文件从头读到尾（authority 2、profiles 7、methods 4、charters 5、README 1），合计 73,623 B。所有 `current_text_basis` 均以此为据，不依赖二手转述。
- **上游原文（校准面）**：
  - A1：`commands/review.toml`、`.gemini/commands/review.toml`（全文，844 B ×2）；`evals/cases/test-driven-development.json`（全文）；`scripts/validate-artifact-paths.js`（全文）；`docs/skill-anatomy.md`（前 120 行 + 章节结构，未读全文）；`skills/debugging-and-error-recovery/SKILL.md`（前 60 行 + 全部 H2/H3 锚点）；`hooks/simplify-ignore.sh`（头注释 + 函数/关键行）。
  - A2：`third_party/xero/{mcp.json, .cursor-plugin/plugin.json, README.md}`（全文）；`third_party/x-money/skills/x-money-guide/SKILL.md`（前 80 行，覆盖批准规则/连接/故障排查主体）与 `x-money/mcp.json`、`plugin.json`；`pstack/skills/poteto-mode/scripts/orch/store.ts`（导入与类型面 + `atomicWrite`/`writeIfMissing`/`holderIsDead`/`acquireLock`/`readTsv`/`writeTsv`，即锁与持久化段）；`orchestrate/skills/orchestrate/SKILL.md`（前 60 行含六条核心原则与节点表）；`docs-canvas/skills/docs-canvas/SKILL.md`（前 50 行含 Status 引用块）。
  - A3：`skills/engineering/diagnosing-bugs/scripts/hitl-loop.template.sh`（全文）；`skills/engineering/tdd/mocking.md`（全文，1,481 B）；`.out-of-scope/question-limits.md`（全文）；`docs/engineering/codebase-design.md`（章节 + 前 40 行 + #458 段）；`skills/in-progress/setup-ts-deep-modules/dependency-cruiser.config.cjs`（全文）；`.changeset/retro-deterministic-checks.md`（全文）。
- **索引级读取**：三份 A TSV 全文解析（1,240 行）用于机制聚类与来源路径锚定；本轨 TSV 中每一条 `source_paths` 均以脚本对三份 A 表逐条校验（183 行、0 条无法解析，6 条为目录前缀引用，见 §6）。
- **未做**：未 fetch / 未安装 / 未起服务 / 未跑测试、eval、hook 或任何上游脚本；未执行 git 写操作；未改 UCBIP；未提交；未派工；未写 core/product/legacy。

### 2.1 前瞻暴露登记（诚实声明）

校准时无法做到全部盲读：本实例开工时先读了三份 HEADER 与三份 TSV 的开头若干行，随后为构建机制清单又打印过 A1 全部 25 个 `skills/*/SKILL.md`、A3 全部 38 个 `SKILL.md`、A2 全部 first-party `SKILL.md` 的 `source_mechanism` 列。因此校准样本按暴露程度分三级记录：

- **盲读（B 未见过该行）**：10 条（A1-1/2/3/4、A3-13/14/15/16/17/18）。
- **仅 HEADER 级暴露**：3 条（A2-7/8/9，HEADER §7 有概述，未见行）。
- **行级已见**：5 条（A1-5/6、A2-10/11/12）。

行级已见的 5 条仍保留在样本内，但它们验证的是"A 的锚点是否可被独立复核"而非"B 能否独立发现"；A 侧漏检率的主要证据来自前 13 条。这不是合格性缺陷，但决定了本校准只能声明"未发现系统性锚定错误"，不能声明"漏检率上界"。

## 3 · 校准样本（18 条，跨源跨类型）

口径：**先读原文、后看 A 行**；下表"独立读"列是本轨从原文得到的机制要点，"A 行"列是事后比对结论。

| # | 源 / 路径 | 类型 | 暴露 | 独立读（要点） | 与 A 行比对 | 判定 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | addy `commands/review.toml` + `.gemini/commands/review.toml` | 平台包装 + 重复 | 盲 | 844 B ×2 逐字节相同；`description` 一行 + `prompt` 五轴（correctness/readability/architecture/security/performance）+ 分级（Critical/Important/Suggestion）+ 要求 file:line | A 行给了同样的双键锚点、三宿主同步面与 `validate-commands.js` 的 NAME_MAP 回查；A 未在本行标注"两文件逐字节相同"（HEADER 已按 blob sha 归纳 5 组真重复） | 锚定准确；重复证据应从 HEADER 并入行内 |
| 2 | addy `evals/cases/test-driven-development.json` | 评测数据（support） | 盲 | 4 条正/负触发（负例带 `owner`）、3 个 eval（两套 fixture：`test-driven-development` 与 `-ecosystem`）、`expectations[]` 是可验证陈述而非措辞、压力场景用例（"hotfix window closes in ten minutes"仍要求先写失败测试） | A 行：正/负触发 + owner 语义 + kind/files/expectations；A 声明"负例 owner 排名断言未运行验证" | 锚定准确；压力场景这一机制线索 A 未单列（属细节损失，非错误） |
| 3 | addy `scripts/validate-artifact-paths.js` | 机器护栏 | 盲 | allowlist 四条（SPEC.md/docs/SPEC.md/tasks/plan.md/tasks/todo.md）× 14 个受护文件（9 命令 + 2 技能 + 3 文档）；正则含占位目录；缺失文件跳过；文件头引用 PR #93 事故；范围自述"刻意收窄" | A 行的 allowlist 内容、受护文件数、PR #93 缘由、窄范围与跳过语义**逐项与实现一致** | 锚定准确（A 标 depth=structure，但描述覆盖了实现要点） |
| 4 | addy `docs/skill-anatomy.md` | 规范文档 | 盲 | 本轨只读前 120 行：frontmatter 规则（name=目录名、description 先 what 后 Use when、≤1024、"不得把流程写进描述"）、推荐章节、支持文件阈值、共享 references、published-name 兼容 | A 行为 full 读，另含 Context Efficiency、Script Requirements、Write the Procedure Not the Workaround（arXiv 引用）、Required vs Recommended、规范-linter 覆盖差 | **A 细节多于本轨**；无漏检，属"细节增益" |
| 5 | addy `skills/debugging-and-error-recovery/SKILL.md` | 技能正文（与现有覆盖重叠） | 行级已见 | Stop-the-Line 六步、六步分诊、不可复现流程树、错误类型分诊、安全降级、埋点、Common Rationalizations、错误输出视为不可信数据、Red Flags、Verification | A 行覆盖同构；A 的 loci 记 `E,F`，而正文的 "document conditions and monitor" 与安全降级偏 D/E，"untrusted data" 偏安全/F | 锚定准确；loci 偏窄（不影响覆盖判定） |
| 6 | addy `hooks/simplify-ignore.sh` | 隐藏支持技术 | 行级已见 | 三事件语义、占位符往返（`BLOCK_<hash>` 8 位）、磁盘始终占位、按项目隔离缓存、`shopt -u patsub_replacement` 的 Bash 5.2 防护、占位符被删/被改时的模糊匹配与告警 | A 行覆盖上述全部，包含 Bash 5.2 细节 | 锚定准确 |
| 7 | cursor `third_party/xero/{mcp.json, plugin.json, README.md}` | 平台包装（stdio 本地进程） | HEADER 级 | `npx -y @xeroapi/xero-mcp-server@latest`；env 注入 `XERO_CLIENT_ID/SECRET`；`variables` 声明仅两字段；Custom Connection（机器到机器 OAuth2）、绑定单一组织、付费附加、`XERO_SCOPES` 收窄、Payroll 限 NZ/UK、"server 是工具名真源" | A 的 `mcp.json` 行是传输级（stdio+env），其余语义在 README 行；A 的 HEADER §7.3/§7.4 已把两类传输与凭据形态列为事实 | 锚定准确；**聚合口径问题**：单看 mcp.json 行会丢失权限/scope/门控语义，机制分组必须并入同 connector 的 plugin.json 与 README 行 |
| 8 | cursor `third_party/x-money/skills/x-money-guide/SKILL.md` | 高风险行为守则 | HEADER 级 | 五条"动钱前一律确认"（每次问/等回答/一次一批/变更重批/不得假装；approval 入参由服务端强制）、连接码+passkey、撤销路径、十类故障的"用户可见原话+一个下一步"、三值 outcome（completed/pending/refused）、拒绝后不得重试、幂等键复用、卡数据绝不上屏 | A 行是本样本中最详尽的一行，逐条与原文一致 | 锚定准确；A 未单列 `name: X Money guide` 与目录名 `x-money-guide` 的不一致（低material的细节） |
| 9 | cursor `pstack/.../scripts/orch/store.ts` | 大型机器面（structure） | HEADER 级 | `atomicWrite`：同目录 `.{base}.{pid}.{uuid}.tmp` + `wx` 独占创建 + `rename` + `finally rm`；`writeIfMissing`；`holderIsDead` 用 `process.kill(pid,0)`/`ESRCH`；`acquireLock` 的 EEXIST→读 holder→陈旧接管→`force` 路径→释放前校验 PID 归属；`readTsv` 校验表头与列宽；`writeTsv` 清洗单元格 | A 的行内描述（锁文件 PID 判定与过期替换、原子写、TSV 校验）与实现一致；A 诚实标注未逐行读 | 锚定准确；本轨补出 `wx`/`finally`/`ESRCH`/`force` 等实现细节，属细节增益 |
| 10 | cursor `thermos/.../thermo-nuclear-code-quality-review/SKILL.md` ↔ `cursor-team-kit/...` | 重复 | 行级已见 | 本轨实测两文件 sha256 相同（见 §1）；A 的 uncertainty 提出该假设并给出 shasum 回查 | A 未直接断定逐字节相同（"可能性高"） | 锚定准确且留白正确；本轨把假设升级为已证事实 |
| 11 | cursor `orchestrate/skills/orchestrate/SKILL.md` | 编排总纲 | 行级已见 | 六条核心原则（planner 不写代码/不知谁接任务/worker 一任务一克隆一次交接/subplanner 递归/handoff 驱动的无终态/传播而非同步）、五节点表、需先读 cursor-sdk、Slack 可选且不影响正确性 | A 行与原文一致（含"Long-running agent loops drift…"引句）；A 的 requery 指向 references/planner.md 的 Prerequisites | 锚定准确；本轨补出"Slack 未设置时只记一次日志、正确性不变"这一边界 |
| 12 | cursor `docs-canvas/skills/docs-canvas/SKILL.md` | 未完成形态 | 行级已见 | 顶部 Status 引用块明确 placeholder；canvas 原语清单（cards/code/diagram/callout/table）；四层布局；语气要求 | A 行一致 | 锚定准确 |
| 13 | matt `skills/engineering/diagnosing-bugs/scripts/hitl-loop.template.sh` | 隐藏支持技术 | 盲 | `step`/`capture VAR` 两助手；KEY=VALUE 回传契约；注释点明"capture 会回显给 agent 读，所以把登录留成 step"；mode 100644 | A 行覆盖全部要点且标注 SKILL 未说明调用方式 | 锚定准确 |
| 14 | matt `skills/engineering/tdd/mocking.md` | 隐藏支持文档 | 盲 | 只在系统边界打桩（外部 API/数据库有时/时间随机/文件系统有时）；不 mock 自己拥有的一切；两条可 mock 设计规则（依赖注入、SDK 式按操作接口 > 通用 fetcher） | A 行覆盖一致，并指出该 DI 规则在 `codebase-design/SKILL.md` 重复 | 锚定准确；重复线索 A 已标记 |
| 15 | matt `.out-of-scope/question-limits.md` | 政策/缺口线索 | 盲 | 不设问题数上限；开放 grilling 的理由；区分"计划确实欠定（按设计工作）"与"问题低质（提示词问题）"；自然语言转向是控制面；先前请求 #44 | A 行覆盖一致；A 标 requery=none，未指出 issue 号不可达 | 锚定准确；**细节损失**：A 未把"issue 号不可达"的弱点写进 uncertainties（HEADER §7.10 提过同类不可达） |
| 16 | matt `docs/engineering/codebase-design.md` | 文档页（docs/SKILL 漂移） | 盲 | glossary 即技能、逐词"don't say"表、depth-as-leverage（显式拒绝 Ousterhout 比值定义）、"reference, not a process"、#458 的强制手段讨论 | A 行覆盖并额外记录四原则与"reference 被误当 driver"的失败模式 | 锚定准确；本轨确认 #458 段与 in-progress lint 规则的冲突真实存在 |
| 17 | matt `skills/in-progress/setup-ts-deep-modules/dependency-cruiser.config.cjs` | 未晋升桶 + 机器规则 | 盲 | `PACKAGES_ROOT`；`PACKAGE_INTERNALS` 派生；五条 severity=error 规则（from-app / across-packages 用 `$1` 同包回引 / tests-through-entrypoints × 自测例外 / tests-folder-is-private / no-circular 全局）；被注释的 layering 桩；resolver options | A 行逐项一致，含 `$1` 回引与"no-circular 可收窄到 packages root"的注释 | 锚定准确 |
| 18 | matt `.changeset/retro-deterministic-checks.md` | 变更记录 | 盲 | mechanical vs judgement 分类优先；mechanical 违规→确定性检查（linter/pre-commit/CI）；`CODING_STANDARDS.md` 只留给判断类；"没有任何护栏"本身就是 finding | A 行一致 | 锚定准确 |

### 3.1 校准结论

1. **无系统性锚定错误**：18 条中没有一条 A 行的 `source_mechanism` 与原文冲突；4 条（#3/#6/#9/#17）本轨逐项复核了实现级细节，全部吻合；#10 把 A 的假设升级为已证事实。
2. **A 的自我留白质量高**：A1 在 `validate-artifact-paths.js` 与 `store.ts` 上标 structure 却给出了实现要点；A2 在 thermo-nuclear 重复上保留"可能性高"而不越权断定；A3 在 mocking.md 上主动标出跨文件重复。
3. **未发现漏检的机制线索（在盲读的 10 条内）**：本轨从原文新提出的机制线索只有两类——(a) eval 用例中的"权威压力下仍先写失败测试"场景；(b) xero README 的组织绑定/付费/区域限制。两者都属于"行内可加，不影响机制存在性"。
4. **主要风险不是错误而是口径**：见 §4 的六项修正，全部是**消费侧口径**问题，不要求重写 A 表。

## 4 · 准入口径修正（C1–C6，连同需回查的受影响组）

按计划 §5"系统性偏差 → 只修口径并列出受影响组，不全量作废"。

| 编号 | 现象（证据） | 口径修正（消费侧） | 受影响组（供 Driver 回查） |
| --- | --- | --- | --- |
| **C1** | `responsibility_loci` 的**顺序与词汇不一致**：A3 用 canonical A→F 顺序；A1 与 A2 不保证顺序（A2 出现 `F,B`、`F,D,B` 等倒序），A2 另有 193 行 `none`（license/资产/metadata）。若按字符串分组会把人/机制切碎 | loci 只作**无序集合**使用；不得作覆盖分母、不得作加权；`none` 不是"无责任"判断而是"该路径未承载判断面" | A1 全部 208 行、A2 全部 863 行（尤其 `third_party` 的 482 行、license/资产行）；A3 无需处理 |
| **C2** | `read_depth` **实例间不可比**：A1 把 844 B 的 `commands/review.toml` 标 `structure`（内容实为全文可用）；A2 对 79 份 `mcp.json` 标 `full`；A3 为 167/169 `full`。深度标签是自述动作而非证据强度 | 把 depth 当"是否需要回查"的提示：`structure`/`metadata` 行的断言在成为 load-bearing 前必须走该行 `requery`；**禁止跨仓比较 depth 计数或据此评估 A 的质量** | A1 `structure` 174 行与 `docs/skill-anatomy.md` 一类"实际读全但标注更保守"的行；A2 `structure` 234 行与 `metadata` 194 行；A3 仅 2 行 |
| **C3** | **机制粒度按仓而异**：A1 是技能级富枚举；A2 的 `third_party` 是模板级（plugin.json 注册 + mcp.json 传输），权限/scope/门控语义散在 README 行；A3 是标签级 | 机制分组的**单元 = (repo, 机制族)**，必须**合并同族的多行**（`plugin.json` + `mcp.json` + `README.md`，或 `SKILL.md` + 支持文件 + docs 页）后再判覆盖，并在 `source_paths` 记录被合并的路径 | A2 `third_party` 79 组 × 6 文件 = 482 行；A2 各插件的 `SKILL.md`+`agents/`+`hooks/`+`rules/` 组；A1 的 `skills/<name>/SKILL.md` + `references/`；A3 的 `SKILL.md` + `agents/openai.yaml` + `docs/**` |
| **C4** | **重复/复制必须成对消费**：真重复已在 A1 HEADER（5 组 blob sha）与 A2 HEADER（跨插件重复面）记录，但行内不总标注（如 #1、#10）；按行计数会把 1 个机制算成 2–3 个 | 重复对**只算一个机制、保留全部路径**；评估重复对时以 sha256/逐字节比对为证据（本轨已对 #1、#10 执行）；不因"另一份没读"降级覆盖状态 | A1 `commands/*.toml` ↔ `.gemini/commands/*.toml`（5 组）与 4 组措辞分叉；A2 `thermos` ↔ `cursor-team-kit` 的 thermo-nuclear、两处 `pr-review-canvas`、`grok-voice` 未引用 logo；A3 `AGENTS.md` ↔ `CLAUDE.md` 符号链接 |
| **C5** | **A 的"不做判定"纪律在本样本中成立**：18 条中无一行出现 adopt/reject/覆盖/评分语言；A2 HEADER §7 的"事实而非判定"标注清楚；A1 的 `evals/skill-impact.md` 空表被如实记录 | 保留；B 消费时不得把 A 的 `nature` 或 `related_materials` 当作覆盖线索；机制清单的"存在性"需 A 行 + B 回读双重确认（本轨对 39 条 adopt 候选均标注是否已读原文） | 全部 1,240 行 |
| **C6** | **行内断言强度差异**：A1 的 eval 行把 runner 的 owner 排名行为写成机制（"runner 会断言 owner 排名高于本技能"），但 A1 自己标注未实测；A2 的某些行把"服务器/平台侧行为"写成机制（x-money 的 approval 强制力） | 凡机制依赖**未在本轮观察的运行时行为**（runner、hook 强制力、平台门控），coverage 轨记 `pending-check` 或在该行 `uncertainties` 标注"未实测"；不得据此宣布覆盖或采纳 | A1 `evals/cases/**` 25 行、`hooks/**` 9 行、`scripts/**` 14 行；A2 `third_party` 的账户级门控行、`orchestrate`/`ralph-loop` 的 hook 行为；A3 的 `.changeset` 历史条目 |

**需回查的组（数量级，供 Driver 决策是否拆分）**：C1/C2/C3 指向的 A2 `third_party` 482 行与 A1 `evals/**` 82 行是两个最大消费侧风险面；本轨已在 TSV 中以 `PEND-01`（79 connector）与 `PEND-04`（eval runner）保留，不作为 confirmed 覆盖。

## 5 · 计数与未评估项

### 5.1 状态计数（按 `ABSORB-B-MECHANISM-COVERAGE.tsv`，183 行机制）

| 类别 | 数量 | 说明 |
| --- | --- | --- |
| **confirmed covered** | **50** | 当前产品正文有对应判断/操作，basis 指到文件+段落 |
| **confirmed partial** | **55** | 原则/问句在场、操作或条件缺席，`missing_elements` 列出缺什么 |
| **confirmed not-covered** | **70** | 通读 19 文件后无对应正文；多为上游机制面 |
| confirmed 小计 | 175 | = 第(2)类"实质覆盖评估完成度"计数 |
| **pending-check** | **8** | `PEND-01..07` + `EVID-19`；保留了缺什么与原因，**不计入 confirmed** |
| **not-assessed** | 见 5.3 | 未转成机制行的面；不进入任何覆盖状态 |

按来源组（同一行可涉及多仓，故小计 > 183）：

| 涉及仓 | covered | partial | not-covered | pending | 小计 |
| --- | --- | --- | --- | --- | --- |
| A3 单仓 | 30 | 10 | 13 | 2 | 55 |
| A2 单仓 | 9 | 14 | 17 | 4 | 44 |
| A1 单仓 | 2 | 1 | 12 | 2 | 17 |
| A2+A3 | 4 | 13 | 9 | 0 | 26 |
| A1+A3 | 3 | 7 | 8 | 0 | 18 |
| A1+A2 | 2 | 8 | 7 | 0 | 17 |
| A1+A2+A3 | 0 | 2 | 4 | 0 | 6 |

裁定候选分布（`verdict_candidate`）：`none` 37、`narrow` 64、`defer` 39、`adopt` 39、`reject` 4。`none` = 当前文本已足够、本轨不提变更；它不出现在裁定轨正文。

### 5.2 两个完成度分开报告（计划 §4）

- **路径记账完成度**：A 侧 1,240/1,240（100%），本轨仅核对（§1），不重复主张。
- **实质覆盖评估完成度**：**175 / 183 = confirmed 机制**；另有 8 行 pending-check 与 §5.3 的未评估面。
- 本轨**不主张**"覆盖评估已全量完成"，也**不主张**任何采纳；采纳需 §5 全文回读，见 ADJUDICATION §1。

### 5.3 not-assessed（未转成机制行、未进入任何计数）

| 面 | 路径数 | 未评估原因 |
| --- | --- | --- |
| A1 `evals/fixtures/**` 逐 fixture 内容 | 48 | 只读了 1 个 case 与 3 条被 A 标 full 的 fixture；机制层用 `EVID-17` 代表，逐条断言未评审 |
| A1 `evals/plugin/**`（prompt + grader 文本） | 9 | grader 机制在 `EVID-18` 以 defer 处理，文本逐条未评审 |
| A1 `docs/**` 宿主安装指南 | 16 | 宿主安装/接入属平台形态；本轨只评估了 `docs/skill-anatomy.md`（SKL-01） |
| A1 仓库门面与卫生（README、LICENSE、.gitattributes、.gitignore、根 plugin.json、`.opencode/skills` 符号链接，以及 AGENTS/CLAUDE/CONTRIBUTING 的**指令文本面**） | 9 | 门面/指令文本；其机制对应项（调用轴、写作纪律）分别在 AUTH-30、META-01 内以 defer/adopt 处理 |
| A1 hooks 的两个 `*-test.sh` 与 `session-start-test.sh` | 3 | 测试文件；其对象机制在 `FMT-05/07` 内以 pending/partial 处理 |
| A2 测试文件（`*.test.ts`/`fakes.test-helper.ts`） | 32 | 测试文件；对应实现机制在 `PEND-02` |
| A2 资产与许可（PNG/SVG/JPG、LICENSE、CHANGELOG） | 278 | 非机制（`PKG-09` 只评估了政策面） |
| A2 未单列插件（`teaching` 已列、`grok-voice` 已列；`pr-review-canvas`/`docs-canvas` 落到 `DLV-04`/`PKG-10`） | — | 其余 first-party 插件的私有机制未单列，若要做需另开工作面 |
| A3 `docs/**` 其余页与 `.changeset/**` 变更记录 | 25 + 11（另 config.json、README.md） | 机制多已在对应 SKILL 行；docs 页的增量内容（常见问题/"It's working if"）未逐页评审；本轨只读了 `.changeset/retro-deterministic-checks.md` 一条 |
| A3 资产/许可/包管理（LICENSE、package-lock、.gitignore） | 3 | 非机制 |

未评估面**不构成覆盖结论**；计划 §4 要求"组不得整体未判而宣称关闭"，因此上表逐面给出范围与原因，并留给 Driver 决定是否拆分（本轨不自行拆）。

## 6 · TSV 完整性与可复核性

- `ABSORB-B-MECHANISM-COVERAGE.tsv`：1 表头 + 183 数据行；每行恰 9 列（tab 分隔）；无空单元；无重复机制 id。
- `source_paths` 使用 `addy:` / `cursor:` / `matt:` 前缀表示复合键的 repo 部分；以**目录结尾**的引用（6 处：`addy:evals/cases`、`addy:evals/fixtures`、两个 grader 目录、`cursor:cursor-sdk/skills/cursor-sdk/references`、`cursor:pstack/skills/why/references`）表示该目录下 A 索引内的多条记录。
- 全部路径经脚本对三份 A 表逐条校验：**0 条无法解析**（183 行、448 条路径引用）。

## 7 · 边界声明

- 本文件与 TSV **不含采纳决定**，不写 core/product/legacy，不改 UCBIP，不派工，不提交。
- 本文件**不给覆盖率百分比**：无加权标准，只按状态计数（计划 §3）。
- 本文件**不重写 A 的记录**：口径偏差只在 C1–C6 中作为消费侧修正记录，受影响组已列名。
- 本文件**不构成** Owner 决定点之外的动作：是否启动落地、是否拆分 work package，仍由 Owner/Driver（计划 §6）。
