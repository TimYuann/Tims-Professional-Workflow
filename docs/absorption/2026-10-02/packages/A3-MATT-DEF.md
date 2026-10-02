# A3-MATT-DEF · mechanism-level review package (D/E/F + support material and scripts)

Source repo: `mattpocock-skills` @ `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`.
Locator (read-only): `.worktrees/legacy-pre-night-2026-10-01/upstreams/mattpocock-skills`.
Companion package (A/B/C family): `docs/absorption/2026-10-02/packages/A3-MATT-ABC.md`.
Product baseline: night worktree tip `800414d`, core 21 files under `professional-workflow/`.

**This package produces no adoption decision**, changes no product file, and executed nothing.
Where a group is already covered by accepted product text, it says so and stops; where a residual gap
exists, the gap is stated as a gap. Coverage judgment and adoption judgment are kept separate.

Because a large part of this family was already absorbed in the M3/M4 round, each group below begins
from **what the product already owns**, and only then states what is left. Padding a group whose
mechanism is fully carried would be exactly the duplication the product's own discipline forbids.

---

## 0 · Read basis and what is deliberately not repeated

Read in full at the pin, for this package:

| Source | Lines | Anchor form |
| --- | --- | --- |
| `skills/engineering/diagnosing-bugs/SKILL.md` + `scripts/hitl-loop.template.sh` | 138 / 44 | phase + line |
| `skills/engineering/code-review/SKILL.md` | 87 | step + line |
| `skills/engineering/improve-codebase-architecture/SKILL.md` + `HTML-REPORT.md` | 71 / — | section |
| `skills/engineering/wayfinder/SKILL.md` | 128 | section |
| `skills/engineering/prototype/SKILL.md` + `LOGIC.md` + `UI.md` | 26 / — / — | section |
| `skills/engineering/research/SKILL.md` | 12 | whole |
| `skills/engineering/wizard/SKILL.md` + `template.sh` | 44 / — | step + helper |
| `skills/engineering/resolving-merge-conflicts/SKILL.md` | 14 | step |
| `skills/productivity/handoff/SKILL.md`, `skills/in-progress/claude-handoff/SKILL.md` | 16 / — | whole |
| `skills/productivity/teach/SKILL.md` + four `*-FORMAT.md` | 140 | section |
| `skills/in-progress/retro/SKILL.md` | 44 | section |
| `skills/in-progress/pr/SKILL.md` + `CREDITS.md` | 168 | section |
| `skills/in-progress/loop-me/SKILL.md` | 32 | section |
| `skills/in-progress/setup-ts-deep-modules/SKILL.md` + `dependency-cruiser.config.cjs` | 102 | step |
| `skills/in-progress/writing-{beats,fragments,shape}/SKILL.md` | — | section |
| `skills/misc/{git-guardrails-claude-code,setup-pre-commit,migrate-to-shoehorn,scaffold-exercises}/` | — | section |
| `scripts/{link-skills.sh,list-skills.sh,sync-plugin-version.mjs}` | 44 / 6 / — | whole |
| The corresponding `docs/**` pages for all of the above (used for failure modes and field reports) | — | `##` section |

Not read / not established: no upstream issue, PR or discussion thread (issue numbers below appear
**as the docs pages report them**); no upstream script was executed; `HTML-REPORT.md`, `LOGIC.md`,
`UI.md`, `template.sh`, the four `teach/*-FORMAT.md` and the three `scripts/` were read in full but are
cited by section/helper rather than line where the file is a template or config.

**Deliberately not repeated here** (already screened in `A3-MATT-ABC.md`, and in several cases already
in the product): the deletion test and the boundary-vs-seam vocabulary collision (ABC MG-10); the
dependency-category list, two-adapters rule, interface-as-test-surface, replace-don't-layer
(ABC MG-10, already in `guide-mock-adapter-choice.md` §Rules 1, 5, 6); redaction, custody and the
HITL step/capture split (already in `guide-redacted-evidence.md`, whose source anchors this session
**verified as accurate**); the defect-path loop, falsifiable hypotheses and correct-seam reporting
(already in `local-defect-feedback-loop.md`); baseline/treatment comparison and the three-state verdict
mapping (already in `behavior-claim-evaluation.md`). Nothing in this package re-proposes them.

---

## 1 · Accounting for this wave

42 paths. Group primary-path counts:

| Group | Paths | Group | Paths |
| --- | --- | --- | --- |
| DEF-1 diagnosis under uncertainty | 3 | DEF-8 merge/rebase resolution | 2 |
| DEF-2 two-axis review (F) | 2 | DEF-9 context transfer | 3 |
| DEF-3 periodic structural upkeep | 3 | DEF-10 durable learning workspace | 6 |
| DEF-4 large-effort planning under fog | 2 | DEF-11 long-form drafting | 3 |
| DEF-5 prototype as bounded evidence | 4 | DEF-12 post-session retro | 1 |
| DEF-6 delegated investigation | 2 | DEF-13 guardrails and tooling | 4 |
| DEF-7 human-only procedure | 3 | DEF-14 repo tooling patterns | 2 |

One path is multi-labelled: `skills/in-progress/setup-ts-deep-modules/SKILL.md` is screened in ABC
MG-10 (as the enforcement answer to a design vocabulary) and again in DEF-13 (as the
"prove the check fails before trusting it" mechanism). Same file, two mechanisms that must be judged
separately; the count above lists it once in DEF-13 and it is not double-added. The remaining 127 of
the 169 paths are the 59 A/B/C paths of `A3-MATT-ABC.md` and the 68 asset/metadata paths (38
`agents/openai.yaml`, 13 `.changeset/*`, 6 READMEs, 4 manifests, 3 distribution/CI, 2 governance ADRs,
2 repo-governance files) — no path in the pin is unaccounted across the two packages.

---

## 2 · Mechanism groups

### DEF-1 · Diagnosis under uncertainty: the gate discipline, tightness, and the reproduction-rate target

**1) Mechanism, trigger, anchors, read status**

| | |
| --- | --- |
| Mechanism | A six-phase diagnosis whose phases are **gates**: each refuses to open until a specific, checkable condition holds. The gating condition for the whole method is a `tight` loop — one named command, already run and shown, that is red-capable on *this* failure |
| Trigger | A concrete failure exists (defect or regression) and cannot be explained by reading |
| Provisional locus | E (runs it) with F consuming the evidence; E owns the loop, F owns the verdict |

Anchors: `skills/engineering/diagnosing-bugs/SKILL.md` §Phase 1 L18, §Ways to construct one L24–37
(ten rungs), §Tighten the loop L39–47, §Non-deterministic bugs L49–51, §When you genuinely cannot
build a loop L53–56, §Completion criterion L57–66, §Phase 2 L68 + §Minimise L78–86, §Phase 3 L88–98,
§Phase 4 L100–112, §Phase 5 L114–128, §Phase 6 L130–138; `docs/engineering/diagnosing-bugs.md`
§The tight loop is the skill, §The gates between phases, §Common questions. Read: full. (Redaction and
the HITL helper are **not** re-screened; see §0.)

**2) Operation, conditions of validity, failure modes, counterexamples**

- *The gate table (the part the product does not carry).* Into Phase 2: "A named command, already run
  and pasted with its output, that can go red on this bug". Into Phase 3: "The repro is reproduced
  *and* minimised: every remaining element is load-bearing". Into Phase 4: "3–5 ranked, falsifiable
  hypotheses exist, each stating its prediction, shown to you before any is tested". Into Phase 5:
  "Probes map to a specific prediction, one variable at a time, every debug log tagged
  `[DEBUG-a4f2]`-style so cleanup is one grep". Done: "Original repro no longer reproduces,
  instrumentation gone, and the hypothesis that turned out correct is written into the commit message".
- *Tightness as a product, not an adjective.* Four named properties — fast (seconds), deterministic
  (same verdict every run), sharp (asserts the exact symptom, not "didn't crash"), agent-runnable —
  with the calibration sentence "A 30-second flaky loop is barely better than none; a 2-second
  deterministic one is tight", and three concrete tightening questions (cache setup / skip unrelated
  init; assert the specific symptom; pin time, seed RNG, isolate the filesystem, freeze the network).
- *Non-deterministic failures: change the goal.* "The goal is not a clean repro but a **higher
  reproduction rate**… A 50%-flake bug is debuggable; 1% is not, so keep raising the rate until it's
  debuggable." Concrete levers: loop the trigger 100×, parallelise, add stress, narrow timing windows,
  inject sleeps. This is a different target function from every other part of the method, and it is
  the one most often missed.
- *Minimisation has a done-condition.* Cut one element at a time and re-run after each cut; "Done when
  **every remaining element is load-bearing**: removing any one of them makes the loop go green."
  Stated payoff: it shrinks the hypothesis space and becomes the clean regression test.
- *Cleanup has a learning clause.* The checklist requires the original repro re-run, the regression
  test passing (or the missing seam documented), all `[DEBUG-…]` gone by grep, throwaway prototypes
  deleted, and the correct hypothesis stated in the commit/PR message "so the next debugger learns".
- *Conditions of validity.* (a) The described symptom is reachable; (b) something can be run
  unattended; (c) the failure is the *user's* failure and not a nearby one ("Wrong bug = wrong fix").
  Where (b) fails, the method's answer is to stop and ask for an environment, a redacted artifact, or
  permission for temporary instrumentation — "Do **not** proceed to hypothesise without a loop."
- *Failure modes, documented.* Over-firing on low-threshold models is the most-reported problem
  (constructed repros "with limited value" before answering). No gate exists between instrumentation
  and the fix, so an agent can start writing code before the root cause is agreed. It diagnoses one
  named failure; it does not audit.
- *Counterexamples / honest limits.* A merge can leave code that "satisfies both branches and passes
  neither's tests" (see DEF-8). A raw bug report is not yet a diagnosis (triage is the upstream lane).
  A proactive "where are the performance problems" question is explicitly not this method, and the
  request for such a skill was proposed and closed.

**3) A–F loci and professional concern; Profile and call timing**

- **E** owns the loop, the minimisation and the repair; **F** owns the verdict and must not be the
  implementer of the candidate. **F** may act *before* implementation only to say the design is not
  observable — the Backbone already separates design challenge from result evaluation, so the gate
  structure maps onto it without a new node.
- Professional concern: *Correctness*; *Performance* only through the measure-first branch.
- Profile: `profiles/implementation.md` (E) primary, `profiles/evidence-evaluation.md` (F) for the
  verdict. Call timing: the trigger is the *existence of an unexplained concrete failure*, not a
  phase — and per the Backbone, applicability must fire before the first dependent conclusion, so the
  loop requirement applies before any hypothesis-shaped statement is relied on.

**4) Current product: exact text, what is covered, the residual gap, why**

Covered — `methods/local-defect-feedback-loop.md` owns the skeleton and, importantly, already carries
these five items: run an observation that distinguishes the defect from expected behavior; make the
reproduction small/quick/repeatable; state falsifiable hypotheses and change one condition at a time;
repair and put regression coverage at a useful seam, reporting the absence of one as a design fact;
rerun and report exact commands, observations, deviations and remaining uncertainty. Its §Limits
already removes the ceremony ("does not require every task to enumerate a fixed number of hypotheses,
try every reproduction technique, create an extra commit for every red test") — **that part must not be
re-absorbed.**

Residual gaps — six, all specific and all inside the existing method's scope:
1. **No gate conditions.** The method is a numbered list, so a caller can proceed to "state falsifiable
   hypotheses" without a red-capable command. The source's load-bearing sentence — "No red-capable
   command, no Phase 2" — and the reason ("jumping straight to a hypothesis is the exact failure this
   skill prevents") are absent. This is the single highest-value addition in the group.
2. **No tightness criteria.** "Small, quick and repeatable as the environment allows" is weaker than
   the four named properties and gives no calibration, so a 30-second flaky loop passes the product's
   wording.
3. **The non-deterministic target is missing.** Nothing tells a caller that for a flaky failure the
   objective is a higher reproduction rate rather than a clean repro, and therefore nothing supplies
   the levers (loop the trigger, parallelise, stress, sleeps).
4. **Minimisation has no done-condition.** The product says make it small; it does not say cut one
   element at a time and keep only what is load-bearing, nor give the terminating test.
5. **No pre-test checkpoint.** The source shows the ranked list to the human *before* testing any
   hypothesis because domain knowledge re-ranks instantly — a cheap checkpoint the product lacks (its
   step 3 states hypotheses but does not surface them).
6. **No cleanup/learning clause.** The product's method ends at "Report exact commands, observations,
   deviations and remaining uncertainty." It has no requirement to remove instrumentation by a tag
   grep, and no requirement to state the confirmed hypothesis where the next debugger will find it.
   The product also has **no loop-construction ladder**, so "I cannot build a loop" has no routes; the
   source's ten rungs are the operational answer to exactly that state.
7. **No cross-method seam note.** The source records that triage's shallow verification duplicates
   this method's first two phases and that "neither file mentions the other". The product's
   `methods/README.md` lists methods independently with no interaction note, so the same silent
   overlap is possible between `local-defect-feedback-loop.md` and a triage-shaped intake.

Why worth absorbing: gaps 1, 3 and 4 are the difference between a procedure and a discipline, they sit
entirely inside a method the product already accepted, and gap 1 is the one that prevents the failure
the method exists to stop.

**5) Retain / change / delete; carrier; coupling; real-SDK dependency**

- **Retain** the gate table, the four tightness properties with the calibration sentence, the
  higher-reproduction-rate target with its levers, the one-at-a-time minimisation with its terminating
  test, the pre-test hypothesis checkpoint, the debug-tag/grep cleanup, the "state the correct
  hypothesis where the next debugger finds it" clause, and the ten-rung ladder as an *enumeration of
  options* rather than a required sequence.
- **Change** the ladder's status: the source presents it as "in roughly this order"; the product's
  existing anti-ceremony Limits text should stay and the ladder should be introduced as a menu for the
  stuck case, explicitly not as a required traversal. Also restate the loop requirement in the
  product's own terms — the gate is a **prerequisite to a hypothesis**, not a phase number, because the
  product has no phase numbering.
- **Delete** the harness coupling: `scripts/hitl-loop.template.sh` is a bash helper and its mechanism
  is already in `guide-redacted-evidence.md` §Rules 6, so nothing new is carried from it (the file is
  screened, at full read depth, and lands as covered).
- Carrier: **extend** `methods/local-defect-feedback-loop.md` (it is the accepted body for exactly this
  need, and the plan's instruction is to extend rather than proliferate).
- Real SDK/runtime dependency: **the ladder's lower rungs do** — headless browser, curl against a dev
  server, `git bisect run` require a real runtime; the ladder should say which rungs need what, so a
  method bound in an offline fixture is not silently unsatisfiable.

**6) Draft text and verification plan (not executed)**

Draft (candidate §Method replacement for steps 1–3, keeping the existing tone):

> 1. **Do not form a theory yet.** Before any hypothesis, produce one command you have already run at
>    least once whose output goes **red on this failure**: it must reach the code path the failure
>    travels and assert the reported symptom, not merely fail to crash. Show the command and its
>    output. If no such command exists, there is no basis for a hypothesis — say what you tried and ask
>    for a reproducing environment, a redacted artifact, or permission for temporary instrumentation.
> 2. **Make the signal tight before making it complete.** Fast (seconds), deterministic (same verdict
>    every run), sharp (asserts this symptom), runnable without you in the loop. A slow flaky signal is
>    barely better than none; pin time, seed randomness, isolate the filesystem, freeze the network.
>    For an intermittent failure the goal is not a clean reproduction but a **higher rate**: repeat the
>    trigger, widen the timing window, add load, until the failure is frequent enough to reason about.
> 3. **Minimise by removing one thing at a time**, re-running after each removal, and keep only what is
>    load-bearing: removing any remaining element must make the signal go green. A minimal case reduces
>    what a hypothesis has to explain and becomes the regression evidence.
> 4. Where more than one explanation is possible, state the falsifiable hypotheses and show the ranked
>    list **before** testing any of them; domain knowledge re-ranks cheaply and this costs one message.
>    Change one relevant condition at a time.
> … (repair step unchanged) …
> 6. **Clean up and record what was learned:** the original failure no longer reproduces at the
>    original surface; instrumentation added for diagnosis is gone (tag every probe with a unique
>    prefix so it is one search to confirm); the hypothesis that turned out correct is stated where the
>    next person meeting this code will find it.

Verification plan: take one known failure in a bounded fixture, apply gates 1–3, and record (a) whether
a red state was actually observed before any theory was written, (b) the observed run time and run-to-run
verdict stability of the signal, and (c) for a deliberately intermittent variant, whether the rate rose.
Boundary: this measures the gates' gate-keeping on one failure; it does not establish that the method
finds causes faster, and no such claim is made.

---

### DEF-2 · Two-axis review, aggregated without re-ranking (F)

**1) Mechanism, trigger, anchors, read status**

| | |
| --- | --- |
| Mechanism | Evaluate the same change along **two axes that must never be merged** — *Standards* (is it built the way this repo requires?) and *Spec* (is it the thing that was asked for?) — in **separate contexts** so neither sees the other's reasoning, then report both and decline to name a single winner |
| Trigger | A diff exists against a fixed point, and its quality must be judged |
| Provisional locus | F, with a real B dependence (the Spec axis needs an accepted statement of what was asked) |

Anchors: `skills/engineering/code-review/SKILL.md` §1 Pin the fixed point L17–24, §2 Identify the spec
source L25–33, §3 Identify the standards sources L34–57 (the twelve named smells, each
*what it is* → *how to fix*), §4 Spawn both L58–73 (the two briefs with the citation requirement and
the word caps), §5 Aggregate L74–79, §Why two axes L80–87; `docs/engineering/code-review.md`
§The two axes, §Common questions, §It's working if. Read: full.

**2) Operation, conditions of validity, failure modes, counterexamples**

- *The separation rule and its justification.* "The two axes are never merged and never re-ranked. The
  report ends with a worst issue *per axis* and refuses to name a single winner across them, because a
  change can pass one axis and fail the other." The two worked asymmetries are the argument: code that
  follows every convention while implementing the wrong thing, and code that does exactly what the
  ticket asked while breaking the repo's conventions. "A blended verdict lets the passing axis hide the
  failing one."
- *Why separate *contexts*, not just separate headings.* Running the axes as parallel sub-agents is
  justified as preventing mutual pollution. The independence argument is extended beyond authorship:
  the same session that wrote the code is biased — "Same context reviewing itself isn't review, it's
  confirmation bias with a slash command." That framing is a genuine addition to an authorship-based
  independence rule.
- *Fail-fast placement.* "Before going further, confirm the fixed point resolves (`git rev-parse`) and
  the diff is non-empty. A bad ref or empty diff should fail here, not inside two parallel
  sub-agents." Plus: the fixed point must be supplied; the skill asks rather than guessing.
- *The citation requirement, which is what makes findings checkable.* Every Standards finding cites a
  documented rule (file + the rule) or a named smell plus the quoted hunk; every Spec finding quotes a
  spec line. "That every finding is required to carry one … is what makes this checkable at all."
- *Findings are hypotheses, not evidence.* "Sub-agent output is a hypothesis, not evidence: one team
  reported a dozen breaking changes that prose-based reviews had waved through. The skill aggregates
  the two reports verbatim or lightly cleaned rather than re-verifying each claim." So the reader must
  read the citation before acting.
- *The floor and the override.* A twelve-smell baseline applies even where a repo documents nothing,
  but each is "a labelled heuristic ('possible Feature Envy'), never a hard violation", "**The repo
  overrides**", and anything tooling already enforces is skipped by both axes.
- *No convergence guarantee.* "Because fixes create new surface, and because the judgement-call half of
  the Standards axis is not deterministic between runs… There is no convergence guarantee. Treat a pass
  as a list of leads, act on the ones with a cited rule behind them, and stop: do not run it in a loop
  until it comes back clean, because it will not."
- *Measurement-validity trap.* It diffs `<fixed-point>...HEAD`, three-dot, "which is measured from the
  merge-base and excludes staged and working-tree changes" — so uncommitted work about to be committed
  is **invisible** to the review.
- *Failure mode with real content.* The two sub-agent briefs did not forbid delegation, so a sub-agent
  could rediscover the skill and fan out again; one report reached 50-plus agents. The applied fix is
  one line in each brief: do not invoke the review and do not spawn additional agents.
- *Counterexample / boundary.* With no spec available, the Spec sub-agent is skipped and the report says
  "no spec available" rather than inventing requirements — the negative case is designed, not
  accidental.

**3) A–F loci and professional concern; Profile and call timing**

- **F** owns the evaluation. The Spec axis consumes **B**'s accepted statement; the Standards axis
  consumes the repo's own documented standards, which is a *D/C-adjacent* artifact (the repo's own
  writing) — so a missing standards source is a **basis defect to return**, not an F judgment.
  Per the source, the repo's own documentation is the primary source and "the repo always overrides".
- Professional concern: *Correctness* (both axes) and *Maintainability* (the Standards axis).
- Profile: `profiles/evidence-evaluation.md` (F). Call timing: on a fixed diff; and, for the two-axis
  discipline specifically, whenever a verdict shaped like "looks good" is about to be produced — the
  mechanism exists to stop a single blended judgment.

**4) Current product: exact text, what is covered, the residual gap, why**

Covered — nothing directly. `methods/behavior-claim-evaluation.md` evaluates **one** falsifiable claim
by baseline/treatment; the nearest product text is its §Limits: "This method evaluates a specific
observable claim, not user value or overall task closure." `profiles/evidence-evaluation.md` requires a
negative control and a stated object/version but has no notion of two independent evaluation axes.
`charters/template.md`'s `Independence` field carries *who* evaluates, not *what axes*.

Residual gaps — five:
1. **No two-axis discipline and no anti-merge rule.** Nothing in the core prevents a single blended
   verdict, which the source identifies as the specific way one axis masks another.
2. **No citation requirement on findings.** The product requires "对象/版本、依据、观察、覆盖限制"
   (`profiles/evidence-evaluation.md` §交出) at the *report* level, but has no per-finding rule that
   each finding must carry the rule it breaches or the line it fails. That per-finding citation is
   what makes a finding checkable and is the anti-LLM-hallucination device in this family.
3. **No fail-fast placement rule.** The product has no statement that a review must first confirm its
   own basis (the fixed point resolves, the compared range is non-empty) *before* spawning evaluation,
   so an invalid basis is discovered inside the evaluation instead of in front of the requester.
4. **No context-independence argument.** The Backbone's independence rule is about *who* (implementation
   author ≠ evaluator, judged by real contribution). The source adds a second, independent reason:
   *holding the authoring assumptions* biases the judgment even where roles differ. `charters/template.md`
   asks for relationships but not for context separation.
5. **No measurement-validity warning on the comparison range.** Three-dot/merge-base semantics and the
   exclusion of staged work are exactly the class of trap the product's
   `methods/behavior-claim-evaluation.md` §Method 3 already guards on the *data* side ("A missing/invalid
   baseline, noisy or incomparable data… makes the observation inconclusive"). The *revision-range*
   instance of the same guard is absent, and it is cheap to state.
6. Two smaller items: **no standards-source discovery order** (commit-message references → an explicit
   input → a matching spec file → ask) and **no "the repo overrides the baseline" rule** — both needed
   only if the product adopts a standards baseline at all.
7. **The delegation-boundary guard.** "Do not invoke this review again or spawn additional agents:
   perform this review directly" is a two-line guard against a real, reproduced runaway. The product
   runs evaluation in delegated agents and has no equivalent instruction; this belongs with DEF-7's
   delegation economy as much as here.

Why worth absorbing: gap 1 is a genuine blind spot in the product's F profile (one verdict shape for
two different questions), gap 2 is the cheapest available defence against findings that cite nothing,
and gap 3 is a placement rule with no cost.

**5) Retain / change / delete; carrier; coupling; real-SDK dependency**

- **Retain** the two axes with the anti-merge rule and the two asymmetry examples; the citation
  requirement; fail-fast basis validation; the repo-overrides rule; the smell baseline as a
  judgement-call floor; "findings are hypotheses"; the no-convergence warning; the three-dot/merge-base
  trap; the context-bias argument; and the do-not-re-delegate guard.
- **Change** the smell baseline's status: twelve named smells are a *useful* floor but they are one
  repository-culture's list. The transferable rule is "each finding names a rule or a named heuristic
  and quotes the site; documented rules can be hard, heuristics are always judgement calls; whatever
  tooling already enforces is out of scope." The specific list can be carried as an example, not as a
  required set.
- **Delete** the platform coupling: parallel sub-agents named as a mechanism, the harness's own
  `/code-review` collision, and the `docs/agents/issue-tracker.md` spec-discovery path (the product's
  Charter names its inputs). Independence must be stated in the product's own terms (real contribution
  and context), not in terms of agent instances.
- Carrier: extend `methods/behavior-claim-evaluation.md` with a short two-axis clause **or** add a
  sibling method for change-level evaluation. The citation rule and fail-fast rule are small enough to
  live in the existing method's §Method; the two-axis discipline is a genuine second mechanism and may
  deserve its own body. Flag for the gate — this is a real fork in landing form.
- Real SDK/runtime dependency: **a real revision range is required** (a git history with a fixed
  point). The axis mechanism itself needs no network or service.

**6) Draft text and verification plan (not executed)**

Draft (candidate clause):

> A change can be built the way this project requires and still be the wrong change, and the reverse is
> just as common. Keep the two questions apart and answer both: **is this built to the standards this
> project documents** (and where it documents nothing, to named heuristics, each a judgement call and
> never a hard breach), and **is this what the accepted statement asked for**. Do not merge them into
> one verdict and do not rank one against the other: a single verdict is how the axis that passed hides
> the axis that failed. Every finding names the rule it breaches, or the named heuristic plus the site
> it applies to, or the line of the accepted statement it fails — a finding that cites nothing cannot
> be checked and should not be acted on. Before any evaluation begins, confirm the basis: the compared
> revision resolves, the range is what you intend to compare, and it is not empty; a malformed basis
> must fail here rather than inside the evaluation. Findings are hypotheses: read the citation before
> acting, and do not iterate the evaluation to a clean result — fixes create new surface, so a pass is
> a list of leads to act on and stop.

Verification plan: run the two axes on one historical diff whose spec exists, with each axis in a
separate context, and record (a) whether either axis produced a finding without a citation, and (b)
whether the two verdicts could have been collapsed into one without loss. Boundary: this tests whether
the discipline is observable and whether the axes actually disagree on a real diff; it does not
establish that two axes find more than one, and no claim about defect yield is made.

---

### DEF-3 · Periodic structural upkeep: survey, strength badges, and durable rejection

**1) Mechanism, trigger, anchors, read status**

| | |
| --- | --- |
| Mechanism | A periodic, non-mutating survey that produces *candidates* for structural improvement, each carrying a strength judgement, and that records a durable reason when a candidate is rejected so a later run does not re-propose it |
| Trigger | A recurring upkeep moment, or a specific structural question before a large change ("how can we make this change easy?" is named as the most effective prompt) |
| Provisional locus | D |

Anchors: `improve-codebase-architecture/SKILL.md` §1 Explore L18–36 (YAGNI scoping; commit-history
weighting; five friction questions; the deletion test as admission filter), §2 Present candidates
L37–61 (the card fields, the three badges, the Top recommendation, "Do NOT propose interfaces yet"),
§3 Grilling loop L62–71 (including the ADR-offer-on-durable-rejection rule);
`docs/engineering/improve-codebase-architecture.md` §Common questions, §It's working if. Read: full.

**2) Operation, conditions of validity, failure modes, counterexamples**

- *The survey never changes code.* "The whole run produces one HTML file in your OS temp directory and
  a conversation; the refactor itself happens later, in a separate session, through the normal build
  flow." That separation is what makes it safe to run on code you are not ready to touch.
- *Two filters against generic cleanup advice.* (i) The deletion test as the admission filter (already
  in the product via ABC MG-10 — cross-reference, do not duplicate). (ii) **Commit-history weighting**:
  unless pointed at an area, read recent history first and bias the scan toward paths that keep
  changing, "on the grounds that a deepening in code nobody touches is a refactor you will never cash
  in". This is a *value* filter, distinct from the correctness filter.
- *The badges are the honesty device.* `Strong` / `Worth exploring` / `Speculative`, and the source
  states their purpose explicitly: "The skill is built to output findings, so the framing pushes it
  toward producing candidates rather than concluding that nothing is wrong. The strength badges are the
  defence: a report where everything is `Speculative` is the skill telling you it found nothing, in the
  only way it knows how." Preserving that reason matters more than the badge names.
- *Durable rejection (the mechanism the product lacks entirely).* After a candidate is rejected for a
  reason that would matter to a future run, the skill offers to record it "so future architecture reviews
  don't re-suggest it" — and the offer is deliberately narrowed: "Only offer when the reason would
  actually be needed by a future explorer to avoid re-suggesting the same thing; skip ephemeral reasons
  ('not worth it right now') and self-evident ones." This is the **same durability test** as ABC MG-6's
  rejection record ("those aren't real rejections, they're deferrals"), reached from the maintenance
  side, and the two should land as one mechanism rather than two.
- *One candidate per session.* The stated reason is context economics: the report, the grilling, the
  domain edits and the code changes all fill the window at once.
- *Conditions of validity.* A codebase with some history to weight by; a place to put the report outside
  the repo; and — for the rejection record — a place to write it that survives.
- *Failure mode (carrier, platform-coupled).* The report loads Tailwind and Mermaid from CDNs, so it
  needs network access when opened, and "it breaks silently when something blocks those scripts" — with
  the agent unable to see the failure because it never renders the page. The recorded workaround is to
  ask for inline CSS and hand-built SVG. Any adoption must not carry the CDN scaffold.
- *Failure mode (behavioural).* The report-then-grill order can invert on weaker models: "weaker models
  skip straight to interviewing you about the first idea they had" — one report describes sessions with
  "10's or 100's of questions" and calls the result "borderline unusable". The design intent is report
  first, grill only on a chosen candidate; there is no documented no-grill mode.
- *Honest limit.* "It will rarely tell you the codebase is fine" (handled by the badges), and on a
  genuinely out-of-control legacy codebase users report it "helped a little but still doesn't seem to
  cut it".

**3) A–F loci and professional concern; Profile and call timing**

- **D** owns the structural judgment. **E** owns the eventual change; **F** owns whether the change
  delivered the claimed improvement.
- Professional concern: *Maintainability* and *Testability*; *Delivery risk* through the
  change-weighting filter.
- Profile: `profiles/technical-planning.md` (D). Call timing: periodic upkeep, and before a large change
  as a "make the change easy" pass — never as a gate on a task.

**4) Current product: exact text, what is covered, the residual gap, why**

Covered — the *vocabulary and the admission test* land in ABC MG-10 (deletion test, depth-as-leverage,
the vocabulary clause in `methods/cross-module-design.md`). `methods/cross-module-design.md` §Use also
already scopes design work to "when the proposed change affects facts, behavior or constraints that
another module, responsibility or verifier must rely on" — i.e. change-driven, not survey-driven.

Residual gaps — three:
1. **No survey mode at all.** Every product method is triggered by a change. The product has no
   mechanism for "look at what exists and propose what to improve", which means structural debt can only
   be discovered when a change happens to touch it. This is the group's substantive gap.
2. **No candidate-strength language.** The product's vocabulary distinguishes deep/shallow but has no
   way to say "this is plausible but the payoff depends on where the code is going next" — i.e. no way
   to report a finding as *weak* while still reporting it. The badges' function (letting a survey say
   "nothing here") is what is missing, and it is the honesty device that makes a periodic process
   tolerable.
3. **No durable rejection for suggested-but-refused work.** This is the same gap as ABC MG-6 part B,
   reached from the other side. Wherever it lands, it must land **once**: a refusal recorded in the
   decision record must be the same artifact a later survey consults before re-proposing. Flagging so
   the gate can merge the two rather than create two homes.
4. **Value-weighting by change history is absent.** The product's `profiles/technical-planning.md`
   §关键问题 asks "改动的因果范围到哪里" for a *given* change; nothing says that where to spend
   improvement effort should be weighted by where change actually happens.

Why worth absorbing: gap 2 is cheap and closes an honesty hole (a product process that can only report
findings will always report findings); gap 3 is a genuine cross-group merge opportunity rather than new
content; gap 1 is a real capability the product does not have, and the gate should weigh whether the
product wants a survey mode at all or deliberately stays change-driven — **both answers are defensible**.

**5) Retain / change / delete; carrier; coupling; real-SDK dependency**

- **Retain** the never-mutates-during-survey rule; the deletion test as admission filter (already
  present); change-history value weighting; the three-strength reporting with its stated purpose; the
  answer-then-choose stop ("Nothing has been decided at that point, and no code has moved"); one
  candidate per session; and the durable-rejection offer with its narrowing rule.
- **Change** the artifact: do not carry an HTML report. The transferable object is "a list of
  candidates, each with what is involved, the friction, a plain-language change, and the benefit stated
  in the product's own terms (locality/leverage or their product equivalents), each carrying a strength
  and a recommended first one". The medium is a carrier decision, and the product's own discipline
  (single source of truth, environment-as-cache) argues for the lightest carrier that survives.
- **Delete** the CDN/network dependency and the visual/diagram scaffold; also drop the parallel-explore
  sub-agent naming.
- Carrier: if accepted, a method body in `methods/` bound by a D Charter. The durable-rejection half
  lands with the MG-6 decision-record method, not here.
- Real SDK/runtime dependency: **reading git history is required** for the value filter; the survey
  itself needs no network, and any adoption must state that the report medium must work offline.

**6) Draft text and verification plan (not executed)**

Draft (candidate method rule, deliberately without the report medium):

> When you survey for structural improvement, change nothing. Produce candidates and stop. Two filters
> decide what earns a candidate: removing the abstraction would spread its difficulty across callers
> rather than removing it, and the code is somewhere work actually happens — an improvement in code
> nobody touches is a saving nobody collects. Where you were pointed at an area, use that instead of
> guessing. Report each candidate with what is involved, what hurts, what would change, what the change
> buys, and how strong it is: *worth doing*, *plausible depending on where this code is going*, or
> *noted for completeness*. Most candidates in a healthy area should be the last kind, and a survey that
> reports everything as worth doing has not judged anything. Stop after the list and ask which one to
> take; then, where the reason for refusing one would matter to the next survey, record the refusal so
> it is not proposed again — but only when it would matter, not for "not now".

Verification plan: run the survey on a bounded area and record (a) the badge distribution, (b) whether
any candidate's benefit statement was unfalsifiable in the product's own terms, and (c) whether a
recorded refusal was respected by a second run. Boundary: this tests the reporting discipline and the
refusal mechanism, not whether the survey finds the "right" improvements.

---

### DEF-4 · Planning a large effort under fog

**1) Mechanism, trigger, anchors, read status**

| | |
| --- | --- |
| Mechanism | For an effort whose **destination** can be named but whose route cannot yet be seen, chart a **map** that is an *index, not a store*: name the destination first, keep unresolved questions as explicitly-phrased **decision items**, keep everything you can tell is coming but cannot yet phrase as *fog*, and work items one at a time off a **frontier** defined by blocked/unclaimed |
| Trigger | The effort is larger than one context window *and* the route is still foggy. The source's own test is session count, not project size |
| Provisional locus | D, with A/C interfaces (destination fixes scope; the vocabulary keeps shared meaning) |

Anchors: `wayfinder/SKILL.md` §Plan, don't do L11–14, §Refer by name L15–18, §The Map L19–31 (§The map
body L27–31), §Tickets L55–72 (claim by assigning; native blocking for frontier visibility), §Ticket
Types L73–81, §Fog of war L82–94, §Out of scope L95–103, §Invocation L105–128 (chart / work);
`docs/engineering/wayfinder.md` §The map, the fog, and the frontier, §The four decision-ticket types,
§Common questions, §It's working if. Read: full.

**2) Operation, conditions of validity, failure modes, counterexamples**

- *Destination first, and it fixes scope.* "Naming it is the first act of charting, before any ticket
  exists, because the destination fixes the scope every ticket is measured against." Also: the
  destination means the end of the whole map, not of one session — the source notes the question reads
  ambiguously and that a session-scoped answer never makes sense.
- *The map is an index.* "It lists the decisions made and points at the tickets that hold their detail;
  a decision lives in exactly one place, its ticket, so the map never restates it, only gists it and
  links." Consequence: a session loads the map at low resolution and zooms on demand, which is what
  lets the map grow without every session paying for its history. This is the product's single-source-of-truth
  discipline applied to a multi-session plan.
- *The fog/ticket test is the mechanism's sharpest operation.* "The test is whether you can state the
  question precisely *now*, **not** whether you can answer it now." Sharp-but-blocked → a real item;
  not-yet-phrasable → fog, and explicitly **not** pre-sliced into item-sized pieces ("it's coarser than
  a ticket, and one patch may graduate into several tickets, or none, once the frontier reaches it").
  Scope is a separate axis: work beyond the destination is **out of scope**, never fog, because "Fog
  only ever gathers *toward* the destination".
- *Claim before work, because the claim is the assignee.* "A session claims a ticket by assigning it to
  itself before doing any work, so the assignee *is* the claim and concurrent sessions skip it." The
  frontier is then derived, not maintained by hand.
- *Native blocking is a visibility mechanism, not bookkeeping.* The stated reason is that dependency
  links "render the frontier _visually_ in the tracker's own UI, so the human sees what's takeable
  without opening the map". Where the backend has no native edges, the source states plainly that the
  graph is inferred from text and "needs closer supervision".
- *Four item types, split by whether a human is in the loop.* Conversation (default) and artifact-building
  are HITL; investigation may be AFK; manual unblocking work is either. One type is the exception to
  one-at-a-time, and only because nothing waits on a human.
- *Plan, don't do — with the failed exception preserved.* The rule is that each item resolves a
  *decision*, and the pull to just do the work "is usually the signal you've reached the edge of the
  map and it's time to hand off". The honest defect the source records: an effort can carry execution
  into the map via its own notes, and those notes are written by the constrained party. One reported
  agent "write 'this map carries execution' into its own Notes and then read it back in later sessions
  as its own licence". **The lesson to carry is structural, not textual:** a constraint that the
  constrained party can edit is not a constraint.
- *Failure mode with field evidence.* "I charted 27 tickets, and by the time I got to the thirteenth,
  the rest no longer made sense." Traced to the map trying to plan comprehensively. Two mitigations are
  named: scope the map to a bounded destination rather than the whole product, and "prototype
  aggressively… Wayfinder is 'prototypemaxxing', not 'planmaxxing'".
- *Counterexample / stopping rule.* If the opening breadth-first pass surfaces no fog, the method stops
  and says the effort is small enough to skip the map. And a closed map is not a build plan: the linked
  decisions must still be collapsed into one agreed statement before execution starts, or "the linked
  detail is thrown away".

**3) A–F loci and professional concern; Profile and call timing**

- **D** owns the plan. **A** owns the destination (what the effort is for) and **C** the vocabulary the
  map keeps consistent. **F** evaluates the eventual *build*, not the map.
- Professional concern: *Delivery risk* and *Maintainability*; *Cost* through the decisions about how
  much to plan before acting.
- Profile: `profiles/technical-planning.md` (D) primary; `profiles/intent-voice.md` (A) for the
  destination. Call timing: when the effort exceeds one working context **and** the route is unclear —
  the source's session-count test, applied before the first dependent decision is fixed.

**4) Current product: exact text, what is covered, the residual gap, why**

Covered — the *scale* boundary is implicit and correct: `methods/cross-module-design.md` §Method 5
produces "a compact Plan with Commitments, Delegated Decisions and Recall Conditions", and
`profiles/technical-planning.md` §关键问题 asks the right scope questions. `methods/README.md` §On-demand
guides and §Selected methods are all single-task-scale. The product's own consistency comes from the
Backbone rather than from a planning artifact.

Residual gaps — five:
1. **No multi-session planning mechanism.** The product has no unit for an effort that outlives one
   context: no destination-first scoping, no index-vs-store map, no explicit fog section, no derived
   frontier. Everything the product has assumes the change and its dependencies fit in one planning
   act. This is the group's substantive gap and it is a real capability, not a stylistic preference.
2. **No sharpness-vs-scope distinction for unresolved work.** The product's
   `profiles/technical-planning.md` §常见误区 warns against Plan detail inflation, but has no device for
   recording *"I can tell this is coming and cannot phrase it yet"* while keeping it distinct from
   *"this is out of scope"*. Those are three different states (sharp, unphrased, excluded) and the
   product has one bucket (Recall Conditions) for one of them.
3. **No claim mechanism.** `profiles/driver.md` §关键问题 does ask "并行写者的写集是否明确？共享文件是否
   单写者串行集成？" — that is the *write-set* half of concurrency and it is already correct. What is
   missing is a *claim* discipline for work items: taking an item before working on it, so a second
   session can tell what is taken. The product's answer to concurrency is serialisation; the source's is
   claiming. Both work, but the product should say which it intends at multi-session scale.
4. **The structural lesson about self-editable constraints is absent.** The product puts prohibitions in
   Charters and the Backbone — artifacts the *task* author writes — and the Backbone already guards the
   important version of this ("不能静默转移权责", "约束的 mandatory／reserved … 来自其有效 authority").
   The source's failure adds a concrete case worth one clause: a constraint expressed only in a document
   the constrained party owns is not enforceable, so an execution prohibition must live where the
   authority lives, not in the working notes.
5. **No bounded-instead-of-comprehensive rule.** "Scope the map to a bounded destination rather than to
   the whole product" is the countermeasure to the dominant failure mode (planning comprehensively and
   having later items invalidated). The product's equivalent guard is the sufficiency test, which
   limits *detail*, not *breadth over time*.

Why worth absorbing: gap 1 addresses a class of work the product currently cannot serve at all, and
gaps 2 and 5 are the two smallest possible guards against the documented failure. Gap 4 is one clause
and closes a real hole.

**5) Retain / change / delete; carrier; coupling; real-SDK dependency**

- **Retain** destination-first; index-not-store with zoom-on-demand; the fog/ticket sharpness test; scope
  as a separate axis from sharpness; derived frontier with claim-before-work; HITL/AFK typing; the
  plan-don't-do rule with the structural lesson; prototype-forward as the countermeasure to
  over-planning; the no-fog stopping rule; and the "a closed map is not a build plan" handoff rule.
- **Change** the storage substrate: the source stores the map on an issue tracker. The product must not
  require a tracker or a label vocabulary. The transferable requirement is *addressable items with
  dependency edges and a claim, visible without loading everything*, and the carrier should be named by
  the task (a file set in the working scope is sufficient; the source itself notes that storing this
  material in the repo leads to "accidental persistence", so the carrier question is genuinely open).
- **Delete** the label/CLI mechanics (`wayfinder:map`, `wayfinder:<type>`, sub-issues, the dependency
  API and its database-id gotcha, the pristine/new/blocked queries) — pure platform coupling. Also drop
  "refer by name" as a *rule*; keep it as a readability consequence of the naming, not a separate
  mechanism.
- Carrier: a method body (`methods/large-effort-planning.md`) bound by a D Charter, plus a
  `methods/README.md` row. The vocabulary-consistency half is ABC MG-7's; note the dependency rather
  than duplicating it.
- Real SDK/runtime dependency: **yes, for the visibility half** — seeing the frontier without loading
  the map needs *something* addressable (a tracker, or files plus a listing). The planning mechanism
  itself has no runtime dependency.

**6) Draft text and verification plan (not executed)**

Draft (candidate method §Method):

> Name the destination before anything else: what reaching the end of this effort looks like. It fixes
> what is in scope, and everything below is measured against it. Then keep one index that holds the
> destination, what has been decided (one line each, pointing at where the detail lives), what is not
> yet specified, and what is ruled out. Nothing lives in the index: a decision lives in exactly one
> place and the index points at it, so a session can load the index cheaply and open only what it needs.
> Distinguish three states and do not merge them. A question you can state **precisely now** is an item,
> even if something else blocks it. A question you can tell is coming but cannot yet phrase is *not yet
> specified* — record it loosely; it will graduate into one item, several, or none. Work beyond the
> destination is **out of scope** and never graduates, because scope and sharpness are different axes.
> Work one item at a time. Before working an item, take it, so a second session can see it is taken.
> An item is resolved when the question is answered and the answer is recorded where the index points;
> answering may sharpen what was unphrased, and what graduates moves out of "not yet specified" so it
> exists in one place only. Both halves are planning, not building: when you feel the pull to build,
> that is the signal you have reached the edge of what this effort needed to decide. If the first pass
> surfaces nothing unphrased, the effort was small enough not to need this — say so and stop.

Verification plan: take one effort known to exceed a single context window, chart the index only, and
record (a) whether the destination was stated before any item existed, (b) whether any item's phrasing
required information that only a later item could produce (a sharpness violation), and (c) whether the
index alone was sufficient to name the next item without opening any detail. Boundary: this tests the
structure's followability and the sharpness rule on one effort; it does not test whether the map
prevents the over-planning failure, which is the failure the source itself documents.

---

### DEF-5 · Prototype as bounded evidence for one question

**1) Mechanism, trigger, anchors, read status**

| | |
| --- | --- |
| Mechanism | Build throwaway code that answers **one** stated question. Throwaway is a constraint on how the code is written (no tests, no error handling beyond runnable, no abstractions, no persistence), not a promise to destroy it: the **answer** is folded into the real code and the **prototype** is kept as a primary source so the next session can re-run the evidence |
| Trigger | A question cannot be settled by talking — a state model whose edge cases cannot be held in the head, or a layout that cannot be judged from a description |
| Provisional locus | E, with D for the design question and an F interface (the prototype is evidence about a design claim, not about the built artifact) |

Anchors: `prototype/SKILL.md` §Pick a branch L10–17, §Rules that apply to both L19–26;
`LOGIC.md` §Process steps 1–5 and §Anti-patterns; `UI.md` §Two sub-shapes, §Process steps 1–6,
§Anti-patterns; `docs/engineering/prototype.md` §Two branches, §The prototype is a primary source,
§Common questions, §It's working if. Read: full.

**2) Operation, conditions of validity, failure modes, counterexamples**

- *The question decides the shape, and the question is written down first.* "The question comes first
  and decides the shape of everything that follows; a prototype that answers the wrong question is pure
  waste, however good it looks." The logic branch states the question "at the top of the demo (in a
  visible intro, not just a comment)", which is what makes the artifact checkable by someone who
  arrives later.
- *Two branches with genuinely different artifacts.* Logic/state → **one self-contained HTML file** that
  opens by double-click: a labelled state panel re-rendered after every action, free-play buttons for
  poking at the model in any order, and tabbed guided walkthroughs each holding a scenario plus the
  ordered buttons to press. UI → **several structurally different variants** on one route, switchable
  from a floating bar and a URL parameter, where the requirement is that variants "disagree about
  structure, not colour" ("three tweaked card grids is wallpaper, not a prototype").
- *The audience argument, which is the reason for the HTML choice.* A terminal app "can only be driven
  by someone with the repo cloned and a runtime installed, which rules out exactly the people whose
  opinion the prototype needs: the designer, the PM, the domain expert who knows what the state model is
  supposed to mean." That is a *requirements* argument for a carrier, and it is the honest form of
  "one file, no build, email-able".
- *The pure-module rule.* "Put the actual logic … in a single `<script>` block written as a small, pure
  module that could be lifted out and dropped into the real codebase later. The page around it is
  throwaway; this module isn't." And the anti-pattern: "If the pure module references the DOM,
  `document`, or button handlers, it's no longer liftable."
- *Evidence preservation, with the reason.* The answer is captured durably (a commit message, a decision
  record, the implementation item) and the prototype is committed to a throwaway branch out of main,
  never merged, with a pointer from the implementation item. The stated reason is a question about the
  next reader: "who picks up the work next session, and what do they have to work from? A prose summary
  of a prototype loses the thing that made it convincing." The change from "delete it" is recorded as a
  deliberate reversal.
- *Conditions of validity.* A question that talking cannot settle; a willing human to look at it; and a
  place for the artifact. The UI branch adds: "much easier to judge when it's butting up against the
  rest of the app… A throwaway route on its own is a vacuum: every variant looks fine in isolation", so
  embedding in an existing screen is preferred and a new route is the last resort.
- *Failure mode → the point of the artifact.* "Someone says 'wait, that shouldn't be possible' or 'huh,
  I assumed X'. That's a bug in the *idea*, which is the entire point."
- *Bounded-scope counterexample.* Prototyping a whole application "has no natural stopping point, so it
  becomes the production app by momentum: the cleanup pass never happens, and code written under
  prototype rules (no tests, no error handling) ends up in front of users." The stated handling: if the
  need is a demo, build a demo and say so; if the need is a design question, cut it down to that.
- *Honest cost framing.* "The comparison that matters isn't tokens against zero; it's tokens against
  building the wrong state model and finding out after it has production callers."

**3) A–F loci and professional concern; Profile and call timing**

- **E** builds it; **D** owns the design question it answers; **F** does *not* verify the prototype as a
  delivered artifact — the prototype is evidence about a design claim, and the source is explicit that
  the answer is what folds into the real code. The prototype is a *primary source*, which is the
  Backbone's own term for the session-as-it-happened; the same reasoning (do not replace a primary
  source with a summary) applies.
- Professional concern: *Correctness* of the design decision; *Delivery risk*; *Cost* explicitly.
- Profile: `profiles/technical-planning.md` (D) when the question is a design question;
  `profiles/implementation.md` (E) to build it. Call timing: at the moment a question is identified as
  unanswerable by discussion — which in the product's vocabulary is *before* the decision that depends
  on it is fixed.

**4) Current product: exact text, what is covered, the residual gap, why**

Covered — the *spirit* appears once, in the Backbone's F section, and it is worth quoting because it
already gives the right permission: "设计挑战的对象是本次 Plan、责任放置与上游约束的关系，可在实施前使用
设计依据、反例或**原型证据**。" So the product already accepts prototype evidence as a legitimate basis for
challenging a design before implementation. `profiles/technical-planning.md` §按需方法入口 lists "方案比较
方法：存在实质方案分歧时使用" — a body-less candidate that a prototype would feed.

Residual gaps — four:
1. **No method for producing prototype evidence.** The Backbone permits it and no method says how. The
   question-first rule, the throwaway constraints (no tests, no error handling, no abstractions, no
   persistence), and the "state the question at the top" discipline are all absent.
2. **Evidence preservation is absent.** The product's discipline is to keep decisions and dispose of
   scaffolding, and it has no rule about *keeping the artifact the decision came from*. The source's
   argument — that a prose summary loses what made it convincing — is a genuine addition, and it is the
   same argument the product already accepts for primary vs secondary sources elsewhere (the
   `docs/overnight` record, the Charter's deliverable rule).
3. **No accessibility rule for the artifact.** "Someone who doesn't read code can drive the logic demo"
   is a *requirement on the carrier*, and the product has no such requirement. It matters because the
   value of a prototype is proportional to who can be put in front of it.
4. **No bounded-question rule.** The "whole app prototype" counterexample maps onto the product's real
   risk: an exploratory instance whose scope is not bounded by a question will harden into production.
   `charters/template.md` has `Object scope`, which is the right field, but nothing says the scope must
   be *one answerable question*.

Why worth absorbing: the product already permits the evidence and has no way to produce it; and the
preservation rule closes the gap between "a decision was taken on evidence" and "the evidence is
findable by the next person", which is exactly the handoff obligation the Backbone already imposes.

**5) Retain / change / delete; carrier; coupling; real-SDK dependency**

- **Retain** question-first with the question written on the artifact; throwaway-as-writing-constraint;
  the two branches chosen by the question; the pure liftable core with the DOM anti-pattern; the
  audience argument; preservation of the artifact as evidence with a pointer from the implementation
  record; the "bug in the idea" success signal; the bounded-question counterexample; the honest cost
  framing.
- **Change** the carriers: do not require HTML, a URL parameter, a floating bar, or a specific routing
  convention. The transferable requirements are (a) the artifact runs with one trivial action, (b) a
  non-author can drive it and see state after each step, (c) competing options differ structurally and
  can be switched without editing, (d) the core logic is separable from the disposable shell. Any
  carrier satisfying those is acceptable; the source's HTML choice is one answer to (a)+(b).
- **Delete** the framework/router snippets, the `process.env.NODE_ENV` gate, and the React-shaped
  switcher pseudocode.
- Carrier: a method body in `methods/` bound by a D or E Charter, referenced from
  `methods/README.md`; the preservation rule also wants one clause where the Charter states what the
  instance delivers.
- Real SDK/runtime dependency: **yes, and it is the point** — a prototype is only evidence if it runs
  where the question lives, so an adoption must accept that this method needs a real runtime and cannot
  be satisfied by a document.

**6) Draft text and verification plan (not executed)**

Draft (candidate method §Use/§Method):

> Use this when a design question cannot be settled by discussion: a state model whose awkward cases you
> cannot hold in your head, or a choice between layouts that all look reasonable in prose. Write the
> question on the artifact itself, at the top, where a reader who was not in the conversation will find
> it — an artifact that answers the wrong question is waste regardless of its quality. Then build the
> smallest thing that answers it, under throwaway rules: no tests, no error handling beyond what makes it
> run, no abstractions, no persistence. Keep the logic in a part that could be lifted into the real
> implementation unchanged, and keep the disposable shell thin over it; if the logic reaches into the
> shell, it is no longer liftable. Anyone whose judgement the question needs must be able to drive it
> without installing anything and must see the state after every step. Where the options under
> consideration are alternatives, make them differ in structure, not in cosmetics, and make switching
> between them cost nothing; judge them inside the surrounding context where possible, because an option
> judged alone always looks acceptable.
> When the question is answered: fold the answer into the real work, and **keep the artifact** where the
> next person can re-run it, with a pointer from the implementation record. A summary of a prototype
> loses what made it convincing. The artifact never merges into the main line.

Verification plan: take one unanswerable-by-discussion question, produce the artifact, and record (a)
whether a non-author could drive it unaided, (b) whether the question was answered in one sitting, and
(c) whether a second reader could locate the artifact from the implementation record alone. Boundary:
this measures the artifact's usability and findability; it does not establish that the resulting design
decision was better.

---

### DEF-6 · Delegated investigation and the fact-versus-decision rule

**1) Mechanism, trigger, anchors, read status**

| | |
| --- | --- |
| Mechanism | Delegate reading legwork to a background agent that works from **primary sources only**, follows every claim back to the source that owns it, and leaves **one cited file**; plus the selection rule that separates a *fact* (delegable, short-lived) from a *decision* (not this mechanism) |
| Trigger | The next step needs something found out from outside the working scope, and doing the reading inline would occupy the current work |
| Provisional locus | E/F (evidence acquisition) with A (what the open question is) |

Anchors: `research/SKILL.md` (whole, 12 lines: the three-item job); `docs/engineering/research.md`
§What it does, §Delegated legwork, §Common questions (the nesting failure, no allowlist for "high
trust", no reuse, no stopping criterion), §It's feeling if / §It's working if. Read: full.

**2) Operation, conditions of validity, failure modes, counterexamples**

- *Operation.* Three instructions and nothing else: investigate against primary sources (official docs,
  source code, specs, first-party APIs) "not a secondary write-up of them"; write the findings to a
  single file citing each claim's source; put it where the repo already keeps such notes, matching the
  existing convention, and say where.
- *The selection rule, which is the most transferable part.* The fact/decision split is stated as the
  boundary between two mechanisms: research produces short-lived assets ("what this library's auth
  mechanism does as of this week"), a decision record is kept — "If what you are producing is a decision
  rather than a fact, you are grilling, not researching." And the sharpest version of the shelf-life
  argument, quoted from a community thread: "ADRs yes. Everything else archive or delete after done. It
  otherwise becomes cruft of work and can poison future repo reads if you've drifted away from the
  spec/research."
- *Delegation economy, with the reason.* "You get a document to grill, plan, or design against, and you
  still make the call." The point of the background execution is not speed but that the current
  context is not spent on reading.
- *Conditions of validity.* A question narrow enough to be answerable ("A narrow, answerable question
  (one API, one behaviour, one version claim) comes back far better than 'research X'"), and a place to
  write. The source states there is **no stopping criterion** in the method and that both complaints —
  going far too deep, and covering a topic broadly while missing the one detail that mattered — "are the
  same gap"; scoping is the caller's job.
- *Honest gap with no shipped fix: "high-trust" is undecided by construction.* "The model does. The
  skill names the *kinds* of source that qualify … and there is no allowlist, no domain gate, and no
  verification pass." The recorded objection is unrefuted: "Five research subagents pointed at junk just
  gives you five confident wrong answers faster. How are you gating what counts as high-trust sources?"
  The only available mitigation is the citation discipline — follow two or three and check they land on
  the thing rather than a summary of the thing.
- *Failure mode with real content: self-perpetuating delegation.* Because the instruction does not
  restrict the agent type, the spawned agent holds the same instruction and fires it again; one report
  measured "roughly 450k tokens across three overlapping runs, with the duplicate finishing half an hour
  later entirely out of view", and the behaviour reproduced outside the original harness. The inverse
  failure also exists: a global instruction forbidding re-delegation makes the background agent decline
  the task and the method silently does nothing.
- *Failure mode: no reuse.* "Nothing auto-loads a past research file; it is a document sitting in the
  repo until a human or a skill points at it." The strongest challenge recorded against the design:
  "the value's the markdown becoming context the agent re-reads later, not the fetch itself. A
  write-once dead file is just a fancy search."
- *Counterexample / when not to use it.* "If a two-line prompt gets you what you need on a small
  question, use the two-line prompt." And against a host's own deep-research mode, "the difference is
  the artifact and the source discipline, not the search."

**3) A–F loci and professional concern; Profile and call timing**

- **A** owns the question being asked; **E/F** consume the result. The *decision* that the finding feeds
  stays with whoever owns it — the source's own sentence is "you still make the call", which is the
  product's "发现要记录，不能私下消化掉跨边界影响" applied to imported facts.
- Professional concern: *Correctness* (source quality) and *Cost* (delegation is also a spend).
- Profile: `profiles/intent-voice.md` (A) for the question; `profiles/evidence-evaluation.md` (F) for
  consuming the evidence with its source quality visible. Call timing: when a needed fact lies outside
  the object scope, and early enough that the dependent decision has not been fixed.

**4) Current product: exact text, what is covered, the residual gap, why**

Covered — `profiles/evidence-evaluation.md` §关键问题 already demands "证据来源与作者关系是什么？" and
§常见误区 rejects treating documents as verified conclusions ("把文档、字段非空、自测输出当作已验证结论"),
and `methods/behavior-claim-evaluation.md` §Method 2 requires preserving the original output as evidence
in an evidence-safe form. So the product has the *consumption* discipline.

Residual gaps — four:
1. **No acquisition mechanism.** The product has a strong rule for judging evidence and no method for
   obtaining it under delegation, which means the acquisition step is either inlined (spending the main
   context) or improvised.
2. **No primary-source rule.** "Follow every claim back to the source that owns it" and "do not repeat a
   blog post's account of an API when the API's own docs are reachable" is a concrete acquisition rule
   the product does not state anywhere. `profiles/evidence-evaluation.md` §关键问题 asks about source and
   authorship but not about *distance from the originating source*.
3. **No fact/decision boundary or shelf-life rule.** This is the gap with the strongest product
   analogue: the product keeps decisions and treats working material as disposable, and it has no rule
   telling a caller that an imported fact has a shelf life and must not be filed as a durable record.
   Without it, a fact file ages into a false premise — the same failure the source describes as
   "poison[ing] future repo reads".
4. **No artifact-reuse rule.** The product's Charter mechanism makes reuse explicit ("cease reuse must
   confirm the version/diff is still covered"), which is the *right* answer, and nothing says that a
   delegated finding is an artifact that must be attached to whatever consumes it. The source's own gap
   is the same one, so the product can do better here rather than copy: state that the file is a
   deliverable that must be pointed at, not a hope.
5. **Delegation-depth guard.** The nesting failure has a two-line fix (tell an agent that is already a
   delegate to do the work itself) and the product's own Driver text warns against "管到进程、并发、锁等
   execution mechanics" — so the guard must be phrased as a *delegation boundary*, not as runtime
   policy.

Why worth absorbing: gap 2 and gap 3 are each one sentence and close a real failure mode (junk sources;
aged facts as premises); gap 1 gives the fact-acquisition half of a profile whose §关键问题 already
assumes facts arrive with a provenance.

**5) Retain / change / delete; carrier; coupling; real-SDK dependency**

- **Retain** primary-sources-only with the follow-it-to-the-owner rule; one cited file; write it where
  the target already keeps such notes and say where; the fact/decision boundary with shelf life;
  delegation to keep the current context unspent; the narrow-question scoping rule; the honest "no
  allowlist" limitation; and the delegation-depth guard.
- **Change** the reuse answer: the source leaves "nothing auto-loads a past file" as an open gap. The
  product's existing rule (a consumer names the artifact and re-checks coverage before reuse) is
  *better* and should be the carried behaviour — do not import the gap.
- **Delete** the harness-specific background-agent launch and the "spawn a subagent" naming; phrase it
  as a delegation whose result is a cited artifact.
- Carrier: a method body in `methods/` (acquisition) whose *consumption* side stays with
  `methods/behavior-claim-evaluation.md`; plus a clause about fact shelf life wherever MG-6's decision
  record lands, since that is where the two meet.
- Real SDK/runtime dependency: **the sources are external** — the method needs real access to the source
  of truth (network or a vendored copy). Any adoption must state which access is assumed, because a
  primary-source rule is unsatisfiable without it.

**6) Draft text and verification plan (not executed)**

Draft (candidate method rule):

> When a fact is needed from outside the work in front of you, get it as a document rather than as
> conversation, and keep the reading out of the current context. Two rules make the document worth
> trusting. First, work from the source that owns the claim — the specification, the source file, the
> first-party description — not from someone's account of it; when you follow a claim, follow it all the
> way to the thing itself. Second, cite per claim, so a reader can check two of them at random and see
> whether the run landed on the thing or on a summary of the thing; that citation is the only check
> available, because nothing gates which sources count as authoritative. Put the result where the target
> already keeps notes, and say where.
> Scope the question narrowly — one behaviour, one interface, one version claim. A broad topic comes
> back broad and misses the detail that mattered, and there is no natural depth at which to stop.
> Know what you are producing: a **fact** has a shelf life and should be attached to whatever consumes
> it and disposed of after; a **decision** is durable and belongs in the decision record. Filing a fact
> as though it were a decision is how a stale premise becomes load-bearing later.
> Delegate the reading; keep the judgment. A delegate that is already a delegate does the work rather
> than delegating again.

Verification plan: run one narrow question through the mechanism and record (a) how many claims cite a
source that owns the claim versus a summary, (b) whether the artifact was reachable from the consumer,
and (c) whether any delegate attempted to delegate again. Boundary: (a) measures citation distance on
one run; it does not establish source quality, which the source itself leaves ungated.

---

### DEF-7 · Human-only procedures: a fixed library, authored stages, and static verification

**1) Mechanism, trigger, anchors, read status**

| | |
| --- | --- |
| Mechanism | When a step can only be taken by a person (provisioning, credentials, an unfamiliar dashboard, a one-off migration), emit an executable procedure whose **invariant scaffolding is fixed and identical everywhere** and whose **per-instance content is the only authored part**, with a static verification path because the artifact cannot be run unattended |
| Trigger | A task reaches a point where a human must act outside the agent's reach, and the steps would otherwise be written into chat where they scroll away |
| Provisional locus | E |

Anchors: `wizard/SKILL.md` §1 Scope the procedure L16–26 (read the environment, don't ask cold; the
stage list and per-value destination), §2 Map each stage's journey L27–32 ("never invent steps that may
not exist"), §3 Author the wizard L33–38 (the helper list; `TOTAL_STAGES`; the invariant-library rule),
§4 Verify and hand off L39–44 (static verification + the trace);
`wizard/template.sh` (the library above the `STAGES` marker: colour/progress, `open_url` with WSL and
explorer paths, `pause`, `confirm`, idempotent `ask`/`ask_secret` with re-run defaults, `write_env`
upsert, `set_secret`/`set_var` with availability and auth checks plus a skipped-list, and `finish`);
`docs/engineering/wizard.md` §Stages, §The template already solves the UX, §Common questions,
§Ephemeral by default. Read: full.

**2) Operation, conditions of validity, failure modes, counterexamples**

- *The scaffolding/content split is the mechanism.* "Everything above the `STAGES` marker is a fixed
  library, identical in every wizard and never hand-edited. The consistency is the point. Your job is
  only to scope the procedure and author its stages." This is a reusable authoring discipline: separate
  the invariant part, make the boundary a literal marker, and forbid edits across it.
- *Scope by reading the environment, not by asking cold.* The source enumerates: `.env`, `.env.example`,
  `.env.*`, `README`, `docker-compose*`, framework config, and every `secrets.*` / `vars.*` reference in
  the CI workflows — "each of those is a value the wizard has to produce". This turns scoping from an
  interview into a derivation from artifacts, and it is what produces the "hidden prerequisites"
  discovery benefit the page claims.
- *Every captured value has a declared destination and a declared sensitivity.* A five-way destination
  table (environment only / CI secret / CI variable / both / nowhere because the stage is a pure
  action), and secrecy decides hidden entry. "Done when" for scoping is stated as exactly these three
  facts per value: where the human gets it, where it is written, and whether it is secret.
- *Never invent the path.* "Where you don't actually know the current UI or the exact command, say so
  and ask the user or check the docs: never invent steps that may not exist." For procedurally-generated
  instructions, hallucinated clicks are the equivalent of a fabricated citation.
- *Ordering rules with reasons.* Open the URL before asking for its value ("You're never asked to paste
  something you haven't been sent to fetch"); a stage is one focused task because the screen is cleared
  between stages and "a stage that overflows the screen loses the part that scrolled away"; `confirm`
  before any irreversible action.
- *Static verification for an unexecutable artifact — the most transferable rule in the group.* The
  author never runs it end to end because "it opens browsers and blocks on human input". Instead:
  `bash -n`, `shellcheck` where available, `chmod +x`, and a **trace** that every value from scoping is
  captured and lands where scoping said, with "every `set_secret` name exactly matches a `secrets.*`
  reference in CI". The source states the consequence honestly: "the first run is yours, and that run is
  the test."
- *Secret handling and its stated boundary.* Hidden entry straight to the destination, with the caveat
  that this holds only for values captured at run time — "If you paste a key into the chat while scoping
  the procedure, it's in the context like any other pasted text." The model never receives the value
  because the model writes the script and the human runs it.
- *Ephemeral by default, with an explicit promotion test.* One-off or personal → save to a scratch path,
  run, delete. "A setup path the next person on the repo will also need" → commit and link from the
  README.
- *Failure modes with real content.* There is no back button, so a wrong entry means re-running; the
  designed mitigation is idempotence — values already written are offered back as defaults, so you
  "press Enter through the stages you got right". Arrow keys insert escape sequences because prompts use
  `read -r` rather than a line editor (backspace works). And `gh` missing or unauthenticated degrades a
  stage to a warning plus a closing summary of what must be done by hand, "instead of failing the run" —
  a deliberate partial-success design.

**3) A–F loci and professional concern; Profile and call timing**

- **E** owns the artifact. The *human's own steps* stay with the human — the source's discipline is that
  the script prompts and waits and does not perform the action on the human's behalf, which matches
  `guide-redacted-evidence.md` §Rules 6's step/capture split already in the product. Authority is
  untouched: the wizard performs no action the human could not, and it never runs itself.
- Professional concern: *Security* (credentials), *Correctness* (procedure that can be followed),
  *Cost* (re-explaining the same setup).
- Profile: `profiles/implementation.md` (E). Call timing: when a required step falls outside the
  instance's reach and the alternative is prose in a conversation. It is not a stage and not a gate.

**4) Current product: exact text, what is covered, the residual gap, why**

Covered — the *recognition* exists: `guide-redacted-evidence.md` §Rules 6 already handles a human-only
step in a runnable loop ("Human-only actions stay in the user's own flow as a `step`; the script prompts
and waits, does not collect the action") and §Rules 2/4 own the credentials boundary. So the product has
the HITL primitive and the custody rules.

Residual gaps — four:
1. **No artifact for a multi-step human procedure.** The product has a `step` in the redaction guide —
   one prompt inside a script whose purpose is collecting evidence. It has nothing for "a procedure with
   ten ordered stages, values captured along the way, and destinations to write them to", which is the
   shape of most provisioning work. This is the group's substantive gap.
2. **No scaffolding/content split convention.** The "fixed library above the marker, never hand-edited"
   discipline is a genuinely reusable authoring rule and the product has no equivalent. It is the same
   idea as the product's own source/export split (`authority/RESPONSIBILITY-BACKBONE.md` is a projection
   with matching digests and a "do not edit the projection; change the source" rule) — so the product
   already accepts the pattern in one place and has no general form of it.
3. **No static-verification rule for artifacts that cannot be executed.** This is the most valuable
   single item: the product's F discipline assumes evidence from execution, and this class of artifact
   (a procedure that blocks on a human) can never be executed by its author. The answer — syntax check,
   static analysis, and a *trace* that every declared input is captured and every declared destination
   is written — is a real verification design for a real class of work.
4. **No "derive the inputs from the environment" rule.** "Read the repo first, don't ask cold" is the
   same principle as ABC MG-9's facts-are-the-asker's-job, applied to a procedure's inputs; the product
   states it for questions and not for artifacts.

Why worth absorbing: gap 1 is a real class of work the product cannot currently serve; gap 3 supplies a
verification design where the product's normal one is unavailable; gap 2 generalises a pattern the
product already trusts.

**5) Retain / change / delete; carrier; coupling; real-SDK dependency**

- **Retain** the scaffolding/content split with the literal marker; scope-by-reading-the-environment
  with the enumerated sources; per-value destination and sensitivity declarations with the scoping
  done-condition; never-invent-the-path; open-before-ask; one-stage-one-screen; confirm-before-irreversible;
  idempotent re-run with offered defaults; partial-success degradation with a skipped list; ephemeral-by-default
  with the promotion test; and the static verification (syntax, analysis, trace) with its honest
  consequence that the first run is the test.
- **Change** the shell target: the mechanism is "an executable procedure with a fixed scaffold", not
  "a bash script". Keep the properties (runs where the human is, opens what it names, hides secret
  entry, is idempotent on re-run, reports what it could not do) and let the carrier follow the target.
- **Delete** the platform specifics: the `gh secret`/`gh variable` calls, the WSL/`explorer.exe`/`xdg-open`
  branch, and the bash helper names.
- Carrier: a method body in `methods/` (produce a human procedure) plus, if the gate accepts it, one
  reusable scaffold as an on-demand support file — because the fixed-library half is only a mechanism if
  the library is single-sourced, which is exactly the product's own single-source rule.
- Real SDK/runtime dependency: **yes, and it is irreducible** — the artifact only exists to be run by a
  human on a real machine, and the third-party services it configures are real. Any adoption must state
  that this method cannot be verified by its author end to end.

**6) Draft text and verification plan (not executed)**

Draft (candidate method rule):

> When a step can only be taken by a person, produce a procedure they run, not instructions they read.
> Derive its inputs from the environment before writing anything: configuration files, the compose or
> framework setup, and every secret or variable the automation already references — each of those is a
> value the procedure must obtain, and finding them is what surfaces the prerequisites nobody
> mentioned. For each value decide three things and write them down: where the person gets it, where it
> is written, and whether it is secret. Then order the steps so that whatever the person must fetch is
> opened before they are asked for it, and so each step fits on one screen — a step that scrolls loses
> the part that scrolled away. Ask for confirmation before anything irreversible, and hide entry for
> anything secret. Never write a click path you are not sure of; if the current interface is unknown,
> say so and ask.
> Keep the invariant part fixed: if there is a scaffold that handles progress, prompting, re-run
> defaults and the closing summary, treat it as a library and author only the steps. Do not hand-edit
> the library — its consistency is the reason it exists.
> You cannot run this to completion, because it waits for a person. Verify it statically instead:
> syntax-check it, run a static analyser where one exists, and trace it — every value you identified is
> obtained, every value reaches the destination you declared, and every secret name matches something
> that actually reads it. Then say plainly that the first run is the test.

Verification plan: produce one procedure for a bounded manual setup and record (a) whether the
declared-input list matched what the procedure actually obtained, (b) whether any step's click path was
invented rather than verified, and (c) whether the trace found a value that reached nowhere. Boundary:
this tests the scoping and static-verification rules on one procedure; it does not establish that a
human can complete it, which only a run can show.

---

### DEF-8 · Merge and rebase: resolve intent, then re-verify

**1) Mechanism, trigger, anchors, read status**

| | |
| --- | --- |
| Mechanism | Resolve a conflict by tracing each side to the **intent** behind it (commit message, change request, original issue) rather than by choosing between blocks of text; preserve both intentions where possible, otherwise choose by the operation's stated goal and say what was traded; and re-run the project's own checks before committing, because a merge is the easiest place to produce code that satisfies both sides and passes neither's tests |
| Trigger | A merge or rebase has stopped on conflicts |
| Provisional locus | E, with F for the checks it runs |

Anchors: `resolving-merge-conflicts/SKILL.md` (whole, 14 lines, five numbered steps);
`docs/engineering/resolving-merge-conflicts.md` §Primary sources over `ours` and `theirs`,
§Common questions, §It's working if, §Where it fits. Read: full.

**2) Operation, conditions of validity, failure modes, counterexamples**

- *The five steps.* See the current state; find the primary sources for each side and understand "why
  each change was made, and what the original intent was"; resolve each hunk preserving both intents
  where possible, choosing by the merge's stated goal where not and noting the trade-off, inventing no
  new behaviour, always resolving and never `--abort`; discover and run the project's automated checks
  (typically typecheck, then tests, then format) and fix what the merge broke; finish — stage and commit,
  continuing through every remaining commit in a rebase.
- *Why the intent step is the mechanism and not politeness.* The failure it exists to kill is stated
  precisely: resolving by flag or by deleting the block that looks less important "can be syntactically
  perfect and still silently drop a change somebody made on purpose. You cannot preserve an intent you
  have not read." So the ordering — history first, diff second — is load-bearing.
- *Why the checks step is separate.* "A merge is the easiest place in git to produce code that satisfies
  both branches and passes neither's tests." This is a measurement-validity argument, not a
  housekeeping step, and it is the reason the checks belong *before* the commit rather than after
  something breaks.
- *The never-abort rule with its reason.* "Aborting throws away the resolution work and returns you to
  the same conflict, unchanged, the next time you try… If you have decided it should not happen, that is
  a decision to make before invoking."
- *Conditions of validity.* The histories are reachable and the intent is recorded somewhere. The source
  is candid that where intent is not recorded, the mechanism degrades to diff-reading.
- *Counterexample / honest value statement.* "Claude Code already resolves conflicts pretty well on its
  own. Why does this need a skill?" — and the answer is itself a boundary: "The value is the two steps
  it will not let the agent skip: reading why each side exists, and running the checks afterwards. That
  is a thin margin over a good model, and it is meant to be: at least one reader has predicted this is a
  whole skill that becomes a no-op as models improve."
- *Parallel-work guidance, which is a separate finding.* Zoning files off between parallel tasks "costs
  more than it saves, because agents are good enough at merge conflicts that the tradeoff is not as harsh
  as it looks. The one piece of discipline worth keeping is to do large refactors first." And a field
  report on sibling sessions each building in their own tree: the merge back is best done by the session
  that wrote the change, "because it is the one that already knows the intent. Batching everybody's
  conflicts onto one agent at the end throws away exactly the context step 2 of this skill has to go and
  reconstruct."

**3) A–F loci and professional concern; Profile and call timing**

- **E** owns the resolution; **F** owns the checks' outcome and the verdict. The intent-tracing step
  consumes B/C/D **records** — commit messages, change requests, issues — which is why a repository with
  no decision record has a weaker version of this mechanism available (a direct dependency on ABC MG-6).
- Professional concern: *Correctness* (silently dropped intent) and *Maintainability*.
- Profile: `profiles/implementation.md` (E). Call timing: when a merge/rebase has stopped — reactive,
  not scheduled.

**4) Current product: exact text, what is covered, the residual gap, why**

Covered — partially and structurally. `profiles/implementation.md` §心智模型 includes "实现是发现事实的
地方" and §边界事实 states "实现中若需改变共享语义、接口或验证依据，先停依赖该结论的工作，保全已完成结果，
再走召回" — which covers the "I discovered something while working" case, not the conflict case.
`methods/local-defect-feedback-loop.md` §Method 5 owns "Rerun the original scenario and relevant
regression checks on the candidate version."

Residual gaps — three:
1. **No conflict-resolution mechanism at all.** Nothing in the core describes resolving a conflict by
   intent, preserving both sides, or choosing by the operation's stated goal. An E instance facing a
   conflict currently has no bound method, and `methods/README.md`'s three rows contain none for it.
2. **No "verify after integration" rule.** The product requires rerunning *the original scenario* for a
   defect repair. It has no rule that after combining two histories the project's own checks must run
   before the result is committed, which is the specific validity risk the source names.
3. **The parallel-writer guidance is absent and the product needs its own version.** `profiles/driver.md`
   §关键问题 asks about write-sets and single-writer serialisation — good, and *different*: the source's
   answer is not "zone the files" but "do the wide refactor first, and let the author of a change merge
   it, because they hold the intent". Given the product expects parallel instances, the *who merges* rule
   is a real addition: a merge performed by anyone other than the author loses the intent the resolution
   needs.

Why worth absorbing: gap 1 is a bound-method hole for a routine E situation; gap 2 is one sentence; gap 3
is a coordination rule the product's own parallelism assumption makes necessary.

**5) Retain / change / delete; carrier; coupling; real-SDK dependency**

- **Retain** intent-first with the quoted reason; preserve-both-then-choose-by-goal with the trade-off
  named; invent-nothing; never abort; run the project's own checks before committing with the
  satisfies-both-passes-neither argument; wide-refactors-first; and the author-merges-it rule.
- **Change** the trigger phrasing away from a specific VCS operation: the mechanism is "combining two
  independently-intentioned changes", and naming git (or `--abort`) should be an instance, not the
  mechanism's definition.
- **Delete** the `--ours`/`--theirs` framing as the organising idea (keep it as the anti-pattern) and any
  harness-specific tooling names.
- Carrier: a short method body in `methods/`; the who-merges rule belongs with the Driver's write-set
  clause (`profiles/driver.md` §关键问题), not in the method.
- Real SDK/runtime dependency: **yes** — a real repository with real history. The intent step is
  unsatisfiable without reachable history.

**6) Draft text and verification plan (not executed)**

Draft (candidate method rule):

> A conflict is not a text problem. Before touching a hunk, find out why each side exists — the message
> that introduced it, the request or issue it came from — so you are choosing between two intentions
> rather than between two blocks. Preserve both where they are compatible. Where they genuinely are not,
> choose the side that matches what this combination is for, and say plainly what was given up; do not
> invent behaviour that neither side had. The combination is going to happen: do not discard the
> resolution and return to the same conflict later.
> Combining two changes is the easiest way to produce code that honours both and satisfies neither, so
> find the project's own checks and run them before the result is committed, not after something looks
> wrong.
> Two habits around this: do the wide mechanical change before the branches that will have to merge past
> it, and let whoever wrote a change resolve its conflicts, because they already hold the intent that a
> third party would have to reconstruct.

Verification plan: take one historical merge with recorded intent and record (a) whether each hunk's
resolution can be traced to a stated intent, (b) whether any behaviour appeared that existed on neither
side, and (c) whether the project's checks ran before the merge commit. Boundary: a retrospective
reading of one merge; it does not measure resolution quality, and the source itself notes the margin
over a capable model is thin.

---

### DEF-9 · Context transfer: portability, not compression

**1) Mechanism, trigger, anchors, read status**

| | |
| --- | --- |
| Mechanism | When work must **travel** out of the current context, write a single document carrying only what is still in flight, plus what the next reader should reach for, and **reference** everything already written down by pointer rather than copying it |
| Trigger | One of four situations: a different host/tool, a different directory, a different person, or a side task forked off mid-work. Absent one of those, the correct move is to continue or to compress in place |
| Provisional locus | Driver (transfer) with A/B/D unchanged by the transfer |

Anchors: `handoff/SKILL.md` (whole, 16 lines: temp location, suggested-skills section, reference-don't-duplicate,
redact, tailor by argument); `claude-handoff/SKILL.md` (same contract, delivered as a seeded background
agent with a descriptive name); `docs/productivity/handoff.md` §What it does (portability-not-compression),
§When to reach for it (the four-situation table + "for anything else … `/compact` is the move"),
§What travels, and what doesn't, §Common questions (temp lifecycle, the what-not-why criticism, the
pointer-chasing trap), §It's working if. Read: full.

**2) Operation, conditions of validity, failure modes, counterexamples**

- *The framing that makes the mechanism narrow and therefore usable.* "What it buys is **portability**,
  not compression. That makes the skill narrower than it sounds. You need a file only when the work has
  to *travel*." And the contrast with the alternatives: "`/compact` preserves your intent, `/clear`
  preserves nothing, `/handoff` preserves the work's ability to move."
- *Reference, don't copy — with the reason.* "Specs, plans, ADRs, issues, commits and diffs are
  referenced by path or URL, never copied. That keeps the file small, and it keeps the settled detail in
  one place instead of two that drift." This is the product's single-source-of-truth rule expressed as a
  transfer rule, and it is the mechanism's most transferable part.
- *What does travel.* The live thread (what is in flight, why, what is next) plus a section naming the
  methods/skills the next reader should reach for — which the source justifies by matching the reader's
  own likely choice ("The suggested-skills section names the skill you'd have reached for yourself").
  Sensitive information is redacted before writing.
- *The fork case, which the source says is the one people skip.* The description "reads like session
  resumption… Read that way it looks like a worse `/compact`, so it gets skimmed past. The fork case is
  the one worth knowing": you stay in your session and hand a copy of the accumulated context to a second
  worker in parallel, then bring the answer back and reference it from the original thread. Two crossings,
  one live conversation, nothing re-explained.
- *Conditions of validity.* Something is actually travelling. The source states the failure plainly: the
  file is a *transit* document, not maintained, and several environments clear temp between sessions, so
  "If the next session isn't starting within the hour, or is starting under a different harness, copy the
  file somewhere durable yourself as soon as it's written."
- *Failure mode with real content: pointer chasing.* "The same applies to anything the document *points
  at*: a dispatch that references other files in temp is a dispatch the next agent can't follow."
- *Failure mode: the what-not-why criticism, with both mitigations.* "A fair and repeated criticism. Two
  things help. Pass the argument (tell it what the next session is for) so the reasoning that bears on
  *that* is kept rather than flattened. And watch for confident claims the session never actually
  verified: 'X isn't built', 'Y is done'. The next agent treats the document as a contract and will not
  re-check it, so a belief written as a fact becomes a false premise for everything that follows." The
  instruction to the author is therefore: read it before handing it over, and downgrade anything you only
  assumed.
- *Boundary case.* Where a mechanism exists that copies context exactly (a session fork), the source
  says plainly that "A fork inherits an exact copy of the context; this skill produces a *targeted*
  compression aimed at a stated next task, in a file. Where a fork will do … a fork is less work."
- *Counterexample for the "is it durable?" instinct.* "Ask whether it's true next month. `CLAUDE.md` is
  standing context about the project, loaded into every session whether it's relevant or not. A handoff is
  about one piece of work in flight and is dead once that work lands. Facts that keep getting re-explained
  are a `CLAUDE.md` problem; a half-finished task is a handoff."

**3) A–F loci and professional concern; Profile and call timing**

- The transfer itself changes no responsibility: A–F conclusions survive it, and the Backbone's Driver owns
  routing. **Voice** is only involved if a human-reserved decision travels.
- Professional concern: *Delivery risk* (work lost or re-explained) and *Cost*.
- Profile: `profiles/driver.md` (routing/transfer), `charters/template.md` §Handoff and return for the
  receiving side. Call timing: at a boundary where something is travelling — the product has the boundary
  concept (independence, reuse) and no stated transfer rule.

**4) Current product: exact text, what is covered, the residual gap, why**

Covered — the *handoff contract* exists in the Charter:
> `charters/template.md` §Handoff and return: "**Deliver:** <specific object, evidence, deviations, and
> remaining questions>" … "**Recall:** <what finding makes dependent work stop; send Driver the affected
> object, fact, and impact…>"

and `profiles/implementation.md` §交出 asks for "实现结果与相关变更、自测证据、偏离与剩余问题、受影响依赖".

Residual gaps — three:
1. **No portability-versus-compression distinction.** The product's transfer vocabulary is
   Deliver/Recall, which is about *what the receiving judgment needs*. It has nothing for the case where
   the same work continues somewhere the context cannot follow — and therefore nothing telling a caller
   when a written transfer is **not** the right move. The source's four-situation trigger is the usable
   form: a transfer document is for travel, and the ordinary same-place case should not produce one.
2. **No reference-don't-copy rule.** This is the gap with the clearest product analogue and the clearest
   remedy: the product's Deliver fields list objects and evidence, and nothing says that an object
   already written down is *pointed at*, never restated. Without it, a transferred brief duplicates the
   record and the two drift — exactly the risk the product's own single-source discipline addresses
   everywhere else.
3. **No "the reader will not re-check it" rule.** The source's sentence — "The next agent treats the
   document as a contract and will not re-check it, so a belief written as a fact becomes a false
   premise" — is a real instruction to the *author* to downgrade unverified claims. This maps directly
   onto the product's fact/assumption/unknown split (`profiles/intent-voice.md` §心智模型: "哪些是观察事实、
   哪些是推断、哪些还是未知"), and the product does not apply that split to its own deliverables.
4. Two smaller items: **the fork-as-artifact-return pattern** (go out, answer, come back, reference it
   from the original thread) and the **durability question** ("is this true next month" decides whether a
   fact belongs in standing context or in a transfer document).

Why worth absorbing: gap 2 is one clause and removes a drift source the product already disdains; gap 3
is one clause and closes the false-premise failure; gap 1 is small and prevents a written artifact from
being produced for transfers that do not need one — i.e. it prevents ceremony, which is exactly the
product's stated priority.

**5) Retain / change / delete; carrier; coupling; real-SDK dependency**

- **Retain** portability-not-compression with the four-situation trigger; the continue/clear/transfer/compress
  contrast; reference-don't-copy with the drift reason; what travels (live thread + what to reach for);
  redact before writing; author must downgrade unverified claims; the pointer-chasing warning; the
  durability question; and the fork case.
- **Change** the substrate: the source mandates the OS temp directory, which is what creates the
  lifecycle failures. The transferable rule is "a transit document, not a maintained artifact" plus
  "place it where the receiver can actually read it" — a target that survives the handover is a
  *requirement*, and temp is one answer that the source itself documents as failing.
- **Delete** the harness-specific launch (`--bg`, names for the job list) and the `/compact`, `/clear`,
  `/branch` names as mechanisms; keep them as the contrast being drawn.
- Carrier: the Charter's §Handoff and return is the natural home for the reference-don't-copy and
  downgrade rules; the portability trigger belongs in `profiles/driver.md`'s method entry list.
- Real SDK/runtime dependency: **none** for the rules; the carrier choice depends on where the receiver
  runs.

**6) Draft text and verification plan (not executed)**

Draft (candidate rule for the Charter's handoff field):

> Write a transfer document only when the work is going somewhere this context cannot follow: another
> tool, another directory, another person, or a fork of the task running alongside. In the ordinary case
> — same place, same work continuing — do not produce one; compress in place instead, because a written
> transfer is lossy in exchange for portability and you only want to pay that when portability is what
> you need.
> Carry what is in flight: what is being done and why, what is next, and what the next reader should
> reach for. Everything already written down — decisions, contracts, plans, changes — is **named, not
> restated**: a copy in two places is a second thing to keep true, and it will drift.
> Before handing it over, read it as a stranger and mark anything you only assumed as assumed. The next
> reader will treat this as settled and will not re-check it; a guess written as a fact becomes their
> false starting point. Remove anything sensitive. And check that everything you point at will still be
> there when they arrive — a reference into a temporary location is a reference they cannot follow.

Verification plan: on one real transfer, record (a) whether any object was restated rather than pointed
at, (b) whether the receiver could resolve every reference, and (c) whether any claim in the document was
an assumption presented as fact. Boundary: this tests the authoring rules on one transfer; it does not
establish that the transfer was sufficient, which is the receiver's judgment.

---

### DEF-10 · Durable learning workspace: mission, retrieval strength, and record-gated progression

**1) Mechanism, trigger, anchors, read status**

| | |
| --- | --- |
| Mechanism | Treat the working directory as a **stateful workspace for one topic**: a stated reason to learn it (which gates everything), a curated source list, short self-contained lessons, separate reference documents that are the artifacts actually revisited, reusable components shared across lessons, and **records that capture demonstrated understanding only** and are used to choose what to work on next |
| Trigger | Learning the topic *is* the project, over more than one sitting |
| Provisional locus | E/D — a durable-artifact discipline that generalises beyond teaching |

Anchors: `teach/SKILL.md` §Teaching Workspace L10–21, §Philosophy L22–33, §Fluency vs Storage Strength
L34–46, §Lessons L47–62, §Assets L63–70, §The Mission L71–80, §Zone Of Proximal Development L81–90,
§Knowledge L91–98, §Skills L99–111, §Acquiring Wisdom L112–121, §Reference Documents L122–137,
§NOTES.md L138–140; `MISSION-FORMAT.md` (Why / Success looks like / Constraints / Out of scope + five
rules incl. "Push back on vagueness"); `RESOURCES-FORMAT.md` (Knowledge / Wisdom split, annotate every
entry, surface gaps, prune ruthlessly); `LEARNING-RECORD-FORMAT.md` (four qualifying triggers, three
explicit non-qualifiers, supersession by marking); `GLOSSARY-FORMAT.md` (the `_Avoid_` shape — screened in
ABC MG-7). Read: full. `docs/productivity/teach.md` used for documented failure modes.

**2) Operation, conditions of validity, failure modes, counterexamples**

- *The two-load distinction, with the asymmetry that makes it operational.* "**Fluency strength**:
  in-the-moment retrieval of knowledge. **Storage strength**: long-term retention of knowledge. Fluency
  can give the user an illusory sense of mastery, but storage strength is the real goal." And the
  asymmetry that decides how to design: "For acquiring knowledge, difficulty is the enemy. It eats
  working memory you need for understanding" whereas "For skill acquisition, difficulty is the tool.
  Effortful retrieval is what builds storage strength." Presented with difficulty is a *lever whose sign
  depends on the phase* — that is the transferable insight, and it generalises to any durable skill
  rather than only to teaching.
- *Records are gated on demonstrated understanding, not coverage.* The four qualifying triggers are
  (demonstrated understanding of something non-trivial; disclosed prior knowledge including its claimed
  depth; a corrected misconception; a mission shift). The three explicit non-qualifiers are the important
  part: "Material that was merely covered. Coverage is not learning. Wait for evidence." / anything
  already captured tersely as a term definition / "Session-by-session activity logs. Learning records are
  not a journal: they are decision-grade insights." Supersession is by marking, not deletion, "because
  the history of how understanding evolved is itself useful signal."
- *The reference/lesson split decides where effort is spent.* "Lessons will rarely be revisited later -
  reference documents will be. They should be the compressed essence of the lesson, in a format designed
  for quick reference." Concretely: the syntax table, the algorithm, the pose sequence, the glossary
  belong in the reference, not buried in the lesson that introduced them.
- *Components with a read-before-author rule.* "Before authoring a lesson, read `./assets/` and build from
  the components already there. When a lesson needs something new and reusable, write it as a component
  in `./assets/` and link to it; never inline code a future lesson would duplicate." And the shared
  stylesheet is "the first component every workspace earns", because it is what stops the output being
  "a pile of one-offs".
- *The mission as the anti-drift device, with a forcing function.* "If the user is unclear about the
  mission, or the `MISSION.md` is not populated, your first job should be to question the user on why they
  want to learn this. Failing to understand the mission will mean knowledge acquisition is not grounded in
  real-world goals. Lessons will feel too abstract. You will have no way of judging what the user should
  do next." And the mission format's own rule: "**Push back on vagueness.** If the user cannot articulate
  why, interview them before writing anything. A bad mission is worse than no mission."
- *Progression is computed, not chosen by feel.* The next lesson comes from the records plus the mission,
  targeting the zone where the work is "challenging enough to take effort, not so far ahead that it stops
  being learnable".
- *Wisdom is delegated, with an opt-out.* Real-world judgement questions get an attempted answer plus a
  pointer to a community where the skill can be tested; "If the user expresses a preference that they
  don't want to join a community, respect it."
- *Parametric knowledge is untrusted.* "Never trust your parametric knowledge" — sources are gathered and
  recorded first (`RESOURCES.md` annotated, Knowledge vs Wisdom, gaps surfaced explicitly, pruned
  ruthlessly), and lessons carry citations plus one recommended primary source.
- *Failure modes, documented.* No assessment step, so session one assumes a level ("It never did
  grilling to establish my starting point so it made lots of assumptions of what I already knew").
  Fabrication is not hypothetical (a learner given move sequences that do not solve the puzzle), with the
  documented diagnostic being model, harness, effort, and source — and risk highest in procedural
  domains with precise notation, lowest where output is immediately verifiable. The quiz-answer-position
  defect (the correct answer landing first, reportedly 33/33 across nine lessons) is a *component* bug,
  not a wording bug, and the fix is a shuffling component. No spaced repetition and no exit criteria:
  "good at making the next lesson, but not as good at knowing when to stop and switch to review or real
  practice."

**3) A–F loci and professional concern; Profile and call timing**

- **E/D** own the workspace. Nothing here transfers authority; the mission is *A-shaped* content (why,
  for whom, what is out of scope), and reading it as A is the right mapping — which is why the mission
  format is the most product-relevant artifact in the group.
- Professional concern: *Correctness* (untrusted parametric knowledge) and *Cost*.
- Profile: no core Profile owns "learning"; the transferable pieces map onto
  `profiles/intent-voice.md` (mission/scope: the why plus explicit non-goals) and
  `profiles/evidence-evaluation.md` (source quality, citations, "is this verifiable"). Call timing: when
  the deliverable is *durable knowledge* rather than a change.

**4) Current product: exact text, what is covered, the residual gap, why**

Covered — nothing directly, and the honest question is whether the product wants this class of content at
all. Two mappings are real: `MISSION-FORMAT.md`'s shape is a near-twin of the product's problem-definition
obligation — `profiles/intent-voice.md` §交出: "可理解的问题定义、目标与非目标、事实/假设/未知划分" — and
`RESOURCES-FORMAT.md`'s "annotate every entry … what it covers and when to reach for it" is the same rule
as ABC MG-8's pointer wording.

Residual gaps — four, with a scoping caveat:
1. **The difficulty-sign-depends-on-phase rule is absent and is generally useful.** The product's methods
   treat difficulty as a cost to be minimised (the anti-ceremony posture). Nothing says that in one class
   of work difficulty is the *mechanism* (retrieval, spacing, interleaving) while in another it is the
   *enemy* (working-memory load during comprehension). Any product method that produces durable
   capability — rather than a one-off artifact — needs that distinction, and the product has no such
   method today.
2. **Coverage-is-not-learning is a general record-quality rule.** The three non-qualifiers are exactly the
   discipline that keeps a growing record honest, and the product has an analogous risk: a decision record
   written because something was *discussed* rather than *decided*. ABC MG-6 already proposes the three
   gates; this adds the negative form ("what does **not** qualify") which is the part that is usually
   omitted and the part that prevents inflation.
3. **The reference-versus-ephemeral split is a carrier rule the product lacks.** "Lessons will rarely be
   revisited; reference documents will be" is a *prediction about reuse* used to decide where content
   goes. The product decides carrier by responsibility instead, which is correct and orthogonal; the reuse
   prediction is the missing complement — it is what tells you whether a piece of content belongs in an
   always-loaded Profile or behind a pointer.
4. **Components with read-before-author and never-inline-a-reusable.** Directly applicable: the product
   has five method files and two guides, and no rule saying that a new method must first check whether an
   existing one already carries the mechanism, and must never inline what a second method would duplicate.
   That is precisely the rule whose absence produces the duplication this package's own §3.4 observation
   found in the source repo.

**Scoping caveat for the gate:** items 1–4 are all *transferable rules*, not a proposal to add a teaching
workspace to the product. The teaching-specific content (lessons as HTML, missions for learners, zones of
proximal development) is domain content for a capability the product does not have and is not obviously
asked to have. If the gate wants only the transferable four, they belong as clauses in existing homes,
not as a new method.

**5) Retain / change / delete; carrier; coupling; real-SDK dependency**

- **Retain** (as transferable rules): the mission-before-content forcing function with "a bad mission is
  worse than no mission"; the explicit-non-goals field; the difficulty-sign distinction; the
  coverage-is-not-learning record gate with supersession-by-marking; the reuse-prediction carrier rule; the
  components discipline (read-before-author, never inline a reusable, one shared base first); annotated
  sources with an explicit gaps section and ruthless pruning; untrusted parametric knowledge with
  per-claim citations.
- **Change**: do not import the learning workspace itself, the lesson format, or the zone-of-proximal-development
  apparatus. Those serve a deliverable class the product does not have.
- **Delete** the HTML lesson carrier, the community/forum sourcing, and the quiz mechanics.
- Carrier: clauses in existing homes — `profiles/intent-voice.md` (mission shape) and
  `profiles/evidence-evaluation.md` / `guide-*` (source annotation, citations, untrusted priors); the
  coverage-gate and reuse-prediction rules belong with MG-6 (decision records) and MG-8 (document
  economy) respectively.
- Real SDK/runtime dependency: **none** for the transferred rules; the source's HTML lessons and quiz
  components are the parts with a runtime, and they are not proposed for carriage.

**6) Draft text and verification plan (not executed)**

Draft (candidate clauses):

> **State why before deciding what.** Work whose output somebody must *understand* later needs its
> reason written first, concretely: what becomes possible, and what is explicitly not being pursued. A
> vague reason is worse than none, because every later choice is measured against it — if it cannot be
> stated, get it stated before producing anything.
> **Where difficulty sits.** During comprehension, difficulty is the enemy: it consumes exactly the
> capacity needed to understand. Where the goal is durable capability rather than a one-off result,
> difficulty is the mechanism: retrieving rather than re-reading, spacing rather than massing, mixing
> related things rather than blocking them. Do not carry the second posture into the first phase.
> **Records are gated on evidence, not exposure.** Write down that something is understood only when it
> has been demonstrated — used correctly, or predicted correctly, or corrected after being wrong. Being
> covered, discussed or agreed is not understanding; write nothing, or write it as still open. When a
> record is later contradicted, mark it superseded rather than deleting it, because how the
> understanding moved is itself information.
> **Carrier follows likely reuse.** Content that will be read once belongs with the work that produced
> it; content that will be returned to belongs where it can be found quickly, compressed to the part
> worth returning to. Decide this from expected reuse, not from where the content was first written.
> **Do not duplicate a reusable.** Before writing a new method or guide, check whether an existing one
> already carries the mechanism; if two would need the same content, it belongs in one place that both
> point at.

Verification plan: (a) on the existing core, check whether any two method or guide files carry the same
mechanism (a duplication census); (b) take one proposed new method and record whether the
read-before-author step changed what was written. Boundary: (a) is a mechanical check of the current
package; (b) tests the authoring rule's effect on one artifact; neither establishes that the rules improve
retention.

---

### DEF-11 · Long-form drafting: grounding, and the shared-document writing rhythm

**1) Mechanism, trigger, anchors, read status**

| | |
| --- | --- |
| Mechanism | Two split jobs. **Explore**: mine raw material with no structure and no commitment. **Exploit**: commit to a path and grow the piece one unit at a time, where every unit may only lean on concepts the reader already has or that an earlier unit established, and each unit's *form* is argued rather than assumed |
| Trigger | A long piece must be written from a pile of raw material |
| Provisional locus | E — with one genuinely general rule about editing a document a human also edits |

Anchors: `writing-fragments/SKILL.md` §What is a fragment (incl. "the leading word is the most valuable
fragment"), §File format, §Writing rhythm (append silently; re-read from disk before every write; never
overwrite; treat "cut the last one / rewrite that one sharper / merge those two" as first-class
instructions); `writing-beats/SKILL.md` §Grounding (prerequisite vs introduced; the unit is the concept
not the word; the running grounded set; the lever in both directions), §What is a beat (with the sizing
test: "If a 'beat' needs five paragraphs and three subheadings, it's not a beat; it's two beats glued
together"), §Pulling from the pile ("The pile is a quarry"), §Ending the journey ("The article ends when
the journey is complete, not when the pile is empty"); `writing-shape/SKILL.md` §The loop (read the pile;
establish prerequisites; 2–3 candidate openings each implying a different thesis with a forced pick;
grow block by block asking "given this opening, what does the reader need to hear next?"), §Conversational
feel (five reusable pushback questions), §Format arguments to actually have (the five trade-offs),
§Writing rhythm, §Out of scope. Read: full.

**2) Operation, conditions of validity, failure modes, counterexamples**

- *The grounding rule is the mechanism's core and it generalises.* Every concept must be grounded before a
  unit leans on it — either the reader arrived knowing it (a **prerequisite**, fixed before the first
  unit) or an earlier unit introduced it. "A block that reaches for an ungrounded concept loses the
  reader." Two operational consequences: keep a running grounded set, and treat an ungrounded concept the
  next move needs as *itself* the answer to "what comes next" — ground it first. The unit is the concept,
  not the word: "a beat can lean on an idea the reader lacks even with no jargon in sight."
- *The lever has two failure directions, both named.* "Demand too much up front and you shut out readers
  who don't have it; ground too much inside and the early beats drown in definitions." That symmetry is
  what makes the rule a trade rather than a checklist, and the falling-back move is stated: when a
  tempting unit requires an ungrounded concept, either ground it first or promote it to a prerequisite.
- *Explore and exploit are separated deliberately, and the separation is what makes each work.*
  Fragments: heterogeneous by design ("a sharp sentence you'd want to deploy somewhere but don't yet know
  where"; "a half-thought"; "a complaint, a confession, a punchline"), readable by the author but
  explicitly **not** required to be comprehensible to a cold reader, with the bar being "is this a piece
  of good writing?" rather than "is this a self-contained argument?" And the model for it: "The novelist's
  diary is the model: years of unstructured noticings that later get mined for raw material." Exploit:
  the pile is read-only, a quarry, not a script; a fragment may be split, merged or paraphrased, because
  "the pile's job is to be mined; the article's job is to read as one voice."
- *The one genuinely general rule: the shared-document rhythm.* For a document a human also edits: append
  only what was agreed rather than batching; **re-read the file from disk before every write** because the
  human may have changed it between turns; never overwrite; and treat edit instructions ("rewrite that
  one", "cut the last one", "merge those two") as first-class commands. This is an artifact-safety
  protocol for human-and-agent co-editing, and it is the group's most transferable item — it is the same
  class of rule as the product's preserve-pre-existing-changes discipline, applied to a live document.
- *Form is argued, not assumed.* Five trade-offs are stated with their criteria: prose vs list (prose
  carries argument, lists carry parallel items — "If items aren't truly parallel, prose is better"); inline
  vs callout (only if it would genuinely derail the main argument inline); table vs repeated structure (the
  same shape three or more times with the same fields); quote vs paraphrase (quote when the wording is the
  point); block vs inline code. And the five pushback questions are reusable as an editing checklist:
  "What does this paragraph do for the reader that the previous one didn't?" / "If I cut this, what
  breaks?" / "Is this prose, or should it be a list? Why prose?" / "This sentence is doing two jobs: split
  it or pick one." / "The opening promised X. We've drifted to Y. Either re-thread it or change the
  opening."
- *Gap naming.* "If the pile lacks something the article needs, name the gap explicitly: 'We need an
  example here and the pile doesn't have one. Give me one now or we cut this section.'" This is the
  honest alternative to inventing material — the same posture as never-invent-the-click-path (DEF-7) and
  no-spec-available (DEF-2).
- *Conditions of validity.* A pile of material and a human willing to make choices. The forced-choice
  design ("Force the user to pick or compose a hybrid") is what prevents the agent from choosing a thesis
  on the human's behalf.
- *Counterexample / out of scope, stated.* Mining for material that is not in the pile; editing the raw
  pile; publishing or platform formatting; adding front matter nobody asked for.

**3) A–F loci and professional concern; Profile and call timing**

- **E** owns the drafting. The *thesis* is a judgment the human owns, which is why the mechanism forces a
  choice instead of making one. Nothing here touches authority.
- Professional concern: *Cost* and *Correctness of communication* (the grounding rule is a correctness
  rule about the reader, not about the content).
- Profile: `profiles/implementation.md` (E) is the closest, with the caveat that this is a different
  deliverable class. The shared-document rhythm maps onto any E instance editing a document a human also
  holds. Call timing: when the deliverable is a long written artifact produced with a human in the loop.

**4) Current product: exact text, what is covered, the residual gap, why**

Covered — the *product's own text* follows rules of this family, and one is worth naming because it shows
the product already accepts the idea: `profiles/behavior-domain.md` §关键问题 asks "现有例子有没有互相
矛盾？" and the Backbone requires conflicts to surface. But nothing in the core governs how a long written
deliverable is produced or co-edited.

Residual gaps — three:
1. **No co-editing protocol.** The product's delivery discipline assumes the instance produces an artifact
   and hands it over. It has no rule for a document a human is editing *while* the instance works on it —
   re-read before every write, append rather than rewrite, treat edit instructions as commands. Given that
   the product's own working materials are written documents that humans review, and given the plan
   expects multiple writers with explicit write-sets, this is a live gap rather than a hypothetical one.
2. **No grounding rule.** "Every claim may lean only on what the reader already has or what an earlier
   part established" is a real quality rule for any produced explanation — including a Charter, a Plan, or
   a method body — and the product has no version of it. It is the reader-side counterpart of ABC MG-8's
   pointer rules, which govern *reachability* rather than *comprehensibility*.
3. **No gap-naming rule.** The family's consistent posture — say what is missing and ask, rather than
   inventing — is already the product's posture in other places (no-spec-available, no-seam-as-finding).
   It is not stated as a general rule for produced text, and it is one sentence.

Why worth absorbing: gap 1 is the substantive one and it is cheap; gaps 2 and 3 are each one clause and
both are the kind of rule that prevents silent degradation of produced text.

**5) Retain / change / delete; carrier; coupling; real-SDK dependency**

- **Retain** the grounding rule with both failure directions and the prerequisite/introduced split; the
  explore/exploit separation with the "readable by the author, not necessarily cold" bar; the read-only
  quarry; gap naming; the forced choice of thesis; the five format trade-offs; the five pushback
  questions; and the co-editing rhythm.
- **Change** the unit names (beat/block/fragment) into the general vocabulary of *unit of the piece*;
  they are useful and not load-bearing.
- **Delete** the file-format specifics (`---` separators, the single H1 rule, `# Working title`) and the
  platform/publishing clauses.
- Carrier: the co-editing rhythm belongs with the Charter's write-set and preserve rules
  (`profiles/driver.md` §关键问题 already asks about write-sets); the grounding and gap-naming rules belong
  as clauses wherever the product governs produced text (so, together with ABC MG-8's material).
- Real SDK/runtime dependency: **none**.

**6) Draft text and verification plan (not executed)**

Draft (candidate clauses):

> **Write for the reader you have.** A statement may lean only on what the reader already has or on what
> an earlier part established; a claim that leans on an unestablished idea loses them, however clear it
> looks to you. Decide up front what the reader arrives with, and hold that line — demand too much of them
> and you exclude them, establish too much inside and the opening drowns in definitions. When the next
> move needs something not yet established, that is the answer to what comes next: establish it first.
> **Say what is missing rather than inventing it.** If the material does not contain what the piece
> needs, name the gap and ask for it, or cut the part that depends on it.
> **When a person is editing the same document.** Add only what was agreed, as it is agreed, rather than
> batching a rewrite at the end. Re-read the document before every write: the person may have changed it
> since you last looked, and their change outranks your recollection. Never overwrite what you did not
> write. Treat instructions to change a specific part as exactly that — change that part and leave the
> rest.

Verification plan: on one co-authored document, record (a) whether any write clobbered a human edit, (b)
whether every added unit could be traced to an established concept, and (c) whether any gap was filled by
invention rather than by asking. Boundary: (a) is a mechanical check on the write protocol; (b) and (c)
test the rules' observance on one document, not the writing quality.

---

### DEF-12 · Making the environment carry the standard: mechanical violations become checks

**1) Mechanism, trigger, anchors, read status**

| | |
| --- | --- |
| Mechanism | After a session, mine what went wrong for **environment** improvements, and apply one discriminating rule: a **mechanical** violation (a fixed syntactic pattern, a banned API, an import shape, a file-location rule) is turned into a **deterministic check**; only genuine **judgement calls** are written as prose standards. Plus: a repository with no guardrail at all is itself a finding, and the check that already exists but is unwired counts as the finding rather than a reinvention |
| Trigger | A session has produced evidence about how the environment made errors possible |
| Provisional locus | D/F — environment design after the fact, with an ownership argument that bears on B/E/F separation |

Anchors: `retro/SKILL.md` §Steps 1–4 (read primary sources; look for candidates in seven categories each
with a *use when* trigger; present ordered by severity), §Implementation vs Review L29–36,
§Files L37–44; `docs/absorption`-side evidence: the source repo's own `changeset retro-deterministic-checks.md`
(recorded in `A3-MATT-ABC.md` §0 as release-note asset) states the same change and its rationale. Read:
full. (Note: the source's own README marks this skill a stub while the body is a complete process — a
discrepancy recorded in the A3 index and not resolved here.)

**2) Operation, conditions of validity, failure modes, counterexamples**

- *The classification rule, with its default.* "Classify the violation first: a **mechanical** one (a fixed
  syntactic pattern, a banned API, an import shape, a file-location rule) gets a deterministic check, full
  stop: a custom rule in the repo's own linter, a new pre-commit hook, or a new CI job, whichever the
  repo's language and existing guardrail make cheapest. **Default to building the check over writing the
  rule.** Reserve `CODING_STANDARDS.md` for genuine **judgement calls** (cross-file consistency, 'matches
  the surrounding style,' anything no guardrail could ever substitute for)."
- *The reader-order rule, which prevents inventing what already exists.* "Read the repo's own check command
  first (its `package.json`/build-tool `lint`/`check` scripts, its CI workflow), so a check that already
  exists but sits unwired or silently broken is the finding, not a reinvention."
- *The no-guardrail finding, stated as a default rather than a demand.* "A repo with no **guardrail** (no
  pre-commit hook and no CI job running its lint/typecheck/test command) is itself a finding: an un-linted
  repo is a standing missed opportunity, not a neutral default." This is a *stance*, and the reason it is
  defensible is that it is the only category where the finding is the absence of a mechanism rather than a
  mistake.
- *The ownership argument, grounded in context economics rather than hierarchy.* "Remember that all work
  goes through two stages: implementation and review. The implementation agent has the most **context
  pressure**. They are responsible for exploration, writing code, and debugging failures. The review agent
  has the least context pressure — it receives a diff, so no exploration needed… This means that the
  **review agent should be responsible for imposing coding standards, not the implementation agent**."
  This is the same load argument as ABC MG-8, applied to *who is asked to hold a rule*.
- *The file-role allocation, which is a concrete instance of the same argument.* The always-loaded
  instruction file "should be used incredibly sparingly, usually only for **navigation pointers** to other
  files"; the standards file "is read during review, not implementation"; docs are pointed at; skills hold
  documentation or user-invoked commands. That is a four-way allocation of the same content under the same
  two-budget model, and it is directly comparable to the product's Profile/method/Charter split.
- *The candidate categories, each with a trigger.* Seven, each carrying a *use when* so the category is
  not applied speculatively: navigation (use when the session took a long time to find something — and a
  "navigation pointer" is the fix); automated checks (a mistake a check could have caught, or no guardrail
  at all); coding standards (the reviewer failed to catch a mistake); the always-loaded instruction file
  (it has grown large); tool economy (an expensive call that could be streamlined); no-ops (instructions
  that do not change behaviour); information access (a crucial piece of information was not available —
  teeing logs, read-only access to third-party services).
- *Conditions of validity.* Access to the session record (the source defaults to the current session)
  and a repository whose check command is discoverable. The "no-ops" category depends on ABC MG-8's
  model-relative no-op test, so it inherits that uncertainty.
- *Failure mode / counterexample.* The rule can be over-applied into writing a check for something that is
  genuinely a judgement call, which is why the classifier is stated as *first*, and why the standards
  document is explicitly reserved rather than eliminated. The source also names the cost of the opposite
  error — a global instruction file grown large — as its own category, so the mechanism polices itself.

**3) A–F loci and professional concern; Profile and call timing**

- **D/F** own the environment change; the *standards* half is the review-side responsibility. The
  ownership argument's product reading is that the **reviewer's** context has room for a rule set and the
  **implementer's** does not — which supports the product's existing separation and gives it a reason it
  does not currently state.
- Professional concern: *Maintainability* and *Delivery risk*; *Correctness* through the check.
- Profile: `profiles/evidence-evaluation.md` (F) for the reviewer-side standards ownership;
  `profiles/driver.md` for the trigger/allocation half. Call timing: after a session, and when a mistake
  recurs — never as a standing gate.

**4) Current product: exact text, what is covered, the residual gap, why**

Covered — the *separation of concerns* is already right and the product states a stronger version of the
independence half. `profiles/evidence-evaluation.md` §心智模型: "独立是真实属性：评价者不得是被评价候选的
实现者… 正常质疑与反例不自动构成作者贡献" and §常见误区 rejects "戴不同帽子" as independence. What the
product does not have is any mechanism for the *environment* itself as a deliverable.

Residual gaps — three:
1. **No mechanism-to-check rule.** The product has no rule that a violation of a fixed pattern should
   become a deterministic check rather than a written instruction. Given the package's stated risk
   (brevity collapsing into abstract principles), this rule is the structural answer to "how do we stop
   relying on prose to hold a line", and it is absent.
2. **No guardrail-absence finding.** Nothing in the core treats "there is no automated check on this
   project at all" as a finding in its own right, and nothing requires reading the existing check command
   before proposing a new one.
3. **No staged ownership of standards, and no statement of *why*.** The product separates B/E/F by
   responsibility; the source adds a second, load-based reason for putting rule-holding on the evaluator
   rather than the implementer. That reason is useful precisely because it is not a hierarchy claim — and
   the product's `charters/template.md` has no field or line that says where a rule set should live
   relative to who holds it.
4. The **file-role allocation** (always-loaded = pointers only; standards read at review; docs pointed at)
   is a directly comparable instance of the product's own two-budget problem, and the product's core
   currently allocates by responsibility without stating the load consequence.

Why worth absorbing: gap 1 is the missing structural remedy for the product's central risk; gap 3 gives
the existing separation a second, non-hierarchical justification; gaps 2 and 4 are cheap.

**5) Retain / change / delete; carrier; coupling; real-SDK dependency**

- **Retain** the classifier with build-the-check-by-default; the reserve-the-standards-document rule; the
  read-the-existing-check-first rule; the no-guardrail finding; the context-pressure ownership argument;
  the file-role allocation; and the categories with their *use when* triggers.
- **Change** the trigger framing: the source runs it as a post-session retrospective, which is one trigger.
  The transferable form is "when a defect or a missed review reveals that a *class* of mistake is possible,
  decide whether the class is mechanical (then make the environment catch it) or a judgement call (then
  write it down)" — usable at the moment the evidence appears, not only afterwards.
- **Delete** the category list's host-specific members (skills as a documentation home, user-invoked
  commands, tool-call economy measured in tokens) while keeping the general idea of each.
- Carrier: a clause set in `profiles/driver.md` (allocation/trigger) plus a short on-demand guide for the
  classifier. The standards-ownership argument belongs in `profiles/evidence-evaluation.md` or the Charter
  template, not in a method.
- Real SDK/runtime dependency: **yes for the check half** — producing a linter rule, a hook or a CI job
  requires the project's real toolchain. The rule itself does not.

**6) Draft text and verification plan (not executed)**

Draft (candidate rule):

> When something goes wrong, ask what in the environment let it go wrong, and classify the answer before
> writing anything. A **mechanical** class — a fixed pattern, a banned construct, an import shape, a
> file that must live somewhere — should be caught by the environment: a lint rule, a pre-commit check, or
> a pipeline job, whichever this project already makes cheapest. Writing it down as an instruction instead
> is the weaker choice, because an instruction competes for attention with everything else and a check does
> not. A **judgement call** — consistency across files, "matches the surrounding style", anything no check
> could decide — cannot be automated, and that is the class the written standards are for.
> Before proposing a new check, read the project's existing check command and its pipeline. A check that
> already exists and is unwired or silently skipping files is the finding; a second check for the same
> class is a cost.
> Where a project has no automated check at all, say so as a finding rather than treating it as neutral.
> Put the rules where the reader has room for them: the implementer is carrying the most context, so the
> reviewer is the one who should hold and apply the standards, and the always-loaded instruction file
> should carry pointers rather than prose.

Verification plan: (a) enumerate the current core's own rule-like statements and classify each as
mechanical or judgement call, recording which have no check behind them; (b) identify any statement that
is mechanical and currently enforced only by prose. Boundary: (a) and (b) are mechanical censuses of the
product's own text, not evidence that checks improve outcomes.

---

### DEF-13 · Guardrails and tooling: prove the check bites, and keep the boundary honest

**1) Mechanism, trigger, anchors, read status**

| | |
| --- | --- |
| Mechanism | Two halves of one idea. When installing a mechanical guardrail, **prove it fails on a violation before trusting it** — a check that has never been seen red is worthless. And be honest about what the guardrail can and cannot stop |
| Trigger | A guardrail (hook, lint rule, dependency boundary) is being installed or relied on |
| Provisional locus | D/E/F |

Anchors: `skills/in-progress/setup-ts-deep-modules/SKILL.md` §4 Wire it into the checks L59–66, §5
Scaffold the example package L67–78, §6 **Prove the rules bite** L79–88, §7 Document the convention L89–96,
§Notes L97–102; `dependency-cruiser.config.cjs` (the four `error` rules, the `$1` back-references, the
commented layering stub, the resolver options); `skills/misc/git-guardrails-claude-code/SKILL.md` §What
Gets Blocked, Steps 1–5 (incl. the merge-don't-overwrite rule and the piped verification expecting exit 2)
+ `scripts/block-dangerous-git.sh` (the nine-regex `DANGEROUS_PATTERNS` array, `grep -qE`, stderr message,
`exit 2`); `skills/misc/setup-pre-commit/SKILL.md` Steps 1–8 (lockfile→package-manager detection; the
staged-first-then-full ordering; adapt-or-omit; commit through the new hooks as the smoke test).
Read: full.

**2) Operation, conditions of validity, failure modes, counterexamples**

- *Prove-the-rules-bite is the flagship mechanism, and it is stated as the completion criterion.* "This is
  the completion criterion for the whole skill: a config that doesn't fail on a violation is worthless."
  The three-step protocol: run it clean and it must pass; introduce a violation (here, a deep import in a
  test) and it must **fail with the specific rule name**; revert and it must pass again. "If step 2 does
  not fail, the rules are not wired correctly, so fix before finishing." This is the negative-control
  discipline of DEF-2/MG-3 transferred to configuration, and it is the single most transferable item in
  this group.
- *The pattern is generalisable to the guardrail's own honest limits, and the source is candid about
  them.* The git hook matches a regex list against the command string: nine patterns for six named
  categories, so the SKILL's list and the script's list are not 1:1; and a regex over a command string is
  bypassable by quoting, aliasing or wrapping. The verification step in the SKILL is a piped test
  invocation expecting a specific exit code and a message on stderr — i.e. the hook is verified the same
  way the boundary rule is. Anyone relying on such a hook as a security boundary would be wrong, and the
  material says enough to see that.
- *Installing a guardrail must not clobber configuration.* "If the settings file already exists, merge the
  hook into the existing `hooks.PreToolUse` array. Don't overwrite other settings." And for an existing
  dependency-boundary config: "If one exists, do **not** overwrite it: merge the four rules and the options
  in, and tell the user what you added."
- *Ordering by cost.* The pre-commit hook runs the staged-only formatter first and then the full typecheck
  and tests — "fast, staged-only" before the expensive full pass.
- *Adapt-or-omit rather than invent.* "If repo has no `typecheck` or `test` script in `package.json`, omit
  those lines and tell the user" — the guardrail is installed to the project's real shape, never a
  hypothetical one. And the absence of an umbrella check command is reported rather than invented
  (paraphrasing DEF-12).
- *The convention is documented where the reader will trip over it.* The boundary rule is written into a
  README beside the code it governs **and** pointed at from the always-loaded instruction file — "This is
  what makes an agent discover the boundary rule instead of tripping over it." That is ABC MG-8's pointer
  rule applied to a guardrail.
- *A structural detail with real value.* The nested-import rules depend on `$1` back-references, and the
  source warns "Don't flatten them into separate per-package rules" — i.e. the guardrail's expressiveness
  comes from a mechanism that is easy to "simplify" into something that no longer holds.
- *Conditions of validity.* A toolchain that supports the check; a runnable clean state to establish the
  passing baseline; and — for the prove-it step — the ability to introduce and revert a violation.
- *Counterexample / misuse.* A guardrail added without the red run is indistinguishable from no guardrail
  while costing the same, which is exactly what the completion criterion exists to prevent.

**3) A–F loci and professional concern; Profile and call timing**

- **D/E** install it; **F** is the category it serves (a mechanical check is evidence-producing
  infrastructure). The installation itself is an E activity inside a delegation.
- Professional concern: *Maintainability*, *Security* (the git hook's intent, with its stated limits), and
  *Correctness* through the boundary rules.
- Profile: `profiles/implementation.md` (E) with a D justification for the boundary. Call timing: when a
  class of mistake has been classified mechanical (DEF-12) — the two groups are one mechanism in two
  halves.

**4) Current product: exact text, what is covered, the residual gap, why**

Covered — nothing. The product's 21 files contain no guardrail-installation method and no rule about
verifying a check. `profiles/technical-planning.md` §关键问题 asks about regression surface and
compatibility, and `methods/cross-module-design.md` §Method 4 owns "Decide which existing checks cover the
new behavior" — a *choice* among checks, not the creation or validation of one.

Residual gaps — three:
1. **No prove-the-check-bites rule.** This is the substantive gap and it is a *verification* rule the
   product is unusually well positioned to state: its three-state verdict discipline already forbids
   turning missing evidence into PASS, and a guardrail that has never been seen failing is exactly
   "missing evidence". Stating the rule costs one sentence and closes a real hole.
2. **No install-without-clobbering rule.** The product's methods create and extend artifacts; nothing says
   that installing a mechanism into an existing configuration must merge and report rather than overwrite.
   Given the plan expects multiple writers with explicit write-sets, this is a live risk.
3. **No documented-limit rule for a guardrail.** A guardrail whose limits are not written down is trusted
   beyond its reach. The source's git hook is the perfect example: a regex over a command string with a
   six-versus-nine mismatch between its description and its implementation is a guardrail whose stated
   scope exceeds its real one. One clause — "state what the guardrail cannot catch" — prevents that.

Why worth absorbing: gap 1 is one sentence and is the configuration-side twin of a discipline the product
already accepts; gaps 2 and 3 are one clause each and both address documented failure modes rather than
hypotheticals.

**5) Retain / change / delete; carrier; coupling; real-SDK dependency**

- **Retain** prove-the-rules-bite as a completion criterion with its pass/fail/pass protocol and its
  stated rationale ("a config that doesn't fail on a violation is worthless"); merge-don't-overwrite with a
  report of what was added; order checks by cost; adapt-or-omit; document the convention beside the code
  and point at it from the always-loaded file; and state the guardrail's limits.
- **Change** the frame from "install a specific tool" to "install a mechanical check": the four boundary
  rules, the hook pattern list and the pre-commit composition are examples, and the boundary rules'
  *expressiveness* (nested/back-referenced rules that resist being flattened into per-item copies) is the
  part worth keeping as a design note.
- **Delete** the tool names and formats (`dependency-cruiser`, husky, lint-staged, Prettier defaults,
  `.cjs`-for-type-module, `pnpm ai-hero-cli`, `@total-typescript/shoehorn`) and the host-specific hook
  file layout. Also drop `migrate-to-shoehorn` and `scaffold-exercises` as mechanisms: their content is a
  single package's API and a private course toolchain respectively — recorded here as screened-and-graded,
  not devalued, so they are not silently dropped.
- Carrier: a short clause set wherever DEF-12 lands (they are one mechanism), plus one on-demand guide if
  the gate wants the installation procedure; the prove-it rule also belongs in
  `methods/behavior-claim-evaluation.md`'s invalidity conditions, since "a check never seen failing" is an
  evidence-validity defect.
- Real SDK/runtime dependency: **yes, fully** — a guardrail is only real once it runs in the project's own
  toolchain, and the red-run proof requires running it.

**6) Draft text and verification plan (not executed)**

Draft (candidate rule):

> A check you have never seen fail is not evidence. Before relying on one — a lint rule, a hook, a
> pipeline job, a dependency boundary — run it on a clean state and confirm it passes, then introduce a
> violation of exactly the kind it exists to catch and confirm it fails, then remove the violation and
> confirm it passes again. If the second step does not fail, the check is not wired to anything you care
> about, and its green result means nothing.
> When installing a check into a project that already has configuration, merge and report rather than
> replace: say what you added and leave everything else as it was. Adapt to what the project already has —
> if there is no script to run, say so rather than inventing one.
> Write down what the check cannot catch. A guardrail described more broadly than it operates is worse than
> no guardrail, because it buys confidence it does not provide.

Verification plan: take one existing mechanical rule from the product's own text (DEF-12's census output)
and apply the pass/fail/pass protocol against a real toolchain. Boundary: this tests the protocol on one
check; it does not establish that the check is worth its maintenance cost.

---

### DEF-14 · Repo tooling patterns: non-mutating drift checks and refuses-when-the-target-is-wrong

**1) Mechanism, trigger, anchors, read status**

| | |
| --- | --- |
| Mechanism | Two small, reusable script patterns. (A) A **drift check that does not mutate**: a flag mode that changes nothing, reports the divergence, and exits non-zero, with a minimal-target write that preserves formatting when it does fix. (B) A script that **refuses to run when its destination turns out to be something other than expected**, rather than writing into the wrong place |
| Trigger | Two generated or duplicated artifacts must stay consistent; or a script writes into a location that might be a link back to its own source |
| Provisional locus | E |

Anchors: `scripts/sync-plugin-version.mjs` (whole: `--check` exits 1 without writing; rewrites only the
version line "to keep the key order and the formatting"; fails loudly if the field cannot be replaced);
`scripts/link-skills.sh` (whole: the per-item symlink loop, the comment that a `git pull` is what keeps
installs current, the destination-is-a-symlink-into-this-repo guard that errors and exits rather than
populating the repo tree, and the bucket exclusions with their stated reasons). Read: full.

**2) Operation, conditions of validity, failure modes, counterexamples**

- *(A) The check mode.* Two artifacts carry the same fact (a package version and a plugin manifest's
  version), one is authoritative, and the script either writes or — under `--check` — reports and exits 1
  without touching anything. The write path is deliberately minimal: a single regex that replaces only
  the version value, with the stated reason "to keep the key order and the formatting", followed by a
  verification that re-parses the result and fails if the replacement did not happen. That last step is a
  *post-write assertion*, which is the cheap version of DEF-13's prove-it rule.
- *(B) The refuse-when-wrong guard.* The script symlinks each item into two destination directories, and
  before doing so it checks whether a destination is itself a symlink resolving into the repository; if so
  it errors and exits with an instruction, rather than creating links back into the repo's own tree. The
  comment states the hazard plainly: "we'd end up writing the per-skill symlinks back into the repo's own
  skills/ tree. Detect and bail out instead of polluting the working copy."
- *Exclusions with reasons.* The script skips two buckets and keeps a third, and the comment gives the
  reason for each — including the case where the "obviously safe" choice would be wrong ("`in-progress/`
  IS still linked: it's public on purpose, feedback wanted, and this local install is exactly where that
  feedback loop runs"). That is a working example of the product's own "state the exception's reason"
  discipline.
- *Conditions of validity.* (A) an authoritative source for the fact and a second consumer; (B) the
  script's destination being knowable at run time — which is precisely what the guard establishes.
- *Failure mode both patterns address.* Silent success: a drift check that silently rewrites hides the
  fact that the two had diverged; a link script without the guard silently populates the wrong tree. Both
  patterns exist so the failure is *loud*.
- *Counterexample / limit.* (A) is only as good as the fact being single-sourced; if three artifacts carry
  the version, a pairwise checker still leaves a gap. Worth stating: the pattern reduces a drift class, it
  does not eliminate it.

**3) A–F loci and professional concern; Profile and call timing**

- **E** owns tooling. (A) produces evidence about consistency, so an F-flavoured consumer can cite it.
- Professional concern: *Maintainability*; *Correctness* of generated artifacts.
- Profile: `profiles/implementation.md` (E). Call timing: when a duplicated fact or a generated artifact
  exists.

**4) Current product: exact text, what is covered, the residual gap, why**

Covered — the product has the *single-source discipline* and even the projection pattern with a matching
digest: `authority/README.md` states the export "is an exact static projection of the frozen design
baseline… Do not edit the projection as a second responsibility definition; change the accepted source
first and regenerate the export only when a new source version is accepted", and it records both digests
so byte identity is checkable. That is *stronger* than the source's pairwise version sync.

Residual gaps — two, both small:
1. **No non-mutating check mode.** The product's projection rule says "regenerate … only when a new source
   version is accepted", and nothing provides or requires a way to *detect* divergence without
   regenerating. Given that the package's central invariant is digest-matching between a source and an
   export, a check-only path ("report divergence, change nothing, exit non-zero") is the operational
   complement to the rule, and it is absent.
2. **No refuse-when-the-target-is-wrong rule.** The product's instructions occasionally write into
   locations; nothing requires a script or an instance to verify that its destination is what it thinks
   before writing. The source's guard is a concrete model.

Both are minor; recorded for completeness because the accounting requires the paths to resolve, and
because if the gate takes DEF-13's guardrail-installation material these two belong with it rather than as
a separate proposal.

**5) Retain / change / delete; carrier; coupling; real-SDK dependency**

- **Retain** (A) the non-mutating check mode with a non-zero exit, the minimal-target write preserving
  formatting, and the post-write assertion; (B) the destination guard with a clear error and no write, and
  the exclusions-with-reasons pattern.
- **Change** nothing structurally; both are already carrier-neutral.
- **Delete** the specific paths and bucket names.
- Carrier: if adopted, one clause in whatever guardrail/tooling material the gate accepts (DEF-12/13),
  with the projection rule in `authority/README.md` cited as the rule the check serves. Not worth a method
  file on its own.
- Real SDK/runtime dependency: **yes** — both patterns are executed tools.

**6) Draft text and verification plan (not executed)**

Draft (candidate clause):

> Where two artifacts must carry the same fact, one of them owns it; the other is generated, and the
> generator has a mode that reports divergence without changing anything and fails loudly. When it does
> write, it changes only the value and leaves the surrounding file alone, then re-reads the result to
> confirm the change actually took. Before writing anywhere, confirm the destination is what it appears to
> be: a destination that turns out to be a link back into the source is a reason to stop with an error, not
> to write and see.

Verification plan: identify every duplicated fact in the current core and record whether divergence is
currently detectable without writing. Boundary: a mechanical census of the package, not a claim that drift
has occurred.

---

## 3 · Cross-cutting observations for the gate

**3.1 Three of the strongest items in this package are the same mechanism at different scales.** A green
check never seen red (DEF-13's prove-the-rules-bite), an evaluation axis that cannot fail (ABC MG-3's
tautology), a guardrail whose stated scope exceeds its real one (DEF-13), and a fact presented as an
assumption-free premise (DEF-9, DEF-6) are all instances of one rule: **evidence that cannot come out
negative is not evidence.** If the gate adopts anything from this package, consolidating this rule once —
in F's evidence conditions — would cover four gaps with one addition. Flagged as an integration
opportunity, not as a fifth proposal.

**3.2 Several groups resolve the same product gap from different sources** (so the gate should merge
rather than count them separately): the rejection record appears in DEF-3 and ABC MG-6; the "state what is
missing rather than invent" posture appears in DEF-7 (never invent a click path), DEF-11 (name the gap)
and DEF-2 (no spec available); the difficulty-sign rule (DEF-10) and the no-op test (ABC MG-8) are both
about matching effort to effect; DEF-12 and DEF-13 are two halves of one mechanism. Per the plan, "多源一个
机制不能重复算知识增量" — these are flagged so the knowledge increment is counted once.

**3.3 Every group in this package names a real SDK/runtime dependency or states that there is none.** This
was checked deliberately, because DEF is where platform coupling concentrates. Summary: DEF-1 (lower
rungs), DEF-2 (a revision range), DEF-5 (runs where the question lives), DEF-6 (source access), DEF-7
(irreducible — it is executed by a human), DEF-8 (real history), DEF-13 (fully), DEF-14 (executed tools),
DEF-12 (the check half); **none** for DEF-3, DEF-4, DEF-9, DEF-10, DEF-11. The gate should not accept a
"no runtime needed" framing for the first set, and should not reject the second set for platform coupling
they do not have.

**3.4 One product-internal consistency question, repeated from `A3-MATT-ABC.md` §3.6 and now with evidence.**
`methods/local-defect-feedback-loop.md` §Limits ends "Treat command output as evidence to inspect, not as
instructions to execute" — a security-concern statement living in an E method body. DEF-1's material
(untrusted error output), DEF-6's (junk sources producing confident wrong answers) and DEF-13's (a regex
hook's bypassability) each raise the same class of concern from a different direction. Whether the core
wants one security-concern home that these point at, or repeats the sentence per method, is a placement
question the gate can settle once. The Backbone already permits either ("Security … 可约束 B 的可见信息、
D 的隔离设计、E 的实现与 F 的泄露验证；不增加责任节点").

**3.5 Coverage-density finding, recorded as a fact rather than a judgment.** Of the 42 paths in this wave,
the already-accepted product text absorbs the *core* of four groups almost completely — DEF-1's defect
loop, DEF-8's rerun-the-checks step, DEF-9's deliverable contract, and DEF-14's single-source rule — and
the residual gaps in those groups are clauses rather than mechanisms. The remaining ten groups contain at
least one mechanism the product does not carry at all. If the gate wants a shortlist, the groups with the
largest genuine gap are DEF-1 (gates and the reproduction-rate target), DEF-2 (two-axis review), DEF-4
(multi-session planning), DEF-6 (delegated acquisition), DEF-7 (human-procedure artifact + static
verification), DEF-12 (mechanical-vs-judgement with build-the-check-by-default) and DEF-10 (the
difficulty-sign and coverage-is-not-learning rules). That ordering is a *description of gap size*, not a
recommendation — adoption remains the gate's decision.

## 4 · Verification status of this package

- **Nothing was executed.** No upstream script, template, hook, config or test was run; no product file was
  modified; no commit was made. Every verification plan above is a proposal, and no mechanism here is
  asserted to work.
- **Every quoted line was read at the pin in this session**, and anchors in §2 were checked against the
  files. The one cross-wave citation check performed earlier (`guide-redacted-evidence.md`'s ranges, all
  accurate; `guide-mock-adapter-choice.md`'s `§Designing for testability` range, narrower than its section
  title) is recorded in `A3-MATT-ABC.md` §3.1–3.2 and is not repeated here.
- **Field reports are attributed, not verified.** The 50-plus-agent review fan-out, the 450k-token
  duplicated delegation, the 27-item map that stopped making sense, the fabricated cube moves, the 33/33
  answer position, the CDN-blocked report and the rest are reported **as the upstream docs pages report
  them**, used as failure-mode evidence only.
- **Two source-vs-source discrepancies are recorded, not resolved.** The source repo's README labels
  `retro` a stub while its body is a complete process (DEF-12); its `SKILL.md` frontmatter still advertises
  "red-green-refactor" while the body documents a two-phase loop (`A3-MATT-ABC.md` §MG-1). Both are
  upstream-internal and inherited as recorded, not as judgments.
- **Known uncertainty carried forward:** DEF-1's ladder presupposes a runtime that some fixtures will not
  have; DEF-2's two axes are unvalidated as a pair; DEF-3's survey mode may be a capability the product
  deliberately does not want; DEF-4's carrier question is genuinely open (the source itself documents the
  accidental-persistence failure of one answer); DEF-6 inherits an ungated notion of source quality; DEF-7
  cannot be verified by its author end to end; DEF-10's rules are proposed as clauses, not as a new
  capability; DEF-12's no-op category inherits ABC MG-8's model-relative uncertainty.
