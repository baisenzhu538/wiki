---
id: 359
assignee: huangyaoshi
status: queued
updated_at: '2026-08-18T16:30:00+00:00'
title: 登记副本与 commit 收口（P1）——40_outputs/code/scripts 版本分裂根治 + #350-353 实体文件入 git
priority: P1
dependency: []
reviewed_by: 欧阳锋
---

# #359 登记副本与 commit 收口（P1）

## 任务目标

收口 08-18 终审暴露的两个交付完整性缺口：登记副本版本分裂 + 在审任务实体文件未入 git。

## 素材/证据

- 版本分裂实锤：`40_outputs/code/scripts/tools.py`（20:18 旧版）vs `kdo-tools/mcp/tools.py`（22:39 活代码）diff 70 行——小昭第三轮审查与欧阳锋终审初版各踩一次 stale-copy 误诊（欧阳锋终审新发现 1）；且整个 `40_outputs/code/scripts/` 目录 untracked，不在版本控制内
- 未提交实锤（王语嫣 git status 2026-08-18）：`kdo-tools/mcp/server.py`（#350 UTF-8 + #353 协议合规实体）、`mcp/config.yaml`、`feishu_doc_server.py`、`openmontage_compact_server.py`、`sync-hermes-mcp.py`、`agents/hermes-mcp-template.yaml` 全部 Modified 未提交——#350/#351/#353 已 reviewed 但代码不在 git 里
- 欧阳锋终审移交（2026-08-18）：登记副本同步并入黄药师下批

## 修改范围

1. **登记副本根治**：`40_outputs/code/scripts/` 与 kdo-tools 活代码对齐；同时给出机制裁定——自动同步脚本 / 改指针引用单一真相源 / 废弃登记副本，三选一黄药师调研建议、任务单留裁定理由。**不接受手工拷贝了事**（手工拷贝必再腐烂，今天已实证两轮）
2. **commit 收口**：上述 #350/#351/#353 实体文件 + 08-18 任务文件族（#350-#359 任务单、queue、dashboard、诊断文档）一次 commit，message 注明范围
3. **工具登记四步法核查**：登记流程哪一步漏了导致副本腐烂，补流程或改文档

## 边界

- 不改任何代码逻辑（纯收口/机制任务）
- 其他会话的 inbox/微信采集资产不入本任务 commit（各自会话收口）

## 验收标准

1. `40_outputs/code/scripts/` 与活代码一致（diff=0）或目录已按裁定处置，机制防复发落地
2. `git status` 中 #350-#353 实体文件与 08-18 任务文件族清零
3. 登记四步法补漏文档化

## 交付

1. 机制裁定 + 同步证据 + commit 哈希
2. 送欧阳锋终审
