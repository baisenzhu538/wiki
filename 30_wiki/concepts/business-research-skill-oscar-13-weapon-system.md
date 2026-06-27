---


id: business-research-skill-oscar-13-weapon-system
created_at: 2026-05-04
domain:
- src_unknown
review_date: 2026-05-04
reviewed_by: 黄药师
source_refs:
- src_20260614_40afd886-theme-finance-legal-business-summary
status: enriched
title: Business Research Skill — OSCAR 13武器体系 Claude Code 实现
trust_level: medium
type: concept
updated_at: '2026-06-16'
author: 老顽童
confidence: 0.7
related:
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
---# Business Research Skill — OSCAR 13武器体系 Claude Code 实现

> huanwang.org 出品，v2.1.0。将 一堂 OSCAR + 13 武器方法论完整编译为 Claude Code Skill 的生产级实现。

## Summary

[huanwang.org](https://huanwang.org) 发布的 `business-research` Skill 是将一堂调研方法论的 **OSCAR 五步法 + 13 武器体系** 工程化为 Claude Code 可执行 Skill 的完整方案。16 步全流程（Step 0-15），含 7 个 BLOCKING 质量门、15 项综合质量门机械检查、置信度加权公式、反向证据强制搜索、ACH 矩阵、Layer 1-3 深度自评、Pre-Mortem 事前验尸、Evaluator Agent 五维评审。输出符合 McKinsey 视觉规范的商业情报报告。

---

## Claims

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

## Critique

### 前提假设
- src_unknown
- src_unknown
- src_unknown
- src_unknown

### 边界与反例
- src_unknown
- src_unknown
- src_unknown

### 关键矛盾
- src_unknown
- src_unknown

### 可靠性
**整体：中高。** 方法论设计严密，质量门体系是同类 Skill 中最完整的。主要风险在执行层——用户跳过质量门的意愿、AI 的确认偏误、线下武器的执行率。

---

## Synthesis

- src_unknown
- src_unknown
- src_unknown
- src_unknown

### 互补与冲突
- src_unknown
- src_unknown

### 可迁移到 KDO 的改进
- src_unknown
- src_unknown
- src_unknown

### 不要用的场景

| 场景 | 为什么失效 | 替代方案 |
|------|-----------|---------|
| 把这个框架/方法当成绝对真理执行 | 任何方法论都是时间截面，它们假设未来会像过去一样发展 | 每次使用前先问"这个结论现在还成立吗？有没有新的反例出现？" |
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

- src_unknown
- src_unknown
- src_unknown
- src_unknown
## Output Opportunities

- src_unknown
- src_unknown

## Action Triggers

| 触发场景 | 第一个动作 | 成功指标 |
|---------|-----------|---------|
| 需要基于这份调研/框架做出关键决策前 | 先问自己"这个结论现在还成立吗？有没有新的反例出现？" | 每次使用前都能说出至少一个可能影响结论有效性的新变化因素 |
