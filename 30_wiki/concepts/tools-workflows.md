---


id: tools-workflows
created_at: 2026-05-21
domain:
  - healthcare
source_refs:
- src_20260522_9d322e81-tools-workflows
status: enriched
title: "Tools Workflows"
type: concept
updated_at: 2026-05-22
pipeline:
  - confidence-source-cited
  - confidence-verified-by-case
author: unknown
reviewed_by: "欧阳锋"
confidence: 0.8
trust_level: medium
related:
  - '[[ocr-一堂-地图-管理地图_conv]]'
  - '[[ocr-微信图片_20260507004746_32_32]]'
  - '[[ocr-微信图片_20260507004801_37_32]]'
  - '[[ocr-screenshot1]]'
  - '[[ocr-ocr_screenshot2]]'
---
# Tools Workflows

## Summary

> 拆分自 `00_inbox/prompt-best-practices-collection.

md` > 条目数：9 https://promptpilot.

volcengine.

## Source Refs

- `src_20260522_9d322e81` -> `10_raw/sources/src_20260522_9d322e81-tools-workflows.md`

## Reusable Knowledge

- 灵感闪现四步法：直接罗列→联想拆解归类→寻求参考激发→找到本质再激发，每层累积变长、严禁删减，用于遍历可能性而非过早优化。
- GEO内容改编原则：融合算法偏好（AI可抓取的结构化信息）与平台爆款逻辑（短视频节奏、情绪钩子、互动设计），实现"机器可读+人类愿转"的双重优化。
- 客服AI角色设计三要素：严格基于知识库回答、分角色语境切换（管理员/操作员）、安全边界明确（不编造、不越权、隐私保护）。
- 超级角色选角"三要三不要"：要普世痛点、集体意意平、人设反转；不要完美主角、边缘路人、肤浅玩梗——核心是将经典角色转化为当代情绪容器。
- Coze工作流设计三阶段法：架构设计（3-8节点宏观拆解）→节点逐一配置（模型选型+提示词+参数定义）→文档固化，每阶段必须用户确认后方可推进。
- 提示词工程分层策略：系统提示词定角色/规则/约束，用户提示词承载具体任务输入，两者分离以确保行为一致性和任务灵活性。
- 多专家角色协同机制：项目总监调度不同专家角色（架构师/配置专家/文档工程师），通过"完全代入"实现深度专业化，而非单角色泛化应对。

## Open Questions

- 灵感闪现四步法声称"不要删减"，但未定义如何判断任务4的"完整答案"何时达成，是否存在过度累积导致信息噪音的问题？
- GEO改编示例中将医学内容（流感防治）转化为短视频脚本，但未说明如何处理医疗信息的准确性审核责任归属，这种改编是否存在健康传播风险？
- Yoopie客服提示词要求"严格基于《Yopoint无仓模式产品手册》"，但未提供该手册的实际内容或更新机制，如何验证其回答的边界是否真正覆盖手册全部内容？
- 超级角色生成器的"三要三不要"准则中，"集体意难平"和"人设反转"是否存在内在冲突——反转是否可能消解原作的情感真实性？
- Coze工作流三阶段法要求"必须获得用户明确肯定"，但未定义用户沉默、模糊回应或部分修改时的处理规则，流程可能陷入无限循环？
- 多专家角色协同机制中"完全代入"的切换标准不明确：若用户需求跨阶段模糊（如同时涉及架构调整和节点细节），总监应中断当前专家还是维持阶段隔离？
- 提示词工程分层策略中系统提示词与用户提示词的分离，在Coze实际平台中是否支持这种严格分离，还是会被模型合并处理？
- 条目36仅提供头条链接无实质内容，该来源的"举一反三"方法论是否经过验证，还是仅为流量导向的概括性主张？

## Output Opportunities

Content: <article: "Prompt Engineering Pattern Library" — cataloging the 6 reusable prompt archetypes from the source (inspiration flash, GEO adaptation, customer service AI, super-character casting, Coze workflow design, tool-layer strategy) with cross-references to the "善用佳软" precision-matching framework, plus a decision tree for selecting the right pattern based on task type, output format, and verification requirements>
Code: <script: "Coze Workflow Stage-Gate Validator" — automates the three-phase confirmation protocol from the source, with built-in handling for edge cases (silence, partial modification, ambiguous response) that the source leaves undefined, integrating the "必须获得用户明确肯定" constraint with timeout/escalation logic>
Capability: <workflow: "AI Content Adaptation Safety Protocol" — addresses the open question about GEO medical content risk by adding a mandatory "Accuracy Verification Gate" before any health/science GEO adaptation, with role-based sign-off (domain expert + legal review) and provenance tracking for source claims>
