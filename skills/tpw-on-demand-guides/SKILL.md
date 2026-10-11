---
name: tpw-on-demand-guides
description: "On-demand support guides for TPW methods (redacted evidence, test-evidence quality, mock/adapter choice, change shape, agent text, professional explanation, pre-write check design, lesson promotion, accessibility observation). Not a method body; load only when a task explicitly needs one of these guides."
license: Local self-use packaging only; no public distribution license granted; upstream MIT notices in THIRD-PARTY-NOTICES.md
disable-model-invocation: true
metadata:
  package: tpw-skills-packaging-f5d6d054
  status: local-use package
  method-location: this package (skills/tpw-on-demand-guides/)
  source-set-historical: professional-workflow/methods/guide-*.md @ f5d6d0547459eb15c40aec25617418d5ea4710e6
  source-pin: f5d6d0547459eb15c40aec25617418d5ea4710e6
  source-tree: 9d7c057417da73895cda3b85ec34d49db58669b6
---

## 这是什么（本机自用固定成品包 · 非自动）

**九份** TPW 支持导引的**按需公共资源根**（固定批内十份导引全部可取：第十份 `guide-positioned-artifacts.md` 随其声明依赖的入口 `tpw-external-tool-operation` 携带）：它们不是能力方法，也不默认激活；只在任务/Charter 明确需要其中某一份时，按本目录内的文件名读取。本根以 `disable-model-invocation: true` 标为非自动入口，只能显式调用（`/skill:tpw-on-demand-guides`）。

- 每份导引逐字节等于**历史固定对象** `professional-workflow/methods/<同名文件>` @ `f5d6d0547459eb15c40aec25617418d5ea4710e6`（tree `9d7c057417da73895cda3b85ec34d49db58669b6`）；**现行位置即本根**（该目录 2026-10-11 起已从工作流包摘出，仍可按 pin 取回）；逐份 SHA-256 见 `SOURCE.md`。
- 条件依赖：本目录内互相引用的导引（`guide-check-design` ↔ `guide-lesson-promotion`、`guide-professional-explanation` → `guide-redacted-evidence`、`guide-accessibility-observation` → `guide-test-evidence-quality`）在同一目录内可解析，无需跨目录、无需 symlink 别名推断。
- 与入口的关系：入口按自身正文的实际条件依赖随包携带所需副本（见各入口 `SKILL.md`）；本根是**未随入口携带时**的公共取回点，不替代入口内的闭包。
- 不随本根携带：`design-alternatives`／`cross-module-design` 等方法正文（它们是能力入口 `tpw-design-alternatives`／`tpw-cross-module-design`）；上游来源锚（出处记录，按上游 pin 取）。
**关于正文内的 Status／评审标注（时间身份）**：正文中 `candidate`、`not yet an accepted reference`、`fixed-diff review still applies` 一类标注，说明该正文在**吸收批次**中的评审阶段。对该批次已 gate-reviewed 并通过的对象，当前接受依据是 `docs/absorption/2026-10-02/FINAL-ACCEPTANCE.md`（Oracle 2026-10-03；product `8ba69427…` / core `d0cbbfc8…`）。该接受**只覆盖原接受对象本身**，不代表本包装、简介、资源可达性、安装状态或任何实际使用已经验证。

**仍然现行有效、不因上述时间身份改写**：正文的适用条件与边界；权力限制（如“不产生 authority／trigger／gate”）；明确标为未经验证的实验性判断；以及明确 deferred／未采纳的分支（不晋升、也不复活）。本包装不重开方法语义，也不把“已安装”推成“已接受”。

- 许可边界：本机自用；公开发行条款未定。上游 MIT 原文见 `THIRD-PARTY-NOTICES.md`。

## 导引清单

| 导引 | 用途 | 入口内副本 |
| --- | --- | --- |
| `guide-accessibility-observation.md` | 按需观察无障碍行为时 | 见对应入口「包装与资源边界」 |
| `guide-agent-text.md` | 写或修改会被 agent 当作任务依据／规范／交接／提示消费的文稿时（方法、Profile/Charter 条目、AGENTS.md/CLAUDE.md 行、spec、ticket、交接、运行时提示）；不因收件者是 agent 就必读 | 见对应入口「包装与资源边界」 |
| `guide-change-shape.md` | 为读者塑造变更时 | 见对应入口「包装与资源边界」 |
| `guide-check-design.md` | 选择、接线或依赖某个自动检查时（linter 规则／pre-commit hook／CI job／guard 脚本／版本-一致性同步）；判它是否真会在目标违规上失败（真实入口＋负控制） | 见对应入口「包装与资源边界」 |
| `guide-lesson-promotion.md` | 把经验提升为载具时（经 guide-check-design 传递） | 见对应入口「包装与资源边界」 |
| `guide-mock-adapter-choice.md` | 选择跨依赖边界的测试替身／观察面时 | 见对应入口「包装与资源边界」 |
| `guide-professional-explanation.md` | 需要帮助一个人理解某物（变化／子系统／决定／当前状态）而非接收状态报告时；普通工程回报／状态汇报有理由不自动触发 | 见对应入口「包装与资源边界」 |
| `guide-redacted-evidence.md` | 输出／交接可能含敏感工件时；证据保管 | 见对应入口「包装与资源边界」 |
| `guide-test-evidence-quality.md` | 判断所产证据能否支撑声明时 | 见对应入口「包装与资源边界」 |

`guide-positioned-artifacts.md` 不在本根：它声明的依赖是 `external-tool-operation.md`，因此随 `tpw-external-tool-operation` 入口携带，避免本根出现无依赖可读的悬空引用。
