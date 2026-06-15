# KDO 卡片质量门禁报告

**扫描时间**：2026-06-15  
**扫描范围**：30_wiki 全库 1190 张卡片  
**P0 阻塞问题卡片**：1 张  
**P1 修复问题卡片**：3 张  
**完全干净卡片**：1186 张  
**YAML 解析错误**：0 张  

---

## P0 阻塞问题清单

| 文件 | P0 问题 |
|---|---|
| `cases\case-纪浩-skill-market-problem-validation.md` | status=enriched 但 reviewed_by=pending |

---

## P1 修复问题清单

| 文件 | P1 问题 |
|---|---|
| `cases\case-truman-ai-partner.md` | 自审: author=老顽童, reviewed_by=老顽童 相同 |
| `cases\case-一堂-无人餐厅-hypothesis-failure.md` | dangling 链接: concept-一堂-key-assumptions|关键假设思维, yt-lean-assumption-verification-3means|关键假设验证的三种手段; 自审: author=老顽童, reviewed_by=老顽童 相同 |
| `concepts\yt-decision-y-model.md` | dangling 链接: yt-decision-width-method\|宽度方法, yt-five-step-method\|一堂五步法, yt-decision-depth-ladder\|深度阶梯, yt-unit-model-build|单元模型, yt-entrepreneur-key-hypotheses|关键假设 |

---

## 使用说明

运行门禁脚本：
```bash
python 90_control/scripts/kcard-quality-gate.py
```

P0 问题必须在卡片进入 enriched/reviewed/stable 前修复。
P1 问题应在发布前修复。