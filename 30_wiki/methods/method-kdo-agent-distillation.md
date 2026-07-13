id: method-kdo-agent-distillation
title: Agent 蒸馏方法——对话→系统提示词 5 步框架
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
- 00_inbox/人机协作双三角/YAI双三角agent对话记录.md
- 00_inbox/人机协作双三角/一堂双三角partner的对话记录20260705.md
- 00_inbox/人机协作双三角/一堂双三角-人机协作模型-口述.txt L2220-2312
related:
- '[[method-yihang-dual-triangle-ai-review]]'
- '[[framework-yihang-knowledge-data-decoupling]]'
- '[[agent-spec-dual-triangle-canvas-filler]]'
- '[[method-judge-skill-meta-evaluation]]'
- '[[method-kdo-agent-design-meta]]'
- '[[method-kdo-inbox-annotation]]'
- '[[method-yihang-human-self-distillation]]'

# Agent 蒸馏方法：对话→系统提示词 5 步框架

## 一句话

从 Agent 对话记录中系统性地提取可复用的核心词（审美+体系）和 data pack（场景+数据+基本功），编译为可注入的 system prompt 段落。

## 外部验证

- **SePO（arXiv 2026.06）**：自进化提示词优化——提示词 Agent 同时优化任务 Agent 和自己的 system prompt。蒸馏的终点不是"人提取"，而是 Agent 自优化。
- **MASS（ICLR 2026）**：拓扑 + prompt 联合优化——多 Agent 系统的 prompt 和交互拓扑需要一起设计，不能分开。
- **Anthropic 原则**："Think Like Your Agent"——把自己放在 Agent 的上下文窗口里理解它的决策。蒸馏的第一步不是提取规则，是理解 Agent 的决策逻辑。
- **提示词工程正在消亡（HuggingFace 2025）**：被 Skills/Tools/Frameworks 替代。蒸馏产出应该是可复用的 Skill + data pack 组合，不是更长的 prompt。

## 5 步蒸馏流程

```
对话上下文输入
  → Cite：标注关键决策点和框架调用
  → Compress：将标注段压缩为结构化规则
  → Connect：映射到已有 KDO 卡片（用双三角六要素对齐）
  → Codify：输出为 agent-spec 格式的 system prompt 段落（核心词+data pack 分层）
  → Evaluate：用双三角自复盘验证蒸馏质量
```

## 三层精度模型

| 层级 | 类型 | 可蒸馏性 | KDO 对应 |
|:---|:---|:---|:---|
| L1 | 结构化规则/框架/约束 | ✅ 精确 | 双三角六要素、追问模式、状态标记 |
| L1.5 | 风格/语气/判断偏好 | ⚠️ 方向正确 | 人格画像、沟通习惯 |
| L2 | 直觉/效用判断 | ❌ 不可编码 | 保持人在环 |

## 失败模式

1. 蒸馏出幻觉规则——Agent 某次对话中表现好≠这条规则是对的。必须多轮验证。
2. 过度拟合单次对话——一次对话的上下文特殊，蒸馏出的规则不够通用。
3. 核心词和 data pack 边界模糊——核心词层混入场景特定数据，导致跨场景复用失败。
4. 忽略多 Agent 拓扑——只优化单个 Agent 的 prompt，忽略 Agent 之间的交互设计。

## Critique

- 5 步流程本质是 Truman YAI 复盘法（L2220-2312）的工程化版本，不是原创方法论
- L2 层（直觉/效用）的"不可蒸馏"边界可能随时间推移变化——SePO 的自进化方向正在逼近这个边界
- 蒸馏需要至少 2-3 轮对话作为素材，单轮对话蒸馏质量不可靠

## Action Triggers

| 触发场景 | 第一个动作 | 成功指标 |
|:---|:---|:---|
| 拿到新的 Agent 对话记录 | 跑 5 步 Pipeline，先拆核心词和 data pack | 产出可挂载的 system prompt 段落 |
| 同一个 Agent 积累 5+ 轮对话 | 对比多轮蒸馏结果，找共有模式 vs 单轮特例 | 识别出至少 3 条跨对话稳定的核心规则 |
| 蒸馏出的 prompt 上线后 | 跑对比实验：蒸馏版 vs 原版，同一任务质量对比 | 蒸馏版不低于原版 90% 质量 |
| 发现蒸馏规则失效 | 回溯到原对话，检查是规则本身错还是场景变了 | 定位失效根因 |

## Synthesis

本方法缝合了三个来源——Truman YAI 复盘法（L2220-2312）的元认知框架、知识层与数据层解耦（L5025-5078）的分层架构、全网调研的蒸馏精度边界（L1/L1.5/L2）。核心创新不在单点技术，在于把这三个来源整合成了一条可工程化的流水线。详见 [[method-yihang-dual-triangle-ai-review]]（复盘法的操作层）、[[framework-yihang-knowledge-data-decoupling]]（解耦架构）、[[agent-spec-dual-triangle-canvas-filler]]（蒸馏产出的第一个应用对象）。
