# Round 2 · 冻结产物终验（独立结论）

对象：未提交的工作树，HEAD `52d3315d881cdff9f42d52c2db0eb2796b4fa44e`。仓根 `/Users/yuantian/Developer/tim-professional-workflow`，Python `3.14.4`，Herdr 活跃（`HERDR_ENV=1`）。按 Arbiter 给的 21 文件列表和逐文件 sha256[:16] 算法，**开验与本报告定稿前均得到 `21 ee34bac59ee1cad2730380f95a287487e3e9793bd97166aca79988e1c4271ca4`**。本节结论在读 `.pi/round2/REPORT.md` 之前写定；R1 的报告属于前一对象，不拿来替代本轮读数。

## 1. 结论（三态）

**FAIL**。R2 的结构修补大多真实存在，且我自己设计的独立 Reviewer 冷启动抓住了坏边界；但**作者侧“缺主收据不开工”实测失败**，文档允许的跳过路线仍有不可能产生的收据和无 Review verdict 的下一环，身份规范自身不一致且 `ws:v1` 可在源文件变更后继续报 EQUAL。还有直投 Oracle 与单一转手者自撞，不能以 19/19 结构检查抵消。这些是已验证的问题，不是环境无法检查。

## 2. 实际执行与原始可证伪读数

### 2.1 机械和回归

- `python3 scripts/check-library.py` → **EXIT=0，19 项通过/0 失败**。它打印扫描 `roles, scripts, pipeline.md, closure.md, identity.md, README.md, AGENTS.md, SOURCES.md, VERSION`，仅排除 `docs/**`、`.pi/**`、`upstreams/**`；收据 **30/30**、产出 **16/16**、主链 **9 行**、按需 **3 行**，身份规则 6/6 内联；身份自检 **8/8**。这次不再自排除 checker。`pipeline.md` 148 行、`README.md` 70 行，符合上限。
- `bash scripts/identity-selftest.sh` → **EXIT=0**；逐项 `P1,P1b,N1,N2,N3,N5,N6,N4` 都 `[PASS]`，末行 `合计：8 通过 / 0 失败`。自检覆盖它声称的夹具，而非下述我新增的反例。
- 各自隔离的 `/tmp/tim-r2-regress-*` 副本（`docs/`、`upstreams/` 仅符号链接作存在性读，不写）：散文收据 `state→statezzz` → checker **EXIT=1**，收据字段缺 `statezzz`，矩阵第 6 行输入 `state` 与角色 §2 不符；主链设计输出字段 `red_flag_screen→red_flag_screenZZZ` → **EXIT=1**，指出第 2 行输出不在 Architect §3；删光主链 → **EXIT=1**，`主链只有 0 行（至少 9）`；在 logger 追加字面具体底座名 → **EXIT=1**，指出 `scripts/log-decision.sh` 行号。R1 的散文收据、矩阵交叉、空主链和 B-7 扫描回归**确实没有倒退**。
- 新增 **G5 反实现挑战**：仅在副本把 `closure.md` **第 1 行跳过调查的替代收据**由 12 字段改为仅 `symptom` 与 `entry_point`（缺 10 项），其它文档不变；`python3 <副本>/scripts/check-library.py` → **EXIT=0，19/19，`[PASS] 可跳过路径 G5：替代收据完整`**。原因是 `scripts/check-library.py:514-528` 只检查有一个 `roles/` 名与移交文本中 ≥2 个反引号字段，没有对上下一环要求的**字段全集**或产出方。此项名字比机器能力宽。
- 我自己设计的 `ws:v1` 实验在 `/tmp/tim-ws-adversarial-*`：生成 `src/a.txt` 的旧 manifest 后把源字节 `GOOD` 改 `BAD!`，旧 manifest 的 `digest` **仍为** `ws:v1:d6edb7a5...`，`compare <旧> <旧>` → **EXIT=0 `EQUAL`**；实际重建当前清单才得 `ws:v1:1f78778c...`。`-src/a.txt=<旧 sha>` **即使源文件仍存在**也可 `manifest` → **EXIT=0**；清单 `../external.txt`（仓根外）也可 `manifest` → **EXIT=0**；相同文件列两次则生成另一 digest，重复路径未拒绝。详情见 B-4：这些都是源字节状态或范围与它自称的对象身份不一致的反例。
- `roles/reviewer.md:84-88` 仍给“剥离文档字符串后逐字相同”免独立审查。独立脚本分别执行含 `"""Safety contract for caller"""` 与去掉该 docstring 的同一函数：去 docstring 后文本一致，但 `fee.__doc__` 从字符串变 `None`。该属性对调用者可观察，**机械证明可能错误**（B-5）。

### 2.2 我自行设计的冷启动功能实验（未借用 R1 测试台）

所有测试台位于 `/tmp`，没有写冻结仓库；两类角色在不同 Herdr tab/pane 且不同目录、不同新会话，启动参数均由我自己调用并在 `herdr agent start` JSON 中确认：`--kind pi --provider opencode-go --model deepseek-v4.1-flash --thinking max --no-skills --no-context-files --append-system-prompt /…/roles/<role>.md`；没有把作者结论交给判断者。

| 可证伪预期 | 实际步骤与读数 | 判定 |
|---|---|---|
| **作者负例：缺 `slice-plan.slices` 时不能开工** | `/tmp/tim-r2-author.K7eU7W` 只有一张 Driver `TASK.md`、原始代码/两个绿测试、Makefile；没有 `slice-plan` 或 `design-proposal`。命令基线 `make check` → **2 tests, OK**。新会话 `r2-author-probe`（pane `w22:p9`）只收“请自行按角色文件判定能否开工”的消息。JSONL `/Users/yuantian/.pi/agent/sessions/--private-tmp-tim-r2-author.K7eU7W--/2026-09-26T14-55-52-103Z_01a0de37-2926-756a-ac69-82edba88abbe.jsonl`：第 17–20 行读/跑基线，第 21–22 行**先编辑测试**，第 24–25 行 RED，26–27 行**编辑实现**，28–29 行 GREEN；直到最后第 32 行才报告“`slice-plan` 未收到，按最小范围自行推导”。它仅 `intercom list/list-cwd`，没有向 Driver/Planner 请求完整收据。现状代码已被它改成 MEMBER 分支，并且 5 tests, OK。 | **FAIL**。`roles/implementer.md:16-24` 明写主收据 `slices` 缺则**不开工**。第三/四层只交 task-card，没有权力把副收据无声代替主收据。它确实做出正确局部功能，但这不是输入契约得到遵守的证据。任务卡不含“忽略缺失、照做”，并未人为豁免。 |
| **独立判断负例：错误边界且唯一测试全绿，应拒收** | `/tmp/tim-r2-review-blind.UWuDyW` 是我单独造的候选：`membership_fee(5000,'MEMBER')` 错误返回 **300**（契约明确应 **0**），测试只测 6000 及 BASE；`make check` 事前 **EXIT=0, 2 tests OK**。移除首次探针中“deliberately wrong”提示后，另起全新 Reviewer 会话 `r2-review-blind`（pane `w22:pA`），只收候选、设计、切片和冻结契约。会话 `/Users/yuantian/.pi/agent/sessions/--private-tmp-tim-r2-review-blind.UWuDyW--/2026-09-26T14-59-34-036Z_01a0de3a-8c14-75e4-a96c-3eea4d160be1.jsonl` 独立重算 `ws:v1`、复跑 make check，并在一次性副本用边界探针与 `> ↔ >=` 变异比较；结论 `review-verdict.state=blocked`，F1 **5000 处多收 300**，F2 **原检查对错实现和修正实现均绿**，给出返修范围与未覆盖项，未改冻结候选。 | **PASS（该局部审查能力）**。候选缺陷由真实读数证实，独立 Reviewer 未采纳 2/2 绿灯，按契约判阻断；不推出所有 Reviewer 冷启动都可靠。 |

第一轮 Reviewer 测试台曾在被审代码中写了 `# deliberately wrong at 5000`，过于显眼，**未把那轮当作盲测证据**；上述第二轮使用全新 session、无该注释、普通 docstring，对应来源是无写者上下文的候选文件。作者探针在业务功能层面有真实红→绿，但越过开工门；这正是评分不能只看 GREEN 的原因。

**测试台边界**：Pi 启动 JSON 证实 `--no-skills --no-context-files` 参数；会话内部的 system 消息正文未可见，不能从 transcript 再次验证注入文件逐字内容。测试台规模小、人工冻结输入，Reviewer 一次成功不等于端到端交接、真实服务运行或所有模型普遍可靠。作者候选的 `base/tree` 是自己在内存拼的 `ws:v1`，无已保存的 manifest 文件/范围声明，依 `identity.md:45-49` **仅交 digest 不算交付**（它在消息中打印过清单但没交文件或路径），这是额外不合格项；不是用来混淆首要的缺主收据失败。

## 3. 阻断项（现象 / 证据 / 为什么 / 最小方向）

1. **B-1 · 独立会话数量被重新命名而非满足。** `pipeline.md:35-45` 定义 `solo(1)` 为 **1 个工作会话 + Owner 亲自履行 Driver + 另一短命判断会话**，`trio(3)` 为 **3 个工作会话 + Owner 或额外的轻量编排会话**；原任务卡 `.pi/round1/TASK.md §2(3),(5)` 要求 Driver 是**独立 session**，同一套角色能以 **1/3/9** 会话装配且实现/判断不合并。Owner 亲自变成 Driver 不是独立 Driver session；若 trio 起额外 Driver，则实际 4 会话。**无法同时满足时应诚实标不可行，而不能把 Owner 重新定义为角色会话来声称 solo/trio 可用**。最小方向：和 Owner 明确是“1/3 工作会话，另计 Driver/判断”还是“1/3/9 总会话”，选一套口径；不把人类替代成未授权的独立会话。
2. **B-2 · 跳过设计缺合法生产者，跳过审查缺合法下游收据。** `closure.md:16,27` 令 `roles/planner.md` 代产完整 `design-proposal`，但 Planner `roles/planner.md:29-41` §3 **只产 `slice-plan`**，`roles/planner.md:12,168` 明说“不重新设计系统”；`pipeline.md:137-149` 也只有 Architect→`design-proposal`。因此 Planner 按角色方法与权限无法交出替代物。`closure.md:30` 跳 Reviewer 后只多交 `equivalence-proof`，而 `roles/verifier.md:25-31` 仍要求 `review-verdict.object/state/blocking/coverage`、`roles/integrator.md:32-34` 仍收 `review-verdict`；没有规则声明 `equivalence-proof` 足以替代它或由谁产生完整 verdict。G5 只判替代栏 ≥2 个反引号字段；缺十字段的突变仍 19/19 全绿（§2.1）。最小方向：不能产生全收据的路径改为“不可跳过”；若允许 Reviewer 的等价快速审，仍由独立 Reviewer 交出字段齐全的 `review-verdict`，只是可复用等价证明；Planner 不能被迫做自己明禁的设计职责。
3. **B-3 · 独立复核“唯一 Driver 转手”与三个角色 §6 直接投递冲突。** `roles/driver.md:226-232` 明定 Driver 唯一构造/转手 `pending-question`，`pipeline.md:137-149` 只列 Architect/Reviewer→Driver→Oracle；`roles/investigator.md:184`、`roles/planner.md:178`、`roles/verifier.md:224` 仍写**“发 `pending-question` 给 `roles/oracle.md`”**。Oracle `roles/oracle.md:16-25` 只接 Driver 收据，直投不能满足同一拓扑，且没有 requested_by 等完整来源。**一份单注入的 Planner/Investigator/Verifier 会听自己 §6 直接发，Driver 的唯一构造者纪律随之失效**。最小方向：三处 §6 改为“把争议事实交 Driver，由 Driver 判四触发、填收据并转手”，或显式添加获授权的直连协议并同步所有收据，勿只改 checker。
4. **B-4 · 新 `ws:v1` 无法证明当前文件与交付对象同一。** `identity.md:45-49` 说接收方复算 digest/比对，却只定义对**已保存 manifest** 的 digest；`scripts/ws-identity.sh:103-127` 的 `digest/compare` 只哈希 manifest 文件本身，源文件变更后仍 EQUAL（§2.1 原样读数）；删除条目 `-path=oldhash` 即使文件仍存在也被接受，`../external.txt` 越出仓根也被接受，重复路径导致同一文件集两身份。`identity.md §2` 却宣称清单“相对仓根、写入范围内全部现存文件+删除项”。**这些不是测试范围内的缓存问题，而是唯一真源与参考实现不一致**；会让被审候选被改后仍以旧对象证明，或范围外字节参与身份。最小方向：验证时必须由明确范围**重新枚举当前源文件**并与交付 manifest 逐字节/逐条比较，缺文件、额外文件、越根、重复路径、伪删除一律报错；自检增加这些能使测试变红的夹具。
5. **B-5 · 新身份规范对 `object` 的形状自身打架。** `identity.md:7-15` 把 `object` 定成一条 `commit:<sha>` / `tree:<sha>` / `ws:v1:<sha>` 的候选身份（`base` 单独是基线）；`roles/reviewer.md:45` 与 `roles/verifier.md:39` 却把 `object` 定成 **`(base + tree)` 的复合身份**，而 `roles/driver.md:104` 的 `equivalence-proof.object` 是三格式之一。Integrator `roles/integrator.md:65` 要三方 `object` 与候选对照，却没有为 tuple 与单一 token 的比较定义。**同一个字段名不代表同一种值**，这是 R1 身份缺口在新规范下残留。最小方向：在唯一规范中选“单 token = candidate.tree”或“有版本的二元组=(base,tree)”，给出实际序列化和相等规则，再同步三角色及等价凭据；勿只检查角色里出现 `ws:v1` 关键词。
6. **B-6 · 角色开工门的真实冷启动失败。** `roles/implementer.md:16-24` 要求主收据 `slice-plan.slices`，缺则不开工；我自己设计的无 slice-plan 负例里，该会话先写测试和产品代码、跑 RED/GREEN，然后才把“未收到 slice-plan/design-proposal”记为自行推导假设。`roles/implementer.md:30-32` 副收据 task-card 只要求 authorization/verification，不要求 Driver 新增的 `auth_record`（`roles/driver.md:55-57`），本测试卡仅声称授权动作、没有授权快照，它也接受并改代码。**G4 的“缺了怎么办”非空不能证明其处置被遵守；主收据不能由猜测替代，更不能在修改后追认**。最小方向：角色 §2 明确“缺主收据→停止并交 Driver 请求合法代产 slice-plan/设计物”，副收据拿不到同样不能以“最小范围”视为已授权；重跑同一缺件测试，原本会写代码的探针必须先停并无写入；单独给齐后再正控制。
7. **B-7 · 等价审查的 docstring 分支仍假绿。** `roles/reviewer.md:84-88` 虽已明确符号集合相同不等价，但对“剥除文档字符串”仍允许剥除后字节相同放行。自测有无 docstring 的 `fee()` 在剥除后代码逐字相同、`fee.__doc__` 实测从 `'Safety contract for caller'` 变 `None`。**docstring 在 Python 是真实可观察接口**，如果外部通过 introspection/doc generation 读取，删除它改变行为；除非已证明没有这种消费方，不能免独立审查。最小方向：把 docstring 列为需证明确无消费者的差异，或不作为“机械等价”免门；真正的注释删除另按目标语言测试。
8. **B-8 · B-5 的来源处置有一半仍是台账自述。** `SOURCES.md:362-368` 对 I-1/I-2（`roles/investigator.md:107,126`）、L-1（新 `constraints` 与 Architect §2）、L-2（matt/addy TDD 真冲突且角色选 addy）、R-3（`roles/reviewer.md:196,200` 选两轮）确有落点；但 `SOURCES.md:194,294` **仍把“当前实测基线→不得回退”称为合法门禁来源**，与已修的 `roles/planner.md:119-127` 及 Owner 的“用户要求/既有契约/CI”冲突；`SOURCES.md:260-263` 选“注释写 why 不写 what”，而所声称的 `roles/implementer.md §4.4`、`roles/reviewer.md §4.3` 均没有这条动作；`SOURCES.md:218` 仍将 addy 的 **3 cycles** 标“保留”并指向已选择 **2 rounds** 的 Reviewer §4.7（`:366` 又称不采纳）。R-2 的 11 条判据清单在 `roles/reviewer.md §4.6` 未改，来源仍是 `SOURCES.md §6` **明说不是吸收来源的只读消费方**，没有上游 `file:line` 或实测本轮逐条证据来满足任务卡 D1 的出处二选一。**为什么阻断**：同一仓同时说“已单选/已落地”和相反旧规则，三仓吸收与单一事实源无法核对。最小方向：逐行撤回旧门禁、错落点、错三轮状态；把消费方 11 条的权威类型请 Owner 明确批准为 D1 的例外，或补各条上游/实测证据，不能只换“已采纳”标签。

## 4. 非阻断 / 已确认改善

- **主链普通路径**：九行、相邻字段及角色收据名实配；在“不跳过”的前提下，两处 R1 的 2/3 空转及角色↔矩阵未对账已经修复。G3 能抓空主链，B-7 能抓脚本底座字面名；README 四原语、9 角色四层接缝、VERSION 单一声明仍在。
- **跳过调查**：Driver §3 已新增 `investigation-report` 十二字段，名字可承接；但“**无现象**”条件下 `first_divergence/root_cause/constraints` 要写什么才算实质内容没有明说，`closure.md:26` 又要求“填不出实质性内容就不得跳过”。不能靠把字段名填齐推断其值合格；这条尚未以真实交接运行，本次作为另一个潜在断档记录，不用它替代 B-2 的确定事实。
- **判据实测与身份自检**：参考实现对自带八个夹具确实按期望变化；冷启动独立 Reviewer 未放过绿色坏候选；其成功只覆盖一个小函数与两个有意弱的用例，不代表大型跨边界候选已被证明。
- **Oracle 结构路由 A0**：Architect/Reviewer 的收/发字段现在对齐 Driver；我发现的三个漏改 §6 是自然语言/拓扑冲突。若要机械门，可在 `pipeline` 的边→角色 §6 收件方做**针对 `pending-question` 的结构对照**：非 Driver 且未声明向 Oracle 直发的角色若 §6 出现“发 `pending-question` 给 `roles/oracle.md`”就 FAIL；更稳的是将每个升级条目改写成明确的 artifact + recipient 结构字段再与拓扑比，别试图机械理解全部散文。

## 5. 核验边界

覆盖了冻结 21 文件两次 hash；9 角色相关输入/输出/权限与 R2 变动方法、`pipeline.md`/`closure.md`、`identity.md` 与脚本全文、SOURCES.md 原冲突与 R2 处置；checker、自检及隔离突变、Herdr 两角色三次冷启动（第二次 Reviewer 为盲化重试）。没有生产服务/真实消费者端到端运行，也没有证明方法在别的模型或无 Herdr 环境相同有效。候选归因测试台是 `/tmp` 下独立模拟，不修改冻结仓库；对会话 system prompt 实际正文，Herdr 启动 argv 是可见证据，但会话 JSONL 不提供可逐字重验的全文。B-4 的 stale-manifest 反例证明参考工具本身不会重算源字节，不排除某个人工使用者额外重读文件；B-2 的 skip 比对由合同与 G5 突变支持，未启动九角色真交接。没有拿 checker 19/19 替语义覆盖，也没有执行任何需要 Owner 授权的发布/合并/删历史动作。

## 6. 与 Owner 七条核心标准逐项对照

| 标准（`.pi/round1/TASK.md §2`） | 判定 |
|---|---|
| 1 方法 > 流程 | **部分**：主体仍在角色，流程 148 行；但角色机械等价及缺件处理有错误的方法判据（B-6/B-7）。 |
| 2 经验装角色、不放 skills | **满足（结构）**：旧 `skills/` 归档、9 角色内联身份规则；冷启动作者仍未服从自己 §2，不能推成行为达标。 |
| 3 Driver 独立会话、只编排 | **不满足**：职能不可兼任已写，但 solo 强制 Owner 当 Driver、trio 可额外会话，未兑现原来的档位/独立会话定义（B-1）。 |
| 4 底座解耦 | **部分**：脚本扫描覆盖自身、角色不含专有命令；`ws:v1` 跨环境参考实现有相对路径/源快照一致性漏洞（B-4）。 |
| 5 厚薄可缩放且实现者≠判断者 | **部分**：冷启动作者/判断不同会话，Reviewer 成功保持独立；solo/trio 实际会话数与 Owner 前提不符，跳 Reviewer 仍缺下游 Verdict（B-1/B-2）。 |
| 6 自洽无断档、单一版本源 | **不满足**：VERSION 唯一、普通链字段对齐，但身份 `object` 两种形状、Oracle 直投旧文、来源台账冲突（B-3/B-5/B-8）。 |
| 7 上一环交出下一环真正需要的字段 | **不满足**：Planner 无权产设计收据，Review 跳过仍无 Verdict，作者冷启动无 slice-plan 自行开工（B-2/B-6）。 |
| 附加：三仓深吸收、重复冲突逐条单选、工具探测只 Driver | **部分**：TDD 真冲突等已裁且 Driver 能力探测恰一处，仍有错落点/旧数字/审查轮次状态与 R-2 出处例外未获明定（B-8）。 |

独立终验至此定稿；之后若读 `.pi/round2/REPORT.md`，只在报告末尾追加“我独立发现 / 与交付方重合 / 与交付方自述不符”的对照，不反向改本结论。

## 7. 定稿后对照 `.pi/round2/REPORT.md`（仅追加）

- **独立发现，交付方未报告为阻断**：B-1 档位更名没有满足 Owner 的 Driver-session 要求；B-2 Planner 无权限/产出接口代产设计、跳 Reviewer 后 `review-verdict` 消失；B-3 Investigator/Planner/Verifier 仍直发 Oracle；B-4 `ws:v1` 的 stale-manifest/伪删除/越根/重复路径；B-5 `object` 单 token vs `(base+tree)` 两种形状；B-6 实跑冷启动作者缺 `slice-plan` 继续编辑；B-7 docstring 机械等价反例；B-8 SOURCES 旧数字/3 cycles/注释落点尚不一致。
- **与自述重合、但边界更窄**：自述 §① 的 checker 19/19、自带身份夹具 8/8、主链空表红、字面底座名红、I-1/I-2/L-1/L-2 的实际落点我独立重跑/核对过；这些 PASS 在其测试范围内成立。自述 §② G5 测的是**删空字段**能红，我的临时突变只删掉 12 个中的 10 个、留下 2 个却 **19/19 绿**，所以“替代收据完整”并未被证明。自述 §⑤ 也承认 N5 只能证明不完整清单与完整清单不同，不证明范围完整，这与 B-4 方向一致，但它没有测试旧清单与已变当前源文件仍匹配的危险路径。
- **自述与冻结对象不符/自我矛盾**：§① 把“5 条跳过路径全补齐”写作完成，但 `roles/planner.md §3/§5` 无 Design 产出且禁重新设计，Verifier/Integrator 缺 Review verdict；§①/§③ 称 17 异常已逐条处置，却保留 `SOURCES.md:194,218,294` 的相反旧结论与注释落点空缺；§⑤ 同时写 Oracle 转手问题“未修”，但 §①「收尾项 A」又宣称 Architect/Reviewer→Driver→Oracle 已修——实际只修了两个角色，其余三处直投见 B-3；§⑥ 引用“最终自检”收据 **28/28**、按需 **2**、探测 `driver.md:154`，而我针对最终摘要 `ee34…` 的实跑是 **30/30**、按需 **3**、探测 `driver.md:163`，这是自述混入旧对象读数，不可作为最终对象的证据。即使这些不一致全部改掉，独立的行为反例仍需返修。

### 17 个单元的逐项处置复核（R1 编号，不把组号当新计数）

| 编号 | R2 实际落点 | 终验 |
|---|---|---|
| 1 I-1 | `roles/investigator.md:107` 改成 Direct **或** Supported | **已落实**，与 pstack epistemics 一致 |
| 2 I-2 | `roles/investigator.md:126` 改交 Owner 或 Driver 转达、不阻塞 | **已落实**；从“下游接手人”改为真正的决定者 |
| 3 R-1 步骤4 | `roles/reviewer.md:84-88` 不再只比符号名；但 docstring 剥除后逐字相同仍允许跳独立审查 | **未闭合**，我的 `__doc__` 反例见 B-7 |
| 4 R-1 步骤5 | `roles/reviewer.md:88` 明定全范围、命令跑不通不算证明 | **已落实**，但未跑完整实物变更的比对程序 |
| 5 R-1 步骤6 | `roles/reviewer.md:89` 把 `True→False` 同符号集反例写进角色 | **已落实**，原始问题在这条路不再假放行 |
| 6 R-2 触发 | `roles/reviewer.md:171` 每条放行判据都检查 | **来源未解决**：只读消费方契约，非三仓/实测 |
| 7 R-2 锚点 | 同节第1条“锚点未核” | **来源未解决**，仅把它称 Owner 已采纳 |
| 8 R-2 阈值 | 同节第2条“阈值未定” | **来源未解决**，同上 |
| 9 R-2 取值 | 同节第3条“取值空间未穷尽” | **来源未解决**，同上 |
| 10 R-2 声明/条目 | 同节第4条 | **来源未解决**，同上 |
| 11 R-2 载体 | 同节第5条 | **来源未解决**，同上 |
| 12 R-2 前提 | 同节第6条 | **来源未解决**，同上 |
| 13 R-2 替身 | 同节第7条 | **来源未解决**，同上 |
| 14 R-2 判断依据 | 同节“能否写出否证观察” | **来源未解决**，同上 |
| 15 R-2 反例 | 同节“A 或 B、B=什么都不出现” | **来源未解决**，同上 |
| 16 R-2 不适用 | 同节“一次性探索脚本” | **来源未解决**，同上 |
| 17 R-3 | `roles/reviewer.md:196,200` 两轮规则已单选 | **角色已落实**，但 `SOURCES.md:218` 仍记“保留上游三轮”，台账未同步 |

**另两条非计数台账不实**：L-1 的 `investigation-report.constraints` 已进 `roles/investigator.md:43`、Architect §2；L-2 的真实 matt/addy TDD 冲突已改 §4.5 并使 Implementer 红绿重构一致。它们的修复不能抵消表内 R-1/R-2/R-3 剩余差异。
