id: tool-yitang-18-strategy-tool-mapping
title: 降龙十八掌→工具映射表：每掌对应的执行工具和 Skill
type: tool
status: reviewed
confidence: 0.9
trust_level: high
domain:
- yitang
- research
source_refs:
- 30_wiki/frameworks/framework-yitang-18-strategy-cards.md
- 30_wiki/concepts/yt-research-osl-framework.md
- 30_wiki/domains/yitang-research-domain-digest.md
- 00_inbox/调研专题/一堂-系统式调研-口述.txt
quality_labels:
- actionable
- cited
- validated
created_at: '2026-06-21'
updated_at: '2026-06-29'
author: 黄药师
reviewed_by: 欧阳锋
related:
- '[[tool-半肥猫-课程Skill化的八步工作流]]'
- '[[tool-ai-skill-engineering-method]]'
- '[[tool-Truman-Skill全生命周期管理]]'
- '[[paddleocr-skill]]'
- '[[case-半肥猫-course-to-skill]]'
- '[[tool-封装可复用skill]]'
- '[[course-to-skill-conversion]]'
- '[[truman-perspective-skill]]'
- '[[tool-ban-fei-mao-yong-skill-zuo-dui-bi-ce-shi-yan-zheng-xiao-guo]]'
- '[[case-ji-hao-skill-market-problem-validation]]'
- '[[case-truman-ai-skill-self-packaging]]'
- '[[yt-skill-checklist-as-ai-protocol]]'
- '[[yt-skill-p-role-prompt-design]]'
- '[[tool-ban-fei-mao-pan-duan-ke-cheng-shi-fou-zhi-de-zuo-cheng-skill]]'
- '[[plan_20260621_skill-iteration-standard]]'
- '[[tool-yitang-research-competitive-quadrant]]'
- '[[tool-yitang-research-follow-map]]'
- framework-yitang-18-strategy-cards
diagnostic_signals:
- framework_lens: 策略→工具映射表
  follow_up_question: 在映射表中找到对应的 wiki 卡片或 Skill
# 降龙十八掌→工具映射表

> 十八掌是"做什么"，这张卡是"用什么做"。每掌给出对应的 wiki 卡片 + Claude Code Skill + 应急方案。

## 映射总表

| # | 策略名 | 核心动作 | wiki 卡片 | Skill | 应急方案 |
|:--|:--|:--|:--|:--|:--|
| 1 | **调研先行验证假设** | 行动前先搜有没有人已经验证过 | `yt-research-hypothesis-test` | `/research` | WebSearch 快速扫一遍 |
| 2 | **最佳实践** | 找行业标杆怎么做 | `tool-yitang-research-best-practice` | `/research-industry-report` | 搜"XX行业 best practice" |
| 3 | **竞对跟踪** | 持续监控竞争对手动态 | `tool-yitang-research-competitor-tracking` | `/research-web-scraping` | Google Alert + Wayback Machine |
| 4 | **行业扫描** | 快速建立行业全貌 | `tool-yitang-research-industry-scan` | `/research-industry-report` | 3 份券商报告速读 |
| 5 | **公司拆解** | 深度拆解目标公司 | `tool-yitang-research-company-disassembly` | `/research-financial-report` | 招股书+年报+G2评论 |
| 6 | **单元模型** | 拆最小经济单元 | `tool-yitang-research-unit-model` | — | 找单店/单客数据反推 |
| 7 | **单点狙击** | 聚焦一个关键问题深挖 | `tool-yitang-research-single-point-sniper` | `/research-cross-validation` | 九层深挖法 |
| 8 | **竞争象限** | 二维矩阵可视化竞争格局 | `tool-yitang-research-competitive-quadrant` | — | Excel 散点图 |
| 9 | **二维定位** | 找差异化坐标 | `tool-yitang-research-two-dimensional-positioning` | — | 对标公司对比表 |
| 10 | **按图索骥** | 根据定位找对标案例 | `tool-yitang-research-follow-map` | `/research-industry-report` | 搜"XX模式+案例" |
| 11 | **地图在手** | 建立全局信息获取体系 | `tool-yitang-research-intelligence-map-in-hand` | `/research` | 域索引入口卡"工具索引" |
| 12 | **穷尽手段** | 不放弃任何信息渠道 | `tool-yitang-research-exhaust-means` | `/research-web-scraping` + `/research-osint` | OSINT Framework 导航 |
| 13 | **事实优先** | 区分事实与观点 | `concept-yitang-research-facts-first` | — | 每句话标注"事实/观点/推测" |
| 14 | **定量建模** | 用数字说话 | `tool-yitang-research-quantitative-modeling` | — | Excel 敏感性分析 |
| 15 | **交叉验证** | 多源印证每个关键结论 | `tool-yitang-research-cross-validation` | `/research-cross-validation` | ≥2独立来源+标注置信度 |
| 16 | **深度归因** | 5Why找到根因 | `tool-yitang-research-deep-attribution` | — | 5Why + 追问"还有吗" |
| 17 | **归一总结** | 整合信息形成统一结论 | `tool-yitang-research-normalize-summary` | — | OSCAR Step 5 模板 |
| 18 | **持续跟踪** | 建立动态监控机制 | `tool-yitang-research-continuous-tracking` | — | Google Alert + RSS + crawler cron |

## 按 OSCAR 阶段分组

| OSCAR 阶段 | 对应的掌 | 核心工具 |
|:--|:--|:--|
| **O**bjective 定目标 | 第 1 掌 | 假设验证 |
| **S**cope 缩范围 | 第 8, 9, 10 掌 | 竞争象限/二维定位/按图索骥 |
| **C**hecklist 列清单 | 第 11 掌 | 地图在手 |
| **A**cquire 取情报 | 第 2, 3, 4, 5, 6, 7, 12 掌 | 最佳实践/竞对/行业/公司/单元模型/单点/穷尽 |
| **R**eason 归因 | 第 13, 14, 15, 16, 17 掌 | 事实优先/定量/交叉验证/归因/归一 |
| **+ 持续** | 第 18 掌 | 持续跟踪 |

## 未覆盖的掌

以下掌当前无独立 wiki 卡片，需老顽童在 Wave 3 补产：

| # | 策略 | 状态 | 建议 ID |
|:--|:--|:--|:--|
| 14 | 定量建模 | ❌ 无独立 tool 卡 | `tool-yitang-research-quantitative-modeling`（已列入 Wave 3）|
| 16 | 深度归因 | ❌ 无独立 tool 卡 | `tool-yitang-research-deep-attribution`（已列入 Wave 3）|

> 注：第 14 和第 15 掌在口述稿中可能重复（都是"定量建模"），需老顽童回查口述确认第 15 掌实际内容。

## Agent 使用方式

```
Agent 知道要用第 X 掌 → 查本卡映射表 → 找到对应 Skill 或 wiki 卡片 → 执行
```

例如：用户说"帮我做个行业扫描" → Agent 查本卡 → 第 4 掌 → `/research-industry-report` → 执行 Doris 四步法。

---

*黄药师 · 2026-06-21 · 调研域架构层整合*

## 目的

解决"知道该用哪一掌策略，但不知道具体用什么工具/Skill 去执行"的断裂问题。这张映射表把降龙十八掌的策略名翻译成可直接调用的 wiki 卡片和 Claude Code Skill，让 Agent 和人都能一步到位找到执行工具。适用于已经用 OSCAR 框架确定调研方向后、进入执行阶段的场景，也适用于 Agent 自动化调研时按策略查表调工具。

## 操作步骤

1. **确定当前策略**：在 OSCAR 流程中定位到当前属于哪一掌（如"行业扫描"=第4掌），确认你要解决的问题类型
2. **查映射表**：在本卡映射总表中找到对应行，查看推荐的 wiki 卡片和 Skill。如果该掌有独立卡片，点进去看详细方法论；如果有 Skill，直接用 `/skill-name` 调用
3. **执行+回填**：按卡片或 Skill 的方法论执行调研，完成后回到映射表确认是否有遗漏的配套工具。如果发现某掌缺独立 wiki 卡片（如第14掌定量建模），标记为 Wave 3 待补产

## 不要用的场景

- **策略本身不明确时**：如果你连"要解决什么问题"都没想清楚，查映射表只会增加混乱。先回到 OSCAR 的 Objective 阶段明确目标
- **组合策略场景**：实际调研往往需要多掌配合（如"行业扫描"+"交叉验证"+"深度归因"），单掌查表可能导致只做了一步就停
- **新手第一次调研**：映射表是索引层，不是教学层。新手应先读口述稿和框架卡理解每掌的含义，再用映射表提速

## 质疑

**核心局限**：映射表是静态索引，依赖人工维护更新。当新的 Skill 被创建或旧 Skill 被废弃时，映射表如果没有同步更新，就会产生指向失效的"死链接"。

**Roger Martin**（战略学派）会指出："把策略简化为'查表找工具'的危险在于，策略的本质是整合判断（abductive reasoning），不是按图索骥的线性流程。映射表让人误以为调研是流水线，实际上每一步都需要策略性直觉。"

**Herbert Simon**（有限理性理论）会批评："映射表假设人能完整列举所有策略-工具对应关系，但现实中决策者的注意力是稀缺的。18 掌看起来全面，但使用者在压力下往往只会用自己最熟的 3-4 掌，映射表的存在并不能改变这个认知偏差。"

**关键术语**：策略-工具映射、OSCAR 框架、Agent 调用链
**适用边界**：仅适用于已掌握基础调研方法论、需要提速执行的场景
**反例**：用户第一次做竞对调研，直接查映射表找到"竞对跟踪"→点进 tool 卡，但因为没有先验知识，完全不理解卡片内容在说什么
