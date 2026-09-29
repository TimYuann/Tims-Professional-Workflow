# 0930 · 旧组停止与新组接手回执

Owner方向：`0930-stop-and-next-wave-BRIEF.md`。旧组有限closeout：`20e9be5:docs/history/handoff/0930-old-team-CLOSEOUT.md`；该文件sha256 `d29836ee2c497c4a6a22c6007afcfe0df20c62866581fc6d5ed7da38eebd61ef`。

Oracle 已直接核旧 Driver、Scout-b、Adversary-b、Scribe-b 停止ACK；旧Driver确认无在飞写入/派工/自动续作，四会话保留为待命，不再推进。Scribe工具限制保留，不修、不伪称职责全部完成。
方法对象 `8d800ecf67c3e4a3da1b87e4a64f664785dfd90c`，tree `d687773a60b5f6a7d1627e686ef8fd08c15d8a73`；`20e9be5`仅新增closeout，方法/入口路径未变化。Oracle独立四检查exit为0/1/0/0，closure 20 PASS/1 FAIL（C1无tag）。旧Driver的无.git干净导出观察为20 PASS/0 FAIL/1 SKIP；不将其升级为所有方法或正式release已验证。
closeout的旧计数仅作快照：按 `git diff be91e15..20e9be5` 的方法/入口路径实际为15，不能用“11文件”替代实际manifest。来源候选与旧18静态状态仍待处置，不混成已采纳。

## 新组的实际身份

| 角色 | Herdr名 | pane | Pi session ID |
|---|---|---|---|
| Driver | tpw-0930-driver-c | w27:p7 | 01a0ef44-4714-710b-a3f7-b44f933d2612 |
| Architect | tpw-0930-architect-c | w27:p9 | 01a0ef44-9c6a-707d-bf04-d82541720978 |
| Scout | tpw-0930-scout-c | w27:p8 | 01a0ef44-ac63-7340-898e-af808fca7edc |
| Adversary | tpw-0930-adversary-c | w27:pA | 01a0ef44-bb9f-72b3-b3bc-1c88c534338c |

独立新会话，均Pi/minimax-cn/MiniMax-M3.1-Flash-Preview/high；角色先compose并以append-system-prompt注入。新Driver已核环境、Intercom身份及三worker双向ACK，自包含上下文可达；初始地址/暂存计数误述已在bootstrap纠正。四个ID前8位相同，使用完整name/ID寻址。
布局新tab w27:t6／t7各两会话；旧tab仍为2/2/1。Oracle tpw-0930-oracle @ w27:p6只收里程碑，不是Intercom endpoint。

## 切换后的第一段授权

新Driver接收协调责任；第一里程碑是Owner指定的G（本仓治理/上层说明）与P（核心workflow优化）的现状、最小设计、两线边界/依赖、可判定停止点和真正缺决定项。新worker可作有界事实调查及候选设计，过程材料按本仓现有history落点保存；正式治理真源/核心内容实施先有固定方案与独立评价。不继续旧组的无限吸收队列，不自动视全部历史候选已接受。
原8暂存保留；旧dirty/未跟踪成果按closeout指针保全，不混入新组commit，不覆盖其冻结字节。新Driver先接受这些既有状态再派活。flat `skills/*.md` 是当前库的文件形态；没有 `SKILL.md` 本身不证明缺技能或需全量转换，加载适配问题须按真实能力查。
本回执只存本次换班事实；后续治理方案由新组确定唯一权威记录，不把这张快照长期维护成第二活名册。
本次不tag/push/发布，不更改UCBIP治理或业务；稳定release就绪再由Oracle通知UCBIP一次。
