# KDO 卡片质量门禁报告

**扫描时间**：2026-06-15  
**扫描范围**：30_wiki 全库 1242 张卡片  
**P0 阻塞问题卡片**：1 张  
**P1 修复问题卡片**：11 张  
**完全干净卡片**：1231 张  
**YAML 解析错误**：0 张  

---

## P0 阻塞问题清单

| 文件 | P0 问题 |
|---|---|
| `dark-knowledges\dk-wanghuan-paced-sales-decision.md` | author 为空; 缺少 trust_level |

---

## P1 修复问题清单

| 文件 | P1 问题 |
|---|---|
| `concepts\concept-wanghuan-adversarial-generation.md` | dangling 链接: framework-wanghuan-gan-three-roles, framework-wanghuan-gan-three-roles |
| `concepts\yt-demand-hierarchy-model.md` | confidence=0.92 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `concepts\yt-demand-user-segmentation.md` | dangling 链接: yt-demand-segmentation-canvas; confidence=0.92 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-wanghuan-paced-sales-decision.md` | source_refs 为空 |
| `dark-knowledges\yt-demand-competitive-displacement.md` | confidence=0.92 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\yt-demand-fake-demand-detection.md` | confidence=0.93 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `frameworks\framework-wanghuan-actor-director-mode.md` | status=draft 但 confidence=0.85 |
| `frameworks\framework-wanghuan-ai-five-level-ladder.md` | status=draft 但 confidence=0.85 |
| `frameworks\framework-wanghuan-bitcoe-prompt-framework.md` | status=draft 但 confidence=0.85 |
| `frameworks\yt-demand-early-validation.md` | confidence=0.92 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `frameworks\yt-demand-scenario-reconstruction.md` | confidence=0.92 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |

---

## 使用说明

运行门禁脚本：
```bash
python 90_control/scripts/kcard-quality-gate.py
```

P0 问题必须在卡片进入 enriched/reviewed/stable 前修复。
P1 问题应在发布前修复。