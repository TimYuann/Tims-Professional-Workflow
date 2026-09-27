# 心智模型 · 实现（`builder`）

原则不是技能：没有触发条件，没有产物，没有消费者。
它们是 `builder` 默认该怎么想的构件，**正文只有这一处**。
其他角色需要同一条原则时，引用它的 id，不复制文字。

角色文件：[../roles/builder.md](../roles/builder.md)

---

## p-subtract-before-add

加东西之前先删死代码、冗余校验和悬空引用。

其他持有它的角色：`cartographer`、`builder`

来源：`upstreams/cursor-plugins/pstack/skills/principle-subtract-before-you-add/SKILL.md`

## p-laziness-protocol

偏向删除与最小变更；警惕为了未来假设而增加的抽象层。

其他持有它的角色：`builder`、`adversary`

来源：`upstreams/cursor-plugins/pstack/skills/principle-laziness-protocol/SKILL.md`

## p-fix-root-causes

先复现，再逐层追问为什么，修在根因上；不用空值守卫掩盖症状。

其他持有它的角色：`builder`

来源：`upstreams/cursor-plugins/pstack/skills/principle-fix-root-causes/SKILL.md`

## p-sequence-verifiable-units

把多步工作切成每步结束于可验证状态的小单元，再决定提交与 PR 的堆叠。

其他持有它的角色：`cartographer`、`builder`

来源：`upstreams/cursor-plugins/pstack/skills/principle-sequence-verifiable-units/SKILL.md`

## p-test-behavior-not-implementation

像用户那样调用代码，断言他们观察到的结果，而不是断言内部实现。

其他持有它的角色：`builder`

来源：`upstreams/cursor-plugins/pstack/skills/principle-test-behavior-not-implementation/SKILL.md`

## p-make-operations-idempotent

在崩溃、重启、重试之间运行的操作，重跑必须收敛到同一终态。

其他持有它的角色：`builder`、`verifier`

来源：`upstreams/cursor-plugins/pstack/skills/principle-make-operations-idempotent/SKILL.md`

## p-separate-before-serializing

并发写同一份状态时先消除共享，实在消不掉再按结构串行化。

其他持有它的角色：`builder`

来源：`upstreams/cursor-plugins/pstack/skills/principle-separate-before-serializing-shared-state/SKILL.md`

## p-build-the-lever

非平凡的工作先造那个能做完或能证明它做完了的工具，而不是手做一遍。

其他持有它的角色：`cartographer`、`builder`

来源：`upstreams/cursor-plugins/pstack/skills/principle-build-the-lever/SKILL.md`
