---

id: framework-strategy-five-basics
title: 冉鹏战略五基本功（5C）：定式/洞察/布局/体系/变革
type: framework
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.88
trust_level: high
language: zh-CN
domain: strategy
source_refs:
- src_unknown
related:
  - "[[strategy-domain-digest]]"
  - "[[ocr-一堂-高阶体系探索营-三种咨询可能性]]"
  - "[[tool-mece体系框架法]]"
  - "[[一堂方法论体系总图]]"
  - "[[tool-敏捷发布快速迭代搭建体系]]"
  - "[[tool-马易-销售智能体体系搭建路径]]"
  - "[[tool-体系框架构建]]"
updated_at: '2026-06-29'
---

# 战略五基本功（5C）

> 战略不只是"定目标"——五基本功覆盖了从框架到执行的完整能力链。大多数公司只练了其中1-2个。

## 5C展开

| # | 基本功 | 英文 | 核心内容 |
|:---:|:---|:---|:---|
| 1 | **定式** | Core foundation | BRM框架为基——差距分析→战略规划→执行，形成肌肉记忆 |
| 2 | **洞察** | Critical insight | 模型+图表+假设验证。速度（多快发现机会）+视野（看多宽） |
| 3 | **布局** | Configuration layout | 三个地平线+撤退+突破——不是做什么，是不做什么 |
| 4 | **体系** | Creation system | 构建生态系统——竞争优势三层：核心价值→生态系统→心智护城河 |
| 5 | **变革** | Change management | 转型三种方式：加外挂/换路/换轮子 |

## 竞争优势三层（融入"体系"）

1. **核心价值**：你的产品/服务比对手好在哪？（最容易复制）
2. **生态系统**：供应商/合作伙伴/渠道形成了什么壁垒？（中等难度）
3. **心智护城河**：客户想到品类第一个想到你？（最难复制）

## Agent执行指令

```python
# 五基本功评估
def assess_5c(company):
    scores = {}
    for c in ["定式", "洞察", "布局", "体系", "变革"]:
        scores[c] = rate(company, c, scale=1-5)
    weakest = min(scores, key=scores.get)
    return f"最弱基本功：{weakest}，优先补强"
```

## 失败模式

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| 只练定式 | 有框架没洞察 | 五基本功是五项独立的肌肉，都需要训练 |
| 体系=局部优化 | 把"建个CRM"当生态 | 体系是外部伙伴+内部流程的系统协同 |

## 适用边界

- src_unknown
- src_unknown

---

*卡片类型：framework | 审核状态：待审*
