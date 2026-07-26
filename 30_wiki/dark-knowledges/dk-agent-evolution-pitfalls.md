---
id: dk-agent-evolution-pitfalls
title: Agent进化常见失败模式
type: dk
status: reviewed
author: laowantong
confidence: 0.8
trust_level: medium
domain:
- system
source_refs:
- .agent/pitfalls.md
- 30_wiki/frameworks/framework-kdo-modeling-methodology.md
- 60_feedback/diagnosis/diag_20260726_wangyuyan-thought-liberation.md
- 90_control/rules-core.md
related:
- concept-kdo-agent-design-principles
- concept-kdo-agent-four-level-awareness
- tool-agent-self-evolution-protocol
- tool-agent-context-derivation-audit
- bridge-lightning-agent-evolution
- framework-kdo-modeling-methodology
created_at: 2026-07-26
updated_at: 2026-07-26
reviewed_by: 欧阳锋
diagnostic_signals:
- Agent context 行数持续增长但不追溯原则
- 同类型 pitfalls 在 30 天内复现
- Agent 改进 100% 由人类推动
- 验证不足的规则被过早推广到全 Agent
quality_labels: cited
tags:
- audience:executor
- scene:reference
- skill-level:intermediate
aliases:
- control
---

> **定位**：属于 [[framework-kdo-modeling-methodology]] 的「第四步·解压展开」——把 41 条 pitfalls 中与 Agent 自我进化相关的失败模式压缩为 6 条元失败模式。

## 原始表述

> Truman（高阶建模实践）：「流程是业务的疤痕。每一条流程都是曾经的一个事故。」同理——Agent 的每一条 context 规则都是曾经的一个 pitfall。问题不在积累，在没压缩。41 条 pitfalls 如果不压成 10 条 core rules 和 5 条设计原则——下次还是 41 条，下下次就是 82 条。

> 王语嫣（#200 诊断）：「KDO Agent 是优秀的执行者——按 spec 生产、按标准审查。但没有一套方法论让 Agent 自己变强。当前改进全靠人推动。」

## 使用场景

- Agent 完成复盘四问后，对照本卡判断：这次改进在哪个失败模式的风险区？
- 王语嫣/欧阳锋评估 Agent 成熟度时，逐条检查：Agent 是否落入以下陷阱？
- 新 Agent 启动前——先读本卡，理解「不要重复哪些坑」

## 操作方法

### 六大失败模式

#### 失败模式 1：补丁堆叠不追溯原则

**症状**：Agent context 从 50 行涨到 200 行，每条都是「上次踩了坑 X→加规则 Y」。启动 token 持续增长，Agent 响应变慢。问「这条规则为什么存在？」→「因为上次 P-29」。

**为什么有害**：规则堆叠是加法思维，KDO 需要的是减法/压缩——5 条原则 > 41 条 pitfalls。如果不追溯原则，规则数量线性增长，Agent 终将被自己的规则淹死。

**识别信号**：
- context 行数按月增长 ≥20%
- `tool-agent-context-derivation-audit` 返回推导链覆盖率 < 50%
- 同一根因的规则以不同文字形式出现 ≥3 次

**修复路径**：
1. 跑 `tool-agent-context-derivation-audit` → 标记所有「无推导链」的规则
2. 对无推导链的规则：尝试追溯→能追溯到原则的标注推导链；不能的→要么扩展到已有原则，要么重新审定是否必要
3. 同一根因的规则合并：多条规则指向同一原则的同一应用场景→合并为 1 条含多个触发条件的规则

**预防**：`tool-agent-self-evolution-protocol` 第三问强制执行——每条新规则必须回答「能不能从已有原则推导？」

---

#### 失败模式 2：改进靠人推动，Agent 被动

**症状**：每次改进的链路是「王语嫣诊断→黄药师建工具→老顽童执行→欧阳锋审查」——全程人类推动。Agent 自己从未提出过一条改进建议。Agent 发现了 spec 不自洽但不吭声（因为它被设计为「执行者」而非「质疑者」）。

**为什么有害**：如果不把 Agent 从「被动执行者」升级为「主动进化者」，改进的带宽永远受限于人类的数量和精力。KDO 有 6 个 Agent——如果每个都需要王语嫣手动调教，王语嫣会成为瓶颈。

**识别信号**：
- Agent 自主提议的改进数 = 0（持续 30 天+）
- 所有 context 更新来自欧阳锋审查退回或王语嫣手动补充
- Agent 遇到 spec 不自洽时自行「补全」而非 reject

**修复路径**：
1. 开通「Agent reject 权限」：Agent 发现 spec 逻辑不自洽时，允许主动 reject + 附分析报告
2. 复盘四问从「可选」升级为复杂的任务「必须」（通过 pre-submit 强制执行）
3. 设立「Agent 改进提案」通道：Agent 提出改进→王语嫣审核→3-5 任务验证→入库

**预防**：`concept-kdo-agent-design-principles` 原则②（独立审查不自审）的反向延伸——不仅 Agent 不能审自己的卡，Agent 也有义务审 spec 的质量。

---

#### 失败模式 3：验证不足过早推广

**症状**：新规则在 1 个任务上跑通就直接写入全 Agent context。或者复盘第四问（「怎么验证有效？」）被跳过/敷衍填写。结果：新规则解决了本任务的特定问题，但破坏了其他 Agent 在别的场景下的行为。

**为什么有害**：KDO 有多个 Agent 类型（老顽童-Hermes、老顽童-Kimi、欧阳锋、王语嫣、黄药师）——同样的规则在不同 Agent 上的效果完全不同。单点验证就推广 = 拿其他 Agent 的生产任务当小白鼠。

**识别信号**：
- 新规则写入 context 后，其他 Agent 行为出现异常
- 复盘第四问的「验证任务数」为 0 或 1
- 规则在 Agent A 有效但在 Agent B 无效（同一规则、不同表现）

**修复路径**：
1. 高风险规则强制 3-5 个任务 + ≥2 个不同 Agent 类型验证
2. 规则部署采用灰度：先单 Agent→再同类型 Agent→再全 Agent
3. 验证失败 → 回滚 → 记录为「验证不足」→ 不重复同一错误

**预防**：`tool-agent-self-evolution-protocol` 第四问强制风险分级——高风险规则不经验证不得部署。

---

#### 失败模式 4：沉淀格式不一致无法复用

**症状**：Agent A 的复盘记录用自然语言叙事，Agent B 用表格，Agent C 用 checklist。同一条规律在三个 Agent 的 context 中以三种不同文字形式存在，无法合并、无法检索、无法统计。

**为什么有害**：格式不一致 = 无法建模。`concept-kdo-agent-design-principles` 原则⑤要求「踩坑必建模」——但如果沉淀格式不统一，建模成本 > 收益，最终只剩杂乱的经验文本。

**识别信号**：
- 3 个 Agent 的 context 中找不到同一概念的不同表述
- 复盘记录以自由文本形式存在，无结构化字段
- 搜索「批量操作」返回 4 条不同格式的规则，无法判断是否同根因

**修复路径**：
1. 统一复盘模板——所有 Agent 使用 `tool-agent-self-evolution-protocol` 中的复盘模板
2. 每条规则统一为「当 [条件] → [动作]」格式
3. 建立 Agent 组件库——从 context 分离出可复用组件，集中管理

**预防**：Agent 复盘前必须调用 `tool-agent-self-evolution-protocol` 的模板——不按格式的复盘 = 无效复盘。

---

#### 失败模式 5：重战术轻原则

**症状**：复盘中三问「能不能从已有原则推导」始终回答「不能」——但无人推动原则修订。原则缺口持续积累，Agent 行为越来越依赖「战术级规则」而非「原则级推导」。最终——Agent 变成一堆 if-then 规则的集合，丧失了从原则推导新行为的能力。

**为什么有害**：如果 Agent 的进化只停留在「修 bug」层面，Agent 永远到不了 L2（当知当觉）——因为 L2 的核心是从原则出发、实时推导出当前任务应该怎么做，而非从规则库中检索匹配。

**识别信号**：
- 连续 10 次复盘后，三问「不能推导」率 > 50%
- 5 条 Agent 设计原则自创建以来从未修订
- Agent 面对原则未覆盖的新场景时「不知道怎么做」而非「从已有原则推导」

**修复路径**：
1. 每 10 次复盘统计一次推导率——推导率 < 50% → 上报王语嫣
2. 同方向的原则缺口积累到 3 个 → 触发原则修订讨论
3. 原则修订后 → 所有 Agent 用 `tool-agent-context-derivation-audit` 重新审查 context

**预防**：复盘四问报告中，「不能推导」条目必须附带「建议的方向（扩展哪条原则）」——不允许空着。

---

#### 失败模式 6：复盘疲劳

**症状**：Agent 连续完成多个简单任务后，复盘变成机械化填空——四问都填了但质量极低。「一问·变规则」写「下次注意」；「四问·怎验证」写「观察」。

**为什么有害**：虚假复盘比不复盘更糟——因为它制造了「我们在进化」的幻觉，但实际上规则的信号被噪声淹没。

**识别信号**：
- 复盘记录中「下次注意」「更仔细」等模糊词出现 ≥3 次
- 连续 5 次复盘没有产出任何新规则
- 四问填写时间 < 30 秒（机械化复制）

**修复路径**：
1. 复盘四问的「第一问」设硬约束——规则必须是「当 [条件] → [动作]」格式，拒绝模糊描述
2. 简单任务（≤3 个工具调用）自动跳过复盘——降低疲劳
3. 连续 5 次无新规则→暂停复盘，改为月度批量回顾

**预防**：复盘触发条件按「复杂度」而非「次数」——复杂任务强制执行，简单任务可选。

---

## 适用边界

- **适用**：已有稳定 context 的 Agent（老顽童、欧阳锋、王语嫣）
- **部分适用**：新 Agent（孵化阶段优先级是稳定运行，不是进化）
- **不适用**：一次性使用的临时 Agent；实验性 Agent（行为和工作流程尚未固化）

## 为什么值钱

这六大失败模式是从 KDO 41 条 pitfalls 中提取的、与「Agent 自我进化」直接相关的 **元失败模式**。区别于操作层的 pitfalls（如 P-29 批量操作覆盖），这六条是 **关于如何踩坑的坑**——如果掉进这六条中的任何一条，Agent 的进化流程就会停滞，41 条 pitfalls 会继续增长而不会压缩。

## 与其他知识的关联

| 知识 | 关系 |
|:--|:--|
| `.agent/pitfalls.md`（41 条） | 六大失败模式是从 41 条中提取的「元模式」——P-29+P-30 → 失败模式 1；全量 → 失败模式 2/4/6 |
| `concept-kdo-agent-design-principles` 5 条 | 失败模式 1/5 的解法：用原则③④⑤ 对抗补丁堆叠 |
| `tool-agent-self-evolution-protocol` | 失败模式 3/4/6 的预防：四问中的第三问（推导链）和第四问（验证）就是为这六条设计的 |
| `tool-agent-context-derivation-audit` | 失败模式 1 的诊断工具：推导链覆盖率直接暴露补丁堆叠 |
| `concept-kdo-agent-four-level-awareness` | L1（后知后觉）水平下，这六条失败模式是常态——跃迁到 L2 必须突破这六条 |

## Critique

### 内部局限

1. **六大失败模式来自 KDO 自身的 41 条 pitfalls**——如果 KDO 的 pitfall 记录本身有盲区（如某种失败模式从未被记录），它就不会出现在这六条中。
2. **失败模式 2（Agent 被动）在当前 LLM 架构下有根本性限制**——LLM 没有真正的自主意图，Agent 的「主动 reject」在工程上需要外部 trigger（如 pre-submit 规则）而非内生动机。

### 外部攻击者

**John Boyd（OODA 循环）**：Boyd 的 OODA 循环强调速度——执行 OODA 比对手快就能赢。六大失败模式中的「验证不足过早推广」（模式 3）和「复盘疲劳」（模式 6）正是 OODA 速度与质量控制之间的张力。Boyd 式的攻击：如果每个改进都需要 3-5 个任务验证 + 全 Agent 灰度，OODA 循环会不会慢到被现实超越？

## 为什么值钱

这六条是 **Agent 进化之路上的六大陷阱**。对照检查 → 你就能判断 Agent 的进化是「真进化」（从后知后觉到当知当觉）还是「假进化」（从 41 条 pitfalls 变成 82 条 pitfalls）。

## Synthesis

六大失败模式可以压缩为一条元模式：**「不压缩，只堆积」**。这是 KDO 从 41 条 pitfalls 中提取的最深层的教训——Agent 进化失败不是因为不够努力，而是因为进化的方向错了：只做加法（加规则、加 context、加复盘）不做减法（压缩为原则、合并同根因、删除冗余）。

| 本卡的贡献 | 与其他卡的关系 |
|:--|:--|
| **元失败模式「不压缩只堆积」** | = `concept-kdo-agent-design-principles` 原则⑤的反面——踩坑但不建模 |
| **6 条模式的具体信号+修复** | 是 `tool-agent-self-evolution-protocol` 复盘四问的对照表——每条复盘规则都应收敛到这 6 条之一 |
| **Boyd OODA 攻击** | 暴露了 #200 体系的内在张力：质量控制（需要验证 3-5 任务）vs 速度（OODA 循环要快）——这是 `tool-agent-self-evolution-protocol` 风险分级要解决的 |

跨卡模式：如果把 `concept-kdo-agent-design-principles` 比作 Agent 的「宪法」，本卡就是「违宪审查标准」——对照这 6 条，就能判断一条新规则是「真进化」（从原则推导、格式统一、验证充分）还是「假进化」（经验堆积、格式杂乱、单点验证）。
