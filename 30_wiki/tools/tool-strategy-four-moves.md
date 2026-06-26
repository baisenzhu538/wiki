---

id: tool-strategy-four-moves
title: 战略四招法：小李飞刀/分筋错骨手/葵花点穴手/乾坤大挪移
type: tool
status: enriched
author: 老顽童
confidence: 0.85
trust_level: high
language: zh-CN
domain: [strategy]
source_refs:
- 00_inbox/战略专题/冉鹏战略课逐字稿_ocr.md §37-40
related:
  - '[[concept-strategy-framework-landscape]]'
  - '[[tool-strategy-gap-analysis]]'
  - '[[framework-multi-agent-research-architecture]]'
  - '[[tool-strategy-four-layers]]'
  - '[[tool-strategy-three-horizons]]'
  - "[[framework-strategy-six-stages]]"
  - "[[tool-strategy-nine-problems]]"
---
## 四招

| 招式 | 核心 | 案例 |
|:---|:---|:---|
| **小李飞刀**（先发优势） | 进入新兴业务进化周期的适者生存期或物种爆发期 | — |
| **分筋错骨手**（逆向投资） | 与市场常识反向而行 | 李嘉诚下行周期并购；小熊电器定位年轻单身男性；爱德华琼斯每镇一人 |
| **葵花点穴手**（细分垄断） | 选对手不防守的点往死里打 | 凉白开高考生切入2年30亿；一米八八奶粉0→20亿 |
| **乾坤大挪移**（底层技术迁移） | 核心技术转到新赛道存活 | 乐凯胶卷→光学薄膜→新赛道 |

## Agent执行指令
```python
def match_move(company):
    if company.stage == "初创": return "葵花点穴手（细分垄断）"
    if company.stage == "吃撑": return "乾坤大挪移（技术迁移）"
    if market.sentiment == "悲观": return "分筋错骨手（逆向）"
```
