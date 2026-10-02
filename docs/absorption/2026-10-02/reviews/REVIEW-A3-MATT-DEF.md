# REVIEW-A3-MATT-DEF

tpw-absorb-gate，2026-10-02。14/14机制实质裁定：合并DEF-1/2/5/6/9/11/12/13/14（9），限缩吸收DEF-3/4/7/8/10（5）。不是14个新文件或独立增量；按下述落点可蒸馏，不是正式正文/运行/集成接受。

对象：包`docs/absorption/2026-10-02/packages/A3-MATT-DEF.md`读取blob `b0b3b7afb0d657285f56bb9239d03070e387c342`；产品基线`800414dd9eb517f7132223866fe484d28a8bbf0b:professional-workflow`/tree `7c814e54c5e775045bc1c5155e3c181ceb1345fb`。源Matt pin `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`，本轮已核clean/HEAD。下文源路径相对pin，产品路径相对professional-workflow。

直接回读承重源：`skills/engineering/{diagnosing-bugs,code-review,improve-codebase-architecture,wayfinder,prototype,research,wizard,resolving-merge-conflicts}/SKILL.md`（批量wayfinder截断中段另补Map/Tickets）；prototype `LOGIC.md/UI.md`；wizard `template.sh`具体ask/write/secret/finish与函数入口；`skills/productivity/{handoff,teach}/SKILL.md`、teach的MISSION/RESOURCES/LEARNING-RECORD formats；`skills/in-progress/{retro,writing-beats,writing-shape,writing-fragments,setup-ts-deep-modules}/SKILL.md`及后者config；`skills/misc/{git-guardrails-claude-code,setup-pre-commit}/SKILL.md`与block-dangerous-git脚本；`scripts/sync-plugin-version.mjs`、`link-skills.sh`。code-review/setup-ts/link已在ABC直接读过不重读。未执行；未把source内部派agent/改工具/安装/发布指令当本任务授权。产品相关正文直接回核与前四份裁定一致。

## 逐机制

### DEF-1 · diagnosis

覆盖：local-defect和redacted guide已充分覆盖基本loop/hypothesis/正确seam，tightness、非确定失败的采样/最小化停止点可改善。**合并**：取diagnosing-bugs §Tighten/Non-deterministic/Minimise/Instrument/Cleanup，最小可靠区分观察、测复现频率与条件、一次删一负载并重跑、已证原因与清理临时probe归纳。新落点只在local-defect §Method 2–5/必要按需诊断支持，不复制六phase或十阶梯全流程。

边界：无3–5hypotheses/秒数/50%/100次/每剩余元素必一一证明/先向Owner展示假说/无red命令绝不推理gate。不能因1%低频放弃诊断；运行成本、采样与统计证据足够即可。压力/sleeps可改变现象要注明，raw secrets仍按既有custody；清理只动自身授权临时物，不销毁承重证据。无“tight loop必找根因/90%已修”收益承诺。补读：无所取机制缺口，未执行HITL模板。

### DEF-2 · two axes

覆盖：F独立性/版本已有，change-review候选已吸收多lens和处置。**合并**：取code-review §Pin/Spec/Standards/Aggregate/Why two axes；清楚固定比较对象，引用适用标准与Spec，各轴证据/缺口独立保留，smells是有标签启发、repo有效约束优先。无spec就记缺失，不从实现造spec。

三方向张力正式裁定：可采用分别阅读后合成处置，合成不得以Standards通过抵消Spec失败或反之。各轴未解决项持续可见；同一缺陷可去重带双来源。实际严重性和blocking由有效规则/authority判断，可为工作安排排序；**不吸收全局禁止跨轴优先级**，也不强制同题两contexts或固定两个agent。是否fresh如实列接触与贡献，独立性不能由标签数量证明。三点diff看merge-base且不含working/staged，若审当前未提交对象须明确追加差分，不能用“HEAD审过”覆盖未审工作。空diff是无变化不必称failure；坏ref不得继续猜。无直到clean反复review、报告verbatim即可靠、no-tool-enforced就不审相关语义。落点共同change-review §Object/axes/disposition，与AB G3、Cursor MG-6同正文。补读：无承重缺口；源docs field reports未复验。

### DEF-3 · architecture survey

覆盖：D有接口/复杂度方法，候选没有系统普查操作。**限缩吸收**：improve-codebase §Explore/Present/Candidate strength与rejection，先定痛点、结合变更历史找高价值维护面，具体friction→受影响对象→候选收益/代价/证据强度，允许“无有依据候选”。提案不改代码；拒绝原因并decision-record，不另建拒绝台账。

边界：频繁修改不必然坏架构，少改可能关键风险，历史作线索非排序定律。deletion启发遵ABC薄安全wrapper例外；不默认deepening/人类grilling/每session一candidate/HTML/CDN/OS-temp或必须产出finding。落点按需`methods/architecture-survey.md` §Scope/evidence/candidates，D入口。补读：HTML scaffold未核不导入；无运行效果。

### DEF-4 · planning under uncertainty

覆盖：Plan三面/依赖/召回已有；已知问题与尚不可表述未知的区分、低分辨索引可改善。**限缩吸收**：wayfinder §Map/Fog/Destination，bounded destination先定，精确但blocked的问题作为问题；尚不能形成问题的是in-scope uncertainty，目标外另列；依赖满足再展开、结果owner文档一处维护，地图只引用。无雾可直接用已有Plan，不强建map。

边界：不是tracker/ticket/100k上下文/一个session一ticket/全HITL工序；claim/assignee不是原子锁保证（a4处理实现）。可编辑Notes不能自授执行权，accepted delegation才是权源。发现更大目标回A/Owner实际authority，不自动删旧ticket或广泛发布。落点`methods/uncertainty-planning.md` §Destination、Known questions/unknowns、Dependencies/update、Handoff；与elicitation/change-slicing互指。补读：无机制缺口，tracker模板/真实阻塞API未验证。

### DEF-5 · prototype

覆盖：Cursor prototype与elicitation已有裁定；逻辑自由探索/有序walkthrough及证据保留补强。**合并**：prototype+LOGIC/UI的一个问题先明示、面向决定者的state/actions/scenarios、同条件可切换实质差异variant、记录选择/观察及可恢复artifact。进入正式实现前重新满足产品合同与验证，prototype不因可lift就成为production-qualified。

边界：HTML/email仅是可运行可分享载体例子，不强制栈/变体数/无测试/无错误处理/真实数据。source一处让代码靠近产品、一处隔离，按任务已有安全空间，不把变体带生产；可丢弃不意味着必须销毁，需证据保留按custody/约定。无默认commit throwaway branch/自动清理旧原型。落点共同bounded-prototype §Question/state/scenarios/capture，互指domain-state/elicitation。补读：无。

### DEF-6 · research

覆盖：A事实区别、source固定与rationale候选已有，技术fact的版本/保质期可补。**合并**research正文的primary-owner来源、逐claim可核引用、实际scope/unknown、repo现有位置与消费指针，进入rationale-and-premise-review/按需`guide-source-evidence.md`。facts与decisions分开；facts也可能需要长期证据，decision不必只能grilling。

边界：无background-agent强制/禁止所有delegation/只要primary就可信/一文件硬格式/任务后自动archive-delete。查询需要相应访问；只核必要主张，记录版本/时点、变化失效条件与二手信息边界。源码事实不是作者意图；已读引用再恢复承重原义，不只信摘要。补读：源12行够本次范围，外网/真实研究未执行。

### DEF-7 · human-only procedure

覆盖：redacted guide有HITL操作/安全证据，交互程序的值流/固定helper结构未覆盖。**限缩吸收**wizard §Scope/Map/Author/Verify 的环境声明中找必需值、不读出真实secret；每值来源/写入destination/sensitivity三问、stage按真实步骤且不发明UI、动作授权/确认、静态syntax+scope/value trace与首run未验证声明。固定helpers和实例stage分开可作为设计例子。

边界：本轮不安装/复制bash库或发布CI secrets；普通可执行步骤不推给人。source helper并不证明安全：write_env直写KEY=value、吞read EOF、缺gh仍显示Setup complete；若使用需核key/value编码、permissions/partial/EOF与实际目标，不能默认原库never-edit或100%正确/无secret入模型。纯静态检查不等于e2e有效。无自动读取全部.env值、固定TTL/delete脚本/重复setup必须commit。落点`methods/guide-human-procedure.md` §When manual、Value/action trace、Artifact verification、Partial/limits，复用redacted custody。补读：如B要提供runnable helper需另核完整库与target，当前方法可蒸馏。

### DEF-8 · merge/rebase

覆盖：preserve user changes/契约有原则，具体冲突处理未覆盖。**限缩吸收**resolving-merge-conflicts五步：核真实进行状态/基点/双方diff与原始意图，保双方有效承诺，冲突不能仅选ours/theirs，必要取舍返owner，集成后发现并跑本仓有用checks再报告状态。

边界：拒绝never-abort、stage everything、alwayscontinue/rewrite、作者自然有merge许可或“zoning不值得”。git merge/rebase/historical change需真实授权，保恢复点、只stage自身；缺意图或上层冲突先保全不发明行为。结构共享写面可预防碰撞，无改好模型足够保证。落点`methods/merge-conflict-resolution.md` §State/intent/resolve/check/return，与handoff指针。补读：无；未执行merge。

### DEF-9 · portability

覆盖：已裁AddyG4/CursorMG7/8的artifact-first与证据状态充分，portable/fork例子可补。**合并**handoff正文reference/redact/focus与已读phase-boundary取舍：已有owner产物指针+未落盘的在飞状态，目标reader真实可取，brief不能建第二契约。不同工具/地点/人员/旁支fork是有用触发例，不穷尽所有场景。

边界：不默认OS-temp为唯一持久地点、summary是真authority、fork继承可直接授权/无需复验、只能travels才留note、永远只带what不why。needed why条件/例外引用可恢复且不可因短而丢。落点共同handoff-and-resume §Portability/fork；认领/调度运行不在此。补读：claude-handoff包装未核，不接受其启动能力。

### DEF-10 · learning evidence

覆盖：C术语/agent文本及Cursor理解型teach部分，持续能力训练/覆盖≠掌握未覆盖。**限缩吸收**teach §Mission/Knowledge/Skills/Learning records：明确专业能力目标/已知程度和成功观察，解释时减不必要负担、练习时用与目标相关的检索/反馈/实践，记录实际展示能力、声称先验水平、纠正和目标变更分别标来源，reference与lesson角色分开，复用已有组件避免副本。

边界：仅在**任务明确包含专业技能学习/传授**时调用，不新增所有工程任务教学前置；不要求固定workspace/files/课程/assessment gate、默认社区加入、parametric知识全不可信、每quiz等长字符或自动推算真实长期掌握。难度反转是源教学启发，未核实验科学收益；单次答对不证长期retention，自述prior knowledge不作demonstrated。Cursor解释不quiz与此能力训练quiz按目标相容，不二选一。落点按需`methods/guide-professional-learning.md` §Goal/knowledge/practice/evidence/limits，与professional-explanation互指。补读：已有source足够，不需退；未读glossary模板已在ABC处理，不重复增量。

### DEF-11 · drafting

覆盖：agent文本/专业解释/语义术语已有，读者前提与实时文档合作可补。**合并**writing-beats/shape/fragments的读者已有/正文新引概念区分、素材不等于最终论证、缺例子不虚构、parallel内容可list/同字段可table、读盘保护人类在飞编辑，只修改被授权段。归guide-professional-explanation §Ground concepts/choose form和guide-agent-text §Co-editing。

边界：无文学workflow作为全工程默认、每段必须Owner选择/append、原材料永不允许编辑（用户明确编辑授权可改）、固定2–3opening/三次同形必table/必须coin术语。accepted与candidate材料分清，不强制全pile展开。补读：三个SKILL已直接读，暂无缺口；未测试文章效果。

### DEF-12 · classify recurring failure

覆盖：lesson-promotion/库维护部分已有，mechanical-vs-judgment、已有check unwired的具体信号补强。**合并**retro §Automated checks/Coding standards/Files：先查本仓check/lint/CI是否已可执行、重复有明确语法模式可考虑最便宜确定性check，不可机械判断留专业证据/反例，按需pointer。

边界：不接受无CI一律finding、mechanical必建checker、F“无需exploration因此独占standards”、E只实现不持约束、所有固定规则都能无误编译化。标准owner/授权继承，新增hook/访问权限/CI有成本/动作边界。本轮只写参考，不建工具。落点lesson-promotion §Classify与下组guide-check-design；没有独立retro框架。补读：无；sourcecontext压力只是论证、无当前实测。

### DEF-13 · prove the guardrail

覆盖：F负控制原则/mockguide有基础，mechanical checker真实pass-fail-pass与配置保全未充分操作化。**合并**setup-ts §Prove rules bite、git-guardrails §Merge/Verify与script、setup-pre-commit §Adapt/Verify，合DEF12的check-design：现有配置合并不覆盖，用scratch/可恢复对象作clean pass→有代表性违例特定诊断fail→撤违例pass，核实际入口而非配置存在，便宜检查先、说明漏抓什么。

边界：不复制TS文件形状/regexhook/常驻CI/framework；源script对字符串regex可绕过、jq/parser失败无安全保证，不能当security authority或权限边界。原config实际五forbidden entries不是包称四error rules；避免继承误计。负控制可按风险有用，不每知识点强建fixture；missing check依委托声明未验证。staged工具可能mutation，只改自身已授权对象。落点`methods/guide-check-design.md` §Existing entry/negative control/configuration/limitations；F/E/D按需引用。补读：migrate-to-shoehorn/scaffold-exercises等工具literal实施不在本次采纳，若拟运行需相应回读与授权。

### DEF-14 · drift check / wrong target refusal

覆盖：source identity/单写已具原则，命令mode的check-vs-mutate与目标验证补强。**合并**sync-plugin-version与link-skills代码：真源与consumer明确，check只报告差异/非零不写；write保格式范围并验证生成内容，目标解析异常不继续写，说明筛选范围/例外。归guide-check-design §Drift/write modes/targets，与Cursor共享写面/a4原子写区分。

纠错：sync脚本在writeFileSync**前**JSON.parse(updated)检查，不是包称post-write readback assertion。它不证明落盘后的字节/原子性；需要readback属于作者新增要求应标明。link脚本只有DEST symlink into repo防护，不能认定所有危险目标安全，且会rm-rf现有非symlink目录；不移植其删除权限/运行实例。two-artifact一致不证明全consumer同步。补读：无当前模式缺口；未运行脚本。

## 可蒸馏归并与分母

统一落点：local-defect（DEF1）；change-review（DEF2）；architecture-survey（DEF3）；uncertainty-planning（DEF4）；bounded-prototype（DEF5）；source-evidence/rationale（DEF6）；human-procedure（DEF7）；merge-conflict-resolution（DEF8）；handoff-and-resume（DEF9）；professional-learning（DEF10）；professional-explanation/agent-text（DEF11）；lesson-promotion+check-design（DEF12–14）。Source pins及关键sections须正文可查，Profile仅指针；Driver管写面，不把该表变发布/任务固定序列。

ABC联动：MG-6拒绝record只一份；MG-8文本/DEF11共享表达规则；MG-3测试oracle与DEF13checker negative control共用理念但各保具体操作。**不将“证据必须能变红”归约到历史置信五档**：Unknown是调查结果，不是失效检测；可核历史引用、统计区间/直接行为反例有不同证据依据。保条件、别把口号当统一框架。

包给169=59+44−2+68的记账较前“37 paths”有解释，仍不代表我已逐资产/metadata/CI精核；本review接受的是14机制处置，不全仓运行/完成资格。Source支持docs field reports、额外临床/学习效果和被引issue未独立复验。没有代写B正文、部署或下游授权；下一步只审真实固定落地差分。
