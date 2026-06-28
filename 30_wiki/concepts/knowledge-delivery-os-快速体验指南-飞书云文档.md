---
id: knowledge-delivery-os-快速体验指南-飞书云文档
created_at: 2026-04-30
domain: master
source_refs:
- 10_raw/sources/src_20260501_6a491b80-knowledge-delivery-os-快速体验指南-飞书云文档.md
status: enriched
title: Knowledge Delivery OS 快速体验指南 - 飞书云文档
type: concept
updated_at: 2026-05-04
pipeline:
- src_unknown
author: unknown
reviewed_by: 欧阳锋
confidence: 0.8
trust_level: medium
related:
- - - concept-wanghuan-tacit-knowledge-examples
- - - yt-management-team-knowledge
- - - tool-泛产品设计-需求工具箱指南
- - - fix-dark-knowledge-extractor-llm
- - - master-knowledge-compound
- - - HIS系统开发实现方案-架构师指南
- - - ocr-泛产品设计-需求工具箱指南
- - - yt-personal-knowledge-extraction
- - - yt-tool-knowledge-extraction
- - - ocr-泛产品设计-审美工具箱指南
---

# Knowledge Delivery OS 快速体验指南

> **定位**：KDO 是一个本地优先的产品，用于将知识转化为可交付资产。不是笔记应用——是基于仓库的工作空间 + CLI，将输入编译为可重用知识，生成三类产出：内容、代码、能力。

---

## Claims

1. **核心循环 9 步闭环**：捕获 (capture) → 注册 (register) → 编译 (ingest) → 路由 (route) → 生产 (produce) → 验证 (validate) → 交付 (ship) → 反馈 (feedback) → 改进 (improve)。每一步有对应的 CLI 命令和目录映射，形成知识到资产的完整流水线。

2. **三层产物模型**：内容（文章/视频/教程/课程/报告）、代码（应用/插件/模板/脚本/包）、能力（技能/代理/工作流/评估/手册）。三类产物共享同一套 source → wiki → artifact 的溯源链路。

3. **本地优先架构**：所有数据存储在本地文件系统，通过 `state.json` 管理状态，通过 Markdown + YAML frontmatter 管理内容。不依赖云端服务，Git 直接可用作版本管理和协作。

4. **CLI 即界面**：12 个核心命令覆盖完整生命周期（init/capture/fetch-url/import-chat/ingest/enrich/query/produce/validate/ship/feedback/improve/lint/status）。不提供 GUI——目标用户是愿意用命令行的技术用户。

5. **飞书作为输入桥**：KDO 可与外部文档系统配合——飞书文档、网页、AI 对话都可作为输入源（`kdo capture` / `kdo import-chat`），进入 inbox 后走标准流水线。

---

## Critique

### 前提假设
- src_unknown
- src_unknown
- src_unknown

### 边界与反例
- src_unknown
- src_unknown
- src_unknown

### 可靠性评估
**整体可靠性：中。** KDO 的架构设计清晰，三层模型（raw → wiki → output）逻辑自洽。但当前版本仍是早期阶段——lint 检查显示大量 scaffold 目录缺失，部分概念卡未完成编译。产品成熟度不足以支撑"生产级"依赖。

---

## Synthesis

### 关联概念
- 待补充链接
- 待补充链接
- 待补充链接
### 互补与冲突
- 待补充链接
- 待补充链接
### 可迁移场景
- 待补充链接
---

### 不要用的场景

| 场景 | 为什么失效 | 替代方案 |
|------|-----------|---------|
| 把这个框架/方法当成绝对真理执行 | 任何方法论都是时间截面，它们假设未来会像过去一样发展 | 每次使用前先问"这个结论现在还成立吗？有没有新的反例出现？" |
## Source Refs

- src_unknown

## Open Questions

- src_unknown
- src_unknown
- src_unknown
- src_unknown
## Output Opportunities

- src_unknown
- src_unknown

## Action Triggers

| 触发场景 | 第一个动作 | 成功指标 |
|---------|-----------|---------|
| 需要基于这份调研/框架做出关键决策前 | 先问自己"这个结论现在还成立吗？有没有新的反例出现？" | 每次使用前都能说出至少一个可能影响结论有效性的新变化因素 |
