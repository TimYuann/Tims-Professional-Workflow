# Gate2 · B1/B2 定向关闭与 positioned 依赖

2026-10-02，tpw-absorb-gate2；仅复核原 finding 的新固定 delta，延续先前轮次/贡献身份，不重审已过 guide 专业正文。

**PASS：B1-J1-boundary、B2-EXT8 全部关闭；既有已关 finding 保持关闭。**

- B1 `d1eed24788cb33982d4c36f6eb7c2bacbd5fcc9d`，唯一父 `c537ed042b25abc601774cb1ada671496fbd8e6f`；delta 仅 domain-state 两处。依赖不变量的执行/安全决定前检查，诊断读取允许且披露范围、不推出全安全/全终止；只拒未填结构/未声明 magic absence，合法 unknown enum/字面 {{customer}} 保留，不二次解释插入文本。符合回核过的 schemas 部分读取及 prompts 限缩；结构绿/语义错、名称/权限、生成视图与独立性边界未弱化。
- B2 `4f86ae7bf0727056101f447d600334872579dd26`，唯一父 `eb24161b74c203888a3e755adcee729a4c7b5295`；delta 仅 external-tool-operation 第8项。pagination/bulk 估算、限范围/stop、跟踪消费；缺授权/超成本或 scope/真实 provider-host 政策才回相应 authority，已有授权不额外 ACK。第4项真实支付/host批准边界未改，观察/未知/partial-success 不变。符合已回源的 THIRD-PARTY 限缩，无新 cost gate。

两笔 git diff --check 无输出，真实父/delta 路径已核，不用作者 mutable 更新。源裁定不重复；未执行 runtime/外部动作，不报实际效果或完整集成接受。

**positioned 依赖裁定：随对装入即可，无需改指。** `guide-positioned-artifacts.md` 的 Use、第16项和 Source anchors 都引用 external-tool-operation 的操作序列/真实host证据，新的第8项不改变这些承诺；文件在 B2 修复对象中未改，guide 专业 PASS 保持。当前 core 尚缺目标时保持 held 正确；Driver 将修后 external 与 guide 配对串行装入同一固定整合对象即可。external 的 interface-contract-and-retry/trust-boundary-and-actions 指针仍需相应目标通过一起装入（B3 受影响两目标随后定向审），不能用复制权限正文或指向没有这些操作内容的泛化原则掩盖缺依赖。

Driver 下一合法动作：采用 d1eed24 的 domain-state delta、4f86ae7 的 external delta及既有通过文件；上述依赖满足后将 positioned/external 同对象消费。只核新集成字节/引用，不重开 guide 内容或旧 findings。review 提交由 Driver 保全。
