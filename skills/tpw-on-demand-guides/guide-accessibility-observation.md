# Accessibility observation · on-demand guide (EF-A)

Status: on-demand guide at a demonstrated gap; creates no authority, gate, or UI responsibility node. It is loaded only when a task actually touches interactive UI or an accessibility claim, and it does not make every task run an accessibility checklist. Framework or component examples are not observations.

## Use

Use when a change touches interactive behavior, focus, semantics or announcements, or when an accessibility claim is being made or verified. The guide supplies **observable invariants and how to observe them**; it does not certify WCAG compliance, does not add an extra gate, and does not replace the real-browser evidence discipline in `verification-harness-design.md` §Surface driving. The source checklist is a reference, not a conformance list: its contrast/size/numeric values are conditions of a particular standard, and the accepted policy plus the actual user need decides the bar. *(Source: addy `2686b620…`, `references/accessibility-checklist.md`; gate2 EF addendum §A.)*

## Keyboard and focus

- **Focus is visible.** A focused control presents a perceivable indicator; removing focus outlines without a visible replacement fails this invariant.
- **Keyboard operation and order.** Interactive elements are reachable and operable from the keyboard, and the focus order follows the visual/logical order. Native controls make this mostly automatic; custom widgets need their keyboard behavior implemented (for example Enter/Space activation, Escape to close).
- **No keyboard trap.** The user can always leave a component. Inside an open modal, focus may be confined to the dialog's scope; that is not a trap because the modal itself provides a close/exit path. The requirement is not "Tab must always escape the modal" — it is "the user can close it and get focus back".
- **Modal focus move and return.** On open, focus moves into the dialog (a sensible first target); on close, focus returns to a sensible trigger or the previously focused element. The observable invariant is the before/after focus state, not that a particular library call was made.
- **`tabindex` is `0` or `−1` only.** A positive value breaks the natural order and is a maintenance risk; where one appears it needs an explicit justification, not a blanket FAIL for the whole widget. A `div`/`span` given `role="button"` (or another role) is legitimate when it carries a complete accessible name, state, and keyboard behavior — do not reject it by tag suffix alone. *(Source: `skills/frontend-ui-engineering/SKILL.md` L176–232 — its `role="button"` example is a legitimate custom-widget counterexample; `accessibility-checklist.md` §Keyboard Navigation and the `tabindex > 0` anti-pattern.)*
- **Observation.** Drive the real keyboard in a real browser and observe focus visibility, movement, escape and restoration. A framework example — a `<dialog open>` wrapper, a `focus()` call in an effect — does **not** certify trapping or focus restoration; observe the keyboard/browser behavior (and the assistive-technology announcement where that is the claim) under a valid scope. A universal extra accessibility gate is not created. *(Gate2 A1.)*

## Semantics and non-color information

- **Action vs navigation.** Prefer a native `<button>` for an action and a link (`<a href>`) for navigation; a custom role is acceptable when it fully carries the corresponding behavior (name, state, keyboard), and `div`/`span` is not automatically wrong when it does.
- **No color-only signaling.** Information conveyed by color (state, error, required, a link among text) needs a second, perceivable channel such as text, an icon or a shape; labels and error messages are associated with their field, and the error state is visible by more than color.
- **Numeric/contrast references are conditions, not a certificate.** The source's contrast ratios, target sizes and similar values belong to the specific standard and conditions it cites; the actual accepted accessibility policy and user need decide what applies, and passing an automated audit is not a compliance claim.

## Live announcements

- **Map the scenario to the region.** Ordinary status updates and urgent alerts differ by real urgency; not every error is assertive, and not every dynamic DOM change deserves a new live region. Duplicate or excessively frequent interruptions are their own defect; a focus change is a separate observation from an announcement.
- **Discoverability and content change matter.** For an announcement to be meaningful, the region is reachable and its content actually changes under the scenario; the region's role/attribute values (`polite`, `assertive`, `status`, `alert`) are examples.
- **Presence does not prove an announcement.** A `role`/`aria-live` attribute in the markup does not prove that assistive technology announced the change; where the claim requires it, observe the real browser/reader behavior. The source SDK/runtime is not verified here, so no uniform frame-agnostic guarantee is imported; expanding to a real component needs the real browser/reader check. *(Gate2 A3.)*

## Observation and locating

- Locate the user-recognizable object by its accessible role/name/text first. A missing role does not prove the whole UI is inaccessible — non-interactive, native and virtualized content differ — and a successful query does not prove screen-reader, focus or operation correctness.
- Test ids and data attributes are legitimate at stable boundaries; they are not automatically worse than a role selector.
- Prefer a real browser with real keyboard input (and the relevant assistive tool when the claim is about announcements) under the task's authorization; a component's API surface or a source example is never itself the observation.

## Limits

- Not a WCAG certification, not a universal gate, and not a per-task checklist run: the guide is loaded on demand, and the bar comes from the accepted policy and the actual user need.
- The source's contrast/size/numeric values, framework examples and SDK/runtime statements are conditions and examples, not library rules; no uniform assistive-technology guarantee is imported.
- The guide creates no UI responsibility node and no new actor; it adds observations to existing B/D/E/F work, and real certification or standards compliance needs the actual standard plus real-browser/reader observation.
- These observations do not replace the general evidence rules (`guide-test-evidence-quality.md`) or the real-surface discipline (`verification-harness-design.md`); a local logic or fixture test remains valid for the claim it covers and does not certify the real experience.

## Source anchors

| Source | Retained contribution |
| --- | --- |
| addy `2686b620fc1fed2e8f60c704839c766b8594c6b6`, `references/accessibility-checklist.md` | The keyboard/focus, semantics/non-color, live-region and `tabindex > 0` items, used as observable invariants and scenarios; its numeric standards and checklist conformance framing are conditions, not imported rules. *(Gate2 A1–A3.)* |
| addy `2686b620…`, `skills/frontend-ui-engineering/SKILL.md` L176–232 | The keyboard/ARIA/focus-management examples, including a legitimate `role="button"` custom widget; the examples are not treated as proof that trapping or focus restoration works. *(Gate2 A1/A2.)* |
| cursor `ecc249f1…`, `cursor-team-kit/skills/control-ui/SKILL.md` | Real browser/keyboard observation with stable markers and fresh captures; referenced for the observation method (`verification-harness-design.md` §Surface driving), not restated here. *(Gate2 F6/A.)* |

Authored additions: the observable-invariant framing, the modal-trap clarification, the `tabindex 0/−1` rule with the custom-widget counterexample, the no-color-only and announcement observations, the framework-example boundary, and the on-demand/no-gate boundaries.
