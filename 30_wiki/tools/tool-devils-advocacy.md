---
id: tool-devils-advocacy
title: Devil's Advocacy：主动攻击自己的结论
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
- web: CIA Tradecraft Primer - Devil's Advocacy
related:
- "[[framework-structured-analytic-techniques]]"
- "[[concept-半肥猫-ai-research-validation]]"
- "[[tool-harness-adversarial-tester]]"
---

# Devil's Advocacy

> 与"交叉验证"的区别：交叉验证=多源核实事实是否正确；魔鬼代言人=即使事实正确，你的逻辑推理有没有漏洞？

## 四步法

### Step 1：选定要挑战的结论

必须是具体的、可被证伪的判断。"这个赛道可以做"太模糊——"我们的单元模型在月销300单时可以盈利"才是可挑战的结论。

### Step 2：指定挑战者（Agent天然适配）

告诉Agent："你现在是这个结论的激烈反对者。你的目标是找到它最脆弱的点并全力攻击。"

### Step 3：要求挑战者提出最强反驳

不只是"这个可能有风险"——是"这个结论在X情况下会完全崩溃，因为Y"。

### Step 4：评估反驳后修正结论或记录风险

反驳成立→修正原结论。反驳不成立→记录为什么反驳无效，但保留作为风险评估的输入。

## 模板

```
我们最大的风险是______，因为______。
如果______发生，我们的______假设将不再成立。
最早能在______（时间）通过______（信号）发现这个风险。
```

## Agent执行指令

```python
# Devil's Advocate Prompt模板
prompt = """你现在是[CONCLUSION]的激烈反对者。你的目标是使用最强逻辑和证据攻击它。

攻击方向：
1. 支撑这个结论的关键假设有什么漏洞？
2. 有哪些反例没有被考虑？
3. 如果结论是错的，最可能的错误原因是什么？
4. 什么情况下这个结论会完全崩溃？

要求：每个攻击点必须有具体推理，不能用"可能有风险"这种模糊表述。
"""
```

## 失败模式

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| 挑战者不够狠 | 给出的反驳都是"可以解决的" | 给Agent更激进的角色设定 |
| 把反驳当人身攻击 | 挑战完后团队氛围变差 | 明确这是结构化技术，攻击的是逻辑不是人 |
| 挑战后不修正 | 反驳有效但结论不改 | Devil's Advocacy的最后一步必须是"修正或记录" |

## 适用边界

- **适用**：高风险决策、团队已形成共识需要打破群体思维
- **不适用**：已进入执行阶段的小调整（不要用大炮打蚊子）
- **Agent优势**：Agent扮演挑战者没有"得罪人"的心理负担

---

*卡片类型：tool | 审核状态：待审*
