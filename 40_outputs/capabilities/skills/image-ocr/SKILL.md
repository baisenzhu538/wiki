---
title: Image OCR Pipeline
type: capability/skill
status: stable
created_at: 2026-05-07
source_refs: []
tags:
  - ocr
  - pipeline
  - paddleocr
  - chinese-ocr
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

## 已知局限

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

## 备选方案

| 方案 | 优点 | 缺点 |
|------|------|------|
| OCR.space API | 高准确率、无需本地模型 | 需联网、500次/天限额、≤1MB/图 |
| tesseract.js | 开源、多语言 | 中文准确率低（~70%） |
| PaddleOCR (本方案) | 本地、免费、高准确率 | 需模型文件、大内存 |
| Kimi 视觉模型 | 原生理解图表/UI/颜色 | 需确认 kimi-for-coding 是否含 vision 能力 |
| 直接切 Claude | 原生多模态，无需 OCR | 需更换 API endpoint |

## 已知局限（更新 v2）

1. PaddleOCR **只能提取文字**，无法理解图表、UI布局、颜色、空间关系
2. 复杂排版（竖排、弯曲文字、手写体）识别率低
3. 首次加载 ~2s（ONNX Runtime WASM 初始化）
4. 内存占用 ~200MB
5. 桌面路径在 WSL 下不可达，必须用 PowerShell 调用

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
