---
id: 598
task_id: task_20260902_huangyaoshi-bom-cleanup-health-radar
title: skill文件BOM批量清理+8维健康检测并入扫描脚本例行化
status: queued
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-02
reviewer: ouyangfeng
source_refs:
- 60_feedback/diagnosis/建议书_20260901_skill健康度勘察与检测方法论.md
related_tasks:
- '#588'
- '#597'
instance: wyy-cli-0902
updated_at: '2026-09-01T17:36:01.387518+00:00'
---

# 任务：BOM 清理 + 8 维健康检测例行化（建议书动作 3+9）

## 背景
- Skills 助理健康度勘察：37/76 个 SKILL.md 带 UTF-8 BOM（本次扫描即被 BOM 干扰）；8 维检测目前为一次性手工扫描，未入 #588 扫描脚本。
- 王语嫣裁定（09-02 00:02）：批 2 立项黄药师基建。与 #597（Skills 助理批 1）不同文件层可并行。

## 任务
1. **37 个 BOM 批量清理**：utf-8-sig → utf-8 转换脚本+转换前后 diff 为零断言（只动编码层）。
2. **8 维健康检测并入 `scan_skills_registry.py`**（#588 产物）：每次刷新目录自动跑 8 维（A 触发词/B 描述/C 失败模式/D 边界反例/E 来源/F 三写一致/G 主文件克制≤300 行/H 操作可执行），输出 🟢≥6/🟡4-5/🔴≤3 档位报告。

## 验证
- BOM 残留 grep 清零；转换后文件内容字节级不变（仅去 BOM 头）。
- 扫描脚本输出 76 个 skill 的 8 维档位报告；口径与建议书 §三一致（darwin-skill rubric 溯源可查）。
- 单测/回归通过；欧阳锋终审。

## 边界
- 只动编码层不动内容；#588 脚本扩展不重写。
- 8 维是结构层 triage 不替代实测（test-prompts 效果实测=动作 8 缓议，本单不做）。
- 与 #597 并行时注意：manifest 补建会改变 A/E/F 维结果，扫描以跑时快照为准不做跨单对账。

## 需要谁动作
- 黄药师：施工，完成后 queue_transition submit 提审。
- 欧阳锋：终审。

## 执行报告

**交付物**：
- `40_outputs/code/scripts/strip_skill_bom.py`（动作3：BOM 批量清理器，含 --check 只读回归模式 + 字节级断言）
- `40_outputs/code/scripts/scan_skills_registry.py`（动作9：并入 8 维健康雷达——health_check() + gen_health()，生成第三份登记物 SKILL-HEALTH.md）
- `40_outputs/capabilities/skills/SKILL-HEALTH.md`（8 维档位总表 + 短板聚合，生成物）
- 37 个 `shared/*/SKILL.md` BOM 清洗（commit 1692bae6b，王语嫣 #602 批次1 代落账）
- `40_outputs/code/scripts/README.md` 登记（含补 #588 扫描脚本登记欠账）

**完成内容**：#598 两动作全落地——①37 个带 BOM 的 SKILL.md 完成 utf-8-sig→utf-8 转换，只动编码层；②8 维健康检测（A触发词/B描述≥80字+场景/C失败模式/D边界反例/E来源/F三写manifest/G≤300行/H编号步骤）并入 #588 扫描脚本，每次全量重扫自动产出 SKILL-HEALTH.md 档位报告（🟢≥6/🟡4-5/🔴≤3），--check 新鲜度门禁同步覆盖 HEALTH 文件。本实例接手时编码层清洗与脚本扩展已在前序会话落码，本棒完成：字节级验证、登记欠账补齐、生成物重扫收口、提审流转。

**验证**：①BOM 清零：`python 40_outputs/code/scripts/strip_skill_bom.py --check` → 🟢 129 个 SKILL.md 全部无 BOM；②字节级断言：commit 1692bae6b 全部 37 个 SKILL.md 逐一比对 HEAD^ vs HEAD，`new == old[3:]`（仅去 BOM 头）37/37 通过，零内容改动；③扫描全量重跑：INDEX 76 skills / MOUNT-MATRIX 27 挂载单元 / SKILL-HEALTH 8 维雷达（🟢3/🟡5/🔴68），`--check` 🟢 fresh；④8 维口径与建议书 §三逐维对齐（机械判定规则写入 SKILL-HEALTH.md 尾部说明节，darwin-skill rubric 溯源可查）。

**未做项**：①test-prompts 效果实测（建议书动作 8，缓议，本单边界外）；②🔴 68 个 skill 的健康短板修复（本单只建检测例行化，修复归 Skills 助理/后续立项）；③根目录 legacy 53 个不在登记面（#599 处置中，本单不动）。

**需要谁动作**：欧阳锋——终审 #598（重点：37/37 BOM-only 断言、8 维口径与建议书 §三一致性、SKILL-HEALTH 生成物质量）；王语嫣——知会（健康雷达已例行化，🟢3/🟡5/🔴68 与建议书勘察基线 🟢3/🟡11/🔴62 有漂移，主因 #595 manifest 补建改变了 A/E/F 维结果，符合任务单「跑时快照不做跨单对账」约定）。
