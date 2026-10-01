# SOURCE-ABSORPTION-REPORT · 当前 main 对三仓两文的实际吸收

**状态：** Driver 报告（只报告/核verify，不新增吸收、不改产品）。委托：Owner 2026-10-01 + `SOURCE-AND-COLDSTART-FOLLOWUP-BRIEF.md` §A。
**对象：** product main `29d8b09e416028ad68bc72da23452c6e23755a5a`（core subtree `91875114e51855517f92ef099cbdf60c34e68243`；`1aee1da` 只增加输入与 brief，产品字节不变）。
**口径：** 不继承旧 lock 的 101/1080 或 absorbed 标签；分母用当前 pin 下的实际 pin+path 计数，分子只用有接受与消费证据的单位；**阅读深度（survey/索引/结构/全文）与采纳分开记录**。计数单位限定为 SKILL.md（否则按文件类型单列）。

## 1 · 五来源身份与当前定位

| 源 | 原始身份 / 许可 | pin（本轮实核） | 当前 locator（只读 legacy） | 历史 locator（已退役） |
| --- | --- | --- | --- | --- |
| S1 addyosmani-agent-skills | `github.com/addyosmani/agent-skills`；plugin 0.6.11；MIT © 2025 Addy Osmani | `2686b620fc1fed2e8f60c704839c766b8594c6b6` | `.worktrees/legacy-pre-night-2026-10-01/upstreams/addyosmani-agent-skills` | 旧 root `upstreams/addyosmani-agent-skills` |
| S2 cursor-plugins（含 pstack 子源） | `github.com/cursor/plugins`；pstack v0.15.5（author Lauren Tan）；各插件许可见仓内 | `ecc249f1e306fc64ddf83c7bed16cacf7c2239db` | `.worktrees/legacy-pre-night-2026-10-01/upstreams/cursor-plugins` | 旧 root `upstreams/cursor-plugins` |
| S3 mattpocock-skills | `github.com/mattpocock/skills`；1.2.3；MIT © 2026 Matt Pocock | `c55ee46073ed923f86ce59a5eb3b6d895095d1b7` | `.worktrees/legacy-pre-night-2026-10-01/upstreams/mattpocock-skills` | 旧 root `upstreams/mattpocock-skills` |
| S4 文章 Pt.1 载体 | 声明原文 `x.com/poteto/status/2094457600259842065`；镜像 `threadnavigator.com/thread/…`；`original_verified: false` | 载体文件 sha256 `b7a167c60fd870396143bdbdcbcddfeb89d74e5b5abd343e1af6739864e37f83`；声明 capture_sha256 无可复算原件 | `.worktrees/legacy-pre-night-2026-10-01/sources/articles/poteto-pstack-pt1.md` | 旧 root `sources/articles/poteto-pstack-pt1.md` |
| S5 文章 Pt.2 载体 | 声明原文 `x.com/poteto/status/2097732320606507506`；同镜像；`original_verified: false` | 载体文件 sha256 `304fd269f44d782037233adfa6ebe09bb077573d81089c86ccd525edd5839230`；capture 同上不可复算 | `.worktrees/legacy-pre-night-2026-10-01/sources/articles/poteto-pstack-pt2.md` | 旧 root `sources/articles/poteto-pstack-pt2.md` |

三仓均为浅克隆；pin 即本轮可核上限，不做历史考古。X 原站 **UNVERIFIED**；镜像身份已核（标题与续篇 id 一致），镜像全文未读（各抽读前 3.5k chars，页面约 20k chars）。

## 2 · 深度分母（按 SKILL.md 单位）

| 源 | SKILL.md 单位（分母，实核） | 全文读过（SKILL） | 结构级 | 索引级（至少 metadata） | 其他类型的全文读取 | 明确未处理 |
| --- | --- | --- | --- | --- | --- | --- |
| S1 addy | **25** | **4**：incremental-implementation、code-review-and-quality、debugging-and-error-recovery、api-and-interface-design | 21 | 25 | 0（agents/commands/hooks/docs 未读） | docs/evals 100、hooks 9、commands 9 正文 |
| S2 pstack | **47**（`pstack/skills/**`：24 常备 + 23 principles） | **8**：figure-it-out、architect、blast-radius、create-verification-skill、interrogate、show-me-your-work、poteto-mode、principle-prove-it-works | 0 | 47 | playbooks 4/23 全文（investigation、multi-phase-plan、bug-fix、feature） | guide 正文 10 章、architect/interrogate/why 的 references、benny 模板 |
| S2 cursor 非 pstack | **46** | **3**：cursor-team-kit/verify-this、thermos/thermo-nuclear-review、cursor-team-kit/review-and-ship | 0 | 46 | — | third_party 482 files、其余插件细则 |
| S2 benny（pstack/automations） | **3** | 0 | 0 | 3 | — | 3 个 benny skill 未读 |
| S3 matt | **38** | **6**：to-spec、domain-modeling、codebase-design、implement、diagnosing-bugs、code-review | 0 | 38 | 支持文档 2 全文（DEEPENING.md、DESIGN-IT-TWICE.md） | 其余 support files、docs 25 页 |
| S4/S5 文章 | 2 个载体（非 skill 单位） | 2 个载体全文（方法摘记，**非原文**） | — | — | 镜像抽读各前 3.5k chars | 原文与镜像全文 |

说明：`SOURCE-SURVEY.md §2` 的聚合“pstack 全文 14”把 playbooks 与 skills 混计，且与 §3 的逐文件锚点（8 SKILL + 4 playbooks = 12）有 2 项差；本报告只采用可有列内锚点的逐文件计数（8/47），并把该差异记为待核限制，不据此抬高覆盖。S1 的 4 篇全文中 2 篇来自 §8 补读；S3 的 6 篇均为逐文件全文记录。

## 3 · 实际采纳（分子）与 owning object

| 来源单位（pin + 仓库相对路径） | 当前 main owning object | 采纳深度 | 接受证据 | 实际消费证据 |
| --- | --- | --- | --- | --- |
| S3 `c55ee460…` · `skills/engineering/diagnosing-bugs/SKILL.md` | `professional-workflow/methods/local-defect-feedback-loop.md` | **主机制**（限缩蒸馏：回路本体/证伪探针/正确 seam/原场景复验） | M4 接受 `0136593…`/tree `2fc8db5…`（`ORACLE-ACCEPTANCE.md` M4 节）；MR-01/02/06/08 | `fixtures/m3-local-fix/CHARTER.md` 绑定（M4 body `3ca23a74…`）；M3 case-1 method-bound E 复验（`M3-LOCAL-E-REVALIDATION.md`）；M6 冷启动 case-1 绑定 shipped bytes `1ba8f8f2…` |
| S1 `2686b620…` · `skills/debugging-and-error-recovery/SKILL.md` | 同上（**有限增量 2 条**：非可复现分类、错误输出视为不可信数据） | **部分机制** | 同上 MR-01/02/06 | 同上（并入同一方法正文） |
| S3 `c55ee460…` · `skills/engineering/codebase-design/SKILL.md`（+`DEEPENING.md` 支持文档） | `professional-workflow/methods/cross-module-design.md` | **主机制**（限缩蒸馏：interface 全义、seam、depth、四类依赖、deletion test） | M4 接受；MR-01/02/06/07/08 | `fixtures/m3-snapshot/D-CHARTER.md` 绑定（M4 body `30066c8b…`）；M3 case-2 D Plan 接受与 affected-claim 复核 |
| S1 `2686b620…` · `skills/api-and-interface-design/SKILL.md` | 同上（**有限原则 3 条**：contract first、一致错误语义、兼容添加） | **部分机制** | 同上 | 同上 |
| S2 `ecc249f1…` · `cursor-team-kit/skills/verify-this/SKILL.md` | `professional-workflow/methods/behavior-claim-evaluation.md` | **必要部分**（claim 可证伪、baseline/treatment、三态映射；非整包） | M4 接受；MR-01/02/06/08 | `fixtures/m3-snapshot/M3-CASE2-F-CHARTER.md` 绑定（M4 body `06b06922…`）；M3 case-2 F 评价记录 |
| （派生自五源候选）`methods/README.md` 选择入口 | `professional-workflow/methods/README.md` | 综合选择入口（M5/M6 shipped bytes `24de9ce2…`） | M4 接受（`72a6ffb4…` 后的 package-status 派生已单独标识） | M6 冷启动选择映射“known local defect → local-defect-feedback-loop.md” |

**未采纳 / 延后 / 明确未用（重要项）：** S3 `DESIGN-IT-TWICE`、S2 `interrogate`、S3 `code-review`、S1 `code-review-and-quality`、S1 idempotency/retention、S2 pstack bug-fix（仅可选，未采用）、S2 其余插件与 benny 全部、S1 其余 21 篇、S3 其余 32 篇、S4/S5 两文 **0 采纳**。各 Profiles 不是五来源的采纳物：它们来自冻结责任主轴设计（M1 接受），与五源候选在 M4 才建立方法映射。

## 4 · 覆盖计数（分子/分母，明确口径）

- **SKILL.md 单位总数（分母）**：25 + 96 + 38 = **159**（96 = pstack 47 + benny 3 + 非 pstack 46）。
- **至少索引级 surveyed**：159/159（survey 记录；非采纳）。
- **全文读过 SKILL.md**：4 + 8 + 3 + 6 = **21/159 ≈ 13.2%**（另：pstack playbooks 4/23 全文、S3 支持文档 2 全文、S2 benny 0/3）。
- **实际采纳来源单位**：**5/159 ≈ 3.1%**——其中 3 篇为主机制 owner（diagnosing-bugs、codebase-design、verify-this），2 篇只贡献有限增量（debugging、api-and-interface-design）。
- **部分机制吸收标注**：三个 shipped 方法均为有界蒸馏，不是整篇/整包吸收；任何“已吸收 X skill”的说法都应写成“采纳了 X 的哪些机制”。
- **文章**：2/2 载体读过（载体是旧库派生方法摘记，非原文），镜像仅抽读，原文 UNVERIFIED；**采纳 0/2**。
- 旧 101/1080/absorbed 标签未使用；如需对照，只能作为历史材料单独引用。

## 5 · 结论

**真正在用**：matt 两篇主机制（diagnosing-bugs、codebase-design）与 cursor 一篇主机制（verify-this）经有界蒸馏进入三个方法正文（局部缺陷反馈回路、跨模块设计、行为 claim 评价），addy 两篇仅贡献有限增量，采纳来源单位合计 5/159；并有直接消费证据：M3 两个 case 的 Charter 实际绑定（local-fix / D / F）、M6 case-1 冷启动绑定与 M4 接受链。**只看过未用**：159 篇中的绝大多数（138 篇只在索引/结构级，21 篇全文读过中另有多篇未进入采纳），以及两篇文章载体（0 采纳）。**剩余缺口**：(a) UCBIP 旧路由名（path-trace/blast-radius/design-compare/drive-preview）与当前三个方法的覆盖映射未做——见 `COLDSTART-DSH-VERIFICATION-AND-PLAN.md`；(b) S4/S5 若要采用，必须先固定原站或镜像全文重核；(c) pstack 聚合全文数与逐文件锚点的 2 项差待核；(d) “部分机制”边界由 MR-01/02/06 的 retain/narrow/strip 记录拥有，不得外推为逐字采用。

**限制**：阅读深度计数来自 `SOURCE-SURVEY.md` 的动作记录（过程证据），本报告只重新实核了 pin、SKILL.md 计数、文章载体摘要、采纳对象摘要与绑定关系；未重新阅读未采纳源。无新吸收、无网络研究、无产品改动。
