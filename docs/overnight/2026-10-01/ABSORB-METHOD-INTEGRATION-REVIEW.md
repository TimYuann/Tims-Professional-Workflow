# Phase 1 · 修正草案与方法集成预稿独立评审

日期：2026-10-01。Reviewer：`tpw-night-method`；非 B/A1/修正草案/集成预稿作者。容量中断前的读取与核验在同一会话保留，本报告完成同一固定评审，不重开调查。

**Disposition: RETURN（静态方法结果 FAIL；FM-1…FM-3 已关闭，剩余一项集成适用边界 must-fix IM-1）。** 已支持的修正、例子与两-guide 结构保留。拒绝的是把本批演练限制泛化成真实任务通用 raw 条件，不是要求重做骨架/全源评估，也不是否定未运行的自拟例子。报告不接受 core、不授予实施/发布权限。

## 固定 identity / 读取范围

Commit：`8769eb44eefa679229e788442c4960087b53c0a4`；tree：`289bf8cb90be0ed6ef6ac46ca462683727287db7`。从该 commit 取得 exact bytes 并复算：

| 对象 | SHA-256 |
| --- | --- |
| ABSORB-CANDIDATE-METHOD-INTEGRATION.md | `922f3a675f7f3a939d20a3a29f24d74c666d320a155ef21ee4ba9461ee1c6a0a` |
| ABSORB-DRAFT-DBG-05-EVIDENCE.md | `40d0213f97d01a4f23362407731a850dc8ab2bb12dbf5346166019d9c757a8a1` |
| ABSORB-DRAFT-DBG-16-MOCK-ADAPTER.md | `73fdb667b8fcf54b3bee039a41a4f9d6ae36a14ffb6bb5d4ab2ac793b33413d9` |
| ABSORB-B-ADJUDICATION.md | `0273139ab601af8655ee2012dfe94462234102855df1806645c5b8fe381bbe8e` |
| ABSORB-B-CALIBRATION.md | `aacef47ff4fa884ae4595072bfef99d9a1a30e438c19bbdcc4946c1e4b388bcf` |
| ABSORB-B-MECHANISM-COVERAGE.tsv | `d297e935d084176bc83a5304087aa54f5fd587c4e8df9f3007036c2b832a94a6` |
| ABSORB-A1-ADDY-INDEX.tsv | `abef7e2a7d173f951e595dec6891a024ba450772974d2329dc85f3b9c8ed62a3` |
| ABSORB-A1-ADDY-HEADER.md | `284ccb68e65122adb8a6d902944abdc01943018361781b02601842e0f02da0ab` |

上下文：FULL-CORRECTION-BRIEF 摘要 `4fc335e42f50f0a777251491eee476382c966d68c4b8fd3add4ff7edc176bf36`，重点 §§2–3；原 FOLLOWUP-REVIEW `db8b2225e3b7280f61ba330ef9e6da3724e985a80d21850656ed1d056640c351` 的 FM-1…3。完整读取177行预稿、两份修正草案及受影响 diff；静态解析 B adopt 标签、DES-14 basis 和 A1 /ship 行。上游只回必要固定源锚（本会话此前已核的六份 DBG 源不因 metadata 改 hash 重审），另直接核 Addy `.claude/commands/ship.md` 的 Rules。

命令为 `git show/rev-parse`、限定 `git diff 5cd2b8e 8769eb44`、Python text/TSV/hash 解析；用 Python 解析自拟JSON fixture，仅核扁平字段缺失、嵌套字段1200这一静态事实，不运行 adapter/test。未读无关上游、跑 UCBIP/网络/支付/服务或实施示例。此 commit core 仍为 `91875114e51855517f92ef099cbdf60c34e68243`，Backbone 未变。

## 原返回条件：实质关闭

| 条件 | 判断与范围 |
| --- | --- |
| **FM-1** | adopt 首R标签独立重算为 R0=24/R1=8/R2=7，B正文/修订记录同步；DES-14 current_text_basis 撤回“相反默认”，明确兼容是条件偏好、操作差异不是现有禁止删除。仅对这些差分关闭，不背书剩余183行真实性。 |
| **A1 /ship** | 新行补全 Rules 5 的三条件必须同时成立：≤2文件、diff<50行、不触及auth/payments/data access/config-env；非平凡blast radius仍需要review。与固定pin `2686b620fc1fed2e8f60c704839c766b8594c6b6` 的实际Rules一致。它仍是上游机制记录，不成为本 core 的新扇出gate。 |
| **FM-2** | 默认例子仅读取已获准的最小脱敏记录，不先保存原始headers/body；危险先写盘路线明确为错误。env只保护命令文本、不等于保护响应；401/realm不推具体token拒绝原因，错误码/另行授权探针另有依据。step只提示等待，正确撤回技术屏蔽回显。原问题关闭；通用raw适用边界另见IM-1。 |
| **FM-3** | 自拟fixture明确nested `data.unit_price_cents=1200`，错误flat字段不存在，且场景明确错误实现将缺值当0；若只用返回领域对象的in-memory adapter，解析路径不执行。对应adapter契约观察能够暴露这个目标缺陷，而非再用port-green冒充transport正确。例子在逻辑上可证伪，但未执行真实/合成adapter，不能标运行PASS。 |
| **mock / replace 限缩** | 进程内内部协作者与跨网络port替代分开，不再“拥有即永不mock”；DB/FS sometimes、stand-in存在条件、内部seam不因测试暴露均保留。旧测试替换只在覆盖对应accepted claim且已有删除授权时成立，不成为always-delete政策。 |

## Must-fix IM-1 · 本批演练边界被写入通用方法规则

位置：预稿§1.1的插入句、§2.1 redacted guide Rules 4／Raw branch；DBG-05修正草案§1.4/DBG-05.4。它们对“任何需要raw”的使用同时要求 **no real-user data、no live network calls**，并作为须全部满足的通用条件，而guide的Use是一般 defect-feedback/behavior-claim evidence任务。

FULL-CORRECTION-BRIEF §2 的原授权是 **examples** 用工作区、无真实凭据/用户/网络；§quality允许两个纯本地演示。固定verify-this L51提供敏感工件默认最小行内、有效同意后可保存的边界，没有规定真实工程所有raw任务必须无活网络或真实用户数据。作者已标这五条件为 authored，避免假源归属，但 authored 标签不能消除它对通用适用性和既有任务授权的影响。

因此目前会把一项合法、已有有效访问/保存许可及保管约束的真实任务，仅因为其涉及真实用户/已授权网络采集，推为永远不能走该guide的raw分支。知识补丁不应替有效policy/Charter决定这种全局保留边界；“creates no gate/authority”的声明也不能代替规则本身的范围说明。

**有限解决条件：** 将无真实用户/活网络等限制明确限定为本批示例/演示或一个明确标注的offline模式；通用知识保留先脱敏、最小信号、保存敏感工件需已有有效同意、受限保管与清理、不得自我扩权。真实任务的访问/数据/网络限制继承其有效policy和Charter，不由guide新授予，也不由guide无条件取消；硬约束与秘密保护仍保持。既有有效授权可继承，不每步重问Owner。

这只修raw支线适用语义与相应插入句，不要求扩大本批演示权限、读取真实数据、运行网络、改变Backbone或研究整个隐私制度。我不代写候选；IM-1由原作者/集成者在已授权纠错scope处理并记录。

## 集成设计与实际消费入口

| 新claim | 方法判断 |
| --- | --- |
| 三份方法只补已证缺口 | 支持。local-defect Method5与F Method2是证据形式/保管的同一增量；cross-module Method3是已有依赖分类的mock/adapter操作展开。未改三态、独立性、兼容接受权、删测试条件或其余正文。IM-1之外无需扩展三方法范围。 |
| guide≤2且按需 | 支持结构。预稿只有redacted与mock-adapter两份完整候选，入口表按support need选择，未把146候选、183统计、R标签或完整120行审计内联入默认startup。指南不是新Role/runtime/validator/composer，也没有复活四个旧方法名。 |
| 来源/自拟区分 | 支持。每份guide正文包含完整相应pin，表列repo-relative源path及chapter/function锚；源规则、范围协调/coverage inference与整体自拟例子分开。没有把自拟adapter案例或五条件冒称原源。IM-1仍是适用边界问题，不是pin错误。 |
| Charter task-local | 支持设计层。methods/README的support表和末句明确任务Charter绑定适用性、独立性与动作许可；未来可把必要guide列在既有Applicable methods并与主方法一起消费，不需新字段/新装配器。当前只是未来路径/候选正文，不能称这些文件已可cat或实际冷启动完成。 |
| 工程例子分辨力 | 静态成立且有明确限度。脱敏例比较相同diagnostic signal下的safe form与unsafe persistence；adapter例比较green port测试与未执行的错误parser，正确观察面改变了会被执行的代码。实际sentinel/adapter演示未运行，现实效果仍未验证，不因“true failing case”标题升级为实测失败。 |

## Suggestions（不单独阻断）

1. 主方法插入可先短述必要规则，再把复杂raw/HITL/adapter选面指向guide；不要把“apply guide”解释成每个无敏感输出的小任务必须装入两份全文。入口宜明确“需要该支线时把对应guide加入本次既有绑定/读取范围”，保持按需，不另设mandatory loading gate。
2. “normalize below the port”空间词有歧义。应以哪段真实normalization被哪条测试调用说明边界；把逻辑移到仍被替换掉的adapter并不会改变覆盖。首选adapter契约观察路径已正确，不需要重开整个ports设计。
3. 两adapter规则来自源的seam纪律，可保留为避免无用间接层的设计依据；不要为满足数量而制造第二实现或对所有既有port作自动否决。当前“不mandatory port/framework”限度继续保留。
4. A1 /ship uncertainties仍有“四条Rules”的旧计数文字，而现在引用了五条Rules；三项跳过条件已经正确，属说明性更正，不触发新全审。
5. 本次阶段metadata（candidate/status/guide行数约数/格式）不影响未变语义评价；真正集成后核实际files/path/source绑定与改变的claim即可。别把这些hash变化拆成一串新审核门。

## Residuals / 后续独立边界

此报告仅评固定预稿与指定差分；未重新评全库/全A表/全部未读B机制，未读面依然provisional。原source、core和M3未变覆盖保留各自固定范围；新guide字节尚未成为active/core接受对象。

没有运行脱敏sentinel或实际adapter反例，也没有fresh-reader消费观察，因此不能给实际使用可靠性或coldstart PASS。它们若用来关闭后续新claim，应有独立、固定、纯本地的相称证据，不成为泛化测试框架或循环审批；method维持评价者身份，不实现被评正文/fixture。

只写本报告，未编辑草案/A/B/core/上游，未提交、派工或跑UCBIP。IM-1是当前scope内真实适用性差分；不把它升级为新广泛研究。下批直接看实际固定集成结果/受影响新claim与必要观察，纯metadata不重开全面评审；额外同Pro对话复查仍按既定条件由Oracle在对象和独立检查固定后处理。
