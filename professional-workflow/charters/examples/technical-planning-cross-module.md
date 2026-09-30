# Charter example · cross-module technical Plan

- **State:** illustrative M5 binding; not an active grant
- **Profile:** `professional-workflow/profiles/technical-planning.md`
- **Instance:** `<planning instance>`

## Task and delegation

- **Task / outcome:** Produce a bounded technical Plan for an accepted change that spans module boundaries.
- **Delegation source:** The concrete task request must grant planning authority and name the fixture or repository and task objective. This example grants no implementation or external action.
- **Object scope:** The technical Plan and the specific system paths needed to establish current facts. Do not infer permission to change code or persistent data.
- **Accepted inputs:** Versioned behavior/domain commitments and current source facts, each with owner and acceptance state.
- **Applicable methods:** `methods/cross-module-design.md` from accepted M4 commit `013659331c8c5f9f54b866b393972a03d7938773` (SHA-256 `30066c8b3ccee2b85e98c8bc36975f57161e2c93d0bd71c9c668b27bf79bae6f`). This method preserves B/C ownership and does not create implementation authority.

## Work and limits

- **Responsibility:** Identify the technical coordination surface and delegated implementation interior required by the accepted commitments.
- **Delegated decisions:** Choose the interface facts and validation seam within the actual planning delegation.
- **Preserve / do not do:** Preserve behavior and domain meanings with their owners. Do not implement, change B/C commitments, accept risk, migrate data, deploy or release.
- **Tools and actions:** Read only the named local fixture or repository and the listed accepted inputs. Use no production service or UCBIP access unless a separate valid delegation explicitly permits it.

## Handoff and return

- **Deliver:** A compact Plan with Commitments, Delegated Decisions, Recall Conditions, evidence anchors and unresolved facts.
- **Independence:** A separate instance may challenge this Plan before implementation; a distinct evaluator later judges the fixed implementation. Record actual contributions and timing.
- **Recall:** If accepted commitments conflict or cannot fit inside the delegation, name the affected owner, fact and impact; pause dependent planning and return the issue to Driver for routing.
- **Acceptance / verification / action / closure:** The task request names who accepts the Plan and implementation separately. Planning does not authorize implementation or consequential action.
