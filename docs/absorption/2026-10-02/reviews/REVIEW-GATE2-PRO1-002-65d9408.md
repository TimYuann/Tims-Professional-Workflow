# Gate2 · TPW-PRO1-002 定向复核

2026-10-03，tpw-absorb-gate2，非作者。**需一处最小修；002暂不关闭。** 原源族/已关finding不重开，不调用Pro或执行支付/Provider操作。

固定对象 `65d9408b8caa2c9aa8de400214f48822cefe7fe5`，唯一父/base `5d7d89d3f8fc295ed7c96e63a2af8952e75398ec`；实际diff仅external-tool-operation四增四减（Status、§11/12、X Money源表）。diff --check无输出，未读mutable。读PRO1-DISPOSITION的002范围，并核此fixed对象interface-contract-and-retry §4–9/Conditions直接一致性；回读Cursor `ecc249f1e306fc64ddf83c7bed16cacf7c2239db` X Money §Reading payment results及Never，不复裁Oracle源族。该文本仅保存条件证据，不宣实际服务保证。

## 已符合的两类条件（保留通过部分）

- **允许的原样重放案例**：既有有效授权；同一意图、key与payload；有效retention覆盖重投；真实服务对完整副作用保证不重复；仅响应丢失。原请求已执行而回复丢失时，原样重放返回原结果而非再做一次，§12确实允许，不再把所有unknown一律禁止。其保证仍需实际服务证据，例子不是授权或执行事实。
- **禁止的重放反例**：服务明示“accepted but could not confirm ... do not send again”时，即使手上有key也不能绕禁令；防重复保证未知、键窗过期、改payload、换key/金额/目标不能冒充安全原样重放。真实逐动作approval继续生效，一般任务授权不能替它。transient retry亦仍受同段合法恢复条件与host政策，不可凭最后一句绕过。
- **X Money出处精确**：refused永不retry；明确unconfirmed payment不得重发；“could not process ... try again later”原文称nothing moved且fresh approval后retry once；网络失败后very same payment复用key。新源表按这些具名情境记录，没有把源的所有动作approval/一次retry变成全库政策。接口的intent/key/payload/retention实现只互指，无整套设计复制。

## 残余：查询与副作用重放的条件不能一并封锁

§12先定义所有“legal recovery”必须same key/payload、有效retention与service no-duplicate guarantee；随后仅“Under those conditions”允许query/replay/reconciliation，又称expired key/unknown guarantee“is not recovery”。这把**只读查询原操作状态**也置于副作用重放的全部前提之下，与同对象interface §8的query恢复路径及Conditions“read-only operation needs no idempotency key”直接冲突。

反例：原写结果unknown，key去重TTL已过，但服务仍有原operation ID并提供授权范围内的只读status查询。不能再重放原写，因为可能重复；仍可以按该ID读取已完成/拒绝/待处理状态。查询不会重新执行原写，不需要原写的去重TTL继续有效，也不需要先证明原写可安全重放。保证未知时，该查询还可能正是区分状态所需证据；禁查询会妨碍合法恢复。

**最小修只改§12范围**：把same intent/key/payload、有效retention与防重复效果条件明确用于**可能重新施加副作用的原样重放**；只读query/status reconciliation按其自身实际capability、对象身份、权限/成本/数据边界执行，原写键过期或不可重放不自动禁止该查询。任何有副作用的协调/补偿仍须自身真实阶段语义、保证和有效授权，不能借“查询/协调”名重发、换key/金额/目标。保服务禁重发与逐动作approval；无需复制接口设计、建恢复平台或实际支付测试。

## 下一合法动作

Driver保全上述允许/禁止反例与X Money回读证据，送该单段限缩后的新fixed对象；gate只核此残余与直接一致性，其他已符合部分不重做。当前整文件暂不集成作002关闭依据。文本修订通过后仍不代表实际provider exactly-once/当前policy/支付授权或全包接受。
