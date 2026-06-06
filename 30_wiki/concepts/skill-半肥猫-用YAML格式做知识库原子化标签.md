---
id: skill-半肥猫-用YAML格式做知识库原子化标签
title: 技能：用YAML格式做知识库原子化标签
type: skill
status: draft
domain: []
source_person: 半肥猫
source_context: AI学习落地
source_refs: []
wiki_refs: []
definition_of_done:
  - 操作步骤清晰可执行
  - 适用场景有正反例
  - 工具要求明确
tags:
  - "#domain/AI"
  - "#domain/learning"
tools_required: []
prerequisite_skills: []
related: []
created_at: '2026-06-07'
updated_at: '2026-06-07'
---

# 技能：用YAML格式做知识库原子化标签

## 原始表述

用YAML格式做知识库原子化标签是半肥猫在AI学习落地中提出的实操方法。

## 操作步骤

1. 将文档拆分为单主题原子化单元
2. 每篇文档头部添加YAML格式标签
3. 根据业务场景定义标签体系（可包含：主题、类型、版本、日期、适用场景、风险等级等）
4. 使用过程中根据召回效果迭代补充标签
5. 确保每个语义切块包含完整索引标签

## 适用场景

- ✅ 构建大型知识库需要高效检索
- ✅ AI需要精准召回特定信息
- ✅ 知识需要多维度交叉索引

## 不适用场景

- ❌ 文档量极小（<100篇）手工管理即可
- ❌ 无需AI检索的个人笔记

## 工具/环境

- 支持YAML的编辑器
- Obsidian/Notion等知识库工具
- 向量化存储系统

## 常见失败模式

- 步骤跳过或省略 → 结果不完整 → **严格按步骤执行**
- 未确认场景是否匹配 → 方法失效 → **先对照"适用场景"确认**

## 为什么有效

大模型无法像人类一样分辨文档重要性，YAML标签帮助AI快速判断相关性，提升召回命中率，避免上下文被污染

## 关联技能

- 待补充

## 来源

- 半肥猫，AI学习落地

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
