# 0930 轮 · 独立性降级方案 —— 独立评价任务书（adversary: `tpw-0930-adversary-b`）

仓库：`/Users/yuantian/Developer/tim-professional-workflow`
你的名字：`tpw-0930-adversary-b`（Herdr agent 名 = Pi `--name` = Intercom 寻址名）
driver：`tpw-0930-driver`
被评价候选的作者：**`tpw-0930-driver` 本人**（Driver）

## 你是谁

`adversary`。**由没有产出该候选的人给出带理由的裁决。**

- 主产物 `A7` 裁决。`A7.fields = [stance, reason, conditions, independence(拟增)]`。
- 你的 `forbidden`（`roles/adversary.md`）：
  - **不得对自己产出的候选给出裁决**
  - **不得在没有证据的情况下宣布「不通过」**

**你与本任务的关系**：候选是 driver 写的，**不是你写的**，所以你可以裁决它。
但注意**反向约束同样成立**——你提出任何修订建议时，那条建议就成了**你**的候选，
**不得由你自己判定它成立**；要么交给第三方核，要么显式标注「本条未经独立复核」。

## 被评价的候选

`docs/history/handoff/0930-boundary1-CONFLICT.md`（150 行）
标题：**「独立性降级：两轴分离的条文修订方案」**

**这份文档的前身是同路径的初稿，driver 已按 Oracle 的语义校正整篇重写。**
初稿的两个错误候选（「放松 P6 让 UNVERIFIED 上线」与「把未经独立复核塞进 `A7.stance` 第四值」）
已在 §4 明确撤回。**你评价的是重写后的版本。**

## 语义基线（Oracle 已校正，driver 已据此重写）

Owner 的裁定**不是**「准许在没验过的情况下交付」。它是：

1. 单会话在**一次** Owner gate 之后，可按规则自审、自验。
2. 交付时**显著标注「未经独立复核」**，然后继续交付。
3. **不反复**向 Owner 索取许可。

据此两轴必须分开：

| 轴 | 记什么 | 取值 | 受 Owner gate 影响吗 |
|---|---|---|---|
| **轴 1 · 结论** | 验证实际观察到什么 | `PASS`/`FAIL`/`UNVERIFIED` | **不受影响** |
| **轴 2 · 独立性** | 结论由谁下的 | `独立复核`/`单会话自审` | **gate 只影响这一轴** |

**关键推论**：单会话自审**可以拿到 `PASS`**（真跑了、满足 `A4` 即可）；
**也可以是 `UNVERIFIED`**（环境坏、跑不了）——**一次 gate 不把它变 `PASS`**，
**P6 的 `PASS` 闸门（`registry.yaml:430`）一字不改。**

## 你要回答什么

给出一条 `A7` 裁决：`stance`（采纳／挑战／附条件通过）+ `reason`（指向具体锚点或一次真实运行）
+ `conditions`（附条件通过时的条件与验收人）。**`reason` 不指向「感觉不对」。**

**逐条攻这五个改动点**（文档 §3 改 1–5），每条给「成立／不成立／有条件成立」+ 证据：

### 攻点 1 · `A7.fields` / `A8.fields` 各加一个正交字段 `independence`

- **要查**：`independence` 真的与 `stance` 正交吗？有没有第三种状态被漏掉
  （例如「本该独立但 Owner 未配合」与「本就没法独立」是不是同一格）？
- **要查**：`A8.notes` 里 `verdict` 的定义是「PASS／FAIL／UNVERIFIED。环境故障既不算 PASS，
  也不得直接判成产品缺陷」（`registry.yaml:296`）——新增 `independence` 与这条是否冲突。

### 攻点 2 · 两条 `hard_rules` 的括注改指产物字段而非散文

- 现：`registry.yaml:406` / `:421` 括注指向 `roles/driver.md`「档位」一节。
- 拟：改指 `A7.independence` / `A8.independence`。
- **要查**：`check-consistency.py` 的 **S4** 到底核不核这个引用？
  driver 的说法是「S4 只核硬规则引用的 id 可解析；指向产物字段它就纳入 C4 的引用解析范围，
  指向散文则永远只能靠人读」。**你自己去读 `scripts/check-consistency.py` 的 S4 实现核实这句话。
  如果 driver 说错了，直接判该改动不成立。**

### 攻点 3 · `AGENTS.md:76` 拆成「结论断言 + 能力断言」两条

拟改措辞在文档 §3 改 3。**要查**：

- 拆成两条之后，**硬边界还有几条**？文档只处理了第 1 条，第 2–5 条的编号与交叉引用怎么办？
- 拟改措辞里「`independence` 必须记 `单会话自审`」——**谁记？** 记在 A7 还是 A8？
  如果两个会话（一个自审 A7、一个自审 A8）分别记，会不会不一致？
- 「**Owner 是否配合（配合／未配合／未答）记进 `A9`**」——`A9` 是 append-only 台账，
  **不是契约产物**。拿它当门禁凭据是不是「让契约判据依赖散文」？

### 攻点 4 · `P6` 加一条判据兑现「交付时显著标注」

- 拟加：`verify: A7.independence 或 A8.independence 为 单会话自审 时，交付物显著标注「未经独立复核」`
- **要查**：「显著标注」在契约里**能不能被机械核验**？driver 自己承认只能取「最弱可核形式」。
  **如果它本质上不可判定，那这条判据就是装饰**——判它不成立，并给出替代。
- **要查**：C13 要求每条退出判据显式声明 `write:` / `verify:`，这条拟加判据的声明对不对？

### 攻点 5 · 配套的检查器影响清单

driver 列了 C15 / C4 / C13 / render.py / S3 / S5 六项。**逐项去脚本里核实**，
特别是：

- **C15**：driver 说「新字段一旦被 `P4`/`P5`/`P6` 判据引用，就要求 `adversary.md` / `verifier.md`
  正文里逐字出现 `` `independence` ``，否则报『没人被要求填它』」。
  **去读 `scripts/check-closure.py` 的 C15 实现核实**（driver 读过了，但你必须自己核）。
- **实测反例**：driver 说 `grep -n "stance\|verdict" scripts/*.py` 零命中，
  **没有任何检查器读字段取值域**。核实这条，并判断：
  **取值域无保护时，新增一个二值字段是不是「引入了一个检查器看不见的约定」？**
  按 `AGENTS.md`「新增检查的保留判据」四条自审该不该加断言：
  (1) 保护的是哪条**真实断言**；(2) 给一个**会红的反例**；(3) 常见合法变体为什么**不会误报**；
  (4) **谁维护**。四条缺一条就别加。

## 硬边界

1. **只读本库。** 唯一可写落点：`docs/history/derivation-0930/ADVERSARY-VERDICT-INDEPENDENCE.md`
2. `upstreams/` 只读。3. 不许 `git add` / `git commit` / `git tag`。
4. **不许改候选文档本身。** 你只裁决，不修。
5. 每条结论带锚点 `路径:行号`；**读脚本要读实现，不读脚本头部的自述**。
6. 三态只用 `PASS` / `FAIL` / `UNVERIFIED`。
   **「我没找到证据」记 `UNVERIFIED`，不记成候选的缺陷。**
7. **不得在没有证据的情况下宣布「不通过」。** 同理，**不得在有反证的情况下放过。**

## 附：本次会话已实测的库状态（你可用，不必重做）

| 检查 | 结果 |
|---|---|
| `render.py --check` | PASS（12 个派生文件逐字一致） |
| `check-closure.py` | 20 PASS / 1 FAIL，FAIL 唯一为 C1 |
| └ C1 细节 | **不是「没有 release tag」**——仓里有 8 个 tag（`v1.0.0-frozen`…`v2.0.7`），
  最新 `v2.0.7` 指向 `f93449e`，**落后 HEAD `72d2b16` 8 个 commit**。所以是「**HEAD 未打 tag**」 |
| `check-consistency.py` | 7/7 PASS |
| `compose-role.py --check` | PASS |
| 8 个 09/30 暂存文件 | 保留不动，已核未改一字节 |
| `.decisions/ledger.tsv` | 37 → 42 行，**只追加**（`git show HEAD:` 与 `head -37` 的 md5 相同） |

## 汇报方式

完成后用 **Intercom** 发一条 `REPORT` 给 `tpw-0930-driver`：

- **一行 `stance`**：采纳／挑战／附条件通过
- **对改 1–5 逐条**：成立／不成立／有条件成立 + 一句理由 + 锚点
- **你判为不成立的条目**：给出可核的替代（若你有）
- **最少问题**：真正需要 Owner 裁的（**不要把「你没找到证据」写成问题**）
- 落点文件路径

长内容写落点文件，消息控制在终端一屏内。
