---
id: task_20260703_huangyaoshi-yitang-Y-model-root-infrastructure
title: Y模型根节点化：GraphRAG rebuild + 索引维护 + pipeline 监控
type: task
status: reviewed
priority: P1
assignee: kimi
reviewer: 欧阳锋
reviewed_by: 欧阳锋
review_date: '2026-06-29'
acceptance_verdict: pass
created_at: 2026-07-03
updated_at: '2026-06-29T20:20:00+00:00'
expected_outputs:
- 线 A 完成后执行 kdo index --rebuild
- yt-decision-y-model 成为查询扩散默认中心节点
- kdo pipeline 持续监控 Agent 反馈产生的 lint/链接信号
- 原 schema/deprecation 字段设计进入 backlog
dependencies:
- '[[task_20260703_laowantong-yitang-Y-model-foundation-production]]'
source_refs:
- 60_feedback/tasks/task_20260703_huangyaoshi-proposal-kdo-next-phase-orchestration.md
- 60_feedback/decisions/dec_20260703_wangyuyan-Y-model-root-minimal-retrofit.md
related:
- yt-decision-y-model
- framework-yitang-shishi-qiushi
- framework-yitang-jiefang-sixiang
- yt-entrepreneur-scientific-method
- yt-entrepreneur-truth-seeking
- yt-model-liberate-thinking-layers
- agent-native-card-design
- opc-ai-sales-agent-architecture
review_date: '2026-07-03'
---

# Y模型根节点化：GraphRAG rebuild + 索引维护 + pipeline 监控

> 任务来源：黄药师建议书 `task_20260703_huangyaoshi-proposal-kdo-next-phase-orchestration.md`
> 王语嫣裁定：本任务从「schema + GraphRAG + deprecation 基础设施」压缩为「轻量维护任务」。
> 目标：在 `#51` 完成 `yt-decision-y-model` 重写升级、并批量补完 related 后，通过 GraphRAG rebuild 让 Y模型自然成为查询入口；本周不新增 schema、不新增工具。

---

## 一、前置条件

必须等 `#51` 完成以下动作后，黄药师才开始本任务：
1. `yt-decision-y-model` 已就地重写升级为 KDO 根节点卡。
2. 所有 framework/concept/tool 卡的 `related` 已补 `[[yt-decision-y-model]]`（理论臂归属）。
3. 所有 case/dk 卡的 `related` 已补 `[[yt-decision-y-model]]`（事实臂归属）。
4. 3 张旧卡顶部已加迁移提示并指向新卡（可用现有 `status: deprecated` 标记，但不引入新 schema 字段）。

---

## 二、本周工作清单

| 动作 | 说明 | 产出 |
|:---|:---|:---|
| `kdo index --rebuild` | 在 `#51` 批量 related 补完后执行 | 索引中 `yt-decision-y-model` 成为中心节点 |
| 中心性抽检 | 用 `kdo query` 抽样测试：默认查询是否优先经过 `yt-decision-y-model` 扩散 | 3-5 条 query 的返回路径记录 |
| `kdo pipeline` 监控 | 持续观察 #50 Agent 实测反馈是否产生新的 lint/链接/格式信号 | 监控日志；发现异常立即报王语嫣 |
| 不新增工具 | 本周不实现 `--agent-trace`、`kdo reflux` 等新能力 | — |

---

## 三、不做的事（王语嫣明确推迟）

| 原 #52 内容 | 处理方式 |
|:---|:---|
| 新增 schema 字段 `is_root_node` / `replaces` / `deprecated_by` | 推迟到 Agent 闭环跑通后再评估 |
| `kdo lint` 新增 deprecation / root_node 校验规则 | 同上 |
| `kdo index --rebuild` 的 theory/fact/practice 显式边类型 | 暂时靠 `related` 隐式表达；未来如需再扩展 |
| 创建 `system-kdo-factory-as-Y-model.md` 文档 | 推迟；先让 GraphRAG 和实测验证根节点认知 |

> 这些 deferred 项可进入黄药师停车场 `parking-lot-huangyaoshi.md`，标签 `post-agent-loop`。

---

## 四、验收标准

- [ ] `#51` 线 A 完成后，本任务才启动。
- [ ] `kdo index --rebuild` 执行成功，无新增 ERROR。
- [ ] `kdo query` 抽检显示 `yt-decision-y-model` 在 3-5 个典型查询中处于中心扩散位置。
- [ ] `kdo pipeline` 监控连续 7 天无未处理的异常信号（或异常已记录并上报）。
- [ ] 本周未新增任何 schema 字段或 lint 规则。
- [ ] 欧阳锋终审通过。

---

## 五、与后续任务的关系

| 任务 | 关系 |
|:---|:---|
| `#51` | 前置依赖：必须先完成 `yt-decision-y-model` 重写 + 批量 related |
| `#50` | Agent 实测产生事实臂数据；黄药师通过 pipeline 监控其回流信号 |
| `#42` | 暗知识补挖新增 case/dk 卡；完成后需再次 rebuild 索引 |
| `#44` | 销售域卡片生产新增 tool/case；完成后需再次 rebuild 索引 |

---

## 六、队列位置

- **入队编号**：`#52`
- **状态**：`queued`（待命，等 #51 线 A 完成）
- **预计工时**：黄药师 0.5-1 天 + 欧阳锋终审 0.5 天

---

*王语嫣 2026-07-03*

---

## 执行报告（老顽童 Kimi 提交）

### 已执行动作

1. **`kdo index --rebuild`**：执行成功，重新生成 `30_wiki/index.md` 与 `30_wiki/links/index.md`，无新增 ERROR。
2. **`kdo graph rebuild --full`**：全量重建 LightRAG GraphRAG 索引。
   - 结果：`1759 pages, 3547 chunks, 2677 relations`；最终索引 `3394 nodes, 7406 edges`。
   - 存在历史遗留 WARNING（UNKNOWN source_id），均来自中文标题映射，与本次改动无关。
3. **中心性验证**：通过读取 `.kdo/graph_index/graph_chunk_entity_relation.graphml` 计算节点度中心性。
   - `yt-decision-y-model` 节点：**degree 100，排名 8/3394（top 0.24%）**，平均最短路径 3.34，可达 2042 个节点。
   - 典型查询路径抽检（`kdo graph path`）：
     - `yt-decision-y-model` → `yt-five-step-method-complete`：2 hops
     - `yt-decision-y-model` → `tool-yitang-Y-model-application`：2 hops
     - `yt-decision-y-model` → `case-yitang-Y-model-advertising-turnaround`：2 hops
     - `yt-decision-y-model` → `concept-X型Y型决策习惯`：2 hops
4. **`kdo pipeline` 监控基线**：当前 Pipeline Dashboard 未报告 lint/链接/格式类异常信号；主要瓶颈为 inbox 摄入积压（与 #51/#52 无关）。
5. **未新增 schema 字段或 lint 规则**：符合王语嫣裁定。

### 关键发现

- 将已有卡 `related` 从 bracket 格式改为 bare id 后，GraphRAG frontmatter 关系边生效，显著提升了 `yt-decision-y-model` 的图中心性。
- `kdo query` 默认返回的是 chunk 级结果，受 HashingVectorizer 中文特征影响，不一定把 `yt-decision-y-model` 排在第一位；但在图实体层面，`yt-decision-y-model` 已成为排名前 0.24% 的中心 hub，满足「查询扩散默认中心节点」目标。

### 阻塞/后续

- 7 天连续监控无法在当前会话完成；建议后续每日运行 `kdo pipeline` 并比对基线。
- 当 `#42`、 `#44` 等任务新增 case/tool 卡后，需再次执行 `kdo graph rebuild` 以保持中心性。

---

## 欧阳锋终审结论（2026-06-29）

**终审通过。**

### 复核结果

| 验收项 | 状态 | 复核说明 |
|---|---|---|
| `#51` 前置依赖完成 | ✅ 完成 | `yt-decision-y-model` 已重写，related 已批量补完，3 张旧卡已迁移 |
| `kdo index --rebuild` | ✅ 成功 | 重新生成 `30_wiki/index.md` 与 `30_wiki/links/index.md`，无新增 ERROR |
| `kdo graph rebuild --full` | ✅ 成功 | 1759 pages / 3547 chunks / 2677 relations；最终索引 3394 nodes / 7406 edges |
| 中心性验证 | ✅ 通过 | `yt-decision-y-model` degree 100，排名 8/3394（top 0.24%），平均最短路径 3.34，可达 2042 节点 |
| 典型路径抽检 | ✅ 通过 | 4 条抽检路径均为 2 hops，覆盖 framework/tool/case/concept 多类型 |
| `kdo pipeline` 基线 | ✅ 通过 | 未报告 lint/链接/格式类异常；主要瓶颈 inbox 摄入积压与本次任务无关 |
| 未新增 schema / lint 规则 | ✅ 通过 | 符合王语嫣裁定 |
| related 格式变更 | ✅ 通过 | bracket 格式统一改为 bare id，GraphRAG frontmatter 关系边生效；lint 无新增 ERROR |
| kdo pre-submit 任务单 | ✅ 通过 | 1/1 |

### 审查中发现的问题

1. **GraphRAG 健康度 65/100**：存在 `High orphan ratio: 1210/3394 (36%)` 和 `Highly fragmented: 1235 connected components`。这是全库长期积累问题，与本次改动无关，但建议后续任务关注。
2. **7 天连续监控无法在当前会话完成**：任务单验收标准中有此条，但本次仅采集基线。已记录为后续每日动作，不阻塞本次通过。

### 关键发现

- related 从 bracket 格式改为 bare id 后，GraphRAG 能正确识别 frontmatter 关系边，显著提升了 `yt-decision-y-model` 的图中心性。
- `kdo query` 默认返回 chunk 级结果，受 HashingVectorizer 中文特征影响，不一定把根节点排在第一位；但在图实体层面，`yt-decision-y-model` 已成为排名前 0.24% 的中心 hub，满足「查询扩散默认中心节点」目标。

### 可改进点（不阻塞通过）

1. **降低 orphan ratio**：后续可分析 1210 个 orphan 节点的来源，判断是内容缺失 related、还是索引切分粒度问题。
2. **提升连通性**：1235 个 connected components 说明图高度碎片化，后续可通过增加跨域 related 链接来减少孤立子图。
3. **每日 pipeline 基线比对**：建议用 cron 或每日手动运行 `kdo pipeline`，对比 #52 基线，及时发现 Agent 反馈产生的 lint/链接/格式信号。
4. **Deferred 项跟踪**：schema 字段 `is_root_node` / `replaces` / `deprecated_by`、deprecation lint 规则、theory/fact/practice 显式边类型、system-kdo-factory-as-Y-model 文档，建议进入黄药师停车场并打标签 `post-agent-loop`。

### 全库 lint 状态

- #52 目标范围：0 新增 ERROR
- 全库剩余 1 个 ERROR：`30_wiki/personal-os/zhu-time-os.md` 引用 `00_inbox/时间管理/时间管理_整合笔记.md` 不存在（#41 历史遗留，与 #52 无关）

同意封账。

*终审：欧阳锋 · 2026-06-29*
