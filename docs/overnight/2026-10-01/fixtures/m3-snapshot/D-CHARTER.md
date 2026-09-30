# M3 case 2 · D technical-planning Charter

**State:** active for this synthetic exercise only
- **Profile:** `professional-workflow/profiles/technical-planning.md` (M1 accepted; SHA-256 `d53da06edc99af3bcfc93c744af5f2cc8d512430d318a8b13b1b7f42652d74aa`)
- **Instance:** `tpw-night-m3-design`

## Task and delegation

- **Task / outcome:** Produce a bounded technical Plan that lets a separate E instance implement the accepted M3 case 2 B/C contract in this fixture.
- **Delegation source:** Owner-authorized offline exercise in `docs/OVERNIGHT-WORKFLOW-PLAN-2026-10-01.md` at fixed M3 plan baseline `496b0676e302e2d0eafba129ff61de4c203d258a`, which delegates the technical Plan judgment for this fixture only.
- **Object scope:** Read the snapshot fixture and write only `TECHNICAL-PLAN.md` in this directory. Do not implement, edit fixture source/tests, B/C objects, method files, or package Profiles.
- **Accepted inputs:** `BEHAVIOR-CONTRACT.md` v1 (SHA-256 `86dd6664b73de07ceefdbc5f4d03e09f49b4b1f2ee11cb6a80e48c251176555c`) and `DOMAIN-SEMANTICS.md` v1 (SHA-256 `15537d71d100dde30075f724c1ef79bc0d4e6a76a179f7f82d7f6c6b286cda06`), both accepted by `tpw-night-m3-bc` for this exercise; bundled Backbone export `professional-workflow/authority/RESPONSIBILITY-BACKBONE.md` (SHA-256 `ce82a70016a4a3fc234ea287f39aac8d79a260ddf13747c4fb705bda580453ba`).
- **Applicable method:** `professional-workflow/methods/cross-module-design.md` from accepted M4 commit `013659331c8c5f9f54b866b393972a03d7938773` (SHA-256 `30066c8b3ccee2b85e98c8bc36975f57161e2c93d0bd71c9c668b27bf79bae6f`). The method does not select B/C meanings or expand this delegated Plan authority.

## Work and limits

- **Responsibility:** Convert the accepted B/C commitments and observed system structure into a sufficient technical Plan.
- **Delegated decisions:** Make and accept the technical Plan for this synthetic fixture while preserving the cited B/C meanings and exercise envelope. This authority does not extend to changing B/C.
- **Preserve / do not do:** Keep behavior and domain decisions with their B/C owners. Do not select new product behavior, reinterpret domain terms, alter B/C inputs, perform implementation, migrate data, or cause external effects.
- **Required output:** State `Commitments`, `Delegated Decisions`, and `Recall Conditions`; cite the inputs and owners they depend on. Do not enumerate every helper or prescribe choices that leave all commitments and constraints unchanged.
- **Tools and actions:** Read only the supplied M3 fixture and frozen design inputs. No network, production or UCBIP access.

## Handoff and return

- **Deliver:** Candidate `TECHNICAL-PLAN.md` with assumptions, affected dependencies, validation basis and unresolved points.
- **Independence:** `tpw-night-method` will independently challenge the fixed Plan before E receives it. A finding returns to the D owner for a decision/revision; the challenger is neither Plan author nor acceptor.
- **Recall:** If B/C inputs conflict or cannot be satisfied within the exercise envelope, identify the affected accepted object, observed fact and impact; return it to Driver for routing to the relevant authority. Do not silently alter B/C.
- **Acceptance / verification / action / closure:** D owns acceptance of this fixture's technical Plan within the cited delegation; Driver checks the inputs and version binding, not the substantive design. F later evaluates implementation. No deployment, migration, release or overall M3 closure is granted here.
