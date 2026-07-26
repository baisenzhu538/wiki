---
id: tool-月白-替换大法改图
title: 技能：替换大法改图
type: tool
status: draft
domain: design- design
source_person: 月白
source_context: AI设计师实操 （原 legacy，已从 title/context/filename 推断为 src_20260522_38173b48）
source_refs:
- 10_raw/sources/src_20260522_38173b48-design-ai-image-generation.md
wiki_refs: null
definition_of_done:
- src_unknown
- src_unknown
- src_unknown
tools_required: null
prerequisite_skills: null
created_at: 2026-06-07
updated_at: '2026-06-16'
pipeline:
- src_unknown
author: 月白
reviewed_by: pending
confidence: 0.6
trust_level: low
related:
- '[[tool-月白-多窗口并行工作法]]'
- '[[tool-月白-AI改图指令精细化]]'
- '[[tool-月白-批量生成多视角素材]]'
- '[[tool-月白-竞品图精益替换法]]'
- '[[tool-月白-AIGC橱窗陈列设计流程]]'
- '[[tool-月白-AI精准替换产品技巧]]'
tags:
- audience:executor
- scene:execution
- skill-level:beginner
---

# 技能：替换大法改图

## 原始表述

替换大法改图是月白在AI设计师实操中提出的实操方法。

## 操作步骤

1. 确定需要替换的维度（位置/风格/内容/视角）
2. 准备参考图A
3. 明确目标需求并整理提示词
4. 将参考图+提示词提交给AIGC
5. 迭代调整直至满意

## 适用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 不适用场景

- src_unknown
- src_unknown

## 工具/环境

- src_unknown

## 为什么有效

降低描述难度，通过参考图+明确指令让AI执行替换，比纯文字描述更精准可控

## 关联技能

- src_unknown

## 来源

- src_unknown

## Feedback Path

- src_unknown

## 目的

解决AI改图时"纯文字描述不准、改不到痛点"的沟通难题。直接用自然语言描述"把左边的杯子换成花瓶"往往效果不可控，因为AI对空间位置的文字描述理解有限。方法通过提供参考图+明确替换指令的方式，将"描述要改成什么样"转化为"照着这张图的这个元素改"，大幅降低沟通难度。适用于需局部替换图片元素的场景（产品替换、背景更换、道具变更）、无PS技能的设计小白、需要快速迭代多个版本的电商设计等场景。核心适用前提是替换内容与原图风格、光照一致，否则易出现合成感。

## 质疑

- **具体假设**：该工具假设结构化方法论本身能产生正确结论，但方法论只是框架——结论质量取决于输入数据的质量和执行者的判断力。
- **边界**：在数据稀缺或快速变化的新兴领域，已有经验框架可能完全失效——工具的有效性高度依赖场景的稳定性。
- **反例**：一个团队完整执行了所有步骤，产出了漂亮的文档，但核心假设从一开始就是错的——流程的完整性掩盖了判断的缺陷。
- **前提**：使用者已具备该领域的基础认知，能正确理解和执行工具规则，且数据来源具有代表性。

**Hany Farid**（数字图像取证专家）会指出：AI替换图像的逼真度和一致性无法保证。光照方向、阴影、透视、材质反射等物理属性在不同元素间难以一致，AI生成的结果在专业审查下极易暴露破绽——这在商业印刷品和法律证据场景中不可接受。方法夸大了"替换"的可靠性，实际成功率取决于场景复杂度和模型版本。

**Philipp Schmitt**（计算摄影学研究者）会批评：参考图指导的方法引入了版权灰色地带。当参考图来自第三方来源（如Pinterest、商业图库），AI在转换过程中可能实质性地复制了原图的创作元素，这在商业使用场景中构成潜在的衍生作品风险。方法没有提示用户检查参考图的版权和使用许可。
