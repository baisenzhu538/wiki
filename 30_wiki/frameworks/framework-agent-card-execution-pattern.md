---
id: framework-agent-card-execution-pattern
title: Agent 执行模式：从卡片到可执行动作
type: framework
status: draft
author: 黄药师
created_at: 2026-07-04
updated_at: 2026-07-04
confidence: 0.8
trust_level: medium
domain:
- kdo
- ai-collaboration
source_refs:
- 30_wiki/tools/agent-spec-dual-triangle-canvas-filler.md
- 30_wiki/tools/tool-opc-sales-dialogue-assistant.md
- kdo-tools/canvas-agent.py
- kdo-tools/agent-prompt-compiler.py
related:
- '[[agent-spec-dual-triangle-canvas-filler]]'
- '[[tool-opc-sales-dialogue-assistant]]'
- '[[system-yitang-Y-model-os]]'
- '[[agents/agent-os]]'
- '[[concept-yihang-dual-triangle-core]]'
tags:
- audience:ceo
- scene:diagnosis
- skill-level:intermediate
---

# Agent 执行模式：从卡片到可执行动作

> **一句话**：KDO 卡片是静态知识，Agent 是动态执行器。本框架定义 Agent 如何基于卡片和 Skill 解决实际问题——判断任务类型、声明工具边界、按 Y模型 迭代执行。

---

## 一、三种执行模式

不是所有问题都该调用同一种 Agent。按任务复杂度分三级：

| 模式 | 触发场景 | 执行方式 | 示例 |
|:---|:---|:---|:---|
| **查询模式** | 单一事实问题 | `kdo query` → 返回卡片 | "用户分层四步法是什么" |
| **诊断模式** | 需判断的复杂问题 | Agent 加载域卡片 → 追问 → 诊断 → 建议 | "这个客户该用什么跟进策略" |
| **执行模式** | 需产出可交付物 | Agent 加载域卡片 + 工具 → 迭代产出 → 飞轮记录 | "帮我把这个任务拆成双三角画布" |

---

## 二、Agent 执行循环

```
1. 收到任务
   ↓
2. 判断任务类型（查询/诊断/执行）
   ↓
3. 声明工具边界：我能做什么、不能做什么
   ↓
4. 加载域卡片（kdo query / agent-prompt-compiler）
   ↓
5. 执行（Y模型迭代：朴素认知 → 假设 → 验证 → 修正）
   ↓
6. 输出 + 飞轮记录（before-after）
```

---

## 三、工具边界声明

每个 Agent 必须在启动时声明：

| 我能做什么 | 我不能做什么 |
|:---|:---|
| 基于 KDO 卡片给出方法论建议 | 替代你的最终判断 |
| 拆解复杂问题到可执行步骤 | 执行涉及资金/合同/法律的动作 |
| 记录迭代反馈到飞轮日志 | 在没有上下文时瞎猜 |

---

## 四、已有 Agent 对照

| Agent | 执行模式 | 工具边界 |
|:---|:---|:---|
| 销售对话助手 | 诊断模式 | 读对话→判阶段→给话术，不自动发送 |
| 画布填充 Agent | 执行模式 | 追问→填六要素→输出画布，不下判断 |
| Y模型 Coach | 诊断模式 | 追问朴素认知→推Y模型循环，不给标准答案 |

---

## 五、设计原则

1. **先跑通一张卡，再建体系。** 销售对话助手已验证。画布 Agent 是第二个。
2. **Agent 是编译产物，不是新建的。** 一张 agent-spec 卡 + 编译器 = Agent。
3. **工具边界必须显式声明。** 不声明边界的 Agent 会越界。越界的 Agent 会失去信任。
