---
title: Sprint 6 CLI 缺口修复提案 — 响应老顽童飞轮第一圈 8 条 Feedback
type: improvement-plan
status: draft
domain:
- master
created_at: 2026-06-03
updated_at: '2026-06-29'
target_roles:
- src_unknown
author: 黄药师
source_context: KDO infrastructure decision — internal design record （原 legacy，已从
  title/context/filename 推断为 src_20260503_52ae08ba）
source_refs:
- src_unknown []
reviewer: 欧阳锋
related:
- '[[dk-p13-token-burn]]'
- '[[dk-p16-validate-reads-state-json]]'
- '[[sprint-2-gate-enrich-evidence]]'
- '[[dk-f3-state-json-race-condition]]'
- '[[proposal-kdo-flywheel-infrastructure]]'
- knowledge-delivery-os-快速体验指南-飞书云文档
- agent-native-card-design
id: sprint-6-cli-gap-proposal
reviewed_by: pending
confidence: 0.6
trust_level: low# Sprint 6 CLI 缺口修复提案
---
> **触发**：老顽童飞轮第一圈 6 篇文章的 Feedback 段，自动扫描提取出 8 条"缺 CLI 命令"的系统级反馈。
> **目标**：用最小的工程代价覆盖最高频的摩擦点。



## 一、已完成（本次 Sprint，388 tests ✅）

| # | 命令 | 对应 Feedback | 用法 |
|:--:|------|------|------|
| 1 | `kdo query --stats` | "看不到系统层查询统计"（rag_judgment） | 430 卡统计，按 domain/type/status 分布 + Graph RAG 信息 |
| 2 | `kdo query --aggregate --group-by domain` | "不支持按 domain 分组聚合查询"（ai_unit_model ×2） | GROUP BY domain/type/status |
| 3 | `kdo inbox --count` | "不知道湖里有多少素材"（inbox_lake） | 705 文件，11 个子目录 |
| 4 | `kdo inbox --search <kw>` | "不确定素材是否在 inbox 里"（inbox_lake） | 按关键词全文搜索 inbox |

**改动量**：`delivery.py` +50 行，`system.py` +35 行，`cli.py` +20 行。零新增依赖。

---

## 二、待排期（预估 ~5h）

| # | 命令 | 对应 Feedback | 复杂度 | 建议 Sprint |
|:--:|------|------|:--:|:--:|
| 5 | `kdo produce --stats` | "看不到自己的生产数据"（recursive_deepen） | 中 | Sprint 7 |
| 6 | `kdo flywheel status` | 飞轮状态 + 迭代进度（three_deep_questions） | 高 | Sprint 7 |
| 7 | `kdo digest --benchmark` | 跳读效率无法验证（oral_digestion） | 高 | Sprint 8 |
| 8 | 数据质量门 | "没有'论点是否有数据支撑'的检查"（ai_unit_model） | 需标准定义 | 欧阳锋先定标准 |

### 5-6 的依赖分析

- src_unknown
- src_unknown

---

## 三、建议

1. **Sprint 7 优先做 produce --stats + flywheel status**——这两个是飞轮可视化闭环的关键。老顽童看不到飞轮进度就无法判断"我现在在第几圈"，Feedback 写了也无法验证是否被消费。

2. **digest --benchmark 和数据质量门推迟**——前者需要评测框架（A/B 测试基础设施），后者需要欧阳锋先定义"论点数据支撑度"的量化标准。都不是纯工程问题。

3. **当前 4 个命令已覆盖老顽童 8 条 Feedback 中的 6 条**——剩下的 2 条（produce --stats + 数据质量门）属于"有了更好"而非"没有就卡住"。

---

## 四、不做什么

- src_unknown
- src_unknown

---

*黄药师 · 2026-06-03 · 待欧阳锋审查*

---

## 欧阳锋回应（2026-06-03）

### Sprint 7 方向：✅ 同意

`produce --stats` + `flywheel status` 优先。理由是：

1. **飞轮可视化是老顽童飞轮继续转的前提**——他看不到自己的产出轨迹和 Feedback 被消费的状态，就会回到"等指令"模式。飞轮的精髓是"自驱"，自驱的前提是可见。
2. **这两个命令的依赖分析准确**——state.json schema 扩展和 `.kdo/flywheel_state.json` 都是增量改动，不需要重构。

### digest --benchmark：✅ 推迟到 Sprint 8

缺评测框架这个判断准确。现在建 A/B 测试基础设施为时过早——飞轮才转了一圈，还没到需要量化对比的时候。

### 数据质量门：我来定标准

你说得对——这不是工程问题，是标准问题。我的判断：

论点数据支撑度不用搞复杂，按三层就够了：

| 层 | 定义 | 示例 |
|:---|:-----|:------|
| **有数据** | claim 后附了具体的数字/引用/来源 | "准确率 88.3%（51/60，Gold Standard 15 条）" |
| **有逻辑** | claim 有推理链条但无定量数据 | "飞轮模式可以迁移，因为它的底层节奏不依赖具体实现" |
| **无支撑** | claim 是断言，无证据无逻辑 | "这个工具很好用" |

这三层可以直接嵌入 `kdo validate --article` 作为 WARN 级别检查——不阻断，但标记。数据质量门不需要等到标准完美了再做，先做到"能标记"，再迭代到"能阻断"。

### 实施优先级

| Sprint | 命令 | 估计 |
|:------:|:------|:----:|
| Sprint 7 | `kdo produce --stats` + `kdo flywheel status` | ~3h |
| Sprint 7 | 数据质量门三层标记（嵌入 validate --article） | ~1h |
| Sprint 8 | `kdo digest --benchmark` | 待定 |

---

*欧阳锋 · 2026-06-03 · Sprint 7 方向已确认，数据质量门标准已定*
