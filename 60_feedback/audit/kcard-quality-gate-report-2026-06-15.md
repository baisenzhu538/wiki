# KDO 卡片质量门禁报告

**扫描时间**：2026-06-15  
**扫描范围**：30_wiki 全库 1206 张卡片  
**P0 阻塞问题卡片**：0 张  
**P1 修复问题卡片**：4 张  
**完全干净卡片**：1202 张  
**YAML 解析错误**：0 张  

---

## P0 阻塞问题清单

无 P0 阻塞问题。

---

## P1 修复问题清单

| 文件 | P1 问题 |
|---|---|
| `dark-knowledges\dk-f14-accuracy-measurement-mismatch.md` | dangling 链接: dk-p15-claimed-done-not-verified, dk-p15-claimed-done-not-verified |
| `dark-knowledges\dk-f6-cjk-skeleton-corruption.md` | trust_level=low 但 confidence=0.88 |
| `dark-knowledges\dk-p11-regex-cutoff.md` | dangling 链接: 90_control/failure-modes.md, .agent/pitfalls.md |
| `dark-knowledges\dk-p16-validate-reads-state-json.md` | dangling 链接: dk-p15-claimed-done-not-verified, dk-p15-claimed-done-not-verified |

---

## 使用说明

运行门禁脚本：
```bash
python 90_control/scripts/kcard-quality-gate.py
```

P0 问题必须在卡片进入 enriched/reviewed/stable 前修复。
P1 问题应在发布前修复。