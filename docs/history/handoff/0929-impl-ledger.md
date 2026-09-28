# 0929 impl ledger handoff（≤15 行，暂停留存）

1. 根因：`scripts/ledger.sh:57-62`（旧版）用 `case "$ledger" in */tmp/*|/tmp/*|...)` 只匹配输入字符串；相对路径经指向 /tmp 的软链时字符串里没有 /tmp，闸放行。
2. 改法：新增 `real_path()`（现 `scripts/ledger.sh:58-140` 区间）——`readlink` 逐级跟软链（含悬空软链）+ `cd/pwd -P` 物理化最近已存在祖先 + `normalize_path()` 折叠 `.`/`..`；临时根同法解析后按路径分量前缀比较；命中 exit 3，解析失败 exit 4。
3. 临时目录定义：只有 `/tmp`、`/var/tmp`、非空 `$TMPDIR` 三类，无第四类；已写进 `docs/ledger.md`「临时目录判定」（含抓不到的边界：TOCTOU 窗口、挂载点、TMPDIR 未设置时的 /var/folders）。
4. 回归：`.pi/review-v4/test-ledger-tmpdir.sh` 共 23 用例（红方 13 / 绿方 10）。新实现 23 PASS / 0 FAIL；旧基线（`baseline-v2.0.6-ledger.sh`）12 FAIL。**`evidence-baseline-red.txt` 的意思是「被测对象=旧基线脚本时套件是红的」**，即测试抓得住该缺陷，不是注入台基线红。
5. 压测：`stress-ledger-concurrency.sh` 10 轮 × 100 并发 PASS（0 丢行 / 0 重复表头 / 0 列错乱 / 0 重复 decision，3m53s）+ 3 轮 × 150 PASS；锁与 O_APPEND 一段未动。
6. 末级软链判断：**拒写**。理由：追加打开跟随软链，字节落在目标处；闸要挡的是「记录丢在临时目录」，所以判落点不判路径名。指向稳定位置的软链放行；悬空软链指向 /tmp 拒；软链成环 exit 4。
7. 新假设：a) TMPDIR 未设置时不覆盖 macOS `/var/folders`（写成边界）；b) 解析失败 fail-closed（exit 4）而非放行；c) 大小写变体按内核解析；d) `软链/..` 按 POSIX 物理语义（=目标之父）；e) 稳定位置的 `tmp` 同名目录不再误报；f) 解析→打开窗口不设防（TOCTOU，写成边界）；g) `/private/tmp` 与 `/tmp` 视为同一真实路径。
8. 未完成项（按暂停指令停手）：`.pi/review-v4/REPORT-0929-impl-ledger.md` 未写；仓库三检查器未复跑；`scripts/ledger.sh` 与 `docs/ledger.md` 的改动已在工作树上，**未 commit、未打 tag**。
