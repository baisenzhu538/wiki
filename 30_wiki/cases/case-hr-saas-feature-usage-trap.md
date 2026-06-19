---

id: case-hr-saas-feature-usage-trap
title: HR SaaS：把“功能使用率↑续费率↑”当因果的功能堆砌陷阱
type: case
status: enriched
domain:
- yitang
- ai-saas
- business-strategy
source_refs:
- 10_raw/sources/src_20260503_52ae08ba-kdo_product_design_agent_final.md
- 10_raw/sources/src_20260503_52ae08ba-kdo_product_design_agent_final.md
- 10_raw/sources/src_20260503_52ae08ba-kdo_product_design_agent_final.md
  - src_20260613_6b939d2b-yitang-business-formula-decomposition-transcript
  - src_20260613_6edbf0af-yitang-business-formula-decomposition-notes
  - src_20260613_a8bcfd38-yitang-business-formula-decomposition-oral
tags:
- '#method/evaluation-method'
- '#content-format/case-study'
- '#domain/saas'
- '#renewal'
- '#domain/yitang'
- '#chunk-type/error-data'
created_at: '2026-06-16'
updated_at: '2026-06-16'
author: 孔阳
source_person: 孔阳
source_context: 一堂 2026-06-13 业务公式拆解培训，逻辑关系章节中的错误示范
reviewed_by: 老顽童
review_date: '2026-06-16'
confidence: 0.8
trust_level: high
related:
- '[[yt-business-formula-abc-model]]'
- '[[dk-yitang-business-formula-plus-times-trap]]'
- '[[yt-business-formula-parameter-iceberg]]'
- '[[case-saas-renewal-formula]]'
---
# HR SaaS：把“功能使用率↑续费率↑”当因果的功能堆砌陷阱

> 一堂业务公式拆解培训中的“相关≠因果”错误示范：一个年 GMV 3000 万、续费率 60% 的 HR SaaS，团队把“功能使用率提高，续费率就提高”当成因果，堆功能、加人，续费率却没上去。来源：一堂 2026-06-13 业务公式拆解培训（孔阳）。

---

## 案例背景

| 维度 | 信息 |
|---|---|
| 行业 | HR SaaS |
| 年 GMV | 3000 万 |
| 当前续费率 | 60% |
| 目标 | 续费率提升至 85% |
| 团队直觉 | 功能使用率↑续费率↑；客户成功团队人数↑续费率↑ |

---

## 错误的公式拆解

团队当时的拆解：

```
续费收入 = 老客户数 × 续费率 × 客单价
```

讨论中出现了典型的相关关系判断：

- “功能使用率和续费率是正相关，功能越多越好。”
- “客户成功团队人数和续费率是正相关，加人就行。”

这些判断的问题在于：**相关不是因果**。

实际拆解后发现：

```
功能使用率 = 核心功能使用率 × 使用深度（× 关系，漏斗）

核心功能使用率 = 功能 A 使用率 + 功能 B 使用率 + 功能 C 使用率（+ 关系，叠加）
```

如果你把“+”写成“×”，就会觉得“每一个功能都必须用起来”，实际上只要有一个核心功能用起来，续费就有保障。

同样，**加人和续费率之间也是相关非因果**——不是加人就能提升续费率，而是“客户成功体系”才导致续费率提升，加人只是其中一个动作。

---

## 正确拆解：先切分客户状态，再拆活跃客户续费率

正确的做法是：

```
续费收入 = 活跃客户续费 + 沉睡客户唤醒 + 流失客户挽回
```

再拆活跃客户续费率：

```
活跃客户续费率 = 使用深度 × 价值感知 × 切换成本（× 关系，漏斗）

使用深度 = 核心功能 A 使用率 + 核心功能 B 使用率 + 核心功能 C 使用率（+ 关系，叠加）

价值感知 = 效果数据化 + 成功案例 + 报告（+ 关系，叠加）

切换成本 = 数据沉淀 + 工作流嵌入 + 团队习惯（+ 关系，叠加）
```

拆完后，优先级立刻清晰：

| 关系 | 业务含义 | 优化动作 |
|---|---|---|
| **× 关系（漏斗）** | 使用深度、价值感知、切换成本，三者缺一不可 | 找出最弱的维度优先提升 |
| **+ 关系（叠加）** | 使用深度内部，ABC 三个功能有一个就够了 | 找到“最小可用功能”，让客户先用起来 |

---

## 关键教训

1. **不要把“功能使用率”当成续费率的直接原因**
   - 功能使用率提高可能只是客户成功体系有效的副产品。
2. **不要把“+”写成“×”**
   - 把功能使用率写成乘法关系，会要求所有功能都必须用起来，导致资源分散。
3. **加人是动作，不是原因**
   - 续费率提升的真正原因是客户成功体系，加人只是体系中的一个环节。

---

## 可迁移的校验方法

当你看到“使用率提高，续费率提高”时，先问：

1. **有没有可能两者都是“客户成功体系”的结果？**
2. **如果只提升一个核心功能使用率，续费率是否依然提升？**
3. **如果客户成功团队人数不变但流程优化，续费率是否提升？**

如果答不上来，就要画完整因果链，而不是直接按相关关系做决策。

---

## 置信度说明

- **高置信度**：相关≠因果的判断逻辑、+/× 运算符号的业务含义（直接来自培训方法论）
- **中置信度**：案例中具体数字为教学示例，未经验证
- **待复核**：HR SaaS 不同功能模块对续费率的真实因果贡献
