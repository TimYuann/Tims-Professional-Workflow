# Pro 返回后 · 受影响 claim 与两份草案静态复核

2026-10-01。Reviewer：`tpw-night-method`，非 A2/B/两份草案作者；此前质疑和建议没有代写这些对象。

**Disposition: RETURN（静态结果 FAIL；未关闭项记录为里程碑问题，不开启新返修环）。** 大部分纠错成立，A accounting 与候选发现价值保留；三项 must-fix 尚在（FM-1…FM-3），因此不能把本批当作全部纠错关闭或两份草案已具备采纳资格。此结果不撤销现行 core，不实施、不派工，不授予 landing。

## 精确 candidate identity

Commit：`5cd2b8e39b5e25f6aa4ffe1107a01d54a45a0235`；tree：`e788187ad9ed64b633b1ac94bb72dc78a80fa4c9`。指定摘要从该 commit 复算，全部 MATCH：

| 固定对象 | SHA-256 |
| --- | --- |
| ABSORB-B-CALIBRATION.md | `aa07e94737a4f6786c6c896b53822a29c6d7cb44fc0661f33c32789d8de1e439` |
| ABSORB-B-MECHANISM-COVERAGE.tsv | `78351a351ce8615a9a1a6c00c9cf6ac2d237a09923208c1312c4257f9bafc082` |
| ABSORB-B-ADJUDICATION.md | `a456b032df63efbe9704fdafcd17c0784e9ac055edeb530145c424b59a75bc59` |
| ABSORB-A2-CURSOR-INDEX.tsv | `1ee869541be45dbb09ce1f463d11956b7a8920446620f8744c0d55cb85f00c71` |
| ABSORB-A2-CURSOR-HEADER.md | `c1ae2a73cbe77a498c927a646f12e24c4ee9f3b0c733129ca07a2938cf8ed961` |
| ABSORB-DRAFT-DBG-05-EVIDENCE.md | `e162d967eba80b5a55db89a8457ea627e8025c3be2db388e6f444775968bb867` |
| ABSORB-DRAFT-DBG-16-MOCK-ADAPTER.md | `81cebd63a2554d2c9fd6b92d55d7cf44f829db9ebc47ba82955d2b424819e43f` |

先读 Pro RESPONSE（`9aa4af3777b2063fe0fca8a5d2e62fd28d0a9794252ac00de7aa1ea514858569`）、DISPOSITION（`fa9d8b073a29909edac86409e16e0a670796378377ca628ddc558c9776d3b9f0`）和原 method check（`7e73c366eb671455f5a7ea1d56b7792988523ef49ae23cf4a402cd7aa94b2444`）。用 `git show`/限定 `git diff 0c6b11c 5cd2b8e`、Python TSV/text/hash 解析核受影响条款/计数，未重审全183机制、全146候选或1240源内容。

两草案完整读取；只读固定源必要正文/章节：Matt ADR-FORMAT、CONTEXT-FORMAT/domain-modeling、ADR0001、diagnosing-bugs Redact/loop 出口、HITL 脚本、mocking、codebase-design Principles/testability、DEEPENING；Cursor verify-this、encode-lessons、cursor-sdk 起始正文；Addy ADR 相关段。没有执行其中脚本/示例、curl、支付、测试或服务。现行 core subtree 仍为 `91875114e51855517f92ef099cbdf60c34e68243`。

## 已关闭的纠错 / MCAL 对照

| 对象 | 静态复核结果 |
| --- | --- |
| AUTH-27 / BHV-10 | **源方向已修正。** Matt ADR 默认标题＋1–3句、可选章节及三条件，与固定 ADR-FORMAT 相符；Addy 默认字段单列且保留既有约定优先。CONTEXT 恢复 glossary-only 与不放规格/实现决定，区分载体和建模活动。仍是记录操作候选，不因缺某模板否认现有 Voice/Charter。 |
| A2 orchestrate | **指定来源错误关闭。** cursor-sdk 主体在 pin 内，实测 blob `bb070b338da14aa5d0847e793f6f364f25a751c3`；纠正行区分 repo 存在与宿主安装/加载未验证。额外 helper/跨插件定位改动仍是引用事实，不产生工具权限。 |
| DES-23 / ORC-07 / AUTH-07 / BHV-08 / AUTH-04 | **主要对象纠错关闭。** DES-23 不再把增量可编译写成已采用默认；顾问操作与独立性规则分开；AUTH-07 不再挂 ADR0001；BHV-08 保留现有决定/范围/条件及接受输入；AUTH-04 的轴 covered 与 CONC-01 操作缺口分开。DES-14 残留见 FM-1。 |
| 175 / covered+narrow / pending | **完成度降格关闭。** 49 covered、55 partial、71 not-covered 是175条比较意见，另8 pending；不是175个已独立完成源评估。not-assessed 单列。covered 与 narrow 并存被准确承认，没有以标签证明采纳/关闭，也没有新覆盖百分比。 |
| narrow/replace / 未读价值删改 | **消费纪律关闭。** 实质删改同样需§5主体及承重支持回读；范围排除不否定专业知识；DES-27/CONC-05/ORC-12 为探索性 defer，没有未读先按篇幅删例子。 |
| DES-24 / DBG-06 | **补读入口关闭。** 给出具体 build-the-lever/watch-pr、diagnosing-bugs/run-smoke-tests 路径，不要求本批先运行或全文重扫。 |
| DES-20 / DLV-07 | **授权与判断分支关闭。** 删除方法“授权未来检查”；恢复不能结构化时加强说明/失败例子、可形成具体待办。与固定 encode-lessons 源相符，不再无条件脚本化。 |
| 183桶 / 474+8 / requery | **主体统计与定位关闭。** 183含10条产品自身来源，不作上游贡献；来源组合互斥表合计183。A2 metadata实数79组/482路径，大小为73组×6、5组×7、1组×9；额外六SKILL＋shopify.mdc＋pricing.md共8，474+8正确。剩余 `ADJ ` 虚构标签为0，改用文件/section/id。个别短文残留见 suggestion。 |
| C1–C6 | **消费侧限缩关闭。** loci无序；depth不可排名但非免责；相关文件共同读但不强揉成一规则；相同bytes仍需语境；关系线索不是证明；文本覆盖/静态源依据/运行强制力分开，未要求运行所有上游来评价知识。 |
| MCAL-1 / 2 / 3 / 4 | MCAL-1泛化撤回；MCAL-2的175降格及主要current-text错误修复，DES-14残句未关闭；MCAL-3全文条件/前置已修，机械R汇总未关闭；MCAL-4的C5、未来权限与未读删例子已关闭。原FAIL与固定对象历史保留。 |

## Must-fix（里程碑问题，不另开开放返修循环）

### FM-1 · 两处纠错未真正同步到当前承重文字

**R 汇总：** 按 ADJUDICATION §4 自定“条目内首个出现的 R 标签”，本次39条adopt实际为 **R0=24、R1=8、R2=7**；§4、修订记录及 CALIBRATION 仍报25/7/7。BHV-10 在此次纠错由R0改成R1，旧批计数不能直接沿用。没有把R标签当资格是正确降格，但机械汇总仍须一致；可以更正或删除不必要汇总，不需增加阅读任务。

**DES-14：** TSV 的 `uncertainties` 与 adjudication 已说明没有“只增不改”的产品默认，`current_text_basis` 却仍写“§Method 6 兼容段与其相反默认”。这是同一行中的活跃相反前提，不是历史引用。应保留真实源/current-text操作差异，去掉该残句；无需重审迁移全文或重开 core。

### FM-2 · DBG-05 的“正确”例子在脱敏前落盘敏感原始工件

位置：草案§3的 `curl -D /tmp/dbg05/headers.txt -o /tmp/dbg05/body.json ...`，随后才 `grep` 信号行。它将全部响应头/体先写盘；同一场景明确讨论Set-Cookie与可能敏感HTTP内容，且没有用户同意落盘的条件。显示少数行不等于没有保存原始敏感bytes。

这与草案自己的§1/DBG-05.3及固定 verify-this L51 的“敏感工件默认最小行内，用户同意才写盘”冲突；env var避免命令文本含明文，不解决响应内容保管。该例不能标成默认正确路线或宣称已避免秘密进入保管面。

可记录的最小解决方向：默认例子仅处理获准的、最小脱敏证据；若需保留raw，明确另有既有有效同意、受限位置与保管/清理边界，并把它写成条件分支。无需本轮实现脱敏脚本、创建目录、发请求或新增权限 gate。这里是草案内容缺陷，没有观察到真实敏感文件被写出。

### FM-3 · DBG-16 的 adapter 反例没有证明所称缺陷会被“正确做法”捕获

位置：草案§3第一变体把缺陷放在 **生产HTTP adapter 的请求/契约假设**，如200＋空字段被当0。提出的修正却是用 in-memory adapter 测试同一deep-module逻辑。若测试完全换掉生产HTTP adapter，其解析/请求缺陷仍不被执行；好的in-memory实现也可能全绿。仅换adapter不是此反例的证伪证据。

需要把“测deep-module逻辑”与“核生产adapter/边界契约假设”分开，不能把前者覆盖泛化到后者。可保留第二变体：mock自己内部协作者掩盖真实逻辑，直接使用真实内部协作者即可形成对应反例；或明确将哪段解析/约束保留在实际被测逻辑内，并说明其覆盖限度。若确需验证transport边界，记录相应契约/adapter观察的需要，不能新设所有任务固定integration gate或在本轮运行服务。

另应在同一条范围说明中区分：不stub掉真实内部协作逻辑，与在跨网络port上提供test adapter是不同操作。原源的 `Anything you control` 禁令与owned-remote替代策略不能无解释并排后，让读者猜它们如何共存。

## 四类结论分开记录

| 评价面 | DBG-05 | DBG-16 |
| --- | --- | --- |
| **源保真** | pin/路径/blob及Redact、verify-this L51、HITL step/capture锚实际存在且匹配；脱敏信号/保存限制来源成立。§3是草案自拟例子，不因源表正确自动正确。 | 三份源pin/path/blob匹配；四类依赖、sometimes DB/FS、SDK/DI、私有seam、两adapter、replace-don't-layer均有源锚。它们不是整篇重复。对组合范围/例子的推论尚需FM-3澄清。 |
| **当前覆盖** | 当前方法确有exact commands/preserve output的记录基础；补脱敏/保管顺序与HITL边界是具体增量，不把现有正文读成要求提交机密。 | 当前cross-module §Method 3已有四类依赖简述；新增mock/adapter选择与例子是操作扩展，不是完全无覆盖，也不把新词汇赋予责任/授权。 |
| **工程细节** | 保留env注入、信号行、不足时替代证据、敏感工件保存、step与回显capture；FM-2使默认示例不合格，不能给草案可采用PASS。 | 保留stand-in存在条件、边界mock、owned remote/true external差异与内部seam；FM-3反例的验证面错配，不能据它说明adapter原始缺陷已被捕获。 |
| **拟议变化/authority** | 仅docs草案和两个记录处拟接点；没有active编辑、generator、工具部署或运行强制力声明；正文也不产生动作许可。 | 仅docs草案/Method 3拟接点；没有真实adapter实施或测试、固定新gate/authority；采纳与发布仍未授权。 |

以上源静态支持不是源机制运行强制力PASS。草案存在、全读源或本检查完成，都不等于方法已采纳、core可合入或landing授权。

## Suggestions（不单独阻断）

1. DBG-16 “深模块接口测试建立后旧浅模块测试成为浪费”的源句，可作为来源背景；后续接入必须保留当前§Method 4的窄条件：replacement已覆盖对应accepted claim、删测试需已有动作授权。不能从“有新测试”推成所有旧检查都无价值；无需新增审批表。
2. DBG-05的step描述应准确：脚本只提示并等待Enter，不技术强制屏蔽用户终端回显；credential不放capture的分流有源支持，但不能声称step自动使登录行为不回显。保持“用户自己的登录流程、只采安全观察”即可。
3. 草案行号存在小偏移（例如mocking.md的SDK优点在L55–59，不仅L37–53），chapter/function锚正确；建议以章节/条款为主，补承重行范围，不需机器索引。
4. 校准修订表仍写“七个互斥桶合计183”，当前表实际七种上游组合＋产品自身来源，共八桶；表内总数正确。SOURCE引用数量的正文应继续区分prefix/product标记与具体path，不把解析成功等同已读。
5. BHV-10的源glossary边界已修，但“领域语义只能散落Charter/Plan”仍是未经实际使用验证的影响推断；AUTH-09/GOV-01等新增载体/状态形态仍是备选，不变成继续骨架设计或校验器的前置。

## Residuals / 停止点

本报告覆盖上述fixed对象的纠错与草案静态claim，未审全库、全部A索引正文、183机制源真实性或其余候选；未验证历史盲读时序/实际阅读动作。pending与not-assessed、其余源回读、效果/运行强制力仍依原边界保留，不为通过本报告强制全量补读/运行。

已接受core及原A路径accounting不因本次草案问题失效。本轮只写本报告，未改草案/B/A/core/上游，未实施、派工、提交、运行UCBIP或新的Pro。

FM-1是有限静态记录纠正，FM-2/FM-3是两份草案尚未具备的实质工程解释。请作为既定里程碑的未决质量交给Driver/Oracle记录与处置，不自动再启动同一开放修订/审核循环、不靠新SHA重置范围。Owner的core landing envelope仍未由本检查产生。
