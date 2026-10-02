# Gate2 · EF addendum / F9 逐机制裁定

2026-10-02，tpw-absorb-gate2。与 `REVIEW-GATE2-A1-ADDY-EF.md` 为同一次EF族处置；P1–9/S1–3/O1–2/A1–3/T1–5 共22支持条目已逐项判断，**不算22独立新增能力/文件**。旧F9 title层“重复”被本次原文取证取代，Oracle CD源裁定不重开；covered与是否值得改分开，作者自称“新增”不继承。

固定包/产品/源身份同主review：7e3a82f、addendum blob `2fb3cee4269448c5c0c500a087d7a62e8d246ee5`；Addy pin `2686b620fc1fed2e8f60c704839c766b8594c6b6`。本次直接读references performance/security/observability/accessibility-checklist与testing-patterns正文；a11y另读frontend-ui-engineering176–232以核custom-role反例；performance主体与Oracle已审C9/C6/C7产品直接对照，Chrome官方页沿本轮已取回版本依原review保。未执行checklists/scripts/浏览器/DB，command/API/version矩阵不当当前可运行资格。

## P · 缓存、容量、查询与前端性能

| 条目 | coverage与采纳 | 理由、边界、落点、补读 |
| --- | --- | --- |
| P1 cache key / viewer隔离 | 当前performance已充分覆盖；与C1/C6互指可合并 | 缓存response所依赖tenant/viewer/locale/permission/flag的正确等价类不能丢；不是必须把每值字面拼key，合法分区/命名空间/已证明不变条件可表达。auth/viewer漏项会串数据，纳入actualcorrectness而非只有速度。不重复新cachekeyguide；具体key/hash/auth变更需其实际contract/run，无当前文本缺口。 |
| P2 stale window / invalidation | 已有explicitstale/key及正确性边界；限缩合并read/write模式 | 可接受陈旧由B/C/policy，不由E顺手TTL；TTL/event/tag/versioned可选择或有明确协议的组合，禁的是偶然mix而非任何多策略。余额/权限/库存不一律禁cache：不满足本claimfreshness且无协调才不能用TTL兑现。write-through“同步写两个”不自证跨store原子/无stale，write-behind需durability/replay/unknown结果，cache不能变唯一未保护真源；按需支线并performance的缓存section，actualprotocol需补观察。 |
| P3 pool容量 / diagnosis | 缺具体容量算术；限缩吸收并performance资源段 | 核真实resource目标与所有竞争consumer：各instance/pool/job/admin/migration/保留headroom共同占用可用上限，不只instances×max单公式。按request造pool会消耗连接；“每process一个pool”是同resource共享例，不禁止多tenant/不同DB/隔离目标的合法多pool。测等待/占用/长transaction/leak再扩；boundedwait/timeout跟SLO与恢复，failfast非全域目标。autoscaling无界需admission/容量保证，multiplexingproxy是一选择，核transaction/session兼容，不加proxy即自动安全。具体engine/client需其版本/执行，不搬参数名。 |
| P4 negative cache | 当前无具体failure distinction；限缩吸收 | 区分authoritative absent与timeout/5xx/permissionmasked/unknown；不能源故障缓存成不存在放大，也不把所有可设计的errorcache全禁。negative窗口按创建可见性/abuse/load等目标定，不必永短于positive；newrecord invalidation/receiver授权语义必须正确。并cache支线，反例是一分钟故障被持久404放大；真实origin语义需补，当前可蒸馏。 |
| P5 coalescing / stampede | 简要cache已有，具体并发机制不足；限缩吸收 | 同key inflight共享结果/失败cleanup、调用者取消与真正fetch取消不同、boundedwait、key与writer范围；局部promise只覆盖该process，共享层可distributedcoordination/admission/符合freshness的SWR等，不固定必须distributedlock。SWR不能在陈旧违约处直接用；lock需owner/fencing/timeout实际保证而非惯例。原loadOnce片段只示意，不认证同步throw、reentrancy、跨进程/取消安全；performance按需支线，实际实现再补src/runtime。 |
| P6 measured cost / hit rate / bound | 测量/复杂度目的已有；资源有界与cache持续收益限缩合并 | expensive/重复读成本是选择证据，boundedmemory/eviction按实际finite生命周期与资源；低hit不必无价值（misscost/correctness/突峰成本不同），量actualtotalcost/tail/维护，不能仅hit阈值全删。已有明确接受非性能目的按其目标评价；缓存“unbounded”是容量风险，不以词本身诊断heap leak。并performance/cache支线，不强制所有projectdashboard；需actualloadrun才证收益。 |
| P7 query plan / index | 当前“planunchanged≠无价值”已充分；细查计划可合并 | baseline计划+实际query/params/data/stats/engine/load，理解scan/sort/estimate误差与writecost。索引“等值先/范围排序后”、cover/partial/expression/fulltext是条件例，不普遍最佳排序或所有engine原语；unchangedplan不自动revert，usage统计缺样不证明无用，删索引还要constraint/consumer/权限。EXPLAIN ANALYZE可能真正执行query（写/函数/资源），只在合法操作环境；无能力就说读收益未核，可在合适替代条件采证，不为完成强求生产probe。现performance窄增补，无具体indexCLI复制资格。 |
| P8 bfcache / dimensions / fonts | bfcache已按官方页纠正；dimensions/fontmetrics限缩合并 | 不重开OracleC9或沿source“No no-store”全禁；敏感cachepolicy不得为指标擅改，浏览器/version目标需真实支持。图片/艺术裁切预留layout与fallbackfontmetrics降低shift可保，实际viewport/fontload测；不固定widthheight所有tag/WOFF2only/fontswap/preconnect/bundleKB或token配额。树摇sideEffects:false不许强设到有副作用package；源码示例不认证平台。并performance frontend段，API调用/当前browser矩阵要展开再核。 |
| P9 interaction三段 | current症状分解已有；input/handler/presentation增补合并 | 顺用户面slowinteraction拆waiting/processing/render，找实际trace/source负载，不只改JS handler；高端机不出现时选代表设备/条件并说明throttling只是proxy，不强制midAndroid/4–6倍/50ms/先RUM才可local调试。scheduler等sourceAPI不当可用白名单，局部capture可支持局部claim。并performance诊断段；具体WebVitals字段/version要实现时补，不产生SLO。 |

P1/P2为正确性/contract concern，可由C/D/E/F在所需场景调用同缓存正文，interface只按实际need互指，不以目录名把语义所有权放performance executor。多源同cache family保Addy原文/C9/当前相关source，不双计。

## S / O · 信任边界与可观察

| 条目 | coverage与采纳 | 理由、边界、落点、补读 |
| --- | --- | --- |
| S1 derivedpath / marker / TOCTOU | trust正文已充分；相对路径精确例可合并 | 现有allowroot/min-depth/authenticatedownership、marker可写非auth、descriptor/no-follow/immutability已具体，作者称全新增失效。相对“..”与“../”escape不等合法“..cache”名称，必须按actualresolvedroot/target/平台语义核；不把stringprefix/源snippet当授权或无race保证。不是复制代码才可采经验，不改trust完整规则。需实际helper时补真实filesystem/run；本组无文本缺口。 |
| S2 install/version矩阵 | trust source-version/client-install边界已充分；actualentry细节合并 | 定位manifest/lock/CI/真实workspace install boundary，冲突显露；不要先executelifecycle再发现。scriptsdisabled/default-deny需实际client有效支持，选择最窄允许、cleanfrozeninstall核所需构建；版本matrix是pin作者时点自述，不通用事实/currentcommand批准。独立subproject可不同manager，不全目录锁数=唯一。路径discover/策略修改/真实install还需有效委托，不整表移植；具体manager/version展开才补docs/run。 |
| S3 misinformation / poisoning | citation/trust主干已有；data/model来源限缩合并 | 关键claims出处/版本/实际覆盖可核，不citation即真；model/finetune/RAG/dataset/plugin输入的provenance/integrity/更新/tenant/审核owner明确，hash签名证身份/完整性不证内容可信或有效。human-in-loop按实际reserved专业判断，不每LLM回复强人审。LLM09/04编号只源 taxonomy引用，不全模型安全认证；合并trust/source-evidence相关段，actualpipeline/host需补。 |
| O1 question-driven dashboard | observability问→signal已有；dashboard消费面合并 | dashboard让operator回答当前问题/依赖/traffic/error/latency/resource，timewindow/分布按事故/SLO/task，不固定1–6h/每endpointRED/至少1告警/newfeature全五gate。验证telemetry要实际路径，testfire/真实traffic仍effectivepermission；nochannel如实缺证，不defaultsend来凑check。既有runbook/obsowner互指，不第二发布validator，未观测实际仪表盘可用。 |
| O2 entry-point ≠ correlation | 当前obs整段已充分，无需重写 | ID标run，entry从起点随边界传播，label猜测非归因已具体；作者自称尚缺不能覆盖实际body。保本support/source贡献，sourceECS `source.*`命名是其schema条件，不任意项目都禁止field source。无需新body/文件；要新SDK传播claim才补。 |

这五项是EF support，不重复裁OracleC6/C7；只对当前coverage与本support实际可蒸馏判断。DoD/其余check项按已接受质量政策适用，不checklist即授权/ready/closed。

## A · 可访问性（不因“没有UI域owner”整体排除）

可访问性是UX concern横跨B可观察承诺、D/E实现与F证据，现有A–F能承载。A的“不属EF/无所有权”只是包分类，不是本轮禁止；但只裁已回源可判断的三支线，不假整个frontend/designsystem已读。

| 条目 | 采纳与落点 | 理由/边界/补读 |
| --- | --- | --- |
| A1 keyboard/focus | 限缩吸收，按需UI/a11y support | focus可見、合理顺序/键盘操作、modal打开后的scope/可退出/关闭return-focus可观察；trap在modal期间与用户能关闭/离开不矛盾，不“永远Tab必须出modal”。正tabindex通常带维护风险，不因此所有legalwidget判FAIL；选择native/rovingfocus按实际交互contract。sourceReact `<dialog open>`/focus例不认证已trap或可恢复焦点，必须实际观测keyboard/browser/assistive范围。无universalextraa11ygate。 |
| A2 semantics / non-color signal | 限缩吸收并同support | action/nativebutton、navigation/link可优先，customrole需完整name/state/keyboard/behavior，不按div/span后缀全拒——frontend原文自己给rolebutton例。color-only信息需非颜色可感知信号，label/error关联/可观察输出有用。sourcecontrast/size/numeric参照是特定标准/条件，实际acceptedWCAG/policy/用户需要决定，不能用source枚举宣合规。要官方norm/certification或代码组件方案再补。 |
| A3 live announcements | 限缩吸收并同support | ordinary/status更新与紧急alert按真实urgency、区域可发现/内容变化条件和assistivetech观察；不是所有错误assertive/每dynamicDOM都新live，防重复/频繁打断、焦点变化另核。role属性/schema存在不证真实播报，genericpolite/assertive只是例。sourceSDK/runtime未测，不统一frame-agnostic保证；展开实际component须补真实browser/reader。 |

优先共同短按需 `guide-ui-accessibility-observation.md` 或现有UX/browsertestowner支线；不铺所有Profile常驻，也不造“UI责任节点”。与F6/harness表面证据互指，实际用户体验/a11y达标未本轮观察。

## T · Testing patterns 支持

| 条目 | coverage与采纳 | 理由、边界、落点、补读 |
| --- | --- | --- |
| T1 user-perceived locator | harness已有roles/labels/stablehandles；限缩合并具体条件 | accessible role/name/text先定位用户可辨对象，真实name/keyboard不足可报具体a11y缺口；找不到role不自证全UI不可访问（非interactive/native/虚拟内容等不同）。testid/data*在适用稳定边界可以合法，不一律坏；存在role并成功query不证明screenreader/焦点/操作正确，F6/A各观察。并test-evidence/harness，不固定RTL/PlaywrightAPI。 |
| T2 endpoint成功/validation/auth例 | 限缩合并C1/testsupport | 正反例应源accepted公开contract：成功的request/output、invalidinputs/error含义、需要auth的身份/资源权限路径。public endpoint不能为了三件套凭空要求401；asyncaccepted不强201、不同错误shape不强422。errorcode和文案何者本contract需保持就断言，不能“永远码不测消息”。局部fixture需生产adapter实际path，HTTPstatus绿不等provider已执行。无需新gate/每endpoint至少3tests，实际API/host版本展开补。 |
| T3 testname形态 | F1/specname覆盖充分，无需改 | `[unit][expected][condition]`可示例非强制句法；实际名字让reader理解所测claim即可，命名不自证执行/coverage。计共同source贡献不独立增量。 |
| T4 equality / tolerance / error | evidenceguide大部；限缩合并短例 | 根据acceptedidentity/结构/类型/数值误差/错误类型与公开文本选择可区分assertion；referenceidentity有时正是contract，不因object就必须deepEqual。浮点tolerance由scale/errorbudget/数据源而非随手precision5，过松/NaN等需具体negativecontrol，多个字段assert可证一个完整contract。weakassert并非永零证据，区分其真覆盖/漏错；sourceJest形状不认证当前library语义。 |
| T5 AAA/mock/async/余示例 | 大部覆盖；await/隔离以条件合并，API形状留reference | setup→act→observableassert可不按固定sections；缺await/return导致结束前异步错误未归run可falsegreen，需用framework真实完成/timeout机制，callback合法不强语言await。setup/cleanup隔离按sharedresource/claim，knownsnapshot需审实际diff；boundarydouble不替productionmapping。sourceAPI/fixturetoken/plaintexts仅示例，无当前consumer不搬；原因是实际need/版本而非API无价值或代码后缀。要实际复用再核当前工具/fixture授权。 |

## 下一合法动作与残余

Driver可安排性能/cache/query/pool支线与当前performance合并，正确性边界按实际contract互指；a11y三支线按需共同carrier；test-pattern与F1/当前guides合并。S1/S2/O2已充分coverage者只保source/贡献；不得把source版本矩阵、规则编号、资产表、工具安装或清单勾选当当前acceptance/动作权。现有cache/source重合不计多新增mechanism。

无新增承重读源缺口阻碍这些文本裁定；完整frontend其他designsystem、具体manager/SDK/db/测试版本/validator/helper/runtime余部未认证。来源“已读待用”清单只定位，不把原A的read-depth传给B或gate；要扩newclaim才补其original/执行。没有任何DB/浏览器/Provider/a11y/eval安全或性能效果观察，不认证全标准。B须直接读对应原文后交固定diff独立复核，本两review不写产品、不派工、不用Pro、不造platform。
