# SOURCE-SURVEY · 五来源身份与方法索引

2026-10-01 夜 · tpw-night-source（Pi / deepseek-v4.1-flash / max）
工作树 `/private/tmp/tpw-night-20261001 @ fc746d8`（night/2026-10-01-workflow）；上游只读（原始源在工作区 `upstreams/`，本 worktree 只含两文载体）。
用途：M4 派单底图。**本文件不裁定采纳**；是否采用由后续 M4 有界核读与 Driver/Oracle 依计划 M4 决定。
写入边界：本轮只写本文件；未改产品正文/旧记录/锁/源码，未 commit，未起会话，未安装/配置新工具。

## 0 · 状态口径

| 标记 | 含义 |
| --- | --- |
| 全文 | 本轮逐行读完正文 |
| 结构级 | 读了 frontmatter + 全部章节锚点，未逐行读正文 |
| 索引级 | 只读 `name`/`description` 元数据 |
| 身份已核 | 本轮实际读 git rev-parse/log/remote 或文件 hash |
| 原站 UNVERIFIED | 未直接读取原站页面 |
| 待核 | 未在本轮实际核验 |

- 命名/身份一律按本轮实际核读；**不继承**旧 `upstreams.lock.yaml` 的 verified/absorbed 标签。旧 lock 仅作定位线索（本轮实测 pin 与其一致，但结论以本轮动作为准）。
- 计数口径：tracked 文件与 `SKILL.md` 为实际 `git ls-files` / `find` 计数；旧 101 skills / 1080 paths 数字不作为本轮结论。

## 1 · 五来源身份卡

### S1 · addyosmani-agent-skills（仓库）

| 项 | 本轮核读值 |
| --- | --- |
| locator | `/Users/yuantian/Developer/tim-professional-workflow/upstreams/addyosmani-agent-skills` |
| remote | `https://github.com/addyosmani/agent-skills.git`（branch main，status clean） |
| pin | `2686b620fc1fed2e8f60c704839c766b8594c6b6`；2026-09-25 21:19:37 -0700；Addy Osmani `<addyosmani@gmail.com>` |
| 版本/许可 | plugin.json **0.6.11**；MIT © 2025 Addy Osmani |
| 规模 | 208 tracked files：25 SKILL.md、4 agents、9 commands(.toml)、7 references、9 hooks、docs+evals 100 |
| 核读方式 | 本轮 `git rev-parse/log/remote/status/ls-files` + `find`/`rg --files` |
| 限制 | 浅克隆（`.git/shallow`），不能做完整历史考古 |

### S2 · cursor-plugins（仓库）+ pstack（子源）

| 项 | 本轮核读值 |
| --- | --- |
| locator | `/Users/yuantian/Developer/tim-professional-workflow/upstreams/cursor-plugins` |
| remote / pin | `github.com/cursor/plugins.git`；`ecc249f1e306fc64ddf83c7bed16cacf7c2239db`；2026-09-25 16:04:33 -0700；minu `<minupal6@gmail.com>` |
| 规模 | 863 tracked files；20 个插件目录、96 SKILL.md（pstack 47、benny 自动化 3、其他 46）；最大目录 `third_party/` 482 files |
| pstack 子身份 | `.cursor-plugin/plugin.json` v0.15.5，author **Lauren Tan**；README 自述 "i'm poteto"；LICENSE MIT © 2026 Lauren Tan；`git log -- pstack/` 作者 "lauren" → 文章作者 poteto 与 pstack 作者为同一人（身份已核） |
| 其他插件归属 | repo README 表（索引级）：cursor-team-kit / cli-for-agent / grok-voice / continual-learning = Eric Zakariasson；thermos / teaching 等 = Cursor |
| 限制 | 浅克隆；单仓多插件，各插件方法风格不统一 |

### S3 · mattpocock-skills（仓库）

| 项 | 本轮核读值 |
| --- | --- |
| locator | `/Users/yuantian/Developer/tim-professional-workflow/upstreams/mattpocock-skills` |
| remote / pin | `github.com/mattpocock/skills.git`；`c55ee46073ed923f86ce59a5eb3b6d895095d1b7`；2026-09-18 11:12:29 +0100；Matt Pocock `<mattpocockvoice@gmail.com>` |
| 版本/许可 | package.json 1.2.3；MIT © 2026 Matt Pocock |
| 规模 | 169 tracked files：38 SKILL.md（engineering 18 / in-progress 9 / misc 4 / productivity 7）；docs 25；`.out-of-scope/` 3 |
| 限制 | 浅克隆；in-progress 组作者自标未定稿 |

### S4 · 文章 Pt.1 载体（本 worktree 内）

| 项 | 本轮核读值 |
| --- | --- |
| locator | `sources/articles/poteto-pstack-pt1.md`（22 行，tracked @ fc746d8） |
| 声明身份 | title "The Complete Guide to pstack Pt. 1"；author poteto；original `x.com/poteto/status/2094457600259842065`；read `threadnavigator.com/thread/2094457600259842065/`；retrieved_at 2026-09-30；`capture_sha256 543835…`；`original_verified: false` |
| 本轮实测 | 载体文件 sha256 `b7a167c60fd870396143bdbdcbcddfeb89d74e5b5abd343e1af6739864e37f83`；与原始工作区 `sources/articles/` 同名缓存 sha256 一致（本轮实测）；声明 capture_sha256 无原始捕获文件可复算 → **待核/不可复算** |
| 载体性质 | 文件明示"不复制原文"，是**方法摘记**，且引用旧库对象（`verification-suite`）→ 旧库派生摘要，不是原文、不能冒充原站 |
| 镜像核验 | 2026-10-01 本轮 fetch `threadnavigator` readable：返回标题一致（约 20,350 chars），自述 "my personal set of skills"（pstack）、Grok @Bot → **镜像身份已核** |
| 原站状态 | x.com 状态页未直接读取 → **原站 UNVERIFIED**；镜像只抽读 0–3,500 chars（验证基础设施主题） |

### S5 · 文章 Pt.2 载体（本 worktree 内）

| 项 | 本轮核读值 |
| --- | --- |
| locator | `sources/articles/poteto-pstack-pt2.md`（23 行，tracked @ fc746d8） |
| 声明身份 | original `x.com/poteto/status/2097732320606507506`；read `threadnavigator.com/thread/2097732320606507506/`；`capture_sha256 7183…`；`original_verified: false` |
| 本轮实测 | 载体文件 sha256 `304fd269f44d782037233adfa6ebe09bb077573d81089c86ccd525edd5839230`；与原始工作区 `sources/articles/` 同名缓存 sha256 一致（本轮实测）；capture 同上不可复算 |
| 镜像核验 | 返回标题一致（约 21,310 chars）；开头链接回 Pt.1 的同一 X status id → 与 Pt.1 互为续篇，身份一致 |
| 原站状态 | **原站 UNVERIFIED**；镜像抽读 0–3,500 chars；载体摘要同样引用旧库对象（teach/recall-context/prototype/codebase-design/task-breakdown） |

## 2 · 方法面规模（本轮实际计数）

| 来源 | 方法单元 | 全文 | 结构级 | 索引级 | 明确未处理 |
| --- | --- | --- | --- | --- | --- |
| S1 addy | 25 skills（+4 agents、7 refs、9 cmds、9 hooks） | 4（§8 补 2） | 21 | 25（含结构级） | docs/evals 100、hooks、commands 正文 |
| S2 pstack | 47 skills（24 常备 + 23 principles）+ 23 playbooks + guide 10 章 + 2 agents + 3 benny skills | 14 | 0 | 47 | guide 正文、architect/interrogate/why 的 references、benny 模板 |
| S2 cursor 其他 | 46 skills（team-kit 18、thermos 3、orchestrate/advisor/… 25） | 3 | 0 | 46 | third_party 482 files 等平台集成面 |
| S3 matt | 38 skills（+support files：DEEPENING、FORMAT 等） | 6（+2 支持文档 §8） | 0 | 38 | 其余 support files、docs 25 页 |
| S4/S5 文章 | 2 载体 + 2 镜像页 | 2 载体；镜像各 3.5k/20k chars | — | — | 原文完整版（各约 20k chars） |

## 3 · 方法图（A–F 判断 × professional concern）

字母是索引、不是执行序；同一方法可跨类。每行给"可能判断 / concern / 为何与活跃路径相关 / 阅读状态"。

### A · Intent / Outcome

| 锚点 | 判断 | concern | 为何与活跃路径相关 | 阅读状态 |
| --- | --- | --- | --- | --- |
| S3 `skills/engineering/wayfinder/SKILL.md` | A/D | — | 超出单会话的大工作→决策地图，逐决策解决；M1 A/Voice 多会话计划候选 | 索引级 |
| S3 `skills/productivity/grilling/`、`grill-me/`、`engineering/grill-with-docs/` | A/Voice/C | — | 对计划/设计多轮追问压测；grill-with-docs 同时产 ADR/glossary | 索引级 |
| S1 `skills/interview-me/SKILL.md` | A/Voice | — | 一次一问到 ~95%，区分 want vs should-want；A profile 与 Voice 读回候选 | 结构级 |
| S1 `skills/idea-refine/SKILL.md` | A | — | 发散/收敛锐化模糊想法（含 frameworks/examples 引用） | 结构级 |
| S2 pstack `skills/why/`（+references/epistemics、source-playbook） | A/C | — | 设计理由、回归史、postmortem 的溯源与证据纪律；C 召回依据 | 索引级 |
| S2 pstack `skills/figure-it-out/SKILL.md` | A/D | — | 无现成 playbook 时设计可审计流程；done 判据须可证伪；rigor 分级 | 全文 |
| S2 pstack `skills/poteto-mode/playbooks/investigation.md` | A/C | — | 只读问题→带引用回答/建议；不产 PR | 全文 |
| S4/S5 文章 | A/B | — | 用自己的话复述问题、事实/推断/未知分开；监督比自己强者的艺术（间接提示） | 载体全文 + 镜像抽读 |

### B · Behavioral Contract

| 锚点 | 判断 | concern | 为何与活跃路径相关 | 阅读状态 |
| --- | --- | --- | --- | --- |
| S3 `skills/engineering/to-spec/SKILL.md` | B/D | — | 会话综合成 spec：问题/用户故事/实现决定/测试决定/out of scope，发布到 tracker；不做访谈 | 全文 |
| S1 `skills/spec-driven-development/SKILL.md` | B | — | Phase 0 范围检查 + 规格模板 + gated workflow；与 S3 to-spec 同功能竞争 | 结构级 |
| S1 `skills/constraint-driven-development/SKILL.md` | B/D | 质量/合规 | 把质量 bar 写成契约、阻止静默降级；四问各带默认→CONSTRAINTS.md（floor/数量/例外） | 结构级 |
| S2 pstack `playbooks/multi-phase-plan.md` | B/D | — | 多 PR 计划模板：每 PR 的 unit/live/perf 证据、"tests alone are not sufficient verification"、review gate | 全文 |
| S4/S5 文章 | B/D | UX | 先写调用者使用体验，再从体验反推接口/类型；M3 case2 接口候选 | 载体全文 + 镜像抽读 |

### C · Domain Semantics

| 锚点 | 判断 | concern | 为何与活跃路径相关 | 阅读状态 |
| --- | --- | --- | --- | --- |
| S3 `skills/engineering/domain-modeling/`（+CONTEXT-FORMAT、ADR-FORMAT） | C | — | 术语挑战、场景压测、代码对照；CONTEXT.md 只做 glossary；ADR 三条件（难逆/反直觉/真取舍） | 全文（SKILL）；两个引用未读 |
| S1 `skills/documentation-and-adrs/SKILL.md` | C | — | ADR 时机与模板；与 S3 同功能竞争 | 结构级 |
| S2 pstack `skills/how/`、`why/` | C/D | — | 变更前系统模型（how）与设计理由（why）；architect/figure-it-out 的 grounding 输入 | 索引级 |
| S3 `diagnosing-bugs` 的 CONTEXT.md/ADR 消费习惯 | C 消费 | — | C 结论复用方式的一个样本 | 全文 |

### D · Technical / System Design

| 锚点 | 判断 | concern | 为何与活跃路径相关 | 阅读状态 |
| --- | --- | --- | --- | --- |
| S3 `skills/engineering/codebase-design/`（+DEEPENING、DESIGN-IT-TWICE） | D | — | deep module 词汇：interface/seam/depth/leverage/locality、deletion test、"一个适配器=假设接缝"；M3 case2 跨模块接口核心候选 | 全文（SKILL）；两个引用未读 |
| S2 pstack `skills/architect/`（+design-red-flags、rationale-template、runner-prompt） | D | — | 先 sketch 类型/签名/模块→arena 多候选→实现；实现反复出现同形摩擦→scrap 重设计；设计红旗清单 | 全文（SKILL）；references 未读 |
| S2 pstack `skills/arena/SKILL.md` | D | — | N 候选同题并行 + 选基座 + graft 落选者长处 | 索引级 |
| S2 pstack `skills/blast-radius/SKILL.md` | D/F | — | 变更影响超出 diff；找"这条安全所依赖的唯一事实"并用真实运行证明；grep 之外（库源码/版本/patch/时序） | 全文 |
| S1 `skills/planning-and-task-breakdown/SKILL.md` | D/A | — | 依赖图/垂直切片/任务模板/checkpoint；D 计划候选 | 结构级 |
| S1 `skills/api-and-interface-design/SKILL.md` | D | — | contract first、错误语义、边界校验、加法优先、Hyrum's Law | 结构级 |
| S3 `skills/engineering/to-tickets/SKILL.md`、`prototype/SKILL.md` | D | — | tracer-bullet tickets + blocking edges；丢弃式原型回答设计问题 | 索引级 |
| S2 pstack principles：`boundary-discipline`、`model-the-domain`、`type-system-discipline`、`foundational-thinking`、`separate-before-serializing-shared-state`、`make-operations-idempotent`、`migrate-callers-then-delete-legacy-apis`、`redesign-from-first-principles`、`subtract-before-you-add`、`laziness-protocol` | D/C | 并发/持久化/依赖 | 单点设计纪律，按需引用；M3 case2（snapshot/freshness 共享状态）相关 | 索引级（23 条 principle 只读描述） |
| S2 cursor `orchestrate/skills/orchestrate/SKILL.md` | D/Driver | 成本 | 云端并行规划树（Cursor SDK 绑定）；当前 harness 不适用，仅登记 | 索引级 |

### E · Implementation

| 锚点 | 判断 | concern | 为何与活跃路径相关 | 阅读状态 |
| --- | --- | --- | --- | --- |
| S3 `skills/engineering/implement/SKILL.md` | E | — | 10 行指针：按 spec/tickets 实现；能则 /tdd；常规 typecheck/单测；完事 /code-review；提交 | 全文 |
| S1 `skills/incremental-implementation/SKILL.md` | E | — | 垂直/契约优先/风险优先切片；每片 implement→test→verify→commit；Rule 0 简单优先；红线表 | 全文 |
| S3 `skills/engineering/diagnosing-bugs/SKILL.md` | E/F | — | **反馈回路是技能本体**：red-capable/deterministic/fast/agent-runnable；3–5 可证伪假设；回归测试需"正确 seam"，无 seam 本身就是发现 | 全文 |
| S1 `skills/debugging-and-error-recovery/SKILL.md` | E/F | — | Stop-the-line、复现→定位→缩小→根因；与 S3 同功能竞争 | 结构级 |
| S2 pstack `playbooks/bug-fix.md` | E/F | — | 科学化修 bug：先自证 repro、二分排查、失败 repro 先入 git 历史、同表面验证 | 全文 |
| S2 pstack `playbooks/feature.md` | E/D | — | how→architect→throughput checkpoint（阻塞/独立工作流/共享可变状态/最小分解）→委托→按面验证→小步 commit/stack | 全文 |
| S1 `skills/test-driven-development/SKILL.md`、S3 `skills/engineering/tdd/`、S2 pstack `skills/tdd/` | E/F | — | 三家 TDD 变体（add：Prove-It/测试金字塔；matt：red-green-refactor + mocking/tests 引用；pstack：只在明确要求或便宜路径用） | 结构级 / 索引级 / 索引级 |
| S2 cursor `fix-ci`、`loop-on-ci`、`fix-merge-conflicts`、`deslop`、`check-compiler-errors` | E | — | CI/编译/冲突/风格收尾；平台工具特定 | 索引级 |

### F · Verification

| 锚点 | 判断 | concern | 为何与活跃路径相关 | 阅读状态 |
| --- | --- | --- | --- | --- |
| S3 `skills/engineering/code-review/SKILL.md` | F | — | 固定基点双轴（Standards 含 Fowler smell baseline / Spec），并行子代理、拒绝合并排序；B 轴回指 spec | 全文 |
| S1 `skills/code-review-and-quality/SKILL.md` | F | Security/依赖 | 五轴 + 严重度前缀 + 多模型评审 + 变更尺寸/描述纪律 + 依赖升级逐包纪律 | 全文 |
| S2 cursor `verify-this/SKILL.md` | F | — | 可证伪 claim + baseline/treatment + 三态 **VERIFIED / NOT VERIFIED / INCONCLUSIVE**；三态最接近 Backbone 的 PASS/FAIL/UNVERIFIED | 全文 |
| S2 pstack `skills/create-verification-skill/`（+feature-map references） | F | — | 项目本地验证 skill：launch/doctor/drive/evidence/cleanup；真跑一次才算交付；feature map 是维护源；文章 Pt.1 主题对应方法 | 全文（SKILL）；references 未读 |
| S2 pstack `skills/maintain-verification-skill/SKILL.md` | F | — | 保持验证 skill 与 feature map 诚实（维护回路） | 索引级 |
| S2 pstack `skills/interrogate/`（+rubric/reviewer-prompt/lead-judgment/code-quality-review） | F | — | 多模型同 prompt 对抗评审；共识/独见/分歧；lead judgment 分类（act on/consider/noted/dismissed）；**独立关系候选** | 全文（SKILL）；references 未读 |
| S1 `skills/doubt-driven-development/SKILL.md` | F | — | 每个非平凡决定交给 fresh-context 对抗评审（CLAIM/EXTRACT/DOUBT/RECONCILE） | 结构级 |
| S2 pstack `skills/show-me-your-work/`（+template、log.sh） | A/F | 成本 | append-only TSV 决策 trail（what/why/evidence/result）+ 跨模型审查 + 对 transcript 审计；A9 台账的近似物 | 全文 |
| S2 cursor thermos `thermo-nuclear-review/SKILL.md` | F | Security/DevEx | security+correctness+devex+feature-leak 审计 prompt；只报 diff 内；intended breakage 与"不过度报告"纪律 | 全文 |
| S2 cursor team-kit `review-and-ship/SKILL.md` | F/E | — | 轻量闭环：diff→定向测试→审查→修复→提交→PR | 全文 |
| S2 pstack `principle-prove-it-works/` | F | — | 对真实 artifact 验证；script the check；失败先怀疑观察方法 | 全文 |
| S4 文章 Pt.1（镜像） | F | 成本 | verification 是基础设施：agent 自验证闭环、CLI 可用性（可组合/危险动作可预演/机器可读）、能力地图从用户视角写 | 载体全文 + 镜像抽读 |

### 跨类 / 连接器（Voice·Driver·路由·交接）

| 锚点 | 判断 | 为何与活跃路径相关 | 阅读状态 |
| --- | --- | --- | --- |
| S2 pstack `skills/poteto-mode/SKILL.md` | 路由/委托/自主 | 23 playbooks + 23 principles 总路由；委托模型/角色默认、autonomy（"Just do it"、always-pause=不可逆）；**其 never-block-on-human 等默认与 Backbone 委托纪律存在张力，须对比而非照搬** | 全文 |
| S3 `skills/engineering/ask-matt/SKILL.md` | 路由 | 技能选择路由表（+PHASE-BOUNDARIES.md） | 索引级 |
| S3 `skills/productivity/handoff/`、in-progress `claude-handoff/`；S2 pstack `recall/`、`reflect/`、`session-pickup`、`pause-safely` | 交接/接续 | 跨会话交接、复盘、暂停恢复的样本 | 索引级 |
| S3 `skills/productivity/writing-for-agents/`（+SKILL-MECHANICS） | 元 | 写 skill/AGENTS 的方法；M4 蒸馏时参考 | 索引级 |
| S1 `skills/using-agent-skills/`、`context-engineering/` | 元/上下文 | skill 发现与上下文层级（规则/规格/源码/错误） | 结构级 |

### Professional concern 面板（横向）

| concern | 主要锚点 | 状态 |
| --- | --- | --- |
| Security | S1 `security-and-hardening`（三层边界 Always/Ask/Never + hardening controls + references/hardening-patterns）；S2 thermos `thermo-nuclear-review`；S2 pstack `principle-boundary-discipline`、`type-system-discipline`；审查内嵌：S1 code-review 五轴 Security | 结构级 / 全文 / 索引级 / 全文 |
| 依赖与供应链 | S1 code-review-and-quality 的 Dependency Discipline（changelog/lockfile/逐包升级）；S1 security-and-hardening 的 audit 处置 | 全文 / 结构级 |
| Persistence/并发/一致性 | S2 pstack `separate-before-serializing-shared-state`、`make-operations-idempotent`、`migrate-callers-then-delete-legacy-apis`、`sequence-verifiable-units`；S1 `deprecation-and-migration` | 索引级 / 结构级 |
| Performance | S1 `performance-optimization`（CWV/优化流程）；S2 pstack `playbooks/perf-issue`、`hillclimb` | 结构级 / 索引级 |
| UX | S1 `frontend-ui-engineering`；S2 cursor `control-ui`；S3 `prototype/UI.md` | 结构级 / 索引级 |
| 成本/资源 | S2 pstack figure-it-out 的 rigor 分级、`principle-guard-the-context-window`；S2 playbooks multi-phase-plan 的证据预算 | 全文 / 索引级 |
| Operability | S1 `observability-and-instrumentation`（先定义 working 再埋点；验证 telemetry 本身） | 结构级 |

## 4 · Active 路径优先候选（供 M4 派单；不裁定采纳）

与 M1（A/Voice、B/C、D、E、F Profile）和 M3（局部缺陷；跨模块 snapshot/freshness）直接相关：

| # | 候选 | 涉判断 | 为什么现在值得核 | 建议下一动作 |
| --- | --- | --- | --- | --- |
| P1-1 | S3 codebase-design vs S1 api-and-interface-design | D | M3 case2 的跨模块承诺需要先有"接缝/深度"判断词汇；两家词汇冲突（module/interface/seam vs contract/boundary） | 全文对读 + 列差异；S3 两个引用文件一并读 |
| P1-2 | S3 diagnosing-bugs vs S1 debugging-and-error-recovery vs S2 bug-fix playbook | E/F | M3 case1 直接使用；三家都要求先建 repro 才许假设 | 全文对读；S1 需全文 |
| P1-3 | S3 code-review vs S1 code-review-and-quality vs S2 verify-this vs S2 interrogate | F | F Profile 与"独立性"边界是 Backbone 硬规则；verify-this 三态与 PASS/FAIL/UNVERIFIED 的映射需专业确认 | verify-this 已全文；其余按需 |
| P1-4 | S3 to-spec vs S1 spec-driven-development | B | B Profile 主候选；S3 假定 issue tracker，S1 自带模板，装配差异大 | S1 全文 |
| P1-5 | S3 domain-modeling vs S2 why/how | C | C Profile 与 M3 case2 的 snapshot/freshness 语义裁定 | S3 引用文件（CONTEXT-FORMAT/ADR-FORMAT） |
| P1-6 | S1 incremental-implementation vs S2 feature playbook | E | E Profile 的"验证单元"概念来源；两者都要求每单元先验证再前进 | 已全文，可直接进入对读 |
| P1-7 | S2 create-verification-skill + S4 文章 Pt.1 | F | 验证基础设施是否进入 M3/M6 冷启动路径，决定是否加深 | 已全文；references/feature-map 例子按需 |
| P1-8 | S1 security-and-hardening vs S2 thermos thermo-nuclear-review | Security | Backbone 要求租户缓存类触发先于泄漏；两个来源给不同层次（设计合同 vs 审计 prompt） | S1 全文 + hardening-patterns |
| P1-9 | S2 show-me-your-work | A/F | 与本库 A9 台账/STATUS 的关系需 Driver/Oracle 判断（是否复用格式、是否本地不提交） | 已全文 |
| P1-10 | S2 poteto-mode 的 Driver 语义 | 路由 | 其 playbook 路由/委托模型可作 Driver 语义对照；autonomy 默认与本库边界冲突，须显式隔离 | 已全文；对读 Backbone §4 |

P2（后续按需）：S3 to-tickets/wayfinder/triage/prototype/tdd/grilling；S1 planning-and-task-breakdown/api-and-interface-design/spec-driven-development/constraint-driven-development/debugging-and-error-recovery/doubt-driven-development；S2 multi-phase-plan/architect references/principle 单条；S4/S5 镜像全文（若文章方法进入采用路径）。

## 5 · 明确排除范围（本轮不处理）

- S2 cursor `third_party/`（482 files：gmail/google-drive/docs/x…）、`grok-voice`、`docs-canvas`、`pr-review-canvas`、`ralph-loop`、`cursor-sdk`、`create-plugin`、`agent-compatibility`、`continual-learning`、`advisor`、`teaching`、`orchestrate`、`cli-for-agent`、thermos 其余 2 skills：平台/集成绑定，与活跃路径无关。
- S3 in-progress 9（implement-spec/pr/retro/writing-\*/loop-me/claude-handoff/setup-ts-deep-modules）：作者自标未定稿；misc 4：工具特定。
- S1 hooks 9、commands 9、docs/evals 100：运行机制与评测，不给方法语义。
- S2 pstack docs/guide 正文 10 章（只读到 README 导航）、architect/interrogate/why 的 references、benny 模板。
- S4/S5 镜像全文各约 20k chars（只抽读前 3.5k）。

## 6 · 真实缺口（给 Driver）

1. **文章载体是旧库派生摘要**，不是原文，且用旧产品词汇（verification-suite/recall-context/task-breakdown）；若 M4 要采用文章方法，须以镜像原文重核，不能引用载体措辞当作新包术语。
2. 文章 `capture_sha256` 不可复算（原始捕获不在库内）；已记载体自身 sha256 作为可复算 digest。X 原站 UNVERIFIED。
3. S1 addy：23/25 只到结构级；若与 matt/pstack 竞争同一判断，需定向全文（P1-1/2/4/6/8）。
4. S3 matt：32/38 索引级；support files（DEEPENING/DESIGN-IT-TWICE/CONTEXT-FORMAT/ADR-FORMAT/tests.md 等）未读。
5. S2 pstack：23 条 principle 只有描述；guide 正文与 interrogate/architect/why 的 references 未读。
6. S2 cursor 非 pstack：46 skills 仅描述级；thermos/team-kit 细则（make-pr-easy-to-review/run-smoke-tests/control-ui/cli）未读。
7. 三仓均浅克隆，无法做完整历史/zombie 作者考古；pin 已核即为上限。
8. 平台绑定差异：matt 用 `agents/openai.yaml` + `disable-model-invocation`；pstack 依赖 `pstack-models.mdc`、Cursor Task/`subagent_type`、/goal、/loop；addy hooks 是 Claude/Codex 风格。移植时必须剥平台机制（未裁定哪些剥）。
9. 五来源正文均为英文；蒸馏需翻译并保留原锚点。
10. 旧 lock 的 101 skills 处置表与旧 absorbed 状态未继承；如需对照旧处置，应作为历史材料单独引用。

## 7 · 本轮合规记录

- 只读操作：`git rev-parse/log/remote/status/ls-files`、`rg --files -uu`（排除 .git）、`find`、`wc`、`shasum`、`head/grep`、只读 `fetch_content`（镜像）。
- 未修改任何 upstream 文件（三仓 status clean）；未安装/配置新工具；未改旧记录/锁/产品正文；未 commit；未另起会话。
- 唯一写入：本文件。

## 8 · M4 有界深读比较（M3 两条活跃路径 + F 三角；2026-10-01 夜补）

**范围与状态**：按 Driver 指定有界核读；只回相关原文正文，未重扫全库、未改上游、**本比较不采纳**。本轮新增全文阅读：S1 `debugging-and-error-recovery`、S1 `api-and-interface-design`、S3 `codebase-design/DEEPENING.md`、S3 `codebase-design/DESIGN-IT-TWICE.md`。F 侧只用已全文读过的 `verify-this`/`interrogate`/`code-review`。S4/S5 未重核（见 8.4）。

### 8.1 路径一 · 局部缺陷的可复现反馈回路

三家共同底线：先复现再动手；修根因不修症状；修后留回归证据；不在证据前猜测。

| 维度 | S3 diagnosing-bugs | S1 debugging-and-error-recovery | S2 pstack bug-fix playbook |
| --- | --- | --- | --- |
| 核心机制 | **反馈回路是技能本体**：先造 red-capable/deterministic/fast/agent-runnable 的一条命令并已跑过一次；没回路就禁止进入假设 | Stop-the-line 六步 + 六步 triage（复现→定位→缩小→修根因→防复发→端到端验证） | 科学方法：每条上线代码溯源运行时证据；在 control skill 上自己复现；二分排除假设；机制须运行时证据确认 |
| 复现 | 10 种回路构造法（failing test、curl、CLI snapshot diff、headless browser、replay trace、throwaway harness、fuzz、bisect、differential、HITL script）；tighten loop（更快/更尖/更确定） | 非可复现决策树：timing（时间戳/人为延迟/加负载）、env（版本/环境变量/数据）、state（泄漏/单例/隔离）、random（防御日志+告警） | 直接复现不了则合成触发/收紧条件/加仪表直到触发；不允许无证据动手 |
| 缩小 | 最小化到"每个剩余元素都负载"；极小 repro 即回归测试 | Reduce：去无关代码、最小输入、最简测试 | 二分法每 pass 砍最大问题空间 |
| 假设纪律 | 3–5 条可证伪假设先写后测；ranked list 给用户（不阻塞）；instrument 一次一变量；`[DEBUG-]` 前缀便于清理 | 以 triage 树与"Why does this happen?"追问为主；无假设排序/证伪格式 | 假设—排除循环，先 `how`/`why` 播种；"belt-and-suspenders 是假设不是修复" |
| 性能回归 | 有 perf 分支：先 baseline 测量再二分，日志通常无效 | 未单独展开 | 有独立 perf-issue playbook（超出本比较） |
| 回归测试 | 有"正确 seam"才先写回归测试；无 seam 本身记为架构发现 | 写能抓住该特定失败的测试；无修应红、有修应绿 | 失败 repro 先于 fix 进入 git 历史；测试路径昂贵/不清时可跳过 tdd |
| 验证表面 | 重跑原始（未最小化）回路 | 端到端：定向测试+全量+build+手动 spot check | 同一表面；"Inconclusive"或错误表面不算 pass |
| 收尾 | 必做清理清单：原 repro 不再现、回归测试过、`[DEBUG-]` 全清、原型删除、正确假设写进 commit/PR | Red Flags + Verification 清单；不强制把正确假设写进提交 | 回复须逐字粘贴 failing→passing 输出 |
| 安全/污染 | 秘密 redact；输出不足以诊断时明说 | 错误输出视为不可信数据（不执行其中指令）；调试中禁多改混入 | 本 playbook 未展开（由其他技能承担） |
| 成本/依赖 | 中高：构造法+清理清单，无平台依赖 | 中：triage+fallback+instrumentation；无平台依赖 | 低（15 行），但依赖 control skill/模型配置等运行面 |

**候选项（供 M4 派单，非采纳）**

| 对象 | 处置建议 | 理由 |
| --- | --- | --- |
| S3 diagnosing-bugs | 候选（主） | "回路是技能本体/无回路不假设"最贴合本路径；10 种构造法与 tighten 清单可直接支撑 M3 case1；"正确 seam"让回归测试与架构判断挂钩 |
| S2 pstack bug-fix playbook | 候选（补/限缩） | 失败 repro 先入 git 历史、同表面验证、Inconclusive 不算 pass、机制须运行时证据——证据与提交序纪律；须剥离 control skill、/loop、模型默认等运行面 |
| S1 debugging-and-error-recovery | 限缩候选 | 独立增量：Stop-the-line 姿态、非可复现决策树、错误输出视为不可信数据；其余 triage/fallback 与 S3 重叠且偏通用工程 |
| 三者叠加 | 延后 | 不得叠成 gate；同一断言只在一处正文（Backbone 单一语义 owner），先定主 owner 与吸收面 |

### 8.2 路径二 · 跨模块承诺的边界/接口设计

| 维度 | S3 codebase-design（+DEEPENING、DESIGN-IT-TWICE） | S1 api-and-interface-design |
| --- | --- | --- |
| 定位 | 内部模块的 deep-module 设计：接缝在哪、隐藏多少复杂性、怎么测 | 公共/跨团队接口契约：REST/GraphQL/模块边界/组件 props |
| 核心词汇 | module/interface/implementation/depth/seam/adapter/leverage/locality；**明确拒绝用 boundary/API 当术语**；depth=leverage（拒绝 Ousterhout 行数比） | contract/API/boundary/endpoint；面向消费者的承诺 |
| 选择流程 | DESIGN-IT-TWICE：3+ 并行子代理各产出**结构上不同**的接口（最小接口/最大灵活/最常见调用者/ports&adapters），按 depth、locality、seam 位置对比，再给强意见或 hybrid | Contract First：先定义类型/契约再实现；无显式多候选比选 |
| 接缝/依赖 | DEEPENING 四类依赖（in-process / local-substitutable / remote-owned 以 port+adapter / true external mock）决定测试怎么跨缝；"一个 adapter=假设接缝，两个才真实"；内部缝 vs 外部缝 | Validate at Boundaries：只在校验边界（路由/表单/外部响应/环境变量）；第三方响应一律不可信；内部函数不再校验 |
| 演进/兼容 | deletion test；replace-don't-layer（旧浅模块单测删除，测试穿过新接口） | Hyrum's Law；One-Version Rule；Prefer Addition Over Modification；Predictable Naming |
| 错误语义 | 未展开（接口含 error modes 但无统一策略） | 单一错误策略（机器码+人类消息+details；状态码映射）；不得混用 throw/null/`{error}` |
| 幂等/重试 | 无 | Idempotency key 完整语义：从意图派生、原子 claim（唯一约束即机制）、payload hash 守门、在途重复三策略、success/failure/unknown 三态、retention 按最长重试链 |
| 与 M3 case2 的贴合 | 直接：snapshot/freshness 承诺要定"缝在哪、谁跨缝、隐藏什么、测试穿哪" | 部分：承诺的行为边界/错误模式/兼容演进/重试幂等可用；REST/分页/命名/GraphQL 等细节超出 |

**候选项（供 M4 派单，非采纳）**

| 对象 | 处置建议 | 理由 |
| --- | --- | --- |
| S3 codebase-design + DEEPENING | 候选（主） | seam/depth/依赖四类/"interface is the test surface"/replace-don't-layer 直接服务 M3 case2 的"谁跨缝、缝在哪、怎么测"；"one adapter=hypothetical"防过度抽象 |
| S1 api-and-interface-design | 限缩候选 | 保留 contract first、consistent error semantics、prefer addition over modification、idempotency 三态与 retention；REST 资源/分页/命名表/GraphQL 等公共 API 细节 → 延后 |
| S3 DESIGN-IT-TWICE | 延后 | "设计两次/对比 depth-locality-seam/给强意见"纪律可留候选；3+ 并行子代理是运行面，且与 M2 薄装配的绑定方式未定，待 D 侧确需多候选比选再开 |
| 词汇冲突（module/interface/seam vs 接口/边界） | 待决（记录） | matt 明确拒绝 boundary/API 当术语，Backbone 正文用"接口/边界"；术语单一 owner 需在 M4/M5 定，本比较不裁定 |

### 8.3 F 三角（verify-this / interrogate / matt code-review）

| 维度 | S2 cursor verify-this | S2 pstack interrogate | S3 matt code-review |
| --- | --- | --- | --- |
| 对象/时点 | 单个可证伪 claim 的行为证据（修复后） | changeset 或设计（实现前或后） | 固定基点以来的 diff（实现后） |
| 输入 | condition/metric/threshold + baseline 与 treatment 同命令同数据同环境 | intent 段 + diff/文件 + reviewer-prompt/rubric/code-quality lens | fixed point + `git diff x...HEAD` + repo 标准 + 原始 spec/ticket |
| 独立信号来源 | 本地 fresh 证据（仪器本身） | 模型多样性：同 prompt/rubric 给多个 reviewer；共识（2+）、独见、分歧分别处理 | 两轴并行子代理（Standards / Spec），分离视角而非重复 |
| 结论形态 | 恰好一个 verdict：VERIFIED / NOT VERIFIED / INCONCLUSIVE + evidence/reasoning | 合成 verdict + 分类（act on/consider/noted/dismissed，注明哪个模型提的）+ Agreement Map；不自动应用 | 两轴报告并列 + 每轴 worst issue；**拒绝跨轴选单一赢家** |
| 明示边界 | 模糊 claim 不用；不软化负面结果 | 不 auto-apply；单模型发现权重降低 | spec 缺失时跳过 Spec 轴并注明；smell 一律 judgement call，repo 标准可覆盖 |
| 作者/评价者关系 | 未定义 | 未定义（模型多样性≠作者独立） | 未定义 |
| 平台绑定 | control-cli/control-ui、/tmp/verify-this 布局 | Cursor Task + 模型配置表（pstack-models.mdc） | issue tracker + `docs/agents/issue-tracker.md`（setup skill） |
| 适配 M3 | case1 修复行为证据直接；case2 可用于行为承诺测量 | case2 设计挑战最直接；case1 可用于挑战跨界修复设计 | 两案例的 standards/spec 审查；不是行为证据 |

**候选项与延后（供 M4 派单，非采纳）**

| 对象 | 处置建议 | 理由 |
| --- | --- | --- |
| S2 verify-this | 候选（F 结论格式） | 三态与 Backbone 同构（INCONCLUSIVE≈测量无效的 UNVERIFIED）；baseline/treatment 结构可复用；但它只是仪器 |
| S2 interrogate | 候选（设计挑战/评审合成程序） | 多独立评审同 rubric、共识/独见/分歧、lead judgment 分类、不自动应用；最贴合 M3 case2"另一实际实例挑战设计"；须剥离 Cursor Task 与模型表 |
| S3 code-review | 候选（standards/spec 审查程序） | 双轴分离、固定基点、repo 标准覆盖 smell baseline、不跨轴重排；须替换 tracker 交互 |
| 三者的独立性缺口 | 记录（不解决） | 三者均不定义"评价者不得是作者"；A7/A8 independence 必须由 Charter/委托承担，不能从方法推导 |
| S1 code-review-and-quality | 延后 | 已全文读过（五轴/严重度/依赖纪律），不在本轮命名比较范围；需要时再开有界比较 |

### 8.4 文章（S4/S5）与阅读状态增量

- 本轮没有具体文章方法被提出进入活跃路径 → **未对 S4/S5 做 fresh read**；旧摘要不算 fresh read。若 Pt.1 verification-infrastructure 或 Pt.2 design/plan 方法后续进入采用路径，先基于原站或固定镜像全文重核（镜像可用、原站 UNVERIFIED），再作正文来源。
- 阅读状态增量：S1 +2 全文（`debugging-and-error-recovery`、`api-and-interface-design`；结构级 23→21）；S3 +2 支持文档全文（`DEEPENING.md`、`DESIGN-IT-TWICE.md`）；其余同 §2。
- 待 Driver 决策的开放点：(1) 路径一主 owner 与 S1 三条增量是否吸收；(2) 路径二词汇 owner 与 S1 限缩边界；(3) F 侧独立性规则是否落到 Charter 层。本文件不裁定。
