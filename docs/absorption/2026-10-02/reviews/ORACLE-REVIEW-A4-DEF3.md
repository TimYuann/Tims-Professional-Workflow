# Oracle / Codex · A4-CURSOR-DEF3 代码机制裁定

2026-10-02，审核者 tpw-0930-oracle / GPT-6.1 SOL medium。包 blob `2796784d085ed298081a7cf7722fe68579bd1b06`，路径 `docs/absorption/2026-10-02/packages/A4-CURSOR-DEF3.md`；源 Cursor `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`。6/6已裁：J1/J5限缩吸收，J2/J3/J4/J6合并到已有或已裁落点。脚本不因后缀贬值；本次不复制上游runtime，也不认证它。

## 实际回源

源路径前缀 `orchestrate/skills/orchestrate/`。已读：`scripts/core/branches.ts`全文、`scripts/core/prompts.ts`主要装配函数14–311（含worker/verifier/subplanner及上游handoff）；`scripts/schemas.ts`1–460及540–730（Plan跨字段refine、state、parseTree/迁移/formatter）；`scripts/cli/util.ts`的crawl/collect入口、解析/URI/dispatcher编码、operator与Slack目标边界；`scripts/cli/task.ts`49–391及478–598（run/kickoff/spawn/respawn/cancel/kill入口、findActiveRootPlanner）；`models.ts`接口/目录头与resolve/render尾、probe-models及generate-json-schemas全文、nudge-root的参数/有界等待发送逻辑；测试 `scripts/__tests__/{operator-boundary,kickoff-dedupe,worker-branch-discipline,slack-channel-boundary}.test.ts`相关全文或明确段落。核生成plan JSON schema结构与缺失的图不变量约束。未称全部脚本/adapter/测试已读，未安装或执行源码、没有云agent/Slack/Provider调用。

包中将多个“选段全读”并列为“逐字全读”，不能按全文资格继承；我只依据本次实际回源范围作下面判断。错误猜测测试在技能根 `__tests__` 后已按 `rg --files`定位实际 `scripts/__tests__`，引用以实际路径为准。

## J1 · 可执行契约与部分读取：限缩吸收

**保留**：输入变体判别、字段约束、统一枚举；引用存在/自依赖/环/重复名等跨字段不变量在数据消费前验证；错误输出字段路径与可执行修复；旧字段迁移显式说明；诊断遍历可隔离坏行，以免无关损坏隐藏其他观察。

**落点**：优先并入 `interface-contract-and-retry.md` 的结构/语义边界和 `domain-state-and-invariants.md` 的非法状态例子；支持细节可按需 `guide-boundary-contract-checks.md`，不因此要求 TPW Charter 变 JSON 或引入validator平台。

**条件与限制**：严格拒未知字段适合封闭输入协议；扩展兼容协议可能明确保留未知字段，不能把 `.strict()`设成全接口纪律。容错遍历要披露已跳过/无法读取范围，不能从残缺视图宣称“已终止所有子任务”或“任务图完整”。源树解析坏行过滤是availability操作，不是批准危险动作。`verifies`不是自己且指向存在任务，只证图关系，不能证明评价者独立、scope正确或契约已接受。正则仅限制名称字形，不证明路径containment/授权。

**新增回源精确化**：源运行期 Plan `superRefine`检查重复名、引用与环；生成 `plan.schema.json`并无这些动态图检查。单源生成减少维护分叉，**不意味着编辑器/生成schema等同所有运行语义**。必须说明两面实际覆盖，不能复现“声明/生成物已保护”那类误读。例子至少区分非法引用被运行解析拒绝、schema结构通过但图语义错、诊断部分读取不等于全体安全可决。

## J2 · 分支与物理锚：合并

并入 `bounded-composition.md`/handoff的共享写面与固定对象。保留任务逻辑标识与实际 branch/commit/worktree 的解析对应，读取依赖时核实际身份；expected touch/源branch/目标branch分开，合并需有效写权且不能默默用另一个tip。

源 `orch/root/task`与`merge-slice`命名是其实现，不成为本库固定分支格式、任何worker都必须push或按dependsOn顺序全部merge的规则。稳定命名不固定内容：仍需确切commit及consumer范围；同名不能代替真实对象。预先约定的命名或显式保存映射均有效，不强迫一切仓库建立确定性branch生成器。

## J3 · 装配与语义保真：合并

并入 `guide-agent-text.md`、Charter装配说明和handoff。保留缺少本次承重输入要显露、条件块只装本次需要内容、模板中未完成的**结构占位符**应在消费前揭示；实际branch、输入和评价对象要与委托相符。源上游handoff原样传送可减少二手失真，但仍是有来源/版本/信任级别的数据，不因进入prompt变新授权。

**不照搬**：必须内联所有handoff/唯一通信只能relay、禁止patch任何template、凡内容出现`{{...}}`都报错、无路径字段便要求Owner逐项批准、所有scope文件自动授变更权。示例中用户文本包含模板字面量与真正未填字段要能区分；不能把语义内容再当二次模板注入。保留用指针按需回源的本库纪律，不为了逐字relay把整段事实灌进常驻上下文。参数编码保护结构，不证明外部自然语言可信。

## J4 · 启动、重试与终止的操作契约：合并

并入 `agent-facing-cli-contract.md`及 `handoff-and-resume.md`，只吸收对外动作语义：发现已有真实活跃对象、解释参数/状态/重试是否新意图、fixed输入/依赖、cancel-running与prune-pending的区别、部分操作结果及诚实报告。路径/glob/`--source`标签可记录动作范围/来源，不自动认证身份。循环、队列、重试次数/超时由采用项目runtime拥有。

**回源限制**：findActiveRootPlanner按完整name、30分钟、pending/running和最多50列表筛；没有比repo、base或完整goal。比前缀匹配好，但仍不能称一般“同目标幂等启动”。相同slug不同repo/goal是反例；需任务真实意图标识/适用范围才能安全复用。没有搜到不证全服务没有对象，记录窗口/分页限制。`--force`是技术选项不产生重复启动权限。

终止先核真实目标/后果及有效许可，不把源 `-y`每次交互确认搬成所有已授权cleanup的重复审批。目录不完整/状态未知时保留限度，不能以“循环无环/坏行忽略”宣称跨服务全终止。重启/重复命令不重置此前审查轮次或权限来源。

## J5 · 操作者与外部通道：限缩吸收

与 `trust-boundary-and-actions.md`合并，不新造human角色；需要具象例子可其按需支持。保留“worker能控制argv/env/cwd、workspace不一定可信”的威胁模型；目标channel/thread/对象范围从受信配置解析，缺授权与受信目标时不执行外部写；token/target半配置早报可判错误；外部字段按所属结构编码（JSON/shell/模板各不同），避免quote/backtick/brace破坏格式。

**不要称普遍不可伪造**：源以OS userInfo home而非环境HOME、非symlink的uid/0600文件作operator flag；代码自身明说worker能写该home需更强边界。相同UID且同home可写时，0600不区分Owner与worker。`--workspace`可指伪造plan，schema验证不认证thread坐标；目标必须有可信来源，而非“plan存在且字段不空”。source string净化/JSON.stringify不防自然语言prompt injection。权限/凭证的真实隔离才约束动作。

保留拒env伪装、HOME覆盖、symlink与半配置的源码测试形态，但它们未排除同用户home写权限或计划伪造，**不能据几条绿测试宣称身份安全完整**。本库不授创建operator flag、加凭据、发Slack或解除限制许可。实际部署若要该机制，专业方需核宿主隔离与受信配置维护权。

## J6 · 能力目录、探测、生成与唤醒：合并

并入 `external-tool-operation.md` 的实际能力发现与 `verification-harness-design.md` 的探测面/生成物边界。保留面向任务的稳定选择名与当前SDK参数映射分离，声明时效/依据，适用版本下做最小必要探测、记录失败与资源收束；一份源生成视图要明确实际执行保护面（J1）；唤醒有deadline、消息源唯一/非空、busy/权限/失败分类，而不是盲目反复发送。

**限制与反例**：目录模型强弱/默认类型是源观点，不成为TPW模型政策；未知slug透传不表示可用，也不一律禁止服务端新能力。源码 probe 只create+send即记OK，不观察回答；cancel失败被吞，仍记OK。其证据最多是该阶段调用被接受，不能证明模型能完成任务、取消成功、零消耗或无遗留资源。对依赖“能答/已停止”的claim需要相应观察，不每次为了目录全probe所有Provider。

json-schema生成未自动保留运行期graph refine（J1），字节新生成不等于语义覆盖。nudge读取latest run不存在或非running时返回只是一种源实现；一般操作不能把观测未知直接判idle，也不因“busy”substring就认定所有失败可重试。实际harness的可靠状态与错误应优先，原版500/15秒等数值不搬成通用规则。

## 脚本及尾部处置

本库当前真实消费没有依赖这些cloud/Slack/SDK runtime脚本，故**不搬原runner/cli/schema generator/probe/nudge**。原因是消费需求/权限/依赖边界，不是脚本没有价值；代码里的上述工程经验实际进入方法。未来项目确需机械helper时可参考pin原脚本、补相关正文/依赖/例子并在项目runtime验证，不先造TPW通用编排平台。

DEF3未全文读的adapter/CLI小命令/错误类/余测试不能假作全量源码认证；同runtime载体的未读实现可归为服务特定参考，只有要写新claim或实际移植时再补承重材料，不把重试、发送或取消资格据摘要推出来。本次六机制都已实质裁定，不叫“源码全执行成功”。

B按共同落点归并，保留上述能揭错例子：结构绿但引用环错、同名跨repo被错误复用、文字占位符误当模板、0600同UID自授、probe接受但未答/未取消。由独立gate审B的真实固定差分；机械校验不替代专业验证或最终授权。本裁定不修改冻结Backbone/产品，也不授任何网络/发布/进程控制。
