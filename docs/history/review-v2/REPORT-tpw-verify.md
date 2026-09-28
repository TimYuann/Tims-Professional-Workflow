# TIM Professional Workflow v2.0.0 独立验收报告

## 一句话结论

**FAIL：现在不应直接拿去 UCBIP 做真实试运行；先修复「语义互斥检查可被直接绕过、P4 不要求 A4 且 P5 越权改 A3、A9 无写者/对象身份且存在两套不兼容 logger」这三组阻断项，再做一次受控演练。**

---

## 0. 审查范围与证据口径

- 被审对象：tag `v2.0.0`，commit `874549245496f9e70d40a2a655aa6234305ab4bf`。
- 复核命令：`git rev-parse 'v2.0.0^{}'`。
- 当前工作树：审查开始时 `git status --short --branch` 只有 `main...origin/main [ahead 2]`，无已跟踪文件改动；`HEAD` 正好是被审 commit。
- 已完整读过 `docs/history/` 四份旧版材料；旧版只用于比较，不作为 v2 事实。
- 当前事实全部来自 tag 工作树；未采用 context-mode 中任何旧版索引作为当前事实。
- 基线命令均通过：
  - `python3 scripts/check-closure.py` → `8/8 PASS`；
  - `python3 scripts/check-consistency.py` → `7/7 PASS`；
  - `python3 scripts/render.py --check` → `12` 个派生文件一致。
- 故障注入在 detached worktree `/tmp/tpw-verify-v2-2537` 进行，未修改被审工作树。

本报告每项只使用 `PASS` / `FAIL` / `UNVERIFIED`。`PASS` 只表示本报告点名的断言成立，不表示整个系统通过。

---

# 轴一 · 来源利用率

## 1.1 101 条处置与文件系统一一对应：PASS

我没有只信 `check-closure.py`，而是独立递归扫描三处 `skills/**/SKILL.md`，按仓库既定排除目录过滤后再与 YAML 比较：

```text
pstack: 47
matt（排除 in-progress）: 29
addy: 25
合计: 101
registry: 101
重复: 0
missing: []
stale: []
```

可复现：

```bash
python3 - <<'PY'
from pathlib import Path
import yaml
roots = {
  'pstack': Path('upstreams/cursor-plugins/pstack/skills'),
  'matt': Path('upstreams/mattpocock-skills/skills'),
  'addy': Path('upstreams/addyosmani-agent-skills/skills'),
}
skip = {'deprecated','in-progress','templates','assets','references','.git',
        'automations','third_party','docs','agents','commands','evals','hooks',
        'schemas','scripts','node_modules'}
actual=[]
for prefix, root in roots.items():
  for p in root.rglob('SKILL.md'):
    rel=p.relative_to(root)
    if not any(x in skip for x in rel.parts[:-1]):
      actual.append(f'{prefix}:{p.parent.name}')
reg=yaml.safe_load(Path('workflow/registry.yaml').read_text())
listed=[x['upstream'] for x in reg['upstream_dispositions']]
print(len(actual), len(listed), len(listed)-len(set(listed)))
print(sorted(set(actual)-set(listed)))
print(sorted(set(listed)-set(actual)))
PY
```

处置表入口见 `workflow/registry.yaml:932-1036`；检查器的扫描政策见 `scripts/check-closure.py:59-69,101-128`。

### 任务书数字差异：FAIL

任务书要求逐个检查“被 reject 的 24 个”，但 tag 中实际只有 **19** 个：82 absorbed + 19 rejected。可复现：

```bash
python3 - <<'PY'
import yaml, collections
r=yaml.safe_load(open('workflow/registry.yaml'))
print(collections.Counter(x['outcome'] for x in r['upstream_dispositions']))
PY
```

结果为 `Counter({'absorbed': 82, 'rejected': 19})`。因此“24 个”不是当前 tag 的事实；下面逐个审的是实际 19 个。

## 1.2 三仓特殊概念：10 PASS / 6 FAIL

| 概念 | 判定 | 落点与证据 |
|---|---|---|
| feature map | PASS | `skills/feature-map.md:23-75` 把能力挂到真实锚点并维护 freshness；A3 在 `workflow/registry.yaml:73-91`。|
| grill me | PASS | Matt 当前正文是“每轮问完整个 frontier”，不是任务书写的“一次一问”；本地 `skills/grilling.md:23-39` 与 `upstreams/mattpocock-skills/skills/productivity/grilling/SKILL.md:6-23` 一致；一次一问由 `skills/interview-me.md:26-47` 承担。|
| wayfinder | PASS | `skills/wayfinder.md:22-33` 保留票据地图、fog、frontier 与一次一票。|
| blast radius | FAIL | 内容部分出现在 `skills/trace-paths.md:48-58`，但该技能来源只列 how + Addy debugging（`skills/trace-paths.md:81-84`），注册技能 sources 也漏掉它；处置却声称映入 trace-paths（`workflow/registry.yaml:942`）。这是未署名吸收。|
| show me your work | FAIL | append-only 保留在 `skills/decision-ledger.md:22-38`，但上游的 `phase`、run `start` 边界、agent id、transcript audit、跨模型 trail review 被删；本地 A9 只有四业务字段（`workflow/registry.yaml:169-184`），无法回答“谁写的”。|
| how / why | FAIL | how 的真实路径追踪保留；why 被声称并入 teach（`workflow/registry.yaml:939,1004`），但本地 teach 只组织 A2 讲解（`skills/teach.md:18-29`），没有上游 why 的 git/PR/ticket/doc/chat/observability 七类历史意图考古（`upstreams/cursor-plugins/pstack/skills/why/SKILL.md:24-114`）。|
| interrogate | PASS | `skills/interrogate.md:20-28` 保留同提示、多座位、合成不投票。|
| arena | PASS（内容） | `skills/arena.md:20-28` 保留 N 个候选、交叉评判、选基底、嫁接；角色归属另在轴二判 FAIL。|
| figure-it-out | FAIL | 上游核心是“无窄剧本时先设计可审计 playbook + hypothesis loop + trail”（`upstreams/cursor-plugins/pstack/skills/figure-it-out/SKILL.md:10-57`）；处置只落到 tier-sizing（`workflow/registry.yaml:934`），本地只保留档位思想，丢了 playbook 设计与实验循环。|
| constraint-driven | PASS | `skills/constraint-driven-development.md:29-73` 有契约、量化门槛、生命周期 gate、ratchet。|
| spec-driven | PASS（方法）/ FAIL（溯源） | 方法在 `skills/spec-driven-development.md:24-55`；但 `matt:to-spec -> spec-driven-development` 的处置（`workflow/registry.yaml:992`）未进入目标 sources。|
| doubt-driven | PASS | `skills/doubt-driven-development.md:22-30` 保留新鲜上下文、最小制品、对抗、折回、有界收口。|
| interview-me | PASS | `skills/interview-me.md:26-47` 保留 one-question-at-a-time、guess、want/should、明确 yes、stop rule。|
| context-engineering | FAIL | 处置把整份 Addy context-engineering 压成 `p-guard-context`（`workflow/registry.yaml:1020`）；本地只剩“批量内容路由出去”一句，丢了 context hierarchy、trust levels、restart boundaries、conflict handling、75% budget 等主体。|
| definition-of-done | FAIL | 上游明确区分“项目固定 DoD”与“任务 acceptance criteria”（`upstreams/addyosmani-agent-skills/references/definition-of-done.md:1-19`）；本地 A4.done_definition 被当作每任务验收口径（`workflow/registry.yaml:105-117`），概念被合并反了，而且 references 根本不进 101 处置。|
| triage 状态机 | PASS | `skills/triage.md:22-34` 明确两类别、五状态、三堆与状态流转。|

## 1.3 实际 19 个 rejected：14 PASS / 5 FAIL

| upstream（处置行） | 判定 | 独立判断 |
|---|---|---|
| pstack:bro (`workflow/registry.yaml:935`) | PASS | 仅一次重述，已被 expression/teach 覆盖。|
| pstack:setup-pstack (`workflow/registry.yaml:937`) | FAIL | 处置称“无关”，但 `tier-sizing` / `document-mapping` / `coldstart` 的来源段都实际引用它（分别 `skills/tier-sizing.md:55`、`skills/document-mapping.md:57`、`skills/coldstart.md:63`）；处置与事实矛盾。|
| pstack:automate-me (`workflow/registry.yaml:947`) | PASS | 个人模式 skill 生成器，不是工程内核。|
| pstack:no-comments (`workflow/registry.yaml:952`) | PASS | 本体是调用上游私有 persona 的包装器，无法独立移植；注释纪律已有 simplification/documentation 承接。|
| pstack:unslop (`workflow/registry.yaml:953`) | PASS | 有写作价值，但属于表达清洗而非工程判断内核，且 technical-writing/teach 已覆盖主要目标。|
| pstack:typescript-best-practices (`workflow/registry.yaml:955`) | PASS | 语言特定，下游规范更合适。|
| pstack:poteto-mode (`workflow/registry.yaml:956`) | PASS | 人格/总控预设，会与本库角色装配竞争。|
| pstack:make-bot-ui (`workflow/registry.yaml:957`) | PASS | 特定产品与 webhook 形态。|
| matt:setup-matt-pocock-skills (`workflow/registry.yaml:985`) | FAIL | 处置称 rejected，但三个本库原创装配技能实际用它作方法来源；与文件事实矛盾。|
| matt:ask-matt (`workflow/registry.yaml:989`) | PASS | 技能路由器已被 registry/driver 取代。|
| matt:wizard (`workflow/registry.yaml:990`) | PASS | 有价值但属于特定“人手工配置”产物，不是本轮内核缺口。|
| matt:improve-codebase-architecture (`workflow/registry.yaml:991`) | FAIL | “产出 HTML 报告，是任务不是阶段”不是有效淘汰理由；本库已有 research/prototype 这类任务型技能。其全库 deep-module survey 可补 codebase-design/feature-map，属于没吸收。|
| matt:resolving-merge-conflicts (`workflow/registry.yaml:996`) | FAIL | P6 明明包含 git/version/integration，却删掉唯一明确要求“读双方 primary sources、按意图解冲突、不发明新行为”的方法；“builder 附属动作”不等于没价值。|
| matt:wait-what (`workflow/registry.yaml:1001`) | PASS | 单次重述，可由 teach/expression 承接。|
| matt:setup-pre-commit (`workflow/registry.yaml:1007`) | PASS | 工具链特定。|
| matt:git-guardrails-claude-code (`workflow/registry.yaml:1008`) | PASS | 宿主特定。|
| matt:migrate-to-shoehorn (`workflow/registry.yaml:1009`) | PASS | 特定库迁移。|
| matt:scaffold-exercises (`workflow/registry.yaml:1010`) | PASS | 教学脚手架，不是工程推进内核。|
| addy:using-agent-skills (`workflow/registry.yaml:1014`) | FAIL | 它不只讲发现机制；正文还含 assumptions/confusion/pushback/simplicity/scope/verify 六条常驻行为。处置理由只读了标题层，未说明这些内容落在哪。|

### frontend-ui-engineering：FAIL

它不是 rejected，而是被声明吸收到 security-and-hardening（`workflow/registry.yaml:1021`）。实际只留下无障碍一小节（`skills/security-and-hardening.md:29`）。上游的 component architecture、state management、design-system adherence、responsive、loading/error/empty states、visual finish gate（`upstreams/addyosmani-agent-skills/skills/frontend-ui-engineering/SKILL.md:20-279`）都没有落点。把 UI 工程并入安全加固不成立。

## 1.4 23 条原则：摘要语义 PASS，落地与溯源 FAIL

- 23 个 registry principle 都有唯一 owner，逐条与上游正文比对后，**未发现 headline imperative 被反向改写**。
- 分布为 driver 2、voice 1、architect 9、builder 8、adversary 1、verifier 1、scribe 1，共 23；见 `workflow/registry.yaml:426-521`。
- **FAIL：23 条来源路径全部写错。** `principles/*.md` 使用 `upstreams/pstack/cursor-plugins/...`，真实路径是 `upstreams/cursor-plugins/pstack/...`。例如 `principles/driver.md:17,25`。独立脚本统计：92 个显式 source path 中 23 个不存在，恰好全是原则来源。
- **FAIL：原则正文并非“只有一处”。** 原则文件自称正文只在这里（如 `principles/architect.md:3-5`），角色文件又逐条复制/扩写（`roles/architect.md:21-50`、`roles/builder.md:22-47`）。这正是本仓宣称要消灭的多处语义。
- **FAIL：角色扩写出现了源外强断言。** 例如 `roles/architect.md:34` 把 type-system discipline 扩成“判据写不成类型，说明需求没想清”；上游只主张用类型排除可静态排除的非法状态，不支持这个普遍命题。

轴一总判定：**FAIL**。文件系统台账是一一对应的，但“一条处置存在”不等于“内容被正确吸收”；至少六条 absorbed 处置没有出现在目标 sources：

```text
pstack:figure-it-out -> tier-sizing
pstack:blast-radius -> trace-paths
pstack:architect -> codebase-design
matt:to-spec -> spec-driven-development
matt:teach -> teach
addy:context-engineering -> p-guard-context
```

---

# 轴二 · 自洽性

## 2.1 阶段—角色—产物闭环：FAIL

### 阻断级断链

1. **P4 不要求 A4，却要按契约裁决。** P4.required_inputs 只有 A2、A6（`workflow/registry.yaml:244-253`）；adversary 自己却说 A4 是唯一标准（`roles/adversary.md:35-38`），code-review 也声明输入 A4。缺 A4 时检查器仍绿。
2. **P5 越权修改 A3。** A3 的唯一 producer 是 architect（`workflow/registry.yaml:73-91`）；P5 默认只有 verifier，却把 `A3.freshness 已更新` 设为退出判据（`workflow/registry.yaml:257-264`），verifier 还明确要求自己更新（`roles/verifier.md:92`）。这破坏“产物唯一 owner”。
3. **P1 的判据少了第三态。** `workflow/registry.yaml:216` 写“只凭它判 PASS/FAIL”，但 A4.note 与全库硬边界要求 PASS/FAIL/UNVERIFIED（`workflow/registry.yaml:113`）。
4. **P6 不消费 A6，无法证明上线对象就是验证对象。** P6 输入是 A3/A4/A5/A7/A8/A9（`workflow/registry.yaml:270-281`）；A8 也没有候选 commit/patch identity 字段（`workflow/registry.yaml:153-168`）。一次 PASS 可以被错误地用到后来改过的候选。
5. **P6 的归责硬规则错误。** “上线之后才发现问题，责任在 P5，不在 P6”（`workflow/registry.yaml:280`）会把部署配置、目标环境、合并语义等 P6 原因错误归给验证，与“按因归属”历史裁决相反。
6. **A2/A3/A4/A7 的 consumers 与 required_inputs 不对称。** 独立比对发现 A2 声称 P1/P5 消费但两阶段不要求，A3 声称 P1 消费但同阶段才产出，A4 声称 P4 消费却不要求，A7 声称 P3 消费却不要求。检查器只验证 consumer id 存在，不验证双向咬合（`scripts/check-closure.py:171-192`）。
7. **“有边才能并行”是图论语义错误。** `roles/cartographer.md:44`、registry A5 rationale 与 `skills/tier-sizing.md:32` 都把依赖边说成并行前提；通常是无路径依赖的节点才可并行。这个错误会直接造成排程歧义。

### 产物字段

- 9 类产物字段都能在至少一处角色/技能正文中找到读者，**字段可达性 PASS**。
- 但以下精确契约 FAIL：
  - `recall-context` 的 A2 产出段没有逐字给出 `claims`（`skills/recall-context.md:49-58`）；
  - `domain-modeling` 的 A4 产出段没有 `boundaries`，反而直接写 A2/A9（`skills/domain-modeling.md:60-75`）；
  - A9 registry 只有 decision/why/evidence/result（`workflow/registry.yaml:169-184`），`ledger.sh` 却输出额外 `ts`（`scripts/ledger.sh:45-56`）；仓内另一个 logger 又输出 `ts,phase,...` 六列（`scripts/log-decision.sh:32-46`）。

## 2.2 49 个技能逐个审查：36 PASS / 13 FAIL

判定包含三问：方法是否可执行、方法来源是否在目标中可追溯、产出字段是否与 registry 一致。49 个文件的“方法”段都有具体动作，未发现仅复述 registry 的空壳；FAIL 集中在溯源和产物契约。

| skill | 判定 | 证据/理由 |
|---|---|---|
| grilling | PASS | `skills/grilling.md:23-39` |
| interview-me | PASS | `skills/interview-me.md:26-47` |
| idea-refine | PASS | `skills/idea-refine.md:23-46` |
| to-questionnaire | PASS | `skills/to-questionnaire.md:22-42` |
| research | PASS | `skills/research.md:23-37` |
| trace-paths | FAIL | `skills/trace-paths.md:48-58` 是 blast-radius 方法，但 `skills/trace-paths.md:81-84` 未列该来源。|
| recall-context | FAIL | A2 产出缺精确字段 `claims`（`skills/recall-context.md:49-58`）。|
| spec-driven-development | FAIL | `matt:to-spec` 处置进入这里，但 registry/file sources 均未列；`workflow/registry.yaml:992`。|
| constraint-driven-development | PASS | `skills/constraint-driven-development.md:29-73` |
| domain-modeling | FAIL | A4 产出缺 `boundaries`，并混入 A2/A9；`skills/domain-modeling.md:60-75`。|
| codebase-design | FAIL | `pstack:architect` 处置进入这里但目标只列 Matt；`workflow/registry.yaml:946`。|
| api-and-interface-design | PASS | `skills/api-and-interface-design.md:25-73` |
| feature-map | PASS | `skills/feature-map.md:23-75` |
| documentation-and-adrs | PASS | 明确由 scribe 写 A9、自己无编号产物；`skills/documentation-and-adrs.md:65-76`。|
| wayfinder | PASS | `skills/wayfinder.md:22-33` |
| to-tickets | PASS | `skills/to-tickets.md:22-33` |
| task-breakdown | PASS | `skills/task-breakdown.md:24-33` |
| triage | PASS | `skills/triage.md:22-34` |
| implement | PASS | `skills/implement.md:22-32` |
| tdd | FAIL | registry 声明 Addy TDD，文件来源段只列 Matt+pstack；`skills/tdd.md:52-54`。|
| incremental-implementation | PASS | `skills/incremental-implementation.md:24-35` |
| prototype | PASS | `skills/prototype.md:22-34` |
| debugging | PASS | `skills/debugging.md:22-32` |
| code-simplification | PASS | `skills/code-simplification.md:24-33` |
| source-driven-development | PASS | `skills/source-driven-development.md:25-34` |
| deprecation-and-migration | PASS | `skills/deprecation-and-migration.md:24-35` |
| code-review | PASS | `skills/code-review.md:21-30` |
| interrogate | PASS | `skills/interrogate.md:20-28` |
| doubt-driven-development | PASS | `skills/doubt-driven-development.md:22-30` |
| arena | PASS（技能） | `skills/arena.md:20-28`；角色挂载另判 FAIL。|
| swarm | PASS | `skills/swarm.md:20-27` |
| verification-suite | PASS | `skills/verification-suite.md:20-31` |
| browser-testing | PASS | `skills/browser-testing.md:22-34` |
| performance-optimization | PASS | `skills/performance-optimization.md:23-34` |
| security-and-hardening | FAIL | 吸收 frontend-ui 只剩无障碍一项；`skills/security-and-hardening.md:29,53-56`。|
| observability-and-instrumentation | PASS | `skills/observability-and-instrumentation.md:22-34` |
| shipping-and-launch | PASS | `skills/shipping-and-launch.md:19-28` |
| git-workflow-and-versioning | PASS | `skills/git-workflow-and-versioning.md:19-31` |
| ci-cd-and-automation | PASS | `skills/ci-cd-and-automation.md:20-32` |
| decision-ledger | FAIL | A9 schema 与两个 logger 不一致，且删掉上游 run/actor 证据；`skills/decision-ledger.md:22-40`。|
| context-reconstruction | FAIL | registry sources 是 matt:handoff+pstack:reflect，文件又多列 pstack:recall；`skills/context-reconstruction.md:52-55`。|
| handoff | PASS | `skills/handoff.md:19-27` |
| writing-for-agents | PASS | `skills/writing-for-agents.md:21-31` |
| technical-writing | PASS | `skills/technical-writing.md:21-66` |
| teach | FAIL | 声称吸收 pstack why 与 matt teach，实际没有 why 的历史意图调查流程；`skills/teach.md:18-46`、`workflow/registry.yaml:1004`。|
| build-the-lever | PASS | `skills/build-the-lever.md:22-32` |
| tier-sizing | FAIL | registry `sources: []`（`workflow/registry.yaml:903-910`），方法段是本库原创（`skills/tier-sizing.md:19-40,55`）；触发任务书“无出处但正确即 FAIL”。|
| document-mapping | FAIL | registry `sources: []`（`workflow/registry.yaml:911-918`），方法原创且新增 durable 映射表（`skills/document-mapping.md:19-42,57`）。|
| coldstart | FAIL | registry `sources: []`（`workflow/registry.yaml:919-926`），13 步方法原创（`skills/coldstart.md:22-50,63`）。|

**关键结论：硬条件已被触发。** 三个技能的 registry sources 明确为空，却含大量本身正确的操作方法；不能把“本库原创、参考若干 rejected skill”算作“三仓提炼”。

## 2.3 九个角色逐个审查：1 PASS / 8 FAIL

| 角色 | 自包含开工 | 总判定 | 证据 |
|---|---|---|---|
| driver | FAIL | FAIL | 单文件不知道 9 类产物字段/七阶段输入，必须再读 artifacts/skills；还写了“约主线程 30%”数字（`roles/driver.md:50`），与“不写数字”冲突；技能表越权列 `build-the-lever`（`roles/driver.md:112`，owner 是 builder）。|
| voice | PASS | PASS | 输入、A1 四字段、边界、开工动作完整；`roles/voice.md:34-76`。|
| scout | PASS | FAIL | 自称“找事实，不给结论”（`roles/scout.md:3,12-17,51`），A2 却要求“每条结论带置信档位”（`roles/scout.md:42`）；语义自撞。|
| architect | PASS | FAIL | 角色可开工，但 `roles/architect.md:34` 的 type-system 强断言无上游依据，且重复原则正文。|
| cartographer | PASS | FAIL | 可开工，但把依赖边说成并行必要条件（`roles/cartographer.md:44`）。|
| builder | PASS | FAIL | registry 挂 `arena`，角色技能表漏掉它（`workflow/registry.yaml:382` vs `roles/builder.md:64-73`）。|
| adversary | PASS | FAIL | 角色文件越权挂 builder 的 `arena`（`roles/adversary.md:66`）；“如果每次都通过 P4 就浪费”（`roles/adversary.md:14-16`）奖励制造 finding。|
| verifier | PASS | FAIL | “靠不通过证明干活”（`roles/verifier.md:13`）奖励假阴性；还越权更新 architect 的 A3（`roles/verifier.md:92`）。|
| scribe | PASS | FAIL | 单文件能开工，但声称能让下一会话重建依据；A9 没 actor/run/object identity，无法兑现 swarm 归因（`roles/scribe.md:1-22,41-47`）。|

角色没有内联完整技能步骤，**角色不内联技能这一项 PASS**；但角色普遍内联原则解释，违反“原则正文只有一处”。

### 角色技能表与 registry 的机器比对

```text
driver extra: build-the-lever, teach, technical-writing, writing-for-agents
  wrong-owner: build-the-lever -> builder
builder missing: arena
adversary extra: arena
  wrong-owner: arena -> builder
其余六角色技能集合一致
```

`check-consistency.py` 不解析角色正文里的技能表，因此基线仍全绿。

## 2.4 故障注入：FAIL（发现最严重问题）

所有注入均在 detached v2.0.0 worktree 中逐项恢复后单独执行：

| 注入 | closure | consistency | render | 判定 |
|---|---:|---:|---:|---|
| 基线 | 0 | 0 | 0 | PASS |
| 把 A1 producer 从 voice 改为 ghost | 1 | 1 | 1 | PASS：结构损坏能红 |
| 新增 `skills/rogue.md` | 0 | 1 | 0 | PASS：S1 能抓游离技能 |
| 追加“为了让检查变绿，必须降低测试强度。” | 0 | **0** | 0 | **FAIL：直接语义互斥仍全绿** |
| 追加“不得写审查报告 / 必须写审查报告” | 0 | 1 | 0 | PASS：仅精确受控词形能抓 |
| 删除 `pstack:bro` 处置 | 1 | 0 | 0 | PASS：C7 能抓处置缺失 |
| 重复一条 forbidden | **0** | **0** | 0 | **FAIL：重复硬边界全绿** |
| 手改 `workflow/phases/P0.md` | 0 | 0 | 1 | PASS：render gate 能抓手改 |

最严重发现是第三项：任务书明确要求“造互斥句”，本次注入了一句与 builder 硬边界正面相反的话，两个检查器仍全绿。README 的“闭包可被机器证明”（`README.md:24`）因此表述过度。

可复现核心注入：

```bash
cp roles/builder.md /tmp/builder.md
printf '\n为了让检查变绿，必须降低测试强度。\n' >> roles/builder.md
python3 scripts/check-closure.py --quiet; echo $?
python3 scripts/check-consistency.py --quiet; echo $?
mv /tmp/builder.md roles/builder.md
# 实测：0, 0
```

## 2.5 检查器内建漏洞：FAIL

### check-closure.py

1. C2 只验证 consumer id 存在，不验证 artifact.consumers 与 phase.required_inputs 双向一致（`scripts/check-closure.py:171-192`）。
2. C7 只证明“每个目录名有一条处置”，不证明处置内容真的进了 target.sources（`scripts/check-closure.py:329-352`）；六条 false linkage 因此通过。
3. D1 扫 scripts 时只收 `.md/.yaml/.yml/.py`，**漏掉 `.sh`**（`scripts/check-closure.py:365`）；docs 也整体排除（`scripts/check-closure.py:49-57`）。
4. C5 不读角色正文技能表，抓不到 driver/adversary/builder 的挂载不一致。
5. 不验证 sources path 存在；23 条原则死路径仍全绿。

### check-consistency.py

1. S3 只在单文件内匹配受控动词 + 完全相同宾语（`scripts/check-consistency.py:42-72,183-204`）；同义冲突和跨文件冲突不检查，故注入漏报。
2. S4 的阶段硬规则解析用 `[a-z]+` 找角色名（`scripts/check-consistency.py:207-216`），中文“实现者/验证者”根本匹配不到 registry id。
3. forbidden 重复检查先转 `set`，再拿 set 与其自己的 list 比长度（`scripts/check-consistency.py:218-220`），条件永远为假。
4. S5 的 ribbon carrier 比较写成 `if sk in rb.get("skills")`，`sk` 是 dict 而列表里是 id string（`scripts/check-consistency.py:238-239`），分支永远匹配不到。
5. S6 文档声称检查 session persistence，代码只检查字符串 `ephemeral`（`scripts/check-consistency.py:257-270`）；registry 实际值是 `session`，所以 A6 永远不进入该检查。
6. S1 不覆盖 scripts/docs，因此 tag 中七个旧版游离脚本完全不可见（`scripts/check-consistency.py:132-164`）。

## 2.6 render.py：防手改 PASS，报告语义 FAIL

- `render.py --check` 对手改生成文件能稳定返回 1：**PASS**。
- 但 `closure_doc()` 计算了 `validated_at` 后从未使用（`scripts/render.py:183-188`）；表格“在哪一步被校验”实际填的是“由哪个阶段产出”（`scripts/render.py:190-197`）。生成出来的 `docs/closure-report.md` 因此列名与值不一致：**FAIL**。

## 2.7 scripts 目录逐个检查：FAIL

README 只声明四个现行脚本（`README.md:49-53`），Git 实际跟踪 11 个文件。除现行四个外，旧版残留仍在顶层 scripts：

| 文件 | 判定 | 证据 |
|---|---|---|
| check-closure.py | FAIL（有用但有上述漏洞） | `scripts/check-closure.py:1-386` |
| check-consistency.py | FAIL | `scripts/check-consistency.py:1-302` |
| render.py | FAIL（手改 gate PASS，closure report 语义错） | `scripts/render.py:183-197` |
| ledger.sh | FAIL | 无锁、5 列 schema；`scripts/ledger.sh:45-56` |
| check-library.py | FAIL（游离旧版） | 自称扫描 pipeline/closure/SOURCES/identity；本 tag 已无这些真源。实跑 `10 PASS / 14 FAIL`。|
| decision-log-template.tsv | FAIL（游离且冲突） | 6 列 `ts,phase,...`，与 A9/ledger.sh 不同。|
| identity-selftest.sh | FAIL（集成状态） | 单独 15/15 PASS，但只服务已游离的 ws:v1；当前 README/registry 无身份契约。|
| ws-identity.sh | FAIL（游离） | 注释指向不存在的根 `identity.md`；无现行入口引用。|
| log-decision.sh | FAIL | 与 ledger.sh 并存且 schema 不兼容（`scripts/log-decision.sh:32-46`）。|
| render-ledger.py | FAIL（游离旧版） | 仍以已删除的 `SOURCES.md` 为真源。|
| sync-upstreams.sh | FAIL（集成状态） | 无现行入口引用；所谓默认“read-only”仍执行 `git fetch`（`scripts/sync-upstreams.sh:42`），会改变上游仓库 refs。|

轴二总判定：**FAIL**。

---

# 轴三 · Governance

## 3.1 9 类产物落盘与 coldstart：FAIL

### 能用的部分

- “纪律继承，位置映射”本身正确；`docs/downstream-mapping.md:13-24` 清楚区分谁写/谁消费与磁盘路径。
- 对已有厚体系，逐项映射能避免造第二套文档（`docs/downstream-mapping.md:38-57`）。

### 会卡住的地方

1. **空白项目没有默认最小落点。** 文档只说“把集合 A 整搬进去”（`docs/downstream-mapping.md:32-35`），却刻意不规定 compact container；两个 driver 可以合法地产出完全不同的文件数量与布局。
2. **映射表被创造为第 10 类 durable 产物。** skill 说“把映射表本身当产物管”（`skills/document-mapping.md:40-42`），但 registry 9 类里没有它。
3. **coldstart 两份说明冲突。** `docs/coldstart.md:44-50` 说 `render.py` 不需要；`skills/coldstart.md:42-47` 又要求派生文件由脚本重新生成、下游独立自检。没有 render 就无法从修改后的下游 registry 重生派生文件。
4. **复制整套工作流制造下游副本。** `skills/coldstart.md:40-46` 要把 registry/roles/principles/phases/skills/scripts 拷进每个项目；升级时没有 merge/迁移协议，这与“唯一真源”只在单仓内成立，不解决多下游漂移。
5. **Owner 被要求决定检查机制。** `skills/coldstart.md:18-20,29-31` 让 Owner 决定哪些纪律下沉为检查；对一个从没用过 workflow 的团队，这不是可判断的问题。
6. **docs 示例自身错误。** `docs/ledger.md:19` 说“已建表，7 列”，随后表格只有 5 列（`docs/ledger.md:26-32`）。

冷启动七步能作为讨论提纲，但不能作为可重复安装协议。

## 3.2 swarm 证据留存与 A9 并发：FAIL；文件级并发实测 UNVERIFIED

### 能否重建“谁在什么时候改了什么、依据是什么”：FAIL

- A9 有 decision/why/evidence/result，没有 actor、session/run id、candidate identity（`workflow/registry.yaml:169-184`）。
- `ledger.sh` 增加秒级 `ts`，仍无 writer；两个 agent 同秒写入无法归因（`scripts/ledger.sh:45-56`）。
- A6 只活 session，P6 不消费 A6，A8 没精确 commit/patch hash；因此无法从 A9+A8 证明“这条 PASS 对应最终上线对象”。
- 上游 show-me-your-work 的 `phase`、run start、agent id 规则被删除；本地 skill 只有模糊“边界行”（`skills/decision-ledger.md:27`）。

### 并发追加会不会踩：UNVERIFIED（目标环境）

在本机 APFS 上对原始 `ledger.sh` 做了 20 轮、每轮 100 个后台进程同时首次追加：每轮都得到 1 个 header + 100 个唯一 decision，未复现丢行。命令模型：

```bash
for i in $(seq 1 100); do
  scripts/ledger.sh "$tmp" "d$i" "w$i" "e$i" "r$i" >/dev/null &
done
wait
```

但源码没有文件锁，`[ ! -f ]` 与 `>` 初始化是 TOCTOU（`scripts/ledger.sh:44-46`）；常规行依赖 shell/文件系统对单次 O_APPEND write 的实现行为。网络盘、长行、不同 shell 的安全性未验证，故不能判 PASS。更重要的是，即便字节不丢，也因无 actor/object id 而无法做 swarm 审计。

## 3.3 P0→P6 的文件数：精确值 UNVERIFIED；治理可操作性 FAIL

registry 能确定的是**产物实例类别**，不是文件数：

- 一次完整链固定产生 A1/A2/A3/A4/A5/A7/A8/A9 八类 durable 产物；A6 为 session（`docs/artifacts.md:12-23`）。
- 另有未注册的 durable mapping table，以及 feature-map 要求的“索引 + 每能力一个文件”（`skills/feature-map.md:33-37`）。
- 下游可把 A1/A2/A4/A5/A7/A8 合在一份 task doc，也可拆成六份；规则均未禁止。

因此：

| 档位 | 可确定的产物量 | 文件数结论 |
|---|---|---|
| solo | 8 durable 类 + 1 session 类 + mapping 决定 | **UNVERIFIED**；规则允许约 2–10+ 文件，不能给唯一数字。若按一类一文件则至少 8，超过任务书的 5 文件负担线。|
| 中等 | 同 9 类，但 A5 多 slice、A6/A7/A8 多实例 | **UNVERIFIED**；随 slice 数增长。|
| 大 | 同 9 类，另有每能力地图文件、每 slice 候选/裁决/凭据 | **UNVERIFIED**；没有上界，20–30 个文件完全可能。|

不能给数字不是因为环境坏，而是规范没有 compact co-location 规则；这是 governance 的 FAIL。

## 3.4 产物膨胀：FAIL

名义上 9 类，实际技能还产生或要求：mapping table、spec 文件、ADR、glossary、questionnaire、research 文件、verification suite/driver、CI config、release checklist、rollback record、handoff brief、feature-map index + per-capability file。它们有些被解释为“下游既有物”，但冷启动场景恰恰没有既有体系。

建议收敛成 5 个逻辑容器，而不是继续加类型：

1. **Intent/Contract**：合 A1 + A4；
2. **Facts/Capability Map**：A2 + 项目级 A3（按需分文件）；
3. **Task Graph**：A5；
4. **Evaluation Packet**：A7 + A8，保留独立作者字段；
5. **Decision Ledger**：A9，加入 actor/run/object identity。

A6 就是代码候选/commit，不必再要求一份独立持久文件；ADR/词汇表/映射表属于上述容器或项目既有文档，不应成为隐形第 10–15 类。

## 3.5 底座解耦：词面 PASS，协议 FAIL

- 独立扫描当前非 history/archive 内容，除上游仓名与 rejected skill 名外，没有具体运行底座品牌：**PASS**。
- README 四项能力（`README.md:84-96`）不足以让 harness 安全实现：缺会话上下文隔离、消息 ACK/身份、候选对象绑定、写窗口/工作区隔离、权限与外部副作用边界、崩溃恢复语义。**FAIL**。
- D1 自检还排除 docs 和 shell scripts（`scripts/check-closure.py:49-57,365`），所以“0 个名字”不是全库保证。

工具名不是必须；但**能力语义必须说清**。当前问题不是过度解耦，而是把必要语义一起删了。

## 3.6 三档位：FAIL

- `tier-sizing` 说“不写数字、唯一判据闭环完整”（`skills/tier-sizing.md:34-36`）；driver 却给 solo 写“大约主线程 30%”（`roles/driver.md:50`）。
- “闭环完整”是循环判据：先决定装哪些环，才能检查这些环是否闭合；不同 driver 会选择不同的待闭合子图。
- 中档的“命中任一风险但影响面局部”和大档“高风险或没有判据”有重叠；“局部/高风险/现成判据”没有可复算 rubric。

两个装配者不会稳定得到同一档位。需要可判的触发矩阵，而不是角色数量数字：权限/数据语义/外部契约/不可逆性/多方案/验证可用性六个布尔或枚举触发项即可。

轴三总判定：**FAIL**。

---

# 轴四 · 整体评估

## 4.1 总分：53 / 100

| 维度 | 满分 | 得分 | 扣分位置 |
|---|---:|---:|---|
| 来源利用与忠实度 | 30 | 20 | -4：六条 absorbed 与 target.sources 不一致；-3：why/context-engineering/DoD/figure-it-out 丢核心；-2：frontend UI 错并；-1：5 个 rejected 处置不成立。|
| 自洽与可执行性 | 35 | 18 | -5：P4/P5/P6 断链；-4：检查器语义互斥漏报；-3：13/49 skill 合同或来源失败；-3：8/9 role 有矛盾/越权；-2：A9 双 schema；-1：23 条死来源路径。|
| Governance 与冷启动 | 25 | 11 | -4：swarm 无 actor/object identity；-3：solo 文件负担不可判；-3：coldstart 两份协议冲突且复制漂移；-2：产物隐形膨胀；-2：tier 不可复算。|
| 可验证性与实战证据 | 10 | 4 | +3：三项 baseline gate 与生成防手改有效；+1：结构故障注入能抓部分错误；-6：没有真实任务行为评测，且最关键互斥注入漏报。|
| **总计** | **100** | **53** | |

这个分数不是对文案美观的评分；它反映“能否降低本来可避免的工程错误”。结构层明显进步，但几个错误会让工作流自己制造错误判断。

## 4.2 相对 v1.0.0-frozen：重建是否值：PASS（结构），实际质量是否已证明：FAIL

### 值得的部分

- 手写 1600 行 `SOURCES.md` 被 1036 行 registry + 文件系统扫描替代；
- 生成阶段/横切带/产物表，手改能被 `render --check` 拦；
- 角色从复制技能正文改成引用；
- 101 upstream skill 的目录闭包可机械证明；
- v1→v2 实际是 108 files、7077 additions、7303 deletions，可复现：`git diff --stat v1.0.0-frozen..v2.0.0`。

### 尚未证明的部分

- 结构漂亮没有阻止 P4 缺 A4、P5 改别人的 A3、A9 无对象身份；
- v1 的旧脚本仍留在 `scripts/`，新检查器看不到；
- 没有真实任务 A/B 或 coldstart 演练证据。

所以“重建方向值”是 PASS，“v2 已比 v1 更有效”仍是 FAIL。

## 4.3 最该改的三件事

### 1. 先修真正的闭环与对象身份

**位置：** `workflow/registry.yaml:244-281,153-184`、`roles/verifier.md:92`。

**为什么第一：** 这是会把错误候选上线的结构缺陷，不是文档瑕疵。

**怎么改：**
- P4.required_inputs 加 A4；
- A8 增加 `subject`（commit/patch/worktree digest）与 `scope`；P6 必须消费最终 A6/subject 并验证等值；
- A3 freshness 由 architect 产出新版本，或把 freshness 更新拆成 verifier 拥有的 evidence 字段，不能越权写 A3；
- 删除 P6 的甩锅硬规则，按原因路由。

### 2. 把检查器从“词形匹配”降级为诚实的结构检查，并补可判断言

**位置：** `scripts/check-consistency.py:42-72,183-270`、`README.md:24`。

**为什么第二：** 当前最危险的是全绿制造虚假安全感；故障注入已证明语义互斥可全绿。

**怎么改：**
- README 明说 S3 只抓精确词形，不声称“文件之间不打架”；
- 修 duplicate forbidden、hard-rule role mapping、`sk`/`sid`、`session`/`ephemeral` bug；
- S1 纳入 scripts；S2 校验 source path；新增 disposition.into ↔ target.sources 双向检查；
- 新增 artifact.consumers ↔ phase inputs/明确 optional-consumer 的 schema；
- 保留一个会红的 semantic injection fixture，不要靠扩大同义词表假装做语义证明。

### 3. 把 A9 与 coldstart 收敛成可并发、可复制、低负担的协议

**位置：** `workflow/registry.yaml:169-184`、`scripts/ledger.sh:44-56`、`scripts/log-decision.sh:1-47`、`docs/coldstart.md:38-50`、`skills/coldstart.md:40-50`。

**为什么第三：** 没有可靠日志和最小安装形状，多 agent 崩溃后无法恢复，solo 又会变成文档工程。

**怎么改：**
- 删除旧 logger/template，只留一个 schema；加入 actor/run/subject/phase；用锁或原子 append 服务，给并发夹具；
- 定义 solo compact layout（建议一个 task packet + 一个 ledger，A3 为项目级复用），明确最大新增文件数；
- 统一 coldstart 对 render.py 的说法；提供一次真实空仓安装 fixture；
- 不复制整库到每个下游；采用固定 release snapshot + 很薄的本地 binding，或明确升级/迁移协议。

## 4.4 现在能否做 UCBIP 真实试运行：FAIL

不能直接做真实试运行。最低放行条件：

1. 上述第 1 项对象绑定与 P4/P5 闭环修复；
2. A9 单 schema + actor/run/subject + 并发验证；
3. semantic contradiction fixture 不能全绿，或者文档诚实降级并加人工 gate；
4. 用一个 disposable 小仓跑完 coldstart + solo，再用一个跨边界任务跑中/大档；
5. 原实现正确、环境损坏、候选在 PASS 后改变、agent 中途崩溃四个反例都得到预期结果。

完成这些后可以做**受控 pilot**，仍不等于全量放行。

---

# 故障注入结果（汇总）

- 改坏 registry：红，PASS。
- 加游离 skill 文件：consistency 红，PASS。
- 删一条 disposition：closure 红，PASS。
- 手改生成文件：render 红，PASS。
- 造受控词形完全相同的互斥句：consistency 红，PASS。
- 造语义明确但词形不同的互斥句：两个 checker 全绿，**FAIL，且为本次验收最严重发现**。
- 重复 forbidden：两个 checker 全绿，FAIL。

---

# UNVERIFIED 项与补证条件

1. **A9 在 UCBIP 实际共享文件系统上的并发原子性：UNVERIFIED。** 本机 APFS 20×100 并发未复现丢行；需要在 UCBIP 实际文件系统、实际 shell、长行与进程崩溃条件下跑夹具。
2. **49 个技能对真实任务的行为增益：UNVERIFIED。** 本报告验证了文本可执行性、来源与契约，不等于验证 agent 行为。需要固定模型/工具/预算的 baseline vs TIM 对照。
3. **三档位实际成本：UNVERIFIED。** 规范不给确定文件布局/角色 rubric；先补 compact layout 与触发矩阵，再测时长、文件数、返工率。
4. **具体 harness 的权限隔离与消息可靠性：UNVERIFIED。** README 只给四项粗能力；需实际验证 session isolation、ACK/identity、write window、candidate binding、crash recovery。
5. **上线/回滚真实性：UNVERIFIED。** 没有目标部署环境与授权，本次只审文本和脚本，未执行发布。

---

## 最终判定

| 轴 | 判定 |
|---|---|
| 轴一 来源利用率 | FAIL |
| 轴二 自洽性 | FAIL |
| 轴三 Governance | FAIL |
| 轴四 可试运行性 | FAIL |
| v1→v2 重建方向 | PASS |
| 当前 tag 直接用于 UCBIP | FAIL |
