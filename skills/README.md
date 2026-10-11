# TPW 工程 Skills · 本机自用固定成品包

本目录是两个成品技能根，供宿主（Pi 或兼容 Agent Skills 的 harness）**按固定对象安装使用**：

| 技能根 | 正文来源（TPW 固定方法） |
| --- | --- |
| `tpw-debug/` | `professional-workflow/methods/local-defect-feedback-loop.md` |
| `tpw-cross-module-design/` | `professional-workflow/methods/cross-module-design.md` |

固定身份：源仓 pin `f5d6d0547459eb15c40aec25617418d5ea4710e6`，tree `9d7c057417da73895cda3b85ec34d49db58669b6`。两个 `SKILL.md` 的正文段是该 pin 下方法正文的**逐字节**内容（只前置 frontmatter 与「包装与资源边界」一节）。逐文件校验值见各根 `SOURCE.md`。

本包**不含**：42 方法的搬运、registry／upstreams 平台、上游仓库整体复制、公开发行许可。它只是两个技能的成品目录 + 记录。

## 安装（本机自用）

宿主侧步骤建议如下，目的是保证默认发现只有一份、且指向不可变内容：

1. **把本目录整体复制到自动发现根之外的版本目录**，例如 `~/.agents/skill-versions/tpw-f5d6d054-lp20261011/`（名字自带 pin 与包装日期）。版本目录一旦建立即视为不可变；要更新就建新版本目录。
2. **只由发现根的两个入口指向该版本目录**（复制两个技能根，或让入口指向版本目录内的同名根）；**不要指向源仓工作树或当前 `main`**，避免 `main` 一移动成品就漂移。
3. **旧版与备份不要放进技能扫描树**，否则会形成第二个默认入口。旧版按上述“版本目录”方式保留在扫描树外，旧任务继续按固定对象取回。
4. 安装后可用 `/skill:tpw-debug`、`/skill:tpw-cross-module-design` 显式调用。默认发现只提供简介；正文按需加载。

安装前请先读两个技能根的 `SKILL.md` 与 `SOURCE.md`；本包默认不执行任何脚本。

## 引用解析范围

本包**只保证随包资源**（各根 `SKILL.md` 中「包装与资源边界」列出的读取型／条件执行／条件读取文件）能按相对本技能目录解析。正文里出现的另外两类路径**不属于本包、也不在本包内解析**：

- **上游来源锚**（如 `skills/engineering/diagnosing-bugs/SKILL.md`、`pstack/…`）：出处记录，按上游 pin 取回。
- **TPW 方法集引用**（`methods/*.md`，正文中一处 `methods/behavior-claim-evaluation.md`）：按 TPW 固定 pin／`professional-workflow/methods/…` 绑定；该文件在 pin `f5d6d054` 中存在（已核）。

## 旧任务版本不漂移

- 任务引用一律写**固定对象**：包自身提交（`git log -1 --format=%H -- skills/` 取包装提交）或本包记录的 pin／tree／路径；不写“最新 main”。
- 需要旧版本时按上述版本目录取回，不改进行中的任务；升级＝新固定对象 + 重新核受影响的引用。

## 许可边界

- **本机自用**：Neil 于 2026-10-11 授权本轮在本机安装／使用本成品。
- **公开发行**：未授予许可。上游 MIT 条款不用于推断 TPW 自有融合增量的条款；正式对外分发前须由 Owner／TPW 维护者确认。
- 上游许可原文见各根的 `THIRD-PARTY-NOTICES.md`（Matt／Addy／pstack／cursor-team-kit 四份 MIT，已与各上游 `LICENSE` 逐条核对）。

## 静态检查（已执行，可复跑）

| 检查 | 命令要点 | 结果 |
| --- | --- | --- |
| 正文逐字节 | 两个 `SKILL.md` 的正文段 SHA-256 与源方法文件比对 | 一致（`0feec14d…`／`373ff499…`） |
| 资源逐字节 | 每个随包资源与其固定来源比对 SHA-256 | 一致（见各 `SOURCE.md`） |
| 相对路径 | 对两个技能根声明的随包资源逐一断言存在（相对技能根），并扫描 `SKILL.md`／`SOURCE.md` 其余反引号路径 token 分类 | 随包资源 **10/10 可解析**；其余 34 条＝上游来源锚 33 + TPW 方法集引用 1（`methods/behavior-claim-evaluation.md`，在 pin 中存在），按设计不在本包解析 |
| Bash 语法 | `bash -n tpw-debug/scripts/hitl-loop.template.sh` | 通过（未执行） |
| 入口发现 | 用宿主静态解析扫描本目录，统计技能入口与诊断 | 恰好 2 个入口、0 诊断 |

未执行：HITL 模板、任何产品命令、任何网络或安装动作。
