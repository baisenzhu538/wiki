---
updated: YYYY-MM-DD
active_branch: main
active_task: （当前在做什么）
blockers: []
---

## 出生两问（#403 · 创建新 agent 前必答，不通过禁止出生）

> 龙虾员工实证：中间传话层是反模式（agent 间本可直接通信，转述失真最终砍掉）。fleet 已 10+ 角色，"要不要生新 agent"必须有前置闸。

- [ ] **第 0 问（AI 人效闸）**：现有角色 + workflow/skill 组合能否覆盖这个需求？
      能 → **不新造**，改复用/扩展现有角色。答"不能"必须说明：现有哪些角色/技能试过、差在哪。
- [ ] **传话反模式检查**：新 agent 是否实质承担传话/转发职责（A→新agent→B 中间层）？
      是 → **拒**，改直连或改文件协作（git/看板异步，文件即真相源）。
- [ ] 两问通过后才允许继续写 context/skill/SOUL。

## 当前状态
- （项目刚接入 agent 记忆系统 / 正在开发 XX 功能 / 卡在 YY 问题）

## 最近决策
（见 decisions.md）

## 下次启动
1. 读 pitfalls.md
2. 读 tasks/current.md
3. 继续 active_task
