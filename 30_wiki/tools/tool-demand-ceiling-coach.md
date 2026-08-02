---
id: tool-demand-ceiling-coach
title: 天花板测算教练：10-15分钟对话输出天花板报告
type: tool
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-07-08
confidence: 0.85
trust_level: medium
language: zh-CN
created_at: 2026-07-08
updated_at: 2026-07-08
domain:
- yitang
- demand-analysis
aliases:
  - 15分钟对话输出天花板报告
  - signal: 创始人给的天花板数字是TAM的1%
  - 分钟对话输出天花板报告
  - 天花板测算教练
  - 天花板测算教练：1015分钟对话输出天花板报告
  - 板测算教练
source_refs:
- 00_inbox/五步法之需求分析/一堂-需求分析-空间测算-口述.txt L322-L344,L1308-L1870
related:
- '[[framework-demand-ceiling-four-lines]]'
- '[[tool-demand-assessment-triangle]]'
- '[[tool-demand-iceberg-l6-hypothesis]]'
- '[[tool-demand-chai-tui-ping-suan-guide]]'
- '[[domain-demand-analysis-index]]'
- '[[yt-entrepreneur-unit-model]]'
- '[[yt-market-size-estimation]]'
diagnostic_signals:
quality_labels:
- actionable
---
# 天花板测算教练：10-15分钟对话输出天花板报告

> **一句话**：不用花半天做Excel。跟AI聊10-15分钟，从BEL一路垒到SOM，输出融资版和经营版两套天花板数字。

---

## 何时用

- 准备见投资人，需要一套靠谱的天花板数字
- 制定年度计划，需要从BEL推导SOM
- 被合伙人问"这个方向天花板多大"——自己也不确定

## 对话流程

### 第1-3分钟：锁定项目信息

```
Q1: 你的产品/服务是什么？（一句话）
Q2: 目标用户是谁？（L1用户标签即可）
Q3: 现在有收入吗？多少？（如果有，这就是BEL的起点）
Q4: 这次算天花板是融资用还是经营用？
```

### 第4-7分钟：从底往上垒

```
融资版路径：确认TAM→SAM（跳过SOM/CR1/BEL）——5分钟够
经营版路径：确认BEL→CR1→SOM——10分钟

Q5: 你现在确认"死活都能做到"的收入是多少？（BEL）
    → 如果没有，问：按最低价格×最保守用户数，能到多少？
Q6: 第一年能做到多少？（CR1 = BEL × 增速系数）
    → 增速系数基于：渠道能力×产品差异化×团队执行力
Q7: 三年内能做到多少？（SOM = CR1 × 拓展系数²）
    → 拓展系数基于：品类增速×竞争格局×复制能力
```

### 第8-15分钟：出报告

输出结构化天花板报告（见下方模板）。

## 输出模板

```markdown
# 天花板测算报告：[项目名称]

## 基本信息
- 产品/服务：
- 目标用户：
- 测算日期：
- 版本：融资版 / 经营版

## 五层线
| 层 | 数字 | 算法 | 置信度 |
|:---|:---|:---|:---:|
| TAM | X亿 | [来源：XX报告2026] | [确认]/[假设] |
| SAM | X亿 | [品类适配] | [确认]/[假设] |
| SOM | X亿 | [BEL→CR1→SOM] | [确认]/[假设] |
| CR1 | X千万 | [BEL×增速系数] | [确认]/[假设] |
| BEL | X百万 | [已确认收入/保守估算] | [确认]/[假设] |

## 关键假设
1. [假设1]：如果这个变了，SOM会变多少？
2. [假设2]
3. [假设3]

## 风险提示
- 最大风险：[哪个假设最不可靠？]
- 底线：如果最坏情况发生，BEL还能守住吗？
```

## 失败模式

| 模式 | 症状 | 修复 |
|:---|:---|:---|
| BEL虚报 | 说"死活能做到"其实没做到过 | 追问：这个数字有合同/订单/付款记录吗？ |
| 增速拍脑袋 | "第二年翻3倍"——没有依据 | 要求拆分：渠道/产品/团队各贡献多少增速 |
| 融资经营混 | 报告里TAM和SOM的算法对不上 | 标注版本——融资版和经营版分开出 |
