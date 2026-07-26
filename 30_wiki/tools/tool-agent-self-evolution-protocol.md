---
id: tool-agent-self-evolution-protocol
title: Agent自我进化协议：每次复盘四问
type: tool
status: reviewed
author: laowantong
confidence: 0.8
trust_level: medium
domain:
- system
source_refs:
- 60_feedback/diagnosis/diag_20260726_wangyuyan-thought-liberation.md
- .agent/pitfalls.md
- 30_wiki/frameworks/framework-kdo-modeling-methodology.md
related:
- concept-kdo-agent-design-principles
- concept-kdo-agent-four-level-awareness
- bridge-lightning-agent-evolution
- dk-agent-evolution-pitfalls
- tool-agent-context-derivation-audit
- framework-kdo-modeling-methodology
- framework-yitang-thought-liberation-lightning
created_at: 2026-07-26
updated_at: 2026-07-26
reviewed_by: 欧阳锋
diagnostic_signals:
- Agent 完成复杂任务后无复盘动作
- 同类型 pitfall 在 30 天内复现
- Agent 改进完全依赖人类推动
quality_labels: cited
tags:
- audience:executor
- scene:execution
- skill-level:intermediate
---

## 核心主张

Agent 每次完成复杂任务（≥5 个工具调用、或遇到错误后恢复、或完成审查）后，必须执行**复盘四问**。这四个问题把 Truman 闪电模型的「建模重构」阶压缩为一个可操作的 Agent 自检流程。

> **定位**：本卡是 `bridge-lightning-agent-evolution` 的「四阶·建模重构」在操作层的落地工具。属于 `framework-kdo-modeling-methodology` 的「第四步·解压展开」——把框架原则解压为可执行的复盘 checklist。

## 适用场景

**触发条件**（满足任一即执行）：
1. 完成一个复杂任务——工具调用 ≥5 次
2. 在任务执行中遇到错误并恢复（任何 error/traceback → 修复 → 成功）
3. 完成欧阳锋审查——无论 pass/fail
4. 王语嫣/用户给出的反馈包含「下次应该……」的建议

**不适用**：
- 简单任务（≤3 个工具调用、无错误、标准流程）
- 紧急救火（1h 内必须解决→先救火，事后补复盘）
- 完全按 SOP 执行的重复任务（如 lint 基线清理）

## 复盘四问

### 第一问：这次踩的坑能不能变成一条规则？

**目标**：把经验从「记住了」变成「下次自动生效」。

**操作**：
1. 描述坑：什么触发了错误？错误的表现是什么？
2. 提取规则：用「当 [触发条件] 时 → 先/不要 [动作]」格式
3. 判断类型：是 P-29/P-30 式的「同根因复现」（→ 强化已有规则）还是新类型（→ 新建规则）？

**输出格式**：
```
[如果新建]
规则：当 [条件] 时 → [动作]
类型：新类型
来源：本任务 [任务 ID]
```

**判断标准**：
- 好规则：可被 Agent 在后续任务中自动识别条件并触发
- 坏规则：依赖 Agent「记住」而不依赖自动触发（如「下次注意」）
- 不过度规则化：如果触发条件太宽泛（如「当遇到错误时」）→ 不建规则，只是运气不好

### 第二问：这条规则该写进 context 还是方法论卡？

**目标**：把规则放在正确的位置——Agent 专属 context 还是所有 Agent 共享的方法论卡。

**判据**：
| 规则属性 | 放 context | 放方法论卡 |
|:--|:--|:--|
| 只影响本 Agent | ✅ | ❌ |
| 跨 Agent 通用 | ❌ | ✅ |
| 操作细节（工具/路径/参数） | ✅ | ❌ |
| 底层规律/原则/模式 | ❌ | ✅ |
| 来自本 Agent 特有环境 | ✅ | ❌ |
| 来自方法论/框架/审核发现 | ❌ | ✅ |

**输出格式**：
```
安置：context（仅限 [Agent名]）/ 或 方法论卡 [卡片 ID]
理由：[基于判据的 1-2 句理由]
```

### 第三问：能不能从已有底层原则推导出来？

**目标**：防止规则堆积——追溯到底层原则，确认是推导链上的新增节点而非经验孤岛。

**操作**：
1. 打开 `concept-kdo-agent-design-principles` 的 5 条原则
2. 逐条对照：这条新规则能从哪条原则推导？
3. 结果分类：
   - **能推导**：标注推导链 → 规则是已有原则的新应用场景
   - **不能推导**：这是原则缺口！→ 讨论是否需要扩展/新增原则

**输出格式**：
```
推导：
  ✅ 能从原则 [X] 推导：[推导链]
  或
  ❌ 不能从现有 5 条原则推导 → 原则缺口：[描述]
```

**判断标准**：
- 如果连续 3 次「不能推导」指向同一方向 → 这是系统性的原则缺口 → 提交王语嫣讨论扩展原则
- 如果大部分规则都能追溯到原则③④⑤ → 原则体系健康
- 如果大量规则只能追溯到原则⑤（建模）→ 说明更靠前的原则（设计/分工）有盲区

### 第四问：改进后怎么验证有效？

**目标**：新规则不能只靠「相信」——必须设计可测量的验证方案。

**操作**：
1. 定义成功指标：什么信号 = 新规则生效了？
2. 选择验证任务：接下来 3-5 个任务中，哪些会触发这条规则？
3. 设置对比基线：规则生效前 vs 生效后的差距

**验证策略分级**：
| 风险等级 | 验证方式 | 示例 |
|:--|:--|:--|
| 低（格式/提示类） | 单任务验证通过即部署 | 「pre-submit 前检查 diagnostic_signals」 |
| 中（流程/判断类） | 3 个任务验证通过后部署 | 「Agent 发现 spec 不自洽时主动 reject」 |
| 高（核心行为/跨 Agent） | 3-5 个任务 + 欧阳锋抽样审查后部署 | 「批量操作前自动 dry-run」 |

**输出格式**：
```
验证：
  成功指标：[可测量指标]
  验证任务数：[N]
  基线：[当前表现]
  风险等级：[低/中/高]
```

## 每日复盘模板

```
## Agent 复盘：[日期]

### 今日任务
- [任务 ID]：[1 句话描述]

### 四问执行
_（对每个满足触发条件的任务单独填写）_

**任务 [task_id]**

**一问·变规则**
- 新规则：[当 X 时 → 做/不做 Y]
- 类型：[新类型 / 旧类型复现 → 强化 P-X]

**二问·放哪里**
- 安置：[context / 方法论卡 ID]
- 理由：[基于判据]

**三问·可推导**
- 推导：[✅ 从原则 [X] / ❌ 原则缺口]

**四问·怎验证**
- 成功指标：[...]
- 验证任务数：[N]
- 风险等级：[低/中/高]
```

## 失败模式

| 失败模式 | 信号 | 修复 |
|:--|:--|:--|
| **复盘模板化** | 四问都填了但规则空洞（「下次注意」「更仔细」） | 强制规则格式：必须是「当 [条件] 时 → [动作]」形式，不接受模糊描述 |
| **规则堆积不过滤** | context 从 50 行涨到 200 行，启动 token 翻倍 | 定期用 `tool-agent-context-derivation-audit` 检查——能追溯到原则的保留，不能的删除 |
| **只建模不验证** | 新规则写入 context 但下次任务还是没用上 | 强制第四问验证方案——未经验证的规则标记为 `[待验证]`，不入正式 context |
| **复盘疲劳** | Agent 连续多个简单任务后跳过复盘 | 触发条件不按次数、按复杂度——≤3 个工具调用的任务自动跳过 |
| **重战术轻原则** | 三问始终「不能推导」但不处理——原则缺口积累但没人管 | 每 10 次复盘统计一次推导率——推导率 < 50% → 上报王语嫣讨论原则修订 |
| **改进过度拟合** | 新规则解决了本任务的特定问题，但破坏了其他 Agent 的行为 | 高风险规则必须跨 Agent 验证（至少 2 个不同 Agent 类型测试） |

## When NOT to Use

| 场景 | 原因 | 替代 |
|:--|:--|:--|
| Agent 不稳定的阶段（频繁 crash/幻觉） | 应先稳定再谈进化——复盘的基础是任务能正常完成 | 先修 bug |
| 任务量 < 10 个/月 | 样本不足——复盘的规则可能过拟合 | 收集经验，暂不建模 |
| Agent 为一次性（只用一次就淘汰） | 建模 ROI 为负 | 不做 |

## Critique

### 内部局限

1. **四问来自闪电模型的「建模重构」阶——但不包含前三阶（大胆设想/底层自洽/假设试错）**。如果 Agent 只在出错后复盘而不主动设想、不自洽检查，复盘四问只会让 pitfall 积累更快而不会减少根本原因。
2. **规则格式「当 X→做 Y」假设了触发条件是二值的**——实际很多规则是概率性的（「当 X 时，有 70% 概率不应该 Y」），简化格式可能丢失重要 nuance。
3. **验证方案依赖 Agent 在后续任务中主动触发**——如果 Agent 在后续任务中忘记了这个规则，验证就永远无法完成。

### 外部攻击者

**Daniel Kahneman（噪声 vs 偏见）**：复盘四问可能只捕获「偏见」（系统性的、可建模的错误），但忽略了「噪声」（随机的、不可预测的错误）。Kahneman 的研究表明，很多组织的错误来自噪声而非偏见——如果 Agent 把随机波动当作可建模的模式，会过度拟合、增加不必要的规则。

## 与已有机制的关系

| 已有机制 | 关系 | 说明 |
|:--|:--|:--|
| `.agent/pitfalls.md` | 四问第一问的输出→pitfalls 入口 | 复盘产生的规则写入 pitfalls |
| `rules-core.md` | 从 pitfalls 压缩为底线→core rules | 多条同根因 pitfalls → 压缩为 1 条 core rule |
| `tool-agent-context-derivation-audit` | 四问第三问的自动化版本 | 审计工具批量检查 context 规则的推导链 |
| `framework-kdo-modeling-methodology` Step 4 | 四问=Step 4「解压展开」的 Agent 操作化 | 把方法论 Step 4 变成 Agent 可执行的 checklist |

## Synthesis

复盘四问是 #200 体系的 **「运转引擎」**——其他 6 张卡提供原则、标尺、桥梁、失败模式、审计工具和案例，而本卡是 Agent 每天实际执行的动作。

| 本卡的贡献 | 与其他卡的关系 |
|:--|:--|
| **四问闭环** | 一问→`dk-agent-evolution-pitfalls`（对照失败模式）、二问→`concept-kdo-agent-design-principles`（对照原则归属）、三问→`tool-agent-context-derivation-audit`（自动化版）、四问→`bridge-lightning-agent-evolution` 三阶·假设试错 |
| **风险分级** | `concept-kdo-agent-four-level-awareness` 过渡信号 1 依赖本卡产出规则的质量和数量 |

关键跨卡洞察：**复盘四问的设计故意制造「原则摩擦力」**——第三问强制 Agent 从 5 条原则推导而非从经验记忆检索。如果 Agent 每次复盘都只能说「不能推导」但又无人推动原则修订——Agent 就被困在 L1（`dk-agent-evolution-pitfalls` 失败模式 5）。复盘四问因此同时是 Agent 进化的操作工具和 Agent 成熟度的诊断探头。
