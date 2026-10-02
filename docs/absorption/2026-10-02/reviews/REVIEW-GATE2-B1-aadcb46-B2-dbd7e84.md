# Gate2 · 两B未审增量合并复核

2026-10-02，tpw-absorb-gate2。非候选作者，沿已裁ABC5/6/7与前B固定对象/已关findings/贡献，不重开934c1ec已过单句。source回源复用本轮原文/sections，另核prompts buildWorker108–143及实际源路径，不运行源码或读作者mutable。

- B1 `aadcb46f142b6d1f67af81b080a1c2116dad79cb`，唯一父934c1ec；本次比较base `8cdd3990991b1da8514d6c81f7734403f4dc64e5`，core `50303cbd0b21a221a9a332bfee5d236af3d107bd`；实际 delta 七文件 +141/-12。
- B2：Driver给“最新/HEAD”，本次一次性解析 `absorb/w2` 为 **`dbd7e8448b8e3fb1880efdff8ffa9643462cfe83`** 后固定读取，唯一父5fd2165；比较base `941a13928ee51b88fc17837ba8ecd74f3fa5ccb8`，core `4755164cfb8992aad42209efbd71d8bfbf5497a5`；delta仅bounded-composition/guide-agent-text +29/-2。后续tip不被此review覆盖。
- 两fixed delta的git diff --check无输出。只写本review，git集成/提交由Driver持有。

## 文件级结论

| 对象/文件 | 结论 | 内容与边界 |
| --- | --- | --- |
| B1 behavior-preserving-change | PASS | structure/visual独立选择；accepted行为与currentbaseline分开、targeted pin可替fullharness、build非behaviorpin；rename非symbol、caller/legacy承诺、合法shim/安全目的保留；visual阈值/比较/噪声/owner修baseline、pixelgreen非interaction均正确。不导入固定PR/loop/函数跨界architect。 |
| B1 verification-harness-design | PASS | repoharness优先、actualsurface/currentmarker/freshstructure、动作→readiness与稳定bundle条件；PTY≠pipe、采样干扰/heap只是线索、custody/ownsessioncleanup、无新增dependency/debug默认权；原repo/CI/entrycoverage通过保持。 |
| B1 guide-professional-explanation | PASS | placeholder docs-canvas只取长篇导航/overview/references，不认证host、不固定card/句数/顺序，不另平台。 |
| B1 change-review | 正文实质PASS；需修G2-SOURCE | 同fixedinput/acceptedcontext、source去重/coverage/closure；描述problem/result/effect/evidence、unit按真实boundary；verdict受rebase/base/依赖/环境影响、patch-id只是线索；frontier/observedstate/动作grant分开、非默认stale-base/flake次数、boundedunattended/贡献/stop范围保留；934单句闭合保持。新增source路径有误，修后才整文件消费。 |
| B1 change-slicing | 正文实质PASS；需修G2-SOURCE | 真实dependencychain与pendingobjects可恢复、composition互指，无新shipping权限/阶段；shipping锚点不存在。 |
| B1 handoff-and-resume | 需修G2-LABEL与G2-SOURCE；其他PASS | 自足输入/actualidentity、checkpoint/error/unknown、最强supported claim percoverage不取min、非盲重试、证据受影响才核及消费记录都符合；但label不是snapshot，shipping锚点不存在。 |
| B1 design-alternatives | 新synthesis正文PASS；需修G2-PIN | 同brief/inputs/resources、真实criteria/合法blind条件、graft适用/来源/新对象、合成者作者关系、分歧/收敛不自证均正确；插入Cursor行后两“Same pin”误指Cursor。 |
| B2 bounded-composition | 新正文大部PASS；需修G2-LABEL | 自足task与Charter互指、logicalstart/真正pendingdependency、实际branch/consumption、不假overrideauthority、env非全禁；可推进frontier/landedref/claimsreuse/多observer单canonicalwriter/动作权限分开。第11项label的snapshot语义需修。 |
| B2 guide-agent-text | Carrier正文PASS；需修G2-ORACLE | 承重why/exception/unknown保全、不得delete-on-doubt、真实relative可含合法包外..、actualhost才metadata、parse≠discovery/trigger/semantic正确；未新hostgate。Status新误指DEF3 review，需保Oracle实际裁定者。 |

## 最小修

### G2-LABEL · 可变标签不是快照（两个owner各一处）

B1 handoff §Task description and artifact identity 写“A branch name or other mutable label is a snapshot at that time”；B2 bounded-composition 第11项写“A mutable branch name is a snapshot taken at handoff time”。branch label本身仍可变，快照是**在消费/约定handoff时解析并记录的commit或artifact version**，不是字符名称；source startingRef without dependency 在spawn时读取当时tip，这也不保证handoff时对象相同。

反例：handoff只写feature/x，handoff后另一个commit推进同branch；receiver再读feature/x看到新内容。不能既称snapshot又让consumer误以为label已固定。最小修明说mutable locator≠fixed object，保存并核实际解析对象与时间/消费范围；保现有依赖/actualcommit核，不建resolver平台或新gate，不把所有已有来源全重读。

### G2-SOURCE · B1三个文件的承重源路径不存在

pin中没有 `cursor-team-kit/skills/{opening-a-pr,shipping,babysit,autopilot-full,autopilot-stack}/SKILL.md`。已用源文件清单核，其真实承重正文是 **`pstack/skills/poteto-mode/playbooks/{opening-a-pr,shipping,babysit,autopilot-full,autopilot-stack}.md`**（本轮已直接读）。

change-review 的Unit granularity/forge states/verdict/frontier及两条Source anchors、handoff evidence reuse正文/Source anchors、change-slicing dependencychain正文/Source anchors需对应修正。`make-pr-easy-to-review/SKILL.md`仍在cursor-team-kit，不能随错误批量搬；原专业内容不需重写。问题是可回源身份断裂，不是因为hostcoupling拒绝经验。修后只核anchors与受影响consumer，不重做方法实验。

### G2-PIN · design两条Same pin的指向

Source anchors先Matt `c55ee460…`，随后新Cursor `ecc249f1…`；再下两行“Same pin, skills/engineering/codebase-design/{SKILL.md,DEEPENING.md}”现在紧接Cursor却属于Matt。用显式Matt repo+pin或把Matt行相邻，并保持Cursor arena行自己的pin；不要让同表插入把上游贡献归错仓。无需改synthesis正文。

### G2-ORACLE · guide-agent-text DEF3出处

Status新增 `REVIEW-A2R-CURSOR-DEF3 (J3)` 不是现有裁定文件/实际审核者。真实来源是 **`ORACLE-REVIEW-A4-DEF3.md` J3**；review目录仅该DEF3裁定。按实际Oracle署名/source归属修Status，其他ABC4/ABC7贡献保持；本文不重裁Oracle J3内容。

## 消费与下一合法动作

Driver可逐文件串行采用B1的behavior-preserving-change/harness/professional-explanation三个通过对象；其互指targets在此前通过body可取得，按真实整合入口列按需使用。B1其余四文件与B2两文件等上述窄修后的fixed对象再核；新sharedchain/source仅专业body通过不够造假resolved reference。已有934单句以及所有旧R/D1/J1/EXT8关闭保持，当前source轮次/多family贡献不清零。

B1/B2 source重复不按文件计独立增量；未运行真实refactor/visual/SDK/CI/model/应用消费或并发实例，正文/锚点通过仍不替效果、动作权、whole-package接受。后续behavior-claim real-leg澄清及ABC8新B对象另审，仅其实际受影响claim。
