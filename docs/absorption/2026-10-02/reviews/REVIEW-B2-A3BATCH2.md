# REVIEW-B2-A3BATCH2

tpw-absorb-gate，2026-10-02。固定candidate `f71138bb1340e9e19ab4c8b2d243a85ed4923a78`，base`d3aab6ad30f36789664287f304e4e91ffd61d96a`；本次新增范围为`11136ebfb101b5f96e9cb65d862ba9af2389ed15..f71138b…`。结论：**第二批需修2项；第一批R1/R2/R3继续未关闭。**

以git show/diff核两个新正文和elicitation扩展，`git diff --check`通过。只评固定commit，未把作者工作区未提交修复当证据。源与产品基线已在REVIEW-A2R-CURSOR-ABC直接核回；新表述对照该裁定，未代写。

## 新R1 · rationale搜索停止规则仍是全扫约束

位置：`methods/rationale-and-premise-review.md` §Trace and search第9项。

前句说按任务/access/resource scale，后句却只准no access或provably irrelevant两个跳过理由（high bar）。未授任务需要以外的调查不能因尚未证明irrelevant而默认搜；资源停止/已足够的具体答案也应可明确记录。与裁定“无每次七类全搜索”的操作相冲突。

最小修：以当前问题需要/承重claim与有效scope为准选择来源；已足够、资源边界、非本次所需、不可访问/未搜索均如实列理由/覆盖限制，不要求证明其绝对无关。不可把未搜称无结果或Unknown的已查事实。现有证据复用、Direct/Supported区分、平衡census仅反驳tested-skew、历史不是当前接受constraint均保持。

## 新R2 · CLI例子错误不能定位缺参

位置：`methods/agent-facing-cli-contract.md` §Examples“Headless missing input”。

例子说`mycli deploy`缺`--env`，返回却是“No image tag specified”；读者无法判断契约在示范哪个required flag，违背本方法actionable error的承诺。不是自动test需求，是正文反例本身不成立。

最小修：将缺失参数、error及修复invocation一致对应（env或tag选一），示例足以检查headless非零且不等待。无头/TTY区分、适用stdin/positional、重试语义及dry-run效应/force不授权限都已成立；无新增普遍validator/gate。

## 其他结论与旧项

- elicitation的Facts/choices与原型扩展符合已裁MG-2：可逆不授权，事实量不裁value，reuse、scope、matching surface及真实实现不同已清楚。
- 第一批“chosen recommendation决定答案”仍在扩展后的第11项，未因renumber关闭；其vendor-A反例与agent-text两finding按原review等待新固定修复。新的范围通过不等于wholef71138b可集成。
- 两新方法没有新增Profile指针；Driver已持methods README集成写面，需补真实消费者和固定version。新rationale非F比较方法，CLI归B；不得填到tools权限字段冒作合同。
- 未执行CLI/真实历史检索或效果experiment；正文PASS只限审查正确性，不能声称已验证运行收益。

B修正后只复核新R1/R2及受影响消费者，旧3项另以新fixed对象复查。
