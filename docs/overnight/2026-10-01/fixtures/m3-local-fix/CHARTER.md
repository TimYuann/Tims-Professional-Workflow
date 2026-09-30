# M3 case 1 · active exercise Charter

- **State:** active for this isolated M3 exercise only
- **Profile:** `professional-workflow/profiles/implementation.md` (M1 accepted; SHA-256 `c96162668a1b80096c872a79321e07111a7eecc346f037f7060834f272b0aa5f`)
- **Instance:** `tpw-night-m3-local-impl`

## Task and delegation

- **Task / outcome:** Repair the known local `normalize_label` defect while preserving the fixture's accepted behavior and public function/error contract.
- **Delegation source:** Owner-authorized offline exercise in `docs/OVERNIGHT-WORKFLOW-PLAN-2026-10-01.md` at plan baseline `496b0676e302e2d0eafba129ff61de4c203d258a`, M3 case 1. Driver issues this Charter only for the synthetic fixture, not for any business product.
- **Object scope:** In `fixtures/m3-local-fix/`, implementation may change `src/labels.py` and may add tests under `tests/`. The fixture contract, task input and baseline observation are read-only evidence. Do not modify other fixture directories or package Profiles.
- **Accepted inputs:** `CONTRACT.md` (`ecfc6195726fe62321208ad766fcbe7005c784c6d2aece7f9b2a2eca4ef293bb`), `TASK-INPUT.md` (`90b7e06d06e525e79a58496cdf65603f15da18f15809a7e1e3a256a1f904167e`), and pre-change `BASELINE.md` (`6e8262b6361be36abc39947cf00fef02adac9c9120f353e5b38070c84e119a57`). For this offline exercise, Driver is the fixture maintainer for the synthetic contract; this does not create or alter product behavior authority.

## Work and limits

- **Responsibility:** Implement the local repair and report the observed result and any deviation.
- **Delegated decisions:** Choose the local algorithm and add a focused test if useful, while the cited contract and function boundary remain unchanged.
- **Preserve / do not do:** Keep the function signature, output/error behavior, contract and recorded baseline intact. Do not redesign shared interfaces, change domain meaning, touch production data, access UCBIP or cause external effects.
- **Tools and actions:** Python standard-library commands from this fixture only; no network or package installation.

## Handoff and return

- **Deliver:** Candidate patch, exact verification command/output, changed paths, and unresolved facts.
- **Independence:** `tpw-night-method` evaluates the resulting version after implementation. The implementer's self-check is evidence input, not an independent conclusion.
- **Recall:** If the cited contract is contradictory or cannot be kept inside this grant, send Driver the affected object, fact and impact before crossing its boundary; pause only work depending on that issue.
- **Acceptance / verification / action / closure:** The evaluator reports evidence for this fixture only. Driver integrates the candidate; M3 milestone acceptance remains with Oracle under the accepted overnight plan. This Charter grants no release, deployment, migration or broader task closure authority.
