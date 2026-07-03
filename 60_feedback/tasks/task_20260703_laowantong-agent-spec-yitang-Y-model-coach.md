---
id: task_20260703_laowantong-yitang-Y-model-os
title: Y模型 OS：所有 Agent 的共享底层 prompt + 可选 Coach 模式
type: task
status: in_progress
priority: P1
assignee: kimi
reviewer: 欧阳锋
reviewed_by: pending
created_at: 2026-07-03
updated_at: '2026-07-03T15:23:15.324117+00:00'
expected_outputs:
- 1 张 system 卡：system-yitang-Y-model-os.md（共享底层 prompt 片段）
- agent-native-card-design.md 更新：所有 agent-spec 卡必须包含 Y模型 OS 层
- 1 张可选 agent-spec 卡：tool-agent-spec-yitang-Y-model-coach（作为 Coach 模式，非调度器）
- 1 个域 Agent 集成示例：修改 OPC 销售对话助手 System Prompt 展示如何加载 OS 层
- 至少 2 个真实场景测试（销售、GEO/网站）
dependencies:
- task_20260703_laowantong-yitang-Y-model-foundation-production reviewed
source_refs:
- 30_wiki/systems/agent-native-card-design.md
- 30_wiki/systems/agent-external-brain-design.md
- 60_feedback/tasks/task_20260703_laowantong-yitang-Y-model-foundation-production.md
related:
- yt-decision-y-model
- framework-yitang-shishi-qiushi
- framework-yitang-jiefang-sixiang
- tool-yitang-Y-model-application
- dk-yitang-Y-model-pitfalls
- agent-native-card-design
- agent-external-brain-design
- tool-opc-sales-dialogue-assistant
- opc-ai-sales-agent-architecture
---

# Y模型 OS：所有 Agent 的共享底层 prompt + 可选 Coach 模式

> 任务来源：黄药师提出正确 Agent 分层——Y模型+实事求是+解放思想是所有 Agent 的共享底层 OS，不是独立元 Agent；域方法论卡和用户个人域才是区分不同 Agent 的层。
> 目标：把 Y模型 OS 写成可复用的共享 prompt 片段，让所有域 Agent 默认加载；Coach 模式只作为可选入口，不替代域 Agent。
> 依赖：`#51` 一堂底层逻辑域 7 张卡终审通过。

---

## 一、问题诊断：之前的摇摆在哪里

之前把 Y模型教练设计成了**一个独立的元 Agent**，想让它成为"新问题第一站 + 领域 Agent 调度器"。这导致两个矛盾：

1. **元 Agent 必须懂域知识才能调度**——但调度销售/GEO/设计需要懂这些域，结果它要么变成全才，要么调度不准。
2. **元 Agent 和域 Agent 之间多了一层摩擦**——用户本来可以直接问销售 Agent，却要先过一遍 Coach，反而慢了。

正确的分层应该是：

```
Y模型 OS（怎么思考）        ← 所有 Agent 共享，建一次
    ↓
域方法论卡（思考什么）       ← 每个域一套，按需建设
    ↓
用户个人域（跟谁协作）       ← 每个用户持续迭代
    ↓
专属 Agent                   ← 三层叠加的可用产品
```

所以 Y模型不是"一个 Agent"，而是**所有 Agent 的底座 prompt**。

---

## 二、核心产出

### 1. `system-yitang-Y-model-os.md`

一张 system 类型的卡片，内容是可被所有 agent-spec 卡引用的共享 prompt 片段。

包含：
- **角色声明**：你是一位用 Y模型 + 实事求是 + 解放思想 思考的助手。
- **协作原则**：不强制流程、跟着用户节奏、一次只做一个有用动作、Y模型是地图不是枷锁。
- **反幻觉规则**：信息不足时标注置信度、区分事实与假设、关键数字必须标注来源。
- **解放思想规则**：主动挑战"显然"、找出隐含假设、提出 1-2 个替代路径。
- **知行合一规则**：每次对话结束给出一个最小可执行动作。
- **个人域加载规则**：启动时读取用户的个人 OS/决策记录/反馈模式（未来实现）。

### 2. `agent-native-card-design.md` 更新

增加一节：

> **所有 agent-spec 卡的 System Prompt 必须分层为**：
> 1. `OS 层`：引用 `system-yitang-Y-model-os.md`（怎么思考）
> 2. `域层`：引用该域的 framework/tool/case/dk 卡（思考什么）
> 3. `用户层`：加载个人域上下文（跟谁协作）

### 3. `tool-agent-spec-yitang-Y-model-coach`（可选 Coach 模式）

不是独立 Agent，而是**任何域 Agent 可以进入的 Coach 模式**。

触发条件：
- 用户说"我们按 Y模型重新理一下"
- 用户问题明显跨域/无明确域归属
- 用户主动要求"先不调用专业 Agent，先帮我想清楚"

行为：
- 只使用 OS 层 + 通用对话，不调用域方法论卡（除非用户明确）。
- 目标是帮用户把问题结构化到可以交给某个域 Agent 的程度。

### 4. 集成示例：OPC 销售对话助手

在销售对话助手的 System Prompt 顶部加入：

```
[OS 层]
{{system-yitang-Y-model-os.md}}

[域层]
你是 OPC 销售对话助手。你的域知识来自：
- framework-yitang-scientific-sales-methodology
- tool-opc-customer-segmentation
- tool-opc-value-proposition-generator
- ...

[用户层]
加载当前用户的个人域：时间 OS、历史决策偏好、客户列表...
```

---

## 三、验收标准

- [x] `system-yitang-Y-model-os.md` 创建并通过 `kdo pre-submit`。
- [x] `agent-native-card-design.md` 增加"Agent Prompt 三层结构"章节，明确所有 agent-spec 必须加载 OS 层。
- [x] `tool-agent-spec-yitang-Y-model-coach` 创建，定位为"可选 Coach 模式"，不是调度器。
- [x] OPC 销售对话助手 System Prompt 更新，展示 OS 层加载方式。
- [x] 至少 2 个真实场景测试：
  - 销售场景：用户直接问销售问题，Agent 用 OS + 销售域知识回答。
  - 跨域/模糊场景：用户问"我想做个顶级网站+GEO"，Agent 先用 Coach 模式结构化，再建议调用设计/SEO Agent。
- [x] 所有关键判断标注置信度。
- [ ] 欧阳锋终审通过。

---

## 四、与后续任务的关系

| 任务 | 关系 |
|:---|:---|
| `#51` | 前置依赖：Y模型/实事求是/解放思想 framework/tool/dk/case 卡是 OS 层的知识来源 |
| `#47/#49` | OPC 销售智能体需要加载 OS 层，本任务提供集成示例 |
| `#55`（原） | 已废弃"独立元 Agent"思路，改为 OS 层 + 可选 Coach 模式 |
| 未来新域 Agent | 全部按"OS 层 + 域层 + 用户层"三层结构设计 |

---

## 五、队列位置

- **入队编号**：`#55`
- **状态**：`queued`（依赖 `#51` reviewed）
- **预计工时**：老顽童 2-3 天 + 欧阳锋终审 1 天

---

*王语嫣 2026-07-03*
