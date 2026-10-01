# M3 case 2 · Technical Plan (D)

**Status:** **ACCEPTED by D** for this fixture's technical Plan, within the `D-CHARTER.md` delegated technical-planning scope — acceptance record at §8.1 (2026-10-01). Independent affected-claim recheck **PASS** on the reviewed predecessor `bb8afeb1d7519cac8926e1553f30e83590b8fb0504f120120c09cd916e0823d3` (`M3-SNAPSHOT-PLAN-V2-RECHECK.md`, `sha256 e93ac8869c2f0c94eb6b9ea8ec91a265920406656d31eacf12cee5b9a25ce278`), whose single non-blocking wording finding is the §8 correction applied in this revision. This acceptance is **not** acceptance of B/C, not evaluation or acceptance of any implementation, not M3 closure, and not authorization to deploy, migrate, release or change UCBIP; it does not authorize implementation, and starting E remains Driver's arrangement under existing authorization.
- **Reconciliation input:** `M3-D-PLAN-RECONCILIATION-PROMPT.md` (`sha256 8cfc6872e9ca266a488f4bb739de94cc42d438e6788332439735bb3fefe0f9df`).
- **Acceptance input:** `M3-D-PLAN-ACCEPTANCE-PROMPT.md` (`sha256 9154e1c7308e325ffd7afa750255975c1d52f3f516c71f13e8b820a1d9071773`).

> ### Dependency eligibility after B/C v2 — former PC-1 blocking callout withdrawn
> B/C v2 resolves the conflict this callout described: the recorded hashes are the **accepted baseline** — the fixture state the contract was authored against — and **not** a continuing no-change condition on `src/**`/`tests/**`. In-scope implementation and test diffs that preserve every acceptance item and observable quantity (`revision`, `open_count`, `case_id`, `status`) **inherit** the acceptance — including new or amended tests, added coordination behaviour, internal decomposition, renames, and the interface shape D selects. Changing the recorded bytes is not by itself an invalidation.
> The former "E must not start" bar and the §5/§6 gating are **withdrawn**. What this does **not** do: it is dependency eligibility only — it does not authorize implementation. D acceptance for the delegated technical-planning scope is now recorded (§8.1); that acceptance likewise does not authorize implementation.
- **Plan owner / decision responsibility:** `tpw-night-m3-design` (D instance for this exercise).
- **Delegation:** `D-CHARTER.md` (`sha256 6a0e6b7da8f8861e5d37c4d242b7df473e3ede1ffa531e5c73edd92e2730609f`) — Owner-authorized offline exercise in `docs/OVERNIGHT-WORKFLOW-PLAN-2026-10-01.md`, fixed M3 plan baseline `496b0676e302e2d0eafba129ff61de4c203d258a`. Task input: `D-PLAN-INPUT.md` (`sha256 89b131138ead556a3f6ac46ab758237c230c8cb6b615a9af57c92238fb4b7374`).
- **Date:** 2026-10-01 · **Object scope:** this fixture directory only.

## 0. Inputs and verified version binding

All bindings this Plan depends on were recomputed and **matched**, including the fixed B/C v2 pair. One method-provenance item stays bounded and recorded rather than resolved by D (§0.2). B/C v2 replaced the v1 Conditions; the v1 objects remain recoverable at commit `893eaf8` and are cited here only as superseded history.

### 0.1 Verified bindings

| Input | Role / decision owner | sha256 (recomputed) | Result |
| --- | --- | --- | --- |
| `BEHAVIOR-CONTRACT.md` **v2** | accepted behavior; owner `tpw-night-m3-bc` | `6cf43d3fb647cf2c250f275179762917c0763a669e84f1718d85968a8e66c738` | match (fixed B/C v2 input) |
| `DOMAIN-SEMANTICS.md` **v2** | accepted meaning/invariants; owner `tpw-night-m3-bc` | `d35766b45085db2b7e5b3315cca5ce4183f722186a850ef317fd571ebba6d45b` | match (fixed B/C v2 input) |
| `M3-BC-V2-REVIEW.md` | independent v2 review (`tpw-night-method`) | `675f32ded97ed90013db7eb4d0e6e6ea56fdce702f28ad1ba9e94124a303d091` | match — **PASS** on PC-1/PC-2 resolution and v1 claim preservation |
| `M3-SNAPSHOT-PLAN-CHALLENGE.md` | prior Plan challenge v1 | `bf3e15de71f4bf82adaa5547b9c412b4384a90d9d919420d5023fd9f593ab126` | match (dispositioned in §0.3) |
| `CASE-INPUT.md` | B/C authoring input (v2 re-open condition: exercise-goal change) | `50063486b149fc599464cb5cb25872cc9b4c4b971d1fcbc2eab0efdabeffd772` | match |
| `BC-CHARTER.md` | B/C delegation (v2 re-open condition: delegation/scope change) | `1395a01731f1ea4885b2e20c157ec47ba607e27fe8e2037006287562d3dd57ba` | match |
| fixture source (`src/**`, `tests/**`) aggregate | **accepted baseline** identity (B/C v2) | `dbd6a306815bdc4cf3a33be14b38d4dd62b49d1535d7db41b9064eb07e51b474` | match (all 7 per-file digests also match) |
| `RESPONSIBILITY-BACKBONE.md` | authority export cited by the Charter | `ce82a70016a4a3fc234ea287f39aac8d79a260ddf13747c4fb705bda580453ba` | match |
| `profiles/technical-planning.md` | Plan profile cited by the Charter | `d53da06edc99af3bcfc93c744af5f2cc8d512430d318a8b13b1b7f42652d74aa` | match |
| `D-STARTUP-PROMPT.md` | this task's startup input | `0f6d0e4e028543676273b33c1d0c74e5d933da2ed033be3f9669ca83ac748c90` | match |
| `D-CHARTER.md` / `D-PLAN-INPUT.md` | delegation / task input | `6a0e6b7da8f8861e5d37c4d242b7df473e3ede1ffa531e5c73edd92e2730609f` / `89b131138ead556a3f6ac46ab758237c230c8cb6b615a9af57c92238fb4b7374` | read, cited above |

**Superseded, cited only as history (recoverable at commit `893eaf8`, not active bindings):** `BEHAVIOR-CONTRACT.md` v1 `86dd6664b73de07ceefdbc5f4d03e09f49b4b1f2ee11cb6a80e48c251176555c`; `DOMAIN-SEMANTICS.md` v1 `15537d71d100dde30075f724c1ef79bc0d4e6a76a179f7f82d7f6c6b286cda06`. B and C are accepted **as a pair at v2**; a new version of either is re-issued together, so the Plan cites both at v2 throughout.

**Aggregate recipe — now normative in B/C v2 and aligned here (challenge PC-2, closed).** v2 states the sort key explicitly: order the files under `src/**` and `tests/**` by **relative path ascending** (Python `sorted()` on the path string), emit one line per file as `<per-file sha256><two spaces><relative path>`, join the lines with `\n`, append a final `\n`, and hash the UTF-8 text. That path order yields the recorded `dbd6a306…`. Sorting the digest-prefixed lines themselves yields `9074f27da8e0d76113bda8f774297c7c8fbceaedaf67d6ea75eec87d2421e88c`, which is **not** the recorded value; v2 records it as the non-matching alternative. Both orderings were recomputed here and agree with v2.
*Superseded in this Plan:* the pre-reconciliation draft explained the divergence as a **locale** effect and raised R-10 asking the B/C owner to correct the recipe wording. **Both are withdrawn** — locale was never involved, and v2 already states the key, so no correction request to the B/C owner survives. **R-10 is closed and is no longer an active recall.**

**Embedded copies vs. on-disk files.** `BASELINE.md` and `README.md` as embedded in `D-STARTUP-PROMPT.md` are byte-identical to the files on disk, as is the embedded Backbone export. The embedded **B and C** sections are byte-identical to the **v1** objects at commit `893eaf8`, **not** to the v2 files now on disk — v2 post-dates the startup prompt. This is the expected consequence of the v2 revision, not a discrepancy: the v1 body and the v2 body are byte-identical apart from the Conditions/recipe/metadata changes (§0.1, A-4), so none of the accepted behavior or domain content this Plan reasons over was altered by the revision.

### 0.2 Method provenance — bounded, independently re-checked (challenge PC-3)

The Charter cites the applicable method as `methods/cross-module-design.md` "from accepted M4 commit `013659331c8c5f9f54b866b393972a03d7938773` (SHA-256 `30066c8b…`)". Three blobs are in play:

| Object | sha256 |
| --- | --- |
| method blob at the cited M4 commit `0136593` | `30066c8b3ccee2b85e98c8bc36975f57161e2c93d0bd71c9c668b27bf79bae6f` |
| method text embedded in `D-STARTUP-PROMPT.md` — the copy this Plan actually applied | `59e686d0a7e488e9c7ae3eb85090da947ad7ac6a68d2feea1b007e4f6ba1456c` |
| method blob at this Plan's candidate commit `e3b2d3c` | `ab0a0bc03448407479fe82b92b2355384e7f2acf49c2ff3026882670f955a0a5` |

- **Semantic equivalence holds.** The normative range (`## Use` … before `## Source anchors`) is byte-identical across all three revisions: `sha256 e68e8d983ec675ce4fa4d6dea625987c94c7c14dc1e8521500203ae373ba42b9`. Differences are confined to the title, the `Status:` metadata line and the trailing deferral/provenance sentence — **no step, limit, trigger, independence rule or acceptance right differs**, and all three defer the same alternatives. The challenger re-derived this independently from Git objects rather than accepting my statement.
- **Acceptance is external to a blob's self-label.** `ORACLE-ACCEPTANCE.md` §M4 fixes `0136593` (tree `2fc8db5e…`) and accepts “该 commit 上三份有界方法正文与选择入口” as dependable content, and states that a change of *acceptance-status wording or typesetting alone* does not require re-running semantics. The earlier draft of this section inferred an unresolved acceptance problem from the blob calling itself "candidate"; **that inference was over-strong and is withdrawn.**
- **Residual, bounded and non-blocking:** the blob applied is not byte-identical to the blob cited. That is a **provenance/recording** matter for Driver and the integration writer — record the embedded copy's origin and the equivalence differential, and D cites one fixed version. It raises no new question for the method owner and does not gate E. It becomes a method-coverage matter only if the *substantive* body ever changes.

The method text applied constrains *how* this Plan is written; it does not select B/C meanings and does not enlarge delegated authority.

### 0.3 Disposition of challenge v1

Fixed object re-verified by me in this repository: candidate commit `e3b2d3cbb8664466fc9fd6d7e461dab82752ec19`, tree `4024c85c47840ddcd5df3ca7a073813892263988`, Plan `bcc10e4829918532f695b2d8be838d1aa2a2b9b8556c7654b5b14f1ce44adc1a` — all match the challenge's fixation.

| Finding | Disposition |
| --- | --- |
| **PC-1** · R-2 + B/C Conditions made any authorized implementation invalidate the acceptance it depends on | **Resolved upstream and verified closed.** B/C v2 Conditions redefine the recorded hashes as the **accepted baseline** — not a no-change condition — and state that in-scope `src/**`/`tests/**` diffs preserving the acceptance items and observable quantities inherit the acceptance. `M3-BC-V2-REVIEW.md` independently returned **PASS** on that resolution. The former blocking R-2 and the ⛔ callout are removed; §5/§6 gating is lifted. |
| **PC-2** · aggregate divergence is path-order vs digest-line-order, not locale | **Accepted; this Plan's factual error, now aligned.** The incorrect recipe explanation and the locale attribution are withdrawn in §0.1, the path-order key is stated to match the now-normative B/C v2 wording, and **R-10 is closed**. |
| **PC-3** · R-9 is bounded provenance, not a blocker; equivalence independently verified; M4 acceptance of `0136593` already recorded | **Accepted.** §0.2 rewritten; R-9 downgraded from "unresolved binding" to a recording action. |
| **PC-4(1)** · D-1/D-5 are not purely interior; name them bounded delegated coordination decisions, require the chosen entry point/episode boundary to be recorded | **Accepted.** §3 relabelled; recording obligation added. |
| **PC-4(2)** · the lazy-resolution sentence in D-5 must not imply any deferred first read is conformant | **Accepted.** D-5 tightened to the declared episode start of C-3. |
| **PC-4(3)** · C-2 is too absolute; re-read+validate is legitimate when both observations share one revision | **Accepted.** C-2 restated as *this Plan's* technical strategy, not a B-level prohibition. |
| **PC-4(4)** · R-7 "no shared state" is inaccurate; `StateStore` is a shared mutable reference | **Accepted; wording error.** R-7 corrected, and deliberately not turned into a safety conclusion. |

Not re-litigated (challenger-supported, unchanged): the core coherence direction, the X-2 falsifier as a discriminating observation, the pinned policy within B-O1/P-1, and the retained-versus-added coverage split.

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

- **C-2 · Coherence is structural under this Plan's chosen strategy (challenge PC-4(3) correction).** *This is D's technical strategy for this fixture, not a claim about what B forbids.* A re-read-and-validate scheme is legitimate when the observations it pairs carry the **same** revision, because coherence then follows from that revision's identity (DS-I4); it fails only when it leaves an already-obtained overview belonging to a different revision. This Plan deliberately chooses **single-resolution structural binding with no retry/reconcile path**, so the straddle cannot arise at all. *Basis:* B-1 with X-2; DS-I1/I4. *Consequence:* the binding unit is the **pair**. *Effect of deviating:* substituting a reconcile-on-mismatch design is a **Plan-conformance** question for E, not a B violation in itself.

- **C-3 · Episode policy is pinned (B-O1 resolved).** An episode resolves its view at its start and reuses it; no mid-episode refresh, no visible-refresh signal. Freshness at episode start is therefore automatic: the view current at start already includes every update completed before the episode began. *Basis:* B-O1 delegates this choice to D; P-1 permits pinning; DS-I3/I5. *Owner of the choice:* D (this Plan). *A weaker alternative is also legal* (switching to a newer revision mid-episode, P-1) — noted at U-4 as an open preference question, not offered as a second policy in this Plan.

- **C-4 · Published views are immutable.** `update_status` must continue to publish a **new** `StateView` and must not mutate a previously published one; `CaseRecord`/`StateView` statuses must remain value-immutable for the lifetime of any pinned view. This is what makes C-3 sound; breaking it fails silently. *Basis:* observed 1.2; DS-I4. *Basis for the constraint:* the pin depends on it, so it is a coordination surface, not an interior choice.

- **C-5 · Observations are values, not live aliases.** The overview and details a caller receives must be immutable or freshly copied, so a pinned presented view cannot change after an update. *Basis:* DS-I1/I2 must hold at presentation time, not merely at read time. *Current code already satisfies this* (fresh `dict`, tuple of frozen records) — preserve it.

- **C-6 · Count rule unchanged.** `open_count` counts exactly `status == "OPEN"`; a case is open iff its status is exactly `OPEN`. Do not add handling, validation, normalization or inference for other labels. *Basis:* C §Terms (open), DS-I2, DS-U1 (undefined; **no authority in this fixture to rule**). *Forbids:* resolving DS-U1 as a side effect of implementation.

- **C-7 · Case order and membership unchanged.** Preserve presented order; do not sort, dedupe or add cases. *Basis:* C §Terms (case set "in the presented order"; two views identical iff same ids in same order with same statuses), DS-I7. Duplicate ids remain outside the contract.

- **C-8 · Compatibility is additive.** Existing call forms `service.start(store) -> Turn` with `page_summary["revision"]`/`["open_count"]`, and `service.cases(store) -> tuple[CaseRecord, ...]`, remain callable with a bare `StateStore` and keep their current results when no update interleaves. The three existing checks stay passing and are **not** deleted or weakened. *Basis:* method step 6 (prefer additive when consumers must remain compatible); DS-U3 notwithstanding, `tests/test_existing_behavior.py` asserts a fresh store starts at revision 1 and one update makes it 2 — so keep start 1 / step 1. *Owner of the compatibility requirement:* D; the coverage itself belongs to the fixture's recorded structure.

- **C-9 · Deterministic, in-process, no new resources.** The coherence mechanism must be exercisable in-process against a bare `StateStore`: no clock, thread, sleep, I/O, retry loop, locking or persistence. *Basis:* method step 3 (seam for the actual dependency shape: in-process, locally replaceable, no true external dependency) and B-6's need for deterministic observation.

- **C-10 · No new observable behavior.** The change adds nothing beyond B-1…B-6. No new exceptions for in-contract inputs, no logging contract, no error semantics beyond what exists, no membership/persistence/concurrency features. *Basis:* B's scope; DS-U4 / B-O2 (outside the exercise); Charter "do not select new product behavior".

- **C-11 · No performance or ordering commitment is added.** No latency, throughput, buffering or ordering guarantee beyond the coherence relation itself; no performance characteristic of this interface becomes something a caller may rely on. *Basis:* method step 2 asks for "relevant performance characteristics" — here the honest answer is that none is relevant to the accepted claims, and inventing one would enlarge the objective.

## 3. Delegated Decisions — bounded coordination choices delegated to E

These are delegated, not prescribed (method step 5: planner preference alone is not a reason to fix them). Per challenge PC-4(1) they are **not** treated as invisible internals: because F and the next consumer must be able to locate the concrete entry point and episode boundary, **E must record the actual choice it makes** — entry point, episode boundary, carrier and pin representation — in its handoff, mapped to C-1…C-10. Nothing here licenses a change to semantics, interface, constraint or verification basis; that is R-4 territory, not delegation. B v2 Conditions explicitly list "the interface shape D selects" among the `src/**`/`tests/**` diffs that inherit the acceptance, so this delegation sits inside the inherited envelope — subject to the same re-open conditions (R-2).

- **D-1 · The carrier shape for a coherent pair (bounded delegated coordination decision).** Whether this is a single producer returning overview and details together, an episode/handle object created at open, an optional revision or pin argument with a store-only fallback, or a pin stored on `StateStore`. Naming and module placement are also E's. *Constraint:* C-1, C-2, C-8, C-9. *Must be recorded:* the concrete entry point a consumer or verifier calls and the episode boundary it establishes (D-5). *Explicitly not prescribed* — `D-PLAN-INPUT.md` states it intentionally does not prescribe module ownership or a token/argument shape, and I am not inventing one.
- **D-2 · Whether the pin is materialized or implicit**, i.e. a stored `StateView` reference versus producing the pair within one call so no separate pin exists. Same constraints.
- **D-3 · Reuse `Turn` as the carrier or add another**, provided `turn.Turn.page_summary` keeps its two keys and meaning (C-8) and the addition is additive.
- **D-4 · `DS-U2` — revision advance on a no-op update.** The seed advances the revision even when the named id is absent. Keeping or changing this is E's, since C leaves it unconstrained and B's X-5 permits either. *Constraint:* DS-I4 must hold, C-8 must hold, C-10 applies.
- **D-5 · Where the episode boundary is drawn in a fixture with no viewer/session object (bounded delegated coordination decision).** B defines the episode from opening the view to the next user action; the fixture has no such object. E may model it as exactly one pair-producing call, or as an explicit open step. *Constraint:* the resolution point must be well-defined and atomic with respect to updates — in this single-threaded fixture, inside one Python call. A lazy (first-use) resolution is conformant **only if it occurs at the episode start declared under C-3**, i.e. the moment the caller's episode opens; a deferred first read that happens *after* further updates have completed is a different episode boundary, not a lazy pin, and must not be presented as satisfying C-3. Either way a presented view never resolves twice (C-1). *Must be recorded:* which boundary was chosen, so F and the next consumer can find it.
- **D-6 · Local types, refactors, and the structure of new tests**, consistent with the existing `unittest` style and with C-9.

## 4. Recall Conditions — when to come back

Return through Driver to the cited authority. Do not silently resolve any of these.

- **R-1 · B/C change.** Any need to alter, reinterpret or extend an accepted B/C meaning, or any finding that a B/C input conflicts: name the affected accepted object, the observed fact and the impact → Driver → `tpw-night-m3-bc`. D does not decide it.
- **R-2 · B/C acceptance scope (was the PC-1 blocker — resolved by B/C v2, retained in narrowed form).** Per B/C v2 Conditions the recorded hashes are the **accepted baseline**, not a no-change condition: in-scope `src/**`/`tests/**` diffs that preserve every acceptance item and observable quantity **inherit** the acceptance, and changing the recorded bytes is not by itself an invalidation. **A new B/C version is still required** — and the changed part is not covered until one is accepted — for a change that alters any acceptance item (B-1…B-6), the observable surface, the read-episode / presented-view model, the freshness anchor (updates completed before an episode begins), or the B-O2 scope notes; any `DOMAIN-SEMANTICS.md` term or DS-I1…I7; the case/view/revision model; a DS-U item resolved or narrowed into a new requirement; or `CASE-INPUT.md` (exercise goal) or `BC-CHARTER.md` (delegation and scope). B and C are accepted **as a pair**, so a new version of either is re-issued together. *Basis:* `BEHAVIOR-CONTRACT.md` v2 and `DOMAIN-SEMANTICS.md` v2 §Conditions — the authority here is the B/C owner, and **D does not decide this and does not read it away**.
  *Citation guidance:* cite the v2 **Conditions**, not the v2 change-log summary, which is narrower than the Conditions list (noted as non-blocking in `M3-BC-V2-REVIEW.md`).
- **R-3 · Undefined semantics pressed into service.** DS-U1 (other status labels) → C owner, and must not be resolved as a side effect of implementation. By contrast, B/C v2 Conditions state that a **D/E choice made freely inside DS-U3** is *not* a re-open condition, and DS-U2 is likewise left unconstrained — so D-4's numbering/advance choice does not return here. The re-open trigger is instead **resolving or narrowing** a DS-U item into a new requirement.
- **R-4 · Coordination surface must change.** If coherence cannot be achieved without changing `StateView`/`CaseRecord` immutability, view publication semantics, or the revision's identity/ordering relations → back to D (this Plan). This is a surface change, not an interior one.
- **R-5 · Accepted coverage must be replaced.** If implementation cannot proceed without deleting or weakening one of the three existing checks → back to D; the method grants no deletion authority, and C-8 forbids it.
- **R-6 · Out-of-scope capabilities requested.** Persistence across restarts, concurrent viewers, case-set membership changes, multi-store comparison, deployment or migration → B-O2 / DS-U4: outside the exercise, **requires a new B version**; and any of these is in any case outside this Plan's and this fixture's action authorization. Do not implement.
- **R-7 · Safety/cost/professional concern appears.** Corrected per challenge PC-4(4): `StateStore` **is** a shared mutable reference across this fixture's reads and updates — "no shared state" was wrong. What the exercise genuinely lacks is *concurrency, cross-viewer sharing, persistence, and any external effect*; the in-process tests plus immutable view values are what cover the surface known today. That is a statement about present scope — **not** a risk assessment, and not a "no risk" claim. If concurrency, cross-viewer sharing, persistence or another external effect is proposed, D cannot rule on it: route via Driver to the relevant professional responsibility; human-reserved items only via Voice.
- **R-8 · Challenge and re-check findings.** `tpw-night-method`'s independent challenge v1 returned **FAIL** on the pre-reconciliation candidate; its findings are dispositioned in §0.3. Findings return to the D owner for decision or revision; the challenger is neither author nor acceptor of this Plan. This reconciliation has **not** itself been independently re-checked — Driver routes only the materially affected Plan claims for recheck, and a further finding re-opens the corresponding claim rather than the whole Plan.
- **R-9 · Method provenance recording (downgraded per challenge PC-3).** **Not a binding failure and not blocking.** The M4 acceptance of `0136593` is recorded in `ORACLE-ACCEPTANCE.md` §M4, and the normative body is byte-identical across the cited, embedded and current blobs (`e68e8d98…`). Action: Driver / the integration writer record the embedded copy's origin and the equivalence differential, and D cites one fixed version. No new acceptance question is raised for the method owner. Re-open only if the *substantive* body changes.

## 5. Validation basis

> **Eligibility (formerly "gated on R-2"; PC-1 resolved).** Under B/C v2 Conditions, in-scope implementation and test diffs — including new or amended tests — inherit the B/C acceptance. What follows is the coverage that must exist when E implements. **This is dependency eligibility, not authorization:** D acceptance is recorded at §8.1, and starting E is Driver's call under existing authorization, not this document's.

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

> **Eligibility (formerly "gated on R-2"; PC-1 resolved).** The change surface below describes where the coherence binding must land, and the in-scope diffs it implies inherit the B/C v2 acceptance. This is **not** authorization to modify these files: D acceptance is recorded at §8.1, and E start is Driver's call under existing authorization.

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
- A-4 · B/C v2 acceptance is **author acceptance by `tpw-night-m3-bc`, not independent evaluation** — stated in both objects. The v2 clarification (PC-1/PC-2) and preservation of the v1 claims were separately reviewed **PASS** by `tpw-night-method` (`M3-BC-V2-REVIEW.md`), and I reproduced the same preservation directly: the v1 body (section heading → EOF) is byte-identical to the v2 body before `## Change log` — `eab01bf9…` for B, `f303d5c9…` for C, matching the review's digests. That review covers the B/C inputs only; it does not accept this Plan and does not authorize E. This Plan relies on the accepted *meanings* and does not extend them to any product.
- A-5 · "Presented view" is realized by composition of the fixture's entry points; the fixture has no viewer/session object, so the episode boundary is a technical proxy (D-5).
- A-6 · The runtime reported in `BASELINE.md` and observed here reproduces the recorded 3/3 pass; the seed's `revision == 2` assertion is live coverage.

## 8. Unresolved points, boundaries and independence

**Resolved by this Plan (within delegation):** B-O1 → pinned policy (C-3/D-1). Version binding → the active bindings are the fixed **B/C v2** pair, verified in §0.1. The startup prompt's **B/C copies are the v1 objects** (identical to commit `893eaf8`); only their behavior/domain body is byte-consistent with v2, since v2 changed only the Conditions, recipe and version metadata (§0.1, A-4). This Plan relies on the **v2 Conditions**, not on the embedded copies being v2. The embedded **Backbone** copy is the original fixed export and stays byte-identical to `RESPONSIBILITY-BACKBONE.md`. All challenge findings are dispositioned in §0.3, with PC-1 closed upstream and PC-2 closed here.

**Nothing is left blocking in this Plan.** The former PC-1 blocker is resolved by fixed B/C v2 and its independent PASS, and the PC-2 correction is applied. D acceptance for the delegated technical-planning scope is recorded below; E start remains Driver's arrangement under existing authorization and the §5/§6 eligibility, and neither this Plan nor its acceptance authorizes implementation.

### 8.1 D acceptance (recorded 2026-10-01)

- **Accepted object:** the corrected Plan in this file, within the technical-planning responsibility delegated by `D-CHARTER.md` (M3 plan baseline `496b0676e302e2d0eafba129ff61de4c203d258a`).
- **Reviewed predecessor and independent basis:** `bb8afeb1d7519cac8926e1553f30e83590b8fb0504f120120c09cd916e0823d3`, independently rechecked for the affected claims with verdict **PASS** — `M3-SNAPSHOT-PLAN-V2-RECHECK.md`, `sha256 e93ac8869c2f0c94eb6b9ea8ec91a265920406656d31eacf12cee5b9a25ce278`. Its single finding (the §8 embedded-copy wording) was classified **non-blocking** and is the correction applied in this revision.
- **Accepting party:** `tpw-night-m3-design`, as the D instance holding this delegation. This records the **existing** D responsibility for the technical Plan; it adds **no new gate**, approval step or authority beyond it.
- **Scope — what is accepted:** this fixture's technical Plan only, as written in this file.
- **Explicitly not accepted or granted here:** B/C themselves (the v2 pair was accepted by `tpw-night-m3-bc` and separately reviewed PASS — a different act, by different parties); any implementation or its correctness; M3 closure; and any deployment, migration, release or UCBIP change.
- **Not claimed:** that *this corrected hash* has itself been independently rechecked. The recheck covered `bb8afeb1…`; this revision differs from it only by the non-blocking §8 correction and this acceptance record — the narrow diff for Driver to verify.

**Left open, deliberately:**
- U-1 · The carrier shape and episode-boundary representation (D-1, D-2, D-5) — **bounded delegated coordination decisions**, not invisible internals: E must record the concrete choice, and any answer satisfying C-1…C-10 within the recorded boundary is acceptable.
- U-2 · `DS-U2` revision behavior on a no-op update (D-4).
- U-3 · `DS-U1` statuses other than `OPEN`/`CLOSED` remain undefined and must not be resolved here (C-6, R-3).
- U-4 · Whether the Owner or B owner would prefer a visible refresh instead of pinning. Pinning is inside D's delegation by B-O1, so no approval is sought; a later switch is a Plan-level change (R-4) and, if it must become an accepted observable, a B change (R-1).
- U-5 · Method provenance recording (§0.2, R-9): the blob applied differs from the blob cited, while the normative body is byte-identical and M4 acceptance of `0136593` is already recorded. This is a recording action for Driver / the integration writer, not a decision, and it stays **bounded** — it is not a method gate, not an acceptance gate, and not a blocker.

**Not granted here:** implementation beyond the cited Charter delegation, deployment, migration, release, product generalization, M3 closure, or acceptance of B/C. Design acceptance does not produce execution permission; `PASS` on future verification does not produce a release authorization.

**Independence.** This Plan is authored by the D instance `tpw-night-m3-design`. It was independently challenged once: `tpw-night-method` — neither author nor acceptor — returned **FAIL** (`bf3e15de…`) against candidate `e3b2d3c` / Plan `bcc10e48…`; that was revised (`f081c1c3…`) and then reconciled to `bb8afeb1…`, on which an independent **affected-claim recheck returned PASS** (`e93ac886…`) with one non-blocking wording finding. Author and acceptor here are the same responsible party, as the delegation provides: the recheck is independent *challenge*, whereas D acceptance (§8.1) is D's own act — two different facts, not a self-review. **This corrected revision has not itself been rechecked**; it differs from the rechecked hash only by the correction that recheck called non-blocking, plus the acceptance record. D owns acceptance of this fixture's technical Plan within the cited delegation; Driver checks input and version binding, not substantive design; F evaluates the implementation later. The B/C inputs were accepted by a different instance (`tpw-night-m3-bc`, session `01a0f39e-8658-7478-ad5e-b1870bb69bd6`) and independently reviewed PASS at v2 by `tpw-night-method`. D acceptance of this Plan is not acceptance of B/C, of any implementation, or of M3 closure.

**Unverified by me:** that the mechanism proposed to E will in fact satisfy B-1…B-6 — that is established only by the implementation and its evidence, or by a further counterexample. This Plan makes the target falsifiable and localizes the defect; it does not itself constitute verification. Also not established here: that any implementation actually placed inside the B/C v2 inherited envelope keeps every acceptance item true — that is what the §5 observables are for, and D's acceptance of this Plan does not substitute for it.
