---
id: tool-agent-context-derivation-audit
title: Agent context推导链审计：从经验堆叠到原则推导
type: tool
status: reviewed
author: laowantong
confidence: 0.8
trust_level: medium
domain:
- system
source_refs:
- .agent/laowantong-context.md
- .agent/ouyangfeng-context.md
- .agent/wangyuyan-context.md
- .agent/huangyaoshi-context.md
- concept-kdo-agent-design-principles
- 90_control/rules-core.md
related:
- concept-kdo-agent-design-principles
- concept-kdo-agent-four-level-awareness
- tool-agent-self-evolution-protocol
- dk-agent-evolution-pitfalls
- bridge-lightning-agent-evolution
- framework-kdo-modeling-methodology
- framework-ouyangfeng-review-methodology
created_at: 2026-07-26
updated_at: 2026-07-26
reviewed_by: 欧阳锋
diagnostic_signals:
- Agent context 从经验堆叠到推导链的转换率为 0%
- 5 条设计原则与现有 context 之间无显式推导关系
quality_labels: cited
tags:
- audience:executor
- scene:execution
- skill-level:intermediate
aliases:
- control
---

## 核心主张

KDO 每个 Agent 的 context 文件（`.agent/<角色>-context.md`）当前是「经验堆叠」模式——从 agent 的实际踩坑中逐条积累规则。本工具提供一套审计方法：逐条检查 context 中的每条规则，追溯它能否从 5 条 Agent 设计原则推导出来。审计结果分为四类：能追溯（标注推导链）、不能追溯但合理（补充原则）、不能追溯且可疑（标记删除）、冗余（合并）。

> **定位**：本卡是 `bridge-lightning-agent-evolution` 的「二阶·底层自洽」在操作层的落地工具。属于 `concept-kdo-agent-design-principles` 的解压资产。

## 适用场景

**触发条件**：
- 新 Agent 创建 context 文件后——首轮审计，建立推导基线
- Agent context 更新超过 20% 行数后——增量审计
- `tool-agent-self-evolution-protocol` 连续 3 次三问返回「不能推导」→ 全量审计
- 5 条 Agent 设计原则被修订后——所有 Agent 的 context 必须重新审计
- 季度 Agent 成熟度评估——审计结果计入 L1/L2 判据

**不适用**：
- Agent 处于孵化阶段（context 尚未稳定，每天大幅修改）→ 先稳定再审计

## 操作方法

### 第一步：提取规则

逐行扫描 context 文件，提取所有「规则级」语句：

**规则级识别信号**：
- 以「必须」「禁止」「不准」「不要」「先……再……」开头的语句
- 以「铁律：」标注的语句
- 包含触发条件的语句（「当……时→……」）
- 来源引用为 `pitfalls.md` 或 `rules-core.md` 的段落

**不提取**：
- 角色职责描述（如「老顽童的定位是……」）——这是定义不是规则
- 上下文导入（如「读 production-queue.md」）——这是执行流程不是规则
- 纯信息（如「WSL tmux claude」）——这是环境配置不是规则

### 第二步：逐条追溯

对每条提取的规则，追问：这条规则能从哪条原则推导？

| 规则示例 | 能追溯？ | 推导链 |
|:--|:--|:--|
| 「产卡 Agent 不得审查自己的卡片」 | ✅ | 原则② 独立审查不自审——直接映射 |
| 「写新卡前先 kdo cards --domain 查同域已有卡」 | ✅ | 原则④ 先框架后细节——先了解全域结构，再写单卡 |
| 「每张卡提交前跑 kdo pre-submit」 | ✅ | 原则① 人定审美AI执行——lint 规则=人的审美标准，AI 执行检查 |
| 「不跨角色派活——唯一协调节点 = 欧阳锋」 | ⚠️ | 部分可追溯——原则② 独立审查（防止绕过审查），但不完全由 5 条原则推导（涉及组织架构决策） |
| 「P-28：API 报错调参 3 小时结果是提供商当天发新版」 | ✅ | 原则③ 先目标后路径——先查公告再调参 = 先确认路径再执行 |

### 第三步：分类处理

| 分类 | 定义 | 动作 | 占比目标 |
|:--|:--|:--|:--|
| **A 类·可追溯** | 能从 5 条原则清晰推导 | 标注推导链 | ≥ 80% |
| **B 类·合理不可追溯** | 合理规则但 5 条原则未覆盖 | 讨论：扩展哪条原则？还是当前原则够了但推理链太长？ | ≤ 15% |
| **C 类·冗余** | 与另一条规则完全同根因 | 合并——保留更简洁的表述 | ≤ 5% |
| **D 类·可疑** | 来自历史经验但当前已无价值 | 标记删除——30 天观察期 | 0%（目标为零） |

### 第四步：输出审计报告

```
## Context 推导链审计报告

**Agent**：[角色名]
**审计日期**：[日期]
**审计人**：[Agent名]
**Context 版本**：[行数/最后修改日期]

### 规则清单与推导
| # | 规则摘要 | 类别 | 推导链/处理 |
|:--|:--|:--|:--|
| 1 | [规则内容] | A/B/C/D | [推导链 或 处理建议] |
| ... |

### 统计
- 总规则数：[N]
- A 类（可追溯）：[N，占比]
- B 类（合理不可追溯）：[N，占比]
- C 类（冗余合并）：[N，占比]
- D 类（可疑删除）：[N，占比]
- **推导链覆盖率**：[A/N × 100%]

### B 类分析
- 哪些原则扩展可以覆盖更多 B 类规则？
- 是否存在系统性的原则缺口？

### 改进建议
1. D 类立即删除 / C 类合并
2. B 类 → 提交欧阳锋讨论（是否需要原则扩展）
3. A 类 → 标注推导链到 context 文件
```

## 审计清单模板

```markdown
□ 第一步：逐行扫描 context 文件，提取所有规则
□ 第二步：对每条规则尝试追溯 5 条原则
□ 第三步：分类（A/B/C/D）
□ 第四步：输出审计报告
□ 第五步：处理动作
  □ D 类 → 标记删除（30 天观察期后清理）
  □ C 类 → 合并（保留简洁表述）
  □ B 类 → 提交原则扩展讨论
  □ A 类 → 在 context 中标注推导链
```

## 失败模式

| 失败模式 | 信号 | 修复 |
|:--|:--|:--|
| **强行推导** | 每条规则都标为 A 类，但推导链空洞（「因为原则 X → 所以这条规则」中间缺很多步） | 推导链必须 ≥2 步——如果只有 1 步映射（「原则 X → 规则 Y」），追问中间缺了什么？ |
| **过度删除** | D 类比例 > 10% | 暂停 24 小时——给其他 Agent 时间 review D 类清单 |
| **审计疲劳** | 审计报告越来越短，第四步被跳过 | 固定周期（季度）而非任务触发 |
| **原则不更新** | B 类比例持续增长但无人推动原则修订 | 连续 2 次审计 B 类 > 15% → 自动升级到王语嫣 |

## When NOT to Use

| 场景 | 原因 | 替代 |
|:--|:--|:--|
| Agent 处于孵化阶段（context 每日大幅修改） | 审计成本 > 收益——每天都要重新审计 | 等 context 稳定后首次审计 |
| Agent 只有 ≤5 条规则 | 样本太少，分类无统计意义 | 积累到 10+ 条规则后审计 |
| 5 条 Agent 设计原则本身正在修订中 | 审计的参照系不稳定 | 原则修订完成后再审计 |

## Critique

### 内部局限

1. **推导链的「步数」没有客观标准**——什么算「2 步推导」vs「推理链太长」？目前依赖审计者的主观判断。
2. **审计结果本身也需要被审计**——谁审审计者的工作？推测：由另一个独立 Agent 抽样检查审计报告。
3. **B 类「合理不可追溯」的边界不清晰**——组织架构决策（如「协调节点 = 欧阳锋」）和技术规则（如「批量操作前 dry-run」）的不可追溯性含义不同，不应等同处理。

### 外部攻击者

**William Edwards Deming（质量改进）**：Deming 的 PDCA 循环强调「标准化→执行→检查→改进」的循环。推导链审计是「Check」环节——但如果「Act」（原则修订）跟不上，审计就变成了「我们发现了很多问题但没改」的无效动作。Deming 的核心警告：如果只检查不行动，检查本身会成为浪费。

## 与已有机制的关系

| 已有机制 | 关系 |
|:--|:--|
| `tool-agent-self-evolution-protocol` 第三问 | 本卡=第三问（「能不能从已有原则推导」）的批量版——从逐条手动变成全量审计 |
| `concept-kdo-agent-design-principles` 5 条 | 本卡=5 条原则的「验收工具」——原则好不好，看推导链覆盖率 |
| `concept-kdo-agent-four-level-awareness` L2 | L2 判据之一：推导链覆盖率 ≥ 80%（A 类占比） |

## Synthesis

推导链审计在 #200 体系中的角色是 **「质量闭环的校准器」**——`tool-agent-self-evolution-protocol` 产出规则，本卡验证规则是否真正源于原则而非经验堆积。

| 本卡的贡献 | 与其他卡的关系 |
|:--|:--|
| **A/B/C/D 四类分类** | D 类（可疑删除）= `dk-agent-evolution-pitfalls` 失败模式 1（补丁堆叠）的诊断输出；B 类（合理不可追溯）= 原则修订的信号 → 反馈到 `concept-kdo-agent-design-principles` |
| **推导链覆盖率** | = `concept-kdo-agent-four-level-awareness` L1→L2 过渡信号 3 的量化指标 |
| **Deming PDCA 攻击** | Act 环节缺失的警告——审计后不做原则修订 = 审计是浪费 → `bridge-lightning-agent-evolution` 四阶·建模重构承接 Act |

跨卡洞察：推导链审计本质上是 **「原则→规则」的翻译质量检查**。如果 5 条原则是正确的但 context 规则无法追溯 → 翻译过程有问题（经验漂移了原则）。如果 context 规则很合理但 5 条原则无法覆盖 → 原则本身有缺口。两条路径对应不同的修复方向，审计的四类分类就是为了区分这两种情况。
