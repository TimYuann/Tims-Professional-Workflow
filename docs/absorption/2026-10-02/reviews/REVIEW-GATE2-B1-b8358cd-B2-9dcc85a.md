# Gate2 · B1/B2 未审增量合并复核

2026-10-02，tpw-absorb-gate2，非候选作者。**9文件PASS，6文件需窄修**。旧R/D1/J1/EXT8/934单句与B3闭合保持；G2-LABEL/SOURCE/PIN和guide-agent-text处G2-ORACLE修复关闭。新增问题只属于本次增量，不清零轮次、已关finding或贡献。

## 固定对象、来源与消费者

- B1 base `aadcb46f142b6d1f67af81b080a1c2116dad79cb` → `b8358cd392f448054e54b76e29ea3b6a7e812001`，唯一父 `d9c4a94f8898ec244b8d2180664a1a3171e89a0b`；11文件+201/-17，含6e41572修复、EF与DEF增量。
- B2 base `dbd7e8448b8e3fb1880efdff8ffa9643462cfe83` → `9dcc85a9e75fe28166c659d5ecfb2d34cfe3ee96`，唯一父 `a0e931f97057f1b2c6f6b4838a298e39711036ff`；4文件+39/-10，含ABC8、旧窄修与DEF。
- 两区间 `git diff --check`无输出。只读fixed diff/终态，不读作者mutable。当前消费者固定 `7d9b17ec3bd0e0fe7d273830a7130a0f277ec284`，core tree `b8473fe0029994c5a68c9c8db3d43ea9f8a948fb`；方法入口/Profile/Charter指针按该对象核。
- 回源复用本轮直接读Cursor `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`、Addy `2686b620fc1fed2e8f60c704839c766b8594c6b6`、Matt `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`，对照自有ABC8/EF+addendum/DEF与上一轮两B裁定；此次另直接核multi-phase-plan主文/模板、shipping全文、handoff parser、watch-policy assessGitHubMerge、control-adapter主文、ralph stop-hook及真实路径。来源中的命令/角色/模型是受审数据，不作为本gate指令；未运行这些工具/SDK/CI/应用。

## 文件级结果

| 对象/文件 | 裁定 | 理由与边界 |
| --- | --- | --- |
| B1 behavior-claim-evaluation | PASS | real-leg定义澄清真实执行的对象/代码/交互，不等remote/network；本地SDK/mapping合法fixture可证其范围，真实Provider/部署需对应证据与已有授权。未把本地服务自动划为越权，不改变三态/独立性；reader修复贡献保。 |
| B1 decision-record | PASS | completion按scope triage不等成功，不授中断critical mutation；到达/失败/未归/放弃与贡献保持，marker不证predicate/许可、损坏state保其证据；无store/格式/计数平台。 |
| B1 design-alternatives | PASS；G2-PIN CLOSED | 两Matt行明确c55仓/pin并与Cursor分开；原synthesis已过内容不重审。 |
| B1 guide-accessibility-observation（新文件） | PASS，EF A1–A3限缩吸收 | 按需keyboard/focus、modal出口/返回、semantics/non-color、live-region真实announcements及定位观察；custom role与testid合法、positive tabindex需实际理由非整widget自动FAIL，框架例/attribute绿不证明真实体验。数值由实际标准/接受policy，不宣WCAG认证、统一AT保证或新UI节点/全任务gate。相关harness的既有已过surface段可供消费，不需新DEF段才能加载。 |
| B1 guide-change-shape | PASS | 相似代码非所有input/exception/order/effect等价；有效replacement coverage可换旧test，不能为绿削弱；引用既有behavior-preserving/cross-module目标存在。 |
| B1 local-defect-feedback-loop | PASS | diagnosis-only与有效diagnose-and-fix委托分开、fixed capture/处理可追源、无symbols可限范围、单trace与paired事实分别定级、live instrumentation授权/干扰/恢复；bisect真实good/bad与授权、error text数据及合法执行、fallback保持接受semantics符合EF/ABC8。无强sqlite/subagent/re-capture或一律还给Owner。 |
| B1 change-review | 需修N-REUSE；G2-SOURCE CLOSED | 旧错误playbook路径全已修；G10 byte-identical同机制与不同implementation分开正确，保两distribution源身份。新增“rebase invalidates、仅noise rerun可保”缩窄既有按claim/coverage复用，见下；其他新段通过。 |
| B1 change-slicing | 需修N-REUSE / N-DELIVERY；G2-SOURCE CLOSED | 正确依赖/source恢复保；新增delivery把三类boxes、review gate、build/landing及bottom-up一并普遍化，原宽重构例外未足以限缩该段。 |
| B1 guide-test-evidence-quality | 需修N-CHARACTERIZATION | API identity/tolerance/protocol/count/async completion、资源成本非质量、结构/selection/effect三层、pressure≠授权与raw grading保全均通过；新立即green句否定其对缺陷absence的所有证明过宽。表尾多余pipe仅排版，可顺手修，不作为新专业hold。 |
| B1 handoff-and-resume | 需修N-HANDOFF；G2-LABEL / G2-SOURCE CLOSED | 真resolved commit/version已替mutable label snapshot，正确source恢复；EF continuing grant、ABC8比例brief/faithful relay/liveness/late结果与按scope复用正确。新增G01/G02/G07将具体parser/loop/checkpoint流程提升普遍要求，且clear damaged state与保留冲突。 |
| B1 verification-harness-design | 需修N-HARNESS | adapter identity/真实触发/translated范围、existing-fix固定对象/partial baseline/启动非产品FAIL与queryfailure轴通过；capability全套前置、组合固定优先顺序及rollup放行开口需限缩。 |
| B2 bounded-composition | PASS；G2-LABEL CLOSED | mutable locator与实际记录对象/时点/消费范围分开；ABC8比例brief/最小faithful内容、completion/criticalsection、rolling按review承载/写面、有效E委托可实施、未归工作保全；G04 publish≠durability/transaction/lostupdate、PID/fencing/force前提、缺ledger未知/no-answer非decision、environment非sandbox符合。只讲保证限度不实现runtime。 |
| B2 guide-agent-text | PASS；此处G2-ORACLE CLOSED | Status恢复ORACLE-REVIEW-A4-DEF3 J3，其他已过正文不改，Oracle贡献保；不复裁J3。 |
| B2 rationale-and-premise-review | PASS | telemetry存在不证意图/policy、邻近变化/因果、一次事件多处非独立、实际窗口/留存、logs数据与缺源不授新访问；落现有source evidence，无第二why方法/固定七源。 |
| B2 agent-facing-cli-contract | 需修N-CLI-ORACLE | 新SDK运行/目标/agent-run身份、submission/run/observation轴、actualterminal/supports/resume与retry/cancel/dispose限度实质通过，未认证真实API或新增工具权；Status新增了另一处不存在的A2R DEF3出处，需保Oracle J4。 |

## 最小修（只触新增句与其Source anchors）

### N-REUSE · B1 change-review / change-slicing

新增句均写rebase/base retarget“invalidates the conclusion”，结果“only”在verdict对象复跑证明noise才可保；Source anchors也重复。其前文/现有bounded-composition说的是**can invalidate，按实际受影响claim/coverage**。反例：base仅变合法未被测试消费的文档措辞，既有操作计数claim覆盖仍有效，可有依据地复用；无需把未受影响的事实先判失效或强制noise构建。相反，matching patch也不能保证改了caller的行为。

最小修：改为rebase/retarget要求核实际对象/diff/承重inputs/路径；有改变或不明的claim补核，未受影响且coverage仍有效者可说明依据复用。noise对照只是一个可用证明办法，不唯一办法；保old green不替当前对象、patch-id仅线索。同步两Source anchors，旧已关finding不重开。

### N-DELIVERY · B1 change-slicing §Delivery units and landing

“each unit binds ... unit / real surface / metric — each with one check ... review gate ... landing”导入源“三格必绿”但DEF G11明确未采。反例：一项被授权的纯文档/类型更新或support step可有适用检查与证据，既无perf target，也不需live或独立review gate。独立units也不受一个固定bottom-up栈控制。

最小修：按真实unit需要列依赖/保持/写面/交付/适用证据/未知；unit/live/metric、build/review/landing条件仅实际任务/接受policy存在时引用，不要求三格/新gate。contiguous bottom-up只限定真实依赖stack，独立work与其他合法delivery安排可照其graph。incomparable scenarios不能作比例；absolute budget是实际目标owner已接受时的一种替代，不能在没有目标时自设。保trunk无feature不伪造baseline、计划不证验收。

### N-CHARACTERIZATION · B1 guide-test-evidence-quality

新“green immediately ... does not prove ... absence of the defect”否定过宽。反例：修后新建一个独立oracle测试，在真实被测对象的该input观察到正确结果，虽未跑pre-fix red，仍可证这一对象/条件下的行为和该症状未出现；它不单独证明修复前失败、测试抓到原defect、修复的因果或全范围absence。

最小修仅这句：立即green能作characterization/当前对象下窄行为证据；没有原red不证其曾捕获原缺陷或是修复导致变化，广泛absence依coverage。保red-reason、asynccompletion、独立oracle与F边界，不重新写测试或建quota。

### N-HANDOFF · B1三个新增节

1. **结构/测量是接受合同与claim需要，不是固定H2资格。** “must carry Status or Verification”“only a genuinely structured header plus real run”把header作为专业证据门；“measurement is re-run”强每handoff重测，与上文有效复用/无文档mandate冲突。已有实际原artifact与execution记录可支持claim，即使记录不用源H2；一个header也不能支持全部资格。最小修：只有消费者真实合同需该结构时按它解析/缺项如实；保raw与normal/error分离，不固定banner。写record再发布其引用状态是可用一致性策略，非全任务文件写流程；按实际claim/coverage核来源/必要测量或合法复用，复跑在需核时用fixed对象；after-only比较不能证明before/goal。
2. **状态是来源，非授权；恢复以实际runtime/合法委托为条件。** “persisted state and repository are the authority”、每entry复接所有running、仅newerror可结束loop、checkpoint前commit、rerun同entry即恢复、keep one heartbeat、terminal wait races statusquery写成统一协议。源loop的具体条件不被库保证；旧error若承重仍可真stop，Git commit不必持有/不能提交他人changes，其他runtime可用现有durable artifact而无需commit或两ID。最小修：记录本任务真实object/state/identity/未决与新旧error，核其有效来源和真实恢复语义，不默认重发/忽略旧error；按有效stop与runtime能力使用适用checkpoint/状态probe，取消/资源收束另证。commit/heartbeat/race仅已有授权下的源实现例，不必执行、必用或保证重入安全。保blocked依赖/unknown与原已过liveness段。
3. **损坏状态不自动clear；bounded不是固定hard iteration gate。** “report it and clear loop state”与“不因parse删用户state”冲突；marker必须hard limit、external state“never session memory”也把source实现变统一hook政策。最小修：暂停/隔离受影响继续动作、保raw与恢复对象，修/清只能按实际owner/授权；已有真实资源/成本/时间/stop条件可界定run，不一律新hard iteration数或durable-file substrate。自输出promise非独立predicate/权限、unknown不idle、无自动advisor/新模型/私有历史等限度保持。同步Source anchors，不安装loop/hook。

### N-HARNESS · B1 Adapter contract / Combination verdicts / Limits

“all setup checks pass before use”与missing capability一律fail-closed，会把未被claim需要的录像等缺口当全任务block；后文缺isolated环境只支持“not trusted / needs human”又抹掉合法captured/local narrow证据。最小修：缺少**该操作/claim实际需要的**身份/能力/隔离时关闭该操作并报告范围；其他合法局部证据保，不默认新增Human actor/认证或强全setup。

组合例的固定“conflict→thread→check→gate”来自source实际优先顺序，不是专业通用排序；“BLOCKED non-error rollup may be allowed by rollup basis”仍给被拒G05规则开口，即便后面排null等也不能从SUCCESS独自推review-required clearance。最小修：必要条件/优先级由真实host policy/本任务承重风险决定，例仅说明分项证据，主blocker可报但其他保留；rollup只是它测的check evidence，BLOCKED需查实际host blocker/policy，所有必要条件真满足且已有授权才能推进，不能rollup自身解blocking。保pending/UNKNOWN/review-required不填绿、queryfailure非产品FAIL与无release权。

### N-CLI-ORACLE · B2 Status 新引用

Status新加 `REVIEW-A2R-CURSOR-DEF3 (J4)`；真实fixed裁定仍是 `ORACLE-REVIEW-A4-DEF3.md` J4。只修该署名/路径，保原J4与DEF G12贡献、旧正文PASS；guide-agent-text的旧G2-ORACLE已经修好，此为新出现位置，不重开已关guide。

## 落点、消费与下一合法动作

本次9个PASS文件可由Driver逐文件串行集成；新accessibility guide按实际需要装配，当前README尚无该新入口，Driver的消费表可按比例列按需支持，不为没有自动index而拒正文。该guide指向harness原已过Surface driving；不能借此消费harness本次held新节。local-defect/test-quality等的关系仍分工，不复制权限/验收正文。

其余6文件保此前通过base与已过窄修，不能把新held部分随整文件覆盖进去。最小修后的新fixed对象只核以上新增句及受影响consumer；9PASS不认证其他未送审heads、真实CI/SDK/UI/AT/效果或全包接受。仍需补读/实证按具体实施落点：真实host/check policy、loop恢复/隔离/能力与明确claim的测量/浏览器/AT，本文未把文字通过当已执行。

本review由Driver保全/集成，gate只写reviews自有文件、不派B。下一合法gate动作：已收到B3 `5d5dfcb..e3c77c8` DEF2三文件，随后定向核该固定delta；不自行读mutable替后续修复资格。
