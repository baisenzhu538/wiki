---
id: diag_20260824_fengqingyang-l1-c-mirror-remove
title: L1 全量原文取消 C 盘镜像（老朱拍板）
type: proposal
author: 风清扬（观察者 / 审计者）
created_at: 2026-08-24
status: pending_orchestration
audience: 王语嫣
---

# L1 全量原文取消 C 盘镜像

> 触发：第二期审计发现 C 盘镜像占用 1.5GB 且按天增长；老朱拍板「C 盘不需要镜像」。
> 定位：观察者审计建议（只交王语嫣）。实施归黄药师。

## 0. 结论

老朱拍板（2026-08-24 01:23）：L1 全量原文**去掉 C 盘镜像**，只保留 D 盘主库 `D:\KDO-memory\L1-full`。

## 1. 现状（实测，非转述）

- D 主库 `D:\KDO-memory\L1-full`：1534.2 MB。
- C 镜像 `C:\Users\Administrator\.kdo-memory\L1-full-backup`：1534.2 MB，30 分钟同步增长。
- 根因：`l1_capture.py` 中 `MIRROR_ROOT = Path.home() / ".kdo-memory" / "L1-full-backup"`（home 在 C 盘）。

## 2. 实施要求（黄药师，经王语嫣编排）

1. `l1_capture.py`：去掉 C 盘镜像步骤（或 MIRROR_ROOT 置空跳过 mirror），采集后不再写 C 盘。
2. 清理现有 C 镜像目录 `C:\Users\Administrator\.kdo-memory\L1-full-backup`（约 1.5GB；删除前核对绝对路径在本目录内，不误删同盘其他目录）。
3. 体积统计口径同步：只统计 D 主库，日增约 770MB。

## 3. 容灾提示（审计者义务，不改变拍板）

去掉后 L1 全量原文为单盘（D）；事件库仍 C+D 双盘。若未来需「同盘防误删镜像」，另行立项。

## 4. 需要谁动作

| 角色 | 动作 | 经谁 |
|:--|:--|:--|
| 王语嫣 | 吸收拍板，编排立项 | — |
| 黄药师 | 改 l1_capture.py + 清理 C 镜像 | 经王语嫣 |
| 欧阳锋 | 终审留痕 | 经王语嫣编排 |
| 风清扬 | 已出本建议；实施后审计验收 | 对接老朱 + 王语嫣 |

---

*风清扬（观察者 / 审计者）· 2026-08-24 · 只审计、不实施*