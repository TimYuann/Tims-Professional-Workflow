# Gate2 · B3 首批七文件与 016e004 增补

2026-10-02，tpw-absorb-gate2，非候选作者；首读 B3，不重置其他 B 的轮次，不重复 Oracle CD/DEF3 源裁定。

对象：初始 `7e9e4dae5ec43592eceadbbb8f1b93247bfc9c29`，唯一父/base `d3aab6ad30f36789664287f304e4e91ffd61d96a`；增补 `016e00402c0cc29aee3556186a6cc425de746951`，唯一父即 7e9e4da，core tree `8cf0e7c53ecc54c4fe9bf19b09249894f3916303`。初始七新文件 +772，增补仅 interface/trust 两文件 +55/-12。git diff --check base..016e004 无输出；正文全部按 git show/diff 固定读取，没有读 B3 mutable 更新。

**结论：quality-policy-enforcement、observability-design 整文件专业正文 PASS；其余五文件需下列定向修复。J1/J5 增补实质通过，不建 guide-boundary-contract-checks 的比例性成立；整体 B3 暂不可全采用。** 技术经验并非因源代码或宿主耦合被拒绝。覆盖与采纳、正文与运行资格分开。

## 逐机制复核

| 机制 / 落点 | 覆盖及处置 | 保留内容、边界、需修 |
| --- | --- | --- |
| C1 interface-contract-and-retry | 限缩吸收的实现基本齐；B3-C1-scope 待修 | caller-visible 输入/输出/错误/partial/list/dependency inventory；信任看 writer；一次意图 UUID 合法；原子 claim、payload 绑定、在途重复、unknown 调和及最长 replay retention 有揭错反例。UNIQUE 不推出跨 provider exactly-once。接口章节的适用性不应被整个方法“必须有 retry”排除。 |
| J1 同文件 §3 | 增补 PASS，合并落地 | variants/enums、跨字段引用/环/重名、字段路径修复、旧字段迁移；closed vs extensible、regex 不等 containment/权限、关系不等独立性；runtime refine 与生成 JSON schema 分开，容错读取披露缺失，不宣称全终止。源脚本不搬入。 |
| C3 deprecation-and-migration | 限缩落地大部齐；B3-C3-data 待修 | 活消费者/未文档依赖、cost、advisory/compulsory、迁移选择、无活消费者纯退役、Owner 终止能力、provenance 保全、不可逆恢复/forward-fix 均保留。expand/contract 例仍缺混跑写入边界，“adds safe in any deploy”过度承诺。 |
| C4 release-and-recovery | 限缩落地大部齐；B3-C4-recovery 待修 | deployed/enabled/accepted/shutdown、四部恢复计划、baseline 比较三决策与 burn rate、数字只作源例、无流量不造 canary、flag owner/清理、通知与部署沿实际授权正确。不能把不可分离 enablement 推成无 recovery。 |
| C5/G5 quality-policy-enforcement | 合并/限缩落地 PASS | policy 与 task criteria 分开、owner 可修政策；detect/cite、指标理由/命令、enforced/measured、成本/coverage 放置、五类放松、可选 ratchet 与例外；regex 只线索，合法删测/suppression 可成立；external 结果在后段明确非不容争辩；0/1/2 分开，不移植 floor-guard，不新建库 validator。 |
| C6 trust-boundary-and-actions | 限缩落地大部齐；B3-C6-policy 待修 | writer/STRIDE/abuse、AskFirst 可有效预委托不一律 Human、derived path 三条件/marker可伪造/TOCTOU、SSRF rebinding、供应链版本/审查/audit 不等 trust 均具体。隐私与 prompts 两段仍与自己的不采条款冲突。 |
| J5 同文件 operator/channel | 增补 PASS，合并落地 | argv/env/cwd/workspace 不自动可信，OS home/non-symlink uid 0600 不能区分同 UID 可写 home；plan schema 不认证目标，受信配置/有效授权与 half-config 早失败；结构编码不防自然语言注入；probe accepted 非 completed、吞 cancel 非 stopped/zero-use，测试绿非全身份安全。 |
| C7 observability-design | 限缩落地 PASS | 运行问题→signal、ID 与 entry point 同传播、bounded labels、平均与尾分布分工、symptom/action/runbook、实际触发看 telemetry；source count/JSON/OTel/tier 不升普遍政策；alert test-fire 明确有效许可、无测试通道如实缺证、不发真实渠道凑绿。 |
| C9 performance-and-neutrality | 限缩落地大部齐；B3-C9-source 待修 | baseline/因果/条件重复/噪声、症状树、query/pool/cache 成本、correctness、neutral 非产品 FAIL、其他已接受目的可保、attempt ledger、数字非 SLO 正确。Chrome 引用把预期 rollout 改成已完成，需修归因。EF-addendum 未裁细支线仍不假称已吸收。 |

## 新 findings：最小修，不重建方法

### B3-C1-scope · 接口与 J1 的独立适用面

Use 与 Conditions 都把无 retry/duplicate 路径的操作排除整个方法。一个只读列表接口仍有 pagination/错误契约；一次性导入图仍有结构/语义验证。§1–3 的经验与 Oracle 落点不依赖重试。

限定排除的是幂等/重试支线，接口/验证章节按其实际边界问题独立选用；不因此要求所有稳定内部函数写 API 文档或配置幂等键。无需新文件/平台。

### B3-C3-data · 添加安全与混跑写入

Persistent data 的 Rules 写 “Adds are safe in any deploy”，而 backfill 例只说 app dual-write 后 deploy、复制旧列、切读。添加 nullable 字段/索引仍可能锁表、改变查询/资源成本；正文另要求测 lock 并未撤掉安全保证。

混跑反例：新实例写双列，旧实例仍只写 name；backfill 复制之后旧实例又改 name，full_name 陈旧，切读兑现错值。须明确在开始依赖新字段前，所有相关活跃 writer/旧版本/后台任务均已兼容，或有能说明的协调/追赶方案；回填与并发更新防旧覆盖、切读前核一致、contract 前核读与写依赖/回退版本。不是强制某一工具或始终双栈，而是声明该例成立条件。将 adds 安全改为相对兼容策略，仍核实际 engine/锁/资源影响。

### B3-C4-recovery · 分離启用不是恢复能力的普遍前提

Preconditions 1 把不能分离 deploy/enable 推成 incremental rollout **and recovery** 不可用；后文自己列 redeploy previous version。反例：小服务原子切换完整 release，没有 flag，仍能在有效授权下重新部署兼容旧 artifact 并观察恢复。

分别说明缺少何种 staged/flag-off 能力与实际可用 redeploy/forward-fix/数据恢复；未演练保持计划/未核，不伪造 canary，也不宣称一律无 recovery。保 baseline 与真实恢复观察。

### B3-C6-policy · 不采边界仍在操作正文回流

Personal data 写 delete including backups、consent gates collection/share；Model output/prompts 写 keep full system prompt out of context。后面的 What is not adopted 又否认 mandatory backup deletion/blanket prompt ban。消费者执行主段会先遇到这些绝对命令，末尾 disclaimer 不能作相反规则的修复。

隐私要求按有效目的/保留/合法依据/权利义务处理各副本，不默认所有合法留存都必须删除备份，也不替专业 authority 决定 consent 是唯一依据；仍保最小化、findable/erasable 与 telemetry 禁泄露。prompt 保护秘密/跨租户及不该暴露政策信息，合法系统提示可以进入本来需要它的上下文；结构输出按边界 parse/validate/encode，不把模型输出永不得作合法路径/查询参数当作 sink 处理后仍禁用。无需法律/SDK 全域认证来修这些已裁限缩。

### B3-C9-source · 官方文档的预期不等完成

候选写 Chrome “completed the rollout in March–April 2025”。本次实际取回官方页（Published 2024-10-21 / updated Sep 9, 2025）写 **expected to reach 100% in March and April 2025**，不是 rollout 完成记录。Chrome 116 实验、cookie/授权变化 eviction、WebSocket/WebTransport/WebRTC、no-store fetch、三分钟、enterprise opt-out 与其他浏览器可能仍阻止均有文档支持。

最小修：忠实记“官方页记载自116实验，并预期于2025年3–4月达100%”；若要“已完成”另补直接完成依据。保版本/vendor 限度、不得为性能绕安全缓存政策；无需运行浏览器实验，也不把文档当目标用户实际收益。

## 不建 guide 的比例性

**成立。** Oracle J1 只说必要时可按需 support，不要求新 guide。现有 interface §3 和 domain-state 的不同消费者分别承载接口操作与非法状态例；再建通用 boundary-check guide 目前无独立需求，会重复主规则。保两正文相同结构/语义界限与合法 diagnostic 读取即可；这不是拒绝代码机制或给 helper 预设禁止。将来确有独立消费/版本细节再按真实准入判断。本次不新建 validator/runner，也不要求 Charter JSON。

## 回源、对象与限制

依据 Oracle CD 与 DEF3 固定裁定，未重裁源机制。直接回核 Addy API Contract First、boundary/idempotency/retention；deprecation decision/process/patterns/expand-contract；shipping flag、stage/threshold/rollback；constraint lifecycle/five moves/ratchet 和 floor-guard Contract；security privacy/LLM 与 hardening-patterns SSRF/derived-path/audit；observability questions/ID/entry point 与 telemetry；performance bottleneck/cache/verify/neutral/ledger。只称实际章节读取，不称全仓/所有支持文件全读。Cursor schemas 的 Plan refine/部分读取、prompts template、util operator 477–513、tools/probe-models 与 tools/generate-json-schemas 正文及 plan.schema.json 的生成结构回核，未运行脚本。

Chrome 官方页通过 agent-reach/Jina Reader 实际取回至 `/tmp/tpw-gate2-bfcache.txt`，URL `https://developer.chrome.com/docs/web-platform/bfcache-ccns`；仅其页面陈述被核，不推断全部浏览器当前行为。无 Provider/业务/安全/性能效果实验，正文通过不授部署/删除/发送权，不宣称 fresh-reader 或整体接受。上述最小修无仍缺承重读源；扩展实际 SDK/engine/当前平台保证须再核相应版本与执行观察。

Driver 下一合法动作：先串行采用 quality-policy-enforcement 与 observability-design（按实际入口指针消费）；原作者定向修五个位置族后交 fixed 对象，仅核受影响 claim。J1/J5 已通过部分保全，改适用范围或相邻 policy 不重开其已支持结论。external-tool-operation / positioned-artifacts 的依赖仍由 B2 修订和相应 interface/trust 通过共同闭合，不能因本 review 把尚未装入目标当已有。review 提交由 Driver 持有。
