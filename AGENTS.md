---
obsidian-note-type: agents-md
target: any-agent
project: tim-professional-workflow
cwd: ~/Developer/tim-professional-workflow
---

# TIM · Professional Workflow — 当前根维护纪律

本文件短、稳定、项目专属。全局行为规则见全局 `AGENTS.md`，不在此重复。
本仓默认 `main` 是 2026-10-01 主线切换后的新版；旧的 registry / roles / skills / principles / scripts 体系已退役出默认根。

## 当前唯一入口与归属

- 入口：`README.md`（最短使用路径、接受状态、旧版归档指针）。
- 目标与术语（可维护）：`docs/WORKFLOW-INTENT.md`。
- 责任边界：`docs/RESPONSIBILITY-BACKBONE.md` 是唯一可编辑的接受源；`professional-workflow/authority/RESPONSIBILITY-BACKBONE.md`
  是其静态冻结导出，**不得手改**；需要变更时先改源、接受后重新导出。
- 方法装配：`professional-workflow/profiles/`、`charters/`、`methods/` 各自拥有正文；各自的 README 只描述选择与装配顺序。
- 交付状态与证据：`docs/overnight/2026-10-01/`（当前接受记录 `M6-FINAL-ACCEPTANCE.md`）。

## 窄而有效的检查

- 生成任务启动文本前，确认引用的 Profile / Charter / 方法 / 任务输入存在，并以 commit / path / section 固定引用；
  方法正文不产生授权，工具权限不等于动作许可。
- 旧 `workflow/registry.yaml`、`scripts/render.py`、`docs/artifacts.md` 等旧真源/生成器已不在默认根：
  不要求、不查找、不运行；只读历史在 `.worktrees/legacy-pre-night-2026-10-01`。
- 冻结字节核对：Backbone 源与包内导出应为同一 SHA-256；不因旧状态文字重写冻结正文。
- 接受语义变更（方法、责任定义、行为合同）需回到相应责任方；入口/状态文字由集成者按接受记录更新。

## 边界

- 本仓不产生调度权、执行授权、风险接受或发布许可；接受状态不等于下游业务/生产授权。
- 主线本地切换与归档已按 Owner 2026-10-01 授权执行；远端 `main` 推送、tag、release 仍按既有授权边界。
