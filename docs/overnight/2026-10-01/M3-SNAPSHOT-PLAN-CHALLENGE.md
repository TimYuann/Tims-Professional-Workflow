# M3 case 2 · 独立 D Plan challenge · v1

2026-10-01。Challenger：`tpw-night-method`；Plan 作者/决定责任：`tpw-night-m3-design`。

**Verdict: FAIL — 当前 Plan 的实施依赖有一项接受条件阻断（PC-1）。** 核心 coherence 方案、公开反例与多数责任边界有依据；R-9 是已独立核实的有界 provenance 差异，不是核心设计失效。结论返回 D 作决定/修订；本报告不是 Plan 接受、E 实施授权或 M3 关闭。

## 固定对象与独立性

- Candidate commit：`e3b2d3cbb8664466fc9fd6d7e461dab82752ec19`；tree：`4024c85c47840ddcd5df3ca7a073813892263988`，实测 MATCH。
- Plan：`docs/overnight/2026-10-01/fixtures/m3-snapshot/TECHNICAL-PLAN.md`，SHA-256 `bcc10e4829918532f695b2d8be838d1aa2a2b9b8556c7654b5b14f1ce44adc1a`，MATCH。
- Challenge prompt：SHA-256 `cf1eb0ea0ec500b18adc71d3f9a44f42fe94c07390e4f7d65162f272a2346bf3`，MATCH。
- 候选的 D Charter：`6a0e6b7da8f8861e5d37c4d242b7df473e3ede1ffa531e5c73edd92e2730609f`；D input：`89b131138ead556a3f6ac46ab758237c230c8cb6b615a9af57c92238fb4b7374`。
- B/C 固定摘要仍分别是 `86dd6664b73de07ceefdbc5f4d03e09f49b4b1f2ee11cb6a80e48c251176555c`、`15537d71d100dde30075f724c1ef79bc0d4e6a76a179f7f82d7f6c6b286cda06`；CASE-INPUT、BC-CHARTER 与七个 seed source/tests 的每项摘要均吻合所列对象。

我不是 B/C、fixture、Plan 或其实现作者；此前方法文档评审没有代写本方案。本轮独立核固定文本、源结构与公开 Plan 反例，未修改 Plan/B/C/代码/测试。预持 case criteria 保持会话私有；这里只报告基于已公开对象的 findings 和观察，不列 rubric。

## PC-1 · 阻断：R-2 使授权内实施本身失去 B/C 依赖

**位置/事实：** B 和 C 的 Conditions 都将“recorded source structure”的任何变化列为接受失效条件，记录的结构是 `src/**`、`tests/**` 的字节摘要。Plan R-2 进一步明确“Any change … recorded seed structure … new B/C version required”，并称目前未触发是因为 seed 摘要相同。与此同时，Plan §5 要求新增测试、§6 预期修改源代码以兑现新增承诺。

**具体影响：** E 按该 Plan 做一项正常内部实现改动，或仅新增一项 §5 所需测试，就改变被记录的 source/tests 身份；按 R-2 的现有字面，其上游 B/C 接受立即失效，E 必须停止并请求新的 B/C 版本。Plan 没有给出“固定 baseline 身份”和“授权内后续实现差分”的适用性区分，故不能同时主张 E 可实施与其所依赖的接受持续有效。

**依据/返回：** Backbone §2 要求进入依赖实施前有仍适用的接受依据；D Charter 不允许 D 改 B/C 的接受条件。D 应通过 Driver 返回 B/C owner，明确这些 hashes 绑定的是调查 baseline 还是对所有后续候选的持续不变约束；由有效 owner 记录允许的授权内实现/测试差分如何继承、哪些语义/结构变化才使依据失效。之后 D 定向更新 R-2/依赖绑定。不能由 challenger 或 D 默默改读为“正常 patch 不算 change”。

**阻断范围：** 当前以该条件继续 E 的依赖资格；不否定已经有效的 seed 观察、B/C 意义或核心 coherence 思路，不要求 Owner 新裁定或重开全链。不是因“跨模块”而升格，也不是新增常驻 gate。

## PC-2 · 有界事实修正：aggregate 的排序键不是 locale

**位置：** Plan §0.1 的 aggregate recipe 及 reproducibility note；B/C 的 Inputs used recipe。

独立对 exact commit 的七个文件计算后：

- 按**路径**排序，然后逐行输出 `<sha256><two spaces><path>\n`，得到所引用 `dbd6a306815bdc4cf3a33be14b38d4dd62b49d1535d7db41b9064eb07e51b474`。
- 按所声明的**完整摘要行**进行 Python/ASCII 字节顺序排序，得到 `9074f27da8e0d76113bda8f774297c7c8fbceaedaf67d6ea75eec87d2421e88c`。

因此“ASCII collation reproduces dbd6…”和“9074…由 locale-sensitive sort 导致”不成立；根因是 path order 与 digest-line order 两种 recipe。七个单文件摘要全部匹配，没有观察到 seed 数据篡改或缺失。

**处理与范围：** D 修正自己报告的计算事实；源 B/C 的 recipe 文字由其 owner 随 PC-1 的有界澄清处理，不由 D 代改。本项自身不是核心设计 blocker：单文件身份已经足够恢复输入，不为这个记录错误重做 B/C 语义研究或所有测试。不得继续把错误 recipe 标为已验证。

## PC-3 · R-9 独立核对：正文等价，接受并不取决于 blob 自标标题

未采用 D 的自述作为结论，而是从 Git 对象提取实际字节，并从 `D-STARTUP-PROMPT.md` 提取嵌入方法（该 prompt 摘要 `0f6d0e4e028543676273b33c1d0c74e5d933da2ed033be3f9669ca83ac748c90`）。

| 方法对象 | full SHA-256 |
| --- | --- |
| Charter 指定的 `013659331c8c5f9f54b866b393972a03d7938773` 上 method blob | `30066c8b3ccee2b85e98c8bc36975f57161e2c93d0bd71c9c668b27bf79bae6f` |
| D startup 嵌入 copy | `59e686d0a7e488e9c7ae3eb85090da947ad7ac6a68d2feea1b007e4f6ba1456c` |
| 本次 candidate commit 上 method blob | `ab0a0bc03448407479fe82b92b2355384e7f2acf49c2ff3026882670f955a0a5` |

三者从 `## Use` 到 `## Source anchors` 之前的完整区段均为 `e68e8d983ec675ce4fa4d6dea625987c94c7c14dc1e8521500203ae373ba42b9`。逐行 diff 显示 source anchors 也未变；差异仅标题、Status 与末尾 deferral/provenance 句。末句各版均延后同一批 alternatives，没有新增操作、trigger、独立性或接受权。

**接受事实：** candidate commit 的 `ORACLE-ACCEPTANCE.md` M4 节明确接受 `0136593` 的固定三份正文与入口作为可依赖内容。该记录能接受正文仍自标 candidate 的固定 blob；不能仅因旧标题判断该对象未接受。D 无须让“方法 owner”再决定外部有效接受记录是否存在，我也不替 Oracle 作新接受。

**R-9 处置判断：有界、不单独阻断。** 实际阅读的 copy 与引用 blob 并非 byte-identical，应由 Driver/集成写者记录嵌入 copy 的来源和上述语义等价差分，D 引用这项绑定核对或固定同一版本；不冒称完整摘要相同。已存在有效接受与可核正文等价，不需要把 provenance 修正变成新专业 gate；未来实质正文变化才处理受影响方法 coverage。

## 设计支持范围与非阻断精确化

独立只读执行 candidate 中未变的 seed source（`git show` 取字节，内存模块加载，不写 fixture）和原测试，在 Python 3.14.4 观察到 `Ran 3 tests … OK`。重放 Plan 已公开的 §1.3 操作：overview `{'revision': 1, 'open_count': 2}`，更新后 details `[('C-1','CLOSED'),('C-2','OPEN')]`，details count 为 1。公开 falsifier 确实能揭示当前 split-read 缺口，不是只有字段非空。

核心技术方向有据：immutable StateView/CaseRecord 和 rebind publication 可提供稳定值视图；对 coherent pair 的共同依赖、值而非 live alias、episode start freshness、保留接受 B/C 与独立 F 的区分都明确。D 可在 B 的合法 variants 内选 pinned policy；这不要求新 B 产品取舍或 Owner 许可。没有业务范围扩大、持久化/迁移/发布权限转移。

可选精确化（不另设 blocker）：

1. D-1 的 carrier/interface 形状、module placement 与 D-5 的 episode proxy 对消费者和验证者并非全属“不影响接口的 implementation interior”。D 已显式授权 E 在 C-1…C-10 内选择，因此可作为**有界委派的协调决定**；建议这样命名并要求实际选择落盘，使 F/下一消费者能找到具体入口与 episode boundary。不要求 D 固定每个 helper 或增加文件白名单。
2. C-3 明确 start pin，但 D-5 对 lazy resolution 的短句只写“不 resolve twice”。建议把有效前提完整限定为满足 C-3 的已声明 episode start，而不暗示任意延迟首次读取都算 Plan-conformant。Plan 声明 delegated choices 仍须满足全部 §2，可据此处理，无须新增 gate。
3. C-2 将“re-read + validate”概括为无法满足 B-1 太绝对：如果旧 overview 与新 details 的 revision 相同，合法性来自同一 revision 的一致身份。D 可以选择 structural pinning/no retry，但应把它记为本 Plan 的技术策略，不将所有合法替代写成 B 禁止。当前 pinned 设计可行，不因此否定其方案。
4. R-7 的“no shared state”不准确，StateStore 在读/更新操作间是共享可变引用；本 exercise 没有的是并发/跨 viewer/持久化资源面。已有 in-process 测试和 immutable views 覆盖本次已知面，不凭这个措辞创造安全审查或无风险结论。

## 返回与后续

请 D 先处理 PC-1 的依赖条件冲突，通过 Driver 找 B/C owner 作有界澄清；同时修正 PC-2 的事实记录，并按 PC-3 记录方法等价绑定。PC-1 未处置前，不能将本候选宣告为已独立通过、可依赖的实施 Plan；其他已支持判断可保全，修订后只核实质受影响差分。

本次 FAIL 是确定的依赖/接受条件冲突，不是环境故障；没有以环境缺口伪造产品 FAIL，也没有给出方法外的新权限或降低 B/C。Plan 接受仍由有委托的 D 责任承担，实施结果另由 F 对固定版本取证，整体 M3 接受/关闭按既有委托处理。
