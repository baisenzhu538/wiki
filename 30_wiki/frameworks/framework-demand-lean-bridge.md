---
id: framework-demand-lean-bridge
title: 需求判断与精益验证的衔接
type: framework
status: reviewed
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-23
quality_labels:
- cited
- principle
- validated
created_at: 2026-06-23
confidence: 0.82
trust_level: medium
language: zh-CN
domain:
- yitang
- lean-startup
- five-step-method
source_refs:
- 60_feedback/audit/cross-domain-bridge-design-specs.md
- 30_wiki/frameworks/framework-demand-iceberg.md
- 30_wiki/tools/tool-demand-iceberg-l1-user.md
- 30_wiki/tools/tool-demand-iceberg-l2-scenario.md
- 30_wiki/tools/tool-demand-iceberg-l3-core-job.md
- 30_wiki/tools/tool-demand-iceberg-l4-job-map.md
- 30_wiki/tools/tool-demand-iceberg-l5-forces.md
- 30_wiki/tools/tool-demand-iceberg-l6-hypothesis.md
related:
discoverable_by:
  - "需求判断精益验证"
  - "需求到精益衔接"
  - "精益需求验证桥接"
- '[[framework-demand-iceberg]]'
- '[[framework-lean-false-model]]'
- '[[framework-lean-abcd-model]]'
- '[[yitang-domain-digest]]'
- '[[lean-startup-domain-digest]]'
- '[[framework-demand-validation-pipeline]]'
updated_at: '2026-06-30'
tags:
aliases:
  - 需求判断与精益验证的衔接
  - 精益衔接
  - 求判断精益验证
  - 断精益验证
  - 求验证桥接
  - 判断与精益验证的衔接
aliases:
  - 需求判断与精益验证的衔接
  - 益需求验证桥接
  - 求到精益衔接
  - 求判断精益验证
- audience:ceo
- scene:diagnosis
- skill-level:intermediate
aliases: []
---

# 需求判断与精益验证的衔接

> 把需求分析冰山（L1–L6）中识别出的需求假设，用 FALSE 模型和 ABCD 模型进行低成本验证。

## 触发问题

- src_unknown
- src_unknown
- src_unknown

## 端到端流程

```
需求分析输出（来自 yitang 五步法 / 需求冰山）
  ├── L1 用户标签    → 验证：这类用户是否真实存在且可触达
  ├── L2 场景问题    → 验证：这个场景是否真实发生且足够痛苦
  ├── L3 核心任务    → 验证：用户是否用一致的语言描述任务
  ├── L4 任务地图    → 验证：任务链中的崩溃点是否准确
  ├── L5 四种力量    → 验证：推力+拉力是否显著大于焦虑+习惯
  └── L6 机会假设    → 验证：这个机会是否值得做成产品
           ↓
    用 RAT 提取每层最危险假设
           ↓
    用 ABCD 模型排序（致命性 × 证据缺口）
           ↓
    用 FALSE 模型选择最低成本验证工具
           ↓
    设计实验 → 执行 → 收集信号 → 更新冰山洞察
```

> 流程结构参考 [[framework-demand-iceberg]] 的“拆·推·评”三段与 [[framework-lean-false-model]] 的成本光谱 [conf=0.82, source=60_feedback/audit/cross-domain-bridge-design-specs.md]。

## 冰山层级 → 典型假设 → 验证工具 → 通过标准

| 冰山层级 | 典型假设 | 验证工具 | 通过标准 | 不通过标准 |
|:---|:---|:---|:---|:---|
| L1 用户标签 | 这类用户存在且可触达 | 假营销、社群测试、广告定向 | 获取成本可控，用户特征与画像一致 | 定向投放 CTR < 1%，获客成本远高于行业均值 |
| L2 场景问题 | 这个场景真实发生且痛苦 | 用户访谈、Reddit/评论分析、客服记录挖掘 | 用户主动描述痛苦，无需引导 | 访谈中需反复提示才能说出问题 |
| L3 核心任务 | 用户用一致语言描述任务 | 访谈、问卷调查、Job Story 验证 | 70%+ 用户用一致动词+对象+语境描述任务 | 用户描述五花八门，无法收敛到统一任务 |
| L4 任务地图 | 任务链中的崩溃点准确 | 用户共创、原型测试、崩溃感识别 | 用户在关键步骤有强烈共鸣，CES 峰值出现在同一处 | 用户认为“最痛苦”的环节与预设不同 |
| L5 四种力量 | 推力+拉力 > 焦虑+习惯 | 量表问卷、A/B 测试、切换访谈 | 推力显著大于惯性，拉力足以抵消焦虑 | 用户表示“现在方案也够用，懒得换” |
| L6 机会假设 | 这个组合值得做产品 | 假产品页面、预售、MVP | 付费转化或深度承诺（预购/推荐信） | 大量兴趣但无付费/承诺 |

> 上表工具映射来自 [[framework-lean-false-model]] 与 [[framework-lean-abcd-model]] 的接口设计 [conf=0.82, source=60_feedback/audit/cross-domain-bridge-design-specs.md]。

## 与相邻卡的关系

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 失败模式

| 失败模式 | 症状 | 修复 |
|:---|:---|:---|
| 把访谈态度当付费意愿 | L2/L3 用户说“这个想法很好”，但 L6 无付费转化 | 必须让 L6 的机会假设包含“愿意付费/承诺”的验证，不能停留在口头兴趣 |
| 把单点数据当普遍需求 | 3 个用户提到同一个痛点，就认为是市场机会 | 用定量工具（问卷/假营销）验证普遍性，至少覆盖 30–50 个目标样本 [conf=0.80, source=30_wiki/tools/tool-demand-iceberg-l6-hypothesis.md] |
| 跳过 L5 直接验证 L6 | 机会卡片看起来很 sharp，但缺少“用户会不会切换”的洞察 | 回到 L5 的四种力量分析，确认（推力+拉力）>（焦虑+习惯） |
| 验证工具错配 | 用 landing page 验证 L3 的核心任务描述 | L3 应先用访谈/问卷收敛任务语言，L6 才适合用 landing page |
| RAT 不够致命 | 列出的假设错了也不会让机会消失 | 每条 RAT 必须通过“如果错了，机会就不存在”的测试 |

## 适用边界

- src_unknown
- src_unknown

---

*老顽童 · 2026-06-23 · 跨域融合计划（策略 A）P2 桥接卡*
