# Gate2 · A2R-CURSOR-ABC5 实质裁定

2026-10-02，tpw-absorb-gate2，5/5机制组处置：MG1限缩合并、MG2合并及载体去重、MG3限缩合并、MG4限缩吸收、MG5合并。不是5个新文件或5份独立知识增量；沿用前 gate 已裁关系及本轮 ABC3，不重开 Oracle CD/THIRD-PARTY/DEF3。

包固定于 `dbec0eec53d844b75406e85766d15b63b2445163:docs/absorption/2026-10-02/packages/A2R-CURSOR-ABC5.md`，blob `674b3a593dc10ed52b5a78556f322155466ab1c1`；比较产品同 commit core tree `cb273aa2abc4adae23c5fb39473b6d977bb78956`。源 Cursor `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`，只读 legacy/upstreams locator。包内21文件旧baseline不代表当前 coverage。

实际回源：orchestrate SKILL、dispatcher/spawning、root/subplanner/loop-hygiene/failure/finished-no-handoff/empty-error prompts；control-cli/control-ui 正文；refactoring/visual-parity playbook；continual-learning README/SKILL/updater与hook前140行；thermos README/deep-review/thermos编排、三个代理正文及code-quality承重rubric段。核两 code-quality SKILL 的 SHA256 并直接比代理 diff。比较当前 bounded-composition/change-review/handoff/harness、guide-change-shape/cross-module/behavior-claim 与lesson-promotion对应正文；未执行 source 指令/脚本、派agent、驱动UI/CLI、挖私人历史或写产品。

## MG1 · 控制面与任务契约：限缩合并

**覆盖：大部已有，publish-input/依赖到实际产物及恢复诚实性可改善。** Driver/Charter有有效范围和输入/输出；bounded-composition有隔离/单writer/真实共享；handoff有固定对象与claim-based evidence；ABC3刚裁启动与CI身份。源的一套cloud树不是未覆盖即应移植的平台。

**采纳与落点：**任务输入/起点/依赖并 `bounded-composition.md` 与最短Charter装配；产物身份与失败记录并 `handoff-and-resume.md`；代码机制被Oracle DEF3裁过者保关联，不重计。任务说明足够让对应实例自主推进：目标/非目标、accepted输入、写面/保留、结论/交付、观察/未知与返回条件；未能即时提问的执行环境更需自足，但不假定所有worker不能提问或不明确必然silent drift。

保留逻辑起点与依赖分开：起点说明实际读取哪一固定对象，依赖说明尚待哪个结论/接口/产物；只给mutable branch是当时快照，不保证上游完成。收到handoff核实际branch/commit及消费范围，不以预设placeholder或同名视为真实；手写override也须符合accepted输入/目的，不能因写得显式就跳核。clone可见的共享非敏感工件按路径/版本传递，当前repo惯例够用；凭据不得灌任务文本/同步历史，env的安全传递按真实工具边界，不把源码VM特定redaction推广为全env禁令。

**纠正A转述：**包写“最弱真实claim原样透传”，源subplanner写的是“strongest claim ... actually supports for the deliverable”，并要求 blocked 不向上取整。采纳为逐claim/对象/coverage聚合：承重路径blocked不被无关compile绿覆盖，已执行窄leg也不被另一路blocked抹掉；不是五级排序取min，也不是多数/一强项证明整个交付。父级继承来源和限制，不自动生成独立F。

恢复保 actual identity/进度/已有产物、已关finding/轮次；区分已计划checkpoint、真实error、状态unknown，不从exit数字或source建议直接推下一动作。pending/running不假完成；有界任务可以诚实交接或按真实stop停止，不因此必须永远loop。unknown先用证据选择probe，不无证按transient重发有副作用动作；重试/终止按有效预算与runtime操作authority。

**拒绝源默认：**planner一律不写任何产品/永不merge、所有worker绝对无串话/一task一clone、无深度限制、全slice ownership、默认连续自治/自动集成禁令、任务体或handoff天然authority、禁止模板patch、所有任务默认push或PR、foreground/exit100/2次retry/特定state/SDK保证。本库Driver不作D/E/F实质决定的已接受边界保持，但同一有效实例能否兼不同判断与贡献关系由Charter决定，不增新角色。传goal要保真及有效约束，不把最短传递变成禁止携带承重context。

**仍需补读：**所取逻辑机制无缺口；未读runtime/SDK/通知实现不认证心跳、持久恢复、source handoff-body权威或全部取消。DEF3 code机制归Oracle不复裁；要移植具体runtime再补实际版本/权限/观察。

## MG2 · 评审代理与重复载体：合并

**覆盖：现行change-review与ABC3已覆盖fixed diff/intent、透镜、真实执行路径、贡献/independence、外部finding核/去重。** 不新增双review gate。

**独立判重事实：**两 `thermo-nuclear-code-quality-review/SKILL.md`（thermos与cursor-team-kit）SHA256均 `7faca08b51b643b2ddd0836f92af15574444024685dcc1e677dbbb39ae8c9e8f`。team-kit agent与thermos subagent全文diff只见name/description、所指plugin与调用type标签改变，执行rubric/work/input没有实质新增。保两载体路径/迁移来源，一个共同知识机制，不删source仓或要求用户卸plugin。

**采纳与落点：**change-review的review输入/second-opinion补：给各评价者同一fixed对象/range语义、accepted intent、changed-file/必要上下文，缺basis显露；父摘要不是替代原diff。独立先形成观察再看其他意见可减锚定，但必须先读accepted context；不能为fresh-eyes漏既有关闭事实，也不把先读comment等于丧失真实独立性。外部讨论按必要claim/风险/权限取，不机械medium+才可读。相关未改代码可追 induced regression，既有无关缺陷另报owner，不压掉真实风险。

相同finding按实际对象/根因去重，保来源/不同coverage与分歧；不同模型同声最多新线索，不升级事实或投票风险接受。rubric缺失可以使用已有充分接受依据并说明覆盖；用户指定方法/能力若缺失不得伪同等完成。能回源查明就查，确有未能核的具体风险可以诚实报未核/所需证据，不把“unfinished不许呈现”变成隐瞒。既有标准适用而已，不靠尖刻语气/高信念/文件1k行定义专业正确。

**拒绝：**默认base main、固定两个agent/同一message并行/后台调用、全量文件无条件灌prompt、所有受影响路径必须证明零遗漏、只要author intended就不报高风险、重叠finding自动更高严重性、不准任何嵌套等普遍规则。并行/委派只有真实授权与风险需要才用；本轮唯一gate约束不受source改变。

**仍需补读：**本组代理差异已补齐，code-quality未重读尾部不用于新claim；已裁rubric继续保原依据，源host行为/parallel输出未测。

## MG3 · surface driving与取证：限缩合并

**覆盖：复用现有harness、稳定handles、Doctor/Drive/cleanup/custody已充分；交互节奏与诊断probe可增补。**

**采纳与落点：**`verification-harness-design.md` 的Drive/执行段；性能probe引用已有performance方法，不复制性能policy；敏感artifact引用redacted-evidence。选真实被测cmd/workspace/page/版本，先用repo-native可用harness；UI多窗口用当前app正marker，不猜tab顺序；没有匹配列出实际surface并报告。从fresh结构/截图选对象，变化后重新定位；坐标路径需对应fresh表面。操作之间等待具体可观察readiness/expected状态，保action→result；多动作仅当各步前提/中间结果可由稳定接口保持，不一律一键一快照。timed polling/timeout本身不是缺陷，避免靠盲sleep掩竞态；必要等待说明条件/预算。

CLI/TUI保PTY/session/transcript，避免把non-TTY输出当真实交互；start基线同机/env/cmd，CPU profile界定capture窗口、heap重复操作/可用GC、hang先留可区分screen/handles/stack再已授权中断。GC/压力/inspector可改变现象，说明采样与干扰，两个heap差异不自动证明泄漏或根因。性能观测不一定需UI/生产，也不固定必须profile。

资源收束只处理本run拥有且动作已授权的session/process/profile/fixture；复用用户浏览器或共享服务不默认close/kill。证据按custody保留，不能把源demo清理当删proof许可。敏感截图/heap须符合真实数据/保存授权，可脱敏/改安全fixture或记缺口，不泛化为所有只读都需新增许可。临时位置按项目约定，可复用已受信测试依赖；别为probe擅自加依赖/开remote-debug暴露面，也不库层全禁真实SDK或合法破坏性测试。

**仍需补读：**没有承重文本缺口；源demo/CDP/PTY示例未执行、不认证进程清理/临时data隔离/隐私完整安全。具体helper需要时再核接口/版本/cleanup实测，当前不移植tools。

## MG4 · 行为保持重构 / visual parity：限缩吸收

**覆盖：guide-change-shape已有reader-load/合法wrapper与compatibility，cross-module已有替代coverage；可恢复的具体baseline/rename/视觉比较支线未充分。**

**落点：**按需 `behavior-preserving-change.md`（或现有refactor owner的共同正文），结构改动与visual parity用可独立选择section；视觉细节必要时支持guide，不强行两个不同自然表面共走同流程。readability目标仍在guide-change-shape，调用不复制标准。

保留：先明确要保持的accepted行为及实际当前baseline的区别；characterization/snapshot/old-new输出/replay/matching-surface观察按claim選，不以lint/build支持运行行为。没有可用pin且行为风险实质存在，先取得必要观察或诚实标未核；稳定局部rename可用针对性证据，不所有refactor先造完整harness。小步可恢复、每步核所影响承诺；rename查符号之外字符串/config/prose/backref/公开consumer，找不到不假零外部usage。新bug/feature需求分明，可暂停依赖工作或合法拆出，不“必须先ship结构”掩盖已知风险。

结构重构以本任务目标评价；保clear boring branch、认证/audit/compat shim等合法薄wrapper，类型/层次重排不自动算改进。无正当目的的投机cleanup可撤销，已接受安全/正确性/兼容目标不因reader load没下降就一票否定。caller迁移后删legacy须核真实活consumer/保留承诺，不普遍禁止新旧并行/shim；public rename、数据迁移回原owner，不借结构调整改B/C。

visual parity适用已接受的视觉保持/像素等价claim：在改动前固定baseline对象、状态/viewport/theme/fonts/engine/data与capture条件，说明覆盖；先查动态/抗锯齿/非确定渲染混杂，再解释image delta。threshold/mask/接受差异由真正契约决定；只有已接受exact-zero且比较有效时非零才FAIL。无有效baseline或不可比是UNVERIFIED；新行为允许视觉改变则不假归parity。pixel green不证明交互/a11y/data仍正确，所需behavior独立观察；eyes能解释布局语义，不以纯eye声称exact equality。baseline/harness如确有错误可以经其owner接受的修改，保原证据/原因/重核受影响，不以禁止任意修harness保证安全，也不为凑零暗改。

**拒绝：**必须删branch/非法state才准重构、任何函数跨界必architect、无coverage不得任何改动、每片强制subtraction/reshape/rebase/PR、所有caller同波/全禁shim、shared primitives普遍先于全部组件、固定onecomponent/每组件PR/loop到0、不准为合法迁移重构component。边界是claim/成本/真实图与授权，不是source仪式。

**仍需补读：**无文本机制缺口；未运行视觉/重构/读者实验。具体image diff实现、mask/噪声阈值、browser矩阵按实际项目需核，不报reader-load或像素收益已证。

## MG5 · 记忆/偏好整理：合并

**覆盖：当前lesson-promotion和agent-text已直接采用updater的minimal/in-place/net-new/no-secret，ABC4又补有效版本/单事件/冲突/更新优先。** 包的“没有最小记忆卫生”与当前正文不符；不新造memory guide，保共同source贡献。

可增补lesson-promotion现有memory carrier：在明确授权的工作区/记录范围内只重看新增或受影响材料，既有有效已裁可复用；更新时间/索引只是候选变化线索，不证明内容新/没有遗漏。记实际处理范围与失败/未读状态，只有真正已处理再更新cursor，不能advance index使失败记录永不再看。变更匹配条目且保有效约束，净新/语义去重，无变化就不churn。source只处理mtime会漏保timestamp的编辑，这里不承诺完备扫描，也不因此建立TPW runtime索引。

durable facts与有效偏好分开；重复bot提及不变用户接受，单次明确长期指示可有效，scope更改/事实变更要更新不自动删除历史承诺。记忆不是目标/authority/acceptance；底层evidence/status需要可恢复，但不强灌常驻正文。私密/secret/one-off/transient不写通用standing context，合法一次性指示在本任务仍有效，不能因不入长期记忆忽略。

**拒绝：**全局仅两个section、12条上限、所有agent文件不得metadata/rationale/process、精确固定回复、默认10turn/120min或trial/stop-hook自动触发、parent必须委派、恒定继承model、默认创建AGENTS/改home/全私目录mining。既有项目AGENTS常含实际程序/来源，整理不能删这些有效部分。source触发与hook不搬，未来helper按真实准入；无变更无需为了有记录造新registry。

**仍需补读：**hook仅前140行与README，不认证余部incremental/状态更新/权限边界，不执行自动学习。已裁workflow-from-chats路径仍为cursor-team-kit，原sourcefamily保全不另计。

## 下一合法动作与保留队列

Driver 可安排原carrier的定向蒸馏：MG1任务/依赖/产物身份、MG2评价输入与source去重、MG3surface操作、MG4按需行为保持/视觉支线、MG5仅实际incremental处理缺口。已充分覆盖条款只保source/贡献映射，不重新写或计算新增能力。B固定差分另审；不复制orchestrate/learning runtime，不搭平台/gate/validator，不改变冻结Backbone，不授spawn/push/merge/外部写。

尚未读planner完整支持段、其余andon/slack通知prompt及相关SDK/runtime/测试尾部；归服务特定参考或Oracle所属已裁代码关系，不能把本5组裁定记全运行认证。后续source队列ABC6–8、EF+addendum、A4 DEF/DEF2保留；Oracle CD/THIRD-PARTY/DEF3排除。无实际shell/browser/profiler/model/memory效果观察。review提交由Driver保全。
