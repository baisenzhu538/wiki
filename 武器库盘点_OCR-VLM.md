# OCR+VLM 武器库盘点

> 盘点人：洪七公（Kimi Code CLI）  
> 盘点时间：2026-07-07  
> 目的：为「苦练基本功」域的 OCR+VLM 处理做准备

---

## 一、武器状态总览

| 武器 | 状态 | 用途 |
|------|------|------|
| Python 3.12.3 | ✅ 就绪 | 运行环境 |
| anthropic 0.115.0 | ✅ 就绪 | Anthropic SDK（MiniMax 兼容） |
| requests 2.34.2 | ✅ 就绪 | HTTP 请求 |
| PyMuPDF 1.24.14 | ✅ 就绪 | PDF 转图片 |
| PIL 12.2.0 | ✅ 就绪 | 图片处理/缩放 |
| json5 0.15.0 | ✅ 就绪 | 健壮 JSON 解析 |
| paddleocr | ✅ 就绪 | 本地 OCR（备用） |
| MiniMax API Key | ✅ 已配置 | `.env` 中存在 |
| MiniMax API 连通性 | ✅ 测试通过 | `api.minimaxi.com/anthropic` |

---

## 二、两套主力脚本

### 脚本 A：深度 OCR + 内容理解（推荐用于课程材料）

**位置**：
- `wiki/00_inbox/人机协作双三角/codex/run_vlm_codex.py`
- `wiki/00_inbox/人机协作双三角/run_vlm_extract.py`
- `wiki/00_inbox/销售专题/run_vlm_sales.py`
- `wiki/00_inbox/实事求是/run_vlm_truth.py`
- `wiki/00_inbox/底层逻辑之一-Y模型/run_vlm_logic.py`
- `wiki/00_inbox/时间管理/run_vlm.py`

**调用方式**：Anthropic SDK + `api.minimaxi.com/anthropic`

**输出格式**：
```markdown
## 原文识别
[OCR 原文]

## 核心主题
[2-3 句话]

## 结构化内容
[Markdown 结构]

## 关键概念
- 

## 一句话总结
[一句话]
```

**适用场景**：
- 课程内容、方法论、案例分析
- 需要完整 OCR + 结构化 + 概念提取
- 高信息密度的教学图片

**优点**：内容深度好，适合后续人工整合  
**缺点**：输出格式不统一，不便自动化聚合

---

### 脚本 B：结构化 VLM 描述（推荐用于分类标注）

**位置**：
- `wiki/40_outputs/code/scripts/describe-images-minimax.py`

**调用方式**：OpenAI-compatible API + `api.minimax.chat/v1`

**输出格式**：
```json
{
  "category": "信息图/框架图/...",
  "title": "...",
  "description": "...",
  "key_elements": [],
  "visual_style": "...",
  "tags": [],
  "usable_for": "...",
  "confidence": 0.95
}
```

**适用场景**：
- 大量图片分类归档
- 需要置信度评分
- 需要统一的 JSON 格式便于聚合

**优点**：输出统一、可聚合、有置信度  
**缺点**：OCR 深度不如脚本 A，对纯文字内容理解偏浅

---

## 三、批量处理工具

### 并发批处理脚本

**位置**：`wiki/00_inbox/_vlm_reprocess/run_vlm_batches.py`

**特性**：
- 支持多域并发处理（默认 3 个 worker）
- 批次大小可配（默认 4 张/批）
- 失败重试机制（保留失败文件在 `_temp_<domain>`）
- 成功文件移到 `_done_<domain>`
- 自动跳过已处理文件（断点续传）

**适合场景**：处理大量图片（50+ 张）时稳定可靠

---

## 四、推荐方案：苦练基本功域

根据以往经验（双三角 108 张、销售 72 张、管项目 69 张），我建议：

### 主方案：脚本 A（深度 OCR）

```bash
cd /c/Users/Administrator/Desktop/wiki/00_inbox/苦练基本功
python run_vlm_kulian.py
```

**理由**：
- 苦练基本功大概率是课程内容/方法论
- 需要完整 OCR + 概念提取 + 一句话总结
- 后续王语嫣要标注升级，需要高质量原文

### 备方案：脚本 B（结构化）

如果需要快速分类归档：
```bash
python /c/Users/Administrator/Desktop/wiki/40_outputs/code/scripts/describe-images-minimax.py \
  -i /c/Users/Administrator/Desktop/wiki/00_inbox/苦练基本功 \
  -o /c/Users/Administrator/Desktop/wiki/00_inbox/苦练基本功/_vlm_output
```

### 混合方案（最佳）

1. 先用脚本 A 跑深度 OCR
2. 对表格密集、低置信度的图片用脚本 B 补充
3. 最后人工整合成结构化笔记

---

## 五、待办事项

- [ ] 等东家把图片放进 `wiki/00_inbox/苦练基本功/`
- [ ] 复制 `run_vlm_codex.py` 为 `run_vlm_kulian.py`，改路径
- [ ] 跑一遍测试（先 1-2 张验证）
- [ ] 全量处理
- [ ] 输出整合笔记

---

## 六、注意事项

1. **API Key**：两个 endpoint 都用同一个 key，注意不要并发过高
2. **终端编码**：读取 .env 必须 `encoding='utf-8'`，否则会报 GBK 错误
3. **图片格式**：支持 .png/.jpg/.jpeg/.jfif/.webp/.bmp/.gif
4. **成本控制**：脚本 B 有图片缩放（1024px），脚本 A 没有（建议大图先压缩）
5. **断点续传**：脚本 B 不会重跑已有输出，脚本 A 会（如需可改造）

---

## 一句话总结

> 武器库齐全，Python + MiniMax API + 两套脚本都已就绪。苦练基本功域建议用「脚本 A 深度 OCR」为主方案，等图片到位即可开工。
