---
id: task_20260707_wangyuyan-oscar-enrichment
type: task
status: queued
assignee: 老顽童
reviewer: 欧阳锋
priority: P0
created_at: 2026-07-07
updated_at: 2026-07-07
source_refs:
- 30_wiki/frameworks/framework-yitang-oscar-research.md
- 30_wiki/concepts/business-research-skill-oscar-13-weapon-system.md
- 40_outputs/capabilities/skills/business-research/SKILL.md
related:
- '[[framework-yitang-oscar-research]]'
- '[[yt-research-weaponry-course]]'
---

# 任务 #124：OSCAR 框架卡从 enriched→reviewed + 桥接 KDO 实战 SOP

## 背景

黄药师发现 `framework-yitang-oscar-research` 和 `business-research-skill-oscar-13-weapon-system` 都是 `enriched` 状态，大量 `src_unknown` 占位，未经欧阳锋终审。飞书 Agent 说"归档了"是错的，但说"不是成品"是对的。

KDO 实战的调研 SOP（选方向→广撒网→深追搜→交叉比对→出诊断+四路 Attacker）本质就是 OSCAR——但术语和结构没打通。

## 动作

1. 补齐两张卡中所有 `src_unknown` 占位
2. 将 KDO 实战外部探索 SOP 的术语映射写入 OSCAR 卡的 Bridge/Synthesis：

| KDO SOP | OSCAR |
|:---|:---|
| 选方向 | O - Objective（目标） |
| 广撒网(3-4路) | S - Scope（范围）→ C - Collect（收集） |
| 深追搜 | C - Collect（收集） |
| 交叉比对(search_files) | A - Analyze（分析） |
| 出诊断+四路 Attacker | R - Report（报告） |

3. 欧阳锋终审

## 验收

- 两张卡 status: enriched → reviewed
- src_unknown 清零
- KDO SOP 映射表在 Synthesis 章节
- `kdo pre-submit` PASS
