---

id: tool-harness-adversarial-tester
title: 对抗测试员：成功标准是"找到bug"
type: tool
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.88
trust_level: high
language: zh-CN
domain:
  - yitang
  - ai-collaboration
source_refs:
- 10_raw/sources/src_20260621_harness-engineering-wanghuan.md
related:
  - [[tool-devils-advocacy]]
  - [[case-strategy-xiaobear]]
  - [[tool-candy-oral-polish]]
  - [[framework-structured-analytic-techniques]]
  - [[tool-red-team-analysis]]
  - [[tool-red-team-analysis]]
  - [[tool-devils-advocacy]]
  - [[framework-wanghuan-gan-three-roles]]
---
# 对抗测试员

> 与Red Team和Devil's Advocacy的三层区分：Red Team = 模拟竞对战略决策（战略层），Devil's Advocacy = 攻击逻辑漏洞（逻辑层），Adversarial Tester = 攻击具体产出物（执行层）。

## 三层攻击体系

| 技术 | 攻击对象 | 层级 | 适用 |
|:---|:---|:---|:---|
| **Red Team** | 竞对的战略决策 | 战略层 | 市场进入、产品规划 |
| **Devil's Advocacy** | 自己的结论逻辑 | 逻辑层 | 商业计划评审、假设检验 |
| **Adversarial Tester** | 具体的代码/文档/方案 | 执行层 | 代码质量、方案漏洞 |

## 对抗测试员的操作

**成功标准**：找到bug = 成功，找不到 = 失职。这与普通测试员的"通过测试=成功"完全相反。

**攻击方法**：
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## Agent执行指令

```python
# 对抗测试员Prompt
prompt = """你是一个对抗测试员。你的KPI是找到bug。
你的成功标准不是"测试通过"，而是"找到了问题"。

对以下产出物执行攻击：
1. 空值/null——系统会崩吗？
2. 边界值——最大值+1会怎样？最小值-1会怎样？
3. 恶意输入——如果用户输入\"<script>alert('xss')</script>\"呢？
4. 并发——同时执行两个操作会冲突吗？
5. 真实用户的奇怪行为——用户会做的任何奇怪操作

输出：找到的所有bug，按严重程度排序（CRITICAL/MAJOR/MINOR）
"""
```

## 失败模式

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| 测试太温柔 | 报告"没发现问题"但用户一用就崩 | 给Agent更强的对抗激励 |
| 过度攻击 | 报告一堆不可能发生的极端情况 | 区分"真实用户会做的"和"理论上可能但不会发生的" |

## 适用边界

- src_unknown
- src_unknown

---

*卡片类型：tool | 审核状态：待审*
