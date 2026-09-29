# TIM · 0930 Oracle → Driver 交接

> 给独立会话 `tpw-0930-driver`。本文件记录 Owner 在当前对话中明确的目标与约束，并给出接手顺序。它不是已冻结的 A4 或 A5；历史研究里的候选也不因写在这里就变成 Owner 裁定。

## 目标与本库边界

Owner 要的是一套可复制进**任何项目**并启动的 multi-agent 工程工作流。核心价值是可迁移的开发经验与规范纪律：环节顺序、进入每环节所需材料、角色该怎么判断、应产出哪些字段、产物如何被下一环消费，以及失败和交接的路径。它会持续吸收上游仓库更新及新的工程文章，按已核实的机制更新 `roles/`、`skills/`、`workflow/registry.yaml` 和必要脚本。

TIM 定义逻辑控制语义，不替下游运行环境设进程、队列、WIP、资源锁、并发上限或具体工具。Driver 必须实时感知所在环境能做什么，再选择执行手段；本库只规定工程上要完成什么、凭什么认为足够、何时退回或交付。

## Owner 已表达的方向，尚待与现有契约逐条对齐

1. **按角色与现场能力 fallback。** 优先独立且 Owner 可见的会话；不具备时看能否用可互通的子代理；再不行由同一会话承担。不能把三种形态硬编码为全局档位。Voice 最好直接与 Owner 访谈；如果子代理不能直接与 Owner 沟通，Driver 自己承担 Voice 职能可能比做消息转发更好；某些子代理可被 Owner 直接对话，须按现场能力判断。
2. **审查／验证缺独立会话时不假装独立，也不默认硬阻塞。** 进入 review/verify 时只需一次 Owner gate：提供可复制粘贴的独立审查／验证启动 prompt，尽量降低 Owner 转发材料与结果的劳动。如果得不到配合，单会话仍按相关规则自审、自验，交付时明确标注“未经独立复核”，继续交付；不要反复向 Owner 索取许可。**独立性与实际验证结果是两轴**：自验若真实跑出满足判据的观察，可以在标明自验的同时给功能验证 `PASS`；环境故障或根本跑不到仍是 `UNVERIFIED`，这次 Owner gate 不等于批准放行未经验证的产品。现行 `AGENTS.md` 的“提出候选的人不得给候选下结论，任何档位不放宽”与此有条文冲突；必须显式仲裁并更新唯一真源及对应角色／阶段表述，不能通过改松检查器掩盖。
3. **完整清点机制来源。** 三仓里的高价值方法不只在 `SKILL.md`，也在 playbooks、references、docs、commands、hooks、evals 等载体。先清点实际范围，读正文后才能判断吸收或拒绝。Matt 的 `in-progress` 九项是上游公开 beta、未进插件；目前没有正式处置，不等于已拒绝或已吸收。它们至少要在完整清单中可见，并区分“已发现”“已读”“已裁定”。
4. **文章是独立来源，可与上游技能交叉。** Owner 指定 poteto 两篇 pstack 长文进入来源体系，后续还会有 Matt Pocock 文章。`72d2b16` 已引入 `article_sources`、`sources/articles/` 与来源检查，补进验证 CLI 可用性、调用者教程和 A5 预期证据；`docs/history/source-intake/2026-09-30-poteto-pstack-articles.md` 保存 26 项机制的基线对照。原始 X 正文未直接读到，镜像缓存可复查，逐字一致性仍未验证。

这些是 Owner 的目标或已接受的方向，**不是说库内相关条文已经全部改完**。尤其第 1–3 项仍要与 09/30 的研究材料逐项对账。不要把 `SYNTHESIS.md` 的 advisory 切片当可直接执行的 A5。

## 当前工作区事实（接手后重核）

- `workflow/registry.yaml` 是机器可读的语义真源；`workflow/phases/`、`workflow/ribbons/`、`docs/artifacts.md` 由 `scripts/render.py` 生成，勿手改。`upstreams/` 只读。`A9` 台账只追加。
- 本交接写下时：`main` HEAD `72d2b16`，比 `origin/main` 超前 2 个提交；另有 8 个 09/30 推演／重扫／汇总／Herdr 调研文件已暂存，是旧会话交付，须保留。先核 `git status`，别把它们当成你的改动或自动提交。
- 最近实跑：`render.py --check`、`check-consistency.py` 7/7、`compose-role.py --check` 通过；`check-closure.py` 20/21，唯一 FAIL 为 C1：当前 commit 没有 release tag。不要为消掉它擅自打 tag，也不要把环境或发布状态说成结构已全绿。
- `docs/history/derivation-0930/DERIVATION.md`、`UPSTREAM-RESCAN.md` 和 `SYNTHESIS.md` 是来源调查、条文推演与交叉候选。原沟通报告在忽略的 `.pi/handoff/COMMUNICATOR-REPORT.md`，可读但不宜作为唯一持久依据。原文所谓“18 条一条未裁”是写作时快照；Owner 随后的回答已改变若干问题的状态，需重新建对照表。

## 你应如何推进

1. **先冷读而不改库。** 读本文件、`AGENTS.md`、`README.md`、`workflow/registry.yaml`、上述三份研究及 8 个暂存文件；重核当前 Git。用自己的话写出 Owner 目标、现有机制、可直接实施项、仍须 Owner 裁的产品选择。明确事实／推断／建议。
2. **先对账，再定契约。** 把 18 条旧清单映射到 Owner 上面已给的回答，指出哪些已足够明确、哪些只定了原则未定操作判据、哪些仍未回答。决策写进本仓现有 owner 文档或追加台账；不要回写历史报告冒充原稿已知。涉及语义时先改 `workflow/registry.yaml`，再 render 派生视图。
3. **组你的独立团队。** 你是 Driver，不要把所有调查、实现和独立裁决揽在一个会话里。优先用 Herdr 起独立 Pi 会话，worker 之间用 Pi Intercom 传递短消息和持久产物指针；起会话前用 `scripts/compose-role.py <角色>` 装配角色，不把裸角色文件当完整 prompt。候选作者与独立评价者分开；Owner 已允许的单会话 fallback 应作为显式降级规则设计，并标注保证程度。
4. **模型纪律。** 你及所有 worker 都用 `--provider minimax-cn --model MiniMax-M3.1-Flash-Preview --thinking high`。每个 worker 的 Herdr agent 名、Pi `--name` 和 Intercom 寻址名保持一致，从 live roster 取真实 ID，不靠 pane 顺序或短前缀猜。新 worker 用 `tpw-0930-<role>-b` 一类唯一名称；不要误接另一个项目的同名会话。先验证一次相互通信与完整任务上下文能传到。
5. **按最小可独立验证的片实施。** 先处理本轮最有根据的缺口：按角色 fallback、独立审查的低摩擦 Owner gate、完整上游机制清点及其来源状态。对逻辑控制与 runtime 的归属有争议时列出具体机制和两种后果，向 Oracle 汇总后再请 Owner 裁。检查项只能保护能给红例、合法变体和维护人的真实断言，不为变绿削弱。
6. **交付与检查。** 每次改动检查真实 diff，按需重跑 `render.py`、`check-closure.py`、`check-consistency.py`、`compose-role.py --check`。验证结果只用 PASS／FAIL／UNVERIFIED，记录 C1 的发布状态边界。只 stage 自己片的文件；本地 commit 按项目流程，push、tag、merge、改历史及发布需 Owner 明示授权。

## 与 Oracle 的沟通

Oracle 是当前 Codex 会话；它**不是 Pi Intercom endpoint**。你的 worker 之间用 Intercom，向 Oracle 则在你的 pane 给出标题为 `【ORACLE REPORT】` 的短报告，并在 `docs/history/handoff/` 留能冷读的指针；Oracle 从 Herdr 读取和回应。报告按**里程碑**或真实阻塞发：完成状态与决定对账、冻结契约前、独立挑战／验证结束后，或遇到无法自行消解的 Owner 产品取舍。不要每次工具调用后汇报，也不要等所有工作停下才上报。每份报告只写：已变事实、证据位置、当前 PASS／FAIL／UNVERIFIED、下一步、需 Oracle／Owner 回答的最少问题。

你可自主开展已授权且可逆的调查、实现和验证。需要 Owner 决定的问题先写清选项与代价，批量交 Oracle；不要把未答复当同意。Oracle 会帮你争取答案并守住项目目标，不接管你的微观派工。
