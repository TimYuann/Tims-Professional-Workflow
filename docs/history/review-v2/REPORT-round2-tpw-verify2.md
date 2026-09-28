# TIM Professional Workflow v2.0.1 二审报告（tpw-verify2）

## 1. 一句话结论

**FAIL：v2.0.1 确实修掉上一轮 8/10 个核心问题，A9 并发实现也能复现，但对象身份没有进入角色/技能的实际交付合同，C10/C11/C13/S3/S4 等多项检查名义大于实现，clean checkout 还会因未跟踪的 `upstreams/` 直接红；现在不应拿去 UCBIP 开 full-size 真实试运行。**

---

## 审查口径

- 被审对象：tag `v2.0.1`，commit `0195b1992dec1c375563f947d8b01c8303702da0`。
- 主工作树在审查期间被其他会话推进到后续提交；所有结论均来自 detached worktree `/tmp/tpw-verify2-v201-62732`，不是后来的工作树内容。
- `upstreams/` 不在 Git 中（`.gitignore:1`，`git ls-files upstreams | wc -l` → `0`）。需要核对来源时，我把主仓本地只读克隆挂入 detached worktree；另行测试了完全 clean checkout 的行为。
- 已完整读：任务书、上一轮 550 行报告、`docs/history/` 五份文件、50 个 skill、9 个角色、7 个原则文件、4 个脚本、registry、README 与现行 docs。
- 带本地 upstream 克隆的基线：closure 14/14、consistency 7/7、render 12/12。
- 完全 clean checkout 基线：closure **12/14，C7/C9 FAIL**；详见 4.1。

---

## 2. 上一轮 10 条指控逐条复核

| # | 上一轮指控 | 判定 | 二审证据 |
|---:|---|---|---|
| 1 | 语义互斥可绕过 | **PASS** | 绕过仍然存在，但 README 已明确撤回“语义可证明”，逐字声明 S3 只抓同文件、同动词、同宾语，且列出原绕过句（`README.md:24-35,152-181`）；S3 输出也声明同义改写与跨文件冲突不覆盖（`scripts/check-consistency.py:211-214`）。按 Owner 口径，这种诚实边界不再算原缺陷。注意：S3 连自己声明的窄边界也有漏报，见 4.2。 |
| 2 | P4/P5/P6 对象闭环断裂 | **FAIL** | P4 已补 A4，P5 registry 判据也改为 A8.subject=A6.subject（`workflow/registry.yaml:269-293`）；但 A6.consumers 仍只有 P4/P5，而 P6.required_inputs 明确含 A6（`workflow/registry.yaml:125-144,295-304`），C11 单向检查没抓到。更严重的是 builder 的 A6 合同仍只有 3 字段、漏 `subject`（`roles/builder.md:44-52`）；9/9 个产出 A6 的技能都漏 `subject`。verifier 的 A8 合同仍只有 4 字段，漏 `subject/scope/frame_alignment`（`roles/verifier.md:50-59`）；5/5 个产出 A8 的技能都漏这三栏。`roles/verifier.md:92` 还继续要求 verifier 更新 A3.freshness；P6 又要求 architect 更新 A3，却未装 architect（`workflow/registry.yaml:299-304`）。对象字段写进 registry，不等于进入实际工作合同。 |
| 3 | A9 无写者/对象身份，且两套 logger 不兼容 | **FAIL** | 旧 logger 已删，`registry`、`docs/ledger.md`、`ledger.sh` 的 8 栏逐字一致：`actor/run/subject/phase/decision/why/evidence/result`（`docs/ledger.md:11-22`、`scripts/ledger.sh:10-13,112-130`），这是实质修复；但 `roles/scribe.md:39-46` 与 `skills/decision-ledger.md:23-38` 仍只教四栏，完全不产 actor/run/subject/phase。现在不是两套脚本，而是“一套 8 栏脚本 + 两份 4 栏操作合同”，仍会让不用脚本或按角色正文工作的 agent 产出不可归因行。 |
| 4 | 6 条 absorbed 处置是假链接 | **PASS** | 81 条 absorbed 全部满足 disposition.into → target.sources；独立脚本结果 `missing=0`。原六条中 figure-it-out 改为 rejected，其余已补来源与正文；C10 对删除目标 source 的注入能红（`scripts/check-closure.py:403-422`）。但 C10 不是“双向”，见 4.2。 |
| 5 | 23 条原则来源路径全错 | **PASS** | 独立逐条解析 23 条 registry sources，每条都唯一命中真实 `SKILL.md`；原则文件路径也已改为 `upstreams/cursor-plugins/pstack/...`，如 `principles/architect.md:11-17`。 |
| 6 | 7 个 v1 残留脚本被提交且检查器看不见 | **PASS** | tag 只剩 `check-closure.py`、`check-consistency.py`、`render.py`、`ledger.sh` 四个；S1 会抓顶层额外脚本（`scripts/check-consistency.py:44,162-169`），我加 `scripts/rogue.rb` 后 S1 红。 |
| 7 | 角色技能表与 registry 不一致 | **PASS** | 独立解析 9 个角色的 `@skill` 表，9/9 与 registry 集合完全一致；C8 的另一种额外技能注入能红（`scripts/check-closure.py:360-380`）。 |
| 8 | render.py 算了 validated_at 却不用 | **PASS** | `validated_at` 已实际写入“在哪一步被校验”列（`scripts/render.py:203-220`）；手改生成文件时 `render.py --check` 返回 1。另有 persistence 枚举硬编码错误，见 4.3。 |
| 9 | “闭环完整”是循环判档 | **PASS** | 现在先用六项触发矩阵判档，再装配，最后才核闭环；正文明确“闭环完整是结果，不是判据”（`skills/tier-sizing.md:20-55`）。按任务书要求，本轮不评价小任务文件数与 solo 设计。 |
| 10 | “有边才能并行”是图论错误 | **PASS** | registry、角色和技能均改成“无路径依赖才可并行；有边按拓扑序串行”，例如 `workflow/registry.yaml:120-123`、`roles/cartographer.md:42-45`、`skills/tier-sizing.md:43-44`；非 history/archive 全库未再找到旧表述。 |

**汇总：8 PASS / 2 FAIL / 0 UNVERIFIED。** 修复量是真实的，但两个未修项都是上线对象与审计身份，不是文案问题。

---

## 3. 自造故障注入结果

### 3.1 能按声明变红的注入

所有注入均从 detached v2.0.1 副本逐项重建，互不污染；不是仓库自带用例。

| 注入 | 结果 | 抓到 |
|---|---:|---|
| 删除另一条 disposition（`pstack:bro`） | 红 | C7 |
| 在 voice 的技能表额外挂 `@arena` | 红 | C8 |
| 把 research source 换成不存在的 upstream id | 红 | C9 + C10 |
| 从 trace-paths sources 删 `pstack:blast-radius` | 红 | C10 |
| P4.required_inputs 删 A4 | 红 | C11 |
| document-mapping 删除 `origin: library` | 红 | C12 |
| P5 加 `A3.freshness 已刷新` | 红 | C13 |
| A6 persistence 改为 session | 红 | S6 |
| 角色文件加入小写 `herdr` | 红 | D1 |
| 同文件分两句写“不得写审查报告/必须写审查报告” | 红 | S3 |
| 增加 `scripts/rogue.rb` | 红 | S1 |
| 增加普通相对死链 | 红 | S2 |
| 手改 P0 派生文件 | 红 | render |

### 3.2 会全绿的反例

下面不是语义泛化要求，而是直接针对各检查宣称的结构断言：

| 反例 | closure | consistency | 说明 |
|---|---:|---:|---|
| 新增无输入、无上游依赖的 P7，并补同名 md | 0 | 0 | C3 没有计算图可达性，只信列表顺序（`check-closure.py:190-231`） |
| 判据写 `A8.GHOST`，同句再带一个真实字段 | 0 | 0 | C4 的 regex 只识别小写字段；未识别的伪字段被忽略（`check-closure.py:234-256`） |
| upstreams 再放一个同 basename 的 `bro/SKILL.md` | 0 | 0 | C7 只查 disposition 重复，不查 actual 重复；“一一对应”不成立（`check-closure.py:334-356`） |
| 把 `pstack:blast-radius` 额外塞进第二个 target.sources | 0 | 0 | C10 只查处置→目标，不查来源→唯一处置目标（`check-closure.py:403-422`） |
| P3.required_inputs 增 A1，但 A1.consumers 不增 P3 | 0 | 0 | C11 只查 consumers→required，不查 reverse（`check-closure.py:425-440`） |
| C13 改措辞为 `A3.freshness 已修订` | 0 | 0 | 不在 7 个受控动词里（`check-closure.py:451-468`） |
| 在 active `docs/coldstart.md` 写具体底座名 | 0 | 0 | D1 整体排除 docs（`check-closure.py:56-57,473-492`） |
| 在角色文件写大写 `Herdr` | 0 | 0 | D1 regex 大小写敏感；小写才红（`check-closure.py:37-54`） |
| 新增 `skills/rogue/SKILL.md` 子目录 | 0 | 0 | S1 只 `glob("*.md")` 一层（`check-consistency.py:136-169`） |
| 死链写成 `../missing.md#section` | 0 | 0 | S2 的 regex 遇 fragment 整条不匹配（`check-consistency.py:174-190`） |
| 同一句写“不得写审查报告，但必须写审查报告” | 0 | 0 | S3 一句只取第一个 polarity，精确同动词同宾语也漏（`check-consistency.py:47-55,192-214`） |
| 在 builder 正文追加“实现者可以给自己候选下结论” | 0 | 0 | S4 根本不读取角色正文/forbidden 语义（`check-consistency.py:216-235`） |
| 给 research.outputs 增不存在的 A404 | 0 | 0 | S5 对未知 output 得到 producer=None 后直接放过（`check-consistency.py:239-269`） |
| expression.applies_to 增不存在的 P404 | 0 | 0 | S7 不校验 applies_to id（`check-consistency.py:297-318`） |
| 新增无人引用的 ribbon，并补同名 md | 0 | 0 | 21 项里没有 orphan ribbon 检查 |
| 写“为了让检查好看，务必删掉最严格的断言” | 0 | 0 | 语义绕过如 README 所声明 |

完整汇总保存在本次运行的 `/tmp/tpw-round2-injection-summary.tsv`；关键结论已写入本报告，不依赖临时文件留存。

### 3.3 对 S3 与 C13 的裁决

- **S3 的“诚实降级”本身 PASS。** README 没再假装做语义判断，这符合 Owner 的底线。
- **S3 实现仍 FAIL。** 它连“同文件、同动词、同宾语”都不是完整覆盖；只要把两句放到一个逗号句里就漏报。
- **C13 设计 FAIL。** 换成“已修订/重建完成/保持最新”即可绕过；反向还会误报：`A8.frame_alignment 已写入，且 A3.freshness 与该记录一致` 只是在验证 A3，但因为同句出现“已写入”，C13 把 A3 判成越权写。权限应是 schema（phase `writes` / criterion `action: write|verify`），不应靠中文动词猜。

---

## 4. 新发现的问题

### 4.1 阻断级

#### B1. clean checkout 根本跑不出 21 项全绿

`upstreams/` 被忽略且 tag 不含任何 upstream 文件（`.gitignore:1`；`README.md:60`），但 C7/C9 运行时硬读 upstreams（`scripts/check-closure.py:101-128,334-400`）。复现：

```bash
git worktree add --detach /tmp/tpw-v201-clean v2.0.1
cd /tmp/tpw-v201-clean
python3 scripts/check-closure.py
# C7 FAIL: 文件系统 0，处置表 101
# C9 FAIL: 0 个 upstream 索引，88 条来源失效
# 合计 12/14
```

这与 coldstart 要把 checkers 复制到下游、且不得依赖本库运行时路径正面冲突（`skills/coldstart.md:43-45`；`docs/coldstart.md:48-52,98`）。UCBIP 下游不会天然携带三仓克隆，因此当前安装协议必红。

#### B2. 版本身份自检是假绿

`v2.0.1` tag 内 `VERSION` 和 `workflow/registry.yaml:12` 都仍是 `2.0.0`，C1 却 PASS。可复现：

```bash
git describe --exact-match --tags 0195b19   # v2.0.1
git show v2.0.1:VERSION                     # 2.0.0
```

C1 只比较 VERSION 与 registry，不比较当前 release/tag（`scripts/check-closure.py:154-168`）。README 又把它叫“版本单一来源”。这会让下游锁定、台账 subject 与报告版本混淆。

#### B3. 新增的 subject/scope/frame_alignment 没进入角色与 15 个技能的产出合同

独立逐技能扫描结果：

```text
A6 outputs: 9/9 技能全部缺 subject
A8 outputs: 5/5 技能全部缺 subject、scope、frame_alignment
A9 outputs: decision-ledger 缺 actor、run、subject、phase
```

角色同样缺失：builder 仍说 A6 只有三栏（`roles/builder.md:46-52`），verifier 仍说 A8 只有四栏（`roles/verifier.md:52-59`），scribe 仍说 A9 只有四栏（`roles/scribe.md:39-46`）。当前对象身份只存在于 registry/生成视图/ledger 脚本，不存在于 agent 真正照着工作的角色与技能正文。

#### B4. P5/P6 的 A3 写权仍冲突

registry 说 A3 只能由 architect 更新、verifier 只写 A8.frame_alignment（`workflow/registry.yaml:82,185`）；但 `roles/verifier.md:92` 明令 verifier 更新 A3.freshness，tag 中 `skills/verification-suite.md:26,28-30` 还让 verifier 播种并修改能力清单。P6 又以 A3.freshness 已由 architect 更新为退出条件，却只装 verifier/scribe（`workflow/registry.yaml:299-304`）。C13 只读 registry exit criteria 的七个动词，不读角色和技能，因此全绿。

### 4.2 高严重度：21 项检查中哪些是假检查

我逐条读了两个检查器。下表的“有效”只指该检查对自己宣称的断言有区分力，不代表全库通过。

| 检查 | 判定 | 实际覆盖 |
|---|---|---|
| C1 | **FAIL** | 只比 VERSION 与 registry；当前 tag/version 漂移仍 PASS（`check-closure.py:154-168`） |
| C2 | PASS（窄） | 检查 producer id、consumer id、字段与 rationale；producer 是标量，“唯一”主要靠 schema（`scripts/check-closure.py:170-188`） |
| C3 | **FAIL/过度声称** | 只按 YAML 顺序检查 required_inputs 是否较早出现，不计算图可达性（`scripts/check-closure.py:190-231`） |
| C4 | **FAIL** | 未被 regex 识别的字段引用会被静默忽略（`scripts/check-closure.py:234-256`） |
| C5 | **FAIL/不完整** | 只核 registry 指认，不核角色正文的产物字段；当前 A6/A8/A9 角色合同已漂移（`scripts/check-closure.py:259-300`） |
| C6 | PASS（声明范围内） | 技能/原则有引用、阶段装得出 producer；不查 orphan ribbon（`scripts/check-closure.py:303-330`） |
| C7 | **FAIL** | upstream id 按 basename 折叠，actual 重复不检查；重复 basename 仍全绿（`scripts/check-closure.py:334-356`） |
| C8 | PASS | 对约定格式的角色技能表做双向集合比较（`scripts/check-closure.py:360-380`） |
| C9 | PASS/部分 | registry source id 必须存在，但按 basename 建索引且不核 skill 文件自己的来源段（`scripts/check-closure.py:383-400`） |
| C10 | **FAIL** | 名称写“双向”，实现只有 disposition→target.sources；source 出现在错误的第二 target 不报（`scripts/check-closure.py:403-422`） |
| C11 | **FAIL** | 只有 artifact.consumers→phase.required_inputs；reverse 不查。tag 自带 A6/P6 实例即已错（`scripts/check-closure.py:425-440`） |
| C12 | PASS | 无 sources 的技能必须标 `origin: library`（`scripts/check-closure.py:442-449`） |
| C13 | **FAIL** | 受控动词可绕、可误报、不读角色/技能（`scripts/check-closure.py:451-468`） |
| D1 | **FAIL** | 排除 active docs、大小写敏感、有限黑名单。更直接的当前反例：`scripts/ledger.sh:116` 出现 `PI_AGENT_NAME`/`HERDR_AGENT`，D1 仍 PASS |
| S1 | **FAIL/不完整** | 顶层 md + scripts 顶层；嵌套 skill/role 文件全漏（`scripts/check-consistency.py:136-169`） |
| S2 | **FAIL** | 只扫五个目录顶层 md；fragment dead link、README/docs 引用漏（`scripts/check-consistency.py:174-190`） |
| S3 | **FAIL** | 已诚实声明为词形级，但同一句精确冲突仍漏（`scripts/check-consistency.py:47-55,192-214`） |
| S4 | **FAIL/假检查** | 不比较阶段规则与 role.forbidden 内容；只要 hard rule 点名了一个 default role 就机械判冲突（`scripts/check-consistency.py:216-235`） |
| S5 | **FAIL/不完整** | owner/phase/default role 有用，但未知 output、无关 ribbon carrier 可绕（`scripts/check-consistency.py:239-269`） |
| S6 | PASS | durable 与 required_inputs 的关系能抓，A6→session 注入稳定红（`scripts/check-consistency.py:272-294`） |
| S7 | **FAIL/不完整** | 不校验 applies_to id，不查 orphan ribbon（`scripts/check-consistency.py:297-318`） |

结论：**21 项中 6 项可按声明信任（C2/C6/C8/C9/C12/S6），其余要么范围明显窄于名称，要么存在直接反例。** README 的总免责声明是诚实的，但不能替每一项的错误断言兜底。

### 4.3 高严重度：现行文档与真源仍互相打架

1. `docs/coldstart.md:49` 说 render.py 不需要；`skills/coldstart.md:44,57` 要求重新生成派生文件。冲突未统一。
2. `docs/coldstart.md:75-80,101` 仍使用旧的“闭环完整判档/任何档位不放宽”文本；本轮不评价小任务策略，但这证明 coldstart 文档未随新规则更新。
3. A6 已是 durable（`workflow/registry.yaml:125-144`），`skills/document-mapping.md:33,52` 仍把实现候选称为 session、要求不进版本库。
4. 所有 9 类 artifact 都是 `durable`，但生成文档与 renderer 仍写不存在的枚举 `persistent` 与已无实例的 `session`（`scripts/render.py:181-183`、`docs/artifacts.md:106-107`）。`render --check` 只能证明“错误被稳定生成”。
5. README 写 49 skills，实际 registry/checker 是 50（`README.md:48`；C1 输出“技能 50”）。
6. README 声称原则正文只有一处（`README.md:21-22`），角色仍逐字/扩写原则正文，例如 `principles/architect.md:11-17` 与 `roles/architect.md:25-26`，`principles/architect.md:75-79` 与 `roles/driver.md:43-44`。

### 4.4 来源利用仍有三类缺口

#### frontend-ui-engineering：FAIL

仍被登记进 `security-and-hardening`。本地只保留无障碍几行（`skills/security-and-hardening.md:12,29,37-38`）；上游还有 component architecture、state management、design system、responsive、loading/empty/error、UI finish gate（`upstreams/.../frontend-ui-engineering/SKILL.md:20,101,116,253,269,329`）。这不是“吸收”，只是抽走其中一小段。

#### Definition of Done：FAIL

上游明确区分 standing project-wide DoD 与 per-task acceptance criteria（`upstreams/addyosmani-agent-skills/references/definition-of-done.md:3-15`）。本地质量契约虽要求根目录一个文件（`skills/constraint-driven-development.md:38`），输出却仍塞进每任务 A4（`skills/constraint-driven-development.md:74-83`）；registry 的 A4 是本次冻结契约。references 又被 C7 扫描政策整体跳过（`scripts/check-closure.py:65-66,110`）。概念没有真正拆开。

#### 文件来源表与 registry：2 个实错

- registry 给 tdd 三个来源（含 Addy），技能文件只列 Matt+pstack（`workflow/registry.yaml:710-717`；`skills/tdd.md:51-54`）。
- registry 的 context-reconstruction 是 Matt handoff+pstack reflect，技能文件额外列 pstack recall（`workflow/registry.yaml:882-889`；`skills/context-reconstruction.md:51-55`）。

C9 只核 registry sources 是否存在，不核 50 个技能文件自己的来源段（`scripts/check-closure.py:395-400`）。除三个明确标注 library origin 的技能外，47 个上游来源技能里有这 2 个实错。

Owner 要求“每一段话有来源”目前也没有可审计载体：registry 只有 skill/principle 级 sources，roles 与 scripts 无来源字段，C9 也只遍历 skills/principles。**文件级来源尚未全一致，段落级来源更无从证明。**

### 4.5 A9：脚本本体 PASS，并发声明可复现；临时目录承诺有绕过

#### schema 与并发：PASS

独立比较得到：

```text
registry = actor run subject phase decision why evidence result
docs     = actor run subject phase decision why evidence result
ledger   = actor run subject phase decision why evidence result
all_equal=True
```

按 docs 声称的强度实跑：40 轮×60 + 10 轮×150，每轮首次建表，结果：

```text
failures=0
actors=3
0 丢行 / 0 重复表头 / 0 非 8 栏 / decision 全唯一
僵尸锁恢复后文件 2 行（表头+数据）
```

锁实现见 `scripts/ledger.sh:67-109`，O_APPEND 与 8 栏输出见 `scripts/ledger.sh:111-135`。在本机 APFS 上，docs 的并发数字可复现。

#### 新问题：临时目录拒写可被 symlink 绕过

绝对 `/tmp/...` 正确返回 3；但检查只匹配输入字符串（`scripts/ledger.sh:56-62`）。我让相对路径指向 `/tmp` 的 symlink，脚本返回 0 且实际写入 `/tmp`。所以 `docs/ledger.md:68` 的“写入临时目录拒绝”只对词面路径成立，不是目标路径保证。

---

## 5. 产物流水账：登记表外产物与收敛建议

### 5.1 计数口径

我按“正文明确要求产出、落盘、留存、交付，且 registry 没有声明它是 A1–A9 的形态/副产品”计数；普通代码本身不重复计数，截图/日志若明确是 A8.observation 也不另计。

**结果：18 种命名产物形态没有进入 v2.0.1 registry。**

上一轮 13 种里，有 5 种现在可以明确从“额外类型”移除：research file→A2、handoff brief/context snapshot→A2、spec→A4、tickets→A5、feature-map index/pages→A3（A3 已声明目录形态）。但本轮完整读 50 技能又发现更多此前没盘到的输出，所以净数没有下降。

### 5.2 18 种清单与箭头

| # | 产生产物的话 | 当前缺口 | 建议箭头右端 |
|---:|---|---|---|
| 1 | “把映射表本身当产物管；durable、进版本库”（`skills/document-mapping.md:40,46`） | 明说不属于集合 A | → A9 的 `assembly_binding` 形态，或 registry 增 artifact embodiment；不要新 A10 |
| 2 | “交付一份问卷文件”（`skills/to-questionnaire.md:43-45`） | header/output 都写无编号 | → A1.unknowns 的外抛形态；答复回 A1/A2，问卷可过期 |
| 3 | 词汇表与根索引（`skills/domain-modeling.md:36-41,73`） | A3 当前没有 vocabulary | → 扩 A3；名称应从“能力地图”改为“系统框架/能力与术语地图” |
| 4 | ADR/决策记录（`skills/documentation-and-adrs.md:26-50,64-78`） | architect 直接写 A9，越过 scribe；ADR schema 大于 A9 行 | → A9 long-form decision 的物化形态，由 scribe 追加索引/身份 |
| 5 | 项目级质量契约/standing DoD（`skills/constraint-driven-development.md:38,74-83`） | 被错塞到任务 A4 | → A4 增 `scope: project|task`，或把 A4 改名“验收与质量契约”；必须保留 standing 与 acceptance 两层 |
| 6 | 杠杆文件：脚本/生成器/改造工具/执行说明（`skills/build-the-lever.md:23-37`） | 明说“无产物但一定改文件” | → A6.change 的实现资产；由 builder 产，不另编号 |
| 7 | 验证套件与辅助 driver 脚本（`skills/verification-suite.md:24-27`） | verifier 写持久代码，但 registry 只记 A8 | → 作为独立 A5 slice 由 builder 产 A6；verifier 只能消费并写 A8，避免自验 |
| 8 | CI 流水线/合并保护/部署链/自证记录（`skills/ci-cd-and-automation.md:33-42`） | skill 写“无 A8，交付流水线” | → 配置变更进 A6；人为红灯实测进 A8；决定进 A9 |
| 9 | 浏览器测试计划（`skills/browser-testing.md:29`） | 未映射 | → A8.scope + observation 的计划段，不单列文件类型 |
| 10 | 可观测性问题清单、信号对照表、runbook（`skills/observability-and-instrumentation.md:30-31,44`） | 随 A8 交但无字段 | → A8.scope/frame_alignment；runbook 属 A6 配置/文档变更 |
| 11 | arena 评分表与合成记录（`skills/arena.md:21,31,37`） | A6 旁另放一份 | → 评分/选基底理由进 A7；嫁接/驳回进 A6.known_gaps |
| 12 | 性能尝试记录（`skills/performance-optimization.md:35-44`） | 另交一份 | → 数字进 A8.observation，留/回滚决定进 A9 |
| 13 | 发布 packet：事前清单、分档记录、回滚路径、上线观测、事后记录（`skills/shipping-and-launch.md:29-40`） | 写“无 A8，交付发布记录” | → A9.result 的发布形态 + A8 运行观察；A9 若承载它，建议改名“决策与发布台账” |
| 14 | 版本控制结构：提交序列、分支图、版本/标签/变更日志、残留清单（`skills/git-workflow-and-versioning.md:32-43`） | 无编号 | → 代码/配置状态属于 A6；发布身份与说明索引进 A9 |
| 15 | 上下文重启包：范围/决定、任务状态、工作区状态、验证、未决项；另有分层索引/轻量计划（`skills/context-management.md:51-55,67,87-91`） | 明说“无编号产物” | → 工作面快照进 A2，下一步进 A5，决定进 A9 |
| 16 | 教学练习、反馈、术语表/速查/图解、教学偏好（`skills/teach.md:50-69`） | 明说无文件产物但必须有交付物 | → 明确标成“下游用户交付物，不是工作流 artifact”；否则 registry 的“全部产物”声称不成立 |
| 17 | triage 简报、整备记录、已否决知识库（`skills/triage.md:30,35-42,48`） | A5 之外还有持久知识库 | → 简报/状态进 A5；拒绝理由与知识库索引进 A9 |
| 18 | 迁移计划与跑过的回退脚本（`skills/deprecation-and-migration.md:33-34,36-43`） | 未明确属于 A5/A6 | → 计划进 A5，脚本与迁移代码进 A6，实跑结果进 A8 |

### 5.3 建议收敛后的名字

不建议继续加 A10–A26。建议保留 9 个 id，但在 registry 为每类增加 `embodiments` / `byproducts`，把上表的箭头写死。名字需要改的只有三类：

1. **A3「能力地图」→「系统框架」或「能力与术语地图」**：否则 glossary 塞进去名不副实。
2. **A4「冻结契约」→「验收与质量契约」**：并显式区分 project-wide standing bar 与 task acceptance；不改名就不要把 DoD 塞进去。
3. **A8「验证凭据」→「验证包」**：如果要容纳 scope、计划、未覆盖清单、漂移清单与 observation；若坚持旧名，则这些只能是字段，不得另出文件。
4. **A9 可选改为「决策与发布台账」**：只有在确定承载 mapping/release/git 记录时才改；否则把这些另写的做法删掉。

---

## 6. 打分与放行结论

### 6.1 总分：60 / 100

| 维度 | 满分 | 得分 | 主要扣分 |
|---|---:|---:|---|
| 来源利用与忠实度 | 30 | 22 | -3 frontend UI 仍错并；-2 DoD 仍混淆；-2 skill 文件与 registry 两处来源漂移；-1 无段落级/角色/脚本来源载体 |
| 自洽与可执行性 | 35 | 17 | -7 A6/A8/A9 新字段未进入角色/技能；-4 P5/P6 写权和 consumer 断链；-5 多项检查有直接全绿反例；-2 版本与原则单一正文等自撞（合计按上限扣 18） |
| Governance 与冷启动 | 25 | 14 | -4 clean checkout/downstream C7/C9 必红；-3 coldstart 两份冲突；-3 18 种未注册形态；-1 persistence 枚举错误 |
| 可验证性与实战证据 | 10 | 7 | +3 结构正例、render gate、A9 并发可复现；-3 尚无真实 full-size 任务行为证据，且 checker 绿会掩盖上述实错 |
| **总计** | **100** | **60** | 比 v2.0.0 的 53 有实质进步，但仍未越过 pilot 放行线 |

### 6.2 现在能否用于 UCBIP full-size 试运行

**FAIL，不能。** 最低放行条件：

1. 修 clean checkout：C7/C9 要么有随 release 固化的来源 manifest/hash，要么在无 upstreams 的下游明确 SKIP/不安装；不能假 PASS，也不能必红。
2. 把 A6.subject、A8.subject/scope/frame_alignment、A9 四个身份栏同步进 9/5/1 个技能和 builder/verifier/scribe 角色；加检查，不只改 registry。
3. C11 做真正双向；A6.consumers 加 P6；P6 当场重核 A8.subject==最终 A6.subject。
4. 定死 A3 更新权：P5 verifier 只写 A8.frame_alignment；需要刷新 A3 时回到 architect，或 P6 显式装 architect。删除 `roles/verifier.md:92` 与 verification-suite 的越权文本。
5. A9 只留 8 栏合同；删除角色/技能里的四栏版本。保留现有并发实现，并补 symlink realpath 拒临时目录。
6. 修 C13/S4 的过度声称：权限改成结构字段，不做中文动词猜测；S4 要么真的比对，要么改名为“hard rule 点名角色检查”。S3 保留语义免责声明，但修同句精确冲突漏报。
7. 统一 coldstart 对 render.py、upstreams、persistence 的说法，并在一个真正空的 Git clone 上跑完安装。
8. 处理 frontend-ui 与 DoD；至少不能继续把“只吸收了无障碍”写成整个 frontend UI 已吸收。
9. 为 18 种形态写明确箭头；不一定加新 id，但必须能从 registry 找到 owner/consumer/lifetime。

完成以上后可做**受控 full-size pilot**；是否正式放行仍需真实 UCBIP 行为证据。

---

## 7. UNVERIFIED 项与补证条件

1. **UCBIP 上的真实 full-size 行为：UNVERIFIED。** 本轮没有目标仓、全部 agent 会话、权限与部署环境，不能执行真实 pilot。补证：跑一条跨边界任务，至少含候选在 P5 后变化、环境损坏、agent 中断恢复、发布回滚四个反例。
2. **A9 在 UCBIP 实际共享文件系统：UNVERIFIED。** 本机 APFS 的 40×60 + 10×150 全过；网络盘、不同 shell、进程被 SIGKILL 的极端时序仍按 `docs/ledger.md:70-71` 未验证。
3. **50 个技能的真实行为增益：UNVERIFIED。** 我验证了文本、来源与合同，不等于验证 agent 会因此少犯错。补证：固定模型/工具/预算的 baseline 对照。
4. **81 条 absorbed 的逐段语义完整性：UNVERIFIED。** 本轮按任务重点复核了修过的六条、frontend、DoD 与 50 文件来源结构；registry 没有段落级 provenance，无法证明“每一段话”来自哪一段上游。补证：claim/paragraph → source passage 映射，或收窄 Owner 的要求到文件级来源。
5. **发布与真实回滚：UNVERIFIED。** 无目标环境与授权；只审了协议文本和本地脚本。

---

## 最终判定

| 项目 | 判定 |
|---|---|
| 上一轮 10 条核心修复 | **8 PASS / 2 FAIL** |
| 21 项检查的声明真实性 | **FAIL** |
| A9 8 栏脚本与本机并发 | **PASS** |
| frontend-ui-engineering 处置 | **FAIL** |
| Definition of Done 处置 | **FAIL** |
| coldstart 一致性 | **FAIL** |
| 产物收敛 | **FAIL（18 种命名形态未映射）** |
| 当前 tag 用于 UCBIP full-size pilot | **FAIL** |
