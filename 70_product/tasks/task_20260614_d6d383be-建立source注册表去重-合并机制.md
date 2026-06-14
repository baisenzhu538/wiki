---
task_id: "task_20260614_d6d383be"
title: "建立source注册表去重/合并机制"
project_id: "proj_20260614_afb74ee2"
artifact_id: ""
kind: "ops"
priority: "medium"
status: "todo"
due: ""
path: "70_product/tasks/task_20260614_d6d383be-建立source注册表去重-合并机制.md"
created_at: "2026-06-14T14:53:40+00:00"
updated_at: "2026-06-14T14:53:40+00:00"
---

# 建立source注册表去重/合并机制

## Project

proj_20260614_afb74ee2

## Artifact

N/A

## Execution Contract

- Kind: ops
- Priority: medium
- Status: todo
- Due: N/A

## Context

目标：解决本次迁移新增72条source记录导致的注册表快速膨胀问题。动作：1）分析90_control/source-registry.yaml中新增72条source的粒度和重复度；2）设计同一主题下多条短录音的合并策略；3）实现或规范source去重/合并机制（脚本或SOP）；4）对历史source进行一轮清理。成功指标：source注册表无重复记录，合并规则写入90_control/或docs/。负责人：黄药师。

## Definition Of Done

- TODO: specify observable completion criteria.

## Result

- TODO: link shipped artifact, delivery record, feedback, or follow-up task.
