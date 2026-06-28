---

id: tool-strategy-four-layers
title: 战略四层结构：集团→业务单元→职能→执行
type: tool
status: enriched
author: 老顽童
confidence: 0.88
trust_level: high
language: zh-CN
domain: [strategy]
source_refs:
  - pending_archive:src_unknown - src_unknown - src_unknown - src_unknown - src_unknown - src_unknown - src_unknown - src_unknown
- src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
---
## 四层定义

| 层 | 核心问题 | 案例 |
|:---|:---|:---|
| 集团 | 做哪些业务？组合合力？ | 方特（范围经济IP复用）vs 迪士尼（规模经济） |
| 业务 | 单一市场怎么打？ | 凉白开：从高考生切入饮用水 |
| 职能 | 品牌/研发/供应链如何承接？ | 一米八八：命名即战略 |
| 执行 | 运营计划/预算/作战地图/BSC | 平衡计分卡拆到每个人 |

## Agent执行指令
```python
def audit_layers(company):
    return {layer: "缺" if not check(layer) else "有" for layer in LAYERS}
```
