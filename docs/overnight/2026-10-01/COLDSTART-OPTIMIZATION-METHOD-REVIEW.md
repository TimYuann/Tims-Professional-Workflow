# Part C · 冷启动优化候选有界方法审核

日期：2026-10-01。Reviewer：`tpw-night-method`。候选作者：`tpw-night-check`；Driver 为本批报告的物理集成者。

**Disposition: RETURN_FOR_BOUNDED_CORRECTION（一次有界修正）；方法审核结果 FAIL。** 不接受候选当前的三项过强/不准确 claim（MC-1…MC-3）。已支持的诊断、已有修复与低成本文档方向保留；不是否定既有 core 接受或要求重审全库。此结果是新候选的设计评价，不是实施验证、优化实施许可或 UCBIP 裁定。

## 精确 candidate identity 与读取边界

- Candidate commit：`c8fed3e642edd0df1ca9942e339e41c6ac564c2c`；root tree：`ea15259d079b5fb7172fc227bbd881af4e84355f`。
- 候选路径：`docs/overnight/2026-10-01/COLDSTART-DSH-VERIFICATION-AND-PLAN.md`；SHA-256：`f022f3a65d7a9c8bd89cabbc898a8550ab145fda50e16256c8f5dabb9b517e16`，从该 commit 取字节独立复算 MATCH。
- Follow-up brief：SHA-256 `90dda07b9a0304d9a6273407d08e6a60e7535915f21c90c5515d5b4bc937cb44`；本任务仅 §C 方法审核及其 §B 的来源/动作边界。
- 原始 prompt：`6831d55616adc123238f78c373e003dc8698f882b22debbf7cee5ce963638dd1`；Owner 转交 feedback：`6e3e6e0f5f2c0b73aaca48f7e2d03c79da8956be915675753da3813e61fd34a7`；解释候选 Oracle analysis：`bc72dd2829ba295e4e4461613589f116c269b45a5fc27fc62f1df4aba934a648`；source note：`5b04c3931ce8fe772a301e5b1da27cedfdf12a6bf422f122768f5c1039946db0`。指定文本均完整读取；Oracle 解释未作为正确答案。
- 历史 TPW：`205b831ecb9ba4e79481a08e6b23f7159dca4113`，root tree `136e0fcda54056bc188b67950a3f32dbfd165319`，core `11e6e3772b6bc0e17259c932b0c0dcabb030a133`。
- 比较 TPW：`29d8b09e416028ad68bc72da23452c6e23755a5a`，root tree `bda41c50198e3c23fbfa881e267beb20a6b7345c`，core `91875114e51855517f92ef099cbdf60c34e68243`。
- 下游测试基线：UCBIP `7fc94e4a483cf6b1d8add214d7dbe9a1d42b7f76`。仅取相关 tracked Git 文档：engineering-method-routing、restart/current-release 控制段、native 卡相关标题、治理的角色/独立关系边界。为核候选已报告的历史→当时 current delta，另读取其具名 `a57db92af75c5feba2cf36d48d46bdbcdcaf9fb5` 的 routing/当前顺序；不把它当审核时的实时状态，更不裁定当前开工。

方法：只读 `git show/rev-parse/diff --name-status` 与文本/hash 核对，必要处按锚点取回。不运行任何 UCBIP checker、测试、服务或脚本，不读取 ignored raw/绑定源/凭据/业务数据，不取新来源。只写本报告，保留用户 `scan.js`；未实施、派工、联系 Owner、调用 Pro、修改 core 或提交。

## Must-fix（限一次返回的修正范围）

### MC-1 · D2 把 `.agent-local` 路径性质直接推成已证实越界

候选 D2/§2 将读 ignored local run-state 判为 **established second boundary stretch**。原 prompt §一允许本地治理读取，§三明确要求定位角色绑定/现行状态并“区分 tracked 文档与本地运行态”，按引用回源；它没有一律禁止 ignored/local 路径。明确禁止的是凭据、用户数据、敏感运行材料及不必要越域读取。

Owner-forwarded feedback §4.G 确实自述访问这些路径；这支持“自报读取了 local runtime”，不自动证明这些具体内容属于被禁敏感材料或越过必要治理回源。没有原始轨迹，候选也承认敏感性未裁定，不能同时把违规升级为 established。Oracle 没标 D2 不等于漏了一个已证实违规。

**所需修正：** 分开活动自述、tracked 不可恢复性、访问授权/敏感性判断。后两者的真实内容/必要性缺证时保留 UNVERIFIED 或具体访问范围疑问，撤回“第二次已证实越界”的无条件定性；不要反过来追认所有 runtime 读取都被允许。该修正不影响 D1 对 checker 自报行为违反原动作禁令的有界判断。

### MC-2 · §3 误称 core 字节不变，且 routing digest 不匹配

候选正确列出 entry already fixed，却紧接着写 “No core/Backbone byte changed between tested and current”。实际 `git diff --name-status 205b831 29d8b09 -- professional-workflow` 仅返回 `M professional-workflow/README.md`；它属于 core，因此 core tree 从 `11e6e377…` 变为 `91875114…`，不是字节不变。

未变的是 Backbone、方法正文等相关语义/文件，不是整个 core：Backbone 两版摘要均为 `ce82a70016a4a3fc234ea287f39aac8d79a260ddf13747c4fb705bda580453ba`。optional example 两版同为 `37335d1c7245e30a10d7c74b8c33a0a74b5c4f7fd3d1c64e7e65f93894a62fce`。

候选 §0/§3 还用 `6963521e…` 标 routing 文件身份。独立取 UCBIP `7fc94e4a` 与其已报告 `a57db92…` 的 `docs/active/engineering-method-routing.md`，两者 SHA-256 均为 `fc0b3942c409b4d4908fa0448502818439091bf8f12f8b4493e1d3f14afbc1ed`；“未变”成立，但这个短摘要不匹配所引固定文件。

**所需修正：** 改成精确的 entry/core tree 字节差分与未受影响语义分离，修正 routing digest 的算法/对象标识。不得用语义覆盖仍有效来声称新 tree/archive 与旧交付字节相同，也不得因这个 pointer/status 差分要求全量证据重跑。

### MC-3 · B1 的因果证据能力过强，B5 被挂到不必要的取证前置

B1 声称取得单份原始 trace 就能知道 D1/D2/D3 是 one-off 或 reproducible，并规定没有 trace 就不加任何机制；B5 又标为 after B1。一次 trace 能确认当次动作及读取顺序，不能证明复现率或把模型/文档/harness 因果分离。候选自己的 single sample/no control group residual 与该 intended result 不相容。

D3 的“反馈错误称停驻线当前可设计”已可由反馈及 `7fc94e4a` 的有效控制文本判断：06:04Z 现行顺序明确 native SSE/UID/TIM 停驻。保留对原因的未知，不妨碍提出一条有来源的当前控制提示，也不必让缺失 raw 阻断 B2/B3 已实测的文档歧义修正。这种前置会让证据澄清成为新 gate，反而违背最小 batch 目标。

**所需修正：** B1 限为可得时核实当次轨迹/执行/访问，不许推出普遍根因或复现性；与已有文本证据支持的文档候选解耦。B5 的一句话仍可列 suggestion，明确按有效下游 authority 的现行控制解释，而不是“时间戳最新的一行天然拥有更大权力”。仍不得重跑禁止命令、联系 Owner 补授权或搭权限平台。

## 已支持的审核面与 conditions

| 审核面 | 结论/范围 |
| --- | --- |
| 因果诊断 | D1 的自报动作与禁止生成器/checker 的委托不相容；实际运行/副作用仍未证。D3 源文本支持误选历史授权为当前可做动作。不能由单样本推模型、harness、骨架无效或日常工作必然过重。D2 按 MC-1 降级。 |
| 责任/authority | TPW 拥有自己的入口/方法/optional 文本；UCBIP 有效治理拥有任务激活、映射、工作优先级与接受/关闭。新候选没有真实权力重开 native、更新 UCBIP routing 或声称三个方法替代四个；这一边界保持。 |
| 历史/当前比较 | D6 正确把根入口 README 的已修复与 sub-README 的 remaining 分开；D8 optional 文件仍有 repo qualifier 歧义。D9 坏 disposition 名在测试对象已修，不应重复报。当前 UCBIP 排序不同不追溯美化旧测试，也不代表现在获准开工。MC-2 校正 exact identities。 |
| 选择性失效 | D4/原 blanket byte invalidation 不由 Backbone 支持；冻结基线与 `cf107522:M6-FINAL-ACCEPTANCE.md` 均只处理受影响结论。旧 mapping/源指针状态补充不撤销未变 M3/M5/M6 的既有覆盖；新对象身份仍须诚实记录。 |
| 独立关系 | D5 不支持“每个边界固定两个主体/所有卡作者永久不可评审”。但其“hard rule is only implementer”措辞也应避免把设计作者贡献忽略：按确切被评对象的真实贡献判断，实质代做方案者同样不能包装为独立挑战。 |

以上是新候选方法 claim 的评价，不重审方法全文、源吸收比例、全库历史或 UCBIP 当下治理资格。

## B1–B5 必要性、owner 与最小落点

| 提案 | disposition / owner / condition |
| --- | --- |
| B1 raw evidence clarification | **可选取证支线，按 MC-3 修正。** Driver/Oracle 若已有可得轨迹，可按既有访问许可取回并在现有 evidence note 记录，不能以本审核新召回 Owner 或读取敏感运行材料。缺 raw 时保留限度，不新增引擎或全体停止前置。 |
| B2 状态指针 | **有据、低优先级 suggestion。** TPW 文档 owner/集成者在后续获准的小改批选择一个最短路线；当前根 README 已明确历史 M1–M5 非当前接受，因而无需再造状态源。若 sub-entry 独读仍混淆，可在它们加回根入口的短指针；不写第二套 acceptance 值。只核 pointer、历史标签与既有接受对象一致性，不重走所有专业方法。 |
| B3 仓库限定指针 | **有据、最小 suggestion。** TPW optional note owner 可在后续授权中补 repo+pin，UCBIP 文档/权限不由 TPW 改。validation 必须按引用类型区分：tracked path 可核 pinned commit；ignored raw/binding 只能核其明确标记为 local point-in-time 的 locator/限制，不能要求它“在 pinned commit 存在”。原 proposal 的 every path at pinned commit 条件需据此限缩，不为缺 Git raw 新造归档/复制。 |
| B4 覆盖声明/下游映射 | **TPW factual coverage note 可选；下游采用决定 deferred。** 三份真实正文与四个旧 routing 名的缺口成立，尤其真实系统 drive-preview 无当前完整替代。可在现有 methods entry 或 optional note选一个位置列准确边界，不复活旧名/增加来源/造映射表。UCBIP 有效 owner 决定实质替代、保留或其他来源，TIM reviewer 不接管。这里“method-owner (C)”应理解为本 Part C 的方法判断职责，不能误指 Domain Semantics C；仅新方法/等价性语义需判断，列三份文件的机械事实不另建常驻审查门。 |
| B5 当前控制提示 | **有据的单句 suggestion，按 MC-3 去掉 B1 gate。** TPW 冷启动 prompt owner 可在以后被批准的测试输入中要求先读回有效现行停驻/顺序，将历史授权单列；保持讨论任务与可派工任务分离。对同一固定输入一次有限 cold-read 可辨别改善，结果不足就保留，不自动加门/复测无限轮或改 UCBIP 优先级。 |

建议下一批若获明确实施授权，可把 B2/B3/B4 的实际重复内容合并到最少入口位置，B5 仍只是一句测试输入澄清；这些是建议，不是当前派单。无需源吸收、新 runtime enforcement、validator/composer、role matrix、永续 trace checklist 或第3笔 Pro。

**新 bytes 的条件：** “docs-only / no semantic change”可支持不重审未变 claim，不意味着沿用旧 source commit/tree/manifest/archive digest 标记新产物，也不天然授予 main/publishing 权限。本批只写 reports，优化产品的权限仍缺。后续若真的改 pointer/status，记录新对象并复核改变的引用/状态解释即可；何种接受动作由既有委托决定，不从“no re-acceptance”一句创设豁免。

## Residuals 与一次返回后的 stop

- 无 DSH 原执行轨迹/模型/独立身份取证，运行/副作用、访问内容、普遍因果与实际成本依然 UNVERIFIED；feedback 只是完整 Owner-forwarded 自述。
- 本轮不读取 `.agent-local` raw/binding、不验证它们可用性，不把 ignored 不可从 Git 取回当作敏感或违规的充分条件。
- 当时 current UCBIP 的排序变化仅按候选已引用的固定 `a57db92…` 文档核对；不评审现在状态，不提出下游开工建议。
- 没有实际优化冷启动可靠性的对照运行；本审核只能判断 proposed changes 是否相称、可核和不增加 ceremony，不能给改善效果 PASS。
- 既有 TIM core/PW-01/M6 接受及未变覆盖不因本报告失败撤销；本报告只拒绝该新候选的 MC-1…MC-3 claim。

Driver 可将 MC-1…MC-3 与表中的验证限缩一次返回原候选作者作有界报告修正；method 不派新实例、不实施机制。后续只核这些受影响差分/必要条件，不扩大设计空间、不因换 SHA 重开无穷轮；若仍有实质分歧，记录给已指定的接受责任，不自动起第3笔 Pro或新设计环。

## 一次有界修正后的差分确认 · 2026-10-01

新固定对象：commit `19df06c57d68547b27fd00e4fdd92040353d17bb`，同一候选路径，SHA-256 `cfe82d2d370148fe0961ab981f70f0b7c4b0d935255ffcdf46680a26087e2ccf`，实测 MATCH。只读其相对 `c8fed3e642edd0df1ca9942e339e41c6ac564c2c` 的指定差分；原审核与 FAIL 记录保留。

**Disposition: PASS（受影响方法 claim 已修正；原 conditions/residuals 继续适用）。** MC-1：D2 及解释段撤回已证实越界，分开活动自述与 scope/sensitivity UNVERIFIED，不追认所有 runtime 读取合法。MC-2：明确 core README 改动与 `11e6e377…→91875114…` 的不同字节身份，未变语义按原覆盖保留；routing 区分 content SHA-256 `fc0b3942c409b4d4908fa0448502818439091bf8f12f8b4493e1d3f14afbc1ed` 与 Git blob `6963521e…`，两种标识均从其所指两版 UCBIP Git 对象独立核对一致。MC-3：B1 限为可得时核当次轨迹，不再证明复现率/根因或作为文档修正前置；B5 改读有效 authority 的当前控制而非时间戳优先，并限一次样本。

B3 已分 tracked 与 ignored locator 的验证，未新造 raw 归档要求；B4 明确 Part C 方法判断不等于 Domain C，机械文件列举不设 gate，下游映射仍归 UCBIP；D5 按被评价对象实质贡献判断独立性。未发现这次差分新增 blocker，不再返回设计环。后续若获准落地仍须诚实固定新 bytes/引用并遵守原授权边界；未实施的可靠性改善、raw/副作用及模型因果仍未验证。本确认不是产品接受、优化开工许可或 UCBIP 决策；只追加本节，未改候选、提交或实施。
