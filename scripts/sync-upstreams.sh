#!/usr/bin/env bash
# sync-upstreams.sh · 更新只读上游克隆并重新生成锁文件
#
# 这是本库唯一允许改动 upstreams/ 的脚本。**只改本地克隆的 refs，不改任何工作区文件**，
# 也不向上游推送。
#
# 它做两件事：
#   1. 拉取三仓最新（可选，见 --fetch）
#   2. 重新生成 upstreams.lock.yaml —— 101 个 skill 的路径 + 内容 sha256 + 每仓 pin
#
# 锁文件是随 release 分发的。它存在的理由：处置表要能被核对，
# 而核对不能依赖 upstreams/ 目录（那三个克隆被 .gitignore 挡着，从不随包分发）。
# 干净 clone 出来的下游要能跑检查，靠的就是这份锁文件。
#
# 用法:
#   scripts/sync-upstreams.sh            # 只重新生成锁文件，不碰网络
#   scripts/sync-upstreams.sh --fetch    # 先 fetch 三仓，再生成锁文件
#   scripts/sync-upstreams.sh --pin      # 把某个仓 pin 回上一个 commit（回退上游更新）

set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LOCK="$ROOT/upstreams.lock.yaml"
FETCH=0
PIN=""

while [ "$#" -gt 0 ]; do
  case "$1" in
    --fetch) FETCH=1; shift ;;
    --pin)   PIN="$2"; shift 2 ;;
    -h|--help) sed -n '2,20p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "未知参数: $1" >&2; exit 2 ;;
  esac
done

if [ -n "$PIN" ]; then
  # 回退形式：--pin <repo>=<commit>
  repo="${PIN%%=*}"; sha="${PIN##*=}"
  for d in "$ROOT/upstreams/cursor-plugins" "$ROOT/upstreams/mattpocock-skills" \
           "$ROOT/upstreams/addyosmani-agent-skills"; do
    if [ -d "$d/.git" ] && [ "$(basename "$d")" = "$repo" ]; then
      echo "把 $repo 回退到 $sha"
      git -C "$d" checkout --quiet "$sha"
    fi
  done
fi

if [ "$FETCH" = "1" ]; then
  for d in "$ROOT/upstreams/cursor-plugins" "$ROOT/upstreams/mattpocock-skills" \
           "$ROOT/upstreams/addyosmani-agent-skills"; do
    [ -d "$d/.git" ] || { echo "跳过（不是 git 克隆）：$d" >&2; continue; }
    echo "fetch $d"
    git -C "$d" fetch --quiet --all
  done
  echo
  echo "注意：fetch 之后**没有**自动 merge 或 checkout——"
  echo "更新哪个仓、pin 到哪个 commit，是维护者的决定，不是脚本的。"
  echo "改完之后重跑本脚本生成锁文件，再复核处置表。"
  echo
fi

[ -d "$ROOT/upstreams" ] || { echo "没有 upstreams/ 目录，本脚本无事可做" >&2; exit 0; }

exec python3 "$ROOT/scripts/_render-lock.py"
