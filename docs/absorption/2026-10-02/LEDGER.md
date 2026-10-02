# 三仓实质吸收 · Driver 台账 (2026-10-02)

## 基线（Driver 从 Git 核回）
- night branch `night/2026-10-01-workflow` tip `d3aab6ad30f36789664287f304e4e91ffd61d96a`（= root main `d3aab6a`）；core subtree `7c814e54c5e775045bc1c5155e3c181ceb1345fb`（21 文件）；Backbone `ce82a70016a4a3fc234ea287f39aac8d79a260ddf13747c4fb705bda580453ba`；local main == night tip；origin/main 未动 `448c3d67`。
- 三仓 pin（`.worktrees/legacy-pre-night-2026-10-01/upstreams/`，worktree clean）：
  - `addyosmani-agent-skills` `2686b620fc1fed2e8f60c704839c766b8594c6b6` — 208 paths — 旧索引 `docs/overnight/2026-10-01/ABSORB-A1-ADDY-INDEX.tsv`（208 行）
  - `cursor-plugins` `ecc249f1e306fc64ddf83c7bed16cacf7c2239db` — 863 paths — 旧索引 `ABSORB-A2-CURSOR-INDEX.tsv`（863 行）
  - `mattpocock-skills` `c55ee46073ed923f86ce59a5eb3b6d895095d1b7` — 169 paths — 旧索引 `ABSORB-A3-MATT-INDEX.tsv`（169 行）
  - 合计 1240；两文章不在分母。

## 名册与布局
| 角色 | live 名 | pane | 备注 |
| --- | --- | --- | --- |
| Driver | tpw-night-driver | w27:pD | 路由/固定对象/串行集成 |
| Oracle | tpw-0930-oracle | w27:p6 | Owner 接口/Pro/接受 |
| Gate（Codex GPT-6.1 SOL medium） | tpw-absorb-gate | w27:p12 | 唯一专业裁定；只写 reviews/ |
| A1 addy | tpw-absorb-a1 | w27:pV | 复用 |
| A2 cursor（旧） | tpw-absorb-a2 | w27:pW | 退休；产物已保全（索引已提交） |
| A2r cursor | tpw-absorb-a2r | w27:pW(新) | 新 Flash max（替换） |
| A3 matt | tpw-absorb-a3 | w27:pX | 复用 |
| A4 cursor 支持/脚本 | tpw-absorb-a4 | 新 pane | 新 Flash max（863 路径拆分） |
| B1 蒸馏 | tpw-absorb-b | w27:pY | 复用；worktree `.worktrees/absorb-w1` |
| B2 蒸馏 | tpw-absorb-b2 | w27:pZ | 复用；worktree `.worktrees/absorb-w2` |
| check | tpw-night-check | w27:pT | 机械身份/引用/包 |
| reader（旧） | tpw-absorb-reader | w27:p0 | 不称 fresh；冷读须新实例 |
| 旧 method | —（已关闭） | — | 无在飞/无未保全，native 历史保留 |

## 批次台账（A 包 → gate 裁定 → B 落地 → gate 差分 → Driver 集成）
| 批次 | A 包（packages/） | 覆盖族 | gate 裁定（reviews/） | B 落地 | check | 集成 |
| --- | --- | --- | --- | --- | --- | --- |
| W1-a1 | ADDY-AB ✅ | A/B | 待 gate | — | — | — |
| W1-a2r | CURSOR-ABC ✅ | A/B/C | 待 gate | — | — | — |
| W1-a3 | MATT-ABC ✅(含修正) | A/B/C | 待 gate | — | — | — |
| W1-a4 | CURSOR-DE | D/E/F + 支持/脚本 | — | — | — | — |

## 固定引用约定（gate 基线核清）
- Accepted core 引用是 **tree** `7c814e54c5e775045bc1c5155e3c181ceb1345fb`（professional-workflow 子树），不是 commit。
- 文件级引用两种等价形式：`git show <commit>:professional-workflow/<path>`（repo-root 相对，commit 用 night tip 或产品 commit `9085d75`）或 `git show 7c814e54:<path-within-professional-workflow>`（子树相对）。
- 产品不含 docs/；docs/absorption 的包/裁定/台账不属于 Accepted core，但属于固定审核对象记录。
- core 自 `9085d75` 起未变：`9085d75`/`d3aab6a`/`800414d`（及后续 docs-only）的 `:professional-workflow` 均为 `7c814e54`。
| W1-a2r#2 | CURSOR-ABC2 ✅ | F/B/C/A/Driver | 待 gate | — | — | — |
| W1-a3#2 | MATT-DEF ✅ | D/E/F+支持 | 待 gate | — | — | — |
| W1-a1#2 | ADDY-CD ✅ | C+尾部 | 待 gate | — | — | — |
| R1 | A3-MATT-ABC | 11/11: 吸收1合并3限缩7 | 可蒸馏 T/P/B/C/A/W 批 | 已派 B1(T/P/C) B2(B/A/W) | — | — |
| W1-a2r#3 | CURSOR-ABC3 ✅ | B/F/E/A/Driver | 待 gate | — | — | — |
| W1-a1#3 | ADDY-EF ✅ | F/E/评估 | 待 gate | — | — | — |
| A1-ADD | EF 尾部补读（F9 四 checklist + testing-patterns 六节 + 已读待用清单） | — | 待 gate | — | — | — |
| W1-a2r#4 | CURSOR-ABC4 ✅ | A/Voice/B/E | 待 gate | — | — | — |
| A3-MAP2 | 正文级联动图（25 组核账） | — | 已转 gate | — | — | — |
| R2 | A2R-CURSOR-ABC | 8/8: 吸收1合并1限缩6 | 落点：rationale/premise、决策启发+原型、CLI契约、domain state、harness、change-review、handoff、decision trajectory | 已派 B1/B2 第二批 | — | — |
| A1-ADD2 | EF addendum（F9 checklist 实质新机制） | 新 perf 9+sec 3+obs 2+a11y 4+test 1 | 待 gate 补裁 | — | — | — |
| W1-a2r#5 | CURSOR-ABC5 ✅ | F/编排/重构/记忆 | 待 gate | — | — | — |
| B-D1 | w1 e561233（A3 T/P/C 蒸馏） | — | 待 gate 差分 | — | — | — |
| B-D2 | w2 11136eb（A3 B/A/W 蒸馏） | — | 待 gate 差分 | — | — | — |
| W1-a2r#6 | CURSOR-ABC6 ✅ | F/交付/验证/清理 | 待 gate | — | — | — |
| W1-a2r#7 | CURSOR-ABC7 ✅ | meta/仲裁/走查/台账 | 待 gate | — | — | — |
| W1-a2r#8 | CURSOR-ABC8 ✅ | 实验/性能/取证/协调 | 待 gate | — | — | — |
| B-FIX | B1 e561233 修1项；B2 11136eb 修3项 | — | 已派修复 | — | — | — |
| W1-a4#1 | CURSOR-DEF ✅ | 编排/取证/交付/D/E/F | 待 gate | — | — | — |
| R3 | A2R-CURSOR-ABC2 | 5/5: 合并3限缩2 | 落点：测试/切片/评审合并、change-shape、lesson-promotion、handoff/专业解释、bounded-composition、CLI/API 幂等 | 已派 B1/B2 第三批 | — | — |
| B-D3 | w1 375b40c（R1修复+batch2） | — | 待 gate | — | — | — |
| B-D4 | w2 f71138b（batch2 only） | — | 待 gate | — | — | — |
| W2-a4#2 | CURSOR-DEF2 ✅ | 交付/扇出/TDD/reflect/SDK/安全 | 待 gate | — | — | — |
| W3-a4 | DEF3（orchestrate 正文）+ third_party 全量 | 尾账 | 已派 | — | — | — |
| R4 | A3-MATT-DEF | 14/14: 合并9限缩5 | 落点：local-defect/change-review/arch-survey/uncertainty/bounded-prototype/source-evidence/human-procedure/merge/handoff/learning/explanation/lesson+check-design | 已派 B1/B2 第四批 | — | — |
| W3-a4 | DEF3 ✅ + THIRD-PARTY ✅ | orchestrate 正文 6 组 + 482 全账 | 待 gate | — | — | — |
| PRO-ALLOW2 | 本轮新额度 2/2 未用（Oracle 持有；与旧已用额分账） | — | — | — | — | — |
| B-D5 | w1 f321c8c（fix+2批完整） | — | 优先复核 | — | — | — |
| B-D6 | w2 b8b1d28（fix+2批完整） | — | 优先复核 | — | — | — |
| B-FIX2 | B1 batch2 R1-R4；B2 batch2 newR1-R2（旧3项待新对象复查） | — | 已派修复 | — | — | — |
| INT1 | 最小通过切片集成 6b64b59（16 文件，core 7dcac80f） | — | Oracle/check 核中 | — | — | — |
| ADOPT | absorb/adopt 9d5859e（ADOPTION.md + cross-module-start） | — | 待 gate 边界 | — | — | — |
| ENTRY-FIX | Oracle读回两处入口修正 + check 报告 | — | 已提交 def5dcfae0efeb597da7a9ae67989a68449d560b | — | — | — |
| ADOPT-FIX | 9d5859e 需修3处（常驻指针/五级硬化/比较泛化） | — | 已派 | — | — | — |
| ADOPT-FIX2 | d8d1532 修3处（常驻指针/五级删阶梯/比较限定） | — | 待 gate 复审 | — | — | — |

## 收束要求（Owner 2026-10-02）
- 最终汇报分开：产品方法/guide 增量（责任位置→可执行操作→例子/反例→消费入口）｜源 SKILL 贡献数 vs playbook/support 贡献另列（不沿用旧 5/159）｜机制组裁定→落地 commit/merge/defer/reject 轨迹。
- 不编覆盖百分比、不重复计同源机制；三仓尾部 pending/未裁包继续，最小通过切片非总体结束。
- Pro 第一次=完整固定产品+通用接入+fresh 消费观察+诚实残余。
- EF addendum bfcache/no-store 绝对断言未裁：若 B 采用须按实际浏览器核官方适用性或写明源版本限度，不为性能否定有效 security/cache policy。
| B-D7 | w1 57b4aad（batch4+R1-R5） | — | 优先复核 | — | — | — |
| B-D8 | w2 a64bbc2（batch4+修复关闭） | — | 优先复核 | — | — | — |
| ORACLE-A4TP | A4-THIRD-PARTY 归 Oracle 裁定（474+8 分母/8指南可迁移、不硬化价格审批） | — | Oracle 接手 | — | — | — |
| ORACLE-A1CD | A1-ADDY-CD 9/9 已裁（C2/C8→B1，其余→B3） | — | 进行中 | — | — | — |
| A4TP-LAND | external-tool-operation + guide-positioned-artifacts | 474+8 归组；7来源不造7文件 | 已派 B2 | — | — | — |
| INT2 | 第二通过切片 5bf9333（B1 10 + B2 5 canonical + README） | core 7aa1ae82 | Oracle 入口核 | — | — | — |
| B-D9 | w3 7e9e4da（CD 7 文件） | — | 待 gate | — | — | — |
| GATE2 | tpw-absorb-gate2（Codex GPT-6.1 SOL medium 冷接班） | w27:p10 | ready，按承载接 A2R-ABC4 起 | — | — | — |
| GATE2 | 仅待命（不并行裁，不用量扩大） | w27:p10 | standby only | — | — | — |
| GATE1-HO | 旧 gate 完成 ABC4 后写最短 handoff 再退 | w27:p12 | 已通知 | — | — | — |
| INDEX-FIX | 补 domain-state-and-invariants / verification-harness-design 两行索引 | — | 280fbf4521abca30134ed94a346db75e9bd8221c | — | — | — |
| R-ABC4 | A2R-CURSOR-ABC4 4/4（合并2限缩2） | 落点：explanation/agent-text、change-review+lesson/check、lesson-promotion/learning | B1/B2 补正文；explanation/learning 部分随 handoff 链 | — | — | — |
| GATE1-RET | 旧 gate 退休（handoff 7c1dc32，无在飞） | — | 已退休 | — | — | — |
| GATE2-ACT | gate2 正式接班（读 GATE-HANDOFF，队列：w1/w2 修复、w3 七文件、ABC3/5-8、A1-EF+addendum、A4-DEF 系） | w27:p10 | active | — | — | — |
| ORACLE-A4DEF3 | A4-CURSOR-DEF3 归 Oracle（可迁移边界/脚本候选准入，非runtime整包） | — | Oracle 接手；gate2 排除 | — | — | — |
| ORACLE-A4DEF3 | A4-DEF3 6/6（J1/J5限缩，其余合并）已保全 10912de | 落点：interface/domain-state、CLI/handoff、agent-text、trust/external/harness | 已派 B3 主接 + B1/B2 各文件 | — | — | — |
| G2-WORK1 | w1 c537ed0 / w2 eb24161 / w3 7e9e4da 差分+源族 | — | 已派 gate2 连续审 | — | — | — |
| w3-DEF3 | 016e004（J1/J5 并入两文件；未建 guide 附比例理由） | — | 已并入 gate2 审单 | — | — | — |
| INT3 | 第三切片 84ffaa6d（8 w1 修后 + professional-learning + README） | core 90956104 | gate2/Oracle 知悉 | — | — | — |
| INT4 | 第四切片 ee50a7fdc87e54828a22a8825928a1e119f82c1d（elicitation/cli-contract/agent-text/positioned-artifacts） | core 见回执 | external-tool-operation §8 修中 | — | — | — |
| DEP-FIX | guide-positioned-artifacts 消费索引暂 hold（依赖 external-tool-operation §8） | — | 8d162269993cb0c8ccc6b61a5131d19cace02edf | — | — | — |
| INT6 | C5/C7 整文件 PASS 集成 9916f23b（core 1f509b6f） | — | gate2 知悉 | — | — | — |
| B-FIX3 | w1 d1eed24（domain-state J1）、w2 4f86ae7（EXT8）待核；B3 C1/C3/C4/C6/C9 修复中 | — | — | — | — | — |
| READER-P21 | p21 由 Owner 窄恢复（cd 工作区 + pi -ne + 同 Flash max）；Driver 暂停启动动作 | — | 等成功身份 | — | — | — |
| READER-C1 | 现有 reader 案例1（fixed 0e2bc4ba72ab8825b84e0e455de9ae5a2df26fe9；已读 root baseline 限度须报） | — | 进行中 | — | — | — |
| READER-C2 | reader2 案例2（纯 fresh，fixed 0e2bc4ba） | — | 进行中 | — | — | — |
| B3-FIX-DONE | 08dca20（C1/C3/C4/C6/C9 五处修） | — | 已送 gate2 定向复核 | — | — | — |
| READER-DONE | 两案例报告已保全（d6a73b03c353ac74043c8d9cc06782357c1f4468）；送 gate2 边界评估 | — | — | — | — | — |
| READER-NOTE | reader2 发现 adoption-examples 在仓库根、非包内；ADOPTION.md L84 已用 ../adoption-examples 且声明 core 不依赖 → 非断链，属可选外部指针设计 | — | — | — | — | — |
| R-ABC3 | ABC3 5/5（MG1限缩 MG2/3/4合并 MG5逐项） | — | B1(MG1/2/3/5) B2(MG5+MG4) 已派 | — | — | — |
| INT7 | 切片7 1ad49080650cf371b371bbbddb7351f521c4fb59（domain-state J1、external-tool-operation、interface/release/trust/performance + positioned 解 hold） | core 见回执 | C3 残余修中 | — | — | — |
| READER-VERDICT | gate2：入口/装配层有限 PASS；两案未直接消费方法正文，不记完整正文/两名 fresh PASS；不宣效率/生产资格 | — | 已入库 | — | — | — |
| B3-C3FIX | 98ba9b4（C3 step3 两条件+快照竞争反例） | — | 优先送 gate2 | — | — | — |
| INT8 | deprecation 集成 f3ba9a00（core d77b9a27）；B3 七文件全入 core，依赖闭 | — | Oracle 知悉；held 仅 B2 Profile 指针 | — | — | — |
| B2-ABC3 | 941a139（charter 最短启动 + rationale citation） | — | 送 gate2 队列 | — | — | — |
| R-ABC5 | ABC5 5/5（1/3限缩合并 2去重 4限缩 5合并）；双 code-quality SKILL 同字节；strongest-supported 聚合 | — | B1(MG1/2/3/4) B2(MG1) 已派 | — | — | — |
| INT9 | 切片9 164c332f740378ea6c3325b52cd00f7360366d99（charters README/template + rationale citation） | core 见回执 | gate2 PASS 集成 | — | — | — |
| READER-USE | reader2 continuation 专业使用观察（fixed f76a5955，adapter mapping 情境） | — | 进行中 | — | — | — |
| B1-ABC3 | 8cdd399（MG1/2/3/5 定向蒸馏） | — | 送 gate2 队列 | — | — | — |
| R-ABC6 | ABC6 6/6（1合并 2/3/4限缩合并 5/6限缩）；patch-id≠行为资格；bucket≠许可 | — | B1/B2 按共同 owner 已派 | — | — | — |
| INT10 | 切片10 0ff4d0f72feb71828e3ed8ad6b71075f2c0aca31（六 delta PASS；change-review 一句修中） | core 见回执 | — | — | — | — |
| B-FIX4 | change-review intake 一句限缩（stale auth/validation guard before protected side effect；普通 finding 事后观察） | — | 已派 B1 | — | — | — |
| R-ABC7 | ABC7 3/3限缩合并；MG4 台账非增量；双 canvas SHA 不同不双计；thirdParty 依 Oracle 474+8 | — | B1(arena/canvas) B2(carrier) 已派 | — | — | — |
| G2-PRI | 934c1ec（change-review 句修）+ reader professional-use 送 gate2 优先核 | — | — | — | — | — |
| G2-B1-B | 934c1ec 单句 PASS（父 a23e9b4，不覆盖其 ABC6 增量）；reader professional-use 有限 PASS（c4668470/f76a5955） | — | ABC6 增量补审中 | — | — | — |
| G2-CONS | 合并复核 w1 8cdd399..aadcb46 与 w2 941a139..HEAD 未审增量 | — | — | — | — | — |
| R-ABC8 | ABC8 4/4（1/2/4限缩合并 3限缩）；performance 不与 Addy 重复 | — | B1(§Use+MG3+MG4) B2(MG4) B3(MG1/2) 已派；reader feedback 一轮 | — | — | — |
| INT11 | 切片11 ebcafa9dc478ac183aa6e94602c378b14a46e8dd（behavior-preserving/harness/explanation 三 PASS） | core 见回执 | 四项窄修派工 | — | — | — |
| B-FIX5 | G2-LABEL(handoff/composition)、G2-SOURCE(change-review/slicing/handoff)、G2-PIN(design) B1；G2-LABEL(composition)、G2-ORACLE(agent-text) B2 | — | 已派 | — | — | — |
| B3-ABC8 | 76976e2（performance MG1/MG2；蒸馏自 review+summary，非直读 playbooks） | — | 送 gate2 队列 | — | — | — |
| R-EF | EF F1-F9 9/9 + addendum 22 条；增量=perf 支线/a11y/testAPI+eval 分层；S1/S2/O2/P1/P2 不动 | — | B3(perf) B1(testAPI+a11y) 已派 | — | — | — |
| B3-EF | 56e4b64（performance P3/P4/P5/P7+compact P6/P8/P9；直读源） | — | 送 gate2 队列 | — | — | — |
| R-DEF | DEF G01-G13 实质；G14 限度/locator；scripts 不移植 | — | B1(G01/02/05/07/08/10/11) B2(G04/09/12) B3(G03/04/06/09/12) 已派 | — | — | — |
| G2-B3-PERF | EF@56内容PASS保全；ABC8@769 两句需限缩（single run 仍是 measurement、跨 module 路由仅实际承诺变化）→ 整 56 文件 held | — | 已派 B3 | — | — | — |
| B3-DEF | 875033a（G03/G04/G05/G06/G09/G12 并入四文件；反例保留） | — | 送 gate2 队列（DEF2 后） | — | — | — |
| B3-PERF2 | 5d5dfcb（两句限缩：single-run 测量充分性按 claim/noise；路由按实际影响） | — | 送 gate2 队列 | — | — | — |
| R-DEF2 | H01-H09 九组（H02/05/06/08/09 窄限缩；其余已充分覆盖）；不建新平台 | — | B1(H02/04) B2(H06) B3(H05/08/09) 派工 | — | — | — |
| B-DEF2 | B1(H02/04+harness/local-defect 承载)、B2(H06)、B3(H05/08/09) | — | 已派 | — | — | — |
| INT12 | 切片12 a05db3f6aad69c54a0d034c4264bdba5004f332f（performance 5d5dfcb + DEF 四文件 875033a） | core 见回执 | B3 线全闭 | — | — | — |
| G2-CONS2 | 合并复核 w1 aadcb46..b8358cd 与 w2 dbd7e84..9dcc85a | — | — | — | — | — |
| B3-DEF2 | e3c77c8（H05/H08/H09 三文件；external-tool-operation 部分转 B2） | — | gate2 审 + B2 承接 | — | — | — |
| INT13 | 切片13 92351c9eeeb40c5adaa39a6f5d91f3c822b85d3b（9 PASS 文件含 accessibility guide） | core 见回执 | 6 窄修派工 | — | — | — |
| B-FIX6 | B1 五项（N-REUSE/N-DELIVERY/N-CHARACTERIZATION/N-HANDOFF/N-HARNESS）；B2 N-CLI-ORACLE | — | 已派 | — | — | — |
| INT14 | 切片14 7228dffa88f2fdf9400a017355ba006a7ad12a8b（B3 DEF2 三文件 PASS） | core 见回执 | B1/B2 修后对象待审 | — | — | — |
| G2-WAKE | 停止原因：两 B 修复 commit 18:54/18:56 到达但无 wake 消息，Driver 待命未主动轮询；现补送 w1 b8358cd..c62bf5e、w2 9dcc85a..f88e105 定向复核 | — | gate2 审中 | — | — | — |
| INT15 | 切片15 07b45124322e6ce24d1b6c3ad1bc646cdb70c3f3（8 PASS；handoff/design 两窄修 held） | core 见回执 | — | — | — | — |
| RESUME | STOPPAGE 已保全 c9d1a97（root=night 12c4c278）；广播完成通道＝herdr prompt driver；8 PASS 集成 slice15 07b45124；handoff/design 两窄修 B1 在飞；gate2 无在飞 | — | — | — | — | — |
