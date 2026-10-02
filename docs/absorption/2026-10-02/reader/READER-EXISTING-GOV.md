# READER-EXISTING-GOV · 案例1：已有治理仓库引入 TPW（只读消费报告）

State: reader consumption test artifact (case 1). 非规范、不授权、不构成流程模板；本文件是本次消费测试的唯一写入。
读取方式：全部产品文件经 `git -C <night> show <commit>:<path>` 读固定对象；未读产品文件的 working tree 版本。

- Fixed product object：night 仓 `/Users/yuantian/Developer/tim-professional-workflow/.worktrees/night-2026-10-01`，
  commit `0e2bc4ba72ab8825b84e0e455de9ae5a2df26fe9`，core subtree `1f509b6f0caebdb8f03046e84608ba98864e3a5e`
  （本报告实测 `git rev-parse 0e2bc4ba:professional-workflow` 与题设一致）。
- 写入边界：只写本文件。未改任何产品文件、未改 working tree 中其他文件。

## 1. 实际打开的 fixed 对象清单（readback）

按要求先读的六个（读取顺序）：

1. `professional-workflow/ADOPTION.md`（全文）
2. `adoption-examples/cross-module-start.md`（全文）
3. `professional-workflow/README.md`（含 `## Use`）
4. `professional-workflow/profiles/README.md`（全文）
5. `professional-workflow/charters/README.md`（全文）
6. `professional-workflow/methods/README.md`（全文）

补充打开（仍来自同一 fixed commit）：

7. `professional-workflow/charters/template.md`（全文；用于核对最小实例的字段形状）
8. `professional-workflow/authority/README.md`（全文；冻结责任边界的来源身份与字节核对说明）
9. `adoption-examples/ucbip.md`（全文；案例1 的已有治理适配例，非规范）
10. 目录树清单（非文件正文）：`git ls-tree` on `professional-workflow/`、`adoption-examples/`、`docs/absorption/`。

**未打开（声明限度）**：`profiles/` 下任一 Profile 正文、`methods/` 下任一方法正文、
`authority/RESPONSIBILITY-BACKBONE.md` 正文。因此本报告只验证入口/选择/装配层与其自述边界，
不对正文质量、Profile 组合细节或责任基线内容作判断。

## 2. 此前已读 root baseline 的限度（必须报告）

进入本测试前，我只读过 root 仓 `/Users/yuantian/Developer/tim-professional-workflow`
（`main@d3aab6a`）的 `README.md` 与 `AGENTS.md`。该读取的限度如下，全部为本测试实测：

- root baseline 的 core subtree 是 `7c814e54c5e775045bc1c5155e3c181ceb1345fb`（旧 core，2026-10-01 基线），
  而本测试的 fixed 对象 core subtree 是 `1f509b6f0caebdb8f03046e84608ba98864e3a5e`——两者不是同一对象。
- 实测差异：`git ls-tree -r d3aab6a -- professional-workflow` 只有 **21** 个文件，**没有** `ADOPTION.md`，
  也没有 2026-10-02 absorption batch 的任何方法文件；`adoption-examples/` 只有 `ucbip.md`，
  **没有** `cross-module-start.md`。fixed 对象下 `professional-workflow/` 有 **51** 个文件。
- 因此 root README（含其“已接受身份与状态”）只能作导航/历史参照，不能作为本次消费的依据；
  其中关于包状态的描述在 fixed 对象上以 `methods/README.md` 的当前选择表与
  `docs/absorption/2026-10-02/LEDGER.md` 的批次身份记录为准（LEDGER 属过程记录、非 Accepted core）。
- 另注：night 仓 HEAD `2b594e9` 的 core subtree 同样为 `1f509b6f…`（HEAD 较 0e2bc4ba 仅 docs/台账提交），
  但本报告不据此用 HEAD 替代题设 fixed commit 的字节。

## 3. 案例1：已有治理仓库引入 TPW（ADOPTION.md §3「映射，不重建」落地）

### 3.1 原则与映射表

已有职责/授权/记录/交付惯例的仓库，**用项目自己的对象填 Charter，不把项目搬进本包词表，不建第二台账/registry/schema，
不为采用 TPW 设常驻角色或 gate**（`ADOPTION.md` §3；`methods/README.md` 与包尾均声明不授予授权）。
映射（`ADOPTION.md` §3 表）：

| 项目已有 | 接到哪 |
| --- | --- |
| 职责/角色/槽位 | 其实际持有的 judgment 与 A–F/Driver 的对应；只映射，不改名、不按 Profile 重设岗位 |
| 授权来源（谁委托、谁接受、谁批动作） | Charter 的 Delegation source / Acceptance / 动作边界；接受、验证、动作、关闭各自分开 |
| 已接受事实（契约、spec、任务状态、政策） | Accepted inputs（带版本与决定人）；本包不复制成第二份台账 |
| 交付物与证据位置 | Deliver 指向项目自己的对象/位置；方法只加证据纪律，不建第二状态源 |

已治理实例的观察锚点在 `adoption-examples/ucbip.md`（非规范、时点观察、不授权）：它记录了下游自己的
Driver 槽位、单一 `main` writer（Integrator）、各卡的 `CARD-STATE`、`docs/evidence-ledger.md` + receipts，
并记录下游自己已写明「外部包只提供方法正文」「方法不产生权限」。该例还记录了反例：此前的冷启动 trial
在 `docs/` 内新增 `docs/decision-ledger.md`，因制造竞争台账权威被下游 drift audit 标记——故引入 TPW 时
不得导入第二 ledger。

### 3.2 最小操作序列

1. **固定版本**：记录源仓库 + commit/tree + 包路径（本次即 `0e2bc4ba` / `1f509b6f…`），或 vendor 复制；
   来源记录写进项目已有的 provenance/status 位置，没有就写一小段来源块，不新增 schema。
2. **发现目标与现有契约**：本次交付什么；项目已接受哪些行为/领域/接口/政策/任务状态；两者之间缺什么 judgment、什么输入。
3. **只选缺少的 judgment**：按 `profiles/README.md` 选择一个或两个 Profile；选择是组合，不是授权。
4. **只绑适用方法**：从 `methods/README.md` 按路径绑定本任务确实需要的方法；不需要就绑 none。
   退役四名（`path-trace`/`blast-radius`/`design-compare`/`drive-preview`）在 fixed 对象无等价正文：
   不得映射到旧名、不得造等价名；没有对应正文就保持未绑定。
5. **填真实委托的 Charter**：复制 `charters/template.md`，字段换成项目真实对象——
   Task/outcome、Delegation source（含决定人）、Object scope（读集/写集与显式边界）、
   Accepted inputs（版本 + 接受者）、Applicable methods（路径 + 固定 commit/digest）、Responsibility、
   Delegated decisions、Preserve/do-not-do、Tools/actions、Deliver、Independence、Recall、
   Acceptance / verification / action / closure（四者分开）。写“允许”不产生权限。
6. **装配启动文本**（确定性顺序）：Profile →（仅当责任边界相关）authority 上下文 → 填好的 Charter →
   绑定的方法文件 → 任务输入（当前事实 + 固定引用）。harness 能按路径读就给路径，不能读就拼接。
7. **交付落回项目自己的对象**：patch/Plan/证据进入项目已有的位置与证据纪律；不建第二状态源。
8. **固定与升级**：core 与任务输入分别固定，互不偷换；升级 = 选新固定对象 → 只 diff 包内两版 →
   重核受影响的约定/方法/Charter 字段/假设，以及有效性依赖被改约定的证据；mutable `main` 不能偷换本次依据。

最小 Charter 形状（说明性；**值必须由真实任务替换，示例不授予任何东西**）：

```text
Instance Charter · <项目任务名>
State:              candidate
Profile:            professional-workflow/profiles/implementation.md
Instance:           <unique session name>
Task / outcome:     <做什么、非目标>
Delegation source:  <项目自己的工单/窗口/指示 + 决定人；只记录既有授权，不新增>
Object scope:       read <...>; write <...>; boundary <...>
Accepted inputs:    <项目契约/spec/卡，版本或 commit，接受者>
Applicable methods: professional-workflow/methods/local-defect-feedback-loop.md @ 0e2bc4ba…（仅当需要）
Responsibility / Delegated decisions / Preserve / Tools and actions: <项目事实>
Deliver:            <项目对象 + 证据 + 偏差 + 未决>
Independence:       <作者/挑战者/评价者；同 session 换标签不构成独立>
Recall:             <停止条件> → Driver 路由到边界责任方；人类保留决定经 Voice
Acceptance / verification / action / closure: <项目各自的责任方，四者分开>
```

### 3.3 最小实例

- **局部缺陷修复（最少实例）**：1 个 E 实例 + 1 个独立 F 实例；不要求先做 Plan；局部改动可引用已有契约，
  加一段本次差分与委托范围即可。E 自测只作 F 的可核对输入。
- **跨模块新承诺**：D 出 Plan（至少含 Commitments / Delegated Decisions / Recall Conditions）→ E 在委托空间内
  按“完成时能独立演示/验证什么”切片实现 → F 先固定审查对象（commit/范围/fixed point）与意图来源再评。
  E/F 各自有自己的 Charter 与启动文本，不复用 D 那一份。
- 实例数与是否拆 F 由真实任务决定；Profile 名或同一 session 内的不同标签不建立独立性。

### 3.4 具体交付

- 项目真实对象：patch / Plan / 切片结果 + 证据（实际执行了什么、命令与观察、覆盖范围与限制、真实贡献）
  + **三态结论（PASS/FAIL/UNVERIFIED）**；在已治理仓库落到其自己的位置（卡状态、receipt、ledger 行、当前事实文档）。
- 比较方法 `behavior-claim-evaluation.md` 只在 claim 确实适用 baseline/treatment 时绑定，不是所有 claim 的通用入口；
  其他 claim 按接受依据与适当验证设计。行为结论由 F 给三态。
- 局部 PASS ≠ 发布/部署/合并许可；审查建议不构成接受。

### 3.5 召回 / 升级路径

- 契约缺失、矛盾或无法在委托范围内保持 → 记录受影响对象、事实与影响，**停止依赖该契约的工作**。
- 事实推翻已接受承诺 → 回 B/C；接口/约束/验证依据要变 → 回 D；超出委托或触碰保留决定 → Driver 路由到
  拥有该边界的责任方；只有人类保留决定才经 Voice。
- 实现者不能自行接受上游变更；下游采纳、任务接受、动作授权与关闭归其有效委托责任方。
- 召回对象写清“受影响对象 + 事实 + 影响”，不夹带对未委托对象的修改。

## 4. Profile 与权限的区别（案例1 的核心检查点）

| | Profile | 权限（授权） |
| --- | --- | --- |
| 是什么 | 可缓存的专业判断配置（A–F/Driver 判断函数组合），不是职位表 | 真实委托已授予的决定/动作许可 |
| 选择/写入的效果 | 选择 = 组合（composition），**不产生权限**；Profile 名不激活方法 | 在 Charter 写“允许”**不产生**权限；权限不因本包或 Profile 产生 |
| 方法激活 | 方法由 Charter 按路径绑定；Profile 名本身不激活任何方法 | 方法正文不构成权限或触发器 |
| 工具与动作 | —— | 工具可用 ≠ 有权限动作；有权限 ≠ 绕过工具限制 |
| 必要来源 | `profiles/README.md`「选择预设 ≠ 授予权限」 | Charter 的 Delegation source / 动作边界指向的项目既有授权 |

出处（fixed 对象）：`professional-workflow/README.md`（"A task Charter must cite the actual delegation and does not
gain authority from a Profile or this package"；包尾"If... no downstream authorization"）；
`profiles/README.md`（"选择预设 ≠ 授予权限"）；`charters/README.md`（Rules 两条："Choosing a Profile is composition,
not authorization"；"Tool access does not grant permission; permission does not bypass tool restrictions"）；
`ADOPTION.md` §2 第 4 条与 §3；`methods/README.md` 尾注。结论：案例1 中，**Profile 只解决“缺哪种判断”，
权限必须来自项目自己的委托对象**；两者在文本上被明确分开。

## 5. 缺什么就无法开工（具体）

对案例1，在能装配启动文本之前，必须由**项目侧**补齐的（缺任一即不能形成真实任务实例）：

1. **真实委托对象**：谁委托、决定人是谁、委托文本/工单/写窗口是什么 → 缺则 Charter 的 Delegation source 为空，
   Profile 选择不构成授权，只能停。
2. **对象范围**：可读集与可写集、显式保留项 → 缺则无法判断“预期会碰的文件”是否越界；预期文件集不等于权限边界，
   除非授权明确设为边界。
3. **已接受输入的版本**：要引用的契约/领域/spec/任务状态/政策的具体 commit/tree/snapshot 与接受者 →
   缺版本则依据不可固定，证据不可核对。
4. **独立性关系**：作者、挑战者、评价者分别是谁 → 缺则 F 的结论独立性不可建立（同 session 换标签不算独立）。
5. **接受 / 验证 / 动作 / 关闭的归属与证据位置**：四者各自的责任方 → 缺则无法关闭，且不得由其中一项推断另一项。
6. **方法绑定事实**：本任务需要的判断在 fixed 对象内是否有对应正文 → 若只有退役旧名相近，必须记录为未绑定，
   不得伪绑或造等价名。
7. **工具与动作边界**：哪些动作有外部效果、需要单独授权（写、联网、发布等）→ 缺则任何有后果动作都不具备许可。
8. **人类保留决定（若有）**：写下该决定与未决状态 → 缺则不应代替人类决定。

对**本次消费测试本身**的缺口（限定声明，不掩盖）：

- 任务输入未给出“被引入仓库”的实际路径/commit 与其在线治理对象，因此本报告只验证了包侧入口文本可被独立重建、
  映射表可用、边界自述一致；**不能**据此产出可执行的真实启动文本，§3.2 的 Charter 只是形状。
- 只读入口/选择/装配层，未打开任一 Profile 正文、方法正文与 `authority/RESPONSIBILITY-BACKBONE.md` 正文；
  对正文质量与责任基线内容不做判断。
- 包刻意不提供下游映射、第二台账、schema/validator/composer/installer、权限引擎（`ADOPTION.md` §5、§6）；
  这些不应被期待或要求，缺它们不构成开工阻断，但缺 §5 第 1–8 项构成。

## 6. 受限结论

在 fixed 对象 `0e2bc4ba` 上，案例1 的引入路径可由入口文本独立重建：选 Profile（不产生权限）→ 用项目自身对象
填 Charter → 按路径绑适用方法 → 依序拼启动文本 → 交付落回项目自己的对象与证据位置 → 召回经 Driver/Voice。
最小实例、三态证据与召回路径均有明确文本出处；未发现需要第二台账、常驻角色、新 schema 或权限引擎的步骤。
本报告的适用限度见 §1（未读正文）与 §5（未给真实目标仓与实时治理对象）。

---

Consumed fixed object：night 仓 `/Users/yuantian/Developer/tim-professional-workflow/.worktrees/night-2026-10-01`，
commit `0e2bc4ba72ab8825b84e0e455de9ae5a2df26fe9`，core subtree `1f509b6f0caebdb8f03046e84608ba98864e3a5e`；
产品读取均经 `git -C <night> show 0e2bc4ba72ab8825b84e0e455de9ae5a2df26fe9:<path>`（`professional-workflow/<path>` 或 `adoption-examples/<path>`）。
