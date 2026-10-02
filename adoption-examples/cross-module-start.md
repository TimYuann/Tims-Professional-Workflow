# 跨模块启动例 · 小修复与跨模块新承诺

State: **非规范示例，位于 core 之外。** 不授予权限，不构成固定流程，不证明真实项目结果。两个例子只说明：从固定包版本选判断、绑方法、填最小实例、装配启动文本，以及何时召回/升级。角色、对象、路径、命令都是可替换示例。

读取约定：方法路径相对 `professional-workflow/` 包根；接入时先在固定版本内确认文件存在与当前 claim（`methods/README.md` 与包内文件），再绑定。方法不在该版本就采用该版本已有合适依据，或明确未绑定；不伪绑、不用退役旧名（`path-trace`/`blast-radius`/`design-compare`/`drive-preview`）替代，也不造等价名。示例不复制 digest，真实任务绑当前固定对象。

## 例 1 · 局部缺陷修复（最少实例）

情境：某模块一个已知缺陷；已有行为契约（输入/输出/错误语义）与一次可复现失败；本次只修这个缺陷，不动接口。

缺的判断：E 实现；F 对修好后的固定版本身份评价缺陷修复 claim。

绑定：
- Profile：`profiles/implementation.md`（E）；
- 方法：`methods/local-defect-feedback-loop.md`（复现、因果修复、回归检查）；F 对固定版本评价缺陷修复 claim——本例有可复现失败，适用 `methods/behavior-claim-evaluation.md` 的 baseline/treatment 比较条件（已复现缺陷可作 baseline）。该方法只覆盖其适用范围内的比较型 claim，不是所有 claim 的通用入口；
- 任务输入：行为契约的固定版本 + 失败观察（命令/输入/输出），都可复现。

```sh
cat profiles/implementation.md \
    charters/<filled-fix-charter>.md \
    methods/local-defect-feedback-loop.md \
    path/to/task-input.md
```

最少实例：一个 E 实例 + 一个独立 F 实例（独立性由真实委托声明；E 自测只作 F 的可核对输入）。不要求先做 Plan：局部改动可引用已有契约，加一段本次差分与委托范围即可。

交付与证据：patch + 自测命令与观察 + 回归覆盖；F 给出三态结论（PASS/FAIL/UNVERIFIED）、覆盖范围与限制。三态是 F 的结论纪律，不必须经过比较方法；本例有可复现失败才适用 `behavior-claim-evaluation.md`，其他 claim 按接受依据与适当验证设计。局部通过不等于发布/部署许可。

召回/升级：契约缺失、矛盾或无法在委托范围内保持 → 记录受影响对象、事实与影响，停止依赖它的工作，由 Driver 路由到拥有该边界的责任方；只有人类保留决定才经 Voice。

## 例 2 · 跨模块新承诺（Plan handoff + 证据记录）

情境：新增跨模块的可观察承诺（例如 snapshot/freshness 跨页面生命周期与消费边界）。B/C 语义已有接受依据；D 给出可依赖的安排，E 在委托空间内实现，F 评价固定结果。

缺的判断：D 规划（coordination surface 与 implementation interior 分开）、E 按切片实现、F 评价固定改动与其中的具体 claim。

绑定（按本任务实际需要，不是固定流水线）：
- Profile：`profiles/technical-planning.md`（D 出 Plan）、`profiles/implementation.md`（E）、`profiles/evidence-evaluation.md`（F）；
- 方法：`methods/cross-module-design.md`（D：接口事实、seam、Plan）、`methods/change-slicing.md`（E：每个切片有可独立演示/验证的结果）、`methods/change-review.md`（F：固定对象与意图、观察到哪一层）；某个具体 claim 适用 baseline/treatment 比较时再按需绑 `methods/behavior-claim-evaluation.md`，它不覆盖所有 claim；
- Plan/切片跨会话或跨实例交接时，按该版本实际存在的方法（如 `methods/handoff-and-resume.md`）处理：交接物按引用不按复制，携带 claim 与证据事实；
- 任务输入：接受的行为/领域承诺（带版本与决定人）+ 当前系统事实 + 固定的代码范围。

D 实例的启动文本（E/F 各自有自己的 Charter 与启动文本：E 绑 `change-slicing.md`，F 绑 `change-review.md`，具体 claim 适用比较时再加 `behavior-claim-evaluation.md`，不复用这一份）：

```sh
cat profiles/technical-planning.md \
    authority/RESPONSIBILITY-BACKBONE.md \
    charters/<filled-planning-charter>.md \
    methods/cross-module-design.md \
    path/to/task-input.md
```

Plan handoff：D 交出的 Plan 至少写 Commitments / Delegated Decisions / Recall Conditions；E 只在委托空间内实现，切片按“完成时能独立演示/验证什么”切，不把层完成当行为完成。F 先固定审查对象（commit/范围/fixed point）与意图来源再评；审查建议不构成接受，也不授权合并。

证据记录：每个结论携带 claim 与对象版本、实际执行了什么、覆盖范围与限制、真实贡献，以及三态结论（PASS/FAIL/UNVERIFIED）。详细证据判断在方法正文：F 的报告按 `methods/change-review.md` 写明观察到哪一层、哪部分未证；交接时来源标签（如 `handoff-and-resume.md` 中列举的标签）只作非穷尽参考，不要求必选或按固定阶梯上升。用合成/夹具还是真实 leg 由 claim 与该任务的有效授权决定，本示例不预设；只读检查的“不写/不联网”不是产品政策。

召回/升级：事实推翻承诺 → 回 B/C；接口/约束/验证依据要变 → 回 D；超出委托或触碰保留决定 → Driver 路由，人类保留决定经 Voice；实现者不能自行接受上游变更。

以上实例数、是否先做 Plan、是否拆分 F、是否交接都由真实任务决定；行为结论由 F 给三态，比较方法只在适用时使用，其他 claim 按接受依据与适当验证设计。这里只展示最少实例与召回/升级路径，不是流程模板或授权。
