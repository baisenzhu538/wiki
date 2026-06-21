---
id: concept-candy-ai-as-collaborator
title: Candy：AI是协作者而非代写工具
type: concept
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.90
trust_level: high
language: zh-CN
domain: [yitang, content-production, ai-collaboration]
source_refs:
- 10_raw/sources/src_20260621_candy-transcript-workflow.md
related:
- "[[framework-wanghuan-gan-three-roles]]"
- "[[concept-harness-cattle-not-pets]]"
- "[[framework-candy-transcript-workflow]]"
---

# AI是协作者而非代写工具

> 方向感必须是人的。AI可以跑很快，但不知道往哪跑。

## 人机分工

| 人负责（不可委派） | AI负责（可委派但需验收） |
|:---|:---|
| 方向判断——这篇东西要讲什么 | 整理——把杂乱素材结构化 |
| 真实案例——只有你经历过的事 | 抽象——从案例中提取可迁移的原则 |
| 指出"哪里不像我"——判断AI输出是否贴合人设 | 扩写——在给定框架下充实内容 |
| 决定保留/删除——最终的取舍权 | 归位——把素材放到正确的位置 |
| | 润色——口语化、短句、连接词 |
| | 生成不同版本——提供选项供人选择 |
| | 学习已有风格——模仿你的表达方式 |

## 与王欢Harness的同构

| Candy | 王欢 Harness | 共同原则 |
|:---|:---|:---|
| 人做方向判断 | 人做Planning(Phase 0-1) | 战略层不可委派 |
| AI负责整理/抽象/润色 | Generator(Sonnet)执行 | AI擅长战术执行 |
| 人指出"哪里不像我" | Evaluator评审 | 验收标准在人的判断 |
| 牲口而非宠物 | Cattle-not-pets | 每次迭代全新实例 |

## 关键原则

- **方向感必须是人的**：AI不知道你的听众是谁、你的品牌调性是什么、你想传递什么价值观
- **人是最终验收者**：AI可以生成10个版本，但只有一个版本是"对的"——这需要人来判断
- **不要问AI"你觉得怎么样"**：问"这里有3个版本，哪个更符合'我想传递X感觉'？"——把判断标准给人，把执行给AI

## 适用边界

- **适用**：内容创作、方案设计等需要"个人风格"和"价值判断"的场景
- **不适用**：纯数据提取、格式化输出等不需要判断的机械任务

---

*卡片类型：concept | 审核状态：待审*
