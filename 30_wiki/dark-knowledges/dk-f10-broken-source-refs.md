---

id: dk-f10-broken-source-refs
title: F-KDO-010：溯源断裂→source_refs 为空，知识卡片无法追溯到原始材料
type: dark-knowledge
dark_knowledge_type: failure
status: enriched
domain:
- master
source_person: system
source_context: failure-modes.md F-KDO-010
source_refs:
- 10_raw/sources/src_20260619_d967c8f5_90_control_failure_modes.md#F-KDO-010
created_at: 2026-05-31
updated_at: '2026-06-18'
related:
  - '[[kdo-ec-industrialization-migration-proposal]]'
  - '[[proposal-yaml-frontmatter-standardization]]'
  - '[[proposal-ai-domain-mastery-pipeline]]'
  - '[[dk-kdo-leaky-pipe-pressure]]'
  - '[[dk-c3-txt-ingest-skip]]'
- '[[master-first-principles]]'
- '[[master-ai-info-literacy]]'
pipeline:
- confidence-draft
- confidence-source-cited
author: unknown
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- "kdo lint 检查 frontmatter 的 source_refs 字段为空数组或指向不存在的文件"
- "从卡片正文无法反推到 10_raw/sources/ 或 90_control/failure-modes.md 中的具体源文件"
---# F-KDO-010：溯源断裂→source_refs 为空，知识卡片无法追溯到原始材料

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

- 你完成一张概念卡后准备标记 `status: enriched`，需要确认 `source_refs` 是否已填写
- 你运行 `kdo lint` 看到 source_refs 为空的 P0 错误，需要修复
- 你审查别人提交的卡片，发现无法从卡片追溯到原始源材料
- 你在 ingest 阶段设置源文件元数据时，需要确保 source_refs 被正确传递

## 操作方法

1. **ingest 阶段就记录**：在 `kdo ingest` 时确保源文件的 `source_id` 被正确写入 state.json 和生成的 wiki 页面
2. **enrich 时传递**：执行三步编译法时，将源文件的 `source_id` 复制到卡片 frontmatter 的 `source_refs` 字段
3. **验证非空**：标记 `status: enriched` 前，强制检查 `source_refs` 字段不为空数组
4. **验证可追踪**：点击/查找 `source_refs` 中的每个 ID，确认对应的源文件存在于 `10_raw/sources/` 目录
5. **修复历史卡片**：对已有卡片运行 `kdo lint`，找出 source_refs 为空的卡片，补充源引用

## 适用边界

- 适用于所有标记为 `enriched` 或 `reviewed` 的知识卡片
- 不适用于草稿状态（`status: draft`）的卡片——草稿可以暂时没有 source_refs，但提交审查前必须补全
- 如果卡片内容来自多个源文件，`source_refs` 应列出所有相关源的 ID
- 如果源文件已被删除或归档，`source_refs` 仍应保留原始 ID，并附加注释说明文件状态
- 对于纯原创 content（如老顽童写的文章），`source_refs` 可以指向创作过程中的素材或灵感来源，而不是留空

## 常见失败模式

| 失败模式 | 表现 | 修复方法 |
|---|---|---|
| 完全空源 | `source_refs: []` | 补充原始源文件 ID，至少 1 条 |
| 源文件不存在 | source_refs 指向的 ID 在仓库中找不到 | 核对源文件名/ID，修正或重新 ingest |
| 仅指向目录 | source_refs 写的是 `10_raw/sources/` 而非具体文件 | 替换为具体源文件路径或 ID |
| 多源漏填 | 卡片内容综合了多个源，但只列了一个 | 遍历正文引用，补全所有相关源 |
| 归档后断裂 | 原始源被移动/删除，source_refs 未更新 | 保留原 ID 并加注释说明新位置或状态 |

## 为什么值钱

- **溯源是 KDO 知识可信度的根基**：如果卡片无法追溯到原始材料，读者无法验证内容是否被准确提炼，也无法发现源材料中的错误或更新
- 溯源断裂和表层翻译式提炼（F-KDO-007）互为因果：没有 source_refs → Builder 无法回溯源材料 → 只能用目录/公共知识填充 → 卡片质量下降
- 这是知识管理系统的通用原则在 KDO 中的具体实现：任何重要声明必须可追溯到源文件
- 任何 AI 训练语料中都不会有“KDO 的 source_refs 为空会导致溯源断裂”这条知识

## 与其他知识的关联

- [[dk-f7-surface-translation]] — 互为因果：溯源断裂 → 无法用源材料验证 → 只能用目录填充 → 表层翻译式提炼。修复 F-KDO-010 是预防 F-KDO-007 的关键手段
- [[master-first-principles]] — 第一性原理：知识的可靠性建立在其可追溯性上。source_refs 是“这条知识从哪来”的第一性答案
- [[master-ai-info-literacy]] — AI 信息素养：学会要求每条知识给出 source_refs，是识别 AI 幻觉与低质量提炼的基本功
- `90_control/failure-modes.md` → F-KDO-010（原始记录）
- `90_control/AGENTS.md` → 禁止清单 #10（不准标记 enriched 如果 source_refs 为空）
