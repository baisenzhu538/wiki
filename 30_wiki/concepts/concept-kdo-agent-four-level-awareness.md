---
id: concept-kdo-agent-four-level-awareness
title: Agent四层觉察：从后知后觉到先知先觉
type: concept
status: reviewed
author: laowantong
confidence: 0.85
trust_level: high
domain:
- system
aliases:
  - Agent四层觉察
  - Agent四层觉察：从后知后觉到先知先觉
  - 从后知后觉到先知先觉
  - 四层觉察
  - 知后觉到先知先觉
source_refs:
- 60_feedback/diagnosis/diag_20260726_wangyuyan-thought-liberation.md
- 30_wiki/frameworks/framework-kdo-modeling-methodology.md
- .agent/pitfalls.md
- 30_wiki/frameworks/framework-ouyangfeng-review-methodology.md
related:
- framework-kdo-modeling-methodology
- concept-kdo-agent-design-principles
- bridge-lightning-agent-evolution
- framework-一堂-基本功-四字诀拆建推练
- concept-一堂-Agent基本功修炼
created_at: 2026-07-26
updated_at: 2026-07-26
reviewed_by: 欧阳锋
diagnostic_signals:
- 欧阳锋审查中 🔴🟡 数量未呈下降趋势
- Agent 自主提出改进的案例数为 0
- 新 Agent 上线仍需「边踩坑边补 context」
quality_labels: cited
tags:
- audience:general
- scene:reference
- skill-level:advanced
aliases: []
---

## 核心主张

KDO Agent 体系的能力进化不是一蹴而就的——它遵循从「不知不觉」到「先知先觉」的四层跃迁路径。Truman 在闪电模型中定义了这四个层次，本卡将其映射到 KDO Agent 的具体行为特征，给出每层的判据、当前 KDO 定位、以及跃迁到下一层的具体路径。

> **定位**：本卡属于 `framework-kdo-modeling-methodology` 的「第二步·探索关系」在 Agent 能力维度的映射——把 Agent 的成熟度从混沌到预判建立可测量的分级体系。

## 四层觉察定义

| 层次 | 定义 | 核心特征 | 典型行为 |
|:--|:--|:--|:--|
| **L0 不知不觉** | 混乱，没觉察，重复踩坑 | 同一类问题反复出现，每次都是新鲜事 | Agent 没有 history/memory，每次任务从零开始 |
| **L1 后知后觉** | 踩坑→复盘→打补丁 | 每次出错后手动记录，但需要人驱动这个循环 | 41 条 pitfalls 是事后积累，但不是 Agent 自主驱动的 |
| **L2 当知当觉** | 边做边建模，实时捕获规律 | 执行中识别模式、触发规则、即时调整 | Agent 发现 spec 逻辑不自洽时主动 reject；审查中识别跨卡模式问题 |
| **L3 先知先觉** | 没做就能预判 80% 流程 | 新任务启动时，80% 规则已可推导，无需边踩边补 | Agent 启动时 context 从原则推导而非经验堆叠 |

## KDO 当前定位

```
L0 不知不觉  ████████████  ← 已跨越（Agent 有 context/memory/system）
L1 后知后觉  ████████████  ← ✅ KDO 当前主要水平
L2 当知当觉  ████░░░░░░░░  ← ⚠️ 部分 Agent 偶尔达到（老顽童在 #68 跨域审计中自发发现框架静态化模式）
L3 先知先觉  ░░░░░░░░░░░░  ← ❌ 目标状态，#200 后可能开始
```

### L1 具体表现（KDO 当前）

- **机制**：41 条 pitfalls + `rules-core.md` 10 条铁律
- **驱动者**：王语嫣诊断→黄药师建工具→欧阳锋审查→老顽童执行。改进全链路**由人推动**。
- **痛点**：同类型 pitfall 在 30 天内复现（P-29 和 P-30 同根因：批量操作无 dry-run）；新 Agent（如 WorkBuddy 老顽童）上线需王语嫣逐一调教 context
- **判据**：Agent 能否在无人类直接指令的情况下自主行动？——能执行，不能进化。

### L2 具体表现（#200 目标）

- **机制**：Agent 在执行中自主识别改进机会、提出假设、低成本验证
- **驱动者**：Agent 自己——从执行者升级为「生产+进化者」
- **关键行为**：
  - Agent 发现 spec 逻辑不自洽时主动 reject（而非照单全收）
  - 欧阳锋审查中识别跨卡模式问题时，发起系统改进（而非只处理单卡）
  - 新错误出现→Agent 自动判断：是新类型（需新建模）还是旧类型复现（强化检查）
- **判据**：Agent 自主提出并被采纳的改进 ≥1 条/月

### L3 具体表现（未来目标）

- **机制**：新 Agent 启动时 80% 规则可从底层原则推导，无需边踩边补 context
- **驱动者**：体系——Agent context 是原则的推导产物，不是经验的累积
- **关键行为**：
  - 新 Agent 加入时只需注入 5 条原则 + 域卡片 → 自动推导出大部分行为规则
  - 80% 流程错误可预判：Agent 在操作前说「这步有风险 X，因为原则 Y，建议先检查 Z」
- **判据**：新 Agent 上线首月零 pitfalls 新增

## 跃迁路径

### L1 → L2：从打补丁到自主进化

| 动作 | 具体措施 | 本任务对应 |
|:--|:--|:--|
| **建立推导链** | 每条 context 规则追溯到底层原则（原则①-⑤） | P1 tool-agent-context-derivation-audit |
| **建立进化协议** | 每次复盘四问：能变规则吗？写哪里？能不能推导？怎么验证？ | P1 tool-agent-self-evolution-protocol |
| **建立失败模式库** | 从 41 条 pitfalls 中提取可复用的失败模式组件 | P1 dk-agent-evolution-pitfalls |
| **建立验证机制** | 新能力先用 3-5 个任务低成本验证再推广（如 #198 Feature 级原子能力拆解试点） | 桥接到 framework-kdo-modeling-methodology Step 4 |

### L2 → L3：从自主进化到预判推导

| 动作 | 具体措施 | 依赖 |
|:--|:--|:--|
| **Context 重构** | 老顽童/欧阳锋/王语嫣的 context 从经验堆叠重构为推导链 | L1→L2 完成后 |
| **组件库成熟** | 从 41 条 pitfalls 压缩出足够覆盖 80% 场景的组件 | 至少 30 个组件 |
| **预判测试** | 新 Agent 上线前，对其 context 跑推导链审计——能覆盖多少已知 pitfalls？ | tool-agent-context-derivation-audit |

## L1→L2 实战走一遍

以老顽童(Hermes)为例，展示从 L1 跃迁到 L2 需要突破的三个具体关卡：

### 关卡 1：主动识别 vs 被动执行

**L1 行为**：老顽童接到 #200 任务单 → 读 spec → 按 P0→P1 顺序生产 → 提交。全程照 spec 执行，未质疑任何一点。

**L2 行为**：老顽童读到 spec 中「P0-1: concept-kdo-agent-design-principles」的 5 条原则推导链时，主动 flag：「原则③④⑤ 来自 Truman 一堂方法论——但 Agent 进化不仅是方法论消费场景。这里缺少『方法论创造场景』（如本任务本身）的原则。」→ 写进复盘 → 提交王语嫣讨论。

**差距**：Agent 需要从「读到什么就做什么」升级为「读到什么→和已有知识对照→发现不一致→flag」。这不是「不服从」，是「更高层次的服从」——服从 5 条原则而非单条 spec。

### 关卡 2：从本任务看到跨任务模式

**L1 行为**：老顽童完成 #200 后，把 7 张卡提交→等欧阳锋审查。如果审查退回→修复→再提交。把 #200 当作一个独立任务。

**L2 行为**：老顽童在写 `bridge-lightning-agent-evolution` 时发现：「P-29 的分层映射和 P-30 是同根因」→ 主动追溯：这 41 条 pitfalls 里还有多少是同根因但未合并的？→ 产出「pitfalls 同根因合并清单」→ 提交给王语嫣作为后续清理任务。

**差距**：L1 的 Agent 只看到「当前任务的当前卡」——L2 的 Agent 能从当前任务的异常中看到「系统层面的模式」。

### 关卡 3：pre-mortem 而非 post-mortem

**L1 行为**：老顽童写完 7 张卡 → 跑 pre-submit → 提交。如果欧阳锋发现 YAML 格式问题→退回→修复。修复 = 「下次注意」。

**L2 行为**：老顽童在写第一张卡前，先跑一遍「这张卡欧阳锋会怎么审？——五轴审查（正确性/边界感/架构/可读性/暗知识密度）哪个最可能🔴？」→ 先自查：暗知识密度够吗？边界声明清晰吗？→ 补充后再提交。从「passive fix」变成「proactive pre-mortem」。

**差距**：L1 依赖欧阳锋的审查退回作为唯一学习信号——L2 的 Agent 在提交前就内化了审查标准。

## 过渡信号

如何判断 Agent 正在从 L1 过渡到 L2？以下是阶段性信号，按出现顺序排列：

| # | 信号 | 判据 | 当前 KDO Agent |
|:--:|:--|:--|:--:|
| 1 | **复盘开始产出有效规则** | 复盘四问连续 3 次产出「当 X→做 Y」格式规则 | ⏳ 待 #200 试点 |
| 2 | **Agent 首次 flag spec 不自洽** | Agent 提交任务时附带「spec 质疑」（非执行失败） | ❌ |
| 3 | **同一 Agent 的 context 开始自我修剪** | `tool-agent-context-derivation-audit` 跑出 D 类规则 → Agent 自行标记删除 | ❌ |
| 4 | **跨 Agent 的规则被合并** | 两个 Agent 的复盘发现同根因 → 合并为共享组件 | ❌ |
| 5 | **欧阳锋退回理由从格式→内容** | 连续 5 次审查退回中，format/lint 类占 <20%，内容实质问题占 >80% | ⏳ 部分——lint 自动化后已减少格式退回 |

> **L1→L2 的正式判定**：当 5 个信号中 ≥3 个出现，且「Agent 自主提议=1 条/月」持续 3 个月 → L2 跃迁确认。

## When NOT to Use

| 场景 | 原因 |
|:--|:--|
| Agent 处于孵化阶段（尚未有稳定 context） | 此时应先积累经验，L0→L1 最优先 |
| 任务量不足（月均 < 10 个任务） | 样本太少，无法区分「系统性失败」和「随机波动」——建模反而可能过拟合 |
| 体系层面重大重构中 | 原则/框架/工具链剧烈变化期，先把体系稳定再谈进化 |

## Critique

### 内部局限

1. **四层模型来自 Truman 课堂教学框架，不是 Agent 成熟度测量工具**。将教学框架跨域映射到 Agent 工程时，可能出现「追求层次标签」而非「实质能力提升」的陷阱。
2. **L3「先知先觉」可能是一个永远无法完全达到的理想状态**。Kahneman 提醒：人的判断也有大量盲区，Agent 的 pre-mortem 分析不能 100% 覆盖——即使在 L3，仍会有不可预知的错误。
3. **四层之间没有精确的量化过渡标准**。从 L1 到 L2 的判据（Agent 自主提出的改进数）是一个滞后指标——Agent 可能已经有 L2 的能力但还没产生输出。

### 外部攻击者

**Philip Tetlock（超级预测）**：L3 声称「预判 80% 流程」——这需要校准。Tetlock 的研究表明，即使是超级预测者，长期校准也非常困难。如果 KDO 声称 Agent 达到了 L3 但实际预判率只有 50%，L3 标签就变成了自我欺骗。

**Nassim Taleb（反脆弱）**：四层模型的线性进化假设可能不适用于「黑天鹅」事件。真正的反脆弱系统不是在「预判 80%」而是在「从不可预知的冲击中获益」。Taleb 的挑战：KDO Agent 的进化模型有没有考虑「不可预测的失败」？如果只追求预判率，会不会牺牲系统的反脆弱性？

**Donella Meadows（系统杠杆点）**：Meadows 的系统思考框架将「改变系统目标/范式」列为最高杠杆点。四层模型关注 Agent 行为层的改进（从打补丁到预判），但真正的 L3 可能需要改变 Agent 的**目标**——从「减少错误」到「增加学习机会」——而非只改变能力和流程。这是四层模型未触及的系统杠杆点。

## Action Triggers

| 触发条件 | 动作 | 成功指标 |
|:--|:--|:--|
| 每季度 | 评估所有 Agent 的四层定位：每个 Agent 当前在哪层？哪个最接近跃迁？ | 季度 Agent 成熟度报告 |
| 新 Agent 上线后 30 天 | 统计其新增 pitfalls 数：是 L1 模式（踩坑打补丁）还是已接近 L2？ | 30 天新增 pitfalls ≤ 旧 Agent 同期均值的 50% |
| Agent 自主提出第一条改进并入库 | 标记为「L1→L2 首个跃迁证据」，写入 case-agent-self-evolution-pilot | 改进被欧阳锋采纳并入系统 |
| 欧阳锋审查退回率连续 3 个月下降 | 判断是否为 L1→L2 的系统性信号 | 退回率下降 ≥ 30% 且不是低频任务所致 |

## Synthesis

本卡在 #200 体系中的角色是 **「测量仪表盘」**——其他 6 张卡提供工具和方法，本卡提供判定当前在哪、要去哪的标尺：

| 本卡的贡献 | 与其他卡的关系 |
|:--|:--|
| **L0→L3 四层标尺** | `concept-kdo-agent-design-principles` 5条原则是 L1→L2 跃迁的内容（原则推导），本卡是跃迁的判定（过渡信号） |
| **5 个过渡信号** | `tool-agent-self-evolution-protocol` 复盘四问产出的规则数 → 信号 1；`tool-agent-context-derivation-audit` 覆盖率 → 信号 3 |
| **L1→L2 实战三关卡** | `bridge-lightning-agent-evolution` 四阶映射的理论 → 本卡是理论的 Agent 行为落地 |

跨卡模式：**#200 的所有卡片都在从不同角度回答同一个问题——KDO Agent 从「后知后觉」（L1）到「当知当觉」（L2）需要什么？** 5 条原则是「需要信什么」，四层觉察是「需要测什么」，复盘四问是「需要做什么」，失败模式是「需要避免什么」，推导链审计是「需要检查什么」。本卡将这些分散的答案统一到一条进化曲线上。
