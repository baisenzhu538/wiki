# KDO 卡片质量门禁报告

**扫描时间**：2026-06-15  
**扫描范围**：30_wiki 全库 1345 张卡片  
**P0 阻塞问题卡片**：0 张  
**P1 修复问题卡片**：37 张  
**完全干净卡片**：1308 张  
**YAML 解析错误**：0 张  

---

## P0 阻塞问题清单

无 P0 阻塞问题。

---

## P1 修复问题清单

| 文件 | P1 问题 |
|---|---|
| `cases\case-smart-medicine-cabinet-failure-patterns-library.md` | source_refs 中的 src ID 未注册: src_20260613_3b5c7fdb |
| `cases\smart-medicine-cabinet-clinic-risk-observation.md` | source_refs 中的 src ID 未注册: src_20260613_1deb50c8, src_20260613_5f96c5bb, src_20260613_420e8085 |
| `concepts\ai-native-五层进阶从答案到效率到作品到产品到系统.md` | type 值异常: “framework”; status 值异常: “enriched” |
| `concepts\pilot-atomic-chunk-comparison.md` | type 值异常: comparison |
| `concepts\smart-medicine-cabinet-national-policy-redlines.md` | source_refs 中的 src ID 未注册: src_20260613_60c91b70, src_20260613_5f96c5bb |
| `concepts\smart-medicine-cabinet-o2o-cost-structure.md` | source_refs 中的 src ID 未注册: src_20260613_0e40f3cd, src_20260613_815b4103 |
| `concepts\smart-medicine-cabinet-regional-policy-map.md` | source_refs 中的 src ID 未注册: src_20260613_60c91b70, src_20260613_5f96c5bb |
| `concepts\yt-business-formula-parameter-iceberg.md` | source_refs 中的 src ID 未注册: src_20260613_fa7b370d |
| `concepts\yt-business-formula-six-level-logic.md` | source_refs 中的 src ID 未注册: src_20260613_0ab21e5e |
| `concepts\yt-business-formula-ten-paradigms.md` | source_refs 中的 src ID 未注册: src_20260613_8bfdc3d1 |
| `concepts\yt-composite-pan-product-methodology.md` | type 值异常: composite-concept |
| `concepts\yt-management-business-formula.md` | source_refs 中的 src ID 未注册: src_20260613_91f90839, src_20260613_8bfdc3d1, src_20260613_0ab21e5e |
| `concepts\yt-personal-ai-thinking-card.md` | type 值异常: method |
| `concepts\yt-prompt-engineering-andrew-ng.md` | type 值异常: course_notes |
| `concepts\yt-research-competitor-toolkit.md` | status=draft 但 confidence=0.85 |
| `concepts\yt-research-expert-interview.md` | status=draft 但 confidence=0.85 |
| `concepts\yt-research-hypothesis-test.md` | status=draft 但 confidence=0.85 |
| `concepts\yt-research-industry-canvas.md` | status=draft 但 confidence=0.85 |
| `concepts\yt-research-intelligence-map.md` | status=draft 但 confidence=0.85 |
| `concepts\yt-research-osl-framework.md` | status=draft 但 confidence=0.85 |
| `concepts\yt-unit-model-ai-assisted.md` | source_refs 中的 src ID 未注册: src_20260524_5e4f3a2b |
| `concepts\yt-unit-model-benchmark.md` | status=draft 但 confidence=0.85; source_refs 中的 src ID 未注册: src_20260524_7c8d9e0f, src_20260524_6b5a4c3d |
| `concepts\yt-unit-model-construction.md` | status=draft 但 confidence=0.85; source_refs 中的 src ID 未注册: src_20260524_9f4e5d6a, src_20260524_7c8d9e0f, src_20260524_6b5a4c3d |
| `concepts\yt-unit-model-dynamic.md` | status=draft 但 confidence=0.85; source_refs 中的 src ID 未注册: src_20260524_6b5a4c3d, src_20260524_5e4f3a2b |
| `concepts\yt-unit-model-selection.md` | status=draft 但 confidence=0.85; source_refs 中的 src ID 未注册: src_20260524_9f4e5d6a, src_20260524_7c8d9e0f |
| `contradictions.md` | type 值异常: meta |
| `decisions\gold-standard-manual-labels.md` | type 值异常: reference |
| `decisions\labeling-research-alignment.md` | type 值异常: comparison |
| `frameworks\yt-business-formula-abc-model.md` | source_refs 中的 src ID 未注册: src_20260613_91f90839 |
| `log.md` | type 值异常: meta |
| `projects\互联网医院项目.md` | type 值异常: project |
| `projects\诊所O2O项目.md` | type 值异常: project |
| `projects\鑫港湾HIS项目.md` | type 值异常: project |
| `systems\workflow-knowledge-collision.md` | type 值异常: workflow |
| `tools\smart-medicine-cabinet-financial-model.md` | source_refs 中的 src ID 未注册: src_20260613_0e40f3cd, src_20260613_5f96c5bb |
| `tools\smart-medicine-cabinet-fraud-detection.md` | source_refs 中的 src ID 未注册: src_20260613_3b5c7fdb, src_20260613_5f96c5bb |
| `tools\tool-smart-medicine-cabinet-site-selection-guide.md` | source_refs 中的 src ID 未注册: src_20260613_0e40f3cd |

---

## 使用说明

运行门禁脚本：
```bash
python 90_control/scripts/kcard-quality-gate.py
```

P0 问题必须在卡片进入 enriched/reviewed/stable 前修复。
P1 问题应在发布前修复。