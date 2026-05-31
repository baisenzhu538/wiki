---
title: "黄药师：萃取器跑通全部月白口述稿 + 产出交付"
assigned_to: "黄药师（Builder）"
priority: "P1"
created_at: "2026-05-31"
reviewer: "欧阳锋"
status: "pending"
depends_on: ["extract_dark_knowledge.py A 版 ✅"]
blocks: ["老顽童 Phase 3 — 口述稿暗知识生产"]
---

# 黄药师：萃取器跑通全部月白口述稿 + 产出交付

## 背景

`extract_dark_knowledge.py` A 版脚本已就绪，在月白某篇口述稿上跑出了 52 条候选（效果对比：B+ 版 266 条 → A 版 52 条，降 81%）。但还有 2-3 篇口述稿未过萃取器。

你的目标：把全部月白口述稿跑完萃取器，产出整理成老顽童可直接取用的交付格式。

## 素材清单

| # | 文件 | 位置 | 萃取状态 |
|:-:|:-----|:-----|:--------:|
| 1 | AI设计-AI设计基础01.txt | `00_inbox/design/` | ⏳ 未萃取 |
| 2 | AI设计-AI设计师实操培训01.txt | `00_inbox/design/` | ⏳ 未萃取 |
| 3 | AI设计-文创案例设计课口述.txt | `00_inbox/design/` | ⏳ 未萃取 |

## 做法

### Step 1：确认当前产出

先确认 `60_feedback/data-quality/dk-candidates/` 下已有哪些候选 JSON，哪些口述稿还没跑。避免重复劳动。

### Step 2：逐篇跑萃取器

对每篇未处理的口述稿运行：

```bash
python extract_dark_knowledge.py --input "00_inbox/design/<文件名>.txt" --output "60_feedback/data-quality/dk-candidates/<文件名>-dk-candidates.json"
```

如有批量参数，直接跑批量。

### Step 3：验证产出

每篇跑完后检查：
- 候选总数是否在合理范围（参考基准：~50 条/篇）
- candidate 的字段完整（title、原始表述、使用场景、操作步骤草稿、type、score）
- score 高的前几条是否真的有价值（人眼确认）

### Step 4：通知老顽童可接

全部跑完后在 `laowantong-next-tasks.md` 尾部追加一行：

```
📦 月白口述稿暗知识候选已就绪 → 60_feedback/data-quality/dk-candidates/
   共 N 篇，约 M 条候选。按 score 从高到低取，预计产出 ~15 张暗知识卡。
```

## 产出格式要求

每篇口述稿输出一个 JSON 文件，每个 candidate 包含：

```json
{
  "id": "yb-{N}-{slug}",
  "title": "简短标题",
  "dk_type": "tool_usage | workflow | failure | insight",
  "原始表述": "直接引用原文片段",
  "使用场景草稿": "AI 初步提取的使用场景",
  "操作步骤草稿": "[OPERATION_NEEDS_HUMAN] 或 AI 提取的步骤",
  "score": 0.00,
  "score_breakdown": {"特异性": 0.00, "独特性": 0.00, "独立性": 0.00, "可操作性": 0.00}
}
```

**注意**：`操作步骤草稿` 字段如果 AI 提取不可靠，统一填 `[OPERATION_NEEDS_HUMAN]`，不要填破碎的原文碎片。

## 验收

| # | 验收项 | 判定 |
|:-:|:------|:----:|
| 1 | 全部月白口述稿跑完萃取器 | `60_feedback/data-quality/dk-candidates/` 下有 N 篇 JSON |
| 2 | 候选总数在合理范围 | 每篇 ~40-60 条，不是 200+ |
| 3 | score 高的前 5 条经人眼确认有价值 | 抽查通过 |

## 不做

- **不做** 进一步优化萃取器（已到 A 版，够用）
- **不做** 跑 Truman 口述稿（那是下一阶段）
- **不做** 给候选 JSON 加多维标注（那是 tag-registry v3 的事）

---

*欧阳锋 · 2026-05-31*
