# Phase 2.3 并行 Agent Prompts

> 黄药师用。每个 prompt 可直接复制给一个 Agent。4 个 Agent 可同时启动，互不冲突。

---

## 共享骨架模板（每个 Agent 都用这个）

```yaml
---
title: "课程中文名"
type: concept
status: draft
domain: ['yitang']
yitang:
  map: <personal|management|entrepreneur>
  module: "模块名"
  course_id: "<编号或⚠️待补>"
  course_type: method
  level: <foundational|core|advanced>
  series: false
source_refs: []
created_at: "2026-05-06"
updated_at: "2026-05-06"
tags:
  - "#yitang"
---
```

正文模板：

```markdown
# 课程中文名

> 来源：TODO。[[一堂方法论体系总图]] | [[yitang-course-map]]

## Summary

TODO

## [Condense]

TODO

## [Critique]

TODO

## [Synthesis]

TODO
```

**规则：**
- 文件名：`30_wiki/concepts/yt-{map}-{slug}.md`（slug 用英文连字符，见下表）
- course_id 已确认的填数字，未确认的填 `"⚠️待补"`
- 系列课 `series: true`（每张地图最后标注了哪些是系列课）
- 执行前确认 `30_wiki/concepts/` 目录存在

---

## Agent A：个人修炼地图（12 门）

**任务**：为以下 12 门课创建骨架文件，命名 `yt-personal-{slug}.md`。

| course_id | 课程名 | slug | level | 系列课 |
|:--:|------|------|------|:--:|
| 401 | 时间管理 | time-management | foundational | |
| 402 | IPO 科学学习 | ipo-learning | foundational | ✅ |
| 404 | 深度复盘 | deep-review | core | |
| 405 | 知识管理 | knowledge-management | core | |
| 406 | 科学成长（刻意练习） | deliberate-practice | foundational | |
| 407 | 清单体笔记 | checklist-notes | core | |
| 408 | 逐字稿 | verbatim-script | core | |
| 409 | 十指销讲模型 | sales-pitch-model | core | |
| 410 | 科学表达（火箭模型） | scientific-expression | core | ✅ |
| 518 | 灵感闪现（认知篇） | inspiration-flash | advanced | ✅ |
| ⚠️ | 泛产品设计 | product-design | core | ✅ |
| ⚠️ | AI 能力（双模型） | ai-capability | advanced | |

**frontmatter 注意事项：**
- `map: personal`
- `yitang.module` 填课程名（含括号内容，如"科学成长（刻意练习）"）
- course_id 已确认的填纯数字字符串：`"401"`, `"402"` 等
- ⚠️ 标记的 `course_id: "⚠️待补"`
- `level` 按上表

---

## Agent B：管理修炼地图（16 门）

**任务**：为以下 16 门课创建骨架文件，命名 `yt-management-{slug}.md`。

| course_id | 课程名 | slug | level | 系列课 |
|:--:|------|------|------|:--:|
| 421 | 项目管理 | project-management | core | ✅ |
| ⚠️ | 基本功认知 | basic-skills | foundational | ✅ |
| ⚠️ | 科学招聘 | scientific-hiring | core | |
| ⚠️ | 新人落地 | onboarding | core | |
| ⚠️ | 科学开会 | scientific-meetings | core | ✅ |
| ⚠️ | 团队知识管理 | team-knowledge | core | |
| ⚠️ | 管理段位 | leadership-levels | core | |
| ⚠️ | 目标管理 | goal-management | core | |
| ⚠️ | 业务公式 | business-formula | core | ✅ |
| ⚠️ | Y模型/科学决策 | scientific-decision | core | ✅ |
| ⚠️ | 转化率黑客 | conversion-hacking | core | ✅ |
| 452 | 战略会 | strategy-meeting | advanced | |
| ⚠️ | 公司文化 | company-culture | advanced | |
| ⚠️ | 合伙股权 | partnership-equity | advanced | ✅ |
| 459 | 财务入门 | finance-basics | advanced | |
| ⚠️ | 一号位 | founder-role | advanced | |

**frontmatter 注意事项：**
- `map: management`
- `yitang.module` 填课程名
- course_id 已确认的填纯数字字符串：`"421"`, `"452"`, `"459"`
- ⚠️ 标记的 `course_id: "⚠️待补"`
- `level` 按上表

---

## Agent C：创业修炼地图（23 门）

**任务**：为以下 23 门课创建骨架文件，命名 `yt-entrepreneur-{slug}.md`。

| course_id | 课程名 | slug | level | 系列课 |
|:--:|------|------|------|:--:|
| **预判** | | | | |
| ⚠️ | 机会选择 | opportunity-selection | core | |
| ⚠️ | 行业预判 | industry-forecast | core | |
| ⚠️ | 集中度分析 | concentration-analysis | core | |
| **起盘** | | | | |
| 259 | 259里程碑 | 259-milestone | foundational | |
| ⚠️ | 关键假设 | key-hypotheses | foundational | |
| ⚠️ | 一堂五步法 | five-step-method | foundational | ✅ |
| ⚠️ | 需求分析 | needs-analysis | foundational | |
| ⚠️ | 产品内核 | product-core | core | ✅ |
| ⚠️ | 单元模型 | unit-model | core | ✅ |
| ⚠️ | 调研认知 | research-cognition | core | ✅ |
| ⚠️ | 低成本验证/MVP | lean-validation | core | ✅ |
| **增长** | | | | |
| ⚠️ | 业务增长 | business-growth | core | |
| ⚠️ | 渠道探索 | channel-exploration | core | |
| ⚠️ | 工业化生产 | industrial-production | advanced | |
| 489 | 增长飞轮 | growth-flywheel | advanced | |
| ⚠️ | 融资认知 | fundraising | advanced | ✅ |
| ⚠️ | 项目壁垒 | barriers | advanced | |
| **底层逻辑（= 无限修炼）** | | | | |
| ⚠️ | 实事求是 | truth-seeking | foundational | |
| ⚠️ | 解放思想 | liberate-thinking | foundational | |
| ⚠️ | Y模型/科学方法 | scientific-method | foundational | |
| ⚠️ | 务实创业 | pragmatic-startup | advanced | |

**frontmatter 注意事项：**
- `map: entrepreneur`
- `yitang.module` 填课程名
- course_id 已确认的填纯数字字符串：`"259"`, `"489"`
- ⚠️ 标记的 `course_id: "⚠️待补"`
- `level` 按上表

---

## Agent D：无限修炼地图（0 门独立文件）

无限修炼地图的 3 门必修课（实事求是/解放思想/Y模型科学方法）已作为创业地图「底层逻辑」阶段的课程，由 Agent C 创建。无需重复建文件。

Agent D 任务：检查 Agent A/B/C 的产出：
- 文件名是否符合 `yt-{map}-{slug}.md` 格式
- frontmatter 是否包含 `yitang:` 嵌套对象
- 正文是否为 TODO 模板（不应填入实际内容）

---

## 启动指令

黄药师，复制以下 3 条消息发送即可（每条启动一个 Agent）：

**启动 Agent A：**
> 在 `30_wiki/concepts/` 下创建 12 个个人修炼地图课程骨架文件。具体课程清单、命名规范、模板看 `90_control/workflows/phase-2.3-agent-prompts.md` 中的「Agent A」章节。创建完成后报告文件名清单。

**启动 Agent B：**
> 在 `30_wiki/concepts/` 下创建 16 个管理修炼地图课程骨架文件。具体课程清单、命名规范、模板看 `90_control/workflows/phase-2.3-agent-prompts.md` 中的「Agent B」章节。创建完成后报告文件名清单。

**启动 Agent C：**
> 在 `30_wiki/concepts/` 下创建 23 个创业修炼地图课程骨架文件。具体课程清单、命名规范、模板看 `90_control/workflows/phase-2.3-agent-prompts.md` 中的「Agent C」章节。创建完成后报告文件名清单。

三个 Agent 可以同时启动，互不冲突（操作不同文件）。
