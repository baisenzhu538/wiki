---
id: "dk-c2-dual-status-machine"
title: "C-2：Schema status 字段混用两个状态机→字段值互相污染"
type: "dark-knowledge"
dark_knowledge_type: "failure"
status: draft
domain:
  - "master"
source_person: "Builder"
source_context: "2026-05-03"
source_refs:
  - "20_memory/corrections.md#C-2"
created_at: 2026-05-31
updated_at: 2026-05-31
related:
  - "dk-c10-batch-tool-no-dry-run"
  - "master-systems-thinking"
tags:
  - #domain/knowledge-management
  - #method/evaluation-method
  - #scene/knowledge-management/tagging
  - #scene/learning-methodology
  - #scene/skill-engineering
pipeline:
  - #boundary/requires-human-judgment
  - #source_type/error
  - confidence-draft
  - confidence-source-cited
author: legacy
reviewed_by: pending
---

# C-2：Schema status 字段混用两个状态机→字段值互相污染

## 原始表述

> `status` 字段出现了 `enriched`（不在 schema 枚举 `draft/reviewed/stable/needs-review` 中），Architect 误判为"Schema 写了但没严格执行"。
> 
> 根因：两个独立状态机共用了同一个字段名：
> - 编译进度状态机：`draft → enriched → reviewed → superseded`（wiki 页面 frontmatter）
> - 审批流程状态机：`draft → reviewed → stable → needs-review`（decision.yaml）
> 
> 修正：当前不改代码，在 `schemas/concept.yaml` 加注释声明两个状态机的存在。下一轮 Schema 升级时考虑拆分字段名（如 `compile_status` vs `approval_status`）。

## 使用场景

- 你在设计或修改 wiki 卡片/决策文件的 frontmatter schema，需要新增或复用字段名
- 你在审查别人提交的卡片，看到 `status: enriched` 或 `status: superseded`，需要判断这是合法值还是 schema 违规
- 你在编写自动化脚本读取 `status` 字段做逻辑分支（如"只处理 reviewed 状态的卡片"）
- 你在做 schema 版本升级，需要评估字段名拆分的影响范围

## 操作方法

1. **看到 status 字段，先问语义**：这个 status 描述的是"编译到哪个阶段了"还是"审批到哪个阶段了"？
2. **查文件类型定状态机**：
   - wiki 页面 frontmatter（`.md` 文件）→ 编译进度状态机：`draft → enriched → reviewed → superseded`
   - decision.yaml / 任务文件 → 审批流程状态机：`draft → reviewed → stable → needs-review`
3. **写 schema 时加注释**：如果在修改 `schemas/concept.yaml`，必须在 `status` 字段旁用注释声明两个状态机的共存，明确各自取值范围
4. **代码审查硬编码值**：检查所有读取 `status` 字段的脚本逻辑，确认它期望的是哪个状态机——一个脚本混用两个语义是灾难
5. **规划拆分**：下一轮 schema 升级时，将字段拆分为 `compile_status`（wiki 页面）和 `approval_status`（决策/任务文件），彻底消除歧义

## 适用边界

- 适用于所有读写 wiki 页面 frontmatter 或 decision.yaml 的场景——只要项目里同时存在"内容编译"和"流程审批"两条流水线
- 不适用于单一状态机的系统：如果整个项目只有一种进度状态，不会踩这个坑
- **当前方案是临时补丁（加注释），不是根治**：根治需要 schema 升级 + 全量数据迁移，成本较高
- 自动化脚本如果硬编码了 `status == "reviewed"` 这类判断，必须逐行确认它处理的是哪种文件类型
- 第三方工具或外部集成如果读取了 KDO 的 frontmatter，也会受到这个歧义的影响——对外接口文档必须说明

## 为什么值钱

- 这是 KDO 特有的 schema 设计债务：**两个状态机共用同一个字段名**。任何外部 AI 训练语料都不会有这条具体知识
- 症状极具迷惑性：`enriched` 看起来像个合法的进度描述，Architect 会误判为"Schema 写了但没严格执行"，而不是"设计冲突"——这种归因偏差会导向错误的修正方向（加 enforcement 而不是拆分字段）
- 揭示了 schema 演进中的经典陷阱：早期系统只有一个状态机，后期叠加第二个子系统时为了"兼容"没有 rename，结果产生语义污染
- 通用软件工程原则（"命名要清晰"）谁都知道，但"什么时候必须把字段拆分"这条边界判断——特别是"共存方案的成本 vs 拆分方案的成本"——只有踩过坑才有体感

## 与其他知识的关联

- [[dk-c10-batch-tool-no-dry-run]] — 同一深层模式：系统设计中"一个组件承担两种语义"导致的级联故障。C-10 是工具（scaffold）同时兼容新旧格式失败，C-2 是字段（status）同时承载两种状态机失败
- [[master-systems-thinking]] — 系统思维中的"边界清晰度"原则：两个独立子系统共用同一资源（字段名）时，边界模糊会导致涌现性故障。C-2 是这一原则在 schema 设计中的具体体现
- `20_memory/corrections.md` → C-2（原始记录）

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
