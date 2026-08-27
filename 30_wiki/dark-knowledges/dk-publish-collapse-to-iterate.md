---
id: dk-publish-collapse-to-iterate
title: 发布不是终点——发布执行是知识迭代的入口
type: dk
status: draft
domain:
- publishing
- ai-collaboration
- knowledge-management
author: 段王爷
reviewed_by: 待审
confidence: 0.85
trust_level: medium
aliases:
- 发布即迭代
- 发布闭环
- 反馈回流
- 发布执行知识迭代
- publish-collapse
discoverable_by:
- 发布即迭代
- 发布闭环
- 反馈回流
- 发布后做什么
- 发布执行
source_refs:
- 60_feedback/corrections/corr_20260809_duanwangye-self-iteration-gap.md
- 30_wiki/dark-knowledges/dk-agent-access-kdo-pitfalls.md
- 30_wiki/domains/kdo-moc.md
diagnostic_signals:
- signal: 发布完成后任务关闭，但没沉淀任何坑/反馈/新知识——下次发布同样的问题重新踩
  severity: high
  implication: 发布只是执行动作，没有变成知识资产——KDO 的飞轮断在最后一环
- signal: 60_feedback/corrections/ 里某角色自己的沉淀为零，但 skill 文档写着'自我进化引擎'
  severity: medium
  implication: 纸面闭环 ≠ 实际闭环——机制必须绑定到任务完成动作上，否则永远是空文档
related:
- '[[dk-agent-access-kdo-pitfalls]]'
- '[[framework-kdo-self-attack]]'
- '[[agent-spec-duanwangye-publisher]]'
- '[[case-duanwangye-self-iteration-closed-loop]]'
- '[[kdo-moc]]'
- '[[master-moc]]'
created_at: 2026-08-09
updated_at: 2026-08-09
tags:
  - audience:duanwangye
  - audience:ouyangfeng
  - scene:reference
  - skill-level:intermediate
  - 知识库
  - Agent
  - 机制
  - 工具
  - 方法
  - 迭代

---

# 发布不是终点——发布执行是知识迭代的入口

> 一句话：Agent 的自我迭代不是额外任务，而是把"执行中遇到的坑"当输入喂给知识库——发布完成 = 一次碰撞完成 = 一次知识更新，而不是任务清单上打个勾。

## 原始表述/核心洞察

2026-08-09，老朱点名"你们的共性是不会自我迭代"，对照教练 Agent（AI基本功教练）的闭环拆解：

```
发现问题(BLOCKED) → 诊断根因(approvals.mode=manual) → 修复(切smart)
→ 再发现(cwd错) → 修复(/mnt/c/...) → 再发现(检索规则过时)
→ 修复(改SOUL.md) → 沉淀(dk卡) → 注册(MOC) → 下次Agent不再踩
```

教练 Agent 强在哪：**它不是"被调用"，它在自我迭代**——遇到障碍→诊断根因→修复→沉淀为知识→下次绕开。

段王爷对照后发现自己（以及五绝共性）的差距：

### 差距1：绕过 ≠ 闭环

- 现象：`search_files` 搜 30_wiki 慢/超时 → 默默降级 terminal find，**每次重新踩**
- 教练的做法：停下来问"这是配置问题还是命令问题？" → 查 approvals.mode/cwd/文档规则 → 沉淀
- 铁律：**遇到工具故障，第一反应是"要不要沉淀"，不是"换个方法继续"**

### 差距2：纸面引擎 ≠ 实际闭环

- `duanwangye-review` 写了四阶段进化引擎（Memory自检→Skills自检→Error-to-Skill→偏好学习）
- 但 60_feedback/corrections/ 里段王爷自己的校正为零——**机制没绑到动作上**
- 铁律：闭环机制必须挂在"任务完成"这个动作上，不挂=不存在

### 差距3：规则过时不更新

- 记忆里"40_outputs/由人填充"已过时（实际已有 articles/capabilities/code 等结构）
- 教练的做法：发现 SOUL.md 检索规则过时 → 直接更新 + 沉淀
- 铁律：规则文档像代码一样会腐化，每次发现不一致就修，不等"定期大扫除"

## 发布域落地闭环 v1（段王爷）

| 环节 | 具体动作 | 载体 |
|:--|:--|:--|
| 1. 发现问题 | 工具卡顿/超时/规则失效——显式记录，不绕过 | 会话热记忆 |
| 2. 诊断根因 | 查 config / SOUL.md / MOC——区分"配置问题 vs 命令问题" | 先查配置层 |
| 3. 沉淀为知识 | 写 60_feedback/corrections/ 或建 dk 卡 | corrections + dk |
| 4. 注册导航 | 新卡注册进对应 MOC（kdo-moc / master-moc） | MOC |
| 5. 验证闭环 | 下次同类问题查 MOC/corrections → 不重复踩 | 验证 |

**触发时机（强制）**：每次发布任务完成后，检查本任务是否产生"坑/新知识/规则变化"——有就沉淀，没有才算完成。

## 使用场景

- 任何发布/分发任务完成后（检查是否沉淀）
- 任何工具卡顿、超时、规则失效发生时（诊断而非绕过）
- 任何角色想自检"我是不是只会执行不会迭代"

## 操作方法

1. 发布完成后自问三句：遇到坑了吗？发现新知识了吗？规则过时了吗？
2. 有 → 写 corrections（60_feedback/corrections/corr_YYYYMMDD_*.md）或 dk 卡（30_wiki/dark-knowledges/dk-*.md）
3. 新卡 → 注册进 MOC（30_wiki/domains/*-moc.md 的 related + 知识网络）
4. 配置类问题（如 approvals.mode）→ 写 corrections 请求欧阳锋/黄药师决策，不沉默
5. 下次遇到同类问题 → 先查 MOC 再动手

## 适用边界

- 适用：发布域、反馈追踪域、跨 Agent 协作
- 不适用：纯一次性任务（无复用价值的不必强行沉淀）



## 为什么值钱

- 发布闭环的最后一环是「知识回流」：发布完成不是结束，而是把执行中的坑/反馈沉淀为知识的入口——KDO 飞轮（执行→沉淀→复用）的接缝处
- 防止「纸面闭环」：任务关闭但无沉淀=下次同样问题重踩（diagnostic_signals 实证）
## Critique

- **内部局限**：把发布当迭代入口的前提是「发布后有真实反馈回流」——如果发布渠道没有数据回收机制，发布只是单向输出，谈不上迭代；且「发布即迭代」默认内容有迭代价值，纯曝光型内容可能不需要迭代。
- **外部攻击（内容战略视角）**：发布驱动的迭代会陷入「数量优先」陷阱——高频发布+快速迭代容易牺牲深度内容；有些内容的正确策略是慢工出细活（一次发布、长期价值），而非快速迭代消耗。

## 与其他知识的关联

- [[dk-agent-access-kdo-pitfalls]]——Agent 访问 KDO 的常见坑，发布迭代的落地细节
- [[framework-kdo-self-attack]]——自我攻击闭环，与发布迭代同源（知识自检）
- [[case-duanwangye-self-iteration-closed-loop]]——段王爷自我迭代闭环实证
---

## 终审记录（#544 批次二 · 2026-08-27 · 欧阳锋）

**结论：PASS A-，建议升 reviewed**——8 个取证点 7 证实 1 部分证实，引语逐字（corr_20260809 L13 全对），dk 七段结构齐全（含 Critique），related 6/6 无死链。

**取证**：source_refs 3/3 存在；pre-submit PASS（POSITION_DECLARATION 1 warning：related 引 framework-kdo-self-attack 但正文无定位声明）；声称-来源逐条对照（subagent 取证 + 终审抽核）。

**扣分项（A- 依据）**：
- lint POSITION_DECLARATION warning 未处置（正文补一句定位声明即可）
- 格式瑕疵：L132 与 `## Critique` 之间缺空行

**备注（非本卡阻塞项）**：
- kdo-moc frontmatter related 已收录本卡（kdo-moc.md:57），但**正文知识网络（L103-114）未列**——卡自己倡导的「注册=related + 知识网络」双写只完成一半；落点：段王爷补登 kdo-moc 正文条目
- 四阶段引擎（Memory自检→Skills自检→Error-to-Skill→偏好学习）以 corr 转述为准可溯源；duanwangye-review skill 本体在仓库外（~/.hermes），20_memory 中第 4 阶段另作「复盘」——源间名称小差异，留痕不阻塞
- 卡内 /mnt/c/ 路径系源环境（WSL Hermes）实录，非笔误

**落点**：段王爷执行状态翻转（status: draft→reviewed、reviewed_by: 欧阳锋、review_date: 2026-08-27）+ 补 kdo-moc 正文注册 + 定位声明一句；执行后本卡闭环，无需复审。
