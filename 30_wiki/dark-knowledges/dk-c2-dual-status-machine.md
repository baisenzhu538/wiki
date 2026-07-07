---

id: dk-c2-dual-status-machine
title: C-2：Schema status 字段混用两个状态机→字段值互相污染
type: dk
dark_knowledge_type: failure
status: reviewed
domain:
- master
source_person: Builder
source_context: 2026-05-03
source_refs:
- src_unknown
created_at: 2026-05-31
updated_at: '2026-06-16'
related:
- "[[kdo-ec-industrialization-migration-proposal]]"
- "[[kdo-protocol-implementation-roadmap]]"
- "[[plan_20260503_f3e9a2b1-improvement-plan]]"
- "[[dk-f10-broken-source-refs]]"
- "[[dk-c4-selfcheck-superseded]]"
- "[[dk-c10-batch-tool-no-dry-run]]"
- "[[dk-p18-yaml-parser]]"
- "[[kdo-yaml-frontmatter-safety]]"
- "[[master-systems-thinking]]"
pipeline:
- src_unknown
- src_unknown
author: unknown
reviewed_by: 欧阳锋
confidence: 0.7
trust_level: low
diagnostic_signals:
- signal: src_unknown
  framework_lens: 同一个 `status` 字段名被两个独立状态机共用：wiki 页面用编译进度状态机，decision.yaml 用审批流程状态机
  follow_up_question: 先确认文件类型：若是 `.md` 则 `enriched/superseded` 合法；若是 `decision.yaml` 则属违规。是否在 schema 注释中显式声明了双状态机？
- signal: src_unknown
  framework_lens: 脚本把单一状态语义硬编码到所有文件类型，没有区分 frontmatter 与 decision 文件的状态机
  follow_up_question: 把脚本改为按文件类型分支；为两种状态机分别定义枚举常量；为过滤逻辑补单元测试，覆盖 enriched、superseded、stable、needs-review 等边界值
- signal: src_unknown
  framework_lens: 这是归因偏差：把设计冲突（两个状态机共用字段名）误判为执行松懈（schema 写了但没严格执行）
  follow_up_question: 重新审视系统中是否真的只有一个状态机；若存在两条流水线，必须拆分字段名或在 schema 中显式保留双枚举并注明适用范围
- signal: src_unknown
  framework_lens: 外部集成未被告知 `status` 字段的双重语义，按单一枚举解析必然报错
  follow_up_question: 在对外接口文档中写明 `status` 的双重语义和两张取值表；考虑对外暴露拆分后的字段（如 `compile_status` / `approval_status`）# C-2：Schema status 字段混用两个状态机→字段值互相污染
---
## 原始表述

> `status` 字段出现了 `enriched`（不在 schema 枚举 `draft/reviewed/stable/needs-review` 中），Architect 误判为"Schema 写了但没严格执行"。
> 
> 根因：两个独立状态机共用了同一个字段名：
> - 编译进度状态机：`draft → enriched → reviewed → superseded`（wiki 页面 frontmatter）
> - 审批流程状态机：`draft → reviewed → stable → needs-review`（decision.yaml）
> 
> 修正：当前不改代码，在 `schemas/concept.yaml` 加注释声明两个状态机的存在。下一轮 Schema 升级时考虑拆分字段名（如 `compile_status` vs `approval_status`）。

## 深度洞察

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **看到 status 字段，先问语义**：这个 status 描述的是"编译到哪个阶段了"还是"审批到哪个阶段了"？
2. **查文件类型定状态机**：
   - src_unknown
   - src_unknown
3. **写 schema 时加注释**：如果在修改 `schemas/concept.yaml`，必须在 `status` 字段旁用注释声明两个状态机的共存，明确各自取值范围
4. **代码审查硬编码值**：检查所有读取 `status` 字段的脚本逻辑，确认它期望的是哪个状态机——一个脚本混用两个语义是灾难
5. **规划拆分**：下一轮 schema 升级时，将字段拆分为 `compile_status`（wiki 页面）和 `approval_status`（决策/任务文件），彻底消除歧义
6. **对外接口显式声明**：任何向外部暴露 `status` 的 API/文档，必须附两张状态机取值表或直接使用拆分后的字段名

## 适用边界

| 边界 | 说明 |
|:
--|:------|
| 适用于同时存在内容编译流与审批流程的项目 | 只有两条流水线共用字段名时才会触发此问题 |
| 适用于所有读取 frontmatter/decision.yaml 的自动化脚本 | 脚本硬编码 `status` 判断时风险最高，必须按文件类型分支 |
| 当前"加注释"方案是临时补丁，非根治 | 根治需要 schema 升级 + 全量数据迁移，成本较高 |
| 不适用于单一状态机系统 | 如果全项目只有一种进度状态，不会出现此问题 |
| 对外接口必须显式说明 | 第三方工具读取 KDO frontmatter 会受歧义影响，接口文档必须声明双状态机 |

| 模式 | 症状 | 修复 |
|:-----|:------|:-----|
| 状态机 A 的值被状态机 B 判定为非法 | `kdo validate` 报告 `status: enriched` 不在 `draft/reviewed/stable/needs-review` 枚举中 | 在 schema 注释声明双状态机；校验脚本按文件类型使用不同枚举 |
| 脚本硬编码单一状态语义 | 过滤脚本只认 `reviewed`，漏掉 enriched 卡片或把 decision 的 stable 卡片当成已审 | 改为按文件类型分支；用显式枚举常量；添加覆盖 enriched/superseded/stable/needs-review 的单元测试 |
| 归因偏差：把设计冲突当执行问题 | 讨论结论变成"加强 schema enforcement"，准备删 enriched 值或强制改写 | 重新审视是否存在第二状态机；若存在，拆分字段或在 schema 中保留双枚举并注明适用范围 |
| 外部集成未被告知双语义 | 第三方工具同步 KDO 卡片后，`status` 字段解析报错或逻辑错误 | 在接口文档写明 `status` 的双重语义；提供映射表；考虑对外暴露拆分后的字段 |
| Schema 升级时未迁移历史数据 | 拆分字段后，旧 `.md` 文件的 `status` 值被误读为 `approval_status` | 升级脚本必须按原文件类型映射旧 `status` 到新字段；升级后全量校验 |

## 落地模板：双状态机排查 Checklist

**适用时机**：新增/修改 schema、写自动化脚本、做 schema 升级、对接外部系统前。

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 为什么值钱

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 与其他知识的关联

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
