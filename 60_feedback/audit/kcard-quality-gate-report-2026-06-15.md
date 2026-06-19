# KDO 卡片质量门禁报告

**扫描时间**：2026-06-15  
**扫描范围**：30_wiki 全库 1212 张卡片  
**P0 阻塞问题卡片**：3 张  
**P1 修复问题卡片**：2 张  
**完全干净卡片**：1207 张  
**YAML 解析错误**：0 张  

---

## P0 阻塞问题清单

| 文件 | P0 问题 |
|---|---|
| `concepts\skill-ban-fei-mao-dong-tai-du-qu-xiang-liang-hua-guan-li-die-dai-zhi-shi.md` | source_refs 为空 |
| `concepts\skill-ban-fei-mao-qing-xi-zi-liao-wei-markdown-ge-shi-wei-gei-ai.md` | source_refs 为空; 缺少 trust_level |
| `concepts\skill-ban-fei-mao-yong-yaml-ge-shi-zuo-zhi-shi-ku-yuan-zi-hua-biao-qian.md` | source_refs 为空 |

---

## P1 修复问题清单

| 文件 | P1 问题 |
|---|---|
| `concepts\skill-ban-fei-mao-gao-su-ai-dang-qian-ri-qi-xian-zhi-shu-ju-shi-xiao.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\skill-ban-fei-mao-pan-duan-ke-cheng-shi-fou-zhi-de-zuo-cheng-skill.md` | dangling 链接: 10_raw/sources/src_20260617_f1830fa6-半肥猫-ai学习落地-口述.md|半肥猫-AI学习落地-口述 |

---

## 使用说明

运行门禁脚本：
```bash
python 90_control/scripts/kcard-quality-gate.py
```

P0 问题必须在卡片进入 enriched/reviewed/stable 前修复。
P1 问题应在发布前修复。