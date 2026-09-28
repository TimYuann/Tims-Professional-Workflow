# Round 1 · 独立验证报告（冻结工作树）

对象是**未提交的工作树**，不是 HEAD diff。冻结范围 9 个 `roles/*.md` + `pipeline.md`、`closure.md`、`SOURCES.md`、`README.md`、`AGENTS.md`、`VERSION`、3 个指定脚本/模板，合计 18 个文件。仓根 `/Users/yuantian/Developer/tim-professional-workflow`，`git rev-parse HEAD` = `52d3315d881cdff9f42d52c2db0eb2796b4fa44e`，Python `3.14.4`。启动验证与写本报告前按 Arbiter 给定的 18 文件算法分别复算：**两次都是 `18 86dc6d75872f63d9ae97f17db86b9f40a4bfab697f949b0ae39618b35682189e`**。下述判断在未读 `.pi/round1/REVIEW-1.md` 和 `.pi/round1/REPORT.md` 的情况下定稿。

## 1. 结论（三态，只许选一个）

**FAIL**。检查有效执行，产物存在硬约束冲突、跳过路径断档和错误的等价证明；机械 checker 的 14/14 不能改变这些事实。非环境故障，因此不选 UNVERIFIED。

## 2. 我实际执行了什么

- `pwd; git rev-parse HEAD; git status --short; python3 --version`：退出码 0。仓根与基线见报告首段；工作树有已暂存的 `skills/`、`workflows/` → `docs/archive/` 移动及未暂存/未跟踪改动；没有误以 HEAD diff 是全对象。
- `git -C upstreams/{cursor-plugins,mattpocock-skills,addyosmani-agent-skills} rev-parse HEAD`：退出码均 0；依次为 `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`、`c55ee46073ed923f86ce59a5eb3b6d895095d1b7`、`2686b620fc1fed2e8f60c704839c766b8594c6b6`，与 `SOURCES.md:7-13` 相符。
- 我亲自运行 `python3 scripts/check-library.py; rc=$?; printf 'EXIT=%s\n' "$rc"`，退出码 **0**；下面是原样 stdout（含扫描/排除声明，目录路径保留）：

```text
TIM · check-library.py（只读自检）
扫描范围: roles , scripts , pipeline.md , closure.md , README.md , AGENTS.md , SOURCES.md , VERSION
显式排除: docs/**（历史材料与归档） ; .pi/**（工作区） ; upstreams/**（只读克隆，按路径豁免） ; 上游仓库名 cursor-plugins / mattpocock-skills / addyosmani-agent-skills / pi-review / superpowers / gstack / humanlayer（溯源标识，非本库依赖或悬停） ; scripts/check-library.py 自身（含 harness token 清单与判定字样，按定义自排除）
本检查能判: 结构与字段级闭环、引用与死链、版本单一来源、底座解耦的措辞、能力探测块的位置与集中度
本检查判不了: §4 方法的实质深度、语义正确性、字段值是否真实、某次跳过是否真的合规——这些交给独立审查与人审
仓库根:   /Users/yuantian/Developer/tim-professional-workflow
------------------------------------------------------------------------
[PASS] 角色文件集合                                 缺 无；多 无
[PASS] 角色 frontmatter + 8 节                   9/9
[PASS] 注入契约声明                                 9/9
[PASS] §4 反例/不适用 ≥2                           9/9
[PASS] §8 常见自欺 ≤4                             9/9
[PASS] 角色文件引用仅限 roles/                        通过
[PASS] 闭环：收据字段 ⊆ 产出方字段                        全部成立｜收据 25/25、产出 11/11 参与校验
[PASS] 闭环：交接拓扑双向一致                            全部一致
[PASS] 闭环矩阵 ↔ 角色文件交叉校验                        主链 9 行 + 按需 2 行，逐行与角色文件交叉校验 全部成立
[PASS] 死链检查                                   无死链
[PASS] 版本单一来源 VERSION                         VERSION=1.0.0，扫描范围内无第二处声明
[PASS] 工具解耦：无具体 harness 名称                    0 命中
[PASS] 工具解耦：能力探测块恰好一处且在 driver.md             命中 roles/driver.md:109（4/4 项）
[PASS] 工具解耦：其他角色文件无能力枚举                       0 命中
------------------------------------------------------------------------
合计: 14 项通过 / 0 项失败 / 14 项检查
EXIT=0
```

- 反实现挑战 1：用 Python 临时目录复制 `roles/`、`scripts/` 及 6 个根文件，**只在副本**把 `roles/investigator.md` §4 替换成“触发条件：有任务。步骤 1：努力完成。判断依据：大致正确。反例：不适用。反例：不适用。”，`docs/`、`upstreams/` 指向原只读路径以保持正常引用可解析；运行副本 `check-library.py`，**EXIT=0 / 14 PASS / 0 FAIL，§4 反例/不适用 ≥2 显示 9/9**。程序承认不能判断方法深度，实际也确实不能；故主仓的结构 PASS 不能支持“工程经验装进角色”的语义结论。第一次只复制可发布件而没给 `docs/upstreams` 链时 `EXIT=1`（死链），这是**夹具缺陷**而非正例；已修夹具后独立重跑得上述假绿。
- 反实现挑战 2：同样仅在临时副本将 `closure.md` 主链九行**全部删除**、保留表头及按需表；副本 checker **EXIT=0 / 14 PASS / 0 FAIL**，其中原样判语为 `[PASS] 闭环矩阵 ↔ 角色文件交叉校验                        主链 0 行 + 按需 2 行，逐行与角色文件交叉校验 全部成立`。它没有守住主链不得为空这一最低覆盖前提。
- 自己用 Python 逐行解析 `closure.md` 主链行 0→8 的输入字段与前一行输出字段：**8/8 逐字子集，0 处缺失**；仅代表**未跳过**时的字段名包含。跳过调查时，`roles/architect.md` 主收据六字段中，`closure.md:24` 仅承诺自行补 `first_divergence`；至少还缺 `entry_point/root_cause/confidence/coverage`。跳过设计时，`roles/planner.md` 主收据五字段中，`closure.md:25` 承诺 `caller_usage` + 一个对照形状，至少还缺 `data_shapes/invariants/change_cost`。脚本打印 `0->1 ... 7->8 input_not_in_previous_output=[]`；这不是跳过路径通过的证据。
- 对 `roles/investigator.md`、`roles/reviewer.md`、`roles/oracle.md` 的 §4 逐触发/步骤/判断/反例做了来源核对：**N=208，忠实或 Owner 直接规定 M=191，不忠实/无合规三仓来源 K=17**；逐节分母和所有 K 的文件行号、上游原文及源映射见 `.pi/round1/VERIFY-CITATION-AUDIT.md`。本仓角色禁止直接写 upstream 路径，因而沿 `SOURCES.md` 的落点映射回跳逐行核对；没有把路径可解析当作意思忠实。另用 Python 检查台账三仓段 92 条明确 `skills/...:line` 引用：**一条越界** `SOURCES.md:82` 的 `skills/architect/SKILL.md:81-84`（原文共 83 行）；跨仓 matt 引用 3 条按显式“matt”标记转到 matt 根，能定位。
- 用临时独立代码反证 `roles/reviewer.md:56` 的“符号集合相同即等价”：原版 `def authorized(): return True`、新版 `return False`；真实执行打印 `same_symbols=True symbol_delta=[] same_behavior=False old=True new=False`，命令退出码 0。此规则不能作为免独立审查的充分证明。
- 9 角色接缝声明脚本（`python3 - <<'PY' ...`，退出码 0）：**9/9** 均含“第 1–2 层 / 第 3 层 / 第 4 层 / 附加内容不得改变本文件的纪律与方法边界”；能力探测原句只在 `roles/driver.md:109` **1** 次、其他角色 **0**。grep 检出的 `Cursor` 仅在仓名 `cursor-plugins` 的溯源语境（`AGENTS.md`/`SOURCES.md`/`sync-upstreams.sh`），不是调用该工具的指令；但 checker 自身含真实工具名，见 B-7。
- `scripts/log-decision.sh` 用临时 TSV 连跑两次：退出码 **0/0**，3 行=1 表头+2 决策、公式 `=SUM(...)` 被前导 `'` 转义、带换行的参数保持六列单行，第二行仍在。`scripts/check-team-version.sh` 用临时绑定文件实测：匹配版本 **0**、漂移 **2**、无法解析版本 **3**、文件不存在 **1**；无写入下游项目。
- `README.md` 68 行（≤80）、`pipeline.md` 150 行（≤150）；`docs/archive/` 保留了旧技能与三个旧流程，没有对其写入。`VERSION` 唯一真实值为 `1.0.0`。
- **未执行**：没有部署或运行一个真实消费方 app；本轮目标是审方法库，且只读下游、不具一个被授权的运行候选/凭据。没有用任何真实产品通过读数代替这个缺口；不运行 `sync-upstreams.sh`（它会写只读 clone），不 commit，不读用户禁止提前阅读的两份评审/自述直至本报告独立结论定稿。

## 3. 阻断项（Blocking）

1. **B-1 · solo 归并让 Driver 亲自实现。** `pipeline.md:40` 定义“单会话顺序兼任 Driver / … / Implementer”；同文件 `:49` 明定“Driver 不实现”，`roles/driver.md:12` 也说“不做实现、审查、验证”。此外任务卡 §2 第 3 条要求 Driver 独立 session、不被执行上下文污染。**为什么阻断**：一个人按官方 solo 装配会同时履行被禁止的两个职责，即使另起 fresh Reviewer 仍不满足 Driver 边界。**最小方向**：不要把 Driver 与 Implementer 放到同一会话；若物理上只开得起作者+判断两会话，应明确谁履行 Driver 独立编排以及不可兼任的条件，否则如实标当前档位不可用。
2. **B-2 · 跳过环节时只移交“职责”没移交完整“收据”。** `closure.md:24-30`：跳调查→Architect 只填 `first_divergence`，但 `roles/architect.md:16-25` 仍要求 `investigation-report` 六字段；跳设计→Planner 只补用法和一种对照形状，`roles/planner.md:16-24` 仍要求完整 `design-proposal` 五字段，`roles/implementer.md:26-27` 也要来自 Architect 的三字段；跳独立审查→Verifier 只补反实现挑战，`roles/verifier.md:25-26` 仍要求 `review-verdict.object/blocking/coverage`；跳验证→Integrator 只核身份，`roles/integrator.md:16-25` 仍要求 `verification-evidence` 六字段；跳集成→Driver 没收到 `integrated-baseline`（`roles/driver.md:32-33`）。**为什么阻断**：至少五条被文档明示允许的路径，下一环按自身 §2 会拒收；主链不跳时 8/8 字面吻合掩盖了这个断档。**最小方向**：逐路径规定替代交接物**完整字段与产出角色**，或把接收契约明确写成可走的其他输入而不是仅填职责；没有替代物的环节不得标“可跳过”。
3. **B-3 · 独立审查的机械等价证明会假放行。** `roles/reviewer.md:54-59` 与 `closure.md:28` 允许“重命名/搬文件仅比较符号集合”作为跳过 Reviewer 的证据；相同符号集合可包含不同函数实现（本报告的执行反例 `True`→`False` 已展示）。**为什么阻断**：契约把非等价候选纳入“可免独立审查”，独立判断要求遭形式规避。**最小方向**：等价判据必须能比较真正承诺的不变行为/语义或同一文件搬迁的内容；无法证明时不允许跳过。
4. **B-4 · Planner 擅自新增数字门禁。** `roles/planner.md:114,187` 规定没有已有数字时“取当前实测值并规定不得回退”；`SOURCES.md:292` 也列“当前实测基线”为第三个合法数字来源。任务卡 D3 的 Owner 收紧原话：指标只能来自 Owner 要求或既有契约，执行者不能发明。**为什么阻断**：测到一次值是事实，设“不得回退”是新增授权外阈值，尤其噪声指标会变成隐性误拦。**最小方向**：无授权阈值时只报告测量与不确定性，提出阈值待 Owner 或既有契约确认，不把测得值自动升级为强制门禁。
5. **B-5 · 来源台账、实际角色方法与冲突裁决不一致。** `SOURCES.md:168` 声称保留 matt TDD“重构不属于红绿循环”，但 `roles/implementer.md:69-77` 明确强制“红—绿—重构”；addy 的 `test-driven-development/SKILL.md:38-95` 恰为红绿重构，冲突表 `SOURCES.md:296-305` 却拿 matt 与并不规定生产 diff 的 pstack `prove-it-works` 制造“生产代码必须改”的假冲突，漏裁真正冲突。`SOURCES.md:42,312-315` 称调查结尾保留 Preserve/Change/Avoid/Risk 约束集，实际 `roles/investigator.md:28-38,151-165` 无此字段/动作。`SOURCES.md:259-261` 对注释方案明写取“甲方处置程序+乙方保留标准”，并未单选；角色实现处也没落地相应注释条件。`SOURCES.md:82` 尚有越界 `file:line`。详见来源底账 17/208 异常。**为什么阻断**：D1/D3 的逐方法可追、冲突单选和深度吸收没有兑现；一条引文“附近有关”不足以背书相反行为。**最小方向**：按真实差异单选（尤其 TDD、注释），对每个来源声明保留/主动改写/不采纳，并同步到角色 §4 和可交字段；修正越界引用，不再将不存在的规则算为已吸收。
6. **B-6 · checker 在空主链时仍报闭环 PASS。** `scripts/check-library.py:362-418` 对相邻行执行了循环，但未断言主链行数、唯一性和非空字段；独立临时副本移除全部九行仍得 **EXIT=0，主链 0 行 / PASS**。**为什么阻断**：D4 明令 checker 机械验证矩阵闭环；连矩阵消失都能通过，当前 14/14 不能作为机器证明。**最小方向**：空/缺行/重复行/字段空直接失败，保持原本 9 行的相邻/跨角色核验。
7. **B-7 · 自行扩大工具扫描豁免。** `.pi/round1/TASK.md §5` 允许排除 `docs/**`、`.pi/**`、`upstreams/**`；其余本库可发布件包括 `scripts/**`。`scripts/check-library.py:27-45,62-68,468-473` 却额外声明并实行 **整个 `scripts/check-library.py` 自排除**，而该可发布脚本本身列出具体底座/模型工具名。**为什么阻断**：Owner 已给精确扫描边界，程序自行把自己移出边界，零命中并不等于按批准范围零命中。**最小方向**：向 Owner 明示申请并记录例外，或改用不在自检脚本正文出现工具名的规则表示，确保全部发布件纳入扫描。

## 4. 非阻断项

- **N-1 · 台账来源数量算术表述不一致。** `SOURCES.md:3` 写“Owner 口径 6 个来源（3 clone + 4 位外部作者）”，3+4 实为 7。Owner 自身文书也有此口径；本表确实如实列了三仓和四个 NOT ABSORBED，不把命名错误单独阻断。
- **N-2 · 单注入测试（Reviewer）有可观察缺口。** 只给 `roles/reviewer.md`、不补 Driver 的第 3/4 层：如果输入方实际交齐其 §2 三收据（candidate、slice-plan、design-proposal），能按 §4 启动并交 §3 五字段；但 `roles/reviewer.md:16-31` 不要求冻结的 `owner-brief`/`task-card` 原始目标与授权。若 `slice-plan.verification/scope` 自身误译 Owner 验收口径，Reviewer 按 §4.2“只看契约”只能复核二手契约，不能察觉偏离原始授权。建议在输入处注明由谁提供冻结原契约或明确不覆盖原始意图，这不等同于它不能审一个已冻结的 slice-plan。
- **N-3 · 真消费方映射（事实、非阻断）**：只读 `/Users/yuantian/Developer/ekunai/Unified-Customs-Bonded-Intelligence-Platform/docs/active/engineering-method-routing.md:21-27` 对照：`path-trace` → `roles/investigator.md §4.1/4.3` 的红回路+第一次失真；`blast-radius` → `roles/reviewer.md §4.3` 影响面和 `roles/verifier.md §4.3` 承重事实+证明档位；`design-compare` → `roles/architect.md §3/§4.4-4.6` 调用者用法、两个结构不同候选、“不重构”、红旗及下次改动成本；`drive-preview` → `roles/verifier.md §4.1-4.2` 的环境断言/真实入口/运行输出**仅部分**，没有显式 Launch/Doctor/Drive/Evidence/Cleanup 五段记录。消费方契约本轮只供映射，不当作额外阻断门。
- **N-4 · 无 `upstreams/**` 修改、无对 ekunai 写入、无 commit**。脚本输出可以复跑，但未对真实运行中的消费者做集成/发布测试，不把这点伪装成已验证。

## 5. 我的核验边界（这条不许省）

- 覆盖：冻结 18 件两次哈希核对；9 角色完整阅读；22 个被抽角色的 §4 方法段（按触发/编号步/判断/例外合计 208 单元）；三仓相应上游与来源落点；两类脚本真实运行；主链静态字段；全部文档明示跳过路径；README/AGENTS/archive/版本；下游方法路由**只读事实映射**。
- 未覆盖：上游仓库全部技能逐文件全文阅读（只读台账关联的有关源段）；没有真实业务项目端到端运行、网络/发布检查、外部账号/浏览器状态。92 条台账显式文件行锚的存在性扫描只覆盖显式完整路径，`同上 :line` 另按相关篇章人工比对；源码能定位不代表论证忠实。角色 §4 的“复合步骤”按一单元计，因此 N/M/K 不是自然语言每一个从句的穷尽统计。无环境故障掩盖已确认的阻断项。
- 判据可能失效处：用静态文档推理跳过路径，未实际发出 9 角色的整套交接包；临时反例测试的是 **checker/等价判据的逻辑**，不是某真实产品的 BUG；`SOURCES.md` 回引有的只是节级落点而非角色逐句引用。即便消除 B-1 至 B-7，仍应跑一轮带冻结身份和实际交接收据的冷启动任务。

## 6. 与需求对照

| Owner `.pi/round1/TASK.md §2` 的 7 条核心标准（加上 §2.1/§5 判线） | 判定与依据 |
|---|---|
| 1 方法 > 流程 | **部分**：`pipeline.md` 150 行，方法主体在 9 角色；但 reviewer 方法有错误等价判据，部分仍为无三仓来源清单，见 B-3/B-5。 |
| 2 经验装进角色，不放 skill | **满足**：`skills/` 原载体进 `docs/archive/skills/`，9 个角色各有实质 §4。 |
| 3 Driver 独立、只编排 | **不满足**：`pipeline.md:40` 让它在 solo 中兼 Implementer，对上 `:49` 与 Owner 禁令，B-1。 |
| 4 完全解耦，脚本可用 | **部分**：角色不发具体运行命令，9/9 注入接缝；`check-library.py` 擅自额外豁免自己，B-7。 |
| 5 厚薄可缩放且实现者 ≠ 判断者 | **部分**：trio/full 分配能隔离 Implementer；solo 为作者侧1+fresh Reviewer，不自评但 Driver 兼任问题仍在；无独立会话时写明 UNVERIFIED。 |
| 6 自洽无断档、无死引用、单一版本 | **不满足**：常规相邻字段 8/8，`VERSION=1.0.0`，但跳过路径断档和台账越界 `file:line`，B-2/B-5/B-6。 |
| 7 上一环实际交出下一环所需字段 | **不满足**：不跳过能对齐，跳调查/设计/审查/验证/集成均无完整替代收据，B-2。 |
| 附加：三仓深吸收并逐条裁决冲突；只允许 Driver 能力探测 | **部分/不满足**：三仓 SHA 与多份机制确已对应，208 单元 17 异常，TDD/注释裁决未真单选、且自动设数字门禁越权；Driver 探测只 1 处，其余角色 0，但 checker 自排除发布脚本，B-4/B-5/B-7。 |

独立结论至此定稿。后续如读 Arbiter 的 `REVIEW-1.md` 与交付方 `REPORT.md`，只追加**对照记录**，不倒改本报告既有结论或计数。

## 7. 定稿后才读的交叉对照（不改变上述判定）

- **我独立发现、先前两份未列作已知阻断**：B-1 solo 的 Driver/Implementer 自撞；B-2 五条跳过路径的完整收据断档；B-4 “实测基线自动变门禁”的授权越界；B-5 真正的 matt/addy TDD 冲突与 `why` 约束集没有落点；B-6 主链删光仍 PASS；B-7 checker 自排除未获任务卡 §5 明示批准。
- **与 `.pi/round1/REVIEW-1.md` 重合但结论更具体**：旧评审 B3 曾要求给机械等价“一条可重复执行的命令与输出”，还把“符号集合不变”列作例子。我的 B-3 实际跑出**符号集合不变但行为不同**；命令可重复也仍可能测错性质，这一层不在旧评审的验证范围内。旧评审 B1/B2 关于散文式收据、矩阵交叉校验均是**返修前**的问题，当前 checker 已分别补解析、覆盖率与交叉校验；不重复报旧问题。旧评审 N2 关于 §4 空话能 PASS，当前 checker 已披露这一能力边界，故我只记录假绿、并未单独把“机器不能读懂方法”定为阻断项。
- **与 `.pi/round1/REPORT.md` 自述不符的部分**：交付方 §1/§5 自称九条冲突均“单选”，但 `SOURCES.md:259-261` 直写取甲处置 + 乙保留且角色落点不足；§2.6 B3 自称机械等价已定义，我的实际反例证实**定义有缺陷**；§6.1 称 Reviewer 剩下的只是“命令选得对不对”，而给定的**标准命令类别本身**就不够证等价；§6.3 将跳过问题描述为“机器不能校验跳过条件”，没有处理**即使按文档合规跳过，下一环仍无完整收据**的 B-2。其 §4.2 自报 Oracle 争议需要经 Driver 转手、可能被漏判是一个我未先发现的额外风险：`roles/architect.md:189-192`、`roles/reviewer.md:185-188` 说“发 pending-question 给 Oracle”，而 `roles/oracle.md:16` 只收 Driver 的来件，`pipeline.md:147` 只有 Driver→Oracle；应在返修时具体决定由谁构造该卡，不能把自述当独立证据。
