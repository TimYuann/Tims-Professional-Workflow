# A2R-CURSOR-ABC4 · cursor-plugins 审核包 4（Voice 表达 / 技术写作 / 注释与清理 / 学习与个人化）

- 发现者：tpw-absorb-a2r（A2r）
- 源仓：`cursor-plugins`，pin `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`（只读 locator：`.worktrees/legacy-pre-night-2026-10-01/upstreams/cursor-plugins`）
- 产品基线：night worktree；core `professional-workflow/`（21 文件）；冻结 Backbone 未触碰
- 供 `tpw-absorb-gate` 实质裁定；本包不自行裁定采纳；处置均为“拟/候选/待裁定”
- 组成本包的四族均为 A/Voice/B/meta 面；不重复包 1–3 已记录的机制。

## 1. 包内机制组总览

| MG | 机制组 | 主要源文件（pin 内） | 建议判断位点 | 类型 |
| --- | --- | --- | --- | --- |
| MG-1 | 面向人的清晰表达与 AI 痕迹清理 | `pstack/skills/bro/SKILL.md`、`pstack/skills/unslop/SKILL.md` | A/Voice（解释与沟通） | 规则候选 |
| MG-2 | 技术写作分层标准 | `pstack/skills/technical-writing/SKILL.md` | A/Voice/B（文档、PR 描述、commit） | 方法候选 |
| MG-3 | 注释纪律与代码 slop 清理 | `pstack/skills/no-comments/SKILL.md`、`pstack/agents/comment-sicko.md`、`cursor-team-kit/skills/deslop/SKILL.md` | B/E 交界（可读性契约） | 方法候选 |
| MG-4 | 学习路径、回顾与个人工作风格 | `teaching/README.md`、`teaching/skills/create-learning-path/SKILL.md`、`teaching/skills/run-learning-retrospective/SKILL.md`、`pstack/skills/automate-me/SKILL.md` | A/meta（能力建设与偏好固化） | 部分吸收/部分拒绝 |

---

## MG-1 面向人的清晰表达与 AI 痕迹清理（A/Voice）

### 1) 机制与触发情境；源锚点与已读/尚缺

| 源锚点 | 已读 | 尚缺 |
| --- | --- | --- |
| `pstack/skills/bro/SKILL.md`（全文，267B） | 全文 | 无 |
| `pstack/skills/unslop/SKILL.md`（全文，6015B，规则 3–33） | 全文 | 无（规则 1/2/4/6/21 等编号空缺，源文说明“A removed rule leaves a gap”，即按 id 稳定保留编号） |
| `pstack/docs/guide/10-recipes-and-pitfalls.md` 的 `/bro` 与 `/unslop` 用法段 | 已读（包 2） | 无 |
| `pstack/skills/poteto-mode/SKILL.md` `## Writing the reply`（包 1 已读） | 已读 | 无（与本组互补：回复写作规则） |

触发情境：技术性很强的回复让人仍不知道说了什么（`/bro`：把最后一条消息用平实人类语言重述、无行话、更简单更简洁）；任何写作表面（`unslop` description：“Cut AI tells from any writing. Must always apply.”）。

### 2) 操作、成立条件、失败模式、反例/例子

**bro（全文机制）**：重述上一条消息；停止使用行话、连贯地说话；更简单更简洁，像一个人对另一个人说话。用法极简（`/bro` 即全部 prompt）。它是 Voice“翻译成人类可理解”的极端形式，不改变内容结论。

**unslop（按类目整理，规则编号保留自源文）**

- Content：3 表面 -ing 短语（highlighting/ensuring/reflecting/showcasing/fostering）→ 删或补真实来源；5 模糊归因（Experts believe / Industry reports suggest / Some critics argue）→ 点名来源或删。
- Language：7 AI 词汇表（Additionally, crucial, delve, enduring, enhance, fostering, garner, interplay, intricate, landscape(抽象), pivotal, showcase, tapestry(抽象), testament, underscore, vibrant）→ 换平实词；8 花式“is”（serves as/stands as/boasts/features）→ 就用 is/has；9 “Not just X, but Y” → 直说要点；10 三段式（rule of three）→ 用自然数量；11 同义词循环 → 选一个词并重复；12 假范围（from X to Y 但不在同一有意义尺度）→ 直接列。
- Style：13 破折号过度 → 完全避免 em dash，只用句号或逗号（含“不用括号、不用 en dash、不用 hyphen 代 dash”）；14 冒号过度 → 冒号只能用在列表/例子前，不能作句中连接；15 粗体过度；16 内联小标题列表（bold label + colon 复述本行）→ 改散文，但“粗体引出、句号结尾、随后是真正新细节”可接受；17 标题用 sentence case；18 装饰性 emoji；19 弯引号 → 直引号。
- Communication artifacts：20 聊天机器人短语（“I hope this helps!”等）→ 删；22 谄媚语气 → 直接回应。
- Filler：23 填充短语（In order to→To；Due to the fact that→Because；“It is important to note that”→删）；24 过度对冲 → 收敛到 may；25 通用结论 → 给具体计划或事实。
- Jargon：26 抽象隐喻名词表（substrate, wedge, vector, locus, vantage, nexus, primitive(as noun), harness(as metaphor), surface(as in API surface), bedrock, scaffolding(as metaphor), modality, paradigm, gold-plating, ratchet(as metaphor), evacuate, endgame, north star, flywheel）→ 换具体词（并给出替换示例：substrate→base、wedge in→add、gold-plating→more than the job needs、endgame→the last phase 等）。
- Plain speech：27 **说它做什么，不说它感觉如何**：给“the database stays close at hand”“SQL you can read”这类感觉句的修复——点名机制或数字；**如果句子换到另一个项目文档里也原样成立，它什么也没说，删掉**；28 缩短或拆分密句（读者要回读就拆）；29 主动语态（只有 actor 未知或确实不重要时才被动）；30 砍副词或用更强的动词（“runs quickly”→给数字）；31 偏好平实词（utilize→use、leverage→use、facilitate→help、numerous→many）；32 做作散文（格言、修辞性残句、拟人化代码、比喻性动词、套话框架）→ 直说；33 **过度压缩**：丢冠词、无动词片段、符号语、让人解码的缩写 → 写完整句子（“Parser rejects bad date → exit 2, no write”改为“The parser rejects a bad date, exits with code 2, and writes nothing.”）。

**成立条件**：有可编辑文本；作者/编辑不改变事实与结论；规则员与“当规则让句子更糟时换一种写法或不动”的元规则同时成立。

**失败模式/反例**：把 unslop 当“改写风格”而改变事实（源文要求 preserve meaning、match intended tone）；把 em dash 用 en dash/hyphen 替代（源文明确禁止替代）；把“bold label + colon”一律禁掉（源文给了可接受的形态）；把过压缩误当简洁（规则 33 反向）；只扫字面词表而不修“感觉 vs 机制”（规则 27）。

### 3) 判断位点与 Profile 调用

| 位点 | 专业 concern | 何时调用 | 由哪个 Profile 提议 |
| --- | --- | --- | --- |
| A/Voice：向人类解释专业取舍 | 沟通可理解性 | 人类看不懂回复/文档时；给 Owner 的解释前 | `intent-voice` |
| B：行为描述与接受条件的写法 | 行为 | 写行为约定/验收描述 | `behavior-domain` |
| 全库：方法/skill 正文自身的写作质量 | 可维护性 | 新写或修改任何方法/Profile 文本 | `driver` / 方法作者 |

### 4) 当前产品锚点、覆盖、缺口、为何值得吸收

- `docs/WORKFLOW-INTENT.md` §4：“更深层判断需要人类决定时，必须翻译成可理解的行为、成本、风险或承诺，不能要求 Owner 对未经解释的实现细节背书。”
- `profiles/intent-voice.md` `## 心智模型`：“Voice 连接人与专业判断：对齐 Delegation Envelope，解释取舍的行为、成本、风险与承诺影响，读回理解，记录接受决定。”
- `profiles/intent-voice.md` `## 常见误区`：“要求 Owner 对未经解释的实现细节背书”。
- 项目 `AGENTS.md` Working Contract：“Prefer Chinese for user-facing discussion…keep code, commands, paths, and API names in their original language.”
- `pstack/skills/poteto-mode/SKILL.md` `## Writing the reply`（包 1 已读）：“Short declarative sentences…No long-dash character anywhere…A colon as a mid-sentence connector is also out”。

已覆盖：产品要求“可理解”；poteto-mode 的回复写作有短句/无破折号/无句中冒号等规则（属参考源，未吸收进产品）。

具体缺口：

1. **产品自身没有写作标准**：方法/Profile/Charter 都是给人读的文本，但没有“说机制不说感觉”“如果换个项目也成立就删”“不堆行话/抽象隐喻”的质量判据；`intent-voice` 的“可理解”只有目标没有操作。
2. **没有“重述为平实语言”的 Voice 动作**：bro 的机制虽然极简，但对应 Voice 的核心失败模式（翻译成了另一套专业话）。
3. **没有 AI 痕迹清单**：本仓产出的方法文本是 agent 生成的，最容易出现 -ing 短语、模糊归因、三段式、抽象隐喻名词（substrate/scaffolding…）、过度压缩的符号语；这些直接损害“可理解”与“可维护”。
4. **没有“规则让句子更糟就另写或不动”的元规则**：单收词表会变成机械 checklist（与执行计划反 ceremony 一致）。

为何值得吸收：直接服务 Voice 的“人类可理解”责任与产品文档的可维护性；全部为文本级规则，零平台耦合，风险低。

### 5) 拟处置与载体

- 拟保留：bro 的“重述为平实语言”动作；unslop 的规则分类与高价值条目（3/5/7/8/9/10/11/12/13/14/16/20/22/23/24/25/26/27/28/29/30/31/32/33）；元规则（规则让句子更糟就另写/不动）；规则 27 的“换个项目也成立就删”检验；规则 33 的反过压缩。
- 拟改变：把 30 条压成产品可维护的短清单（建议保留 12–15 条），按产品语言重写为“写作检查”；把 “unslop”/“bro” 名称去掉，改为动作名（“平实重述”“写作体检”）。
- 拟删除：emoji/弯引号（若产品不使用此类表面，可删）；把“破解折号”改为“避免破折号作连接”的中文适用表述（中文里对应的是破折号/分号滥用，注意语言适配）。
- 载体：方案 1（推荐）新增 `methods/guide-plain-language.md`（写作与重述检查），在 `profiles/intent-voice.md` 按需入口加一行；产品自身文档在写/改时引用该 guide。方案 2 只把“重述为平实语言”加入 `intent-voice.md` 的关键问题（代价：丢失写作质量面）。
- 语言适配提示（供 B/gate）：源规则以英文文本为对象；中文吸收时需保留判断精神（行话、抽象隐喻、填充、过度压缩、被动滥用）而不是逐条直译。

**平台耦合/依赖**：零平台耦合（纯文本规则）。无 SDK/runtime 依赖。

### 6) 正文草稿与验证方案

```
写作体检（草稿，中文适用版）
1. 说机制/数字，不说感觉：把“让数据库触手可及”“SQL 读起来舒服”改成具体行为或数字；若句子换到别的项目也原样成立，删。
2. 平实重述：把一段专业回复用一个人对另一个人的话讲一遍，再决定保留哪版的关键内容。
3. 删填充与对冲：In order to → To；应当/或许/可能 叠加 → 收敛到一个；通用结论 → 具体计划或事实。
4. 不滥用：破折号作连接、句中冒号、三段式、同义词循环、粗体标签复述、装饰 emoji。
5. 主动语态；动词弱就换强动词，别用副词撑。
6. 不过度压缩：保留冠词/动词/完整句子，符号与箭头展开成词。
元规则：任何一条让句子更糟时，换一种写法或不动；事实与结论不得被改。
```

验证方案（未执行）：取本仓一段已发布文本（如某 method 文件）按体检清单改写，检查：(a) 是否不改事实；(b) 抽象隐喻/填充是否减少；(c) 是否出现“换到别的项目也成立”的空话被删。反例：机械套用导致句子更糟（元规则应触发）。边界：不追求统一文风；不改变作者语气 intent。

---

## MG-2 技术写作分层标准（A/Voice/B）

### 1) 机制与触发情境；源锚点与已读/尚缺

| 源锚点 | 已读 | 尚缺 |
| --- | --- | --- |
| `pstack/skills/technical-writing/SKILL.md`（全文，10205B） | 全文 | 其引用的外部规范（diataxis.fr、Google developer style、ASD-STE100、Global English Style Guide）**只按源文转述读取，未逐字读原规范** |
| `pstack/skills/poteto-mode/playbooks/opening-a-pr.md`（PR 描述/commit 规则） | **未读** | 包 1/3 未覆盖；本组引用 guide 05 的转述（PR 体是 briefing、禁 SHA 清单等） |
| `pstack/docs/guide/05-build-and-clean.md` 的 `/technical-writing` 段 | 已读（包 3） | 无 |

触发情境：写或评审 docs、RFC、readme、PR 描述、commit message（description 原文列出的表面）。

### 2) 操作、成立条件、失败模式、反例/例子

**三条元以上规则**：① **每个不做事的词都删**（句子去掉该词仍成立就删；“In order to”即“to”）；② 用短而日常的词（use 不是 utilize；help 不是 facilitate；do 不是 perform）；长词必须用精确性买下它的长度；③ **规则让句子更糟时，换一种写法或不动**——规则服务读者；“follows every rule and sounds like a machine wrote it has failed”。

**第一层：先选模式（Diátaxis）**。一个文档一个模式；两个问题：内容是 inform action（doing）还是 understanding（thinking），服务 learning 还是 work。tutorial（action+learning）：你在教，“learner's success is your job”；开篇说将 build 什么而不是将“学到”什么；每步都有可见结果；告诉对方应看到什么；解释压到一句+链接；用 “we”、命令式。how-to（action+work）：解决人的问题而不是机器的操作；假定有能力；跳过教学；只行动，无 digression/背景/为完整而完整；允许分叉与判断（“If you want x, do y”）；标题按任务命名。reference（understanding+work）：只描述，无 instruction/persuasion/opinion；dry、完整、确定；事实/选项/限制/错误无 hedge；结构 mirror 被描述之物；能由代码生成就生成。explanation（understanding+learning）：一个有界主题，可脱离产品阅读；标题能前置 “About…”；锚定真实 why 问题；给背景（设计决定、历史、约束、替代）；只有在这里允许 opinion。**不得混模式**（tutorial 里不放 reference 表，reference 里不 hand-hold，how-to 里不争论）；要拆开并链接。

**第二层：面向读者的句子（Google developer style）**：用 “you”、现在时（will 只用于真正稍后发生的事）；说谁做什么（“the compiler checks” 而非 “is checked”）；指令写命令式（“Click Submit.”），事实平述，不写 “should be done”；条件在指令前（“To delete the document, click Delete.”）；常见情形在前、例外在后；像懂行的朋友，不堆 buzzword/比喻，指令里不写 please，也绝不写 simply/easy/quickly；不预告未来，不连续句同开头；链接文字说出目的地（页面标题或短描述），绝不用 “click here”，优先给页面内一句上下文而不是外链；标题承载要点而非只给主题（“Pick the mode first” 而非 “Modes”），sentence case，任务标题是裸动词短语、概念标题是名词短语，一页一个 h1、不跳级；序列用编号列表、其余用 bullet，列表前用完整句引入，条目平行；代码用等宽、UI 元素加粗、用序列逗号、不用 etc. 并说明列表不完整。

**第三层：一次只承载一条（STE）**：一句一指令；指令句 >约 20 词、其他句 >约 25 词就拆；警告/条件放在它守护的步骤之前；保留 the/a（“Remove backup file” 有两种读法，“Remove the backup file” 只有一种）；每个词一个含义一个职责并保持；“check” 若表示 inspect 就不要又表示 restrain；每个动作固定一个词（start 不要一处 start 一处 initiate）；过程写直接命令，不写叙述、不用被动；尽量避免 -ing 词（承担太多语法角色、滋生误读）。

**第四层：不留两种读法（Global English）**：only/not 紧贴其修饰词（“only fails on growth” vs “fails only on growth”）；拆长名词串（“the proto import budget check script”→“the script that checks the proto-import budget”）；每个 it/they/this 明确指向一个物，拿不准就重复名词，不用 this/which 指整句；不丢动词；保留结构小词（“Ensure that the switch is off” 保留 that 只留一种解析）；系列中重复冠词防误读；说明 and/or 连接什么（Both…and、either…or、if…then 是免费消歧器）；用句号不用分号，em dash 改新句；括号内容要么是完整语法单位要么独立成句，不用 “(s)” 造复数；不用斜杠（写 “a, b, or both”）；每样东西全篇一个名字（同一物不要又叫 gate 又叫 ratchet 又叫 budget check；未改的句子不要为了改写而改写）；不用习语、口语、拉丁缩写、隐喻（非母语读者、译者、agent 都最擅长平实结构）。

**节奏与 repo 特性**：故意混合句长（短句落点、长句带条件/后果的事实），一个想法一句不等于一个长度；在模式允许处要有观点（explanation 权衡取舍要说自己的看法，reference 保持 dry）；具体胜过 sterile（不是 “schema changes can cause issues” 而是 “a column rename fails the build”）；**codebase 就是词表**（写真实符号/文件/flag/命令名，不写同义词或描述）；不发明行话，用开发者会说出声的词；命名模式可以，但首次出现要说明含义。**PR 描述与 commit message 也是写作**：除 Diátaxis 外所有层都适用；PR 体是 reviewer 一分钟内读完的 briefing；不要贴 swarm log、SHA 清单、指标表，改为链接。**产品 UI 字符串不是文档**，用产品自己的 copy 指南。代码片段用 tab 缩进；写真实路径与符号；每个计数/树形声明在落地的 commit 上为真并附可重生成的命令。

**工作示例（原文 before/after）**：before 用 “Configuration of … is performed via…”“Note that it's important to remember that…”“should only be done when…”；after 改为 `budget.mjs` 读 `budget.json` 并数 import proto 的文件、超预算 CI 失败、`--write` 只用于降低预算。

**成立条件**：有明确的读者与文档用途；作者能选一个模式；可引用真实符号。

**失败模式/反例**：一个文档混多模式；PR 体贴日志/SHA/表格而不 link；用 “should be done” 指令；条件放在步骤后；标题只给主题；不动事实地机械改写导致机器味（违反元规则 ③）；产品 UI 文案混用文档规范；计数声明随 commit 过期而无重生成命令。

### 3) 判断位点与 Profile 调用

| 位点 | 专业 concern | 何时调用 | 由哪个 Profile 提议 |
| --- | --- | --- | --- |
| A/Voice：与人沟通的文档/说明 | 可理解性 | 写 RFC/readme/说明/PR 描述 | `intent-voice` |
| B：行为约定文档的准确性 | 行为 | 写接受条件/规格 | `behavior-domain` |
| Driver/meta：方法库自身的文档质量 | 可维护性 | 新写/修改 methods/profiles | `driver` / 方法作者 |

### 4) 当前产品锚点、覆盖、缺口、为何值得吸收

- `docs/WORKFLOW-INTENT.md` §4：“必须翻译成可理解的行为、成本、风险或承诺”。
- `profiles/intent-voice.md` `## 关键问题`：“需要人类决定的是哪一个选择，用行为/成本/风险/承诺怎么表达才可理解？”
- `charters/README.md` `## Assembly`：展示了 package 的确定性文本顺序（消费者需要可读的说明）。
- `docs/absorption/2026-10-02/EXECUTION-PLAN.md`：“一条争议可独立”“不按每文件填长表；一组一份完整包”——本仓自身的写作规范需求。

具体缺口：

1. **产品没有文档模式选择**（tutorial/how-to/reference/explanation）：方法库与 Charter 是混模式文本，读者需要猜哪段是操作、哪段是解释、哪段是参考。
2. **没有“文档 vs 实现命名一致”的纪律**：codebase 是词表、写真实符号；产品文里已有“引用已接受对象”的要求但没有命名一致性检查。
3. **没有 PR/commit 的写作面**：产品有交付与证据纪律，但没有“PR 体是 briefing、不贴日志/清单/表格”的规则。
4. **没有读者消歧规则**（one instruction per sentence、条件前置、only/not 位置、代词指向、句号优先）：这对把方法正文翻译成中文同样适用，且能减少 Agent 误读（产品的方法正文由 agent 消费）。
5. **没有“文档计数/树声明必须可重生成”** 的证据纪律。

为何值得吸收：直接提升方法库被 agent 与人类正确消费的概率；四层规范都可文本化，且与 MG-1 互补（MG-1 清理 AI 痕迹，MG-2 决定结构与清晰度）。

### 5) 拟处置与载体

- 拟保留：三条元规则；Diátaxis 四模式与“不混模式”；Google style 的读者导向条目；STE 的“一句一指令/条件前置/保留冠词/一词一义”；Global English 的消歧条目；节奏与“具体胜过 sterile”；codebase 是词表；PR/commit 适用性；计数声明可重生成。
- 拟改变：把英文语言特定条目（serial comma、Latin 缩写、斜杠、the/a）按中文适用性重写（中文保留“量词/代词指向/条件前置/一句一指令/不混模式/不滥用破折号与分号”等）；来源引用（diataxis.fr 等）保留为来源说明，正文自包含；去 `/technical-writing` 命令名。
- 拟删除：与产品无关的外部规范细节（STE 编号规则、字典）；UI 文案指南（产品不适用）。
- 载体：方案 1（推荐）新增 `methods/guide-technical-writing.md`（可作 `guide-plain-language.md` 的第二层，或独立），在 `methods/README.md` 按需表加一行；方案 2 把本组并入 MG-1 的写作 guide（本包倾向合并为一份 `guide-language-and-writing.md`，两层：平实重述 + 文档分层）。理由：同属“给人读的文本质量”，拆分会产生两个交叉检查清单。
- 与 a4 的分工：`opening-a-pr`/`shipping` 的交付流程与 commit 规范实现归 a4；本组只保留写作质量判据。

**平台耦合/依赖**：零平台耦合。

### 6) 正文草稿与验证方案

```
技术写作检查（草稿，压缩版）
先选模式：教学（tutorial）/任务（how-to）/查阅（reference）/解释（explanation）。一个文档一个模式，不混；混了就拆开并链接。
句子：you + 现在时；条件在指令前；常见在前；指令命令式；不用 should be done；不写 simply/easy/quickly。
一次一条：一句一指令；>20/25 词拆；保留冠词；一词一义，一动作一名；避免 -ing 堆叠。
消歧：only/not 贴身；拆长名词串；代词指向明确；不丢动词；and/or 说明连接什么；句号优先，破折号改新句。
命名：用 codebase 的真实符号；每个东西全篇一个名字；不发明行话。
节奏：混合句长；explanation 允许观点，reference 保持 dry；具体有数而非空泛（“列改名会让构建失败”）。
PR/commit：适用除 Diátaxis 外全部层；PR 体是 briefing，链接日志/清单/表格而不是粘贴。
元规则：规则让句子更糟就换一种写法或不动。
```

验证方案（未执行）：用一份本仓已有文档做前后对照，检查 (a) 是否单一模式、混模式处是否被拆；(b) 条件是否前置、是否有 “should be done” 类被动；(c) 词表命名是否与代码一致；(d) PR 体规则是否可操作。反例：机械重写导致机器味（元规则触发）、把 reference 写成 tutorial。边界：不要求所有文档重写；不改变内容事实。

---

## MG-3 注释纪律与代码 slop 清理（B/E 交界）

### 1) 机制与触发情境；源锚点与已读/尚缺

| 源锚点 | 已读 | 尚缺 |
| --- | --- | --- |
| `pstack/skills/no-comments/SKILL.md`（全文） | 全文 | 无 |
| `pstack/agents/comment-sicko.md`（全文，kept list 逐字） | 全文 | 无 |
| `cursor-team-kit/skills/deslop/SKILL.md`（全文） | 全文 | 无 |
| `pstack/docs/guide/05-build-and-clean.md` 的 no-comments/deslop 段 | 已读（包 3） | 无 |
| `pstack/skills/poteto-mode/SKILL.md` `## Comments` 段 | 已读（包 1） | 无 |

触发情境：diff/分支上有 AI 生成或历史注释、叙述注释、workaround 布道、防御性死重、cast 绕类型；评审前要清理 diff；注释声称约束（“do not remove”）需要决定去留。

### 2) 操作、成立条件、失败模式、反例/例子

**Comment Sicko keep list（逐字，唯一 leash）**：① 法律/许可头；② 由我们无法重塑的外部依赖、平台、厂商或协议强制的非显然行为（**我们自家代码里的 surprise 是肉，杀掉并给该符号标 `MUST KILL`**，用 rename/extract/type/rearchitecture 让行为自明而无需散文）；③ `// prettier-ignore`；lint suppression 只在规则本身有缺陷/迂腐/纯风格时存活；④ 定义 public API 契约的 doc comment；⑤ 解释代码无法表达之约束的 issue/RFC 链接。**不确定 keep 条件是否适用时，注释死掉。** 其余都是肉。

**suppression 规则**：`eslint-disable`、`@ts-ignore`、`@ts-expect-error` 之类臭；查该规则：若它抓真 bug 或保护正确性/安全，则杀掉 suppression 并把精确的 guilty symbol 标 `MUST KILL`。`IMPORTANT`、`do not remove`、`too risky`、`fine for now`、长辩护是 scent 不是 conviction；判断前读附近代码；若其主张在附近不明显，跑 `/how`、`/why` 或两者查命名符号或调用；只有“foreign keep-list gotcha 今天在 live path 上被证明为真”才能存活；我们自家代码的 surprise 一律死。**没有已证明 keep-list 例外作背书的长辩护就是 confession**；杀掉，绝不把肉润色成更短的口供；标精确符号 `MUST KILL`；kill 到此为止，不改代码。**每个 flag 必须指出 scope 内代码并说真话，不发明；只碰注释与标记 refactor 目标，绝不写应用代码。** 报告：touched files、deletion count、`MUST KILL` flags 一行一个、skips。

**no-comments 主流程（6 步，操作要点）**：范围=调用者的文件/diff，否则当前 diff 对 base（默认 main，含工作树）；spawn Comment Sicko（不重述其规则）；检查其报告与 diff——拒绝：应用代码编辑、scope escape、被例外保护的删除、误述 `MUST KILL` 理由、把有意保留的代码当有罪；我们自家代码上的 reshape flags 保持可行动，不恢复这些注释；**keep 只有在“证明它关于我们无法改变的东西”时才存活**；审计遗漏的 scoped lint 与 TS suppression；correctness/safety suppression 保持可行动的 `MUST KILL`；恢复删除只在有精确例外与 scoped 证据时；对薄的 `IMPORTANT`/`do not remove` kill 或 keep，接受前跑 `/how` 或 `/why`；kill 含糊时不恢复；keep 被反驳或仍含糊时删除；被拒报告 revert 重跑一次并点名失败，第二次拒绝就报 open 并 fail `/no-comments`。修复：trivial flag 直接删死路径/去参数/用真 API；任何修复需要形状就跑一次 `/architect`（只到 sketch，architect 定形状，第 4 步实现）；第 4 步做 scope 内最小根因修复，移除每个 named workaround；root cause 出 scope 就落最小 in-scope 修复并报其余 open；**fix-root-causes 与 redesign-from-first-principles 只指导 intent，都不授权扩大围栏或修围栏外实例；绝不 bolt symptom guard**。约束注释（`do not remove`/`do not change wording`/`talk to X before changing`）：留下关于我们无法改变之事的 keep；提供最便宜的 in-scope type/runtime/test/CI lint；**交互式说明要等用户批准；无人值守与 eval 需要 caller 预批准**；批准则先 encode 再删，否则删掉并报 constraint open 与 sketch out-of-scope work。报告：deletion count、restored comments、reruns、architect sketch、fixes、encoding offers、encodings、unenforced constraints、other open work。

**deslop（代码 slop 清理，焦点区）**：不必要的注释或与本地风格不一致的注释；trusted code path 上不正常的防御检查或 try/catch；仅用于绕类型问题的 `any` cast；应改早返回的深嵌套；其他与文件/周边 codebase 不一致的模式。Guardrails：行为不变除非修明显 bug；偏好最小聚焦编辑而非大重写；最终总结 1–3 句。

**成立条件**：有 scoped diff/文件；有能跑 `/how`/`/why` 的能力（用于核实 keep 主张）；约束 encode 的通道存在（type/test/lint）。

**失败模式/反例**：把注释交给作者自己清（源文明确要 fresh eyes、非作者）；把 claimed constraint 直接删而不先核实与给 encode 选项；允许应用代码编辑或 scope escape；把 `MUST KILL` 当成真的改代码指令；在无人值守时未经预批准 encode；用 symptom guard 代替根因修复；deslop 变成大重写。

### 3) 判断位点与 Profile 调用

| 位点 | 专业 concern | 何时调用 | 由哪个 Profile 提议 |
| --- | --- | --- | --- |
| B/E：代码可读性契约与交付质量 | 可维护性 | 评审前、提交前、diff 有 slop 时 | `implementation`（自清）与 `evidence-evaluation`（评审） |
| D：注释声称的约束如何编码 | 技术 | 约束注释需 type/test/lint 时 | `technical-planning`（a4 侧） |
| Driver：清理作为交付而非抛光 | 程序性 | closeout 前的 diff 卫生 | `driver` |

### 4) 当前产品锚点、覆盖、缺口、为何值得吸收

- `profiles/implementation.md` `## 常见误区`：“‘能改就改’：顺手重构、扩大改动面，把局部自由当成扩大授权的理由。”
- `profiles/implementation.md` `## 心智模型`：“实现是发现事实的地方…发现要记录，不能私下消化掉跨边界影响。”
- `methods/local-defect-feedback-loop.md` `## Limits`：“does not require a particular control skill, loop command, model, pull request, or change of module merely because a function boundary exists.”
- 包 1 MG-1 已记录 encode-lessons-in-structure（机械/结构优先于文本指令）。

具体缺口：

1. **没有注释的 keep/kill 判据**：产品没有“什么注释值得留下、什么必须变成代码结构”的规则；`implementation.md` 只讲不顺手重构，不讲注释处理。
2. **没有“约束注释 → type/test/lint 编码”的操作**：这与包 2 MG-3 的 encode-lessons 直接衔接，但产品无语境化流程（谁批准、无人值守怎办、encode 后删除）。
3. **没有“注释交非作者评审”的独立性规则**：与 `evidence-evaluation.md` 的“评价者不得是实现者”同源，但注释清理需要另一条具体路径。
4. **没有 suppression 的处理纪律**：`@ts-ignore`/`eslint-disable` 类 suppression 若护正确性/安全必须转成真修；产品无此判断。
5. **没有“清理是交付的一部分，不是事后抛光”的定位**：deslop 的焦点区与“不扩大改写面”的 guardrail 可直接用。

为何值得吸收：注释与 slop 是 agent 产出的高频噪声，直接影响 reviewer 与后续 agent 的读者负担；机制全为文本/流程，无平台耦合。

### 5) 拟处置与载体

- 拟保留：Comment Sicko keep list 五条与“不确定时死”；“我们自家代码的 surprise 没有 pass”；suppression 查规则后决定；约束注释 → 最便宜 encode + 批准流程 + encode 后删除；非作者新鲜眼睛；kill 只标记不写代码；deslop 焦点区与 guardrails；“清理不是可选抛光”。
- 拟改变：去 `Task`/`subagent_type`、`prettier-ignore`/`eslint-disable`/`@ts-*` 具体工具名为“格式化/lint/类型 suppression”；把 `/how`/`/why`/`architect` 命令名改为“核实符号能力/上游设计判断”；`MUST KILL` 改为产品词（如“需重构标记”）。
- 拟删除：Comment Sicko 的角色扮演语气文本（“Yes... Ha ha ha...”）不进产品；这是载体风格不是机制。
- 载体：方案 1（推荐）新增 `methods/guide-comment-and-diff-hygiene.md`，在 `methods/README.md` 按需表加一行并在 `profiles/implementation.md`/`evidence-evaluation.md` 按需入口指向；方案 2 并入包 2 MG-3 的 lesson promotion（代价：注释清理是独立触发——提交/评审前——与“重复纠正”触发不同）。本包倾向方案 1。
- 与 a4 的分工：具体 lint/类型/suppression 实现与 deslop 工具面归 a4；本组保留判断流程。

**平台耦合/依赖**：零平台耦合；encode 选项的真实可用性依赖新工程能力（type system/test/lint），属 a4/D。

### 6) 正文草稿与验证方案

```
注释与 diff 卫生（草稿）
keep 只剩：许可头；外部依赖/平台/协议强制的非显然行为（自家代码的 surprise 不算）；格式化/lint suppression 且规则本身有缺陷/纯风格；定义 public API 契约的 doc comment；解释代码无法表达之约束的 issue/RFC 链接。不确定就不留。
- 声称“don't remove / too risky / fine for now”的注释先核实（读邻近代码、查符号历史）；无已证例外则删除。
- 护正确性/安全的 suppression 转成真修，标出需重构符号；绝不写应用代码。
- 约束若真实：给最便宜的 in-scope 编码（类型/测试/lint/runtime check），人类批准后先编码再删注释；无人值守需预批准，否则删除并报 open。
- 清理由非作者执行；不越 scope；不做大重写；行为不变除非修明显 bug。
定位：清理是交付的一部分，不是事后抛光。
```

验证方案（未执行）：对一段真实 diff 跑注释清理，检查 (a) keep 是否只按五条存活；(b) 声称约束的注释是否得到 encode 选项而非直接删除；(c) suppression 是否被核查；(d) 是否有越 scope 或应用代码改动。反例：把作者自己的注释当 fresh eyes、把历史遗留 intentionally-kept 注释误杀且无证据。边界：不要求删除所有注释；encode 需要真实可用通道。

---

## MG-4 学习路径、回顾与个人工作风格（A/meta）

### 1) 机制与触发情境；源锚点与已读/尚缺

| 源锚点 | 已读 | 尚缺 |
| --- | --- | --- |
| `teaching/README.md`（全文） | 全文 | 无 |
| `teaching/skills/create-learning-path/SKILL.md`（全文） | 全文 | 无 |
| `teaching/skills/run-learning-retrospective/SKILL.md`（全文） | 全文 | 无 |
| `pstack/skills/automate-me/SKILL.md`（全文，7164B） | 全文 | 无 |
| `pstack/skills/workflow-from-chats/SKILL.md`（全文） | 包 2 MG-3 已读 | 无 |
| `pstack/skills/reflect/SKILL.md`（全文） | 包 2 MG-3 已读 | 无 |
| `teaching/plugin.json` | **未读** | 元数据 |

触发情境：多 session 培养某主题能力（create-learning-path）；完成里程碑后要数据驱动调整计划（run-learning-retrospective）；用户想把工作风格固化进 skill（automate-me：“automate me”“create/update/refresh my -mode skill”“turn/capture my preferences or working style into a skill”）。

### 2) 操作、成立条件、失败模式、反例/例子

**teaching/create-learning-path（原文 5 步）**：评估基线知识与目标结果 → 从基础到应用排序主题 → 定义里程碑项目与有时间盒的 checkpoint → 加 deliberate practice 练习与反馈标准 → 审查进度并调整节奏。工具：Ask user。Guardrails：里程碑在给定 schedule 内可达成；每个阶段含练习与反思；通过优先少量材料避免资源过载。输出：按周或按里程碑的计划、练习作业、进度回顾 rubric。

**teaching/run-learning-retrospective（原文 5 步）**：拿完成的工作对照目标结果 → 找出反复出现的 blocker 与弱概念 → 排优先级：强化什么 vs 推后什么 → 调整节奏与后续练习 → 设下一里程碑与可测 checkpoint。输出：进度回顾、更新后的计划、下一里程碑定义。

**automate-me（操作要点）**：输出一个 `<handle>-mode` skill，串起三件事：inline mining、作者的 skill-authoring 流程、unslop。
- 0 检查既有 skill：递归找 `.cursor/skills/**/*-mode/SKILL.md` 与 `~/.cursor/skills/*-mode/SKILL.md`（可能在个人分类目录 `.cursor/skills/<handle>/`）；存在则问更新（重复运行的默认）还是重开（罕见，先问 why）；更新模式只挖 skill 上次编辑以来的历史（`git log -1 --format=%cI <path>`）、只问“变了什么/缺什么”、就地编辑并**保留用户未否定的 section、按新证据修订、只对真正新增规则加新 section**。
- 1 挖历史：定位本 workspace 的 transcripts（**只用系统提示给该 workspace 的路径；不要 glob 跨 `~/.cursor/projects/*/`**）；多个并行 subagent 分片（如最近 2–4 周分 3 片）；每片返回带证据指针的简短结构化 pattern 列表；默认信号：response preferences（长度/语气/格式/“dumb it down”纠正）、delegation habits（subagent/模型/专门工作流/并行）、verification posture（什么算 done、单测 vs live repro、reviewer）、code and prose discipline（风格、引用的 principles、lint/format 工具）、process conventions（worktree、commit、PR、review/merge 工具）、meta preferences（中途修 skill、提议新 skill）；**跨片交叉验证**，2+ 片见过的 pattern 为高置信，孤立信号弱并通常丢弃。
- 2 直接问用户：用结构化多选而非让用户从零打字；1–2 个问题、每个 4–6 选项、category 问题 allow_multiple；先宽后窄；结构化轮之后一个自由文本问题捕漏；**不要一次丢 20 个问题**。
- 3 聚类：response style / autonomy / understand first / subagents / prose & code discipline / review and verify / process / skills（只取适用项）；以 poteto-mode 为形状参考但**不复制其内容**（“The user's rules are not the same as poteto-mode's.”）。
- 4 起草：用作者的 skill-authoring 流程；路径保留既有 mode 分类，新建用 `.cursor/skills/<handle>/<handle>-mode/SKILL.md` 或项目/个人默认；handle 用 first name 或标识；frontmatter description 触发于 `<name>`+`/<handle>-mode`+“work in their style”，**不要用 “write code”/“review PR” 之类泛词**；默认 `disable-model-invocation: true`，除非用户明确要每回合应用。
- 5 迭代 prose：对每一行走 unslop 与作者的写作指南；把草稿给用户并接受多轮反馈；**“A mode skill is not a manual.”**（大幅删减）。
- 6 落地：worktree off main；commit + PR；不直推 main。
- Guardrails：**不要 overfit 单次对话**（某偏好说过一次又被另一次反驳就是噪声；编码前要求多次出现）；不要 clever（复述他人 skill 内容、发明隐喻、给 agent 读者写“诗”是纯成本）；**引用而非内联**（用户依赖的其他 skill 用路径引用，不要粘贴摘录；维护在别处的 principle 文档同理）；**section 保持最小**（只有用户有特定非默认规则时才加 section；“Communicate clearly” 不是 section，“Short paragraphs. Tables when comparing options. Bullets only when items are genuinely parallel.” 是）；约定名保持通用（指令里用 “the user”/“the human” 而不是作者名）；**不要强求对称**（没有值得写下的 process 规则就整个跳过 Process section）。
- Evaluation：mode skill 是主观输出，作者的 test/iterate benchmark loop 不适用；与用户 vibe-check（读起来像不像他/漏了什么）再 ship；只有当触发准确率实际出问题时才跑 description-optimization。
- When not to use：任务特定 skill（不是工作约定）→ 只用作者的 skill-authoring，无需 mining；捕获单一窄工作流（如“我怎么写 commit message”）→ 是普通 skill 不是 mode skill。

**成立条件/失败模式**

- 学习路径：有明确主题与目标结果；有可安排的 schedule；有可反馈的练习。反例：里程碑不可达、只堆材料无练习/反思、资源过载。
- automate-me：有可读的 workspace 内 transcript；用户愿意结构化回答；有可落地的 skill 载体。失败模式：overfit 单次对话；复制 poteto-mode 内容；把其他 skill 内容内联；加“Communicate clearly”类空 section；强制对称；一次性偏好直接编码；跨 workspace 读 transcript。

### 3) 判断位点与 Profile 调用

| 位点 | 专业 concern | 何时调用 | 由哪个 Profile 提议 |
| --- | --- | --- | --- |
| A：能力建设与目标 | 目标/学习 | 长期能力培养 | `intent-voice`（A） |
| A/Voice：偏好固化与接受记录 | 偏好/沟通 | 反复纠正成模式、用户要求固化风格 | `intent-voice` + `driver`（bounded composition） |
| meta：经验编码 | 可维护性 | 同包 2 MG-3（lesson promotion） | `driver` |

### 4) 当前产品锚点、覆盖、缺口、为何值得吸收

- `profiles/intent-voice.md` `## 交接与召回`：“人类接受记录（决定、范围、条件）”。
- `profiles/intent-voice.md` `## 按需方法入口（候选）`：“人机读回方法：用自己的话复述理解，检查接受状态与适用条件。”“访谈/追问方法：目标、约束或价值冲突不清楚时使用。”
- `profiles/README.md` `## 组合说明`：“是否拆分按真实任务信号决定”。
- `docs/WORKFLOW-INTENT.md` §2：“经验按责任和问题挂载，控制注意力负担、传递失真与流程成本。”

已覆盖：人类接受记录；读写回方法入口（候选）；经验挂载原则。

具体缺口：

1. **没有“偏好提取与置信”纪律**：`intent-voice` 有“读回”，但没有“同一偏好说了一次又被反驳 → 不编码”的 overfit 判据与“2+ 片交叉验证”的置信规则（包 2 MG-3 从 workflow-from-chats 角度覆盖了偏好置信，本组的 automate-me 侧重落到 skill 载体的全过程）。
2. **没有“个人/团队工作风格如何固化”的流程**：产品有 Profiles 与方法，但没有“从会话挖出用户实际做法 → 结构化确认 → 起草 → 迭代 → 落地”的装配指南；Driver 的 bounded composition 只到“组装实例”。
3. **没有“引用而非内联 / section 最小 / 不要强求对称”的载体纪律**：产品方法库自身最需要这几条（避免把他人方法内容复制进 Profile）。
4. **学习路径本身与产品关系弱**：teaching 插件的两个 skill 只有 821/637 字节、5 步通用流程、无工程行为、无例子、无失败模式；除“里程碑要可达成、每阶段含练习与反思、优先少量材料、用完成工作对照目标结果、设可测 checkpoint”这些通用常识外，没有值得作为专业方法吸收的独特经验。
5. **产品没有“能力建设”责任**：A–F 与 Backbone 都不包含学习/训练责任；把 learning path 硬塞进 A 会扩大 A 的范围（A 已对齐“不替 Owner 创造目标”）。

为何值得吸收/不吸收：automate-me 的**偏好固化纪律**与包 2 MG-3 的 lesson promotion 互补，值得并入 A/Voice/Driver 的候选方法；teaching 插件内容薄且与产品责任边界不符，建议**暂缓/拒绝吸收**（若 gate 认为要吸收，最多作为 A 的“访谈/追问”例子，且必须明确不产生新责任节点）。

### 5) 拟处置与载体

- 拟保留（automate-me）：0 既有 skill 更新模式（只挖自上次编辑以来的历史、保留未否定 section、只新增真正新规则）；1 跨片交叉验证 + 2+ 片高置信；2 结构化提问优于让用户从零打字；3 聚类与“不复制来源内容”；4 触发描述要具体；5 多轮迭代 + “mode skill is not a manual”；guardrails：不过拟合、不 clever、引用而非内联、section 最小、命名通用、不强制对称；evaluation：主观输出不做 benchmark、vibe-check；when-not-to-use 边界。
- 拟改变：去 `.cursor/` 路径与 `Task`/`AskQuestion`/`create-skill`/`unslop` 命令名；把 `-mode` 概念改为“个人/团队工作风格预设”；transcript 路径改为“本 workspace 可读会话记录”；落地 PR/worktree 归 a4/Driver。
- 拟删除（teaching 插件）：Ask user tool 引用；若吸收只保留一条“能力建设不属于当前 A–F 责任；如需训练计划，按外部任务处理”的边界说明，避免产品扩权。
- 载体：方案 1（推荐）把 automate-me 纪律并入包 2 MG-3 的 `guide-lesson-promotion.md`（作为“从会话固定偏好到载体”的流程），不新建独立方法；teaching 不进入方法库，只在未读残余说明中记录拒绝理由。方案 2 独立成 `methods/guide-workstyle-capture.md`（代价：与 lesson promotion 触发重叠）。
- 与 Backbone 的一致性：不得引入“学习责任”或新决策节点；偏好固化只影响装配与写法，不产生权限。

**平台耦合/依赖**：transcript 读取与 skill 载体是宿主；纪律骨架零耦合。

### 6) 正文草稿与验证方案

```
偏好固化（automate-me 摘要，并入 lesson promotion）
1. 已有载体？更新优先于重开；只挖上次编辑以来的历史，保留未被否定的 section，只对真正新增规则加 section。
2. 证据：本 workspace 内可读记录，分片并行；跨片交叉，2+ 片为高置信；孤立信号弱，通常丢弃。
3. 直接问用户（结构化多选，先宽后窄，最多一两轮 + 一个自由文本）；不要一次丢二十问。
4. 聚类；不复制来源 skill 内容；触发描述具体（名字/命令/“用我的风格”），不用泛词。
5. 迭代 prose，多轮反馈；载体要操作化，不是手册。
6. 边界：不过拟合单次对话；引用而非内联；section 最小；命名通用；不强求对称；无规则就跳过该 section。
不进产品：学习路径/回顾（teaching 插件薄且超出 A–F 责任）。
```

验证方案（未执行）：用一个真实偏好场景（同一偏好出现两次以上且有一次反驳），检查流程是否 (a) 保留/修订/新增 section 正确；(b) 不把孤立信号编码；(c) 载体不内联其他方法内容。反例：把一次纠正写成规则；把来源 skill 内容整段粘贴进新载体。边界：学习/训练计划不进产品责任；偏好固化不产生权限与 gate。

---

## 8. 包级综合观察（供 gate，不是裁定）

1. 本包四组共同构成 A/Voice 的“输出面”：MG-1/2 管怎么说清、MG-3 管交付物里的注释与 diff 卫生、MG-4 管怎么把说清的方式固化。产品当前只有“可理解/可核对”的目标，没有输出面的操作。
2. 与包 2 MG-3 的重叠：automate-me 与 workflow-from-chats/reflect 共享“从会话提取偏好”的机制；建议 gate 合并为一份 lesson-prevention/lesson-promotion 支持文件，避免三份清单互相漂移。
3. teaching 插件的评估：内容薄（无例子、无失败模式、无工程行为）、且“学习责任”不在 A–F 与 Backbone 内；本包建议**不吸收**，若 Owner 未来要训练能力，应作为独立责任另议（不由此包创造）。
4. 写作规范的语言适配：MG-1/2 的规则源于英文；中文吸收时保留判断精神（行话/抽象隐喻/填充/过压缩/被动/消歧/模式不混），不逐条直译语法条目。
5. 风险：MG-3 的“注释 keep/kill”若被写成机械 gate（凡注释必删）会伤害真实 keep 用例；正文必须保留“不确定时核实、约束先 encode 再删”的顺序与批准边界。

## 9. 未读残余（本包未覆盖；不假装已评估）

- `teaching/.cursor-plugin/plugin.json`。
- `pstack/skills/poteto-mode/playbooks/opening-a-pr.md`（PR 描述/commit 规则）。
- `pstack/skills/poteto-mode/references/bugbot-triage.md` 剩余部分（包 3 MG-2 已读全文，本包未重读）。
- 其余同仓目录与包 1/2/3 的未读残余相同（thermos agents、orchestrate scripts/prompts（部分已由包 3 MG-5 补读）、advisor hooks、ralph-loop 余部、continual-learning、create-plugin、cursor-sdk、grok-voice、third_party、docs-canvas、pr-review-canvas、control-cli/control-ui、arena/swarm/SKILL 正文等）。

## 10. 包内自检（机械项，非专业裁定）

- 源 pin 与路径：均为 `ecc249f1e306fc64ddf83c7bed16cacf7c2239db` 下实际存在的路径；
- 未修改产品/他人文档/registry；未 commit；
- 每组含 6 项要求；所有验证方案标注未执行；源说法标注为原文描述；teaching 的“不吸收”建议附理由而非默认拒绝。
