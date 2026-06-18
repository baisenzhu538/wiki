# KDO 卡片质量门禁报告

**扫描时间**：2026-06-15  
**扫描范围**：30_wiki 全库 1199 张卡片  
**P0 阻塞问题卡片**：3 张  
**P1 修复问题卡片**：22 张  
**完全干净卡片**：1175 张  
**YAML 解析错误**：1 张  

---

## P0 阻塞问题清单

| 文件 | P0 问题 |
|---|---|
| `dark-knowledges\dk-note-maximum-common-divisor.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 1, column 1:
    id: dk-note-maximum-common-divisor
    ^
expected <block end>, but found '<scalar>'
  in "<unicode string>", line 30, column 9:
    - "显著更好"等效果描述来自主观对比，缺乏量化指标（token消耗、准确率、迭代轮数）
            ^ |
| `dark-knowledges\dk-note-surplus-brainpower.md` | source_refs 为空 |
| `dark-knowledges\dk-truman-document-is-real-project-is-fake.md` | source_refs 为空 |

---

## P1 修复问题清单

| 文件 | P1 问题 |
|---|---|
| `cases\yt-lean-beauty-store-conversion.md` | source_refs 为空 |
| `cases\yt-lean-daily-chemical-mvp.md` | source_refs 为空 |
| `cases\yt-lean-flower-mom-group-leader.md` | source_refs 为空 |
| `concepts\knowledge-error-self-exposure.md` | source_refs 为空 |
| `concepts\yt-lean-daily-probability-decision.md` | source_refs 为空 |
| `concepts\yt-lean-essence.md` | source_refs 为空 |
| `concepts\yt-tob-cash-flow.md` | source_refs 为空 |
| `concepts\yt-tob-revenue-is-customer-cost.md` | source_refs 为空 |
| `dark-knowledges\dk-truman-document-is-real-project-is-fake.md` | trust_level=low 但 confidence=0.88 |
| `decisions\xingangwan-pharma-mall-cabinet-internet-hospital-model.md` | dangling 链接: 单柜财务测算; status=draft 但 confidence=0.85; source_refs 中的 src ID 未注册: src_20260613_internet, src_20260613_internet, src_20260618_changzhi |
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
| `projects\parking-lot.md` | type 值异常: task-backlog; status=draft 但 confidence=0.85; source_refs 中的 src ID 未注册: src_20260618_changzhi |

---

## 使用说明

运行门禁脚本：
```bash
python 90_control/scripts/kcard-quality-gate.py
```

P0 问题必须在卡片进入 enriched/reviewed/stable 前修复。
P1 问题应在发布前修复。