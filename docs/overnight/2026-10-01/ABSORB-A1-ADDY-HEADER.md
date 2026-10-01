# ABSORB-A1-ADDY-HEADER · A 类路径发现/索引（addyosmani-agent-skills）

2026-10-01 · tpw-absorb-a1（Pi / deepseek-v4.1-flash / reasoning=max / session `01a0f783-b545-76cd-b6f5-cb72d19d8073`）
工作树：`~/Developer/tim-professional-workflow/.worktrees/night-2026-10-01`（初次写入时 HEAD `b7f6d94c65eb7e971251ee962536510a0c8497f6`；本索引初版已由 Driver 提交于 `4bd5f50`；**§8 修订时 HEAD `a87d82e6da829da30708e417932fec16058008be`**，修订为工作树内未提交修改）
本轮**只读上游**，只写本目录下两份文件：
- `ABSORB-A1-ADDY-INDEX.tsv`（208 数据行 + 1 表头行）
- `ABSORB-A1-ADDY-HEADER.md`（本文件）

依据：`UPSTREAM-DEEP-ABSORPTION-PLAN.md` §1（固定输入与分母）与 §2（A · per-path screen）。
本文件与索引**不是** B 类文档：不构成覆盖率判定，不构成采纳/否决，不给分。

---

## 1 · 固定输入核对（pin 与分母）

| 项 | 本轮实测值 |
| --- | --- |
| locator | `/Users/yuantian/Developer/tim-professional-workflow/.worktrees/legacy-pre-night-2026-10-01/upstreams/addyosmani-agent-skills` |
| 期望 pin | `2686b620fc1fed2e8f60c704839c766b8594c6b6` |
| `git rev-parse HEAD` | `2686b620fc1fed2e8f60c704839c766b8594c6b6` → **与 pin 相等，未停** |
| `git -C <path> ls-tree -r <pin> \| shasum -a 256` | `edab716179583a1b7a5f80f490485eabcbca6164e27c1dfe1997e36330fbbb06` |
| 同上 listing 行数 | **208**（= 期望 tracked 数） |
| `git ls-tree -r HEAD \| shasum -a 256` | `edab716179583a1b7a5f80f490485eabcbca6164e27c1dfe1997e36330fbbb06` → 与 pin listing 同摘要 |
| 工作树状态 | `git status --porcelain` 空（无本地改动，故工作树内容 = pin 内容，读取工作树文件不引入漂移） |
| 权限位分布 | `100644` ×199、`100755` ×8、`120000` ×1（`.opencode/skills` 符号链接 → `../skills/`） |
| 文件类型 | 全部为文本（`file --mime` 检查无二进制/非 UTF-8 项）；扩展名：md 105、js 33、json 32、toml 18、sh 8、yml 2、py 2、tsx 1、patch/diff/html/gitignore/gitattributes/LICENSE 各 1 |

分母对账：本索引数据行数 = 208 = `git ls-tree -r <pin>` 行数；路径集合与 pin listing **逐一相等且无重复**（脚本断言 `path set equal: True`，`dup paths: 0`）。
重建方式即计划 §1 要求的直取 `ls-tree -r <pin>`，未使用 `ls-files`，未生成第二份 1240 清单。

## 2 · 生成方法（实际动作，可复现）

1. **pin 核对**：`git -C <path> rev-parse HEAD`；`git ls-tree -r --long <pin>`；`git ls-tree -r <pin> | shasum -a 256`；`git status --porcelain`。
2. **逐路径结构抽取**（Python，本机一次遍历 208 个文件）：
   - `.md`：YAML frontmatter 的 `name`/`description` 与全部 H1–H3 标题锚点；
   - `.js`/`.tsx`：头部注释块 + 顶层 `function`/`const`/`class`/`module.exports` 声明序列；
   - `.py`：头部注释 + `def`/`class`/常量；
   - `.sh`：头部注释 + 函数定义名；
   - `.json`：顶层键 + `name`/`version`/`description` 等字段；
   - `.toml`：顶层键（`description`/`prompt`）；
   - `.yml`：顶层键；其余（patch/diff/html/LICENSE/gitignore/gitattributes/symlink）：直接读取或 `readlink`。
   该抽取结果用于填 `nature`、`source_mechanism`、`mechanism_lead_and_anchor`。
3. **重复内容证据**：`git ls-tree -r <pin>` 按 blob sha 分组求 >1 成员组 → 仅 5 组真重复：`.gemini/commands/{build,planning,review,spec,test}.toml` 与 `commands/` 同名文件逐字节相同（其余 4 对 only 措辞分叉，已逐对 diff 确认差异点）。
4. **跨文件关系证据**：
   - `evals/cases/*.json` 的 `skill_name` / `trigger.positive[]` / `trigger.negative[].owner` / `evals[].kind` / `evals[].files[]` 结构化抽取，用于把每个 case 与 `skills/<name>/` 及 `evals/fixtures/**` 配对；
   - `scripts/validate-artifact-paths.js` 的 `ARTIFACT_ALLOWLIST` 与 `GUARDED_FILES` 实际常量；
   - `scripts/validate-versions.js` 的 `manifestPaths`；
   - `scripts/validate-commands.js` 的 `DIRS`/`NAME_MAP`；
   - `.claude-plugin/plugin.json` 的 `experimental.evals`。
5. **定向正文阅读**（用于命名机制，非全库通读）：见 §4 的 34 条 `full` 清单；另对 `references/orchestration-patterns.md`、`docs/skill-anatomy.md`、`skills/using-agent-skills/SKILL.md`、`CONTRIBUTING.md`、`hooks/SDD-CACHE.md`、`hooks/SIMPLIFY-IGNORE.md`、`skills/constraint-driven-development/references/floor-guard.md` 等做了分段补齐直至读完全文。
6. **生成与自检**：单次 Python 生成 TSV（列序固定），随后独立校验：行数 209、每行恰 10 列、无空单元、路径集合与 pin listing 全等、`read_depth` 仅取 `metadata|structure|full`。

**本轮未做**：未 fetch / 未安装 / 未起服务 / 未跑测试或 eval / 未执行任何脚本（含 `git` 写操作以外的一切执行）/ 未改 UCBIP / 未提交 / 未派工 / 未写 core 或 product / 未写 `legacy-pre-night-2026-10-01` 工作树。

过程草稿（路径清单、结构抽取脚本与抽取结果）只落在系统临时目录（`/tmp/a1-list2.txt`、`/tmp/a1-digest.txt`、`/tmp/a1gen/gen.py`），不进仓库、不构成交付物。

注：读取期间观察到 `legacy-pre-night-2026-10-01` 工作树本身存在**与本轮无关的既有改动**（`.decisions/ledger.tsv` 与 `docs/history/derivation-0930/` 等）；本轮未对其做任何写入。`upstreams/addyosmani-agent-skills` 读取前后 `git status --porcelain` 均为空。

## 3 · 列义（TSV 10 列，tab 分隔）

| 列 | 含义与填写口径 |
| --- | --- |
| `repo` | 固定 `addyosmani-agent-skills`（复合键 = repo + path） |
| `path` | pin 下的仓库相对路径，逐字来自 `git ls-tree -r <pin>`；每个 tracked path 恰一行 |
| `nature` | 文件性质（技能定义／技能自带参考／persona／命令包装／eval 案例／eval fixture／plugin manifest／hook 脚本／hook 文档／校验器／校验器单测／共享清单／文档／配置／许可／符号链接／CI workflow 等），按后缀与实测内容如实标注，不对资产/脚本/包装按后缀贬值 |
| `read_depth` | **只能是 `metadata` / `structure` / `full`**，按本轮实际动作填写：`full` = 本轮把该文件从头读到尾；`structure` = 读了 frontmatter／标题锚点／顶层声明序列（并可能含为命名机制所需的定向正文段）；`metadata` = 只读树元数据（尺寸/模式/类型）与路径名。**修订后**：208 行中 `full` 52 行、`structure` 156 行、`metadata` 0 行（每个路径至少读到结构级；修订前的初版为 full 34 / structure 174） |
| `source_mechanism` | 该路径承载的**源机制**（做了什么、按什么规则做、可复用的工作方式），一句到数句；纯数据/fixture 标为其服务的行为 eval |
| `responsibility_loci` | 多标签，逗号分隔，取自责任骨架 A–F（`A` Intent/Outcome、`B` Behavioral Contract、`C` Domain Semantics、`D` Technical/System Design、`E` Implementation、`F` Verification）。**仅作参考标签**，不是判定、不是评分、不是 A–F 执行顺序 |
| `related_materials` | 重复/支持文件与同组材料（逐字节重复对、宿主三态命令、persona↔技能↔命令、hook↔被服务技能、manifest↔版本校验器、case↔fixture、共享清单↔引用技能） |
| `mechanism_lead_and_anchor` | 机制线索 + 定位锚（章节标题／YAML 键／函数名／常量名／表格列头等），供 B 按锚点回读原文 |
| `uncertainties` | 本轮已识别的未决点（未读章节、计数口径冲突、宿主分叉、软约束无机器检查、未实测行为等），**不是缺陷结论** |
| `requery` | 回查入口（具体文件/命令）+ 回查原因 |

## 4 · read_depth 口径的实际落点

**`full`（52 条，本轮读到文件末尾）**：
初版 34 条：`.agents/plugins/marketplace.json`、`.claude-plugin/plugin.json`、`.claude/commands/constraints.md`、`.claude/commands/plan.md`、`.claude/commands/spec.md`、`.claude/rules/skills-contributing.md`、`.codex-plugin/plugin.json`、`.gitattributes`、`.github/workflows/test-plugin-install.yml`、`.gitignore`、`.opencode/skills`（符号链接，`readlink` 即其全部内容）、`AGENTS.md`、`CLAUDE.md`、`CONTRIBUTING.md`、`LICENSE`、`docs/agents.md`、`docs/developer-onboarding.md`、`docs/skill-anatomy.md`、`evals/README.md`、`evals/plugin/code-review-fires/graders/{off-by-one,severity-labels,skill-fired}.md`、`evals/plugin/code-review-stays-quiet-on-commit-message/graders/not-fired.md`、`evals/plugin/code-review-stays-quiet/graders/{not-fired,tdd-fired}.md`、`evals/plugin/code-review-stays-quiet/prompt.md`、`evals/skill-impact.md`、`hooks/SDD-CACHE.md`、`hooks/SIMPLIFY-IGNORE.md`、`plugin.json`、`references/orchestration-patterns.md`、`skills/constraint-driven-development/references/floor-guard.md`、`skills/idea-refine/scripts/idea-refine.sh`、`skills/using-agent-skills/SKILL.md`。

修订新增 18 条（§8，均为本轮为补齐适用条件而读完全文）：`
.claude/commands/{build,code-simplify,review,ship,test,webperf}.md`、`commands/{build,code-simplify,review,ship,test,webperf}.toml`、`.gemini/commands/{build,code-simplify,review,ship,test,webperf}.toml`。其中 `commands/ship.toml`↔`.gemini/commands/ship.toml` 与两处 `webperf` 采用「全文读其一 + 逐字 diff 全部差异」的方式确定全文；`review`/`test`/`build` 的 TOML 对经 diff 确认逐字相同。

**`structure`（156 条）**：其余全部路径。其中：
- 25 个 `skills/*/SKILL.md`：仅 1 个（`using-agent-skills`）为 `full`——按计划与派单要求，技能读 metadata + 标题结构；修订时按 `## When to Use` 锚点补读了适用/排除条件（§8），但正文仍未逐行读，未读正文的机制细节**不在**本索引的强度范围内。
- 14 个 `scripts/*.js`：读头注释 + 顶层声明 + 关键常量段（如 `ARTIFACT_ALLOWLIST`、`GUARDED_FILES`、`manifestPaths`、`NAME_MAP`、`COLLISION_*`、修订补读的 `REQUIRED_SECTIONS`/`SECTION_EXEMPT_SKILLS`），未逐行读实现。
- 25 个 `evals/cases/*.json`：读结构化抽取（正/负提示、kind、files[]、expectations 计数），未逐字读全部 `expectations` 文本。
- 48 个 `evals/fixtures/**`：读结构抽取，其中 3 条（`browser-testing-with-devtools/{README.md,server.js}`、`ci-cd-and-automation/src/slug.js`）为 `full`。
- 6 条 TOML 指针行（`commands/`、`.gemini/commands/` 的 `constraints`、`spec`、`planning`）为结构级，其适用条件以同族 `.claude/commands/*.md` 行为可读正文（已在行内标注该口径）。
- 其余文档/清单/hook 脚本/persona：结构级（4 个 `agents/*.md` 已按 `## Rules`＋`## Composition` 锚点补读）。

## 5 · 限制（本索引不能主张什么）

1. **不含判定**：无 per-file 总分、无 high/medium/low、无 adopt/reject/narrow 建议、无覆盖率百分比。本文件与索引**不产生** coverage verdict，也不参与 B 的机制级覆盖评估。
2. **机制命名有粒度误差**：174 条为结构级，`source_mechanism` 来自 frontmatter + 标题锚点 + 顶层声明；`Common Rationalizations` 表格内的具体反驳条目、正文中段的条件/反例细节未纳入。
3. **未实测**：本轮未运行任何脚本、eval、校验器或 hook；凡涉及"行为"的描述均来自源码自述注释与 CI 调用点，不是本轮观察结果。Tier 2/3 与 plugin eval 的实际结论不在本索引内。
4. **未读章节**：部分文档的少数小节仅见标题（已在对应行的 `uncertainties` 逐条标出，例如 `docs/advanced-per-agent-configuration.md` 的 `Status`、`docs/copilot-cli-setup.md` 的 "What you get, and what you don't"、`docs/opencode-setup.md` 的 `Limitations`、`docs/antigravity-setup.md` 的 `Verification & Validation`）。
5. **已识别的口径冲突（不代 B 裁定）**：技能计数 25（`skills/` 目录与 README/CLAUDE.md）对 24（`.codex-plugin/plugin.json` 的 `longDescription`）；`evals/skill-impact.md` 机制已声明但表体为空；`.claude/commands/constraints.md`、`commands/constraints.toml`、`.gemini/commands/constraints.toml` 第 6 步的 harness 指引目标各不相同（CLAUDE.md ／ AGENTS.md+CLAUDE.md ／ AGENTS.md+GEMINI.md）。
6. **仅覆盖一个 pin、一个仓库**：本轮只处理 `addyosmani-agent-skills`（A1 分工）；`cursor-plugins`、`mattpocock-skills` 不在本索引内，1240 总分母由各实例分头对账。
7. **证据可复核性**：`evals/results/`、`evals/plugin/results/` 与两个 hook 缓存目录均在 `.gitignore` 中，故本索引引用的"实测数字"（如 evals/README.md 的触发率）只能是文档叙述，不能从库里复核。

## 6 · 声明（边界）

- 本索引**无评分**：不含权重、总分或等级标签；`responsibility_loci` 的 A–F 仅作参考标签。
- 本索引**无采纳**：不主张任何路径/机制应被吸收、扩展或落地；不构成 §5"实际采纳"所需的全文阅读、保留/变更/删除记录或落点建议。
- 本索引**无否决**：不主张任何路径/机制应被排除、降级或延后。
- 计数与完成度口径：本文件只报告**路径记账完成度 100%**（208/208 tracked path 有行）。它**不报告**实质性涵盖评估完成度——后者只能由 B 以"已确认状态（covered／partially covered／not covered + 依据）"计数得出，且 `pending-check` 不计入。
- 阅读顺序不作为否决：本轮未设阅读顺序，也未以文件类型、后缀或包装形态对任何路径降权。
- 接收方可据此索引定位与回读，不可据此索引宣布覆盖或采纳结论。

## 7 · 本轮产出指纹

| 文件 | 行数 | 说明 |
| --- | --- | --- |
| `ABSORB-A1-ADDY-INDEX.tsv` | 209（表头 1 + 数据 208） | 列 10、行不空、路径集合与 pin listing 全等；sha256 `abef7e2a7d173f951e595dec6891a024ba450772974d2329dc85f3b9c8ed62a3`（修订后） |
| `ABSORB-A1-ADDY-HEADER.md` | 本文件 | 含 §8 修订记录 |

上游 listing 摘要：`edab716179583a1b7a5f80f490485eabcbca6164e27c1dfe1997e36330fbbb06`（208 行，pin = HEAD = 读取源）。

---

## 8 · 修订记录（补适用条件/例外）

**触发**：`ABSORB-FULL-CORRECTION-BRIEF.md` §1（Pro RETURN + full-correction brief）与 tpw-night-driver 的补正指示。
**基线**：修订前版本＝提交 `4bd5f50`（Driver 所提交的 A1–A3 路径索引）；本修订只动 `ABSORB-A1-ADDY-INDEX.tsv` 与 `ABSORB-A1-ADDY-HEADER.md`，未提交、未改其他文件。
**问题类别**：`/ship` 行保留了并行评审流程，却**漏记上游 Rules 中允许跳过扇出的适用条件**；同类的「结构级读取丢失适用条件/例外」需要一并自查。
**回读源确认**：pin 仍为 `2686b620…`（`git rev-parse HEAD` 相等，`git status --porcelain` 空），逐字重读 `.claude/commands/ship.md`、`commands/ship.toml`、`.gemini/commands/ship.toml`。

### 8.1 遗漏的具体条件（`## Rules` 第 5 条，三宿主逐字相同）

> Skip the fan-out **only if all of the following are true:** the change touches **2 files or fewer**, the diff is **under 50 lines**, and it **does not touch auth, payments, data access, or config/env**. Otherwise, default to fan-out. `/ship` is designed for production-bound changes — when the blast radius is non-trivial, run the parallel review even if the diff looks small.

同节其余未被记录的规则也已补入：第 3 条（**回滚计划是任何 GO 的强制前置**）、第 4 条（任一 persona 报 Critical 则**默认 NO-GO**，除非用户明确接受风险）。

### 8.2 本次修订改动的行（45 行，全部有源锚可核）

| 组 | 行数 | 补入的适用条件/例外 | 源锚 |
| --- | ---: | --- | --- |
| `/ship` 家族（3 宿主） | 3 | Rules 1–5，含跳扇出三条门槛（≤2 文件 ∧ <50 行 ∧ 不触及 auth/payments/data access/config-env，须同时成立）；非平凡爆炸半径一律跑并行 | `## Rules` 第 5 条 |
| `/webperf` 家族（3 宿主） | 3 | 作用域排除（不得用于工具库/CLI/无浏览器面向输出的服务端代码）；Deep 六类激活输入；Quick 为默认且每条发现标 `potential impact`；单 persona 无合并步 | 首段排除句 ＋`## Determine the mode`＋`## Output` |
| `/code-simplify` 家族（3 宿主） | 3 | 默认作用域＝最近改动的代码（除非显式给更大范围）；六步流程；**测试失败即回退该次改动** | 正文 1–6 步＋末段 |
| `/review` 家族（3 宿主） | 3 | 五轴逐条判据（安全→security-and-hardening，性能→performance-optimization 的委派）；分级 Critical/Important/Suggestion；输出须含 `file:line` 与修复建议 | 五条轴＋分级句＋输出句 |
| `/test` 家族（3 宿主） | 3 | 新特性 3 步；缺陷 Prove-It **5 步（含先确认测试失败）**；浏览器相关须一并调用 browser-testing-with-devtools | 两段流程＋末段条件分支 |
| `/build` 家族（3 宿主） | 3 | 模式判定 `auto`/`all`；自主模式 7 步及其全部停机条件（spec 白名单、基线清洁、单检查点、`git add -A` 禁令、三类必停情形） | `## Modes`＋`## Autonomous` 1–7 步 |
| 4 个 `agents/*.md` | 4 | `## Rules` 全文（含『绝不建议关闭安全控制』『只在系统边界打桩』『不把实验值当字段值』『不纳入 /ship 扇出的理由』）＋`## Composition` 三条（直调条件/经何命令/**不得由其他 persona 调用**） | `## Rules`、`## Composition` |
| 14 个 `skills/*/SKILL.md` | 14 | `## When to Use` 的适用前提与 **`When NOT to use` 排除清单**（如 browser-testing 的『纯后端/CLI/非浏览器代码』、code-simplification 的四条、interview-me 的五条、observability 的三条指向别的技能等） | `## When to Use` |
| 2 个无 `## When to Use` 的技能 | 2 | 记录其**豁免来源与真实适用面**：`idea-refine`（legacy 结构，触发面只在 frontmatter description）与 `using-agent-skills`（元技能，适用面＝`Skill Discovery` 决策树） | `scripts/lib/skill-lint.js` 的 `SECTION_EXEMPT_SKILLS` |
| 6 条 TOML 指针行 | 6 | `constraints`/`spec`/`planning` 的 TOML 侧适用条件指向同族 `.claude/commands/*.md`（并标注该口径为跨格式引用、未逐字 diff md↔toml 正文） | 同族 `.claude` 侧正文 |
| `scripts/lib/skill-lint.js` | 1 | `REQUIRED_SECTIONS`（5 个必备章节）与 `SECTION_EXEMPT_SKILLS`（仅 2 条豁免及理由，豁免写在 linter 内以防贡献者自改绕过） | 同名常量 |

合计 **45 行**（18 行机制整体重写 ＋ 27 行追加），其余 163 行逐字节未改。

### 8.3 修订中的顺带发现（不代 B 裁定，只记证据）

- **严重度词表三处不一致**：`/review` 命令要求 Critical／Important／Suggestion；`agents/code-reviewer.md` 模板用 Critical Issues／Required Changes／Optional／Nits；`evals/plugin/.../severity-labels.md` 正则只接受 Critical|Required|Nit|Optional|Consider|FYI（`Important`/`Suggestion` 不被命中，只有 `Critical` 有交集）。
- **`/ship` 与 `/webperf` 的组合理由**：`agents/web-performance-auditor.md` 的 Composition 明写本 persona **不纳入 `/ship` 扇出**（性能审计只适用 Web 应用，放进全局发布前扇出会在非 Web 项目产生噪音）。
- **宿主分叉（已逐字比对）**：`commands/webperf.toml` 对 CrUX 密钥有『须用 `$CRUX_API_KEY`/`$GOOGLE_API_KEY` 且不得硬编码进配置文件』的约束，`.gemini/commands/webperf.toml` 无该约束；`constraints` 第 6 步的 harness 指引目标在 Claude／Antigravity／Gemini 三处各不相同（此前已记）。

### 8.4 本次修订的残留（未在本次补正范围内）

- 25 个技能**正文**（Common Rationalizations 条目、Red Flags、Verification 具体项）仍未逐行读；本索引对技能的强度仍止于结构级＋适用/排除条件。
- `docs/*.md` 与 `references/*.md` 的少数小节仍仅见标题（`uncertainties` 已逐条标注）。
- `commands/`、`.gemini/commands/` 的 `constraints`/`spec`/`planning` 三族 TOML 正文未逐行读，其条件表述以 `.claude` 侧为可读正文（已在行内标注）。

### 8.5 修订后的边界声明（与 §6 一致，未放松）

本次修订只**补记适用条件与例外**，仍不评分、不采纳、不否决；不因补记了『跳扇出门槛』而对任何机制形成裁定或落地建议。
