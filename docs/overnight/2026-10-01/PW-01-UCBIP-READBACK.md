# PW-01 · UCBIP read-only authority readback

State: **readback index** produced by `tpw-night-adopt` for `PW-01-DISPATCH.md` §A. Point-in-time
observation of one downstream repository at one commit. It is not downstream authority, not a new
ledger or roster, and carries no acceptance claim. The optional note it supports lives at
`adoption-examples/ucbip.md`.

## Read identity

| Item | Value |
| --- | --- |
| Producer | `tpw-night-adopt` — Pi session `01a0f666-937f-77c2-a59f-f9988876b313`, provider `commandcode`, model `deepseek/deepseek-v4.1-flash`, thinking `max` |
| Target | `/Users/yuantian/Developer/ekunai/Unified-Customs-Bonded-Intelligence-Platform` |
| HEAD | `7fc94e4a483cf6b1d8add214d7dbe9a1d42b7f76` on `main` |
| HEAD commit | `2026-10-01T14:06:23+08:00` · `docs(governance): sync current control to the tool-seal implementation window` |
| Dispatch expectation | §A fixed references named HEAD `7fc94e4a483cf6b1d8add214d7dbe9a1d42b7f76`; observed value is identical ⇒ no drift between dispatch and this read |
| Tracked tree | clean (`git status --porcelain --untracked-files=no` empty) |
| Untracked, not read | `engineering_report.html`, `pi-session-2026-09-23T17-42-32-555Z_01a0cf5c-….html` (pre-existing root exports; UCBIP's own drift audit already recommends moving them out) |
| Method | `git rev-parse` / `git status` / `git ls-files` / `git grep` / `sed` / `shasum -a 256` — read-only |
| Not done | no UCBIP write, no service, no test suite, no network, no credential or production-data access, no product source read, `scripts/render_current_state.py` **not executed** |

## Object-family index

Seven families, each with the object that currently holds the fact and the anchor to quote.

| # | Family | Authoritative object (path) | Anchor | Keeps it true |
| --- | --- | --- | --- | --- |
| 1 | Agent entry / multi-agent principles | `AGENTS.md`; `docs/active/multi-agent-development-principles.md` | `AGENTS.md` §Start here (items 2/3/4/5), §Repository invariants, §Domain navigation · principles §5 (75–92), §5.1 role contracts (94–117), §6–§10, §11 (201), §11.1–§11.7 (206–311) | Owner-approved tracked docs; principles define roles/routing/verification, not permissions |
| 2 | Delivery contract | `docs/active/agent-delivery-contract.md`; short form `docs/templates/agent-delivery.md` | contract §1 Start and assign (7), §2 Isolate writes and runtime (17), §3 Implement and verify (27), §3.1 fake-green rebuttals (51), §4 Integrate and update project facts (66), §5 Retain the right evidence (84), §6 Handoff and cleanup (100), §7 Cold-checkout procedure (108) · template §一项可验收任务 (5) / §卡的当前状态块 (33) / §最小交付记录 (47) | Integrator writes tracked facts; each role keeps its own record |
| 3 | `CARD-STATE` | the per-task card's block, e.g. `docs/tasks/2026-09-30-l5-live-sse.md` `<!-- BEGIN CARD-STATE … END CARD-STATE -->`; grammar in `docs/templates/agent-delivery.md`; reader/checker `scripts/render_current_state.py` | template 卡的当前状态块 `task_id / task_revision / phase / result_owner / candidate / basis / next_or_blocker / checkpoint`, `phase` is a closed vocabulary · renderer docstring lines 1–20, `REGION_NAMES` (40), `BINDING_PATH` (89) | the card's **result owner**; one hand-written state per node, never the projection |
| 4 | `role-binding` | `.agent-local/driver-0922/role-binding.tsv` (ignored, Driver-owned, 4 columns `role / bearer / pane / as_of`); projection in `docs/tasks/2026-09-19-multi-agent-restart.md` (19–31) and `docs/active/current-release.md` (18–19) | restart card 「当前控制权」/「换班规则」(6, 32) · current-release 承载源 (18), 绑定表校验 (19) | the Driver slot; each handover updates the one source and refreshes projections |
| 5 | Generated current-release | `docs/active/current-release.md` `## Now` + `<!-- BEGIN GENERATED: current-entry -->` (10–35); restart card `role-binding` (19–31) and `dag-table` (78–102) regions | uniqueness rule at current-release 61: one hand-written place, three generated regions, `--check` must FAIL on hand edits; renderer exit codes 0 = fresh, 1 = drift, 2 = cannot evaluate | projection only; the carrier's `CARD-STATE` and the binding source are upstream |
| 6 | Receipts | `docs/receipts/2026/*.md` — 129 tracked files at this commit, incl. `consolidated-2026-09-23/INDEX.md` | contract §5 table; §6 handoff fields | the flow that produced the result, promoted by the Integrator |
| 7 | Evidence ledger | `docs/evidence-ledger.md` — header row at 23, 186 data rows, classes at 13 (`R-claim` / `R-round` / `R-rebuild` / `R-scratch`) | columns `evidence-id / flow / produced-by / produced-at / path / sha256 / bytes / about-candidate / class / retain-until / rebuildable / referenced-by / status`; raw bytes live in ignored `.agent-local/evidence/<flow>/` | the assigned integration-checkout writer; receipts cite `evidence-id`, never a path |

Adjacent object worth naming for the method seam: `docs/active/engineering-method-routing.md`
(lines 1–25 and 35) already records that the four pstack method bodies are carried by the external
`tim-professional-workflow` project, that upstream "只提供方法正文", and that 方法不产生权限.

## Checks actually performed (and nothing stronger)

1. **Git identity** — HEAD, branch, commit date and tracked cleanliness read directly; two untracked
   root HTML exports recorded but not opened.
2. **Byte match of the binding source** — `shasum -a 256 .agent-local/driver-0922/role-binding.tsv`
   = `83572fd4c85f06f104b4b4914b2e1feaad8abee4ca8abbaee45e1deb45dc644b`, which is exactly the digest
   `docs/active/current-release.md:19` declares for as-of `2026-10-01T06:04Z` (4 columns, 10 lines,
   9 roles; 4 roles carried, 5 written `—`). The binding source is ignored by `.gitignore:191`
   (`/.agent-local/`), matching contract §7's rule that runtime binding may live outside tracked
   files only with one source, a pointer plus `as-of`, and an existence/freshness check.
3. **Anchors exist and are tracked** — every path in the table above is in `git ls-files` at HEAD and
   carries the cited section/line anchor.
4. **Counts** — 129 tracked receipt files under `docs/receipts`; 186 ledger data rows.

Not performed: the renderer's own `--check` (a read-only script, but executing it is outside
"read-only documents and necessary generated source" in §A), any product test, any UCBIP mutation.

## Residual limits of this readback

- It names objects and owners; it does **not** verify that every declared state is current, that the
  five AGENTS §Start here cold-read questions are answerable without extra reading, or that the
  tool-seal window's ignored card is the truth of the current wave. The generated projection's
  freshness is only checked at the binding-source byte level (item 2), not by re-running the checker.
- Only the objects needed to name the authority were opened; `docs/TODO.md` (211 KB),
  `docs/active/current-release.md` beyond the `## Now` region, the receipt bodies and the ledger
  bodies were sampled, not read through.
- Downstream role bindings are recorded as read, not endorsed or extended. This file grants nothing.
- No UCBIP-side owner reviewed this index; recall path in §A applies — if a downstream owner finds a
  mismatched object, the affected item stops and goes back to the Driver.
