---
id: task_20260816_huangyaoshi-migration-t3
assignee: huangyaoshi
status: queued
priority: P1
wsjf: 3.0
created_at: 2026-08-16
updated_at: 2026-08-16
source: 迁移建议书会审裁定（2026-08-16）
related: #343
---

# T3 duanwangye 飞书 Windows 就绪测试（#345）

## 背景
~~beikai 整体留 WSL 明确~~ —— **已过时：#347 已把 beikai 迁 Windows（2026-08-16 用户拍板全量 Windows）**，本任务聚焦 duanwangye 就绪测试收尾（实际也已迁 Windows，2026-08-18 codex 核实）。

## 任务
1. **飞书 Windows 就绪测试**（lark-cli v1.0.81 Windows auth 已就绪——#306 实测，聚焦 Bitable API/文档创建/pre-ship-check）：黄药师出方案 + Codex 只读探测协助
2. 通过 → duanwangye 按 T1 流程迁移；不通过 → 留 WSL + 专项任务（不阻塞其他批次）

## 验收标准
- duanwangye 已迁移（08-18 codex 核实）：飞书发布链路冒烟通过
- beikai 已由 #347 迁 Windows（08-16）：本任务不再涉及

## 回滚
duanwangye 迁移失败回滚 WSL；beikai 本轮不改无需回滚

## 执行门禁
⏸ **挂起：等老顽童 CLI 手头工作完成 + 用户命令**


## 挂起条件解除（2026-08-18 王语嫣编排更新）

- 老顽童 CLI 已确认空闲（2026-08-18 老顽童本尊：活跃待命、无在产任务、失忆恢复完成）
- 用户已下令起链（2026-08-18）——本任务可领取执行


## 过时文本修正（2026-08-18 王语嫣，codex 核实驱动）

- 原任务写「beikai 整体留 WSL」——与 #347（beikai 迁 Windows，用户拍板全量 Windows）冲突，已划线标注过时
- 实际状态：duanwangye 已迁 Windows（codex 08-18 只读核实）；本任务转为就绪测试收尾/状态对齐
