---
id: tool-strategy-value-capture
title: 价值获取：盈利模式八问——从价值主张到怎么赚钱
type: tool
status: enriched
confidence: 0.90
trust_level: high
domain:
  - strategy
source_refs:
  - 00_inbox/战略专题/冉鹏PPT截图/引擎点火20260110 战略破局（冉鹏）(1)_115_vlm_desc.md
created_at: "2026-06-21"
updated_at: "2026-06-21"
author: 老顽童（初版）→ 黄药师v2标准补强
reviewed_by: 欧阳锋
related:
  - "[[framework-strategy-business-design]]"
  - "[[tool-strategy-value-proposition]]"
---

# 价值获取：盈利模式八问

> 业务设计六要素第3要素。核心问题：**你的价值主张很好——但你怎么从中赚钱？**

## 操作步骤：八问A-H

| 问 | 内容 | 无法回答=危险信号 |
|:--|:--|:--|
| A 产品 | 核心产品/服务怎么定义？ | 产品边界模糊=什么都能做=什么都做不好 |
| B 用户 | 谁来买单？决策链是什么？ | 使用者和付费者不是同一人 |
| C 渠道 | 通过什么渠道触达付费者？ | 渠道成本超过毛利 |
| D 创新 | 技术/模式有什么不同？ | "我们更努力"不是创新 |
| E 交付 | 怎么保证交付质量？ | 交付不稳=口碑崩盘 |
| F 财务 | 收入模型+成本结构 | 说不清单位经济模型 |
| G 壁垒 | 竞争对手为什么不能复制？ | "先发优势"=没有壁垒 |
| H 替代 | 如果这个模式不行，备选？ | 只有一条路=没有Plan B |

## Agent 执行指令

```python
def value_capture_8q(proposition: str, customer: str):
    questions = ["产品", "用户", "渠道", "创新", "交付", "财务", "壁垒", "替代"]
    answers = {}
    for q in questions:
        answers[q] = ask(f"基于价值主张「{proposition}」和目标客户「{customer}」，{q}维度的答案是什么？")
    red_flags = [q for q in questions if "说不清" in answers[q].lower() or len(answers[q]) < 20]
    return {"answers": answers, "red_flags": red_flags}
```

## 失败模式

| 失败 | 症状 | 修复 |
|:--|:--|:--|
| 跳过F（财务） | 只说了收入不说成本 | 强制做单位经济模型——每单赚多少 |
| G（壁垒）空洞 | "先发优势""品牌溢价" | 追问：如果腾讯/字节明天进场，你凭什么不输？ |

---

*老顽童初版 · v2补强 · 2026-06-21*
