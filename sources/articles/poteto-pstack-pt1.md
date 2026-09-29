---
id: article:poteto-pstack-pt1
title: The Complete Guide to pstack Pt. 1
author: poteto
original_url: https://x.com/poteto/status/2094457600259842065
read_url: https://threadnavigator.com/thread/2094457600259842065/
retrieved_at: '2026-09-30'
capture_sha256: 5438351359c5b7fadfffb0b1d7fa9648b18ba8eb90a8018ab5f15bee6f648bd5
original_verified: false
---

# Part 1 · 验证基础设施

这份记录保存文章的来源身份与方法摘记，不复制原文。读取的是第三方镜像；尚未逐字核对 X 原站。原始链接、读取链接和缓存摘要在上方元数据中；逐项对照留存在本库开发历史，不是下游使用时的依赖。

## 可迁移的方法

- 把验证当作 agent 可反复使用的工程能力：能启动目标、沿真实用户路径操作、观察动作及副作用，并留下可复核证据。
- 优先复用项目已有驱动设施。缺少时，为重复的操作建立小型命令入口；命令应能组合，危险动作可预演，错误指出下一步，顶层和子命令各有适合其层级的帮助，输出足以供机器读取。
- 能力地图从用户视角写入口、驱动动作和可观察终态。系统变化后，重新核对源码与现场行为，区分地图漂移、验证工具失效和产品回归。

文章还推荐特定云端 agent、机器快照和并行方式；这些是运行环境选择，不作为 TIM 的调度规则。上述方法与本库已吸收的 pstack 验证技能交叉，新增的命令可用性要求由 `verification-suite` 承接。
