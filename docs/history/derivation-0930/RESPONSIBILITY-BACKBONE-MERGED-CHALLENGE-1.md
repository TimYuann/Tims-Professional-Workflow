# Backbone：首轮双评合并与第二轮委托

维护者：tpw-0930-oracle；2026-09-30。
状态：Oracle 独立评审与 Owner 转交的外部 GPT 独立 challenge 均已收到并合并；候选未接受／未冻结。
Owner 已授权将合并意见送给 tpw-0930-spine-executor，作一轮有界修订。以下是修订范围，不是所有建议已获 Owner 最终裁定的声明。

## 固定输入

- 首轮对象：RESPONSIBILITY-BACKBONE-CANDIDATE.md，150 行，已由 commit 6ad63b3 保全。
- SHA-256：94f49561ef8ee4c474494e1b80cf957b3cd1428cd7e8edb29949fc3992662610。
- Oracle 原始意见：RESPONSIBILITY-BACKBONE-ORACLE-CHALLENGE-1.md（O1、O2、S1）。
- 外部 GPT 意见来源：Owner 本轮完整转交；六点依次为正交轴、主动触发、三种状态、横向取舍权、Driver 足够性、组合冲突条件。
- 上层意图：docs/WORKFLOW-INTENT.md；原委托：docs/history/handoff/0930-spine-executor-BRIEF.md。

两方一致：保留六类判断与 Voice／Driver 分工，不重写骨架；本轮尚不足以冻结。
GPT 前四点是冻结前结构问题，后两点与 Oracle O2 一起补最小可判规则；不是无限留到未来。

## R1 · 两条轴与主动调用（GPT 1、2）

明确 A–F 是 judgment function；Security、Performance、Persistence、UX、Compliance 等是 professional concern。
同一 concern 可作用于多类判断；风险接受权仍来自实际委托，不来自专业名称或 D/F 索引。
不要把 concern 扩为第七、第八责任节点，也不要求每个 concern 常驻一名 Agent。

修正“只在缺结论或失效时召回”：任务／变更命中已接受的 applicability trigger，且要求的判断尚未满足时，应在依赖该判断的实施前主动调用。
例如租户相关缓存触发隔离判断、schema 调整触发兼容／恢复判断；触发要求的是判断，不必新开会话或做一套完整审查。
用少量有因果依据的例子说明，保留已满足结论的复用；不建立全仓风险清单或万能安全 gate。

## R2 · 三种状态与 Driver 的足够性（GPT 3、5）

明确 contract acceptance ≠ evidential verification ≠ action authorization。
当前契约被有权责任接受、证据支持何种结论、某实际动作可执行，须概念分开；可在同一产物有界部分说明。
沿用 schema 例子区分设计接受、代码验证、实际迁移授权，不造状态机、三个表格或三个审批阶段。

Driver 检查 procedural sufficiency：有适用版本、相关范围、有效 authority／接受依据、所需交付与未决冲突可路由。
专业依据是否充分属于 substantive sufficiency，由相应责任判断；Driver 可提出疑问并召回，不能替其作结论。
避免把程序项变成每次齐套材料；只检查影响本次继续的依赖。

## R3 · 横向取舍权与升格路线（GPT 4 + Oracle O1）

Security／Performance 等合法判断可能冲突；delegation envelope 应能指出共享边界的 trade-off / integration authority 及其裁量范围。
它可以是现有责任的一项委托，不新增 Integrator Role，不授予忽略硬政策的权力。
没有有效整合委托时，Driver 找上级委托来源确认谁能裁定，任何一方不因先到场而获胜。
只在冲突涉及人类保留边界时经 Voice；专业保留权、资源保留权不可默认都返回人类。
修正通用返回句与其镜像位置，保持同一套路线。增加一个横向冲突的短示例，区分可取舍偏好与不可放宽约束。

## R4 · 组合合法性与评价对象（GPT 6 + Oracle O2）

用组合失效条件定义边界，而非固定 Role matrix：权责冲突、要求真实独立性、自我接受／自证、注意力跨度损害专业深度。
标明“戴不同帽子”不解决以上问题；自我接受限制应指向相应候选／判断及既有独立性要求，不把所有局部自主决定一律做成外部审批。
Driver 在已有预设和约束内装配；组合缺能力或存在冲突时路由相应判断，不建立常驻资格审批平台。

明确设计挑战和实现结果评价各自的对象、作者／评价者关系、证据时点与覆盖。
设计被挑战过不能替代实际实现证据；实现符合 Plan 不能单独证明 Plan 的责任放置正确。
同一外部实例可在不同时间承担两项评价，但不能把自己参与形成的判断包装成独立挑战；评价复用须对本次版本／差分仍适用。
给一个已有契约局部任务、一个新增共享承诺任务的简短调用示例；不新增固定双 gate、三名 F 或 session 重命名伪独立。
保持现行 registry 的 A7/A8 纪律与三态不变；本轮只设计候选，不通过修订豁免当前规则。

## S1 · 共用接口压缩（Oracle S1）

统一说明只需本次相关、适用且足够的依据，可复用已有结论；缺无关材料不构成阻断。
四类边界夹具只改到能检验上述连接，无需重写整套案例。通用原则写一处，其他处引用，不每节补防御性段落。

## 交付与停止点

唯一写入：修订 docs/history/derivation-0930/RESPONSIBILITY-BACKBONE-CANDIDATE.md。
首轮已在 Git 可恢复，不另造冻结件／版本族。Oracle 持有上层 intent 与评审记录；你本轮不改它们。
输出标记为第二轮候选；双评收到不等于采纳，不自报通过。可在文末用短段落标明处理与仍未定事项。
优先重组和压缩原文，不逐项叠加评审条款；保留极简／优雅目标，篇幅按理解需要控制，不以硬行数凑完工。
不改方法真源、角色、技能、上游、脚本、A9 或原八项暂存；不 commit、push、tag、派新会话或启服务。
自查限于本轮语义与实际差分，不因只有候选文档修改而机械重跑四项方法检查；若引用运行结论，清楚写其对象与时点。
完成候选，短报路径及仍需裁定的最少问题，然后待命，等待下一轮两方 challenge，不自动连续修订。
