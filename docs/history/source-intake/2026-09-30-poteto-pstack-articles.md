# poteto 的 pstack 两篇文章：来源摄取与本库对照

> 2026-09-30；source research，供独立复核与 Owner 裁决。本文只描述来源和现有条文的对应，不是 A4、A5、吸收批准或运行验证报告。

Owner 已指定这两篇文章进入后续吸收范围，并说明后续还会加入 Matt Pocock 的文章。本次完成来源保存与机制清点；表中的“已承接”只表示当前库内能找到对应行为，不把其余候选冒称为已落库。
下表的覆盖状态以写作时的 `570bea3` 为基线；本轮后续新增的承接位置另记在文末“落库回写”，不倒改基线判断。

## 来源、读法与边界

- **作者原站**：[Part 1](https://x.com/poteto/status/2094457600259842065)、[Part 2](https://x.com/poteto/status/2097732320606507506)。本轮 `agent-reach doctor --json` 报 X 的 active backend 为 OpenCLI；两次 `opencli twitter article ... -f yaml` 均以 `BROWSER_CONNECT / Failed to start opencli daemon` 退出；本机代理也使 Jina Reader 的 `curl` 连接失败。因此**没有读到 X 原站正文**。
- **实际阅读文本**：[Thread Navigator 镜像 Part 1](https://threadnavigator.com/thread/2094457600259842065/)（页面题为 *The Complete Guide to pstack Pt. 1*，标示 2026-09-01）和[镜像 Part 2](https://threadnavigator.com/thread/2097732320606507506/)（*Pt. 2*，标示 2026-09-10）。下表 `P1/P2 Lx–y` 指镜像抓取页的正文行，不是 X 原站行号；镜像是否与原站逐字一致未独立验证。
- **本机复查缓存**：2026-09-30 通过直连抓取镜像 HTML，分别保存在 `~/.agent-reach/captures/tpw/poteto-pstack-pt1-2094457600259842065.html`（SHA-256 `5438351359c5b7fadfffb0b1d7fa9648b18ba8eb90a8018ab5f15bee6f648bd5`）和 `~/.agent-reach/captures/tpw/poteto-pstack-pt2-2097732320606507506.html`（SHA-256 `7183e3a03750393ffbc1126b00e70632cd51535b6d5f9cc74e1553a29b5cc4a6`）。缓存位于仓库外，不随 Git 分发；原始链接和下文的逐项概述才是可移交的索引。
- **技术机制的一手核对**：实际读取 `upstreams/cursor-plugins/pstack/skills/**/SKILL.md` 与 `skills/poteto-mode/playbooks/*.md` 的相关正文，pin 为 `upstreams/cursor-plugins` commit `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`；本库对照基于 HEAD `570bea356a6d9374367cf01e48390aebfa21322f` 及当前工作树。下表 **pstack 列**的相对路径均以 `upstreams/cursor-plugins/pstack/` 为前缀。
- **版权与证据等级**：文章文字版权归作者及相关权利人；Thread Navigator 是第三方转载页面，非原站授权状态证明。本文只给中文概述、定位与极少术语，不复制文章全文、示例长段或图片。文章中的产量、倍数、效果与个人用法均是**作者自述**，本轮未作独立实测；本库“承接”仅指现有条文可定位，不等于方法有效、下游已执行或 A8 已 `PASS`。

状态词：**已承接**＝可指出本库对应行为条文；**部分承接**＝有同向条文但缺文章所述关键动作或边界；**未承接**＝已读的相关本库条文中无该动作；**属运行环境而不纳入**＝其实体是平台、进程、并发或资源机制，本库 Driver 的逻辑编排层不设这些值。状态是研究者的**条文匹配推断**，不是候选吸收裁决；所有“部分／未承接”的后续处理均**需独立复核、Owner 待裁**。

## 逐项机制对照

下表“文章”列是镜像所述行为的中文概述与定位（来源事实）；“pstack”列是已读原始正文锚点（源码事实）；“本库／判断”列是对当前条文覆盖程度的推断。锚点均为 `文件:行号`，范围只为方便复核。

### Part 1：验证基础设施

| # | 文章中的具体行为与定位 | pstack 正文锚点 | 本库承接文件及行号；条文匹配判断 |
|---|---|---|---|
| 1 | 让 agent 驱动真实用户路径、看动作与结果，闭合自验证循环；P1 L33–47、L158–177 | `skills/create-verification-skill/SKILL.md:9,27-31,38-40` | `skills/verification-suite.md:22-26,33,40-45`；**已承接**。自验证是工作方法，文章声称的生产力倍数未经验证。 |
| 2 | 先盘真实表面、启动、认证、数据、可观察物与实例隔离；先使用已有驱动设施；P1 L45–48、L75–82 | `skills/create-verification-skill/SKILL.md:11-21` | `skills/feature-map.md:24-32`、`skills/verification-suite.md:22-24`；**已承接**。具体 CDP、模拟器、sidecar 属下游按技术栈选用。 |
| 3 | 用小型可重跑 CLI 把启动、交互、截图、诊断和清理封成工具，而非每次临时写脚本；P1 L49–90 | `skills/create-verification-skill/SKILL.md:25-32`、`skills/principle-build-the-lever/SKILL.md:8-18` | `skills/verification-suite.md:25-26`、`skills/build-the-lever.md:18-25`；**已承接**工具原则与验证套件结构；文章所列命令是示例，非本库通用接口。 |
| 4 | CLI 要可组合、危险命令可预演、分层 help、清楚错误和机器可读输出；P1 L93–104 | `skills/create-verification-skill/SKILL.md:28-32`、`skills/principle-build-the-lever/SKILL.md:14-18`（相关但未列全 CLI 设计项） | `skills/verification-suite.md:25-26`、`skills/build-the-lever.md:23-25`；**部分承接**：现有条文规定真实命令、只读体检、证据及可重跑，未把这组 CLI 可用性条件列为统一规范。需独立复核／Owner 待裁。 |
| 5 | 能力地图按用户视角写索引及每项能力的入口、驱动法、可观察终态；P1 L114–154 | `skills/create-verification-skill/SKILL.md:34-40` | `skills/feature-map.md:34-42,65-76`、`workflow/registry.yaml:168-174`；**已承接**。本库把 A3 owner 定为 architect。 |
| 6 | 随应用变化保鲜地图与驱动方案，读源码并逐项活跑，区分文档漂移和产品缺陷；P1 L153–155、L183–187 | `skills/maintain-verification-skill/SKILL.md:9-10,23-39` | `skills/feature-map.md:44-63`、`skills/verification-suite.md:27-36,47-55`；**已承接**主要动作。本库规定 verifier 只记 `A8.frame_alignment`、architect 后续更新 A3，不能把二者写成同一次已闭环。文章的“每日”频率不是本库固定值。 |
| 7 | 性能工作先取基线 trace，针对性改动，复测；用多次驱动抵抗偶然样本；P1 L174–177 | `skills/poteto-mode/playbooks/perf-issue.md:3-19`、`skills/swarm/SKILL.md:22-26,38-42` | `skills/performance-optimization.md:24-33,39-42`、`skills/verification-suite.md:42-45`；**已承接**测量与不确定性记录。并行 worker 数及云端分配属 runtime，不纳入 Driver。 |
| 8 | 将用户反馈触发的复现接入例行自动化，必要时再修复；P1 L179–182 | `skills/poteto-mode/playbooks/bug-fix.md:5-11`、`skills/create-verification-skill/SKILL.md:29-40`；pstack 这两份给复现／验证步骤，文章的日程触发依赖外部服务 | `skills/triage.md:21-32`、`skills/debugging.md:21-38`、`skills/verification-suite.md:20-36`；**部分承接**反馈分诊与复现，定时／事件触发是下游 runtime 集成，不在本库定义。需独立复核／Owner 待裁。 |
| 9 | 用云 agent 的独立机器、预构建快照扩大并行并避免本机 worktree 争用；P1 L106–112、L170–173 | `skills/swarm/SKILL.md:28-34`、`skills/poteto-mode/playbooks/orchestrate.md:13-19` | `AGENTS.md:50-60`（协作前提）、`roles/driver.md:109-121`（物理并行由 runtime 决定）；**属运行环境而不纳入**。云机器、快照、并发上限不应进入本库 Driver control semantics。 |
| 10 | 让协调 bot 管理其他 agent，释放主上下文；P1 L168–173 | `skills/poteto-mode/playbooks/orchestrate.md:3-17,34-56` | `roles/driver.md:47-51,104-125`、`workflow/registry.yaml:224-227`；**部分承接**“谁负责／什么可并行”的逻辑语义；云 agent 生命周期、队列和资源管理属于下游 runtime。需独立复核／Owner 待裁。 |

### Part 2：研究、原型与设计

| # | 文章中的具体行为与定位 | pstack 正文锚点 | 本库承接文件及行号；条文匹配判断 |
|---|---|---|---|
| 11 | 面对噪声报告，先由 agent 用自己的话重述底层问题，让人及时发现误读，不先把自己的假设灌入；P2 L36–56 | `skills/poteto-mode/playbooks/investigation.md:3-9`（只读调查）；在已读相关 pstack 正文中未见文章“间接提示”完整步骤 | `skills/idea-refine.md:23-27`、`roles/voice.md:42,67`、`workflow/registry.yaml:126-128`；**部分承接**重述和可复述的 A1，未明确把“先不引导假设”写为统一动作。需独立复核／Owner 待裁。 |
| 12 | `/how` 按复杂度追代码路径，复杂子系统分角度调查后合成；P2 L58–64 | `skills/how/SKILL.md:13-58` | `skills/trace-paths.md:23-38,40-52`；**已承接**调查语义。具体 explorer 模型与 spawn 数是运行机制。 |
| 13 | `/why` 从代码历史、PR、票据、文档、讨论、观测、错误与数据查当初动机，保留空结果和置信语言；P2 L64–71 | `skills/why/SKILL.md:15-17,25-34,58-80,94-121` | `skills/teach.md:29-47`、`skills/research.md:24-33,40-47`；**已承接**多来源考古、来源锚点和事实／推断区分；能否访问各系统由下游环境决定。 |
| 14 | `/teach` 把 how 与 why 合成供人理解的解释，也迫使 agent 自查依据；P2 L58–71 | `skills/teach/SKILL.md:9-17` | `skills/teach.md:19-31,68-81`；**已承接**；“教过之后 agent 一定更准确”是作者经验，不视为已验证效果。 |
| 15 | `/recall` 用过往会话及共享记录重建工作面，并核对当前状态；P2 L73–78 | `skills/recall/SKILL.md:9-21,24-35` | `skills/recall-context.md:22-47,49-63`；**已承接**。 |
| 16 | 共享包设计先从调用者的 README／教程体验倒推 API 和实现；P2 L79–98 | `skills/architect/SKILL.md:81-83`（调用者用法优先）、`skills/technical-writing/SKILL.md:30-49`（文档模式） | `skills/codebase-design.md:69-75,143-150`、`skills/technical-writing.md:20-29`；**部分承接**调用者优先与文档分层；“先写可用教程作为设计输入”未被明确规定为通用触发。需独立复核／Owner 待裁。 |
| 17 | 将教程、how-to、参考、解释分成不同用途，写作帮助暴露设计目标；P2 L84–98 | `skills/technical-writing/SKILL.md:30-49` | `skills/technical-writing.md:20-29,31-63`；**已承接**分层；本库另有“决策”形态，不能与原文四分法简单等同。 |
| 18 | 把近期经验、现有实现和历史理由先装进设计输入，再要求设计解释其取舍；P2 L100–109 | `skills/architect/SKILL.md:21-31`、`skills/recall/SKILL.md:9-21`、`skills/teach/SKILL.md:11-15` | `skills/recall-context.md:22-47`、`skills/codebase-design.md:15-20,69-79`、`skills/teach.md:19-31`；**已承接**各动作；跨技能顺序是文章示例，并非本库固定编排。 |
| 19 | 有待实测的设计分歧时造多个一次性变体，用切换器与真实表面截图／时间数据比较；P2 L110–133 | `skills/poteto-mode/playbooks/prototype.md:3-14` | `skills/prototype.md:17-32,37-43`；**已承接**问题、变体、观察与丢弃；本库另要求原型材料留在一次性分支。 |
| 20 | 大改先查现状，再画至少两种类型／接口草图，筛红旗、交叉比选，按草图实现；P2 L135–146 | `skills/architect/SKILL.md:21-57,81-83` | `skills/codebase-design.md:69-105,143-155`、`skills/arena.md:21-27`；**已承接**。候选提出者不得给自己候选下最终裁决，见 `AGENTS.md:74-83`、`skills/codebase-design.md:127-137`。 |
| 21 | 实现若反复逼出额外参数、状态或类型逃生口，把它当设计形状错误证据，重画而非持续补丁；P2 L144–151 | `skills/architect/SKILL.md:53-79` | `skills/codebase-design.md:97-125`；**已承接**。 |
| 22 | 冻结设计后才写多 PR 的可审计清单：每项有独立可观察凭据，结构脚本校验，执行等操作者明确 go；P2 L152–160、L178–183 | `skills/poteto-mode/playbooks/multi-phase-plan.md:3-13,22-35,79-119` | `workflow/registry.yaml:210-227`、`skills/task-breakdown.md:23-40`、`skills/to-tickets.md:21-40`；**部分承接**可独立验证的切片与依赖；pstack 的逐 box 证据字段、`check-plan.mjs` 检查及显式 go 边界不能从现有 A5 条文直接推出。`docs/history/derivation-0930/SYNTHESIS.md:3-9` 明言它只是候选、不是可消费 A5；不能把它算作这里的已实现承接。需独立复核／Owner 待裁。 |
| 23 | 不明原因 bug 先给已知事实、数据和假设；以复现和判别性检查收敛根因；P2 L163–170 | `skills/poteto-mode/playbooks/bug-fix.md:5-11`、`skills/poteto-mode/playbooks/investigation.md:3-9` | `skills/debugging.md:17-38`、`skills/trace-paths.md:40-52`；**已承接**。 |
| 24 | 新服务边界先做竞争性接口设计，用原型回答实测问题，再供人审；P2 L171–177 | `skills/architect/SKILL.md:21-57`、`skills/poteto-mode/playbooks/prototype.md:7-12` | `skills/codebase-design.md:69-95`、`skills/prototype.md:17-32`；**已承接**方法。实例中的“先让我 review”是该调用者的明确门槛，不应推成所有设计的默认人工门。 |
| 25 | 大迁移切成小的可验证 PR，守住视觉与现场行为；P2 L178–183 | `skills/poteto-mode/playbooks/multi-phase-plan.md:3-13,79-132` | `skills/to-tickets.md:24-40`、`skills/verification-suite.md:25-36`、`workflow/registry.yaml:224-227`；**部分承接**切片和实测；文章示例的“保留旧 bug 的视觉一致性”是特定目标，不是通用原则；具体 PR 堆叠、数量和执行调度属下游。需独立复核／Owner 待裁。 |
| 26 | playbook 按任务条件加载；`prototype` 是探索，`multi-phase-plan` 是计划交付，不能把两者混成抽象长计划；P2 L110–128、L150–160 | `skills/poteto-mode/SKILL.md:115-143`、`skills/poteto-mode/playbooks/prototype.md:3-14`、`skills/poteto-mode/playbooks/multi-phase-plan.md:3-11` | `workflow/registry.yaml:855-862`、`skills/prototype.md:7-13`、`skills/task-breakdown.md:15-25`；**部分承接**任务触发与阶段分工。本库提供方法及控制语义，不负责上游 Cursor 的自动加载器；需独立复核／Owner 待裁。 |

## 本轮落库回写

以下是基线清点之后的实际改动，仍须独立语义复核；当前规则以 `workflow/registry.yaml` 和技能正文为准。

- **#4**：`skills/verification-suite.md` 已补可组合命令、可观察的预演、诊断性错误、顶层与子命令分层帮助、机器可读输出；文章来源登记为 `article:poteto-pstack-pt1`。基线的“部分承接”理由已不再适用于这组动作。
- **#16**：`skills/codebase-design.md` 已把共享包的一条真实用法短教程写进接口设计动作；文章来源登记为 `article:poteto-pstack-pt2`。基线的“教程未明确”理由已不再成立。
- **#22**：`A5.acceptance` 与 `skills/task-breakdown.md` 已补每片的预期证据落点，并区分计划和实际观察；仅请求计划时交付 A5 后停下。文章里特定的计划格式校验脚本和完整 PR 清单没有作为通用规则并入，因此仍是部分承接。

## 需带给独立复核者的问题

1. 先核镜像与 X 原站的同一性，再决定文章措辞能否作为一手作者证据；目前可独立确证的是镜像页面内容与本地 pin 的 pstack 正文。
2. 独立复核 #4、#16、#22 的落库回写是否忠实于文章且没有过度约束；继续判断 #11、#22、#25、#26 的剩余差异是规范缺口、任务特例，还是已有 owner 条文覆盖。本文不把未承接项自动判为应新增规则，也不把候选 `SYNTHESIS.md` 冒充已批准任务图。
3. 对 #9、#10、#26，请维护 Driver 的硬边界：本库可写谁该上场、证据够不够、何时停；机器、进程、云快照、队列、并发和资源上限交给下游 runtime。任何例外先由 Owner 明确变更边界。

## 后续接入 Matt Pocock 文章可复用的来源记录字段

一篇一条：`author`、`title`、`original_url`、`published_at`（标明来自哪一页）、`retrieved_at`、`retrieval_method`、`read_surface`（原站／镜像及镜像 URL）、`original_vs_mirror_check`、`copyright_holder_or_notice`、`permitted_use`（概述／短引，避免全文复制）、`source_version_or_archive_id`、`upstream_pin`、`article_anchor`、`upstream_body_anchor`、`local_anchor`、`mechanism_behavior`、`fact_or_inference`、`coverage_status`、`open_gap`、`independent_reviewer`、`owner_decision`。未来的研究者先填获取和版权字段，再逐机制填三层锚点；未审过的 `owner_decision` 留空。
