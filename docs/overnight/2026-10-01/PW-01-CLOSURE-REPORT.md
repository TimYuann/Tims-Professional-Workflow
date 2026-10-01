# PW-01 closure report · optional UCBIP adoption layer

**State:** PW-01 work is complete within `PRO-AUDIT-1-DISPOSITION.md` scope; the delivery is ready for Oracle push/readback and the second Pro slot. This is a self-contained handoff, **not** a self-acceptance: M6 stays unaccepted until Oracle (and Pro slot 2) dispose.

## Result

- Fixed object: commit `05f4bbb9a490f055855bdd0cde859c4c09421342`; repository root tree `4b7f99f5ecabde30dd550dbfb226fbe7a8b638e8`; `professional-workflow/` package subtree `11e6e3772b6bc0e17259c932b0c0dcabb030a133`.
- Core 19-file archive SHA-256: `5d551aca0e9dfef47f7886799b9975cadd55c1c16698158efafe8088eacd996d`.
- New manifest with the core/optional split: `M6-PACKAGE-CANDIDATE-05f4bbb.md` (supersedes `M6-PACKAGE-CANDIDATE-d672914.md` as current candidate). Core change vs d672914 is exactly two appended files, +6 lines; Backbone bytes unchanged.
- Tip adds only process records on top of the fixed object (this report, the manifest, STATUS refresh).

## What was done (disposition scope)

1. **PW-01 UCBIP read-only authority check** (instance `tpw-night-adopt`, Pi Flash/max): read-only verification at UCBIP commit `7fc94e4a483cf6b1d8add214d7dbe9a1d42b7f76` (`main`, tracked tree clean) of AGENTS/multi-agent principles, delivery contract, CARD-STATE, role-binding, generated current-release, receipts, evidence-ledger; produced the optional note `adoption-examples/ucbip.md` and the index `PW-01-UCBIP-READBACK.md`. No UCBIP write, service, test, network, product-data, or credential access; `render_current_state.py --check` not run. UCBIP HEAD and untracked state unchanged at close.
2. **§B bounded minor fixes** (instance `tpw-night-fix`, Pi Flash/max), committed `e9c0c99`: fixture case-2 adoption entry (`start`→`Turn` pair; bare-store `cases` is a separate read); `authority/README.md` A7/A8 provenance side note (no numbering/schema/legacy checkers; frozen bytes unchanged); package README non-normative pointer to the outside note; STATUS refresh.
3. **§C independent check + cold read** (instance `tpw-night-check`, Pi Flash/max; authored none of A/B): `PW-01-MAPPING-REVIEW.md` — fidelity PASS with 2 defects, positioning PASS, core-start-without-note PASS, cold read PASS with recorded ambiguities.
4. **Defect fix + bounded re-verify**: the two factual defects (disposition object name; generated-region count/location) and one fidelity omission (missing “network”) were fixed by the author in `adoption-examples/ucbip.md`; the same reviewer re-verified exactly those three locations — all PASS/closed, appended as “Post-fix re-verify”.
5. **Thin entry**: `PW-01-DISPATCH.md` records the three short Charters (Profile none activated, applicable methods none, explicit write sets, stop points). No new node, role matrix, state machine, gate, or method category was added.

## Evidence map (digests at 05f4bbb)

| Object | SHA-256 | Role |
| --- | --- | --- |
| `adoption-examples/ucbip.md` | `5d6bfde3…d7a8` | optional adoption note (non-binding, outside core) |
| `PW-01-UCBIP-READBACK.md` | `c1683b13…7cc9` | §A read-only index and observed anchors |
| `PW-01-MAPPING-REVIEW.md` | `9a6e873f…9585` | §C independent check + cold read + post-fix re-verify |
| `PW-01-DISPATCH.md` | `06b0d832…27ed` | thin-entry dispatch/Charters |
| `PRO-AUDIT-1-DISPOSITION.md` | `afc63730…712f` | Oracle scope/stop points |
| `ORACLE-ACCEPTANCE.md` | `9b498d36…af4c` | M3 bounded / M5 local-adoption / M6-PW-01 acceptance text |
| `PRO-AUDIT-ALLOWANCE.md` | `ad104446…a742` | slot 1/2 record |
| `PRO-AUDIT-1-RESPONSE.txt` / `.json` | `a7c2c923…aac4` / `533be09b…7296` | Pro-1 raw preservation |
| core archive | `5d551aca…996d` | core 19-file export at the fixed commit |

## Residuals and exact unverified

- No full package re-qualification, no M3 reruns, no runtime/deploy/recovery claim. Old F/cold-start/rollback evidence stays bound to its own objects; only the affected assembly/no-dependency claim was re-observed.
- Cold-read ambiguities recorded in the review: README title reads “M5 integration candidate” while the active process is PW-01/M6; `path/to/current-task-input.md` placeholder; M1-era “待 M4” Profile labels need the methods/README hop; pointer placement after §Package state. None of these was rewritten in this batch.
- Review limits: product-behavior owner row verified at path level only; readback sampled, not read through; no UCBIP-side owner review of the readback; renderer `--check` not executed.
- M6 remains unaccepted; the optional note remains preparation-only and grants nothing.

## Recommendation for Oracle

1. Push the latest tip and `ls-remote` readback; the fixed object for review is `05f4bbb` (core subtree `11e6e377…`).
2. Submit Pro slot 2 against the exact pin with the manifest, readback, and review; keep it read-only and scoped to the PW-01 revision plus the open M6 acceptance question.
3. Keep `main`, tags, merge, force-push, release, archive, and UCBIP untouched; Oracle owns push/readback and the Pro decision.
