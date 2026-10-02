# REVIEW-B1-LATEST-f321c8c

tpw-absorb-gate，2026-10-02。固定完整对象：`d3aab6ad30f36789664287f304e4e91ffd61d96a..f321c8c72f6c1cb4bddcf32ef00f628b53d29c45`，branch absorb/w1。**整笔：需修。** 第一批原R1已关闭；第二批旧4项仍存在，新增prototype证据分类及handoff恢复搜索相关差分需定向修。

核验：固定diff全文件清单20项、`375b40c..f321c8c`九文件增量；用git show补读全部新增guide及之前diff截断正文，git diff --check通过。复用已审不变对象，不把工作区新字节算修复。直接补核cursor pin `ecc249f1…` 的continual-learning memory updater、bro、unslop、guide08对本次新引用的对应原文；此前A3/Cursor/Addy reviews的承重源不全重读。实际贡献仍只是review，没有正文代写。

## 仍开与新增阻断（一次列清，避免重复循环）

| ID | 固定对象位置 | 当前问题 / 最小修要求 |
| --- | --- | --- |
| R1（原batch2） | `methods/handoff-and-resume.md:15`，表L19–25、L27；新§Reconstruct/shared-record bullet | 仍称handoff必选五grades、live可trust as shipped、unit非UI即可/所有UI需live；receiver不会recheck。改为源观察方式例子，不强制类型或UI分类分配结论，按claim/对象/真实执行/覆盖/独立性判定，未知旧pass不假造运行类型。新恢复段又规定named feature必须shared-record sweep、不是judgment call；改为在当前scope/必要claim缺依据时取所需来源，已给完整capsule可复用，记录未查范围，不能自授默认全扫。原已正确baseline复用/红acted custody不改。 |
| R2（原batch2） | `methods/domain-state-and-invariants.md:20` | D/E被一并限为不改变coordination surface。分清D在有效envelope内决定/修订共享技术方案，E在承诺内选局部表示，B/C改变与越界才走相应返回。 |
| R3（原batch2） | `methods/verification-harness-design.md:44`、L57及§Use | 保留source-clean也required live/每feature至少一次，与Limits/裁定不一致；comparison又称唯一claim/threshold/verdict owner。按本次受影响features/claims/recipes维护；需要真实leg才真实驱动，harness变更重驱对应recipe；只有委托本就全featureaudit才全跑。comparison只是适用时的路径，不能取代B/C/任务policy/F设计。 |
| R4（原batch2） | `methods/change-review.md:57`–64 | 作者有context即defer，review可无independent但不区分selfcheck/F要求；跨轴永不排序硬禁、follow-up至多一次被写普遍规则。作者信息供核、决定看有效authority；独立F按Charter真实贡献，自查标自查；Spec/Standards不抵消且保未解来源，工作安排可按实际影响；来源咨询次数不新增额度gate。 |
| R5（新，Oracle提疑后回源成立） | `methods/bounded-prototype.md` §Evidence limits“Prototype evidence is not production evidence … does not prove … performance under real data” | 标签不能预设实际输入/运行时全是合成，也不能预设无法测真实data条件下的窄claim。改为按实际输入、运行环境、真实/替身依赖和观察范围说明证据。保留prototype不等于生产实现交付/发布，控制输入的局部结果不证生产全域。无须放开额外网络/数据权限。 |

R1–R4在f321c8c上核仍存在（新commit只追加批次内容，没有这些旧修订），不把新actor/commit视作对象重置。复查只关注上述句子/表及直接依赖，无新普遍validator/gate或多agent流程。

## Prototype回源依据与反例

cursor `pstack/skills/poteto-mode/playbooks/prototype.md` §1/3/5–6把prototype定义为解决具体问题的throwaway instrument，可用最小脚本测behavior/timing，并未限定输入必须合成。Matt `skills/engineering/prototype/SKILL.md` §Rules 3允许为持久化问题使用scratch DB；`prototype/UI.md` §Sub-shape A保留现有data fetching/auth。这些是本轮已直接读的原文，支持“用途/交付成熟度”与“证据来源/覆盖”分开。

反例：获授权的隔离原型实际调用固定版本SDK读取一份真实记录，可证明该版本/该输入上的读取及mapping观察；不能仅因prototype名降成synthetic，也不能据此证明部署、所有输入或规模性能。若全用fixture，则仅支持fixture条件下的claim。R5由证据判断成立，不因Oracle一句疑问自造mustfix。

## 可立即采用的通过部分（固定文件对象，不等于整笔通过）

下列在f321c8c对应的**整文件字节PASS**，包括其已审新增差分：

- `methods/test-first-behavior-slice.md`
- `methods/guide-test-evidence-quality.md`
- `methods/change-slicing.md`
- `methods/design-alternatives.md`
- `methods/cross-module-design.md`
- `methods/behavior-claim-evaluation.md`
- `methods/decision-record.md`（含轨迹段）
- `methods/domain-language.md`
- `methods/guide-change-shape.md`
- `methods/guide-lesson-promotion.md`
- `methods/guide-professional-explanation.md`
- `methods/local-defect-feedback-loop.md`
- `profiles/implementation.md`
- `profiles/evidence-evaluation.md`（与B2指针串行合并后再核）
- `profiles/technical-planning.md`

这些文件指向的已通过目标在candidate内存在，方法的操作/反例与条件有源支持，未见新权限/固定门槛。scope/proportionality按任务委托调用，不因存在建议就强制新平台。guide-lesson的机制排序有detectability/false-positive/cost限定；无需复制源的CI/metadata机制。其未完整落地的DEF12/check设计知识不冒称本次已具运行checker。

Driver若选择串行集成这些文件，应固定实际整合commit，核方法选择README的needs/按需入口和状态声明、共享F Profile两方指针及相对引用。**不能整笔cherry-pick f321c8c；**五个需修文件不在以上PASS列表。此范围是可review的已审文件对象，不是新的权限白名单或长期整合规则。方法正文的能力与本次动作授权仍分开。

消费依赖补充：上表PASS指正文专业内容；`guide-change-shape.md`消费引用`bounded-prototype.md`，`guide-professional-explanation.md`消费引用`handoff-and-resume.md`，两目标尚需修。这两guide须与目标通过后的对象一起集成，或暂留待集成，不能留下断链/指向未接受正文。其余13文件及B2已列3方法可组成当前最小通过切片，仍需在Driver实际整合对象核引用和选择入口；不是要求造依赖checker。

未执行真实工程/SDK/模型效果实验，不将源启发当效果PASS。正式候选的修复由原作者作，我只审新/受影响claim。
