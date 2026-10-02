# Behavior claim evaluation · M4 accepted reference

- **Method owner:** F verification. Independence comes from the active Charter and actual contribution record.
- **Status:** accepted as a bounded reference for specific behavior claims; not a complete F workflow. A task Charter defines the evaluator and independence.

## Use

Use when a contract can be evaluated by comparing a concrete baseline with a treatment. Other F judgments, including whether a design is observable, can need other evidence.

The verification surface follows the claim's natural requirement. Synthetic or fixture-based evidence is appropriate when the claim is about logic isolation or mapping under controlled input; when the claim is about a real Provider, an actual SDK, wire behavior, deployment or end-user experience, an appropriate real leg is required under the task's existing policy and Charter authorization — a cheaper substitute's green result does not establish such a claim, and this method does not require a real leg for every task. If the needed real evidence lies beyond the existing authorization or boundary, use the task's recall path instead of self-granting access. Test mode is a professional choice, not a whitelist.

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
