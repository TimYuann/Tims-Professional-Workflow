# Check design · on-demand guide (DEF-13/14)

Status: on-demand guide at a demonstrated gap; creates no authority, tool, or gate. Source anchors and authored additions are marked. It is a reference for designing and wiring an automated check — it adds no tooling in this package.

## Use

On demand, when an automated check is being chosen, wired, or trusted — a linter rule, a pre-commit hook, a CI job, a guard script, a version/consistency sync. The guide covers the two things that decide whether such a check is worth anything: whether it actually **bites** on the violation it is meant to catch, and whether its **scope and failure behaviour** are honest. It is not a build-a-tool mandate: a check is discussed only when the task's reliability level and cost justify one (`guide-lesson-promotion.md` §Classify the violation decides that).

## Entry point and negative control

- **Use the repo's real entry point.** A check is wired where the repo already runs checks — the umbrella `check`/`ci`/`validate` script, the CI workflow, the pre-commit hook — so it runs in the same path as the rest, not in a side command nobody runs. If an existing check is present but unwired or silently broken, wiring it is the finding rather than a reason to write a new tool. *(Source: matt `c55ee460…`, `skills/in-progress/setup-ts-deep-modules/SKILL.md` §4 L59–65; `skills/misc/setup-pre-commit/SKILL.md` §4 L37–47.)*
- **A check that has never been observed failing is unproven.** Prove it bites: on a clean state it **passes**; introduce a representative violation through the real entry point and it **fails with the expected diagnosis**; revert and it **passes again**. Three observations, in that order — the middle one is the negative control, and the first/last confirm the clean state is genuinely clean. *(Source: `setup-ts-deep-modules/SKILL.md` §Prove the rules bite L79–87.)*
- **Pick the violation by risk, not by knowledge point.** One representative violation of the class that matters (the banned import shape, the destructive command, the missing script) is enough to establish the check bites; a fixture per rule or per documented sentence is ceremony unless a specific rule is itself high-risk or was previously found broken. *(Authored boundary; the review's negative-controls-by-risk rule.)*
- **Verify the check, not its config text.** The negative control exercises the actual entry point (the command CI runs, the hook the tool calls), because a rule may be present in a config file and not be reached by the command the repo runs. *(Authored.)*

## Configuration and scope

- **Merge, don't overwrite.** If a config already exists, merge the new rules/options in and say what was added, preserving the existing setup. Overwriting silently removes rules that were there for a reason. *(Source: `setup-ts-deep-modules/SKILL.md` §1 L43.)*
- **State the scope and exceptions in the check itself.** The paths, files, or package surface the check covers, and the deliberate exceptions, belong where the check runs so a later reader does not extend it by guesswork. *(Authored.)*
- **Adapt or omit missing pieces; don't fabricate them.** When a project lacks the script or tool the check would run (`typecheck`, `test`), omit that part and tell the owner rather than inventing a command that always passes or fails. *(Source: `setup-pre-commit/SKILL.md` §4 L47.)*
- **No hidden production effect.** A dev-time guard belongs in dev tooling and must not change production behaviour; prototype-only or check-only helpers stay out of the shipped path. *(Authored; `setup-ts-deep-modules` runs in the check path only.)*

## Check mode vs write mode

- **A check reports; it does not write.** A check command exits non-zero with a diagnosis and changes nothing. Keep that separate from any write/update mode that fixes the artifact. *(Source: `scripts/sync-plugin-version.mjs` L4, L22–27.)*
- **Write mode preserves the target's shape and validates before writing.** When the tool reconciles a generated artifact, it should rewrite the smallest necessary part (not reformat the whole file), and check that the intended replacement actually targets what it claims to — the version-sync script parses the proposed result and exits non-zero *before* `writeFileSync` if the field it meant to replace is absent. It does not read back the written file, and crash-safety/atomicity is not established by that design; treat those as open unless separately handled. *(Source: same file L29–40; the not-established boundary is authored.)*
- **When the target cannot be resolved, stop rather than write.** An unresolvable range/field/path is an error with a non-zero exit, not a best-effort partial write. *(Source: same file L35–38.)*

## Drift between a source and a consumer

- **One source, one consumer, an explicit check for divergence.** A generated or mirrored artifact (a version field, a derived file, an index) should have an identifiable single source and a `--check`-style mode that reports divergence without writing, used by CI so drift fails loudly. *(Source: same file L2–4, L22–27.)*
- **A guard covers what it says, not a safe-write guarantee.** A write-back guard may only cover one dangerous target condition (for example, a destination symlinked into the write source); that does not certify the general case. Do not import a script's specific safety mechanism as proof that all its writes are safe — the skills-link script, for instance, still `rm -rf`s an existing non-symlink directory at a destination, which is a risk this package deliberately does not adopt. *(Source: `scripts/link-skills.sh` L33–62; the non-import is the review's correction.)*
- **Two artifacts in sync does not prove all consumers are synced.** Version consistency between two files says nothing about downstream consumers; keep the claim to what the check actually compares. *(Authored.)*

## Limitations

- **A check is a consistency aid, not a security or permission boundary.** A hook that pattern-matches commands can be bypassed by string variations, and a wrapper's parsing decision is not a guarantee; it deters accidents, it does not confer authority. *(Source: `skills/misc/git-guardrails-claude-code/SKILL.md` §What gets blocked L10–18, §Verify L87–95; the bypass boundary is authored.)*
- **Verify with a real invocation.** A guard is verified by feeding the actual protocol a representative input and observing the expected exit/behaviour, not by reading the script. *(Source: same file, §Verify L87–95.)*
- **The package adds no tools.** This guide describes design rules for checks that the task itself has decided to build; it creates no linter rule, hook, CI job, script, or config here, and it does not make a check mandatory. *(Authored, per the dispatch boundary.)*
- **Missing tooling is declared, not improvised.** If the check cannot be built or run within the task's authorization and cost, say which part of the object is then unverified rather than substituting a weaker check that always passes. *(Authored; `behavior-claim-evaluation.md`.)*
- **"It must be able to go red" is not a confidence scale.** An `unknown` in a confidence or evidence grade for a historical/inferred claim is an investigation result about the object, not a failure-detection verdict; keep the check's red-capability question distinct from how strong a historical reference or statistical interval is. *(Gate boundary on this batch.)*

## Source anchors

| Source | Retained contribution |
| --- | --- |
| matt `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`, `skills/in-progress/setup-ts-deep-modules/SKILL.md` §1 L39–45, §4 L59–65, §6 L79–87 and `dependency-cruiser.config.cjs` L28–72 | Merge into existing config; wire into the repo's umbrella check; prove the rules bite (pass → fail on a representative violation → pass). Note: the SKILL says "four rules" while the shipped config carries five `error` entries (the entry-point boundary is split into from-app and across-packages); the negative control is the authority, not the count. |
| matt, `skills/misc/setup-pre-commit/SKILL.md` §4 L37–47, §7 L73–79 | Adapt or omit missing scripts and tell the owner; verify the hook works by running it. The exact Husky/lint-staged/Prettier stack is an example, not a required setup. |
| matt, `skills/misc/git-guardrails-claude-code/SKILL.md` L10–18, §5 L87–95 | A pre-execution guard for destructive commands; verify with a real protocol invocation (exit code + message). The pattern-match guard is not a security boundary. |
| matt, `scripts/sync-plugin-version.mjs` L2–4, L22–40 | `--check` reports and exits non-zero without writing; write mode rewrites only the version line to preserve formatting and parses the proposed result before `writeFileSync`; unresolvable target exits instead of writing. No post-write readback and no atomicity claim. |
| matt, `scripts/link-skills.sh` L33–62 | The symlink-into-source guard is a single destination condition, not a general safe-write guarantee; the `rm -rf` on an existing non-symlink destination is a risk not imported. |

Authored additions: negative controls by risk rather than per rule, verify-the-entry-point rather than the config text, the check/write separation, the stop-rather-than-write rule, the two-artifacts-in-sync limit, and the no-tools/no-mandate and confidence-scale boundaries.
