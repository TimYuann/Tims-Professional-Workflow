# 夜间编队启动委托

Owner 已授权 2026-10-01 过夜纯自主推进；外部 GPT 一轮计划 review 已吸收，不再等外部评审。执行依据：docs/OVERNIGHT-WORKFLOW-PLAN-2026-10-01.md、docs/RESPONSIBILITY-BACKBONE.md、docs/WORKFLOW-INTENT.md 的新目标。
本轮从零开发，旧 AGENTS 的旧角色装配／registry／阶段规则不作为新包设计约束；上游只读、保护成果、独立判断与 Git 可逆性保持。不要读旧 history 或旧角色 prompt 来定义本轮职责。

## 本次实际委托

工作树 /private/tmp/tpw-night-20261001，分支 night/2026-10-01-workflow，起点 496b067。只开发 professional-workflow/ 新包与 docs/overnight/2026-10-01/ 本夜过程证据。
Oracle=tpw-0930-oracle(w27:p6)，只里程碑与真正边界争议。Driver=tpw-night-driver，Codex gpt-6-luna/xhigh，位于 Oracle 右侧。
Driver 管计划推进、依赖、任务 charter、消息及单一集成写入，可在本分支 commit、接入自有 worker delta；不能把自己的候选当独立接受，不是专业裁定／风险接受的万能 owner。
Owner 已明确不需逐阶段询问。专业候选由独立实际会话评审，Oracle 根据接受范围与证据在里程碑接受；纯机械范围内动作不等待 Oracle。保留动作停相关项，其他继续。
07:00 前停止增加研究和新范围，保留最终冷启动/回退/报告窗口；目标08:00晨验。实际用时/费用可取就记，不伪造效率。

## 写入与通信

共享产品配置由 Driver 作为物理集成者串行写；worker 可写明确不重叠路径或在自己的分支交 delta。并行前由 Driver 明确实际写集，禁止 git add .。本分支根目录遗留文件只读。
过程状态唯一在 docs/overnight/2026-10-01/STATUS.md，由 Driver维护；决定 append-only 记 DECISIONS.md。证据按对象引用，不另造脚本平台。
跨 Codex/Pi 用 Herdr短消息与产物指针，名字每层一致。报告完成不是自己验收。禁止绕过批准/沙箱或写入UCBIP、操作其服务、push/merge/tag/发布。
只用获准三配置：Pi commandcode/deepseek/deepseek-v4.1-flash/max 适合清晰并行任务；Luna/xhigh 关键确定性执行和Driver；Sol/medium 除Oracle外最多一个，仅关键判断，默认按需。
Oracle/Driver tab至多两agent，其他每页四agent；起会话先核真实model/effort。工具故障一次有界诊断后可换另一个获准配置，记录实际配置。
原工作区 /Users/yuantian/Developer/tim-professional-workflow 只读，旧dirty/staged保全于 /private/tmp/tpw-legacy-preservation-20261001，不纳入本分支。

## 首轮推进

Driver 先核Git、创建简短STATUS与DECISIONS，按计划M0-M6持续推动，不等待逐步派工。马上委托 Flash 完成M1 Profile候选、五来源只读索引；后者只做身份/方法索引，不自行采纳。
M1 新Profile先有适合责任的心智模型与常见误区，M2 Charter绑定本次权责，M3真实任务不得泄露预期路由答案；同一Profile需两个不同Charter。
固定演练rubric由独立evaluation担当预先保管，与实施输入隔离；提供目标、真实结构与约束，不发预期解题路线。
M4改活跃语义必须标相关M3coverage失效并定向重验。脚本只因真实采用需求/已观察机械成本进入，不替代专业判断。
有阶段接受材料时用短Herdr提示Oracle并给自含文件路径；不要高频轮询或让Oracle转发普通worker消息。继续可并行无依赖工作。
完成M6固定commit/tree、core包/manifest、真实样例证据、冷启动/回退、UCBIP只读adaptive说明、残余和晨验报告，按夜间closure rule结束。
