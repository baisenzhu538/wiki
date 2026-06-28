---


id: skill-research-triangulation-stop-rule
title: 多源交叉验证的停止规则
type: skill
status: enriched
confidence: 0.80
trust_level: high
language: zh-CN
domain:
- src_unknown
- src_unknown
source_person: 王语嫣
source_context: research 域 40 张 case 卡跨案例合成，洞察 2
source_refs:
- 60_feedback/audit/synthesis_research.md
- 30_wiki/dk/dk-research-triangulation-stop-rule.md
created_at: "2026-06-25"
updated_at: "2026-06-25"
author: 王语嫣
reviewed_by: 欧阳锋
review_date: "2026-06-25"
related:
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
diagnostic_signals:
  - framework_lens: 边际收益规则
    follow_up_question: "新增一个来源预计能改变当前结论的概率是否 >30%？"
  - framework_lens: 置信度阈值规则
    follow_up_question: "当前综合置信度是否已达到预设阈值？阈值是多少？"
  - framework_lens: 决策延迟成本规则
    follow_up_question: "继续验证的延迟成本是否已超过决策错误的预期损失？"
---

# 多源交叉验证的停止规则

> **Burn line**：交叉验证不是越多越好，而是一个成本-置信度权衡问题——当新增一个验证源带来的置信度提升已经低于其时间/金钱/机会成本时，就应该停止。

---

## 何时使用

- src_unknown
- src_unknown
- src_unknown
- src_unknown

---

## 核心框架：把「停止」变成可计算的决策

| 步骤 | 操作 | 判断标准 |
|:---|:---|:---|
| 1. 标定关键信息 | 列出会改变决策的 3-5 条关键信息 | 如果这条信息错了，决策会怎么变？ |
| 2. 设定目标置信度 | 为每条关键信息设定决策所需置信度 | 高风险决策 ≥0.85；低风险决策 ≥0.70 |
| 3. 列出独立来源 | 为每条信息列出至少 2 个可获取的独立来源 | 来源之间不能有共同的生成机制 |
| 4. 计算边际成本 | 评估新增一个来源需要的时间、金钱、机会成本 | 包括决策延迟成本 |
| 5. 应用停止规则 | 当新增来源的期望置信度提升 < 边际成本时停止 | 把资源转回决策或实验 |

---

## 停止规则的三种形态

1. **置信度阈值规则**
   当关键信息的综合置信度达到预设阈值，即可停止。例如，三个独立来源一致，且覆盖「一手数据 + 专家 + 行为痕迹」，可认为足够。

2. **边际收益规则**
   新增一个验证源后，若结论没有实质性改变，且反例未出现，继续验证的收益递减。

3. **决策延迟成本规则**
   即使置信度未达理想值，如果继续验证会导致错过窗口期，应停止并采用「小规模实验」替代「继续调研」。

---

## 快速检查单

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

---

## 失败模式

| 失败模式 | 症状 | 修复 |
|:---|:---|:---|
| 验证过度 | 不同来源已一致，仍不断寻找「更权威」来源 | 设定置信度阈值并执行 |
| 验证不足 | 只有单一二手来源就做大额决策 | 强制至少 2 个独立来源 |
| 伪独立来源 | 五个来源都是同一篇报告的不同转载 | 检查来源生成机制是否独立 |
| 把安全感当标准 | 老板问「够稳了吗」，只能回答「再保险一点」 | 用量化阈值替代感觉 |

---

## 适用边界

- src_unknown
- src_unknown

---

## 行动触发器

- src_unknown
- src_unknown
- src_unknown

---

## 关联卡片

- src_unknown
- src_unknown
- src_unknown

---

*作者：王语嫣 | 复核：欧阳锋 | 来源：research 域跨案例合成报告*
