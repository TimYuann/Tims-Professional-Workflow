# Instance Charters · M2 candidate

A Charter binds one use of a reusable Profile to the actual task. It cites the source of delegation and accepted inputs, then states this instance's responsibility, output, recall path, independence relation, and permitted tools/actions.

## Rules

- Choosing a Profile is composition, not authorization. A Charter records authority already granted elsewhere; writing “allowed” here does not create that grant.
- Identify the delegation source and the exact task/object scope. State accepted commitments with their versions and decision owners; separate acceptance, verification, action authorization, and closure.
- List decisions delegated to this instance and the boundaries it must preserve. Do not turn the initial expected file set into a permission list unless an authority explicitly made it a boundary.
- A changed or missing dependency goes to the authority that owns the affected decision. Use Voice only when a human-reserved decision or human acceptance is involved.
- State who authored, challenges, and evaluates the relevant object. Profile names and different labels in one session do not establish independence.
- Name the actual tools and action limits. Tool access does not grant permission; permission does not bypass tool restrictions.

## Assembly

From the `professional-workflow/` package root, use the selected Profile, only the authority context the Charter needs, the filled Charter, its method files, and task-specific inputs. The example below shows the deterministic text order; the package intentionally has no schema validator or general permission engine.

```sh
cat profiles/implementation.md \
    charters/examples/implementation-local-fix.md \
    methods/local-defect-feedback-loop.md \
    path/to/current-task-input.md
```

For a cross-module technical Plan, use `profiles/technical-planning.md`, include the bundled Backbone when its responsibility boundary matters, bind `charters/examples/technical-planning-cross-module.md`, and include `methods/cross-module-design.md` before the task inputs.

```sh
cat profiles/technical-planning.md \
    authority/RESPONSIBILITY-BACKBONE.md \
    charters/examples/technical-planning-cross-module.md \
    methods/cross-module-design.md \
    path/to/current-task-input.md
```

`template.md` is the compact binding form. The two implementation examples show one Profile with different task scopes; the planning example shows D's separate method binding. None is an active grant until its delegation and input references are replaced by real objects.
