# REPORT · 0929 impl-checkers（收口：上一批的报告 + Q2 + D2 升级 + C1 加固）

被审对象（我自己改的代码）：`12aecf1`（前一批，driver 代提交）→ `5a66660`（Q2 未门控清单，driver 代提交）→ `05a8b4a`（C1 判据加固，我提交）→ `6e69a5e`（C1 skip 文案补句，我提交）。
`HEAD=6e69a5e`，**无 tag**，`VERSION` 仍是 2.0.6（遵守「commit 但不要打 tag」）。
改动面：只动 `scripts/check-closure.py`、`scripts/check-consistency.py`（前一批在 `12aecf1` 里）；本轮新增的只有 `scripts/check-closure.py` 上三处：Q2 未门控清单、C1 判据加固、检查器 docstring 补 C21/C22 两行。`.pi/` 只写这份报告。

基线数字（全部实测，命令见 §5）：

| 环境 | closure | consistency | render |
|---|---|---|---|
| 工作树 `6e69a5e`（自己的 git、无 tag） | 20 / **1 FAIL** / 0 / 21（唯一红是 C1 的「没有 tag」，收口打 tag 即消） | 7 / 0 / 0 / 7 | 12/12 |
| 带 tag 的副本（tag 打在 HEAD 上） | 21 / 0 / 0 / 21 | 7 / 0 / 0 / 7 | — |
| `git archive` 导出（无 .git） | 20 / 0 / **1 SKIP** / 21，rc=0 | — | — |

上一轮的负对照台 22 条本轮扩到 **23 条，全过**（新增 A3：副本装在下游仓库里）；本轮另加 D2 升级、Q2 双向回归、三段记录三套。

---

## 0. 先纠正我自己上一轮的错

我上一轮的交接快照（`.pi/handoff/0929-impl-checkers.md` §3）里有一句结论不成立：「D2 注入只删 `roles/architect.md` 的教学，architect 拥有的技能仍教 scope，选 (a) 也不会红」。
**那不是「(a) 走不通」的证据，是注入不彻底**：architect 名下的技能还在教 `scope`。
本轮把注入做彻底（§3），结论才成立。这一条记在这里，因为它正是本库批评过的那种测量错误——
**注入没改到位，和「检查器抓不到」在输出上一模一样**。

---

## 1. 逐条判定

### C1 · 结构与版本单一来源 —— 加断言（SKIP 分支）＋本轮再加固

**理由**：round-3 §1 与 §6.7：无 `.git` 时判 FAIL，是把环境故障判成产品缺陷，违反硬边界 3。
**改动**：`check-closure.py:256-272`（判据）、`:294-297`（detail 消息）、`:298-299`（`skip=`）。
**本轮新发现并修掉的第二个假 FAIL**：副本装进下游仓库时，`rev-parse --git-dir` **成功**（找到外层的 `.git`），于是旧判据读的是**下游仓库的 HEAD 与 tag**，拿本库的 `VERSION` 去对一个不相干的 commit，报「当前 commit 上没有 tag」。
这正是 C1 三态分支要治的假话换了个入口。判据改为 **git 顶层必须等于 ROOT 自己**：

```python
probe = subprocess.run(["git", "rev-parse", "--show-toplevel"], ..., cwd=str(ROOT))
git_meta = bool(probe.returncode == 0 and top and Path(top).resolve() == ROOT.resolve())
```

**自测（四态，三段记录见 §4）**：
- 工作树：`[FAIL] C1 … ↳ 当前 commit 上没有 tag`，rc=1 —— 真纪律，保留。
- `git archive`：`[SKIP] C1 …；无本库自己的 git 元数据（如 git archive 导出，或副本装在下游仓库里），未核对 VERSION 与 release tag 的对齐`，rc=0。
- 副本装在 `git init` 过的下游仓库里：同样 `[SKIP]`，**不再出现「当前 commit 上没有 tag」**。
- 带 tag 副本：`[PASS] C1`。

**误报排查**：有 tag 但 tag 名不含语义化版本 → 仍 FAIL（真断言）；下游副本外层即使有 `v2.0.6` tag 也不会被当成本库的 tag（顶层不符即 SKIP）。

**新假设**：`show-toplevel == ROOT`（经 `resolve()` 比较）是「本库自己的 git 元数据」的判据；worktree / submodule 形式（`ROOT/.git` 是文件）同样满足。

### C9 · 来源声明与锁文件一致（有实物时校验内容）—— 改名 + 两档输出

**理由**：round-3 §3 B1、§6.2、§5(3)：旧名字承诺「锁 + 实物对照」，而实物对照整段挂在 `if upstreams/` 里，下游进不去；修法降了能力却没把缩小量说出口。
**改动**：`:570-574`（改名与边界注释）、`:580-582`（`has_upstreams` / `pin_unchecked`）、`:583-612`（sha256 + 可信 git 判据）、`:621-642`（四支输出：FAIL 优先 / 锁文件档 / 实物不完整档 / 全核档）。
**自测**：

| 场景 | 输出（节选） |
|---|---|
| 无 `upstreams/` | `PASS（锁文件核对）…未发现 upstreams/，未做上游实物 sha256/pin 对照；不证明锁文件与真实上游一致。` |
| 有 `upstreams/`，全核过 | `PASS（锁文件＋实物核对）…上游文件 sha256 与 3 仓 pin 均与锁文件一致。` |
| 有 `upstreams/`，篡改锁 sha256 | `[FAIL]` + `addy:api-and-interface-design 的内容漂移…` |
| 有 `upstreams/`，仓的 git 元数据不可信 | `[SKIP]` + `未核 pin：上游 pstack 没有可信的 git 元数据…` |

**误报排查**：锁文件档的 PASS 不会被读成「与真实上游一致」（detail 自带这句话）；`lock.repos` 为空 → 记入 `pin_unchecked`（不冒充核过）；真漂移优先于任何 SKIP 分支。
**新假设**：「可信 git」= 解析出的 `show-toplevel` 落在 `ROOT/upstreams` 之内（把上游子目录单独拷进别的 git 检出，不会把外层仓库当上游 pin——B4 反例）；上游以软链指向本库之外的克隆时，一律判「没有可信 git 元数据」→ SKIP（fail-closed，见 §7 观察 3）。

### C12 · 无吸收来源技能显式标注 —— 改名 + 与 C20 交叉对账

**理由**：round-3 §6.5：同一个库里「原创」有两个意思（`origin: library` vs 来源段「本库原创」），C12 报「3 个原创」、C20 报「0 原创/3 借鉴」，两条都绿。
**改动**：`:726-729`（改名与计数说明）、`:982-989`（C20 加交叉断言）、`:1013-1017`（C20 detail 写明对账）。
**自测**：负对照 D1「把 tdd 的 registry 标成 `origin: library`（正文是吸收形态）」→ C20 红，报「正文说吸收、注册表说库内」。
**误报排查**：借鉴 / 纯原创两种非吸收形态标 `origin: library` 合法；吸收形态不写 `origin` 合法；只有「正文吸收 + registry library」这一种交叉点红。
**新假设**：对账等式 = C12 计数（`sources` 空）与 C20 的非吸收形态数（borrowed + original）；形态仍由来源段文本判定。

### C13 · 越权写由显式声明判定 —— 声明边界

**理由**：round-3 §6.3：B4 这类「角色正文与 registry 写权冲突」是被散文治好的，不是被检查器治好的；把中文语义映射变成断言没有确定性做法。
**改动**：`:763-767`（detail 末尾写「仅核阶段退出判据的 write:/verify:；不读取角色正文；正文与 registry 的写权冲突须人审」）。
**自测**：把 B4 原样注回去（verifier 正文改写权）→ 仍全绿。**这一条我没在本轮重跑**：它来自 round-3 复审的既有实验（`roles/verifier.md` 改回「由我更新 `A3.freshness`」、全套检查器零红），本轮 C13 只加了边界文字、判据一字未动，所以该实验结论继续成立。判据里的 `write:` 指向本阶段不产出的产物仍会红（原断言未减弱）。
**新假设**：C13 的覆盖面 = `phases[].exit_criteria` 的 `write:`/`verify:` 前缀，不含 notes 与正文。

### C15 · 被判据校验的字段 —— 两条边界 ＋ Q2 展示（判据不变）

**理由**：round-3 §6.6：`taught` 是子串搜索，分不清「提过」和「教过」；`role-contract-drift`（某一份改名、另一份仍列着）是合法变体，不是缺陷。
**改动**：`:845-856`（清单的推导与消费者说明）、`:857-866`（两条边界原文 + 未门控清单）。
**自测**：
- D2 升级（教学删净、只留诱饵）→ C15 仍 PASS，边界描述如实（§3）。
- Q2 双向回归：加 `fields` 项 → 未门控 21→22；加引用它的 `verify:` 判据 → 22→21 且清单消失该项；恢复基线 → 21 且逐项相同（§4）。
- 负对照 E1（只删角色文件教学）→ 仍 PASS，且打印证据说明技能仍教着（那是注入不彻底，已作废，见 §0）。

**误报排查**：字段在产出方名下任一份文件里出现即算「有人被要求填」；技能文件改名、角色文件仍列 → 不判缺陷；未门控字段计数与清单**永不**导致红。
**新假设**：见 §6。

### C20 · 技能来源段与注册表形态一致 —— 新增交叉断言

见 C12 条。改动 `:982-989`。自测：controls D1。误报排查同上。

### C21 · 原则来源与注册表完全相等 —— 新增断言（上一轮，`12aecf1`）

**理由**：round-3 §5 第 1 条：`provenance_policy.principles` 声称 `enforced`，而没有任何检查器读原则的「来源：」行（注入挂幽灵路径 / 整行删掉 → 双绿）。
**改动**：`:1019-1081`。断言：`principles/*.md` 每个 `## p-*` 段落里「来源：」行反查出的上游 id 集合必须与 `registry.sources` **完全相等**；拒绝幽灵路径、缺失、串线、重复；`本库原创` 分支必须给内部锚点。
**自测（我自己的 6 条负对照 + driver 独立复测 3 条）**：删「来源：」行→红；幽灵路径→红；**两条原则互换来源的串线→红**；同路径重复→红；纯原创无内部锚点→红；纯原创带锚点→绿（合法变体）。三段记录见 §4-A。
**误报排查**：多来源按集合比，顺序与写法不影响；`borrowed`（有路径 + 本库原创）仍走集合相等；registry 里 `sources` 为空的纯原创带任意内部锚点（`A*` / `@id` / 相对链接 / `p-*`）即合法。
**新假设**：内部锚点 = `A\d+`、`` `@id` ``、`](...)`、`p-*` 四类之一；`principles/` 的文件名与 `p-*` 段落标题不作为身份判据（只认 `## p-*` 标题）。

### C22 · 来源政策的 enforced_by 绑定真实载体 —— 新增元检查（上一轮，`12aecf1`）

**理由**：round-3 §5 第 2 条：`provenance_policy.current[*].status` 不可证伪——把它从 `UNVERIFIED` 翻成 `enforced`，没有任何检查器会红。
**改动**：`:156-159`（`CHECK_COVERS` 维护者登记）、`:1119-1181`。核四件事：① `enforced_by` 指向本次运行中注册的检查项；② 该检查在 `CHECK_COVERS` 里声明的类目与 policy 的类目一致；③ `enforced` 必须有可核粒度（level≠none），`UNVERIFIED` 必须带 owner 与 due；④ level 不超该类别的机械上限（skills=file、principles=clause，`known_limits` 的影子）。
**自测（我 7 条 + driver 5 条，全红）**：翻 enforced 无 `enforced_by`→红；`enforced_by` 指向不存在的检查→红；指向别类目的检查→红；UNVERIFIED 去掉 owner→红；level 抬到 paragraph→红；检查项没登记 `CHECK_COVERS`→红；`CHECK_COVERS` 类目改错→红。三段记录见 §4-B。
**误报排查**：UNVERIFIED 只要 owner 与 due 非空即合法；level 为 `none`/`file`/`clause` 且在 cap 内合法；policy 的其它字段（carrier/gap/known_limits 文本）不参与判定。
**新假设**：见 §6。**边界（写在输出里）**：`CHECK_COVERS` 是维护者的人工声明，C22 只证「声明的类目」与 policy 一致，不证检查实现真读了那些文件——后者靠 C20/C21 的注入反例。

### 三态 schema 对齐 + 死代码 —— 两个检查器同 schema（上一轮，`12aecf1`）

**理由**：round-3 §6.8：closure 报四栏、consistency 报三栏；`check-consistency.py:122` 有一行被下一行覆盖的死代码。
**改动**：`check-closure.py:162-186`；`check-consistency.py:103-137`（`Result` 支持 skip、`failed` 属性、四栏合计、删死代码）。
**自测**：G0 两行合计逐字同形：

```
合计: 21 项通过 / 0 项失败 / 0 项跳过 / 21 项检查     （closure，带 tag）
合计: 7 项通过 / 0 项失败 / 0 项跳过 / 7 项检查       （consistency）
```

**误报排查**：SKIP 不计入通过也不计入失败；当前 consistency 没有任何 SKIP 分支（参数为 schema 对齐保留，注释写明）。
**新假设**：两个检查器共享同一 summary schema；consistency 将来加 SKIP 分支时不需要再改格式。

### S4 · 硬规则引用可解析 —— 声明边界（上一轮，`12aecf1`）

**改动**：`check-consistency.py:398-406`。边界原文：S4 不读角色正文；「实现者」↔`builder`、「下结论」↔「给出裁决」是中文语义映射，没有确定性规则能变成断言（`s4-role-body`）。
**自测**：`.pi/injection/suite.py` 的 `s4-role-body` 记「设计内不报」并引用检查器输出里的边界原文；`role-contract-drift` 同理。两个台都钉在 `29a50e4`，对本轮只加边界文字的改动零覆盖（见 §5 末台外观察）。

---

## 2. 文档口径：哪些句子被我的改动弄假了、应该改成什么

这一节全部是**给 driver 的措辞**。以下行号是 `05a8b4a` 工作树上的行号。

### 2.1 `docs/coldstart.md`

**已假的三处**（你已改了上半段，这三处还在）：

1. `:57`「**`C7` 与 `C9` 照样是 `PASS`，不是 `SKIP`。**」——C9 现在**可以** SKIP：挂了 `upstreams/` 但某个仓的 git 元数据不可信时，pin 核不了。
2. `:67-68`「任何一种情况下这几项都必须是 `PASS`，不能是「没查就当过了」。」——SKIP 就是「这一层没查」，只是它被强制说出来。
3. `:70-72` 引用块「锁文件随包分发之后 `SKIP` 分支已经不可达……现已改成实况：**要么 `PASS`，要么红。**」——**SKIP 分支可达**（C1 无 git 元数据；C9 pin 不可核）。

**替换措辞（可直接覆盖 `:57-72`）**：

```markdown
**在下游，`C7`（上游处置完备）与 `C9`（来源声明与锁文件一致）正常情况下是 `PASS`。**
它们核对的 `upstreams/` 不随包分发，但 `upstreams.lock.yaml` 随包分发——
所以这两项在干净 clone 里直接对锁文件判，**实测全绿**。
有克隆的本库里，**`C9`** 会**额外**逐条比 sha256 与 pin（`C7` 在有克隆时行为不变），
克隆漂了就变红；克隆不在场时 `C9` 的输出会自己写明「未做上游实物 sha256/pin 对照；
不证明锁文件与真实上游一致」。
**所以：漏拷 `upstreams.lock.yaml` 的下游会直接红，而且不止一项**——
实测 `C7`、`C9`、`C20` 三项同时红（`C20` 的来源段也要对锁文件里的上游 id）。
`C7` 的 detail 显示「锁文件 0 个上游 skill，处置表 101 条」这样的对账差，
**不是**「锁文件过期」——那句只在「锁在、但索引与处置表对不上」的分支里出现。
**这是故意的，不是「下游跑不了」。**

> `SKIP` 是可达的，但它只表示**这一项在这个环境里判不了**，不表示通过：
> 挂了 `upstreams/`、而某个上游仓的 git 元数据不可信（例如只拷了子目录、
> 或软链到本库之外）时，`C9` 无法核对 pin，判 `UNVERIFIED`（渲染为 `SKIP`）并点名是哪个仓；
> 无 git 元数据（`git archive` 导出、或副本装在下游仓库里）时 `C1` 同样判 `UNVERIFIED`。
> v2.0.5 之前 `C7`/`C9` 在下游一律 `SKIP`，后来矫枉过正成「绝不可达」——
> 现在的实况是：**能判的判，判不了的如实 `SKIP`，判出坏的红。**
```

### 2.2 `skills/coldstart.md`

**已假的三处**：

1. `:48`「`C9`（来源真实存在）在下游是 `PASS`，不是 `SKIP`」——名字旧（已改名），且 C9 可 SKIP。
2. `:52-53`「**没有「因为下游没有上游所以跳过」这种状态**」——pin 层判不了就是跳过。
3. `:64-66`「全部检查项 `PASS`……见到 `SKIP` 说明装法或检查器有问题」与 `:78-80`「见到 `SKIP` 说明漏拷了锁文件或者检查器退化了，两种都要当故障查」——SKIP 现在也可能是**本库的环境故障**（上游仓没带 git 元数据），不是装法问题。

**替换措辞**：

`:48-53` 段：

```markdown
    **`C7`（上游处置完备）在下游是 `PASS`；`C9`（来源声明与锁文件一致）在只核锁文件的档位也是 `PASS`。**
    它们核对的 `upstreams/` 不随包分发，但第 9 步那份 `upstreams.lock.yaml` 随包分发，
    所以这两项直接对锁文件判。漏拷锁文件的后果是**红，而且不止这两项**（实测 `C7`、`C9`、`C20` 三项），
    **不是**提示「锁文件过期」——`C7` 的 detail 是「锁文件 0 个上游 skill，处置表 101 条」这样的对账差。
    `C9` 在只核锁文件档位会自己写明「未做上游实物 sha256/pin 对照」；本库里挂了 `upstreams/`
    而某个仓的 git 元数据不可信时，它判 `UNVERIFIED`（`SKIP`）并点名是哪个仓——
    **那是本库的环境故障，不是下游装错了**。
```

`:64-66` 段：

```markdown
- **凡是可判的检查项必须 `PASS`。** `C7` 与只核锁文件档的 `C9` 对随包分发的 `upstreams.lock.yaml` 判，
  下游完全判得了。`SKIP` 是可达的，但它只表示**这一项在当前环境里判不了**（`C9` 的 pin 不可核对、
  `C1` 无本库自己的 git 元数据）——读它自己写的原因，别把它当通过，也别把它当必然故障。
```

`:78-80` 段：

```markdown
- **把 `SKIP` 一律当通过，或反过来一律当故障。** `C7` 与只核锁文件档的 `C9` 在下游是 `PASS`；
  `SKIP` 可达，只表示这一项在当前环境里判不了（`C9` 的 pin 不可核、`C1` 无本库自己的 git 元数据）。
  见到 `SKIP` 先读它自己写的原因——环境故障不是产品缺陷；把它当通过同样错。
  见到 `PASS` 也要读它的范围声明（`C9` 在无 `upstreams/` 时会写明未做实物对照）。
```

### 2.3 `README.md` 的检查项说明

你已经把表重写过一轮（`5a66660`），C1/C9/C12/C13/C15/C19–C22 的措辞与代码一致，**没有发现要改的假话**。只有三处建议：

1. **计数还是错的**：`:25`「26 项检查（`check-closure.py` 19 项 + `check-consistency.py` 7 项）」与 `:127`「`# 19 项`」。实际 closure 本次运行 **21 项**（C1–C7、C9–C16、C18–C22、D1），合计 **28 项**；你自己的提交信息里也写着「closure 20/21」。改成「28 项检查（21 + 7）」。
2. **C15 那一行**建议补一句（本轮新增的展示）：在「边界：只验字段名出现，不验是否在教」之后加「；并在 detail 里列出**未被任何判据门控**的字段（不是缺陷）」。
3. **三态段**（`:272-285`）建议补一句可达性说明，避免读者再形成「SKIP 不可达」的印象：「当前可达的 `SKIP` 有两处：`C1`（无本库自己的 git 元数据——`git archive` 导出，或副本装在下游仓库里）、`C9`（有 `upstreams/` 但 pin 不可核）。两者都在输出里点名原因。」另外 `:282` 的括号里补上「或副本装在下游仓库里」。

---

## 3. D2 升级：教学删净、只留语义无关的提及（本轮，结论：(b) 成立）

**注入**：`roles/architect.md` + architect 名下**全部**含 `` `scope` `` 的技能（逐文件扫出来是 2 个：`spec-driven-development.md`、`constraint-driven-development.md`，合计 3 个载体）。删掉三者所有含 `scope`/`项目级`/`任务级` 的行，各补一句诱饵「本文提到 `scope` 一词时均指技术范围，与契约分层无关」。

**后置条件（先证明注入真的打到了 C15 的判据）**：

```
被注入的载体（3 个）：architect.md，spec-driven-development.md，constraint-driven-development.md
后置条件 a（文件确实变了）：3/3 变；无未变
后置条件 b（producer_text 仍含 `scope` → 子串搜索成立）：True
后置条件 c（残留 3 行全部是诱饵行）：True
独立重算 taught(A4.scope) = True（True 表示 C15 只被子串骗到）
rc=0 C15=PASS
```

**对照组**：只删 `roles/architect.md`（技能仍教）→ C15 仍 PASS，证明 C15 的 `producer_text` 覆盖产出方名下全部技能（单删角色文件不影响它对字段的判定）。注：这一组整个仓库不是绿的——`check-consistency` 的 S1（「注册表里的 `roles:architect` 没有对应文件」）与 S2（`principles/architect.md` 的死链）会红；绿的只是 C15 这一项。

**判定：维持 (b) 边界声明，不改判。**
- 教学删净后 C15 仍绿，且 residue 全是诱饵——说明「`taught` 只验出现、不验在教」是与代码相符的描述，不是漏报。
- (a) 不可行的机械理由：任何「教学上下文」的字面判据都能被一句同样字面合规的诱饵满足（本轮诱饵就是活例；把诱饵写成「`scope`：填 project 或 task（本行不表示任何约束）」同样能骗过任何『要求出现 填/取』的规则）。要真判语义就没有确定性规则——这正是本库把语义层交给人审的原因。
- 我**没有**为了这一条去加强断言，也没有把边界从 C15 detail 里拿掉。

**报告里同时留一句边界**：这个实验只覆盖 A4.scope 一个字段；它证明的是「C15 的判定谓词对语义无关提及无免疫力」，不是「所有字段的教学都抓不到」。

---

## 4. Q2：未门控字段清单（本轮新增）＋ 三段记录格式

### 4.1 实现

`check-closure.py:845-856` 现算，`:857-866` 展示：

```python
all_fields = {(a["id"], fld) for a in artifacts for fld in (a.get("fields") or [])}
ungated = sorted(f"{aid}.{fld}" for aid, fld in all_fields - gated)
```

放在 **C15 的 detail** 里，输出（每次运行都可见，本行原文）：

```
未门控字段 21 个（不是缺陷：字段可以有价值而不是退出门槛）：A1.done_meaning, A1.unknowns, A2.claims, A2.evidence, A3.consumers, A3.freshness, A4.why, A5.edges, A6.change, A7.conditions, A7.stance, A8.claim, A8.environment, A8.observation, A8.scope, A9.decision, A9.evidence, A9.phase, A9.run, A9.subject, A9.why
```

- **不判缺陷、不新增断言、不影响退出码**（oracle 的要求）。
- **不新增检查项**：一条永远不可能失败的检查就是假检查。
- **不新建静态名单文件**：清单每次现算，随注册表增删自动变长变短。
- **不改 C15 覆盖面**：门控集合仍是「被阶段退出判据引用的字段」。

### 4.2 双向回归（driver 的判据，原样实测）

```
Q2-0 基线：未门控 21 个；清单里有 A2.claims、没有待注入字段
Q2-① 只给 A2.fields 加一项：registry 文件确实变了；未门控 21 → 22（+1）；
      清单里出现 A2.new_probe_field；其余清单项未受影响
Q2-② 给 P1 加引用该字段的 verify:：registry 文件确实变了；22 → 21（-1）；
      清单消失 A2.new_probe_field；清单与基线逐项相同；
      唯一新增的红是 C15（新门控字段没有产出方教学，C15 按设计点名它）
Q2-②b 对照：门控一个已有教学的未门控字段（A4.why）→ rc=0 无红，21 → 20，清单消失 A4.why
Q2-③ 恢复基线：21 个，清单与基线逐项相同
```

**要点**：②里 C15 变红是**正确行为**——把一个没人教的字段设成退出判据，正是 C15 要抓的。清单本身的增减与退出码无关（②b 是无红的对照）。

### 4.3 三段记录格式（oracle 裁决 Q3②）与我的三段实例

**格式**（每条检查一张，缺一段不出数）：

```
① 注入：命令/替换串 + 注入前后 sha256（证明确实改到文件）+ 语义后置条件（缺陷真的被引入）
② 期望项独立变红：那一项的 [FAIL] 原样输出 + 除它之外的新增红清单（防「顺手弄红别的」）
③ 恢复基线：从干净副本重跑，同一项回 [PASS]、合计回注入前数字
```

（六个成品的原样输出在 §4.3b；这里不再重复。）

**检查器异常不得记绿**：三段脚本里任何一段断言失败即以非零退出（本轮的 d2/q2/three_stage/three_stage_all6/controls 五个台都如此）。

### 4.3b 本轮六项改动的逐条三段记录（oracle 放行条件第②条）

脚本 `/tmp/tpw-0929/three_stage_all6.py`，`rc=0`，「六项三段记录全部成立」。每项：① 注入真改到文件（sha256 / git ref 前后）→ ② 预期项独立变红（原样行 + **新增红集合**）→ ③ 恢复基线（同一文件 sha256 回基线、该项回 PASS）。

**记录 1 · C1 判据改法**

```
① 基线：tag 指向 HEAD（['v2.0.6']），ref 文件 sha256=926860499c66；C1=PASS rc=0
① 注入：删掉指向 HEAD 的 v2.0.6 tag；ref 文件 926860499c66 → （已删除）；tag --points-at HEAD=[]
② rc=1 C1=FAIL；新增红=['C1']
   ↳ 当前 commit 上没有 tag——打了 tag 之前不能算一个 release
③ 恢复基线：ref 文件 sha256=926860499c66；C1=PASS rc=0
③v 同族变体 archive（无 .git）：C1=SKIP rc=0
③v 同族变体 下游仓库里的副本：C1=SKIP rc=0
     两者 skip 文案均包含新增句「本库的 release 身份只能由本库自己的仓库或外层发布流程保证；本树内不可判」
```

**记录 2 · C9 改名与两档**

```
① 基线（tag+upstreams）：lock sha256=a056b2ced80d；C9=PASS rc=0
   PASS（锁文件＋实物核对）…上游文件 sha256 与 3 仓 pin 均与锁文件一致。
① 注入：篡改锁文件里 addy:api-and-interface-design 的 sha256；lock a056b2ced80d → f0e78297ffd5
② rc=1 C9=FAIL；新增红=['C9']
   ↳ addy:api-and-interface-design 的内容漂移：锁文件记 deadbeef00000000，磁盘是 5dafd0c44a3aabf1
③ 恢复基线：lock sha256=a056b2ced80d；C9=PASS rc=0
③v 无 upstreams（锁文件档）：C9=PASS rc=0；PASS（锁文件核对）…未做上游实物 sha256/pin 对照；不证明锁文件与真实上游一致。
③v pstack 无 git 元数据：C9=SKIP rc=0；未核 pin：上游 pstack 没有可信的 git 元数据（该路径上没有属于 upstreams/ 的仓库）…
     （该夹具另两个仓是软链到本库 upstreams 的，也解析到本 ROOT 之外，所以一并被列为「没有可信 git 元数据」——fail-closed，非缺陷）
```

**记录 3 · C12↔C20 交叉断言**

```
① 基线：registry sha256=811813c95da2；C20=PASS C12=PASS rc=0
① 注入：给吸收形态的技能 tdd 加 origin: library；registry 811813c95da2 → 0f233c1fdbbe
② rc=1 C20=FAIL C12=PASS；新增红=['C20']
   ↳ 技能 tdd 的来源段是吸收形态（逐条列了 3 条上游路径），但 registry 标了 origin: library——正文说吸收、注册表说库内
③ 恢复基线：registry sha256=811813c95da2；C20=PASS rc=0
```

**记录 4 · C21 原则来源与注册表完全相等**

```
① 基线：principles/adversary.md sha256=9e41ccf5e5a8；C21=PASS rc=0
① 注入：删掉该原则的「来源：」行；sha256 9e41ccf5e5a8 → bc0381ee8c4d
② rc=1 C21=FAIL；新增红=['C21']
   ↳ principles/adversary.md 的 p-attack-the-premise 没有「来源：」行——来源无处可核
③ 恢复基线：sha256=9e41ccf5e5a8；C21=PASS rc=0
```

**记录 5 · C22 enforced_by 绑定真实载体**

```
① 基线：registry sha256=811813c95da2；C22=PASS rc=0
① 注入：roles 的 UNVERIFIED → enforced（不给 enforced_by）；registry 811813c95da2 → 3646827e2788
② rc=1 C22=FAIL；新增红=['C22']
   ↳ provenance_policy.current.roles 标 enforced 却没写 enforced_by——没有承载体
   ↳ provenance_policy.current.roles 标 enforced 但 level=none——没到任何可核粒度就不能声称执行
③ 恢复基线：registry sha256=811813c95da2；C22=PASS rc=0
```

**记录 6 · Q2 未门控清单（展示项，预期是「独立变化」而不是变红——这是与上述五项的差别，写出来不是含糊过去）**

```
① 基线：未门控 21 个；C15=PASS rc=0
① 注入 a：给 A2.fields 加 segment_probe；registry 811813c95da2 → d13c8b639378
② 未门控 21 → 22（+1）；片段 …A2.claims, A2.evidence, A2.segment_probe…；C15 仍 PASS rc=0
① 注入 b：再给 P1 加引用它的 verify: 判据
② 未门控 22 → 21（-1），清单里消失该字段；C15=FAIL（新门控字段无人教，C15 按设计点名它）
③ 恢复基线：未门控 21 个；C15=PASS rc=0
```

**注**：本节六项覆盖 driver 点名的 C1 判据改法、C9 改名与两档、C12↔C20 交叉、C21、C22、Q2（共 6 项；driver 消息里写「5 项」但列了 6 个名字，我按 6 个各出一条）。

### 4.4 这份清单会被谁读、什么时候读（driver 要我判断的「伪需求」问题）

**判断：值得做，但它的消费者很窄，我如实说清。**

- **谁**：维护者（改 `registry.yaml` 的 `fields` 或阶段 `exit_criteria` 的人）与审查者。
- **什么时候**：① 拆掉某条判据、或往产物里加字段的那一次改动时——同一行输出立刻显示「你刚拆掉的门出现在这里」；② 审查「哪些声明字段目前只是装饰」时。
- **已经发生过一次**：round-3 §6.4 第 4 条（A3.freshness 因为删掉一条 P6 判据而变成无人门控）和 Q1 之后你刚指出的「A3.freshness 仍不在其中」——这正是它要防的事故类型，而且它现在确实出现在清单里（见 4.1 输出）。
- **我不会为它做的事**：不加断言、不加检查项、不写静态文件、不把它做成「看起来更严谨」的第二份名单。你如果判断连这点价值也不值得，直接删掉 `:845-856` 与 `:857-866` 两处即可，不影响任何断言。

---

## 5. 自测总表（命令 → 数字）

| 台 | 命令 | 结果 |
|---|---|---|
| 负对照（23 条） | `python3 /tmp/tpw-0929/controls.py` | `23/23 条控制符合预期`（A 三态/C1 4 条、B C9 4 条、C C21 6 条、D C12×C20 1 条、E C15 1 条、F C22 7 条——含本轮新增 A3；G 的 schema 对齐另打印、不进这 23） |
| D2 升级 | `python3 /tmp/tpw-0929/d2_upgraded.py` | 后置条件 3/3；C15=PASS；rc=0 |
| Q2 双向 | `python3 /tmp/tpw-0929/q2_regression.py` | 全部符合预期（+1 / -1 / 恢复逐项相同） |
| 三段记录（六项） | `python3 /tmp/tpw-0929/three_stage_all6.py` | `六项三段记录全部成立`，rc=0（C1/C9/C12↔C20/C21/C22/Q2，输出见 §4.3b） |
| 三段记录（三例） | `python3 /tmp/tpw-0929/three_stage.py` | C21/C22/Q2 三段全部成立（与上一条重叠，保留为早期版本） |
| 工作树 | `python3 scripts/check-closure.py` | 20/1/0/21，唯一 FAIL=C1（无 tag） |
| 工作树 | `python3 scripts/check-consistency.py` | 7/0/0/7 |
| 工作树 | `python3 scripts/render.py --check` | `OK（12 个派生文件逐字一致）` |
| archive | `git archive HEAD \| tar -x -C /tmp/...; python3 scripts/check-closure.py` | 20/0/1/21，C1=SKIP，rc=0 |
| 带 tag 副本 | `base`（tag 打在 HEAD 上） | 21/0/0/21；C9 两档输出均实测（锁文件档 / 锁文件＋实物档） |

台外观察（不属本轮改动、供你分派）：`.pi/injection/suite.py` 现在把被审对象钉在 `29a50e4`／`tag v2.0.6`，因此它对本轮改动**零覆盖**；它这次报的 1 条 `c9-lock-corrupt-NO-upstreams` 是打在旧代码上的（无 `upstreams/` 时锁文件没有可对照物，本来就不该期望 C9 红），tag 换代后需要重新钉对象。

---

## 6. 我引入的每一个新假设

（上一轮遗留的也在这里，未变动的照旧列出；本轮新增/加固的用 **[本轮]** 标。）

1. **SKIP = UNVERIFIED 的渲染**。三态只有 PASS/FAIL/UNVERIFIED，SKIP 是后者的渲染；`skip=True` 不计入通过也不计入失败。
2. **C9 的四个分支**：无 `upstreams/` 仍 PASS（锁文件档，detail 自曝未做实物对照）；`repos` 为空记入未核；真漂移 FAIL 优先于任何 SKIP；实物档 sha256 与 pin 都核过才写「均与锁文件一致」。
3. **「上游自己的 git」判据** = `git rev-parse --show-toplevel` 解析出的顶层落在 `ROOT/upstreams` 之内。推论：上游以软链指向本库之外的克隆 → 一律判「没有可信 git 元数据」→ SKIP（fail-closed）。
4. **[本轮]「本库自己的 git」判据** = `show-toplevel` 等于 `ROOT`（`resolve()` 后比较）。含 worktree/submodule（`ROOT/.git` 是文件）形式；下游仓库里的副本、archive 导出、裸目录一律算「无本库 git 元数据」。
5. **C1 的无 tag FAIL 与 SKIP 的分界**：有本库 git 且本库 HEAD 无 tag → FAIL（发布纪律）；没有本库 git → SKIP（环境）。
6. **CHECK_COVERS 是模块常量、人工登记**，不由代码自省推导；新增 `enforced_by` 绑定前必须来这里登记。
7. **C22 的 level 上限硬编码** `{"skills": "file", "principles": "clause"}`，是 `provenance_policy.known_limits` 的机械影子。
8. **C22 的 status 只认 enforced / UNVERIFIED**，其余值一并报非法。
9. **C21 的 `borrowed` 不特殊分支**，走与吸收相同的集合相等；**纯原创必须有内部锚点**（`A\d+` / `` `@id` `` / 相对链接 / `p-*`）。
10. **C21 的身份是 `## p-*` 标题**，不是文件名；文件里出现 registry 没有的段落即报孤段。
11. **C15 选 (b)：不把 `taught` 加强成语义判断**。理由与实验见 §3；边界写在输出里。
12. **C15 的 `gated` 正则** = `\b(A\d+)\.([A-Za-z_][A-Za-z0-9_]*)`，只扫 `phases[].exit_criteria`；notes 里提到不算门控。
13. **[本轮] 未门控清单** = `artifacts[].fields` 全集 − 上述 `gated`；**不按「有没有教学/有没有产出」过滤**；不进退出码；不新增检查项；不落静态文件。清单里的 `(aid, field)` 是二元组，`A1.subject` 与 `A9.subject` 不同项。
14. **[本轮] 清单的展示位**在 C15 的 detail 末尾（同一行可见），不动 `--quiet` 之外的输出结构。
15. **check-consistency 的 `skip` 参数**当前只服务两检查器的 summary schema 对齐；它没有 SKIP 分支，将来加时才用。

---

## 7. 未做 / 边界 / 台外观察

1. **未做**：C13 的角色正文语义冲突、C15 的教学语义、`role-contract-drift` 三类都只声明边界，不加断言（理由见 §1）。
2. **未做**：`.pi/injection/suite.py` 的对象重钉与 `c9-lock-corrupt-NO-upstreams` 期望修正——那是 impl-harness 的台，我只报观察（§5 末）。
3. **观察（C9 的软链语义变严）**：上游克隆以软链形式挂在 `upstreams/` 时，pin 一律核不了 → SKIP。本库的 `upstreams/*/` 在 `.gitignore` 里，正常形态是实物克隆（本库实测两档都是实物档）；软链用户会看到 SKIP 而不是假 PASS。若你们认为软链是合法安装形态，需要的是「允许解析到 ROOT 之外但锁定到同一锁文件 pin」的判据，那会放开一个明显更大的口子，本轮没做。
4. **观察（E3）**：把 `roles/architect.md` 整个删掉，`check-closure` 全绿（C15 也绿，因为技能还在教），但 `check-consistency` **会红**：S1 报「注册表里的 `roles:architect` 没有对应文件」、S2 报 `principles/architect.md` 的死链。即「缺角色文件」已经被 S1 看着，没有我原先设想的那个空子。（我第一版写这份报告时只跑了 closure，错判成「无人拦」；复测 consistency 后改正在此。）
5. **边界**：本报告所有数字都测在 `6e69a5e`（以及它的副本/导出）上；`6e69a5e` 只改 C1 的 skip 文案，计数与 `05a8b4a` 相同。副本里 `v2.0.6` tag 是我在 `/tmp` 副本上强制打给测试用的，**真实仓库的 `v2.0.6` 仍指向 `29a50e4`**，`HEAD` 上没有 tag。

---

## 8. 追加判定：本库自己以子目录形式待在 monorepo 里，C1 该判 SKIP 还是 FAIL？

（driver 指定「给判断，不用改代码」；判断记在这里。）

**判断：SKIP 是正确的；不能判 FAIL。** 理由按强度排：

1. **哪个属性才是 C1 能核的**。C1 的 tag 断言只在「本树是那个『tag 即本库 release』的仓库根」时成立。monorepo 的 tag 是仓库级的，tag → 子项目的映射是命名约定（`tpw/v2.0.6`？还是整仓 release？），C1 无从知道。按未建立的约定判 FAIL，就是把「猜」说成「查出来是坏的」。
2. **FAIL 会误伤文档要求的下游形状**。coldstart 第 2 步与第 9–10 步明确要求把检查器、注册表拷进下游仓库；下游仓库就是一个 git 仓库，本库内容在它里面就是子目录、没有自己的 tag。若这判 FAIL，**每一个按文档安装的下游都永久红 C1**，与「下游装完必须能全绿（含声明的 SKIP）」直接冲突。而「下游 vendored 副本」与「monorepo 是唯一家」从树内看**完全一样**，C1 区分不了。
3. **硬边界 3**。这是安装形态差异，不是产品缺陷。判 FAIL 等于拿一个 C1 判不了的属性给人定罪。

**但 SKIP 不等于没事**：在「monorepo 是唯一家」的场景里，v2.0.1–v2.0.3 那类「tag 与 VERSION 对不上」的缺陷确实在这里静默了。它必须由**外层仓库的发布流程**承担——那是流程责任，不是 C1 能机械核的。两个不需要新机制的补救（都可选）：

- C1 的 skip 文案补一句：「本库的 release 身份只能由本库自己的仓库或外层发布流程保证；本树内不可判。」（你说不用改代码，所以我只给措辞：`check-closure.py:294-297` 末尾追加即可。）
- README / coldstart 里写明 C1 的 tag 核对的前提（本树是仓库根）——这是你文件里的措辞，可加在 §2.3 那一段附近。

**被我否掉的替代方案**：即使顶层不等于 `ROOT`，也去看 `git tag --points-at HEAD` 里有没有 `v{x.y.z}` 或 `*/v{x.y.z}` 的 tag，有就判 PASS。否掉的理由：monorepo 里同名 tag 可能属于另一个包，版本号巧合相同就得到**假 PASS**——比 SKIP 坏，SKIP 至少说自己没查。
