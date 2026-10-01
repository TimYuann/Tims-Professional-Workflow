# ABSORB-DRAFT-DBG-16 · mock / adapter 选择 · 草案候选

**状态：草案候选（未采纳、不产生 authority / 生成器 / gate）。** rev.2：按 `ABSORB-METHOD-FOLLOWUP-REVIEW.md` FM-3 分离业务逻辑端口测试与生产 transport/serialization adapter 正确性，替换 §3 反例的验证面，并按 suggestion #1/#3 收窄 replace-don't-layer 的绝对表述、校正源行锚。

- 授权：Owner 2026-10-01 有界起草授权（只写 `docs/overnight/`，不碰 `professional-workflow/`）；口径见 `ABSORB-PRO-REVIEW-RESPONSE.txt` 第四节、`ABSORB-PRO-REVIEW-DISPOSITION.md`、`ABSORB-FULL-CORRECTION-BRIEF.md` §2。
- 写集：仅本文件。未改任何 active 方法 / Profile / Charter / Backbone；未新建注册表、脚本、校验器或 gate；未提交、未发布、未运行脚本或测试。
- 性质：静态源核验后的知识候选；不声明任何运行时（测试是否执行、接缝是否可用、adapter 是否正确）；不产生未来改对象、加检查或删规则的权限。
- 拟接点（仅记录，未施工）：`professional-workflow/methods/cross-module-design.md` §Method 3；候选集成口径见 `ABSORB-CANDIDATE-METHOD-INTEGRATION.md`。

## 0 · 固定源核验（只读）

| 源 | pin（HEAD == pin，已核） | 文件 | blob |
| --- | --- | --- | --- |
| mattpocock-skills | `c55ee46073ed923f86ce59a5eb3b6d895095d1b7` | `skills/engineering/tdd/mocking.md` | `71cbfee674d93244ce81d1830b930ca9a69200bd` |
| mattpocock-skills | 同上 | `skills/engineering/codebase-design/SKILL.md` | `3f63c8146dd2604b419c929e9876b90c30d410e9` |
| mattpocock-skills | 同上 | `skills/engineering/codebase-design/DEEPENING.md` | `cd94075cfd754d147555c5d747a16431ed4c7dd8` |

上游工作树 `git status --porcelain` 为空；无 checkout、无写入、无脚本执行。定位根：`.worktrees/legacy-pre-night-2026-10-01/upstreams/`。

## 1 · 候选正文（草案措辞；非 active、未采纳）

> 以下只是候选措辞的行文参考。若未来采纳，需先有独立编辑决定与新的接受记录；本草案不自行落入 active 方法。

1. 先分类依赖，再决定测试替身与接缝位置：**进程内**（纯计算/内存状态，不需要 adapter，直接透过接口测试）；**本地可替代**（有本地 stand-in，如 PGLite、内存文件系统；接缝在内部，不在模块外部接口开 port）；**远程但自有**（在接缝定义 port；生产用 HTTP/gRPC/queue adapter，测试用 in-memory adapter）；**真正外部**（第三方作为注入 port，测试用 mock adapter）。
2. 打桩只在系统边界：外部 API；数据库"有时"（优先真实测试库）；时间/随机性；文件系统"有时"。不 mock 进程内自己的类/模块与内部协作者（mocking.md 的适用范围）。**范围协调（自拟解释）**：owned-remote 的 port + test adapter 是在跨网络接缝替换 transport，不是在进程内替换真实协作者；两条规则作用于不同接缝，不构成"凡自有必可 mock"或"凡自有一律不 mock"的绝对政策。
3. **覆盖边界（自拟工程推断，源未言明）**：port/in-memory 测试覆盖深模块的逻辑，**不**执行生产 transport/serialization adapter。若风险在 adapter 的请求构造/响应解析，in-memory 替身全绿不能证明生产 adapter 正确；需要 adapter 级契约观察（本地 stub/录制 fixture，无活网络），或把归一化逻辑放到 port 之下、让深模块测试真正执行它。
4. 需要在边界打桩时，为可 mock 而设计：依赖注入（传入外部依赖而非内部构造）；优先 SDK 式按操作接口而非通用 fetcher——每个 mock 返回一个具体形状、测试设置无条件分支、能看出测试实际点到哪些端点。
5. 接缝纪律：一个 adapter 是假设接缝，两个 adapter（通常生产＋测试）才是真接缝；没有至少两个 adapter 不开 port；内部接缝（模块私有、供自身测试）与外部接缝并存，但不得因测试要用而把内部接缝暴露进接口；接口即测试面，若要"测试越过接口"，先怀疑模块形状。
6. 测试策略（源背景 + 窄条件）：上游主张新接口测试建立后旧浅模块单测"成为浪费"；本候选不把它变成"总是删旧单测"的政策——按当前方法 §Method 4，只有新测试确实覆盖对应 accepted claim、且删除已有动作授权时，才谈替换；否则保留旧覆盖并记录边界。

## 2 · 条文明细（每条：源 pin+路径+章节锚点 / 适用条件 / 例外 / 反例）

### DBG-16.1 四类依赖决定测试替身

- **源锚点**：matt `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`，`skills/engineering/codebase-design/DEEPENING.md` §`Dependency categories`（L5–25：1 In-process L9–11；2 Local-substitutable L13–15；3 Remote but owned L17–21；4 True external L23–25）。
- **规则**：先分类依赖，再选测试路径与 adapter；远程但自有用 port + 生产 adapter + 测试 in-memory adapter，真正外部用注入 port + mock adapter。
- **适用条件**：设计/评审跨依赖模块时，决定测试路径与是否引入 adapter/port。
- **例外**："Deepenable if the stand-in exists"——本地替代件不存在时该路不成立；数据库/文件系统属 "sometimes"，优先真实替身。
- **反例**：把自有远程服务在 HTTP 客户端层 mock 掉，并当作已验证；应 port + 生产 adapter + in-memory adapter，且注意 in-memory 路不覆盖生产 adapter（见 §1.3、§3）。

### DBG-16.2 打桩边界与源差异（不做绝对政策）

- **源锚点**：matt 同上 pin，`skills/engineering/tdd/mocking.md` §`# When to Mock`（L3–14：系统边界清单 L5–8；Don't mock 清单 L10–14）；范围协调另见 DEEPENING L17–21。
- **规则**：只在系统边界打桩；不 mock 进程内自己的类/模块、内部协作者、自己控制的一切。
- **适用条件**：决定测试里是否引入 mock。
- **例外**：数据库与文件系统 "sometimes"（优先测试库/临时目录）；owned-remote 的跨网络 port 走 DBG-16.1 的 test adapter 路——两条规则接缝不同，解释见 §1.2，不做"拥有即绝不 mock"或"拥有即可 mock"的泛化。
- **反例**：对进程内真实协作者下桩、用 fake 的"预期行为"取代真实语义（见 §3 第二变体）。

### DBG-16.3 可 mock 的接口设计

- **源锚点**：mocking.md §`Designing for Mockability`（L16–59：DI L20–35 含示例；SDK 式 L37–59，含 L55–59 的四条优点）；`skills/engineering/codebase-design/SKILL.md` §`Designing for testability`（L69–80，item 1 "Accept dependencies, don't create them"，L71）。
- **规则**：依赖注入；SDK 式按操作接口；每个 mock 返回一个具体形状、测试设置无 condition 逻辑、能看出测试点到的端点。
- **适用条件**：已确定边界需要 mock adapter 并要设计其接口时。
- **例外**：DI 是边界依赖的形状规则，不是"所有内部函数都加参数"的通用要求。
- **反例**：通用 fetcher 的 mock 内写 if/else 分支，测试看不出实际调用哪些端点、类型退化为宽泛类型。

### DBG-16.4 接缝纪律：不暴露内部接口

- **源锚点**：`codebase-design/SKILL.md` §`Principles`（L62 内部接缝 vs 外部接缝；L64 接口即测试面；L65 一 adapter 假设/两 adapter 真）；`DEEPENING.md` §`Seam discipline`（L27–31，L31 "Don't expose internal seams through the interface just because tests use them"）。
- **规则**：不因测试需要把内部接缝暴露进接口；没有至少两个 adapter 不开 port（单 adapter seam 只是 indirection）；测试跨接口断言可观察结果。
- **适用条件**：决定是否开新 seam/port，以及测试跨哪条缝。
- **例外**：这是设计纪律而非自动 gate；与现有 `cross-module-design.md` §Limits "Do not force modules to merge for depth" 的克制一致。
- **反例**：把 private 方法/字段提升进公共接口让测试拿内部状态；或给只有一个实现的依赖加 port，只剩间接层。

### DBG-16.5 replace-don't-layer 的窄条件

- **源锚点**：`DEEPENING.md` §`Testing strategy: replace, don't layer`（L32–37："Old unit tests on shallow modules become waste once tests at the deepened module's interface exist; delete them."）；当前 core `91875114e51855517f92ef099cbdf60c34e68243` `cross-module-design.md` §Method 4（"Replace or remove old coverage only when the replacement demonstrably covers its accepted claim; this method does not grant deletion authority."）。
- **规则**：源句作为背景保留；采纳面只取窄条件——替换或删除旧覆盖需同时满足"新测试覆盖对应 accepted claim"与"已有删除授权"。
- **适用条件**：深模块接口测试建立后，评估旧单测去留时。
- **例外**：不满足窄条件时，旧覆盖保留为已有行为证据，不用"有新测试"推定其无价值。
- **反例**：把"新接口测试已存在"直接推成"旧单测全部删除"——动作授权与覆盖对应性都未证明。

### DBG-16.6 源关系校正（不是"两处全文重复"）

- **源锚点**：mocking.md L20–22 与 `codebase-design/SKILL.md` L71 共享"把依赖传进来"这一条原则；三份材料覆盖面不同。
- **校正**：`tdd/mocking.md` 管边界打桩与为可 mock 设计接口；`codebase-design/SKILL.md` 管深模块/接口/接缝/深度词汇与原则（DI 只是其 §Designing for testability 的一条）；`DEEPENING.md` 管依赖分类决定测试策略。共享一条 DI 原则 ≠ 两份全文重复；未来采纳时源锚按实际保留内容分别给出，不得"指认单源"。
- **适用条件**：将来把本候选写入正文时的源引用纪律。
- **例外**：无。
- **反例**：`ABSORB-B-ADJUDICATION.md` DBG-16 行的"指认单源（上游两处重复）"——会丢掉接缝纪律与依赖分类；Pro 审核已要求恢复适用语境的协调。

## 3 · 反例：错误测试面掩盖真实缺陷（FM-3 修正，草案自拟）

场景：订单模块依赖自有的 pricing 服务（远程但自有），契约 fixture（本地录制，无活网络）为：

```text
GET /price?sku=X → 200 {"data":{"unit_price_cents":1200,"discount":null}}
```

生产 adapter 假定响应是扁平结构（`body.unit_price_cents`），实际字段嵌套在 `data` 下 → 取到 `undefined` → 折价/总价按 0 处理，生产把订单算成免费。

- **为什么端口级测试全绿**：测试用 in-memory adapter 替换 transport，直接返回正确的领域对象 `{ unitPriceCents: 1200, discount: null }`；生产 adapter 的解析代码从未被执行。in-memory 替身可以证明深模块逻辑，不能证明被替换掉的生产 adapter 正确——这正是 FM-3 指出的验证面错配。
- **正确测试面（任务本地选择，不设全局 integration gate）**：(a) 对生产 adapter 做 adapter 级契约观察——在本地 stub server/录制 fixture 上喂嵌套、`null`、缺字段等形状，断言请求构造与解析结果，无活网络；(b) 或把归一化放到 port 之下，让 in-memory 测试执行同一段映射逻辑，adapter 保持薄。两条路都需在任务记录里写明覆盖边界与未覆盖部分。
- **第二变体（正确归因）**：缺陷在自己的进程内协作者（订单×库存交互），测试却把该协作者 mock 成"按预期行为"——此时修复方式是直接使用真实协作者，不需要 port。它与在跨网络 port 上提供 test adapter 是不同操作。

## 4 · 适用边界与不主张

- 不主张运行时效果：未执行任何测试或服务；本候选是静态知识。
- 不新增 gate：不要求任何模块必须 mock、必须开 port 或必须注入依赖；与 `cross-module-design.md` 现有 §Use/§Limits 的"按任务需要"一致。
- 不为测试暴露内部接口；不把 DI 变成内部函数的统一签名要求；不把 replace-don't-layer 变成删测试政策。
- 源与自拟区分：§1.1/2 前段、§1.4/5 有源锚；§1.2 范围协调、§1.3 覆盖边界、§1.6 窄条件、§3 全例为自拟工程展开（authored），不冒充上游正文，也不因源表正确而自动正确。
- 不产生未来权限；采纳与否需独立编辑决定与接受记录。

## 5 · 源锚点汇总

| # | 源 pin | 路径 | 章节/行 | 提供 |
| --- | --- | --- | --- | --- |
| 1 | c55ee460… | skills/engineering/tdd/mocking.md | §When to Mock L3–14 | 系统边界清单、不 mock 进程内自有物 |
| 2 | c55ee460… | 同上 | §Designing for Mockability L16–59 | DI（L20–35）、SDK 式接口与优点（L37–59） |
| 3 | c55ee460… | skills/engineering/codebase-design/SKILL.md | §Principles L62–65 | 内部/外部接缝、接口即测试面、一/两 adapter |
| 4 | c55ee460… | 同上 | §Designing for testability L69–80 | Accept dependencies, don't create them |
| 5 | c55ee460… | skills/engineering/codebase-design/DEEPENING.md | §Dependency categories L5–25 | 四类依赖与测试替身 |
| 6 | c55ee460… | 同上 | §Seam discipline L27–31 | 不暴露内部接缝、单 adapter 不开 port |
| 7 | c55ee460… | 同上 | §Testing strategy: replace, don't layer L32–37 | 接口即测试面；删除句的源背景 |
| 8 | core 91875114… | professional-workflow/methods/cross-module-design.md | §Method 3 / §Method 4 / §Limits | 现有依赖形状列表、删除窄条件与接点 |

## 6 · 残余

- 未读 `tdd/SKILL.md`、`tests.md` 等其他 TDD/测试材料；它们的覆盖不由本草案声称。
- 未验证这些规则在目标运行环境的实际执行效果（无测试运行、无服务操作）；生产 adapter 契约观察在本轮未实施。
- 本文件存在不等于 PASS、采纳或任何授权。
