# Charter example · accepted cross-module snapshot contract

- **State:** illustrative M2 binding; not an active grant
- **Profile:** `professional-workflow/profiles/implementation.md`
- **Instance:** `<implementation instance>`

## Task and delegation

- **Task / outcome:** Implement a new snapshot/freshness behavior across the modules named in an accepted technical plan.
- **Delegation source:** The concrete task request must grant implementation authority for the isolated fixture and cite the accepted B/C commitments and D Plan. A missing or unaccepted reference means this example cannot be activated.
- **Object scope:** The modules and consumers covered by that Plan. Do not infer a file whitelist from the example; the Plan and task grant define the actual boundary.
- **Accepted inputs:** Versioned behavior and domain commitments plus a Plan that names Commitments, Delegated Decisions, and Recall Conditions, with their decision owners and acceptance state.

## Work and limits

- **Responsibility:** Implement the accepted cross-module behavior and surface implementation facts that affect the plan.
- **Delegated decisions:** Choose local algorithms, helpers, and test seams inside the Plan's delegated space.
- **Preserve / do not do:** Preserve accepted snapshot meaning, freshness ownership, shared interfaces, mismatch behavior, and validation basis. Do not edit upstream commitments, migrate persistent state, deploy, release, or cause external effects.
- **Tools and actions:** Use the named offline fixture and permitted commands only after the task request grants them. No production service or UCBIP access.

## Handoff and return

- **Deliver:** Patch, self-check observations, affected commitments, deviations, and remaining questions.
- **Independence:** A distinct instance challenges the relevant Plan before implementation; an evaluator who did not implement the candidate assesses the fixed result afterward. Record real contributions and timing for each object.
- **Recall:** If keeping a cited commitment requires a change outside delegated decisions, report the affected object, observed fact, and impact to Driver, then pause dependent work. Driver finds the authority that owns that boundary. Voice is used only for a human-reserved decision or human acceptance.
- **Acceptance / verification / action / closure:** The task request identifies acceptance, verification, consequential-action, and closure authority separately. Implementing or verifying the contract does not authorize migration, deployment, or publication.
