---
id: task_20260907_huangyaoshi-bundle-regen
title: "bundle 备份过期 47.6h 处置（kdo-wiki-bundle-backup 停摆排查+重新生成+告警阈值核实）"
seq: 673
status: queued
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-07
decision_source: vault-integrity 探针告警（09-07 02:08：bundle mtime 47.6h ago > 26h 阈值）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-07T02:50:00+08:00'
---

# #673 bundle 备份过期处置（黄药师）

## 实证
vault-integrity 探针：wiki-bundle-20260905.bundle mtime 47.6h > 26h 阈值——kdo-wiki-bundle-backup 任务疑似停摆（09-03 D 盘清理后任务状态待查）。

## 任务
1. 排查停摆原因（任务禁用？脚本失败？静默失败？）
2. 重新生成 bundle + integrity-check 通过
3. 恢复节拍或修正告警阈值（若 26h 阈值不合理需给依据）
4. 防复发：停摆原因进 infrastructure-inventory 已知故障族

## 验收
新 bundle mtime 新鲜 + integrity-check PASS + 任务恢复节拍实证。
