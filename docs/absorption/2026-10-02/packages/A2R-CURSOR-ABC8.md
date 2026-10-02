# A2R-CURSOR-ABC8 · cursor-plugins 审核包 8（测量实验 / 性能修复 / 诊断交付 / 程序协调）

- 发现者：tpw-absorb-a2r（A2r）
- 源仓：`cursor-plugins`，pin `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`（只读 locator：`.worktrees/legacy-pre-night-2026-10-01/upstreams/cursor-plugins`）
- 产品基线：night worktree；core `professional-workflow/`（21 文件）；冻结 Backbone 未触碰
- 供 `tpw-absorb-gate` 实质裁定；本包不自行裁定采纳；处置均为“拟/候选/待裁定”
- 与包 1–7 的关系：本包补 F 的测量/诊断证据面与 Driver 的程序协调面；与包 1 MG-7（交接）、包 3 MG-3（CI 循环）、包 5 MG-1（编排任务契约）、包 6 MG-4（无人值守队列）交叉引用，不重复其内容。
- 已接受 gate 对包 1 的路径纠错。

## 1. 包内机制组总览

| MG | 机制组 | 主要源文件（pin 内） | 建议判断位点 | 类型 |
| --- | --- | --- | --- | --- |
| MG-1 | 单一指标的实验纪律（hillclimb） | `pstack/skills/poteto-mode/playbooks/hillclimb.md` | F（测量证据） | 方法候选 |
| MG-2 | 性能修复的测量故事（perf） | `pstack/skills/poteto-mode/playbooks/perf-issue.md` | F/E（测量验证） | 方法候选 |
| MG-3 | 诊断交付（live / captured artifact） | `pstack/skills/poteto-mode/playbooks/runtime-forensics.md`、`trace-forensics.md` | F（诊断证据） | 方法候选 |
| MG-4 | 程序协调者的程序纪律 | `pstack/skills/poteto-mode/playbooks/orchestrate.md` | Driver/F（限缩） | 方法候选（runtime 不吸收） |

---

## MG-1 单一指标的实验纪律（hillclimb）（F）

### 1) 机制与触发情境；源锚点与已读/尚缺

| 源锚点 | 已读 | 尚缺 |
| --- | --- | --- |
| `pstack/skills/poteto-mode/playbooks/hillclimb.md`（全文） | 全文 | 无 |
| `pstack/skills/principle-prove-it-works`、`build-the-lever`、`show-me-your-work`、`sequence-verifiable-units`、`separate-before-serializing-shared-state`、`guard-the-context-window`、`laziness-protocol` | 包 2/5 已读 | 无 |
| 真实测量工具 | **未运行** | 未执行任何 hillclimb |

触发情境：对同一个可测量对象做持续、科学、迭代式的改进（“hillclimb 这个指标”）。一次性修复走 Bug fix 或 Perf issue，本 playbook 是“循环”。

### 2) 操作、成立条件、失败模式、反例/例子

**核心纪律**：“one change, one measurement, keep or revert. Never stack untested changes, and never claim a win from code inspection.”

1. **先 ground 工作负载与架构再选指标**：对目标跑 how，命名能移动结果的真实工作负载维度（data size、history、state、concurrency），选一个复现用户 complaint 的 case；**若没有 case 能复现，先修 repro 而不是 hillclimb**；然后固定**一个指标、哪个方向算更好、以及一个可检查的 stop predicate（把 target 与“尝试次数下限”配对，防止侥幸早胜终结 run）**——示例形状：“至少比 baseline 好 50% 且至少 10 次迭代”；用户给了数字就用，没给就约定。
2. **建测量 harness、证明其敏感度、然后冻结**：跑对比性的真实工作负载，确认 target case 复现症状且更简单的 case 按预期区分开；**若 harness 分不清它们，就改工作负载或指标**；冻结后**一条可重复命令输出指标，采样足以压过噪声（N 次的中位数，不是单次 run）**；在任何改动前记录 baseline 指标与 regression gate 的绿色 run（必须继续通过的测试）。
3. **用 show-me-your-work 开 decision log**：`decision.tsv`，每次尝试一行：id、hypothesis、change、before、after、delta、tests、verdict（kept/reverted）、note；**每次尝试前先读它**；放在 tree 之外（gitignored）。
4. **每个 hypothesis 都要 grounding 在 step 1 的架构模型上**，说出具体机制（“把 X 从 boot path 延后，因为它挡 first paint”），不是“试试 memoize 点什么”。
5. **循环，每次迭代一个 hypothesis**：把改动交给子代理（配置的 hillclimb 模型，scope 紧）；**监督并审查 diff 而不是自己敲**；多个独立 hypothesis 同时活时并行分给各自 worktree 的子代理；用冻结 harness 测 before/after 并跑 regression gate；**只有指标越过噪声且 gate 保持绿才接受，否则完整 revert**（“might help” 的 tweak 不留）；**每个被接受的修复一个 commit，只 stage 你改过的文件（`git add <files>`，绝不 `-A`）**；**无论 kept 还是 reverted 都记一行**。每次迭代在下一次开始前结束于一个检查。无人值守时只借用 autonomous-run 的 wake 机制，**不借它的 stop rule**。
6. **推过第一个 plateau**：停滞、连续几个 reject 时，pivot 类别、组合 near-miss、重读源码或尝试更激进的方案，再断定山爬完了；**正确性与简单性优先于数量**；破坏行为的“win”要 revert；保持住数字的简化要保留。
7. **predicate 满足或剩余想法边际收益不值得成本时停**；**不放宽 predicate 来迎合**；**cheap untried hypotheses 还在时不要退出**；卡住就 surface，不空转。
8. 走 Opening a PR，**被接受的 commit 按落地顺序 stack**。

**成立条件**：存在可复现的用户 complaint case；有可冻结的测量 harness；有 regression gate；指标不被噪声吞掉。

**失败模式/反例**：选指标前没有 workload/架构 grounding；没有 repro case 就 hillclimb（应先修 repro）；harness 无法区分 target/easy case 仍继续；单次采样当指标（噪声）；不证明 harness 敏感度就冻结；stack 未测改动；从代码检查宣称胜利；接受“might help”的 tweak；`git add -A` 混入无关文件；只在 kept 时记 decision；放款 predicate；cheap untried hypotheses 还在就退出；用被测系统的自报代替 harness。

### 3) 判断位点与 Profile 调用

| 位点 | 专业 concern | 何时调用 | 由哪个 Profile 提议 |
| --- | --- | --- | --- |
| F：指标/阈值/复现/噪声/回归 gate | 证据 | 性能或其他持续指标改进 | `evidence-evaluation` |
| E：单假设最小改动 | 实现 | 每轮尝试 | `implementation` |
| Driver：迭代顺序与停滞处置 | 程序性 | 长循环 | `driver` |

### 4) 当前产品锚点、覆盖、缺口、为何值得吸收

- `methods/behavior-claim-evaluation.md`：单 claim、条件/度量/阈值、baseline/treatment、三态。
- `profiles/evidence-evaluation.md` `## 常见误区`：“只验证‘能跑通’，不设计能揭示错误的负控制。”
- `methods/local-defect-feedback-loop.md`：“Do not require every task to enumerate a fixed number of hypotheses, try every reproduction technique…”。
- 产品没有“持续指标改进”的实验纪律。

具体缺口：

1. **没有 stop predicate 的“target + 尝试下限”形状**：产品的 claim 有 threshold，但没有“防止侥幸早胜”的次数下限；这是持续实验与单次 claim 的关键差别。
2. **没有 harness 敏感度证明与冻结**：先证明 harness 能区分 target/easy case，再冻结；产品有“同一命令同环境”，但没有“证明测量面敏感度”。
3. **没有“接受/完整 revert”与“每次尝试一行（kept 或 reverted）”的台账纪律**：与包 1 MG-8 的轨迹同源但触发不同（实验循环）。
4. **没有“放款 predicate 是禁止的”“cheap untried hypotheses 还在就不退”“正确性/简单性优先于数字”**三条收口。
5. **没有“只 stage 改过的文件”**的提交卫生。

为何值得吸收：这是 F 在持续优化场景下的操作面，且与 `behavior-claim-evaluation`（单 claim）互补；全为判据，零平台耦合。

### 5) 拟处置与载体

- 拟保留：workload/架构先 grounding；先修 repro；target + 尝试下限的 predicate；harness 敏感度证明后冻结；N 次中位数；baseline + regression gate；decision.tsv 每次尝试一行、kept/reverted 均记；单 hypothesis；接受/完整 revert；只 stage 改动文件；推过 plateau 的手段；不放宽 predicate；cheap untried 不退出；正确性/简单性优先。
- 拟改变：去模型名/子代理/`git add` 具体命令与 `decision.tsv` 文件名为产品中性说法（决策台账）；去“borrow wake mechanism”的宿主细节（保留无人值守的条件）。
- 拟删除：具体模型与 per-role 配置。
- 载体：方案 1（推荐）新增 `methods/guide-measurement-experiment.md`（持续指标实验），与 `behavior-claim-evaluation.md`、包 1 MG-8 的轨迹方法交叉引用；在 `profiles/evidence-evaluation.md` 按需入口加一行；方案 2 并入 `behavior-claim-evaluation.md`（代价：该文件声明为单 claim 参考，持续循环会撑破边界）。本包倾向方案 1。
- 与 a4 的分工：性能剖析工具与实现面归 a4；本组保留实验与证据纪律。

**平台耦合/依赖**：测量工具是宿主；纪律零耦合。

### 6) 正文草稿与验证方案

```
持续指标实验（草稿）
1. 先 grounding 工作负载与架构，选复现用户 complaint 的 case；无 repro 先修 repro。
2. 固定一个指标、方向、predicate = target + 尝试次数下限（防侥幸早胜）。
3. 建 harness → 证明能区分 target/easy → 冻结；N 次中位数；记录 baseline 与 regression gate 绿。
4. 每次一个 hypothesis，grounding 在架构上（说具体机制）；测 before/after + gate。
5. 越过噪声且 gate 绿才接受，否则完整 revert；“might help”不留；每次尝试记一行（kept/reverted）。
6. 推过 plateau（pivot/组合/重读/激进），不放宽 predicate，cheap untried 还在不退；正确性/简单性优先于数字。
```

验证方案（未执行）：选一个真实小指标，检查 (a) harness 是否先证明敏感度再冻结；(b) 是否 kept/reverted 均记录；(c) 是否拒绝了一次“might help”的改动；(d) predicate 是否含次数下限。边界：不要求所有优化都做 prolonged hillclimb；一次修复走局部缺陷方法。

---

## MG-2 性能修复的测量故事（perf）（F/E）

### 1) 机制与触发情境；源锚点与已读/尚缺

| 源锚点 | 已读 | 尚缺 |
| --- | --- | --- |
| `pstack/skills/poteto-mode/playbooks/perf-issue.md`（全文） | 全文 | 无 |
| `cursor-team-kit/skills/control-cli`、`control-ui`（包 5 MG-3 已读） | 全文 | 无 |
| `methods/local-defect-feedback-loop.md`（产品） | 已读 | 无 |

触发情境：有测量过的慢点要追踪并改善（“启动 1.8s，trace 它，修测得的原因，给我 before/after”）。

### 2) 操作、成立条件、失败模式、反例/例子

**六步**：“You own the measurement story. Plan, review, verify the numbers. Tie every fix to a measurement, don't read source instead of measuring.”

1. 通过匹配 control skill 捕获 **baseline trace**。2. 用 how grounding hypotheses；**没有先跑过就不要宣称 perf ceiling**。**大部分修复来自八个策略族**，把它们当 hypothesis 生成器而非 checklist；**一个族只有在 trace 显示它命名的信号时才获得尝试资格**：Elimination（先问热路径是否需要存在：没人消费的计算、对该用户 always-off 的 feature gate、冗余镜像状态的 sync、just-in-case 的 legacy path；**trace 只显示什么慢、从不显示什么可删，所以这一族需要 how pass 而不是 profiler**）；Divide and conquer（主导成本随输入规模增长：chunk/shard/prune 或并行独立块）；Caching（相同输入重复计算/取：存并复用，**声称胜利前先命名什么使它失效**）；Indirection（热路径做昂贵工作而更便宜的中间层能吸收：索引替代扫描、队列把工作挪出交互线程、handle 让更便宜实现换入；**只有当它从 critical path 移除的比增加的多时才加这跳**）；Batching（许多小操作各付固定开销：合并成一批付一次）；Redundancy（等待卡在一个慢实例/尝试：复制工作取最快；**trace 必须显示等待占主导且系统有 headroom**）；Lazy evaluation（成本落在从未使用或尚不需要的结果上：boot path 上的 eager init、渲染 offscreen：延后到首次使用）；Scheduling（工作必须发生但不在交互时刻：idle callback、boot 后 warmup、用户到来前 precompute、frame commit 后 cleanup；**赢的是感知延迟，所以要测交互路径而不是总工作量**）。3. 从 trace 计划修复；跨函数边界先 architect；委派实现；审查 diff；**捕获 post-fix trace**；每个尝试在下一个前验证。4. **解析并比较 artifact（JSON to sqlite, diff）**；**“Inconclusive” 或错 surface 不是 pass，要 flag**。5. 在 PR 里引用测量。6. 走 Opening a PR。持续改进而非一次性修复 → Hillclimb。

**成立条件**：有可捕获的 baseline trace 与匹配 surface；有 control skill；修复可被 post-fix trace 比较。

**失败模式/反例**：不测就宣称 ceiling；把八族当 checklist 每族都试（无 trace 信号）；用 Elimination 时只看 profiler 不看 how；Caching 不说失效条件；加 Indirection 但没从 critical path 净移除；Redundancy 无 headroom 证据；Scheduling 只测总工作量；post-fix 不捕获 trace；inconclusive/错 surface 当 pass；PR 不引用测量。

### 3) 判断位点与 Profile 调用

| 位点 | 专业 concern | 何时调用 | 由哪个 Profile 提议 |
| --- | --- | --- | --- |
| F：baseline/treatment trace 与比较 | 证据 | 性能 claim | `evidence-evaluation` |
| E：策略选择与实现 | 实现/性能 | 修复时 | `implementation`（a4 侧） |
| D：策略跨界时 | 技术 | indirection/batching 影响接口 | `technical-planning`（a4 侧） |

### 4) 当前产品锚点、覆盖、缺口、为何值得吸收

- `methods/behavior-claim-evaluation.md` `## Method` 2：“Compare baseline and treatment with the same command, data and environment.”
- `profiles/evidence-evaluation.md` `## 常见误区`：“把环境/工具故障判成产品 FAIL”。
- `docs/WORKFLOW-INTENT.md` §4 的 Performance 作为横向 concern（Backbone §1：“Security、Performance、Persistence、UX、Compliance 是 professional concern”）。

具体缺口：

1. **产品没有“性能修复从 trace 出发”的策略生成器**：八族（尤其 Elimination 需要 how、“trace 显示什么慢但从不显示什么可删”）是具体操作经验；产品只有 claim 比较。
2. **没有“错 surface/inconclusive 不是 pass”**（与三态一致但需在性能语境点名）。
3. **没有“Caching 先命名失效条件”“Indirection 净移除”“Redundancy 需 headroom”“Scheduling 测交互路径”**这些“胜利条件先于宣称”的检查。

为何值得吸收：性能是 Backbone 已列的横向 concern，产品缺该方法；八族+胜利条件可直接用于 D/E/F 的性能判断，且不引入工具依赖。

### 5) 拟处置与载体

- 拟保留：baseline trace；不测不宣称 ceiling；八族作为条件性 hypothesis 生成器；每族的“赢的条件”（Elimination 需 how、Caching 需失效条件、Indirection 需净移除、Redundancy 需 headroom、Scheduling 测交互路径）；post-fix trace；artifact 解析比较；inconclusive/错 surface 不是 pass；PR 引用测量。
- 拟改变：去 `how`/`architect`/模型/control skill 名（改为一般能力）；去 JSON-to-sqlite 具体工具（作例子）。
- 拟删除：无。
- 载体：方案 1（推荐）并入包 1 的 `methods/guide-proof-strength.md`（证据强度）作为“性能测量”一节，或与 MG-1 的测量实验合并为 `methods/guide-measurement-and-perf.md`；方案 2 独立 `methods/perf-evidence.md`（代价：与测量实验触发高度重叠）。本包倾向与 MG-1 合并（同族：测量证据），并在 `profiles/evidence-evaluation.md` 入口引用。
- 与 a4 的分工：具体 profiler/实现归 a4；本组保留“trace 驱动 + 胜利条件”的判断。

**平台耦合/依赖**：剖析工具是宿主；判断零耦合。

### 6) 正文草稿与验证方案

```
性能证据（草稿）
1. 先捕 baseline trace；没跑不宣称 ceiling。
2. 八族是 hypothesis 生成器不是 checklist；每族只有在 trace 显示其信号时才试。
   胜利条件：Elimination 需 how 证明可删；Caching 需命名失效条件；Indirection 需净移除 critical path；Redundancy 需 headroom；Scheduling 测交互路径。
3. 跨边界先设计；每尝试验证；捕 post-fix trace；解析比较 artifact。
4. inconclusive/错 surface 不是 pass，要 flag；PR 引用测量。
```

验证方案（未执行）：对一个真实慢点跑八族筛选，检查是否只有 trace 有信号的族被尝试、Caching 是否先命名失效条件、post-fix trace 是否比较。边界：无 control skill/surface 时记录阻断；一次性修复不必走 hillclimb。

---

## MG-3 诊断交付：live 与 captured artifact（F）

### 1) 机制与触发情境；源锚点与已读/尚缺

| 源锚点 | 已读 | 尚缺 |
| --- | --- | --- |
| `pstack/skills/poteto-mode/playbooks/runtime-forensics.md`（全文） | 全文 | 无 |
| `pstack/skills/poteto-mode/playbooks/trace-forensics.md`（全文） | 全文 | 无 |
| `pstack/skills/poteto-mode/playbooks/autonomous-run.md`（包 1 MG-8 已读） | 全文 | 无 |
| 真实 profiler/CDP/heap 工具 | **未运行** | 未执行任何取证 |

触发情境：runtime-forensics——诊断一个运行时症状（leak、idle-CPU spin、glitch），从 live instrumentation 入手，**交付物是诊断不是修复**；trace-forensics——诊断一个事后交给你的 captured profiling artifact（cpuprofile、trace、spindump、heap snapshot），**交付物同样是诊断不是修复**。

### 2) 操作、成立条件、失败模式、反例/例子

**runtime-forensics（5 步）**：① 在匹配 surface 上通过 control skill 捕 live 信号（spinning 进程的 CPU profile、leak 的 heap snapshot、visual glitch 的 CDP trace）——**真实 artifact 不是猜测**；② 把 artifact 缩减到 smoking gun（热路径上的函数、从 leaked object 到 GC root 的 retainer chain、无输入仍在触发的 loop）；**大 artifact 在子代理解析，主线程只留缩减后的 finding**；③ **在相信机制之前先证明它**：通过 CDP eval 在运行进程注入 instrumentation，或热修 live code 而不 reload，便宜地确认 hypothesis；④ 把 finding 映射回源码：file、symbol、分配或调度的行；⑤ throughput checkpoint 保持一行 `throughput checkpoint: n/a, read-only forensics`。Reply：捕获的信号、缩减后的 finding、如何证明机制、源码位置、artifact 路径；**除非被要求不给修复**；原因已知后交回 Bug fix 或 Perf。

**trace-forensics（6 步）**：与 runtime-forensics 区分——**capture 已经存在；artifact 是固定数据集，读它、不要重跑**；工具保持通用以便可移植（cpuprofile 与 `.json.gz` 用 DevTools/trace parser、spindump 用文本编辑器、heapsnapshot 用 heap 工具）。① 识别格式并用对的工具加载；大 artifact 在子代理解析、主线程留缩减 finding；② **把原始 artifact 转成可查询形式**：把 trace 或 heap snapshot dump 进 sqlite，一行一个 sample/frame/node；**先到可查询形状再读**；③ 缩小原因：查占时间最多的 frame 并沿 call tree 走热路径；leak 则从 leaked object 沿 retainer chain 到 GC root；spindump 则找卡在 on-CPU 或 blocked 的线程及其 wait reason；④ **归因到源码**：用 artifact 自带符号把热 frame 映到 file/symbol/line；**没有源码映射的 frame 还不是诊断**——解析符号，或明说 artifact 不携带它们；⑤ **有配对 capture 就对照确认**：diff before/after artifact；没有配对则**把 finding 标为“artifact 支持的最强 hypothesis”而不是确认的原因**；⑥ 交回有引用的诊断，除非被要求不给修复；原因已知后路由到 Bug fix 或 Perf issue；throughput checkpoint 一行。Reply：artifact 与格式、缩减 finding、源码位置、artifact 路径、配对 capture 是否确认。

**成立条件**：能捕获 live 信号或拿到 captured artifact；有符号/源码映射；有（或没有）配对 capture。

**失败模式/反例**：从源码理论化而不 instrument（runtime）；把猜测当诊断；大 artifact 直接在主线程读爆上下文；相信未证明的机制；找 frame 但不解析符号就称诊断；没有配对 capture 却宣称确认原因；trace-forensics 重跑 capture（它是固定数据集）；交付诊断时顺手修（越权）；配对 diff 缺失时不标注假设性质。

### 3) 判断位点与 Profile 调用

| 位点 | 专业 concern | 何时调用 | 由哪个 Profile 提议 |
| --- | --- | --- | --- |
| F：诊断证据（信号、机制证明、归因） | 证据 | leak/spin/glitch/artifact 诊断 | `evidence-evaluation` |
| E：instrument/hotfix（live 证明） | 实现 | 需要便宜确认 hypothesis 时 | `implementation`（a4 侧） |
| Driver：诊断完成后的路由（Bug fix/Perf） | 程序性 | 原因已知后 | `driver` |

### 4) 当前产品锚点、覆盖、缺口、为何值得吸收

- `methods/local-defect-feedback-loop.md` `## Method` 2：“do not infer a root cause from an unverified log message”；3 竞争解释。
- `profiles/evidence-evaluation.md` `## 关键问题`：“什么观察能把‘成立’与‘不成立’分开？”
- `methods/behavior-claim-evaluation.md` `## Limits`：“This method evaluates a specific observable claim, not user value or overall task closure.”

具体缺口：

1. **产品没有“诊断交付”与“修复交付”的分离**：两种 forensics 都明确“deliverable is a diagnosis, not a fix”，原因已知后路由；产品有召回/路由，但没有“诊断本身是产物”的形态。
2. **没有 live vs captured 的两条路径**（instrument 还是读固定 artifact；captured 不重跑）。
3. **没有“证明机制先于相信”**（CDP eval/hotfix 便宜确认）与“无源码映射的 frame 不是诊断”。
4. **没有“配对 capture 才能确认，否则只是最强假设”**的置信纪律——与 why 的 confidence 分层同构但对象是 profiling artifact。

为何值得吸收：这是 F 在“不清不楚的运行时症状”上的取证方法，与局部缺陷反馈循环（可复现 bug）互补；全为判断与证据纪律。

### 5) 拟处置与载体

- 拟保留：live 信号捕获、缩减 smoking gun、主线程留 finding；相信前先证明机制（instrument/hotfix）；映射回源码（file/symbol/行）；诊断不是修复、原因已知后路由；captured artifact 是固定数据集不重跑；先转可查询形状再读；按 artifact 类型缩小（热 frame、retainer chain、wait reason）；无源码映射不算诊断；配对 capture 才确认，否则标最强假设。
- 拟改变：去 CDP/DevTools/sqlite 具体工具名（保留“instrument、可查询化、符号映射”等一般操作）；去模型/子代理细节。
- 拟删除：无。
- 载体：方案 1（推荐）并入包 1 的 `methods/guide-proof-strength.md` 或与 MG-1/2 合并为 `methods/guide-measurement-and-diagnosis.md`；方案 2 独立 `guide-forensics.md`。本包倾向与测量族合并（同属“从真实 artifact 取证”），在 `methods/README.md` 按需表加一行。
- 与 a4 的分工：profiler/heap/CDP 工具与实现归 a4；本组保留诊断证据纪律。

**平台耦合/依赖**：profiler/CDP/heap 工具是宿主；纪律零耦合。

### 6) 正文草稿与验证方案

```
诊断交付（草稿）
live：捕真实信号（CPU/heap/CDP trace）→ 缩减 smoking gun（主线程只留结论）→ 在相信前用 instrument/热修证明机制 → 映射 file/symbol/行 → 诊断交回，修复另派。
captured：固定数据集不重跑 → 用对工具加载 → 转可查询形状（一行一 sample/frame/node）→ 缩小（热 frame / retainer chain / wait reason）→ 符号映射回源码（无映射不算诊断）→ 有配对 capture 才确认，否则标“最强假设”。
两者都是 read-only 诊断；原因已知后路由 Bug fix 或 Perf。
```

验证方案（未执行）：用一个人工构造的 heap 或 CPU artifact 跑 captured 路径，检查 (a) 是否先转可查询再读；(b) 是否有符号映射；(c) 无配对时是否标为假设。边界：无 control skill/符号时如实报阻断；不越权修复。

---

## MG-4 程序协调者的程序纪律（Driver/F，限缩）

### 1) 机制与触发情境；源锚点与已读/尚缺

| 源锚点 | 已读 | 尚缺 |
| --- | --- | --- |
| `pstack/skills/poteto-mode/playbooks/orchestrate.md`（全文，16779B） | 全文 | 无 |
| `orchestrate/skills/orchestrate/references/*`、prompts（包 1 MG-7 + 包 5 MG-1 已读关键） | 相关 | scripts/state.json 细节归 a4 |
| `pstack/skills/show-me-your-work/SKILL.md`（包 1 MG-8 已读） | 全文 | 无 |

触发情境：整个项目交给一个 standing coordinator chat：多日、许多 stacked PR、几十到几百个子代理、人类一天 check in 两次（“run this whole project”“own this migration until it lands”）。一个任务驱动到 predicate 是 autonomous-run；需要 bespoke workflow 的雄心 run 是 figure-it-out；只有超出单 agent 生命周期的才走这里。

### 2) 操作、成立条件、失败模式、反例/例子

**三根支柱**：“Completions are queue events, not interrupts. Every spawn and every resume carries the standing orders verbatim. The brief is the product. A vague brief fails quietly, because a worker cannot ask you a question.”

**角色与放置**：Coordinator（本地；frame、写 brief、drain inbox、拥有 human report、做判断；**绝不写/改代码**；冲突合并、restack、代码改动永远是任务； mechanically landing 一个已验证单元（fast-forward 或干净 cherry-pick 后 push）是 coordinator 可自做的 bookkeeping，在本地 git 便宜时）；Sub-coordinator（本地、持久、每 track 一个，只在程序超出单 coordinator drain 能力时；每层嵌套都要重付完整 orientation preamble；blocking 的 sub-coordinator 会藏住 children 而 parent 空转；拥有自己 track 的 units/boards、写 worker brief、spawn 自己的 worker/verifier、在 wave 边界 roll up；**绝不转发 raw child report**；in-flight child 上限约十个滚动窗口，永不 blocking batch）；Worker/verifier（除需要本机（control skill 验证、本地 transcript、模拟器、仅本机 auth）外都用 cloud）。**深度固定在 coordinator/track/worker**；track 分解按项目（build/landing/verification 是常见切法不是必需形状）；硬编码 swarm 树被尝试后认为太僵而被 park。

**Store layout（每文件恰一个 writer）**：`preferences.md` 是 standing orders 寄存器（编号行、一行一条约束：model policy、stack shape/count、verification bar、forbidden paths、escalation policy；**每次 spawn 与 resume 逐字粘贴**——指令会跨 resume 衰减，掉一条就多花人类一个回合；**当发现自己在重述某条指令时，先 append 再行动**）；`overview.md` 持久 PR/issue DB，append 不整体重写；`units.tsv` 一行一单元（id/track/state/branch/PR/head SHA/brief path）就地更新；`frontier.json` 计算出的 merge frontier；`ledger.tsv` 验证台账；`inbox/` 完成指针；`gates.md` 停人类 gate（问题、选项、无回答时的默认）；`decisions.tsv` 轨迹；`status.md` **每次 drain 从 units.tsv/ledger.tsv 派生，绝不手维护**。

**Brief 模板（每次 spawn 都带全）**：GOAL（一句、结果、无 chat 访问的陌生人可执行）；SCOPE（可写路径、不可写、独占 worktree/branch）；CONTEXT（文件与 PR 指针；**依赖的上游报告要全文粘贴，因为 worker 看不到 sibling**）；ACCEPTANCE（可检查标准，一行一条）；VERIFY（确切命令或 control-skill 路径 + known gotchas）；TIMEBOX（粗略运行时上限；到期返回部分发现并停，不继续跑）；FORBIDDEN（no gt、no rebase、no force-push、no fixes outside scope + 单元特有禁令）；REPORT（status、branch、head SHA、PRs、verdict、**真正跑了什么**、deviations、建议 follow-up）；STANDING（preferences.md 逐字）。**按单元大小 brief**（一行命令的单元压成一段但仍含 goal/scope/verify/report shape；4KB 模板围着一个两行编辑是成本）；本地 spawn 可按 store 路径引用 standing orders，**cloud spawn 与每次 resume 必须逐字**。Sub-coordinator brief 另加 track 边界与 unit 列表、spawn 预算与 local 例外表、drain 协议、rollup 格式。**依赖是 context relay 不只是顺序**；未声明的上游上下文让 worker 猜；**缺字段是 refuse-to-spawn 条件**；每个 sub-coordinator 每 wave 抽审一份 worker brief，**与它抽样的 wave 并行，绝不作为其前面的 gate**；brief 失败停该 track 并修 sub-coordinator 的指令（不只修 worker），因为 brief 质量在 run 后期衰减；**绝不 resume-chain 一个 brief**，用合并 scope 重新 respawn。

**Steps**：1 Frame（done predicate 写成可计数的，如“126 units 全部合并、每个 ledger-verified unit-test-verified 或更好”；量化 scope：units、粗估 effort、预期 stacks、wall-clock 预算；**若单 agent 能在预算内完成，停在这里走 Autonomous run**；collapsing 不依赖另一文档存在；约 70% 预算时停止 spawn 并落地已验证部分；争议分解或 one-way door 先过 arena；framing 只讲一次，reversible prep 不等）。2 Install runtime（init、开轨迹、**任何 spawn 前写 standing orders**、seed frontier）。3 **Pilot**：把一个单元走完整路径（brief→worker→verification→stack entry→ledger row→merge），**pilot 的存在是为了用 1 个 agent 的代价证伪 brief 模板、verify recipe 与单元大小**，在任何 fan-out 前从 pilot 证据修合同；近同质廉价单元的第一个单元就是 pilot；专用 pilot pipeline 只用于昂贵/新颖单元形状。4 Scale（滚动窗口到 in-flight cap，完成即补；**blocking batch 要付每批最慢 child 的代价**；recompute ready work after each drain；把上游报告 relay 进下游 brief；兄弟只向上通信；抽审 brief 与 wave 并行、失败停下一次 refill 而非当前）。5 Drain。6 **Land 是连续的，绝不是终末 phase**：integration 从第一个已验证单元开始并与剩余 wave 并行；重仓 repo 从第一波起就有 standing stacker；本地 git 便宜时 coordinator 自己落地；**保持 frontier green 再做 upper-stack 工作**；只在 merge 或报告新 head SHA 时推进 frontier.json。7 Close（drain 最后 inbox、**把每个 spawn 过的 agent 对账到终态行（done/abandoned/zombie-reconciled）**、在真实 artifact 上确认 predicate、确认每个 landed PR 对它当前 head SHA 都有 verdict、审计轨迹含跨模型 review、把反复纠正编码进 preferences.md 或 brief 模板；store 保留作为 postmortem）。

**Queue and drain**：完成通知 → 推 inbox 并回到手上的事，**绝不 inline deep-review**；需要 review 的完成变成 verifier unit；**绝不在 drain 里 review diff**。在四个点批量 drain：critical section 结束、track rollup、frontier watcher wake、human report 前；每次 drain 先 drain inbox；drain 期间到达的等下一批。先完成你手上的 critical sections（写 brief、stack 操作、冲突决定、写 gate、更新 ledger/frontier）。每次 drain 分类每个指针（landed/needs-verify/failed/zombie/noise）、经 CLI 写行、跑 status、一条消息 spawn 下一波；**每个 spawn 的 child 都要在其 track rollup 对账（arrived/respawned/scope 被显式吸收）**——静默重做缺失 child 的工作会同时隐藏浪费与覆盖缺口。drain 回合一结束于三行 status（计数、变化、开着的 gate）；细节在 status.md。

**Stack safety**：frontier 是计算对象不是叙事；每次 merge 与 stack mutation 后从权威工具重算（GitHub base ref 会在 restack 中途漂移）；**恰好一个 stacker 每 stack 可运行 stack 工具，串行**，holder 记在 standing orders；restack 在 cloud（本机规模化 restack 会拖垮笔记本）；**worker 永不 rebase、永不运行 stack 工具**；babysitter 一个 stack 一个、scope 到一个不可变 frontier generation，冲突报告给 stacker 而不是自己 restack；PR close/retarget 只经 stacker（关 base PR 会 orphan 整条上面的链）；merge 与 stack surgery 是像其他单元一样的带 brief 单元；一个 retro watcher 跟踪已合并 PR 的 revert、post-merge CI 破坏、orphan follow-up。

**Verification**：**按单元缩放**——VERIFY 是单条便宜命令时 worker 跑并报输出、coordinator 抽验 receipts；专用 verifier agent（与 worker 不同模型家族）用于验证昂贵、判断密集或高 blast radius 的单元；**整个产物只是重跑一条命令的 verifier agent 是 ceremony 不是 verification**。Ledger 一行一 verdict，key 是 PR 号 + head SHA：`live-ui-verified | unit-test-verified | type-check-only | verifier-blocked | verifier-failed`；**CI green 是 verdict 的输入不是 verdict**；行为工作要好于 `type-check-only`；`verifier-blocked` 不是 pass（环境恢复后 respawn）；`verifier-failed` 得到 fix unit 而不是 re-verify；worker 可自报、verifier 在同 key 覆盖；**新 head SHA 使旧行失效，restack 后重验**；ledger 回答“是否验证过”，不是记忆也不是 transcript。**单元未把输出外化就不算完成**：worker push branch、verifier 写 ledger 行、receipts 落 store；只在某个 VM 上存在的工作在 VM 死时从未存在。

**Liveness and failure**：**绝不 resume 一个 agent 来检查它**（resume 会重启 idle agent）；只读 probe：ledger、units.tsv、forge、pushed branch、cloud agent 状态；**transcript mtime 不是 liveness**；silent death 得到合成 postmortem inbox 行（unit、failure mode、last evidence、options）；按证据 replan、不等完全静止；retry by mode：cap-hit/oom 缩小 scope respawn；network-drop 原样；tool-error 换模型；unknown 重试一次；**两次重试后 abandon 该单元并 replan around it**；**僵尸迟到回来先对账当前 frontier 与 ledger 再接受**，通过新单元 salvage 独有发现，绝不盲 merge；**继续 spawn 会产生全树垃圾时**在 standing orders 顶部写 stop line、让 in-flight 完成、修因、清线；**像约束 child 一样约束自己的 infra retry**（连续几次 tool abort 后停止重试，写终态 handoff 到持久状态并结束 run）；Cursor 重启后本地 agent 死、cloud 工作不死：重读 standing orders 与 units.tsv、重算 frontier、**按 PR/branch 而不是 agent id 重挂 cloud 工作**、每个 track 从 stored brief + 当前状态 respawn 一个 sub-coordinator、drain、resume；锁由下次写清除。

**Escalation**：到人类的（批量进 status page 而非逐项）：irreversible actions（force-push 共享分支、deploy、删除、关别人的 PR）、genuine product/preference calls 无实验能定、与观察现实矛盾的 standing order、replan 后仍存的 program-level dead end；每项先 park 为 `gates.md` 条目再问，并把工作绕开它。**绝不**到人类的：frontier nudges、restack mechanics、retries、CI flake triage、review-thread triage、format fixes、brief 已禁的 scope（refuse 并继续）、“我应该继续吗”；**拿不准就行动并记录**。Mid-run discoveries 只修阻塞 frontier 的；其余 park 成 follow-up（这个 fan-out 下小 scope 泄漏会繁殖成没人要的 PR）。Reply 在 checkpoints/close 给：predicate 与计数（来自表不是叙事）、tracks 及各自落地、frontier（PR 列表+SHA）、verdicts 摘要、abandoned 与原因、等人类的 gates（唯一 ask）、store path、trail path；含 PR 链接。

**成立条件**：工作真的超出单 agent 生命周期；有持久 store 与 standing orders；有 coordinator 可 drain 的队列。

**失败模式/反例**：把 completion 当 interrupt 立即深审；spawn/resume 不带 standing orders（指令衰减）；vague brief（worker 无法提问→静默失败）；缺字段仍 spawn；resume-chain brief；blocking batch；把 sub-coordinator 当默认层；worker rebase/run stack 工具；多 stacker；verifier 只是重跑一条命令；CI green 当 verdict；旧 head 的 ledger 行继续有效；在 drain 里 review diff；resume agent 查活性；transcript mtime 当活性；两次重试后仍硬试；僵尸盲 merge；自己的 infra retry 不设界；按 agent id 重挂重启后的工作；把该自主处理的事抛给人类；把 mid-run discovery 全做进 scope；close 不把每个 child 对账到终态。

### 3) 判断位点与 Profile 调用

| 位点 | 专业 concern | 何时调用 | 由哪个 Profile 提议 |
| --- | --- | --- | --- |
| Driver：队列/drain/brief/standing orders/活性/升级 | 程序性 | 程序级协调 | `driver` |
| F：ledger/verdict/head SHA/验证缩放 | 证据 | 每单元验证 | `evidence-evaluation` |
| A/Voice：人类 gate 与不可逆动作 | 授权 | 升级时 | `intent-voice` + authority |
| D：stack 拓扑与 restack | 技术 | frontier 变动 | `technical-planning`（a4 侧） |

### 4) 当前产品锚点、覆盖、缺口、为何值得吸收

- `profiles/driver.md` `## 关键问题`：“本次关闭对象、证据要求与关闭规则是什么？谁持有关闭权？”；“并行写者的写集是否明确？共享文件是否单写者串行集成？”
- `profiles/driver.md` `## 常见误区`：“管到进程、并发、锁等 execution mechanics。”
- `authority/RESPONSIBILITY-BACKBONE.md` §4：“常规交接用产物指针和短消息，不让 Owner 每次扮演转述专业上下文的人。”
- 包 5 MG-1（orchestrate 插件的任务契约）与包 6 MG-4（autopilot 队列）已覆盖任务发布/依赖/证据 gate；本组补**coordinator 侧的 brief/standing orders/drain/活性/升级/关闭**。

具体缺口：

1. **没有“brief 是产品、缺字段拒绝 spawn、依赖是 context relay”**的发布纪律；与包 5 MG-1 的“任务发布即最后机会”互补（一个讲任务内容，一个讲协调者如何写与审）。
2. **没有 standing orders 逐字随每次 spawn/resume 的防衰减纪律**，以及“发现自己在重述就先 append”。
3. **没有 drain 的四点批量与“绝不在 drain 里 review diff”**；没有“完成是队列事件不是中断”。
4. **没有 ledger 以 PR+head SHA 为 key、新 head 使旧 verdict 失效、verifier-blocked 不是 pass、verifier 只重跑一条命令是 ceremony** 的验证缩放纪律（与包 6 MG-2 的 patch-id 同族，对象是 ledger）。
5. **没有只读活性 probe、“transcript mtime 不是 liveness”、“绝不 resume 来检查”**。
6. **没有升级分类**（什么到人类、什么绝不到人类、gates.md 先 park 再问、绕开）。
7. **没有 close 的全量对账**（每个 spawned agent 到终态、每个 landed PR 的当前 head verdict、轨迹含跨模型 review、反复纠正编码进 standing orders）。

为何值得吸收/限缩：这组是 Driver 在程序级最完整的操作经验；但**必须限缩**：runtime/store/CLI/cloud/并发机制不吸收（与产品“Driver 只在逻辑编排层”一致），只保留“brief 纪律、队列事件、drain 分类、验证台账 key、只读活性、升级边界、关闭对账”。不得把“cloud 默认/本地例外”“进程/锁”等 execution mechanics 带入。

### 5) 拟处置与载体

- 拟保留：coordinator 不写代码；completion 是队列事件；brief 模板字段与缺字段拒绝；依赖是 context relay；standing orders 逐字粘贴与 append-before-act；按单元大小 brief；抽样 brief 审计与 wave 并行不作为前 gate；pilot-first 与“用 1 个 agent 证伪合同”；滚动窗口而非 blocking batch；drain 四点与分类；绝不 drain 内 review；landing 连续、frontier 计算对象、stacker 单写者、worker 不 rebase；ledger key=PR+head SHA、新 head 失效、blocked 不是 pass、验证按单元缩放；输出外化才叫完成；只读活性 probe（transcript mtime 不是 liveness）；失败重试阶梯与两次后 abandon；僵尸先对账；stop line；约束自己的 infra retry；重启按 PR/branch 重挂；升级分类与 gates.md；mid-run 只修 frontier blocker；close 全量对账。
- 拟改变：去 `orch.ts`/store 路径/cloud/cursor/Task/子代理上限数值（保留“持久台账/队列入口/可用执行环境”等一般词）；把 ledger 值合并进产品三态表达（PASS 的子类），不新增第四态。
- 拟删除：CLI/锁/进程机制（不复活 runtime）。
- 载体：方案 1（推荐）扩写包 1 的 `methods/handoff-and-evidence-grading.md`（加入 coordinator 侧 brief/drain/ledger）或新增 `methods/program-coordination.md`，与包 5 MG-1、包 6 MG-4 交叉引用；方案 2 并入 driver Profile（代价：Profile 不承载方法正文）。本包倾向新增方法文件或并入既有交接方法，并按 gate 对包 1 MG-7 的边界（拒绝唯一通道/机械映射）保留“产物是主、消息是路由”。
- **给 gate 的限缩建议**：与包 6 MG-4 同处理——不吸收自主权限与 runtime；只吸收“发布/队列/台账/活性/升级/关闭”的判断。

**平台耦合/依赖**：cloud/Task/store/CLI 是宿主；纪律零耦合。

### 6) 正文草稿与验证方案

```
程序协调纪律（草稿）
1. 协调者不写代码；完成是队列事件；需要 review 的完成变成验证单元；绝不在 drain 里审 diff。
2. brief 是产品：GOAL/SCOPE/CONTEXT/ACCEPTANCE/VERIFY/TIMEBOX/FORBIDDEN/REPORT/STANDING；缺字段拒绝 spawn；依赖项上下文全文 relay，让 worker 不猜。
3. standing orders 逐字随每次 spawn/resume；发现重述就 append。
4. pilot-first：用 1 个 agent 证伪 brief 模板/verify recipe/单元大小，再 fan-out；滚动窗口不用 blocking batch。
5. 验证按单元缩放：便宜命令 worker 跑并抽验；昂贵/高 blast radius 用独立 verifier；台账 key=PR+head SHA，新 head 失效；blocked 不是 pass；CI green 不是 verdict。
6. 活性只读 probe；不 resume 查活性；两次重试后 abandon 并重规划；僵尸先对账再接受。
7. 升级：不可逆/产品偏好/与观察矛盾的指令/程序死路 → 先 park gate 再问并绕开；其余自己处理并记录。
8. 关闭：每个 spawned agent 对账到终态；每个 landed PR 的当前 head 有 verdict；反复纠正编码进 standing orders。
```

验证方案（未执行）：用一个小程序检查 (a) brief 是否字段齐全且依赖上下文已 relay；(b) drain 是否只分类不审 diff；(c) ledger 新 head 是否使旧 verdict 失效；(d) close 是否对账全部 child。边界：不引入 runtime/store；程序规模不足以超出单 agent 时不适用。

---

## 8. 包级综合观察（供 gate，不是裁定）

1. 本包四组是 F（测量/诊断）与 Driver（程序协调）的补面；与包 1–7 合计覆盖本 A2R 线在 A/B/C 主干 + 工程裁决的主要机制。剩余未读基本属 a4（D/E/F 实现、资产、脚本、SDK）。
2. **最高价值单条**：MG-1 的“harness 先证明敏感度再冻结”与“target + 尝试下限 predicate”；MG-4 的“brief 是产品/缺字段拒绝 spawn/standing orders 逐字”。
3. **最高风险**：MG-4 的程序协调含自主与 runtime；按 gate 对包 6 MG-4 的同样标准限缩，不吸收权限与机制。
4. **与 a4 的分工**：profiler/CDP/heap 工具、stack 机制、cloud/store/CLI 全归 a4；本包保留证据与程序判断。
5. **与产品已 defer 内容的一致性**：本包不复活任何 runtime/registry；MG-1 的持续实验按需，不设强制循环。

## 9. 未读残余（本包未覆盖；不假装已评估）

- `why/references/sources/*`、`investigator-prompt.md`；`interrogate/references/code-quality-review.md`；`architect/references/design-red-flags.md` 等（gate 已判“不接受为已吸收能力，B 引用再固定回读”）。
- pstack 余：`typescript-best-practices`、`make-bot-ui`、`automate-me`（已读）、`setup-pstack` 余部、`automations/benny/*`、`references/*`、`scripts/*`。
- cursor-team-kit rules、agents 细节；cursor-sdk、grok-voice、schemas、scripts；docs-canvas/pr-review-canvas 渲染资产；orchestrate scripts/schemas/tests。
- 其余同包 1–7 的残余；均按委托归 a4 或后续轮次。

## 10. 包内自检（机械项，非专业裁定）

- 源 pin 与路径：均为 `ecc249f1e306fc64ddf83c7bed16cacf7c2239db` 下实际存在的路径；
- 未修改产品/他人文档/registry；未 commit；
- 每组含 6 项要求；所有验证方案标注未执行；runtime 内容标注为不吸收。
