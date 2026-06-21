---
id: tool-strategy-value-proposition
title: 价值主张：马斯洛金字塔交叉定位+排序方法
type: tool
status: enriched
confidence: 0.90
trust_level: high
domain:
  - strategy
source_refs:
  - 00_inbox/战略专题/冉鹏PPT截图/引擎点火20260110 战略破局（冉鹏）(1)_108_vlm_desc.md
created_at: "2026-06-21"
updated_at: "2026-06-21"
author: 老顽童（初版）→ 黄药师v2标准补强
reviewed_by: 欧阳锋
related:
  - "[[framework-strategy-business-design]]"
  - "[[tool-strategy-customer-selection]]"
  - "[[framework-demand-usp-model]]"
---

# 价值主张：马斯洛金字塔交叉定位

> 业务设计六要素第2要素。核心问题：**我们提供什么独特价值？为什么客户选我们不选别人？**

## 操作步骤

### Step 1：马斯洛需求层定位
你的产品落在马斯洛金字塔的哪一层？
- 生理（生存必需）→ 安全（保护/保障）→ 归属（关系/社群）→ 尊重（地位/认可）→ 自我实现（成长/意义）

### Step 2：消费者敏感维度交叉
在该需求层，客户最敏感的核心维度是什么？
- 价格敏感？品质敏感？便利敏感？情感敏感？社交敏感？

### Step 3：差异化价值声明
`我们的产品在[需求层]通过[敏感维度]为[客户群]提供[独特价值]`

### Step 4：价值主张排序
列出3-5条可能的差异化价值，按"客户在乎程度×我们能做到的程度"排序取Top 1

## Agent 执行指令

```python
def value_proposition_analysis(target_customer: str):
    steps = {
        "需求层定位": f"「{target_customer}」的核心需求落在马斯洛金字塔的哪一层？生理/安全/归属/尊重/自我实现？为什么？",
        "敏感维度": "该客户群在购买同类产品时，最敏感的是哪个维度？价格/品质/便利/情感/社交？给出理由。",
        "差异化声明": "用一句话公式表达：我们的产品在[X层]通过[Y维度]为[客户]提供[Z价值]",
        "价值排序": "列出3-5条差异化价值，按'客户在乎程度1-5'和'我们能做到程度1-5'两个轴打分排序"
    }
    return {step: ask(prompt) for step, prompt in steps.items()}
```

## 失败模式

| 失败 | 症状 | 修复 |
|:--|:--|:--|
| 价值太泛 | "我们的价值是高品质"——所有人都这么说 | 定位到具体需求层——高品质=安全层的可靠还是尊重层的档次？ |
| 需求层错位 | 把"安全需求"的产品定位在"自我实现" | 问客户最后一次购买时最首要的考量是什么 |
| 价值排序靠直觉 | 觉得A重要就选A | 强制两条轴打分——客户在乎度×我们的优势度 |

---

*老顽童初版 · v2补强 · 2026-06-21*
