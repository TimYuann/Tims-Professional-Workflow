---
obsidian-note-type: agents-md
target: any-agent
project: tim-professional-workflow
cwd: ~/Developer/tim-professional-workflow
---

# TIM · Professional Workflow — 本仓维护纪律

本文件短、稳定、项目专属。全局行为规则见全局 `AGENTS.md`，不在此重复。

## 这是什么

一套与工具无关的工程工作流：角色、技能、原则、产物契约、脚本。
它提供工程经验，不提供调度。

## 唯一真源

`workflow/registry.yaml` 是机器可读的事实来源。

**任何含义都不在两处各自设值。** 需要新增或修改语义时，改真源，
然后 `python3 scripts/render.py` 重新生成派生视图。

派生视图（`workflow/phases/`、`workflow/ribbons/`、`docs/artifacts.md`）
**不得手工编辑**——手改会被 `render.py --check` 报出来，
所以不存在「生成区和真源对不上、需要人去核对」这种状态。

## 改动纪律

1. **上游只读。** `upstreams/` 只作参考源，永不修改。
   吸收的机制要**先读正文**；没读正文不算吸收。
   上一版的 `NOT ABSORBED` 里就有一条是没读就标的。
2. **处置表由文件系统核对。** 每个上游 skill 在
   `upstream_dispositions` 里恰好一条。`check-closure.py` 直接对着
   `upstreams/` 扫目录核对，**这不是人写的台账，所以不会对不上**。
3. **原则正文只有一处。** 一条原则有唯一的 owner 角色；
   其他角色引用它的 id。想复用一条原则，就引用，不要复制文字。
   上一版把 23 条原则回填进九个角色正文，于是同一件事在九个地方
   被写成互相矛盾的说法——这正是 `check-consistency.py` 要拦的。
4. **角色不内联技能。** 角色文件讲「这个人是谁、怎么想、不能做什么」；
   技能正文在 `skills/`，按需引用。
5. **产物不是文件。** 产物是一组字段 + 产出方 + 消费者 + 存活期。
   落在下游哪个路径由 `driver` 按集合 B 裁定；纪律由本库定义。
   不要在本库里规定下游的目录结构。
6. **角色是装配出来的，不是直接读的。** 原则正文只在 `principles/<owner>.md`；
   角色文件里只有引用与 `trigger`（这个角色何时加载它），不复述原则的意思。
   起会话前用 `python3 scripts/compose-role.py <角色>` 拿到拼好的 prompt，
   `python3 scripts/compose-role.py --check` 验结构。直接发角色文件正文
   会让里面的原则引用变成未定义符号。
7. **多 agent 协作走「起独立会话 + 会话间消息」，不走进程内子代理。**
   子代理与主会话共享一个进程与一份上下文，没有独立身份，
   跨轮交接、独立重开、彼此发消息都做不了。
   每层用同一个名字：本仓叫什么、那个会话就叫什么。
   **不要因为某个封装工具看起来更方便就换过去。**

## 改动之后

```bash
python3 scripts/render.py
python3 scripts/check-closure.py
python3 scripts/check-consistency.py
python3 scripts/compose-role.py --check
```

三个都只读或幂等，非零退出即失败。**不要修脚本来让它过。**
先问是哪条断言不成立，再决定改真源还是改断言。

## 硬边界（任何档位都不放宽）

1. 提出候选的人不得给这个候选下结论。
2. 不得为让检查变绿而削弱检查。
3. 验证只有三态：`PASS` / `FAIL` / `UNVERIFIED`。
   环境故障既不算 `PASS`，也不判成产品缺陷。
4. `A9` 台账只追加。不修改、不删除既有行。
5. **本库的 Driver 停在「逻辑编排层」。** 它定义 control semantics——
   谁该上场、哪个 artifact 够不够格、退给谁、什么时候停。
   它**不定义 execution mechanics**——进程、并发上限、WIP、队列、锁、
   重试、资源治理都属下游 runtime。下游 harness 也管这些。

## 检查器判不了什么

- 方法本身是否真的有效。
- 退出判据是否合理、是否可判定。
- 下游是否真的照做了。
- 某一次跳过是否真的合规。

这些交给人审。**检查器全绿不等于这套东西好用**——它只证明结构没塌。

## 新增检查的保留判据

要能说清它保护的是哪条**真实断言**、给一个会红的反例、
说清常见合法变体为什么不会误报、以及谁负责维护它。
四条缺一条就别加。本库的检查器是从旧版的 26 项里收敛到 8 + 7 的。
