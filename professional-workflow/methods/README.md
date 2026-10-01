# Selected methods · M4 accepted references

Profiles remain the owners of reusable responsibility mental models; this directory owns the selected method bodies. The method links below resolve bounded needs for the two M3 exercise paths. Use one when the task Charter binds it; this list does not add applicability triggers, authority, or a fixed phase chain.

| Task need | Method file | Judgment focus |
| --- | --- | --- |
| Reproduce and repair a known local defect | `local-defect-feedback-loop.md` | E, with evidence supplied to F |
| Plan a change with cross-module dependencies | `cross-module-design.md` | D, preserving B/C ownership |
| Evaluate a specific behavior claim | `behavior-claim-evaluation.md` | F |

## On-demand guides

| Support need (on demand) | Guide file | Boundary |
| --- | --- | --- |
| Record or hand off evidence that may contain sensitive artifacts | `guide-redacted-evidence.md` | evidence custody and HITL split; no verdict/authority change |
| Choose a test double/adapter across a dependency boundary | `guide-mock-adapter-choice.md` | design/test-surface choice; no mandatory gate |

These guides are on-demand references at demonstrated knowledge gaps; they add no applicability triggers, authority, or fixed phase chain. When the support is needed, add the relevant guide to this task's existing bound/read set; no mandatory loading for tasks without that need. The task Charter still binds applicability, independence, and action permission.

## Status and source trace

The accepted M4 source objects are fixed at commit `013659331c8c5f9f54b866b393972a03d7938773`, tree `2fc8db5e9bbd0a2c378882c89c2328505fddee`. M4 acceptance applies to those exact source digests. The M5 candidate carries package-status/source-trace metadata edits; it is not byte-identical to the accepted M4 tree, and this directory does not claim those M5 package bytes have been accepted. The table makes both identities explicit. The normative method body remains linked to its M4 source; task applicability, independence, and authority remain in the actual Charter.

| Package method file | Accepted M4 SHA-256 | Current M5 candidate SHA-256 |
| --- | --- | --- |
| `local-defect-feedback-loop.md` | `3ca23a74a1a1890123bbab01a114aba813d7e20a7ffcb21b7b2289d5047cb32c` | `1ba8f8f2fb46a0094c22e7ac946e27f30a27b1ce25e201fd5ede819ddc2e4215` |
| `cross-module-design.md` | `30066c8b3ccee2b85e98c8bc36975f57161e2c93d0bd71c9c668b27bf79bae6f` | `ab0a0bc03448407479fe82b92b2355384e7f2acf49c2ff3026882670f955a0a5` |
| `behavior-claim-evaluation.md` | `06b0692290a9ce8cdc7048b33a89ec21f3636ee00138a613121ec4b72457af06` | `cfacc0f57cedadc6360ad0338645e43740dad4b1e15cc6876088eb89b4034f02` |

The accepted M4 selection entry `methods/README.md` itself had SHA-256 `72a6ffb46277e3974f27d41e078623ce5b46865074898dae24cbdb6de2205e73`. This M5 selection entry is a package-status derivative; its exact bytes are fixed by the M5 package tree/manifest, not by the M4 digest. Acceptance of either object does not establish actual task binding, final M3 coverage, runtime dependency closure, or whole-package qualification.

| Source repository | Fixed locator and pin | Used by |
| --- | --- | --- |
| Matt Pocock skills | `https://github.com/mattpocock/skills.git` · `c55ee46073ed923f86ce59a5eb3b6d895095d1b7` | local defect; cross-module design |
| Addy Osmani skills | `https://github.com/addyosmani/agent-skills.git` · `2686b620fc1fed2e8f60c704839c766b8594c6b6` | limited debugging and interface additions |
| Cursor plugins (verify-this) | `https://github.com/cursor/plugins.git` · `ecc249f1e306fc64ddf83c7bed16cacf7c2239db` | behavior-claim evidence |

These locators preserve source identity; pins and in-file anchors identify the reviewed bodies. The fixed Backbone projection is bundled under `../authority/` with its source commit and digest.

Deferred alternatives: the S2 bug-fix playbook's control/loop/model/PR defaults, `DESIGN-IT-TWICE` and its parallel-agent count, idempotency/retention rules, and the `interrogate`/`code-review` lenses. They were outside the two active M3 method needs; no alternative became a mandatory gate. No S4/S5 article-derived method is included. The X original remains `UNVERIFIED`; cached article notes are locator evidence only.

Nothing here grants authority, permissions, risk acceptance, or permission for consequential actions.

## Scope and current state (2026-10-01)

This selection entry ships three method bodies (`local-defect-feedback-loop`, `cross-module-design`, `behavior-claim-evaluation`) plus the two on-demand guides above. It does not contain `path-trace`, `blast-radius`, `design-compare` or `drive-preview`; those four retired names have no equivalent body here and are not revived. Current package acceptance/status is recorded in `docs/overnight/2026-10-01/M6-FINAL-ACCEPTANCE.md` and the later correction/candidate records; the M4/M5 digests above describe their own snapshots. The 2026-10-01 corrected candidate extends the three methods at demonstrated gaps and adds the guides; it awaits the directed independent recheck and does not by itself grant authority or task applicability.
