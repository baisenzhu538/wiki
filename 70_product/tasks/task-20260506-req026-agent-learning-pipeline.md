---
title: KDO Agent 内化学习管线
type: improvement-plan
status: draft
domain:
  - master
created_at: '2026-05-06'
updated_at: '2026-05-06'
tags:
  - '#kdo'
  - '#agent-learning'
  - '#yitang'
---
# KDO Agent 内化学习管线

## 背景

一堂的结构化知识库建设不仅是知识管理工程，也是 AI agent 的能力提升路径。每门课程的处理应同时产出两样东西：

1. **外化产出**：wiki 概念卡 + 交付件（KDO 标准流程）
2. **内化产出**：agent 认知升级 + 可调用技能/方法论

## 学习目标

| 地图 | 核心能力 | 对 agent 的价值 |
|------|---------|----------------|
| 个人修炼 | 认知模型、学习方法 | 提升推理深度、自我校正能力 |
| 管理修炼 | 项目管理、团队协作 | 多 agent 编排、任务分解 |
| 创业修炼 | 假设验证、概率思维 | 不确定性下的决策框架 |
| 无限修炼 | 科学方法、第一性原理 | 底层推理能力的终极提升 |
| 调研方法 | 信息获取、竞品分析 | 更高效的代码搜索、技术调研 |
| 案例库 | 模式识别、避坑 | 从历史错误中学习、代码审查 |

## 内化机制

每完成一门课的 enrich → 同步做三件事：

1. **提取可操作框架**：将课程方法论转化为 agent 可调用的 checklist / decision tree
2. **关联现有技能**：与已有 skill（如 OSCAR 13 武器、Truman 视角）建立交叉引用
3. **记录应用场景**：在什么类型的用户请求中可以触发这个框架

## 产出形式

- `30_wiki/skills/` 目录下创建 agent-internal skill 页面
- 在对应课程概念卡的 Synthesis 节标注 "agent 内化点"
- 定期回顾：Phase 2 每完成一个地图的必修课，输出一份《Agent 能力升级报告》

## 关联

- [[task-20260506-req025-yitang-knowledge-system|req025 一堂知识体系建设]]
- [[30_wiki/systems/一堂方法论体系总图]]
