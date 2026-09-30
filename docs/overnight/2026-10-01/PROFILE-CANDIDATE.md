# M1 · Professional Profile 候选报告

状态：**候选**，未提交、未验收。作者：`tpw-night-profile`（Pi / commandcode / deepseek-v4.1-flash / max）。
写入范围：`professional-workflow/profiles/` 与本文；其余路径只读。未执行 commit，未作出任何"已接受"声明。
本文是作者自述与自查记录，**不构成独立评价**；独立评价、修订与集成由 Driver 安排。作者自查只检查了结构、边界表述与旧内容残留，验收下一手仍是独立实例。

## 1. 依据（已完整读入）

- `docs/overnight/2026-10-01/BOOTSTRAP.md`：委托、写入与通信纪律、首轮推进。
- `docs/OVERNIGHT-WORKFLOW-PLAN-2026-10-01.md`：§2 delegation envelope、§4 写入可逆性、§5 M1 标准。
- `docs/RESPONSIBILITY-BACKBONE.md` 设计基线 1：§2 短接口、§3 A–F 责任、§4 Voice/Driver、§5 四类边界检验、§6 实例组合与最短调用。
- `docs/WORKFLOW-INTENT.md`：上层意图与本轮术语。

未作为设计输入：旧 `roles/`、`principles/`、`skills/`、`workflow/registry.yaml`、旧检查器与历史；未复制旧 skills 正文。未做外部来源核读：本批心智模型来自冻结基线的责任区分；方法正文按 M1/M4 分工留给 M4 按来源重新解析。

## 2. 实际文件

共 7 个文件、309 行（不含本报告），全部在 `professional-workflow/profiles/`：

| 文件 | 行数 | 判断函数 | 一句话 |
| --- | --- | --- | --- |
| `README.md` | 44 | 选择入口 | 选择表、组合说明、绑定状态 |
| `intent-voice.md` | 42 | A + Voice | 诉求 → 可继续的问题定义；人类接口与接受记录 |
| `behavior-domain.md` | 49 | B + C | 可观察行为约定与领域语义 |
| `technical-planning.md` | 45 | D | 接受承诺 → 可实施的协调安排 |
| `implementation.md` | 41 | E | 承诺内实现并发现事实 |
| `evidence-evaluation.md` | 43 | F | 对象/版本上的证据判断与三态 |
| `driver.md` | 45 | Driver | 触发、路由、程序足够性、召回与关闭执行 |

每个预设固定五块：心智模型、关键问题、常见误区、交接与召回、按需方法入口（候选）。文件中不含权限清单、工具清单、注册表、检查器或 Skill 正文。

## 3. 责任覆盖

| 判断/接口 | 覆盖位置 | 负责 | 明确不拥有 |
| --- | --- | --- | --- |
| A Intent/Outcome | `intent-voice` | 问题定义、目标/非目标、事实-推断-未知区分 | Owner 的目标与价值取舍 |
| Voice | `intent-voice` | envelope 对齐、读回、取舍翻译、接受记录 | 冻结 C/D、替 Owner 接受风险或扩大授权 |
| B | `behavior-domain` | 可观察行为、场景/异常/接受条件 | A 的目标、C 的业务语义 |
| C | `behavior-domain` | 概念、规则、不变量、上下文边界 | 实现选择；未获委托的业务规则 |
| D | `technical-planning` | 协调面、方案、委派决策、召回去向 | B/C 决定权、政策/预算/人类保留边界 |
| E | `implementation` | 承诺内实现、局部选择、自测事实 | 静默改写承诺、自证结论、扩权 |
| F | `evidence-evaluation` | 验证设计、观察、三态、覆盖与独立性 | 改预期、接受剩余风险、授予关闭/发布 |
| Driver | `driver` | 触发、路由、程序足够性、依赖/召回/关闭执行 | 实质专业裁定、runtime 机制、默认人类接口 |

组合说明：A+Voice、B+C 按 Backbone §6 的有界组合；B/C 的组合失效信号写在该文件内。`driver` 是调用入口（判断函数之外的路由角色），不是第七个判断，也不是固定岗位。

## 4. 选型取舍

做的：

1. 先 D/E/F 三份，再以 A/Voice、B/C 两个有界组合与 Driver 入口补齐完整启动路径；6 份预设覆盖 A–F + Voice + Driver，不设六个固定岗位。
2. 每份开头一句绑定声明：选用预设不获得任务授权；实际责任、范围、输入/输出、工具与独立性由 Instance Charter 绑定。预设只提供心智模型、误区与方法入口。
3. 误区写成具体可错的事（如"多改模块=需重新申请""自测绿=正确依据""改预期宣布成功""程序齐全=实质足够"），不写泛化资历、不携带每任务全历史。
4. 召回按 Backbone 的共用返回路线表述（回到受影响判断、经 Driver 路由、越界找对应 authority），不发明 gate；B/C 只写一条 §6 已有的组合失效信号，未为每个边界加防御条文。
5. README 给选择表 + 两个说明性选择示例，回答"未参与设计者如何选到接近配置"。

不做的（负空间）：

- 不造固定岗位目录、执行序号或六阶段；README 明说可只选一两个预设、可复用已有适用结论。
- 不造 registry/schema/validator/frontmatter 权限字段：M1 明确"不为此制造 schema validator"；职责绑定交 M2 Charter。
- 不内联 Skill：按需方法入口只写"需要什么方法 + 候选状态"，不含方法正文。
- 不写 M2 的 Charter 模板、M4 的来源结论、M5 的包入口与集成；这些留给 Driver 与后继里程碑。
- 不复制旧职责正文，不使用旧编号/旧检查作为本轮依据。

取舍代价：6 份的最小性、组合拆分的判定门槛、Driver 是否应独立成文件，均由独立评价与 M3 真实案例检验；若出现注意力或召回问题，按 §6 拆分，而不是加 gate。

## 5. 同一 Profile 的两个不同 Charter（说明）

目的：证明预设不偷带任务授权。用 M3 计划的两类委托作为两套 Charter 骨架；**M2 才定 Charter 模板**，本节是说明性绑定，不是正式 Charter。同一 `implementation` 预设：

| 维度 | Charter A：局部缺陷修复 | Charter B：新增跨模块 snapshot/freshness 承诺 |
| --- | --- | --- |
| 对象 | 已有可恢复行为的私有函数与失败观察 | 跨模块 snapshot 绑定与 freshness 协调面 |
| 责任来源 | 缺陷报告 + 仓库既有行为约定与测试依据 | 已接受的 B/C 版本 + D 的 Plan |
| 输入 | 复现观察、现有测试依据 | Commitments / Delegated Decisions / Recall Conditions |
| 权限边界 | Charter 绑定：仅实现内部，对象禁令明确 | Charter 绑定：委派决策范围内；共享接口不得自改 |
| 独立性 | F 对本次版本独立取证；E 自测只作输入 | 设计挑战与结果评价可由同一外部实例分时点完成，按贡献重判独立性 |
| 召回对象 | 输入语义不清/需改调用者/输出承诺无法保持 → B/D | 需自改读 head/改 snapshot 绑定/复制 freshness 责任/改失配行为 → D/C/B |
| Profile 贡献 | 心智模型、关键问题、误区、方法入口 | 同左，完全相同 |

同一 `evidence-evaluation` 预设：

| 维度 | Charter A | Charter B |
| --- | --- | --- |
| 对象与 claim | 修复后局部实现版本；既有约定是否恢复、负控制是否有效 | 跨模块承诺的实现版本；行为兑现 + 隔离/恢复等适用要求的观察 |
| 依据 | 已有契约与失败观察 | B/C 接受版本 + D 约束 |
| 独立性 | 不得是该候选的实现者 | 不得是实现者；设计挑战与结果评价的关系分别如实记录 |
| 召回 | 依据冲突 → B/C/D；实现违规 → E；环境阻断记 UNVERIFIED | 同上 |

两次使用中 Profile 完全相同，而对象、责任来源、权限边界、输入、独立性关系与召回对象都随 Charter 变化。预设没有携带对象许可、接受权或工具许可。

## 6. 最少未定点

1. **Charter 模板与字段**：M2（Driver）定稿；本候选只给绑定关系说明。
2. **方法入口绑定**：M4 按原始来源重新解析后决定采用/限缩/蒸馏；当前全部为候选，无方法正文。
3. **组合拆分判定**：A+Voice、B+C 是否需在真实案例中拆开，以及 Driver 入口的文件形态，待 M3 信号与 Driver 集成决定。
4. **独立性/三态记录载体**：由 M2/M5 集成时定义；本候选只要求如实记录真实独立关系与 PASS/FAIL/UNVERIFIED。
5. **本候选的独立评价**：尚未发生；作者自查不是验收。

## 7. 请独立评价关注的断言

- 未参与设计者仅凭 README 能否为两类 M3 任务选到接近预设，并理解"选择 ≠ 授权"。
- 每份的误区与召回是否具体、可操作、无自创 mandatory trigger/gate/风险接受条款。
- §5 的两-Charter 说明是否足以证明预设不夹带对象或权限。
- 是否存在旧角色/旧方法正文、每任务携带的历史、无任务依据的防御条文。
- 三态与真实独立性是否未被削弱；独立性不可得或能力降级时是否仍如实披露且不产生新授权。

## 8. 修订记录

### M1-B1（2026-10-01）

- 来源：`docs/overnight/2026-10-01/PROFILE-EVALUATION.md` 定向 finding M1-B1；请求：`tpw-night-driver`。
- 改动：仅 `professional-workflow/profiles/driver.md` 第 37 行"召回"表述。原先把"越界、保留项或需人类决定"统一送 Voice；现改为越界/保留项**先返回实际拥有该判断/边界的 authority**（专业、风险、资源保留权不默认属于人类），**仅人类保留决定或需人类决定时经 Voice**。
- 未改：其余 6 份预设与 README 未动；未新增 gate/节点/文件；三态与独立性表述未变。
- SHA-256（driver.md）：`b61dcbd483ec96ac117cb1cbbfd5da2d684013c528c2602c439aff58118a833b`（评价所记旧值）→ `8a2f42c874ca08c94b06e20131623178f5a45bc6b7d419a3a8fb7ce1651be399`。
- 状态：仍为候选，未 commit、未验收；完成后停下，待 `tpw-night-method` 差分复核。
