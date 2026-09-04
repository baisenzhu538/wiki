---
id: task_20260904_laowantong-qingdanti-scoring-rubric
title: 清单体评分 rubric 化：训练段位图（L1-L6+六维）→ 可执行评分表 + transcript-to-qingdanti skill v1.1（两步法定位+自检门禁嵌入）
seq: 640
status: queued
assignee: laowantong
created_by: wangyuyan
created_at: 2026-09-04
decision_source: 老朱 09-04 设计定稿：两步法（深挖验收→清单体整理）+「清单体做得好不好要有评分规则」
reviewer: 欧阳锋
---

# #640 清单体评分 rubric + skill v1.1（老顽童）

## 背景

老朱两步法定稿：第一步=接收→门禁验收（W6 三方法+暗知识全挖，用清单体枚举防漏）；第二步=清单体整理（结构层，锦上添花）。王语嫣实测背书：清单体改可达性不改增量。缺评分规则——原料在库：`00_inbox/一堂-AI清单体笔记（训练段位图）-truman-结构化.md`（L1-L6+六维）+ yt-note 卡族。

## 任务

1. **清单体评分 rubric**（落 `90_control/templates/` 或随 skill）：以段位图六维为骨架转成可打分表（每维 0-2 分锚点描述+总分档线），L4 清单笔记特征（重新整理/故事线/强逻辑）为合格线
2. **skill v1.1 升级**（`shared/transcript-to-qingdanti/`）：写入两步法定位（本 skill 管第二步结构层；第一步深挖走 W6 另轨）+ rubric 嵌入为交付前自检门禁（产出自评分数写进交付物头部）
3. 用 Live261 试跑件复评一次：按 rubric 打分，验证 rubric 可分辨好坏（自评+若分低修到达标再提）

## 交付

- rubric 文件 + skill v1.1 diff + Live261 复评分数实证 + 执行报告
- claim/complete 走 queue_transition（complete 640）
