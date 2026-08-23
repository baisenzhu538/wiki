---
id: queue-dashboard-field-map
title: 队列-工作台字段映射（W6 落地文档）
type: protocol
version: v1.0
doc_id: D-20260823-003
author: 王语嫣
created_at: '2026-08-23T09:00:00+00:00'
updated_at: '2026-08-23T09:00:00+00:00'
status: effective
effective_from: '2026-08-23'
approved_by: 老朱（会诊 W6 拍板：队列管执行流转、工作台管全员可见，字段映射写进落地文档）
---

# 队列-工作台字段映射（W6 落地文档）

> 分工总纲（会诊 W6 老朱拍板）：**队列（production-queue.md）管执行流转；工作台（dashboard.html）管全员可见**。字段口径单一真相源=队列，工作台全派生。

## 一、状态字段（队列唯一，工作台派生）

| 状态 | 归属 | 写入者 | 工作台展示 | 可领取 |
|:--|:--|:--|:--|:--|
| `queued` | 队列行状态列 | queue_transition（立项时王语嫣写初值） | 待领取 | ✅ |
| `claimed-<instance>` | 队列行状态列 | queue_transition claim | 进行中（显示实例名） | ❌ |
| `pending_review` | 队列行状态列 | queue_transition complete | 审查中 | ❌ |
| `reviewed` | 队列行状态列 | queue_transition review | 已完成 | ❌ |
| `waiting-external` | 队列行状态列 | queue_transition mark-waiting | 等外部（不阻塞他单） | ❌ |
| `cancelled` | 队列行状态列 | queue_transition cancel（#461，待实施） | 已取消 | ❌ |
| frontmatter `status` | 任务单 frontmatter | **queue_transition 独占**（上板冻结唯一例外） | 不展示 | — |

## 二、归属字段

| 字段 | 写入者 | 口径 |
|:--|:--|:--|
| 队列行 `assignee` 列 | 王语嫣（立项时） | 角色名 |
| 任务单 frontmatter `assignee` | queue_transition claim（#444 起） | 角色名（hermes/kimi→laowantong 映射）；实际实例另存 `instance` 字段 |
| 任务单 frontmatter `id` | 王语嫣（立项时） | 队列号 #xxx，三层编号不混用（E045） |

## 三、派生字段（工作台生成，禁手写——B2-4）

| 工作台字段 | 来源 | 生成方式 |
|:--|:--|:--|
| 总任务数 | 主表行数+归档累计 | generate-dashboard.py 扫描 |
| 待领取/进行中/审查中/已完成 | 队列状态列分组统计 | 同上 |
| 任务名/assignee/验收要点 | 队列行直读 | 同上 |

**纪律**：dashboard 全部字段派生生成，**任何手工编辑 dashboard.html=违规**（B2-4 状态字段队列生成禁手写）；数字与队列不一致时以队列为准并重跑生成脚本。

## 四、REVIEW-PENDING / INBOX-PENDING / PROPOSAL-PENDING 段

- 三段均由脚本自动维护（queue_transition / watch_inbox / conveyor_probe），**勿手改段结构**；王语嫣仅划掉待裁行（PROPOSAL-PENDING）
- 段行已划掉记录保留 30 天，随队列瘦身归档（#453）

## 五、变更纪律

- 本映射变更=新任务书（文件流转规范 §已交冻结）；字段增减先改本映射再改脚本
- 关联：charter §3.15（上板冻结）/ #444（assignee 口径）/ #453（归档）/ #461（cancel）
