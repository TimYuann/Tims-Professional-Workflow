# Gate2 · B1/B2 窄修与DEF2增量定向复核

2026-10-03，tpw-absorb-gate2，非候选作者。**8文件PASS、2文件需最小修**。沿上一轮review，不清零轮次/贡献/未决，不重开旧R/D1/J1/EXT8/G2与B3已关。N-REUSE、N-DELIVERY、N-CHARACTERIZATION、N-HARNESS、N-CLI-ORACLE关闭；N-HANDOFF其余子项关闭，仅量化claim复用句残留。新增N-H02-SOURCE仅源定位，不重审已过synthesis。

## 固定范围与实际核查

- B1 `b8358cd392f448054e54b76e29ea3b6a7e812001..c62bf5e2ceb99cde5776a50ce5aac9db801634fb`；head唯一父 `a66edb396607d8d804f91269edfff336d17e598e`。实际7文件+40/-33，覆盖a66edb3 H02/H04/H09与c62窄修。
- B2 `9dcc85a9e75fe28166c659d5ecfb2d34cfe3ee96..f88e105f5b8f438cbe08eaa49bb11e33e93e3039`；head唯一父 `8ee9f7da3cbca95a2b1031260675229dc656df93`。实际3文件+22/-5，覆盖H06/H09、external H08/H09与CLI出处修。
- 两固定区间`git diff --check`无输出；未读mutable候选或替HEAD后续对象裁定。当前消费对象 `8677ef99eec5371d9bf775d6a44f497a0f46207c`，core tree `a4505b3955ef7545f4db47fe25f0a233aee99d95`。
- 独立回源沿已直接读Cursor `ecc249f1e306fc64ddf83c7bed16cacf7c2239db` 的arena/swarm、reflect/recall、benny triage/reproduce+adapter/verify、SDK auth/stream/MCP/失败章、why三源、loop/handoff/measurement/hooks/watch-policy与shipping；本次再直接核swarm Frame/Aggregate、Sentry/Linear承重段，源HEAD仍为该pin。对照自有DEF2及上一轮两B具体finding，不继承作者全文/实跑资格；Oracle J4仅核署名不复裁业务机制。

## 文件级结论与落点

| 文件 | 结论 | 关闭/新增范围、理由与边界 |
| --- | --- | --- |
| B1 change-review | PASS；N-REUSE CLOSED | 按actual object/diff/承重inputs与路径判断affected/unclear，未受影响且coverage有效可说明依据复用；noise复跑为可用办法非唯一；Source anchor同步，patch-id/old green不升级。 |
| B1 change-slicing | PASS；N-REUSE / N-DELIVERY CLOSED | delivery按实际unit依赖/保持/写面/交付/适用证据/未知；三boxes/build/review/landing仅真实task/接受policy存在时使用，absolute budget由目标owner接受；bottom-up限定真依赖stack，独立work按自身graph。原wide-refactor例外与旧C8保。 |
| B1 guide-test-evidence-quality | PASS；N-CHARACTERIZATION CLOSED | immediate green明确可证当前对象窄行为，但不证明曾抓到原defect或修复因果，广泛absence按coverage；不再抹掉真实after观察。表尾排版修不当新机制，旧EF/effect段保。 |
| B1 verification-harness-design | PASS；N-HARNESS CLOSED，H09限缩合并 | 缺身份/能力/隔离只关闭该claim所需操作，保local/captured证据、不全setup或默认新Human；combo条件/优先级按host/task风险，rollup仅checks、BLOCKED查真blocker/policy、不借green清review-required。新增actual trigger/discriminating state/paired objects与真实用户surface、local mapping按各claim覆盖，未强双UI/全部media。 |
| B1 local-defect-feedback-loop | PASS；H09限缩合并 | actual trigger、判别状态、paired时同条件固定before/after；precondition可安排但不setter伪造用户路径，local logic/mapping有合法自己的claim。原diagnosis-only/有效diagnose-and-fix与单trace可成立的边界保，不要求每defect都有paired。 |
| B1 design-alternatives | 专业新增内容PASS；需修N-H02-SOURCE | H02宣mode/selection/predicate/artifact/method、coverage与race分开、gap非PASS、losing/late限度保、same/multi model非独立及非固定数量/host/重跑规则正确；新增source table把swarm机制只归arena，见最小修。旧G2-PIN关闭不重开。 |
| B1 handoff-and-resume | N-HANDOFF部分关闭；仅measurement复用句待修 | H04旧capsule为版本源与live事实核、旧承诺/round不清、readonly标签不免effect/无自动backlog通过；H2非专业资格门、真实record可支持claim、state是source非authority、旧error可真stop、恢复按runtime/委托、不强Git commit/id pair/heartbeat/race、damaged保raw按授权修清、真实stop非fixed iteration全部关闭。量化reuse句仍无条件rerun，见下。 |
| B2 agent-facing-cli-contract | PASS；N-CLI-ORACLE CLOSED | Status具名`ORACLE-REVIEW-A4-DEF3` J4恢复正确审核者/出处；未动J4/DEF G12已过内容，不复裁Oracle、无当前SDK认证。 |
| B2 rationale-and-premise-review | PASS；H06/H09限缩合并 | 历史路径/生成/搬运、scope/duplicate/bot template、grouping/sampling/retention、resolved!=实际fix、Seer是候选原因，不用状态/模板推真实决定；trigger eligibility非结论/委托，可信配置与parent/recipient复核不授外写，不默认搜全部历史/访问私workspace。落原Trace/Source evidence，无第二why或bot。 |
| B2 external-tool-operation | PASS；H08/H09限缩合并 | agent/run/event/terminal/config/effective与observation/submission/run失败分开；done需实际terminal而finished非artifact资格；persistence/reload/inflight与backpressure按client保证；key形式非身份、explicit/env不同可信源；触发source/target/parent/recipient/permission闭合、unknown不盲fallback、marker只数据、不授code；stdio/HTTP secret去向/读者与注册不认证deployment。保现有permission/cost/partial/retry边界，不造新actor/gate或external-write方法；thinking事件无记录要求。 |

## 仍需的最小修

### N-HANDOFF residual · 只改Measurements第二句的条件

§Handoff parsing, measurement and environment现在写：`A declared quantitative claim that is being reused for the current object is re-run ...`。标题“where the claim needs it”和后句“不强每measurement”仍不能解除这句对**所有被复用claim**的必复跑要求。

反例沿原finding：固定对象/条件/coverage仍有效的既有实测请求计数记录，可以有依据地复用；恰因复用而必须再跑会取消前文claim/coverage复用规则。需要补核或对象/条件改变、不明时当然要实际重测；不是允许信handoff自报数。

最小修：改为“核所需对象/条件/coverage与来源；既有有效实测可以说明依据复用；**需要复测时**在对应fixed对象（非mutable clone）按适用比较重测”。保after-only复现不证before/operation/goal、tolerance/units/unknown与权限；不改其他已关子项，不建测试/测量gate。Source anchor已有when claim needs it，可相应精确到需复测时。

### N-H02-SOURCE · 只补design的实际swarm锚点

新增mode（coverage/race/mixed）、预声明selection、exact SHA/method、receipt gap、每必需slice聚合来自`pstack/skills/swarm/SKILL.md` §Phase A/Phase C。当前Source anchors仍仅列`pstack/skills/arena/SKILL.md`，却把这些一起写作其retained contribution，实际arena负责rubric/base/graft/synthesis，不是该覆盖/竞速规则出处。

最小修：在相同Cursor pin下列明swarm路径及Frame/Aggregate，区分其fan-out/aggregation贡献与arena synthesis贡献（可以同一行双source或分行）；保DEF2 H02与作者蒸馏身份，不doublecount，不新增方法或再改专业正文。不要挪动Matt显式pin或重开其已关finding。

## 消费、需补读与下一合法动作

Driver可串行集成本次8PASS整文件；harness H09不依赖handoff新measurement句，local-defect与test-evidence原互指无需复制权限/重写入口。consumer方法/README/Profile引用按固定core核，其解释/职责与PASS新增段相容。两held文件保上一通过对象与已关子项，勿以新整文件将held句装入；只修上面两处并送新fixed对象定向核即可。

文本PASS不等source runtime移植、当前SDK/forge支持、真实CI/UI/诊断/效果或全包接受。具体执行时仍需真实client/host policy、环境隔离、对应claim的实际观察与授权；本轮未执行源/外部动作。只写自有reviews，Driver集成/保全，gate不派B、不stage/commit。
