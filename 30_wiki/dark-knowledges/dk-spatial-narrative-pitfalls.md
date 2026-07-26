---
id: dk-spatial-narrative-pitfalls
title: 空间叙事四大失败模式：等距平铺/伪嵌套/横图看不清/构建者自审
type: dk
status: reviewed
confidence: 0.88
trust_level: high
domain:
- content-production
author: 老顽童
reviewed_by: 欧阳锋
review_date: '2026-07-21'
grade: B+
created_at: '2026-07-21'
updated_at: '2026-07-21'
quality_labels:
- insight
diagnostic_signals:
- signal: 全景图看起来像棋盘格
  lens: 等距平铺——所有元素间距相同
  follow_up: 用聚簇四原则重组空间布局
- signal: 有箭头但点进去没有钻入动画
  lens: 伪嵌套——平铺排列+箭头假装层级
  follow_up: 检查scale比≥3+子坐标在父包围盒内
source_refs:
- 00_inbox/多模态输出/王欢：把一个想法，做成一张会移动的无限画布/王欢：把一个想法，做成一张会移动的无限画布.md L48-L51
- 00_inbox/多模态输出/王欢：把一个想法，做成一张会移动的无限画布/王欢：把一个想法，做成一张会移动的无限画布.md L111-L113
- 00_inbox/多模态输出/王欢：把一个想法，做成一张会移动的无限画布/王欢：把一个想法，做成一张会移动的无限画布.md L139-L143
- 00_inbox/多模态输出/王欢：把一个想法，做成一张会移动的无限画布/王欢：把一个想法，做成一张会移动的无限画布.md L163-L170
- 00_inbox/多模态输出/王欢：把一个想法，做成一张会移动的无限画布/王欢：把一个想法，做成一张会移动的无限画布.md L269-L274
related:
- concept-spatial-narrative-design
- tool-presentation-quality-gate-pipeline
- framework-ouyangfeng-review-methodology
- case-infinite-canvas-founders-playbook
- framework-一堂-表达力火箭模型
tags:
- audience:executor
- scene:reference
- skill-level:advanced
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

## 为什么值钱

1. **反直觉**：大多数Prezi初学者以为"会动=好"，失败后归因于"我不够有设计感"——实际上四个失败模式全是结构性问题，有明确的检测方法和修复步骤。
2. **量化了"经验直觉"**：等距平铺vs聚簇、伪嵌套vs真嵌套——这些原本是"老手一眼能看出来的问题"，现在变成了可逐条检查的清单。scale比≥3、子坐标在父包围盒内——都是可测量、可程序化检查的。
3. **与欧阳锋审查方法论同构**：构建者自审是最隐蔽的失败模式——自己做的东西自己审，盲区永远存在。这个失败模式在代码审查中也高频出现（老顽童返工记录可证），跨域价值极高。

## 与其他知识的关联

- `concept-spatial-narrative-design`：四大失败模式是空间设计概念的反面教材——理解"怎么做对"之后，必须知道"怎么做错"
- `tool-presentation-quality-gate-pipeline`：四大失败模式中的#1-#3由机械闸门自动拦截，#4由信任红线拦截
- `framework-ouyangfeng-review-methodology`：构建者自审的失败模式与欧阳锋"写审分离"完全同构——不同领域、同一个根因
- `case-infinite-canvas-founders-playbook`：《创始人手册》案例中60镜头避免了等距平铺（中心辐射+嵌套），是正向对比
- `framework-一堂-表达力火箭模型`：空间叙事服务于表达递进——空间结构错了，表达力火箭就飞不起来
