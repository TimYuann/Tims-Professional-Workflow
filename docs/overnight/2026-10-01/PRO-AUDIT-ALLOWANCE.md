# Owner 追加：两次 ChatGPT Pro 完整产物审核

2026-10-01 Owner 明确授权本夜最多两次 ChatGPT 6 Pro 审核，由 Oracle 决定调用时机；不是每阶段 mandatory gate。
使用 ego-browser 打开 chatgpt.com，核实际模型与 Pro 档位，在 composer 挂 GitHub connector。
为审核可将已提交的夜间候选分支推到 origin `https://github.com/TimYuann/Tims-Professional-Workflow.git`；只推本夜独立分支，不推 main、tag 或 force-push，不混原工作区 dirty/index。
这项追加授权覆盖接受计划中的“本夜不 push”限制，仅限本审核所需分支。其他生产／发布／UCBIP修改保留边界不变。

首选时机：第一次 M5 完整集成对象（Profile+Charter+路由+精选方法+M3证据）；第二次 M6 固定交付对象及资格证据。不是用零碎草稿消耗额度。
Driver 准备 fixed commit／tree、远端 branch、最短完整核读清单、已验/未验范围。Oracle 负责是否使用与浏览器送审；Driver 不自动发起第三次或再让 Owner 手工转述。
GitHub connector 必须实际挂入 composer，审核提示要求读取对应 repo/branch/commit，不把网页摘要或缓存 main 当候选源码。
Pro 返回是独立 challenge，不证明真实运行或替代本地 F；发现项合并后只重验受影响 claim 与证据覆盖。
记录 audit 次数、对象、模型/Pro可见证据、GitHub连接状态、对话URL、完整回答与处置。未发送不耗额度；提交后不因返回不满意重置计数。
登录、connector权限或指定 Pro 配置不可用时，诚实记阻断，不替换为普通模式冒充Pro；不阻断其他已授权夜间工作。

## 使用记录

当前：0 / 2 已发送。浏览器仅预检，未送审。实际调用后追加记录。
预检已成立：ego TaskSpace 19／p1，chatgpt.com已登录；composer中可见GitHub chip；模型菜单显示“6 / Pro”。菜单文本证据暂存 /private/tmp/tpw-night-prompts/chatgpt-pro-preflight.txt。正式发送前再核候选对象与该状态，不把预检当审核结果。

### Audit 1 · 已发送，等待结果（覆盖前述当前额度状态）

当前使用 1 / 2。Oracle 已先push远端night分支到 d0f208f80e573527dd42a512eb2ac2bc559e8cd3，并ls-remote读回完全MATCH。审阅候选62e3792/root tree c0f3a47、package subtree9e4fa14保持固定；远端tip只加过程/交接记录。
2026-10-01使用同一ego TaskSpace19/p1；发送前模型菜单再次实显6/Pro，composer中GitHub chip可见；draft Unicode/候选SHA检查通过。已观察新聊天URL和Pro思考／GitHub核读进度，非仅点击回执。
对话：https://chatgpt.com/c/6abe03be-ad9c-83e8-852e-d882fb600552。
完整请求与模型证明在仓库 .worktrees/runtime/tpw-night-prompts/pro-audit-1-request.txt、pro-audit-1-model-proof.txt；结果尚未取回，不声称已通过。
旧Luna Driver已收口退休；新的同名Pi Driver为独立session 01a0f639-ecce-7195-817b-05c3fe8d68ea，Flash/max实测，等待Oracle吸收结果再派明确范围。名字相同不改写旧贡献记录。
