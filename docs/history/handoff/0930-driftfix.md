# 0930 轮 · 规格漂移修复报告（`tpw-0930-driftfix`）

- 任务书：`.pi/handoff/0930-driftfix-TASK.md`；driver：`tpw-0929-driver`。
- 改动：5 个文件，`+9 / -8`。未 commit、未 tag、未改 `VERSION`。
- `git status --short` 只有这五个：`roles/architect.md`、`skills/decision-ledger.md`、
  `skills/implement.md`、`skills/recall-context.md`、`skills/research.md`。

## 一、三个任务

### 任务 1：`A9` 字段规格歧义

- `skills/decision-ledger.md:24`（方法 2）改写：`A9` 一行是八栏
  （`actor` / `run` / `subject` / `phase` / `decision` / `why` / `evidence` / `result`），
  本技能负责的是**后四栏内容**，不是整行；前四栏是行格式的一部分、**不是可选项**，
  同会话可由 `ledger.sh` 代填（`actor` / `run` 读环境变量，`subject` / `phase` 随调用给），
  不能因为「只写四件事」就整条略过；末尾补交叉引用 `roles/scribe.md` 的 A9 表格与 `docs/ledger.md`。
- `skills/decision-ledger.md:36`（产出节）同步改成「一行是八栏、身份四栏由 `ledger.sh` 补齐、
  下面四栏是本技能字段」，避免只读产出节的人仍然以为一行四栏。
- 依据：registry `A9.fields`（`workflow/registry.yaml:305-313`）＝ 八栏。
  `roles/scribe.md:40` 与 `docs/ledger.md:8` 已经是八栏，未动。

### 任务 2：`A2` 与 `A6` 的字段数漂移 + `gaps` 同名不同义

- `skills/implement.md:30`：「三个字段」→「四个字段（`subject` / `change` / `runnable` / `known_gaps`）」。
  依据 `A6.fields`（`workflow/registry.yaml:236-240`）＝ 4；`roles/builder.md:46` 的「四栏」是对的，未动。
- `skills/research.md:40`：「四个字段」→「三个字段」。依据 `A2.fields`（`:140-143`）＝ 3；
  该文件其余部分（三栏正文 + 一段载体说明）没有第二处第四字段暗示，未再动。
- `skills/recall-context.md:57-59`：把与 `A2.gaps` 撞名的字段改称「**反复出现的问题**」（最多 5 条），
  并显式加一句「**这不是 `A2.gaps`**——那份 `gaps` 记的是『查过但没查到的』」。语义未变，只消除同名不同义。

### 任务 3：`A9` 写入权表述冲突

- `roles/architect.md:89 / :112 / :118` 三处「写进 A9」全部改成交接措辞：
  「**交给 `scribe` 追加进 `A9`**」（`A4` 冻结那一步同样）。
- 依据：registry `A9.producer = scribe`（`:302`）；对齐方向是 `skills/documentation-and-adrs.md:68`
  （「`A9` 的唯一产出方是 `scribe`。把下面四栏交给 `scribe` 追加」）。该技能由 architect 拥有
  （解析 registry 实测 `owner_role: architect`、`outputs: []`），所以这是向自己的技能正文对齐，
  不是引入第二份真源；未改该技能。
- 冻结动作本身仍要落在 `A9`（registry P1 判据 `:367` 要求「在 A9 写下不修的理由与裁决」），
  改的只是写入路径（经 `scribe`），不是删掉这条动作。

## 二、我顺手核到但没改的

1. A2/A6 其余引用点都已是正确数字：`roles/scout.md:38`（A2 三字段）、`roles/builder.md:46`（A6 四栏）、
   `skills/trace-paths.md:97`、`skills/handoff.md:30`、`skills/context-reconstruction.md:36`（A2 三字段）；
   派生视图 `docs/artifacts.md:30-34`、`:56-61` 也已按 registry 列出 3/4 字段。均未动。
2. `skills/recall-context.md:36` 头部仍声明 `产物：A2`，但该技能的 A2 快照形状
   （胶囊 / 线索 / 反复出现的问题 / evidence / 下一步）与 registry `A2.fields`（`claims` / `evidence` / `gaps`）
   只有 `evidence` 重叠。改名只解决撞名，不解决形状差异——属语义问题，未动。
3. `README.md:254-256` 有一处历史变更记录写着旧的「A6……三个字段」状态。那是在描述修复史，
   不是现行规格；且 README 不在可改名单，未动。
4. `skills/domain-modeling.md:73`「词汇表与决策记录是落地文件……决策记录落在 A9 上」：
   只说落点，不说写者，与 architect 那三处的「直接写入」语气不同。未动。
5. 三项语义问题的现场证据（只报不改）：
   - **driver 映射无产物归属与判据**：registry 里 `document-mapping` 是 `owner_role: driver`、`outputs: []`
     （`workflow/registry.yaml:1090-1099`），而同一份真源 `A9.embodiment`（`:316`）说
     「装配记录（集合 A↔B 映射结果、冷启动三栏报告）是 A9 在装配时写的几行」——载体在散文里有、在声明里没有；
     P0 的四条退出判据（`:346-350`）与映射无关，`driver_seat_note`（`:352-353`）明说「它不产出本阶段任何产物」。
   - **「退回」无载体**：`roles/*.md` 里 35 行 / 37 次（`grep -c` 按行 35，`grep -o` 按次 37）；
     registry 只有两处无关提及（`:333` 环境故障、`:1086` 重判档）。库里没有字段或规则说
     「退回」记在哪、什么形态、谁需要看到；例子：`roles/scout.md:74`、`roles/builder.md:91-94`。
   - **角色不声明 runtime 能力**：registry 的角色字段集合实测为
     `id / zh / mission / owns_artifacts / ribbons / skills / principles / forbidden`（以 scout 为例，
     `python3` 解析 registry 得到），`roles/scout.md` 的标题也没有能力声明节；而 scout 的技能要求真实执行与工具
     ——`skills/research.md` 方法 4 要求「一次真实运行的命令与输出」，`skills/recall-context.md` 方法 5
     要求「拿工具逐个查现状」。没有 shell 时这些技能的 `evidence` 没有来源，与试装时 scout 被派到无 shell agent 一致。
6. registry 内一对重复 `note:` 键：`workflow/registry.yaml:1076-1088`（tier-sizing）同一块里出现两个 `note:`
   （`:1082` 与 `:1088`），`yaml.safe_load` 解析后只剩后者（实测 `tier-sizing.note` = 「本库原创……」），
   「inputs 为空是刻意的……」那段不在解析数据里。registry 不在可改名单，未动；纯记录。

## 三、我对判定的疑问

1. **「`A9` 唯一产出方是 scribe」比 registry 实际写死的更强。** registry 只写 `A9.producer = scribe`，
   但同一份真源里 `A9.embodiment`（`:316`）说装配记录由 driver 一侧在装配时写进 A9，且 `A9.actor` / `run`
   两栏的设计前提就是多写者。读成「字段合同与追加路径的 owner」是自洽的；读成「只有 scribe 能产生 A9 行」
   就会和这两处打架。我按任务书把 architect 的三处对齐到「经 scribe 追加」（方向上不会更错），
   但「谁可以往 A9 追加行」在 registry 里没有单一答案：若定死「都经 scribe」，
   `document-mapping`（driver 拥有、装配记录进 A9）与 `skills/coldstart.md:61,76`（档位/映射/冷启动都记进 A9）
   也需要同一轮对齐；若保留多写者，`skills/documentation-and-adrs.md:68` 的「唯一产出方」措辞要放宽。
   这条建议 Owner 给出单一读法。
2. **registry 能裁决字段的名字与个数，裁决不了各技能的物化形状。** 任务 2 的仲裁（A2=3、A6=4）成立；
   但 `skills/recall-context.md` 声明 `产物：A2`，其快照形状除了改名后的「反复出现的问题」，
   还有「胶囊 / 线索 / 下一步」也不在 `A2.fields` 里。如果规则是「声明 `产物：A2` 的技能必须使用 registry
   字段集合」，那要改的不止 `gaps` 一处；如果允许技能在 A2 载体上自定展示形状，需要写明这条豁免。
   我按任务书只做了撞名修复，没有扩到形状。
3. **「前四栏可由 `ledger.sh` 代填」这句我在正文里做了区分。** 严格说只有 `actor` / `run` 是从环境变量取，
   `subject` / `phase` 仍由调用方随命令给出（见 `docs/ledger.md` 用法一节的参数顺序）。我把这点写进技能正文，
   免得后来者以为四栏都不用管；如果后续希望统一口径，以 `ledger.sh` 的实际入参为准。

## 四、三个检查的实际输出

改动前基线：closure 20/21（唯一 FAIL = C1）、consistency 7/7、compose-role --check OK。
改动后三项与基线一致——未引入新的红，也没有为了让检查变绿而削弱检查。
另附 `render.py --check`：派生视图逐字一致（本次没有改注册表，无需重新生成）。

### `python3 scripts/check-closure.py`（退出码 1）

```text
TIM · check-closure.py（只读闭包检查）
真源: workflow/registry.yaml
----------------------------------------------------------------------------
[FAIL] C1 结构与版本单一来源              版本 2.0.7，产物 9／阶段 7／角色 9／原则 23／技能 51
         ↳ 当前 commit 上没有 tag——打了 tag 之前不能算一个 release
[PASS] C2 产物有主且有人接               9 类产物全部有唯一产出方且被消费
[PASS] C3 阶段可达、依赖闭合且无孤儿          7 个阶段按序可达、所需产物在上游已产出，7/7 个阶段至少有一条依赖边（无孤儿）
[PASS] C4 判据可判定（引用全部可解析）         26 条退出判据，0 处无法解析的引用，全部 A*.field 都指向真实字段
[PASS] C5 角色装配件一致                9 个角色的产物／技能／原则指认双向一致
[PASS] C6 无孤儿且阶段装得出来             51 个技能／23 条原则全部被引用，每个阶段的默认角色能产出它声称的产物
[PASS] C7 上游处置完备（对锁文件）           锁文件 101 个上游 skill，处置表 101 条，一一对应
[PASS] C9 来源声明与锁文件一致（有实物时校验内容）   101 个上游 skill 索引（锁文件），0 条失效来源。PASS（锁文件＋实物核对）：来源在锁文件中；上游文件 sha256 与 3 仓 pin 均与锁文件一致。
[PASS] C10 处置与来源双向咬合              101 条处置与目标 sources 双向一致（正向：into 里的每个目标都得列它；反向：sources 里的每个上游都得有指向该目标的 absorbed 处置）
[PASS] C11 消费声明与装配双向咬合            23 条消费声明全部被阶段接住，且每个阶段的 required_inputs 都在对应产物的 consumers 里
[PASS] C12 无吸收来源技能显式标注            3 个技能没有吸收来源（registry.sources 为空）并标了 origin: library；该计数与 C20 的非吸收形态数（借鉴＋纯原创）对账，两者由交叉断言保证相等
[PASS] C13 越权写由显式声明判定             26 条判据全部显式声明了 write/verify，没有越权。边界：仅核阶段退出判据的 write:/verify: 显式声明；不读取角色正文，正文与 registry 的写权冲突须人审。
[PASS] C14 技能头部产物声明与注册表一致         51 个技能的头部声明与注册表 outputs 一致
[PASS] C15 被判据校验的字段：声明的人与产出合同都成立  19 个被阶段判据校验的字段，声明的责任人与产出方正文里的填法两两对齐。边界：taught 只验字段名在产出方（角色文件 + 它拥有的技能正文）里出现，不验是否在教——把真实教学删掉、只留一句语义无关提及的情形抓不到，属语义、由人审。边界：不保证字段名在角色文件与技能文件之间逐字一致——某一份改名、另一份仍列着（role-contract-drift）不算缺陷。未门控字段 21 个（不是缺陷：字段可以有价值而不是退出门槛）：A1.done_meaning, A1.unknowns, A2.claims, A2.evidence, A3.consumers, A3.freshness, A4.why, A5.edges, A6.change, A7.conditions, A7.stance, A8.claim, A8.environment, A8.observation, A8.scope, A9.decision, A9.evidence, A9.phase, A9.run, A9.subject, A9.why
[PASS] C16 每阶段都要求记台账              7 个阶段都有 A9 判据
[PASS] C18 开工前的技能不依赖开工后才有的产物      2 个开工前技能不依赖任何阶段产物
[PASS] C19 横切带无孤儿                 3 条横切带全部被至少一个角色挂载，携带的技能与挂载引用全部可解析
[PASS] C20 技能来源段与注册表形态一致          48 个吸收／3 个借鉴／0 个纯原创（形态 original）；其中 3 个标 origin: library，与 C12 的计数对账（交叉断言：吸收形态不得标 origin: library）
[PASS] C21 原则来源与注册表完全相等           23 条原则的「来源：」行反查出的上游 id 与 registry.sources 逐条相等（拒幽灵路径、缺失、串线、重复）。边界：只证锚点存在且与注册表一致，不证段落语义忠实——「这条原则的正文真的来自那段上游」不可机械核验，由人审。
[PASS] D1 底座解耦（已知名黑名单·大小写不敏感）    扫描 93 个库内容文件（含 docs/，只豁免 history/ 与 archive/），0 处命中已知底座名。边界：黑名单是人工枚举的 14 条已知名称，不是穷尽清单——别名、缩写、厂商代号抓不到
[PASS] C22 来源政策的 enforced_by 绑定真实载体 provenance_policy.current 共 4 条；enforced 的绑定经 CHECK_COVERS 核对（C20→skills/## 来源；C21→principles/来源：）；UNVERIFIED 条目均带 owner 与 due。边界：CHECK_COVERS 是维护者的声明——C22 证明「声明的类目」与 policy 一致，不证明检查实现真的读了那些文件；后者靠 C20/C21 的故障注入反例。
----------------------------------------------------------------------------
合计: 20 项通过 / 1 项失败 / 0 项跳过 / 21 项检查
```

### `python3 scripts/check-consistency.py`（退出码 0）

```text
TIM · check-consistency.py（只读一致性与互斥检查）
真源: workflow/registry.yaml
----------------------------------------------------------------------------
[PASS] S1 无游离文件（rglob 含子目录）    角色 9／技能 51／阶段 7／横切带 3 与注册表对齐（含子目录逐个文件比对），scripts/ 无残留
[PASS] S2 引用可解析（含 fragment 死链） 扫描 84 个库文件与入口文档（含 README/AGENTS/docs，只豁免 history/ 与 archive/），0 处未知 id、0 处死链
[PASS] S3 文件内权限互斥（子句级）         扫描 84 个文件的「动作+宾语」否定/要求配对（极性按子句判），0 处互斥。边界：只抓同一文件内同动词同宾语；同义改写与跨文件冲突抓不到，那部分靠独立审查与人审
[PASS] S4 硬规则引用可解析 + 实现裁决验证不同场 3 条阶段硬规则只引用已定义的阶段/角色；2 组职责分离不共场；19 条角色硬边界无重复。边界：硬规则的中文语义（如「solo 档除外」的豁免）抓不到——本检查只看它引用的 id 与它维护的分离约束。边界：S4 不读角色正文；「实现者」↔`builder`、「下结论」↔「给出裁决」是中文语义映射，没有确定性规则能把它变成断言——角色正文里写反硬边界的散文抓不到（s4-role-body）。
[PASS] S5 技能三角一致（含 outputs 可解析） 51 个技能的阶段／归属角色／outputs 可解析／装配四者相容
[PASS] S6 产物持久性一致              9 类产物的 persistence 与各阶段依赖、各角色归属相容
[PASS] S7 横切带适用范围一致且可解析        3 条横切带的适用范围全部是已定义阶段，且覆盖其携带角色参与的阶段
----------------------------------------------------------------------------
合计: 7 项通过 / 0 项失败 / 0 项跳过 / 7 项检查
```

### `python3 scripts/compose-role.py --check`（退出码 0）

```text
角色装配：结构成立（9 个角色，34 条原则引用，正文均在 principles/，角色内无第二份释义）
```

### 附：`python3 scripts/render.py --check`（退出码 0）

```text
render --check: OK（12 个派生文件逐字一致）
```
