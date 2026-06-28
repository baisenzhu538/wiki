---

id: dk-f2-txt-ingest-skip
title: F-KDO-002：非 .md 文件 ingest 静默跳过→state.json 无变化但用户以为成功
type: dk
dark_knowledge_type: failure
status: reviewed
domain:
- master
source_person: system
source_context: failure-modes.md F-KDO-002
source_refs:
- src_unknown
created_at: 2026-05-31
updated_at: '2026-06-28'
related:
  - [[dk-c1-cjk-regex-silent-fail]]
  - [[kdo-input-channel-strategy-2026-06-16]]
  - [[kdo-protocol]]
  - [[modeling-to-kdo-toolchain]]
  - [[kdo-batch-produce-req014]]
  - [[kdo-15-dimension-label-spec]]
  - [[obsidian-kdo-内容产出工作流-产品设计大纲]]
  - [[tool-月白-课程资料文件命名规范]]
pipeline:
- src_unknown
- src_unknown
- src_unknown
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.7
trust_level: low
review_date: '2026-06-28'

---

## 原始表述

> **触发命令**：`kdo ingest`
>
> **表现**：对 `.txt` 文件：无输出、无报错、state.json 无变化、无源文件创建。用户以为 ingest 成功了。
>
> **根因**：`kdo ingest` 只扫描 `00_inbox/*.md`，其他扩展名被静默忽略
>
> **触发信号**：`ls 10_raw/sources/` 没有新文件产生；state.json 的 `ingested_inbox_files` 列表无新增
>
> **防御措施**：ingest 完成后：① 打印实际处理的文件数量 ② 对 `00_inbox/` 中剩余的非 .md 文件给出 warning ③ 建议在 ingest 前跑 `find 00_inbox -type f` 确认所有文件都是 .md
>
> **临时绕过**：`cp file.txt file.md && rm file.txt` 后重新 ingest
>
> **关联文件**：`kdo/commands/ingestion.py`

## 深度洞察

KDO ingest 的"静默跳过"不是 bug，而是**设计选择**：扩展名白名单只包含 `.md`，对不符合条件的文件选择不处理、不报错、返回 exit code 0。这种选择在流水线场景下非常危险——它把"是否处理"的验证责任完全推给了用户。用户一旦把 `.txt`、`.docx`、`.pdf` 等原始素材直接丢进 `00_inbox/`，就会得到一次"伪成功"的运行：命令结束、日志干净、状态码正常，但知识库没有任何变化。更隐蔽的是，如果 `00_inbox/` 中同时存在 `.md` 和 `.txt`，只有 `.md` 被处理，`.txt` 被默默落下，用户很容易把"部分成功"误判为"全部成功"。

这条暗知识的核心不是"怎么转格式"，而是：**任何返回 0 的 CLI 命令都不能替代对输出状态的实质性验证**。在 KDO 的语境里，实质性验证就是比较 `00_inbox/` 的输入清单与 `state.json` / `10_raw/sources/` 的输出清单。

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **检查文件扩展名**：运行 ingest 前，先 `find 00_inbox -type f` 确认所有文件都是 `.md` 格式
2. **非 .md 文件先转换**：对 `.txt` 文件执行 `cp file.txt file.md`，然后再运行 `kdo ingest`
3. **批量处理脚本**：如果文件量大，用循环自动转换——`for f in 00_inbox/*.txt; do cp "$f" "${f%.txt}.md"; done`
4. **验证 state.json**：ingest 完成后检查 `state.json`，确认 `ingested_inbox_files` 列表有新增
5. **读取骨架验证**：打开自动生成的 wiki 页面，确认内容没有被碎片化（特别是 CJK 内容，参见 [[dk-c1-cjk-regex-silent-fail]]）
6. **建立入口检查清单**：在 CI 或本地 hook 中加入"Ingest 前非 .md 文件拦截"步骤

## 诊断信号

| Signal | Lens | Follow-up |
|:
----|:-----|:----------|
| `kdo ingest` 执行后终端无任何 per-file 输出，只有空白或极简 summary | 可能是所有输入文件都被扩展名白名单过滤掉了 | 立即执行 `find 00_inbox -type f ! -name '*.md'`；若有非 .md，按操作方法转换后重跑 |
| `state.json` 的 `ingested_inbox_files` 计数在 ingest 前后没有变化 | 新素材未被实际写入知识库 | 比对 `10_raw/sources/` 最新文件时间戳与 `00_inbox/` 输入文件；定位缺失项 |
| `10_raw/sources/` 中没有与 `00_inbox/` 文件同名（除扩展名外）的新文件 | 该文件被静默跳过 | 检查文件扩展名；确认是否只支持 `.md`；转换后重新 ingest |
| ingest 日志显示"成功"但 `00_inbox/` 中仍有 `.txt`、`.docx`、`.pdf` 等残留 | CLI 只处理了 .md，其余被忽略 | 清理或转换残留文件；将"扩展名检查"加入标准 SOP |

## 适用边界

| 边界 | 说明 |
|:-----|:------|
| ✅ 适合 | KDO CLI 默认 `kdo ingest` 流程，且输入目录 `00_inbox/` 中混有 `.txt` 等非 .md 文件的场景 |
| ❌ 不适合 | `.docx`、`.pdf`、`.html`、图片等富媒体格式——需要专用转换脚本，不能简单改扩展名 |
| ❌ 不适合 | 已使用自定义 ingest 插件或修改 `ingestion.py` 扩展名白名单的情况——行为由插件自身决定 |
| ❌ 不适合 | 非 KDO CLI 环境（如直接用 Obsidian、Git 手动复制文件）——本暗知识只针对 `kdo ingest` |
| ⚠️ 需人工干预 | 即使 `.txt` 已改为 `.md`，若内容完全无结构，仍需补充 frontmatter 和结构化标记 |

### 常见失败模式

| 失败模式 | 真实症状 | 可执行修复 |
|:---------|:---------|:-----------|
| 盲目信任 exit code 0 | 命令返回成功，但 `state.json` / `10_raw/sources/` 没有任何新增 | 强制做"输入-输出"对账：`find 00_inbox -type f` 计数 vs `ingested_inbox_files` 增量 |
| 批量脚本未做扩展名过滤 | `00_inbox/` 中 `.md` 与 `.txt` 共存，只有 `.md` 被处理，`.txt` 被落下 | ingest 前运行 `find 00_inbox -type f ! -name '*.md' -print`；全部转换后再跑 ingest |
| 改扩展名但未补 frontmatter | 转换后的 `.md` 被 ingest，但生成的 wiki 页面缺少 title/type/source，成为孤儿页面 | 转换时同时写入最小 frontmatter：`---\ntitle: ...\ntype: source\nsource_id: ...\n---` |
| 缺少监控导致事后才发现数据丢失 | 数天后回溯素材时发现某些 `.txt` 从未进入知识库，原始文件已被清理 | 每次 ingest 后保存 `state.json` diff；建立"非 .md 残留数"监控指标 |

## 案例：工厂层 txt 跳过事故复盘

**背景**：2026-05-03，Builder 将 12 份口述稿素材放入 `00_inbox/`，其中 8 份为 `.md`，4 份为 `.txt`。运行 `kdo ingest` 后，终端显示成功退出，日志无报错。

**发生了什么**：
- src_unknown
- src_unknown
- src_unknown

**结果**：4 份口述稿永久丢失，相关 wiki 页面被迫标注为 `source_missing`。

**可迁移教训**：
- src_unknown
- src_unknown
- src_unknown

## Ingest 前检查清单

```markdown
□ 运行 `find 00_inbox -type f`，确认所有待处理文件扩展名均为 `.md`
□ 若存在 `.txt`，执行 `for f in 00_inbox/*.txt; do cp "$f" "${f%.txt}.md"; done`
□ 对转换后的 `.md` 补充最小 frontmatter（title / type / source_id）
□ 运行 `kdo ingest`
□ ingest 后检查 `.kdo/state.json`：确认 `ingested_inbox_files` 数量增加
□ 检查 `10_raw/sources/`：确认每个输入文件都有对应输出
□ 读取自动生成的 wiki 骨架：确认 CJK 内容未出现碎片化（参见 [[dk-c1-cjk-regex-silent-fail]]）
```

## 为什么值钱

- src_unknown
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
- src_unknown

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
