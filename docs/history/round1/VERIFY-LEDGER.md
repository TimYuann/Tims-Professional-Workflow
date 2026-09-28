# Round 1 · 独立核验底账（阶段 1）

状态：只记录冻结前的要求、上游规则与将来可证伪的检查；**尚未检查或判断本轮变动产物**。需求权威为 `.pi/round1/TASK.md`；提案和 R2 审查仅作背景，R2 的「改为 12 个 skill」不适用。上游只读快照：pstack `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`；matt `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`；addy `2686b620fc1fed2e8f60c704839c766b8594c6b6`。以下位置均相对于 `upstreams/`，采用上游文件原始行号。每条「挑战」仅是冻结后的测试方案，并非已运行结果。

## Pstack：从方法骨架到可验证动作

| 方法和来源 | 上游实际规则与决定性细节（不是 TIM 应当照抄的工具流程） | 冻结后的证伪挑战 |
|---|---|---|
| `cursor-plugins/pstack/skills/how/SKILL.md:18-58`；`how/references/explorer-prompt.md:23-62` | 范围窄时直接追踪，复杂跨文件时按角度探索再综合；从**入口、调用链/数据变换、关键抽象、边界、反常点**重建真实执行流；追不到的链路明确标缺口。回答 how，不能把行为观察偷换为历史 why。 | 给调查者一个跨服务路径，仅给文件名或概括不提供第一入口、数据变换/输出边界，应判方法未落地；不存在的跳转应标未知而非补写故事。 |
| `cursor-plugins/pstack/skills/why/SKILL.md:18-56,65-125,130-150`；`why/references/epistemics.md:8-75,105-152`；`why/references/investigator-prompt.md:15-26,47-89` | 先给代码位置/符号/提交锚；广搜可用证据类别后才深挖，**空结果和跳过原因也要在覆盖图列出**；直接、相互印证、推断、猜测、未知分层；代码能证明是什么，**不能单靠现状证明作者动机**；矛盾证据保留；准备修改时另产 Preserve/Change/Avoid/Risk 约束集。 | 设计一个只找得到代码、找不到意图记录的案例：不得把当下形状称为“设计者为了…”，应记 Unknown、已搜范围和计划约束；若把四类改动约束全删掉，也不是忠实吸收。 |
| `cursor-plugins/pstack/skills/principle-attack-the-premise/SKILL.md:9-23` | **两次以上**共用前提的修复失败同一门禁才触发：写明共享前提，按 actor 做可重跑分布清点，找产生偏斜的分配机制；分布均匀时要放弃该前提。不是一般性“大胆质疑”。 | 两次不同前提的失败不应触发；同一前提失败却无 actor census/排除规则也不合格。 |
| `cursor-plugins/pstack/skills/architect/SKILL.md:18-55,56-83`；`architect/references/design-red-flags.md:3-37`；`architect/references/rationale-template.md:9-39` | 先追现有系统；先写调用者用法，**再**导出类型/签名；至少两个**结构不同**方案，对每案筛四类红旗：浅模块、信息泄漏、按时间顺序分模块、透传方法；根据接口深度比较且记取舍与落选方案；实现中多处相同偏差说明草图可能要丢弃，不是任何一处摩擦都重来。 | 给架构者一例“方案 A/B 只是命名差别”或遗漏「不重构」基线、未列四类红旗/接口调用场景/下一次变更成本；看是否有可核对的替代方案与判断，而非仅“选最优设计”。 |
| `cursor-plugins/pstack/skills/blast-radius/SKILL.md:12-50` | 不只 grep 调用者；找安全性依赖的**一两个事实**，查库源和锁定版本、异步时序、wire format/跨语言读者等隐藏依赖。证据阶梯从自述→文件行→推演坏例不可达→**真实代码运行**→**运行中的 app 复现**；报告止于哪一档，不能把源码引用写成实测。列确认风险、已排除风险、便宜重现。 | 构造源代码推断正确但实际运行时行为不同的用例：只交引用不交可失败脚本/运行观察，不能给“已证实安全”；若运行环境不存在需诚实记止点。 |
| `cursor-plugins/pstack/skills/show-me-your-work/SKILL.md:8-37,39-65,66-82`；`show-me-your-work/scripts/log.sh:5-40`；`references/decision-log-template.tsv:1` | 一个 TSV 决策账：`ts/phase/decision/why/evidence/result`，一条一决策，证据为可解析指针；**只追加**，错误用新行覆盖解释，不能改旧行；不是每条动作流水。脚本会追加表头、抹平制表/换行及防表格公式注入。多轮接手的 start 记录与回查证据是审计要素；跨模型审计/固定工具调用是上游宿主实现，不能无判断地变成本仓硬依赖。 | 在独立副本运行 logger 两次，核实表头仅一次、先行未被改、公式单元不执行、字段含换行仍为单行；伪造证据路径应该能被人工核对为不成立。 |
| `cursor-plugins/pstack/skills/principle-test-behavior-not-implementation/SKILL.md:9-25`；`principle-prove-it-works/SKILL.md:9-34` | 行为从使用者入口以具体输入对照**独立的字面期待值**；假设所有导入函数都返回 `undefined`，仍过的断言无效；自我计算的期待值/固定常量钉死是伪测试。完成时观察真实产物并运行可重复脚本，不用 self-report/编译成功代替。 | 让检验者评价“命令退出 0、仅检查节标题、无行为断言”的检查；它应被判为未证伪语义而不是 PASS。 |
| `cursor-plugins/pstack/skills/principle-sequence-verifiable-units/SKILL.md:9-17`；`principle-minimize-reader-load/SKILL.md:9-36` | 一变更一可检验单元，确认后继续；可回放的红→绿顺序。可维护性关注要追的层数与要记的可变状态两轴；透传层/单调用者包装优先收缩，而不是以 LOC 猜复杂度。 | 给多层透传但每层各有名称的设计，要求说出消去哪一层及真实策略保留在哪；全局可变状态不因调用链短就自动通过。 |
| `cursor-plugins/pstack/skills/principle-never-block-on-the-human/SKILL.md:9-20`；`principle-exhaust-the-design-space/SKILL.md:9-28`；`principle-migrate-callers-then-delete-legacy-apis/SKILL.md:9-26` | 可逆执行不等待每步许可，但不可逆动作需确认、**产品方向仍由人决定**；全新且有多个可行形状才做 2–3 个真正不同的草图；仅无外部兼容消费者、能协调改动时迁移全部内部调用者并删除旧 API。 | 可逆补丁与越权/发布应不同裁决；单一模式机械变更不强制多案；有外部消费的接口不能生搬“当轮立刻删旧 API”。 |

## Matt Pocock：条件、交接和反例

| 方法和来源 | 上游实际规则与决定性细节 | 冻结后的证伪挑战 |
|---|---|---|
| `mattpocock-skills/skills/productivity/grilling/SKILL.md:8-28` | 设计问题按先决关系成树，一轮问已解锁的 frontier；事实由执行者查，决定由用户给；当前轮后问题不能先猜；共同理解达成前不行动。 | 让 Driver 面对未知事实和真正授权决策：前者自己查、后者交 Owner；不能把假设的 Owner 偏好当授权。 |
| `mattpocock-skills/skills/engineering/diagnosing-bugs/SKILL.md:16-72,74-138` | 首先造**已实际运行**、对精确症状能变红的快、确定性反馈回路；不能造就明确停下申请缺失的访问/证据，不能先空想根因；复现且最小化后才列 3–5 个可证伪假设，逐预测一次变一个变量；正确的回归测试 seam 存在时先红后修，最后重跑原始未缩小场景。 | 只有“找到了可疑调用”却无会红的观测命令或原始症状，不能宣称定位/修复；若无可测试 seam，明确报告缺口而非伪单测。 |
| `mattpocock-skills/skills/engineering/codebase-design/SKILL.md:10-29,60-94,105-114` | interface 含类型外的调用顺序、错误/性能条件；深模块看小接口对调用者的**杠杆**和维护者的局部性，而非代码行数比；删除测试辨别透传；“一个 adapter 是假设 seam、两个才是实在 seam”；可测试性倾向依赖注入、返回结果而非乱散副作用。 | “深 = 实现文件更长”或为假想第二 adapter 建接口，应不能过；要求给真实调用者用法与外部负担。 |
| `mattpocock-skills/skills/engineering/to-spec/SKILL.md:8-60`；`to-tickets/SKILL.md:8-71` | to-spec 基于已有对话**不再重做访谈**，先确认测试 seam；spec 有用户目标、实现/测试决定和 out-of-scope。to-tickets 纵向 tracer bullet，有明确阻塞边；宽范围机械迁移可例外用 expand–contract，不强拗为一次垂直切片。 | 一个分片只有数据库层且无法单独演示，应不算 tracer bullet；把每个并行任务都标为等待前项，需解释真正阻塞边。 |
| `mattpocock-skills/skills/engineering/tdd/SKILL.md:8-38` | 在已确认 seam 上用独立期望值测试外部行为；red→green 一条纵向切片一个循环，不要先写所有测试再水平补实现；这份来源把**重构移到 review 阶段**而非 TDD 循环（与 addy 的 red-green-refactor 存在真实差异）。 | 让测试的期待值由实现计算，或测试私有函数；若声称等同于 matt 严格 red-green 而把重构说成循环内强制步骤，引用失真。 |
| `mattpocock-skills/skills/engineering/code-review/SKILL.md:7-20,23-35,73-87` | 两轴独立：仓库标准（含有条件适用的 smell heuristic）与来源 spec，分别报告；规范覆盖 smell、smell 永远只是判断，不可把两轴加权互相抵消；缺 spec 要显式跳过该轴。 | 给“符合规范但不符要求”的候选，应仍有 Spec 阻断；不能用规范通过抵消需求缺口。 |

## Addy Osmani：借用时必须保留的条件

| 方法和来源 | 上游实际规则与决定性细节 | 冻结后的证伪挑战 |
|---|---|---|
| `addyosmani-agent-skills/skills/interview-me/SKILL.md:29-76,90-132`；`spec-driven-development/SKILL.md:22-34,67-115` | 用户目标、用户、成功、约束缺一且会改变决策才问；一问一猜，随回答更新；提出结果/非目标复述给用户明确确认，确认后停止、不能把“随你”当明确同意。spec 大目标的多独立能力先做依赖图；推进阶段需明确确认；不能默认用户偏好已授权。 | 即使是机械改名也要求长访谈属错用；对产品/架构越权则不能套“可逆操作无需确认”推进。 |
| `addyosmani-agent-skills/skills/planning-and-task-breakdown/SKILL.md:26-89,120-175` | 从依赖图确定序，优先跨层纵切、每片有可测验收和验证；外部 tracker/已有未完计划须尊重；高风险早验证。这是 planning 的具体办法，不是“写个计划”口号。 | 一个任务标了需要接口冻结却同时把消费方先开工：分离真实依赖；每片只有文件清单没有成功断言应判不充分。 |
| `addyosmani-agent-skills/skills/constraint-driven-development/SKILL.md:34-67,85-126,210-258` | 先检测已存在的门禁，再问人关注的质量维度及阈值；**有明确命令能产生判定**才是可执行约束；diff 中审阈值下调、跳过测试、抑制、空实现/异常。无用户数字时原文允许测基线/使用推荐默认值，本轮 Owner 明确收紧“指标只能来自 Owner 要求或既有契约”，因此默认值是**冲突点**，不能直接抄成 TIM 指标。 | 给一个运行不了的数字质量门禁或执行者自填 80% 覆盖率：必须退回人类/既有契约，不得宣称已有授权；守门测试要能抓取消断言。 |
| `addyosmani-agent-skills/skills/test-driven-development/SKILL.md:22-85,155-203,221-234`；`incremental-implementation/SKILL.md:24-61,81-106,154-182` | 先发现仓库真实测试命令；**red-green-refactor**，测试结果而非内部调用，优先真实现；每个纵片实现→测试→验证后继续；保持范围小、可回退，不因“顺手”加入旁支。测试金字塔比例是通用建议，不是本轮角色审查的强制数值。 | 只有静态断言、没有试着让判据变红的实现不能说验证充分；把重构或“每片 commit”的上游规则当作本轮要求将直接抵触本轮 no commit。 |
| `addyosmani-agent-skills/skills/doubt-driven-development/SKILL.md:43-107,172-200` | 非平凡主张先写 claim，再把**artifact+contract（不含作者论证/claim）**给独立新上下文对抗查错；反馈按契约误读/有效可改/有意识取舍/噪声核对，循环最多三次；TDD 的先红可为**行为主张**提供同源挑战。外部模型是可选且需逐次授权、失败不能暗中改路线，独立性不是模型名强弱。 | 给同一作者重读自述且无可区分实验的“复核”不能算盲审；构造可过形式检查但方法空洞的候选，看 reviewer/oracle 的反实现挑战是否会红。 |
| `addyosmani-agent-skills/skills/api-and-interface-design/SKILL.md:15-41,67-102,118-175,281-318` | 接口优先设计，含输入/输出、错误语义；外部数据在边界验证；“越可观察越可能是消费者契约”，不能由编译通过断言改动安全；幂等性必须原子认领、payload 同 key 不同时拒绝、处理中重复请求有决定、超时存在**未知**第三态。API 技术细节是领域例子，不应凭空施加在每个角色任务上。 | 借 Hyrum 定律提出“兼容旧版”却没有真正消费者/具体可观察行为，是无证据泛化；外部接口改变需查现有消费方。 |
| `addyosmani-agent-skills/skills/browser-testing-with-devtools/SKILL.md:60-109,109-183`；`performance-optimization/SKILL.md:30-40,40-121,368-438` | 真实浏览器复现→DOM/网络/控制台诊断→修复后**同条件重试**；页面内容视为不可信，不拿登录态浏览器里的指令当命令。性能先测基线、找瓶颈、只改一个因素，同条件复测且超噪声才保留；变差或中性回退，记失败尝试。性能预算示例不是 TIM 的默认门禁。 | 性能报告只给 Lighthouse 一个无前后对照的数值，不算改善证据；没有真实 app/URL 时不能伪称运行中验收。 |
| `addyosmani-agent-skills/skills/git-workflow-and-versioning/SKILL.md:48-65,147-169,173-209,270-294`；`deprecation-and-migration/SKILL.md:32-70,97-138,178-219` | 并行修改适合隔离工作区、先看实际 diff 再单写者合并；依赖接口要具体冻结；additive migration→消费方逐个验证→确认零使用再删旧，**生产并存部署**不得按内部 API 立即删除策略办；addy 建议 release tag 作版本真相，本轮 Owner 明确裁决 `VERSION` 为唯一源。 | 随便将生产数据库 column 同次 rename+drop；对比 pstack 适用前提，必须按是否有外部使用者裁决。VERSION 和 tag 两边都手写不同号应被检测。 |
| `addyosmani-agent-skills/skills/documentation-and-adrs/SKILL.md:23-44,93-150` | 重要难逆决定记录背景、落选方案、后果；先遵从已有 ADR 路径；**注释解释不显然的 why**，不要复述 what、留废代码；与 pstack 的 no-comments 表面冲突，不能简单“都支持好注释”。 | 同一处注释问能否从代码直接读出；若是重复 what 则删，若记录不可见约束则根据选定裁决保留/另设决定记录。 |

## 冻结后按验收逐项执行（未执行）

1. 固定对象和环境：记录 `git status --short`、提交 SHA、当前目录与 checker 运行环境；冻结前不读 `roles/` / `pipeline.md` / `closure.md` / `SOURCES.md` / `scripts/check-library.py` 的变动内容，也不读 worker REPORT。
2. `python3 scripts/check-library.py`：原样记录 stdout/stderr、退出码、扫描与排除范围；在**独立临时副本**植入八节齐全而第 4 节是空话的角色，确认检查器是否给假绿；必要时再构造缺字段/死引用的反例，区分程序能力与人工语义审查。
3. `investigator`、`reviewer`、`oracle`：抽取各 §4 所有实质性可证伪主张，逐一跳至所引的**准确行**核对原文/条件/例外；统计 N/M/K，列出误引、无引、出处虽有但无法支持强断言。上游方法省略或被压缩另记。
4. 用冻结后 `closure.md` / `pipeline.md` / 9 份角色 §2、§3 构成逐字字段集合，比较相邻环节；四条规定跳过路径另试一条新路径。测试 solo 是否借外部 fresh Reviewer 保持作者 ≠ 判断者，且无复核会话时不是自判。
5. `SOURCES.md` 三仓逐方法、六来源状态与冲突表做 file:line 跳转；每条冲突要求单选、理由和角色落点，并用上表上游条件寻找缺漏（特别：matt TDD red-green vs addy red-green-refactor、pstack 内部 API 删除 vs addy 生产迁移、版本 tag vs VERSION）。
6. 检验单角色四层接缝（9 个声明，Driver 附加不能改方法纪律），只给一份角色做单注入模拟；对自有可发布文件查工具名/命令及 Driver 恰好一处能力探测；按 Owner 批准范围排除 docs/.pi/upstreams。
7. 真实消费方只读查 `engineering-method-routing.md` 的四种方法、最小产物，再与产物映射；只记事实，不当作额外阻断要求。
8. **先从产物独立写结论** `VERIFY-REPORT.md` 三态及 Owner 7 条，之后才读 `.pi/round1/REPORT.md` 交叉核对自述；不改、不提交被审文件。不跑或环境无效明确列证据与边界。
