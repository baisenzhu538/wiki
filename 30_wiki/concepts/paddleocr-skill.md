---
title: "PaddleOCR — 本地+云端双模 OCR 识别 Skill"
type: concept
status: enriched
domain: ['master']
source_refs: []
created_at: "2026-05-07"
updated_at: "2026-05-07"
related:
  - "[[web-scraping-三剑客-scrapling-crawl4ai-firecrawl]]"
  - "[[tinyfish-agentic-web-infrastructure]]"
  - "[[KDO Protocol]]"
tags:
  - "#skill"
  - "#ocr"
  - "#tool"
  - "#paddleocr"
  - "#document-parsing"
trust_level: high
reviewed_by: "黄药师"
review_date: "2026-05-07"
---

# PaddleOCR — 本地+云端双模 OCR 识别 Skill

> 百度 PaddlePaddle 出品，GitHub 74K+ stars，PP-OCRv5 中文准确率 ~97.8%，覆盖 80+ 语言。已安装 2 个官方 Claude Code Skill。

## Summary

PaddleOCR 是目前中文 OCR 领域事实标准。官方提供了 2 个 Claude Code Skill：文本识别（线级文字提取）和文档解析（版面/表格/公式/印章/图表结构化还原）。两个 Skill 采用同一架构：SKILL.md + PEP 723 内联依赖脚本（uv 自动解析），需 PaddleOCR API Key。

与此同时，黄药师已在本地部署 PaddleOCR Python 库，可直接通过 Python API 调用，无需 API Key。

---

## [Condense] 核心架构

### 两个 Skill 的分工

| Skill | 做什么 | 输入 | 输出 | 触发词 |
|-------|--------|------|------|--------|
| **paddleocr-text-recognition** | 线级文字提取，可带 bbox 坐标 | 图片/截图/扫描件/PDF | 纯文本 + 每行坐标 | OCR、文字识别、图片转文字 |
| **paddleocr-doc-parsing** | 文档结构完整还原（表格/公式/图表/印章/页眉页脚/多栏/阅读顺序） | PDF/文档图片/复杂排版 | Markdown/JSON（含LaTeX公式、HTML表格） | 文档解析、版面分析、表格提取、公式识别 |

### 使用策略（决策树）

```
用户给图片/PDF
├── 只需要纯文字？
│   └── paddleocr-text-recognition ✅
├── 有表格/公式/印章/多栏排版？
│   └── paddleocr-doc-parsing ✅
├── 本地有 Python 环境且无 API Key？
│   └── 本地 Python API 直接调用 ✅
└── 有 API Key 且需要最快速度？
    └── uv run scripts/ocr_caller.py ✅
```

### 本地 Python API（黄药师已部署）

```python
from paddleocr import PaddleOCR

# 文字识别
ocr = PaddleOCR(lang='ch', ocr_version='PP-OCRv5')
result = ocr.predict("image.jpg")
for res in result:
    res.print()       # 打印结果
    res.save_to_json("output/")  # 保存 JSON

# 文档结构解析
from paddleocr import PPStructureV3
pipeline = PPStructureV3(
    use_table_recognition=True,
    use_formula_recognition=True,
    use_chart_recognition=True,
    use_seal_recognition=True,
    lang='ch'
)
output = pipeline.predict("document.pdf")
for page in output:
    print(page.to_markdown())
```

### 云端 API（Skill 模式）

```bash
# 文字识别
uv run scripts/ocr_caller.py --file-path "image.png" --pretty

# 文档解析
uv run scripts/layout_caller.py --file-path "document.pdf" --pretty
```

需要环境变量：`PADDLEOCR_OCR_API_URL` + `PADDLEOCR_ACCESS_TOKEN`

### CLI 命令

```bash
# 命令行 OCR
paddleocr ocr -i image.jpg --lang ch --ocr_version PP-OCRv5

# 文档结构解析
paddleocr pp_structurev3 -i document.pdf --use_table_recognition True
```

---

## [Critique] 批判性评估

### 前提假设

- 假设云端 API 的识别质量与本地部署一致。【可靠性：高】云端使用相同模型 PP-OCRv5，且推理资源更充足
- 假设 Skill 的 PEP 723 内联依赖模式（uv run）在 WSL 环境下可用。【可靠性：中】需要 uv 已安装，WSL 网络环境可能影响首次依赖解析
- 假设 Document Parsing 的版面还原质量满足 KDO wiki 的转写需求。【可靠性：中】复杂多栏中文排版（如课程讲义）的阅读顺序仍有出错可能

### 边界与反例

- **最适合**：截图文字提取、发票/财报结构化、扫描件 OCR、课程 PPT 转写
- **不适合**：手写体（PP-OCRv5 对手写支持有限）、严重倾斜/变形文本、纯英文场景（有更轻量的方案）
- **关键限制**：Document Parsing 单次最多 100 页 PDF；大图需压缩后上传

### 与现有工具的关系

| 工具 | 层面 | 定位 |
|------|------|------|
| **PaddleOCR** | 视觉理解层 | 将图片/PDF 中的文字→可搜索/可编辑文本 |
| **TinyFish** | Web 操作层 | 将网页→结构化数据 |
| **Scrapling/Crawl4AI** | 爬虫层 | 将网页 HTML→文本 |
| **business-research** | 调研编排层 | 将这些能力编排为调研流程 |

### 可靠性

**整体：高。** PaddleOCR 是百度核心开源项目，74K+ stars，被 Dify 等主流项目集成。云端 API 经 40M+ 调用验证。本地部署的质量取决于模型版本和硬件。

---

## [Synthesis] 与 wiki 知识库的关联

- [[web-scraping-三剑客-scrapling-crawl4ai-firecrawl]] — PaddleOCR 补充了"图片/PDF→文本"这一环，之前整个工具栈只有"网页→文本"
- [[tinyfish-agentic-web-infrastructure]] — TinyFish 的 Fetch 端返回 Markdown，PaddleOCR 负责把 Fetch 拿不到的图片内文字提取出来。两者组合：TinyFish 获取页面 → PaddleOCR 识别嵌入图片
- [[business-research-skill-oscar-13-weapon-system]] — Step 3 在线采集时，遇到图片形式的财报/数据，可以用 PaddleOCR 提取结构化数据
- [[KDO Protocol]] — PaddleOCR 是第四个 tool 型 Skill，验证了 tool 型 Skill 的 pre-flight check 模式

### Skill 体系更新

| 类型 | Skill | 核心能力 |
|------|-------|---------|
| methodology | business-research | OSCAR + 13 武器调研 |
| persona | truman-perspective | 许楚思维模拟 |
| tool | use-tinyfish | Web Search/Fetch/Agent/Browser |
| tool | **paddleocr-text-recognition** | 图片/PDF → 线级文本 |
| tool | **paddleocr-doc-parsing** | 文档 → 结构化 Markdown/JSON |

## Open Questions

- 本地 PaddleOCR 部署的具体路径和可用模型版本？
- PADDLEOCR_API_URL 和 ACCESS_TOKEN 是否已配置？
- 本地部署 vs 云端 API 在 KDO wiki 转写场景中的速度和成本差异？
- PP-StructureV3 对中文课程讲义的表格/公式还原效果如何？

## Output Opportunities

- **KDO capture 增强**：PaddleOCR 作为 `kdo capture` 的图片预处理插件——截图自动 OCR 后存入 inbox
- **business-research 集成**：Step 3 遇到图片财报/数据截图时自动调用 PaddleOCR 提取
- **TinyFish + PaddleOCR 组合**：Fetch 获取页面 → PaddleOCR 识别嵌入图片 → 完整 Markdown
