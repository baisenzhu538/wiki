---
title: "记忆生命周期管理"
assigned_to: "黄药师"
created_by: "欧阳锋"
created_at: "2026-05-04"
status: complete
priority: P1
completed_at: "2026-05-05"
---
# 记忆生命周期管理

`20_memory/` 下的 staleness 检测 + 自动更新机制，防止用户偏好和纠正记录过时。

## 完成方案

### Staleness 检测（7 号健康检查）

`kdo watch --health` 新增第 7 项检查 `_check_memory_staleness()`：
- 每个记忆文件有独立的过期阈值：LATEST_SESSION.md (2d), project-continuity.md (7d), corrections.md (14d), user-preferences.md (30d), cli-preferences.json (30d), operating-principles.md (60d)
- 超期文件输出到 health report，含建议操作
- 集成到 watch daemon 定时巡检和 crontab 每日报告

### 自动更新机制

`kdo memory --update` 自动检测并标记已修复的纠正记录：
- 检测 C-1 (CJK enrich broken) → 自动追加 "✅ 已修复" 标记（因 REQ-016 已解决）
- 未来扩展：更多 fix-detection 规则

### 新增命令

| 命令 | 用途 |
|------|------|
| `kdo memory --check` | 检查 20_memory/ 过期状态（默认） |
| `kdo memory --update` | 自动更新可修复条目 |
| `kdo memory --update --dry-run` | 预览 --update 将执行的操作 |

**变更文件**：
- `kdo/memory.py` — 新建：check_memory_staleness(), auto_update_memory(), fix detection
- `kdo/health_check.py` — 新增 _check_memory_staleness() 作为第 7 项检查
- `kdo/commands/watch.py` — _run_health_cycle() 计数纳入 memory_staleness
- `kdo/commands/memory.py` — 新增 cmd_memory() handler
- `kdo/cli.py` — 新增 `kdo memory` 子命令 + `cmd_memory` import
- `20_memory/corrections.md` — C-1 自动追加已修复标记
