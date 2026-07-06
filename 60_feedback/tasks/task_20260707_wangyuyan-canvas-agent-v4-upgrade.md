---
id: task_20260707_wangyuyan-canvas-agent-v4-upgrade
type: task
status: queued
assignee: 老顽童
reviewer: 欧阳锋
priority: P1
created_at: 2026-07-07
updated_at: 2026-07-07
source_refs:
- C:/Users/Administrator/Desktop/从知识库到agent.txt
- 00_inbox/skills/triangle-assessment.html
- 30_wiki/tools/agent-spec-dual-triangle-canvas-filler.md
related:
- '[[agent-spec-dual-triangle-canvas-filler]]'
- '[[method-kdo-agent-design-meta]]'
---

# 任务 #130：画布 Agent v4——注入 Judge Skill + 七要素 + 雷达图

## 来源

v3 注入了 YAI 蒸馏的 13 项对话能力。v4 注入新获得的三个资产：

| 资产 | 来源 | 注入内容 |
|:---|:---|:---|
| Judge Skill 五维打分 | 蓝鱼 #128 | 画布填完后自动五维自评（输出标准/边界/坑/约束/门控），输出分数和改进建议 |
| Skill 七要素 | 蓝鱼 #129 | agent-spec 增加 Error Correction（纠错机制）+ Mini Loop（小循环自迭代） |
| 雷达图可视化 | 蓝鱼 triangle-assessment.html | 画布输出增加六维雷达图（文本版），同时标注各维度当前段位（L1-L6） |

## 产出

- `agent-spec-dual-triangle-canvas-filler` v3 → v4
- 画布填充完成后自动输出：五维自评分数 + 六维雷达图（文本）+ 改进建议

## 验收

- agent-spec v4 含 Judge Skill 自评章节 + 七要素完整（纠错+小循环）+ 雷达图输出模板
- `kdo pre-submit` PASS
