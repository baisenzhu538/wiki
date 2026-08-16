---
name: five-step
description: 一堂五步法总入口——需求→产品内核→商业模式→增长→壁垒
version: 1.0.0
author: 黄药师
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [五步法, 创业, 商业分析, 商业模式, 增长, 壁垒]
    related_skills: [five-step]
---

# 五步法（Five-Step Method）

一堂五步法：需求→产品内核→商业模式→增长→壁垒。创业分析的底层操作系统。

## Constraints

<hard_limits>
- 五步必须按顺序——前一步的输出是后一步的输入，跳步意味着质量折半
- 每步产出一个明确的交付物，不得用"了解了"代替
</hard_limits>

## Pipeline 架构

```
/five-step-demand       → 需求是否真实？市场多大？
        ↓ (输出：需求验证报告)
/five-step-product      → 产品内核是什么？用户为什么选你？
        ↓ (输出：产品内核画布)
/five-step-business-model → 怎么赚钱？单元模型是否成立？
        ↓ (输出：商业模式画布)
/five-step-growth       → 怎么增长？增长引擎是什么？
        ↓ (输出：增长策略)
/five-step-barrier      → 壁垒在哪？能守多久？
        ↓ (输出：壁垒评估 + 综合结论)
```

## 意图分类

| 问题 | 路由到 |
|:--|:--|
| "这个需求真的存在吗？" | `/five-step-demand` |
| "用户为什么会选我？" | `/five-step-product` |
| "怎么赚钱？能持续吗？" | `/five-step-business-model` |
| "怎么增长？增长引擎？" | `/five-step-growth` |
| "壁垒在哪？能守多久？" | `/five-step-barrier` |
| 完整分析 | 按 Pipeline 全流程 |

## 参考卡片
- `five-step-domain-digest` — 域索引入口（66张卡）
- `yt-five-step-method` — 五步法总纲
- `yt-entrepreneur-five-step-method` — 创业者五步法
