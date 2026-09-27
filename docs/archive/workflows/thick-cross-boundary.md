---
title: "Thick Cross-Boundary Workflow · 厚任务配方（跨边界设计与实施）"
project: tim-professional-workflow
version: "1.0.0"
description: "适用于涉及跨模块通信、共享状态归属变更、数据库 Schema 演进或公开接口调整的重型工程任务。"
---

# Thick Cross-Boundary Workflow · 厚任务配方

## 1. 适用场景
- 涉及两个以上核心模块间的契约或通信协议调整；
- 共享状态的写入权归属重新划分；
- 数据库 Schema、持久化层结构演进；
- 重构现有复杂流程、拆分大型服务或实现全新的业务特性。

## 2. 全链路 9 角色严密协作流

```mermaid
sequenceDiagram
    autonumber
    actor Driver as Driver (统筹)
    participant Inv as Investigator (因果归因)
    participant Arc as Architect (方案设计)
    participant Orc as Oracle (人类代理人)
    participant Pla as Planner (任务切片)
    participant Imp as Implementer (垂直实施)
    participant Rev as Reviewer (对抗审查)
    participant Ver as Verifier (真实证伪)
    participant Int as Integrator (基线集成)

    Driver->>Inv: 派发调查 (还原真实路径与历史原因)
    Inv-->>Driver: 交付零假设客观事实报告
    Driver->>Arc: 派发设计 (先写调用者代码, Design-It-Twice)
    Arc-->>Driver: 交付 2-3 种方案对比 (含不改基准)
    alt 方案存在体验或业务偏好取舍
        Driver->>Orc: 调起 Oracle (代表人类进行品味裁决)
        Orc-->>Driver: 交付意图仲裁卡
    end
    Driver->>Pla: 派发切片 (Tracer-bullet 切片与量化门禁)
    Pla-->>Driver: 交付实施任务卡序列
    loop 每个 Tracer-bullet 切片
        Driver->>Imp: 派发实施 (指定文件白名单)
        Imp-->>Driver: 交付 Diff 与自验通过日志
        Driver->>Rev: 派发对抗审查 (Fresh Context, P0/P1/P2)
        Rev-->>Driver: 交付审查 Verdict
        Driver->>Ver: 派发独立验证 (真实端到端路径, 变异证伪)
        Ver-->>Driver: 交付三态证据 (PASS / FAIL / UNVERIFIED)
        Driver->>Int: 授权合入集成分支
        Int-->>Driver: 合入完成, 交付新基线
    end
    Driver->>Driver: 全局收口, 准备晨会汇报材料
```

## 3. 厚任务硬性约束
1. **接口先行**：未产出经批准的强类型接口草案前，Implementer 严禁动工。
2. **切片垂直**：任务必须拆解为端到端可独立运行的 Tracer-bullet 切片，禁止横向堆砌未经验证的中间层代码。
3. **安全前提证明（Blast-radius Proof）**：必须运行真实代码证明改动不会破坏既有外部模块依赖。
