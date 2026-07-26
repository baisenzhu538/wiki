---
id: tool-strategy-map
title: 战略地图——公司/各BU/业务单元的战略蓝图模板
type: tool
status: reviewed
confidence: 0.88
trust_level: high
domain: strategy
source_refs:
- 00_inbox/战略专题/冉鹏PPT截图/引擎点火20260110 战略破局（冉鹏）(1)_142_vlm_desc.md
created_at: '2026-06-22'
updated_at: '2026-06-29'
author: 黄药师（从 PPT _142 提取）
reviewed_by: 欧阳锋
related:
- '[[strategy-domain-digest]]'
- '[[anthropic-官方发布创始人手册打造-ai-原生初创公司]]'
- '[[yc-放出一套ai-native-公司组织方法论直接把公司当操作系统来设计中层管理变成了-markdown]]'
- '[[pending_unknown]]'
- '[[pending_unknown]]'
- tool-strategy-pareto
tags:
- audience:executor
- scene:execution
- skill-level:advanced
---
# 战略地图

> PPT _142。冉鹏方法论中用于公司/各 BU/业务单元的标准化战略蓝图。不是"目标拆解"——是"每个业务单元的战略一致性检查"。

## 模板

| 维度 | 业务单元 A | 业务单元 B | 业务单元 C |
|:--|:--|:--|:--|
| **使命/愿景** | | | |
| **客户选择** | | | |
| **价值主张** | | | |
| **战略控制点** | | | |
| **盈利模式** | | | |
| **关键举措（90天）** | | | |
| **所需资源** | | | |
| **风险/障碍** | | | |

## 使用方式

1. 每个业务单元独立填写——不自查，填写时不知道其他 BU 的内容
2. 汇总对比——找"各 BU 战略是否对齐公司整体方向"
3. 识别冲突——两个 BU 的客户选择重叠？资源竞争？
4. 识别空白——哪个战略方向没有任何 BU 覆盖？

## 和六要素工作坊的区别

| 六要素×三步骤 | 战略地图 |
|:--|:--|
| 单个业务设计 | 多个 BU 对齐 |
| 深度（现有→期望→挑战） | 广度（跨 BU 一致性） |
| 工作坊用 | 战略会议用 |

## Agent 执行指令

```python
def strategy_map_alignment(business_units: list):
    """生成多BU战略地图并检测对齐问题"""
    matrix = {}
    for bu in business_units:
        matrix[bu] = {
            "客户选择": ask(f"{bu}: 谁是最重要的客户？"),
            "价值主张": ask(f"{bu}: 提供什么独特价值？"),
            "战略控制点": ask(f"{bu}: 护城河在哪？"),
            "盈利模式": ask(f"{bu}: 怎么赚钱？"),
            "90天关键举措": ask(f"{bu}: 未来90天最重要的3件事？"),
        }
    # 检测冲突：两个BU是否有重叠的客户群？
    conflicts = detect_overlaps(matrix)
    # 检测空白：公司战略方向中有没有被任何BU覆盖的？
    gaps = detect_gaps(matrix, corporate_strategy)
    return matrix, conflicts, gaps
```

---

*黄药师 · 2026-06-22 · 从 PPT _142 提取*

## 目的

> 待补充：这个工具解决什么问题？适用于什么场景？

## 操作步骤

1. **步骤一**：待补充
2. **步骤二**：待补充
3. **步骤三**：待补充

## 不要用的场景

> 待补充：什么情况下这个工具效果有限或不应该使用？

## 质疑

> 待补充：这个工具的内在局限是什么？外部反对者会怎么批评？

**Robert Kaplan** 可能会质疑：这个工具依赖的 **因果关系链、指标选择、战略假设、动态反馈** 是否已经被充分验证？

- 战略地图的因果链往往是假设而非事实，需要数据验证。
- 指标选择若与真实战略目标脱节，地图会变成形式主义工具。

- 使用前应明确本工具的 **具体假设**、适用 **边界**、潜在 **反例** 和隐含 **前提**，避免把模板输出直接当成战略结论。
