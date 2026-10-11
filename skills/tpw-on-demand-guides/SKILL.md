---
name: tpw-on-demand-guides
description: "On-demand support guides for TPW methods (redacted evidence, test-evidence quality, mock/adapter choice, change shape, agent text, professional explanation, pre-write check design, lesson promotion, accessibility observation, positioned artifacts). Not a method body; load only when a task explicitly needs one of these guides."
license: Local self-use packaging only; no public distribution license granted; upstream MIT notices in THIRD-PARTY-NOTICES.md
disable-model-invocation: true
metadata:
  package: tpw-skills-packaging-f5d6d054
  status: local-use package
  source-set: professional-workflow/methods/guide-*.md
  source-pin: f5d6d0547459eb15c40aec25617418d5ea4710e6
  source-tree: 9d7c057417da73895cda3b85ec34d49db58669b6
---

## 这是什么（本机自用固定成品包 · 非自动）

10 个 TPW 支持导引的**按需公共资源根**：它们不是能力方法，也不默认激活；只在任务/Charter 明确需要其中某一份时，按本目录内的文件名读取。本根以 `disable-model-invocation: true` 标为非自动入口，只能显式调用（`/skill:tpw-on-demand-guides`）。

- 每份导引与 `professional-workflow/methods/<同名文件>`（pin `f5d6d0547459eb15c40aec25617418d5ea4710e6`，tree `9d7c057417da73895cda3b85ec34d49db58669b6`）**逐字节相同**；逐份 SHA-256 见 `SOURCE.md`。
- 条件依赖：本目录内互相引用的导引（`guide-check-design` ↔ `guide-lesson-promotion`、`guide-professional-explanation` → `guide-redacted-evidence`、`guide-accessibility-observation` → `guide-test-evidence-quality`）在同一目录内可解析，无需跨目录、无需 symlink 别名推断。
- 与入口的关系：入口按自身正文的实际条件依赖随包携带所需副本（见各入口 `SKILL.md`）；本根是**未随入口携带时**的公共取回点，不替代入口内的闭包。
- 不随本根携带：`design-alternatives`／`cross-module-design` 等方法正文（它们是能力入口 `tpw-design-alternatives`／`tpw-cross-module-design`）；上游来源锚（出处记录，按上游 pin 取）。
- 许可边界：本机自用；公开发行条款未定。上游 MIT 原文见 `THIRD-PARTY-NOTICES.md`。

## 导引清单

| 导引 | 用途 | 入口内副本 |
| --- | --- | --- |
| `guide-accessibility-observation.md` | 按需观察无障碍行为时 | 见对应入口「包装与资源边界」 |
| `guide-agent-text.md` | 写 agent-facing 文本时（经传递闭包） | 见对应入口「包装与资源边界」 |
| `guide-change-shape.md` | 为读者塑造变更时 | 见对应入口「包装与资源边界」 |
| `guide-check-design.md` | 写前该查什么（范围／真实入口／负控制）；UCBIP routing 中与本入口组合消费 | 见对应入口「包装与资源边界」 |
| `guide-lesson-promotion.md` | 把经验提升为载具时（经 guide-check-design 传递） | 见对应入口「包装与资源边界」 |
| `guide-mock-adapter-choice.md` | 选择跨依赖边界的测试替身／观察面时 | 见对应入口「包装与资源边界」 |
| `guide-professional-explanation.md` | 解释机制／理由时 | 见对应入口「包装与资源边界」 |
| `guide-redacted-evidence.md` | 输出／交接可能含敏感工件时；证据保管 | 见对应入口「包装与资源边界」 |
| `guide-test-evidence-quality.md` | 判断所产证据能否支撑声明时 | 见对应入口「包装与资源边界」 |

`guide-positioned-artifacts.md` 不在本根：它声明的依赖是 `external-tool-operation.md`，因此随 `tpw-external-tool-operation` 入口携带，避免本根出现无依赖可读的悬空引用。
