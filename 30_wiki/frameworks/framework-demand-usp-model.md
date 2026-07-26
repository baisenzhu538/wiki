---
id: framework-demand-usp-model
title: USP需求洞察模型：Demand = User × Situation × Problem
type: framework
status: reviewed
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.9
trust_level: high
language: zh-CN
domain:
- yitang
- five-step-method
source_refs:
- 00_inbox/五步法之需求分析/一堂-需求分析-需求洞察USP模型-图-01_ocr_text.md
related:
- '[[yitang-domain-digest]]'
- '[[yt-note-problem-solving-capability]]'
- '[[yt-demand-level-assessment]]'
- '[[tool-demand-iceberg-l1-user]]'
- '[[case-demand-pharma-bigdata]]'
- '[[yt-demand-peak-end-rule]]'
- '[[tool-月白-AI模型选择策略]]'
- '[[tool-demand-iceberg-l3-core-job]]'
- '[[tool-demand-iceberg-l6-hypothesis]]'
- '[[yt-demand-insight-extraction]]'
- '[[concept-最简单元模型]]'
- '[[case-treadmill-demand-analysis]]'
- proposal-prompt-injection-infrastructure
- tool-yitang-amazon-bestseller
updated_at: '2026-06-29'
tags:
- audience:ceo
- scene:diagnosis
- skill-level:advanced
aliases:
- 五步法之需求分析
- 需求分析
---
# USP需求洞察模型

> Demand = User × Situation × Problem。需求不来自"用户是谁"，来自"用户在特定场景下遇到了什么阻碍"。

## 公式拆解

| 因子 | 含义 | 问题 |
|:---|:---|:---|
| **U**ser | 谁？上一个用户→当前用户→下一个用户的流转 | 我的核心用户边界在哪？ |
| **S**ituation | 在什么场景下？→ 触发什么任务(JTBD)？ | 这个场景下用户要完成什么？ |
| **P**roblem | 有什么阻碍？→ 现有方案和理想状态之间的差距(Gap) | 是什么阻止了用户完成任务？ |

## 与冰山模型的关系

USP是需求分析的"入口公式"，冰山模型的L1-L6是需求分析的"深度展开工具"。USP帮你快速定位需求，冰山模型帮你系统化验证。

## Agent执行指令

```python
prompt = """用USP模型分析以下需求：

U（用户）：谁在经历这个问题？用户画像+边界
S（场景）：在什么具体情境下？触发什么任务？
P（阻碍）：用户遇到了什么障碍？现有方案的差距在哪？

输出公式：Demand = U × S × P
"""
```

## 适用边界

- src_unknown
- src_unknown

---

*卡片类型：framework | 审核状态：待审*
