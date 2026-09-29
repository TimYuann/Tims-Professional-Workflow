# 0930 轮 · 完整上游机制来源清点（scout: `tpw-0930-scout-b`）

仓库：`/Users/yuantian/Developer/tim-professional-workflow`
你的名字：`tpw-0930-scout-b`（Herdr agent 名 = Pi `--name` = Intercom 寻址名，三层已核对一致）
driver：`tpw-0930-driver`

## 你是谁

`scout`。**找事实，不给结论。查过没查到的，也要写下来。**

- 主产物 `A2` 事实集的形状：`claims`（事实断言）+ `evidence`（每条带 `仓/路径:行号` 锚点）。
- 你的 `forbidden`（`roles/scout.md`）：**不得在没有读正文的情况下声称已吸收或已理解**；
  **不得把「没人提过」当作「不存在」**。
- 本轮你**不裁决任何处置**。「该不该吸收」是 `adversary` 的活，你交的是清单与证据。

## 硬边界

1. **只读。** 本库除下面指定的**唯一一个落点文件**外，一个字节都不许改。
2. `upstreams/` **只读**（本仓硬边界，永不修改）。
3. 不许 `git add`、不许 `git commit`、不许 `git tag`。
4. 落点（唯一可写）：
   `docs/history/derivation-0930/UPSTREAM-INVENTORY-0930.md`
5. **空结果必须写。** 「这条线上什么都没有」是有效结论，比编一个更有价值。
   上一轮就是「没写正文就算吸收」栽的（`AGENTS.md` 改动纪律第 1 条）。
6. 每个事实断言带锚点 `仓/路径:行号`。**摘录一律逐字**，解释写在引用之外。
7. 三态只用 `PASS` / `FAIL` / `UNVERIFIED`。**「环境/范围给不了」既不记 PASS，也不判成缺陷——记 UNVERIFIED 并写清缺什么。**

## 背景：为什么要做这件事

本库 `workflow/registry.yaml` 的 `upstream_dispositions` 有 **101 条**，每个上游 skill 恰好一条，
由 `scripts/check-closure.py` 的 C7 对 `upstreams.lock.yaml` 核对。

**Owner 的要求（已明确）**：三仓里的高价值方法不只在 `SKILL.md`，也在 playbooks、references、
docs、commands、hooks、evals 等载体。**先清点实际范围，读正文后才能判断吸收或拒绝。**
处置表现在**只有「已裁定」一格**（`absorbed` / `rejected`），没有「已发现」「已读」两格，
所以「没进处置表」既读不出是已发现、是未读，还是已拒绝——**Owner 要求至少让它们在完整清单里可见**。

## driver 已实测的基线（你要求复核，但不必重做）

以下数字是 driver 在派工前用只读命令实测的，**你可以直接采信，也可以独立复核**：

- `upstreams/` 共 **1344** 个文件，其中 `SKILL.md` **159** 个。
- `upstreams.lock.yaml` 枚举 **101** 个。
- ⇒ **58 个 `SKILL.md` 完全不在锁文件里**，即处置表结构上就看不见它们。

58 个的分布（driver 实测）：

| 位置 | 数量 | 为什么不在锁里 |
|---|---|---|
| `cursor-plugins/cursor-team-kit/skills/*` | 18 | `REPOS` 没有 `cursor-team-kit` 这条路径 |
| `mattpocock-skills/skills/in-progress/*` | 9 | `SKIP_DIRS` 含 `in-progress` |
| `cursor-plugins/third_party/*` | 6 | `SKIP_DIRS` 含 `third_party` |
| `cursor-plugins/pstack/automations/benny/skills/*` | 3 | `SKIP_DIRS` 含 `automations` |
| `cursor-plugins/grok-voice/*` | 4 | 同 cursor-team-kit，`REPOS` 无此路径 |
| `cursor-plugins/ralph-loop/*` | 3 | 同上 |
| `cursor-plugins/thermos/*` | 3 | 同上 |
| `cursor-plugins/{advisor,agent-compatibility,cli-for-agent,continual-learning,create-plugin(×2),cursor-sdk,docs-canvas,orchestrate,pr-review-canvas,teaching(×2)}` | 12 | 同上 |

**根因（driver 推断，你复核）**：`scripts/_render-lock.py:23-27` 的 `REPOS` 只登记 3 条路径
（`cursor-plugins/pstack`、`mattpocock-skills`、`addyosmani-agent-skills`），
且 `:28-29` 的 `SKIP_DIRS` 排掉 7 个目录名。`cursor-plugins/` 下实际有 **16 个插件目录**，
**只有 `pstack` 在 `REPOS` 里**，另外 15 个从未被 walk。

### 非 SKILL.md 载体（同样结构性地不可见）

- `addyosmani-agent-skills/` 根下有 `agents/`、`commands/`、`docs/`、`evals/`、`hooks/`、
  `references/`、`scripts/` —— **`_render-lock.py` 只 walk `base/"skills"`，这些目录一个都不进枚举**。
- 已知线索（**你必须独立核，不要照抄**）：UPRESCAN 提到 `in-progress` 9 个、`.changeset` 2 份、
  `evals/` 三个沉默桶；`SKIP_DIRS` 里有 `references` 意味着**任何 skill 自带的 references/ 也不被枚举**。

## 你要交付什么

一份**清点清单**，不是处置意见。每条上游机制条目给四个字段：

1. **身份**：`仓/相对路径`（尽量给到具体文件，不只是 skill 目录名）
2. **载体类型**：`SKILL.md` / `references` / `docs` / `commands` / `hooks` / `evals` / `playbooks` / `automations` / `.changeset` / 其他
3. **来源状态**（Owner 要的三格，缺一不可）：
   - `已发现` —— 你知道它存在，但**没读正文**
   - `已读` —— 你**读了正文**，能给出行号锚点与一句「它到底讲什么」
   - `已裁定` —— `registry.yaml:upstream_dispositions` 里已有对应条目（给出那条的 id 与 outcome）
4. **证据**：`仓/路径:行号`；读了正文的给逐字摘录

**必须单独成节回答的四个问题：**

- **Q-A** 完整枚举范围到底是什么？`SKILL.md` 之外的载体**一共有多少个文件**、分几类、每类多少？
- **Q-B** 58 个不在锁文件里的 `SKILL.md`，**哪些是本库可能用得上的方法**？给出路径 + 一句话它讲什么。
  **只描述，不裁决吸收。**
- **Q-C** `in-progress` 9 个（`claude-handoff`、`implement-spec`、`loop-me`、`pr`、`retro`、
  `setup-ts-deep-modules`、`writing-beats`、`writing-fragments`、`writing-shape`）——**逐个读正文**，
  给出「讲什么 + 与本库现有 `skills/` 是否有重叠 + 重叠在哪一条」。这是 Owner 点名要「至少可见」的一批。
- **Q-D** `registry.yaml` 里**判 `rejected` 但你没找到对应正文**的条目有哪些？
  （UPRESCAN 记过 N12：`registry.yaml:1180` 判 rejected 但没读正文。**独立复核，别照抄。**）

## 与已有研究的关系（避免重复劳动，也避免被其结论带跑）

- `docs/history/derivation-0930/UPSTREAM-RESCAN.md`（694 行，**已暂存**）是上一轮的只读重扫，
  含 R1/R2/R3 三个盲区与 N1–N12 编号。**读它，但它的结论要独立复核**——
  它的 §0 已经自陈过一次归因错误（把活枚举源写成死代码 `check-closure.py:201-231`）。
- `docs/history/derivation-0930/DERIVATION.md`（1217 行，**已暂存**）是 A1–A9 × 三形态 × 六问的推演，
  §5 是库内登记盲区。你做的是**库外枚举**的盲区，**两者方向相反，不要混**。
- `docs/history/derivation-0930/SYNTHESIS.md`（877 行，**已暂存**）的 S1/S2 两节与本任务直接相关，
  但它是 **advisory 方向候选，不是裁定**，不要当既成事实引用。

## 汇报方式

- 完成后用 **Intercom** 给 `tpw-0930-driver` 发一条 `REPORT`，正文只写：
  **已变事实 / 证据位置 / 当前 PASS·FAIL·UNVERIFIED / 落点文件路径 / 需要 driver 或 Owner 回答的最少问题**。
- 长内容写进落点文件，消息里只给路径 + 摘要（消息要短到能在终端一屏读完）。
- 查完没查到的**照实说 UNVERIFIED**，不要为了让清单显得完整而猜。

## 你的判断边界

- 你**不决定**任何条目该不该吸收、该不该改判据、该不该加检查项。
- 你**不改** `registry.yaml`、`roles/`、`skills/`、`scripts/`。
- 你发现的问题，**只记录，不修**。修是 driver 派给下一个角色的事。
