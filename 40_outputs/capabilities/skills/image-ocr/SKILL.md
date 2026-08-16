---
title: Image OCR Pipeline
type: capability/skill
status: published
created_at: 2026-05-07
source_refs: []
tags:
  - ocr
  - pipeline
  - paddleocr
  - chinese-ocr
owner: huangyaoshi
version: 1.0.0
---

# Image OCR Pipeline

从图片中提取中文文本的本地 OCR 能力。

## 引擎

**PaddleOCR v5** (ONNX Runtime Web backend)
- 本地运行，无需网络/API key
- 针对中文优化，准确率高
- 每张图 1-5 秒（取决于尺寸）

## 文件位置

| 文件 | 路径 |
|------|------|
| 能力文档 | `40_outputs/capabilities/skills/image-ocr/SKILL.md` |
| 包装脚本 | `40_outputs/capabilities/skills/image-ocr/ocr-image.ps1` |
| 运行时目录 | `C:\Users\Administrator\ocr-pipeline\` |
| 核心脚本 | `C:\Users\Administrator\ocr-pipeline\ocr-paddle.cjs` |
| 检测模型 | `C:\Users\Administrator\ocr-pipeline\models\det.onnx` (4.6MB) |
| 识别模型 | `C:\Users\Administrator\ocr-pipeline\models\rec.onnx` (15.8MB) |
| 字符字典 | `C:\Users\Administrator\ocr-pipeline\models\dict.txt` (74KB) |

> **为什么运行时在 wiki 外面**：模型文件 ~20MB + node_modules ~670MB，不能进 git 仓库。

## 使用方式

### 单张图片

```powershell
.\40_outputs\capabilities\skills\image-ocr\ocr-image.ps1 "path/to/image.png"
```

输出：同目录下 `<原文件名>_paddle_ocr.txt`

### 批量处理

```powershell
.\40_outputs\capabilities\skills\image-ocr\ocr-image.ps1 "00_inbox/*.png" -Batch
```

### 直接调用 Node.js

```bash
node C:\Users\Administrator\ocr-pipeline\ocr-paddle.cjs <image-path>
```

## 支持的图片格式

- PNG (通过 `fast-png` 解码)
- JPEG (通过 `jpeg-js` 解码)
- 自动检测格式（magic bytes），不依赖文件扩展名
- 自动处理 RGBA → RGB 转换

## 能力边界（硬限制）

> ⚠️ **本 skill 仅适用于「纯文字提取」场景**。以下场景**明确不支持**，必须升级到深度文档解析引擎：

| 场景 | 支持状态 | 说明 |
|------|---------|------|
| 普通水平文字 | ✅ | 本 skill 主力场景 |
| 中英文混合 | ✅ | 基于 dict.txt 6623 字符字典 |
| **表格结构化提取** | ❌ **不支持** | 无法识别表格行列关系，输出为混乱纯文本 |
| **数学/物理公式** | ❌ **不支持** | 无法输出 LaTeX，公式会碎成乱码字符 |
| **密集小字号文字** | ❌ **不支持** | 字号 < 12pt 或 DPI < 150 时准确率骤降 |
| **多栏排版** | ❌ **不支持** | 无法保持栏间逻辑顺序，文字会串行 |
| **图表/流程图** | ❌ **不支持** | 无法解析图形语义关系 |
| 竖排/弯曲文字 | ❌ 不支持 | CTC 解码器对旋转文本失效 |
| 手写体 | ❌ 不支持 | 训练集仅含印刷体 |

**诊断信号**：当 OCR 输出出现以下情况时，说明已触碰能力边界，必须换引擎：
- 表格内容变成无空格的长串乱序文本
- 公式中出现无法理解的单个字符（如孤立的下标/上标）
- 密集段落中整行漏识别或错识别率 > 20%

## 已知局限（运行时）

1. **图片质量敏感**：低分辨率/模糊图片识别率下降
2. **复杂排版**：非水平文字、弯曲文字识别受限
3. **首次加载慢**：ONNX Runtime WASM backend 初始化 ~2s
4. **内存占用**：模型加载 ~200MB RAM

## 关键 Bug 教训

**dict 索引偏移问题**：
- PaddleOCR 模型的 CTC output class 0 是 blank token
- class 1 是空格（全角空格 `　`），class 2 起是实际字符
- **dict 文件不能 filter 空行**！必须保留所有行以保持索引对齐
- 错误的 `.filter(l => l.trim())` 会移除全角空格行，导致所有字符索引偏移 1
- 症状：OCR 输出为随机中文乱码（字符都认识但内容完全不对）

## 截图自动发现（v2 新增）

当用户粘贴截图到聊天但平台不支持多模态时，使用自动发现流程：

```powershell
# 自动发现最近 N 张截图并 OCR
.\40_outputs\capabilities\skills\image-ocr\read-screenshot.ps1 -Last 3

# 指定具体文件
.\40_outputs\capabilities\skills\image-ocr\read-screenshot.ps1 -Path "C:\Users\Administrator\Desktop\Snipaste_xxx.png"
```

**搜索范围**：
1. 桌面：`Snipaste_*.png`、`Screenshot_*.png`、`*.screenshot*.png`
2. Vault inbox：`00_inbox/screenshot*.png`
3. 兜底：桌面上最近 10 张任意 PNG

**输出**：OCR 文本打印到终端 + 图片自动拷贝到 `00_inbox/ocr_*.png`

## 为什么需要这个（模型层分析）

当前会话的模型后端是 **DeepSeek V4 Pro**（通过 Kimi Code API），该模型**不支持多模态**：
- Read 工具返回 `[Unsupported Image]` —— 模型无法处理像素数据
- WebSearch 返回 `tool_choice` 错误 —— DeepSeek Reasoner 不支持工具选择

因此所有图片理解必须走本地 OCR 管道。这是非多模态模型下看图能力的唯一可行方案。

## 升级方案：深度文档解析（表格/公式/密集文字）

当费用本 skill 触碰能力边界（表格、公式、密集文字、多栏）时，必须切换到以下**深度文档解析引擎**。这些引擎不是简单的 OCR，而是具备版面理解能力的文档结构化提取器。

### 引擎对比（2026-05 调研）

| 维度 | **MinerU** (`magic-pdf`) | **Marker** (`marker-pdf`) | **PaddleOCR Python + PP-Structure** |
|------|--------------------------|---------------------------|-------------------------------------|
| 厂商 | 阿里通义 | 社区开源 | 百度飞桨 |
| 安装 | `pip install magic-pdf[full]` | `pip install marker-pdf` | `pip install paddleocr` + 多模型管理 |
| 模型大小 | ~1GB（自动懒加载） | ~4GB | ~500MB（需手动管理） |
| 表格识别 | ⭐⭐⭐ 极强 | ⭐⭐☆ 良好 | ⭐⭐⭐ 极强 |
| 公式识别 | ⭐⭐⭐ LaTeX 输出 | ⭐⭐⭐ LaTeX 输出 | ⭐⭐☆ 需单独配置 PP-Formula |
| 密集文字 | ⭐⭐⭐ 专门优化 | ⭐⭐☆ | ⭐⭐⭐ 中文极强 |
| 多栏布局 | ⭐⭐⭐ 自动分栏 | ⭐⭐☆ | ⭐⭐⭐ 版面分析 |
| 中文支持 | ⭐⭐⭐ 原生优化 | ⭐⭐☆ 依赖 Qwen-VL | ⭐⭐⭐ 母语级 |
| 输出格式 | Markdown / JSON / HTML | Markdown | JSON / 多种格式 |
| 运行方式 | Python CLI + API | Python CLI | Python API |

### 七公推荐：MinerU 作为主力

**理由**：
1. KDO 知识库以中文为主，MinerU 阿里内部打磨，中文课程截图/研报识别率最高
2. 一体化输出：一次调用同时得到 Markdown（含表格、LaTeX）+ JSON（坐标/置信度/区块类型）
3. Markdown 可直接注入 `30_wiki/concepts/` 卡片正文
4. JSON 坐标可用于后续 Visual Analysis
5. 支持图片 + PDF 双输入

### 引擎选型决策树

```
任务类型
├── 纯文字提取（登机牌、发票、简短截图） → 本 skill (PaddleOCR.js)
├── 表格/公式/密集文字（课程截图、研报、论文、对比图） → MinerU
├── 英文学术 PDF 转 Markdown → Marker（公式效果更稳定）
└── 深度定制场景（特殊字体、手写体） → PaddleOCR Python + 自训练模型
```

### MinerU 快速试用

```bash
# 安装
pip install magic-pdf[full]

# 单张图片解析
magic-pdf -p input.png -o output_dir -m auto

# 输出结析
output_dir/
├── input.md       # Markdown 正文（含表格、公式）
├── input.json     # 结构化元数据（区块类型、坐标、置信度）
└── images/        # 提取的嵌入图片
```

### 备选方案（轻量级）

| 方案 | 适用场景 | 优点 | 缺点 |
|------|---------|------|------|
| OCR.space API | 偶尔识图 | 无需本地模型 | 需联网、500次/天限额 |
| tesseract.js | 多语言场景 | 开源 | 中文准确率低（~70%） |
| Kimi 视觉模型 | 图表理解 | 原生多模态 | 需确认 API 是否含 vision |
| 直接切 Claude | 复杂图片 | 无需 OCR | 需更换 API endpoint |

## 依赖

```json
{
  "paddleocr": "^1.1.1",
  "onnxruntime-web": "^1.25.1",
  "fast-png": "^8.0.0",
  "jpeg-js": "^0.4.4"
}
```

安装：`npm install paddleocr onnxruntime-web fast-png jpeg-js`

## 触发词

**触发场景**：需要从图片中提取中文文本时——方法论图片、PPT、信息图、截图、扫描件的文字提取；本地 OCR（PaddleOCR，无需网络/API key）。

**负面例子（不要触发）**：英文为主的图片（准确率低，考虑其他引擎）；视频文字提取（那是视频处理）；图片只有图形没有文字。
