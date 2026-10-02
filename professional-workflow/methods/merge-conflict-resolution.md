# Merge conflict resolution · on-demand method (DEF-8)

- **Method owner:** E implementation owns the resolution; F owns the checks' outcome and the verdict. The intent-tracing step consumes B/C/D records (commit messages, change requests, issues); actioning a merge/rebase is an owner-level git decision, not a method-level one.
- **Status:** on-demand reference at a demonstrated gap (combining two independently-intentioned changes); a task Charter decides applicability. It is not a git tutorial and it does not by itself authorize merging, rewriting, or publishing history.

## Use

Use when combining two independently-intentioned changes has stopped on conflicts — a merge, a rebase, a cherry-pick, a patch application. The VCS operation is an instance, not the definition: the mechanism is resolving between two *intentions*, not between two blocks of text. *(Source: package DEF-8 §5 retain/change; matt `c55ee460…`, `skills/engineering/resolving-merge-conflicts/SKILL.md` L10.)*

## State and authorization

- **First establish the real state:** which operation is in progress, the base point, the conflicting objects, and both sides' actual diffs. Do not resolve against a guessed base. *(Source: same file, step 1.)*
- **The git action needs real authorization.** Running `git merge`, `git rebase`, `git push`, a history rewrite, or `--continue` is an action with effects beyond the working tree; it proceeds only under the task's valid delegation or the owner's approval, following the repository's git discipline. The method does not grant it. *(Authored, per the repo's git-discipline boundary.)*
- **Keep a recovery point.** Before starting, know how to get back (the pre-merge commit/ref, `git merge --abort`/`--quit`, a stash or a temporary branch as applicable); do not begin an integration that cannot be backed out. *(Authored; `SKILL.md`'s never-abort rule is narrowed below.)*

## Trace intent before the diff

- **Find the primary source for each side.** Read the commit messages, the change requests, the issues or tickets, and the surrounding decisions that introduced each side — the "why" of the change, not just its text. Resolving by which block looks less important "can be syntactically perfect and still silently drop a change somebody made on purpose": you cannot preserve an intent you have not read, so history comes first and the conflict markers second. *(Source: same file, step 2; package DEF-8 §2.)*
- **Where intent is not recorded, say so.** The mechanism degrades to careful diff-reading; record that limitation rather than inventing a motive. *(Package DEF-8 §2 conditions of validity.)*

## Resolve

- **Preserve both intents where they are compatible.** Do not reduce a conflict to picking a side when both changes can coexist. *(Source: same file, step 3.)*
- **Where they genuinely conflict, choose by the operation's stated goal** — what this combination is for — and state plainly what was given up. *(Same source, step 3.)*
- **Invent no behaviour that neither side had.** A conflict is a preservation problem before it is a design problem; if a genuine design decision is needed, it goes back to its owner rather than being settled inline. *(Same source, step 3; authored routing.)*
- **Backing out is a legitimate answer.** The source says always resolve and never abort, because aborting throws away the resolution work and returns the same conflict later. That reason holds only when the destination of the operation is known and wanted: if the operation itself is wrong, the intent is missing, or the state is unclear, stopping and returning to the owner is correct, not a failure. Decide *before* invoking whether the combination should happen at all. *(Package DEF-8 §2; the never-abort rule is narrowed per the gate ruling.)*
- **Keep the steps recoverable.** Resolve in small units, keep intermediate commits/checkpoints small where the operation allows, and run a targeted probe (a build of the affected area, the specific test, a quick typecheck) as you go, rather than resolving the whole conflict set blind and discovering an integration break at the end. The project's own checks still run before the result is committed. *(Authored, from the review's probes/small-commits guidance; addy's process guidance.)*
- **Detect every conflict, leave no marker, regenerate lockfiles with the real package manager.** Take the complete set of conflicted files from the actual state, and leave no conflict marker behind. A lockfile conflict is resolved by regenerating with the project's actual package manager and then reviewing the real dependency diff — regeneration is not a guarantee that the resolved content is correct, and hand-editing the lockfile is not the fix. Do not merge the latest mainline automatically as part of resolution, and do not push or tag during it; a genuinely unrelated mainline fix may be brought in only inside the existing integration authorization and risk bounds, then re-checked. *(Source: cursor `ecc249f1…`, `cursor-team-kit/skills/fix-merge-conflicts/SKILL.md`; gate2 MG3 ruling.)*
- **Order work so conflicts stay rare.** Do a wide mechanical refactor before the branches that will have to merge past it, so later work rebases onto the settled shape instead of colliding mid-flight. *(Package DEF-8 §2 parallel-work guidance.)*
- **Stage only your own resolution.** Do not stage unrelated working-tree files, and do not let a resolver's `git add -A` sweep another owner's in-flight work into the merge commit. *(Authored git-discipline rule; package DEF-8 §2 "stage everything and commit" is rejected as blanket guidance.)*
- **Who resolves matters.** A merge is best performed by whoever wrote one of the sides, because they already hold the intent a third party would have to reconstruct; batching conflicts onto one uninvolved resolver throws away exactly the context the intent step exists to recover. *(Package DEF-8 §2; the coordination rule belongs with the Driver's write-set clause.)*

## Verify after integration

- **Run the project's own checks before committing the combination.** Discover the repo's actual check command (typecheck, tests, format/lint, in whatever order the project defines) and fix what the combination broke. A merge is the easiest place to produce code that honours both branches and satisfies neither's tests, so this is a validity check on the integration rather than housekeeping after something looks wrong. *(Source: same file, step 4; package DEF-8 §2.)*
- **Re-run the specific evidence the two changes carried** where it exists, in addition to the general checks; where no usable check exists, say which part of the combination is unverified rather than implying the merge is proven. *(Authored; `behavior-claim-evaluation.md`.)*
- Record the merge as integration evidence honestly: a merge commit can carry real integration while the individual sides' claims still stand on their own evidence.

## Limits

- No blanket "never abort": the correct answer may be stopping and returning when the operation, the intent, or the state is wrong. The method also rejects "always continue/the tool knows best", "stage everything", and "the author has an inherent merge permission".
- Not a general git-authority: the method does not grant merge/rebase/push/rewrite permission, and it does not override the repo's branch or review rules.
- No specific VCS vocabulary (`ours`/`theirs`, `--abort`) as the organising idea; those are instances of the mechanism. No harness-specific hook or tool is required to run it.
- No requirement of a specific check order beyond the project's own; format can run before tests where the project says so. No requirement to fix unrelated pre-existing failures as part of the merge — record them for their owner.
- Zoning files off between parallel writers is not required: the discipline worth keeping is the ordering (wide refactor first) and the author-merges rule, not a file-partition ceremony.

## Source anchors

| Source | Retained contribution |
| --- | --- |
| matt `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`, `skills/engineering/resolving-merge-conflicts/SKILL.md` L6–14 and `docs/engineering/resolving-merge-conflicts.md` (§Primary sources over `ours` and `theirs`; §Common questions; §It's working if; §Where it fits) | Current-state check; intent before diff with the "cannot preserve an unread intent" reason; preserve both intents, choose by the operation's goal and name the trade-off; invent no new behaviour; run the project's own checks before committing with the "satisfies both, passes neither" argument; wide-refactors-first; the author-merges-it rule. The always-resolve/never-abort and stage-everything rules are narrowed/rejected; the `ours`/`theirs` framing is the anti-pattern only. |
| cursor `ecc249f1…`, `cursor-team-kit/skills/fix-merge-conflicts/SKILL.md` | Complete conflicted-file detection with no marker left behind; lockfile regeneration with the real package manager plus dependency-diff review (not hand-editing, not a content guarantee); no big refactor during resolution; no automatic mainline merge and no push/tag during resolution. *(Gate2 MG3.)* |

Authored additions: the authorization/recovery-point boundary around the git operation itself, the back-out-as-legitimate-answer narrowing, small recoverable steps with targeted probes, stage-only-your-own, and the check/verdict separation (E resolves, F judges).
