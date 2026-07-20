---
id: dk-spatial-narrative-pitfalls
title: "空间叙事四大失败模式：等距平铺/伪嵌套/横图看不清/构建者自审"
type: dk
status: draft
confidence: 0.88
trust_level: high
domain:
  - content-production
author: 老顽童
reviewed_by: 待审
review_date: "2026-07-21"
created_at: "2026-07-21"
updated_at: "2026-07-21"
quality_labels:
  - insight
diagnostic_signals:
  - signal: "全景图看起来像棋盘格"
    lens: 等距平铺——所有元素间距相同
    follow_up: 用聚簇四原则重组空间布局
  - signal: "有箭头但点进去没有钻入动画"
    lens: 伪嵌套——平铺排列+箭头假装层级
    follow_up: 检查scale比≥3+子坐标在父包围盒内

source_refs:
  - "00_inbox/多模态输出/王欢：把一个想法，做成一张会移动的无限画布/王欢：把一个想法，做成一张会移动的无限画布.md"
related:
  - concept-spatial-narrative-design
  - tool-presentation-quality-gate-pipeline
  - framework-ouyangfeng-review-methodology
  - case-infinite-canvas-founders-playbook
  - framework-一堂-表达力火箭模型
---

# 空间叙事四大失败模式

> 一句话：Prezi 最常见的失败不是"不好看"——是空间结构根本没做对。

---

## 原始表述

| # | 失败模式 | 症状 | 如何识别 | 修复 |
|:---:|:---|:---|:---|:---|
| 1 | **等距平铺** | 所有元素间距相同，没有聚簇 | 全景图看起来像棋盘格 | 用聚簇四原则重排——同主题靠近、主次分大小 |
| 2 | **伪嵌套** | 平铺排列+箭头假装层级关系 | 没有钻入动画、子元素不在父包围盒内 | 真嵌套：scale比≥3、子坐标在父内部、有钻入+退回 |
| 3 | **横图看不清** | 图片太大、横跨多个屏幕，缩放后细节丢失 | 缺少 imgfocus——没标注"这个图观众应该看哪个区域" | 给每张大图标注焦点区域坐标 |
| 4 | **构建者自审** | 自己做的东西自己审——有盲区 | review.json 的 reviewer 和 builder 是同一个人 | 信任红线：构建者禁自审、禁改 review.json |

---

## 使用场景

- Prezi/空间叙事类演示制作前自检
- 审查他人演示时的检查清单

## 操作方法

```
1. 做完全景图→对照四大失败模式逐一排查
2. 等距平铺→用聚簇四原则重组
3. 伪嵌套→检查scale比和包围盒
4. 横图→标注imgfocus
5. 自审→交给独立Agent审查
```

## 适用边界

- ✅ Prezi/impress.js 等空间叙事工具
- ❌ 传统PPT——不存在空间结构问题

## Critique

- 四大失败模式覆盖了Prezi最常见的结构问题，但不同演示工具（Keynote/PowerPoint/reveal.js）有不同的失败模式——空间叙事特有的问题不适用于传统幻灯
- 伪嵌套的判断标准（scale比≥3）依赖impress.js的缩放机制，其他工具可能需要不同的判断标准
