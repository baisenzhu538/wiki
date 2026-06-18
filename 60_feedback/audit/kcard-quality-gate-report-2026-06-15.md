# KDO 卡片质量门禁报告

**扫描时间**：2026-06-15  
**扫描范围**：30_wiki 全库 1206 张卡片  
**P0 阻塞问题卡片**：2 张  
**P1 修复问题卡片**：2 张  
**完全干净卡片**：1202 张  
**YAML 解析错误**：1 张  

---

## P0 阻塞问题清单

| 文件 | P0 问题 |
|---|---|
| `concept-card-index-latest.md` | YAML 解析错误: None |
| `frameworks\xingangwan-pharma-business-formulas.md` | source_refs 为空 |

---

## P1 修复问题清单

| 文件 | P1 问题 |
|---|---|
| `frameworks\xingangwan-pharma-business-model-formulas.md` | source_refs 中的 src ID 未注册: src_20260618_xingangw |
| `projects\shanxi-field-research-checklist-20260701.md` | source_refs 为空; status 值异常: diagnostic |

---

## 使用说明

运行门禁脚本：
```bash
python 90_control/scripts/kcard-quality-gate.py
```

P0 问题必须在卡片进入 enriched/reviewed/stable 前修复。
P1 问题应在发布前修复。