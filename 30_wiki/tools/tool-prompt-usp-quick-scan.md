---
id: tool-prompt-usp-quick-scan
title: USP 快速需求拆解——3分钟单轮提示词模板
type: prompt-template
status: enriched
confidence: 0.88
trust_level: high
domain:
  - src_unknown
prompt_role: "需求分析助手——基于USP模型快速拆解业务需求"
prompt_methodology: "USP模型（用户-场景-问题）三维拆解"
prompt_version: "1.0.0"
source_refs:
  - 00_inbox/五步法之需求分析/AI辅助探讨需求选项的提示词.md
created_at: "2026-06-21"
updated_at: "2026-06-21"
author: 黄药师（从程诚同学提示词提取）
reviewed_by: 欧阳锋
related:
  - src_unknown
  - src_unknown
---

# USP 快速需求拆解

> `prompt-template` — 3分钟单轮提示词。与 USP 深度洞察引擎（重型）互补——这个是快速版。

## 触发场景

需求初步梳理、快速输出核心框架。适合新手、时间紧张、或只需要"第一版"拆解的场景。如果需要深度分析，用 `tool-prompt-usp-demand-analysis`。

## 完整提示词

```markdown
我需要基于"用户-场景-问题"USP模型拆解业务需求，请按以下要求输出结构化结果：
1. 核心任务：帮我拆解【你的业务名称，例：ToB灵活用工结算服务】的需求；
2. 拆解维度（每维度至少3条关键信息）：
   - src_unknown
   - src_unknown
   - src_unknown
3. 输出格式：
   - src_unknown
   - src_unknown
   - src_unknown
```

## 定制方法

| 操作 | 说明 |
|:--|:--|
| 替换 `【你的业务名称】` | 如"社区生鲜配送服务""通信基站兼职结算系统" |
| 不需要额外补充信息 | AI 会基于通用逻辑输出基础框架 |
| 如果输出模糊 | 追加"请为每个维度补充至少1个具体数字或案例" |

## 输出示例

```
- src_unknown
- src_unknown
  1. 拆用户：主体-三大运营商运维部门、中小代维外包企业(50-200人)；属性-运营商(国企，合规优先)、代维商(民企，成本+效率优先)；诉求优先级-合规票据＞结算效率＞成本控制
  2. 拆场景：时间-基站紧急抢修后24小时内、5G工程集中攻坚期、季度报税前夕；空间-偏远基站、城市商圈室分站点；事件-台风后故障抢修、开学季宽带装机
  3. 拆问题：合规痛点-兼职无发票，企业无票支出面临税务风险；效率痛点-分散人员对账慢，批量发薪需2-3天；应急痛点-紧急场景下结算滞后影响兼职人员积极性
- src_unknown
```

## 设计原理

| 设计决策 | 为什么有效 |
|:--|:--|
| 单轮而非多轮 | 快速决策场景下，多轮追问会让用户放弃——一次给够 |
| 每维度"至少3条" | 3条是"足够具体"的最小阈值——1条是随口说，3条是认真想了 |
| 输出格式预定义 | 预定义格式降低了AI自由发挥出错的可能 |
| 不含字典 | 与重型版的关键差异——字典会增加10倍token但3分钟场景不需要 |

## 已知局限

- src_unknown
- src_unknown
- src_unknown
- src_unknown
