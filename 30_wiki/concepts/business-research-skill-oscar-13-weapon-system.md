---
title: "Business Research Skill — OSCAR 13武器体系 Claude Code 实现"
type: concept
status: enriched
domain: ['yitang']
source_refs: []
created_at: "2026-05-04"
updated_at: "2026-05-04"
related:
  - "[[一堂调研武器库13招]]"
  - "[[一堂调研行动营-ai辅助系统式调研方法论]]"
  - "[[一堂-调研行动营启动_原文润色]]"
  - "[[kimi-深度调研集群方法论-deep-research-swarm]]"
  - "[[kdo-protocol]]"
tags:
  - "#yitang"
  - "#research"
  - "#business-analysis"
  - "#skill"
  - "#methodology"
  - "#oscar"
trust_level: high
reviewed_by: "黄药师"
review_date: "2026-05-04"
---

# Business Research Skill — OSCAR 13武器体系 Claude Code 实现

> huanwang.org 出品，v2.1.0。将 一堂 OSCAR + 13 武器方法论完整编译为 Claude Code Skill 的生产级实现。

## Summary

[huanwang.org](https://huanwang.org) 发布的 `business-research` Skill 是将一堂调研方法论的 **OSCAR 五步法 + 13 武器体系** 工程化为 Claude Code 可执行 Skill 的完整方案。16 步全流程（Step 0-15），含 7 个 BLOCKING 质量门、15 项综合质量门机械检查、置信度加权公式、反向证据强制搜索、ACH 矩阵、Layer 1-3 深度自评、Pre-Mortem 事前验尸、Evaluator Agent 五维评审。输出符合 McKinsey 视觉规范的商业情报报告。

---

## [Condense] 核心架构

### 16 步流程全景

| 阶段 | 步骤 | 内容 | 门 |
|------|------|------|:--:|
| 准备 | Step 0 | Preflight 用户确认 | 🔴 |
| | Step 1 | 假设构建与边界界定 (O+S) | 🔴 |
| | Step 2 | 武器决策表 13 行必填 (C) | 🔴 |
| 采集 | Step 3 | 在线信息采集（第一轮） | |
| | Step 4 | 子方向深度委托（→ deep-research） | |
| | Step 5 | 线下武器行动指南（第二轮） | |
| | Step 6 | 事实抽取与信源分级 | |
| 验证 | Step 7 | 假设验证与四态判定 | |
| | Step 8 | 反向证据强制搜索门 | 🔴 |
| 分析 | Step 9 | 竞争格局分析 (Goal Anchor) | 🔴 |
| | Step 10 | Layer 1-3 深度自评 (≥2.0) | 🔴 |
| | Step 11 | 交叉验证+置信度公式+Pre-Mortem | 🔴 |
| | Step 12 | 信息哨兵系统设计 | |
| 交付 | Step 13 | 15 项综合质量门 | 🔴 总闸 |
| | Step 14 | SCQA 专业报告生成 | |
| | Step 15 | Evaluator 独立评审 (≥21/25) | 🔴 |

### 五大核心机制

1. **假设驱动**：模糊问题 → 可证伪假设（致命/核心/辅助三级），致命假设不成立则方案推倒
2. **13 武器决策表**（BLOCKING）：每个武器标注 执行/跳过/线下 + ≥10字理由，标准调研 ≥7 武器，深度尽调 ≥10
3. **反向证据强制搜索门**：对抗确认偏误——每个 ✅ 致命假设强制执行 ≥3 条反向搜索，找到 L1/L2 反例则降级
4. **深度自评 Layer 1-3**：What（表面事实,1分）→ Why（原因机制,2分）→ So What（决策含义,3分），平均 < 2.0 禁止进入下一步
5. **置信度加权公式**：致命×0.5 + 核心×0.3 + 信源中位数/5×0.2 → ≥0.80 高 / 0.55-0.80 中 / <0.55 低。禁止拍脑袋

### 信源五级评分

| 级别 | 信源 | 基础权重 |
|:----:|------|:-------:|
| L1 | 年报/法院判决/政府统计/源码 | 5 |
| L2 | 学术论文/顶级券商/专家专访 | 4 |
| L3 | 财新/彭博/36氪深度 | 3 |
| L4 | 知乎高赞/论坛技术帖 | 2 |
| L5 | 微博/小红书/普通论坛 | 1 |

动态调整：时效近1月 +1 / 直接当事人 +1 / 利益冲突 -1 / 匿名 -0.5

---

## [Critique] 批判性评估

### 前提假设
- 假设用户能在 Step 0 清晰表述决策问题和假设。【可靠性：中】实际用户常处于"知道自己不知道"的阶段，Step 0 本身就是方法论中最难的一步
- 假设 AI Agent 能在 Step 11 自主执行 Pre-Mortem 并生成高质量反向假设。【可靠性：中】LLM 的内在确认偏误（系统倾向于同意用户而非挑战）与 Step 8 的反向搜索机制存在根本张力
- 假设 15 项质量门中的正则匹配规则覆盖所有情况。【可靠性：中高】机械检查可捕获明显违规，但无法评估推理质量
- 假设用户有执行线下武器（产品体验/面试/专家访谈）的意愿和能力。【可靠性：低】对大多数非专业调研者，线下武器的高门槛可能导致"13选5"变成"13选AI能做的5"

### 边界与反例
- **最适合**：有明确商业决策节点的调研（投融资、市场进入、竞品对标）
- **不适合**：纯探索性调研、学术文献综述、技术原理深度研究（应委托给 deep-research）
- **成本警告**：深度尽调模式（5 Agent 并行 + 250+ 次搜索）的 API 费用可能达数十至上百元

### 关键矛盾
- **"机械检查" vs "判断质量"**：15 项质量门偏向形式完整性而非实质推理质量。一篇"武器决策表 13 行完整但理由都是凑字数"的报告可以通过机械检查
- **"AI 负责加速 vs 人负责判断"** 的张力贯穿全程：方法论反复强调人做判断，但 16 步流程本身的复杂度可能让用户放弃判断而全盘接受 AI 输出

### 可靠性
**整体：中高。** 方法论设计严密，质量门体系是同类 Skill 中最完整的。主要风险在执行层——用户跳过质量门的意愿、AI 的确认偏误、线下武器的执行率。

---

## [Synthesis] 与 wiki 知识库的关联

- [[一堂调研武器库13招]] — 本 Skill 是 13 招的 **Claude Code 工程化实现**。13 招定义了"做什么"，本 Skill 定义了"怎么做+怎么验证"
- [[一堂调研行动营-ai辅助系统式调研方法论]] — OSCAR 五步法在两个体系中共源。本 Skill 的 Step 0-2 对应行动营的 O-S-C，Step 3-5 对应 A，Step 6-12 对应 R
- [[kimi-深度调研集群方法论-deep-research-swarm]] — Step 4 的委托机制直接与 deep-research 互操作。两者共享"多Agent并行+交叉验证"的认知前提
- [[kdo-protocol]] — 本 Skill 的质量门体系（7 BLOCKING + 15 项机械检查）可作为 KDO validate 阶段的参考

### 互补与冲突
- **互补**：一堂的行动营教"调研思维"，本 Skill 提供"调研机器"——思维+机器的组合形成完整能力
- **冲突**：一堂强调"行动中学习"（边做边学），本 Skill 强调"先设计再执行"（Step 0-2 不可跳过）。二者的"规划 vs 涌现"张力与 KDO Protocol 中的同一矛盾形成三级对应

### 可迁移到 KDO 的改进
- 质量门 15 项清单模式 → KDO 的 `kdo validate` 命令设计
- 置信度加权公式 → KDO concept card 的 `trust_level` 计算
- Step 4 委托机制 → KDO Research 子任务分派协议

## Skill 文件清单

安装路径：`~/.claude/skills/business-research/`

| 文件 | 大小 | 作用 |
|------|------|------|
| `SKILL.md` | 41KB | 主文件，16 步完整流程 |
| `references/analysis-frameworks.md` | 4.5KB | 企业/竞品/行业/项目 4 套分析框架 |
| `references/bias-checklist.md` | 2.6KB | 5 类认知偏误防御清单 |
| `references/ach-methodology.md` | 2.3KB | ACH 竞争假设矩阵 |
| `references/market-sizing.md` | 3.2KB | 三角验证 + 费米估算 + 单位经济基准 |
| `references/databases-index.md` | 4.5KB | 11 类数据库索引 |
| `references/ci-platforms.md` | 2.1KB | CI 平台选型 |
| `references/research-principles.md` | 4.6KB | AI 调研 10 原则 + 4 层使用深度 |
| `references/report-guide.md` | 7.5KB | 配图/图表/Takeaway Title 规范 |
| `references/style-guide.md` | 7.5KB | 完整视觉规范 |
| `references/weapon-action-templates.md` | 4.6KB | 线下武器行动模板 |
| `templates/report-structure.md` | 11.2KB | 报告结构模板 |
| `templates/fact-card.md` | 2.1KB | 事实卡片模板 |
| `templates/weapon-checklist.md` | 2.6KB | 武器检查清单模板 |

## Open Questions

- Step 13 的 15 项机械检查中，正则匹配规则对中文报告的适配程度？
- Step 4 委托 deep-research 的 JSON 契约在实际使用中的通过率？
- Evaluator Agent (Step 15) 的 CLASSic 五维评分与人类评审的相关性如何？
- 线下武器执行率低（多数用户只使用 AI 可直接执行的 5-6 个武器）是否是方法论的结构性短板？

## Output Opportunities

- Code: 封装 `kdo research` 命令，对接本 Skill 的 Step 0-15 流程
- Capability: KDO Research Agent — 自动选择 business-research vs deep-research 路由
