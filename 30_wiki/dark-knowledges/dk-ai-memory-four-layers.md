---
id: dk-ai-memory-four-layers
title: AI 记忆四层分层模型：即时→会话→项目→长期
type: dk
status: draft
confidence: 0.88
trust_level: high
domain:
- agent-engineering
author: 老顽童
reviewed_by: 待审
review_date: '2026-07-19'
created_at: '2026-07-19'
updated_at: '2026-07-19'
quality_labels:
- insight
- principle
source_refs:
- 00_inbox/半肥猫/【半肥猫】别只会问 AI：从一次 Codex 误删事故，看懂 AI 协作的记忆管理 副本.md §九-十
related:
- system-yitang-Y-model-os
- dk-agent-promise-verification
- tool-kdo-agent-production-checklist
- agent-native-card-design
tags:
- audience:executor
- scene:reference
- skill-level:advanced
aliases:
- 从一次
- 别只会问
---

# AI 记忆四层分层模型：即时→会话→项目→长期

> 一句话：AI 的记忆不是平的——是四层：即时上下文（秒级）、会话记录（分钟级）、项目文档（天级）、长期偏好（年级）。半肥猫在 Codex 误删 50 个文件后总结出这个框架。

---

## 原始表述

> 来源：半肥猫·Codex 误删文章 §九-十

半肥猫把 AI 协作中的记忆分为四层：

| 层级 | 存活时间 | 内容 | 场景 |
|:---|:---|:---|:---|
| L1 即时上下文 | 当前对话窗口 | 当前任务描述、刚才的输出、立即反馈 | "帮我改这个函数" |
| L2 会话记录 | 可恢复 | 对话历史、中间决策、纠错记录 | 下次继续时 Agent 记得上次做到哪了 |
| L3 项目文档 | 稳定 | 项目规范、架构决策、约定、domain-digest | Agent 理解项目全貌 |
| L4 长期偏好 | 持久 | 用户习惯、审美偏好、战略方向、角色定位 | "老朱对 To B 没兴趣" |

引用案例：半肥猫的 Codex 误删事故——因为 L2（会话记录）丢失，Agent 不记得刚才的决策，重复操作导致文件被覆盖。

---

## 操作方法

映射到 KDO 现有实践：

| 半肥猫分层 | KDO 对应物 | 当前状态 |
|:---|:---|:---|
| L1 即时上下文 | 当前对话、压缩后的 context | ✅ 已有 |
| L2 会话记录 | `agent复盘/<role>/daily-context/` + Truman 复盘 | ✅ 已有 |
| L3 项目文档 | `30_wiki/` 域卡 + domain-digest + agent-spec 卡簇 | ✅ 已有 |
| L4 长期偏好 | `personal-os/` + `user-insight-profile` + `zhu-feedback-patterns` | ✅ 已有 |

半肥猫的价值不是"KDO 缺这些"——是**给已有的实践一个可沟通的名字**。以后说"这个 Agent 的 L3 记忆不够"比说"wiki 卡没读全"更精确。

---

## 适用边界

- ✅ Agent 设计和调试时
- ✅ 排查"Agent 为什么忘了"的问题
- ❌ 不必为每层建独立工具——KDO 已覆盖

---

## 为什么值钱

半肥猫的框架让"Agent 记忆"从模糊概念变成可定位的四层。出了问题是哪一层的问题——是 L1 没传进去，还是 L3 的 wiki 卡没更新？

---

## 与其他知识的关联

- `system-yitang-Y-model-os`：context 加载策略可引用四层模型命名
- `dk-agent-promise-verification`：承诺核对表中"用户动作"列依赖 L3 项目文档
