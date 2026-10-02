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
