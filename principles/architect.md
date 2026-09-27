# 心智模型 · 建模与定契约（`architect`）

原则不是技能：没有触发条件，没有产物，没有消费者。
它们是 `architect` 默认该怎么想的构件，**正文只有这一处**。
其他角色需要同一条原则时，引用它的 id，不复制文字。

角色文件：[../roles/architect.md](../roles/architect.md)

---

## p-foundational-thinking

写逻辑之前先定核心类型与数据结构，决定脚手架与特性的先后，并问清并发参与者共享什么。

其他持有它的角色：`architect`

来源：`upstreams/cursor-plugins/pstack/skills/principle-foundational-thinking/SKILL.md`

## p-model-the-domain

有状态逻辑或大量分支重复同一形状假设时，把领域编码进结构，而不是散落的条件判断。

其他持有它的角色：`architect`

来源：`upstreams/cursor-plugins/pstack/skills/principle-model-the-domain/SKILL.md`

## p-type-system-discipline

让非法状态不可表示；边界穷尽优于运行时检查。

其他持有它的角色：`architect`

来源：`upstreams/cursor-plugins/pstack/skills/principle-type-system-discipline/SKILL.md`

## p-boundary-discipline

校验集中在系统边界（外部输入、适配器、配置），不要在内部每层重复。

其他持有它的角色：`architect`、`verifier`

来源：`upstreams/cursor-plugins/pstack/skills/principle-boundary-discipline/SKILL.md`

## p-minimize-reader-load

审查难以追踪的代码时，数一数问题与答案之间隔了几层，收缩可变作用域。

其他持有它的角色：`scout`、`architect`、`scribe`

来源：`upstreams/cursor-plugins/pstack/skills/principle-minimize-reader-load/SKILL.md`

## p-redesign-from-first-principles

把新需求当成一开始就存在的基本假设来重新设计，而不是打补丁。

其他持有它的角色：`architect`

来源：`upstreams/cursor-plugins/pstack/skills/principle-redesign-from-first-principles/SKILL.md`

## p-exhaust-the-design-space

面对无先例的交互或架构决策时，先造 2–3 个竞争原型再比选，不要一上来就押注。

其他持有它的角色：`architect`

来源：`upstreams/cursor-plugins/pstack/skills/principle-exhaust-the-design-space/SKILL.md`

## p-migrate-callers-then-delete

引入新内部 API 时，把调用方迁移与旧 API 删除放在同一波里，不保留兼容层。

其他持有它的角色：`architect`

来源：`upstreams/cursor-plugins/pstack/skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md`

## p-outcome-oriented

收敛到目标架构，不为了中间态平滑而保留过渡结构。

其他持有它的角色：`driver`、`architect`

来源：`upstreams/cursor-plugins/pstack/skills/principle-outcome-oriented-execution/SKILL.md`
