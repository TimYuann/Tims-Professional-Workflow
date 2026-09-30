# Professional Workflow · local candidate

This directory is the greenfield package root. The accepted responsibility boundary is `docs/RESPONSIBILITY-BACKBONE.md` (design baseline 1); it defines responsibilities, not this package's task permissions.

## Use

1. Select the closest preset in [`profiles/README.md`](profiles/README.md).
2. Bind the current task with an [Instance Charter](charters/README.md), citing the actual delegation and accepted inputs.
3. Give the instance the Profile, Charter, and task-specific input in that order. For example:

   ```sh
   cat professional-workflow/profiles/implementation.md \
       professional-workflow/charters/examples/implementation-local-fix.md \
       path/to/current-task-input.md
   ```

The output is the startup prompt text. The final path is supplied by the caller and must contain the current task facts and source references. Do not put task-specific authority in a Profile.

## State

The Profile content is accepted M1 input at the hashes recorded in `docs/overnight/2026-10-01/ORACLE-ACCEPTANCE.md`. Its method-entry labels describe needs, not mandates; selected source-based bodies are M4 candidates in `methods/` and remain unaccepted for downstream use. The Charter template and examples are M2 design candidates; they do not activate a real task delegation or prove a cold start. Nothing in this directory alone grants decision authority, permission to change an object, or permission to perform a consequential action.
