---
name: professional-workflow
description: "TIM Professional Workflow 全局入口技能。引导 Driver 执行环境能力探测、与人类大白话对齐波次目标与越权预案、自适应文档体系并装配 9 大核心角色。"
version: "1.0.0"
leading-words: ["wave kickoff", "capability negotiation", "speak human", "worktree isolation", "professional teams"]
---

# Professional Workflow · 全局入口技能

## 概述
当任意 AI 编排主控（Driver）开始接手项目任务或启动一次无人值守/过夜波次时，首先加载并执行本技能。本技能向大模型注入顶尖工程师的系统性组织方法，指导 Driver 完成**环境探测、纯大白话人类沟通、模型能力分配、动态越权预案与 9 大专业角色派发**。

## 操作规程（Step-by-Step Process）

### 步骤 1：环境原语探测（Pre-flight Capability Negotiation）
探测当前开发环境的技术条件，形成本轮装配决策：
1. **会话控制能力**：
   - 是否支持通过工具动态创建、关闭、恢复终端/会话（如 `herdr`、`pi intercom`、`orchestra-dsh`）？
   - 若支持，走动态多会话管理；若只支持平台内置子代理（如 Subagent Teams），走平台团队模式；若只能依赖单一上下文，走轮换装配模式。
2. **消息路由能力**：
   - 检查 Agent 之间是否可以直接发送定向消息（A2A Message）。
3. **隔离工作区支持**：
   - 检查当前环境是否支持 Git Worktree。若支持，确认启用越权隔离试验机制。
4. **模型矩阵盘点**：
   - 扫描当前可用的模型列表与推理（Reasoning Effort）档位。

### 步骤 2：对齐人类 Owner（铁律：必须说人话！）
**绝对禁止使用任何技术黑话或 AI Agent 术语与人类对话！**
采用纯自然语言大白话多轮对话，向 Owner 汇报并锁定：
1. **本波次目标**：“今晚主要解决哪几个具体问题？”
2. **修改权限边界**：“允许改哪些功能模块？哪些核心文件绝对不许动？”
3. **模型分配建议**：“建议用高推理模型守护架构与审查，普通模型写代码，您看合适吗？”
4. **动态越权预案**：“如果夜间调查发现必须做大架构重构，我们会自动在独立测试分支上完整做完试验，绝不碰主线代码，明早向您汇报结果，这样定可以吗？”

### 步骤 3：自适应项目文档体系
检查当前项目（CWD）的文档状况：
- **模式 1（已有完备文档，如 UCBIP）**：直接读取项目的权威入口（如 `CONTEXT.md`、`project-current-state.md`），自动适配已有任务卡与证据账本，绝不强行制造第二事实源；
- **模式 2（文档缺失或散乱）**：礼貌向 Owner 提议：“发现当前项目缺少统一的决策记录和验证账本规范。是否允许我们为您引入一套轻量规范，方便后续追溯？” 征得同意后引入标准模板。

### 步骤 4：装配 9 大核心角色并按厚薄路由派发
根据任务风险特征选择流转路径：
- **薄任务（局部 Bug / 小微调）**：调起 `roles/implementer.md` ➔ `roles/reviewer.md` ➔ `roles/verifier.md` ➔ `roles/integrator.md`；
- **厚任务（跨边界大改）**：调起 `roles/investigator.md` ➔ `roles/architect.md` ➔ (必要时调 `roles/oracle.md` 做品味仲裁) ➔ `roles/planner.md` ➔ `roles/implementer.md` ➔ `roles/reviewer.md` ➔ `roles/verifier.md` ➔ `roles/integrator.md`。

---

## 典型自欺与反辩解表（Common Rationalizations & Red Flags）

| 典型借口 / 行为偏差 | 严厉反驳与纠偏纪律 |
| :--- | :--- |
| “为了显得专业，我把 AST 解析和 Context Compaction 讲给人类听” | **红线违规！** 人类要的是业务确定性，讲黑话是不懂用户需求的典型表现，必须转译为“用户操作后系统做了什么”。 |
| “既然人类睡着了，我就在主干上顺手把这个大架构也改了吧” | **绝不允许！** 必须开辟独立 Git Worktree 进行隔离试验，主干代码保持纯净。 |
| “这个 Bug 很好修，我一个人包揽代码、审查和 Git 提交就行了” | **单体自审陷阱！** 实现者不能做最终验收者，必须移交给独立 Reviewer 和 Verifier。 |

---

## 完成退出判据（Exit Criteria）
- [ ] 当前环境能力与可用模型探测完毕，并形成清晰分配方案；
- [ ] 人类 Owner 用大白话对齐了波次目标、边界与越权预案；
- [ ] 任务被准确打上“薄任务”或“厚任务”标签，并完成第一个角色的派发。
