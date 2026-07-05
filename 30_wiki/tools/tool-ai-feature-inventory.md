---
id: tool-ai-feature-inventory
title: AI 工具特性清单——原子化 Feature 分类框架
type: tool
status: draft
author: 王语嫣
confidence: 0.88
trust_level: high
created_at: 2026-07-06
updated_at: 2026-07-06
source_refs:
- 00_inbox/人机协作双三角/一堂双三角-人机协作模型-口述.txt L1402-1451
- GitHub synaptiai/agent-capability-standard 99原子能力本体
- arXiv 2510.14537 MCP Server Taxonomy
- IEEE Access 2026 7维29子维评估框架
related:
- '[[concept-yihang-ai-feature-thinking]]'
- '[[framework-yihang-dual-triangle-weapon-library]]'
- '[[concept-yihang-dual-triangle-core]]'
---

# AI 工具特性清单：原子化 Feature 分类框架

## 一句话

把 AI 工具拆成最小可操作技术特性（Feature），按层级和域分类，让 Agent 选型和能力评估有结构化依据而非凭工具名。

## 外部验证

Truman 的 Feature 思维——"可操作的原子化的最小技术单位，拆完之后一共也就几十个特性"（口述稿 L1426-1427）——与全球工程趋势一致：
- Synaptiai 99 原子能力本体（8 层：感知→建模→推理→行动→安全→元→记忆→协调）
- MCP 生态 308 服务器、2797 工具、8 大功能域
- 中国移动九天"原子化+大闭环"框架

## 三层分类框架

### 第一层：通用 Feature 原子表（跨工具）

| 域 | 原子 Feature | 说明 | 代表工具 |
|:---|:---|:---|:---|
| 模型参数 | temperature、top_p、max_tokens | 控制随机性和输出长度 | 所有 LLM |
| 上下文工程 | 长上下文、RAG、长时记忆、上下文压缩 | 管理 AI 的工作记忆 | Claude/Kimi/GPT |
| 推理增强 | 思维链(CoT)、自我一致性、多轮辩经 | 提升复杂推理质量 | 所有 LLM |
| 外部能力 | 浏览器使用、代码执行、API 调用、文件读写 | AI 与外部世界交互 | Claude Code/Codex |
| 输入增强 | few-shot、约束、角色、输出格式 | 控制输入质量 | 所有 LLM |
| 输出控制 | JSON 模式、Function calling、结构化输出 | 控制输出格式 | GPT/Claude |
| 多模态 | 图像理解、语音输入/输出、视频分析 | 非文本交互 | GPT-4o/Gemini |
| 协作机制 | 多 Agent 并行、红蓝军对抗、投票收敛 | 多 AI 协同 | AutoGen/CrewAI |
| 记忆系统 | 会话记忆、持久记忆、分层记忆 | 跨会话状态保持 | Mem0/Chroma |
| 安全校验 | 幻觉检测、输出过滤、权限控制 | 安全边界 | Guardrails |

### 第二层：KDO 内部工具映射

| 工具 | 核心 Feature 组合 | KDO Agent 适用场景 |
|:---|:---|:---|
| Claude Code | 代码执行 + 长上下文 + 文件读写 + 浏览器 | 代码考古、架构分析 |
| Codex | 代码理解 + 结构化输出 | 代码模块分析 |
| Kimi Agent 集群 | 多 Agent 协作 + 长上下文 | 批量梳理、交叉验证 |
| DeepSeek API | 低成本 + 模型参数调优 | Agent CLI 日常运行 |
| GLM 5.2 | 多模态 + 中文优化 | 待测试 |

### 第三层：按 Agent 类型的 Feature 组合推荐

| Agent 类型 | 必需 Feature | 可选 Feature | 不需要的 |
|:---|:---|:---|:---|
| 画布教练 | 上下文工程 + 推理增强 + 输出控制 | 多模态 | 代码执行 |
| 代码考古员 | 代码执行 + 长上下文 + 文件读写 | 协作机制 | 多模态 |
| 复盘 Agent | 推理增强 + 记忆系统 + 输出控制 | 外部能力 | 代码执行 |
| HR Agent | 记忆系统 + 协作机制 + 推理增强 | 安全校验 | 多模态 |

## 失败模式

1. 分类太粗——Feature 聚合度太高，Agent 选型时没有区分度
2. 分类太细——维护成本爆炸，每次新工具发布都要更新
3. 只覆盖国外工具——国内 Kimi/智谱/豆包的特性体系不同，需要独立维护
4. 静态分类——工具迭代后 Feature 变化，分类过时
5. Feature 和 Skill 混淆——Feature 是原子能力，Skill 是封装后的工作流，不能混在一张表里

## 更新规则

- 新工具发布→只问"比现有工具多了哪几个 Feature"→增量更新
- 每季度全量复审一次
- Feature 过时标记 deprecated，不移除
