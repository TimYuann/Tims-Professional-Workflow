# Upstream deep-absorption plan · A full-path discovery/index + B substantive adjudication

**State:** planning only, prepared by Driver from the Owner–method discussion. No 1240 scan, no absorption, no product/core change, no crew dispatch, no fetch/install, no Pro. Baseline: main `0e06d8c0a118fa1396c0d5b192d8f9952c99f7ad`, core `91875114e51855517f92ef099cbdf60c34e68243`.
**Terminology note:** the `A`/`B` here are this phase's deliverable labels (discovery/index vs substantive adjudication); they are not the Backbone's A–F judgment classes, and A–F are not an execution order.

## 1 · Fixed inputs and accounting baseline

- Three repos, read-only at pins: `addyosmani-agent-skills` `2686b620…`; `cursor-plugins` `ecc249f1…`; `mattpocock-skills` `c55ee460…`. Locator root: `.worktrees/legacy-pre-night-2026-10-01/upstreams/`.
- **Baseline = the union of `git ls-files` at those pins.** Checked today without full enumeration: 208 + 863 + 169 = **1240** tracked paths. At execution start, freeze the exact NUL-safe listing, count and digest per repo and reconcile to 1240; the discussed 1240 figure is a reconciliation target, not an acceptance fact. No separate list file is needed unless reconciliation fails.
- Articles are excluded from this denominator; nothing from them counts as adopted without a later full original/mirror read.
- Accounting unit = each tracked path (text, support example, script, asset). Every path gets its own record even when content identity is shared; grouped non-method handling is allowed only with in-group exceptions, the related text and exclusion reasons. Never claim a file was fully read when it was not, and never assert every file is a "skill".

## 2 · A · full-path discovery and index (breadth, no adjudication authority)

- Record per path: source identity; **actual read depth** (metadata / structure / full); file nature; multi-label judgment/professional concern (Backbone A–F as reference, not order); concrete mechanism leads with original anchors; related files; uncertainties; coarse reading priority (high/medium/low).
- Priority only orders reading: it is not a score, not a stage, and not an adopt/reject signal; a low label must not become an implicit veto.
- Write boundary: A writes only its index documents under `docs/overnight/2026-10-01/` at fixed paths; no product/core, no upstream, no B documents.

## 3 · B · substantive mechanism adjudication (depth, independent)

- B independently re-reads the relevant originals, support files and current corresponding content, then states **adjudicated / explicitly deferred (with reason) / not-yet-judged (with reason)** and gives substantive reasons for adopt / narrow / re-frame / replace / reject / defer.
- B may extend an existing method or propose a new method, professional guide or counterexample library; it must not force findings into the current three methods. A missing current method is a gap lead, not a low score.
- Minimum reference for each adjudicated item: the full relevant source/support text, the concrete engineering problem it addresses, the domain correctness requirements, and existing coverage; answers why it works, when it fails, concrete how, what counterexample overturns it, and what it adds.
- Distillation keeps engineering rationale, applicability conditions, exceptions, counterexamples, techniques and operational detail; strips only named harness/model/fan-out/default-PR mechanisms, not professional experience (e.g., idempotency keeps intent/attempt, atomic claim, same-key-different-payload, in-flight duplicates, unknown outcome and retention causality).
- Write boundary: B writes only its adjudication documents at fixed paths; no product/core, no upstream, no rewriting A's records (deviations from A's screen are annotated in B's own documents).
- Independence: B reads originals before/independently of A's screen and is not the A author; no self-PASS.

## 4 · Accounting ↔ adjudication linkage, tail and closure

- Every A record carries a mechanism/adjudication group id (or an explicit grouped non-method disposition); group ids link A rows to B decisions.
- Per source-group final visible states: adjudicated (with disposition) / explicitly deferred (reason) / not-yet-judged (reason + re-query entry).
- Two completion statements are reported **separately** and must not stand in for each other: (1) file-accounting completion over the baseline; (2) mechanism-adjudication completion (groups with decisions). Neither implies adoption.
- Tail: low/undetermined/wrapper classes keep a re-query entry; tails must reach a group-level adjudication or an explicit deferral; grouped non-method disposition must list in-group exceptions, related text and exclusion reasons; sample checks only validate the initial screen, they do not dispose of the tail.
- Coverage closure criterion: 1240/1240 paths accounted and every path in a group whose state is one of the three above. Coverage closure ≠ full absorption, and adoption is decided separately.

## 5 · Small-sample calibration

- Small cross-source, cross-type sample (12–18 suggested; a suggestion, not a hard N or an Owner per-batch gate) including support-file hidden techniques, duplicates, platform wrappers, items overlapping existing coverage, and low/undetermined items.
- A produces the initial screen; B independently reads the originals first, then compares for anchoring, missed mechanism leads, classification drift and detail loss.
- Systematic bias → fix the criteria and re-check only affected groups; no full invalidation, no third standing gate.
- The calibration result is a bounded checkpoint visible to Driver/method, not a new permission layer.

## 6 · Preserving professional detail and actual-adoption criteria

- Adoption requires a full read of the relevant text and support files, with a record of what is kept / changed / deleted and why, the current-content difference, and the landing position.
- A high priority is not adoption; any effectiveness claim needs corresponding use evidence.
- Changes to existing methods follow the accepted method discipline (retain/narrow/strip records; delta review if active semantics change, revalidating affected claims only).
- Flash resources are sufficient: full-file coverage is not traded away to save tokens.

## 7 · Owner decision points (formal scope)

1. Authorize the phase and its formal coverage scope (three pinned repos; articles excluded).
2. Confirm composition/resources: A instance per repo or sequential; B instance(s); bounded method review points; Oracle milestone acceptance (no crew dispatch before this).
3. Confirm adoption authority: B proposes, method evaluates the design, Oracle accepts milestones; each core/product adoption batch needs explicit Owner authorization.
4. Confirm the closure definition in §4 and that adoption scope is decided by Owner after B.
5. Confirm no new terminology/state/permission platform, no third Pro, and that current accepts (PW-01/M6, main cutover) stay unchanged.

## 8 · Relation to earlier practice (how the two responsibilities change)

Earlier, one survey with reading-depth labels and one bounded dossier fed a single method review, leaving coverage implicit. Now: (a) A owns exhaustive per-path accounting with no adopt/reject authority and no veto; (b) B owns independent, group-level substantive adjudication with explicit deferred/not-yet-judged tails; (c) accounting completion and adjudication completion are separate reports; (d) a small calibration checks the screen before scale; (e) adoption is authorized by Owner only after B and requires full read plus use evidence. No scoring system, no new state machine, no extra permanent gate.
