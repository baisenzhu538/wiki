---
id: diag_20260824_external-agent-usage-observation
title: 外部 agent 使用 KDO 观察留档（WorkBuddy 会话实证——外部使用基线首例）
type: diagnosis/observation
author: 王语嫣
created_at: '2026-08-24'
status: draft
audience: 老朱 / 黄药师（检索基建）
related:
  - F-052（外部检索入口指引，停车场）
  - F-053（kdo query 外部可及性，停车场）
---

# 外部 agent 使用 KDO 观察留档（首例基线）

## 现象

2026-08-24 晚，外部 agent（WorkBuddy/Claw 项目实例，非 KDO 体系内）在 `C:\Users\Administrator\Desktop\对话上下文_2026-08-24_18点后.zip` 会话中消费 KDO 知识库（读 8 个文件、写 3 份一堂课程作业），并讨论 OpenClaw vs Hermes 架构。老朱 08-24 指示：其检索方式作外部使用证明，审计 KDO 检索基建。

## 检索方式证据（会话还原）

| 方式 | 证据 | 评价 |
|:--|:--|:--|
| Read 已知路径直接读（8 个 KDO 文件） | 00_inbox 逐字稿 / 60_feedback 诊断 / 30_wiki 卡 | ✅ 路径可发现——目录结构对陌生 agent 可用 |
| Grep 全文关键词（带纪律：-C 3/-n/head_limit 40） | 探索营逐字稿 grep `Hermes\|爱马仕\|OpenClaw\|龙虾` | ✅ 有纪律 grep（与我们 W3 定点复核同构） |
| 命中后定点 Read 大段（offset 405 limit 80） | 读探索营 L405-485 | ✅ 行号锚定设计对外友好 |
| **未用** kdo query / search_index / MOC / domain-mapping | 全程无语义层触达 | ⚠️ 语义检索对外不可发现——Grep 全文碰运气 + 大段推理试探路径（找"Truman 分工论述"低效实证） |

## 外部建议（会话中 WorkBuddy 对老朱）

1. 别在"OpenClaw vs Hermes"选边上内耗（Feature 思维自由穿梭）
2. **产物沉淀成高质量顶层文档/角色配置文档**——文档成为跨工具资产（"文档完备度 >> 工具选择" L479）
3. Session << AI记忆 << 文档知识库（L437）——显性文档最值钱
4. 老朱卡点=共享上下文/顶层文档未沉淀扎实（非框架问题）

## 基线三指标（外部使用基线首例）

1. **路径可发现性**：✅ 通过（目录结构友好，陌生 agent 直觉可读）
2. **语义检索触达**：⚠️ 未触达（kdo query/MOC 对外不可发现——基建缺口实证）
3. **外部建议与 KDO 哲学一致性**：✅ 一致（文档>工具/上下文模式=vault 真相源设计，独立印证方向正确 + 提醒文档完备度继续投资）

## 落地

- **F-052**：外部 agent 检索入口指引（AGENTS.md/README 加"外部检索协议"：kdo query 用法/MOC 清单/域清单路径）
- **F-053**：kdo query 外部可及性（无 workspace 上下文轻量检索入口，与 F-021 同族）
- 本留档作基线参照，后续外部使用事件可对比

*王语嫣 · 2026-08-24 · 留档（证据=桌面 zip 会话导出）*
