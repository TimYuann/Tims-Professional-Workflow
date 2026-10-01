# ABSORB-A1-ADDY-HEADER · A 类路径发现/索引（addyosmani-agent-skills）

2026-10-01 · tpw-absorb-a1（Pi / deepseek-v4.1-flash / reasoning=max / session `01a0f783-b545-76cd-b6f5-cb72d19d8073`）
工作树：`~/Developer/tim-professional-workflow/.worktrees/night-2026-10-01`（HEAD `b7f6d94c65eb7e971251ee962536510a0c8497f6`）
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
| `read_depth` | **只能是 `metadata` / `structure` / `full`**，按本轮实际动作填写：`full` = 本轮把该文件从头读到尾；`structure` = 读了 frontmatter／标题锚点／顶层声明序列（并可能含为命名机制所需的定向正文段）；`metadata` = 只读树元数据（尺寸/模式/类型）与路径名。本轮 208 行中 `full` 34 行、`structure` 174 行、`metadata` 0 行（每个路径至少读到结构级） |
| `source_mechanism` | 该路径承载的**源机制**（做了什么、按什么规则做、可复用的工作方式），一句到数句；纯数据/fixture 标为其服务的行为 eval |
| `responsibility_loci` | 多标签，逗号分隔，取自责任骨架 A–F（`A` Intent/Outcome、`B` Behavioral Contract、`C` Domain Semantics、`D` Technical/System Design、`E` Implementation、`F` Verification）。**仅作参考标签**，不是判定、不是评分、不是 A–F 执行顺序 |
| `related_materials` | 重复/支持文件与同组材料（逐字节重复对、宿主三态命令、persona↔技能↔命令、hook↔被服务技能、manifest↔版本校验器、case↔fixture、共享清单↔引用技能） |
| `mechanism_lead_and_anchor` | 机制线索 + 定位锚（章节标题／YAML 键／函数名／常量名／表格列头等），供 B 按锚点回读原文 |
| `uncertainties` | 本轮已识别的未决点（未读章节、计数口径冲突、宿主分叉、软约束无机器检查、未实测行为等），**不是缺陷结论** |
| `requery` | 回查入口（具体文件/命令）+ 回查原因 |

## 4 · read_depth 口径的实际落点

**`full`（34 条，本轮读到文件末尾）**：
`.agents/plugins/marketplace.json`、`.claude-plugin/plugin.json`、`.claude/commands/constraints.md`、`.claude/commands/plan.md`、`.claude/commands/spec.md`、`.claude/rules/skills-contributing.md`、`.codex-plugin/plugin.json`、`.gitattributes`、`.github/workflows/test-plugin-install.yml`、`.gitignore`、`.opencode/skills`（符号链接，`readlink` 即其全部内容）、`AGENTS.md`、`CLAUDE.md`、`CONTRIBUTING.md`、`LICENSE`、`docs/agents.md`、`docs/developer-onboarding.md`、`docs/skill-anatomy.md`、`evals/README.md`、`evals/plugin/code-review-fires/graders/{off-by-one,severity-labels,skill-fired}.md`、`evals/plugin/code-review-stays-quiet-on-commit-message/graders/not-fired.md`、`evals/plugin/code-review-stays-quiet/graders/{not-fired,tdd-fired}.md`、`evals/plugin/code-review-stays-quiet/prompt.md`、`evals/skill-impact.md`、`hooks/SDD-CACHE.md`、`hooks/SIMPLIFY-IGNORE.md`、`plugin.json`、`references/orchestration-patterns.md`、`skills/constraint-driven-development/references/floor-guard.md`、`skills/idea-refine/scripts/idea-refine.sh`、`skills/using-agent-skills/SKILL.md`。

**`structure`（174 条）**：其余全部路径。其中：
- 25 个 `skills/*/SKILL.md`：仅 1 个（`using-agent-skills`）升到 `full`——按计划与派单要求，技能读 metadata + 标题结构；未逐行读的正文机制细节**不在**本索引的强度范围内。
- 14 个 `scripts/*.js`：读头注释 + 顶层声明 + 关键常量段（如 `ARTIFACT_ALLOWLIST`、`GUARDED_FILES`、`manifestPaths`、`NAME_MAP`、`COLLISION_*`），未逐行读实现。
- 25 个 `evals/cases/*.json`：读结构化抽取（正/负提示、kind、files[]、expectations 计数），未逐字读全部 `expectations` 文本。
- 48 个 `evals/fixtures/**`：读结构抽取，其中 3 条（`browser-testing-with-devtools/{README.md,server.js}`、`ci-cd-and-automation/src/slug.js`）为 `full`。
- 其余文档/清单/命令载体/hook 脚本/persona：结构级。

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
| `ABSORB-A1-ADDY-INDEX.tsv` | 209（表头 1 + 数据 208） | 列 10、行不空、路径集合与 pin listing 全等；sha256 `213eb4fc817fc52afbed4bad6f69d2fc4c38da5d1763649a5712a84cba5e65ca` |
| `ABSORB-A1-ADDY-HEADER.md` | 本文件 | — |

上游 listing 摘要：`edab716179583a1b7a5f80f490485eabcbca6164e27c1dfe1997e36330fbbb06`（208 行，pin = HEAD = 读取源）。
