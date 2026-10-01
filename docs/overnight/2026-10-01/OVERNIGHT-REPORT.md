# Overnight M0–M6 report · 2026-10-01

**Overall state:** local evidence and M5/M6 review materials are prepared. Oracle/Owner acceptance and the two authorized Pro reviews are still pending. This report does not declare the overnight workflow closed.

## Milestones

| Milestone | Current result | Self-contained evidence |
| --- | --- | --- |
| M0 | PASS; the opening branch, inputs, and preservation state are recorded. | `STATUS.md`, `DECISIONS.md` |
| M1 | ACCEPTED by Oracle; the original Profile review FAIL and narrow correction remain preserved. | `M1-REPORT.md`, `PROFILE-EVALUATION.md`, `ORACLE-ACCEPTANCE.md` |
| M2 | Charter/template design and case-1 method-bound activation were exercised. Package-wide runtime/cold-start claims remain limited to their fixed samples. | `STATUS.md`, M2 design checkpoint `97c51bc`, case-1 E/F reports |
| M3 | Oracle accepted both fixed case results and the case-2 Turn presented-view boundary. Overall M3 remains open pending disposition of the post-ruling no-side-effect authorization observation and the material-separation question. | `ORACLE-ACCEPTANCE.md`; `M3-REPORT.md`; `M3-AUTHORITY-BOUNDARY-OBSERVATION.md` |
| M4 | ACCEPTED by Oracle for the three bounded methods and selection entry at fixed M4 commit/tree. | `METHOD-CANDIDATES.md`, `METHOD-REVIEW.md`, `ORACLE-ACCEPTANCE.md` |
| M5 | Fixed package candidate `d672914` has an independent targeted F1–F4 PASS. Full-object/Pro acceptance remains open. | `M5-REPORT.md`, `M5-PACKAGE-REPAIR-RECHECK.md` |
| M6 | The 19-file export has independent case-1 cold-start sample PASS and controlled-copy rollback evidence PASS. Full M6/Pro acceptance remains open. | `M6-REPORT.md`, `M6-PACKAGE-CANDIDATE-d672914.md`, cold-start and rollback reports/verifications |

## Fixed candidates and evidence

- M5/M6 package source: commit `d672914ac80eeed0aa5f04a0c80f448acc9de6f3`, repository root tree `c88b662421bc44270fdf38bf43267010fe0a1d38`, and `professional-workflow/` package subtree `9e4fa14a427f42dc2fc6304a08fa76fd7596313e`.
- M5/M6 export: 19-file manifest SHA-256 `c40b31e87bdad8374af0bf7b393bec5583dd45deee38601e4fed324c669f1ad0`; archive SHA-256 `e2571ca9cca6148378d1b6ec1a580c0432252727e135fa0bb29f59ec23c5a39d`.
- M3 case 1 F PASS applies only to implementation commit `9699276ab1d413379ace91afa0cf683a83b69aa3`. The bound E revalidation reports no code/test changes. Residual: “whitespace” is not Unicode-enumerated in the contract; E's use of Python `str.split()` is preserved as an unresolved edge.
- M3 case 2 E candidate: commit `17602f2b12822aba88785e27a733f75a3238214d`, tree `f9b4f90b9e5a0c7ae11dfe681b82a4a22dddef03`; E report SHA-256 `557c1ed51e5c9b8c951b1e68a01b318160126ac63924c960b6e1b0c9dd298aed`; independent F report SHA-256 `406b9efc56e60bc88cc9da28061427b660171866f285bd5cd802055cb3a0dacb` is PASS for the recorded Turn presented-view entry.
- The earlier M5/M6 Pro candidate `ed3120c` is superseded. `DRIVER-HANDOFF.md` fixes the review candidate commit/tree; the latest branch tip adds only the final pin and handoff/status records, and its exact HEAD/tree are returned in the completion notice. The package source identity remains `d672914` root tree `c88b662…` / package subtree `9e4fa14…`.

## Cost and remaining limits

- M3 used six unique named sessions: Driver, B/C author, D author, E author, case-1 method-bound E, and F/method evaluator. The E author and method/F evaluator identities were reused across both cases; workspace migration created no new independence.
- M3 records 12 inter-role artifact handoffs, one post-ruling request/response observation, and the report delivery to Oracle. Oracle's fixed baseline is 34 selected M3 Markdown artifacts / 437,182 bytes; the separately added authority-observation report is 5,319 bytes. The earlier E/F startup packets are 97,850 / 115,048 bytes. These figures exclude source/test bytes, package Profile/Backbone bytes, and private F criteria. Oracle did not accept the material load as lightweight; no combined count is asserted because the additional observation is a separately scoped decision record. No unnecessary authority recall was identified. One malformed initial Herdr E prompt was corrected before work began.
- Exact implementation and coordination wall-clock time and per-session token totals were not captured. The M3 report marks those figures UNVERIFIED and does not infer them from test-runner timing.
- Case 2 F PASS does not cover the legacy `start(store)` plus separate `service.cases(store)` two-read composition, which can observe mixed revisions. It covers the D-accepted `Turn` presented-view entry. No concurrency, persistence, production, UCBIP, or release behavior is established.
- M5 residual: a frozen M1 “待 M4” label remains visible in an assembled E prompt; the package README supersedes it for selected methods and the adjacent Charter pins both method versions.
- M6 rollback evidence is limited to a controlled package copy. It does not prove application/database/runtime restoration or independently replay the restoration action; the verification report records its scratch-state gaps.
- At the 03:52 pause, the planned 08:00 closure target was unmet. Later M3/M5/M6 evidence does not rewrite that outcome. No Pro review has been submitted (`0/2`). Oracle pushed prior branch checkpoint `96114e1a97227e7d1541965c89bb91deb860866b` with matching remote readback; the present checkpoint still awaits Owner/Oracle push. No tag, merge, UCBIP change, or release action occurred.

## Next actions

1. Oracle decides whether the post-ruling authorization observation closes the overall M3 boundary gap and submits the fixed candidate for the first Pro review.
2. Preserve the current package candidate; consume Pro allowance `1/2` only after the actual submission and record the exact response/disposition.
3. New Driver resumes after Oracle's push/readback and first Pro response; use the fixed pins and bounded next actions in `DRIVER-HANDOFF.md`.
