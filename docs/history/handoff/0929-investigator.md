# 0929 investigator · handoff（暂停前状态摘要，≤15 行）

1. 基线 PASS：tag v2.0.6 / 29a50e4 干净 clone → render 12/12、closure 19/19、consistency 7/7。A/B/C/D 四件**全部做完**；完整证据与复现命令在 `.pi/investigation/REPORT-0929-investigator.md`（**尚未 commit**，停手指令后未做 git 操作）。仅 D 的判档口径一处留 UNVERIFIED。
2. A：40 个产物字段中 21 个不被任何阶段判据门控（25 条判据零命中，复算与 verify 一致）。三堆清单——真空：无；有软约束（15）：A1.done_meaning、A1.unknowns、A2.claims、A2.evidence、A3.consumers、A3.freshness、A4.why、A5.edges、A6.change、A7.stance、A7.conditions、A8.claim、A8.scope、A8.observation、A8.environment；实际被别的东西约束（6）：A9.run、A9.subject、A9.phase、A9.decision、A9.why、A9.evidence（ledger.sh:50-55 拒空、:126 自动生成 run，且仅在使用该工具时生效）。
3. A 受控实验：C15 扩到 40 字段 → 全绿（40/40 字段当前正文都教了）；抹掉 A9.why 教学后扩版红、原版绿。
4. B：15/18 有 embodiment 箭头；三条无人接——arena 的合成记录/评分表/交叉评判无字段承接；git-workflow-and-versioning 的提交序列/分支/版本/标签/变更日志/残留清单无承接（仅 A9.result 的 P6 判据接住「发布动作+回滚路径」）；teach 的「对方脑子里的模型/手上的东西」无承接（outputs: [] 与正文「不产出文件」一致）。
5. C 读写方：写＝architect（roles/architect.md:52、skills/feature-map.md:74/:86），读＝无（全库 grep 只有说明语句与派生视图）；保鲜循环产出 A8.frame_alignment（skills/verification-suite.md:33/:48-50），P5/P6 判据要求记录，但下一次 P1（inputs=[A1,A2]）无接收方。
6. C 实验（P6+architect）：只加 default_roles → 全绿零变化；加 `write: A3.freshness` → C13 越权写红（P6.produces=[]）；加 `verify: A3.freshness` → 全绿、C15 门控 19→20；再给 P6.produces 加 A3 → 全绿。
7. D（C7/C9 下游）共 2 个结果版本互相矛盾：README.md:263-268「下游必须 SKIP」（skip=True 全库 0 处使用，与代码矛盾）vs docs/coldstart.md:57-67 + skills/coldstart.md:48-52/:63-65（PASS，与代码一致）；另有 4 处机制/细节与代码不符：README.md:139、:141、:274、docs/coldstart.md:60（「这两项」实际只有 C9 比 sha256），以及 docs/coldstart.md:61 + skills/coldstart.md:50 的「锁文件过期」消息文本（实际缺锁消息为「缺少 upstreams.lock.yaml…」，且 C9/C20 同时红）。
8. D 判档：skills/tier-sizing.md:16/:21 要求 A1 vs registry.yaml:1046 inputs=[] + registry.yaml:1050-1052 note（被同技能块 :1055 的重复 note 键覆盖，解析后丢失）+ check-closure.py:779-787 注释，三处说法不同；C18 硬编码只查 {tier-sizing, coldstart}（check-closure.py:790-792）。docs/coldstart.md:91「不写数字」vs 技能表 2/5/12 → UNVERIFIED。
9. 未查完：C9 的 sha256 篡改未重注入（只验证该分支执行、detail 出现后缀）；非 ledger.sh 手写空栏未测；README 计数漂移（:25/:122/:129/:159）已记录，属相邻话题。
10. 注意：工作树 3 个脚本有他人未提交改动（check-closure.py / check-consistency.py / ledger.sh），我全程未触碰未 stage；报告全部行为证据取自 tag 检出，未把半成品状态记成结论。
