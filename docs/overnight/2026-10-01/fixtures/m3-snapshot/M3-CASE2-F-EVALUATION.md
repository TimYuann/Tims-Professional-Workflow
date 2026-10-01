# M3 case2 · 独立 F 结果评价

2026-10-01。Evaluator：`tpw-night-method`；E 作者：`tpw-night-m3-local-impl`（原会话复用，不是新身份）。

**Verdict: PASS。** 固定 treatment 的 recorded presented-view 入口兑现隔离 fixture 的 B/C v2 及 D 已接受的 pinned-pair 承诺；保留原测试，独立行为观察与有效负控制支持该结论。只覆盖下述固定版本和边界，不接受整体 M3、用户价值、剩余风险、部署、迁移或发布。

## 固定身份与独立关系

| 对象 | 固定身份（实测 MATCH） |
| --- | --- |
| Treatment | commit `17602f2b12822aba88785e27a733f75a3238214d`；tree `f9b4f90b9e5a0c7ae11dfe681b82a4a22dddef03` |
| Baseline | commit `2ad72273c6aa7dd9cb9775d9146a6fd549db19b1`；tree `f7f3fb2524a8f6a7ad125c0f45a6564d29139744` |
| M3-CASE2-F-STARTUP-PROMPT.md | SHA-256 `375f12b621b9c9b41c41410cca0ddb0da2c5a8d484a22e55bd759914e710af65` |
| M3-CASE2-F-CHARTER.md | SHA-256 `98ab5c2bd4db2da434e5ed0d7346c354af08e9870a8f367a316a2512bb11e26b` |
| B v2 / C v2 | `6cf43d3fb647cf2c250f275179762917c0763a669e84f1718d85968a8e66c738` / `d35766b45085db2b7e5b3315cca5ce4183f722186a850ef317fd571ebba6d45b` |
| D-accepted Plan | `a306205729a002fdf1bc4eac6a623849cb2198985f8a6fbae4ec4c00ec47e5b9`；D 的接受记录为 §8.1 |
| Exact M4 method | `013659331c8c5f9f54b866b393972a03d7938773:professional-workflow/methods/behavior-claim-evaluation.md`；SHA-256 `06b0692290a9ce8cdc7048b33a89ec21f3636ee00138a613121ec4b72457af06` |
| E factual handoff | treatment 中的 `M3-CASE2-E-REPORT.md`；SHA-256 `557c1ed51e5c9b8c951b1e68a01b318160126ac63924c960b6e1b0c9dd298aed`，仅作自述输入 |

startup packet 全文与独立 Charter 已读；逐段提取嵌入字节，核对声明摘要及相应 Git blob/Charter，全部匹配，包括 Profile、Backbone、B/C、Plan、M4、CASE-INPUT、BASELINE、E report 和三份 treatment source/tests。提取时最后一个区段与中间区段的换行分隔不同，首次统一剥换行导致本地解析断言失败；按实际区段边界重算后 test blob 完全 MATCH，这是解析器边界问题，不是候选差异。

case2 私有 criteria 在候选读取前已于本会话预持，当前仍可用；未从 E 或 packet 重建，也未向 E 请求。本报告只以公开 B/C/Plan 表达证据，不披露私有 criteria、rubric 或其精确预期。我此前审阅 B/C、挑战 D，没有编写本实现/测试；正常 findings 与补证要求没有变成作者贡献，工作区迁移没有新增独立身份。

## 字节变更与来源核验

baseline→treatment 的 fixture 变化仅 E report、新增测试、`src/page_summary.py` 与 `src/turn.py` 两份实现文件。后者将 view 总结提为 `summarize_view(view)`，并让 `Turn` 持有单个不可变 `StateView`，两个观察属性均从该值导出。`service.start(store)` 的现有调用形态、独立 `service.cases(store)`、StateStore/CaseRecord 的发布与更新实现未改。

| treatment 相对路径 | SHA-256 |
| --- | --- |
| src/page_summary.py | `a3b81175423bd241a2c63c9d0b530fda2aad9698a3e96ba6bd9495764d7570f1` |
| src/turn.py | `2be753eb357ad4c0eb150861c61a2b220c75af5423fc10a2ad9d304eede52354` |
| tests/test_episode_coherence.py | `4f0b000892b2e5f3808166ee305bc8ba492661262d1be27757c661dac317076e` |
| tests/test_existing_behavior.py（未变） | `9ac7ea872b8c50f921128e7a8d734539b273551e7d6e9363e3d5116103c7876f` |
| src/state_store.py（未变） | `90a1cb56549f5afdbae24d2b485f8a956e66081939159a435aa83e2f43029196` |
| src/case_reader.py（未变） | `89f05180854b8cb38b58299f516e7298cd2d211b88bed38f35087e6b1fe350bc` |
| src/service.py（未变） | `ea3fff5faf10d3025b19a07cc709985467b9dc67e607282ff1c87c73ddd66a0d` |
| src/__init__.py（未变） | `a5f855a87138b8c9a515d76a2b7858da6bba6fb60eff9446197fafc774733cf4` |

按 B/C v2 的相对路径顺序/UTF-8/最终换行 recipe，独立计算 baseline aggregate 为 `dbd6a306815bdc4cf3a33be14b38d4dd62b49d1535d7db41b9064eb07e51b474`，treatment 为 `93b54a8c439ae7466f4faa0adec2234a7170e81f0d25f9537768e5aa8e43141f`。差分不再被当作 B/C 自动失效；本次须且已依据行为取证，而非凭新 aggregate 宣告继承成立。

## 独立运行方式与输出

环境：Python 3.14.4，`/opt/homebrew/opt/python@3.14/bin/python3.14`；离线、仅标准库，与 baseline 记录的版本一致。实际命令为 `python3 - <<'PY'` 的内存 Git-object runner：用 `git show <rev>:<fixture>/src/<name>.py` 获取原样字节，注册 `types.ModuleType` 到独立的 `src.*` 运行上下文，以 `compile`/`exec` 加载；测试也取 exact blob，由 `unittest.defaultTestLoader.loadTestsFromModule` 与 `TextTestRunner(verbosity=2)` 运行。每次切换版本都清掉前一版 `src.*`，设置 `sys.dont_write_bytecode=True`。没有使用 mutable 工作区 source、写运行副本、缓存或修改现有 verification copy。

可复核的公开测试 runner 核心如下（不包含私有 criteria）：

```python
import subprocess, sys, types, unittest
prefix = 'docs/overnight/2026-10-01/fixtures/m3-snapshot/'
def blob(rev, rel):
    return subprocess.check_output(['git', 'show', rev + ':' + prefix + rel])
def run(source_rev, test_rev, files):
    sys.dont_write_bytecode = True
    for key in list(sys.modules):
        if key == 'src' or key.startswith('src.'):
            del sys.modules[key]
    package = types.ModuleType('src'); package.__path__ = []
    sys.modules['src'] = package
    for name in ['state_store', 'page_summary', 'turn', 'case_reader', 'service']:
        module = types.ModuleType('src.' + name)
        sys.modules[module.__name__] = module
        exec(compile(blob(source_rev, 'src/' + name + '.py'),
                     'git:' + source_rev + ':' + name, 'exec'), module.__dict__)
    suite = unittest.TestSuite()
    for name in files:
        module = types.ModuleType(name.removesuffix('.py'))
        exec(compile(blob(test_rev, 'tests/' + name),
                     'git:' + test_rev + ':' + name, 'exec'), module.__dict__)
        suite.addTests(unittest.defaultTestLoader.loadTestsFromModule(module))
    return unittest.TextTestRunner(verbosity=2).run(suite)
```

调用与实测结果（runner 对测试结果分别记录 effective exit 0/1；外层 Python 命令正常完成为 exit 0，因为负控制失败是有意捕获）：

| 运行 | source/test Git 对象及 files | 结果 |
| --- | --- | --- |
| Baseline smoke | 两者为 `2ad7227`；`test_existing_behavior.py` | exit 0；`Ran 3 tests in 0.000s; OK` |
| Treatment 全部公开测试 | 两者为 `17602f2`；`test_episode_coherence.py`、`test_existing_behavior.py` | exit 0；`Ran 12 tests in 0.000s; OK` |
| 旧实现负控制 | source `2ad7227`、tests `17602f2`；`test_episode_coherence.py` | exit 1；`Ran 9 tests in 0.001s; FAILED (failures=1, errors=6)` |

Treatment 12 项输出的测试名及结果摘录（省略重复的 module/class 全限定名）：

```text
test_each_update_between_episodes_is_visible ... ok
test_empty_case_set_presents_zero_open_and_no_details ... ok
test_episode_observations_are_pinned_values ... ok
test_equal_revision_presents_equal_case_data ... ok
test_existing_entry_points_stay_callable_with_a_bare_store ... ok
test_later_episode_revision_never_decreases ... ok
test_mid_episode_update_cannot_straddle_the_presented_pair ... ok
test_update_completed_before_episode_is_visible ... ok
test_update_with_unknown_case_id_leaves_all_statuses_unchanged ... ok
test_case_reader_returns_current_cases ... ok
test_summary_counts_current_open_cases ... ok
test_update_changes_next_current_read ... ok
```

负控制的 6 个 errors 都是旧 Turn 没有 `cases`，另一个有效失败为：`AssertionError: {'open_count': 99} != {'revision': 1, 'open_count': 1}`。这复现 E 记录但由 F 独立取得；旧版本缺新接口不是当前环境故障，也不能只凭这些 errors 声称完整行为已证明。下面的公开行为比较提供另外的语义证据。

## 公开行为比较与 coverage

使用同一 Python、同一 store 初始数据和更新操作，按公开 X-2 重放：打开、取 overview、完成更新、取 details。baseline 通过其旧独立 details 入口，treatment 通过 E 已记录的 `Turn.cases` 入口（接口差分明确，不伪称相同接口）。

```text
PUBLIC X-2 replay 2ad7227 {'revision': 1, 'open_count': 2}
details [('C-1', 'CLOSED'), ('C-2', 'OPEN')]
count-faithful False; current revision 2

PUBLIC X-2 replay 17602f2 {'revision': 1, 'open_count': 2}
details [('C-1', 'OPEN'), ('C-2', 'OPEN')]
count-faithful True; current revision 2

PUBLIC X-3 fresh next episode {'revision': 2, 'open_count': 1}
details [('C-1', 'CLOSED'), ('C-2', 'OPEN')]
C-1 resolution count: at open 1; after repeated observation access 1
```

这些观察从独立内存 runner 加载的 `service.start`、`StateStore.update_status`、`Turn` 属性取得，没有改文件。分辨真实呈现 pair 与错误跨 episode 混配的公开 B-6 负控制，输出 `correct pair valid True; mixed pair valid False`。它是对观察组合的负控制，不是 treatment 的失败。

另以公开 OPEN/CLOSED 输入与单线程更新组合独立运行 32 条短轨迹（96 个 episode 观察），核对每个 episode 的 count fidelity、后续更新不改变该 pinned pair、下一 episode 读取当前更新与 revision 单调关系，命令 exit 0，输出 `PUBLIC B/C trajectory checks 96 observations across 32 trajectories: completed`。这是补充有限样本，不宣称全输入穷尽或泄露私有 criteria。

| 公开 claim | 证据范围 |
| --- | --- |
| B-1/DS-I1/I2；D C-1…C-5 | 单次 current_view resolution 实测；Turn 持有 immutable StateView；两个观察来自同值；X-2 与混配负控制；新测试覆盖返回 dict 不会成为持久 live alias。 |
| B-2/B-3/B-5；DS-I3/I5 | 新 episode 的公开 X-3、两次更新/多次观察测试与独立短轨迹；旧 episode 保持 start pin，不能拿它当新 episode 判 stale。 |
| B-4/DS-I4 | 同 revision 的公开 equal-data 测试；旧视图没有被更新修改；源码保持新 StateView 发布而非 mutate，补充轨迹同样观察 pin 不变。 |
| DS-I7 与未决 DS-U2 | StateStore 源字节未变，已有/新增检查确认局部更新与 unknown id 不改 statuses；revision advance 是 E 已记录、C 容许的选择，不提升为通用业务规则。 |
| X-6、C-6/C-7/C-8 | 空集合、OPEN-only count、原 case 顺序/集合、bare-store 调用与原三项测试保留；未借此裁定 undefined statuses 或新增 membership。 |
| D bounded coordination / 无外部动作 | E handoff 明确 entry point、carrier、episode boundary、pin representation，实际 source 一致；变化只有两个局部实现文件/一份新测试，无时钟/线程/I/O/锁/持久化/外部依赖。 |

## 判断边界与限制

有效比较的 baseline/处理对象、环境和公开输入已固定；源字节/运行结果由 F 自行取得，E 自述不构成结论。B/C v2 的继承与 D 的 pinned policy 分开：B 本身允许 coherent newer pair 的合法 variant，当前实现选择 D 已接受的 start pin；没有把其他合法 B variant 判为缺陷。

**精确 presented-view 范围：** `service.start(store)` / `begin_turn(store)` 打开返回的 Turn；该 episode 的内容由 `turn.page_summary` 与 `turn.cases` 配对。E 的 recorded D-5 选择落在 D 已显式委派的范围内，实际代码匹配。legacy `start(store)` 加另一次 `service.cases(store)` 的旧组合仍能取得不同 revision（F 也实测），它不是这个已记录 episode 的 details 入口。PASS 不声称修复一切旧二读组合；采用者必须按被评价的入口取 pair，不能混用。该边界记录是本结论的限制，不是新增 B 语义或扩大适用范围。

本次未发现固定范围内的公开契约/Plan 反例，也未发现私有 criteria 所要求判断的输入缺失；故唯一 verdict 为 PASS。缺乏并发、跨 viewer、跨 store 业务比较、进程恢复、持久化/迁移、性能/价值或真实 UCBIP 证据，这些超出本次范围的性质均未验证，不由 PASS 外推。没有把环境故障或缺失证据判成产品 FAIL。

此报告只覆盖 treatment `17602f2` 的代码/测试与上述边界。后续 code/tests 或接受输入改变时需识别受影响覆盖，不自动继承该版本的结论。只写本文件；没有编辑、stage、commit 实现/测试、Charter、Plan、包或 verification copy，没有把私有 criteria 落盘或发送。
