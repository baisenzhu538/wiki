---
id: concept-strategy-framework-landscape
title: 战略框架全景图：冉鹏覆盖了什么、没覆盖什么
type: concept
status: reviewed
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.88
trust_level: high
language: zh-CN
domain: strategy
source_refs:
- 60_feedback/diagnosis/diag_20260621_战略域_冉鹏框架_交叉验证.md
related:
- '[[strategy-domain-digest]]'
- '[[pending_unknown]]'
- tool-strategy-pareto
updated_at: '2026-06-29'
tags:
- audience:general
- scene:reference
- skill-level:advanced
---
# 战略框架全景图

> 冉鹏框架是"中国实战提炼的完整战略体系"，但不是"战略领域的全部"。Agent用这张卡知道：冉鹏覆盖了什么、没覆盖什么、缺的部分去哪找。

## 冉鹏覆盖的（本域已入库）

| 冉鹏框架 | KDO卡 | 覆盖领域 |
|:---|:---|:---|
| BRM框架 | `framework-strategy-brm` | 战略闭环管理 |
| 六阶段 | `framework-strategy-six-stages` | 企业生命周期 |
| 五基本功 | `framework-strategy-five-basics` | 战略能力建设 |
| 九问题 | `tool-strategy-nine-problems` | 战略诊断 |
| 竞争优势三层 | 融入 五基本功§体系 | 竞争优势 |

## 冉鹏未覆盖的战略领域（需外域补充）

| 缺失框架 | 领域 | 何时用 |
|:---|:---|:---|
| **波特五力** | 行业竞争结构 | 分析行业吸引力、进入壁垒 |
| **VRIO** | 资源基础观 | 判断竞争优势是否可持续 |
| **蓝海战略ERRC** | 市场创造 | 创造新需求而非争夺现有市场 |
| **PESTLE** | 宏观环境 | 政治/经济/社会/技术/法律/环境扫描 |
| **Greiner模型** | 组织成长危机 | 诊断组织不同阶段的典型危机 |
| **BCG矩阵** | 业务组合管理 | 多业务线的资源分配 |

## Agent选择决策

```python
# 什么时候用冉鹏框架 vs 外部框架
def select_framework(problem_type):
    if problem_type in ["战略闭环", "阶段诊断", "组织问题"]:
        return "冉鹏框架（BRM/六阶段/九问题/鱼骨图）"
    elif problem_type in ["行业分析", "竞争结构"]:
        return "波特五力"
    elif problem_type == "竞争优势可持续性":
        return "VRIO"
    elif problem_type == "新市场创造":
        return "蓝海战略ERRC"
    elif problem_type == "外部框架补充":
        return "创新方向框架（凯纳跨界战略咨询）——补充蓝海战略以外的跨界创新视角"
```

---

*卡片类型：concept | 审核状态：待审*
