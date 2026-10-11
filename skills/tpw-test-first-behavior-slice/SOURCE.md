# 来源与包装身份 · tpw-test-first-behavior-slice

**本包**：`tpw-skills-packaging-f5d6d054`，在 TPW 仓任务分支 `tpw-skills-packaging-2026-10-11` 上提交（基于 `main@89b5203d`，不改动 main）。本机自用固定成品包；接受与安装状态由宿主的接收记录承载，不在本包内声明。

## 固定来源

正文的**现行位置**是本包 `SKILL.md`；下表历史对象用于身份与取回。

| 项 | 值 |
| --- | --- |
| 方法源路径（历史固定对象） | `professional-workflow/methods/test-first-behavior-slice.md` @ `f5d6d0547459eb15c40aec25617418d5ea4710e6` |
| 源仓 pin | `f5d6d0547459eb15c40aec25617418d5ea4710e6` |
| 源树 tree | `9d7c057417da73895cda3b85ec34d49db58669b6` |
| 正文 SHA-256 | `5d664c28b3352576e5a3082c369e29692a6fc6102942567818f45313842b5310` |

正文逐字节保留：本包 `SKILL.md` 的正文段（自第一行标题起至文件末）与该 SHA-256 一致。**现行位置即本包**；历史固定对象为 `professional-workflow/methods/… @ f5d6d0547459eb15c40aec25617418d5ea4710e6`（2026-10-11 起正文已从工作流包摘出，仍可按该 pin 取回）。

## 随包资源及其独立身份

| 资源 | 性质 | 身份 / 校验 |
| --- | --- | --- |
| `guide-mock-adapter-choice.md` | TPW guide（读取型） | 历史固定对象 `professional-workflow/methods/guide-mock-adapter-choice.md` @ `f5d6d054`；现行副本即本目录 `guide-mock-adapter-choice.md`；SHA-256 967f089fa57d7a803b6657836a1ba4610d27c60b0fe9342e96d9a268b0d7414e` |
| `guide-test-evidence-quality.md` | TPW guide（读取型） | 历史固定对象 `professional-workflow/methods/guide-test-evidence-quality.md` @ `f5d6d054`；现行副本即本目录 `guide-test-evidence-quality.md`；SHA-256 0ea7a4ec3c1cb5da3286ffe68aec4770f6da370f59a25cc58bcefe496e2063e6` |

携带规则：正文按文件名指向的资源（含传递的 guide→guide 引用，及已核的实际条件依赖）随包取回，保证同一固定包内可读；仅出处锚与“边界指针”不携带。

## 边界指针（文件不随包）

- 无

## 来源（本正文 + 随包资源的并集）

| 来源 | pin | 出现于 |
| --- | --- | --- |
| Matt | `mattpocock-skills` @ `c55ee46073ed923f86ce59a5eb3b6d895095d1b7` | `test-first-behavior-slice.md`、`guide-mock-adapter-choice.md`、`guide-test-evidence-quality.md` |
| pstack | cursor-plugins `pstack` @ `ecc249f1e306fc64ddf83c7bed16cacf7c2239db` | `test-first-behavior-slice.md`、`guide-test-evidence-quality.md` |
| cursor-team-kit | cursor-plugins `cursor-team-kit` @ `ecc249f1e306fc64ddf83c7bed16cacf7c2239db` | `guide-test-evidence-quality.md` |

以上是**出处锚**：不要求为使用本包而重新加载上游正文；需要其独特能力时显式绑定其固定版本。`THIRD-PARTY-NOTICES.md` 按同一并集保留许可原文。

## 本地包装差异（仅此三类，正文未改）

1. `SKILL.md` 的 YAML frontmatter（name／description／license／metadata）。
2. `SKILL.md` 中新增的「包装与资源边界」一节。
3. 新增 `SOURCE.md`、`THIRD-PARTY-NOTICES.md` 两个记录文件。

## 许可边界

- **本机自用**：Neil 于 2026-10-11 授权在本机安装／使用该成品；范围仅限本机个人使用。
- **公开发行**：未授予任何公开发行许可。上游 MIT 条款不用于推断 TPW 自有融合增量的条款；正式对外分发前须由 Owner／TPW 维护者确认自有部分条款。
- 包内不完整声明任何自有许可；`license` frontmatter 字段只表述上述自用边界。

## 版本不漂移

旧任务使用本包时，须绑定**本包自身提交**或本文件记录的 pin／路径（可取回），不得依赖“当前 main”“CURRENT”或可变目录名。升级＝选新的固定对象并重新核；旧对象保留可取回。
