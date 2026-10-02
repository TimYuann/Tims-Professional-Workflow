# A3-MATT-ABC · mechanism-level review package (A/B/C family)

Source repo: `mattpocock-skills` @ `c55ee46073ed923f86ce59a5eb3b6d895095d1b7` (169 paths).
Locator (read-only): `.worktrees/legacy-pre-night-2026-10-01/upstreams/mattpocock-skills`.
Navigation only: `docs/overnight/2026-10-01/ABSORB-A3-MATT-INDEX.tsv`.
Product baseline: night worktree tip `800414d`, core 21 files under `professional-workflow/`.

**This package produces no adoption decision.** Every group below is a candidate for
`tpw-absorb-gate` to accept / narrow / defer / reject. Nothing here was implemented, no product
file was changed, and no verification was executed (see §5).

---

## 0 · Read basis

Read in full at the pin, in this session, for this package:

| Source | Depth | Anchor form used below |
| --- | --- | --- |
| `skills/engineering/tdd/SKILL.md` | full (38 L) | section + line |
| `skills/engineering/tdd/tests.md` | full (77 L) | section |
| `skills/engineering/tdd/mocking.md` | full (59 L) | section + line |
| `skills/engineering/codebase-design/SKILL.md` | full (114 L) | section + line |
| `skills/engineering/codebase-design/DEEPENING.md` | full (37 L) | section + line |
| `skills/engineering/codebase-design/DESIGN-IT-TWICE.md` | full | section |
| `skills/engineering/domain-modeling/SKILL.md` | full (74 L) | section |
| `skills/engineering/domain-modeling/ADR-FORMAT.md` | full (47 L) | section + line |
| `skills/engineering/domain-modeling/CONTEXT-FORMAT.md` | full (60 L) | section + line |
| `skills/engineering/to-spec/SKILL.md` | full (75 L) | step + line |
| `skills/engineering/to-tickets/SKILL.md` | full (105 L) | section + line |
| `skills/engineering/code-review/SKILL.md` | full (87 L) | section + line |
| `skills/engineering/triage/SKILL.md`, `AGENT-BRIEF.md`, `OUT-OF-SCOPE.md` | full | section |
| `skills/engineering/setup-matt-pocock-skills/` (SKILL + `domain.md` + 3 tracker templates + `triage-labels.md`) | full | section |
| `skills/productivity/grilling/SKILL.md` | full (28 L) | line |
| `skills/productivity/grill-me/SKILL.md`, `to-questionnaire/SKILL.md`, `wait-what/SKILL.md` | full | line |
| `skills/productivity/writing-for-agents/SKILL.md` | full (81 L) | section + line |
| `skills/productivity/writing-for-agents/SKILL-MECHANICS.md` | full (22 L) | section |
| `skills/engineering/ask-matt/` (SKILL + `PHASE-BOUNDARIES.md`) | full | section |
| `skills/engineering/implement/SKILL.md`, `skills/in-progress/implement-spec/SKILL.md` | full | line |
| `skills/in-progress/setup-ts-deep-modules/` (SKILL + `.cjs`) | full | step |
| `.agents/invocation.md`, `.agents/writing-docs.md`, `.agents/install-block.md` | full | section |
| `CONTEXT.md`, `CHANGELOG.md` (structure), `AGENTS.md`/`CLAUDE.md` | full / structure | — |
| 25 `docs/engineering/*.md` + `docs/productivity/*.md` pages used below | full | `##` section |

Product side read in full: all 21 core files (`README.md`, 7 `profiles/`, 4 `charters/` +
`charters/README.md`, 5 `methods/`, `authority/README.md`, frozen `authority/RESPONSIBILITY-BACKBONE.md`).

**Not read / not established (stated so it is not inferred):** no matt path outside the pin; no
upstream issue, PR or discussion thread referenced by the docs pages (issue numbers appear below only
as the pages report them); no execution of any upstream script; the changelog was read at structure
depth only. `docs/overnight/2026-10-01/METHOD-REVIEW.md` and `METHOD-CANDIDATES.md` were read as
*old navigation*, and their `adopt`/`narrow`/`defer` labels are treated as leads, not as standing
qualification — where I propose something they listed as deferred, I say so and give the reason
independently.

---

## 1 · Accounting: how this wave covers the 169 paths

All 169 paths resolve; none is left implicit. **A/B/C distinct paths: 59.** Two paths are
multi-labelled by design, because one file carries two mechanisms that must be judged separately
(same file, several mechanisms — allowed and required by the dispatch): `skills/engineering/tdd/SKILL.md`
(MG-1 loop rules + MG-4 seam agreement) and `skills/engineering/tdd/tests.md` (MG-1 good-test
standard + MG-3 the two anti-pattern pairs).

| Disposition | Paths | Note |
| --- | --- | --- |
| A/B/C mechanism groups MG-1…MG-11 (this package) | 59 | primary-path counts per group below |
| DEF-wave candidates (§4 names each) | 42 | not dropped; handed to `A3-MATT-DEF` with its group |
| Platform metadata (`skills/*/agents/openai.yaml`) | 38 | Codex UI keys + `policy.allow_implicit_invocation`; the *mechanism* it encodes is the invocation axis → MG-8. This row keeps all 38, so none is double-counted as DEF |
| Release-note/config assets (`.changeset/*`) | 13 | record *that* a change happened and why; no independent engineering operation |
| Index/README assets | 6 | top-level + bucket indexes; duplicate carriers of MG-8's router mechanism |
| Manifest / hygiene assets | 4 | `package.json`, `package-lock.json`, `.gitignore`, `LICENSE` |
| Distribution / CI assets | 3 | `.claude-plugin/plugin.json`, `marketplace.json`, `.github/workflows/release.yml` |
| Governance ADRs | 2 | `.agents/adr/0001`, `0002`; non-method governance |
| Repo governance | 2 | `AGENTS.md` (symlink) + `CLAUDE.md`; the *mechanism* (bucket-promotion invariants) is MG-8 |
| **Sum** | **169** | reconciled by set equality against `git ls-tree -r --name-only <pin>`, not by count |

Per-group primary paths (a path may appear in more than one row only for the two multi-labelled
files above; the column sums to 61 because of those two):

**Cross-package overlap, declared so neither package counts the same mechanism twice:**
`skills/in-progress/setup-ts-deep-modules/SKILL.md` (here in MG-10; also screened in
`A3-MATT-DEF.md` DEF-13 for the *prove-the-check-fails* mechanism) and `skills/in-progress/retro/SKILL.md`
(here in MG-8 for the file-role / context-load allocation; also screened in DEF-12 for the
mechanical-vs-judgement classifier). Both are counted in this package's 59 and in that package's 44,
so the two-package reconciliation is `59 + 44 − 2 + 68 = 169`.

| Group | Paths screened here |
| --- | --- |
| MG-1 red-before-green loop | 6 |
| MG-2 vertical slice / demo-path test | 3 |
| MG-3 test-design anti-patterns | 1 |
| MG-4 seam agreement as contract | 3 |
| MG-5 criteria that can fail | 3 |
| MG-6 decision + rejection records | 7 |
| MG-7 glossary discipline | 5 |
| MG-8 document and context economy | 13 |
| MG-9 structured elicitation | 6 |
| MG-10 module-boundary vocabulary | 6 |
| MG-11 per-repo configuration surface | 8 |

Assets are grouped rather than精读 because they carry no independent engineering operation — they are
carriers or records. The three top-level `scripts/` and `dependency-cruiser.config.cjs` are **not**
excluded by suffix: three of them carry real engineering behaviour (`link-skills.sh` in MG-11,
`dependency-cruiser.config.cjs` in MG-10) and are screened as mechanisms; `list-skills.sh` and
`sync-plugin-version.mjs` are handed to DEF-14.

---

## 2 · Mechanism groups

### MG-1 · The test-first loop as contract generation (red before green)

**1) Mechanism, trigger, anchors, read status**

| | |
| --- | --- |
| Mechanism | Write the failing test **first**, then only enough code to pass it; repeat one slice at a time. The loop's output is not "tests" but a *generated, executable restatement of the behavior contract* — the first consumer that can disagree with the implementation |
| Trigger | A concrete behavior is being built or a defect fixed, and the behavior can be stated with an input and an observable output |
| Provisional locus | B (the contract it expresses) → E (who runs the loop) → F (who judges the result) |

Anchors: `skills/engineering/tdd/SKILL.md` L34–38 (§Rules of the loop: *Red before green* /
*One slice at a time* / *Refactoring is not part of the loop*); L12–14 (§What a good test is);
`docs/engineering/tdd.md` §The loop, and the seam it runs at (L27–46) and §Common questions (L47–76);
`skills/engineering/implement/SKILL.md` (whole body, 8 L) + `docs/engineering/implement.md`
§What one run does (five beats). Read: full.

**2) Operation, conditions of validity, failure modes, counterexamples**

- *Operation.* Red → green, then the next behavior. "Don't anticipate future tests or add
  speculative features." No refactor phase inside the loop.
- *Conditions of validity.* (a) There is an independent source of truth for the expected value —
  otherwise the loop manufactures the tautology MG-3 names; (b) a seam exists at which the
  behavior is observable; (c) the change has an input/output pair at all.
- *Stated limits (keep, do not soften).* The upstream body explicitly says refactoring was **dropped
  from the loop** because "agents essentially never performed it", and that implementation and review
  work better as separate sessions (`docs/engineering/tdd.md` §The loop…). The frontmatter still
  advertises "red-green-refactor" — the page records that mismatch as an open issue; the *description*
  is therefore not the contract.
- *Failure mode the source names.* The loop is applied where no independent source of truth exists,
  producing the tautological anti-pattern "arrived at from the other direction". The page records the
  unresolved hole: nothing in the skill decides *whether* a change is worth the loop at all
  (glue, config, wiring, type annotations, straight CRUD delegation).
- *Counterexample (verified local to the sources, not to a real task).* `docs/engineering/tdd.md`
  reports a user reporting the agent writing a Playwright test first and then burning a long loop
  concluding the *test* was broken for a feature that did not exist. That is the loop applied
  before the behavior exists at all — the correct handling stated is to declare slow browser tests
  as written *after* the behavior works, in the repo's own instructions.

**3) A–F loci and professional concern; Profile and call timing**

- **B** owns the behavior statement the test restates; **E** runs the loop and owns local algorithm
  and seam choice; **F** judges the delivered version and must not be the implementer.
- Professional concern: primarily *Correctness*, secondarily *Performance* only via the "slow test
  makes the loop stop paying" clause.
- Profile: `profiles/implementation.md` (E) as the primary; `profiles/behavior-domain.md` (B) when
  the behavior statement itself is unsettled; `profiles/evidence-evaluation.md` (F) for the version
  judgment. Call timing: **B before the loop, E during it, F after the fixed version exists** — not
  a fixed phase chain, and not mandatory for a local change that already has an accepted contract and
  a red observation (that path is `local-defect-feedback-loop.md`).

**4) Current product: exact text, what is covered, the specific gap, why**

Covered — `methods/local-defect-feedback-loop.md` §Method 1–5 already owns the *defect* path:
> "1. Identify the exact contract and original failing scenario. Run an observation that can
> distinguish the reported defect from the expected behavior. … 4. Repair the cause inside the
> delegated implementation scope. Put regression coverage at a useful behavior seam."

and §Limits correctly removes the ceremony: "does not require every task to enumerate a fixed number
of hypotheses, try every reproduction technique, create an extra commit for every red test…".

Gap — that method begins from **an existing failure** ("an observable failure", §Use). It has no
statement for the case where the behavior does **not exist yet**, so nothing generates the first
failing observation. `profiles/implementation.md` §关键问题 asks "自测能观察到什么？哪些关键负控制必须
变红？" — that is the right question but has no operation attached, and `profiles/implementation.md`
§按需方法入口 lists only "增量实现/小步验证方法" as a body-less candidate. The specific gap is:
**the red-before-green ordering rule, and the reason it produces a contract rather than a
verification, appear nowhere in the core.**

Why worth absorbing: it is the only mechanism in either round that *generates* the falsifiable
artifact F later judges, and it is the missing on-ramp to the method the product already accepted.
It also carries a professional detail the product's brevity would otherwise lose: the loop is
value-bearing even when an agent does not follow it strictly, and the honest position is to watch the
run rather than trust the instruction to enforce itself.

**5) Retain / change / delete; carrier; coupling; real-SDK dependency**

- **Retain** the ordering rule, the "one slice at a time" rule, and the refactoring-out-of-the-loop
  decision with its reason.
- **Drop** the upstream framing that makes the loop a *session driver* (an implementation method
  already existed in the product; the loop is a discipline inside E, not a separate phase).
- **Drop** all harness coupling: `tdd/SKILL.md` L26 instructs "call the Skill tool with
  `codebase-design`" — a host-specific invocation convention. In the product the equivalent is the
  Charter's `Applicable methods` binding, which is already the right carrier.
- Carrier: extend `methods/local-defect-feedback-loop.md` with a *new-behavior* use case, **or** a
  new sibling method (e.g. `methods/test-first-behavior-slice.md`) bound by the Charter. Do **not**
  inline into `profiles/implementation.md` (EXECUTION-PLAN §目标与边界: "不要把所有经验内联进
  Profile").
- Real SDK/runtime dependency: **none** for the rules themselves. Only the "watch the run" clause
  depends on a real agent observation.

**6) Draft text and verification plan (not executed)**

Draft (a candidate §Use paragraph for the extended or new method body):

> Use when a concrete behavior you are adding can be stated with an input and an observable output,
> and no failing observation for it exists yet, because it does not exist yet. State the behavior,
> write the smallest test that fails for that reason alone, then write only enough code to make it
> pass; take the next behavior after that. Do not batch the tests ahead of the implementation: a
> batch verifies imagined behavior and fixes the test structure before the implementation is
> understood. Where the change has no independent source of truth for its expected value, do not run
> this loop — say so, because a test whose expected value is computed the way the code computes it
> can never disagree with the code. Whether a change is worth this loop at all is an E judgment inside
> the delegation, not a gate.

Verification plan (a task, not a claim): run one bounded fixture (one behavior, one seam) with an
independent, independently-supplied expected value and observe (a) whether a red state actually
occurred before any implementation existed, and (b) whether the resulting test still passes after an
internal rename that does not change behavior. Boundary: this validates the *rule's* operating
behavior on one fixture; it does not validate the claim that the loop improves outcomes, and no such
claim is made here.

---

### MG-2 · Vertical slice / tracer bullet, and the demo-path test against horizontal slicing

**1) Mechanism, trigger, anchors, read status**

| | |
| --- | --- |
| Mechanism | Split work into slices that each cut a **complete but narrow path through every layer**, so each is independently demoable/verifiable; the opposite (one layer per slice) has to reach into other slices' work to define done |
| Trigger | A multi-step build is being decomposed, and the decomposition is about to be written down |
| Provisional locus | B (what "done" is observable as) → D (the arrangement) → E (the build) |

Anchors: `skills/engineering/to-tickets/SKILL.md` L25–41 (`<vertical-slice-rules>` block + the
wide-refactor exception at L41); `docs/engineering/to-tickets.md` §Tracer bullets, not layers
(L25–32) and §The wide-refactor exception (L44–55); `docs/engineering/triage.md` (criterion-shape
analysis, see MG-5). Read: full.

**2) Operation, conditions of validity, failure modes, counterexamples**

- *Operation.* Each slice: narrow **and complete**; demoable alone; sized to one fresh context
  window; prefactoring first.
- *The discriminating question (this is the usable test).* One question per slice: **"what can I
  demo when this is done?"** A ticket with no answer is a horizontal slice. This is what makes the
  rule operational rather than stylistic.
- *Failure mode, with field evidence as reported by the page.* "One team ran a 26-ticket stack sliced
  by layer (corpus, producer, aggregator, selector) and got roughly twenty agent runs per closed
  ticket, about three quarters of them rework. Their own post-mortem traced every failure class back
  to the horizontal slicing rather than to the implementations." (Attribution: the page reports this;
  it was not independently verified here.)
- *Conditions of validity.* (a) The layers are known well enough to name; (b) the consumer of the
  slices is a session that has never seen the plan — which is why the size bound is "one fresh
  context window" rather than a line count.
- *Preserved exception — do not flatten.* A **wide refactor** (one mechanical change with a blast
  radius across the codebase) cannot be sliced vertically at all: no slice lands green. The source
  gives a real sequence, expand → migrate in batches sized by blast radius → contract, with a stated
  fallback when even batches cannot stay green (shared integration branch, all blocked by a final
  integrate-and-verify slice, "green is promised only there"). This exception is a mechanism in its
  own right and must survive as a named case, not become an exception footnote.
- *Counterexample available from the same family.* `docs/engineering/to-tickets.md` §The wide-refactor
  exception exists precisely because the vertical rule, stated without it, produces an impossible
  plan.

**3) A–F loci and professional concern; Profile and call timing**

- **B/D** own the slice definition jointly — the slice boundary is a statement about what is
  observable, so B has a locus; the arrangement across modules is D's. **E** is the executor and can
  report that a slice was mis-sized.
- Professional concern: *Correctness* (done is defined by demonstrable behavior), plus *Delivery
  risk* via the prefactoring rule.
- Profile: `profiles/technical-planning.md` (D) primary; `profiles/behavior-domain.md` (B) for the
  demoable-behavior half. Call timing: when work is being decomposed for more than one session, and
  again at review time via the same question.

**4) Current product: exact text, what is covered, the specific gap, why**

Covered — `profiles/technical-planning.md` §心智模型 does the right thing *for a plan*, not for a
slice: "Plan 三件事：Commitments / Delegated Decisions / Recall Conditions；不要求三份文件" and the
sufficiency test "未参与讨论的合格实现者能开始且不猜共享承诺" — which is the same *consumer* premise
as the slice-size rule.

Gap — the core has **no slice-decomposition rule at all**. `profiles/technical-planning.md`
§关键问题 asks "改动的因果范围到哪里？回归影响、兼容与恢复依据是什么？" but never asks what makes one
piece of the change independently demoable, and `methods/cross-module-design.md` §Method 5 produces a
Plan with Commitments/Delegated Decisions/Recall Conditions — a *shape*, not an ordering. Nothing
tells a planner that a layer-per-package split is a defect, and nothing supplies the one-question
test. The wide-refactor case is also absent: `methods/cross-module-design.md` §Method 6 covers
"prefer an additive change" and "a valid authority may accept a breaking change", which is the
*compatibility* half of expand–contract but not the *sequencing* half (expand → batched migrate →
contract, with the green-promise fallback).

Why worth absorbing: it is the difference between a plan that can stop and be checked and a plan that
can only be checked when everything has landed — i.e. it decides whether F can evaluate anything
before the whole change exists.

**5) Retain / change / delete; carrier; coupling; real-SDK dependency**

- **Retain** the demo-path question, the completeness rule, the one-fresh-context size bound, and the
  expand–contract exception with its fallback.
- **Change** the size bound's unit: "one fresh context window" is a host-capacity claim. The product
  already frames the same idea in responsibility terms ("未参与讨论的合格实现者能开始且不猜共享承诺"),
  so the bound should be restated as *a slice a session with no prior context can finish without
  guessing a shared commitment*.
- **Drop** the tracker/label mechanics (`ready-for-agent`, blockers as native links) — those are the
  source repo's distribution channel, not the mechanism.
- Carrier: a method body (e.g. `methods/change-slicing.md`) bound by the Charter, plus one line in
  `methods/README.md`'s selection table. Not into the Profile.
- Real SDK/runtime dependency: **none**.

**6) Draft text and verification plan (not executed)**

Draft (candidate method rule):

> Decompose so that each part can be shown working on its own: narrow, but complete through every
> layer the behavior passes. The test is one question asked of each part — *what can be shown working
> when this alone is done?* If the answer is a layer ("the schema is done"), the part is not a slice.
> Make each part finishable by a session that has not seen this plan. One shape does not decompose
> this way: a single mechanical change whose blast radius spans the codebase, where no part can be
> green alone. Do that one as expand (add the new form beside the old, nothing breaks), then migrate
> call sites in batches sized by blast radius, then contract (delete the old form once no caller
> remains); where even a batch cannot be green alone, its parts share one integration point and green
> is promised only there.

Verification plan: take one already-decomposed change from a past task and apply only the demo-path
question; record which parts have no answer. Boundary: this tests the question's discriminating power
on a real decomposition, not the claim that vertical slicing improves delivery outcomes, which is not
asserted here.

---

### MG-3 · Test-design anti-patterns with their tells

**1) Mechanism, trigger, anchors, read status**

| | |
| --- | --- |
| Mechanism | Two named test defects with a *detectable tell* and a stated repair: **implementation-coupled** (the test breaks when you refactor and behavior did not change) and **tautological** (the assertion recomputes the expected value the way the code does, so it can never disagree with the code) |
| Trigger | Tests exist or are being written and something must decide whether they are worth keeping |
| Provisional locus | F (whether the evidence can disagree with the artifact) ← E (who writes them) |

Anchors: `skills/engineering/tdd/SKILL.md` L28–32 (§Anti-patterns, incl. the `expect(add(a,b)).toBe(a+b)`
form and "Expected values must come from an independent source of truth: a known-good literal, a
worked example, the spec"); `skills/engineering/tdd/tests.md` §Good Tests L3–24, §Bad Tests L25–77
(the interface-bypass pair `db.query(...)` vs `getUser(user.id)`, and the tautological pair
`items.reduce(...)` vs the literal `15`); `docs/engineering/tdd.md` §Common questions. Read: full.

**2) Operation, conditions of validity, failure modes, counterexamples**

- *Operation.* For each test, ask the tell question rather than arguing about style: *does this test
  break when I rename an internal function?* (implementation-coupled) and *where did the expected
  value come from?* (tautological). Both repairs are stated: assert through the public interface; take
  the expected value from a known-good literal, a worked example, or the spec.
- *Conditions of validity.* Requires a public interface to assert through; where the only reachable
  surface is internal, the finding is about the module shape, not the test (this is the same
  conclusion the product already reaches in `local-defect-feedback-loop.md` §Method 4: "If no suitable
  seam exists, report that as a design fact rather than forcing a test-only abstraction"). Also
  requires a stated list of what the test is allowed to mock — already covered in the product by
  `guide-mock-adapter-choice.md` §Rules 2.
- *Failure mode.* A suite of green tests that cannot disagree with the artifact: "the test passes by
  construction". The stronger version, which the source states as a general risk of the loop itself,
  is that this is *reached from the other direction* by running a test-first loop where no independent
  source of truth exists.
- *Counterexamples.* The two worked pairs in `tests.md` are usable as-is in a product guide, because
  they are language-neutral in shape (a side-channel read vs an interface read; a recomputed sum vs a
  literal).

**3) A–F loci and professional concern; Profile and call timing**

- **F** owns the judgment that evidence can disagree; **E** owns the repair. Both anti-patterns are
  *evaluation* findings about implementation-authored evidence, so F must state them and must not
  author the fix silently (`profiles/evidence-evaluation.md` §常见误区: "评价者顺手改成作者，再声称独立").
- Professional concern: *Correctness*.
- Profile: `profiles/evidence-evaluation.md` (F) primary; `profiles/implementation.md` (E) for the
  repair. Call timing: whenever self-check output is being offered as input to an F judgment —
  precisely the moment `profiles/implementation.md` §交出 describes ("自测证据").

**4) Current product: exact text, what is covered, the specific gap, why**

Covered — `profiles/evidence-evaluation.md` §关键问题 already asks the right negative-control
question and §常见误区 already rejects the wrong input:
> "只验证"能跑通"，不设计能揭示错误的负控制。" / "把文档、字段非空、自测输出当作已验证结论。"
> "什么观察能把"成立"与"不成立"分开？关键负控制是什么？"

Gap — the profile states the *requirement* (a negative control, an observation that can separate
true from false) but the core has **no operation for detecting the two ways a test silently fails to
be one**. "把自测输出当作已验证结论" names the symptom; the tautology and the implementation-coupling
are the two mechanisms that make the symptom indistinguishable from a real green. Without them F can
only demand "a better negative control" without being able to point at what is wrong with the one in
front of it. `methods/behavior-claim-evaluation.md` §Method 2 ("Compare baseline and treatment with
the same command, data and environment") is about a comparison being valid, not about a check being
*able to fail at all*.

Why worth absorbing: it converts a correct but unactionable F requirement into two checkable
questions, and it is the cheapest available defence against the product's single most dangerous
false signal (a green self-check offered as evidence).

**5) Retain / change / delete; carrier; coupling; real-SDK dependency**

- **Retain** both tells and both repairs.
- **Change** the framing from "test anti-patterns" to a **negative-control validity check** on
  evidence, so it lands where the product already has a home (F's evidence evaluation) rather than as
  test-craft.
- **Delete** nothing; the upstream text carries no ceremony to strip.
- Carrier: extend `methods/behavior-claim-evaluation.md` §Use/§Method with the two tells as
  invalidity conditions **or** add them to `methods/README.md` as a short on-demand guide beside
  `guide-mock-adapter-choice.md`. Extension is the smaller product change and keeps F's ownership.
- Real SDK/runtime dependency: **none** (the examples are language-neutral in shape).

**6) Draft text and verification plan (not executed)**

Draft (candidate addition to F's method §Method 3, which already decides whether a comparison is
valid):

> Before reading a green check as support, test whether it could have been red for this claim.
> Two shapes are green by construction and must be treated as invalid evidence until repaired:
> **(a) coupled to the implementation** — the check passes through an internal collaborator or a side
> channel instead of the interface actually under contract, and its tell is that it breaks when the
> implementation is renamed while behavior is unchanged; **(b) tautological** — the expected value is
> produced the way the artifact produces it, and its tell is that it cannot be derived from anything
> outside the artifact (a known-good literal, a worked example, or the accepted contract). Report
> either as an evidence defect, not as a product failure, and do not author the repair inside the
> evaluation.

Verification plan: on one existing fixture, apply the two tells and record whether each of the
fixture's checks survives an internal rename and whether its expected value is derivable from
something outside the artifact. Boundary: this measures the tells' discriminating power on known
checks; it does not establish a general claim about suite quality, and no such claim is made.

---

### MG-4 · Seam agreement as an accepted contract item (merged across four files)

**1) Mechanism, trigger, anchors, read status**

| | |
| --- | --- |
| Mechanism | The set of seams the change will be tested at is **decided and confirmed while the contract is being agreed**, not discovered during implementation; the agreed set is small (ideally one), prefers existing seams, and later phases are checked against it |
| Trigger | A behavior change is being turned into an accepted commitment, before implementation begins |
| Provisional locus | B (it becomes part of the accepted contract) → D (feasibility) → F (what it is checked against) |

This group is a **cross-file merge**: it exists only as the interaction of four statements, none of
which is sufficient alone.

| File | Statement | Anchor |
| --- | --- | --- |
| `to-spec/SKILL.md` | "Sketch out the seams at which you're going to test the feature. Existing seams should be preferred to new ones. Use the highest seam possible. … The fewer seams across the codebase, the better - the ideal number is one." + "Check with the user that these seams match their expectations." | L15–17 |
| `tdd/SKILL.md` | "**Test only at pre-agreed seams.** … No test is written at an unconfirmed seam. You can't test everything, so agreeing the seams up front is how testing effort lands on the critical paths and complex logic instead of every edge case." | L22 |
| `implement/SKILL.md` | "Use /tdd where possible, at pre-agreed seams." | whole body |
| `code-review/SKILL.md` | Spec axis checks the diff against the originating spec; the page adds that review checks only agreed seams were used | L8–9 + `docs/engineering/tdd.md` §Where it fits |

Read: full.

**2) Operation, conditions of validity, failure modes, counterexamples**

- *Operation.* Three moves: prefer an existing seam over a new one; take the **highest** seam that
  reaches the behavior; drive the count toward one. Confirm with the human, then let the affected
  methods consume the agreed set.
- *Conditions of validity.* A consumer that actually checks against the set. The source states the
  binding is **indirect** and that this is the reason to take it seriously early: "the binding is
  indirect: it runs through this document, which is exactly why the seam conversation is worth taking
  seriously here rather than deferring it to implementation" (`docs/engineering/to-spec.md` §Seams
  before prose).
- *Failure mode 1 (structural).* Nothing agrees the seams → "the precondition never fires and the run
  quietly becomes 'just write the code'" (`docs/engineering/implement.md` §Pre-agreed seams). This is
  the named weakest joint in the whole family.
- *Failure mode 2 (interaction quality).* The source records the most-reported friction: the prompt
  "lists candidate seams by name only, with nothing about what each one catches or misses, so you are
  choosing between labels" — with the stated fix being to ask for the trade-offs before answering, and
  the structural fix being to agree seams where the whole feature is in view rather than at one
  prompt.
- *Counterexample / boundary case.* The same page distinguishes a seam that is too shallow to catch
  the real bug pattern from a usable one, and states that where only a shallow seam exists, writing a
  test there "gives false confidence" and the absence of a seam **is itself the finding**. The product
  already owns the defect-path version of this; this group is about the *agreed-set* version.

**3) A–F loci and professional concern; Profile and call timing**

- **B** owns the contract the seams belong to; **D** owns whether the seam is real in the system
  (`methods/cross-module-design.md` §Method 3 already locates it); **F** owns whether the delivered
  version was checked at the agreed surface and nowhere else.
- Professional concern: *Correctness*; *Performance* only insofar as seam height trades against test
  speed.
- Profile: `profiles/behavior-domain.md` (B) at agreement time; `profiles/technical-planning.md` (D)
  to confirm the seam is real; `profiles/evidence-evaluation.md` (F) at evaluation time. Call timing:
  **at contract agreement**, and again at evaluation. Not a mandatory artefact — a *set small enough to
  state in the contract* is the requirement, not a new document.

**4) Current product: exact text, what is covered, the specific gap, why**

Covered — the product has the *individually* correct pieces and states them well.
`methods/cross-module-design.md` §Method 3:
> "Locate the seam where behavior can be substituted or tested. Use the actual dependency shape to
> choose a useful test path: in-process, locally replaceable, remotely owned behind an adapter, or a
> true external dependency."

and `guide-mock-adapter-choice.md` §Rules 5 owns the seam-discipline half:
> "One adapter means a hypothetical seam; two adapters (usually production + test) mean a real one —
> don't introduce a port unless at least two adapters are justified. Internal seams stay private…
> The interface is the test surface."

Gaps — three, all specific:
1. **Who locates the seam is D; when it is agreed is never stated.** The product's seam appears in a
   *method the planner runs*, so it lands in the Plan, not in the accepted contract. There is no text
   making the seam set something B agrees and F checks against.
2. **No count discipline and no preference rule.** "The fewer seams, the better — the ideal number is
   one" and "existing seams should be preferred to new ones" are exactly the constraints that keep a
   change testable without inventing surface, and neither appears in the core.
3. **No consumer.** `methods/cross-module-design.md` §Method 3 says do not expose internal seams, and
   §Method 4 says "Replace or remove old coverage only when the replacement demonstrably covers its
   accepted claim" — but nothing in the core *checks* that only the agreed seam was used. The
   product's `charters/template.md` has an `Applicable methods` field but no field or sentence that
   carries an agreed verification surface from B to F.

Why worth absorbing: it is the only mechanism found that binds a *verification surface* into the
accepted contract without adding a gate, and the product's own D→F handoff currently has no such
link — F must re-derive the right surface, which is precisely the independence defect the Backbone's
F section warns about ("依据冲突或缺失返回 B/C/D").

**5) Retain / change / delete; carrier; coupling; real-SDK dependency**

- **Retain** the three moves (existing > new, highest, tend to one) and the indirect-binding
  observation with its "take it seriously early" consequence.
- **Change** the carrier: upstream puts it in a spec document that the source repo publishes to a
  tracker. The product's carrier is the Contract/Plan handoff — the natural landing is
  `profiles/behavior-domain.md`'s "按需方法入口" plus either a clause in
  `methods/cross-module-design.md` §Method 2–3 or a small method body. **Do not** create a new
  artefact type; the product already rejects "三份文件".
- **Delete** the tracker/host mechanics and the `/skill` invocation convention.
- Real SDK/runtime dependency: **none**.

**6) Draft text and verification plan (not executed)**

Draft (candidate clause for the B-facing side, phrased to stay inside B's existing ownership):

> When the contract for a behavior is being settled, settle with it the surface the behavior will be
> observed at. Prefer a surface that already exists; among the surfaces that reach the behavior, take
> the highest one, because a higher surface survives more implementation change. Keep the set small —
> the useful target is one — since every extra surface is another thing the implementation must keep
> true. This set is part of the contract, not an implementation detail: later evaluation checks the
> delivered behavior at these surfaces and does not quietly accept a different one. Where no surface
> reaches the real case, that absence is a finding about the design, and saying so is the correct
> outcome.

Verification plan: on one bounded change, record (a) whether the seam set was stated before any
implementation existed, and (b) whether the evaluation used the same surface. Boundary: this tests
whether the clause is *observable in a trace*, not whether it improves outcomes.

---

### MG-5 · Acceptance criteria that can fail

**1) Mechanism, trigger, anchors, read status**

| | |
| --- | --- |
| Mechanism | An acceptance criterion is only a criterion if some observation would make it **false**, and if it is actually false at the version the work starts from. Two checks, both cheap, applied to each criterion at authoring time |
| Trigger | Acceptance criteria are being written for a commitment or a work item |
| Provisional locus | B (the criterion is the observable commitment); F consumes it |

Anchor: `docs/engineering/triage.md` §Common questions, the entry beginning "The acceptance criteria
graded nothing: some passed before any work was done." It names the three recurring shapes — "a
criterion already true at the base commit, a criterion that can only be satisfied by work another
ticket owns, and one that restates the request rather than deriving from the artifact" — and the
check: "For each criterion, name the observation that would show it false, and confirm it fails at the
commit the implementer starts from." Companion: `skills/engineering/triage/AGENT-BRIEF.md` §Complete
acceptance criteria ("Each criterion should be independently verifiable", with a good/bad pair), and
`skills/engineering/to-tickets/SKILL.md` (ticket template `- [ ] Acceptance criterion`). Read: full.

**2) Operation, conditions of validity, failure modes, counterexamples**

- *Operation.* Per criterion: (1) name the observation that would show it false; (2) confirm that
  observation is currently red at the base version. Both are read-only acts on an existing revision.
- *Conditions of validity.* A fixed base version to test "already true" against — without it only the
  first check applies. And the criterion has to be about the artifact, not about the request.
- *Failure mode.* A criterion that "restates the request rather than deriving from the artifact"
  passes trivially and grades nothing; the family then closes work whose acceptance signal was never
  capable of being negative. This is the B-side mirror of MG-3's tautology: the same defect
  (an assertion that cannot fail) arising one layer earlier, in the commitment rather than the test.
- *Counterexample.* "if the whole change fits in one context window, you don't need this skill at all"
  — the source's own boundary against applying criterion-authoring ceremony to a change whose
  acceptance is self-evident.

**3) A–F loci and professional concern; Profile and call timing**

- **B** owns the criterion. This is the clearest B-only operation in the package. **F** consumes it
  and, per `profiles/evidence-evaluation.md` §召回, returns a missing/invalid basis to B.
- Professional concern: *Correctness*; *Delivery risk* when criteria are supplied to a downstream
  worker.
- Profile: `profiles/behavior-domain.md` (B). Call timing: **when the criterion is written** — this is
  the only point at which the second check is cheap. `profiles/behavior-domain.md` §关键问题 already
  asks "交付后，外部应该看到什么？什么能把正确与错误区分开？" — this group is the operation behind that
  sentence.

**4) Current product: exact text, what is covered, the specific gap, why**

Covered — `profiles/behavior-domain.md` §心智模型 states B's product precisely and already includes
the "can it be wrong" intent:
> "B 的产物是**可观察行为约定**：场景、交互、输出、异常与接受条件；例子用来暴露漏项与冲突。"
> §关键问题: "交付后，外部应该看到什么？什么能把正确与错误区分开？哪些场景、异常、空值与边界还没覆盖？现有例子有没有互相矛盾？"

Gap — "什么能把正确与错误区分开" is asked about the *contract*, and there is no test for whether an
*individual criterion* can be false, nor for the "already true at the base version" case. The core
also has no home for the second failure shape — a criterion that can only be satisfied by work outside
this change — which is a *boundary* defect, i.e. exactly the class the Backbone's B section says must
surface rather than be silently resolved ("冲突要在约定正文显露，不能在正文里悄悄解决"). Neither
`methods/behavior-claim-evaluation.md` (F: baseline vs treatment) nor
`methods/local-defect-feedback-loop.md` (E: existing failure) covers criterion authoring.

Why worth absorbing: it is a two-question read-only check, it sits exactly in the B gap the product's
own profile acknowledges, and it fires at the cheapest possible moment. It also gives F a legitimate
ground to return a criterion to B instead of judging against a criterion that cannot fail — closing a
loop the Backbone already requires.

**5) Retain / change / delete; carrier; coupling; real-SDK dependency**

- **Retain** both checks and the three failure shapes.
- **Change** the trigger from "triage of incoming work" to "B writing any acceptance criterion" —
  upstream reaches it through an issue-triage path that the product does not have and does not want.
- **Delete** the tracker-specific scaffolding.
- Carrier: one clause in `profiles/behavior-domain.md`'s B section (the §关键问题 list plus a one-line
  operation), or a two-line entry in the B-facing method. Keeping it *in the Profile* is defensible
  here, unusually, because it is a question the Profile already asks — the operation that answers it
  is short and its home is the §关键问题 list. Flag for the gate: this is the one group in this package
  where inlining into a Profile may beat a method body.
- Real SDK/runtime dependency: **none**.

**6) Draft text and verification plan (not executed)**

Draft (candidate B-side operation, to sit beside the existing §关键问题 entry):

> For each acceptance condition, name the observation that would show it false, and check that
> observation is currently negative at the version the work starts from. Two shapes look like
> conditions but grade nothing: one already true at the starting version, and one that can only be
> satisfied by work outside this change's boundary — the second is a scope statement, not an
> acceptance condition, and belongs in the boundary or in the other change.

Verification plan: take an existing accepted contract from the package's own fixtures and apply both
checks to its acceptance list; record which conditions fail each check. Boundary: the check's
sensitivity on real conditions, not a claim about downstream outcomes.

---

### MG-6 · Durable decision memory: the ADR gate, the minimal record, and the rejection record

**1) Mechanism, trigger, anchors, read status**

| | |
| --- | --- |
| Mechanism | Two durable records with different bars. (A) A decision record is written only when **all three** hold — hard to reverse, surprising without context, the result of a real trade-off — and it is then **short** (a title plus one to three sentences). (B) A **rejection** record exists so the same request does not have to be re-litigated; it is one file per rejected *concept*, with a durable reason and the list of prior requests |
| Trigger | (A) a decision is being made that a later reader will need the *why* for; (B) a request is being closed as not-to-be-done |
| Provisional locus | C (meaning and rule ownership) → D/B (the decisions themselves) |

Anchors: `skills/engineering/domain-modeling/SKILL.md` §Offer ADRs sparingly; `ADR-FORMAT.md` §Template
L7–15, §Optional sections L17–23, §Numbering L25–27, §When to offer an ADR L29–37, §What qualifies
L39–47; `docs/engineering/domain-modeling.md` §Two artifacts, two bars (L31–45) and §Common questions
(L52–74); `skills/engineering/triage/OUT-OF-SCOPE.md` §File format, §Naming the file, §Writing the
reason, §When to write to `.out-of-scope/`; the source repo's own `.out-of-scope/*.md` (three
instances). Read: full.

**2) Operation, conditions of validity, failure modes, counterexamples**

- *Operation (A).* Before writing: run the three gates. "If a decision is easy to reverse, skip it:
  you'll just reverse it. If it's not surprising, nobody will wonder why. If there was no real
  alternative, there's nothing to record beyond 'we did the obvious thing.'" Then write the minimum:
  "An ADR can be a single paragraph. The value is in recording *that* a decision was made and *why*,
  not in filling out sections." Optional sections (status, considered options, consequences) "only
  … when they add genuine value. Most ADRs won't need them."
- *The qualifying categories (A) — the operational part, seven of them:* architectural shape;
  integration patterns between contexts; technology choices that carry lock-in ("Not every library:
  just the ones that would take a quarter to swap out"); boundary and scope decisions, where "The
  explicit no-s are as valuable as the yes-s"; **deliberate deviations from the obvious path** ("These
  stop the next engineer from 'fixing' something that was deliberate"); constraints not visible in the
  code (compliance, partner SLA); rejected alternatives where the rejection is non-obvious ("otherwise
  someone will suggest GraphQL again in six months").
- *Operation (B).* One file per concept, not per request; a relaxed design-document format for the
  reason; a **durability test** on the reason: "Avoid referencing temporary circumstances ('we're too
  busy right now'); those aren't real rejections, they're deferrals." Read the whole directory before
  evaluating a new request, and match **by concept rather than keyword** — the source's own example is
  "night theme" matching `dark-mode.md`.
- *Sharp boundary case, stated in the source and worth preserving verbatim in substance:* if something
  is closed as out of scope **because it is already implemented**, do *not* write a rejection record —
  "That's a built feature, not a rejected one; recording it would poison the dedup checks with false
  rejections." This is the exception that keeps mechanism (B) from decaying; it is exactly the kind of
  case that gets lost when a method is compressed.
- *Failure mode (A), documented and cross-model.* "Left unchecked, models treat 'write to
  `CONTEXT.md`' as permission to persist every answer you give, and the file turns into a running
  spec. This is the most-reported problem with the skill, across several models." The stated repair is
  a direct instruction to make it concise and remove implementation detail, and the source explicitly
  warns against the tempting fix: split into a context map only *after* the file is lean, because
  "splitting a bloated file just gives you several bloated files."
- *Honest counter-argument the source records (keep it attached).* A glossary's value is contested:
  "the sharpest public pushback is that a term and its plain-English expansion get the same result
  from the model, and that the vocabulary really compresses communication between the humans who share
  it." And: "an unreviewed, agent-authored glossary is worse than none: it becomes confident-sounding
  lore that later sessions treat as truth."

**3) A–F loci and professional concern; Profile and call timing**

- **C** owns decision-record content where the decision is semantic; **D** where it is technical;
  **B** where it is behavioral. The *gate* is a discipline, not a new responsibility, and the source
  is explicit that the record is "offered, not assumed".
- Professional concern: *Maintainability/Delivery risk* — the record's job is to stop a later session
  re-deciding or silently reversing something deliberate.
- Profile: `profiles/behavior-domain.md` (B/C) is the natural home; `profiles/technical-planning.md`
  (D) for the technical-decision case. Call timing: at the moment a decision is made and its reversibility
  is still assessable; and at the moment a request is refused.

**4) Current product: exact text, what is covered, the specific gap, why**

Covered — almost nothing on the decision-record side, but the *intent is registered*. Two places name it
and neither has a body:
- `profiles/behavior-domain.md` §按需方法入口（候选）: "**决定记录方法**：留下接受的规则、范围与 owner，避免第二份定义。"
- `methods/README.md` §Selected methods: its table has exactly three rows and two on-demand guides;
  **there is no decision-record method, and no entry for one.**

Adjacent and correct, but different: `profiles/behavior-domain.md` §常见误区 already warns "把 C 当作词典
写作任务，每次重写全部领域模型" — that is the *anti-bloat* guard for the glossary half. And
`methods/README.md` §Deferred alternatives already defers `interrogate`/`code-review` lenses and
`DESIGN-IT-TWICE` — but the ADR mechanism has *never* been in scope, so it was neither adopted nor
deferred; it simply has no body. This matters at completion accounting: the group is `not-covered`,
not `pending` from a previous round.

Gap — four specific absences:
1. No gate for *when* a decision deserves a record (the three-condition test), so the product has
   `Do not open a second definition` as an intent with no criterion.
2. No minimal-record discipline (title + 1–3 sentences), and therefore no defence against record
   inflation, in a package whose central risk is verbosity.
3. No coverage list, so a planner has no way to notice that a lock-in technology choice or a
   deliberate deviation from the obvious path went unrecorded — and those two categories are exactly
   what stops a later session from "fixing" a deliberate decision.
4. No rejection record at all. The product has no mechanism to keep a refused request from returning
   as new, and `.out-of-scope/`'s durability test (deferral ≠ rejection) is the discriminating rule
   that makes such a record trustworthy rather than an excuse.

Why worth absorbing: it is the product's largest genuinely uncovered C-locus area, the Profile already
points at it, the `methods/` selection table already reserves a place for method bodies, and the
"deliberate deviation" + "constraint not visible in the code" categories are the two record types whose
absence is invisible until a later session reverses a decision that was never written down.

**5) Retain / change / delete; carrier; coupling; real-SDK dependency**

- **Retain** the three-gate test, the minimal format, the sequential-numbering rule, the seven
  qualifying categories, and (B) the concept-not-keyword matching plus the durability test plus the
  already-implemented exception.
- **Change** the addressability: upstream ties the glossary to a specific filename `CONTEXT.md` and
  ADRs to `docs/adr/`. The product must not hard-code those paths as a *requirement* — the durable
  part is "one authoritative place per meaning, discoverable from the accepted contract", and the
  existing `setup-matt-pocock-skills`-style per-repo mapping (MG-11) is how a local convention would
  be named. Flag for the gate: whether the product wants a named local convention at all, or leaves
  the location to the task.
- **Delete** the C-vs-D ownership ambiguity risk: the source offers ADRs for both domain and technical
  decisions in one file. The product's Backbone separates C from D, so the method must state that the
  *record's* content stays with whoever owns the decision — the record itself creates no ownership.
  `ADR-FORMAT.md` implicitly assumes one owner ("a decision"); the product cannot.
- Carrier: **a new method body** (`methods/decision-record.md` or similar) bound by the Charter, plus a
  row in `methods/README.md`'s selection table. This is the one group where a new method file is the
  right answer, because the Profile already declares the need and `methods/README.md` structurally
  reserves the slot.
- Real SDK/runtime dependency: **none**.

**6) Draft text and verification plan (not executed)**

Draft (candidate method §Method, condensing the two records):

> **Record a decision when all three hold:** reversing it later is expensive; a competent reader
> would otherwise ask why it was done this way; and there were genuine alternatives and this one was
> chosen for a stated reason. Miss any one and there is no record — an easily reversed decision will
> just be reversed, an unsurprising one is nobody's question, and one with no real alternative records
> that the obvious thing was done. Write the minimum that carries the *why*: a title and one to three
> sentences. Add status, considered options or consequences only where they carry weight.
> Record in particular: a deliberate deviation from the obvious path (otherwise a later session
> "fixes" it), and a constraint that cannot be seen in the code (a compliance limit, an external
> contract). **Keep the record's content with the owner of the decision:** the record is a memory, not
> a second authority.
>
> **Record a refusal** so the same request does not return as new: one file per rejected *concept*
> (not per request), carrying the decision, a reason that survives the circumstance — "we are too busy
> now" is a deferral, not a refusal — and the requests already refused on it. Match a new request by
> concept, not by wording. Do not record a refusal for something that was closed because it already
> exists: that is a built feature, and filing it as a rejection corrupts exactly the check this record
> exists to serve.

Verification plan: (a) apply the three gates to a sample of decisions actually taken in this session
and record disagreements between the two authors of the judgment; (b) test the rejection record by
feeding the mechanism a request that is a paraphrase of an existing rejection and observing whether
the concept match fires. Boundary: (a) measures the gate's discriminating power, not whether records
improve later work; (b) measures matching, not dedup effectiveness.

---

### MG-7 · Glossary discipline: what a term entry is, `_Avoid_`, and the drift failure

**1) Mechanism, trigger, anchors, read status**

| | |
| --- | --- |
| Mechanism | One canonical term per concept, with the rejected synonyms recorded beside it (`_Avoid_`), each defined as what the thing **is** (one or two sentences) rather than what it does; only project-specific concepts qualify; general programming concepts are excluded even when heavily used. Written inline **when** the term resolves, not batched at the end |
| Trigger | Two words are in use for one concept, one word is doing several jobs, or a term is about to be relied on by a second party |
| Provisional locus | C |

Anchors: `CONTEXT-FORMAT.md` §Structure L3–23 (the term/`_Avoid_` shape with three worked entries) and
§Rules L25–30 (the four rules, including "Define what it IS, not what it does" and the "is this unique
to this context, or a general programming concept?" filter); `skills/engineering/domain-modeling/SKILL.md`
§During the session (the five moves: challenge against the glossary; sharpen fuzzy language; concrete
scenarios; cross-reference with code; update inline) and the explicit "It is a glossary and nothing
else" prohibition; `docs/engineering/domain-modeling.md` §Two artifacts, two bars (L31–45),
§Cross-referencing, and where it stops (L46–51), §Common questions (L52–74). Companion instance:
`skills/productivity/teach/GLOSSARY-FORMAT.md` (same term/`_Avoid_` shape, plus "Add a term only when
the user understands it" and "Revise as understanding deepens"). Read: full.

**2) Operation, conditions of validity, failure modes, counterexamples**

- *Operation.* On encountering a term: if it conflicts with the recorded meaning, say so
  ("Your glossary defines 'cancellation' as X, but you seem to mean Y. Which is it?"); if it is vague
  or overloaded, propose a canonical term and a split ("do you mean the Customer or the User?"); if a
  relationship is being asserted, stress it with a concrete edge-case scenario; if the human states
  how something works, **check the code and surface the contradiction out loud** ("Your code cancels
  entire Orders, but you just said partial cancellation is possible, which is right?"); write the
  resolution immediately.
- *The `_Avoid_` rule is the load-bearing part.* Multiple words for one concept → pick one and list
  the others as rejected. Without it, the entry is a definition and not a *decision*, and the drift
  continues.
- *Conditions of validity.* A place to write (created lazily on the first resolved term); a second
  party who will read it; and a real project-specific concept. The source's own test is explicit:
  "is this a concept unique to this context, or a general programming concept? Only the former
  belongs."
- *Failure mode (documented, cross-model).* Glossary drift into a running spec, described above in
  MG-6; the same failure from this angle is that "merely reading `CONTEXT.md` for vocabulary is not
  this skill" — i.e. the passive habit and the active discipline are different jobs, and conflating
  them produces a file nobody maintains.
- *Stated limit (keep).* The cross-check covers code and committed records and **not** the team's
  issue history, so "a naming collision that was argued out and deliberately settled in a closed issue
  months ago gets surfaced as if it were new" (reported as open, with the workaround being a repo-local
  instruction file). Preserve as a boundary, not a flaw to hide.
- *Counterexample the source supplies.* The naming of the file itself is contested and the source
  refuses to settle it: the argument for a glossary name is strong, the argument for a context name is
  the map, and at least one user maintains a fork purely to rename it. This is an honest
  "no settled answer" that a product method should either adopt as a decision or drop — not silently
  resolve.

**3) A–F loci and professional concern; Profile and call timing**

- **C** owns the term and the rule. The cross-check move *consumes* code and E's facts without
  transferring ownership.
- Professional concern: *Correctness* of shared meaning; *Maintainability*.
- Profile: `profiles/behavior-domain.md` (C) primary; `profiles/intent-voice.md` (A/Voice) when the
  disagreement is about the problem statement rather than the concept. Call timing: at the moment a
  term is disputed or relied upon by another party — not as a project-wide modelling pass.

**4) Current product: exact text, what is covered, the specific gap, why**

Covered — `profiles/behavior-domain.md` §心智模型 has the right *shape* and one good anti-pattern:
> "C 的产物是**领域语义**：概念、关系、状态、不变量、规则与上下文边界；同一规则只应有一个 owner。"
> §常见误区: "把 C 当作词典写作任务，每次重写全部领域模型。"
> §关键问题: "这个词在这里究竟指什么？和其他上下文里的同名概念是不是一回事？这条规则由谁拥有？"

The Backbone's C section adds the ownership rule ("界定概念、关系、状态、不变量、业务规则和上下文边界；
解释同名概念何时不同、同一规则由谁拥有") and the handoff ("相关概念、规则与边界及区分性例子").

Gap — three, and the third is the substantive one:
1. **No `_Avoid_` mechanism.** The product asks "这个词在这里究竟指什么" but has no rule that a
   resolution must also record **the words being given up**. That recording is what makes the
   resolution binding on the next session; without it the same ambiguity returns.
2. **No entry standard.** "Define what it IS, not what it does" and the one-or-two-sentence bound are
   absent, and the product has no equivalent of "only project-specific concepts belong" — which is the
   rule that prevents the C artefact becoming a general programming dictionary.
3. **No cross-check move and no stated limit.** The strongest single operation in this family —
   compare the human's statement against the code and surface the contradiction *before* changing
   either — has no product equivalent. `profiles/behavior-domain.md` §常见误区 says conflicts must
   surface in the contract rather than be resolved inside it, which is the *same principle applied to
   a different pair of sources*; the code-vs-statement case is missing. Its limit (it cannot see
   already-settled history) is also worth inheriting, because a product method that omits the limit
   invites over-trust.
4. The honest counter-argument (a glossary may not improve model performance; its value may be
   human-to-human) is not represented anywhere, and the product's own Position depends on C being
   real work. Whether to carry the counter-argument is a gate call; flagging it because the source
   treats it as substantive rather than as a caveat.

Why worth absorbing: it is the only set of concrete *operations* found for the C locus that the
product currently expresses as questions, and the `_Avoid_` + entry-standard pair is what makes a C
artefact survive contact with a second session.

**5) Retain / change / delete; carrier; coupling; real-SDK dependency**

- **Retain** `_Avoid_`, the "define what it IS" rule, the project-specific filter, the four session
  moves, and the cross-check operation with its stated limit.
- **Change** the artefact variable: the source fixes one filename; the product should state the
  *properties* (one authoritative place per meaning; discoverable from the accepted contract) and let
  the per-repo convention be named at configuration time (MG-11).
- **Delete** nothing structural; the multi-context map (`CONTEXT-MAP.md`) is a real feature but is a
  *scale* answer — carry it as a boundary case, not as the default, in line with the source's own
  warning against splitting a bloated file.
- Carrier: the C half belongs with `profiles/behavior-domain.md`'s method entries. Because MG-6 and
  MG-7 are the two halves of one "durable meaning and decision" concern, the gate should consider one
  method body covering both (a decision-record method that also carries the term-entry standard),
  rather than two files — the source keeps them in one skill for exactly this reason.
- Real SDK/runtime dependency: **none**.

**6) Draft text and verification plan (not executed)**

Draft (candidate rule set for the C-facing method):

> When a concept is settled, write it down at once, in the one place that owns it: the term, what the
> thing **is** in one or two sentences (not what it does), and the words that are now ruled out.
> Recording the rejected words is what makes the resolution hold; without them the next session
> reintroduces the ambiguity under a different name. Keep out anything that is not specific to this
> project: a general programming concept belongs in general knowledge, not here, however much this
> project uses it. When someone states how something works, compare that statement with what the code
> actually does and surface the disagreement before changing either — the pair (statement, code) is
> the cheapest place to catch a divergence. This comparison reaches the code and the written records;
> it does not reach what was settled and closed elsewhere, so a collision that looks new may already
> have been decided, and the human is the one who knows.

Verification plan: take one ambiguous term currently in use, resolve it under the rule, then have a
second reader reconstruct the term's meaning from the entry alone; record whether the rejected words
were needed to do so. Boundary: this measures the entry's sufficiency for a second reader, not whether
the vocabulary improves agent output — the source itself leaves that contested and so does this
package.

---

### MG-8 · Document and context economy for agent-consumed text

**1) Mechanism, trigger, anchors, read status**

| | |
| --- | --- |
| Mechanism | Two budgets govern any text an agent reads — **context load** (the cost of always-loaded material on every turn, whether or not it fires) and **cognitive load** (the human's cost of knowing which documents exist). Levers: context pointers whose *wording* decides whether the material is reached; an information hierarchy with progressive disclosure; completion criteria with **clarity** and **demand**; **leading words** as pretrained anchors; and pruning by the **no-op test** (does this line change behaviour versus the default?) |
| Trigger | Any text that an agent will read — a method, a profile, a charter, a pointer, a description |
| Provisional locus | C (meaning economy) with the Driver/assembly layer (what is loaded at all) |

Anchors: `skills/productivity/writing-for-agents/SKILL.md` §Context pointers L10–19, §The two loads
L20–28, §Information hierarchy L29–44, §Steps and completion criteria L45–53, §When to split L54–60,
§Leading words L61–75, §Pruning L76–81; `writing-for-agents/SKILL-MECHANICS.md` §Invocation L5–15,
§Splitting by invocation L16–19, §Router skills L20–22; `.agents/invocation.md` §Model-invoked vs
user-invoked L1–13 and §Dependencies between them L14–23; `.agents/writing-docs.md` §Page structure,
§Conventions, §Done when; `docs/productivity/writing-for-agents.md` §The two loads, §The levers;
`skills/engineering/ask-matt/PHASE-BOUNDARIES.md` (the context-boundary tree: continue / clear /
handoff / subagent / compact, with the primary-vs-secondary source loss table) and `ask-matt/SKILL.md`
§Context hygiene (the smart-zone limit). Read: full.

**2) Operation, conditions of validity, failure modes, counterexamples**

- *Operation (the levers, in the source's own order).*
  - **Pointer wording decides reachability, not the target:** "A must-have target behind a weakly
    worded pointer is a variance bug: sharpen the wording first, and inline the material only if
    sharpening fails."
  - **One trigger per branch:** "Synonyms that rename a single branch are one branch written twice;
    collapse them." Plus: front-load the leading word; cut identity the body already carries.
  - **Disclosure test:** "inline what every branch needs, and push behind a pointer what only some
    branches reach."
  - **Completion criteria:** clarity (can the agent tell done from not-done) and **demand** (how much
    it requires), with the failure being premature completion driven by *visible post-completion
    steps*; defence order is sharpen the bound first, and hide later steps only if the bound is
    irreducibly fuzzy **and** the rush is observed — and hiding only works across a real context
    boundary. **Legwork** (the digging latent in the wording) is what demand buys.
  - **Leading words:** a compact concept already in pretraining, repeated as a token and never as a
    sentence; it anchors twice — execution in the body, invocation in the pointer. Worked refactors
    given: "fast, deterministic, low-overhead" → *tight*; "a loop you believe in" → *red*, which
    "turn[s] a fuzzy gate into a binary observable state".
  - **Negation is a failure mode, not a technique:** "steering by prohibition drags the forbidden
    behaviour into context and makes it *more* available… _Don't think of an elephant_… Prompt the
    positive"; a prohibition earns its place only as a hard guardrail that cannot be phrased
    positively, and then must be paired with the positive target.
  - **Pruning:** single source of truth; duplication "inflates a meaning's prominence on the ladder
    past its real rank"; **environment as a cache** — a document restating `package.json` scripts
    "earns its load only when the lookup is expensive", so "cache what the agent cannot find by
    looking"; relevance/sediment; and the no-op test, whose verdict is **model-relative** and "settle[d]
    … by running the document, not by debate". When a sentence fails, "delete the whole sentence
    rather than trim words from it" — because agents told to shorten "optimise for length, because
    length is the thing they can see".
- *Conditions of validity.* A named reader (agent vs human) and a named default to compare against;
  the no-op test is only answerable relative to a model's default, so it needs either a run or a
  stated assumption.
- *Counterexamples.* (i) The length-vs-behaviour trap above — a length instruction does not change
  behaviour; the source's sibling illustration is "a four-hundred-line concision skill still leaves
  the model verbose, because the model reads the volume, not the plea". (ii) A leading word too weak to
  beat the default is itself a no-op: "_be thorough_ when the agent is already thorough-ish" — the fix
  is a stronger word, not a different technique.
- *Second mechanism in this group, genuinely distinct:* the **context-boundary decision** (continue /
  clear / handoff / subagent / compact) with its ordering rule — continue is ruled out first because
  it is the only move that keeps the session as a primary source, and "every move except Continue turns
  a primary source into a secondary source". The source states plainly that these are judgement calls
  and that "the value is in asking them in order, at the boundary rather than in the middle of the
  work". This is the *same trade* as the pointer/cognitive-load trade, one level up.

**3) A–F loci and professional concern; Profile and call timing**

- **C** owns meaning economy inside a document. The *assembly* half (what is loaded into a startup
  prompt, what is bound by a Charter) is the **Driver** connector's, and the Backbone already gives
  Driver exactly the right boundary ("Driver 留在逻辑编排层", "Procedural sufficiency … 只检查影响本次继续
  的内容，不要求材料齐套").
- Professional concern: *Maintainability* and *Cost* (context is a real, metered resource).
- Profile: `profiles/driver.md` for the load/binding decisions; `profiles/behavior-domain.md` (C) for
  term economy. Call timing: whenever a document is authored or a method is bound — i.e. the assembly
  step in `professional-workflow/README.md` §Use step 4, and the Charter's `Applicable methods` field.

**4) Current product: exact text, what is covered, the specific gap, why**

Covered — the product already implements the *structural* half, and it should be said plainly that it
did so before reading this source: `charters/template.md`'s `Applicable methods` ("Bind only methods
needed for this task; their bodies add no authority, trigger, or scope") is a context-pointer rule;
`methods/README.md`'s on-demand guides state "When the support is needed, add the relevant guide to
this task's existing bound/read set; no mandatory loading for tasks without that need" — that is
progressive disclosure, correctly implemented; and the Backbone's Driver section already separates
procedural from substantive sufficiency, which is a sharper version of "a pointer is a reachability
mechanism, not a judgment".

Gaps — four specific absences:
1. **No pointer-wording discipline anywhere.** The product's pointers are the Charter's
   `Applicable methods` line and `profiles/*/按需方法入口` lists. Nothing states that the *wording* of
   those entries decides whether the method body is actually reached, nor gives the three pointer
   rules (front-load the leading word; one trigger per branch; cut redundant identity). Given that the
   package's whole delivery mechanism is a `cat` of files into a prompt, this is the highest-leverage
   missing rule in the group.
2. **No completion-criteria mechanism.** The product has sufficiency tests for *content* ("未参与讨论的
   合格实现者能开始且不猜共享承诺") but nothing about a *step's* done-condition, its demand, or premature
   completion. `charters/template.md` has no field for it, and the Backbone's procedural sufficiency
   doesn't cover it either.
3. **No no-op test and no explicit anti-bloat instruction beyond brevity.** `methods/README.md` and the
   Profiles repeatedly assert brevity as a *value* ("简洁不能变抽象原则集" is the plan's own
   constraint). The source states that this exact form of instruction fails: agents optimise for the
   length they can see, and a line is only removable if behaviour is unchanged. Without the no-op test
   the product has a value but no operation, which is the failure the source documents.
4. **No leading-word discipline or negation warning.** The product is bilingual: Profiles are Chinese,
   methods are English, and the Backbone mixes both. A "leading word" mechanism that depends on
   pretraining recruitment is affected by which language the anchor token lives in, and the product
   has no rule about it. Separately, the negative-instruction finding ("Don't think of an elephant")
   applies directly to a package whose §Limits sections are largely prohibitions — those are exactly
   the places most at risk of making the forbidden behaviour more available.

Why worth absorbing: the product *is* agent-consumed text, so this group improves every other group's
carrier; and the product's central risk (a method library that either bloats or flattens into abstract
principles) is precisely the risk these levers were built for. It is also the only group where the
product's existing design is *validated* by the source rather than extended — worth recording as
covered-by-design so it is not re-litigated.

**5) Retain / change / delete; carrier; coupling; real-SDK dependency**

- **Retain** both loads, the pointer rules, the disclosure test, completion criteria with
  clarity/demand and premature completion, leading words with the dual anchor, the negation finding,
  the no-op test, environment-as-cache, sediment, and the boundary tree's ordering rationale.
- **Change / strip intentionally:**
  - The **invocation axis** (`model-invoked` vs `user-invoked`, `description` as an always-loaded
    pointer, router skills, per-harness frontmatter flags) is **platform coupling** and must not enter
    the product as such. Its transferable core is one sentence: *a capability that is loadable on
    demand should not sit in every context, and what stays always-loaded must earn that place.* In the
    product that is the Charter's binding, not a `description` field.
  - The **`ask-matt` router** is a Claude-specific cure for accumulated cognitive load (a list of
    slash commands). Do not import the artefact; the transferable rule — *when the number of things a
    human must remember grows, one entry point that names them beats the human holding the list* — is
    already the job of `profiles/README.md` and `methods/README.md`.
- **Delete** nothing else.
- Carrier: the pointer-wording + no-op rules belong in the authoring home for the product's own text —
  i.e. as a short on-demand guide (`methods/guide-*.md`) that the *author* of a method or Charter
  binds, not as content inside every method. The Driver-facing load/binding half belongs in
  `profiles/driver.md`'s method entry list. Flag for the gate: whether the product wants an
  authoring guide at all, or treats its own 21 files as frozen enough that the rule is only needed for
  future method bodies.
- Real SDK/runtime dependency: **the no-op test is model-relative** — the source itself says it is
  settled by running the document, and disallows settling it by argument. Any adoption must therefore
  carry a real observation requirement (whose) rather than a rule. This is the one group in this
  package with a genuine runtime dependency, and it is a *veto* on claiming the rule works without an
  observation.

**6) Draft text and verification plan (not executed)**

Draft (candidate pointer-and-pruning clause):

> Anything that sits in an agent's context on every turn has to earn that place; anything only some
> branches need belongs behind a pointer to it. Whether a pointer is followed depends on the pointer's
> own wording far more than on its target, so write it as the thing plus the condition that should
> fire it — one condition per distinct branch, with the key word first. Keep the target of a
> must-have pointer sharp rather than inlining the material, and inline only if sharpening fails.
> Before deleting or keeping a line, ask what changes if it is gone: a line the reader already obeys
> by default costs context and changes nothing. That question is about the reader's default, not about
> taste, so settle a disagreement by running the document rather than by arguing about it. When a
> sentence earns deletion, delete the sentence — trimming words from it leaves the cost and hides the
> problem. Do not restate what the environment already answers; put in the document only what cannot
> be looked up.

Verification plan: for one candidate method body, list each line, state the default behaviour it is
supposed to change, and record which lines change nothing; then run the *reduced* body against the
same bounded task and observe whether the outcome differs. Boundary: this is model-relative and
task-bound; a single run does not establish the rule, and no claim of improvement is made here.

---

### MG-9 · Structured elicitation: design tree, frontier, rounds, facts vs decisions

**1) Mechanism, trigger, anchors, read status**

| | |
| --- | --- |
| Mechanism | Map a decision space as a **design tree**; ask, in each **round**, exactly the **frontier** — every decision whose prerequisites are already settled — and nothing whose answer depends on a question still open in that round. Facts are the agent's job (go and find them); decisions are the human's (ask and wait). Close only when the frontier is empty **and** the human confirms shared understanding |
| Trigger | A plan, contract, scope or value judgment is under-specified, and the person who owns the decision is available |
| Provisional locus | A (what is actually being asked for) → B/C (the decisions themselves) |

Anchors: `skills/productivity/grilling/SKILL.md` L6–8 (the tree, the frontier definition, whole-frontier
per round, wait before the next), L10–22 (the round template: numbered ❓ question, body, single
recommended answer on its own line), L24 (recompute; a dependent question belongs to a later round),
L26 (facts vs decisions, subagent dispatch, do not block the rest of the frontier), L28 (done =
frontier empty + explicit confirmation, "Do not act on it until the user confirms");
`docs/productivity/grilling.md` §The round, the frontier, and who decides; `grill-me/SKILL.md`;
`docs/productivity/grill-me.md` §It's a conversation, not an interview (the passivity failure) and
§Grillable and ungrillable; `docs/productivity/grilling.md` §Common questions (the frontier's limit;
the one-question-at-a-time opt-out). Read: full.

**2) Operation, conditions of validity, failure modes, counterexamples**

- *Operation.* Three rules, each with a reason: (i) a round contains only mutually independent
  questions, so no answer in a round can invalidate another question in the same round — the source
  answers the obvious objection this way; (ii) the next round is *recomputed*, not pre-written;
  (iii) each question carries the agent's recommended answer, which makes a round answerable by number
  ("1 yes, 2 the second option, 3 no, here's why") and forces a position rather than a menu.
- *Facts vs decisions (the part a product method should keep most carefully).* "Finding facts is your
  job, never the user's… Don't block on it: a running exploration is an unsettled prerequisite, so only
  the questions downstream of it wait… The decisions are the user's: put each to them and wait." The
  source states the failure explicitly: "An agent running `grilling` that answers its own decisions has
  broken the skill, not interpreted it liberally."
- *Conditions of validity.* A human who owns the decision and will answer. The source's own boundary:
  questions that need something to react to are **ungrillable** — "no amount of grilling will get you
  there", and the correct move is to build a throwaway and come back with a one-line answer. This is
  the mechanism's honest limit and belongs in the product as a scope condition, not as a caveat.
- *Failure modes, all documented.* (i) **Passivity:** "answering 'agreed, agreed, agreed' for forty
  questions and coming out with a plan the agent wrote and you nodded at. It feels productive because
  it was long. Nothing was actually decided, and the result carries a certainty it hasn't earned." The
  mitigation named is steering: push back, say when scope drifts, answer "I don't know" and mean it —
  "This skill is built to aid an engineer, not to replace one: what comes out tracks the quality of
  your answers, not the number of questions asked." (ii) **Scope too large:** a 200-question session
  usually means the subject should be split first, and long sessions "drift into the dumb zone, where
  the context window is full enough that the questions get worse". (iii) **The frontier is a
  judgement, not a computed graph:** "It can put two questions in one round and only afterwards
  discover that one answer should have changed the other. There is no guard against that beyond
  telling it, which reopens the affected branch in the next round." (iv) The recommendation can argue
  against the question as worded, so agreeing with it means answering "no" — a real format edge the
  source documents. (v) **Model sensitivity:** "Grilling leans on the model's own sense of how systems
  break, so give it your best one."
- *Counterexample / supported override.* The round default is contested and the source supports the
  opt-out rather than merely tolerating it: a one-line instruction for one-question-at-a-time is
  "genuinely contested", with practitioners who read slowly, work in a second language, or use the
  sequential format as focus scaffolding all reporting the sequential rhythm is better.

**3) A–F loci and professional concern; Profile and call timing**

- **A** owns the question that must be answered; **B/C** own the decisions produced. The mechanism
  itself is a *connector*: it belongs to whoever needs an input, and the Backbone's answer is that
  applicability is triggered, not role-bound ("按任务触发判断"). It is not a stage.
- Professional concern: cross-cutting; its own risk is *attention/quality of the elicited answers*.
- Profile: `profiles/intent-voice.md` (A/Voice) is the natural caller, since the output is a
  problem-definition and the loop is human-facing; `profiles/behavior-domain.md` (B/C) when the
  decisions are behavioral/semantic. Call timing: when a needed input is missing **and** a human owns
  it — the Backbone's own trigger rule ("在第一个依赖该判断的下游结论、承诺或动作形成前调用").

**4) Current product: exact text, what is covered, the specific gap, why**

Covered — the product registers the need twice and has a body for neither:
- `profiles/intent-voice.md` §按需方法入口（候选）: "**访谈/追问方法**：目标、约束或价值冲突不清楚时使用。"
- `profiles/behavior-domain.md` §按需方法入口（候选）: "行为规格/场景枚举方法：用例子与反例找漏项与冲突。"
and `profiles/intent-voice.md` §关键问题 supplies the *content* of good questions ("哪些是观察事实、哪些是
推断、哪些还是未知？哪个未知会改变方向？") without a procedure for asking them.

Also covered, and worth not duplicating: `profiles/intent-voice.md` §常见误区 already contains the
passivity failure in product form — "在未读回、未记录接受的情况下，把一次讨论当作已冻结的承诺" — and
the Backbone's Voice section already owns read-back and acceptance recording ("读回目标和行为…记录接受
决定"). So the *human-interface* half exists; what is missing is the *question-scheduling* discipline.

Gap — the specific absence is the **frontier/round scheduling rule and the facts-vs-decisions split**:
1. Nothing tells a caller in what order or grouping to ask questions, so the natural failure is either
   one-question-at-a-time drift or an undifferentiated question dump. The source records the second as
   the concrete symptom of a failed load: "It asked everything at once, with no recommendations, and
   never mentioned `CONTEXT.md`."
2. Nothing states that finding facts is the asker's job and must not be delegated to the human, which
   in the product's terms is a **professional-obligation** rule: asking a human for something the
   agent could have looked up is spending the human's scarce decision attention (the Backbone's
   "Owner 不应被要求编写 schema 设计"). Conversely, nothing states that the agent must **not** answer
   its own decisions — the product relies on independence rules elsewhere but has no rule for the
   elicitation loop itself.
3. Nothing states the completion condition (frontier empty **and** the human confirms), which is the
   mechanism's anti-premature-completion device and pairs directly with MG-8's completion-criteria
   lever.

Why worth absorbing: it is the only elicitation procedure found that has a *termination condition*
and an explicit division between what the asker must find out and what the human must decide — both of
which the product's A/Voice profile asks for and neither of which it can currently execute.

**5) Retain / change / delete; carrier; coupling; real-SDK dependency**

- **Retain** the tree/frontier/round structure, the mutual-independence rule with its reason,
  recompute-don't-pre-write, the recommendation line and its documented edge, the facts-vs-decisions
  split with the "only downstream questions wait" rule, the empty-frontier-plus-confirmation close, the
  ungrillable boundary, and the four failure modes with their mitigations.
- **Change** the surface: the source's template is a chat format with a specific glyph style. Keep the
  *properties* (numbered, individually answerable, one recommendation each, a round answers by
  number); drop the glyphs.
- **Delete** the platform coupling: "dispatch a sub-agent to find it" names a harness capability. In
  the product this is an ordinary delegation and should be phrased as such. Also drop the
  `CLAUDE.md`-specific opt-out wording and keep the substance (one-question-at-a-time is a supported
  rhythm).
- Carrier: a method body bound by the A/Voice Charter (e.g. `methods/decision-elicitation.md`) plus a
  `methods/README.md` row; the Profile keeps only the pointer, per EXECUTION-PLAN's "不要把所有经验内联进
  Profile".
- Real SDK/runtime dependency: **the asker's model matters** — the source states grilling quality
  depends on the model's own sense of how systems break. Any claim that the procedure produces good
  questions needs a real run with a named model; the *procedure* is model-independent, the *quality
  claim* is not.

**6) Draft text and verification plan (not executed)**

Draft (candidate method §Method):

> Treat the subject as a tree: each decision hangs off the decisions that must be settled first. Ask
> in rounds. A round contains exactly the questions that can be answered now without assuming an
> answer you have not heard — never a question whose answer depends on another question still open in
> the same round. Put your own recommended answer with each question, and number them, so the answers
> can come back by number. Recompute the next round from what the answers settled; do not prepare it
> in advance.
> Two jobs are not the same job. Finding facts is yours: if a question can be answered by looking at
> the system, look, and do not spend the human's attention on it. Deciding is theirs: put each decision
> to them and wait — a question you answer yourself has produced your opinion, not their decision. A
> running look-up is an unsettled prerequisite, so only the questions downstream of it wait; ask the
> rest now.
> Stop when no question remains and the human confirms the shared understanding. Do not act on the
> result before that confirmation. Some questions cannot be answered by talking — anything that needs
> something to react to; stop asking and make something to react to instead. If the round count keeps
> growing, the subject is too large: split it and elicit the parts.

Verification plan: run the procedure on one genuinely under-specified input with a real human, and
record (a) how many rounds occurred, (b) whether any round contained a question whose answer changed a
question in the same round (a frontier violation), and (c) whether any fact question was put to the
human. Boundary: this measures whether the scheduling rule is followable and violable-detectably on
one input; it does not measure decision quality, and the model-sensitivity the source reports is
carried forward as a named uncertainty.

---

### MG-10 · Module-boundary vocabulary: interface facts, the deletion test, testability rules, rejected framings

**1) Mechanism, trigger, anchors, read status**

| | |
| --- | --- |
| Mechanism | A fixed vocabulary for the *technical* shape of an abstraction — module, interface, implementation, depth, seam, adapter, leverage, locality — with explicit **rejected substitutes and rejected framings**, plus three operational tests: the **deletion test**; **depth is a property of the interface, not the implementation**; and **the interface is the test surface**. Plus three interface-design rules for testability |
| Trigger | A module's shape, an interface, or an extraction boundary is the thing being decided — and, for the A/B/C interface, when a *contract* statement needs to say what callers must know |
| Provisional locus | D (the shape) with a **B/C interface**: "interface facts" are contract surface, and the vocabulary collides with C's "boundary" |

Anchors: `skills/engineering/codebase-design/SKILL.md` §Glossary L10–28 (term-by-term, each with
`_Avoid_`), §Deep vs shallow L30–58 (the two ASCII diagrams + three interface-shrinking questions),
§Principles L60–65, §Designing for testability L67–95 (rule 1 L69–80, rule 2 L82–91, rule 3 L95),
§Relationships L97–103, §Rejected framings L105–109; `DEEPENING.md` §Dependency categories L5–25,
§Seam discipline L27–31, §Testing strategy L32–37; `DESIGN-IT-TWICE.md` §Process;
`docs/engineering/codebase-design.md` §The vocabulary L23–38, §The four principles L39–47,
§Common questions L48–77; `skills/in-progress/setup-ts-deep-modules/SKILL.md` +
`dependency-cruiser.config.cjs`; `skills/productivity/wait-what/SKILL.md` +
`docs/productivity/wait-what.md` (the repair action when a shared term fails in use). Read: full.

**2) Operation, conditions of validity, failure modes, counterexamples**

- *Operation — the deletion test.* "Imagine deleting the module. If complexity vanishes, it was a
  pass-through. If complexity reappears across N callers, it was earning its keep." One imagined
  action, one binary read. The companion guard is *depth is not a size ratio*: the source explicitly
  rejects Ousterhout's implementation-lines-to-interface-lines definition because "That metric rewards
  padding the implementation", and substitutes depth-as-leverage.
- *Operation — the interface is the test surface.* "Callers and tests cross the same seam. If you want
  to test *past* the interface, the module is probably the wrong shape." This is the design-side
  counterpart of MG-3's implementation-coupling tell and MG-4's seam agreement: all three are the same
  commitment seen from three loci.
- *Operation — the three testability rules.* "Accept dependencies, don't create them"; "Return results,
  don't produce side effects" (with the `calculateDiscount(cart): Discount` /
  `applyDiscount(cart): void` pair); "Small surface area. Fewer methods = fewer tests needed. Fewer
  params = simpler test setup."
- *Operation — one adapter means a hypothetical seam,* two mean a real one. (Already in the product;
  see below.)
- *Conditions of validity.* A module-shaped unit with a caller boundary. The source is explicit that
  depth is not a required size ratio and that vocabulary does not assign ownership — a discipline
  against over-application.
- *Failure mode (documented, valuable as evidence).* Treated as a process rather than a reference, the
  skin burned a very large amount of context "redesigning things I never asked about", reaching for
  the most action-shaped content (the parallel sub-agents) and running a long way before asking
  anything. The stated workaround is to name a driver skill and let the vocabulary sit underneath.
  **This evidence validates a product design decision already taken** (see §4) and should be recorded
  as such rather than absorbed as a new rule.
- *Rejected framings, with reasons (the operationally load-bearing part).* "Depth as ratio of
  implementation-lines to interface-lines" → rewards padding. "'Interface' as the TypeScript
  `interface` keyword or a class's public methods" → too narrow; interface means *every fact a caller
  must know*. "'Boundary'" → **"overloaded with DDD's bounded context. Say seam or interface."** That
  last rejection is a **C-locus collision**, not a style preference, and the product has the same
  collision in different words.
- *Second-order failure mode worth keeping.* The source records that this vocabulary, offered as a
  skill, can be reached for autonomously and mis-scoped; it also records that the *enforcement* half is
  a separate question, answered by an in-progress skill that lays down a lint rule. The product's own
  structure (methods bound by a Charter) removes the first hazard; the second is the reason
  `dependency-cruiser.config.cjs` is screened here rather than dismissed as a config file.

**3) A–F loci and professional concern; Profile and call timing**

- **D** owns the module shape. **B** has a real interface here because "everything a caller must know"
  is a contract statement (ordering, error modes, invariants, performance characteristics) — the
  product's `methods/cross-module-design.md` §Method 2 already says exactly this. **C** has an interface
  because of the boundary-vs-seam vocabulary collision.
- Professional concern: *Maintainability* and *Testability*; *Performance* enters through the
  "performance characteristics are part of the interface" clause.
- Profile: `profiles/technical-planning.md` (D) primary; `profiles/behavior-domain.md` (C) for the
  vocabulary collision. Call timing: when a shape or extraction boundary is being decided — bound by
  the Charter, never fired on its own.

**4) Current product: exact text, what is covered, the specific gap, why**

Covered — substantially, and it should be stated as such. `methods/cross-module-design.md` §Method 2 and
§The terms paragraph already own the core:
> "2. Identify the interface in its full technical sense: the facts a caller must know, including
> inputs, outputs, ordering, error behavior, invariants and relevant performance characteristics."
> "The terms `module`, `interface`, `seam` and `depth` describe technical design. Depth describes how
> much useful behavior callers obtain without needing to know the implementation; it is leverage from a
> compact interface, not a required size ratio. These terms do not assign B/C ownership…"

and `guide-mock-adapter-choice.md` §Rules 5 owns the two-adapters rule and "the interface is the test
surface" verbatim, and §Rules 1 owns the four dependency categories.

Gaps — three, and they are narrow because the coverage is genuinely good:
1. **The deletion test is absent.** The product's *guard* against over-applying depth exists
   ("Do not force modules to merge for depth, prescribe each helper, or choose a design solely from
   file count" — §Limits), but the positive decision procedure that makes the guard usable is not
   there. A planner told "don't merge modules for depth" with no test has been told what to avoid, not
   how to decide. This is the single clearest content gap in the group.
2. **"Return results, don't produce side effects" is absent.** `guide-mock-adapter-choice.md` §Rules 4
   carries "Inject external dependencies rather than constructing them" (rule 1 of three) and nothing
   else from the testability set. The side-effect rule and "small surface area" are missing; the
   side-effect one is the operationally important one, because a side-effecting interface is what makes
   an eval have to reach past the surface.
3. **The `boundary` collision is unnamed.** The product uses "coordination surface" / "implementation
   interior" for the responsibility split and `seam` for the technical substitutable point, so it is
   already safe. But the *reason* — that "boundary" is overloaded with a domain-bounded-context sense,
   i.e. it collides with **C's** vocabulary — appears nowhere. Since the product is bilingual and
   `profiles/behavior-domain.md` explicitly owns "上下文边界" for C, a reader can reasonably reuse
   "boundary/边界" for a seam. One clause removes a real cross-locus ambiguity.
4. **`DESIGN-IT-TWICE`: review the prior deferral on its merits.** The old round deferred it and its
   3+ parallel-agent count (`methods/README.md` §Deferred alternatives; `METHOD-CANDIDATES.md` L64
   "不吸收 DESIGN-IT-TWICE 的 3+ 并行子代理数量：运行面绑定；有实质方案分歧时可保留"两案对比
   depth/locality/seam"纪律，但不得变成产品要求"). Reading the original: the count *is* a runtime
   claim and should stay excluded; but the mechanism beneath it is **not** a count. It is: *frame the
   constraints first and show them; give each alternative a genuinely different design constraint
   rather than three variants of one; then compare on depth, locality and seam placement; then give one
   opinionated recommendation, including a hybrid.* The source also states why one design is not
   enough ("your first idea is unlikely to be the best"). The product currently has **no** comparison
   discipline: `profiles/technical-planning.md` §关键问题 asks "有没有多个实质不同的方案？取舍依据是
   什么" and §按需方法入口 lists "方案比较方法：存在实质方案分歧时使用" — with no body. So this is a
   *narrowed re-entry* of a previously deferred item, with the count explicitly dropped, not a
   resurrection of it. Flagged as such for the gate.

Why worth absorbing: gap 1 and gap 2 are small, cheap, and close a hole the product's own Limit text
exposes; gap 3 is a one-clause C-safety fix; gap 4 is the only place in this package where a prior
deferral deserves re-examination on the original text rather than on the old label.

**5) Retain / change / delete; carrier; coupling; real-SDK dependency**

- **Retain** the deletion test; the interface-is-the-test-surface rule (already present — do not
  duplicate); the three testability rules with the side-effect pair; depth-as-leverage with the
  rejected ratio **and its reason**; the three rejected framings with reasons; the dependency-category
  list (already present — do not duplicate).
- **Change (for DESIGN-IT-TWICE)** the parts that are runtime claims: drop the 3+ count and the
  parallel-agent mechanism; keep frame-then-show, the different-constraint-per-alternative rule, and
  compare-on-depth/locality/seam with an opinionated synthesis. Add the product's own constraints: the
  alternatives are compared *inside* the delegated space, and the method grants no authority to change
  an accepted commitment (`methods/cross-module-design.md` §Method 6 already owns "A valid authority
  may accept a breaking change; this method does not override that authority").
- **Delete** the "call the Skill tool with X" invocation coupling (present in `tdd/SKILL.md` L26 and
  throughout the family) and any harness-specific sub-agent naming.
- Carrier: add the deletion test + side-effect rule to `guide-mock-adapter-choice.md` (it already
  carries the sibling rules, so this is an extension, not a new file) **or** to
  `methods/cross-module-design.md` §Method 2–4. The vocabulary clause belongs in
  `cross-module-design.md`'s existing terms paragraph. A design-comparison method, if accepted, is a
  method body in `methods/`.
- Real SDK/runtime dependency: **only** for the design-comparison half, and only if the product wanted
  parallel alternatives — which this package recommends **not** carrying. With the count dropped,
  dependency: none.

**6) Draft text and verification plan (not executed)**

Draft (candidate additions):

> **Does this abstraction earn its place?** Imagine deleting it. If the difficulty it holds disappears,
> it was passing through; if the difficulty reappears at every caller, it was carrying its weight.
> Judge that, not the ratio of implementation lines to interface lines — that ratio rewards padding the
> implementation, which is the opposite of the point.
> **Shape the interface to be observed.** Take dependencies in rather than constructing them; return
> results rather than writing them into something the caller already holds; keep the surface small.
> These are not style preferences: a surface that must be reached past cannot be evaluated without
> reaching past it.
> **Words.** Use *seam* for the place where behaviour can be substituted, and *interface* for
> everything a caller must know. Avoid *boundary* for either: it already means a bounded area of the
> domain here, and the collision is what makes a design conversation and a domain conversation look
> like they agree when they do not.

Verification plan: take one existing extraction in the package's fixtures, apply the deletion test, and
record whether the answer agrees with the design decision already taken; then check whether any current
sentence in the product uses "boundary/边界" for a seam. Boundary: the first is one retrospective
judgment, not a validated test; the second is a mechanical check of the product text, not of the
mechanism.

---

### MG-11 · Per-repo configuration read at run time instead of hard-coded

**1) Mechanism, trigger, anchors, read status**

| | |
| --- | --- |
| Mechanism | Keep the method bodies identical everywhere and put the *local* facts — where work is tracked, what the label strings are called, where domain documentation lives — in a per-repo configuration that methods **read at run time**. The stated consequence: "The tracker is a setup answer, not a skill property", so no method file needs editing to point it somewhere else |
| Trigger | A method needs a fact that differs per repository, and the temptation is to hard-code it or to fork the method |
| Provisional locus | A (what the task is and where its inputs live) with a D/C interface for the vocabularies it configures |

Anchors: `skills/engineering/setup-matt-pocock-skills/SKILL.md` (whole: explore → present → confirm →
write; the three sections; the file-selection rule) and its five seed templates
(`domain.md`, `issue-tracker-github.md`, `issue-tracker-gitlab.md`, `issue-tracker-local.md`,
`triage-labels.md`); `docs/engineering/setup-matt-pocock-skills.md` §The three decisions, §Common
questions, §It's working if; `scripts/link-skills.sh` (the write-back guard). Read: full.

**2) Operation, conditions of validity, failure modes, counterexamples**

- *Operation.* Explore the repo rather than asking cold; lead each decision with the recommended
  answer so it can be accepted in a word; **skip a section entirely when exploration already settled
  it**; show the draft before writing; record the result as committed prose that the other methods
  read. The tracker options are a real set with real escape hatches: first-class templates for the
  common cases, plus an explicit "other" path recorded as freeform prose — "It is the reason Jira,
  Linear, Azure DevOps and Beads all work".
- *The strongest single idea in this group, and it is an A/C mechanism:* **the configuration is a
  mapping, not a vocabulary.** `triage-labels.md` keeps the *canonical* role names ("The skills speak
  in terms of five canonical triage roles. This file maps those roles to the actual label strings used
  in this repo's issue tracker") and instructs "Edit the right-hand column to match whatever vocabulary
  you actually use." The local naming is thereby a *translation layer*, and the method body speaks one
  vocabulary while the repo keeps another. That is the same pattern as `_Avoid_` in MG-7, applied
  across vocabularies.
- *Conditions of validity.* A repo-scoped config surface that methods actually consult. The source
  states the alternative plainly and rejects it: duplicating tracker instructions into every method
  that touches work items.
- *Failure modes (all documented).*
  1. **Wrong file for the harness**: the file-selection rule is "edit `CLAUDE.md` if it exists, else
     `AGENTS.md`" — it checks *which file exists*, not *which harness runs*, so the configuration block
     can land somewhere the running agent never reads. Two workarounds recorded.
  2. **A mapping is not a creation step**: the config records label strings but does not create the
     labels, so the first run against a fresh tracker fails on a missing label. Repeatedly filed.
  3. **No user-level scope**: every repo carries its own copy; the request for a shared location is
     open and unimplemented.
  4. **Staleness**: the seed templates change between releases, so a config written by an older version
     can drift against the methods now reading it — with two defensible positions on whether re-running
     is required, reported as an acknowledged gap.
  5. **The honest objection the source keeps**: "having a skill to set up the other skill does not feel
     right to me: that means the LLM is configuring its own skills." Its stated mitigation — the output
     is inspectable, editable markdown, and day-to-day tweaks are ordinary edits rather than another
     run — is the reason the mechanism is acceptable at all.
- *Counterexample for scope discipline.* The source refuses to make this the home for preferences:
  "It configures three things: tracker, labels, doc layout… the standing answer is that skills stay
  opinionated: 'Config is death.'" That boundary is as load-bearing as the mechanism.

**3) A–F loci and professional concern; Profile and call timing**

- **A** in the Backbone's sense: the local facts determine what the task's inputs actually are
  (which tracker, which vocabulary, which document set), and getting them wrong produces wrong output
  rather than fuzzy output.
- Professional concern: *Integration/Delivery risk*; *Correctness* of anything that publishes.
- Profile: `profiles/driver.md` is the closest fit — the Backbone's Driver owns "识别适用触发与缺失／失效
  结论，找有委托的责任方，检查程序足够性" and the composition of instance inputs, which is what a per-repo
  input surface is. Call timing: at task assembly, before dependent judgments form.
- **Not** a Profile of its own, and **not** a responsibility node: the Backbone forbids new nodes
  ("不增加责任节点或常驻 Agent").

**4) Current product: exact text, what is covered, the specific gap, why**

Covered — partially, and the product already has the right *container*, which is why this is a
bounded question rather than a new mechanism. `professional-workflow/README.md` §Use names the task
input as a first-class assembly slot: "assemble the Profile, any authority context the Charter needs,
the filled Charter, its bound method files, and task-specific input in that order", and warns "The task
input must carry current facts and source references."
`methods/README.md` carries per-source pins in a table ("Fixed locator and pin | Used by"), and
`charters/template.md` has `Accepted inputs`, `Applicable methods` (with "Bind only methods needed for
this task"), and `Object scope`.

Gaps — three:
1. **No per-repo configuration surface.** The product's unit of binding is the *task* (Charter). There
   is no unit for "this repository does it this way", so a fact that is constant for a repo but varies
   across repos has no home except repetition into every Charter. The product's own
   `docs/RESPONSIBILITY-BACKBONE.md` and `professional-workflow/` are themselves repo-scoped; the gap
   is that the package has no stated way to carry a *local convention* without editing a method body.
   Note the honest caveat: the product has exactly one real consumer today (this repository), so the
   need is latent rather than demonstrated — the gate should weigh whether to add a surface for a
   second repo or leave it until a second repo exists.
2. **No vocabulary-mapping pattern.** The product mixes two vocabularies by language (Chinese Profiles,
   English methods) and by register (`coordination surface` / `implementation interior` vs
   `module`/`interface`/`seam`), and — per the old round and `methods/README.md` — needs accepted
   terms like `freshness`, `revision`, `snapshot` to stay with their owners. What is missing is the
   *pattern* the source uses: name the canonical vocabulary once, keep a per-context translation, and
   mark the translation as the editable half. `ADR-FORMAT.md`'s `_Avoid_` is the same pattern inside
   one context; `triage-labels.md` is the cross-context version. The product has neither as a rule.
3. **No stated re-sync trigger.** The source's staleness failure has a direct product analogue: the
   method bodies now carry accepted source digests (`methods/README.md` §Status and source trace,
   `charters/examples/*` each cite an M4 SHA-256), and the product has no rule for when a re-check is
   owed after a method body changes. The Backbone's own rule points the right way — reuse is valid
   "已有结论覆盖本次版本与差分即可复用" and F must "复用评价前确认本次版本/差分仍在其覆盖内" — but no
   artefact states the trigger. This is a real, current gap, not a hypothetical one.

Also worth recording, and it is a *validation* rather than a gap: `charters/examples/*` cite a
historical digest **and** say "current package bytes are recorded in `methods/README.md` §Status and
source trace and the night candidate manifest — a real task rebinds the current fixed object rather
than copying a digest here." That is the source's re-sync concern solved by construction, and it should
not be re-litigated.

**5) Retain / change / delete; carrier; coupling; real-SDK dependency**

- **Retain** the explore-then-confirm loop; the recommended-answer-led question; the skip-if-settled
  rule; the canonical-vocabulary-plus-translation pattern; the "config is a setup answer, not a method
  property" principle; and the "Config is death" boundary that keeps preferences out.
- **Change** the trigger direction: upstream is *run once per repo, by a human, before using the other
  methods*. In the product this must not become a mandatory pre-step for every task (it would be a new
  gate). The transferable form is: *where a fact is constant for the target but not universal, name it
  once and have the methods read it at run time.*
- **Delete** the harness-specific parts: the `CLAUDE.md`-vs-`AGENTS.md` selection rule is a defect
  finding, not a mechanism; do not carry it. Also drop the tracker templates as literal templates —
  they encode `gh`/`glab` command shapes, which are pure platform coupling (and one of them, the GitHub
  external-PR listing command, is documented as failing as written).
- Carrier: if adopted, it is a **Driver-facing clause** plus, at most, one short on-demand guide about
  naming a local convention. Explicitly **not** a registry, schema, or validator — the plan forbids
  "不建 registry/框架", and the source's own answer to "should there be a check mode" was no.
- Real SDK/runtime dependency: **yes, but only for the tracker-readback half** — publishing and reading
  work items requires a real tracker (CLI, API, or files). The *configuration pattern* has no such
  dependency. Any adoption must state which half it takes; the mapping/vocabulary half is
  runtime-free.

**6) Draft text and verification plan (not executed)**

Draft (candidate Driver-facing clause):

> Where a fact is fixed for the target but not everywhere — where work is tracked, what the local
> vocabulary is, where the written record lives — state it once, in a place the methods read, and keep
> the method bodies free of it. Keep one canonical vocabulary in the method and carry a readable
> translation to the local names, with the translation marked as the half that gets edited. Where a
> local fact has no home yet, put it in the task input rather than editing a method body for one
> target. Do not turn this into a preferences store: it holds facts the methods need, not opinions
> about how work should be done.
> When a method body changes or an accepted input ages, say which dependent conclusion is no longer
> covered by its evidence, and re-check only that.

Verification plan: (a) take one fact currently repeated across Charters and show it once, then check a
cold reader can still assemble a startup prompt; (b) enumerate the accepted inputs whose evidence is
bound to a digest and confirm each names what invalidates it. Boundary: (a) tests the surface's
sufficiency for assembly, not the mechanism's value; (b) is a documentation-completeness check, not a
claim about correctness.

---

## 3 · Cross-cutting observations and citation-precision checks

These are **A-class observations for the gate**, not adoption proposals.

**3.1 Existing source anchors in the accepted guides were checked and are accurate.**
`guide-mock-adapter-choice.md` cites, in its anchor table: `tdd/mocking.md` §When to Mock L3–14 and
§Designing for Mockability L16–59 (file is 59 lines — both correct); `codebase-design/SKILL.md`
§Principles L62–65 (L60 header, L61 blank, L64–65 the four bullets — correct); `DEEPENING.md`
§Dependency categories L5–25, §Seam discipline L27–31, §Testing strategy L32–37 (file is 37 lines; all
three exact).

**3.2 One citation range is narrower than the section name it carries.** The same table cites
`codebase-design/SKILL.md` "§Designing for testability L69–80". The section actually spans **L67–95**:
L69 is the lead-in, L71–80 is rule 1 (`Accept dependencies, don't create them`), L83–91 is rule 2
(`Return results, don't produce side effects`), and L95 is rule 3 (`Small surface area`). The
substantive claim the guide rests on ("inject external dependencies rather than constructing them" —
§Rules 4) *is* inside L69–80, so the guide's content is sound; the range under-covers the section title
it names. Relevant to MG-10 gap 2 for the same reason: the two rules left outside the cited range are
exactly the two the product does not carry. Mechanical, cheap to correct.

**3.3 Cross-wave check on `guide-redacted-evidence.md` (DEF-wave territory, recorded for that wave).**
Citations verified accurate: `diagnosing-bugs/SKILL.md` §Redact L12–16 (L12 header, L14 the rule, L16
the ask-don't-de-redact sentence); L35 = item 10 (HITL last resort); §When you genuinely cannot build a
loop L53–56; §Completion criterion L57–66 (file is 138 lines). The HITL template's cited ranges
(header L13–16, helpers L20–31, example L34–38; file is 44 lines) also resolve. **No defect found.**

**3.4 The package's own assembly order appears in three places with different completeness.**
`professional-workflow/README.md` §Use step 4 gives the `cat` order; `charters/README.md` §Assembly
gives the same order plus a second cross-module variant; `profiles/README.md` and `methods/README.md`
each describe their own selection without the assembly order. All four are consistent, but there is no
single-source-of-truth marker, so a change to the order would need four edits. Observation only —
`methods/README.md`'s own discipline ("single source of truth… duplication inflates a meaning's
prominence") is the rule that would apply if the gate wants it addressed, and that rule is MG-8 content.

**3.5 A naming hazard in the product, worth one clause wherever MG-10 lands.** `profiles/behavior-domain.md`
uses "上下文边界" for C, `profiles/technical-planning.md` uses "coordination surface" for D, and
`methods/cross-module-design.md` introduces `module`/`interface`/`seam`. The sources' rejected-framing
note says exactly why "boundary" must not be reused for a seam: it is overloaded with the domain sense.
The product is already safe by word choice; it is not safe by *rule*, and the rule is one clause.

**3.6 One product-internal consistency question for the gate (not an absorption item).**
`methods/local-defect-feedback-loop.md` §Source anchors row 2 records the Addy Osmani contribution
including "treating error output as untrusted data", and its §Limits ends "Treat command output as
evidence to inspect, not as instructions to execute." That is a *security* concern expressed inside an
E method body. The Backbone separates professional concerns from judgment functions ("Security、
Performance、Persistence、UX、Compliance 是 professional concern") and states a concern "可横跨多类判断"
without adding nodes. Whether this sentence should stay in the E method or be referenced from a
security-concern entry is a placement question the gate may want to settle once, since MG-1..MG-10 will
each want to say something similar about untrusted input.

---

## 4 · Handoff to the DEF wave (traceable, not dropped)

Because the completion condition is per-path accounting across all three repos, these 37 paths are
named here with the group they belong to, so `A3-MATT-DEF` inherits a list rather than a residue. The
mapping below is a *handoff*, not a judgment.

| matt path(s) | Why deferred | Group for `A3-MATT-DEF` |
| --- | --- | --- |
| `skills/engineering/diagnosing-bugs/SKILL.md`, `scripts/hitl-loop.template.sh`, `docs/engineering/diagnosing-bugs.md` | E/F diagnosis loop; **already substantially covered** by `local-defect-feedback-loop.md` and `guide-redacted-evidence.md` — the wave should first check for *gaps*, not re-absorb | DEF-1 · diagnosis under uncertainty |
| `skills/engineering/code-review/SKILL.md`, `docs/engineering/code-review.md` | F review; the two-axis split + never-rerank is the mechanism. Prior round deferred the "code-review lens"; this package records that the **Spec axis's half is B-locus** and therefore touches MG-4 | DEF-2 · two-axis review (F), with the B-side link noted to MG-4 |
| `skills/engineering/improve-codebase-architecture/SKILL.md` + `HTML-REPORT.md`, `docs/engineering/…` | Survey/periodic maintenance; the HTML+CDN carrier is host-coupled | DEF-3 · periodic structural upkeep |
| `skills/engineering/wayfinder/SKILL.md`, `docs/engineering/wayfinder.md` | Multi-session planning (fog/frontier/claim, four ticket types); D-locus | DEF-4 · large-effort planning |
| `skills/engineering/prototype/SKILL.md` + `LOGIC.md` + `UI.md`, `docs/…` | D/E throwaway-to-answer; the two branches and the primary-source capture rule | DEF-5 · prototype as evidence |
| `skills/engineering/research/SKILL.md`, `docs/engineering/research.md` | Delegated reading + citation artifact; background-agent coupling | DEF-6 · delegated investigation |
| `skills/engineering/wizard/SKILL.md` + `template.sh`, `docs/…` | Human-only procedure automation; the fixed library / authored stages split is a real E mechanism | DEF-7 · human-in-the-loop procedure |
| `skills/engineering/resolving-merge-conflicts/SKILL.md`, `docs/…` | E; intent-over-flag resolution + run-the-checks-before-commit | DEF-8 · merge/rebase resolution |
| `skills/productivity/handoff/SKILL.md`, `docs/…`, `skills/in-progress/claude-handoff/` | Context transfer; portability-not-compression; overlaps MG-8's boundary tree (the 5 options live in `PHASE-BOUNDARIES.md`, covered in MG-8) | DEF-9 · context transfer |
| `skills/productivity/teach/SKILL.md` + 4 `*-FORMAT.md`, `docs/…` | Stateful teaching workspace; storage-strength/desirable-difficulty; the components/assets reuse rule | DEF-10 · durable learning workspaces |
| `skills/in-progress/{writing-beats,writing-shape,writing-fragments}/` | Writing craft (grounding model, format arguments); in-progress bucket, no docs page | DEF-11 · long-form drafting |
| `skills/in-progress/{pr,retro,loop-me,setup-ts-deep-modules}/` | `setup-ts-deep-modules` is partially screened here (MG-10) as the enforcement answer; the rest are E/process | DEF-12 · misc in-progress |
| `skills/misc/{git-guardrails-claude-code,setup-pre-commit,migrate-to-shoehorn,scaffold-exercises}/` | Tooling/guardrail installation; `block-dangerous-git.sh` is a real mechanism (regex-over-command, bypassable) but is harness-specific | DEF-13 · guardrails and tooling |
| `scripts/link-skills.sh`, `list-skills.sh`, `sync-plugin-version.mjs` | Repo tooling; `link-skills.sh`'s write-back guard and `sync-plugin-version.mjs --check` are reusable patterns | DEF-14 · repo tooling patterns |
| `.agents/{invocation.md,writing-docs.md,install-block.md}`, `AGENTS.md`, `CLAUDE.md` | Screened here for the *mechanism* (MG-8); the governance/CI/promotion halves are non-method | DEF-15 · governance (non-method) |

Explicitly **not** carried forward as knowledge increments: `.changeset/*` (13), `skills/*/agents/openai.yaml`
(38 — mechanism extracted into MG-8), `README.md`/bucket READMEs (6), manifests/hygiene (4),
distribution/CI (3), governance ADRs (2).

## 5 · Verification status of this package

- **Nothing was executed.** No upstream script, template, hook, config or test was run; no product file
  was modified; no commit was made. Every "verification plan" in §2 is a **proposal**, and no mechanism
  in this package is asserted to work.
- **Every quoted source line was read at the pin in this session** and the line anchors in §2 were
  checked against the files (§0, §3.1–3.3).
- **Field reports are attributed, not verified.** The 26-ticket horizontal-slicing post-mortem, the
  runaway-context episode, the 200-question session, the missing-label failures and the other
  user-reported findings are reported **as the upstream docs pages report them**. They are used here as
  failure-mode evidence for the mechanism, never as independent measurements.
- **Old-round labels were not inherited.** Where this package re-opens a previously deferred item
  (§MG-10 gap 4), the proposal is derived from the original text with the runtime part explicitly
  dropped, and it says so.
- **Known uncertainty carried forward:** the no-op test's verdict is model-relative by the source's own
  statement (MG-8); the elicitation procedure's question quality is model-dependent (MG-9); and the
  per-repo configuration mechanism's need is *latent* in the product, which has one consumer today
  (MG-11).
