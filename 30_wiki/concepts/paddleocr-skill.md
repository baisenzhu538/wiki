---

id: paddleocr-skill
created_at: 2026-05-07
domain: master
review_date: 2026-05-07
reviewed_by: pending
status: draft
title: PaddleOCR — 本地 ONNX + 云端 API 双模 OCR Skill
trust_level: medium
type: concept
updated_at: '2026-06-16'
author: 黄药师
confidence: 0.7
source_refs:
- src_unknown
source_context: （原始 source 无法追溯，已标记为 src_unknown，待后续补充）
related:
  - "[[ocr-微信图片_20260507004811_41_32]]"
  - "[[ocr-微信图片_20260507004801_37_32]]"
  - "[[tinyfish-agentic-web-infrastructure]]"
  - "[[ocr-微信图片_20260507004758_35_32]]"
  - "[[ocr-微信图片_20260507004806_40_32]]"
---
# PaddleOCR — 本地 ONNX + 云端 API 双模 OCR Skill

> 百度 PaddlePaddle 出品，GitHub 74K+ stars，PP-OCRv5 中文准确率 ~97.8%。**本地部署方案已投产**：Node.js + ONNX Runtime，零网络依赖。

## Summary

黄药师已完成 PaddleOCR 本地生产级部署。与官方云端 API Skill 形成互补双模架构。

与此同时，黄药师已在本地部署 PaddleOCR Python 库，可直接通过 Python API 调用，无需 API Key。

---

## Claims

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

## Critique

### 前提假设

- src_unknown
- src_unknown
- src_unknown

### 边界与反例

- src_unknown
- src_unknown
- src_unknown

### 关键约束

- src_unknown
- src_unknown
- src_unknown

### 可靠性

**整体：高。** 生产级部署，已通过 dict 索引偏移 bug 修复验证。PP-OCRv5 中文准确率 97.8%，本地 ONNX 推理不受 API 限流/网络中断影响。

---

## Synthesis

- 待补充链接
- 待补充链接
- 待补充链接
- 待补充链接
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

### 不要用的场景

| 场景 | 为什么失效 | 替代方案 |
|------|-----------|---------|
| 把这个框架/方法当成绝对真理执行 | 任何方法论都是时间截面，它们假设未来会像过去一样发展 | 每次使用前先问"这个结论现在还成立吗？有没有新的反例出现？" |
## Open Questions

- src_unknown
- src_unknown
- src_unknown
## Output Opportunities

- src_unknown
- src_unknown
- src_unknown

## Action Triggers

| 触发场景 | 第一个动作 | 成功指标 |
|---------|-----------|---------|
| 需要基于这份调研/框架做出关键决策前 | 先问自己"这个结论现在还成立吗？有没有新的反例出现？" | 每次使用前都能说出至少一个可能影响结论有效性的新变化因素 |
