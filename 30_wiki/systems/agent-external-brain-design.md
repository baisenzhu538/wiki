---
title: "Agent 外挂大脑设计"
type: system
status: enriched
domain: master
created_at: 2026-05-16
source_refs: ["project-continuity.md", "corrections.md", "operating-principles.md"]
tags:
  - agent-memory
  - context-management
  - token-efficiency
  - cross-tool
---

# Agent 外挂大脑设计

> **一句话**：在项目根目录下扔三个 Markdown 文件，agent 失忆问题解决 80%。

---

## 问题

Agent（Claude Code、Cursor、Windsurf、Copilot）每次新 session 启动时不知道：

- 这个项目是什么、做到哪了
- 上一个 session 做了什么决策、为什么
- 踩过什么坑、哪个方案试过了不行

恢复上下文消耗大量 token，且质量不稳定。

---

## 方案

在项目根目录建 `.agent/` 目录，三个文件：

```
project/
├── .agent/
│   ├── context.md        ← agent 启动第一个读
│   ├── pitfalls.md       ← 踩过的坑，永久编码
│   ├── decisions.md      ← 架构决策记录（ADR）
│   └── tasks/
│       └── current.md    ← 当前 Sprint/任务
├── CLAUDE.md             ← 一行：启动时先读 .agent/context.md
└── src/
```

### context.md：会话入口

agent 启动读这一个文件，30 秒恢复上下文。

```markdown
---
updated: 2026-05-16
active_branch: main
active_task: 初始化 agent 外挂大脑
blockers: []
---

## 当前状态
- 项目刚接入 agent 记忆系统

## 最近决策
（见 decisions.md）

## 下次启动
1. 读 pitfalls.md
2. 读 tasks/current.md
3. 继续 active_task
```

**约定**：
- 最新状态在最上面
- session 结束花 2 分钟更新
- `blockers` 不为空时优先解决

### pitfalls.md：错误永久编码

每踩一个坑追一条，格式：**症状 → 根因 → 对策**。

```markdown
## P-1: Prisma migration 在 CI 中静默失败

**症状**：CI 绿了但数据库 schema 没变
**根因**：prisma migrate deploy 在无 DATABASE_URL 时静默返回 0
**对策**：CI pipeline 加 prisma migrate status 前置检查
```

agent 读到就知道不重蹈覆辙。

### decisions.md：架构决策记录

格式：**日期 → 背景 → 决策 → 原因 → 否决的替代方案**。

```markdown
## 2026-05-16: JWT 用 RS256 而非 HS256

**背景**：auth 服务需要签发和验证 JWT
**决策**：RS256
**原因**：微服务架构下多服务需要验签，公钥可分发
**替代方案**：HS256 — 被否决，共享密钥在微服务间分发不安全
```

下一个 agent 看到就知道为什么做了这个选择。

---

## 为什么省 80% token

| 环节 | 无外挂大脑 token | 有外挂大脑 token | 省 |
|------|:--:|:--:|:--:|
| 恢复上下文 | 3000 | 500 | 83% |
| 了解架构 | 2000 | 400 | 80% |
| 避开已知坑 | 5000（踩坑+修复） | 300 | 94% |
| 回顾决策 | 2000 | 300 | 85% |
| 找当前任务 | 1000 | 200 | 80% |
| 质量自检 | 3000（试错） | 500（门禁清单） | 83% |

真正干活的 token（读源码、写代码）不变——省的都是恢复和纠错层。

---

## 和 `/memory` 的区别

| | Claude Code `/memory` | `.agent/` |
|------|------|------|
| 存在哪 | `~/.claude/` 用户目录下 | 项目根目录，跟着 git 走 |
| 换电脑 | ❌ 没了 | ✅ `git clone` 就在 |
| 换工具 | ❌ 只有 Claude Code 能读 | ✅ 任何 agent 都能读 |
| 谁管 | Claude Code 自动加载 | agent 读文件，人也能直接编辑 |

本质：`/memory` 是工具的私有记忆。`.agent/` 是项目的公共记忆。

---

## 为什么没人说

1. **工具厂商不想说**：锁在工具里的记忆 = 切换成本 = 护城河
2. **搞明白的人没空写**：项目跑顺了该上线了
3. **太简单卖不动**：没法融资、没 SaaS、没 subscription。但管用。

---

## 迁移步骤

```bash
mkdir -p .agent/tasks
# 把上面三个模板文件扔进去
# CLAUDE.md 加一行：启动时先读 .agent/context.md
```

新开 session 说"继续"——agent 应该直接报出上次做到哪。

---

## 边界

- 项目 <5 个文件、<2 个 session 时不值得建
- 超过 10 个文件、跨 3 个 session 以上开始回收成本
- 人必须养成 session 结束更新 context.md 的习惯——2 分钟省下次 20 分钟
