---
title: "黄药师 Sprint 4 数据卫生批修报告"
author: "黄药师"
created_at: "2026-05-24"
status: "completed"
sprint: "Sprint 4"
reviewer: "欧阳锋"
---

# Sprint 4 数据卫生批修报告

## 执行摘要

Sprint 4 共三个任务，全部完成。**未删除任何卡片，未丢失任何内容。** 所有操作均为文件内部修改（标题重命名、路径格式修正、重复段落合并）。

验证：操作前后卡片总数均为 375 张，`git diff --name-status` 显示 0 个 Deleted 文件。

---

## Task 21：断链批量修复

**问题**：~113 个 broken wikilinks（指向不存在目标 或 路径格式错误）

**执行**：
1. 扫描全库 wikilinks，分类为两种：
   - **无效链接**（目标文件不存在且非 aspirational forward reference）：26 个 → 移除
   - **路径格式错误**（如 `[[30_wiki\concepts\file.md]]` 应为 `[[file]]`）：2097 个 → 修正为 Obsidian 标准格式
2. 修正逻辑：剥离目录路径和 `.md` 后缀，只保留文件 stem 作为 wikilink 名称

**结果**：
- 移除：26 个无效链接
- 修正：2097 个路径格式链接
- index.md 验证：0 个反斜杠残留，393 个干净 wikilinks

**未删除任何文件。** 仅修改了文件内部的 `[[...]]` 文本。

---

## Task 22：frontmatter 批量补全

**问题**：原估计 ~271 张卡缺失 frontmatter 字段（title, type, status, created_at）

**执行**：
1. 用 YAML safe_load 诊断 → 报告 57 张"缺失"
2. 深入排查发现：这 57 张卡的 frontmatter 实际**完整**，是 YAML 解析器在遇到复杂内容（长列表、特殊字符、query_triggers 等）时崩溃，导致整个 frontmatter 返回空 dict 的**误报**
3. 改用 regex 验证：所有 370 张卡均已具备 title、type、status、created_at 且值非空

**结果**：无需修改。原始估计基于有缺陷的检测方法。

**未修改任何文件。**

---

## Task 23：新旧格式统一

**问题**：卡片内部存在新旧标题格式并存（如 `## [Condense]` 与 `## Critique` 同卡共存；重复的 `## Visual Analysis` 等）

**执行**（严格遵守 C-10 铁律：单卡 dry-run → 单卡 write → 验证 → 批量）：

### Pass 1：旧括号标题重命名（20 张管理/模型卡）

| 旧格式 | 新格式（v1.5标准） |
|--------|-------------------|
| `## [Condense]` | `## Claims` |
| `## [Critique]` | `## Critique` |
| `## [Synthesis]` | `## Synthesis` |

这些卡使用的是早期"三步编译法"括号标题。内容100%保留，只改标题名。

### Pass 2：重复段落移除（7 张泛产品卡）

这些卡内部有完全一模一样的段落出现两次（如两个相同的 `## Visual Analysis` + `## Constraints & Boundaries`，内容逐字重复）。保留第一个，移除重复副本。

涉及卡片：yt-model-pan-product-36-strategies, yt-model-pan-product-aesthetic-toolkit, yt-model-pan-product-climbing-map, yt-model-pan-product-demand-toolkit, yt-model-pan-product-execution-toolkit, yt-model-pan-product-three-virtues, yt-panproduct-demand-five-step-method

### Pass 3：研究卡括号标题修正（26 张）

与 Pass 1 相同逻辑，覆盖 `kdo enrich` 生成的研究卡（如 `## [Condense] 核心观点` → `## Claims`）。其中 12 张在重命名后产生了同名段落碰撞（卡内原本已有 `## Synthesis`，又有 `## [Synthesis] 对比迁移` 被重命名为 `## Synthesis`），通过合并两段内容解决。

### 特殊处理：web-scraping 卡

该卡有多个 `## [Condense]` 子主题段落 → 第一个改为 `## Claims`，后续改为 `### 子标题`（降为 H3）。

**结果**：
- 修改卡片数：53 张（文件内部标题修改，无文件删除）
- 混合格式卡剩余：0 张（验收标准 <10）
- 卡片总数不变：375 张

---

## 关键声明：无卡片被删除

| 指标 | 操作前 | 操作后 |
|------|--------|--------|
| `30_wiki/concepts/*.md` 文件数 | 375 | 375 |
| git deleted files | — | 0 |
| 内容丢失 | — | 无 |

所有操作均为：
1. 文件内部 wikilink 文本修改（Task 21）
2. 无操作（Task 22）
3. 文件内部 H2 标题重命名 + 重复段落合并（Task 23）

**没有任何 `rm`、`git rm`、或文件删除操作。**

---

## 验证方法

如需复查，可执行：

```bash
# 确认卡片数量
ls 30_wiki/concepts/*.md | Measure-Object

# 确认无删除操作
git diff --name-status 30_wiki/concepts/ | Select-String "^D"

# 确认格式统一结果
python -c "
import re
from pathlib import Path
mixed = 0
for f in Path('30_wiki/concepts').glob('*.md'):
    text = f.read_text(encoding='utf-8', errors='replace')
    h2s = re.findall(r'^## (.+)$', text, re.MULTILINE)
    if any(h.startswith('[') for h in h2s):
        mixed += 1
    dupes = [h for h in set(h2s) if h2s.count(h) > 1]
    if dupes:
        mixed += 1
print(f'Mixed-format remaining: {mixed}')
"
```
