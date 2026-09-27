# investigator · 文档体系 / 角色权限粒度 / 四套方法论 证据调研

**你的角色：调查者。只收集证据与熔炼，不改任何产物。** 你交出的东西要能直接拿给一个高阶 reviewer 做综合判断。

**背景（Owner 的诉求）**：这套 workflow 主打两点——① 优质工程经验；② **自主执行**。而自主执行有一个必须满足的条件：**全程的记录都不能丢**。
现在的实际状态（Owner 判断）：**这个库有"角色 + 交接物"，但没有"文档体系"**——角色之间传纸条传得挺好，**纸条本身没人管**：没规定落在哪、谁保管、活多久、谁维护它不腐烂。
目标是让这套工作流的产物**可溯源、可分析，而不是黑箱**。

**纪律（硬要求）**：
- 每条结论必须给 **`file:line` + 原文摘录**，或给权威外部来源。**不许凭印象写"大概是"**。
- 三仓里没有的，**明说"三仓无此法"**，再给权威外部来源或标"未找到"。
- **不许改任何产物文件**（`roles/**`、`pipeline.md`、`closure.md`、`identity.md`、`SOURCES.md`、`scripts/**`、`README.md`、`AGENTS.md`）。你只读，只写 `.pi/investigation/**`。
- 三仓在 `upstreams/`：`cursor-plugins`（含 pstack）、`mattpocock-skills`、`addyosmani-agent-skills`。**对每个仓做检索之前先看它的 README/目录**，不要猜结构。

---

## 要查的 5 组（一组一节，逐个给证据）

### G1 · 三仓怎么管理"文档与进度记录"
**要回答**：它们有没有正式的文档/记录管理？如果有，**是什么形态、谁写、存在哪、活多久、怎么更新、怎么防止腐烂**。
**线索（不限于）**：report、ticket、plan、spec、ledger、changelog、decision record、issue tracker、progress notes、onboarding doc、`docs/` 目录结构。
**特别关注**：进度是**记在文件里**还是**记在会话里**？谁负责更新？更新频率由什么触发？
**Owner 的原话**：*"我不相信它们完全不管理，至少我那套系统里 report、ticket 这些都是有的。"*

### G2 · `feature map`（pstack 的专项）
**已知起点**（请自己去读原文，不要只用我这几行）：
- 生成器：`upstreams/cursor-plugins/pstack/skills/create-verification-skill/`
- 维护器：`upstreams/cursor-plugins/pstack/skills/maintain-verification-skill/`
- 例子：`skills/create-verification-skill/references/feature-map-example/`
- 导读：`upstreams/cursor-plugins/pstack/docs/guide/06-verify-and-ship.md`
**要回答**：feature map **到底是什么**（结构、字段、四个固定小标题）；**谁产它、谁维护它、什么时候冻结**；**它腐烂了怎么办**；**缺了它会怎样**（原文里似乎有 fail-closed）；它**在项目文档层级里处在哪一层**。
**并且查**：matt 与 addy 两仓有没有**对应物**（例如 spec 文件、checklist、行为清单）。

### G3 · 三仓怎么限制"某个角色能写什么"
**问题来源（真实缺陷）**：我们派活时经常说"**reviewer 禁止写**"——**这太笼统了：禁止写的话，它的报告怎么写？**
**要回答**：三仓里有没有把"不许写"**按类别细分**的做法。至少区分这几类：
- **产品实现代码**
- **自己的交付物/报告**（必须能写）
- **临时探针与实验**（临时空间）
- **共享状态与配置**（谁能改）
- **日志/记录**（只准追加？）
**要回答**：它们**限制角色的权限时用的粒度是什么**，以及**有没有必要限制**——如果某个仓**根本不限制**，那也是有价值的证据，请如实写并说明它的替代机制。

### G4 · 四套开发模式，分别对应我们的哪个角色
**四套**：
- **BDD** = Behavioral Driven Development
- **TDD** = Test Driven Development
- **DDD** = Domain Driven Development
- **SDD** = Spec Driven Development
**要回答**：
1. 每套的**最权威解释与工程 practice**（优先三仓原文；三仓没有的，给权威外部来源，**标明来源**）。
2. 每套**对应我们这 10 个角色里的哪一个或哪几个**（`roles/driver.md`、`oracle.md`、`investigator.md`、`architect.md`、`planner.md`、`implementer.md`、`reviewer.md`、`verifier.md`、`integrator.md`、`ledger-custodian.md`）。**要给出理由，不是贴标签。**
3. 四套之间**有没有重叠或冲突**——如果两套对同一件事给了不同规矩，指出来。
**注意**：本库现有的方法里已经散落着这四套的影子（例如 implementer 的行为先行、architect 的领域建模、spec 类的前置规格）。**你要做的是把它们认出来并归位，而不是新造。**

### G5 · 我们自己现在的缺口（复核我的结论）
我的初判，**请你独立复核并给出你自己的清单**：
- 本仓的交接物有一批名字（`investigation-report`、`design-proposal`、`slice-plan`、`candidate`、`review-verdict`、`verification-evidence`、`ledger-report`、`roundup` 等），**但没规定落在哪、谁保管、活多久**；
- **没有跨角色的文档层级**；
- **没有 feature map 类的东西**；
- **没有 to-do / 进度管理**；
- **没有"哪些算过程性记录必须保全、哪些算工作现场可以丢"的规定**（这条是我认定的根因，请复核它成不成立）。
**方法**：读 `README.md`、`AGENTS.md`、`pipeline.md`、`closure.md` 与十个角色文件，**逐条核实**。

---

## 交付物

1. `.pi/investigation/EVIDENCE.md` —— 逐组证据：`file:line` + 原文摘录；三仓没有的明说
2. `.pi/investigation/SUMMARY.md` —— **熔炼**：这五组合起来，对 **"文档体系该长什么样 / 角色权限该按什么粒度限制 / 四套方法论各归哪个角色"** 给出的答案；并列出**你判断不了、必须交给人或更高阶 reviewer 裁的开放问题**
3. 停机，等我把它交给独立 reviewer 做综合判断。**不要开始设计、不要写方案。**

## 一条范围纪律

这是**吸收**任务，不是**发明**任务。**先找经验、再谈诉求**——三仓有现成做法就照实引；三仓确实没有的，明确说"无"，不要为了让答案好看而自己编一套。
