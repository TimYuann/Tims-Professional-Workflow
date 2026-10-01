# M3 case 2 · F independent evaluation Charter

- **State:** active for evaluating the fixed case-2 E candidate only; this Charter records Owner-authorized verification and adds no publication authority.
- **Profile:** `professional-workflow/profiles/evidence-evaluation.md`, SHA-256 `d72b3a5097f142f5ea397ab423b146a3b853913c5c1de096d93b95133199f900` (M1-accepted Profile).
- **Instance:** `tpw-night-method` (Codex / gpt-6.1-sol / medium), independent of E author session `tpw-night-m3-local-impl`.

## Task and delegation

- **Task / outcome:** Independently evaluate the fixed case-2 implementation candidate against the accepted B/C behavior/domain claims and D Plan, applying the case-2 evaluation criteria held for this F instance. Return a three-state result and an auditable evidence report.
- **Delegation source:** Owner-authorized M3–M6 overnight exercise and the accepted case-2 input chain: B/C v2 (owner-accepted and independently reviewed), D-accepted Plan, and fixed E candidate. The Charter records the existing F responsibility; writing it does not create acceptance authority.
- **Object scope:** Read only the fixed candidate commit/tree and the public evidence listed in the startup packet. Do not edit the implementation, tests, B/C, Plan, Profiles, Charters, or any package file. May write only `M3-CASE2-F-EVALUATION.md`.
- **Accepted inputs:** B/C v2 (`6cf43d3f…` / `d35766b4…`), D-accepted Plan (`a3062057…`), and E candidate commit `17602f2b12822aba88785e27a733f75a3238214d`, tree `f9b4f90b9e5a0c7ae11dfe681b82a4a22dddef03`. Candidate file hashes and E self-report are fixed in the startup packet.
- **Applicable method:** `behavior-claim-evaluation.md` from M4 accepted commit `013659331c8c5f9f54b866b393972a03d7938773`, SHA-256 `06b0692290a9ce8cdc7048b33a89ec21f3636ee00138a613121ec4b72457af06`. It is a bounded baseline/treatment method, not a complete F workflow; its exact accepted body is included in the startup packet.

## Work and limits

- **Responsibility:** Apply the held case-2 criteria to this exact E candidate; assess the specified claims, evidence validity and coverage. Independently reproduce observations needed for a verdict; treat E's report as input, not as an F conclusion.
- **Verdict:** Use only `PASS`, `FAIL`, or `UNVERIFIED` with the accepted method's mapping. An invalid comparison or environment limitation is `UNVERIFIED`, not product `FAIL`.
- **Confidentiality/isolation:** The case-2 rubric is held by this F session and is not included in the E Charter, E startup packet, source/test files, or shared repository. Do not reproduce, quote, or expose the private criteria in the report. If the held criteria are not available in this session's context, do not infer or request them from E; return `UNVERIFIED` and state the missing-input limit without revealing private content. Report evidence and rationale in terms of public B/C and Plan claims.
- **Tools and actions:** Offline fixture only. Local test execution and ephemeral read-only copies of fixed Git objects are allowed for baseline/treatment comparison. Do not change the main candidate or any package/verification copy. No network, UCBIP, deployment, migration, release, push, merge, or commit.

## Handoff and return

- **Deliver:** `M3-CASE2-F-EVALUATION.md` with exact candidate identity, inputs and hashes, commands/results, claim-level evidence, verdict, coverage and limitations. Do not claim overall M3 acceptance.
- **Independence:** E implementation was authored by a different session. This F instance previously reviewed B/C and challenged the D Plan but did not author the case-2 implementation. Workspace migration adds no independence.
- **Acceptance / closure:** F owns the independent case result only. Driver integrates the evidence; Oracle/Owner milestone acceptance remains separate. F does not accept the D Plan, residual risk, or overall M3.
