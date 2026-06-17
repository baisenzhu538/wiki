# KF-021 收尾：33 张 content 卡 source 缺失处理报告

**处理时间**：2026-06-17  
**负责人**：老顽童  
**处理原则**：
- 移除 `source_refs` 中不存在于 `10_raw/sources/` 或 `00_inbox/` 的项；
- 移除 `source_refs` 中非 source 的条目（如书目字典项、非 source 字符串）；
- 不修改卡片 body；
- 清理后 `source_refs` 为空的卡，status 降为 `draft`，confidence 设为 0.65，trust_level 设为 `low`；
- 清理后 `trust_level=high` 但 source 仅剩 1 个的卡，trust_level 降为 `medium`。

## 变更统计

- 处理目标卡：33 张
- 降级为 draft：18 张
- 保持/调整 trust 后保留 enriched/stable：15 张

## 逐卡变更明细

| 卡片 ID | 原 status | 新 status | 原 refs | 新 refs | 动作 | 移除项 |
|:---|:---|:---|---:|---:|:---|:---|
| `case-yitang-tob-grinding-machine` | enriched | enriched | 3 | 2 | clean/remove_invalid | src_20260616_0e684368 |
| `yt-lean-beauty-store-conversion` | enriched | draft | 3 | 0 | downgrade_draft | src_20260616_b1e25c49; src_20260616_59f708ea; src_20260616_e66bd149 |
| `yt-lean-daily-chemical-mvp` | enriched | draft | 3 | 0 | downgrade_draft | src_20260616_b1e25c49; src_20260616_7dc80216; src_20260616_59f708ea |
| `yt-lean-flower-mom-group-leader` | enriched | draft | 3 | 0 | downgrade_draft | src_20260616_b1e25c49; src_20260616_7dc80216; src_20260616_6c8b240b |
| `yitang-huazong-ama-by-industry` | stable | stable | 1 | 1 | clean/remove_invalid | - |
| `yitang-huazong-ama-summary` | stable | stable | 1 | 1 | clean/remove_invalid | - |
| `yt-entrepreneur-lean-validation` | enriched | enriched | 4 | 1 | clean/remove_invalid | src_20260616_b1e25c49; src_20260616_7dc80216; src_20260616_6c8b240b |
| `yt-lean-daily-probability-decision` | enriched | draft | 3 | 0 | downgrade_draft | src_20260616_b1e25c49; src_20260616_59f708ea; src_20260616_e66bd149 |
| `yt-lean-essence` | enriched | draft | 3 | 0 | downgrade_draft | src_20260616_b1e25c49; src_20260616_7dc80216; src_20260616_6c8b240b |
| `yt-tob-cash-flow` | enriched | draft | 2 | 0 | downgrade_draft | src_20260616_0e684368; src_20260616_5f991553 |
| `yt-tob-revenue-is-customer-cost` | enriched | draft | 2 | 0 | downgrade_draft | src_20260616_0e684368; src_20260616_5f991553 |
| `yt-tob-sales-unit-model` | enriched | enriched | 4 | 2 | clean/remove_invalid | src_20260616_0e684368; src_20260616_5f991553 |
| `concept-minto-pyramid-principle` | enriched | enriched | 3 | 1 | clean/remove_invalid | {'Minto, B. (2009). *The Pyramid Principle': 'Logic in Writing and Thinking*. 3rd ed. FT Press.'}; Rasiel, E. (1999). *The McKinsey Way*. McGraw-Hill. |
| `yt-lean-assumption-prioritization` | enriched | draft | 4 | 0 | downgrade_draft | src_20260616_b1e25c49; src_20260616_6c8b240b; src_20260616_e66bd149; src_20260616_7dc80216 |
| `yt-lean-assumption-verification-3means` | enriched | draft | 3 | 0 | downgrade_draft | src_20260616_b1e25c49; src_20260616_7dc80216; src_20260616_6c8b240b |
| `yt-lean-b2b-b2c-hardware-content-testing` | enriched | draft | 3 | 0 | downgrade_draft | src_20260616_b1e25c49; src_20260616_59f708ea; src_20260616_e66bd149 |
| `yt-lean-consumer-deep-experience-testing` | enriched | draft | 2 | 0 | downgrade_draft | src_20260616_b1e25c49; src_20260616_59f708ea |
| `yt-lean-false-model-ai` | enriched | draft | 3 | 0 | downgrade_draft | src_20260616_b1e25c49; src_20260616_7dc80216; src_20260616_6c8b240b |
| `yt-lean-growth-stage-gate` | enriched | draft | 3 | 0 | downgrade_draft | src_20260616_b1e25c49; src_20260616_7dc80216; src_20260616_6c8b240b |
| `yt-lean-qualitative-quantitative-research` | enriched | draft | 2 | 0 | downgrade_draft | src_20260616_b1e25c49; src_20260616_6c8b240b |
| `yt-tob-barriers` | enriched | enriched | 4 | 2 | clean/remove_invalid | src_20260616_0e684368; src_20260616_5f991553 |
| `yt-tob-core-characteristics` | enriched | draft | 2 | 0 | downgrade_draft | src_20260616_0e684368; src_20260616_5f991553 |
| `yt-tob-customer-tiering` | enriched | draft | 2 | 0 | downgrade_draft | src_20260616_0e684368; src_20260616_5f991553 |
| `yt-tob-demand-metrics` | enriched | enriched | 3 | 1 | clean/remove_invalid | src_20260616_0e684368; src_20260616_5f991553 |
| `yt-tob-demand-scenarios` | enriched | draft | 2 | 0 | downgrade_draft | src_20260616_0e684368; src_20260616_5f991553 |
| `yt-tob-growth-channel` | enriched | enriched | 3 | 1 | clean/remove_invalid | src_20260616_0e684368; src_20260616_5f991553 |
| `yt-tob-product-kernel` | enriched | draft | 2 | 0 | downgrade_draft | src_20260616_0e684368; src_20260616_5f991553 |
| `yt-tob-solution-model` | enriched | enriched | 3 | 1 | adjust_trust | src_20260616_0e684368; src_20260616_5f991553 |
| `yt-tob-unit-model` | enriched | enriched | 3 | 1 | adjust_trust | src_20260616_0e684368; src_20260616_5f991553 |
| `yt-tob-customer-sabc` | enriched | enriched | 3 | 1 | adjust_trust | src_20260616_0e684368; src_20260616_5f991553 |
| `互联网医院项目` | active | verified_valid | 3 | 3 | no_change | - |
| `诊所O2O项目` | active | verified_valid | 1 | 1 | no_change | - |
| `鑫港湾HIS项目` | active | verified_valid | 1 | 1 | no_change | - |

## 验证结果

```bash
python 90_control/scripts/kcard-quality-gate.py
```

结果：

```text
total=1193, p0=0, p1=18, clean=1175, yaml_error=0
```

- **P0 = 0**：无阻塞问题。
- **P1 = 18**：全部为降级为 `draft` 的卡因 `source_refs` 为空而触发；这是按 KF-021 处理原则主动降级后的预期结果，非新增异常。
- **YAML 错误 = 0**。

## 备注

- `yitang-huazong-ama-by-industry`、`yitang-huazong-ama-summary` 的 `source_refs` 指向真实文件 `src_20260529_huazong_ama-yitang-huazong-ama-20250526.md`，无需变更。
- 3 张中文 ID active 卡（互联网医院项目、诊所 O2O 项目、鑫港湾 HIS 项目）的 source_refs 均指向真实存在的 source 文件，无需变更。
- 任务清单中 `concept-minto-pyramid-principle` 的书目字典项和非文件字符串已被移除，保留真实 source `src_20260614_8269ccdb`。