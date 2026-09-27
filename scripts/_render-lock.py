#!/usr/bin/env python3
"""
_render-lock.py · 生成 upstreams.lock.yaml

只读 upstreams/，只写 upstreams.lock.yaml。不碰任何其他文件。
由 scripts/sync-upstreams.sh 调用，也可以单独跑（只读源 + 写一个文件）。
"""

import hashlib
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("需要 pyyaml：python3 -m pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
LOCK = ROOT / "upstreams.lock.yaml"

REPOS = {
    "pstack": "cursor-plugins/pstack",
    "matt": "mattpocock-skills",
    "addy": "addyosmani-agent-skills",
}
SKIP_DIRS = {"deprecated", "in-progress", "templates", "assets", "references",
             ".git", "automations", "third_party", "node_modules"}


def main():
    if not (ROOT / "upstreams").is_dir():
        sys.exit("没有 upstreams/ 目录。锁文件是**从上游实物生成**的——"
                 "没有实物就只能人工维护，那正是它要取代的东西。")

    skills, repos = {}, {}
    for prefix, rel in REPOS.items():
        base = ROOT / "upstreams" / rel
        if not base.is_dir():
            print(f"跳过 {prefix}：{rel} 不存在", file=sys.stderr)
            continue
        if (base / ".git").exists():
            head = subprocess.run(["git", "-C", str(base), "rev-parse", "HEAD"],
                                  capture_output=True, text=True).stdout.strip()
            date = subprocess.run(["git", "-C", str(base), "log", "-1",
                                   "--format=%ad", "--date=short"],
                                  capture_output=True, text=True).stdout.strip()
        else:
            head, date = "", ""
        repos[prefix] = {"path": f"upstreams/{rel}", "commit": head, "date": date}

        for root, dirs, files in __import__("os").walk(base / "skills"):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
            if "SKILL.md" not in files:
                continue
            skill_md = Path(root) / "SKILL.md"
            relp = skill_md.relative_to(ROOT)
            digest = hashlib.sha256(skill_md.read_bytes()).hexdigest()[:16]
            skills[f"{prefix}:{Path(root).name}"] = {
                "path": str(relp), "sha256": digest}

    lock = {
        "schema": "tpw-upstreams-lock/1",
        "why": "处置表的可核对性不能依赖 upstreams/ 目录——那三个只读克隆被 .gitignore "
               "挡着，从不随 release 分发。干净 clone 出来检查器直接红，"
               "而 coldstart 又要求把检查器复制到下游且不依赖本库运行时路径。"
               "这份锁文件就是那本可随包分发的账。",
        "verify": "有 upstreams/ 时 check-closure 会逐条比 sha256 并核 pin；"
                  "没有时只用它核对处置表与 sources。两种情况都必须通过。",
        "repos": repos,
        "skills": dict(sorted(skills.items())),
    }

    header = (
        "# 上游锁文件 · 随 release 分发\n"
        "#\n"
        "# 101 个上游 skill 的清单 + 内容 sha256 + 每仓 pin 的 commit。\n"
        "# 它是「处置表」与「上游实物」之间那本可随包分发的账：\n"
        "#   - 没有 upstreams/ 时，用它核对 registry 的处置表与 sources（干净 clone 也成立）\n"
        "#   - 有 upstreams/ 时，check-closure 会逐条比 sha256 并核 pin，把漂移抓出来\n"
        "#\n"
        "# 不要手工编辑。由 `scripts/sync-upstreams.sh` 重新生成。\n\n"
    )
    LOCK.write_text(header + yaml.dump(lock, allow_unicode=True, sort_keys=False,
                                       width=100), encoding="utf-8")
    print(f"已生成 {LOCK.relative_to(ROOT)}：{len(skills)} 个 skill，"
          f"{len(repos)} 个仓 pin")


if __name__ == "__main__":
    main()
