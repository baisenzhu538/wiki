---

id: tool-demand-agent-auto-verify
title: Agent L6自动预验证：RAT的竞品数据+趋势快速验证
type: tool
status: reviewed
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
aliases:
  - AgentL6自动预验证：RAT的竞品数据+趋势快速验证
  - L6自动预验证
  - RAT的竞品数据+趋势快速验证
  - 的竞品数据
  - 自动预验证
  - 趋势快速验证
source_refs: null
discoverable_by:
  - Agent L6自动预验证：RAT的竞品数据+趋势快速验证
  - L6自动预验证
  - RAT的竞品数据+趋势快速验证
related:
- '[[yitang-domain-digest]]'
- '[[ai-collaboration-domain-digest]]'
- kdo-protocol-implementation-roadmap
updated_at: '2026-06-29'
tags:
- audience:executor
- scene:execution
- skill-level:advanced
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

## 目的

> 待补充：这个工具解决什么问题？适用于什么场景？

## 操作步骤

1. **步骤一**：待补充
2. **步骤二**：待补充
3. **步骤三**：待补充

## 不要用的场景

> 待补充：什么情况下这个工具效果有限或不应该使用？

## 质疑

- **具体假设**：该工具假设"Agent 搜索到的竞品数据和评论趋势能预判 RAT 的真伪"，但 Agent 的搜索结果存在"幸存者偏差"——只能找到已经公开的信息，而失败的产品不会留下评论。RAT 被"预验证为可能错误"的案例，恰恰可能是真正有价值的新方向。
- **边界**：在全新品类（无竞品、无评论数据）中，Agent 搜索不到任何信号——预验证完全失效。
- **前提**：该工具的前提是"Agent 的情感分析准确度足够高"，但 LLM 对用户评论的情感判断在反讽、混合情绪等场景下错误率超过 30%。

**Stuart Russell**（UC 伯克利计算机科学教授，《Human Compatible》作者）会质疑：预验证的核心问题是"错杀"——Agent 为了避免人类浪费时间验证"可能错误的 RAT"，会用过于保守的阈值过滤掉"看似不合理但有突破性"的假设。真正的创新恰恰来自"所有人都不看好"的方向。Agent 的预验证可能变成"创新过滤器"——把最激进的想法提前杀掉，只留下"安全的平庸想法"。
