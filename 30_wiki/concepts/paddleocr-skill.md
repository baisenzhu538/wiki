---
title: "PaddleOCR — 本地 ONNX + 云端 API 双模 OCR Skill"
type: concept
status: enriched
domain: ['master']
source_refs: []
created_at: "2026-05-07"
updated_at: "2026-05-07"
related:
  - "[[web-scraping-三剑客-scrapling-crawl4ai-firecrawl]]"
  - "[[tinyfish-agentic-web-infrastructure]]"
  - "[[kdo-protocol]]"
tags:
  - "#skill"
  - "#ocr"
  - "#tool"
  - "#paddleocr"
  - "#onnx"
trust_level: high
reviewed_by: "黄药师"
review_date: "2026-05-07"
---

# PaddleOCR — 本地 ONNX + 云端 API 双模 OCR Skill

> 百度 PaddlePaddle 出品，GitHub 74K+ stars，PP-OCRv5 中文准确率 ~97.8%。**本地部署方案已投产**：Node.js + ONNX Runtime，零网络依赖。

## Summary

黄药师已完成 PaddleOCR 本地生产级部署。与官方云端 API Skill 形成互补双模架构。

与此同时，黄药师已在本地部署 PaddleOCR Python 库，可直接通过 Python API 调用，无需 API Key。

---

## [Condense] 核心架构

### 生产部署（本地 ONNX Runtime）

```
40_outputs/capabilities/skills/image-ocr/
├── SKILL.md                    # 能力文档
└── ocr-image.ps1               # PowerShell 包装脚本

C:\Users\Administrator\ocr-pipeline\
├── ocr-paddle.cjs              # 核心引擎（Node.js）
├── models/
│   ├── det.onnx (4.6MB)        # 文字检测模型
│   ├── rec.onnx (15.8MB)       # 文字识别模型
│   └── dict.txt (74KB)         # 字符字典 6700+ entries
├── package.json                # paddleocr + onnxruntime-web + fast-png + jpeg-js
└── node_modules/ (~670MB)
```

**为什么运行时在 wiki 外面**：模型 + node_modules ~700MB，不进 git。

### 技术栈

| 组件 | 选型 | 备注 |
|------|------|------|
| OCR 引擎 | PaddleOCR v5 (ONNX Runtime Web) | Node.js 封装，非 Python |
| 检测模型 | `det.onnx` | 4.6MB，文字区域定位 |
| 识别模型 | `rec.onnx` | 15.8MB，CRNN-CTC 序列识别 |
| 字符字典 | `dict.txt` | 6700+ 字符，含全角空格（索引 1） |
| 图片解码 | `fast-png` + `jpeg-js` | magic bytes 自动检测格式 |
| 推理后端 | `onnxruntime-web` | WASM backend，CPU 推理 |

### 已知 Bug 教训（dict 索引偏移）

PaddleOCR CTC 输出的 class 0 = blank token，class 1 = 全角空格 `　`，class 2 起才是实际字符。**dict 文件不能 filter 空行**——错误的 `.filter(l => l.trim())` 会移除全角空格行，导致所有字符索引偏移 1，症状为随机中文乱码。

### 使用方式（三种调用路径）

```powershell
# 路径 1: PowerShell 包装脚本（单张）
.\40_outputs\capabilities\skills\image-ocr\ocr-image.ps1 "path/to/image.png"

# 路径 2: PowerShell 批量处理
.\40_outputs\capabilities\skills\image-ocr\ocr-image.ps1 "00_inbox/*.png" -Batch

# 路径 3: 直接调用 Node.js
node C:\Users\Administrator\ocr-pipeline\ocr-paddle.cjs <image-path>
```

---

## [Critique] 批判性评估

### 前提假设

- 假设 ONNX Runtime Web (WASM) 在 Node.js 环境下的推理精度与原生 PaddlePaddle 一致。【可靠性：高】ONNX 是标准格式，模型权重完全相同
- 假设 6700+ 字符字典覆盖 KDO wiki 场景中绝大多数中文文本。【可靠性：高】常用汉字 + 标点 + 字母数字均覆盖
- 假设 magic bytes 格式检测对 PNG/JPEG 的识别可靠。【可靠性：高】这是标准做法，边界情况（WebP/BMP/PDF）会报错退出

### 边界与反例

- **最适合**：截图文字提取、扫描件 OCR、课程 PPT/讲义图片、微信群聊截图
- **不适合**：PDF 直接解析（需要先转图片）、手写体、严重倾斜/弯曲文字、复杂表格还原
- **已知局限**：低分辨率模糊图片识别率下降；非水平文字受限；首次加载 ~2s（WASM 初始化）；内存占用 ~200MB

### 关键约束

- 只能从 WSL 通过 `/mnt/c/Users/Administrator/ocr-pipeline/` 路径调用——Windows 的 PowerShell 脚本 WSL 无法直接执行
- 需要 `cmd.exe /c "powershell ..."` 或 `/mnt/c/Windows/System32/WindowsPowerShell/v1.0/powershell.exe` 桥接
- 输出文件 `<原名>_paddle_ocr.txt` 保存在源图片同目录

### 可靠性

**整体：高。** 生产级部署，已通过 dict 索引偏移 bug 修复验证。PP-OCRv5 中文准确率 97.8%，本地 ONNX 推理不受 API 限流/网络中断影响。

---

## [Synthesis] 与 wiki 知识库的关联

- [[web-scraping-三剑客-scrapling-crawl4ai-firecrawl]] — PaddleOCR 补充了"图片/PDF→文本"这一环，之前整个工具栈只有"网页→文本"
- [[tinyfish-agentic-web-infrastructure]] — TinyFish 的 Fetch 端返回 Markdown，PaddleOCR 负责把 Fetch 拿不到的图片内文字提取出来。两者组合：TinyFish 获取页面 → PaddleOCR 识别嵌入图片
- [[business-research-skill-oscar-13-weapon-system]] — Step 3 在线采集时，遇到图片形式的财报/数据，可以用 PaddleOCR 提取结构化数据
- [[kdo-protocol]] — PaddleOCR 是第四个 tool 型 Skill，验证了 tool 型 Skill 的 pre-flight check 模式

### 补充：WSL 侧 Python PaddleOCR

生产部署是 Windows Node.js ONNX 方案。WSL 侧另装了 `paddleocr 3.5.0`（Python），可用于更复杂的文档解析（PPStructureV3），但日常使用以 Node.js 方案为主。

### 补充：云端 API Skill

`~/.claude/skills/paddleocr-text-recognition/` 和 `~/.claude/skills/paddleocr-doc-parsing/` 是官方 Claude Code Skill（PEP 723 + uv），作为本地 ONNX 的备份，需要 PaddleOCR API Key。

### Skill 体系（至此 5 个 Skill）

| 类型 | Skill | 核心能力 |
|------|-------|---------|
| methodology | business-research | OSCAR + 13 武器调研 |
| persona | truman-perspective | 许楚思维模拟 |
| tool | use-tinyfish | Web Search/Fetch/Agent/Browser |
| tool | paddleocr-text-recognition | 图片/PDF → 线级文本（云端 API） |
| tool | paddleocr-doc-parsing | 文档 → 结构化 Markdown（云端 API） |
| **local** | **ocr-pipeline (ocr-paddle.cjs)** | 本地 ONNX 推理，零网络依赖 |

## Open Questions

- Node.js 方案能否扩展支持 PDF 直接输入（目前仅 PNG/JPEG）？
- ONNX 检测模型对竖排中文的表现如何？
- 云端 PP-StructureV3 的表格还原质量是否值得配置 API Key？

## Output Opportunities

- **KDO capture 增强**：PaddleOCR 作为 `kdo capture` 的图片预处理插件——截图自动 OCR 后存入 inbox
- **business-research 集成**：Step 3 遇到图片财报/数据截图时自动调用 PaddleOCR 提取
- **TinyFish + PaddleOCR 组合**：Fetch 获取页面 → PaddleOCR 识别嵌入图片 → 完整 Markdown
