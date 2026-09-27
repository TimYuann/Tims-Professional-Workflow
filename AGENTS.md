---
obsidian-note-type: agents-md
target: any-agent
project: tim-professional-workflow
cwd: ~/Developer/tim-professional-workflow
created: 2026-09-26
updated: 2026-09-26
---

# TIM · Professional Workflow

全局可复用的 AI 工程能力库：**工程经验装进角色，流程薄到只有 Driver 读一份**。与业务解耦、与运行底座解耦、可独立版本化，由下游项目的多会话协作按需取用。

## 核心原则

1. **方法 > 流程**。流程只保证"谁在什么时候把什么交给谁、什么时候必须停、什么时候可以复用旧结论"；判断方法全部在角色文件里。
2. **注入单元就是角色文件**。每个 `roles/<role>.md` 自包含：单独注入一个会话即可开工，不需要另外读别的文件才敢动手。
3. **四层注入契约**。第 1 层工作纪律 + 第 2 层工作方法来自角色文件（工具无关、稳定不变）；第 3 层本轮工作流切片与第 4 层工具安排由 Driver 在注入时附加，**附加内容不得改变角色的纪律与方法边界**。
4. **判断与实现永不合并**。实现某个候选的人，不得对该候选给出审查、验证或复核结论；任何档位都不放宽。
5. **门禁按风险触发，不按文件数触发**。高风险条件见 `pipeline.md §2`；不满足条件就不给小事加仪式。
6. **说人话**。面向人类 Owner 的汇报以"结果与后果"为主；需要时保留准确技术名词，但不用术语替代事实。
7. **记录分歧与出处**。机制来自哪里、改写了什么、删了什么，写在 `SOURCES.md`；三仓立场不一致处逐条单选裁决，不写"综合两者"。
8. **决定者、权威位置、写者分别点名。** 同一含义不在多处各自设值；**收件四步＝清点、核对、缺则退回、齐则开工**。角色单文件开工所需的安全规则可以有**登记的内联副本**，维护者改权威规则时要同步复核所有副本。不同角色对同一红灯的**不同用途**（诊断、实现、判据审查、独立验证）不算竞争定义。来源台账记录出处，不自动变成第二个规则仓库；生成视图不得手工维护。

## 目录职责

```
tim-professional-workflow/
├── AGENTS.md        本仓治理与操作纪律（本文件）
├── README.md        概览：给谁用、底座需要哪 4 个原语、三档位怎么选
├── VERSION          版本单一来源（SemVer，唯一）
├── pipeline.md      Driver 唯一读的流程：交付链/档位/硬边界/依赖/并行/写窗/停止/证据复用/汇合/授权
├── closure.md       闭环矩阵：字段级闭环 + 每条可跳过路径的职责移交
├── SOURCES.md       上游吸收台账 + 冲突裁决表 + 引文审计处置 + NOT ABSORBED 清单
├── identity.md      对象身份的维护者规范（唯一真源）
├── roles/           10 个角色文件（driver/oracle/investigator/architect/planner/
│                    implementer/reviewer/verifier/integrator/ledger-custodian）
├── scripts/
│   ├── check-library.py        只读自检：结构、闭环、矩阵、身份、死链、版本单一来源、底座解耦
│   ├── ws-identity.sh          无版本历史时的对象身份（ws:v1）
│   ├── identity-selftest.sh    身份实现的正负夹具（可失败）
│   ├── log-decision.sh         append-only 决策台账 logger
│   ├── decision-log-template.tsv  台账表头
│   └── sync-upstreams.sh       Layer 1：上游同步与 diff 摘要
├── docs/            设计背景、历史评审、归档
│   ├── TIM-PROFESSIONAL-WORKFLOW-PROPOSAL.md         设计背景（非权威）
│   ├── TIM-PROFESSIONAL-WORKFLOW-PROPOSAL_REVIEW.md  历史评审
│   ├── TIM-PROFESSIONAL-WORKFLOW-PROPOSAL_REVIEW_R2.md 历史评审（Owner 未跟踪文件）
│   └── archive/     被替换掉的旧载体（workflows/ 与旧 skills/），保留供追溯，不再被引用
└── upstreams/       只读原始克隆（受 .gitignore 保护）
    ├── cursor-plugins/          含 pstack
    ├── mattpocock-skills/
    └── addyosmani-agent-skills/
```

## 本仓工作边界与操作纪律

1. **只读上游绝不修改**：`upstreams/` 只作参考源；机制吸纳后落在 `roles/`、`scripts/`，并在 `SOURCES.md` 登记来源文件与行号。吸纳前必须读正文——**没读过正文不算吸收**。
2. **两层同步**：Layer 1 用 `scripts/sync-upstreams.sh` 拉取上游并生成 diff 摘要。Layer 2：本库发布版本以 `VERSION` 为单一来源，发布标签与该值对齐；下游必须**按固定 commit 引用** release——不许跟随可变分支、不许执行期跟踪可变目录、不许用复制品；并确保**本次实际读取的对象与 pinned commit 一致（checkout 必须干净）**：固定 commit 只锁 Git 对象，**不自动锁执行中实际读取的工作区**。**本库当前不提供漂移检测脚本**；绑定格式与消费者确立后，由下游绑定负责人落实快照核验。
3. **证据绑定对象与三态判定**：验证结论绑定精确的提交对象与运行环境；结论只有 `PASS` / `FAIL` / `UNVERIFIED` 三态，环境故障严禁冒充 `PASS`，也不得直接判成产品缺陷。
4. **按因归属返工**：不把所有失败推给实现者。实现偏差 → Implementer；设计内在矛盾 → Architect；切片或依赖问题 → Planner；验证夹具或环境问题 → Investigator / Verifier；业务取舍 → 独立复核或 Owner。
5. **底座解耦**：本库内容只声明"需要什么能力、需要达到什么效果"。具体运行方式由 Driver 附加的第 4 层提供，不写进本库。
6. **改动先自检**：改本库的角色/契约/来源时，维护者跑 `python3 scripts/check-library.py` 并在交付中附其输出；它只兜**结构与确定性回归**，**不是角色工作流的 PASS，也不检验某次交接物的真实值**——某次交接由收件人按角色文件 §2 核实。上下文压缩后先重读角色/当前任务与最后接收的实际产物；只有继续改本库时才重跑库级检查。
7. **证据与摘要一致**：报告里的每一句都要能在证据里找到对应；找不到就删掉或改成"未验证"。
