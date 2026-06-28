---
id: tool-纪浩-problem-validation-four-checks
title: 技能：四问验证法 —— 判断需求是真实Problem还是伪需求
type: tool
status: enriched
domain:
- src_unknown
- src_unknown
source_person: 纪浩
source_context: AI俱乐部·AI协作方法论分享（2026年）
source_refs:
- 00_inbox/纪浩-AI协作方法论-口述.md
created_at: '2026-06-09'
updated_at: '2026-06-28'
related:
- pending_unknown
- pending_unknown
- pending_unknown
- pending_unknown
- pending_unknown
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
- lens: 伪需求识别
  follow_up: 执行Step 1：要求用户描述解决前后的具体行为变化，说不清=想象需求
- lens: 需求真实性争议
  follow_up: 用四问逐一验证，任何一问答案不满意=伪需求，需重新定义
- lens: 因果链断裂
  follow_up: 检查Step 4因果链：每个环节是否有具体能力/资源支撑？缺了哪个环节？
- lens: 四问未迭代
  follow_up: 每达到一个里程碑回顾四问，Problem定义随信息增加而演化
- lens: 强制性任务
  follow_up: 四问对强制需求可能走过场，改问：如果可以选择不做，这个需求还值得做吗？

---
# 技能：四问验证法

## Actionable Steps

**当你想判断一个需求是真实Problem还是伪需求时，依次问这四个问题：**

### Step 1：Before & After

**问题：解决之前和之后是什么状态？**

- src_unknown
- src_unknown
- src_unknown

### Step 2：真实锚点

**问题：问题的具体场景在哪里？**

- src_unknown
- src_unknown
- src_unknown

### Step 3：受益人

**问题：解决之后谁觉得开心？**

- src_unknown
- src_unknown
- src_unknown
- src_unknown

### Step 4：因果链与能力支撑

**问题：这个问题是可解的吗？**

- src_unknown
- src_unknown
- src_unknown
- src_unknown

**验证结果：**
四个问题都有满意答案 = 真实Problem，可以下场动手。
任何一个问题答案不满意 = 伪需求，需要重新定义。

## 关键要点

1. **真实锚点是筛选器：**大多数伪需求的问题在于没有真实场景，是"如果有XX就好了"的想象。
2. **不要在步骤1之前做步骤4：**很多人一上来就研究解决方案，但如果Before/After都说不清楚，方案再好也没用。
3. **因果链是故事讲通的关键：**即使有真实场景和受益人，如果解决方案缺少关键环节，项目也会失败。

## Claims

1. **伪需求的根本特征是缺少“真实锚点”，而不是“理论完整性”**
   - src_unknown
   - src_unknown

2. **因果链验证是可执行性的最后一道门，也是创业者最容易跳过的门**
   - src_unknown
   - src_unknown

3. **四问不是一次性活动，而是项目全生命周期的“导航仪”**
   - src_unknown
   - src_unknown

## 判断标准

| 标准 | 自检问题 |
|:-----|:---------|
| 四问全部通过 | 每个问题都有满意的答案，且有具体的事实/数据支撑吗？ |
| Before/After 可观察 | Before和After之间的变化是否可量化或可视化？ |
| 真实锚点确认 | 能说出具体的时间、地点、人物、动作吗？ |
| 受益人明确 | 受益人是能命名的具体人，而非"所有人"或"未来用户"吗？ |
| 因果链可解 | 解决方案的每个环节都有具体的能力或资源支撑吗？ |

## 常见失误与解决方案

**失误1：用"谁需要"代替"是不是真需要"。**
- src_unknown

**失误2：四问通过后不做记录。**
- src_unknown

**失误3：四问只做一次，不随项目进展更新。**
- src_unknown

## 相关案例

- src_unknown

## 关联概念

- src_unknown
- src_unknown

- src_unknown

## Constraints & Boundaries

### 适用边界

| 边界 | 说明 |
|:-----|:-----|
| ✅ 适合 | 创业项目启动前判断需求真实性 |
| ✅ 适合 | 团队对需求有分歧需要结构化验证 |
| ✅ 适合 | 业务遇到瓶颈时检查是否解决了错的问题 |
| ✅ 适合 | 有≥1周时间做需求调研和信息收集 |
| ❌ 不适合 | 强制性任务（上级指派） → 四问可能走过场，改问"如果可选不做还值得做吗" |
| ❌ 不适合 | 时间窗口极窄（<3天） → 四问需要信息收集时间，来不及做完整验证 |
| ❌ 不适合 | 判断"市场大不大" → 四问只验证"是不是真需求"，不验证市场规模 |
| ❌ 不适合 | 纯情感/潜在欲望类创新 → 用户自己说不清楚的需求，四问可能过滤掉真正创新 |

### 常见失败模式

| 模式 | 症状 | 修复 |
|:-----|:-----|:-----|
| **用"谁需要"代替"是不是真需要" | 有需求就认为是真实需求 | 必须用四问逐一验证，而非直接采纳 |
| **四问通过后不做记录** | 验证完就忘，项目走偏无法回溯 | 将四问答案写成文档，作为项目"出生证明" |
| **四问只做一次** | 项目执行到一半发现方向错了 | 每达到一个里程碑回顾四问，Problem定义随信息演化 |
| **信息不足硬答** | 对业务不够了解，四问回答不出来 | 先做调研，信息不足时标注"待验证"而非强行回答 |
| **敏捷反噬** | 认为四问太慢，直接做MVP | 四问+MVP不矛盾：四问定方向，MVP验假设，各负责不同环节 |
| **设计思维冲突** | 四问过滤掉用户情感需求 | 四问后加一步：用户情感动机是什么？是否被满足？ |
| **因果链过度乐观** | 认为每个环节都有支撑，实际缺资源 | 每个环节必须具体到：谁、用什么、在什么时候、花多少 |

## 外部攻击

**1. 敏捷开发范式（Agile/Lean Startup）**

> "四问太慢了。在快速变化的环境中，等你四问完，机会窗口已经关闭了。正确的做法是先做一个MVP投入市场，用实际数据验证需求。四问是分析法，但市场不等人分析。"

**2. 设计思维范式（Design Thinking）**

> "四问过于理性和分析性，忽视了用户的情感需求和潜在欲望。真正的创新往往来自于用户自己都说不清楚的需求。如果只做四问，iPhone不会被发明出来，因为用户根本不知道自己需要一个没有键盘的手机。"

## Synthesis

### 关联知识节点
- src_unknown
- src_unknown
- src_unknown

### 知识体系定位
- src_unknown
- src_unknown

### 跨学科锚点
- src_unknown
- src_unknown
