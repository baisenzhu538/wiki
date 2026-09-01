---
id: 597
task_id: task_20260902_skills-assistant-skill-manifest-batch1
title: skill登记面批1：72个manifest.yaml补建+2个name不一致修复
status: in_progress
assignee: skills-assistant
created_by: wangyuyan
created_at: 2026-09-02
reviewer: ouyangfeng
source_refs:
- 60_feedback/diagnosis/建议书_20260901_skill健康度勘察与检测方法论.md
related_tasks:
- '#588'
- '#593'
- '#594'
- '#595'
instance: skills-assistant-kimi
updated_at: '2026-09-01T18:55:26.611926+00:00'
---

# 任务：skill 登记面批 1（建议书动作 1+2）

## 背景
- Skills 助理《skill 健康度勘察与检测方法论建议书》（09-01）勘察：76 个登记 skill 中 72/76 无 manifest.yaml、72/76 无 trigger.natural_language、53/76 description<80 字符、2 个 frontmatter name 与目录名不一致——**登记面系统性欠账=「挂了但路由不可用」**。
- 王语嫣裁定（09-02 00:02）：部分采纳分批立项。本单=批 1（P0 登记面）；BOM+8 维检测例行化=批 2（#598 黄药师）；动作 4/5/6（降级/挂载/收编编排判定）待本单产出后王语嫣复核；动作 7（legacy 53 个归档）涉目录结构变更待老朱；动作 8 缓议。

## 任务
1. **72 个 manifest.yaml 补建**（样板=`deep-debug`/`anti-ai-bs-three-moves`）：每含 `trigger.natural_language`（触发词表）+ `adapted_from`（来源卡）+ `适用 agent` 字段；按 8 维 rubric（建议书 §三）自检。
2. **2 个 name 不一致修复**：`content-production-polish`（现=Vikki-human-speech）、`knowledge-collision`（现=knowledge-collision-workflow）——frontmatter name 对齐目录名。

## 验证
- 72/76 manifest 齐；INDEX.md/MOUNT-MATRIX.md 三写一致复扫通过。
- 8 维机械复扫：🔴 数量显著下降（P0 维 A/E/F 清零）；name 不一致清零。
- 欧阳锋终审。

## 边界
- **开工前置=#595 终审收口**（同域 frontmatter 面，错峰防写冲突；#595 已 pending_review 等欧阳锋）。
- 只补结构层（manifest/name）不重写 SKILL.md 正文。
- `adapted_from` 无对应来源卡的**不编造**，标 `adapted_from: null # 待复核`（#495 口径）。
- description <80 字符的顺手补齐可做，但不得虚构触发场景（从正文提炼）。

## 需要谁动作
- Skills 助理：施工+自检，完成后 queue_transition submit 提审。
- 王语嫣：产出后复核动作 4/5/6 编排判定。
- 欧阳锋：终审+后续补 manifest 批次出口门控。
