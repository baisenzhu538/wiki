---

id: system-yitang-research-workflow
title: 调研工作流：从问题到报告的端到端执行路径
type: system
status: enriched
confidence: 0.9
trust_level: high
domain:
  - src_unknown
source_refs:
  - 30_wiki/frameworks/framework-yitang-oscar-research.md
  - 30_wiki/frameworks/framework-yitang-high-level-plan.md
  - 30_wiki/frameworks/framework-yitang-high-level-execution.md
  - 30_wiki/domains/yitang-research-domain-digest.md
  - 40_outputs/capabilities/skills/shared/research/SKILL.md
created_at: "2026-06-21"
updated_at: "2026-06-21"
author: 黄药师
reviewed_by: 欧阳锋
related:
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
diagnostic_signals:
  - framework_lens: 端到端工作流——7步从问题到报告
    follow_up_question: 你现在卡在哪一步？每一步的产出物是什么？
---

# 调研工作流：从问题到报告的端到端执行路径

> 接到调研任务 → 7 步走到可交付报告。每步有明确产出物、用到的卡片、可调用的 Skill。

## 总览

```
Step 1: 定目标    → OSCAR Plan   → 一句话调研目标 + 假设清单
Step 2: 缩范围    → OSCAR Plan   → 范围声明（含/不含）
Step 3: 列清单    → 武器库        → 信息需求清单 + 工具匹配
Step 4: 取情报    → 武器库/Skill  → 原始情报 + 来源标注
Step 5: 深挖验证  → 交叉验证/九层深挖 → 验证矩阵 + 置信度标注
Step 6: 归因总结  → AR Execute    → 调研结论 + 决策建议
Step 7: 质量自检  → 六维门禁      → 自检通过 → 交付
```

## 详细步骤

### Step 1: 定目标（15 分钟）

| 动作 | 工具 | 产出 |
|:--|:--|:--|
| 用一句话写下调研目标 | `framework-yitang-high-level-plan` | "我要验证 [假设]，以支持 [决策]" |
| 列出要验证的假设（≥3 条） | `yt-research-hypothesis-test` | 假设清单 |
| 写 Pre-Mortem："如果调研结果错了，最可能是因为什么？" | `framework-yitang-nine-layer-deep-dig` | 风险预判 |

**Skill 调用**：`/research <问题>` — 自动做意图分类

### Step 2: 缩范围（10 分钟）

| 动作 | 工具 | 产出 |
|:--|:--|:--|
| 明确时间范围（近X年） | — | 例如"2023-2025 财年" |
| 明确地域/竞品范围 | — | 例如"A 股上市连锁药房 ≥3 家" |
| 声明"不在本次范围内" | `concept-yitang-research-scope` | 排除清单 |

### Step 3: 列清单（20 分钟）

| 动作 | 工具 | 产出 |
|:--|:--|:--|
| 列出所有需要的信息 | `framework-yitang-research-weapon-system` | 信息需求清单 |
| 为每条信息匹配获取工具 | 域索引入口"工具索引" | 工具→信息映射 |
| 标注每条信息的必需程度（必须/最好有/锦上添花） | — | 优先级标注 |

**工具匹配决策**（引用 Step 3 映射表）：

| 信息类型 | 首选工具/Skill |
|:--|:--|
| 公司财务数据 | `/research-financial-report` |
| 行业市场规模 | `/research-industry-report` |
| 竞品公开信息 | `/research-web-scraping` |
| 行业专家观点 | `/research-expert-interview` |
| 验证已有结论 | `/research-cross-validation` |
| 设备/域名/身份 | `/research-osint` |

### Step 4: 取情报（核心执行阶段）

| 动作 | 工具 | 产出 |
|:--|:--|:--|
| 按 Step 3 的工具匹配执行 | 对应 Skill | 原始数据 + 来源标注 |
| 每条数据标注来源 URL + 获取时间 | — | 可追溯的来源链 |
| 初步标注置信度（高/中/低） | `framework-yitang-six-layer-cross-validation` | 置信度初标 |

**执行原则**：
- src_unknown
- src_unknown
- src_unknown

### Step 5: 深挖验证

| 动作 | 工具 | 产出 |
|:--|:--|:--|
| 关键结论 ≥2 个独立来源 | `/research-cross-validation` | 验证矩阵 |
| 矛盾数据标注 + 分析 | `framework-yitang-six-layer-cross-validation` | 分歧说明 |
| 需要深挖的线索 → 九层深挖 | `framework-yitang-nine-layer-deep-dig` | 深挖结论 |
| 单一来源结论降级标注 ⚠️ | — | 置信度修正 |

### Step 6: 归因总结

| 动作 | 工具 | 产出 |
|:--|:--|:--|
| 归一整合所有信息 | `framework-yitang-high-level-execution` | 综合结论 |
| 回答 Step 1 的假设（证实/证伪/不确定） | — | 假设验证结果 |
| 给出可操作的决策建议 | `framework-yitang-research-quality-gate` | 行动建议 |

### Step 7: 质量自检

| 动作 | 工具 | 产出 |
|:--|:--|:--|
| 逐维自检六维门禁 | `framework-yitang-research-quality-gate` | 自检表 |
| 不合格项回补 | — | 补充调研 |
| 全部通过 → 交付 | — | 最终报告 |

## 常见失败模式

| # | 症状 | 根因 | 修复 |
|:--|:--|:--|:--|
| 1 | 调研了 2 周，报告 50 页，说不出最关键的一个结论 | Step 1 目标没定 | 回 Step 1：用一句话说清调研目标 |
| 2 | 所有数字来自同一篇券商报告 | Step 4 信源单一 | 追加 2 个独立来源 |
| 3 | 报告被问"反面可能性呢？"答不上来 | Step 5 没做对立检验 | 做 Pre-Mortem |
| 4 | 调研结论是"需要更多研究" | Step 6 没归因 | 回到假设：到底验证了什么？ |
| 5 | Agent 全程只用 WebSearch | Step 3 工具匹配跳过 | 查域索引入口"工具索引" |

## 按调研类型分流

| 调研类型 | 重点步骤 | 预计耗时 |
|:--|:--|:--|
| 上市公司财报分析 | Step 1→3→4（财报）→5→6 | 2-4 小时 |
| 行业市场规模 | Step 1→3→4（行业报告）→5→6 | 3-6 小时 |
| 竞品深度拆解 | Step 1→3→4（爬虫+OSINT）→5→6 | 4-8 小时 |
| 专家访谈 | Step 1→3→4（访谈）→5→6 | 1-2 天 |
| 综合尽调 | 全流程 | 1-2 周 |

---

*黄药师 · 2026-06-21 · 调研域架构层整合*
