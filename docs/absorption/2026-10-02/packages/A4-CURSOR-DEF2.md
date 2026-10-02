# A4-CURSOR-DEF2 · cursor-plugins 审核包 2（D/E/F 残余：交付技能、扇出聚合、自评与重建、TS 实践、why 源、评审镜头、SDK 集成、benny 运行文件）

- 实例/角色：`tpw-absorb-a4`（A 类发现者；只产出审核包，不裁定采纳）。
- 源仓与 pin：`cursor-plugins` @ `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`（863 paths）。
- 只读 locator：`.worktrees/legacy-pre-night-2026-10-01/upstreams/cursor-plugins`；本 session 全部 `git show <pin>:<path>`，未 checkout、未执行、未写源。
- 前置包：`docs/absorption/2026-10-02/packages/A4-CURSOR-DEF.md`（G-01..G-14）；a2r 包 `A2R-CURSOR-ABC1..8`。
- 本包边界：不产生采纳裁定；不改产品/他人文档；不 commit；未执行的观察一律标注。
- 定位：DEF1 的 §0/T-04/T-05/T-07/T-08/T-09 残余中，按 D/E/F 价值挑出的第二波读源。A/B/C 主干仍归 a2r；与 a2r 重叠处只做**核对/补实现细节**，不复述。

---

## 0 · 读深声明

**pin 内逐字全读（本包新增）**：

- `cursor-team-kit/skills/{fix-ci,loop-on-ci,fix-merge-conflicts,run-smoke-tests,make-pr-easy-to-review,new-branch-and-pr}/SKILL.md`（6 份全文）。
- `pstack/skills/arena/SKILL.md`、`pstack/skills/swarm/SKILL.md`、`pstack/skills/tdd/SKILL.md`、`pstack/skills/reflect/SKILL.md`、`pstack/skills/recall/SKILL.md`、`pstack/skills/typescript-best-practices/SKILL.md`（全文）。
- `pstack/skills/why/SKILL.md`（全文）+ `why/references/sources/{code-archaeology,sentry,linear}.md`（全文）。
- `pstack/skills/interrogate/references/code-quality-review.md`（全文；a2r ABC3 明确列为残余）。
- `cursor-sdk/skills/cursor-sdk/references/{auth,streaming,mcp}.md`（全文）。
- `pstack/automations/benny/skills/{triage-issue-reports,reproduce-and-fix-issues}/SKILL.md`（全文）。

**未读（本包不评估）**：`pstack/skills/typescript-best-practices/references/patterns.md`；`why/references/{investigator-prompt,synthesizer-prompt,sources/{notion,slack,databricks}}`；`cursor-sdk/references/{patterns,advanced}.md`；benny `setup-benny/SKILL.md`、`templates/*automation-prompt.md`、`routing.example.md`、`feature-map.example.md`；`pstack/skills/{how,architect,figure-it-out,automate-me,setup-pstack,make-bot-ui,unslop}/`；`cursor-team-kit` 其余 skills；orchestrate schemas/cli/tests 正文（DEF1 T-06）；third_party 全量（DEF1 T-03）。a2r 已读项（interrogate rubric/lead-judgment/reviewer-prompt、why synthesizer-prompt、worker/verifier prompts、feature-map README+create-note）本包不重复。

---

## 1 · 与 DEF1 / a2r 的分界

| 本包组 | 与既有包的关系 |
| --- | --- |
| H-01 交付/CI/合并技能 | DEF1 G-05 是判定状态机（watcher）；H-01 是操作循环（人/agent 手册）；a2r ABC3 MG-3 已覆盖 `fix-merge-conflicts` 与绿色闭环，本包只做**逐字核对与差异补充** |
| H-02 arena/swarm | a2r ABC2/ABC4 提出"执行单元与证明纪律"；H-02 补**扇出形态与聚合规则的完整操作**（ORC-02/03/13 未覆盖面） |
| H-03 tdd | a2r ABC2 MG-1/ABC3 已涉及 TDD 的适用边界；H-03 做逐字核对（DBG-14/15/18 补缺） |
| H-04 reflect/recall | a2r ABC3 MG-5 提及 recall 邻接；H-04 补 transcript 范围纪律与自评路由（ORC-08/09 未覆盖） |
| H-05 TS 实践 | DEF1 G-12 通用类型纪律；H-05 是该纪律的 TS 具体映射（语言层，非新机制） |
| H-06 why | DEF1 G-09 已读 epistemics + incident-postmortem + datadog + blast-radius；H-06 补 why/SKILL 与 code-archaeology/sentry/linear 三份源 playbook |
| H-07 质量镜头 | a2r ABC3 残余 `code-quality-review.md`；H-07 补齐并与 thermo-nuclear 判重 |
| H-08 SDK 集成 | DEF1 G-12 只读了 SKILL + 2 份 reference 部分；H-08 补 auth/streaming/mcp 全文 |
| H-09 benny 运行文件 | DEF1 G-08 只读 adapter/verify-existing-fix/config/FOR_AGENTS；H-09 补两个 SKILL 的硬安全规则 |

---

## H-01 · 交付与 CI/合并操作循环（cursor-team-kit 六技能）

### 1) 机制与触发情境；源锚点与已读/尚缺

触发情境：PR 已开，需要把 CI 弄绿、解冲突、跑冒烟、提升可评审性、开新分支与 PR。这些是"最后一公里"的 E/F 操作，不是 F 的判定语义。

源锚点（pin 内，全读）：

- `cursor-team-kit/skills/fix-ci/SKILL.md`：`gh pr checks --json name,bucket,state,workflow,link` 为 PR 状态真源；从失败 job 取**第一个可执行错误**（GHA log 或 check link）；最小安全修复；推送后重查整组；"一次修一个可执行失败"；"不要为了推进绕过 hooks"。
- `cursor-team-kit/skills/loop-on-ci/SKILL.md`：先看再等；已失败先诊断；pending 用 `--watch --fail-fast`；每次 push 后重查（检查集可能变）；flake 只重试一次并记录证据；**与 PR 无关且 main 已修好 → 合 main 而不是把无关修复塞进 PR**；不得 `--no-verify`。
- `cursor-team-kit/skills/fix-merge-conflicts/SKILL.md`：逐冲突最小正确修；安全时保留双方，否则选"能编译且公共行为不变"的；**lockfile 用包管理器重新生成，不手编**；修完跑 compile/lint/相关测试；**解冲突期间不重构、不 push/tag**；不留冲突标记。
- `cursor-team-kit/skills/run-smoke-tests/SKILL.md`：先构建前置；跑全套或聚焦单文件；失败看 trace/log 定位根因；最小修复重跑至稳；确定性等待而非脆弱 timeout；passing 修复要复跑以排除 flake；**只有明确要求且有记录才 quarantine**。
- `cursor-team-kit/skills/make-pr-easy-to-review/SKILL.md`：默认目标是**行为不变的可评审性**；识别噪声 commit/陈旧描述/无关改动/机械与逻辑混改/缺测试/入口不清；**重写历史前必须提计划**（用户要求或同意）；`ORIGINAL_TREE=$(git rev-parse origin/<head>^{tree})` 记录侧，重写后比对 tree 是否一致，不一致不推；可评审分组通常按依赖序（schema/生成定义 → 核心逻辑 → 接线 → 界面 → 测试）；**不得把行为变化藏在 cleanup 里**；太大就建议拆分而不是粉饰。
- `cursor-team-kit/skills/new-branch-and-pr/SKILL.md`：干净树（或显式处理）→ 从最新 main 开描述性分支 → 实现与测试 → 聚焦提交推送 → PR 带 summary/test notes。

a2r 已覆盖/本包差异：a2r ABC3 MG-3 已转述 `fix-merge-conflicts` 与 `fix-ci`/`loop-on-ci` 的主线；本包补三条它未逐字记录的判据：① **ORIGINAL_TREE 比对**（历史重写的内容恒等验证）；② **"无关失败合 main 而不是塞无关修复"**；③ **smoke 的 flake 复跑与 quarantine 门槛**。

### 2) 操作、成立条件、失败模式、反例

- CI 回路：检查集是状态真源（不是 `gh run list`）；一次一个可执行失败；最小修复；push 后重查整组；flake 最多一次并留证据；无关失败改基线（合 main）而不是改 PR；**永不绕过 hooks**。
- 冲突解析：逐 hunk、保双方、保公共行为、lockfile 重生成、期间不动大结构、不推送；完成后 typecheck/test 顺序执行。
- 可评审性：先计划后重写；tree 恒等验证；机械/逻辑分离；行外说明优先于历史重写；不隐藏行为变化；过大建议拆分。
- 新分支：单变更集；有验证记录才请求评审。

失败模式/反例：把 CI 绿当 verdict（DEF1 G-05/G-11 已给判定结构）；一次多个失败一起改导致无法归因；为过检查 `--no-verify`；flake 反复重试；解冲突时顺带重构或推远端；手改 lockfile；重写历史后忘记比对 tree 导致丢改动；把行为变化写进"cleanup"；PR 过大靠描述粉饰。

### 3) A–F 判断位点与专业 concern

| 位点 | concern | 何时调用 | Profile |
| --- | --- | --- | --- |
| E：CI/冲突/冒烟的局部实现 | 实现/可靠性 | PR 到 merge-ready 期间 | `implementation` |
| F：检查集真源、flake 判据、tree 恒等 | 验证/证据 | 判断"到底绿没绿/是否丢码" | `evidence-evaluation` |
| D：解冲突的兼容取舍、重写计划 | 架构/版本 | 冲突涉及接口/行为时 | `technical-planning` |
| Driver：合并前顺序与授权 | 程序性 | 从绿到合 | `driver` |

### 4) 当前产品锚点、覆盖与缺口

- 已覆盖：`profiles/implementation.md` 的"局部缺陷由 E 修正"；`methods/local-defect-feedback-loop.md` 的"重跑原始场景"；`methods/behavior-claim-evaluation.md` 的三态。
- 缺口：**CI 回路的具体纪律**（一次一个可执行失败、检查集真源、flake 一次、无关失败合基线、不绕过 hook）；**解冲突的行为保持与 lockfile 重生成**；**历史重写的 tree 恒等验证**；**可评审性与行为变化分离**。这些是 E/F 的日常操作，产品完全空白。

为何值得吸收：产品有"证据"哲学，但"每天要用的操作纪律"缺失；这些条目都能以一段"操作规则 + 反例"吸收，且不引入新节点。

### 5) 拟处置与载体

- 拟保留：检查集真源；一次一个可执行失败；flake 一次 + 证据；无关失败改基线；不 `--no-verify`；冲突逐 hunk + lockfile 重生成 + 期间不重构/不推；历史重写的 ORIGINAL_TREE 恒等验证；隐藏行为变化禁令；过大拆分。
- 拟改变：`gh`/GHA/tree hash 命令作为例子；"`--fail-fast`"等参数标实现细节。
- 拟删除：GitHub 专属字段名与 PR 机制；保留 `origin/<branch>^{tree}` 的**对象标识**思想（任何版本控制系统里用"内容标识"验证重写）。
- 载体落点：on-demand guide `pr-delivery-loop.md`（CI/冲突/冒烟/可评审性四节），或并入 DEF1 G-11 的落地方法来承载操作细节；`methods/README.md` 按需表一行。
- 仍依赖 runtime：真实 forge/CI、包管理器、运行中的测试环境；无 forge 时退化为"本地检查+人工"。

### 6) 可讨论正文草稿/操作例子 + 验证方案

```markdown
## CI 回路（操作）
- 以"附着在该变更集上的完整检查集"为状态真源；不要用某个命令的局部输出代替。
- 每次只修一个可执行的失败；修完推送，重查整组（检查集本身会变）。
- flake 最多重试一次并记录证据；重复的同一失败按非 flake 处理。
- 失败与变更无关且基线已修：更新到基线，而不是把无关修复塞进本次变更。
- 不绕过 hooks；检查失败不得用"稍后补"叙事略过。

## 冲突解析（操作）
- 逐冲突最小正确修；能保双方就保双方；否则选"能编译且外部行为不变"的一侧。
- 锁文件/生成物用工具重新生成，不手写。
- 解析期间不做大重构、不推送；解析完按编译→测试→格式化的顺序验证。

## 历史重写的前置（操作）
- 先提出计划并取得同意；记录重写前的内容标识（tree/哈希）；重写后比对内容标识与目标分支 diff；不一致不得推送。
- 不得把行为变化藏进"清理"；过大到无法通过说明变得可评审时，建议拆分。
```

验证方案（**未执行**）：本地 mock 一个"两个失败检查 + 一个 flake + 一个无关失败"的 PR 流：期望逐个处理、flake 只重试一次、无关失败通过更新基线解决；再造一个重写历史的场景，故意改坏 tree 检查能否拦下；造一个 lockfile 冲突验证"重新生成 vs 手编"的差异。边界：不要求真实 CI；无 forge 时只做本地检查与恒等验证。

---

## H-02 · 并行候选与扇出聚合（arena / swarm）

### 1) 机制与触发情境；源锚点与已读/尚缺

触发情境：一个非平凡产物只做一次会锁死第一形态（设计/命名/算法/难以逆转的决定）；或需要并行覆盖切片、竞速、混合形态并汇总一份报告。

源锚点（pin 内，全读）：

- `pstack/skills/arena/SKILL.md`：六阶段 Frame/Fan out/Cross-judge/Pick/Graft/Verify；**prompt 即契约**；先写 3–6 条可评分 rubric（只给 picker，不给候选）；候选同一 prompt、各自独立输出位置（worktree 或临时目录，引 `separate-before-serializing-shared-state`）；一次消息内全部启动、每个候选同时交 rationale（含被弃方案）；judge 与候选**不同模型家族**、只读、按 rubric 逐条打分并推荐 base，与父阅读并行而非与候选并行；父**逐候选通读**；逐条对分而非整体感觉；选"未来维护者最容易扩展且不破坏不变量"的 base（tie 时更干净的边界/更小的 API）；graft 每个 loser 通常只有 1–2 个值得移植项，手工折叠而不是粘贴；N 个收敛 → 强一致信号，直接采用共识形态；N 个发散 → Phase A 欠规格，重框而非平均；合成物按普通产出验证。
- `pstack/skills/swarm/SKILL.md`：四阶段 Frame/Fan out/Aggregate/Report；先定 done predicate 与必返工件；形态（切片/同题竞速/混合）与选择规则（first pass/rank all/best-of）**先声明**；N 是总 worker 数而非并发上限；每个 worker 独立可写输出，测量/验证 brief 必须写**精确 SHA 与方法**（采样数、一个样本是什么、顺序）；报告固定 `PASS/ISSUES/BLOCKED` + 证据；报告缺 SHA/方法 → 丢结果并重跑一次，二次仍缺记 gap（**gap 不算 pass**）；覆盖需要每个必需切片有结果；竞速按先声明的规则选择；不得贴原始 dump。

已读：两份全文；尚缺：`pstack/skills/architect/SKILL.md`、`pstack/skills/figure-it-out/SKILL.md`（与之衔接的上层路由）。

### 2) 操作、成立条件、失败模式、反例

- **扇出前定契约**：done predicate、必返工件、证据格式、选择规则、模型与成本；"先启动后想"是最大反例。
- **隔离写面**：候选/worker 各自写自己的位置（worktree 优先）；测量/验证必须记录 SHA 与方法，否则结果不可比、不可复现。
- **聚合纪律**：缺证据重跑一次，二次记 gap 且 gap≠pass；覆盖形态下每切片必须有结果；竞速按预声明规则；父保留紧凑表而非 dump。
- **arena 的取舍**：judge 只是输入，父必须逐条打分并读两个 rationale；分歧表示偏差或 rubric 歧义，不能"投票";graft 手工、保持单一心智模型；收敛不 graft。
- **与 DEF1 G-11 的关系**：G-11 的"十车道+回归车道+perf 双边"是 arena/swarm 在合并门处的具体化；本组给通用扇出规则。

失败模式/反例：不先写 rubric 就 spawn；judge 与候选同家族；父不读全部候选只看 judge；把发散平均成"折中设计"；worker 报告缺 SHA/方法仍当结果；把 gap 当 pass；覆盖形态漏切片仍宣称完成；竞速未预声明选择规则；把原始 worker 输出粘进最终报告。

### 3) A–F 判断位点与专业 concern

| 位点 | concern | 何时调用 | Profile |
| --- | --- | --- | --- |
| D：多方案比较与 base/graft | 架构/取舍 | 难以逆转的设计 | `technical-planning` |
| F：rubric、逐条评分、gap≠pass | 验证/证据 | 选择与聚合 | `evidence-evaluation` |
| Driver：扇出编排、预算、选择规则 | 程序性 | 并行工作 | `driver` |

### 4) 当前产品锚点、覆盖与缺口

- 已覆盖：`cross-module-design.md` 的接口/seam 与"不要求固定数量设计备选"；`profiles/driver.md` 的并行写集问题。
- 缺口：**多候选/多 worker 的扇出契约与聚合规则**——rubric 先写、独立写面、证据含 SHA/方法、gap≠pass、竞速预声明、收敛/发散的处理。产品明确"不要求固定数量备选"（对），但缺少"一旦做多候选/并行覆盖，怎么保证可比与可聚合"。

为何值得吸收：这是 ORC-02/03/13 的未覆盖面，且与产品已接受的"独立性是真实属性"直接衔接；吸收后不引入固定 gate。

### 5) 拟处置与载体

- 拟保留：扇出前契约（predicate/工件/证据/选择规则）；隔离写面；测量 brief 必含 SHA+方法；缺证据重跑一次、二次 gap、gap≠pass；逐条评分而非整体；judge 独立家族；收敛/发散判据。
- 拟改变：模型目录/`run_in_background`/cloud environment → "宿主提供的并行能力"；N/默认模型名删除。
- 拟删除：`pstack-models.mdc` 依赖、具体 slug。
- 载体落点：on-demand `parallel-fanout.md`；`profiles/driver.md` 关键问题补一行"选择规则是否事先声明"；`technical-planning.md` 按需入口一行。
- 仍依赖 runtime：真实并行宿主与隔离环境；无并行能力时本方法退化为"多方案串行比较"（arena 的 Frame/Pick/Graft 仍适用）。

### 6) 可讨论正文草稿/操作例子 + 验证方案

```markdown
## 扇出前必须写下的（操作）
- 完成谓词与必返工件；证据格式（含对象与版本标识）；worker 形态与总数；选择规则（先到/全排名/最优）。
- 每个写者独立输出位置；测量类任务写明采样数与顺序；否则结果不进入聚合。
- 聚合：缺证据先重跑一次，二次记 gap；gap 不等于通过；覆盖形态每切片必须有结果，竞速按预声明规则。

## 多候选设计（操作）
- 先把"成功长什么样"写成 3–6 条可评分标准；候选只看任务；评审者看标准不看整体感觉。
- 候选各自交 rationale（含被弃方案）；父逐候选读完再决定；评审意见与自己的逐条打分不一致时先复查偏差/标准歧义。
- 选"未来最容易扩展且不破坏约定"的 base；从落选者手工折入 1–2 个优点并保持单一心智模型；验证合成物。
```

验证方案（**未执行**）：同一小设计任务跑 3 候选 + 1 独立评审，按 rubric 逐条打分；再故意缺一个候选的 SHA/方法，检查是否被丢弃并记 gap；再让所有候选收敛，检查不 graft 直接采用。边界：单候选直做不需要本方法；无多模型环境时用同一模型的多次尝试并明确标注独立性限制。

---

## H-03 · 测试优先的缺陷修复（tdd）

### 1) 机制与触发情境；源锚点与已读/尚缺

触发情境：缺陷有**便宜、局部、明确**的测试目标；用户明确要求 TDD 或回归测试。反情境：测试路径不清、昂贵、集成重、只有生产态能复现。

源锚点（pin 内，全读）：`pstack/skills/tdd/SKILL.md`：描述即**双向门槛**（只在明确要求或便宜路径时用；否则跳过并要求用最近可用的验证）；六步（理解 → 选最窄可执行检查 → 先写失败测试 → 修前确认因预期原因失败 → 最小生产改动 → 复跑）；"测试编码意图而非镜像实现"； impractical 时用定向脚本/手工复现/浏览器自动化/快照/日志断言/聚焦集成检查；**"宁可不加测试也不要坏测试"**（坏 = 测 mock 为主、编码实现细节、依赖时序/全局态、昂贵基础设施、事后即删）；护栏（不迁就错误实现改测试、不削弱既有断言除非行为真变了、聚焦本缺陷、flake 先确定化并记录锁定的信号、暴露更广类别时先落聚焦回归再扩）。最终回复要求"证据而非结果"：nominal 失败测试与失败输出、修后通过运行、无法给出 failing-before 时的原因与替代。

a2r 覆盖情况：ABC2 MG-1（执行单元与证明纪律，F）与 ABC3 邻接提到过 TDD 适用边界；本包逐字核对并补：**坏测试清单**、**"宁可不加"**、**flake 确定化+锁信号**、**最终回复的证据格式**。

### 2) 操作、成立条件、失败模式、反例

- 成立：路径局部、测试成本低、能确认"因预期原因失败"。失败模式：为流程而非缺陷加测试；测试通过是因为 mock/夹具自证；失败原因不对仍继续改实现；把昂贵集成测试塞进快速回路；修后只跑新测试不跑邻近验证；flake 隐藏为"再跑一次就好"。
- 反例：`expect(f(a)).toBe(f(a))`、只断言 `toBeDefined`、把常量抄进断言、fixture 自证（DEF1 G-12 引 `principle-test-behavior-not-implementation` 已给五形，a2r ABC2 亦已提出；本组不再展开）。
- 产品关系：`local-defect-feedback-loop.md` 已要求"回归覆盖放在有用的行为缝；没有合适缝就报告为设计事实"，与本 SKILL 的"不强制测试"一致；本组补"先红后绿确认失败原因"和"最终回复格式"。

### 3) A–F 判断位点与专业 concern

| 位点 | concern | 何时调用 | Profile |
| --- | --- | --- | --- |
| E：写失败测试与最小修复 | 实现/测试缝 | 有便宜测试路径的缺陷 | `implementation` |
| F：失败原因的确认与修后证据 | 验证/证据 | 判断"红线是否说明问题" | `evidence-evaluation` |

### 4) 当前产品锚点、覆盖与缺口

- 已覆盖：`local-defect-feedback-loop.md`（复现/最小化/假设/回归缝/重跑）；`profiles/evidence-evaluation.md` 的"负控制"。
- 缺口：**"因预期原因失败"的确认步骤**、**坏测试清单与"宁可不加"**、**flake 的确定化与信号锁定**、**最终回复的证据格式**（failing-before 不可得时如何说）。

为何值得吸收：这是 E 的日常操作，且与产品已验证的 F 纪律互补；不引入新 gate（"只在便宜路径或用户要求时"）。

### 5) 拟处置与载体

- 拟保留：双向适用门槛；先红后绿且确认失败原因；编码意图而非实现；坏测试清单与"宁可不加"；flake 确定化+记录信号；修后邻近验证；最终回复格式。
- 拟删除：具体测试框架名（若有）；不改。
- 载体落点：并入 `local-defect-feedback-loop.md` 的"回归覆盖"段作为操作细节，或在 `methods/README.md` 加一个"TDD 适用性"短节；不新建方法文件（避免与既有方法重复）。
- 仍依赖 runtime：真实测试运行器；无运行器时按 impractical 分支报告。

### 6) 可讨论正文草稿/操作例子 + 验证方案

```markdown
## 先红后绿的最低要求（操作）
- 新测试必须因为缺陷本身失败；若它通过或因为无关原因失败，先修测试/复现，不要改实现。
- 测试编码"期望行为"，不复制当前实现细节。
- 修后复跑该测试与邻近验证；报告 failing-before 的输出与 passing-after 的运行。
- 不能给出 failing-before 时，说明原因并给出最接近的可执行检查（脚本/手工/浏览器/快照/日志断言）。
```

验证方案（**未执行**）：拿一个真实小缺陷，按六步走；再故意写一个"导入函数全返回 undefined 也通过"的测试，检查是否被坏测试清单识别并删除；造一个时序 flake，检查是否先确定化再进入回归。边界：integration-heavy 或路径不清时明确跳过并说明。

---

## H-04 · 自评反思与上下文重建（reflect / recall）

### 1) 机制与触发情境；源锚点与已读/尚缺

触发情境：会话结束/阶段性完成后想把教训沉淀进 skill（reflect）；开始或接续工作前需要重建"我做到哪了、周围发生了什么"（recall）。

源锚点（pin 内，全读）：

- `pstack/skills/reflect/SKILL.md`：只处理**durable learning**，一次性事件不算；先由父定位自己的 transcript（三种布局：flat/nested/subagent；用首行开场用户消息匹配；不跨 workspace glob）；三 reviewer 并行（judgment/tooling/divergent，各自模板与角色行）；synthesizer 输出 Accepted/Rejected/Backlog；**结构强制检查**：能被 lint/脚本/元数据/运行时检查更可靠执行的条目从 Accepted 移到 Backlog（引 `encode-lessons-in-structure`）；**应用前必须把完整三分类展示给用户并等待明确批准**（skill 变更影响未来所有 agent，不得自动应用）；Backlog 自动进团队跟踪器、只有 Accepted 等批准；按 Routing 字段精确执行（trivial 直改、substantive 走建 skill 流程、description 调优、新建）；有 SKILL 校验器就跑；总结输出固定四栏（applied/new/backlog/dropped）。
- `pstack/skills/recall/SKILL.md`：先分类路由（单个会话接续→session-pickup；习惯→automate-me；人类可读总结→另一件事）；**先锁范围**（时间窗默认近 7 天、主题、workspace；绝不把 all 静默变 recent N）；并行便宜模型按切片挖掘，按真实 mtime 排序、先 grep 主题再读匹配段、跳过当前会话与 noise（subagent/eval/test）；返回统一 schema（topic/goal/decisions/open threads/struggles/artifacts，各带 UUID）；**共享记录默认要扫**（交给 why 的 source investigators，问题改为"当前状态、试过什么没成、用户还在报什么"，null 结果也是发现，缺 MCP 要说明）；用 git/gh 对 live state 核验；输出契约（capsule ≤5 行、threads 每行一个状态 tag、problems ≤5、next move 单一）；相邻特性不进来；超屏先砍细节不砍 threads；引用 UUID/source 并脱敏。

已读：两份全文；尚缺：`reflect/references/*`（a2r 只读部分）、`recall` 依赖的 `why` 其余源。

### 2) 操作、成立条件、失败模式、反例

- **range discipline**（范围纪律）是两者的共同机制：transcript 只在当前 workspace 读、不跨项目 glob；recall 的窗口/主题/工作区必须显式；reflect 必须先确认开场消息匹配。
- **默认扫共享记录**：recall 明确"命名了特性/文件/区域/缺陷就必须扫"，只有纯活动回顾才可跳；这防止"只从自己聊天里重建"。
- **人不批准不改规则**：reflect 的 Accepted 是变更未来所有 agent 的规则，必须等待明确批准；Backlog 自动、Accepted 人工。
- **"结构优先"的再落点**：能结构化的教训不进文本 skill，而是 lint/脚本/标志；这与 DEF1 G-04 的 check-plan 样例互证。
- **输出契约**：状态 tag 使 thread 可被机读；problems 保留"反复出现的症状与回滚过的修复"（下次从上次失败处开始）。

失败模式/反例：跨 workspace 读私有 transcript；把一次性事件当 learning；自动应用 skill 修改；cap 数超时砍 threads 而不是细节；把 all 变成 recent 5；默认只读自己历史不扫共享记录；输出无 tag/无证据指针。

### 3) A–F 判断位点与专业 concern

| 位点 | concern | 何时调用 | Profile |
| --- | --- | --- | --- |
| F/A：教训的可持久性与证据 | 学习/证据 | 会话后沉淀 | `evidence-evaluation` + `intent-voice`（人类批准） |
| Driver：上下文重建与接续 | 程序性 | 开始/接续工作 | `driver` |
| D：结构化的落点 | 可维护性 | 重复指令 | `technical-planning`（辅） |

### 4) 当前产品锚点、覆盖与缺口

- 已覆盖：`profiles/driver.md` 的"检查依赖与交接资格"；a2r ABC2 MG-3（原则语言/学习编码）与 ABC3 MG-5（recall 邻接）。
- 缺口：**范围纪律**（不跨 workspace、窗口显式）；**"必须扫共享记录"的默认**；**反思必须人工批准且只把可结构化的移到 backlog**；**输出契约的状态 tag**。这些部分已被 a2r 触及（原则/回忆），本组补的是**不可越界与审批**的硬约束。

为何值得吸收：跨会话/跨来源重建是高频需求，且最容易越界（读私有聊天、静默缩小范围）；执行纪律很具体，可直接写成操作规则。

### 5) 拟处置与载体

- 拟保留：transcript 匹配与 workspace 边界；窗口/主题/工作区显式；共享记录默认扫；null 也是发现；reflect 的三视角与 Accepted/Rejected/Backlog；**不自动应用**；结构优先迁移；输出契约。
- 拟改变：具体模型/角色行/`Task` 字段 → "并行审查能力"；`~/.cursor/...` 路径 → "当前工作区的会话记录"。
- 拟删除：UUID 具体的工具调用方式、团队跟踪器名称。
- 载体落点：与 a2r 拟建的 Driver/学习方法合并（不新建）；若 a2r 已落 recall 邻接，本组作为其"范围与审批"补丁并入。
- 仍依赖 runtime：真实会话记录与共享来源；无记录时退回显式用户 capsule。

### 6) 可讨论正文草稿/操作例子 + 验证方案

```markdown
## 上下文重建（操作）
- 先声明范围：时间窗、主题、工作区；不得把"全部"静默变成"最近 N 条"。
- 只读当前工作区的记录；不要跨工作区扫描他人会话。
- 主题命中时，除了自己的历史，还要查共享记录（工单/事故/提交/聊天），并把问题从"当初为什么"改成"当前状态、试过什么没成、用户还在报什么"。
- 用 live state（分支/PR/工单）核验挖掘结果。

## 反思沉淀（操作）
- 只沉淀可复用教训；一次性事件不在此列。
- 输出分 Accepted / Rejected / Backlog；能用结构（lint/脚本/标志/运行检查）保证的条目进 Backlog 而不是文本规则。
- 应用任何规则修改前，展示完整清单并取得明确批准；规则变更影响未来所有会话。
```

验证方案（**未执行**）：造两个 workspace 的会话记录，确认 recall 只读当前工作区；给定"最近"但不给窗口，确认输出先声明默认窗口；造一条"能被 lint 保证"的反思项，确认被移到 backlog；确认未批准前没有任何 skill 修改。边界：无会话记录时不得编造历史。

---

## H-05 · TypeScript 具体映射（typescript-best-practices）

### 1) 机制与触发情境；源锚点与已读/尚缺

触发情境：读写 `.ts/.tsx` 时的语言层约定；它是 DEF1 G-12 通用类型纪律的具体语法映射。

源锚点（pin 内，全读）：`pstack/skills/typescript-best-practices/SKILL.md`：先应用 `type-system-discipline`；规则表——判别联合（`kind` 字面量，不得可选字段包）、branded types（`& { readonly __brand: "X" }`，边界校验一次）、构造式建模（`[T,...T[]]` 非空、`[T,T][]` 偶数、start+duration 区间）、最小全函数类型（只有松散类型逼出 `!`/cast/"永不发生"时才加强）、外部数据 `unknown`、schema 优先于手写 guard（`z.infer`）、禁 `as`（校验后才可）、收窄层级（判别 switch > `in` > `typeof/instanceof` > 用户 guard > `as`）、类型 guard 必须真实（撒谎的 guard 比 as 更糟，`isX/hasX` 命名）、穷尽性（`const _exhaustive: never = x`）、`satisfies` 优于 `as`、边界解析到命名领域类型、schema 派生类型（`Pick/Omit/Parameters/ReturnType/Awaited/typeof`）、对象参数（热路径例外）、真实测试（能跑就别 mock，UI 在运行构建里验，只 mock 跑不了的）、结构化遥测（带上下文的日志，发布代码无 `console.log`）。

已读：SKILL 全文；尚缺：`references/patterns.md`（DEF2 §0 列未读）。

### 2) 操作、成立条件、失败模式、反例

- 该表把 G-12 的抽象判断落到 TS 语法；吸收时应**保留语言无关的判据 + 语言层例子标注**，不把 TS 细节写成普适规则。
- 主要反例在 G-12 已列（cast/any/可选字段包/自证 guard/热路径对象参数开销/发布代码日志）；本组新增：**"撒谎的 guard"可比 `as` 更坏**（bug 藏在"安全"名下）；**收窄层级**是有序偏好而非等价选择；**schema 派生优先于手写 guard**。

### 3) A–F 判断位点与专业 concern

| 位点 | concern | 何时调用 | Profile |
| --- | --- | --- | --- |
| D/E：语言层类型与边界 | 类型/实现 | 写静态类型代码 | `technical-planning`/`implementation` |

### 4) 当前产品锚点、覆盖与缺口

- 已覆盖：DEF1 G-12 拟议的类型纪律（待 gate 裁定）。
- 缺口：如果 G-12 落地为语言无关方法，可把这张表作为**附例**；不单独新建方法。

为何值得吸收：单一映射表，低成本，高日常命中率。

### 5) 拟处置与载体

- 拟保留：整表作为附例；标注"TS 语法，语言无关判据见类型纪律"。
- 拟删除：无（若 gate 只采纳语言无关部分，则整表留 source anchor）。
- 载体落点：G-12 方法的附录或 `implementation.md` 按需入口。
- 仍依赖 runtime：TS 编译器与测试运行器。

### 6) 可讨论操作例子 + 验证方案

例子：把 `{status:string; data?:T; error?:string}` 改成 `{kind:"ok";data:T}|{kind:"err";error:string}`，确认非法组合无法构造且 switch 穷尽。验证方案（**未执行**）：在一个 TS 文件上按表逐条演示反例与修法；用一个"导入全返回 undefined 仍通过"的测试验证守卫纪律。边界：语言特定规则不外推到其他语言。

---

## H-06 · why 调查姿态与来源 playbook（code-archaeology / sentry / linear）

### 1) 机制与触发情境；源锚点与已读/尚缺

触发情境：需要"为什么这样设计"的完整调查（DEF1 G-09 已给 epistemics 与影响分析；本组补调查编排与三个源的操作细节）。

源锚点（pin 内，全读）：

- `pstack/skills/why/SKILL.md`：调查者姿态（谨慎精确、区分知道与推断）；Step 1 目标/问题解析（目标模糊时从上下文取最佳猜测并声明）；Step 2 **代码锚**（文件/行段、关键符号、最近提交、PR 号；`git blame`/`log --follow`/`log -S`/`log -G`/PR JSON）；Step 3 并行调查者（默认全量）：先列可用来源，映射到**七类**（源码控制、工单、长文档、实时聊天、基础设施可观测、错误追踪、产品分析仓）；一来源一调查者、单消息并发；防御性目标加 `incident-postmortem` 横切；**跳过必须显式且书面**（无非是 gap 不是选择；"可证明无关"是高标准）；Step 4 合成者（单独实例；默认配置与调查者不同模型家族；可访问引用核验，因 readonly 会剥掉 MCP 而用 agent 模式）；Step 5 呈现（置信措辞不改写）；输出八段 + Sources Consulted 每来源一行（含返回空与被跳过的）；**若 why 是改代码的前奏，追加 Preserve/Change/Avoid/Risk 约束集**；常见失败：近因偏差（当前形态是多次决策的沉积）。
- `sources/code-archaeology.md`（全文）：最可信来源；`git log --follow`/pickaxe `/S` `-G`/blame/PR JSON（`reviews`+`comments` 才有信号）/ADR/TODO-FIXME/tests 名字/co-change/CHANGELOG；证据形态（解释问题的 PR 描述、争论替代方案的 review thread、解释非显然约束的行内注释、揭示边界用例的测试名、引用工单/incident 的 commit、用户可见 rationale 的 changelog）；坑：squash flatlands、误导性 commit message（看 diff 不看话）、cargo-cult（追更早的引入 commit）、bot/auto-merge、**把代码当意图证据**；返回每条带原文/引用/作者/日期/直接或间接。
- `sources/sentry.md`（全文）：错误轨迹的**时间相关性**是最有价值信号（first/last seen、频率轨迹、affected releases 与目标 PR 日期对齐）；查询（issues/events/releases/replays/profiles/评论）；坑：grouping drift、release 相关混杂、silent fixes、resolved≠fixed、Seer 幻觉、采样；返回 issue 元数据 + stack 片段 + 时间相关性 + 链接 + 作者注释。
- `sources/linear.md`（全文）：工单承载**产品/业务强制力**；先取被引用工单、再关键词、走父子树（父常带 why）、项目文档、标签/里程碑；坑：scope drift、模板化"Why"、陈旧工单、duplicate 链、私有 workspace；返回原文引用（不转述）+ 标签/父/项目/作者/日期/链接。

已读：上述；尚缺：`why/references/investigator-prompt.md`、`synthesizer-prompt.md`（a2r 已读后者）、`sources/{notion,slack,databricks}.md`、`source-playbook.md`。

### 2) 操作、成立条件、失败模式、反例

- **先建代码锚再并行**，否则调查会发散到泛泛主题。
- **七类来源的覆盖图**：空结果要记录，跳过要书面；这与"缺失证据是合法输出"（G-09）一致，提供可审计的搜索面。
- **每源一份 playbook + 单工具**：一个调查者一个 MCP，避免"一个 agent 覆盖多源"。
- **时间相关性 ≠ 因果**（Sentry 的坑与 Datadog 同源）；**resolved 是人类标记**；**私有不可达记为 gap**。
- **返回原文而非转述**：合成者需要可引用文本。
- **结尾约束集**：当调查是变更前奏时，产出 Preserve/Change/Avoid/Risk，直接喂 D 的 Plan。

失败模式/反例：只查 git 或只查自己的聊天；把"没有工单"当"没有业务动机"；把 Sentry 的 release 相关当证明；用 bot commit/auto-merge 找意图；把 Seer/AI 分析当一手证据；跳过项不写理由；输出自信叙事（G-09 已给措辞纪律）。

### 3) A–F 判断位点与专业 concern

| 位点 | concern | 何时调用 | Profile |
| --- | --- | --- | --- |
| F：证据来源覆盖与置信 | 研究/证据 | 回答动机/回归 | `evidence-evaluation` |
| A/B/C：动机归属 | 目标/行为/语义 | 结论涉及决定权 | 按结论回相应 Profile |
| D：Preserve/Change/Avoid/Risk | 架构约束 | 调查是变更前奏 | `technical-planning` |

### 4) 当前产品锚点、覆盖与缺口

- 已覆盖：DEF1 G-09 拟议的五层置信与 blast-radius；a2r ABC3 补读 synthesizer-prompt。
- 缺口：**调查编排**（代码锚、七类来源覆盖、一源一人、跳过书面、输出八段 + Sources Consulted、约束集）。这是 G-09 的"操作臂"。

为何值得吸收：把"未知"变成可审计的搜索面，是 F/D 的高价值能力；且可在无 MCP 环境下退化为"仅有源码控制"。

### 5) 拟处置与载体

- 拟保留：代码锚步骤；七类来源与覆盖图；空结果/跳过书面；一源一人；原文引用；时间相关性≠因果；resolved 是人类标记；结尾约束集；近因偏差警示。
- 拟改变：MCP/具体工具名 → "可用的一手来源";`gh/git` 命令作为例子。
- 拟删除：模型角色行、具体 tracker 名。
- 载体落点：与 DEF1 G-09 合为一份 `rationale-research.md`（本组提供编排与源 playbook 附录）；`methods/README.md` 一行。
- 仍依赖 runtime：真实仓库/工单/遥测/聊天；无外部源时只做源码控制并与输出中注明。

### 6) 可讨论正文草稿/操作例子 + 验证方案

```markdown
##动机调查编排（操作）
1. 先建代码锚：文件/行段、符号、最近提交、PR 号（`blame`/`--follow`/pickaxe）。
2. 列出可用的一手来源并分类；每类一个调查者、并发；防御性代码额外查事故视角。
3. 每类返回原文引用 + 标识 + 作者/日期 + 直接/间接；空结果写"查过、没有"；跳过要写理由。
4. 合成：置信分层措辞不改写；矛盾并置；代码不作为意图证据；输出含"我们不知道什么"。
5. 若这是变更前奏，追加 Preserve / Change / Avoid / Risk 约束集。
```

验证方案（**未执行**）：选一段防御性代码，按七类各写"查了/空/跳过+理由"；用 Sentry/Datadog 任一可用源验证"时间相关性≠因果"的例子；输出八段并抽查引用可解析。边界：无外部 MCP 时只保留代码锚与源码控制。

---

## H-07 · 评审质量镜头细则（interrogate/code-quality-review.md）

### 1) 机制与触发情境；源锚点与已读/尚缺

触发情境：对抗式评审需要一份攻击性质量镜头；a2r ABC3 已将 `rubric.md`/`lead-judgment.md` 拟入其评审方法，但明确把本文件列为残余。

源锚点（pin 内，全读）：`pstack/skills/interrogate/references/code-quality-review.md`：Core Prompt（深度审计当前分支、行为不变地重构、提高抽象/模块化/简洁/可读、允许大改、measure twice cut once）；八个维度（0 结构简化 ambitious；1 文件从 <1k 到 >1k 是强 smell；2 禁止 spaghetti 增长；3 清理设计而非接受能跑；4 直白而非魔法；5 类型/边界；6 逻辑在 canonical 层、复用既有 helper；7 不必要的串行与不原子更新）；输出优先级；**approval bar 的 presumptive blockers**（保留大量 incidental complexity 且存在 code-judo；跨 1k 行；tangles；散落 feature check；多余抽象/包裹/cast；重复 helper/放错层）；tone。

与 thermo-nuclear 的关系（本包核对）：两者内容高度重合（DEF1 G-10 已证 `thermos` 与 `cursor-team-kit` 的质量 rubric 逐字节一致）；`interrogate` 这份是**同一质量标准的镜头版**（面向多模型评审的 lens），不是独立机制。建议吸收时**复用同一份质量标准**，把本文件作为其"多模型评审附录"而非新规则。

### 2) 操作、成立条件、失败模式、反例

- 成立条件：有明确 diff/分支；评审者被允许 ambition（结构大改）；输出按结构回归优先而非 nitpick 洪流。
- 失败模式：把 1k 行当唯一指标；对所有 diff 要求 code-judo（小变更上过度要求）；approval bar 被读成硬 gate（源文说 presumptive blocker，须作者给出理由）；与 thermo-nuclear 并列为两套标准导致分叉（G-10 已给单源纪律）。

### 3) A–F 判断位点与专业 concern

| 位点 | concern | 何时调用 | Profile |
| --- | --- | --- | --- |
| F：质量镜头与批准条 | 质量/可维护性 | diff 审计 | `evidence-evaluation` |
| D：结构简化/t 类型/边界 | 架构 | 结构回归 | `technical-planning` |

### 4) 当前产品锚点、覆盖与缺口

- 已覆盖：a2r MG-6 拟议评审裁决方法；`profiles/technical-planning.md` 的"别把私有模块当无关"等。
- 缺口：镜头维度表与 approval bar 作为**质量标准的附属镜头**；建议随 a2r 落地，不另建方法。

为何值得吸收：给评审提供一个可复用的"质量 lens"，且明确它复用既有标准、不新增 gate。

### 5) 拟处置与载体

- 拟保留：八维与 approval bar 作为 lens 附录；结构优先的输出顺序。
- 拟改变：1k 行阈值标为来源经验；"code judo" 作为启发式不是硬门。
- 拟删除：与 thermo-nuclear 重复的正文，只留单一标准 + 引用。
- 载体落点：a2r 评审方法的附录（与 `rubric.md` 合并引用）。
- 仍依赖 runtime：无。

### 6) 可讨论操作例子 + 验证方案

例子：对一个真实小 diff 跑该 lens，输出限 5 条以内并按结构优先级排序；与 rubric 结果对照去重。验证方案（**未执行**）：确认同一 diff 不会因两套重复标准产生冲突结论。边界：小改动不做结构大改要求。

---

## H-08 · SDK 集成参考（auth / streaming / mcp）

### 1) 机制与触发情境；源锚点与已读/尚缺

触发情境：把 agent 能力以真实 SDK 集成进脚本/服务（DEF1 G-12 的 runtime 依赖面）。

源锚点（pin 内，全读）：

- `references/auth.md`：两种 key（用户 / 团队服务账号）同槽位、同格式、不可目视区分；查找顺序（显式 `apiKey` → env）；共享基础设施必须显式传 `apiKey`；症状表（首 send 的 AuthenticationError；BAD_USER_API_KEY；仅 cloud 失败；`ERROR_GITHUB_NO_USER_CREDENTIALS` 不是代码 bug；CI 401 多为注入问题；间歇 401 多为轮换/双值）；轮换纪律（生产定期轮换、泄露先撤销再新建、按环境分 key）；同进程多 key 支持。
- `references/streaming.md`：stream 与 wait 的分工（"没有只 stream 不 wait 的正确模式"）；事件类型参考（assistant/thinking/tool_call/status/task/user/system/request；tool_use 公告 vs tool_call 执行；request_id 关联）；何时 stream（渲染/日志/可观测/轮询他人 run）与不必 stream；每事件带 `agent_id`/`run_id`。
- `references/mcp.md`：两种传输、三种部署形态（本地 stdio / 本地或远程 http / 云内 stdio）；**云 stdio 拒绝 `cwd`**（`ConfigurationError("Cloud MCP server cannot include cwd.")`）；本地 stdio 是子进程（需 dispose 收尸）；本地 http headers 直发；`auth: {CLIENT_ID, CLIENT_SECRET?, scopes?}` 触发 OAuth；云上 **http headers/auth 由后端代理并服务端脱敏**，**stdio env 注入云 VM**（视同生产秘密、勿放终端用户凭据）；`command/args` 必须在云 VM 内可解析；仪表盘配置的 MCP 在云上生效且内联配置叠加；**`Agent.resume` 不持久化内联 mcpServers**。

已读：三份全文；尚缺：`patterns.md`、`advanced.md`。

### 2) 操作、成立条件、失败模式、反例

- 可迁移结论（与 DEF1 G-12 合并）：两类失败分离、生命周期 dispose、`supports` 守卫、resume 重传配置、显式 key、退避重试边界。
- 平台专属证据（标注）：具体错误码、dashboard 步骤、云 VM 行为、`cwd` 拒绝。
- 安全判断：**云上 http headers 被代理脱敏 vs 云 stdio env 注入 VM** 是"凭据去向"的关键差异；本地 stdio 是"调用者机器执行"。与 DEF1 G-13 的凭据形态分类互补（本地/云两个维度）。
- 反例：把 `agent_id` 当 run id；只 stream 不 wait；共享服务依赖 env 变量；在 CI 里忘了 secret 作用域；云 stdio 带 `cwd`；把终端用户凭据通过 stdio env 注入云 VM；resume 后以为 MCP 还在。

### 3) A–F 判断位点与专业 concern

| 位点 | concern | 何时调用 | Profile |
| --- | --- | --- | --- |
| D/E：runtime 选择、凭据去向、生命周期 | 接口/安全/可靠性 | 集成真实 SDK | `technical-planning`/`implementation` |
| F：真实 Provider/部署的验证腿 | 验证/证据 | 需要真实 leg 的主张 | `evidence-evaluation` |

### 4) 当前产品锚点、覆盖与缺口

- 已覆盖：`behavior-claim-evaluation.md` 的"真实 Provider/部署需要真实 leg"；`guide-mock-adapter-choice.md` 的适配器覆盖边界。
- 缺口：把"两类失败/生命周期/能力守卫/凭据去向"作为**真实 SDK 集成的最小纪律**；DEF1 G-12 已提出，本组补三份 reference 的逐条证据。

为何值得吸收：产品要求"真实 leg"，但没写"真实集成最容易在哪些点失败"。这些都是 E 的可执行警告。

### 5) 拟处置与载体

- 拟保留：两类失败 + 退出码分离；dispose/wait/supports；resume 重传配置；显式 key；retry 边界；凭据去向（代理脱敏 vs VM 注入）；命令必须在目标 VM 可解析。
- 拟改变：`@cursor/sdk` API 名 → 通用"run 句柄与 agent 生命周期"；错误码作为"平台示例"。
- 拟删除：dashboard URL、具体 slug。
- 载体落点：G-12 方法的"真实 SDK 集成"附节；`methods/README.md` 一行按需入口；不单独成方法。
- 仍依赖 runtime：任何真实 SDK/Provider；无真实调用时必须标未验证。

### 6) 可讨论操作例子 + 验证方案

```markdown
## 真实 SDK 集成最小纪律（摘要）
- 启动失败（未开始执行）与运行失败（做了但失败）分开处理：不同原因、不同处置、不同退出码。
- 每个 agent/run 句柄在 finally 释放；终态必须等待；调用可选操作前先查询支持性。
- 恢复已有会话时，内联的外部工具配置不会自动保留，必须重传。
- 共享基础设施显式传凭据，不用环境变量兜底。
- 凭据去向按传输形态区分：经宿主代理的请求头 vs 注入执行环境的变量；后者视同生产秘密。
```

验证方案（**未执行**）：mock 三类失败（启动抛错/运行 error/操作不支持）验证分流；真实进行一次本地集成，观察 dispose 后无残留子进程；对云/代理路径记录"凭据是否落入执行环境"。边界：无真实 Provider 时只做 mock 与结构验证。

---

## H-09 · benny 运行文件的硬安全规则（triage / reproduce）

### 1) 机制与触发情境；源锚点与已读/尚缺

触发情境：外部触发的自动化（如聊天报告）需要"只在该线程说一次、绝不越界、失败关闭"；DEF1 G-08 已覆盖 adapter/verify-existing-fix/config，本组补两个操作文件的硬安全规则。

源锚点（pin 内，全读）：

- `pstack/automations/benny/skills/triage-issue-reports/SKILL.md`：**硬安全规则**（源频道/根线程坐标不可变；绝不发根消息；绝不发别处/DM/广播/新线程；tracker 写入前与 verdict 发布前做 parent 预检；parent 缺失/删除/不可达/不确定 → 停止且不写；只发一条实质 verdict；coordinator 是唯一 Slack 发布者；子 worker 只返回发现、只读、不得有 Slack 凭据或写动作；每个子 prompt 必须显式禁止 Slack 写工具；无法强制隔离就在 coordinator 里做；不能回链的票不建；宁可不建也不猜/重复）；流程（冻结坐标含 permalink；读全帖与附件、不可读要在 verdict 说明、不编造；路由前做有界的 cause trace——`how` 走路径、`why` 查回归/防御代码、查近期改动与已有 PR、区分事实/假设；无法读仓就不猜 owner 并保守分类；四分类 Bug/Performance/Feature/Question；只发一条实用 verdict）。
- `pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md`：等待**可信 triage 标记**（作者匹配配置身份、是根线程下的回复、恰好一个标记）；只对 bug/performance 继续；`other`/缺标记/不可信/冲突/超时都静默停；ownership 门（人明确认领或要求实现才算；bot 汇总/查日志/要求诊断/假设不算）；已有 PR/commit → 切 verify 模式不另写；**同一判别性症状必须通过真实 UI 出现两次**；state 检查只能确认不能注入症状；无确认复现不得写修复；`github.com` PR 链接；捕获物/录像/日志/token 不进源码管理；coordinator 是唯一 Slack 发布者；子分析 worker 只读；修复阶段代码 worker 只有在**可证明排除 Slack 凭据与所有写动作**的环境才可编辑，否则 coordinator 自己改；每个子 prompt 显式禁止 Slack 写；子任务不发 token/发布坐标/对外权限；需要 Slack 写才能运行的任务不得启动；工具 bot 是证据来源，除人类明确外不拥有修复。

已读：两份全文；尚缺：`setup-benny/SKILL.md`（配置/首建流程）、`templates/*`。

### 2) 操作、成立条件、失败模式、反例

- **不可变坐标 + 每次发布前后预检**：这是"外部系统写动作"的最小安全协议（与 DEF1 G-03 的 Slack 边界互补：G-03 是机器侧队列约束，本组是 agent 行为约束）。
- **可信标记替代自由文本**：只有配置身份的回复 + 恰好一个标记才算 triage 契约；这防止"有人随口说修好了"触发自动化。
- **怀疑但不停摆**：等待时保持沉默、超时静默停；不重试到根或备用频道。
- **子实例最小权限**：子 worker 只读、无外部写凭据；代码 worker 要"可证明排除写能力"，否则 coordinator 自己做。这是"工具权限 ≠ 动作许可"在自动化里的对应物。
- **证据双复现**：同症状经真实 UI 两次；state 只读；无复现不写修复。
- **失败关闭**：配置/adapter/feature map 缺失或不确定 → 停。

失败模式/反例：坐标用回复/operations 时间戳替换；parent 校验只在开始时做一次；子 worker 带 Slack token；一个 approval 覆盖多个动作；把 bot 的假设当认领；已有 PR 时另开竞争 PR；只复现一次就修；把 state 注入当复现；工具 bot 当修复 owner；超时后在根频道或别处兜底发布。

### 3) A–F 判断位点与专业 concern

| 位点 | concern | 何时调用 | Profile |
| --- | --- | --- | --- |
| F/D：外部写动作的边界与失败关闭 | 安全/证据 | 外部触发的自动化 | `evidence-evaluation`+`technical-planning` |
| E：子实例权限隔离 | 实现/安全 | 委派到子 worker | `implementation` |
| Driver：所有权与路由 | 程序性 | 谁来修、何时停 | `driver` |

### 4) 当前产品锚点、覆盖与缺口

- 已覆盖：Backbone 的"工具权限≠执行授权"；`profiles/evidence-evaluation.md` 的独立性；DEF1 G-03 的机器侧边界。
- 缺口：**外部触发的 agent 行为协议**——不可变坐标、可信标记、子实例无写凭据、失败关闭、证据双复现。产品没有"自动化"层的方法，但这些都是 D/E/F 的安全操作。

为何值得吸收：任何把 agent 接上外部系统的团队都会遇到"越界发布/误触发/子实例权限";这些规则可独立于 Slack 表述为"外部写动作的最小协议"。

### 5) 拟处置与载体

- 拟保留：不可变坐标 + 发布前后预检；可信标记（身份+位置+唯一性）；等待期沉默与超时静默；子实例只读/无写凭据；需要写能力才能运行的任务不启动；工具 bot 是证据非 owner；已有修复→verify 模式；双复现；失败关闭；无回链不建票。
- 拟改变：Slack→"外部可见通道"；benny/`[benny:*]` 标记→"配置的可信标记"；具体 tracker 字段删除。
- 拟删除：benny 命名与目录。
- 载体落点：与 DEF1 G-03 合并为 `external-write-boundary.md`（本组提供行为协议一节）；`methods/README.md` 一行。
- 仍依赖 runtime：真实外部通道与权限隔离；无法隔离时规则要求降级到 coordinator。

### 6) 可讨论正文草稿/操作例子 + 验证方案

```markdown
## 外部写动作最小协议（操作）
- 冻结目标坐标（频道/线程/接收者）并在每次写前复核；只写该坐标，绝不回退到根或备用目标。
- 触发器必须是可信且唯一的标记（身份匹配 + 位置匹配 + 恰好一个）；否则静默停止。
- 子实例默认只读、无外部写凭据；需要写能力才能运行的工作不在子实例做。
- 失败关闭：配置/驱动面/坐标缺失或不确定时不做任何写。
- 证据：同一判别性症状在真实界面上出现两次；状态检查只读，不注入症状；已有修复工件时改为验证它而不另写。
```

验证方案（**未执行**）：mock 外部通道，检查：坐标替换、parent 消失、子任务带写工具、重复标记、超时后写根频道、已有 PR 时另写等场景是否全部被拦或静默停。边界：无外部系统时只验证行为协议，不声称外部效果。

---

## 2 · 尾部增量（对 DEF1 G-14 的更新）

| # | 面 | 本包状态 |
| --- | --- | --- |
| T-04' | cursor-team-kit 交付技能 | H-01 已读 6/13；其余（get-pr-comments、review-and-ship、verify-this、weekly-review、what-did-i-get-done、workflow-from-chats、check-compiler-errors、deslop、typescript-exhaustive-switch）仍属 A/B/C 或已由 a2r/产品覆盖 |
| T-05' | pstack 未读 skills | H-02（arena/swarm）、H-03（tdd）、H-04（reflect/recall）、H-05（typescript-best-practices）已补；`how/architect/figure-it-out/automate-me/setup-pstack/make-bot-ui/unslop` 仍列未读（B/A 侧为主）；`typescript-best-practices/references/patterns.md` 未读 |
| T-05'' | why | H-06 补 SKILL + 3 源；`investigator-prompt`、`notion/slack/databricks` 三源、`source-playbook` 未读 |
| T-05''' | interrogate | H-07 补齐 `code-quality-review.md`；`reviewer-prompt.md` 由 a2r 已读 |
| T-08' | cursor-sdk references | H-08 补 auth/streaming/mcp；`patterns.md`、`advanced.md` 未读 |
| T-09' | benny | H-09 补 triage/reproduce SKILL；`setup-benny/SKILL.md`、模板、示例未读 |
| T-06 | orchestrate schemas/cli/tools/tests 正文 | 未读；DEF1 已覆盖行为契约，精确接口按需回读 |
| T-01/02/03/12 | 纯资产/CHANGELOG/third_party 全量/marketplace | 未变；G-13 已给分类框架 |

---

## 3 · 机械自检（非专业裁定）

- 本包只新增 `docs/absorption/2026-10-02/packages/A4-CURSOR-DEF2.md`；未改产品、未改他人文档、未 commit、未执行源内任何脚本/测试。
- 源引用均为 `cursor-plugins` @ `ecc249f1…` + repo-relative path + section；未读项在 §0 与 §2 明示。
- 与 DEF1/a2r 的分工在 §1 逐组声明；本包不重述 a2r 已拟入方法的正文。
- 本包机制组 9 个（H-01..H-09）；无采纳裁定、无权限创设、无 registry/框架新增。
