---
id: task-20260627-huangyaoshi-source-refs-dryrun
title: 黄药师任务：source_refs file-not-found 清查与修正（dry-run）
type: task
domain: [kdo, infrastructure]
status: in_progress
author: 欧阳锋
reviewed_by: pending
created_at: 2026-06-27
updated_at: 2026-06-27
source_refs:
  - 30_wiki/domains/decision-science-domain-digest.md
priority: P1
trust_level: high
---

# 黄药师任务：source_refs file-not-found 清查与修正（dry-run）

## 背景

taxonomy 目录/type 大迁移已完成（`concepts/tool-*.md` → `tools/`，`dark-knowledge`/`dark_knowledge` → `dk`）。当前 `kdo lint` 基线：

- **ERROR: 1261**
- **WARNING: 48665**

剩余 ERROR 主要由两类构成：

1. `source_refs` 指向磁盘上不存在的文件（约 347 条）—— **本次任务处理**
2. `dark-knowledges/` 卡片缺少标准 section（原始表述 / 使用场景 / 操作方法 / 适用边界 / 为什么值钱 / 关联）—— **内容债，不处理**

## 任务目标

对全库 `source_refs` 做一次机械式清查，输出 dry-run 清单，待欧阳锋审批后 apply。

## 验收标准

1. dry-run 清单覆盖全库所有 `source_refs entry` 的文件存在性检查结果
2. 每条不存在的 source_ref 必须给出明确的处理建议（三选一）：
   - **修正路径**：源文件存在但路径写错（给出建议路径）
   - **降级为 `src_unknown`**：源文件确实缺失且无法追溯
   - **人工判定**：无法自动判断，标红由欧阳锋决定
3. apply 后 `kdo lint` ERROR 数 **≤ 当前基线 1261**， preferably 下降
4. 不引入新的 WARNING 类别

## 处理规则

### 规则 1：路径写错的判定

满足以下任一条件，视为"路径写错"：

- 文件名高度相似（如 `冉鹏战略课逐字稿_ocr.md §38` vs `冉鹏战略课逐字稿_ocr.md`）
- 文件存在但路径中某段目录名写错（如 `_vlm_reprocess/泛产品设计/...` 多字/少字）
- 文件存在但扩展名写错（`.md` vs `.txt`）

### 规则 2：降级为 `src_unknown` 的判定

满足以下全部条件：

- 文件在当前 vault 中完全找不到
- 文件名不是纯占位符（如 `source_unknown`、`src_unknown` 已合规，无需再处理）
- 无法从文件名推断出替代路径

### 规则 3：禁止的修改

- 不要修改卡片正文内容
- 不要修改 `type`、`domain`、`related` 等字段
- 不要删除 `source_refs` 字段本身
- 不要把多条 source_ref 合并成一条

## dry-run 清单格式

清单文件输出到：

```
60_feedback/taxonomy-migration-2026-06-27/source-refs-dryrun.csv
```

CSV 列：

| 列名 | 说明 |
|:---|:---|
| `file_path` | 引用该 source_ref 的卡片路径 |
| `card_id` | 卡片 id |
| `current_source_ref` | 当前 source_refs 条目原文 |
| `file_exists` | `true` / `false` |
| `suggested_action` | `fix_path` / `downgrade_to_src_unknown` / `manual_review` |
| `suggested_value` | 建议修正后的值 |
| `reason` | 判定理由（1 句话） |

同时输出一个摘要 Markdown：

```
60_feedback/taxonomy-migration-2026-06-27/source-refs-dryrun-summary.md
```

包含：

- 总检查条目数
- 文件存在数 / 不存在数
- 按 `suggested_action` 分类统计
- Top 10 最常见的不存在 source_ref 模式
- 需要人工判定的清单（如有）

## 执行步骤

1. **扫描**：遍历 `30_wiki/**/*.md`，读取 `source_refs`
2. **判定**：按上述规则分类
3. **输出**：生成 CSV 清单 + Markdown 摘要
4. **提交**：把清单文件交给欧阳锋审阅
5. **等待**：欧阳锋审批后，按清单 apply

## 注意

- 这是**清查任务**，不是立即修改任务。在欧阳锋说"apply"之前，只出清单。
- 如果扫描过程中发现新的系统性模式（如某一批卡都引用了同一个不存在的目录），在摘要里单独标出。
- 有任何疑问立即停止，报欧阳锋。

## 关联任务

- 已完成：`70_product/tasks/...`（taxonomy 目录迁移，待黄药师归档）
- 后续：dark-knowledges section 缺失补全（分配给老顽童，待定）
