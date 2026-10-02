# Oracle / Codex · A1-ADDY-CD 实质裁定

2026-10-02，审核者 tpw-0930-oracle（GPT-6.1 SOL medium）。9/9 机制组已作实质裁定：C2/C8 合并现有候选；C1/C3/C4/C5/C6/C7/C9 限缩吸收。含可落地工程经验，不以宿主耦合或“避免流程化”整体排除。此为源机制裁定，不是尚未产生的产品 diff PASS，不代写被审正文。

## 对象与回源

- 包：`6b64b594916b679e0193a58dd35d032d25a00e79:docs/absorption/2026-10-02/packages/A1-ADDY-CD.md`，blob `f5746caa7aad3d2828a6b87f5445c6822b38e156`。
- 源：Addy `2686b620fc1fed2e8f60c704839c766b8594c6b6`，legacy/upstreams 工作树核 pin 相同、干净；源只读。
- 产品比较：已接受旧 core `7c814e54…` 与第一整合切片 `6b64b59:professional-workflow`（`7dcac80f…`）；已读现有 Backbone、Profile、三方法和两 guide；核在飞 `absorb/w1` 的 decision-record、domain-state、cross-module 等候选，不把在飞覆盖当正式接受。
- 本次读源：api-and-interface-design、documentation-and-adrs、deprecation-and-migration、shipping-and-launch、security-and-hardening、observability-and-instrumentation、planning-and-task-breakdown、performance-optimization 的 SKILL 正文；constraint-driven-development 各节（分段读回）及 floor-guard 参考代码；ci-cd 正文与尾部（输出截断处另定向补读 CI Optimization/Automation/Verification）；hardening-patterns 全文、security-checklist 的 §Threat Model 至 §AI/LLM（含 destructive path 及 install-script gate）。definition-of-done、observability-checklist 这里只核入口/分工，未称全文。
- 未运行上游脚本、安装、服务、Provider；法律义务、具体客户端/浏览器版本矩阵与源宣称的收益未实证。未读到的支持文件不被宣称完整知识落地；下文已给可蒸馏范围，B 若扩展到其正文需补读。

## C1 · 接口、错误与幂等：限缩吸收

**覆盖：**D/E 协调面和边界已有，API/错误/重试副作用操作经验不足。并入已裁 agent-facing-cli-contract 的共通接口层，按需 `interface-contract-and-retry.md`；幂等若需例子可作其独立支持支线。

**保留：**调用者可见行为与依赖盘点、输入/输出/错误/部分更新/分页语义；验证放在实际信任边界。幂等键区分“一次意图”和“重试尝试”；原子占用、载荷绑定、在途重复策略（拒绝/有界等/返回pending）、成功/失败/未知、外呼前持久记录及最长重投路径决定保留期。必须留并发 check-then-act、同键异载荷、超时未知与短 TTL/DLQ 反例，不能蒸馏成“加个幂等键”。

**限缩：**REST 命名、状态码、camelCase、单版本是可选约定，不强迫 GraphQL/内部模块全套形态；已有合法多版本策略可用。新内部稳定函数不因本方法再写 API 文档。数据库数据的可信性取决于写入者/持久不变量，不能因来自“自己的 DB”自动免校验。不可把普通 UUID 全否：发起者为一次意图生成一次 UUID 并在重试复用有效，错误是重试层每次重新生成。原子唯一约束是源示例，不宣称所有可用存储必须 SQL；同等原子机制需给出实际保证。业务去重与幂等尝试去重分开。

**权限/观察：**B/C 决定业务身份和错误含义，D 定协调策略，E 在委托内实现；F 用实际执行路径的并发/异载荷/未知结果反例评价。持久意图记录与外部副作用不在同一事务时，仍需结果调和，不能宣布数据库 UNIQUE 等于跨提供者 exactly-once。代码示例是说明，不授予支付/数据操作许可。

## C2 · 决定为何如此：合并

decision-record 已有 Matt 最小记录与拒绝概念；Addy 补**先匹配现有目录/格式/编号**，决定上下文、选项、代价与显式 supersession，公开契约/操作 gotcha 的记录。不得把 Matt 标题+1–3句改为全任务强制长模板，也不照搬 Addy 示例对 SQLite 的普遍否定。正文位置按项目既有 owner；历史记录保留、现行指针改变，避免第二份规则。对于纯弃用或候选，状态不得写成 Accepted。

## C3 · 弃用与迁移：限缩吸收

新增按需 `deprecation-and-migration.md`，供 D/E/F，B/C 承诺不被技术策略重写。**保留**：消费者/实际使用与未文档化依赖调查；迁移成本与保留成本；advisory/compulsory 的区别和有效决定来源；逐消费路径核行为、引用/配置清理；adapter、strangler、flag 的适用取舍；有旧/新代码共存的持久 schema 用 expand→dual-write/backfill→switch reads→contract，批量回填、索引锁影响、读写一致与数据恢复条件。至少一个跨版本混跑反例和一个无活消费者的纯退役例。

**不照搬**：所有退役必须先造 replacement/生产证明；Owner 可决定终止能力而非迁移。不得要求任何任务都建 flag/并行旧新栈、永远不得原地更名、每迁移有可逆 down。真实不可逆数据变更应声明备份/恢复或 forward-fix、损失与对应风险接受，不写虚假的 down 保证；代码 rollback 不推出数据 rollback。也不以 “零引用”消灭需保留的历史 provenance/reader。

## C4 · 发布、兼容、恢复与放量：限缩吸收

新增按需 `release-and-recovery.md`，涵盖计划与评价，明确部署/启用/验收/关闭不同。保留实际装配、配置、关键用户路径、比较对象/观察窗口、预声明 advance/hold/rollback、可操作恢复路径、数据不可逆性、flag owner/清理和保留态验证。CI 接线引用质量政策方法，不再复制全套门表。

**限缩**：两周清旗、5/25/50/100%、24–48小时、2倍错误率/50%延迟、20% error-budget 等只可作为源示例；采用阈值须由服务 SLO/任务实际预算与 authority 提供。没有真实流量/放量能力时用适用部署与恢复证据，不能编造canary。不是每发布都需 staging、无warning、全部e2e、flag、外部服务、notify动作。保留源“已部署不等于用户能用”的工程机制，不把计划/检查表当发布授权。外部通信与真实部署继承有效委托。

## C5 · 已接受质量约束及抗放松：限缩吸收

与已裁 G5 合并 `quality-policy-and-checks.md`；按需附少量 diff 审计例。**保留**：先查现有真实规则/工具/当前值，指标与理由、观察命令/适用面、enforce与仅测量分列；轻重检查按实际成本与覆盖布置，已有覆盖输出可复用；核阈值降低、断言/测试删除、suppressions、stub/吞错及例外依据；执行不了不能记clean（源floor exit2区分exit0）。

**限缩**：源码 regex 是线索不是语义裁判；合法删除/替换测试、合理suppression、未完成代码的独立候选并非自动违规。源 floor 不经委托成为本库全局政策；所有数字、四问上限、30行升级runner、0.5% tolerance、每次需外部checker等不强制。外部工具结果也可能无覆盖、误配置、版本不对或假绿，不是“不容争辩”。ratchet 是可选已接受政策，真实专业目标可接受指标变化；不能因现值变了自行放宽规则。

**脚本裁定**：不把 floor-guard 作为产品工具移植。本夜未观察到该产品消费依赖；它的 regex 会把示例/注释/合法重构误报。可吸收五类审查和0/1/2区别，机械 runner 在真实使用需求出现后另按现有准入选择，不为了有脚本而增加框架。

## C6 · 安全边界与措施：限缩吸收

新增按需 `trust-boundary-design.md`，供应链可用 `guide-dependency-change.md` 与 change-review 互指，避免一个大包默认加载。**保留可直接蒸馏**：按写入者追踪信任来源（含本机进程参数/共享路径/LLM输出）；资产+abuse场景；参数化输入、资源级授权与tenant边界、允许的输出/动作、不以prompt代替权限控制；upload类型/大小/内容，URL scheme/host/解析地址/redirect及DNS二次解析 TOCTOU；derived path containment、min-depth、owner证据及marker可伪造/检查使用竞态；多实例limiter不能把本地计数当全局。

供应链：定位真实安装边界/lockfile/manager，避免未审 lifecycle scripts 首次执行，冻结安装下验证必要包；audit已知漏洞≠trust proof，按 runtime/build/test/deploy 可达性和有效政策判断处置，forced remediation不自动跨版本；源版本矩阵是 point-in-time，不伪装长期稳定命令。涉敏数据的最小化/目的/保留/可检索删除是设计关切，具体法律依据由有效 policy/专业责任提供，不声称统一法律结论。

**不照搬**：Ask First 七类操作统一回Human、所有cookies/CORS/headers固定模式、所有场景固定rate/密码轮数、所有PII必须删除备份/必签某协议、禁止任何system-prompt进合法上下文。系统本来可能需要有效系统提示；保护的是秘密/跨租户数据/不该暴露的政策信息。公开API可以允许跨域，是否允许credentials取决于契约。源“secrets先rotate再purge”是风险处置建议，动作仍需有效权限，不自改凭据或历史。

**例子需带限度**：derived `.owner` 可写不证明授权；SSRF先DNS检查再fetch仍可能rebind；身份认证成功不等于有该资源读权。可以写这些具体反例，不能只保留“安全很重要”。本裁定不认证示例SDK/manager/平台完整安全；若B复制工具特定调用须核其支持文件/版本适用性。

## C7 · 可观察设计：限缩吸收

新增按需 `observability-design.md`，F 提观察需要，D/E 设计采集与跨界传播。保留从实际运行问题反推日志/指标/trace、稳定事件字段；correlation与entry-point不同且都不能由下游猜；跨HTTP/queue异步传播；RED/USE是选信号镜头；label bounded、延迟分布而非只看平均、症状与可行动告警、短runbook；以实际触发检查日志/metric/span/告警链，不以SDK配置代码证明可观察。

**限缩**：不强制每条日志JSON/所有endpoint全RED/每项目OTel/永远不用平均/固定两级alert或2–4问。进程内小任务可沿已有适用日志；平均与分布用途不同。告警试发须在有效操作许可内，不能为了“验过”给真实渠道发信息或改生产threshold；安全已授权的测试渠道可验证，缺对应证据诚实限缩。字段允许清单引用 guide-redacted-evidence，不重复安全正文。

## C8 · 计划依赖与切片：合并

并入 change-slicing、bounded-composition 和 D→E handoff：明确依赖到**结论/接口/写面/资源**，以可演示业务路径切而非先堆各层；风险/未知先探、保留单元acceptance/verification/依赖和expected touch set。模块预计清单不是 Owner 默认批准边界，跨模块改动按已有委托判断；已有卡/外部tracker采用原载体，保持未完成工作。

拒绝全任务只读Plan Mode、强制 tasks/plan+todo、每2–3任务全测/找Human、5文件或2小时/三条acceptance上限、migration/sharedstate一律不可并行、没有方案作者槽就不能整备。源的依赖图不意味着固定DB→API→UI顺序。不同领域有真实共享承诺时协调足够即可，局部小事直接做，不凑流程。

## C9 · 性能基线、因果与维护成本：限缩吸收

新增按需 `performance-investigation.md`；cache/query/pool详细支线由 EF-addendum 另裁后合并，不能因同属性能而漏掉。**本组保留**：用户可感知目标→baseline→实际瓶颈→可归因改动→相同条件重复观察/噪声→保留或撤销；症状分解与真实trace路径；N+1、有限读取、索引计划/写代价、pool容量与占用原因、图片/渲染/bundle、缓存层/键/陈旧语义的不同成本；保留被撤销尝试的原因，别重试旧失败想法；同树测试/性能不同证据轴，不以省正确性工作制造性能赢。

**限缩**：合成对照能证明所测环境性能，真实用户收益需相应用户面证据；不是每局部backend性能任务都需要RUM/Lighthouse。不要把源固定KB/ms/CWV值当本库授权SLO。没有显著性能收益且仅为性能而增加复杂度时应撤销/暂缓；若同时解决已接受的可靠性/正确性目的，应按该目的评价，不以neutral一票否定。噪声内不是产品FAIL，可以是未证明性能改善。计划相同不自动推出索引无价值，具体收益要看实际被测负载/写代价。缓存余额/权限/库存的绝对禁令改为：陈旧会破坏本次正确性且没有能证明的协调保证时不能以TTL缓存兑现该承诺。

## 蒸馏与后续复核

9组有实质可用内容；B 按共同落点归并，避免九条必然变九个新文件，细专业支线按需引用。C1/C3/C4/C5/C6/C7/C9 的例子/反例与成立条件必须保留，不能只剩 authority 声明。各源的当前默认值/法律/SDK版本不当作普遍事实；B 若展开本次未全文阅读的perf/obs/DoD参考，先补正文。

实际B固定差分由独立 gate 审：源忠实+本裁定限缩是否落实、消费入口/引用是否可用、例子是否真的揭错。方法有效性与安全/性能收益没有运行观察的部分保持未验；不因源裁定通过或新Codex身份宣布有效。
