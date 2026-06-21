---
id: framework-ci-operating-model
title: CI运营模型：从信息收集到决策改变的闭环
type: framework
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.85
trust_level: high
language: zh-CN
domain: [yitang, research]
source_refs:
- web: Competitive Intelligence Alliance CI Operating Model
- web: BestBootcamps CI Framework Guide 2026
related:
- "[[framework-yitang-research-weapon-system]]"
- "[[tool-ci-define-phase]]"
- "[[tool-ci-implement-phase]]"
---

# CI运营模型：从信息收集到决策改变的闭环

> "If the output does not change a decision, you did not do CI. You gathered trivia." — CI行业铁律。一堂武器库解决了"怎么收集"，CI模型补充了"收集之后怎么办"。

## 四阶段循环

```
Define（定义问题）
  → Gather（收集情报）  ← 一堂武器库覆盖
    → Analyze（分析洞察）
      → Implement（嵌入决策）
        → 回到 Define
```

## 与一堂武器库的映射

| CI阶段 | 一堂覆盖度 | 缺口 |
|:---|:---:|:---|
| **Define** | ✗ 未覆盖 | 不会从决策倒推信息需求 |
| **Gather** | ✓ 全量覆盖 | 三层八模块+OSINT补充 |
| **Analyze** | △ 部分覆盖 | 有交叉验证，缺结构化分析框架 |
| **Implement** | ✗ 未覆盖 | 报告产出了，但没人用 |

## 每阶段的决策问题

| 阶段 | 关键问题 | 输出物 |
|:---|:---|:---|
| Define | 什么决策需要我们收集情报？ | KITs + KIQs 清单 |
| Gather | 用到哪些来源和工具？ | 原始数据 + 初步整理 |
| Analyze | 数据讲什么故事？对决策意味着什么？ | 洞察 + 建议 |
| Implement | 谁需要知道？怎么让他们行动？ | Battlecard / 简报 / 预警 |

## Agent执行指令

```python
# CI运营模板（Agent可据此设计CI流程）
ci_cycle = {
    "define": {
        "trigger": "关键决策窗口期到来",
        "output": "KITs + KIQs 文档",
        "owner": "Decision maker + CI analyst"
    },
    "gather": {
        "trigger": "KIQs 确认",
        "output": "原始信息库",
        "tools": ["OSINT", "Firecrawl", "Google Dorking", "招聘API"]
    },
    "analyze": {
        "trigger": "Gather完成",
        "output": "洞察报告",
        "tools": ["ACH", "Devil's Advocacy", "Key Assumptions Check"]
    },
    "implement": {
        "trigger": "洞察确认",
        "output": "Battlecard / 决策备忘录",
        "channels": ["QBR", "deal review", "Slack digest"]
    }
}
```

## 失败模式

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| 跳过Define | 收集了一堆信息但不知道用来干什么 | 先写KIQ再动手收集 |
| Gather过量 | 信息收集永远停不下来 | 设定时间盒：Gather不超过总时间的40% |
| Analyze肤浅 | 洞察=数据摘要 | 用SATs框架做结构化分析 |
| Implement缺失 | 报告发出去没人看 | 嵌入运营节奏，不是"一次性的报告" |

## 适用边界

- **适用**：竞对情报需要持续运营的B2B/SaaS公司、有专门CI人员或Agent的团队
- **不适用**：一次性调研任务（不需要运营模型）

---

*卡片类型：framework | 审核状态：待审*
