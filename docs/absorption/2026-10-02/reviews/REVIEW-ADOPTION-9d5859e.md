# REVIEW-ADOPTION-9d5859e

tpw-absorb-gate，2026-10-02。固定candidate `9d5859eabc6020355b9ddc6e09b9329ad72e671d`，branch absorb/adopt；仅两新增对象：`professional-workflow/ADOPTION.md`、`adoption-examples/cross-module-start.md`。结论：**需修3处消费语义；边界设计其余通过。**

依据：`docs/absorption/2026-10-02/ADOPTION-DELIVERY-BRIEF.md`本轮增补、已读冻结Backbone/Charter/package入口、最新B1/B2裁定。用git show读固定两文件全文；当前产品和例子未被我修改。我未代写接入说明，保持独立。此review不授权下游采用、实际写入、联网或生产资格。

## 需修项

### R1 · 常驻的是指针，不是多个完整入口

位置：ADOPTION §5第一项“短指针（常驻上下文）：包README、本文件、profiles README与methods README选择入口……”

把完整本文件/多个入口列为常驻对象，会让采用者把全部入口材料始终加载，与brief“默认始终加载的短指针与按需正文分开”混淆。若意图只是链接，需明确，不要求整份ADOPTION随每任务进入context。

最小修：常驻一条指向固定版本接入/选择入口的短指针即可；需要接入/选择/装配时才读相应入口及本说明。Profile/方法/authority仍只读当前Charter需要内容。不强制项目拥有AGENTS文件或统一文件名，不新增composer。

### R2 · 示例移植了未通过证据等级

位置：cross-module-start例2标题“证据等级”、Plan交接项和§证据等级，例2的change-review/handoff绑定。

示例要求验证主张按五值等级携带；该规则已在B1handoff的R1判需修，不能借接入示例升级成另一份真源。五种类型是源运行协议，不是通用证据门槛；live不证明shipped、unit非UI不自动足够，typecheck也可有效证明typing claim。证据阶梯也只是观察方式/覆盖，不强制每claim按固定序列上升。

最小修：示例携带claim/对象版本/实际执行/覆盖限制/真实贡献及PASS/FAIL/UNVERIFIED；可列五种来源标签作非穷尽例，不要求必选等级或机械映射。方法正文拥有详细判断，示例只引用，不另复制规则。F三态与状态/授许可分开，保留真实leg按claim与授权决定的现有句。

### R3 · 比较型方法泛化所有行为claim

位置：例1“F评价具体行为claim时另绑behavior-claim-evaluation”，其交付映射；例2“行为claim的verdict”及末段“行为claim用该方法三态”。

既有behavior-claim-evaluation §Use明确是baseline/treatment比较，其他F判断可以需其他证据。示例目前把所有claim路由到它，重现B1已修的范围泛化。三态来源于责任纪律，不必须经过该比较方法才有三态。

最小修：给出这里具体适用的baseline/treatment条件（已复现缺陷可作比较例），适用时绑定该方法；其他claim按接受依据与适当验证设计，由F给三态。避免因没有baseline把直接不变量反例降为无效。无需添加一个通用验证方法/检查器。

## 固定引用与条件集成

`change-review.md`、`handoff-and-resume.md`等在B分支候选中有正文，但仍需修、未集成；采用例先声明在固定版本查存在、无正文不伪绑，这一边界正确。实际集成应**等对应方法目标修复通过后一起固定**，或者示例条件性说明仅版本确有这些能力时使用，缺失时采用该版本已有合适依据/明确未绑定；不能把未来方法列成当前core已有接受对象，也不自动创造替代等价名。

入口指针由Driver单写。最终固定整合对象需核两例引用目标实际存在/适用、README状态和选择入口一致；这只是当前消费对象检查，不要求通用validator/schema/gate。

## 已通过的边界

- 无权限引擎/安装平台/强制project schema；目录、既有治理owner与下游动作权限由目标项目决定。Profile不是authority，Charter只记录真实grant，接受/验证/动作/关闭分开。
- 固定repo+commit/tree+包相对路径；`git show commit:professional-workflow/path`和子tree相对读取正确；mutable main不偷换本次依据。vendor保留来源/署名/本地patch，布局变更需实际相对引用可解析，而不只修改路径标签。
- 五步接入从目标/已有承诺、缺judgment、按需方法、真实Charter到纯文本startup，简单任务不强造全项目治理；缺必要目标/authority/保留项/closure具体明示。
- core与任务输入分开固定，升级按差分判断受影响约定/证据，已有有效证据可复用，无全量re-review默认。
- 跨harness用现有Git/文件文本可消费；只有真实机械摩擦才考虑项目侧小helper，不默认composer。无需下游UCBIP example，四退休名字不装等价方法。
- “不写/不联网”明确只读测试约束不传播产品政策；真实任务证据种类由claim/有效授权决定，例子权责可替换且不授权。未要求下游policy采用此review流程。

未做fresh-reader实际消费或验证项目效率；该观察须在正式整合版本后由已安排的真实fresh reader进行，不能把本作者说明/本review当冷读证据。修复只核R1/R2/R3及消费依赖，避免扩大scope。
