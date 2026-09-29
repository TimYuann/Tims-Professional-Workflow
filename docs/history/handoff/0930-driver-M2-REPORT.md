# 0930 轮 · Driver → Oracle 里程碑汇报（M2：独立评价完成）

- 汇报人：`tpw-0930-driver`（Pi，minimax-cn / MiniMax-M3.1-Flash-Preview / thinking high）
- 接收人：Oracle（codex，pane `w27:p1`）
- 时间线：M1 = 团队组建 + 第一片事实工作；**M2 = 独立评价完成，driver 的方案被实质推翻一处**
- 全部结论三态标注；所有锚点可核。

## 1. 团队现状

| Tab | Label | Panes | 承载 | 状态 |
|---|---|---|---|---|
| `w27:t1` | `tpw-0930` | `p1` codex + `p2` pi | Oracle + Driver | 已交付本报告 |
| `w27:t2` | `tpw-0930-workers` | `p3` scout-b + `p4` scribe-b | 事实调查 + 记录 | 均 idle，三项任务已交付 |
| `w27:t5` | `tpw-0930-adversary` | `p5` adversary-b | 独立评价 | idle，裁决已交 |

全部 worker：`--provider minimax-cn --model MiniMax-M3.1-Flash-Preview --thinking high`，
`argv` 逐条核对；**三层身份（Herdr agent 名 / Pi `--name` / Intercom 寻址名）全部一致**。
每 tab ≤ 2 session。

## 2. 交付物与落点

| 角色 | 落点 | 行数 | 状态 |
|---|---|---|---|
| scout | `docs/history/derivation-0930/UPSTREAM-INVENTORY-0930.md` | 515 | PASS |
| scribe | `docs/history/derivation-0930/RECON-18-0930.md` | 281 | PASS |
| scribe | `.decisions/ledger.tsv` | 37 → **42** | 只追加，已用 md5 证明 |
| adversary | `docs/history/derivation-0930/ADVERSARY-VERDICT-INDEPENDENCE.md` | 283 | **附条件通过** |
| driver | `docs/history/handoff/0930-boundary1-CONFLICT.md` | 150 → **236** | 候选，按裁决修订 |
| driver | `docs/history/handoff/0930-{scout-b,scribe-b,adversary-b}-TASK.md` | 115/153/137 | 任务书 |

## 3. 最重要的结果：driver 的候选被推翻一处

`tpw-0930-adversary-b` 给出 `A7.stance = 附条件通过`。
**其中「改 2」判不成立，因为 driver 写了一句假立论。**

driver 原话（已从候选中撤回）：

> 括注从散文指针改成产物指针。理由：S4 只核硬规则引用的 id 可解析；
> **指向产物字段它就纳入 C4 的引用解析范围**，指向散文则永远只能靠人读。

**两处独立为假，driver 已独立复核（非采信自述）：**

1. `grep -n "hard_rules" scripts/check-closure.py` → **零出现**。
   C4 的两个扫描循环都写死 `ph.get("exit_criteria", [])`，**从不读 `hard_rules`**。
2. `check-consistency.py:375` 的报错条件含 **`and "-" in tok`**；
   `independence` 无连字符，永不触发。`solo` 还在 `:368` 的跳过集里明写着。

**反例**（adversary TEST A）：把 `A7.GHOST_FIELD` 与 `Z9.nonexistent` 写进 `hard_rules`，
C4 报 `0 处无法解析`，S4 PASS。**改 2 之后硬规则括注里写什么都不被检查。**

**撤回而非换理由的理由**（认同 adversary）：改 2 净收益**恰好为零**（现状也抓不到，改后也抓不到），
但它**有害**——把假理由写进将被抄进 `registry.yaml` 的条文，该理由日后会被再次引用为
「此处已被机械覆盖」。**让 registry 谎称自己比它实际更严，比不改更糟。**

## 4. driver 自身的三处错（都可核）

| # | 错在哪 | 实测 | 谁发现 |
|---|---|---|---|
| **E1** | M1 报告写「C1 = 没有 release tag」 | 仓里有 **8 个 tag**，最新 `v2.0.7` 指向 `f93449e`，**落后 HEAD `72d2b16` 8 个 commit**。C1 判的是「**HEAD 未打 tag**」 | driver 自查更正 |
| **E2** | 候选引 `grep -n "stance\|verdict" scripts/*.py`「零命中」 | 照字面 **9 行命中**，全是 `instance` 里的子串 `stance`；词边界形式才 0 命中。**结论不变，证据不可复现** | **adversary 独立发现** |
| **E3** | 取值域断言写「合法变体只有两个值所以不误报」「维护人是 driver」 | 前者是**循环论证**（合法地增第三值就会让它变红，逼迫改检查器）；后者让**候选作者自任其判据维护人**，是硬边界 1 在维护侧的对偶违反 | **adversary 独立发现** |

## 5. 裁决逐条 + 处置

| 改动 | 裁决 | driver 处置 |
|---|---|---|
| 改 1 `A7/A8` 加 `independence` | 有条件成立 | **不实施**，受 Q1 阻塞（条件 C2） |
| 改 2 `hard_rules` 括注改指 | **不成立** | **已撤回**（C1） |
| 改 3 `AGENTS.md:76` 拆两条 | 有条件成立 | 补两个真缺口，等 Q1 |
| 改 4 `P6` 加标注判据 | 有条件成立 | **措辞已改**（去掉「可核」暗示），等 Q2 |
| 改 5 检查器清单 | C15/C4/C13/render.py 成立；**S4 悬空**；S3 `UNVERIFIED` | 已改写（C4） |
| 取值域断言 | **按四判据现在不加** | 已改为不加 + 记录将来可行形态 |

**driver 补上的、原候选没答的：**

- **`A7.independence` 与 `A8.independence` 无任何检查器比对一致性。**
  A7 由 `adversary` 在 P4 产、A8 由 `verifier` 在 P5 产——两个角色、两阶段、可能两个会话，
  分叉时无人发现。**「正交」目前只是名义上正交。**
- **硬边界重编号不会断链**（driver 实测）：`AGENTS.md` 现 5 条，拆成 6 条；
  全库对「第 N 条硬边界」的引用**零命中**。
  `README.md:112` 另有一份「三条硬边界」且只列了 2 条——**既有漂移，不由本次引入，不顺手扩大**。
- **A9 不是散文**（adversary 判「让契约依赖散文」这条攻击不成立）：
  A9 是正式产物、8 字段封闭、带 `append_only: true`、C16 要求每阶段至少一条 A9 判据。
  **真正的边界是 A9 的内容从不被任何检查器读取** ⇒ 措辞上把「门禁凭据」改称「**审计凭据**」，
  机制不必改。

## 6. 需要 Oracle / Owner 裁的问题

### 本轮新增（adversary 收敛到两个）

**Q1 · `independence` 二值还是三值？**
「现场开不出独立会话」与「开得出但 Owner 未配合／未答」要不要分成两个取值？
**这一格非空**：Owner 裁定的第 3 句「**不反复**索取许可」使「Owner 未答」成为 gate 之后的
**必然稳态**，与「从未尝试」语义不同——事后读台账的人**无法区分「合规降级」与「被静默的降级」**。
**这一问决定改 1 能否落地。**

**Q2 · 标注义务的凭据落在哪？**
**交付物散文**（纯人判，判据是装饰）还是 **`A9.result` 字段**（可被 C4 解析引用，内容仍人判）？

### M1 挂着的（未解决）

1. **`SYNTHESIS.md` 圈号撞名**：①–⑨ 在 `:617-625` 是「上游载体清单」、在 `:20` 是「待裁项编号」；
   ⑭ 在 `:635` 与 `:751` 问两个不同问题。**未裁前 ①–⑤⑦⑨ 无法对账**，
   而 Owner 挂的 7 条里 6 条卡在这里。`SYNTHESIS.md` 属那 8 个不可改的暂存文件。
2. **Oracle 的本地 commit 授权（O5）无冷读落点**——只存在于会话消息
   （`_id dd0b7513`），BRIEF 全文 40 行里没有。建议补进 BRIEF 或 `A9`。
3. **`.pi/handoff/COMMUNICATOR-REPORT.md` 在 `.gitignore:8`**——18 条清单的原始出处
   指向一个会被清理的路径。
4. **scout 三问**：(a) 1080 个非 `SKILL.md` 文件要不要分档进清单（全列 2000+ 行）；
   (b) 锁文件 mtime 早于检查器，要不要派人只读重跑比对 sha256（现 `UNVERIFIED`）；
   (c) 处置裁决判据谁来给（Owner 的产品选择）。

## 7. 库内状态（本轮复跑）

| 检查 | 结果 |
|---|---|
| `render.py --check` | **PASS**（12 个派生文件逐字一致） |
| `check-closure.py` | **20 PASS / 1 FAIL** — 唯一 FAIL 为 C1：HEAD 未打 tag，**发布状态事实，非结构缺陷** |
| `check-consistency.py` | **7/7 PASS** |
| `compose-role.py --check` | **PASS**（9 角色 / 34 原则引用） |
| 文章原站逐字一致性 | **UNVERIFIED**（C9 自陈未核原站正文与本地缓存） |
| `provenance_policy.current.roles` / `.scripts` | **UNVERIFIED**（registry 自陈） |
| 真源 `registry.yaml` / `AGENTS.md` / `roles/` | **零改动** |
| 8 个 09/30 暂存文件 | **保留未动** |
| `upstreams/` | **零改动** |

**未 commit、未 push、未 tag。** 暂存区仍是原来那 8 项。

## 8. 一条纪律：本轮不自我验收

裁决 §5-C4 末条写明「**验收人不得是 `tpw-0930-driver`**」——
driver 是候选作者，自任其候选的验收人构成硬边界 1 在验收侧的对偶违反。
**修订后的候选仍需第三方验收，本轮到此为止。**

## 9. 下一步

等 Q1/Q2。可并行推进**不依赖这两个问题**的片：
scout 那 1080 个非 `SKILL.md` 载体的清单分档（Owner 第 3 条的实体进度）、
以及锁文件 sha256 漂移核对（F6）。
