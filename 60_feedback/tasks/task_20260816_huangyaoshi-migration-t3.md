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
beikai（=飞书洪七公）**整体留 WSL 明确**（用户确认：迁移后 WSL 只留它——openmontage 886MB Linux 工具链 Windows 无部署，不拆双实例）。duanwangye 单独走飞书就绪测试。

## 任务
1. **飞书 Windows 就绪测试**（lark-cli v1.0.81 Windows auth 已就绪——#306 实测，聚焦 Bitable API/文档创建/pre-ship-check）：黄药师出方案 + Codex 只读探测协助
2. 通过 → duanwangye 按 T1 流程迁移；不通过 → 留 WSL + 专项任务（不阻塞其他批次）

## 验收标准
- duanwangye 若迁移：飞书发布链路冒烟通过
- beikai：保留 WSL gateway 稳定运行，工具调用无退化（本轮不动）

## 回滚
duanwangye 迁移失败回滚 WSL；beikai 本轮不改无需回滚

## 执行门禁
⏸ **挂起：等老顽童 CLI 手头工作完成 + 用户命令**
