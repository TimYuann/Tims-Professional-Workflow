#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""B/C/D 批验收情景 · 从库文件现场文本提取规则行并按情景断言。

被断言的句子全部从 roles/*.md、pipeline.md、AGENTS.md、README.md、SOURCES.md、
scripts/check-library.py 现场读出；脚本只做"这条规则在不在、有没有被矛盾占据"的判定。
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def lines(rel: str, pattern: str) -> list[str]:
    pat = re.compile(pattern)
    return [ln.strip() for ln in read(rel).splitlines() if pat.search(ln)]


FAILED = []


def check(name: str, cond: bool, detail: str) -> None:
    print(("  [PASS] " if cond else "  [FAIL] ") + name + " :: " + detail)
    if not cond:
        FAILED.append(name)


def hits(name: str, rel: str, pattern: str, want: bool = True) -> list[str]:
    rows = lines(rel, pattern)
    check(name, bool(rows) == want, ("%d 行" % len(rows)) + ("" if rows else "（期望 %s）" % ("有" if want else "无")))
    for r in rows[:2]:
        print("        命中: " + r[:150])
    return rows


def scenario(title: str) -> None:
    print("\n" + title)


def main() -> int:
    print("B/C/D 批验收（规则提取自库文件现场文本；ROOT=%s）" % ROOT)

    scenario("[R1] 跨过「开始实现」前必须对齐；说明≠批准；送达失败不得写「已说明」")
    hits("driver §4.9 存在", "roles/driver.md", r"^### 4\.9 推进前说明")
    hits("硬线只有一条：跨过开始实现前已送达", "roles/driver.md", r"唯一不可让的硬线：跨过「开始实现」这条线之前")
    hits("时机提示不等于同等强制点", "roles/driver.md", r"触发条件（时机提示，不是同等强制点）")
    hits("送达≠批准", "roles/driver.md", r"不把收到说明误当批准")
    hits("发送失败不得写已说明", "roles/driver.md", r"发送失败或无法确认送达时不得写")
    hits("§4.1 交叉提示", "roles/driver.md", r"交叉提示\*\*：需 Owner")
    hits("pipeline §10 说明不产生授权", "pipeline.md", r"推进前说明不产生授权")
    hits("pipeline §10 硬线", "pipeline.md", r"唯一硬线：跨过「开始实现」这条线之前必须已用自然语言对齐")
    check("R1 不把首次派出写成与实现前同等强制", "必须已向 Owner" not in read("pipeline.md"), "pipeline 未要求发卡即对齐")

    scenario("[R3] 环境阻塞按类分流；Verifier 自建前提要披露；doctor 绿≠原缺陷已修")
    hits("driver §4.2 第 5 步", "roles/driver.md", r"环境阻塞按\*\*资源可用\*\*前置边处置")
    hits("driver §6 环境阻塞行", "roles/driver.md", r"环境阻塞（缺种子数据/服务/凭据")
    hits("verifier 自建前提披露", "roles/verifier.md", r"\*\*我自建过前提时\*\*")
    hits("doctor 报红条件与真实入口", "roles/verifier.md", r"哪一条坏条件能让 doctor 报红")
    hits("自检红一例不足以自判装置可靠", "roles/verifier.md", r"自检红一例只证明该例会被抓住")
    hits("environment 含义列含装置来源", "roles/verifier.md", r"另写装置来源（复用项目已有/临时自建）")
    hits("verifier §6 进仓/唯一放行闸", "roles/verifier.md", r"我自建的前提要进仓")
    hits("重估旧证据环境等价性", "roles/verifier.md", r"重估旧证据的环境等价性并重新跑原主张")
    hits("driver 路由含 doctor 绿不等于已修", "roles/driver.md", r"doctor 绿不等于原缺陷已修")
    hits("investigator 具名阻塞分流", "roles/investigator.md", r"交\*\*具名阻塞\*\*")

    scenario("[R4] 意外失败先停/保全证据/分诊；建不出回路具名阻断；回归保护不留浅测试")
    hits("investigator §4.1 第 0 步", "roles/investigator.md", r"^0\. 遇到\*\*意外\*\*的测试失败")
    hits("停在当前改动 + 脱敏报错原文", "roles/investigator.md", r"先\*\*停在当前改动\*\*，保存脱敏的报错原文")
    hits("五层分诊面", "roles/investigator.md", r"测试本身 / 产品代码 / 构建与配置 / 外部依赖 / 数据与共享状态")
    hits("回路成立 + 具名阻塞", "roles/investigator.md", r"交 `roles/driver.md` 一份\*\*具名阻塞\*\*")
    hits("§7 阻断交付状态", "roles/investigator.md", r"阻断交付（合法停机，不等于算做完）")
    hits("阻断不产字段缺失正式报告", "roles/investigator.md", r"不产字段缺失的正式 `investigation-report`")
    hits("阻断不派空 repro_command", "roles/investigator.md", r"不向 Architect/Implementer 派空 `repro_command`")
    hits("阻断不得记成诊断 PASS", "roles/investigator.md", r"不得记成诊断 `PASS`")
    hits("implementer 回归保护 + 不许浅测试冒充", "roles/implementer.md", r"把红→绿检查保留为回归保护")

    scenario("[R5] bugfix 旧基线红→绿独立复现；取不到旧环境不伪造；Reviewer 不是实现循环")
    hits("verifier §2 bugfix 副收据", "roles/verifier.md", r"仅\*\*报告过的 bugfix\*\*")
    hits("实际对应到旧基线", "roles/verifier.md", r"实际对应到旧基线")
    hits("不伪造一次「亲眼看红」", "roles/verifier.md", r"不伪造一次「亲眼看红」")
    hits("证明不了就进 uncovered", "roles/verifier.md", r"证明不了就在 `uncovered` 标明")
    hits("新功能不强求历史基线红", "roles/verifier.md", r"新功能 / 纯静态改动不强求历史基线红")
    hits("§7 算做完含旧基线红→绿", "roles/verifier.md", r"报告过的 bugfix 另有旧基线的红→绿实际对应")
    hits("没说亲眼见红不算做完", "roles/verifier.md", r"把没跑过的旧基线绿灯说成")
    hits("reviewer 4.5 判据证伪不是实现循环", "roles/reviewer.md", r"判据证伪\*\*，不是再写一轮产品实现")

    scenario("[R6] 术语裁定权归业务侧（Owner 裁定）；无授权角色则挂起；Architect 只查证/备选/记录")
    hits("architect §4.9 存在", "roles/architect.md", r"^### 4\.9 术语冲突")
    hits("裁定权 = 项目 Owner 或 Owner 授权业务角色", "roles/architect.md", r"裁定权 = 项目 Owner 本人，或 Owner 书面指定 / 明确授权的业务角色")
    hits("没有这样的角色 → 挂起待裁", "roles/architect.md", r"没有这样的角色可问时 → \*\*挂起待裁\*\*")
    hits("Architect 职责只到查证/备选/记录", "roles/architect.md", r"Architect 的职责只到：查证")
    hits("新建词汇表需 Owner 同意 + 先映射权威文档", "roles/architect.md", r"先经 Owner 同意，并先映射该项目已有的权威文档")
    hits("不就地新建第二事实源（反例）", "roles/architect.md", r"为同一个词在项目里新造第二份词汇文档")
    hits("investigator 保留原症状用词", "roles/investigator.md", r"\*\*保留原症状用词\*\*")
    hits("reviewer 词义冲突报阻断指向有权者", "roles/reviewer.md", r"不由审查方替业务定名")
    hits("planner 未决词义不得自行定名", "roles/planner.md", r"未决词义不得由切片自行定名")
    hits("implementer 不自行定名", "roles/implementer.md", r"不自行定名")
    hits("driver 路由到 Owner/授权业务负责人", "roles/driver.md", r"领域含义待定（词义冲突、无定义新词）")
    check("driver 路由不以 Oracle 代授权", "不以 Oracle 代授权" in read("roles/driver.md"), "0 残留")

    scenario("[R7] 性能症状：改动前基线→定位→单因素改动→同条件复测→无对照只报未测出")
    hits("investigator §4.8 存在", "roles/investigator.md", r"^### 4\.8 性能症状")
    hits("改动前取重复基线", "roles/investigator.md", r"先在\*\*改动前\*\*以固定输入")
    hits("按症状选测量对象", "roles/investigator.md", r"按症状选测量对象")
    hits("无有效基线按 §4.1 第 5 步阻断", "roles/investigator.md", r"无法取得有效基线时，按 §4.1 第 5 步交具名阻断")
    hits("§7 性能结论边界", "roles/investigator.md", r"性能结论边界")
    hits("verifier 同条件复测", "roles/verifier.md", r"同一命令 / 预热 / 缓存 / 样本条件")
    hits("没有授权阈值不得自设门", "roles/verifier.md", r"没有授权阈值不得自设门")
    hits("记录保留与放弃的尝试", "roles/verifier.md", r"记录保留与放弃的尝试及其读数")
    hits("implementer 单因素改动", "roles/implementer.md", r"\*\*绩效分支\*\*：一次候选只处理\*\*一个可归因的性能因素\*\*")
    hits("绩效回退 = 新候选 + 新冻结", "roles/implementer.md", r"绩效回退 = 新候选 \+ 新冻结")

    scenario("[R8] 一条权威规则 + 内联登记；两轮硬规定；停手条件按角色自守；估算不是门")
    hits("AGENTS 原则 8", "AGENTS.md", r"决定者、权威位置、写者分别点名")
    hits("AGENTS 收件四步", "AGENTS.md", r"收件四步＝清点、核对、缺则退回、齐则开工")
    hits("AGENTS 内联副本需同步复核", "AGENTS.md", r"维护者改权威规则时要同步复核所有副本")
    hits("AGENTS 生成视图不得手工维护", "AGENTS.md", r"生成视图不得手工维护")
    hits("reviewer 两轮硬规定", "roles/reviewer.md", r"两轮是本库硬规定")
    hits("reviewer 不得被装配参数覆盖/放宽", "roles/reviewer.md", r"不得被装配参数覆盖或放宽")
    hits("driver §4.5 只路由、不设第二个默认值", "roles/driver.md", r"审查侧不在这里设第二个默认值")
    hits("driver 停止=归因转手", "roles/driver.md", r"停止发第三次同前提修复，把这次停止记为一次\*\*归因转手\*\*")
    hits("investigator 同前提换新证据要写下区别", "roles/investigator.md", r"换前提或引入新证据后重开的尝试，写下与上一链的区别")
    hits("planner 不设第二个轮次默认值", "roles/planner.md", r"审查链的轮次上限不在这里写")
    hits("pipeline §7 两种不同事件", "pipeline.md", r"两种不同事件，不是通用轮次表")
    hits("planner 数字三类", "roles/planner.md", r"授权门槛\*\*（需来源与可失败命令）/ \*\*估算输入\*\*")
    hits("planner 文件数不是门", "roles/planner.md", r"文件数本身不是必须拆的门")
    hits("planner expand–contract", "roles/planner.md", r"机械宽范围改动可用 expand–contract")
    hits("planner §5 估算/测量值不当门", "roles/planner.md", r"把 `change_cost`、体量估算或一次测量值当成准入门")
    hits("architect 成本是比较输入不是门", "roles/architect.md", r"带依据的比较输入，不是准入门")
    hits("SOURCES 4.10 记录 D2 裁定", "SOURCES.md", r"Owner D2 裁定（2026-09-26）")
    check("残余矛盾处置已清", "要不到就按最小范围处理" not in read("roles/driver.md") + read("roles/architect.md") + read("roles/planner.md") + read("roles/implementer.md") + read("roles/reviewer.md") + read("roles/verifier.md") + read("roles/integrator.md"), "0 残留")

    scenario("[R9/D4] 删除失真脚本并如实声明；固定 commit + 干净 checkout；checker 不是工作流 PASS")
    check("脚本已删除", not (ROOT / "scripts/check-team-version.sh").exists(), "scripts/check-team-version.sh 不存在")
    hits("AGENTS 不提供漂移检测脚本", "AGENTS.md", r"本库当前不提供漂移检测脚本")
    hits("AGENTS 固定 commit", "AGENTS.md", r"下游必须\*\*按固定 commit 引用\*\*")
    hits("AGENTS 干净 checkout", "AGENTS.md", r"checkout 必须干净")
    hits("AGENTS 固定 commit 不自动锁工作区", "AGENTS.md", r"不自动锁执行中实际读取的工作区")
    hits("AGENTS 纪律 6 checker 不是 PASS", "AGENTS.md", r"不是角色工作流的 PASS，也不检验某次交接物的真实值")
    hits("AGENTS 收件人按 §2 核实", "AGENTS.md", r"某次交接由收件人按角色文件 §2 核实")
    hits("AGENTS 树已移除该脚本", "AGENTS.md", r"sync-upstreams.sh       Layer 1")
    check("AGENTS 树不再列该脚本", "check-team-version" not in read("AGENTS.md").split("## 目录职责")[1].split("## 本仓工作边界")[0], "0 命中")
    check("README 目录不再列该脚本", "check-team-version" not in read("README.md").split("## 目录")[1], "0 命中")
    hits("README 自检判不了", "README.md", r"它判不了")
    hits("README 新增检查保留判据", "README.md", r"新增库级检查的保留判据")
    hits("check-library 头注明同义重复须人审", "scripts/check-library.py", r"同义重复（同一含义的措辞在库内没有唯一权威位置时，只能人审）")
    hits("check-library 输出注明同义重复", "scripts/check-library.py", r"同义重复\"\)")
    hits("SOURCES §8 记 D4 已删", "SOURCES.md", r"已删除\*\*（Owner D4 裁定，2026-09-26）")

    scenario("[交叉] R2-⑨ / R3-② / R8 单文件自包含 / R9 收件人门")
    hits("资源就绪仍需断言环境（不能只看 ready 标签）", "roles/verifier.md", r"把环境事实从\"记录\"升级为\"断言\"")
    hits("实例启动必须晚于候选生成（旧构建探针不得宣称 PASS）", "roles/verifier.md", r"进程启动时间必须晚于候选生成时间")
    hits("写入隔离与实际加载来源一致", "roles/verifier.md", r"整个运行期间写入隔离与实际加载来源一致")
    hits("环境与对象不成立先报协调方不开验", "roles/verifier.md", r"这些条件不成立就\*\*先报协调方，不开始验证\*\*")
    hits("错误测试先判测试自身", "roles/investigator.md", r"测试本身 / 产品代码 / 构建与配置 / 外部依赖 / 数据与共享状态")
    hits("收件人不把发件人说法当现场事实", "roles/verifier.md", r"不把\"发件人说有\"当作\"现场确有\"")
    hits("AGENTS 明写某次交接由收件人核实", "AGENTS.md", r"某次交接由收件人按角色文件 §2 核实")
    rev47 = read("roles/reviewer.md").split("### 4.7")[1].split("## 5")[0]
    check("reviewer §4.7 单文件自包含：不引用 pipeline.md", "pipeline.md" not in rev47, "0 引用")
    check("reviewer §4.7 自带升级去向", "升级给独立复核或设计方" in rev47, "含升级去向")
    check("reviewer §4.7 自带两轮硬上限", "两轮是本库硬规定" in rev47, "含硬上限")
    check("reviewer §4.7 自带换对象不重置", "不许靠换对象或换人来重置轮次" in rev47, "含不重置")
    check("R1 的已说明不得用自写记录充数", "拿一条自己写的记录充作 Owner 已收到" in read("roles/driver.md"), "0 残留")

    print("\nB/C/D 批验收结论: " + ("全部通过" if not FAILED else "存在 FAIL: " + "; ".join(FAILED)))
    return 0 if not FAILED else 1


if __name__ == "__main__":
    sys.exit(main())
