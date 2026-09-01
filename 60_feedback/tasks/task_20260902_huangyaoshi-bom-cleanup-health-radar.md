---
id: 598
task_id: task_20260902_huangyaoshi-bom-cleanup-health-radar
title: skill文件BOM批量清理+8维健康检测并入扫描脚本例行化
status: in_progress
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
updated_at: '2026-09-01T16:10:52.675581+00:00'
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
