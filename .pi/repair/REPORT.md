# core 闭环 repair 实施报告

**状态**：9 项改动（R1–R9）全部落盘；D1–D4 均按 Owner 裁定（2026-09-26 两条 intercom 消息）实现；**未 commit**；工作树保持可 `git diff` 状态。
**执行者**：本轮唯一执行者（subagent-chat-01a0dd53）。**本报告是执行者自证，不是独立复验**——语义层的复验按计划留给独立会话（见 §6 残留）。

前置事实：

- HEAD 未动：`52d3315 chore: sanitize absolute file paths to relative markdown links`（`git log --oneline -1`）。
- 他人的改动保留：`docs/**`（含 Owner 未跟踪的 `REVIEW_R2.md`）与 `upstreams/**` 的 pre/post 状态逐字节一致；`.pi/**` 只新增本任务自己的 `repair/**`。
- 我改动的文件（content hash 与事前不同）：`AGENTS.md`、`README.md`、`pipeline.md`、`SOURCES.md`、`roles/*.md`（10 份全部）、`scripts/check-library.py`、删除了 `scripts/check-team-version.sh`。未改：`closure.md`、`identity.md`、`scripts/{ws-identity.sh,identity-selftest.sh,log-decision.sh,sync-upstreams.sh,render-ledger.py,decision-log-template.tsv}`。
- `docs/TIM-PROFESSIONAL-WORKFLOW-PROPOSAL.md:260` 与 `docs/…REVIEW_R2.md:347` 仍引用已删脚本：那是历史材料，计划明令不得动 `docs/**`，未清（见 §6 残留 R-3）。
- 证据目录：`.pi/repair/evidence/`、验收夹具：`.pi/repair/acceptance/`。

---

## 1. 每条改动落在哪（①）

行号取本报告生成时的工作树。`SOURCES.md` 的行号在生成区重新渲染后可能再移动，以锚点文本为准。

| # | 改哪里 | 落点（file:line） | 关键文本 |
|---|---|---|---|
| **R1** | Driver 推进前说明 | `roles/driver.md:262`（§4.9 新增）；`roles/driver.md:153`（§4.1 第 6 步交叉提示）；`pipeline.md:127`（§10 一行） | 硬线唯一：**跨过「开始实现」这条线之前，说明必须已送达**；"一批任务首次派出 / 写窗开放 / 目标·范围·风险实质变化"降为**时机提示**；送达≠批准；发送失败不得写"已说明"，也不得开工 |
| **R2** | 十角色收件四步 + 权威位置 | `AGENTS.md:23`（原则 8）；§2 首行：`roles/driver.md:16`、`oracle.md:16`、`investigator.md:16`、`architect.md:16`、`planner.md:16`、`implementer.md:16`、`reviewer.md:16`、`verifier.md:16`、`integrator.md:16`、`ledger-custodian.md:24`；verifier 专句 `roles/verifier.md:18`；矛盾处置替换 18 处（原"要不到就按最小范围处理并写明"→"停止受影响的写入与通过判断，点名缺什么、谁应补"）；登记表 `SOURCES.md:476`（§9） | 清点 → 核对 → 缺则退回 → 齐则开工；不把"发件人说有"当作"现场确有"；Verifier 专句：本轮任务必须说明运行目标及期望环境，"未声明就绪"≠"就绪"，建不起来记 `UNVERIFIED` 并交 Driver 一张解除阻塞任务 |
| **R3** | 谁修环境 / 怎么评价自建台 | `roles/verifier.md:46`（§3 `environment` 含义列）、`:47`（`commands`）、`:49`（`falsification`）、`:51`（`uncovered`）、`:86`（§4.1 自建前提段）、`:237`（§6 行）；`roles/driver.md:171`（§4.2 第 5 步）、`:311`（§6 行）；`roles/investigator.md:204`（§6 行） | 装置来源（复用/临时自建）、坏条件能让 doctor 报红、真实入口、是否清理；自检红一例不足以自判装置普遍可靠；进仓/共享数据/唯一放行闸→Driver 发卡给有写权者；改运行配置/种子/版本要重估旧证据环境等价性；doctor 绿≠原缺陷已修 |
| **R4** | 意外失败入口 + 阻断出口 + 防复发 | `roles/investigator.md:54`（§4.1 第 0 步）、`:59`（第 5 步尾）、`:213`（§7 阻断交付）、`:217`（不算做完加一条）；`roles/implementer.md:171`（§4.5 第 6 步） | 先停当前改动、保全脱敏原文、五面分诊（测试本身/产品代码/构建配置/外部依赖/数据共享状态）；建不出回路→具名阻塞，不输出已证实根因；不产字段缺失的正式 `investigation-report`、不派空 `repro_command`、不得记诊断 `PASS`；回归保护不得用浅测试冒充 |
| **R5** | bugfix 红→绿独立复现 | `roles/verifier.md:33`（§2 副收据，仅报告过的 bugfix）、`:98`（§4.2 第 6 步）、`:186`（§4.6 不适用项）、`:243`（§7）；`roles/reviewer.md:179`（§4.5 判断依据） | 旧基线实际对应 → 候选变绿 → 重走未最小化原场景；旧环境不可用**不伪造一次「亲眼看红」**，证明不了进 `uncovered`；新功能/纯静态不硬造历史红灯；反实现挑战是判据证伪，不是再写一轮实现 |
| **R6** | 术语冲突与裁定权（D3） | `roles/architect.md:201`（§4.9 新增）、`:209`（裁定权）；`roles/investigator.md:95`（§4.3 第 7 步）；`roles/reviewer.md:141`（§4.3 第 5 步）；`roles/planner.md:107`（§4.4 第 5 步）；`roles/implementer.md:99`（§4.1 第 5 步）；`roles/driver.md:310`（§6 行）；`SOURCES.md:179` | 裁定权＝项目 Owner 本人或 Owner 书面指定/明确授权的业务角色；**没有这样的角色可问 → 挂起待裁**，工程侧不得擅自决定；Architect 职责只到查证/备选/记录；新建词汇表需 Owner 同意且先映射既有权威文档 |
| **R7** | 性能症状与三段交接 | `roles/investigator.md:177`（§4.8 新增）、`:215`（§7 性能结论边界）；`roles/verifier.md:158-160`（§4.5 第 6–8 步）；`roles/implementer.md:152`（§4.4 第 7 步）、`:190`（§4.6 第 6 步）；`SOURCES.md:241` | 改动前固定输入取重复基线并标噪声；按症状选测量对象；无有效基线→§4.1 第 5 步阻断；同条件复测、无授权阈值不得自设门；一次只改一个因素、回退＝新候选+新冻结；记录保留与放弃尝试 |
| **R8** | 权威位置 / 轮次 / 数字（D2） | `AGENTS.md:23`（原则 8，与 R2 同一处）；`roles/reviewer.md:217`（§4.7 判断依据，两轮硬规定）；`roles/driver.md:212`（§4.5 改为路由）；`roles/planner.md:162`（§4.7 第 4 步）、`:125`（§4.5 第 6 步）、`:88`（§4.3 第 1 步）、`:174`（§5）；`pipeline.md:95`（§7 两事件表）；`roles/architect.md:164`（§4.6 判断依据）；`roles/investigator.md:152`（§4.6 第 6 步）；`SOURCES.md:373`（§4.10 #17） | 决定者/权威位置/写者分别点名；生成的视图不得手工维护；**两轮是本库硬规定，不得被装配参数覆盖或放宽**；同前提重复失败由 Investigator 归因，Driver/Planner 只路由；文件数与 `change_cost` 不是准入门；测量值不自动升级为门 |
| **R9** | 版本核验与自检边界（D4） | `AGENTS.md:59`（纪律 2）、`:63`（纪律 6）、目录树删除脚本行；`README.md:57-59`（目录）、`:72-74`（自检判不了 + 保留判据）；`SOURCES.md:472`（§8）；`scripts/check-library.py:32` 与运行输出行（同义重复须人审）；**删除 `scripts/check-team-version.sh`** | 本库当前不提供漂移检测；下游按固定 commit、checkout 必须干净、实际读取对象与 pinned commit 一致；checker 只兜结构与确定性回归，不是工作流 PASS，某次交接由收件人按 §2 核实 |

计划里"不新增"的硬约束遵守：未新增收据类型、角色、状态机或通用 packet validator；R2–R9 全部落在既有 `task-card / investigation-report / candidate / review-verdict / verification-evidence` 交付物上（`check-library.py` 报"收据 30/30"闭环成立）。

---

## 2. 验收情景：原样命令与原样输出（②）

### 2.1 A 批两条截断情景（消息点名）

```console
$ python3 .pi/repair/acceptance/a_scenarios.py 2>&1 | tee .pi/repair/evidence/a-scenarios.txt
A 批验收（规则提取自角色文件现场文本；ROOT=/Users/yuantian/Developer/tim-professional-workflow）
[情景 A-1] 任务声称有 slice-plan 却没交 → 实现者必须停止开工、零写入并点名缺件
  [PASS] 存在「停止开工/零写入」规则 :: 6 行
  [PASS] 存在「点名缺什么、谁应补」规则 :: 6 行
  [PASS] 存在「唯一合法动作是停止」规则 :: 1 行
  [PASS] 已无「要不到就按最小范围处理」矛盾处置 :: 0 残留
  - slice-plan 与收件四步
      命中规则: | `slices` | ... | **停止开工**：把缺件写成请求交 `roles/driver.md` 请它合法代产（或转 `roles/planner.md`）；拿到完整 `slice-plan` 之前**零写入** |
      命中规则: | `scope` | ... | **停止开工**；不得用「按最小范围处理」这类自解释代替写入范围白名单 |
      命中规则: 5. 停止期间**零写入**：不写测试、不写产品代码、不写「我假设……」的推导记录。

[情景 A-2] 任务写「服务已就绪」但现场找不到正确实例 → 验证者必须给 UNVERIFIED + 缺什么 + 交 Driver，不得借旧材料发 PASS
  [PASS] 任务须声明运行目标与期望环境 :: 1 行
  [PASS] 「未声明就绪」≠「就绪」 :: 1 行
  [PASS] 缺目标/授权向 Driver 要 :: 1 行
  [PASS] 建不起来记 UNVERIFIED :: 1 行
  [PASS] 不给产品代码判 FAIL/PASS :: 1 行
  [PASS] 环境不满足不得改写成通过（§4.2 第 5 步） :: 1 行
  [PASS] 不把发件人说法当现场事实（收件四步） :: 1 行
  - 验证者收件与三态
      命中规则: **本轮任务必须说明运行目标及期望环境**（实例/版本、权限、数据、入口）；"未声明就绪"不等于"就绪"。先在现场核对；缺目标或授权向 `roles/driver.md` 要，不得擅自选实例。环境未就绪但临时装置在本卡授权内时，可按 §4.1/§4.2 自建，交付时披露；建不起来则记 `UNVERIFIED`，并明确交 `roles/driver.md` 一张解除阻塞的任务——不给产品代码判 `FAIL`/`PASS`。
      命中规则: 5. 环境与资源不满足就记"未运行"或"运行无效"，不要改写成通过。

A 批验收结论: 全部通过
EXIT=0
```

### 2.2 B/C/D 批与交叉情景

```console
$ python3 .pi/repair/acceptance/bc_scenarios.py > .pi/repair/evidence/bc-scenarios.txt 2>&1; echo "EXIT=$?"
EXIT=0
```
逐情景汇总（完整逐条输出见 `.pi/repair/evidence/bc-scenarios.txt`，共 **103 条 PASS / 0 FAIL**）：

```
[R1] 跨过「开始实现」前必须对齐；说明≠批准；送达失败不得写「已说明」                 PASS=9  FAIL=0
[R3] 环境阻塞按类分流；Verifier 自建前提要披露；doctor 绿≠原缺陷已修                PASS=10 FAIL=0
[R4] 意外失败先停/保全证据/分诊；建不出回路具名阻断；回归保护不留浅测试              PASS=9  FAIL=0
[R5] bugfix 旧基线红→绿独立复现；取不到旧环境不伪造；Reviewer 不是实现循环          PASS=8  FAIL=0
[R6] 术语裁定权归业务侧（Owner 裁定）；无授权角色则挂起；Architect 只查证/备选/记录  PASS=12 FAIL=0
[R7] 性能症状：改动前基线→定位→单因素改动→同条件复测→无对照只报未测出              PASS=10 FAIL=0
[R8] 一条权威规则 + 内联登记；两轮硬规定；停手条件按角色自守；估算不是门             PASS=18 FAIL=0
[R9/D4] 删除失真脚本并如实声明；固定 commit + 干净 checkout；checker 不是工作流 PASS PASS=15 FAIL=0
[交叉] R2-③ / R3-② / R8 单文件自包含 / R9 收件人门                              PASS=12 FAIL=0
B/C/D 批验收结论: 全部通过
```

计划逐条"如何验收"与本验收的对应：

| # | 计划要求的情景 | 验收证据 |
|---|---|---|
| R1 | 已授权单文件卡：发卡前 Owner 收到具体说明、不等待第二次批准；权限未定卡：先停并请 Owner 定 | bc `[R1]` 9 条：`时机提示，不是同等强制点`、`唯一不可让的硬线：跨过「开始实现」…`、`不把收到说明误当批准`、`发送失败或无法确认送达时不得写`；交叉段 `拿一条自己写的记录充作 Owner 已收到` 必须触发禁令 |
| R2 | ①缺 slice-plan→零写入点名；②"服务已就绪"→UNVERIFIED+缺什么+交 Driver；③资源就绪仍核对实例，不看 ready 标签 | A-1、A-2；交叉段 `把环境事实从"记录"升级为"断言"`、`进程启动时间必须晚于候选生成时间`、`写入隔离与实际加载来源一致`、`这些条件不成立就先报协调方，不开始验证` |
| R3 | 缺种子数据→UNVERIFIED→Driver 发环境修复卡→修后重核身份/条件并重跑原目标；临时装置加载旧构建必须拒判 PASS | `[R3]` 10 条（含 `doctor 绿不等于原缺陷已修`、`重估旧证据的环境等价性并重新跑原主张`、`我自建的前提要进仓`）+ 交叉段旧构建断言 |
| R4 | 三因先留原始读数再区分；缺环境则 UNVERIFIED/阻断；错误测试作为对照先判测试自身 | `[R4]` 9 条（含五面分诊、具名阻塞、阻断不等于 PASS、浅测试不得冒充防复发） |
| R5 | 旧版本真红/候选绿且原入口恢复；无法取旧环境→降结论；纯新功能不被错误阻断 | `[R5]` 8 条（含 `不伪造一次「亲眼看红」`、`新功能 / 纯静态改动不强求历史基线红`、`判据证伪，不是再写一轮产品实现`） |
| R6 | 同一词两义→先映射既有位置、提交边界用例、裁定前依赖项不进实现、选定后只更新既有事实源 | `[R6]` 12 条（Owner D3 后的裁定权/挂起/查证备选记录/新建需同意/先映射；另一会话不得造第二份词汇文档） |
| R7 | 原样负载量基线→定位资源等待→一处改动→同条件复测；噪声内不给 PASS；缺测量环境回 R3 | `[R7]` 10 条（含 `没有授权阈值不得自设门`、`记录保留与放弃的尝试及其读数`、绩效回退=新候选+新冻结） |
| R8 | 单注入 Reviewer 也能守停手；第三次同前提补丁被拒且换前提不被误计；`change_cost=5–8` 可讨论拆片但不能得出 FAIL | `[R8]` 18 条 + 交叉段 `reviewer §4.7 单文件自包含：不引用 pipeline.md`、自带升级去向/硬上限/不重置 |
| R9 | AGENTS/README/SOURCES 不再把已删脚本说成能力；同 VERSION 但脏 checkout 不得宣称一致；固定 commit+干净入口才可说明内容来源；普通项目缺字段收据即使 checker 绿仍退回 | `[R9/D4]` 15 条（`本库当前不提供漂移检测脚本`、`按固定 commit 引用`、`checkout 必须干净`、`不自动锁执行中实际读取的工作区`、`不是角色工作流的 PASS，也不检验某次交接物的真实值`）+ 交叉段收件人门 |

### 2.3 库级收口（⑤）

```console
$ python3 scripts/render-ledger.py --check
render-ledger --check: OK（222 个 key，生成区与重新生成的结果逐字一致）
EXIT=0

$ python3 scripts/check-library.py
完整输出：.pi/repair/evidence/check-library-final.txt（与前次同结构，输出行已含"同义重复"）
最终：26 项通过 / 0 项失败 / 26 项检查
EXIT=0
```

逐项（原样）：

```
[PASS] 角色文件集合 / 角色 frontmatter + 8 节 / 注入契约声明 / §4 反例·不适用 ≥2 / §8 常见自欺 ≤4
[PASS] 角色文件引用仅限 roles/
[PASS] 闭环：收据字段 ⊆ 产出方字段        全部成立｜收据 30/30、产出 19/19 参与校验
[PASS] 闭环：交接拓扑双向一致
[PASS] 收据处置 G4：缺了怎么办非空
[PASS] 闭环矩阵 G3 / 相邻 + 角色交叉      主链 9 行 + 按需 4 行
[PASS] 可跳过路径 G5 / 死链检查 / 版本单一来源 VERSION / 工具解耦三项
[PASS] 身份规范 G1 / 身份实现 G2（15 通过 / 0 失败）/ 开工门 B-6 / G5′ / G7 / G6 / G8
[PASS] 台账落点 P5′（222 个 key 一致）/ P5（7 条带节号的落点声明全部存在）
合计: 26 项通过 / 0 项失败 / 26 项检查   EXIT=0
```

关键回归点：删除脚本后**无死链**、`check-team-version` 在扫描范围内**零引用**（除 SOURCES §8 的"已删除"记录本身）；`render-ledger` 在新 key 下 222/222 一致。

---

## 3. 未做项与 D 节待裁项（③）

- **D1–D4 全部已裁并已落盘**：D1（唯一硬线＝开始实现前对齐，其余为时机提示）、D2（两轮＋同前提两次失败为硬规定，不得被装配参数覆盖/放宽）、D3（裁定权归项目 Owner 或 Owner 授权业务角色，无角色则挂起；Architect 只查证/备选/记录；新建词汇表需同意＋先映射）、D4（删脚本＋声明不提供漂移检测＋固定 commit＋checkout 干净＋清理引用）。
- **计划内无未做项**：R1–R9 的"改哪里"全部执行；R9 里"若一定要引用 `scripts/log-decision.sh` 须另获授权"——**未引用**，无需授权。
- 计划允许但未做的：未新增任何库级检查门（checker 仍 26 项）；未把检查接到真实项目交接（计划明确要求先证明能读真实交接物并获得 Owner 授权）。

---

## 4. 计划与现状冲突之处（④）

1. **R4 引用的上游文件当时未读未登记**：计划以 addy `debugging-and-error-recovery/SKILL.md:10,23-31,40-154,291-298` 为依据，但 `SOURCES.md` 把它标为 `[仅目录]`／NOT ABSORBED。处理：**读正文**，落盘改动后按 `AGENTS.md` 纪律 1 补登为"局部吸收（改写）"（`SOURCES.md:251`），并从 NOT ABSORBED 清单移除。**未改计划内容**。
2. **R8 的术语 `expand–contract` 不来自计划所引的 addy 文件**：该提法出自 matt `skills/engineering/to-tickets/SKILL.md:40`（当时同为 NOT ABSORBED）。处理：读正文→只吸收该句→按纪律补登（`SOURCES.md:180`）→从 NOT ABSORBED 移除。
3. **R3 引用的 `control-ui/SKILL.md` 不在 `pstack/` 下**：实际路径是 `upstreams/cursor-plugins/cursor-team-kit/skills/control-ui/SKILL.md`，且 `SOURCES.md` 此前完全没有 cursor-team-kit 的任何登记。处理：读正文→补登（`SOURCES.md:142`，用完整 `upstreams/...` 路径以便死链检查豁免）；同批把 pstack `create-verification-skill`（原标"删除（本轮）"）读正文后补登为局部吸收（`SOURCES.md:141`）。
4. **R1 引用的 pstack `figure-it-out` 当时标"未评估→删除（本轮）"**：D1 裁定后 R1 在范围内，处理：读正文（53 行）→补登局部吸收（`SOURCES.md:140`）→从删除清单移除。
5. **R1 引文行号有小幅偏移**：`interview-me/SKILL.md:94-115` 覆盖了 Step 4（`:94`），但"explicit yes"门在 `:113-126`（SOURCES 已登记 `:94-112` 与 `:113-123`），属可核实的近似引文，未影响落盘；仅记录。
6. **两处既存悬空重复行**：`roles/verifier.md` 在 `review-verdict` 收据后、`roles/implementer.md` 在 `investigation-report` 收据后，各有一条重复的"缺任一条…先向 `roles/driver.md` 要"行（前一版本编辑残留）。R2 要求替换矛盾处置，我按新措辞改写了两处**但未删除重复行**（不清理他人内容）；建议 Owner 授权在下轮清理。
7. **`docs/**` 仍引用已删脚本**（`docs/TIM-PROFESSIONAL-WORKFLOW-PROPOSAL.md:260`、`docs/TIM-PROFESSIONAL-WORKFLOW-PROPOSAL_REVIEW_R2.md:347`）：计划明令不动 `docs/**`，且该目录是历史材料而非"自有发布件"，故未清；checker 已显式排除该目录，不影响死链项。

---

## 5. 计划外但由纪律强制的补充

按 `AGENTS.md` 纪律 1（"吸纳前必须读正文——没读过正文不算吸收"）与纪律 7（"记录分歧与出处"），下列补充登记属于落盘改动的必要后果，不是扩大范围：

- `SOURCES.md:140-142`：figure-it-out / create-verification-skill / control-ui 三条新吸收。
- `SOURCES.md:179-181`：domain-modeling / to-tickets / writing-for-agents 三条新吸收，同时从 NOT ABSORBED 清单移除（`SOURCES.md:182`），修正"`[仅目录]` 却被当作已读全文"的状态。
- `SOURCES.md:251`：debugging-and-error-recovery 新吸收。
- `SOURCES.md:241`：性能五步由"不采纳（未落地）"改为"局部吸收（方法骨架分角色落地，具体工具表未吸收）"。
- `SOURCES.md:373`：§4.10 #17 按 D2 记录硬规定与来源撤回（不再以消费者契约背书）。
- `SOURCES.md:476`（§9 新增）：收件四步的权威位置 + 十处内联副本 + 维护者与同步规则（DG 计划要求的登记，非第二份正文）。
- `AGENTS.md:23` 原则 8 的内联副本纪律，是 R2 与 R8 的共同落点。

---

## 6. 残留与需要独立复验的部分

1. **本验收是规则层验收**：A/B/C/D 夹具从角色文件现场文本提取规则行并断言"该情景下会要求什么、有没有矛盾指令残留"。**真正的语义验收需要独立会话**（例如：真给一个冷启动 Implementer 一张缺 `slice-plan` 的卡、真给 Verifier 一张"服务已就绪"但实例不对的卡），按计划文末"完成上述情景仍需独立判断产物、权限、候选与运行环境，不能由实现者给自己验收"，本轮**不冒充**已做。
2. **未触碰下游项目**：`/Users/yuantian/Developer/ekunai/**` 只读未动；D4 的下游绑定协议留给下游负责人。
3. **`docs/**` 历史引用**：见 §4 第 7 条。
4. **重复悬空行**：见 §4 第 6 条。
5. **未 commit**：按要求保持工作树可 `git diff`。

---

## 7. 证据索引

| 文件 | 内容 |
|---|---|
| `.pi/repair/evidence/head.txt` | 事前 HEAD（未动） |
| `.pi/repair/evidence/pre-status.txt` / `post-status.txt` | 事前/事后 `git status --porcelain`（唯一差异：`M → D scripts/check-team-version.sh`） |
| `.pi/repair/evidence/pre-hashes.txt` / `post-hashes.txt` | 23 个文件的事前/事后 sha256 |
| `.pi/repair/evidence/pre-diffstat.txt` / `post-diffstat.txt` | 事前/事后 `git diff --stat` |
| `.pi/repair/evidence/a-scenarios.txt` | A 批两条截断情景的原样输出（EXIT=0） |
| `.pi/repair/evidence/bc-scenarios.txt` / `bc-summary.txt` | B/C/D 与交叉情景逐条输出（103 PASS / 0 FAIL）、逐情景汇总 |
| `.pi/repair/evidence/check-library-final.txt` | 最终 `check-library.py` 输出 + `render-ledger --check` 输出（均 EXIT=0） |
| `.pi/repair/evidence/anchors.txt` / `report-anchors.txt` | 每条改动的 file:line 锚点清单（后者为报告表格的机器核对版本） |
| `.pi/repair/acceptance/a_scenarios.py` / `bc_scenarios.py` | 可重跑的验收夹具（只读库文件，不写库） |
