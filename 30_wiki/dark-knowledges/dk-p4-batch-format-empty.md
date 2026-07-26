---
id: dk-p4-batch-format-empty
title: P-4：批量格式升级产生"格式完整但思维空洞"卡片 (C-8)
type: dk
dark_knowledge_type: failure
status: reviewed
domain:
- master
source_person: system
source_context: pitfalls.md P-4
source_refs:
- src_unknown
created_at: 2026-06-03
updated_at: '2026-06-18'
related: null
pipeline:
- src_unknown
- src_unknown
- src_unknown
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown# P-4：批量格式升级产生"格式完整但思维空洞"卡片 (C-8)
tags:
- audience:executor
- scene:reference
- skill-level:intermediate
---

## 原始表述/核心洞察

> **症状**：抽检 `motivation-resistance` 和 `peak-end-rule` 两张卡——格式符合 agent-native 标准，但 Claims 无具体反例、Constraints 模板化。
>
> **根因**：批处理只改了结构和 frontmatter，没有触发真正的理解加工。格式门禁检测不到"搬运 vs 理解"。
>
> **对策**：v1.5 新增理解门禁——每条 Constraint 必须有具体场景 + 可验证的失败模式。批量升级后至少抽检 2 张。

核心洞察：**格式正确是质量的必要不充分条件**。自动化可以复制结构，但无法复制理解；若把"格式全对"当作完成标准，就会批量生产出看起来完整、读起来空洞的卡片。

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **明确区分格式升级和内容升级**：
   - src_unknown
   - src_unknown

2. **每批批量升级后抽检**：
   - src_unknown
   - src_unknown
   - src_unknown
   - src_unknown

3. **v1.5 理解门禁**：
   - src_unknown
   - src_unknown
   - src_unknown

4. **建立"抽检文化"**：
   - src_unknown
   - src_unknown

5. **不要做的事**：
   - src_unknown
   - src_unknown
   - src_unknown

## 适用边界

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

| 失败模式 | 典型信号 | 根因 | 修复动作 |
|
|---|---|---|
| Claims 无具体反例 | 字段非空，但读完后回想不起任何案例 | 批量只搬结构，未做理解加工 | 为每条 Claim 补充 1 个具体场景 + 1 个反例 |
| Constraints 模板化 | 多张卡片的 Constraint 措辞雷同 | 模板填充，未针对具体知识定制 | 每条 Constraint 必须包含"当...时"+"会导致..." |
| Critique 万能化 | 批判段落放之四海而皆准 | 未针对本卡的具体假设或边界 | 至少一条 Critique 指向本卡的隐藏假设 |
| Synthesis 凑数关联 | wikilink 与主题关联微弱 | 为完成格式而硬凑关联 | 只保留能解释"为什么相关"的实质链接 |
| "格式全对"即宣布完成 | 格式门禁通过即结束流程 | 缺少理解门禁或抽检环节 | 每批升级后随机抽检 ≥2 张不同 domain 卡片 |

## 为什么值钱

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 与其他知识的关联

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
