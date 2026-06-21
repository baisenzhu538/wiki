---
id: tool-key-assumptions-check
title: Key Assumptions Check：审计你信以为真的东西
type: tool
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.90
trust_level: high
language: zh-CN
domain: [yitang, research]
source_refs:
- web: CIA Tradecraft Primer - Key Assumptions Check
related:
- "[[framework-structured-analytic-techniques]]"
- "[[tool-yitang-research-validate-assumption]]"
- "[[framework-yitang-nine-layer-deep-dig]]"
---

# Key Assumptions Check

> 与第1掌（调研先行验证假设）的升级关系：第1掌强调"做事前先验证假设"，KAC提供一个结构化的四步法来系统执行。

## 四步法

### Step 1：列出所有支撑当前判断的假设

不只是"明显的假设"，也包括"太明显以至于你没意识到的假设"。

**案例**：一堂进入Skill市场
- 企业客户愿意为内部工具买Skill ✓
- 企业有预算给"工具"类产品 ✓
- 决策者是技术负责人而非HR ✓
- Skill市场不会在12个月内被平台方免费化 ✓
- 竞对不会快速复制 ✗（潜意识假设）

### Step 2：评估每条假设的证据强度

| 证据等级 | 含义 |
|:---|:---|
| 🔴 无证据 | 完全凭直觉或信念 |
| 🟡 弱证据 | 有1-2个轶事或类比，但没有系统数据 |
| 🟢 强证据 | 有多个独立数据源交叉验证 |

### Step 3：标记"无证据支撑"的假设

这些是你最大的风险敞口——你基于它们做了重大决策，但它们可能完全不成立。

### Step 4：为弱假设设计验证方案

对每个🟡或🔴假设，设计最小成本验证路径。

## Agent执行指令

```python
# KAC Prompt模板
prompt = """基于以下商业计划，执行Key Assumptions Check：

[PLAN TEXT]

请完成：
1. 列出该计划隐含的10-15条假设（包括"太明显以至于没写出来"的）
2. 将每条假设标记证据强度（RED/YELLOW/GREEN）
3. 对RED和YELLOW假设，设计最小验证路径
4. 特别指出：如果哪条RED假设不成立，整个计划会崩塌
"""
```

## 失败模式

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| 遗漏"太明显"的假设 | 检查完没发现任何RED假设 | 强制问"这个计划成立需要什么外部条件" |
| 把信念当事实 | "这个显然成立"被标为GREEN | 追问"如果你要跟一个怀疑论者证明这一点，你需要什么证据" |

## 适用边界

- **适用**：重大决策前的最后检查、商业计划评审
- **不适用**：低风险决策（KAC本身的时间成本可能超过决策价值）

---

*卡片类型：tool | 审核状态：待审*
