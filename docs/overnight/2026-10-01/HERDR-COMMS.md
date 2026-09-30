# 本夜混合会话通信

适用：Codex 与 Pi 的本夜 TPW 编队。统一使用 Herdr，不用 Pi Intercom；这份操作说明不进入工具无关的产品 core。

```bash
herdr agent list
herdr agent prompt tpw-night-driver '来自 <会话名>：<状态/问题>；产物 <路径>；需要 <下一动作>。'
herdr agent get tpw-night-driver
herdr agent read tpw-night-driver --source visible --lines 30
```

- 使用实时名册中的唯一 agent name 或 pane ID，不用 terminal ID；Herdr/Pi名称一致。
- 消息只传路由、状态与持久产物指针；事实、判断、条件和实际观察写进任务产物，收件人按需读回。
- `agent prompt` 向空闲会话开启一轮，工作中会话接收排队/steering。返回“送达”不证明已读、完成或接受。
- 通常不加 `--wait`；需要明确完成节点时可 `herdr agent wait <name> --timeout 60000`。生命周期 wait 不对应某一条消息，不用它猜测当前任务是否完成。
- 正常worker报告发 Driver；方法问题给 tpw-night-method；关键交付里程碑由 Driver 给 tpw-0930-oracle。普通消息不经 Owner 转发。
- 缺回复先继续无依赖工作；必要时单次 get/read核实，不持续轮询，不重复长篇ACK。
- 仅在已授权的TPW编队通信，不给UCBIP派活。后续新会话由Driver指向本文件即可，无需反复广播。

角色接口：tpw-night-method（Sol/medium）检查关键方法／配置／验证设计；tpw-0930-oracle 检查关键实际交付与接受条件。独立评价者仍按对象声明作者关系，不设每件产物双Sol gate。
