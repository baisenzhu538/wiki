---
title: "黄药师 2026-06-05 工作复盘"
type: improvement-plan
status: stable
domain:
  - master
created_at: 2026-06-05
updated_at: 2026-06-05
author: 黄药师
---

# 黄药师 2026-06-05 工作复盘

## 做了什么

| 产出 | 类型 | 状态 |
|:-----|:-----|:----:|
| embedded-ir-debugging playbook | capability | ✅ |
| kdo stale CLI 命令 (Task A) | code | ✅ committed (9f9b658) |
| KDO lessons 4 条审查请求 | task | ✅ 等欧阳锋 |
| claude-smart 卸载 + superpowers 安装 | infra | ✅ |
| Task B spec (brainstorming) | design | ✅ committed |
| 电子工程域 KDO 化建议 | alignment | ✅ 等讨论 |

## 核心教训

### 1. 先设计后实现 > 边写边想

今天 Task B 用了 superpowers 的 brainstorming 流程——先探索上下文、一次问一个问题、逐步收敛到 spec——和昨天的做法（直接看任务文件→开写代码）形成鲜明对比。

**对比**：

| | 昨天 (Task A) | 今天 (Task B) |
|:--|:------------|:------------|
| 设计阶段 | 已有任务文件详规，直接实现 | brainstorming → spec → 等审批 |
| 边界情况 | 写测试时发现 | 设计阶段逐个问，全部覆盖 |
| 返工 | 0（任务文件写得好） | 0（但 spec 更结构化） |
| 用户参与 | 任务文件已拍板 | 用户参与了 6 个决策 |

**结论**：任务文件已经写得很详细、阈值表已拍板的场景（Task A），直接实现是高效的。但对于"有方向但未细化"的场景（Task B），brainstorming 流程显著减少了遗漏。关键是**判断该走哪个路径**——不是所有任务都需要 brainstorming，也不是所有任务都该跳过。

→ 追加 P-22（跨域知识迁移边界判断）

### 2. 知道"什么不该做"比"该做什么"更重要

电子工程域讨论时，我的核心判断是：**KDO 不管理硬件文件本身，管理关于硬件项目的知识。** 这个判断避免了把原理图/PCB 塞进 capture→ingest 的错误方向。

欧阳锋已经写了三套提示词和 8 阶段处理架构——那些是 AI Agent 的执行规范，不是 KDO 的 ingest 管线。分辨这两个边界后，我的 5 条建议全部集中在"文本层知识"上（dk 卡、playbook link、项目元数据卡、retrospective→dk 管线、合并提醒），没有一条建议"给原理图建卡片"。

→ 追加 P-23（插件安装环境依赖链）

### 3. 新工具（superpowers）即插即用

superpowers 今天第一次用，直接上手了 brainstorming 流程。关键原因：
- 它的 skill 自动触发（不需要手动调用）
- 流程检查清单化（不会被跳过）
- 和 KDO 的开发节奏兼容（spec→plan→implement→review→verify）

不需要"学习"——第一天就能用起来。

### 4. 对齐文档的格式很重要

`huangyaoshi-kdo-electronics-proposal.md` 里用了"现状→边界→建议→对齐表→不建议"的结构，特别是"和欧阳锋现有设计的对齐"那张表——明确标出共识和分歧。这比写一篇长文然后让读者自己找"你到底同意什么不同意什么"高效得多。

## 可以改进的

| 问题 | 改进 |
|:-----|:-----|
| vault backup 自动提交让我不确定文件是否入库 | 信任机制——写完文件后等 1-2 分钟即可，不需要手动验证 |
| 插件安装三次失败有点耗时 | P-23 记录了排查链，下次先跑 `git ls-remote` |
| 今天一个会话跨度太大（CLI 开发→spec 设计→电子工程域讨论） | 如果明天发现上下文太长响应变慢，该 /new 就 /new |

## 明日建议

1. 等用户审批 Task B spec → 开工实现
2. 等欧阳锋+用户讨论电子工程域建议 → 如果"先做 E-FM→dk"通过，直接开工
3. Task B 完成后启动 P-22/P-23 的关联卡片生产

---

*黄药师 · 2026-06-05*
