# Gate2 · Pro#1 001/003与低影响精确化

2026-10-03，tpw-absorb-gate2，非作者。**release/interface/trust三文件PASS；TPW-PRO1-001 CLOSED。performance需两句局部限缩，TPW-PRO1-003未关闭。002仍依其独立固定审单未决，不在本对象替其关闭。** 旧源族、已关finding、轮次与贡献保持；本gate不调用Pro。

固定对象 `054b30ce3b91b1c31ba535d1bf3007dda21fbec6`，唯一父/base `5d7d89d3f8fc295ed7c96e63a2af8952e75398ec`；actual diff仅四methods，diff --check无输出。对照PRO1-DISPOSITION 001/003及其低影响建议，读fixed相关正文/直接依赖，不读mutable或重新全库审。回源资格沿已直接核Addy `2686b620…` performance/shipping与Cursor `ecc249f1…` schema/refine/probe，此次直接核源performance的“3%/±5%”原句与probe-models全文；低影响建议不升新must-fix。

## 文件级结论

| 文件 | 结果 | 理由与边界 |
| --- | --- | --- |
| release-and-recovery | PASS；001 CLOSED | deployed/enabled/observed-or-verified usable/shut down分开；观察带对象/version/path/time/conditions/evidence或gap。接受是有权责任方/有效规则对明确对象的动作，记录acceptor/rule/time/scope，不从F PASS或“看起来能用”推接受；有效委托可接受，不默认Human。观察与接受字段分别记，不建状态机；后文观察与风险/发布权限保持。 |
| trust-boundary-and-actions | PASS；低影响精确化通过 | 删除不存在独立dependency-upgrade guide的存在性承诺，指change-review的真实dependencies/assumptions/findings disposition与本文件install边界，不复制程序/权限。probe源定位到实际`scripts/tools/probe-models.ts`：create/send后记ok、cancel异常吞掉的承重代码存在，仍只支持accepted≠completed/吞error≠cancelled；未运行probe、未认证model资格。 |
| interface-contract-and-retry | PASS；低影响精确化通过 | §3以shape-only检查/生成视图与runtime refine/superRefine实际能力分开，后文明确Plan runtime图检查不自动进入generated artifact；不再用“schema全类别不能跨字段”否认已知runtime能力。按该段shape-only上下文消费，不将所有schema/generator都认证或否认。无新validator或schema adopter政策，Oracle旧源裁不重开。 |
| performance-and-neutrality | 大部修复通过；003仍有局部残余 | 样本量/配对相关/可比性/混杂、usable estimate与价值阈值分开、inconclusive非产品FAIL、按预算continue/defer/revert、可靠性/正确性独立目的、无统一统计工具/N均正确；但新增band句仍从原spread推出证据不足，且repeat必要一概化，见下。 |

## 001 条件证据（纸面判读，不宣部署）

- **已观察、未接受**：对象build H、路径P、时点T、条件C下canary/关键流观察通过，record可写observed H/P/T/C/evidence；保留接受未发生，accepted记录为未发生/待相应authority。不能以F PASS填acceptor或授发布权。
- **契约已接受、实现未观察**：接受的是契约K/version V，由实际B/C接受委托或既有效规则记录时间/scope；implementation build H尚无运行证据，其observed为未核/gap。K的接受不是H可用证据。正文已明确对象种类/范围，不把这两项折成“accepted实现可用”。

这与fixed Backbone的contract acceptance≠evidential verification≠action authorization≠task closure、title不产生接受权直接一致；字段只是已有记录内容，不新建接受actor/表。

## 003 算术与相反案例

按Pro hypothetical既定条件计算：两独立可比组各n=1000、均值100/97 ms、SD各5 ms，`SE_diff = sqrt(25/1000 + 25/1000) = 0.22360679775 ms`，`3/SE = 13.4164`。本gate只用短自有算术核值，未采样/跑分；结果不是普遍N门槛、固定检验法或因果资格。

- **原始分布重叠但估计可用**：在独立/可比/无实质混杂的明确条件下，3 ms mean difference的不确定性可远小于原始5 ms spread，能支持这个受限平均差claim。是否值得keep还看接受的收益阈值/维护成本与其他目的，不由13.4 SE自授决策。
- **均值看似改善但估计不成立**：样本过少、相关结构未处理、冷/热cache不一致、另一个变更/负载同时变化等，可产生均值移动而不能支持所称效果。报告improvement未成立，按已有预算与目的继续/暂缓/回退；不产品FAIL、不因貌似mean更好自动keep。

正文两个条件例及决策表大部能区分上述情况；source的过强原句不能因忠实于Addy而免责，此次修订应保其拒绝记录。

## 003 残余最小修（仅§Verify新增bullet）

1. **band仍被赋予证据不足的结论**：新句“3% inside ±5% ... not by itself verdict no benefit: **it says the evidence as collected cannot establish the improvement** ...”仍由两个裸数推出cannot establish，与后面的n=1000算例直接冲突。最小修：**仅凭这两个裸数不能判断改善已建立、未建立或无收益**；需要效果估计/不确定性与设计条件。不应把“不够信息判断”写成“已判断证据不足”。保usable estimate与实际价值两轴，不全文重写或新统计gate。
2. **Repeating is necessary过宽**：同一bullet新写“Repeating the measurement is necessary”，未限定有噪声/估计稳定收益claim，与同文件已过Ground条款“固定输入一次计数可以支持窄count claim”直接冲突。最小修：按claim、已知噪声/变异与coverage选择所需重复和设计；对需要估计噪声/稳定收益者取适当重复，确定性窄count观察不一律要求额外run。保无fixedN、统计效果不确定性/混杂、已有授权/预算stop，不重开旧单run finding或ABC8源族。

memoize例需沿此解释：其“this sample effect not established”是案例已知的估计/设计不足，不能仅由±15 spread推出；可把该案例假定的不足写明，或去掉spread作为理由的歧义，不另造实验。其他decision/complexity/other-purpose已改内容保留，不因这两句重做。

## 交付与下一合法动作

Driver可逐文件串行集成release/interface/trust三个PASS，保001上述条件例与算术证据给Oracle；performance待上述两句的fixed窄修后定向核，003暂不关。002的只读query残余依独立review处理，不能由本四文件PASS代关。当前文字资格不认证真实统计设计/Provider/production/部署或全包接受。只写自有reviews，未产品写入、派B、stage/commit或扩大审查。
