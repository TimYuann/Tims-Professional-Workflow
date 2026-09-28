# REPORT · round-3 独立复审（verify）

被审对象：`tag v2.0.6` / `commit eaa8eb2`（「fix(v2.0.6): P0 概念拆分 + P1 假检查逐条处理 + 测量纪律三条」）
对照物：`.pi/review-v2/REPORT-round2-tpw-verify2.md`（FAIL 60/100）
取证方式：全部在 `/tmp` 的独立检出上做，未在仓库工作树上改过任何文件。
三态口径：`PASS` / `FAIL` / `UNVERIFIED`。环境故障既不算 `PASS`，也不判成产品缺陷。

**证据边界声明**：本报告没有把 `.pi/injection/REPORT-0928-impl.md` 当作证据，一个字都没引用它的结论或数字。
我读了 `harness.py` / `suite.py` 的**源码**（因为「审注入台」本身是被交代的任务），把它当「该去查哪里」的线索。
上一轮报告我当对照物读，不当结论读。

---

## 0. 两个必须先说的事件

### 0.1 复审期间仓库在动，`v2.0.6` 这个 tag 被移动过

我 15:35 开始时：`HEAD = eaa8eb2`，`v2.0.6` 是**轻量 tag** 指向 `eaa8eb2`。
我 15:36 前后再查：新增了 `29a50e4`，`v2.0.6` 变成**附注 tag** 并指向 `29a50e4`。
再往后 `HEAD` 又变成 `8825b0e`，而 `v2.0.6` 仍停在 `29a50e4`。

```
eaa8eb2  fix(v2.0.6): P0 概念拆分 ...        ← 本报告的被审对象
29a50e4  docs: 故障注入表按 v2.0.6 实测重生成  ← 只改 README.md，未触产品面
8825b0e  chore(A9): 补记 v2.0.6 收口 12 行     ← 只改 .decisions/ledger.tsv
```

这不是我造成的，我全程只读 + 在 `/tmp` 副本上操作。事实后果有两条：

1. **「tag v2.0.6」在复审窗口内不是一个稳定句柄。** 交付里凡是写「v2.0.6 已复审」的，指的必须是 `eaa8eb2` 这个 commit，不是 tag 名。
2. 我按纪律把被测对象钉死在 `eaa8eb2`（每轮运行前重新断言 `HEAD`），所以本报告的所有数字都只对 `eaa8eb2` 成立。
   顺带复验了 `29a50e4`：`19/19 + 7/7 + render 12/12`，同样全绿——所以我的判定不是针对一个半成品中间态。

### 0.2 `upstreams/` 被 gitignore，这决定了后面一半的判定

`.gitignore:1` 是 `upstreams/*/`。所以**任何 `git clone` 出来的干净仓库都没有 `upstreams/` 目录**。
这一点同时决定了「下游能不能跑」和「C9 到底测没测东西」，是本轮最关键的环境事实。

---

## 1. 基线（先测基线，再看别的）

在 `git clone` + `checkout eaa8eb2` 的**真实**干净检出上：

| 检查 | 结果 |
|---|---|
| `python3 scripts/render.py --check` | `OK（12 个派生文件逐字一致）` |
| `python3 scripts/check-closure.py` | `合计: 19 项通过 / 0 项失败 / 0 项跳过 / 19 项检查`，exit 0 |
| `python3 scripts/check-consistency.py` | `合计: 7 项通过 / 0 项失败 / 7 项检查`，exit 0 |

**基线判定：`PASS`。** 上一轮阻断条件 B1「clean checkout 根本跑不出全绿」在**退出码层面**已经修好。

但基线绿不等于检查器在测东西。下面 §4 的 A1/A2 是一组受控对照，说明 C9 的绿灯里有一部分是空的。

另有一条基线层面的环境依赖：`git archive` 导出（无 `.git`）跑 C1 会红，且消息是
`当前 commit 上没有 tag——打了 tag 之前不能算一个 release`。真实原因是**没有 git 元数据**，
不是「没打 tag」。这条我判 `FAIL`（违反本库自己的硬边界 3：环境故障应判 `UNVERIFIED`），
但它不是产品缺陷，是 C1 少了一个 `skip` 分支。

---

## 2. 结论：**不放行** UCBIP full-size 试运行

不放行，但**离放行很近**，缺口是三条 P1，全部是小改动（见 §6）。

理由不是「结构还塌着」——结构没塌，二审诊断的病基本治好了。是这三条：

1. **A9 台账的「拒绝写临时目录」是假的，且这个假法正好命中试运行场景。**
   `docs/ledger.md:71` 用表格无条件承诺「写入临时目录 → 拒绝（退出码 3）」。
   实测：`cd ~/x && ln -s /tmp tmpalias && ledger.sh tmpalias/evil.tsv ...` → **exit 0，文件真写进了 `/tmp`**。
   一次 full-size 试运行极可能就发生在临时工作区里，而 A9 是「全程记录不丢」这条纪律的唯一载体。
   在试运行里最可能用到的形状上，唯一挡着「记录丢在临时目录」的那道闸是漏的。
2. **tag 里带着一份自相矛盾的安装说明。** `README.md:248-255` 教「在下游仓库里 C7/C9 必须 SKIP」，
   两份 coldstart（本轮刚改对）教「下游是 PASS，SKIP 不可达」。`skip=True` 全库无一处使用，**coldstart 是对的，README 是错的**。
   下游按 README 装，会去追一个不会发生的 SKIP 故障。（这条维护者已经自己在 A9 台账里记成待办，见 §5 第 1 条。）
3. **对外呈现为 PASS 的能力，有一块在真实消费路径上是死代码。** C9 名为「来源真实存在（锁 + 实物对照）」，
   而实物对照整段挂在 `if (ROOT / "upstreams").is_dir()` 里面——下游永远进不去（§4 A1/A2）。

为什么不是「先放行、边跑边修」：这三条里有两条会**主动误导**试运行的执行者（README 教错、A9 承诺不成立）。
让试运行去撞这两个，比先花半小时改掉更贵。

---

## 3. 逐条对上一轮阻断条件的独立判定

任务书写「8 项」，实际列了 9 条，我按 9 条逐条判。

| # | 二审阻断条件 | 本轮判定 | 我的独立依据 |
|---|---|---|---|
| 1 | B1 clean checkout 跑不出全绿 | **表面修好，实质降级** | 真 clone `eaa8eb2` → 19/19 + 7/7 + render 12/12。但修法是让 C7/C9 退到「只核锁文件」而不是补齐上游；受控对照 A1/A2 证明实物对照在下游从不执行。 |
| 2 | B2 版本身份假绿 | **已修**（带一条环境依赖） | C1 现在核 tag；我的 F2 注入（改 VERSION 不改 tag）→ C1 红，`PASS`。残留：`.git` 缺席时判 FAIL 且消息误导。 |
| 3 | B3 对象身份字段没进角色与技能合同 | **核心机制修好，覆盖面有洞** | C15 是真交叉核对，D1 注入抓得住。**但 C15 的门控完全取决于「字段名是否出现在某阶段 exit_criteria」**；40 个产物字段只门控 19 个，未门控 21 个含 `A8.scope`。D3/D4 受控对：`A8.scope` 无人教 → 全绿；给它加一条判据 → C15 立刻红。 |
| 4 | B4 P5/P6 的 A3 写权冲突 | **实例修好，类别未覆盖** | `roles/verifier.md:98` 已写「不更新 `A3`」，`skills/verification-suite.md:50,54` 同步。**但我把 B4 原样注回去（改成「由我更新 `A3.freshness`」），全套检查器零红。** |
| 5 | A9 临时目录拒写可被 symlink 绕过 | **未修** | 实测复现：从非 `/tmp` 目录用相对路径经 symlink 写入 `/tmp`，exit 0，文件真在 `/tmp/evilspace/x.tsv`。`docs/ledger.md:71` 的无条件承诺仍写着。 |
| 6 | C13 与 S4 过度声称 | **已修** | C19+C20 之类不管，只看这条：C13 已改名为「越权写由**显式声明**判定」，S4/S3/S7 的 detail 尾部都带 `边界：` 明写抓不到什么。措辞现在与能力相符。 |
| 7 | coldstart 两份打架 | **两份之间修好，第三处未修** | `docs/coldstart.md:57` 与 `skills/coldstart.md:48,51,65,77,79` 五处一致地说「下游是 PASS，SKIP 不可达」，与代码相符。**但 `README.md:248-255` 说相反**，且已随 tag 发布。 |
| 8 | frontend-ui 与 DoD | **已修** | `addy:frontend-ui-engineering` 处置改为 `into: [user-interface-engineering]`，新技能正文来源段列对路径，且组件架构/状态/设计系统/响应式/加载/收尾闸门六个话题都在正文里（逐词命中 13/18/4/7/3/6）。DoD 侧 `skills/constraint-driven-development.md:76-91` 真教了 `scope: project` 与 `scope: task` 两层填法。 |
| 9 | 18 种产物形态无箭头 | **15/18** | `embodiment` 加在 A1–A9 上（正确的落点）。逐条比对二审 §5.2 的 18 行：15 行能按 `@技能id` 找到归属；`arena`、`git-workflow-and-versioning`、`teach` 三行仍无箭头。 |

---

## 4. 我自己造的注入：对照表

我没有只跑它自带的 28 条。我另写了 `/tmp/rev3/{harness.py,suite.py}`，
针对它栽过的同一个病做了 6 处加固（M1–M6），然后造了 14 条注入 + 3 条台外实验。

### 4.1 我方 harness 的加固点（以及为什么自带那台不够）

| | 加固 | 针对的病 |
|---|---|---|
| M1 | 被测对象钉死在 `eaa8eb2`，每轮运行前重新断言 `HEAD` | 自带那台 `SRC=工作树`，`git_rev()` 只出现在 assert 消息里，基线绿时根本不打印——「测于哪个 commit」靠人记得看报告 |
| M2 | 每条注入自带 `probe(d)` **语义后置条件**，不成立即判 `UNVERIFIED` | 自带那台只看「整树指纹变了没」，见 §4.3 |
| M3 | 内置负对照，证明 M2 不是摆设 | 自检自检 |
| M4 | exit 非 0/1 或含 traceback → `CHECKER_CRASHED` | 崩了当绿 |
| M5 | 解析全部三态 + 比对前后检查项集合 | 自带那台只收 `[FAIL]` 行，检查项整个消失会被静默 |
| M6 | 「合计」行与逐行明细对账 | 摘要说全绿、明细其实没跑 |

M6 在我自己的 harness 上先炸了一次：两个检查器的输出被我合并统计，却只匹配了最后一条「合计」行。
护栏抓到了我自己的 bug——这算它有效的一次证据。

### 4.2 14 条注入的结果

`PASS` = 被期望的检查项抓住；`FAIL` = 漏报（真缺陷）；`设计内` = 本就不该红。

| 注入 | 做了什么 | 期望 | 实际 | 判定 |
|---|---|---|---|---|
| `A1-c9-corrupt-lock-NO-upstreams` | 篡改锁文件里某个上游的 sha256，**干净 clone（无 upstreams/）** | C9 红 | 全绿 | **FAIL** |
| `A2-c9-corrupt-lock-WITH-upstreams` | 同一处篡改，挂了 upstreams/ 的树 | C9 红 | C9 红 | PASS |
| `B1-ribbon-only-on-phaseless-role` | 把 `context` 横切带改成 `always:false` + 合法 `applies_to`，而它**只挂在 `driver` 身上，`driver` 不参与任何阶段** | C19/S7 红 | 全绿 | **FAIL** |
| `B2-ribbon-carries-no-skill` | 把 `expression` 横切带的 `skills` 清空 | C19 红 | 全绿 | **FAIL** |
| `C1-principle-ghost-source` | 原则的「来源：」行挂一个锁文件里没有的上游 | 红 | 全绿 | **FAIL** |
| `C2-principle-drop-source` | 整条删掉一个原则的「来源：」行（9→8） | 红 | 全绿 | **FAIL** |
| `C3-policy-flip-UNVERIFIED-to-enforced` | 把 `provenance_policy` 里 roles/scripts 的 `UNVERIFIED` 翻成 `enforced` | 无 | 全绿 | 设计内 |
| `D1-A4-scope-untaught` | 抹掉 architect 正文与其技能里所有 `` `scope` `` | C15 红 | C15 红 | PASS |
| `D2-A4-scope-decoy-mention` | 删掉 `scope` 的**真实教学**，只留一句语义无关的 `` `scope` `` 提及 | C15 红 | 全绿 | **FAIL** |
| `D3-A8-scope-untaught-everywhere` | 抹掉 verifier 角色文件 + 它**全部 5 个**提到 `scope` 的技能 | C15 红 | 全绿 | **FAIL** |
| `D4-A8-scope-gated-THEN-untaught` | **对照**：先加一条引用 `A8.scope` 的判据，再抹掉教学 | C15 红 | C15 红 | PASS |
| `E1-noop-injection` | 只 append 一句无害注释（负对照） | — | 全绿 | 设计内 |
| `F1-new-ribbon-fully-wired` | 完全合规地新增一条横切带 | 无 | 全绿 | 设计内 |
| `F2-VERSION-vs-tag` | 改 `VERSION` 不改 tag | C1 红 | C1 红 | PASS |

统计：**PASS 4 ／ FAIL 8 ／ 设计内 2**。

**A1/A2 与 D3/D4 是两组受控对照**，是本轮最有说服力的两条：
- A1/A2 同一处篡改，只因树里有没有 `upstreams/` 而一个红一个不红 → C9 的实物对照在真实消费路径上不存在。
- D3/D4 同一处缺失，只因判据里有没有出现字段名而一个不红一个红 → C15 的覆盖面由判据字符串决定，不由字段重要度决定。

### 4.3 台外实验三条

**(a) B4 原样注回去** —— `roles/verifier.md` 的「4. **不更新 `A3`。**」改成「4. **由我更新 `A3.freshness`。**」，
`check-closure` + `check-consistency` 全程：**新增红 = 无**。
C13 至今不读角色正文，所以 B4 是被散文治好的，不是被检查器治好的。

**(b) A9 symlink 绕过** —— 复现成功，exit 0，写进了 `/tmp`。（已清理我自己的测试目录。）

**(c) 攻击自带注入台** —— 造一条**只 append 一句无害注释**的注入，树确实变了，别的事没破坏：

```
自带 harness：
    整树指纹：变了（护栏放行）
    检查器新增红：无
    它给出的判定：✘ 漏报
```

它的指纹护栏问的是「文件变了吗」，不是「缺陷引入了���。于是一条坏注入在它的账本上变成了一条
**指控检查器缺陷的假证据**。这正是它自己在注释里认领要治的那个病，复发在测量工具自己身上。

### 4.4 我自己出过一次错，记录在案

D3/D4 第一版我只抹了 2 个文件，而 C15 的 `producer_text` 覆盖产出方**拥有的全部技能**（`scope` 实际散在 5 个技能里），
后置条件没达成却被记成「漏报」。我的 M2 只查了 `roles/verifier.md`，太弱。
修正后重跑才得到上表的 D3/D4。**记这一条是因为它正是我批评自带 harness 的那个错**——
我的第一版探针也不足以证明「缺陷真的引入了」。

---

## 5. 同一个病，有没有第七次

**有。不止一次，我找到四处。**

那个病的形状是「声明了，但没人产出」/「声明了要测，但那个测量本身没被测过」。

| # | 第七次长在哪 | 声明 | 实况 | 证据 |
|---|---|---|---|---|
| **1** | `provenance_policy.principles` | `level: clause, status: enforced, carrier: 原则每条的「来源：」行` | **没有任何检查器读原则的「来源：」行**。C20 只管技能；C9 只核 registry 的 `sources` 是否在锁文件里；C10 只管技能 | 注入 C1（挂幽灵路径）、C2（整行删掉）双双全绿 |
| **2** | `provenance_policy` 自身的 `status` 字段 | 声称 `roles/scripts = UNVERIFIED`，并给出 `gap` 说明 | **这个字段不可falsify**：把它从 `UNVERIFIED` 翻成 `enforced`，没有任何检查器会红。它连「被检查」这件事本身都没有承载体 | 注入 C3 |
| **3** | C9 的名字「锁 + 实物对照」 | 对照实物存在性 | 实物对照整段在 `if (ROOT/"upstreams").is_dir()` 里，而 `upstreams/*/` 被 gitignore → **下游永远进不去**。绿灯是「只核锁文件」的绿灯 | 注入 A1 vs A2 |
| **4** | 自带注入台的指纹护栏 | 「注入没改到文件就拒绝出数」（针对第六次） | 指纹只证明「树变了」，不证明「缺陷引入了」。坏注入照样出数，并被记成「漏报」 | §4.3(c) |

同时要说清楚**这一轮真正治好的**那一次，别让上面的清单盖过它：
C15 是货真价实的真交叉核对——它明确废掉了「`notes` 里写一句『由 X 填』就是免死金牌」这条短路，
要求产出方的**正文里真的教了**。D1/D4 两条注入证明它一旦门控住就真的抓得住。
`A4.scope` 这个本轮新增的字段，机制上是接上了的。

**为什么第 1 条最要紧**：它不是「少测了一个字段」，是 `provenance_policy` 这份新增文档
**整段核心承诺（段落级来源可核）里，有一半（principles）挂着一个不存在的检查器**。
而这份文档正是本轮用来回应「owner 要求每一段话有来源」的交付物。
`roles/scripts` 标 `UNVERIFIED` 是诚实的；`principles` 标 `enforced` 不是。

---

## 6. 本轮做错或做过头的地方

按要求，这一节不许空。以下每条我都能给出可执行的判据。

1. **README 是同一个错的第三处残留，没改。**
   两份 coldstart 改对了，README 改成了相反的教法，还随 tag 发了出去。
   维护者已经在 A9 台账里把它记成 P1 待办（`README.md:261-267… scribe 自行发现，driver 清单外`，
   台账是在 `29a50e4` 之后写的，所以那里用的 `261` 是加长 README 后的行号；在被审的 `eaa8eb2` 上对应 `248-255`），
   但**登记待办 ≠ 已修**，而 README 是最常被读的那份。
   判据：`README.md:248-255` 的措辞与 `docs/coldstart.md:57` 一致。

2. **B1 的修法是「让检查降级」而不是「把能力补齐」，但对外呈现为 PASS。**
   C7/C9 在下游能 PASS，是因为检查对象从「上游实物」退到了「随包分发的锁文件」。
   这是一个合理的工程选择，但它**缩小了检查能力**，而缩小量没有在 C7/C9 的 detail 里说出口
   （detail 只说「101 个上游 skill 索引（锁文件）」，读者容易读成「101 个都核对过了」）。
   判据：C9 的 detail 在无 `upstreams/` 时显式写明「未做实物对照」。

3. **B4 是改散文治好的，C13 的盲区原地不动。**
   `roles/verifier.md:98` 现在写对了，但把这句话改回去，没有任何检查器会红。
   也就是说这类「角色正文与 registry 写权冲突」的缺陷，下次照样能悄悄进来。
   判据：一条注入（把 `不更新 A3` 改成 `由我更新 A3.freshness`）能让至少一项检查红。

4. **为了消掉 P5/P6 的 A3 冲突，把 P6 里那条 A3 判据整条删了。**
   冲突确实没了，但 `A3.freshness` 从此**不被任何判据门控**，落进那 21 个未门控字段里。
   「能力地图已保鲜」在 README 的阶段表里还写着（`README.md:77`），
   而现在没有任何判据要求它保鲜。二审建议的另一个修法（把 `architect` 装进 P6）没走。
   判据：`A3.freshness` 要么被某阶段判据门控，要么 README:77 那行改掉。

5. **C12 与 C20 对同一批 3 个技能给出互相矛盾的标签，而且两条都 PASS。**
   C12 输出「3 个原创技能已标注」，C20 输出「0 个原创／3 个借鉴」。
   同一套检查器里「原创」有两个意思（`origin: library` vs 正文出现「本库原创」），
   而**没有任何交叉检查**。`skills/tier-sizing.md` 的来源段同时写着「本库原创」和四个 `参考了 upstreams/...`。
   判据：C12 与 C20 的计数必须能对账（要么统一术语，要么加一条交叉断言）。

6. **C15 的 `taught` 是子串搜索，分不清「提过」和「教过」。**
   D2 证明：把 `scope` 的真实教学全删掉、只留一句「本文提到 `scope` 一词时均指技术范围，与契约分层无关」，C15 照样绿。
   判据：要么 `taught` 要求命中带教学语义的上下文，要么在 C15 的 detail 里明写「只验出现过，不验是否在教」。

7. **三态是装饰性的，而且违反本库自己的硬边界 3。**
   两个检查器都实现了 `SKIP` 的渲染与计数，但 `skip=True` **全库无一处使用**——三态实际只有两态可达。
   同时 C1 在 `.git` 缺席时把**环境故障判成 FAIL**，而不是 `UNVERIFIED`。
   而 `README.md:100` 自己写着：「验证三态判定。环境故障既不算 `PASS`，也不判成产品缺陷——判 `UNVERIFIED`。」
   也就是说这条约束在文档里是硬要求，在代码里没有承载体。
   判据：`git archive` 导出上 C1 判 `SKIP`（或 `UNVERIFIED`），不是 `FAIL`。

8. **两个检查器的「合计」行 schema 不一致，`check-consistency.py` 里有死代码。**
   closure 报 `通过/失败/跳过/检查`，consistency 报 `通过/失败/检查`（少了「跳过」）。
   另外 `scripts/check-consistency.py:122` 的 `nfail = sum(1 in [0] for c in ... if not c[2])`
   紧接在 123 行被 `nfail = len(self.checks) - npass` 整个覆盖掉——是 SKIP 概念半途拆掉的残留。
   判据：两个检查器的 summary schema 一致，或有明确文档；122 行删掉。

9. **注入台测的是工作树，不是被审对象。**
   `harness.py` 的 `SRC` 指向工作树，`git_rev()` / `git_state()` 只出现在 assert 的**消息字符串**里，
   基线绿的时候 assert 不触发，于是**「测于哪个 commit」根本不会出现在输出上**。
   我这次重跑它，它打印的是 `29a50e4`——而交付要求审的是 `eaa8eb2`。
   判据：每次运行无条件打印 `commit／tag／工作树状态` 三元组（我方 M1 是这么做的），并把三元组写进报告表头。

10. **注入台的 2 条「设计内不报」没有退出判据，容易变成垃圾桶。**
    `s4-role-body`（角色正文语义冲突）与 `role-contract-drift` 期望集为空。
    边界写进 S4 的输出是好的，但「声明了抓不到」和「懒得测」在报告里长得一模一样。
    判据：每条「设计内」必须指向检查器输出里某句 `边界：` 原文，否则不算合法豁免。

---

## 7. `UNVERIFIED` 项与补证条件

| 项 | 状态 | 补证条件 |
|---|---|---|
| 注入台 28 条自带的 26 条「真抓住」 | `UNVERIFIED` | 我只把它当线索跑了一遍，没有逐条独立复现。补证：对每条补 `probe` 后置条件后重跑。 |
| `eaa8eb2` 之外的 commit | 不在范围内 | 被审对象就是 `eaa8eb2`。`29a50e4`/`8825b0e` 我只验了基线全绿。 |
| C3「本来就不该红」 | 设计内，但结论是「policy 不可falsify」 | 这个判断来自「没有任何检查器 grep 到 `provenance`」这一条静态证据，不来自注入结果。 |
| 段落级来源的**语义忠实** | `UNVERIFIED`（且不可机械核验） | `provenance_policy.not_covered` 自己就写明了这一点。本报告不重复夸大。 |

---

## 8. 复现本报告

```bash
# 基线
git clone <repo> /tmp/tpw-v3-clone && cd /tmp/tpw-v3-clone && git checkout eaa8eb2
python3 scripts/render.py --check
python3 scripts/check-closure.py
python3 scripts/check-consistency.py

# 我的注入台（14 条 + 自检）
python3 /tmp/rev3/suite.py
python3 /tmp/rev3/m3_selfcheck.py
```

我的 harness 每次运行前断言 `HEAD == eaa8eb2f0cb8ebcf3d3d782fbc3edab1a85e4a12`，
参考树有未提交改动就拒绝出数。
