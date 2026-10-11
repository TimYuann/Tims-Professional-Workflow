# 来源与包装身份 · tpw-cross-module-design

**本包**：`tpw-skills-packaging-f5d6d054`，在 TPW 仓任务分支 `tpw-skills-packaging-2026-10-11` 上提交（基于 `main@89b5203d`，不改动 main）。本机自用固定成品包；接受与安装状态由宿主的接收记录承载，不在本包内声明。

## 固定来源

正文的**现行位置**是本包 `SKILL.md`；下表历史对象用于身份与取回。

| 项 | 值 |
| --- | --- |
| 方法源路径（历史固定对象） | `professional-workflow/methods/cross-module-design.md` @ `f5d6d0547459eb15c40aec25617418d5ea4710e6` |
| 源仓 pin | `f5d6d0547459eb15c40aec25617418d5ea4710e6` |
| 源树 tree | `9d7c057417da73895cda3b85ec34d49db58669b6` |
| 正文 SHA-256 | `373ff499c9b56a8b5426046c017e7b9ab01770f75e670953489858438665a204` |

正文逐字节保留：本包 `SKILL.md` 的正文段（自 `# Cross-module design method…` 起至文件末）与该 SHA-256 一致。另已核源仓 `main@89b5203d` 与 pin `f5d6d054` 的 `professional-workflow/` 子树零差异。

## 随包资源及其独立身份

| 资源 | 性质 | 身份 / 校验 |
| --- | --- | --- |
| `guide-mock-adapter-choice.md` | TPW 方法正文（读取型） | 历史固定对象 `professional-workflow/methods/guide-mock-adapter-choice.md` @ `f5d6d054`；现行副本即本目录 `guide-mock-adapter-choice.md`；SHA-256 967f089fa57d7a803b6657836a1ba4610d27c60b0fe9342e96d9a268b0d7414e` |
| `design-alternatives.md` | TPW 方法正文（读取型，真实方案分歧才读） | 历史固定对象 `professional-workflow/methods/design-alternatives.md` @ `f5d6d054`；现行副本即本目录 `design-alternatives.md`；SHA-256 36653fe8d9f809831e7b1c0e4f92e093e54d735eef8864c0595c63af3849be7e` |
| `references/DEEPENING.md` | **上游原件 + 一处导航链接适配**（条件读取） | 上游：Matt `mattpocock-skills` @ `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`，`skills/engineering/codebase-design/DEEPENING.md`，SHA-256 `f3dd099ce99289bd213914d8ee3e2429b78309c3957ca4583f7659551b1d53c1`；包装：SHA-256 `5176f5fcf2606d7d53d9d6d7560c489fc349571e65f03df8ec44862b1b7ed9f0`，差异仅首段导航链接 `[SKILL.md](SKILL.md)` → `[SKILL.md](../SKILL.md)`（否则在本目录下断链；未造空依赖）。冲突以已接受适配为准，不自动采其删除建议。 |
| `THIRD-PARTY-NOTICES.md` | 上游许可原文 | Matt / Addy / pstack / cursor-team-kit 四份 MIT，逐条与各上游 `LICENSE` 文件核对一致 |

## 上游来源锚（正文 Source anchors 段，pin 已核）

- Matt Pocock，`mattpocock-skills` @ `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`（`skills/engineering/codebase-design/SKILL.md`、`DEEPENING.md`、`to-spec/SKILL.md`、`tdd/SKILL.md`）
- Addy Osmani，`addyosmani-agent-skills` @ `2686b620fc1fed2e8f60c704839c766b8594c6b6`（`skills/api-and-interface-design/SKILL.md`）

**已声明 deferred、不在本包**：`DESIGN-IT-TWICE` 正文、其 3+ 并行 agent 数量，以及 idempotency／retention 规则；比较框架以 `design-alternatives.md` 按需提供。

这些是**出处锚**：不要求为使用本包而重新加载上游正文；需要其独特能力时显式绑定实际固定版本。

## 本地包装差异（仅此几类，正文未改）

1. `SKILL.md` 的 YAML frontmatter（name／description／license／metadata）。
2. `SKILL.md` 中新增的「包装与资源边界」一节。
3. 新增 `SOURCE.md`、`THIRD-PARTY-NOTICES.md` 两个记录文件。
4. `references/DEEPENING.md` 的一处导航链接适配（见上表；上游原件其余字节保留）。

## 许可边界

- **本机自用**：Neil 于 2026-10-11 授权本轮在本机安装／使用该成品；范围仅限本机个人使用。
- **公开发行**：未授予任何公开发行许可。上游 MIT 条款不用于推断 TPW 自有融合增量的条款；正式对外分发前须由 Owner／TPW 维护者确认自有部分条款。
- 包内不完整声明任何自有许可；`license` frontmatter 字段只表述上述自用边界。

## 版本不漂移

旧任务使用本包时，须绑定**本包自身提交**或本文件记录的方法 pin／路径（可取回），不得依赖“当前 main”“CURRENT”或可变目录名。升级＝选新的固定对象并重新核；旧对象保留可取回。
