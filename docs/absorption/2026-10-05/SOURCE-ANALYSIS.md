# 三仓源调查与下一轮 TPW 吸收建议

日期：2026-10-05（Asia/Shanghai）。状态：**源调查与候选提炼；尚未接受、尚未写入方法包**。

## 1. 结论

这三个仓库分别补三个不同的方向：

- **Emil：** 把交互品质判断变成具体、可观察的设计与评价操作。最有价值的是动画必要性、可中断交互、真实数据边界和全尺寸原型比较。
- **12-factor-agents：** 把模型实际输入、动作执行边界、暂停恢复和错误反馈讲成可设计的接口。最适合补 TPW 的启动消费与交接示例。
- **HumanLayer：** 提供研究、计划、实施、验证、交接的详细操作模板，以及审批记录/通知/会话状态的历史实现案例。适合提取产物形状与反例，不适合作为当前已验证 runtime 直接采用。

结合刚完成的 [UCBIP 实践报告](../../research/2026-10-05-ucbip-practice.md)，下一轮最值得吸收的是**具体操作、例子和反例**。现有 TPW 的责任、授权、独立评价、版本固定、证据覆盖原则已有正文；新来源不意味着必须新增三套工作流或按来源一一创建方法。

建议第一批聚焦四组：**实际上下文装配、可消费 Plan 与恢复材料、真实 UI 边界、交互/动画必要性与中断**。批准这些建议需要后续固定候选与有效接受流程，本次仅完成克隆、调查和分析。

## 2. 已拉取的固定对象

TPW 基线为 `1f95f0650638b6b6fbc892dcb697dbad4da86fa4` 的完整身份见 [SOURCE-PINS.json](SOURCE-PINS.json)，方法包子树为 `9d7c057417da73895cda3b85ec34d49db58669b6`。下表源 commit 均已 checkout 为 detached HEAD，工作树干净。

| 来源 | 固定 commit | 本地位置（TPW 根相对） | 实际文件范围 |
| --- | --- | --- | --- |
| [emilkowalski/skills](https://github.com/emilkowalski/skills/tree/e8a175de22ae1e49370fc144c1f3bb9aeedf988d) | `e8a175de22ae1e49370fc144c1f3bb9aeedf988d` | `.worktrees/source-intake-2026-10-05/emilkowalski-skills/` | 28 tracked paths；24 Markdown；14 `SKILL.md` |
| [humanlayer/12-factor-agents](https://github.com/humanlayer/12-factor-agents/tree/d20c728368bf9c189d6d7aab704744decb6ec0cc) | `d20c728368bf9c189d6d7aab704744decb6ec0cc` | `.worktrees/source-intake-2026-10-05/12-factor-agents/` | 499 tracked paths；52 Markdown；无 `SKILL.md` |
| [humanlayer/humanlayer](https://github.com/humanlayer/humanlayer/tree/99abe673498cf8bdcd5f989aebe9406a27185b3b) | `99abe673498cf8bdcd5f989aebe9406a27185b3b` | `.worktrees/source-intake-2026-10-05/humanlayer/` | 794 tracked paths；85 Markdown；无 `SKILL.md` |

三个都是独立浅克隆（`--depth 1 --no-tags`），没有拉取 submodule、安装依赖或执行上游脚本。`.worktrees/` 已由 TPW 现有 `.gitignore` 排除，源码副本不会进入 TPW 提交。JSON 记录 origin、commit、tree、提交时刻、文件计数、README/LICENSE 的 SHA-256，供未来恢复同一研究对象。

这是“源码已取得”的证据，不是所有内容已读、所有机制已接受或任何能力已运行的证据。本轮阅读范围和未读项见三个分仓报告：

- [Emil 源分析](EMIL-SOURCE-ANALYSIS.md)
- [12-factor 源分析](12FACTOR-SOURCE-ANALYSIS.md)
- [HumanLayer 源分析](HUMANLAYER-SOURCE-ANALYSIS.md)

## 3. 必须先认识的来源差异

### 3.1 HumanLayer 当前仓库已声明基本弃用

固定版本的 README 只有公开 issues 仓库说明，并明确表示代码基本已弃用、指向另一个重建产品。`humanlayer.md` 也记录旧 SDK 被移除；根 `CLAUDE.md` 仍提到已经不存在的旧 SDK 目录。GitHub description 和历史架构文字不能单独证明当前仓库的产品身份。[README](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/README.md#L1-L3)、[SDK 历史说明](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/humanlayer.md#L1-L5)。

因此本轮把 `.claude/commands` 的方法文本、`hld/hlyr` 的历史机制和其他 app/package 路径分开读。没有接入 HumanLayer 云服务，也没有把仓库视为当前可安装、可投产的审批系统。

### 3.2 12-factor 是文章与教学代码，不是十二篇 Skill

README 指向 `content/factor-01…09` 与 `factor-10…12`；未补零的 `factor-1…9` 是迁移指针，不是另外九篇原则。Factor 12 的 Markdown 正文很短，主要通过两张图表达；不能由标题推定已有可复用 reducer 接口、持久恢复协议或 runtime 实现。

源中 Factor 5 所称 business state 举例是 workflow 已发生的 messages/tool calls/results，与 UCBIP 的 Case、tenant、ledger 等业务权威不是同义词。其减少重复状态的建议可以讨论，但不能推广成“模型 thread 统一拥有全部业务状态”。[Factor 5](https://github.com/humanlayer/12-factor-agents/blob/d20c728368bf9c189d6d7aab704744decb6ec0cc/content/factor-05-unify-execution-state.md)、[Factor 12](https://github.com/humanlayer/12-factor-agents/blob/d20c728368bf9c189d6d7aab704744decb6ec0cc/content/factor-12-stateless-reducer.md)。

### 3.3 许可按对象区分

| 来源 | 本次读到的许可声明 | 后续吸收的实际要求 |
| --- | --- | --- |
| Emil | 根 `LICENSE`：MIT，版权为 Emil Kowalski 2026 | 复制/改编时保留对应许可与归属；不能只留下作者风格名 |
| 12-factor | README：content/images 为 CC BY-SA 4.0；code 为 Apache 2.0。根 `LICENSE` 为其实际 Apache 载体 | 文章、图和代码分别处理；译写/改编正文需按其对象适用的署名、修改说明及许可安排落盘，不能把全文一概标 Apache/MIT |
| HumanLayer | 根 `LICENSE` 声明 Apache 2.0；读取索引未发现其他嵌套 LICENSE/NOTICE 文件 | 保留源归属、实际许可和改编说明；不能据历史产品介绍继承服务使用权或运行资格 |

许可依据：[Emil LICENSE](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/LICENSE)、[12-factor README §License](https://github.com/humanlayer/12-factor-agents/blob/d20c728368bf9c189d6d7aab704744decb6ec0cc/README.md#L254-L258)、[HumanLayer LICENSE](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/LICENSE)。本表记录来源声明与后续处理点，不是完整分发许可审查；当前没有搬入来源正文或图片到方法包，也没有为整个 TPW 改许可。

## 4. 候选机制与 TPW 落点

表中的 merge/narrow/defer 是本次研究建议，不是接受裁定。重复贡献按机制计一次，不按三个仓库的文件数累加。

| 机制组 | 主要来源与具体贡献 | 当前 TPW 已有 | 本轮建议与最小落点 |
| --- | --- | --- | --- |
| M1 实际模型输入的所有权与可见性 | 12-factor own prompts/context；HumanLayer 首先取得任务和承重原件、研究输出携带版本/坐标 | `ADOPTION`、Charter、`guide-agent-text` 已规定固定输入、正文消费与占位符边界 | **merge/narrow**：补一个真实启动例；代码对象/治理对象/方法对象分开；实际 prompt 或读取记录可核，不建立统一 composer |
| M2 研究产物与工程 Plan 的消费关系 | HumanLayer 研究先查现有事实，Plan 用实际接口/模式，实施核 Plan 与当前代码，validate 分自动/人工 | `cross-module-design`、`uncertainty-planning`、`change-review` | **merge/narrow**：给一个短“事实与未知→共享承诺→实现自主→观察/召回”实例；先判断新增机制必要性，不固定 research→plan→impl 的全套阶段 |
| M3 暂停点、动作与恢复 | 12-factor tool 选择与调用分离、可暂停后继续；HumanLayer handoff/resume 复核真实对象 | `interface-contract-and-retry`、`handoff-and-resume`、`trust-boundary-and-actions` | **merge/narrow**：方法例明确当前暂停位置、候选动作、作用域/身份/幂等依据和重验项；审批/恢复的实际实现留在项目 |
| M4 错误反馈与有界失败处理 | 12-factor 将错误反馈到 context；HumanLayer mismatch 具名说明、实现停止受影响工作 | `local-defect-feedback-loop`、`external-tool-operation`、F 三态 | **merge/narrow**：短错误包保原始locator、阶段和未知，避免压缩丢因；工具故障不冒产品 FAIL；重试上限/升级来源由任务给定 |
| M5 真实 UI 数据与操作边界 | Emil `break-ui`：schema/现实数据、同数据边界、空/单/大量项、容器/窄屏/zoom/RTL/touch | `behavior-contract-examples`、`guide-test-evidence-quality`、`guide-accessibility-observation` | **优先候选**：引入可运行的现实边界构造与 demo/坏数据对照例；CSS 推断与真实可见观察分开，不把所有异常输入强行列为合法业务输入 |
| M6 动画是否值得、用户等待与可中断性 | Emil 先问频率/目的/功能，可不动画；从当前 presentation 接受新输入/反向或取消 | 现有可观察行为/性能/可访问性原则已有，具体 motion 操作较薄 | **优先候选**：先把必要性、重触发/中断/终态的反例写进既有行为/证据载体；仍有独立 motion 内容时才提一个小 on-demand guide |
| M7 原型要比较实质决策 | Emil 用命名差异轴、全尺寸真实邻接、一键切换/重播；HumanLayer 先给事实再问选择 | `bounded-prototype`、`design-alternatives`、`decision-elicitation` | **merge**：借具体比较方法；沿既有有效委托推进可逆探索，不照搬固定变体数、目录、组件或逐次审批 |
| M8 小任务与并行取证 | 12-factor focused agents；HumanLayer locator/analyzer/pattern finder 分工 | Driver 与 `change-slicing`、`bounded-composition` | **主要去重**：按负载判断与独立性拆任务；不固定多个代理、role 编制或常驻阶段；范围内读事实不等于扩大执行权限 |
| M9 审批记录、事件通知、会话状态 | HumanLayer 本地审批 store/eventBus/MCP 等待、会话恢复源码 | TPW 已区分 acceptance/verification/action/closure | **仅作反例/项目侧参考**：记录存在≠通知送达≠接收处理≠动作安全；没有采用审批 daemon、状态存储或重试 runtime |
| M10 统一状态、跨渠道触发、stateless reducer、prefetch | 12-factor Factor5/11/12/Appendix13 | `domain-state-and-invariants`、`external-tool-operation`、已有权威边界 | **限缩或延后**：检查重复派生/当前输入；不让 thread 取代业务权威，不因来源“from anywhere”授触发权，不把 prefetch all 变成全量敏感读取 |

## 5. 三仓各自最值得保留的内容

### 5.1 Emil：从“有品味”转为可以检查的专业操作

应优先保留四件事：

1. **动前先问必要性。** 经常使用、信息密集、需要立即操作的界面与营销/演示面不同；可以明确选择不动画，或只保留必要状态反馈。
2. **中断是行为条件。** 快速开/关、反向输入、取消、重触发和终态到达时，从当前显示状态处理；不能只看一条动画能播完。
3. **真实边界数据。** 从 schema/契约和可信现实例构造长名字、大计数、空集、缺值、RTL等，在真实容器中对照正常数据；找到字段无界也是具体事实。
4. **比较可观察选择。** 全尺寸组件、邻接上下文、切换/重播与慢速观察支持决策；漂亮缩略图或源码参数不是交互已成立。

依据：[animate](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/animate/SKILL.md)、[break-ui](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/break-ui/SKILL.md)、[prototype](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/prototype/SKILL.md)。

要限缩的默认包括统一 `<300ms`、固定曲线、某频率数字、只许 transform/opacity、禁键盘动画、固定组件/库清单。源内自身存在 drawer/toast 的不同时间、width/height 动画等例外；它们可以是说明性参数，不能直接变成 TPW 通用 gate。`prefers-reduced-motion` 也必须按用户需求和有效政策判断，不能把“gentler, not zero”当所有场景的唯一正确实现。

尤其不能用 blur/crossfade掩饰 UCBIP 的 live/canonical 双正文或来源错误。视觉平滑不代替完整内容、解析域、终态和零双显的已接受关系。

### 5.2 12-factor：把关键接口显露出来

适合吸收的是以下问题形态：模型这次到底收到什么；工具输出怎样变成候选动作；候选与执行在哪里分开；暂停时保存了什么；恢复时哪些作用域/事实还需重验；错误反馈能不能支持下一次决定。

TPW 中“固定引用”已经成立，源贡献是具体输入/事件/暂停接口的例子。Own prompts/context 不意味着每次从零手工拼所有输入；它意味着承重输入的形状、版本与进入方式可解释。Contact humans with tools 可以支持项目的具名返回接口，但不能改变用户已经给定的自主空间或每动作都重批。[Factor2](https://github.com/humanlayer/12-factor-agents/blob/d20c728368bf9c189d6d7aab704744decb6ec0cc/content/factor-02-own-your-prompts.md)、[Factor3](https://github.com/humanlayer/12-factor-agents/blob/d20c728368bf9c189d6d7aab704744decb6ec0cc/content/factor-03-own-your-context-window.md)、[Factor6](https://github.com/humanlayer/12-factor-agents/blob/d20c728368bf9c189d6d7aab704744decb6ec0cc/content/factor-06-launch-pause-resume.md)、[Factor7](https://github.com/humanlayer/12-factor-agents/blob/d20c728368bf9c189d6d7aab704744decb6ec0cc/content/factor-07-contact-humans-with-tools.md)。

教学 template 的序列化/CLI暂停例可以说明步骤，不证明原产品副作用安全、tenant隔离或长期恢复。源内静态契约疑点与未运行部分见分仓报告，不能因为有示例程序就选它作 TPW runtime。

### 5.3 HumanLayer：借产物，不搬其环境

最可迁移的是研究先给可核事实和未知、Plan引用真实接口/既有模式、实施遇不一致显露偏差、验证分自动与人工、handoff让接任者回读当前代码/运行态。这与 UCBIP“给角色名却没有正文、旧副树缺治理、咨询包缺最终候选”的问题直接相关。

研究命令自己限定“只描述当前实现”，这适合事实调查任务，不能变成任何研究都不允许根因分析或改进建议。源码优先规则只能用于当前实现，不允许当前代码自行覆盖已接受的产品目标。固定 `opus`、总是多代理、整文件全读、固定 `thoughts/`、Linear/Claude专用命令及持续轮询默认，均不迁入 TPW。[research_codebase](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/.claude/commands/research_codebase.md)、[create_plan](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/.claude/commands/create_plan.md)。

父研究者另核 `hld/approval/manager.go`：本地 store持久记录、事件通知、状态更新是不同步骤，correlation有best-effort限定。不是“有approval就已安全/已送达”。daemon源码把重启时仍active的 orphan session标failed；保留interrupted状态供以后resume，不能说它自动透明续跑。[approval manager](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/hld/approval/manager.go#L15-L115)、[daemon recovery](https://github.com/humanlayer/humanlayer/blob/99abe673498cf8bdcd5f989aebe9406a27185b3b/hld/daemon/daemon.go#L341-L382)。

## 6. 与 UCBIP 经验的直接接点

| UCBIP 已观察问题 | 新来源可提供的实际增量 | TPW候选动作 | 如何避免空转 |
| --- | --- | --- | --- |
| 路径/标签有了，正文未证进入实例 | 12-factor输入形状；HumanLayer承重材料取得和版本化产物 | 真实启动例，沿已有日志核实际输入 | 装配证明与应用效果分开；不读全包、不新builder |
| 多轮门在同一个气泡/单位前提内自洽 | Emil必要性/用户任务取舍；HumanLayer事实调查再问未知 | Plan起点回用户结果/单位/生命周期/owner/必要性 | 成熟技术不能代替产品单位裁定，不把源turn定义直接复制 |
| 只补已知反例，完整关系未恢复 | Emil正常/边界数据同位置对照；中断/重复操作 | 保留原完整合同、有效正例、真正到达规则的反例 | 不以CSS参数、截图数、测试数当完整关系成立 |
| Loop反复wake却未发现已交结果 | 12-factor显式状态/控制边界；HumanLayer记录/通知分层 | 只读观察例：实际可用工具、固定原件、接收者状态、UNKNOWN | runtime继续归下游；发出不等于收到/处理 |
| 旧候选与新治理、组合对象混淆 | HumanLayerresume现场复核；12-factor暂停位置 | 代码/治理/方法身份分开，差分召回 | 不rebase候选补文，不用旧PASS或SDK示例推定新组合资格 |

UCBIP报告中的归因限制仍保持：没有证实 TPW造成40%延长，没有证明补读或新规则已提效；这三个来源也不补出那些效果证据。

## 7. 推荐的下一轮吸收批次

### A：实际消费与交接例（优先）

来源以12-factor 2/3/6/8与HumanLayer研究/计划/交接命令为主。落点优先 `ADOPTION`、Charter示例、`guide-agent-text`、`handoff-and-resume`。交付一个完整启动例和一个代码候选/治理输入分版本的恢复例，正文只补原规则尚不够具体的步骤。

验证时让新实例从真实入口取得正确方法与固定输入；缺路径、已填/未填结构槽、stale材料能准确区分。证明读入不宣效果。

### B：真实UI边界与比较（优先）

来源以Emil `break-ui`、`prototype`为主。落点 `behavior-contract-examples`、`bounded-prototype`、`design-alternatives`、既有可访问性/证据指南。交付数据边界构造、真实容器对照、实质设计轴和合法保持面的小例。

评价要核真实渲染/操作所需的面；源码可支持推断，但不升级为实测。不要给非UI任务加这套观察。

### C：交互与motion的专业操作（次序按实际任务）

来源以Emil动画必要性和中断方法为主。先在现有B/D/E/F工作中承载可观察行为；如现有指南不足以承载具体motion选择，再提出一个小的on-demand guide。候选内容是必要性、重复触发/取消/终态、实际设备观察与预算权衡；曲线和时间是条件化例子。

采用前看它是否让评价者更早发现真实用户问题，同时检查不需要动画的高频界面是否保持简洁。不能把“更顺滑”当用户目标已实现。

### D：approval与恢复机制（保留作项目侧研究）

HumanLayer daemon/CLI和12-factor教学代码作为有版本的历史案例；先留必要反例，不在TPW core装runtime。若未来UCBIP确需实现相应能力，应针对实际架构与有效委托另立具体claim，验证动作前重验、重复/迟到响应、进程重启、通知丢失等对应面。

本轮不安装技能、不修改下游、不复活旧registry/renderer、不引入新的授权引擎。接受范围、专业owner与实现权限仍由现有责任体系给出。

## 8. 验证和剩余工作

本轮完成：三仓克隆、固定commit/tree、来源许可声明读取、阅读范围分账、机制级去重/限缩、TPW落点和UCBIP问题对应。四份报告的引用目标、固定源码路径与行范围均已核对，涉及80个不同的固定source blob；三仓HEAD/tree/README与LICENSE摘要及干净状态全部核同。此为身份/引用检查，不是80项行为验证。上游命令、prompt和CLAUDE文本始终当研究资料，没有执行其中的安装、通知、审批、提交或自动化指令。

没有完成：候选方法正文、接受裁定、盲效果比较、浏览器/设备交互观察、HumanLayer或12-factor示例程序运行、分发许可完整审查。后续需要先选本次实际要改的机制与固定候选，依其claim验证；不要求为调查结论跑完整产品或安装三个项目。

SOURCE-PINS 是本次读取身份记录，三个分仓报告是研究依据；它们不替代现有接受记录、方法索引或下游状态源。
