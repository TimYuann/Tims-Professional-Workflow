# M6 · case-1 cold-start run report

- **Session:** fresh session, no prior Driver/M3 conversation history.
- **Workspace:** `/private/tmp/tpw-m6-coldstart-d672914/` (clean disposable fixture).
- **Instruction read first:** `/private/tmp/tpw-night-20261001/docs/overnight/2026-10-01/M6-COLDSTART-PROMPT.md`, verified SHA-256 `ab32fdb6ddba45201c2672be7df2bb12b162114f746b7992300b21bc28bd122c` (matches the fixed hash).
- **Isolation observed:** no old role/compose/history files, M3 E/F reports, evaluator criteria, Git session history, UCBIP, or production data were read. Reads were limited to `professional-workflow/` and `case1/`. No network, installation, or external effects.
- This is candidate cold-start evidence only, not independent F evaluation or M6 acceptance.

## 1. Startup selection

Started at `professional-workflow/README.md`; consulted `profiles/README.md`, `methods/README.md`, `charters/README.md`, `authority/README.md`, and `authority/RESPONSIBILITY-BACKBONE.md`, then bound the task through the fixed case-1 Charter.

| Role | Object actually used | SHA-256 | Why |
| --- | --- | --- | --- |
| Profile | `professional-workflow/profiles/implementation.md` (E) | `c96162668a1b80096c872a79321e07111a7eecc346f037f7060834f272b0aa5f` | Task is "produce the result inside an accepted commitment": one known local defect, fixed contract, fixed public boundary. E's interior autonomy covers local algorithm and test seam. |
| Method | `professional-workflow/methods/local-defect-feedback-loop.md` | `1ba8f8f2fb46a0094c22e7ac946e27f30a27b1ce25e201fd5ede819ddc2e4215` (M5 candidate bytes, matches the digest published in `methods/README.md`); accepted M4 body digest `3ca23a74a1a1890123bbab01a114aba813d7e20a7ffcb21b7b2289d5047cb32c` | Selection entry maps "Reproduce and repair a known local defect" to this file. M5 shipped bytes are a package-status/source-trace derivative of the M4-accepted body; the digest I bound is the shipped one above. |
| Charter | `case1/M6-COLDSTART-CHARTER.md` (filled instance form) | `2da085ba8bd976973f84ba257fd946cc41bbadceed58b4e07b9c43db892dfd15` | The actual fixed delegation for this instance. `charters/template.md` and `charters/examples/implementation-local-fix.md` were read as the binding form / design reference only, not as grants. |
| Selection entry | `professional-workflow/methods/README.md` | `24de9ce294c682afd7c9930a1000b2c5b37fb5a518edb34e3544b21ba6c87538` | Owns method selection; the accepted M4 selection entry had SHA-256 `72a6ffb46277e3974f27d41e078623ce5b46865074898dae24cbdb6de2205e73`; this is the M5 package-status derivative. |
| Package entry | `professional-workflow/README.md` | `2aad8921a4feb679995c85e3ef9ffe23d10ef02e022e716e407a2ba70349cef4` | Assembly instruction: Profile → authority context → Charter → bound method files → task input. |

**Profile combination decision:** `evidence-evaluation.md` (F, `d72b3a5097f142f5ea397ab423b146a3b853913c5c1de096d93b95133199f900`) was intentionally **not** bound in this instance. The Charter and Backbone §3/§6 require the F conclusion to come from a verifier that is not the implementer; E self-checks are "可核对输入" only (`profiles/implementation.md`; Backbone §3 F). This session is E, so its test outputs are handed to the separate verifier, not used as an independent conclusion.

**Assembly actually used** (startup text order; the fixed Charter and case-1 inputs replace the illustrative ones):

```sh
cat professional-workflow/profiles/implementation.md \
    professional-workflow/authority/RESPONSIBILITY-BACKBONE.md \
    case1/M6-COLDSTART-CHARTER.md \
    professional-workflow/methods/local-defect-feedback-loop.md \
    case1/CONTRACT.md case1/TASK-INPUT.md case1/BASELINE.md \
    case1/src/labels.py case1/src/__init__.py case1/tests/test_labels.py
```

## 2. Charter authority, limits, and recall (as located and applied)

- **Delegation source:** owner-authorized M3 case 1 offline exercise at plan baseline `496b0676e302e2d0eafba129ff61de4c203d258a`; this M6 rehearsal reuses that authority in a disposable copy. It grants no product, production, UCBIP, release, deployment, or migration authority.
- **Object scope applied:** read the fixed inputs, seed source/tests, and `../professional-workflow/`; write only `src/labels.py` and files under `tests/` in `case1/`. The package and all fixed inputs were not edited (hashes below confirm).
- **Delegated decisions used:** local collapse algorithm; regression-test seam and cases.
- **Preserve / not done:** contract, function signature, `TypeError` type, punctuation-preserving uppercase, public behavior; no interface redesign, no dependency change, no external effects; existing test expectations not weakened (supplied `tests/test_labels.py` untouched).
- **Recall path (Backbone §3 E and §4):** local defects stay with E; if the accepted contract could not be preserved or the delegation had to be crossed, I would record the affected object/fact/impact and return it through Driver to the authority owning that boundary, using Voice only for a human-reserved decision. No recall was triggered — the contract could be preserved inside the granted scope.
- **Closure boundary (Backbone §2/§4; Charter "Independence / closure"):** acceptance, verification, action authorization, and closure are separate. The separate verifier evaluates the fixed bytes; my self-check neither accepts the candidate nor authorizes release or closure.

## 3. Inputs verified before use

All fixed hashes matched the cold-start instruction and the Charter:

| Input | SHA-256 |
| --- | --- |
| `case1/M6-COLDSTART-CHARTER.md` | `2da085ba8bd976973f84ba257fd946cc41bbadceed58b4e07b9c43db892dfd15` |
| `case1/M6-COLDSTART-INVITATION.md` | `100b39261b03e1665ae6bf093b8ba6d128455d9cd30d31a229c5e52b15c095a1` |
| `case1/CONTRACT.md` | `ecfc6195726fe62321208ad766fcbe7005c784c6d2aece7f9b2a2eca4ef293bb` |
| `case1/TASK-INPUT.md` | `90b7e06d06e525e79a58496cdf65603f15da18f15809a7e1e3a256a1f904167e` |
| `case1/BASELINE.md` | `6e8262b6361be36abc39947cf00fef02adac9c9120f353e5b38070c84e119a57` |
| seed `case1/src/__init__.py` | `01668323d7700904ad3ff81941a8c1beaf0b22fe2ccbf96d2749689d64cc576e` |
| seed `case1/src/labels.py` (pre-fix) | `0507c9e7f1f297d69a050b2f6ff96ce75fb00829aead1739666d8d2bcad50e49` |
| seed `case1/tests/test_labels.py` | `8dbf28589f9e4ce34cc36aa87df88a8aeed63cb260214d3bf1997f0fe396bb06` |
| Backbone projection | `ce82a70016a4a3fc234ea287f39aac8d79a260ddf13747c4fb705bda580453ba` (matches its recorded source digest) |
| Other package files used | `profiles/README.md` `2e103f2f…49711`; `charters/README.md` `035f2a1f…6439`; `charters/template.md` `f03cc007…0cdb`; `charters/examples/implementation-local-fix.md` `038e6a31…3cc1`; `authority/README.md` `e509641d…89b7`; `methods/README.md` `24de9ce2…7538`; `profiles/evidence-evaluation.md` `d72b3a50…f900` |

## 4. Commands, exits, results

Environment: Python 3.14.4 (matches BASELINE.md), run from `case1/`.

1. **Baseline reproduction before any change**
   `python3 -m unittest discover -s tests -v`
   Exit `1`; 4 tests ran, 3 passed; `test_collapses_internal_whitespace` failed with `'NORTHERN   STAR' != 'NORTHERN STAR'` for input `" \tNorthern   Star\n"`. This matches BASELINE.md exactly (deterministic, local).

2. **Method step 3 — bounded falsification of candidate repairs** (read-only inline script, same 4 contract cases):
   - C1 current `strip().upper()` → fails `" \tNorthern   Star\n"` (the reported defect).
   - C2 `" ".join(value.split()).upper()` → passes all 4.
   - C3 `"".join(value.split()).upper()` (remove-all) → fails `" \tNorthern   Star\n"` and `"north star"` (would delete a legitimate single space), falsified by the contract's "collapse to one ASCII space".
   - C4 `re.sub(r"\s+", " ", value).strip().upper()` → passes all 4.
   C2 chosen over C4: same stdlib whitespace class as the existing `strip()`, no import, smallest diff.

3. **Repair applied** to `src/labels.py`: `value.strip().upper()` → `" ".join(value.split()).upper()`. One line; nothing else changed.

4. **Rerun on the candidate**
   `python3 -m unittest discover -s tests -v`
   Exit `0`; **7 tests ran, all passed (OK)** in 0.000s — the original 4 plus 3 new regression tests.

5. **Direct original failing scenario**
   `python3 -c "from src.labels import normalize_label; print(repr(normalize_label(' \tNorthern   Star\n')))"`
   Exit `0`; output `'NORTHERN STAR'`.

6. **Fixed-input immutability recheck after writing**
   `shasum -a 256` of `CONTRACT.md`, `TASK-INPUT.md`, `BASELINE.md`, both cold-start prompts, `src/__init__.py`, `tests/test_labels.py` — all identical to §3. Package directory untouched.

## 5. Changed paths

| Path | Change | SHA-256 after |
| --- | --- | --- |
| `case1/src/labels.py` | single line: `value.strip().upper()` → `" ".join(value.split()).upper()` (whitespace runs collapse to one ASCII space; leading/trailing removal and `TypeError` preserved) | `f767787ba2ac8cf52e7b4f62e74b146b858fad91031bed139c849c9e23a92f87` |
| `case1/tests/test_labels_regression.py` | new: mixed internal whitespace collapse; single internal space preserved (negative control against remove-all); already-normalized input unchanged | `a60868486e9652bf8c83fe4ff661654ed80df34d78227fde26f1d8e9280ece5f` |

No other file was written. The supplied `tests/test_labels.py` was intentionally left byte-identical (not weakened).

## 6. Remaining facts, unresolved semantics, deviations

- **Unresolved semantics — whitespace class:** the contract says "whitespace" without enumerating characters. The chosen implementation uses Python `str.split()` semantics, i.e. the same `str.isspace()` class the pre-existing `strip()` used (this includes non-ASCII whitespace such as NBSP, which the observable evidence does not cover). Behavior for those characters is therefore inherited, not newly decided; only `space`, `\t`, `\n` appear in the accepted evidence. Flagging for the verifier; no redesign, consistent with TASK-INPUT.md's "no D redesign requested".
- **Unresolved semantics — uppercase mapping:** contract says "uppercase"; `str.upper()` preserves its existing Python semantics (including length-changing mappings such as `ß` → `SS`). Unchanged by this repair and not exercised by the tests.
- **Order equivalence:** contract orders strip → collapse → uppercase; the fix does split/join → uppercase. For the covered cases the orders are observably equivalent (case mapping does not move characters across the whitespace/non-whitespace boundary); verified by the passing suite.
- **Path deviation (no action taken):** the Charter's delegation text cites the disposable copy at `/private/tmp/tpw-m6-export-d672914/case1/`, while the actual workspace is `/private/tmp/tpw-m6-coldstart-d672914/case1/` (fixed by the cold-start instruction's package/workspace paths). Same authority, same fixture roles, different rehearsal directory name. I recorded it rather than resolving it, since the write set forbids touching the package and fixed inputs and the authority itself is unchanged.
- **Not evidence of acceptance:** passing self-checks are E observations handed to the separate verifier. The candidate bytes above are what a verifier should evaluate; this report does not claim PASS, closure, or release.
