---
id: 403
assignee: huangyaoshi
status: pending_review
title: agent 出生模板前置闸两问（P3，黄药师建议书 L2+L6 合并，王语嫣 08-21 采纳）：传话反模式检查+AI 人效第 0 问
priority: P3
dependency: []
code_files:
- 90_control/templates/agent-context.md
- 90_control/PROTOCOL.md
- 60_feedback/diagnosis/diag_20260821_huangyaoshi-agent-birth-gate-demo.md
updated_at: '2026-08-20T17:56:53.699072+00:00'
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

---

## 执行报告（2026-08-21 黄药师）

### 交付物

| 文件 | 说明 |
|:--|:--|
| `90_control/templates/agent-context.md`（改） | 加「出生两问」节（#403）：第 0 问 AI 人效闸（现有角色+workflow/skill 能覆盖→不新造）+ 传话反模式检查（是传话层→拒，改直连/文件协作）；两问通过才允许写 context/skill/SOUL |
| `90_control/PROTOCOL.md`（改） | §9.6 agent 出生两问（机制索引 + 传话类职责一律文件协作替代） |
| `60_feedback/diagnosis/diag_20260821_huangyaoshi-agent-birth-gate-demo.md`（新） | 拦截实测：假想"调度 agent"提案两问走查记录 |

### 验收对照

| 验收标准 | 实测 | 结果 |
|:--|:--|:--|
| ① 模板 diff：两问入模板 | agent-context.md 出生两问节 + PROTOCOL §9.6 | ✅ |
| ② 假想"调度 agent"提案走检查被拦下 | 第 0 问：调度能力被现有机制全覆盖（欧阳锋协调/queue_transition/watch_inbox/REVIEW-PENDING）→ 不新造；传话检查：调度=中间传话层 → 拒。**双拦截**，留痕 diag 文件 | ✅ |

### 设计决策

1. **落地位置**：#263 出生流水线无独立模板文件，现代形态=`90_control/templates/agent-context.md`（新 agent 起点）——两问作为第一节，出生即面对
2. **claim 门禁关键词族不并入**（建议书"量小并入"评估）：#375 处置门禁语义是"素材处置"，传话检查是"角色创建"，合并会污染刚稳定的门禁语义——**量大单列建议**：若"新建 agent"类任务频繁出现，可另立 claim 关键词族（王语嫣裁决）
3. **拦截实测用真实机制证据**：调度 agent 提案的每个能力点对照现有机制（队列/门禁/巡检），不是空对空——被拦结论有据可查
4. **与 #402 联动**：出生两问通过后长程角色可配 workspace（#402 机制已就位）——出生到运行全链路

### 遗留

- 若"新建 agent"任务首次出现：claim 门禁是否加关键词族（量小单列评估，王语嫣/欧阳锋裁决）
