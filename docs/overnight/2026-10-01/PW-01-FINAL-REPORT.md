# PW-01 / M6 final closeout report · R1/R2 differential batch

**State:** the two bounded corrections from `PRO-AUDIT-2-DISPOSITION.md` are complete and independently checked, fixed at commit `205b831ecb9ba4e79481a08e6b23f7159dca4113`. Oracle owns read-back and closure under its accepted scope; this report is not an acceptance.

## Fixed object

- Commit: `205b831ecb9ba4e79481a08e6b23f7159dca4113`
- Repository root tree: `136e0fcda54056bc188b67950a3f32dbfd165319`
- `professional-workflow/` core subtree: `11e6e3772b6bc0e17259c932b0c0dcabb030a133` — **unchanged**; no core byte was touched in this batch (Oracle already accepted this subtree).
- Accepted-pin archive identity (at `05f4bbb`): `5d551aca0e9dfef47f7886799b9975cadd55c1c16698158efafe8088eacd996d` — unchanged.
- The tip after this report adds only this document; the fixed object for the R1/R2 evidence is `205b831`.

## Corrected optional-layer identity (final bytes at the fixed commit)

| File | SHA-256 |
| --- | --- |
| `adoption-examples/ucbip.md` | `37335d1c7245e30a10d7c74b8c33a0a74b5c4f7fd3d1c64e7e65f93894a62fce` |
| `docs/overnight/2026-10-01/PW-01-DISPATCH.md` | `37aa265903aec355dc3cb83ad52affc021f74d437767a8e30ab7adc9f1212654` |
| `docs/overnight/2026-10-01/PW-01-UCBIP-READBACK.md` | `83a54d0b2cf0f713ad12b74c2d22a426808d4da2bcbc586bbb65674488735ce5` |
| `docs/overnight/2026-10-01/M6-PACKAGE-CANDIDATE-05f4bbb.md` | `9845bfbe896c73b0d0a90489afb263f8a6a7d7916766523a18eff7e483e6eb06` |
| `docs/overnight/2026-10-01/PW-01-MAPPING-REVIEW.md` | `256a8d0610004844a81c359c360e8f41f3b8c70e495e7d7ea4fd3cea207371dc` |

`M6-PACKAGE-CANDIDATE-05f4bbb.md` keeps its historical optional-artifact table pinned to the `05f4bbb` digests (not rewritten, per the disposition); the identities above are the final bytes for the R1/R2 batch.

## R1/R2 changes (actual)

- **R1 acceptance authority:** the note's Charter `Acceptance` now attributes only the TIM-side adaptation-preparation artifact and the local-adoption delivery to TIM Oracle; UCBIP adoption, task acceptance, action authorization and closure remain with the responsibility designated by the effective downstream delegation; no downstream acceptance occurred in this run. The equivalent correction was appended as errata to the historical `PW-01-DISPATCH.md` §A with the original text preserved.
- **R2 retrieval boundary:** the note now distinguishes tracked documents/generated projections (retrievable at `7fc94e4a`) from the ignored binding source and other runtime raw (local point-in-time observation with recorded path/digest/`as-of`; no commit-only recovery promise; a future adoption must re-read the then-effective binding). Errata appended to `PW-01-UCBIP-READBACK.md` check 3, original preserved; manifest correction appended for the §B fixture README append (fixture contract/code/tests unchanged).
- **Clarity:** hand-written state sources (each card's `CARD-STATE`, the Driver-owned binding source) are distinguished from generated entry/projections (`## Now`/`current-entry`, and the `role-binding` + `dag-table` regions, refreshed by `scripts/render_current_state.py`).
- No new archive, evidence ledger, gate, role, or scope.

## Independent differential verdict

- `tpw-night-check` (Pi session `01a0f66d-0b7b-7701-8c51-8d262cb2f8d4`, separate from the author) appended **“Differential re-check · R1/R2”** to `PW-01-MAPPING-REVIEW.md`: R1/R2/H/S/N/M six items PASS; exact fixed output identity recorded; no downstream acceptance or commit-only recoverability invented; historical originals preserved.
- Reviewer limits retained: original dispatch sentence preserved by design; the manifest table still pins the historical `05f4bbb` identity; no whole-package or M3 re-check; no commit by the reviewer.
- Driver recomputed the five digests (match) and read the diffs; `professional-workflow/` stayed clean.

## Residuals and exact unverified

- Core acceptance and prior evidence scopes stand exactly as `ORACLE-ACCEPTANCE.md` records; no whole-project effectiveness or efficiency claim.
- Downstream owner acceptance has not occurred; no governance adoption or business startup.
- Pro could not retrieve UCBIP `7fc94e4a` through its connector (404): downstream original-source verification by Pro is **UNVERIFIED**, not evidence that the local readback is false.
- Readback is sampled, not read through; renderer `--check` not run; no runtime/deployment/recovery claim; exact timing/cost limits retained.
- `/tmp` scratch use is retained as a non-blocking process deviation (accepted, not retroactively compliant); future scratch stays in workspace verification directories.

## Stop

No auto continuation: no third Pro, no source absorption, no core change, no M3 rerun, no `main`/tag/merge/archive/release, no UCBIP write/service/test/startup. Oracle reads the differential evidence and closes PW-01/M6 under the accepted scope.
