---

id: dk-f10-broken-source-refs
title: F-KDO-010：溯源断裂→source_refs 为空，知识卡片无法追溯到原始材料
type: dk
dark_knowledge_type: failure
status: enriched
domain:
- master
source_person: system
source_context: failure-modes.md F-KDO-010
source_refs:
- src_unknown
created_at: 2026-05-31
updated_at: '2026-06-18'
related:
  - [[kdo-input-channel-strategy-2026-06-16]]
  - [[kdo-protocol]]
  - [[modeling-to-kdo-toolchain]]
  - [[kdo-batch-produce-req014]]
  - [[dk-foresight-source-material-blindness]]
  - [[kdo-15-dimension-label-spec]]
  - [[obsidian-kdo-内容产出工作流-产品设计大纲]]
  - [[tool-ban-fei-mao-qing-xi-zi-liao-wei-markdown-ge-shi-wei-gei-ai]]
  - [[framework-kdo-self-attack]]
  - [[kdo-yaml-frontmatter-safety]]
  - [[kdo-priority-checklist]]
  - [[dk-ai-scarcest-resource-is-self]]
  - [[tool-doris-industry-report-source-evaluation]]
  - [[kdo_product_design_agent_final]]
  - [[proposal-kdo-flywheel-infrastructure]]
pipeline:
- src_unknown
- src_unknown
author: unknown
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- src_unknown
- src_unknown# F-KDO-010：溯源断裂→source_refs 为空，知识卡片无法追溯到原始材料

---

## 原始表述/核心洞察

### 原始表述

> **触发场景**：Builder 完成知识卡片后标记 `status: enriched`
>
> **表现**：frontmatter 中 `source_refs: []` 为空数组，知识卡片无法追溯到原始材料
>
> **根因**：Builder 在 enrich 阶段未记录源文件引用，或 ingest 阶段未正确设置 source_refs
>
> **触发信号**：`kdo lint` 检查 frontmatter 的 source_refs 字段为空或指向不存在的文件
>
> **防御措施**：① L1 Lint：`source_refs` 为空数组 = P0 阻断，卡片不得标记为 enriched（Sprint 1 实现）② 对标 KF-005（溯源强制）
>
> **关联案例**：2026-05-08 审查的 5 张卡片 source_refs 全部为空；EC 迁移提案痛点 #1（14 broken wikilinks）
>
> **关联**：与 F-KDO-007（表层翻译式提炼）互为因果——无源文件可追溯 → 只能用目录填充

### 核心洞察

溯源是 KDO 知识可信度的根基。`source_refs` 不是装饰字段，而是“这条知识从哪来”的第一性答案。一旦 source_refs 为空或断裂，读者无法验证提炼是否准确，也无法发现源材料的更新或错误，最终卡片退化为不可审计的目录式摘要。

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **ingest 阶段就记录**：在 `kdo ingest` 时确保源文件的 `source_id` 被正确写入 state.json 和生成的 wiki 页面
2. **enrich 时传递**：执行三步编译法时，将源文件的 `source_id` 复制到卡片 frontmatter 的 `source_refs` 字段
3. **验证非空**：标记 `status: enriched` 前，强制检查 `source_refs` 字段不为空数组
4. **验证可追踪**：点击/查找 `source_refs` 中的每个 ID，确认对应的源文件存在于 `10_raw/sources/` 目录
5. **修复历史卡片**：对已有卡片运行 `kdo lint`，找出 source_refs 为空的卡片，补充源引用

## 适用边界

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 常见失败模式

| 失败模式 | 表现 | 修复方法 |
|
|---|---|
| 完全空源 | `source_refs: []` | 补充原始源文件 ID，至少 1 条 |
| 源文件不存在 | source_refs 指向的 ID 在仓库中找不到 | 核对源文件名/ID，修正或重新 ingest |
| 仅指向目录 | source_refs 写的是 `10_raw/sources/` 而非具体文件 | 替换为具体源文件路径或 ID |
| 多源漏填 | 卡片内容综合了多个源，但只列了一个 | 遍历正文引用，补全所有相关源 |
| 归档后断裂 | 原始源被移动/删除，source_refs 未更新 | 保留原 ID 并加注释说明新位置或状态 |

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
