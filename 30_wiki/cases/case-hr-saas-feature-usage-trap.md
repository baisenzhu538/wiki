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
- pending_archive:src_20260613_6b939d2b-yitang-business-formula-decomposition-transcript
- pending_archive:src_20260613_6edbf0af-yitang-business-formula-decomposition-notes
- pending_archive:src_20260613_a8bcfd38-yitang-business-formula-decomposition-oral
- pending_archive:src_20260613_6b939d2b-yitang-business-formula-decomposition-transcript
- pending_archive:src_20260613_6edbf0af-yitang-business-formula-decomposition-notes
- pending_archive:src_20260613_a8bcfd38-yitang-business-formula-decomposition-oral
tags:





created_at: '2026-06-16'
updated_at: 2026-06-28
author: 孔阳
source_person: 孔阳
source_context: 一堂 2026-06-13 业务公式拆解培训，逻辑关系章节中的错误示范
reviewed_by: 老顽童
review_notes: 历史遗留，写审分离规则确立前的早期卡片。有效性由月度抽检覆盖。
review_date: '2026-06-16'
confidence: 0.8
trust_level: high
related:
  - "[[yitang-domain-digest]]"
  - "[[private-domain-saas-sales-funnel]]"
  - "[[case-yitang-xujian-invoice-saas-channel]]"
  - "[[tool-水水-识别自证预言陷阱]]"
  - "[[case-saas-renewal-formula]]"
  - "[[tool-水水-识别数据折磨陷阱]]"
  - "[[case-truman-ai-skill-self-packaging]]"
---

# HR SaaS：把“功能使用率↑续费率↑”当因果的功能堆砌陷阱

> 一堂业务公式拆解培训中的“相关≠因果”错误示范：一个年 GMV 3000 万、续费率 60% 的 HR SaaS，团队把“功能使用率提高，续费率就提高”当成因果，堆功能、加人，续费率却没上去。来源：一堂 2026-06-13 业务公式拆解培训（孔阳）。



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

- src_unknown
- src_unknown

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
   - src_unknown
2. **不要把“+”写成“×”**
   - src_unknown
3. **加人是动作，不是原因**
   - src_unknown

---

## 可迁移的校验方法

当你看到“使用率提高，续费率提高”时，先问：

1. **有没有可能两者都是“客户成功体系”的结果？**
2. **如果只提升一个核心功能使用率，续费率是否依然提升？**
3. **如果客户成功团队人数不变但流程优化，续费率是否提升？**

如果答不上来，就要画完整因果链，而不是直接按相关关系做决策。

---

## 置信度说明

- src_unknown
- src_unknown
- src_unknown

## 关键证据

| 证据点 | 来源 | 可检验性 |
|:---|:---|:---|
| src_unknown | src_unknown | src_unknown |
| src_unknown | src_unknown | src_unknown |

## 可迁移场景

- src_unknown（待补充：这个案例的经验可以迁移到哪些场景）

## 教训

- src_unknown（待补充：什么时候应该学这个案例（正面））

## 失败模式

- src_unknown（待补充：常见的踩坑方式和避免方法（反面））
