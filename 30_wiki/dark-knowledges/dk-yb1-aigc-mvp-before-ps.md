---

id: dk-yb1-aigc-mvp-before-ps
title: 设计师AIGC工作流：先跑MVP再开PS
type: dark-knowledge
dark_knowledge_type: workflow
status: enriched
domain:
- design
- ai-collaboration
source_person: 月白
source_context: '口述稿: AI设计-AI设计基础01'
source_refs:
- 10_raw/sources/src_20260604_design-ai-basics-01.md
created_at: 2026-06-04
updated_at: '2026-06-19'
related:
  - '[[dk-yb31-style-first-controlnet]]'
  - '[[dk-yb27-pseudo-layer-evasion]]'
  - '[[dk-yb6-midjourney-chinese-text-fix]]'
  - '[[dk-yb23-ai-pre-screen-three-minutes]]'
  - '[[dk-yb5-style-asset-archive]]'
- '[[dk-yb5-style-asset-archive]]'
- '[[dk-yb8-file-naming-eight-elements]]'
- '[[dk-yb7-design-demand-80-10-10]]'
pipeline:
- confidence-source-cited
author: 月白
reviewed_by: 欧阳锋
confidence: 0.85
trust_level: medium
diagnostic_signals:
- signal: 设计师接到需求后第一反应是打开PS/AI开始做，跳过方向验证直接进入执行
  framework_lens: 肌肉记忆陷阱——传统工具的使用习惯阻碍AIGC工作流落地
  follow_up_question: 最近3次设计任务中，有几次是先收集参考图跑AI验证方向，再打开传统工具的？比例低于1/3说明工作流未转变。
- signal: 设计产出被反复推翻，每次改稿都在PS里重新做，而不是回到提示词/方向层调整
  framework_lens: 改稿成本错位——方向级问题应该在MVP阶段解决，而非在执行层反复修改
  follow_up_question: 统计最近改稿的原因分布：方向调整占多少？执行细节占多少？前者的MVP阶段本应拦截。
---
# 设计师AIGC工作流：先跑MVP再开PS

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
|:-----|:-----|
| **不适用纯传统手工设计项目** | 无AIGC参与的场景不需要此工作流。 |
| **不适用于审美本身就是核心交付物的阶段** | 如最终视觉精修，此时需要审美判断主导。 |
| **"不需要审美"仅指前期探索阶段** | 非全程放弃审美——方向确认后，审美执行仍然关键。 |
| **需要团队有AIGC工具使用基础** | 如果设计师还不会用Midjourney/SD/ComfyUI，先补齐工具能力。 |

## 常见失败模式

| 失败模式 | 典型症状 | 修复方法 |
|---|---|---|
| 跳过MVP直接执行 | 打开PS做了半天，被推翻后全部重做 | 强制规则：任何设计任务的前30分钟只能用来找参考图和跑AI方向验证 |
| MVP跑太多方向不收敛 | 跑了20个方向仍不确定，拖延决策 | 设定MVP时间盒（如2小时），到点必须选1-2个方向进入执行 |
| 找参考图时陷入审美判断 | "这张图太丑了不参考"——用审美过滤了本应开放的参考池 | 找图阶段用数量替代质量，目标：30分钟内收集50+张参考 |
| 方向确认后跳过传统精修 | AI产出直接交付，细节粗糙 | 方向确认后必须回到传统工具做最终精修和品质控制 |

## 行动 Checklist

- [ ] 接到设计需求后，是否先打开了参考图收集工具而非PS？
- [ ] 是否在30分钟内收集了足够的参考图（≥30张）？
- [ ] 是否用AIGC跑出了至少2个方向供比较？
- [ ] 方向确认的依据是什么？是否和需求方对齐过？
- [ ] 进入PS前，是否已明确"这次执行只需要做哪些细节调整"？

## 为什么值钱

公开语料中充斥"设计师要拥抱AI"的泛论，但极少有人明确指出"打开PS就做"这个具体肌肉记忆是最大障碍，以及"找图不需要审美"这种反直觉的操作顺序——传统设计教育强调每一步都要有审美判断，而AIGC时代需要先分离"方向验证"与"审美执行"。

## 与其他知识的关联

- [[dk-yb5-style-asset-archive]] — AI绘图降本的前提：风格资产工程化归档
- [[dk-yb8-file-naming-eight-elements]] — 文件命名八要素体系
- dk-yb15-prompt-length-constraint — 提示词长度即约束强度
