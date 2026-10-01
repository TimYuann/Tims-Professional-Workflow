# M5 · Independent Package-Use and Isolation Review

- **Reviewer:** fresh independent instance; no Driver session history, decision ledger, or prior review note was consulted.
- **Review basis:** `docs/overnight/2026-10-01/M5-PACKAGE-REVIEW-PROMPT.md`, SHA-256 `f35989cf7a730ceb73fd49074262fe702e11066bcabb2623ef5f29a9ddb9a5e3` (recorded value re-verified; matches).
- **Fixed object:** commit `f11de8b4b35015b14dfc50dd94d19525e424cd07`, tree `252093659181f0fd73e8ef6f9316e0778f524961`, package root `professional-workflow/` (19 files, all `.md`).
- **Working method:** `git archive f11de8b… professional-workflow | tar -x` into a temporary directory; all reads, link checks, hash checks, and the assembly smoke were performed against that extraction of the fixed tree. No package file, fixture, ledger, or source checkout was modified. The only write is this report.
- **Repo state observed:** at review time the worktree HEAD was `0299f28`; `git diff f11de8b 0299f28 -- professional-workflow/` is empty, so the fixed package equals the current packaged state in this checkout.
- **Result framing:** each check below is reported separately. This is a partial M5 package-use/isolation review and gives no whole-M5/M6 verdict.

## Checks and results

### 1. Object identity — PASS

| Claim | Observed |
| --- | --- |
| `f11de8b…` is a commit | `git cat-file -t` → `commit` |
| Tree equals `252093659181f0fd73e8ef6f9316e0778f524961` | `git rev-parse f11de8b^{tree}` → exact match |
| Package root `professional-workflow/`, 19 files | `git ls-tree -r f11de8b -- professional-workflow/` → 19 entries |
| Message | `docs: close self-contained M5 package entry` |

### 2. In-package links — PASS

All 5 relative Markdown links across the package resolve inside the package (authority link, authority README link, profiles/charters/methods entries from the root README). 0 external URLs are used as required links. Code-span path references (`../authority/`, `methods/*.md`) use package-root-relative paths and resolve from the package root. No reference requires a file outside the package for normal reading.

### 3. Documented text-assembly smoke with synthetic input — PASS

Both documented assemblies were run from the package root with a synthetic task input placed outside the package:

| Documented path | Command source | Output | Result |
| --- | --- | --- | --- |
| E implementation | `professional-workflow/README.md` §Use step 4; `charters/README.md` §Assembly | 8,869 bytes | Assembled, no `path/to/` placeholder, no external file needed |
| D technical planning | `charters/README.md` §Assembly (with Backbone) | 31,540 bytes | Assembled, same |

- Only residual placeholders are the example charters' `- **Instance:** \`<implementation instance>\`` / `<planning instance>` fields, which the README instructs the user to replace with fixed task-specific objects.
- The assembled startup text requires no script, network, or package-external file; all referenced content comes from the package plus the supplied task input.
- Minor observation (not a defect): the E assembly names Driver, Voice, and F for routing/independence without defining them locally. The README says to consult/include the bundled Backbone "when a responsibility boundary matters", so this is a documented composition choice, not a missing in-package definition.

### 4. Backbone source/export identity — PASS

`authority/RESPONSIBILITY-BACKBONE.md` is byte-identical to its recorded source:

| Field | Recorded in `authority/README.md` | Observed |
| --- | --- | --- |
| Source commit | `a77c3974128cee6059b1662579e3803fc1bdfcb9` | commit exists; tree `0a84b498…` matches the recorded source tree |
| Source path | `docs/RESPONSIBILITY-BACKBONE.md` | exists at that commit |
| Source SHA-256 | `ce82a70016a4a3fc234ea287f39aac8d79a260ddf13747c4fb705bda580453ba` | match |
| Export SHA-256 | same value | match on `authority/RESPONSIBILITY-BACKBONE.md` |

Both paths also carry the identical Git blob `6cb486e5f9897fdff2d3c03f687aac987771f7e1`, confirming exact-projection byte identity. The package README's "source commit and digest are recorded" claim holds.

### 5. Profile provenance — PASS with a status-text caveat (Finding F2)

All seven `profiles/` files are byte-identical to checkpoint `429a78b` (`feat: checkpoint accepted M1 professional profiles`), so the README's "Profile content is the M1 accepted input at checkpoint 429a78b" is true as a provenance location. However, the frozen profile text still self-describes as candidate/pending-M4 while the package now declares M4 method acceptance (F2 below).

### 6. Method acceptance and pin traceability — FAIL (Finding F1)

The shipped method bodies do not match the recorded acceptance tree, and the pinned digests in the example charters do not match the shipped files:

| Shipped file at `f11de8b` | Shipped SHA-256 | Recorded M4 value (tree `2fc8db5e…` / commit `0136593…`) | Cited in package as |
| --- | --- | --- | --- |
| `methods/local-defect-feedback-loop.md` | `1ba8f8f2fb46a0094c22e7ac946e27f30a27b1ce25e201fd5ede819ddc2e4215` | `3ca23a74a1a1890123bbab01a114aba813d7e20a7ffcb21b7b2289d5047cb32c` | `charters/examples/implementation-local-fix.md:13` |
| `methods/cross-module-design.md` | `ab0a0bc03448407479fe82b92b2355384e7f2acf49c2ff3026882670f955a0a5` | `30066c8b3ccee2b85e98c8bc36975f57161e2c93d0bd71c9c668b27bf79bae6f` | `charters/examples/technical-planning-cross-module.md:13` |
| `methods/behavior-claim-evaluation.md` | `cfacc0f57cedadc6360ad0338645e43740dad4b1e15cc6876088eb89b4034f02` | `06b0692290a9ce8cdc7048b33a89ec21f3636ee00138a613121ec4b72457af06` | no digest cited anywhere in the package |

- `methods/README.md:13` and `README.md:23` both state the three method bodies and selection entry were "accepted from M4 commit `0136593…`, tree `2fc8db5e…`". That tree's bytes differ from every shipped method file (and the shipped selection entry itself differs from the M4 entry, `72a6ffb4…`).
- The two digest pins that a task Charter would use to verify its bound method both fail against the shipped files. `behavior-claim-evaluation.md` has no pin at all, so F's method cannot be digest-bound from the package.
- Content delta is small and traceable: `git diff 0136593 f11de8b -- professional-workflow/methods/` shows only the status/header relabeling (`M4 candidate` → `M4 accepted reference`, status sentence) plus the removal of one sentence pointing at the overnight dossier in `cross-module-design.md`. The distilled method steps are unchanged. The defect is therefore version identity, not method content: the package's own pins cannot verify what it ships. The M5 integration commits (`1382b3f`, `f11de8b`) are neither recorded nor given their own digests inside the package. Whether an acceptance decision for the integrated bytes exists outside the package is outside this review's read set.

### 7. Upstream method source pins and anchors — PASS

| Pinned upstream (read-only check) | Result |
| --- | --- |
| `mattpocock/skills` `c55ee460…` — `diagnosing-bugs/SKILL.md`, `codebase-design/SKILL.md`, `codebase-design/DEEPENING.md` | commit resolves; paths exist |
| `addyosmani/agent-skills` `2686b620…` — `debugging-and-error-recovery/SKILL.md`, `api-and-interface-design/SKILL.md` | commit resolves; paths exist |
| `cursor/plugins` `ecc249f1…` — `cursor-team-kit/skills/verify-this/SKILL.md` | commit resolves; path exists |

Named anchors exist at the pinned revisions: `Glossary`, `Principles`; `Dependency categories`, `Testing strategy: replace, don't layer`; `Contract First`, `Consistent Error Semantics`, `Prefer Addition Over Modification`; `Workflow`, `Verdict Rules`, `Output`. The `methods/README.md` source table's "used by" mapping matches the anchor tables inside the method files. (This confirms anchor existence/path traceability, not the semantic fidelity of each distillation.)

### 8. Dependency on legacy roles/phases/scripts/registry — PASS with one documentation gap (Finding F3)

- No package file references `roles/`, `scripts/`, `principles/`, `compose-role`, or the legacy `workflow/registry.yaml` as something to load. The only `workflow/registry.yaml` mention is inside the frozen Backbone text itself (line 6), and `authority/README.md:15` explicitly declares such references provenance-only, not runtime dependencies at startup.
- Legacy runtime is not needed for package use: the package contains only Markdown, and both documented assemblies complete from package files alone.
- Gap: the provenance-only disclaimer enumerates `WORKFLOW-INTENT.md` and `workflow/registry.yaml`, but the frozen Backbone also cites `history/derivation-0930/RESPONSIBILITY-BACKBONE-ORACLE-CHALLENGE-3.md` and `history/derivation-0930/RESPONSIBILITY-BACKBONE-MERGED-CHALLENGE-2.md` (lines 179–180). These are also unresolvable from inside the package and should be covered by the same disclaimer.

### 9. Ownership and authority claims inside the package — PASS

No package file grants authority. All six profiles, both Charter READMEs, the template, the method files, and the package README state consistently that choosing a Profile, binding a method, or filling a Charter creates no permission; decision authority comes from the actual delegation, and verification does not authorize action. The bundled Backbone's "contract acceptance ≠ evidential verification ≠ action authorization ≠ task closure" position is reflected in the Profile/Charter/Method disclaimers; no contradicting grant was found.

## Findings

| ID | Severity | Finding | Evidence | Suggested action |
| --- | --- | --- | --- | --- |
| F1 | High (traceability) | Shipped method files are not the M4-accepted bytes; recorded M4 tree (`2fc8db5e…`) and the two Charter digest pins fail `shasum -a 256` against the shipped files, and the F method has no pin at all. | Hashes in the table above; `charters/examples/implementation-local-fix.md:13`; `charters/examples/technical-planning-cross-module.md:13`; `methods/README.md:13`; `README.md:23` | Either re-pin acceptance to a recorded commit/tree that contains the shipped bytes (e.g. `1382b3f`/`f11de8b`) and update the two Charter digests to the shipped values, or restore the M4 bytes. Add the shipped `behavior-claim-evaluation.md` digest. Do not rely on the M4 tree label while shipping M5-edited files. |
| F2 | Low (status claim) | Profile files are frozen M1 text and still say the method entry is "候选，待 M4 归位后绑定" (`profiles/README.md:5`, and the same line in all six profiles), while the package declares M4 method acceptance and the E assembly immediately binds an "accepted M4" method. | `profiles/README.md:5,44`; `profiles/*.md` "绑定状态" lines; `methods/README.md:13` | Add a one-line supersession note (in `profiles/README.md` or the package README) that the M1-era "待 M4" status lines are superseded by `methods/README.md`, without editing the frozen profile text. |
| F3 | Low (doc gap) | `authority/README.md`'s "does not load or rely on those files at runtime" disclaimer enumerates `WORKFLOW-INTENT.md` and `workflow/registry.yaml`, but the frozen Backbone also cites two `history/derivation-0930/*.md` paths. | `authority/RESPONSIBILITY-BACKBONE.md:179-180`; `authority/README.md:15` | Extend the disclaimer to name the `history/` references as provenance-only too. |
| F4 | Info (path convention) | Example Charter `Profile:` fields use parent-of-package paths (`professional-workflow/profiles/…`) while the documented assembly commands are run from the package root and use `profiles/…`. | `charters/examples/*.md:4`; `professional-workflow/README.md` §Use; `charters/README.md` §Assembly | Align the field example to the package-root-relative form, or state that the field is repo-root-relative. |

## Limits

- **Not covered:** M3 evidence and coverage, actual task binding acceptance, clean-session qualification, rollback, and whole M5/M6 acceptance — explicitly out of this review.
- **Read set:** fixed package object at `f11de8b`; the Backbone source at `a77c397` and the M1/M4 trees (`429a78b`, `0136593`) only to verify recorded digests/provenance; upstream skill files at the three cited pins (read-only). No legacy role/compose/history files, decision ledger, prior review note, or UCBIP content was read.
- **Acceptance authority is not adjudicated:** F1 is about package-internal byte/claim consistency. Whether the M5-integrated method bytes were separately accepted is outside this read set.
- **Synthetic input:** the task input was written by the reviewer for assembly mechanics only; it is not a real fixture and its subject matter was not evaluated.
- **Upstream check depth:** pins/paths/anchors were checked for existence at the cited revisions; the reviewer did not re-derive each distilled method claim from source.
- **Network:** pin existence was checked with read-only GitHub API/raw requests; results reflect upstream availability at review time.

## Appendix A · Synthetic task input used in the assembly smoke

```md
# Task input (synthetic · review smoke)

- Task: Repair the off-by-one defect in `fixture/parse_window.py` that drops the final window on exact boundary input.
- Behavior contract: contract/parse-window.md v3 (accepted by fixture owner); expected: input of N complete windows returns N entries.
- Failure observation: `python3 -m pytest fixture/tests/test_parse_window.py::test_exact_boundary` fails on commit `deadbee` with "expected 3, got 2".
- Delegation: local fix authorized by fixture owner; no production data, no external effects.
```

## Appendix B · Exact smoke commands

```sh
# extracted fixed tree
git archive f11de8b4b35015b14dfc50dd94d19525e424cd07 professional-workflow | tar -x -C <tmp>
cd <tmp>/professional-workflow

# documented E assembly
cat profiles/implementation.md \
    charters/examples/implementation-local-fix.md \
    methods/local-defect-feedback-loop.md \
    <tmp>/synthetic-task-input.md > <tmp>/assembled-E.txt   # 8,869 bytes

# documented D assembly
cat profiles/technical-planning.md \
    authority/RESPONSIBILITY-BACKBONE.md \
    charters/examples/technical-planning-cross-module.md \
    methods/cross-module-design.md \
    <tmp>/synthetic-task-input.md > <tmp>/assembled-D.txt   # 31,540 bytes
```
