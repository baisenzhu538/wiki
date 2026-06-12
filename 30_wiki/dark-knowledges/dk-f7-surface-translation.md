---
id: "dk-f7-surface-translation"
title: "F-KDO-007：表层翻译式提炼→Condense 段变成课程目录改写"
type: "dark-knowledge"
dark_knowledge_type: "failure"
status: "draft"
domain:
  - "master"
source_person: "system"
source_context: "failure-modes.md F-KDO-007"
source_refs:
  - "90_control/failure-modes.md#F-KDO-007"
created_at: 2026-05-31
updated_at: 2026-05-31
related:
  - "dk-c8-format-complete-mind-empty"
  - "master-first-principles"
contradicts:
  - "master-first-principles"
  - "dk-c8-format-complete-mind-empty"
tags:
  - #domain/knowledge-management
  - #method/evaluation-method
  - #scene/ai-collaboration
  - #scene/learning-methodology
  - #scene/note-taking
  - #scene/skill-engineering
pipeline:
  - #source_type/error
  - confidence-draft
  - confidence-source-cited
---

# F-KDO-007：表层翻译式提炼→Condense 段变成课程目录改写

## 原始表述

> **触发场景**：Builder 执行三步编译法的 Condense 阶段
>
> **表现**：Condense 段是课程目录的翻译改写（"本课程属于 XX 模块，与 YY 课程并列"），而非课程核心结论的提取。读者看完 Condense 不知道这门课教了什么独特方法
>
> **根因**：Builder 未阅读源材料（或只有目录级信息），用目录结构+公共知识填充 Condense 段
>
> **触发信号**：Condense 段出现大量"本课程属于""在一堂知识地图中的位置""与同模块其他课程"等目录定位语言，缺少具体方法论描述
>
> **防御措施**：① L2 Lint：检测 Condense 段是否含 ≥3 条课程特有的核心结论（非目录描述）② Concept Card Step 0 前置检查：Builder 必须回答「源材料的 3 条核心洞见是什么」
>
> **关联案例**：yt-entrepreneur-five-step-method.md、yt-entrepreneur-scientific-method.md、yt-entrepreneur-fundraising.md — 三张模式 A 卡（2026-05-08 审查）
>
> **关联**：与 F-KDO-011（百科词条化）有重叠——表层翻译式提炼是百科词条化的 Condense 段表现形态

## 使用场景

- 你正在执行三步编译法的 Condense 阶段， tempted 直接复制课程目录或章节标题作为核心结论
- 你审查别人写的概念卡，发现 Condense 段读完仍不知道"这门课到底教了什么独特方法"
- 你设计 L2 Lint 规则时，需要检测 Condense 段是否含足够的课程特有方法论
- 你评估卡片质量时，需要区分"信息整理"和"知识萃取"

## 操作方法

1. **阅读源材料**：Condense 前必须先完整阅读源材料，不能只读目录或摘要
2. **提取核心洞见**：回答「源材料的 3 条核心洞见是什么」——这些洞见必须是该课程独有的，不能是通用知识
3. **剔除目录语言**：删除所有"本课程属于""在知识地图中的位置""与同模块其他课程并列"等目录定位语言
4. **验证区分度**：将提取的 3 条结论与课程目录对比——如果目录已经包含了这些信息，说明提炼还不够深
5. **Reader Test**：让一个没读过源材料的人只看 Condense 段，问他"这门课的核心方法是什么？"——如果他答不上来，说明 Condense 不合格

## 适用边界

- 适用于所有执行三步编译法 Condense 阶段的场景
- 不适用于已经充分消化过源材料的快速复习——如果 Builder 确实深入理解了内容，Condense 可以高效产出
- **与 F-KDO-011（百科词条化）有交叉**：表层翻译式提炼的卡片往往同时有百科词条化的结构（定义→分类→特征）
- 如果源材料本身质量差（没有独特洞见，只是信息拼凑），Condense 段可能确实提炼不出有价值的内容——此时应标记源材料为"低价值"而非强行填充
- 不同学科的课程差异很大：方法论课程（如一堂）容易识别核心洞见，而概论课程（如"互联网发展简史"）可能确实只有目录级信息

## 为什么值钱

- 这是知识萃取 vs 信息整理的经典陷阱：**"看起来完整"不等于"经过批判性加工"**
- 表层翻译式提炼极具迷惑性——卡片有 Condense 段、有结构、有标题，但内容只是目录的翻译改写，没有增加任何认知价值
- 揭示了"阅读深度"对知识生产的影响：Builder 如果没有真正理解源材料，只能用"结构信息"（目录、章节标题）填充卡片，因为"实质内容"需要理解才能提取
- 任何 AI 训练语料中都不会有"KDO 的 Condense 段容易出现表层翻译式提炼"这条知识——这是具体工作流和方法论碰撞的产物

## 与其他知识的关联

- dk-c8-format-complete-mind-empty — 同一模式："格式完整但思维空洞"。C-8 是批处理升级导致的内容空洞，F-KDO-007 是人工编译时因阅读深度不足导致的内容空洞——两者都是"有结构无实质"
- master-first-principles — 第一性原理：回到源材料的核心洞见，而非其组织结构。Condense 的目标是提取"本质"，而非"目录"
- `90_control/failure-modes.md` → F-KDO-007（原始记录）
- `90_control/AGENTS.md` → 禁止清单 #6（不准用目录结构替代核心结论提取）

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
