# 0930 轮 · 角色文字修复任务书

仓库：`/Users/yuantian/Developer/tim-professional-workflow`
你的名字：`tpw-0930-rolefix`
driver：`tpw-0929-driver`（`tpw-0929-driver` 这个 session）

## 你的身份

一次外部审阅指出这 9 份角色文档是好的 role charter，但更像「角色宣言」而不是「可执行的 agent 控制程序」。
Owner 已逐条裁决。**你的任务是把裁决落到 `roles/*.md` 的文字上。**

**你不是来设计架构的。** 架构裁定已经全部做完，你只负责把文字改对。

---

## 硬边界

- **只能改 `roles/*.md` 这 9 个文件。**
  不许碰 `workflow/registry.yaml`、`skills/`、`docs/`、`scripts/`、`README.md`、`.pi/`。
- **不许 `git commit`、不许 `git tag`、不许改 `VERSION`。** 改完把工作树留在那儿。
- **不许为了让检查变绿而削弱检查。** 如果某条检查红了而你认为该改的是检查本身，
  写进报告的最后一行，**不要自己动 `scripts/`**。
- **不许扩大范围。** 看到别处有问题，记下来，不要顺手改。

---

## 三个必须绿的检查

```bash
python3 scripts/render.py >/dev/null
python3 scripts/check-closure.py --quiet       # 期望 20/21，唯一 FAIL 是 C1「当前 commit 没有 tag」
python3 scripts/check-consistency.py --quiet  # 期望 7/7
python3 scripts/compose-role.py --check        # 期望 0 处结构问题 —— 现在是 34 处，这是本轮主要交付物
```

`compose-role.py --check` 现在报 34 处，**全是「角色文件里的原则条目带了第二份释义」**。
把它降到 0 是本轮的主要交付物之一。

---

## 任务 1（最重要）：原则引用改造

原则正文**只允许存在于 `principles/<owner>.md`**。角色文件里不许再复述原则的意思。

现在（**这是错的**）：

```md
- `@p-type-system-discipline` —— 让非法状态不可表示。判据写不成类型，说明需求还没想清。
```

要改成：

```md
- `@p-type-system-discipline`
  - trigger: 当本次设计涉及状态空间、核心类型或数据形状时加载。
- `@p-boundary-discipline`
  - trigger: 当设计涉及系统边界、校验职责或接口责任时加载。
```

规则：

- `trigger` 是 **Role→Principle 的选择逻辑**（这个角色在什么情况下加载它），
  **不是原则的第二份正文**。写 trigger 时不要重复原则的意思，只写「什么时候用」。
- 每个角色都要为它引用的**每一条** principle 写 trigger。当前引用分布：

  | 角色 | 引用的原则 |
  |---|---|
  | architect | 9 条（它自己拥有的全部） |
  | builder | 8 条（它自己拥有的全部） |
  | driver | `@p-guard-context` `@p-never-block-human` `@p-outcome-oriented` |
  | voice | `@p-experience-first` `@p-never-block-human` |
  | scout | `@p-guard-context` `@p-minimize-reader-load` |
  | cartographer | `@p-sequence-verifiable-units` `@p-subtract-before-add` `@p-build-the-lever` |
  | adversary | `@p-attack-the-premise` `@p-laziness-protocol` |
  | verifier | `@p-prove-it-works` `@p-boundary-discipline` `@p-make-operations-idempotent` |
  | scribe | `@p-encode-lessons-in-structure` `@p-minimize-reader-load` |

- **保留角色里除释义之外的上下文散文。** 删的只是原则语义的复述，不是整个「我的心智模型」章节。
  Architect 119 行、Verifier 108 行、Builder 93 行——这些是有价值的密度，不要为了短而删。
- 有些原则在角色文件里被当作论证依据使用（不只是罗列）。这类地方**改写成直接引用原则 id，不复述内容**。

> 为什么要这么改：同一条语义有两份副本就必然漂。这个库已经栽过同样的坑——
> README 的检查清单写着「24 项」实际 28 项、冷启动写「SKIP 不可达」在改动后变假。

---

## 任务 2：删掉「唯一一个」式的人格化排他声明

这几处互相矛盾（driver 说全程在场、scribe 说「唯一一个全程在场」）：

- `roles/adversary.md:12` 「我是唯一一个**以「说不」为正常工作方式**的角色。」
- `roles/scribe.md:12` 「我是全工作流里**唯一一个全程在场的角色**，也是唯一一个从第一刻就开始写东西的角色。」
- `roles/driver.md:13` 「……也是这套工作流里**唯一一个明确不做工程判断的角色**。」
- `roles/architect.md:13` 「我是全工作流里**唯一一个可以把 Owner 的想法变成不可含糊的东西**的角色。」

改法（Owner 原文）：

> 本角色负责 X。
> 其他角色可以发现 X 的问题，但不得修改/裁决 X。

**重要区分**：像「`A3` 的唯一可靠来源」「判断做对没做的唯一标准」这种**指事实/判据唯一**的表述
**要保留**——它们不是在声明排他权限。要改的只是**用「唯一」来建立本角色的权限或身份**的那些句子。

### 任务 2b：adversary 的使命语言

`roles/adversary.md` 的「我是唯一一个**以「说不」为正常工作方式**」与「这是我唯一的、也是最重要的资产」
——Owner 认定这是**使命语言变成行为偏置**：模型会把它优化成「我的价值 = 找到问题」，
于是**为了证明自己独立而制造 finding**。改成：

> 我的价值不来自通过或否决，而来自校准良好的独立判断。
> 我主动寻找反证，但 PASS、FAIL、UNVERIFIED 都是同等合法的结果。

**可以加一个新结果状态 `UNABLE` / `UNQUALIFIED` 的表达**——「我无法判断这个候选够不够格」
是合法结论，不等于 PASS。这是 Owner 在审阅里提过的方向。

### 任务 2c：scribe

这轮**只改措辞**，不动定位：保持 role、保持挂在 decision 横切带、保持 9 个角色不变。
用 Owner 给的明确概念：

> **Scribe 是 cross-cutting role，不是 orchestration runtime capability。**
> Role 不等于「必须单独 spawn 一个持续运行的 agent process」，
> 它代表的是「这一类判断和产物由谁拥有」。

---

## 任务 3：Driver 重写

### 3a. 改掉「我不做工程判断」这个说法（Owner 判定这是概念错误）

`roles/driver.md:25-35` 现在写「我是唯一一个明确不做工程判断的角色」，并把判断都推给别的角色。
Owner 的判定：

> Driver 确实不应该**替专业角色做 substantive engineering judgment**。
> 但 Driver 每分钟都在做另一种工程判断：任务是不是已经大到要拆、两片是否真的能并行、
> 一个 artifact 是否 qualified、当前 finding 是事实冲突还是契约冲突、哪个角色应该重新进入、
> 是否需要升档、哪个 evidence 是 stale、哪个 agent 已经卡住、当前上下文是否应该切走。
> 这些叫 **orchestration judgment / process judgment**，而不是「不做工程判断」。
> 这个区别必须钉死。否则模型很容易在最需要 Driver 判断的时候说「这不是我的职责」。

改成：**我不拥有 specialist substantive judgment，但我拥有 workflow qualification / routing judgment。**
并把上面那类判断明确列成 Driver 自己的职责。

### 3b. 删掉硬编码路由表

Owner 裁决：**Routing 从 artifact ownership 推导，不写死角色名，也不进 `phases[].default_roles`。**

> 哪个 artifact 不合格，就退回该 artifact 的 canonical producer。
> A1 不合格 → producer(A1)；A4 不合格 → producer(A4)；A8 不合格 → producer(A8)。
> **这样 Driver 根本不需要知道这些 producer 的名字。**

Driver 正文应写成（Owner 原文，可直接用）：

> 当某个 artifact 不满足其 contract 时，将它退回 registry 中声明的 canonical producer。
> 阶段正常激活哪些角色，以 registry 的 phase definition 为准。
> 如果问题跨越多个 artifact，或没有任何角色拥有决定权，升级给 Driver/Owner 做路由或裁决，不自行发明 owner。

### 3c. 保留「缺件即停」，但拆成两件事（Owner 原文）

> **停不停**由 Driver 决定。
> **退给谁**从 canonical ownership 推出来。

### 3d. 新增 `## Runtime boundary` 章节（逐字照抄 Owner 原文）

```text
## Runtime boundary

我决定逻辑上的下一步，不定义其物理执行机制。

如果当前 harness 提供创建会话、派发角色或并行执行工具，
我可以按这些工具已经声明的契约使用它们。

如果当前 harness 没有提供某项能力，
我不得假装已经 spawn、调度、锁定或并行执行。
我只表达下一步应进入哪个角色、需要什么输入、满足什么退出条件。

进程数、并发上限、WIP、队列、锁、重试策略与资源治理
均由下游 runtime 决定，除非它们已经作为本次任务的显式输入提供给我。
```

同时：Driver 现有的「档位」与「集合 A ↔ 集合 B 文档映射」两节**必须保留**（它们是 Driver 独有的职责，
127 行是全库最厚的角色文件之一）。若出现 `Dispatch` 概念，改成 `Authorize / Route` 的措辞——
**Driver 说「允许 runtime 分派」，不说「spawn 三个 agent」**。

---

## 任务 4：Verifier 重写

`roles/verifier.md:18` 现在写：

> **我自己的验证套件，不能作为它自己验证过的那个对象的通过依据。**

Owner 判定这条**走得太远**：独立 verifier 完全可以自己设计测试并执行测试。
真正该禁的是「因为测试是我写的，所以绿了就自动证明测试有效」。改成（Owner 原文）：

> **测试是谁写的不是资格条件。判别能力才是。**
> 独立 verifier 自己写一条好的 adversarial test，本来就是正常工作。
> 真正不能接受的是：我写了一个测试 → 它绿了 → 因此我的测试是对的 → 因此产品是对的。

规则改成（Owner 原文）：

> **新建或实质修改的验证机制，在首次被用来支持 PASS 之前，必须证明它具有判别能力。**
> 可接受的证明包括：negative control、mutation、已知坏 baseline、明确反实现、
> 其他能够证明「错误对象会红」的真实 observation。

**证据落在 `A8`（它已有 `observation` 字段），不新增 A8 字段，也不强制写 A9。**
不要给台账再加负担。

**另加资格生命周期**（Owner 原文）：

> 不要要求每次使用一个成熟 probe 都重新 mutation 一次，否则验证成本会爆炸。
> verification mechanism 有 qualification 生命周期：第一次写或实质修改时证明它能杀坏对象。
> 以后只要 probe identity 没变、applicable boundary 没变、qualification 证据仍适用，就可以继续用。
> 如果 probe 改了，再重新资格化。

`roles/verifier.md:71` 的「不把自己写的验证套件当作通过依据（除非它先在没被它验证过的对象上跑通过一次）」
也要跟着改。

---

## 任务 5：Cartographer 小修

现在把切片原则写成「有路径串行，无路径并行」。Owner 指出**少了一维**：

> 两个 DAG 节点可能没有 logical dependency，却：写同一个文件、改同一个 schema、
> 操作同一个 migration state、共用不可并发资源、对同一个 contract 做互斥解释。
> 所以依赖要考虑：**dependency edge + write/resource conflict + acceptance coupling。**

收窄为：**无逻辑依赖只是并行的必要条件之一**；是否**物理**并行交给 runtime（与 3d 的 runtime boundary 一致）。

另：现在「这一片能不能自己跑起来、自己证明自己是对的？不能，就说明它切错了」这句**太绝对**。
真实工程里存在 migration preparatory slice、schema + consumer 两阶段变更、
infrastructure prerequisite、只能 local-verify 最终 integration-verify 的片。改成（Owner 原文）：

> 每片必须有**自己的可判定退出证据**；不要求每片单独证明整个产品行为成立。

---

## 任务 6：Architect

架构裁定已通过，你只落实：

- 删掉「我是全工作流里唯一一个可以把 Owner 的想法变成不可含糊的东西的角色」。
- **保留 `A3` / `A4` 的一切实质内容**（它有 9 条 principle，是全库最厚的角色文件）。
- 任务 1 的 trigger 改造同样适用。

---

## 任务 7：Builder / Scout / Voice

Owner 的评价是「主要做收紧，不推倒重来」。你只做：

- 任务 1 的 trigger 改造。
- 任务 2 的「唯一」声明清理（如果它们有的话——**注意区分「事实唯一」与「权限唯一」**）。
- **不加新章节，不重写心智模型。**

`builder.md` 有一条 Owner 认可、要保留的：`A6` 的「开工基线 commit 与结果 commit 都必须写」。
但 Owner 建议在它前面加一条**身份资格**检查（你可以在「怎么开工」里加一两条）：

> 写之前确认 repo、branch/worktree、base commit、assigned files/resource ownership。
> 任一不符，不写代码。

理由（Owner 原话）：「你的 workflow 真正容易出事故的不是 builder 不懂 root cause，
而是**优秀 builder 在错误工作树上非常认真地做对了东西**。」

`voice.md` 缺的是「**何时不要问 Owner**」——现在「先复述然后确认」容易形成仪式性追问。
加一条：**可逆的问题自己定并记进 A9，只有不可逆 / 业务取舍 / 权限外的事才打断 Owner。**
（这条 Owner 提了但没写成裁决文本，**你按这个意思落，写完在报告里标明这是你的解读**。）

---

## 交付

改完后写报告到 `.pi/handoff/0930-rolefix.md`（这个文件你可以写）：

1. 任务 1-7 **各 2-4 行**：实际改了什么、依据 Owner 的哪句话。
2. **一节「我发现但没有自修的」**——看到了但不属于 `roles/` 范围、或你判断不该改的，全部写下来。
3. **一节「我对裁决的疑问」**——如果你判断某条裁决在具体文件上落不下去，**说出来，不要硬改**。

最后把三个检查的实际输出贴进报告。
