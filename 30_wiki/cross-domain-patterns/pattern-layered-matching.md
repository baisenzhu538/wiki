---
id: pattern-layered-matching
title: 跨域模式：分层+匹配
type: pattern-index
status: draft
domain:
- methodology
- cross-domain
author: 黄药师
created_at: 2026-07-06
updated_at: 2026-07-06
confidence: 0.85
trust_level: high
related:
- "[[pattern-hypothesis-validation]]"
- "[[pattern-tool-vs-model]]"
- "[[yt-decision-y-model]]"
- "[[concept-yitang-model-system-boundary]]"
---

# 跨域模式：分层+匹配

> **一句话**：一堂方法论中反复出现的底层结构——先把问题按复杂度/深度/类型分层，再为每一层匹配不同的分析工具和决策方式。不是"用一个框架解释所有问题"，而是"不同层级的问题用不同层级的工具解决"。

## 模式本质

```
分层（Decompose）→ 匹配（Match）→ 逐层解决（Solve per layer）
```

**反模式**：不分层直接套框架 → 方法论堆叠（[[dk-yitang-methodology-stack-fallacy]]）

## 跨域出现位置

### 决策科学域

| 卡片 | 分层维度 | 匹配逻辑 |
|:---|:---|:---|
| [[yt-decision-abcd-model]] | 按决策类型分四层：A商业/B决策/C增长/D转化 | 不同类型→不同展开方式（参数化/多维度/业务公式/三要素） |
| [[yt-decision-depth-ladder]] | 按分析深度分层 | 浅层判断→常识即可，深层判断→需要Y模型完整循环 |
| [[yt-decision-width-method]] | 按视角宽度分层 | 单维度→多维度→跨域 |
| [[yt-decision-height-toolkit]] | 按工具复杂度分层 | 简单决策→checklist，复杂决策→完整框架 |
| [[yt-decision-consensus-iceberg]] | 按共识深度分层 | 表面共识→利益共识→价值观共识 |

**用法差异**：决策域的分层最"结构化"——每层有明确的参数、工具和验收标准。是分层+匹配模式最完整的表达。

### 需求分析域

| 卡片 | 分层维度 | 匹配逻辑 |
|:---|:---|:---|
| [[tool-iceberg-triangle-modeling]] | 需求冰山：表面需求→深层需求→需求本质 | 每层用不同的挖掘方法（访谈/观察/数据分析） |
| [[yt-demand-analysis-hiking-map]] | 需求分析全流程分层 | 不同阶段→不同工具（用户画像/JTBD/场景拆解） |

**用法差异**：需求域的分层是"深度导向"的——从可见到不可见。越深层的需求越难获取但越有价值。

### 用户/客户域

| 卡片 | 分层维度 | 匹配逻辑 |
|:---|:---|:---|
| [[tool-yitang-customer-segmentation-4step]] | 用户按价值/行为/需求分层 | 不同层级→不同服务策略 |
| [[yt-tob-customer-tiering]] | ToB 客户分层 | 入围型/一次性采购/周期性采购→不同销售投入 |
| [[yt-tob-solution-model]] | 解决方案按标准化×履约方式二维分层 | 标品+一次性=产品型，定制+持续=服务型 |

**用法差异**：用户/客户域的分层是"策略导向"的——分层的目的是资源分配（把最好的人力给最重要的客户）。

### 能力/认知域

| 卡片 | 分层维度 | 匹配逻辑 |
|:---|:---|:---|
| [[framework-yitang-jiefang-sixiang]] L0-L5 六层认知模型 | 按认知依据从低到高：自我想象→事实→常识→方法→本质→学科经典 | 不同层级→不同创新空间 |
| [[yt-five-step-method]] | 五步递进：需求→内核→单元模型→增长→壁垒 | 前一步不扎实不进下一步 |
| [[concept-yitang-model-system-boundary]] | 问题类型分层：决策型/执行型/探索型 | 不同问题类型→不同模型适用域 |

**用法差异**：能力域的分层是"进阶导向"的——不是所有人都需要爬到最高层。大多数商业问题在 L3/L4 就能解决。

### AI 协作域

| 卡片 | 分层维度 | 匹配逻辑 |
|:---|:---|:---|
| [[framework-yihang-dual-triangle-weapon-library]] | 人类三角（审美/体系/创造力）+ AI三角（场景/数据/基本功）| 六维按任务类型组合匹配 |
| [[framework-yihang-dual-triangle-ai-landing-five-steps]] | AI 落地五阶段 | 每阶段→不同的人机分工比例 |

**用法差异**：AI 协作域的分层是"互补导向"的——不是 AI 替代人，是找到各自最擅长的层。

### 销售域

| 卡片 | 分层维度 | 匹配逻辑 |
|:---|:---|:---|
| [[framework-yitang-scientific-sales-five-step]] | 销售五步法：用户分层→卖点→过程拆解→业绩管理→激励 | 每步→对应工具和方法 |
| [[tool-opc-sales-dialogue-assistant]] | 销售对话阶段分层 | 开场/需求挖掘/异议处理/促成→不同话术策略 |
| [[tool-agent-spec-yitang-sales-process-tracker]] | 销售阶段追踪 | 不同阶段→不同跟进频率和内容 |

**用法差异**：销售域的分层是"流程导向"的——分层的目的是在正确的时间做正确的动作。

## 为什么这个模式会跨域重复

1. **商业问题的本质是分层的**：从战略（做什么）到战术（怎么做）到执行（做多少），不同层需要不同的思维工具
2. **一堂方法论的核心假设**：没有万能框架。好的方法论不是给你一个锤子，是给你一个工具箱+一套"什么情况用什么工具"的判断力
3. **分层本身降低认知负荷**：先把复杂问题拆成可管理的层，再逐层解决，是认知科学验证过的最有效策略

## 识别信号

在阅读一张新卡时，如果出现以下结构，就是在使用分层+匹配模式：
- "根据...的不同，分为..." / "按...维度拆解"
- 表格的行是层级、列是匹配策略
- "不同...用不同..." 的句式
- 递进关系：先...再...然后...

## 与另外两个模式的关系

- 分层+匹配是 **骨架**（结构层）——定义"问题长什么样"
- [[pattern-hypothesis-validation]] 是 **引擎**（动力层）——定义"怎么确认每一层的判断是对的"
- [[pattern-tool-vs-model]] 是 **进化**（成长层）——定义"怎么从用别人的分层进化到建自己的分层"
