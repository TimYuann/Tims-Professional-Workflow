# Test evidence quality guide · on-demand support (MG-3)

Status: on-demand guide at a demonstrated gap; creates no authority, generator, or gate. Source anchors and authored additions are marked.

## Use

On demand, when a check or test suite is being used as evidence: E before handing self-test evidence on, or F when judging a suite or a claim. Add it to the task's existing bound/read set when that need exists; it is not mandatory loading and it is not a gate. It checks whether a green result is meaningful evidence. It does not decide the product verdict, change `behavior-claim-evaluation.md`'s job, or replace the Charter.

## Oracle: where the expected value comes from

- Expected values must come from an independent source of truth: a known-good literal, a worked example, the accepted spec or contract, or prior art. *(Source: matt `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`, `skills/engineering/tdd/SKILL.md` §Anti-patterns L31; `skills/engineering/tdd/tests.md` §Bad Tests L63–76.)*
- Recomputing the expectation with the same formula or logic as the implementation makes the check agree with the implementation's own mistake. *(Same source, L31.)* Authored precision: this is a **correlated-error risk**, not a guarantee that the check stays green under every implementation; the defect is "it can never disagree with this specific mistake".
- A literal copied out of the implementation is not independent even though it is a literal. *(Authored application of L31.)* A snapshot produced by the code under test is the same shape; a value derived by hand using the implementation's steps is not independent either.
- An expectation can also be supplied by prior art (an existing accepted example elsewhere in the suite/repo) when it was derived independently and is cited. *(Authored clarification; the source names spec, worked example, known-good literal.)*

## Coupling: what the check is actually attached to

Tells that a check is coupled to implementation rather than behavior: mocking internal collaborators, testing private methods, asserting call counts or order, or verifying through a side channel instead of the interface (for example, querying the database instead of using the interface). The classic tell: the check breaks when internals are refactored although behavior did not change. *(Source: `tdd/SKILL.md` §Anti-patterns L30; `tdd/tests.md` §Bad Tests L25–61.)*

Authored qualifications — the source's anti-pattern list is not absolute:

- Implementation coupling mainly harms maintainability, or makes the check verify a different claim; on its own it does not prove a green result was constructed. Report the specific defect (what it verifies, what it misses) rather than a blanket "this evidence is invalid".
- Call counts, database queries, and internal seams are legitimate when they are themselves the accepted claim: persistence or schema behavior, a "must not call twice" guarantee, a deliberately internal unit. State that the claim is the object; do not present it as coverage of external behavior.
- An assertion about **absence** can be the claim ("no request is sent when the input is invalid"); a **type-level** check proves a typing claim; a nil guard can fulfil an accepted "invalid input is rejected" contract. None of these is automatically a weak test — name the claim.
- Internal tests may exist and are useful. They must not be reported as external-behavior coverage when they are not.

## Signal: weak, absent, or self-referential assertions

The concrete omissions to look for — the check never runs the subject, or asserts nothing about its output: *(Source: cursor `ecc249f1…`, `pstack/skills/principle-test-behavior-not-implementation/SKILL.md` L9–23.)*

- **Weak or no assertion:** no `expect`, or only `toBeDefined`, truthiness, `not.toThrow`, "instance of", `toBeGreaterThan(0)`.
- **Mock or absence only:** only `toHaveBeenCalled`/`not.toHaveBeenCalled`/`toBeUndefined`/`toEqual([])`/`toHaveLength(0)`/`not.toBe(wrongValue)` — unless that call/absence is the accepted claim (see the coupling qualifications).
- **Self-referential:** the expected value comes from the code under test (`expect(f(a)).toBe(f(a))`, `expect(parsed.url).toBe(buildUrl(…))`).
- **Constant pin:** the assertion restates a hand-maintained constant, config default, table row or prompt string (`expect(LIMITS.maxTools).toBe(8)`), or presents a compile-time/type-only check as runtime evidence.
- **Fixture asserts fixture:** the assertion reads data the test built or a value computed in setup, and the subject never runs in the body.
- A test name that describes HOW instead of WHAT is a weaker tell; use it to look for the omissions above, not as proof on its own. *(Source: `tdd/tests.md` L44.)*

**The undefined-substitution check is a heuristic, not a mechanical criterion.** Asking "would this still pass if every imported function returned `undefined`?" exposes the weak/absence/mock/fixture families, but `toBeDefined()` fails when the subject returns `undefined`, so the source's blanket "still passes" claim does not hold for that assertion. Use the question to look for the concrete omission (the subject does not execute, or nothing about its output is asserted); do not turn it into an automatic pass/fail rule or a quality score. *(Authored qualification of the source's check; source L11.)*

## Waits, retries and flakes

- **Prefer a deterministic wait over a timeout.** A fixed sleep is a brittle assertion: wait on the observable condition (the element, state, event, or log line) rather than on elapsed time, and assert the specific expected state rather than the absence of an immediate crash. *(Source: cursor `ecc249f1…`, `cursor-team-kit/skills/run-smoke-tests/SKILL.md`; gate2 MG3 ruling.)*
- **A flaky result is evidence about the check.** Record each retry's object, conditions and result; a rerun that goes green does not erase the first real failure, and the retry itself may be the flake. The retry count follows the sampling cost and the phenomenon — not a fixed one, and not an unbounded loop until green. *(Same source; gate2 MG3 ruling.)*
- **Quarantine or skip changes the accepted evidence policy.** It needs a valid owner, a stated reason, and a follow-up verification plan; it is not a way to make a failing claim pass. A bypassed hook (for example `--no-verify`) must record the skipped coverage and its basis, and the run is not presented as fully green. *(Authored, from the gate2 MG3 ruling.)*

## What an assertion can establish (API counterexamples)

The accepted contract decides the assertion; the API shape is not a rule: *(Source: addy `2686b620…`, `references/testing-patterns.md`; `skills/test-driven-development/SKILL.md` §Step 1 and §Red Flags — retained as claim-bound counterexamples. Gate2 F1/F9-T4/T5.)*

- **Reference identity can itself be the contract.** Do not force a deep/structural comparison because the value happens to be an object; if the accepted behavior is "returns the same instance", identity is the correct assertion.
- **Tolerance comes from the claim, not a habit.** A floating-point tolerance follows the scale, error budget and data source rather than an arbitrary precision; a too-loose tolerance and a NaN case need their own negative control. Several assertions may jointly prove one complete contract — a short-looking assertion is not automatically zero evidence, and a weak assertion is not automatically strong either: name what it does and does not cover.
- **Interaction observation is valid when the interaction is the contract.** Call counts, order and arguments may be exactly the public protocol or a safety guarantee (a "must not call twice" rule, a required ordering); that is a claim-bound exception, not a licence for arbitrary internal assertions (see §Coupling).
- **Naming is not a syntax rule.** A check's name should let a reader understand the condition and the expected outcome, and helpers may remove repetition as long as the data stays independently readable. The AAA sections, a single-assert rule and a fixed name pattern are examples, not requirements.
- **An asynchronous check must finish before its result is claimed.** A missing `await`/return can end the run before an async error is attributed and produce a false green; use the framework's real completion/timeout mechanism. A callback is legitimate where the framework's own contract uses callbacks.
- **A new check that goes green immediately can be a valid characterization of existing behavior and narrow behavior evidence for the current object.** It does not show that the check caught the original defect or that the fix caused the change, and a broad absence claim depends on its coverage. The source's "a test that passes immediately proves nothing" is narrowed to that: it proves nothing about the new fix or the pre-fix failure, not that the check is worthless. *(N-CHARACTERIZATION.)*
- **Resource classes describe cost, not quality.** Process, I/O, network, data and time costs are a useful way to say what a check spends; the source's small/medium/large style ratios are examples, not a quota.
- **A local fixture or UI-logic check is valid for the claim it covers** (logic under controlled input) and does not certify the real layout, interaction or experience claim, which needs its own real leg (`behavior-claim-evaluation.md` §Use).

## Effect evaluation is a separate layer

Evaluating a method's *behavior* is not a test-quality check and not a structural lint. Keep three questions separate: (1) are the bytes/structure/references consumable (the file exists, references resolve, the frontmatter parses); (2) does the actual host **select/load** the needed method for a real prompt; (3) does the actual output/behavior **meet the goal**. A structural check cannot answer (2) or (3), and a lexical similarity ranking is a proxy for (2) — not semantic triggering, and not model-behavior qualification. *(Source: addy `2686b620…`, `evals/README.md` and `evals/skill-impact.md`; gate2 F7.)*

- **Design the cases against real use.** Positive prompts paraphrase how users actually ask (not the description text); a negative prompt names a real neighboring target/owner or a legitimate "no method needed" category, so the check cannot pass vacuously on an empty match. Never rewrite the user's intent so a grader accepts it, and never silently loosen a metric or ratchet: those belong to the accepted policy, and changing one is explicit. *(Same source; gate2 F7.)*
- **Record an effect claim with its scope.** Variant, model/provider/version, host/config, inputs/tools/resources/randomness, what was actually selected, the trace/artifacts and the scope — plus a same-question/control comparison that checks for confounds. The result is not an exit code, a regex hit or a "tool used" marker alone. *(Same source.)*
- **Invocation is not capability.** A regex matching a severity word does not prove a real defect was found; a ToolUsed marker proves only the call; and no invocation does not prove no effect — a loaded description can shape an output without being invoked. Source self-reported numbers (for example a 7/27→21/27 routing change) remain the source author's self-report without raw results here: they are not our evidence and not a universal cause. *(Same source.)*
- **Pressure cases test pressure, not authority.** Time, sunk-cost and pseudo-authority cases are useful for boundary behavior, but a genuinely authorized new instruction must be distinguished from untrusted pressure; an executor's permission mode or tool allowlist is not a sandbox, a business/network authorization, or independence. Grader schema/id checks prove JSON structure and question binding, not judgment correctness; an unknown grader identifier stays unknown. A failed or invalid grading preserves the invalid/raw evidence with its custody — it is not dressed as green. *(Same source.)*
- **Boundaries.** The source's eval runner has no current consumer in this library, so its tooling is not ported and its experience is not rejected for being a script; the source's efficiency and selection-rate claims are not accepted here. The current text's correction does not run an evaluation every time. Adoption/rejection/defer decisions go to the existing decision record, not a new ledger or automatic commit. *(Gate2 F7 rejected-defaults list: no per-method 3 positive/2 negative/1 behavior quota, no rank/collision hard thresholds, no fixed turn budget, no mandatory CI/runner, no automatic positive whitelist for new methods, no token-mode/SDK-version availability claim, no source-green-as-independent-F.)*

## Examples and exceptions

- **Correlated oracle (rejected):** `const expected = items.reduce(…); expect(calculateTotal(items)).toBe(expected)` — if both sides use the same wrong formula, the check agrees. **Independent oracle (kept):** `expect(calculateTotal([{price:10},{price:5}])).toBe(15)`, with 15 traceable to the spec or a worked example. *(Source: `tdd/tests.md` L63–76.)*
- **Side channel vs interface:** verifying persistence by querying the table behind the interface is coupled to storage details; verifying `getUser(user.id)` after `createUser` observes the capability callers have. *(Source: `tdd/tests.md` L47–61.)*
- **Legitimate persistence observation (exception):** when the accepted claim *is* the storage or relational behavior — a cross-table relationship, an invariant across tables, a migration backfill, a schema constraint — then observing the relation directly is the right surface, not a side channel. Name the claim that makes it legitimate. *(Authored exception.)*
- **Type-level checks** (`*.test.d.ts`, compile-time assertions) can legitimately pin a type or API contract, including a constant shape a runtime check cannot express. They do not establish runtime behavior; record that boundary instead of counting them as behavior coverage. *(Authored exception.)*
- **Behavior-preserving refactor signal:** if renaming or moving internals breaks the suite while behavior is unchanged, the affected checks are coupled. Review them, then decide per the coverage-replacement rule (`cross-module-design.md` §Method 4) rather than deleting blindly.
- **Evidence defect vs product verdict:** an unusable green is an evidence problem — UNVERIFIED at best; it is not by itself a product FAIL. A product FAIL needs a valid counterexample or observation against the accepted claim — a baseline/treatment comparison is one way to obtain it, and only when that method is invoked do its comparison-validity rules apply. Report the two separately. *(Authored linkage to `behavior-claim-evaluation.md` §Verdict mapping.)*
- **Counterexample without a baseline (accepted-claim observation):** the accepted invariant is "tenant A cannot read tenant B's orders". Observing, on the correct object version with authorized test data, that A can read B's object is a valid counterexample against the accepted claim — FAIL does not require obtaining a separate baseline. If instead the harness itself is broken, the observation is inconclusive (UNVERIFIED), not a FAIL. *(Authored counterexample; the FAIL condition stays "a valid observation contradicts the accepted claim", and the three-state mapping is unchanged.)*

## Risk and safety facts (blast-radius signals)

When the evidence concerns whether a change is safe beyond the diff, the quality test is whether the safety fact was proven — not whether the write-up sounds right. *(Source: cursor `ecc249f1…`, `pstack/skills/blast-radius/SKILL.md` §Don't trust your own writeup L15–17; §Steps L31–38.)*

- **Listing callers is not the check.** Grep can find those; the job is the breakage grep will not show. Look where grep stops: the called library's own source and its pinned version or local patch; when things run (microtasks, teardown/unmount); the JSON an API returns; a DB column; a wire format; another language reading the same bytes; a feature flag; code several hops downstream.
- **Find the one or two facts the change's safety depends on** ("this call only drops already-dead cache entries") and prove them by running the real code — usually one small script that imports the same library and calls the exact function. A fact that sounds convincing proves nothing.
- **Say how far the evidence got** and stop there honestly: (1) you said so; (2) a real `file:line` or the library source; (3) you walked the failure path and showed the bad case cannot happen; (4) you ran a script/test against the real code; (5) you reproduced it in the running app. Mark what remains **unproven** rather than implying a stronger grade.
- **Keep the categories separate:** confirmed risks (with how it breaks, the `file:line`, how likely and how bad, how to check), **cleared** items (checked and fine), and unproven items. A search that finds nothing is still an answer; never invent a caller or an API.
- **Do not fabricate likelihoods or costs.** Only state a probability or a time cost that came from an actual observation; a made-up percentage or millisecond figure is worse than "unknown".
- **Counterexample:** a grep of callers returning nothing is not evidence of no risk — the missed failure can sit in the library, the timing, the wire format, or a downstream consumer.
- **Boundary:** this is an evidence-quality check for a claim, not a merge gate and not a mandate to run everything; for a big or wide change an independent second attempt (another model/session) may help, but it is optional and it does not raise the fact's grade by itself.

## Limits

- No new gate, validator, mandatory suite review, or test framework; no requirement that every check be integration-style. No per-method case-count quota and no fixed similarity/rank threshold is imported from the effect-evaluation source; the eval tooling is not ported.
- Does not change verdict mapping, ownership, independence, or task authority; the Charter remains binding.
- Which evidence, and how much of it, a claim needs is decided by the claim itself, the applicable policy, the task's verification design, and F's judgment. `behavior-claim-evaluation.md` supplies one path (the baseline/treatment comparison) within its own scope, not the only route to F evidence. This guide only examines the quality of the evidence that was produced.
- The exceptions above are claim-bound: invoking one without naming the claim it serves is the same defect the guide warns about.
- There is no universal "cannot go red, therefore not evidence" reduction: a negative search, a historical reference, or a type-level proof has its own evidence conditions (see §Risk and safety facts), and none of them is replaced by an oracle-style score or confidence label. In particular, "can this evidence go red?" is not the same axis as a confidence/evidence grade used for historical or inferred claims: an `unknown` on that scale is an investigation result about the object, not a failure-detection verdict, and historical references, statistical intervals and direct counterexamples each carry their own basis rather than being folded into one red-capability scale.

## Source anchors

| Source | Pin / path | Section |
| --- | --- | --- |
| mattpocock-skills | `c55ee460…`, `skills/engineering/tdd/SKILL.md` | §What a good test is L12–16; §Seams L18–26; §Anti-patterns L28–32 |
| mattpocock-skills | `c55ee460…`, `skills/engineering/tdd/tests.md` | §Good Tests L3–23; §Bad Tests L25–77 |
| cursor-plugins | `ecc249f1…`, `pstack/skills/principle-test-behavior-not-implementation/SKILL.md` | The five still-passes shapes L15–23; the fix L23; the kept exceptions L25 |
| cursor-plugins | `ecc249f1…`, `pstack/skills/blast-radius/SKILL.md` | §Don't trust your own writeup L15–17; §How sure are you L19–29; §Steps L31–38; §What to hand back L40–48 |
| cursor-plugins | `ecc249f1…`, `cursor-team-kit/skills/run-smoke-tests/SKILL.md` | Deterministic waits/assertions over brittle timeouts; flake retries record object/conditions/result instead of letting one green rerun erase the first failure; quarantine/skip requires a valid owner, reason and follow-up verification. *(Gate2 MG3.)*
| addy | `2686b620…`, `references/testing-patterns.md` and `skills/test-driven-development/SKILL.md` §Step 1 / §Red Flags | Assertion counterexamples: reference identity as contract; tolerance from the claim; interaction-as-contract exception; async completion and false-green risk; immediate green as characterization of existing behavior (not proof of a new fix); resource classes as cost description; local fixture validity scoped to its claim. *(Gate2 F1/F9.)*
| addy | `2686b620…`, `evals/README.md` and `evals/skill-impact.md` | Effect evaluation as a separate layer: structural vs host-selection vs behavioral questions; lexical ranking as a proxy; real-phrasing positives and real-owner negatives; metrics owned by accepted policy; effect-claim recording with confounds; invocation ≠ capability; pressure vs authority; evidence preservation on failed grading. The eval runner/tooling, case-count quota and rank/collision thresholds are not imported. *(Gate2 F7.)* |
| mattpocock-skills | `c55ee460…`, `docs/engineering/tdd.md` | §The loop and the seam L27–45; §It's working if L77–84 |

Authored additions: the correlated-error precision, the constant-pin and type-check exceptions, the cross-table relational exception, the evidence-defect/verdict separation, and the claim-binding requirement for exceptions.
