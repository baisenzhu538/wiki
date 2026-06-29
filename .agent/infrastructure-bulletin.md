# KDO 基建变更公告

> 更新：2026-06-29  
> 面向：所有 Agent  
> **每个 Agent 启动时必须读此文件了解最新基建变更。**

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
