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

## 3. 本机（KDO 运行环境）实测评估

### 3.1 硬件信息

| 项目 | 实测值 |
|---|---|
| GPU | NVIDIA GeForce GTX 1650 with Max-Q Design |
| 显存 | **4 GB**（实测空闲约 3.95 GB） |
| 驱动 | 546.33 |
| 系统内存 | 16 GB |

### 3.2 结论

**本机 4GB 显存无法本地运行 FLUX.1。**

FLUX.1 的最低门槛：
- FLUX.1 schnell 量化版：约 **6 GB 显存** 起步
- FLUX.1 dev FP8：约 **12 GB 显存** 起步
- FLUX.1 dev FP16：约 **24 GB 显存**

本机 GTX 1650 4GB 低于所有推荐下限，强行本地跑会 OOM 或频繁触发 CPU offload，生成一张图可能要数分钟到数十分钟，体验极差。

### 3.3 针对本机的可行方案

| 方案 | 说明 | 推荐度 |
|---|---|---|
| **云端 FLUX API** | fal.ai、Replicate、Together AI、Black Forest Labs 官方 API，按量付费 | ⭐⭐⭐⭐⭐ |
| **Midjourney** | 订阅制，云端生成，无需本地显存 | ⭐⭐⭐⭐ |
| **Stable Diffusion 1.5 / SDXL 轻量版** | 4GB 显存可跑 SD 1.5；SDXL 需进一步量化或 CPU 辅助 | ⭐⭐⭐ |
| **WSL CPU 跑 FLUX** | 用 `enable_model_cpu_offload()` 把模型塞进 16GB 内存，极慢，仅适合验证 | ⭐ |
| **Google Colab / Kaggle** | T4 16GB 可跑 FLUX schnell，适合偶尔批量生成 | ⭐⭐⭐ |

### 3.4 给 KDO 的建议

- **短期**：把 FLUX/Midjourney 放在云端 API 或在线服务，本地只负责 prompt 工程和结果归档。
- **中期**：如果预算允许，升级到 12GB+ 显存的机器（如 RTX 3060 12GB、4060 Ti 16GB），即可本地跑 FLUX.1 dev FP8。
- **长期**：KDO 流水线可设计成“本地 prompt + 云端生图 + 本地后处理”的混合架构，兼顾隐私与硬件成本。

---

## 5. 快速选型建议

| 场景 | 推荐工具 | 理由 |
|---|---|---|
| 想要“打开即用”、不折腾 | Midjourney Web / Discord | 无需硬件，质量高 |
| 本地隐私、批量、自动化 | FLUX.1 + ComfyUI | 开源可控，可脚本化 |
| 低显存、想接近 A1111 体验 | FLUX.1 + Forge | 界面熟悉，量化友好 |
| 程序化集成到 KDO 流水线 | FLUX.1 + diffusers | Python 原生，易调度 |
| 本机 4GB 显存想跑图 | 云端 API / Midjourney / Colab | 本地硬件不满足 FLUX 最低要求 |

---

## 6. 云端 API 价格对比（2026 年 6 月）

由于本机无法本地跑 FLUX，云端 API 是最现实方案。下面按 **每图成本** 排序：

| 服务商 | 模型 | 单价 | 备注 |
|---|---|---|---|
| **Runware** | FLUX.1 schnell | **$0.0013/张** | 目前最低，但公司较新、生态小 |
| **fal.ai** | FLUX.1 schnell | **$0.003/张** | 速度快、接口统一，新用户送 $10-$20 |
| **Replicate** | FLUX.1 schnell | **$0.003/张** | 社区模型多，文档好 |
| **Together AI** | FLUX | **$0.003/张** | 部分模型比 Replicate 便宜 10-17 倍 |
| fal.ai | FLUX.1 dev | $0.025/MP | 质量更高 |
| Replicate | FLUX 1.1 Pro | $0.04/张 | 生产级质量 |
| fal.ai | FLUX.1 Pro | $0.05/张 | 官方 Pro 质量 |

> 注：$0.003/张 ≈ 1000 张图 $3，对 KDO 批量生成封面/信息图非常友好。

### 推荐方案

- **主力：fal.ai FLUX.1 [schnell]**
  - 理由：价格与 Replicate 持平、速度更快、SDK 简洁、新账户有免费额度，适合 KDO 自动化流水线。
- **备用：Replicate FLUX.1 [schnell]**
  - 理由：文档完善、社区模型多，fal.ai 不可用时切换。
- **超低价尝试：Runware**
  - 如果预算极紧，可以先试，但需注意稳定性与账单透明度。

---

## 7. 已知坑点

- Midjourney 的“私人服务器”并不等于隐私；图默认公开。
- FLUX.1 dev 在 Windows 原生运行需 NVIDIA 驱动 + CUDA Toolkit 匹配 PyTorch 版本。
- 低显存跑 FP16 会 OOM，务必先选择 FP8 / NF4 / GGUF 量化版。
- AUTOMATIC1111 原版 **不支持** FLUX，请用 Forge 或 ComfyUI。
- Windows 11 的 Recall 功能可能截图保存本地生成的图；如在意隐私请关闭。

---

## 8. 下一步行动

1. ✅ 评估本机 GPU 显存（结论：4GB，不满足 FLUX 本地最低要求）。
2. ✅ 选择最便宜云端方案：fal.ai FLUX.1 [schnell]（$0.003/张，新用户 $10-$20 免费额度）。
3. ✅ 已提供 Python 脚本：`40_outputs/code/scripts/generate-images-fal.py`，填入 FAL_KEY 即可跑。
4. 注册 fal.ai 获取 API key，运行脚本生成 KDO 文章封面/信息图测试。
5. 如需本地轻量生图，尝试 Stable Diffusion 1.5 + 4GB 优化配置。
6. 如未来升级硬件（12GB+ 显存），再按本 skill 安装 ComfyUI + FLUX.1 dev FP8。

---

## 参考链接

- Midjourney 官方 Discord 邀请与 Bot 使用说明
- ComfyUI 官方仓库：https://github.com/comfyanonymous/ComfyUI
- FLUX.1 Hugging Face：https://huggingface.co/black-forest-labs
- Forge + FLUX 一键包与 nf4 模型（社区维护）
- 本地 FLUX 部署综合指南（2026）：https://localaimaster.com/blog/flux-local-image-generation
