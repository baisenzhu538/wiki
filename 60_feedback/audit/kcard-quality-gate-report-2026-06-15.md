# KDO 卡片质量门禁报告

**扫描时间**：2026-06-15  
**扫描范围**：30_wiki 全库 1190 张卡片  
**P0 阻塞问题卡片**：0 张  
**P1 修复问题卡片**：25 张  
**完全干净卡片**：1165 张  
**YAML 解析错误**：0 张  

---

## P0 阻塞问题清单

无 P0 阻塞问题。

---

## P1 修复问题清单

| 文件 | P1 问题 |
|---|---|
| `cases\yt-lean-beauty-store-conversion.md` | source_refs 中的 src ID 未注册: src_20260616_b1e25c49, src_20260616_59f708ea, src_20260616_e66bd149 |
| `cases\yt-lean-daily-chemical-mvp.md` | source_refs 中的 src ID 未注册: src_20260616_b1e25c49, src_20260616_7dc80216, src_20260616_59f708ea |
| `cases\yt-lean-flower-mom-group-leader.md` | source_refs 中的 src ID 未注册: src_20260616_b1e25c49, src_20260616_7dc80216, src_20260616_6c8b240b |
| `concepts\yt-lean-daily-probability-decision.md` | source_refs 中的 src ID 未注册: src_20260616_b1e25c49, src_20260616_59f708ea, src_20260616_e66bd149 |
| `concepts\yt-lean-essence.md` | source_refs 中的 src ID 未注册: src_20260616_b1e25c49, src_20260616_7dc80216, src_20260616_6c8b240b |
| `concepts\yt-tob-cash-flow.md` | source_refs 中的 src ID 未注册: src_20260616_0e684368, src_20260616_5f991553 |
| `concepts\yt-tob-revenue-is-customer-cost.md` | source_refs 中的 src ID 未注册: src_20260616_0e684368, src_20260616_5f991553 |
| `concepts\yt-tob-sales-unit-model.md` | source_refs 中的 src ID 未注册: src_20260616_0e684368, src_20260616_5f991553 |
| `frameworks\yt-lean-assumption-prioritization.md` | source_refs 中的 src ID 未注册: src_20260616_b1e25c49, src_20260616_6c8b240b, src_20260616_e66bd149 |
| `frameworks\yt-lean-assumption-verification-3means.md` | source_refs 中的 src ID 未注册: src_20260616_b1e25c49, src_20260616_7dc80216, src_20260616_6c8b240b |
| `frameworks\yt-lean-b2b-b2c-hardware-content-testing.md` | source_refs 中的 src ID 未注册: src_20260616_b1e25c49, src_20260616_59f708ea, src_20260616_e66bd149 |
| `frameworks\yt-lean-consumer-deep-experience-testing.md` | source_refs 中的 src ID 未注册: src_20260616_b1e25c49, src_20260616_59f708ea |
| `frameworks\yt-lean-false-model-ai.md` | source_refs 中的 src ID 未注册: src_20260616_b1e25c49, src_20260616_7dc80216, src_20260616_6c8b240b |
| `frameworks\yt-lean-growth-stage-gate.md` | source_refs 中的 src ID 未注册: src_20260616_b1e25c49, src_20260616_7dc80216, src_20260616_6c8b240b |
| `frameworks\yt-lean-qualitative-quantitative-research.md` | source_refs 中的 src ID 未注册: src_20260616_b1e25c49, src_20260616_6c8b240b |
| `frameworks\yt-tob-barriers.md` | source_refs 中的 src ID 未注册: src_20260616_0e684368, src_20260616_5f991553 |
| `frameworks\yt-tob-core-characteristics.md` | source_refs 中的 src ID 未注册: src_20260616_0e684368, src_20260616_5f991553 |
| `frameworks\yt-tob-customer-tiering.md` | source_refs 中的 src ID 未注册: src_20260616_0e684368, src_20260616_5f991553 |
| `frameworks\yt-tob-demand-metrics.md` | source_refs 中的 src ID 未注册: src_20260616_0e684368, src_20260616_5f991553 |
| `frameworks\yt-tob-demand-scenarios.md` | source_refs 中的 src ID 未注册: src_20260616_0e684368, src_20260616_5f991553 |
| `frameworks\yt-tob-growth-channel.md` | source_refs 中的 src ID 未注册: src_20260616_0e684368, src_20260616_5f991553 |
| `frameworks\yt-tob-product-kernel.md` | source_refs 中的 src ID 未注册: src_20260616_0e684368, src_20260616_5f991553 |
| `frameworks\yt-tob-solution-model.md` | source_refs 中的 src ID 未注册: src_20260616_0e684368, src_20260616_5f991553 |
| `frameworks\yt-tob-unit-model.md` | source_refs 中的 src ID 未注册: src_20260616_0e684368, src_20260616_5f991553 |
| `tools\yt-tob-customer-sabc.md` | source_refs 中的 src ID 未注册: src_20260616_0e684368, src_20260616_5f991553 |

---

## 使用说明

运行门禁脚本：
```bash
python 90_control/scripts/kcard-quality-gate.py
```

P0 问题必须在卡片进入 enriched/reviewed/stable 前修复。
P1 问题应在发布前修复。