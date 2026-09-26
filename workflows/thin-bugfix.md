---
title: "Thin Bugfix Workflow · 薄任务配方（缺陷快速闭环）"
project: tim-professional-workflow
version: "1.0.0"
description: "适用于范围清晰、单文件/单函数局部缺陷或微调的极轻量协作路径。"
---

# Thin Bugfix Workflow · 薄任务配方

## 1. 适用场景
- 明确知道出问题的局部函数或单文件逻辑；
- 界面文案修改、微小样式调整、单接口轻量字段修复；
- 不涉及数据库表变更、不涉及跨服务/跨模块公开 API 语义改变。

## 2. 角色精简流水线
薄任务的核心是**省去独立的 Architect 会话，但坚决保留独立 Reviewer 与 Verifier 门禁**：

```mermaid
flowchart LR
    Driver[Driver 派发轻量卡] --> Imp[Implementer 垂直切片修复]
    Imp --> Rev[Reviewer 独立新鲜审查]
    Rev --> Ver[Verifier 反例复现证伪]
    Ver --> Int[Integrator 合入基线]
```

1. **Driver**：
   - 提取 3-5 行清晰的预期行为和允许写入的文件；
   - 直接派工给 `Implementer`，跳过重量级的架构方案对比；
2. **Implementer**：
   - 编写 Failing Test 捕捉该 Bug（确保测试能复现该错误）；
   - 在规定文件内用最少改动使测试转绿；自测全过；
3. **Reviewer**：
   - 独立新鲜上下文，审查 Diff 是否引入了新的坏味道或未捕获的边界；
   - 给出审查结论（无 P0 则通过）；
4. **Verifier**：
   - 运行真实端到端测试，证明 Bug 确实被修复，且相关核心链路未受负面影响；
5. **Integrator**：
   - 确认双方 PASS 凭据，合入目标本地集成分支。

## 3. 动态升级机制（Thickness Escalation）
若 Implementer 或 Reviewer 在处理过程中发现该 Bug 实际上源于“两个模块对同一个状态的争抢”：
- **立即中断薄任务**；
- 报告 Driver：“发现隐藏的跨模块状态冲突，申请升级为厚任务”；
- 转入 `workflows/thick-cross-boundary.md`，调起 `Architect` 重新设计边界。
