# M4 · 载体台账独立复核（adversary）

- 评价人：`tpw-0930-adversary-b`（adversary）
- 被评价对象：`docs/history/derivation-0930/UPSTREAM-CARRIER-LEDGER-0930.md`
  （1752 行，md5 `7b33e0cf238cb0d8df175f71184fcc80`，作者 `tpw-0930-scout-b`）
- 姊妹：`docs/history/derivation-0930/UPSTREAM-INVENTORY-0930.md`
  （579 行，md5 `d866992fbe622896e989cfcd15030a61`）
- **候选不是我产出的，故我可裁决。** 但**本文件 §4 的三档判断是我提出的候选，不由我自裁**。
- **不裁决任何处置。** 吸收／拒绝／是否纳入清单，Owner 尚未给判据，本文件一个字不碰。
- **只读纪律**：全程未运行 `scripts/_render-lock.py`（它会写 lock）。
  所有枚举、哈希、git 调用均为我自己写的只读代码，输出只进本文件与终端。
  `upstreams.lock.yaml` 读后 sha256 = `a056b2ced80d3a6e6937f66b5b9e81457cb281bf26611d7d9389c4079fe4e282`，
  size 15451。本轮结束时复核该值未变。未改 scout 的两个文件、未改 registry/roles/skills/scripts，
  未 `git add` / `commit` / `tag`。

---

## 0. 结论一览

| 任务 | 判定 | 一句话 |
|---|---|---|
| 一 · `1080` 零省略零遗漏零抽样 | **PASS**（含一处**局部** FAIL） | 独立重算 = **1080，逐字相符**；1080 个载体**一个不缺**。但 §2 局部声明「全部 20 个文件」实为 21 |
| 一 · 三个沉默桶计数 | **PASS 3/3** | in-progress 9 包 / `.changeset` 13 文件 / evals 84 文件，全部属实 |
| 一 · 任务二 101/101 sha256 | **PASS** | 我自己重跑：101 一致、0 不一致、0 缺失 |
| 一 · 任务二 3/3 commit pin | **PASS** | 三个仓 HEAD 与锁内 pin 逐字一致 |
| 一 · 任务二 F6 结清 | **PASS** | 反向差集 52 + third_party 6 = 58，与姊妹文件 §4 自洽 |
| 一 · `pstack` 无自有 `.git` | **PASS**（附一条**更精确的表述**） | 属实，但 scout 描述的失效模式比实际**轻** |
| **二 · 438 / 476 / 92%** | **PASS** | 算术与「零方法正文」定性都成立 |
| 二 · 「高估 4.5 倍」 | **UNVERIFIED** | 全文只出现 1 次、**无推导**，我复现不出来。不记为 scout 缺陷，但它是会被引给 Owner 的数 |
| 二 · §5.2 逐包表 | **FAIL（差 1）** | `x` 包实为 **9** 个文件，§5.2 写 8；与 §5.1 的 37 自相矛盾 |
| 三 · 25 类三档初判 | **有条件成立** | 抽核 6 类：3 类理由可核但**数字错**，1 类**低估**，1 类**理由与事实不符**，1 类**未核**（记 UNVERIFIED） |

---

## 1. 任务一 · 机械性声明

### 1.1 `1080` 与「零省略、零遗漏、零抽样」→ **PASS**（§2 局部 FAIL）

**我独立重算的分母**（口径：全部文件，排除 `.git`，减去 `SKILL.md`）：

```
磁盘全部文件（排除 .git）              1239
  其中 SKILL.md                        159   （锁内 101 + 未锁 52 + third_party 6）
  载体（非 SKILL.md）                 1080   ← 与台账标题逐字相符
```

**台账侧**：从全文（反引号内 + 代码块裸行）抽出形如 `<repo>/<path>` 的 token，
去重后 **1101** 个。其中 21 个不是载体文件（是目录 token 与 §2 为说明构成而列出的
`SKILL.md`），故 **1080 个载体全部在台账中出现，差集为 0**。

> **载体有台账无 = 0。** 「零遗漏、零抽样」在**全局口径上成立**。

**§2 的局部声明 FAIL**：§2 写「该目录下**全部 20 个文件**（9 个 `SKILL.md` + 11 个载体）」，
并给出「载体构成：9 份 `agents/openai.yaml` + `README.md` + `pr/CREDITS.md`」= 11。
**磁盘实为 21 个文件（9 `SKILL.md` + 12 载体）**。差的那一个是：

```
mattpocock-skills/skills/in-progress/setup-ts-deep-modules/dependency-cruiser.config.cjs
```

**重要限定，避免夸大**：该文件**并未从台账里消失** —— 它出现在 §1 的
「`_root:cjs` — 根级 cjs」小节（台账第 680 行）。所以这是
**§2 自己那一句局部清点写错了**，不是全库遗漏。数量上 1/1080，
但 `dependency-cruiser` 是真实的架构约束工具，这份配置**不是零信息载体**，
所以它错在哪值得 Owner 知道：漏掉它的恰好是 Owner 点名的那个沉默桶。

### 1.2 三个沉默桶 → **PASS 3/3**

| 桶 | scout 声明 | 我的独立实测 | 判定 |
|---|---|---|---|
| `in-progress` | 9 | 9 个包目录 / 21 个文件 | **PASS**（包数对；文件数见 1.1） |
| `.changeset` | 13 | 13 个文件，13 条全列出 | **PASS** |
| `evals` | 84 | 84 个文件，全部在 addyosmani | **PASS** |

- `.changeset` 声称「其中 6 份直接记录 skill 判据改动」，我逐个核对那 6 个文件名
  （`retro-deterministic-checks`、`grilling-add-hr-between-questions`、
  `grilling-remove-em-dashes`、`remove-em-dashes-repo-wide`、
  `user-invoked-skill-invocation`、`skill-tool-invocation-terminology`）**全部存在**。
- evals：我一度测到 86，**是我的过滤器问题，不是 scout 的**。
  多出的 2 个是 `addyosmani-agent-skills/scripts/run-evals.js` 与 `run-evals-test.js`
  —— 名字里带 "evals" 但不在 `evals/` 目录下，属 `scripts/` 类，**不该算进 evals 桶**。
  scout 的 84 **是对的**。

### 1.3 任务二 · 锁文件只读核对 → **PASS 全部**

我自己写的只读等价代码（未调用 `_render-lock.py`）：

**逐 skill sha256**：锁内 `skills` 段 101 条，哈希记录长度实测 **16 个十六进制字符（前缀，非全 64 位）**。

```
一致 101 / 不一致 0 / 文件不存在 0
```

**逐仓 commit pin vs 实际 HEAD**：

| 锁内条目 | pin | 实测 HEAD | 判定 |
|---|---|---|---|
| `addy` | `2686b620fc1fed2e8f60c704839c766b8594c6b6` | 同 | **一致** |
| `matt` | `c55ee46073ed923f86ce59a5eb3b6d895095d1b7` | 同 | **一致** |
| `pstack` | `ecc249f1e306fc64ddf83c7bed16cacf7c2239db` | `upstreams/cursor-plugins` HEAD = `ecc249f1e306…` | **一致（经父仓解析）** |

**反向差集（复现枚举逻辑，只读）**：

```
磁盘 SKILL.md（排除 .git / third_party） 153   锁内 101   交集 101
磁盘有锁无 52      锁有磁盘无 0
52 + third_party 6 = 58
```

**58 与姊妹文件 §4「58 个不在锁里的 `SKILL.md`」逐字自洽。** F6 由
`UNVERIFIED` 结清为「已排除脱节」**成立**。

### 1.4 `pstack` 无自有 `.git` → **PASS**，但真实危害比 scout 写的更大

**事实成立**，实测：

```
upstreams/cursor-plugins/pstack/.git            不存在
upstreams/addyosmani-agent-skills/.git          存在
upstreams/cursor-plugins/.git                   存在
upstreams/mattpocock-skills/.git                存在
```

`pstack` 确为 `cursor-plugins` 的子目录，pin 指向父仓 HEAD `ecc249f1e306…`，属实。

**但 scout 描述的失效模式偏轻。** 派工与我核实的表述是
「任何以仓目录为单位直接 `rev-parse` 的清点方式都会**误判为「无法比对」**」。
实测：

```
$ git -C upstreams/cursor-plugins/pstack rev-parse HEAD
ecc249f1e306fc64ddf83c7bed16cacf7c2239db
```

**它不报错。它静默返回父仓的 HEAD。**

⇒ 真实危害不是「大声失败、无法比对」，而是
**一个子目录单位会静默继承父仓 commit，从而拿到一个「看起来合理但归属错误」的 pin**。
本例恰好正确（pstack 确实处于 `ecc249f1e306`），但这个「恰好」正是问题：
**父仓解析必须是一次被显式记录的决定，不能是一次碰巧对得上的默认行为。**
换成「子目录相对父仓已被改动」或「该路径其实是独立 worktree」两种情形，
同一个命令会给出**貌似有效、实则错误**的 pin —— 那比报错难发现得多。
**建议把这一条写进清点口径**：子目录单位必须记录「解析到哪个仓的哪个 commit」，
而不是只记一个 commit 串。

---

## 2. 任务二 · 那个会改写分母的数字（本轮最关键）

### 2.1 `438` / `476` / `92%` → **PASS**

我独立重算 `cursor-plugins/third_party/`：

```
包目录数        79
文件总数       482      （scout 亦称 482）
SKILL.md        6
非 SKILL.md    476      ← 「载体」口径
```

**构成**（按 basename 统计全部 482）：
`README.md 79` + `plugin.json 79` + `mcp.json 79` + `LICENSE 79` + `CHANGELOG.md 79`
+ `logo.png 62` + `logo.svg 17`（= 79 个 logo）+ `SKILL.md 6` + `shopify.mdc 1` + `pricing.md 1`
= **474 骨架 + 8 非骨架 = 482** ✓

**纯骨架包 = 73 个，每个恰好 6 个文件**（我逐包验证：文件数集合 = `{6}`，无例外）
⇒ **73 × 6 = 438** ✓ **`438 / 476 = 92.0%`** ✓

**「零方法正文」这一定性我做了内容抽检，成立**：
- `mcp.json` 每个 **8 行**，内容就是一个 MCP server 的 type + url（如
  `{"mcpServers":{"ahrefs":{"type":"http","url":"https://api.ahrefs.com/mcp/mcp"}}}`）—— 确为绑定清单。
- `README.md` 39–95 行（中位 61），我读了最长的两个：
  `posthog-mcp`（77 行）、`salesforce`（95 行）—— 内容是「这个 SaaS 是什么 +
  怎么装 + 它能干什么」，**没有一条是工程方法/流程/判据**。
- `CHANGELOG.md` 8–24 行（中位 9），版本说明。
- 补充一条 scout 没提的事实：73 份 README **内容两两不同（73/73 唯一）**，
  所以它们**不是同一份模板的复制**。这不影响「零方法正文」的结论，
  但影响 Owner 读法 —— 它们**不是零信息，是零「方法」**。

### 2.2 `x` 包计数差 1 → **FAIL**

scout §5.2 逐包表写 `x | 8`。实测 `x` 包 **9** 个文件：

```
.cursor-plugin/plugin.json, CHANGELOG.md, LICENSE, README.md,
assets/logo.svg, mcp.json,
skills/x-api-mcp-guide/SKILL.md,
skills/x-api-mcp-guide/references/pricing.md,
skills/x-chat/SKILL.md
```

⇒ §5.2 的列相加 = 7+7+7+8+7 = **36**，而 §5.1 的「带 SKILL.md 5 包 / **37** 文件」
**是对的**（7+7+7+9+7 = 37）。**同一份文件里两张表对同一批包给出不同总数。**
§5.1 的 37 与 438 + 37 + 7 = 482 三者自洽，所以错的是 §5.2 那一格。
量级是 1，但性质是**同一含义在两处各自设值**。

### 2.3 「高估 4.5 倍」→ **UNVERIFIED**，并附可推导的正确口径

全文 `grep -n "4\.5"` **只命中第 923 行一处，无任何推导过程**。
我尝试了多种口径组合，**都复现不出 4.5**（见下表）。

按纪律：**我复现不出来 ⇒ 记 `UNVERIFIED`，不记为 scout 的缺陷。**
但它是一个**写在「理由一」里、会被直接引给 Owner 的数**，所以我必须把可推导的口径交出来：

| 口径 | 算式 | 结果 |
|---|---|---|
| 台账总数 | — | **1080** |
| `third_party` 占台账 | 476 / 1080 | **44.1%** |
| 476 中来自 73 纯骨架包 | 438 / 476 | **92.0%**（scout 的数，成立） |
| **476 中真正含方法正文的** | `pricing.md` + `shopify.mdc` = **2** | 零方法 = **474 / 476 = 99.6%** |
| 剥掉 438 后的台账 | 1080 → 642 | 膨胀 **1.68×** |
| 剥掉全部 476 后的台账 | 1080 → 604 | 膨胀 **1.79×** |
| 剥掉全部 474 零方法载体 | 1080 → 606 | 膨胀 **1.78×** |
| `third_party` 内部比值 | 476 : 2 | **238×** |
| 包级比值 | 79 : 5 | **15.8×** |

**⇒ 没有任何一个自然口径等于 4.5。**
它在 `third_party` 内部口径下（238×）**严重低估**，
在整册口径下（1.79×）**高估约 2.5 倍**。

### 2.4 这对 Owner 的直接含义

派工说这个分母是 **Owner 第 3 条的直接输入，数字错了会让 Owner 按错误规模排优先级**。
那么可以确定的与不能确定的分别是：

**可以确定（我已实测，可直接引用）：**
1. `1080` 这个总数**准确**，没有虚报。
2. `third_party` 一个目录就占了 **44.1%**。
3. **但它的 99.6%（474/476）不含任何方法正文** —— 比 scout 自己说的 92% 更极端
   （因为 5 个带正文的包另外还贡献了 30 个骨架文件，同样零方法）。
4. **真正含方法正文的 `third_party` 载体只有 2 个文件**：
   `x/skills/x-api-mcp-guide/references/pricing.md` 与 `shopify-store/rules/shopify.mdc`。
5. 因此 **整册 1080 的「方法来源」分母应当按 604–642 计，而不是 1080**，
   膨胀 **1.68–1.79 倍**，**不是 4.5 倍**。

**不能确定（交给 Owner，本文件不裁）：**
- 这 474 个该整体排除，还是保留为「已知且已排除的库存」——
  scout §5.3 给了建议，**那是建议不是裁决，我按纪律不接**。
- 本库域将来会不会扩到非工程工作流（scout 已把这条反方事实写明）。

**⇒ 给 Owner 的一句话**：*按 1080 排优先级会把 44% 的注意力放在 2 个文件上；
真实待判的规模是 604–642，其中 `references`(56)、`playbooks`(23)、
`agents/` 真人格定义(17)、`.changeset`(13) 是 method-bearing 密度最高的几类。*

---

## 3. 任务三 · 25 类三档初判

**口径声明**：初判本身是 scout 的候选，**理由与数字可否核由我核，档位由 Owner 裁**。
下表只对我**实际抽核**的 6 类给判定；未抽的类**不评**。

| 类 | 声明 | 初判 | 我的核验 | 判定 |
|---|---|---|---|---|
| `references/` | 56 · 高 | 「56 份全是判据/清单/模板类正文」 | 计数 **56 PASS**（第 57 个是 `third_party/x/.../references/pricing.md`，归 §5，正确） | **可核，理由成立** |
| `playbooks/` | 23 · 高 | 「可直接对照本库 phase 的成文流程剧本」 | **我未独立重数 23** | **UNVERIFIED**（我没查，不记缺陷） |
| `agents/` | 55 · 中 | 「**39** 份 openai.yaml + **16** 份真人格定义」 | 55 **PASS**；拆分实测 **38 / 17** | **数字 FAIL**，结论不受影响 |
| `commands/` | 27 · 中 | 「9 条命令 × 3 种 harness」 | **9×3=27 PASS** | **可核**；但「同一套」是 8/9（见下） |
| `hooks/` | 20 · 中 | 「20 份是运行时钩子实现（**sh/ts/json**）」 | 20 PASS；扩展名实测 **md 2 / sh 14 / json 3 / ts 1** | **理由与事实不符 + 疑似低估** |
| `evals/` | 84 · 高 | 「84 份含 **27** 个 case 定义 + **4** 组负例 grader」 | 84 PASS；cases 实为 **25**，plugin 场景实为 **3 组** | **数字 FAIL**，且漏掉主体成分 |

### 3.1 `agents/` 55：中（拆分 38/17，非 39/16）

实测 `agents/` 共 55 个文件：**38 份 `agents/openai.yaml`**，**17 份真人格 `.md`**
（`code-reviewer` / `security-auditor` / `test-engineer` / `web-performance-auditor` /
`advisor-subagent` / 4 份 `agent-compatibility` reviewer / `agents-memory-updater` /
`plugin-architect` / `ci-watcher` / 2 份 thermo / `comment-sicko` / `poteto-agent`）。

**总数对，拆分两半各差 1。** 「多数是低价值模型映射配置」这个结论不受影响。

### 3.2 `commands/` 27：中（成立，但「同一套」是 8/9）

三处各 9 个，**27 = 9×3 成立**。但命令名不完全对应：
`.claude/commands/` 是 `plan`，另两处是 `planning`。其余 8 个同名。
**「同一套命令的重复落地」严格说是 8/9，不是 9/9。** 属措辞，不影响档位。

### 3.3 `hooks/` 20：中 —— **理由与事实不符，且这 2 份疑似被低估**

实测扩展名：**`md` 2 / `sh` 14 / `json` 3 / `ts` 1**。
理由里的「（sh/ts/json）」**漏掉了 2 份 `.md`**，而这 2 份不是边角料：

- **`hooks/SDD-CACHE.md`（167 行）** —— 我读了正文，它论证的是一条**再验证不变式**：
  「每次复用都向源站重新验证（`If-None-Match` / `If-Modified-Since`），
  **只有源站回 `304` 才算新鲜验证** —— 那是一次新鲜验证，不是记忆读取。」
  **这正是本库的核心命题**：缓存不得冒充验证、过期内容不得冒充现状。
  它与本库 `A8.verdict` 的三态纪律、「环境故障既不算 `PASS`」是**同一个论点的两种写法**。
- **`hooks/SIMPLIFY-IGNORE.md`（91 行）** —— 「块级保护」标注法：
  用 `simplify-ignore-start/end` 把不该被简化的代码圈起来，模型看不见就不会动。

**⇒ 档位判「中」我认为可接受；但判它的理由（「都是运行时钩子实现，本库不管 execution mechanics」）
在这 2 份文件上不成立** —— 它们是**散文判据**，不是运行时实现。
若按类聚合处置，这 2 份会被「本库不定义 execution mechanics」这句话**连带排除掉**，
而它们恰好是本类里最贴本库命题的两份。
**我的候选（未经独立复核）**：把 `hooks/` 拆成
`18 份运行时实现（方法价值 低／机制参照 高）` + `2 份 hook 契约正文（中）`，
或至少在类理由里点名这 2 份。

### 3.4 `evals/` 84：高 —— **两个数字都错，且理由漏掉了 57% 的内容**

实测 84 的真实构成：

```
README.md 1 + cases 25 + fixtures 48 + plugin 9 + skill-impact.md 1 = 84
```

- **「27 个 case 定义」→ 实为 25**（`evals/cases/*.json` 全部 25 个）。
- **「4 组「该不该开火」负例 grader」→ 实为 3 组场景**：
  `code-review-fires`（3 grader）、`code-review-stays-quiet-on-commit-message`（1）、
  `code-review-stays-quiet`（2），共 **6 份 grader + 3 份 prompt = 9**。
- **理由完全没有提到 `fixtures/` 的 48 个文件** —— 而那是本类**最大的一块（57%）**。

⇒ 「84 份含 27 个 case 定义 + 4 组负例 grader」这句话
**只覆盖了 84 里的 31 份，且其中两个数字都错**。

**档位判「高」我认为仍然成立**，但成立的理由要换：
支撑它的是 **25 份 case + 6 份 grader 组成的「该开火／不该开火」可执行评测结构**
（本库确实没有任何 skill 触发判据的可执行评测，这一点 scout 说对了），
**不是** 84 这个数。48 份 fixture 是评测输入，与 case 配对才有意义，
单独看价值低 —— **把它们和 case 分开计数，比笼统说「84 份」更能说明价值在哪里。**

### 3.5 有没有被判「低」却其实含判据类正文的类？

我核了判「低」的两个主要类：

- **`third_party` 476 · 低** —— **「低」是对的**，474/476 零方法正文已实测。
  仅有的 2 份例外（`pricing.md` 是 API 定价表、`shopify.mdc` 是 Shopify 商店规则）
  **都不是面向「与工具无关的工程工作流」的判据**。
  **但请注意粒度副作用**：正因为 99.6% 是骨架，**这 2 份在类粒度上完全不可见**。
  scout 已在 §5.3 把它们作为反方事实写明，**处理是诚实的**。
- **`scripts/` 104 · 低（作为方法）/ 高（作为机制参照）** —— 双档写法与本库
  「Driver 停在逻辑编排层、不定义 execution mechanics」的定位自洽，**不构成低估**。

**其余判「低」的类体量小或为配置目录，未见判据正文。**
`references`(高)、`playbooks`(高)、`evals`(高)、`.changeset`(中) 的「高/中」与其内容密度相符。

### 3.6 一处结构性提示（非缺陷）

§1 的 13 个具名类 + `根级与配置类（合计 139 个）· 初判见各组` + `third_party 476` + `scripts 104`
= 500 + 476 + 104 = **1080** ✓（我已独立求和验证）。

其中 **139 个（12.9%）没有单一类级档位**，继承自各子组（台账已披露「初判见各组」）。
**这是可接受的披露方式**，不是缺陷；但 Owner 若要按档位排优先级，
**这 139 个需要按子组展开才有档位**，直接看类表会漏掉近 13%。

---

## 4. 我提出的三档判断（**候选，未经独立复核，不由我自裁**）

按 `AGENTS.md`「提出候选的人不得给这个候选下结论」，以下只给理由与依据，**不判定其成立**：

1. **`hooks/` 20 · 中** —— 建议拆为「18 份运行时实现（方法 低／机制参照 高）」
   与「2 份 hook 契约正文（中）」。依据：实测扩展名分布与
   `SDD-CACHE.md:1-15` 的再验证不变式原文。
2. **`evals/` 84 · 高** —— 建议理由改为按 `cases 25 + graders 6` 的可执行评测结构陈述，
   并把 `fixtures 48` 单列为「配对输入，单独价值低」。依据：§3.4 实测构成。
3. **`agents/` 55 · 中** —— 档位不变，建议把「39/16」改为「38/17」。
4. **`commands/` 27 · 中** —— 档位不变，建议把「9 条同一套」改为
   「9 条命令 × 3 harness，其中 8 条同名、1 条 `plan`/`planning` 不一致」。
5. **`playbooks/` 23 · 高** —— **我未独立重数，UNVERIFIED，不提档位意见。**
6. **类粒度建议** —— 处置若按类进行，`references`(56) 密度最高且被判「高」；
   而 `hooks/` 的 2 份判据正文在类粒度下会被「不管 execution mechanics」连带排除。
   **若 Owner 想避免这种连带排除，需要的是「类 + 例外」而不是「类」这一层粒度。**

---

## 5. 纪律自证

- 三态只用 `PASS` / `FAIL` / `UNVERIFIED`。
- 记 `UNVERIFIED` 而**未**记为 scout 缺陷的：「4.5 倍」的推导、
  `playbooks/` 的 23 我未独立重数、Owner 对 474 个骨架包的处置意向。
- 判 `FAIL` 的两处均给出可复算依据：
  §2.2（`x` 包实测 9 个文件，§5.2 写 8）、§3.4（cases 实测 25、grader 场景实测 3）、
  §1.1（`in-progress` 实测 21 个文件，§2 写 20）。**无一处凭印象。**
- **不裁决任何处置**：吸收／拒绝／是否纳入清单，本文件一个字未写。
- 全程只读；未运行 `_render-lock.py`；`upstreams.lock.yaml` 前后 sha256 一致；
  未改 scout 的两个文件；未改 `registry/roles/skills/scripts`；
  未 `git add` / `commit` / `tag`。
- §4 全部标注为我的候选，未经独立复核。
