---
id: "588"
title: "Skill目录与挂载矩阵机制——扫描生成+登记制（Skills助理基建配套）"
type: infrastructure
status: queued
priority: P1
assignee: 黄药师
created_by: 王语嫣
created_at: 2026-09-01
updated_at: 2026-09-01
source_refs:
- 40_outputs/capabilities/skills/shared/
---

# #588 Skill 目录与挂载矩阵机制（老朱 09-01 直令，#587 配套基建）

## 现状缺口（王语嫣盘点实证）

- 73 个 shared skill 无统一目录：其他 agent「不知道有什么可挂载」
- agent-spec 无「已挂载skills」标准节：谁挂了什么全黑箱，重复挂载/漏挂无对账

## 交付物

1. **扫描脚本**：遍历 `40_outputs/capabilities/skills/shared/*/`，从 SKILL.md frontmatter 提取 name/description/trigger.natural_language/adapted_from → 生成 `40_outputs/capabilities/skills/INDEX.md`（目录菜单：名称/一句话/触发词/来源卡）
2. **挂载矩阵**：扫描 `agents/*/CLAUDE.md` + `30_wiki/agent-specs/*.md` 的 skills 引用 → 生成 `40_outputs/capabilities/skills/MOUNT-MATRIX.md`（agent×skill 对照表，标出：已挂载/可挂载未挂/无主skill）
3. **spec 模板增补**：agent 出生模板（#326 机制）加「已挂载skills」节标准
4. **增量更新钩子**：新 skill 注册/新 agent 部署时目录与矩阵自动刷新（或纳入健康巡检 #326 巡检项）

## 验收标准

- INDEX.md 覆盖 73/73，字段齐全可检索
- MOUNT-MATRIX.md 出全厂 agent 挂载现状（含「可挂未挂」清单≥1 份 actionable）
- 增量机制可演示（新增一个测试 skill → 目录自动出现）

## 执行报告

（完工后填写）
