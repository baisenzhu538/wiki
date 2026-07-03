---
id: mineru-pdf-parsing-setup
title: MinerU (magic-pdf) PDF 解析工具安装与使用
type: tool
status: enriched
confidence: 0.75
trust_level: medium
domain:
- src_unknown
- src_unknown
source_refs:
- src_unknown
created_at: '2026-06-17'
updated_at: '2026-06-29'
author: 黄药师
reviewed_by: 王语嫣（代欧阳锋）
review_date: '2026-06-17'
related:
- '[[dk-wanghuan-magic-defeats-magic]]'
- '[[pending_unknown]]'
- '[[pending_unknown]]'
- '[[pending_unknown]]'
- '[[pending_unknown]]'
- tool-ban-fei-mao-an-yu-yi-qie-fen-wen-dang-zuo-xiang-liang-hua
tags:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
diagnostic_signals:
- framework_lens: MinerU 安装检查
  follow_up_question: 安装了 magic-pdf 吗？WSL 里执行 `pip show magic-pdf` 确认。
---
# MinerU (magic-pdf) PDF 解析工具

## 当前状态

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 安装步骤（新环境）

```bash
# WSL 内执行
pip install magic-pdf

# 下载模型（首次使用需要，约 500MB）
magic-pdf download_models
```

## 使用

```bash
# WSL 内执行，PDF 转 Markdown
magic-pdf -p "path/to/file.pdf" -o "output_dir" -m auto

# PNG 图片也可以
magic-pdf -p "image.png" -o "output_dir" -m auto
```

**注意**：必须在 WSL 内运行（Windows 未安装）。路径用 `/mnt/c/...` 访问 Windows 文件。

## 踩坑记录

1. **不要在 Windows 装** — magic-pdf 依赖 PyMuPDF/torch/transformers，Windows 兼容性差
2. **模型下载可能失败** — 如果 `download_models` 超时，手动从 HuggingFace 下载模型到 `~/.cache/magic-pdf/`
3. **内存占用** — 模型加载需要 2-4GB 内存，大 PDF 可能需要更多
4. **API key** — magic-pdf v1.3+ 需要 API key，获取方式见官方文档

## 目的

> 待补充：这个工具解决什么问题？适用于什么场景？

## 操作步骤

1. **步骤一**：待补充
2. **步骤二**：待补充
3. **步骤三**：待补充

## 不要用的场景

> 待补充：什么情况下这个工具效果有限或不应该使用？

## 质疑

> 待补充：这个工具的内在局限是什么？外部反对者会怎么批评？
