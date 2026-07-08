---
id: tool-yitang-dual-triangle-domain-registry
title: 双三角域注册表
type: tool
status: draft
author: 王语嫣
reviewed_by: pending
confidence: 0.80
trust_level: medium
language: zh-CN
created_at: 2026-07-08
updated_at: 2026-07-08
domain:
- yitang
- ai-collaboration
- planning
source_refs:
- 00_inbox/人机协作双三角/一堂双三角-人机协作模型-口述.txt
related:
- '[[concept-yihang-dual-triangle-core]]'
- '[[framework-yitang-y-model-dual-triangle-synergy]]'
- '[[agent-spec-yitang-dual-triangle-cross-domain-diagnostician]]'
aliases:
- 双三角域注册表
- 跨域域注册表
---

# 双三角域注册表

> **一句话定义**：一个维护「业务域 → 双三角知识卡 / Agent / 工具」映射关系的注册表，用于跨域诊断时快速定位相关资源。

---

## 一、注册表结构

| 字段 | 说明 |
|:---|:---|
| **domain_id** | 域唯一标识 |
| **domain_name** | 域中文名 |
| **related_concepts** | 相关概念卡 |
| **related_frameworks** | 相关框架卡 |
| **related_tools** | 相关工具卡 |
| **related_agent_specs** | 相关 Agent 规范卡 |

---

## 二、使用步骤

1. 输入任务描述或域标识。
2. 查询注册表，返回相关域及其资源映射。
3. 由用户或诊断 Agent 确认最合适的域。
4. 调用对应资源进行下一步分析。

---

## 三、使用原则

- 注册表只负责「定位」，不替代诊断。
- 一个任务可能对应多个域，需人工确认优先级。
- 随着知识库扩展，注册表需要定期同步更新。

---

## 四、Critique

### 内部局限

1. **依赖注册表完整性**：未录入的域无法被检索到。
2. **边界模糊时容易误判**：相近域需要人工复核。

---

## 五、Action Triggers

| 触发场景 | 第一个动作 | 成功指标 |
|:---|:---|:---|
| 跨域诊断前 | 查询注册表，列出候选域 | 返回 ≥1 个相关域 |
| 发现新域 | 注册新域并关联相关资源 | 新域可被后续查询命中 |
