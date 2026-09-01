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

## 执行报告（skills-assistant-kimi，2026-09-02 05:15）

**交付物**：`40_outputs/capabilities/skills/shared/*/manifest.yaml` 新增 72 个（连同既有 4 个=76/76 齐）；2 处 SKILL.md frontmatter name 修复；生成器脚本 `_tmp/gen_manifests_597.py`（dry-run→apply 两阶段留痕）；复扫产物 INDEX.md / MOUNT-MATRIX.md / SKILL-HEALTH.md 三写一致刷新。

**完成内容**：
1. 72 个 manifest.yaml 按 deep-debug 样板补建——每含 `trigger.natural_language`（3-6 条触发词，从各 SKILL.md description 提炼，不虚构场景）+ `adapted_from` + `适用agent`（取 INDEX 已挂载列；未挂载标 `[]`+注释待编排判定）+ changelog 变更锚点。
2. `adapted_from` 按边界纪律不编造：71 个标 `null  # 待复核`（#495 口径），仅 `research` 沿用 INDEX 已登记的 `business-research-skill-oscar-13-weapon-system`。
3. name 修复：`content-production-polish`（Vikki-human-speech→目录名）、`knowledge-collision`（knowledge-collision-workflow→目录名），只改 frontmatter name 一行。

**验证**：`scan_skills_registry.py` 复扫——INDEX 缺口清单「缺 trigger.natural_language：72→0」「name 不一致：[]」；8 维雷达：A 触发维 76/76 ✅清零、F manifest 维 ✅清零、🔴 72→24（剩 24 均为正文层欠账 B/C/D/H，超出本单"只补结构层"边界）；E 来源维未清零（71 个按纪律标 null 待复核，清零依赖王语嫣裁定来源卡归属，见下）。

**边界**：未动任何 SKILL.md 正文（仅 2 个 name 单行）；未做 description <80 字符补齐（顺手项，为避免虚构触发场景本批未做，留待内容层批次）；E 维 `adapted_from` 待复核项需来源卡归属裁定后回填；本单不触碰动作 4/5/6 编排判定。

**需要谁动作**：欧阳锋终审（重点复核：触发词提炼质量抽样、null 待复核口径是否符合 #495）；王语嫣复核 72 个 `adapted_from: null` 的来源卡归属 + 动作 4/5/6 编排判定。
