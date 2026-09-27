# R4 报告 · 台账改为生成物 + 专职台账管理员

**最终状态**：`python3 scripts/check-library.py` → **26 项通过 / 0 失败，EXIT=0**；`bash scripts/identity-selftest.sh` → **15/15，EXIT=0**；`render-ledger.py --check` → **215 个 key，逐字一致，EXIT=0**。**未 commit**。

---

## ① 交付物落点（file:line）

### D1 `scripts/render-ledger.py`（223 行，新脚本）

| 部件 | 位置 |
|---|---|
| 规则行抽取（编号步骤 / 判断依据 / 条目 / 表行 / 契约块 / 整段，带 `## 节` + `### 小节`） | `scripts/render-ledger.py:94` `collect_rules()` |
| 人写 key 的读取（**只看表格行最后一列**，正文里的 `@` 不算 key） | `scripts/render-ledger.py:142` `read_keys()` |
| 渲染 + fail closed 判定 | `scripts/render-ledger.py:158` `render()` |
| 写生成区 / `--check` | `scripts/render-ledger.py:184` `main()` |
| 生成区（派生视图） | `SOURCES.md:474`（`BEGIN`）～ `:1549`（`END`） |
| 生成区前的说明段（"不要手工编辑本区"） | `SOURCES.md:469-473` |

**人写面**：`SOURCES.md` 各表格的「落点」列，形如 `@注释只写 why，；@既有约定的破坏：…`。**生成面**：文件 · 节 · 小节 · 行类型与编号 · 该行原文，全部由脚本从 `roles/*.md` 抄出。

**fail closed 三类**（`render()`）：key 命中 0 处 / 命中 ≥2 处 / 目标文件不存在（该文件全部 key 一起失效）→ **非零退出并逐条列出**。

### D2 `roles/ledger-custodian.md`（第 10 个角色，214 行）

- frontmatter `role: ledger-custodian` + 标准注入契约段（含"第 1–2 层"）；8 个必需节齐全。
- **§4 九个小节**：4.1 唯一动作序列（重跑，不手写）｜4.2 生成区 diff 三分类（新增 / 删除 / 位置或内容变化）｜4.3 key 失效与歧义只报回不迁就｜4.4 手工编辑生成区的识别与恢复｜4.5 人写列的边界｜4.6 批次顺序与合并｜4.7 什么算"必须处理"｜4.8 交付语言给 diff 与判据｜**4.9 存量 key 的意图回读（首次接管时，见 §③）**。每节都带触发条件 / 步骤 / 判断依据 / 2 条反例。
- **硬边界写进文件**：不得手工编辑生成区；key 找不到时不得改 key 迁就，只能报回产出方或改人写的处置列；不出具任何判断类结论。

### D3 接线

| 处 | 内容 |
|---|---|
| `scripts/check-library.py:107-109` | `ROLE_IDS` 加 `ledger-custodian` |
| `scripts/check-library.py:165` `run_ledger_check()` | **P5′ 改为调 `render-ledger.py --check`**；原先那套自带锚点正则解析**已删除**（它漏解析粗体形态） |
| `scripts/check-library.py` `read_without_generated()` | 生成区是派生副本，不参与"某段文字恰出现一次"这类计数（否则原文被引用一次=两处） |
| `closure.md:41` | A3 行：输入 `changed_files` `key_set` `batch_id` → 输出 `region_diff` `broken_keys` `moved_steps` `regenerated_at` |
| `pipeline.md:17`、`:148-149` | 记录侧边 `driver → ledger-input → ledger-custodian → ledger-report → driver`，并写明**不参与实现与判断链**（全文仍 150 行） |
| `roles/driver.md:50`、`:299` | 副收据 `ledger-report` ← custodian；产出 `ledger-input` → custodian |
| `README.md:52`、`AGENTS.md:35-36` | 角色数 9 → 10 |

---

## ② V1–V7 原样输出

```
$ python3 scripts/render-ledger.py                                     # V1
render-ledger: 已刷新生成区（215 个 key，1125 条规则行可定位）
V1 EXIT=0

$ python3 scripts/render-ledger.py --check                             # V2
render-ledger --check: OK（215 个 key，生成区与重新生成的结果逐字一致）
V2 EXIT=0

$ # V3 正控制：临时副本删掉一条被 key 引用的角色规则（roles/implementer.md §4.4 步骤 6 注释判据）
$ python3 scripts/render-ledger.py
render-ledger: FAIL（1 个 key 有问题，fail closed）
  - key 找不到：@注释只写 why，
V3 EXIT=1

$ # V4 歧义控制：把 key 短语原样复制进 roles/oracle.md 的第二条规则
$ python3 scripts/render-ledger.py
render-ledger: FAIL（2 个 key 有问题，fail closed）
  - key 有歧义（命中 2 处）：@既有约定的破坏： → roles/oracle.md（§4.1「触发条件：满足任一即启用」 · 判断依据）；roles/reviewer.md（§4.3「对抗性提问清单」 · 第 5 步）
  - key 有歧义（命中 2 处）：@既有约定的破坏：它有没有破坏这个仓库里既有的命名、 → roles/oracle.md（§4.1「触发条件：满足任一即启用」 · 判断依据）；roles/reviewer.md（§4.3「对抗性提问清单」 · 第 5 步）
V4 EXIT=1

$ # V5 篡改控制：临时副本里把生成区一处「第 6 步」手改成「第 7 步」
$ python3 scripts/render-ledger.py --check
render-ledger --check: FAIL（生成区与重新生成的结果不一致——有人手工改过生成区，或规则已移动）
V5 EXIT=1

$ python3 scripts/check-library.py | grep -E "P5′|合计"                 # V6
[PASS] 台账落点 P5′：render-ledger --check         退出码 0｜render-ledger --check: OK（215 个 key，生成区与重新生成的结果逐字一致）
合计: 26 项通过 / 0 项失败 / 26 项检查
V6 EXIT=0

$ bash scripts/identity-selftest.sh | tail -2                            # V7
----
合计：15 通过 / 0 失败（被测实现：…/scripts/ws-identity.sh）
V7 EXIT=0
```

**额外（D1 第三类 fail closed：目标文件不存在）**

```
$ mv roles/oracle.md /tmp/oracle.bak && python3 scripts/render-ledger.py
render-ledger: FAIL（11 个 key 有问题，fail closed）
  - key 找不到：@只拿两样输入：
  - key 找不到：@只拿两样输入：产物本身（候选内容、
  - key 找不到：@不要作者的结论、
  - key 找不到：@写一个能区分选项的实验，
  - key 找不到：@写裁决结论：
  - key 找不到：@这份职责不消失：
  - key 找不到：@问："什么样明显错误的实现，
  - key 找不到：@本次改动改变接口形态 / 状态归属 / 权限 / 数据语义
  - key 找不到：@问："什么样明显错误的实现，仍能通过当前的检查？
  - key 找不到：@本次改动改变
  - key 找不到：@不得当唯一闸门。
EXIT=1
```

---

## ③ 6 处错误落点：改写后的回读结论（脚本只保证"存在且原文被引出"，语义靠人判）

| # | 行 | 改后的 key → 生成出的落点与原文 | 语义回读 |
|---|---|---|---|
| 1 | `:263` 注释与文档（原写 `implementer §4.4` **步骤 4**） | `@注释只写 why，` → `roles/implementer.md` §4.4「增量纪律与范围自律」 · **第 6 步**（注释只写 why、能编码进类型／运行时／检查的约束不写成注释、决策级 why 进设计交付物）；`@既有约定的破坏：…` → `reviewer` §4.3 第 5 步（审查侧同步审注释纪律）；`@按强度排序选择不变量的落点：…` → `architect` §4.3 第 2 步；`@按固定顺序写：…` → `architect` §4.7 第 1 步 | **也对**。四条落点各自引出的原文就是该条机制要求的动作；步骤号由脚本从文件里读出，不可能再写错 |
| 2 | `:143-156` 计划文档不许覆盖（原落点是"不适用…"一条无关规则） | `@我不可以：改变模块接口契约或重新设计系统` → `planner` §5 权限边界整段，原文含"**覆盖他人未完成的计划文档**" | **也对**（原落点指错规则，现已指到真正写着这条禁令的那一行） |
| 3 | `:57-90` 四问 / 每问自带默认值 / "Stop at four" | `@每个问题附上我的推荐答案` → `driver` §4.1 第 3 步 | **部分对，已如实收窄**：处置从"改写"细化为「只落地『每问自带推荐答案』与『按 frontier 分轮』」，理由写明「**不超四问未落地**——本库用 frontier 而非问题数量设界」 |
| 4 | `:173-189` 保存点模式 | `@每一步之后项目必须能构建、既有检查必须通过` → `implementer` §4.4 第 2 步 | **部分对，已如实收窄**：处置改为「改写（只落地『不留坏状态』）」，理由写明「**回到上一个固定点再查**未落地」 |
| 5 | `:236-258` 控制台零告警 | **无落点** | **改为"不采纳（未落地）"**：本库未把"控制台零告警"写成判据，浏览器类验证只要求断言外部可观察结果。原先标"保留"是夸大 |
| 6 | `performance-optimization/SKILL.md:30-39` 五步循环 | **无落点** | **改为"不采纳（未落地）"**：五步循环未落成角色动作；本库只落地噪声带与"先量后说"（`verifier` §4.5）。原先标"保留"是夸大 |

**另外 3 处（回读时新发现，一并修）**：`documentation-and-adrs/SKILL.md:104-135`（原落点指到 `implementer §4.4` 第 1 步「增量纪律」——迁移时粗体 `**步骤 6**` 未被正则捕获而落到节内第一条规则）；`§6.1 :73`（多挂了一条 planner 数字门禁的无关落点）；`§6.1 :145`（原落点指到 `driver §4.3` 能力探测，与"方案审查门"无关 → 改为 `driver §4.7` 判断依据，并写明本库不采用文件数/行数门）。

---

## ④ 未做项与原因（如实）

1. **只做了这批 key 的意图回读，没有对全部 193 行做成规模语义核对。** 脚本能保证"key 存在、原文被引出、步骤号真实"（构造上不可能再出现"写错步骤号"），但**"这条 key 的意图对不对"脚本判不了**——成因是迁移时把旧的人写锚点自动转成 key，凡是旧锚点用了粗体形态（`**步骤 6**`）的行，都会落到"该节第一条规则"上。我已修掉能逐行判定的 9 行（含 oracle 点名的 6 行），**其余行没有逐条回读**。
   - 处置：新增 `roles/ledger-custodian.md §4.9`（存量 key 的意图回读），把这件事写成常驻职责与三条允许的处置；并在 `check-library.py` 的输出里保留"判不了"边界说明。
2. **生成区现在是 1076 行**（`SOURCES.md:474-1549`），比原先的人写落点列长。这是"能算出来的不写第二遍"的代价：人写面变短（每行只剩 `@key`），派生面变长且不可手工改。
3. **key 短语的可读性不齐**：多数是自然短语（`@注释只写 why，`、`@既有约定的破坏：…`），少数因为短语必须全库唯一而较长（如 `@把改动固定成一个明确身份（commit:<sha> / tree:<sha> / ws:v1:<sha256> 三者之一，`）。没有做人工润色——润色会改变 key 字符串，需要重跑并重新回读。
4. **未 commit**（按要求停笔等冻结）。
5. 过程性副作用：核对脚本时产生过 `scripts/__pycache__`，导致 `check-library.py` 读二进制崩溃；已删，并让扫描只读 `.md/.sh/.py/.tsv` + 跳过 `__pycache__`，`.gitignore` 也补了两行。

---

## ⑤ 最终退出码

```
$ python3 scripts/check-library.py ; echo $?
合计: 26 项通过 / 0 项失败 / 26 项检查
0
```
