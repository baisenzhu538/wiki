---
name: research-ci-framework
description: CI竞争情报系统——Define→Gather→Analyze→Implement持续循环
version: 1.0.0
author: 黄药师
license: MIT
platforms: [cli, feishu]
metadata:
  hermes:
    tags: [CI, 竞争情报, KITs, KIQs, battlecard, 持续监控]
    related_skills: [research]
---

# CI 竞争情报系统

不是一次性调研——是持续的竞争情报循环。CIA 级别的 CI 运营模型：Define→Gather→Analyze→Implement。

## Constraints

<hard_limits>
- CI 系统是长期运营，不是一次性项目。设计时必须考虑可持续性
- KITs (Key Intelligence Topics) 必须从决策倒推，不能从"好查的"开始
- 情报分发必须有节奏——不是"有了就发"，是"决策者需要的时候有"
</hard_limits>

## 四阶段循环

```
Define ──→ Gather ──→ Analyze ──→ Implement
  ↑                                  │
  └──────────── 反馈 ────────────────┘
```

### Phase 1: Define（定义情报需求）

| 步骤 | 产出 | 要点 |
|:--|:--|:--|
| 识别决策者 | 谁用这份情报？ | 不是"公司"，是具体的人 |
| 定义 KITs | 3-5 个关键情报主题 | 从决策倒推，不是从数据倒推 |
| 转化 KIQs | 每个 KIT → 3-5 个可回答的问题 | KIQ 必须可验证 |
| 排优先级 | KIQ 优先级矩阵 | 紧急×重要 |

**KITs 示例**：
| KIT | 对应的决策 | KIQ 示例 |
|:--|:--|:--|
| 竞对定价策略 | 我们要不要降价？ | 竞对过去 12 个月的定价变化？触发因素？ |
| 竞对新品计划 | 我们的 roadmap 要不要调整？ | 竞对招聘什么岗位？专利申请什么？ |
| 行业监管变化 | 合规成本会增加多少？ | 哪些政策在征求意见？什么时候生效？ |

### Phase 2: Gather（收集）

| 来源类型 | 工具 | 频率 |
|:--|:--|:--|
| 公开信息 | WebSearch / Google Alerts | 日/周 |
| 财报/公告 | `/research-financial-report` | 季度 |
| 行业报告 | `/research-industry-report` | 月 |
| 招聘信息 | `/research-web-scraping` | 周 |
| 专利/商标 | 专利数据库 | 月 |
| 社交媒体 | Reddit / Twitter / 脉脉 | 周 |

### Phase 3: Analyze（分析）

| 技术 | 何时用 | Skill |
|:--|:--|:--|
| SWOT/五力 | 季度态势评估 | — |
| Key Assumptions Check | 每轮分析前 | `/research-sats` |
| Devil's Advocacy | 结论看起来太顺时 | `/research-sats` |
| Red Team | 预测竞对动作 | `/research-sats` |
| Battlecard 更新 | 竞对信息变更时 | 本 Skill |

### Phase 4: Implement（嵌入决策）

| 交付物 | 受众 | 频率 |
|:--|:--|:--|
| **CI 周报** | 产品/销售负责人 | 周 |
| **Battlecard** | 销售团队 | 月更新 |
| **深度分析** | CEO/战略 | 按需 |
| **预警** | 全员 | 触发式 |

## 决策树：我需要哪种 CI 能力？

| 需求 | 方案 | 复杂度 |
|:--|:--|:--|
| 偶尔看竞对 | 不用 CI，用 `/research` 单次调研 | 低 |
| 持续盯 1-2 个竞对 | CI Lite：周报 + Battlecard | 中 |
| 3+ 竞对 + 行业动态 | 完整 CI 系统 | 高 |
| 多市场 + 监管 + 技术 | CI 团队 + 专业工具 | 企业级 |

## 执行流程

```
输入：业务目标（win rate/定价/差异化/风险）
  ↓
Phase 1: Define → KITs(3-5) → KIQs(每个KIT 3-5个问题)
  ↓
Phase 2: Gather → 设计收集计划 → 分配频率和工具
  ↓
Phase 3: Analyze → 每轮用 SATs 检验 → 更新 Battlecard
  ↓
Phase 4: Implement → 周报/预警/深度分析 → 反馈 → 回 Define
```

## CI Lite 快速启动（最小可行）

如果不需要完整 CI 系统，从 CI Lite 开始：

1. 选 1 个最重要的竞对
2. 定义 3 个 KITs（定价/新品/客户）
3. 设置 5 个 Google Alerts
4. 每周五花 30 分钟写 CI 周报（5 条关键情报 + 1 条行动建议）

## 相关 wiki 卡片
- `framework-ci-operating-model`
- `tool-ci-define-phase`
- `tool-ci-implement-phase`
- `research-sats` — 分析阶段的 SATs 技术
- `research-web-scraping` — 收集阶段的爬虫工具
