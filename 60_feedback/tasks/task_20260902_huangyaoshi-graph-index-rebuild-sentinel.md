---
id: task_20260902_huangyaoshi-graph-index-rebuild-sentinel
title: graph_index 归零重建 + 健康哨兵机制化（08-31 整树事故清空后语义腿空转 2 天无人发现）
seq: 622
status: in_progress
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-02
decision_source: 外部审计建议书 diag_20260902_external-audit-graph-index-empty-recur（P1）+ 王语嫣 09-02 裁定（存在性核查：.kdo/graph_index 0 字节，mtime 08-31 02:11 正落在整树事故窗口）
reviewer: 欧阳锋
instance: huangyaoshi-kimi
updated_at: '2026-09-02T15:36:42.167552+00:00'
---

# #622 graph_index 重建 + 哨兵（黄药师，P1）

## 背景（已核实）

- `.kdo/graph_index/` = 0 字节空目录，mtime 08-31 02:11——正落在整树事故窗口（02:00-02:09），清空根因大概率=事故本身（无任务记录因为不是任务干的）
- #358（08-19 PASS A）曾重建至 2349 页/5080 chunks，事故后归零，**hybrid RRF 语义腿空转 2 天**全厂静默降级（口语化检索实测全跑偏，关键词检索 BM25 兜底正常）
- 引擎层 #358 已修好不用动，本单=重建数据 + 补哨兵

## 任务

1. **重建**：按 #358 已验证流程全量重建 graph_index（先删后建，30-60min，挂后台低峰跑），重建后实测口语化查询（「我卖护肤品的，怎么让犹豫的客户快点下单」应命中转化率案例卡）
2. **哨兵机制化（本单关键增量）**：graph_index 空目录 / 0 records / 陈旧超 48h → 探针面显式告警（复用既有探针/门禁通道，不新建扫描器）——「修完没加哨兵=同类事故必再发」是 #357/#358 两轮打过的模式，这次闭环
3. 根因注记落执行报告：08-31 02:11 事故窗口归因的证据链（目录 mtime vs 事故时间线）

## 红线

- 重建挂后台，不占前台；先删后建流程按 #358 来
- 哨兵只告警不动作

## 交付

- 重建产物记录（页数/chunks 数）+ 口语化查询前后对照 + 哨兵上线实证 + 执行报告
- claim/complete 走 `python 90_control/scripts/queue_transition.py`（complete 622）

## 执行报告（2026-09-02 黄药师）

**交付物**：① `.kdo/graph_index/` 全量重建产物（graphml 6.5MB + vdb_entities/relationships/chunks + kv_store，共 ~79MB）② conveyor_probe.py 第十一信号 `_scan_graph_index_health`（kdo-tools/conveyor_probe.py，挂第九信号 infra_alerts 同通道）③ 回归测试 4 条（kdo-tools/tests/test_conveyor_probe.py）④ notification-coverage-matrix.md 行 27 同步登记（§3.19）⑤ 重建日志 `_tmp/622-graph-rebuild.log`

**完成内容**：① 重建——先删后建按 #358 流程：claim 前实测口语化查询确认 0 chunks/0 entities（空转实证），`rm -rf .kdo/graph_index` 后 `kdo graph rebuild --full` 挂后台跑完：**2428 页 / 5267 chunks / 6705 relations**（对比 #358 重建时 2349 页/5080 chunks，增量来自期间新卡）② 哨兵机制化——三档检测：空目录/缺失 → 报；graphml `<node` 字节扫描 0 节点 → 报 0 records；graphml mtime 落后 search_index.json 超 48h → 报陈旧（陈旧取 #356 双索引同步相对口径，规避手动重建节奏下绝对 48h 的常态误报——search_index 随卡片写入增量更新，是基准钟；search_index 读不出则跳过陈旧项）。沿触发幂等、恢复重新武装、原因切换重报、只告警不动作 ③ 根因注记——`.kdo/graph_index` 清空态 mtime/birth = 2026-08-31 02:11:44（stat 实证，claim 前取样），落 08-31 整树事故窗口（02:00-02:09）尾段 2 分钟内，无任何任务单/工单记录指向该目录操作，归因=事故连带清空（与王语嫣存在性核查一致）

**验证**：① 前后对照——重建前 `kdo graph query "我卖护肤品的，怎么让犹豫的客户快点下单"` = Found: 0 chunks/0 entities/0 relations（空转）；重建后同查询命中转化率域案例卡（优秀触点案例合集、棋牌室新客办卡率1%→5% 等 12 条实体），语义腿复明 ② 哨兵单测 4 条全过（空目录告警+幂等 / 0 records / 陈旧 50h 告警+10h 不告 / 恢复重新武装重报），探针全量回归 47 passed ③ 真机 dry-run：`conveyor_probe.py --dry-run --json` 健康态无告警、state 键 `graph_index_issue=None`（武装态）正常落位 ④ 健康函数对真实 ROOT 调用返回 [] 且状态键正确

**边界**：哨兵只告警不动作（本单红线）；哨兵挂探针 10 分钟拍，非实时；陈旧判定依赖 search_index.json 存在且增量更新正常（该文件自身停更是另一信号面，不在本单）；claim 走 --force 留痕（#621 挂审期间并行，台账 force-exceptions.log 可查）

**需要谁动作**：欧阳锋终审（重点核：哨兵陈旧口径取相对 search_index 而非绝对 mtime 的判断是否认可；matrix 行 27 登记口径）。无需老朱/王语嫣动作
