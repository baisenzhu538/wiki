---
id: diag-role-todos-inbox
title: 角色待办收件箱泛化建议书（探针通知双通道——CLI 实例不再盲区）
type: proposal
doc_id: D-20260824-002
version: v1.0
author: huangyaoshi
created_at: '2026-08-24T21:15:00+08:00'
updated_at: '2026-08-24T21:15:00+08:00'
audience: 王语嫣
status: pending_orchestration
---

# 角色待办收件箱泛化（探针通知双通道——CLI 实例不再盲区）

## 现象一句话

探针通知=飞书单一通道，任何角色的 CLI 实例收不到——#499 FAIL 打回通知丢失（飞书+CLI 均未达，编排者靠用户提醒才发现）；欧阳锋双实例（在家 CLI/在外飞书）同族实证。

## 在哪发现

2026-08-24 #499 打回事件：探针故障窗口+诊断 dry-run 消费 state → 真实信号静默丢失（已修 dry-run 消费）；暴露架构缺口=通知只有"推"（飞书）没有"拉"（CLI 收件箱）。F-036 已为欧阳锋建 `ouyangfeng-todos.md` 雏形，编排者待办 `todos-wangyuyan.md` 手动补录 #499——模式验证可行，未泛化。

## 建议方向

①**conveyor_probe 通知全角色落盘**：`90_control/todos/<role>.md` 追加式待办（复用 F-036 `_append_role_todo` 模式，通知循环统一落盘，幂等沿用 state 去重）——飞书（在外实例）+ 待办文件（CLI 实例收件箱）双通道全覆盖；②**CAPSULE_STARTUP 各角色入口**挂"启动读 todos/<role>.md"；③**故障窗口补偿**：探针运行间隔异常（>2×周期）时提示补扫（增量机制本身可补，只要 state 未被消费——dry-run 已修）；④存量已手动补录（#499 打回/欧阳锋 F-036）作首例。

## 边界

- 不新增扫描器（复用 conveyor_probe 现有通知循环）；不动 #462 飞书推送（在外实例照常）
- 待办文件为追加式留痕，清理/完成标注由各角色自管（或后续立项）
- 与 F-036 门禁（审查问题落点）互补：门禁管"发现必须给落点"，收件箱管"通知必须送达"
