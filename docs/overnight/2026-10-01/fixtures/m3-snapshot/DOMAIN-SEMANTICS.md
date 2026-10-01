# M3 case 2 · Domain semantics (C) — case, view, revision and invariants

Definitions and invariants for the same isolated synthetic fixture. Meaning only: observable acceptance is owned by `BEHAVIOR-CONTRACT.md` v2 and is not restated. Not a UCBIP or product domain model; it must not be cited or generalized outside this fixture.

- **Version:** v2 · 2026-10-01 — supersedes v1 (`sha256 15537d71d100dde30075f724c1ef79bc0d4e6a76a179f7f82d7f6c6b286cda06`), which remains recoverable at commit `893eaf8`. v2 changes only the Conditions, the aggregate recipe and version metadata; the terms and invariants below are unchanged from v1.
- **Owner:** `tpw-night-m3-bc` — B/C authoring instance for this exercise.
- **Scope:** meaning of the exercise's domain terms and the invariants B/D may rely on, for one case-store lineage in this fixture. No module responsibility, interface, technical plan or implementation is defined here.
- **Conditions:** accepted against the baseline inputs below. Those hashes identify the fixture state the terms and invariants were defined against — the **accepted baseline** — not a continuing no-change condition on the fixture source tree.
  - **Inherits this acceptance (no new B/C version needed):** diffs under `src/**` and `tests/**` that keep these terms and invariants true — including implementation changes, new or amended tests, internal decomposition and renames. The authorized D/E exercise is expected to produce such diffs; changing the recorded bytes is not by itself an invalidation.
  - **Requires a new B/C version:** a change to any term definition or to DS-I1…I7; a change to this document that resolves or narrows DS-U1…U4 into new requirements (a D/E choice made freely inside DS-U3 is not such a change); any change to the case/view/revision model itself; a change to `BEHAVIOR-CONTRACT.md` acceptance items (C's terms are cited there); or a change to `CASE-INPUT.md` (exercise goal) or `BC-CHARTER.md` (delegation and scope). Until a new version is accepted, the changed part is not covered by this acceptance.
  - This document and `BEHAVIOR-CONTRACT.md` are accepted as a pair (both at v2); a new version of either is re-issued together.
  - **Conflict rule:** if a fixture fact conflicts with a definition below, that is an open item to report, not a reason to silently redefine the term. D may rely on these meanings and may not silently change them.
- **Acceptance status:** **ACCEPTED** for the isolated exercise only, by the owner under `BC-CHARTER.md` (instance `tpw-night-m3-bc-contract`), as `DOMAIN-SEMANTICS.md` v2 paired with `BEHAVIOR-CONTRACT.md` v2. Author acceptance, not independent evaluation. No product generalization is accepted or implied.
- **Produced by:** Pi session `01a0f39e-8658-7478-ad5e-b1870bb69bd6`; runtime verified from the process environment as `commandcode / deepseek/deepseek-v4.1-flash / max`.

## Inputs used (exact hashes)

**Accepted baseline** (recorded at v1 acceptance on 2026-10-01; the baseline identity these terms and invariants were defined against, not a continuing no-change condition — see Conditions):

- **`CASE-INPUT.md`** — `sha256 50063486b149fc599464cb5cb25872cc9b4c4b971d1fcbc2eab0efdabeffd772`
- **Fixture source structure** (`src/**`, `tests/**`) — aggregate `sha256 dbd6a306815bdc4cf3a33be14b38d4dd62b49d1535d7db41b9064eb07e51b474`
  - All seven per-file hashes below were independently re-verified on 2026-10-01 against both the worktree and commit `893eaf8`:
  - `src/__init__.py` — `sha256 a5f855a87138b8c9a515d76a2b7858da6bba6fb60eff9446197fafc774733cf4`
  - `src/case_reader.py` — `sha256 89f05180854b8cb38b58299f516e7298cd2d211b88bed38f35087e6b1fe350bc`
  - `src/page_summary.py` — `sha256 59bffca2096cdb3818a202e552fa5214dd3f263466fd4799b3d7ba4e4fac2fc4`
  - `src/service.py` — `sha256 ea3fff5faf10d3025b19a07cc709985467b9dc67e607282ff1c87c73ddd66a0d`
  - `src/state_store.py` — `sha256 90a1cb56549f5afdbae24d2b485f8a956e66081939159a435aa83e2f43029196`
  - `src/turn.py` — `sha256 5de7b6c681f8379e567d9be455a3176a48c429ca460b6810092ff7ae46504ac0`
  - `tests/test_existing_behavior.py` — `sha256 9ac7ea872b8c50f921128e7a8d734539b273551e7d6e9363e3d5116103c7876f`
  - aggregate recipe: order the files under `src/**` and `tests/**` by their relative path ascending (Python `sorted()` on the path string), then emit one line per file as `<per-file sha256><two spaces><relative path>`, join the lines with `\n`, append a final `\n`, and take the sha256 of that UTF-8 text. This path order yields the recorded aggregate. Sorting the digest-prefixed lines themselves instead yields `sha256 9074f27da8e0d76113bda8f774297c7c8fbceaedaf67d6ea75eec87d2421e88c`, which is not the recorded value.
- **`BC-CHARTER.md`** (delegation) — `sha256 1395a01731f1ea4885b2e20c157ec47ba607e27fe8e2037006287562d3dd57ba`
- **`professional-workflow/profiles/behavior-domain.md`** (accepted Profile, per Charter) — `sha256 d8b75a5734c015f70d4c3f1479e094be11b92f2ee20d193dc22726fd599377fa`

## Terms

- **Case.** A tracked item identified by `case_id`, carrying exactly one current status. Case ids are opaque strings; this exercise assumes a view's case set has unique ids, and treats duplicates as outside the contract.
- **Case status.** A label on a case. This exercise defines two labels: `OPEN` (still pending) and `CLOSED` (no longer pending). A case is **open** iff its status is exactly `OPEN`. The **open count** of a view is the number of its open cases. Meaning of any other label is undefined here (DS-U1).
- **Case set.** The cases a view contains, in the presented order. This exercise does not change membership (DS-U4).
- **View (state view).** A complete assignment of one status to every case of a case set at one point in the store's history. Two views are **identical** iff they contain the same case ids, in the same order, with the same statuses.
- **Revision.** An integer tag identifying a view within one store lineage; its ordering, equality and freshness semantics are the invariants below.
- **Update (status update).** An operation naming one case id and one new status; its effect is DS-I7. An update is **completed** once its result is part of the store's history — in this single-threaded fixture, when the call returns.
- **Read episode.** As defined in `BEHAVIOR-CONTRACT.md` §Observable surface; C uses the term and does not redefine it.
- **Coherent / coherence.** A set of observations is coherent when one revision explains every observation in the set.
- **Presented view.** As defined in `BEHAVIOR-CONTRACT.md` §Observable surface; the invariants below constrain it.

## Invariants

- **DS-I1 · Episode coherence.** For any presented view, its overview observation and its details observation belong to exactly one revision. No presented view mixes two revisions.
- **DS-I2 · Count fidelity.** For any presented view, the open count equals the number of cases whose status is `OPEN` among that view's own details, and the overview's revision is the revision those details belong to.
- **DS-I3 · Monotonicity.** Within one store lineage, revision never decreases as updates complete.
- **DS-I4 · Revision identity.** Two observations with the same revision describe identical case data. If two observations show different statuses for the same case, their revisions differ, and the observation made later in time has the greater revision. (A revision may change without case data changing; case data cannot change without the revision changing.)
- **DS-I5 · Freshness.** If one or more updates completed before a read episode begins, the episode's presented view has a revision greater than or equal to the resulting revision of every such update — equivalently, a new episode cannot render older than the newest completed update at its start.
- **DS-I6 · Scope.** Revisions are comparable only within one store lineage; revisions of different stores are unrelated numbers.
- **DS-I7 · Update locality.** An update names one case id. The view after the update differs from the view before it only in that case's status when the id is present; when the id is not present, every case status is unchanged.

## Distinguishing examples

- A view over `C-1 OPEN`, `C-2 CLOSED` has open count 1: the count is derived from the same view's statuses (DS-I2), not from a separately read list.
- Revision 4 in one store and revision 4 in another store are unrelated (DS-I6).
- An update naming `C-9` (not in the set) leaves all statuses unchanged (DS-I7); whether the revision advances is DS-U2.
- Two observations showing `C-1 OPEN` and `C-1 CLOSED` cannot have the same revision (DS-I4); a presented view showing both descriptions of `C-1` is incoherent (DS-I1).

## Unresolved semantic questions (not decided here)

- **DS-U1.** Meaning and count treatment of statuses other than `OPEN`/`CLOSED`: undefined in this exercise; the seed store accepts arbitrary strings and this fixture holds no business authority to rule on them.
- **DS-U2.** Whether an update that leaves every status unchanged (unknown case id) advances the revision: not constrained. If it does, DS-I4 still holds.
- **DS-U3.** The numbering scheme (start value, step): not fixed; only the DS-I3/DS-I4 ordering and equality relations are required. The seed starts at 1 and steps by 1; the examples' numbers are illustrative.
- **DS-U4.** Case-set membership changes (creation or removal of cases): outside this exercise; if ever introduced, revision identity (DS-I4) must be re-derived for the new view type before it can be relied on.

## Change log

- **v1 · 2026-10-01** — initial accepted semantics; baseline inputs and per-file hashes recorded.
- **v2 · 2026-10-01** — challenge PC-1 bounded clarification: the recorded hashes are the acceptance **baseline**, not a continuing no-change condition on `src/**`/`tests/**`; in-scope implementation/test diffs inherit this acceptance, and only semantic changes require a new B/C version. Challenge PC-2 bounded correction: the aggregate recipe now states the sort key explicitly (path order), with the digest-line-sorted value `9074f27d…` recorded as the non-matching alternative. No term definition or invariant was changed.
