---
id: framework-knowledge-naming-systems-comparison
title: 知识编码体系对比：业务流前缀 / PARA / Johnny Decimal（实测体系版）
type: framework
status: pending_review
author: 老顽童
reviewed_by: pending
confidence: 0.85
trust_level: medium
language: zh-CN
created_at: 2026-08-20
updated_at: 2026-08-20
domain:
- knowledge-management
- yitang
aliases:
- 知识编码体系对比
- 知识库编码顺序
- 业务流前缀编号
- 数字前缀工作流顺序
- PARA方法
- JohnnyDecimal
- 知识库编号体系
tags:
  - audience:manager
  - scene:knowledge-management
  - skill-level:intermediate
  - 机制
  - 框架
  - 方法
  - 边界
  - 复盘
  - 口述
source_person: 楚门 + PARA(fortelabs) + Johnny Decimal 官网
source_context: 楚门口述 L1114-1120 + fortelabs.com/blog/para/ + johnnydecimal.com（2026-08-20 实取）
source_refs:
- 00_inbox/AI知识库/楚门-AI知识管理探索营-口述.txt
related:
- '[[dk-doc-numbering-business-logic]]'
- '[[concept-structured-naming-as-infrastructure]]'
- '[[framework-一堂-机会预判]]'
- '[[dk-best-datasource-is-floor]]'
- '[[framework-knowledge-compound-rocket-six]]'
- '[[dk-context-patching-recipe]]'
---
# 知识编码体系对比：业务流前缀 / PARA / Johnny Decimal

> **定位**：属于知识库组织架构的比较框架——三种**实测来源**的编码体系（楚门业务流前缀 / PARA / Johnny Decimal），给出适用边界对照。Zettelkasten/LATCH 因无一手源未纳入（王语嫣门禁条件）。

## 核心结构

```
┌─────────────────┬──────────────────┬─────────────────────┐
│  楚门业务流前缀   │      PARA        │   Johnny Decimal    │
├─────────────────┼──────────────────┼─────────────────────┤
│ 分类轴=业务流顺序 │ 分类轴=行动状态    │ 分类轴=领域+唯一ID   │
│ 1拆解→2最佳实践→  │ P=Projects(有期限)│ 10-19/20-29… 十进位  │
│ 3建模→4报告→5封装  │ A=Areas(长期责任) │ 每项唯一 ID+名称     │
│ →复盘+技能池      │ R=Resources(参考) │                     │
│                 │ A=Archives(归档)  │                     │
└─────────────────┴──────────────────┴─────────────────────┘
```

## 框架说明

> 「首先顶层，这是真实项目的目录……一开头的文档都是关于拆解的基本思路，然后二开头就是市场的最佳实践，然后三开头的文档基本上就是建模和来回测评。四开头的文档就是记那个报告，来回打磨。然后五开头的文档就是封装成 Y 模型要用到的支持四个数据包，最后还有什么复盘文档……技能是封装完了放到一个技能池里面，然后 AI 就可以学了。」（楚门口述 L1114-1118）
> PARA（fortelabs 官方）："Four top-level folders – Projects, Areas, Resources, and Archives"——四个顶层文件夹（2026-08-20 实取 fortelabs.com/blog/para/）
> Johnny Decimal（官网）：十进位编号体系（area 10-19/20-29）+ 名称，每项有唯一 ID；提供 Life Admin / Small Business 模板系统（2026-08-20 实取 johnnydecimal.com）

**核心机制**：
- **楚门业务流前缀**：数字前缀=工作流顺序（1 拆解→2 最佳实践→3 建模测评→4 报告打磨→5 封装数据包→复盘+技能池）——**编号即执行顺序**，AI/人照前缀走完就是完整项目流程（L1120"我只需要最多指定一个位置，说你去那儿，给一个关键词或者一个链接，然后他就能学会"）
- **PARA**：按"行动状态"分类——P 是有目标有期限的项目，A 是长期责任领域，R 是兴趣参考，A 是归档——解决"东西放哪"的决策成本
- **Johnny Decimal**：按"领域+唯一 ID"分类——十进位区间（10-19 是一个领域）+ 名称，每项唯一可引用

## 操作方法

1. **选体系先问分类轴**：你的知识库是"按流程走"（楚门前缀）/"按状态放"（PARA）/"按领域归档"（JD）？
2. **楚门流**（项目全生命周期）：1 拆解→2 最佳实践→3 建模测评→4 报告打磨→5 封装数据包→复盘+技能池——数字前缀=工作流顺序，适合"单项目深度执行"
3. **PARA**（个人知识库顶层）：P/A/R/A 四个顶层文件夹，行动导向——适合"多项目并行管理"
4. **Johnny Decimal**（强结构归档）：十进位编号+名称，唯一 ID——适合"长期静态归档/企业档案"

## When NOT to Use

- 楚门前缀：不适合"知识库全局组织"（它是项目内的流水线编号，不是库顶层架构）
- PARA：不适合"项目内深度流程"（P/A/R/A 不表达执行顺序）
- Johnny Decimal：不适合"频繁变动的活跃项目"（十进位编号重命名成本高）

## 失败模式

| 失败模式 | 信号 | 修复 |
|:--|:--|:--|
| 体系混用 | 项目内用 PARA、库顶层用 JD、文件再用时间戳 | 定一个主体系（按分类轴选） |
| 编号即流程但流程没定 | 前缀有了但每步不知道放什么 | 先定工作流步骤再定前缀（楚门流前提） |
| 归档无唯一 ID | JD 想引用但编号冲突 | 先划领域区间再分配 |
| 只编不放 | 有规范但实际文件乱放 | 规范+工具双落地（Obsidian 模板/插件） |

## 与已有框架的关系

- 与 `dk-doc-numbering-business-logic` 互补：dk 讲"编号=业务逻辑"的洞察，本框架给"三种体系对比"的选型
- 与 `concept-structured-naming-as-infrastructure` 承接：命名/编号是基础设施——本框架是具体方案集
- 与 `framework-knowledge-compound-rocket-six` 关联：知识复利依赖组织架构（编码体系是复利的载体）

## Action Triggers

- 新知识库/项目目录结构设计 → 先选编码体系（按分类轴）
- 项目文件乱放、找不到 → 楚门流前缀（按执行顺序重排）
- 个人知识库顶层混乱 → PARA（按行动状态分）
- 长期归档引用困难 → Johnny Decimal（唯一 ID）

## Critique

> 来源：楚门口述 + PARA/JD 官网实取（2026-08-20），批判性评估为补写。

- **反驳**：三种体系真的互斥吗？——不是。它们是**不同层级**的编码：楚门前缀=项目内流水线，PARA=库顶层状态，JD=长期归档 ID——可以组合使用（库顶层 PARA，项目内楚门前缀，归档后 JD）。
- **反驳**：分类轴是唯一差异吗？——不是。三种体系对"变动成本"的容忍度不同：PARA 最灵活（移动成本低）、JD 最刚性（重编号贵）、楚门前缀居中——选型还要看内容变动频率。
- **条件**：此卡前提=知识库以文档/文件为主（Obsidian 型）；数据库/强结构系统（企业 ERP）不适用此对比。
- **注意**：Zettelkasten/LATCH 未纳入（门禁条件：无一手源）——如需补充须先取一手源再扩展。

## 与其他知识的关联

- `dk-doc-numbering-business-logic`：编号=业务逻辑（洞察层）
- `concept-structured-naming-as-infrastructure`：命名即基础设施（为什么层）
- `framework-opportunity-foresight`：机会预判（跨域 yitang）
- `dk-best-datasource-is-floor`：数据源质量（跨域 research）
- `framework-knowledge-compound-rocket-six`：知识复利六引擎（知识管理域）
- `dk-context-patching-recipe`：上下文补全配方（跨域 ai-collaboration）
