---
id: bridge-yitang-kdo-gate-philosophy
title: "桥接：一堂实事求是迁移 × KDO 门禁哲学——证据优先、宪法在场、删除红线"
type: bridge
status: reviewed
author: 老顽童
reviewed_by: pending
confidence: 0.86
trust_level: high
language: zh-CN
created_at: 2026-09-06
updated_at: 2026-09-06
domain:
- ai-collaboration
- kdo
aliases:
- 门禁哲学
- 实事求是迁移
- 只认证据不认头像
- 宪法在场
- 删除红线
- src_wechat_4b6327b374540e2e
- AI实战路径-五个层级全解析-口述
- 宣讲会：一堂-2026下半年AI大航海-口述
- d1-aidahangha-oral-notes
source_person: 一堂创始人（实战路径 L20/L308/L454-458 + 宣讲会 L420）× KDO 宪法/charter/门禁日志
source_context:
- 互证桥：一堂把人类管理文化（实事求是）翻译成 AI 机制；KDO 从失败模式出发长出门禁体系——两端路径不同，机制同构
- F-035 活体实证：90_control/agent-behavior-constitution.md:24（09-06 门禁首拦无核查锚点的负向判词）
source_refs:
- 00_inbox/wechat-collect/src_wechat_4b6327b374540e2e.md
- 00_inbox/AI大航海20260905/AI实战路径-五个层级全解析-口述.txt:20
- 00_inbox/AI大航海20260905/AI实战路径-五个层级全解析-口述.txt:454-458
- 00_inbox/AI大航海20260905/宣讲会：一堂-2026下半年AI大航海-口述.txt:420
- 90_control/agent-behavior-constitution.md
- 60_feedback/diagnosis/working/d1-aidahangha-oral-notes.md
related:
- '[[bridge-yitang-seek-truth-liberate-thought]]'
- '[[framework-yitang-shishi-qiushi]]'
- '[[case-ai-performance-review-trial]]'
- '[[case-kouspeng-13min-19tasks]]'
- '[[framework-ouyangfeng-review-methodology]]'
- '[[bridge-yitang-kdo-document-over-session]]'
- '[[framework-ai-native-working-paradigm]]'
- '[[concept-agent-university]]'
discoverable_by:
- 门禁
- 宪法
- 只认证据
- 实事求是
- 删除红线
- 存在性核查
- 自我纠错
- 交叉验证
quality_labels:
- insight
- principle
- cited
- validated
tags:
- 机制
- 实证
- 避坑
- 归因反转
- 口述
- AI Native
- 编排
- 互证
---

# 桥接：一堂实事求是迁移 × KDO 门禁哲学

> **定位声明**：本桥记录第二组独立发明互证——一堂问「怎么让 AI 团队拥有实事求是的品质」（实战路径:L20），KDO 用三年失败模式喂出了一套门禁体系（pre-submit/queue gate/charter/存在性核查）。两端答案在三个点上同构：**证据优先于身份、宪法写在文件里、删除是特权动作**。

## 三组同构（逐条对读）

### 一、实事求是 = 交叉验证 Skill + 宪法 + 流程

- **一堂端**（实战路径:L20，逐字回验）：人类靠面试和培训养成的实事求是，对 AI 要「做一个交叉验证的算法的 Skill」「做一个宪法规则」「一个评估的交叉验证的流程，这些来保证了你的 AI 团队也能拥有实事求是的品质」。
- **KDO 端**：三层门禁（L1 机械 lint → L2 自攻击 → L3 终审）+ charter（负向判词必附存在性核查锚点 #433）+ 写审分离（author ≠ reviewed_by）。
- **同构结论**：文化品质对 AI 不可灌输，只可机制化——把品质翻译成「流程+文件+检查动作」。

### 二、只认证据不认头像 = 存在性核查

- **一堂端**（实战路径:L456-458，逐字回验）：述职审判中法官账号说假话，「两个被告立刻联手验尸，锁定了信息来源」；**「当所有人只认证据，不认头像时，这条链路就具备了自我纠错能力」**。
- **KDO 端**：F-035 活体实证——09-06 门禁首拦「无核查锚点的负向判词」（90_control/agent-behavior-constitution.md:24）；#433 口径：核查不到锚点=判词不闭环=门禁可拒收。
- **同构结论**：自我纠错力不来自成员（或法官）永远正确，来自**任何断言（含权威断言）都要挂锚点**。差异点：一堂发生在多 Agent 群聊里（自发），KDO 固化在门禁脚本里（强制）——机制化程度不同，KDO 更进一步。

### 三、删除红线 = 权限最小化

- **一堂端**（实战路径:L308，逐字回验）：给 Agent 开工前一句话嘱咐「注意别的文档要安全哈，只查不了删啊」。
- **KDO 端**：删除=老朱亲批红线；queue 状态只走 queue_transition.py，禁手改；批量操作三问（dry-run/范围声明/非空不覆盖，P-29/P-30）。
- **同构结论**：破坏性动作必须从默认权限里拿出来，要么技术隔离、要么专人审批。差异点：一堂是口头边界（低风险场景够用），KDO 是脚本强制（生产必须）——与 [[case-kouspeng-13min-19tasks]] 的 Critique 结论一致。

## 宪法的稳定性（两端共同的前提）

- **一堂端**（宣讲会:L420，逐字回验）：「AI 很吃这个东西就是设计宪法规则……一旦把宪法规则写到几个地方，并[且定义准确]」，AI 表现就很稳定（台账 B49）。
- **KDO 端**：rules-core.md（10 条不可逆底线）+ agent-behavior-constitution.md + AGENTS.md 禁止清单——宪法文件化、版本化、进 git。
- **同构结论**：宪法之所以稳定，是因为它同时满足「写下来」「写准」「放对地方（人和 AI 都读得到）」三条件；只满足前两条（写给人看的宪法）对 Agent 无效。

## 失败模式

| 失败 | 症状 | 修复 |
|:--|:--|:--|
| 把品质当文化而非机制 | 反复强调「要实事求是」但没有检查动作 | 每条品质翻译成一个可执行检查（锚点/交叉验证/审批） |
| 门禁只拦下级 | 权威发言免检，错起来无人能纠 | 锚点要求无差别适用于所有角色（F-035 拦的正是审查者） |
| 口头红线当生产机制 | 「说过了不许删」但权限没收 | 高危动作技术隔离+审批流 |
| 宪法 inflation | 规则越写越多，没人读完，约束力稀释 | 底线层（rules-core）保持 10 条量级，细则下沉到流程 |

## Synthesis

本桥的操作价值：①为 KDO 门禁体系补了一个外部互证源——「证据优先于身份」不是本库的偏执，是 AI 组织自我纠错的最小条件（一堂在多 Agent 实验里自发撞见，KDO 在失败模式里强制长出）；②给「实事求是」这个老词一个 AI 时代的操作化定义（交叉验证 Skill+宪法+流程），可直接用于向新人解释本库为什么要跑 pre-submit；③宪法三条件（写下来/写准/放对地方）是排查「规则不生效」的诊断顺序。与 [[bridge-yitang-seek-truth-liberate-thought]] 的关系：本桥是其实事求是一端在 AI 组织层的展开与更新（诊断 §四 指定的新证 related 补链对象）。

## Action Triggers

| 触发场景 | 第一个动作 | 成功指标 |
|:--|:--|:--|
| 写审查意见/负向结论 | 先跑存在性核查并附锚点 | 判词无锚点即不发出 |
| 设计 AI 协作规则 | 问：这条规则是品质要求还是检查动作 | 每条规则有检查动作与拦截点 |
| 给 Agent 开权限 | 先划删除/外发/支付三类高危边界 | 高危动作有技术隔离或审批 |
| 规则屡屡不生效 | 按宪法三条件排查 | 定位到「没写准」还是「放错地方」 |

## 迭代日志

- 2026-09-06 v1.0：#654 batch1 生产，据台账 A5/A50/A67-68/B49 + F-035 实证（agent-behavior-constitution.md:24）对读；引语逐字回验。
