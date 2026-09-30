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

The integrated M1 Profile content and M4 bounded methods/selection entry have milestone acceptance recorded in [`../docs/overnight/2026-10-01/ORACLE-ACCEPTANCE.md`](../docs/overnight/2026-10-01/ORACLE-ACCEPTANCE.md). M1's accepted bytes remain the fixed input; its method-entry status still does not make task-level method binding. The Charter template and examples are accepted as a design reference, not an active grant or proof of a successful cold start. M5 package integration and M6 clean-package qualification are still in progress.

Nothing in this directory alone grants decision authority, permission to change an object, risk acceptance, or permission for a consequential action.
