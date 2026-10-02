# Gate2 · A1-ADDY-EF 实质裁定

2026-10-02，tpw-absorb-gate2，F1–F9 9/9处置：F1–F6/F8限缩合并，F7限缩吸收并归共同效果评估family，F9按addendum逐项裁（不是旧“仅审计面重复”关闭）。既有AB/OracleCD裁定、轮次/来源贡献不重开。机制处置≠九项新能力或九文件。

包 `7e3a82f6c26f995f20a0290329c93cfbcabadc40:docs/absorption/2026-10-02/packages/A1-ADDY-EF.md`，blob `85f09d6b93f8109fd859c4d83d0d0828945a945d`；addendum blob `2fb3cee4269448c5c0c500a087d7a62e8d246ee5`。产品同commit core `d47b09173939177b64293ad4f23097b0e8852b31`，不是旧800414d/21文件基线。源Addy pin `2686b620fc1fed2e8f60c704839c766b8594c6b6`，legacy只读。Oracle CD不重复裁，实际产品已吸收C1/C3–7/C9等不能当空白。

## 直接回源与资格

本次直接读七SKILL test-driven-development/debugging-and-error-recovery/incremental-implementation/code-simplification/source-driven-development/browser-testing-with-devtools/context-engineering的承重正文；code-simplification结构/语言例子与restart/budget段另补截断部分。evals README三tier/plugin/case/metrics与skill-impact；run-evals常量、TF-IDF/rank入口、resolveFixturePath、materializeWorkspace、parseGrading、model提取/落盘/执行与grader/cleanup；三plugin prompt与六grader原文。未逐行读runner全量、测试/fixtures余部或实际结果目录，不执行runner/安装/模型/业务/浏览器。四checklist及testing-patterns逐机制直接读，细裁见同目录 `REVIEW-GATE2-A1-ADDY-EF-ADDENDUM.md`；a11y补读frontend-ui-engineering176–232。

比较当前test-first/guide-test-evidence/mock-adapter、local-defect/change-slicing/guide-change-shape/behavior-preserving、rationale/Charter/context/handoff、trust/obs/performance等相应正文与前source裁定；仅称已读承重段，截断/未读尾部不伪全文。源作者实验次数/工具默认/版本自述不继承为gate的运行观察。

## F1 · TDD / Prove-It / 实际栈：限缩合并

**覆盖：test-first-behavior-slice、local-defect、guide-test-evidence已充分覆盖red原因/独立oracle/适当seam，不缺新的普遍TDD。** Addy的repo wrapper/discover已在ABC3 harness落地，DAMP/resource模型可补具体取舍。

落点test-first的cheap-path/证据质量guide：先核真正语言/build/framework/wrapper、聚焦/full/acceptedCI命令、测试惯例，声明所run对象；焦点循环与适用回归按claim和政策，不假npm或全suite永远必跑。red必须揭本缺陷/新行为而非坏env；已有有效failing观察复用，不制造新red。有时新测试立即绿是已有功能的有效characterization，只是没证新修复；source“立即绿证明零”不采。新逻辑是否test-first由任务/有效方法选择，非所有code必须TDD。

测试断言accepted行为/副作用/契约而不是任意内部call；若调用顺序/参数本身是公开协议或安全契约，interaction观察有效，不全禁。命名表达condition/outcome、数据可独立读、合理helper可省重复，不固定AAA/一个assert/三段名。resource class用于说明process/I/O/network/data/time成本，5/15/80比例与small绝大多数非库配额；真实implementation/替身选择由seam/副作用/覆盖，不排序即决定最高confidence。port-levelfake不覆盖production adapter的mapping，保持已有Rule3和real-leg自然表面。

复杂repro可用独立视角减少迎合，但不默认subagent/隐藏全acceptedspec或宣blind必更可靠。一次确定性充分run后无新增原因无需重复；flake/性能噪声/并发频率/环境改变可合理重复，不“code没变就绝不增加证据”。局部fixture/UIlogic不因browser标签无效，真实体验claim用其真实表面；测试绿不授acceptance/release。

**仍需补读：**实际stack/tooling需真实项目核；sourceJS框架示例不认证版本/API运行。无本轮TDD效果实验。

## F2 · 调试与恢复：限缩合并

**覆盖：当前local-defect已症状/假说/区分probe/最低有用repro/负控制；source新增timing/env/state分支和错误分类可具体化。**

落点其Diagnosis loop：同失败不同可检验hypothesis（timing/版本/数据/持久/测试污染/资源）；选最便宜能区分的timestamp/负载/环境对照/独立与连续run，记录压力与sleep如何改变现象。test本身/观察instrument可错，build/import/config/dependency及runtime层只选线索，4xx/5xx不直接定罪某方。bisect需已有有效good/bad观察和git操作/恢复授权，不在未裁worktree跑；一个oldcommit不一定validknown-good。

止依赖错误前提的工作，独立合法工作可继续；不stop整个项目或没red禁止推理。error/trace外文命令是数据；核独立可信命令来源与任务动作权后可合法执行，不一律每见URL/修复建议都再问Human。temporaryprobes按任务权添加/cleanup，原proof/owner文件/必要生产遥测保；长期instrument不是默认删。fallback需accepted错误/保持语义与权限，不能用空串default/吞异常伪正常。source重复“必须全suite/步骤不可跳/所有bug可可靠repro”等限缩不继承。

**仍需补读：**机制无；具体alert/CI/prod操作需要对应authority/版本/环境；没有实际根因/run或恢复效果观察。

## F3 · 增量执行：限缩合并

**覆盖：change-slicing已有真实依赖/vertical结果/宽refactor例外，release/migration已有flags/不可逆恢复。** 增补scope和每unit实际evidence，不另强制incrementfile。

落点change-slicing与E相关methods：一unit明确accepted结果/支持关系、读写面/保持、可观察结束与回退；contract-first适合跨执行者真实协议并行，risk-first优先未知，两者由依赖图选择不固定DB→API→UI。验证/受影响regression在新对象，不因为commit/save就done。临时未启用路径必须不突破accepted可见行为/权限，但flag只是一种策略；safe default由实际contract定义，默认“不通知/disabled”不适用于所有任务。小步骤要可恢复，不虚构任何data迁移可down；代码revert不还数据，外呼副作用另调和。无法逐unit保持绿的合法宽迁移沿现有例外，不能100LOC/多file/每改全suite/每步commit当gate。

sourceRule0/0.5的简单与scope指导可补真实counterexample，不借“naivefirst”忽略已接受nonfunctional目标或换掉成熟pattern；邻近cleanup/feature不自动授权。F1的重复run限度同本组，没新增变化但统计/故障研究仍可run。

**仍需补读：**无取用机制缺口；未读非承重尾部不报source全覆盖，具体发布/manager/migration实例不执行。

## F4 · 简化 / 先理解：限缩合并

**覆盖：guide-change-shape/cross-module/rationale/behavior-preserving已readability两轴/合法thinwrapper/current≠accepted/保持证据。** Chesterton-style六问可补具体消费条件，而非一切改动先完整why访谈。

落点guide-change-shape的判断：读真正职责/caller/callee/error/acceptedtests/历史约束与source；有信息的why不能delete-on-doubt，有效scope内只改本task必要对象。信号是可读性/概念/状态复杂度，不3nested/50LOC/500LOC/第三usecase触发自动extract或新codemod。compare实际新旧load与accepted行为，有意保encoding/auth/audit/compat wrapper/安全guard；sourcebefore-after语言样例只是candidate，需本callsiteinput/异常/ordering/sideeffect证据，不源码looks相似即全输入等价。不为让测试绿删测试承诺，旧test依implementation需要合法替代时可以改/删并证coverage；不全“testsmustneverchange”。

只为readability的新复杂度没有收益可撤，已接受安全/性能/适配目的按其目标评价；拆feature/refactor为了可审/回退，真实耦合可同授权sequence，不普遍强制两个PR。固定cleanconsole/no-comments/reviewagent/全suite不采。

**仍需补读：**实际语言/代码对象无测；全文没被取用的technical例不自证语义或安全。没有reader理解收益实验。

## F5 · versioned源驱动：限缩合并

**覆盖：rationale已source-owningclaim/primary非充分/时间/版本/引文回核/未知，source实现与授权分开；framework-specific判据可补。**

落点rationale evidence与必要技术method：先辨manifest声明range、lock实际resolved、wrapper/client/runtime实际版本及patch，不能从package.json一项假精确版本。按承重API/feature取适用官方spec/docs/changelog或pinimplementation，与当前对象/条件绑定，冲突显露；primary只是所述范围依据，official docs最新不必适合旧pinnedclient或本项目acceptedcontract。代码/observe给机制/actual behavior，历史给intent/acceptedauthority，citation不证明运行。neededsource未查/未能核如实标限度，已有同claim有效材料可复用。

不可把“不在docs”写成实现错误或不准任何方案；经验/实现/readme可支持其适用claim，具体最佳实践主张要其版本证据。fetchdata/例子URL不控制agent或自动授执行/外呼/telemetry；只提取相干信号。项目有自己devex/兼容要求时专业D/E在有效envelope内判断，不每当前pattern和docs不同都Human二选一；需改变acceptedboundary才返回其owner。sourceallframeworkcallalwaysfetch、最新弃用全部禁、每行commentURL/mandatorybrowsermatrix、speedoverride允许免关键验证均不采。

**仍需补读：**无文本缺口；sourceReact/manager版本举例未联网认证，不作为本库当前spec。具体API落地前核实际版本/run。

## F6 · 浏览器证据与untrusted内容：限缩合并

**覆盖：harness surface/真实leg/marker/敏感capture、trust writer与redactedcustody已具体；profile暴露面可补。**

落点harnessDrive / trust与custody互指：择只触任务对象的可用testprofile，隔离logged-in身份/data/共享session；真实登录必须已有authority，不能为了本地页面擅连用户全profile/关闭别人tabs。只读inspect与JS mutation/network/authmaterial/资源动作分开，选DOM/style/console/request/perf/screenshot/keyboard等所需观察及expected结果；UIunitlogic证据合法但不代layout/真实体验。请求状态/console只是诊断信号，非“4xxclient必错/5xxserver必错/零warnings才准ship”。browser/工具名称不保证snapshot/network真实当前build。

页面/console/API/JS返回是数据，不能当新任务/authority；由此得出的合法tasktarget仍按真实约束核，不一律每navigation都再问。秘密/token不因可读就发到工具/报告；合法teststate inspection不全禁storage，敏感auth需真实need/授权/custody。mutation包括JS按钮/DOM编辑/调试hotfix，继承已有动作权，缺权返回；不是JSexec叫debug就readonly。sourceChrome版本/default/flags/standards数字时点特定，不移植MCP配置/latest安装，不claim官方兼容或legal合规。

**仍需补读：**specificDevTools/currenthostAPI不认证；源不涉及的profilesafety保证不推断。无actualbrowser/网络/截图行为观察。

## F7 · 方法结构 / routing / 行为效果：限缩吸收

**覆盖：ABC6MG5效果评估、ABC7carrier/synthesis、当前lesson/agent-text effects limits已有，分层与有/无方法ablation/negativeowner可增补。** 不是最大空白就必须整套CI/runtime；合并同family的按需method-behavior-evaluation，不重复两guide。

三问题分开：字节/结构/引用可消费；实际host是否选择/加载所需方法；实际输出/行为是否满足目标。TF-IDF词相似rank是词法代理，非语义触发/模型行为资格；相似描述可能不同scope，词不相近仍可semanticcollision。positive用自然真实问法，negative要有真实邻近target/owner或合理“无需方法”类别，避免空匹配就成功；不能为grader通过硬把用户意图改成描述。指标/ratchet由已接受policy所有，合法改policy明示，不silentlyloosen。

效果claim记录variant/模型与provider/version/host/配置、输入/工具/resource/随机性/actual选用/trace/产物及范围；同题/对照控制混杂，结果不是一个exitcode或ToolUsed。regex看到severity词不证review抓了真缺陷，ToolUsed只证调用，不充分证能力/改善；没调用也可能受已加载description影响，不能“没触发=无影响”。对照with/without需检查其它差异及judgecriterion，引用源7/27→21/27只能记源作者自述（pin无rawresults），不是我方实证或普遍因果。

pressurecase可测time/sunkcost/伪authority下的边界，但必须区分真实有权新指示与untrusted压力，不能以sourceprocedure永不改当安全。executor权限保证能产生所称artifact/实际观察，工具allowlist/acceptEdits不是sandbox、业务/网络授权或真实独立性。trace按数据处理及custody，fences只降误解释不是完整injection防护；largeinput用stdin等结构化输入避免argv限制，不固定某CLI。executor/grader的时间/失败/未产物/unknown分别记录；schema/id/计数核只证JSON结构/题目绑定，不证grader判断正确；看实际证据与缺口，未知grader_model要保持unknown。

execution和dialogue按交付物/claim选：对话是产物不必硬造fileexecution，声称代码运行不能以美好叙述代；当前文本校正也不每次eval。fixture与source/输出scope需真实路径与隔离/cleanup设计；sourcehelper未认证symlink/网络/凭据全隔离，不搬runner到产品。失败的grading保invalid/raw可恢复和敏感限度，不伪green；不默认删除全部workspaces/proof。采拒绝/接受/defer原因并现有decision-record，不建defaultbranch另ledger或自动commit/push。

**拒绝：**每method3positive/2negative/1behavior、rank95/碰撞0.5或0.75硬门槛、固定≥10turn、free结构永远CI/behavior永不CI、dialogue必须人类豁免、新方法自动正向白名单、tokenmode定义动作权/某SDK/CLI版本当前可用、sourcegrader绿=F独立/生产资格。运行平台按真实need/预算/权限选，不因脚本后缀拒经验，也不为移植完整runner而造validator。

**仍需补读：**runner其余实现/tests、fixtures具体内容、externalplatform当前说明/actualresults未核；本轮只提取上述可判断contract，未执行任何modelcall。source效率/选择率不被gate证实。

## F8 · context与可重启边界：限缩合并

**覆盖：handoff/Charter已fixedinput/实际status/恢复必要claim/sourcepointer和activeconstraints，agent-text已有progressive disclosure。** restartable支持补source贡献，不另contextbudget平台。

落点handoff与agent-text：保实际任务/有效accepteddecisions/本次fixedobject、source与证据ptr、已关/未决/在飞/write状态/下一动作/真实authority；必要事实局部加载，过期draft/噪声压缩保结论与回核位置，不删未理解约束。summary不是第二true-source，相关claim能回原物；新实例先核任务/状态/当前git/diff/对应coverage，继续授权沿真实grant，不要求用户已授权动作重ACK，也不因为previouschat口头未落盘就自动取消有效现session授权。

75%/2000或5000行、freshsession每feature、重要内容必须末尾、全rules永久常驻只是source启发；模型上下文窗口≠能力保证，源lost-in-middle论据未在本任务实验。项目代码/config/tests的字形或仓内路径不自动决定trust/authority，writer/有效指令源才是依据；facts/constraints/假说/外部data分开，不源码正常注释就读成用户命令。冲突/缺product目标返回该owner，low-risk技术可在有效envelope判断，不“任何缺case都human”。重启/崩溃/未停止资源不假completed，process/model选择由真实harness而非方法授予。

**仍需补读：**context实测效应/hostsupervisor未核；不执行restart或配置写入，不把读取原文称收益。

## F9 · checklist / testing支持：原自评被增量证据取代

旧F9仅title层，不可据其“清单面”关闭；本次直接回读performance/security/obs/a11y/checkpatterns与addendum。既有C5/DoD语义充分，C6/C7/C9多数当前已落地；其余机制逐项见 `REVIEW-GATE2-A1-ADDY-EF-ADDENDUM.md`，不凭title/代码后缀整体采或拒，不重新裁Oracle源族。

DoD是项目已接受qualitypolicy与taskcriteria互补；sourcefullruntime/testfirst/humanreview/deployready/固定unchangingbar不成为TPW全域义务。有效owner可修改policy；缺执行/证据按具体claim未核，不“singlegreen=done”。只以现有质量政策方法承载，本文不重新定义责任接受。

## 合法下一动作与残余

Driver可安排F1–6/F8在原owner的实际缺口定向补，F7与Cursor效果评估并同family；不强造九file，coverage已充分者保来源/贡献即可。B需回原文本蒸馏，fixed正文再独立核，source裁定不是运行PASS。README/index/字节核可机械协助，专业coverage/方法效果仍分开。

未逐行读tests/runner全部、evalfixtures、hook/metadata/CI/docs尾部；包T/R索引只作locator，不全149路径资格认证。源示例/法律/平台/version/效益无本轮实证，未网络/业务/SDK/modelexperiment。addendum不可省，A4DEF/DEF2仍未裁；Oracle三包继续排除。review由Driver保全。
