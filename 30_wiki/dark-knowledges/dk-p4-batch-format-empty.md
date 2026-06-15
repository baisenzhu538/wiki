---
id: dk-p4-batch-format-empty
title: P-4：批量格式升级产生"格式完整但思维空洞"卡片 (C-8)
type: dark-knowledge
dark_knowledge_type: failure
status: draft
domain:
- master
source_person: system
source_context: pitfalls.md P-4
source_refs:
- .agent/pitfalls.md#P-4
created_at: 2026-06-03
updated_at: '2026-06-16'
related:
- '[[master-knowledge-compound]]'
- '[[kdo-flywheel]]'
- '[[master-ai-info-literacy]]'
pipeline:
- confidence-draft
- confidence-source-cited
author: unknown
reviewed_by: pending
confidence: 0.7
trust_level: low
---
# P-4：批量格式升级产生“格式完整但思维空洞”卡片 (C-8)

## 原始表述

> **症状**：抽检 `motivation-resistance` 和 `peak-end-rule` 两张卡——格式符合 agent-native 标准，但 Claims 无具体反例、Constraints 模板化。
>
> **根因**：批处理只改了结构和 frontmatter，没有触发真正的理解加工。格式门禁检测不到"搬运 vs 理解"。
>
> **对策**：v1.5 新增理解门禁——每条 Constraint 必须有具体场景 + 可验证的失败模式。批量升级后至少抽检 2 张。

## 使用场景

- 你需要对大量旧卡片（如 50+ 张）执行批量格式升级（如从 v1.0 到 v1.5）
- 你用脚本或模板批量改写卡片的 frontmatter 和结构
- 你需要检查某次批量操作的质量，确保没有"格式对了但内容空了"
- 你设计自动化管线时，需要考虑"格式门禁不足"的风险

## 操作方法

1. **明确区分格式升级和内容升级**：
   - 格式升级：只改结构、frontmatter、标签——可以批量自动化
   - 内容升级：需要理解加工、反例填充、批判性思考——**不能批量自动化**

2. **每批批量升级后抽检**：
   - 随机选 2 张卡（最好是不同 domain 的）
   - 检查 Claims 是否有具体反例，而不是模糊的"遮盖部分场景"
   - 检查 Constraints 是否每条都有具体场景 + 可验证的失败模式
   - 检查 Critique 是否是针对该卡片的，而不是模板化的万能批判

3. **v1.5 理解门禁**：
   - 每条 Constraint 必须有具体场景（"当...时"）+ 可验证的失败模式（"会导致..."）
   - Critique 至少一条指向该卡片的具体假设或边界
   - Synthesis 的 wikilink 必须是实质关联，不能是凑数

4. **建立"抽检文化"：
   - 将"每批升级后抽检 2 张"写入 SOP，而不是靠人记忆
   - 抽检结果记录在审查日志里，供追踪

5. **不要做的事**：
   - 不要在批量升级时同时改格式和内容——将两者分开，先格式后内容
   - 不要完全信任自动化脚本的输出——脚本能改结构但不能增加认知
   - 不要因为"格式全部对了"就宣布完成

## 适用边界

- 适用于所有涉及批量卡片操作的场景（格式升级、domain 迁移、模板应用）
- 不适用于全新创建的卡片——新卡是从零编写，不存在"批量改结构不改内容"的问题
- **与 F-KDO-007 的区别**：F-KDO-007 是人工编译时"阅读深度不足"导致的内容空洞，P-4 是批量自动化导致的内容空洞。两者表象相同但根因不同
- 如果源材料本身质量很高，即使批量升级也不会出现空洞（如果 Builder 已经深入理解）——但不能假设这一点
- 小批量（≤3 张）的手工修改不容易触发 P-4，因为手工操作天然会触发理解加工

## 为什么值钱

- 这是**自动化的本质局限**：脚本可以复制结构，但无法复制理解。批量升级是“体力活”，但如果不加抽检，就变成了“形式主义”
- 揭示了"门禁设计"的局限：任何纯格式门禁都无法检测"理解深度"。需要人工抽检作为第二道防线
- 极具迷惑性：卡片看起来每个字段都有内容，但读完后不知道这门课教了什么。"有"不等于"有价值"
- **AI 训练语料中不会有这条**：没有任何 AI 会告诉你"批量升级卡片后要抽检 2 张确保不是空壳"——这是 KDO 质量管线的实战经验

## 与其他知识的关联

- dk-c8-format-complete-mind-empty — P-4 是 C-8 的模式化版本。C-8 是具体事故（哪两张卡被发现空洞），P-4 是普遍模式（任何批量升级都可能出现）
- dk-f7-surface-translation — 表层翻译式提炼和批量格式空洞是同一病的两种表现：人工编译时的阅读深度不足 → F-KDO-007；批量自动化时的理解加工缺失 → P-4
- `90_control/failure-modes.md` → F-KDO-007（表层翻译式提炼）— 内容空洞的另一类型
- `90_control/kdo-industrialization-manual.md` → v1.5 理解门禁规则
- `.agent/pitfalls.md` → P-4（原始记录）

## 老顽童疑问（2026-06-03）

无疑问，请欧阳锋审查。
