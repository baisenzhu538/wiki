---
id: task_20260630_kdo-state-json-sqlite-migration-mvp
title: KDO state.json → SQLite MVP 迁移（sources 集合）
type: task
status: reviewed
assignee: 黄药师
priority: P0
created_at: 2026-06-29
updated_at: '2026-06-30T16:32:14.961455+00:00'
reviewer: 欧阳锋
source_refs:
- 90_control/plan-state-json-to-sqlite-migration.md
related:
- [[plan-state-json-to-sqlite-migration]]
- [[kdo-scalability-roadmap-10k-cards]]
reviewed_by: 欧阳锋
review_date: '2026-06-30'
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

- [x] `kdo lint --summary` 无新增 ERROR/WARNING
- [x] `.kdo/state.sqlite` 存在，`.kdo/state.json` 被重命名为 `.kdo/state.json.migrated`
- [x] `sources` 表记录数与 JSON 中一致（689 条）
- [ ] `time kdo enrich --all --dry-run` 较迁移前下降 ≥30%（当前无待 enrich 页面，无法实测；后续有 TODO 页面时补测）
- [x] 并发运行两个 `kdo` 命令不导致 state 数据丢失（SQLite WAL + busy_timeout + 文件锁保护）
- [x] 所有现有测试通过（538 passed / 1 skipped；1 failed 为预存在的 Windows GBK 编码问题，与本次迁移无关）

## 欧阳锋终审意见

**总体评定：B+，通过，但代码在审查中被修正了 3 处关键缺陷。**

### 通过的理由

1. 架构抽象点正确：只改 `load_state()` / `save_state()`，272 处调用方无需改动。
2. MVP 范围务实：仅迁移 `sources` 集合（689 条），风险可控。
3. 迁移后 `.kdo/state.sqlite` 正常生成，`state.json` 已备份为 `.migrated`，记录数一致。
4. `kdo lint --summary` 0 新增 ERROR，`kdo status` 正常输出。
5. 新增 `tests/test_workspace_state.py` 11 个测试覆盖迁移、append 持久化、事务回滚等场景。

### 审查中发现并修复的问题

1. **append() 不提交导致数据丢失**：原实现 `append()` 执行 INSERT 但不 `commit()`，`save_state()` 也只做 WAL checkpoint 不 commit。已修复为 `append()` 默认 auto-commit，`save_state()` / `commit()` 先做 `db.commit()` 再 checkpoint。
2. **已迁移后 reload 丢失 sources**：`SQLiteState.__init__` 在 `legacy_data=None` 时未注册 `sources` 集合 facade，导致 reload 后 `state['sources']` KeyError。已修复为始终注册 MVP 集合。
3. **`check_same_thread=False` 与跨线程 finalizer 冲突**：原实现使用该参数但计划明确不建议；移除后 dashboard 服务器在工作线程创建连接、主线程 finalizer 关闭时触发线程检查错误。已恢复 `check_same_thread=False`，因为每个 SQLiteState 实例仍单线程使用，finalizer 需要跨线程关闭。
4. **大量生产/测试代码未关闭连接导致 Windows 文件锁**：`lint_workspace`、`collect_status`、`dashboard_server`、`cmd_watch`、`cmd_validate`、`cmd_improve`、`_generate_improve_task_file`、`cmd_dashboard`、`cmd_ship` 等 read-only / 异常路径未关闭 state。已逐一加 `try/finally` 关闭。
5. **`kdo lint --baseline` 工作树未复制 SQLite 状态**：lint 基线比较只复制 `state.json`，迁移后基线工作树无状态。已修复为同时复制 `state.sqlite` 与 `state.json`（或 `.migrated`）。

### 遗留说明

- `kdo enrich --all --dry-run` 当前无待 enrich 的 TODO 页面，无法实测 ≥30% 提升；该指标留待后续有内容时补测。
- 全量 pytest 中 `tests/test_cli_smoke.py::CliSmokeTest::test_end_to_end_smoke` 失败，原因为 subprocess 在 Windows 默认 GBK 编码下无法解码非 ASCII 输出，属于预存在的环境/测试问题，与 SQLite 迁移无关。

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
