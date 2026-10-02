# Gate2 · B3 ABC8 与 EF performance 两笔定向复核

2026-10-02，tpw-absorb-gate2，非正文作者。对象1 `76976e21e219742fe6c0230d27d66cfeb72e92f6`，唯一父 `98ba9b4d4d3d553b5642d5861071e37a11deb788`，仅performance +43/-6；对象2 `56e4b6431c69ff33af410bf66ae734ba27cba61c`，唯一父76976e2，仍仅performance +10/-7。两真实父diff --check无输出，固定字节/新与受影响claim，旧C9/C3与七文件已过段不重开。

独立回源复用本轮已直接读Cursor hillclimb/perf-issue、Addy performance/checklist与对应ABC8/EF-addendum裁定；作者ABC8只读裁定/摘要的经历照实保留，不冒称作者直接全文回源。EF作者声明直接读checklist，仅在实际source/贡献记录内计其该部分；文本PASS不算实验或整篇运行资格。

## 76976e2：大部符合，两个新增范围待限缩

workload/replicatingcase、适用metric/真实target与资源stop、harness信号/量尺改变保baseline、warmup/cache/order/sample/noise/负控制、既有计时/log/query可用、捕获条件/版本、八族机制而非固定taxonomy、cache/invalidation、indirection净成本、hedging的副作用/资源、lazy/schedule真实交互/延期成本、onehypothesis/probe与联合归因限制、wrong-surface/inconclusive不PASS、记录actualobject/命令/threshold/限制、validprior复用、授权内revert/instrument及合法stop都**内容PASS**。无N/attempt/PR/freeze硬门槛，非性能metric不塞此方法，未造runner/第二perf平台。

### B3-PERF-EVIDENCE

Ground the workload第6条：“A single run is a sample, not a measurement”。一次run仍是对实际对象/条件的测量；其不足是通常不能独立推出稳定/全负载改善，不是没测量。反例：固定输入的trace计数确认这一run的请求从100次变1次，它是有效的该条件下operation-count measurement；不能把它升级全部用户延迟，但也不能因没有N而抹掉该事实。

最小修：单run是一个已观察样本/测量，是否充分取决于claim、已知噪声/确定性与覆盖；统计稳定收益按适当重复和条件采证。保N-median不充分/不普适、无fixedN与原noise段，不引入新数字/测试或取消可靠性要求。

### B3-PERF-RECALL

八族后句“A change that reaches across a module or interface boundary returns to its D/B/C owner”会把所有已授权跨模块实现也列return，虽后句ordinaryfunctioncall免designreview仍未区分真正commitment变化。反例：D已授权一套batching安排，E在两个module内部按既定接口实现，不改变sharedcommitments/语义/验证依据；仅多个module不产生新的B/C/D取舍或ACK。

最小修：按实际受影响/将改变的domain/sharedinterface/兼容/既定technicalcommitment及envelope路由；已有有效委托内、保持这些约定的cross-module/internal实施可继续。保性能loop不能自改上游/扩大权限，不改旧domain R2等已关结论、不需新actor/approvalgate。

## 56e4b64 EF增量：新细节PASS，整文件仍继承上两处held

- P3全resource/competition/headroom、合法分池、holder先诊断、boundedwait按SLO、autoscale admission/proxy transaction/session适用保留，未固定参数或宣自动安全。
- P4 authoritativeabsent不同error/timeout/权限mask/unknown，source失败不缓存成persistentnotfound；negative窗口按创建可见/abuse/load/authorization，不固定短于positive。
- P5key内coalescing/失败cleanup/boundedwait、局部vs共享范围、SWR不违freshness、锁owner/fencing/timeout需真保证、caller放弃≠fetch取消、snippet非全安全都具体。
- P7baselineplan/actualparams/data/engine/load/stats、writecost及cover/partial/expression/fulltext条件、unchangedplan非自动撤或无价值、drop-index检查constraint/consumer/permission、EXPLAIN ANALYZE可能执行、无授权能力记未核正确。索引例按实际query/engine/coverage读，不推广任何单个signal为普遍收益保证。
- P6cost/ratio/eviction/hitrate非绝对价值、otheracceptedpurpose及维护；P8真实viewport/font/load/sideEffects非强设；P9三段交互/representativecondition/CPUthrottleproxy、无强RUM-first正确。P1/P2等价key/namespace/明确策略组合/staleowner与跨store写并非原子补强不重定义其业务contract，C1/trust互指按已过目标存在。
- 所述依赖/参数/CLI/矩阵都尚需实际system验证，无当前政策/运行资格；sourceanchors正确，S1/S2/O2未再次重写或计增量。

Driver下一合法动作：原作者只修performance上述两个ABC8句群，给基于56e4b64的新fixed对象；EF新增内容专业通过保全，避免整轮重做/重开旧C9或Oracle源裁。当前769/56整文件不可直接全替换旧通过版；修复关闭后可将ABC8+EF同一carrier串行消费。无实际DB/browser/Provider/model/性能效果run，无新权限/整体接受，review由Driver保全。
