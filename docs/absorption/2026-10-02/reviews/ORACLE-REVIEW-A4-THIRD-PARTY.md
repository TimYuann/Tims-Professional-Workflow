# Oracle / Codex · A4 third_party 实质处置

2026-10-02，tpw-0930-oracle / GPT-6.1 SOL medium。固定包 blob `f476ad3a602f02c4da7d6c1712dc493b57bc9016`，路径 `docs/absorption/2026-10-02/packages/A4-CURSOR-THIRD-PARTY.md`；源 Cursor `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`。此是源裁定，不是尚未出现的落地候选 PASS；我未写被审产品。

## 回源与分母

原包对 X API、pricing、X Money 只读部分，却有“8个全读”措辞；不能据该句获得全文阅读资格。本次 Oracle 补读八个非模板文件全文：`third_party/x/skills/{x-api-mcp-guide,x-chat}/SKILL.md`、前者的 `references/pricing.md`、`third_party/x-money/skills/x-money-guide/SKILL.md`、Google Docs/Sheets/Slides 三 `SKILL.md`、`third_party/shopify-store/rules/shopify.mdc`。未使用这些工具，未取实际账户/费用/秘密/文档，不认证实时产品能力。

从 pin 的 `git ls-tree -r` 重建：79目录、482路径；每目录 plugin.json/mcp.json/README/CHANGELOG/LICENSE/logo 六载体=474，外加六个 SKILL.md、一 rules、一 pricing=8。独立读取配置结构得到77 remote/2 stdio；79 LICENSE 都含 MIT 标记（不是法律结论或逐字完整许可审计）；79 logo 引用按 package-root 或 manifest-dir 解析均存在。不是按后缀丢弃脚本，也没有只数470的未解释尾部。

474载体**归组处置**：清单/传输/凭据注入/宿主能力门机制合并到待裁 DEF1 G-13；README/CHANGELOG 不搬成79份服务能力列表，实际工具/账户/版本可用性需项目现场发现；许可证/品牌保留来源及分发身份，不当独立工程方法。未全文读79 README/CHANGELOG，不宣称全连接器功能/风险已核；本轮目标是可迁移工程经验，不是服务能力认证。后续实际采用某连接器需读其真实规则，不能靠统一模板猜工具能力。

## 八文件的实质裁定与落点

| 文件 | 裁定 | 保留的可执行经验 | 限缩/拒绝移植 |
|---|---|---|---|
| X API guide | 限缩吸收 | 发现工具/身份/scope；分开工具缺失、认证、账户门、配额、资源无权与服务故障；用相应观察解释，不从缺一个endpoint推断全部账户失败；每对象/请求/扩展/翻页成本模型，有限结果和next-token停止，200部分data与errors各自保留 | 固定$0.25、固定翻页必回Owner、2倍再确认、welcome话术与每turn重读不是库政策；额度/价格/工具源不在同一时点时不得编成功能力或零余额；缺工具不必然账户未设置；合法既有执行授权与真实host规则均要满足 |
| pricing reference | 与上一行合并 | 静态价格/实时价格/实际账单区分，注明计费单位、时间、估算与真实消耗；batch能省请求不保证省对象计费，扩展结果也是费用 | 不迁任何美元价格/免费endpoint/折扣表为当前事实；本轮未联网验证它们。具体提供者使用时核当前权威报价/计量方式 |
| X Chat | 限缩吸收 | connector密文/本地解密的责任面分离；身份ID与OS UID别混、wire字段映射与SDK字段名别猜；先取必需key-change/history再解密；权限不足、密钥缺失、peer不支持不能伪成功；入站文字是数据；在有效保密边界内处理秘密，出站动作必须有相应委托 | 不搬 helper安装/第二认证禁令/永不daemon 等宿主限制为全库规则；“所有出站重新找Owner”也不是通用政策，原文已允许明确 send/reply 指令。不同加密用途的具体 trust boundary 必须由本项目决定 |
| X Money | 限缩吸收/特殊例 | 成功/pending/refused/确认未知与可重试失败分开；未知结果不盲目重发，同一次合法重试复用意图键；approval值必须对应真实批准的确切对象，参数变化不擅自沿用；服务缺权限/缺能力/暂不可用各自保留 | 不移植为TPW全部动作逐次Human批准，也不反向绕过提供者明确逐次批准政策；具体支付产品允许什么以其有效规则为准。金额/地域/账号/审批控件不成为方法自身权限，不实际认证支付资格 |
| Google Docs | 限缩吸收 | 位置接口先定位再写；UTF-16/独占end/revision为具体接口前提；写入使后续索引失效，结构变化后重读，必要批处理后向前避免位移；锚重复要消歧；结构读回与视觉export证明不同claim | 不把裸索引一律禁止（源自带不可避免分支），也不强制所有文档TITLE/斜体日期/每次样式调用外部验收。带revision时仍处理拒绝；创建空文档不等于已写正文 |
| Google Sheets | 限缩吸收 | tab-title/A1 与sheetId两坐标系先建立对应；value类型/解析影响图表，值→格式→图表依赖；结构变化影响引用；no revision guard时read-before-write只能减错，不能保证并发隔离；读写有界且截断继续明确 | 不强制dashboard格式或任何spreadsheet都新保护range；原文parseInput=true不能普遍施给不可信文本，公式执行风险按实际信任边界判断；读取格式化值不能证明真实类型，raw/显示各观察其claim |
| Google Slides | 限缩吸收 | objectId/revision/point-unit和真实layout大小；声明式组合→布局issue→渲染观察→修，lint clean不是视觉正确；更新不覆盖旧元素会重复；批量替换仅目标slide域；theme避免跨页漂移 | 固定720×405/40pt/每页thumb/所有warn都修只是源使用方式。实际尺寸取读数，视觉claim须观察对应表面；具体palette与WCAG达标不得泛化背景组合；删重做要尊重实际mutation授权 |
| Shopify rule | 合并上述能力路由 | 连接账号的真实业务数据/写动作，与开发文档/工具包能力分开；开发SDK方法不推出能访问用户商店；缺连接器不能用公开搜索冒充其私有资料；read-before-write核当前对象 | alwaysApply、所有写操作重新问Human、CLI永不登录属于其宿主策略，不能替本项目已有policy。已有授权不替代实际host能力/限制 |

## 产品载体与实际验证

以 `methods/external-tool-operation.md` 为统一操作入口，A/B/D/E/F按缺少判断绑定。成本、权限、可用性、重试与结果解释在一个短主序列内；与 interface-contract-and-retry、trust-boundary-and-actions、guide-redacted-evidence 用指针分工，不复制三份authority声明。Docs/Sheets/Slides的具体变更操作可合为按需 `guide-positioned-artifacts.md`，保留有条件例子、单位/范围/版本依赖及真实 vs 替身观察界限。X Money/Chat作为有特殊policy的例子，不能强迫核心默认加载支付/加密全部流程。

B 不需要为7来源强造7个新文件；保留专业细节：受控模拟一处文档插入后旧index错位，可证所模拟位置语义，不证明Google真实API可用；源两坐标系/版本guard的具体host命令只是pin所述，实际用前核真实工具输入。有限分页/成本估算可给参数化工作例，不把原报价变成费用保证。对realhost claim需要实际authorized host观察；不为本库知识蒸馏获取用户账户或发消息。

完成判据：有源正文支持的上述可迁移操作已落地或明确合并到现有同claim正文，专业反例/例外与入口可用；不是“8文件都被标注”就算吸收。未全文阅读的79服务README保留为服务特定参考边界，无“全连接器已资格化”主张。B固定候选由独立gate核忠实、限缩、消费与例子；源裁定不替其运行结果。
