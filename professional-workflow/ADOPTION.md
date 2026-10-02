# 跨仓接入 · ADOPTION（通用）

本文件是 `professional-workflow/` 包的接入说明：让一个没有 TPW 历史的新仓库，从固定版本选择经验并装配出可用的任务实例。它不是方法正文、不是责任定义、不授予任何权限；取包方式、目录与项目治理形态由下游自己决定。

包内选择入口：`README.md`（装配顺序）、`profiles/README.md`（选 Profile）、`charters/README.md` + `charters/template.md`（填 Charter）、`methods/README.md`（选方法）、`authority/README.md`（冻结责任边界的来源身份）。

## 1. 取包：固定 Git 版本直读，或复制 / vendor

两种都合法，按项目条件选一种；先固定一个版本：**源仓库 + commit 或 tree（`professional-workflow/` 子树）+ 包内相对路径**。

### A. 直接读取固定 Git 版本

- 每次从固定对象读：`git show <commit>:professional-workflow/<path>`，或 `git show <tree>:<path>`（子树相对）。工程内已有 checkout 时，用同一 commit 读同一路径。
- 包内引用（`profiles/…`、`methods/…`、`authority/…`）以 `professional-workflow/` 为根解析。
- 引用与归属：Charter 的 Accepted inputs 写固定对象与所引方法路径；不写“最新 main”。
- 更新：项目决定升级时选新的固定 commit/tree，记录新对象；只对照旧对象 diff 包内受影响文件（见 §4）。

### B. 复制 / vendor 到下游

- 目录由项目决定：整包或子集、放哪里都行；保持包内相对路径可解析（相对复制根），改了布局就同步改 Charter 里的方法路径。
- 来源记录：源仓库、commit/tree、复制的路径；项目已有 provenance/status 位置就写在那里，没有就写一小段来源块（不新增 schema）。需要字节身份时记 SHA-256。
- 归属：保留复制字节里的来源锚点，以及 `authority/README.md`、`methods/README.md` 的来源/状态记录；不要剥掉上游署名。许可与所有权以仓库的实际记录为准，不从本文件推断。
- 更新：从新的固定 commit 重新复制或对照 diff；本地改动单独记录（patch/commit），不让 vendored 副本与来源身份静默漂移。

## 2. 最短接入路径

1. **发现目标与现有契约。** 本次要交付什么；项目已接受哪些行为/领域/接口/政策/任务状态；两者之间缺什么 judgment、什么输入。
2. **按缺少的 judgment 选 Profile。** 用 `profiles/README.md` 的选择入口；一两个够用。Profile 是判断配置，不是职位，选择不产生授权。
3. **只加载适用方法。** 从 `methods/README.md` 或包内实际文件，绑定本任务确实需要的路径；不需要就绑 none。方法不构成固定阶段链。
4. **填真实委托的 Instance Charter。** 复制 `charters/template.md`，把字段换成真实对象：委托来源与决定人、对象范围、Accepted inputs 及版本/接受状态、绑定方法路径与固定版本、工具/动作边界、交付物、独立性、Recall、验收/关闭责任。写“允许”不产生权限。
5. **形成启动文本。** 按阅读顺序拼成纯文本：Profile →（需要时）authority 上下文 → 填好的 Charter → 绑定的方法文件 → 任务输入（当前事实 + 固定引用）。harness 能按路径读文件就给路径，不能就读入拼接。

```sh
cat profiles/implementation.md \
    charters/<filled-task-charter>.md \
    methods/local-defect-feedback-loop.md \
    path/to/task-input.md
```

## 3. 已有治理 / 没有既有治理

**已有治理：映射，不重建。** 用项目自己的对象填 Charter，不把项目搬进本包词表。

| 项目已有 | 接到哪 |
| --- | --- |
| 职责 / 角色 / 槽位 | 其实际持有的 judgment 与 A–F/Driver 的对应；只映射，不改名、不按 Profile 重设岗位 |
| 授权来源（谁委托、谁接受、谁批动作） | Charter 的 Delegation source / Acceptance / 动作边界；接受、验证、动作、关闭各自分开 |
| 已接受事实（契约、spec、任务状态、政策） | Accepted inputs（带版本与决定人）；本包不复制成第二份台账 |
| 交付物与证据位置 | Deliver 指向项目自己的对象/位置；方法只加证据纪律，不建第二状态源 |

项目文档若已写明“外部包只提供方法正文、方法不产生权限”，照它执行；本包与 UCBIP 例子的观察不改变下游所有权。

**没有既有治理：只补这次任务够用的最小内容。** 缺什么具体补什么，不为采用 TPW 建 registry、schema、常驻角色或 gate：

- 目标：做什么、非目标；
- 授权：谁委托、可改哪些对象、工具/动作边界与保留项；
- 保持面：不得改的行为/接口/政策；确实没有就写“无既定冻结面，本次结果本身是待接受对象”；
- 关闭依据：谁验收、什么算完成、证据放哪、剩余风险谁接受；
- 需要人类保留决定时，写下该决定及未决状态，不代替人类决定。

上述最小内容通常就是一段任务简述 + 一份填好的 Charter；到此为止，不升级成项目流程。

## 4. 版本固定与升级

- **固定 core：** 记录源仓库 + commit/tree + 包路径；Charter 与任务输入引用同一对象；vendor 时另记复制路径与来源。
- **固定任务输入：** 任务输入文件带当前事实与固定引用，与包版本分开记录；分支 tip / “最新”不是固定版本。
- **升级：** 选新的固定对象 → 只 diff 包内两版 → 找出受影响的约定、方法、Charter 字段与假设 → 只重核这些，只重跑其有效性依赖被改约定的证据。旧证据不因换版自动成立，也不需要全量重评。
- mutable `main` 不能偷换本次依据：任务内引用的 commit/tree 不变；要用新版本，先升级、再重核、再改 Charter。

## 5. 始终加载的短指针 vs 按需正文

- **常驻的只有一条短指针：** 指向固定版本（源仓库 + commit/tree）的接入/选择入口，写在项目自己的任务启动处或已有文档里；不要求统一文件名，也不要求项目一定有 AGENTS 文件。
- **按需读：** 接入、选择或装配时才读相应入口（包 `README.md`、本文件、`profiles/README.md`、`methods/README.md`）；Profile 正文、方法正文、`authority/RESPONSIBILITY-BACKBONE.md`（责任边界相关时）、on-demand guides 只读当前 Charter 实际需要的内容。Charter 里一行方法路径只是引用，不是方法正文。
- Profile 名不激活方法；方法由 Charter 按路径绑定。不把本文件或全部入口设为每任务常驻上下文，也不把全部方法内联进 Profile。

## 6. 跨 harness 与辅助脚本

- 全部是纯文本（Markdown + 路径引用），无 runtime、无 registry、无平台依赖；能读文件或拉取固定 commit 的 harness 都能消费。
- 常规路径用现有 Git/文件工具就够（`git show`、`cat`、编辑器粘贴、路径引用）；**够用就不造 composer、生成器或安装器**。
- 只有出现真实、重复的机械摩擦（例如某 harness 无法按路径拼接，或 vendored 多文件字节核对成本实际出现）才考虑提取一个小的项目侧辅助脚本；脚本是项目自己的便利，不是包的一部分，也不得演化为 schema/权限引擎。

## 7. 例子、旧名与边界

- `../adoption-examples/ucbip.md`：一个已有治理项目的适配例（非规范、时点观察）；core 不依赖它。`../adoption-examples/cross-module-start.md`：小修复与跨模块新承诺两个短启动例。只 vendor `professional-workflow/` 时这两个例子可能不在副本中，不影响 core。
- 四个退役旧名（`path-trace`、`blast-radius`、`design-compare`、`drive-preview`）在本包没有等价方法正文（见 `methods/README.md`）：不得把任务映射到这些名字，也不得用它们替代真实方法。需要相近能力时，按固定版本内实际存在的方法文件的 claim 显式绑定；不存在就保持未绑定。
- 例子中的权责、对象、范围与证据只是可替换示例，不替任何项目授权，也不证明真实项目效率或生产资格。
- 真实任务的写入/联网/发布等动作，由该任务的 claim 与有效项目授权决定；不要从本包或任何只读检查的约束推断成产品政策。

本文件不授予决定权、改动物件许可、风险接受或任何有后果动作的许可。
