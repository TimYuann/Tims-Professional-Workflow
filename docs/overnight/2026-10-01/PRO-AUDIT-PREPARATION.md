# Pro audit preparation · M5 integration and M6 delivery

**State:** fixed review candidate is ready for Oracle's timing decision; no Pro audit has been sent and usage remains `0/2`. Oracle operates ego-browser/ChatGPT Pro/GitHub connector. M3 evidence is complete but its milestone acceptance is pending Oracle/Owner.

## Fixed object pin for Oracle's timing decision

- Repository: `https://github.com/TimYuann/Tims-Professional-Workflow.git`
- Branch: `night/2026-10-01-workflow`
- Fixed main branch review candidate, captured after both M3 F reports and the M5/M6 report checkpoint: commit `ed3120c3475339fe7140fc4afbb7fa0c1e8e5aa0`, tree `d2e91104c58777242b7f7fde4d82e31837071564`.
- The `professional-workflow/` subtree at that commit is exactly tree `c88b662421bc44270fdf38bf43267010fe0a1d38`, matching the package source object below. The commit includes M3, M5 and M6 reports. It records M3 evidence ready for acceptance; it does not record M3, M5 or M6 milestone acceptance.
- The workspace has an unrelated untracked `scan.js`; it is excluded from this committed review object and remains untouched.
- Package source object currently fixed: commit `d672914ac80eeed0aa5f04a0c80f448acc9de6f3`, tree `c88b662421bc44270fdf38bf43267010fe0a1d38`.
- Export identity: 19-file manifest SHA-256 `c40b31e87bdad8374af0bf7b393bec5583dd45deee38601e4fed324c669f1ad0`; deterministic archive SHA-256 `e2571ca9cca6148378d1b6ec1a580c0432252727e135fa0bb29f59ec23c5a39d`.

Oracle chooses whether to send the fixed object now or after its separate M3 milestone decision. If submitted, each Pro prompt must identify the exact repository, branch, commit and tree above and inspect that commit through the GitHub connector, not `main`, a web summary, or cached content. The pin includes both local M3 case reports and the M5/M6 evidence reports; it does not record M3 milestone acceptance. This preparation note and later status/decision records are outside the pinned commit and do not change the reviewed object.

## Audit 1 · M5 full integration

Read the complete `professional-workflow/` tree from the final pinned branch commit (19 files), then the integration evidence needed to judge its exact use:

- `ORACLE-ACCEPTANCE.md` M1/M4 entries and the fixed Responsibility Backbone identity.
- M1 Profile report/acceptance and M4 selected-method dossier/reviews.
- Actual Charter template/examples and selected method files in the package, including their accepted-source vs shipped-byte provenance.
- B/C v2 pair, D-accepted case-2 Plan, and both case-2 E/F reports; case-1 E/F reports and fixed candidate identity.
- `M5-PACKAGE-INDEPENDENT-REVIEW.md` and `M5-PACKAGE-REPAIR-RECHECK.md`, including the frozen M1 status-label residual.

Ask Pro to assess whether the exact shipped package and final M3 evidence support the declared integration/traceability claims, identify any remaining inconsistency or unsupported claim, and keep the review bounded to the pinned objects. Pro review does not substitute for local F or confer release authority.

## Audit 2 · M6 final delivery

Read the complete same pinned package object and the export/qualification evidence:

- `M6-PACKAGE-CANDIDATE-d672914.md`, 19-file external manifest, and deterministic archive identity.
- `M6-COLDSTART-REPORT.md` and `M6-COLDSTART-VERIFICATION.md`.
- `M6-ROLLBACK-REPORT.md` and `M6-ROLLBACK-VERIFICATION.md`.
- The final M3/M5 acceptance state and any remaining limits in `STATUS.md`/`DECISIONS.md`.

Ask Pro to assess package/export identity, startup usability, cold-start evidence, controlled-copy rollback evidence, and whether the stated limits match the evidence. Preserve the verification reports' explicit gaps: they do not prove application/database/runtime recovery, independently reproduce the recovery action, or cover every claim in the package.

## Submission controls

- At send time, visibly confirm ChatGPT 6 Pro and the GitHub connector in the composer; record model/tier evidence, connector state, conversation link, full response and disposition.
- Include the exact repository, branch, commit and tree in each prompt. The M5 and M6 requests use distinct allowance entries, even if they inspect the same fixed branch commit.
- Count an allowance only after the prompt is actually submitted. Do not substitute a non-Pro model or reset the count after a response.
- No `main`, tag, force-push, merge, UCBIP change, or production/release action is authorized by this review preparation.
