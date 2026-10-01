# Professional Workflow · M5 integration candidate

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

The Profile content is the M1 accepted input at checkpoint `429a78b`; its generic method-need labels do not bind a method to a task. The M4 acceptance fixes the accepted method bodies and selection entry at commit `013659331c8c5f9f54b866b393972a03d7938773`, tree `2fc8db5e9bbd0a2c37888282c89c2328505fddee`. The current M5 candidate carries small package-status/source-trace edits to those files, so its shipped bytes are identified separately in `methods/README.md`; M4 acceptance does not itself accept the M5 package bytes or actual task binding. The M1-era “待 M4” labels remain in the frozen Profiles; for the three currently selected method references, use `methods/README.md`. This does not add applicability triggers; each task Charter binds any method it uses. The Charter template and examples are design references, not active grants. M5 integration and M6 clean-package qualification remain in progress.

Nothing in this directory alone grants decision authority, permission to change an object, risk acceptance, or permission for a consequential action.
