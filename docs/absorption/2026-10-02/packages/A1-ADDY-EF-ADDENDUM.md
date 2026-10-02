# A1 · addyosmani-agent-skills · EF 补充包（有界补读）

- **发现者**：tpw-absorb-a1（A 实例；不自行裁定采纳，不改产品）
- **源仓库 / pin**：`addyosmani-agent-skills` @ `2686b620fc1fed2e8f60c704839c766b8594c6b6`（locator `.worktrees/legacy-pre-night-2026-10-01/upstreams/addyosmani-agent-skills`）
- **派工来源**：tpw-night-driver 有界补读派工（关闭 `A1-ADDY-EF.md` 中标注的 `尚缺` 项）
- **范围**：只有两块 —— ① F9 四份 checklist 条目正文的机制判定；② `references/testing-patterns.md` 六节的机制判定。另附一份**已读待用清单**（本轮及上一轮已读、但未写入任何包的尾部材料，供 gate 按需索取）。
- **引用约定**：`addy@2686b620:<path>#<section>`。
- **边界**：本文件只补读与判定，**不重写 CD/EF**、不改产品、不 commit。凡判"有新机制"的条目只给锚点/操作/条件/反例与拟定落点，**不展开成完整方法正文**（那属 B 的落地环节，且需 gate 先裁）。

## 判定原则（本补充包如何区分"新机制"与"审计面重复"）

一条内容被判为**新机制**，须同时满足：
1. 它不是 F1–F8（或 AB/CD）里任何一条的**同义改写**；
2. 它能被表述为**可判定的操作 + 成立条件 + 失败反例**（而不是"要注意 X"）；
3. 它改变的是**判断内容**，而不是同名判断在不同对象上的复述。

以下情形判为**审计面重复**：同一判据在清单里以勾选项形式复述；同一事实在技能/清单/文档三处出现；仅提供工具 API 形状或平台参数。

---

# 1 · F9 四份 checklist 条目正文

## 1.1 `references/performance-checklist.md` → **有新机制（本组最多）**

> EF 的 F9 只记了"清单是审计面"，未读条目正文。读完的结论是：**这份清单包含 EF/CD 都未覆盖的机制**，而且其中两条属**正确性**范畴（缓存键完整性、陈旧窗口），一条属**容量算术**。

### P-1 · 缓存键完整性（凡影响响应的输入都要进键）

- **锚点**：`addy@2686b620:references/performance-checklist.md#Caching Strategies`（`Cache checklist` 第 3–4 项）与 `#Common Anti-Patterns`（"Cache key missing the viewer → One user's data served to another"）。
- **操作**：键必须包含**响应会随其变化**的每一个输入——租户、观察者（viewer）、语言、权限、特性开关；**绝不把按用户数据缓存在一个不标识用户的键下**。
- **成立条件**：存在"多租户/多用户/多权限视角"的读路径；缓存层在多请求间共享。
- **反例**：`GET /profile` 以 `url` 为键、无 viewer → 一个用户的数据被送给另一个（源文把它列为反模式，并加了一句判据："这**会**以性能收益的名义上线"）。
- **判断位点**：**C**（"陈旧/隔离"的语义）+ **D**；载体落点：与 EF/C9 的"缓存"小节合并；我方有 `guide-redacted-evidence` 的租户/隔离直觉但无缓存语境的判据。**这条是正确性而非性能**，故它同时是 C1（契约）与 C6（隔离）的实例。

### P-2 · 陈旧窗口是写下来的、而不是顺手填的 TTL

- **锚点**：同节 `Cache checklist` 第 6 项「Acceptable staleness window written down, not implied by whatever TTL was typed」；并配套第 5 项「One invalidation strategy chosen (TTL, event/tag, or versioned keys), not an accidental mix」与第 11 项「Nothing cached whose staleness is a correctness bug（balances, permissions, inventory at checkout）」。
- **操作**：为每个缓存**显式写下可接受的陈旧窗口**；**只选一种失效策略**（TTL／事件或标签／版本化键），不允许"碰巧混用"；把"陈旧即正确性错误"的读路径**列入禁止缓存清单**。
- **条件**：存在缓存；且该数据有一个可被接受的最长陈旧时间。
- **反例**：TTL 由实现者顺手填写（没人知道为什么是这个数）；三种失效策略在同一系统里各自为政；把余额/权限/库存放进缓存。
- **判断位点**：**B**（对外可观察的陈旧程度是一种承诺）+ **D**。载体落点：与常备门槛/接口契约相邻。**这是我方完全空白的一条**（我方谈"freshness 的含义要引用"，但没谈"把可接受陈旧窗口写下来"）。

### P-3 · 缓冲/连接类容量的算术判据与"先诊断再扩容"

- **锚点**：`#Backend Checklist > Connection pooling`（5 项）与 `#Common Anti-Patterns`（"Connection pool per request → Exhausts max_connections"）、`skills/performance-optimization/SKILL.md#Step 3` 的 "Connection Pool Exhaustion"（"**Bigger is not faster.** A pool larger than what the database can execute concurrently just relocates the queue from your app to the database, where it is harder to see."）。
- **操作**：**每进程一个池**（不是每请求、不是每模块）；维持 **`实例数 × 池上限` < 数据库的 `max_connections`**；设连接超时使其**快速失败**而不是永久排队；**扩容前先诊断**（谁占着连接：长事务、漏了 await、泄漏的客户端）；**实例数无界时（无服务器/自动伸缩）用多路复用代理，而不是加大池**。
- **条件**：有共享的有界资源（连接、线程、worker 池）且实例数可伸缩。
- **反例**：池上限加大到"看起来够用"→ 队列从应用搬到数据库、更难看见；池按请求创建 → 负载下打爆 `max_connections`；超时缺省 → 排到天荒地老。
- **判断位点**：**D**；载体落点：CD 的兼容/恢复或 C9 的性能设计；**我方无任何"容量算术"判据**。

### P-4 · 否定缓存与"错误绝不进缓存"

- **锚点**：`#Caching Strategies > Negative caching`。
- **操作**：把**"不存在的结论"也缓存**（否则每次查找都打源站——"一个只保护happy path 的缓存"）；否定条目用**更短**的 TTL（短到新建记录能及时出现）；**源站错误绝不写成否定缓存条目**。
- **条件**：存在"反复查询不存在对象"的路径（循环里的不存在 ID、404 资源）。
- **反例**：**一次一分钟的源站故障因为被缓存成"不存在"而放大成很多分钟**。
- **判断位点**：**D/E**；载体落点：同上。**我方空白**。

### P-5 · 击穿防护（一个重算、N 个等待者）

- **锚点**：同节 `Request coalescing (stampede protection)`（含 `loadOnce` 形态）与 `#Common Anti-Patterns`（"Cache stampede on a hot key → Origin takes full concurrent load at expiry"）。
- **操作**：热键过期时**合并并发未命中**——同一键的在途请求共享一个 promise（源文给出最小形态）；共享缓存的情况需要**分布式锁**或 **stale-while-revalidate**（让等待者先拿到旧值而不是阻塞）。
- **条件**：热点键 + 冷启动/过期时刻的并发尖峰。
- **反例**：热键一过期，所有并发请求一起穿透（"这是缓存从防止故障变成造成故障的方式"）。
- **判断位点**：**D**。**我方空白**。

### P-6 · 缓存的前提判据（先量后缓存 / 命中率必须被监控 / 有界）

- **锚点**：`Cache checklist` 第 1、2、9、10 项：**被缓存的调用必须先被测量为昂贵**（"caching a fast call adds a hop and buys nothing"）；读写比支持缓存；**设淘汰策略与内存上限**（"an unbounded cache is a memory leak"）；**监控命中率**（"a cache nobody measures is an assumption, and a low hit rate is pure overhead"）。
- **操作**：加缓存前先给出"这个调用贵"的测量；设定淘汰与内存上限；把命中率纳入监控并在低命中时撤掉缓存。
- **条件**：有测量能力。
- **反例**：给一个很快的调用加缓存（多一跳、零收益）；无上限缓存（内存泄漏穿着优化的外衣）；从不测命中率。
- **判断位点**：**D/F**；与 C9 的"先测量"同源但**对象不同**（C9 管"优化是否需要证据"，本组管"缓存是否需要证据 + 它现在是否还有收益"）。载体落点：与 C9 合并成"性能与缓存判断"。

### P-7 · 索引改动的"先读计划、计划不变就回退"

- **锚点**：`#Backend Checklist > Query plans`（5 项）与 `#Index strategy`（8 项）与 `#Common Anti-Patterns`（"Indexing without reading the plan → Write cost paid, read gain unproven → `EXPLAIN ANALYZE` before and after; **revert if the plan is unchanged**"）。
- **操作**：索引改动前**捕获计划作为基线**（不是只捕获改动后）；读懂大表上的顺序扫描（缺索引／索引不可用／确实不值得）；**估计行数与实际行数差一个数量级就先刷新统计而不是先动索引**；没有能把排序吸收掉的复合索引；改动后**重看计划——计划没变就把索引回退**；坚持"等值列在前、范围/排序列在后"的复合顺序；按查询形状（过滤+排序）建索引而不是按单列；热读路径考虑覆盖索引；低选择性的主导值不建索引（用部分索引服务稀有值）；函数上建表达式索引；前缀通配搜索用全文/三元索引而非 B 树；**写代价要被计量**（每个索引都在给每次写入加税）；**未被使用与重复的索引要删**。
- **条件**：存在真实数据库与 `EXPLAIN ANALYZE`（或等价）能力。
- **反例**：加索引而不读计划（付出了写代价、读收益未被证明）；计划没变却留着索引；在不刷统计的情况下调索引；忘记每个索引都在拖慢写入。
- **判断位点**：**D**（取舍）+ **F**（"改动是否产生了可观察效果"）。**这条是 C9"保留/回退"决策表在数据库域的同构**，且它自带一条明确的回退条件（计划不变 → 回退）。

### P-8 · 三条平台契约级的"别破坏"判据

- **锚点**：`#Frontend Checklist > Rendering` 末项「No `unload` event handlers and no `Cache-Control: no-store` on HTML responses — **preserves back/forward cache (bfcache) eligibility**」；`### Images`「explicit `width` and `height`（prevents CLS in art direction）」；`### Fonts` 的 `size-adjust`/`ascent-override`/`descent-override` 与 `font-display`。
- **操作**：把三条"容易顺手破坏、后果明显"的判据单独列出：①**不注册 `unload`、不在 HTML 响应上设 `no-store`**（两者都会让页面失去 bfcache 资格，而收益是"看起来更谨慎"）；②**图片与 `<source>` 显式声明宽高**（防止艺术指导场景的布局位移）；③**字体回退用度量覆盖参数**把字体交换造成的 CLS 压下去。
- **条件**：有浏览器渲染面。
- **反例**：为了"更安全"给 HTML 加 `no-store` → 前进后退变慢且用户可感知；图片只写 CSS 尺寸不写属性宽高 → 加载期跳动。
- **判断位点**：**B/D**；载体落点：属 CD 尾部的"前端/可访问性设计约束"族（本组判其在**我方没有该域所有权**的前提下，只宜作为按需清单条目）。

### P-9 · 慢交互的三分解（诊断工具）

- **锚点**：`#Measurement Commands > INP field data and DevTools workflow` 与 attribution 形态（`interactionTarget`、`inputDelay`、`processingDuration`、`presentationDelay`）。
- **操作**：把"交互慢"拆成三段——**输入延迟 / 处理时长 / 呈现延迟**，分别对应三类修法（主线程被占／处理器过重／渲染阻塞）；并且**先取字段数据再优化**、**在中端机上测**（4×–6× 节流）、**长任务（>50ms）要切分并主动让出主线程**（源文并列了 `yieldToMain`、`scheduler.yield`（首选）、`scheduler.postTask`、`isInputPending`、`requestIdleCallback` 的适用面）。
- **条件**：有真实用户交互指标。
- **反例**：看到"交互慢"就直接优化代码（没有分解，因此不知道该修哪一段）；只在本机高端设备上测（问题不出现）。
- **判断位点**：**D/F**；载体落点：C9 的补充。

### 1.1 结论表

| 判定 | 条目 | 一句话理由 |
| --- | --- | --- |
| **新机制（正确性范畴）** | P-1 缓存键完整性、P-2 陈旧窗口写下来 | 两者都是"陈旧/隔离"的语义判据，我方与 CD 均空白 |
| **新机制（容量/资源）** | P-3 容量算术与先诊断、P-6 缓存前提与命中率、P-4 否定缓存、P-5 击穿防护 | 都是我方没有的"有界资源共享"判据族 |
| **新机制（改动需证据）** | P-7 先读计划/计划不变即回退 | 与 C9 的保留-回退同构，但对象是数据库计划 |
| **新机制（诊断分解）** | P-9 慢交互三分解 | 把"慢"分解为可分别修复的三段 |
| **新机制（平台契约）** | P-8 bfcache/尺寸/字体度量 | 三条"顺手就破坏"的判据 |
| **审计面重复** | CWV 阈值表、图片/JS/CSS/网络/渲染的其余勾选项、Measurement Commands 的具体命令、`#Common Anti-Patterns` 的其余行 | 与 CD/C9 及 EF/F1 的取向同义；命令与阈值属语境 |

## 1.2 `references/security-checklist.md` → **有新机制（三条）**

> EF 的 F9 与 CD 的 C6 已覆盖三档边界、SSRF、限流、密钥、依赖供应链、隐私、LLM 边界。读完清单正文的结论：**控制面基本重复，但有三条新东西**——其中第一条是**带自我削弱说明的参考实现**，第二条是**处理"平台默认值快速变化"的方法**。

### S-1 · 破坏性路径的容纳配方与它的两条自我削弱说明

- **锚点**：`addy@2686b620:references/security-checklist.md#Input Validation > Destructive Path Operations`（代码块 + "What this does not do, and must be said where the snippet is copied from"）。
- **操作**：先**解析真实路径**（解析符号链接）再判定；判定内容为"落在允许列表根之下的**候选**"（不是授权）：`rel` 判定必须精确（源文点名：`rel === '..'`／`'../'` 才算越界，**朴素的 `startsWith('..')` 会把合法子目录 `..cache` 也拒掉**）；深度 ≥1；**所有权证据在调用之前读取**（`.owner` 内容须等于**来自已认证状态**的期望值）；不满足则抛错拒绝。
- **自我削弱说明（必须随代码一起被复制——这是本条最有价值的部分）**：
  ① **标记是自我证明**：任何能写进这个根的东西都能写 `.owner`；因此 `expectedOwner` 必须来自**已认证状态**，且标记需要**完整性保护**（受限属主或 MAC），否则它只是"对错误目标的一致性检查"，**不是授权**。
  ② **返回一个路径会留下检查/使用竞态**：若不可信进程能在检查与调用之间替换某个祖先目录，就必须改为**在描述符上操作**（no-follow、根内语义），或保证该层级在此期间不可变。
- **条件**：存在"由数据命名目标"的删除/移动/覆盖。
- **反例**：把形状检查当授权；把 `.owner` 当授权（自证）；检查后返回路径再使用（TOCTOU）；用 `startsWith('..')` 误拒合法目录。
- **判断位点**：**D/E**；载体落点：C6 的"派生路径破坏性操作"节——CD 已收录三条合取与"拒绝即停止"，**本补充新增的是两条自我削弱说明与 `rel` 判定的精确性**（CD 的 C6 行已记"标记自我证明与检查/使用竞态会使该检查比读起来弱"，但未给判据；此处补齐）。

### S-2 · 处理"平台默认值快速变化"的方法（版本锚定策略矩阵）

- **锚点**：同文件 `#Dependency Security > Install-Script Gate`（四步 + **Point-in-time snapshot** 段落 + 按管理器版本列出的策略表 + 三条官方来源链接）。
- **操作**：①**先定位安装边界**（父级 `workspaces` 命中就用该工作区根；否则用拥有 manifest 与依赖图的最近项目根），并在该边界上**用 `packageManager`、锁文件、CI 命令三方互相印证**——**不一致或存在竞争锁文件就停下**；②**绝不用"先跑一次普通安装"来发现生命周期脚本**：以禁用脚本或**缺省即拒 + 失败即关闭**的方式引导；③检查**确切的脚本源码与包版本**后才批准；④在安装边界记录**最窄的**原生策略并提交；⑤用该策略跑一次**干净的冻结/不可变安装**并验证所需包仍能构建；⑥**每个管理器版本给出一条对应策略**，并附一条纪律：**"对未列出的管理器或版本，查其官方文档；不要拿另一个管理器的命令或更新的默认值来替代。"**
- **条件**：存在依赖安装边界；管理器默认值会随版本变化。
- **反例**：靠普通安装发现脚本（等于让脚本先跑）；批量批准；用别的管理器的命令代替；把旧版本的默认值当成当前默认值。
- **判断位点**：**D**（工程纪律）+ **F**（"策略是否真的生效"要由一次干净冻结安装来证明）。**这条的可转移部分不是矩阵本身，而是"平台默认值不可继承、必须按 pinned 版本查证并记录最窄策略"这一方法**——它与我方"平台耦合拆除"和"未经验证不得写成已有效"是同一条纪律在依赖域的实例。

### S-3 · LLM 边界的另外两条（信息质量与投毒）

- **锚点**：`#OWASP Top 10 for LLMs Quick Reference` 的 **LLM09 Misinformation**（"Ground answers with citations; validate critical claims; keep a human in the loop"）与 **LLM04 Data and Model Poisoning**（"Use trusted model sources, verify integrity; vet fine-tuning and RAG data"）。
- **操作**：把"引用来源 + 关键主张要验证 + 关键处保留人类在环"与"模型/数据集/插件按依赖对待（来源可信、完整性校验、微调与 RAG 数据要审查）"列为 LLM 边界的两条判据。
- **条件**：功能调用 LLM 或使用 RAG/微调数据。
- **反例**：把模型输出当权威（无引用、无验证）；用未审查的数据集做 RAG 或微调。
- **判断位点**：**C/F**（我方 F 的"依据来源"与"覆盖限制"）；载体落点：与 C6/F5 合并。**与 F5（源驱动开发）天然配对**：F5 管"实现依据要有来源"，本条管"模型产出的主张要有来源与验证"。

### 1.2 结论表

| 判定 | 条目 | 一句话理由 |
| --- | --- | --- |
| **新机制** | S-1 容纳配方的两条自我削弱说明 + `rel` 精确判定 | 把"检查比读起来弱"从警告变成可写下来、可复制的判据 |
| **新机制（方法）** | S-2 版本锚定策略矩阵 + "不可用别的管理器的命令替代" | 一条处理"平台默认值漂移"的可转移纪律 |
| **新机制（LLM）** | S-3 LLM09/LLM04 | 我方已有 LLM01/02/05/06/07/10 的对应，缺"信息质量"与"投毒"两条 |
| **审计面重复** | 威胁建模四项、认证阈值（bcrypt ≥12、≤10 次/15 分钟、重置令牌 ≤1 小时一次性）、授权/输入校验勾选项、头部集合与 CORS 形态、数据保护、审计可达性分诊、OWASP Top 10 表、Error Handling 形态 | 与 C6 及本补充的待用清单同义；具体阈值属语境 |

## 1.3 `references/observability-checklist.md` → **有新机制（两条）**

### O-1 · 仪表盘必须以"回答值班问题"为存在理由

- **锚点**：`addy@2686b620:references/observability-checklist.md#Dashboards`（4 项）与 `#Pre-Launch Gate`（5 项）。
- **操作**：服务健康仪表盘至少含**错误率、延迟 p99、流量、饱和度**；**依赖健康面板**（逐服务的错误率与延迟）；判据句：**"仪表盘要回答开头那些值班问题——而不是'除了答案以外的所有东西'"**；**默认时间范围要合理**（1–6 小时，不是 30 天）。发布前门禁五项：结构化日志已进聚合器；每个新端点与依赖的 RED 指标在仪表盘可见；**至少一条基于症状的告警已配置、已挂 runbook、已试触发过一次**；一个请求能跨它经过的每个服务被追踪；值班知道 runbook 在哪。
- **条件**：有生产服务与值班。
- **反例**：仪表盘堆满指标但答不出"现在坏了吗、坏在哪"；默认窗口 30 天（变化被平均掉）；告警配了但从未试触发（链接是坏的也没人知道）。
- **判断位点**：**F**（可诊断性的验收面）+ **D**；载体落点：C7 的补充（C7 已覆盖"先写问题→选信号→告警→runbook→验遥测"，**缺"仪表盘与发布前门禁"这一收尾面**）。

### O-2 · 归因 ≠ 关联：同一日志流多入口时必须打入口点字段

- **锚点**：`skills/observability-and-instrumentation/SKILL.md#3. Structured logging` 的 "When several entry points write to one log, name the entry point." 段落（含 `runLog(entryPoint, runId)` 形态与命名提示"用 `entryPoint` 而不是 `source`，因为 `source.*` 被 ECS 保留给网络字段"）。
- **操作**：**相关 ID 只能标识"一次运行"，不能说明"是哪条代码路径启动的"**——同一个作业被调度器、补放端点与手工 CLI 触发时在同一 sink 里产生可互换的行，于是归因退化为排除法（交叉阅读调度器历史、进程表、部署日志），而**那个论证只在这些外部记录仍然存在时成立**。因此：**在运行开始处打上入口点字段**，并让入口点与相关 ID **走同一条传播路径**（队列元数据、HTTP 头），否则 worker 只能重新推导入口点——那是猜。
  附一条判据：**"仅仅与入口点相关的字段是提示，不是归因：任何能触发这个作业的东西都能复制它。"**
- **条件**：一个日志 sink 被多个入口写入；存在"同一作业多种触发方式"。
- **反例**：只打相关 ID 不打入口点 → 归因靠排除法且依赖外部记录尚存；打一个"与入口点相关"的值（如载荷里的某个字段）当作归因；worker 自己推导入口点（猜）。
- **判断位点**：**F**（"证据的来源与覆盖"：这条是关于证据**归属可证性**的判据）+ **D**；载体落点：C7（C7 行原记"§3/4/5 未读"，本条即为其中一条）。**这条与我方"不得把程序齐全当作实质足够"同构**（相关 ID 齐全 ≠ 能归因到入口）。

### 1.3 结论表

| 判定 | 条目 | 一句话理由 |
| --- | --- | --- |
| **新机制** | O-1 仪表盘以值班问题为存在理由 + 发布前五门禁 | C7 缺"收尾面"（仪表盘与门禁） |
| **新机制（证据归属）** | O-2 入口点字段与"相关 ≠ 归因" | 一条关于证据可归属性的判据，且含反例（排除法依赖外部记录尚存） |
| **审计面重复** | 值班问题三项、结构化日志其余项（级别表、相关 ID 传播、不记密钥、字段白名单、外部调用只记元数据）、指标 RED/USE 与标签基数、追踪 OTel 六项、告警六项、验证遥测四项 | 与 C7（已读 §1/§2/§6/§7）及本补充的待用清单同义；具体命令/库名属语境 |

## 1.4 `references/accessibility-checklist.md` → **域约束为主；含少量可判定不变量**

> 判定要点：这份清单**确实包含 F1–F8 未覆盖的内容**，但那些内容属**前端/UI 设计约束**（我已在 CD §T 中记为"建议归 EF 或按需、并保留一条判据"的尾部族）。它们不是 EF 的机制；**若 gate 认为该族要落，落点应在 UI 域的按需准备文件，而不是这里**。以下只列其中**不依赖具体框架、可当场判定**的少数不变量。

### A-1 · 键盘与焦点不变量（可判定，不依赖框架）

- **锚点**：`addy@2686b620:references/accessibility-checklist.md#Essential Checks > Keyboard Navigation` 与 `#Common Anti-Patterns`。
- **操作（四条不变量）**：①**焦点可见**（删掉轮廓线是反模式，要"改样式而不是去掉"）；②**没有键盘陷阱**（用户总能 Tab 离开一个组件）；③**模态在打开时把焦点锁在里面、关闭时把焦点还回去**；④**`tabindex` 只允许 0 或 -1**（`> 0` 会破坏自然 Tab 顺序）。配套："跳转到主内容"链接在键盘聚焦时可见。
- **条件**：有任何自定义交互组件。
- **反例**：`div` 当按钮（不可聚焦、无键盘支持）；去掉 focus outline；`tabindex="3"`；模态关闭后焦点丢失。
- **判断位点**：**B/E**（可观察行为 + 实现）；**我方无 UI 域所有权**，故只宜作为按需清单。

### A-2 · 语义元素选择与"颜色不能是唯一信道"

- **锚点**：同文件 `#Common HTML Patterns > Buttons vs. Links`（含 "NEVER use div/span as buttons"）与 `#Essential Checks > Visual/Forms`。
- **操作**：动作 → `<button>`；导航 → `<a href>`；**绝不用 `div`/`span` 扮演按钮**。**颜色不得作为唯一的信息载体**（对比度：正常文本 ≥4.5:1、大文本 ≥3:1、UI 组件 ≥3:1；必填、错误状态、链接都要有颜色以外的标识）。
- **条件**：有交互或状态表达。
- **反例**：色盲用户看不到的"仅颜色"状态；只靠颜色区分链接与正文；错误只用红框不用文字/图标。
- **判断位点**：**B**（信息可传达性）；域约束，非 EF 机制。

### A-3 · ARIA live 区域到场景的映射表

- **锚点**：同文件 `#Quick Reference: ARIA Live Regions`（`polite`＝下次停顿播报→状态更新/保存确认；`assertive`＝立即播报→错误/时间敏感告警；`role="status"`≡polite；`role="alert"`≡assertive）与 "Common HTML Patterns" 的 `role="status"`/`role="alert"`/`aria-busy` 样本。
- **操作**：按**场景**选播报时机（普通状态用礼貌、错误用立即），并给动态内容配 live 区域。
- **条件**：有异步/动态内容。
- **反例**：用 `assertive` 播报普通状态（打断屏幕阅读器）；动态内容无 live 区域（用户不知道变了）。
- **判断位点**：**B/E**；域约束。

### 1.4 结论表

| 判定 | 条目 | 一句话理由 |
| --- | --- | --- |
| **有新内容但属 UI 域** | A-1 键盘/焦点四不变量、A-2 语义元素与颜色非唯一信道、A-3 live 区域场景映射 | 可判定，但落点是 UI 设计约束族（CD §T 已列），**不是 EF 机制** |
| **审计面重复** | 表单、屏幕阅读器、视觉、内容各节的其余勾选项、Testing Tools 命令、Anti-Patterns 其余行 | 多数是 `skills/frontend-ui-engineering/SKILL.md#Accessibility (WCAG 2.1 AA)` 的枚举形式（技能是方法、清单是审计面） |

**去重指向**：若 gate 决定落 UI 族，应以 `skills/frontend-ui-engineering/SKILL.md` 的 WCAG 节为方法面、本清单为审计面，**只一次落地**（CD §T 已标明该族"我方无技术域所有权，宜作为按需指南"）。

---

# 2 · `references/testing-patterns.md` 六节

> EF 的 F9 已读 `#Test Anti-Patterns` 与 `#Mocking Patterns`；本次补读 `#Test Structure`、`#Test Naming Conventions`、`#Common Assertions`、`#React/Component Testing`、`#API/Integration Testing`、`#E2E Testing (Playwright)`。

## T-1 · 按"用户感知的方式"定位元素（本组唯一新机制）

- **锚点**：`addy@2686b620:references/testing-patterns.md#React/Component Testing`（注释明写 "Find elements by accessible role/label (**not test IDs**)"，全部查询走 `getByRole`/`findByText`/`getByLabel`）与 `#E2E Testing (Playwright)`（同样全用 `getByRole`/`getByLabel`）。
- **操作**：组件与端到端测试**优先用可访问角色与标签定位元素**，而不是 `data-testid`；断言**用户可见的结果**（例如"该项变成删除线"）而不是内部状态。
- **成立条件**：被测界面有可访问语义（角色/标签）——若无，**这本身就是一条发现**（界面无法被辅助技术使用）。
- **反例**：用 test ID 定位（重构即碎、且不检验可访问性）；断言 CSS 类名或组件内部状态（行为没变也会碎）。
- **判断位点**：**F**（测试作为证据的**稳定性与覆盖面**）+ **E**；**它同时是 A-1/A-2 的可执行检验**——把可访问性不变量变成测试选择器，这是我方"验证设计"与"UI 约束"之间的桥。
- **载体落点**：F1 的"六条判据"扩为第七条（或作为其第一条的实例：断言可观察结果 = 用用户感知的定位方式）。

## T-2 · 端点三件套（小模板，可判定）

- **锚点**：`#API/Integration Testing` 的三个用例形态——**成功**（201 + 响应体形状用 `toMatchObject` 断言必需字段）、**校验失败**（422 + **断言结构化错误码** `body.error.code`）、**未认证**（401）。
- **操作**：每个对外端点至少三条用例：成功、非法输入、未认证；并断言**错误码而不是错误文案**。
- **条件**：有对外端点与结构化错误契约。
- **反例**：只测 happy path；只断言状态码不断言错误码；未认证路径没有用例。
- **判断位点**：**F**；**与 C1 的错误语义单一化天然配对**（C1 定"错误形状唯一"，本条是它的最小验证集）。载体落点：F1 或 C1 的方法中的"验证"一节。

## T-3 · 命名三段式（小模板）

- **锚点**：`#Test Naming Conventions`：**`[单元] [预期行为] [条件]`**（`TaskService.createTask` + "creates a task with default pending status" / "throws ValidationError when title is empty"）。
- **操作**：测试名按"单元 + 预期行为 + 条件"三段构造；条件用 `when/for` 引导。
- **反例**：`it('works')`、`it('test 3')`（F1 已列）。
- **判定**：**这是 F1"命名像规格"的一个可套用模板**，不是新机制；列于此以备 gate 需要"可抄的形态"。

## T-4 · 等值判定的三档与浮点容差（微判据）

- **锚点**：`#Common Assertions` 的 `toBe`（严格相等）／`toEqual`（深相等）／`toStrictEqual`（深相等 + 类型匹配），`toBeCloseTo(0.3, 5)`（浮点），`toThrow(ValidationError)`／`toThrow('specific message')`（错误类型与消息的区分）。
- **操作**：按"你想让它抓住哪一类缺陷"选断言强度——**过松的断言等于没有断言**（F1/F9 的"断言过宽"反模式的实例化）；浮点用容差；错误断言要分清"类型对"与"消息对"。
- **判定**：**不是新机制**（同 F1"一概念一断言"与"断言过宽"），但它把"过松"具体化为**三档可选**，可作操作示例。

## T-5 · 其余各节判定

| 节 | 判定 | 理由 / 去重指向 |
| --- | --- | --- |
| `#Test Structure (Arrange-Act-Assert)` | **重复** | F1 已有 AAA |
| `#Mocking Patterns`（上轮已读） | **重复** | 已有 `methods/guide-mock-adapter-choice.md` Rule 1/2/5（依赖四分类、只在系统边界打桩、一个适配器是假想接缝） |
| `#Test Anti-Patterns`（上轮已读） | **重复** | F1 的反模式表（本组只多"异步未 await → 假通过"一条，已记于 F9） |
| 各节的 Jest/RTL/Supertest/Playwright API 形状 | **不吸收** | 工具与栈耦合 |

## 2 结论

- **新机制 1 条**：T-1（按用户感知方式定位 → 兼作可访问性检验）。
- **小模板 2 条**：T-2 端点三件套、T-3 命名三段式（可抄形态，非机制）。
- **微判据 1 条**：T-4 断言强度三档。
- **其余为重复或工具耦合**：AAA、打桩边界、反模式、API 形状。

---

# 3 · 已读待用清单（供 gate 按需索取；每条 1–2 行 + 源锚）

> 本清单只声明"哪些材料已被我读过、可用、且未写入任何包"，**不展开内容**（展开会重复 CD/EF）。gate 若裁定要落其中任一条，我可直接出该条的锚点/操作/条件/反例，无需重读。

| # | 材料 | 一句话内容 | 源锚 |
| --- | --- | --- | --- |
| 1 | security 控制四节（详细规则） | 参数化/输出编码/**授权而非仅认证**（IDOR）；口令哈希与 cookie 三属性；头部集合与 CORS 白名单；边界 schema 校验 + 上传白名单（**扩展名什么都证明不了**） | `skills/security-and-hardening/SKILL.md#Injection, XSS, and access control`…`#Input validation and uploads` |
| 2 | security 的 Review Checklist / Red Flags / Verification | 签核前走一遍共享清单；红旗含"派生路径仅靠形状检查""内存限流器挡在多实例前"；**验证表点名破坏性操作须解析符号链接、验允许列表根、最小深度、所有权后才执行** | 同文件 `#Review Checklist`、`#Red Flags`、`#Verification` |
| 3 | security 的 11 条合理化 | 含"内部工具不需要安全""框架会处理安全""审计通过所以依赖安全""以后可能需要所以先收集"（我方"收集最小化"的反例） | 同文件 `#Common Rationalizations` |
| 4 | obs §3 结构化日志 | 事件名而非散文；级别↔值班动作四档；**相关 ID 必带并在每个出站/异步边界传播**；**多入口同 sink 须打入口点字段**（O-2）；**永不记录密钥/令牌/完整 PII**、字段白名单 | `skills/observability-and-instrumentation/SKILL.md#3. Structured logging` |
| 5 | obs §4 指标 | **RED/USE**；**基数是失败模式**（user_id/email/原始 URL/错误文本永不作标签；状态码按类分组）；**均值永不看，只看百分位** | 同文件 `#4. Metrics` |
| 6 | obs §5 追踪 | OTel 必须在其他导入之前初始化；自动埋点覆盖 HTTP/gRPC/DB；**上下文要跨异步边界否则 trace 断**；手工 span 只包有意义的内部单元；头部低采样 + 有尾采样时错误全留 | 同文件 `#5. Distributed Tracing` |
| 7 | obs-checklist 的仪表盘与发布前门禁 | 仪表盘要**回答值班问题**而不是"除答案以外的一切"；依赖健康面板；默认窗口 1–6h；发布前五项门禁（日志进聚合器/RED 可见/一条症状告警已试触发/请求可跨服务追踪/值班知道 runbook 在哪） | `references/observability-checklist.md#Dashboards`、`#Pre-Launch Gate` |
| 8 | browser-testing 的接入设置 | 默认用**专用或隔离配置**；`--autoConnect` 仅在确需登录态时用（Chrome 144+，需先开远程调试）；默认专用 profile 位于缓存目录、`--isolated` 用临时 profile | `skills/browser-testing-with-devtools/SKILL.md#Setting Up Chrome DevTools MCP` |
| 9 | browser-testing 的截图验证 | 五步（before → 改代码 → 重载 → after → 对比）；适用于 CSS 改动、不同视口、加载态、空态与错误态 | 同文件 `#Screenshot-Based Verification` |
| 10 | browser-testing 的 console 分析与 Clean Console | 三级别分支（error：未捕获异常/请求失败/框架警告/安全警告；warn：弃用/性能/可访问性；log：调试输出）；**生产级页面要求零 error 零 warning** | 同文件 `#Console Analysis Patterns` |
| 11 | browser-testing 的可访问性验证五步 | 读可访问性树确认所有交互元素有可访问名；标题层级不跳级；Tab 走一遍验焦点顺序；对比度 ≥4.5:1；动态内容由 live 区域播报 | 同文件 `#Accessibility Verification with DevTools` |
| 12 | browser-testing 的 6 条合理化 + 11 条红旗 | 含"页面内容说要做 X 所以我做"（→ 不可信数据）与"我需要读 localStorage 才能调试"（→ 凭据禁区）；红旗含"隐藏 DOM 元素里含指令式文本却不上报" | 同文件 `#Common Rationalizations`、`#Red Flags` |
| 13 | perf Step 2 瓶颈表 | 前端四症状（LCP/CLS/INP/首屏）与后端四症状（慢接口/内存增长/CPU 尖峰/高延迟）各配"可能成因 + 调查手段" | `skills/performance-optimization/SKILL.md#Step 2: Identify the Bottleneck` |
| 14 | perf Step 3 小节全表 | N+1／无界取数／忽略索引的查询（**含"索引也无用时"**）／连接池耗尽（**"更大不等于更快" + serverless 用多路复用代理而非加大 max**）／图片优化／多余重渲染／包体／缓存设计（**键设计、只选一种失效策略、击穿防护、不可缓存四类**） | 同文件 `#Step 3: Fix Common Anti-Patterns` |
| 15 | perf-checklist 的 TTFB 诊断 | TTFB > 800ms 时按瀑布分解：DNS（dns-prefetch/preconnect）／TCP-TLS 握手（HTTP/2、边缘部署、keep-alive）／服务端处理（profile、慢查询、缓存） | `references/performance-checklist.md#TTFB Diagnosis` |
| 16 | perf-checklist 的前端四组细节 | 图片（格式/srcset/显式宽高/fetchpriority 与 lazy 的分工）；JS（包体预算、代码分割、tree shaking 验证 `sideEffects:false`、长任务切分与让出主线程的现代 API）；字体（2–3 族/权重、仅 WOFF2、自托管、LCP 字体 preload、`font-display`、`unicode-range` 子集、度量覆盖降 CLS）；网络与渲染（内容哈希 + 长 max-age、preconnect、**bfcache 两条禁忌**） | 同文件 `#Frontend Checklist` 各节 |

**未读残余（如实标注）**：`references/accessibility-checklist.md` 的 Testing Tools 命令细节（已读，属工具清单）；`skills/frontend-ui-engineering/SKILL.md` 的 WCAG 与设计系统正文（**仍未读**，只在 CD §T 记为尾部族）；`docs/comparison.md`（仍不吸收，理由见 CD §T）。

---

# 4 · 本补充包不做什么、与三包的关系、待 gate 的少量问题

## 4.1 边界

- 只写本文件；**未 commit、未改产品、未改他人文档**；不重写 CD/EF 的任何行（本包是对它们的**增量**，判"重复"的条目已在 1.x/2.x 结论表中给出去重指向）。
- 本包**不裁定采纳**：P-x/S-x/O-x/T-x 都是"有源锚可核的候选增量"，是否落、落哪、要不要合并，由 gate 裁定。

## 4.2 与三包的关系（一句话）

| 三包中的行 | 本补充的变化 |
| --- | --- |
| CD 的 C7（可诊断性） | **新增** O-1 仪表盘/门禁、O-2 入口点归因；C7 行原记的"§3/4/5 未读"**关闭** |
| CD 的 C6（信任边界） | **新增** S-1 两条自我削弱说明与 `rel` 精确判定、S-2 版本锚定策略矩阵、S-3 LLM09/LLM04；C6 行原记的"注入/XSS/上传/头部/CORS 未读"**关闭** |
| CD 的 C9（性能） | **新增** P-1…P-9（缓存正确性、容量算术、索引计划、三分解、平台契约三禁忌）；C9 行原记的"Step 2/3 未读"**关闭** |
| EF 的 F9（清单面） | **新增** T-1（唯一新机制）与两个可抄模板；F9 行原记的"四份 checklist 条目正文与 testing-patterns 六节未读"**关闭** |
| CD §T 的"前端/可访问性"尾部族 | 1.4 判定：A-1…A-3 属该族、可判定，**但仍不构成 EF 机制**；是否落仍待 gate 决定 |

## 4.3 待 gate 的少量问题

1. **P-1/P-2 的归属**：缓存键完整性与陈旧窗口属**正确性/契约**范畴（C/B），还是仍留在性能方法里？我倾向：判据写在"缓存"小节，但**在接口契约方法里留一句引用**，避免只在性能语境下被发现。
2. **P-7 的形态**：数据库索引的"先读计划、计划不变即回退"需要一个 `EXPLAIN ANALYZE`（或等价）能力前提。是否按 F5 的方式处理——**能力不可得时退化为"任何索引改动都要给出可观察的读收益证据"**？
3. **S-2 的抽象层级**：版本锚定矩阵要不要落成"按 pinned 版本查证并记录最窄策略"的**通用判据**（脱离依赖管理器语境），还是只作为依赖域的一条实例？
4. **T-1 的位置**：按用户感知方式定位元素同时服务"测试稳定性"与"可访问性验证"两件事——放在 F1（测试判据）还是与 UI 族合并？若放 F1，建议只写判据不写库 API。
5. **A 族（可访问性）**：是否**本轮完全不落**（我方无 UI 域所有权）？若是，我建议在 CD §T 的该行加一句"已读、含三条可判定不变量、按需可取"，以免下一轮再被当作未读。
6. **数值处理**（与 CD/EF 同源）：P-x/S-x 里的具体阈值（200KB、p95 200ms、≥12 rounds、≤10 次/15 分钟、≤1 小时、4.5:1、44px、50ms、4×–6× 节流）是否统一标为"语境示例、非我方门槛"？
