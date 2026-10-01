# M3 case 2 · offline snapshot fixture

This is a dependency-free synthetic Python fixture. It describes only the offline exercise; it does not set product or UCBIP behavior.

## Seed

The source/test seed is recorded at commit `893eaf8`. `BASELINE.md` captures its pre-contract observation: three existing module-level checks pass, but no test covers one coherent view across a turn. The seed goal is in `CASE-INPUT.md`.

Run the seed checks from this directory with:

```sh
python3 -m unittest discover -s tests -v
```

## Accepted case-2 inputs

- Behavior: `BEHAVIOR-CONTRACT.md` v2, SHA-256 `6cf43d3fb647cf2c250f275179762917c0763a669e84f1718d85968a8e66c738`.
- Domain semantics: `DOMAIN-SEMANTICS.md` v2, SHA-256 `d35766b45085db2b7e5b3315cca5ce4183f722186a850ef317fd571ebba6d45b`.
- D technical Plan: `TECHNICAL-PLAN.md`, SHA-256 `a306205729a002fdf1bc4eac6a623849cb2198985f8a6fbae4ec4c00ec47e5b9`; accepted by the D instance within `D-CHARTER.md`. The affected-claim challenge is `M3-SNAPSHOT-PLAN-V2-RECHECK.md` (PASS on predecessor `bb8afeb1…`, with one non-blocking §8 wording correction applied in the accepted file).

The B/C pair is accepted for this fixture only. Its v2 Conditions treat the recorded source hashes as the accepted baseline: authorized `src/**` and `tests/**` changes inherit the acceptance while preserving its behavior and domain claims. Changes to accepted meanings or scope must return to the relevant owner.

## Case-2 implementation status

The E Charter and startup prompt are the controlling task binding. E may write only `src/**`, `tests/**`, and the named `M3-CASE2-E-REPORT.md` handoff in this fixture. The separate F evaluator's private criteria are not part of the implementation input. E self-checks are evidence for F; they are not an independent verdict. No implementation is accepted and M3 remains open until its case evidence and overall scope are handled.

The earlier seed note naming B/C v1 as current is superseded; those v1 objects remain recoverable at commit `893eaf8`.

## Case-2 adoption entry

Adopting a presented pair means opening an episode with `service.start(store)` and reading the returned `Turn`: `turn.page_summary` (overview) and `turn.cases` (details) are one presented pair resolved at that start. A bare-store `service.cases(store)` call is a separate current read with its own resolution, not this episode's details; the two must not be mixed inside one presented view (B-1, B-6(b)). Adoptable object: treatment commit `17602f2b12822aba88785e27a733f75a3238214d`; the PASS verdict, its exact presented-view boundary, and the limit below are recorded in `M3-CASE2-F-EVALUATION.md` (F PASS covers that fixed treatment and boundary only). This entry adds no B/C meaning and leaves B/C v2, the accepted Plan, the implementation and the tests unchanged.
