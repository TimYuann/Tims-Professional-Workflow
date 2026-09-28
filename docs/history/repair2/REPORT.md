# 真实链路测试后 · 最小修复实施报告（repair 2）

**状态**：3 项改动（A1 / B2 / B3）已落盘；B1 只做回归确认（**零产物修改**）；D1/D2 **未裁，未代签**；**未 commit**；未动 `/tmp/f-review-probes/`。
**执行者**：repair-1（本仓唯一执行会话）。**本报告是执行者自证，不是独立复验**；三个情景的语义复验按计划留给独立判断侧。

前置事实：

- HEAD 未动：`52d3315`（`git log --oneline -1`）。
- 他人改动保留：`docs/**`（含 Owner 未跟踪的 `REVIEW_R2.md`）与 `upstreams/**` pre/post 逐字一致。
- 本轮相对上一轮（repair 1 收口）改动的文件恰为：`identity.md`、`pipeline.md`、`SOURCES.md`、`roles/{planner,driver,reviewer,verifier,integrator}.md`；其余（含 `AGENTS.md`、`README.md`、`closure.md`、`scripts/ws-identity.sh`）逐字未动（sha256 对照见 `.pi/repair2/evidence/post-hashes.txt` 与 `.pi/repair/evidence/post-hashes.txt`）。
- 硬约束核对：未新增角色（仍 10 份）、未新增收据/artifact（无 `evidence-store`/`harness-receipt`）、未新增总控层；`scripts/ws-identity.sh` **未改**且不含 `.pi` 排除项。
- 证据目录：`.pi/repair2/evidence/`；验收夹具：`.pi/repair2/scenarios/`。

---

## 1. 三项改动落在哪（①）

| # | 改哪里 | file:line | 关键条文 |
|---|---|---|---|
| **A1** | Planner 判据设计 | `roles/planner.md:141`（§4.6 第 1 步）、`:142`（第 2 步） | "写判据时先从 Owner 的结果句提出至少一个合理但错误的实现或边界读法"；"`make check` 只说明运行入口"；语义未定才问 Owner，可由已定语义算出的期望值不推回 Owner |
| | Driver 发卡前判据核对 | `roles/driver.md:68`（§3 `task-card.verification` 含义列）、`:104`（代产 `slice-plan.verification` 含义列）、`:172`（§4.2 第 6 步） | "目标主张 + 真实检查入口 + 一组可判否的正/反对照"；"不得只填 `make check` 并据它放行"；补判据由 Implementer 改测试并形成新候选，**Driver 与 Reviewer 都不顺手改产品** |
| | 独立挑战不挪走 | `roles/reviewer.md:170`（§4.5）、`roles/verifier.md:169`（§4.6） | 未改动，仍是上游判据之外的第二道闸 |
| **B1** | **零产物修改** | — | `closure.md` 主链第 3 行、`roles/driver.md §3`、`pipeline.md §11`、`roles/implementer.md §4.0` 原样保留；只做两份场景回归（见 §3） |
| **B2** | 身份范围例外 | `identity.md:36`（§2 排除列后） | "编排/工具运行时产物不自动全局豁免"；例外须**首个写入前**在范围声明指名具体路径/受限模式（如 `.pi/loops/loops-*.json`、`.prev`）；不能事后扩大为 `.pi/**`；每项必答"放了产品代码会不会被排掉" |
| | Driver 范围分列 | `roles/driver.md:64`（§3 `task-card.scope` 含义列）、`:206`（§4.4 第 5 步） | 源码允许写入范围与"仅作全树比对例外的运行时路径"**分列**；后者不是 Implementer 的写入授权；范围/例外变化要重新声明并通知判断侧 |
| | Integrator 核两套声明 | `roles/integrator.md:72`（§4.1 第 5 步） | 候选 manifest 与全树越界比对各用**各自正确**的范围声明；事前例外之外的新文件（含未声明的 `.pi/` 源码）也要查；事后扩大排除不得换取"无越界" |
| **B3** | 冻结判据的承重证据 | `roles/reviewer.md:50-51`（§3 `coverage`/`residuals` 含义列）、`:108`（§4.1 第 8 步） | 写清具体对象、路径/可重建输入、hash、**需保留到哪个交付/复核点**、原产者；`/tmp` **只算临时证据**；不得静默搬到范围外目录 |
| | Verifier 字段约束 | `roles/verifier.md:47`（`commands`）、`:49`（`falsification`）、`:51`（`uncovered`） | 证据以文件路径承重时同样写 hash/保留点/原产者；变异读数只在临时位置要标临时；不可复用的推断记 `uncovered` |
| | Driver 交接核与收口 | `roles/driver.md:207`（§4.4 第 6 步）、`:276`（§4.8 第 7 步） | 核"现在可取回 + 保管到所需时间 + 搬迁有授权"；不满足先向 Owner 要**保存位置或仅本轮一次性使用**的决定；`roundup` 不得把未获保管授权的临时证据写成将来可复用 |
| | 复用判据收紧 | `pipeline.md:108`（§8 第 1 条） | "可取回"包含**承重夹具/原始读数仍可取回、位置未失效**；只剩摘要或已不存在的 `/tmp` 路径不得复用为 `PASS` |
| **台账边** | SOURCES 落点同步 | `SOURCES.md:120`（test-behavior 新增行）、`:485`（新增 §9.1 本库自定：范围例外与证据寿命）、`@一组可判否的正/反对照` 与 `@不得静默搬到范围外目录` 等新 key | 归台账那条边：新增/更新落点并重跑 `render-ledger.py`（225 key 一致） |

**附：一处上轮自造缺陷的清理（已披露）**：上一轮我把 `§4.9 推进前说明` 插在 `§4.8 收口与汇报` 之前，本轮在动 `driver.md` 时顺手把它移回 4.8 之后（`roles/driver.md:265` 为 4.8，`:284` 为 4.9）。属我自己的改动归位，不是计划外新规则。

---

## 2. C 批三个情景：原样命令与原样输出（②）

### 2.1 情景 1 · 比例错实现对照

```console
$ bash .pi/repair2/scenarios/c1/run_c1.sh | tee .pi/repair2/evidence/c1-ratio-vs-fixed.txt
### 1) 旧 7 条 vs 比例错实现（旧测试全绿，必须被读成"不能区分"，不得据此晋升）
----- PYTHONPATH=impl_ratio pytest -q test_pricing_old.py -----
.......                                                                  [100%]
7 passed in 0.03s
[pytest 退出码] 0

### 2) 新判据（旧 7 条 + 非边界 witness）vs 比例错实现（应红）
----- PYTHONPATH=impl_ratio pytest -q test_pricing_new.py -----
.......F                                                                 [100%]
=================================== FAILURES ===================================
___________________ test_non_boundary_witness_51000_is_49500 ___________________

    def test_non_boundary_witness_51000_is_49500():
>       assert pricing.price(51000) == 49500
E       assert 49470 == 49500
E        +  where 49470 = <function price at 0x107d2eb90>(51000)
E        +    where <function price at 0x107d2eb90> = pricing.price

test_pricing_new.py:9: AssertionError
=========================== short test summary info ============================
FAILED test_pricing_new.py::test_non_boundary_witness_51000_is_49500 - assert...
1 failed, 7 passed in 0.09s
[pytest 退出码] 1

### 3) 新判据 vs 定额实现（应全绿）
----- PYTHONPATH=impl_fixed pytest -q test_pricing_new.py -----
........                                                                 [100%]
8 passed in 0.03s
[pytest 退出码] 0

### 4) 上游判据规则是否已在角色文件里（开写窗前要求非边界正/反对照）
141:1. 每条验收判据配一条验证命令，并写明它**怎么判否**。**写判据时先从 Owner 的结果句提出至少一个合理但错误的实现或边界读法**，再找能让两者读数不同的输入与字面期望值；写下这一对"正确/错误各会返回什么"，并说明仓库命令是否真会执行该断言。
142:2. 高风险片在实现之前就要指出"怎样的实现是错的但能过检查"，把这条写进判据里。**`make check` 只说明运行入口**；若现有用例不能区分，在实现开始前把要补的断言写进本片 `verification`。语义本身未定才问 Owner，不把可由已定语义算出的期望值推回 Owner。
68:| `verification` | 用什么命令或操作判定做完；判据必须能判否。**目标主张 + 真实检查入口 + 一组可判否的正/反对照**；无 Planner 而由我代产 `slice-plan` 时同样核对：写不出区别"符合目标"和"一种合理错实现"的读数，就先补判据或退回 `roles/planner.md`；**不得只填 `make check` 并据它放行** |

### 5) Reviewer 的独立挑战仍在（上游判据不是终审）
170:### 4.5 反实现挑战：判据真的能抓住错误实现吗
175:1. 提出一个问题并写下来："什么样明显错误的实现，仍能通过当前这套判据？"
```

**读数**：① 旧 7 条对比例错实现 **7 passed** → 该证据不能使任务卡晋升；② 加入非边界 witness（51000→49500）后比例实现 **1 failed, 7 passed**（读数 49470 ≠ 49500）、定额实现 **8 passed**；③ 上游判据在开写窗前给出 witness 的要求已写进 Planner/Driver；④ Reviewer 的独立挑战仍在。
**如实说明**：原始 7 条用例位于 `/tmp/f-review-probes/`（D1 待裁，未触碰），本情景用**结构等价的 7 条重建**（唯一采样点 50000，定额 1500 与比例 3% 在该点读数相同）；重建的是判别结构，不是原始文件本身。

### 2.2 情景 2 · 范围对照

```console
$ python3 .pi/repair2/scenarios/c2/run_c2.py | tee .pi/repair2/evidence/c2-range-scope.txt
C2 范围对照（tree=/Users/yuantian/Developer/tim-professional-workflow/.pi/repair2/scenarios/c2/tree）
  基线文件数=4；事前声明 sha256=81cd4402c7c0015d
  候选 manifest(两文件) digest=ws:v1:f3adce67d3b4e4be8103c4ccd3453f15a7e9093954f8947da8a3c6d40082e7e8
  (a) 变化=['.pi/loops/loops-1.json', '.pi/loops/loops-1.json.prev']
  [PASS] 具名 loops 变化可被事前声明排除 :: ['.pi/loops/loops-1.json', '.pi/loops/loops-1.json.prev']
  [PASS] (a) 范围外变更集为空 :: []
  [PASS] loops 自动写入不使两文件候选 manifest 漂移 :: ws:v1:f3adce67 vs ws:v1:f3adce67
  [PASS] 身份复核走 verify：运行时写入后按范围声明复核仍通过 :: exit=0 ['VERIFIED ws:v1:f3adce67d3b4e4be8103c4ccd3453f15a7e9093954f8947da8a3c6d40082e7e8']
  (b) 白名单内变化=['src/fee.ts', 'src/price.ts']
  [PASS] 白名单内改动被记入写入范围 :: ['src/fee.ts', 'src/price.ts']
  [PASS] 契约内源码改动使候选身份变化（需新冻结） :: ws:v1:f3adce67 -> ws:v1:6ebf0b40
  (c) 未声明新增后的范围外变更=['.pi/evil.py']
  [PASS] 未声明的 .pi/ 源码文件必须被发现 :: ['.pi/evil.py']
  [PASS] 事前声明未被事后改写（哈希门） :: pre=81cd4402c7c0 now=81cd4402c7c0
  (d) 即使另写一份 .pi/** 排除声明，判定仍用事前声明 → 范围外=['.pi/evil.py']；不得据此得出"无越界"
  [PASS] 事后扩大排除不得获得"无越界"结论 :: ['.pi/evil.py']
  [PASS] scripts/ws-identity.sh 无"全局排除 .pi/**" :: 命中 0 行
  ws-identity.sh sha256=7bf666ab013cc21b

C2 结论: 全部通过
```

**读数**：具名 loops runtime 变化可在**事前声明**的例外里排除；额外放入的未声明 `.pi/evil.py` 必须被发现；事后另写 `.pi/**` 排除声明不能换取"无越界"（判定绑定事前声明哈希）；候选 manifest 只覆盖两个白名单文件，运行时写入不使其漂移，走 `ws-identity.sh verify` 仍通过。

### 2.3 情景 3 · 证据寿命对照

```console
$ python3 .pi/repair2/scenarios/c3/run_c3.py | tee .pi/repair2/evidence/c3-evidence-lifetime.txt
C3 证据寿命对照（临时根=/tmp/f-repair2-94011；禁区=/tmp/f-review-probes）
  [PASS] 临时根不是 /tmp/f-review-probes :: /tmp/f-repair2-94011
  禁区是否仍存在（只读观察，不写入）: 存在

--- 1) 冻结判据引 /tmp 时立即可运行 ---
$ cd /tmp/f-repair2-94011 && python3 -m pytest -q test_pricing_base.py
........                                                                 [100%]
8 passed in 0.03s
[退出码] 0
  [PASS] 此刻可运行且 8 passed :: rc=0

--- 2) 规则是否要求写明保留点、且把 /tmp 定为临时证据 ---
  [PASS] pipeline.md §8 位置未失效
  [PASS] reviewer §4.1 第 8 步临时证据
  [PASS] reviewer §4.1 禁止静默搬迁
  [PASS] verifier §3 commands 保留点/原产者
  [PASS] driver §4.4 第 6 步三问
  [PASS] driver §4.8 第 7 步不得写成可复用

--- 3) 临时证据消失后，按同一冻结判据复用 ---
$ cd /tmp/f-repair2-94011 && python3 -m pytest -q test_pricing_base.py   # 目录已删除
ERROR: file or directory not found: test_pricing_base.py
[退出码] 4
  [PASS] 复用失败（不得再发 PASS） :: rc=4

--- 4) 能重建的最小输入经 hash 核对后可按新对象重做 ---
  [PASS] 重建输入 hash 与冻结判据记录一致 :: 76b08069dc5197b9
  注：重建的是**输入**；原本未保留的变异原始读数不能因此说成还在。

C3 结论: 全部通过
```

**读数**：冻结判据引 `/tmp` 时立即可运行（8 passed），但规则要求标明保留点/原产者且把 `/tmp` 只算临时证据；临时证据删除后同一判据复用**失败（rc=4）**；可重建的最小输入经 hash 核对一致，能从新对象重做——但**不能**把未保留的变异读数说成还在。`/tmp/f-review-probes/` 只读观察、未写入。

### 2.4 规则层总表（A1/B2/B3）

```console
$ python3 .pi/repair2/scenarios/rules/run_rules.py | tee .pi/repair2/evidence/rules-abc.txt
...
A1/B2/B3 结论: 全部通过     （32 条 PASS / 0 FAIL，EXIT=0）
```

---

## 3. B1 回归确认读数（③）

```console
$ python3 .pi/repair2/scenarios/b1/run_b1.py | tee .pi/repair2/evidence/b1-regression.txt
[现行落点核对] 计划称这些已经是 Driver 代产完整 slice-plan，不重复修
  [PASS] closure.md 主链第 3 行存在
  [PASS] 第 3 行跳过时由 Driver 代产完整 slice-plan（"五字段全填"）
  [PASS] driver §3 声明 slice-plan 产出
  [PASS] driver §3 限定「单片、无依赖」才代产
  [PASS] pipeline §11 有 Driver→slice-plan→Implementer 边
  [PASS] implementer §4.0 缺件先停
[场景 1] 只有 task-card、没有 slice-plan
  → 读数: 停止开工 + 零写入 + 向 Driver（或 Planner）点名缺件
[场景 2] Driver 合法代产全字段 slice-plan
  → 读数: 收据齐 + 授权有效 → 开工（代产者身份不降低核对）
[零改证据]
  [PASS] closure.md 未被本项改动 :: c653f80fa317798b（= 上一轮收口值）
  [PASS] scripts/ws-identity.sh 未被本项改动 :: 7bf666ab013cc21b（= 上一轮收口值）
B1 结论: 回归成立、零产物修改
```

即：报告里"closure 让 Implementer 补"的读法被确认已作废，**没有**为修一个不存在的句子而改动 `closure.md`；当前 producer 仍是 Driver，未把正式判据写权分给作者侧。
（上面为读数摘要；逐字输出见 `.pi/repair2/evidence/b1-regression.txt`，脚本 `python3 .pi/repair2/scenarios/b1/run_b1.py` 可重跑。）

---

## 4. D1 / D2 未裁标注（④，未代签）

| 决定 | 本轮处置 | 待裁点 |
|---|---|---|
| **D1 既有 C9 `/tmp` 证据去向** | **未动**：`/tmp/f-review-probes/` 未写入、未迁移、未清理；C3 只用自建 `/tmp/f-repair2-<pid>/` 并已删除 | A 授权稳定位置并搬迁承重最小材料（需新冻结）／B 只承认本轮一次性、不作将来可复用 PASS／C 保留现状等待（`/tmp` 消失即断链）。在 Owner 决定前，库内规则已禁止把该证据写成长期锚（`pipeline.md §8`、`roles/reviewer.md §4.1` 第 8 步、`roles/driver.md §4.4` 第 6 步） |
| **D2 未来项目的运行时目录例外权** | **未代签**：只落了"每批事前具名声明 + 事后扩大无效"的可执行规则（`identity.md §2`、`roles/driver.md §3/§4.4`、`roles/integrator.md §4.1`）；未写任何"库级自动排除 `.pi/**`" | A 每项目/每批由 Owner 或既有授权持有人事前批准**具名路径模式**（当前实现与之一致）／B 库级自动排除 `.pi/**`（**未采用**）。本次只把已获批的 `loops-*.json(.prev)` 作为**例子**写入，未把它写成所有项目的默认 |

---

## 5. 最终检查（⑤）

```console
$ python3 scripts/render-ledger.py --check
render-ledger --check: OK（225 个 key，生成区与重新生成的结果逐字一致）
EXIT=0

$ python3 scripts/check-library.py
...（完整输出见 .pi/repair2/evidence/final-checks.txt）
合计: 26 项通过 / 0 项失败 / 26 项检查
EXIT=0
```

完整输出文件：`.pi/repair2/evidence/final-checks.txt`（先 render-ledger 后 check-library，两段均 EXIT=0）。

---

## 6. 残留与说明

1. **未做（按计划）**：不新建角色/收据/总控层；不把检查接到真实项目交接（计划明确要求先证明能读真实交接物并获 Owner 授权）；未触碰下游项目与 `/tmp` 现场。
2. **语义复验留给独立侧**：本轮的 C 批是"用真实命令把三种对照跑出来"，其中 C1 的 7 条为等价重建（原始文件在受保护现场）、C2/C3 为夹具树/自建临时目录。真实链路的三条情景仍应由独立判断侧在真项目上复核。
3. **SOURCES 落点区已重生成**（222 → 225 key）；新增 §9.1 明确标注两条规则为**本库自定**（来自 `FLOWTEST-REPORT.md`），不冒充三仓吸收。
4. **未 commit**，工作树保持可 `git diff`；`docs/**`、`upstreams/**`、`.pi/core/**` 未动。
5. **上轮自造缺陷清理**：`roles/driver.md` §4.8/§4.9 顺序归位（见 §1 附注）。
