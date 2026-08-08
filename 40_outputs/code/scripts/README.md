# KDO 可复用脚本索引

> 本目录存放经洪七公（Multimodal Arbiter）验证的可复用脚本。  
> 处理多媒体任务前，先查本索引，避免重复造轮子。  
> 详细选型指南见：`40_outputs/capabilities/skills/image-understanding-pipeline/SKILL.md`

---

## 图像识别与理解

### `ocr-images-easyocr.py`
- **功能**：批量 OCR 图片中的中文/英文文字
- **输出**：每张图 `${stem}.md` + `${stem}.json` + `README.md`
- **使用场景**：PaddleOCR 失败时的本地 fallback
- **依赖**：WSL + Python + easyocr
- **运行**：
  ```bash
  python3 40_outputs/code/scripts/ocr-images-easyocr.py \
    -i "00_inbox/某个目录" \
    -o "00_inbox/某个目录"
  ```

### `describe-images-minimax.py`
- **功能**：用 MiniMax-M3 VLM 批量生成图片的结构化描述
- **输出**：每张图 `${stem}_vlm_desc.md` + `README-VLM描述汇总.md`
- **使用场景**：需要理解画面语义、风格、用途时
- **依赖**：MiniMax API key（格式 `sk-api-...`）
- **运行**：
  ```bash
  export MINIMAX_API_KEY=你的key
  python3 40_outputs/code/scripts/describe-images-minimax.py \
    -i "00_inbox/某个目录" \
    -o "00_inbox/某个目录"
  ```

### `describe-images-siliconflow.py`
- **功能**：用 SiliconFlow Qwen-VL 批量生成图片的结构化描述
- **输出**：同 MiniMax 版本
- **使用场景**：MiniMax 不可用时的备选
- **依赖**：SiliconFlow API key（格式 `sk-...`）
- **运行**：
  ```bash
  export SILICONFLOW_API_KEY=你的key
  python3 40_outputs/code/scripts/describe-images-siliconflow.py \
    -i "00_inbox/某个目录" \
    -o "00_inbox/某个目录"
  ```

---

## 图像生成

### `generate-images-minimax.py`（推荐 · 国内可直接支付）
- **功能**：用 MiniMax Image-01 国内 API 文生图
- **输出**：指定路径图片 + `*_metadata.json`
- **使用场景**：需要批量生成封面/海报/信息图，且 fal.ai 无法充值时
- **依赖**：MiniMax API key（与 VLM 共用同一个 key）
- **运行**：
  ```bash
  export MINIMAX_API_KEY=你的key
  python3 40_outputs/code/scripts/generate-images-minimax.py \
    -p "一张极简商务风格的信息图，主题是科学决策" \
    -o "40_outputs/content/images/generative/test.png" \
    -r 16:9
  ```
- **备注**：`MINIMAX_API_KEY` 与 `describe-images-minimax.py` 相同；支持 16:9 / 1:1 / 3:4 / 21:9 等比例，可选画风参数 `--style`。

### `generate-images-fal.py`
- **功能**：用 fal.ai FLUX 把文章标题转成封面图
- **输出**：`40_outputs/content/images/generative/`
- **使用场景**：需要批量生成文章封面/信息图
- **依赖**：fal.ai API key（注意：当前账户余额不足，需充值）
- **状态**：余额耗尽，已降级为备用方案

---

## 文档解析

### `download-mineru-models.sh`（WSL）
- **功能**：下载 MinerU 所需模型权重
- **使用场景**：WSL 首次部署 MinerU
- **依赖**：WSL + Python + modelscope

> MinerU 主命令是 `magic-pdf`，不是本脚本。配置详见 `document-parsing-toolkit` skill。

---

## 本地已部署工具（不在本目录）

| 工具 | 位置 | 用途 |
|---|---|---|
| PaddleOCR v5 | `C:\Users\Administrator\ocr-pipeline\` | 本地批量 OCR（node.js） |
| MinerU | WSL `/home/dministrator/.local/bin/magic-pdf` | PDF/复杂图文解析 |
| Marp | 全局安装 | Markdown → 幻灯片 PDF |
| edge-tts | Windows Python | 文本 → 播客/配音 MP3 |

---

## 使用原则

1. **先查索引再动手**：本 README 和 `image-understanding-pipeline` skill 是首选入口
2. **优先用本地已部署工具**：PaddleOCR、MinerU、edge-tts 都已配好
3. **云端工具需确认 key 状态**：fal.ai 当前余额不足，MiniMax/SiliconFlow 需确认额度
4. **输出放原图目录**：便于其他 agent 发现和复用

---

## 维护记录

- 2026-06-19：洪七公创建本索引，汇总图像识别/理解/生成相关脚本。


## Feature 周期表查询

### `kdo-tools/feature_menu.py`
- **功能**：从 96 个 AI 基本功 Feature 中按层级/维度/场景过滤点菜
- **命令**：`python kdo-tools/feature_menu.py list|query|pick|info`
- **使用场景**：#251 Agent 部署的数据源 / 消费端协议试点 / 老顽童 W1 生产点菜
- **运行**：
  ```bash
  python kdo-tools/feature_menu.py list                    # 全量 96 Feature
  python kdo-tools/feature_menu.py query --layer L2        # 按层级过滤
  python kdo-tools/feature_menu.py query --dimension A     # 按维度过滤
  python kdo-tools/feature_menu.py pick --n 5 --seed 42    # 随机点菜（可复现）
  python kdo-tools/feature_menu.py info F001               # 单 Feature 详情
  ```
- **登记日期**：2026-08-08
