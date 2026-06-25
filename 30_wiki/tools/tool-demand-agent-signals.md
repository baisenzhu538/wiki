---

id: tool-demand-agent-signals
title: Agent L1-L2信号聚合：替代"凭经验猜用户"
type: tool
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.88
trust_level: high
language: zh-CN
domain: [yitang, five-step-method, ai-collaboration]
source_refs:
- web: thrv 2025 segmentation methods
- web: Reddit/Glassdoor public data analysis
related:
  - '[[tool-yitang-18-strategy-tool-mapping]]'
  - '[[tool-demand-agent-case-match]]'
  - '[[tool-alt-data-overview]]'
  - '[[tool-demand-agent-auto-verify]]'
  - '[[tool-demand-agent-signal-substitute]]'
- "[[tool-demand-iceberg-l1-user]]"
- "[[tool-demand-iceberg-l2-scenario]]"
- "[[tool-demand-blindspot-checklist]]"
---

# Agent L1-L2信号聚合

> L1+L2的传统做法是"凭经验猜用户画像和场景"。Agent可以替代这一步——自动聚合Reddit/评论/搜索趋势/竞品数据，用信号代替直觉。

## 方法

**Agent自动采集信号源**：
- Reddit/知乎：该品类被提及的高频场景和用户抱怨
- App Store/电商评论：竞品的差评集中在什么场景
- Google Trends：品类搜索趋势和地域分布
- 竞对招聘JD：竞对在招什么岗位→他们在押注什么用户群

## 与对应冰山卡的关系

- L1（用户标签）：Agent用"多角色映射"替代"我猜用户是谁"
- L2（场景问题）：Agent用"Job Story格式"自动生成场景假设

## Agent执行指令

**具体工具引用**：`research-web-scraping`（Firecrawl抓取竞品评论）、`research-osint`（Wayback Machine查历史版本）

```python
# Agent自动聚合用户信号
signals = agent.search_across([
    "reddit.com/r/{CATEGORY} top posts last 6 months",
    "app store reviews for {COMPETITOR_APP} 1-2 star",
    "google trends {CATEGORY} past 12 months",
    "linkedin jobs at {COMPETITOR} new in last 30 days"
])
# 输出：用户高频场景+痛点+情绪强度排序
```

## 失败模式

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| 信号当结论 | Reddit上3个人抱怨就当作普遍需求 | 交叉验证：至少2个平台出现同一模式 |
| 忽略沉默用户 | 只看到发声的人，忽略沉默的大多数 | 信号分析后必须做定量验证 |

## 适用边界

- **适用**：L1/L2的初步用户画像和场景假设生成
- **不适用**：最终决策——Agent提供信号，人做判断

---

*卡片类型：tool | 审核状态：待审*
