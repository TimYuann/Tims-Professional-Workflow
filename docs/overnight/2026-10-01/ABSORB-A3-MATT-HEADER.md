# A3 · mattpocock-skills — path→mechanism index header

Read contract and frozen-baseline record for `ABSORB-A3-MATT-INDEX.tsv`.
Index document only. It carries **no coverage verdict, no adoption decision, no score, and no ranking** (plan §2).

## 1 · Identity and scope

| | |
|---|---|
| Instance | `tpw-absorb-a3` (A-class, path discovery/index) |
| Authorised by | `tpw-night-driver`; Owner has authorised the A/B coverage assessment (no implementation, no absorption, no core change) |
| Repo under screen | `mattpocock-skills` **only** (A3's assignment; the other two pins belong to A1/A2) |
| Authority for scope | `docs/overnight/2026-10-01/UPSTREAM-DEEP-ABSORPTION-PLAN.md` §1 and §2 |
| Deliverables | `ABSORB-A3-MATT-INDEX.tsv` (records) and this header — nothing else |
| Output location | `docs/overnight/2026-10-01/` (fixed write surface per plan §2) |
| Input root (read-only) | `.worktrees/legacy-pre-night-2026-10-01/upstreams/mattpocock-skills` |

## 2 · Frozen baseline (verified, not inherited)

```
pin                        c55ee46073ed923f86ce59a5eb3b6d895095d1b7
HEAD == pin                yes — `git rev-parse HEAD` returned the identical 40-hex id
                           (the read-only source checkout sat on the pin; no checkout/mutation was performed)
tracked paths              169
listing command            git ls-tree -r <pin>
listing sha256             1ff31a4e6a638dff5bfdd38ef3749549dc156d10e5fdede18c967dd47368e6e1
listing lines              169
worktree cleanliness       0 entries from `git status --porcelain` (no writes to the upstream tree)
```

Cross-check digests, so a later reader can detect a different listing method rather than a changed baseline:

| Listing form | sha256 |
|---|---|
| `git ls-tree -r <pin>` (full mode/type/sha/tab/path) | `1ff31a4e…368e6e1` (the recorded digest) |
| `git ls-tree -r --name-only <pin>` | `c77f759fe8398d694cc3e72fb4467308160c9839cb0d95afc1d198295004898f` |
| the same paths, sorted | `29e21856fbaf949f09b666b8ee881d07b741067bd16f070189d6c1b20d3b25da` |
| `git ls-tree -r -l <pin>` (adds size column) | `43e5645f3fe9b4f5185b32935e8ef488e2169f718f5dd10a3bba54c7a3e31a22` |

Tree composition and size:

```
modes          100644 × 165, 100755 × 3, 120000 × 1
blob bytes     673,358 across the 169 paths
executable     scripts/link-skills.sh, scripts/list-skills.sh,
               skills/misc/git-guardrails-claude-code/scripts/block-dangerous-git.sh
symlink        AGENTS.md -> CLAUDE.md (mode 120000, blob is the 9-byte string "CLAUDE.md")
```

Accounted denominator: **169 / 169 = 100% of this repo's baseline paths**, reconciled by exact set
equality against `git ls-tree -r --name-only <pin>` sorted (not by count alone). No path is
unaccounted, and no extra path was invented.

Per plan §4, this is completion statement **(1) path accounting** only. Completion statement
**(2) substantive coverage assessment** is B's to report and is not claimed, implied or partially
asserted anywhere in this index; the A rows carry no confirmed coverage state, no `pending-check`
count and no `not-assessed` count because A does not assign any of those.

## 3 · Record shape and column order

The TSV is exactly **170 physical lines**: one column-name row, then 169 record rows. There are no
`#` comment lines inside the TSV (the former provenance block now lives in §11 of this header).
Every record row has exactly **10** tab-separated fields, one physical line per record; no field is
empty and no field contains a tab or a newline.

The column set is now **identical to `ABSORB-A1-ADDY-INDEX.tsv`, in name and in order** — verified by
diffing the two header rows byte-for-byte, not by eye:

| # | Column | Meaning |
|---|---|---|
| 1 | `repo` | always `mattpocock-skills`; with `path` this is the composite key (plan §1), so a path with duplicated content elsewhere is still accounted once per repo |
| 2 | `path` | repo-relative path exactly as git reports it |
| 3 | `nature` | what the path *is* — the A3 `file_nature` values carried over unchanged (skill body, skill metadata, skill support, docs page, bucket README, manifest, script, changeset note, governance ADR, …); 22 distinct values across 169 rows |
| 4 | `read_depth` | `full` \| `structure` \| `metadata` — what was actually read, never inferred from extension |
| 5 | `source_mechanism` | the mechanisms the path carries, as `;`-separated tags |
| 6 | `responsibility_loci` | Backbone A–F, multi-label, canonical A→F order, `,`-separated to match A1, `none` where no locus applies — **reference only** (plan §2) |
| 7 | `related_materials` | group, support files, duplicate content, consumers |
| 8 | `mechanism_lead_and_anchor` | the leading term(s) plus the **jump anchor** — section heading, template block, config key, field name or function — that takes a reader straight to the mechanism in that file. A3 had no separate lead column, so this column was authored from the mechanism already screened in column 5: it adds no new claim, it only supplies the retrieval handle |
| 9 | `uncertainties` | what was not established or is known to be drifted |
| 10 | `requery` | the cheapest targeted re-read if this row's content becomes load-bearing |

Delimiter contract, so B can parse both A files the same way: fields are tab-separated; `;`
separates items inside `source_mechanism` and `related_materials`; `,` separates loci in column 6;
` + ` separates the lead from the anchor in column 8.

**Column-order question: resolved.** An earlier revision of this file recorded that A1's column
order was not observable from this instance, and derived a 9-column order from plan §2’s field
list. A1's index is now readable and its header was diffed against this one — the two match exactly.
The reorder was a pure field permutation plus one added column: no original was re-read, no anchor
content required a fresh read, and all 169 paths were kept, verified by re-running the exact set
comparison against `git ls-tree -r --name-only <pin>` after the rewrite.

**Value-format differences that remain (deliberate, recorded so they are not mistaken for drift).**
Two A-side differences survive the column alignment, and neither is a column mismatch:

- **Language.** A1 writes its cell prose in Chinese; A3 writes in English. The column meanings are
  the same; only the natural language of the values differs.
- **`requery` phrasing.** A1 uses the two-part form `回查入口：<action>；原因：<why>`. A3 states the
  same two things inline, e.g. *"List the full `^## ` version headings and re-read the entries
  covering a named skill's rename or behaviour change"*, and writes `none` where no follow-up
  exists. Reconciling the phrasing would require rewriting 169 values (a paraphrase pass, not a
  re-read); it was left alone as out of the dispatch's scope.

**Tag vocabulary is local.** Column 5's tags are this screen's index vocabulary, not upstream
nomenclature and not a taxonomy anyone has accepted. They exist so B can group paths by mechanism;
they carry no authority and should not be quoted as if the upstream repo named things this way.
Likewise column 8's anchors are retrieval handles, not upstream section titles in every case.

## 4 · Read depth actually achieved

```
full        167 paths   content read end to end
structure     1 path    CHANGELOG.md — version headings plus head/tail sampling
metadata      1 path    package-lock.json — root manifest, lockfileVersion, entry count, samples
```

- `full` means the whole file text was read in the version at the pin. It includes all 38
  `agents/openai.yaml` files, all 38 `SKILL.md` files, all 27 in-skill support files, all 25
  `docs/**` pages, the three `scripts/`, the root guidance and vocabulary files, every
  `.changeset/*`, both plugin manifests, the CI workflow, and the three `.out-of-scope/*` policy
  files. (Counts are taken from column 4 of this index, not estimated.)
- `structure` / `metadata` are recorded as such rather than inflated. `CHANGELOG.md` is 44,408
  bytes and `package-lock.json` is 49,290 bytes; their per-entry detail was **not** read, so any
  claim that needs a specific historical changelog rationale or a transitive dependency entry
  needs the re-query named in its row.
- No read depth was invented for assets, binaries or generated files — the repo contains none of
  those categories, so the question did not arise.

## 5 · Support files and scripts are not devalued

Per the dispatch: hardening/reference material and tooling carry mechanisms and are screened at
the same fare as skill bodies. Noted explicitly so B does not have to re-derive it:

- In-skill support files: 27 paths, of which 22 are reference documents and 5 are non-reference.
  The 22 references: `ask-matt/PHASE-BOUNDARIES.md`; `codebase-design/DEEPENING.md` and
  `DESIGN-IT-TWICE.md`; `domain-modeling/ADR-FORMAT.md` and `CONTEXT-FORMAT.md`;
  `improve-codebase-architecture/HTML-REPORT.md`; `prototype/LOGIC.md` and `UI.md`;
  `setup-matt-pocock-skills/domain.md` plus `issue-tracker-{github,gitlab,local}.md` and
  `triage-labels.md`; `tdd/mocking.md` and `tests.md`; `triage/AGENT-BRIEF.md` and
  `OUT-OF-SCOPE.md`; `writing-for-agents/SKILL-MECHANICS.md`; `teach/`'s four `*-FORMAT.md`.
- Tooling and non-reference support (5 in-skill plus 3 top-level `scripts/`): executable in git —
  `scripts/link-skills.sh`, `scripts/list-skills.sh`,
  `skills/misc/git-guardrails-claude-code/scripts/block-dangerous-git.sh`; shipped but mode 100644 —
  `skills/engineering/diagnosing-bugs/scripts/hitl-loop.template.sh`,
  `skills/engineering/wizard/template.sh`,
  `skills/in-progress/setup-ts-deep-modules/dependency-cruiser.config.cjs`,
  `scripts/sync-plugin-version.mjs`; attribution-only — `skills/in-progress/pr/CREDITS.md`.
  All of the above are screened at full read depth and carry mechanisms in their own rows.
- `in-progress/`, `misc/` and `deprecated/` paths are all recorded, not treated as noise. The
  bucket itself is recorded as a fact (`nature`, `related_materials`); whether non-promoted
  status means anything for coverage is B's call, not this file's.

## 6 · Boundary compliance

- **Read-only.** No file in the upstream tree was created, modified or deleted; the source
  worktree reports zero changes.
- **No network.** Nothing was fetched, installed, updated or resolved externally.
- **No tests, no execution.** No repo script, hook, template or config was run; no package manager
  command was invoked.
- **No commit.** This index and this header are written but deliberately not staged or committed.
  The only new paths in the night worktree are these two files (`scan.js` was already untracked
  before this instance started and is not mine).
- **No A/B bleed.** This instance produced no coverage state, no gap lead, no adopt/narrow/re-frame/
  replace/reject/defer position, and wrote no B document.
- **No product/core/upstream change**, and no probing of anything outside the A3 assignment.

## 7 · Path-level observations (facts for B, not verdicts)

Recorded because they are path-level facts this screen can establish; **none of them is a coverage
judgement and none implies an action**:

1. **Promoted-set count divergence.** `README.md` and `skills/engineering/README.md` +
   `skills/productivity/README.md` list 24 promoted skills, while `.claude-plugin/plugin.json`
   carries 25 `skills[]` entries. The promoted bucket READMEs in fact enumerate 18 engineering + 7
   productivity = 25. Which list is the promotion authority is unresolved from the text; the
   plugin manifest is the one that gates installation.
2. **One content identity, two denominator paths.** `AGENTS.md` is a symlink to `CLAUDE.md`, so the
   two rows are byte-identical guidance. Recorded twice, correctly, under the repo+path composite
   key.
3. **Docs/SKILL divergence on `diagnosing-bugs` Phase 6.** The changeset
   `user-invoked-skill-invocation.md` records removing the Phase 6 hand-off to
   `improve-codebase-architecture`; `docs/engineering/diagnosing-bugs.md` still describes it.
4. **Docs/SKILL divergence on deep-module enforcement.** `docs/engineering/codebase-design.md`
   states there is no shipped lint rule, while
   `skills/in-progress/setup-ts-deep-modules/dependency-cruiser.config.cjs` is exactly that rule.
   The docs page is not aware of the in-progress skill's current contents.
5. **Docs/SKILL divergence on `tdd`'s name.** The frontmatter description still advertises
   red-green-refactor while the body documents a two-phase loop with refactoring moved to
   `code-review`. Recorded here as an observed mismatch (the docs page already tracks it as an open
   issue).
6. **Duplicated mechanism text across paths** (drift surface, not a defect claim): the phase-boundary
   tree appears in `PHASE-BOUNDARIES.md`, `ask-matt/SKILL.md` and `docs/engineering/ask-matt.md`;
   the ADR three-gate test in `domain-modeling/SKILL.md`, `ADR-FORMAT.md` and the docs page; the
   grounding model in both `writing-beats` and `writing-shape`; the invocation axis in
   `.agents/invocation.md` and `SKILL-MECHANICS.md`; the seam definition in `tdd/SKILL.md` and
   `codebase-design/SKILL.md`; dependency-injection testability rules in `tdd/mocking.md` and
   `codebase-design/SKILL.md`; the leading-word definition in `writing-fragments/SKILL.md` and
   `writing-for-agents/SKILL.md`; the promoted-skill list in three READMEs. No source-of-truth
   marker exists in any of these clusters.
7. **An unreferenced shipped support file.** `skills/productivity/teach/GLOSSARY-FORMAT.md` exists
   but is never linked from `teach/SKILL.md`, so it is unreachable except by asking.
8. **Non-executable templates.** `diagnosing-bugs/scripts/hitl-loop.template.sh` and
   `wizard/template.sh` are mode 100644; the wizard skill instructs the author to `chmod +x` the
   copy, so the mode is intentional rather than an omission.
9. **No automated check surface in the repo.** `package.json` has no lint/test/typecheck script and
   `.github/workflows/release.yml` is release-only, so no CI job would catch broken frontmatter,
   manifest drift or a bad `SKILL.md`. Relevant to any later discussion of guardrails, not a
   coverage statement.
10. **Unresolvable external dependencies named in the text.** `.agents/writing-docs.md` points at
    `~/repos/matt/personal-wiki` and `~/repos/ai/ai-coding-dictionary`, which are machine-local and
    outside the pin; `docs/engineering/*` pages cite issue and PR numbers that cannot be resolved
    from the pin.

## 8 · Re-query entries

Cheapest targeted follow-ups, so scale does not require re-reading the repo:

- **CHANGELOG.md** — list the `^## ` version headings, then read only the entries covering a named
  skill's rename or behaviour change.
- **package-lock.json** — read one `packages["node_modules/<name>"]` entry if a dependency or
  supply-chain claim is needed.
- **Promoted-set authority** — re-count `plugin.json` `skills[]` against the three READMEs.
- **Any duplicated-mechanism cluster (§7.6)** — re-diff only the named copies before citing one.
- **Renames and removals** — `CHANGELOG.md` is the "where did it go" source that the docs-page
  standard itself names; use it rather than searching the tree.
- **Column order** — if A1/A2 differ, reorder these 9 fields; do not re-read originals.

## 9 · Residual risk

- Fields 5 and 6 are one reader's labels applied to 169 paths at one pin. They are an index, not a
  measurement, and a different reader would group some paths differently.
- Two paths (44 KB + 49 KB) were read at structure/metadata depth. Every other path was read in
  full, so residual risk is concentrated in those two and is named in their rows.
- The upstream repo is a moving target: this is a frozen screen of one pin only, and nothing in this
  file survives a pin change without re-verification.
- Prose-level defects recorded in the `docs/**` pages (live bugs, open issues, unfixed behaviour)
  were screened as content about mechanisms, not re-verified against upstream trackers. Where a row
  says "documented", it means the page says so.

## 10 · Provenance of these deliverables

```
ABSORB-A3-MATT-INDEX.tsv  sha256 26f4d1681c0d70113900ef9926e6b984764e2fd84f851b83025fdfd7f2cbcdfc
                          layout 170 physical lines = 1 column-name row + 169 record rows
                                 (no # comment lines; provenance block is §11 below)
git state                 untracked; not staged, not committed (intentional)
```

## 11 · Provenance block (moved out of the TSV)

The 15 `#` lines that used to head the TSV were removed so the index parses as a plain 170-line
table. Their content is preserved verbatim here; nothing was dropped or reworded.

```
# ABSORB-A3-MATT-INDEX.tsv
# Path->mechanism screen (plan section 2) for the A3 instance: repo mattpocock-skills only.
# Derived directly from the fixed Git pin; nothing else in this file is a frozen baseline.
# repo: mattpocock-skills
# pin: c55ee46073ed923f86ce59a5eb3b6d895095d1b7
# HEAD-==-pin check: equal (git rev-parse HEAD returned the same 40-hex id)
# tracked_paths: 169
# listing_command: git ls-tree -r c55ee46073ed923f86ce59a5eb3b6d895095d1b7
# listing_sha256: 1ff31a4e6a638dff5bfdd38ef3749549dc156d10e5fdede18c967dd47368e6e1
# listing_lines: 169
# data_rows: 169 (one per tracked path; composite key repo+path)
# comment_lines: leading lines beginning with "#" are provenance, not records;
#   the first non-comment line is the column-name row.
# note: field values never contain tabs or newlines; ";" separates labels inside a field.
# note: there is no scoring, ranking, adoption verdict or coverage claim in this file (plan section 2).
```

The last two lines are superseded by §3's delimiter contract (column 6 now uses `,`) and by the
removal of the comment lines themselves; they are reproduced as written rather than edited, so the
record of what the file used to say is intact.
