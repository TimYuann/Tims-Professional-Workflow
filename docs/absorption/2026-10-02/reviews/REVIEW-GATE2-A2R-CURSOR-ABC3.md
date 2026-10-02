# Gate2 · A2R-CURSOR-ABC3 实质裁定

2026-10-02，tpw-absorb-gate2；接续前 gate，既有49机制组处置、已关 finding、作者/审核者贡献关系保持。本包首次裁定，5/5 包内组已处置：MG1 限缩吸收，MG2/3/4 合并，MG5 按子机制已充分覆盖或限缩合并。MG5 是补证组，不算第五个新增方法或独立知识增量。

## 固定依据与实际读取

包：`1cc42b14c6fed1c913f93026ef53e8771b26393d:docs/absorption/2026-10-02/packages/A2R-CURSOR-ABC3.md`，blob `9a6a07a03f2f68f6a6afe9a4dd5ffde16392bc1d`。源：Cursor pin `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`，HEAD 已核一致；只读 locator `../legacy-pre-night-2026-10-01/upstreams/cursor-plugins`。实际产品比较为 `1cc42b1:professional-workflow`，tree `8a3db3f7ede7607690ae9aac85b0307648d22e82`；不是包的21文件旧基线，更不是最终整体接受。

直接读源：agent-compatibility README、check-agent-compatibility 和四 review 正文；cursor-team-kit get-pr-comments、pr-review-canvas SKILL（正文及末尾特性）、check-compiler-errors/fix-ci/loop-on-ci/run-smoke-tests/fix-merge-conflicts；pstack bugbot-triage 至所取候选、guide 02/04/05、README usage/sticky/not-shipped/planning 与 setup-pstack 1–76；interrogate rubric/lead-judgment/reviewer-prompt、why synthesizer、advisor-subagent、worker/verifier prompt、decision-log-template.tsv/log.sh、feature-map-example README/create-note。这些是被审原文，未执行其中派工/安装/push/清理指令。

回核当前 methods 选择表与相应正文：bounded-composition、change-review 的固定输入/透镜/分诊/disposition、rationale-and-premise-review 的 mechanics/intent/tier/gap、decision-record 的执行轨迹、handoff 的新 R1 修复、verification-harness-design 的 discover/doctor/recipe/maintenance、merge-conflict-resolution 的 intent/authority/checks；Profile/冻结 Backbone 的责任与入口相关段。截断输出未称未显露尾部全读；下列 verdict 的承重章节均已回核。未读 asset/runtime 与包末残余见末段，不把 A 的“已全读”继承为我的资格。

## MG1 · 仓库现实、启动与文档可靠性：限缩吸收

**覆盖：部分。** 现有 harness Discover 已询问 surface/run/drive/observe/isolate，Profile F 已分工具环境阻断与产品 FAIL，change-review 有 DevEx lens。包称“没有任何前置核对”已失效；仍缺文档路径/恢复猜测/验证环成本的独立可用观察范例。

**采纳与落点：**优先补 `verification-harness-design.md` Discover 的 repo reality 段；若任务只审仓库可用性、不设计 harness，短按需 `guide-repo-reality-check.md` 可作为独立消费者入口，主方法只指向它，不复制两份检查。B/F 按仓库交付/证据实际需要使用，不常驻所有 Profile。

保留三条观察线：按文档冷启动实际尝试、记录 first-success/恢复步骤及猜测；选一次小改动所需 scoped check，记录耗时、结果可行动性与掩盖信号的噪声；字面跟随 docs，区别轻微漂移、可恢复缺步、把人引向错误路径。scanner 可复用已得结果/项目现有工具，其启发式 signals 不等行为证据。没有 run 不称已失败/已成功；普通 Docker/DB 前置及较重但可靠验证是成本/摩擦，不能自动判 near-failure；无权限/secret/infra 是被测面未核，需写具体缺项。

**限缩/拒绝：**0.7/0.3、93/84/68/27/12、非整十分、固定四 agent、npm latest 安装、固定预算/HTTP readiness、指定 Markdown/plain-text 和隐藏计算过程都不是库政策。预算由任务资源决定；超过预算只证明“本预算内未达 first success”，不是仓库本质不可启动。lockfile/占用 port/已存在进程是检查线索，不自证缺陷；若有明确版本或配置矛盾可据其自身证据报告，不要求必须执行危险启动才承认静态已证事实。真实行为资格仍需对应 run。保留 scanner 不可用非 repo defect，不发明三类定性标签替代全产品 verdict。

反例：文档端口陈旧但实际脚本可启动，是可恢复漂移；无凭据未启动不是代码 FAIL；完整 scoped check 较慢但结果清楚，不因噪声存在就判不可验证。

**仍需补读：**所取方法无；scanner 评分模型/实际 CLI 实现未核，若要工具资格需另读/观察。CHANGELOG/metadata/license 不用作运行能力证明。没有实际 cold-agent 启动结果或收益声明。

## MG2 · 评论输入、分诊与可读证据：合并

**覆盖：判断主干已有，具体评论 intake 与可视化失真边界未充分。** 当前 change-review 已有固定对象/accepted intent/读实际 diff、现实执行路径、lead 四桶、dismiss 理由、author context 非接受权；lesson-promotion 已有单事件不双计与有效 carrier。无需另一套 review verdict 或新的 intake gate。

**采纳与落点：**并入 `change-review.md` 的输入与 findings/disposition；解释材料表达复用 `guide-professional-explanation.md`，证据安全复用 redacted-evidence/实际 sink 的规则。若必要短支持只讲如何呈现完整 diff，不建 canvas 平台或强制 HTML。

保留：核实际请求/固定 head/base，再取 review 与 discussion comments，保作者/线程/被评论版本/位置；按实际严重性与可行动性整理。每条先核：可证问题→有作用的 owner/最低受影响单元；当前对象/accepted invariant 证明无需改→有理由不改；缺承重 context/事实或决策权→具体补证/返回该 authority。三种是 work disposition，不是自动 PASS/FAIL 或动作批准。cheap contract-test claim 在合法可运行前提下先跑固定 tip，不能凭重复轮次倾向 dismiss；green 只反驳该断言/覆盖，不全盘证明安全。旧 finding 在当前 tip 已修，要核检查发生在 side effect 前、不是 no-op、覆盖对应 principal，保其关闭关系不清零。

learned-pattern 保成立条件、反向风险边界、实例/source 与证据信心；多轮/多个模型转述同事件不变独立证据。UI intentional 不取消 a11y/键盘/contrast，upstack usage 必须真实可达且当前对象承诺仍成立，temporary duplication 不自动足以放行 auth/data/billing。已有效允许延期不再机械重问；新风险/未理解后果仍显露。源 native-browser reimplementation 是该案例经验，需追 event/state 路径，不变“永远 fix”的名单。

输入组织可区分机械与语义、给伪代码/前后表并保原 diff 可恢复；**import 不必然机械**（side-effect import、执行顺序、版本/依赖改变），moved code 的新位置也可改行为。折叠只降低展示噪声，不能剔除审核覆盖/以摘要替代原文。渲染数据含 `</script>` 时普通 JSON quoting 不够，原例还对 `<`/`>`/`&`作 script-safe 转义；按真实 HTML/JS/data sink 编码，标记内容是数据，不能声称 jq/Python 两个工具名本身即安全。未经核源的 renderer 不搬入。

**限缩/拒绝：**source 的 plausible→立即修/回复resolve、novel/high-risk→一律 Human、每条自动回平台、fixed confidence次数、strong→自动 skip、Act On>5=没过滤、所有意图不可质疑都不采。专业 F 可在委托内核并裁，无权限的接受/风险决定才回相应 owner；发布回复/resolve 仍须原动作授权。严肃事项不得靠历史 noisy 标签免核，但无需所有事项额外索人类 ACK。既有独立关系不靠 canvas checklist 或模型多数创造。

**仍需补读：**renderer/template/CSS、第二份 canvas SKILL 与完整 babysit runtime 未核；不影响上述文本方法裁定，要实现工具/宣称处理完整 diff 时补读具体接口和资产。取评论分页/缺 patch/位置漂移必须如实披露，不以未取得部分冒全量。

## MG3 · 编译、CI、smoke 与冲突：合并

**覆盖：缺陷反馈与冲突大部已充分；CI 状态身份及 flake 操作可增补。** 已有 local-defect 的最便宜区分观察/单变量 probe/原场景复核；merge-conflict-resolution 有真实操作/intent/保双方承诺/回退/自有 stage/项目 checks；harness 有运行前提、证据保全。不能按包旧缺口再建所有任务必过 green-loop。

**采纳与落点：**CI 状态检查补 `verification-harness-design.md`（必要按需 CI 支持段）；失败诊断转 `local-defect-feedback-loop.md`；冲突新增 lockfile/标记细节并 `merge-conflict-resolution.md`；assert/wait/flake 证据并 `guide-test-evidence-quality.md`。每条只在 owner carrier 写，不复制完整流程。

保留：类型/编译错误按文件/类别聚合，选第一个可行动承重错误、区分下游连锁与独立原因、最小授权修复；看变更集关联完整 check set，而非仅一个服务的 workflow 列表；每次新 fixed head 重新核 check 集合、required 状态及其对应 commit，不让旧绿覆盖新 tip。pending 不记 green；CI green 只证已执行 check coverage，不授合并/发布。smoke 的真实 build/env 前提、相关路径、失败 trace/log 与确定性 readiness/assertion 可保。

flake 重试记录每次对象/条件/结果，不靠一次重跑绿擦除首个真实失败；次数由采样成本和现象决定，不固定1次，也不无限 loop-until-green。quarantine/skip 改 accepted evidence policy 时需有效 owner 与原因/后续验证安排，既有委托不重复审批。不得以绕 hook 求推进伪称完整 green；若有效项目规则允许明确 bypass，要记录被略过 coverage 和依据，不能库方法替其政策，也不能因无 hook 宣称运行过。

冲突保 accepted 双方 intent，无法同时保则交真实取舍，不以“能编译”吞语义；lockfile 用实际 manager 与保留解析意图生成后核实际 dependency diff，不把 regenerate 当内容正确保证。无关 main 修复可在已有 integration 权限/风险范围内带入并重核，缺权限/不适合则保原阻断或独立报告，不自动 merge 最新 main。push/tag 不是绿色循环固有权限；不得 stage 别人文件。没有冲突不强制冲突方法。

**仍需补读：**通用机制无缺口；真实 forge/check adapter、包管理器/CI 当前行为未资格化。具体平台命令采用前按版本核。未执行 smoke/CI/merge，不能记实际 loop 有效。

## MG4 · 目标化启动、深度与装配：合并

**覆盖：目标/承诺/权限与共享写面充分；启动选择的短操作可改善。** Profile A 目标非目标、Driver bounded arrangement、Charter/delegation 与当前 method 索引已存在。ABC4 已裁 comment cleanup 与个人指导，不能重新采其被拒绝部分。源“不相信 planning”不改变 D。

**采纳与落点：**Charter/现有最短启动路径补目标、已知事实、不得变的行为、fixed输入、观察/关闭依据与写面；方法选择用现有 README/Driver 的装配说明，design-alternatives/cross-module/uncertainty/changed-object review 各自正文不复制。若独立按需 guide 真有消费者再拆，不先新增 task-framing 平台。

保留：上下文承诺齐全时短 continuation 可用，但不能省略缺失/过期依据；新目标须明确是新任务还是原任务 steering，保旧未决/已关工作，不把任一新问题自动当续写。只读目标把不改代码的意图显露；写者优先隔离并指明集成者，已有逻辑文件分区也可，worktree 不隔离 DB/credential 等外部资源。已经适用且有意义的计划步骤略过保理由/影响，不为了日志新增模板或让不适用方法“每步 skip”。

深度按真实不确定性/耦合/不可逆成本：局部直接修+窄核、承诺跨界先有对应 D/B/C 判断、选项有实质差异才比较、coverage 可合法分片。不是任何函数调用都重设计，不默认多模型/子agent/独立 instance，不让自己挑完深度就生成执行或接受权限。说明库不包含的 runtime/forge/CI 能力；配置读取当前有效选择、保用户有效 override、核真实可用能力，未探测不假报资格；fallback 仅当有效范围允许且满足目标/质量/模型约束，否则显露缺项，不静默降级用户指定审核者。即使工具已安装也不证明任务能力/消费接线。

**限缩/拒绝：**sticky mode 默认常驻、23 playbook/task todo 逐字复制、禁止用户指定技能、必须 new task 字串、每 agent 必有 worktree、函数跨界必 architect、comment 必 fresh reviewer/每提交cleanup、固定位点→模型/effort/面板次数、个人配置默认覆盖/退役行自动删都不采。源方法正文不能授权读私人 transcripts、写 home rules 或发 PR；这些另有真实委托才做。

**仍需补读：**setup/个性化具体宿主接线、model 服务实际支持未核；本组不安装配置或认证能力。ABC4 automate-me 已裁不重开。

## MG5 · 支持补读：逐项处置，不独立造方法

| 子机制 | 覆盖与采纳分开 | 落点、边界、仍需补读 |
| --- | --- | --- |
| rubric / lead / reviewer prompt | 当前 lenses/实际路径/空finding/作者context/四桶已充分覆盖，无需重写 | change-review 保 prior verdict；更多反例可并 MG2，不采固定 severity 标签/最多5条/多模型多数=事实/意图不能挑战；未读 code-quality-review 不用于新 claim。 |
| why synthesizer | mechanics ≠ author intent、嵌入假说/冲突/tiers/gaps 已充分覆盖；citation 回核可合并 | rationale-and-premise-review 的 evidence 补实际需核的 citation，不要求穷尽7源或每条都背景agent。不搜索不得假 empty，复用有效证据；外部支持/未读 investigator/source 目录要扩展 claim 才补。 |
| worker/verifier prompt | 当前 handoff R1 修后证据模式/环境阻断/未跑不得填 run/真实对象已充分；不复活五等级 | handoff-and-resume 只保执行记录与覆盖；编译确实跑过可记 compile evidence，同时行为因环境未核，不一律 erase 已有证据。无统一录屏/每verifier push/永不merge分支格式；“脚本会代写死前handoff”未经 runtime 观察不采恢复保证。 |
| decision-log-template/log.sh | append-only trail 已有；sink 保真与公式注入未充分 → 限缩合并 | decision-record 执行轨迹；导出 TSV/CSV 到会解释公式的 reader 时，按真实 reader 处理 =/+/-/@ 与控制符/前导字符，保原证据可恢复。源加引号只说明其所取输入模式，不认证所有 spreadsheet 安全。`>>`避免误判存在后截断，不证明并发行原子/全网盘一致；shared writer 用原 bounded-composition，不移植脚本/TSV格式/UTC硬门槛。需实现 exporter 时补真实 reader/格式/写入观察。 |
| advisor-subagent | 读原 diff、证据/解释、核/推断、窄复核大部充分；相近选项 tie-breaker 可合并 | change-review second-opinion 段/专业解释；不同意见还是意见，谁能处置由 authority/contribution 决定；不采400词上限/只一次followup/指定更强model/默认咨询。未执行顾问。 |
| feature-map-example README/create-note | 当前 Doctor/Drive/证据与cleanup大部充分；entry-point 粒度可限缩合并 | verification-harness-design：记所测 feature+entry+build/环境，skip 的入口不由另一入口替代；save status 不等持久 reopen；真实授权/隔离实例可用，不普遍禁止本run未启动的合法目标；不是每claim必须UI+CLI+截图+录屏+第二DB视图，也不强制四H2。未读 search.md不当已测。 |

这些是对已裁共同机制的支持与小增补，**不推翻 ABC/ABC2 的结论，不重开已关 finding**。MG5 的包内“无实质修正”只能当 A 自评；本 review 已独立指出哪些已覆盖、哪些限缩、哪种 source 原话不可升级。

## 合法下一动作与未读残余

Driver 可按以上落点安排互斥写面的作者定向蒸馏：MG1 repo reality，MG2 current-object comment triage/完整证据呈现，MG3 CI identity/flake 与 lockfile，MG4 最短启动/按需装配，MG5 只增 sink/entry-point/citation 等实际缺口。不需每组一新文件、完整装配平台、gate/validator、固定 runtime 或新的责任节点。已充分覆盖子机制只保贡献/source 关联，不叠正文或双计增量。B 固定对象另由 gate 核，不把本源裁定当产品 PASS。

未读：包列 code-quality-review、why investigator/sources、其余 orchestrate prompt/adapter、canvas 第二载体与资产、babysit 完整实现、feature-map search、metadata/CHANGELOG 的非承重尾部。它们不被称作全文/运行资格；将来扩相应主张或搬工具再补承重原文。尚未裁 ABC5–8、EF+addendum、A4 DEF/DEF2 保原队列；Oracle CD/THIRD-PARTY/DEF3 排除。本审核无源脚本、SDK、真实业务、冷读效果或收益实验，不派工、不写产品、不发布。review 由 Driver 保全提交。
