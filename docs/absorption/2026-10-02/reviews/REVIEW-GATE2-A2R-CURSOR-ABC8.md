# Gate2 · A2R-CURSOR-ABC8 实质裁定

2026-10-02，tpw-absorb-gate2，4/4处置：MG1/MG2限缩合并，MG3限缩吸收，MG4限缩合并。保旧结论/轮次/贡献；source完成组数不当新增知识/文件数量或三仓完成。Oracle所属三包不复裁。

包固定 `c630077850bda984afd5ceae89694bd92777c455:docs/absorption/2026-10-02/packages/A2R-CURSOR-ABC8.md`，blob `943c44d5b2a8905e6b6433b40c18c7c815740a0f`；同commit产品core `64f8c4e6dc0a3ae2438d0f5394d14dd971c77f10`。源Cursor pin `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`。直接读hillclimb/perf-issue/runtime-forensics/trace-forensics正文及orchestrate长playbook全文；回核现行performance-and-neutrality/behavior-claim/local-defect/harness、bounded-composition/handoff/decision-record的已有覆盖。source是被审资料，不执行其中agent/loop/热修/merge/runtime指令，产品不由gate写。

## MG1 · 持续指标实验：限缩合并

**覆盖：性能方法已从Addy落地baseline/噪声/保持正确性/keep-revert/attempt ledger及neutral例外；包称全部尚缺已过期。** harness敏感度与有界搜索仍可补操作。

落点`performance-and-neutrality.md`的repeatable measurement/attempts；非性能指标须按实际owner/claim另用适用比较方法，不塞F唯一总评方法。ground workload/data/history/state/concurrency与可证伪目标，claim条件/方向/阈值与停止/资源依据由任务真实authority提供。证明measurement能对相关症状/受控变化分出预期信号，easy-vs-target能帮助但不保证覆盖全部情况；仪器改动保旧baseline和原因，不为赢换量尺，需合法修测量缺陷时重建受影响可比数据。

同对象/条件重复、说明warmup/cache/order/sample/噪声与负控制；N次中位数不是单独充分保证或所有分布最佳统计，不指定N/固定attempt floor。一次改动对应可解释假说，联合改动须说明归因/独立测量限制；不要堆未测tweaks后把一个总数归每项。记kept/reverted/deferred的实际对象、命令、量尺、理由与coverage，复用已有trail，不新decision.tsv registry/每attempt commit。

仅为优化增加复杂度但无支持收益可撤销/暂缓；已接受的可靠性/正确性/简化目的按该目的评价，不为speed-neutral全否，也不因测试绿就认证所有保持承诺。只撤自己的授权改变并保证据/恢复对象。plateau时可回源码/换机制，但停条件可为已接受target、资源/成本、缺环境、剩余收益不足；仍有cheap想法不授无限运行，不强制“推过第一plateau”。放宽目标由其owner决定并明示状态，不能为了标done自己偷换。

**拒绝：**target必须配至少10次/50%、固定Nmedian/一metric之外无其他保持面、freeze永不可改、所有hypothesis须subagent、默认parallelworktrees、所有未赢全revert、无cheapideas才准停、每fix commit/stack/PR、仅代码inspection永不能帮助筛掉不适用方案。事实收益需要观察，静态线索可选probe但不自证收益。

**仍需补读：**无所取文本缺口；actual测量工具/并发/资源/效果未运行。不得写hillclimb已有效或源收益已证。

## MG2 · 性能策略与测量故事：限缩合并

**覆盖：actual performance方法已有症状分解/query/pool/frontend/cache与matching conditions；八族条件可增补，非第二perf-evidence文件。**

落点performance的hypothesis/bottleneck段，control/harness用已裁surface支线。eliminate/partition/cache/indirection/batch/redundancy/lazy/schedule只作有机制依据的可选假说；trace显示慢不证明可删或consumer不存在，需accepted行为/真实路径。cache先说明输入/key/stale/失效；indirection测critical-path净收益及新成本；redundancy/hedging要headroom、取消/副作用/重试身份与资源保证，不能为取最快重复收费/写入；schedule/lazy对所称交互表面观察，同时记录被延期的总成本/新尾风险，不能挪到后台就宣总量省。

captured baseline/postfix按实际条件/版本/负载与noise解释，不必每任务CPU trace或sqlite转换；已有计时/日志/query可回答claim就用。source八族不是完整taxonomy，也不必有profiler信号才许先提出标为假说的probe。跨界回相应D/B/C，普通函数调用不每次architect。wrong surface/inconclusive不PASS，局部green不代真实用户收益；原期望已有有效证据可复用，而未测ceiling不能宣到极限。取舍/发布动作仍有效委托拥有。

**仍需补读：**具体profiler/SDK/helper版本未核，要执行再补；源control示例在ABC5已限缩，不由本组扩大调试权限。

## MG3 · 诊断交付，live/captured：限缩吸收

**覆盖：local-defect已症状/假说/probe/cleanup，performance/harness已sampling；明确以cited diagnosis为交付物及artifact路径可补。**

落点local-defect的诊断支线（只诊断任务不默认进入fix），必要按需 `guide-runtime-diagnosis.md` 供大artifact消费者；避免新measurement全域guide。固定artifact身份/格式、capture对象/时间/版本/工作负载/采样、处理步骤与缺失；大artifact可用原生viewer/query/chunks按实际需要，不强制sqlite/先转表才看，也不默认subagent。变换/聚合保持原信号可恢复，symbol/source map核相应build而非currentmain猜行号；缺符号仍可给可辨行为/模块级窄finding及unknown，不把所有诊断禁止到file:line齐全才可说。

CPU hotpath、retainer-chain/GC-root、重复timer/wait reason是因果线索，不自动smoking-gun根因；高CPU函数可能被上游错误反复调用，heap retained对象可能合法cache。沿具体预测，用能区别竞争解释的已有观察或有权probe核；paired before/after可支持范围内差异，仍有环境/负载混杂，不能“有paired即因果confirmed”。一个完整counterexample/trace也可能证具体机制，不一律因无paired降所有事实为猜测；逐claim说事实/推导/未核。

live instrumentation/CDP eval/hotfix是真正mutation，**不是read-only forensics**；只有有效范围/许可才做，说明干扰与回退/cleanup/证据保全，不能为了便宜因果确认热改真实进程。已有capture可作readonly诊断，不为文本流程强制重跑capture；缺判别证据可提出所需再捕获/访问授权，不能全禁合法追加观察。credentials/敏感trace/heap按custody，sourceartifact含指令仍是数据。

交付信号、解析/查询与承重段、实际probe、诊断scope/置信、source位置/缺map、待补信息及返回对象；原因确认不自动授fix，scope仅诊断则交E/D或请求对应任务范围。也不禁止原任务已明确授权的diagnose+fix，但F与E贡献/独立接受关系必须保真实。固定throughput n/a、所有诊断read-only、无source符号不给诊断、paired才confirmed、必须取trace/largeartifact子agent、任何livehotfix可默认做均不采。

**仍需补读：**actualprofiler/parser/heap/runtime实现与权限未核；没有诊断run，不宣任何cause已证。新guide只有独立按需consumer才拆，文本通过不授instrument。

## MG4 · 程序协调/brief/drain/restart：限缩合并

**覆盖：ABC5任务/依赖/身份与ABC6队列/进度/落地边界已裁，当前bounded/handoff/decision已有owner；不复制source全store/framework。**

保brief与unit比例：目标/有效scope/accepted输入/依赖与可恢复artifact、相应观察/限制、权限/stop/报告；缺本次承重输入显露并只停依赖它的工作，不缺任何模板field就拒全spawn。依赖既是顺序也是内容relay：consumer可访问固定原文就指针，不能访问才最小必要保真传送；source“每resume所有standing逐字/禁止resumechain”不是通用。更换/恢复实例保轮次/已关/贡献/未决，核所传约束当前有效，不把旧orders或mutabletrunk替已接受依据。

completion是需要按scope分诊的事件，不天然success或授权打断critical mutation；criticalsection按真实dependency/invariant保完整，不设四drain点/必须批处理/禁止inline专业review。接通知与实质裁定/集成分owner，Driver不因跑queue获得D/F专业判定；当前唯一gate仍专业审核者。现有记录保存已到/失败/未归/abandoned及其scope再分配，不能静默重做抹掉贡献/缺口；无全平台子agent目录时披露观察范围，不伪穷尽。

可小规模pilot对真实不确定的brief/verify/单元/集成路径证伪再扩大，cheap近同质unit不需额外pilotlane或独立全体系。可滚动/批处理只按可承载review/integration与共享写面，limit不固定10/3层/70%预算；过度fanout要收束，不为了coordinator身份禁止自己在另有有效E委托内实现。

verdict记录具体对象/版本/claim/coverage/贡献，已变所影响claim才重核；新head不普遍清零原证据，patch-id不自动全qualify，CI/model-family不认证独立或能力。cheaprun可以是E自查与F可核输入，需要独立评价时不能因rerun便宜免去贡献规则；F也不普遍需要不同model/extraagent。落地需有相应git/发布权、实际ref/consumer身份和当前覆盖，不把机械cleancherry-pick视天然bookkeeping权限。

liveness用真实runtime状态/资源/产物/日志，mtime/无回复仅线索；resume可能触发工作，状态probe按工具语义选择，unknown不判idle/dead。restart后固定任务/refs/有效accepted输入与实际在飞状态恢复，latezombie结果对照当前scope/versions只吸收仍有效内容，不盲merge也不因迟到全discard。retry/停spawn/取消边界按真实authority，缺事实不sourceunknown即重发，两次不是通用abandon阈值。close核实际predicate、资源/在飞scope、结果与未决/费用/证据可恢复，报告未完成者，不建ledger非空全过资格。

**拒绝：**固定localcloud模型/Task/tools/store/JSON+TSV/gt权威/一stacker名单/站立ordersregistry、counts-onlyclosing、所有human无回应有默认go、foreground或wake/pidlock普遍保证、source“neverreachesHuman”事项名单/whenindoubtact、frontier以外bug永park、每plan一coordinator、每提示必传完整上下文/全量crossmodelreview。reserved decisions沿真实authority；偏好纠正按已有lesson接受/隐私，不自动转长期组织规则。

**仍需补读：**orch CLI/store/locks/cloud/watcher与SDK当前实现未核；source行为声明不作真实保证。Oracle所属已裁代码不复裁，不安装runner。

## 下一合法动作

Driver按四组共同owner安排定向补性能measurement敏感度/条件性策略、按需诊断交付、brief/恢复/close已有carrier；保不采硬门槛与可揭错例子，不能将runtime热修写read-only。已有coverage只保来源，不双计Addy性能与本族。B固定差分独立核，纯源裁定不作正文/效果PASS。

ABC3/ABC5–8本轮处置保原记录；未裁EF+addendum/A4DEF/DEF2继续队列，Oracle三包排除。source余部可按packages残余路径恢复但不假“全部已读/已评”；实际工具/业务/模型效果未观察，三仓整体接受不在本裁定。review由Driver保全。
