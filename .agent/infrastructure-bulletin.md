# KDO 基建变更公告

> 更新：2026-09-06  
> 面向：所有 Agent  
> **每个 Agent 启动时必须读此文件了解最新基建变更。**

## 2026-09-06 行为宪法 v1.1 第六条：kdo query 第一优先门禁（#669）

| 变更 | 内容 |
|:--|:--|
| 宪法 v1.0→v1.1 | 增补**第六条**：知识问题第一动作=`kdo query`（检索词同义/中英扩展 ≥2 变体）；0 命中或证据不足才降级 grep 兜底；诊断/调研/报告产出必附「kdo query 检索记录」节（查询词+命中数+日期），无检索记录=不闭环 |
| grep 降级双口径 | grep 只用于①kdo query 之后补充定位②非知识类检索（代码/配置/日志）。grep 沿自己足迹搜 ≠ 调研（W11 违例实证：grep 漏库内已有方法卡两周） |
| pre-submit 新门禁 | `kdo pre-submit` 新增 `KDO_QUERY_LOG` 检查：诊断/调研/报告类（frontmatter type=diagnosis/research/report 或落 60_feedback/diagnosis|diag|diags|analysis/）缺检索记录节 → **WARNING 软一周（至 2026-09-13）→ 升 HARD 拦截**；`KDO_QUERYLOG_HARD_DATE` env 可提前门禁化 |
| 谁改的 | 黄药师（任务单 #669，老朱直令「不信自律信门禁」，欧阳锋终审中） |

## 2026-09-06 拉起器通道健康预检+fallback（#656，F-073）

| 变更 | 内容 |
|:--|:--|
| 通道预检+fallback | `kimi-headless-launch.py` launch 前逐通道最小探针（1-token HTTP / CLI 级），主通道死→自动切下一个健康通道（todos+stdout 通知）；全死→**不硬派** exit 2 报王语嫣 |
| 通道-模型认知表 | `90_control/channel-model-map.md`——CLI 名→真实供应商→模型→key 指纹。**值守报通道必须连报真实供应商+模型**（claude.exe=智谱GLM，codex=relay→DeepSeek，kimi/hermes=kimi-for-coding 同墙） |
| 新 flag | `--no-probe` 应急跳预检硬拉；`--force-dead kimi,claude` 模拟死通道（测试钩） |
| 新台账 | `logs/channel-health.log`（append-only JSONL，每次拉起决策一行） |
| 谁改的 | 黄药师（任务单 #656，欧阳锋终审中） |

## 新增工具

| 工具 | 路径 | 用途 |
|:--|:--|:--|
| 卡片可用性模拟器 | `90_control/scripts/kcard-simulate-feedback.py --batch 5` | AI 扮演用户测试卡片能否用 |
| 新卡冲突检测 | `90_control/scripts/kcard-diff-new-vs-existing.py --new <id>` | 新卡入场自动对比旧卡 |
| 精修分级器 | `90_control/scripts/kcard-refinement-grader.py --card <id>` | A/B/C/D 四级精修深度评估 |
| 域摘要卡 | `30_wiki/domains/five-step-domain-digest.md` | 读一张读完一个域 |
| **知识自攻击** 🆕 | `/kdo-self-attack` 或 `60_feedback/adversarial/` | 四路Agent攻击知识卡片→人只审攻击报告 |
| **合成用户调研** 🆕 | `/demand-analysis-synthetic` | 多Agent角色扮演+全网验证，替代问卷 |
| **审查流程升级** 🆕 | 旧：逐卡读→新：先自攻击→再审报告 | 解决 E009/P-35 审查疲劳漏检 |
| **依赖冻结** 🆕 | `kdo freeze -c <card>` / `kdo freeze --all` | 对卡片引用的 wikilink 依赖做 SHA256 锁定 |
| **依赖校验** 🆕 | `kdo verify-deps` / `kdo verify-deps <card>` | 检测上游卡片是否变更/缺失 |
| **环境锁定** 🆕 | `kdo env-check --lock` / `kdo env-check` | 锁定并校验 Python/kdo/git 版本 |
| **批量回退** 🆕 | `kdo snapshot` / `kdo revert` / `kdo batch -f ...` | 批量操作前打 tag，失败可回滚 |
| **按域 lint** 🆕 | `kdo lint --domain <domain> --summary` | 只查看某个 domain 的 WARNING 数量，用于分域内容债清理 |

## 新增模板

| 模板 | 用法 |
|:--|:--|
| BTICME | `kdo scaffold --template bticme` — 背景+任务+方法+约束+示例 |
| PACED | `kdo scaffold --template paced` — 决策链还原（暗知识专用） |
| Book | `kdo scaffold --template book` — 书籍拆解 |

## 规则变更

| 规则 | 变更内容 |
|:--|:--|
| KF-025 | 三问→四问：新增"④跨域共同模式——每完成两个域做跨域对比" |
| 知识冲突 SOP | `90_control/contradiction-resolution-sop.md` — 新素材与旧卡冲突的四种处理 |
| 批量操作 P-30 | 任何批量操作前必须在任务文件声明预期变更范围 |
| 批量操作 P-31 🆕 | 批量操作前必须 `kdo snapshot` 或 `kdo batch`，保留回退 tag；失败时用 `kdo revert <tag>` 回滚 |
| EC 依赖冻结 🆕 | 关键卡片（如 EC 工业化产出卡）必须用 `kdo freeze` 锁定 wikilink 依赖；发布前用 `kdo verify-deps` 检测上游变更 |
| EC 环境锁定 🆕 | 每个 Agent 启动时/批量任务前应 `kdo env-check`；环境变更后 `kdo env-check --lock` 更新锁文件 |
| Skill 迭代标准 | `30_wiki/decisions/plan_20260621_skill-iteration-standard.md` — 卡片→Skill 的触发条件、质量标准、审核流程。各域生产者 Wave 末尾评估 |
| **工具登记四步法** | 新增工具/脚本必须：①放入 `40_outputs/code/scripts/` ②登记到 README.md ③复杂逻辑写 skill ④ skill 之间互引。不登记=不存在 |
| 精修分级 | 格式精修(30张/批) vs 内容精修(5张/批) — 验收时区分 |

## 新增管道

| 管道 | 说明 |
|:--|:--|
| `kdo ingest --batch <subdir> --auto-scaffold` | 批量素材→卡片骨架 |
| `kdo graph bridge <dom_a> <dom_b>` | 跨域桥接检测 |
| `kdo query --view needs-review` | 预设视图过滤 |
| `kdo freeze` / `kdo verify-deps` | 对卡片 wikilink 依赖做 SHA256 锁定与变更检测 | 对应 EC 手册「依赖冻结」|
| `kdo env-check --lock` / `kdo env-check` | 锁定并校验 Python/kdo/git 工具链版本 | 对应 EC 手册「环境锁定」|
| `kdo snapshot` / `kdo revert` / `kdo batch` | 批量操作前打 tag 建回退点，失败回退 | 对应 EC 手册「回退预案」|

## 全Agent行为宪法 v1.0（#652，2026-09-06 上线）

> 老朱 09-06 拍板：实事求是=准则，调研=基本技能挂载，全 agent 强制（含飞书 hermes 端）。
> 五条：断言三级标注【实证/推断/猜测】/ 负向判词必附存在性核查锚点 / 疑问先检索再开口（W11）/ 解放-检验循环 / Y模型三问后才方案。
> 全文：`90_control/agent-behavior-constitution.md`（v1.0，欧阳锋终审后生效；增条款走修订单）。
> 挂载点：`.agent/startup.md`（全角色开机必读）+ `90_control/scripts/kimi-headless-launch.py` PROMPT_TEMPLATE（无头实例）+ hermes 6 profile SOUL.md（飞书端）。
> 调研技能实装面：business-research skill 唯一已实装（商业主体类）；deep-research 仅原始素材未封装、research-core 仅矩阵登记无文件——技术/概念类用 kdo query+grep，不虚指。
