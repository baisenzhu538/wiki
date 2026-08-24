---
id: 501
assignee: huangyaoshi
status: queued
updated_at: '2026-08-24'
version: v0.1
instance: huangyaoshi
---

# #501 角色待办收件箱泛化（探针通知双通道——CLI 实例不再盲区）

- **任务号**：#501
- **状态**：queued
- **assignee**：huangyaoshi（conveyor_probe 扩展+入口挂载；王语嫣编排；欧阳锋终审）
- **优先级**：P1（治编排者盲区——#499 FAIL 打回通知丢失实证：飞书+CLI 均未达，编排者靠用户提醒才发现）
- **立项**：2026-08-24 王语嫣（黄药师建议书 `diag_20260824_huangyaoshi-role-todos-inbox.md` 裁定采纳）

## 背景

探针通知=飞书单一通道，任何角色的 CLI 实例收不到——#499 FAIL 打回通知丢失（飞书+CLI 均未达，编排者靠用户提醒才发现）；欧阳锋双实例（在家 CLI/在外飞书）同族实证。根因：通知只有"推"（飞书）没有"拉"（CLI 收件箱）。F-036 已建 `_append_role_todo` 模式 + `90_control/ouyangfeng-todos.md` 雏形 + `todos-wangyuyan.md` 手动补录 #499 首例——模式验证可行，未泛化。

## 任务

1. **conveyor_probe 通知全角色落盘**：`90_control/todos/<role>.md` 追加式待办（复用 F-036 `_append_role_todo`，通知循环统一落盘，幂等沿用 state 去重）——飞书（在外实例）+ 待办文件（CLI 实例收件箱）双通道全覆盖
2. **CAPSULE_STARTUP 各角色入口**挂"启动读 todos/<role>.md"
3. **故障窗口补偿**：探针运行间隔异常（>2×周期）时提示补扫（增量机制本身可补，只要 state 未被消费——dry-run 已修）
4. 存量已手动补录（#499 打回/欧阳锋 F-036）作首例，验收时核对

## 验证（验证分层）

- L1：conveyor_probe 通知事件同时落盘 todos/<role>.md（state 幂等去重，重跑不重复追加）
- L2 狗粮：制造一次终审/建议书事件，CLI 侧读 todos 文件可查（非飞书侧）
- L3 待活体：下一次角色流转事件（提审/打回/建议书）CLI 实例不再靠用户提醒

## 边界

- **不新增扫描器**（复用 conveyor_probe 现有通知循环）
- **不动 #462 飞书推送**（在外实例照常）
- 待办文件追加式留痕；清理/完成标注由各角色自管（或后续立项）
- 与 F-036 门禁互补：门禁管"发现必须给落点"，收件箱管"通知必须送达"

## 关联

- 黄药师建议书 `diag_20260824_huangyaoshi-role-todos-inbox.md`
- #462（探针流转完成信号——飞书通道，本单补 CLI 通道）
- F-036（agent复盘 git 化 + `_append_role_todo` 模式源）
- #499 打回事件（本单触发实证）

## 需要谁动作

- **黄药师**：conveyor_probe 扩展 + CAPSULE_STARTUP 挂载
- **王语嫣**：验收 CLI 收件箱效果（下次流转事件）
- **欧阳锋**：终审本单

## 执行报告（F-034 五字段，complete 前必填）
