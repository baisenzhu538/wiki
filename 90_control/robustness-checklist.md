---
id: robustness-checklist
title: 基建健壮性检验清单（五层框架 + 演练记录）
type: checklist
version: v1.0
created_at: '2026-08-24T03:00:00+08:00'
updated_at: '2026-08-24T03:00:00+08:00'
owner: 黄药师（基建单一实例）
audience: 黄药师 / 欧阳锋 / 风清扬
---

# 基建健壮性检验清单（#主动立项 2026-08-24）

> 健康（infra-status 全绿）≠ 健壮性（扛住故障/变更/恢复）。本清单五层检验，逐层勾选。
> 执行方式：黄药师主动执行（职责授权，2026-08-24 用户拍板"发现了可以主动做，做完结果写入文档"）；关键演练结果追加本文件；常规项随 infra-status/health-check 自动。

## L1 · 存在/配置层（✅ 已就位）

| 检验动作 | 命令 | 最近结果 |
|:--|:--|:--|
| 资产存在性+未登记 | `python kdo-tools/infra-status.py` | 27 项全绿，未登记 0（08-24） |
| 健康检查 9 项 | `python 90_control/scripts/health-check.py` | 每日 02:07 自动 |
| 探针六信号 | conveyor-probe 计划任务 | 每日 10min 自动 |

## L2 · 功能层（✅ 已就位）

| 检验动作 | 命令 | 最近结果 |
|:--|:--|:--|
| 单测全量 | `pytest 90_control/scripts/tests/ kdo-tools/tests/` | scripts 90 + kdo-tools 73（08-24） |
| 狗粮真实场景 | 各单交付时 | 见各任务单执行报告 |
| 幂等验证 | l1_capture 二次跑 | 13→0 新增（08-24 #491） |

## L3 · 故障层（⚠️ 演练中，2026-08-24 首次）

| 演练 | 场景 | 结果 |
|:--|:--|:--|
| F-1 探针依赖降级 | conveyor_probe 加载 file-flow-check 失败 | 见下方演练记录 |
| F-2 采集源缺失 | l1_capture SOURCE_DIRS 指向不存在目录 | 见下方演练记录 |
| F-3 队列文件缺失 | queue_transition 队列路径不存在 | 见下方演练记录 |
| F-4 主库缺失 | memory_capsule status 主库不存在 | 见下方演练记录 |

## L4 · 变更层（⚠️ 依赖图 2026-08-24 首建）

核心依赖关系（变更 A 前查此表——影响面）：
- `queue_gate` ← queue_transition / audit_queue_integrity / conveyor_probe（解析真相源，**改它=三处全变**）
- `queue_transition` → gate-blocked.log / force-exceptions.log / 任务单 frontmatter（流转+台账）
- `l1_capture` ← 计划任务 kdo-l1-capture；→ L1 主库 / trace-index / 体积日志
- `conveyor_probe` → PROPOSAL-PENDING 段 / 飞书 webhook / friction-log / gate-blocked.log（**只读消费方**）
- `memory_capsule` ← daily-context-save / l1_capture（写入端）；→ L1 库+镜像
- `file-flow-check` ← conveyor_probe（查重复用）/ infra-status（未登记对照不含）
- `tags-audit` ← check-tags-health（importlib 复用）

## L5 · 恢复层（⚠️ 首次演练 2026-08-24）

| 演练 | 场景 | 结果 |
|:--|:--|:--|
| R-1 镜像恢复 | 从 D 盘镜像恢复副本→校验可读 | 见下方演练记录 |
| R-2 L1 库恢复 | 从镜像恢复 activity_log.db 副本→integrity | 见下方演练记录 |

---

## 演练记录（2026-08-24 首轮）

### F-1 探针依赖降级 ✅（2026-08-24 实测）
场景：conveyor_probe 的 doc_id 查重模块（file-flow-check）加载失败。
做法：mock importlib.spec_from_file_location 抛异常 → 调 `_reject_duplicate_doc_ids`。
结果：**降级路径生效**——stderr 打印"⚠️ 查重模块加载失败，跳过查重"并返回原 hits（登记不被阻断）。正常路径（依赖存在）返回 hits 完整。**确认：探针不因辅助模块故障挂掉，降级是有意设计（#483）。**

### F-2 采集源缺失 ✅（2026-08-24 实测）
场景：SOURCE_DIRS 某源目录被删/不存在。
做法：SOURCE_DIRS 指向不存在目录 → capture(dry_run)。
结果：`if not src.exists(): continue`——**跳过不崩**，输出"待采集 0 个文件"，rc=0。采集面容错 ✅。

### F-3 队列文件缺失 ✅ 但可改进（2026-08-24 实测）
场景：queue_transition 队列路径不存在。
做法：KDO_QUEUE_PATH 指向不存在文件 → `queue_transition.py status`。
结果：**失败可见**（FileNotFoundError traceback）——但不友好（raw 堆栈而非清晰错误消息，对比 F-4）。**改进点：队列文件缺失时包一层清晰报错。**

### F-4 主库缺失 ✅（2026-08-24 实测）
场景：memory_capsule 主库不存在。
做法：A_DB 指向不存在路径 → cmd_status。
结果：**清晰报错**"❌ A 主库不存在（未 init）"，rc=1——失败可见 ✅（比 F-3 友好，作为报错范式）。

### R-1 事件库镜像恢复 ✅（2026-08-24 实测）
场景：从 D 盘事件库镜像（L1-backup，2 文件）恢复副本。
做法：copytree 到临时目录 → 文件数+抽样 hash 校验。
结果：**文件数一致=True、抽样 hash=True**——恢复路径可用。
⚠️ 注意：**L1-full 全量原文为单盘 D（#491 去 C 镜像后无备份）**——其"恢复"只能从 D 盘自身（防误删靠归档 zip）；事件库仍 C+D 双盘（本演练验证 D 镜像可恢复）。

### R-2 事件库恢复 ✅（2026-08-24 实测）
场景：从镜像恢复 activity_log.db 副本。
做法：复制到临时目录 → sqlite PRAGMA integrity_check。
结果：**integrity=ok，16 行数据完整**——事件库恢复路径可用。

---

## 结论（2026-08-24 首轮实测）

- **L1/L2 已就位**（infra-status 27 项全绿/health-check 9 项/pytest 163 用例）
- **L3 首演 4 项 3 过 1 可改进**：探针依赖降级不挂 ✅、采集源缺失跳过不崩 ✅、主库缺失清晰报错 ✅、队列文件缺失失败可见但 raw traceback（改进点：包清晰报错）
- **L4 依赖图首建**：改 queue_gate 波及三处（最高风险资产）；改 l1_capture 影响采集+体积+归档链；探针=只读消费方
- **L5 首演 2 项全过**：事件库镜像/库恢复副本可读+integrity ok（16 行）——恢复路径可用；**L1-full 单盘无备份为容灾缺口（#491 已注明，如需"同盘防误删镜像"另立项）**

**遗留/改进点**：
1. F-3 队列文件缺失报错改进（包清晰消息，替代 raw traceback）——可立项小改
2. 破坏性恢复演练（真删真恢复）待定期执行（低风险窗口）
3. 依赖图随资产增补维护（L4）
4. L3 演练每季度或关键变更后复演（建议挂停车场或 health-check 提示）

*黄药师 · 2026-08-24 · 首轮健壮性检验实测*

*黄药师 · 2026-08-24 · 首轮健壮性检验*
