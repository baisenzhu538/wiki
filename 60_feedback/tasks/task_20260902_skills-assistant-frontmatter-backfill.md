---
id: '595'
title: 全厂 skill frontmatter 字段补齐（66/76 缺 status，Skills助理第二单）
type: skill-production
status: in_progress
priority: P2
assignee: skills-assistant
created_by: 王语嫣
created_at: 2026-09-02
source_refs:
- 60_feedback/tasks/task_20260902_skills-assistant-research-core-integration.md
- 40_outputs/capabilities/skills/INDEX.md
instance: skills-assistant
updated_at: '2026-09-01T15:12:46.012741+00:00'
---

# #595 全厂 skill frontmatter 字段补齐（老朱 09-02 拍板「立」）

## 背景

#594 终审遗留①：实测 66/76 shared skills 缺 `status:`/`reviewed_by:` 字段（门禁与检索的地基缺口）。老朱拍板立项。

## 任务

1. 扫描 76 个 shared skill，按内容真实状态补齐 frontmatter 四字段：`status` / `reviewed_by` / `review_date` / `grade`
2. 口径：有终审记录（MOUNT-MATRIX 挂载在案/任务单终审 PASS）→ status: enriched + reviewed_by: 欧阳锋 + 实际日期等级；无终审记录 → status: draft + reviewed_by 留空（不虚构）
3. 红线：**只动 frontmatter，正文零改动**（#594 边界纪律同款，git diff 逐卡核查）
4. 重跑 scan_skills_registry.py 刷新 INDEX/MOUNT-MATRIX，`--check` 🟢 fresh
5. pre-submit 抽验 5 张 + 执行报告五字段 + complete 提审（用完整 task_id）

## 验收标准

1. 76/76 skill frontmatter 四字段齐全，零虚构（draft 就是 draft）
2. git diff 全量核查：每卡仅 frontmatter 行变更
3. --check fresh + pre-submit 抽验 5/5 PASS

## 执行报告

（待施工后补）
