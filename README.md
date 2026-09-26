# TIM · Professional Workflow (Professional Teams & Engineering Kit)

> **全局 AI 软件工程能力库与专业角色套件**
> 独立版本化 · 9大核心角色 · 方法全局配方本地 · 动态越权隔离 · 双层同步

本项目旨在将业界顶级工程师（Cursor 团队、Matt Pocock、Addy Osmani、Dex Horthy、Armin Ronacher 等）开源的工程经验、方法论和工作化脚本（Skills / Rules / Scripts）进行解构、去重、冲突裁决与深度整合，形成一套**与具体业务解耦、与 Harness 底座解耦、可被多 Agent 工作流按需调度**的专业工程能力体系。

---

## 核心设计哲学

1. **工具底座解耦（Harness-Agnostic）**：
   - 底座插件（如 `orchestra-dsh`）专精提供基础会话生命周期与 A2A 消息通信；
   - Professional Workflow 专注认知决策、角色纪律与工程方法。Driver 在任务启动时自主探测环境能力并自适应装配。
2. **“说人话”铁律（Speak Human Principle）**：
   - 面向人类 Owner 的交互必须使用非技术的大白话，严禁输出任何 AI 黑话或技术术语，通过自然语言对话降低人类把控门槛。
3. **波次起止介入与自主闭环（Wave Model）**：
   - Owner 仅在波次开始（对齐目标、授权与预案）和结束（验收晨会）介入；
   - 授权范围内团队 100% 自主推进，交接不打扰人类。
4. **动态越权 Worktree 隔离机制**：
   - 夜间遇到超出预先授权的大架构调整时，系统自动在独立的 Git Worktree（`worktree-isolate/<task>`）上完成端到端探索与验证，主线不受影响，晨会交付完整决策分支。
5. **项目文档体系双模适配**：
   - 模式 1：已具备完善文档（如 UCBIP），自动映射真源，不制造第二事实源；
   - 模式 2：文档缺失或不规范，Driver 征得 Owner 同意后一键生成规范模板，提升项目工程治理。

---

## 九大核心角色编制（The 9 Core Roles）

| 角色 | 核心使命 | 主要交付物 | 绝对不应该做的事 |
| :--- | :--- | :--- | :--- |
| **Driver** | 任务编排、依赖梳理、派工与对外大白话沟通 | 结构化任务卡、对外自然语言进展报告 | 包揽代码编写；代替人类擅自改变产品承诺 |
| **Oracle** | 人类代理人，在过夜自主运行时代人类把控业务意图与偏好 | 业务意图裁决卡、产品偏好仲裁意见 | 陷入技术实现细节；推翻人类已冻结契约 |
| **Investigator** | 还原系统真实行为，区分事实与假说，定位根因 | 因果诊断报告、执行路径追踪 | 顺手改代码；把“附近的报错”当根因；夹带修复补丁 |
| **Architect** | 决定接口形态、状态归属与模块边界，比较方案 | 接口草案、2-3 种方案对比（含不改基准） | 把个人偏好当契约；自动进入编码实施 |
| **Planner** | 将设计转化为按依赖排序、可独立验证的切片 | Tracer-bullet 改动清单、验收命令矩阵 | 借拆解任务之名偷偷重新设计系统或扩大改动范围 |
| **Implementer** | 在严格限定的文件与语义范围内完成变更与自验 | 代码变更（Diff）、开发自验通过证据 | 超出授权范围改动无关文件；自行宣布最终业务验收通过 |
| **Reviewer** | 独立对抗性审查，挖掘结构坏味道与安全前提 | 结构化 Findings（分机器修复与人类考量） | 为了证明存在感挑刺无害代码；替作者重写实现 |
| **Verifier** | 独立构造反例与真实端到端路径，证伪核心主张 | 真实环境执行日志、反例构造结果、覆盖率声明 | 绕过真实入口只测 Mock；把“测试全绿”等同于“交付正确” |
| **Integrator** | 将已验证结果合入目标分支，消除意图冲突 | 集成后版本、冲突消解说明、全量回归证据 | 借合并之机插入未经审查的新改动；擅自突破发布权限 |

---

## 快速导航

- 📘 **完整架构与裁决规范 (v1.0-final)**：[`docs/TIM-PROFESSIONAL-WORKFLOW-PROPOSAL.md`](file:///Users/yuantian/Developer/tim-professional-workflow/docs/TIM-PROFESSIONAL-WORKFLOW-PROPOSAL.md)
- 📝 **GPT-6 Pro 审查意见全文**：[`docs/TIM-PROFESSIONAL-WORKFLOW-PROPOSAL_REVIEW.md`](file:///Users/yuantian/Developer/tim-professional-workflow/docs/TIM-PROFESSIONAL-WORKFLOW-PROPOSAL_REVIEW.md)
- ⚙️ **上游源同步脚本**：[`scripts/sync-upstreams.sh`](file:///Users/yuantian/Developer/tim-professional-workflow/scripts/sync-upstreams.sh)
- 🔍 **下游版本漂移核验**：[`scripts/check-team-version.sh`](file:///Users/yuantian/Developer/tim-professional-workflow/scripts/check-team-version.sh)
