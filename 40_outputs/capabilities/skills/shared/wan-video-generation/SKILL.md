---
name: wan-video-generation
description: "Wan 2.2 开源 AI 视频生成。阿里巴巴出品，Apache 2.0 完全商用。2026年开源视频质量之王——文本/图片→5秒高清视频，支持 GGUF 量化在 12GB 消费级 GPU 运行。通过 ComfyUI 节点集成。"
version: 1.0.0
category: creative
metadata:
  hermes:
    tags: [video-generation, ai-video, wan, alibaba, comfyui, open-source, text-to-video]
    related_skills:
      - beikai-multimodal-pipeline
      - comfyui-local
      - text-to-video-pipeline
      - cosyvoice-tts
  env:
    WAN_MODEL_DIR: "Wan 模型存放目录"
---

# Wan 2.2 — 开源 AI 视频生成

> "叫花子以前做视频，全仗 hyperframes HTML 硬画。现在有了 Wan 2.2——一段文字进去，五秒视频出来。丐帮也有了自己的摄影棚。" — 洪七公

## 定位

北丐视频武器库的**生成引擎**，替换不可用的 manim-video，补充 hyperframes 的 AI 能力：

| 维度 | hyperframes（旧） | manim-video（断剑） | Wan 2.2（新） |
|:--|:--|:--|:--|
| 生成方式 | HTML → 截图 → 合成 | Python 程序化动画 | **AI 文本→视频** |
| 风格 | 自定义 HTML 设计 | 3B1B 数学动画 | 真实世界视频 |
| 内容自由度 | 需自写 HTML | 需自写代码 | **自然语言驱动** |
| 中文理解 | 手动 | 手动 | ✅ 原生中文 |
| 分辨率 | 1080p | 1080p | 480p-720p（可上采样 4K） |
| 速度 | 实时渲染 | 慢 | 4-8分钟/5秒 |
| 许可证 | MIT | MIT | **Apache 2.0** |

## 技术规格

| 维度 | Wan 1.3B | Wan 14B |
|:--|:--|:--|
| 开发者 | 阿里巴巴 | 阿里巴巴 |
| 许可证 | Apache 2.0 | Apache 2.0 |
| 分辨率 | 480p | 480p/720p |
| 帧率 | 24 FPS | 24 FPS |
| 时长 | ~5秒 | ~5秒 |
| VRAM（标准） | ~8GB | ~24GB+ |
| VRAM（GGUF Q5量化） | — | ~11GB |
| VRAM（GGUF Q3/Q4） | — | ~7-10GB |
| 速度 RTX 4090 | ~4分钟 | ~4-8分钟 |
| 能力 | 文生视频 | 文生视频 + 图生视频 |

> 2026年2月发布的 Wan 2.2 增加 MoE 变体（A14B），质量提升显著。
> InsiderLLM 评测：14B 模型在社交媒体和 B-roll 场景下与 Runway Gen-4 竞争力相当。

## 安装

### 硬件前提
```bash
nvidia-smi  # 确认 GPU 可用
# 最低: 12GB VRAM + CUDA 11.8+
# 推荐: 24GB VRAM (RTX 3090/4090)
```

### 通过 ComfyUI（推荐）

```bash
# ComfyUI 已安装的前提下：
# 1. 下载 Wan 2.2 模型到 ComfyUI models 目录
cd ComfyUI/models/diffusion_models/
wget https://huggingface.co/.../wan2.2-14b-fp16.safetensors

# 2. 通过 ComfyUI Manager 安装 Wan 节点
#    UI → Manager → Install Missing Custom Nodes → 搜索 "Wan"

# 3. 从 ComfyHub 加载 Wan 2.2 工作流
#    https://comfy.org/workflows → 搜索 "Wan 2.2"
#    拖入 ComfyUI 即可使用
```

### 独立安装（可选）

```bash
git clone https://github.com/Wan-Video/Wan2.2.git
cd Wan2.2
pip install -r requirements.txt

# 下载模型
huggingface-cli download Wan-AI/Wan2.2-14B --local-dir models/
```

## 快速使用

### 文生视频（ComfyUI 工作流）

```
工作流节点链:
[CLIP Text Encode] → [Wan 2.2 Sampler]
    → [VAE Decode] → [Video Save]

参数:
  模型: Wan2.2-14B (GGUF Q5 可用 12GB)
  步数: 20-30
  CFG: 7.0
  分辨率: 480p (1.3B) / 720p (14B)
  时长: 5秒 / 120帧
```

### 图生视频

```
[Load Image] → [CLIP Vision Encode]
    → [Wan 2.2 Sampler (I2V模式)]
    → [VAE Decode] → [Video Save]

用途:
  - 静态信息图 → 动态展示
  - 产品图 → 360°展示视频
  - 封面图 → 视频开头动画
```

### Python API（通过 ComfyUI）

```python
"""批量文生视频"""
import json, urllib.request

COMFYUI = "http://localhost:8188"

# 加载 Wan 2.2 工作流模板
with open("workflows/wan2.2_text2video.json") as f:
    workflow = json.load(f)

# 修改提示词
scenes = [
    "武林高手在华山之巅打出一招降龙十八掌，金色龙形气劲爆发，电影级画质",
    "未来城市夜景，霓虹灯闪烁，飞行汽车穿梭，赛博朋克风格",
    "江南水乡清晨，薄雾笼罩，小桥流水，国风水墨画风格",
]

for i, prompt in enumerate(scenes):
    # 找到文本编码节点并修改
    for node in workflow.values():
        if node.get("class_type") == "CLIPTextEncode":
            node["inputs"]["text"] = prompt
    
    req = urllib.request.Request(
        f"{COMFYUI}/prompt",
        data=json.dumps({"prompt": workflow}).encode(),
        headers={"Content-Type": "application/json"}
    )
    prompt_id = json.loads(urllib.request.urlopen(req).read())["prompt_id"]
    print(f"[{i+1}/{len(scenes)}] {prompt_id}: {prompt[:40]}...")
```

## 视频后处理

### RTX Video Super Resolution 4K 升频

```python
# ComfyUI 节点
"""
[Load Video] → [RTX Video Super Resolution]
    → [4K Upscale] → [Video Save]

480p → 4K（实时，需要 RTX 40/50 系列）
"""
```

### 音视频合成

```python
# Wan 2.2 生成视频 + CosyVoice 3.0 生成配音 + ffmpeg 合成
import subprocess

def merge_video_audio(video_path: str, audio_path: str, output_path: str):
    subprocess.run([
        "ffmpeg", "-i", video_path, "-i", audio_path,
        "-c:v", "copy", "-c:a", "aac", "-shortest",
        "-y", output_path
    ])
```

## 集成到北丐流水线

### 文章→AI视频（新 pipeline）

```
文章 Markdown
│
├── 1. LLM 拆解脚本 → 5段场景描述
├── 2. Wan 2.2 逐段生成视频素材（每段5秒）
├── 3. CosyVoice 3.0 生成配音（克隆品牌声音）
├── 4. hyperframes 拼接触屏/转场/字幕
└── 5. ffmpeg 合成成品 MP4
```

### 与 hyperframes 分工

| 场景 | 用 hyperframes | 用 Wan 2.2 |
|:--|:--|:--|
| 片头/片尾卡 | ✅ 精确排版 | — |
| 金句字幕 | ✅ 字体动画 | — |
| B-roll 视频 | — | ✅ AI 生成 |
| 场景插画 | — | ✅ AI 生成 |
| 转场/过渡 | ✅ GSAP 动画 | — |
| 数据可视化 | ✅ p5.js | — |

## 提示词技巧

### 中文 Wano 最佳实践

```
# ✅ 好的提示词
"未来科技实验室，银白色金属质感，蓝色全息投影，主角正在操作悬浮界面，电影级光影"

# ❌ 差的提示词
"科技"  # 太短

# 关键要素：场景 + 动作 + 风格 + 画质词
- 场景：室内/室外/太空/水下
- 动作：行走/飞行/操作/对话
- 风格：赛博朋克/水墨/电影级/写实
- 画质：4K/电影级/虚幻引擎/octane render
```

### 图生视频提示词

```
"保持原图构图，镜头缓慢推进，增加微小动态（树叶摇曳/水流/光晕变化）"
```

## 性能基准

| GPU | 模型 | 5秒视频耗时 | VRAM |
|:--|:--|:--|:--|
| RTX 3060 12GB | Wan 1.3B | ~10分钟 | 8GB |
| RTX 3060 12GB | Wan 14B GGUF Q4 | ~15分钟 | 10GB |
| RTX 4090 24GB | Wan 1.3B | ~4分钟 | 8GB |
| RTX 4090 24GB | Wan 14B | ~4-8分钟 | 24GB |
| RTX A6000 48GB | Wan 14B | ~3分钟 | 24GB |
| H100 80GB | Wan 14B | ~1分钟 | 24GB |

> 来源: InsiderLLM 2026-02, LTX Blog 2026-05

## 常见坑点

### Pitfall 1: GGUF 量化模型加载失败
```bash
# 依赖 llama.cpp 的 gguf 支持
pip install llama-cpp-python
# WSL 下可能需要手动编译 CUDA 版本
CMAKE_ARGS="-DGGML_CUDA=on" pip install llama-cpp-python
```

### Pitfall 2: ComfyUI 中 Wan 节点缺失
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/kijai/ComfyUI-WanVideoWrapper.git
# 重启 ComfyUI
```

### Pitfall 3: 视频结果闪烁/跳帧
调低 CFG 值（5-7），增加采样步数（25-30），使用 Wan 2.2 而非 2.1。

### Pitfall 4: 图片比例不对
Wan 2.2 原生支持 16:9（1280×720）。其他比例需先裁剪/填充图片。

### Pitfall 5: 长视频生成
单次限制 5 秒，长视频需拼接。ComfyHub 有"Wan 2.2 Extend Video"工作流可自动衔接。

## 验证清单

- [ ] ComfyUI 中 Wan 2.2 节点可用
- [ ] 文生视频 5 秒无报错
- [ ] 图生视频正常转换
- [ ] GGUF 量化在 12GB GPU 可跑
- [ ] RTX VSR 升频 4K 可用

## 参考资料

- GitHub: https://github.com/Wan-Video/Wan2.2
- ComfyUI 节点: https://github.com/kijai/ComfyUI-WanVideoWrapper
- InsiderLLM 评测: https://insiderllm.com/guides/local-ai-video-generation
- LTX Blog 对比: https://ltx.io/blog/best-open-source-video-generation-models
