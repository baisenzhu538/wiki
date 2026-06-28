---

id: tool-demand-agent-auto-verify
title: Agent L6自动预验证：RAT的竞品数据+趋势快速验证
type: tool
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.88
trust_level: high
language: zh-CN
domain:
- yitang
- five-step-method
- ai-collaboration
source_refs:
- src_unknown
related:
  - [[yitang-domain-digest]]
  - [[ai-collaboration-domain-digest]]
  - [[pending_unknown]]
  - [[pending_unknown]]
  - [[pending_unknown]]
updated_at: '2026-06-29'
---

# Agent L6自动预验证

> L6产出的RAT（最危险假设）在投入真实验证之前，Agent可以先做一轮"预验证"——自动搜索竞品数据/评论趋势，快速判断哪些RAT可能已经错了。

## 方法

1. 对每个RAT，Agent自动搜索：竞对有没有类似产品？用户对此类产品的反馈？
2. 快速判断：RAT是"合理假设"还是"已被市场证伪"？
3. 过滤掉已被证伪的RAT，聚焦剩余的做真实用户验证

## Agent执行指令

**具体工具引用**：`research-cross-validation`（双重验证RAT）、`research-osint`（Wayback Machine查竞对历史产品变化）

```python
for rat in rats:
    evidence = agent.search(f"has anyone tried {rat['hypothesis']}?")
    sentiment = agent.analyze_sentiment(evidence)
    if sentiment == "negative" and confidence > 0.8:
        rat["status"] = "likely_falsified"
    else:
        rat["status"] = "needs_validation"
```

## 失败模式

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| 预验证代替真实验证 | Agent说"没找到证据"就认为RAT不成立 | 预验证只是快速过滤，不能替代真实用户验证 |
| 搜索不全面 | Agent只搜了英文结果 | 多语言搜索+多平台交叉 |

## 适用边界

- src_unknown
- src_unknown

---

*卡片类型：tool | 审核状态：待审*
