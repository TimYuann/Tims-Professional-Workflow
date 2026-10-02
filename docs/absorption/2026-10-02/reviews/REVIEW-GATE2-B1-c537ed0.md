# Gate2 · B1 c537ed0 固定差分复核

2026-10-02，tpw-absorb-gate2，唯一接班专业审核者；非候选作者。沿用 REVIEW-B1-57b4aad 的轮次、贡献关系和已关 finding，不重新裁 Oracle 的源包。

对象 `c537ed042b25abc601774cb1ada671496fbd8e6f`；比较对象 `57b4aad0e7cecac8b82d1adcfdfe6b2f3f50177d`；共同 base `d3aab6ad30f36789664287f304e4e91ffd61d96a`；core tree `3fa76ffd52ab428259f32230b64c8d54a04f9a77`。实际 delta 八文件 +87/-18，git diff --check 无输出。仅用 git show/diff 固定正文，不读取作者 mutable 更新。

## 结论与保全

**旧 R1-rest、D1 关闭；R2/R3/R4/R5 继续关闭。七个 delta 文件 PASS；domain-state-and-invariants 新 J1 段需一个定向边界修复，整笔不可无差别采用。** 先前 PASS 未改内容继续有效；architecture-survey 仍采用 B2 的 canonical，不改既有去重结论。

| 机制 / 文件 | 覆盖与复核处置 | 理由、边界及落点 |
| --- | --- | --- |
| handoff-and-resume，R1-rest / R1 精化 | 修复 PASS，关闭残余 | beliefs 句改为误把未核报告当事实的风险；必要 claim 按固定对象/实际覆盖核，保已有有效接受，不要求接收者免核。真实执行覆盖与 UI logic / experience 分开，无必选五等级。 |
| local-defect-feedback-loop，D1 | 修复 PASS，关闭 | 暂定假说可选 probe，不能冒充已证根因；未复现如实报告观察/限制；最小化按区分力与成本停，不需证明全部元素不可删。负控制仍有实际作用。 |
| change-review，R4 精化与 ABC4 MG2/3 | 合并 / 限缩的落地 PASS | context 提供者不变接受者；F 贡献按 Charter；reviewability 是输入，描述须核对象；comment/suppression 判断只读、有授权才动作，负类型测试可保，未知保提醒。拒绝 delete-on-doubt/内部 why 全删/固定重跑。 |
| verification-harness-design，R3 精化 | PASS，旧关闭保留 | 明示 pass 的 feature/claim/recipe 范围；source-only 不升 live，适用真实 leg 未执行即未核；不恢复全 feature 强制。 |
| decision-record，C2 | 合并落地 PASS | 匹配现有格式/序号、冲突显露；候选不记 Accepted，历史 supersede 保全，规则正文仍唯一源。四问限于所写记录，保最短形式，不强迫长模板。 |
| change-slicing，C8 | 合并落地 PASS | 依赖落实到结论/接口/写面/资源；vertical slice、早探未知与 checkpoint 按真实图及 claim；无固定层序、全测、人类 ACK、数量/时间门槛。 |
| guide-lesson-promotion，ABC4 MG3/4 | 合并落地 PASS | 同约束由新 carrier 兑现且已核才去提醒；优先更新并保有效约束；同事件不双计；学习仅显式任务，表达/检查复用原 owner。professional-learning 实際反馈补正文不在本 w1 delta，留 B2 对象另核，不假记已落地。 |
| domain-state-and-invariants，R2 精化 / DEF3 J1 | R2 精化 PASS；新增 J1 局部需修 | 结构/语义、名称/身份、生成物/运行检查、关系/独立性区分正确；但见下列新边界 finding。不重开 Oracle J1 源裁定。 |

## 新 finding B1-J1-boundary（不是旧 R2 重开）

`domain-state-and-invariants.md` §Illegal states and referential integrity，固定正文 L32/L34：

1. “before anything consumes the data” 覆盖了诊断读取；Oracle J1 明确允许隔离坏行的诊断遍历，并要求披露缺失。反例：图有环，诊断器读取它以输出字段路径/环；不应因语义未通过就禁止诊断消费。限缩为依赖这些不变量的执行/安全决定前检查；诊断部分读取可用，但披露范围，不推出全图安全或全终止。
2. “A sentinel string in a domain field is not a valid state” 及 rendered artifact 中 residual placeholder 必须失败仍过宽。显式合法枚举 `unknown` 可以是协议状态；示例文本 `{{customer}}` 可以是文档内容。只拒冒充已填值的未完成结构占位符或未声明 magic absence，不拒合法域值/字面量；检查须区分模板结构与插入内容，不能二次解释用户内容。后句允许合法 template-like text 尚未限缩这两个前提。

最小修仅此段，不新增工具、schema 平台或 guide；保留结构绿/图错、名称不等身份及生成视图覆盖的反例。其余 domain-state 正文沿用通过结论。

## 独立回源与限制

核三源 HEAD 与既定 pin 相同。实际读：Matt diagnosing-bugs 全文；Addy documentation-and-adrs 正文及 planning-and-task-breakdown 的依赖/切片/排序段；Cursor no-comments、comment-sicko、deslop、principle-model-the-domain、maintain-verification-skill、teaching 两 SKILL 正文，technical-writing/automate-me 的承重条款；orchestrate schemas.ts 1–380（Plan superRefine）及 590–640（部分读取），prompts.ts 1–105（替换/残余匹配）。候选八文件 delta 已读，handoff/local-defect 受影响正文与 Limits 回核。输出截断的上游尾部未冒称全读；旧已裁源结论按其原 review 保全，不用摘要创造新源资格。

无需补读即可作上述定向裁定；若新增 SDK/runtime 安全或效果 claim 才须补相关实现/实验。未执行上游流程、SDK、Provider、业务或读者实验；文本 PASS 不等于效果/授权/整体接受。

Driver 下一合法动作：串行采用本对象七个 PASS delta 及既有通过文件，保 B2 architecture canonical 与跨分支消费依赖；domain-state 新 J1 段由原作者定向修后交新固定对象复核，其余旧 PASS 无需全量重做。review 提交/共享台账由 Driver 保全，本审核者不抢共享 Git 写面。
