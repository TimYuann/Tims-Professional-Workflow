---
name: adversarial-review
description: "以怀疑驱动的对抗姿态开展独立代码审查，结合 Fowler 坏味道与双轴检验，分栏交付 P0/P1/P2 结构化 Findings。"
version: "1.0.0"
leading-words: ["doubt-driven", "adversarial review", "fresh context", "fowler smells", "P0 P1 P2 findings"]
---

# Adversarial Review · 怀疑驱动对抗性代码审查技能

## 概述
当由独立 Reviewer 对候选代码 Diff 进行审查时调用本技能。融合了 Addy Osmani 的“怀疑驱动”、Matt Pocock 的“双轴审查与 Fowler 坏味道”，以及 Armin Ronacher 的“分栏结论机制”，**以证伪视角审视代码，绝不做廉价的赞美，并精准分级阻断与建议项**。

## 核心操作规程（Process）

### 步骤 1：确立新鲜对抗上下文（Fresh Adversarial Context）
- 必须在完全隔离的干净上下文中运行，不带实现者的主观偏见；
- 假定作者过度自信，重点从以下 5 个脆弱面寻找漏洞：
  1. **边界条件与空值**：输入为极限值、空数组、超长字符串时系统是否优雅降级？
  2. **异步竞态与并发**：多个操作同时到达时是否存在写入争抢？
  3. **错误处理真实性**：捕获异常后是否掩盖了事实？
  4. **状态泄漏与副作用**：函数是否意外修改了外部全局对象？
  5. **安全注入防御**：SQL、Shell、HTML 是否经过严格转义？

### 步骤 2：双轴检验与 Fowler 12 坏味道排查
- **规格轴（Spec Axis）**：实现是否真正满足了初始方案的边界约定？
- **标准与坏味道轴（Standards Axis）**：扫描 Martin Fowler 经典坏味道：
  - *Mysterious Name*（神秘命名）/ *Duplicated Code*（重复代码）
  - *Shotgun Surgery*（霰弹式修改）/ *Divergent Change*（发散式变化）
  - *Feature Envy*（依恋情结）/ *Data Clumps*（数据泥团）
  - *Primitive Obsession*（基本类型偏执）/ *Refused Bequest*（被拒绝的遗赠）

### 步骤 3：结构化分级输出 Findings（分栏交付）
严格区分缺陷的性质，严禁将建议项当作卡死流程的假阳性武器：
- **【P0 - 阻断项（Blocker）】**：
  - 核心逻辑漏洞、契约被破坏、数据损坏风险；
  - 阻断合入，必须打回返工。
- **【P1 - 建议修复项（Actionable Suggestion）】**：
  - 坏味道、命名不清晰、轻微性能冗余；
  - 属于代码质量优化，若时间紧急不阻断本次过夜合入，记录入待办。
- **【P2 - 意图与体验裁决项（Human / Oracle Callout）】**：
  - 代码技术无 Bug，但改变了用户交互直觉或涉及业务取舍；
  - 移交 **Oracle**（过夜）或 **Owner**（晨会）仲裁。

---

## 反借口与典型红线（Common Rationalizations & Red Flags）

| 典型借口 / 行为偏差 | 严厉反驳与纠偏纪律 |
| :--- | :--- |
| “作者通过了全部单测，那代码肯定没问题，给 PASS 吧” | **审查失职！** 审查者要看的正是单测没覆盖到的死角与设计缺陷，不能盲信单测。 |
| “这几行代码虽然写得烂，但能跑就算了” | **杜绝破窗效应！** 必须开出 P1 Finding，指出坏味道类型并给出清晰重构建议。 |
| “我觉得这个变量名不够优雅，定为 P0 阻断合入” | **假阳性滥用职权！** 变量命名不涉及数据破坏的一律划入 P1，不得无端卡停整个波次。 |

---

## 退出判据（Exit Criteria）
- [ ] 完整审查了全部变更文件与核心上下文；
- [ ] 输出清晰分栏的 Findings（包含精确文件行号、失败机理与依据）；
- [ ] 给出确凿的最终 Verdict（存在 P0 则 REJECT，否则 PASS）。
