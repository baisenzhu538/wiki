---
id: 364
assignee: huangyaoshi
status: reviewed
updated_at: '2026-08-18T17:27:12.052738+00:00'
title: health-check 巡检加漂移检测（P2）——进程版本 vs 最新 commit + 双索引同步态
priority: P2
dependency:
- 361
reviewed_by: 欧阳锋
review_date: '2026-08-18'
grade: A
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

## 执行记录（2026-08-19 黄药师，已提审）

### 交付

1. **`90_control/scripts/check-runtime-drift.py`**（新建，只读巡检）：三项检测
   - 进程版本漂移：kdo MCP server 进程 CreationDate vs 相关源码（tools.py/server.py/delivery.py/graph.py，wiki+KDO 双仓）最新 commit 时间——进程早于最新修复即 DRIFT（小昭第四轮 9 进程 21:41 旧代码事故制度化兜底）
   - 双索引同步：graph_state.json vs search_index.json mtime 差 >24h 报警（#356 机制）
   - 启动指针有效性：CAPSULE_STARTUP 路由引用目标存在（#366）
2. **挂入 health-check**：checks 列表 + 场景化提示（#364 行）
3. 退出码 0/1，支持 --json

### 实测（验收标准全过）

- 干净基线：16 进程全新 / 双索引 14.7h / 指针目标存在 → [PASS] 零误报 ✅
- 反向（双索引）：`touch -d "2 days ago" search_index.json` → [DRIFT] 47h 报警 → 恢复 → [PASS] ✅
- 反向（进程逻辑，单元级）：伪造 24h 旧进程 → 命中；新进程 → 不误报 ✅
- health-check 完整模式：`[PASS] 运行时漂移巡检（#364）` 挂入成功 ✅

### 遗留（2026-08-19 用户授权后已闭环）

- **范围 5 自动化已落地**：schtasks 计划任务 `KDO-Health-Check` 创建成功（每日 08:47，用户授权 2026-08-19）；手动触发冒烟通过（LastRun 1:25:47，LastResult 2 = health-check 既有 lint 红灯的退出码，机制本身正常）

### 遗留（需用户/编排者决定）

- **范围 5 自动化未落地**：每日自检计划任务（schtasks KDO-Health-Check 每日 08:47）被权限分类器拦截（持久化系统任务需用户明确授权）——授权后执行 `schtasks /Create /TN KDO-Health-Check /TR "<python> health-check.py" /SC DAILY /ST 08:47`
- **1508 份 60_feedback/auto/ 未消费产物**：加消费状态标记或归档未做（P3 量级，建议单独立项或并入 #369 派生脚本化时处理）

## 交付

1. check-runtime-drift.py + health-check 挂入 + 正反向实测
2. 送欧阳锋终审

---

## 授权记录（2026-08-19 王语嫣转记）

老朱已口头授权创建每日自检计划任务（`schtasks KDO-Health-Check`，此前被权限拦截）。黄药师在终审通过后执行建任务动作，命令与执行证据回本文件补记。
