# 固定集成 core 候选 · 独立方法评审

2026-10-01。Reviewer：`tpw-night-method`，未编写本候选正文/guide/入口；此前 findings 为独立质疑与补证要求，不构成作者贡献。

**Disposition: PASS（固定实际字节的有界静态方法评审）；无 must-fix。** 三方法增量、两份按需 guide、IM-1 适用边界和候选状态在实际 core 中成立。不是整体效果/运行强制力、Pro 或 Oracle 的最终接受，不授权晋升、发布或下游动作。

## 精确对象与身份核验

- Review commit：`20640db3999e9a6514f2e7d0896a385bad05fb70`；root tree：`e9651722e3d3d20a0392b3c69cf6362d40650d17`。
- Core subtree：`69226762d65a7ded108977df7e816fe7894e795e`，21 文件。
- 比较的已接受 core：`91875114e51855517f92ef099cbdf60c34e68243`（`29d8b09e416028ad68bc72da23452c6e23755a5a:professional-workflow`）。
- Manifest：该 review commit 中 `docs/overnight/2026-10-01/ABSORB-CORRECTED-CORE-MANIFEST.md`，SHA-256 `119136ed5b9401094d1908bcc5d1aaac3a081041bf170ad1656b8741dea52cef`。
- Manifest 自己固定的 source commit 是 `eb7930b42524096a7a286186ba4561df7b95a24e`、root tree `cc16a7110f1c93976887daec6f5d0a328bac1126`，不是 review commit；两者 core subtree 精确相同。21/21 文件摘要和 exact path set 与本次 review 对象 MATCH。
- 对 manifest 指定 source 只读重算 `git archive --format=tar eb7930b42524096a7a286186ba4561df7b95a24e professional-workflow`，SHA-256 `6fa0738773c38c30007da418c070698963b5ea205202b0ecd0553b866f902d57`，MATCH。仅在内存取/hash archive，没有落盘或宣称另一commit的archive同摘要。

相对已接受 core 的实际 diff：7份文件修改（根README、charters/README、methods/README、三方法、profiles/README），2份guide新增；其余字节未改。Backbone 摘要仍为 `ce82a70016a4a3fc234ea287f39aac8d79a260ddf13747c4fb705bda580453ba`，Charter template/examples及所有Profile正文也未变。

## 受影响文件字节

| core 内路径 | SHA-256（manifest与Git实际字节一致） |
| --- | --- |
| README.md | `b146920ebcf03e1a14b5fc401c4ffba28a2475386e6b6244e73f80affc6f9a27` |
| charters/README.md | `3fe252aad220e77be434c2d3ee0390da79d998b6c35807c5a763a250a552fda9` |
| methods/README.md | `ccc0f141864419eeaf4671d09c6adc61bbdc64bc1d747acd1d9e4b1ef1390a8b` |
| methods/local-defect-feedback-loop.md | `41ddaf9ca133dd25da1c5e71c20fc4263b51a571bc1bf99bea86843c8d0e434b` |
| methods/behavior-claim-evaluation.md | `0531835f77a8c176df4f173cee64ceee89a21e412ee471a7cc1b0b82f4110c99` |
| methods/cross-module-design.md | `f9d9c040a94381886fd6f01dc651d25740997cdfe6ab4436498fcf570fcb68c6` |
| methods/guide-redacted-evidence.md | `7c10676614e717715cddba33b6c3f5abb4d5e62d45f911653712dab4ae16d04d` |
| methods/guide-mock-adapter-choice.md | `5ad055b39a7af01ded16399e10a63fab31b452a30e51522e9b502ff23c059208` |
| profiles/README.md | `5fa0e3153a43529470aea48a37e9cb7f98872ef5d89d47f18f90bd3fa55c7d7a` |

读取/机械核验仅 `git show/rev-parse`、限定 `git diff 29d8b09 20640db3 -- professional-workflow`、Python/hash解析及上述只读Git archive。完整读两份实际guide与改变的入口/方法条款；静态回核六份固定源的chapter/function锚，沿用此前已完整或按承重章节核读的正文关系，未重新研究未变Profile/Backbone或全库。未运行草案例子、upstream脚本、UCBIP checker/test/service或网络。

## 专业 claim 逐项结论

1. **三方法只补已证缺口：PASS。** local-defect Method5补证据形式/保管与HITL分流，F Method2澄清保留original output不是持久化机密，cross-module Method3补test-double选择和production adapter覆盖边界。与已支持预稿的目的/内容相符；修正了空间歧义，要求说清哪段真实normalization被哪条test执行，而不是移动到仍被替换的adapter。三态、独立性、兼容接受权及原Limits未被削弱。

2. **源保真与自拟关系：PASS（静态、有界）。** redacted guide 的 Matt pin `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`/diagnosing-bugs `Redact`、loop出口、HITL script `step/capture` 与 Cursor pin `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`/verify-this `Artifact Layout`实际存在；mock guide 的同一Matt pin下 mocking、codebase-design `Principles/testability`、DEEPENING `Dependency categories/Seam discipline/Testing strategy`实际存在。每份guide有完整pin、repo-relative path及章锚；自拟raw保管操作、401因果限制、port-vs-adapter推论/协调和整段例子都标为authored，不把共享DI误作三份全文重复。保留sometimes/stand-in存在/内部seam等适用语境。

3. **IM-1在实际字节落实：PASS，原唯一must-fix关闭。** redacted guide Rule4明确：通用raw需已有有效同意、受限位置、保管/清理与不自行扩权；真实任务access/data/network继承有效policy/Charter，既不授予也不无条件取消已有许可，既有有效授权无需每步重问。无真实用户/活网络限制标为本批offline example mode，Example Raw branch也一致。主方法插入同步使用通用条件，不再把这批演练限制变成所有真实任务的永久禁令。

4. **真实消费入口与task-local绑定：PASS（设计/字节层）。** 两guide真实存在于methods目录，support表按敏感证据/HITL或dependency/test-double需要指向它们；table后句、两guide Use及local-defect插入明确需要时加入本次已有bound/read set，不mandatory loading。既有Charter保持真实delegation、Applicable methods、权限/独立关系，既有装配可把相关guide与bound method一起列入，不新增字段/框架。不是实际cold-reader已成功消费的结论。

5. **无新增越权机制：PASS。** 只有三方法＋两个按需知识guide，没有新Role、runtime、generator/validator/composer、额外审批节点或固定phase链。没有内联A/B183统计/146裁定/R分级审计记录到默认startup。四个旧名仅在scope声明为没有等价body且不复活；下游是否映射/采用仍归其有效owner，不决定UCBIP task/priority/写窗。

6. **测试替换窄条件：PASS。** cross-module Method4原字节仍要求replacement覆盖对应accepted claim，并且method不授予删除权；mock guide Rule6明确保留这两项，不将源的replace-don't-layer推成always-delete。port/in-memory与production transport解析的覆盖区分保留；无“owned即全部可mock/永远不可mock”的泛化。

7. **入口状态与接受区别：PASS，有非阻断可读性残余。** profiles/README解释M1内容已有原接受且自身不激活方法；charters/README解释M2是设计snapshot；根README与methods scope明确当前改动是night candidate待定向recheck，既有M6接受只拥有旧固定对象，不把21文件新tree标成旧accepted core。guides自身仍candidate，诚实。旧M4/M5来源表保留为各自snapshot，不是新三方法hash表；实际新bytes以本报告/manifest固定。

## Must-fix / suggestions

**Must-fix：无。** 本报告不要求因为状态或纯metadata hash变化重开全审。

非阻断 suggestions：

- methods来源表的“Current M5 candidate”宜在后续允许的说明性编辑中明确“historical M5 snapshot”，避免单独读表误把旧摘要当当前21文件；scope段已经解释其own snapshots，本次不因词语造成新gate。
- 根README的当前identity导航可直接指既有 `ABSORB-CORRECTED-CORE-MANIFEST.md`（注明TPW repo过程记录），而不是只指旧RETURN-MILESTONE与泛称later correction records；profiles里的裸 `ORACLE-ACCEPTANCE.md` 也可标TPW过程路径。当前没有假接受，只是导航仍依赖repository上下文，不要求新状态文件/ledger。
- guide的Wrong persistence例子应按“未经明确raw许可的默认路线”理解；已有独立raw许可下的受限采集不是同一情形。Rule4及Raw branch已提供该例外，后续编辑可把短例句限定得更直白，避免抹去刚修复的通用条件。
- 2-adapter原则作避免无谓间接层的设计依据，不要为满足数量造第二实现；当前Limits无mandatory port已限定它，不需要再造统一资格检查。

## Residuals / disposition limits

本PASS只覆盖 `20640db3` 的实际core语义增量、源/自拟边界与消费设计。没有重评全部源机制、未读B候选或文章，相关源工作仍provisional；没有因21文件的新身份全量撤销旧M3/责任证据，旧证据只继承未变claim的原范围。

未独立运行secret-sentinel/adapter契约演示，未阅读或验证manifest所提demo observations，也未观察fresh-reader实际绑定，因此不声称脱敏被宿主强制、production adapter被真实验证或知识使用可靠性已运行PASS。自拟例子的可证伪逻辑有支持，但运行观察是另外的覆盖面。

archive/manifest完整性是机械证据，不代替专业有效性；静态方法PASS不产生Oracle接受、Pro裁定、local main晋升、remote push/tag/release或UCBIP动作授权。本scope下一步按已有委托汇集必要局部观察/独立冷读与固定对象，Oracle仍按授权条件作接受，不新增常驻gate。

仅写本报告；未代写或编辑core/guide/草案/上游，未实施、派工、提交或跑UCBIP。用户 `scan.js` 未动。

2026-10-01 delta确认：**PASS，原静态PASS范围与IM-1边界继续适用**；新对象 `bc1c3fccd3703ca3095875160dcfa8b0a1bfc8aa` 相对 `20640db3` 仅四处已建议的措辞/导航修正，未扩大raw许可或改变方法主体：`methods/README.md` SHA-256 `2fe8d51db93b73bccdd013867c8e83c518fdf62fec7b94dfe30ad695baf9acb0`，根 `README.md` `ee5a284328b80d19a6450415c3604f2405324d2535448638a8b97ea148eca3bc`，`profiles/README.md` `e2a37dbaecd3747300c6ad652403e3ceec1b2708395ac36498ff897797e4244c`，`methods/guide-redacted-evidence.md` `8961cf6fa57ac03f9b7b6b7f661cb7b44f31b679ac1d7e87fff3b2076dbd2fb4`（均从固定commit实测）；新例句限定未经授权默认路线并保留Rule4例外，历史摘要列/TPW过程定位更明确；无新增must-fix，不重开全审，不将旧manifest/archive身份外推到新bytes，原运行/接受残余不变；只追加本行，未改其他文件或提交。

2026-10-01 Rule2定向确认：**PASS（方法安全与可用性的静态解释，不是运行效果PASS）**；固定对象 `08d990727deaea13e220e8764f9a3ecf7a8bd4cb` / core `baf2991e004912b14048098d42ad024fc441324e`，guide-redacted-evidence SHA-256 `9d2e43a10d7a83e4e8fe69942399dc376f40e2159bc98c7c448a0c517dab0b0c`、local-defect SHA-256 `cc8f3911125c8ec8c7b87625590dbb3ffbbd29da4c10b06e785ed1cbaa0d6348`均实测；相对 `7461778` 仅两文件指定四处差分，Rule2允许在有效授权内新采集或复用最小必要证据，展示/记录/共享/保存前脱敏，raw依Rule4，既不扩权/授权未许可捕获也不逐次重问；旧记录明确只是常见一例，不再禁止build loop的新观察，Matt保留内容与collect-or-reuse自拟adaptation标注诚实，主方法指针同义且三态不变；batch-only尾注已不在通用Rule4/raw支线，不产生全面synthetic/no-network政策；此前PASS未单独识别Rule2的过窄限制，本次明确确认该受影响语义已修，其余既有范围/残余继续保留，不全审21文件，不外推旧archive身份；只追加本行，未改作者正文或提交。

2026-10-02 audit后定向确认：**RETURN／定向静态FAIL（不重开全审）**；对象 `1184fcc553292d8745d94b165ab103f0ee1a3fe2` / core `82e30fc5a6abc51a7fba46fa7b7cb10bc2f49e7f`，F方法 SHA-256 `25086584eb4acd9ef7d1521153f3c3c9b164f253223b1ee027fbd2276375181e`、mock guide `c3ba6c254dab10db4a417a0895dc21d87c377a9376cfbf26ec40659e0f733abc`（固定Git字节核对）；audit在该commit未提交，仅读工作区上下文，不当固定core证据；MF-1两个示例已把失效M5摘要标为historical并保留当前绑定入口，NB指针/历史声明无新增许可或gate；§Use按claim天然要求选验证面、真实对象所需适当证据继承policy/Charter与召回、不强制全任务真实e2e的方向成立，guide应仅引用/按adapter语境应用该单一原则，不另定义测试mode；唯一未关闭的新claim是Rule3泛称port/in-memory测试同时覆盖adapter-level mapping——替身直接返回领域对象时并未执行真实映射，须限为实际被测试调用的映射函数/路径，不能把便宜替身全绿扩为被替换adapter的证明；本次仅拒绝这句新增过强覆盖断言，旧PASS／IM-1／Rule2及其他未变范围继续保留，actual SDK/Provider关键词也不自动要求网络全e2e，证据强度仍按具体claim；只追加本行，未改其他文件、提交或实施。

2026-10-02 Rule3 delta确认：**PASS，1184fcc唯一新增覆盖断言FAIL已关闭**；固定对象 `8a7db4a74fe8dffc7378b3ece52f89a3b77ba791` / core `5e2c6b2dc13c773e2d1749c6efb82312cf8435f3`，mock guide SHA-256 `3e047e1f5ef50cce907364ed7159d21b622a2ec9f48b71c6b60db3d0c397bdac`实测；相对1184fcc的core差分仅该guide Rule3与例句，明确double只执行测试实际调用的内容、直接返回领域对象不执行被替换adapter请求/transport/mapping，正确测试面须实际调用mapping路径；guide按adapter语境引用behavior-claim-evaluation §Use，不独立设mode白名单，适当真实证据仍按具体claim及有效policy/Charter、非所有任务真实e2e且不新授访问；MF-1/历史指针已关闭及旧PASS／IM-1／Rule2未受影响范围继续适用，无新增must-fix，不重开全审、不外推旧manifest/archive摘要，原运行/接受残余保留；只追加本行，未改其他文件或提交。

2026-10-02 entry delta确认：**PASS，非方法/授权语义变化，无新增gate**；固定对象 `a41f6962f8fe061c8ef8cc4466bb43180db5d35c` / core `e5e5338ed8abc717bdda48e0f4ae751dea30dbb1` 相对 `8a7db4a` 实际core差分仅根README历史层压缩及两个Charter示例删除历史M5摘要子句、改指现有来源/manifest并要求本次固定对象而非复制陈旧digest；六Profile方法绑定指针与Intent历史标记已在前序对象落实，此次未再改变；方法/guide/Backbone字节及执行授权未变，candidate与旧接受仍分开，MF-1关闭保持，绑定本次适用固定版本不意味着所有任务追最新HEAD；原PASS／IM-1／Rule2／Rule3未受影响范围和运行/接受残余继续适用，不重开全审、不把旧manifest/archive身份当新tree身份；只追加本行，未改其他文件或提交。
