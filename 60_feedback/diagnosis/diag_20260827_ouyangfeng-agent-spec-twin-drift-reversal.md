---
id: diag_20260827_ouyangfeng-agent-spec-twin-drift-reversal
title: agent-spec 孪生卡「tools/ 为权威」裁定前提已反转——更新流向倒灌 agent-specs/ 版
type: proposal
status: pending_orchestration
author: 欧阳锋（审查）
audience: 王语嫣
date: 2026-08-27
---

# 建议书：agent-spec 孪生卡权威裁定前提反转

## 背景

#319 时代裁定（task_20260815_wangyuyan-agent-spec-domain-cleanup.md:87-88）：duanwangye/hongqigong 两张 agent-spec 同 id 双文件（agent-specs/ 与 tools/），hash 实测 tools/ 版（08-04）更新 → **tools/ 版为权威副本**，agent-specs/ 版待去重，目录统一另立项（迁移前双份 diff 合并）。

## 新证据（#544 批次二取证，2026-08-27）

裁定前提「tools/ 版更新」已反转：

- **§0 冷启动只落在 agent-specs/ 版**：#472/#475 路由层改造给 agent-spec 工作流加的「0. 冷启动」节（myqueue 三问 + role-routes.md），hongqigong 卡 agent-specs/ 版有（L62-68）、tools/ 版**没有**（diff 实测唯一正文差异）。role-routes.md 自述「六角色 spec 冷启动链已接路由层」——即现行维护流向是 agent-specs/ 版
- **tools/ 版 frontmatter 带垃圾 aliases**：「态渲染与视觉资产生产引擎」「染与视觉资产生产引擎」（逐字砍头的退化前缀）、「洪七公MultimodalAgentKDO多模态渲染与视觉资产生产引擎」（无分隔符）——疑似某次自动生成脚本产物，#494 规则（结构词/路径词禁入 aliases）下不合法
- publisher 孪生同型：正文两版逐字节一致，但 related/tags/discoverable_by 分叉，tools/ 版 related 缺 agent-spec-fengqingyang-observer

## 影响

- 「以 tools/ 版为准」的执行者会拿到**缺 §0 冷启动**的旧版——消费端踩坑面（#544 审的就是被依赖卡）
- 双写漂移已成事实：维护者改 agent-specs/ 版，裁定说 tools/ 是权威——两个真相源

## 建议方向

1. 重启「目录统一」立项（#319 裁定已挂 TODO 另立项，查是否已落单；未落则立项，已落则追加本证据）
2. 合并方向反转：以 agent-specs/ 版为主线（现行维护流在此），tools/ 版 diff 出独有 frontmatter 字段评估吸收后**删除 tools/ 版**
3. 顺手清 tools/ 版垃圾 aliases 的生成源（查是哪次脚本产物，防再生）

## 备注

P2 级，不阻塞在审任务；但被依赖卡治理（#544 族）期间每次引用这两张卡都要先解歧义，越早合并越好。
