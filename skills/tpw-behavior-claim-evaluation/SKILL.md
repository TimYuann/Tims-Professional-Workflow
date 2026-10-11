---
name: tpw-behavior-claim-evaluation
description: "Evaluate whether produced evidence supports a specific baseline/treatment behavior claim. Use to fix comparison scope and evidence sufficiency; the verdict stays with the responsible authority."
license: Local self-use packaging only; no public distribution license granted; upstream MIT notices in THIRD-PARTY-NOTICES.md
metadata:
  package: tpw-skills-packaging-f5d6d054
  status: local-use package
  method-location: this package (skills/tpw-behavior-claim-evaluation/SKILL.md)
  source-method-historical: professional-workflow/methods/behavior-claim-evaluation.md @ f5d6d0547459eb15c40aec25617418d5ea4710e6
  source-pin: f5d6d0547459eb15c40aec25617418d5ea4710e6
  source-tree: 9d7c057417da73895cda3b85ec34d49db58669b6
  source-sha256: 0d71dcc2063fc28658da4a9726de5467fe3a1f95bebb7d94cc806331613ce7bd
---

## 包装与资源边界（本机自用固定成品包）

正文逐字节等于**历史固定对象** `professional-workflow/methods/behavior-claim-evaluation.md` @ `f5d6d0547459eb15c40aec25617418d5ea4710e6`（tree `9d7c057417da73895cda3b85ec34d49db58669b6`）；**现行位置即本包**（该路径 2026-10-11 起已从工作流包摘出，仍可按 pin 取回）。包装只增加本 frontmatter 与本节，不改正文。

- **读取型资源 / 实际条件依赖**（随包提供，路径相对本技能目录）：`guide-redacted-evidence.md`（输出／交接可能含敏感工件时；证据保管）。
- **读取型资源 / 实际条件依赖**（随包提供，路径相对本技能目录）：`guide-test-evidence-quality.md`（判断所产证据能否支撑声明时）。
- **边界指针**：正文未把职责外派给其他方法文件的指针。
- **来源锚**（正文 Source anchors 段中的上游路径）：是出处记录，不是加载或执行本包的要求；需要这些能力时显式绑定其固定原件。

`SOURCE.md` 记录固定 pin、逐项校验值与本地包装差异；`THIRD-PARTY-NOTICES.md` 保留上游 MIT 原文。本包许可边界：本机自用，公开发行条款未定。

# Behavior claim evaluation · M4 accepted reference

- **Method owner:** F verification. Independence comes from the active Charter and actual contribution record.
- **Status:** accepted as a bounded reference for specific behavior claims; not a complete F workflow. A task Charter defines the evaluator and independence.

## Use

Use when a contract can be evaluated by comparing a concrete baseline with a treatment. Other F judgments, including whether a design is observable, can need other evidence.

The verification surface follows the claim's natural requirement. Synthetic or fixture-based evidence is appropriate when the claim is about logic isolation or mapping under controlled input; when the claim is about a real Provider, an actual SDK, wire behavior, deployment or end-user experience, an appropriate real leg is required under the task's existing policy and Charter authorization — a cheaper substitute's green result does not establish such a claim, and this method does not require a real leg for every task. If the needed real evidence lies beyond the existing authorization or boundary, use the task's recall path instead of self-granting access. Test mode is a professional choice, not a whitelist.

A real leg means actually executing the declared object, code or interaction; it does not mean remote or network access. A real SDK or production mapping may be exercised locally under a legal stub or fixture and can prove that scope; a local service does not automatically exceed the local test authorization merely by being called real, while remote Provider or deployment behavior still needs its own corresponding evidence. *(Authored addition from the reader-misreading fix; guides reference this definition rather than restating it.)*

## Method

1. State one falsifiable claim and its conditions, measure and threshold. Name the exact object and version.
2. Compare baseline and treatment with the same command, data and environment. Preserve the original output as evidence. "Preserve the original output" means preserving the signal-bearing evidence in an evidence-safe form: apply `guide-redacted-evidence.md` before storing or sharing. The §Verdict mapping is unchanged.
3. Decide whether the comparison is valid before interpreting its result. A missing/invalid baseline, noisy or incomparable data, failed measurement, or material environment difference makes the observation inconclusive.
4. Report the verdict, exact command and inputs, observed result, coverage and limitations.

When the comparison's evidence is a test or a suite, its quality check is bounded and separate: `guide-test-evidence-quality.md` covers the expected-value source, coupling, and weak-signal tells. This method stays a comparison-and-verdict method; the short reference does not expand it into a test-suite review.

## Verdict mapping

- **PASS:** a valid comparison supports the predicted direction and threshold, without a material confound.
- **FAIL:** a valid comparison provides a counterexample, shows no required change, or misses the stated threshold.
- **UNVERIFIED:** the comparison is not valid or the environment prevents a conclusion. Do not turn an invalid observation into product failure; do not turn missing evidence into PASS.

This mapping is semantic, not label substitution. In the source method, `VERIFIED` maps to PASS only when its conditions hold; `NOT VERIFIED` maps to FAIL only after a valid comparison; `INCONCLUSIVE` maps to UNVERIFIED. Independent authorship is not part of the measurement method and is not proved by a fresh instrument, model diversity or multiple labels.

## Limits

This method evaluates a specific observable claim, not user value or overall task closure. It does not accept residual risk or authorize release, deployment or other actions. The Charter must identify the actual evaluator and its independence for the object. Test-quality diagnosis, when that is the question, belongs to `guide-test-evidence-quality.md`; it changes neither the three-state mapping nor this method's scope.

## Source anchors

Cursor Team Kit `verify-this` in `cursor-plugins` at `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`, `cursor-team-kit/skills/verify-this/SKILL.md` (`Workflow`, `Verdict Rules`, `Output`): falsifiable claim, baseline/treatment comparison, single verdict and evidence output.
