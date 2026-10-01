# ABSORB-B-ADJUDICATION · 采纳裁定候选轨（与 coverage 分离）

2026-10-01 · 实例 `tpw-absorb-b` · 依据 `UPSTREAM-DEEP-ABSORPTION-PLAN.md` §3（裁定与覆盖分开）、§4（完成度口径）、§5（实际采纳的前置与纪律）、§6（Owner 决定点）。
覆盖计数见 `ABSORB-B-CALIBRATION.md` §5；机制清单见 `ABSORB-B-MECHANISM-COVERAGE.tsv`。**本文件不写 core/product，不实施，不授权落地。**

## 0 · 规则

1. **覆盖 ≠ 采纳**：`covered` 不自动等于 `adopt`；`not-covered` 也不自动等于 `adopt`。裁定轨只处理 TSV 中 `verdict_candidate != none` 的 **146** 行。
2. **裁定取值**：`adopt`（建议新增/吸收机制正文）、`narrow`（建议限缩现有或上游机制到明确边界）、`reframe`（本次未使用；见 §4 说明）、`replace`（本次未使用）、`reject`（建议不入包，给出范围理由）、`defer`（本轮不裁定，给出阻塞点与决定归属）。`none`（37 行）= 当前文本已足够、本轨不提变更。
3. **裁定是候选，不是落地**：计划 §6 规定"没有 Owner 的落地授权，覆盖与裁定不能实施"。本文件所有 `adopt` 均为**候选**，落地需另行授权。
4. **回读分级（诚实标注每条的前置）**：
   - **R2** = 本轨已读原文（机制主体或全文），并读过相关支持文件；
   - **R1** = 本轨读过原文的部分段落或同族样本，其余依赖 A 屏；
   - **R0** = 本轨只读了 A 的行，未读原文。
   **计划 §5 要求采纳前必须有相关原文+支持文件的完整回读**：因此 **R1/R0 的 adopt 候选在落地前必须补读**（每条给出补读对象）；`narrow`/`defer`/`reject` 不要求同等回读，但不得被当作已实现变更。
5. **不得为省 gate 剥掉专业细节**（计划 §5）：涉及幂等、原子认领、同键异载荷、在途重复、未知结果、保留因果等细节的裁定，`保留/改变/删除` 一栏必须列全，不允许用"以后再说"代替。
6. **无当前方法 = 缺口线索**，不是低分：`not-covered` 行在本文件里以"缺口线索"登记，供 Owner 决定取舍。

## 1 · 回读记录（本轨实际读了什么）

| 族 | 已读原文（R2 面） | 部分读 / 仅 A 屏（R1/R0） |
| --- | --- | --- |
| AUTH/BHV/META | 产品 19 文件全文（R2）；matt `.out-of-scope/question-limits.md` 全文；`docs/engineering/codebase-design.md` 章节+#458 段 | matt `skills/productivity/grilling/SKILL.md`、`writing-for-agents/**`、`domain-modeling/CONTEXT-FORMAT.md`、`to-spec`、`to-tickets`、`wayfinder`、`docs/engineering/grill-with-docs.md` 均未读原文（R0）；addy `interview-me`、`spec-driven-development`、`documentation-and-adrs` 未读（R0） |
| DES | cursor `pstack/skills/principle-*` 未逐份读（R0，仅 A 行）；matt `dependency-cruiser.config.cjs` 全文（R2）；`codebase-design/DEEPENING.md`、`DESIGN-IT-TWICE.md` 未读（R0）；cursor `store.ts` 锁/持久化段（R2），其余结构（R1） | addy `api-and-interface-design`、`incremental-implementation`、`deprecation-and-migration`、`constraint-driven-development` 未读（R0） |
| DBG | matt `diagnosing-bugs/scripts/hitl-loop.template.sh`（R2）、`tdd/mocking.md`（R2）；addy `debugging-and-error-recovery/SKILL.md`（前 60 行 + 标题，R1） | matt `diagnosing-bugs/SKILL.md`、`tdd/SKILL.md`、`tdd/tests.md`；cursor `pstack tdd`、`principle-fix-root-causes`、`principle-test-behavior-not-implementation` 未读（R0） |
| EVID | addy `evals/cases/test-driven-development.json`（R2）；addy `scripts/validate-artifact-paths.js`（R2） | cursor `verify-this`、`blast-radius`、`interrogate`、`arena`、`thermo-nuclear-*`、`show-me-your-work`；addy `code-review-and-quality`、`references/definition-of-done.md`、`agents/*`、`evals/plugin/**` 未读（R0） |
| DLV/PKG | cursor `third_party/xero/**`（R2）、`x-money/skills/x-money-guide/SKILL.md`（R1，前 80 行）、`orchestrate/SKILL.md`（R1）、`docs-canvas/SKILL.md`（R1） | addy `git-workflow-and-versioning`、`shipping-and-launch`、`ci-cd-and-automation`；matt `wizard`、`handoff`、`in-progress/pr`、`git-guardrails`；cursor `make-pr-easy-to-review`、`new-branch-and-pr`、`create-plugin/**` 未读（R0） |
| ORC/HIT/CONC/SKL/FMT/GOV | 同上；`dependency-cruiser.config.cjs`（R2） | `swarm`、`arena`、`reflect`、`recall`、`continual-learning`、`technical-writing`、`unslop`、addy `security-and-hardening`、`observability`、`reference checklists` 未读（R0） |

**因此**：本文件的所有 `adopt` 均为"有理由的候选 + 明确补读清单"，而不是"已完成 §5 全文回读的采纳"。

---

## 2 · 逐机制裁定候选

格式：`裁定 · id 名称` — 理由；与现有内容差异；保留/改变/删除；建议落点；回读/前置。

### 2.1 AUTH（责任/治理/分发）

- **narrow · AUTH-04 横向专业关注轴** — 理由：轴本身已被 Backbone §1/§5 固定，但"有五类关注点"不构成可执行判断；差异：当前只有轴与四例，无任何关注点检查面；保留：轴与"不新增责任节点"；改变：把"轴已覆盖"降级为 partial，避免下游误读为安全/性能已有操作；删除：无；落点：不改 Backbone，改在 methods 或 Concern 清单层（见 CONC-01）；回读 R2（产品全文）；前置：无。
- **narrow · AUTH-09 关闭权与 closure rule** — 理由：产品有关闭规则概念，但把 finding 是否阻断交由 authority 判定而**没有状态机**，下游无法复现转移；差异：上游 triage 有 category/state 角色与 exactly-one 不变式；保留：Driver 不作新专业裁定；改变：只保留"阻断判定有 authority"这一句，不引入标签体系；删除：不引入 tracker 状态机；落点：methods/driver 侧（若 Owner 要）或明确登记为不做；回读 R0（matt triage 未读）；前置：补读 `skills/engineering/triage/SKILL.md` 再定。
- **narrow · AUTH-16 共享引用代替重复正文** — 理由：产品已有该规则，但缺少可操作的"写作/引用"纪律；差异：上游 writing-for-agents 给出 leading word、删除测试、一分支一触发等操作；保留：共享引用+差分；改变：把"引用"从原则升为写作操作（见 META-01）；删除：无；落点：docs 规则或方法附件；回读 R0；前置：补读 `writing-for-agents/SKILL.md` 与 `SKILL-MECHANICS.md`。
- **narrow · AUTH-18 未接受建议可用于可逆探索** — 理由：原则正确但无"可逆"判据，也没有原型形态；差异：上游 prototype 有 throwaway-and-marked、不持久化、跳过打磨、留答案作 primary source；保留：原则；改变：补可逆判据（见 DES-26）；删除：无；落点：方法或 Charter 工具段；回读 R0；前置：补读 `skills/engineering/prototype/SKILL.md` 与 `LOGIC.md`/`UI.md`。
- **narrow · AUTH-20 冻结导出纪律** — 理由：人工摘要核对在两个 21KB 文件上可持续性存疑；差异：上游用 `--check` 脚本在 CI 失败；保留：先改源、接受后导出、不得手改投影；改变：明确"当前无机器检查"并登记为风险（PKG-03/FMT-08），不因此新增 gate；删除：无；落点：authority/README 的现状句或 DOC；回读 R2（authority/README）；前置：无。
- **narrow · AUTH-24 方法正文不产生授权 + digest 溯源** — 理由：digest 表已做到"身份可辨"，但 M4/M5 双摘要与"M1 时代字样"并存会让读者误判有效状态；差异：上游有版本同步脚本与 changeset 血统；保留：表格与 digest；改变：标注过时叙述、把"当前有效"指向唯一入口（与 META-03/GOV-01 合并处理）；删除：不删历史快照；落点：professional-workflow/README + methods/README 状态段；回读 R2；前置：无。
- **narrow · AUTH-25 分发路线与包形态** — 理由：当前是"可 cat 的文本包"，但缺依赖/缺文件时的降级与版本迁移没有判据；差异：上游 ADR 0002 记录了路线取舍与 manifest 能力约束；保留：cat 装配；改变：补"缺依赖怎么办"与"包被复制后语义归属"；删除：不引入安装器；落点：README 或方法（若 Owner 要）；回读 R0（matt ADR 0002 未读）；前置：补读 `.agents/adr/0002-ship-as-a-claude-code-plugin.md`。
- **defer · AUTH-26 hard/soft dependency 与优雅降级** — 理由：产品是纯文本包，上游 ADR 是 skill 前置依赖语境，可映射度需 Owner/Driver 判定；差异：产品完全没有依赖分级；保留：现有绑定状态句；改变：无（本轮不改）；删除：无；落点：若采纳则进 Charter 的 Applicable methods 段；回读 R0；前置：补读 `.agents/adr/0001-*` + `to-spec`/`to-tickets`/`triage` 的前置行；决定归属：Driver。
- **adopt · AUTH-27 决定记录（ADR）** — 理由：产品把"决定记录方法"列为候选却无字段集，导致"已接受结论"缺少可复查载体；当前做法会让后续读者无法判断某条规则是接受、候选还是历史快照；差异：上游 ADR-FORMAT 有 Status/Date/Context/Decision/Alternatives/Consequences 与生命周期；保留：Charter/Plan 的既有分工；改变：新增（或并入 Charter 的）最小记录形态；删除：不删任何现有文本；落点建议：`methods/` 新方法 `decision-record.md`，或并入 `charters/template.md` 一节；回读 R1（读过 `docs/engineering/codebase-design.md` 与 A3 ADR 行，未读 ADR-FORMAT 原文）；前置：补读 `skills/engineering/domain-modeling/ADR-FORMAT.md` + `addy:skills/documentation-and-adrs/SKILL.md`。
- **adopt · AUTH-28 out-of-scope 登记册** — 理由：产品已有"目标与非目标同权"与多处 deferred alternatives，但没有登记册，导致同一推迟项会被反复重新讨论（本轨校准中即遇到 META-04/DLV-06 等重复出现）；差异：上游以"一条一理由一判据 + 先前请求编号"承载；保留：非目标同权原则；改变：把散落的推迟项收成登记册并由单一入口指向；删除：不删 deferred 说明；落点建议：`docs/` 或方法附件；回读 R2（读过 `question-limits.md` 全文与另两份 out-of-scope 的 A 行）；前置：补读另两份 out-of-scope 原文。
- **narrow · AUTH-29 单一口径安装/使用文本** — 理由：包内三处装配示例并存（README、charters/README、methods/README 语境），内容不同；差异：上游用 `<canonical-block>` + 向外传播规则；保留：三处说明各自语境；改变：明确唯一装配命令与其变体规则；删除：不删示例；落点：README 与 charters/README 的表述统一（属文档一致性，不是新机制）；回读 R2；前置：无。
- **defer · AUTH-30 调用模式轴（model-invoked vs user-invoked）** — 理由：当前包没有机器路由面，机制无处附着；若未来包被做成 skill 包则成为前置；差异：产品入口是人工选择；保留：现状；改变：无；删除：无；落点：仅当包形态改变时；回读 R0；前置：补读 `matt:.agents/invocation.md` + `addy:docs/skill-anatomy.md`（后者本轨读了前 120 行）。
- **defer · AUTH-31 命名兼容与改名迁移** — 理由：包无版本化对外名，改名风险低；但 Profile/Method 名已出现在 Charters 与 examples 中，改名成本真实；差异：上游有改名 lineage 但无可执行 alias；保留：现状；改变：无；删除：无；落点：若引入版本化发布再处理；回读 R0；前置：补读 `matt:CHANGELOG.md` 相关条目（另见 PEND-06）。

### 2.2 BHV / META（行为、领域、规格、写作）

- **narrow · BHV-01 行为约定可观察化** — 理由：判据在，但没有最小结构，不同实例写出的行为约定质量差异大；差异：上游 to-spec 有六段模板；保留：判据与例子用法；改变：补最小字段（场景/交互/输出/异常/接受条件），不引入模板强制；删除：无；落点：behavior-domain profile 的方法入口或新方法；回读 R0；前置：补读 `skills/engineering/to-spec/SKILL.md`。
- **narrow · BHV-04 领域语义单一 owner** — 理由：原则在，"同一规则只应有一个 owner"没有落地形态；差异：上游 CONTEXT.md 给布局与惰性创建；保留：原则；改变：补文件形态（见 BHV-10）；删除：无；落点：同 BHV-10；回读 R0。
- **narrow · BHV-05 同名概念跨上下文** — 理由：产品只有"同名概念何时不同"的问句；差异：上游有 CONTEXT-MAP 间接层与 flagged-ambiguity register；保留：问句；改变：补指路形态；删除：无；落点：与 BHV-10 合并；回读 R0（本轨读过 `wait-what` 的 A 行）。
- **narrow · BHV-07 问题定义** — 理由：A/Voice 的四要素齐全，但人类诉求如何被"问出来"没有操作；差异：上游 interview-me 有置信度数字、一次一问、want vs should-want、Terminal Turn 与 95% 停止条件；保留：事实/推断/未知划分；改变：把访谈从"候选方法名"升为有停止条件的操作（与 META-05 合并）；删除：无；落点：intent-voice 绑定的方法；回读 R0；前置：补读 `addy:skills/interview-me/SKILL.md` + `grilling/SKILL.md`。
- **narrow · BHV-08 人类接受记录** — 理由：读回要求明确，但"记录什么字段"未定；差异：上游 handoff/to-questionnaire 有产物形态；保留：读回+记录；改变：补最小字段（决定/范围/条件/时点）；删除：无；落点：intent-voice 方法或 Charter 的 Acceptance 段；回读 R0。
- **defer · BHV-09 规格模板与阶段门** — 理由：产品刻意只做方法+Charter，"规格→计划→任务"分层属交付流水线，是否入包取决于 Owner 对包范围的判断；差异：产品无规格产物；保留：Plan 三件事；改变：无；删除：无；落点：若采纳则新方法，且必须与"不设固定阶段链"的既有立场调和；回读 R0；决定归属：Owner（范围）→ Driver（落点）。
- **adopt · BHV-10 领域文档形态（CONTEXT）** — 理由：C 的所有权在场而载体缺席，导致领域语义只能散落在 Charter/Plan 里；差异：上游有单/多上下文布局、惰性创建、原地更新、glossary-only 禁令；保留：C 的判断权与"不重写完整词典"；改变：新增文件形态；删除：不引入 EARS/规格内容；落点建议：`methods/domain-context.md` 或 behavior-domain 的支持文件；回读 R0（本轨读过 `CONTEXT.md` 行与 `codebase-design.md` 的 C 语义段）；前置：补读 `domain-modeling/SKILL.md` + `CONTEXT-FORMAT.md`。
- **defer · BHV-11 未定项路线图（wayfinder）** — 理由：与 META-05/META-06 相邻且更重（多会话载体），当前包无长周期对象；差异：产品只有"哪个未知会改变方向"；保留：现状；改变：无；删除：无；落点：若引入多会话 initiative 再处理；回读 R0；决定归属：Driver。
- **narrow · BHV-12 上下文工程** — 理由：产品声明 runtime 机制不属 Driver（profiles/driver.md），但上下文打包属方法层，归属未定；差异：上游有五级层级、打包策略、预算与压缩优先级；保留：共享引用的有界部分；改变：先明确归属（方法层 vs 包外），再决定是否吸收；删除：无；落点：待归属裁定；回读 R1；前置：补读 `addy:skills/context-engineering/SKILL.md`。
- **adopt · META-01 面向 agent 的写作纪律** — 理由：产品自身大量使用该文体（短句、判据式、"不要…"），但没有任何成文规则，导致新增文本风格漂移（校准中已见 M1 时代字样残留）；差异：上游有删除测试、leading word、一分支一触发、context vs cognitive load；保留：现有文体；改变：新增写作规则；删除：不删现有文本；落点建议：`docs/` 写作规则（优先）或 methods 附录；回读 R0（本轨读过 `writing-for-agents` 的 A 行与 `skill-anatomy` 部分）；前置：补读 `writing-for-agents/SKILL.md` + `SKILL-MECHANICS.md`。
- **defer · META-02 文档页固定框架** — 理由：当前只有单页门面，尚无多页文档面；差异：上游四节+路由职责；保留：现状；改变：无；删除：无；落点：若包扩展到多文档再处理；回读 R0；决定归属：Driver。
- **narrow · META-03 变更记录与发布血统** — 理由：产品用 M1–M5 叙述与 digest 表承担变更记录，读者需自行判断有效性；差异：上游 changeset 条目面向使用者、按 Minor/Patch/Major 分组；保留：过程记录；改变：把"当前有效"与"历史快照"分离标注；删除：不删历史；落点：README 状态段；回读 R2；前置：无。
- **defer · META-04 兼容标识符与弃用** — 理由：无版本化对外面，弃用机制无附着点；差异：上游有 deprecated 桶与公告规则；保留：现状；改变：无；删除：无；落点：与 AUTH-31 一起，若引入版本化再处理；回读 R0；决定归属：Driver。
- **adopt · META-05 决策树访谈** — 理由：产品两处提到"访谈/追问"候选方法但无正文，实际使用会出现问题数量与收敛标准不一致（上游 out-of-scope 正因此设"不设上限"政策）；差异：上游有 frontier、单问+推荐答案、事实/决定分工、同轮不依赖；保留：A/Voice 的问句；改变：把候选方法名升为可绑定方法；删除：不引入上限/计数；落点建议：`methods/grilling-interview.md`；回读 R2（本轨读了 `question-limits.md` 全文）+ R0（未读 grilling 原文）；前置：补读 `skills/productivity/grilling/SKILL.md` + `skills/engineering/grill-with-docs/SKILL.md`。
- **narrow · META-06 由讨论合成规格与工单** — 理由：产品定位是判断方法而非交付流水线，spec/ticket 分解仅作候选；差异：上游有 synthesis 契约、垂直切片、阻塞边、单上下文窗口尺寸；保留：Plan 三件事；改变：仅保留"由既有讨论合成、不重复访谈"这一条契约；删除：不引入标签与发布流；落点：META-05/06 合并为一个方法的边界条款；回读 R0；前置：补读 `to-spec`/`to-tickets`。

### 2.3 DES（设计/架构/类型/幂等/并发）

- **narrow · DES-03 depth 定义** — 理由：depth-as-leverage 已被吸收，但只保留一半（缺 locality），单独使用会偏向"更小接口"而不计维护收益；差异：上游保留 locality 与四原则；保留：leverage 定义；改变：补 locality；删除：不引入 Ousterhout 比值；落点：cross-module-design.md 的 depth 段；回读 R1（读过 `docs/engineering/codebase-design.md`）；前置：补读 `codebase-design/SKILL.md`。
- **narrow · DES-04 删除测试** — 理由：产品刻意不规定设计规则，但"何时不该加抽象"缺失会让 E 的设计自由度无判据；差异：上游用删除测试与两适配器规则；保留：不强行合并模块；改变：加一条自检问句（拿掉它，复杂度去哪）；删除：无；落点：cross-module-design.md §Method 3；回读 R1；前置：补读 `DEEPENING.md`。
- **narrow · DES-05 locality** — 理由：同 DES-03；差异：上游 locality 定义（改一次全场景同步）；保留：无；改变：并入 depth 段；删除：无；落点：同上；回读 R1。
- **adopt · DES-06 设计空间穷尽** — 理由：产品保留问句但显式不要求备选数量，结果是"有实质分歧时"缺少最低操作；差异：上游给 2–3 个可比较方案与"变体不算"判据；保留：不设固定数量、不绑并行 agent；改变：把"何时必须做多方案"写清（无先例的新交互/架构选择）；删除：不引入 DESIGN-IT-TWICE 的并行数；落点建议：cross-module-design.md 新增一节；回读 R0；前置：补读 `DESIGN-IT-TWICE.md` + `principle-exhaust-the-design-space/SKILL.md`。
- **adopt · DES-08 边界校验纪律** — 理由：产品只保留"错误语义可预测"，未规定校验位置，导致内部冗余校验与类型信任边界无判据；差异：上游把校验/收窄/错误处理放在系统边界、内部信任类型、解析函数是纯变换；保留：错误行为可预测；改变：补边界纪律；删除：无；落点：cross-module-design.md §Method 2/6；回读 R0；前置：补读 `principle-boundary-discipline/SKILL.md`。
- **narrow · DES-09 类型系统纪律** — 理由：与 C 的不变量语义直接相关，但跨语言规则面太大，且产品 §Limits 已明确不收；差异：上游有非法状态不可表示、品牌类型、parse-don't-validate、穷尽性；保留：§Limits 的克制；改变：只收与 C 不变量直接对应的"非法状态不可表示"一条；删除：不收语言特定清单；落点：behavior-domain（C）或 cross-module-design 的一句判据；回读 R0；前置：补读 `principle-type-system-discipline/SKILL.md`。
- **adopt · DES-10 幂等与崩溃安全** — 理由：计划 §5 点名不得剥掉该细节，而当前产品零覆盖；这是本轨最大缺口之一；差异：上游有两必答问、三条测试、收敛式启动、按内容等价清理；保留：不引入的"无任务需要则不导入"克制由 §Limits 承担（本机制按需绑定）；改变：新增；删除：不删 §Limits 的克制句，但需在方法内声明适用范围；落点建议：`methods/idempotency-and-recovery.md`（或 cross-module-design 的持久化节，容量不足则独立）；回读 R1（读过 `store.ts` 的原子写/锁实现 + `x-money` 的幂等键规则）；前置：补读 `principle-make-operations-idempotent/SKILL.md`。
- **defer · DES-11 原子写实现** — 理由：属实现级技巧，是否入包取决于包是否承担持久化职责（当前不承担）；差异：上游有同目录临时文件+wx+rename+finally、写缺失、结构校验；保留：无；改变：无；删除：无；落点：若 DES-10 采纳则作为其"实现示例"附注（保留 intent/attempt/原子认领细节，不得简化掉）；回读 R2；决定归属：Driver。
- **defer · DES-12 锁与陈旧锁接管** — 理由：产品显式把 runtime 机制排除在 Driver 外，但 E 的实现自愈锁属责任边界内的实现细节，归属需裁定；差异：上游有 PID 存活判定、EEXIST 重试、force 路径、释放归属校验；保留：§4 的排除声明；改变：无；删除：无；落点：同 DES-10（示例）或明确登记为包外；回读 R2；决定归属：Driver。
- **adopt · DES-13 共享可变状态先分离再串行化** — 理由：产品只有"单写者"问题，没有操作，并行写者场景下会重复出现同一 failure；差异：上游有先问"是否需要同一可变对象"、消除共享手法、结构性串行化、反例；保留：单写者问题与写集问句；改变：新增操作；删除：无；落点建议：与 DES-10 同方法（同一节）或 Driver 的编排附件；回读 R1（读过 `store.ts`）+R0（principle 未读）；前置：补读 `principle-separate-before-serializing-shared-state/SKILL.md`。
- **adopt · DES-14 迁移调用者并删旧 API** — 理由：与产品"只增不改"的默认构成真实张力，缺适用边界会让实例要么永不删除、要么破坏兼容；差异：上游给出适用条件、同波迁移-删除、限时适配器；保留：兼容优先默认；改变：新增适用边界与操作；删除：不删兼容原则；落点建议：cross-module-design.md §Method 6（兼容段）扩写；回读 R0；前置：补读 `principle-migrate-callers-then-delete-legacy-apis/SKILL.md` + `addy:skills/deprecation-and-migration/SKILL.md`。
- **adopt · DES-15 兼容/恢复操作面** — 理由：责任路由已覆盖（Backbone §5），操作面缺失会让"回滚判据/不可逆点"在真实迁移中靠临场发挥；差异：上游有 expand-contract、绞杀者、双读双写、回滚判据；保留：§5 的路由示例；改变：新增操作；删除：无；落点建议：与 DES-14 合并为"迁移与兼容"方法；回读 R0；前置：补读 `addy:skills/deprecation-and-migration/SKILL.md` + `matt:skills/engineering/to-tickets/SKILL.md` 的 expand-migrate-contract 段。
- **narrow · DES-16 减法优先** — 理由：产品有"不要加"的反面纪律，"何时删/折叠"没有正面判据；差异：上游有按观察到的用法设计、无第二实现的适配器折叠、留桩与删除取舍；保留：§Limits 的克制；改变：补正面判据；删除：无；落点：cross-module-design.md §Limits 附近；回读 R0；前置：补读 `principle-subtract-before-you-add/SKILL.md` + `principle-laziness-protocol/SKILL.md`。
- **narrow · DES-17 读者负担两轴** — 理由：与 DES-03/04/05 同源，产品只有 leverage；差异：上游有两轴与状态作用域阶梯；保留：无；改变：并入 depth/locality 一节；删除：无；落点：cross-module-design.md；回读 R0。
- **narrow · DES-18 从第一性原理重设计** — 理由：与兼容默认有张力，但"何时重设计而非外挂"的产品判据缺失；差异：上游有"从零写会怎样"与变更传播清单；保留：兼容优先；改变：补触发与传播清单；删除：无；落点：与 DES-14/15 同方法；回读 R0。
- **adopt · DES-19 前提攻击** — 理由：产品给了 E"挑战上游"的权利但没有触发判据，导致同一前提反复失败时仍继续打补丁；差异：上游有同闸门失败触发、前提书写、actor 普查、停止条件；保留：挑战权与返回责任方；改变：新增操作；删除：无；落点建议：local-defect-feedback-loop.md 新增一节，或独立方法；回读 R0；前置：补读 `principle-attack-the-premise/SKILL.md`。
- **adopt · DES-20 把教训编码进结构** — 理由：本包是大量散文规则的集合，正是该机制的适用对象；若采纳可减少规则漂移（如"待 M4"字样、三处装配示例）；差异：上游有第二次写同一指令的自问、机制强度阶梯、编码后删指令、反馈环；保留：现有全部正文；改变：新增规则（并授权未来把重复规则转为检查）；删除：编码后删除被替代的散文指令（作者需在落地时逐条登记）；落点建议：`docs/` 维护规则 + 可选校验脚本；回读 R1（读过 `.changeset/retro-deterministic-checks.md` 全文与 `create-plugin` 质量门 A 行）；前置：补读 `principle-encode-lessons-in-structure/SKILL.md`。
- **narrow · DES-21 领域建模为数据结构** — 理由：C 的所有权在场，操作清单缺席；差异：上游有结构清单与克制规则；保留：C 判断权；改变：作为 C 方法的实现手段补入；删除：无；落点：与 BHV-10 同方法；回读 R0。
- **narrow · DES-22 基础性思考** — 理由：与 DES-16/21 同源，单独列出会造成重复；差异：上游有数据形状先行、脚手架优先顺序；保留：无；改变：并入 DES-16/21；删除：不单独成节；落点：同上；回读 R0。
- **narrow · DES-23 面向结果的执行** — 理由：产品默认"增量可编译"（addy 侧），与"允许有计划的中间破损"相反；两条默认不同时陈述会让下游矛盾；差异：上游有护栏（计划、边界、可回滚、完成时完整验证）；保留：增量默认；改变：补适用边界；删除：无；落点：cross-module-design.md 或 implementation profile；回读 R0；前置：补读 `principle-outcome-oriented-execution/SKILL.md` + `addy:skills/incremental-implementation/SKILL.md`。
- **adopt · DES-24 制造杠杆** — 理由：非平凡重复工作缺工具化判据，实践中会用手工批量操作；差异：上游有单一可重跑工件、先手工学配方、扇出时把配方置于子代理写范围外；保留：不加不必要抽象的克制；改变：新增操作（并要求产出文件）；删除：无；落点建议：implementation 侧方法或新方法；回读 R0。
- **narrow · DES-25 薄切片与范围纪律** — 理由：产品明确不设阶段链，切片操作缺席；差异：上游有垂直切片/契约先行/风险优先与六条规则；保留：不设固定阶段链；改变：只补切片选择判据与可验证状态定义；删除：不引入六条规则全文；落点：local-defect-feedback-loop.md 的 §Use 或 technical-planning；回读 R0。
- **adopt · DES-26 一次性原型** — 理由：产品只有"可逆探索"一句，原型的目的声明/丢弃规则/证据保留缺失；差异：上游有分支路由、throwaway-and-marked、不持久化、留答案作 primary source；保留：可逆探索；改变：新增原型方法；删除：无；落点建议：`methods/prototype.md`；回读 R0；前置：补读 `prototype/SKILL.md` + `LOGIC.md`/`UI.md`。
- **narrow · DES-27 代码简化** — 理由：产品只有"行为不变"原则；差异：上游有五原则+四步+语言特定 before/after；保留：行为不变与最小改动；改变：补 Chesterton's Fence 与增量施加；删除：不收语言特定例子（避免正文膨胀）；落点：implementation profile 的方法入口或新方法；回读 R0；前置：补读 `addy:skills/code-simplification/SKILL.md`。
- **adopt · DES-28 质量约束写成可执行契约** — 理由：产品没有"把质量条写成可执行契约"的载体，与 DES-20 互补；差异：上游有 CONSTRAINTS.md 四类条目、棘轮、生命周期接入、Exceptions 到期；保留：measure/threshold 只针对单条 claim 的既有设计；改变：新增约束文件形态；删除：无；落点建议：新方法或 Charter 附件；回读 R0；前置：补读 `addy:skills/constraint-driven-development/SKILL.md` + `references/floor-guard.md`。

### 2.4 DBG（调试/缺陷/测试）

- **adopt · DBG-04 no-loop-no-hypothesis gate + loop 阶梯** — 理由：产品只要求"先复现"，但假设阶段没有门；差异：上游把 loop 建成设为前置，并给出十级构造阶梯与每级判据；保留：复现优先与最小化；改变：把"没有 loop 不进入假设"写成硬判据 + 阶梯；删除：无；落点建议：local-defect-feedback-loop.md §Method 2 扩写；回读 R0（本轨未读 matt diagnosing-bugs 原文）；前置：补读 `matt:skills/engineering/diagnosing-bugs/SKILL.md` 全文（含 redact 段）。
- **adopt · DBG-05 redact-first** — 理由：证据采集前脱敏是安全边界，产品零覆盖，而 local-defect 明确要求"report exact commands, observations"；差异：上游有环境变量构造与信号行摘录法；保留：如实记录；改变：在记录前插入脱敏步骤；删除：无；落点建议：local-defect-feedback-loop.md §Method 5 + Charter 的工具/动作段；回读 R0；前置：同 DBG-04。
- **adopt · DBG-06 flake 处理** — 理由：产品只记录条件，没有复现率目标与"先怀疑观察方法"的顺序；差异：上游有提高复现率、并发加压、隔离前记录要求；保留：条件记录；改变：新增顺序与目标；删除：无；落点：local-defect-feedback-loop.md §Method 2；回读 R0。
- **adopt · DBG-09 根因修复 vs 症状抑制** — 理由：产品有"修因"但没有反症状修复的判据与同形模式排查；差异：上游有长注释即代码错的判据、grep 全量修、仪表优先；保留：修因；改变：补判据与排查；删除：无；落点：local-defect-feedback-loop.md §Method 4；回读 R0（本轨读了 `store.ts` 的失败模式但未读 principle 原文）；前置：补读 `principle-fix-root-causes/SKILL.md`。
- **narrow · DBG-10 重启/间歇类缺陷专项** — 理由：与 DES-12 相邻，属 E 的实现卫生；差异：上游把"陈旧持久状态"设为第一怀疑对象；保留：无；改变：作为 DES-10 的一个已知失败模式登记；删除：无；落点：DES-10 方法的反例/失败模式节；回读 R1（读过 `store.ts`）；前置：补读 `principle-fix-root-causes/SKILL.md`。
- **narrow · DBG-11 安全降级与埋点** — 理由：与 CONC-03 相邻，产品零覆盖；差异：上游有降级模式与埋点指南；保留：无；改变：并入 CONC-03；删除：不单独成节；落点：可观测性方法（若采纳）；回读 R0。
- **narrow · DBG-12 错误类型分诊** — 理由：通用循环已覆盖主流程，分类清单是效率增益；差异：上游按测试/构建/运行时分类；保留：通用循环；改变：加三步分诊入口；删除：不收全套清单；落点：local-defect-feedback-loop.md §Use；回读 R1（读过 addy 调试技能前 60 行 + 标题）；前置：补读 addy `debugging-and-error-recovery/SKILL.md` 全文。
- **adopt · DBG-13 人机协作复现夹具** — 理由：需要人类动作的复现步骤在真实缺陷中常见，产品只有"Charter 有 permitted commands"这一层；差异：上游有 step/capture 助手、KEY=VALUE 回传、凭据不进入脚本的规则；保留：Charter 工具段；改变：新增夹具形态；删除：无；落点建议：local-defect-feedback-loop.md 的支撑文件或 Charter 附件；回读 R2（读过 hitl-loop.template.sh 全文）；前置：补读 `wizard/template.sh`（同族）。
- **adopt · DBG-14 测试先行次序（Prove-It）** — 理由：产品用"observation"而非"test"，次序语义偏弱；差异：上游有明确的"失败测试先于改生产代码"与"因预期原因失败"的确认；保留：§Limits 的"不要求每个红测试一次提交"；改变：把次序写成判据（在方法适用范围成立时）；删除：不引入"六步 TDD"全套；落点建议：local-defect-feedback-loop.md §Method 1/4；回读 R0（本轨读了 `tdd/mocking.md` 与 A 行）；前置：补读 `matt:skills/engineering/tdd/SKILL.md` + `cursor:pstack/skills/tdd/SKILL.md`（注意两处适用范围相反：一个默认 gate、一个明确请求才用——落地时必须在正文里给出适用边界，不得二选一而不说明）。
- **adopt · DBG-15 好测试判据** — 理由：产品只有"在行为接缝加回归覆盖"，没有"什么算好测试"，会出现实现耦合测试通过而缺陷漏过；差异：上游有行为判据、同义反复/实现耦合/横向切片三反模式、弱断言清单、测试尺寸；保留：接缝选择；改变：新增判据（含"若导入的每个函数都返回 undefined 还会通过吗"这一句）；删除：无；落点建议：与 DBG-14 同一方法；回读 R0；前置：补读 `matt:skills/engineering/tdd/SKILL.md` + `tests.md` + `principle-test-behavior-not-implementation/SKILL.md`。
- **adopt · DBG-16 mock 纪律** — 理由：产品没有任何 mock 规则，而 cross-module-design 已要求"按依赖形状选测试路径"，两者相邻；差异：上游有系统边界清单与可 mock 设计两规则；保留：依赖形状选测试路径；改变：新增 mock 边界与设计规则；删除：无；落点建议：cross-module-design.md §Method 3 扩写；回读 R2（读过 `tdd/mocking.md` 全文）；前置：在采纳时指认单源（上游两处重复：`mocking.md` 与 `codebase-design/SKILL.md`）。
- **narrow · DBG-18 无法复现时的替代路径** — 理由：产品给了出口但无阶梯；差异：上游按"该代码路径既有的最近测试类型优先"给出替代序列；保留：出口；改变：补阶梯与跳过记录要求；删除：无；落点：与 DBG-04/14 同方法；回读 R0。

### 2.5 EVID（证据/验证/评审/评测）

- **narrow · EVID-06 可复现记录** — 理由：产品要求如实记录但无格式；差异：上游有单行决策 TSV 与受控结果值；保留：如实记录；改变：补最小记录格式（见 EVID-23）；删除：无；落点：behavior-claim-evaluation.md §Method 4；回读 R0；前置：补读 `show-me-your-work/SKILL.md` + `scripts/log.sh`。
- **adopt · EVID-07 负控制** — 理由：产品已在 F profile 提出"关键负控制是什么"，但无设计方法，实践中容易只做正向验证；差异：上游有"若 claim 为假哪个观察必须变红"、变异/回退控制、无效控制识别；保留：三态与无效观察判定；改变：新增负控制设计节；删除：无；落点建议：behavior-claim-evaluation.md 新增 §Method；回读 R0；前置：补读 `principle-prove-it-works/SKILL.md` + `tdd/SKILL.md`。
- **adopt · EVID-08 证据阶梯** — 理由：产品把"证据"当同质概念，缺强度分级，导致"指到行"与"运行中复现"被同等对待；差异：上游五级阶梯 + 每项如实标注停在哪级 + "影响清单无价值"判据 + grep 停住处排查面；保留：三态判定；改变：新增阶梯与标注要求；删除：无；落点建议：behavior-claim-evaluation.md 或 F profile；回读 R0；前置：补读 `blast-radius/SKILL.md`。
- **adopt · EVID-09 直接检查真实工件** — 理由：产品有相邻原则（不得从未验证日志推断根因），但无真值优先级与"比较脚本化"要求；差异：上游有真值优先级、可重跑脚本工件、怀疑观察方法的顺序；保留：原则；改变：补优先级表；删除：无；落点：behavior-claim-evaluation.md §Method 2；回读 R0；前置：补读 `principle-prove-it-works/SKILL.md`。
- **narrow · EVID-10 逐项测量诚实** — 理由：产品覆盖"缺证据不等于 PASS"，但没有 per-field 标注与"未测项呈现规则"；差异：上游有 not-measured 标注与可复算原始数件清单；保留：原则；改变：补呈现规则；删除：无；落点：behavior-claim-evaluation.md §Method 4；回读 R1（读过 addy `agents/web-performance-auditor.md` 的 A 行，未读原文）；前置：补读该文件。
- **adopt · EVID-12 评审五轴与流程** — 理由：产品把"评价"抽象为三态判定，没有评审工作面，实际评审会退化为随机检查；差异：上游有五轴、五步流程（含"先看测试"与"验证其验证"）、变更规模纪律；保留：三态与独立性；改变：新增评审方法；删除：不接受把评审降格为"找问题清单"；落点建议：`methods/code-review.md`；回读 R0；前置：补读 addy `code-review-and-quality/SKILL.md` + `matt:skills/engineering/code-review/SKILL.md` + `docs/engineering/code-review.md`。
- **narrow · EVID-13 发现分类与收敛** — 理由：多评审者一致性可提高漏项发现，但产品明确禁止用多模型证明独立性；差异：上游有分档、2+ 一致即最高信号、never-rerank；保留：独立性立场（优先）；改变：只吸收"分类与合并同义、分歧记录"部分，不吸收"多模型=更强结论"；删除：不收独立性问题上的多模型主张；落点：与 EVID-12 同方法的"多评审者"节；回读 R0；前置：补读 `interrogate/SKILL.md` + `arena/SKILL.md`。
- **narrow · EVID-14 大 diff 评审分工** — 理由：与 FAM-H 编排重叠，产品声明 runtime 不在包内；差异：上游有并行 reviewer、只读约束、按 rubric 评分；保留：独立性立场；改变：只保留"只读评审者"与"按标签评分"两条，不引入扇出机制；删除：不引入模型池与跨评者选择；落点：与 EVID-12 同方法；回读 R0。
- **adopt · EVID-15 Definition of Done** — 理由：产品有"关闭对象由委托定义"，但没有常备清单，导致关闭证据依赖临场枚举；差异：上游有 DoD 五类清单与"DoD 不得替代验收标准"的红旗；保留：关闭对象由委托定义；改变：新增 DoD 形态（明确其为 project-wide 门槛）；删除：无；落点建议：`references/` 或 Charter 附件；回读 R1（A 行 + 产品）；前置：补读 `addy:references/definition-of-done.md`。
- **defer · EVID-16 触发评测** — 理由：当前包无技能路由面，评测对象不存在；差异：产品无对应物；保留：无；改变：无；删除：无；落点：若未来做 skill 包再处理；回读 R1（读过一个 case 全文）；决定归属：Driver。
- **defer · EVID-17 执行评测** — 理由：同上；差异：上游用 fixture+可验证期望陈述，产品无评测框架；保留：无；改变：无；删除：无；落点：同 EVID-16（可作为"方法生效性"的验证手段备选）；回读 R2（读过 `test-driven-development.json`）+R1（fixtures 未读）；决定归属：Driver。
- **defer · EVID-18 评分器** — 理由：同 EVID-16/17；差异：上游有 not-fired grader 等；保留：无；改变：无；删除：无；落点：同；回读 R0；决定归属：Driver。
- **defer · EVID-19 技能影响评估表（空表）** — 理由：机制已声明但表体为空，且数据源在 `.gitignore` 内不可从 pin 复核；本轨无法判定其机制是否成立；差异：不适用；保留：无；改变：无；删除：无；落点：不落（缺证据）；回读 R1（A 行 + README）；决定归属：Driver（建议登记为已知未完成项）。
- **narrow · EVID-20 性能指标诚实** — 理由：与 EVID-10 同源；差异：上游有 Quick/Deep 双模式与 scorecard；保留：无；改变：并入 EVID-10；删除：不收性能测量方法（见 CONC-02）；落点：behavior-claim-evaluation.md；回读 R0。
- **narrow · EVID-21 合并冲突保持双方意图** — 理由：属 E 操作面，产品无 VCS 层方法；差异：上游有逐 hunk 判据、不发明、不 --abort、锁文件重生成、检查顺序；保留：无；改变：作为"实现事实发现"的一个已知场景登记；删除：不引入完整冲突方法；落点：implementation profile 或方法附件；回读 R0；前置：补读 `matt:skills/engineering/resolving-merge-conflicts/SKILL.md`。
- **defer · EVID-22 CI 失败回路** — 理由：与 FAM-F 交付面重叠，产品无 CI 语境；差异：上游有检查集真源、一次一个失败、最小修复；保留：无；改变：无；删除：无；落点：与 DLV 类一起由 Owner 决定是否入包；回读 R0；决定归属：Driver。
- **narrow · EVID-23 可评审记录格式** — 理由：产品要求如实记录但读者要自行重建结构；差异：上游有单行 TSV 与受控结果值；保留：记录要求；改变：补最小格式；删除：不引入 PR 载体；落点：behavior-claim-evaluation.md §Method 4；回读 R0。

### 2.6 DLV / PKG（交付、平台包装、连接器）

- **narrow · DLV-01 提交纪律** — 理由：产品无 VCS 层，但本仓自身有提交纪律（AGENTS.md Git Discipline）；差异：上游有原子提交、消息规范、提交前卫生；保留：全局 AGENTS.md 的 Git 纪律；改变：若要吸收则只在包外文档，不进 methods；删除：不引入分支策略全文；落点：仓库级 docs（非包内方法）；回读 R0。
- **adopt · DLV-02 危险 git 命令护栏** — 理由：安全边界要求"prefer reversible changes"，但包内无任何具体危险命令清单；上游以 hook 结构强制；差异：产品只有一般性安全边界；保留：一般边界；改变：新增危险命令清单（清单可进 docs/规则，hook 属工具层）；删除：无；落点建议：`docs/` 安全规则；回读 R0；前置：补读 `matt:skills/misc/git-guardrails-claude-code/SKILL.md` + `block-dangerous-git.sh`。
- **defer · DLV-03 PR 可评审性** — 理由：无 PR 载体；差异：上游有噪声 commit 识别与历史清理前置；保留：无；改变：无；删除：无；落点：与交付面一起由 Owner 决定；回读 R0。
- **defer · DLV-04 PR 正文模板** — 理由：产品已有 before/after 对照语义，但载体不存在；差异：上游有摘要视觉/证据对/Merge Danger；保留：对照语义；改变：无；删除：无；落点：待交付面决定；回读 R0；决定归属：Owner/Driver。
- **narrow · DLV-05 worktree 隔离** — 理由：产品有写集问题，worktree 属实现环境，落点未定；差异：上游有独立 worktree、干净树前置、清理；保留：写集问句；改变：仅登记为"若引入并行实现则需的操作"；删除：无；落点：Driver 编排附件；回读 R0。
- **defer · DLV-06 发布前清单与放量** — 理由：产品明确"关闭≠发布授权"，发布操作面属包外；差异：上游有清单、放量阈值、错误预算、回滚模板；保留：关闭≠发布；改变：无；删除：无；落点：登记为包外（建议在 README 的"不授权"句旁列明）；回读 R1；决定归属：Owner。
- **adopt · DLV-07 交付后回看与自我改进** — 理由：本包已有事实上的回看对象（每个 phase 的 overnight 记录）但无分类与落点规则，改进容易停留在叙述；差异：上游有七类候选改进、确定性检查优先、无护栏即 finding；保留：overnight 记录；改变：新增回看分类与落点规则（与 DES-20 合并实施）；删除：不保留"只写报告不落检查"的做法；落点建议：`docs/` 维护规则或 retro 方法；回读 R1（读过 `.changeset/retro-deterministic-checks.md`）；前置：补读 `matt:skills/in-progress/retro/SKILL.md`。
- **narrow · DLV-08 版本与 tag** — 理由：产品的 digest 纪律覆盖"同一对象两处标识"，缺版本化发布；差异：上游有 `--check` 漂移检测与语义化版本；保留：digest；改变：登记"无版本化"为现状风险；删除：无；落点：README 状态段；回读 R2；前置：补读 `matt:scripts/sync-plugin-version.mjs`（若采纳机器检查）。
- **adopt · DLV-09 面向人类的操作向导（wizard）** — 理由：人类保留项在包内只到"经 Voice"，缺"让人类执行的步骤如何被脚本化并回收结果"；差异：上游有模板驱动的 UX 契约、默认一次性、可提交例外；保留：Voice 路由；改变：新增向导形态（与 DBG-13 同族）；删除：无；落点建议：`methods/human-step-wizard.md` 或 Charter 附件；回读 R0；前置：补读 `wizard/SKILL.md` + `template.sh`。
- **adopt · DLV-10 会话级交接产物** — 理由：产品有交接原则（短消息承载路由、事实落产物），但没有交接文档的形态与落盘规则，跨会话续接会丢失"下一步"；差异：上游有临时目录、必含节、引用而非复制、脱敏、按参数裁剪；保留：路由与产物指针；改变：新增交接形态；删除：不落工作区（遵守上游的落盘规则）；落点建议：driver 侧方法或模板文件；回读 R0；前置：补读 `matt:skills/productivity/handoff/SKILL.md` + `claude-handoff/SKILL.md`。
- **adopt · DLV-11 历史研究检索** — 理由：产品要求"引用的是哪一版上游结论"但没有检索方法，实际会退化为读当前文件；差异：上游有代码锚、blame/log --follow/pickaxe、"为什么这样设计"的调查面；保留：引用版本要求；改变：新增检索方法；删除：无；落点建议：technical-planning 的方法附件；回读 R0；前置：补读 `cursor:pstack/skills/why/SKILL.md`。
- **narrow · DLV-12 研究纪律** — 理由：本包有 pin+digest 实践，但没有研究方法的成文规则；差异：上游有一手来源、claim→owner、单一带引用产出；保留：pin+digest；改变：补最小研究规则；删除：不引入笔记系统；落点：docs 或方法附件；回读 R0。
- **defer · PKG-01 插件注册与组件装配面** — 理由：当前包无 manifest，装配靠 cat；是否引入声明式组件面取决于分发形态；差异：上游有组件字段与名字相等校验；保留：cat 装配；改变：无；删除：无；落点：若包形态变化；回读 R1（读过 addy/matt manifest A 行）；决定归属：Owner。
- **defer · PKG-02 客户端版本门** — 理由：平台专有，当前包不面向多宿主；差异：上游有 `minClientVersions`（含 `never`）；保留：无；改变：无；删除：无；落点：同 PKG-01；回读 R2（读过 x-money plugin.json 全文）；决定归属：Owner。
- **narrow · PKG-03 校验器诚实边界** — 理由：产品对"无机器检查"有意识但没有登记形态，读者会高估一致性保障；差异：上游虽窄但明确、并把未覆盖面交给 prose checklist；保留：README 的"无 validator"声明；改变：把"哪些不变量有检查、哪些只有散文"写成一条声明；删除：无；落点：README/authority README；回读 R1（读过 cursor validate-plugins 的 A 行）；前置：补读 `cursor:scripts/validate-plugins.mjs`。
- **defer · PKG-04 MCP 传输模型** — 理由：当前包不接外部服务；作为"第三方集成风险"机制的价值属未来形态；差异：上游区分 http/stdio（本地执行）；保留：无；改变：无；删除：无；落点：若引入连接器再处理；回读 R2（读过 xero mcp.json/README）；决定归属：Owner/Driver。
- **adopt · PKG-05 凭据形态与最小面** — 理由：安全边界要求保护 secrets，产品只有"无密钥"类禁令，没有凭据形态与撤销路径；差异：上游有四种注入形态、variables 声明、`${VAR}` 间接、撤销面；保留：禁令；改变：新增凭据形态说明（用于评审与 Charter 工具段）；删除：无；落点建议：Charter 的 Tools/Actions 段参考或 docs 安全规则；回读 R2（读过 xero 三件套）；前置：补读 brevo/docusign/x 的 A 行对应的原文（若要把四类写全）。
- **adopt · PKG-06 权限与作用域最小化 + 按动作批准** — 理由：产品的"consequential action 需单独授权"目前只有原则，缺"一次只批一个、变更重批、拒绝不得重试"的操作；差异：上游有 scope 收窄、逐动作批准、拒绝后不得重试、admin 二步门；保留：需单独授权的原则；改变：新增操作条款；删除：无；落点建议：Charter 模板的"Tools and actions"扩写 + docs 安全规则；回读 R1（读过 x-money 前 80 行）；前置：补读 `x-money-guide/SKILL.md` 全文 + `third_party/x/README.md` + 一个 admin 门控 connector README。
- **narrow · PKG-07 副作用显式披露** — 理由：产品有风险接受归属，但没有"能力清单须标注副作用"的呈现规则；差异：上游 connector README 在文首标注 live 效果；保留：风险归属；改变：补呈现规则（一条即可）；删除：无；落点：docs 安全规则或 Charter 输入要求；回读 R1（读了 xero/coinbase 的 A 行）；前置：补读一个 money connector README 原文。
- **narrow · PKG-08 工具面权威** — 理由：与 EVID-09 同族；差异：上游明确"server 是真源、不得假定能力、按账户变化、结果用自己话转述"；保留：真源优先原则；改变：并入 EVID-09/behavior-claim-evaluation；删除：无；落点：behavior-claim-evaluation.md；回读 R1。
- **narrow · PKG-09 第三方材料处理** — 理由：本包用 digest 保证字节一致，但无第三方材料政策；差异：上游逐条留账、资产引用一致性；保留：digest；改变：若包引入第三方内容再补政策；删除：无；落点：docs 或 README；回读 R2（读过 header §5/§7 与 ahrefs 路径）。
- **narrow · PKG-10 未完成形态显式声明** — 理由：本包用大量"候选/未接受"叙述承担同一功能（M1 字样、M4/M5 双摘要），没有统一标记，读者需自行判断；差异：上游用 Status 引用块 + 桶语义；保留：候选/接受区分；改变：补统一标记规则（候选/接受/历史快照三类）；删除：不删历史；落点：README + methods/README；回读 R2（读过 docs-canvas SKILL 与产品 README）；前置：补读 `matt:skills/in-progress/README.md`（A 行已读）。
- **narrow · PKG-11 跨插件重复与漂移面** — 理由：本包已用 digest 区分同一对象两处身份（thermo-nuclear 重复已在 A 侧记录且本轨实测同一），但没有"重复内容单源判定"规则；差异：上游把重复记录为漂移面而不合并；保留：digest；改变：补单源判定规则；删除：不强制合并；落点：docs 维护规则；回读 R2（实测 sha256）；前置：无。
- **narrow · PKG-12 组件可发现性与质量门** — 理由：本包目录约定是隐式的（靠 README 叙述），新增文件缺少位置规则；差异：上游有路径合法性与"声明必须对应真实文件"；保留：目录约定；改变：把约定写入 README 或 docs 规则；删除：不引入校验器（与 PKG-03 一致）；落点：professional-workflow/README；回读 R1；前置：补读 `cursor:create-plugin/rules/plugin-quality-gates.mdc`。

### 2.7 ORC / HIT / CONC / SKL / FMT / GOV / PEND

- **narrow · ORC-01 编排者归属与调用图** — 理由：产品以责任路由替代角色图，是否需要调用图取决于未来是否引入可执行编排；差异：上游有 persona 不得互调与技能必经跳；保留：Driver 路由；改变：仅保留"不得新增路由面/不得双路由"一条（与 FMT-07 合并）；删除：不引入调用图；落点：Driver profile 或 docs；回读 R1（读过 `docs/engineering/codebase-design.md` 的调试页面对照但非本文件）；前置：补读 `addy:references/orchestration-patterns.md`。
- **narrow · ORC-02 并行扇出与合并** — 理由：产品有写集问题，操作面缺失；差异：上游有完成谓词、必返工件、独立输出路径、测量简报内容；保留：写集问题；改变：仅保留"先定完成谓词与必返工件"一条（与 ORC-11/12 合并）；删除：不引入扇出机制；落点：Driver 编排附件；回读 R0；前置：补读 `swarm/SKILL.md`。
- **defer · ORC-03 扇出形态与规模** — 理由：产品明确不设固定并行数，形态选择属 runtime 编排；差异：上游有切片/竞速/混合与判优；保留：不设固定数量；改变：无；删除：无；落点：包外；回读 R0；决定归属：Owner/Driver。
- **narrow · ORC-04 上下文隔离与保全** — 理由：与 BHV-12 同源，归属未定；差异：上游有隔离判据与摘要内容要求；保留：有界引用；改变：先定归属再决定；删除：无；落点：待定；回读 R0。
- **reject · ORC-05 planner/worker 隔离模型** — 理由：产品在 `authority/RESPONSIBILITY-BACKBONE.md` §4 与 `profiles/driver.md` 明确"不定义进程/并发/队列/锁/重试"、"不建固定 Role matrix"，该机制与本包已接受的边界直接冲突；差异：上游是完整的云端编排模型（克隆隔离、无终态、handoff 传播）；保留：产品的责任路由；改变：不改变；删除：无；落点：不落；回读 R2（读过 `orchestrate/SKILL.md` 前 60 行 + 产品全文）；前置：无（若 Owner 要重构包边界则需重新评估）。
- **reject · ORC-06 长跑循环状态协议** — 理由：同 ORC-05，属 runtime 机制且产品显式排除；差异：上游有状态文件契约与 hook 判定；保留：Driver 的"有界循环而非递归"精神（产品已有"不能在无证据时继续假设"的同类约束）；改变：不改变；删除：无；落点：不落；回读 R1（A 行）；前置：无。
- **defer · ORC-08 会话史挖掘** — 理由：涉及隐私与范围授权，产品无历史挖掘机制；差异：上游有时窗/主题/工作区锁定与只读约束；保留：无；改变：无；删除：无；落点：若做多会话续接再处理；回读 R0；决定归属：Owner（授权面）。
- **narrow · ORC-09 会话自评** — 理由：与 DLV-07 重叠；差异：上游有三评审维度；保留：无；改变：并入 DLV-07 的维度设计；删除：不单独成节；落点：DLV-07 方法；回读 R0。
- **defer · ORC-10 记忆维护** — 理由：本包已有 AGENTS.md 人工维护纪律，自动化维护是否引入取决于工具面；差异：上游把更新委托给子代理并设阈值；保留：人工纪律；改变：无；删除：无；落点：若引入自动化再处理；回读 R1（A 行）；决定归属：Driver。
- **narrow · ORC-11 任务图与稀疏通信** — 理由：与 AUTH-06/ORC-02 同族；差异：上游有 ready frontier、上下文指针通信、票尺寸；保留：Plan 三件事；改变：仅保留"票尺寸=一个上下文窗口"这一条尺寸判据；删除：不引入任务图工具；落点：Plan 方法；回读 R0。
- **narrow · ORC-12 验证夹具维护** — 理由：产品有"复用评价须确认覆盖"原则，缺夹具维护；差异：上游有特性→源入口→配方的索引与漂移扫描；保留：复用确认；改变：补"落盘可重跑配方"一条（与 DLV-11 相邻）；删除：不引入索引工具；落点：behavior-claim-evaluation.md 或 docs；回读 R0。
- **reject · ORC-13 自动运行与安全暂停** — 理由：runtime 编排，产品显式排除；差异：上游有 autopilot 分级与 pause-safely；保留：无；改变：不改变；删除：无；落点：不落；回读 R1（A 行）；前置：无。
- **narrow · HIT-01 理解失败重述协议** — 理由：产品有"用自己的话复述"但没有触发与格式；差异：上游有点名理解失败、要求重讲、简化语言、必须复用术语表；保留：读回原则；改变：补最小协议（复用 CONTEXT 术语一条与 BHV-10 联动）；删除：不引入完整语言标准；落点：intent-voice 方法；回读 R1（A 行）；前置：补读 `matt:skills/productivity/wait-what/SKILL.md`。
- **defer · HIT-02 反向提问（问卷）** — 理由：产品只覆盖 Owner 取舍，向第三方取输入的场景未在范围内；差异：上游有收件人识别与 done-when；保留：无；改变：无；删除：无；落点：若扩展输入面再处理；回读 R0；决定归属：Driver。
- **reject · HIT-03 教学系统** — 理由：本包定位是责任与判断，不含教学或学习工作区；差异：上游是完整教学契约；保留：无；改变：不改变；删除：无；落点：不落；回读 R0；前置：无。
- **defer · HIT-04 长文写作方法** — 理由：属写作方法，落点可能不在包内（本包正文为中文，上游方法面向英文技术写作）；差异：上游有相位与增量写作规则；保留：无；改变：无；删除：无；落点：仓库 docs 或包外；回读 R0；决定归属：Driver。
- **defer · HIT-05 技术写作模式与句层规则** — 理由：同上，且与本包文体（判据式短句）不同源；差异：上游 Diátaxis 四模式；保留：现有文体；改变：无；删除：无；落点：包外 docs 规则；回读 R0；决定归属：Driver。
- **defer · HIT-06 去 AI 味** — 理由：规则的对应物（中文版）不在三仓分母内，本轨不据此裁定；差异：上游是英文 unslop 规则；保留：现有文体；改变：无；删除：无；落点：若要做中文写作规则需另找来源；回读 R0；决定归属：Driver。
- **adopt · CONC-01 安全检查面** — 理由：产品有 concern 轴与安全路由，但没有任何可勾选的安全面，这是"轴在、操作不在"的典型缺口，且 AGENTS.md 要求保护 secrets/数据；差异：上游有威胁建模、三档边界、控制项清单、OWASP 快查、供应链门禁；保留：concern 轴与责任路由；改变：新增清单（可挂在 F/E 的评审面）；删除：无；落点建议：`references/security-checklist.md` 式支持文件（不是 Profile 正文）；回读 R0；前置：补读 `addy:skills/security-and-hardening/SKILL.md` + `references/security-checklist.md` + `agents/security-auditor.md`。
- **defer · CONC-02 性能方法** — 理由：产品无性能语境，是否入包取决于包是否要覆盖质量面；差异：上游有测量/目标/定位/验证/防回归；保留：成本关注轴（Backbone §5）；改变：无；删除：无；落点：由 Owner 决定是否扩包；回读 R0；决定归属：Owner。
- **defer · CONC-03 可观测性** — 理由：同类，且与 DBG-11 重叠；差异：上游有信号选择与遥测自检；保留：无；改变：无；删除：无；落点：同上；回读 R0；决定归属：Owner。
- **defer · CONC-04 可访问性** — 理由：无前端语境；差异：上游 WCAG 清单；保留：无；改变：无；删除：无；落点：由 Owner 决定；回读 R0；决定归属：Owner。
- **narrow · CONC-05 测试模式参考** — 理由：与 DBG-15/16 重叠；差异：上游有按层模式与语言示例；保留：无；改变：只保留"打桩边界"一条并入 DBG-16；删除：不收完整模式库；落点：与 DBG-14/15/16 同方法；回读 R0。
- **narrow · CONC-06 运行时夹具** — 理由：产品 F 方法刻意仪器无关，夹具层是可选增益；差异：上游有浏览器/终端取证与既有 harness 优先；保留：仪器无关的 F 方法；改变：仅登记"若无夹具则说明"一条；删除：不引入工具清单；落点：behavior-claim-evaluation.md §Method 2 的注；回读 R0。
- **narrow · SKL-01 技能格式规范** — 理由：当前包不是 skill 包，规范无处附着；差异：上游有 frontmatter/章节/描述禁令；保留：现状；改变：若未来做 skill 包则先读本条；删除：无；落点：包形态决定后；回读 R1（读过 `docs/skill-anatomy.md` 前 120 行）；前置：补读该文件全文 + `skill-lint.js`。
- **adopt · FMT-04 工件路径漂移护栏** — 理由：本包靠人工摘要核对跨文件约定（profile↔method↔charter 的引用），已有漂移风险实例（三处装配示例、M1 字样）；差异：上游用一个 allowlist + 受护文件清单把多宿主路径约定锁死；保留：人工核对；改变：新增窄范围校验（可选）；删除：无；落点建议：`scripts/` 校验器 + CI（若 Owner 允许引入脚本面）；回读 R2（读过该脚本全文，描述与实现一致）；前置：确认包是否允许携带脚本（当前 README 声明无 validator）。
- **defer · FMT-05 三事件 hook 机制** — 理由：包无执行面，hook 属宿主工具层；差异：上游有三事件分工与占位符往返；保留：无；改变：无；删除：无；落点：若引入工具层再处理；回读 R2（读过脚本头与函数清单）；决定归属：Owner/Driver。
- **narrow · FMT-06 缓存须向源站重验证** — 理由：与 EVID-06 同族，价值在"缓存不得降低证据新鲜度"这一条；差异：上游用 validator 而非 TTL；保留：无；改变：作为 EVID-06 的一条注（若引入缓存）；删除：不引入缓存实现；落点：behavior-claim-evaluation.md 或 docs；回读 R1。
- **defer · FMT-07 不要第二个路由器** — 理由：包无路由面；差异：上游禁止重复注入；保留：不增加责任节点（Backbone §2）；改变：无；删除：无；落点：包形态决定后；回读 R2（读过 session-start.sh 的 A 行 + 产品全文）；决定归属：Driver。
- **narrow · FMT-08 机器校验族** — 理由：与 AUTH-20/PKG-03/FMT-04 同族；差异：上游有五类窄范围校验器与豁免清单；保留：人工核对；改变：只登记"哪些不变量应被检查"的清单，不引入校验器；删除：不复制整套脚本；落点：docs 或 scripts（由 Owner 决定）；回读 R1；前置：补读 addy `scripts/validate-*.js` 的 A 行对应原文（若要把清单写准）。
- **narrow · FMT-09 注释卫生** — 理由：E 的局部卫生，产品只给局部自由度；差异：上游有豁免清单与 MUST KILL 标记；保留：局部自由；改变：仅保留"豁免清单"思路并入实现卫生；删除：不引入清理代理；落点：implementation profile 或 CONC-05；回读 R0。
- **adopt · GOV-01 桶分类与晋升不变式** — 理由：本包已有同类漂移（README 保留 M1 时代"待 M4"字样；Profile/Method/Charter 三处状态叙述），与 A3 的计数漂移同病；差异：上游用三条不变式（README 条目 + 清单条目 + docs 页）与再同步触发；保留：现有状态叙述；改变：确立单一权威清单 + 三处一致性 + 变更触发再同步；删除：不删历史快照；落点建议：professional-workflow/README + methods/README（可加检查，见 FMT-04）；回读 R2（读过产品全文 + A3 的 AGENTS.md 行）；前置：补读 `matt:AGENTS.md` 原文以照抄不变式措辞（避免自造）。
- **narrow · GOV-02 派生清单再同步触发** — 理由：与 GOV-01 同源；差异：上游把"任何用户可达变更"设为触发；保留：无；改变：并入 GOV-01；删除：不单独成条；落点：同 GOV-01；回读 R1。
- **defer · PEND-01 79 connector 逐条清单** — 理由：A 只按模板筛到 section 级，本轨只抽样两条，逐条能力/scope/门控未读；差异：不适用；保留：不适用；改变：无；删除：无；落点：不落（未评估）；回读 R2（抽样两条）；前置：逐条读 `third_party/<name>/README.md` 三节；决定归属：Driver（建议拆为独立 work package）。
- **defer · PEND-02 A2 大型机器面并发语义** — 理由：上游 structure 深度，本轨只读 store.ts 一处；若 DES-10/12/13 进入落地，才需要其 spawn/wait 与恢复语义；差异：不适用；保留：不适用；改变：无；删除：无；落点：DES-10 的前置；回读 R2（store.ts 锁与持久化）；前置：读 `agent-manager.ts` spawn/wait 路径；决定归属：Driver。
- **defer · PEND-03 A2 SDK/why 参考** — 理由：本轮非优先面；差异：不适用；保留：不适用；改变：无；删除：无；落点：不落；回读 R0；前置：读 `cursor-sdk/skills/cursor-sdk/references/**` 与 `pstack/skills/why/references/**`；决定归属：Driver。
- **defer · PEND-04 eval runner 断言语义** — 理由：无执行授权且未读实现，A1 亦标注未实测；差异：不适用；保留：不适用；改变：无；删除：无；落点：不落；回读 R2（case JSON）+R0（runner）；前置：读 `scripts/run-evals.js` 断言段；决定归属：Driver。
- **defer · PEND-05 非晋升桶是否入分母** — 理由：上游自身计数漂移（README 24 vs plugin.json 25）且无晋升权威清单；差异：不适用；保留：不适用；改变：无；删除：无；落点：不落；回读 R2（读过 plugin.json 的 A 行 + 三份 README 的 A 行）；前置：读 `matt:AGENTS.md` 晋升规则段 + 重新计数；决定归属：Driver。
- **defer · PEND-06 CHANGELOG 血统** — 理由：A3 明确 structure 读，本轨未读；差异：不适用；保留：不适用；改变：无；删除：无；落点：不落；回读 R0；前置：读 `matt:CHANGELOG.md` 的 `^##` 条目；决定归属：Driver。
- **defer · PEND-07 pricing 与成本主张** — 理由：A2 标 unread；差异：不适用；保留：不适用；改变：无；删除：无；落点：不落；回读 R0；前置：读 `third_party/x/skills/x-api-mcp-guide/references/pricing.md`；决定归属：Driver。

---

## 3 · 缺口线索（无当前方法者）

计划 §3："缺当前方法是缺口线索，不是低分"。以下为本轨判定为 `not-covered` 且**没有任何候选方法/文件承载**的机制（共 70 行中的重点，按建议优先级排列）：

1. **幂等/崩溃安全/保留因果**（DES-10，含 DES-11/12、DBG-10 的失败模式）——计划 §5 点名不得剥离细节的机制，当前零覆盖。
2. **安全面清单与三档边界**（CONC-01，含 PKG-05/06 的凭据与逐动作批准）——轴在、操作不在。
3. **质量约束的可执行契约 + 教训编码进结构**（DES-28 + DES-20）——与本包"大量散文规则"的形态直接相关。
4. **评审五轴与流程、负控制、证据阶梯**（EVID-12/07/08）——F 的工作面目前只有三态判定。
5. **测试质量判据与 mock 纪律、no-loop-no-hypothesis gate**（DBG-15/16/04）——E 与 F 的观察面质量前置。
6. **领域文档形态（CONTEXT）与 ADR**（BHV-10/AUTH-27，已列 adopt）。
7. **机器校验/漂移护栏**（FMT-04/08、GOV-01）——本包自身的状态漂移已有实例。
8. **提交/交付/CI/发布**（DLV-01/03/04/06、EVID-22、CONC-02/03/04）——是否入包取决于 Owner 对包范围的判断。

## 4 · 计数与说明

- 处理行数：183 机制；裁定轨覆盖 **146**（adopt 39 / narrow 64 / defer 39 / reject 4）；`none` 37 不进入本轨。
- **本次未使用 `reframe` 与 `replace`**：`reframe` 需要先认定现有机制的语义被误置（本轨在校准中未发现此类实例，最接近的两条——EVID-04 的三态语义重定义、EVID-13 的多模型独立性协调——已在既有正文中显式说明，故记 `none`/`narrow`）；`replace` 需要"已接受机制被更完整机制替代"的判断依据（如实证失败或责任冲突），本轨无此证据，故不制造该结论。二者不得被读作"已完成评估"。
- **`adopt` 的前置不满足者**：39 条 adopt 中，R0 计 27 条、R1 计 12 条、R2 计 0 条（R2 的情况在本轨记 `narrow` 或 `none`）。因此**采纳前必须先完成计划 §5 的原文+支持文件回读**；每条已给出补读对象。
- **与 A 的关系**：本轨不重写 A 表；校准的六项口径修正（CALIBRATION §4）只影响消费方式。
- 残余风险：本轨的 coverage 判定以产品正文全读为据、以上游 A 屏为参照面；上游未被回读的机制细节可能使个别 `not-covered` 实为 `not-covered-but-different`（即机制形状与本轨描述有差），故每条 `source_paths` 与 `requery` 都给出了回读入口。

## 5 · 边界声明

- 本文件**只是候选**：不实施、不吸收、不改 core/product/legacy、不写任何落地文件、不改 UCBIP。
- 本文件**不代替 Owner 决定点**（计划 §6）：是否启动落地、是否有界落地授权、后续批次是否重复申请，均待 Owner。
- **覆盖 ≠ 采纳**再次声明：CALIBRATION §5 的 confirmed covered 50 条中，本轨未对其中任何一条主张"应保持现状"以外的结论；`not-covered` 与 `adopt` 之间也需要 Owner 的范围判断。
