# 0930 旧组 closeout

本文件是 `tpw-0930-driver` 与 scout-b / scribe-b / adversary-b 交接待命的自包含记录。
依据：`0930-stop-and-next-wave-BRIEF.md`（Owner 范围调整）与 Oracle 的 ACK 指令。
**本组到此停止推进，不向新组派活，不自动续作，不关闭任何 pane。**

---

## 1. 冻结对象

| 项 | 值 |
|---|---|
| commit | `8d800ecf67c3e4a3da1b87e4a64f664785dfd90c` |
| tree | `d687773a60b5f6a7d1627e686ef8fd08c15d8a73` |
| 实施片起点 | `be91e15`（独立性降级实施片开始前的 HEAD） |
| 实施范围 | 11 个文件：`workflow/registry.yaml`、`AGENTS.md`、`README.md`、`docs/coldstart.md`、`skills/tier-sizing.md`、`skills/decision-ledger.md`、`roles/adversary.md`、`roles/driver.md`、`roles/verifier.md`、`scripts/render.py`、派生产物 4 个 |
| 检查器 | **三个 `check-*.py` 与 `compose-role.py` 相对 `be91e15` 零改动**；`render.py` 4 增 1 删（新增 `criteria_note` 渲染 3 行 + 修该文件内一处既有 U+FFFD） |

---

## 2. 已验范围与结果

### 2.1 独立性降级契约（已实施且经独立评价）

- `A7`／`A8` 各加一个正交字段 `independence`（二值：`独立复核`／`单会话自审`），与 `stance`／`verdict` 正交，两字段允许合法不同、不加相等断言，P6 取较弱一侧。
- `AGENTS.md` 硬边界 5→6 条，第 1 条拆成**结论断言**与**能力断言**。
- **全局 `solo` 自足豁免已消除**：原「`solo` 档显式豁免两条硬规则」删除，改为五档路线表；**只有第一行硬规则照旧**，其余四行是已授权的合法 fallback。
- 作者自审三条件的合取按「**独立评价者有没有真的接手**」写，不是按 Owner 行为写——
  **枚举里出现某情形不等于合取允许该情形**。
- P6 加披露判据 + `criteria_note` 承载机械效力边界；**`A8.verdict 是 PASS` 那条一字未改**。

独立评价：`ADVERSARY-VERDICT-IMPL-1`、`-IMPL-FINAL`、`-CONJ`、`-ENTRY-B1`、`-BATCH1-REREAD`，共 14 份裁决在册。
`CONJ` stance = **通过（无附加条件）**；Oracle 裁定本片记 **A7.stance = 采纳**（用真源三值，不把 CONJ 的自然语言「通过」扩成第四值）。

### 2.2 入口修复（已实施，delta 已独立评价）

C-1／C-2（README 无例外全局禁令、硬边界指针表）、C-4／C-5（冷启动判据与自检三项）、
C-6（`skills/tier-sizing.md` 把「开不出独立会话」绑到 `UNVERIFIED`，根因是两种能力缺失被混为一谈，已拆两支）、
C-7（**先撤回我自己的错误立论**：registry 的「摘要」是 hash digest 不是文字摘要，技能要求指针与 digest 本就不冲突；
另修 Oracle 直接读出的真冲突——「簿子默认一次性不进版本库」与 A9 的 `durable` 冲突）。

### 2.3 现有包隔离冷启动（本人实测）

用 `git archive HEAD` 导出**无 `.git`** 的干净包（4.2 MB），脱离工作树与本仓 git 元数据后实跑：

| 检查 | 干净包 | 工作树 |
|---|---|---|
| `render.py --check` | **exit 0**（12 个派生文件逐字一致） | exit 0 |
| `check-closure.py` | **exit 0 —— 20 通过／0 失败／1 跳过** | exit 1（20／1／0） |
| `check-consistency.py` | exit 0 | exit 0 |
| `compose-role.py --check` | exit 0 | exit 0 |

**关键事实**：干净包里 C1 由 `FAIL` 变 **`SKIP`**，检查器逐字写明理由是「无本库自己的 git 元数据（如 `git archive` 导出）」。
⇒ **C1 的 FAIL 是本仓 HEAD 无 release tag 的发布身份状态，不是包缺陷。**
这一条同时印证了检查器自己关于「三种环境形状按硬边界第 3 条判 `SKIP`」的设计意图。

### 2.4 其他

- 实施文件 U+FFFD = **0**（10 个文件实扫；**不是全历史为 0**——旧 `ADVERSARY-VERDICT-V10.md` 仍含 2 个，按裁定保留原字节）。
- `A9` 台账 **69 行**；**前 56 行 md5 `5f10bc90cc595329c3f06dc18093a735`** 与实施前逐字一致（只追加，硬边界第 5 条）。
- 候选冻结件 6 份在册（`--v4/v5/v6/v8/v11/v12-frozen`）。

---

## 3. 未验 / 候选 / 未裁定（**不得当作已完成**）

| 对象 | 状态 | 说明 |
|---|---|---|
| `DISPOSAL-BATCH1-REREAD.md`（503 行） | **候选，未裁定** | in-progress 九项 + 两份 hooks 全文重读的机制候选。独立评价 `ADVERSARY-VERDICT-BATCH1-REREAD.md` 附条件通过，**5 条澄清性条件，未裁定任何一项处置** |
| `DISPOSAL-BATCH1-INPROGRESS.md`（542 行） | **已被否掉处置理由的历史记录** | Oracle 裁定「摘录确实存在」≠「摘录足以覆盖正式处置理由」，且禁止「转读即视为全面读过」。**保留原字节，不删不改** |
| `RECON-18-STATUS-0930.md`（613 行） | **候选，仅静态复核** | scout 在停令前写出。**只静态复核的项不得升级为真实验证**——本组未对其做运行级验证 |
| 载体层 1080 个文件 | **处置记录未建** | 技能层 101 条处置（absorbed 81 + rejected 20）是真的，与载体层**不是同一层**。**不得互相冒充** |
| 642 口径 | **未按路径集合复核** | 已选为初筛工作池，但分档复核未做 |
| 文章原站一致性 | **UNVERIFIED** | poteto 两篇仅有镜像缓存，**语义身份未验**。已授权做一次有界核读，**本组未执行** |
| `SDD-CACHE` 落点 | **需补读后才可裁定** | `source-driven-development/SKILL.md` 未读（裁定条件 B1-3） |
| `edges` 另 4 处命中 | **未核** | `cartographer.md`／`artifacts.md`／`registry.yaml`／`P2.md` 是否只是字段引用而非重定义（条件 B1-2） |
| 11 份来源版本 | **UNVERIFIED** | 均不在 lock 的 `skills:` 枚举内、无文件级 pin。`md5` 是内容指纹不是时间戳；**mtime 同秒是批量 checkout 产物，不是修改时间**。缺的是可寻址性，不是可核性 |

---

## 4. Dirty 归属

| 类别 | 内容 | 处置 |
|---|---|---|
| **原 8 暂存（旧会话交付）** | 8 files / 3814 insertions | **保留，未纳入本组任何 commit，不混提交** |
| 已修改未暂存 | `docs/history/derivation-0930/DISPOSAL-BATCH1-REREAD.md`（B1-5 措辞） | 属本组，已 commit `0477895` 之后又被 B1-5 改动**未提交** |
| 已修改未暂存 | `docs/history/handoff/0930-boundary1-CONFLICT.md` | **历史文档，自实施片起未再改动**；Oracle 裁定不整体判通过，留工作区 |
| 未跟踪 | `ADVERSARY-VERDICT-BATCH1-REREAD.md`、`ADVERSARY-VERDICT-ENTRY-B1.md`、`RECON-18-STATUS-0930.md`、`0930-oracle-BATCH1-CLARIFICATION.md`、`0930-oracle-SCOPE-DECISION.md`、`0930-stop-and-next-wave-BRIEF.md` | **本组证据，保留未提交**——新组按指针冷读，不整批装旧长会话 |

---

## 5. 本组的三处真实失守（供新组当作已知风险）

1. **弄丢过两版候选的可恢复字节，两次都是 driver 造成**：V7「该冻没冻」、V9「覆盖了已冻结件」。
   **两形态不同**（前者无冻结件可覆盖），已分别立纪律 A／B。V7、V9 的字节**永久不可恢复**。
2. **A9 派工竞态造成 6 行重复**：driver 见 `agent_not_found`（Herdr **agent 注册**缺失）即判定会话已死，
   自行接管同一批追加并先行提交，scribe 量基线时已是 62 行，遂再追加同样 6 项。
   append-only 台账**无法清理**；已追加去重行（`ada3d96`）指向二者关系。
   **教训：`agent_not_found` 只排除 agent 注册，不等于会话进程已死**——该读 pane 确认。
3. **`tpw-0930-scribe-b` 会话两次卡在 `ctx_batch_execute`、重启仍复现**，本组内不可用。
   A9 追加改由 driver 用 `ledger.sh` 机械完成，**actor 写实际写入者，未伪装 Scribe**。
   **裁定不授权为本组修该工具**；新组若需 scribe 请另起会话。

**另有一类反复出现的失效形状**（不是同一处代码 bug，是同一个做法）：
**对没有读完的文本下断言**。表现为——把「词义不同」当成「语义冲突」两次；
把上游一句从上下文里摘出来当独立主张（loop-me「Mandate nothing structural」）；
给一段并不存在的文字加「逐字」二字（AGENTS 硬边界第 6 条并无「构建期依赖」排除）。
**三次都由 Oracle 纠正。** 新组接手来源工作时值得当作已知风险。

---

## 6. 剩余对象（交给新组，本组不做）

- 两条线 G（本仓治理与上层说明）／P（workflow 核心优化）的范围与切线：**以 Owner 回答为准**。
- 上述第 3 节的未裁定候选、未验项。
- C1 仍是发布身份 FAIL：**本组不打 tag、不 push、不通知 UCBIP**。

---

## 7. Worker ACK

- **`tpw-0930-adversary-b`**：已停止写（不再新建文件，14 份裁决保留原字节不改）；
  已停止派工（无在飞任务、无自动续作、未向任何角色派活、未关闭任何 pane、未 push/tag、未碰原 8 暂存）。
  最后已确认效果：`ADVERSARY-VERDICT-BATCH1-REREAD.md`（384 行、md5 `a2c000462ce0ad9f17d26ef4a41e9c25`、
  U+FFFD 0、stance 附条件通过、5 条澄清性条件）；四检查 `0/1/0/0`，C1 按裁定记 `FAIL` 未改判，
  三个 `check-*.py` 自 `be91e15` 起零改动。
- **`tpw-0930-scout-b`**：已停止写、已停止派工（ACK 经 Intercom 已送达 driver）。
  最后已确认效果：`DISPOSAL-BATCH1-REREAD.md` 与 `RECON-18-STATUS-0930.md` 写出。
- **`tpw-0930-scribe-b`**：**工具阻塞，非已完成**。两次卡在 `ctx_batch_execute`、重启仍复现。
  其 A9 追加已交付（台账 63–68 行，见第 5.2 节重复说明），此后不再追加。
- **`tpw-0930-driver`（本人）**：无在飞写入，**未设任何自动续作 loop / 定时任务 / 事件触发**，
  未向新组派活，未关闭任何 pane。closeout 写毕后进入待命。

---

## 8. 一条本组认为该留给新组的经验（候选，未经独立复核）

三次「对没读完的文本下断言」都由同一句话纠正——**冲突的源头常常不是真冲突，
而是对既有词义的一次错误理解**。正确处理不是先裁定，是**先去确认那个词本来是什么意思**。

与之配套的一条来自 adversary（它自己的候选，未经独立复核）：

> 一个判据体系的质量上限，不在它有多少条断言，
> 在**最后一个执行者读它时，能不能不问第二个文件就走完**。

本组三个真缺陷（一条判据在派生产物里被静默删除、一条五档表自称自足却需要表外文字、
一条 README 写「这里不复述第二份」而前面已复述）**全部由这条抓到，检查器一个都没报**。
