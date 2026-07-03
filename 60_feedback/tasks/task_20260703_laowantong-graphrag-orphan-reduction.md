---
id: task_20260703_laowantong-graphrag-orphan-reduction
title: GraphRAG 健康度提升：跨域 related 补链降低 orphan 比例
type: task
status: in_progress
priority: P2
assignee: kimi
reviewer: 欧阳锋
created_at: 2026-07-03
updated_at: '2026-07-03T18:48:18.029009+00:00'
expected_outputs:
- orphan 卡片来源分析报告
- 跨域 related 补链方案
- 至少 100-200 张 orphan 卡补完 related（目标：orphan 比例从 36% 降至 ≤30%）
- kdo graph stats --health 复测报告
dependencies:
- task_20260703_huangyaoshi-yitang-Y-model-root-infrastructure reviewed
source_refs:
- 60_feedback/tasks/task_20260703_huangyaoshi-yitang-Y-model-root-infrastructure.md
related:
- yt-decision-y-model
- agent-native-card-design
- graph-rag
---

# GraphRAG 健康度提升：跨域 related 补链降低 orphan 比例

> 任务来源：`#52` 终审结论中的可改进点：GraphRAG 健康度 65/100，orphan 比例 36%，1235 个 connected components。
> 目标：通过分析 orphan 来源并补充跨域 related 链接，提升图连通性，不引入新 schema 或 lint 规则。

---

## 一、背景

`#52` 终审时 GraphRAG 重建成功，但健康度指标显示：

- **orphan 比例**：36%
- **connected components**：1235 个
- **健康度**：65/100

欧阳锋判断这是历史积累，与本次任务无关，但建议后续任务分析 orphan 来源并增加跨域 related 链接。

---

## 二、任务目标

不追求 0 orphan，而是有策略地降低：

| 指标 | 当前 | 目标 |
|:---|:---|:---|
| orphan 比例 | 36% | ≤30% |
| connected components | 1235 | ≤900 |
| 健康度 | 65/100 | ≥72/100 |

实现方式：**识别孤立卡片簇 → 找到最近的跨域连接点 → 补充 related 链接**。

---

## 三、执行步骤

### 3.1 分析 orphan 来源

- 运行 `kdo graph stats --orphans`（或等效命令）导出 orphan 卡片列表。
- 按卡片 type 和 domain 聚类，识别最大孤立簇。
- 分类：
  - **可自然连接**：与其他域有概念关联，只是没建 related。
  - **需要桥接卡**：跨域概念之间缺一张桥接卡。
  - **暂时无法连接**：内容过于孤立，进入 backlog。

### 3.2 制定补链策略

| 孤立簇类型 | 补链策略 |
|:---|:---|
| 同一域内的孤岛 | 补 domain digest / index 卡作为 hub |
| 跨域相关但未链接 | 在两张卡 frontmatter 中互加 related |
| 有概念关联但缺桥接 | 建议新建 1-2 张桥接 concept/framework 卡（需王语嫣判断） |
| 历史遗留 / 待归档 | 标记为 `post-agent-loop` backlog，本次不处理 |

### 3.3 批量补 related

- 对筛选出的 orphan 卡，用 `kdo link-suggest` 或直接人工判断补充 related。
- 优先补充指向/来自以下 hub 节点的链接：
  - `yt-decision-y-model`（根节点）
  - 各域 digest/index 卡
  - 高频概念卡（如 `yitang-methodology-system`、`framework-kdo-self-attack`）

### 3.4 复测

- 补链后重新运行 `kdo index --rebuild` 和 `kdo graph stats --health`。
- 输出前后对比报告。

---

## 四、验收标准

- [ ] orphan 来源分析报告完成，识别 Top 5 孤立簇。
- [ ] 补链方案经王语嫣确认。
- [ ] 至少 100-200 张 orphan 卡补完真实 related 链接（非占位）。
- [ ] `kdo lint` 0 新增 ERROR。
- [ ] `kdo graph stats --health` 复测：orphan 比例 ≤30%，connected components ≤900，健康度 ≥72/100。
- [ ] 欧阳锋抽检 ≥20 张补链卡片的相关性质量。
- [ ] 欧阳锋终审通过。

---

## 五、与后续任务的关系

| 任务 | 关系 |
|:---|:---|
| `#52` | 前置依赖：GraphRAG 已重建，基线数据已采集 |
| `#54` 已消化素材案例补扫 | 可并行；案例补扫发现的新 case 可能成为 orphan 卡的新连接点 |
| `#55` Y模型 OS | 不阻塞；OS 层建设与图结构无关 |

---

## 六、队列位置

- **入队编号**：`#57`
- **状态**：`queued`
- **预计工时**：老顽童 2-3 天 + 欧阳锋抽检/终审 1 天

---

*王语嫣 2026-07-03*
