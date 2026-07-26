---
id: method-judge-skill-meta-evaluation
title: Judge Skill——评判 Skill 的 Skill：五维度元评估与3轮迭代法
type: method
status: reviewed
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-07-07
confidence: 0.88
trust_level: high
language: zh-CN
created_at: 2026-07-07
updated_at: 2026-07-07
domain:
- ai-collaboration
- yitang
source_refs:
- C:/Users/Administrator/Desktop/从知识库到agent.txt
related:
- '[[method-kdo-agent-design-meta]]'
- '[[agent-spec-dual-triangle-canvas-filler]]'
- '[[framework-yihang-dual-triangle-weapon-library]]'
- '[[method-kdo-agent-distillation]]'
- '[[dk-ai-collaboration-degradation-spiral]]'
diagnostic_signals:
- signal: Skill/Agent-spec 上线后效果不稳定，有时好有时差
  lens: 缺质量门控——Skill 没有内置自检机制
  follow-up: 用 Judge Skill 五维度逐项打分，优先补"质量门控"和"已知坑"
- signal: Agent 在非目标场景下也尝试使用 Skill，结果很糟
  lens: 缺信任边界——Skill 没有定义"不可迁移场景"
  follow-up: 补 When NOT to Use，用真实失败案例定义边界
- signal: 改了很多轮 Prompt 但效果没有明显提升
  lens: 缺结构化打磨流程——改完没有打分验证
  follow-up: 用 Judge Skill 打分→按反馈修改→再打分，至少3轮
quality_labels:
- actionable
- principle
- validated
tags:
- audience:general
- scene:diagnosis
- skill-level:advanced
---

# Judge Skill——评判 Skill 的 Skill：五维度元评估与3轮迭代法

> **一句话**：蓝鱼提出的"评判 Skill 的 Skill"——不靠感觉评价一个 Skill/Agent-spec 好不好，而是按五个维度逐项打分，每轮修改后重新打分，通常 3 轮从 30 分拉到 90+。这是 Skill 质量从"靠手艺"到"可度量"的关键拐点。

---

## 一、原始表述

蓝鱼分享（《从知识库到agent》）：

> "做了评判 Skill 的 Skill（Judge Skill），按五维度打分——输出标准/信任边界/已知坑/提示词约束/质量门控。30分→52分→84分→95分，3 轮迭代。"

> "Skill 是包含七个要素的复杂体系——流程、标准、示例输出格式、纠错、小循环、信任边界、已知坑、质量门控。缺任一要素，Skill 就不完整。"

---

## 二、为什么要用 Judge Skill

| 没有 Judge Skill 时 | 有 Judge Skill 时 |
|:---|:---|
| 靠感觉判断 Skill 好不好——"感觉不太对" | 五维度逐项打分——知道具体哪个维度弱 |
| 修改后不知道有没有进步 | 每轮修改后重新打分——30→52→84→95，进步可视化 |
| 不同人评判标准不一致 | 统一打分框架——所有人用同一把尺子 |
| Skill 上线后效果不稳定 | 五维度全齐的 Skill 有内置自检——出问题有信号 |

---

## 三、五维度评估标准

| 维度 | 检查什么 | 评分标准 | KDO Agent-spec 对应 |
|:---|:---|:---|:---|
| **1. 输出标准** | 是否定义了期望输出格式与质量要求 | 有明确的输出模板/格式说明→满分；只有模糊描述→扣分 | Output Gate |
| **2. 信任边界** | 适用领域 vs 不可迁移场景 | 列出了 ≥3 个不可用场景→满分；没有 When NOT to Use→扣一半以上 | When NOT to Use |
| **3. 已知坑** | 列出常见失效情形 + 诊断信号 | 每条坑有症状+修复→满分；只列坑名无修复→扣分 | Failure Modes |
| **4. 提示词约束** | 规则约束，防止跑偏/幻觉 | 有明确的反幻觉规则/行为边界→满分；只有笼统的"不要犯错"→扣分 | Anti-hallucination Rules |
| **5. 质量门控** | 内置自检机制 | 有 Action Triggers + 验证步骤→满分；无自检→扣分 | Action Triggers |

---

## 四、打分量表

| 分数 | 含义 | 判断标准 | 示例 |
|:---|:---|:---|:---|
| **30分** | 初版框架 | 有基本流程描述，但缺标准/边界/坑/约束/门控——五维全空 | 蓝鱼选书 Skill 初版：只有"怎么做"的流程，其他四维空白 |
| **50-60分** | 补了标准+边界 | 输出标准写清楚了，信任边界也写了几条——但坑和约束还是空的 | 补了"输出应为结构化书单 + S/A/B/C 评级说明"和"不适用于小说/文学类" |
| **80+分** | 四维齐 | 标准/边界/坑/约束都有了，但缺质量门控（没有自检机制） | 加了已知坑（Z-Library 单账号限10本）和约束（优先权威来源） |
| **95分** | 五维全齐 + 实测验证 | 五个维度都有 + 经过 ≥1 次真实场景测试并有迭代记录 | 加了"质量门控：生成后自检——是否遗漏了某类推荐源？是否解释了每类为什么选？" |

---

## 五、迭代流程

```
Step 1：初版生成
  用完整的 Data Pack + 一段指令，让 AI 封装成初版 Skill
  → Judge Skill 评分：约 30 分

Step 2：Judge Skill 评估
  用五维度逐项打分，产出"扣分项 + 修改建议"
  不是笼统的"改一下"，是指出具体哪个维度缺什么

Step 3：按反馈修改
  针对 Judge Skill 指出扣分的维度，逐项补充——
  - 缺输出标准 → 补模板
  - 缺信任边界 → 补 When NOT to Use
  - 缺已知坑 → 每坑写症状+修复
  - 缺约束 → 补反幻觉规则
  - 缺门控 → 补 Action Triggers

Step 4：重新评分
  修改后的 Skill 再跑 Judge Skill，对比上一轮分数
  → 蓝鱼数据：30→52→84→95

Step 5：迭代至达标
  通常 3 轮从 30 拉到 90+。达标标准：五维度全齐 + 真实测试验证通过
```

---

## 六、蓝鱼实战数据

以"小书童选书 Skill"为例的迭代记录：

| 轮次 | 分数 | 变化 | 补了什么 |
|:---:|:---:|:---|:---|
| 初版 | 30 | — | 只有流程描述 |
| 第1轮修改 | 52 | +22 | 补了输出标准 + 信任边界 |
| 第2轮修改 | 84 | +32 | 补了已知坑 + 提示词约束 |
| 第3轮修改 | 95 | +11 | 补了质量门控 + 真实测试验证 |

**关键观察**：
- 第1轮增幅最大（+22）——补齐最明显的结构缺陷
- 第2轮增幅最大（+32）——补坑和约束是最核心的质量提升
- 第3轮增幅最小（+11）——边际递减，说明已经接近上限

---

## 七、KDO Agent-spec 评分速查

用这套标准评价 KDO 现有的 Agent-spec 卡片：

| 维度 | 检查方法 | 常见问题 |
|:---|:---|:---|
| 输出标准 | 看 agent-spec 有没有"Output Gate"段 | 多数有，但格式不够具体——"输出诊断报告"不够，要"输出包含六段的标准诊断报告模板" |
| 信任边界 | 看有没有"When NOT to Use"段 | 多数缺——Agent 在非目标场景下也在用，产出质量差 |
| 已知坑 | 看 Failure Modes 段有没有症状+修复 | 多数有坑名但缺修复步骤——"输出格式不一致"→修复是什么？ |
| 提示词约束 | 看 System Prompt 中有没有行为边界 | 多数集中在"做什么"，缺"绝对不做什么" |
| 质量门控 | 看有没有 Action Triggers 或自检步骤 | 多数缺——Agent 输出后没有"对不对"的检查 |

---

## 八、Skill 七要素参考（蓝鱼框架）

Judge Skill 的五个评分维度源自蓝鱼的 Skill 七要素定义：

```
Skill ≠ Prompt

Skill = 流程（Process）
      + 标准（Standard）
      + 示例输出格式（Example Output Format）
      + 纠错（Error Correction）
      + 小循环（Mini Loop）
      + 信任边界（Trust Boundary）
      + 已知坑（Known Pitfalls）
      + 质量门控（Gating/Check）
```

> "缺任一要素，Skill 就不完整。缺失要素会导致 Agent 理解偏差、过度自由发挥、反复试错浪费 Token。"——蓝鱼

---

## 九、Critique

**[Over-Engineering Skeptic]**
> "不是每个 Skill 都需要五维度全齐。一个简单的'搜一下'Skill，写清楚搜索词就够了，加上信任边界和质量门控是过度设计。"

**回应**：同意。Judge Skill 适用于"会被反复调用、输出影响决策质量"的 Skill。对于一次性/简单查询类 Skill，可以用轻量版——只检查"输出标准"一个维度。五维度全齐是质量上限，不是所有场景的最低门槛。

**[Iteration Cost Realist]**
> "3 轮迭代从 30 到 95 分——看起来很美，但第1轮到第2轮之间最耗时。补坑和约束需要真实使用才能发现，不是坐在那里想就能想出来的。"

**回应**：对。第2轮的"已知坑"和"提示词约束"不能靠凭空想象——必须有 ≥1 次真实测试作为输入。蓝鱼的 30→52→84→95 是建立在"小书童已上线使用，暴露了问题"的基础上。Judge Skill 不能替代实战测试，它的作用是把实战中暴露的问题**结构化地吸收进下一版 Skill**。

---

## Constraints & Boundaries

### 适用边界

| 场景 | 适合？ | 说明 |
|:---|:---:|:---|
| 会被反复调用的 Agent-spec / Skill | ✅ | 投入 3 轮迭代有复利 |
| 输出影响决策质量的 Skill | ✅ | 值得五维度全齐 |
| 新 Skill 上线前的质量检查 | ✅ | 至少覆盖输出标准+信任边界 |
| 简单一次性查询 | ❌ | 过度设计，只需检查输出标准 |
| 刚写完还没用过一次的 Skill | ⚠️ | 先跑一次再用 Judge Skill——没有实战数据，坑和约束填不出来 |

### 常见失败模式

| 模式 | 症状 | 修复 |
|:---|:---|:---|
| 打分走过场 | 每次都是"80分挺好的"，没有具体扣分项 | 强制每个维度必须给出"扣分原因 + 修改建议"——不能只写"OK" |
| 只打分不改 | 知道哪里差但不去改，下次打分还是同一个分数 | 每轮打分后把修改建议抄进 TODO，改完再打分 |
| 坑靠编 | 已知坑写的是"可能出现幻觉"这种通用废话 | 每条坑必须有真实触发场景——"上次在XX输入下，Agent 做了YY，导致ZZ" |
| 迭代停在84 | 四维度齐了就满意了，不加质量门控 | 质量门控是区分"好用"和"可靠"的最后一公里——不加门控=上线后靠人盯着 |
| 过度追求95 | 一个简单 Skill 反复迭代 5 轮以上 | 设定终止条件：连续2轮分数增长<5分→停止，边际递减不值得 |
