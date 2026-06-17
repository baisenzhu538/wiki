# KDO 卡片质量门禁报告

**扫描时间**：2026-06-15  
**扫描范围**：30_wiki 全库 1193 张卡片  
**P0 阻塞问题卡片**：1 张  
**P1 修复问题卡片**：19 张  
**完全干净卡片**：1173 张  
**YAML 解析错误**：1 张  

---

## P0 阻塞问题清单

| 文件 | P0 问题 |
|---|---|
| `concept-card-index-latest.md` | YAML 解析错误: None |

---

## P1 修复问题清单

| 文件 | P1 问题 |
|---|---|
| `cases\yt-lean-beauty-store-conversion.md` | source_refs 为空 |
| `cases\yt-lean-daily-chemical-mvp.md` | source_refs 为空 |
| `cases\yt-lean-flower-mom-group-leader.md` | source_refs 为空 |
| `concepts\yt-lean-daily-probability-decision.md` | source_refs 为空 |
| `concepts\yt-lean-essence.md` | source_refs 为空 |
| `concepts\yt-research-competitor-toolkit.md` | 自审: author=老顽童, reviewed_by=老顽童 相同 |
| `concepts\yt-tob-cash-flow.md` | source_refs 为空 |
| `concepts\yt-tob-revenue-is-customer-cost.md` | source_refs 为空 |
| `frameworks\yt-lean-assumption-prioritization.md` | source_refs 为空 |
| `frameworks\yt-lean-assumption-verification-3means.md` | source_refs 为空 |
| `frameworks\yt-lean-b2b-b2c-hardware-content-testing.md` | source_refs 为空 |
| `frameworks\yt-lean-consumer-deep-experience-testing.md` | source_refs 为空 |
| `frameworks\yt-lean-false-model-ai.md` | source_refs 为空 |
| `frameworks\yt-lean-growth-stage-gate.md` | source_refs 为空 |
| `frameworks\yt-lean-qualitative-quantitative-research.md` | source_refs 为空 |
| `frameworks\yt-tob-core-characteristics.md` | source_refs 为空 |
| `frameworks\yt-tob-customer-tiering.md` | source_refs 为空 |
| `frameworks\yt-tob-demand-scenarios.md` | source_refs 为空 |
| `frameworks\yt-tob-product-kernel.md` | source_refs 为空 |

---

## 使用说明

运行门禁脚本：
```bash
python 90_control/scripts/kcard-quality-gate.py
```

P0 问题必须在卡片进入 enriched/reviewed/stable 前修复。
P1 问题应在发布前修复。