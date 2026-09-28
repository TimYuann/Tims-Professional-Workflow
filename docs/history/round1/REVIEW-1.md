# REVIEW-1 · planner/reviewer 对 Round 1 交付的审查

审查者：planner session（未参与实现）
对象：worker 交付的工作树（未 commit）
方法：**自己重跑 + 自己植入缺陷**（不采信交付方转述的读数）
一句话结论：**结构层达标；"闭环"这一项的机械保证在大面积空转，必须返修后才能冻结给独立 verifier。**

---

## 1. 阻断项

### B1 · 闭环检查 2/3 空转，且把空转报告成"全部成立"

**现象**
`check-library.py` 的「闭环：收据字段 ⊆ 产出方字段」只解析**表格形态**的字段声明（正则 `^\|\s*\`field\``），而 9 个角色文件里有 **24 个收据，其中 16 个用的是散文式声明**（`字段：\`a\` ｜ \`b\`` 一行）。这 16 个收据的字段集**恒为空集**，于是"⊆"对它们**恒真**。

**证据（正控制，我自己跑）**
把 `roles/verifier.md` §2 副收据 `review-verdict` 的 `object` 改成 `objectZZZ`（产出方 `roles/reviewer.md` §3 仍声明 `object`）→
```
[PASS] 闭环：收据字段 ⊆ 产出方字段    全部成立
EXIT=0
```
应当报红的边没有报红。

**盲区清单（16 个收据，含最关键的几条边）**
`architect←driver(task-card)`、`driver←investigator(investigation-report)`、`driver←oracle(oracle-ruling)`、`driver←integrator(integrated-baseline)`、`implementer←architect(design-proposal)`、`implementer←driver(task-card)`、`implementer←investigator(investigation-report)`、`implementer←reviewer(review-verdict)`、`integrator←implementer(candidate)`、`integrator←reviewer(review-verdict)`、`oracle←implementer(candidate)`、`oracle←architect(design-proposal)`、`planner←investigator(investigation-report)`、`reviewer←planner(slice-plan)`、`reviewer←architect(design-proposal)`、`verifier←reviewer(review-verdict)`。

**为什么阻断**
Owner 的标准第 2 条就是"工程上的闭环"。这项检查正是它的机械保证；现在它报的是"全部成立"，而实际参与校验的收据不到 1/3。**空转被报成全绿，比没有这项检查更坏**——它让人以为闭环已经被验证过。

**最小修复**
1. 解析器同时识别散文式 `字段：` 行（或把 16 处收据统一改成表格形态）。
2. 输出里**打印真实覆盖面**，例如 `闭环：收据字段 ⊆ 产出方字段 16/24 收据参与校验`；空转分子分母必须可见。

---

### B2 · 闭环矩阵主链与角色契约之间没有交叉校验

**现象**
`closure.md` 的维护规则写着"本表字段与角色文件不一致时，以角色文件为准…`scripts/check-library.py` 会同时检查两处"。实现上，主链只做了**矩阵内部**的相邻行比对（第 N 行输入 ⊆ 第 N−1 行输出），**没有**把矩阵字段与角色文件的 §2/§3 对账（按需表有对账，主链没有）。

**证据（两处独立突变，各自新副本）**
| 突变 | 期望 | 实测 |
|---|---|---|
| 把 `closure.md` 主链里 `red_flag_screen` **一致改名**（矩阵内部仍自洽，但角色文件里无此名） | 报红 | **无 FAIL，EXIT=0** |
| 把 `roles/reviewer.md` §3 的 `coverage` 改名（矩阵仍引用 `coverage`） | 报红 | **无 FAIL，EXIT=0** |
| （对照）把 `closure.md` 第 6 行输入 `object` 改成 `objekt` | 报红 | ✅ FAIL：`第 6 行输入 ['objekt'] 不在上一行输出里` |

即：矩阵**内部**相邻关系有牙，矩阵**与角色契约之间**没有牙。

**最小修复**
矩阵每行的输入/输出字段，必须能在承接角色的 §2/§3 里解析到；解析不到即报红。否则就把 `closure.md` 那句话改成与实现一致的措辞（二选一，不许让文档强于实现）。

---

### B3 · `机械等价` 是一条没有判据的旁路

**现象**
`roles/driver.md:215` 要求"写下一行等价证明（同语义、同判据、机械等价）"；`closure.md` 第 5 行（审查）的"可跳过条件"是"只有机械等价的小改，且卡上已写出等价证明（机械等价的判据必须可复核）"。
但**"什么算等价证明"全库无定义**。这是唯一一条绕过独立审查的通道，却没有门槛。

**为什么阻断**
跳过独立审查是本库最硬的一条纪律；唯一允许跳过它的通道必须有一个**可复核**的判据，否则它一定会被当成"我觉得这个改动很小"的托词。

**最小修复**
把证明定义成**一条可重复执行的命令 + 它的输出**，例如：
- 纯重命名 / 搬文件 → 符号级 diff（`git diff -M --stat` 之外，需给出"符号集合不变"的比对命令与输出）；
- 剥除注释或 docstring → 剥除后逐字相同的比对命令与结果（AST 级或文本级皆可，但要写出命令）。
**写不出命令 = 不算证明 = 必须开独立审查。**

---

### B4 · 独立判断在能力缺失时没有停机规则

**现象**（交付方自己报的第 ③ 条，我核对后确认成立）
`closure.md` 四条必答路径与 `roles/oracle.md` §4 都写了"必须另起 fresh 会话""不得由实现者本人承担"。但**没有写"如果一个独立会话都开不出来，应该怎么办"**。

**为什么阻断**
压力会磨掉硬边界：真到了开不出会话的时候，现场就会退化成"我自己判断一下，然后记成已做过独立复核"。而"实现者 ≠ 判断者"是本库唯一一条不可让的硬约束。

**最小修复**
补一句硬规则，并把它接进 Driver 的能力探测：
> 当本轮环境不提供独立会话能力（由 Driver 在装配阶段检测并声明）时，**本轮的判断类结论最高只能是 `UNVERIFIED`**，或由 Owner 明确书面接受风险；**不得记为 PASS**。
即：能力缺失只降低结论的等级，不降低纪律的要求。

---

## 2. 非阻断项

### N1 · 能力探测检查是字面匹配，检查项名字强于能力
`CAPABILITY_MARK = "检测当前工作环境提供哪些能力"` 是字面串。我在 `roles/driver.md` 追加一句语义等价的能力探测（"开工前要再看一次能不能开独立会话、能不能隔离工作区、有哪些模型档位"）→ 仍报 `能力探测句恰好一处且在 driver.md`。
**最小修复**：把该项改名为它真正做的事（"指定措辞出现一次"），或改成多词命中计数（独立会话 / 会话间通信 / 工作区隔离 / 模型档位）。

### N2 · §4 的实质深度不可机械判定，但没声明这条边界
反实现挑战：把 `roles/oracle.md` §4 整段换成空话 + 两条写在 §4 内的名义反例 → **13/13 全绿、EXIT=0**。
这不是缺陷（机械检查判不了深度），但必须在 checker 输出里写明"本检查**不**判定 §4 的实质深度"，否则它给出的信心是假的。深度这件事只能由独立审查者的**引用忠诚度抽查**承担。

### N3 · 吸收广度欠账（已如实标注，可接受）
pstack 17 个 `principle-*` 只读了 6 个；`SOURCES.md` 已按 `[全文]/[局部]/[仅目录]` 如实标注，并另列「本轮明确不吸收的机制」。属可接受欠账，下轮补。

---

## 3. 我复核过、确认合格的部分（避免只报坏消息）

| 项 | 我做了什么 | 结果 |
|---|---|---|
| 退出码有效性 | `python3 scripts/check-library.py >/tmp/o 2>&1; echo $?` | ✅ 有失败时 `EXIT=1`。**注**：我第一次测出 EXIT=0 是我自己 `| tail` 管道的 bug，交付方"EXIT=1"的自述正确 |
| 结构类检测有牙 | 自植入 5 处缺陷（缺节、缺注入契约、死链、harness 名、反例清零） | ✅ 全部抓出 |
| 闭环矩阵**内部**相邻关系 | 第 6 行输入 `object`→`objekt` | ✅ `FAIL：第 6 行输入 ['objekt'] 不在上一行输出里` |
| 引用忠诚度（我的抽样） | `how/SKILL.md:17-20`、`how/references/explorer-prompt.md:30`、`why/SKILL.md:78`、`why/SKILL.md:36-48` 逐行核对 | ✅ **4/4 忠实**（"When in doubt, take the simple path."、"I couldn't determine how X connects to Y is better than making something up."、"Document the null, don't skip the search." 均在引用行内） |
| 冲突裁决表 | `grep "综合两者\|取长补短\|两者兼顾"` | ✅ 只命中一句元描述（声明"不给综合两者"），实际 9 条裁决均单选 |
| 工具解耦 | 扫描范围内 harness 字样 | ✅ 0 命中；能力探测仅 `roles/driver.md` 一处 |
| SOURCES.md 诚实性 | 结构 + 抽样 | ✅ 三个 clone 的 SHA 实取；`NOT ABSORBED` 单列；明确写了本仓对"几个上游"说法不一致 |

---

## 4. 我的核验边界（不许省）

- 我的抽样只覆盖 4 条 SOURCES.md 引用、5 类结构缺陷、6 类突变；**角色级、逐条主张的引用忠诚度抽查（investigator/reviewer/oracle）我留给了独立 verifier**，我没有做。
- 我**没有**逐字读完 9 个角色文件（约 1830 行）与 436 行 SOURCES.md；我读的是抽样段落 + 机械检查 + 定向突变。
- 我只验证了 checker **抓得到什么**，没有验证它**该抓而没想到的类别**（除了 N2 的深度这一条）。
- 我对"方法是否真能在真实开发里用得上"**没有验证**——这需要一次真实任务，不是读文件能得出的。
