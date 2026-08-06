---
id: task_20260806_wangyuyan-deep-review-backlink
task_id: 235
assignee: laowantong
status: queued
updated_at: 2026-08-06
domain: personal
priority: P1
---

# #235 已有复盘卡补链（4 张，只改 related 不动正文）

## 任务目标
把新课产出与已有复盘卡族双向补链，形成完整复盘知识网络。**只改 related 字段，禁止修改任何 reviewed 卡正文**（E010/C-10 教训）。

## 补链清单

| 卡 | 现状 | 补链动作 |
|:---|:---|:---|
| `yt-model-deep-review-iceberg`（reviewed） | 冰山五层+Critique 完整 | related 追加：新 framework-复盘本质与三要素 / framework-四象限复盘法 / case×4（本批） |
| `yt-personal-deep-review`（enriched，周子敬 IPO 课） | 元认知/科学学习 | related 追加：新 framework-复盘本质与三要素（呼应"从经验中学=IPO 第一策略"，口述 L486-496） |
| `framework-yitang-project-retrospective`（reviewed） | 美团 16 字诀 | related 追加：framework-四象限复盘法（16 字诀=项目复盘流程 vs 四象限=复盘重心选择，口述 L1404-1422） |
| `tool-复盘推演法` | 事前推演 | related 追加：framework-四象限复盘法（事前推演 vs 事后复盘边界） |

## 验收标准
1. 每卡补链后 related 无死链（`kdo pre-submit` 验证）
2. git diff 确认：只动了 related 字段，正文零改动
3. lint 0 新增 ERROR

## 边界说明
- 禁止 enrich 正文（含补 Critique/案例）——如发现正文确有缺口，另开修补任务单走欧阳锋审查
- 禁止修改 `yt-personal-deep-review` 课程归属（周子敬课独立成体系）
