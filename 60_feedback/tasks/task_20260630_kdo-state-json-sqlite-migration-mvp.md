---
id: task_20260630_kdo-state-json-sqlite-migration-mvp
title: "KDO state.json → SQLite MVP 迁移（sources 集合）"
type: task
status: queued
assignee: 黄药师
priority: P0
created_at: 2026-06-29
updated_at: 2026-06-29
reviewer: 欧阳锋
source_refs:
  - 90_control/plan-state-json-to-sqlite-migration.md
related:
  - [[plan-state-json-to-sqlite-migration]]
  - [[kdo-scalability-roadmap-10k-cards]]
---

# KDO state.json → SQLite MVP 迁移（sources 集合）

## 目标

把 `.kdo/state.json` 中的 `sources` 集合迁移到 SQLite，解决 `kdo enrich` 中 O(n) 线性查找 sources 的瓶颈，同时保持所有现有调用代码不变。

## 背景

- 当前 `state.json` 1.8 MB，含 17 个顶层集合。
- KDO 代码库中 272 处引用 `state.json` / `load_state` / `save_state`。
- `kdo enrich --all` 对每张需要 enrich 的卡线性扫描 `state["sources"]`（689 条），是主要慢路径之一。
- 完整方案见：[[plan-state-json-to-sqlite-migration]]

## 本周交付物

1. `kdo/workspace.py` 中新增 `SQLiteState` + `SQLiteCollection`
2. 修改 `load_state()`：自动检测 SQLite、自动迁移 JSON、保留备份
3. 修改 `save_state()`：SQLite 下做 WAL checkpoint
4. 只支持 `sources` 集合，其余 16 个集合继续走 JSON
5. 多进程并发安全：`busy_timeout=5000` + 进程级文件锁 `.kdo/state.sqlite.lock`
6. 显式事务上下文 `state.transaction()` 供批量写入
7. benchmark：`time kdo enrich --all --dry-run` 迁移前后对比

## 不做

- ❌ 双写过渡期（过度防御）
- ❌ `check_same_thread=False` 无保护方案
- ❌ 本周不迁移其余 16 个集合
- ❌ 本周不实现 `kdo migrate state --rollback`（下周做）

## 验收标准

- [ ] `kdo lint --summary` 无新增 ERROR/WARNING
- [ ] `.kdo/state.sqlite` 存在，`.kdo/state.json` 被重命名为 `.kdo/state.json.migrated`
- [ ] `sources` 表记录数与 JSON 中一致（689 条）
- [ ] `time kdo enrich --all --dry-run` 较迁移前下降 ≥30%
- [ ] 并发运行两个 `kdo` 命令不导致 state 数据丢失
- [ ] 所有现有测试通过

## 风险

| 风险 | 缓解 |
|:---|:---|
| SQLite 文件损坏 | WAL 模式 + `state.json.migrated` 备份 |
| 多进程写冲突 | `busy_timeout=5000` + 进程级文件锁 |
| 批量 append 中途失败留下脏数据 | 默认单条 auto-commit；批量用 `state.transaction()` |
| 旧代码直接读 `state.json` | 搜索全库直接路径引用，改为 `load_state()` |

## 关联文档

- [[plan-state-json-to-sqlite-migration]]
- [[kdo-scalability-roadmap-10k-cards]]
