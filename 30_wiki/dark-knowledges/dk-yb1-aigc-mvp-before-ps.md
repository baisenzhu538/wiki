---

id: dk-yb1-aigc-mvp-before-ps
title: 设计师AIGC工作流：先跑MVP再开PS
type: dk
dark_knowledge_type: workflow
status: enriched
domain:
- design
- ai-collaboration
source_person: 月白
source_context: '口述稿: AI设计-AI设计基础01'
source_refs:
- src_unknown
created_at: 2026-06-04
updated_at: '2026-06-19'
related:
  - "[[ai-collaboration-domain-digest]]"
  - "[[tool-半肥猫-课程Skill化的八步工作流]]"
  - "[[yt-panproduct-execution-low-cost-mvp]]"
  - "[[tool-月白-AIGC设计作业复盘法]]"
  - "[[tool-月白-设计师AI工具习惯切换]]"
  - "[[tool-月白-设计师AI资产四类型沉淀]]"
  - "[[tool-月白-用AIGC做设计专家批评复盘]]"
  - "[[tool-马易-工作流拆解找场景]]"
  - "[[tool-月白-设计项目MVP拆解法]]"
  - "[[tool-月白-AIGC反向拆解法]]"
  - "[[tool-月白-AIGC人群画像驱动详情页规划]]"
  - "[[tool-月白-PPT全AI生成工作流]]"
  - "[[yt-lean-daily-chemical-mvp]]"
  - "[[case-yitang-mvp-reward-interview-waste]]"
pipeline:
- src_unknown
author: 月白
reviewed_by: 欧阳锋
confidence: 0.85
trust_level: medium
diagnostic_signals:
- signal: src_unknown
  framework_lens: 肌肉记忆陷阱——传统工具的使用习惯阻碍AIGC工作流落地
  follow_up_question: 最近3次设计任务中，有几次是先收集参考图跑AI验证方向，再打开传统工具的？比例低于1/3说明工作流未转变。
- signal: src_unknown
  framework_lens: 改稿成本错位——方向级问题应该在MVP阶段解决，而非在执行层反复修改
  follow_up_question: 统计最近改稿的原因分布：方向调整占多少？执行细节占多少？前者的MVP阶段本应拦截。# 设计师AIGC工作流：先跑MVP再开PS

---

## 原始表述

> 打开ps就开始做，不能这样打开ps就开始做。你MVP先建起来先跑，他跟审美没有关系，你做这些都不需要审美，你找图不需要审美，你先找找到了，然后捞风格提示词，风格提示词捞完了之后再让AIGC跑，先确认方向再开始动作。

## 使用场景

传统设计背景、习惯直接打开PS/AI开始动手的设计师，在接入AIGC工具（Midjourney/SD等）时，需要转变工作流。

## 操作方法

1. **禁止第一步打开PS**
2. 先找参考图（无需审美判断，大量收集即可）
3. 从参考图中"捞"出风格提示词（prompt）
4. 用AIGC快速跑MVP验证方向
5. 方向确认后，再进入传统设计工具执行

## 适用边界

| 边界 | 说明 |
|:
--|:-----|
| **不适用纯传统手工设计项目** | 无AIGC参与的场景不需要此工作流。 |
| **不适用于审美本身就是核心交付物的阶段** | 如最终视觉精修，此时需要审美判断主导。 |
| **"不需要审美"仅指前期探索阶段** | 非全程放弃审美——方向确认后，审美执行仍然关键。 |
| **需要团队有AIGC工具使用基础** | 如果设计师还不会用Midjourney/SD/ComfyUI，先补齐工具能力。 |

| 失败模式 | 典型症状 | 修复方法 |
|---|---|---|
| 跳过MVP直接执行 | 打开PS做了半天，被推翻后全部重做 | 强制规则：任何设计任务的前30分钟只能用来找参考图和跑AI方向验证 |
| MVP跑太多方向不收敛 | 跑了20个方向仍不确定，拖延决策 | 设定MVP时间盒（如2小时），到点必须选1-2个方向进入执行 |
| 找参考图时陷入审美判断 | "这张图太丑了不参考"——用审美过滤了本应开放的参考池 | 找图阶段用数量替代质量，目标：30分钟内收集50+张参考 |
| 方向确认后跳过传统精修 | AI产出直接交付，细节粗糙 | 方向确认后必须回到传统工具做最终精修和品质控制 |

## 行动 Checklist

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 为什么值钱

公开语料中充斥"设计师要拥抱AI"的泛论，但极少有人明确指出"打开PS就做"这个具体肌肉记忆是最大障碍，以及"找图不需要审美"这种反直觉的操作顺序——传统设计教育强调每一步都要有审美判断，而AIGC时代需要先分离"方向验证"与"审美执行"。

## 与其他知识的关联

- src_unknown
- src_unknown
- src_unknown
