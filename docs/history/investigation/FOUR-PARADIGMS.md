# FOUR-PARADIGMS · BDD / TDD / DDD / SDD：三仓形态、权威解释、本库影子、归属证据

**角色**：调查者 B（只读取证，不改任何产物；本文件是唯一写入物）。
**对象**：`upstreams/{cursor-plugins（含 pstack）, mattpocock-skills, addyosmani-agent-skills}`（pin 见下）+ 本仓 `roles/*.md`（10 份）、`pipeline.md`、`closure.md`、`identity.md`、`SOURCES.md`、`docs/**`。

| 取证对象 | 锁定值 | 工作区 |
|---|---|---|
| `upstreams/cursor-plugins`（pstack 0.15.5） | `ecc249f1e306fc64ddf83c7bed16cacf7c2239db` | 干净 |
| `upstreams/mattpocock-skills` | `c55ee46073ed923f86ce59a5eb3b6d895095d1b7` | 干净 |
| `upstreams/addyosmani-agent-skills` | `2686b620fc1fed2e8f60c704839c766b8594c6b6` | 干净 |
| 本仓 | 只读 | — |

**方法**：先按字符串穷举（列出**匹配总数**，使"没有"可被复核），再读命中文件正文；每条结论给 `file:line` + 原文摘录。外部来源标明 URL 与抓取日期（2026-09-27）。**三仓没有的写"三仓无此法"，不替它们补。**
**未覆盖**：三仓 `third_party/**`、`node_modules`、git 历史；本仓 `index.html`、`scripts/**` 的语义（只按 SOURCES.md 登记读）。
**记号**：`[事实]` = 有原文可直接核对；`[推断]` = 由原文推出，附推导链；`[外部]` = 非三仓来源。

---

## 0. 先给"四套最后是怎么说的"——本轮的取证结论

**Owner 的问题是"四套东西最后是怎么说的"，而本文件只能给证据。以下三条是取证能直接支撑的事实，不是方案。**

### 0.1 [事实] 三仓对四套的覆盖度**极不对称**，其中一套完全不存在

| 范式 | 三仓里的匹配总数（可复现的命令见 §8） | 实质存在形态 |
|---|---|---|
| **BDD** | `BDD` 7 处 / `behaviour-driven` **0** / `behavior-driven` **0** / `given-when-then` **0** / `gherkin` **0** / `cucumber` **0** | **三仓无此法**。7 处 `BDD` 全部是 matt `CHANGELOG.md` 里同一个 commit SHA `…cbdd1c91818e` 的**子串**（`:54` `:82` `:88` `:98`），不是术语 |
| **TDD** | `TDD` 92 / `test-driven` 89，落在 40 个文件 | 三仓各有独立技能：`pstack/skills/tdd`、`addy/skills/test-driven-development`、`matt/skills/engineering/tdd` + `docs/engineering/tdd.md` |
| **DDD** | `DDD` 5 处 / `domain-driven` 1 处 / `ubiquitous` 10 处 | **没有名为 DDD 的技能**。5 处 `DDD` 里 1 处是 CHANGELOG 的 SHA 子串，其余 3 处是注释式提及（`domain-modeling.md:58`、`:70`、`codebase-design/SKILL.md:109`）；实体是 matt 的 `domain-modeling`（自称 ubiquitous language）与 pstack 的 `principle-model-the-domain` |
| **SDD** | `spec-driven` 66，落在 23 个文件 | 最完整：addy `skills/spec-driven-development` + `commands/spec.toml` + `commands/build.toml` + `hooks/SDD-CACHE.md`；matt `to-spec`；pstack `skills/architect` + `docs/guide/04-design.md` |

**推论（事实层）**：本库把"四套"当同一层级的四个对象讨论，但**上游根本没有把 BDD/DDD 当成两个可独立引用的技能**——它们是**外部方法名**（Dan North / Eric Evans / Fowler），三仓只以**局部机制**的形式出现（BDD→"测行为不测实现"这一条判据；DDD→"术语冲突摊开 + 词汇表"这一条纪律）。**SDD/TDD 才有三仓内的成品技能。**

### 0.2 [事实] 四套各自回答的是**不同问题**，不是同一问题的四种答法

| 范式 | 它回答的那个问题（由原文抽出的问句） | 原始出处 |
|---|---|---|
| **BDD** | **"谁和谁在一起谈、谈出什么？"** | Dan North：`You need analysts working with testers to capture the stories and identify the acceptance criteria, and then you need programmers working with testers to automate the scenarios.`（[外部] `https://dannorth.net/blog/theres-more-to-bdd-than-evolving-tdd/`） |
| **TDD** | **"什么时候写检查、一次写多少？"** | Fowler 三步（[外部] `https://martinfowler.com/bliki/TestDrivenDevelopment.html`）；三仓版本：`pstack/skills/tdd/SKILL.md:17`「**Write the failing test first.**」 |
| **DDD** | **"用什么词、词在哪里被固定？"** | Evans 经 matt 引用：`upstreams/mattpocock-skills/README.md:107`「With a ubiquitous language, conversations among developers and expressions of the code are all derived from the same domain model.」 |
| **SDD** | **"先冻结什么、冻到哪一级再动手？"** | spec-kit（[外部] `https://github.com/github/spec-kit`）：「Define **what and why** before deciding **how** to build it.」＋「**Constitution once per project; specify → plan → tasks → implement → converge per feature.**」 |

**这是 Oracle 那句"四套非严格集合关系"能落到实处的形式**：四个问题**不同轴**，所以任何"谁是子集"的图都会漏掉东西。这不是我下的定义，是四份原文的题面本身不同。

### 0.3 [事实] DDD / SDD **都不止输入层**——各有一条原文直接反证

- DDD 不止输入层：pstack `principle-model-the-domain/SKILL.md:3`（description）「**Apply when writing stateful logic** … Encode the domain in a structure instead of scattered conditionals.」；`:11`「**Choosing it at write time is cheap.** Recovering it later reads as a refactor and gets deferred.」→ 该机制的作用时刻是**写实现的当下**。
- SDD 不止输入层：spec-kit（[外部]）「Repeat **implement → converge** until convergence reports **Converged**.」→ SDD 的流程里本来就含**实现与收敛**两段，不只是"先写规格"。
- 反向证据（DDD 也不是全在写代码时）：matt `docs/engineering/domain-modeling.md:70`「**DDD gets less useful the closer it gets to the implementation**: the payoff is upstream, in naming and concept alignment, not in aggregates and layer ceremony.」
- 反向证据（BDD 也不只是验收层）：Cucumber（[外部] `https://cucumber.io/docs/bdd/`）三实践 `Discovery / Formulation / Automation`，其中 `Discovery` 是「structured conversations, called **discovery workshops**」——**一次会，不是一次实现**。

### 0.4 [事实，与 Owner 已知线索的冲突] "BDD ⊃ TDD"在原文里**不是集合关系，是一次改名**

Dan North 原文（[外部] `https://dannorth.net/blog/introducing-bdd/`，页首日期 `20 Sep 2006`）：
> 「I found the shift from thinking in tests to thinking in behaviour so profound that **I started to refer to TDD as BDD**, or behaviour- driven development.」

同页又有：
> 「**“Behaviour” is a more useful word than “test”** … My first “Aha!” moment occurred as I was being shown a deceptively simple utility called agiledox … The word “test” is stripped from both the class name and the method names」

→ **BDD 的起点是把 TDD 的用词换掉**，不是"在 TDD 外面套一层"；后来才长出 `Requirements are behaviour, too` 与 `Acceptance criteria should be executable` 两段（同页小节标题）。**"BDD ⊃ TDD"这个图是把两个不同年代的 BDD 叠在一起画的**（2003 的改名 + 2004-2006 的验收扩展）。Oracle 的纠正有原文支持。

---

## 1. BDD · Behavioral Driven Development

### 1.1 它在三仓里的确切存在形态 → **三仓无此法**

- `grep -rniF "behaviour-driven"` / `"behavior-driven"` / `"given-when-then"` / `"gherkin"` / `"cucumber"` 在三仓 **全部为 0 命中**（含 `*.md`/`*.toml`/`*.json`/`*.js`/`*.ts`）。
- `BDD` 7 处命中全部是 SHA 子串：`mattpocock-skills/CHANGELOG.md:54/82/88/98` 中 `…77d207ef03219cc603e2832e1159cbdd1c91818e`、`:115` 中 `…44eed545186ffd0263e8004867750b80cfddd215`。
- **BDD 这个名字在三仓一次也没有作为方法名出现过。**

**最接近的两处零件（都不是 BDD，只是同一判据的不同来源）：**
- `cursor-plugins/pstack/skills/principle-test-behavior-not-implementation/SKILL.md:3`（description）：「**Apply when you write, change, or keep a test.** Call the code the way its users do and assert the result they observe against a literal expected value. If the test would still pass when every imported function returns undefined, rewrite the assertion or delete the test.」
- `cursor-plugins/pstack/README.md:222`（同一技能的目录行，分类列写 `verification`）。

### 1.2 它的"权威解释"（原话，非三仓）

**A. Dan North《Introducing BDD》**（[外部] `https://dannorth.net/blog/introducing-bdd/`，页首 `20 Sep 2006`）
- 起源：「My response is behaviour-driven development (BDD). It has evolved out of established agile practices and is designed to make them more accessible and effective for teams new to agile software delivery. **Over time, BDD has grown to encompass the wider picture of agile analysis and automated acceptance testing.**」
- 命名模板：「**The class _should_ do something**」
- 核心词替换：「**“Behaviour” is a more useful word than “test”**」
- 对 _should_ 的解释：「_Should_ implicitly allows you to **challenge the premise of the test: “Should it? Really?”**」
- 需求层：「**Requirements are behaviour, too**」；「A story's behaviour is simply its acceptance criteria」
- 场景模板：`Given some initial context (the givens), / When an event occurs, / Then ensure some outcomes.`
- 「**Acceptance criteria should be executable**」

**B. Dan North《There's more to BDD than evolving TDD》**（[外部] `https://dannorth.net/blog/theres-more-to-bdd-than-evolving-tdd/`，`4 Jun 2006`）
- 「BDD is fundamentally about identifying behaviour. **At the analysis level, the behaviour of a story is its acceptance criteria**, which BDD expresses in the form of automated scenarios. **You need analysts working with testers to capture the stories and identify the acceptance criteria, and then you need programmers working with testers to automate the scenarios.**」

**C. Cucumber 官方《Behaviour-Driven Development》**（[外部] `https://cucumber.io/docs/bdd/`）
- 「BDD is a way for software teams to work that **closes the gap between business people and technical people** by: * Encouraging collaboration across roles to build shared understanding of the problem to be solved * Working in rapid, small iterations to increase feedback and the flow of value * Producing system documentation that is automatically checked against the system's behaviour」
- 与既有流程的关系：「**BDD does not replace your existing agile process, it enhances it.** Think of BDD as **a set of plugins for your existing process**」
- 三实践：「We call these practices _**Discovery**, **Formulation**, and **Automation**._」；`Discovery: What it could do` / `Formulation: What it should do` / `Automation: What it actually does`
- 产物定位：「Although documentation and automated tests are produced by a BDD team, **you can think of them as nice side-effects**. The real goal is valuable, working software」

### 1.3 它在我们体系里现在有没有影子 → **有，但只有"验收判据那一半"**

| 本库落点 | 原文 | 与 BDD 的对应关系 `[推断]` |
|---|---|---|
| `roles/implementer.md:107-122` | §4.2 标题「**行为先行**：红—绿—重构」；`1.`「在接缝处先写一个能捕捉目标行为的检查」 | `Behaviour` 替换 `test` 的写法 |
| `roles/driver.md:68` | `verification`「判据必须能判否。**目标主张 + 真实检查入口 + 一组可判否的正/反对照**」 | 「Acceptance criteria should be executable」的本库化 |
| `roles/planner.md:103` | 「验收判据（**可判否的条件清单**）」 | 同上，落在切片层 |
| `roles/planner.md:141` | 「**写判据时先从 Owner 的结果句提出至少一个合理但错误的实现或边界读法**，再找能让两者读数不同的输入与字面期望值」 | Cucumber `Formulation`（把例子写成能判的形态） |
| `roles/reviewer.md:170-186` | §4.5 标题「**反实现挑战**：判据真的能抓住错误实现吗」 | Dan North「Should it? Really?」的审查化 |
| `roles/oracle.md:126-142` | §4.5「反实现挑战：不需要第二个模型的同源信号」 | 同上，落在独立复核侧 |
| `roles/verifier.md:88-105` | §4.2「从真实入口驱动」`2.`「断言**外部可观察的结果**」 | Cucumber「system documentation that is **automatically checked** against the system's behaviour」 |
| `roles/verifier.md:169-186` | §4.6「判据必须能失败」 | 同上 |
| `docs/archive/skills/behavioral-tdd/SKILL.md:3` | description「**行为驱动**垂直切片测试先行技能，在接缝处断言可观测行为…」 | **本仓历史载体**（已归档，不再是现行依据） |

**本库缺的那一半（事实）**：BDD 的 `Discovery`（与业务方开会谈出行为）在本库**没有任何载体**——`roles/driver.md §4.1` 的 frontier 提问（`:143-160`）是"与 Owner 对齐目标与授权"，其产出是 `task-card` 的 `scope`/`authorization`，**不是行为清单**；本库**没有** Given-When-Then 一类的场景载体，也没有"规格即测试"（可执行规格）的形态。`roles/planner.md:145`「每一行门禁必须写下'由什么命令判定'」是**判据 + 命令**，与"规格本身能跑"是两件事。

### 1.4 归哪个角色 + 理由（不给方案，只给支撑归属的原文事实）

| 角色 | 承担 BDD 的哪一部分 | 支撑原文 / 推导链 |
|---|---|---|
| **Driver（主，Discovery 的输入侧）** | 把"要什么"变成可验收的主张 | BDD 的 Discovery 需要"能代表业务方的人在场"（Three Amigos 里的 `product owner`）；本库唯一能代表 Owner 定目标与授权的是 Driver（`roles/driver.md:56-70` task-card 的 `goal`+`verification`；`pipeline.md:120-128` §10 授权检查）。**但注意**：Driver 的产出是**授权与范围**，不是行为清单 → 见 §1.3 的缺口 |
| **Planner（主，Formulation）** | 把行为切成可判否的判据 | `roles/planner.md:103`、`:141`；BDD 的「Acceptance criteria should be executable」在角色分工里就是 `slice-plan.verification` |
| **Implementer（主，Automation）** | 行为先行、先写能表达行为的检查 | `roles/implementer.md:107-122`；Cucumber `Automation`「starting with an automated test to guide the development of the code」 |
| **Reviewer / Oracle（副，`should` 的挑战面）** | 判"行为本身是否仍成立、判据能否抓住错实现" | Dan North 的 `Should it? Really?` 是**挑战动作**，不是实现动作；本库把它放在 `reviewer.md:170` 与 `oracle.md:126`，两者都无权改实现（`reviewer.md:229`「不可以…改候选实现」） |
| **Verifier（副，对着系统行为自动核对）** | 从真实入口断言外部可观察结果 | `roles/verifier.md:88-105`、`:169-186` |

**归属理由的公共骨架 `[推断]`**：BDD 的每一步都有一个"谁有权说这句话"的问题，本库的答案与 BDD 原文一致——**行为该不该是这样的问题归业务侧，行为有没有被实现的问题归工程侧**。这个分界在本库是硬规则（`pipeline.md:45-52` §3：实现者 ≠ 判断者），所以 BDD 不是"归某一个角色"，而是**按它的三个阶段分别落到有权的那一侧**。

---

## 2. TDD · Test Driven Development

### 2.1 三仓形态（三仓都有，且各自完整）

**pstack**
- `skills/tdd/SKILL.md:3`（description）：「**Use only when the user explicitly asks for TDD**, a failing test, or a regression test, OR when the bug has an obvious cheap local test target. **Skip when the test path is unclear, expensive, integration-heavy, or not requested.**」
- `:9`「When fixing a bug with a clear, cheap test path, make the broken behavior executable before changing production code.」
- `:11`「**Do not force a test when it would be impractical.**」
- `:17`「**Write the failing test first.** Add the smallest focused test that would have caught the bug.」
- `:26`「**Prefer no new test over a bad test.**」
- `:30-31`（Guardrails）「Do not change tests merely to match a wrong implementation.」/「**Do not weaken existing assertions unless the expected behavior has genuinely changed and the reason is clear.**」
- `cursor-plugins/pstack/README.md:126`「`/tdd` | you're fixing a bug and there's a cheap local test path. write the failing test first, then the fix.」
- `docs/guide/05-build-and-clean.md:35-43`「Write the failing test first with `/tdd`」…「If a test would need broad harness setup or brittle mocks, the skill says so and uses the closest executable check instead.」
- `skills/poteto-mode/playbooks/bug-fix.md:11`「**Stage the commits so the failing repro lands before the fix in git history.**」
- 配套（BDD 判据那一半）：`skills/principle-test-behavior-not-implementation/SKILL.md:9,11,23`

**addy**
- `skills/test-driven-development/SKILL.md:3`（description）「Drives development with tests using the **red-green-refactor** loop. Use when implementing any logic, fixing any bug, or changing any behavior.」
- `:10`「Write a failing test before writing the code that makes it pass. For bug fixes, reproduce the bug with a test before attempting a fix. **Tests are proof — “seems right” is not done.**」
- `:24-34`「**Discover the Stack First** … **Never assume a default like `npm test`**」→ 本库落点 `roles/implementer.md:91-101`
- `:38-47` 三段图 `RED → GREEN → REFACTOR`；`:51`「Write the test first. **It must fail.** A test that passes immediately proves nothing.」
- `:96-142`「**The Prove-It Pattern (Bug Fixes)**」「When a bug is reported, **do not start by trying to fix it.** Start by writing a test that reproduces it.」
- `:190-209`「**Test State, Not Interactions**」；`:301-310` 反模式表；`:375-385` Red Flags（含 `:384`「Skipping tests to make the suite pass」）；`:387-398` Verification（含 `:395`「No tests were skipped or disabled」）

**matt**
- `skills/engineering/tdd/SKILL.md:3`（description）「Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions “red-green-refactor”, or wants integration tests.」
- `:10`「When exploring the codebase, read `CONTEXT.md` (if it exists) so test names and interface vocabulary match the project's domain language」← **TDD 与 DDD 的接缝在这里，是"读"，不是"谈"**
- `:14`「Tests verify behavior through public interfaces, not implementation details.」
- `:20`「A **seam** is the public boundary you test at」
- `:22`「**Test only at pre-agreed seams.** Before writing any test, write down the seams under test and confirm them with the user. **No test is written at an unconfirmed seam.**」
- `:30-32` 三个反模式：`Implementation-coupled` / `Tautological`（「the assertion recomputes the expected value the way the code does … Expected values must come from an independent source of truth: a known-good literal, a worked example, **the spec**」）/ `Horizontal slicing`
- `:36-38` 循环三规则：「**Red before green.**」/「**One slice at a time.**」/「**Refactoring is not part of the loop.** It belongs to the review stage … not the red → green implementation cycle.」
- `docs/engineering/tdd.md:31`「**There is no refactor phase: it was dropped in June 2026** because agents essentially never performed it, and because review and implementation work better as separate sessions.」
- `docs/engineering/tdd.md:21`（**上游自己承认的洞**）「The skill decides *where* the seams go; **nothing in it decides *whether* a change is worth the loop at all.** … It is [issue #746] and it is open. Until it closes, that judgement is yours or your `CLAUDE.md`'s.」
- `docs/engineering/tdd.md:91` 主链：「`grill-with-docs → to-spec → to-tickets → implement → code-review`」

### 2.2 权威解释（原话，外部）
- Martin Fowler《Test Driven Development》bliki（[外部] `https://martinfowler.com/bliki/TestDrivenDevelopment.html`）：「Write a test for the next bit of functionality you want to add. / Write the functional code until the test passes. / Refactor both new and old code to make it well structured.」；「there's also a vital initial step where we write out a list of test cases first」；「**thinking about the test first forces us to think about the interface to the code first**」；「The most common way that I hear to screw up TDD is neglecting the third step.」
- Kent Beck《Canon TDD》（[外部] `https://newsletter.kentbeck.com/p/canon-tdd`）：五步，末步为「Optionally refactor to improve the implementation design」。
- **TDD 与 BDD 的边界（Fowler 那句是分界的原文）**：TDD 的第三步是重构；BDD 的三实践是 Discovery/Formulation/Automation。**两者不共享同一条主链。**

### 2.3 本库影子（最密的一套，且**已按裁决单选过**）

| 本库落点 | 原文 |
|---|---|
| `roles/implementer.md:107-122` | §4.2「行为先行：红—绿—重构」；`2.`「**绿**：写最少量的实现让它通过，不过度设计」；`3.`「**重构**：在检查保护下整理结构，每一步之后重跑」（= 采纳 addy，**明确不采纳 matt**） |
| `roles/implementer.md:124-139` | §4.3「反同义反复：这条检查真的能失败吗」；`1.`「如果这个检查 import 的每个函数都返回空值，它还会通过吗？」（**逐字对译** `pstack/principle-test-behavior-not-implementation:11`） |
| `roles/implementer.md:161-179` | §4.5「缺陷修复：先复现，再修」；`1.`「用 `roles/investigator.md` 交来的最小复现场景写成检查，跑它，**确认它红**」 |
| `roles/implementer.md:217` / `:219` | 算做完：「`self_verification` 里包含"**预期会红的那一次**"」／不算做完：「**检查是我改绿而不是实现改对**」 |
| `roles/implementer.md:91-101` | §4.1「先发现这个仓库自己的命令」（= addy `:24-34`） |
| `roles/planner.md:49-65` / `:81-97` | §4.1「垂直切片，不按层切」（= matt vertical slice / addy 垂直切片） |
| `roles/planner.md:141` | 先定接缝与判据（= matt `:22`「pre-agreed seams」） |
| `roles/investigator.md:49-67` | §4.1「先建反馈回路，再谈原因」 |
| `roles/investigator.md:76` | 「最小化完成后，把最小场景保存下来，**它就是后面要交给实现方的回归测试本体**」 |
| `roles/verifier.md:98` | 「（仅报告过的 bugfix）确认**红→绿**…确认它对原症状会红」 |
| `roles/verifier.md:169-186` | §4.6 判据必须能失败（变异） |
| `roles/reviewer.md:186-206` | §4.6 判据可伪证性检查 |
| `SOURCES.md:306-313` | **已裁过一次的 TDD 内部冲突**：`4.5 TDD 循环里放不放重构`；甲方 matt `:38`「Refactoring is not part of the loop」，乙方 addy `:38-95`；「**TIM 采纳：采纳乙方：重构在循环内**…**明确不采纳甲方**」，理由是本库角色边界「审查者不改实现」 |
| `docs/archive/skills/behavioral-tdd/SKILL.md` | **本仓历史载体**：`:11`「融合了 Matt Pocock 的垂直切片与接缝测试理论，以及 `pstack` 的"测试行为而非实现细节"硬指标」 |

**登记状态（事实，与"影子"是两件事）**：`SOURCES.md:120` 登记了 pstack `principle-test-behavior-not-implementation:11` 为 `保留`；`SOURCES.md:172-173` 登记了 matt `engineering/tdd:36`（保留）与 `:38`（不采纳）；`SOURCES.md:202` 登记了 addy `test-driven-development:24-37`（保留）。**但 pstack 的 `skills/tdd/SKILL.md` 全文与 addy 的 TDD 全文主体没有逐条登记**——`SOURCES.md:143` 把 pstack `tdd` 列在「`[仅目录]` / 未评估 / 删除（本轮）」里。→ **[事实] 本库的 TDD 纪律是"多处局部吸收 + 部分未登记"，不是一次成体系的吸收。**

### 2.4 归哪个角色 + 理由

| 角色 | 承担哪一部分 | 支撑 |
|---|---|---|
| **Implementer（主）** | 红—绿—重构、发现仓库自己的命令、反同义反复 | `roles/implementer.md:91-139`；`:217`/`:219` |
| **Investigator（主，缺陷路径）** | 先建能判红的回路；最小场景=回归测试本体 | `roles/investigator.md:49-67`、`:76`。Fowler 的"先写测试"在本库被泛化为"**能判红的命令**"（`investigator.md:53`「失败测试 → 直连运行中服务的请求脚本 → …」），这是**本库对 TDD 的一处主动扩张**：测试不再是唯一载体 |
| **Planner（副）** | 定接缝与判据；"这条检查由哪个命令判定" | `roles/planner.md:141`、`:145`；Fowler「thinking about the test first forces us to think about the interface first」 |
| **Verifier / Reviewer / Oracle（副，绿色的上限）** | 绿只证明"实现能满足写下的测试"；要证"判据能抓住错实现"必须另有动作 | `roles/verifier.md:169-186`、`roles/reviewer.md:170-186`、`roles/oracle.md:126-142`。**`reviewer.md:180` 明确划界**：「这里的反实现挑战是**判据证伪**，不是再写一轮产品实现或复做 TDD 循环」 |

**归属理由 `[推断]`**：TDD 的每条规则都要求"手上有代码的写权"（改测试、改实现、跑仓库命令）——`roles/implementer.md:201`「我可以：在指定写入范围内修改代码与检查」。**判断角色手里没有这个权限**（`reviewer.md:227`「只读候选与契约」、`oracle.md:79`「只拿两样输入」），所以他们只能承担"给绿色设上限"的那一半，不能承担红绿循环本身。

---

## 3. DDD · Domain Driven Design（标准术语是 **Design**，不是 Development）

### 3.1 三仓形态：**没有 DDD 技能，只有它的两条零件**

- 全仓 `DDD` 5 处：`mattpocock-skills/CHANGELOG.md:115`（SHA 子串）、`docs/engineering/domain-modeling.md:58`、`:70`、`skills/engineering/codebase-design/SKILL.md:109`；`grep -rniF "domain-driven"` 仅 1 处：`mattpocock-skills/README.md:109`（**书名的引文出处**）。
- **真正承载 DDD 的两处**：
  1. **matt `skills/engineering/domain-modeling/`**（唯一自称 ubiquitous language 的技能）
     - `SKILL.md:3`（description）「Build and sharpen a project's **domain model**. Use when discussing codebase terminology, writing or editing a `CONTEXT.md`, or recording or editing an ADR.」
     - `:8`「Actively build and sharpen the project's domain model as you design. This is the *active* discipline: **challenging terms, inventing edge-case scenarios**, and writing the glossary and decisions down the moment they crystallise. (**Merely *reading* `CONTEXT.md` for vocabulary is not this skill** … This skill is for when you're **changing** the model, not just consuming it.)」
     - `:46`「When the user uses a term that conflicts with the existing language in `CONTEXT.md`, **call it out immediately.** “Your glossary defines 'cancellation' as X, but you seem to mean Y. Which is it?”」
     - `:50`「When the user uses vague or overloaded terms, **propose a precise canonical term.**」
     - `:54`「**Invent scenarios that probe edge cases** and force the user to be precise about the boundaries between concepts.」
     - `:58`「**Cross-reference with code** … “Your code cancels entire Orders, but you just said partial cancellation is possible. Which is right?”」
     - `:62`「When a term is resolved, **update `CONTEXT.md` right there. Don't batch these up**」
     - `:64`「It is **a glossary and nothing else.**」
     - `:70-72` ADR 三条件（Hard to reverse / Surprising without context / The result of a real trade-off）
     - `CONTEXT-FORMAT.md:27`「**Be opinionated.** When multiple words exist for the same concept, pick the best one and list the others under `_Avoid_`.」；`:32-52` `CONTEXT-MAP.md` + `Relationships`（= **Bounded Context 的对应物**）
     - `docs/engineering/domain-modeling.md:70`（**上游自己承认的边界**）「**DDD gets less useful the closer it gets to the implementation**: the payoff is upstream … **On a one-day build, skip it.** And an unreviewed, agent-authored glossary is worse than none: it becomes confident-sounding lore that later sessions treat as truth.」
     - `docs/engineering/domain-modeling.md:73`（**裁定权的上游原文**）「**A domain language you do not understand yourself becomes meaningless drivel once written down. This skill enforces precision once you have the understanding; it does not manufacture vocabulary you do not have.**」
     - `docs/engineering/domain-modeling.md:60-61`「**Where did `/ubiquitous-language` go?** It was removed, and it was not deprecated. Its job moved into `domain-modeling`」
  2. **pstack `skills/principle-model-the-domain/`**（把领域编进结构）
     - `SKILL.md:3`（description）「Apply when **writing stateful logic**, or when code branches a lot … Encode the domain in a structure instead of scattered conditionals.」
     - `:9`「Encode the real domain in a data structure instead of scattering it across conditionals.」
     - `:11`「A structure that matches the domain makes **invalid states unrepresentable** and deletes branches. **Choosing it at write time is cheap.**」
     - `:15-22` 结构清单：「A **state machine** instead of scattered booleans … A **map, registry, lookup table, or discriminated union** … A reducer or command/event model …」
     - `:24`「**Do not force an abstraction.** Prefer boring code if the current shape is already clear」
     - `:26`「The sign that you skipped this is a new feature that grows an existing if/else chain by one more branch」
     - `cursor-plugins/pstack/README.md:213` 分类列为 `architecture`
- 旁证：`mattpocock-skills/skills/engineering/codebase-design/SKILL.md:22`「*Avoid*: boundary (**overloaded with DDD's bounded context**).」；`:109`「**"Boundary"**: overloaded with DDD's bounded context. Say **seam** or **interface**.」→ **matt 明确把 DDD 的一个核心词降级为"不要用"，并把领域词/模块形状分给两个技能**（`docs/engineering/domain-modeling.md:86`「the two are the vocabulary layer under everything else, **this one for the *domain*, that one for the module's *shape***」）。

### 3.2 权威解释（原话，外部）
- **Fowler《Domain-Driven Design》**（[外部] `https://martinfowler.com/bliki/DomainDrivenDesign.html`）：「Domain-Driven Design is an approach to software development that **centers the development on programming a domain model** that has a rich understanding of the processes and rules of a domain… **A particularly important part of DDD is the notion of Strategic Design - how to organize large domains into a network of Bounded Contexts.**」
- **Fowler《Ubiquitous Language》**（[外部] `https://martinfowler.com/bliki/UbiquitousLanguage.html`）：「the practice of building up a common, rigorous language between developers and users. This language should be based on the Domain Model used in the software … **Evans makes clear that using the ubiquitous language in conversations with domain experts is an important part of testing it** … the language (and model) should evolve as the team's understanding of the domain grows.」
- **matt README 引 Evans 原书**（`upstreams/mattpocock-skills/README.md:107-109`）：「With a ubiquitous language, conversations among developers and expressions of the code are all derived from the same domain model. — Eric Evans, [Domain-Driven-Design]」

### 3.3 本库影子（**已吸收，但被主动改写**）

| 本库落点 | 原文 |
|---|---|
| `roles/architect.md:201-217` | §4.9「**术语冲突：映射既有事实源，业务含义由有权者裁定**」；`:203` 触发条件「一个词在 Owner 说法、代码行为、词汇表 / 契约之间冲突，或需求里出现没有定义的领域词」 |
| `roles/architect.md:206` | 「项目已有词汇表 / ADR / 契约先**映射现有事实源**，不预设必须新建文档」（= matt `:40` Create files lazily 的本库化，且更严：先映射既有权威文档） |
| `roles/architect.md:207` | 「列出原文、真实用例与不同读法；**拿具体边界场景向有权定义业务意思的人提问**」（= matt `:54`「Invent scenarios that probe edge cases」） |
| `roles/architect.md:209` | 「业务含义的**裁定权 = 项目 Owner 本人，或 Owner 书面指定 / 明确授权的业务角色**…工程侧（Architect / 任何角色）**不得擅自决定**。Architect 的职责只到：查证…、提出备选、**记录裁定结果**」 |
| `roles/architect.md:210` | 「**Architect 是默认写者，不是业务决定者**」 |
| `roles/architect.md:211` | 「词汇表只放词义与边界；**难回退、无上下文难懂、存在真实取舍**三条齐才建议 ADR」（= matt `:68-72` 三条件的**逐条对译**） |
| `roles/architect.md:99-116` | §4.3「数据形状先行，不变量尽量编码进类型」（= pstack `principle-model-the-domain` 「invalid states unrepresentable」） |
| `roles/architect.md:118-135` | §4.4「至少两个结构不同的候选，外加"不改"对照」（设计空间侧） |
| `roles/investigator.md:95` | 「**保留原症状用词**…发现同一个词在 Owner 说法、代码行为、词汇表之间冲突时，在 `not_proven` 里**并列两种读法，不替它选定含义**」 |
| `roles/planner.md:107` | 「卡里引用的领域词必须是已接受的含义，或明确列为**未决项**；**未决词义不得由切片自行定名**」 |
| `roles/reviewer.md:142` | 「**领域词义冲突要报为阻断并指向有权裁定者，不由审查方替业务定名**」 |
| `roles/driver.md:314` | 升级表：「领域含义待定（词义冲突、无定义新词）→ **Owner 或经 Owner 授权的业务负责人**…**不以 Oracle 代授权**，不由角色自定」 |
| `SOURCES.md:180` | 登记 matt `domain-modeling` 为「**局部吸收（改写）**」，改写点：「上游默认由技能直接写 `CONTEXT.md`/ADR；本库把**裁定权与写权分开**（Owner D3）：业务含义只能由项目 Owner 或 Owner 授权的业务角色裁」 |

**登记状态**：`SOURCES.md:141` 把 pstack `principle-model-the-domain` 列在「`[仅目录]` / 未读全文 / **删除（本轮）**」，理由「**没有读过正文就不算吸收**」。→ **[事实] 本库的 `architect.md §4.3`「数据形状先行 / 不变量编码进类型」与 pstack 的 `principle-model-the-domain` 是同一机制，但在台账上并未登记为已吸收。** 出处在本轮才读到（`principle-model-the-domain/SKILL.md:11,15-22`）。

### 3.4 归哪个角色 + 理由

| 角色 | 承担哪一部分 | 支撑 |
|---|---|---|
| **Architect（主，映射与记录）** | 术语冲突摊开、canonical 化、查证三处说法、写回权威文档、ADR | `roles/architect.md:201-217`；`:99-116` |
| **Owner / Owner 授权的业务角色（决定者，不在 10 个工程角色内）** | **裁定业务含义**——不是"参与"，是**唯一有权** | `roles/architect.md:209`；`roles/driver.md:314`；matt `docs/engineering/domain-modeling.md:73`（「does not manufacture vocabulary you do not have」）**两边同向** |
| **Investigator（供料）** | 保留原始用词、并列冲突读法、不替它选义 | `roles/investigator.md:84-103`、`:95` |
| **Planner / Reviewer（守门）** | 未决词义不得定名；词义冲突报阻断 | `roles/planner.md:107`、`roles/reviewer.md:142` |
| **Implementer（写时落地）** | 把领域编进结构，使非法状态不可表示 | `roles/implementer.md:141-160`（增量纪律）+ `pstack principle-model-the-domain:11`「write time is cheap」；本库目前**没有**一条明确的"写实现时建模"规则 → 见 §3.5 |
| **Bounded Context 在本库没有对应角色/产物** | 本库只有一个项目范围，没有 `CONTEXT-MAP` 层 | `SOURCES.md:180` 只吸收了 glossary/ADR 写法；`roles/architect.md:207` 只有"映射既有事实源"，没有"多上下文划分" |

**归属理由 `[推断]`**：DDD 的机制里**混着两种权利**：①「一个词该是什么意思」= 业务裁定权；②「这个词在代码里长成什么形状」= 写权。本库把这两种权利**拆给了两个不同主体**（`architect.md:209` vs `architect.md:210`），这与 matt 上游"技能直接写 `CONTEXT.md`"不同——**上游不区分，本库区分**。所以 DDD 的归属不能只写 Architect：**裁定那一半不在 10 个角色里**。

### 3.5 [事实] 一处本库未定的事：DDD 的"写时落地"没有承接者

- matt `docs/engineering/domain-modeling.md:70` 说 DDD 的回报在**上游**（命名与概念对齐），但 pstack `principle-model-the-domain:3` 说该机制的作用时刻是**写 stateful logic 时**。
- 本库 `roles/architect.md §4.3`（数据形状/不变量）与 `roles/implementer.md §4.2/§4.4`（行为先行、增量、范围自律）**都不提"领域建模"**；`implementer.md:141-160` 只讲增量与范围。
- **结论（事实层）**：本库有 DDD 的**词汇面**（`architect.md §4.9`）与**部分形状面**（`architect.md §4.3`），**没有**"在写实现时把领域编进结构"的规则。这两条原文指向的行为不同，本库只覆盖了前者 + 设计期的后者。

---

## 4. SDD · Spec Driven Development

### 4.1 三仓形态：**最完整的一套，且三仓各有各的"级别选择"**

**addy（最成体系）**
- `skills/spec-driven-development/SKILL.md:3`（description）「**Creates specs before coding.** Use when starting a new project, feature, or significant change and no specification exists yet… Use when a single requirement spans several independently testable capabilities and needs decomposing into a **capability map** of modules before specifying.」
- `:10`「Write a structured specification before writing any code. **The spec is the shared source of truth between you and the human engineer** — it defines what we're building, why, and how we'll know it's done. **Code without a spec is guessing.**」
- `:12-20` 触发条件（含「The task would take more than 30 minutes to implement」）；**不适用**「Single-line fixes, typo corrections, or changes where requirements are unambiguous and self-contained」
- `:24`「Spec-driven development has **four phases**, preceded by a scope check (Phase 0) … **Do not advance to the next phase until the current one is validated.**」
- `:26-32` 门禁图：`SPECIFY ──→ PLAN ──→ TASKS ──→ IMPLEMENT`，**每阶段下面都写 `Human reviews`**
- `:34-65` **Phase 0 capability map**：「**Stable module ids.** Kebab-case, **chosen once, never renamed mid-initiative.**」；`:63`「**The map is gated like every phase.**」；`:65`「The map, not filename guessing, is the index of what exists」
- `:69`「Start with a high-level vision. **Ask the human clarifying questions until requirements are concrete.**」
- `:71-82`「**Surface assumptions immediately.**」「Don't silently fill in ambiguous requirements.」
- `:84-114` spec 六核心区：`Objective` / `Commands` / `Project Structure` / `Code Style` / `Testing Strategy` / `Boundaries`（Always / Ask first / Never）
- `:113` Boundaries 的 Never 行：「Commit secrets, edit vendor directories, **remove failing tests without approval**」
- `:150-154`「**External spec tools:** This workflow is format-agnostic. **If the project already uses OpenSpec or another specification system, keep that system's artifact format and storage conventions instead of creating a duplicate `SPEC.md`.** … the external tool owns how the approved spec is represented.」
- `:156-168`「**Reframe instructions as success criteria.**」（把"Make the dashboard faster"改成三条可测）
- `:170-184` Phase 2 Plan → `tasks/plan.md`；`:186-204` Phase 3 Tasks（含 `Acceptance` / `Verify` / `Files` 模板；「No task should require changing more than ~5 files」）
- `:206-208` Phase 4 Implement：「Execute tasks one at a time following `incremental-implementation` and `test-driven-development`」← **SDD 与 TDD 的关系在这里：TDD 是 SDD 的 Phase 4 内部机制**
- `:210-217`「**Keeping the Spec Alive**」「The spec is a **living document**, not a one-time artifact」；「Update when decisions change … **Commit the spec** … Reference the spec in PRs」
- `commands/spec.toml`：`/spec` 入口；`commands/build.toml:30`「**Require a spec. Look only for a spec at a known path: SPEC.md at the repo root, docs/SPEC.md, or a file under spec/. A README or arbitrary doc does NOT count. If none exists, stop and tell the user to run /spec first — do not invent requirements.**」← **fail-closed 的 SDD**
- `commands/build.toml:33`「**Single checkpoint.** … This is the only human gate — after approval, run autonomously.」

**matt**
- `skills/engineering/to-spec/SKILL.md:3`（description）「Turn the current conversation into a spec and **publish it to the project issue tracker: no interview, just synthesis** of what you've already discussed.」
- `:7`「**Do NOT interview the user**; just synthesize what you already know.」
- `:13`「Use the project's domain glossary vocabulary throughout the spec, and respect any ADRs in the area you're touching.」← **SDD 与 DDD 的接缝**
- `:15`「**Sketch out the seams at which you're going to test the feature.** … The fewer seams across the codebase, the better - the ideal number is one.」；`:17`「Check with the user that these seams match their expectations.」
- `:19`「then **publish it to the project issue tracker**. Apply the `ready-for-agent` triage label」
- `:21-73` spec 模板：`Problem Statement` / `Solution` / `User Stories` / `Implementation Decisions` / `Testing Decisions` / `Out of Scope` / `Further Notes`
- `:55`「**Do NOT include specific file paths or code snippets.** They may end up being outdated very quickly.」
- `docs/engineering/tdd.md:91` 主链把 spec 摆在中间：「`grill-with-docs → to-spec → to-tickets → implement → code-review`」

**pstack**
- `skills/architect/SKILL.md:3`（description）「**Sketch types, signatures, and module structure before code**, then stay in the loop while implementation fills in.」
- `:9`「Design before implementing. Sketch types, function signatures, class shapes, and module boundaries with `not implemented` bodies and pseudocode. … **If implementation proves the sketch wrong, throw it out and redesign.**」
- `:35`「**Design it twice.** Require at least two structurally distinct candidates before synthesis, even when the first looks sufficient.」
- `:43-47` **Phase C Agree（opt-in）**「**Default: proceed directly to implementation with the synthesized design. No human checkpoint.** Opt in to a checkpoint when the invoker explicitly asks」← **pstack 与 addy 的关键分歧：人工门是不是默认开**
- `:55`「Replace `not implemented` bodies with code, pseudocode with logic. **The synthesized sketch is the contract.**」
- `:57`「**Deviations from the sketch are signal worth surfacing**, not friction to absorb silently.」
- `:59-70` **Phase E Scrap**「If implementation keeps producing friction the sketch can't absorb, **throw the sketch out**.」
- `docs/guide/README.md:10`「Design the change. `/architect`, `/arena`, `/swarm`, and `/interrogate` before code locks in a shape.」
- `skills/poteto-mode/playbooks/multi-phase-plan.md:3`「**The plan is the deliverable.**」；`docs/guide/06-verify-and-ship.md:7-9`「State the finish condition up front. Put what done means in the first prompt」

### 4.2 权威解释（原话，外部）
- **GitHub Spec Kit**（[外部] `https://github.com/github/spec-kit`）：
  - 「Define **what and why** before deciding **how** to build it. SDD turns your requirements into a specification, a technical plan, and actionable tasks, then guides implementation against those artifacts.」
  - 「**Constitution once per project; specify → plan → tasks → implement → converge per feature.**」
  - 「Repeat **implement → converge** until convergence reports **Converged**.」
  - 「These are **independent entry points**, not three mandatory phases.」
- **Böckeler / martinfowler.com《Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl》**（[外部] `https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html`）：
  - 三级分类：「1. **Spec-first**: A well thought-out spec is written first, and then used in the AI-assisted development workflow for the task at hand. 2. **Spec-anchored**: The spec is kept even after the task is complete, to continue using it for evolution and maintenance of the respective feature. 3. **Spec-as-source**: The spec is the main source file over time, and only the spec is edited by the human, the human never touches the code.」
  - 「**All SDD approaches and definitions I've found are spec-first, but not all strive to be spec-anchored or spec-as-source.** And often it's left vague or totally open what the spec maintenance strategy over time is meant to be.」
  - **SDD 与 TDD/BDD 的关系（原文）**：「While many people draw analogies between SDD and TDD or BDD, I think another important parallel to look at for spec-as-source in particular is **MDD (model-driven development)**.」→ **作者把 SDD 的"同源家族"认成 MDD，不是 TDD/BDD。**
  - 「**the term “spec-driven development” isn't very well defined yet**」
  - Kiro 的工作流（转述于该文）：「**Workflow:** Requirements → Design → Tasks … Each workflow step is represented by one markdown document」
  - 「Tessl is the only one of these three tools that **explicitly aspires to a spec-anchored approach, and is even exploring the spec-as-source level**」

### 4.3 本库影子（**有，但不是从 addy 吸收的**）

| 本库落点 | 原文 |
|---|---|
| `roles/driver.md:56-70` | `task-card` 八字段：`goal` / `symptom` / `scope` / `authorization` / `auth_record` / `dependencies` / `verification` / `escalation` |
| `roles/architect.md:34-52` | `design-proposal` 十字段：`caller_usage` / `data_shapes` / `alternatives` / `red_flag_screen` / `invariants` / `change_cost` / `open_questions` / `chosen_shape` / `approved_by` / `bound_contract` |
| `roles/architect.md:49` | `bound_contract`「这个形状绑定的**冻结契约**／版本标识…供下游引用」 |
| `roles/planner.md:35-46` | `slice-plan` 五字段：`slices` / `dependencies` / `verification` / `scope` / `stop_condition` |
| `roles/planner.md:103` | 「写四件事：…验收判据（可判否的条件清单）；验证动作…；依赖」 |
| `pipeline.md:45-52` | §3 硬规则：第 5 条「**判断者不得由本人放宽判据。** 判据不足由 `roles/planner.md` 补」 |
| `pipeline.md:55-67` | §4 四类依赖，第 1 类 `接口冻结`「上游交出确定的接口/契约，消费者可据此开发」 |
| `pipeline.md:88-94` | §6 写窗：`1.`「候选**冻结**后，发出交付通知，等**接收确认**」；`3.`「**定向返修 = 新候选 + 新冻结**」 |
| `pipeline.md:104-113` | §8 证据复用四条件 |
| `pipeline.md:114-119` | §9 波次汇合：「一个批次交付前，必须在**合并后的候选**上走一次**旅程级验收**：完整用户旅程、关键路径、真实入口。**各项各自 PASS 的集合不等于交付**」← **本库对"converge"的对应物** |
| `closure.md:21-33` | 主链相邻校验表：每行的"输出字段"必须逐字等于下一行的"输入字段" |
| `closure.md:5-8` | 「**每一环被跳过时，下一环要收的收据必须完整地被交出来**…**只移交"职责"不算通过**：字段缺一条，接收方按自己 §2 就有权拒收」 |
| `identity.md:1-20` | 对象身份的**单一真源**：`commit:<sha>` / `tree:<sha>` / `ws:v1:<sha256>`；「`base` 指向基线对象，`object` 指向被检查的候选对象」 |
| `pipeline.md:31-43` | §2 装配档位：按「项目成熟度 × 本次变更风险」选档，**不按文件数选** |
| `roles/verifier.md:130-147` | §4.4 三态结论（`PASS` / `FAIL` / `UNVERIFIED`） |
| `roles/integrator.md:80-96` | §4.2「组合检查：**无文本冲突不是通过**」 |
| `docs/TIM-PROFESSIONAL-WORKFLOW-PROPOSAL.md:203-205` | **历史裁决**：把「规格驱动 vs 代码即规格」列为五大冲突之一，裁决为「**动态厚薄路由：小修局部走薄配方，跨边界大改走厚规格；支持运行中自动升级厚度并隔离试验**」 |
| `docs/archive/workflows/thick-cross-boundary.md` / `thin-bugfix.md` | 上述裁决的**历史载体**（已归档） |

**登记状态（关键事实）**：`SOURCES.md:253` 把 addy 的 `skills/spec-driven-development` 登记为「**未读全文 / NOT ABSORBED**」；`SOURCES.md:183` 把 matt 的 `to-spec`、`grill-with-docs` 登记为「**未读全文 / NOT ABSORBED**」。
→ **[事实] 本库的 spec 层（task-card / design-proposal / slice-plan / 冻结契约）不是从 addy 的 SDD 吸收来的，而是本库自己长出来的；两边的相似是"同一工程直觉的两次独立实现"，不是传承。** 这条对"该归哪个角色"有直接影响：**本库不需要为了装 SDD 而新增载体，因为载体已经在，只是名字不叫 spec。**

### 4.4 归哪个角色 + 理由

| 角色 | 承担哪一部分 | 支撑 |
|---|---|---|
| **Driver（主，"每批的宪法"）** | 每批一份 `task-card`：目标、范围、授权、依赖、判据。**这是本库的 constitution/specify 位置** | `roles/driver.md:56-70`；`pipeline.md:120-128` §10 授权检查。理由：spec-kit 的 constitution 是"每个项目一次"（[外部]），本库对应的是"**每批一次**"的卡；**这是本库对 SDD 的一处改写** |
| **Architect（主，spec 的技术层）** | `design-proposal`：调用方用法先行、数据形状、候选对照、不变量、绑定的冻结契约 | `roles/architect.md:34-52`；`:82`「先写调用者用法，再推导类型」；`:99`「数据形状先行」 |
| **Planner（主，spec → tasks）** | `slice-plan`：垂直切片 + 每片判据 + 验证命令 + 停止条件 | `roles/planner.md:35-46`、`:103`；= spec-kit 的 `plan → tasks` |
| **Implementer（承约者）** | 在冻结契约内实现；偏离即信号，不静默吸收 | `roles/implementer.md:161-179`；pstack `architect/SKILL.md:57`「Deviations from the sketch are signal worth surfacing」同向 |
| **Verifier / Reviewer / Integrator / Oracle（守约者）** | `closure.md` 字段闭环 + `identity.md` 对象身份，使"实现是否按 spec 走"可核对 | `closure.md:21-33`、`identity.md:1-20`、`pipeline.md:114-119` |
| **本库当前处在 SDD 的哪一级** | **spec-first + 局部 spec-anchored**：`design-proposal` / `slice-plan` 是每批冻结的契约（`pipeline.md:88-94`）；但本库**没有** "spec 作为长期活文档"的载体（无 `docs/specs/`、无 spec 生命周期字段），所以**不是** Böckeler 定义的 spec-anchored / spec-as-source | `pipeline.md §6`；本仓无 spec 目录（`find . -name 'SPEC*.md'` 0 命中） |

**归属理由 `[推断]`**：SDD 的每一步都在回答"**谁有权冻结**"。本库的答案是分层冻结——`task-card`（Driver，含授权）、`design-proposal.bound_contract`（Architect）、`slice-plan.verification`（Planner）、候选身份（Implementer 产出、由 `identity.md` 固定）。**没有哪一层能单独叫 "the spec"**，这也是 REPAIR-PLAN-3 那句「`design-proposal` 是**设计契约**，不自动等于完整产品 spec」的原文来源。

---

## 5. 必须单独查的冲突：BDD「前提变了就删测试」 vs 本库「不许为变绿削弱检查」

### 5.1 上游 BDD 原文（外部，逐字）

`https://dannorth.net/blog/introducing-bdd/`，小节 **An expressive test name is helpful when a test fails**：
> 「After a while, I found that **if I was changing code and caused a test to fail**, I could look at the test method name and identify the intended behaviour of the code. Typically one of three things had happened:
> * I had introduced a bug. Bad me. Solution: Fix the bug.
> * The intended behaviour was still relevant but had moved elsewhere. Solution: Move the test and maybe change it.
> * **The behaviour was no longer correct; the premise of the system had changed. Solution: _Delete the test._**
>
> **The latter is likely to happen on agile projects as your understanding evolves.** Unfortunately, **novice TDDers have an innate fear of deleting tests**, as though it somehow reduces the quality of their code.
>
> A more subtle aspect of the word _should_ becomes apparent when compared with the more formal alternatives of _will_ or _shall_. **_Should_ implicitly allows you to challenge the premise of the test: “Should it? Really?”** This makes it easier to decide whether a test is failing due to a bug you have introduced or simply because your previous assumptions about the system's behaviour are now incorrect.」

**同页另有一段（写测试时的对话）**（小节 **“Behaviour” is a more useful word than “test”**）：
> 「When a test fails, simply work through the process described above: **either you introduced a bug, the behaviour moved, or the test is no longer relevant.**」

### 5.2 上游到底**谁有权**宣布"前提变了" → **上游没有指定人；原文只指定了"前提属于哪一层"**

- `[事实]` Dan North 段落的主语是「**I was changing code**」与「**you**」——即**正在改代码、刚把测试搞红的那个实现者**。他给出的是**三个诊断分支**，不是**授权规则**。
- `[事实]` 但同一位作者在另一篇里把**前提下沉的层**点明了：`https://dannorth.net/blog/theres-more-to-bdd-than-evolving-tdd/`
  > 「At the **analysis** level, the behaviour of a story is its acceptance criteria … **You need analysts working with testers to capture the stories and identify the acceptance criteria**, and then you need programmers working with testers to automate the scenarios.」
  → **"行为该不该是这样"这一层的原始拥有者是 analyst / 业务侧，不是 programmer。**
- `[事实]` Cucumber 官方把"谁在场"写成了硬规则：`https://cucumber.io/docs/bdd/discovery-workshop/`
  > 「A discovery workshop is a conversation where **technical and business people collaborate** to explore, discover and **agree** as much as they can about the desired behaviour for a User Story.」
  > 「at a bare minimum your **Three Amigos** should be present: **a product owner, a developer, and a tester**. Your **product owner will identify the problem** the team should be trying to solve, your developer will address how to build a solution around said problem, and your tester will address any edge cases that could arise.」
- `[推断，推导链]` 因此："前提变了"**不是实现者可以单方面判定的事实**——原文给的三个分支里，"bug"与"行为搬家"是工程判断，第三支（"行为不再正确"）要求的输入（业务想要什么）**只在 analyst / product owner 手里**。Dan North 的 `Should it? Really?` 是一个**需要对方回答的挑战**，不是自我授权。**但必须说清：这是从三份原文合成出来的，Dan North 本人没有写"谁有权宣布"。**

### 5.3 三仓的处置：**三仓彼此不一致，且都留了缺口**

| 仓 | 原文 | 谁批 |
|---|---|---|
| **pstack** | `skills/tdd/SKILL.md:31`（Guardrails）「**Do not weaken existing assertions unless the expected behavior has genuinely changed and the reason is clear.**」 | **没有指名任何人**；标准是"行为真的变了 + 理由清楚"——即**由执行者自证** |
| **pstack** | `skills/principle-test-behavior-not-implementation/SKILL.md:11`「If yes, it observes no behavior and cannot fail for a defect. **Rewrite the assertion or delete the test.**」；`:23`「When no such assertion exists, **delete the test**.」 | 这是**另一个删除理由**（检查抓不到缺陷），与"前提变了"无关——**两者不能混** |
| **addy** | `skills/spec-driven-development/SKILL.md:113` Boundaries 的 `Never do`：「Commit secrets, edit vendor directories, **remove failing tests without approval**」 | **需要 "approval"** ← 三仓里**唯一明写"要批"**的一处 |
| **addy** | `skills/constraint-driven-development/SKILL.md:108`（Floor）「No skipped or deleted tests **without a reason in the commit message**」 | **要"理由入提交信息"**，不要求事前批准 |
| **addy** | `skills/constraint-driven-development/SKILL.md:133-137`（Exceptions 表）列头含 **`Owner`** 与 **`Expires`**：「`Exceptions` / `ID` / `Rule` / `Path` / `Reason` / **`Owner`** / **`Expires`**」（示例行 `W1 | no-explicit-any | src/legacy/** | Rewrite tracked in ENG-441 | @addy | 2026-11-01`） | **降档必须登记到人 + 到期日** |
| **addy** | `skills/constraint-driven-development/references/floor-guard.md:10`（Contract）「**Detects the five Step 6 moves:** a weakened threshold in `CONSTRAINTS.md`, **a test made easier (`.skip`, a deleted test file, an assertion removed from a test that stayed)**, a silenced checker …」；`:14`「**Tightening is silent, loosening is loud:** only surfaces moves that lower the bar.」；`:11`「Exit codes: `0` clean, `1` at least one floor violation (**block the change**)」 | **放松被机器盯住并阻断** |
| **addy** | `skills/test-driven-development/SKILL.md:384`（Red Flags）「Skipping tests to make the suite pass」；`:395`「No tests were skipped or disabled」 | 同向 |

**三仓结论 `[事实]`**：
1. **"删测试"在三仓是两件不同的事**——(a) 检查抓不到缺陷 ⇒ **pstack 允许直接删**（`principle-test-behavior-not-implementation:11,23`）；(b) 为了通过而放松 ⇒ pstack 有条件允许（`tdd:31`），addy 要求"批准"或"记理由"并**用 floor-guard 拦**。
2. **"谁有权宣布前提变了"三仓都没有回答**。最接近的是 addy 的两种机制（`without approval` / Exceptions 表的 `Owner` 列），但它们管的是**质量底线（CONSTRAINTS.md）**，不是"业务行为该不该是这样"。

### 5.4 本库的原文

**禁的那一侧**
- `roles/implementer.md:121`（§4.2「反例」）「**反例：为了让检查变绿而修改期望值、跳过检查或删掉检查。**」
- `roles/implementer.md:203`（§5「我不可以」）「**为了让检查变绿而削弱检查**」
- `roles/implementer.md:219`（§7「不算做完」）「**检查是我改绿而不是实现改对**」
- `roles/verifier.md:184`（§4.6「反例」）「**反例：为了让证据好看而删除、跳过或弱化检查。**」
- `roles/planner.md:132`（§4.5「反例」）「**反例：把门禁本身改松以让改动通过。**」
- `pipeline.md:49`（§3 第 5 条）「**判断者不得由本人放宽判据。** 判据不足由 `roles/planner.md` 补，不由审查/验证方临时放宽。」
- `roles/reviewer.md:186-206` §4.6 判据可伪证性检查（把"判不了"的判据列为形态 1–7）

**允许删的那一侧（本库自己也有，且与 pstack 同源）**
- `roles/implementer.md:132`（§4.3 第 4 步）「**找不到这样的断言就删掉检查。**」
- `roles/architect.md:90`（§4.1）「用"**删除测试**"检查每个模块：想象删掉它。」

**改判据的路径（本库的"谁批"答案）**
| 情形 | 归属 | 原文 |
|---|---|---|
| 判据不够、写不出判否 | → Planner | `pipeline.md:49`；`roles/planner.md:136-153` §4.6；`roles/verifier.md:234`「判据本身无法判否 → `roles/planner.md`（补判据）」 |
| 判据有争议 | → Driver 判触发条件 | `roles/verifier.md:234`；`roles/driver.md:248-264` §4.7 |
| 改测试需要新写窗 | → **由 Implementer 改测试并形成新候选 / 新冻结**；Driver 与 Reviewer 都不顺手改产品 | `roles/driver.md:172`「补判据涉及新测试写窗时，由 `roles/implementer.md` 改测试并形成新候选/新冻结——**Driver 与 Reviewer 都不顺手改产品**」 |
| 前提本身被证伪 | → Investigator 重新归因 | `roles/planner.md:160`「前提不真交 `roles/investigator.md`」；`roles/architect.md:231` |
| **前提变了（= 业务行为不再正确）** | → **Owner 或 Owner 授权的业务角色** | `roles/architect.md:209`；`roles/driver.md:314` |
| 实现者自己想改判据 | **只能请求，不能决定** | `roles/implementer.md:201`（我可以）「**请求补前提或改切片**」；`:205-213` §6 升级表 |

**本库对"前提"的专门机制**（这一节最容易被漏掉）
- `roles/investigator.md:142-154` §4.6「**连续失败：质疑前提，而不是写第三个补丁**」：`:144` 触发「两个或更多共享同一前提的修复，在同一道判据上连续失败」；`:147`「把那句被所有失败修复共享的前提写下来」；`:150`「若清点是均匀的，前提不是原因」；`:151`「前提未写下、清点未做之前，不许提第三次修复」
- `roles/driver.md:215-228` §4.5「停止与归因：同前提重复失败转 Investigator」；`:220`「停止发第三次同前提修复，把这次停止记为一次**归因转手**」
- `roles/planner.md:154-160` §4.7 停止条件第 1 条「同一**前提、同一道判据、无新证据**的连续两轮失败（→ 转 `roles/investigator.md` 重新归因，**前提清点由它做**）」；第 2 条「前提不真交 `roles/investigator.md`」
- **出处**：`SOURCES.md:127` 登记 pstack `principle-attack-the-premise`（本轮已读：`upstreams/cursor-plugins/pstack/skills/principle-attack-the-premise/SKILL.md:9`「When two or more fixes that share one premise have failed the same gate, suspect the premise, not the fixes.」；`:14`「**Write the premise down.**」）为落点 `roles/investigator.md §4.6`。

### 5.5 两边对不对得上（**这是本节的结论，只做事实判定，不做裁决**）

| 命题 | 判定 | 依据 |
|---|---|---|
| BDD 的"Delete the test"＝"为变绿而删断言"？ | **不是同一件事** | BDD 的前提是**行为不再正确**（业务事件）；本库禁的是**检查妨碍通过**（工程事件）。两者的**主语不同**：前者是"要的行为变了"，后者是"我要它变绿"。BDD 原文第 2 支「Move the test and maybe change it」与本库"改判据要回 Planner"同向 |
| 本库是否覆盖了 BDD 的合法删测试场景？ | **部分覆盖，有一处缺口 `[事实]`** | 覆盖：`implementer.md:132`（检查抓不到缺陷可删，与 pstack `:11` 同源）＋ `implementer.md:201`（可请求改判据）＋ `architect.md:209`（业务含义归 Owner）。**缺口：本库没有任何一条规则说"当 Owner 判定某行为不再需要时，对应的检查由谁、按什么程序移除"。** `pipeline.md:88-94` §6 只规定"定向返修 = 新候选 + 新冻结"，**没说"判据被撤销"这种情形**（`grep -rn "撤销\|废止\|不再需要" roles/ pipeline.md closure.md` → **0 命中**） |
| 谁有权宣布"前提变了"（本库 vs BDD） | **本库比 BDD 明确** | BDD 原文没点名（§5.2）；本库点名了两类：**业务前提** → Owner/授权业务角色（`architect.md:209`、`driver.md:314`）；**诊断前提（为什么一直失败）** → Investigator（`investigator.md:142-154`）。**这是本库相对上游的一处加强，不是冲突** |
| "不许为变绿削弱检查"是否过宽、会不会误伤 BDD 的合法场景？ | **从原文看，本库写的是"为了让检查变绿"，带了限定语，不是禁止一切删除** | `implementer.md:203` 原文「**为了让检查变绿**而削弱检查」；`implementer.md:121` 原文「**为了让检查变绿**而修改期望值、跳过检查或删掉检查」。两处都带这个状语，且同文件 `:132`、`:137-139` 明确列了三种**可以删／必须保留**的例外。→ **文字上不是"禁止删除检查"** |
| 那么这条冲突还成立吗？ | **成立，但形态不是"A 允许 B 禁止"** `[推断]` | 真正未被本库回答的是 **§5.5 第 2 行那个缺口**：业务前提被撤销之后，遗留检查的移除**程序与授权**没有规则；而 BDD 恰好把这一步当成常规动作（「likely to happen on agile projects as your understanding evolves」）。→ 待裁的是**程序**，不是**许可** |

---

## 6. "四套非严格集合关系"的证据汇编（回应 Oracle 的纠正）

Oracle 的判词（原文在 `.pi/core/REPAIR-PLAN-3.md:13`）：
> 「BDD 源于 TDD、扩展到需求发现与验收，**不是严格集合式 `BDD ⊃ TDD`**；TDD 可在没有 BDD 仪式的逻辑片实施。DDD 的领域模型会贯穿设计/代码与演化，**不只属于输入层**；SDD 还含收敛/核验，也不只是输入层。」

本轮独立取证，逐条给证据：

| Oracle 的判断 | 本轮证据 | 判定 |
|---|---|---|
| 不是严格 `BDD ⊃ TDD` | ① Dan North 自述 BDD 起点是**改名**（`introducing-bdd`「I started to refer to TDD as BDD」），不是套壳；② BDD 的三实践里 `Discovery`/`Formulation` **不是测试活动**（Cucumber）；③ TDD 可独立成立：pstack `tdd/SKILL.md:3`「**Use only when the user explicitly asks for TDD** … **Skip when the test path is unclear**」；matt `docs/engineering/tdd.md:21`「nothing in it decides *whether* a change is worth the loop at all」；④ 本库自己是分开装的：`implementer.md §4.2`（TDD 循环）与 `reviewer.md §4.5`（BDD 的 `Should it?`）**在两个角色里** | **成立** |
| DDD 不只属于输入层 | pstack `principle-model-the-domain/SKILL.md:3`「Apply when **writing stateful logic**」；`:11`「**Choosing it at write time is cheap.**」→ 该机制的触发时刻在实现；matt `domain-modeling/SKILL.md:8` 是"design 时主动改模型"（设计期）；`docs/engineering/domain-modeling.md:70` 又说回报在 implementation **之前** → **同一个 DDD 在三个不同时刻各有一段**，任一层都装不下 | **成立** |
| SDD 不只属于输入层 | spec-kit（[外部]）「**specify → plan → tasks → implement → converge per feature**」「Repeat **implement → converge** until convergence reports **Converged**」（4/5 段在输入层之后）；addy `spec-driven-development/SKILL.md:24-32` 的 Phase 4 是 `IMPLEMENT`；`:210-217`「**Keeping the Spec Alive** … The spec is a **living document**」 | **成立** |
| 四套非严格集合关系（一般形式） | §0.2：四套回答**四个不同轴**的问题；§7 反证表给"任何包含链都至少有一个反例" | **成立** |

### 6.1 [事实] 哪些"包含链"能被原文直接反证

| 假想的包含关系 | 反例（原文） |
|---|---|
| `BDD ⊃ TDD` | TDD 可在无任何 BDD 仪式的场景下独立执行（pstack `tdd:3` 的触发条件、matt `docs/engineering/tdd.md:21` 的洞） |
| `TDD ⊃ BDD` | BDD 的 `Discovery` 不写测试（Cucumber），且 BDD 的权威对话方是 analyst/PO（Dan North `theres-more-to-bdd…`） |
| `SDD ⊃ TDD` | spec-kit 的 SDD 主链末段是 `converge`，**不是** red-green-refactor；addy 把 TDD 放在 Phase **4 内部**（`spec-driven-development:208`）——即 TDD 是 SDD 的**实现手段**，不是它的子集，因为 TDD 也能在无 spec 时独立跑（pstack `tdd:3`） |
| `TDD ⊃ SDD` | spec-kit `converge` 与 Böckeler 的三级（spec-first/anchored/source）在 TDD 里没有对应物 |
| `DDD ⊃ 任何` / `任何 ⊃ DDD` | DDD 的裁定权在业务侧（matt `domain-modeling docs:73`、本库 `architect.md:209`），TDD/SDD 的授权在工程侧 → **权利主体不同，无法互为子集** |
| `BDD = "TDD 的行为版"` | Böckeler 把 SDD 的"同源家族"认成 **MDD** 而不是 TDD/BDD（原文「another important parallel … is MDD」）——**类比关系在专业文献里本身就存在分歧**，不能当成定义 |

---

## 7. 供裁决用的开放点（**不是方案，只列证据不足或缺原文的位置**）

| # | 开放点 | 为什么本文件判不了 |
|---|---|---|
| O1 | **BDD 的 Discovery 在本库没有承接者** | 三仓无此法（§1.1）；本库 `driver.md §4.1` 的产出是授权与范围，不是行为清单（§1.3）。要不要有、由谁有，是设计决定 |
| O2 | **"业务前提被撤销后，遗留检查的移除程序"没有规则** | 本库 `grep 撤销\|废止\|不再需要` → 0 命中；`pipeline.md §6` 只覆盖"定向返修"（§5.5 第 2 行） |
| O3 | **DDD 的"写时落地"没有角色** | pstack `principle-model-the-domain:11` 要求 write time 建模；本库 `implementer.md` 无对应规则；且该上游文件在 `SOURCES.md:141` 仍登记为"未读/删除"（§3.5） |
| O4 | **SDD 的级别选择（spec-first / anchored / source）本库未表态** | 本库现状实测为 spec-first + 局部 anchored（§4.4 末），但**没有任何文档写下这个选择**；Böckeler 明说这个选择本身"often left vague" |
| O5 | **`design-proposal` 是不是 "the spec"** | REPAIR-PLAN-3 已判"不自动等于完整产品 spec"，但**本库没有一处正面定义 what/why 的承载物**（`owner-brief` 是 Driver 收的、`task-card` 是 Driver 发的，两者的字段都不含"用户是谁 / 为什么现在"） |
| O6 | **Bounded Context 在本库无对应物** | `SOURCES.md:180` 只吸收 glossary/ADR 写法；多领域同名异义时的边界载体在三仓里 matt 有（`CONTEXT-FORMAT.md:32-52`），本库没有（§3.4） |
| O7 | **三仓自己就"谁批准删测试"不一致** | §5.3：pstack 无名批准人 / addy `spec-driven-development:113` 要 approval / addy `constraint-driven-development:108` 只要理由入提交信息。**取哪一条是取舍，不是取证** |

---

## 8. 可复现的检索命令（"三仓无此法"的核对方式）

```bash
cd /Users/yuantian/Developer/tim-professional-workflow/upstreams
for p in BDD behaviour-driven behavior-driven TDD test-driven DDD domain-driven SDD spec-driven \
         given-when-then gherkin cucumber ubiquitous; do
  printf '%-16s %s\n' "$p" "$(grep -rniF "$p" --include='*.md' --include='*.toml' --include='*.json' --include='*.js' --include='*.ts' . 2>/dev/null | grep -v node_modules | wc -l | tr -d ' ')"
done
# 逐条看命中（排除 SHA 子串）：
grep -rnoiE '.{30}bdd.{30}' --include='*.md' . | grep -v node_modules
grep -rnoiE '.{30}ddd.{30}' --include='*.md' . | grep -v node_modules
```

实测结果（2026-09-27，pin 见文首）：

| 串 | 命中数 | 其中实质命中 |
|---|---|---|
| `BDD` | 7 | **0**（全为 matt `CHANGELOG.md` 的 SHA 子串） |
| `behaviour-driven` / `behavior-driven` | 0 / 0 | 0 |
| `given-when-then` / `gherkin` / `cucumber` | 0 / 0 / 0 | 0 |
| `TDD` | 92 | 有（40 个文件） |
| `DDD` | 5 | 3（`domain-modeling.md:58`、`:70`、`codebase-design/SKILL.md:109`） |
| `domain-driven` | 1 | 1（`upstreams/mattpocock-skills/README.md:109` 引文书名） |
| `ubiquitous` | 10 | 有（matt domain-modeling 一系） |
| `SDD` / `spec-driven` | 23 / 66 | 有（addy `spec-driven-development`、`commands/*`；matt `grill-with-docs` 文档；pstack `architect`） |

---

## 9. 本文件的"三仓无此法"汇总

1. **BDD 作为一个方法名**：三仓无此法（§1.1）。BDD 的三实践（Discovery / Formulation / Automation）、Given-When-Then、可执行规格，三仓**全无**。
2. **"谁有权宣布前提变了"**：三仓无此法（§5.3）。三仓只给"要批准 / 要理由 / 放松会被拦"，**没有一处指定业务前提的裁定人**。
3. **DDD 作为一个技能**：三仓无此法（§3.1）。只有两条零件（matt 的术语纪律、pstack 的写时建模），且两处都不自称 DDD。
4. **Bounded Context / 上下文映射作为可操作产物**：matt 有 `CONTEXT-MAP.md`（`CONTEXT-FORMAT.md:32-52`），**pstack / addy 无此法**；本仓也**没有**对应产物。
5. **SDD 的三级（spec-first / spec-anchored / spec-as-source）**：pstack / matt 无此分类；**只有 addy 一系（spec 作为活文档）+ 外部 Böckeler**。
6. **"出范围为代价"的 spec 生命期字段**：三仓都没有"spec 的维护者 / 到期 / 替代关系"字段（对照：addy 的 `CONSTRAINTS.md` Exceptions 表有 `Owner` + `Expires`，但那只管质量底线，不管 spec）。
