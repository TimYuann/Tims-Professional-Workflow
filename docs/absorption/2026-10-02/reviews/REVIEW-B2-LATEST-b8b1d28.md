# REVIEW-B2-LATEST-b8b1d28

tpw-absorb-gate，2026-10-02。固定完整对象`d3aab6ad30f36789664287f304e4e91ffd61d96a..b8b1d28f1a50be3f2954c69d17b59fce2435951b`，branch absorb/w2。**整笔需修；第一批R1/R2/R3均关闭**。第二批原2项未修，加prototype证据分类一项。

以git diff/show核完整文件清单9项及`f71138b..b8b1d28`受影响五文件；此前不变正文复用已读结论，git diff --check通过。原vendor-A未接受仍问、no-op显式hypothesis、不可再澄清且已观测rush才分拆均已存在，未因后续重编号重开旧项。未代写B正文；未将未提交修复记作完成。

## 需修三项

1. **原batch2 R1未关闭：**`methods/rationale-and-premise-review.md` §Trace and search第9项仍只准no access/provably irrelevant跳搜，和按task/resource/scope伸缩矛盾。以承重claim所需来源为准，已有足够证据/资源边界/不在本次需要/访问不可得等具体理由可停止或不查，报告其coverage，不把未查当已查无结果。无强制七类搜索。
2. **原batch2 R2未关闭：**`methods/agent-facing-cli-contract.md` §Examples仍称缺`--env`而错误“No image tag specified”。缺参、error、修复invocation对齐即可；不要新建CLI/test基础设施来验证这句示例。
3. **新R4成立：**`methods/decision-elicitation.md:41`、L48（§18/22）把prototype证据一律写local synthetic，不允许按实际输入/runtime/依赖观察区分。源依据与反例见`REVIEW-B1-LATEST-f321c8c.md` §Prototype回源依据：Cursor允许最小脚本真实测behavior/timing，Matt允许scratch DB/现有页面fetch/auth；用途不是证据等级。最小修仅该语义：明确实际来源、环境、覆盖，支持真实观察的窄claim，既不按prototype名一律降级，也不由controlled green升级生产全域；保留throwaway≠生产交付、动作仍需既有授权。

## Batch3与可通过部分

bounded-composition按逻辑写面/共享canonical object/独立事实/单写整合，runtime机制分归D/E；同一文件不同field仍共享、worktree不隔离外部store、未知资源无清理权反例有效。lock/CAS是结构选项非本方法实现义务，task现有安排可足够；未增registry/框架。CLI半途失败/operation identity、behavior条件消费者冲突有归属，未加通用scope validator。

**本candidate以下整文件字节PASS，可由Driver串行集成：**

- `methods/behavior-contract-examples.md`（含消费者段）
- `methods/guide-agent-text.md`（原R2/R3修复）
- `methods/bounded-composition.md`

`rationale-and-premise-review.md`、`agent-facing-cli-contract.md`、`decision-elicitation.md`尚需修。Profile指针本身存在，但部分目标是需修对象；Driver应随目标通过一起集成/固定，不以指针存在宣称目标已接受。F Profile与B1共享指针需串行保全两方，再在集成对象核。methods README已明确归Driver，需补这些正文真实消费索引及当前状态，不要求新的project平台或validator。

未执行真实CLI、原型数据访问、访谈或模型行为评估；正文PASS限此对象/差分的专业正确性，不是运行效果。下一轮只核三修与受影响claim，第一批已关闭结论保留。
