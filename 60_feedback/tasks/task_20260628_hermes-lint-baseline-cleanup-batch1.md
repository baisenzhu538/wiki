---
id: task_20260628_hermes-lint-baseline-cleanup-batch1
type: task
status: queued
assignee: Hermes 老顽童
priority: P1
created_at: 2026-06-28
updated_at: 2026-06-28
reviewer: 欧阳锋
source_refs:
- 60_feedback/auto/health-check-2026-06-27.md
- 90_control/.tmp/hermes_lint_safe_batch.json
- 90_control/.tmp/hermes_lint_unsafe_batch.json
---

# Hermes 老顽童 lint 基线清理（Batch 1）：机械性 frontmatter 修复

## 任务目标

把全库 lint ERROR 中**可以机械修复、不改动正文内容**的 659 个文件处理掉。
不追求内容补全（如 src_unknown 占位、正文缺 section 等），只修复 frontmatter 语法错误，让 `kdo lint` 不再因格式问题报错。

## 背景

- 2026-06-27 健康巡检显示新卡健康度 `715F / 2081W`。
- 其中 659 个 FAIL 属于**已知复制粘贴失败模式**， Hermes 可以安全处理；剩余 128 个为需要人工判断或内容补全的复杂错误，**不纳入本次任务**。
- 本次任务结束后，预期全库 lint ERROR 从 697 降至约 128（+ 少量 residual）。

## 任务范围

**只处理以下 5 类 frontmatter 机械错误**（已导出到 `90_control/.tmp/hermes_lint_safe_batch.json`）：

| 错误类型 | 数量 | 典型表现 | Hermes 修复方式 |
|:---|---:|:---|:---|
| `colon_in_scalar_list_item` | 336 | 列表项后紧跟缩进的 `framework_lens:` / `lens:` / `dimensions:` / `relation:` 等键，导致 YAML 把上层标量误解析为 mapping key | 把缩进键改为列表项对象的子字段：`- src_unknown` → 删除或改为 `- id: ...`；如果 `src_unknown` 后面有 `framework_lens`，应把 `src_unknown` 替换为真实字段名，或整体改为 `- lens: ...` 格式。详见下方「修复规则」。 |
| `body_leak_into_frontmatter` | 260 | 正文 `# 标题`、`>` 引用块、`|` 表格等 Markdown 内容漏进 frontmatter，通常是因为 `---` 结束符缺失或 frontmatter 最后一行与正文粘在一起 | 在 frontmatter 与正文之间补上正确的 `---\n` 分隔；把正文内容移回 body。**禁止删除正文内容**。 |
| `expected_colon` | 38 | YAML 期望 `:` 但没找到，常见是 frontmatter 里出现裸 Markdown 行、列表项后面漏了键 | 检查 frontmatter 结尾；如果是正文泄漏，按 `body_leak` 处理；如果是列表项格式错误，修正为合法 YAML。 |
| `no_closing_separator` | 24 | frontmatter 只有开头的 `---`，没有闭合的 `---`，导致 YAML 把正文也吞进去 | 在 frontmatter 最后一行与正文 `# 标题` 之间插入 `---\n`。 |
| `indent_or_list_error` | 1 | 列表缩进不一致或 block mapping 结束符缺失 | 按 YAML 语法修正缩进。 |

**不处理**（已导出到 `90_control/.tmp/hermes_lint_unsafe_batch.json`，共 128 个）：
- `colon_in_scalar_other`：标量内部含 `:` 且不在列表项上下文，可能需要加引号或重写句子。
- `no_frontmatter_start`：如 `index.md`、`concept-card-index-latest.md` 等系统生成索引，非卡片内容。
- 任何需要补全正文、补 source_refs、补 related、调整 domain 等**内容判断**的工作。

## 修复规则（必须遵守）

### 规则 1：不改动正文
- 只能调整 frontmatter（`--- ... ---` 之间的 YAML）。
- 正文段落、标题、列表、代码块、wikilink 一律保留。
- 如果正文内容错误地出现在 frontmatter 里，把它**移回正文**而不是删除。

### 规则 2：`src_unknown` 占位不补内容
- 本次任务不查素材、不补 source_refs / related / tags / query_triggers。
- `src_unknown` 可以保留；只需让 YAML 能解析。

### 规则 3：修复 `colon_in_scalar_list_item`
这是最常见错误。frontmatter 中形如：

```yaml
diagnostic_signals:
- src_unknown
  framework_lens: 某个 lens 文本
  follow_up_question: 某个问题
```

YAML 会把 `src_unknown` 后面的 `framework_lens:` 误解为 `src_unknown` 的 value。

**标准改法**是把 `- src_unknown` 替换为字段名本身，例如：

```yaml
diagnostic_signals:
- framework_lens: 某个 lens 文本
  follow_up_question: 某个问题
```

如果同一列表里既有 `- src_unknown` 占位、又有真实内容，只保留真实内容字段：

```yaml
# 错误
- src_unknown
  framework_lens: X
  follow_up_question: Y

# 正确
- framework_lens: X
  follow_up_question: Y
```

如果 `lens:` / `framework_lens:` 后面跟着中文冒号 `：` 或包含 `:` 字符，**不要改成英文冒号**，而是给整个标量加双引号：

```yaml
- lens: "商业模式: B2B vs B2C"
```

### 规则 4：修复 `body_leak_into_frontmatter`
典型症状：frontmatter 最后一行后面直接跟着 `# 标题` 或 `>` 引用。

```yaml
tags:
- src_unknown
# 这是正文标题
```

应改为：

```yaml
tags:
- src_unknown
---
# 这是正文标题
```

注意：
- 有些文件 frontmatter 根本没有闭合 `---`，正文从第一行 `#` 开始；这种情况按规则 5 处理。
- 有些文件 frontmatter 内部出现 `>` 或 `|` 开头的 Markdown 行，说明正文泄漏进 frontmatter；把这些行移出 frontmatter。

### 规则 5：修复 `no_closing_separator`
文件以：

```yaml
---
id: ...
related:
- [[...]]
# 标题
```

应改为：

```yaml
---
id: ...
related:
- [[...]]
---
# 标题
```

### 规则 6：`expected_colon` 检查清单
1. 先看是否正文泄漏；是 → 按规则 4。
2. 再看是否是列表项后面跟了子字段但 `- src_unknown` 未合并；是 → 按规则 3。
3. 最后检查是否标量含 `:` 未加引号；是 → 加双引号。

## 执行步骤

1. **读取任务单**（本文件）和 `90_control/.tmp/hermes_lint_safe_batch.json`。
2. **按目录分批处理**，建议顺序：
   1. `30_wiki/dark-knowledges/`（156 个，body_leak 为主，最快）
   2. `30_wiki/tools/`（106 个）
   3. `30_wiki/concepts/`（244 个，最多，分 2 小批）
   4. `30_wiki/cases/`（63 个）
   5. `30_wiki/frameworks/`（45 个）
   6. 其他零散目录（`decisions/`, `systems/`, `entities/`, `_archive/`, `projects/`, `domains/`）
3. **每处理 50-100 个文件**，跑一次 `kdo lint --scope <目录>`（如支持）或 `kdo lint`（超时则用 `--limit` 或目录过滤）验证 ERROR 下降。
4. **每个文件改完后**用 `kdo pre-submit -f <文件路径>` 或 Python `yaml.safe_load()` 验证 frontmatter 可解析。
5. **完成后**：
   - 把本任务单 `status` 改为 `pending_review`。
   - 在 `production-queue.md` 中把对应条目状态改为 `pending_review`。
   - 释放队列锁。

## 验证标准

- 任务单中 659 个文件的 frontmatter 必须通过 `yaml.safe_load()`。
- 这些文件在 `kdo lint` 中不再产生 `missing or unparseable frontmatter` 类 ERROR。
- 正文内容不能被删除或改写。

## 禁止事项

- 不要改 `90_control/.tmp/hermes_lint_unsafe_batch.json` 中的 128 个文件。
- 不要补全 `src_unknown` 占位的内容（除非只是 YAML 语法需要把它删掉或合并）。
- 不要重写卡片标题、summary、claims。
- 不要修改 reviewed / enriched 等状态字段（除非原来就是错的）。

## 输出要求

完成时提交一份简短报告到本任务单末尾：

```markdown
## 执行报告

- 处理文件数：659
- 修复类型分布：colon_in_scalar_list_item=336, body_leak_into_frontmatter=260, expected_colon=38, no_closing_separator=24, indent_or_list_error=1
- 跑 `kdo lint` 后全库 ERROR：XXX（应 ≈128）
- 残余未处理：128 个 unsafe 文件（见 hermes_lint_unsafe_batch.json）
- 备注：...
```

## 关联文件

- `90_control/.tmp/hermes_lint_safe_batch.json` — 本次要处理的 659 个文件及错误类型
- `90_control/.tmp/hermes_lint_unsafe_batch.json` — 本次不处理的 128 个文件及原因
- `60_feedback/auto/health-check-2026-06-27.md` — 原始健康巡检报告
