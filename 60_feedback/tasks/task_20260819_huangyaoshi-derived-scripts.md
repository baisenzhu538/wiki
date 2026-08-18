---
id: 369
assignee: huangyaoshi
status: queued
updated_at: '2026-08-19T01:30:00+00:00'
title: 派生脚本化 + 写入唯一入口（P3，codex 建议书⑤采纳）——daily-context-save 收口 + 派生物全脚本生成
priority: P3
dependency:
- 365
- 366
reviewed_by: 欧阳锋
---

# #369 派生脚本化 + 写入唯一入口（P3）

## 任务目标

派生物全部脚本生成、写入只走唯一入口：消灭"派生副本手改"（codex 根因 5）与多头写入。

## 素材/证据

- codex 建议书 §二根因 5：dashboard.md/dashboard.html/vault-status.md/agent-contexts-summary.md 有手改痕迹；§四 P3 方案
- 现有基础：generate-dashboard.py / daily-context-save.py 已在役，本任务=收口而非新建

## 修改范围

1. **daily-context-save.py 扩展为唯一写入入口**：所有 agent 收尾统一调用（含版本/hash 留痕）
2. **派生物脚本化**：dashboard/vault-status/agent-contexts-summary 全脚本生成 + `updated_at` + `git_head` 标记；手改痕迹检测（生成 hash 校验）
3. **可选**（不在必做范围）：kdo MCP 加 memory get/set，Hermes 三处 MEMORY.md/USER.md 收口统一读写——先出评估不实施

## 边界

- 依赖 #365（注册表定义派生关系）+ #366（指针引用派生物）
- MCP 记忆服务为可选项，需评估单独立项

## 验收标准

1. 派生物全部由脚本生成且带版本标记
2. 手改派生物可被检测报警
3. 全厂收尾统一走 daily-context-save.py（抽查 2 角色）

## 交付

1. 脚本化收口 + 检测机制
2. 送欧阳锋终审
