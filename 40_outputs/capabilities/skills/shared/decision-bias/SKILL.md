---
name: decision-bias
description: 决策偏见速查——9种常见决策暗知识，决策前必过一遍
version: 1.0.0
author: 黄药师
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [偏见, 认知偏差, bias, 决策陷阱, 暗知识]
    related_skills: [decision]
---

# 决策偏见速查

决策前必过的 9 种常见偏见——来自 Y 模型域暗知识卡聚合。

## Constraints

<hard_limits>
- 偏见速查必须决策前做，不能决策后找借口
- 如果发现 ≥3 种偏见同时出现，暂停决策
</hard_limits>

## 9 种决策暗知识

### 1. 确认偏差
**症状**：只找支持自己判断的证据，忽略反面证据。
**检查**：我有没有主动找 ≥2 条反对自己判断的证据？
**卡**：`master-cognitive-bias-checklist`

### 2. 过度自信
**症状**：对自己的判断信心过高，实际准确率远低于自称。
**检查**：我过去的类似判断，实际准确率是多少？有没有记录？
**修复**：记录每次判断 + 回顾验证 → 校准自信。

### 3. 锚定效应
**症状**：第一次听到的数字/判断影响后续所有判断。
**检查**：我现在的判断是否被某个"先入为主"的数字锚定了？
**修复**：先独立判断，再看别人的数字（`/decision-hygiene` Step 1）。

### 4. 幸存者偏差
**症状**：只看到成功案例，没看到大量失败案例。
**检查**：我有没有主动找失败案例？失败率是多少？
**卡**：`dk-yitang-survivor-bias-in-research`

### 5. 价值观覆盖 ROI
**症状**：当价值观权重超过经济理性时，硬套 ROI 公式做决策。
**检查**：这个决策本质上是"值不值得做"还是"想不想做"？
**卡**：`dk-decision-value-overrides-roi`

### 6. 解释性本质陷阱
**症状**：满足于"解释过去"的框架，但框架不能预测未来。
**检查**：这个框架上一次指导了哪个真实决策？结果怎样？
**卡**：`dk-modeling-explanatory-vs-predictive-essence`

### 7. AI 判断外包
**症状**：把本该自己做的判断外包给 AI。
**检查**：AI 给的结论，我有没有独立验证？
**卡**：`dk-ai-judgment-human-responsibility`、`dk-modeling-ai-judgment-limit`

### 8. 噪声混淆
**症状**：把不同人对同一问题的判断差异当成"观点不同"，没意识到是噪声。
**检查**：团队成员的判断差异，是因为假设不同还是噪声？
**修复**：`/decision-hygiene` 五步降噪。

### 9. 外部视角缺失
**症状**：只从内部视角看问题，没参考类似情境的基准概率。
**检查**：类似情况下，base rate（基准概率）是多少？
**卡**：`skill-decision-outside-view`

## 决策前速查

```
□ 1. 确认偏差 — 找了 ≥2 条反面证据？
□ 2. 过度自信 — 过去类似判断准确率？
□ 3. 锚定效应 — 被某个数字锚定了？
□ 4. 幸存者偏差 — 看过失败案例？
□ 5. 价值观覆盖 — 是想做还是值得做？
□ 6. 解释性本质 — 能指导行动吗？
□ 7. AI 判断外包 — 独立验证了吗？
□ 8. 噪声混淆 — 是观点不同还是噪声？
□ 9. 外部视角 — base rate 是多少？
```

≥3 个答不上来 → 暂停决策，补缺后再做。

## 参考卡片
- `master-cognitive-bias-checklist`
- `dk-decision-value-overrides-roi`
- `dk-modeling-explanatory-vs-predictive-essence`
- `dk-ai-judgment-human-responsibility`
- `skill-decision-outside-view`
- `skill-decision-delay-intuition`
