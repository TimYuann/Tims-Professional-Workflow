# Corrected core candidate · manifest and identity

**State:** night-branch candidate only. It is **not** the accepted core and must not be FF-promoted to local `main` before the directed Pro recheck closes. Accepted core identity stays `91875114e51855517f92ef099cbdf60c34e68243`.

## Fixed object

- Candidate commit: `eb7930b42524096a7a286186ba4561df7b95a24e`
- Repository root tree: `cc16a7110f1c93976887daec6f5d0a328bac1126`
- Package subtree: `69226762d65a7ded108977df7e816fe7894e795e` (21 files)
- Deterministic archive: `git archive --format=tar eb7930b42524096a7a286186ba4561df7b95a24e professional-workflow` SHA-256 `6fa0738773c38c30007da418c070698963b5ea205202b0ecd0553b866f902d57`
- Backbone export bytes unchanged: `ce82a70016a4a3fc234ea287f39aac8d79a260ddf13747c4fb705bda580453ba`.

## File manifest (21 files)

```text
b146920ebcf03e1a14b5fc401c4ffba28a2475386e6b6244e73f80affc6f9a27  professional-workflow/README.md
01fe9a811a465786ffec8bfd931a5140663bf9f86e85fdd87e4ace9f7d351d12  professional-workflow/authority/README.md
ce82a70016a4a3fc234ea287f39aac8d79a260ddf13747c4fb705bda580453ba  professional-workflow/authority/RESPONSIBILITY-BACKBONE.md
3fe252aad220e77be434c2d3ee0390da79d998b6c35807c5a763a250a552fda9  professional-workflow/charters/README.md
b159bf96323a9b89a286a5d80fdd703a1375da02467a60645e989b4903336627  professional-workflow/charters/examples/implementation-cross-module.md
038e6a31d699fad0d607cc23aebd02c8f0d6947051863beed98c3901653d3cc1  professional-workflow/charters/examples/implementation-local-fix.md
62050af72fdf53784d757026eb2569bf989ef770b8b95c692584e49245feba5f  professional-workflow/charters/examples/technical-planning-cross-module.md
f03cc007ff6e3c9b7a62f7fbe23953dce9ce0cc080f12fd3326d5084075a0cdb  professional-workflow/charters/template.md
ccc0f141864419eeaf4671d09c6adc61bbdc64bc1d747acd1d9e4b1ef1390a8b  professional-workflow/methods/README.md
0531835f77a8c176df4f173cee64ceee89a21e412ee471a7cc1b0b82f4110c99  professional-workflow/methods/behavior-claim-evaluation.md
f9d9c040a94381886fd6f01dc651d25740997cdfe6ab4436498fcf570fcb68c6  professional-workflow/methods/cross-module-design.md
5ad055b39a7af01ded16399e10a63fab31b452a30e51522e9b502ff23c059208  professional-workflow/methods/guide-mock-adapter-choice.md
7c10676614e717715cddba33b6c3f5abb4d5e62d45f911653712dab4ae16d04d  professional-workflow/methods/guide-redacted-evidence.md
41ddaf9ca133dd25da1c5e71c20fc4263b51a571bc1bf99bea86843c8d0e434b  professional-workflow/methods/local-defect-feedback-loop.md
5fa0e3153a43529470aea48a37e9cb7f98872ef5d89d47f18f90bd3fa55c7d7a  professional-workflow/profiles/README.md
d8b75a5734c015f70d4c3f1479e094be11b92f2ee20d193dc22726fd599377fa  professional-workflow/profiles/behavior-domain.md
8a2f42c874ca08c94b06e20131623178f5a45bc6b7d419a3a8fb7ce1651be399  professional-workflow/profiles/driver.md
d72b3a5097f142f5ea397ab423b146a3b853913c5c1de096d93b95133199f900  professional-workflow/profiles/evidence-evaluation.md
c96162668a1b80096c872a79321e07111a7eecc346f037f7060834f272b0aa5f  professional-workflow/profiles/implementation.md
0f3206ae22fa478c40402d60e17d197f8909184fe6a29b6c89ec4c6fa059ddc8  professional-workflow/profiles/intent-voice.md
d53da06edc99af3bcfc93c744af5f2cc8d512430d318a8b13b1b7f42652d74aa  professional-workflow/profiles/technical-planning.md
```

## Diff vs the accepted core (`91875114`)

- Modified: `README.md`, `charters/README.md`, `methods/README.md`, `methods/behavior-claim-evaluation.md`, `methods/cross-module-design.md`, `methods/local-defect-feedback-loop.md`, `profiles/README.md`.
- Added: `methods/guide-mock-adapter-choice.md`, `methods/guide-redacted-evidence.md`.
- Not changed: `authority/*` (Backbone bytes frozen), all Profiles except their README pointer, Charter template/examples.
- Content of the changes: the three methods gain the method-review-supported insertions at their demonstrated gaps (evidence-safety/custody pointer; mock/adapter coverage boundary; replace-don't-layer narrow condition already present and preserved); `methods/README.md` gains the on-demand guide table and a current-state/scope statement (three methods, four retired names not revived, no equivalence); entry READMEs gain current-state pointers; the optional UCBIP example gains repository-qualified paths. No new Role, gate, validator, composer or authority.

## Use bounds / residuals

- The candidate awaits the directed independent recheck; until then it must not be treated as accepted and must not be promoted to local `main`.
- The two guides are integrated as on-demand support; they mandate no loading, no test framework and no action permission. Runtime enforcement (redaction actually executed, adapter contract observation actually run) remains UNVERIFIED; the synthetic demos in `ABSORB-KNOWLEDGE-DEMO-OBSERVATIONS.md` show the examples are usable, not that a host enforces them.
- The B/A source work keeps its provisional status (175 comparison opinions, 8 pending, not-assessed faces, 39 adopt candidates without the §5 full read); this candidate does not change that.
- Historical Backbone, retired upstream schema/history and the stored DSH prompt/feedback remain untouched.

## Rev.2 · wording/navigation clarifications (commit `bc1c3fccd3703ca3095875160dcfa8b0a1bfc8aa`)

- New core subtree: `85d305b222ca76ffd7d939ab3320c626222d8a95` (21 files; same path set).
- New archive: `git archive --format=tar bc1c3fccd3703ca3095875160dcfa8b0a1bfc8aa professional-workflow` = `0ae1e17b1eb2a2fa33df861ae2635514722de25237da4ccb5e2007809066e9cb`.
- Changed files vs `eb7930b`: `professional-workflow/README.md` `ee5a284328b80d19a6450415c3604f2405324d2535448638a8b97ea148eca3bc`, `methods/README.md` `2fe8d51db93b73bccdd013867c8e83c518fdf62fec7b94dfe30ad695baf9acb0`, `profiles/README.md` `e2a37dbaecd3747300c6ad652403e3ceec1b2708395ac36498ff897797e4244c`, `methods/guide-redacted-evidence.md` `8961cf6fa57ac03f9b7b6b7f661cb7b44f31b679ac1d7e87fff3b2076dbd2fb4`; the other 17 files are unchanged.
- Content: method's non-blocking suggestions only — “Historical M5 candidate” column label, explicit navigation to this manifest and the integrated method review, a repo-qualified `ORACLE-ACCEPTANCE.md` path, and the Wrong-persistence example bounded to the un-authorized default route with the Rule 4 exception named. No semantic or authority change.
- Archive pairing clarification (independent check): tar digests are commit-specific even for identical trees — `eb7930b`→`6fa07387…`, `20640db`→`055005fa2bffc709b992617f54e8b08fe1045d3f506db59f96b2793144d90fee`, `bc1c3fc`→`0ae1e17b…`. The original pairing above pins the archive to `eb7930b` and remains correct.
- Independent observations at the reviewed object (`20640db`): `ABSORB-CANDIDATE-VERIFY.md` (9/10 mechanical checks PASS plus a cold-read evaluation PASS with one PARTIAL branch) and `ABSORB-INTEGRATED-CORE-METHOD-REVIEW.md` (method PASS, no must-fix); the reader answer itself is local at `.worktrees/verification/absorb-reader/ANSWER.md`, not committed. Method's delta confirmation for Rev.2 is appended to its review report.
- The candidate remains night-only: no FF to local `main`, no `main` push, no acceptance implied.

## Rev.3 · removed batch-specific audit context from the general guide (commit `dca01b4f717aa300d818c6bbe143d6331f1252c6`)

- Pure explanatory cleanup per Owner direction before the directed Pro recheck: `methods/guide-redacted-evidence.md` no longer carries the batch/offline demo parenthetical in Rule 4 or the batch-mode sentence in the Example Raw branch. The general conditions are unchanged (existing valid authorization, restricted location, custody/cleanup, minimal signal, no self-expansion, no need to re-ask when authorized).
- The synthetic/offline observation scope remains in `ABSORB-KNOWLEDGE-DEMO-OBSERVATIONS.md` and the correction brief, not in the general product guide.
- New core subtree: `6536343eadad72c46cb9e1f4f43f8a6dcb8b1331`; archive: `git archive --format=tar dca01b4f717aa300d818c6bbe143d6331f1252c6 professional-workflow` = `0e658c35f8110121d889ee5ab852a7140efe54c87d73d65f36e278d75c170e8f`. Changed file: `methods/guide-redacted-evidence.md` `7a6875c1994cf08ab008aef20839266b854b552b85e018fc85443645ffb5804f`; the other 20 files are unchanged (diff shows exactly those two removals).
- No demo rerun, no full method re-review and no amend of earlier identities; method's PASS and IM-1 delta remain bound to their own objects, and this removal changes no source, rule or authority.

## Rev.4 · Rule 2 collection wording (commit `08d990727deaea13e220e8764f9a3ecf7a8bd4cb`)

- Rule 2 no longer reads as a ban on new collection: inside the task's valid authorization the guide allows collecting new observations or reusing existing records, keeps only minimal signal-bearing evidence, redacts before show/record/share/store, and leaves raw artifacts to Rule 4. No new permission is granted, unpermitted capture is not authorized, and no per-step re-asking is required.
- The default example marks reuse as one common case and states that fresh observations are collected inside the same authorization with the same discipline; the source note records Matt retained plus an authored collect-or-reuse adaptation.
- New core subtree: `baf2991e004912b14048098d42ad024fc441324e`; archive: `git archive --format=tar 08d990727deaea13e220e8764f9a3ecf7a8bd4cb professional-workflow` = `e9b1c92181c436e314e45aa2fb88b86ca5eefac29e0591b0dc75225f1b311e40`. Changed files vs `dca01b4`: `methods/guide-redacted-evidence.md` `9d2e43a10d7a83e4e8fe69942399dc376f40e2159bc98c7c448a0c517dab0b0c`, `methods/local-defect-feedback-loop.md` `cc8f3911125c8ec8c7b87625590dbb3ffbbd29da4c10b06e785ed1cbaa0d6348`; the other 19 files are unchanged.
- Method's targeted Rule 2 confirmation is appended to `ABSORB-INTEGRATED-CORE-METHOD-REVIEW.md`; no full review was reopened.

## Rev.5 · audit disposition (commit `31929b34f4eada9e7a3653b1804f409785d9b7c7`)

- **MF-1 closed by deletion:** both Charter examples keep the M4 historical source and now point current bytes to `methods/README.md` §Status and source trace plus the night manifest; no current digest is copied in two places; a real task rebinds the current fixed object.
- **NB-1:** the six Profiles and `profiles/README.md` now point method bodies/selection to `methods/README.md` (mental-model prose unchanged). **NB-2:** the package entry compresses M1–M5 into historical source pointers plus the current candidate/manifest status (no five-layer decode). **NB-3:** `docs/WORKFLOW-INTENT.md` §10 carries the registry-retired historical marker; Backbone bytes untouched.
- Audit identity corrected by its author (`tpw-audit-overprocess`, native session `01a0f831-733d-7230-9b84-5a0d4d84ecc0`); conclusion unchanged.
- New core subtree: `e5e5338ed8abc717bdda48e0f4ae751dea30dbb1`; archive: `git archive --format=tar 31929b34f4eada9e7a3653b1804f409785d9b7c7 professional-workflow` = `a45e8cba3be1f3f23de144dddbaccd87a356854017a5837f970e8018362d469f`.
- Verification chain after this revision: the independent check runs a short references/state verification plus the full package manifest at the final pin; method gives the substantive semantic-diff view (these are metadata/entry changes; the claim-determined verification principle and the Rule 3 invoked-paths fix remain as previously confirmed).
- The candidate stays night-only until the directed Pro recheck closes; no `main` FF or push.

## Rev.6 · final 21-file digest table (core subtree `e5e5338ed8abc717bdda48e0f4ae751dea30dbb1`, `31929b3` core-change commit)

```text
0d80d3c2b0d3a73a686f56df465cb64249f527562edea9b30f735fa19a5022ce  professional-workflow/README.md
01fe9a811a465786ffec8bfd931a5140663bf9f86e85fdd87e4ace9f7d351d12  professional-workflow/authority/README.md
ce82a70016a4a3fc234ea287f39aac8d79a260ddf13747c4fb705bda580453ba  professional-workflow/authority/RESPONSIBILITY-BACKBONE.md
3fe252aad220e77be434c2d3ee0390da79d998b6c35807c5a763a250a552fda9  professional-workflow/charters/README.md
b159bf96323a9b89a286a5d80fdd703a1375da02467a60645e989b4903336627  professional-workflow/charters/examples/implementation-cross-module.md
b0dff7041e7edb970d384231df5582665a8ce7765dd2833fd8ff9ff14de6d927  professional-workflow/charters/examples/implementation-local-fix.md
8d1168ae783e5b23c9f21419ac218ac0a193d078c98cc3e856893c9e44306f9c  professional-workflow/charters/examples/technical-planning-cross-module.md
f03cc007ff6e3c9b7a62f7fbe23953dce9ce0cc080f12fd3326d5084075a0cdb  professional-workflow/charters/template.md
2fe8d51db93b73bccdd013867c8e83c518fdf62fec7b94dfe30ad695baf9acb0  professional-workflow/methods/README.md
25086584eb4acd9ef7d1521153f3c3c9b164f253223b1ee027fbd2276375181e  professional-workflow/methods/behavior-claim-evaluation.md
f9d9c040a94381886fd6f01dc651d25740997cdfe6ab4436498fcf570fcb68c6  professional-workflow/methods/cross-module-design.md
3e047e1f5ef50cce907364ed7159d21b622a2ec9f48b71c6b60db3d0c397bdac  professional-workflow/methods/guide-mock-adapter-choice.md
9d2e43a10d7a83e4e8fe69942399dc376f40e2159bc98c7c448a0c517dab0b0c  professional-workflow/methods/guide-redacted-evidence.md
cc8f3911125c8ec8c7b87625590dbb3ffbbd29da4c10b06e785ed1cbaa0d6348  professional-workflow/methods/local-defect-feedback-loop.md
047a76dc62457f7b566ae98ed656f26cd32cfab86b63ad367bb2b7441df50187  professional-workflow/profiles/README.md
43b02f332286194f562fb2e4cf5eda1c3cbf25fed743be733338709bd83d2dc0  professional-workflow/profiles/behavior-domain.md
0703cf617940f70d532771c52629ef33ee30ae25b40aa5b358d7b5c526d775ea  professional-workflow/profiles/driver.md
76cd77f888bba175c7644fdca1ef6ff7715b5685a00561d6cefdbbc0c7bd87d4  professional-workflow/profiles/evidence-evaluation.md
5c4186d4efa86202a2d0f897c9f54c1e543be98378802ebc8212ae1aa6f7e564  professional-workflow/profiles/implementation.md
f54e283e8a83fe6b57540db3b3d50299bf544f4c28f5fffa20275a8c67927170  professional-workflow/profiles/intent-voice.md
15c751670b24434f6d9ec2ed9f3c1e164400bb844e1f88ce0b1d52424cf2b08f  professional-workflow/profiles/technical-planning.md
```

- The earlier table and Rev.2–5 deltas describe their own objects; this table is the final candidate state. Docs-only commits after `31929b3` do not change `professional-workflow` bytes. Archive digests are commit-specific tar metadata: `31929b3` → `a45e8cba3be1f3f23de144dddbaccd87a356854017a5837f970e8018362d469f`; the final pin archive is computed in the handoff message.
- Independent check (`ABSORB-FINAL-VERIFY.md`): references/state 6/6 PASS; 21-path set, core subtree and unchanged Backbone confirmed; the digest-table LIMIT is closed by this table. Method's final entry delta: PASS (metadata/entry only, no method/authority/gate change).

## Rev.7 · final integrated identity after acceptance status sync (`9085d758848de8836a3e6e6083962480b1af42ca`)

The directed Pro recheck passed at reviewed identity `16c554de8abfe16547837cbfb19d9b7707a4d4dd` / core `e5e5338ed8abc717bdda48e0f4ae751dea30dbb1` / archive `ea10803f0c29c8f147caf75652f55b2abef9f27ebecb0b1458448ccd453d34b7` (`ABSORB-PRO-RECHECK-*`, `ABSORB-FINAL-ACCEPTANCE.md`). The acceptance authorizes factual status synchronization; that changes four package files, so the final integrated object carries a new identity as the acceptance record requires.

- Final integrated root tree: `27bbdfb85299d751fe0bc48e09c1dc8b545f5dcf`; core subtree: `7c814e54c5e775045bc1c5155e3c181ceb1345fb`.
- Product-bytes commit: `9085d758848de8836a3e6e6083962480b1af42ca`; archive at that commit: `git archive --format=tar 9085d758848de8836a3e6e6083962480b1af42ca professional-workflow` = `63ac073fcdb976cb5a11bc2556036a914e82b62a7e8447e467ff8d18491d260e`.
- Changed vs the reviewed identity: `README.md` (package status), `methods/README.md`, `methods/guide-mock-adapter-choice.md`, `methods/guide-redacted-evidence.md` — status labels/pointers only, no method meaning change; the other 17 files unchanged. Retired-name, authority and residual statements retain their accepted wording.

```text
ad1b569c62c070d989b226cfe20a8f2c61c4876c817a4e373c7bb061f908c277  professional-workflow/README.md
01fe9a811a465786ffec8bfd931a5140663bf9f86e85fdd87e4ace9f7d351d12  professional-workflow/authority/README.md
ce82a70016a4a3fc234ea287f39aac8d79a260ddf13747c4fb705bda580453ba  professional-workflow/authority/RESPONSIBILITY-BACKBONE.md
3fe252aad220e77be434c2d3ee0390da79d998b6c35807c5a763a250a552fda9  professional-workflow/charters/README.md
b159bf96323a9b89a286a5d80fdd703a1375da02467a60645e989b4903336627  professional-workflow/charters/examples/implementation-cross-module.md
b0dff7041e7edb970d384231df5582665a8ce7765dd2833fd8ff9ff14de6d927  professional-workflow/charters/examples/implementation-local-fix.md
8d1168ae783e5b23c9f21419ac218ac0a193d078c98cc3e856893c9e44306f9c  professional-workflow/charters/examples/technical-planning-cross-module.md
f03cc007ff6e3c9b7a62f7fbe23953dce9ce0cc080f12fd3326d5084075a0cdb  professional-workflow/charters/template.md
fddb1d0278c6561cfd9d70efea6f1db7f8205bbb896af60279eff6239c19d8e7  professional-workflow/methods/README.md
25086584eb4acd9ef7d1521153f3c3c9b164f253223b1ee027fbd2276375181e  professional-workflow/methods/behavior-claim-evaluation.md
f9d9c040a94381886fd6f01dc651d25740997cdfe6ab4436498fcf570fcb68c6  professional-workflow/methods/cross-module-design.md
967f089fa57d7a803b6657836a1ba4610d27c60b0fe9342e96d9a268b0d7414e  professional-workflow/methods/guide-mock-adapter-choice.md
0abd46cec7198ae97671dbc03e428be559cd75927537a9bd06ebd2c63aef5335  professional-workflow/methods/guide-redacted-evidence.md
cc8f3911125c8ec8c7b87625590dbb3ffbbd29da4c10b06e785ed1cbaa0d6348  professional-workflow/methods/local-defect-feedback-loop.md
047a76dc62457f7b566ae98ed656f26cd32cfab86b63ad367bb2b7441df50187  professional-workflow/profiles/README.md
43b02f332286194f562fb2e4cf5eda1c3cbf25fed743be733338709bd83d2dc0  professional-workflow/profiles/behavior-domain.md
0703cf617940f70d532771c52629ef33ee30ae25b40aa5b358d7b5c526d775ea  professional-workflow/profiles/driver.md
76cd77f888bba175c7644fdca1ef6ff7715b5685a00561d6cefdbbc0c7bd87d4  professional-workflow/profiles/evidence-evaluation.md
5c4186d4efa86202a2d0f897c9f54c1e543be98378802ebc8212ae1aa6f7e564  professional-workflow/profiles/implementation.md
f54e283e8a83fe6b57540db3b3d50299bf544f4c28f5fffa20275a8c67927170  professional-workflow/profiles/intent-voice.md
15c751670b24434f6d9ec2ed9f3c1e164400bb844e1f88ce0b1d52424cf2b08f  professional-workflow/profiles/technical-planning.md
```

- Archive digests are commit-specific tar metadata: this pairing belongs to the product-bytes commit above. Later docs-only commits (this Rev.7 and `ABSORB-FINAL-INTEGRATION.md`) do not change `professional-workflow` bytes; the independent check verifies at the final tip: path set, per-file hashes, core subtree `7c814e54…`, this archive pairing, and unchanged Backbone `ce82a700…`.
