---
id: task_20260902_huangyaoshi-graph-index-rebuild-sentinel
title: graph_index 归零重建 + 健康哨兵机制化（08-31 整树事故清空后语义腿空转 2 天无人发现）
seq: 622
status: queued
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-02
decision_source: 外部审计建议书 diag_20260902_external-audit-graph-index-empty-recur（P1）+ 王语嫣 09-02 裁定（存在性核查：.kdo/graph_index 0 字节，mtime 08-31 02:11 正落在整树事故窗口）
reviewer: 欧阳锋
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
