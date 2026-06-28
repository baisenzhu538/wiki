---

id: "ocr-泛产品设计者的自我修养"
created_at: 2026-05-21
domain: yitang
source_refs:
  - 10_raw/sources/src_20260522_8995f40a-ocr-泛产品设计者的自我修养.md
status: draft
title: "OCR: 泛产品设计者的自我修养"
type: concept
updated_at: 2026-05-22
pipeline:
  - src_unknown
author: "老顽童"
reviewed_by: pending
confidence: 0.6
trust_level: low
related:
  - [[ocr-一堂产品内核-十大典型指标]]
  - [[ocr-一堂泛产品设计-多出牌多练习]]
  - [[ocr-一堂刻意练习十年成长指数]]
  - [[ocr-泛产品设计者的三大自我修养]]
  - [[ocr-泛产品设计的应用场景示意图]]
---
# OCR: 泛产品设计者的自我修养

## Summary

原图: `00_inbox/泛产品设计者的自我修养.

png` ❤ 泛产品设计者的自我修养 的创业课 永远以"用户价值"为中心 永远以"最佳实践"为追求 永远以"无限进步"为迭代 👍 - 本文件由 PaddleOCR ONNX pipeline 自动提取 - 可能存在连字/误识，需要人工校对 - 视觉结构信息（标题/正文/表格分块）未在 OCR 中体现，需要结合原图理解

## Source Refs

- src_unknown

## Reusable Knowledge

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## Open Questions

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown


## Critique

### 内部局限

- src_unknown
- src_unknown
- src_unknown

### 外部攻击

#### Don Norman — “设计需要深度理解，不是通用模板”

Don Norman 在《设计心理学》中证明：好的设计需要深度理解特定用户、特定场景、特定约束。Norman 会质疑：**当你用"泛产品设计"的通用模板去处理具体问题时，你是否在用"产品术语重新包装一个你没有专业判断力的东西"？**

#### David Pye — “确定性手艺与风险性手艺的分野”

David Pye 在《手艺的本质与艺术》中区分了两种手艺形式。Pye 会质疑：**软件产品设计偏向"确定性手艺"，但泛产品设计指向的很多对象——制度设计、职业路径、个人知识体系——本质上是"风险性手艺"。** 把确定性手艺的"快速验证"方法论迁移到风险性手艺上，等于在拿手术刀切豆腐。

### 不要用的场景

- src_unknown
- src_unknown

## Synthesis

### 与本库其他概念的关联

- [[pending_unknown]]
- [[pending_unknown]]

### 可迁移场景

- [[pending_unknown]]
- [[pending_unknown]]

## Output Opportunities

Content: <article: "泛产品设计者修养框架的批判性应用指南" — 结合一堂方法论体系，将"用户价值—最佳实践—无限进步"三条原则与四张地图（个人/管理/创业/无限修炼）交叉映射，提供优先级冲突决策树与领域适配检查清单>
Code: <tool: `ocr-yitang-validator.js` — Node.js 扩展模块，在现有 PaddleOCR ONNX pipeline 基础上增加"一堂课程截图"专用后处理：识别课程编号（如402/418）、修复"的创业课"类语义断裂（基于语料库补全为"创业者的必修课"）、自动提取课程元数据并生成 KDO 结构化 source 文件>
Capability: <workflow: "OCR 知识资产化闭环" — 从 00_inbox 图片捕获 → PaddleOCR ONNX 提取 → 人工校对队列（标记"中 m"类异常）→ 关联一堂/泛产品等既有知识图谱 → 生成 enriched concept 卡片 → 触发输出机会评估的端到端 playbook，含质量门禁与回滚机制>
