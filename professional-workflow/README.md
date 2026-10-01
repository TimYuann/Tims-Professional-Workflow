# Professional Workflow · accepted local-adoption delivery (2026-10-01)

This directory is a self-contained package candidate. Its fixed responsibility boundary is bundled at [`authority/RESPONSIBILITY-BACKBONE.md`](authority/RESPONSIBILITY-BACKBONE.md); source commit and digest are recorded in [`authority/README.md`](authority/README.md). The Backbone defines responsibility boundaries. A task Charter must cite the actual delegation and does not gain authority from a Profile or this package.

## Use

1. Select a suitable [Profile](profiles/README.md) for the judgment needed.
2. Fill an [Instance Charter](charters/README.md) with the current task's actual delegation, accepted inputs, object scope, handoff, evaluator and permitted actions.
3. Consult the [method selection entry](methods/README.md). Bind only task-relevant method files in the task Charter; the Profile name alone does not activate them.
4. From this directory, assemble the Profile, any authority context the Charter needs, the filled Charter, its bound method files, and task-specific input in that order:

   ```sh
   cat profiles/implementation.md \
       charters/examples/implementation-local-fix.md \
       methods/local-defect-feedback-loop.md \
       path/to/current-task-input.md
   ```

The output is startup prompt text. Replace the illustrative Charter and task-input path with fixed, task-specific objects. Consult the bundled Backbone when a responsibility boundary matters; include only the context the active Charter needs. The task input must carry current facts and source references. Do not put task-specific authority in a Profile.

## Package state

The Profile content is the M1 accepted input at checkpoint `429a78b`; its generic method-need labels do not bind a method to a task. The M4 acceptance fixes the accepted method bodies and selection entry at commit `013659331c8c5f9f54b866b393972a03d7938773`, tree `2fc8db5e9bbd0a2c37888282c89c2328505fddee`. The current M5 candidate carries small package-status/source-trace edits to those files, so its shipped bytes are identified separately in `methods/README.md`; M4 acceptance does not itself accept the M5 package bytes or actual task binding. The M1-era “待 M4” labels remain in the frozen Profiles; for the three currently selected method references, use `methods/README.md`. This does not add applicability triggers; each task Charter binds any method it uses. The Charter template and examples are design references, not active grants. Current status: Oracle accepted the bounded PW-01/M6 local-adoption delivery on 2026-10-01 (record: `docs/overnight/2026-10-01/M6-FINAL-ACCEPTANCE.md`; corrected identity and R1/R2 verdict: `docs/overnight/2026-10-01/PW-01-FINAL-REPORT.md`). The historical M1–M5 labels above describe their own snapshots and are not current acceptance; this package grants no downstream authorization.

Corrected candidate (2026-10-01): the night branch carries a bounded correction of the absorption round — the three methods extended at demonstrated gaps plus two on-demand guides (see `methods/README.md`), source/ship identity clarifications, and entry pointers. It awaits the directed independent recheck and is not yet the accepted core identity; the accepted identity above still refers to its own object. The candidate's fixed identity is recorded in `docs/overnight/2026-10-01/ABSORB-RETURN-MILESTONE.md` and the later correction records (night branch only until the recheck closes).

Nothing in this directory alone grants decision authority, permission to change an object, risk acceptance, or permission for a consequential action.

## Optional adoption example (non-normative pointer)

An optional adoption example lives outside this package at `../adoption-examples/ucbip.md`. It is non-normative: this package does not own downstream UCBIP semantics, authority, or current state, the example grants nothing, and it does not affect the assembly or package state described above.
