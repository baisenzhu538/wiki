# KDO 卡片质量门禁报告

**扫描时间**：2026-06-15  
**扫描范围**：30_wiki 全库 1248 张卡片  
**P0 阻塞问题卡片**：0 张  
**P1 修复问题卡片**：9 张  
**完全干净卡片**：1239 张  
**YAML 解析错误**：0 张  

---

## P0 阻塞问题清单

无 P0 阻塞问题。

---

## P1 修复问题清单

| 文件 | P1 问题 |
|---|---|
| `concepts\yt-demand-b2b-vs-b2c.md` | dangling 链接: xujian-tob-fivestep-oral |
| `concepts\yt-demand-hierarchy-model.md` | confidence=0.92 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `concepts\yt-demand-user-segmentation.md` | confidence=0.92 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\yt-demand-competitive-displacement.md` | confidence=0.92 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\yt-demand-fake-demand-detection.md` | confidence=0.93 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\yt-demand-scope-creep.md` | confidence=0.92 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `frameworks\yt-demand-decision-chain.md` | dangling 链接: xujian-tob-fivestep-oral |
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