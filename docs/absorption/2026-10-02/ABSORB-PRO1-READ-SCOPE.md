# TPW Pro #1 · 实际阅读与身份核对范围

审阅日期：2026-10-03。此文件是本次审阅记录，不是 TPW 产品文件、采用门禁或新的项目台账。

## 固定对象与实际核对

- Repository: `TimYuann/Tims-Professional-Workflow`
- Branch: `night/2026-10-01-workflow`
- GitHub connector 实际返回的 branch tip: `edce02a9d9341376a1197503bb20720e1fee6fa0`
- 产品 commit: `5d7d89d3f8fc295ed7c96e63a2af8952e75398ec`
- GitHub commit 对象返回的 root tree: `344d438813a27300b4c7cec961d580f6a18412f8`
- GitHub root tree 返回的 core subtree: `0e7614cd4eec20b4b43b7b0caba43187d3ec10b4`
- 由附件正文独立计算的 core subtree: `0e7614cd4eec20b4b43b7b0caba43187d3ec10b4` — MATCH
- 独立重算 59 个正文 SHA-256、Git blob SHA-1 与嵌套 tree；59/59 匹配。不是以附件头部的自报 SHA 代替计算，也不是以机械 PASS 代替专业审阅。
- 方法/guide 正文 42 个；其他 core 文件 17 个；均全文阅读。
- GitHub compare 返回：tip 相对产品 pin ahead 4、behind 0，merge-base 为产品 pin；变化仅 LEDGER 与新增机械报告，无产品路径变化。评审仍绑定产品 pin。
- Backbone 本地 SHA-256: `ce82a70016a4a3fc234ea287f39aac8d79a260ddf13747c4fb705bda580453ba`；Git blob `6cb486e5f9897fdff2d3c03f687aac987771f7e1`，与固定源 `a77c3974128cee6059b1662579e3803fc1bdfcb9:docs/RESPONSIBILITY-BACKBONE.md` 的 connector blob 相同。
- 另定向从产品 pin 取回 release-and-recovery L1–45、external-tool-operation L15–45、performance-and-neutrality L90–130，核查本次必须修订项。
- 没有重建 git archive 的 tar，故 archive SHA-256 `2758099eabcaeb8c4c19deab22a4341e48323ea8313ab42f49f2110d439e3395` 仅核到远端报告中的记录，未独立复算 tar。完整 core 的字节身份由上述重建 Git subtree 核回。

## Core 全文阅读清单

阅读来源：上传包中的完整正文。身份验证：重算每个正文和完整子树，与 GitHub 固定对象相接。没有宣称逐个通过 connector 下载了全部 59 个正文。

| 固定产品相对路径 | 正文行数 | SHA-256 | Git blob |
| --- | ---: | --- | --- |
| `ADOPTION.md` | 89 | `6a1eb4cdc4c528bbd1098fb5890d0c25c098902e1aff7cd9ed16efd7de0bc2db` | `7639d60377c5a9fff014284e97be342dc5f6c7b9` |
| `README.md` | 30 | `89c6229fd7821354c5df7659c2d73c7ebf3acc1a24ecf8ce3e0c9b94d7fdc0a9` | `fe4a4b7d234444dae8feb8d8892bd52f94ecaefb` |
| `authority/README.md` | 17 | `01fe9a811a465786ffec8bfd931a5140663bf9f86e85fdd87e4ace9f7d351d12` | `b543b7d3c4865788a383e842215f33dd61ede056` |
| `authority/RESPONSIBILITY-BACKBONE.md` | 182 | `ce82a70016a4a3fc234ea287f39aac8d79a260ddf13747c4fb705bda580453ba` | `6cb486e5f9897fdff2d3c03f687aac987771f7e1` |
| `charters/README.md` | 50 | `9d745b0c4cb8fe2f9291cf254991c2257e1ef97d6e59d82f32856b54b1b44cd1` | `f22c0ded68aff34c3ee973c23ea246b21ffe26f9` |
| `charters/examples/implementation-cross-module.md` | 27 | `b159bf96323a9b89a286a5d80fdd703a1375da02467a60645e989b4903336627` | `af1ecfc431ed7d0aa32c2e90c895dfe5ff99d64c` |
| `charters/examples/implementation-local-fix.md` | 27 | `b0dff7041e7edb970d384231df5582665a8ce7765dd2833fd8ff9ff14de6d927` | `417922df98ca3b12a3cf7c44d34ac5bccd094a73` |
| `charters/examples/technical-planning-cross-module.md` | 27 | `8d1168ae783e5b23c9f21419ac218ac0a193d078c98cc3e856893c9e44306f9c` | `21e81189edeabebef7b3da7371ba66ebdca83b17` |
| `charters/template.md` | 27 | `31a2b2c4bcfa4a7e81c5bd62525b6c4235f886114e19945bbc46791aed8a47eb` | `e082c4a5fb73ee12bc1fd5017b49dc7b81d80416` |
| `methods/README.md` | 89 | `521e3cc058036163ced93e7b2b5c0a8410439dd5d9124005e4394bd6eff11527` | `8a85f27987d9bd1bb19fd5d43e224bd67719c008` |
| `methods/agent-facing-cli-contract.md` | 85 | `e471ee1502adaf4ab4d32a3dcf7eaa97b5107bcf5734f49576d8c0d49f1fd2e0` | `ab196647330026151035933d8cacc8b2f1d05610` |
| `methods/architecture-survey.md` | 48 | `682d7d36471806f4809cc627f17d298ac27487a294baa5807b1703e0557fef0e` | `6d75e1ecfbad2780a7bc754374424978370ba704` |
| `methods/behavior-claim-evaluation.md` | 37 | `0d71dcc2063fc28658da4a9726de5467fe3a1f95bebb7d94cc806331613ce7bd` | `82a9f229533b3a7caef10acbffcb055dbcec8e5d` |
| `methods/behavior-contract-examples.md` | 68 | `6c9ae6ba219f9d4c6eee9739c6fdfb1edb760a50163bfdfeb2ffb47e3a13663e` | `b94d36e1f617a933f6410a6de96d8b4008605b3b` |
| `methods/behavior-preserving-change.md` | 45 | `e635088e3372031ed6a1b89bf80d5c62c1d5b2a6848ab0a7c5cf3545ec485e64` | `7389e030c7b20daea462104e9968d12e59b7626e` |
| `methods/bounded-composition.md` | 89 | `aa80e19358560d0542310e8bbc14bcb98f98d9a6e54558701a7a1036c8be0644` | `ff0f7fae64ae4a5c1f524f02e7cf56fa724ee3f5` |
| `methods/bounded-prototype.md` | 64 | `aa65d1ac4a7fdf7c28be9ee4f42cba6929a349377709d0950276b2828916a92d` | `c85ebdf3053978b82df5dd813df8e0fc855972e7` |
| `methods/change-review.md` | 169 | `214e942e959063a68de10f06853bda982162e7506fa404696db939250d82b1e9` | `ae1f9d5dbbd14f235eee44c959d7b6c7374dbbaf` |
| `methods/change-slicing.md` | 94 | `ea9cb37f6d8c63b918dedebb635547018b3129c0a93d63bc841af8643695e964` | `c2006b4ed8a892ea4b2520357c27ad37da439ffb` |
| `methods/cross-module-design.md` | 41 | `373ff499c9b56a8b5426046c017e7b9ab01770f75e670953489858438665a204` | `241df01003c7b7c8a0bbff0be2390a0ef856edf2` |
| `methods/decision-elicitation.md` | 84 | `5ce9b2939b4b2211a69ba6bee4042ec39211a01ec729d2ffaeb02183560a956d` | `d8777521d1b88bf8057bce50d0a2193f778972bf` |
| `methods/decision-record.md` | 109 | `7fdc4a510ebd39f71200e32a852fa4132e70f62173553b2b49cc7ca85492f59b` | `1d37530a87bb29bbab6150718fdc5ff1974359db` |
| `methods/deprecation-and-migration.md` | 117 | `6c71c209131cd94d2adcc010358c963ff4b82eefa61eedfc74f9960492a0a4f2` | `2a1446cded5137570d933400ad2fc55228ee7fa4` |
| `methods/design-alternatives.md` | 73 | `36653fe8d9f809831e7b1c0e4f92e093e54d735eef8864c0595c63af3849be7e` | `bf5298a2e76cb9309f4c7ba13057768af1f590bd` |
| `methods/domain-language.md` | 62 | `7bab573a300b74ddbea93cb0f047dbc677014e97a3a9751fa91fff2308b623f4` | `51c0de6c064061f6e6cae1185642f27e807f6364` |
| `methods/domain-state-and-invariants.md` | 67 | `d82206461adc4c9c6c2d0861d2ecaf37a32427989523b02c47de34f22f02a09b` | `bf84001402795dedf0dc36454b6207808ece3baf` |
| `methods/external-tool-operation.md` | 80 | `8a52d01960fa6c36a08b2940dc162b0b4c05a4d2eee6f3a4d65ca2a2e9514fc4` | `38ccf0361fe2785509a33452d144258a39cbb3dd` |
| `methods/guide-accessibility-observation.md` | 51 | `e08ef8c3b0048ab364d2ad03e4e5780195a56d64d219c0b8e1373c9f4f8e0551` | `89b4d65776e1f690256b972cc38e9152f443d847` |
| `methods/guide-agent-text.md` | 90 | `9b97dc57f9b363977c2db3506429a3d27a34ec6824d561e3700588e8627948e5` | `5415a9131567f9fa4acbafe040f2080ec730c938` |
| `methods/guide-change-shape.md` | 85 | `56e1e40edb7ccdf01d32d1e73aa66e612e59c273c3c8f302eeaa86620810eb2d` | `603499993c8e60d3fc4b8f685d1f96417ec75c8d` |
| `methods/guide-check-design.md` | 53 | `5a13dcaea0c87e76a1c005cf4b41ae486a243009359e93612a3d230d20487a8e` | `17d8aada361917f874e5d8d46366d6d33aa2eaa0` |
| `methods/guide-lesson-promotion.md` | 82 | `82bcd49e3235fd96b8ab515942b6cd8acbe444cd516207e0fdc1c70cd1b024e5` | `4f819c17374a059f372878c66ebb568e2e285e02` |
| `methods/guide-mock-adapter-choice.md` | 45 | `967f089fa57d7a803b6657836a1ba4610d27c60b0fe9342e96d9a268b0d7414e` | `f6d60a30d44e78127a798a3669c299444a0c4efc` |
| `methods/guide-positioned-artifacts.md` | 57 | `9864a33c0a3f2230e11eb8210484e45e575b670079b381bdfc43b4e37a229aca` | `7142a84482dfa2b85a6e6c9b30b6f4fd16f7cfcb` |
| `methods/guide-professional-explanation.md` | 65 | `7a79d708454eec70f9462400a20611c0794ceb4fb609f91c6bf8271d98632d28` | `41e92283addd78c84315c6441d7259b26e178850` |
| `methods/guide-redacted-evidence.md` | 56 | `0abd46cec7198ae97671dbc03e428be559cd75927537a9bd06ebd2c63aef5335` | `e2b620698431e86074456b2c84b98c30c378451e` |
| `methods/guide-test-evidence-quality.md` | 112 | `0ea7a4ec3c1cb5da3286ffe68aec4770f6da370f59a25cc58bcefe496e2063e6` | `e71e5f8fecaff53c32a6380f00856faa9d649e3c` |
| `methods/handoff-and-resume.md` | 146 | `1ac789b455eb42521b6f8e56487b2d180cf324f57b83e67fccd42b2c1d669ca8` | `12e394d6c3728bb2e821abc49bc24503933a69e5` |
| `methods/human-procedure.md` | 45 | `00004bc8a95b0f796d40a64391bcc8a512b21f239cb87ff7d1ab9e5bd3f145dd` | `bd75e213d8fd9501c35a286a39220c905142385b` |
| `methods/interface-contract-and-retry.md` | 150 | `7576b9f1e4a5c173a4d48bf9a1db7948827d49d3081d5e38a592428e20f87b08` | `8def292ccc39f6503358ba4940c133871ec8cd83` |
| `methods/local-defect-feedback-loop.md` | 81 | `0feec14d81db315262f79a9709a67b08d621d8833e3e28ad9c55beedc90a8bd2` | `babcb158334d46f4243bb23d1a06c3995a2edfb0` |
| `methods/merge-conflict-resolution.md` | 54 | `29f91abdb0bf3daa3c40455f8b007fa0865833fb7f9bc2441dcd721168bc2ebf` | `6f8d566e96635a84adff938114717d15462eaab7` |
| `methods/observability-design.md` | 119 | `73334523cc7d452af3dbf8a649dd4e6f7757c976de7d7a58d3dc742176d28d13` | `f97442f86664eb3228b6708e7181c5b7190d1be3` |
| `methods/performance-and-neutrality.md` | 162 | `0563362fd89303635617e1550bed834bb849f942f6bdbf8aeb07b3798b5e48e9` | `60db9b51505fcffe9d95a2b52f33f3ac0365f225` |
| `methods/professional-learning.md` | 43 | `925dc0aed5e903d459677d74377b1db64f498993e34bdf2da7e60e311a1413c2` | `6b42c92194a63c443cdc646719c3b865fbaca7ff` |
| `methods/quality-policy-enforcement.md` | 107 | `2e2f6d86ca1db4f9342b13804e630f8b79001543ed120469cc59cf8689bf2f01` | `686d6321cf486168688742da38d0b59d43553471` |
| `methods/rationale-and-premise-review.md` | 93 | `bb3c19d3372b109a854361b157294d1adcbb13cee601463aca799b6e5d434a8f` | `7227d58c66d35de0e9bf24cdf26277731479d456` |
| `methods/release-and-recovery.md` | 88 | `11afc4e70e6e729a8d3486cc0000d6c0ae80487e14c57f193ca459854c21fb2e` | `22b60b676dcd9719fad238ab0b85a6bd2e0f6a3d` |
| `methods/test-first-behavior-slice.md` | 65 | `5d664c28b3352576e5a3082c369e29692a6fc6102942567818f45313842b5310` | `9d4c1553582e14adb6ccc979a853d192c575e5b3` |
| `methods/trust-boundary-and-actions.md` | 175 | `31b23c0d7a86c11a2d992dff731d0de6b14b9ce416a7e27cc340234ad9739a41` | `6c5d88ab90c0fe8727c6c2e389875758aff484b0` |
| `methods/uncertainty-planning.md` | 49 | `d37a4ef1cace6786f31db307d1808a57c7248fb16cb20a62fa387f4adedf5601` | `b74a9aeeddb0d5da7c94990c05bd3a420556a6ac` |
| `methods/verification-harness-design.md` | 118 | `ae9bafebd5209f8d134019a53ee3f1ebabf297a654806a0550b34f2e5b359c72` | `57fb91adac46b4ab5a00e4528f0056fbf9aa7cbf` |
| `profiles/README.md` | 46 | `8e7449974763e6de656f58699dc345149f86f20c73db630f3d35541df6ec6486` | `c9a7bee50166956468f191d0f2b131f45d1af3ec` |
| `profiles/behavior-domain.md` | 51 | `ef214632f1d1a601ea045153702e82e2338c3da34513c14b67bf41afa18631b5` | `ab87328bc4f86d1cb4c9d52edcdbd300b0819f33` |
| `profiles/driver.md` | 45 | `0703cf617940f70d532771c52629ef33ee30ae25b40aa5b358d7b5c526d775ea` | `5d657bec2b5ecfad79d20dcb93192ea81c2a09cb` |
| `profiles/evidence-evaluation.md` | 45 | `6d11c157c6bd3ff7cb8f90e8a04a57ad08df72fcce5fd26636d3459efe4ec73d` | `81a474a2c22dbf86b42c5ca666dc1ee4d7a6c0d8` |
| `profiles/implementation.md` | 43 | `8ca992608a1fdf66fda24035ec9ab40f7717f2527adfd37b624f656bdb2855de` | `5c5cbe958703044aefc53cc16cf50b28c086fcd5` |
| `profiles/intent-voice.md` | 43 | `919f3e7d49efe42979e971f1446cae77a7b0238b7e3845fef26e72c4e8f1ab78` | `467cd3da858660f0ee5f1733856bd334fb97b576` |
| `profiles/technical-planning.md` | 48 | `ff3c57ec6ce823cc8cc6aca28248b609df695aa70a3eed69dea7fa0b6b1239b6` | `cac2a2f674b1c3d5a67b6caf12e6b460153e1dc5` |

## 支持材料

以下 9 个支持文件均已在附件中全文阅读；进一步将其完整正文计算出的 Git blob 与 `edce02a9` 的 connector 对象核对，9/9 MATCH。三个 reader 的 SHA 来自固定目录列表；两个限缩评价与机械报告还直接取回了正文；通用示例、计划、追加 brief 以固定文件元数据 SHA 核正文。

| 路径（固定 edce02a9） | Git blob | 状态 |
| --- | --- | --- |
| `adoption-examples/cross-module-start.md` | `b7a8a8a12fd64020b37d45aaa693ef4e3c8d5d9a` | 全文已读；字节 MATCH |
| `docs/absorption/2026-10-02/EXECUTION-PLAN.md` | `881468e5da7a9ce18ee1284dde14f9620aad1ffe` | 全文已读；字节 MATCH |
| `docs/absorption/2026-10-02/ADOPTION-DELIVERY-BRIEF.md` | `2b2beaf221bf369cdc26aedcc96684f465320679` | 全文已读；字节 MATCH |
| `docs/absorption/2026-10-02/reader/READER-EXISTING-GOV.md` | `6362016d8b200ffabd54c67b07a95b5067b2514c` | 全文已读；字节 MATCH |
| `docs/absorption/2026-10-02/reader/READER-LIGHTWEIGHT.md` | `a2329a2cca9450c2e99390d86f9e7fc57b9d9c2f` | 全文已读；字节 MATCH |
| `docs/absorption/2026-10-02/reader/READER-PROFESSIONAL-USE.md` | `5e444dfa4f78a1b2eb193c288a65caf1659bc3d8` | 全文已读；字节 MATCH |
| `docs/absorption/2026-10-02/reviews/REVIEW-READER-CONSUMPTION.md` | `c80aad206039e88f4ee23320db019b02800c646e` | 全文已读；字节 MATCH |
| `docs/absorption/2026-10-02/reviews/REVIEW-READER-PROFESSIONAL-USE.md` | `13078f46f01aad04fb8dbf0b701e3ee60cb496ac` | 全文已读；字节 MATCH |
| `docs/absorption/2026-10-02/reviews/INTEGRATION-CHECK-5d7d89d3.md` | `617b0c512cc8e2d5c67bbeb0564587482b3bef69` | 全文已读；字节 MATCH |

`LEDGER.md`：定向读取，不宣称全文读完。读了附件提供的全部 tail/accounting/停止点，并从 edce02a9 回源核其 §基线（首 30 行）、L120 起的批次片段及 tail/未采/未读/冻结段；connector blob 为 `29267b9d6132544c4d532393df3357e65b95728e`。没有独立重算 1240 路径会计或复核所有 51 份 review。

## 三个上游的实际回查范围

这部分为定向原文审查，不是三个源仓全覆盖或软件资格认证。未执行下列文件中的命令、安装步骤、测试或 probe。

### Addy — 2686b620fc1fed2e8f60c704839c766b8594c6b6

- `skills/api-and-interface-design/SKILL.md`：全文回查，意图/尝试、原子占用、payload、在途、未知结果、保留与源边界。
- `skills/shipping-and-launch/SKILL.md`：L1–260，清单、flags、分批发布、阈值、error budget 与恢复入口。
- `skills/deprecation-and-migration/SKILL.md`：L1–225，消费者、迁移选择、expand/dual-write/backfill/contract、可逆与 DDL 假设。
- `skills/performance-optimization/SKILL.md`：L1–215、L320–490，测量与瓶颈、池/索引、缓存、噪声/neutral/因果及保留-回退判断。
- `references/accessibility-checklist.md`：L1–155，键盘/modal、ARIA、语义与数值/合规来源限制。

### Matt — c55ee46073ed923f86ce59a5eb3b6d895095d1b7

- `skills/engineering/codebase-design/DEEPENING.md`：全文，四类依赖、接缝、原文 replace-don’t-layer。
- `skills/engineering/tdd/mocking.md`：全文，system boundary 与内部替身、SDK-style interface。

### Cursor — ecc249f1e306fc64ddf83c7bed16cacf7c2239db

- `third_party/x-money/skills/x-money-guide/SKILL.md`：全文，平台动作规则、特定 unconfirmed 支付结果与网络故障同 key 重试的区别。
- `orchestrate/skills/orchestrate/scripts/schemas.ts`：L1–400，结构类型、PlanSchema.superRefine 的重复/self/unknown/cycle 检查；未读余部，不声称审完整生成器或运行 graph。
- `orchestrate/skills/orchestrate/scripts/cli/util.ts`：L1–650 返回至文件末尾；诊断遍历、argv/env/cwd、OS-home operator flag、目标来源与 nonempty 字段。
- `orchestrate/skills/orchestrate/scripts/models.ts`：L1–230 返回至文件末尾；模型目录与选择映射；不是 probe 实现，也不证明模型可用或能力。
- `orchestrate/skills/orchestrate/scripts/cli/inspect.ts`：L1–245 返回至文件末尾；models --check 路由到 tools/probe-models.ts。
- `orchestrate/skills/orchestrate/scripts/tools/probe-models.ts`：全文；create/send 后先置 ok，再 getRun/cancel，取消异常被吞。仅静态阅读，没有调用 SDK。
- 固定 `scripts/cli` 目录用于定位；尝试的 `scripts/cli/models.ts` 返回 404，随后沿实际目录与导入追到上述真实实现，未留下 probe 来源访问缺口。产品原锚 `models.ts (probe path)` 不精确，作为非阻断来源修正建议。

## 额外外部验证

- Chrome for Developers：`Enabling bfcache for Cache-Control: no-store`。核其官方页标注的日期、条件及“expected rollout”措辞；没有由网页说明推导当前所有浏览器/企业策略下的实际运行状态。
- NIST Engineering Statistics Handbook：§1.3.5.2 Confidence Limits for the Mean、§1.3.5.3 Two-Sample t-Test for Equal Means。用于检验“原始 run spread 必须小于收益”的推理；不是 TPW 已吸收的第四源，也不要求下游引入统计框架。

## 未读、未核及影响

- 没有全文读取三仓 1240 条会计路径；没有独立复算全源实质采纳率或知识增量。
- 未读产品声明保留的完整 tail：其余 runtime/prompt/adapter、workspace-audit、第三方模板、SIM/CI、测试/评估 fixture、教学格式/阻塞 API/原型 scaffold 等。它们不是本次库运行依赖闭包的已验证组成部分。
- 未全文读 51 份逐批专业 review，也未读取角色会话/执行 transcript；本次判断来自当前产物和所列原始来源，不能认证既有每次审查的实际独立性。
- 未运行 TPW 任务、源脚本、SDK、Provider、部署、性能 benchmark、浏览器/读屏器或并发/资源恢复实验。文中的反例是分析/构造，不伪装成运行证据。
- 未读旧 roles/skills/registry 作为候选依据，未审远端旧 main，也未读 UCBIP 仓库或授予其资格。包外可选 `adoption-examples/ucbip.md` 未全文读取；其 reader 引述不算全文阅读，core 的装配不依赖它。
- 未在一个新下游仓库实际运行 direct-read 与 vendor 两项工程任务；装配/指针和正文可理解性判断不等于宿主选择/执行效果。
- 未审许可法律结论；README 的来源/保留文字不是再许可证明。
- 不将上述正常范围限制升级为“整库无法审”。产品字节可核，三个必须修订项的承重原文可取回；它们是方法语义/判定正确性问题，不需要重建运行框架。
