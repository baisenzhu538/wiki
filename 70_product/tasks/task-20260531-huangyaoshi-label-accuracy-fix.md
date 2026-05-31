---
id: auto-label-accuracy-baseline-vs-gold-standard
title: "Auto-label 准确率基线 vs Gold Standard：34.8%（47/135）"
type: evaluation
status: draft
domain:
  - master
created_at: 2026-05-31
updated_at: 2026-05-31
target_roles:
  - 黄药师（Builder）
reviewer: 欧阳锋（Architect）
related:
  - gold-standard-manual-labels
  - kdo-15-dimension-label-spec
---

# Auto-label 准确率基线 vs Gold Standard

> **测试方式**：欧阳锋手工标注的 15 条 Gold Standard chunk → `auto_label_chunk()` 管线（LLM: Kimi）→ 逐维度比对
> **测试脚本**：`_verify_gold_standard.py`
> **原始数据**：`60_feedback/data-quality/label-results/gold-standard-verify.json`

---

## 总体结果：34.8%（47/135）

远低于目标 85%。但需要拆开看。

---

## 分维度准确率

### ✅ 核心 4 维（管线实际在标的）：~75%

| 维度 | 准确率 | 错误模式 |
|:-----|:------:|---------|
| `chunk_type` | 11/15 = **73%** | claim ↔ cross_reference 混淆、definition ↔ procedure 混淆 |
| `method_family` | 12/15 = **80%** | thinking-tool ↔ decision-framework 偶尔误判 |
| `audience` | 10/15 = **67%** | manager→general（低估受众层级）、developer→general |
| `perspective` | 12/15 = **80%** | 稳定，但偶尔丢 general 值 |

**这 4 维合计 75%（45/60）。如果只算这 4 维，离 85% 差 10 个百分点——主要是 audience 拉低了。**

### ❌ 缺标的 5 维（全 0%）

| 维度 | 状况 | 根因 |
|:-----|:-----|------|
| `platform` | 15/15 `<missing>` | 管线激活维度不足，platform 未被选入候选 |
| `confidence` | 15/15 `<missing>` | 质量组维度不在 pre-screen 候选范围 |
| `prerequisite_knowledge` | 15/15 `<missing>` | 同上 |
| `expiry` | 15/15 `<missing>` | 同上 |
| `usage_depth` | 15/15 `<missing>` | 同上 |

**这 5 维不是"标错了"，是"根本没标"。** 管线目前只激活了检索组+视角组的部分维度，质量组和价值组完全没有进入标注流程。

---

## 需要黄药师做的两件事

### 任务 A：把前 4 维推到 85%（调 prompt）

当前的前 4 维准确率 75%，差 10 个百分点。

**主要问题在 audience**：
- `manager`→`general` 出现 3 次——内容明显在讲团队决策，但 AI 选了最安全的 general
- `developer`→`general` 出现 1 次——技术口述内容被降级为通用

**建议**：在 `LABEL_PROMPT` 中加强 audience 判断的指引，告诉 LLM "不要默认选 general，仔细看内容的目标读者是谁"。

**验证方式**：跑这个脚本就能出结果——
```powershell
python _verify_gold_standard.py
```

### 任务 B：激活质量组和价值组维度（改代码）

5 个维度 `<missing>` 的原因是 **pre-screen 阶段从来没把这些维度的值送入候选列表**。需要检查：

1. `tag-registry.yaml` 中 quality / value 组的 `includes` 描述是否足够触发 bigram 匹配
2. `prescreen_chunk()` 的 `min_score=0.15` 是否对质量组阈值太高
3. 是否需要给质量组/价值组加**强制注入**——即使 bigram 分数不够，也至少把 domain 配套的 quality 维度送入 LLM 候选

### 任务 C：萃取器升级（LLM 精提取）

见 `[[30_wiki/decisions/fix-dark-knowledge-extractor-llm.md]]`。

把 `extract_dark_knowledge.py` 从纯 regex 升级为 regex 预筛 + LLM 精提取（+~80 行）。

---

## 任务优先级

| 优先级 | 任务 | 估时 |
|:------:|:-----|:----:|
| **P0** | 任务 A：调 audience prompt → 前 4 维推到 85% | ~30min |
| **P1** | 任务 B：激活质量组/价值组标注 | ~1h |
| **P2** | 任务 C：萃取器 LLM 升级 | ~1h |

全部完成后一起通知欧阳锋复审。

---

## 验证脚本用法

```powershell
cd C:\Users\Administrator\Desktop\wiki
python _verify_gold_standard.py
```

输出会自动写入 `60_feedback/data-quality/label-results/gold-standard-verify.json`。

---

*欧阳锋 · 2026-05-31*
