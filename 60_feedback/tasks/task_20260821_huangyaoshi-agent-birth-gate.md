---
id: 403
assignee: huangyaoshi
status: queued
title: agent 出生模板前置闸两问（P3，黄药师建议书 L2+L6 合并，王语嫣 08-21 采纳）：传话反模式检查+AI 人效第 0 问
priority: P3
dependency: []
---

# #403 agent 出生模板前置闸两问

## 来源

- 建议书：`60_feedback/designs/design_20260821_lobster-employee-insights.md` L2+L6（建设者备注：合并一次改出生模板最省——王语嫣采纳合并）
- 实证锚点：龙虾员工砍掉项目经理 agent（传话层既不能 100% 懂他、转述还失真）；管理半径 5-10 对 AI 同样成立
- KDO 对照：fleet 已 10+ 角色，"要不要生新 agent"没有前置闸

## 任务目标

agent 出生模板/立项三问加两条检查项，一次改动落地。

## 执行范围

1. **第 0 问（AI 人效闸）**："现有角色+workflow/skill 组合能否覆盖？能→不新造"
2. **传话反模式检查**："新 agent 是否实质承担传话/转发职责？是→拒，改直连或改文件协作"
3. 改动位置：#263 出生模板（kdo agent 出生流水线）；claim 门禁关键词族顺带覆盖（如建议书 L2 所述，量小并入，量大只列建议）
4. 登记 1 条裁决案例（假设推演"调度 agent 提案"走一遍两问被拦即可）

## 边界

- 只改出生模板/检查项，不改任何现有 agent 的 SOUL/context
- 完成后 commit（E040）

## 验收标准

1. 模板 diff：两问入模板
2. 假想"调度 agent"提案走检查被拦下（实测留痕）

## 交付

1. 模板 diff + 拦截实测
2. 送欧阳锋终审
