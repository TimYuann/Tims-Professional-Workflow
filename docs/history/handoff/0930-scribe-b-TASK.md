# 0930 轮 · 旧 18 条对账 + 暂存文件收口（scribe: `tpw-0930-scribe-b`）

仓库：`/Users/yuantian/Developer/tim-professional-workflow`
你的名字：`tpw-0930-scribe-b`（Herdr agent 名 = Pi `--name` = Intercom 寻址名，三层已核对一致）
driver：`tpw-0930-driver`

## 你是谁

`scribe`。**维护 append-only 决策台账，并让下一个会话能重建判断依据。**

- 主产物 `A9` 决策与记忆。台账在 `.decisions/ledger.tsv`。
- 你的 `forbidden`（`roles/scribe.md`）：
  - **不得修改或删除既有台账行**（只追加）
  - **不得在台账里写入无法追溯到证据的结论**

## 硬边界

1. **A9 台账只追加。** 不修改、不删除既有行。发现旧行写错了，**追加更正行**，不改它。
2. 不许 `git add`、不许 `git commit`、不许 `git tag`。**commit 由 driver 做**（Owner 已授权 driver 在独立检查后按任务范围本地 commit）。
3. `upstreams/` 只读。
4. 落点（你唯一可写的两个文件）：
   - `docs/history/derivation-0930/RECON-18-0930.md`（对账表）
   - `.decisions/ledger.tsv`（**只追加**）
5. 每个结论带证据锚点。**分清事实 / 推断 / 建议。**

## 任务一：把旧的「18 条」映射到 Owner 已给的答复

### 背景

上一轮 `docs/history/derivation-0930/DERIVATION.md`（1217 行，**已暂存**）§6 列了 **Q1–Q13** 十三个待裁点。
`SYNTHESIS.md` 里引用了一个更大的集合（正文出现「⑨⑩⑪⑬」这样的编号，指向 **18 条**清单）。
**「18 条」这个清单的原始出处你要自己找**——可能是 `SYNTHESIS.md` 的某一节、
`docs/history/handoff/0930-derive-TASK.md`（已暂存修改），或 `.pi/handoff/COMMUNICATOR-REPORT.md`
（**在忽略目录 `.pi/` 下，Oracle 说可读但不宜作唯一持久依据**）。**先找到它，找不到就记 UNVERIFIED 并写清。**

### Owner 在本轮已经明确答复的四条（原话要点，见 BRIEF）

BRIEF 在 `docs/history/handoff/0930-oracle-to-driver-BRIEF.md`，**你自己读原文**，下面是 driver 的转述，**以原文为准**：

1. **按角色与现场能力 fallback。** 优先独立且 Owner 可见的会话；不具备时看能否用可互通的子代理；
   再不行由同一会话承担。**不能把三种形态硬编码为全局档位。**
   形态 2（子代理）的环境事实**由当场探测**，不挡本轮。
2. **审查／验证缺独立会话时不假装独立，也不默认硬阻塞。** 进入 review/verify 时只需**一次** Owner gate：
   提供可复制粘贴的独立审查／验证启动 prompt，尽量降低 Owner 转发材料与结果的劳动。
   **如果得不到配合，单会话仍按相关规则自审、自验，交付时明确标注「未经独立复核」，继续交付；
   不要反复向 Owner 索取许可。**
3. **完整清点机制来源。** 三仓里的高价值方法不只在 `SKILL.md`，也在 playbooks、references、docs、
   commands、hooks、evals 等载体。先清点实际范围，读正文后才能判断吸收或拒绝。
   Matt 的 `in-progress` 九项是上游公开 beta、未进插件；**目前没有正式处置，不等于已拒绝或已吸收。**
   它们至少要在完整清单中可见，并区分「已发现」「已读」「已裁定」。
4. **文章是独立来源，可与上游技能交叉。** Owner 指定 poteto 两篇 pstack 长文进入来源体系，
   后续还会有 Matt Pocock 文章。`72d2b16` 已引入 `article_sources`、`sources/articles/` 与来源检查。

**另有 Oracle 在本轮追加的裁定（同样已定，不是待裁）：**

5. **本地 commit 可在独立检查后按任务范围做。** 8 个原有暂存文件先保留和对账。
   **push / tag / merge 仍需 Owner 授权。**

### 你要交付的对账表

对每一条旧清单项，给四个字段：

| 字段 | 取值 |
|---|---|
| **原编号** | 旧清单的编号（Q1、⑨、…）与它在 `DERIVATION.md` / `SYNTHESIS.md` 的行号锚点 |
| **原问题** | 一句话复述（**引用原文，不改写意思**） |
| **现状** | 三档之一：`Owner 已答` / `只定了原则未定操作判据` / `仍未回答` |
| **Owner 答复落点** | 对应上面第 1–5 条哪一条；**若答案是「仍未回答」，写清缺的是什么** |

**判定纪律：**

- 「Owner 说了方向」**不等于**「库内条文已改完」。BRIEF 明写：
  「这些是 Owner 的目标或已接受的方向，**不是说库内相关条文已经全部改完**」。
  所以你的 `现状` 栏要额外区分：
  - `已答且库内已一致`
  - `已答但库内条文仍冲突/未改` ← **这一类是最有价值的，请重点标出并给冲突锚点**
- **不要**把 `SYNTHESIS.md` 的 advisory 切片当可直接执行的 A5（该文件自己就这么写）。
- **不要**回写历史报告冒充原稿已知。
- 每条都要能追溯到 BRIEF 原文或 Oracle 裁定的原文。

## 任务二：8 个既有暂存文件的对账

`git status` 实测（driver 已核，你复核）：

```
## main...origin/main [ahead 2]     HEAD = 72d2b16
A  docs/history/derivation-0930/DERIVATION.md
A  docs/history/derivation-0930/SYNTHESIS.md
A  docs/history/derivation-0930/UPSTREAM-RESCAN.md
M  docs/history/handoff/0930-derive-TASK.md
A  docs/history/handoff/0930-herdr-pitfalls-TASK.md
A  docs/history/handoff/0930-synth-TASK.md
M  docs/history/handoff/0930-upscan-TASK.md
A  docs/history/handoff/HERDR-PI-PITFALLS.md
?? docs/history/handoff/0930-oracle-to-driver-BRIEF.md
```

**这 8 个是 09/30 旧会话的交付，不是本轮改动。** 处置：**保留原样，一个字节都不改。**

你要交付的是**对账**，不是处置：

1. 逐个文件给：它是什么、谁产出（哪个会话名）、产出时基于哪个 commit、
   **它现在还有效吗**（有没有被 `72d2b16` 之后的事实推翻）。
2. `HERDR-PI-PITFALLS.md`（793 行）来自**另一个项目**（UCBIP）的调研，是**搬运候选**，
   **不是本库纪律**。请核：里面有没有已经在本库 `AGENTS.md` 里存在的规则？
   有的话标出**重复**，供 driver 决定是否收编。
3. **未跟踪的 BRIEF 文件**（`0930-oracle-to-driver-BRIEF.md`）是否应入库？给出你的建议与理由。
4. **不要 stage、不要 commit、不要删任何一个。**

## 任务三：A9 台账追加

`.decisions/ledger.tsv` 现有 **36 行数据**（`wc -l` = 37，含表头）。最后一批是 0929 轮 scribe 写的，
**0930 轮尚无 A9 行**。

你要**追加**本轮的起手行（不是全部细节，是让下一个会话能重建判断依据的最小集）：

- 本轮 driver 是谁、用什么模型纪律、起了几位 worker、命名约定
- 上面 1–5 条裁定的落点（指 BRIEF 行号，不复述全文）
- 8 个暂存文件的处置决定（保留不动）
- 检查基线（下面这张表）

**格式纪律**（`roles/scribe.md` + 0929 轮 scribe 已确立的口径）：

- 8 栏，`actor` 栏写**你自己的名字** `tpw-0930-scribe-b`。
  0929 轮留下的口径问题是「写入者 vs 决策人哪个进 actor 栏」——**driver 尚未裁定**。
  你按 **0929 轮 scribe 自己确立的做法**（actor = 执笔者）写，并在该行的说明栏里**显式记下这个未裁定的口径问题**。
- 工具只认 `TPW_ACTOR` 环境变量，**没有它就没有归因**。写入前确认它已设。
- 只追加。不改既有行。

## 当前检查基线（driver 本轮实跑，你可以复跑核对）

| 检查 | 结果 |
|---|---|
| `python3 scripts/render.py --check` | **PASS** — 12 个派生文件逐字一致 |
| `python3 scripts/check-closure.py` | **20/21 PASS，1 FAIL** |
| └ C1 | **FAIL** — 「当前 commit 上没有 tag」。**这是发布状态，不是结构缺陷。** |
| `python3 scripts/check-consistency.py` | **7/7 PASS** |
| `python3 scripts/compose-role.py --check` | **PASS** — 9 角色 / 34 条原则引用 |
| 文章原站逐字一致性 | **UNVERIFIED**（C9 自陈未核原站正文与本地缓存） |
| `provenance_policy.current.roles` / `.scripts` | **UNVERIFIED**（registry 自陈） |

## 汇报方式

- 完成后用 **Intercom** 给 `tpw-0930-driver` 发一条 `REPORT`，正文只写：
  **已变事实 / 证据位置 / PASS·FAIL·UNVERIFIED / 落点路径 / 需要 driver 或 Owner 回答的最少问题**。
- 长内容写进 `RECON-18-0930.md`，消息里只给路径 + 摘要。
- 查不到、读不到、无法判定的，**照实记 UNVERIFIED**，不要编。

## 你的判断边界

- 你**不裁决**业务取舍，**不决定**任何条文该怎么改。
- 你**只追加**台账，**不改**任何既有行。
- 你**不 stage、不 commit、不删**任何既有暂存文件。
