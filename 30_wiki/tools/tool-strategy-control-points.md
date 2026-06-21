---
id: tool-strategy-control-points
title: 战略控制点：护城河的五锚点定位法
type: tool
status: enriched
confidence: 0.90
trust_level: high
domain:
  - strategy
source_refs:
  - 00_inbox/战略专题/冉鹏PPT截图/引擎点火20260110 战略破局（冉鹏）(1)_122_vlm_desc.md
created_at: "2026-06-21"
updated_at: "2026-06-21"
author: 老顽童（初版）→ 黄药师v2标准补强
reviewed_by: 欧阳锋
related:
  - "[[framework-strategy-business-design]]"
  - "[[framework-strategy-five-basics]]"
---

# 战略控制点：五锚点定位

> 业务设计六要素第5要素。核心问题：**你的护城河在哪？如果对手明天复制你的一切，你凭什么还活着？**

## 操作步骤

### Step 1：五锚点评估
对每个锚点评分（1-5你在哪个位置）

| 锚点 | 1分（无控制） | 3分（中等控制） | 5分（绝对控制） |
|:--|:--|:--|:--|
| **产品领先** | 无技术壁垒 | 有专利但可绕开 | 核心专利+持续研发领先 |
| **客户亲密** | 客户随时可换 | 有粘性但可替代 | 客户深度绑定（数据/习惯/生态） |
| **运营卓越** | 成本无优势 | 有规模效应 | 成本结构对手无法复制 |
| **品牌溢价** | 无品牌认知 | 有区域影响力 | 品类=品牌 |
| **生态锁定** | 单点产品 | 有互补产品线 | 切换成本极高/网络效应 |

### Step 2：选定主锚点
五锚点中选1-2个作为主控制点——"在哪个维度上做到对手无法追赶"

### Step 3：护城河压力测试
"如果我们明天投入竞争对手10倍的资源，我们能复制他们的护城河吗？"→能=你也没有护城河

## Agent 执行指令

```python
def control_point_assessment():
    anchors = ["产品领先", "客户亲密", "运营卓越", "品牌溢价", "生态锁定"]
    scores = {}
    for a in anchors:
        scores[a] = ask(f"在我们的行业，「{a}」这个锚点上，我们1-5分打几分？为什么？")
    primary = max(scores, key=scores.get)
    stress_test = ask(f"如果对手明天投入10倍资源复制我们的{primary}，他们能做到吗？")
    return {"scores": scores, "primary": primary, "压力测试": stress_test}
```

## 失败模式

| 失败 | 症状 | 修复 |
|:--|:--|:--|
| 锚点分散 | 五个都想做到最好 | 选1-2个主锚点，其他维持即可 |
| 护城河幻觉 | "我们体验好"=没有护城河 | 压力测试——10倍资源能否复制？ |

---

*老顽童初版 · v2补强 · 2026-06-21*
