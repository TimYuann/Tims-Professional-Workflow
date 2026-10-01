# Overnight M0–M6 report · 2026-10-01

**Overall state:** local evidence and M5/M6 review materials are prepared. Oracle/Owner acceptance and the two authorized Pro reviews are still pending. This report does not declare the overnight workflow closed.

## Milestones

| Milestone | Current result | Self-contained evidence |
| --- | --- | --- |
| M0 | PASS; the opening branch, inputs, and preservation state are recorded. | `STATUS.md`, `DECISIONS.md` |
| M1 | ACCEPTED by Oracle; the original Profile review FAIL and narrow correction remain preserved. | `M1-REPORT.md`, `PROFILE-EVALUATION.md`, `ORACLE-ACCEPTANCE.md` |
| M2 | Charter/template design and case-1 method-bound activation were exercised. Package-wide runtime/cold-start claims remain limited to their fixed samples. | `STATUS.md`, M2 design checkpoint `97c51bc`, case-1 E/F reports |
| M3 | Both local cases have independent F PASS results on fixed objects. The integrated milestone report is ready for Oracle/Owner acceptance; acceptance is not yet recorded. | `M3-REPORT.md` SHA-256 `c8cac65c835604b0d6f67059d88d90f9fc8d92d4a605b7d365260247baf60915` |
| M4 | ACCEPTED by Oracle for the three bounded methods and selection entry at fixed M4 commit/tree. | `METHOD-CANDIDATES.md`, `METHOD-REVIEW.md`, `ORACLE-ACCEPTANCE.md` |
| M5 | Fixed package candidate `d672914` has an independent targeted F1–F4 PASS. Full-object/Pro acceptance remains open. | `M5-REPORT.md`, `M5-PACKAGE-REPAIR-RECHECK.md` |
| M6 | The 19-file export has independent case-1 cold-start sample PASS and controlled-copy rollback evidence PASS. Full M6/Pro acceptance remains open. | `M6-REPORT.md`, `M6-PACKAGE-CANDIDATE-d672914.md`, cold-start and rollback reports/verifications |

## Fixed candidates and evidence

- M5/M6 package source: commit `d672914ac80eeed0aa5f04a0c80f448acc9de6f3`, tree `c88b662421bc44270fdf38bf43267010fe0a1d38`.
- M5/M6 export: 19-file manifest SHA-256 `c40b31e87bdad8374af0bf7b393bec5583dd45deee38601e4fed324c669f1ad0`; archive SHA-256 `e2571ca9cca6148378d1b6ec1a580c0432252727e135fa0bb29f59ec23c5a39d`.
- M3 case 1 F PASS applies only to implementation commit `9699276ab1d413379ace91afa0cf683a83b69aa3`. The bound E revalidation reports no code/test changes. Residual: “whitespace” is not Unicode-enumerated in the contract; E's use of Python `str.split()` is preserved as an unresolved edge.
- M3 case 2 E candidate: commit `17602f2b12822aba88785e27a733f75a3238214d`, tree `f9b4f90b9e5a0c7ae11dfe681b82a4a22dddef03`; E report SHA-256 `557c1ed51e5c9b8c951b1e68a01b318160126ac63924c960b6e1b0c9dd298aed`; independent F report SHA-256 `406b9efc56e60bc88cc9da28061427b660171866f285bd5cd802055cb3a0dacb` is PASS for the recorded Turn presented-view entry.
- The M5/M6 Pro review candidate is branch `night/2026-10-01-workflow`, commit `ed3120c3475339fe7140fc4afbb7fa0c1e8e5aa0`, tree `d2e91104c58777242b7f7fde4d82e31837071564`. Its `professional-workflow/` subtree matches the `d672914` source tree. It includes the M3, M5, and M6 reports and is pinned in `DECISIONS.md` D-049 and `PRO-AUDIT-PREPARATION.md`.

## Cost and remaining limits

- M3 used six unique named sessions: Driver, B/C author, D author, E author, case-1 method-bound E, and F/method evaluator. The E author and method/F evaluator identities were reused across both cases; workspace migration created no new independence.
- M3's recorded count is 12 inter-role artifact handoffs plus the final Oracle delivery. Thirty-four selected M3 Markdown artifacts total 437,182 bytes, excluding source/test bytes, package Profile/Backbone bytes, and private F criteria. No unnecessary authority recall was identified. One malformed initial Herdr E prompt was corrected before work began.
- Exact implementation and coordination wall-clock time and per-session token totals were not captured. The M3 report marks those figures UNVERIFIED and does not infer them from test-runner timing.
- Case 2 F PASS does not cover the legacy `start(store)` plus separate `service.cases(store)` two-read composition, which can observe mixed revisions. It covers the D-accepted `Turn` presented-view entry. No concurrency, persistence, production, UCBIP, or release behavior is established.
- M5 residual: a frozen M1 “待 M4” label remains visible in an assembled E prompt; the package README supersedes it for selected methods and the adjacent Charter pins both method versions.
- M6 rollback evidence is limited to a controlled package copy. It does not prove application/database/runtime restoration or independently replay the restoration action; the verification report records its scratch-state gaps.
- At the 03:52 pause, the planned 08:00 closure target was unmet. Later M3/M5/M6 evidence does not rewrite that outcome. No Pro review was submitted (`0/2`), and no branch push, tag, merge, UCBIP change, or release action occurred.

## Next actions

1. Oracle/Owner decides M3 milestone acceptance using `M3-REPORT.md`.
2. Oracle chooses whether and when to use the two Pro reviews on the pinned M5/M6 candidate; the preparation brief contains the exact read lists and submission controls.
3. Record the Pro responses and bounded dispositions before changing any accepted package object. Preserve the current candidate hashes and all stated limitations meanwhile.
