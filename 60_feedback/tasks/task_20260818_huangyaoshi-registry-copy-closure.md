---
id: 359
assignee: huangyaoshi
status: reviewed
updated_at: '2026-08-18T16:32:41.461909+00:00'
title: 登记副本与 commit 收口（P1）——40_outputs/code/scripts 版本分裂根治 +
priority: P1
dependency: []
reviewed_by: 欧阳锋
review_date: '2026-08-18'
grade: A
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

## 执行记录（2026-08-18 黄药师，已提审）

### 机制裁定：指针引用单一真相源（三选一中第 2 项）

**理由**：MCP 工具链活代码在 `kdo-tools/mcp/`（启动入口 run_kdo_mcp.cmd 指那里），`40_outputs/code/scripts/` 副本无任何运行时/文档引用（grep 全库确认）——副本唯一作用是"登记展示"，拷副本必然漂移（08-18 已实证两轮 stale-copy 误诊）。废弃副本+README 指针引用，物理上杜绝漂移；本目录其他脚本（ocr-*.py 等）是真身非副本，保持不动。

### 执行证据

- 副本删除：`40_outputs/code/scripts/{tools.py,server.py,sync-hermes-mcp.py}` 已删（tools.py 漂移 70 行实证；server.py/sync 当时 diff=0 一并收掉防再生）
- README 更新：登记规则节（副本禁放+指针引用+登记四步法补漏）+ MCP 工具链指针表
- commit 哈希：`95e8c7e4d`（登记处置+队列解冻流转）；#350-#353 实体文件与任务族由 vault backup `4e08ca1f7`（23:36）收净
- 验收 2 补充：备份 commit 为自动机制（message 非主题化），本次已核 git log 确认实体文件全部入 git；工作区残留仅 dashboard.html（他会话产物）

### 登记四步法补漏

漏洞点：四步法第 1 步"脚本放入 40_outputs/code/scripts/"与"活代码在 kdo-tools/"冲突——登记人不知该拷还是该指。补漏：README 顶部登记规则明确"有活代码的脚本禁放副本，登记=指针"；后续可考虑在 startup.md 工具登记纪律节同步（D4 审批后）。
