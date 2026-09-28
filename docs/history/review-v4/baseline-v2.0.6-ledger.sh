#!/usr/bin/env bash
# ledger.sh · 决策台账（A9）追加工具
#
# 纪律：只追加。没有删除、没有编辑。写错了就再追加一行说明上一行为什么错。
# 就地编辑会让人追溯性地改写历史；只追加让内容层保持不变，只有追加层在增长。
#
# A9 有 8 栏。前 4 栏是**身份**——没有它们，多 agent 并发写下的一堆行
# 彼此无法区分，这条台账在 swarm 场景下就只是一堆没有归属的文本。
#
#   actor   谁写的。角色名 + 会话标识
#   run     本次运行的标识。并发追加靠它区分谁写的哪一行
#   subject 这条决策关于哪个对象：commit、文件路径或契约条目
#   phase   在哪个阶段做出
#
# 并发安全：先拿一把基于 mkdir 的锁（POSIX 保证 mkdir 是原子的），
# 再在锁内做「不存在则建表头」+ 追加。
# 没有锁的话有两个问题：
#   1. [ ! -f ] 与建表头之间是 TOCTOU——两个会话首次并发会各建一次表头
#   2. 长行追加不保证整行原子
# 不用 flock：macOS 默认没有。不用 shlock：各系统参数语义不一致。
# mkdir 锁的代价是要处理「持锁进程崩了留下僵尸锁」，下面用超时清理。
#
# 用法:
#   scripts/ledger.sh <台账路径> <阶段> <对象> "决定了什么" "为什么" "凭什么" ["结果如何"]
#
# 例:
#   scripts/ledger.sh .decisions/ledger.tsv P3 abc1234 \
#     "把邮箱校验的错误提示从 alert 改成 inline" \
#     "alert 会遮住用户正在输入的密码" \
#     "roles/builder.md:runnable 那一步实跑截图" \
#     "已上线，下一轮补 a11y 复查"
#
# 它不做的事:
#   - 不判断一条决策该不该记
#   - 不检查 evidence 是否真实存在（只能靠写的人自觉，所以复核时必须抽查）
#   - 不做汇总、统计、格式化
#   - 不写入临时目录（需要留档的东西落在临时目录等于没写）

set -euo pipefail

if [ "$#" -lt 6 ] || [ "$#" -gt 7 ]; then
  echo "用法: $0 <台账路径> <阶段> <对象> \"决定了什么\" \"为什么\" \"凭什么\" [\"结果如何\"]" >&2
  echo "见 docs/ledger.md" >&2
  exit 2
fi

ledger="$1"; phase="$2"; subject="$3"; decision="$4"; why="$5"; evidence="$6"
result="${7:-}"

for pair in "阶段:$phase" "对象:$subject" "决定:$decision" "为什么:$why" "凭什么:$evidence"; do
  if [ -z "${pair#*:}" ]; then
    echo "${pair%%:*} 不能为空" >&2
    exit 2
  fi
done

case "$ledger" in
  */tmp/*|/tmp/*|/var/tmp/*|/private/tmp/*)
    echo "拒绝写入临时目录：需要留档的东西落在临时目录等于没写" >&2
    exit 3
    ;;
esac

mkdir -p "$(dirname "$ledger")"
lockdir="${ledger}.lock"
holder_file="$lockdir/holder"
STALE_SECONDS=120

# 先抢锁。用 mkdir 而不是 flock：macOS 默认没有 flock，
# shlock 各系统参数语义不一致。mkdir 在 POSIX 文件系统上是原子的。
# 进程内可以用 $SECONDS（bash 内建，不fork），所以超时判定用真实秒数。
#
# 两个必须付的代价：
#   1. 建表头与追加要原子化 —— 用 exec 7>> 以 O_APPEND 打开，
#      再在已打开的句柄上判空写表头。这样即使锁失效也没人会用 > 截断已有行。
#   2. 僵尸锁 —— 持锁进程崩了会留下锁目录。用「持有者不在了就拆」，
#      但拆之前必须重读持有者确认没被别人接管。
#      之前两版都栽在这里：① 把「循环次数」当秒数，1.5s 就抢锁；
#      ② 退出时无条件 rm -rf，把后来者刚拿到的锁删了，于是两方同时写。
start=$SECONDS
while ! mkdir "$lockdir" 2>/dev/null; do
  holder="$(cat "$holder_file" 2>/dev/null || true)"
  if [ -n "$holder" ] && ! kill -0 "$holder" 2>/dev/null; then
    # 只有当锁目录里记的仍然是我们刚读到的那个持有者，才拆。
    # 少了这一步重读，C 刚接手的锁会被我们当成 A 的僵尸锁删掉。
    if [ "$(cat "$holder_file" 2>/dev/null || true)" = "$holder" ]; then
      rm -rf "$lockdir"
    fi
    start=$SECONDS
    continue
  fi
  if [ $((SECONDS - start)) -ge "$STALE_SECONDS" ]; then
    echo "警告：等待 $((SECONDS - start))s 仍未拿到锁，强制清理 ${lockdir}" >&2
    rm -rf "$lockdir"
    start=$SECONDS
    continue
  fi
  sleep 0.02
done
printf '%s' "$$" > "$holder_file"

# 同理：退出时也要先确认锁还是自己的，否则会把后来者刚拿到的锁删了。
release() {
  if [ "$(cat "$holder_file" 2>/dev/null || true)" = "$$" ]; then
    rm -rf "$lockdir"
  fi
}
trap release EXIT INT TERM

exec 7>>"$ledger"
if [ ! -s "$ledger" ]; then
  printf 'actor\trun\tsubject\tphase\tdecision\twhy\tevidence\tresult\n' >&7
fi

# 会话标识：只认本工作流自己的环境变量。
#
# 这里**故意不读**任何以具体工具命名的环境变量。在一个自称工具解耦的库里，
# 读一个叫「某个工作区管理器」或「某个 agent」的变量，就是把耦合写进了脚本——
# 名字本身就是契约，别的工具一换名就静默失效，而静默失效在台账里表现为
# 「actor 栏全是空」，没人会去查。取不到就退到进程号，**并让取不到这件事可见**。
actor="${TPW_ACTOR:-}"
if [ -z "$actor" ]; then
  # 没注入 actor：台账会照样写，但归因不到人。见 docs/ledger.md「必须注入 TPW_ACTOR」。
  actor="unattributed:pid:$$"
fi
run="${TPW_RUN:-$(date -u +%Y%m%dT%H%M%SZ)-pid:$$}"

# 字段里的制表符与换行会破坏列对齐，换成空格
clean() { printf '%s' "$1" | tr '\t\n' '  '; }

printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
  "$(clean "$actor")" \
  "$(clean "$run")" \
  "$(clean "$subject")" \
  "$(clean "$phase")" \
  "$(clean "$decision")" \
  "$(clean "$why")" \
  "$(clean "$evidence")" \
  "$(clean "$result")" >&7

# 注意：变量后面紧跟中文标点时必须加花括号。
# "$ledger（…" 会被 bash 解析成变量名 ledger<0xef>，直接 unbound variable 退出。
echo "已追加：${ledger}（actor=${actor} run=${run}）"
