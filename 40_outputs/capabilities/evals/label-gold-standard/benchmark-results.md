---
title: "Auto-Label 准确率轨迹"
type: reference
status: stable
created_at: 2026-06-01
updated_at: 2026-06-01
---

# Auto-Label 准确率轨迹

> 每次修改 prompt 或管线后，跑一次 `_verify_gold_standard.py`，记录结果到本文件。

## 2026-05-31 — v10（最终版）

| 维度 | 准确率 | 基线 |
|------|:--:|:--:|
| chunk_type | 93% (14/15) | 7% |
| method_family | 93% (14/15) | 7% |
| audience | 87% (13/15) | 40% |
| perspective | 80% (12/15) | 53% |
| **总(4维)** | **88.3% (51/60)** | 26.7% |
| confidence | 新增 | — |
| platform | 新增 | — |
| expiry | 新增 | — |
| prerequisite_knowledge | 新增 | — |
| usage_depth | 新增 | — |

**模型**：kimi-for-coding (DeepSeek V4)
**温度**：0.01
**策略**：中文 few-shot (7例) + card上下文 + 9维单选

## 2026-06-01 — v10 9维全量 baseline

| 维度 | 准确率 | 状态 |
|------|:--:|:--:|
| chunk_type | 87% (13/15) | ✅ |
| method_family | 93% (14/15) | ✅ |
| audience | 87% (13/15) | ✅ |
| perspective | 93% (14/15) | ✅ |
| confidence | 53% (8/15) | ❌ 需调优 |
| platform | 100% (15/15) | ✅ |
| expiry | 100% (15/15) | ✅ |
| prerequisite_knowledge | 67% (10/15) | ⚠️ 边缘 |
| usage_depth | 100% (15/15) | ✅ |
| **总(9维)** | **86.7% (117/135)** | ✅ **PASS** |

**分析**：9 维总准确率 86.7%，超 85% 目标。confidence（53%）是主要瓶颈——LLM 对"多源验证 vs 单源强证据"的判断不精准。prerequisite_knowledge（67%）有 5 例边界混淆。但两者都是质量辅助维度，不影响核心 4 维的检索和分类用途。

**结论**：门禁通过。confidence 和 prerequisite_knowledge 的调优作为 P2 优化项，不阻塞 Pilot 启动。

## 迭代历史

| 版本 | 日期 | 改动 | chunk_type | method_family | audience | perspective | **总** |
|:--:|------|------|:--:|:--:|:--:|:--:|:--:|
| v1 | 05-31 | 基线: 英, 45候选 | 7% | 7% | 40% | 53% | 26.7% |
| v5 | 05-31 | 中, 单选, 5 few-shot | 73% | 47% | 80% | 73% | 68.3% |
| v6 | 05-31 | +eval示例 | 80% | 60% | 80% | 67% | 71.7% |
| v7 | 05-31 | +裁决规则 | 87% | 53% | 73% | 80% | 73.3% |
| v8 | 05-31 | +thinking-tool区分 | 80% | 67% | 73% | 87% | 76.7% |
| v9 | 05-31 | +developer示例 | 87% | 73% | 93% | 87% | 85.0% |
| **v10** | **05-31** | **+card上下文 +5质量维** | **93%** | **93%** | **87%** | **80%** | **88.3%** |

## 变更记录模板（每次记录用）

```
## YYYY-MM-DD — v{N}

| 维度 | 准确率 | 变化 |
|------|:--:|:--:|
| chunk_type | X% (n/15) | +/-Y% |
...

**模型**：
**改动**：
**新增错误模式**：
```
