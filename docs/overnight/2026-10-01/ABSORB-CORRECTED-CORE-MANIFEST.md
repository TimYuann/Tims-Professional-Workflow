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
