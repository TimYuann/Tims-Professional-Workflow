# Gate2 · B3 08dca20 五处定向复核

2026-10-02，tpw-absorb-gate2；候选作者身份不变，沿 REVIEW-GATE2-B3-016e004 的 finding 与已过 C5/C7/J1/J5，不重置轮次。

对象 `08dca20b29f4bce2aecc73ce5ad39de7d4a92f24`，唯一父 `016e00402c0cc29aee3556186a6cc425de746951`；delta 仅原五文件 +26/-18，git diff --check 无输出。只读固定差分和受影响相邻语义，没有读在飞正文。

**四项 PASS 并关闭；B3-C3-data 大部修复，仍有一个 backfill 并发残余，deprecation 新版本暂 held。**

| 原 finding | 复核结论 | 理由/边界 |
| --- | --- | --- |
| B3-C1-scope | 关闭 PASS | §1–3 contract/verification 与 §4–9 retry 可独立选；无 retry 只排幂等支线，不强迫 stable function 建 doc/schema/key。J1 实质通过保持。 |
| B3-C4-recovery | 关闭 PASS | 分开缺 staged/flag-off 与真实 redeploy/forward-fix/restore；需实际观察，否则只是计划，不推导所有恢复不可能。数字/授权/数据恢复边界保留。 |
| B3-C6-policy | 关闭 PASS | copies/retention/legal basis/consent 条件化，findable/erasable 与 telemetry保护保留；合法 system prompt 可在所需上下文使用，敏感内容不得下放；合法 validated 参数与 raw sink 分开。J5 身份/target/观察边界未弱化。这里不认证具体法律义务或风险接受可替法律。 |
| B3-C9-source | 关闭 PASS | Chrome 源页 expected 表述保真，未认证完成/用户收益；先前取回官方页可复用，无需再联网。vendor/version/security-cache policy 边界不变。 |
| B3-C3-data | 部分关闭，残余见下 | adds compatible-not-free、活 writer/旧版/后台、切读一致、contract 读写/回退版本以及 mixed-run stale writer 反例均已补；但 backfill 与合法 concurrent dual-write 的一致性仍被 OR 省掉。 |

## B3-C3-data-rest：全体双写不等 backfill 并发安全

固定 `deprecation-and-migration.md` worked shape 第3步：要么 every writer already writes both，**or** copy has consistency/catch-up rule。第一分支仍把兼容 writer 当作充分条件；尾部反例说 backfill with consistency 不能撤掉具体操作中的 OR。

区分反例：所有活跃 writer 都已双写；backfill 先读 name=A，应用随后原子提交 name=B/full_name=B，backfill 再按旧快照写 full_name=A。现在两列不一致，且没有任何旧 writer。全体兼容解决的是旧 writer 漏写，不解决 backfill 与新 writer 的顺序/快照竞争。

最小修：writer 兼容/能覆盖其 gap 的协调，与 backfill 自身并发一致性都要满足，不能二选一。用实际 engine/事务/条件更新/版本检查/追赶或冻结等能说明的方案；“只填 new column unset + final pass”只是需声明/验证实际保证的例子，不认证普遍正确。切读前一致核对仍保留，不用反复查整表替代运行期间协调设计，不要求某特定 DB 或平台。

无需新承重读源即可判此反例；已有源 expand/contract 与本次数据竞争推导分开，未执行 engine/runtime，不能认证其实现收益。

Driver 下一合法动作：从 08dca20 串行采用 interface/release/trust/performance 四已过新正文，加前笔 C5/C7；deprecation 原作者只修第3步的一致性残余后再给固定对象。C1/trust 目标已过，可与 B2@4f86ae7 external + 已过 positioned guide 一起配对消费，引用依赖因此可闭合；仍核实际集成字节与目标存在，不由单件 PASS 自动整体接受。review 提交由 Driver 保全。
