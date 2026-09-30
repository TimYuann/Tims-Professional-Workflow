# Professional Presets · 选择入口（M1 候选）

本目录存放可复用的专业预设（Professional Profile）。预设是**可缓存的判断配置**，不是职位表，不产生任务决定权，也不自带方法正文。

状态：M1 候选，未经独立验收，未提交。方法入口为候选，待 M4 按来源归位后绑定。

## 选择入口

| 任务主要是 | 先选 | 常配合 |
| --- | --- | --- |
| 把人的诉求变成可理解的问题与目标；与人类对齐取舍 | `intent-voice`（A/Voice） | behavior-domain、technical-planning |
| 说清交付后外部应看到什么；概念、规则与不变量是什么意思 | `behavior-domain`（B/C） | intent-voice、technical-planning |
| 把已接受承诺变成别人能继续依赖的可实施安排 | `technical-planning`（D） | behavior-domain、implementation、evidence-evaluation |
| 在承诺内把结果做出来 | `implementation`（E） | technical-planning、evidence-evaluation |
| 判断哪些约定成立、证据覆盖到哪里 | `evidence-evaluation`（F） | 按被评价对象追溯 B/C/D |
| 识别触发、找对责任方、检查依赖与交接资格、执行关闭 | `driver`（路由入口） | 全部；它不替专业判断 |

选择规则：

- 一次任务可以只调用一个或两个预设；已有适用结论可直接复用，不重做。
- 组合使用时，若权责冲突、真实独立性受损，或注意力跨度损害专业深度（责任基线 §6），拆分实例或补充能力；不以"戴不同的帽子"解决。
- **选择预设 ≠ 授予权限。** 实际责任、范围、输入/输出、工具与独立性由本次 Instance Charter 绑定；Charter 继承实际委托与既有政策，不凭写入"允许"产生权限。

## 预设与判断函数

| 文件 | 判断函数 | 组合说明 |
| --- | --- | --- |
| `intent-voice.md` | A + Voice | 有界组合：问题定义与人类接口 |
| `behavior-domain.md` | B + C | 有界组合：可观察行为与领域语义 |
| `technical-planning.md` | D | 技术/系统规划 |
| `implementation.md` | E | 实现 |
| `evidence-evaluation.md` | F | 验证与证据评价 |
| `driver.md` | Driver | 逻辑路由入口，不属于 A–F |

A–F 是判断函数索引，不是执行序号；不要求六种固定岗位。组合依据为责任基线 §6 的允许组合，是否拆分按真实任务信号决定。

## 选择示例（说明性）

- 局部缺陷修复，已有可恢复行为约定与失败观察：`implementation` + `evidence-evaluation`；F 对本次版本独立取证，E 自测只作可核对输入。
- 新增跨模块 snapshot/freshness 承诺：`technical-planning` 先定协调面，`implementation` 在委派决策内实现，`evidence-evaluation` 对实际版本评价行为与隔离；设计挑战与结果评价可以是不同时点、同一外部实例，按贡献重判独立性。

## 方法绑定状态

"按需方法入口"只写方法需要与候选定位，不含 Skill 正文。方法正文由 M4 重新解析原始来源后决定采用、限缩或蒸馏；在此之前任何入口均为候选，不构成采用结论，也不得假装 Skill 已存在。
