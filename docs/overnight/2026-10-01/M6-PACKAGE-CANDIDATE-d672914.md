# M6 package export candidate · d672914

**State:** fixed package export candidate; M6 qualification is incomplete. The prior f11de8b export record is preserved in `M6-PACKAGE-CANDIDATE-f11de8b.md` and is superseded as the current package candidate.

## Fixed package identity

- Source commit: `d672914ac80eeed0aa5f04a0c80f448acc9de6f3`
- Repository root tree at the source commit: `c88b662421bc44270fdf38bf43267010fe0a1d38`
- `professional-workflow/` package subtree at the source commit: `9e4fa14a427f42dc2fc6304a08fa76fd7596313e`
- Export root: `professional-workflow/`
- Deterministic archive command: `git archive --format=tar d672914ac80eeed0aa5f04a0c80f448acc9de6f3 professional-workflow`
- Git archive SHA-256: `e2571ca9cca6148378d1b6ec1a580c0432252727e135fa0bb29f59ec23c5a39d`
- External 19-file manifest SHA-256: `c40b31e87bdad8374af0bf7b393bec5583dd45deee38601e4fed324c669f1ad0`
- Local extraction: `/private/tmp/tpw-m6-export-d672914/`
- Backbone source commit/tree: `a77c3974128cee6059b1662579e3803fc1bdfcb9` / `0a84b498a60630e66bf305359fb7e1253a03f6af`
- Backbone source/export SHA-256: `ce82a70016a4a3fc234ea287f39aac8d79a260ddf13747c4fb705bda580453ba`

The manifest is stored outside the package at `/private/tmp/tpw-m6-export-d672914/SHA256SUMS`; it covers the 19 committed package files and does not self-hash.

## File manifest

```text
2aad8921a4feb679995c85e3ef9ffe23d10ef02e022e716e407a2ba70349cef4  professional-workflow/README.md
e509641d31aa52f20970564371d614c947c5bd3ff4c11dcd55696c772a4389b7  professional-workflow/authority/README.md
ce82a70016a4a3fc234ea287f39aac8d79a260ddf13747c4fb705bda580453ba  professional-workflow/authority/RESPONSIBILITY-BACKBONE.md
035f2a1f58cc28373a5f90b6478061bcad51d02b0cc341b7fd2d0ffb49306439  professional-workflow/charters/README.md
b159bf96323a9b89a286a5d80fdd703a1375da02467a60645e989b4903336627  professional-workflow/charters/examples/implementation-cross-module.md
038e6a31d699fad0d607cc23aebd02c8f0d6947051863beed98c3901653d3cc1  professional-workflow/charters/examples/implementation-local-fix.md
62050af72fdf53784d757026eb2569bf989ef770b8b95c692584e49245feba5f  professional-workflow/charters/examples/technical-planning-cross-module.md
f03cc007ff6e3c9b7a62f7fbe23953dce9ce0cc080f12fd3326d5084075a0cdb  professional-workflow/charters/template.md
24de9ce294c682afd7c9930a1000b2c5b37fb5a518edb34e3544b21ba6c87538  professional-workflow/methods/README.md
cfacc0f57cedadc6360ad0338645e43740dad4b1e15cc6876088eb89b4034f02  professional-workflow/methods/behavior-claim-evaluation.md
ab0a0bc03448407479fe82b92b2355384e7f2acf49c2ff3026882670f955a0a5  professional-workflow/methods/cross-module-design.md
1ba8f8f2fb46a0094c22e7ac946e27f30a27b1ce25e201fd5ede819ddc2e4215  professional-workflow/methods/local-defect-feedback-loop.md
2e103f2f05c038e4d6064cf2caf4c5d4cb482a3aba3e8205764db6488db49711  professional-workflow/profiles/README.md
d8b75a5734c015f70d4c3f1479e094be11b92f2ee20d193dc22726fd599377fa  professional-workflow/profiles/behavior-domain.md
8a2f42c874ca08c94b06e20131623178f5a45bc6b7d419a3a8fb7ce1651be399  professional-workflow/profiles/driver.md
d72b3a5097f142f5ea397ab423b146a3b853913c5c1de096d93b95133199f900  professional-workflow/profiles/evidence-evaluation.md
c96162668a1b80096c872a79321e07111a7eecc346f037f7060834f272b0aa5f  professional-workflow/profiles/implementation.md
0f3206ae22fa478c40402d60e17d197f8909184fe6a29b6c89ec4c6fa059ddc8  professional-workflow/profiles/intent-voice.md
d53da06edc99af3bcfc93c744af5f2cc8d512430d318a8b13b1b7f42652d74aa  professional-workflow/profiles/technical-planning.md
```

## Export observations

- `shasum -a 256 -c SHA256SUMS` passed all 19 exported files.
- Synthetic external task input SHA-256 `361530ee8aa421696f1ff376f101f8229b7bfbd035696e2bee7caa1ba12d5565` was used only to exercise assembly syntax; it is not in the package.
- Extracted-package local assembly hash: `713925256a7eb3157697edd60baaf9a3762d16cddf373d0bef8347c0e6f7b181`.
- Extracted-package D/Backbone assembly hash: `e8c2b98d3548651bf81a64cb9a8e34b861396ca542843e691f58c6d3a4407601`.
- These are text-assembly observations only. No fresh session has cold-started from this export, no independent clean-package verifier has completed, and no rollback rehearsal has occurred.
- At this package-source freeze, the targeted M5 F1–F4 recheck had not yet completed. Its later fixed report `M5-PACKAGE-REPAIR-RECHECK.md` records PASS; M5 remains unaccepted pending full-object review.
- At this package-source freeze, case 2 was blocked at PC-1. B/C v2 and the D Plan later resolved that dependency with bounded PASS reviews; Oracle accepted the two fixed case execution results and the stated Turn presented-view scope. Overall M3 remains open; see `ORACLE-ACCEPTANCE.md`, `M3-REPORT.md`, and `M3-AUTHORITY-BOUNDARY-OBSERVATION.md`.
- UCBIP remains untouched. Pro audit count is still 0/2. Oracle pushed prior night-branch checkpoint `96114e1a97227e7d1541965c89bb91deb860866b` with matching remote readback; this checkpoint awaits Owner/Oracle push. No tag, merge, or release action occurred.

Use this candidate only for further qualification against exact commit/tree above. If M5 review changes the package, export and manifest a new fixed object.
