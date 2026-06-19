---
title: "图像理解流水线：从 OCR 到 VLM 的选型与复用"
type: capability
subtype: skill
status: stable
target_user: KDO 任意需要处理图片素材的 agent 或人类协作者
scope: "洪七公 / Multimodal Arbiter，但可被全角色调用"
origin: "洪七公于 2026-06-19 整理，防止重复造轮子"
last_verified: "2026-06-19"
---

# 图像理解流水线：从 OCR 到 VLM 的选型与复用

## 为什么要有这个 skill

KDO 中多个 agent 都需要处理图片（OCR、识图、生成描述、归档分类）。如果不统一，每个人都会重新调研、安装、写脚本，浪费时间。

本 skill 是一个**决策地图 + 工具索引**，告诉你：
- 遇到图片任务，**先选哪个工具**
- 每个工具**在哪里、怎么用**
- 工具失败时** fallback 到哪个**
- 相关脚本和 skill 的**精确路径**

---

## 一、快速选型表

| 你的需求 | 首选工具 | 脚本/路径 | 何时不用 |
|---|---|---|---|
| **只想提取图中文字** | PaddleOCR v5（本地已部署） | `C:\Users\Administrator\ocr-pipeline\` | 图片里文字极少或纯视觉时 |
| **PaddleOCR 失败/不好使** | EasyOCR | `40_outputs/code/scripts/ocr-images-easyocr.py` | 已有 PaddleOCR 且效果好时 |
| **PDF/复杂图文混排** | MinerU | `magic-pdf` + `document-parsing-toolkit` skill | 单张简单图片 |
| **要理解画面内容、生成描述** | MiniMax-M3 VLM | `40_outputs/code/scripts/describe-images-minimax.py` | 只需文字、不想花钱 |
| **MiniMax 不可用时** | SiliconFlow Qwen-VL | `40_outputs/code/scripts/describe-images-siliconflow.py` | 已有 MiniMax key 且可用 |
| **要生成图片/封面** | **MiniMax Image-01**（国内，推荐） / 通义万相 / fal.ai（余额耗尽） | `40_outputs/code/scripts/generate-images-minimax.py` | 只需识图 |

---

## 二、已部署工具

### 1. PaddleOCR v5（本地 Node.js，最快）

- **位置**：`C:\Users\Administrator\ocr-pipeline\`
- **启动方式**：`npm start`（需 node 环境）
- **输入输出**：把图片放到 `_ocr_input/`，结果在 `_ocr_output/`
- **优点**：纯本地、速度快、已配置好
- **缺点**：对复杂排版/艺术字/低对比度图效果一般
- **相关 skill**：`40_outputs/capabilities/skills/image-ocr/`

### 2. EasyOCR（WSL Python，fallback）

- **脚本**：`40_outputs/code/scripts/ocr-images-easyocr.py`
- **运行**：
  ```bash
  python3 40_outputs/code/scripts/ocr-images-easyocr.py \
    -i "00_inbox/某个目录" \
    -o "00_inbox/某个目录"
  ```
- **优点**：无需 node，中文识别尚可，按阅读顺序合并文本行
- **缺点**：首次需下载模型，复杂图效果一般
- **相关 skill**：`40_outputs/capabilities/skills/image-ocr-easyocr/`

### 3. MinerU（WSL，PDF + 复杂图文）

- **命令**：`magic-pdf -p input.pdf -o output_dir -m auto`
- **脚本辅助**：`_tmp/download-mineru-models.sh`
- **配置**：`~/magic-pdf.json`（WSL 内）
- **优点**：布局分析强，输出 Markdown + JSON + 图片
- **缺点**：模型大，WSL 配置略复杂
- **相关 skill**：`40_outputs/capabilities/skills/document-parsing-toolkit/`

### 4. MiniMax-M3 VLM（云端，语义理解）

- **脚本**：`40_outputs/code/scripts/describe-images-minimax.py`
- **运行**：
  ```bash
  export MINIMAX_API_KEY=你的key
  python3 40_outputs/code/scripts/describe-images-minimax.py \
    -i "00_inbox/某个目录" \
    -o "00_inbox/某个目录"
  ```
- **输出**：`${stem}_vlm_desc.md` + `README-VLM描述汇总.md`
- **优点**：理解画面语义、风格、用途，生成结构化描述
- **缺点**：需要 API key，按 token 计费
- **相关 skill**：本 skill

### 5. SiliconFlow Qwen-VL（云端，备选）

- **脚本**：`40_outputs/code/scripts/describe-images-siliconflow.py`
- **运行**：
  ```bash
  export SILICONFLOW_API_KEY=你的key
  python3 40_outputs/code/scripts/describe-images-siliconflow.py \
    -i "00_inbox/某个目录" \
    -o "00_inbox/某个目录"
  ```
- **优点**：模型选择多，OpenAI 兼容
- **缺点**：需单独注册充值

---

## 三、标准工作流

处理一批图片时，建议按以下顺序：

```
1. 先用 PaddleOCR v5 批量跑文字提取
        ↓
2. 检查 OCR 质量：
   - 如果大部分文字都出来了 → 结束
   - 如果很多图识别不全 → 用 EasyOCR 或 MinerU 补跑
        ↓
3. 如果需要语义理解/标签/归档：
   - 用 MiniMax-M3 VLM 生成结构化描述
        ↓
4. 把 OCR + VLM 描述合并，生成最终归档材料
```

---

## 四、输出规范

无论用哪个工具，最终输出建议放在**原图所在目录**，命名规范：

| 工具 | 输出文件名 | 示例 |
|---|---|---|
| PaddleOCR | `${stem}_paddle_ocr.txt` | `一堂-科学决策-决策三角形_paddle_ocr.txt` |
| EasyOCR | `${stem}.md` / `${stem}.json` | `一堂-科学决策-决策三角形.md` |
| MinerU | `${stem}.md` | `一堂-科学决策-决策三角形.md` |
| MiniMax VLM | `${stem}_vlm_desc.md` | `一堂-科学决策-决策三角形_vlm_desc.md` |

这样别人打开目录，一眼就能看到原图和所有处理结果。

---

## 五、常见坑

| 坑 | 原因 | 解决 |
|---|---|---|
| MiniMax key 报 401 | 用了 `api.minimax.io` 而不是 `api.minimax.chat` | 中国用户用 `https://api.minimax.chat/v1/chat/completions` |
| MiniMax 说看不到图 | 原生 `/text/chatcompletion_v2` 不支持 base64 图片 | 改用 OpenAI 兼容端点 `/v1/chat/completions` |
| VLM 输出不是 JSON | 模型没严格遵循 prompt | 脚本已做 markdown fence 提取 + JSON fallback |
| MinerU GPU 模式失败 | WSL NVIDIA 驱动太老 | 改用 CPU 模式，或降级 PyTorch 到 cu121 |
| PaddleOCR 中文乱码 | 终端编码问题 | 文件本身 UTF-8，用 VS Code / Obsidian 打开 |

---

## 六、相关 skill

- `image-ocr`：PaddleOCR.js 版本
- `image-ocr-easyocr`：EasyOCR 版本
- `deep-image-parser`：深度图像解析（表格、公式、多栏）
- `document-parsing-toolkit`：PDF/文档解析（MinerU）
- `ai-image-generation-setup`：图像生成平台选型
- `audio-production-pipeline`：音频生成

---

## 七、维护记录

- 2026-06-19：洪七公整理本 skill，统一索引 OCR / MinerU / VLM 工具，避免王语嫣式重复造轮子。
