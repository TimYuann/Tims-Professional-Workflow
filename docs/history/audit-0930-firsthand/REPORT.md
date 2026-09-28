# 亲自核对：9 份角色文档的产出物 / 落点 / 标准 / 消费者 / 上游产出方

核对人：外部会话（非本库任何 agent、非 driver、非 rolefix）
核对对象：`HEAD = e2571f9`（含 0930 rolefix 改动）的 `roles/*.md`（9 份，874 行）
+ 它们引用的 45 个 `skills/*.md`
+ 系统侧：`workflow/registry.yaml`（artifacts / phases / ribbons）、`docs/artifacts.md`
方法：9 份角色文件由核对人**逐行通读**；技能正文由 9 个只读子代理分头**逐行通读**（禁 grep 下结论），
子代理只被允许读 `roles/` 与 `skills/`（不许读 README/docs/.pi，避免继承既有结论）。
子代理原始报告：`~/.pi/agent/sessions/--Users-yuantian-Developer-tim-professional-workflow--/subagent-artifacts/*_reviewer_output.md`

---

## 一、角色文件自己声明了哪些产出物（9/9 都有，且写得很实）

| 角色 | 主产物 | 字段与合格线 |
|---|---|---|
| voice | A1 诉求陈述 | 4 字段：ask / done_meaning / non_goals / unknowns（unknowns 那行只给了字段释义，没给合格线） |
| scout | A2 事实集 | 3 字段：claims / evidence / gaps，逐条有合格线 |
| architect | A3 能力地图、A4 冻结契约 | A3 三字段、A4 五字段，逐条有合格线 |
| cartographer | A5 任务图 | 3 字段：slices / edges / acceptance，逐条有合格线 |
| builder | A6 实现候选 | 4 栏：subject / change / runnable / known_gaps，逐条有合格线 |
| adversary | A7 裁决 | 3 字段：stance / reason / conditions，逐条有合格线 |
| verifier | A8 验证凭据 | 7 栏：claim / subject / scope / observation / frame_alignment / environment / verdict |
| scribe | A9 决策台账 | 8 字段：actor / run / subject / phase / decision / why / evidence / result |
| driver | **无**（"唯一持久的产出是 A9 里的映射决定"） | 无 |

另有若干**次级产出**散落在正文里，没有字段清单：voice 的 `@to-questionnaire` 外抛、
architect 的 A9 条目与契约变更、builder 的偏差报告、verifier 的"回滚路径 + 上线后可观测项"、
driver 的判档/映射/卡口决定。

**技能层额外声明要产出的东西**（45 个技能里）比角色文件多得多：决策树、词汇表、六行复述、
变体清单、隐藏假设清单、问卷、票据、迁移通告、合成记录、七块对抗报告、信号对照表……
其中**只有 `skills/to-questionnaire.md:45` 一处给了落点**（"落在你当前的工作目录里，文件名用主题命名"）。

---

## 二、四个问题的答案（逐条）

### 1. 落点：**体系有答案，但答案不在角色文件里**

- 角色文件层面：**9 份文件里，说清产出物落在哪里的，只有两处半**
  - `roles/architect.md:71` A4 的 `scope: project` 形态"仓库根目录那份质量契约"
  - `roles/scribe.md:56`"用 `scripts/ledger.sh` 追加"（但**连台账文件本身落在哪都没说**）
  - `roles/voice.md:52`"我负责落盘 `A1`"（只说"落盘"）
- 系统层面：`registry.yaml` 的 artifacts 段开头就写死了这件事的归属——
  > 「产物不是文件，是"字段 + 谁产出 + 谁消费"。**落到哪个路径由 driver 按集合 B 映射。**」
- 并且 `docs/artifacts.md` 末尾有**三条不可协商的落盘纪律**：
  durable 产物必须有可追溯落点、不许出现活不过跨会话的产物、台账只追加。
  registry 也给每个产物标了 `shape`（可合并的包 / 目录 / 单文件）与 `embodiment`（形态）。

⇒ **判定：落点是"有意不写死"，由 driver 每次裁定。设计自洽。**
代价是：**任何只读自己角色文件的会话，拿不到落点**。落点只活在三个地方——
driver 的映射裁定、A9 的装配行、以及交接时随包传递的东西。这三处任一丢失，下游就无从下笔。

### 2. 标准：**写得最实的一环**

字段级合格线在三个地方同时给出且基本一致：角色文件的「合格线」表、registry 的 `notes`、
phases 的 `exit_criteria`（verify 断言）。这块没有系统性缺口，只有零星几处：

- `roles/voice.md:45` `unknowns` 那行的"合格线"格写的是字段释义，不是判据
- `roles/verifier.md:70` 的"回滚路径 / 上线后可观测项"无任何合格线（且 `:104` 同一件事又变成自查问句）
- `roles/scribe.md` 给 A9 行写了逐字段合格线，但**没给全部 8 栏**（phase/why 只说语义）

### 3. 下游消费者：**registry 齐全，角色文件几乎全缺**

- `registry.yaml` 每个 artifact 都带 `consumers: [P1..P6]`，phases 的 `required_inputs` 与之对得上。
- 但 **9 份角色文件里没有任何一处点名消费者角色 id**。出现的全是代词："下游""别人""后来者"
  "拿到这一片的人""作者""人"。skills 层也一样（`trace-paths.md:50` 是唯一给了消费者画像的地方，
  但画的是"一个刚接手这个子系统的高级工程师"，不是角色 id）。

### 4. 上游产出方：**系统侧能对上，角色文件不写**

把 9 角色的「我收到什么」对到 phases 的 `produces` / `required_inputs`，映射是完整的：
A1←voice、A2←scout、A3/A4←architect、A5←cartographer、A6←builder、A7←adversary、
A8←verifier、A9←scribe。**每个输入都有 canonical producer，这一点成立。**
但角色文件自己一处都没写产出方，`roles/scout.md:34` 的"如果有人已经查过背景"就是典型：
"有人"是谁，没落到任何角色。

**两处输入在角色文件与技能之间对不上**（不是缺 producer，是输入清单漏项）：
- `skills/triage.md:17-18` 把 A2 定为硬前置，`roles/cartographer.md:31-33` 的输入清单里没有 A2
- `skills/git-workflow-and-versioning.md:15` 要求 A5，`roles/verifier.md:46-51` 的输入清单里没有 A5

---

## 三、真正的缺口（不是"落点缺失"，是下面这几条）

1. **driver 的产出没有归属。** `roles/driver.md:5` 说它"唯一持久的产出是 A9 里的映射决定"，
   而 registry 里 **A9 的 producer 写的是 scribe**，driver 也不在任何 phase 的 `default_roles` 里
   （只有 `driver_seat: pre`）。⇒ 装配结果（集合 A↔B 映射表）**没有 canonical producer，也没有检查器**。
   映射表本身是什么形态、落在哪、谁签字，全库没有定义。冷启动时它是第一件要产出的东西。

2. **A9 的字段规格两处不一致。** `roles/scribe.md:40` 写"八个字段"（含 actor/run/subject/phase），
   `skills/decision-ledger.md:24` 写"每次只写四件事"（decision/why/evidence/result），
   `:36-41` 的产出清单也只有四个。同一产物两份互不相容的规格，没说差异从哪来。

3. **同一产物的字段数在三处不同（同一角色内）。**
   - scout 的 A2：角色说 3 字段；`skills/research.md:40` 说"四个字段"（正文只列 3 条 + 1 条载体）；
     `skills/recall-context.md:51-60` 又是 5 项。**同名三种形状。**
   - builder 的 A6：角色说"四栏"；`skills/implement.md:30` 说"三个字段"（它自己的产出栏又列了四栏）。
   - `gaps` 同名不同义：scout 的 `gaps`="查过但没查到的"；`recall-context.md:57` 的 `gaps`="反复出现的问题，最多 5 条"。

4. **A9 的写入权在角色文件与技能之间相反。**
   `roles/architect.md:89/112/118` 要求 architect 写 A9；`skills/documentation-and-adrs.md:68` 说
   "它也**不直接写台账**——`A9` 的唯一产出方是 scribe"。两条同时在仓库里。

5. **一条硬边界没有执行主体。** `skills/arena.md:24-25` 的"选基底 + 嫁接"由读它的人执行；
   若由 `builder` 本人跑，就与 `roles/builder.md:57`「不对自己产出的候选给出裁决……任何档位都不放宽」冲突。
   文件只对"交叉评判"做了隔离（`:23` 起一个只读评判者），对选基者没有。

6. **"退回"这个动作没有载体。** 9 份角色文件里"退回"出现 20 余次，没有一处说退回记在哪里、
   用什么形态、谁需要看到它。退回是这套工作流里最高频的失败信号，它没有落点。

---

## 四、净结论

| 问题 | 答案 |
|---|---|
| 产出物清单找得出来吗 | 找得出。9 个角色 + 45 个技能，逐条可引 |
| 写没写"按什么标准写" | **写了**，且写得最实（三处互证） |
| 写没写"放在哪儿" | **有意不写死**，交给 driver 每次裁定；体系只给形态与三条落盘纪律 |
| 有没有下游消费者 | registry 有、角色文件没有 |
| 上游有没有人负责产出 | registry/phases 有、角色文件没有 |

⇒ **这套文档的产出物是"可执行的控制程序"，但它执行时需要一份外部输入：driver 的映射表。**
角色文件与 registry 合起来是完整的，**单看角色文件是不完整的**（落点、消费者、上游产出方三样都在外面）。
所以冷启动时"先做映射"不是流程里的一个可选项，而是让其余角色能够开工的前提。
而这件事恰恰是**唯一没有 canonical producer、也没有检查器覆盖**的一环。
