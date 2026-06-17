# KDO 卡片质量门禁报告

**扫描时间**：2026-06-15  
**扫描范围**：30_wiki 全库 1193 张卡片  
**P0 阻塞问题卡片**：0 张  
**P1 修复问题卡片**：4 张  
**完全干净卡片**：1189 张  
**YAML 解析错误**：0 张  

---

## P0 阻塞问题清单

无 P0 阻塞问题。

---

## P1 修复问题清单

| 文件 | P1 问题 |
|---|---|
| `concepts\master-antifragile-checklist.md` | status=draft 但 confidence=0.88 |
| `concepts\skill-水水-管理决策权重偏差.md` | status=draft 但 confidence=0.85 |
| `concepts\yt-foresight-addition-subtraction.md` | confidence=0.9 但 source 仅 1 个; status=draft 但 confidence=0.9 |
| `concepts\yt-foresight-ten-fatal-flaws.md` | confidence=0.9 但 source 仅 1 个; status=draft 但 confidence=0.9 |

---

## 使用说明

运行门禁脚本：
```bash
python 90_control/scripts/kcard-quality-gate.py
```

P0 问题必须在卡片进入 enriched/reviewed/stable 前修复。
P1 问题应在发布前修复。