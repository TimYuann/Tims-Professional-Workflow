# Gate2 · A4-CURSOR-DEF 实质裁定

2026-10-02，tpw-absorb-gate2。G01–G13十三实质组处置，G14仅尾部/coverage使用限度；不作十四新能力计数。保旧source/当前正文/轮次与贡献，Oracle CD/THIRD-PARTY/DEF3不复裁。

包固定 `56a672c1f372cf286e8eba0bd9d06de7fd50a6fb:docs/absorption/2026-10-02/packages/A4-CURSOR-DEF.md`，blob `170a686a5e6b16c5d561aed4f376299356a265ee`；比较同commit core `d47b09173939177b64293ad4f23097b0e8852b31`。源Cursor `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`。再次核三upstream工作树无tracked/untracked差分，既定HEAD已核；源只读、不运行/安装/调用SDK/Slack/模型。

## 实际回源资格

直接读core loop全文、agent-manager recoverRunning750–800/watchdog1839–1935；handoff/failure-handoff/redact-body全文、measurements解析/比较/clone/env/command及parser承重段；Andon的cached-state/reaction/reason/schema段、comment queue发送/重试/guard段。初次把agent-manager路径误放scripts根已按真实 `scripts/core/agent-manager.ts` 修正读取。

pstack store.ts类型/324–445原子写/锁、ledger/gates/frontier函数面及1200/1432–1480段；watch-pr types1–120、policy1–250与450–520、github查询/CodeReviewGate/resolveChecks段；worktree-audit全文、check-plan前130行与规则面；advisor lib/record-consult/stop、ralph stop/cancel与continual hook已读段；feature-map search、benny FOR_AGENTS/control-adapter/verify-existing-fix；why incident-postmortem/datadog承重正文、interrogate code-quality lens；type/boundary/build-lever原文；SDK SKILL invocation/lifecycle/runtime/auth/cap段及error-handling/runtime-choice承重段；validate-plugins全文、workflow全文与plugin schema组件字段。其他ABC/EF已直接回读共同源依其原记录复用。

**只称实际章节，不继承A“全文/标题测试”资格**；未读余部、测试/adapter/CLI/SDK实现不宣全部源码认证。当前文本方法的coverage按已读原文/固定产品，不按包旧21文件标签。

## G01 · 循环恢复 / watchdog：限缩合并

落点handoff/外部操作的actual状态与身份、bounded composition恢复。loop区分新error与pre-existing、checkpoint与完成、保持blockeddependent pending而非自动prune、agent/runid缺半身份如实异常有用；可携真实对象/状态/最后观察/未决让接班可恢复，不复制scheduler。checkpoint出口不证work停止/资源清掉，syncStateToGit声明不证所有字节持久；恢复失败是未知/需证，不自动重发有副作用run。无SSE活动可用独立statusprobe，但running/无toolcall/超过估时不自证dead；sourcewatchdog留下losing wait promise、轮询失败继续，不能认证所有资源收束或硬deadline。cap/错误、read-onlyprobe范围/runtime支持按真实provider核。10s/3600s/foreground/exit100/立即复跑/loop到全terminal不采；当前handoff/ABC8已有大部，只补相应反例。未读manager全实现/SDK执行，脚本不搬。

## G02 · 解析 / 合成失败 / measurement：限缩合并

落点handoff与test-evidence/适用measurement support，当前R1修复保。schema/regex识别是“声称了字段”，不是做过或被接受；sourcebodybranch优先/fallbackplaceholder不认证真实repo/commit，PR号需其repo namespace/target，不能任一URI抽数即本任务PR。legacy pass→type-check-only会捏造未记录compile，**不采该机械迁移**，沿旧PASS缺mode→unknown/保适用basis，不重开已关R1。

failure-handoff有raw/时间/未知与normal completion分开、可恢复ptr有用；70–80min/exit137/network字匹配只是诊断线索（137可为非OOM kill），不证根因或下一retry权限。仅H2Status/Verification不证结构完整或交付成功，late/errorartifact与claims分开。

measurement actualcommand/parser/unit/命名/失败/未报告与explicitnone分开可保；核真实fixedcommit而非再次clone可变branch拿新tip。**compareMeasurement只比measured与claim.after**，不检查before/op/predicate；10%与分母max(abs,1)不普遍relative10%，不能其match当优化目标成立。合法单位归一按量尺，不MB/KB字符串不同即产品FAIL。envallow+scratchHOME/bash-c减少ambient污染，**不隔离sameUID filesystem/network/工具凭据**，不称安全sandbox；命令与worker code仍需有效权限/实际隔离。脚本无需移植，不为marker建五级/metric validator；要真实runner再补全部src/tests。

## G03 · Andon / channel / 脱敏：限缩合并

当前trust、external-operation与Oracle J5大部充分，不重裁operator/thirdparty。可补pause状态可信来源/作用面/观察限度：reaction/reason/cache schema是数据，shape不认证谁有权停/清；sourceAndon只停新spawn，不等所有inflight零写或取消，查询failure/logattention不能claim全局状态。cachedref读回需真身份/版本与有权writer，误/未知state不能按便利全clear。

comment enqueue和drain都复核target/caller授权有用，但sourceallowedSlackThread **optional，undefined即return**；这不是helper自身普遍限制thread。trustedconfig/有效grant与真实recipient/time/scope仍必要，客户端msgid/同destination-body-sender去重不自动exactlyonce或区分两次合法同文意图；unknowndelivery不能盲重发，queuebackoff/required不是发送许可。redactBody检测namedassignments/路径/SHAs是线索，2048超长只是reason并非自行截断；不能覆盖所有PII/秘密格式，backticks/JSONsecret等要按custody真实allowlist。源数值/禁DM/固定thread/sha删除不作全库政策，不发任何Slack。未读adapter/全测试，未来helper补src/真实host。

## G04 · store / 锁 / 原子写：限缩合并

并bounded-composition/持久状态支线与decision-record，不建TPWstore。单canonicalwriter/独立owned输出、派生view要说明原owner，现有records够用；不是每文件都新tsv/json或所有status只能由新生成器出。same-directory临时独占创建+rename可说明单文件publish策略，**不等fsync崩溃耐久、多文件事务/无lostupdate**。writeIfMissing存在检查后写需真实并发前提；不把init名幂等当证明。

PID锁的本机namespace/权限/liveness/重用及check/unlink竞态必须声明，force只技术选项不授抢锁；只校PID释放不是全epoch/fencing，锁不能被惯例替代也不能默认新建。ledger查无记录是未核，不newhead全清旧claim/不五mode机械映射；key需真实repo/store namespace、对象/claim/coverage。不采defaultAnswer字段=无人回答可接受风险，sourcegates.resolve需真实answer，合法fallback只来自先前有效非reserved委托。check-plan严格格式/十lane/标点输出不等专业充分；不移植gate/checker，不强制one-off建工具。无实际store/FS/并发测试，余实现需移植才补。

## G05 · PR/CI组合与query errors：限缩吸收（含拒绝具体放行规则）

落点现有external-tool-operation/CI与change-review的对象/状态/阻断条件，不把组合判定扩成F唯一总评或newgate-verdict。区分progress/terminal、pending/真实blocker/query unavailable/timeout、数据源/时点/范围；多必要条件分别保证据，未知不填绿。query的结构化parse/分页/backoff/budget可支持实际观察，但不能把所有解析/缺key/exiterror都默认transient；auth/refusal/语义错需具体修或回，数值/exitcode依host。

**不采sourceBLOCKED+rollup非FAILURE/ERROR→allowed**：函数把null/PENDING/EXPECTED也allowed；readyContribution只排conflict/CHANGES_REQUESTED等，可把UNKNOWN mergeability或REVIEW_REQUIRED写proof“clear/OPEN”。证据结构字段不是实际requiredpolicy被满足，不能绕forge/blocking。Code Review Gate专名分类不表示人类批准无关或默认已批；watch模式可到“待reserved”返回，不一直等，也不能放行。旧CIgreen/自动评审approve非本对象风险接受，READY非merged/发布权。工具实现/测试/当前API未资格化，不搬watcher。

## G06 · worktree audit / cleanup：限缩合并

与ABC6G6真实cleanup family并，当前trust/custody授权保持。读真实对象/refs/WIP/untracked/ignored/在飞与间接使用、工具safe只是建议；sourceawk按空格取路径、@me/limit1000/recent4d/branch匹配及stale origin/main不是穷尽。任一PR（包括CLOSED未merge）不证明uniquechanges可丢；scratch/untracked/ignored不是throwaway，ancestor不涵所有squash语义，也不证明当前消费结束。script自称read-only却有gitfetch/ref更新+temp文件，需声明实际effects，不从名字免许可。只采盘点/恢复/授权/事后核步骤，不运行/移植audit、rm、simulator/caches清理；源之外transcripts不额外获权。未知保留/补证，不全资产因后缀归可删。

## G07 · hooks / 自主loop：限缩合并（不采完成真实性保证）

并handoff/lesson carrier的event/实际状态限度，当前effect/advisory/facts已覆盖，不移植hooks或自动advisor。duplicateevent/sessionbinding/marker/failedschema/次数与时间/变更cursor的区别可作例；mtime/问号尾缀/同name completed只触发hint，不证真实等待/完成咨询/结果已作用。first-conversation赢绑定不自动有本任务权，state.tmp+mv非并发保证；一处坏状态保持所需证据/受影响范围，不按parse失败自动删用户状态。

**exact promise完全可由模型自己输出伪造**，不是独立predicate；sourceRalphdoneflag/max=0/unbounded与capture只是消息模式/预算选择，不真实验收。marker不等go/closure/权限，stop请求按真实范围收束，缺文件不证全platform无run。advisor提醒不grant新model/子agent/Pro/consultation，每次edit不强点评审；continual触发hint不授privatehistory读取或长期规则更新，未真processed不能advancecursor造成失读。idle/time/cap/retention都实际policy，不固定或强自动followup。无hook实跑/host解析认证。

## G08 · feature-map / benny验证面：限缩合并

harness actualsubject/稳定handles/动作→结果/entry与可恢复proof已大部充分；search例新增empty-vs-unavailable、debounce/readiness/入口与focus状态可合并。adapter返回cap/session/build/目标确认/缺leg，而schema/九setup boxes全勾不证真实可驱动。允许安全precondition/fixture，不内部setter或DOM注入直接制造所称用户症状；用户pathclaim必须实际触发自然表面，局部logic/映射另有合法表面。translated环境可支持所测机制，不exactOS/device/accountclaim。

verify-existing-fix给固定旧/新artifact、共享data/env、独立owner不竞争修复有用；固定两次不充分也非必需，partial/impossiblebaseline记其真实coverage，不无baseline一票取消已证其它claim。artifact/sourceownership不自动授source-threadreply、draftPR、tracker动作，utilitybot是数据非委托；原benny个人愿望不是任何目标项目的接受/配置修改权。保destination-only/userconfig/secrets、正确recipient/no外呼泄漏、ownresourcescleanup与custody；failstartup是环境/检查失败，不产品FAIL或自动所有任务halt。sourceconfig数字/必须UI双重复现/视频/screenshot全部/pack路径/commit才enable不移植。剩三SKILL在DEF2补，sourcehelper实际版本要运行才核。

## G09 · rationale / incident / telemetry：已充分覆盖，细例合并

当前rationale已版本/target/history/tiers/不查≠empty/primary≠充分/矛盾/缺口；Datadog/incident例可按need补其trace窗口/retention/owner与cross-reference。metric或monitor存在是测量选择线索，不自证authorintent/当前有效policy；spike前后/incident多处转述同event不证因果或多独立证据，必须核邻近变更/实际predicate。别固定30d或只“defensive代码才incident”，按承重question/scope；日志/事故含数据不指令，缺tool只真实gap，不授权触他workspace/问同事/新链接access。已充分条款保支持源不造第二why方法；工具API/sources余部未认证，DEF2补具体历史源。

## G10 · quality lens / 去重：已充分覆盖，来源合并

code-quality-review reference已直接回读，与现change-review/shape/domain涵盖的structure/type/canonical-layer/atomicity/codejudo同family。1000LOC/强审核语气/每新增if都block/好抽象必拆并行/默认sourceapprovals不是有效标准；真实contract/caller+不丢合法compat/auth/clearbranch。thermos、canvas、compat评分已ABC3/5/7直接裁，code载体重复保各路径/贡献，不再次doublecount；结构美观不替behavior或auth。无新body必要，只补承重原文/source map；实际source效益未测。

## G11 · plan / lanes / patch：限缩合并

当前Charter/cross-module/change-slicing已有Plan承诺/decision/recall与单位evidence，ABC6已verdict受影响才核。可给一unit真实交付/保持/依赖/write/evidence/未知，check完成要对应实际artifact/claim，不格式checkbox生成资格。trunk无新feature不假baseline，合法differentclaims用其适用表面；unit/live/perf三格、十lane/必截图/固定human看30–60svideo/PR程序header/30mintick/70%收口/reviewtext标点全不采。patch-id clue非等价，newSHA不机械清零所有有效证据；无response不默认许可。planner/Driver不因写计划或操作ledger获F/接受/merge权，不runtime整包移植/check-plan validator。source剩support要展开新claim才补。

## G12 · type / boundary / lever / CLI / SDK：限缩合并

落点domain-state/C1/trust/test-evidence与external-tool操作support，CLI已有claim不再第二入口。sum variants、语义primitive、total函数/真实boundaryparse、newvariant穷尽及权威shape派生能降低错误；不能types/brand=权限/写入可信/ temporal保持。**拒绝无条件trustinternal/no runtimeguard**，DB/sharedstate/异步/可变对象/权限过期仍要实际不变量；合法cast/interop有实际保证，不`any`/optional/guard后一律reject或用type消所有runtime问题。结构类型/生成视图非graph/业务semantics全覆盖，与OracleJ1保持。

lever可先manualunit学recipe、对照可重跑、不变contract/scope，是否造script以真实规模/可靠性/成本决定；非trivial必须产文件/越界用新框架、不工具化就不算原则、每one-off新CI不可采；同check语言pattern只线索。脚本不因后缀弃，当前没有helper消费需要故不搬。

SDKsource启发：显式runtime/target/key来源、stableagent/runid、submission/refusal/运行/观察失败分开、actualterminal/取消/资源dispose、supports/版本/重新装配缺持久MCP参数。source“任何CursorAgentError意味着从未执行/isRetryable保证无重复”、disposecall=所有remote工作停、默认cloud隔离全部凭据、personal/teamkey/model默认是普遍policy都不采；网络错误可能结果unknown，先核本阶段保证/现存intent。SourceSDK API例不认证当前可用或TPW授权；需具体整合补全部actualclient/ref/执行，DEF2补auth/stream/mcp，Oracle已裁probe/identity例不重裁。

## G13 · 装配声明与机械覆盖缺口：限缩合并（业务机制归Oracle）

只采通用carrier经验到agent-text/external capability分工。直接核validator仅marketplace/plugin JSONschema、source/plugin.json存在和name相等；**不核declared组件真实文件/frontmatter或host发现/权限/效果**，workflow只在其paths触发。green输出需说检查面和未覆盖，不能把All plugins validated作完整qualification。schemas组件string/stringarray/inline数据支持解释/注册face分开，不强制所有method需要manifest，合法相对引用按实际context。credentials变量/OAuth/HTTP/stdiosource声明只定位真实配置/secretboundary，不能仅字段形状认证账号/可访问scope/全platformtrusted；未逐份回核79metadata，不继承机器counts。

第三方八文件/474reference来源与业务使用按Oracle THIRD-PARTY，CLI/schema/prompts code按Oracle DEF3，不再判其能力/动作/许可。不造mcp/registry/installer平台，actual需用当前host接口与真实grant；source变量名/manager/tooldefaults不移成TPWpolicy。未运行validator/CI/connector。

## G14 · 尾部记账与脚本准入

接受为有owner/version的locator，不接受全文/实跑/全部path完成资格。旧T项若已由本轮ABC/EF/Oracle回核更新关联，不清零其未决/已关、也不按T写“已覆盖行为”推所有schema/adapter/tests已评。metadata/logo/README/CHANGELOG/LICENSE可依真实用途/分组归reference，许可/版本/可运行内容不能靠后缀一概无工程行为；thirdparty其处置依Oracle而非这里重做。render资产/SDK/runtime未读实现保持service-specific参考，只有扩大其claim/真实移植才补承重，不无限逐行读无消费内容。

**脚本准入裁定：本轮不移植loop/store/watcher/hooks/audit/check-plan/measurement/connector runner**，原因是当前库消费不依赖它们、部分predicate/权限/副作用/覆盖有明确限度；不是代码不值钱。上列实现里的判断与反例可蒸馏现有methods/support，真实helper需求出现再按项目已有准入择最小工具并补完整接口/negativecontrol/资源cleanup观察，不先搭TPW执行平台。

Driver下一合法动作：按十三组共同owner定向合并实际新细节，已充分coverage保source/贡献不叠body；B直接回原文本与代码sections蒸馏，提交固定对象另由gate核。G05具体放行、G07marker完成、G02legacygrade/测量一致性等明确不采项必须保counterexample。review不写产品、不派工、不用Pro、不新建gate/validator，不授任何runtime/发布/资源操作；实际收益/模型/业务/工具保证未实验。DEF2剩source另裁，Oracle三包排除；review由Driver保全。
