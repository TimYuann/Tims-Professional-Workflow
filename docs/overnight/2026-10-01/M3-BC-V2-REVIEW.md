# M3 case2 · B/C v2 有界独立复核

日期：2026-10-01。Reviewer：`tpw-night-method`。作者/接受责任：B/C 文档声明的 `tpw-night-m3-bc`，实际实例 `tpw-night-m3-bc-contract`。

**Result: PASS。** 这两个固定 v2 对象解决 PC-1 的持续 no-change 条件冲突与 PC-2 的 aggregate recipe 错误，保留 v1 的行为/领域 claim；未发现新的接受边界 blocker。该结果只评价 B/C 输入与声明差分，不接受 D Plan、不授权 E、不评价实现或接受整体 M3。

## 固定对象与命令

| 输入 | SHA-256（实测 MATCH） |
| --- | --- |
| M3-BC-V2-REVIEW-PROMPT.md | `c0e44544ae4b9eaf837b9ff2d919119e8028a975b82a6b8e73abf37822d8cc51` |
| fixtures/m3-snapshot/BEHAVIOR-CONTRACT.md v2 | `6cf43d3fb647cf2c250f275179762917c0763a669e84f1718d85968a8e66c738` |
| fixtures/m3-snapshot/DOMAIN-SEMANTICS.md v2 | `d35766b45085db2b7e5b3315cca5ce4183f722186a850ef317fd571ebba6d45b` |
| M3-SNAPSHOT-PLAN-CHALLENGE.md（仅 PC-1/PC-2） | `bf3e15de71f4bf82adaa5547b9c412b4384a90d9d919420d5023fd9f593ab126` |

只读操作：`shasum -a 256` 核上述身份；`cat` 完整读取两份 v2 与 review prompt；`git show 893eaf8:<B/C path>` 取回 v1；`git diff 893eaf8 -- <B path> <C path>` 限定差分；`sed` 读取 challenge PC-1/PC-2。Python 仅比较上述文本区段、从其 Inputs used 元数据抽取七组 path/hash 并重算 aggregate，未读取任何 `src/**`/`tests/**` 内容。

取回的 v1 B/C 摘要分别为 `86dd6664b73de07ceefdbc5f4d03e09f49b4b1f2ee11cb6a80e48c251176555c`、`15537d71d100dde30075f724c1ef79bc0d4e6a76a179f7f82d7f6c6b286cda06`，与 prompt/候选声明一致。

## Findings 与依据

### PC-1 · 已解决

两份 Conditions 都明确 source hashes 识别作者据以定义契约的 accepted baseline，不要求之后 fixture 字节永远不变。B 将继承限制为保持全部接受项与可观察数量；C 限制为保留既有术语/不变量。授权内实现、测试、内部拆分/重命名等差分不会仅因字节变化失效。

重开条件保留边界：行为项、observable surface、episode/presented-view 模型、freshness anchor、领域术语/不变量、将未决项转成新要求、CASE-INPUT 目标或 BC-CHARTER 委托变更不自动继承旧接受；变更部分须新的有效接受。两份文档作为 v2 配对，避免引用混合版本。

这只说明上游结论适用性如何继承，不证明任何具体代码/测试已符合它，也不授予修改权限。B 明确“不授权实施”；C 明确发现事实冲突不能静默改词义。与原 PC-1 的矛盾不同，正常授权内差分现在有合法继承空间，而语义改变仍回到有效 owner。

### PC-2 · 已解决

两份 Inputs used 的 recipe 都明确：先按相对 path 的 Python `sorted()` 顺序排列，输出 `<sha256><two spaces><relative path>`，以换行连接并加最终换行，对 UTF-8 文本取 SHA-256。

仅使用文档所列七组元数据重算：path order 为 `dbd6a306815bdc4cf3a33be14b38d4dd62b49d1535d7db41b9064eb07e51b474`；digest-line order 为 `9074f27da8e0d76113bda8f774297c7c8fbceaedaf67d6ea75eec87d2421e88c`。与 v2 分别标记的记录值/非匹配替代值一致，没有再把排序键差异归因于 locale。

这是 recipe 与已列元数据的独立核对，不是重新核验源文件实际字节，也不为作者“七份文件重新核验”的历史活动自述作独立背书。

### v1→v2 claim 保留 · 已确认

不是仅相信 change log：直接比对 B 从 `## Observable surface` 到原文件末尾与 v2 `## Change log` 之前的区段，逐字节相同，区段 SHA-256 为 `eab01bf9d644ba3d02b2e5261526b7d959375e8ccd527a7709c0ceccbe5c18f1`。这覆盖 observable surface、B-1…B-6、例子、P-1…P-3、B-O1…B-O2。

C 从 `## Terms` 到对应末尾区段同样逐字节相同，区段 SHA-256 为 `f303d5c94063a313c74fa0d9cf335dfa49758eaaa9b65e7366767382cdcc2dc3`，覆盖全部 term definitions、DS-I1…I7、例子与 DS-U1…U4。范围仍为单 store lineage 的隔离 exercise；没有增加业务规则、并发/持久化能力或新实施义务。

## 非阻断措辞建议与限制

两份 Change log 的“only contract-content/semantic changes require a new B/C version”比 Conditions 的完整列表更窄；完整列表还含 exercise goal/delegation 变化。可改成“上述 Conditions 所列变化需新版本”，避免以后只读摘要时漏掉边界。详细 Conditions 已明确且彼此相容，当前不构成 blocker，也无需额外评审 gate。

本次独立关系沿用同一 session：我不是两份候选作者，此前 PC-1/PC-2 findings 属质疑/补证要求，没有代写新 B/C 内容。本轮未读实现、测试、D Plan、实现输出或私有 criteria，未改 B/C 或其他产物；只写本报告，未 commit。候选自行声明的 exercise author acceptance 与本次独立 review 是不同事实；本报告不产生额外接受权或执行许可。

本 PASS 覆盖上述精确 B/C v2 摘要。D 依赖更新或后续候选资格属于各自固定对象，不由本报告自动放行。
