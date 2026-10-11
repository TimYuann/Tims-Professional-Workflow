# 来源与包装身份 · tpw-debug

**本包**：`tpw-skills-packaging-f5d6d054`，在 TPW 仓任务分支 `tpw-skills-packaging-2026-10-11` 上提交（自觉于 `main@89b5203d`，不改动 main）。本机自用包，待宿主 review，尚未安装。

## 固定来源

| 项 | 值 |
| --- | --- |
| 方法源路径 | `professional-workflow/methods/local-defect-feedback-loop.md` |
| 源仓 pin | `f5d6d0547459eb15c40aec25617418d5ea4710e6` |
| 源树 tree | `9d7c057417da73895cda3b85ec34d49db58669b6` |
| 正文 SHA-256 | `0feec14d81db315262f79a9709a67b08d621d8833e3e28ad9c55beedc90a8bd2` |

正文逐字节保留：本包 `SKILL.md` 的正文段（自 `# Local defect feedback loop…` 起至文件末）与该 SHA-256 一致。另已核源仓 `main@89b5203d` 与 pin `f5d6d054` 的 `professional-workflow/` 子树零差异，故当前源树取同一正文不会漂移。

## 随包资源及其独立身份

| 资源 | 性质 | 身份 / 校验 |
| --- | --- | --- |
| `guide-redacted-evidence.md` | TPW 方法正文（读取型） | `professional-workflow/methods/guide-redacted-evidence.md`，SHA-256 `0abd46cec7198ae97671dbc03e428be559cd75927537a9bd06ebd2c63aef5335` |
| `guide-test-evidence-quality.md` | TPW 方法正文（读取型） | `professional-workflow/methods/guide-test-evidence-quality.md`，SHA-256 `0ea7a4ec3c1cb5da3286ffe68aec4770f6da370f59a25cc58bcefe496e2063e6` |
| `scripts/hitl-loop.template.sh` | **上游原件**（条件执行） | Matt `mattpocock-skills` @ `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`，`skills/engineering/diagnosing-bugs/scripts/hitl-loop.template.sh`；SHA-256 `35103539fc36873eea36074769ad454f9379d6fc8b2dc0e26ce987fd3bfe5503`。仅人类操作确不可替代且获授权时运行。 |
| `THIRD-PARTY-NOTICES.md` | 上游许可原文 | Matt / Addy / pstack / cursor-team-kit 四份 MIT，逐条与各上游 `LICENSE` 文件核对一致 |

## 上游来源锚（正文 Source anchors 段，pin 已核）

- Matt Pocock，`mattpocock-skills` @ `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`（`skills/engineering/diagnosing-bugs/SKILL.md`）
- Addy Osmani，`addyosmani-agent-skills` @ `2686b620fc1fed2e8f60c704839c766b8594c6b6`（`skills/debugging-and-error-recovery/SKILL.md`）
- cursor-plugins @ `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`（`pstack/skills/principle-fix-root-causes`、`pstack/skills/principle-prove-it-works`、`cursor-team-kit/skills/check-compiler-errors`、`pstack/skills/poteto-mode/playbooks/runtime-forensics.md`、`pstack/automations/benny/skills/reproduce-and-fix-issues/references/*`）

这些是**出处锚**：不要求为使用本包而重新加载上游正文；也不把它们当作本包的可执行资源。

正文另有一处 `methods/behavior-claim-evaluation.md`，属 **TPW 方法集内引用**（该文件在同一 pin 的 `professional-workflow/methods/` 下存在，已核），不在本包内；需要时按 TPW 固定 pin／路径绑定，不要按本包相对路径查找。

## 本地包装差异（仅此三类，正文未改）

1. `SKILL.md` 的 YAML frontmatter（name／description／license／metadata）。
2. `SKILL.md` 中新增的「包装与资源边界」一节。
3. 新增 `SOURCE.md`、`THIRD-PARTY-NOTICES.md` 两个记录文件。

## 许可边界

- **本机自用**：Neil 于 2026-10-11 授权本轮在本机安装／使用该成品；范围仅限本机个人使用。
- **公开发行**：未授予任何公开发行许可。上游 MIT 条款不用于推断 TPW 自有融合增量的条款；正式对外分发前须由 Owner／TPW 维护者确认自有部分条款。
- 包内不完整声明任何自有许可；`license` frontmatter 字段只表述上述自用边界。

## 版本不漂移

旧任务使用本包时，须绑定**本包自身提交**或本文件记录的方法 pin／路径（可取回），不得依赖“当前 main”“CURRENT”或可变目录名。升级＝选新的固定对象并重新核；旧对象保留可取回。
