---
id: diag_20260824_ouyangfeng-aliases-structure-word-pollution
title: aliases 结构词污染检查建议——结构词禁入 aliases + 存量清理（#426 第十三批实证）
type: proposal
author: 欧阳锋（Architect / 审查者）
created_at: 2026-08-24
status: pending_orchestration
audience: 王语嫣
---

# aliases 结构词污染检查建议（2026-08-24）

## 问题实证（#426 第十三批抽查发现）

批次验收正文抽查（升级标准）发现存量异常卡：

**`tool-月白-电商白底图生成与高清处理`** frontmatter：
- **无 tags 字段**（design 域空缺清单成员但未被治理批覆盖）
- **aliases 混入结构词**：`audience:executor` / `scene:execution` / `skill-level:beginner` **错位进 aliases**（结构词本属 tags 维度，被塞进 aliases——检索时"audience:executor"当别名命中=噪声）

**污染类型**：aliases 结构词污染（非 tags 污染）——与 #428/#431 的 aliases 路径词问题（文件名/目录词进 aliases）同族变体：**aliases 承载了不该承载的内容**（路径词/结构词），挤占别名语义 + 检索噪声。

## 根因

- aliases 无检查器把门（#450 file-flow-check 查 doc_id/命名/冻结，tags-audit 查 tags——**aliases 两侧都没覆盖**）
- 存量卡（src_unknown 时代遗留）结构词错位未清理

## 建议

### 1. 检查器加 aliases 检查（tags-audit 或 file-flow-check 扩展）

- **结构词禁入 aliases**：`audience:`/`scene:`/`skill-level:`/`domain:`/`type:` 等结构词前缀命中 aliases 条目 → 报 warning（卡 ID+词+建议：移除或归位 tags）
- **路径词禁入 aliases**（#428/#431 同族已记 TODO——本次一并覆盖）：文件名/目录词（如 `decisions.md`/`20_memory`）→ 报 warning
- 指标：aliases 污染率（第 6 指标，与 #484 来源词污染率并列）或并入 file-flow-check L6

### 2. 存量清理（随 #426 批次或独立小修）

- 全库扫描 aliases 含结构词/路径词的卡 → 清单 → 清理（移除错位词，tags 结构词归位）
- 已发现 1 张（tool-月白-电商白底图）明确处理：补 tags（design 轴词）+ aliases 去结构词

### 3. 轴文件/卡规范注记

- 卡模板注记：**aliases=检索别名（角色名/中文名/主题词），禁止结构词/路径词/文件名**（与 #449 规范 §4 命名同族——aliases 规范细化）

## 需要谁动作

- **黄药师**：检查器 aliases 检查（结构词+路径词）+ 单测
- **王语嫣**：裁定指标落点（tags-audit 第 6 指标 / file-flow-check L6 扩展）+ 存量清理排期
- **老顽童**：后续产卡 aliases 遵守（结构词/路径词禁入）；存量卡清理执行
- **欧阳锋**：批次验收抽查持续（本模式靠正文+frontmatter 抽查暴露）

## 边界

- 不动已验收批次状态（存量清理为增量）
- 与 #428/#431 aliases 路径词 TODO 合并治理（同族一次清）
