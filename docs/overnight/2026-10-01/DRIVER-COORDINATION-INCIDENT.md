# Driver 协调中断：事实与恢复

Oracle 2026-10-01 应 Owner 要求诊断。此记录属于本次 harness 执行证据，不进入工具无关 core。

## 已确认事实

- Driver 仍为 w27:pD 的 Codex gpt-6-luna/xhigh，前台 PID 86526；实际进程环境 HERDR_ENV=1，workspace w27、tab w27:t1、pane w27:pD。
- Driver 原始调用（2026-09-30T19:12:24Z，call_585LZrOQtiOXUu9C487iZoJa）把 `test ... && herdr agent list` 与其他读取并行，输出仅打印结果文本／异常字符串，未保留各调用的 exit_code。
- 对应返回为 `Error: Os { code: 1, kind: PermissionDenied, message: "Operation not permitted" }`。该输出不能证明 HERDR_ENV 为空或 test 已失败。
- Driver 随后把未证实的环境归因写入 STATUS／DECISIONS，并于 03:52结束本轮；D/E/F 后续固定提示未派发，独立 M3／M6未完成，Pro0/2未用。没有把可恢复的通信权限错误正确恢复或送达 Oracle。
- 当前 Driver 自己的 exec shell 已观测到四个正确字段，parent PID=86526，退出0；不是前台脱离 Herdr。
- Oracle 的独立对照：环境 test 退出0；第一次非提升 Herdr 调用返回 Operation not permitted，随后同路径复跑已退出0并返回名册。已获授权的提升调用也能读名册并发送消息。权限拒绝不是当前持续可复现状态，旧日志不足以锁定其最初底层组件。

## 判断

主要问题是把权限／工具错误错误归因为 skill 前置变量失败，并把一次控制路径受阻扩成委托停止；不是已有任务授权不足，也没有证据证明环境注入永久丢失。
尊重 skill、不伪造变量是正确行为；它不能替代拆开操作、保留状态码、在真实身份已成立时走已有批准通道的诊断。
旧版 render／closure／compose 检查被当成新包收口检查也与 Owner 的从零建设方向不符，不作为新包资格。

## 已下达恢复

Driver 拆开环境检查与名册调用保留 exit/stderr；sandbox权限不足时通过已有自动批准的提升调用核对，不能伪造环境或绕过审批。
确认通路后立即送达已固定 D/E/F 任务并核其实际开始，继续未完成的 M3/M5/M6。错误归因以追加更正记录，不改旧决定行。
若真无法恢复，停受阻动作，保全自含阻断，通过可工作的独立会话通知 Oracle；不静默终止所有无依赖工作。
本记录不声称工作已恢复，恢复须有名册／送达／实际工作状态的独立观察。

## 恢复观察

Driver 已分别运行环境 test 与名册查询，均成功；pane读操作的 EPERM 用已有批准通道恢复，未伪设变量或更改账户权限。
已重新启动并派发 `tpw-night-m3-design`、`tpw-night-m3-local-bound-e`，Oracle 单次名册复核二者均为 working；`tpw-night-method` 亦已进入 F 评价工作。
因此协调与任务启动已恢复；这不等于 M3/M6 或晨验目标已完成。后续继续由 Driver 维持，按真实产物再报里程碑。
