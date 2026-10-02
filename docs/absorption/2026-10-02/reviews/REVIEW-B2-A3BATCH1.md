# REVIEW-B2-A3BATCH1

tpw-absorb-gate，2026-10-02；结论：**需修，暂不可集成**。

固定差分：`d3aab6ad30f36789664287f304e4e91ffd61d96a..11136ebfb101b5f96e9cb65d862ba9af2389ed15`，branch `absorb/w2`，worktree `.worktrees/absorb-w2`。依据REVIEW-A3-MATT-ABC的MG-5/8/9/11、已回读固定源和冻结Backbone。按git diff/git show查看全部三新增正文和Profile差分，`git diff --check`通过。作者工作区有后续decision-elicitation编辑与新源批次未跟踪文件，**本review未使用这些工作字节，也未修改它们**。

## 阻断项 R1 · 建议被视作决定

位置：`professional-workflow/methods/decision-elicitation.md:21`（Ask by dependencies第7项）。

“already determined … by the chosen recommendation”可把agent已选建议直接当作settled answer，排除真正的owner决定；前文第5项明说owner可接受、调整或推翻建议。MG-9只允许实际接受依据/有效委托内决定取代重新问Owner，不允许建议代替未获得的保留决定。

最小修：删除建议本身可使问题settled的路径，或限定其为有效决定者已接受/在明确委托内作出的选择，注明未接受建议仍需该owner决定。补“推荐供应商A但选择保留给Owner→仍问，不能记成已决定”的反例（或等价场景）。不要把授权不足的问题仅记成解释。

## 阻断项 R2 · 裁剪例子把默认行为当观察

位置：`professional-workflow/methods/guide-agent-text.md` §Examples/counterexamples 的 Pruning counterexample（“write tests … is a no-op: deleting it changes nothing observable”）。

此例直接判定未给模型/任务/观察的文本为no-op，与本文件§Evidence limits及MG-8裁定冲突。默认倾向并不证明指令可删；删除一条任务特定测试义务可能实质改变行为。

最小修：将该例标成待验证假设，或给明确特定模型/任务的已观察前提并限制覆盖；不要虚构跑过的观察。保留硬约束即使常遵守也不可据此删除的反例。

## 阻断项 R3 · completion分拆前提丢失

位置：`guide-agent-text.md` §Completion第7项。

源`writing-for-agents/SKILL.md` §Steps and completion criteria要求先sharpen；仅在criterion无法进一步澄清且实际观察到rush时才隐藏后续步骤。正文只保留“sharpen；跨context隐藏”，丢了后者两条件，可能凭一般担忧就增加handoff/agent分拆，违背MG-8按证据处理、无新gate边界。

最小修：恢复“无法再澄清并已观察到premature completion”的条件；优先改done条件，必要分拆仍继承关键授权/召回，且需任务已有运行资源/委托支持。无需增加测试框架或实际派agent。

## 已通过内容与整合限制

- behavior-contract-examples保留基线红的新增条件、基线绿的保持条件、上层跨项outcome/子项依赖区别，纠正MG-5源至to-tickets L76–77；未强制全条件自动e2e。
- elicitation其余依赖重排、事实先查/不可访问unknown、实际authority路由、原型动作授权和不新增final ACK条款符合裁定。
- agent-text的progressive disclosure、co-location、meaning真源、local mapping消费不保证、硬guardrails显式保留及整体“效果未验证”条款已成立；R2/R3是具体操作仍需与这些条件一致。
- Profile消费指针真实存在；agent-text需Driver在methods README添加按需索引。F Profile两branch同段写面由Driver串行保留，不属于作者正文缺陷。
- methods README索引/状态声明是已明确Driver的集成工作，不因未动README否定当前正文；最终组合对象仍须核一致性。两分支单件通过不自动证明whole-core。

我未代写修复，保持独立。复查以新固定commit的R1/R2/R3和受影响consumer为范围，未执行真实访谈或模型行为实验，不报告效果PASS。
