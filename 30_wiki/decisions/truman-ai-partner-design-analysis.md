---


date: 2026-06-07
author: 黄药师（Builder）
source_context: KDO infrastructure decision — internal design record （原 legacy，已从
  title/context/filename 推断为 src_20260503_52ae08ba）
source_refs: []
status: draft
type: analysis
domain:
- ai
- yitang
related:
- [[dk-modeling-ai-judgment-limit]]
- [[dk-modeling-ai-compound-leverage]]
- [[master-ai-info-literacy]]
- [[dk-modeling-ai-without-judgment]]
- [[dk-wanghuan-standard-by-iteration]]
- [[yt-note-ai-human-division]]
- [[yt-note-checklist-concept]]
id: truman-ai-partner-design-analysis
reviewed_by: pending
created_at: '2026-06-15'
confidence: 0.6
trust_level: low
title: truman ai partner design analysis
updated_at: '2026-06-16'# Truman AI Partner（阿蕊老师）设计反推

## 摘要

基于 Truman 口述稿、清单体笔记课程内容、老顽童的卡片产出、洪七公的 OCR 结果，逆向推导了 Truman 的 AI Partner agent 设计。核心发现：Truman 设计的不是"最强的 AI"，而是"最能让人成长的 AI"。三个硬约束（P 角色、L1-L2 边界、清单体 I/O）构成了设计的骨架。

---

## 一、架构三层

```
┌─────────────────────────────────────┐
│              上层工作流              │
│  用户输入(清单体) → Agent执行 → 输出(清单体)  │
├─────────────────────────────────────┤
│              底层逻辑                │
│  P角色身份 · 一堂知识库 · L1-L2边界  │
├─────────────────────────────────────┤
│              元层                   │
│  "你把它当什么，它就变成什么"         │
│  上下文定位决定输出天花板             │
└─────────────────────────────────────┘
```

Truman 原话确认三层结构："agent 的封装的**底层逻辑**和**上层的工作流**"。

---

## 二、四个核心设计决策

### 决策 1：P 角色而非 C 角色

| | P 角色（实践者） | C 角色（顾问） |
|:---|:---|:---|
| 做什么 | 直接干活 | 探讨、建议 |
| 说话风格 | 废话很少 | 解释为什么 |
| 交互模式 | 接收→执行→交付 | 对话→分析→推荐 |

选择 P 角色的原因：如果让 AI 做 C 角色，它会开始"替你想"。L4-L5 的思考必须人类独占。P 角色是防止 AI 越界的硬约束。

推测系统 prompt 片段：

> 你是一个实践者，不是一个顾问。你不探讨、不说教、不解释"为什么"。你直接干活。用户交代的事情，你迅速完成，交付一个干净的结果。不要做判断。不要替用户决定什么重要。你只负责结构和格式。判断留给人。

### 决策 2：清单体作为 I/O 协议

```
传统方式：prompt 描述任务 → AI 理解 → AI 输出
Truman方式：清单体笔记 → 笔记 = prompt + context → AI 输出清单体
```

Truman 把 prompt engineering 变成了 note-taking engineering。写好笔记 = 写好 prompt。

| 维度 | Prose（20000字） | 清单体（3000字） |
|:---|:---|:---|
| 结构信号 | 隐藏在段落中 | 显式（分点+分层） |
| Token 消耗 | 高 | 低 5-10x |
| 幻觉概率 | 高 | 低 |
| 人类可读 | 逐字读 | 5 分钟扫读 |

### 决策 3：L1-L2 硬边界

```
L1 备忘 ──── AI 极其擅长 ────┐
L2 整理 ──── AI 非常擅长       │ AI Partner 领地
L3 内化 ──── AI 辅助，判断由人 │ "在词这一层就能把活干差不多"
───────────────────────────────┘
L4 建模 ──── AI 很弱 ──────────┐
L5 现场 ──── AI 完全不行       │ 人类独占
L6 资产 ──── 标准由人定义 ──────┘
```

边界是设计上的硬约束，不是 AI 能力的自然边界。系统 prompt 中有明确的禁止清单。

### 决策 4：上下文定位决定天花板（元设计）

"你把它想象成什么，它就会慢慢变成什么"——这是 agent 设计的元层原理：

```
用户心态         → 提供的上下文        → AI 输出质量
当跟班             简略、敷衍             下限
当业务负责人       清晰、完整             中等
当合伙人/专家顾问  深度、建模级上下文     上限
```

Agent 的质量上限不是模型决定的，是用户给它的上下文决定的。一个人的笔记水平（L几）直接决定了他能给 AI Partner 什么质量的输入。这就是 Truman 说的"你们追求越高这个 partner 价值越大"。

---

## 三、Agent 封装工作流（推测）

```
用户输入(清单体) → Agent解析(层级/边界) → Agent执行(L1备忘/L2整理) → Agent输出(清单体)
                        │                       │                      │
                        ▼                       ▼                      ▼
                 结构化笔记=prompt          只做格式和结构       人类做L3+内化/建模
                 无需二次翻译              不做判断和取舍
```

关键环节：
- src_unknown
- src_unknown
- src_unknown

---

## 四、为什么能 work——三条核心原理

### 1. 数据飞轮

```
用户记笔记(清单体) → AI处理 → 用户增强(AI输出+L3思考)
      ↑                                      │
      └── 更好的输入 ← 更好的审美 ←──────────┘
```

### 2. 格式即接口

清单体是人类认知和 AI 数据结构之间的适配层。不需要中间的"翻译"步骤。这就是"最大公约数"的真正含义。

### 3. 约束即能力

每个"限制"实际上都让人站到了正确的位置：
- src_unknown
- src_unknown
- src_unknown

**Truman 设计的不是"最强的 AI"，而是"最能让人成长的 AI"。**

---

## 五、对 KDO 的启示

Truman 的 AI Partner 设计与 KDO 的架构高度同构：

| Truman AI Partner | KDO |
|:---|:---|
| 清单体 = prompt + context | 卡片 = KDO 的知识原子 |
| P 角色 = 只执行不讨论 | Builder/Producer 角色分工 |
| L1-L2 边界 = 硬约束 | 质量门 = 自动化校验 |
| 上下文定位决定天花板 | Agent context 决定输出质量 |
| 1500 篇模型笔记 = 知识库 | Graph RAG = 语义检索层 |

KDO 的 Graph RAG + 清单体格式卡片天然适合封装成同类型的 domain agent。
