# HANDOFF · 0929 impl-checkers（停手快照，未 commit；只改 scripts/check-closure.py 与 scripts/check-consistency.py）
## 1 已完成并落盘（未提交；行号=当前文件）
- check-closure.py:154-157 CHECK_COVERS（C20→skills/##来源；C21→principles/来源：）。
- check-closure.py:246-288 C1：无 git 元数据（rev-parse --git-dir 失败，如 git archive 导出）→ SKIP 且消息写「无 git 元数据」，不再误报「没打 tag」；有 git 无 tag 仍 FAIL。
- check-closure.py:559-631 C9 改名「来源声明与锁文件一致（有实物时校验内容）」+两档：无 upstreams→PASS（锁文件核对）自曝未做实物对照；无可信 git→SKIP「未核 pin」；全比→PASS（＋实物核对）；真漂移→FAIL 优先。
- check-closure.py:715-718 C12 改名去「原创」歧义；:753-757 C13 边界原文；:833-841 C15 两条边界（只验出现不验在教 / role-contract-drift）；:957-964+988-992 C20×C12 交叉断言（吸收形态不得标 origin: library）。
- check-closure.py:994-1054 新增 C21（原则 ## p-* 与 registry 对齐；来源路径反查 upstream id 集合=registry.sources，拒幽灵/缺失/串线/重复；original 需内部锚点）；:1094-1156 新增 C22（enforced 须有 enforced_by+已注册+CHECK_COVERS 类目一致；UNVERIFIED 须 owner+due；level 不超 skills=file/principles=clause）。
- check-consistency.py:102-139 Result 支持 skip、合计四栏与 closure 同 schema、删被覆盖的死代码原 122 行；:397-405 S4 边界原文（s4-role-body）。
## 2 没做完 — .pi/review-v4/REPORT-0929-impl-checkers.md 未写（逐条判定/自测/误报/四条保留判据/文档变假清单）；未 commit（遵停手令）；git archive 实跑待 commit 后。
## 3 踩到未闭环 — 工作树基线 20 PASS/1 FAIL（C1：e7f6de1 无 tag）/0 SKIP；带 tag 副本 21/21；自制 22 条负对照全过（/tmp/tpw-0929/controls.py）；另 scripts/ledger.sh 有非我的未提交改动。
- 文档变假：README:266-273 说 C7/C9 会 SKIP（实为 C1/C9 可 SKIP）；docs/coldstart.md:57,65-66 与 skills/coldstart.md:48-51,64-65,77-79 说「SKIP 不可达/见到 SKIP 即故障」。
- D2 注入只删 roles/architect.md 的教学，architect 拥有的技能仍教 scope，选 (a) 也不会红，故按判据选 (b) 边界声明；B4 台证明 pstack 无 git 时不再假称已核 pin。
## 4 被否决 · 5 等你 · 6 新假设 — 无人否决、未为变绿放松断言；等你 pane 重启后的下一批派活，停手期间不 commit 不 tag。
- 新假设：SKIP=UNVERIFIED 渲染；C9 无 upstreams 仍 PASS、真漂移 FAIL 优先于 SKIP、repos 为空判 SKIP；「上游自己的 git」=show-toplevel 落在 ROOT/upstreams 内；C1 用 rev-parse --git-dir；CHECK_COVERS 用模块常量；level 上限硬编码；status 只认 enforced/UNVERIFIED；C21 内部锚点=A*/@id/链接/p-*、borrowed 只比集合；C15 选 (b) 不加强断言；consistency 的 skip 仅 schema 对齐、当前无分支。
