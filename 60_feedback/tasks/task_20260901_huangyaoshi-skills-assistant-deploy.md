---
id: '593'
title: Skills助理Agent部署——U1-U3实跑验收（两阶段第二阶段）
type: deploy
status: queued
priority: P1
assignee: 黄药师
created_by: 王语嫣
created_at: 2026-09-01
source_refs:
- agents/skills-assistant/SPEC.md
- 60_feedback/tasks/task_20260901_wangyuyan-skills-assistant-spec.md
- 60_feedback/tasks/task_20260901_huangyaoshi-skill-registry-mount-matrix.md
---

# #593 Skills 助理 Agent 部署（#587 终审指令：编排层立项，带两阶段口径）

## 背景

#587 SPEC 已欧阳锋终审 PASS A（2026-09-01），终审指令「**部署另立项，编排层处理部署单排期**；部署验收单须把 U1-U3 实跑作为验收门」。#588 挂载矩阵已 PASS A-（扫描脚本/INDEX/MOUNT-MATRIX/spec 模板增补全交付），前置依赖全清。源头=老朱 09-01 直令：「我要的 skills 助理是专门生产和配置 skills 的」（工厂第 7 角色=Skill 生产+配置中枢）。

## 任务（SPEC 两阶段流程·第二阶段：部署验收）

1. 按 `agents/skills-assistant/SPEC.md` 建 agent 实体部署面（比照 #303/#304 三件套部署先例：SOUL/config/profile 注册+cap_hub 登记）；挂载配置遵 SPEC 第六节：默认 shared 全员可见+专属标 `scope: <角色>`+挂载变更 manifest changelog 留痕
2. 施工对齐 #587 终审记档小项：mount-matrix 大小写统一（随 INDEX.md/MOUNT-MATRIX.md 大写惯例，一行对齐）
3. **U1-U3 实跑验收（=验收门，逐条必过）**：
   - U1 存量工具卡行为化：`30_wiki/tools/` 九字诀卡族候选→P1-P4 全流程→另一 agent 仅凭 description 正确决定用/不用
   - U2 新卡行为化：`method-anthropic-skill-design-patterns`（#586 产）→行为化 skill→与 `tool-ai-skill-engineering-guide` 互链不撞车
   - U3 配置流：deep-debug skill 挂载到指定 agent spec「已挂载skills」节→矩阵更新→changelog 留痕（三写一致）
4. 执行报告五字段提审

## 验证

- U1-U3 三用例逐条实跑留痕（SPEC 第八节验证点全命中）
- `python 40_outputs/code/scripts/scan_skills_registry.py` 重跑矩阵刷新正常（shared 计数以扫描实测为准，#587 终审实测 74）
- 路由面自检：skill 注册后可被其他 agent 按 description 正确路由

## 边界

- ❌ 不含飞书壳/IM 入口（SPEC 边界第三条：远期另立项，老朱拍板后才启动）
- ❌ U1/U2 产出的 skill 内容本身仍走欧阳锋终审，部署单验收口径=流程走通+用例通过
- agent-spec 模板「已挂载skills」节 #588 已落，本单不重复改模板

## 关联

- #587 SPEC（PASS A，两阶段第一阶段已闭环）
- #588 挂载矩阵（PASS A-，依赖已解除）
- #335 研究伙伴部署先例同构

## 需要谁动作

黄药师——按 SPEC 第九节两阶段口径执行部署+U1-U3 实跑，完成后执行报告五字段提审，欧阳锋终审。
