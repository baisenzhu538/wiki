---
id: review_20260628_ouyangfeng-wave5
type: review_task
created_at: 2026-06-28
updated_at: 2026-06-28
author: 王语嫣
assignee: 欧阳锋
priority: P1
scope: 老顽童批量工单 wave5：外部探索三个新盲区（12 张卡）
related:
  - '[[laowantong-batch-2026-06-20-wave5]]'
  - '[[task_20260621_外部探索_Wave5_CI框架_SATs_多智能体架构]]'
  - '[[diag_20260621_外部知识探索_三个新盲区]]'
status: pending_review
---

# 欧阳锋审查任务：wave5 外部探索三个新盲区（12 张卡）

> **来源**：`60_feedback/tasks/task_20260621_外部探索_Wave5_CI框架_SATs_多智能体架构.md`。
> WorkBuddy 老顽童已完成全波次生产：CI 框架 3 张 + SATs 工具包 5 张 + 多智能体架构 4 张。
> **Wave 5 是外部探索任务**——三个盲区（CI 框架、SATs、多智能体架构）均来自外部资料（CIA 方法论、竞对情报实践、LangChain benchmark），非一堂内生素材。审查时需注意：外部方法论的适用性需标注"待一堂实践验证"。

---

## 0. 任务元信息

| 项目 | 内容 |
|------|------|
| 待审任务 | `laowantong-batch-2026-06-20-wave5` |
| 来源队列 | `70_product/tasks/production-queue.md` 第 9 项 |
| 生产方 | WorkBuddy 老顽童 |
| 卡数 | 12 张 |
| 目标 | 补充一堂调研武器库三个新盲区：CI 框架（Define/Gather/Analyze/Implement 四阶段）、SATs 结构化分析技术（5 种）、多智能体研究架构（4 种模式） |
| 质量门禁 | 12 张卡 `kdo pre-submit` 全通过（12 passed / 0 failed） |

---

## 1. 待审 12 张卡清单

### Wave 5a：CI 框架（3 张）

| # | 卡片路径 | 类型 | 标题 | 审查重点 |
|:---:|:---|:---|:---|:---|
| 1 | `30_wiki/frameworks/framework-ci-operating-model.md` | framework | CI 操作系统模型 | 四阶段循环完整性；与一堂三层八模块的映射关系；Implement 阶段是否真的是一堂武器库缺失环节 |
| 2 | `30_wiki/tools/tool-ci-define-phase.md` | tool | CI Define 阶段：KITs/KIQs 方法 | KITs/KIQs 操作步骤是否具体；与"调研问题设计"的区分是否清晰 |
| 3 | `30_wiki/tools/tool-ci-implement-phase.md` | tool | CI Implement 阶段：Battlecard 制作与运营 | Battlecard 标准是否可操作；嵌入运营节奏（forecast call/deal review/QBR）是否具体 |

### Wave 5b：SATs 工具包（5 张）

| # | 卡片路径 | 类型 | 标题 | 审查重点 |
|:---:|:---|:---|:---|:---|
| 4 | `30_wiki/frameworks/framework-structured-analytic-techniques.md` | framework | 结构化分析技术体系 | 八类技术分类是否完整；与一堂方法论的映射关系是否准确 |
| 5 | `30_wiki/tools/tool-key-assumptions-check.md` | tool | 关键假设核查（Key Assumptions Check） | 四步法是否具体；ACH 核心原则"找反驳证据"是否突出；与`[[tool-半肥猫-ai-research-validation]]`的关联是否有效 |
| 6 | `30_wiki/tools/tool-devils-advocacy.md` | tool | 魔鬼代言人（Devil's Advocacy） | 标准操作步骤（60-90分钟）是否具体；与"自攻击"的区别是否清晰 |
| 7 | `30_wiki/tools/tool-red-team-analysis.md` | tool | 红队分析（Red Team Analysis） | 竞对视角模拟四步法是否可操作；竞对画像重建方法是否具体；与"竞对跟踪"的区别 |
| 8 | `30_wiki/tools/tool-indicators-signposts.md` | tool | 指标与路标（Indicators & Signposts） | 从假设导出 Indicators 的方法是否具体；Leading vs Lagging 区分是否清晰；信号触发阈值定义 |

### Wave 5c：多智能体架构（4 张）

| # | 卡片路径 | 类型 | 标题 | 审查重点 |
|:---:|:---|:---|:---|:---|
| 9 | `30_wiki/frameworks/framework-multi-agent-research-architecture.md` | framework | 多智能体研究架构模式 | 四种模式对比矩阵是否完整；LangChain benchmark 数据是否准确；选择决策树是否实用 |
| 10 | `30_wiki/tools/tool-agent-research-supervisor.md` | tool | Supervisor 模式：中心化任务分发 | `langgraph-supervisor` 操作步骤是否具体；3 个优化选项是否实用 |
| 11 | `30_wiki/tools/tool-agent-research-swarm.md` | tool | Swarm 模式：对等节点协商 | 收敛条件设置是否具体；与 Kimi Deep Research Swarm 的对比是否准确；⚠️ 时间敏感性标注是否醒目 |
| 12 | `30_wiki/tools/tool-agent-research-pipeline.md` | tool | Pipeline 模式：阶段化顺序推进 | 对应 OSCAR 五步法是否准确；阶段间契约设计是否具体；阶段门控（Gate）是否可操作 |

---

## 2. 欧阳锋审查标准

### 2.1 通用标准

| 判定 | 条件 |
|:---|:---|
| **deep / 通过** | 正文 ≥100 行（framework ≥150 行）；Claims/Evidence/Critique/Synthesis/Action Triggers/Failure Modes 六段齐全；失败模式具体；数字有来源标注；`related` 有效；内容区无 `src_unknown` 残留 |
| **shallow / 返工** | 正文 < 80 行；缺六段中任一；失败模式模板化；数字无来源；related 死链；内容区仍有 `src_unknown` |
| **borderline / 小修** | 局部数字未标注、related 缺 1-2 条、个别表述不精确 |

### 2.2 本次重点审查项

1. **外部方法论的适用性标注**
   - 12 张卡均来自外部资料（CIA/竞对情报/LangChain），是否标注了"待一堂实践验证"或类似的适用性边界
   - 与一堂现有方法论的映射关系是否准确（如 CI 四阶段 vs 一堂三层八模块）

2. **工具卡的可操作性**
   - 每张 tool 卡是否有具体操作步骤（ numbered steps ）
   - 典型场景/常见错误/失败模式是否具体

3. **framework 卡的系统性**
   - 分类是否完整（如 SATs 八类、多智能体四种模式）
   - 对比矩阵/选择决策树是否实用

4. **wikilink 有效性**
   - Wave 5 生产中发现并修复了 4 处 wikilink 错误（`skill-半肥猫` → `tool-半肥猫`、`concepts/kimi-...` → `kimi-...`）
   - 审查时需再次确认所有 `[[...]]` 链接指向真实存在的文件

5. **frontmatter 完整性**
   - `domain` / `related` / `tags` 的 `src_unknown` 占位是否已清理
   - `confidence` 是否合理（外部方法论卡片应为 `curated` 或 `ai_generated`，不应为 `unverified`）

---

## 3. 判定规则

| 情况 | 处理 |
|:---|:---|
| 12 张全部 deep | 全部标记 `reviewed_by: 欧阳锋`，`status: reviewed`，任务状态改 `reviewed` |
| 少数 shallow/borderline | 通过的卡先标记 reviewed；返工卡列清单退回 WorkBuddy 老顽童；任务保持 `pending_review` |
| 多张核心问题 | 整体任务改为 `blocked`，列明问题，通知王语嫣/用户 |

---

## 4. 审查后动作

### 4.1 若全部或大部分通过

1. 12 张卡片 frontmatter 更新：
   - `status: enriched` → `reviewed`
   - `reviewed_by:` → `欧阳锋`
   - 加 `review_date: "2026-06-28"`
   - `updated_at:` → `2026-06-28`
2. `70_product/tasks/production-queue.md`：任务 #9 状态改为 `reviewed`
3. `70_product/tasks/dashboard.md`：wave5 状态改 `reviewed`
4. `.agent/context.md`：追加 wave5 终审完成记录
5. **解锁下游任务**：wave5 reviewed 后，王语嫣可规划 wave6（如有）
6. 本文件末尾追加审查结论

### 4.2 若有返工

1. 保持任务 #9 状态为 `pending_review` 或改为 `blocked`
2. 在本文件末尾追加返工清单
3. 通知 WorkBuddy 老顽童按清单修复

---

## 5. 给欧阳锋的启动口令

**完整版**：
> 你是欧阳锋。先进入工作目录 `C:\Users\Administrator\Desktop\wiki\`，读 `.agent/startup.md`、`.agent/ouyangfeng-context.md`、`70_product/tasks/production-queue.md`，找到 wave5 pending_review 项，读 `60_feedback/tasks/review_20260628_ouyangfeng-wave5.md`，按清单审 12 张卡，重点检查外部方法论适用性标注、工具卡可操作性、wikilink 有效性，跑 `kdo pre-submit` 抽查，给出 verdict。

**短版**：
> 欧阳锋，切到 wiki 目录，读 startup、队列、wave5 审查任务单（`60_feedback/tasks/review_20260628_ouyangfeng-wave5.md`），审 12 张卡。

---

## 6. 状态记录

| 日期 | 事件 | 操作人 |
|:---|:---|:---|
| 2026-06-28 | WorkBuddy 老顽童完成 wave5 全波次生产（12 张卡） | WorkBuddy 老顽童 |
| 2026-06-28 | 王语嫣写本审查任务单 | 王语嫣 |
| 2026-06-28 | 12 张卡 `kdo pre-submit` 全部通过（12 passed / 0 failed） | WorkBuddy 老顽童 |
| 2026-06-28 | 修复 wikilink 错误 4 处（`skill-半肥猫` → `tool-半肥猫`、`concepts/kimi-...` → `kimi-...`） | WorkBuddy 老顽童 |

---

## 7. 欧阳锋终审结论

**（待欧阳锋填写）**

---

*维护人：王语嫣 | 最后更新：2026-06-28 | 终审：待欧阳锋*
