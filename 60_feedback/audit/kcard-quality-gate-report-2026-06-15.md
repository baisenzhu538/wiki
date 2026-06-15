# KDO 卡片质量门禁报告

**扫描时间**：2026-06-15  
**扫描范围**：30_wiki 全库 1339 张卡片  
**P0 阻塞问题卡片**：0 张  
**P1 修复问题卡片**：16 张  
**完全干净卡片**：1323 张  
**YAML 解析错误**：0 张  

---

## P0 阻塞问题清单

无 P0 阻塞问题。

---

## P1 修复问题清单

| 文件 | P1 问题 |
|---|---|
| `cases\case-milktea-five-step.md` | dangling 链接: concept-一堂-business-prediction |
| `concepts\concept-一堂-hypothesis-driven-business-methodology.md` | dangling 链接: concept-一堂-business-prediction |
| `concepts\concept-一堂-key-assumptions.md` | dangling 链接: concept-一堂-business-prediction |
| `concepts\kdo_product_design_agent_final.md` | dangling 链接: obsidian-kdo-内容产出工作流-产品设计大纲 |
| `concepts\skill-一堂-business-prediction-15-char.md` | dangling 链接: concept-一堂-business-prediction, concept-一堂-business-prediction |
| `concepts\skill-一堂-spectrum-positioning.md` | dangling 链接: concept-一堂-business-prediction, concept-一堂-business-prediction |
| `concepts\yt-unit-model-benchmark.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\yt-unit-model-construction.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\yt-unit-model-dynamic.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\yt-unit-model-selection.md` | trust_level=high 但 source 仅 1 个 |
| `decisions\agent-ecosystem-design.md` | dangling 链接: concept-一堂-business-prediction |
| `decisions\fix-data-curator-parse-bug.md` | dangling 链接: plan_20260531_data-curator-v1 |
| `decisions\kdo-protocol-implementation-roadmap.md` | dangling 链接: obsidian-kdo-内容产出工作流-产品设计大纲 |
| `entities\紫鲸AI.md` | dangling 链接: 紫鲸ai_智能体工作流平台_深度分析与产品设计 |
| `links\index.md` | dangling 链接: 紫鲸ai_智能体工作流平台_深度分析与产品设计, obsidian-kdo-内容产出工作流-产品设计大纲, concept-一堂-business-prediction |
| `systems\kdo-protocol.md` | dangling 链接: obsidian-kdo-内容产出工作流-产品设计大纲, obsidian-kdo-内容产出工作流-产品设计大纲 |

---

## 使用说明

运行门禁脚本：
```bash
python 90_control/scripts/kcard-quality-gate.py
```

P0 问题必须在卡片进入 enriched/reviewed/stable 前修复。
P1 问题应在发布前修复。