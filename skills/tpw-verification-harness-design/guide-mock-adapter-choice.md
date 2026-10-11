# Mock / adapter choice guide · on-demand support (accepted bounded reference)

Status: accepted bounded reference (2026-10-02); creates no authority, generator, or gate. Source anchors and authored additions are marked.

## Use

On demand, when a design or test decision must cross a dependency boundary: choosing a test double/adapter, placing a seam, or deciding whether an internal interface needs to be exposed. When this support is needed, add the guide to the task's existing bound/read set; it is not mandatory loading. It mandates no test framework, gate, or module shape; the Charter binds applicability.

## Rules

1. **Classify the dependency first.** In-process (no adapter; test through the interface); local-substitutable (use the local stand-in; the seam is internal, no port at the external interface); remote but owned (define a port; production HTTP/gRPC/queue adapter, test in-memory adapter); true external (inject as a port; mock adapter in tests). *(Source: matt `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`, `skills/engineering/codebase-design/DEEPENING.md` §Dependency categories L5–25.)*
2. **Mock at system boundaries only.** External APIs; databases "sometimes" (prefer a test DB); time/randomness; file system "sometimes". Do not mock your in-process classes/modules, internal collaborators, or anything you control. *(Source: matt `skills/engineering/tdd/mocking.md` §When to Mock L3–14.)* Scope reconciliation *(authored)*: the owned-remote port strategy substitutes transport at a network seam; the "don't mock" list addresses in-process collaborators. They live at different seams; neither becomes an absolute policy about everything you own, and an existing local stand-in is preferred over a hand-written fake.
3. **Coverage boundary around the production adapter.** *(Authored engineering inference applying `behavior-claim-evaluation.md` §Use to adapter seams; the sources do not state this boundary.)* A double exercises only what the test actually calls: if the test double directly returns a ready domain object, the replaced adapter's request construction, transport and response mapping are not executed. If the risk or claim is in that adapter or its mapping, observe the adapter at its own surface — a local stub or recorded fixture is one option for contract mapping; a claim about a real Provider, actual SDK, wire behavior or deployment needs an appropriate real leg under the task's existing authorization (a green substitute does not establish it, and this guide does not require a real leg for every task). Or state which real normalization function runs under which test: moving logic into an adapter that the test double still replaces does not change coverage. Record the uncovered part; this is not a universal no-network rule.
4. **Design mockable interfaces.** Inject external dependencies rather than constructing them; prefer SDK-style per-operation functions over one generic fetcher: each mock returns one specific shape, no conditional logic in test setup, visible endpoint usage. *(Source: mocking.md §Designing for Mockability L16–59, incl. L55–59.)*
5. **Seam discipline.** One adapter means a hypothetical seam; two adapters (usually production + test) mean a real one — don't introduce a port unless at least two adapters are justified. Internal seams stay private, used by the module's own tests; do not expose them through the interface just because tests use them. The interface is the test surface. *(Source: matt `codebase-design/SKILL.md` §Principles L62–65; `DEEPENING.md` §Seam discipline L27–31.)*
6. **Replace-don't-layer, narrowly.** Source background: old tests on shallow modules become waste once tests at the deepened interface exist. *(Source: DEEPENING.md §Testing strategy: replace, don't layer L32–37.)* Adoption keeps the current method's narrow condition: replace or remove old coverage only when the replacement demonstrably covers its accepted claim and deletion is already authorized. This is not an "always delete old unit tests" policy.

## Counterexample (authored; true failing case)

Scenario: an order module depends on an owned pricing service (remote but owned). Contract fixture: `GET /price?sku=X → 200 {"data":{"unit_price_cents":1200,"discount":null}}`.

The production adapter assumes a flat body (`body.unit_price_cents`); the real field is nested under `data`, so it reads `undefined`, prices the order at 0, and production gives the order away.

- Port-level tests are green: the in-memory adapter returns the correct domain object `{unitPriceCents: 1200, discount: null}`; the production parsing path never runs. This is the mislabeled surface.
- Correct test surface (task-local; no global integration gate): observe the production adapter against a local stub/recorded fixture covering nested/missing/null shapes and assert request + parsed output, with the mapping path actually invoked (this maps contract shapes; a real-Provider/SDK/wire/deployment claim needs the appropriate real leg under existing authorization); alternatively, name which real normalization is called by which test and move it where that test actually executes it — moving it into an adapter that the test double still replaces does not change coverage.
- Second variant, correctly attributed: the defect is in an in-process collaborator (order × inventory) that the test mocked as "as intended". Fix: use the real collaborator directly — not the same operation as substituting transport at a cross-network port.

## Conditions and exceptions

- Applies to design/test decisions at a dependency boundary; not to every unit test.
- `sometimes` for DB/file system: prefer a real substitute (test DB, temp dir) when available; state the choice and its coverage.
- Do not expose internal seams for tests; if a test must reach past the interface, suspect the module shape rather than exporting internals.

## Limits

- No new gate, validator, mandatory mock/port/DI, or test framework; no runtime claim.
- Does not change responsibility ownership or task authority; the Charter remains binding.

## Source anchors

| Source | Pin / path | Section |
| --- | --- | --- |
| mattpocock-skills | `c55ee460…`, `skills/engineering/tdd/mocking.md` | §When to Mock L3–14; §Designing for Mockability L16–59 |
| mattpocock-skills | `c55ee460…`, `skills/engineering/codebase-design/SKILL.md` | §Principles L62–65; §Designing for testability L69–80 |
| mattpocock-skills | `c55ee460…`, `skills/engineering/codebase-design/DEEPENING.md` | §Dependency categories L5–25; §Seam discipline L27–31; §Testing strategy L32–37 |
