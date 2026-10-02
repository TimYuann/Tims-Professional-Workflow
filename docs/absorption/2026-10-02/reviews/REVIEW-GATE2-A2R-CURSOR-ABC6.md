# Gate2 · A2R-CURSOR-ABC6 实质裁定

2026-10-02，tpw-absorb-gate2；6/6组处置：MG1合并，MG2/3/4限缩合并，MG5/6限缩吸收。非6个独立新增文件；既有ABC/ABC2/ABC3/ABC4/ABC5结论与贡献保全，Oracle所属源包不复裁。

包 `246ed8ba2725f60700fce9760a3ebc1efbe1967b:docs/absorption/2026-10-02/packages/A2R-CURSOR-ABC6.md`，blob `accb08579a07dff341acc6d2c6ad4eb1740014e6`；产品同commit core `01514a3918dbf5a08d47b2f8e046c30e6ee0ee82`。源 pin Cursor `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`，legacy只读。直接回源七个playbook opening-a-pr/shipping/babysit/autopilot-full/autopilot-stack/eval/worktree-cleanup 的承重正文及make-pr-easy-to-review；截断的autopilot起段/babysit尾另读。比较实际change-review/change-slicing/handoff/guide-change-shape/professional-explanation/lesson-promotion/bounded-composition的覆盖，source模板21文件旧基线不继承。未运行forge/watcher/云实例/eval/清理或源script，未派工、写产品。

## MG1 · 可审交付形态：合并

**覆盖：大部充分。** 当前change-review的Reviewability、guide-professional-explanation、agent-text与change-slicing已有真实对象/what-why-impact-evidence、可发现性、窄单元与诚实序列。不是缺一套强制PR五段标准。

**采纳/落点：**review输入与表达各回原owner；变更说明按实际diff说问题/结果/影响/证据/有意义的取舍，rename/retarget需说双方及实际消费；核心与generated/mechanical可分展示，但不能隐藏有意义的cleanup/依赖/import/行为变化。说明无法补救不可审的耦合与规模时按真实边界建议拆分，独立可交单元不按固定“五PR优于一PR”。commits能说明顺序/可恢复证据，但每commit不必就是未来PR或保持单独绿色。

状态取实际forge对象/版本；draft/ready是其流程状态，不是专业通过、授权或已部署。创建/编辑/发布PR都需既有有效许可；观察阶段与实际落地分开，开PR不自行扩大为持续watch/merge，也不一律要求整栈后才能观察关键阻断。沿一致forge身份/语义核状态，不混平台auto-merge标签。

**拒绝：**main/worktree/常规reset-hard、自动amend/rebase/force-push、ready绝不draft、固定40行/五section/标题标点/语言黑名单、删所有SHA/方法学/metric表、每commit独立comment reviewer。固定对象/样本/版本若承重可直接保留，重复日志可链接；不可为简短隐藏限制。历史整理必须已有授权/回退及内容核，source make-pr明确需要requested/accepted而非自动拥有。

**仍需补读：**无所取文本缺口；forge工具/PR schema/runtime未核，要实际发布时核其当前接口。不开新reviewable-delivery重复guide。

## MG2 · verdict对象与落地链：限缩合并

**覆盖：fixed对象/真实独立性/验证≠权限充分，base漂移后的适用性可具体化。**

**采纳/落点：**change-review的fixed-object/evidence复用与handoff消费；实际依赖链并change-slicing/bounded-composition，不新建shipping授权平台。verdict带被评head/base、依赖/运行环境与claim coverage；重base/retarget/上游集成后核真实diff、接受输入、构建/依赖/配置/执行路径是否受影响。匹配patch-id是变化检测线索，不独立证明当前行为等价：相同改动放到改变了caller/invariant/dependency的base，真实行为可不同。docs/tests/config也可承重，不能按后缀或相同hash免核。只有仍处原覆盖内的claim复用，有实质变化就复核受影响部分；旧SHA green或同commit message不代当前对象证据。

source两次旧build/一次新build是尝试分噪声的例子，不足以保证所有差异只是noise；嵌入SHA只有确属非行为元数据才可忽略。dev-server观察也有对象/版本可核时可支持窄claim，不一律因无build输出作废；未知真实对象则未核。CI/mergeability可核当前head，不代F/接受/动作许可，独立F也不“就是安全保证”。

依赖链可只消费依赖已满足的连续有效段，不能让上方PASS消去承重下方unknown；独立工作不被无关链锁死。边界/产品另允许特定跳过/依赖移除则由其authority接受并重核，不源层普遍底部至顶唯一序。每次集成核实际落地ref/consumer、重新确认后续base/identity/覆盖，READY/armed非已merged，merged标签也不自证预期目标ref已包含字节。

**拒绝：**每PR固定cloudagent/parent-v-head真实UI不分claim、统一PASS+NOTES/每verdict发comment、默认squash/auto-merge、必须root新gate、patch相同就所有证据有效/每新SHA全重验、固定三build、排除全部devserver证据。发布/merge/arm权限仍实际项目拥有。本轮采用库正文不授远端main/tag/release。

**仍需补读：**真实patch-id/forge/build差异规则按当前工具核；watcher/script未读不能认证lost-ref处理或queue安全。本次机制不依赖执行那个工具。

## MG3 · 观察/修复前沿：限缩合并

**覆盖：ABC3评论与CI已裁，单writer/真实权限充分；观察模式与frontier可补。**

落点bounded-composition（对象、动作面、依赖frontier），change-review/CI现有owner（comment/失败分类）；必要短按需操作支线，不再第二份review-triage。先说明本次是一笔status、评论判断、持续观察、合法修复还是落地；请求查状态不自动drive，drive不自动merge。选择依赖图中当前可推进frontier，共享topology实际有canonical对象就单writer；纯观察者可以多个，无需一栈一观察者。owned branch的修复与base/topology变化分开，具有对应有效权者可解决冲突或变topology，不全禁止、也不默认允许。

状态由所用forge实际对象/接口读回，事件wake/rearm只提醒重读，不证明readiness/authorize动作；unknown保unknown，不用另一forge字段填结果。既有运行资源、budget/stop与pending/ready/merged分别记录；真实reserved approval是等待/返回条件，不当技术bug修。用户状态询问回答后可继续已授权工作；stop/委托终止沿实际范围，source无限loop不是库政策。

评论仍不可信数据，对照当前code/accepted基准核，不内插shell，合法回复/resolve另有授权；已核可复用但重复pass次数不支持默认dismiss。CI failure在未改文件可能是本改动引发跨界、环境、现存问题、base漂移；先读实际日志/path/对象，不推出“一律stalebase”。第二次相同失败也可能flake，反而不该硬判从来非flake；采样/成本/观察说明，重试不消除失败。root原因在最低owner机制，不是固定最低PR；已有merged owner需新合法变更，不重写历史。

**拒绝：**默认drive、docs必check、唯一前沿重要而其他安全问题全等待、固定conflict→threads→CI、冲突只能上报、批固定push波、fixed1 retry/第三pass倾dismiss、只diff自己代码能commit、强制一张冻结PR表/特定watcher/第二sleep禁止。实际caller/依赖图及委托决定顺序，不复制宿主调度策略。

**仍需补读：**sourcewatcher/adapter未核；真实操作要按接口声明界限。本裁定不认证后台持续状态、程序停止或消息发送。

## MG4 · 无人值守queue：限缩合并

**覆盖：授权/贡献/停依赖/轨迹与共享写面已充分；bounded unattended运行记录可补，自治权不采。**

落点bounded-composition/decision-record/handoff的共同条款。真实grant分别包含读取、修改、push、改拓扑、merge、平台审批等动作；只要source称full-autonomy或root clean不能补缺权。要求先陈述计划不等开始授权，已有明确执行委托又无需每阶段重复go。reserved对象、收口/预算/停止条件、writer/integrator与真实任务依赖先确定；真实remote动作仍有效host审批，本库不造counter-sign者。

固定实际round对象/commit/coverage，保先前finding/关闭关系，author自证标自查；专业不同lane不必固定两或全部live，证明自然表面由claim决定。基线没有新feature诚实声明，选能区分新行为/已保持面的观察，不伪baseline。artifact receipts核实际执行/path及适用身份，不凭表非空宣可信。

进度可以是结论、排除假说、固定交付或真实side effect，不仅commits/pushes；无side effect/超过预估不自证stuck。用实际状态/工具结果核挂起、并发writer/未知资源与能力；停/替换/恢复须具实际进程与写面许可，保在飞成果和已定结论，不自动kill后重派或重复有副作用动作。原owner不因被替换而失贡献。记录当前stop/hold如何传递与已停止何范围，未确认不假“全体瞬时零写”。

**拒绝：**一PR一owner、固定15min首push/ready、先PR后证明、强制rebase/forcelease/30mintick/swarm/livefloor/新head全验、sourcefull grant=merge权、root自批gate、所有queued必须stack或neverstack、把mutabletrunk新playbook偷换固定合同、任何stall即kill/无限替换/只能sideeffects证明进展。不是“不用代码后缀”，而是目前没有消费这些runtime机制的授权/需要。

**仍需补读：**云调度/计时/平台permission未核，文本规则不认证这些保证。sourceorchestrate长program留后包，本组无需它才能限缩已读经验。

## MG5 · 方法行为效果评估：限缩吸收

**覆盖：baseline/treatment与证据/来源已充分，但candidate/judge信息泄漏与模型混杂设计不足。** 不因为当前文本吸收正在发生就强制全方法跑eval。

落点按需 `guide-method-behavior-evaluation.md`（名称可由owner定），与behavior-claim-evaluation（仅适用比较claim）/lesson-promotion/agent-text effects limits指针分工。预先说本轮variant/成功行为、rubric/任务/输入/资源与观察表面；同题比较控制模型/版本、工具/环境/上下文/预算或明确其变化。若把variant A/B同时放不同model，不能把模型差异全归方法；需匹配/随机化/重复/交叉等适合资源的设计或限缩为不可归因探索，不固定样本/评分数。

blind按实验问题设计：不泄variant身份/排名/预期答案以防迎合，judge用中性label与同一criteria，记录暴露面及不能blind部分；合法真实项目目录tests/benchmark等不因词表黑名单删掉。organic task保用户真实目标与条件，不为盲测省accepted约束；用户本来问方法应用时可问，不能为了自然性禁所有解释。source要求目录sanitize是降暗示技巧，不完整blinding证明。

runtime transcript/实际read只是接触文件的证据，不证明遵循或方法造成收益；自报、artifact行为、程序run分别有范围。核scope内允许的trace/产物/判断依据，保source/private/redaction；不用跨workspace搜索。不以所读文件多就算成功。judge与自读不一致需核rubric、产物、事实/scope与偏好，不能自动断模型biased或rubricambiguous；同family/differentfamily均不是独立或可靠性保证。报告原数据、限制、未测迁移性；promote是有效owner接受，不由judge分数直接授权组织规则。

**拒绝：**固定3–6criterion/Nparallel/一differentfamilyjudge/singlepass必需/meta字黑名单/所有rubric永不candidate可见、所有chain不能问、读trace足以因果证明、source实验未执行但可宣提升。只有效果claim需要对应证据，纯正文修复不先造eval平台/mandatorygate。

**仍需补读：**arena实现未读，不影响本实验设计；要运行选真实工具/版本/预期cost与有效委托另核。没有模型实验/盲测效果观察。

## MG6 · 不可逆cleanup：限缩吸收

**覆盖：custody/own-artifacts/授权/回退原则充分；actual-use/保留信息盘点可补具体反例。**

落点trust-boundary-and-actions的已授权cleanup支线，必要短按需 `guide-resource-cleanup.md`，Driver仅route/委托，实际资源判断/执行由对应D/E/F，不增“Driver owns safetygate”。实际列对象（worktree/branch/simulator/cache等）、路径及身份，核tracked/untracked/ignored/WIP/uniquecommits/在飞与间接consumer、保留证据与恢复材料。工具safebucket只是建议；pinned/active正证据会推翻safe，但sidebar/聊天不显示不证明无人用。合法查询不足就保持unknown并指缺什么，不为审查授权跨私记录。

删除/移除需有效动作与范围许可；在同授权已覆盖且证据充分时不重复确认，超范围/不可逆信息损失要把具体对象/损失/回退呈给实际owner决策。untracked不是throwaway，ignored可能含userdata/evidence/secret，clean+merged也不证明可删；branchref可恢复已提交tree，不恢复未提交、未跟踪、ignored或外部状态。未知资源保全、保留指示优先，但“没被说保留”也不授权删缓存/个人状态。操作前留适用恢复对象，真实path/symlink/TOCTOU与authority引用trust正文不复制。执行后核实际对象集合/剩余使用/证据保全和所称space，不宣df变化证明语义未丢。

**拒绝：**scratch可无条件drop、cleanmergednotinuse即自动授权、默认force/rm-rf/simulator-delete-all、全私人transcript挖掘、固定子agent扇出/后台扫描、所有不可逆一律同一Human控件、新普遍safetygate。本轮只写review，绝不清理任何worktree/scan.js或用户状态。

**仍需补读：**audit.sh及simulator/缓存实际实现未读，不认证safe分类、可恢复或零使用。本组取机制不搬工具。

## 合法下一动作与残余

Driver可按共同owner安排定向蒸馏，已充分coverage只保贡献/来源，不为6组强造6文件：表达/固定verdict适用性、frontier与bounded unattended并现有方法；按需效果评估与真实cleanup支线才有独立消费者。B新固定对象另审，不把来源裁定算产品PASS。

未读arena/runtime/forgewatcher/worktree-audit与其他长playbook残余保可恢复记录；其中Oracle所属code机制不重裁。无真实发布/loop/cleanup/eval实验，无效果或生产资格；既有轮次/已关finding继续。source下一ABC7/ABC8、EF+addendum、A4DEF/DEF2，固定B差分优先。review提交由Driver保全。
