# Optional adoption example · UCBIP governance hand-off

State: **preparation-only, non-normative, outside the core package.** This file is referenced from
the package entry (`professional-workflow/README.md`) only as an optional example. It is not part of
`professional-workflow/`, is not a status source, and grants no role, write window, permission or
acceptance. Nothing here activates on any session.

The core package deliberately ships no downstream mapping: it owns its Profile/Charter/method text
and their assembly order, while authority, product behavior, current state and evidence stay with the
downstream repository. This example shows that seam for one repository (UCBIP) at one observed
commit. Values below are point-in-time; a future embodiment must re-read the downstream sources and
bind them again.

## Read basis

- Repository: `/Users/yuantian/Developer/ekunai/Unified-Customs-Bonded-Intelligence-Platform`
- Commit actually read: `7fc94e4a483cf6b1d8add214d7dbe9a1d42b7f76` (`main`, tracked tree clean).
- Path/section index, the four checks performed, and the non-read list:
  `docs/overnight/2026-10-01/PW-01-UCBIP-READBACK.md`. That file is this batch's process record; it is
  an index, not the downstream ledger and not a second status board.
- The read was documentation-only: no UCBIP write, service, test run, network, product data or
  credential access, and the downstream state checker was not executed.

## Who owns what

| Object | Owner |
| --- | --- |
| Method bodies, Profile/Charter text, assembly order | this package (`professional-workflow/`); method reference only |
| Task graph, priorities, write windows, dispatch | downstream **Driver slot** → `docs/tasks/2026-09-19-multi-agent-restart.md` 「当前控制权」 |
| `main` writes | downstream **Integrator slot** (`writer` in the binding source); single writer, serial merge |
| Node state | each task card's `CARD-STATE` block (the one hand-written state per node) |
| Entry / generated projection | three generated regions across two files — `current-entry` in `docs/active/current-release.md` `## Now`, and `role-binding` + `dag-table` in `docs/tasks/2026-09-19-multi-agent-restart.md`; refreshed by `scripts/render_current_state.py`, never hand-edited |
| Role-to-session binding | `.agent-local/driver-0922/role-binding.tsv` (ignored, Driver-owned) + pointer and `as-of` in the tracked entry |
| Raw evidence / sanitized receipts | `.agent-local/evidence/<flow>/` + a row in `docs/evidence-ledger.md`; receipts in `docs/receipts/2026/` |
| Product behavior | `docs/active/stable-v1-product-contract.md` |

UCBIP already states the neighbouring rule itself: `docs/active/engineering-method-routing.md` records
that the external `tim-professional-workflow` carries method bodies only, that upstream provides
"只提供方法正文", and that 方法不产生权限.

## Bounded task example (real, exercised)

This is the PW-01 §A read-only check, written in the package's compact Charter form. Every field below
is a fact of that run, not a template to reuse.

```text
Instance Charter · PW-01 A · UCBIP read-only authority check

State:              exercised for this instance; not an accepted reference
Profile:            none activated (explicit; a bounded read-only documentation/adaptation task,
                    not a Profile-mediated judgment — assembly was not applied)
Instance:           tpw-night-adopt (separate Pi session)

Task / outcome:     read-only check of current UCBIP Git and the actual governance authority for
                    AGENTS/multi-agent principles, delivery contract, CARD-STATE, role-binding,
                    generated current-release, receipts, evidence-ledger; then write the short
                    optional adoption note and a raw readback index.
                    Non-goals: no UCBIP write/service/test/network/product source/credential access;
                    no change to professional-workflow/.
Delegation source:  Owner 2026-10-01 direction + Oracle disposition
                    docs/overnight/2026-10-01/PRO-AUDIT-1-DISPOSITION.md (SHA-256
                    afc63730d8f886230dc4e6b43056a2425b1536d2e6a4632d4081437ad005712f).
                    Records existing authorization; adds none.
Object scope:       read — UCBIP git metadata + the governance documents and generated current-release
                    sources needed to name the authority, plus this repo's disposition/acceptance
                    files. write — exactly adoption-examples/ucbip.md and
                    docs/overnight/2026-10-01/PW-01-UCBIP-READBACK.md.
Accepted inputs:    PW-01-DISPATCH.md §A; the disposition above; ORACLE-ACCEPTANCE.md Pro-audit-1
                    section (Oracle's working SHA-256 9b498d36…af4c).
Applicable methods: none bound (explicit; no method authority added).

Responsibility:     name the real downstream objects and their owners; draft the non-normative note.
Delegated decisions: how to index the objects; wording of the note. No acceptance, no downstream
                    change, no role binding.
Preserve / do not:  frozen package bytes, UCBIP, and every other path; do not invent authority when a
                    target is missing, ambiguous or denied.
Tools / actions:    shell read-only commands (git/sed/shasum). No downstream mutation; no external
                    effect.

Deliver:            the two files; deviations and unresolved items; one line naming session and model.
Independence:       author only. Independent check by a separate instance (tpw-night-check); the
                    author must not record a self-PASS.
Recall:             missing/ambiguous target or denied access → record the fact and its impact, stop
                    that item, report to the Driver; do not invent authority.
Acceptance:         Oracle owns package/downstream acceptance; the note stays optional and
                    non-binding. Downstream landing, if a future UCBIP task is authorized:
                    phase → the card's CARD-STATE; sanitized result → one docs/receipts/2026/
                    receipt; raw → .agent-local/evidence/<flow>/ plus one
                    docs/evidence-ledger.md row; accepted current facts → the owning tracked
                    document, written in the same integration batch by the Integrator slot
                    (main single writer).
```

**Sanitized result and retrievable raw index.** The result is the tracked readback
(`PW-01-UCBIP-READBACK.md`, paths and digests only, no secrets). The raw index is the downstream
objects themselves, retrievable by querying the recorded commit `7fc94e4a…` — this batch therefore
creates no copy, no archive and no second ledger. A future UCBIP-side task would instead land its raw
bytes under `.agent-local/evidence/<flow>/`, add one `docs/evidence-ledger.md` row, and keep at most
one sanitized `docs/receipts/2026/` receipt per flow.

## Future embodiment (placeholder — not authorized)

```text
Instance Charter · <task name>
State:              candidate
Profile:            <one of profiles/*.md; name it and add its assembly line>
Instance:           <unique session name>
Task / outcome:     <bounded task in UCBIP>
Delegation source:  <the UCBIP task card / Driver write-window record that grants it; none here>
Object scope:       <read set, write set, explicit boundary>
Accepted inputs:    <downstream card, contract/current-truth refs, evidence refs, versions>
Applicable methods: <exact methods/ path(s), or none>
Responsibility:     <the judgment actually delegated>
Preserve / do not:  <accepted commitments; product source only in an independent worktree>
Deliver:            <candidate/object + evidence + residuals>
Independence:       <author, challenger, evaluator; a reviewer did not implement the candidate>
Recall:             <what stops dependent work; Driver routes to the boundary owner>
Acceptance:         <who evaluates, who accepts, who owns closure — separate from delivery>
```

Activation conditions, all required: (1) a UCBIP task card or Driver window actually grants the work;
(2) the binding source is re-read at that time and the role actually carrying the slot is named from
it, not from this example; (3) the write set and the single `main` writer (Integrator) are stated in
the card; (4) outputs are bound to existing UCBIP objects — `CARD-STATE` for phase, receipt + ledger
row for evidence, generated entry for visibility. Until then this block is a placeholder.

## What this example is not

- Not an authorization, role binding or write window; the bindings read above are observational and
  are not extended by this file.
- Not a second state source: UCBIP's unique control record and `## Now` entry remain the only current
  state, and its ledger remains the only evidence index.
- Not a precedent for importing a second ledger. UCBIP's own drift audit already records the counter-
  example: a prior TIM cold-start trial (`72ac591`, not on `main`, not contained in any branch) added
  `docs/decision-ledger.md` inside `docs/` and was flagged exactly because it created a competing
  ledger authority (`docs/evidence-ledger.md`, row `L6-GOVERNANCE-0929/drift-audit`, audited
  2026-09-29). UCBIP's `docs/TODO.md` also records that this package's repository is another project
  and must not be modified from there.
