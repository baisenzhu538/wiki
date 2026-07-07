---
id: task_20260707_wangyuyan-project-management-domain-phase2
type: task
status: queued
owner: 王语嫣
assignee: 老顽童
reviewer: 欧阳锋
priority: P2
created_at: 2026-07-07
updated_at: 2026-07-07
estimated_cards: 30
dependencies:
  - task_20260707_wangyuyan-project-management-domain-production
source_diagnosis: 60_feedback/diagnosis/diag_20260707_yitang-project-management-nine-layer.md
---

# 管项目域 P2 补产与深挖：约 30 张卡

> 来源：`00_inbox/管项目`（5 口述稿 + 5 笔记 + 69 图）
> 前置：#131 管项目域 P1 核心 13 张卡 reviewed 后启动
> 目标：补全案例、工具入口、L5/L6 暗知识，并将 69 张图中可直接转化的 checklist/小抄批量卡片化。
> 深挖依据：`60_feedback/diagnosis/diag_20260707_project-management-annotation-divergence-deep-dive.md`

---

## 一、任务目标

1. 新建 2 张 case 卡：Leo 官网改版失败、一堂 2022 初五大课复盘。
2. 新建 1 张 tool 卡：`tool-yitang-project-weapon-library-v1-8`（项目管理武器库入口/索引）。
3. 视 #131 终审反馈，决定是否将「方案评估三角形」「RASCI」从现有卡中拆出为独立 tool 卡（最多 2 张）。
4. 新建 1 张 dk 卡：`dk-yitang-project-overmanagement-vs-bare-run`（过度管理 vs 裸跑的平衡）。
5. 批量转化 69 张工具图中可直接卡片化的 checklist/模板/小抄，预计 20-25 张 tool 卡。
6. 反向更新 #131 产出的骨架卡与已有管理域卡片的 `related`。
7. 如 #131 的 `framework-yitang-project-plan-design` / `tool-yitang-project-plan-canvas` 装不下定方案口述稿 L604-L642 和 L840-L866 两段操作演示，拆出 1-2 张 companion case 卡。
8. 统计 #131 五张 framework 卡中的失败模式总数，若 ≥40 条，新建 `framework-yitang-project-failure-mode-index` 或将其纳入武器库索引页。
9. 为 `framework-yitang-project-abcd-classification` 补全具体例子（图书角/A、官网改版/B-C、创业工具手册/C、马拉松/D）和 go/no-go 条件。

---

## 二、source_refs

与 #131 相同，另需重点引用：

- `00_inbox/管项目/项目管理-入门篇-口述.txt`（Leo 官网改版案例）
- `00_inbox/管项目/项目管理-做复盘-口述.txt`（一堂 2022 初五大课复盘案例）
- `00_inbox/管项目/项目管理-项目管理武器库_vlm_desc.md`
- `00_inbox/管项目/README-VLM描述汇总.md`（用于批量 tool 图筛选）

---

## 三、卡片生产清单（初排）

| 序号 | 卡片 ID | 类型 | 标题 | 优先级 | 备注 |
|------|---------|------|------|:----:|------|
| 1 | `case-yitang-leo-website-redesign` | case | Leo 官网改版失败案例 | P1 | 入门篇核心教学案例 |
| 2 | `case-yitang-2022-annual-lessons` | case | 一堂 2022 初五大课复盘案例 | P1 | 内部真实案例 |
| 3 | `tool-yitang-project-weapon-library-v1-8` | tool | 项目管理武器库 V1.8 | P1 | 入口索引卡，链接四课全部工具 |
| 4 | `dk-yitang-project-overmanagement-vs-bare-run` | dk | 过度管理 vs 裸跑的平衡 | P2 | L5/L6 缺口暗知识 |
| 5 | `tool-yitang-project-evaluation-triangle` | tool | 方案评估三角形（可选拆出） | P2 | 若 #131 画布已覆盖则不建 |
| 6 | `tool-yitang-project-rasci-model` | tool | RASCI 角色分工模型（可选拆出） | P2 | 若 #131 拆计划框架已覆盖则不建 |
| 7-30 | 定方案/拆计划/管过程/做复盘 checklist 工具卡 | tool | 批量转化 | P2 | 从 69 张图中筛选高复用模板 |

---

## 四、批量转化标准

一张工具图进入批量转化的条件：

1. 内容为可直接填写的 checklist、模板、小抄或一页纸画布。
2. 与 #131 已有工具卡不重复。
3. 能在 200 行以内完成 KDO 标准化（Summary + Claims/步骤 + Constraints + 失败模式 + Action Triggers）。
4. 有明确口述稿或笔记段落支撑「为什么这样设计」。

不符合以上条件的图，作为 source 归档，不入卡。

---

## 五、验收标准

1. 所有目标卡 `kdo pre-submit` PASS。
2. 新卡 `related ≥ 5`；case 卡 `related ≥ 7`。
3. 批量 tool 卡无内容空泛、无重复建设。
4. dk 卡必须包含：现象、根因、反向信号、行动触发器、失败模式。
5. 全量产出通过欧阳锋终审。

---

## 六、风险与阻塞

| 风险 | 影响 | 应对 |
|------|------|------|
| 批量 tool 卡同质化 | 降低知识库信噪比 | 严格按转化标准筛选，宁可少做 |
| case 卡写成故事而非教学资产 | 无法被 Agent 调用 | 必须提炼失败模式、决策点、Action Triggers |
| #131 终审不通过 | 影响 Phase 2 启动 | Phase 2 在 #131 reviewed 后领取 |

---

## 七、产出后动作

1. 老顽童完成生产并跑 `kdo pre-submit`。
2. 将本任务状态改为 `pending_review`。
3. 欧阳锋按队列终审。
4. 终审通过后，黄药师执行 `kdo index --rebuild`。
