# A2 · cursor-plugins — path→mechanism index header

Read contract and frozen-baseline record for `ABSORB-A2-CURSOR-INDEX.tsv`.
Index document only. It carries **no coverage verdict, no adoption decision, no score, and no ranking** (plan §2).

## 1 · Identity and scope

| | |
|---|---|
| Instance | `tpw-absorb-a2` (A-class, path discovery/index) |
| Session / model | `01a0f784-6467-77cd-8e73-02aa918fa660` · `commandcode/deepseek/deepseek-v4.1-flash` (reasoning `max`) |
| Authorised by | `tpw-night-driver`; Owner has authorised the A/B coverage assessment (no implementation, no absorption, no core change) |
| Repo under screen | `cursor-plugins` **only** (A2's assignment; the other two pins belong to A1/A3) |
| Authority for scope | `docs/overnight/2026-10-01/UPSTREAM-DEEP-ABSORPTION-PLAN.md` §1 and §2 |
| Deliverables | `ABSORB-A2-CURSOR-INDEX.tsv` (records) and this header — nothing else |
| Output location | `docs/overnight/2026-10-01/` (fixed write surface per plan §2) |
| Input root (read-only) | `.worktrees/legacy-pre-night-2026-10-01/upstreams/cursor-plugins` |
| Generated (UTC) | 2026-10-01 (index written 2026-10-01T13:26Z) |

## 2 · Frozen baseline (verified, not inherited)

```
pin                        ecc249f1e306fc64ddf83c7bed16cacf7c2239db
HEAD == pin                yes — `git rev-parse HEAD` returned the identical 40-hex id
expected tracked paths     863 (dispatch stated "期望 tracked=863")
observed tracked paths     863
listing command            git ls-tree -r <pin>
listing sha256             114a1c9a267bb3758d892b02b39402ad1fb47814f75909a54fb99e9cd4462d77
listing lines              863
worktree cleanliness       0 entries from `git status --porcelain` (no writes to the upstream tree)
```

The pin check was performed **before** any reading. No checkout, fetch, install or mutation was performed on the source tree.

Cross-check digests, so a later reader can detect a different listing method rather than a changed baseline:

| Listing form | sha256 |
|---|---|
| `git ls-tree -r <pin>` (full mode/type/sha/tab/path) | `114a1c9a…d4462d77` (the recorded digest) |
| `git ls-tree -r --name-only <pin>` | `3a67346c5c7334265ad317e2a22090ff035996da57979fabd2110f21f4bb0504` |
| the same paths, sorted | `c0ca6d95a5bf78ede92fdb7c4484d48ed743fe7e8cee9c8c58f7a5902bd67b6c` |
| `git ls-tree -r -l <pin>` (adds size column) | `74b377abe5959e81f3c827d222f925d6f7715419e79c264e5b47501432199a36` |

Tree composition and size:

```
modes          100644 × 851, 100755 × 12
blob bytes     6,027,523 across the 863 paths
file types     .md 385 · .json 186 · no-ext 95 · .png 75 · .ts 72 · .svg 18 · .sh 9 · .jpg 6 · .mdc 4
               .gitignore 3 · .mjs 2 · .lock 2 · .yml/.yaml/.tsv/.js/.html/.css 1 each
executables    12 paths, incl. pstack/skills/poteto-mode/scripts/watch-pr/watch-pr and
               pstack/skills/poteto-mode/scripts/worktree-audit.sh (mode 100755)
no symlinks    (the sibling repo A3 screened had one; this repo has none)
```

Accounted denominator: **863 / 863 = 100% of this repo's baseline paths**, reconciled by **exact set equality** against `git ls-tree -r --name-only <pin>` sorted (`diff` reports IDENTICAL), not by count alone. Every record row has exactly 10 tab-separated fields, no field is empty, no path appears twice.

Per plan §4, this is completion statement **(1) path accounting** only. Completion statement **(2) substantive coverage assessment** is B's to report and is not claimed, implied or partially asserted anywhere in this index; the A rows carry no confirmed coverage state, no `pending-check` count and no `not-assessed` count because A does not assign any of those.

## 3 · Record shape and column order

The TSV carries **one column-name row first, then 863 record rows — no comment/provenance lines** (per the Driver's dispatch: "首行表头、tab 分隔、恰好 10 列 … 不加注释行（说明放 HEADER.md）"). Column order matches A1's `ABSORB-A1-ADDY-INDEX.tsv` exactly, confirmed by reading that file before writing this one, and re-confirmed by the Driver.

| # | Column | Meaning |
|---|---|---|
| 1 | `repo` | always `cursor-plugins`; with `path` this is the composite key (plan §1), so a path with duplicated content elsewhere is still accounted once per repo |
| 2 | `path` | repo-relative path exactly as git reports it |
| 3 | `nature` | what the path *is* (plugin manifest, skill body, playbook, hook script, JSON schema, test file, binary asset, license, …) |
| 4 | `read_depth` | `full` \| `structure` \| `metadata` — what was actually read, never inferred from extension |
| 5 | `source_mechanism` | the mechanisms the path carries, in prose |
| 6 | `responsibility_loci` | Backbone A–F, multi-label, canonical A→F order, `none` where no locus applies — **reference only** (plan §2) |
| 7 | `related_materials` | group, support files, duplicate content, consumers |
| 8 | `mechanism_lead_and_anchor` | the field / constant / paragraph that actually carries the mechanism |
| 9 | `uncertainties` | what was not established, is known to drift, or is a text-level constraint |
| 10 | `requery` | the cheapest targeted re-read if this row's content becomes load-bearing |

**No column-order uncertainty for this worktree.** A1's file was observable before this header was written and its 10 columns were read directly; the Driver also confirmed the order in writing. Column-order risk is therefore zero, unlike the situation A3 recorded.

**Tag vocabulary is local.** Field 5's mechanism wording and field 6's A–F labels are this screen's indexing vocabulary, not upstream nomenclature and not an accepted taxonomy. They exist so B can group paths by mechanism; they carry no authority and should not be quoted as if the upstream repo named things this way.

## 4 · Read depth actually achieved

```
full        435 paths   content read end to end (or, for tests/schemas, the defining surface read in full)
structure   234 paths   section-level read: headings, exported symbols, constants, per-file purpose, changelog
                       version lines and lockfile headers — not every line
metadata    194 paths   tree metadata plus the manifest reference only: MIT licence bodies, brand and
                       illustration assets, and the one unread pricing reference
```

Depths follow A1's stated口径 (A1 header §3): `full` = the file was read from front to back this round; `structure` = frontmatter/heading anchors/top-level declaration sequences were read; `metadata` = only tree metadata (size/mode/type) and the path name were read. The 81 changelog and lockfile rows are `structure` rather than `metadata` precisely because their heading or header lines were read.

- `full` includes: all 94 `plugin.json` manifests, all 79 `mcp.json` server configs, the whole pstack skill/playbook/principle corpus, orchestrate's docs/prompts/references/SKILL, the six `third_party` skill bodies, root `marketplace.json`/`README.md`/both schemas/`validate-plugins.mjs`/the CI workflow, and every first-party plugin's README/skill/agent/hook text.
- `structure` is recorded **honestly** rather than inflated: it covers the 72 `.ts` script bodies, the 28 orchestrate test suites, the 9 large `why` reference files, cursor-sdk's five remaining reference files, `x-api-mcp-guide` (21.6 KB), and the 77 third_party READMEs read by section rather than sentence. Any claim needing a specific assertion, branch or paragraph in those paths needs the re-query named in its row.
- `metadata` is likewise honest: 94 MIT licence bodies (1063 B each, never read as text), 91 brand/illustration assets (PNG/SVG/JPEG, never decoded), and 1 unread pricing reference (`x-api-mcp-guide/references/pricing.md`).
- **No read depth was invented for assets, binaries or generated files**, and no path was marked `full` merely because it was small.

## 5 · Multi-plugin decomposition — every path stays on the books

Per the dispatch ("单仓多插件（pstack / cursor-team-kit / thermos / third_party 等），按 path 如实分；非 pstack 插件与 third_party 资产同样留账不贬值"):

| Group | paths | note |
|---|---|---|
| `third_party/` (79 connectors) | 482 | 79 × 6 base files, +6 extras (3 Google skills, 3 X files, 1 X Money skill, 1 Shopify rule) |
| `pstack` | 158 | 1 plugin, 45 skills (incl. 23 principles), 23 playbooks, 10 prompts-equivalent docs, 62 script/test files |
| `orchestrate` | 84 | 1 plugin, 10 prompt templates, 4 references, 2 schemas, 62 script/test files |
| `cursor-team-kit` | 29 | 18 skills (one duplicated from thermos), 2 agents, 2 rules, 1 HTML renderer trio |
| `advisor` | 14 | 1 skill, 1 subagent, 4 hook scripts + 1 hook config |
| `cursor-sdk` | 11 | 1 skill + 7 references (the SDK's declared source of truth) |
| `thermos` | 10 | 3 skills (one a copy of a cursor-team-kit skill), 2 agents |
| `ralph-loop` | 10 | 3 skills, 2 hooks, loop state protocol |
| `agent-compatibility` | 10 | 1 orchestrator skill + 4 review agents |
| `grok-voice` | 9 | 4 skills + 2 logos |
| `create-plugin` | 9 | 2 skills, 1 agent, 1 rule |
| `continual-learning` | 8 | 1 skill, 1 agent, 1 TS hook |
| `teaching` | 6 | 2 skills |
| `pr-review-canvas` / `docs-canvas` | 6 + 6 | the pair of Canvas plugins; `docs-canvas` self-declares as a placeholder |
| `cli-for-agent` | 4 | 1 skill |
| repo root | 7 | `README.md`, `.gitignore`, `.cursor-plugin/marketplace.json`, `.github/workflows/validate-plugins.yml`, `schemas/×2`, `scripts/validate-plugins.mjs` |

- **`third_party` assets are not devalued.** Every connector's `LICENSE`, `assets/logo.*`, `CHANGELOG.md` and `mcp.json` has its own row. Licenses and logos are recorded at `metadata` depth **as assets**, with the reference relationship to `plugin.json` established; no path was dropped for being repetitive.
- **Non-pstack plugins are not devalued.** Each has its README, skills, agents, rules, hooks and control files on the books at the depth actually achieved, including the two plugins whose mechanism is almost entirely machine-side (`orchestrate`, `ralph-loop`).
- **Cross-plugin duplication is recorded, not merged away.** Notable duplicated-or-overlapping surfaces, each visible in its own rows: `thermo-nuclear-code-quality-review` exists in both `cursor-team-kit` and `thermos`; `pr-review-canvas` exists as a `cursor-team-kit` skill (local HTML walkthrough) and as the standalone `pr-review-canvas` plugin (Cursor Canvas); `deslop`/`control-cli`/`control-ui` live in `cursor-team-kit` but are consumed by pstack; `grok-voice/assets/logo.svg` is shipped but not referenced by its manifest; three 24,255-byte `avatar.png` files and other brand PNGs are reused across first-party plugins.

## 6 · Boundary compliance

- **Read-only.** No file in the upstream tree was created, modified or deleted; the source worktree reports zero changes and no checkout was performed.
- **No network.** Nothing was fetched, installed, updated or resolved externally. No npm/npx/bun install was run (several rows document servers that *would* fetch at runtime; none was executed).
- **No tests, no execution.** No hook, script, test suite or CLI in the upstream repo was executed. All 12 executable files are recorded as paths only.
- **No commit.** This index and this header are written but deliberately not staged or committed.
- **No A/B bleed.** This instance produced no coverage state, no gap lead, no adopt/narrow/re-frame/replace/reject/defer position, and wrote no B document.
- **No product/core/upstream change**, and no probing of anything outside the A2 assignment. The two deliverable paths are the only files this instance wrote under `docs/overnight/2026-10-01/`.
- **Not fetched or absorbed:** `agent-compatibility`'s scanner is deliberately not bundled upstream (the plugin runs a published npm package at need); this screen records that fact, it did not run it.

## 7 · Path-level observations (facts for B, not verdicts)

Recorded because they are path-level facts this screen can establish; **none of them is a coverage judgement and none implies an action**:

1. **One repo, one marketplace, two client families.** The root `.cursor-plugin/marketplace.json` lists 94 plugins = 15 first-party + 79 `third_party` directories, with exact set equality against the directory listing. Three entries carry `minClientVersions` with `cursor: "never"` (`finance` 1.1.2, `x-money` 1.0.0, `shopify-store` 1.0.0) — they are invisible to Cursor and targeted at Grok Bot/sand. `schemas/marketplace.schema.json` defines the `never` literal in its `clientVersionRequirement` branch; neither the root README nor any first-party doc explains it.
2. **The connector template is highly uniform.** 79 connectors share one six-file shape (`plugin.json`, `README.md`, `CHANGELOG.md`, `LICENSE`, `assets/logo.*`, `mcp.json`). Five deviate: `x` (9 files — two skills plus a pricing reference), `x-money`, `google-docs`, `google-sheets`, `google-slides` (7 each — one skill), `shopify-store` (7 — one rule).
3. **Transport split.** 77 connectors use remote HTTP (`"type": "http"`); two are local stdio: `playwright` (`npx -y @playwright/mcp@latest`) and `xero` (`npx -y @xeroapi/xero-mcp-server@latest`, with credentials injected as process `env`). Only these two execute code on the caller's machine.
4. **Credential shapes differ four ways** and the difference is a security-relevant fact: header-injected user keys (`brevo`, `github`, `hunter`, `similarweb`, `smartsheet`, `wrike`), inline OAuth client id/secret via `${VAR}` (`docusign`, `gong`, `hubspot`, `salesforce`, `zoom`), env injection for a local process (`xero`), and built-in OAuth client ids that ship in the repo (`x` and `x-ads`, the same `CLIENT_ID` value in both). Twelve connectors declare `variables` in `plugin.json`; the rest rely on OAuth.
5. **`x` requests 18 scopes and deliberately excludes `tweet.write`** — its README states posting is not included; `x-chat` further requires `dm.read`/`dm.write` and refuses to fake classic unencrypted DMs. `x-money`'s skill makes per-action approval a hard rule and forbids retrying a refusal or an unconfirmed payment.
6. **Money- and side-effect-bearing connectors say so in their own text**: `coinbase` ("Orders placed through this server are live"), `robinhood` ("You are responsible for every trade the agent places"), `buffer` ("Publishing is live to real social accounts"), `posthog-mcp` (many tools write to the project), `tinyfish` (automations act on real sites with saved credentials), `trello` (writes land on boards teammates see).
7. **Two connectors describe a server whose auth story is in flux**: `meltwater` (server advertises OAuth + dynamic client registration while its public docs still describe API-key auth) and `docusign` (server "in beta"). `ashby`, `brex`, `customer-io`, `jotform`, `navan`, `outreach` and `statsig` each require a one-time *admin* toggle before any user can connect — a two-step gate that lives only in the README.
8. **`docs-canvas` is a self-declared placeholder** (README "initial scaffold"; the skill body carries a `> Status: placeholder` block saying the full body still needs writing), while `pr-review-canvas` in the same generation of plugins is complete. The two are otherwise structural twins.
9. **`create-plugin` advertises a `create-plugin` command** in its README and CHANGELOG that has no `commands/` directory and no `commands` field in its manifest.
10. **Cross-plugin duplication surface** (drift surface, not a defect claim): the thermo-nuclear code-quality rubric appears in both `cursor-team-kit` and `thermos`; the `pr-review-canvas` name exists twice with different implementations; `grok-voice/assets/logo.svg` is shipped but unreferenced by its manifest; `thermos`'s own description mentions "take-the-wheel and FSD merge-ready flows" that no file in the plugin implements.
11. **The only executable check in the repo is manifest-shaped.** `.github/workflows/validate-plugins.yml` triggers only on changes to `marketplace.json`, `**/plugin.json` or `schemas/**`, and `scripts/validate-plugins.mjs` validates those manifests plus marketplace↔plugin name equality. It does **not** check that declared `skills`/`agents`/`rules`/`hooks`/`mcpServers` paths exist, nor frontmatter — that surface is covered only by the prose checklist in `create-plugin`'s `review-plugin-submission` skill. Relevant to any later discussion of guardrails, not a coverage statement.
12. **The two largest machine surfaces** are `orchestrate/skills/orchestrate/scripts/core/agent-manager.ts` (68,875 B) and `pstack/skills/poteto-mode/scripts/orch/store.ts` (42,927 B). Both are recorded at `structure` depth (constants, exported types, purpose), with the specific requery named in their rows.

## 8 · Re-query entries

Cheapest targeted follow-ups, so scale does not require re-reading the repo:

- **Any `.ts` script row** — the row names the module's exported surface and constants; read only the named function or constant's body.
- **The two large TS files (§7.12)** — read `agent-manager.ts`'s spawn/wait paths or `store.ts`'s lock/atomic-write paths only if a concurrency or durability claim is needed.
- **The 28 orchestrate test suites** — grep the `describe`/`test` titles to find the assertion a claim needs; per-file case counts are already in the rows.
- **`x-api-mcp-guide/SKILL.md`** — read the `Session start`, `Cost awareness`, `Fields, pagination`, `Search operators`, `Workflows` or `Don't` sections (frontmatter + first 130 lines are already screened).
- **`x-api-mcp-guide/references/pricing.md`** — unread; read in full if cost claims matter.
- **Any third_party README** — rows record the gate, capability and note lines; read the full file only when wording precision matters.
- **Column order** — no action needed; A1's order was read directly and the Driver confirmed it.

## 9 · Residual risk

- Fields 5 and 6 are one reader's labels applied to 863 paths at one pin. They are an index, not a measurement, and a different reader would group some paths differently.
- 428 of 863 paths (234 `structure` + 194 `metadata`) were not read line-by-line, and the rows say so. Residual risk is concentrated in the large TS surfaces, the orchestrate test suites, the five cursor-sdk references, the nine `why` reference files and the unread `pricing.md`; each names its re-query.
- `third_party` READMEs were screened by section (install, MCP config, gate, capabilities, notes), not sentence by sentence. Where a connector's risk lives in a paragraph outside those sections — regulatory limits, regional endpoints, per-account tool availability — the row records what that section said and flags it as a text-level statement, not a verified behaviour.
- Several rows describe behaviour that is **claimed by the upstream text but not verifiable from the pin**: server-side tool surfaces ("the hosted runtime is the source of truth for tool names and schemas"), client-version gates, and platform-side approval mechanics (`x-money`'s `SendToUser` widget, the `approval` input the server enforces). These are recorded as documented mechanisms.
- The upstream repo is a moving target: this is a frozen screen of one pin only, and nothing in this file survives a pin change without re-verification.
- Two logo-extension mismatches were introduced by this reader and corrected against `git ls-tree` during initial reconciliation (intercom, x-ads); the set-equality check in §2 is what caught them, which is the check a later reader should repeat rather than trusting the count. A second, externally reviewed correction pass is recorded in §11.

## 11 · Revision record

**Revision 1 — bounded factual correction (2026-10-01, after Pro pre-read returned RETURN).** Owner authorised one bounded correction pass; only this TSV and this header were touched, no re-reading was performed (every anchor cited below was already read in this screen), and nothing was committed.

The pre-read flagged one real factual error: row 165 (`orchestrate/skills/orchestrate/SKILL.md`) asserted in `uncertainties` that "本仓不含该技能正文" for the `cursor-sdk` skill. That skill body **is** in the fixed pin. Verified with `git ls-tree -r <pin>` and `git show HEAD:cursor-sdk/skills/cursor-sdk/SKILL.md`:

```
path   cursor-sdk/skills/cursor-sdk/SKILL.md
blob   bb070b338da14aa5d0847e793f6f364f25a751c3
size   15,428 bytes / 239 lines
note   this screen had already recorded that same path at `full` depth in its own row,
       so the two rows contradicted each other
```

The cell now states that the body exists in-repo (with the pin + path + blob anchor) and separates the remaining unverified claim: *whether that plugin is installed or loaded on the target host* — this repo only carries the marketplace registration and the plugin directory, which proves nothing about host-side installation.

A `grep` self-check for the same assertion family ("本仓不含 / 外部插件 / 缺失 / 不存在 / 外置 / 外部依赖") produced 17 further hits, judged one by one against the pin:

| Row | Path | Was | Now |
|---|---|---|---|
| 343 | `create-plugin/rules/plugin-quality-gates.mdc` | machine-side constraint called "本仓外的 marketplace 校验器" | **wrong**: `schemas/plugin.schema.json` is in this repo and is consumed by the root `scripts/validate-plugins.mjs`; cell now says so and separates it from the fact that the rule is about plugins authored elsewhere |
| 273 | `cursor-sdk/.cursor-plugin/plugin.json` | cursor-sdk called an "orchestrate 的外部依赖" | **imprecise**: the plugin directory and skill body are in-repo; cell now says "跨插件依赖" + in-repo anchors, and keeps host install/load as an unverified separate claim |
| 72, 76, 83 | `visual-parity.md`, `shipping.md`, `multi-phase-plan.md` | `pstack/skills/control-*（外置…）` | **path not in the pin**: no `pstack/skills/control-*` exists; now `cursor-team-kit/skills/control-{cli,ui}（pstack 之外置依赖）` |
| 75, 84, 137 | `babysit.md`, `worktree-cleanup.md`, `show-me-your-work/SKILL.md` | upstream-relative helper paths quoted bare (`scripts/watch-pr/watch-pr`, `scripts/worktree-audit.sh`, `scripts/log.sh`) | not false — the upstream text writes them that way — but now carry their repo-relative resolution so a reader does not hunt a path that does not exist at the repo root |

Hits checked and left unchanged because they are correct against the pin: the "not shipped here"三 external references in `pstack/README.md` (deslop/control-cli/control-ui really do live in `cursor-team-kit`, and `create-skill`/`loop`/`babysit` really are host built-ins); the `~/.cursor/skills-cursor/canvas/SKILL.md` dependency in `pr-review-canvas` and `docs-canvas` (no `skills-cursor` path exists in the pin); the `xchat-grokbot-helper` + `chatxdk` dependency in `x-chat` (absent from the pin); the host-side `SendToUser`/`approval` mechanism in `x-money-guide` (the pin only documents it); and `deslop`'s statement that pstack does not bundle it.

A bounded path-token sweep was then run: every backticked repo-relative-looking path in all 863 rows was resolved against the pin's path set. The only remaining unresolvable tokens are the three upstream-relative helper quotes above (now qualified) and `.cursor-plugin/plugin.json`, which is correct in its three contexts because it names *a plugin's* manifest in a plugin directory, not a path at the repo root. Row count (863), column count (10), field emptiness, unique-path count, and set equality against `git ls-tree -r <pin> --name-only` were all re-verified after the edits; set equality still reports IDENTICAL. Read-depth distribution is unchanged at full 435 / structure 234 / metadata 194.

## 10 · Provenance of these deliverables

```
ABSORB-A2-CURSOR-INDEX.tsv  sha256 1ee869541be45dbb09ce1f463d11956b7a8920446620f8744c0d55cb85f00c71
                            records 863 + 1 column header (no comment lines)
                            size    757,962 bytes
                            rev 1   see §11 (bounded factual correction; 9 cell replacements in 8 rows)
baseline listing            git ls-tree -r ecc249f1e306fc64ddf83c7bed16cacf7c2239db
                            sha256 114a1c9a267bb3758d892b02b39402ad1fb47814f75909a54fb99e9cd4462d77
git state                   both files untracked; not staged, not committed (intentional)
```
