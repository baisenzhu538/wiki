---
id: task_20260903_laowantong-research-skills-explosion-digging
title: 调研域 skill 补位：爆炸式五步法 skill + 挖掘式穷尽手段流程 skill + research-core 第一层嵌四类型判定
seq: 629
status: in_progress
assignee: laowantong
created_by: wangyuyan
created_at: 2026-09-03
decision_source: skills-assistant 建议书《调研域skill化缺口与四类型整合》（老朱直令勘察的产出）09-03 王语嫣裁定：动作1/2 立项本单；动作3 裁定=嵌入 research-core 第一层（不另起前置 skill，防路由分裂）；动作4 并入；动作5 验收挂载归 skills-assistant 本职
reviewer: 欧阳锋
instance: laowantong
updated_at: '2026-09-02T20:42:11.426930+00:00'
---

# #629 调研域 skill 补位（老顽童）

## 背景

skills-assistant 全库勘察实证：调研域 90+ 卡方法体系完整，但 skill 化不均——爆炸式完全无 skill（五步法卡在库、research-explosion-partner agent 已部署，唯独缺通用 skill）、挖掘式只有工具无流程、四类型判定逻辑未行为化。建议书：`60_feedback/diagnosis/建议书_20260902_调研域skill化缺口与四类型整合.md`（内含四类型表/缺口证据/验收口径）。

## 任务

1. **research-explosion-five-step skill**（P0）：爆炸式五步法行为化——参照 research-explosion-partner SPEC（#335 终审 A-）+ framework-baozhashidiaochan-five-step 卡；含 manifest/触发词/失败模式/When NOT（单一信息点→挖掘式/推理决策→OSCAR/时间极短不用）/反例黑名单
2. **research-digging-approach skill**（P1）：挖掘式流程——穷尽手段 5 层升级逻辑+单点狙击+合规边界（When NOT：简单查询/紧急决策/成本过高/法律风险）
3. **research-core 第一层嵌四类型判定**（P1）：诊断信号表+When NOT 写进第一层（最小自包含），按深/高/宽/动态分型路由到四方法线；不改 OSCAR 现有武器库路由，两者互补
4. 验收配合：产出后交 skills-assistant 过 darwin-skill 9 维门禁+挂载（他不产只验）

## 边界

- 不重写 30_wiki 卡（产 skill 不产卡）；与 #594/#595/#597 已收口无撞车面
- 参照样板：skill-architecture-design（#593 U2 行为化样板）
- 自动式不动 CI 框架，只把「何时启用+监控搭建」写进判定层

## 交付

- 2 个 skill + research-core 第一层 diff + manifest 三写一致 + 路由盲测记录 + 执行报告
- claim/complete 走 queue_transition（complete 629）
