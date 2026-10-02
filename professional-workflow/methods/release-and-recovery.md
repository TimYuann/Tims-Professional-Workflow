# Release and recovery · candidate method body

- **Status:** candidate distilled under `docs/absorption/2026-10-02/reviews/ORACLE-REVIEW-A1-ADDY-CD.md` (C4, 2026-10-02, source `addy@2686b620`) and further extended under `docs/absorption/2026-10-02/reviews/REVIEW-GATE2-A4-CURSOR-DEF.md` (G05 gate-status counterexample, G04 gate-answer semantics, 2026-10-02, source Cursor `ecc249f1`); not yet an accepted reference; creates no authority, trigger, or gate. A fixed-diff review still applies.
- **Method owner when bound:** D/E plan the change, its rollout and its recovery path; the go/no-go decision, risk acceptance and any external communication stay with the authority that actually owns them.

## Use

Use when a change involves persistence, external behaviour, deployment, or a staged rollout. A fully local change that can be discarded at any time with no external observable effect does not need this method.

Four different things are often called "release". Keep them separate, because closing one does not close the others:

- **deployed** — the artifact is present in the target environment
- **enabled** — the feature is active for someone (flag on, route serving, job scheduled)
- **accepted** — the intended user path actually works and is observed to work
- **shut down** — the old path is removed and the temporary machinery (flag, dual path, migration task) is gone

**Deployed is not enabled, and enabled is not usable.** A deployment that reports success while the user path fails is a deployment, not a release.

## Preconditions

1. **Deployment can be separated from enablement.** If it cannot, staged/flag-off rollout is not available; state that as a design gap rather than imitating a rollout. It does **not** follow that there is no recovery path: an atomic release with no flag is still recovered by redeploying a compatible previous artifact or rolling forward, and a small service that cannot stage still has whatever redeploy/restore capability it actually runs. Name separately which staged capability is missing and which recovery mechanism is actually available; exercise it under valid authorization, and if it has never been exercised, report it as a plan rather than a capability. Do not claim that rollout is available, or that recovery is impossible, without checking.
2. **A baseline exists.** Every threshold below is *relative to a baseline*. Without a baseline there is no "2×" to compare against.
3. **The recovery path is verified, not merely documented.** A written rollback that has never been exercised is a plan, not a capability.

## The rollback plan (four parts; a missing part means there is no plan)

- **Trigger conditions.** Which signals cause a rollback — error rate relative to baseline, latency, data integrity, security, a user-reported failure pattern.
- **Rollback steps.** Which action comes first (turn the flag off, or redeploy the previous version), how the rollback is verified, and who is told.
- **What happens to the data.** Data written by this change is preserved, cleaned up, or needs separate reconciliation. Code rollback does not roll data back.
- **Time to roll back, as a number.** Give the magnitude for each mechanism the task actually has — flag off, redeploy, database action. "Fast" is not a duration; the source's `< 1 min` / `< 5 min` / `< 15 min` figures are examples, and a real plan states the measured or estimated value for its own mechanisms.

## Staged rollout: three decisions relative to the baseline

Every stage of a rollout must be able to go three ways — not two:

| Decision | Signal |
| --- | --- |
| **Advance** | the metric is near the baseline; no new failure class |
| **Hold and investigate** | the metric is clearly worse than baseline but not at the rollback line |
| **Roll back** | the metric crosses the rollback line, or integrity/security is in doubt |

Also read the **burn rate**, not only the current value: consuming the allowed error budget faster than the baseline pace is a hold signal even while each individual threshold is still green. A green snapshot with a rising burn is not "fine".

Source example thresholds (error rate within 10% / 10–100% / >2×; P95 latency within 20% / 20–50% / >50%; error-budget bands >20% / 0–20% / exhausted / reset; percentages 5 → 25 → 50 → 100; monitoring windows 24–48 h; flag cleanup within two weeks). None of these is a library rule. Adopting a threshold requires the service's actual SLO, its actual budget, and the authority that owns that policy.

**When there is no real traffic or no staged-rollout capability**, use the deployment and recovery evidence that actually applies — deploy verification, a dry-run recovery, an authorized synthetic request through the real path — and state the missing user-facing evidence honestly. Do **not** fabricate a canary result or present a synthetic check as user-facing evidence.

## Flags

If a flag is used to stage the rollout:

- every flag has an **owner** and an **expiry**; an unowned, never-expiring flag is permanent complexity
- after full rollout, remove the flag and the dead path together (the source's two-week window is an example)
- **do not nest flags** — combinations multiply and the test matrix stops being real
- **test both states**; a flag whose off-branch is never exercised is an untested code path carrying production risk

## Rollout gates and the error budget

The error budget is a policy signal, not a negotiation: what action follows when the budget is low or exhausted comes from the service's error-budget policy and its owner. The source's four bands (>20% ship normally; 0–20% slow rollouts, no high-risk changes; exhausted freeze feature work; reset resume and bake in the fix) are one concrete policy example. The method does not invent the bands, and a plan or dashboard does not by itself authorize a release.

**A gate or status field is not release permission.** A null, pending, `UNKNOWN` or not-yet-decided value is not "clear"; a review-required flag is not an allow; a rollup that is merely "not FAILURE" is not a pass; and a structurally correct field does not mean the required policy was satisfied. A previously green CI run or an automated review approval is not risk acceptance for this object, and a `READY` state is neither merged nor released. A default "(no answer) = accepted risk" field is not a decision: resolving a gate needs a real answer, and a legitimate fallback can only come from a previously valid, non-reserved delegation.

## Observation after enablement

The first hour after enabling is when "deployed" is tested against "usable". The source's checks are a usable starting set: the health check returns successfully, error monitoring shows no new error class, latency shows no regression, the **critical user flow is exercised by hand**, logs are flowing and readable, and the rollback mechanism is confirmed ready (a dry run where possible). These are observation steps, not a universal gate; the actual set follows the change's critical path.

## Recovery and data

- State whether the change's data is reversible. If it is not, say what the backup/restore or forward-fix path is, what would be lost, and who accepted that risk.
- A recovery path that depends on a human action must name who acts and how they are reached — inside the existing valid delegation, not by assuming it.
- **Notification and actual deployment inherit the task's existing valid delegation.** This method does not grant reach, access, or permission to notify external parties; a communication plan that is not covered by the current authorization needs its own decision.

## Limits

- Not every release needs staging, a warning-free build, the full e2e suite, a feature flag, external services, or a notification action. Which of these are needed follows the change and the accepted quality policy.
- The rollout percentages, time windows, latency/error multipliers and budget bands above are source examples. They are not this library's thresholds, and using one requires the actual SLO, budget and authority.
- A plan, a checklist, or a dashboard is not release authority. Risk acceptance and the go/no-go decision remain where the project's authority places them.
- Continuous-integration gate wiring belongs to the quality-policy method; this method states rollout and recovery behaviour and does not duplicate the gate table.

## Source anchors

| Source | Retained contribution |
| --- | --- |
| Addy Osmani, `addyosmani-agent-skills` at `2686b620fc1fed2e8f60c704839c766b8594c6b6`, `skills/shipping-and-launch/SKILL.md` (`Feature Flag Strategy`, `Staged Rollout`, `Rollout Decision Thresholds`, `When to Roll Back`, `Monitoring and Observability`, `Post-Launch Verification`, `Error Budget Release Gate`, `Rollback Strategy`, `Red Flags`) | Deployment/enablement/acceptance/shutdown distinction; flag owner, expiry, no nesting, both states tested; advance/hold/rollback relative to a baseline; burn rate as a hold signal even when individual thresholds pass; the four-part rollback plan with a time magnitude; data reversibility; first-hour verification including the critical user flow; error-budget policy as an owner decision. |
| Same pin, same file (`The Pre-Launch Checklist`, `Common Rationalizations`) | The deployed-is-not-usable mechanism. The full pre-launch checklist (code quality, security, performance, accessibility, infrastructure, documentation) is not adopted as a universal gate; its applicable parts follow the actual change and the accepted quality policy. |
| Cursor plugins, `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`, `pstack/skills/poteto-mode/scripts/watch-pr/policy.ts` (`resolveChecks` / gate status rollup) | A gate or status field is not release permission: null/pending/`UNKNOWN` is not clear, review-required is not an allow, "not FAILURE" is not a pass, structural fields do not satisfy the required policy, prior CI green or automated approval is not risk acceptance, `READY` is neither merged nor released, and a default "(no answer) = accepted risk" field is not a decision. The watcher/rules are not ported. |

Narrowed from the source: the specific thresholds, rollout percentages, time windows and budget bands are examples rather than rules; staging, no-warning builds, full e2e and flags are not required for every release. The source's "BLOCKED + rollup not FAILURE/ERROR → allowed" rule is rejected: unknown or review-required status is not an allow, and a gate's structural fields are not proof the required policy was met. The Cursor watcher and rules are not ported, and a READY state grants no merge or release authority.
