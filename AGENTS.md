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
它将业界顶尖工程师开源的工程经验、方法论和工作化脚本（Skills / Rules / Scripts）进行解构、去重、冲突裁决与深度整合，形成一套**与具体业务解耦、可独立版本化、可验证、由现有 Multi-Agent Workflow 调度的角色与方法库**。

## 核心使命

不是建立“二十年顶级架构师”的虚拟人设表演，而是建立一套**独立、可组合、可验证的工程能力体系**：
- **角色（Roles）**：责任与权限入口（回答：由谁判断、输入什么、交付什么、何时停手、绝不越权做什么）。
- **方法（Skills）**：工程问题的解决配方（回答：触发条件、确定性操作步骤、证据要求、典型错误反例）。
- **工作流（Workflows）**：多角色协作网络（回答：依赖顺序、厚薄任务路由、交接契约、独立审查门禁）。
- **项目绑定（Project Bindings）**：注入下游具体项目的事实（回答：项目权威文档、架构地图、启动命令、测试入口）。

“**方法全局，配方本地**”：全局库提供经过检验的工程方法与角色纪律；下游具体项目（如 UCBIP / ekunAi）通过轻量绑定消费，不将项目私有契约反向污染到本全局库。

## 目录职责与架构

```
tim-professional-workflow/
├── AGENTS.md                  # 本仓治理与操作指南（本文件）
├── README.md                  # 仓库概览与快速使用入口
├── VERSION                    # 当前发行的全局能力版本号 (SemVer)
├── docs/                      # 架构提案、设计文档与审查材料
│   └── TIM-PROFESSIONAL-WORKFLOW-PROPOSAL.md  # 提交 GPT-6 Pro 审查的完整架构方案
├── roles/                     # 八个核心工程角色定义
│   ├── driver.md              # 任务组织者
│   ├── investigator.md        # 调查与诊断者
│   ├── architect.md           # 方案与边界设计者
│   ├── planner.md             # 实施方案与切片制定者
│   ├── implementer.md          # 授权内实现者
│   ├── reviewer.md            # 独立对抗审查者
│   ├── verifier.md            # 独立真实路径验证者
│   └── integrator.md          # 集成与意图消解者
├── skills/                    # 整合提炼的可复用工程方法
│   ├── alignment/             # 需求澄清与决策对齐
│   ├── architecture/          # 接口、数据与状态边界设计
│   ├── diagnosis/             # 真实路径追踪与根因归因
│   ├── implementation/        # 垂直切片与行为 TDD
│   ├── review-verification/   # 对抗性审查、影响面证明与验证生成
│   └── meta/                  # 结构化沉淀与规则提炼
├── workflows/                 # 协作协议与厚薄任务配方
│   ├── thin-bugfix.md         # 薄配方：缺陷修复与局部变更
│   ├── thick-cross-boundary.md# 厚配方：跨模块与契约变更
│   ├── read-only-audit.md     # 薄配方：只读调研与架构审计
│   └── handoff-contracts.md   # 角色间交接契约标准
├── upstreams/                 # 只读原始克隆（受 .gitignore 保护，绝不直接修改）
│   ├── cursor-plugins/        # Cursor 官方插件目录 (含 pstack)
│   ├── mattpocock-skills/     # Matt Pocock skills
│   └── addyosmani-agent-skills/# Addy Osmani agent-skills
├── scripts/                   # 上下游同步与质量护栏脚本
│   ├── sync-upstreams.sh      # 上游 GitHub 源同步与 diff 报告
│   ├── check-team-version.sh  # 下游项目版本漂移检测
│   └── lint-skills.mjs        # Skill 格式与反借口规则静态检查
└── evals/                     # 行为评测用例与回归基准
    ├── cases/                 # 历史典型场景用例
    └── run-evals.mjs          # 盲评与基准测试运行器
```

## 本仓工作边界与操作纪律

1. **原始克隆绝不修改（Strict Read-Only Upstreams）**：
   - `upstreams/` 下的子目录仅作为只读参考源。
   - 所有本库吸纳的代码、脚本和文档必须落地到 `roles/`、`skills/` 或 `scripts/` 中，并显式标注上游来源与 commit SHA。
2. **两层同步机制（Two-Tier Sync）**：
   - **Layer 1 (Upstream Ingestion)**：运行 `scripts/sync-upstreams.sh` 拉取最新代码，生成 diff 摘要，由架构师评估是否吸纳演进。
   - **Layer 2 (Downstream Pinning)**：下游项目必须引用固定的 release 版本（或 commit tag），禁止在执行期直接软链接跟踪 `master` 最前沿，防止会话期间规则漂移。
3. **结构化守卫（Encode Lessons in Structure）**：
   - 优先通过脚本、TSV 日志模板、Linter 和静态检查来保证执行纪律，避免无休止地堆砌纯自然语言提示词。
4. **切断自动合入与无授权推进**：
   - 上游 Skill 中的自动 commit、自动 merge 或无确认推进逻辑必须剥离；推进与合入权属于全局 Workflow 中的 Driver 与 Integrator/Custodian。
