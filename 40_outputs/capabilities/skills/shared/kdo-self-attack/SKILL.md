---
name: kdo-self-attack
description: KDO知识自攻击——用对抗Agent主动找出知识卡片的弱点，在用户发现之前自我修复
version: 1.0.0
author: 黄药师
license: MIT
platforms: [cli, feishu]
metadata:
  hermes:
    tags: [自攻击, 对抗审查, 质量, 自我迭代, GAN, SATs]
    related_skills: [research-sats, ai-collaboration-gan]
---

# KDO 知识自攻击

用 GAN + SATs 对抗 Agent 主动攻击 KDO 自己的知识卡片——在用户/欧阳锋发现问题之前，自己先找到弱点。

## Constraints

<hard_limits>
- 攻击必须基于事实和逻辑，不得为了"找出问题"而编造不存在的漏洞
- 每次攻击结果必须写入 `60_feedback/adversarial/`，形成可追溯的改进记录
- 攻击发现的问题分级：🔴致命（核心主张错误）→ 🟡严重（证据不足）→ 🟢轻微（表述不精确）
</hard_limits>

## 四路攻击 Agent

```
卡片
  ↓
  ├── Attacker A: 逻辑攻击——核心主张的逻辑链成立吗？有没有偷换概念？有没有循环论证？
  ├── Attacker B: 证据攻击——source_refs 能支撑 Claims 吗？数字有出处吗？有没有"口述当事实"？
  ├── Attacker C: 完整性攻击——缺了什么？有没有故意回避的反例？有没有未覆盖的关键视角？
  └── Attacker D: 时效性攻击——信息是否过时？有没有 2025-2026 年的新发现可以补充？
  ↓
合并攻击报告 → 写入 60_feedback/adversarial/
```

## 使用方式

### 单卡攻击
```
/kdo-self-attack <card-id>
```

### 域批量攻击
```
/kdo-self-attack --domain yitang --sample 5
```

### 定期自检（建议每周）
```
/kdo-self-attack --domain yitang --random 3
```

## 四路攻击详解

### Attacker A: 逻辑攻击

| 检查项 | 攻击问题 |
|:--|:--|
| 核心主张 | 这张卡的 Summary 有没有偷换概念？"X 很重要"≠"X 是唯一方案" |
| 因果关系 | Claims 中的因果推断成立吗？相关性被当成因果了吗？ |
| 循环论证 | "这个方法有效因为它是科学方法"→ 循环 |
| 概念漂移 | 同一个词在卡的不同部分含义是否一致？ |

**攻击模板**：
```
我要攻击这张卡的核心逻辑：
1. Summary 声称 [X]，但 [Y] 的证据表明 [反例]
2. Claim 3 的因果推断 [A→B] 忽略了一个关键变量 [C]
3. Constraints 节列出的边界是否足够？[场景Z] 明显也被排除但未提及
```

### Attacker B: 证据攻击

| 检查项 | 攻击问题 |
|:--|:--|
| source_refs 覆盖 | 每条 Claim 都有对应的 source 吗？ |
| 数字可追溯 | 关键数字能追溯到原始来源吗？还是"口述待独立核实"？ |
| 来源层级 | L1官方/L2权威/L3多源/L4推理/L5单源——主要结论的层级够吗？ |
| 幸存者偏差 | 证据是否只来自成功案例？失败案例被排除了吗？ |

### Attacker C: 完整性攻击

| 检查项 | 攻击问题 |
|:--|:--|
| 反例缺失 | 有什么场景下这个框架不适用？卡里说了吗？ |
| 视角盲区 | 如果从竞对/用户/监管的角度看，会指出什么遗漏？ |
| 跨域连接 | 这个域的其他卡有没有矛盾点？有没有应该互链但没链的？ |
| "大象"测试 | 有没有一个显而易见的问题，整张卡都没提？ |

### Attacker D: 时效性攻击

| 检查项 | 攻击问题 |
|:--|:--|
| 数据时效 | 卡里的数字/案例是什么时候的？2024 之前的需要标注 |
| 方法演进 | 这个领域 2025-2026 年有没有重要的新方法未被引用？ |
| 工具更新 | 引用的工具/API 是否还可用？有没有被替代？ |
| 最佳实践漂移 | 业界共识是否已经改变了？ |

## 攻击报告模板

```markdown
# 自攻击报告：<card-id>

**攻击时间**：2026-06-21
**攻击者**：KDO Self-Attack Agent (GAN 四路)

## 攻击摘要
🔴 致命: 0 | 🟡 严重: 2 | 🟢 轻微: 3

## Attacker A: 逻辑
- [🟢] Claim 2 的因果方向可逆——也可能是 Y 导致 X

## Attacker B: 证据
- [🟡] "市场规模 500 亿"无 source 引用，疑似口述
- [🟡] 三个案例全部来自同一个来源——缺乏独立验证

## Attacker C: 完整性
- [🟢] 缺少"什么时候不应该用这个框架"的明确说明
- [🟢] 与 [[相关卡]] 有观点矛盾，未标注

## Attacker D: 时效性
- (无发现)

## 建议改进
1. 补"市场规模 500 亿"的 source_refs
2. 增加至少 1 个独立来源的案例
3. 增加"不适用场景"节
```

## 反馈闭环

```
60_feedback/adversarial/atk_<card-id>_<date>.md
  ↓
Agent/老顽童 读取攻击报告
  ↓
修复 → kdo lint → confidence 更新
  ↓
重新攻击 → 确认修复 → 关闭
```

## 与现有反馈体系的关系

| 反馈类型 | 目录 | 触发方式 |
|:--|:--|:--|
| Agent 诊断反馈 | `60_feedback/diagnosis/` | 王语嫣主动诊断 |
| Agent 修正反馈 | `60_feedback/corrections/` | 发现问题后修正 |
| 用户直接反馈 | `60_feedback/` | 用户提出 |
| **知识自攻击** 🆕 | `60_feedback/adversarial/` | 定期/按需自动触发 |

自攻击和其他反馈的区别：**不等人发现问题——Agent 主动找问题。**

## 相关 Skill

| Skill | 关系 |
|:--|:--|
| `/research-sats` | SATs Devil's Advocacy 在知识域的应用 |
| `/ai-collaboration-gan` | GAN 三角色——本 Skill 的架构原型 |
| `/demand-analysis-synthetic` | 合成调研——同样的"对抗+交叉验证"逻辑，应用于需求假设 |
| `framework-yitang-research-quality-gate` | 六维门禁——自攻击是门禁 5（对立面检验）的自动化执行 |
