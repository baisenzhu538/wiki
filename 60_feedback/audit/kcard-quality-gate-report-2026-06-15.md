# KDO 卡片质量门禁报告

**扫描时间**：2026-06-15  
**扫描范围**：30_wiki 全库 1190 张卡片  
**P0 阻塞问题卡片**：1 张  
**P1 修复问题卡片**：0 张  
**完全干净卡片**：1189 张  
**YAML 解析错误**：1 张  

---

## P0 阻塞问题清单

| 文件 | P0 问题 |
|---|---|
| `cases\case-truman-prd-checklist-evolution.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 29, column 3:
    - signal: 同一个低级错误在两周内出现第二次
      ^
expected <block end>, but found '<scalar>'
  in "<unicode string>", line 30, column 25:
      framework_lens: "不再二错"机制失效
                            ^ |

---

## P1 修复问题清单

无 P1 修复问题。

---

## 使用说明

运行门禁脚本：
```bash
python 90_control/scripts/kcard-quality-gate.py
```

P0 问题必须在卡片进入 enriched/reviewed/stable 前修复。
P1 问题应在发布前修复。