# REVIEW-B1-A3BATCH1

tpw-absorb-gate，2026-10-02；结论：**需修，暂不可集成**。

固定差分：`d3aab6ad30f36789664287f304e4e91ffd61d96a..e561233a556e2073c98ecc5cd46cc45a0acf1b74`，branch `absorb/w1`，worktree `.worktrees/absorb-w1`。只审上述commit，不把作者后续工作区编辑混入；起读status无差分。依据 `REVIEW-A3-MATT-ABC.md` 的MG-1/2/3/4/6/7/10/11与该裁定已直接回读的固定Matt源、冻结Backbone。

已完整查看固定diff及六个新增正文（批量diff截断部分另用git show补读），确认11文件写面，`git diff --check base candidate`通过。未代写候选/修复，实际独立性保持。结构检查和正文例子分析不是方法实际工程效果实验。

## 阻断项 R1 · 比较方法被泛化为全部F依据

位置：`professional-workflow/methods/guide-test-evidence-quality.md:40`（Examples and exceptions）及`:46`（Limits）。

L40称任何product FAIL都需要valid comparison；L46称任何claim需要多少/哪些测试证据都是`behavior-claim-evaluation.md`的工作。现有方法§Use明确仅适用于baseline/treatment比较，其他F判断可用其他证据；guide自身又用于任意check/suite。两句使比较方法变成所有验证的唯一依据，超出MG-3的质量支持定位。

区分反例：接受的不变量是“租户A不可读取租户B订单”；在正确版本和授权测试数据上直接观察A读到了B对象，即是有效反例，未取得另一baseline不能因此排除FAIL。反之harness坏仍UNVERIFIED。问题是覆盖范围，并非修改既有三态。

最小修：把FAIL需要的依据表述为对接受claim的有效反例/观察；只有调用baseline/treatment方法时才要求其有效comparison。证据种类/数量由claim、适用政策、任务验证设计与F判断决定，comparison方法在其适用范围内提供一种路径。保持既有方法§Use和三态不变，补上述直接反例或等价短例。由B修，我不代写。

## 非阻断观察与已通过内容

- red原因核对、独立oracle、局部重构权限、两观察表面、慢测试成本取舍均保持MG-1/4限缩；未新增人类seam ACK gate。
- correlated oracle与合法存储/type evidence反例确实区分不同claim；避免了“内部耦合等于永远绿”的错误。
- change-slicing保留基础设施支持项的自身可检结果及宽迁移无法单批绿例外；不授branch/migration/delete权限。
- decision-record保留已有委托要求记录的例外、拒绝/暂缓/已实现区分及历史状态；domain-language保留context-local Avoid和当前代码不等于业务规则；design-alternatives有实质比较依据且无默认并行agent gate。
- 实际Profile指针可以进入新增正文；相互引用的目标路径在固定candidate存在。B/C的decision-record/domain-language消费指针仍可由对应作者/Driver入口整合补齐，不以D指针冒称所有专业入口已完整。
- methods README尚未更新是已明确的Driver集成工作，**不作为本diff正文缺陷**。最终整合必须加入各任务need索引，更新“仅三方法两guide”状态文字，合并F Profile两分支指针并核新固定对象；此review不证明整体已一致。

未逐行认证所有源line-range元数据，无运行收益PASS；所需语义核回已足以定位R1。复核范围只需R1受影响guide及相关consumer，其他已审内容可按差分复用。
