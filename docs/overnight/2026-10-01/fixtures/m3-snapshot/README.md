# M3 case 2 · offline snapshot fixture seed

This seed is an intentionally small, dependency-free Python system for a later exercise. It contains a page summary, a turn wrapper and a case reader. Current module behavior works independently; no cross-read snapshot contract has been accepted in this seed.

Run the existing smoke tests from this directory with:

```sh
python3 -m unittest discover -s tests -v
```

The B/C authoring input is `CASE-INPUT.md`. It states the task goal without selecting a module, interface or implementation. D/E work begins only after the exercise B/C outputs and a challenged D Plan are fixed.
