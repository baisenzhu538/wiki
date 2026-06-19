# KDO 卡片质量门禁报告

**扫描时间**：2026-06-15  
**扫描范围**：30_wiki 全库 1214 张卡片  
**P0 阻塞问题卡片**：2 张  
**P1 修复问题卡片**：0 张  
**完全干净卡片**：1212 张  
**YAML 解析错误**：2 张  

---

## P0 阻塞问题清单

| 文件 | P0 问题 |
|---|---|
| `dark-knowledges\dk-five-step-framework-legitimizes-bias.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 39, column 3:
    - signal: 五步法报告很完整——每个框都填了、画布很漂亮—— ... 
      ^
expected <block end>, but found '<scalar>'
  in "<unicode string>", line 40, column 24:
      framework_lens: "框完成"≠"框验证"——填满动作无法替代数据溯源
                           ^ |
| `dark-knowledges\dk-level-blindspot-external-feedback.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 41, column 3:
    - signal: "完成度"被用作段位指标——画布填满了、模板用全 ... 
      ^
expected <block end>, but found '<scalar>'
  in "<unicode string>", line 41, column 16:
    - signal: "完成度"被用作段位指标——画布填满了、模板用全了，就觉得段位提升了
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