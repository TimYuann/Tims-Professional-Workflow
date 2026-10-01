# ABSORB-DRAFT-DBG-16 · mock / adapter 选择 · 草案候选

**状态：草案候选（未采纳、不产生 authority / 生成器 / gate）。**

- 授权：Owner 2026-10-01 有界起草授权（只写 `docs/overnight/`，不碰 `professional-workflow/`）；口径见 `ABSORB-PRO-REVIEW-RESPONSE.txt` 第四节与 `ABSORB-PRO-REVIEW-DISPOSITION.md`。
- 写集：仅本文件。未改任何 active 方法 / Profile / Charter / Backbone；未新建注册表、脚本、校验器或 gate；未提交、未发布、未运行脚本或测试。
- 性质：静态源核验后的知识候选；不构成对任何运行时行为（测试是否实际执行、接缝是否可用）的声明；不产生未来改对象、加检查或删规则的权限。
- 拟接点（仅记录，未施工）：`professional-workflow/methods/cross-module-design.md` §Method 3（现有四类依赖形状 "in-process, locally replaceable, remotely owned behind an adapter, or a true external dependency" 的扩写处）。

## 0 · 固定源核验（只读）

| 源 | pin（HEAD == pin，已核） | 文件 | blob |
| --- | --- | --- | --- |
| mattpocock-skills | `c55ee46073ed923f86ce59a5eb3b6d895095d1b7` | `skills/engineering/tdd/mocking.md` | `71cbfee674d93244ce81d1830b930ca9a69200bd` |
| mattpocock-skills | 同上 | `skills/engineering/codebase-design/SKILL.md` | `3f63c8146dd2604b419c929e9876b90c30d410e9` |
| mattpocock-skills | 同上 | `skills/engineering/codebase-design/DEEPENING.md` | `cd94075cfd754d147555c5d747a16431ed4c7dd8` |

上游工作树 `git status --porcelain` 为空；无 checkout、无写入、无脚本执行。定位根：`.worktrees/legacy-pre-night-2026-10-01/upstreams/`。

## 1 · 候选正文（草案措辞；非 active、未采纳）

> 以下只是候选措辞的行文参考。若未来采纳，需先有独立编辑决定与新的接受记录；本草案不自行落入 active 方法。

1. 先分类依赖，再决定测试替身与接缝位置：
   - **进程内**：纯计算/内存状态，不需要 adapter，直接透过接口测试。
   - **本地可替代**（存在本地 stand-in，如 PGLite、内存文件系统）：用 stand-in 在测试套件中运行；接缝在内部，不在模块外部接口开 port。
   - **远程但自有**（自有服务跨网络）：在接缝定义 **port**；生产用 HTTP/gRPC/queue adapter，测试用 in-memory adapter；逻辑留在同一深模块。
   - **真正外部**（第三方：Stripe、Twilio 等）：作为注入的 port，测试用 mock adapter。
2. 打桩只在系统边界：外部 API；数据库"有时"（优先真实测试库）；时间/随机性；文件系统"有时"。不 mock 自己的类/模块、内部协作者、任何自己控制的东西。
3. 需要在边界打桩时，为可 mock 而设计：依赖注入（传入外部依赖而非内部构造）；优先 SDK 式按操作接口而非通用 fetcher——每个 mock 返回一个具体形状、测试设置无条件分支、能看出测试实际点到哪些端点。
4. 接缝纪律：一个 adapter 是假设接缝，两个 adapter（通常生产＋测试）才是真接缝；没有至少两个 adapter 不开 port；内部接缝（模块私有、供自身测试）与外部接缝并存，但不得因测试要用而把内部接缝暴露进接口；接口即测试面，若要"测试越过接口"，先怀疑模块形状。
5. 测试策略是替换而非叠加：深模块接口测试建立后，旧的浅模块单元测试成为浪费；测试断言透过接口的可观察结果，能在内部重构后存活。

## 2 · 条文明细（每条：源 pin+路径+章节锚点 / 适用条件 / 例外 / 反例）

### DBG-16.1 四类依赖决定测试替身

- **源锚点**：matt `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`，`skills/engineering/codebase-design/DEEPENING.md` §`Dependency categories`（L5–25：1 In-process L9–11；2 Local-substitutable L13–15；3 Remote but owned L17–21；4 True external L23–25）。
- **规则**：先分类依赖（进程内 / 本地可替代 / 远程但自有 / 真正外部），再选测试路径与 adapter；远程但自有用 port + 生产 adapter + 测试 in-memory adapter，真正外部用注入 port + mock adapter。
- **适用条件**：设计/评审跨依赖模块时，决定测试路径与是否引入 adapter/port。
- **例外**："Deepenable if the stand-in exists"——本地替代件不存在时该路不成立；数据库/文件系统属 "sometimes"，优先真实替身（测试库、临时目录）。
- **反例**：把自有远程服务当第三方、在 HTTP 客户端层 mock 掉；应 port + 生产 adapter + in-memory adapter，让重试/契约逻辑留在测试面内。

### DBG-16.2 打桩边界与不 mock 自有物

- **源锚点**：matt 同上 pin，`skills/engineering/tdd/mocking.md` §`# When to Mock`（L3–14：系统边界清单 L5–8；Don't mock 清单 L10–14）。
- **规则**：只在系统边界打桩：外部 API；数据库"有时"——prefer test DB；时间/随机性；文件系统"有时"。不 mock 自己的类/模块、内部协作者、自己控制的一切。
- **适用条件**：决定测试里是否引入 mock。
- **例外**：数据库与文件系统的 "sometimes" 为真例外——优先测试库/临时目录等真实替身。
- **反例**：见 §3（错误打桩掩盖真实缺陷）。

### DBG-16.3 可 mock 的接口设计

- **源锚点**：mocking.md §`Designing for Mockability`（L16–53：DI L20–35 含示例；SDK 式 L37–53）；`skills/engineering/codebase-design/SKILL.md` §`Designing for testability`（L69–80，item 1 "Accept dependencies, don't create them"，L71）。
- **规则**：依赖注入；SDK 式按操作接口；每个 mock 返回一个具体形状、测试设置无 condition 逻辑、能看出测试点到的端点、类型安全按端点。
- **适用条件**：已确定边界需要 mock adapter 并要设计其接口时。
- **例外**：DI 是边界依赖的形状规则，不是"所有内部函数都加参数"的通用要求。
- **反例**：通用 fetcher 的 mock 内写 if/else 分支，测试看不出实际调用哪些端点、类型退化为宽泛类型。

### DBG-16.4 接缝纪律：不暴露内部接口

- **源锚点**：`codebase-design/SKILL.md` §`Principles`（L62 内部接缝 vs 外部接缝；L64 接口即测试面；L65 一 adapter 假设/两 adapter 真）；`DEEPENING.md` §`Seam discipline`（L27–31，L31 "Don't expose internal seams through the interface just because tests use them"）；§`Testing strategy: replace, don't layer`（L32–37）。
- **规则**：不因测试需要把内部接缝暴露进接口；没有至少两个 adapter 不开 port（单 adapter seam 只是 indirection）；测试跨接口断言可观察结果、内部重构后可存活；替换而非叠加旧浅模块测试。
- **适用条件**：决定是否开新 seam/port，以及测试跨哪条缝。
- **例外**：这是设计纪律而非自动 gate；与现有 `cross-module-design.md` §Limits "Do not force modules to merge for depth" 的克制一致，不强制任何模块结构。
- **反例**：把 private 方法/字段提升进公共接口让测试拿内部状态；或给只有一个实现的依赖加 port，只剩间接层。

### DBG-16.5 源关系校正（不是"两处全文重复"）

- **源锚点**：mocking.md L20–22 与 `codebase-design/SKILL.md` L71 共享"把依赖传进来"这一条原则；三份材料覆盖面不同。
- **校正**：
  - `tdd/mocking.md`：管边界打桩（哪里可以 mock、哪里不可以）与为可 mock 设计接口（DI、SDK 式）。
  - `codebase-design/SKILL.md`：管深模块/接口/接缝/深度词汇与原则（内部 vs 外部接缝、一/两 adapter、接口即测试面）；DI 只是其 §Designing for testability 的一条。
  - `codebase-design/DEEPENING.md`：管依赖分类决定测试策略（四类 + replace-don't-layer）。
  - 共享一条 DI 原则 ≠ 两份全文重复；未来采纳时源锚需按实际保留内容分别给出，不得"指认单源"。
- **适用条件**：将来把本候选写入正文时的源引用纪律。
- **例外**：无。
- **反例**：`ABSORB-B-ADJUDICATION.md` DBG-16 行的"前置：在采纳时指认单源（上游两处重复：mocking.md 与 codebase-design/SKILL.md）"——按单源指认会丢掉接缝纪律与依赖分类；Pro 审核已要求恢复适用语境的协调。

## 3 · 反例：错误打桩掩盖真实缺陷（1 个）

场景：订单模块依赖自有的 pricing 服务（远程但自有）与第三方支付网关（真正外部）。

错误做法：测试在 HTTP 客户端层 mock 掉 pricing 服务，返回写死的 happy-path JSON；支付重试用 mock adapter 也只返回成功。

- 真实缺陷在 adapter 的请求/契约假设里（如 pricing 对无折扣商品返回 200 + 空字段，代码把空字段当 0 处理）——mock 返回"代码想要的形状"，真实契约怪癖从未进入测试面。
- 或者缺陷在自己的内部协作者（订单×库存交互），却被 mock 成"按预期行为"——违反"不 mock 自己拥有的东西"，测试断言的是 mock 的假设而非真实语义。

两个变体都会全绿而生产失败。正确做法：自有 remote 服务走 port + 生产 HTTP adapter + 测试 in-memory adapter，让契约/重试逻辑落在同一深模块的测试面；内部协作者不 mock、直接测；只有第三方网关作为真正外部在边界 mock。

## 4 · 适用边界与不主张

- 不主张运行时效果：未执行任何测试或服务；本候选是静态知识。
- 不新增 gate：不要求任何模块必须 mock、必须开 port 或必须注入依赖；与 `cross-module-design.md` 现有 §Use/§Limits 的"按任务需要"保持一致。
- 不为测试暴露内部接口；不把 DI 变成内部函数的统一签名要求。
- 不产生未来权限；采纳与否需独立编辑决定与接受记录。

## 5 · 源锚点汇总

| # | 源 pin | 路径 | 章节/行 | 提供 |
| --- | --- | --- | --- | --- |
| 1 | c55ee460… | skills/engineering/tdd/mocking.md | §When to Mock L3–14 | 系统边界清单、不 mock 自有物 |
| 2 | c55ee460… | 同上 | §Designing for Mockability L16–53 | DI（L20–35）、SDK 式接口（L37–53） |
| 3 | c55ee460… | skills/engineering/codebase-design/SKILL.md | §Principles L62–65 | 内部/外部接缝、接口即测试面、一/两 adapter |
| 4 | c55ee460… | 同上 | §Designing for testability L69–80 | Accept dependencies, don't create them |
| 5 | c55ee460… | skills/engineering/codebase-design/DEEPENING.md | §Dependency categories L5–25 | 四类依赖与测试替身 |
| 6 | c55ee460… | 同上 | §Seam discipline L27–31 | 不暴露内部接缝、单 adapter 不开 port |
| 7 | c55ee460… | 同上 | §Testing strategy: replace, don't layer L32–37 | 替换而非叠加、接口即测试面 |
| 8 | core 91875114… | professional-workflow/methods/cross-module-design.md | §Method 3 / §Limits | 现有依赖形状列表与接点（不否定） |

## 6 · 残余

- 未读 `tdd/SKILL.md`、`tests.md` 等其他 TDD/测试材料；它们的覆盖不由本草案声称。
- 未验证这些规则在目标运行环境的实际执行效果（无测试运行、无服务操作）。
- 本文件存在不等于 PASS、采纳或任何授权。
