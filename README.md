# TIM · Professional Workflow

本仓默认分支 `main` 是 **2026-10-01 夜间完成并通过 Oracle 接受的新版 Professional Workflow**。
旧版（registry / roles / skills / principles / scripts 体系）不再位于默认根，其完整工作状态保存在本地 worktree
`.worktrees/legacy-pre-night-2026-10-01`（本地分支 `legacy/pre-night-2026-10-01`，HEAD 为旧 `main@496b067`）。

## 新版是什么

一套与工具无关的专业判断装配：**意图 → 责任边界 → Profile / Instance Charter / 方法 → 交付证据**。
它提供工程方法、责任语汇与装配顺序；不提供调度，不产生任务授权、执行许可或风险接受。

## 最短使用路径

1. 读 `docs/WORKFLOW-INTENT.md`（上层意图与术语）和 `docs/RESPONSIBILITY-BACKBONE.md`（责任边界接受冻结源；
   包内 `professional-workflow/authority/RESPONSIBILITY-BACKBONE.md` 是同字节的静态导出，不得手改）。
2. 在 `professional-workflow/profiles/` 选择 Profile；按 `professional-workflow/charters/README.md` 填本次 Instance Charter；
   按 `professional-workflow/methods/README.md` 只绑定任务需要的方法。
3. 按 `professional-workflow/README.md` 的装配顺序生成任务启动文本；任务输入携带当前事实与固定引用。
4. 交付状态、接受与证据入口：当前接受为 `docs/absorption/2026-10-02/FINAL-ACCEPTANCE.md`（2026-10-03，Pro #2 PASS）；历史过程与证据在 `docs/overnight/2026-10-01/` 与 `docs/absorption/2026-10-02/`。

## 已接受身份与状态（本地）

- 2026-10-03 Oracle 最终接受三仓实质吸收（bounded cross-repository adoption；Pro #1 RETURN → 三项修订 → Pro #2 PASS）：`docs/absorption/2026-10-02/FINAL-ACCEPTANCE.md`（接受对象 product `8ba69427105d09b3efa1d3a5f28182d4243b5fea` / core `d0cbbfc8b56f588c183efdf8b6d503d9131b5f58`；状态同步对象另记新 Git 身份）。
- 2026-10-02 Oracle 接受修正后的首版（bounded usable first edition）：`docs/overnight/2026-10-01/ABSORB-FINAL-ACCEPTANCE.md`（reviewed source `16c554de`；最终整合身份见 `ABSORB-CORRECTED-CORE-MANIFEST.md` Rev.7 与 `ABSORB-FINAL-INTEGRATION.md`）。
- 跨仓接入与使用：`professional-workflow/ADOPTION.md` 与 `adoption-examples/cross-module-start.md`（其他仓库如何固定版本引入/使用 TPW）。
- 2026-10-01 Oracle 接受有界本地采用交付（bounded local-adoption delivery）：`docs/overnight/2026-10-01/M6-FINAL-ACCEPTANCE.md`（前序）。
- 修正后的交付身份与 R1/R2 独立结论：`docs/overnight/2026-10-01/PW-01-FINAL-REPORT.md`。
- 本次主线切换与新旧对象：`docs/overnight/2026-10-01/MAIN-CUTOVER-REPORT.md`。
- 接受只覆盖本仓交付内容；下游（如 UCBIP）的采纳、任务接受、动作授权与关闭归其有效委托责任方。

## 旧版归档入口（只读）

旧版完整工作状态（含切换时的 staged / unstaged / untracked 字节与 `upstreams/` 原始参考）在
`.worktrees/legacy-pre-night-2026-10-01`；旧提交历史保留在本地分支 `legacy/pre-night-2026-10-01`。
可按需读回旧脚本与历史证据；不要把旧 registry/roles/skills/scripts 当默认治理，也不要在新根恢复旧体系。
