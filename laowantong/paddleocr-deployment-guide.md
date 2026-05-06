---
title: PaddleOCR 本地部署使用指南
type: guide
status: reviewed
created_at: 2026-05-07
updated_at: 2026-05-07
---

# PaddleOCR 本地部署使用指南

> 本文档对应正式 capability：`40_outputs/capabilities/skills/image-ocr/SKILL.md`

---

## 1. 正式封装结构

老板已完成正式封装，分为两部分：

### 运行时（不进 git）

```
C:\Users\Administrator\ocr-pipeline\
├── ocr-paddle.cjs          ← 核心脚本（Node.js）
├── package.json            ← 依赖配置
├── node_modules/           ← 已安装依赖（~670MB）
└── models/
    ├── det.onnx            ← 文字检测模型（4.6MB）
    ├── rec.onnx            ← 文字识别模型（15.8MB）
    └── dict.txt            ← 字符字典（74KB）
```

> 运行时不进 git 的原因：模型文件 ~20MB + node_modules ~670MB，超出 git 合适范围。

### Wiki 封装（进 git）

```
wiki/40_outputs/capabilities/skills/image-ocr/
├── SKILL.md                ← 能力文档
└── ocr-image.ps1         ← PowerShell 包装脚本
```

---

## 2. 技术栈

| 组件 | 版本 | 作用 |
|------|------|------|
| **PaddleOCR** | v5 (ONNX) | 核心引擎 |
| **ONNX Runtime** | 1.25.1 | 模型推理 |
| **fast-png** | 8.0.0 | PNG 图片解码 |
| **jpeg-js** | 0.4.4 | JPEG 图片解码 |
| **Node.js** | v14+ | 运行时 |

---

## 3. 使用方式

### 推荐：PowerShell 包装脚本

**单张图片**：
```powershell
.\40_outputs\capabilities\skills\image-ocr\ocr-image.ps1 "path/to/image.png"
```

**批量处理**：
```powershell
.\40_outputs\capabilities\skills\image-ocr\ocr-image.ps1 "00_inbox/*.png" -Batch
```

输出：同目录下 `<原文件名>_paddle_ocr.txt`

### 直接调用 Node.js

```bash
node C:\Users\Administrator\ocr-pipeline\ocr-paddle.cjs <image-path>
```

---

## 4. 支持的图片格式

- **PNG** — 通过 `fast-png` 解码
- **JPEG** — 通过 `jpeg-js` 解码
- 自动检测格式（magic bytes），不依赖文件扩展名
- 自动处理 RGBA → RGB 转换

---

## 5. 关键 Bug 教训

**索引偏移问题**：
- PaddleOCR 模型的 CTC output class 0 是 blank token
- class 1 是全角空格 `　`，class 2 起是实际字符
- **dict 文件不能 filter 空行**！必须保留所有行以保持索引对齐
- 错误的 `.filter(l => l.trim())` 会移除全角空格行，导致所有字符索引偏移 1
- 症状：OCR 输出为随机中文乱码（字符都认识但内容完全不对）

---

## 6. 已知局限

1. **图片质量敏感**：低分辨率/模糊图片识别率下降
2. **复杂排版**：非水平文字、弯曲文字识别受限
3. **首次加载慢**：ONNX Runtime WASM backend 初始化 ~2s
4. **内存占用**：模型加载 ~200MB RAM

---

## 7. 备选方案对比

| 方案 | 优点 | 缺点 |
|------|------|------|
| **PaddleOCR (本地)** | 本地、免费、高准确率 | 需模型文件、大内存 |
| **OCR.space API** | 高准确率、无需本地模型 | 需联网、500次/天限额、≤1MB/图 |
| **tesseract.js** | 开源、多语言 | 中文准确率低（~70%） |

---

## 8. 五绝使用场景

| 使用者 | 场景 | 建议工具 |
|--------|------|---------|
| **黄药师** | 截图/课程图片识别→转文本→KDO ingest | **PaddleOCR** 本地更快 |
| **洪七公** | 表格类图片（价格表、数据表） | **OCR.space** 保留表格结构 |
| **段智兴** | 发布前图片审核、文字校对 | **PaddleOCR** 本地处理 |
| **欧阳锋** | 技术文档截图识别 | **PaddleOCR** |
| **周伯通** | 批量处理截图/评估质量 | **PaddleOCR** `-Batch` 批量模式 |

---

## 9. 快速命令速查

```powershell
# 单图
.\40_outputs\capabilities\skills\image-ocr\ocr-image.ps1 "image.png"

# 批量
.\40_outputs\capabilities\skills\image-ocr\ocr-image.ps1 "*.png" -Batch

# 直接 Node.js
node C:\Users\Administrator\ocr-pipeline\ocr-paddle.cjs "image.png"
```

---

## 10. 文件对照表

| 文件 | 路径 | 说明 |
|------|------|------|
| 能力文档 | `wiki/40_outputs/capabilities/skills/image-ocr/SKILL.md` | 正式文档，进 git |
| PowerShell 脚本 | `wiki/40_outputs/capabilities/skills/image-ocr/ocr-image.ps1` | 包装脚本，进 git |
| 核心脚本 | `C:\Users\Administrator\ocr-pipeline\ocr-paddle.cjs` | Node.js 实现，不进 git |
| 检测模型 | `C:\Users\Administrator\ocr-pipeline\models\det.onnx` | 4.6MB，不进 git |
| 识别模型 | `C:\Users\Administrator\ocr-pipeline\models\rec.onnx` | 15.8MB，不进 git |
| 字符字典 | `C:\Users\Administrator\ocr-pipeline\models\dict.txt` | 74KB，不进 git |
