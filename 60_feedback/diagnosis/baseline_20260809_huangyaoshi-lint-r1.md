---
title: #271 lint R1 四类规则全库基线报告
type: report
status: draft
created_at: 2026-08-09
author: 黄药师
---

# #271 lint R1 四类规则全库基线报告

> 生成命令（可复现）：
> ```
> cd C:\Users\Administrator\Desktop\wiki
> python -c "import sys; sys.path.insert(0, r'C:\Users\Administrator\Knowledge Delivery OS 0.0.1'); from pathlib import Path; from kdo.workspace import lint_workspace; issues = lint_workspace(Path(r'C:\Users\Administrator\Desktop\wiki')); [print(tag, len([i for i in issues if tag in i.message])) for tag in ['R1-a','R1-b','R1-c','R1-d']]"
> ```

## 基线数字（2026-08-09 扫描）

| 规则 | 级别 | 命中 | 说明 |
|:--|:--:|:--:|:--|
| R1-a reviewed 缺 reviewed_by/review_date | ERROR | **461** | E012 扩大版——存量终审标记不完整卡 |
| R1-b 重复节名 | ERROR | **37** | E009 批量版——ai-virtual-coach-prompt 单卡 3 处重复 |
| R1-c source_refs 仓库外路径 | WARNING | **10** | 桌面/YAI 路径引用，git 无法追溯 |
| R1-d 行号超界 | WARNING | **0** | 全库 708 个带行号 ref 全部界内（源文件 2000+ 行）；#250 L54 已被 #257 修复 |

**合计：508 命中（461 error + 47 warning）**。对应 `kdo lint` 全库新增 975 error / 569 warning（其余为 fuzzy match 等既有规则增量）。

## 清扫任务清单（P1-2 产出，另排执行）

### P1：R1-a 461 张 reviewed 缺字段
- 症状：`status: reviewed` 但缺 `reviewed_by` 或 `review_date`
- 根因：E012——终审标记与卡片 frontmatter 分离（欧阳锋手动 patch 队列但未同步卡）
- 动作：批量补标记（git log 追溯终审记录 → 补 reviewed_by/review_date）；无记录的降级 enriched
- 参考：#264 review_mark.py（已实现终审标记 CLI）

### P2：R1-b 37 张重复节名
- 症状：同卡两个 `## 角色设定` / `## 评估标准` 等
- 动作：逐卡人工合并/去重（内容操作，不可脚本化）——建议给老顽童
- 单卡重灾：ai-virtual-coach-prompt（3 处重复）

### P2：R1-c 10 张仓库外路径
- 症状：source_refs 指向 `C:/Users/.../Desktop/...`
- 动作：素材入仓库（10_raw/sources）后改相对路径；无法入仓的改 pending_archive

### 观察
- R1-d 为防增量规则（0 存量违规），纳入 pre-submit 门禁即可，无需清扫
- R1-a 的 461 是历史审查流程缺口的量化——建议欧阳锋知悉（终审时同步卡片 frontmatter）
