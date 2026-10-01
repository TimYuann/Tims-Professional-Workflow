# Upstream deep-absorption plan · A path→mechanism accounting + B mechanism-level coverage & verdicts

**State:** revised once per Oracle read-back of `e6bb40f` and the Owner's latest clarification (mechanism-level coverage is the main axis; scoring was only an example). Planning only: no 1240 scan, no absorption, no product/core change, no crew dispatch, no fetch/install, no Pro. Baseline: main `e6bb40fe63bd7afb42e69554f0a82acdff7438d6`, core `91875114e51855517f92ef099cbdf60c34e68243`.
**Terminology note:** `A`/`B` are this phase's deliverable labels (path accounting vs mechanism coverage/adjudication), not Backbone A–F judgment classes; A–F are a reference and not an execution order.

## 1 · Fixed inputs and denominator

- Three repos read-only at pins: `addyosmani-agent-skills` `2686b620…`; `cursor-plugins` `ecc249f1…`; `mattpocock-skills` `c55ee460…`. Locator root: `.worktrees/legacy-pre-night-2026-10-01/upstreams/`. Articles are excluded from this denominator.
- **Denominator is rebuilt from the fixed Git pins** (`git ls-tree -r <pin>` direct; if `ls-files` is used, first show HEAD/index equal the pin; verified today: 208 + 863 + 169 = **1240**). No second 1240 list file is required: the final index is the single per-path record, and its header records each repo pin, per-repo count and listing digest — that is what "frozen baseline" means. Reconciliation failure is the only case that opens a separate listing.
- Composite key = **repo + path**; every path is accounted once even when content identity is shared. Assets, scripts and binary files are accounted too, without inventing a read depth and without devaluing them by extension or packaging label.

## 2 · A · per-path screen: source mechanism / responsibility loci / related materials

- Record per path: repo+path; actual read depth (metadata / structure / full); file nature; the **source mechanism(s)** the path carries; **multi-label responsibility loci** (Backbone A–F as reference only); related materials (support files, duplicate content, group); uncertainties; re-query entry.
- The screen is coverage-oriented, not score-oriented: no per-file total score, no high/medium/low as a primary filter or adopt/reject signal. If a reading order is kept, it is an ordering aid only and never a veto.
- A produces no coverage verdict and no adoption decision.
- Write boundary: index documents under `docs/overnight/2026-10-01/` at fixed paths; no product/core, no upstream, no B documents.

## 3 · B · mechanism-level coverage assessment and adoption verdicts (two separate meanings)

- For each **mechanism** (grouped from A's mapped loci): responsibility position; current-text basis (file + paragraph/section); **coverage state = covered / partially covered / not covered / pending-check**; what is missing in judgments / operations / conditions / counterexamples / examples; related support materials; uncertainties.
- Coverage is judged against the current text as it is: a mentioned term is **not** engineering-operation-usable coverage; a missing current method is a **gap lead**, not a low score.
- With no established weighting standard, **do not fabricate coverage percentages** over skills or mechanisms: report counts per state (per mechanism and per source group). Skill-level entries may carry aggregated summaries only where the mechanism mapping is already explicit.
- **Adoption verdicts are a separate track from coverage**: covered does not imply adopt; zero coverage does not automatically imply adopt; adopt / narrow / re-frame / replace / reject / defer each need the substantive reasons, full-read basis and counterexample/condition detail of §5.
- B independently re-reads originals and support files before/independently of A's screen; B is not the A author; no self-PASS.
- Write boundary: adjudication documents at fixed paths; no rewriting of A's records (screen deviations are annotated in B's own documents).

## 4 · Accounting vs assessment completion, tails and closure

- Two completion statements are reported **separately** and neither stands for the other: (1) path accounting 100% (every baseline path has an index record); (2) substantive coverage assessment completion, counted only from **confirmed** states (covered / partially covered / not covered, each with basis). Neither implies adoption.
- `pending-check` is an honest phase result: it keeps what is missing and the reason, but it is **not** counted as a confirmed coverage state and does not increment the assessment-completion count. `not-yet-judged` likewise does not count as closed.
- Reports list these buckets separately: confirmed covered / partially covered / not covered; pending-check; not-assessed. A report may not claim substantive coverage assessment complete merely because every row carries a label.
- If the phase is actively stopped, it is delivered as a phase result with residuals or an explicit deferral — never as "pending closed".
- Group-level non-method or deferral dispositions must state scope reasons, in-group exceptions, related text and exclusion reasons; a group cannot be left entirely unjudged while "full assessment closed" is claimed.
- Coverage-task closure means every baseline path is accounted in a mechanism group; **assessment closure is the confirmed-state count only**. Any group left pending keeps its missing list, reason and an owner-facing re-query entry. No fabricated percentage; counts per state.

## 5 · Calibration and actual adoption

- **Calibration:** a small cross-source, cross-type sample (12–18 suggested; not a hard N or an Owner gate) including hidden support-file techniques, duplicates, platform wrappers, items overlapping existing coverage, and low/undetermined items. B reads the originals first, then compares A's screen for anchoring, missed mechanism leads, classification drift and detail loss. Systematic bias → fix criteria and re-check only affected groups; no full invalidation, no third standing gate. The result is a bounded checkpoint visible to Driver/method, not a permission layer.
- **Adoption requires** a full read of the relevant original plus support files, a record of what is kept / changed / deleted and why, the current-content difference and the landing position; effectiveness claims need corresponding use evidence.
- Mechanism detail may extend an existing method or propose a new method, professional guide or counterexample library; **do not strip professional detail to avoid gates** (e.g., idempotency keeps intent/attempt, atomic claim, same-key-different-payload, in-flight duplicates, unknown outcome, retention causality).
- Changes to existing methods follow accepted retain/narrow/strip discipline with affected-claim revalidation only.
- Flash resources are sufficient; full-file coverage is not traded away to save tokens.

## 6 · Owner decision points (the only ones that remain)

1. **Whether this phase starts** (A/B with the pinned baseline and the boundaries above).
2. **Whether the deliverable is coverage/verdict candidates only, or also a bounded landing authorization.** Without that authorization, coverage and verdicts cannot be implemented.
3. If the Owner grants a landing envelope as a whole, later batches inside it do not re-ask per batch by default.
Composition, ordinary docs/TSV write surfaces and the calibration checkpoint are Driver/Oracle-managed inside the phase; no per-item Owner ACK is required.

## 7 · Relation to earlier practice

Earlier, one survey with reading-depth labels and one dossier fed a single method review, leaving coverage implicit. Now: (a) A owns exhaustive **path→mechanism accounting** with no verdict or veto authority; (b) B owns independent **mechanism-level coverage assessment** and, separately, adoption verdicts; (c) accounting completion and assessment completion are separate reports; (d) a small calibration checks the screen before scale; (e) implementation waits for the Owner's landing envelope. No scoring system, no registry platform, no extra permanent gate.
