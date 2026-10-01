# Charter example · local behavior-preserving fix

- **State:** illustrative M2 binding; not an active grant
- **Profile:** `profiles/implementation.md` (relative to the `professional-workflow/` package root)
- **Instance:** `<implementation instance>`

## Task and delegation

- **Task / outcome:** Repair one known local defect in an isolated fixture while preserving its existing input, output, and error contract.
- **Delegation source:** The concrete task request must identify the fixture and grant local implementation authority. The accepted behavior reference and failure observation must be cited before this example is activated.
- **Object scope:** The affected helper and its local test seam. This expected touch set does not itself grant write permission.
- **Accepted inputs:** The cited behavior contract and a deterministic failure observation, each with a fixed version or digest and authority.
- **Applicable methods:** `methods/local-defect-feedback-loop.md` (relative to the package root). Accepted M4 source: commit `013659331c8c5f9f54b866b393972a03d7938773`, SHA-256 `3ca23a74a1a1890123bbab01a114aba813d7e20a7ffcb21b7b2289d5047cb32c`; the M5 snapshot SHA-256 `1ba8f8f2fb46a0094c22e7ac946e27f30a27b1ce25e201fd5ede819ddc2e4215` is historical — current candidate bytes are recorded in `methods/README.md` §Status and source trace and in the night candidate manifest. F's evaluation method, if needed, belongs in F's own Charter.

## Work and limits

- **Responsibility:** Implement the repair and report what the code and fixture reveal.
- **Delegated decisions:** Choose local algorithm, helper organization, and regression-test seam while the accepted contract remains unchanged.
- **Preserve / do not do:** Preserve callers, public behavior, and existing error semantics. Do not redesign interfaces, change domain meaning, touch production data, or perform external actions.
- **Tools and actions:** Use only the named offline fixture and its permitted commands after the task request grants them. No production service, migration, release, or UCBIP access.

## Handoff and return

- **Deliver:** Patch, self-check commands and observations, deviations, and unresolved facts.
- **Independence:** A separate instance evaluates the resulting version against the cited contract; E's self-check is evidence input, not the independent conclusion.
- **Recall:** If the contract is missing, contradictory, or cannot be kept within the granted scope, tell Driver which object, fact, and impact changed and stop only dependent work. Driver routes to the relevant decision authority; Voice is involved only for a human-reserved decision.
- **Acceptance / verification / action / closure:** The task request names acceptance and closure authority. F evaluates the fixed patch. A successful local check does not authorize release or deployment.
