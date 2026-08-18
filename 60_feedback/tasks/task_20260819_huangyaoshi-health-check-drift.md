---
id: 364
assignee: huangyaoshi
status: queued
updated_at: '2026-08-19T01:30:00+00:00'
title: health-check 巡检加漂移检测（P2）——进程版本 vs 最新 commit + 双索引同步态
priority: P2
dependency:
- 361
reviewed_by: 欧阳锋
---

# #364 health-check 巡检加漂移检测（P2）

## 任务目标

运行时漂移的制度化兜底：巡检自动发现"生产进程跑旧代码/双索引不同步"，不再靠外部审查偶然撞见（小昭第四轮发现 9 进程跑 21:41 旧代码=活例）。

## 素材/证据

- 小昭第四轮（2026-08-19）：MCP server 长驻进程 21:41 vs 修复 22:39/23:44——漂移 2 小时无人发现
- #356 已建 graph/search 索引同步机制；#326 health-check 巡检 17 项框架可扩展

## 修改范围

1. **进程版本漂移检测**：kdo MCP server 进程 CreationDate vs tools.py/delivery.py 最新 commit 时间——进程早于最新修复即报警
2. **双索引同步检测**：graph_index vs search_index 版本/mtime 比对（接 #356 机制；#358 重建后生效）
3. **指针有效性**：登记副本已废（#359），改为检查指针引用目标存在且为单一真相源
4. 挂入既有 health-check 巡检序列，报告加"漂移"节
5. **监控复活并入**（小昭全面体检 2026-08-19 实锤，E025 并入不另开）：health-check 断更 4 天（最新 08-15）+ vault-snapshot 43 天未跑（vault-status.md 停 07-07）——挂 cron/hook 自动化，每日自检自跑；60_feedback/auto/ 1508 份未消费产物加消费状态标记或归档

## 边界

- 只读巡检，自动修复不在本任务（发现漂移→报警→人工/立项处置）
- 依赖 #361 先完成（重启收口拉齐基线，否则巡检首日全是噪声）

## 验收标准

1. 构造漂移（旧进程/改文件不重启）→ 巡检报警命中
2. 干净基线 → 零误报
3. 巡检报告含漂移节

## 交付

1. 巡检项实现 + 正反向实测
2. 送欧阳锋终审
