# M3 case 2 · E implementation handoff

- **Instance:** `tpw-night-m3-local-impl` (Pi session `01a0f3ac-a22b-75ef-9946-984ec8f6603b`) — the existing E author session previously used for case 1; reused, not a new independent identity.
- **Binding inputs (hashes as received and re-verified):** startup packet `M3-CASE2-E-STARTUP-PROMPT.md` `e0cf4f0e4beac2e777c460e74f3eee5142e1eb2b5ab30b0c1057ac49696ad346`; Charter `M3-CASE2-E-CHARTER.md` `75b5f5023c5682bd932069a6a783bc808e5b1c76b447a659f155abe0fee39661`; B/C v2 pair `6cf43d3fb647cf2c250f275179762917c0763a669e84f1718d85968a8e66c738` / `d35766b45085db2b7e5b3315cca5ce4183f722186a850ef317fd571ebba6d45b`; accepted D Plan `a306205729a002fdf1bc4eac6a623849cb2198985f8a6fbae4ec4c00ec47e5b9`.
- **Environment:** worktree `…/.worktrees/night-2026-10-01`, branch `night/2026-10-01-workflow`, base commit `2ad7227`; Python 3.14.4; offline, standard library only.
- **Scope of this report:** implementation facts and self-check observations only. It is **not** a verdict on the behavior; no PASS/FAIL is claimed, and no F criterion, rubric or report was read, searched for or inferred. E self-checks are evidence input for F, not an independent conclusion. No release, deployment, migration or closure is claimed.

## 1. Pre-edit baseline verification (seven per-file hashes and the aggregate)

Verified against the worktree files before any edit, with the B/C v2 recipe (files under `src/**` and `tests/**` ordered by relative path ascending; one line per file as `<sha256><two spaces><path>`; joined with `\n` + final `\n`; sha256 of the UTF-8 text):

| File | Recorded (B/C v2) | Recomputed | Result |
| --- | --- | --- | --- |
| `src/__init__.py` | `a5f855a8…33cf4` | `a5f855a87138b8c9a515d76a2b7858da6bba6fb60eff9446197fafc774733cf4` | match |
| `src/case_reader.py` | `89f05180…e350bc` | `89f05180854b8cb38b58299f516e7298cd2d211b88bed38f35087e6b1fe350bc` | match |
| `src/page_summary.py` | `59bffca2…ac2fc4` | `59bffca2096cdb3818a202e552fa5214dd3f263466fd4799b3d7ba4e4fac2fc4` | match |
| `src/service.py` | `ea3fff5f…d66a0d` | `ea3fff5faf10d3025b19a07cc709985467b9dc67e607282ff1c87c73ddd66a0d` | match |
| `src/state_store.py` | `90a1cb56…029196` | `90a1cb56549f5afdbae24d2b485f8a956e66081939159a435aa83e2f43029196` | match |
| `src/turn.py` | `5de7b6c6…504ac0` | `5de7b6c681f8379e567d9be455a3176a48c429ca460b6810092ff7ae46504ac0` | match |
| `tests/test_existing_behavior.py` | `9ac7ea87…c7876f` | `9ac7ea872b8c50f921128e7a8d734539b273551e7d6e9363e3d5116103c7876f` | match |
| **aggregate** | `dbd6a306…e51b474` | `dbd6a306815bdc4cf3a33be14b38d4dd62b49d1535d7db41b9064eb07e51b474` | match |

The digest-line-sorted alternative was also recomputed as `9074f27da8e0d76113bda8f774297c7c8fbceaedaf67d6ea75eec87d2421e88c`, matching the non-matching value recorded in B/C v2 — so the path-order recipe is the one in force and it reproduces the recorded aggregate.

After implementation, the five files the change did not touch (`src/__init__.py`, `src/case_reader.py`, `src/service.py`, `src/state_store.py`, `tests/test_existing_behavior.py`) were re-hashed and still match their baseline digests above.

## 2. Chosen design (D-1, D-2, D-3, D-5; C-1…C-3, C-9)

- **Carrier (D-1, D-3):** the existing `turn.Turn` is reused as the pair carrier. No new module, no new public function, no second carrier type.
- **Entry point (D-5):** `service.start(store)` (which calls `turn.begin_turn(store)`). This is the call a consumer or verifier makes to open the episode; it returns the pinned `Turn`.
- **Episode boundary (D-5):** one call, atomic with respect to updates. The episode is the `Turn` returned by `start`/`begin_turn`; it resolves `StateStore.current_view()` exactly once, at open. The two observations of that episode are `turn.page_summary` (overview: `revision`, `open_count`) and `turn.cases` (details: the case pairs), both serving the presented view. No mid-episode refresh, no retry/reconcile path.
- **Pin representation (D-2):** materialized — `Turn.view: StateView` holds the single resolution; `page_summary` and `cases` are derived properties over that one view. The overview count is computed by the same `page_summary.summarize_view(view)` used by the retained `build_page_summary(store)`, so the `OPEN`-only count rule has one implementation.
- **Observation values (C-5):** `page_summary` returns a fresh `dict` per access and `cases` returns the pinned view's immutable tuple, so nothing a caller receives can change under a later update.
- **`DS-U2` / D-4:** kept the seed behavior — an update that leaves every status unchanged (unknown case id) still advances the revision. Legal under DS-U2 and X-5; DS-I4 still holds because no case data changes.
- **Compatibility (C-8):** `service.start(store)` still returns a `Turn` whose `page_summary` carries exactly `revision` and `open_count`; `service.cases(store)` is unchanged; the three existing checks are byte-identical and were not deleted or weakened. `StateStore.update_status` still publishes a new `StateView` by rebinding (C-4), and `CaseRecord`/`StateView` remain frozen.

Boundary note for F and the next consumer: `service.cases(store)` and `page_summary.build_page_summary(store)` remain independent single-resolution callables. Two separate calls still resolve twice and can observe different revisions; that two-call pattern is **not** the presented view under this Plan's model — the modeled presented view is the pinned pair carried by the `Turn` opened by `service.start`. No hidden episode state was added to `StateStore` to bridge the two call forms.

## 3. Changed files and SHA-256

| Path | Change | SHA-256 (current bytes) |
| --- | --- | --- |
| `src/page_summary.py` | modified — added `summarize_view(view)`; `build_page_summary(store)` now delegates | `a3b81175423bd241a2c63c9d0b530fda2aad9698a3e96ba6bd9495764d7570f1` |
| `src/turn.py` | modified — `Turn` pins the resolved `StateView`; `page_summary`/`cases` are derived properties; `begin_turn` resolves once | `2be753eb357ad4c0eb150861c61a2b220c75af5423fc10a2ad9d304eede52354` |
| `tests/test_episode_coherence.py` | added — coherence coverage (see §5) | `4f0b000892b2e5f3808166ee305bc8ba492661262d1be27757c661dac317076e` |

No other file in the fixture was written. Nothing was committed; the candidate is the worktree state above (base commit `2ad7227`), so F/Driver can fix the object by these hashes.

## 4. Commands and observations

All commands run from `docs/overnight/2026-10-01/fixtures/m3-snapshot`.

**4.1 Seed baseline before any edit** — `python3 -m unittest discover -s tests -v`
Exit `0`; `Ran 3 tests … OK` (matches `BASELINE.md`).

**4.2 Pre-change falsifier probe (negative control on the unmodified seed bytes, in-process, `PYTHONDONTWRITEBYTECODE=1`)** — opens a "view", completes an update, then obtains the details through the then-available second resolution:

```
seed overview  : {'revision': 1, 'open_count': 2}
seed details   : [('C-1', 'CLOSED'), ('C-2', 'OPEN')]
count-faithful : False
same revision  : False
X-2 straddle (B-6(b)) present in seed split pattern: True
Exit 0
```

**4.3 New tests against the unmodified seed (red evidence)** — `python3 -m unittest discover -s tests -p 'test_episode_coherence.py' -v`
Exit `1`; `Ran 9 tests … FAILED (failures=1, errors=6)`. The carrier was absent (`AttributeError: 'Turn' object has no attribute 'cases'`) and the pinned-value check failed on the seed because a mutated returned summary was the stored object (`{'open_count': 99}`) — the live-alias defect behind C-5.

**4.4 Post-change full suite (Charter seed command)** — `python3 -m unittest discover -s tests -v`
Exit `0`; `Ran 12 tests … OK` (3 retained existing checks + 9 new).

**4.5 Post-change carrier probe** — same scenario as 4.2 through the pinned carrier:

```
carrier overview: {'revision': 1, 'open_count': 2}
carrier details : [('C-1', 'OPEN'), ('C-2', 'OPEN')]
count-faithful  : True
still revision 1: True
store revision  : 2
Exit 0
```

## 5. Coverage preserved and added

Preserved: the three checks in `tests/test_existing_behavior.py` are byte-identical (hash §1) and pass; nothing was deleted or weakened.

Added (`tests/test_episode_coherence.py`, 9 checks):

| Check | Claims exercised |
| --- | --- |
| `test_mid_episode_update_cannot_straddle_the_presented_pair` | X-2, B-1, B-6(a)(b), DS-I1, DS-I2, C-1…C-3 |
| `test_episode_observations_are_pinned_values` | C-3, C-5 (caller mutation cannot alter a pinned observation) |
| `test_update_completed_before_episode_is_visible` | X-3, B-2, B-5, DS-I5 |
| `test_later_episode_revision_never_decreases` | B-3, B-6(c), DS-I3; start-1/step-1 compatibility (C-8) |
| `test_equal_revision_presents_equal_case_data` | X-1, B-4, DS-I4 |
| `test_each_update_between_episodes_is_visible` | X-4, B-2, B-5 |
| `test_empty_case_set_presents_zero_open_and_no_details` | X-6, B-1 |
| `test_update_with_unknown_case_id_leaves_all_statuses_unchanged` | DS-I7 with DS-U2 (documents the kept D-4 choice) |
| `test_existing_entry_points_stay_callable_with_a_bare_store` | C-8 (keys and call shapes) |

## 6. Deviations, boundary facts and unresolved items

- **Deviations from the Plan: none identified.** No B/C meaning, D commitment, observable surface, scope or acceptance item was changed; no R-1…R-9 recall condition was triggered. `CASE-INPUT.md`, `BC-CHARTER.md`, the B/C v2 pair, the Plan, the Charters, the packet, `professional-workflow/` and all evaluation artifacts were not edited.
- **Placement fact (D-1 leaves placement to E):** the change lands in `src/page_summary.py` and `src/turn.py`; `src/case_reader.py` and `src/service.py` needed no edit — `service.start` already delegates to `begin_turn`, which now pins.
- **Boundary fact recorded for F:** the legacy two-call pattern (`start(...)` then `cases(store)`) still resolves twice by design; the modeled episode/presented view is the `Turn` (see §2). This is the recorded D-5 boundary, not a residual defect claim.
- **Unresolved / left to F and the next consumer:** whether the pinned-pair carrier and the recorded boundary are the ones to rely on; observable independence and coverage adequacy of these self-checks; behaviour under concurrency, persistence or cross-viewer sharing is outside the exercise (B-O2, DS-U4) and was not attempted.
- **Not claimed:** behavioral correctness, an F verdict, M3 closure, or any authorization beyond this fixture.

## 7. Independence

This implementation was authored by the case-1 E session above, which is the same identity for case 2. The case-2 F evaluator (`tpw-night-method`) is a different session and did not author these changes; E did not read or infer its criteria, and this report does not speak for it. E self-check observations above are inputs to that evaluation, not an independent result.
