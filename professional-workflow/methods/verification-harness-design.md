# Verification harness design · on-demand method (MG-5)

- **Method owner:** F for the claim and its evidence; E for running the environment. The harness is an instrument, not a verdict.
- **Status:** on-demand reference at a demonstrated gap (a scripted way to drive the real app/service and maintain it); a task Charter decides applicability. It adds no gate, test framework, or mandatory feature map.

## Use

Use when a claim about a real user-facing path needs evidence that only driving the actual app/service can provide and the repo has no scripted way to do it — or when such a harness has drifted. It complements, and does not replace: `behavior-claim-evaluation.md` (one applicable claim/verdict path), `guide-mock-adapter-choice.md` (which surface substitutes for which dependency), and `guide-redacted-evidence.md` (evidence custody). Fixture, pure-logic and internal setup evidence remain legitimate for the claims they fit; this method exists for the claims those cannot settle. A real leg is required only for the claims that need one, and the harness scope follows the delegation: a full pass across every feature is for a delegation that asked for exactly that. *(Source: cursor `ecc249f1…`, `pstack/skills/create-verification-skill/SKILL.md` L9–21; the claim-driven real-leg boundary is from the review and the R3 ruling.)*

## Discover

Interview the repository, not only the user; ask a person only for what the code cannot tell you *(Source: `create-verification-skill/SKILL.md` §1 L11–21)*:

- **Surface:** what does a user actually touch (web UI, CLI/TUI, desktop app, API, mobile, library)? Pick the primary one, note the rest.
- **Run:** how does the app start locally? Prefer the repo's own documented dev command. Note ports, env vars, seed data, auth.
- **Drive:** how can an agent interact programmatically? Existing harnesses first (Playwright/Cypress specs, expect scripts, PTY helpers, curl-able endpoints, debug ports); only then a generic recipe.
- **Observe:** what evidence can be captured (screenshots, terminal transcripts, response bodies, logs, exit codes, DB state)?
- **Isolate:** can two instances run side by side (ports, data dirs, profiles)? If not, say so in the harness; refusing to double-drive a shared instance beats corrupting the user's session.

If the checkout does not build or start as-is, fix that first or report it precisely before writing the harness: a harness written against a broken base teaches wrong steps. Creating scaffolding needed only because of an irrelevant missing asset is allowed when marked as scaffolding and removed in cleanup. *(Source: same section L21.)*

## Recipe

The harness must carry, from this repo rather than examples *(Source: §2 L25–32)*:

- **Launch:** the exact command, how to tell it is ready (log line, port answering, prompt), and teardown; for a short-lived CLI/TUI, build once and start each drive in its own isolated session.
- **Doctor:** one read-only check answering "is this instance worth driving?" — process up, right version/build, port owned by us, auth valid. Run it when the state is in question (a fresh instance, a fresh session, after a failed or surprising drive), not as a fixed gate before every action; where doctor cannot see the failure (a wedged UI on a healthy process), reset to a known state or relaunch rather than hoping. *(Source: same section L28; the review's doctor boundary.)*
- **Drive:** the harness recipe with real selectors/commands; prefer stable handles (ARIA labels, data attributes, prompt strings, route paths) over coordinates and tab order.
- **Evidence:** what to capture for a proof and where it goes. Proof standards: exercise the real user path, not internal setters or test-only endpoints; capture the action and the resulting state, not just the final screen; verify side effects (files written, rows inserted, messages sent) alongside what is visible; substitute/mock only where a production boundary already isolates the external system. A dry-run or test mode must be verified by observing what it actually skips (files, network, refs) rather than trusting its name — some dry-runs still touch the network.
- **Cleanup:** how to tear down instances the run created; kill what you started, never by process name. Cleanup removes instances and scratch state, **never the evidence** — proof artifacts survive teardown at a named location. *(Source: same section L31.)*
- **Helpers:** every shipped script is executable and its invocation is in the body; a helper the reader must reverse-engineer is not a helper. *(Source: same section L32.)*

## Prove and limits

- **Prove before handing over.** Run the harness's own instructions end to end once: launch, doctor, drive one mapped feature, capture evidence, clean up. After cleanup, confirm the evidence still exists where it was promised — a cleanup that eats the proof fails the step. Fix what fails and run cleanup after every failed iteration so broken attempts do not strand processes or ports. A harness that was never executed is a draft, not a deliverable. *(Source: §4 L38–40.)*
- **Feature map — where the repo wants one.** One file per user-facing feature answering, from the user's point of view: what it is, how to reach it, how to drive it, and what observable end state proves it. The map records *how to observe*; it does not define what the behavior should be — B/C own the accepted behavior. When the product disagrees with the map, first check the accepted version; a mismatch is doc drift or a product regression, and updating the docs is not the default fix. Not every repo needs a map; this method does not require one. *(Source: §3 L34–36; `maintain-verification-skill/SKILL.md` §Edit scope L21, §Pass 5 L35.)*

## Maintain

The unit of upkeep is the **feature**, not every sentence *(Source: `maintain-verification-skill/SKILL.md` L9–17)*:

- Outcomes are **clean / changed / blocked** — work states, not the three-state verdict; say which one applies.
- **Edit scope:** only the verification harness's own directory (skill body, feature files, its scripts). Never edit product code during the pass: a behavior the map describes that the app no longer does is either doc drift (fix the map) or a product regression (report it, do not paper over it in docs). *(Source: same file L21.)*
- **Pass:** index hygiene (missing/extra/duplicate/dead entries); a read-only source wave per feature (how the feature works, likely drift with citations, one live recipe); reconcile (merge overlapping recipes, spot-check cited drift, sweep recent churn for missing surfaces); a **live pass** over the features this pass affects or whose claims need a real leg — the source wave can look clean and still miss runtime drift, so the live leg is required for the affected claims rather than for every feature, and a harness change re-drives the recipes it touched. Run across all features only when the delegation itself is a full-feature audit. Keep three invariants: doctor the instance when its state is in question, evidence survives every cleanup, and nothing a drive started outlives its usefulness; a doctor failure caused by harness drift is drift — fix it under edit scope and retry the affected path once. *(Source: §Pass L23–33; the affected-features/claims scoping is the R3 gate ruling.)*
- **Triage:** wrong/missing user-facing description → doc drift; behavior the harness cannot drive → harness gap (the fix is re-driven live before shipping); behavior actually broken → product gap, recorded for the owner and kept out of this change. *(Source: §Pass 5 L35.)*
- A feature that cannot be reached is reported with its concrete prerequisite (auth, entitlement, OS, external state) and the route attempted; if the map omits that prerequisite, that is drift. *(Source: §Pass 4 L33.)*

## Cleanup and evidence

- Cleanup removes instances and scratch state; proof artifacts survive at a named location and are checked after teardown, not assumed. *(Source: `create-verification-skill/SKILL.md` L31; `maintain-verification-skill/SKILL.md` §Pass 4 L33.)*
- Cleanup must not destroy evidence that custody requires; but raw sensitive retention and its expiry still follow `guide-redacted-evidence.md` and the task's policy — "never delete evidence" is not a reason to keep secrets.
- Fixing a broken base, generating scaffolding, or cleaning another instance's residue requires existing action authorization; a broken environment is recorded UNVERIFIED rather than absorbed into the claim. *(Source: the review's broken-base/authorization boundary.)*

## Limits

- No test framework, no mandatory feature map, no requirement that every repo be driven live for every maintenance task, and no per-action health gate. The doctor is a state check, not a ritual.
- The harness is evidence infrastructure: it does not set the claim, the threshold, the verdict, acceptance, or action permission. The accepted behavior stays with B/C; the task's policy and Charter define what evidence a claim requires; F designs and judges the evaluation. `behavior-claim-evaluation.md` is one applicable path within its own scope — not the sole owner of every claim, threshold, or verdict, and not a substitute for B/C's accepted behavior or the task's policy. *(The ownership scoping is the R3 gate ruling.)*
- Substitution choice stays with `guide-mock-adapter-choice.md`; this method does not re-derive it.
- Any harness that was generated but not executed is a draft; this method's own sources were read, not run, and their runtime behavior is not claimed here.

## Source anchors

| Source | Retained contribution |
| --- | --- |
| cursor-plugins `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`, `pstack/skills/create-verification-skill/SKILL.md` (§1 Interview L11–21; §2 Generate L23–32; §3 Seed the feature map L34–36; §4 Prove L38–40; §5 Maintenance pointer L42–44) | The surface/run/drive/observe/isolate interview; launch/doctor/drive/evidence/cleanup/helpers; proof standards including dry-run observation; run-it-once and evidence-survives-cleanup; the optional feature map and its user-POV shape. |
| cursor-plugins `ecc249f1…`, `pstack/skills/maintain-verification-skill/SKILL.md` (§Outcomes L11–17; §Edit scope L19–21; §Pass L23–37) | clean/changed/blocked as work states; edit-scope discipline (doc drift vs product regression); index hygiene, source wave, reconcile, live pass, the three pass invariants, triage. |

Authored additions: the claim-driven framing in Use, the doctor-as-state-check boundary, the "harness never executed is a draft" statement restated for this package, the cleanup-vs-custody sentence, the authorization boundary for scaffolding/other instances, and the Limits.
