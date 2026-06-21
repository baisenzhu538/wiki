---
name: decision
description: 科学决策总入口——Y模型+决策卫生+预判模型+偏见速查
version: 1.0.0
author: 黄药师
license: MIT
platforms: [cli, feishu]
metadata:
  hermes:
    tags: [决策, Y模型, 决策卫生, 预判, 偏见, 科学决策]
    related_skills: [decision]
---

# Decision（科学决策总入口）

基于一堂科学决策方法论。核心命题：在不确定中做出比别人更好一点的判断。

## Constraints

<hard_limits>
- 决策类问题必须先判断类型：个人决策 vs 团队决策；可逆 vs 不可逆
- 任何决策建议必须标注不确定性——"这个判断的置信度是X，最可能错的原因是Y"
</hard_limits>

## 意图分类

| 类型 | 路由到 | 示例 |
|:--|:--|:--|
| 团队决策/多人判断不一致 | `/decision-hygiene` | "团队对估值判断差5倍怎么办" |
| 个人决策/需要结构化框架 | `/decision-y-model` | "要不要换工作" |
| 预判未来/趋势判断 | `/decision-prediction` | "这个市场三年后会怎样" |
| 决策偏见自查 | `/decision-bias` | "我现在的判断可能有哪种偏见" |

## 决策类型判断

```
决策前先问：
├── 可逆吗？→ 可逆：快速决定，不纠结
├── 个人 vs 团队？→ 团队：先各自独立判断 → 决策卫生聚合
├── 有数据吗？→ 有：Y模型 / 没有：预判模型
└── 时限？→ <1天：直觉+偏见速查 / >1天：完整流程
```

## 参考卡片
- `master-decision-hygiene` — 决策卫生五步法
- `yt-decision-y-model-philosophical-roots` — Y模型哲学根基
- `yt-model-prediction-model` — 预判模型
