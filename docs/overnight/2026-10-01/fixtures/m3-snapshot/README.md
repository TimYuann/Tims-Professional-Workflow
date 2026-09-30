# M3 case 2 · offline snapshot fixture seed

This seed is an intentionally small, dependency-free Python system for a later exercise. It contains a page summary, a turn wrapper and a case reader. The seed predates the cross-read snapshot contract; the accepted exercise B/C objects are now `BEHAVIOR-CONTRACT.md` v1 and `DOMAIN-SEMANTICS.md` v1.

Run the existing smoke tests from this directory with:

```sh
python3 -m unittest discover -s tests -v
```

The B/C authoring input is `CASE-INPUT.md`; it states the goal without selecting a module, interface or implementation. B/C outputs are now fixed. D may prepare a Plan; E implementation begins only after an independent challenge and acceptance of that Plan.
