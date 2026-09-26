---
obsidian-note-type: agents-md
target: any-agent
project: tim-professional-workflow
cwd: ~/Developer/tim-professional-workflow
created: 2026-09-26
updated: 2026-09-26
---

# TIM · Professional Workflow (Professional Teams & Engineering Kit)

这是全局可复用的 AI 软件工程能力库与专业角色套件（Professional Teams）的母仓。
它将业界顶尖工程师开源的工程经验、方法论和工作化脚本（Skills / Rules / Scripts）进行解构、去重、冲突裁决与深度整合，形成一套**与具体业务解耦、与具体 Harness 底座解耦、可独立版本化、由现有 Multi-Agent Workflow 调度的专业角色与工程方法库**。

## 核心使命与运行原则

1. **四层分离**：
   - **角色（Roles）**：9 大固定工程职责与负面边界。
   - **方法（Skills）**：具体工程问题的解决配方（含反借口表与退出判据）。
   - **工作流（Workflows）**：多角色协作网络、厚薄任务配方与波次交接契约。
   - **项目绑定（Project Bindings）**：下游项目注入的局部事实，实现“**方法全局，配方本地**”。
2. **“说人话”铁律（Speak Human Principle）**：
   - 任何面向人类 Owner 的 Session 和沟通环节，必须使用纯自然语言大白话讲解系统行为与进展，严禁堆砌 AI Agent 黑话或深层技术行话。
3. **波次起止介入与自主闭环（Wave Model）**：
   - 人类 Owner 仅在波次开始（目标、授权范围、动态越权预案对齐）和波次结束（成果汇报）介入；
   - 波次执行中团队在授权范围内 100% 自主推进、交接与返工，无需人类逐步点击确认。
4. **动态越权 Worktree 隔离机制**：
   - 执行中若发现必须进行超出昨夜授权的架构重构或大变动，系统立即开辟独立的 Git Worktree（`worktree-isolate/<task>`）进行隔离试验；主干继续推进其他已授权任务，晨会向 Owner 交付完整试验成果供决策合并。
5. **项目文档体系双模适配**：
   - 模式 1：下游项目已有完善文档体系（如 UCBIP），自动映射适配，绝不造第二事实源；
   - 模式 2：下游项目文档体系缺失，Driver 征得 Owner 同意后一键引入 TIM 轻量规范文档模板，顺带提升工程治理。

## 目录职责与架构

```
tim-professional-workflow/
├── AGENTS.md                  # 本仓治理与操作指南（本文件）
├── README.md                  # 仓库概览与快速使用入口
├── VERSION                    # 当前发行的全局能力版本号 (SemVer)
├── docs/                      # 架构提案、设计文档与审查材料
│   ├── TIM-PROFESSIONAL-WORKFLOW-PROPOSAL.md         # 终审架构方案 (v1.0-final)
│   └── TIM-PROFESSIONAL-WORKFLOW-PROPOSAL_REVIEW.md  # GPT-6 Pro 审查意见全文
├── roles/                     # 九大核心工程角色定义
│   ├── driver.md              # 统筹调度与人类接口 (说人话)
│   ├── oracle.md              # 人类代理人 / 业务意图守护者 (过夜决策)
│   ├── investigator.md        # 调查与归因者 (零假设原则)
│   ├── architect.md           # 方案与边界设计者 (深模块与方案对比)
│   ├── planner.md             # 方案切片者 (Tracer-bullet 与门禁)
│   ├── implementer.md          # 授权内实现者 (TDD 垂直切片)
│   ├── reviewer.md            # 独立对抗审查者 (分栏 Findings)
│   ├── verifier.md            # 独立真实路径验证者 (反例与变异测试)
│   └── integrator.md          # 集成与意图消解者 (基线维护)
├── skills/                    # 提炼出的高浓度工程方法 (Agent Skills 规范目录)
│   ├── decision-grilling/     # 需求与意图对齐
│   ├── interface-and-boundary-design/ # 接口与模块边界设计
│   ├── system-tracing/        # 真实路径拓扑还原
│   ├── causal-diagnosis/      # 因果诊断与确定性反馈回路
│   ├── behavioral-tdd/        # 行为驱动垂直切片 TDD
│   ├── adversarial-review/    # 怀疑驱动对抗性审查
│   ├── blast-radius-proof/    # 可运行代码证明安全前提
│   └── ...                    # 其他配套技能
├── workflows/                 # 协作协议与厚薄任务配方
│   ├── thin-bugfix.md         # 薄配方：局部缺陷快速闭环
│   ├── thick-cross-boundary.md# 厚配方：跨边界设计与隔离实现
│   ├── read-only-investigation.md # 薄配方：只读诊断与溯源
│   └── wave-execution.md      # 波次启动、动态越权与晨会交接规程
├── upstreams/                 # 只读原始克隆（受 .gitignore 保护，绝不直接修改）
│   ├── cursor-plugins/        # Cursor 官方插件目录 (含 pstack)
│   ├── mattpocock-skills/     # Matt Pocock skills
│   └── addyosmani-agent-skills/# Addy Osmani agent-skills
├── scripts/                   # 上下游同步与质量护栏脚本
│   ├── sync-upstreams.sh      # 上游 GitHub 源同步与 diff 报告
│   └── check-team-version.sh  # 下游项目版本漂移检测
└── evals/                     # 行为评测用例与回归基准
    ├── cases/                 # 历史典型场景用例
    └── run-evals.mjs          # 盲评与基准测试运行器
```

## 本仓工作边界与操作纪律

1. **原始克隆绝不修改（Strict Read-Only Upstreams）**：
   - `upstreams/` 仅作为只读参考源。所有吸纳的方法和代码落地到 `roles/`、`skills/` 或 `scripts/` 中，并显式标注上游来源与 commit SHA。
2. **两层同步机制（Two-Tier Sync）**：
   - **Layer 1 (Upstream Ingestion)**：定期运行 `scripts/sync-upstreams.sh` 拉取最新代码，生成 diff 摘要；
   - **Layer 2 (Downstream Pinning)**：下游项目必须引用固定的 Release Commit 快照，严禁执行期动态跟踪可变目录。
3. **证据严格绑定对象与三态判定**：
   - 验证结论必须绑定精确的 Commit SHA 与运行环境；
   - 结论严格区分 `PASS`（通过）、`FAIL`（失败）与 `UNVERIFIED`（未完成有效验证），严禁环境故障冒充 PASS。
4. **按因归属返工（Cause-Directed Rerouting）**：
   - 绝不把所有测试失败都推给 Implementer；根据失败原因精准分流至 Implementer（代码 Bug）、Architect（设计缺陷）、Planner（切片问题）或 Investigator（环境问题）。
