# KDO 卡片质量门禁报告

**扫描时间**：2026-06-15  
**扫描范围**：30_wiki 全库 1192 张卡片  
**P0 阻塞问题卡片**：1 张  
**P1 修复问题卡片**：1 张  
**完全干净卡片**：1190 张  
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
| `tools\mineru-pdf-parsing-setup.md` | dangling 链接: paddle-ocr-setup; confidence=0.95 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |

---

## 使用说明

运行门禁脚本：
```bash
python 90_control/scripts/kcard-quality-gate.py
```

P0 问题必须在卡片进入 enriched/reviewed/stable 前修复。
P1 问题应在发布前修复。