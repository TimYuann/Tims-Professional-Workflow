# 0930 rolefix 交付

## 任务 1–7

1. 九份 `roles/*.md` 的 34 条原则引用均改为独立 id 行与 role-specific `trigger`；不再在条目中复制原则释义。依据「原则正文只在 `principles/`，角色里只留 id + trigger」；保留了各角色产物契约及非原则释义的上下文。
2. 清理以「唯一」建立身份或权限的句子，保留 `A3` 事实来源等事实唯一表述。Adversary 改为以校准的独立判断为价值，Scribe 明确是 cross-cutting role 而非持续运行进程；依据 Owner 对使命偏置与 role/runtime 区别的裁决。
3. Driver 明确 substantive judgment 与 workflow qualification / routing judgment 的边界，列出资格、过期证据、卡住及升档等判断；缺件由 Driver 决定停，退件依据 registry canonical producer，正常角色激活依据 phase definition。逐字加入 Owner 的 `Runtime boundary`，保留档位及 A↔B 映射。
4. Verifier 改为以判别能力而非测试作者定资格；新建或实质修改 probe 首次支持 PASS 前须有能杀坏对象的真实 observation，成熟 probe 依身份、边界与证据适用性沿用，变更后重新资格化。证据仅放 `A8.observation`，依据 Owner 对 qualification 生命周期的裁决。
5. Cartographer 的每片要求改为自身可判定退出证据，不强求单片证明整体产品；并行资格同时检查 dependency edge、write/resource conflict、acceptance coupling，物理并行留给 runtime。依据 Owner 对两处绝对化切片规则的修正。
6. Architect 删除排他性身份宣称，保留 `A3` / `A4` 的字段、scope 双层、地图保鲜及开工/退回等实质内容；九条原则只换引用形式。依据「保留 A3/A4 一切实质内容」。
7. Builder 在开工前增加 repo、branch/worktree、base commit、assigned files/resource ownership 身份核对，不符则不写；保留 `A6.subject` 双 commit。Voice 将仪式性复述确认收窄为业务歧义才问，可逆问题自行决定记入 A9，只有不可逆、业务取舍或权限外打断 Owner；**这一条是我按任务书提示对 Owner 意图的解读**。Scout 仅收紧排他身份与原则引用，没有重写心智模型。

## 我发现但没有自修的

- `docs/coldstart.md` 仍讲直接送入角色文件；本轮只许改 `roles/`，没有碰它。实际运行时需要用已提供的 `scripts/compose-role.py` 装配正文与原则。
- `workflow/registry.yaml` 的 `A7.stance` 仍是采纳／挑战／附条件通过，非 PASS／FAIL／UNVERIFIED；本轮未改 registry，也没有增加第四种 stance。Adversary 在无法判定时退回补证据，不宣称通过。
- `compose-role.py --check` 检查同一行 id 后的释义，不对 trigger 是否有语义重复作机器判定；这次按文字逐条写了选择条件，没有修改检查器。

## 我对裁决的疑问

- Owner 把 PASS／FAIL／UNVERIFIED 称为 adversary 同等合法结果，但 registry 的 A7 stance 是另一套三值；我按「判断态度不能偏向造 finding」处理，不将其写成 A7 的新枚举。若要求独立的 UNABLE/UNQUALIFIED 持久状态，需要另行裁定 A7 contract，而不是在角色文字里暗改。
- Builder 的「身份资格」被我解释为开工前校验与任务分配匹配、发现偏差即不写；Voice 的「何时不要问 Owner」被解释为可逆决策记 A9，而不是一切复述都取消。请 Owner 确认这两处解读。

## 检查实际输出

```text
$ python3 scripts/render.py >/dev/null
(exit 0; 无输出)
$ python3 scripts/check-closure.py --quiet
合计: 20 项通过 / 1 项失败 / 0 项跳过 / 21 项检查
(exit 1; 非 quiet 输出确认唯一失败是 C1：当前 commit 没有对应 tag)
$ python3 scripts/check-consistency.py --quiet
合计: 7 项通过 / 0 项失败 / 0 项跳过 / 7 项检查
(exit 0)
$ python3 scripts/compose-role.py --check
角色装配：结构成立（9 个角色，34 条原则引用，正文均在 principles/，角色内无第二份释义）
(exit 0)
$ git diff --check
(exit 0; 无输出)
```
