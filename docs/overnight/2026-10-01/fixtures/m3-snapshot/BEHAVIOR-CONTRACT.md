# M3 case 2 · Behavior contract (B) — read-episode coherence and later-episode freshness

Isolated exercise contract for this synthetic fixture directory. It defines the externally observable behavior of the viewer exercise only. It is not a UCBIP rule and not a general product freshness policy; it must not be cited or generalized outside this fixture.

- **Version:** v1 · 2026-10-01
- **Owner:** `tpw-night-m3-bc` — B/C authoring instance for this exercise.
- **Scope:** observable behavior of a read episode, and of a later read episode, over one case-store lineage in this fixture. Meanings of the terms used here (case, status, view, revision, update, coherence) are owned by `DOMAIN-SEMANTICS.md` v1 and are not restated.
- **Conditions:** valid only against the inputs below. Any change to `CASE-INPUT.md`, the recorded source structure, or `BC-CHARTER.md` invalidates this acceptance and requires a new B version. This file defines behavior only: it does not assign module responsibility, select an interface, prescribe implementation, write a technical plan, or authorize implementation. The seed's current split-read behavior is evidence of the starting system, not this contract, and does not by itself satisfy the acceptance below.
- **Acceptance status:** **ACCEPTED** for the isolated exercise only, by the owner under `BC-CHARTER.md` (instance `tpw-night-m3-bc-contract`). Author acceptance, not independent evaluation. No product generalization is accepted or implied.
- **Produced by:** Pi session `01a0f39e-8658-7478-ad5e-b1870bb69bd6`; runtime verified from the process environment as `commandcode / deepseek/deepseek-v4.1-flash / max`.

## Inputs used (exact hashes)

- **`CASE-INPUT.md`** — `sha256 50063486b149fc599464cb5cb25872cc9b4c4b971d1fcbc2eab0efdabeffd772`
- **Fixture source structure** (`src/**`, `tests/**`) — aggregate `sha256 dbd6a306815bdc4cf3a33be14b38d4dd62b49d1535d7db41b9064eb07e51b474`
  - `src/__init__.py` — `sha256 a5f855a87138b8c9a515d76a2b7858da6bba6fb60eff9446197fafc774733cf4`
  - `src/case_reader.py` — `sha256 89f05180854b8cb38b58299f516e7298cd2d211b88bed38f35087e6b1fe350bc`
  - `src/page_summary.py` — `sha256 59bffca2096cdb3818a202e552fa5214dd3f263466fd4799b3d7ba4e4fac2fc4`
  - `src/service.py` — `sha256 ea3fff5faf10d3025b19a07cc709985467b9dc67e607282ff1c87c73ddd66a0d`
  - `src/state_store.py` — `sha256 90a1cb56549f5afdbae24d2b485f8a956e66081939159a435aa83e2f43029196`
  - `src/turn.py` — `sha256 5de7b6c681f8379e567d9be455a3176a48c429ca460b6810092ff7ae46504ac0`
  - `tests/test_existing_behavior.py` — `sha256 9ac7ea872b8c50f921128e7a8d734539b273551e7d6e9363e3d5116103c7876f`
  - aggregate recipe: sort the lines `<per-file sha256><two spaces><path relative to this fixture directory>`, join with `\n`, append a final `\n`, then take the sha256 of that UTF-8 text.
- **`BC-CHARTER.md`** (delegation) — `sha256 1395a01731f1ea4885b2e20c157ec47ba607e27fe8e2037006287562d3dd57ba`
- **`professional-workflow/profiles/behavior-domain.md`** (accepted Profile, per Charter) — `sha256 d8b75a5734c015f70d4c3f1479e094be11b92f2ee20d193dc22726fd599377fa`

## Observable surface

- A **read episode** is the bounded series of reads a viewer performs from opening the view until the next user action.
- An **overview observation** carries a revision indicator and an open count.
- A **case-details observation** carries the cases as `(case_id, status)` pairs.
- A **presented view** is the overview observation and the details observation an episode presents as its content.
- Seed vocabulary today: `revision`, `open_count`, `case_id`, `status`. The observable quantities and their relations below are fixed; naming, wire shape and call structure are not selected here.

## Acceptance

- **B-1 · Coherent episode.** Every presented view is coherent (DS-I1) and count-faithful (DS-I2): its open count equals the number of OPEN cases among its own details, and its revision is the revision those details belong to. A presented view that pairs an overview from one revision with details from another revision is a violation.
- **B-2 · Fresh episode.** If one or more status updates completed before an episode begins, that episode's presented view is at least as new as the newest of those updates (DS-I5): both its overview and its details reflect that update.
- **B-3 · Later episode, no regression.** A later episode never reports a revision smaller than an earlier episode's revision; a viewer comparing episodes in time order may treat a decreased revision as a violation (DS-I3, DS-I5).
- **B-4 · Equality is trustworthy.** Two episodes reporting the same revision present the same case data (DS-I4), so a viewer may treat an unchanged revision as unchanged statuses.
- **B-5 · Change is visible.** If an update changed a case's status between two episodes, the later episode presents the new status and its revision is strictly greater (DS-I4).
- **B-6 · Negative controls.** These observable outcomes are violations and must be treated as failures: (a) open count inconsistent with the details of the same presented view; (b) a presented view mixing two revisions; (c) a later episode reporting a revision smaller than an earlier episode's; (d) a later episode that begins after an update completed but still presents the pre-update status.

## Examples

Numbers in the examples are illustrative (DS-U3).

- **X-1 · No change (legal).** At revision 1 the store holds `C-1 OPEN`, `C-2 OPEN`. Episode 1 presents revision 1, open count 2, details `C-1 OPEN`, `C-2 OPEN`. No update follows. Episode 2 presents the same. *Acceptance: B-1, B-4.*
- **X-2 · Change between an episode's two reads (the important exception).** Episode 1 has already read its overview (revision 1, open count 2). Before its details are presented, `C-1 → CLOSED` completes (revision 2, open count 1). Legal outcomes: the episode presents the revision-1 pair (open count 2 with `C-1 OPEN`) or the revision-2 pair (open count 1 with `C-1 CLOSED`) — but not a revision-1 overview combined with revision-2 details. *Acceptance: B-1.*
- **X-3 · Change before a later episode (legal).** Episode 1 presents revision 1 with 2 open. `C-1 → CLOSED` completes. Episode 2 begins; it must not present revision 1, and it presents 1 open with `C-1 CLOSED`. *Acceptance: B-2, B-3, B-5.*
- **X-4 · Two changes between episodes (legal).** After `C-1 → CLOSED` and then `C-2 → CLOSED` complete, the next episode presents 0 open with both cases CLOSED and a revision greater than the first episode's. *Acceptance: B-2, B-5.*
- **X-5 · Unknown case id (exception, not fixed here).** An update naming a case id not in the case set leaves every status unchanged (DS-I7); whether the revision advances is not constrained (DS-U2). If it advances, the episode still satisfies B-1, B-3 and B-4: a revision may change with unchanged case data, while changed case data under an equal revision is a violation.
- **X-6 · Empty case set (legal).** A store with no cases presents an overview with open count 0 and empty details (the seed numbers its initial revision 1; DS-U3 does not fix the starting number). *Acceptance: B-1.*

## Permitted variants (not gaps)

- **P-1.** An episode may stay pinned to the revision current at its start, or switch to a newer revision when an update lands mid-episode, provided its presented view is coherent (B-1). No particular way of signalling a mid-episode refresh is required.
- **P-2.** An episode may read its details before its overview, or interleave reads, provided B-1 holds for what is presented.
- **P-3.** Revision values need not be contiguous or start at any particular number (DS-U3); only the ordering, equality and freshness relations are fixed.

## Open items (not decided here)

- **B-O1.** If an update lands mid-episode, whether the viewer sees a visible refresh (and in what form) or silently keeps the pinned revision: either is legal under P-1; whether the exercise fixes one is left to the D design.
- **B-O2.** Persistence across process restarts, concurrent viewers, and case-set membership changes are outside this exercise (see DS-U4); introducing any of them would require a new B version.
