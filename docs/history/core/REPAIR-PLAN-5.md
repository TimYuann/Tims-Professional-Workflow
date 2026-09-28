# 引入方式、脚本闭环、技能压缩与四范式 · 最终判断

**状态：独立结论与最小修订建议，不是实施许可。** 本轮只写此文件。依据为当前工作树 `AGENTS.md`、`README.md`、`pipeline.md`、10 个 `roles/*.md`、`scripts/` 实际文件、`SOURCES.md §1–9`、八份 `docs/archive/skills/*/SKILL.md`；证据方的 `.pi/investigation/FOUR-PARADIGMS.md` **在本轮取证时尚未出现**，以下范式判断依已核原文与现行角色作出，日后出现须比对而非自动改判。此前 `.pi/investigation/AB-SPEC.md` 的 A/B 已获 Owner 确认，沿用；不重议。

**Owner 最新约束优先**：本轮及今后的规范/脚本方案**不使用 `/tmp` 或 private tmp**；需留档的东西一律放在已获授权且可跨会话取回的 B 位置，临时工作也不得默认落在 tmp。A↔B **只映射位置/载体，不映射流转纪律**；历史文档**不删、不压缩、不套现在的交接规则**，只更新指向历史原件的入口指针。前一版 `.pi/core/REPAIR-PLAN-4.md` 对历史记录“保留到依赖解除”的建议与新裁定不符，**本方案明确撤回这一建议**；现存旧内容保持原样。现行角色与脚本里出现的 `/tmp` 属待修冲突，不因本方案写了禁止就自动消失。

## 1. 结论一：引入方式的正确骨架与三处不成立

**正面判断：Owner 说的“完整注入角色正文→加本轮任务和工具→开独立会话”是正确骨架；“复制粘贴整个库 + 若干 skill 就自动闭环”在当前仓库不成立。**

- 当前库的**运行单元**是 `roles/<role>.md` 全文；Driver 还读 `pipeline.md`（`AGENTS.md` 原则 1–3、`README.md:27-41`）。角色文件只给第 1–2 层，Driver 必须附第 3 层**已批准的本轮切片/收据/范围/写窗**与第 4 层**该宿主真实可用的工具、可写产物位置与可执行命令**；让新会话自己猜 A/B 位置、授权或隔离方式不算自包含。若宿主的“初始用户消息”不具备稳定的规则注入效力，**只把全文贴进普通对话并不足以保证行为约束**：须用该宿主真实的角色/高优先级配置通道，验证它被完整读取；方式与命令属第 4 层，不固化进库。Reviewer/Verifier 必须处于**与实现该候选者不同**的会话；会话能启动不等于有已冻结输入或独立判断。
- **库并非现成的 role+skill+script 三套运行件**：当前 `skills/` **没有可用目录/文件**，Git 原位的 8 个 `skills/*/SKILL.md` 在当前工作树均标删除，保留的 8 份只在 `docs/archive/skills/`（`SOURCES.md §7–8` 明言“以技能目录为载体不吸收”）；当前可用方法在**10 个角色正文**，不是八个可以随角色调用的 active skill。与此同时，薄流程 `pipeline.md`、字段闭环 `closure.md`、身份规则 `identity.md`、上游来源 `SOURCES.md`、库版本 `VERSION` 都不能从“角色/技能/脚本三项”中凭空推得。
- **“复制粘贴过去”与已生效的下游绑定规范直接冲突**：`AGENTS.md:59` 禁下游使用复制品或可变分支，要求固定 release commit、实际读取对象与 pinned commit 一致且 checkout 干净。复制一份散落到目标仓，改坏后既没有回指 commit 的可复算关系，也不知哪个角色/脚本来自哪个发行对象；上游后续改动不会自动到复制品。**推荐**下游指向同一个经发布、干净的只读库快照（固定 commit；具体可为既有供应方式），Driver 在每次装配记录该 commit 与读取状态，只传本轮需要的角色全文及 B 的已解析指针；底座可以把文本送入会话，**送文本不等于把源库拷成可随意改的第二套规范**。下游改行为应回本库升版本、或由 Owner 明示批准项目扩展且不能改不可映射纪律；升级时看锁定 commit 间角色/脚本/收据差异，重跑本库结构检查与一次真实冷启动，变更前旧判断不自动延续。当前**没有**发布/消费侧自动漂移检测器（`AGENTS.md:59` 已明说），因此不能声称“复制/固定 commit 自带升级闭环”。本轮 `git status` 仍显示多个角色与 AGENTS/README 有未提交改动、`skills/` 原位删除等，**当前工作树尚不能冒充一个已发布且干净的下游快照**；须由库维护者按授权完成版本/发布与绑定验证后才可供下游按此方案引用。

**最小接入说明建议**：在 `README.md:13-41` 加一段：
> 下游引用固定且干净的 TIM commit；Driver 读该快照的 `pipeline.md` 与自己的 `roles/driver.md`，核目标仓 B 映射、授权与四个运行原语。派会话时完整注入目标角色文件的第 1–2 层，并附已批准任务/交接物的第 3 层和本宿主真实可用工具/存放位置的第 4 层；角色需要的技能若已写在正文里，不依赖另装旧 `docs/archive/skills/`。仅在脚本真实需要且获准使用的环境里按角色约定调用；每次运行把命令、对象和输出写回既有收据。引用不是复制发行包；升级另核 pinned commit 与实际运行字节。
**判否**：仅把 `investigator.md` 路径或摘要发给会话，或拷归档 skill 不附冻结卡/写窗，不能称成功启动；复制到 B 后随意改角色仍声称“跑的是 TIM commit X”应被对象核对驳回。

## 2. 结论二：7 个文件≠7 个可执行脚本；调用闭环当前没有闭上

`find scripts -maxdepth 1 -type f` 得到 **7 个文件 = 6 个可执行程序 + 1 个 TSV 表头模板**。10 个角色文件中，`rg 'scripts/|check-library|ws-identity|identity-selftest|log-decision|render-ledger|sync-upstreams|decision-log-template' roles/*.md` 仅 **`roles/ledger-custodian.md` 1 个角色显式引用 `scripts/render-ledger.py`**；其余 9 个角色没有点名任何脚本。六个身份使用者内联的是**算法与交接判据**，并未依赖 `ws-identity.sh` 名称；Verifier §4.8 规定 append-only 台账，但未点名 `log-decision.sh`。这不自动算错误——工具无关是刻意设计——但足以否定“贴脚本过去，何时用、谁用、写哪里就自动闭环”。

| 实物 | 当前调用者/事件、输出 | 未闭合点；建议的**最小**接法与失败门 |
|---|---|---|
| `scripts/ws-identity.sh` | `identity.md:90-95` 列 `manifest/digest/compare/verify`，六角色正文仅内联规则；输出是 `ws:v1` 清单、摘要/比对读数。 | Driver 第 4 层在**无 Git 版本历史**且本轮有该工具时点名“事前基线 manifest → Implementer 定稿 manifest/digest → Reviewer/Verifier/Integrator `verify`”（按收据与写窗）；分别存 `candidate.base/tree`、`review-verdict.object/coverage`、`verification-evidence.object/commands`、`integrated-baseline.base/tree`，**连同清单和 scope 在 B 获准位置**。`compare` 只比文件，不替 `verify` 重算当前源；工具失败/清单缺失 → 身份主张 `UNVERIFIED`、停晋升。若有干净 Git 对象身份，**不强求** ws 工具。当前脚本 `mktemp`（`:78,148`）未经改造可能用 tmp；Owner 禁令下暂**不得运行这个实现**，先使其仅在获准的非 tmp 工作区产生临时排序文件并核删除不碰承重清单，或给同效实现经夹具验过后再放行。 |
| `scripts/identity-selftest.sh` | `identity.md:95` 标正负夹具；`scripts/check-library.py:699-707` 的 G2 间接调用；输出测试读数。 | **维护者/本库 identity 变更时**（或库级检查触发）运行，读数进入本批库级自检报告，不进入下游产品 `verification-evidence`。非零→本库身份工具不可放行；`check-library` 绿≠产品行为 PASS。它的 `WORK="$(mktemp -d)"` (`:29`) 同样违反 Owner 最新禁令；未改成获准非 tmp 工作区且复测前，**不要运行 `identity-selftest.sh` 或会间接运行它的 `check-library.py`**。 |
| `scripts/check-library.py` | `AGENTS.md:63`、`README.md:65-75` 指派**本库维护者**在库角色/契约/来源变动后调用；结果只证结构，且间接运行上行 selftest。 | 把退出码、失败检查项与对象放在本库改动报告/`ledger-input` 的可读证据指针，不冒充任何项目候选的 `PASS`。非零阻断本库该批完成（或注明未通过/不能交付）。在 tmp 禁令解除**实现层冲突**前不能运行默认组合命令并声称遵纪。下游一般无需拷贝/运行该脚本。 |
| `scripts/render-ledger.py` | **唯一明确的角色调用**：`ledger-custodian.md:47-56` 接 `ledger-input` 后先生成、再 `--check`；`ledger-report.region_diff/broken_keys/moved_steps/regenerated_at` 已接住读数。 | 本库每批改动落盘后按现有 A3 触发；正常模式**写 `SOURCES.md` 生成区**，`--check` 只读；生成失败/缺 key 不准声称“已同步”，Driver 收到 broken keys 停库批次收口。**只属于本库来源账**；下游 B 没有 `SOURCES.md`，A3 在下游 N/A（见 `.pi/core/REPAIR-PLAN-4.md`），不得造一个。 |
| `scripts/log-decision.sh` + `scripts/decision-log-template.tsv` | `roles/verifier.md:207-220` 要决策表，脚本用法收文件路径与六栏，首次使用**自己写表头**；模板只是同样列的参考数据，**并不被脚本读取或调用**。 | Driver 为长期/自主批次在既有 B 位置指定一个**独占写者**的台账并把路径经第 4 层给需记决策的角色；Verifier 若本轮用此脚本，就在 §4.8 的自身决定中触发，行与核账结果进 `verification-evidence`/Driver 的本批过程记录；脚本非零、证据指针无效/并发多写者，不得宣称“决策已归档”，Driver 在 roundup 限缩记录完整性。短任务可用已有收据而**不强制 TSV**。脚本头部示例 `:8` 用 `/tmp/run.log`，需先改为获准 B 路径；脚本接任意路径、会 `mkdir -p` (`:20-26`)，**当前缺路径授权校验和单写者保证**，由第 4 层及写窗显式保证，不把 shell 的退出 0 当审批。 |
| `scripts/sync-upstreams.sh` | `AGENTS.md:59` 指本库维护者 Layer 1 上游检查；**没有任何角色文件引用**；输出 upstream 差异摘要、当前 clone 提交。 | **库维护操作，不随下游工作流启动。** 即使默认文案写“read-only”，代码 `:39` 仍 `git fetch origin`，会有网络/修改本地 `.git` 元数据；`--pull` (`:56-62`) 会改上游 clone，违反本库现行上游只读边界，且不能当“只读”或自行运行。要用须先与 Owner 批准的上游同步方式一致：把检查与更新分开，前者只查看已有快照，更新在获准隔离 clone/写窗做，差异/出处落本库 `SOURCES.md` 人写列；异常/未读正文不得列“已吸收”。**不可复制下游再让其跟踪可变上游。** |

**最小修改范围**：在 `roles/driver.md §4.3/§4.4` 的第 4 层工具安排写一条“触发→角色→B 目录→现有收据字段→失败退回”的分派要求；`identity.md §6` 和六个身份角色的**已有 §3 object/§4 身份步骤**各只补一句“有获准 ws 工具时可运行 `verify`，失效按角色现有缺件处理”，其算法仍自包含、无需强行每人读脚本；`roles/verifier.md §4.8` 补可选 logger 的 B 位置/单写者/失败去处；`roles/ledger-custodian.md §4.1` 维持现有；`README.md`/`AGENTS.md` 把本库工具与目标项目工具区分、目录列全 `render-ledger.py`；`scripts/ws-identity.sh`、`identity-selftest.sh`、`log-decision.sh` 的 tmp 与路径边界先按 Owner 新纪律调整。每条变化记 `SOURCES.md` 本库自定/真来源，运行结构检查需等非 tmp selftest 可安全执行。**不新增脚本分发状态机。**

## 3. 结论三：“八九个 skill 太少吗？”——数量不构成证据，当前运行中是 **0**

当前 `git ls-files 'skills/**'` 在工作树已全部标删除，`find skills …` 无运行文件；`docs/archive/skills/` 有 **8 份历史 skill**。三上游实物本轮只读计数：`find upstreams/{cursor-plugins,mattpocock-skills,addyosmani-agent-skills} -name SKILL.md` 各约 **90 / 38 / 25**（总 **153**，含 cursor-plugins 多个插件、非全是本任务已读/已吸收的方法），不是“153→8 的一对一打包”。当前 `SOURCES.md §1–3` 有 **约 168 行**被标保留/改写/局部吸收的上游引文条目（本轮按表格第三列统计，`同上` 归前源），落在角色及少数脚本；**来源行数≠独立技能数**。`SOURCES.md` **没有对这 8 个旧 skill 逐件建“直接映射了几条”**，只在 `§8` 总体说已归档。下面数字是*按相关上游家族关键词关联的引文行数*，跨组可重叠，不是“这份旧 skill 的覆盖率/证明已完整搬运”：

| 历史 skill（非现役） | 原意与现役大致落点；SOURCES 相关条目（启发式） |
|---|---|
| `professional-workflow` | 旧 Driver 入口/装配，相关 pstack `figure-it-out`、Matt `grilling`、Addy `interview-me` 等 **~12 行**；现 `roles/driver.md` + `pipeline.md`。旧文写越权试验/固定九角色，**不能原样恢复**。 |
| `system-tracing` | pstack `how`（真实路径）+ `why`（历史意图）**~18 行**，分别在 Investigator §4.3/§4.4；原件的未核 Dex 归因不是新增可信来源。 |
| `causal-diagnosis` | Matt `diagnosing-bugs`、pstack `attack-the-premise`、Addy 调试来源 **~16 行**，现 Investigator §4.1–4.6；旧件把“确定性”和第三个补丁绝对化、带缺失模板引用，不应再注入。 |
| `interface-and-boundary-design` | pstack `architect`、Matt `codebase-design`、Addy `api-and-interface-design` **~27 行**，现 Architect §4.1–4.9；业务词义 Owner 裁定，不能靠复制旧 skill 代签。 |
| `decision-grilling` | Matt `grilling`、Addy `interview-me` **~10 行**，现 Driver §4.1 与 Oracle 的独立复核**不同权责**；旧文“所有决定显式 YES 才能继续/可交 Oracle 代 Owner”不适用于已授权可逆部分。 |
| `behavioral-tdd` | Matt/Addy TDD、Addy incremental、pstack `test-behavior` **~19 行**，现 Driver/Planner 判据与 Implementer §4.2/§4.3；旧 skill 混写 BDD/TDD，没有 Owner discovery/独立验收完整链。 |
| `adversarial-review` | pstack `interrogate` + Addy `doubt-driven` **~13 行**，现 Reviewer §4.1–4.7；旧件声称 Matt 双轴虽形似，`SOURCES.md:183` 对 Matt `code-review` 当轮记 NOT ABSORBED，**不能声称其原文已吸纳**；旧 P0/P1/P2 与现三态/两轮停止非同一约束。 |
| `blast-radius-proof` | pstack `blast-radius` + `prove-it-works` **~10 行**，现 Verifier §4.3/§4.6/§4.7；旧件四档“最高”与当前五档不一致。 |

**正面判断**：八份归档 skill 的数量既不“太少”也不“已经足够”：**它们已不参与执行**。按旧件划分看，`system-tracing` 的 how/why、`behavioral-tdd` 的需求行为发现/TDD 循环、`decision-grilling` 的 Driver 问权/Oracle 独立裁，是**应该按不同触发与权力边界分开**的；现行角色节已分开，故不必为这三个分法重开 SKILL 文件。反过来“很多上游各有一份 skill”但消费方/触发/判据完全一样的，如两个测试先行变体、不同上游的浅模块警告，应在**一个角色方法节**保留单一被裁版本，而非两份重复规范。**不存在“现役技能之间仍该拆/合”这一当前事实**，因为现役为零；新缺口（如完整 feature-map 生成与维护）是否需要独立 skill，要看它能否作为**非必需、按条件加载**的能力、是否有独立触发/产出/维护人，不能以“要凑到 20 个”为理由。

**压缩的判据**：只吸收**读过正文且有任务消费方**的机制；按行为/风险触发而非上游文件数；每项有明确做什么、何时不适用、失败如何判、谁生产/谁独立判断、一个权威位置与来源裁决。**数量少不是独立优点**；错误地并合不同决定者会破坏权责，过细拆分则让一次任务读多份同义规则、导航与同步成本失控。Owner 说“保留十几二十个，只要绑定在角色文件并自包含”——**有条件成立**：可把完全独立、仅按需触发的技术参考作为可选 skill；但角色**单文件必须能完成其必需主任务和安全边界**，不能靠“skill 同时已复制过去”替代核心方法；Driver 第 4 层须给位置/版本/触发，角色里用**条件明确的一行指针**而非把二十份正文都塞进去。否则每个会话的常驻上下文和旧版/新版维护面都膨胀，跨角色共用同义规则会漂移；若还采用“随意复制技能文件”，又直接违反固定 commit。要增加先证明某项自成独立消费场景且角色冷启动不读它也能完成基本交接，再评估加载预算/缺件 fallback，非以数量为验收门。

## 4. 四套开发驱动范式的最终归属（不是四个新 skill/四个机械关卡）

| 范式 | 正式由谁承担、做什么 | 与其余三者的真实区别 |
|---|---|---|
| **BDD：行为驱动** | **Owner/获权业务人**决定用户可见行为与变更前提；**Driver** 用具体例子对齐与传授权，**Planner** 把例子变成 `slice-plan.verification` 的可判否正反读数（无 Planner 时由 Driver 代产完整片）；**Implementer** 将约定行为自动化、按接缝实现；**Reviewer** 独立挑战行为前提及判据区分力，**Verifier** 从真实用户入口给对象/环境绑定的三态证据。 | 它跨**业务发现→具体例子→可执行验收→实现**，不等于只写 Given/When/Then 文件，也不等于 TDD 的局部代码循环。Driver/Reviewer 可以提出“该不该有这行为”，但不能代 Owner 定业务语义。 |
| **TDD：测试驱动** | **Implementer 是红→绿→重构的唯一实现主责**（`roles/implementer.md:107-140`）；缺陷路径由 **Investigator** 先建对原症状判红的复现回路并交固定输入/红点，Planner 定适当接缝，Reviewer/Verifier 独立检“检查能抓错”但**不**替作者做绿/重构。 | TDD 解决“下一小块代码如何由先红的检查牵引”；可以用于非 BDD 项目。Investigator 的诊断 RED 是供料，**不是第二位 TDD 实现者**。 |
| **DDD：领域驱动设计** | **Architect** 建模、查证词义与上下文边界、提出备选并记录**已由 Owner/获权业务角色决定**的含义（`roles/architect.md:201-217`）；**Investigator** 保留现场原话/旧意图，**Planner** 不在未定含义上切片，**Implementer** 把接受的模型/不变量体现在代码，Reviewer 守冲突。多个业务上下文同名词应注明各自作用域，不能强行全局统一。 | 解决“某个领域概念/边界是什么”，且模型在实施后也可依法演化；不是所有局部任务必须先建 glossary/ADR，也不仅是前置输入。业务裁定权**不因 Architect 会写文档而转移**。 |
| **SDD：规格驱动** | **Owner/Driver** 保证项目既有规格或 `owner-brief`/`task-card` 说明获准的 what/why 与边界；**Architect** 在适用时给 `design-proposal` 的设计约束/how（它**不是**完整产品 spec），**Planner** 将冻结契约转可实施的有判据切片，**Implementer** 对合同实施；Reviewer/Verifier/Integrator 对精准对象与本轮契约检查，发现规格错误回 Driver 追原批准而非改绿后自认成立。 | 解决“需求/规格如何先于方案、持续成为本轮实施与验收的依据”；不代表必须新建长期 `SPEC.md`，也不与 TDD/BDD 排斥。默认小任务可用现有薄契约；是否做长期 spec-anchored 是独立产品维护决定，不由方法名推导。 |

**不是集合图**：BDD 从 TDD 教学演化而范围扩到需求发现与自动验收，但 TDD 可以独立运作；SDD 也包含后续规格核验，DDD 包含实现期模型演化，不能贴“DDD/SDD 只输入、BDD/TDD 只证明”。四者在**业务例子、领域含义、冻结规格、先红反馈**四个问题上交叉，按任务需要调用相应角色已拥有的方法，不新添四个同名技能文件。

**BDD 删测试冲突的排他裁决**：Dan North 的 [BDD 原文](https://dannorth.net/blog/introducing-bdd/) 确实说“行为前提已变→Delete the test”；这句话的条件是**行为本身经证实不再应成立**，不是“现有实现未满足旧行为”。在本库里，**只有项目 Owner 或其明确授权的业务决定者**能宣布**业务前提**已变；Driver 传达并核授权，Architect/Planner 呈现影响并修订设计/判据（依相应职责），Implementer 在**新授权写窗**改/删过时断言并生成**新候选与冻结**，Reviewer/Verifier 独立核“原前提确已失效、替代判据抓得住错实现”，旧结论和历史指针保留。Oracle 可复核**已冻结**范围内争议，不凭专业判断取得 Owner 业务改规权；Driver 若**本人正是 Owner**可用 Owner 身份决定，但需把授权原文与生效对象记清。未有这条业务决定、只因测试红而删断言，仍是当前 `roles/implementer.md:203` 所禁止的**为了变绿削弱检查**。技术性过时断言（例如测试夹具证明不了原行为）也由 Planner/Reviewer 对照原契约提出，若触及业务答案仍回 Owner，不靠实现者“前提变了”的自述单方面改变验收。

## 5. 建议修改与冷启动反例（仅方案，不直接修现行文件）

1. **接入说明**：`README.md:13-41`、`AGENTS.md:59`：指明**按固定干净 commit 引用→Driver 分层注入→下游不得复制版替代 pin→升级单独验**；正例新会话拿到完整角色+已授权卡+项目 B locator；反例只给旧归档 skill/只给文件路径/未锁定来源不通过。影响 Driver、下游绑定人；SOURCES 只记录这条**本库接入规则**，不虚构上游命令。
2. **工具表与临时禁令**：`README.md:50-59`/`identity.md:90-95`/`roles/driver.md §4.3`、`roles/verifier.md §4.8`、`roles/ledger-custodian.md §4.1`、`roles/reviewer.md:51,108`、`pipeline.md:108`、`scripts/{ws-identity.sh,identity-selftest.sh,log-decision.sh}`：采用上表**触发→操作者→对象/收据→失败**；现行 Reviewer/pipeline 写的“`/tmp` 仅临时可用”也须改为**不得作为本轮写入位置**（原有证据失效与复用判据不放宽）；把非留档内部临时文件改到获准的非 tmp 工作区，日志示例不用 `/tmp`。负例未获准目录/意外默认 tmp/不存在的证据路径应阻断，不以 `check-library` 的其他结构绿掩盖；本库维护报告保留命令/退出码。补 `AGENTS.md` 的目录清单 `render-ledger.py`，模板标明是数据非脚本。同步受影响来源/本库方法索引，不改历史原件。
3. **范式定位**：在各角色**现有 §4**只补其缺的“谁有权声明行为前提变化、未决回哪、旧测试新候选”最小句，相关裁决记 `SOURCES.md`（保留既有 TDD 重构单选、DDD Owner 裁决）；不用把四种名字堆进 `pipeline.md` 或创建四个 skill。反例 Implementer 删除仍有效断言称“BDD 许可”应被 Reviewer 阻断；正例 Owner 已批准新行为，经新冻结后替换旧测试应可被独立核证。
4. **历史文档**：`docs/archive/**` 与历史 `docs/TIM-*.md` 内容不删、不压缩、不按现在 §2/§3 补字段；库级 README/项目 B 映射只改**入口指针**使历史能被找到，不把历史源里的过时路径当现行命令执行。前版“依赖解除后可清历史”的建议撤销。脚本/角色里现有 `/tmp` 是**现行规范/实现**而非受保护历史，须按第 2 项处理。

**验收门限**：这份文件只确认了当前工作树的静态事实及来源文本，未运行会触发 tmp 的自检；不能声称脚本层已经可安全启用。若 `.pi/investigation/FOUR-PARADIGMS.md` 后来落盘，复核其每项源引文与本节结论，不为满足先前的层级图或技能数量改写事实。
