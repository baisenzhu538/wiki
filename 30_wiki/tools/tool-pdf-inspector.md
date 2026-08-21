---
id: tool-pdf-inspector
title: PDF-Inspector (Firecrawl)：先分类再提取的极速 PDF→Markdown 解析器
type: tool
status: pending_review
author: 小昭（外部建议稿），老顽童核验入库
reviewed_by: pending
created_at: 2026-08-21
updated_at: 2026-08-22
confidence: 0.9
trust_level: high
language: zh-CN
domain: knowledge-management
aliases:
  - PDF-Inspector Firecrawl 极速 PDF 解析器
  - pdf-inspector PDF 转 Markdown
  - 先分类再提取 PDF 解析
  - Firecrawl PDF Inspector
source_refs:
  - https://github.com/firecrawl/pdf-inspector
  - https://pypi.org/project/pdf-inspector/
  - https://www.firecrawl.dev/blog/anydoc-and-pdf-inspector
discoverable_by:
  - PDF-Inspector Firecrawl 极速 PDF 解析器
  - pdf-inspector PDF 转 Markdown
  - 先分类再提取 PDF 解析
related:
  - '[[mineru-pdf-parsing-setup]]'
  - '[[tool-agent-crawl4ai]]'
tags:
  - audience:executor
  - scene:execution
  - skill-level:intermediate
  - pdf
  - rag
  - ingestion
diagnostic_signals:
  - framework_lens: PDF 进料检查
    follow_up_question: 这份 PDF 是原生文本还是扫描件？先 `detect-pdf` 分类再决定走本地直提还是送 OCR。
---

# PDF-Inspector (Firecrawl)

> 本卡是 KDO PDF 进料 classify-then-route 路由的"快速通道"工具卡：先用 `detect-pdf` 判断 PDF 类型（原生文本/扫描/图片/混合），原生文本型本地直提（官方口径 under 200ms），扫描/混合页才路由去 OCR/MinerU。与 [[mineru-pdf-parsing-setup]] 互补不替代（MinerU 管扫描件/复杂版面）。

> 纯 Rust、MIT 开源。核心思想：**先判断"这份 PDF 到底要不要 OCR"，再决定怎么转**。原生文本型直接本地提取（官方口径 under 200ms），扫描件/图片才路由去 OCR，混合型只把缺文本层的那几页送去 OCR。对 RAG / Agent 进料、批量 PDF 入库特别合适。

> 数字核验（2026-08-22 老顽童，官方源=PyPI 官方 description 即 GitHub README 镜像，GitHub 直连超时）：0.470s / 54% / 10–50ms / 0.788vs0.811 四项 VERIFIED；"~150ms" 官方未写（官方口径 under 200ms），已修正。

## 为什么需要它（vs MinerU / 盲跑 OCR）

现实里约 **54%** 的 PDF（Word 导出、报告、发票）本来就带文本层，却被很多流程拿 OCR 逐像素"看"一遍，纯属浪费时间和 token。pdf-inspector 在提取前加一个 **10–50ms 的分类判断**，直接砍掉一大半无谓的 OCR 等待。

这与 KDO 已收录的 [[mineru-pdf-parsing-setup]]（MinerU）是**互补**关系，不是替代：

| 维度 | pdf-inspector | MinerU (magic-pdf) |
|:---|:---|:---|
| 定位 | 原生文本 PDF 的**极速直提** | 扫描件 / 复杂版面的 **OCR + 视觉还原** |
| 速度 | 200 个 PDF 0.47s（官方 benchmark，opendataloader-bench 语料，本地无模型） | 需加载 2–4GB 模型，慢得多 |
| OCR | **不做**（只分类，扫描件交出去） | 做（本地推理） |
| 适用 | 文本型报告 / 文档 / 发票批量入库 | 扫描档案 / 多栏论文 / 复杂表格 |
| 依赖 | 纯 Rust，单依赖 lopdf | torch/transformers/PyMuPDF，需 WSL |

**KDO 进料默认策略**：先用 `detect-pdf` 分类 → 文本型走 pdf-inspector 本地直提（快、省 token）→ 扫描/混合型把标出的页送 MinerU 或 OCR。这就是 KDO 的 classify-then-route 路由。

## 安装步骤

四种入口，按使用场景选：

```bash
# 1) Python（KDO 流水线、数据处理、Agent 后端，推荐）
pip install pdf-inspector

# 2) CLI（测试 / 批处理 / shell 管道，需 Rust 工具链）
cargo install pdf-inspector
# 装完得到两个命令：pdf2md / detect-pdf

# 3) Node.js（服务端 / JS 文档管道）
npm install @firecrawl/pdf-inspector

# 4) 浏览器 / Web Worker（WASM，文件不出本机）
npm install @firecrawl/pdf-inspector-wasm
```

> 实测（2026-08-21 黄药师狗粮，`wiki/_tmp/pdf-inspector/` venv，Python 3.12.3）：`pip install pdf-inspector` 装到 1.15.0，导入正常，`process_pdf` 可用。5 份 KDO 真实 PDF 狗粮 5/5 通过——全部正确分类 `text_based`（conf 0.875–1.0），耗时 0.2–0.42s/份，中文无乱码；其中 2 份正确标出混合页（`pages_needing_ocr: [27]` / `[18]`），供 classify-then-route 路由。注意 PDF 专有 WASM 版只处理 PDF；如需 Word/PPT/Excel 等 14 种格式统一转 Markdown，Firecrawl 同门 `anydoc` 底层 PDF 引擎用的就是它。

## 使用

### 先分类（路由判断，10–50ms）

```bash
detect-pdf document.pdf --json
# 返回：pdf_type (text_based|scanned|image_based|mixed) + confidence + pages_needing_ocr
```

### 再提取（转 Markdown）

```bash
pdf2md document.pdf > document.md            # 基础转换
pdf2md document.pdf --compact                # 压缩点线表等填充，省 token
pdf2md document.pdf --pages                  # 插入页码标记，便于溯源
pdf2md document.pdf --select-pages 1,3,5-10  # 只处理指定页
```

### Python（Agent 友好）

```python
import pdf_inspector
result = pdf_inspector.process_pdf("document.pdf")
print(result.pdf_type)    # "text_based" / "scanned" / "image_based" / "mixed"
print(result.markdown)    # Markdown 字符串，或 None（扫描件直提为空）
```

### classify-then-route 模板（KDO 批量进料）

```python
import pdf_inspector, subprocess

def route(pdf_path, ocr_for_scan="magic-pdf"):
    r = pdf_inspector.process_pdf(pdf_path)
    if r.pdf_type == "text_based":
        return r.markdown                      # 本地直提，0 OCR 成本
    if r.pdf_type == "mixed":
        # 只把 pages_needing_ocr 标出的页送 OCR，其余本地直提
        return hybrid_extract(pdf_path, r.pages_needing_ocr)
    # scanned / image_based → 整体送 MinerU / OCR 服务
    return subprocess.run([ocr_for_scan, "-p", pdf_path], ...)
```

## 接入 KDO 流水线

pdf-inspector 适合作为 KDO **PDF 进料的默认快速通道**，尤其契合以下两个真实场景：

1. **知识工厂文档入库（daily-capture-flow / labeling-pipeline）**：偶遇的 PDF 资料先过 `detect-pdf`，文本型秒级进库，避免每条都排队上 OCR。
2. **10TB 设计师素材库中的 PDF/画册/折页文件**：那批文件里大量是 Word/AI 导出的原生文本 PDF，用 pdf-inspector 先筛一遍，能省下可观的 OCR 排队与 token；只有扫描版才回落到 MinerU。

接入方式：在 黄药师 Builder 的进料脚本里把 `detect-pdf` + `pdf2md --compact --pages` 设为 PDF 类型文件的默认预处理节点，扫描/混合页再转交 MinerU。输出 Markdown 带页码标记，下游分块和引用都能溯源到原页。

## 失败模式 / 边界

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| 扫描件直提为空 | `pdf_type=scanned`，markdown 为 None | 必须走 MinerU / OCR，pdf-inspector 故意不做 OCR |
| 多栏论文阅读顺序乱 | 学术多栏排版串行错乱 | 多栏复杂版面用 Docling / Marker 更准确 |
| 标题层级偏弱 | heading 识别分 0.788，低于 liteparse 0.811（官方 benchmark） | 依赖标题层级的下游加一次校验 pass |
| 编码损坏页 | CJK Type0/Identity-H 偶发乱码 | 标出页回落 OCR（用 `--items-json` 定位） |

- **PDF-only**：不处理 Word/PPT/Excel/图片，多格式统一转换用 `anydoc`。
- **无内置 OCR**：它负责"判断 + 文本直提"，OCR 是外部环节。

## 质疑

**Doug Cutting**（Lucene/Nutch/Hadoop 创始人）会质疑：pdf-inspector 以"本地零模型、极致速度"为卖点，但在需要版面语义深度理解的场景（嵌套表格、公式、多栏论文），它刻意放弃的视觉模型恰恰是准确率的关键——用速度换精度的边界，在哪里开始反噬质量？

- **具体假设**：它假设"采样内容流判断文本/图像操作符"足以区分是否需要 OCR，但加密 PDF、残缺文本层、半扫描半排版的灰区文档，分类置信度会掉，误判会把该 OCR 的当文本直提（丢内容）或反之（浪费）。
- **边界**：对高价值、低容错文档（合同、医疗报告），纯文本直提的漏识风险可能超过省下的效率——这类应强制走 OCR 校验。
- **前提**：框架假设"先分类再路由"全局最优，但在文档类型高度单一的同质批次里，分类这一步本身是冗余开销（虽然 10–50ms 几乎可忽略）。
