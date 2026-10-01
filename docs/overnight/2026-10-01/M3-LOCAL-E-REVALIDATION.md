## M3 case 1 · E 方法绑定复验 — 报告

### 固定输入核验
```
d6e2768326fede1856cae430f07f566ca562e41ca827976560f84adf36b6444b  docs/overnight/2026-10-01/fixtures/m3-local-fix/STARTUP-PROMPT.md
ecfc6195726fe62321208ad766fcbe7005c784c6d2aece7f9b2a2eca4ef293bb  CONTRACT.md
90b7e06d06e525e79a58496cdf65603f15da18f15809a7e1e3a256a1f904167e  TASK-INPUT.md
6e8262b6361be36abc39947cf00fef02adac9c9120f353e5b38070c84e119a57  BASELINE.md
```
四个哈希与 Charter 一致；`python3 --version` → `Python 3.14.4`。候选版本（`9699276`）为 `" ".join(value.split()).upper()`，前置缺陷版本（`0452132`）为 `value.strip().upper()`。

### 观察 1 — 原始失败场景命令（fixture 目录内）
```
$ python3 -m unittest discover -s tests -v
Ran 7 tests in 0.000s
OK
EXIT=0
```
同一命令连跑两次，结果一致（含 `test_collapses_internal_whitespace` → ok）。

### 观察 2 — 区分性探针（方法与步骤 1/3）
同一输入 `" \tNorthern   Star\n"`，两个实现各一次：
```
pre-change (strip().upper()) -> 'NORTHERN   STAR'
candidate  (split()-join)    -> 'NORTHERN STAR'
contract expected            -> 'NORTHERN STAR'
```
确定性：候选实现该探针重复 1000 次，唯一结果 `{'NORTHERN STAR'}`；函数纯、无状态/时序/随机依赖。

### 观察 3 — 负控制（每次只改一个条件，全部走公开函数）
```
leading/trailing only  '  north  '        -> 'NORTH'        PASS
internal run only      'north   star'     -> 'NORTH STAR'   PASS
mixed run+punctuation  'north\t-\n star'  -> 'NORTH - STAR' PASS
whitespace-only        ' \t\n'            -> ''             PASS
empty                  ''                 -> ''             PASS
hyphen preserved       'north-star'       -> 'NORTH-STAR'   PASS
non-string             None               -> TypeError('value must be a string')  PASS
```

### 观察 4 — 前置版本回放（只读、进程内替换 `src.labels`，未写盘）
对前置实现跑现有 7 个用例：`run=7 failures=3 errors=0`。原始失败逐字重现：
```
AssertionError: 'NORTHERN   STAR' != 'NORTHERN STAR'   (test_collapses_internal_whitespace)
```
另两个红是候选自带的回归用例（`alpha \t\n beta`、`north\t-\n star`）在前置代码下变红 → 该回归覆盖非空转，落点是 `normalize_label` 公开行为接缝，不需要 test-only 抽象。

### 覆盖与结论
- 契约 6 条（首尾空白、内部空白折叠为单个 ASCII 空格、保留标点、空/纯空白→空串、非字符串 TypeError、签名不变）在当前候选上全部可观察通过。
- `src/labels.py` 在复验前后哈希不变 `f767787ba2ac8cf52e7b4f62e74b146b858fad91031bed139c849c9e23a92f87`；`tests/test_labels.py` `8dbf2858…`、`tests/test_labels_whitespace_runs.py` `d52e05f5…` 亦不变。

### 变更路径
**无。** 未写任何文件；写集内（`src/labels.py`、`tests/`）零改动，未触碰契约/任务输入/BASELINE/其他 fixture。`git status` 仅显示 `?? F-STARTUP-PROMPT.md`（非本次产生，且未读取）。

### 阻塞
无。剩余不确定（如实记录，未据此改码）：
1. 契约写「whitespace」未枚举字符集；`str.split()` 按 Unicode 空白判定，NBSP `\xa0`、NEL `\x85` 等会被归一为 ASCII 空格。这是契约措辞的歧义，不是本次委托可单方面裁决的对象。
2. 本次全部输出是 E 自验证据，按 Charter 不构成独立结论；被评价的固定候选版本是 `f767787b…`，由独立 F 实例评判。`EVALUATOR-CHARTER.md` 与 `F-STARTUP-PROMPT.md` 未读取，未推断任何 held F 判据。
