---
id: task_20260719_wangyuyan-banfeimao-agent-production
title: 半肥猫实战素材——Agent批量生产方法提取
type: task
status: in_progress
priority: P1
assignee: hermes
reviewer: 欧阳锋
created_at: 2026-07-19
expected_cards: 3（新卡）+ 2（已有卡补充）
source_refs:
- 00_inbox/半肥猫/（9篇文章，重点3篇）
- 00_inbox/半肥猫/【半肥猫】我的商业突破实践指南：如何封装一个可复用的业务 Skill_MCP 副本.md
- 00_inbox/半肥猫/【半肥猫】用 AI 把脑子里的经验，推进成一个最小可验证的数字交付 副本.md
- 00_inbox/半肥猫/【半肥猫】别只会问 AI：从一次 Codex 误删事故，看懂 AI 协作的记忆管理 副本.md
related:
- agent-native-card-design
- system-yitang-Y-model-os
- case-kdo-agent-factory-dual-triangle-practice
- framework-建模四步法
updated_at: '2026-07-20T14:44:08.144081+00:00'
---

# 半肥猫实战素材——Agent批量生产方法提取

> **来源**：半肥猫（AI一人公司实践者，18个数字员工+300+付费用户）的9篇实战文章
> **定位**：**不是新方法论——是已有方法论的实战验证与操作化**。提取半肥猫在Agent生产中已验证的标准化方法，注入KDO Agent生产管线。
> **域归属**：Agent建设域（已有 `agent-native-card-design` + `system-yitang-Y-model-os` + agent-spec卡簇）

---

## 一、核心判断

半肥猫的价值不是"他说了什么新理论"，而是"他**把理论跑成了可复制的操作流程**"。

| 半肥猫做了什么 | KDO当前状态 | 差距 |
|:---|:---|:---|
| Agent生产五步标准化 | 逐张任务单驱动，流程隐式 | **缺显式SOP** |
| 每张Skill卡附带"承诺核对表" | agent-spec有Action Triggers，但不统一 | **缺反向验收标准** |
| AI记忆四层分层管理 | KDO有四层对应的context加载 | **缺命名/可沟通框架** |
| 从课到Agent完整产品化链路 | 已在做但隐式 | **缺命名→缺复制→缺加速** |

---

## 二、生产清单

### 2.1 新建卡片（3张）

| # | 卡ID | 类型 | 优先级 | 核心内容 | 来源 |
|:--|:---|:---|:---|:---|:---|
| 1 | `tool-kdo-agent-production-checklist` | tool | P0 | 🔴 **最优先**。基于半肥猫五步法的Agent生产SOP清单：①找业务任务→②定输入输出协议→③封装Skill（Prompt+正反例+流程+验收标准）→④接入环境（MCP/TCPR）→⑤加控制机制（RAG检索+权限+日志+人工审核+测试回归）。每步附检查项、验收标准和常见跳步错误。老顽童接任务单后按此清单逐项勾稽 | Skill/MCP文章·五步法 + 经验→数字交付文章·第五步承诺核对表 |
| 2 | `dk-agent-promise-verification` | dk | P1 | "承诺核对表"：每张agent-spec卡必须标注四列——对外承诺/对应交付/用户动作/验收标准。"不能补交付的，就把表达降级"——反向核对逻辑。当前KDO agent-spec卡缺"不能承诺什么"的标注 | 经验→数字交付文章§第五步 |
| 3 | `dk-ai-memory-four-layers` | dk | P1 | AI记忆分层模型：即时上下文(临时)→会话记录(可恢复)→项目文档(稳定)→长期偏好(持久)。映射到KDO：当前对话/agent复盘/doc.md+domain-digest/personal-os+user-insight-profile。半肥猫Codex误删案例作为引子 | Codex误删文章§九-十 |

### 2.2 已有卡补充（2项）

| # | 目标卡 | 补充内容 | 来源 |
|:--|:---|:---|:---|
| 4 | `agent-native-card-design` | §Agent规格卡的验收标准中新增"承诺核对表"要求——每张agent-spec必须标注"能做什么"和"不能承诺什么"，映射到半肥猫的四个验收维度 | 半肥猫·承诺核对表 |
| 5 | `system-yitang-Y-model-os` | §context加载策略中引用 `dk-ai-memory-four-layers`，将KDO已有的四层context实践显式命名为"AI记忆分层模型" | 半肥猫·AI记忆分层 |

---

## 三、关键规则

### 3.1 与其他域的关系声明

- `tool-kdo-agent-production-checklist` 必须注明："本卡是KDO Agent生产操作SOP。Agent设计规范见 `agent-native-card-design`，运行时加载见 `system-yitang-Y-model-os`"
- 不要与建模域的 `framework-建模四步法` 混淆——建模四步法是方法论建模工具，本卡是Agent生产工序清单

### 3.2 `tool-kdo-agent-production-checklist` 的具体格式

必须做成**老顽童可直接勾稽的清单**，而非概念描述。每条检查项包含：
- 检查内容（一句话）
- 合格标准（可判断的）
- 典型跳步错误（如果跳过会怎样）

五步各不少于3条检查项。

### 3.3 链接规则

- 每张新卡 related ≥ 5 条
- `tool-kdo-agent-production-checklist` 必须双向链接到 `agent-native-card-design`
- `dk-ai-memory-four-layers` 必须双向链接到 `system-yitang-Y-model-os`

### 3.4 注意避坑

- **不要建新域**——挂Agent建设域下
- **不要拆18个数字员工案例**——那是半肥猫的业务，不是KDO的
- **不要重复建模域的内容**——建模四步法是方法论，本卡是操作SOP，互补

---

## 四、验收标准

- [ ] 3张新卡 + 2项补充全部通过 `kdo pre-submit`
- [ ] `tool-kdo-agent-production-checklist` 可被老顽童直接当checklist逐项勾稽（非概念描述）
- [ ] `dk-agent-promise-verification` 含半肥猫原文的表结构引用
- [ ] 已有卡补充不引入新ERROR
- [ ] 欧阳锋抽检 `tool-kdo-agent-production-checklist`——确认SOP可执行性

---

## 五、队列位置

- **入队编号**：待分配
- **状态**：`queued`
- **阻塞/依赖**：无
- **预计工期**：0.5-1个老顽童实例周期（3张轻量卡）

---

*王语嫣 · 2026-07-19 · 基于半肥猫实战素材提取*
