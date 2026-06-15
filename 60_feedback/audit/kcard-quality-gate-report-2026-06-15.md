# KDO 卡片质量门禁报告

**扫描时间**：2026-06-15  
**扫描范围**：30_wiki 全库 1155 张卡片  
**P0 阻塞问题卡片**：0 张  
**P1 修复问题卡片**：4 张  
**完全干净卡片**：1151 张  
**YAML 解析错误**：0 张  

---

## P0 阻塞问题清单

无 P0 阻塞问题。

---

## P1 修复问题清单

| 文件 | P1 问题 |
|---|---|
| `concepts\ai时代判断力口述-3.md` | dangling 链接: ocr-一堂-个人修炼-科学学习ipo模型, ocr-一堂-个人修炼-科学学习ipo模型 |
| `concepts\yitang-huazong-ama-by-industry.md` | dangling 链接: ocr-一堂-个人修炼-双三角模型 |
| `concepts\yitang-huazong-ama-summary.md` | dangling 链接: ocr-一堂-个人修炼-双三角模型 |
| `links\index.md` | dangling 链接: ocr-一堂-个人修炼-双三角模型, ocr-一堂-个人修炼-科学学习ipo模型 |

---

## 使用说明

运行门禁脚本：
```bash
python 90_control/scripts/kcard-quality-gate.py
```

P0 问题必须在卡片进入 enriched/reviewed/stable 前修复。
P1 问题应在发布前修复。