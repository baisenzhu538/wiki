---
id: tool-presentation-quality-gate-pipeline
title: "演示产线双防线质量控制：四道机械闸门 + 七维独立终审"
type: tool
status: draft
confidence: 0.90
trust_level: high
domain:
  - content-production
author: 老顽童
reviewed_by: 待审
review_date: "2026-07-21"
created_at: "2026-07-21"
updated_at: "2026-07-21"
quality_labels:
  - actionable
source_refs:
  - "00_inbox/多模态输出/王欢：把一个想法，做成一张会移动的无限画布/王欢：把一个想法，做成一张会移动的无限画布.md"
related:
  - concept-spatial-narrative-design
  - framework-ouyangfeng-review-methodology
  - framework-一堂-基本功-四字诀拆建推练
  - dk-spatial-narrative-pitfalls
  - case-infinite-canvas-founders-playbook
---

# 演示产线双防线质量控制

> 一句话：王欢的无限画布生产管线有两道防线——四道机械闸门（自动化拦截）+ 七维独立终审（人工Agent审查）。与欧阳锋审查方法论完全同构：独立审查、多维检查、禁止自审。

---

## 第一道防线：四道机械闸门

| 闸门 | 检查阶段 | 拦截什么 | 不合格处理 |
|:---|:---|:---|:---|
| **Plan** | 结构规划后 | 空间结构不合理（等距平铺/伪嵌套） | rc≠0 → 打回重做 |
| **Media** | 素材准备后 | 图片缺失/分辨率不足/格式不支持 | rc≠0 → 补充素材 |
| **Build** | HTML生成后 | impress.js语法错误/镜头路径断链 | rc≠0 → 修复后重跑 |
| **Final** | 全流程后 | 总检查：前三个闸门全部通过+终审通过 | 任一未过→降级 |

---

## 第二道防线：七维独立终审

| 维度 | 检查问题 | 独立Agent |
|:---|:---|:---|
| R1 结构完整性 | 内容有没有逻辑缺口？章节数对不对？ | Agent-Structure |
| R2 空间设计 | 四种结构选择是否正确？聚簇四原则是否满足？ | Agent-Spatial |
| R3 镜头设计 | 每个镜头路径是否自然？停留时长合理？ | Agent-Camera |
| R4 视觉一致性 | 颜色/字体/动画风格统一？ | Agent-Visual |
| R5 内容准确性 | 有没有事实错误？数据来源标注？ | Agent-Content |
| R6 性能 | 加载时间？移动端兼容？ | Agent-Perf |
| R7 整体印象 | 从头播一遍，有没有"卡住"的感觉？ | Agent-Review |

---

## 信任红线

| 规则 | 为什么 |
|:---|:---|
| **构建者禁止自审** | 自己做的东西有盲区——必须由独立 Agent 审查 |
| **禁止修改 review.json** | 审查结果是事实，不是可以"协商"的 |
| **降级铁律** | 2-3 次失败→立即降级为静态PPT，不再追求Prezi |

---

## 与欧阳锋审查方法论的同构

| 王欢的双防线 | 欧阳锋审查方法论 |
|:---|:---|
| 四道闸门（机械拦截） | 分层阻断（不同层级拦截不同类型问题） |
| 七维独立终审 | 五轴审查+魔鬼代言人 |
| 信任红线（禁自审） | 写审分离（老顽童生产、欧阳锋终审） |

---

## 迭代日志

- **2026-07-21 v1.0**：来自王欢 infinite-canvas-prezi 技能文档。
