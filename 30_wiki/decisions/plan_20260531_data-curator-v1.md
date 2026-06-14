---
id: "plan_20260531_data-curator-v1"
title: "Data Curator Skill — 数据清洗+原子切分+多维标签 实施方案 v1.0"
type: "improvement-plan"
status: "superseded"
superseded_by: "plan_20260531_data-curator-v1.1"
domain:
  - "master"
tags:
  - "#domain/knowledge-management"
  - "#method/evaluation-method"
source_refs:
created_at: 2026-05-31
updated_at: 2026-05-31
version: 1
supersedes:
related:
  - "kdo-industrialization-manual"
  - "tool-card-excellence-standard"
  - "AGENTS"
author: "legacy"
reviewed_by: "pending"
confidence: 0.75
trust_level: "medium-low"
---

# Data Curator Skill 实施方案 v1.0

## 来源

本计划由黄药师（Builder）与用户关于 KDO 知识工厂数据架构的讨论触发。

**核心问题**：KDO 缺少原子级切分和多维标签体系——不是 AI 不需要，而是还没做。

## Summary

- **影响范围**：384 张概念卡（30_wiki/concepts/）
- **数据现状**：Gen A (154 张 YAML 丰富版) + Gen B (230 张 JSON 极简版)
- **核心缺口**：domain 192 缺失、tags 186 缺失、source_refs 14 缺失（P0）
- **skill 位置**：`40_outputs/capabilities/skills/data-curator/`
- **审批状态**：2026-05-31 方案已批准，pilot 待执行

---

## 五阶段流水线

```
Phase 1: Audit（只读）    → 数据质量报告 → 60_feedback/data-quality/
Phase 2: Clean（逐卡写）   → frontmatter 规范化 + 缺失字段推断
Phase 3: Tag（逐卡写）     → 受控词表 90_control/tag-registry.yaml + 全库打标
Phase 4: Chunk（写 state） → 原子主张注册表 .kdo/state.json chunks 字段
Phase 5: Validate（只读）  → 通过率矩阵 → 目标 ≥ 95%
```

## 安全约束（来自 pitfalls + 工业化手册）

| 约束 | 来源 | 规则 |
|------|------|------|
| 批量上限 5 张卡 | KF-022 | 每批 ≤ 5 张，逐批审查 |
| 先 dry-run 单卡 | C-10 | 禁止基础设施修改后直接批量 |
| 中文不跑 regex enrich | C-1 / F-KDO-001 | 用结构化解析（heading-based），不用 CJK regex |
| 标签禁止脚本自动生成 | C-9 | AI 推断 + 人类确认，不留不审的标签 |
| 完成=代码+数据+验证 | P-15 | 每批写完跑 kdo lint + kdo validate |
| 编辑前必须 Read | F-KDO-016 | 写卡前确认当前文件状态 |

## Phase 1: Audit

**脚本**：`scripts/audit_cards.py`
**产出**：`60_feedback/data-quality/audit-YYYY-MM-DD.json`
**状态**：✅ 已完成（2026-05-31，384 张卡）

**关键发现**：
- 15 张卡有 error，384 张卡有 warning
- top 缺失：trust_level(292), contradicts(230), domain(192), tags(186)
- status 分布：enriched(342), draft(18), reviewed(14)
- 1 张卡花引号编码损坏（`��enriched��`）
- contradicts 字段全库零使用（死字段）

## Phase 2: Clean

**脚本**：`scripts/clean_cards.py`
**清洗规则**：

| 规则 | 内容 |
|------|------|
| 引号统一 | 花引号→直引号；YAML 值统一不加引号 |
| 日期格式 | ISO timestamp → YYYY-MM-DD |
| 小数精度 | confidence 统一 2 位小数（0.8 → 0.80） |
| 枚举标准化 | domain 统一为 YAML 列表；type 补充缺失 enum |
| 缺失推断 | type 默认 concept；id 从文件名推导；status 按 Critique 存在性推断 |
| 死字段 | contradicts 移除（保留 schema 定义） |

**执行节奏**：pilot 3 张 → batch(5) → 384 张
**状态**：⏸️ pilot dry-run 完成，待 write 审批

## Phase 3: Tag

**脚本**：`scripts/tag_cards.py`
**词表**：`90_control/tag-registry.yaml`（4 维 27 个受控标签值）

| 维度 | namespace | 示例 |
|------|-----------|------|
| 方法论 | `#method/*` | thinking-tool, decision-framework, learning-method |
| 领域 | `#domain/*` | healthcare-it, ai-engineering, entrepreneurship |
| 质量信号 | `#quality/*` | needs-review, stub, ocr-card, high-signal |
| 图谱角色 | `#role/*` | hub, leaf, bridge, reference |

**推理规则**：文件名前缀 → domain tag → 内容关键词（优先级递减）
**状态**：⏸️ pilot dry-run 完成，待 write 审批

## Phase 4: Chunk

**脚本**：`scripts/chunk_cards.py`
**块类型**（从卡片章节结构派生）：

| 类型 | 来源 heading |
|------|-------------|
| claim | Claims, 核心主张, 稳定概念 |
| constraint | Critique, 质疑, Constraints, 外部攻击 |
| critique | Scholar, 学者, 攻击者 |
| synthesis | Synthesis, 对标, 综合, 跨域 |
| question | Open Questions, 开放问题 |
| action_trigger | Action Triggers, 触发, 适用场景 |
| procedure | Procedure, 步骤, 操作 |
| definition | Summary, 概述, 定义 |
| example | Example, 案例, 实例 |
| reference | Source Refs, 来源, 参考文献 |

**寻址方案**：`<card_slug>/<chunk_type>/<NNN>`
**元数据继承**：domain, tags, confidence, trust_level, source_refs, status, type
**状态**：⏸️ pilot dry-run 完成，待 write 审批

## Phase 5: Validate

**脚本**：`scripts/validate_clean.py`
**12 个验证维度**：frontmatter 存在性、核心字段、domain 非空/合法、tags 非空/在词表中、source_refs 非空、status/type 合法、chunks 存在/ID 唯一/source_refs 继承
**目标**：≥ 95% 通过率
**状态**：⏸️ 待 Phase 2-4 完成

## 交付物清单

| 文件 | 状态 |
|------|------|
| `40_outputs/capabilities/skills/data-curator/SKILL.md` | ✅ 已创建 |
| `40_outputs/capabilities/skills/data-curator/scripts/audit_cards.py` | ✅ 已创建，已验证 |
| `40_outputs/capabilities/skills/data-curator/scripts/clean_cards.py` | ✅ 已创建，dry-run 验证通过 |
| `40_outputs/capabilities/skills/data-curator/scripts/tag_cards.py` | ✅ 已创建，dry-run 验证通过 |
| `40_outputs/capabilities/skills/data-curator/scripts/chunk_cards.py` | ✅ 已创建，dry-run 验证通过 |
| `40_outputs/capabilities/skills/data-curator/scripts/validate_clean.py` | ✅ 已创建 |
| `90_control/tag-registry.yaml` | ✅ 已创建（v1, 27 标签值） |
| `90_control/schemas/concept.yaml` | ⏸️ 待扩展（status + enriched, type + tool/framework） |
| `.kdo/state.json` | ⏸️ 待 Phase 4 写入 chunks 字段 |

## 迭代设计

- **v1.0**（当前）：方案定义 + 脚本实现 + pilot dry-run
- **v1.1**（待定）：pilot 3 张卡 write + lint 验证
- **v1.2**（待定）：batch 5 推进 + 数据管理文档集成
- **v2.0**（待定）：384 张卡全量完成 + schema 更新 + state.json 扩展

## Pilot 测试结果（2026-05-31）

| 卡片 | Clean | Tag | Chunk |
|------|-------|-----|-------|
| master-systems-thinking | 无需修改 | 5 tags 有效 | 16 chunks (4 types) |
| business-analysis | 日期 ISO→YYYY-MM-DD | 2 tags 有效 | 5 chunks (5 types) |
| ocr-一堂-个人修炼-科学学习ipo模型 | 日期 ISO→YYYY-MM-DD | 5 tags（1 误判需人工修） | 7 chunks (5 types) |

## 待输入

- [ ] 用户提供的更多数据管理文档 → 触发方案迭代（v1.1+）
- [ ] 每次迭代更新本文件的 `version` 和 `updated_at`
