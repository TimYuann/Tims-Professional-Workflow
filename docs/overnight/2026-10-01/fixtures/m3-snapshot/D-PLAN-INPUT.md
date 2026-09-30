# M3 case 2 · task input for D

Produce the technical Plan required by `D-CHARTER.md` for the accepted B/C behavior contract and domain semantics. The fixture's current structure is evidence of the system, not a prescribed responsibility map:

- `src/state_store.py` holds a current view and can advance its revision after a case update.
- `src/page_summary.py` reads an overview from a current view.
- `src/turn.py` creates a turn carrying the overview.
- `src/case_reader.py` reads the current cases.
- `src/service.py` composes the current entry points.

Read the actual files. Identify the technical facts and dependencies that matter to the accepted B/C inputs, then write the smallest Plan that lets an E instance start without guessing shared commitments. Do not implement or change B/C meanings. Do not copy a solution route from this task input; it intentionally does not prescribe module ownership, a token/argument shape, or a recall answer.
