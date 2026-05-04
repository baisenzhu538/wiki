---
title: "kdo watch 自动识别 skill 路由"
assigned_to: "黄药师"
created_by: "欧阳锋"
created_at: "2026-05-04"
status: queued
priority: P1
---
# kdo watch 自动识别 skill 路由

kdo watch 检测到 inbox 新文件时，读 frontmatter `type:` 字段：
- `type: skill` → 走 capability 管线（注册到 `40_outputs/capabilities/skills/`）
- 默认 → 走 knowledge 管线（ingest → enrich → 概念卡）
