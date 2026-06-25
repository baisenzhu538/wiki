---

id: tool-strategy-nine-problems
title: 九个常见战略问题：方向/目标/定位/路径/共识/组织/能力/资源/机制
type: tool
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.9
trust_level: high
language: zh-CN
domain:
- strategy
source_refs:
- 00_inbox/战略专题/冉鹏老师战略课程知识点_ocr.md §11-20
related:
  - '[[case-strategy-failure-01-cosmetics]]'
  - '[[case-strategy-failure-07-phone-l]]'
  - '[[case-strategy-failure-06-phone-n]]'
  - '[[tool-strategy-four-moves]]'
  - '[[ocr-一堂-ai学习-提问工程化]]'
- '[[framework-strategy-brm]]'
---

# 九个常见战略问题

> 企业出问题，表面上是"业绩不好"，根因往往在这九个问题的某一个。鱼骨图帮你拆解，九问题帮你定位类型。

## 九问题速查

| # | 问题类型 | 关键信号 | 案例 |
|:---:|:---|:---|:---|
| 1 | 方向错误 | 在太小的市场里拼命 | 长尾品类化妆品H |
| 2 | 目标错误 | 在高速增长期追求盈利 | 精品超市O |
| 3 | 定位错误 | 盲目高端→丢低端 | 清洁用品L |
| 4 | 路径错误 | 重渠道轻研发 | 家电公司G |
| 5 | 共识不足 | 高层反复横跳 | IT公司H |
| 6 | 组织僵化 | 组织不适→迭代缓慢 | 手机公司N |
| 7 | 能力缺失 | 无软件生态→收购失败 | 国产手机L |
| 8 | 资源短缺 | 版权库太弱 | 视频平台B |
| 9 | 机制背离 | 激励偏财务→安全事故 | 飞机制造公司 |

## Agent执行指令

```python
# 九问题初步诊断
def diagnose_nine(company_symptoms):
    for i, problem in enumerate(NINE_PROBLEMS):
        if match(company_symptoms, problem.signals):
            return f"初步判断：问题类型 #{i+1} - {problem.name}"
```

## 失败模式

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| 只看到表面 | "业绩不好"→直接做促销 | 用鱼骨图拆到根因，对照九问题定位 |

## 适用边界

- **适用**：企业问题的初步诊断和分类
- **不适用**：问题根源已经很明确时

---

*卡片类型：tool | 审核状态：待审*
