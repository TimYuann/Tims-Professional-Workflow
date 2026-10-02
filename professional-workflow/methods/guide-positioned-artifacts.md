# Positioned artifacts guide · on-demand support (candidate)

- **Status:** candidate distilled under `ORACLE-REVIEW-A4-THIRD-PARTY` (2026-10-02); not yet an accepted reference; creates no authority, trigger, or gate. A fixed-diff review still applies.
- **Use:** on demand when a task changes a document, spreadsheet, or deck through a position- or object-addressed API (the Google Docs/Sheets/Slides connectors are the worked examples). Locate the target through the interface before writing, and carry the API's unit, range, and version premises into the plan. The external-operation sequence in `external-tool-operation.md` still applies for permission, cost, and result interpretation.

## Locate before writing

1. Address content by locating it, not by computing an offset that was valid in an earlier read. A locate call returns fresh ranges for the exact text; locate and edit in back-to-back calls.
2. Docs: ranges are zero-based UTF-16 index ranges within one tab and the end is exclusive — one short misses the last character, one long styles the character after the phrase. Guessed or stale indexes silently hit the wrong paragraphs. Structure-derived ranges come from reading the document elements; raw indexes require read → one edit → pass the latest revision id → re-read before the next positional edit.
3. Anchor duplication: a phrase or anchor that appears more than once must be disambiguated before the edit. Do not stretch one list/range operation across two visually separate lists (it can continue the first list's numbering instead).
4. Sheets: two coordinate systems on purpose — value tools address a tab title plus A1 cells; structure and format tools address the numeric `sheetId`. Read the spreadsheet metadata first and keep the title↔sheetId mapping; a new tab's id comes from its creation reply.
5. Sheets sequencing: write values, then format, then chart last. A chart depends on the values and their real types; the first range is the domain and later ranges are series on the same tab. Fix a wrong chart in place rather than stacking a second chart over it.
6. Slides: elements are addressed by `objectId` from a layout read; positions are points from the slide's top-left, and the real slide size comes from the tool read, not from an assumed constant. Prefer declarative composition (a layout tree or documented HTML subset) so alignment, overflow, and contrast hold by construction; then read the returned `issues`, then render a thumbnail and look. A lint-clean plan is not visual correctness.
7. Slides repetition: build the first slide fully, then duplicate its object and scope text replacement to that slide's page object ids. A whole-shape text set replaces the entire text (not a range), and moving does not resize — delete and recreate when the size is wrong.

## Writes invalidate reads

8. Any write invalidates subsequent positional reads: re-read after a structural change (insert, delete, merge, sort, style-then-more-edits). Re-reading is a premise, not an optimization.
9. Batch operations can run from the end toward the beginning when intermediate re-reads are too expensive, so earlier ranges stay valid.
10. Sheets structural operations: merges keep only the top-left value (write text after merging); sorts rewrite positions; row/column inserts and deletes are 1-based and deletes are immediate and not undoable through the API; bound a whole-tab read by a cell range and continue from the truncation token.

## Revision and concurrency premises

11. A revision id makes the next write fail instead of corrupting a concurrent edit. Pass the latest revision and still handle a rejection by re-reading and re-deciding, not by retrying blindly.
12. Where the API has no revision guard, read-before-write only reduces the chance of overwriting another writer; it does not guarantee concurrency isolation or a particular last-write-wins outcome. State which premise the run relied on.

## Units, ranges, and observation

13. Units and ranges are interface facts: index units (UTF-16 code units), exclusive versus inclusive ends, points versus pixels, A1 versus sheetId, per-tab versus document-wide scope, and the size the tool reports. Take the actual value from a reading; do not convert by assumption.
14. A formatted-value read does not prove the underlying type — raw and formatted reads serve different claims. A structure read and a visual export likewise prove different claims.
15. A visual claim needs the visual surface: render or export the artifact (thumbnail, PDF) and look at the rendered result. Lint, schema checks, and element reads are not visual evidence.
16. A substitute run (fixture, scratch document, mock connector) can prove position or shape semantics; it does not prove the real provider's API, permissions, or rendering. Real-host claims need the actual authorized host, as in `external-tool-operation.md`.
17. Scope a batch replace to the intended domain (the named tab, or the target slide's object ids); an unscoped replace crosses boundaries.
18. Reuse one theme/palette across pages and derive on-colors from the fill behind the text, so the artifact does not drift page to page; fix a page in place rather than stacking a second element over the bad one.

## Conditions and exceptions

- The source's numeric defaults (a fixed slide size, margins, font sizes, a thumbnail per page, all warnings must be fixed, mandatory title styling, dashboard formatting, `parseInput: true` everywhere) are one team's usage, not universal interface rules. Apply what the actual tool documents and the artifact needs; read the real size and ranges from the tool.
- `parseInput` on untrusted text can execute formulas; decide by the actual trust boundary rather than copying a boolean from an example.
- Template/brand palettes and accessibility standards are inputs from their owner; do not generalize one example's color pairs as a universal palette.
- Creating an empty document or deck is not the same as having written its content; verify the content claim separately.

## Limits

- On-demand support only: no validator, no mandatory styling pass, no fixed layout template, and no required number of thumbnails.
- Numbers, units, and ranges in any source may drift with the API; re-read the tool for the actual premise.
- This guide does not create mutation authorization; delete-and-recreate, batch replace, and export follow the task's existing permissions.
- Later cross-source work may merge this guide with another positioned-artifact source; keep the locate-before-write discipline, the two coordinate systems, the write-invalidates-reads and revision premises, the value→format→chart dependency, and the real-versus-substitute observation boundary.

## Source anchors

| Source | Pin / path | Section |
| --- | --- | --- |
| Cursor plugins | `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`, `third_party/google-docs/skills/google-docs/SKILL.md` | Locate text, never compute indexes (UTF-16, exclusive end, write shifts); raw-index path with revision and back-to-front order; list/anchor disambiguation; create/blank document; styling end-index rule; table fill order and re-read after structural edits; verify structure vs Markdown vs PDF |
| Cursor plugins | same pin, `third_party/google-sheets/skills/google-sheets/SKILL.md` | Two coordinate systems (tab title + A1 vs sheetId) and the metadata mapping; values→format→chart sequencing; chart domain/series and in-place fix; no revision guard and read-before-write; merge/sort/insert/delete structure effects; bounded reads with truncation; formatted vs unformatted verify |
| Cursor plugins | same pin, `third_party/google-slides/skills/google-slides/SKILL.md` | Points from the slide's top-left and the size from `read_slide_layout`; objectId addressing and `requiredRevisionId`; compose→issues→thumbnail look→fix; grid conventions; palette reuse and contrast against the fill behind the text; duplicate-and-scope replace; `set_shape_text` whole-text replacement; pdf export for the visual claim |
| Product core | `methods/external-tool-operation.md` | Permission, cost, capability-class, and real-versus-substitute observation boundary for the surrounding operation |
