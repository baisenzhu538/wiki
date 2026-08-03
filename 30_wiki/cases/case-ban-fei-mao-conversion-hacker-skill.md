---

id: case-ban-fei-mao-conversion-hacker-skill
title: 案例：一堂转化率黑客课→Skill ——从拿到资料到测试通过的完整历程
type: case
status: reviewed
domain:
- ai-collaboration
- yitang
source_person: 半肥猫
source_context: AI俱乐部-AI学习落地 分享
aliases:
  - 一堂转化率黑客课→Skill
  - 从拿到资料到测试通过的完整历程
  - 半肥猫
  - 案例
  - 案例：一堂转化率黑客课→Skill从拿到资料到测试通过的完整历程
  - 转化率黑客课
source_refs:
- 10_raw/sources/src_20260617_2b8a01ce-ai俱乐部-ai学习落地-半肥猫-口述.txt
- 10_raw/sources/src_20260617_26d0ee0b-ai俱乐部-ai学习落地-半肥猫-笔记.txt
created_at: 2026-06-07
updated_at: '2026-06-29'
discoverable_by:
  - 案例：一堂转化率黑客课→Skill ——从拿到资料到测试通过
  - 一堂转化率黑客课→Skill
  - 从拿到资料到测试通过的完整历程
related:
- '[[ai-collaboration-domain-digest]]'
- '[[yitang-domain-digest]]'
pipeline: null
author: 半肥猫
reviewed_by: 欧阳锋
confidence: 0.9
trust_level: high
tags:
- audience:general
- scene:reference
- skill-level:advanced
- 俱乐部
- 半肥猫
- 学习落地
---

# 案例：一堂转化率黑客课→Skill

## 一句话摘要

半肥猫受一堂官方挑战，在一个晚上将《转化率黑客》课程转化为一个有边界、可验证、可安装的 AI Skill，并通过两组真实场景测试验证其“拒绝不适合场景”的能力显著优于通用模型。

## 背景

半肥猫接到一堂官方提出的挑战：拿一堂最经典的《转化率黑客》课程，在一个晚上（到凌晨四点）做成一个有边界、可验证、可安装、可持续迭代的 Skill。这不是简单的课程搬运——而是把一门方法论课程转化为可执行的 AI 协议。

## 关键事件/决策点

### 决策 1：先判断课程值不值得做 Skill

半肥猫的判断：**这门课值得做，但不是做成“转化率万能提效”，而是做成“实验约束型转化率方案推演”。**

判断依据：
- src_unknown
- src_unknown
- src_unknown

> 若这一关过不了，后面七步都不用做，不要浪费时间。

### 决策 2：课程内容的“三中转化”——不是搬运，是重构

半肥猫在制作 Skill 时做的不是简单把课程内容扔给 AI，而是三个核心转化：

1. **方法→协议**：把课程方法论转化为可执行的诊断协议（问题是什么、不是什么、场景分类、评分规则、风险分级）
2. **案例→案例库**：不仅保留课程案例，还补充了国际真实案例、中国案例、中小微企业案例——正面、负面都有
3. **经验→约束**：把课程里隐性的经验映射为明确的执行约束（如何触发、如何拒绝、如何评分）

### 决策 3：证据校准——不是“尊重老师”，是“批判性检视”

半肥猫强调：**不能默认老师的所有观点都正确**。他做了以下动作：
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 结果

两组测试都通过了验证：

| 测试组 | 用 Skill 得分 | 不用 Skill 得分 | 差值 | 结果 |
|:---|:---|:---|:---|
| 烘焙店正常业务 | 36 分 | 8 分 | +28 | ✅ 通过 |
| 保险高风险场景 | 36 分 | 9 分 | +27 | ✅ 通过 |

**核心发现**：两组测试中，最大的差距都出现在“拒绝能力”——用了 Skill 的 AI 会在场景不适合时说“暂时别做”，而通用模型会为了讨好用户说“做吧做吧”。

## 复盘与洞察

1. **边界感是 Skill 质量的分水岭**：优秀的 Skill 不是“什么都能做”，而是“知道什么不该做”。本次案例中，拒绝能力的提升是测试得分差距的主要来源。
2. **课程→Skill 不是压缩，而是再设计**：把课程内容直接喂给 AI 只能得到“懂一点转化率的助手”；只有经过方法协议化、案例库化和经验约束化，才能得到可安装的协作能力。
3. **证据分层提升可信度**：将课程经验、外部权威资料、真实案例分层处理，并对每类证据设置可核验标准，是避免“AI 幻觉污染 Skill”的关键。
4. **对 KDO 的启发**：KDO 现有管线是“素材消化 → 卡片编译 → 知识入库”，缺少“课程→Skill 化”的标准管线。半肥猫的工作流可以补充为：课程素材 → 判断 → 整理 → 协议 → 校准 → 结构 → 测试 → 封装 → Skill。这意味着 KDO 可以在 `40_outputs/capabilities/skills/` 之上，增加一个“课程→Skill 化工作流”的标准操作手册。

## 可迁移模式

1. **KDO 课程的 Skill 化**：KDO 的课程内容（如清单体笔记、AI 协作方法论）可以按同样的八步工作流转化为 Skill。
2. **企业内部培训课程的工具化**：任何有科学方法论底座的培训课程，都可以走这个路径。
3. **个人学习中的“作业→工具”转化**：不限于课程，任何学到的方法论都可以按这个框架沉淀为可复用工具。

## 失败模式/教训

**什么时候不应该直接套用本案例**：
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 相关卡/互链

- src_unknown
- src_unknown

---

## 关键证据

- src_unknown
- src_unknown
- src_unknown

---

## 可迁移场景

| 场景 | 如何套用 | 关键组件/关联卡片 |
|---|---|---|
| src_unknown | src_unknown | src_unknown |

---

## 教训

- src_unknown
- src_unknown
- src_unknown
