---
id: 360
assignee: codex
status: queued
updated_at: '2026-08-19T00:30:00+00:00'
title: note-coach 迁 AppData\Local + 服务化激活（P2，#346 拆分项）——用户确认要用，现状是旧目录瘫痪态
priority: P2
dependency: []
reviewed_by: 欧阳锋
---

# #360 note-coach 迁 AppData\Local + 服务化激活（P2）

## 任务目标

note-coach 用户已确认要用（#346 队列备注 2026-08-16），但当前停在旧 `.hermes\profiles\note-coach`：未迁 AppData\Local、未 NSSM 服务化、gateway_state 陈旧（06-07）——"要用"但处于瘫痪态。本任务把它迁正激活。

## 素材/证据

- codex #346 收尾核验（2026-08-18）：note-coach 未迁 AppData\Local、未服务化、gateway_state 06-07 陈旧
- 王语嫣抽查实证（2026-08-18）：`AppData\Local\hermes\profiles\` 无 note-coach；9 个 hermes-gateway 服务无 note-coach；旧目录仍在 `.hermes\profiles\note-coach`
- 先例：#343/#344 迁移 5 项清单（skills 补拷 / config 路径修复 / WinError 87 补丁 / memories 同步 / 服务化）

## 修改范围

1. note-coach profile 迁 `AppData\Local\hermes\profiles\note-coach`（按 #344 迁移 5 项清单执行：skills/config/补丁/memories）
2. NSSM 服务化（hermes-gateway-note-coach）+ 冒烟
3. 旧目录处置：归档不真删（同 duan/kimi-test 先例）
4. 若判定 note-coach 实际无人用，回报证据由老朱改判归档——不擅自归档

## 验收标准

1. `hermes-gateway-note-coach` 服务 Running/Automatic
2. AppData\Local profile 目录齐全（SOUL/config/memories）
3. 冒烟：agent 应答正常
4. 旧目录归档留痕

## 交付

1. 迁移 + 服务化 + 冒烟证据
2. 送欧阳锋终审
