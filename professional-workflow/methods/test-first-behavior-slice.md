# Test-first behavior slice · on-demand method (MG-1)

- **Method owner:** E implementation for the slice; the evidence conclusion remains with F.
- **Status:** on-demand reference at a demonstrated gap (new behavior, one step at a time); a task Charter decides applicability and evaluator independence. It is not a universal TDD gate.

## Use

Use when a task builds new behavior at an observable surface and a failing check can be written before the implementation. When an existing defect already has a suitable failing observation, reuse it (`local-defect-feedback-loop.md` covers that path) and do not manufacture a redundant red.

The expectation asserted in a slice must be traceable to an independent source of truth: the accepted contract/commitment, a worked example from outside the implementation, a known-good literal, or prior art. A slice whose expectation can only be copied from the code about to be written is not ready.

## Loop

1. **Red before green.** Write the failing check for one behavior first, then only enough production code to pass it. Do not anticipate later checks or add speculative structure.
2. **Check why it is red.** The failure must come from the target behavior not being delivered — not from a missing dependency, a broken fixture or harness, environment state, or a stale artifact. A harness failure is fixed as harness work; it is not the slice's red. If the check passes, or fails for an unrelated reason, correct the check or the reproduction before touching the implementation. *(Source: cursor `ecc249f1…`, `pstack/skills/tdd/SKILL.md` §Workflow items 3–4 L17–18.)*
3. **One slice at a time.** One surface, one check, one minimal implementation per cycle; the first cycle is a tracer bullet through the smallest complete path. Let what the cycle taught you shape the next slice. Do not write a batch of checks for imagined behavior first (horizontal slicing): bulk checks commit to a shape before the implementation is understood, and they go insensitive to real changes.
4. **Keep the expectation independent.** Expected values come from the contract, a worked example, an independently computed literal, or prior art. Recomputing the expectation with the same formula as the implementation creates a correlated failure mode (the check can agree with the implementation's own mistake); a literal copied out of the implementation is not independent either. `guide-test-evidence-quality.md` has the diagnostic detail.
5. **Checks express accepted conditions; they do not create them.** A check is an executable expression of an accepted contract and evidence for the slice. If the slice exposes a missing or contradictory condition, surface it to the contract owner (B/C) instead of letting the check silently define a new contract.
6. **Behavior-preserving refactoring stays available.** The source moved its refactoring step to review; that is a source workflow decision, not a rule that E may never restructure inside its authorized scope. When a slice needs local restructuring, keep it behavior-preserving and inside the delegated scope, and note it; it does not need a separate review session before it can proceed. What must not happen is rewriting the accepted behavior so the check passes.
7. **Close the slice.** Re-run the original check and the relevant regression checks on the candidate version; report the exact command, the observation, and any remaining uncertainty.

## Cheap path first

The check is worth writing only where a practical one exists:

- Choose the **narrowest executable check**, preferring the closest test (unit, component, integration, regression) already used for that code path. *(Source: cursor `ecc249f1…`, `pstack/skills/tdd/SKILL.md` §Workflow 2 L16.)*
- If no practical check path is obvious — broad harness setup, brittle mocks, slow end-to-end infrastructure, production-only state, vague reproduction steps, large unrelated fixture churn — do not create one from scratch just to satisfy this method. Use the closest executable regression check instead (targeted script, manual reproduction command, browser automation, snapshot comparison, log assertion, focused integration check) and say which one and why. *(Source: same file §If a Failing Test Is Impractical L22–24.)*
- **Prefer no new check over a bad one.** A bad check mostly tests mocks, encodes current implementation details, depends on timing or unrelated global state, needs expensive infrastructure for a small fix, or would be deleted immediately after proving the fix. *(Source: same file L26.)*
- Report the evidence truthfully: name the failing-before check and the failure it produced, name the passing-after run, and if failing-before evidence could not be demonstrated, state why and which substitute check was used. *(Source: same file §Final Response L36–42.)*

## Example (authored, small)

A “share a cart” rule: (1) add the check `sharing a cart with one item makes it visible to the other member` at the existing cart API; run it — red for the target reason (the capability does not exist yet), not because the sharing fixture or the API import is broken; (2) implement only enough for that one path, with the expected value taken from the accepted behavior example (not recomputed from the new code); (3) re-run red→green; if the slice needs a local helper move, keep it behavior-preserving and say so. The check is red first and green after; the next slice starts from what this one taught.

## Surface choice (where the check observes)

Decide this before writing the check:

- Prefer an existing surface over a new one, and prefer the surface a caller would use (the interface is the test surface). Fewer surfaces across the change is better; "the ideal is one" is a heuristic, not a rule.
- State what the chosen surface catches and what it misses, and what the slower or more expensive alternative would catch; that trade-off is the reason to pick it.
- Different claims can need different surfaces: port-level or in-memory checks exercise the module's logic; they do not by themselves verify a production transport/serialization adapter. If the risk is in the adapter's request construction or response mapping, observe the adapter itself (local stub or recorded fixture), or name which real normalization function runs under which check; one external behavior plus one production adapter can honestly need two surfaces. Do not reduce the surface count at the cost of the claim — `guide-mock-adapter-choice.md` carries the full choice.
- Local test seams belong to E inside the delegated implementation scope. A change to a shared technical surface follows the cross-module design method's recall judgment (does it change a dependency commitment or the validation basis?), not an automatic human ACK.
- Slow browser or end-to-end checks are a feedback-cost and risk decision per claim: not always first and not banned. Where the red-green loop no longer pays for itself, write the check after the behavior works and say so.

## Limits

- Not a universal TDD gate, a fixed phase chain, or a mandate to test everything. Configuration, wiring, glue, and straight delegation may have no independent source of truth to assert against; check `guide-test-evidence-quality.md` before forcing a check there.
- Does not require a commit per red check, a fixed number of cycles, a particular test framework, or a separate review session for local refactors.
- Does not create, change, or accept B/C contracts, does not grant action permission, and does not replace the Charter.
- Guardrails on existing checks: do not change a check merely to match a wrong implementation; do not weaken existing assertions unless the expected behavior genuinely changed and the reason is clear; keep the regression focused on the behavior (no broad fixture churn or unrelated coverage expansion). *(Source: cursor `ecc249f1…`, `pstack/skills/tdd/SKILL.md` §Guardrails L28–34.)*
- A flaky target: make the check deterministic where possible and document the signal being locked down. If the defect exposes a broader class of failures, land the focused regression path first and consider sibling coverage after. *(Source: same section L33–34.)*
- E's self-check is evidence input, not an independent F conclusion.
- Reusing an existing failing observation is preferred over manufacturing a redundant one.

## Source anchors

| Source | Retained contribution |
| --- | --- |
| Matt Pocock, `mattpocock-skills` at `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`, `skills/engineering/tdd/SKILL.md` (§Rules of the loop L34–38; §Anti-patterns L28–32; §What a good test is L12–16; §Seams L18–26) | Red before green; one slice at a time; refactoring moved to review; implementation-coupled / tautological / horizontal-slicing anti-patterns; tests at observable seams. |
| Same pin, `docs/engineering/tdd.md` (§The loop, and the seam it runs at L27–45; §Common questions: refactor L49–51, browser/e2e L61–63) | Tracer bullet; the source's stated refactor-to-review rationale; the slow-browser feedback-cost trade-off. |
| Same pin, `skills/engineering/tdd/tests.md` (§Good/Bad Tests L5–77) | Behavior through public interfaces; independent expected values; side-channel vs tested interface. |
| Same pin, `skills/engineering/to-spec/SKILL.md` (§Process 2, L15) | Existing seams preferred; "the ideal number is one" as a heuristic. |
| cursor-plugins `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`, `pstack/skills/tdd/SKILL.md` (§Workflow L13–20; §If a Failing Test Is Impractical L22–26; §Guardrails L28–34; §Final Response L36–42) | The narrowest executable check and the closest existing test; correct-red-reason confirmation before touching the implementation; the cheap-path/impractical-test substitution list; prefer-no-new-test-over-a-bad-test; the focused-regression guardrails and evidence reporting. |

Authored additions: the red-cause check (Rule 2), the correlated-oracle qualification in Rule 4, the refactor-to-review scoping in Rule 6, and the two-surface counterexample in the surface section. They adapt the sourced rules to this package's responsibility boundary; they add no gate.
