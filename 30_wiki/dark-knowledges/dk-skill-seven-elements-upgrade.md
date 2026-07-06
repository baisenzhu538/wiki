---
id: dk-skill-seven-elements-upgrade
title: Skill ≠ Prompt——蓝鱼七要素告诉你完整 Skill 缺了什么
type: dk
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
- "[[method-judge-skill-meta-evaluation]]"
- "[[method-kdo-agent-design-meta]]"
- "[[agent-spec-dual-triangle-canvas-filler]]"
- "[[method-kdo-agent-distillation]]"
- "[[dk-ai-collaboration-degradation-spiral]]"
diagnostic_signals:
- signal: Agent 在某个步骤出错后无法自我纠正，继续往下走错得更远
  lens: 缺纠错要素——Skill 没有 Error Correction 机制
  follow-up: 在 Skill 中增加纠错段：当输出出现 X 时→回退到上一步，重新执行
- signal: Agent 一次生成后直接输出结果，中间没有自我检查
  lens: 缺小循环——Skill 没有 Mini Loop
  follow-up: 在关键步骤后加 Mini Loop：生成→自检→如果不通过→修正→再自检
- signal: Skill 上线后发现各种边缘情况没覆盖，反复打补丁
  lens: 七要素不全——缺 Trust Boundary 和 Known Pitfalls
  follow-up: 用 Judge Skill 五维度打分，优先补边界和坑
quality_labels:
- actionable
- insight
- principle
---

# Skill ≠ Prompt——蓝鱼七要素告诉你完整 Skill 缺了什么

> **一句话**：蓝鱼提出的 Skill 七要素框架（流程/标准/示范/纠错/小循环/边界/已知坑 + 质量门控）揭示了 KDO agent-spec v3 的两个系统性缺口——纠错（Error Correction）和小循环（Mini Loop）。缺了这两个，Agent 出错后靠人兜底而不是自己修复。

---

## 原始表述

蓝鱼（《从知识库到agent》）：

> "Skill 是包含七个要素的复杂体系——流程、标准、示例输出格式、纠错、小循环、信任边界、已知坑。缺任一要素，Skill 就不完整。缺失要素会导致 Agent 理解偏差、过度自由发挥、反复试错浪费 Token。"

> "光有 Skill 标准不够——没有衡量标准就无法达到预期效果，评估全靠感觉会浪费 Token、模型绕圈、缺关键节点自己还不知道。"

---

## 使用场景

- 新建 Agent-spec / Skill 时，用七要素做结构检查
- 现有 Skill 效果不稳定时，用七要素诊断缺了哪个
- 团队对齐 Skill 质量标准时，七要素作为共同语言
- 评估外部 Skill（别人的 Agent prompt）时，七要素作为对比框架

---

## 操作方法

### 蓝鱼 Skill 七要素 + 质量门控

```
                            ┌─────────────────┐
                            │   质量门控        │  ← 第八要素（元层）
                            │   Gating/Check   │
                            └────────┬────────┘
                                     │ 贯穿全流程
    ┌──────────┬──────────┬──────────┼──────────┬──────────┬──────────┐
    │  流程     │  标准     │  示范     │  纠错     │ 小循环    │  边界     │  已知坑   │
    │ Process  │Standard │ Example  │ Error    │ Mini     │ Trust    │ Known    │
    │          │          │          │ Correct  │ Loop     │ Boundary │ Pitfalls │
    └──────────┴──────────┴──────────┴──────────┴──────────┴──────────┴──────────┘
```

### 七要素逐个说明

| # | 要素 | 做什么 | 缺了会怎样 | KDO agent-spec v3 现状 |
|:---:|:---|:---|:---|:---|
| 1 | **流程（Process）** | 定义 Skill 的执行步骤和顺序 | Agent 不知道先做什么后做什么，输出混乱 | ✅ 有（九层深挖流程） |
| 2 | **标准（Standard）** | 定义期望输出的格式和质量要求 | Agent 输出格式随意，每次不一样 | ✅ 有（Output Gate） |
| 3 | **示范（Example）** | 提供输入→输出的具体示例 | Agent 理解偏差——"我以为是这个意思" | ✅ 有（Few-shot 示例） |
| 4 | **纠错（Error Correction）** | Agent 输出错误时的自我纠正机制 | 一步错步步错，靠人发现后重新跑 | ❌ **缺失** |
| 5 | **小循环（Mini Loop）** | 关键步骤的内置自检→修正→再检循环 | Agent 一次生成直接输出，没有中间检查 | ❌ **缺失** |
| 6 | **信任边界（Trust Boundary）** | 明确不可迁移的场景和领域 | Agent 在不该用的场景也在用，效果很差 | ⚠️ 部分（有不适用清单，但未独立成章） |
| 7 | **已知坑（Known Pitfalls）** | 列出已知失败情形 + 诊断信号 | 踩坑后靠人总结，Agent 不会自己避开 | ⚠️ 部分（有失败模式，但坑≠失败模式） |
| + | **质量门控（Gating）** | 全流程的自检关卡 | 缺了六要素中的任何一个都发现不了 | ⚠️ 部分（有 Action Triggers，但非结构化门控） |

---

### 两个关键缺口深度分析

#### 缺口 1：纠错（Error Correction）

**什么是纠错**：当 Agent 的某个步骤输出不符合预期时，Skill 内置了"识别→回退→重试"机制。不是等人发现错误后重新跑，而是 Agent 自己能发现并纠正。

**KDO 当前问题**：
- Agent-spec 定义了"怎么做对"，没有定义"做错了怎么办"
- 九层深挖的每一层都可能出错——假设检验错了、数据源引用错了、结论跳步了——但没有任何一层有纠错流程
- 后果：人必须逐层检查，发现错误后让 Agent 重新跑——纠错成本在人侧

**蓝鱼的做法**：
```
纠错标准写法（示例）：
- 当输出不满足 [标准X] 时 → 标记为"待修正"，回退到上一步
- 当引用的来源不可验证时 → 标注"⚠️ 未验证"，不进入下一层
- 当连续 2 次尝试仍不满足标准 → 输出"此步骤无法完成，原因：____"，不继续
```

**KDO 应该补什么**：
- 每张 agent-spec 的每个关键步骤增加"错误处理"子段
- 格式：`如果 [检查条件] → 则 [回退/重试/标记/停止]`
- 不是写"Agent 应该检查正确性"（那是废话），是写具体的触发条件和动作

#### 缺口 2：小循环（Mini Loop）

**什么是小循环**：在关键步骤内部，Agent 执行"生成→自检→修正→再生成"的短循环，而不是一次性生成就结束。

**KDO 当前问题**：
- Agent 执行九层深挖时，每层是"输入→输出→下一层"，没有层内自检
- L3（交叉验证）需要多轮搜索→比对→修正，但当前是一次搜索就过
- 后果：Agent 生成很快，质量靠运气——有时候刚好搜到好来源就输出好，搜不到就糊弄

**蓝鱼的做法**：
```
Mini Loop 标准写法（示例）：
Step 3：交叉验证
  Loop（最多 3 轮）：
    1. 搜索 → 获得 N 条结果
    2. 自检：≥2 个独立来源确认？关键数据可追溯？
    3. 如不通过 → 换关键词重搜 → 回到步骤 1
    4. 如 3 轮仍不通过 → 标记"信息不足，置信度降级"
    5. 如通过 → 进入下一层
```

**KDO 应该补什么**：
- 在需要验证的步骤（交叉验证、归因、结论合成）加入 Mini Loop
- 每轮 Mini Loop 有明确的终止条件——不是无限循环
- Mini Loop 的典型模式：搜索→自检→不够→换策略→再搜→够了→过关

---

### 七要素补充：已知坑 vs 失败模式

KDO agent-spec 已有"失败模式"段，但蓝鱼的"已知坑（Known Pitfalls）"概念更精确：

| 维度 | KDO 失败模式 | 蓝鱼 已知坑 |
|:---|:---|:---|
| 粒度 | 一个失败模式对应一个宏观问题 | 一个已知坑对应一个具体的触发条件 |
| 格式 | "症状 + 修复" | "触发条件 → Agent 会做什么 → 为什么是错的 → 应该怎么做 → 怎么检测" |
| 来源 | 设计者预判 | 实战中踩过的真实坑 |
| 自检 | 无 | 每个坑附带检测信号——"当看到 X 时意味着踩了这个坑" |

**升级方向**：把 KDO 的失败模式从"症状+修复"升级为蓝鱼五段式已知坑——触发条件→Agent 反应→错误原因→正确做法→检测信号。

---

## 适用边界

- **适用于**：会被反复调用的 Agent-spec / Skill；输出影响决策质量的 Skill；团队协作的共享 Skill
- **不适用于**：一次性使用的简单 Prompt；纯探索性对话（没有固定流程）

---

## 为什么值钱

1. **统一了 Skill 质量的共同语言**：不再靠"这个 Skill 感觉不太对"——七要素让缺什么、补什么都明确
2. **识别了 KDO 的两个系统性缺口**：纠错和小循环是目前 KDO agent-spec 最薄弱的两个环节，补上后 Agent 从"靠人兜底"进化到"自我修复"
3. **提供了可操作的升级路径**：不是空谈"要加强质量"，而是给出了每个要素的具体写法和反例
4. **与 Judge Skill 形成互补**：Judge Skill 负责打分（好不好），七要素负责结构（全不全）。两者合在一起构成 Skill 质量的完整保障体系

---

## 与其他知识的关联

- `[[method-judge-skill-meta-evaluation]]`：Judge Skill 五维度评分框架——七要素是"全不全"的检查，Judge Skill 是"好不好"的打分
- `[[method-kdo-agent-design-meta]]`：KDO Agent 设计元方法论——七要素是该方法的"完整性检查清单"
- `[[agent-spec-dual-triangle-canvas-filler]]`：画布 Agent v3——本卡指出的两个缺口（纠错+小循环）是 v4 升级的关键输入
- `[[dk-ai-collaboration-degradation-spiral]]`：退化螺旋中的"工具升级≠系统升级"——七要素齐全的 Skill 才是系统，缺了就是半成品
