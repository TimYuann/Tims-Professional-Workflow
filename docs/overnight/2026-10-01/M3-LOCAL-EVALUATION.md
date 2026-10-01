# M3 case 1 · 独立结果评价

日期：2026-10-01。评价者：`tpw-night-method`。

**Verdict: PASS** — 固定候选的局部修复恢复本 fixture 契约；原始测试未削弱，函数接口与错误行为保留。该结论只评价下面固定代码/测试对象，不接受 M3 里程碑、剩余风险、部署或发布，也不证明业务产品/UCBIP 有效性。

## 对象、依据与独立关系

- 候选：`9699276ab1d413379ace91afa0cf683a83b69aa3`，仅 `docs/overnight/2026-10-01/fixtures/m3-local-fix/` 的代码与测试；fixture tree `3a5489cd3a12a83bb443319c71e77b080bb1dfd5`。
- 基线：`04521323d0afdb44da99e839bb3a21535dd551c6`。
- 固定 F startup prompt：SHA-256 `75ef8c4305b7f4255a75b379d5ae6b7c44feeb002c30c1d4aa6b1226dace4bbd`，实测匹配。
- 使用候选 commit 的 `EVALUATOR-CHARTER.md`，SHA-256 `678e47e51c0a88e4206b134ebccda471c8c138328a89078a95ba0ca140d48661`。与最初预持阶段的 Charter 相比，它增加 M4 方法引用；未改变本次 claim、权限或私有 case criteria。
- 候选的 `CONTRACT.md` / `TASK-INPUT.md` / `BASELINE.md` 摘要分别仍为 `ecfc6195726fe62321208ad766fcbe7005c784c6d2aece7f9b2a2eca4ef293bb` / `90b7e06d06e525e79a58496cdf65603f15da18f15809a7e1e3a256a1f904167e` / `6e8262b6361be36abc39947cf00fef02adac9c9120f353e5b38070c84e119a57`。
- F method 取自 Charter 所指的 `013659331c8c5f9f54b866b393972a03d7938773:professional-workflow/methods/behavior-claim-evaluation.md`，实测 SHA-256 `06b0692290a9ce8cdc7048b33a89ec21f3636ee00138a613121ec4b72457af06`，匹配其绑定。候选 commit 中后来更新状态标题的同名文件是不同字节对象，不混用摘要。
- 作者实例：`tpw-night-m3-local-impl`；物理集成者 Driver。我未写 fixture、契约、实现或测试；此前方法评审没有代写本候选。case criteria 在候选读取前已于本会话预持，未写入 repo 或发给作者/Driver；本报告不列出 rubric 或私有预期。

## 变更与身份核验

seed→候选的 code/tests diff 仅两项：`src/labels.py` 的内部实现由 `value.strip().upper()` 改为 `" ".join(value.split()).upper()`；新增 `tests/test_labels_whitespace_runs.py`。原 `tests/test_labels.py` 字节未变，签名、类型检查和 TypeError 分支未变。契约、任务输入及原失败观察保持原摘要。

| 候选相对路径 | SHA-256 |
| --- | --- |
| src/__init__.py | `01668323d7700904ad3ff81941a8c1beaf0b22fe2ccbf96d2749689d64cc576e` |
| src/labels.py | `f767787ba2ac8cf52e7b4f62e74b146b858fad91031bed139c849c9e23a92f87` |
| tests/test_labels.py | `8dbf28589f9e4ce34cc36aa87df88a8aeed63cb260214d3bf1997f0fe396bb06` |
| tests/test_labels_whitespace_runs.py | `d52e05f5d10c2ac5d8615d864361c21b5de6469f19359882044c442f73bba40b` |

## 独立观察

环境：Python 3.14.4，executable `/opt/homebrew/opt/python@3.14/bin/python3.14`，与记录的基线 Python 版本一致。仅标准库，无网络/安装/外部服务。

隔离方式：用 `git ls-tree -r --name-only <commit> -- <fixture>/src <fixture>/tests` 列出路径，逐项 `git show <commit>:<path>` 导出原样字节至系统临时目录的 seed/candidate 两个目录；导出后核 SHA-256。设置 `PYTHONDONTWRITEBYTECODE=1`、移除继承的 PYTHONPATH，分别以 fixture 副本为 cwd 运行同一 executable。临时目录运行后自动回收；没有改仓库中的实现、输入或测试。下表保留实际命令、退出码与输出信息，不以 E 自报代替观察。

| 观察 | cwd 与命令（python3 指上述 executable） | exit | 结果 |
| --- | --- | --- | --- |
| seed 原始场景 | seed；`python3 -m unittest discover -s tests -v` | 1 | 4 tests，1 FAIL，3 PASS |
| 候选原有测试 | candidate；`python3 -m unittest discover -s tests -p test_labels.py -v` | 0 | 同一原始测试文件的 4 tests 全部 PASS |
| 候选完整测试 | candidate；`python3 -m unittest discover -s tests -v` | 0 | 7 tests 全部 PASS |
| 负控制 | seed；`python3 -m unittest discover -s <candidate-copy>/tests -v` | 1 | 同一候选测试集加载 seed 实现，7 tests 中 3 FAIL，4 PASS |

本次 `<candidate-copy>` 实际为 `/var/folders/vq/dk3gntzd7dz529mp_57ybgyh0000gn/T/tpw-case1-f-qfrso33u/candidate`；负控制的实际完整命令为 `/opt/homebrew/opt/python@3.14/bin/python3.14 -m unittest discover -s /var/folders/vq/dk3gntzd7dz529mp_57ybgyh0000gn/T/tpw-case1-f-qfrso33u/candidate/tests -v`。该临时路径只标识本次运行，不是持久证据依赖；可从固定 commit 字节重新导出。

原始失败输出（路径无关部分）：

```text
test_collapses_internal_whitespace (test_labels.NormalizeLabelTests.test_collapses_internal_whitespace) ... FAIL
test_non_string_raises_type_error (test_labels.NormalizeLabelTests.test_non_string_raises_type_error) ... ok
test_preserves_punctuation (test_labels.NormalizeLabelTests.test_preserves_punctuation) ... ok
test_whitespace_only_becomes_empty (test_labels.NormalizeLabelTests.test_whitespace_only_becomes_empty) ... ok
AssertionError: 'NORTHERN   STAR' != 'NORTHERN STAR'
Ran 4 tests in 0.001s
FAILED (failures=1)
```

候选完整运行输出：

```text
test_collapses_internal_whitespace (test_labels.NormalizeLabelTests.test_collapses_internal_whitespace) ... ok
test_non_string_raises_type_error (test_labels.NormalizeLabelTests.test_non_string_raises_type_error) ... ok
test_preserves_punctuation (test_labels.NormalizeLabelTests.test_preserves_punctuation) ... ok
test_whitespace_only_becomes_empty (test_labels.NormalizeLabelTests.test_whitespace_only_becomes_empty) ... ok
test_collapses_mixed_internal_whitespace_run (test_labels_whitespace_runs.WhitespaceRunTests.test_collapses_mixed_internal_whitespace_run) ... ok
test_collapses_multiple_runs_around_punctuation (test_labels_whitespace_runs.WhitespaceRunTests.test_collapses_multiple_runs_around_punctuation) ... ok
test_empty_string_becomes_empty (test_labels_whitespace_runs.WhitespaceRunTests.test_empty_string_becomes_empty) ... ok
Ran 7 tests in 0.000s
OK
```

负控制是原样 seed 实现与原样候选 tests 的组合，没有弱化/修改测试。失败名称为 `test_collapses_internal_whitespace`、`test_collapses_mixed_internal_whitespace_run`、`test_collapses_multiple_runs_around_punctuation`；对应实际错误结果为 `NORTHERN   STAR`、`ALPHA \t\n BETA`、`NORTH\t-\n STAR`。空串、原空白串、标点及 TypeError 测试仍 PASS，摘要为 `Ran 7 tests in 0.001s; FAILED (failures=3)`。这表明测试集对修复前缺陷有区分力，不是仅验证“能运行”。

## 判断、覆盖与限制

比较有效：同一 Python/执行环境，原有测试输入及期望字节相同；候选新增覆盖单列，负控制使用同一候选测试集对 seed 运行，避免把新增测试数量误作修复证据。没有测量失效或环境阻断；有效原失败在候选消失，回归测试能在旧实现变红。

契约检查结合上述运行观察与一行实现的静态核对：内部空白合并为 ASCII space、边缘空白消除和大小写转换由对应字符串操作完成，标点没有过滤步骤；既有非字符串保护/错误类型及签名未变。运行覆盖是有限输入样本，不声称穷尽所有字符串、特殊 str 子类或所有平台；未发现本次明确契约的反例，也不声称验证目标价值或大项目效果。

**范围固定：本评价覆盖 `9699276` 的代码/tests 字节，仅此版本。** 写报告前观察到当前 HEAD 为 `10c8b727dbf14481960c02688f1de1dc252ea38f`，其 code/tests 与候选及工作区的对应 diff 为空；这不是对该后续 commit 的完整接受。后续 E 若改变任一代码/测试字节，当前 PASS 不自动覆盖，应向 Driver 报新的固定对象及受影响差分。

本报告没有验证 E 的后续 method-bound 重验是否实际执行、流程成本、case2、包冷启动或整体 M3 接受；这些属于其对应证据与 authority。Driver 可将本报告作为该固定局部实现的独立 F 输入，不由此取得 closure、迁移、部署、发布或风险接受权限。
