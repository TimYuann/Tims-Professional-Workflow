# Main cutover · Owner-authorized execution plan

状态：**Owner 已授权 Driver 执行本地完整切换与 TPW pane 精简，2026-10-01**。不是提案等待批准。本计划覆盖 Driver 启动时旧 system-prompt 的 main 禁令：本次有限 main 迁移、归档与入口整理可以执行；旧禁令仍约束其它业务/发布。Oracle 管交付结果，Driver 负责自主维持与串行集成。

## 1. Outcome / accepted limits

Owner 希望根工作目录 `/Users/yuantian/Developer/tim-professional-workflow` 的 `main` 使用已接受的新 Professional Workflow，旧版保存在可访问的独立 worktree；以后可选择性取回旧脚本，不恢复旧治理。

完成形态：

- 根目录 `main` = 新版 + 本次入口迁移提交；默认 `AGENTS.md` / README 只引导新 intent、Backbone、Profiles、Charters、methods 与交付状态。
- `.worktrees/legacy-pre-night-2026-10-01` = 旧 main@`496b0676e302e2d0eafba129ff61de4c203d258a`，独立 legacy 分支；完整保存切换时的 staged / unstaged / untracked / relevant ignored 字节与属性。本地 dirty 不当成新 main 方法，也不擅自盖“已接受”章。
- `.worktrees/night-2026-10-01` 可继续保留为本次新版本构建/恢复工作树；不得删它的 `scan.js`（归属未知）。不为腾出分支名而删除 Git 历史。
- 保持已接受 core 内容/方法语义、Backbone 冻结字节；只允许当前包入口状态、引用定位与根目录维护规则必要更正。不得重新吸收、优化方法或重开冷读报告里的 UCBIP 接线/业务问题。
- 本轮完成**本地主线**切换。不自行推送 `origin/main`、force-push、tag、GitHub release 或修改远端默认分支。远端更新由 Oracle 在最终固定结果后处理；交付必须明确本地/远端状态，不把本地切换说成远端已切换。

## 2. Known starting facts (re-read before mutation)

- Primary root branch main@496b067; ahead origin/main 40 commits. Night branch@`e503afc14f951031ecf69e287c36baf2e8964757` before this plan; main is an ancestor, night ahead 50. No rebase/history rewrite required.
- Root has original eight staged paths, three tracked unstaged modifications and multiple untracked reports. Preserve actual snapshot, not remembered counts. `.decisions/ledger.tsv` and the old boundary work document are concurrent/user state.
- Night tracked tree was clean, except unknown untracked `scan.js`. New cutover-plan commit will advance night; use actual fixed tip.
- Night still contains legacy root AGENTS/README, roles/skills/principles/workflow/scripts/VERSION and old docs. A branch FF alone does **not** perform the intended authority switch.
- Accepted delivery `205b831` core subtree `11e6e3772b6bc0e17259c932b0c0dcabb030a133`; final acceptance `cf10752`; DSH test analysis `e503afc`. Keep fixed evidence accessible from Git.
- There are two old detached worktrees under /private/tmp and live unnamed user pane `w27:pN`; they are outside this cutover/retirement scope. Never change/move/delete them.

## 3. Crew / writing discipline

Driver `tpw-night-driver` (Pi Flash/max) is the only physical product/main writer for this task. Existing `tpw-night-check` is the separate migration/check reader; existing `tpw-night-method` (Sol/medium) is retained only for a real unresolved responsibility/authority interpretation, not mechanical diff/hash checks.

Do not start a large new team. Checker writes only its explicit verification report, not candidate entry text or migration code. No parallel root/main writer. Communicate through Herdr short routing plus exact artifact refs.

Root Oracle and unnamed user session will not be asked to restart or have their configuration altered. State clearly that their historical loaded instructions are stale after cutover; actual current root docs are the reference for new tasks. Driver may continue from the linked night tree after root promotion; it need not terminate its own live session to change cwd. Future writer operations explicitly target the correct tree.

## 4. Execution / completion boundaries

### C0 · Freeze and preserve old现场 (before clearing anything)

Re-read root/night Git, worktree identities and live crew. If root/legacy paths are changing concurrently, stop the affected mutation, tell Oracle exactly which identity drifted; do not overwrite.

Create a uniquely named custody directory inside `.worktrees/preservation/` (no /tmp): old HEAD/ref, porcelain with NUL-safe path handling, index inventory/staged binary diff, unstaged binary diff, untracked path+content manifest and copies. Save relevant local/ignored content that would otherwise become stranded (raw upstream references, `.decisions` data, agent/local configs when present). Never commit private runtime data or secrets. Do not copy or replace shared `.git` administration, and do not recursively copy `.worktrees/` into itself. Existing preservation archives are a reference, not proof current bytes are preserved.

Create `legacy/pre-night-2026-10-01` at exact old root HEAD, then add its worktree at `.worktrees/legacy-pre-night-2026-10-01`. Reproduce the original staged vs unstaged distinction there using explicit patches/paths, plus untracked and relevant ignored files. Filesystem metadata/symlinks/executable bits and staged blob identities matter; preserve logical index state, not a byte-for-byte transplant of a different worktree's index. No shared stash and no “commit everything” snapshot of unknown/private data.

**C0 done:** legacy HEAD matches old root; old staged diff/index entries, unstaged diff and inventoried local file identities match; independent reader verifies. Save a named checkpoint/recovery capsule that can reconstitute old root. Only then clear/move root files that have been verified as migrated. Prefer targeted `git restore` and explicit path moves/removal against the inventory; no blanket `reset --hard`, `git clean`, `rm -rf`, worktree prune or shared `.git` replacement.

### C1 · New root入口 and retirement of legacy active surfaces

Work on night branch. Make a small explicit keep/archive inventory before moves. New root retains `professional-workflow/`, `adoption-examples/`, active intent/Backbone source, new overnight plan/evidence/test analysis and this cutover record. `.worktrees/` stays ignored locally **and in tracked .gitignore for fresh clones**.

Retire from **active root checkout** old `roles/`, `skills/`, `principles/`, `workflow/`, `scripts/`, old `VERSION`, `.decisions` and old active/generated docs (such as artifacts/coldstart/ledger/downstream-mapping/closure-report). They remain accessible unchanged in the verified legacy worktree and Git. Classify other legacy docs/source-reference paths explicitly; default to legacy, not active instructions. Raw upstream/source assets are read-only source material, not adopted method: keep an explicit legacy locator rather than silently restoring old source-disposition authority. Do not duplicate an entire archive directory into new main just to preserve what legacy/Git already preserves.

Root README gives one default entry, accepted package identity/state, shortest use path and a brief legacy-retrieval pointer. Root AGENTS describes current owner files and narrow meaningful checks; it must not declare legacy registry the current authority or require old render/compose/check scripts. Keep owner hierarchy clear: intent controls goals; Backbone responsibility definitions have one editable accepted source; bundled projection is static accepted export, not another mutable definition; each Profile/Charter/method owns its own content. Do not introduce a replacement mega-registry.

Only necessary package entry/status wording may be brought current (root/core README and Profile/Charter/method indexes); label historical source acceptance vs shipped current acceptance precisely. Frozen Backbone historical design-status text is not rewritten; authority README may explain its dated context without reviving old runtime references. Fix cross-repository pointers in the optional example only where needed to resolve them reliably (repo identity + fixed ref/path); no UCBIP governance changes or old-name method mapping in this task.

Review actual diff and commit a reversible cutover checkpoint. Any product semantic change is outside C1: report it instead of smuggling in a method rewrite. Entry metadata updates give a **new core identity** if bytes change; recompute current manifest/identity and describe why prior semantic evidence still covers unchanged claims. Do not reuse old tar digest for a new source commit.

**C1 done:** reader entering root AGENTS/README reaches one current path without chasing legacy registry, early phase-state claims or guessed repo bases; archived active surfaces no longer compete. Existing accepted method/Backbone semantics stay unchanged.

### C2 · Promote locally and verify recoverability

After C0 preservation PASS and C1 entry diff accepted by the separate reader, restore a clean primary root only for inventoried migrated changes. If new user files appear, preserve and stop the affected step instead of cleaning them. Keep ignored custody/other live worktrees untouched.

Fast-forward local primary `main` to the fixed night cutover tip (`git merge --ff-only` with the root as explicit cwd is the expected operation). No force branch replacement, rebase or amendments of the old commits. If not FF, report divergence with exact refs; don't auto-resolve by rewriting history.

Verify root branch/HEAD, new default paths, legacy HEAD+preserved dirty/staged identities, linked worktree registration, preserved scan.js, and fixed new core vs declared manifest. Demonstrate recovery in a **workspace-local controlled copy** from legacy checkpoint/capsule, compare the preserved tracked modifications/index distinctions and sampled local assets. Do not actually roll back the promoted main to perform a demonstration. Existing Git/patch tools suffice; no recovery framework or product validator.

**C2 done:** local root main is fixed new cutover object; preserved legacy remains usable including original eight staged changes; one controlled restoration succeeds at its stated scope. All remote refs remain unchanged by Driver.

### C3 · Bounded cold read / final handoff

Separate reader uses root AGENTS+README and normal file references to answer: current version/entry; which content owns which kind of meaning; how one task binds a Profile/method; what is legacy; how to recover an old script. No new external Pro, full source survey, old four checks, UCBIP test/service or actual business task. Cold read is a document/reference check; if it needs command execution, explicit isolated workspace scope is required.

Deliver one short self-contained report under `docs/overnight/2026-10-01/MAIN-CUTOVER-REPORT.md`: old/new HEADs, legacy path/ref, staged/unstaged/untracked preservation result, exact entry/core diff, independent check and controlled recovery limits, new core manifest, root main status, remote main status, exceptions, and stop. Private custody is referenced, not pushed. No need to restate all overnight history.

Oracle reviews milestone result. Driver waits after this handoff; no automatic method absorption, old script restoration or business launch. User's wish to potentially reuse legacy scripts is satisfied by an accessible preserved worktree, not by auto-reimporting them now.

## 5. Stop / reserved issues

Bounded failure handling: preserve achieved checkpoint, stop only affected action, report exact blocker. Do not silently cease maintenance for an ambiguous Herdr/sandbox error. Verify HERDR_ENV independently from command permission; approved execution escalation is not a forged environment.

No UCBIP write/pause change, no private data publication, no tag/release/remote-main push, no unrelated user's pane close, no third Pro. The explicit local main/legacy migration and necessary archive removals **are authorized here**; do not ask again merely because older docs prohibited main writes or legacy archival.

## 6. Oracle pane cleanup (parallel coordination, not a Driver product task)

Oracle retains p6 / Driver pD in t1 (two agents), method pG and check pT for this task. Ten completed named overnight worker panes E/F/P/K/H/M/J/Q/R/S are eligible for retirement after live identity+idle recheck; session history/cwd are recorded, native histories not deleted. User unnamed pN and all UCBIP panes untouched. Method/check share one worker tab; worker tabs max4, Oracle/Driver tab max2. Driver must not dispatch to a retired name from a historical roster.

## Owner final clarification · execution priority (overrides excess ceremony above)

Owner: “让当前仓库以后进来之后，默认工作区就是昨晚做的非常干净的night0930，原先那个版本完整地进入 worktree，不再造成干扰。” The actual night branch/path is `night/2026-10-01-workflow` / `.worktrees/night-2026-10-01`; do not create a second version because of the nickname.

Keep the implementation simple: preserve the complete legacy working state into its worktree; remove legacy active surfaces from new default root; make root main and entry docs the new version; independently read the entry and verify preserved bytes/index state. This is the required endpoint. The optional controlled-copy rollback demonstration above is unnecessary if complete legacy transfer and exact preservation have already been verified. Do not create extra recovery/test/role frameworks, duplicate legacy directories in new main, or expand documents to manufacture stages. Reuse existing Git and custody records. No need to physically move the core out of professional-workflow/ or rename the primary repository.
