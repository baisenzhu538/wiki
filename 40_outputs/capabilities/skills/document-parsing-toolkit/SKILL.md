---
name: document-parsing-toolkit
title: Document Parsing Toolkit — 从 PDF/图片到结构化 Markdown 的引擎选型与管线
type: capability/skill
status: draft
description: >
  系统梳理从 PDF、课程截图、研报、论文中提取结构化 Markdown 的可用引擎：
  PaddleOCR.js（本地轻量）、PaddleOCR-VL（中文 SOTA）、MinerU 2.5（复杂中文文档）、
  Marker（英文学术 PDF）、多模态 AI Vision。含选型决策树、安装命令、输出格式对比。
triggers:
  - 需要从 PDF/图片提取表格、公式、多栏文字
  - 需要选择 OCR/文档解析引擎
  - 现有 PaddleOCR.js 输出混乱（表格串行、公式丢失）
  - 需要批量解析课程截图/研报/论文
source_refs:
  - "PaddleOCR-VL Technical Report (2026). https://ernie.baidu.com/blog/publication/PaddleOCR-VL_Technical_Report.pdf"
  - "MinerU: An Open-Source Solution for Precise Document Content Extraction (2024). https://arxiv.org/pdf/2409.18839"
  - "OmniDocBench v1.5 benchmark"
tags:
  - ocr
  - document-parsing
  - pdf-to-markdown
  - table-extraction
  - formula-recognition
---

# Document Parsing Toolkit

## 1. 一句话定位

把 **PDF / 图片 / 截图** 变成 **结构化 Markdown** 的引擎选型手册。不同引擎对应不同场景，选错引擎 = 表格变乱码、公式变图片、多栏文字串行。

---

## 2. 引擎矩阵（2026-06 现状）

| 引擎 | 类型 | 中文 | 表格 | 公式 | 多栏 | 速度 | 本地/云端 | 最佳场景 |
|:---|:---|:---:|:---:|:---:|:---:|:---|:---|:---|
| **PaddleOCR.js** | 本地 ONNX 流水线 | ⭐⭐⭐ | ❌ | ❌ | ❌ | 快 | 本地 | 短截图、纯文字、无网络 |
| **PaddleOCR-VL-0.9B** | 端到端 VLM | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | 快 | 本地/云端 | **中文文档首选，综合 SOTA** |
| **MinerU 2.5** | 多模型流水线 | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | 中等 | 本地 | 复杂中文 PDF/研报/课程 |
| **Marker** | 开源 PDF→MD | ⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ | 中等 | 本地 | 英文学术 PDF |
| **多模态 AI (GPT-4o/Qwen2.5-VL)** | 通用 VLM | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | 慢 | API | 复杂排版、需要语义理解 |

> **中文场景排序**：PaddleOCR-VL > MinerU 2.5 > 多模态 API > Marker > PaddleOCR.js

---

## 3. 详细引擎介绍

### 3.1 PaddleOCR.js（已有）

- **路径**：`C:\Users\Administrator\ocr-pipeline\`
- **入口**：`40_outputs/capabilities/skills/image-ocr/ocr-image.ps1`
- **适用**：纯文字截图、登机牌、发票、简短聊天记录
- **限制**：表格、公式、多栏、密集小字均不支持
- **坑**：`dict.txt` 不能 filter 空行，否则字符索引全偏

### 3.2 PaddleOCR-VL-0.9B（推荐升级）

2026 年新出的端到端文档解析 VLM，中文场景 SOTA。

| 指标 | PaddleOCR-VL | MinerU 2.5 | Qwen2.5-VL-72B |
|:---|:---:|:---:|:---:|
| OmniDocBench v1.5 Overall | **92.56** | 90.67 | 82.67 |
| 中文 OCR Edit Distance | **0.041** | 0.356 | 0.113 |
| 公式 CDM | **0.9453** | 0.9187 | 0.8747 |
| 参数量 | 0.9B | 1.2B pipeline | 72B |
| 推理速度 (A100) | **1.62 pages/s** | 1.06 pages/s | 慢 |

**优势**：小参数、快、中文极强、支持图表识别（饼图/柱状图/折线图/热力图）。

**安装**（待验证本地环境）：

```bash
pip install paddleocr-vl  # 包名待确认，先查官方仓库
# 或从源码
# git clone https://github.com/PaddlePaddle/PaddleOCR
```

### 3.3 MinerU 2.5

成熟的开源 PDF 解析流水线，阿里通义出品。

**组件**：
- 布局检测：LayoutLMv3 / DocLayout-YOLO
- 公式检测：YOLO-v8
- 公式识别：UniMERNet
- 表格识别：RapidTable / TableMaster / StructEqTable
- 文字 OCR：PaddleOCR
- 阅读顺序：LayOutReader

**安装**：

```bash
pip install magic-pdf[full]
```

**使用**：

```bash
magic-pdf -p input.pdf -o output_dir -m auto
# 或图片
magic-pdf -p input.png -o output_dir -m auto
```

**输出**：
- `output.md`：含表格、公式的 Markdown
- `output.json`：结构化元数据（区块类型、坐标、置信度）
- `images/`：提取的嵌入图片

### 3.4 Marker

专注英文学术 PDF 的开源解析器。

```bash
pip install marker-pdf
```

```bash
marker_single input.pdf --output_dir output_dir
```

### 3.5 多模态 AI Vision

当以上工具都搞不定时，直接用 GPT-4o / Qwen2.5-VL / Claude 3.7 Sonnet 等视觉模型。

**Prompt 模板**：

```text
请深度解析这张图片/PDF页面的全部内容：
1. 识别所有文字，包括小字号和密集文字；
2. 如果发现表格，用 Markdown 表格格式还原；
3. 如果发现公式，用 LaTeX 格式标注；
4. 如果发现清单/步骤/条目，用有序或无序列表还原；
5. 如果发现对比关系，说明对比维度；
6. 识别视觉标记（高亮、红框、颜色等）的语义含义；
7. 最终输出一份完整的结构化 Markdown 文档，保留原始层级和逻辑关系。
```

---

## 4. 选型决策树

```
输入类型
├── 纯文字短截图（无表格/公式/多栏）
│   └── PaddleOCR.js（本地、最快、免费）
├── 中文文档/课程截图/研报/教材
│   ├── 有 GPU 或愿意本地部署 → PaddleOCR-VL（推荐）
│   └── 想快速试用/复杂 PDF → MinerU 2.5
├── 英文学术 PDF
│   └── Marker（公式更稳定）
├── 复杂排版/手写/需要语义理解
│   └── 多模态 AI Vision API
└── 已有批量自动化管线
    └── MinerU / PaddleOCR-VL CLI + Python 脚本
```

---

## 5. KDO 集成工作流

### 5.1 单张图片 → 知识卡片

1. 用决策树选引擎
2. 运行解析，得到 Markdown
3. 读 Markdown + 原图交叉验证
4. 整合进 `30_wiki/concepts/<target>.md`
5. 添加 `source_refs` 指向原图路径
6. 更新 `updated_at`

### 5.2 批量目录监控（未来建设）

```bash
# 伪代码
watch 00_inbox/screenshots/
  → 新图片触发解析
  → 输出到 10_raw/parsed/
  → 生成待整合摘要
```

---

## 6. 能力边界与故障排查

| 现象 | 可能原因 | 解决方案 |
|:---|:---|:---|
| 表格列对齐错乱 | 合并单元格复杂 | 手动校对 Markdown 表格 |
| 公式识别不准 | 手写体/非标准符号 | 对照原图修正 LaTeX |
| 多栏文字串行 | 引擎没做布局分析 | 换 MinerU / PaddleOCR-VL |
| 输出为空 | 图片过暗/模糊 | 提高分辨率或换多模态 API |
| 识别慢 | 模型加载 + 大图片 | 裁切图片、用 GPU |

---

## 7. 与现有 skills 的关系

- `image-ocr`：本 toolkit 的轻量级子集，负责简单文字
- `deep-image-parser`：多模态 AI 解析方案，可作为本 toolkit 的 fallback
- 本 skill：负责**引擎选型**和**本地部署方案**

---

## 8. 下一步待验证

- [ ] 在本地 Windows/WSL 验证 PaddleOCR-VL 安装
- [ ] 在本地验证 MinerU `magic-pdf[full]` 安装
- [ ] 用 3-5 张真实课程截图做引擎对比测试
- [ ] 建立 Gold Standard 评测集（类似 `_verify_gold_standard.py`）
