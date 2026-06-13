# AI 图像生成工具安装调研

skill_name: ai-image-generation-setup  
status: stable  
scope: Multimodal Arbiter / 洪七公  
last_verified: 2026-06-13  

---

## 调研目标

回答两个核心问题：
1. 在本地或订阅环境中如何安装/使用 **Midjourney**？
2. 如何在本地安装并跑通 **FLUX.1**？

结论先行：
- **Midjourney**：目前无官方本地版，必须通过 Discord 或官方 Web/App 使用，需订阅。
- **FLUX.1**：可本地部署，推荐 **ComfyUI** 或 **Stable Diffusion WebUI Forge**；显存需求从 6GB（量化版）到 24GB（FP16 完整版）不等。

---

## 1. Midjourney

### 1.1 官方形态

- Midjourney 是 **云端闭源模型**，没有可下载的本地权重，也没有本地安装包。
- 所有生图请求都在 Midjourney 服务器上完成。

### 1.2 使用方式（2026 年仍有效）

| 方式 | 说明 | 费用 |
|---|---|---|
| **Discord Bot** | 在 Midjourney 官方 Discord 或把 Bot 邀请到自己的 Discord 服务器（<1000 人） | 订阅制 |
| **Midjourney Web / Alpha** | 浏览器访问 alpha.midjourney.com，界面生图 | 订阅制 |
| **第三方 API 封装** | 非官方，存在封号/数据风险，不推荐生产使用 | 按量付费 |

### 1.3 订阅与权限

- 必须有活跃订阅或试用才能调用 `/imagine`。
- 新用户首次使用 `/imagine` 会自动开启试用。
- 在私人服务器生成的图仍受 Midjourney 内容审核策略约束；除非开启 Stealth Mode，否则图会公开到 midjourney.com。

### 1.4 对 KDO 洪七公的意义

- 适合快速产出高质量概念图、封面、信息图。
- 不适合敏感/本地数据，也不适合批量自动化（无官方 API）。
- 建议把 Midjourney 作为“灵感/首稿工具”，再用 FLUX/Stable Diffusion 做本地精修。

---

## 2. FLUX.1（Black Forest Labs）

### 2.1 模型版本

| 版本 | 许可 | 质量 | 速度 | 推荐显存 |
|---|---|---|---|---|
| **FLUX.1 [pro]** | API 专用，不开源 | 最高 | 云端 | 不适用 |
| **FLUX.1 [dev]** | 开源，可商用 | 高 | 较慢 | 16-24 GB |
| **FLUX.1 [schnell]** | Apache-2.0，本地友好 | 中高 | 快（4 步蒸馏） | 6-16 GB |

### 2.2 推荐本地部署方案

#### 方案 A：ComfyUI（最灵活，推荐）

1. 安装 ComfyUI：
   ```bash
   git clone https://github.com/comfyanonymous/ComfyUI.git
   cd ComfyUI
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. 下载模型并放入对应目录：
   - 单文件 FP8：`ComfyUI/models/checkpoints/flux1-dev-fp8.safetensors`
   - 完整版拆散放置：
     - `models/unet/flux1-dev.safetensors`
     - `models/clip/clip_l.safetensors`
     - `models/clip/t5xxl_fp8_e4m3fn.safetensors`
     - `models/vae/ae.safetensors`
3. 启动：`python main.py`
4. 浏览器打开 `http://127.0.0.1:8188`，拖入 workflow JSON 即可。

#### 方案 B：Stable Diffusion WebUI Forge（界面友好）

1. 下载 Forge 一键包（CUDA 12.1 + PyTorch 2.3.1）。
2. 解压后依次运行 `update.bat`、`run.bat`。
3. 下载 FLUX 量化模型，例如 `flux1-dev-bnb-nf4`：
   - https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4
4. 放入 `models/Stable-diffusion/`，在 WebUI 中选择模型生图。

#### 方案 C：Python / diffusers（程序化）

```python
import torch
from diffusers import FluxPipeline

pipe = FluxPipeline.from_pretrained(
    "black-forest-labs/FLUX.1-dev",
    torch_dtype=torch.bfloat16
)
pipe.enable_model_cpu_offload()

image = pipe(
    "A photorealistic portrait of a woman, golden hour lighting, "
    "shot on Fujifilm X-T5, 35mm f/1.4",
    num_inference_steps=28,
    guidance_scale=3.5
).images[0]
image.save("output.png")
```

低显存可改用 4-bit 量化 + `BitsAndBytesConfig`。

### 2.3 显存与硬件对照

| 配置 | 可运行模型 | 备注 |
|---|---|---|
| 6 GB VRAM | FLUX.1 schnell GGUF Q4 / Forge nf4 | 慢，需量化 |
| 8 GB VRAM | FLUX.1 schnell FP8 / SDXL | 可接受 |
| 12 GB VRAM | FLUX.1 dev FP8 / Forge 量化版 | 推荐起点 |
| 16 GB VRAM | FLUX.1 dev FP8 单文件 | 较流畅 |
| 24 GB VRAM | FLUX.1 dev FP16 完整版 | 最佳质量 |

### 2.4 模型下载源

- Hugging Face：`black-forest-labs/FLUX.1-dev`、`black-forest-labs/FLUX.1-schnell`
- CivitAI：社区微调版、LoRA
- 国内镜像：ModelScope / hf-mirror.com

### 2.5 对 KDO 洪七公的意义

- 可本地批量生成信息图、封面、概念图，prompt 和图都不出本机。
- 与 ComfyUI 工作流结合，可自动化批量生成（配合 Markdown 元数据）。
- 推荐作为 KDO 视觉内容的主力生成引擎。

---

## 3. 快速选型建议

| 场景 | 推荐工具 | 理由 |
|---|---|---|
| 想要“打开即用”、不折腾 | Midjourney Web / Discord | 无需硬件，质量高 |
| 本地隐私、批量、自动化 | FLUX.1 + ComfyUI | 开源可控，可脚本化 |
| 低显存、想接近 A1111 体验 | FLUX.1 + Forge | 界面熟悉，量化友好 |
| 程序化集成到 KDO 流水线 | FLUX.1 + diffusers | Python 原生，易调度 |

---

## 4. 已知坑点

- Midjourney 的“私人服务器”并不等于隐私；图默认公开。
- FLUX.1 dev 在 Windows 原生运行需 NVIDIA 驱动 + CUDA Toolkit 匹配 PyTorch 版本。
- 低显存跑 FP16 会 OOM，务必先选择 FP8 / NF4 / GGUF 量化版。
- AUTOMATIC1111 原版 **不支持** FLUX，请用 Forge 或 ComfyUI。
- Windows 11 的 Recall 功能可能截图保存本地生成的图；如在意隐私请关闭。

---

## 5. 下一步行动

1. 评估本机 GPU 显存，决定跑哪个 FLUX 版本。
2. 在 WSL 或 Windows 安装 ComfyUI / Forge。
3. 下载一个 FLUX 模型（建议从 schnell 或 dev FP8 开始）。
4. 用 KDO 文章标题/摘要生成第一批测试图，验证 prompt 工程。

---

## 参考链接

- Midjourney 官方 Discord 邀请与 Bot 使用说明
- ComfyUI 官方仓库：https://github.com/comfyanonymous/ComfyUI
- FLUX.1 Hugging Face：https://huggingface.co/black-forest-labs
- Forge + FLUX 一键包与 nf4 模型（社区维护）
- 本地 FLUX 部署综合指南（2026）：https://localaimaster.com/blog/flux-local-image-generation
