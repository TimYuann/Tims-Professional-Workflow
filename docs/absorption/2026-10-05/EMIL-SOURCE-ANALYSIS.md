# Emil Kowalski skills → TPW 下一轮吸收研究

研究日期：2026-10-05。状态：**只读分析；未实施吸收；未接受新方法；效果未验证**。

## 结论

建议把这个来源作为 **UI 动态行为的专业案例与观察操作来源**，优先蒸馏四类机制：

1. 写动画之前，先证明它值得存在：真实使用频率、目的、信息阅读/操作代价，以及保留静态/更少动作的选择。
2. 把交互的生命周期、可中断性与当前呈现状态写成可观察合同：快速重复、反转、取消、退出、重新抓取等不能只看最终截图。
3. 用同一数据边界喂现实负例：先查字段及真实限制，再测空/单/大集合、缺字段、长短/多语言文本、失败状态与真实容器。
4. 用真正可玩、能重播的同条件比较与逐帧观察验证；代码/样式存在、框架配置、静态截图不替代真实交互与渲染证据。

**不建议整库 vendor 或照搬它的专业审美 gate。** 来源把频率、曲线、300ms、动画属性、库清单和报告格式写成强偏好；它们可供比较与实验，不能自行成为 TPW 或 UCBIP 的接受条件。TPW 已有原型、方案比较、真实浏览器证据、可访问性和性能方法，下一轮应加具体操作/反例，避免再增加平行方法平台。Swift、Expo 和 Sonner 的具体配方在没有对应任务消费者时保留来源索引即可。

## 固定对象与读取范围

| 对象 | 固定身份/读取结果 |
| --- | --- |
| 来源 | `emilkowalski/skills`，commit `e8a175de22ae1e49370fc144c1f3bb9aeedf988d` |
| 只读本地路径 | `/Users/yuantian/Developer/tim-professional-workflow/.worktrees/source-intake-2026-10-05/emilkowalski-skills` |
| TPW 比较基线 | `main@1f95f0650638b6b6fbc892dcb697dbad4da86fa4` |
| 内容读取深度 | README、LICENSE、全部 **14 个 SKILL.md**、全部 **9 个支持正文**（8 个各 skill 附件 + `performance-cheatsheet.md`），共 **25 个内容文件 / 4710 行**；逐篇实读，长文拆段，工具截断部分补读 |
| 其余 tracked 文件 | `.gitattributes`、`.gitignore` 实读；`.pl` 空文件。Git 树共 28 个文件；未发现其他 tracked 支持正文 |
| 未读项 | Git 历史、README/skill 链接的文章、WWDC 原视频/样例、各第三方库当前官方文档/API源码、安装后的宿主环境与 runtime；未把这些写成已验证来源 |
| 未做动作 | 未安装、未执行源中的命令/指令、未启动测试/浏览器、本子任务未改源仓或 TPW 方法、未新建子代理；分仓草稿仅写入 /tmp，最终由主研究者集成 |

README 将内容定位为面向设计/工程的经验性 skill，并称源于作者在 Vercel/Linear 的经历。这是作者对来源与目标的说明，不是本次方法效果验证。[README L10–18](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/README.md#L10-L18)

### 许可事实

仓库 `LICENSE` 为 **MIT License**，版权行为 `Copyright (c) 2026 Emil Kowalski`；其许可列举使用、复制、修改、合并、发布、分发、再许可、销售，并要求在复制品或实质部分中保留版权与许可通知，内容按原样提供。[LICENSE L1–21](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/LICENSE#L1-L21)

若后续实际吸收复制/蒸馏 substantial source 内容，应保留此来源、pin、路径/段及版权/许可通知。此事实不替代对源外 WWDC、链接文章、第三方库与资产的许可核对，也不授权向 TPW 发布/合并新语义。本文没有执行这种吸收。

## 全部 14 个 skill 的吸收机制矩阵

| Skill / 固定来源 | 可蒸馏的操作或例子 | TPW 现有重叠/建议落点 | 必须限缩或留待验证 |
| --- | --- | --- | --- |
| [`emil-design-eng` L62–145](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/emil-design-eng/SKILL.md#L62-L145)；[L557–656](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/emil-design-eng/SKILL.md#L557-L656) | 先是否动画→目的→取值；动态 UI 的中断/边界行为；timer hidden-tab、快速添加 toast、慢放与逐帧等具体反例 | `cross-module-design` 的机制必要性；`behavior-contract-examples` 的动态行为例；`verification-harness-design` 的 motion 观察 | “品味不是偏好”“美带来差异化”、下载量、速度感知为来源主张；100/day、全禁键盘动画、指定曲线、表格格式不升级成 core 规则 |
| [`animate` L39–96](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/animate/SKILL.md#L39-L96)；[L143–201](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/animate/SKILL.md#L143-L201) | 是否需要运动→目的→最轻足够工具→属性/中断/退出→降动作与输入能力→实际 feel-check；明确“不写动画”也可为成功 | `cross-module-design` 与 `design-alternatives` 的“不新增/复用”候选；可选 UI motion 操作段 | 原文 gate 与永不允许值是作者标准；CSS/WAAPI/Motion 能力/性能需以目标版本/浏览器实际确认；不自动装库、不强制全部按序适用 |
| [`review-animations` L27–82](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/review-animations/SKILL.md#L27-L82)；[L110–120](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/review-animations/SKILL.md#L110-L120) | 必要性、频率、中断、origin、性能、a11y分别查；先删除/减少再调曲线/物理性；不确定手感明确提出观察 | `change-review` / F 的专业检查例；motion 改进建议需分证据与审美判断 | “default flagging”“Block/Approve”、十条无协商标准、固定表格不作为 TPW F 三态或接受政策；纯 fade 与非GPU形状不能凭语法判产品 FAIL |
| [`improve-animations` L38–94](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/improve-animations/SKILL.md#L38-L94)；[PLAN-TEMPLATE L50–72](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/improve-animations/PLAN-TEMPLATE.md#L50-L72) | 先查实际 stack/tokens/频率与上下文→实读确认发现→按影响/改动成本排序→可冷读计划；机械检查与明确 feel-check分开 | `architecture-survey`、`technical-planning`、`handoff-and-resume` 已有同类归属；补 UI 计划具体观察项，不新建 audit平台 | 不移植固定8类全扫/代理计数/计划目录/默认top3–5/弱模型零taste/先等用户选的固定仪式；“注释写了 deliberate tradeoff就不报”应核有效接受依据 |
| [`find-animation-opportunities` L20–75](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/find-animation-opportunities/SKILL.md#L20-L75)；[L105–140](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/find-animation-opportunities/SKILL.md#L105-L140) | 按频率/目的/速度/功能过滤候选；记录具名拒绝对象及哪个条件不满足；零候选是正常结果 | `design-alternatives` 的受约束选择与 `decision-record` 的拒绝理由；与上一轮必要性建议最贴合 | 不要求每轮5–7建议/2–5拒绝/每类清账；频率须来源可核，不凭估计造100/day；“最有价值”需真实用户任务而非趣味 |
| [`animation-vocabulary` L28–35](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/animation-vocabulary/SKILL.md#L28-L35)；[L96–141](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/animation-vocabulary/SKILL.md#L96-L141) | 把看见/感到的模糊描述映到名称；相近概念对比，说明近似与未知；presentation、中断、连续性、velocity用词可帮助跨角色解释 | `domain-language` / `guide-professional-explanation` 的 UI 示例；少量词解释支持行为讨论 | 词库是作者快照，不作为canonical领域词典；“必须逐字引用、只能词表内”不移植；60/120fps、GPU/布局说法不是运行保证 |
| [`apple-design` L28–118](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/apple-design/SKILL.md#L28-L118)；[L207–271](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/apple-design/SKILL.md#L207-L271) | 反馈与提交分离；拖动尊重抓取点；presentation值→中断/反向与速度handoff；降动作/透明度/对比度独立适配；交互原型/真实context | `behavior-contract-examples` / `domain-state-and-invariants` 动态UI合同；`guide-accessibility-observation` motion/材料例；`verification-harness-design` 中间帧 | WWDC 2018/2020/2026 的归因未经本次原源核验，不能称已核Apple规则；固定spring/投影/阻尼、强制玻璃材料、所有键盘/手指规则不可无条件推广 |
| [`write-swift` L18–31](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/write-swift/SKILL.md#L18-L31)；[L111–170](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/write-swift/SKILL.md#L111-L170)；[L226–267](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/write-swift/SKILL.md#L226-L267) | 先简单具体表示；需要身份/共享才reference；测到成本才并发/优化；await后假设重核、演员互斥≠事务、取消≠停止、bounded task；algorithm first/profile second | 很多已在 `domain-state-and-invariants`、`interface-contract-and-retry`、`performance-and-neutrality`、handoff中；没有Swift消费者时**暂缓专门吸收** | Swift6.3/6.4发布/能力、默认Actor/build settings、Testing精确API、ARC/unsafe/类型保证均需官方/toolchain复核；noncopyable不能替跨进程/重试的“副作用仅一次”保证 |
| [`pick-ui-library` L17–24](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/pick-ui-library/SKILL.md#L17-L24)；[L26–85](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/pick-ui-library/SKILL.md#L26-L85) | 先认任务需要、查package中既有依赖；不为作者推荐而换竞争库；简单fade不需motion库 | `design-alternatives` / `cross-module-design` 复用既有合适机制；不加选型列表到core | 清单是这个pin的作者偏好，未核现维护/许可/兼容/功能；Base UI/Sonner/Virtuoso等不能写成2026通用最佳；不把手写一概判错 |
| [`prototype` L25–80](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/prototype/SKILL.md#L25-L80)；[PICKER L124–138](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/prototype/PICKER.md#L124-L138) | 实质不同的轴→同context/token；全尺寸真实邻接、一次展示一个；instant切换、可重播/地址持久、输入焦点不截快捷键；每variant真的操作 | `bounded-prototype` 已有绝大部分；补全尺寸/重播/shortcut不抢焦点的UI观察例即可 | 不移植固定3/5、指定pill皮肤/max-z-index、生产升格/默认删除资产、所有选择等用户；source要求默认删与TPW当前保存可恢复证据存在冲突，应保TPW约定 |
| [`mobile-native` L29–35](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/mobile-native/SKILL.md#L29-L35)；[L86–221](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/mobile-native/SKILL.md#L86-L221) | 先症状→why→最小平台机制；按输入能力而非设备猜测；动态viewport/软件键盘/安全区/可复制内容；touch-action轴owner；硬件观察诚实报告 | `guide-accessibility-observation` / `verification-harness-design` 的触摸与viewport例；不新移动角色 | `16px`、300ms delay、Tailwindv3/v4、env/meta行为与“模拟都复现不了”是目标环境要复核的说法；root全局禁overscroll/全局tap反馈替换/控制文字不可复制需任务语义 |
| [`break-ui` L24–89](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/break-ui/SKILL.md#L24-L89)；[L117–160](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/break-ui/SKILL.md#L117-L160) | 逐字段查真实source/limit/optional；同data边界不改CSS制造bug；现实且schema-backed极值、空/单/大集；真实容器+zoom/RTL/touch；报告破损与保持面、设计选择分开 | 本次**最高优先案例来源之一**；`behavior-contract-examples` + `verification-harness-design` + `guide-test-evidence-quality` 的真实UI反例 | “所有catalog都测”、320px/200%/1000行、每发现都停等修复不作通用gate；CSS签名只是诊断候选不是根因；无browser时推断不能称真实视觉已验证；输入无上限本身也不自动是缺陷 |
| [`ask-sonner` L20–57](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/ask-sonner/SKILL.md#L20-L57)；[L72–88](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/ask-sonner/SKILL.md#L72-L88) | loading→成功/错状态、stable id更新vs重复、手动dismiss vs自动超时、promise永不settle、root/portal堆叠与SSR/client边界；排查具体症状 | 小部分可作 `interface-contract-and-retry` / UI lifecycle正反例；具体API仅给Sonner消费者 | API/defaults未绑定Sonner包版本；“一Toaster”“classes需!important”“headless推荐”不移植成通用组件政策；多个toaster target语义要实际核 |
| [`animate-expo` L43–82](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/animate-expo/SKILL.md#L43-L82)；[L151–213](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/animate-expo/SKILL.md#L151-L213)；[RECIPES L125–207](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/animate-expo/RECIPES.md#L125-L207) | 区分state切换vs连续输入；别让每帧反馈回React工作；一次action/threshold反馈、gesture轴与scroll共存、当前呈现值、中断关闭callback、实际release/代表性设备观察 | UI lifecycle/测量负例有价值；具体Expo/Reanimated4消费者缺席则**暂缓专门吸收** | 版本API/线程/NativeTabs/Link.Menu/架构/Expo安装都未核；“手指都必须spring”“RN runtime必抖”“transform免费”不能当通用事实；实际fps/性能需测 |

### 支持正文的覆盖与用途

9 份支持正文均完整读取（下表 8 个附件，另列全局 cheatsheet）；它们不是各自新增一个 TPW 方法：

| 支持文件 | 可用部分 | 边界 |
| --- | --- | --- |
| [animate/RECIPES L29–324](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/animate/RECIPES.md#L29-L324) | popover/modal origin差别、tooltip群组跳过重复延迟、toast中断、accordion成本、drag边界、多指/捕获；可提取场景 | 实现框架/数值和全部代码不必移植；hold-to-delete仅视觉配方，未定义授权/副作用安全合同 |
| [animate-expo/RECIPES L47–385](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/animate-expo/RECIPES.md#L47-L385) | 先查native sheet/Swipeable；presentation值重抓、callback仅finished；虚拟化row重复入场；keyboard真实位置；gesture轴、threshold一次事件 | SDK/API版本未实际跑；示例代码不是安全证明；haptic精确同帧和线程/取消行为要真实设备验证 |
| [review-animations/STANDARDS L5–187](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/review-animations/STANDARDS.md#L5-L187) | 场景目录、明确候选配方、慢放/逐帧/真实device观察问题 | 整体是作者review标准，不作为TPW accepted policy；举值保留source上下文 |
| [improve-animations/AUDIT L5–115](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/improve-animations/AUDIT.md#L5-L115) | purpose/frequency与source-token recon；中断、pointer、动静选择、只报真实UX seam | 不机械逐8类；grep只作查找线索，不升级成finding |
| [improve-animations/PLAN-TEMPLATE L14–73](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/improve-animations/PLAN-TEMPLATE.md#L14-L73) | 当前对象、exemplar、目标值、边界、独立机械/feel证据与明确done；快速反复/降动作负例 | 不用每个文件excerpt规定E helper；漂移只停实际依赖；目录/status不建立第二状态源 |
| [prototype/PICKER L124–197](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/prototype/PICKER.md#L124-L197) | 不遮目标、replay、stable URL、每次切换重置、keyboard排除editing/modifier | 严格皮肤/max-z-index/innerHTML无直接core消费者；源码初始URL index若越界会无active，具体picker应先验证而非称现成已可靠 |
| [break-ui/CATALOG L9–135](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/break-ui/CATALOG.md#L9-L135) | 字形/locale/grapheme、identifier尾部区别、page-size+1、时区、媒体fallback、partial/no-permission、touch/RTL/zoom负例 | 以产品真实输入/支持政策选子集；catalog的“现实值”是候选，不替产品合同/真实分布 |
| [ask-sonner/API L5–64](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/ask-sonner/API.md#L5-L64) | source pin中的作者API表及事件语义查找 | 没有依赖版本或运行证据，真实任务先核自己的包与官方API；不称2026通用API |

独立 `performance-cheatsheet.md` 仅有短提示表，可用“`will-change` 只在见到症状后考虑”和测量问题的线索；其“全部Motion shorthand会掉帧、blur20px”等不作为已验阈值。[cheatsheet L3–11](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/performance-cheatsheet.md#L3-L11)

## TPW 已有覆盖与真实增量

| 待吸收机制 | 已有 TPW 覆盖（基线 `1f95f06`） | 本来源真正新增的可用细节 |
| --- | --- | --- |
| 设计先判断价值/必要性，不加无用结构 | `cross-module-design` 删除思想实验/薄wrapper例外、`design-alternatives` 已接受约束；前轮已建议明确前置机制必要性 | motion的频率×功能目的例；“无动画/更少运动”合法选择；明确记录被拒候选，避免一味找可加内容 |
| 交互可观察合同 | B/C Profile与`behavior-contract-examples`已有行为/语义/反例、`domain-state-and-invariants`已有状态/转移 | 当前presentation vs logical target；快速重复/取消/反向、重抓、键盘/gesture竞争；exit后何时才允许结束状态或callback |
| 原型比较 | `bounded-prototype`已有明确问题、隔离、同真实条件/结构差异、switcher、实际interaction、恢复证据 | 一次全尺寸在真实邻接context呈现，明确variant轴、可重播、选择URL、shortcut不抢editing；大多是例子增量，无须平行prototype方法 |
| 真实验证 | `verification-harness-design`已有真实目标、实际动作+结果、负例/效果范围；F已有三态/independence | motion的中间帧/慢放/逐帧问题；快速反转、hidden tab、双输入、软件keyboard、回收row、真实device的观察边界 |
| UI negative controls | `guide-test-evidence-quality`独立oracle/反例；behavior contract可证伪 | break-ui字段source/实际limit→同数据边界，空/单/极大/长短/locale/permission/media失败交叉，真实容器而非只看viewport |
| 可访问性 | `guide-accessibility-observation`目前侧重keyboard/focus、semantics、noncolor/live announcements | 新增on-demand reduced-motion、pointer/touch、多输入、viewport/zoom、透明度/对比度例；不从原表抽数值当合规认证 |
| 性能 | `performance-and-neutrality`已有测量/工作量/真实interaction trace、输入/处理/presentation分解 | animated属性/每帧state/父CSSvar/布局回流作为待核假设与小负例，绝不绕现有“先有测得问题再优化”纪律 |
| 选择第三方UI库 | `design-alternatives`既有依赖策略与跨模块责任 | 作者库表可供需要时检索线索；不在core维护当前推荐清单 |

TPW 覆盖原件：[cross-module Step 1–4](/Users/yuantian/Developer/tim-professional-workflow/professional-workflow/methods/cross-module-design.md:12)、[方案 Frame](/Users/yuantian/Developer/tim-professional-workflow/professional-workflow/methods/design-alternatives.md:10)、[可证伪行为条件](/Users/yuantian/Developer/tim-professional-workflow/professional-workflow/methods/behavior-contract-examples.md:14)、[状态问题](/Users/yuantian/Developer/tim-professional-workflow/professional-workflow/methods/domain-state-and-invariants.md:10)、[原型已有同条件/真实switcher](/Users/yuantian/Developer/tim-professional-workflow/professional-workflow/methods/bounded-prototype.md:24)、[真实验证与adapter](/Users/yuantian/Developer/tim-professional-workflow/professional-workflow/methods/verification-harness-design.md:35)、[a11y当前范围](/Users/yuantian/Developer/tim-professional-workflow/professional-workflow/methods/guide-accessibility-observation.md:5)、[性能测量与interaction分解](/Users/yuantian/Developer/tim-professional-workflow/professional-workflow/methods/performance-and-neutrality.md:28)。

### 建议落点与最小切片

**A. 优先：`cross-module-design` 的必要性段 + 一个 UI例。** 先核真实用户问题、完成单位/生命周期/fact owner；若新增motion/身份/状态机制，说明静态或既有路径无法满足哪项接受行为。Emil 提供目的/频率/功能限制例，TPW仍保留B/C裁定。不要把“键盘触发都不准动画”作为owner尚未接受的硬规则。

**B. 优先：`verification-harness-design` 的动态UI与现实数据观察例。** 用一个说明性例子把真实trigger、对象版本、输入/环境、关键中间帧与terminal、实际可证伪观察绑起来；补 `break-ui` 的字段/数据边界步骤。既有方法已十分长，若实例集使正文难读，可以把案例放外部示例并从所拥有的段落指向；不另建UI职责或强制全套audit。

**C. 其次：`guide-accessibility-observation` 的 motion与输入能力 on-demand段。** 增加“降动作后还可理解/可操作、touch上hover功能仍可达、键盘/焦点不被动画锁住、zoom/keyboard不遮提交/退出”等可观察不变量。动画存在、media query存在、库原生示例存在都不证明效果；标准值仍由真实accepted policy决定。

**D. 其次：`behavior-contract-examples` 的 presentation/terminal反例和 `bounded-prototype` 的全尺寸重播例。** 当前logical target与屏幕中途状态不同、取消/exit后的callback只有一次，示例必须引用实际accepted behavior，而非把每条消息/每次paint当完成单位。原型对实际选择提供证据，生产合同/授权/qualification仍须重新成立。

**E. 暂缓：独立Swift/Expo/Sonner方法与固定库推荐。** 只有当真实任务已绑定技术栈/版本/具体claim时，核官方API和最小运行样例，再决定蒸馏到相应现有方法还是留项目侧配方。不为吸收完整而补对称章节。

## 与 UCBIP 实务的对应

1. **turn/message 与 working 生命周期。** 源库的运动关注状态可见性和中断；它不能裁定UCBIP业务完成单位。正确使用是先由对应owner固定完成/working终态，再观察同一承诺在快速输入、流式成员到达、完成/取消路径的实际呈现。不能由 `animationend`、某条message结束或toast消失推断turn终态。TPW已有F规则：测试绿不证明价值，符合Plan不证明责任放置正确。[F既有边界](/Users/yuantian/Developer/tim-professional-workflow/professional-workflow/profiles/evidence-evaluation.md:12)
2. **同帧双显/Markdown归段。** Emil的blur-mask crossfade是审美配方；UCBIP若接受的合同是同帧零双显、跨锚不污染，blur不能把错误事实伪装成单一感知，也不能使候选资格成立。应录下真实帧和实际内容归属，再按合同判断。静态最终截图或“看起来过渡顺滑”不替负例。[blur来源例](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/animate/RECIPES.md#L292-L309)
3. **减法后的必要能力。** “删/减少motion先于polish”有价值，但只对非必要动画成立；不能用少DOM、少层或短duration作为功能保持证据。减少后还要核关键工作状态反馈、焦点/操作、隔离/权限等原承诺。源中的无动画成功例可用于提醒减少机制，而非替下游守门。[减法层次](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/review-animations/SKILL.md#L70-L82)
4. **页码/完整关系与现实负例。** `break-ui` 可让fixture输入来自真实schema限制，并多样覆盖空/单/边界；它没有定义实际Item页、declared face页与final row页应等集的语义。那是领域/行为合同，先派生独立expected再真实驱动生产路径。不能为了制造/消掉反例手改CSS、数据或合同。[相同数据边界](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/break-ui/SKILL.md#L29-L36)
5. **实际工具面与UNKNOWN。** 源skills承认没有browser/device时手感未证；可补前轮只读监督教训：Charter要求获取motion/terminal/设备证据前，必须确认真实工具可用。静态源码最多支持语法/实现观察，不从“加载了专业skill”推断真实UI或监督已生效。

以上是将来源机制应用到已知问题的**研究推断与建议**，不是UCBIP效果已验证的事实；没有重跑UCBIP候选、隔离、Full或Office。

## 源内例外、冲突与必须限缩的默认

| 源里写法 | 核到的例外/冲突或范围问题 | TPW 蒸馏处理 |
| --- | --- | --- |
| UI一般under300ms | 同源drawer500ms、toast400ms且明确个性化取值；Expo toast反称300ms严格。[web recipes L107–151](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/animate/RECIPES.md#L107-L151)；[Expo L344–363](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/animate-expo/RECIPES.md#L344-L363) | 保留“为什么这段响应需要/允许这段时间”的问题，参数来自项目policy/真实测量与偏好；不创建300ms universal hard gate |
| only transform/opacity；非GPU即finding | 同源accordion height与picker width例外，Apple materials又建议blur；position/layout性能受engine/形状/负载影响。[accordion L155–166](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/animate/RECIPES.md#L155-L166)；[PICKER L124–128](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/prototype/PICKER.md#L124-L128) | 作为profiling假设：trace layout/paint/composite、操作duration/flow依赖；不凭属性名判所有产品FAIL |
| Never keyboard animation /100+day不动画 | picker键盘切variant内容instant，但highlight仍动画；source并不能证明所有键盘场景都是100/day。[picker L127–138](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/prototype/PICKER.md#L127-L138) | 使用实际频率/目的/可操作性；nearby合法低频键盘反馈作反例；不无条件禁止 |
| purefade/no-transform入口被flag | source同时要求reduced-motion保留opacity/static；模态/不同产品也可能接受纯fade。[review L53–66](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/review-animations/SKILL.md#L53-L66)；[apple reduced L207–224](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/apple-design/SKILL.md#L207-L224) | 不将视觉得分当合同；保留可理解且可操作的静态/轻反馈分支 |
| 绝对同frame haptic/visual | Expo给worklet→RN scheduling，实际时序与硬件availability未测。[Expo L182–188](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/animate-expo/SKILL.md#L182-L188) | 描述对因果与同步的目标、能测的容差和实际限制；不声称scheduler保证同frame |
| “现实catalog”“cause almost always” | CSS signature可以有其他原因；任意很长input可达性取决实际合同；后端更长column不必意味着更长值必出现。[break-ui L93–115](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/break-ui/SKILL.md#L93-L115) | signature是竞争假设；field limit查所有真实writer/normalizer，保留诊断证据；不假定所有输入合法或加limit即正确 |
| 原型必须用户选择、默认删除 | TPW已由Charter决定接受authority；当前方法要求可恢复原型/决定证据，不默认丢弃；固定原型样式也不是产品规则 | 保住TPWaccepted owners与custody，不移植源的自动promotion、删除/固定确认流程 |

源中对GPU、Motion shorthand、WAAPI/clip-path、parent CSS变量、Swift/Expo版本等技术说法只作为**这个pin的源码主张**。本轮未查当前官方原源或目标runtime，因此不把它们写成2026已验证事实，也不凭它们推荐迁移技术栈。

## 可证伪验证建议（未执行）

方法效果与产品资格分开；每题记录输入版本、模型/host/tools/resources、是否已见答案、实际输出与原件。先对旧方法/最小新段做同题控制，避免模型、工具和文本同时改变后归因给skill。

| 待验证的增量 | 未泄露答案/代表性输入 | 成功与失败怎么区分 | 证据边界 |
| --- | --- | --- | --- |
| 必要性/减动作 | 一个高频操作与可读数据界面提议装饰运动；一个确有状态/空间反馈缺口的邻近题 | 主动核实际目的/频率与完成单位，能拒绝无用motion也能保留必要反馈；不能一律删 | 不先喂“应该删/turn单位”答案；少代码不是效果指标 |
| presentation与terminal | opening期间反转、closing期间重新抓、连续两次trigger、取消与重复callback；原合同/基线明确 | 无逻辑/呈现jump；输入不被非必要锁住；只按accepted terminal结束工作状态；记录反例帧 | 真render与实际input负例；源码轨迹或终态截图不足 |
| 现实data负例 | 真field/accepted limits、空/单/page-size+1、长identifier尾不同、RTL/missing权限/慢媒体 | 仍可识别/读取/操作，失败准确归到数据/布局/产品决策；演示与负例都复核 | 合成fixture只能证明fixture条件；真实接口有自己的证据腿 |
| reduced-motion/pointer | 同场景在reduce、keyboard、touch/混合输入、zoom与软件keyboard | 可读反馈/退出/提交仍可达；motion更轻不靠hover独享功能；不复制数值装合规 | media query/API存在不是browser/assistive/device结果 |
| 性能说法 | 原accepted interaction在固定版本/设备/负载，CSS/JS候选或父var/直接transform差异 | trace实际显示所猜瓶颈；同条件measure；当前CPU/渲染条件下效果/噪声说明 | 只支持实际测试版本环境；“纯CSS”不自动60fps，换属性不自动用户更快 |
| 原型比较 | 同条件/真实context的不同轴，输入焦点、invalidURL variant、replay | 每个variant可操作且可恢复；switcher不遮目标/抢输入；replay从明确初始态；差别确实关于问题 | prototype不是生产acceptance；源picker须验证行为而非copy即资格 |
| 装配与能力 | 已绑定UI方法、但browser/phone工具不可得；旧worktree缺治理输入 | 精确报哪项claim缺证据/UNKNOWN；能继续合法静态或captured证据，不假全局产品FAIL/健康 | 实读只证明加载；未证新段运行有效 |

对“快spinner让加载感觉更快”“spring/blur更自然”“某curve更好”“首次tooltip之后无延迟更好”的结论，若要升级成用户体验效果，应有相同任务条件下的交互比较或用户观察；源码作者解释不是TPW自身效果。对“同帧零双显”这类已接受硬合同，直接有效反例可判违约，不需把它改成主观投票。

## 吸收决策建议

**候选接受（仍需相应责任方评审）：**目的/频率/功能前置必要性；presentation与中断负例；同data边界现实UI负例；慢放/逐帧/真实interaction观察；reduced-motion/pointer条件；全尺寸/可重播原型的具体例子。

**索引保留、不内联复制：**animation词汇完整库、所有web/Expo配方、Sonner API、作者库清单、Swift全面指南。只有真实任务缺这种知识时读取固定原源并核目标环境。

**明确不吸收为core默认：**固定100/day、300ms、curves/spring、velocity、blur20px、1000行阈值，强制GPU-only、禁止所有键盘/纯fade、固定代理数量/计划目录/表格/审批等待、全局安装/自动promote/删除、作者推荐库即当前通用最佳、source声称性能即TPW验证。

**暂缓直到有消费者与验证：**Swift6.3/6.4、Reanimated4/Expo/新architecture具体技术规则；WWDC原source归因；实际硬件性能/gesture/haptic效果。不要以来源丰富为由扩大TPW任务边界。

按上述切片推进时，先增现有方法的最小操作例，再做盲案例/运行观察；如果没有测到改进，保持UNKNOWN或拒绝该增量。源库丰富的是专业判断的细节，它没有替TPW解决“规则已写→实际加载→实际判断改变→结果更好”的证据链。
