# KDO 卡片质量门禁报告

**扫描时间**：2026-06-15  
**扫描范围**：30_wiki 全库 1210 张卡片  
**P0 阻塞问题卡片**：2 张  
**P1 修复问题卡片**：2 张  
**完全干净卡片**：1206 张  
**YAML 解析错误**：0 张  

---

## P0 阻塞问题清单

| 文件 | P0 问题 |
|---|---|
| `cases\case-ji-hao-ai-workspace-chaos.md` | source_refs 为空 |
| `cases\case-ji-hao-ui-design-constraint-evolution.md` | source_refs 为空 |

---

## P1 修复问题清单

| 文件 | P1 问题 |
|---|---|
| `cases\case-ban-fei-mao-skill-ab-test.md` | trust_level=low 但 confidence=0.88 |
| `cases\case-guang-leng-dian-zi-hx-smj.md` | dangling 链接: failure-modes-electronics, project-standards, project-standards, failure-modes-electronics |

---

## 使用说明

运行门禁脚本：
```bash
python 90_control/scripts/kcard-quality-gate.py
```

P0 问题必须在卡片进入 enriched/reviewed/stable 前修复。
P1 问题应在发布前修复。