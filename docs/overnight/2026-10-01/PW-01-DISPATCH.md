# PW-01 dispatch · thin entry

Delegation: Owner 2026-10-01 direction (bounded Flash write sets, serial Driver integration, preserve Root raw/disposition/acceptance/allowance files) plus Oracle disposition `PRO-AUDIT-1-DISPOSITION.md` SHA-256 `afc63730d8f886230dc4e6b43056a2425b1536d2e6a4632d4081437ad005712f`. Scope and stop points exist only in that disposition. Driver is the serial integrator; Pro slot 2 stays with Oracle.

## Fixed references (read on demand; do not bulk-copy)

- Disposition: `docs/overnight/2026-10-01/PRO-AUDIT-1-DISPOSITION.md`
- Oracle acceptance, Pro-audit-1 section: `docs/overnight/2026-10-01/ORACLE-ACCEPTANCE.md` (working SHA-256 `9b498d367d0585d3b220a548e366ad7ba00424c09760ae98f1fb15e1bbd8af4c`)
- Pro 1 raw, specific quotes only: `PRO-AUDIT-1-RESPONSE.txt` / `PRO-AUDIT-1-RESPONSE.json`
- Package core (pre-revision identity): commit `62e3792`, package subtree `9e4fa14`, 19 files under `professional-workflow/`
- Frozen Backbone (bytes unchanged): `professional-workflow/authority/RESPONSIBILITY-BACKBONE.md` SHA-256 `ce82a70016a4a3fc234ea287f39aac8d79a260ddf13747c4fb705bda580453ba`
- UCBIP read-only root: `/Users/yuantian/Developer/ekunai/Unified-Customs-Bonded-Intelligence-Platform` (HEAD observed `7fc94e4a483cf6b1d8add214d7dbe9a1d42b7f76` at dispatch; the author re-reads and records the actual commit)

## A · `tpw-night-adopt` · UCBIP read-only authority check + optional adoption note

- **State:** candidate. **Profile:** none activated — bounded read-only documentation/adaptation, not a Profile-mediated judgment. **Instance:** `tpw-night-adopt` (new Pi Flash/max session).
- **Task / outcome:** read-only check of current UCBIP Git and the actual governance authority for AGENTS/multi-agent principles, delivery contract, CARD-STATE, role-binding, generated current-release, receipts, evidence-ledger; then write the short optional adoption note and a raw readback index.
- **Delegation source:** Owner direction + disposition PW-01. Records existing authorization; adds none.
- **Write set (only):** `adoption-examples/ucbip.md`, `docs/overnight/2026-10-01/PW-01-UCBIP-READBACK.md`.
- **Read scope:** UCBIP git metadata plus the governance documents and generated current-release sources needed to name the authority; this repo's disposition/acceptance files. Never open credential or production data; no UCBIP writes, services, tests, or network; do not modify `professional-workflow/`.
- **Applicable methods:** none bound (explicit; no M1-era pending label; no method authority added).
- **Note content (keep short):** optional/preparation status and non-normative boundary; actual read commit plus path/section index; owner separation between method reference and downstream authority/product/current-state owners; one bounded task Charter/packet example in the existing short-entry form covering input acceptance/delegation source, outputs, independent evaluation/acceptance landing points, Integrator main single-writer, sanitized result plus retrievable raw index — this authorized read-only check is the real example, future embodiments are placeholders with activation conditions; no faked role binding or authorization; no competing state/evidence system.
- **Deliver:** the two files; deviations and unresolved items; one line naming session and model.
- **Independence:** author only; independent check by `tpw-night-check` (separate instance). No self-PASS.
- **Recall:** if a target is missing/ambiguous or access is denied, record fact and impact, stop that item, report to Driver; do not invent authority.
- **Acceptance:** Oracle owns package/downstream acceptance; the note stays optional and non-binding.

## B · `tpw-night-fix` · bounded minor fixes

- **State:** candidate. **Profile:** none activated. **Instance:** `tpw-night-fix` (new Pi Flash/max session).
- **Task / outcome:** exactly the three bounded document edits below; nothing else.
- **Delegation source:** same as A.
- **Write set (only):** the three files below.
  1. `docs/overnight/2026-10-01/fixtures/m3-snapshot/README.md` — append a short case-2 adoption entry: `start` obtains `Turn`; its `page_summary`/`cases` are one presented pair; a bare-store `cases` read is a separate current read and must not be mixed with the Turn view; cite treatment commit `17602f2b12822aba88785e27a733f75a3238214d` and the F PASS scope in `M3-CASE2-F-EVALUATION.md`; leave B/C, implementation, and tests unchanged.
  2. `professional-workflow/authority/README.md` — append a side note: the frozen text's `A7`/`A8` references are source-repository provenance pointers for independence/three-state discipline; this package does not inherit A7/A8 numbering, schemas, or legacy checkers; the Backbone export bytes are unchanged (same digest as the table).
  3. `professional-workflow/README.md` — append one short non-normative pointer section: the optional adoption example lives outside this package at `../adoption-examples/ucbip.md`; the package does not own downstream UCBIP semantics, authority, or current state; the example grants nothing and does not affect assembly.
- **Applicable methods:** none bound (explicit).
- **Preserve / do not do:** keep every other byte of those files and all other files unchanged; do not touch Profiles, methods, Backbone, fixtures, or process records beyond the specified appends.
- **Deliver:** the three edited files plus a one-line summary of each edit; no commits.
- **Independence:** author only; Driver checks the diff; `tpw-night-check` later checks core separation from the optional note. No self-PASS.
- **Recall:** if an edit conflicts with an accepted statement, stop and report to Driver instead of rewriting.
- **Acceptance:** Oracle owns package acceptance.

## C · `tpw-night-check` · independent check + cold read

- **State:** candidate. **Profile:** none activated. **Instance:** `tpw-night-check` (new Pi Flash/max session), started after A and B deliver.
- **Task / outcome:** bounded independent review of the adoption mapping plus one cold read observation.
- **Delegation source:** same as A.
- **Write set (only):** `docs/overnight/2026-10-01/PW-01-MAPPING-REVIEW.md`; optional scratch only under `.worktrees/verification/`; no tracked-file writes.
- **Checks:** (1) mapping fidelity against `PW-01-UCBIP-READBACK.md` and read-only spot-check of the cited UCBIP commit/paths (sample level, no full audit); (2) positioning: optional/non-normative/outside core, no role binding or authorization invented, no competing state/evidence system; (3) core-start-without-note: the package has no runtime dependency on the optional note (only the README pointer references it), the documented assembly still yields ordered startup text with fixed objects, and the core file set remains the 19 files; (4) cold read: from `PW-01-DISPATCH.md` plus the package README alone, record whether Profile/methods/objects/constraints/return points could be located within bounded steps, and any observed ambiguity — a bounded observation, not re-qualification.
- **Applicable methods:** none bound (explicit).
- **Preserve / do not do:** do not re-run package qualification, do not modify UCBIP, do not redo M3 cases, do not accept anything for Oracle.
- **Deliver:** `PW-01-MAPPING-REVIEW.md` with PASS/limits per check, exact objects, and unresolved items.
- **Independence:** new instance; authored none of A/B outputs. No self-referential independence claim beyond that.
- **Recall:** fidelity or core-start failure → report to Driver with the affected object and fact; do not silently patch.
- **Acceptance:** Oracle; this check does not accept M6.

## Driver integration (this batch)

Driver serial integration: verify diffs, update `STATUS.md` old state, commit in-batch changes locally, compute the new core manifest and the optional/outside artifacts list, and hand the fixed commit/tree, manifest, evidence, residuals, and exact unverified points to Oracle for Pro slot 2. No push by this Driver; Oracle pushes and reads back as needed. No main/tag/merge/force-push/release/UCBIP/archive action.
