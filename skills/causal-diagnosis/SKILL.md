---
name: causal-diagnosis
description: "构建 10 种确定性反馈回路，生成可证伪假设，对重复失败坚决质疑共同前提，杜绝打补丁式修 Bug。"
version: "1.0.0"
leading-words: ["deterministic feedback loop", "attack the premise", "root cause", "falsifiable hypothesis", "no band-aids"]
---

# Causal Diagnosis · 因果诊断与根因归因技能

## 概述
当排查复杂系统缺陷、时序竞态或性能退化时调用本技能。融合了 Matt Pocock 的 10 种确定性反馈回路构建法与 `pstack` 的“质疑共同前提（Attack the Premise）”硬纪律，**把诊断的核心转化为构建一个高频、可自动运行的 Pass/Fail 信号，杜绝加 `if (x == null)` 掩盖崩溃的治标做法**。

## 核心操作规程（Process）

### 步骤 1：构建确定性反馈回路（Build the Feedback Loop）
**这是诊断的 90% 所在。没有确定性反馈，任何代码修改都是盲人摸象。**
根据场景在以下 10 种工具中挑出一种，构建一个 Agent 可一键反复运行的脚本：
1. **Failing Unit/Integration Test**（最优先）
2. **Curl / HTTP 专用复现脚本**
3. **带真实 Fixture 的 CLI 驱动命令**
4. **无头浏览器端到端脚本（Headless Browser Trace）**
5. **Replay 回放捕获的真实日志或请求流量**
6. **抛弃型最小复现脚手架（Throwaway Harness）**
7. **属性/模糊测试（Fuzz / Property-based Loop）**
8. **Git 二分定位脚本（Bisection Harness）**
9. **差分比对循环（Differential Loop，新旧版本输出比对）**
10. **HITL 人机交互排查循环模板（`hitl-loop.template.sh`）**

### 步骤 2：生成可证伪假设并排队（Ranked Falsifiable Hypotheses）
- 提出 2–3 个合理的竞争性解释；
- 每个假设必须回答：**“如果该假设成立，我们在哪里加探针应该看到什么？如果不成立，又会看到什么？”**
- 按验证成本由低到高，用最小探针逐一实验并排除。

### 步骤 3：连续两次失败必须质疑共同前提（Attack the Premise）
- **绝不在死胡同里撞墙**：
  - 如果基于假设 X 的前两次修复尝试都未能通过验证门禁；
  - **严禁提出基于假设 X 的第三个补丁！**
  - 必须倒推停下来，做一次前提普查：这两个失败的方案共享了哪一个尚未经证实的底层前提？推翻该前提，重新归因！

### 步骤 4：追溯至真正根因（Fix Root Causes, Resist Band-Aids）
- 严禁在崩溃发生的最后一行随手加一个判空来消灭报错；
- 必须问五次为什么（Five Whys），追溯非法数据到底是从哪个入口灌入的，把根因修在源头。

---

## 反借口与典型红线（Common Rationalizations & Red Flags）

| 典型借口 / 行为偏差 | 严厉反驳与纠偏纪律 |
| :--- | :--- |
| “我加了一个 `if (!obj) return;` 之后控制台不报错了，说明修好了” | **治标不治本！** 你只是把崩溃压制了，导致系统带着静默的脏状态继续运行，必须找出为什么 `obj` 会是空的！ |
| “复现太麻烦了，我直接看代码猜一个改动试试看吧” | **禁止盲猜！** 先花时间建立确定性反馈回路，这是唯一能向 Reviewer 和 Verifier 证明你修对的方法。 |
| “这次修没过，那我换个变量名再提交一次同类补丁” | **触发质疑前提纪律！** 连续两次失败必须推翻假设，严禁在错误前提下重复打补丁。 |

---

## 退出判据（Exit Criteria）
- [ ] 拥有一个可被命令行重复执行的确定性复现测试/脚本；
- [ ] 排除竞争性解释，锁定真实的源头缺陷位置。
