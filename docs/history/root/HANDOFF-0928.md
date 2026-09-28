# 交接书 · TPW 修复推进

**交出方**：TPW repair（原 `subagent-chat-01a0e33d`，workspace w26/pane w26:p2）
**接收方**：`tpw-driver-0928`（workspace w26/pane w26:p3）
**交接时间**：2026-09-28
**仓库**：`/Users/yuantian/Developer/tim-professional-workflow`
**当前版本**：`v2.0.5`（commit 见 `git log --oneline -1`）

---

## 一、这个项目是什么

`TIM Professional Workflow` —— 一套**与工具无关**的工程工作流内核：
9 个角色、50 个技能、23 条原则、7 个阶段 + 3 条横切带、9 类产物、2 个检查脚本 + 2 个生成/记账脚本。

**要解决的真实问题**（判断做得好不好的唯一标尺）：
多 agent 编排（DAG、并发、消息收发）已经够用了，**缺的是工程经验**——
agent 反复犯那些「只要有更高阶工程经验就能避免」的错误。
本库把这些经验提炼成可按任务体量动态装配的内核。**它不做调度。**

**Owner 已明确**：下一个阶段在 UCBIP 上做真实试运行，**开全部 agent（full size）**。
所以「小任务要几个文件」「solo 档怎么设计」这些**本轮不用再管**。

## 二、走到哪了

| 版本 | 内容 | 检查 |
|---|---|---|
| v2.0.0 | 从第一性原理重建：唯一真源 `workflow/registry.yaml` + 机器可证闭包 | 13 项 |
| v2.0.1 | 一审 FAIL(53/100) 后的修复：假链接、角色技能表、5 个 checker bug、A9 身份四件套、并发锁 | 21 项 |
| v2.0.2 | 逐个读完全部 50 技能。产物收敛为「9 类 + 落盘形态 + 工作副产品」三层 | 26 项 |
| v2.0.3 | 模拟走查抓出的 P5→P6 断链 + 判档循环 + A9 无判据 + P6 越权 | 26 项 |
| v2.0.4/5 | 二审 FAIL(60/100) 阻断项：干净 clone 可跑、VERSION 对齐 tag、身份字段进工作合同、C13 改显式声明 | 24 项 |

**当前状态**：24 项检查（17 closure + 7 consistency）全绿；
`render.py --check` 12 个派生文件逐字一致；21 条故障注入 21/21 变红；
**`git clone --branch v2.0.5` 到空目录后 17/17 + 7/7 全绿**（这一条在 v2.0.1–v2.0.3 是完全跑不起来的）。

## 三、两份独立报告在哪

| 报告 | 谁写的 | 结论 |
|---|---|---|
| `.pi/review-v2/REPORT-tpw-verify.md`（550 行） | tpw-verify（GPT-5.6 Sol xhigh）一审 | FAIL 53/100 |
| `.pi/review-v2/REPORT-round2-tpw-verify2.md`（323 行） | tpw-verify2 同上，二审 | FAIL 60/100 |
| `.pi/map/lineage.md` + `artifact-arrows.md` + `simulation.md` + `lineage.mmd` + `artifact-arrows.mmd` | tpw-map（DeepSeek V4.1 Flash · think:max · 1M） | 血���图 / 96 条产出箭头 / P0→P6 走查 |
| `.pi/map/_v2.0.1-full/` | tpw-map 建的冻结快照 | 复核用，逐行可对照 |

**先读 tpw-verify2 的报告再动手。** 它是最新且最狠的一份。

## 四、接下来要做的事（按优先级）

### P0 · 二审指出但本轮没修的

1. **`frontend-ui-engineering` 没有真正吸收。**
   现在只抽走了无障碍一小段，上游还有 component architecture、state management、
   design system adherence、responsive、loading/empty/error states、UI finish gate 全都丢了。
   被并进 `security-and-hardening` 这个归并**不成立**——界面工程不是安全加固。
   处置：要么单独成为 P5 验证侧的一个技能，要么明确 rejected 并写清理由。

2. **`definition-of-done` 的概念混淆。**
   上游明确区分「项目固定的 DoD」与「每任务的 acceptance criteria」，
   本库把两者塞进了同一个 `A4.done_definition`。
   注意：`constraint-driven-development` 已经产出了一份仓库根目录的质量契约文件——
   **那其实就是项目级 DoD，只是没在注册表里这么叫。** 建议把「项目级质量契约」显式认成
   `A4` 的一个**项目级形态**（和 ADR、词汇表一样是 embodiment，不是新编号），
   并在 `A4.done_definition` 的 notes 里写清它与项目级契约的分工。

3. **两处技能来源段与 registry 对不上。**
   `skills/tdd.md` 的来源段只列 Matt+pstack，registry 三个（含 Addy）；
   `skills/context-reconstruction.md` 多列了 `pstack:recall`。
   **C9 只核 registry 的 sources 是否存在，不核技能文件自己的来源段**——这是已知漏洞。

4. **角色与脚本没有来源字段。**
   Owner 的要求是「每一段话有来源」，目前只做到 skill/principle 级。
   registry 的 sources 不覆盖 `roles/` 与 `scripts/`。

### P1 · 检查器里被点名的「假检查」

`tpw-verify2` 逐条给了 15 个会全绿的反例，结论是 **21 项里只有 6 项可按声明信任**
（C2/C6/C8/C9/C12/S6）。被点名的：

- **C3** 只按 YAML 列表顺序查，不算图可达性 → 塞一个孤立的 P7 能过
- **C4** 未被正则识别的字段引用被静默忽略 → 写 `A8.GHOST` 能过
- **C5** 只核 registry 指认，不核角色正文的产物字段
- **C7**（旧版）按 basename 折叠、不查 actual 重复 —— **已在 v2.0.5 改成对锁文件核对，但「同一上游被两个本库技能认领」仍不报**
- **C10** 名字叫「双向」但只查处置→目标；来源出现在第二个错误目标不报
- **C11** 只查 consumers→required_inputs，**反向不查**（tag 自带的 A6/P6 就是错的对）
- **D1** 排除 docs、大小写敏感、有限黑名单；`scripts/ledger.sh` 里的 `HERDR_AGENT` 就没被抓到
- **S1** 只 `glob("*.md")` 一层，嵌套目录全漏
- **S2** 遇 fragment 的死链整条不匹配
- **S3** 同一句里的精确冲突也漏（只取第一个 polarity）
- **S4** 不读角色正文，只机械判冲突 —— 是假检查
- **S5** 未知 output 取到 producer=None 就放过
- **S7** 不校验 `applies_to` 的 id，不查孤儿横切带

**处理方式建议**：逐条决定是「加断言」还是「改名把范围缩到名实相符」。
**改名比假装覆盖更诚实**——这一版已经在 S3 上这么做了一次，效果不错。

### P2 · 口径差异待对齐

`tpw-map` 报「登记表外产物 54 种」，本库的口径是「落盘形态不算新产物，9 类就够」。
两边数量对不上，**需要你裁定哪个口径为准**，或者给出第三条。
`tpw-map` 的箭头表 `.pi/map/artifact-arrows.md` 里有 96 条 file:line 级证据，是现成的输入。

## 五、必须继承的硬边界（任何档位都不放宽）

1. **提出候选的人不得给这个候选下结论。**（`P4`/`P5` 各一条硬规则）
2. **不得为让检查变绿而削弱检查。**
3. **验证三态**：`PASS` / `FAIL` / `UNVERIFIED`。环境故障既不算 PASS，也不判成产品缺陷。
4. **`A9` 台账只追加。**
5. **工具解耦**：库内容不出现任何具体运行底座名称（`D1` 守着）。

## 六、这个项目反复犯的同一个病（务必警惕）

**「声明了，但没人产出。」**

已经犯过三次，每次都是同一个形状：
- v2.0.0：处置表说 6 条 skill 被吸收，但目标技能的 `sources` 里根本没有它
- v2.0.1：给 `A6`/`A8` 加了 `subject`/`scope`/`frame_alignment`，但没告诉任何人谁填
  → `P5` 判据永远无法满足 → `P6` 要 PASS → **链断在 P5→P6**
- v2.0.3：`roles/scribe.md` 还在教 4 栏台账，v2.0.1 加的身份四栏从没进角色文件

**每加一个字段、一个产物、一个检查项，先问一句：谁填？在哪个文件里写？**
现在由 `C15` 守着判据引用的字段，**但只覆盖判据引用到的**。
新加东西时请顺手把产出方那条也改了——`roles/*.md` 与 `skills/*.md` 才是 agent 真正照着工作的合同，
registry 只是元数据。

## 七、怎么跑检查

```bash
python3 scripts/check-closure.py      # 17 项，图通不通
python3 scripts/check-consistency.py  #  7 项，文件之间打不打架
python3 scripts/render.py            # 改了注册表后重新生成派生视图
python3 scripts/render.py --check    # 核对派生视图
python3 scripts/sync-upstreams.sh     # 重新生成 upstreams.lock.yaml（改了上游吸收才需要）
```

**C1 会要求 `VERSION` 与当前 tag 对齐**——发版流程是：改 `VERSION` → 改 `registry.version`
→ commit → 打同号 tag。反过来做会被 C1 当场抓住。

**改完东西务必跑一次故障注入**：造一条真实故障，看检查器会不会红。
不会红就说明那个检查是摆设——这已经栽过两次了。

## 八、角色分工建议（本轮已开好的 session）

| session | 模型 | 建议职责 |
|---|---|---|
| `tpw-driver-0928` | MiniMax-M3.1-Flash-Preview 512K | 你自己。判档、派发、收口、对外汇报 |
| `tpw-investigator-0928` | 同上 | P0-1/2/3/4 与 P2 口径差异的取证；读上游正文 |
| `tpw-impl-0928` | 同上 | P1 假检查的逐条处理（加断言 or 改名） |
| `tpw-verify-0928` | 同上 | 独立复审。**不得参与实现**（硬边界 1） |
| `tpw-scribe-0928` | 同上 | 决策台账；把每轮结论记进 `A9` |
| `tpw-voice-0928` | 同上 | 对 Owner 的单一汇报面 |
| `tpw-oracle-0928` | **GPT-6 Sol · think:xhigh · 828k** | 裁决。**由 driver 持有**，别人不直接找它 |

## 九、交接时没做完的

- 我改过 `~/.pi/agent/models.json` 与 `settings.json`（MiniMax-M3.1-Flash-Preview 上下文 1M→512K，
  reserveTokens 320k→160k，maxTokens 524288→131072），**原文件已留 `.bak-<时间戳>` 备份**。
- w22 工作区里 8 个 v1 时代的 agent（tpw-driver / repair-1 / tim-investigator /
  tim-investigator-b / tpw-verify / tpw-verify2 / tpw-map 等）全部 idle，交接时会关闭。
  它们的会话记录仍在 `~/.pi/agent/sessions/--Users-yuantian-Developer-tim-professional-workflow--/`，
  报告已落盘在 `.pi/` 下，不会丢。
