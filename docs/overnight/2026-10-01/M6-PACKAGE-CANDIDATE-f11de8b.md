# M6 package export candidate · f11de8b

**State:** fixed package export prepared; M6 qualification is incomplete. This document records an export candidate, not an acceptance or release.

## Fixed package identity

- Source commit: `f11de8b4b35015b14dfc50dd94d19525e424cd07`
- Source tree: `252093659181f0fd73e8ef6f9316e0778f524961`
- Export root: `professional-workflow/`
- Deterministic command: `git archive --format=tar f11de8b4b35015b14dfc50dd94d19525e424cd07 professional-workflow`
- Git archive SHA-256: `817d66602f81ff981e82a963d11b94ee5bb4ebeea24120f4d2d2815d910bc7f4`
- External 19-file manifest SHA-256: `6161f038176ac0d14cd7c2c535ecf794ee6e8dd14a9a15bddbb70a50ee3bf348`
- Backbone source commit/tree: `a77c3974128cee6059b1662579e3803fc1bdfcb9` / `0a84b498a60630e66bf305359fb7e1253a03f6af`
- Backbone source and export SHA-256: `ce82a70016a4a3fc234ea287f39aac8d79a260ddf13747c4fb705bda580453ba`

The local extraction used for these checks is `/private/tmp/tpw-m6-export-f11de8b/`. The manifest is outside the package root, so it does not self-hash or add an unaccepted product file.

## File manifest

```text
ec39ef84b1cb782b5f62fe6454a3f26b837c630c018fe24ea5f8259d420d22c2  professional-workflow/README.md
004164ff7414c7344e105e0883f6d36c871c43644707dcf85977f010e7d3dd37  professional-workflow/authority/README.md
ce82a70016a4a3fc234ea287f39aac8d79a260ddf13747c4fb705bda580453ba  professional-workflow/authority/RESPONSIBILITY-BACKBONE.md
035f2a1f58cc28373a5f90b6478061bcad51d02b0cc341b7fd2d0ffb49306439  professional-workflow/charters/README.md
aa1ae2a99e844767f251d1392be2b98f1d196b5ebb76a8efa8dc5f6120b66f68  professional-workflow/charters/examples/implementation-cross-module.md
230990f3402787a4c837398f0e8da5ae523c0b673a8e493ed3215611494791ed  professional-workflow/charters/examples/implementation-local-fix.md
27ebf506fcc0a3f477ca5f03f6df4b4294a2b9a5de8567aca85f2c3be1d019df  professional-workflow/charters/examples/technical-planning-cross-module.md
f03cc007ff6e3c9b7a62f7fbe23953dce9ce0cc080f12fd3326d5084075a0cdb  professional-workflow/charters/template.md
dc4bb280b36b948d943e645aa13c2729669c15bd8594346f8e04b218a450a197  professional-workflow/methods/README.md
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

## Checks and limits

- `shasum -a 256 -c SHA256SUMS` passed all 19 exported files.
- The package-root illustrative local-fix assembly ran from the extracted package and produced SHA-256 `287340b31f7ad14741bfa6e7ba178a7ed20f58435e302232a39ea1d6d723741b`. Its smoke task input was external caller input; this is text assembly evidence, not a fresh-session cold start.
- A separate D/Backbone composition in the working tree produced SHA-256 `061b0b4d558dd55ce8871972574df4e30a7f1948f7b9dafe22f924eeea3910bf`.
- The repository consistency check passed 7/7 and `compose-role.py --check` passed. The legacy closure checker returned 19 PASS / 2 FAIL: it requires a tag (prohibited) and scans required tool-specific execution records as library content. Neither checker establishes package method effectiveness.
- No independent clean-package verifier, fresh-session cold start, rollback rehearsal, or final M3 acceptance has occurred. UCBIP has not been read or changed. No Pro review has been sent; allowance remains 0/2.

Keep this candidate only as a fixed export input for later independent qualification. Any semantic M5 change requires a new commit, archive digest, and manifest before review.
