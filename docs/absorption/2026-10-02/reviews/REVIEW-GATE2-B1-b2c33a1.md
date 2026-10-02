# Gate2 · B1 两处窄修复核

2026-10-03，tpw-absorb-gate2，非作者。固定对象 `b2c33a1b9ca71e7e934346e58e9a463aeaf17298`，唯一父 `c62bf5e2ceb99cde5776a50ce5aac9db801634fb`；实际delta仅handoff/design两文件，diff --check无输出。只核新增句及其承重来源，旧PASS/已关finding/轮次/贡献不重开。源依据复用此前直接读Cursor `ecc249f1e306fc64ddf83c7bed16cacf7c2239db` 的swarm Frame/Aggregate、arena与measurement/shipping，及自有DEF2 H02与上一轮窄修裁定；无运行或mutable读取。

## handoff-and-resume：PASS，N-HANDOFF residual CLOSED

§Measurements明确既有有效measurement按claim/coverage、说明basis可复用，affected/unclear才需重测；需重测时使用fixed对象，after-match不证before/operation/goal，Source anchor同步。与前文对象/覆盖复用一致，没有新增测量gate。先前N-HANDOFF其他子项已关保持。Driver可串行集成此整文件；文本不认证实际测量效果。

## design-alternatives：仍需两处局部修

新增swarm真实pin/path与Frame/Aggregate使源**可达**，但修复不止加锚点：正文新增“result dropped、worker rerun once、second miss gap”的必执行流程，Source anchor再次列此规则；H02自有裁定明确不采固定一次重跑。原arena行还把declared coverage/race/mixed、receipt等swarm贡献原样归arena，新增第二行没有消除原错归属。N-H02-SOURCE未完全关闭；新增N-H02-RETRY只涉及此次额外引入的规则。

### 最小修

1. **N-H02-SOURCE**：arena行只载其rubric/base/graft/synthesis/候选比较；mode/coverage/race/receipt/method聚合由swarm行承载，或同一行明确双source分工。保原Matt pin、两Cursor路径与贡献，不doublecount；原finding在审单叫N-H02-SOURCE，当前N-ANCHOR可作alias，勿生成另一个已关finding替代它。
2. **N-H02-RETRY**：缺所需SHA/method的结果不能支持对应claim，保raw与缺口；可按已有授权/成本/真实选择规则补证或重跑，也可直接如实报告gap，不固定必重跑一次/第二次才允许记gap。`first pass`/`rank all`/`best-of`可作为预声明选择规则的例子，不能限定所有合法竞速只能这三种。正文与swarm Source anchor同步，把原源的一次重跑标明为未采默认。保每必需slice覆盖、gap非PASS、实际对象/方法记录、owned outputs与迟到结果限度，不需要新runner/gate或再改其他synthesis。

反例：当前授权/成本只够已有读证，不允许再启动worker；缺receipt可直接交缺口，不能因本段必须重跑一次而自扩执行。一次重跑也不保证receipt充分，次数不是专业覆盖证据。

## 下一合法动作

Driver可现在集成handoff整文件；design保上一通过正文，待仅以上源归属与新流程限缩的fixed对象定向核。此次两文件不能一起报全PASS或宣固定候选齐；其余八PASS/CLI/旧G2保持。具体运行保证/全包接受由各自实际证据与责任持有，gate不调用Pro、不派工、不改产品或stage/commit。
