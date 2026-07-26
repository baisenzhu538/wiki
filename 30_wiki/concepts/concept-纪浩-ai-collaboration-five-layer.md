---
id: concept-纪浩-ai-collaboration-five-layer
title: 概念：纪浩AI协作五层工作空间法
type: concept
status: reviewed
domain:
- src_unknown
- src_unknown
source_person: 纪浩
source_context: AI俱乐部·AI协作方法论分享（2026年）
source_refs:
- 10_raw/sources/src_20260619_e18427b7_00_inbox_纪浩_AI协作方法论_口述.md
- 00_inbox/纪浩-AI协作方法论-口述.md
- 10_raw/sources/src_20260619_e18427b7_00_inbox_纪浩_AI协作方法论_口述.md
- 00_inbox/纪浩-AI协作方法论-口述.md
created_at: '2026-06-09'
updated_at: '2026-06-17'
related:
- - - concept-wanghuan-adversarial-generation
- - - yt-concept-weapon-arsenal
- - - yt-note-checklist-concept
- - - case-ji-hao-ui-design-constraint-evolution
- - - case-纪浩-focus-prompt-design
- - - case-纪浩-from-zip-to-five-layers
wiki_refs:
- src_unknown
- src_unknown
definition_of_done:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
pipeline:
- src_unknown
- src_unknown
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.75
trust_level: medium
diagnostic_signals:
- lens: 结构缺失
  follow_up: 检查五类知识是否混在一起，按L1-L5分层，分开后结构才能自然长出来
- lens: 渐进披露缺失
  follow_up: 使用渐进式披露流程：导诊台→工作手册→经验库→领域知识，逐层深入
- lens: L4管理失控
  follow_up: L4任务管理需要状态管理和版本控制，快速增长的知识需独立管理
- lens: 导诊台缺失
  follow_up: 用导诊台做任务分发，每个Agent有自己的工作手册，避免冲突
- lens: L3未沉淀
  follow_up: 约束文档属于L3工作手册，多任务共享时应沉淀为经验库
tags:
- audience:general
- scene:reference
- skill-level:intermediate
aliases:
- 协作方法论
---

# 概念：纪浩AI协作五层工作空间法

## 定义

**纪浩AI协作五层工作空间法**是一种为AI Agent设计工作环境的结构化方法，核心主张是：

> **AI只会模仿，不会做结构设计。人必须先定义结构，把五类知识分开，结构才能自己长出来。**

五层结构从静态到动态、从稳定到变化，每层有不同的增长速度和管理方式。

## 核心主张

### 主张1：人定结构，AI执行

AI是模式匹配系统，不会创造结构。它的所有结构设计都是从预训练中找相似结构。如果人不先定义好结构，AI就会在错误的道路上越走越远。

### 主张2：五类分开，结构自长

当五类知识混在一起时，一定会乱。分开后，结构才能自然长出来。

### 主张3：知识速度不同，分层管理

不同类型的知识增长速度不同，需要不同的管理策略。

## 支撑论证

**五层结构详解：**

| 层级 | 内容 | 增长速度 | 管理策略 |
|------|------|---------|---------|
| **L1 系统自述** | 项目架构、组件、技术栈 | 缓慢 | 人工维护，定期更新 |
| **L2 领域知识** | 纯业务知识（与项目本身无关） | 缓慢 | 专业人员维护，逐步积累 |
| **L3 Agent服务** | 导诊台、工作手册、工具集、经验库 | 前快后缓 | 任务稳定后趋于稳定 |
| **L4 任务管理** | 任务定义、交付物、流程、上下文 | 迅速变更 | 需要状态管理和版本控制 |
| **L5 日志** | 执行记录、排查信息 | 最快 | 自动化收集，定期清理 |

**渐进式披露流程：**

```
复杂任务
    ↓
导诊台（任务分类）
    ↓
工作手册（规范流程）
    ↓
经验库（避免重复犯错）
    ↓
领域知识（深层业务逻辑）
```

知识越来越深，逐层披露，避免一次性给AI过多信息。

## Constraints & Boundaries

### 适用边界

| 边界 | 说明 |
|:-----|:-----|
| ✅ 适合 | 需要管理多个AI Agent的复杂项目 |
| ✅ 适合 | 知识类型多样、增长速度不同的工作空间 |
| ✅ 适合 | 需要渐进式披露避免信息过载的场景 |
| ✅ 适合 | 团队协作中需要统一工作空间结构 |
| ❌ 不适合 | 单一简单任务（无需分层） → 直接给完整上下文即可 |
| ❌ 不适合 | 快速原型验证（时间紧迫） → 分层管理增加 overhead |
| ❌ 不适合 | 无明确项目边界的探索性工作 → L1系统自述难以定义 |
| ❌ 不适合 | 团队对AI协作结构无共识 → 先对齐认知再分层 |

#| 模式 | 症状 | 修复 |
|:-----|:-----|:-----|
| **五类混放** | 系统自述、领域知识、任务管理混在一起，目录混乱 | 强制按L1-L5分目录，每类知识有独立存放位置 |
| **渐进披露缺失** | 一次性给AI全部信息，输出质量下降 | 按导诊台→工作手册→经验库→领域知识逐层深入 |
| **L4管理失控** | 任务定义频繁变更，上下文丢失 | L4需要状态管理和版本控制，快速增长的知识独立管理 |
| **导诊台缺失** | 多个Agent协作时任务分发混乱 | 用导诊台做任务分发，每个Agent有自己的工作手册 |
| **L3未沉淀** | 约束文档散落在各处，无法复用 | 约束文档属于L3工作手册，多任务共享时沉淀为经验库 |
| **分层僵化** | 严格按照五层执行，效率低下 | 聊和问可以并行，查和测可以重叠，分层是逻辑不是物理隔离 |
| **日志不清理** | L5日志堆积，查找困难 | 自动化收集+定期清理，保留关键日志归档 |
| **结构不迭代** | 初始结构定义后从不更新 | 每季度Review结构有效性，任务稳定后调整分层 |

## 演变与派生

- src_unknown
- src_unknown
- src_unknown

## 关联案例

- src_unknown
- src_unknown

## 关联概念

- src_unknown
- src_unknown
