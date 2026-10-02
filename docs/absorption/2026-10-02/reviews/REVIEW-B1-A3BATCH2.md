# REVIEW-B1-A3BATCH2

tpw-absorb-gate，2026-10-02。固定候选`375b40c4e64c7ee0828f62793afb8888fcb1e1dd`，base`d3aab6ad30f36789664287f304e4e91ffd61d96a`，branch absorb/w1。用git diff/show核commit；作者当前在飞字节未参与。`git diff --check`通过。

依据REVIEW-A3-MATT-ABC、REVIEW-A2R-CURSOR-ABC及已出的跨源AB/DEF联动裁定；已完整读新增五正文、轨迹段与R1修复。源承重正文已在上述reviews直接回核，本次不重复全部读源；新增consumer和实际表述逐条核。未代写B，不作效果实验。

## 第一批复查

**原R1关闭。** guide-test-evidence-quality现在明确F反例/有效观察可独立于comparison成立，给租户隔离直接反例，证据选择归claim/policy/design/F，既有comparison方法§Use和三态未改。

**第一批11文件的受审内容可复用PASS**（以本candidate对应字节为准，decision-record新轨迹见下述新范围）。不得据此称整个375b40c通过；第二批以下阻断仍在。

## 第二批：需修，暂不可整笔集成

### R1 · handoff重新硬化证据类型

位置：`methods/handoff-and-resume.md` §Handoff 的“carries one of five grades; old labels migrate”、等级表Reading、Failure mode beliefs句。

裁定已拒五值机械映射/全局等级；表仍规定live-ui“trust as shipped”、unit非UI够且UI需live，旧标签保守迁移又未明确实际执行与覆盖。后段“grade about claim”不能让前表这些动作成立。**最小修：**五类只作来源中的可选观察方式例子，采用claim/对象版本/实际执行/覆盖/局限/独立性决定结论；live不证明shipped或全claim，UI可有正确logic fixture且真实体验claim需真实leg，旧pass缺证据标未核不伪称type-check执行。beliefs句不能称receiver treats as contract/will not recheck；接受依据和未经证实自报分开。反例保留compile可证type、live局部不足证全部、broken instrument仍UNVERIFIED。

### R2 · domain representation禁止D的合法变化

位置：`methods/domain-state-and-invariants.md` §State questions，ownership split：“D/E decide … only insofar as it does not change the coordination surface”。

D在有效envelope内可选择/修订技术coordination，E仅在已委托承诺内自主。当前一句将D/E一起限为不得改coordination，改变冻结分界。**最小修：**分清D共享方案的有效委托内决定与E内部表示选择；改变上游B/C语义或越界才回其authority，E发现共享承诺变化召回D。无须给新actor/审批流程。

### R3 · harness正文仍规定全feature live维护

位置：`methods/verification-harness-design.md` §Maintain Pass，§Limits第二项及§Use/limits对comparison的归属。

Pass称source clean也required live、每feature至少一次；Limits又说无每maintenance全live要求。裁定要求按本次受影响claim/recipe覆盖，不能靠段末否定掩盖前面全量命令。另Use/Limits称comparison拥有claim/threshold/verdict，重现原R1范围泛化。

**最小修：**明确当前维护对象及其受影响features/claims/recipe，source-only检查不冒称live；需要证真实路径的claim才跑该路径，改harness后重驱受影响recipe；任务本就委托全feature审计时才全量。证据/判据来自接受契约、任务验证设计、policy和F；comparison仅适用时用。cleanup证据存续与敏感到期边界已正确，保留。

### R4 · change-review作者地位与独立性

位置：`methods/change-review.md` §Disagreements 的“Author override … defer”、§Limits“No mandatory review form”与two-axis段。

作者有更多context是补证理由，不产生覆盖接受标准/风险或撤独立finding权限。既有委托才有接受权。新F方法“Not every change needs … an independent reviewer”也未说明：若是Charter要求的独立F评价，作者不能自证；可不调用本方法与本方法被调用后的真实independence不是同一层。

**最小修：**作者补充context后由有效专业/接受authority核，按Charter贡献关系作F评价；自查明确自查，无默许把作者覆盖当authority。two-axis保留各轴证据/未解项与不相互抵消，不能把“never cross-ranked”当全局阻止有权者按实际风险安排工作的规则（已在A3-DEF正式限缩）。second-opinion固定至多一次follow-up也是源运行额度例，不变普遍门槛。其余finding因果链/thermos纠正源/多模型不升证据级已正确。

## 已核内容及消费限制

bounded-prototype的observable量与价值选择、授权/throwaway/真实生产leg区别成立；其“no assertion substitute”宜说明适用prototype观察而非一切自动assertion无价值，当前既有Limits不构新测试禁令。decision-record轨迹不创造exit/side-fix权限，来源身份可查，原历史保存/状态正确。domain不变量与合法简单branch例有区分力；无需每知识点代码test。

实际diff`e561233..375b40c`仅7方法文件+332/−2，**未新增第二批Profile指针、未改变cross-module/claim**（这些已在第一批）。新正文彼此引用可达，但harness/domain-state/change-review/bounded-prototype/handoff的选择消费入口尚待Driver显式补入methods README及适用Profile；不能以第一批已有D指针宣称新方法已完整可启动。这是已委托集成工作，非单件正文缺陷；整合固定对象需再核。

复核范围：上述R1–R4和其直接consumer；第一批原R1不重开。保存实际working edits，修复由B完成。第二批不PASS，Driver不得整笔集成375b40c。
