---
title: PaddleOCR 本地部署使用指南
type: guide
status: reviewed
created_at: 2026-05-07
updated_at: 2026-05-07
---

# PaddleOCR 本地部署使用指南

## 1. 部署现状

PaddleOCR 已本地部署在 `wiki/.tmp/ocr/` 目录下，可直接使用。

### 目录结构

```
wiki/
├── .tmp/ocr/                    ← 脚本与依赖
│   ├── ocr-paddle-final.cjs     ← 主脚本（推荐用此版）
│   ├── ocr-paddle.cjs         ← 早期版本（备份）
│   ├── package.json           ← Node.js 依赖
│   └── node_modules/          ← 已安装依赖
└── _tmp/ocr/models/             ← ONNX 模型文件
    ├── det.onnx                 ← 文字检测模型
    ├── rec.onnx                 ← 文字识别模型
    └── dict.txt                 ← 中文字典（3758 字）
```

### 技术栈

- **运行时**: Node.js + `paddleocr` npm 包
- **模型框架**: ONNX Runtime (`onnxruntime-web`)
- **模型版本**: PP-OCRv5 Mobile（检测+ 识别两阶段）
- **输入格式**: PNG 图片
- **输出格式**: 纯文本 (`*_paddle_ocr.txt`)

---

## 2. 使用方式

### 单图识别

```bash
cd "C:\Users\Administrator\Desktop\wiki\.tmp\ocr"
node ocr-paddle-final.cjs "<path-to-image.png>"
```

例子：
```bash
node ocr-paddle-final.cjs "C:\Users\Administrator\Desktop\wiki\00_inbox\screenshot.png"
```

输出：同目录下生成 `screenshot_paddle_ocr.txt`

### 已处理记录

目前已用 PaddleOCR 处理 **14 张图片**，输出保存在 `wiki/00_inbox/` 下：

- `一堂-*_paddle_ocr.txt` × 13 份
- `一堂进步大地图_paddle_ocr.txt` × 1 份

---

## 3. 识别效果对比

### PaddleOCR vs ocr.space（在线 API）

| 维度 | PaddleOCR (本地) | ocr.space (在线) |
|------|------------------|-----------------|
| **连接方式** | 无需网络 | 需要网络 + API key |
| **隐私性** | 图片不出本地 | 上传到第三方服务器 |
| **中文识别** | ✅ 准确度高 | ✅ 也较高 |
| **表格结构** | 纯文本，无格式 | 保留制表符 `	` |
| **英文混排** | ✅ 支持 | ✅ 支持 |
| **识别速度** | 1-3 秒/张 | 取决于网络 |
| **费用** | 免费 | 免费额度有限 |
| **可靠性** | ✅ 本地，不受网络影响 | ❌ 网络故障时不可用 |

### 实际输出对比（以创业必修课程清单为例）

**共同优点**：两者中文识别准确率都很高，课程名称、口令等关键信息均正确提取。

**差异点**：
- **ocr.space**: 输出包含 `	` 制表符，对表格类图片结构保留更好
- **PaddleOCR**: 输出更干净，无多余空白和制表符，更适合直接喂给 LLM

> **建议**：表格类图片用 ocr.space，文本类/截图类用 PaddleOCR。

---

## 4. 与 RapidOCR 的关系

| | RapidOCR | PaddleOCR (当前部署) |
|---|---|---|
| **定位** | 轻量级 Python 封装 | 完整 Node.js 实现 |
| **依赖** | Python + pip | Node.js + npm |
| **模型** | 内置 PP-OCRv4 | 外部 PP-OCRv5 ONNX |
| **部署难度** | 一行命令 | 需要配置模型路径 |
| **适用场景** | Python 脚本快速调用 | Node.js 工作流稳定运行 |

> 两者都是基于百度 PaddleOCR 的实现，核心识别能力相当。当前部署的是 PP-OCRv5，模型更新。

---

## 5. 五绝使用场景

| 使用者 | 场景 | 建议工具 |
|--------|------|---------|
| **黄药师** | 截图/课程图片识别→转文本→KDO ingest | **PaddleOCR** 本地更快 |
| **洪七公** | 表格类图片识别（价格表、数据表） | **ocr.space** 保留表格结构 |
| **段智兴** | 发布前的图片审核、文字校对 | **PaddleOCR** 本地处理 |
| **欧阳锋** | 技术文档截图识别 | **PaddleOCR** |
| **周伯通** | 批量处理截图/评估质量 | **PaddleOCR** 可批量化 |

---

## 6. 快速命令

### 单图识别
```bash
cd "C:\Users\Administrator\Desktop\wiki\.tmp\ocr"
node ocr-paddle-final.cjs "<image.png>"
```

### 批量识别（需自行编写批量脚本）
```javascript
const { execSync } = require('child_process');
const images = ['a.png', 'b.png', 'c.png'];
for (const img of images) {
  execSync(`node ocr-paddle-final.cjs "${img}"`, { stdio: 'inherit' });
}
```

---

## 7. 注意事项

1. **输入格式**: 仅支持 PNG，如果是 JPG/WEBP 需先转换
2. **图片大小**: 建议图片宽度不超过 2000px，过大会慢
3. **模型路径**: 脚本内写死了 `models/` 目录路径，不要移动
4. **Node 版本**: 需要支持 async/await 的 Node.js 版本（v14+）

---

## 8. 关键结论

- ✅ **PaddleOCR 本地部署已可用**，无需网络、无需 API key
- ✅ **中文识别准确率高**，适合 KDO 素材收集场景
- ⚠️ **表格结构丢失**，纯文本输出，对结构化数据不友好
- ✅ **建议主要使用** 本场 PaddleOCR，表格类再用在线 API
