# M3 case 2 · Technical Plan (D)

**Status:** candidate Plan, pre-challenge. Not yet implemented. Not an acceptance of B/C, not an implementation authorization beyond the cited delegation.
- **Plan owner / decision responsibility:** `tpw-night-m3-design` (D instance for this exercise).
- **Delegation:** `D-CHARTER.md` (`sha256 6a0e6b7da8f8861e5d37c4d242b7df473e3ede1ffa531e5c73edd92e2730609f`) — Owner-authorized offline exercise in `docs/OVERNIGHT-WORKFLOW-PLAN-2026-10-01.md`, fixed M3 plan baseline `496b0676e302e2d0eafba129ff61de4c203d258a`. Task input: `D-PLAN-INPUT.md` (`sha256 89b131138ead556a3f6ac46ab758237c230c8cb6b615a9af57c92238fb4b7374`).
- **Date:** 2026-10-01 · **Object scope:** this fixture directory only.

## 0. Inputs and verified version binding

All bindings the B/C conditional acceptance depends on were recomputed and **matched**. One cited binding did not resolve to the text in hand; it is a bookkeeping discrepancy in a *reference* document, is fully characterized in §0.2, and is reported rather than silently absorbed. Per B/C §Conditions a mismatch on the first five rows would have voided acceptance and stopped this Plan; none occurred.

### 0.1 Verified bindings

| Input | Role / decision owner | sha256 (recomputed) | Result |
| --- | --- | --- | --- |
| `BEHAVIOR-CONTRACT.md` v1 | accepted behavior; owner `tpw-night-m3-bc` | `86dd6664b73de07ceefdbc5f4d03e09f49b4b1f2ee11cb6a80e48c251176555c` | match |
| `DOMAIN-SEMANTICS.md` v1 | accepted meaning/invariants; owner `tpw-night-m3-bc` | `15537d71d100dde30075f724c1ef79bc0d4e6a76a179f7f82d7f6c6b286cda06` | match |
| `CASE-INPUT.md` | B/C authoring input (acceptance condition) | `50063486b149fc599464cb5cb25872cc9b4c4b971d1fcbc2eab0efdabeffd772` | match |
| `BC-CHARTER.md` | B/C delegation (acceptance condition) | `1395a01731f1ea4885b2e20c157ec47ba607e27fe8e2037006287562d3dd57ba` | match |
| fixture source (`src/**`, `tests/**`) aggregate | recorded seed structure (acceptance condition) | `dbd6a306815bdc4cf3a33be14b38d4dd62b49d1535d7db41b9064eb07e51b474` | match (all 7 per-file digests also match) |
| `RESPONSIBILITY-BACKBONE.md` | authority export cited by the Charter | `ce82a70016a4a3fc234ea287f39aac8d79a260ddf13747c4fb705bda580453ba` | match |
| `profiles/technical-planning.md` | Plan profile cited by the Charter | `d53da06edc99af3bcfc93c744af5f2cc8d512430d318a8b13b1b7f42652d74aa` | match |
| `D-STARTUP-PROMPT.md` | this task's startup input | `0f6d0e4e028543676273b33c1d0c74e5d933da2ed033be3f9669ca83ac748c90` | match |
| `D-CHARTER.md` / `D-PLAN-INPUT.md` | delegation / task input | `6a0e6b7da8f8861e5d37c4d242b7df473e3ede1ffa531e5c73edd92e2730609f` / `89b131138ead556a3f6ac46ab758237c230c8cb6b615a9af57c92238fb4b7374` | read, cited above |

Aggregate recipe confirmed as stated: sort `<per-file sha256><two spaces><path>` lines, join with `\n`, append a final `\n`, sha256 the UTF-8 text. **Reproducibility note:** a locale-sensitive `sort` yields a *different* aggregate (`9074f27d…`); use byte-order (ASCII) collation, under which the cited `dbd6a306…` reproduces exactly.

The B, C, `BASELINE.md` and `README.md` sections **embedded** in `D-STARTUP-PROMPT.md` were compared byte-for-byte against the corresponding files: all four are byte-identical, so the accepted text this Plan reasons over is the accepted text on disk. The embedded Backbone export is likewise byte-identical to `RESPONSIBILITY-BACKBONE.md`.

### 0.2 Finding — the method citation does not resolve to the text supplied (reported, non-substantive)

The Charter cites the applicable method as `methods/cross-module-design.md` "from accepted M4 commit `013659331c8c5f9f54b866b393972a03d7938773` (SHA-256 `30066c8b…`)". Three distinct revisions are in play:

| Revision | sha256 | Self-declared title / status |
| --- | --- | --- |
| file at cited M4 commit `0136593` | `30066c8b3ccee2b85e98c8bc36975f57161e2c93d0bd71c9c668b27bf79bae6f` | "M4 **candidate**"; status: "candidate for the isolated M3 path" |
| **method text actually embedded in the startup input** | `59e686d0a7e488e9c7ae3eb85090da947ad7ac6a68d2feea1b007e4f6ba1456c` | "M4 **accepted reference**" |
| current working tree (moved on by commit `1382b3f`) | `ab0a0bc03448407479fe82b92b2355384e7f2acf49c2ff3026882670f955a0a5` | "M4 **accepted reference**" |

Observations, stated as facts and not resolved by D:

- The cited hash `30066c8b…` is the genuine blob at the cited commit, so the citation is internally consistent — **but that revision declares itself a candidate, not accepted**, so the Charter's word "accepted" does not match the artifact's own status at the revision it names.
- The text I actually applied is neither of those: it is the embedded copy `59e686d0…`, which matches the current tree except for one sentence and differs from the cited revision on its title line, its `Status:` line, and that sentence.
- **The discrepancy is bookkeeping, not substance.** The normative body — `## Use`, `## Method` steps 1–6, `## Limits` — is byte-identical across all three revisions (`sha256 e68e8d983ec675ce4fa4d6dea625987c94c7c14dc1e8521500203ae373ba42b9`). Only the title, the `Status:` metadata, and the trailing `DESIGN-IT-TWICE` deferral sentence differ, and in all three the rule is *deferred*. **No method step, limit, or source anchor I relied on differs.**
- Consequence: this Plan's method binding is **approximate and must be re-confirmed by the method reference's owner**; no step of this Plan rests on the divergent metadata. D does not own this reference and does not resolve it (see R-9). The other frozen design inputs are unaffected and are byte-exact.

The method text applied (whichever of the three revisions) constrains *how* this Plan is written; it does not select B/C meanings and does not enlarge delegated authority.

## 1. Observed system facts (evidence, not prescription)

All of the following is from reading the actual fixture files and from a read-only in-process probe (`PYTHONDONTWRITEBYTECODE=1`; no file written, no test added).

**1.1 Structure.** `StateStore` holds `_current: StateView`; `StateView(revision, cases)` and `CaseRecord(case_id, status)` are frozen dataclasses with a `tuple[CaseRecord, ...]`. `page_summary.build_page_summary(store)` resolves `current_view()` once and returns a fresh `dict` carrying `revision` and `open_count`. `case_reader.read_cases(store)` resolves `current_view()` **again** and returns the case tuple. `turn.begin_turn` wraps the summary; `service.start` / `service.cases` are thin compositions.

**1.2 Enabling fact — the snapshot is a sound coherence unit.** `update_status` never mutates: it rebuilds the tuple and **rebinds** `self._current` to a new `StateView`. The old view therefore never changes. Observed:

```
captured view stable under later update?: True  [('C-1','CLOSED'),('C-2','OPEN')] -> [('C-1','CLOSED'),('C-2','OPEN')]
```

So a single captured `StateView` pins revision *and* statuses together, and holding it is sufficient to satisfy DS-I1/DS-I2 by construction.

**1.3 The defect — two independent resolutions of one presented view.** Each individual read is self-consistent; nothing binds them. Reproduced on the unmodified seed:

```
overview            : {'revision': 1, 'open_count': 2}
details             : [('C-1', 'CLOSED'), ('C-2', 'OPEN')]
store revision now  : 2
open count in details: 1
B-1/DS-I2 count-faithful?  False
B-6(a)/(b) violation?      True
```

This is exactly B's negative control X-2 illegal outcome. The cause is localized: `page_summary` and `case_reader` each call `store.current_view()` separately, so a completed update between the two calls yields a revision-1 overview with revision-2 details.

**1.4 Already-conformant behavior (do not "fix").** `open_count` counts exactly `status == "OPEN"` and is derived from the same view whose revision it reports, so DS-I2 holds *within* the overview. `update_status` preserves case order and, for an absent id, leaves every status unchanged (DS-I7). Revision always advances on update — legal under DS-I4 (revision may change with unchanged data) and DS-U2. Empty case set: `{'revision': 1, 'open_count': 0}` with empty details, per X-6. The existing suite passes 3/3, matching `BASELINE.md`.

**1.5 Coverage gap.** The three existing checks cover the module operations only. None asserts coherence spanning the overview/details pair — `BASELINE.md` says so and the test file confirms it.

## 2. Commitments — what others must rely on

Each commitment is a coordination surface: changing it forces a dependent to change semantics, interface, constraint or verification basis. Basis and owner are cited. **D does not acquire B/C's decision authority by writing these.**

- **C-1 · One resolution per presented view.** Every presented view is derived from **exactly one** resolution of `StateStore.current_view()`. The overview's `revision` is that view's revision; the details are that view's cases; `open_count` is computed from that same view's statuses. *Basis:* B-1, B-6(a)(b); DS-I1, DS-I2. *Owner of the requirement:* B/C (`tpw-night-m3-bc`). *Forbids:* pairing an overview and details produced by two separate reads.

- **C-2 · Coherence is structural, not reconciled after the fact.** Coherence must hold by construction of the pair. A design that re-reads details and validates them against a known revision — without re-deriving the overview from the same resolution — cannot satisfy B-1, because the already-obtained overview would still belong to the other revision. *Basis:* B-1 with X-2; DS-I1. *Consequence:* the binding unit is the **pair**, not a single read.

- **C-3 · Episode policy is pinned (B-O1 resolved).** An episode resolves its view at its start and reuses it; no mid-episode refresh, no visible-refresh signal. Freshness at episode start is therefore automatic: the view current at start already includes every update completed before the episode began. *Basis:* B-O1 delegates this choice to D; P-1 permits pinning; DS-I3/I5. *Owner of the choice:* D (this Plan). *A weaker alternative is also legal* (switching to a newer revision mid-episode, P-1) — noted at U-4 as an open preference question, not offered as a second policy in this Plan.

- **C-4 · Published views are immutable.** `update_status` must continue to publish a **new** `StateView` and must not mutate a previously published one; `CaseRecord`/`StateView` statuses must remain value-immutable for the lifetime of any pinned view. This is what makes C-3 sound; breaking it fails silently. *Basis:* observed 1.2; DS-I4. *Basis for the constraint:* the pin depends on it, so it is a coordination surface, not an interior choice.

- **C-5 · Observations are values, not live aliases.** The overview and details a caller receives must be immutable or freshly copied, so a pinned presented view cannot change after an update. *Basis:* DS-I1/I2 must hold at presentation time, not merely at read time. *Current code already satisfies this* (fresh `dict`, tuple of frozen records) — preserve it.

- **C-6 · Count rule unchanged.** `open_count` counts exactly `status == "OPEN"`; a case is open iff its status is exactly `OPEN`. Do not add handling, validation, normalization or inference for other labels. *Basis:* C §Terms (open), DS-I2, DS-U1 (undefined; **no authority in this fixture to rule**). *Forbids:* resolving DS-U1 as a side effect of implementation.

- **C-7 · Case order and membership unchanged.** Preserve presented order; do not sort, dedupe or add cases. *Basis:* C §Terms (case set "in the presented order"; two views identical iff same ids in same order with same statuses), DS-I7. Duplicate ids remain outside the contract.

- **C-8 · Compatibility is additive.** Existing call forms `service.start(store) -> Turn` with `page_summary["revision"]`/`["open_count"]`, and `service.cases(store) -> tuple[CaseRecord, ...]`, remain callable with a bare `StateStore` and keep their current results when no update interleaves. The three existing checks stay passing and are **not** deleted or weakened. *Basis:* method step 6 (prefer additive when consumers must remain compatible); DS-U3 notwithstanding, `tests/test_existing_behavior.py` asserts a fresh store starts at revision 1 and one update makes it 2 — so keep start 1 / step 1. *Owner of the compatibility requirement:* D; the coverage itself belongs to the fixture's recorded structure.

- **C-9 · Deterministic, in-process, no new resources.** The coherence mechanism must be exercisable in-process against a bare `StateStore`: no clock, thread, sleep, I/O, retry loop, locking or persistence. *Basis:* method step 3 (seam for the actual dependency shape: in-process, locally replaceable, no true external dependency) and B-6's need for deterministic observation.

- **C-10 · No new observable behavior.** The change adds nothing beyond B-1…B-6. No new exceptions for in-contract inputs, no logging contract, no error semantics beyond what exists, no membership/persistence/concurrency features. *Basis:* B's scope; DS-U4 / B-O2 (outside the exercise); Charter "do not select new product behavior".

- **C-11 · No performance or ordering commitment is added.** No latency, throughput, buffering or ordering guarantee beyond the coherence relation itself; no performance characteristic of this interface becomes something a caller may rely on. *Basis:* method step 2 asks for "relevant performance characteristics" — here the honest answer is that none is relevant to the accepted claims, and inventing one would enlarge the objective.

## 3. Delegated Decisions — E's autonomy (implementation interior)

Changing any of these does not force a dependent to change semantics, interface, constraint or verification basis, provided §2 holds. Method step 5/general rule: planner preference alone is not a reason to fix them.

- **D-1 · The carrier shape for a coherent pair.** Whether this is a single producer returning overview and details together, an episode/handle object created at open, an optional revision or pin argument with a store-only fallback, or a pin stored on `StateStore`. Naming and module placement are also E's. *Constraint:* C-1, C-2, C-8, C-9. *Explicitly not prescribed* — `D-PLAN-INPUT.md` states it intentionally does not prescribe module ownership or a token/argument shape, and I am not inventing one.
- **D-2 · Whether the pin is materialized or implicit**, i.e. a stored `StateView` reference versus producing the pair within one call so no separate pin exists. Same constraints.
- **D-3 · Reuse `Turn` as the carrier or add another**, provided `turn.Turn.page_summary` keeps its two keys and meaning (C-8) and the addition is additive.
- **D-4 · `DS-U2` — revision advance on a no-op update.** The seed advances the revision even when the named id is absent. Keeping or changing this is E's, since C leaves it unconstrained and B's X-5 permits either. *Constraint:* DS-I4 must hold, C-8 must hold, C-10 applies.
- **D-5 · Where the episode boundary is drawn in a fixture with no viewer/session object.** B defines the episode from opening the view to the next user action; the fixture has no such object. E may model it as exactly one pair-producing call, or as an explicit open step. *Constraint:* the resolution point must be well-defined and atomic with respect to updates — in this single-threaded fixture, inside one Python call, with no yielding between resolving the view and publishing the pin. A lazy resolution is acceptable only if a presented view never resolves twice (C-1).
- **D-6 · Local types, refactors, and the structure of new tests**, consistent with the existing `unittest` style and with C-9.

## 4. Recall Conditions — when to come back

Return through Driver to the cited authority. Do not silently resolve any of these.

- **R-1 · B/C change.** Any need to alter, reinterpret or extend an accepted B/C meaning, or any finding that a B/C input conflicts: name the affected accepted object, the observed fact and the impact → Driver → `tpw-night-m3-bc`. D does not decide it.
- **R-2 · Acceptance basis broken.** Any change to `CASE-INPUT.md`, the recorded seed structure, or `BC-CHARTER.md` invalidates B/C acceptance per its own §Conditions → new B/C version required → Driver → B/C owner. (Not triggered: all bindings verified, §0.)
- **R-3 · Undefined semantics pressed into service.** DS-U1 (other status labels), or DS-U2/DS-U3 if a choice there would change an accepted claim or the accepted coverage → C owner.
- **R-4 · Coordination surface must change.** If coherence cannot be achieved without changing `StateView`/`CaseRecord` immutability, view publication semantics, or the revision's identity/ordering relations → back to D (this Plan). This is a surface change, not an interior one.
- **R-5 · Accepted coverage must be replaced.** If implementation cannot proceed without deleting or weakening one of the three existing checks → back to D; the method grants no deletion authority, and C-8 forbids it.
- **R-6 · Out-of-scope capabilities requested.** Persistence across restarts, concurrent viewers, case-set membership changes, multi-store comparison, deployment or migration → B-O2 / DS-U4: outside the exercise, **requires a new B version**; and any of these is in any case outside this Plan's and this fixture's action authorization. Do not implement.
- **R-7 · Safety/cost/professional concern appears.** None is in scope here (no persistence, no shared state, no external effect, no budget). If one appears — for example someone proposes sharing the store across viewers or persisting it — D cannot rule on it: route via Driver to the relevant professional responsibility; human-reserved items only via Voice.
- **R-8 · Challenge finding.** `tpw-night-method`'s independent challenge returns findings to the D owner for decision or revision; the challenger is neither author nor acceptor of this Plan.
- **R-9 · Method reference binding unresolved** (§0.2). If the method reference's owner confirms the accepted revision differs in its normative body from `e68e8d98…`, this Plan's method basis must be re-confirmed. As it stands the normative body is identical across all three revisions, so this does not block E. D does not own the method reference and does not resolve the discrepancy; it is recorded for Driver/owner attention.

## 5. Validation basis

**Existing coverage:** the three checks in `tests/test_existing_behavior.py` cover the module-level operations and their accepted claim ("each current operation works"). They stay. **New coverage is required** because none of them asserts coherence across the pair (1.5). No existing check is replaced, so the method's replacement condition is not engaged.

**Falsifier for the core claim (design-time and implementation-time):** the X-2 straddle — produce a presented view's overview, complete a status update, then obtain the presented view's details. A design or implementation is invalid if it can present that pair as a revision-1 overview with revision-2 details. On the seed this falsifier fires today (§1.3), so it discriminates.

**Per-claim observables** (all reachable in-process with a bare `StateStore`; no mocks, no clock, no I/O):

| Claim | Observation that would falsify it |
| --- | --- |
| B-1 / DS-I1, DS-I2 | overview `revision` not the revision of its own details, or `open_count` ≠ number of `OPEN` among its own details, or a pair assembled from two resolutions |
| B-2 / DS-I5 | update completes, then episode opens, and the presented view's revision is older than that update |
| B-3 / DS-I3 | later episode reports a revision smaller than an earlier episode's |
| B-4 / DS-I4 | two episodes report an equal revision with different case data |
| B-5 | an update changed a status between episodes, and the later episode shows the old status or a non-greater revision |
| B-6 (a)–(d) | the four negative controls occur; (b) mixed pair and (d) pre-update status after a completed update are the two reachable on the seed |
| X-1, X-6 | no-change episode, and empty case set → count 0 with empty details |
| C-8 | any of the three existing checks fails or is weakened |

**Boundary for F — do not mislabel a legal variant as a B violation.** Pinning (C-3) is a **permitted** choice under P-1, not an accepted B requirement. An implementation that pins satisfies B; an implementation that instead switches to a newer revision mid-episode also satisfies B. F must verify B-1…B-6. Whether the implementation honors this Plan's pinned policy is a Plan-conformance question, not a B violation, and F owns neither acceptance of this Plan nor the policy choice. F also must not treat "no visible refresh" as a defect. `A8`-style verdicts here remain three-state; an environment block is `UNVERIFIED`, not a product defect.

**Expected scope of change (implementation assumption, not a file list):** the defect site is the second independent `current_view()` resolution in `src/case_reader.py` relative to `src/page_summary.py`, and the missing pair carrier across `src/turn.py` / `src/service.py`. `D-PLAN-INPUT.md` warns that the current structure is evidence, not a responsibility map; E owns placement (D-1).

## 6. Affected dependencies and regression surface

- `src/state_store.py` — `StateView`/`CaseRecord` immutability and rebind-not-mutate publication are **design dependencies** (C-4). `update_status` semantics for absent ids and for `"OPEN"`-only counting feed C-6/C-7.
- `src/page_summary.py` — already coherence-correct within the overview; may need to expose its view or be composed differently (E's choice).
- `src/case_reader.py` — the second resolution; the change site.
- `src/turn.py` — `Turn.page_summary` is a compatibility surface; the pair carrier currently does not exist.
- `src/service.py` — the entry points; compatibility surface (C-8).
- `tests/test_existing_behavior.py` — accepted coverage; retained verbatim (C-8, R-5).
- **Consumers outside the fixture:** none. No persistence, no schema, no migration, no external effect, so no compatibility or recovery obligation arises beyond C-8. No dependency on `UCBIP` or any product is created.

## 7. Assumptions

- A-1 · Single-threaded, in-process, one store lineage; no read/update interleaving *within* a single call (grounded in C's "in this single-threaded fixture, when the call returns").
- A-2 · `StateView`/`CaseRecord` value-immutability and rebind publication survive implementation (C-4). If not, R-4 governs.
- A-3 · E works within the Charter's object scope and does not modify B/C objects, `CASE-INPUT.md`, or the Charters.
- A-4 · B/C acceptance is **author acceptance by `tpw-night-m3-bc`, not independent evaluation** — stated in both objects. This Plan relies on their accepted *meanings* but does not claim to have independently verified them, and does not extend them to any product.
- A-5 · "Presented view" is realized by composition of the fixture's entry points; the fixture has no viewer/session object, so the episode boundary is a technical proxy (D-5).
- A-6 · The runtime reported in `BASELINE.md` and observed here reproduces the recorded 3/3 pass; the seed's `revision == 2` assertion is live coverage.

## 8. Unresolved points, boundaries and independence

**Resolved by this Plan (within delegation):** B-O1 → pinned policy (C-3/D-1). Version binding → every binding B/C conditional acceptance depends on is verified, and the embedded B/C/Backbone text is byte-identical to the files (§0.1); one *method-reference* binding remains unresolved and is reported, not absorbed (§0.2, R-9).

**Left open, deliberately:**
- U-1 · The carrier shape and episode-boundary representation (D-1, D-2, D-5) — genuinely interior; the orchestrating question the Plan leaves open is *where the pin lives*, and any answer satisfying C-1…C-10 is acceptable.
- U-2 · `DS-U2` revision behavior on a no-op update (D-4).
- U-3 · `DS-U1` statuses other than `OPEN`/`CLOSED` remain undefined and must not be resolved here (C-6, R-3).
- U-4 · Whether the Owner or B owner would prefer a visible refresh instead of pinning. Pinning is inside D's delegation by B-O1, so no approval is sought; a later switch is a Plan-level change (R-4) and, if it must become an accepted observable, a B change (R-1).
- U-5 · The method-citation discrepancy in §0.2 (cited revision self-declares as "candidate"; embedded copy is a later revision). Non-substantive — the normative body is byte-identical — but the binding is not verified and is reported to Driver (R-9). The method reference's owner decides whether "accepted" was intended.

**Not granted here:** implementation beyond the cited Charter delegation, deployment, migration, release, product generalization, M3 closure, or acceptance of B/C. Design acceptance does not produce execution permission; `PASS` on future verification does not produce a release authorization.

**Independence.** This Plan is authored by the D instance `tpw-night-m3-design` and is a **candidate**: it has not been independently challenged. `tpw-night-method` independently challenges the fixed Plan before E receives it, and is neither author nor acceptor. D owns acceptance of this fixture's technical Plan within the cited delegation; Driver checks input and version binding, not substantive design; F evaluates the implementation later. The B/C inputs were accepted by a different instance (`tpw-night-m3-bc`, session `01a0f39e-8658-7478-ad5e-b1870bb69bd6`), so this Plan is not a self-acceptance of that work. No independent evaluation of B/C or of this Plan is claimed.

**Unverified by me:** that the mechanism proposed to E will in fact satisfy B-1…B-6 — that is established only by the implementation and its evidence (or by the challenger's counterexample, whichever comes first). This Plan makes the target falsifiable and localizes the defect; it does not itself constitute verification. Also unverified: the method-citation binding (§0.2), which D does not own.
