# ABSORB-DRAFT-DBG-05 · 脱敏取证（redact-first evidence）· 草案候选

**状态：草案候选（未采纳、不产生 authority / 生成器 / gate）。** rev.2：按 `ABSORB-METHOD-FOLLOWUP-REVIEW.md` FM-2 修正默认示例（脱敏先于落盘，raw 为独立显式边界）并按 suggestion #2 校正 step 描述。

- 授权：Owner 2026-10-01 有界起草授权（只写 `docs/overnight/`，不碰 `professional-workflow/`）；口径见 `ABSORB-PRO-REVIEW-RESPONSE.txt` 第四节、`ABSORB-PRO-REVIEW-DISPOSITION.md`、`ABSORB-FULL-CORRECTION-BRIEF.md` §2。
- 写集：仅本文件。未改任何 active 方法 / Profile / Charter / Backbone；未新建注册表、脚本、校验器或 gate；未提交、未发布、未运行脚本或测试。
- 性质：静态源核验后的知识候选；不声明运行时强制力；不产生未来改对象、加检查或删规则的权限。
- 拟接点（仅记录，未施工）：`professional-workflow/methods/local-defect-feedback-loop.md` §Method 5 与 `professional-workflow/methods/behavior-claim-evaluation.md` §Method 2 的取证／记录处；候选集成口径见 `ABSORB-CANDIDATE-METHOD-INTEGRATION.md`。

## 0 · 固定源核验（只读）

| 源 | pin（HEAD == pin，已核） | 文件 | blob |
| --- | --- | --- | --- |
| mattpocock-skills | `c55ee46073ed923f86ce59a5eb3b6d895095d1b7` | `skills/engineering/diagnosing-bugs/SKILL.md` | `061c25a524acaa93d4534e9e08a793c0a5fe45fd` |
| mattpocock-skills | 同上 | `skills/engineering/diagnosing-bugs/scripts/hitl-loop.template.sh` | `243198464a8401a7ba1d63b3708fa43c3d067665` |
| cursor-plugins | `ecc249f1e306fc64ddf83c7bed16cacf7c2239db` | `cursor-team-kit/skills/verify-this/SKILL.md` | `54bcf49ad0cc6256a90750fdbec7e27f79eb3d39` |

上游工作树 `git status --porcelain` 为空；无 checkout、无写入、无脚本执行。定位根：`.worktrees/legacy-pre-night-2026-10-01/upstreams/`。

## 1 · 候选正文（草案措辞；不是已接受字节）

> 以下只是候选措辞的行文参考。若未来采纳，需先有独立编辑决定与新的接受记录；本草案不自行落入 active 方法。

1. **脱敏先于展示、记录或保存**：秘密写 `<REDACTED>`；回路尽量让凭据从环境变量进入，使命令文本本身不含明文。env var 只解决命令文本，不解决响应内容/捕获工件的保管。
2. **默认只处理已获准的最小脱敏证据**：不新增 raw 落盘；只引用承载信号的行（状态行、错误码、请求 ID 等）。
3. **敏感工件保存边界**：工件可能含敏感代码、提示、截图、HTTP body 或 heap 数据时，默认只保留最小化行内证据；除非用户同意，不落盘。
4. **需要 raw 时是独立显式边界**，须同时满足：既有有效同意（记录在案）；受限工作区位置（如 `<workspace>/.worktrees/verification/…`，不提交）；保管/清理边界（谁可读、何时删除或过期）；工件不含 secrets、真实用户数据；不使用活网络调用（本地脱敏 fixture 或既有记录）。
5. **人手操作与回显捕获分开**：只能由人执行的动作走 step（动作留在用户自己的流程；脚本只提示并等待，不采集该动作，也不宣称技术屏蔽终端回显）；可安全回显的观察值才走 capture——capture 的值会打印回终端供 agent 解析，因此凭据不得走 capture。
6. **脱敏后信号不足时**，如实说明不足并请求替代证据（可复现环境访问 / 脱敏后的捕获工件 / 临时插桩许可）；不为"完整"回填明文。

## 2 · 条文明细（每条：源 pin+路径+章节锚点 / 适用条件 / 例外 / 反例）

### DBG-05.1 脱敏先于取证，并保留诊断信号

- **源锚点**：matt `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`，`skills/engineering/diagnosing-bugs/SKILL.md` §`Redact`（L12–16）。
- **规则**："Redact every secret first"，秘密写 `<REDACTED>`；命令/回路用 env var 注入凭据；捕获工件（含认证头）只引用带信号的行。
- **适用条件**：证据将离开当前上下文（落盘、提交、跨 agent/评审交接、进日志或展示）之时。
- **例外**：脱敏后不足以诊断时（同文件 L16），说明不足并向用户求助，而不是默默继续或回填明文。
- **反例**：为"完整"把含 `sk_live_…` 的原始命令与 `Set-Cookie` 全量响应头写入证据并提交；诊断信号并未因此增加，秘密却被固化。

### DBG-05.2 脱敏不足的处置（请求替代证据）

- **源锚点**：matt 同上 pin，`SKILL.md` §`When you genuinely cannot build a loop`（L53–56）；§Phase 1 "Completion criterion"（L59："show the invocation and its output, redacted"）。
- **规则**：请求 (a) 可复现环境访问、(b) 脱敏后的捕获工件（HAR file / log dump / core dump / 带时间戳的录屏）、(c) 临时生产插桩许可；不引入明文。
- **适用条件**：脱敏使信号不可判读，或回路根本无法构造时。
- **例外**：无；这是"先说明不足"的出口，不是回填明文的许可。
- **反例**：把"exact commands"读成"必须原样粘贴含明文密钥的输出"；或把整段响应体删光后再声称"无法诊断"。两者都可用本条出口替代。

### DBG-05.3 敏感工件保存边界

- **源锚点**：cursor `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`，`cursor-team-kit/skills/verify-this/SKILL.md` §`Artifact Layout`（L37–51，L51 为边界句）；§`Local Surfaces`（L28–35）给出工件种类。
- **规则**：仅在"安全写工件"时使用 baseline/treatment/diff 布局；工件可能含敏感代码、提示、截图、HTTP body 或 heap 数据时，默认只保留最小化行内证据；除非用户同意，不落盘。
- **适用条件**：决定 baseline/treatment 工件是否落盘、落盘哪些子集、是否进入仓库证据面。
- **例外**：用户明确同意可落盘（并约定受限位置）；最小化行内仍是默认。
- **反例**：把含真实客户 PII 的 HTTP body 原样存进 `baseline/` 并提交，只为"对比方便"。

### DBG-05.4 raw 的独立显式边界（自拟操作，非源文照抄）

- **源锚点**：桥接来源为 verify-this L51（"unless the user agrees to disk storage"）与 §Redact L14（凭据留在环境）；五条件本身是本草案的工程展开，标注为 authored，不冒充上游正文。
- **规则**：默认路径不产生 raw；确需保留 raw 时，独立分支同时满足 §1 第 4 条五条件（既有有效同意 / 受限位置 / 保管清理 / 无 secrets 与真实用户 / 无活网络）。
- **适用条件**：最小脱敏证据确实不足以定位缺陷，且已存在有效同意时。
- **例外**：任一条件不满足即回到默认路径或走 DBG-05.2 出口；不得以"调试需要"自我授权。
- **反例**：为图省事把完整 headers/body 先落到临时目录再慢慢脱敏——落盘一旦发生，保管边界已被绕过（FM-2 所否决的正是这种默认路线）。

### DBG-05.5 step 与 capture 的真实差异

- **源锚点**：matt `c55ee460…`，`scripts/hitl-loop.template.sh` 头注 L13–16 与 `step()`/`capture()` 实现 L20–31（示例 L34–38）；同 pin `SKILL.md` §Phase 1 item 10（L35，HITL 为 last resort）；§Completion criterion（L64："a human in the loop only via `scripts/hitl-loop.template.sh`"）。
- **规则**：只能由人做的动作走 `step`（脚本提示并等待 Enter；动作留在用户自己的流程）；可安全回显的观察值走 `capture`；capture 值打印为 KEY=VALUE 供 agent 解析，故凭据/口令/token 不得进入 capture。
- **适用条件**：复现必须经过人手（登录、受限环境、硬件操作）。
- **例外**：HITL 是最后手段——优先 agent-runnable 回路；均不可得时按 DBG-05.2 出口索取替代证据。
- **反例**：`capture PASSWORD "Enter your password:"` 会让口令回显给 agent 并进入 KEY=VALUE 输出；应为 `step "Sign in at …（凭据在你自己的终端输入）"`，只 capture 是否成功/错误消息。注意：step 不采集值，但脚本并不技术屏蔽用户终端自身的回显，不得据此宣称登录行为"自动不回显"。

### DBG-05.6 与现有正文的关系（不否定现有基础）

- **源锚点**：当前 core `91875114e51855517f92ef099cbdf60c34e68243`，`professional-workflow/methods/local-defect-feedback-loop.md` §Method 5；`professional-workflow/methods/behavior-claim-evaluation.md` §Method 2。
- **规则**：现有"如实记录 / preserve original output"保持有效；本候选增加顺序（先脱敏再保留）、工件保管边界与 step/capture 分流。"exact commands" 允许命令文本逐字记录（凭据来自 env var 时文本不含明文），不等于无条件落盘带秘密的原始输出。
- **适用条件**：仅证据记录/保存点，不扩成通用 gate。
- **例外**：无（消费口径澄清）。
- **反例**：把现有正文读成"必须把原始机密输出落盘"，是过度解释；Pro 审核已否定该读法。

## 3 · 可区分正误的具体例子（草案自拟，非源文例子）

场景：复现"支付请求在生产返回 401、开发环境正常"。默认可用的只有既有授权步骤已产生的最小脱敏记录（工作区文件 `evidence/dbg05/redacted-http.txt`，内容为信号行）：

```text
POST /v1/charges
Authorization: Bearer <REDACTED>
HTTP/1.1 401 Unauthorized
www-authenticate: Bearer realm="api"
x-request-id: 7f3c…
```

- **默认正确路线**：不新增采集、不写 raw，只读上述已获准的最小脱敏证据。可支持 `401`（认证未被接受）与 `411 missing content-length` 的区分；`www-authenticate: Bearer` 只说明期望的认证方案，**不能**由 401 单独推断 bearer 被拒的原因（过期/撤销/scope 不足）。要区分原因，需另取获准的脱敏错误码（如 `error=token_expired`）或另行授权探测，而不是取用原始 token。
- **错误路线（FM-2 所否决）**：先 `curl -D <workspace>/headers.txt -o <workspace>/body.json` 把完整响应头/体写盘，再事后 `grep` 信号行。即使命令用 `$AUTH_TOKEN` 避免文本明文，响应内容（Set-Cookie、body）已在获准边界之外落盘；"只显示少数行"不等于没有保存原始敏感 bytes。
- **raw 分支（独立显式边界）**：仅在 §DBG-05.4 五条件全部满足时，把必需子集写入受限位置，如 `<workspace>/.worktrees/verification/dbg05-raw/`（不提交、不复制进 `docs/overnight/` 或工单文本），并在使用后按保管/清理边界删除或过期。本草案不实现该分支。

## 4 · 适用边界与不主张

- 不主张运行时强制力：host/hook/上传链是否真的执行脱敏，未验证；写入步骤 ≠ 已发生效果。
- 不新增 validator / 常备清单 / 生成器 / gate；不要求特定脱敏工具或函数；raw 分支不是新权限。
- 不扩大任何任务权限、不替代 Charter 的工具/动作段。
- 源与自拟区分：§1.1–3、§1.5 分流有源锚；§1.4 五条件、§3 的 401 推断限制与覆盖边界展开为自拟工程展开（authored）。§3 示例整体为自拟，不因源表正确而自动正确。

## 5 · 源锚点汇总

| # | 源 pin | 路径 | 章节/行 | 提供 |
| --- | --- | --- | --- | --- |
| 1 | c55ee460… | skills/engineering/diagnosing-bugs/SKILL.md | §Redact L12–16 | 脱敏先于取证、env var、信号行、不足时求助 |
| 2 | c55ee460… | 同上 | §Phase 1 item 10 L35 | HITL 为最后手段 |
| 3 | c55ee460… | 同上 | §When you genuinely cannot build a loop L53–56 | 替代证据出口（环境/脱敏工件/插桩） |
| 4 | c55ee460… | 同上 | §Completion criterion L57–66 | 展示 invocation + redacted 输出、人只在 script 内 |
| 5 | c55ee460… | skills/engineering/diagnosing-bugs/scripts/hitl-loop.template.sh | 头注 L13–16 | capture 会回显、登录留给 step |
| 6 | c55ee460… | 同上 | step()/capture() L20–31、示例 L34–38 | 两种助手与 KEY=VALUE 回传（不屏蔽终端回显） |
| 7 | ecc249f1… | cursor-team-kit/skills/verify-this/SKILL.md | §Artifact Layout L37–51 | 敏感工件默认行内、落盘需用户同意 |
| 8 | ecc249f1… | 同上 | §Local Surfaces L28–35 | 工件种类（HTTP 响应、截图、heap 等） |
| 9 | core 91875114… | professional-workflow/methods/local-defect-feedback-loop.md | §Method 5 | 现有"exact commands/observations"基础与接点 |
| 10 | core 91875114… | professional-workflow/methods/behavior-claim-evaluation.md | §Method 2 | 现有"preserve original output"基础与接点 |

## 6 · 残余

- 本次只读固定源与当前正文；未运行 hook、未验证宿主是否加载、未测试任何真实脱敏工具，raw 分支未实现。
- 其他同族材料不在本草案声称范围内；本草案不代表 DBG-05 之外候选的源评估完成。
- 若未来采纳，仍需独立编辑决定与接受记录；本文件存在不等于 PASS 或授权。
