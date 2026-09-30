# M3 case 1 · pre-implementation observation

Fixture: offline `normalize_label` exercise. This documents the source state before any implementation session; it is not product or UCBIP evidence.

- Runtime: Python 3.14.4.
- Command, run from this fixture directory: `python3 -m unittest discover -s tests -v`.
- Exit: `1`.
- Result: 4 tests ran; 3 passed; `test_collapses_internal_whitespace` failed.
- Failure: input `" \tNorthern   Star\n"` returned `"NORTHERN   STAR"`; exercise contract expects `"NORTHERN STAR"`.
- Reproduction is deterministic and local. The other checks (punctuation preservation, empty input, and `TypeError` for non-string input) passed.

The fixed input contract is `CONTRACT.md` (SHA-256 `ecfc6195726fe62321208ad766fcbe7005c784c6d2aece7f9b2a2eca4ef293bb`). At this observation no implementation candidate has been written.
