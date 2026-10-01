# M3 case 2 · record D acceptance after bounded Plan PASS

- **Owner:** `tpw-night-m3-design`; write only `fixtures/m3-snapshot/TECHNICAL-PLAN.md`.
- **Reviewed Plan:** SHA-256 `bb8afeb1d7519cac8926e1553f30e83590b8fb0504f120120c09cd916e0823d3`.
- **Independent affected-claim recheck:** `M3-SNAPSHOT-PLAN-V2-RECHECK.md`, SHA-256 `e93ac8869c2f0c94eb6b9ea8ec91a265920406656d31eacf12cee5b9a25ce278`, PASS. It records one non-blocking §8 factual wording correction; no blocker or new gate.
- **Applicable D delegation:** `fixtures/m3-snapshot/D-CHARTER.md`; fixed B/C v2 and their independent PASS are identified in the reviewed Plan and D-035.

## Task

1. In §8, replace the unqualified summary that the embedded B/C text is byte-identical to active files with a precise statement consistent with §0.1: active bindings are B/C v2; the startup prompt contains the v1 B/C copies, whose behavior/semantic body is byte-identical to v2, while the Backbone copy is the original fixed export.
2. Record D's explicit acceptance of the corrected Plan **within the delegated technical-planning scope**. Cite the reviewed predecessor hash and method PASS, and state that acceptance covers this fixture's technical Plan only; it does not accept B/C anew, evaluate/accept implementation, close M3, or authorize any deployment/UCBIP/release action. Do not add a new approval gate beyond the existing D responsibility.
3. Make no other content changes. Do not modify B/C, Charter, implementation, tests, STATUS, DECISIONS, or any other file. Do not start E/F.
4. Return the final Plan SHA-256 and state that the only changes from the reviewed candidate were the §8 correction and D acceptance record. Driver will verify this exact narrow diff; the method report already classifies the wording item as non-blocking, so no new method round is requested unless the diff exceeds this scope.
