# R3 任务卡 · 终轮返修（配额最后一轮：改完 → 我审 → oracle 终验）

**前提**：这是三轮配额里的最后一轮修改。因此——
- **每一条都必须按"类"改，不许按实例改**（上一轮我只点名了 architect/reviewer 两处，同一模式在 investigator/planner/verifier 里还在，被 oracle 抓出来，这是我的失误）。
- **做不到的，必须在报告里如实标"未修 + 原因"**，不许静默跳过、不许把阻断降级成建议。
- 冻结身份已作废（要改文件），改完由我重新冻结并算新 digest。仍然**不要 commit**。

---

## 0. 先做一件事：全库模式扫描

对下面 5 个模式**每一处**都列出来（`grep -n` 全库，不只 roles/），逐个处理，并在报告里附清单：

| 模式 | 说明 |
|---|---|
| P1 | 任何角色声明"直接发/直投某角色"（绕过 Driver 唯一转手） |
| P2 | 任何"可跳过"路径的替代职责，与该产出方 §5 负面边界冲突 |
| P3 | 任何"跳过 N 后，下一环 §2 仍要求某收据" |
| P4 | 任何字段名在不同文件里指**不同形状的值**（如 `object` 单 token vs 二元组） |
| P5 | 任何声称"已落地的动作"在其声称的落点（角色 file:line）**实际不存在** |

---

## 1. B-1 · 档位口径（我定了，照此写）

**问题**：上一轮把 Owner 重定义成 Driver，用"改名"绕开了"Driver 必须是独立会话"这条要求，并让 trio 实际变成 4 会话。

**我的裁定**：
- **档位口径 = 工作会话数**（作者侧 + 判断侧的工作会话）；**Driver 的承载单列，不计入档位数**。
- 承载三选一，必须显式声明：① Owner 亲自；② 独立轻量编排会话；③ （仅限 `full`/`trio`）作者侧之一兼任——**但仅当它不是实现该候选的人**。
- **`solo(1)` 如实标注**：`可用，但不满足「Driver 是独立会话」这条要求`（编排由 Owner 承担，需 Owner 明确接受）；`trio(3)`/`full(9)` 满足。
- **禁止**再把"Owner 亲自当 Driver"写成"满足独立 Driver 会话"。**如实标不满足**，别改口径去迎合。

---

## 2. 逐条修（8 项）

### B-2 · 跳过设计缺合法生产者 + 跳审查后下游收据消失
- **①** `closure.md:16` 让 Planner 代产完整 `design-proposal`，但 `roles/planner.md:12,29-41,168` 明说只产 `slice-plan`、不重新设计 → **Planner 不能代产**。改法：跳过设计时，替代物由 **Architect 的最小形式**产出（Architect 本就是它的生产者）；**Architect 也不参与时，该路径标"不可跳过"**。
- **②** `closure.md:30` 跳 Reviewer 只补 `equivalence-proof`，但 `roles/verifier.md:25-31` 与 `roles/integrator.md:32-34` 仍收 `review-verdict` → 改法：**Reviewer 不可完全跳过**。允许"**快速等价审**"，但必须由**独立 Reviewer**交出**字段齐全**的 `review-verdict`（只是复用等价证明、缩短工作量）。`equivalence-proof` 不得单独充当 `review-verdict`。
- **③ G5 是假绿**：oracle 实测"12 字段只留 2 字段"仍 `19 PASS`。改法：G5 不得只判"替代栏有 ≥2 个反引号"，必须**逐字段比对接收方 §2 要求的字段集**（差集非空即 FAIL），并把该突变做成常驻夹具。

### B-3 · 三处 §6 仍直发 Oracle（P1 类）
`roles/investigator.md:184`、`roles/planner.md:178`、`roles/verifier.md:224` 仍写"发 `pending-question` 给 `roles/oracle.md`"。
改法：三处改成"把争议事实交 Driver，由 Driver 判四条触发、填收据并转手"；**并按 P1 全库扫描，把同类一次性清完**。
**加机械门**：拓扑里凡指向 Oracle 的边，只有 Driver 可作起点；任何角色 §6 出现"发 `pending-question` 给 `roles/oracle.md`"即 FAIL（oracle 建议的结构对照）。

### B-4 · `ws:v1` 无法证明"当前文件与交付对象同一"（工具缺陷）
实测缺陷（oracle 原样读数）：
- `digest`/`compare` 只哈希 **manifest 文件本身**；源文件改了，旧 manifest 与新 manifest 比较**仍 EQUAL**；
- 伪删除 `-path=oldhash`（文件其实还在）被接受；
- `../external.txt` 越出仓根被接受；
- 重复路径让同一文件集产生两个身份。

改法（最小）：
1. 新增 **`verify` 模式**：由明确**范围声明**重新枚举当前源文件，逐条与交付 manifest 比较；**缺文件 / 多文件 / 越根 / 重复路径 / 伪删除 → 一律报错、非零退出**。
2. `identity.md` 写清：**`compare` 只比两份 manifest**，不能证明"当前树与交付对象同一"；**身份复核必须走 `verify`**。
3. `identity-selftest.sh` 为上述五类各加一条**必须变红**的夹具。

### B-5 · `object` 的形状两套（P4 类）
`identity.md:7-15` 把 `object` 定成单 token；`roles/reviewer.md:45`、`roles/verifier.md:39` 定成 `(base + tree)`；`roles/driver.md:104` 的 `equivalence-proof.object` 又是单 token；`roles/integrator.md:65` 要三方对照却没定义 tuple 与 token 怎么比。
**我的裁定**：`object` 统一为**二元组**，固定序列化：
```
object := base=<token>;tree=<token>
（token = commit:<sha> | tree:<sha> | ws:v1:<sha256>）
相等判定：两个 object 相同 ⇔ base token 与 tree token 各自按 identity.md §4 判定相同
```
同步 `identity.md`（作为唯一定义）、reviewer / verifier / integrator / driver 四处，以及 `equivalence-proof`。**并按 P4 全库扫一遍还有没有别的字段名指两种形状。**

### B-6 · 开工门的真实冷启动失败（最关键的行为缺陷）
oracle 自建负例：**无 `slice-plan`、只给 Driver 任务卡**，Implementer **先写测试和产品代码、跑 RED/GREEN，末尾才把缺件记成"自行推导假设"**。
改法：
1. `roles/implementer.md` §4 **新增第 0 步「开工前收据核对」**，并写明：**核对不通过时唯一合法动作是停止**——把缺件列出来交 Driver 请求合法代产，**不得自行推导、更不得事后追认**。
2. §2 主收据那行把"缺：不开工"写成**可执行动作**（向谁要、要什么、停在哪个状态），不是一句原则。
3. 副收据 `task-card` 必须含 `auth_record`（授权快照）；**拿不到同样不能以"按最小范围处理"当作已授权**。
4. **验收方式**：重跑同一缺件探针（我或 oracle 跑），**必须零写入**；然后给齐 `slice-plan` 再跑正控制。

### B-7 · docstring 等价旁路仍假绿
`roles/reviewer.md:84-88` 允许"剥除 docstring 后字节相同"放行；oracle 实测 `fee.__doc__` 从 `'Safety contract for caller'` 变成 `None`——**docstring 在 Python 是可观察接口**（introspection / 文档生成）。
改法：docstring **不算机械等价**；要免独立审查必须**证明没有消费者读取它**；真正的注释删除按目标语言另测。

### B-8 · SOURCES 一半仍是台账自述（P5 类）
逐行撤回/落点补正：
- `SOURCES.md:194,294` 仍把"当前实测基线 → 不得回退"称为合法门禁来源 → 与已修的 `roles/planner.md:119-127` 及"用户要求/既有契约/CI"冲突，**撤回**。
- `SOURCES.md:260-263` 选"注释写 why 不写 what"，声称落在 `roles/implementer.md §4.4`、`roles/reviewer.md §4.3`，**两处都没有这条动作** → 要么补落点，要么改成"不采纳"。
- `SOURCES.md:218` 仍把 addy 的 **3 cycles** 标"保留"并指向已选 **2 rounds** 的 Reviewer §4.7（`:366` 又说不采纳）→ 统一口径。
- **R-2 的 11 条判据**：来源是 `SOURCES.md §6` 自述"不是吸收来源"的**只读消费方**。**我的裁定：消费方契约不构成 D1 的"三仓出处"**——把这 11 条显式标为 `消费方契约（非三仓吸收）`，并说明其权威类型；不许只换"已采纳"标签。
- **按 P5 全库扫**：凡声称"已落地到 X 角色 Y 节"的，逐条回读该节确认动作存在。

---

## 3. 机械门要跟着长（否则下一轮还会回到同样的问题）

| 门 | 必须能抓 |
|---|---|
| G5′ | 替代收据字段集 vs 接收方 §2 要求字段集的**差集非空** |
| G6 | P1：非 Driver 起点指向 Oracle 的边 / 角色 §6 直投 Oracle |
| G7 | P3：任何"可跳过"路径，其下一环 §2 要求的字段必须能被替代收据或上游收据覆盖 |
| G8 | P4：同名身份/关键字段在不同文件里形状不一致 |
| G3′ | （已有）主链行数/唯一/非空 |

**每道门都要有常驻负夹具，并在报告里附"夹具 → 变红"的原样输出。**

---

## 4. 本轮仍不做（如实标欠账）

- 不重写角色整体结构、不新增角色、不引入第二套状态机。
- `check-team-version.sh` 的完整内容快照机制：仍不做，但边界要写清。
- 性能诊断的完整方法（瓶颈定位表 + 测量清单）：仍为欠账。

## 5. 报告

`.pi/round3/REPORT.md`：① §0 五个模式的**全库清单**与逐处处理结果；② B-1…B-8 逐条落点（file:line）；③ G3′/G5′/G6/G7/G8 的**负夹具实跑输出**；④ 未修项 + 原因；⑤ 最终 `check-library.py` 退出码与输出。

改完 intercom 回我 ≤15 行，然后**停笔等冻结**。
