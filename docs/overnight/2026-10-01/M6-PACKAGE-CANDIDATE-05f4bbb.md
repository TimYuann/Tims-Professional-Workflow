# M6 package export candidate · 05f4bbb (PW-01 revision)

**State:** fixed package export candidate after the PW-01 closure. M6 remains **unaccepted** pending Oracle push/readback and the second Pro slot. This record supersedes `M6-PACKAGE-CANDIDATE-d672914.md` as the current candidate; the d672914/f11de8b records and their evidence remain valid for their own objects.

## Fixed package identity

- Source commit: `05f4bbb9a490f055855bdd0cde859c4c09421342`
- Repository root tree at the source commit: `4b7f99f5ecabde30dd550dbfb226fbe7a8b638e8`
- `professional-workflow/` package subtree at the source commit: `11e6e3772b6bc0e17259c932b0c0dcabb030a133`
- Export root: `professional-workflow/`
- Deterministic archive command: `git archive --format=tar 05f4bbb9a490f055855bdd0cde859c4c09421342 professional-workflow`
- Git archive SHA-256: `5d551aca0e9dfef47f7886799b9975cadd55c1c16698158efafe8088eacd996d`
- Core revision since `d672914`/subtree `9e4fa14`: exactly two files, +6 appended lines — `git diff --stat d672914 05f4bbb -- professional-workflow` shows only `professional-workflow/README.md` (+4, non-normative optional pointer) and `professional-workflow/authority/README.md` (+2, A7/A8 side note). The frozen Backbone bytes are unchanged (`ce82a70016a4a3fc234ea287f39aac8d79a260ddf13747c4fb705bda580453ba`).
- Backbone source commit/tree: `a77c3974128cee6059b1662579e3803fc1bdfcb9` / `0a84b498a60630e66bf305359fb7e1253a03f6af`

## Core 19-file manifest

The manifest covers the 19 committed package files and does not self-hash:

```text
ff458157fd1457508fdff77dbe170b2d657336c24ae11e99d762af9d63514371  professional-workflow/README.md
01fe9a811a465786ffec8bfd931a5140663bf9f86e85fdd87e4ace9f7d351d12  professional-workflow/authority/README.md
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

## Optional/outside artifacts (not part of the core package)

None of these is loaded by the package; together they are the PW-01 adoption layer and the Pro-1 process records. Digests at commit `05f4bbb`:

```text
5d6bfde397dc21414d8accec3cf39e0d89a0b1a9c50406ce2278c73ff673d7a8  adoption-examples/ucbip.md
06b0d832ffef78c0b69e8e1f43748f7031eda21ffa4234663f1037a47cec27ed  docs/overnight/2026-10-01/PW-01-DISPATCH.md
afc63730d8f886230dc4e6b43056a2425b1536d2e6a4632d4081437ad005712f  docs/overnight/2026-10-01/PRO-AUDIT-1-DISPOSITION.md
c1683b131d2f03dcb96c639a10353b827eeeaaff37fae76d2507ad9846387cc9  docs/overnight/2026-10-01/PW-01-UCBIP-READBACK.md
9a6e873f1e0c909926e5905d468079714c1f5099ea94b265461abf4483f49585  docs/overnight/2026-10-01/PW-01-MAPPING-REVIEW.md
9b498d367d0585d3b220a548e366ad7ba00424c09760ae98f1fb15e1bbd8af4c  docs/overnight/2026-10-01/ORACLE-ACCEPTANCE.md
ad1044467cc04b9de3c310281f950653eb518291514b18c366b592639eaea742  docs/overnight/2026-10-01/PRO-AUDIT-ALLOWANCE.md
a7c2c923475b0c59c1da82cb5adb7fa442a22e8540ecad2c4b2397fca57baac4  docs/overnight/2026-10-01/PRO-AUDIT-1-RESPONSE.txt
533be09b6c26179857bec5979b2d951dba05091eea13ef150d645c383f397296  docs/overnight/2026-10-01/PRO-AUDIT-1-RESPONSE.json
```

Two self-describing records are added after this fixed object (`M6-PACKAGE-CANDIDATE-05f4bbb.md` and `PW-01-CLOSURE-REPORT.md`, plus the STATUS refresh): tip-only process documents, not referenced by the package or the manifest above.

## In-package reference and inherited evidence

- The only in-package reference to the optional note is the appended pointer in `professional-workflow/README.md`; no core file body depends on `adoption-examples/`. The independent check re-observed this and the documented assembly order (`PW-01-MAPPING-REVIEW.md`, check 3).
- No method, Profile, Charter-template, fixture, or Backbone byte changed. Local code F PASS and the old M6 cold-start/rollback evidence stay bound to their own objects; the core change is pointer/status text only, so no rerun was required and only the affected claim (assembly/no-dependency) was re-observed.
- M3 bounded acceptance and M5 local-adoption acceptance remain exactly as `ORACLE-ACCEPTANCE.md` records; this revision triggers no new semantic invalidation.

## Scope limits

- M6 remains unaccepted. This revision waits for Oracle push/readback and the second Pro slot.
- No application/runtime/deployment/recovery claim; the optional note is non-binding, preparation-only, and was not reviewed by a downstream UCBIP owner.
- No `main`, tag, merge, force-push, release, archive, or UCBIP change occurred; UCBIP HEAD stayed `7fc94e4a483cf6b1d8add214d7dbe9a1d42b7f76` with only its two pre-existing untracked HTML exports.

## Manifest correction (appended 2026-10-01; the original sentences above are preserved unchanged)

The "In-package reference and inherited evidence" sentence "No method, Profile, Charter-template, fixture, or Backbone byte changed" is narrowed here: the M3 fixture README `docs/overnight/2026-10-01/fixtures/m3-snapshot/README.md` did receive the §B case-2 adoption append (+4 lines), so its bytes changed. The fixture's contract, code and tests were **not** changed. The core 19-file manifest above and the archive digest are unaffected, since the fixture README is outside `professional-workflow/`.
