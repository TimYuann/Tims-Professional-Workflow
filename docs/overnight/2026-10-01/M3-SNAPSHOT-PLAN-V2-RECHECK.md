# M3 case2 · D Plan v2 受影响 claim 独立复核

日期：2026-10-01。Reviewer：`tpw-night-method`；D 作者/接受责任：`tpw-night-m3-design`。

**Verdict: PASS。** 固定候选对 PC-1/R-2 与 PC-2/R-10 的处置成立，无新增受影响边界 blocker。该结果是限定 challenge/recheck，不记录 D 接受，不授权 E/F，不评价实现或接受 M3。先前原 Plan FAIL 及其证据保留，本 PASS 只覆盖下面新对象的受影响 claims。

## 固定输入

所有指定 SHA-256 实测 MATCH：

| 对象 | SHA-256 |
| --- | --- |
| M3-SNAPSHOT-PLAN-V2-RECHECK-PROMPT.md | `e40851d9b43b55ae2ea90d0f6e0853fb157b7b639143ee03f1191403875ec000` |
| fixtures/m3-snapshot/TECHNICAL-PLAN.md | `bb8afeb1d7519cac8926e1553f30e83590b8fb0504f120120c09cd916e0823d3` |
| BEHAVIOR-CONTRACT.md v2 | `6cf43d3fb647cf2c250f275179762917c0763a669e84f1718d85968a8e66c738` |
| DOMAIN-SEMANTICS.md v2 | `d35766b45085db2b7e5b3315cca5ce4183f722186a850ef317fd571ebba6d45b` |
| M3-BC-V2-REVIEW.md | `675f32ded97ed90013db7eb4d0e6e6ea56fdce702f28ad1ba9e94124a303d091` |
| M3-SNAPSHOT-PLAN-CHALLENGE.md | `bf3e15de71f4bf82adaa5547b9c412b4384a90d9d919420d5023fd9f593ab126` |
| M3-D-PLAN-RECONCILIATION-PROMPT.md | `8cfc6872e9ca266a488f4bb739de94cc42d438e6788332439735bb3fefe0f9df` |

只读核验使用 `shasum -a 256`、`cat`/分段 `sed` 完整读取当前 Plan 与限定 prompt；读取固定 B/C Conditions 和独立 review，并与本会话已读的原 challenge 对照。`git show e3b2d3c:<TECHNICAL-PLAN path>` 仅用于原 Plan 文本差分，未读取该 commit 的代码/测试。Python 仅做文档区段比较；例如当前 §1 与原 Plan 的相应区段字节一致，未重新评价其中运行自述。

## 受影响 claim 判断

### PC-1 / R-2 · 通过

锚点：顶部 Dependency eligibility、§0/§0.1/§0.3、R-2/R-3、§5/§6 Eligibility、A-4、§8。

活跃引用已使用 v2 B/C 摘要和配对关系，v1 只作可恢复历史。顶部、R-2 及 §§5–6 明确 hashes 是 accepted baseline，保持既有接受项/observable quantities 的授权内 `src/**`、`tests/**` 差分可继承；旧的 byte-change-alone 阻断、旧 U-6/实施 gating 均不再作为活跃条件。看到的旧禁令措辞都在明确“former/withdrawn”上下文中，不是残留执行要求。

R-2 对照两个 v2 Conditions 保留：B-1…B-6、observable surface、episode/presented-view 模型、freshness anchor、B-O2 范围、C term/DS-I1…I7、case/view/revision 模型、将 DS-U 项变成新要求、CASE-INPUT 目标或 BC-CHARTER 委托/范围变化仍需新的有效 B/C 接受；变更部分不提前继承，B/C 新版配对。R-3 区分未决项变新规则与 DS-U3 已容许的自由选择，不因正常编号选择自动重开语义。

该修订只解除原依赖冲突。Status、§§5–6、§8 均保留候选与 D 接受尚未记录的状态，依赖资格不证明具体实施符合契约，也不授予修改/执行许可。Driver 的 start/dispatch 是既有授权与依赖资格下的程序安排，不取代 D 专业接受或产生 E/F 新权限；本 recheck 不执行该安排。

### PC-2 / R-10 · 通过

锚点：§0.1 Aggregate recipe、§0.3 PC-2、§8。

Plan recipe 与固定 B/C v2 相同：按相对 path 的 Python `sorted()` 顺序输出 `<sha256><two spaces><relative path>`，换行连接、最后再加换行、UTF-8 SHA-256。path-order `dbd6a306815bdc4cf3a33be14b38d4dd62b49d1535d7db41b9064eb07e51b474` 与 digest-line-order `9074f27da8e0d76113bda8f774297c7c8fbceaedaf67d6ea75eec87d2421e88c` 的角色标记准确。

文本明确撤回 locale 解释与向 B/C owner 发出的旧修正请求，R-10 已关闭、不在活跃 recall 列表中。没有保留“等待源 owner 修 recipe 才继续”的新 blocker。本轮只核文档声明与先前已验证的元数据计算，不再次读取源文件或 tests 来核作者执行自述。

### PC-3 / PC-4 差分 · 未新增阻断

只核已改处置，不重审方法正文或未变核心方案：§0.2/R-9/U-5 正确沿用原 challenge 的外部接受与正文等价结论，将实际 copy/hash 差异保留为 Driver/集成写者的有界 provenance 记录，不再要求方法 owner 重新接受或制造 E gate。

PC-4 所指变化也按原 finding 限缩：§3/D-1/U-1 将 entry point/carrier/episode boundary 视为有界委派协调决定并要求落盘；D-5 将 first-use resolution 限在 C-3 声明的 episode start；C-2 不再把合法 same-revision validate 说成 B 禁止，而区分 D 的 structural strategy 与 B 要求；R-7 修正共享可变引用事实并明确不等于风险评价。这些改变不扩大 B/C 或执行 authority。

## 唯一非阻断措辞 finding

§8 的 “embedded B/C/Backbone text is byte-identical to the files” 仍是未限定的旧概括，与 §0.1 明确“embedded B/C matches v1, not v2 on disk”相矛盾。建议改为：active bindings 是固定 v2；startup 的 B/C copy 对应 v1，仅行为/领域区段与 v2 保持一致；Backbone copy 是原固定导出。

该处不能作为“完整嵌入 copy 等于 v2”的事实依据。不过 §0.1 已明确版本差分，R-2 实际使用 v2 Conditions，两个活跃输入摘要准确；目前没有据此继续采用 v1 no-change 条件或新增权限，因此是有界记录措辞修正，不阻断本次受影响 claim PASS，也不要求全量重审。

## 独立关系与限制

我未编写/编辑 Plan 或新 B/C 内容；原 findings 属独立质疑与补证要求，不构成替作者代做方案。此轮完整读当前 Plan，但仅复核所指定的受影响 claims；未读实现、测试、私有 criteria 或无关包产物，未运行 fixture。

只写本报告，未 commit。PASS 不外推为 Plan 已接受、E/F 已授权、具体实现合格或整体 M3 已接受；D 仍按真实委托拥有 Plan 接受责任，后续固定对象的独立评价另有范围。
