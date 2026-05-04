---
title: "kdo watch 增加定时巡检层"
assigned_to: "黄药师"
created_by: "欧阳锋"
created_at: "2026-05-04"
status: done
priority: P1
spec: "30_wiki/systems/kdo-watch-health-check-layer.md"
---

# kdo watch 增加定时巡检层

> 实现 6 项定时巡检 + 自动写入健康报告。
> 技术说明：`30_wiki/systems/kdo-watch-health-check-layer.md`

## 要做什么

在现有 `kdo watch`（监听 inbox → auto pipeline）基础上，加一条独立的巡检线程，支持两种模式：

1. `kdo watch --health` → 手动跑 6 项巡检，输出到控制台 + 文件
2. `kdo watch --health --cron 24h` → 后台定时，每 24h 自动巡检

6 项巡检：
- TODO 残留
- 低信任源
- 孤立页面
- 超期未更新
- 矛盾未解决
- 重复页面

输出：`60_feedback/eval-results/health_YYYY-MM-DD.md`

## 约束

- 纯标准库，不引入新依赖
- 巡检线程和 inbox 监听线程独立，不互锁
- 只读不写，不自动修复

## 验收

完成后跑一次 `kdo watch --health`，确保 6 项都有输出结果。
