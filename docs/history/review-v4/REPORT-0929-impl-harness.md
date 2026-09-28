# REPORT-0929-impl-harness · 故障注入台 v2 收口

- 角色：`tpw-0929-impl-harness`（pane 重启后新会话；上一轮状态在 `.pi/handoff/0929-impl-harness.md`）
- 授权改动范围：`.pi/injection/harness.py`、`.pi/injection/suite.py`、`probes.py`（拆出来的只读谓词）、
  `.pi/review-v4/impl-harness/`（本报告与证据）。**未改任何 `scripts/` 检查器**。
- 证据目录：`.pi/review-v4/impl-harness/`
- 三态口径：`PASS` / `FAIL` / `UNVERIFIED`。环境故障既不算 `PASS`，也不判成产品缺陷。
- 落盘文件的 sha256（`.pi/` 被 gitignore，无法 commit，故以此定版）：

```
1256f1a708e79f28e521f11cab6509089ff076c0d42531485833c4b20eb49e18  harness.py
904ac799fe8bc970571959ba763bbec67a66ab4db8d338468b8ba1211b929adb  suite.py
20b41bbaab6f263f67d3d87fe1a6cc86db8fd7794f4a159607866fd54eb79e31  probes.py
```

被审对象（**无条件打印**，本节开头就是运行输出原文的第一、二行）：

```
被审对象：commit 29a50e4（29a50e40f2ed0bf5d5bff85b7fbfa6b78059df3c）／tag v2.0.6／参考树干净
钉死参考树：/tmp/tpw-inj4/subject
```

---

## 0. 一句话结论

1. **全量重跑（31 行）**：真抓住 **27** ／ 漏报 **1** ／ 设计内 **1** ／ 负对照通过 **2** ／ UNVERIFIED **0**。
   两条负对照都按声明被拒绝记成指控。证据：`full-run.txt`。
2. **26 条历史「真抓住」不再 UNVERIFIED**：28 条旧注入逐条补上语义 probe，全量重跑全部通过；
   其中 26 条新增红 = 期望项，`probe=真`（缺陷真的落地）。证据：`full-run.txt` §probe 表 + §5 并排表。
3. **唯一一条漏报** `c9-lock-corrupt-NO-upstreams`：缺陷真实（锁文件 sha256 相对实物是假的；`probe=真`），
   但 v2.0.6 的 C9 在无 `upstreams/` 的树里**只核锁文件、不做实物核对，却在输出里打着「锁 + 实物对照」的名字**。
   这不是本台的问题，是检查器的实名缺口——verify 第二轮已用同一实验判过 `FAIL`（`review-v3` §4.2 A1、§6.2 判据）。
   该缺口在 impl-checkers 随后提交/落盘的版本里已被显式披露修掉（§6）。
4. **六道护栏逐条自证**（§1）：每道都给出「原来抓到过什么 / 现在还抓不抓得到 / 怎么验的」。
5. **上一轮那台被 4 条攻击打穿**（§5，单独成节）：同一条注入，旧台记「漏报」，新台分别记
   「负对照通过 / UNVERIFIED」；旧台还会把**被人改了一半的工作树**当成被审对象照样出数。

---

## 1. 六道护栏逐条

「原来抓到过什么」取自上一轮独立复审 `review-v3/REPORT-round3-verify.md`（它攻破过旧台）
与 `injection/REPORT-0928-impl.md`；「怎么验」指向本轮的实跑证据。

| # | 护栏 | 它原来抓到过什么 / 原来为什么会漏 | 现在还抓不抓得到 | 怎么验的 |
|---|---|---|---|---|
| 1 | **基线必须恰好等于 expected** | 0928 轮基线一度红在 C1/D1，旧台用 `baseline_pinned` 把「允许红哪几项」写死，漂了就炸——这条救过一次命；但旧台对「少红」（项被修好）与「多红」（新缺陷）不能同时断言 | 抓得住，且是**集合精确相等**：多一项、少一项都炸 | SC9（expected 写错 → AssertionError）；`demo-baseline-refusal.txt`（`--allow-baseline C99` → 断言炸并打印三元组） |
| 2 | **整树指纹（降为辅助）** | 它原来就是**唯一**的「缺陷落地证明」，于是一条只 append 无害注释的坏注入被记成「漏报」——坏注入伪装成对检查器的指控（verify §4.3(c)） | 抓得住「probe 真而指纹没变」的自相矛盾；但**不再用于判缺陷**，主门是 probe | SC7（probe 真 + 指纹没变 → 拒绝出数）；A1（同一条 noop 注入：旧台「漏报」／新台「负对照通过」，§5） |
| 3 | **检查器崩溃检测** | verify M4 指出「崩了当全绿」；旧台补了 exit∉{0,1}/traceback，但它**只认显式崩溃**——检查器静默 exit 0、什么都不打印，仍会被读成「没红」 | 抓得住，且覆盖面更大：静默退出会落到「合计行 0 次」而拒绝判定 | SC6（合成脚本 raise → CheckerCrashed）；A4（检查器被改成 `sys.exit(0)`：旧台「漏报」／新台 `UNVERIFIED(SummaryMismatch)`） |
| 4 | **三态解析 + 前后检查项集合比对** | 旧台只收 `[FAIL]` 行（`re.match(r"\[FAIL\]…")`），检查项整行消失或转 `SKIP` 会被静默当作无事发生（verify M5） | 抓得住：`gone`（整行消失）与 `new_skip`（转 SKIP）分别浮出，都判 UNVERIFIED | SC1/SC3/SC4；A2（把 C13 改成 SKIP：旧台「漏报」／新台 `UNVERIFIED(gone=∅ skip=['C13'])`，且落地复核确认 `[SKIP] C13` 与自洽合计行） |
| 5 | **「合计」行与逐行明细对账** | 旧台不读合计；verify 自己踩过「合并两个脚本输出只匹配最后一条合计」的坑（M6） | 抓得住：**逐脚本**对账，PASS/FAIL/SKIP/总数四项全等；`合计` 出现 0 次或 ≥2 次也拒绝 | SC2（改坏合计 → SummaryMismatch）、SC5（合并输出陷阱：聚合明细 (8,1,1,10) vs 最后一条摘要 (7,0,0,7)）；A3（合计撒谎：旧台「漏报」／新台 `UNVERIFIED(SummaryMismatch)`） |
| 6 | **无条件打印三元组 + 被审对象钉死** | verify §9：旧台 `SRC=工作树`，`git_rev()` 只出现在 assert 消息里（实测旧 suite 会在基线之后补打一行，但描述的是可变工作树，§5.4）；工作树脏了也照测 | 抓得住：运行**开始前**先打三元组，**结束后**再复核一次；每行测量前重新 `assert_subject`（HEAD + 参考树干净双重断言），脏了拒绝出数 | 运行输出首尾各一行三元组（`full-run.txt`）；SC8（喂别的 commit → SubjectDrift）、SC10（把参考树写脏 → 拒绝出数）、SC11（三元组可独立打印）；`demo-dirty-ref-refusal.txt`（脏参考树 → exit 3，消息里带三元组） |

补充（第 6 条的「钉死模式」实跑）：

- `--subject e7f6de1 --fixture-tag`（`full-run-subject-e7f6de1-fixture.txt`）：换靶成功，首行 `commit e7f6de1／tag （无）`，
  并明写「夹具基线，不是真实基线」。
- `--subject 05a8b4a --fixture-tag`（`full-run-subject-05a8b4a-fixture.txt`）：对 impl-checkers 提交后的检查器
  （21+7 项）重跑，31 行判定与 v2.0.6 完全一致（27/1/1/2），说明本台不绑死在某一版检查器上。

---

## 2. 28 条注入的 probe 后置条件（逐条）

### 2.1 probe 是什么、凭什么算数

`probes.py` 是**缺陷的定义**，不是检查器的输出：它只读文件、自己解析（`import hashlib, re, yaml`，
无一处 import `scripts/`；grep 证据见本节末）。每条注入的 probe 回答一个问题：
**「这条注入要制造的缺陷，现在真的在这棵树里吗？」** 返回 `False` 时判这条注入无效（UNVERIFIED），
**绝不允许**记成「检查器漏报」——这正是上一轮 verify 攻破旧台的那条病。

注入落地有三重机器确认，顺序固定（`harness.measure`）：

1. **锚点断言**：`sub()` 的原文没匹配上 → `InjectionBroken`（不是漏报）；
2. **probe 语义后置条件**：缺陷没落地 → `InjectionBroken`；
3. **指纹**：probe 真但整树内容没变 → `InjectionBroken`（两者矛盾）。

### 2.2 逐条结果（v2.0.6 全量实跑：28 条旧行 + 1 条负对照 + 2 条 C9 形态行 = 31 行）

`probe=真` 表示「缺陷真的被引入了」；`负对照` 行的 probe 必须为假。

| 注入 | probe | probe 结果 | 期望 | 实际新增红 | 判定 |
|---|---|---|---|---|---|
| c3-orphan-phase | `c3_probe` | 真 | C3 | C3 | PASS |
| c4-ghost-field | `c4_probe` | 真 | C4 | C4 | PASS |
| c10-second-target | `c10_second_target_probe` | 真 | C10,C20 | C10,C20 | PASS |
| c11-reverse | `c11_reverse_probe` | 真 | C11 | C11 | PASS |
| c13-no-prefix | `c13_probe` | 真 | C13 | C13 | PASS |
| d1-uppercase | `d1_roles_probe` | 真 | D1 | D1 | PASS |
| d1-ledger-env | `d1_ledger_probe` | 真 | D1 | D1 | PASS |
| d1-docs | `d1_docs_probe` | 真 | D1 | D1 | PASS |
| s1-nested-dir | `s1_probe` | 真 | S1 | S1 | PASS |
| s2-fragment-link | `s2_probe` | 真 | S2 | S2 | PASS |
| s3-one-sentence | `s3_probe` | 真 | S3 | S3 | PASS |
| s4-role-body | `s4_role_body_probe` | 真 | （设计内） | - | 设计内（边界原文已在输出里，见 §2.3） |
| s5-unknown-output | `s5_probe` | 真 | S5 | S5 | PASS |
| s7-bad-applies-to | `s7_probe` | 真 | S7 | S7 | PASS |
| orphan-ribbon | `orphan_ribbon_probe` | 真 | C19 | C19 | PASS |
| skill-src-drift | `skill_src_drift_probe` | 真 | C20 | C20 | PASS |
| role-contract-drift | `role_contract_drift_probe` | **假** | （负对照） | - | 负对照通过 |
| version-drift | `version_drift_probe` | 真 | C1 | C1 | PASS |
| judge-undeclared | `judge_probe` | 真 | C13,C4 | C13,C4 | PASS |
| c15-declared-untaught | `c15_declared_probe` | 真 | C15 | C15 | PASS |
| c15-undeclared-untaught | `c15_undeclared_probe` | 真 | C15 | C15 | PASS |
| c20-shape-mix | `c20_shape_mix_probe` | 真 | C20 | C20 | PASS |
| c20-ghost-path | `c20_ghost_path_probe` | 真 | C20 | C20 | PASS |
| c20-drop-source | `c20_drop_source_probe` | 真 | C20 | C20 | PASS |
| d1-self-file | `d1_self_file_probe` | 真 | D1 | D1 | PASS |
| s4-separation | `s4_separation_probe` | 真 | S4 | S4 | PASS |
| c7-into-not-list | `c7_probe` | 真 | C7 | C10,C7 | PASS（**期望外红 C10**，见 §2.3） |
| c10-into-drops-target | `c10_into_drops_probe` | 真 | C10 | C10 | PASS |
| noop-append | `noop_append_probe` | **假** | （负对照） | - | 负对照通过 |
| c9-lock-corrupt-WITH-upstreams | `c9_probe` | 真 | C9 | C9 | PASS |
| c9-lock-corrupt-NO-upstreams | `c9_probe` | 真 | C9 | - | **FAIL（唯一漏报，§6）** |

对历史的交代：上一轮 `REPORT-0928-impl` 报的是「真抓住 26 ／ 漏报 0 ／ 设计内 2」。
本轮 28 条旧行里，26 条抓住的全部仍然是 `PASS` 且 `probe=真`；`s4-role-body` 仍是设计内
（现在必须引用输出里真实存在的「边界：」原文才成立）；`role-contract-drift` 从「设计内」
升级成「负对照通过」——它第一次有了机器判据：`probe=False` 证明这条注入**没有**引入缺陷，
所以它根本不该出现在「漏报」或「设计内」里的任何一个桶。26 条从 UNVERIFIED 到可核对的
通路就是这张表：每条都有 probe 名、probe 结果、期望、实际新增红四列。

### 2.3 两处必须说清的行

- `c7-into-not-list`：注入把 `into: [interrogate]` 改成标量，C7 按 schema 红，**C10 也连带红了**。
  新台不把「期望外的红」藏起来，而是打印 `期望外红：C10`，判定仍 PASS（期望项 C7 确实红了）。
  老台是宽集合判定（红的和期望有交集就算抓住），会把这类连带红静默吞掉。
- `s4-role-body`：expect 为空的设计内行。新台要求它的 `boundary` 字符串**真实出现在检查器输出里**，
  否则判 UNVERIFIED。本轮引用的原文是 `本检查只看它引用的 id 与它维护的分离约束`——
  在「豁免必须引用输出原文」的前提下，它证明这条豁免不是垃圾桶。

### 2.4 probe 独立性证据

```text
$ grep -n "^import\|^from" .pi/injection/probes.py
14:from __future__ import annotations
16:import hashlib
17:import re
18:from pathlib import Path
20:import yaml
$ grep -n "scripts" .pi/injection/probes.py     # 仅出现在注释里
5:它只读文件、自己解析，**不复用 scripts/ 里的任何代码**——拿被审对象的实现
```

---

## 3. 负对照：证明 probe 不是摆设

两条负对照都是**文件真的被改了**（指纹变化被断言）却**没有引入缺陷**的注入：

| 负对照 | 注入做了什么 | 指纹 | probe | 判定 | 证人 |
|---|---|---|---|---|---|
| `noop-append` | 往 `skills/tdd.md` 末尾 append 一句 `<!-- 无害注释 -->` | 变了 | **假**（来源段语义与 registry 仍一致） | 负对照通过——**拒绝记成任何指控** | `c20-drop-source`（同一条谓词 `tdd-source-semantics`，probe=真且被 C20 抓住） |
| `role-contract-drift` | 把 `roles/verifier.md` 里 `` `subject` ``/`` `scope` ``/`` `frame_alignment` `` 改名，但 verifier 名下的技能正文仍教这些字段 | 变了 | **假**（字段没有从产出方全部正文里消失） | 负对照通过 | `c15-undeclared-untaught`（同族谓词：证人用 `field-untaught-everywhere` = 负对照的 `field-lost-from-producer` ∧ 被阶段判据门控） |

互证机制：每个负对照声明一个证人，运行器单独检查「证人 PASS 且 probe 真」；
谓词不同时打印「同族谓词：负对照=`field-lost-from-producer`，证人=`field-untaught-everywhere`」，
不冒称「同一条谓词」。运行输出：

```
✔ 负对照互证（同一条谓词 tdd-source-semantics）：noop-append（probe=假）+ c20-drop-source（probe=真 且被抓住）
✔ 负对照互证（同族谓词：负对照=field-lost-from-producer，证人=field-untaught-everywhere）：role-contract-drift（probe=假）+ c15-undeclared-untaught（probe=真 且被抓住）
```

**这条负对照直接对应 driver 今天自己栽的那一次**：替换串没匹配上 = 注入没改变目标状态，
却被读成「漏报」。新台把这种输入全部挡在「漏报」桶之外：锚点不中 → `InjectionBroken`，
probe 不成立 → `InjectionBroken`；作为普通注入判 UNVERIFIED，作为负对照判负对照通过。
§5 的 A1 是这条控制的旧台并排。

---

## 4. 被审对象钉死与无条件打印（实现与实测）

- 参考树 `/tmp/tpw-inj4/subject` 是 detached clone；每行测量前 `assert_subject()` 重新断言
  `HEAD == pin` 且 `git status` 干净；`upstreams/` 是参照物、用 `.git/info/exclude` 排除，不算脏。
- 三元组打印点有三个，都不依赖 assert 触发：
  1. 运行开始前（早于自检与基线）；
  2. 运行结束后复核（确认整轮之间没漂）；
  3. 拒绝出数的错误消息里（脏树/换靶都会带上三元组）。
- 实测证据：
  - `full-run.txt` 首行与倒三段各一条三元组；
  - `demo-baseline-refusal.txt`：`--allow-baseline C99` 让基线断言炸，报错文本里仍含三元组；
  - `demo-dirty-ref-refusal.txt`：参考树写脏 `WIP-ATTACK.md` → `exit 3`，
    `参考树有未提交改动，拒绝出数：?? WIP-ATTACK.md ／ 被审对象：commit 29a50e4…／参考树有未提交改动`。

---

## 5. 攻破上一轮那台：新旧判定并排（单独成节）

**实验设置**：旧台 = `.pi/injection/prev-r3/{harness,suite}.py` 冻结件（sha256 与 `MANIFEST.sha256`
逐字节一致；已复核），**只补了 3 处路径常量**（`SRC`、`WORK`、`sys.path`），判定逻辑一字未动；
旧台按它自己的用法加 `--fixture-tag`。新台 = 本轮 v2。两边的被审对象都是同一份
`/tmp/tpw-inj4/subject`（`29a50e4` 的 detached clone）。

### 5.1 同一批注入的判定并排

完整表：`ab-old-vs-new.tsv`（旧台 28 行 + 新行并集 31 行）＋本节攻击表。旧台全量结果：`old-suite.txt`
（`真抓住 26 ／ 漏报 0 ／ 设计内不报 2`，与 0928 轮公布的数字一致——所以下面这些攻击
**不是**它自带行集的回归，是行集之外的新输入）。

| 差异点 | 旧台 | 新台 |
|---|---|---|
| `role-contract-drift` | 设计内（期望集为空，无任何判据） | 负对照通过（probe=False，有机器判据） |
| `c10-second-target` 期望集 | `{C10}`（宽） | `{C10,C20}`（收紧；实际红两项） |
| `c3-orphan-phase` 期望集 | `{C3,C6,S1}`（宽） | `{C3}` |
| `orphan-ribbon` 期望集 | `{C19,C6,S1}`（宽） | `{C19}` |
| 期望外的红 | 不呈现 | `c7-into-not-list` 打出 `期望外红：C10` |
| `noop-append` / 两条 C9 | 没有这些行 | 负对照通过 / PASS / FAIL |

### 5.2 4 条攻击：同一条注入，两边判定

每条攻击先打印目标文件内容 sha 前 12 位的变化（证明**注入真的改了目标状态**——这是
driver 今天栽跟头的那条纪律的机器化）：

| 攻击 | 注入（目标文件 sha 变化） | 旧台判定 | 新台判定 |
|---|---|---|---|
| A1-noop-append | `skills/tdd.md` 只 append 无害注释 `76b769e5e2a4→2bd638556e0b` | **漏报**（新增红=∅） | **负对照通过**（probe=假 → 拒绝记成指控） |
| A2-c13-to-skip | 把 C13 改渲染成 `SKIP` 且合计行自洽 `d4061a5dde7f→70ed97af5fa2` | **漏报** | **UNVERIFIED**（`gone=∅ skip=['C13']`；落地复核：`[SKIP] C13 …` + `合计: 18/0/1/19`） |
| A3-summary-lie | 明细不变，合计行改成 `99 项通过/0 失败/0 跳过/99 项检查` `d4061a5dde7f→67381e5da1df` | **漏报** | **UNVERIFIED**（SummaryMismatch 合计 (99,0,0,99) vs 明细 (19,0,0,19)） |
| A4-silent-checker | `check-closure.py` 换成 `import sys; sys.exit(0)` `d4061a5dde7f→14c75fb904c5` | **漏报** | **UNVERIFIED**（合计行出现 0 次） |

A2–A4 的攻击对象是**检查器被改坏**，不是树里多了缺陷。旧台对这三种都输出「漏报」——
**指控检查器漏报，而真实情况是检查器已经坏了/被改了**。这正是「坏输入变成假证据」的第二种形状；
新台一律拒绝判定（UNVERIFIED）。

### 5.3 旧台测工作树：半成品会被当成被审对象

对同一份「clone 在 `29a50e4` 上、带一个改动中的 tracked 文件 + 一个未跟踪文件」的树：

```text
$ python3 old-dirty/suite.py --fixture-tag --only c3-orphan-phase     # 旧台
测于 commit 29a50e4／tag ['v2.0.6']／工作树有未提交改动
基线全绿（0 项失败）
c3-orphan-phase         ✔ 抓住    C3                C3,C6,S1
真抓住 1 ／ 漏报 0 ／ 设计内不报 0          # ← 照常出数
```

它输出了「工作树有未提交改动」这半句话，然后**继续**：`seal_for_c1` 的 `git add -A` 把
未提交改动连带塞进 fixture commit，于是副本看起来是"干净"的。被审对象到底是什么 commit？
没法回答——这正是 driver 说的「别人改到一半的脏树会被当成基线被测」。
新台对同一份树：`demo-dirty-ref-refusal.txt`，`exit 3`，不出任何数字。

### 5.4 旧台做到了的（公平起见）

- 它**会**检测显式崩溃（exit∉{0,1}/traceback）；
- 锚点不中时它抛 AssertionError，suite 打印「注入失败」而不是记漏报；
- 它**也**打印三元组——但在基线测量**之后**，且描述的是可变 `SRC`（工作树），不是被测副本；
- 它自带行集里的 26 条确实都抓住了。攻破它靠的是**行集之外的新输入**（A1–A4 与脏树），
  这一点必须说清楚，不能把「旧台 26 条全抓」说成假的。

---

## 6. 我发现但不自修（检查器侧）

1. **v2.0.6 的 C9 在没有 `upstreams/` 时"实名不符"**（本台唯一的 FAIL 行）。
   同一处锁文件 sha256 篡改：挂了 `upstreams/` 的树 → `[FAIL] C9 … 并已逐条比对 sha256 与 pin`；
   干净 clone 形态 → `[PASS] C9 来源真实存在（锁 + 实物对照） … 0 条失效来源`，
   **没有一个字说它跳过了实物核对**。检查器 docstring 写了「有克隆时另比 sha256/pin」，
   但那句话不在输出里，读者只能看到 PASS。
   verify 第二轮已经用 A1/A2 受控对判过同一个缺口（`review-v3` §2 第 3 条、§6.2 判据）。
   **不修原因**：不在授权范围（只能改注入台与自己的报告），且 impl-checkers 随后落盘的新版
   已把它改成实名输出——对无 `upstreams/` 的树，C9 现在的原文是：
   `PASS（锁文件核对）：registry.sources 均在随包 upstreams.lock.yaml；未发现 upstreams/，未做上游实物 sha256/pin 对照；不证明锁文件与真实上游一致。`
   本台对这个新行为**维持 FAIL**：不是因为它该被修，而是因为被钉在 `v2.0.6` 上的对象还没有这句话。
   §5.1 的 `c9-lock-corrupt-NO-upstreams` 行在我的判定里保持红色，直到被审对象换成带披露的版本为止——
   我不会为了账面好看把它改判成「设计内」。
2. **本台没有 C21/C22 的反例**。这两项在 `12aecf1` 才进入被审对象，而委派给定的基线是 `v2.0.6`（`29a50e4`），不含它们。
   我另跑了一次 `--subject 05a8b4a --fixture-tag`（`05a8b4a` = 含 C21/C22 的当前 HEAD）：同一套 31 行判定不变，但**新检查项本身**
   没有专属注入。若要让「C21/C22 不是摆设」也可机核，需要给它们各补一条 probe 注入
  （例如删除某条原则的「来源：」行、把 `UNVERIFIED` 翻成 `enforced`）——这超出本轮的 28 条范围，
   记在这里由 driver 决定。
3. **`c7-into-not-list` 的期望外红 C10** 是检查项之间的连带，不是缺陷；本台已如实打印，
   不吞、也不算进期望。它同时暴露一件事：**归因到具体检查项**这条纪律在「一条注入触发多项」时，
   需要人读「期望外红」列，机器只保证它不被藏起来。
4. 备注：`.pi/` 被 `.gitignore` 挡住，本台不能进任何 commit；`prev-r3/` 用 sha256 清单冻结，
   我自己复核过清单与实物逐字节一致（MANIFEST 两行）。**没有改任何检查器文件**（`git status` 干净）。

---

## 7. UNVERIFIED 与残留

- 本轮 31 行：**UNVERIFIED = 0**。唯一非 PASS 的注入行是 FAIL（漏报），且 §6.1 已给归属。
- 仍然**不可机核**的（明确列为残留，不冒充已证）：
  1. **probe 语义的忠实性由本台作者声明**。probe 证明的是「我声明的那个缺陷定义在树里成立」，
     它不证明「这个定义等价于检查器名字所承诺的事情」。独立复审若要再核，入口是 `probes.py`
     的每个谓词是否等义于注入描述（这一点和第二轮的 `UNVERIFIED` 同源，但已经从「连后置条件都没有」
     推进到「有可读、可反驳的谓词」）。
  2. **C9 无实物边界的实测**：只有带 `upstreams/` 的形态能证明 C9 真的比较内容；干净 clone 形态下
     「无法比较」是环境事实，不是检查器能力（§6.1 的 FAIL 判的是实名，不是能力）。
  3. 新检查器 `05a8b4a` 上的 31 行是在 `--fixture-tag` 下跑的（该 commit 无 tag）；
     夹具基线已在输出首段自我声明，不能当真实基线引。
- 上一轮 verify 的 `UNVERIFIED` 项之一——「注入台 28 条自带的 26 条真抓住」——
  本轮以「逐条 probe + 全量重跑 + 新旧并排」作为补证材料；**是否接受补证由独立复审决定，本台不自判**。

---

## 8. 复现

```bash
# 0. 钉死参考树 + 全量（默认被审对象 v2.0.6）
cd ~/Developer/tim-professional-workflow
python3 .pi/injection/suite.py                      # 期望 exit 1：唯一 FAIL 是 C9 无 upstreams

# 换靶（无 tag 的 commit 用 --fixture-tag，输出会自我声明夹具基线）
python3 .pi/injection/suite.py --subject e7f6de1 --fixture-tag
python3 .pi/injection/suite.py --subject 05a8b4a --fixture-tag

# 自检（11 项）与拒绝出数演示
python3 .pi/injection/suite.py --allow-baseline C99          # exit 2，断言炸但打三元组
echo WIP > /tmp/tpw-inj4/subject/WIP-ATTACK.md               # 之后记得删掉
python3 .pi/injection/suite.py --only c3-orphan-phase        # exit 3，脏参考树拒绝出数

# 旧台（冻结件 + 路径补丁）与新台攻击对照
# 见 /tmp/tpw-ab/{old,attacks.py}（临时装置，一次性；证据已归档到 .pi/review-v4/impl-harness/）
```

证据清单（均在 `.pi/review-v4/impl-harness/`）：

| 文件 | 内容 |
|---|---|
| `full-run.txt` | v2.0.6 全量 31 行 + SC1–SC11 + 首尾三元组 |
| `full-run-subject-05a8b4a-fixture.txt` | 对 impl-checkers 提交后检查器（21+7）的同一套注入 |
| `full-run-subject-e7f6de1-fixture.txt` | 换靶演示 |
| `demo-baseline-refusal.txt` | 基线断言炸 + 三元组 |
| `demo-dirty-ref-refusal.txt` | 脏参考树 → exit 3 |
| `old-suite.txt` | 旧台（同一被审对象）全量：26 抓 / 0 漏 / 2 设计内 |
| `old-attacks.txt` / `new-attacks.txt` | 4 条攻击的新旧并排 + 注入落地 sha |
| `old-dirty-src.txt` | 旧台对脏工作树照常出数 |
| `ab-old-vs-new.tsv` | 28 条旧行 + 3 条新行（noop-append、两条 C9）的判定并排 |
