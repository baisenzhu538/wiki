---
title: 飞轮基础设施提案：将知识挖掘飞轮固化为 KDO 系统机制
type: improvement-plan
status: draft
domain:
- master
created_at: 2026-06-02
updated_at: 2026-06-02
target_roles:
- 欧阳锋（Architect）
reviewer: 欧阳锋
author: 黄药师
source_context: KDO internal record
source_refs: []
related:
- knowledge-flywheel-discovery-20260602
- sprint-6-four-death-sentences
- kdo-industrialization-manual
- proposal-deep-synthesis-infrastructure
id: proposal-kdo-flywheel-infrastructure
reviewed_by: pending
confidence: 0.6
trust_level: low
---

# 飞轮基础设施提案

> **触发**：今晚六个循环的知识挖掘飞轮，全部是意外触发的——没有流程支撑。如果飞轮依赖"用户刚好说了一句不够深刻"，它就不会稳定转。
> **提案**：把飞轮从人的习惯固化为系统的机制。

---

## 一、飞轮的解剖：是哪六个循环、每个循环的能量从哪来

| 循环 | 动作 | 触发方式 | 如果是系统机制会怎样 |
|:--:|------|:--:|------|
| 1 | 诊断三步编译法盲区 | 用户说"不够深刻" | `kdo validate --article` 的 D1-D4 自动标记深度不足 |
| 2 | 用新产线自写文章 | 黄药师主动试写 | `kdo produce --deep` 强制建造者自己先用 |
| 3 | Feedback 三个问题 | 文章末尾的 Feedback 段 | `kdo feedback --auto-enrich` 自动将 Feedback 问题路由到下一轮 produce |
| 4 | 深推 U/D/Pilot | 用户追问 | `kdo flywheel --next` 自动识别上一轮 Feedback 中最高杠杆的问题 |
| 5 | 跑 Pilot 实验 | 用户说"跑 Pilot 拿数据" | `kdo pilot --card N` 标准化实验流程 |
| 6 | 发现 chunk_type bug | 数据分析 | `kdo label --audit` 自动检测标注异常分布 |

**当前状态**：全部靠人推。**目标状态**：每个循环都有对应的 CLI 命令或门禁自动触发。

## 二、飞轮的核心规律：建造→使用→反思→实验

六个循环不是随机的。它们遵循同一个三拍节奏：

```
建造（Build）：建一个工具/框架/门禁
    ↓
使用（Use）：建造者自己用这个工具做真实产出
    ↓
反思（Reflect）：在使用中发现摩擦 → 问"为什么"→ 挖深一层
    ↓
实验（Experiment）：当推理碰壁时，跑实验拿数据
    ↓
回到建造（用新发现驱动下一轮）
```

**每个循环的能量来源不是"计划"，是"摩擦"。** 建造者必须同时是使用者——否则感受不到摩擦。感受不到摩擦就发现不了下一层问题。

## 三、把这四个步骤固化为 KDO 命令

### 3.1 `kdo produce --deep`（建造+使用合一）

当前 `kdo produce` 生成 TODO 骨架。深度合成模式下，强制建造者填写 Judge 段落（自我应用/边界判断/转换叙事）后才允许 ship。

```
kdo produce content/article --topic "AI数据" --deep
  → 生成 deep-synthesis-article 模板
  → 建造者填写全文
  → kdo validate --article（含 D1-D4）
  → D1-D4 不通过 → 退回，标注具体缺失维度
  → D1-D4 通过 → 进入 Feedback 收集
```

### 3.2 `kdo feedback --escalate`（反思自动化）

当前 `kdo feedback` 只记录。新增 `--escalate` 模式：当 Feedback 段包含"？"结尾的问题时，自动提取问题 → 创建下一轮 produce 工单。

```bash
kdo feedback --kind eval-results --escalate
  → 解析文章的 Feedback 段
  → 匹配"？"结尾的句子 → 提取为问题列表
  → 按问题类型路由：
      - "是否应该..." → 创建 decision 工单
      - "如何..." → 创建 improvement-plan 工单
      - "什么场景下..." → 创建 experiment 工单
  → 写入 70_product/tasks/flywheel-{date}.md
```

### 3.3 `kdo pilot --card N`（实验标准化）

当前 Pilot 是 ad-hoc 脚本。标准化为命令：

```bash
kdo pilot --card 20 --domains master,yitang,ai-saas --output pilot-results.json
  → 自动分层选卡（domain × type × chunk密度）
  → 跑 auto_label_chunk()
  → 产出分布报告（每维度值分布 + 异常检测）
  → 写入 60_feedback/data-quality/label-results/
```

### 3.4 `kdo label --audit`（数据驱动的下一轮）

标注完成后自动检测异常：

```bash
kdo label --audit pilot-results.json
  → 检测：某个值占比 > 50%？→ 可能聚集
  → 检测：出现不在候选值的标签？→ bug
  → 检测：某个维度的值分布与 Gold Standard 显著偏离？→ prompt 问题
  → 输出：飞轮下一轮的建议方向
```

## 四、飞轮命令的串联：一条命令转一圈

最终形态：

```bash
# 一圈飞轮 = 一条命令
kdo flywheel --topic "KDO 数据架构" --from article_20260602

# 等价于：
# 1. kdo produce --deep（基于上一轮的 Feedback 问题）
# 2. 建造者填写 → kdo validate --article（D1-D4）
# 3. kdo ship
# 4. kdo feedback --escalate（提取新问题 → 创建下一轮工单）
# 5. 如果 Feedback 含"跑实验"关键词 → kdo pilot --card 20
# 6. kdo label --audit → 飞轮下一轮建议
```

## 五、飞轮的可迁移性

### 今晚的飞轮为什么有效

六个循环共享三个条件：

| 条件 | 含义 | 反例 |
|------|------|------|
| **建造者 = 使用者** | 建工具的人必须自己先用 | 黄药师建了 label 管线，自己写文章时发现四个死刑 |
| **反馈通道畅通** | 使用者能立刻告诉建造者哪里不够好 | 用户说"不够深刻"→ 开启了整个链条 |
| **摩擦力可见** | 每次使用都能暴露新问题 | Feedback 段强制写"不足或遗漏" |

### 可迁移到什么场景

**1. 产品设计**：设计师建了组件 → 自己用组件做页面 → 发现组件在 XX 场景下不好用 → 改进组件。飞轮 = Design → Dogfood → Friction → Refine。

**2. 代码审查**：写了一个 lint 规则 → 用自己的代码跑这个规则 → 发现误报/漏报 → 改进规则。飞轮 = Rule → Self-lint → False Positive → Fix。

**3. 学习方法论**：学了一个框架 → 用它分析自己的一个真实决策 → 发现框架在 XX 条件下失效 → 修正框架的理解。飞轮 = Learn → Apply to Self → Find Edge Case → Deepen。

**4. 商业策略**：做了一个市场判断 → 用这个判断做一次真实投入 → 发现判断的前提假设错了 → 修正判断模型。飞轮 = Hypothesis → Bet → Surprise → Update Model。

### 可迁移的通用模板

```
1. 建一个东西（工具/框架/判断/规则）
2. 自己先用它做一次真实的事（不能是 toy example）
3. 问三个问题：
   - 哪里和我预期不一样？
   - 这个不一样是执行问题还是设计问题？
   - 如果是设计问题，根因是什么？
4. 基于根因，建下一个东西
5. 循环，直到连续两次使用没有发现新的"设计问题"
```

### 什么时候不能迁移

| 场景 | 为什么飞轮转不起来 |
|------|------|
| 建造者和使用者是不同的人 | 建造者感受不到摩擦，反馈是二手的 |
| 没有真实使用场景 | toy example 没有摩擦力 |
| 反馈通道断裂 | 使用者发现问题但不说，或者说了建造者不听 |
| 一次性任务 | 不需要第二轮 |

---

## 六、实施建议

| 优先级 | 行动 | 负责 |
|:--:|------|:--:|
| P0 | 欧阳锋审查本提案 | 欧阳锋 |
| P1 | Sprint 6 断裂点 3（feedback 回流）融入飞轮的 escalate 逻辑 | 黄药师 |
| P1 | `kdo pilot --card N` 命令化 | 黄药师 |
| P2 | `kdo label --audit` 异常检测 | 黄药师 |
| P2 | `kdo flywheel` 全串联命令 | 黄药师 |

---

*黄药师 · 2026-06-02*
