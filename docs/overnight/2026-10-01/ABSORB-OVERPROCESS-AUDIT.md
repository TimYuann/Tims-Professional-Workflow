# ABSORB-OVERPROCESS-AUDIT · 独立过度流程化审查（night candidate active 文本）

审查者：fresh 独立实例 `tpw-audit-overprocess`（Herdr pane `w27:p11`，native session `01a0f831-733d-7230-9b84-5a0d4d84ecc0`）。未编写本 candidate 的正文、guide 或入口；不是 method；未参与集成或裁定。此前 ABSORB-* 记录只作背景读取，不作为现行要求。

固定对象：night branch HEAD `08d9907`（worktree 实测 bytes；worktree 另有其他 session 未提交的过程报告修改，不属本审查对象）。`docs/RESPONSIBILITY-BACKBONE.md` 及其包内导出为冻结参照，只核事实、不改评。实测：Backbone 源与 `professional-workflow/authority/RESPONSIBILITY-BACKBONE.md` SHA-256 同为 `ce82a70016a4a3fc234ea287f39aac8d79a260ddf13747c4fb705bda580453ba`。

方法：只读 `read`、`git show`/`git cat-file`、`shasum` 与文本检索；未运行 UCBIP、服务、测试或网络；未把旧吸收候选、统计或演练限制当作现行口径。

**结论：must-fix 1 项；非阻断 3 项；其余点名口径未发现人为流程。** night delta 对“一般禁新采集 / fixture 普遍禁令 / 某次演练限制通用化”三类问题均已按当前字节修复（见 §4）。

---

## 1. must-fix

### MF-1 · 两个 Charter 示例仍以现在时声明已失效的方法 bytes 摘要

**具体文件 + 段落**

- `professional-workflow/charters/examples/implementation-local-fix.md` · §Task and delegation · Applicable methods：
  > `methods/local-defect-feedback-loop.md` (relative to the package root). Accepted M4 source: commit `013659331c8c5f9f54b866b393972a03d7938773`, SHA-256 `3ca23a74a1a1890123bbab01a114aba813d7e20a7ffcb21b7b2289d5047cb32c`; **this M5 candidate file SHA-256 `1ba8f8f2fb46a0094c22e7ac946e27f30a27b1ce25e201fd5ede819ddc2e4215`**.
- `professional-workflow/charters/examples/technical-planning-cross-module.md` · 同段：
  > `methods/cross-module-design.md` (relative to the package root). Accepted M4 source: commit `01365933…`, SHA-256 `30066c8b3ccee2b85e98c8bc36975f57161e2c93d0bd71c9c668b27bf79bae6f`; **this M5 candidate file SHA-256 `ab0a0bc03448407479fe82b92b2355384e7f2acf49c2ff3026882670f955a0a5`**.

**反例（本地实测）**

- 当前 candidate 实际 bytes（worktree HEAD `08d9907`）：
  - `professional-workflow/methods/local-defect-feedback-loop.md` = `cc8f3911125c8ec8c7b87625590dbb3ffbbd29da4c10b06e785ed1cbaa0d6348`
  - `professional-workflow/methods/cross-module-design.md` = `f9d9c040a94381886fd6f01dc651d25740997cdfe6ab4436498fcf570fcb68c6`
  - `professional-workflow/methods/behavior-claim-evaluation.md` = `0531835f77a8c176df4f173cee64ceee89a21e412ee471a7cc1b0b82f4110c99`
- 示例所写的 `1ba8f8f2…` 与 `ab0a0bc0…` 恰好等于 accepted core tree `91875114e51855517f92ef099cbdf60c34e68243` 内同名文件（M5 快照）的摘要；night candidate `eb7930b` 在三方法的已证缺口处加入正文后改变了这些 bytes，而 `charters/` 目录在 manifest 中记为 “Not changed”（`ABSORB-CORRECTED-CORE-MANIFEST.md`），所以示例没有随之更新。
- 同包 `professional-workflow/methods/README.md` 第 24 行已把同一列改名为 `Historical M5 candidate SHA-256`（Rev.2），两个示例未同步；示例里的 M4 值经 commit `013659331c…` 实测（`3ca23a74…`、`30066c8b…`、`06b06922…`）全部正确，失效只发生在 “this … file” 这一现在时声明。
- 两个示例文件本身的 shipped bytes（`038e6a31…`、`62050af7…`）自 accepted core 起未变，因此这是“随包文件变了、引用它的 metadata 声明没变”。

**后果**

- 任务 Charter 照示例填写时，会把与随包文件不符的摘要写进本次委托记录；独立复核对当前 bytes 做机械核对会 FAIL；读者可能误判方法文件被越权改动，或误判 night 插入正文不属于被绑定对象。
- 这正是“把专业选择误写成 metadata 白名单”的实际形态：绑定以 metadata 值为准，而该值不描述被绑定对象。它不改变方法语义，但会让整层身份 metadata 不可信。

**对应源语义**

- Backbone §2：下游应能找到“本次相关、适用且足够的结论、条件、依据、决定责任与接受状态”。
- `charters/README.md` §Rules：“State accepted commitments with their versions and decision owners”。
- `methods/README.md` 已自认是方法身份/来源 trace 的 owner，并把同一值标为 historical；`authority/README.md` 也以 “source 与 export 同摘要才建立 byte identity” 为纪律。

**最小修改（二选一，不改方法语义、不新增校验步骤）**

1. 删除两处 `this M5 candidate file SHA-256 …` 子句，改为指向 `methods/README.md` §Status and source trace；或
2. 保留数值但改写为 “accepted-core / M5 snapshot SHA-256（历史）”并注明当前 candidate bytes 以 night manifest 为准。

---

## 2. 非阻断

### NB-1 · Profile 的“按需方法入口（候选）/ 待 M4 归位后绑定”仍在默认装配路径里

**具体文件 + 段落**

- 六份 Profile 文件末节“按需方法入口（候选）”的最后一行：`profiles/implementation.md:41`、`profiles/evidence-evaluation.md:43`、`profiles/behavior-domain.md:49`、`profiles/intent-voice.md:42`、`profiles/driver.md:45`、`profiles/technical-planning.md:45`，均为“绑定状态：候选，待 M4 归位后绑定；本预设不含方法正文。”
- `profiles/README.md:44`：“方法正文由 M4 重新解析原始来源后决定采用、限缩或蒸馏；在此之前任何入口均为候选，不构成采用结论，也不得假装 Skill 已存在。”

**反例 / 事实**

- 包内已有 3 个方法正文 + 2 份 guide（`methods/README.md`），而 Profile 仍逐个列出没有正文的方法名（如 driver 的“bounded composition 方法”、evidence-evaluation 的“复现/取证方法”），并声明待 M4。
- 根 README §Use 的装配命令是 `cat profiles/implementation.md …`，并明确 “The output is startup prompt text”；这些失效句会随 Profile 全文进入任务启动文本。

**后果**

- 启动文本一边声明“方法不存在 / 待 M4”，一边携带真实方法文件；agent 可能忽略被绑定的方法正文，或去“寻找”候选方法。属常驻清单 + 失效 metadata 进入默认路径的噪声，不产生新 gate。

**对应源语义**

- Backbone §7 “Roles are caches, not authorities”；`methods/README.md` 是方法选择与身份的 owner；根 README 已用“The M1-era ‘待 M4’ labels remain in the frozen Profiles … use `methods/README.md`”绕行说明。
- `profiles/README.md:44` 的“不得假装 Skill 已存在”是更早的候选期纪律，和当前已发布方法正文并列时会误导。

**最小修改 or 保留理由**

- 最小修改：把各 Profile 的“绑定状态”行改为指向 `methods/README.md`（一行）；并把 `profiles/README.md` §方法绑定状态改为“方法正文由 `methods/README.md` 拥有”，保留候选清单作为 “method needs only”。
- 保留理由：Profiles 是 M1 接受输入，根 README 已声明绕行，不阻塞 recheck；留到下一次允许的 Profile 编辑即可。

### NB-2 · 包入口 README 的状态层叠与 “current M5 candidate” 措辞

**具体文件 + 段落**

- `professional-workflow/README.md` §Package state（第 23 行）与 “Corrected candidate (2026-10-01)” 段（第 25 行）。

**反例 / 事实**

- 入口文档在使用路径之后并列 M1 checkpoint、M4 commit/tree、M5 candidate、M6/PW-01 接受、night corrected candidate、三份过程记录指针，以及 “M4 acceptance does not itself accept the M5 package bytes”。
- 其中 “**The current M5 candidate** carries small package-status/source-trace edits …, so its shipped bytes are identified separately in `methods/README.md`” 与同包 `methods/README.md` 的 `Historical M5 candidate` 列不一致；“current” 不描述当前 shipped bytes（当前是 night candidate）。

**后果**

- 只需装配任务启动文本的读者要先解开 5 层对象身份；该句可能让读者把 M5 快照当当前 bytes，或把过程记录当必读。属入口噪声与不必要的历史阅读压力，不是 requirement。

**对应源语义**

- Backbone §8：消息/入口承载路由与状态，事实与结论由持久产物承载；包 README 的职责是使用路径与当前状态的短指针。

**最小修改 or 保留理由**

- 最小修改：保留一句当前状态（accepted core identity + night candidate 待 recheck）+ 指针；把 M1/M4/M5 历史身份集中到 `methods/README.md` §Status 或 manifest；把 “current M5 candidate” 改为 “historical M5 candidate”。
- 保留理由：包处于接受/候选交替状态，身份诚实必要；因此仅标非阻断。

### NB-3 · `docs/WORKFLOW-INTENT.md` §10 的现在时 registry 指令落在切换注记覆盖范围之外

**具体文件 + 段落**

- `docs/WORKFLOW-INTENT.md:287`：“本文件当前迭代不改 registry、角色、脚本、生成区；不启动业务试点、不发布、不通知 UCBIP 可用。”

**反例 / 事实**

- `workflow/registry.yaml` 已于 2026-10-01 从默认根退役；同文 `:16` 的切换注记写的是“**上文**涉旧体系的表述均为历史记录”，而 §10 位于该注记之下，不被“上文”覆盖。§1 第 13 行的 registry 表述则被该注记覆盖，无问题。
- 冻结 Backbone `docs/RESPONSIBILITY-BACKBONE.md:6` 也有同类 registry 表述，但那是冻结字节，且 `professional-workflow/authority/README.md:15` 已声明这类引用只是 provenance、运行时不加载。

**后果**

- 读者可能把一句针对已退役对象的迭代状态指令读成当前要求，或去找不存在的 registry。轻微、可自解。

**对应源语义**

- 本仓 `AGENTS.md`：“旧 `workflow/registry.yaml` … 已不在默认根：不要求、不查找、不运行”；WORKFLOW-INTENT 自身 `:16` 的切换口径。

**最小修改 or 保留理由**

- 最小修改：给该句加短括号（“历史迭代；registry 已于 2026-10-01 退役”）或整句删除。
- 保留理由：属设计 brief 的历史状态记录，不影响包内规则；可不阻塞。

---

## 3. 已检查、未发现问题的项（对应点名口径）

1. **一般禁止新采集：无。** `guide-redacted-evidence.md` Rule 2：“you may either collect new observations or reuse existing records”；Example：“reuse is the common case here, **not a ban on new collection**”；`local-defect-feedback-loop.md:18` 为 “collect or reuse”。
2. **把 fixture/合成写成普遍禁令：无。** fixture / recorded stub 只作为具体 seam 的选项（`cross-module-design.md` Method 3、`guide-mock-adapter-choice.md` Rule 3 与反例）；guide §Conditions 声明 “Applies to design/test decisions at a dependency boundary; **not to every unit test**”；Charter 示例的 “named offline fixture / no production service” 是该示例自身的任务范围，不是全局禁令。
3. **把某次演练限制写成通用规则：无。** 当前 `guide-redacted-evidence.md` 内已无 batch/offline/no-real-user/no-live-network 的通用条件（实测检索无残留）；Rule 4 与 Raw branch 明确真实任务 access/data/network 继承有效 policy/Charter，“neither grants nor unconditionally cancels existing allowances”，既有有效授权不需逐步重问。Rev.3 的移除在当前 bytes 生效。
4. **一律禁真 / 一律跑真：都没有。** 包内没有要求真实 provider/SDK/部署腿的常驻步骤，也没有禁止真实腿；`guide-mock-adapter-choice.md` Rule 3 的 fixture 选项限于 adapter 的 request construction / response parsing，并要求 “Record the uncovered part”；`behavior-claim-evaluation.md` 要求同 command/data/environment 且先判 comparison validity——证据要求由 claim 决定，不写死真实腿或 fixture。
5. **测试 mode 被写成人为白名单：无。** 方法是菜单 + 条件分支，适用性归 Charter；包内没有禁止使用包外方法或其它测试手段的条文（“self-contained” 是范围声明，不是许可白名单）。Rule 2 的来源禁令有 authored reconciliation（“neither becomes an absolute policy about everything you own”）；Rule 6 明确 “This is not an ‘always delete old unit tests’ policy。”
6. **新增角色/gate/validator/常驻流程：night delta 未新增。** 两份 guide 与三处插入都带 no gate / no mandatory loading / not a universal gate 边界；实测检索未见新 validator/composer/generator/runtime/常驻清单；`local-defect-feedback-loop.md` §Limits 与 `cross-module-design.md` §Limits 保留显式反过度流程条款。
7. **metadata 表本身是否构成白名单：不构成。** `methods/README.md` 的 M4/M5 digest 表与 source pin 表是来源/身份追溯；M4 值经 commit `013659331c…` 实测全部正确，M5 列已正确标 `Historical`；唯一失效是 MF-1 的示例内现在时声明。模板要求 “accepted source commit/digest” 属 provenance 字段，对字节固定的接受对象是相称的；它没有禁止任务绑定包外方法或其它测试手段。
8. **冻结 Backbone 内的 registry 引用：** 属冻结 provenance；`authority/README.md:15` 已声明不加载、不继承编号/检查器。本审查不动 Backbone 源与导出字节。
9. **`profiles/driver.md` 的“并行写者写集 / 单写者串行集成”：** 判断为 delegation/写集事实，不是 runtime mechanics，与同文“不定义进程、并发、队列、锁、重试”及“管到 execution mechanics”的误区不冲突；无需改。
10. **包 README 的 “self-contained” 与外部指针：** `docs/overnight/2026-10-01/` 与 `../adoption-examples/ucbip.md` 在仓库内实测存在；这些是 provenance 入口而非必读要求；“self-contained” 指的是责任边界已随包绑定。保留。

---

## 4. night delta 对 Pro/IM-1 关心口径的核对

- **新采集（Rule 2）**：当前 guide Rule 2 标题与正文为 “Collect or reuse minimal necessary evidence inside the existing authorization”，并写明 “This requires no re-asking each time”；HEAD 提交 `08d9907` 即为该修正。旧“默认只用既有证据”的写法已不在当前 bytes。
- **演练限制通用化（Rev.3）**：当前 `guide-redacted-evidence.md` 无 batch/offline demo 括号，Raw branch 只保留 Rule 4 的通用条件；受限演练范围只留在过程记录中，未进入通用 guide。
- **fixture/own 绝对政策**：`guide-mock-adapter-choice.md` Rule 2 保留来源禁令并加 authored scope reconciliation，Rule 6 保留 narrow replace 条件；两条绝对化风险都有显式否定句。
- **无新增机制**：三处方法插入只加指针与一句覆盖边界，未加 Role/gate/validator/composer/固定 phase 链；两份 guide 均声明 candidate、no authority/gate，并按需绑定。

---

## 5. 本审查的边界与残余

- 只写本文件：未改其它文件、未提交、未运行 UCBIP/服务/测试/网络。
- 未评估运行效果（脱敏是否被宿主强制、adapter 观察是否实际运行、cold-reader 是否成功消费），这些不在文本审查的证据范围内。
- 未按旧吸收候选/统计/R 分级作现行要求核对；ABSORB-* 记录仅作背景。
- 本审查不产生接受、授权、风险接受或晋升结论；MF-1/NB-1…NB-3 是否处理、何时处理，由固定 recheck 与有效 owner 决定。
