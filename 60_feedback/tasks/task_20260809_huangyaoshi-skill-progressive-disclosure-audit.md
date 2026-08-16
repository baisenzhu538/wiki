---
id: task_20260809_huangyaoshi-skill-progressive-disclosure-audit
assignee: huangyaoshi
status: closed_merged
updated_at: 2026-08-09
priority: P2
---

# Skill 渐进披露合规审计（B4）

## 任务目标

对标 Anthropic 官方 Agent Skills 最佳实践，审计 52+69 skill 的结构合规性，输出改造清单。

## 背景

- Anthropic 官方规范（2026）：三级渐进披露——frontmatter name/description（~100 词，第三人称+具体触发词）→ SKILL.md 1500-2000 词 → references/ 下沉长内容；单一职责；触发词含负面例子防误触发；禁止把长期项目记忆混入 SKILL.md
- KDO 现状：52+69 skill 无系统性合规检查，部分 skill 可能超长/描述含糊/触发词碰撞

## 规格

1. 审计维度：① frontmatter 完整性（name/description 第三人称+触发词）② SKILL.md 长度（>3000 词标记）③ 是否含长期项目记忆（应下沉 references 或记忆系统）④ 触发词碰撞（同名/近似 skill 间）
2. 输出：审计报告（60_feedback/）+ 分级改造清单（P0 违规/P1 建议/P2 可选）
3. 标杆：task-orchestration（2026-08-09 新建，已按规范双写）作为合规样例

## 验收标准

- 审计覆盖全部 skill（shared 69 + 顶级 39 + .claude 52 去重）
- 报告列出每项违规的 skill 路径 + 具体问题 + 改造建议
- 改造清单按优先级入队（不在本任务内执行改造）

## 边界

- 本任务只审计不改造（改造任务单另行）
- 内容质量（方法好坏）不在审计范围，只审计结构合规

## ⚠️ 已合并（2026-08-09 王语嫣裁决）

本任务已并入 **#278**（`task_20260809_huangyaoshi-skill-cleanup.md`——Skill 盘点+渐进披露审计+大扫除三合一），勿单独领取。


## CLOSE（2026-08-09）

已并入 #278（Skill 盘点+审计+大扫除，reviewed）——本任务关闭不执行。
