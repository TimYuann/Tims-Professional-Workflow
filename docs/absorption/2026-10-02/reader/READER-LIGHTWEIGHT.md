# READER-LIGHTWEIGHT · 案例2「轻量项目从零接入 TPW」

读者状态：全新消费读者，无先前 baseline 阅读，只读 fixed 对象。
读取纪律：全部内容经 `git -C .worktrees/night-2026-10-01 show <commit>:<path>` 打开；未在工作区读取任何 mutable 文件。

## 0. 消费定位（已核对）

- commit：`0e2bc4ba72ab8825b84e0e455de9ae5a2df26fe9`（`cat-file -t` = commit）
- core 子树：`professional-workflow/`，tree `1f509b6f0caebdb8f03046e84608ba98864e3a5e`（与任务给定一致；`ls-tree -r` 共 51 个文件）
- 本报告本身是唯一写出的文件，路径见文首/文末。

## 1. 实际打开的 fixed 文件

按要求先读的六个对象（含路径修正，见下）：

| # | 实际读取路径 | 备注 |
| --- | --- | --- |
| 1 | `professional-workflow/ADOPTION.md` | 全文 |
| 2 | `adoption-examples/cross-module-start.md` | **不在 `professional-workflow/` 内**，见下 |
| 3 | `professional-workflow/README.md` | 全文（含 Use 四步） |
| 4 | `professional-workflow/profiles/README.md` | 全文 |
| 5 | `professional-workflow/charters/README.md` | 全文 |
| 6 | `professional-workflow/methods/README.md` | 全文 |

为完成本报告额外打开的 fixed 文件：

| # | 实际读取路径 | 为什么读 |
| --- | --- | --- |
| 7 | `professional-workflow/authority/README.md` | 区分「权限/授权」来源时核对 authority 投影的授权地位 |
| 8 | `professional-workflow/charters/template.md` | 案例2 的「最小实例」需要真实 Charter 字段 |
| 9 | `professional-workflow/profiles/implementation.md`（前 60 行） | 核对 Profile 自身是否携带授权语 |

**找不到的文件（实际观察，不是推测）：**

- `professional-workflow/adoption-examples/cross-module-start.md` 在 commit `0e2bc4ba` 中不存在。该 commit 的 `professional-workflow` 子树共 51 个文件，没有任何 `adoption-examples/` 目录。
- 同一 commit 的**仓库根**存在 `adoption-examples/cross-module-start.md`（另有 `adoption-examples/ucbip.md`）；我读取的是这一份。`ADOPTION.md` §7 自身把这两个例子标为包外（`../adoption-examples/…`），并写明「只 vendor `professional-workflow/` 时这两个例子可能不在副本中，不影响 core」。因此不存在「core 内路径」的该文件版本。

## 2. 我如何区分 Profile 与权限/授权

读到的机制是分层且互不生成的：

1. **Profile = 判断配置，不是授权。** `profiles/README.md`：「预设是可缓存的判断配置，不是职位表，不产生任务决定权，也不自带方法正文」；选择规则明写「**选择预设 ≠ 授予权限**。实际责任、范围、输入/输出、工具与独立性由本次 Instance Charter 绑定」。`profiles/implementation.md` 开头同样写「选用本预设不获得任务授权」。
2. **Charter = 对已有授权的记录，不创造授权。** `charters/README.md`：「Choosing a Profile is composition, not authorization. A Charter records authority already granted elsewhere; writing "allowed" here does not create that grant.」`charters/template.md` 的 Delegation source 字段：「if absent, no authority is implied」。
3. **包/方法/工具都只是上下文或能力，不是许可。** `README.md` 结尾：「Nothing in this directory alone grants decision authority, permission to change an object, risk acceptance, or permission for a consequential action.」`ADOPTION.md` 结尾同义；`charters/README.md`：「Tool access does not grant permission; permission does not bypass tool restrictions.」`authority/README.md`：冻结投影的摘要一致「do not grant authority to a task, alter the source of truth, or prove an active delegation」。
4. **Profile 名不激活方法**：`ADOPTION.md` §5「Profile 名不激活方法；方法由 Charter 按路径绑定」；`README.md` Use 第 3 条同义。

因此我的区分法：**Profile 回答「缺哪种判断、用哪套心智模型」；授权只能来自别处真实存在的委托（谁委托、可改什么、动作边界），由 Charter 引用并分开记录接受/验证/动作/关闭（`ADOPTION.md` §3、`charters/README.md`）。任何"允许"字样、工具权限、包内容、Profile 选择都不能生成授权。**

## 3. 案例2 · 轻量项目从零接入

**案例条件（读者设定的演示，不是读到的项目事实）：** 一个没有既有治理的小项目——无 registry、无角色表、无 gate、无既有 TPW 历史；本次只有一个有界的首个任务（下面以「修复一个已有可复现失败的局部缺陷」为演示任务）。以下步骤全部依据读到的文本，演示任务本身可替换。

### 3.1 最小实例要装什么

按 `ADOPTION.md` §2/§3/§5、`README.md` Use、`charters/template.md`：

1. **固定版本引用**：源仓库 + commit/tree + 包路径（本次即 `0e2bc4ba` / tree `1f509b6f…` / `professional-workflow/`）；Charter 的 Accepted inputs 与任务输入引用同一对象，不写「最新 main」（§4：分支 tip /「最新」不是固定版本）。
2. **一条常驻短指针**：指向固定版本的接入/选择入口，放项目自己的任务启动处或已有文档；不要求统一文件名，也不要求项目有 AGENTS 文件（§5）。
3. **最小任务内容**（无既有治理时"缺什么补什么"）：
   - 目标：做什么、非目标；
   - 授权：谁委托、可改哪些对象、工具/动作边界与保留项；
   - 保持面：不得改的行为/接口/政策；没有就写「无既定冻结面，本次结果本身是待接受对象」；
   - 关闭依据：谁验收、什么算完成、证据放哪、剩余风险谁接受；
   - 人类保留决定：写下该决定及未决状态，不代替人类决定。
4. **一份填好的 Instance Charter**：从 `charters/template.md` 复制，字段换成真实对象——Profile 路径、Instance、Task/outcome、Delegation source、Object scope、Accepted inputs、Applicable methods（精确 `methods/` 路径 + 接受版本；**不需要就绑 none**，方法正文不产生授权/触发/范围）、Responsibility、Delegated decisions、Preserve/do not do、Tools and actions、Deliver、Independence、Recall、Acceptance/verification/action/closure。
5. **只加载本任务需要的正文**：选中的 Profile →（需要时）authority 上下文 → 填好的 Charter → 绑定的方法文件 → 任务输入（当前事实 + 固定引用），按此顺序拼成启动文本；示例命令形如：
   `cat profiles/implementation.md charters/<filled-charter>.md methods/<bound>.md path/to/task-input.md`
   （`ADOPTION.md` §2.5、`README.md` Use 第 4 条；路径与示例可替换）。
6. **到此为止**：不为采用 TPW 建 registry、schema、常驻角色或 gate（§3）；「够用就不造 composer、生成器或安装器」（§6）。上述最小内容通常就是「一段任务简述 + 一份填好的 Charter」。

### 3.2 本次具体交付（演示任务）

`ADOPTION.md` §3 说明最小接入的产物是任务简述 + 填好的 Charter；任务本身的交付物由 Charter 的 Deliver 决定。若采用 `cross-module-start.md` 例 1 的最少模式（该文件自标「非规范示例」），一个轻量缺陷修复的实例可装为：

- 一个 E 实例：patch + 自测命令与观察 + 回归覆盖（只作可核对输入）；
- 一个独立 F 实例：对固定版本给出三态结论（PASS/FAIL/UNVERIFIED）、覆盖范围与限制；独立性由真实委托声明，E 自测只作 F 的可核对输入；
- 局部改动可引用已有契约，加一段本次差分与委托范围，「不要求先做 Plan」（例 1 原文；末尾也说明实例数、是否先做 Plan、是否拆分 F 都由真实任务决定）。

注意：以上示例模式不构成流程模板或授权（例 1/例 2 文件头与末尾均自标非规范、不授予权限）。

### 3.3 召回/升级路径

- **召回（任务内）：** `charters/template.md` Recall 字段——出现使依赖工作停止的发现时，记录受影响对象、事实、影响，交 Driver 路由到拥有该边界的责任方；**只有 human-reserved 决定或人类验收才经 Voice**。`cross-module-start.md` 例 1：契约缺失、矛盾或无法在委托范围内保持 → 停止依赖它的工作并记录；例 2 末尾：事实推翻承诺 → 回 B/C；接口/约束/验证依据要变 → 回 D；超出委托或触碰保留决定 → Driver 路由；**实现者不能自行接受上游变更**。
- **升级（TPW 版本）：** `ADOPTION.md` §4——选新的固定 commit/tree → 只 diff 包内两版 → 找出受影响的约定、方法、Charter 字段与假设 → 只重核这些、只重跑有效性依赖被改约定的证据；旧证据不因换版自动成立，也不需要全量重评；mutable `main` 不能偷换本次依据（要用新版本先升级、再重核、再改 Charter）。

### 3.4 缺什么会无法开工（具体）

- **缺固定版本（源仓库 + commit/tree + 路径）**：Charter 的 Accepted inputs 与任务输入无法给出可核对引用；「分支 tip / 最新」不是固定版本（§4）。
- **缺真实委托来源**：谁委托、授予什么、可改哪些对象填不出来；`charters/template.md`「if absent, no authority is implied」，写「允许」也不产生权限（`charters/README.md`）。没有它，任何有后果动作都无依据。
- **缺验收/关闭责任**：不知道什么算完成、证据放哪、剩余风险谁接受（§3 关闭依据）。
- **缺目标与非目标**：Task/outcome 无法填，也就无从按「缺的 judgment」选 Profile。
- **缺任务输入（当前事实 + 固定引用）**：启动文本无法装配（§2.5）。
- **缺人类保留决定的明示**：涉及 human-reserved 决定时只能停在未决状态，不代替人类决定（§3）。

不阻塞开工的缺口（文本允许显式记账）：「保持面」确实没有时可写「无既定冻结面，本次结果本身是待接受对象」；适用方法可绑 none；常驻上下文可只有一条短指针。

## 4. 消费 commit

本报告消费 fixed 对象：commit `0e2bc4ba72ab8825b84e0e455de9ae5a2df26fe9`，core 子树 `professional-workflow/` = tree `1f509b6f0caebdb8f03046e84608ba98864e3a5e`。报告内的所有引用均出自上述对象内的文件；未使用任何 mutable 工作区内容。
