---

id: framework-wanghuan-three-tier-dev-architecture
title: 王欢三层开发架构：需求拆解→AI开发→哨兵质检
type: framework
status: enriched
domain:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
created_at: '2026-06-19'
updated_at: '2026-06-28'
author: 王语嫣
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
source_person: 王欢
source_context: 王欢 AI 实战分享（2026-06-18 授课）
source_refs:
- 10_raw/sources/src_20260619_e4b35a3a_wanghuan_task_product_system_transcript.md
- 10_raw/sources/src_20260619_536bca67_wanghuan_actor_director_oral.txt
- 10_raw/sources/src_20260619_a3a2a803_wanghuan_actor_director_notes.txt
related:
  - [[framework-wanghuan-actor-director-mode]]
  - [[framework-wanghuan-bitcoe-prompt-framework]]
  - [[concept-wanghuan-adversarial-generation]]
  - [[case-wanghuan-shenyang-software-3x-efficiency]]
  - [[pending_unknown]]
diagnostic_signals:
- lens: 系统瓶颈 vs. 工具瓶颈
  follow_up: 检查当前流程是否只是给马车换发动机，还是已重新设计工作系统
- lens: 角色定义
  follow_up: 将角色重新定义为让 AI 把代码写好的人，强调判断力而非执行量
- lens: 输入质量
  follow_up: 回到需求拆解层，用 BTICOE 补全原子任务和约束条件
- lens: 验收标准
  follow_up: 检查哨兵质检层是否有清晰的人工复核 checklist 和红线约束
tags:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

---

# 王欢三层开发架构：需求拆解→AI开发→哨兵质检

> **Burn line**: 程序员不是写代码的人，是让 AI 把代码写好的人。

---

## 用一句话讲清楚

把人机协作的软件开发拆成三层：**需求拆解层、AI 代码执行层、审查验收层**。人负责定义问题和验收标准，AI 负责中间执行；把程序员的职责从写代码升级为质量守门人，从而在工具不变的前提下实现效率数量级跃升。

---

## 核心要点

1. **三层分工**：需求拆解层把模糊需求拆成可执行的原子任务；AI 开发层按任务生成代码与单元测试；哨兵质检层对代码质量、安全、规范进行审查与人工逻辑复核。
2. **人的角色升级**：人不是执行者，而是定义者和验收者；核心能力从写代码变成判断代码能不能用。
3. **效率跃升来源**：不是换更好的 AI 工具，而是重新设计工作系统；沈阳软件公司案例显示，同一批工具下效率从 +30% 跃升至接近 3 倍。
4. **导演的底层逻辑**：与 [[framework-wanghuan-actor-director-mode]] 一致——定义开头 + 验收结尾，中间执行交给 AI。
5. **可迁移到通用知识工作**：内容生产、知识萃取、KDO 建卡均可映射为拆解→生成→质检三段式。
6. **关键使能器**：[[framework-wanghuan-bitcoe-prompt-framework]] 用于消灭输入模糊；[[concept-wanghuan-adversarial-generation]] 可用于哨兵层的对抗评审。

---

## 边界

| 适用 | 不适用 |
|:---|:---|
| 软件外包/内部研发团队，需求可被拆分为原子任务 | 需求高度模糊、变化极快、无法定义验收标准的探索性项目 |
| 团队已能用 AI 辅助编程，但效率卡在 30% 左右 | 团队尚未具备基本 AI 工具使用能力，或成员完全拒绝协作 |
| 有明确编码规范、测试标准、安全要求 | 没有质量基准、无 SOP、无法判断好代码长什么样 |
| 程序员愿意承担质量守门人新角色 | 组织仍按代码行数或工时考核个人产出 |
| 重复性开发任务占比高 | 高度创造性架构设计或零到一算法研究 |

---

## 失败模式 / 常见走偏

| 走偏模式 | 表现 | 纠偏动作 |
|:---|:---|:---|
| **拆解不清就开发** | AI 生成的代码偏离需求，反复返工 | 回到需求拆解层，用 BTICOE 补全原子任务、输入输出、验收标准 |
| **人陷入代码细节** | 程序员忍不住自己改代码，成为更快的演员 | 明确角色契约：你是让 AI 写好代码的人，只在验收节点介入 |
| **质检流于形式** | 只跑 ESLint/SonarQube，不做人工逻辑复核 | 建立人工复核 checklist，把能不能上线作为最终人的决策 |
| **三层串行变孤立** | 拆解不管开发，开发不管验收，各层输出对不上 | 每层输出必须是下一层的输入，用统一文档和验收标准串联 |
| **忽视团队心理障碍** | 成员担心被 AI 取代，消极抵制 | 先让负责人自己跑通，再定义新角色为判断力升级而非能力否定 |
| **工具崇拜** | 认为换更贵模型就能自动达到 3 倍效率 | 先检查系统是否重新设计；工具升级无法替代流程重构 |

---

## 行动 Checklist

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

---

## 相关卡 / 互链

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

---

## Critique

- src_unknown  
  **回应**：该架构并非取消程序员，而是把程序员的精力从逐行编码转移到需求拆解、约束定义和最终验收。AI 不懂的行业暗规则，恰好需要人的判断力来填补，人的经验反而更稀缺。

- src_unknown  
  **回应**：三层架构适用于需求可结构化、可定义验收标准的场景；在高度不确定的探索期，应先用最小原型验证假设，而不是硬套完整三层流程。

- src_unknown

---

## Synthesis

王欢的三层开发架构本质上是一套人机协作系统：它把软件开发中人的价值从执行压到定义与验收两端，让 AI 承担中间可规模化执行的部分。沈阳软件公司案例说明，真正的效率跃升并非来自更贵或更新的工具，而是来自对工作系统的重新设计——同一批 AI 工具，在演员思维下只能线性提升 30%，在导演思维下可接近 3 倍。这一模式可以迁移到任何需求可被结构化、输出可被验收的知识工作：内容生产、知识萃取、销售训练，甚至 KDO 卡片生产。

但要让这套架构落地，组织必须同时解决技术标准和身份标准两个问题：技术上要有清晰的原子任务、约束红线和人工复核 checklist；身份上要让执行者接受从写代码的人变成让 AI 写好代码的人。如果缺少任一条件，三层架构都会退化为新瓶装旧酒的流程装饰。参考 [[case-wanghuan-shenyang-software-3x-efficiency]] 的落地路径：先由负责人自己跑通，再小范围验证，最后才把新角色和流程推广到团队。
