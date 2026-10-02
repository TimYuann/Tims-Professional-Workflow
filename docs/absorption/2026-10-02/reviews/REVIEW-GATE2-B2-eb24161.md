# Gate2 · B2 eb24161 固定差分复核

2026-10-02，tpw-absorb-gate2，非正文作者；延续 REVIEW-B2-a64bbc2 的轮次、已关 finding 和贡献身份。对象 `eb24161b74c203888a3e755adcee729a4c7b5295`，比较 `a64bbc224a135b38e806853212d361e0249fc7ab`，共同 base `d3aab6ad30f36789664287f304e4e91ffd61d96a`，core tree `8ca96fdf80e81906fdba8da7e022c581a4b3eb1f`。固定 delta 五文件；git diff --check 无输出。没有读取作者在飞正文。

**R4-rest 关闭；第一批 finding、rationale/CLI 已关闭结论保留。四个 delta 文件 PASS；新 external-tool-operation 第8项需定向限缩，整笔不可全采用。** 不重新裁 Oracle THIRD-PARTY/DEF3，仅核其固定落地。

| 机制 / 文件 | 处置、落点 | 理由与边界 |
| --- | --- | --- |
| decision-elicitation §18/22 | 修复 PASS，R4-rest 关闭 | 实际已执行 real leg 支持该版本/输入/范围的窄 provider 或体验观察；未观察部分不可由替身绿替代。throwaway 不等于生产交付或发布授权；不因标签贬掉真实证据。 |
| guide-agent-text，ABC4 MG2/4 与 DEF3 J3 | 合并落地 PASS | 语义保留事实、条件、置信；数字不可捏造，canonical term 不改，未知可保；不复制既有 carrier。装配区分结构缺项与字面量，不二次模板解释，实际 branch/对象匹配委托，relay 是数据不变授权，仍按需指针消费。 |
| agent-facing-cli-contract，DEF3 J4 | 合并落地 PASS | 名称检索明确有窗口/status/list 边界，真实意图/范围决定复用，跨 repo/goal 同名反例能揭错；cancel-running/prune-pending 分开，force 不授重复动作权；无固定 retry 数/窗口。既有缺 tag 修复保留。 |
| guide-positioned-artifacts，THIRD-PARTY | 限缩落地 PASS | Docs UTF-16/exclusive end/重复锚、Sheets 两坐标系及值→格式→图表、Slides objectId/points/布局读与渲染分别有实际操作；revision 拒绝须重读，无 revision 的先读不证明隔离。公式解析按信任边界，固定尺寸/字体/颜色/thumbnail 配额不升库政策。此为 pinned 接口经验，实际操作须核真实工具当前前提。 |
| external-tool-operation，THIRD-PARTY | 大部符合限缩；新 B2-EXT8 未关 | 能力/身份/scope/私有数据路由、按真实 billing 单位估算、partial data/errors、未知不盲重发、real/substitute 分开正确；但分页/批量的普遍 Owner stop 仍照搬源宿主规则，见下。 |

## 新 finding B2-EXT8

`external-tool-operation.md` 第8项写成本越阈值 **or any pagination loop or bulk job** 就 present estimate / wait for owner's decision。Oracle THIRD-PARTY 明确不采固定翻页必回 Owner；Limits 虽说 approval frequency 来自真实政策，仍未覆盖主序列的绝对 stop。

反例：项目已明确授权三页只读提取、总预算与字段范围齐全，提供者无另行批准政策；第二页不因“loop”再停。反向反例：支付 host 有真实每动作批准政策，原授权不能跳过它，正文第4项应保。

最小修：分页/批量需估算、明确有界范围/停止条件并跟踪消费；仅缺有效授权、超现有成本/范围边界或真实 provider/host 政策要求时返回对应 authority。已有授权覆盖的分页/批量不额外索 ACK。仅改第8项及必要一致文字，不改能力/观察/支付边界、不建 cost gate。

## 回源与覆盖资格

本次独立回读 Cursor pinned prototype playbook 全文；orchestrate prompts.ts 1–105、cli/task.ts 478–515；bro/technical-writing/automate-me 所取表达条款沿本轮读取及 ABC4 裁定核，非运行效果认证。THIRD-PARTY 承重回读：X API Cost awareness/Fields pagination/错误与 partial-data 相关段、pricing 计费模型及头部；X Money 批准规则与结果/未知/重试相关段；Shopify rule 全文；Google Docs 定位/范围/revision/结构编辑相关段，Sheets 全文、Slides 1–125；X Chat 身份/密文/权限/出站相关段。截断输出和未读尾部不宣称全文资格，未联网核当前服务规则/报价、未调用真实连接器或支付/文档 API。

candidate 五文件新内容已读；professional-learning 仍为先前固定正文，本 delta 没有新增 ABC4 teaching feedback，不能把 lesson-promotion 指针当作 learning 补正文已落地。原能力/反馈方法的 PASS 保留，增补覆盖单独记未完成，不阻挡其旧已过对象采用。

无补读缺口阻碍本裁定；若扩展 provider 具体行为或当前 pricing claim，须核真实工具/时点/有效政策并作相应观察。

Driver 下一合法动作：从本固定对象串行采用四个 PASS delta 与此前已过文件（architecture 仍用 B2 canonical），external-tool-operation 留原作者修 B2-EXT8 后固定复核；其依赖 interface/trust 两目标随 B3 通过一起消费。个别正文 PASS 不冒称整合接受或运行收益；review 提交由 Driver 保全。
