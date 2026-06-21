---
id: tool-demand-iceberg-l2-scenario
title: L2粗拆场景问题：捕捉表层的痛点和需求
type: tool
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.88
trust_level: high
language: zh-CN
domain: [yitang, five-step-method]
source_refs:
- 00_inbox/五步法之需求分析/AI场景推演教练提示词.txt
related:
- "[[framework-demand-iceberg]]"
- "[[tool-demand-iceberg-l1-user]]"
- "[[tool-demand-iceberg-l3-core-job]]"
---

# L2粗拆场景问题

> L1确定了"谁"，L2回答"在什么情况下遇到什么问题"。场景是连接用户和需求的桥梁。

## 核心三问

| 问题 | 示例 |
|:---|:---|
| **在什么场景下？** | 出差、加班、带娃、通勤、周末宅家 |
| **遇到了什么问题？** | 时间不够、信息过载、选择困难、信任缺失 |
| **现在怎么解决的？** | 用竞品、问朋友、忍了、用土办法——暴露替代方案 |

## Agent执行指令

```python
# 引自 AI场景推演教练 Step 1（续）
prompt = """基于已确认的目标用户群（{USER_SEGMENT}），
列出该用户群最常遇到的3-5个场景和对应痛点：
1. 场景描述（什么时候/在哪）
2. 痛点（具体什么困难）
3. 现有解决方案（他们现在怎么做）
"""
```

## 失败模式

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| 场景太泛 | "用户想买东西"——太泛 | 缩小到具体的购买情境 |
| 只列场景不列痛点 | "用户在通勤"——然后呢？ | 每个场景必须跟一个具体痛点 |

## 适用边界

- **适用**：L1确认后的自然下一步
- **不适用**：跳过L1直接用L2（不知道是谁的场景=没有意义）

---

*卡片类型：tool | 审核状态：待审*
