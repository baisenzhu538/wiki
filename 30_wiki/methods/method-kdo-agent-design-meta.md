---
id: method-kdo-agent-design-meta
title: KDO Agent 设计元方法——用双三角加速 Agent 建设
type: method
status: reviewed
author: 王语嫣
reviewed_by: 欧阳锋
review_date: 2026-07-06
confidence: 0.85
trust_level: high
created_at: 2026-07-06
updated_at: 2026-07-06
source_refs:
- 00_inbox/人机协作双三角/一堂双三角-人机协作模型-口述.txt L4595-4604
- 00_inbox/人机协作双三角/一堂双三角-人机协作模型-口述.txt L462-600
related:
- '[[agent-spec-dual-triangle-canvas-filler]]'
- '[[method-yihang-ai-self-xray-iteration]]'
- '[[method-dual-triangle-flywheel-engine]]'
- '[[method-kdo-agent-distillation]]'
- '[[method-judge-skill-meta-evaluation]]'
- '[[method-yihang-human-self-distillation]]'
tags:
- audience:general
- scene:diagnosis
- skill-level:advanced
---

# KDO Agent 设计元方法：用双三角加速 Agent 建设

## 一句话

把 Truman 做 partner 的方法（先画双三角画布→引擎迭代→自复盘）固化为 KDO 所有 Agent 建设的标准流程。目标：3-5 天产一个 Agent，下饺子。

## 外部验证

- **MongoDB Canvas Framework（2025）**：POC 8 格 + Production 11 格——先验证产品问题再设计 Agent 能力再选数据再选模型，"product→agent→data→model"流程与 Truman 的"先填画布再动手"逻辑一致。
- **Abundly Agent Design Canvas（2025）**：50+ Agent 实战提炼 8 要素——Purpose/Trigger/Input/Action Plan/Interface/Output/Knowledge/Capabilities。比 KDO 双三角画布多了 Trigger 和 Interface 两个维度。
- **Anthropic 三原则**：① 只在模糊高价值可验证任务上用 Agent ② 核心架构 = environment + tools + system prompt，先跑通再优化 ③ "Think Like Your Agent"。
- **21 Agentic Design Patterns（Gulli 2025）**：从 Prompt Chaining 到 Multi-Agent Collaboration 的 21 个可复用模式。

## 三步法

### 第一步：画 Agent 自身的双三角（动手前）

```
每个 Agent 在设计前必须填自己的双三角画布：
  H.审美 —— 这个 Agent 输出"好"的标准是什么？
  H.体系 —— 它执行任务的稳定流程是什么？
  H.创造力 —— 它的边界在哪？什么情况下它该说自己不知道？
  A.场景 —— 它解决什么问题？不为哪些场景设计？
  A.数据 —— 它需要什么数据包？从哪些 wiki 卡编译？
  A.基本功 —— 它用什么模型/工具？Feature 组合是什么？
  🆕 Trigger —— 什么触发它？（手动/定时/事件驱动）
  🆕 Interface —— 它通过什么界面交互？（CLI/飞书/API）
```

画布填满 = 可以承诺交付。这是风险判断工具。

### 第二步：Y 模型引擎迭代（动手后）

```
Agent v0 → 真实场景测试 → trace 复盘 → 暴露缺口
  → 回画布：哪个角不够？补上
  → Agent v0.1 → 再测 → 再复盘
```

不是一次性设计好——第一版足够粗糙但可跑，然后每天迭代。

### 第三步：Agent 自复盘（每次运行后）

```
会话结束 → Agent 自己跑复盘 → 映射本轮对话到六要素
  → 画飞轮 → 自我改进建议 → 存入 trace
  → 下次会话作为 data pack 加载
```

## 不该用 Agent 的场景

| 场景 | 为什么不该用 | 替代方案 |
|:---|:---|:---|
| 确定性任务 | Agent 的随机性反而增加风险 | 直接用脚本/工作流 |
| 低价值高频任务 | Agent 的 token 成本 > 人的时间成本 | 传统自动化 |
| 不可验证的任务 | 没有验证标准的 Agent = 不可控 | 先建审美标准再引入 Agent |
| 单次一次性任务 | 不值得花 3-5 天建设 | 直接用 LLM 对话 |

## 失败模式

1. **画布形式主义**——填完画布 ≠ 想清楚了。填满格子可以承诺交付，但格子里的内容质量比数量重要。
2. **过度设计**——还没跑过 v0 就开始优化 prompt 拓扑。先跑通一个 Agent，再谈多 Agent 编排。
3. **忽视 Trigger 设计**——Agent 什么时候启动、什么时候停、什么情况下叫停——这些比 prompt 本身更重要。
4. **单 Agent 思维**——多个 Agent 之间的交互拓扑和单个 Agent 的 prompt 需要一起设计（MASS ICLR 2026）。
5. **没有"不该用 Agent"的判断标准**——不是所有问题都适合用 Agent 解决。

## 多 Agent 工位拆分

**工位概念**：把复杂任务拆成细分场景，每个场景一个独立 Agent。不要幻想一个万能 AI 解决所有问题——"工位"就是 Agent 的分工单元。

**熙熙 4 工位案例**：

| 工位 | 做什么 | 对应双三角场景角 |
|:---|:---|:---|
| **关键词布局 Agent** | 研究目标人群的搜索习惯，做关键词策略 | 场景（细分流量入口） |
| **案例替换 Agent** | 把通用案例替换为真实用户案例，提升内容可信度 | 数据（案例库调用） |
| **评审大师 Agent** | 模仿目标期刊/平台审稿人标准做质检 | 审美（对标的判断标准） |
| **评论区 Agent** | 模拟真实读者评论，检测内容的传播力 | 场景（转化承接） |

**工位与双三角画布场景角的对应**：每个工位 = 场景角的一次细分。画布填"我要做内容"→工位拆"关键词→案例→评审→评论"四个独立 Agent。工位拆得越细，每个 Agent 的 prompt 越精准。

## Critique

- 三步法的核心是 Truman 的方法论，KDO 只是操作化。如果 Truman 的原始方法有缺陷，这套也会继承。
- "3-5 天下饺子"是 Truman 一堂团队的体感，KDO 目前尚未验证这个速度。
- 外部 Agent 设计画布（MongoDB/Abundly）比 KDO 画布多了 Trigger 和 Interface 维度——KDO 画布需要升级。

## Action Triggers

| 触发场景 | 第一个动作 | 成功指标 |
|:---|:---|:---|
| 决定新建一个 KDO Agent | 先填 Agent 双三角画布（10 格），不跳过 | 画布六要素 + Trigger + Interface 全部有内容 |
| 画布填完准备动手 | 选最小可行性版本——只做一个场景、一个输出格式 | v0 在 1-2 天内可跑 |
| Agent v0 跑完第一轮测试 | 跑自复盘→暴露缺口→回补画布 | 画布至少更新 1 个角的认知 |
| 多个 Agent 需要协作 | 先画 Agent 交互拓扑图，再各自优化 prompt | 拓扑图明确谁先动、谁后动、什么情况下叫停 |
| Agent 连续 3 轮迭代无明显改进 | 回到"不该用 Agent"清单检查——可能这个场景根本不适合 Agent | 做出 go/no-go 判断 |

## Synthesis

本方法是 KDO Agent 化的操作系统——上承 [[method-kdo-agent-distillation]]（蒸馏对话→prompt），下接 [[agent-spec-dual-triangle-canvas-filler]]（第一个走完三步法的试点 Agent），左靠 [[method-dual-triangle-flywheel-engine]]（引擎迭代），右依 [[method-yihang-ai-self-xray-iteration]]（自复盘闭环）。四张卡共同构成 KDO Agent 从设计→蒸馏→迭代→自进化的完整流水线。
