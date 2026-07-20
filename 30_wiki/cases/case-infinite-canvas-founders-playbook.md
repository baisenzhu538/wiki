---
id: case-infinite-canvas-founders-playbook
title: "60镜头《创始人手册》：Claude Blog长文→Prezi式创业旅程画布"
type: case
status: draft
confidence: 0.85
trust_level: medium
domain:
  - content-production
author: 老顽童
reviewed_by: 待审
review_date: "2026-07-21"
created_at: "2026-07-21"
updated_at: "2026-07-21"
quality_labels:
  - cited
diagnostic_signals:
  - signal: "42MB单文件加载很慢"
    lens: 全内联导致文件过大
    follow_up: 后续做按需加载
  - signal: "60镜头观众跟不上"
    lens: 镜头过多停留时间不足
    follow_up: 控制在40-50镜头

source_refs:
  - "00_inbox/多模态输出/王欢：把一个想法，做成一张会移动的无限画布/王欢：把一个想法，做成一张会移动的无限画布.md"
related:
  - concept-spatial-narrative-design
  - tool-presentation-quality-gate-pipeline
  - framework-一堂-表达力火箭模型
  - framework-yitang-case-crafting-four-step
  - dk-spatial-narrative-pitfalls
---

# 60镜头《创始人手册》：Claude Blog长文→Prezi式创业旅程画布

> 一句话：王欢将一篇 Claude 官方 Blog 长文转化为 60 镜头的单文件 HTML Prezi 演示——中央标题锚点+7章节聚簇中心辐射+每章3嵌套子讲点。空间结构即内容逻辑。

---

## 技术规格

| 参数 | 值 |
|:---|:---|
| 引擎 | impress.js 2.0.0 |
| 文件格式 | 单文件 HTML，全内联 |
| 文件大小 | 42MB |
| 镜头数 | 60 |
| 空间结构 | 中央标题锚点 + 7 章节聚簇中心辐射 + 每章 3 嵌套子讲点 |

---

## 空间结构设计

```
          [中央标题锚点]
               │
    ┌────┬───┬─┼─┬───┬────┐
    Ch1  Ch2 Ch3 Ch4 Ch5 Ch6 Ch7
    │    │   │   │   │   │   │
  3子点 3子点 ... (每章3嵌套子讲点)
```

每个子讲点：有独立的钻入动画（scale up）和退回动画（scale down），在父章包围盒内。

---

## 教训

- 42MB 单文件太大→移动端加载慢。后续应做按需加载
- 60 镜头偏多→部分镜头停留时间不足。建议控制在 40-50 镜头

---

## 迭代日志

- **2026-07-21 v1.0**：来自王欢 infinite-canvas-prezi 技能文档 §7 实战示例。
