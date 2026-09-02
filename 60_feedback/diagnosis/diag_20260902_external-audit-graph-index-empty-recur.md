---
id: diag_20260902_external-audit-graph-index-empty-recur
title: graph_index 重建后再次归零——hybrid RRF 语义腿空转一周无人发现（口语化检索实测失败）
type: proposal
status: orchestrated
author: 外部第三方审计（2026-09-02 会话）
created_at: 2026-09-02
audience: 王语嫣
priority: P1
tags:
  - infrastructure
  - index
  - graph-rag
  - search-quality
  - recurrence
source_refs:
  - 60_feedback/tasks/task_20260818_huangyaoshi-graph-embedding-pipeline.md
  - .agent/friction-log.md
  - 90_control/kdo-scalability-roadmap-10k-cards.md
  - 60_feedback/diagnosis/diag_20260902_xiaozhao-外部基础设施审计与治理建议.md
---

# graph_index 重建后再次归零——hybrid RRF 语义腿空转，口语化检索实测失败

> **定位**：外部第三方审计投递（观察者通道，同小昭/风清扬惯例：只诊断与建议，不动队列/看板/代码，不手改 production-queue）。本建议书中的修复动作执行权归黄药师，编排裁定权归王语嫣。

## 发现（2026-09-02 实测证据）

**现象**：`.kdo/graph_index/` 目录 **0 字节空**（目录时间戳 08-31 02:11）；`kdo query` 启动日志显示
"Created new empty graph file" + 全部 `0 records`（0 entities / 0 relations / 0 vector chunks）。

**时间线**（证据链）：

| 日期 | 事件 | 证据 |
|:--|:--|:--|
| 07-04 | graph_index 陈旧 | friction-log 08-18 记录（O-15/O-16 家族） |
| 08-18 | #358 立项：graph 向量库空，hybrid RRF 的 graph 腿名存实亡（王语嫣 P1） | task_20260818 任务单 |
| 08-19 | #358 修复 PASS A（根因 A-D 全修），**重建 graph_index：2349 页/5080 chunks**，备份 `graph_index.bak_20260818` | task_20260818 执行记录 |
| 08-31 02:11 | graph_index 归零（无任何任务/提交记录对应此操作——08-30/31 git log 全为 #584 无关提交） | git log + 目录 mtime |
| 09-02 | 本次体检实测：0 records，query 全部走 BM25 fallback | 本次运行日志 |

**检索质量实测对照**（同一主题两种问法，`kdo query --limit 5`）：

- 关键词问「什么是科学销售五步法」→ Top1 精准命中 framework 卡（30.32）✅
- 关键词问「古法护肤 转化率 私董会」→ Top1 命中对应案例卡（60.62）✅
- **口语化问「我卖护肤品的，怎么让犹豫的客户快点下单？」→ Top5 全跑偏**（返回统计操纵文章/24 行业获客清单等），完美匹配的转化率案例卡未进榜 ❌

**结论**：卡与 BM25 索引都在（`search_index.json` 597MB，09-02 23:11 仍更新），丢的是**语义向量 + 实体图腿**。
长句/口语/同义改写 = 撞字面，撞不到就丢——知识库定位（AI for Business 语义检索）的核心场景受损。

## 为什么这是"复发事故"而非新问题

1. **#358 已修引擎层且重建成功（08-19 PASS A），一周后索引再次消失**——修复未持久化，且无任何机制发现它又丢了。
2. **消费层不可见问题依旧**（#358 判 P1 的核心理由）：engine 字段仍显示 hybrid RRF，graph 腿空转一周，期间全厂 query 静默降级无人察觉——直到本次手工体检。
3. **可疑背景关联**：xiaozhao 09-02 外部审计指出 **C 盘 95% 满（剩 18G）**，`graph_index.bak_20260818` 08-19 遗留待清——清空动作疑似磁盘清理/rebuild 中断（先删后建流程），但**无任务记录、无留痕**。

## 建议（供王语嫣编排）

1. **P1 定位清空根因 + 全量重建**：查 08-31 02:11 前后操作（磁盘清理？rebuild 中断？同步机制误删？），用 #358 已验证流程重建（先删后建，30-60min，低峰执行，建议挂后台）。
2. **P1 健康哨兵机制化（本次最关键的增量）**：graph_index 空/陈旧/0 records → 探针或 infra-status 显式告警。**#358 修完没加哨兵 = 同类事故必然再发**——"失败不可见"是 #357/#358 两轮都在打的模式，这次补上防复发闭环。
3. **P2 容量方案衔接**：`search_index.json` 597MB 冷加载 >300s（friction 08-18 已记录）与 C 盘 95% 满同源——接 xiaozhao 审计与 scalability roadmap 的索引瘦身/分片决策，一并排期。

## 合规声明

- type: proposal / status: pending_orchestration / audience: 王语嫣（探针契约三元组齐全）
- 关联任务 #358 已 reviewed（PASS A），本建议书为复发实证升级，不重复其修复内容

---

## 王语嫣裁定（09-02 23:25）：存在性核查通过（graph_index 0 字节，mtime 08-31 02:11 落整树事故窗口）——「复发」定性修正为「事故清空+无哨兵未重建」；采纳立项 #622（重建+哨兵，P1）。容量衔接归 F-010（等老朱拍板）。
