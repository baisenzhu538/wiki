---
title: "本地图片 OCR 识别（EasyOCR 版）"
type: capability
subtype: skill
status: stable
target_user: KDO 任意 agent 或人类协作者，需要把图片中的文字提取为结构化文本
scope: "洪七公 / Multimodal Arbiter"
origin: "洪七公于 2026-06-14 验证并创建"
last_verified: "2026-06-14"
---

# 本地图片 OCR 识别（EasyOCR 版）

## 能力定位

把本地图片（PNG/JPG/WebP/BMP）批量识别为中文/英文文本，输出 Markdown 和 JSON，适合：
- 提取方法论图片、PPT、信息图里的文字
- 为老顽童或其他 agent 生成可继续加工的结构化素材
- 离线/本地运行，图片不上云

>  companion skill：`40_outputs/capabilities/skills/image-ocr/`（基于 PaddleOCR.js）。当 PaddleOCR 因网络/版本问题无法下载模型时，使用本 EasyOCR 版。

---

## 输入

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `input_dir` | string | 是 | 待识别图片目录 |
| `output_dir` | string | 否 | 输出目录，默认与原图目录相同 |
| `langs` | list | 否 | 识别语言，默认 `["ch_sim", "en"]` |
| `batch_name` | string | 否 | 本次识别批次名，用于生成汇总文件名 |

---

## 输出

| 文件 | 说明 |
|---|---|
| `{image_stem}.md` | 单张图片的结构化识别文本 |
| `{image_stem}.json` | 单张图片的原始 OCR 数据（含坐标、置信度） |
| `README.md` | 批次汇总索引 |
| `{batch_name}-处理素材（精修版）.md` | 可选：人工精修后的老顽童/交付素材 |
| `{batch_name}-方法论汇总.md` | 可选：纯文本汇总 |

---

## 运行环境

- **WSL Ubuntu 22.04**（已在 `/home/dministrator` 验证）
- Python 3.10+
- 已安装包：`easyocr`
- 模型首次运行自动下载到 `~/.EasyOCR`

### 环境检查

```bash
python3 -c "import easyocr; print('OK')"
```

### 安装（如未安装）

```bash
pip install easyocr
```

---

## 调用方式

### 方式 1：直接运行脚本

```bash
cd /mnt/c/Users/Administrator/Desktop/wiki

python3 40_outputs/code/scripts/ocr-images-easyocr.py \
  -i "00_inbox/AI短剧创作" \
  -o "00_inbox/AI短剧创作"
```

### 方式 2：作为 agent 工具调用

agent 收到任务时，按以下步骤执行：

1. **确认输入目录存在**（Read / Bash ls）
2. **检查 EasyOCR 可用**（Bash `python3 -c "import easyocr"`）
3. **运行脚本**（Bash）
4. **检查输出文件**（Read / Bash ls）
5. **如需精修**，人工/LLM 整理为处理素材

---

## 脚本位置

`40_outputs/code/scripts/ocr-images-easyocr.py`

脚本功能：
- 扫描目录内所有图片
- 用 EasyOCR 识别文字并按阅读顺序排序
- 自动合并同一行的文本块
- 简单提取"三板斧"、"罗盘"等结构化章节
- 输出 Markdown + JSON

---

## 已知限制

1. **复杂信息图识别有限**：带大量装饰性字体、英文艺术字、密集排版的图片会识别错误。
2. **首次运行需下载模型**：约 100MB+，若 WSL 网络受限会失败。
3. **不包含视觉理解**：只能识文字，不能"看懂"图表结构。如需深度解析，结合 LLM 视觉模型或 MinerU。
4. **语言以中文为主**：`ch_sim` 对繁体/古字/特殊符号支持一般。

---

## 验证记录

- 2026-06-14：在 WSL 下成功识别 `00_inbox/AI短剧创作` 7 张图片，生成完整 Markdown + JSON。
- 同目录输出方式已验证：原图与识别结果放在一起，便于查找。

---

## 失败处理

| 现象 | 原因 | 处理 |
|---|---|---|
| `ModuleNotFoundError: No module named 'easyocr'` | 未安装 | `pip install easyocr` |
| 模型下载失败 | 网络受限 | 检查 WSL 能否访问 `https://www.jaided.ai/`；必要时手动下载模型 |
| 识别结果为空 | 图片无文字或文字过小 | 提高图片分辨率后再试 |
| 英文乱码 | 艺术字体/装饰字体 | 结合原图人工校对 |

---

## 相关 skills

- `image-ocr`：PaddleOCR.js 版本
- `deep-image-parser`：深度图像解析（表格、公式、多栏）
- `document-parsing-toolkit`：文档级解析（PDF/图片）
- `delivery-producer`：把识别结果进一步加工成交付物

---

## TODO / 下一步改进

- [ ] 增加对"罗盘"类复杂信息图的视觉结构描述能力
- [ ] 接入本地多模态模型做图文联合理解
- [ ] 支持输出 Obsidian 卡片格式，直接沉淀到 `30_wiki/`
