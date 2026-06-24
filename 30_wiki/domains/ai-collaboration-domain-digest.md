---
id: ai-collaboration-domain-digest
title: 域摘要：AI 协作方法论（王欢 · Harness Engineering）
type: index
status: enriched
confidence: 0.85
trust_level: high
domain:
  - ai-collaboration
  - yitang
source_context: 王欢 AI 实践方法论——从"用好 AI"到"建 AI 系统"
source_refs:
  - 00_inbox/拆书会第208期：《AI 2041：预见未来二十年》逐字稿（完整版）.md
created_at: "2026-06-23"
author: 黄药师
reviewed_by: pending
related:
  - "[[five-step-domain-digest]]"
  - "[[yitang-research-domain-digest]]"
  - "[[strategy-domain-digest]]"
---

# 域摘要：AI 协作方法论

> 王欢 AI 实践方法论——从演员到导演，从任务到系统。
> 核心理念：人机协作不是在用好 AI，是在建一个 AI 能自己进化的系统。

## 核心定位

AI 协作域是 KDO 的 **执行引擎层**——它不定义"做什么"（战略/五步法/决策负责），而是定义"怎么做成"：

```
调用关系
├── 调研域   → AI 协作域提供多 Agent 并行调研
├── 需求域   → AI 协作域提供自动预验证
├── 五步法   → AI 协作域提供 Harness 七阶段构建
└── 决策域   → AI 协作域提供 OODA 闭环
```

## 核心框架（先读）

| 卡 | 一句话 |
|:--|:--|
| `concept-harness-cattle-not-pets` | 牲口而非宠物——每次迭代用全新 Generator 实例，不修复旧代码 |
| `concept-harness-scoring-anchors` | 评分锚定——1-5 分制 + 语义锚点，不用"感觉"衡量 |
| `framework-multi-agent-research-architecture` | 多 Agent 调研架构——三种模式的对比与选择 |
| `concept-mcp-protocol` | MCP 协议——Agent 调用外部工具的统一标准 |
| `framework-ai2041-critical-reading-os` | AI 2041 批判性认知操作系统——概率→具体的人→选择点 |
| `framework-ai-deconstruction-methodology` | 王欢三层拆书法——还原/审计/生长 |

## 批判性阅读（AI 2041）

| 卡 | 一句话 |
|:--|:--|
| `tool-ai-critical-reading-three-layers` | 三层拆书批判法——还原/审计/生长的操作清单 |
| `tool-tech-probability-80-filter` | 李开复 80% 概率过滤器——把无限焦虑收敛为有限准备 |
| `concept-ai-amara-law-business-judgment` | 阿马拉定律与商业判断校准——高估短期、低估长期 |
| `concept-ai-chair-determines-view` | 椅子决定视角——作者的利益位置、技术立场、时代局限决定其 AI 判断 |
| `concept-ai-neutrality-bias` | 中立的暴政——假装没有立场是最精明的立场 |
| `tool-ai-cross-reading-method` | 交叉阅读法——用 2-3 本立场相反的书对撞 |
| `tool-ai2041-source-verification-checklist` | AI 预测来源验证检查单——来源可信度五问 + 信息质量阶梯 |

## 算法伦理案例（AI 2041）

| 卡 | 一句话 |
|:--|:--|
| `case-compas-racial-bias` | COMPAS 再犯算法种族偏见——ProPublica 77.3% 数字与 Northpointe 辩护并置 |
| `case-apple-card-gender-bias` | Apple Card 信用额度性别争议——NYDFS 未违法结论与公众伤害并置 |
| `case-dutch-childcare-scandal` | 荷兰育儿补贴算法丑闻——26,000 家庭与内阁辞职 |
| `case-cambridge-novelists-survey` | 剑桥小说家对 AI 创作态度调查——97% 反对整本书的英国样本 |
| `case-chen-qiufan-ai-writing` | 陈楸帆对 AI 写作的态度转向——2017 拥抱到 2025 审慎 |

## AI 协作技能（Claude Code + Hermes 双可用）

| Skill | 用途 |
|:--|:--|
| `/ai-collaboration` | 总入口——自动路由到对应子 Skill |
| `/ai-collaboration-harness` | Harness 七阶段——从想法到 AI 产品 |
| `/ai-collaboration-bitcoe` | BITCOE 提示词框架——六个要素写出高质量 Prompt |
| `/ai-collaboration-ooda` | OODA 决策闭环——Observe/Orient/Decide/Act |
| `/ai-collaboration-gan` | GAN 三角色——生成器/判别器/合成器，多模型协作 |
| `/ai-collaboration-dev` | 三层开发架构——需求拆解→AI 开发→哨兵质检 |

## Tool 卡（Agent 自动化）

| 卡 | 用途 |
|:--|:--|
| `tool-agent-research-swarm` | Swarm 模式——多 Agent 自发协同与交叉验证 |
| `tool-agent-research-pipeline` | Pipeline 模式——OSCAR 五步的 Agent 实现 |
| `tool-agent-research-supervisor` | Supervisor 模式——一个 Agent 调度多个 Worker |
| `tool-agent-crawl4ai` | Crawl4AI——开源 AI 爬虫 |
| `tool-agent-firecrawl` | Firecrawl——LLM Web 抓取 API |
| `tool-agent-native-overview` | Agent 原生工具概览——2025-2026 新范式 |
| `tool-harness-adversarial-tester` | 对抗测试员——找到 Agent 的 bug |
| `tool-demand-agent-auto-verify` | L6 自动预验证——RAT 精品案例+受控开放验证 |
| `tool-demand-agent-case-match` | L4 案例匹配——历史摩擦矩阵 |
| `tool-demand-agent-multi-hypothesis` | L3 多假设并行——5 个诊断方向同时跑 |
| `tool-demand-agent-signal-substitute` | L5 信号替代——微观行为的非结构化数据分析 |
| `tool-demand-agent-signals` | L1-L2 信号聚合——不再"凭感觉问用户" |

## Concept 卡（原则与方法）

| 卡 | 核心观点 |
|:--|:--|
| `concept-candy-ai-as-collaborator` | AI 是协作者不是代写工具 |
| `concept-yitang-ai-research-10-assumptions` | 十项假设——人机协作的底层原则 |
| `concept-yitang-ai-research-human-loop` | 人机环——判断节点在哪里 |

## 暗知识

| 卡 | 一句话 |
|:--|:--|
| `dk-yitang-ai-research-prompt-craft` | AI 效果取决于人判断+提示词技巧 |
| `dk-yitang-research-ai-hallucination` | AI 幻觉——浅尝辄止 vs 双重验证 |

## 案例

| 卡 | 一句话 |
|:--|:--|
| `case-yitang-ai-time-management-coach` | AI 时间管理小助手：从产品验证到 Agent |

## 跨域桥接

| 目标域 | 桥接卡 | 关系 |
|:--|:--|:--|
| 调研域 | `yitang-research-domain-digest` | 13 个 Research Skill 是 AI 协作域的执行工具 |
| 五步法域 | `five-step-domain-digest` | Harness 七阶段是五步法在 AI 开发中的落地 |
| 战略域 | `strategy-domain-digest` | AI 产品战略需要 GAN + OODA 闭环 |

---

*黄药师 · 2026-06-23 · AI 协作域建制（老顽童 P0+P1 增补）*
*38 张卡 · 5 个 Skill · 3 个跨域桥接 · P0+P1 14/22 完成*
