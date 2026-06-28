---
id: task_20260628_huangyaoshi-lint-batch2-source-refs
type: task
status: queued
assignee: 黄药师
priority: P1
created_at: 2026-06-28
updated_at: 2026-06-28
reviewer: 欧阳锋
source_refs:
- 90_control/.tmp/lint_20260628_1620.log
- 90_control/.tmp/lint_batch2_source_refs.json
---

# lint Batch 2-C：source_refs 真实存在性清理（107 文件）

## 目标

修复 107 张卡片中 `source_refs` 指向不存在文件或格式错误的条目，使 `kdo lint` 不再报 `source_refs entry ...: file not found on disk` / `concept card has empty source_refs`。

## 问题分类

1. **合并写法**：一行里写两个文件路径，用 `-` 或 `空格` 连接，导致整条被视为一个不存在文件。
   - 例：`00_inbox/纪浩-AI协作方法论-口述.md - 00_inbox/AI俱乐部-人和AI协作-纪浩-参考案例-结构化.md`
   - 例：`00_inbox/一堂-产品内核验证课-Truman-口述.txt - 00_inbox/一堂-产品内核验证课-truman-笔记.txt`
2. **外部 URL**：`https://...` 被 lint 视为本地文件路径。
   - 例：`https://www.amazon.com/Structured-Analytic-Techniques-...`
   - 例：`https://www.langchain.com/blog/benchmarking-multi-agent-architectures`
3. **文件确实不存在**：hash 前缀对应的源文件已改名/删除/未 ingest。
   - 例：`src_20260606_640c2818-一堂-产品内核实操课-Truman-口述.md` 等大量引用
4. **concept 空 source_refs**：2 张 concept 卡 `source_refs` 为空列表。

## 规则

1. **合并写法**：拆分为独立 YAML 列表项。
2. **外部 URL**：
   - 若卡片内容确实来自该 URL，改为 `external_refs` 字段（如 schema 支持）或保留在 source_refs 但加引号并告知欧阳锋；
   - 若 lint 规则无法识别 URL，优先将 URL 移入正文 `## Sources` 段落或新增 `external_refs`。
3. **不存在的源文件**：
   - 先在 `10_raw/sources/`、`00_inbox/` 中搜索同名/同 hash 文件；
   - 能找到的修正路径；
   - 找不到的改为 `pending_archive` 占位，不凭空编造。
4. **空 source_refs 的 concept**：至少补一个 `pending_archive` 或真实源文件路径。
5. 不改动卡片正文内容，只调整 frontmatter 的 source_refs。

## 验证

- 全部 107 张卡 `kdo lint` 不再报 source_refs 相关 ERROR。
- 每张卡 `kdo pre-submit` 通过。

## 输出

完成后写执行报告：处理文件数、拆分条目数、URL 处置数、pending_archive 数、找到并修正的真实文件数。
