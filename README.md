# TIM · Professional Workflow (Professional Teams & Engineering Kit)

> **全局 AI 软件工程能力库与专业角色套件**
> 独立版本化 · 职责严格隔离 · 方法全局配方本地 · 结构化双层同步

本项目旨在将业界顶级工程师（Cursor 团队、Matt Pocock、Addy Osmani、Dex Horthy、Armin Ronacher 等）开源的工程经验、方法论和工作化脚本（Skills / Rules / Scripts）进行解构、去重、冲突裁决与深度整合，形成一套**与具体业务代码解耦、可被多 Agent 工作流（Multi-Agent Workflow）按需调度**的专业角色套件（Professional Teams）。

---

## 核心设计哲学

1. **四层解耦（Separation of Concerns）**：
   - **角色（Roles）**：责任与权限入口（谁负责判断、谁有权提交、谁独立验收）。
   - **方法（Skills）**：具体技术问题的确定性解决步骤与反欺骗反例。
   - **工作流（Workflows）**：多角色协作网络、厚薄任务配方与交接契约。
   - **项目绑定（Project Bindings）**：下游项目注入的局部事实（启动脚本、端口、权威入口）。
2. **方法全局，配方本地**：
   - 全局库提供经过检验的工程方法与角色纪律；下游具体项目（如 UCBIP / ekunAi）通过轻量绑定消费，不将项目私有契约反向污染到本全局库。
3. **结构化守卫（Encode Lessons in Structure）**：
   - 优先通过脚本、TSV 决策日志、Linter 和静态检查来保证执行纪律，避免堆砌口号式提示词。
4. **两层同步机制（Two-Tier Sync Architecture）**：
   - **Layer 1 (Upstream Ingestion)**：只读跟踪上游 GitHub 仓库，通过 `scripts/sync-upstreams.sh` 抓取变更并生成 diff 报告以驱动能力演进。
   - **Layer 2 (Downstream Pinning)**：下游项目显式声明引用的 release 版本，通过 `scripts/check-team-version.sh` 在执行前检查版本漂移，防止执行期规则突变。

---

## 核心角色编制（The 8 Core Roles）

| 角色 | 核心责任 | 主要交付物 | 绝对不应该做什么 |
| :--- | :--- | :--- | :--- |
| **Driver** | 任务组织、依赖编排、派工与升级处理 | 任务卡与阶段授权 | 包揽重型诊断或实施；擅自篡改产品决策 |
| **Investigator** | 事实归因、执行路径追踪与假设证伪 | 带证据的诊断报告与关键路径 | 顺手改代码；把未经证实的假设当根因 |
| **Architect** | 接口、状态与模块边界设计，方案对比 | 接口草案、替代方案与折中取舍 | 把个人建议当契约；自动进入实施 |
| **Planner** | 实施步骤拆分、Tracer-bullet 切片与验证安排 | 可执行改动配方与验收标准 | 擅自扩大范围或重新设计产品 |
| **Implementer** | 在严格授权范围内完成代码与自测 | 代码变更与开发自验通过证据 | 擅自扩大改动面；自行宣布最终验收通过 |
| **Reviewer** | 独立对抗性审查、坏味道检查与影响面证明 | 明确分级的 Findings 与审查结论 | 为了证明价值制造假阳性；替作者重写代码 |
| **Verifier** | 独立真实路径验证与反例构建 | 真实环境运行证据与反例测试 | 仅凭“测试全绿”等同于业务目标达成 |
| **Integrator** | 按意图解决冲突，维护基线与证据合流 | 集成后的版本与最终验证回执 | 趁合并做新功能；突破既定权限边界 |

---

## 仓库结构速览

```
tim-professional-workflow/
├── AGENTS.md                  # 本仓操作与治理规则
├── README.md                  # 本说明文件
├── VERSION                    # 当前发行的全局能力版本号
├── docs/                      # 架构提案与审查报告
│   └── TIM-PROFESSIONAL-WORKFLOW-PROPOSAL.md  # 提交 GPT-6 Pro 审查的完整提案
├── roles/                     # 8 个核心角色的结构化定义文件
├── skills/                    # 整合提炼的全局工程技能
├── workflows/                 # 厚薄任务配方与交接契约标准
├── upstreams/                 # 只读原始克隆（受 .gitignore 保护）
│   ├── cursor-plugins/        # Cursor 官方插件目录 (含 pstack)
│   ├── mattpocock-skills/     # Matt Pocock skills
│   └── addyosmani-agent-skills/# Addy Osmani agent-skills
├── scripts/                   # 自动化同步与版本审计脚本
│   ├── sync-upstreams.sh      # 上游源拉取与更新检查
│   └── check-team-version.sh  # 下游项目版本锁定核验
└── evals/                     # 行为评测用例与回归基准
```

---

## 详细方案文档

完整架构设计、三仓重叠与冲突的深度裁决细节、外部名家经验吸收方案及 V1 实施规划，详见：
📄 **[`docs/TIM-PROFESSIONAL-WORKFLOW-PROPOSAL.md`](file:///Users/yuantian/Developer/tim-professional-workflow/docs/TIM-PROFESSIONAL-WORKFLOW-PROPOSAL.md)**
