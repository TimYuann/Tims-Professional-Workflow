# REVIEW-B2-a64bbc2

tpw-absorb-gate，2026-10-02。candidate `a64bbc224a135b38e806853212d361e0249fc7ab`，实际父`c81c43ba0760f1101ae29ebcaa560b72df52b058`，core tree `7497df8bd851320eb578ff05f6603d8cbfbb370a`。审查新增范围`b8b1d28f1a50be3f2954c69d17b59fce2435951b..a64bbc2…`七文件，另确认实际父差分只含elicitation prototype三处相关行；git diff --check通过。固定Git字节，未用作者mutable工作区。

结论：**原rationale/CLI两项关闭；新增A3-DEF正文PASS；prototype上限R4还有一处残余，整笔暂需修。** 原第一批3项仍关闭，不重开其已审变化。源依据复用本轮已回读的Matt research/wizard/template/teach formats/writing、architecture survey及Cursor prototype/epistemics，对本次新段与反例独立比较；我未代写。

## 关闭项

- rationale第9项改为task/承重claim/resource选择来源，无需证明绝对irrelevant；未查/不可得/已足够都有真实理由与coverage，未查不假称empty result/Unknown已搜。Source evidence新增primary不自动可信、版本/时点、fact/decision/引用与行为证据分开、无mandatory背景agent，符合DEF-6。
- CLI缺`--tag`、error、修复命令一致，non-TTY不等待的例子可区分；幂等/半途失败/preview行为条件未弱化。

## R4-rest · 实际来源已说明，末句仍有一律不证明的上限

`methods/decision-elicitation.md` §18已按实际input/runtime/真实或替身dependency说明证据，这是正确修复；但仍说controlled green不能建立“a real-provider…or end-user experience”任何claim，§22又说“it is not proof of production behavior”。这两处仍可能排除**原型确实执行过**的窄真实leg，而不只是排除没有执行到的全域claim。

反例沿已裁：在有效授权下，prototype用固定SDK真实调用provider读取某record，能支持该版本/输入/观察到的provider路径与mapping；真实页面的窄交互也可有该环境下的实际体验观察。它们不证明全deployment/全部输入/scale，也不让artifact生产qualified，但不能因prototype标签把已执行的real leg说成无效。

最小修：将上限限定为**未实际观察或超出覆盖**的provider/部署/用户/生产全域claim；某claim的real leg实际执行过可支持该部分，未执行不能用controlled fixture替代。§22保留artifact≠生产交付/发布与观察覆盖界限，去掉“任何production behavior都不能证明”的读法。只改这两语义，不要求新experiment/放宽网络或数据授权。此项仍是原R4，不新设method gate。

## Batch4已通过对象

`architecture-survey.md`、`human-procedure.md`、`professional-learning.md`、`rationale-and-premise-review.md`、`agent-facing-cli-contract.md`、`guide-agent-text.md`在本candidate的**整文件正文PASS**；既有behavior-contract-examples/bounded-composition/Profile指针原通过内容可复用。

human-procedure保每值source/destination/sensitivity、真实UI不发明、static trace不冒e2e、helper不证明安全（KEY=value/EOF/partial/permissions/actual target），不实施CI secret/migration动作；learning仅显式专业学习任务调用，coverage≠掌握/selfreport≠展示、difficulty只是未经当前实验验证的启发，无默认course/认证/评估gate；agent-text增补受众concept/材料与论证分开/缺fact不虚构/读盘保人在飞编辑，无逐段OwnerACK。未要求新的project平台。

**同路径归并：**architecture-survey与B1同机制同路径，采用本B2固定48行版本为共同canonical，B1版不重复安装/计数；裁定理由见REVIEW-B1-57b4aad。professional-learning引用professional-explanation，后者正文PASS但handoff目标尚需修；Driver按消费依赖串行一起固定。其余方法的真源引用可从源身份与section恢复，不要求搬入全源仓。

Driver下一合法动作：可集成独立通过文件；elicitation新版本留待R4-rest修好固定后复核，相关Profile目标通过后再同对象消费。无须重审所有来源、给每知识点写test或把现有scope检查升为通用validator。本文不证运行效果/fresh-reader/最终整体接受。
