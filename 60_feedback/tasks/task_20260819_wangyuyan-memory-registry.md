---
id: 365
assignee: wangyuyan
status: queued
updated_at: '2026-08-19T01:30:00+00:00'
title: 记忆注册表 memory-registry.md（P0，codex 建议书①采纳）——唯一真相源/派生副本/命名规范/废弃清单四张表
priority: P1
dependency: []
reviewed_by: 欧阳锋
---

# #365 记忆注册表 memory-registry.md（P0）

## 任务目标

建 `20_memory/memory-registry.md`——回答"我该读哪份、哪份是最新真相"的唯一权威文件。codex 记忆一致性审计（2026-08-19）P0 建议，王语嫣裁定采纳。

## 素材/证据

- codex 建议书：`agent复盘/codex/KDO工厂记忆一致性审计报告暨任务编排建议书_2026-08-19.md` §二（5 根因全带证据，王语嫣已抽核：双轨目录/Hermes 三处漂移/入口脆弱均实锤）
- 老朱痛点（2026-08-19）："各个 agent 的记忆不一致，看的文件不一样，各种漂移各种对齐，浪费大量时间和 token"

## 修改范围

新建 `20_memory/memory-registry.md`，四张表：

1. **唯一真相源表**：每类事实 → 唯一权威位置（当前任务→production-queue.md；组织记忆→daily-context 最新；错误模式→各 agent 错误模式库；……）
2. **派生副本表**：dashboard.html/vault-status 等只读派生物，标生成脚本 + 禁手改
3. **命名规范表**：`*-amnesia-recovery.md` 去日期后缀等
4. **废弃清单表**：`新建文件夹`、`laowantong-next-tasks.md` 等（处置方式=冻结标 DEPRECATED，不真删）

## 边界（王语嫣起草 + 黄药师会审）

- 纯文件+约定，零代码零队列改动
- 不定"怎么迁"（那是 #366/#367 的活），只定"真相在哪"

## 验收标准

1. 四表齐全，真身/派生/废弃/命名逐项可 grep 定位
2. 黄药师会审通过（基建视角核可行性）
3. 欧阳锋终审

## 交付

1. memory-registry.md
2. 送欧阳锋终审
