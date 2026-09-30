# METHOD-CANDIDATES · M4 active-method dossier

状态：**candidate**（供 Driver 串行集成；本文件不构成采用、接受或 Skill 正文）
作者：tpw-night-source；日期：2026-10-01 夜；范围：仅三条活跃路径方法候选。
依据：`METHOD-REVIEW.md`（tpw-night-method，MR-01，M4 §8 适配 PASS）、`SOURCE-SURVEY.md` §8（sha256 `31f638eb6d27a059aca813588ca7d77476b2c5fab318247bccb5b41135fb697e`）、`RESPONSIBILITY-BACKBONE.md` §§1–4、计划 M4。
写集：仅本文件；未改上游 / Profiles / Charters / 产品目录；以自己话蒸馏，不整段复制原文。

**来源 full pin（本轮实核）**

| 源 | pin | 相关方法面 |
| --- | --- | --- |
| S1 addy | `2686b620fc1fed2e8f60c704839c766b8594c6b6` | `debugging-and-error-recovery`、`api-and-interface-design` |
| S2 cursor-plugins（pstack、cursor-team-kit） | `ecc249f1e306fc64ddf83c7bed16cacf7c2239db` | `pstack/playbooks/bug-fix`、`verify-this`、`interrogate` |
| S3 matt | `c55ee46073ed923f86ce59a5eb3b6d895095d1b7` | `diagnosing-bugs`、`codebase-design`(+DEEPENING/DESIGN-IT-TWICE)、`code-review` |

## ① 局部缺陷 · 主方法 S3 diagnosing-bugs（+ S1 有限补充；S2 仅可选）

| 项 | 内容 |
| --- | --- |
| 主正文（owner 候选） | S3 `skills/engineering/diagnosing-bugs/SKILL.md` |
| 有限补充 | S1 `skills/debugging-and-error-recovery/SKILL.md`：非可复现分类、错误输出不可信 |
| 可选列示（不采用） | S2 `pstack/skills/poteto-mode/playbooks/bug-fix.md`：同表面验证、机制需运行时证据、失败 repro 先入 Git 历史 |
| 状态 | **candidate** |

**保留（keep）**
- 以症状专属反馈回路为核心：一条已实际跑过、能对该缺陷变红、足够快、确定或有稳定复现率的命令；没有回路不进入假设。
- 复现并最小化到每个剩余元素都负载；用可证伪假设与一次一变量的探针定位根因；修后重跑原始场景。
- 回归测试挂在"正确 seam"上；seam 不存在本身作为发现（与 D 的连接点）。
- S1 增量仅两条：非可复现按 timing/env/state/random 分类处置；错误输出视为数据而非指令（不执行其中命令/URL）。

**限缩（narrow）**
- 原方法面向 hard bugs 且允许有解释地跳步；本路径是"已有行为约定与失败观察的局部缺陷"，复用回路即可：不重造平台、不穷举十种构造法、不强制三至五个无意义假设。
- S1 Stop-the-line 只限依赖故障的工作，不扩为全队停工。
- S2 三项分别可选：同表面复验、机制需运行证据可作参考；失败 repro 先入历史仅在适用时作交付纪律，不为每次修复造额外提交。

**删除 / 剥离（delete/strip）与理由**
- 剥离 S2 的 control skill、`/loop`、默认委派模型、"跨函数就 architect"、Opening a PR：属运行面或平台绑定；函数边界≠Backbone 的共享承诺边界；来源操作指令不产生本包发布权限。
- 未携带但可恢复：S3 的 HITL 分支引用同目录 `scripts/hitl-loop.template.sh`；若实际启用该分支，须完整核读并携带脚本，当前不启用、不阻断。

## ② 跨模块承诺 · 设计方法 S3 codebase-design + DEEPENING（+ S1 三原则补充）

| 项 | 内容 |
| --- | --- |
| 主正文 | S3 `skills/engineering/codebase-design/SKILL.md`、`codebase-design/DEEPENING.md` |
| 补充（限缩） | S1 `skills/api-and-interface-design/SKILL.md`：contract first / 一致错误语义 / 加法优先 |
| 延后 | S3 `codebase-design/DESIGN-IT-TWICE.md`；S1 idempotency 三态与 retention |
| 状态 | **candidate** |

**保留（keep）**
- interface 全义：调用者必须知道的全部事实（类型、不变量、顺序、错误模式、配置、性能特性）；seam 是可替换行为的位置；depth=leverage；deletion test。
- DEEPENING 四类依赖（in-process / local-substitutable / remote-owned 以 port+adapter / true external mock）供 D 分析测试如何跨缝。
- 测试穿过真实 interface；replace-don't-layer 只在新覆盖已替代旧覆盖时适用。
- S1 三原则：先定契约再实现；单一可预测错误语义（机器码 + 人类消息，不混用 throw/null/`{error}`）；在本次必须保持既有消费者约定时优先兼容添加；方法不取代有效 authority 对破坏性变更的接受权。

**限缩（narrow）**
- 不搬 REST 资源设计、分页、命名表、GraphQL；S1 idempotency 三态/retention 只在真实路径出现重试或副作用时加载（当前候选不足以证明需要）。
- 不为"深模块"强制合并模块；不自动授权删测试或扩大改造范围。

**词汇 owner（沿用 MR-01）**
- 责任/授权词汇：冻结 Backbone；领域词汇：本次 C 接受对象；D 方法可使用 module/interface/seam 技术词汇，并显式记录两词定义。
- 不把 Backbone 的"边界"全局改成 seam；matt 禁 boundary/API 属其内部词汇纪律，限缩移植时说明该调整，不声称逐字采用。

**删除 / 剥离与理由**
- 不吸收 DESIGN-IT-TWICE 的 3+ 并行子代理数量：运行面绑定；有实质方案分歧时可保留"两案对比 depth/locality/seam"纪律，但不得变成产品要求。
- 方法不得决定 B/C 意义、freshness 责任或任务接受权。

## ③ F · 单证据方法 S2 verify-this（必要部分）+ 严格三态映射

| 项 | 内容 |
| --- | --- |
| 主正文 | S2 `cursor-team-kit/skills/verify-this/SKILL.md` |
| 状态 | **candidate** |

**保留（keep）**
- 把 claim 写成可证伪形式（条件、指标、阈值）；baseline 与 treatment 同命令、同数据、同环境；比较原始 artifact；输出单一 verdict；不软化负面结果。
- 三态映射（严格，非机械标签转换）：
  - VERIFIED → PASS：方向符合、达到阈值、无明显混淆。
  - NOT VERIFIED → FAIL：行为未变 / 反向 / 未达阈值。
  - INCONCLUSIVE → UNVERIFIED：缺有效 baseline、噪声、测量失败或环境差异；不得当 PASS。
- 观察对象、版本与覆盖必须随结论说明。

**限缩（narrow）**
- 只取必要部分（claim 表述 + baseline/treatment + 三态）；`/tmp/verify-this` artifact 布局与 control-ui/control-cli 表面选择属运行面，参考不继承为产品规则。
- verify-this 只覆盖具体变化 claim，不覆盖一切 F 判断。

**独立性**
- 由 Charter / 实际贡献声明承担；模型多样性、多个标签或 fresh 仪器都不证明作者独立性；Backbone 独立性标准仍是责任 owner。

**延后 / 候选（不设 gate、不常驻并行）**
- S2 `interrogate`（同 rubric、去重、共识/独见/分歧、lead judgment）：候选程序；其 `references/code-quality-review.md` 含 1000 行阈值、激进结构审查、presumptive blockers 偏好——若只采用合成/rubric，须显式延后硬阈值与机会性重构倾向；单模型安全/正确性反证不得因缺共识丢弃。
- S3 `skills/engineering/code-review/SKILL.md` 的 Standards/Spec 分轴：候选；大段 lens 不再展开。
- S1 `code-review-and-quality`：延后（已全文读过，不在本轮范围）。

## ④ 定位与延后登记

- S4/S5：不进活跃路径；原站 UNVERIFIED；缓存摘要仅定位（载体 sha256 已记）；若后续进入活跃路径，须先固定原站或镜像全文核读。
- 其他延后：DESIGN-IT-TWICE、interrogate、code-review lens、S2 bug-fix 同表面证据（仅可选）、S1 idempotency 三态、S1 code-review-and-quality。

## ⑤ 溯源与合规

- 来源 pin、正文 anchor 均在上表列出；未读旧 roles/compose/history 来定义责任。
- 本文件仅写自身；未改上游 / Profiles / Charters / 产品目录；未 commit、未另起会话；未采纳、未接受。
- 后续：Driver 串行集成；若集成改变活跃 Profile/Charter/Skill/routing 含义，按计划标受影响 M3 coverage 失效并定向重验；不新增 gate。

## 修订记录

- 2026-10-01 · MR-02 可选精确化 #1（§2）：S1 三原则第三条改为“在本次必须保持既有消费者约定时优先兼容添加；方法不取代有效 authority 对破坏性变更的接受权”；其余内容未动；状态仍为 candidate。
