---


id: sk-ai-system-redundancy
title: 技能：系统冗余度快速检查清单
type: tool
status: enriched
domain:
  - ai-collaboration
  - yitang- ai-collaboration
source_person: 水水
source_context: 拆书会《偶然》分享，2026-06
source_refs:
- 10_raw/sources/src_20260614_fb753683-世界发展-偶然与必然讨论.md
wiki_refs:
- '[[sk-ai-purpose-bias-check]]'
- '[[tool-checklist-cheatsheet-modeling]]'
definition_of_done:
- 操作步骤清晰可执行
- 适用场景有正反例
- 工具要求明确
tags:
- '#method/prompt-engineering'
- '#domain/ai-saas'
- '#method/workflow'
created_at: '2026-06-06'
updated_at: '2026-06-18'
tools_required:
- 文档编辑工具（Notion / Word / 飞书文档等）
- 数据管理工具（Notion / Airtable 等）
prerequisite_skills: []
related:
  - '[[tool-ai-narrative-test]]'
  - '[[tool-ai-prd-for-ai]]'
  - '[[tool-ai-purpose-bias-check]]'
  - '[[sk-ai-old-small-checklist]]'
  - '[[tool-ai-system-redundancy]]'
  - '[[sk-ai-purpose-bias-check]]'
  - '[[tool-checklist-cheatsheet-modeling]]'
author: unknown
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- 检查时被当作"增加成本"而非"降低崩溃风险"的保险
- 只检查一次后束之高阁，没有定期复盘机制

---
# 技能：系统冗余度快速检查清单

## 用一句话讲清楚

在方案、项目或个人职业系统的设计阶段，用六项检查快速识别单点故障和脆弱依赖，通过预留冗余来提升抗意外能力，而不是追求虚假的确定性。

## 核心要点

复杂系统具有自组织临界性，微小扰动可能引发灾难性崩溃。留有冗余比追求虚假确定性更重要。

### 检查维度

| 检查项 | 问题 | 无冗余的信号 | 应对动作 |
|---|---|---|---|
| **单点故障** | 如果 X 失效，整个系统还能运行吗？ | 某个关键环节断掉后全盘均输 | 增加备份方案或备选路径 |
| **人员依赖** | 如果某个人离开，这个能力还存在吗？ | 只有 1 个人会做某件事 | 文档化 SOP，培养后备 |
| **资源依赖** | 如果主要资源源失效，有替代吗？ | 只有 1 个供应商/渠道/客户 | 发展第二供应商/渠道 |
| **时间缓冲** | 如果计划被打断，有几天的缓冲期？ | 每天都在赶 deadline，没有缓冲 | 预留 30% 的空闲时间作为缓冲 |
| **信息冗余** | 关键信息是否只有一份？ | 关键数据/文档只存在 1 个地方 | 定期备份，少次多地存储 |
| **能力冗余** | 如果你的主要技能过时了，有备选技能吗？ | 所有收入都依赖单一技能 | 发展跨领域能力或副业 |

### 使用流程

1. 选择一个正在设计的系统或方案（产品、项目、个人职业规划均可）。
2. 逐条检查清单，标记已有冗余或缺冗余项。
3. 缺冗余项优先级排序：先补"单点故障"和"人员依赖"（危险最高）。
4. 每月复盘时重新跑一遍这个清单。

## 边界

- **适用**：方案/系统设计、职业规划、团队管理、产品容错机制设计。
- **不适用**：追求最优效率且无法承担任何冗余成本的场景；已经高度标准化、低风险的重复流程。
- **注意**：冗余是降低崩溃概率，不是消除所有风险；过度冗余会导致成本失控。

## 失败模式 table

| 失败模式 | 触发条件 | 后果 | 预防/修复 |
|---|---|---|---|
| 步骤跳过或省略 | 急于出结论，未逐项检查 | 遗漏关键脆弱点，系统仍暴露于单点故障 | 严格按步骤执行，每步必须验收后进入下一步 |
| 单人操作忽视团队协作 | 仅由个人填写，未与执行方对齐 | 成果难推广，清单流于形式 | 步骤 1 就征求团队意见 |
| 把冗余当浪费 | 只算直接成本，忽视崩溃损失 | 该加的备份没加 | 用"失效成本 × 发生概率"来评估冗余价值 |
| 检查一次后不再更新 | 环境变化但清单未同步 | 新的单点故障无法被识别 | 设定每月/每季度复盘日历提醒 |

## 行动 Checklist

- [ ] 明确要检查的系统/方案边界
- [ ] 逐项走完六项冗余检查
- [ ] 标记"无冗余"项并评估风险等级
- [ ] 优先处理"单点故障"和"人员依赖"
- [ ] 为每项缺失制定 30 天内可执行的补强动作
- [ ] 把清单和结果同步给相关团队成员
- [ ] 设置下一次复盘时间（建议每月）

## 相关卡/互链

- [[sk-ai-purpose-bias-check]]：在定义系统目标时检查是否存在目的偏误
- [[tool-checklist-cheatsheet-modeling]]：把检查清单沉淀为可复用的 cheatsheet

## 来源

- 水水，拆书会《偶然》分享，2026-06

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
