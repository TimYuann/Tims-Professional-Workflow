# REVIEW-A2R-CURSOR-ABC4

tpw-absorb-gate，2026-10-02。4/4机制组实质裁定：合并MG-1/MG-4，限缩吸收MG-2/MG-3；均有可蒸馏部分，**不是4个新文件或独立增量**。没有因为缺源退整包，不授产品/下游动作权限。

## 固定对象与回源

- 包：`e5b19d486d15161075a40a208455794def75ad3a:docs/absorption/2026-10-02/packages/A2R-CURSOR-ABC4.md`，工作字节blob `0edc0beaf66f728cb48e038bbc2a69430d5b7f73`。
- 源：本地`../legacy-pre-night-2026-10-01/upstreams/cursor-plugins`；本次再次核HEAD=`ecc249f1e306fc64ddf83c7bed16cacf7c2239db`、status无差分。下文源路径均相对此pin。
- 实际整合产品参照：`2158ad2e2ce41184915532535da461aec451e0e0:professional-workflow`，tree `e1114aba1eb8c893e7f52b07a96599ff303cc110`。其方法索引、A/Voice入口与guide-agent-text已直接回读固定字节；三基础方法/Profiles/Charter与冻结Backbone此前已读。包的“21文件”是其旧基线描述，不用作当前数量证明。
- 已裁但未完成消费集成的候选另列：B1@`57b4aad`的guide-professional-explanation、guide-lesson-promotion；B2@`a64bbc2`的professional-learning/human-procedure等。这些只作已审覆盖输入，不能冒称当前已集成。
- 直接回读承重源：`pstack/skills/{bro,unslop,technical-writing,no-comments,automate-me}/SKILL.md`、`pstack/agents/comment-sicko.md`、`cursor-team-kit/skills/deslop/SKILL.md`、`teaching/README.md`与`teaching/skills/{create-learning-path,run-learning-retrospective}/SKILL.md`。bro/unslop本轮前段已读，这次不按重复文件另计增量；workflow-from-chats/reflect已在ABC2直接读。未执行source流程、改技能/个人配置、派agent、访问其他会话或发布。
- **纠正源路径：**MG-4写`pstack/skills/workflow-from-chats/SKILL.md`，pin内实际是`cursor-team-kit/skills/workflow-from-chats/SKILL.md`；已自行核明，不退形式补包。技术写作正文提到的外部Diátaxis/Google/STE/Global English仅为pinned源作者转述，未在本review读取外部规范，不宣称官方规范合规。

我不是包或产品正文作者，仅给机制裁定和消费落点；B固定正文差分另审。产品路径下文相对professional-workflow。

## MG-1 · plain restatement / remove writing noise

**覆盖：部分，且已裁候选覆盖大部。** A/Voice有专业取舍读回、事实/推断/未知与真实接受；当前guide-agent-text有句式负担/单真源/裁剪与证据限制。已审professional-explanation有audience、具体mechanism和逐层说明，不能说“产品没有任何写作标准”。plain restatement与含糊归因/过压缩的具体修复可改善。

**采纳：合并。** bro全文与unslop §Process及Content/Plain speech取：读者看不懂时用平实语言重述同一结论，保原事实、约束、条件与置信程度；删填充/无依据泛泛归因，含推导就明确链条和来源；具体行为/机制优先，保持同一概念命名，完整句子胜解码符号串，形式按实际平行/顺序关系，回看是否改变含义。归并已有解释/文本支持，不新造plain-language并行guide。

**边界：**不继承“Must always apply”、30条/12–15条配额、英文词黑名单、全禁括号/破折号/分号/粗体/被动、每处模糊措辞都删。API名/领域canonical term和合法数学/程序记号不为“去行话”改名；保留物质不确定性，不因“hedging”削掉证据界限。通用但有效的授权/安全/操作原则跨项目也成立，**不能用“换个项目仍成立就删”直接判no-op**。量化只有有真实依据才写，不为更具体编造数字。source author的文风与是否“AI写的”不决定内容正确性或可用性。

**落点（可蒸馏）：**`methods/guide-professional-explanation.md` §Audience/Mechanism/Plain restatement，`methods/guide-agent-text.md` §Pruning/Examples保语义检查；Voice Profile只给相应按需指针。人类文本与agent指令的不同消费需求保留，不把Voice交付改成全套写作检查。

**仍需补读：无承重缺口。** guide10/poteto Writing reply中的未重新读取条款不作为本组新增依据。无真实读者理解或模型行为实验，不报写作收益PASS。

## MG-2 · technical document purpose / ambiguity

**覆盖：部分。** 当前agent-text有steps/reference/progressive disclosure，已审professional-explanation有受众前提与表达形式。tutorial/how-to/reference/explanation的用途分类、条件前置与代词/连接范围消歧，及代码符号/计数时点核实可补。

**采纳：限缩吸收。** technical-writing §Pick the mode/Write sentences/Make statements/Leave no sentence/Voice specifics：先确定读者是在学习、执行、查阅还是理解原因，结构让所需段可发现；操作步骤先说明适用条件/风险和可见结果，代词/only/not/and-or明确所指，用项目真实symbol/path/flag，事实来源与当前固定对象一致；计数/树形声明说明范围/版本，必要时用可恢复命令核回；PR/commit给what/why/影响/证据摘要与链接，不贴无用日志。

**边界：**不采一个文档绝对只能一模式、tutorial不能有必要reference表、method正文不准共置步骤与成立条件，避免与当前核心按需/co-location冲突。按需可分section/链接，只有实际混淆才拆文件。reference也可有真实unknown/限制，**不能为“dry/no hedge”把未证事实写确定**。不引入20/25词、60秒、固定tab/英语时态/serial comma/不准slash等硬门槛；中文按消歧而非英文语法逐条照搬。代码与业务接受规则冲突时显露差异，不以“codebase是词表”让实现改写C。需要固定SHA/小比较表供review的正文可以直接保留，不一律禁止表或SHA而要求读者追链接。

**落点（可蒸馏）：**在共同professional-explanation的Document purpose/Instructions vs evidence/Examples段补四用途与具体歧义对照；agent-text只补可发现性/语义保真，不复制四层检查清单。写变更说明与change-review的Reviewability/inputs互指；无新增独立技术写作平台。

**反例保留：**同一方法文件中操作步骤旁边紧邻前提和例外是正当；“只在X情况下修改Y”与“只修改Y，不处理其他对象”语义不同；已知API字段与接受术语冲突必须说明而不是统一假象。

**仍需补读：**外部规范未核，若B声称官方STE/Diátaxis compliance需另核真正规范；本次只接源作者写作启发可直接蒸馏。opening-a-pr详细流程留ABC6/a4，不能借本组授创建PR/commit/发布权限。

## MG-3 · comments / suppressions / cleanup

**覆盖：scope/保持行为/真实独立性原则已充分，注释约束与suppression诊断操作未充分。** 现行E与local-defect不许可顺手重构，change-review候选已有有证据finding；不缺一个提交前cleanup gate。

**采纳：限缩吸收。** no-comments §Scope/Step 2/5、comment-sicko的keep-list（作为例子）与deslop §Focus/Guardrails里能独立使用的部分：限定被审diff/段落、读附近代码与承重历史查注释声称的why/contract/外部约束，区分重复代码叙述与有信息解释；核suppression对应规则/被隐藏问题/能否以已有类型或验证表达；只有相同约束确实由新carrier兑现、验证支持且动作已授权后才去掉旧提醒；保人在飞编辑与当前行为，真正bug/上层取舍另返回其owner。

**明确拒绝组内默认：**

- 不确定keep就delete；自家代码的surprise一律kill；仅外部且今日live证明的gotcha能留；不获编码批准仍删约束注释；这些会丢不可从代码推导的业务/安全/历史理由。unknown先保全、指出缺证，不“默认删”制造正确。
- `MUST KILL`标签/固定两次重跑/mandatory Comment Sicko或architect/how/why调用、全评论非作者清理。作者可作局部self-clean；若交独立F评价按实际贡献分开，不因style请求强加新instance。
- safety/correctness suppression一律去掉、内部defensive check异常即删、显然bug即可跨本次cleanup权限修。合法`@ts-expect-error`负向类型测试就是反例；类型不足以证明运行时authorization/时间性约束已安全。source“不加symptom guard”按真实契约核，不全禁必要guards。

**归属：**代码可读性/注释取舍通常为E/D的Maintainability concern，F核证；public doc comment若影响外部行为语义才涉及B/C，不把所有comment变成人类冻结面。

**落点（可蒸馏）：**`methods/change-review.md` §Relevant lenses/Comment and suppression evidence放只读判断；`methods/guide-lesson-promotion.md` §Choose carrier放constraint可表达才编码，复用check-design验证实际carrier；必要一个短按需`guide-comment-and-cleanup.md`仅当E需要完整编辑操作时再独立，不在所有Profile内联“keep/kill清单”。优先共同正文，避免新universal cleanup method。

**区分例子：**废弃的重复算法叙述可在授权内删；“不得重试charge，因为远端可能已成功”内部调用理由若没被可证明dedup机制兑现不能删；API contract/licence/合法negative-type test各有不同依据，不按后缀机械定罪。

**仍需补读：无所取机制缺口。** 相关hook/runtime未执行、不接受其freshness/自主cleanup/guardrail安全能力。对read-only review不要把source的actual删改流程说成已经运行。

## MG-4 · personal guidance / learning feedback

**覆盖：偏好置信与carrier选择已在ABC2裁定/lesson-promotion候选，大部分已有；显式professional-learning候选已有目标/练习/能力证据，teaching两小正文是同用途补充。**

**采纳：合并，分两个既有owner carrier。** automate-me §Existing/History/Ask/Guardrails取更新优先于重建、核已有指令的有效版本与后续纠正、保未被推翻的约束、只新增确有差异的section、引用共享方法不复制内容、不强求形式对称、实际需要才补目标化澄清。归lesson-promotion。teaching两SKILL取已完成工作对目标、查弱概念/阻断、调整练习与下一可测里程碑，补professional-learning §Evidence/feedback，**不是另建课程/学习责任节点**。

**对A自评的独立判断：**不因teaching文字薄或“学习不在A–F”就整体拒绝；A3-DEF10已限缩到任务明确包含专业学习/传授时的实际能力。两文没补充复杂独特执行机制，故只作同family的反馈补强/来源，不算独立知识增量。普通工程任务不自动转learning任务，不由本方法创造新目标。

**边界：**不继承2+切片自动高置信、单次显式偏好必需重复才有效、当前权威纠正与旧情境不同就当noise。同一事件被复制到多个transcript不是独立证据；有效最新指示/范围可覆盖旧偏好，冲突查实际authority。无默认2–4周/三agent/4–6选项/固定questioncount、全私人目录递归读取、强制`-mode`格式/工具/metadata/PR。subjective风格可由真实owner读回，仍可验证结构/触发/禁止事项；不采“mode主观所以benchmark永不适用”。既有明确更新授权不再逐section索ACK，未授权长期组织规则不能靠confidence升格；用户尚未要求常驻应用时不默认全任务激活。

**落点（可蒸馏）：**lesson-promotion §Update an existing carrier/Scope/conflicts、agent-text的按需/不重复已覆盖不再复制；professional-learning §Review demonstrated progress补适应练习。Voice方法入口按真实需要指向已有共同方法，Driver只管理依赖而不裁定用户偏好或发明长期authority。

**仍需补读：无机制缺口。** plugin metadata无新增工程行为未作为运行资格读取；任何实际历史挖掘/个人skill写入/持续学习workspace另受其任务权限，本review未执行。

## 可蒸馏批次、合法下一动作与残余

| 批次 | 机制/落点 | 不重复计数 |
| --- | --- | --- |
| 人类与技术表达 | MG-1/2→professional-explanation；agent-text只补指针/语义检查 | 与A3 ABC8/DEF11、Cursor ABC2 MG4共一family |
| 评论与cleanup | MG-3→change-review判断+lesson/check carrier；仅必要时短E支持 | 不引入Comment Sicko gate，不复制通用ownership |
| 偏好与学习反馈 | MG-4→lesson-promotion/professional-learning各自段 | 与workflow-from-chats/reflect/continual-learning、A3 DEF10共享来源family |

Driver可按这些已完整裁定机制安排作者定向补当前共同正文；共享文件互斥写面并串行整合。我不直接派B或写正文。完成后我审固定落地差分，旧已通过条款不全量重审。读者可理解/误读减少等效果未实验，无PASS收益。四组范围处置完成，不认证全cursor863路径、外部规范或尚未审ABC3/5–8及a4尾部。
