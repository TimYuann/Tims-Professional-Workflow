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
