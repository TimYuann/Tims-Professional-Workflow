# TPW 工程方法 · 本机自用固定成品批

本目录是 TPW 既有方法的原生成品批：**32 个能力入口**（一个能力方法一个入口）＋ **1 个非自动的按需导引根**（`tpw-on-demand-guides`）。正文逐字节取自 TPW 固定方法集，供宿主按固定对象安装使用。装配顺序、Profile/Charter/authority（`professional-workflow/`）**不是**技能入口，仍由 TPW 包自身承担。

固定身份：源仓 pin `f5d6d0547459eb15c40aec25617418d5ea4710e6`，tree `9d7c057417da73895cda3b85ec34d49db58669b6`。每个入口的 `SKILL.md` ＝ frontmatter ＋「包装与资源边界」一节 ＋ 该方法正文的**完整字节**。逐文件校验值见各根 `SOURCE.md`。

命名规则：`tpw-` ＋ 方法文件名干；唯一例外 `tpw-debug` ← `local-defect-feedback-loop.md`（既有已安装固定身份，不改）。

## 入口清单（32 个能力入口）

| 入口 | 方法正文 | 随包读取资源 |
| --- | --- | --- |
| `tpw-agent-facing-cli-contract` | `professional-workflow/methods/agent-facing-cli-contract.md` | — |
| `tpw-architecture-survey` | `professional-workflow/methods/architecture-survey.md` | guide-check-design.md, guide-lesson-promotion.md, guide-agent-text.md, guide-professional-explanation.md, guide-redacted-evidence.md |
| `tpw-behavior-claim-evaluation` | `professional-workflow/methods/behavior-claim-evaluation.md` | guide-redacted-evidence.md, guide-test-evidence-quality.md |
| `tpw-behavior-contract-examples` | `professional-workflow/methods/behavior-contract-examples.md` | — |
| `tpw-behavior-preserving-change` | `professional-workflow/methods/behavior-preserving-change.md` | guide-change-shape.md |
| `tpw-bounded-composition` | `professional-workflow/methods/bounded-composition.md` | guide-check-design.md, guide-lesson-promotion.md, guide-agent-text.md, guide-professional-explanation.md, guide-redacted-evidence.md |
| `tpw-bounded-prototype` | `professional-workflow/methods/bounded-prototype.md` | — |
| `tpw-change-review` | `professional-workflow/methods/change-review.md` | guide-agent-text.md, guide-professional-explanation.md, guide-redacted-evidence.md |
| `tpw-change-slicing` | `professional-workflow/methods/change-slicing.md` | — |
| `tpw-cross-module-design` | `professional-workflow/methods/cross-module-design.md` | guide-mock-adapter-choice.md（＋既有 `design-alternatives.md`，固定身份） |
| `tpw-debug` | `professional-workflow/methods/local-defect-feedback-loop.md` | guide-redacted-evidence.md, guide-test-evidence-quality.md |
| `tpw-decision-elicitation` | `professional-workflow/methods/decision-elicitation.md` | behavior-claim-evaluation.md, guide-redacted-evidence.md, guide-test-evidence-quality.md |
| `tpw-decision-record` | `professional-workflow/methods/decision-record.md` | — |
| `tpw-deprecation-and-migration` | `professional-workflow/methods/deprecation-and-migration.md` | — |
| `tpw-design-alternatives` | `professional-workflow/methods/design-alternatives.md` | guide-mock-adapter-choice.md |
| `tpw-domain-language` | `professional-workflow/methods/domain-language.md` | — |
| `tpw-domain-state-and-invariants` | `professional-workflow/methods/domain-state-and-invariants.md` | — |
| `tpw-external-tool-operation` | `professional-workflow/methods/external-tool-operation.md` | guide-positioned-artifacts.md, guide-redacted-evidence.md |
| `tpw-handoff-and-resume` | `professional-workflow/methods/handoff-and-resume.md` | guide-redacted-evidence.md |
| `tpw-human-procedure` | `professional-workflow/methods/human-procedure.md` | guide-redacted-evidence.md |
| `tpw-interface-contract-and-retry` | `professional-workflow/methods/interface-contract-and-retry.md` | — |
| `tpw-merge-conflict-resolution` | `professional-workflow/methods/merge-conflict-resolution.md` | — |
| `tpw-observability-design` | `professional-workflow/methods/observability-design.md` | guide-redacted-evidence.md |
| `tpw-performance-and-neutrality` | `professional-workflow/methods/performance-and-neutrality.md` | — |
| `tpw-professional-learning` | `professional-workflow/methods/professional-learning.md` | guide-professional-explanation.md, guide-redacted-evidence.md |
| `tpw-quality-policy-enforcement` | `professional-workflow/methods/quality-policy-enforcement.md` | — |
| `tpw-rationale-and-premise-review` | `professional-workflow/methods/rationale-and-premise-review.md` | — |
| `tpw-release-and-recovery` | `professional-workflow/methods/release-and-recovery.md` | — |
| `tpw-test-first-behavior-slice` | `professional-workflow/methods/test-first-behavior-slice.md` | guide-mock-adapter-choice.md, guide-test-evidence-quality.md |
| `tpw-trust-boundary-and-actions` | `professional-workflow/methods/trust-boundary-and-actions.md` | guide-redacted-evidence.md |
| `tpw-uncertainty-planning` | `professional-workflow/methods/uncertainty-planning.md` | — |
| `tpw-verification-harness-design` | `professional-workflow/methods/verification-harness-design.md` | guide-check-design.md, guide-lesson-promotion.md, guide-agent-text.md, guide-mock-adapter-choice.md, guide-professional-explanation.md, guide-redacted-evidence.md, guide-test-evidence-quality.md |

## 资源携带规则（实际依赖 vs 指针 vs 锚）

每个入口只保证**随包资源**能从该入口目录内取回；正文里其余两类路径不携带、也不要求读：

1. **读取型资源 / 实际条件依赖（随包）**：正文按文件名指向、且属于“实际读”的资源——含传递的 guide→guide 引用，以及已核的非 guide 依赖（如 `tpw-decision-elicitation` 正文要求使用 `behavior-claim-evaluation.md` §Use，故整份随包）。**不因文件名不是 guide 而断闭包。**
2. **边界指针（不随包）**：正文只做职责归属（如 `bounded-composition` 标注 “pointer only” 的 `handoff-and-resume.md`、`rationale-and-premise-review` 的互指 `local-defect-feedback-loop.md`、`architecture-survey` 词表锚 `cross-module-design.md`），不携带；按本批同名入口取。
3. **上游来源锚（不随包）**：正文 Source anchors 段中的上游路径，属出处记录。

**来源与许可口径**：每根的 `SOURCE.md` 来源表与 `THIRD-PARTY-NOTICES.md` 都按**该根本正文 ＋ 全部随包资源**的来源**并集**生成（不只看主方法的 Source anchors）。例：`tpw-architecture-survey` 主方法只涉 Matt，但随包的 `guide-redacted-evidence`／`guide-agent-text`／`guide-lesson-promotion`／`guide-professional-explanation` 涉及 pstack 与 cursor-team-kit，因此其 NOTICES 覆盖 Matt ＋ pstack ＋ cursor-team-kit 三份 MIT；SOURCE 表逐项标出“出现于”哪些文件。

`tpw-on-demand-guides/` 是非自动的按需导引根（`disable-model-invocation: true`，只能显式调用）：携带 9 份导引，供未被任何入口按依赖携带时按需读取；`guide-positioned-artifacts.md` 不在其中，它随其声明的依赖入口 `tpw-external-tool-operation` 携带。**固定批内十份导引全部可取**（逐份出现在至少一处：本根或对应入口）。

## 安装（本机自用）

宿主侧步骤，目的是默认发现只有一份、且指向不可变内容：

1. **把本目录整体复制到自动发现根之外的版本目录**，例如 `~/.agents/skill-versions/tpw/<包装提交>/skills/`。版本目录一旦建立即视为不可变；更新＝建新版本目录。
2. **只把选定入口指向该版本目录**（复制入口目录，或让入口指向版本目录内的同名根）；**不要指向源仓工作树或当前 `main`**。
3. **旧版与备份不要放进技能扫描树**，否则会形成第二个默认入口；旧版按版本目录保留在扫描树外，旧任务按固定对象取回。
4. 取包示例：`git archive <包装提交> skills/ | tar -x -C <版本目录>`。安装前先读目标入口的 `SKILL.md` 与 `SOURCE.md`；本批默认不执行任何脚本。

**路径注意**：入口的技能目录可能被宿主以 symlink 别名（`~/.agents/skills/<name>`）指向版本目录。因此本批**只使用入口目录内部的相对资源**（入口声明资源 + 随包副本），不依赖 `../` 跨目录或 symlink 别名推断；公共导引以 `tpw-on-demand-guides` 这一独立根内的副本提供。

## 旧任务版本不漂移

- 任务引用一律写**固定对象**：包自身提交（`git log -1 --format=%H -- skills/`）或本包记录的 pin／tree／路径；不写“最新 main”。
- 需要旧版本时按版本目录取回，不改进行中的任务；升级＝新固定对象＋重新核受影响的引用。

## 许可边界

- **本机自用**：Neil 于 2026-10-11 授权在本机安装／使用本成品。
- **公开发行**：未授予许可。上游 MIT 条款不用于推断 TPW 自有融合增量的条款；正式对外分发前须由 Owner／TPW 维护者确认。
- 上游许可原文见各根 `THIRD-PARTY-NOTICES.md`（按该正文 Source anchors 识别出的来源取子集：Matt／Addy／pstack／cursor-team-kit，四份 MIT 已与各上游 `LICENSE` 逐条核对）。

## 静态检查（已执行，可复跑）

| 检查 | 方法 | 结果 |
| --- | --- | --- |
| 正文逐字节 | 32 个能力入口的正文段后缀 SHA-256 与源方法文件比对 | **32/32 一致** |
| 资源逐字节 | 50 份随包资源副本（guide 副本 + 非 guide 依赖副本）与来源比对哈希 | 一致 |
| 读取闭包 | 扫描入口自身与随包副本中的 `methods/<name>.md` 引用，断言在入口目录内可取回 | 无闭包缺口：唯一剩余的一处是 `tpw-debug` 正文的 Source 括注（来源锚，非读取依赖） |
| Markdown 链接 | 扫描 `skills/` 下全部 Markdown（151 个）的显式相对链接，剔除行内代码跨度示例 | 真链接 **1/1** 可解析（`tpw-cross-module-design/references/DEEPENING.md` 的 `../SKILL.md`；上游 `f3dd099c…`／包装 `5176f5fc…`，属既有固定身份） |
| Bash 语法 | `bash -n tpw-debug/scripts/hitl-loop.template.sh` | 通过（未执行） |
| 入口发现 | 宿主静态解析（`loadSkillsFromDir`） | **33 入口 / 0 诊断**；其中 1 个标 `disable-model-invocation`（按需导引根）；描述均 ≤1024 字符 |
| NOTICES | 每根按「本正文 ＋ 随包资源」的来源**并集**生成、非空，并与上游 `LICENSE` 逐条核对 | **33/33** |
| 尾随空行 | `git diff --cached --check`（新增文件） | 通过，无 EOF 多余空行 |

未执行：HITL 模板、任何产品命令、任何网络或安装动作。

## 已知残差与未定（不兜底）

1. **`tpw-debug` 的那处方法引用是来源锚，不是读取依赖**：正文 Root cause 段 “When stuck, instrument rather than guess” 一行的括注写作 `*(Source: same file; methods/behavior-claim-evaluation.md.)*`——它是出处标注，不要求 caller 去读，因此**不构成闭包缺口**，也不在入口内加副本；该能力本身由本批 `tpw-behavior-claim-evaluation` 入口提供。
2. **`tpw-architecture-survey`／`tpw-bounded-composition`／`tpw-verification-harness-design` 的 `guide-check-design` 携带**依据 UCBIP `docs/active/engineering-method-routing.md` 的两个组合消费行（“症状明确、原因不明”与“改动非局部／修复位置有争议”）；其余组合关系未验证。
3. **需求侧未验证**：多数入口在 UCBIP 旧链无引用，本轮属“整体成果”覆盖；不称全完成，不把 32 个入口当作需要全员同时读或自动激活。
4. deferred 分支不晋升：`DESIGN-IT-TWICE` 与其并行 agent 数、S2 playbook 的控制/循环/模型/PR 默认、idempotency／retention 规则、`interrogate`／`code-review` lenses，均不随包。
