# 0930 轮 · 第二轮：独立审计发现的规格漂移修复

仓库：`/Users/yuantian/Developer/tim-professional-workflow`
你的名字：`tpw-0930-driftfix`
driver：`tpw-0929-driver`

## 背景

一个**独立审计会话**（不属本库任何角色，Owner 直接派的）逐行读完了 9 份 `roles/*.md`
与 45 个技能，判出 8 条缺口。其中 3 条是**纯文本规格漂移**，仲裁依据明确，就是你的活。
另外几条是语义问题，driver 已经交给 Owner 裁定，**不在你的范围**。

**硬边界：只改下面三处点名的地方，一处不多。** 别的即使看到问题也写进报告，不要动。

## 硬边界

- **只能改 `skills/decision-ledger.md`、`skills/research.md`、`skills/implement.md`、
  `roles/architect.md` 这四个文件。**
- 不许碰 `workflow/registry.yaml`、`scripts/`、`docs/`、`README.md`、`.pi/`、其他 `skills/`、其他 `roles/`。
- **不许 `git commit`、不许 `git tag`、不许改 `VERSION`。**
- 不许为了让检查变绿而削弱检查。

---

## 任务 1：`A9` 字段规格歧义

**现状**：

- `roles/scribe.md:40` —「`A9` 决策台账，**八个字段**，每行一条。前四栏是身份，后四栏是内容」
- `roles/scribe.md:53` —「**前四栏不是可选项。**」
- `docs/ledger.md:8` —「八栏：前四栏是身份」
- `skills/decision-ledger.md:24` —「**每次只写四件事**：`decision` / `why` / `evidence` / `result`」

**问题**：只读 `decision-ledger.md` 的人会以为一行只需要四栏，而那四栏恰好全是**内容栏**，
身份栏被整条略过——而身份栏缺的正是「多 agent 并发时谁写的哪一行」。

**registry 是仲裁者**：`A9.fields` = `actor, run, subject, phase, decision, why, evidence, result`（八栏）。

**要改**：把 `skills/decision-ledger.md:24` 改清楚——

- 一行是**八栏**，`decision-ledger` 这条技能负责的是**后面四栏内容**（`decision` / `why` /
  `evidence` / `result`），**不是整行的全部**；
- 前面四栏（`actor` / `run` / `subject` / `phase`）是**行格式的一部分，不是可选项**，
  同会话可由 `ledger.sh` 代填，但**不能因为「我只写四件事」就整条略过**；
- 补一句交叉引用：完整字段规格看 `roles/scribe.md` 的 A9 表格与 `docs/ledger.md`。

**不要**改 `roles/scribe.md`——它是对的。

---

## 任务 2：`A2` 与 `A6` 的字段数漂移

**registry 是仲裁者，实测值**：

- `A2.fields` = `claims, evidence, gaps` → **3 个**
- `A6.fields` = `subject, change, runnable, known_gaps` → **4 个**

**三处漂移**：

| 位置 | 原文 | 判定 |
|---|---|---|
| `roles/builder.md:46` | 「`A6` 实现候选，**四栏**全部非空」 | ✅ 对，**不要动** |
| `skills/implement.md:30` | 「附上 A6 的全部**三个字段**」 | ❌ 错，A6 是 4 个 |
| `skills/research.md:40` | 「A2 事实集，**四个字段**：」后面只列了 3 个 | ❌ 自相矛盾 |

**要改**：

1. `skills/implement.md:30` —「三个字段」改「四个字段」，并把四个名字列出来
   （`subject` / `change` / `runnable` / `known_gaps`）。
2. `skills/research.md:40` —「四个字段」改「三个字段」。顺便核一遍该文件后面有没有别的
   地方也在暗示 A2 有第 4 个字段，有就一并改成 3。

**顺带一件（同一个根因，一并做）**：`gaps` 这个词在两处含义不同——
`roles/scout.md:44` 与 `skills/research.md:47` 的 `gaps` 是「**查过但没查到的**」，
而 `skills/recall-context.md:57` 的 `gaps` 是「**反复出现的问题**」。两者同名不同义。
在 `skills/recall-context.md:57` 上把它的说法改成不与 `A2.gaps` 撞名的写法
（例如「反复出现的问题」列表，**不要**再叫它 `gaps`），并加一句「这不是 `A2.gaps`」。
**这个文件不在我上面点的名单里，但它属于任务 2 的同一个根因，一并改。**

---

## 任务 3：`A9` 写入权表述冲突

**现状**：

- `roles/architect.md:89` —「我发现的额外机会，写进 `A9` 交给 Owner 判断」
- `roles/architect.md:112` —「不改 → **在 `A9` 写下**不修的理由（或 Owner 的裁决）」
- `roles/architect.md:118` —「冻结 `A4`，把冻结这件事本身**写进 `A9`**」
- `skills/documentation-and-adrs.md:68` —「它也**不直接写台账**——`A9` 的唯一产出方是
  `scribe`。**把下面四栏交给 `scribe` 追加**」

**问题**：`architect.md` 三处读起来像 architect 直接写台账，而 registry 里
`A9.producer = scribe`，`documentation-and-adrs.md` 已经写对了。

**要改**：只改 `roles/architect.md` 那三处，把「写进 A9」改成明确的交接措辞——
「**把……交给 `scribe` 追加进 `A9`**」，或等义的写法。**不要**改
`skills/documentation-and-adrs.md`，它是对的。

**这是第二轮 rolefix 拒绝做的那类事的同一类**：worker 上一轮拒绝在角色文字里把 `A7`
暗改成另一套枚举，理由是「那会变成第二份真源」。**这一条是同一个道理的反面——
`documentation-and-adrs.md` 才是对的，architect 要向它对齐。**

---

## 不要碰的（driver 另案处理）

独立审计还判了几条**语义问题**，driver 已经交给 Owner 裁定，**不是你能改的**：

- driver 的映射决定没有产物归属、也没有退出判据（`P0` 的四条判据里没有映射那条）
- 「退回」在 9 份角色文件里出现 35 次，却没有任何地方说它记在哪、什么形态、谁需要看到
- 角色文件不声明自己需要什么 runtime 能力（试装时 scout 被派了一个没有 shell 的 agent）

**你如果在这些方面看到具体的文字证据，报告里写，别动手。**

---

## 交付

报告写 `.pi/handoff/0930-driftfix.md`：

1. 三个任务**各 2-4 行**：实际改了什么、依据 registry 的哪个字段。
2. **「我顺手核到但没改的」**。
3. **「我对判定的疑问」**——如果你认为某条漂移的仲裁依据不是 registry 说了算，说出来。
4. 三个检查的实际输出（`check-closure.py` 期望 20/21，唯一 FAIL 是 C1「当前 commit 没有 tag」）。
