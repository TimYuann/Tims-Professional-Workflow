# Gate2 · B1 ABC3 定向蒸馏复核

2026-10-02，tpw-absorb-gate2，固定对象 `8cdd3990991b1da8514d6c81f7734403f4dc64e5`，唯一父 `d1eed24788cb33982d4c36f6eb7c2bacbd5fcc9d`，core tree `2b3c8cd61db2b1c3511b5925dff4e9ada4433c24`。实际 delta 七文件 +59/-6，git diff --check 无输出。只读固定差分与受影响正文；复用本轮 ABC3 的实际回源，不重读全仓、不重开旧R/D1/J1或其他PASS，不改变作者/评价者贡献关系。

**六个 delta 文件 PASS；change-review 大部 PASS，仅一条新泛化需限缩，整笔暂不全采用。**

| 文件 / 机制 | 结论 | 依据与边界 |
| --- | --- | --- |
| verification-harness-design，MG1/MG3/MG5 | PASS | repo 实际 manager/wrapper/entry、doc漂移实际损害、budget-relative startup、普通前置friction/secret阻断与静态线索均分开；CI完整集合/currenthead/requiredstatus/pending/coverage以及有效bypass透明；entry/build/环境、另一入口不冒所跳入口、持久readback、合法既有target不强禁。无评分/四agent/全绿或live强门槛。 |
| local-defect-feedback-loop，MG3 | PASS | compile/type errors分组、首可行动根错误/cascade分开，窄授权内修复与named blocker；原D1允许暂定假说/成本停/低频反例保持。 |
| merge-conflict-resolution，MG3 | PASS | 实际conflict集合/无标记、manager再生成后核真实依赖diff，不把生成当正确保证；无自动mainline合入，作用范围/回退/自有stage/authority继续。 |
| guide-test-evidence-quality，MG3 | PASS | waits观察条件/真实assert；重试记录对象/条件/结果，不让绿抹首失败，不固定1或无限重试；quarantine/skip/bypass保有效owner与理由/后续依据。 |
| decision-record，MG5 | PASS | sink-specific formula/control/leading字符处理并保原evidence，quote不认证全reader安全；append避免截断非并发原子，全TSV/script/UTC不作普遍规定，复用bounded composition。 |
| handoff-and-resume，MG5 | PASS | 已执行compile窄证据可保、行为因环境未核同时如实记，不整体erase也不升fullcoverage，既有mode非必选/necessaryclaim核固定对象保持。 |
| change-review，MG2/MG5 | 一处需修；其余PASS | intake先对象/acceptedintent，评论source/version/位置与缺取范围；三工作disposition非F verdict/授权、cheapcommand限合法可跑、risk边界不按历史pattern免核、原diff可恢复/import非机械、script-safe非JSON够；secondopinion无400词/model/quota、贡献与有效authority保留。新旧finding句见下。 |

## 新 finding B1-ABC3-intake：防护检查时序不能成为所有finding的关闭门槛

`change-review.md` §Comment intake and triage · Old findings on current tip 写：任何 prior finding claimed fixed 都要 verify check ran **before the side effect**, non-no-op、principal coverage。这来自 bugbot-triage 的 **stale security-review finding already fixed**，其具体问题是 authorization/validation guard 是否在副作用前；ABC3 review 的对应缩写也必须读在该安全机制范围，不能推广所有finding。

反例：界面文案或列表排序finding修好后，F运行其观察验证，运行时间当然在产物变化后；纯类型/编译finding没有“principal及被保护sideeffect”。不能据通用句要求其验证先于被评变化，否则导入不存在的关闭前提。

最小修：所有旧finding按当前对象/claim/覆盖核修复并保关闭关系；只有涉及防护/权限/验证guard的finding，再核guard本身在被保护副作用之前、非no-op且覆盖对应principal/object。区分产品里的guard与F事后执行的观察，不要求所有验证先于效果。仅改这条，不重开旧已关闭项、不要求新实验/审核实例/guide或validator。

## 消费与下一动作

六个通过delta复用已有owner文件与实际存在的guide依赖，无新增平台；该对象change-review的新版本先held。Driver可串行采用六文件及先前已过对象，原作者只修上述一句后给fixed delta核，其他新MG2/MG5条款无需整轮重做。没有runtime/SDK/CI/真实项目收益或fresh-reader观察，文本PASS不替整体整合接受。review提交由Driver保全。
