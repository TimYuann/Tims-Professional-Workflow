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

Use the selected Profile, the filled Charter, and task-specific inputs. The example below shows the deterministic text order; the package intentionally has no schema validator or general permission engine.

```sh
cat professional-workflow/profiles/implementation.md \
    professional-workflow/charters/examples/implementation-cross-module.md \
    path/to/current-task-input.md
```

`template.md` is the compact binding form. The examples demonstrate one Profile with different task scopes; they are not active grants and must not be used until their delegation and input references are replaced by real objects.
