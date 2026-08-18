---
id: 366
assignee: huangyaoshi
status: queued
updated_at: '2026-08-19T01:30:00+00:00'
title: CAPSULE_STARTUP 升级统一启动指针（P1，codex 建议书②采纳）——version/git_head/队列尾 + 角色路由
priority: P1
dependency:
- 365
reviewed_by: 欧阳锋
---

# #366 CAPSULE_STARTUP 升级统一启动指针（P1）

## 任务目标

升级 `.kdo/CAPSULE_STARTUP.md` 为全厂唯一启动指针：所有 agent 启动只读它，按角色路由到具体必读文件。治"入口文件多 + 角色识别靠工作目录脆弱信号"（codex 根因 4；08-19 王语嫣亲历被 AGENTS.md 规则误判黄药师）。

## 素材/证据

- codex 建议书 §二根因 4 + §三业界实践（统一启动指针+路由）
- E034 三连实证（08-18）：启动/审查不对齐 git HEAD + 队列尾 = 过时快照事故
- 现有入口：CLAUDE.md / AGENTS.md / .agent/startup.md / 各 *-context.md——收敛为指针路由，不删文件

## 修改范围

1. **指针固定字段**：version / updated_at / git_head / 队列尾任务号
2. **启动流程统一**：读指针 → 校验版本（git_head 不一致=停下读真相源，不治标继续）→ 按角色路由到 role-context + context.md + 队列 + 最新 daily-context（按目录最新，不写死日期）
3. **各入口收敛**：CLAUDE.md/AGENTS.md/.agent/startup.md 改为指向指针的薄壳
4. 路由表与 #365 memory-registry 的真相源表一致（单一真相源，不两套）

## 边界

- 纯文件+约定，零代码
- 依赖 #365（注册表先定真相在哪，指针才有路由依据）

## 验收标准

1. 指针四字段齐全
2. 任一 agent 实例只读指针即可定位全部必读文件（抽 2 角色实测）
3. git_head 校验不一致时行为正确（停下而非带病继续）

## 交付

1. 指针 + 薄壳改造 + 实测
2. 送欧阳锋终审
