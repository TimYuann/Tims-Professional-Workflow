# Professional Workflow · 2026-10-02 absorption candidate

This directory is a self-contained package containing the 2026-10-01 accepted 21-file baseline plus the 2026-10-02 absorption deltas, each independently reviewed and integrated into the candidate. Prior baseline acceptance: `docs/overnight/2026-10-01/ABSORB-FINAL-ACCEPTANCE.md`; Oracle/Pro overall acceptance of the current 59-file candidate is not yet complete, and M1–M5 labels are historical snapshots only — they do not accept all current bytes. Its fixed responsibility boundary is bundled at [`authority/RESPONSIBILITY-BACKBONE.md`](authority/RESPONSIBILITY-BACKBONE.md); source commit and digest are recorded in [`authority/README.md`](authority/README.md). The Backbone defines responsibility boundaries. A task Charter must cite the actual delegation and does not gain authority from a Profile or this package.

## Use

1. Select a suitable [Profile](profiles/README.md) for the judgment needed.
2. Fill an [Instance Charter](charters/README.md) with the current task's actual delegation, accepted inputs, object scope, handoff, evaluator and permitted actions.
3. Consult the [method selection entry](methods/README.md). Bind only task-relevant method files in the task Charter; the Profile name alone does not activate them.
   For another repository introducing or vendoring this package, start from [ADOPTION.md](ADOPTION.md) (fixed-commit read or vendor, minimal entry, pinning/upgrade, pure-text consumption).
4. From this directory, assemble the Profile, any authority context the Charter needs, the filled Charter, its bound method files, and task-specific input in that order:

   ```sh
   cat profiles/implementation.md \
       charters/examples/implementation-local-fix.md \
       methods/local-defect-feedback-loop.md \
       path/to/current-task-input.md
   ```

The output is startup prompt text. Replace the illustrative Charter and task-input path with fixed, task-specific objects. Consult the bundled Backbone when a responsibility boundary matters; include only the context the active Charter needs. The task input must carry current facts and source references. Do not put task-specific authority in a Profile.

## Package state

The Profile content is the M1 accepted input at checkpoint `429a78b`; the method bodies and selection entry were accepted at M4 commit `013659331c8c5f9f54b866b393972a03d7938773`, tree `2fc8db5e9bbd0a2c37888282c89c2328505fddee`. M1–M5 labels in this package describe those snapshots and are not current acceptance; historical M5 snapshot bytes remain identified in `methods/README.md`. Current status: the prior baselines are accepted as recorded (M6 delivery 2026-10-01 `M6-FINAL-ACCEPTANCE.md`; 21-file corrected baseline `ABSORB-FINAL-ACCEPTANCE.md`, identity in `ABSORB-CORRECTED-CORE-MANIFEST.md` Rev.7). The 2026-10-02 absorption candidate integrates all independently reviewed deltas; its Oracle/Pro overall acceptance has not yet been completed, so no historical acceptance implies acceptance of all current package bytes. Each task Charter binds any method it uses; this package grants no downstream authorization.

Nothing in this directory alone grants decision authority, permission to change an object, risk acceptance, or permission for a consequential action.

## Optional adoption example (non-normative pointer)

An optional adoption example lives outside this package at `../adoption-examples/ucbip.md`. It is non-normative: this package does not own downstream UCBIP semantics, authority, or current state, the example grants nothing, and it does not affect the assembly or package state described above.
