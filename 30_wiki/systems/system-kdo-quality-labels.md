---
id: "system-kdo-quality-labels"
title: "KDO 卡片质量标签体系使用指南"
type: "system"
domain:
  - "kdo"
status: "enriched"
confidence: 0.85
difficulty: "intermediate"
language: "zh-CN"
created_at: 2026-06-30T14:17:42+00:00
updated_at: 2026-06-30T14:17:42+00:00
author: "老顽童"
reviewed_by: "pending"
source_refs:
  - "00_inbox/AI-study/0071Vikki战队-2群 · 认知精华提炼.md"
  - "00_inbox/AI-study/0017大馨战队 · 短视频内容拆解方法论精华提炼.md"
query_triggers:
  - KDO 卡片质量标签怎么用
  - 怎么给卡片打标签
  - quality_labels 字段含义
  - insight hypothesis actionable quotable principle cited quality validated 区别
  - 如何用标签筛选卡片
aliases:
  - quality-labels
  - 卡片质量标签
  - KDO quality_labels
tags:
  - "#scene/system-design"
  - "kdo"
related:
  - "[[framework-brand-three-degree]]"
  - "[[framework-yitang-research-quality-gate]]"
  - "[[model-quality-four-levels]]"
  - "[[business-formula-to-kdo-card-quality]]"
pipeline:
  - "confidence-draft"
---

# KDO 卡片质量标签体系使用指南

> **Burn line**: 标签不是为了分类，而是为了让人和 Agent 在几千张卡片里，3 秒内判断"这张卡值不值得看、能不能用、可不可信"。

## 为什么需要质量标签

30_wiki 卡片数量快速增长后，出现三个问题：

1. **检索噪音大**：搜一个关键词出来 50 张卡，不知道哪张是实战验证过的，哪张还只是假设。
2. **审查成本高**：欧阳锋终审时，需要快速判断一张卡的成熟度。
3. **生产标准不统一**：老顽童产卡时，不清楚哪些卡片应该被优先打磨，哪些可以先放 draft。

质量标签把"这张卡是什么"和"这张卡有多好"分开描述：
- `tags`：自由标签，描述主题、场景、来源
- `quality_labels`：受控标签，描述内容类型和质量层级

## 标签体系

### 内容类型维度（来自 Vikki 五标签）

| 标签 | emoji | 含义 | 判断标准 |
|:---:|:---:|:---|:---|
| `insight` | 💡 | 有新洞察 | 提出了反常识判断、新框架或新因果链 |
| `hypothesis` | 🎯 | 待验证判断 | 明确标注为假设、confidence ≤ 0.70 或 status = draft |
| `actionable` | ✅ | 可执行步骤 | 有明确操作清单、 checklist、下一步动作 |
| `quotable` | 🔥 | 高传播性表述 | 有金句、burn line、可独立引用的核心判断 |
| `principle` | ❤️ | 解释因果机制 | 解释"为什么"而非"怎么做"，有底层逻辑 |

### 质量层级维度（来自大馨品牌三度）

| 标签 | 含义 | 判断标准 |
|:---:|:---|:---|
| `cited` | 被多次引用 | related 中有 ≥3 个真实 wikilink |
| `quality` | 审查质量高 | status = reviewed/stable 且 confidence ≥ 0.80 |
| `validated` | 有实战验证 | source_refs 中有非 pending/unknown 的真实来源 |

## 标签判定规则

### 自动判定（由 `label-quality-migrate.py` 执行）

```python
# cited: related 中 ≥3 个真实 wikilink
# quality: reviewed/stable + confidence ≥ 0.80
# validated: source_refs 中有真实来源
# actionable: type = tool/case
# principle: type = framework/concept
# hypothesis: draft + confidence ≤ 0.70
# insight: framework + reviewed
# quotable: 不自动判定，需人工判断
```

### 人工判定场景

| 标签 | 谁决定 | 依据 |
|:---:|:---|:---|
| `quotable` | 作者或审查者 | 是否有 burn line、金句或适合单独引用的判断 |
| `insight` | 作者或审查者 | 是否提出了真正的反常识洞察（不仅符合自动规则） |
| 其他 | 自动 + 人工抽检 | 自动规则给出初判，人工抽检 10% |

## 在 frontmatter 中的写法

```yaml
quality_labels:
  - insight
  - actionable
  - validated
```

规则：
- 只使用上面 8 个受控标签
- 每个标签单独一行，用 `-` 列表
- 不要和 `tags` 混淆：`tags` 可以自由写主题词

## 使用场景

### 场景 1：老顽童生产时自检

写完一张卡后，问自己：
- 这张卡是可操作的（actionable）还是讲因果的（principle）？
- 有没有真实来源支撑（validated）？
- 值不值得被其他卡片引用（cited）？
- 有没有一句能单独传播的话（quotable）？

### 场景 2：欧阳锋终审时快速判断

- 同时有 `quality` + `validated`：优先 deep 审查
- 只有 `hypothesis`：降低审查深度，标记为待验证
- 有 `actionable` 但无 `validated`：要求补充 source_refs 或标注为经验断言

### 场景 3：查询过滤

当前可用命令：

```bash
# 查看所有带 quality_labels 的卡片
python 90_control/scripts/label-quality-migrate.py --dry-run

# 按单个标签过滤
kdo query --label actionable

# 按多个标签同时过滤（AND 关系）
kdo query --label actionable --label cited

# 查看所有标签及其卡片数
kdo query --list-labels

# 临时兼容：用 grep 过滤
rg "^  - actionable$" 30_wiki -g "*.md" -l
```

## 标签组合示例

| 组合 | 含义 | 典型卡片 |
|:---|:---|:---|
| `insight` + `principle` + `quality` | 高质量洞察型框架 | `framework-yitang-three-ring-ability-focus` |
| `actionable` + `validated` | 可执行且有来源的工具/案例 | `tool-yitang-feedback-self-check` |
| `hypothesis` | 待验证的新判断 | 新 domain 早期 draft |
| `cited` + `quality` + `validated` | 知识库核心资产 | 高频引用的 reviewed framework |
| `quotable` + `insight` | 适合传播的金句卡 | burn line 特别锋利的 concept |

## 常见误用

| ❌ 错误 | ✅ 正确 |
|:---|:---|
| 把 `quality_labels` 当自由标签用 | 只使用 8 个受控标签 |
| 每张卡都贴满标签 | 一张卡通常 2-4 个标签，标签必须能被内容支撑 |
| 把 `validated` 当成"有 source_refs" | `validated` 要求 source_refs 是真实来源，不是 pending/unknown |
| 忽略 `quotable` | 每张优质卡片尽量提炼 1 句 burn line，争取 `quotable` |

## 与其他质量机制的关系

| 机制 | 作用 | 区别 |
|:---|:---|:---|
| `quality_labels` | 快速描述卡片类型和质量 | 受控标签，机器可读 |
| `confidence` | 作者对内容正确性的主观置信度 | 0-1 数值 |
| `trust_level` | 来源可信度 | high/medium/low |
| `status` | 卡片生命周期 | draft/enriched/reviewed/stable/deprecated |
| `kdo lint` | 机械质量检查 | 检查格式、链接、section |
| 欧阳锋终审 | 内容深度审查 | 人工判断 |

## Synthesis

| 关系 | 目标节点 | 说明 |
|---|---|---|
| 理论来源 | [[framework-brand-three-degree]] | 品牌三度（知名度/美誉度/信任度）映射为 cited/quality/validated |
| 方法来源 | `0071Vikki战队-2群 · 认知精华提炼.md` | Vikki 五标签（💡🎯✅🔥❤️）映射为 insight/hypothesis/actionable/quotable/principle |
| 质量把关 | [[framework-yitang-research-quality-gate]] | 质量标签是质量门禁的输入信号之一 |
| 卡片成熟度 | [[model-quality-four-levels]] | 质量标签帮助判断卡片处于哪个成熟度层级 |
| 生产标准 | [[business-formula-to-kdo-card-quality]] | 质量标签把"好卡片"的定义从感觉变成可检查的标准 |

## Action Triggers

| 触发场景 | 第一个动作 | 成功指标 |
|---|---|---|
| 新产一张卡 | 写完后根据内容选 2-4 个 quality_labels | frontmatter 完整，标签有内容支撑 |
| 批量标注历史卡片 | 跑 `python 90_control/scripts/label-quality-migrate.py --dry-run` | 无异常，标签分布合理 |
| 审查任务 | 先看 `quality_labels`，再决定审查深度 | 高 quality + validated 优先 deep |
| 检索知识 | 先用标签过滤，再用关键词搜索 | 找到目标卡片的时间缩短 |

## Open Questions

1. `quotable` 是否应该有更客观的判定标准（如被其他卡片引用的次数）？
2. `cited` 的阈值 3 个 wikilink 是否合理？是否应该按 domain 调整？
3. 质量标签是否需要定期重新计算（如 confidence 变化、related 更新后）？

## 来源

- `00_inbox/AI-study/0071Vikki战队-2群 · 认知精华提炼.md`（Vikki 五标签）
- `00_inbox/AI-study/0017大馨战队 · 短视频内容拆解方法论精华提炼.md`（品牌三度）
- `90_control/scripts/label-quality-migrate.py`（迁移脚本，黄药师）
